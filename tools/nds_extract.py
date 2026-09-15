#!/usr/bin/env python3
"""Verified Nintendo DS component extractor for local reverse-engineering work.

The retail ROM is an input only. Output belongs under an ignored local directory
(e.g. build/extracted/) and is not intended to be committed verbatim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path, PurePosixPath

CHUNK = 1024 * 1024


def u16(buf: bytes, off: int) -> int:
    return struct.unpack_from("<H", buf, off)[0]


def u32(buf: bytes, off: int) -> int:
    return struct.unpack_from("<I", buf, off)[0]


def digest_file(path: Path) -> dict[str, str]:
    hs = {name: hashlib.new(name) for name in ("md5", "sha1", "sha256")}
    with path.open("rb") as f:
        for block in iter(lambda: f.read(CHUNK), b""):
            for h in hs.values():
                h.update(block)
    return {name: h.hexdigest() for name, h in hs.items()}


def digest_bytes(data: bytes) -> dict[str, str]:
    return {"md5": hashlib.md5(data).hexdigest(), "sha1": hashlib.sha1(data).hexdigest(), "sha256": hashlib.sha256(data).hexdigest()}


def load_baseline(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def verify_target(rom_path: Path, baseline: dict) -> None:
    expected_size = baseline.get("file_size")
    actual_size = rom_path.stat().st_size
    if expected_size is not None and actual_size != expected_size:
        raise SystemExit(f"size mismatch: expected {expected_size}, got {actual_size}")
    actual = digest_file(rom_path)
    expected = baseline.get("hashes", {})
    mismatches = [k for k in ("md5", "sha1", "sha256") if expected.get(k) and expected[k].lower() != actual[k].lower()]
    if mismatches:
        details = ", ".join(f"{k}: expected {expected[k]} got {actual[k]}" for k in mismatches)
        raise SystemExit(f"target hash mismatch: {details}")


def parse_fat(rom: bytes, off: int, size: int) -> list[tuple[int, int]]:
    if size % 8:
        raise ValueError(f"FAT size is not a multiple of 8: 0x{size:X}")
    return [struct.unpack_from("<II", rom, off + i * 8) for i in range(size // 8)]


def parse_fnt(rom: bytes, off: int, size: int, fat: list[tuple[int, int]]) -> list[dict]:
    fnt = rom[off : off + size]
    if len(fnt) < 8:
        return []
    dir_count = u16(fnt, 6)
    dirs: dict[int, tuple[int, int, int]] = {}
    for i in range(dir_count):
        p = i * 8
        if p + 8 > len(fnt):
            raise ValueError("FNT directory table extends beyond FNT")
        dirs[0xF000 + i] = (u32(fnt, p), u16(fnt, p + 4), u16(fnt, p + 6))
    files: list[dict] = []
    active: set[int] = set()

    def walk(dir_id: int, prefix: str) -> None:
        if dir_id in active:
            raise ValueError(f"FNT directory cycle at 0x{dir_id:04X}")
        if dir_id not in dirs:
            raise ValueError(f"FNT references missing directory 0x{dir_id:04X}")
        active.add(dir_id)
        subtable, file_id, _parent = dirs[dir_id]
        pos = subtable
        while pos < len(fnt):
            tag = fnt[pos]
            pos += 1
            if tag == 0:
                break
            is_dir = bool(tag & 0x80)
            name_len = tag & 0x7F
            if pos + name_len > len(fnt):
                raise ValueError("truncated FNT name")
            name = fnt[pos : pos + name_len].decode("ascii", "strict")
            pos += name_len
            if is_dir:
                if pos + 2 > len(fnt):
                    raise ValueError("truncated FNT directory reference")
                child = u16(fnt, pos)
                pos += 2
                walk(child, prefix + name + "/")
            else:
                if file_id >= len(fat):
                    raise ValueError(f"FNT file id {file_id} exceeds FAT")
                start, end = fat[file_id]
                files.append({"file_id": file_id, "path": prefix + name, "start": start, "end": end, "size": end - start})
                file_id += 1
        active.remove(dir_id)

    walk(0xF000, "")
    return files


def parse_overlays(rom: bytes, table_off: int, table_size: int, fat: list[tuple[int, int]]) -> list[dict]:
    if table_size % 32:
        raise ValueError(f"overlay table size is not a multiple of 32: 0x{table_size:X}")
    out = []
    for i in range(table_size // 32):
        p = table_off + i * 32
        overlay_id, ram_address, ram_size, bss_size, static_start, static_end, file_id, flags = struct.unpack_from("<8I", rom, p)
        if file_id >= len(fat):
            raise ValueError(f"overlay {overlay_id} references file id {file_id} beyond FAT")
        start, end = fat[file_id]
        out.append({"overlay_id": overlay_id, "ram_address": ram_address, "ram_size": ram_size, "bss_size": bss_size, "static_init_start": static_start, "static_init_end": static_end, "file_id": file_id, "flags": flags, "rom_start": start, "rom_end": end, "file_size": end - start})
    return out


def safe_output(root: Path, rel: str) -> Path:
    p = PurePosixPath(rel)
    if p.is_absolute() or any(part in ("", ".", "..") for part in p.parts):
        raise ValueError(f"unsafe NitroFS path: {rel!r}")
    out = root.joinpath(*p.parts)
    out.parent.mkdir(parents=True, exist_ok=True)
    return out


def write_blob(path: Path, data: bytes, *, offset: int | None = None, extra: dict | None = None) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    rec = {"path": path.as_posix(), "size": len(data), "hashes": digest_bytes(data)}
    if offset is not None:
        rec["rom_offset"] = offset
    if extra:
        rec.update(extra)
    return rec


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("rom", type=Path)
    ap.add_argument("--baseline", type=Path, default=Path("manifests/rom-baseline.json"))
    ap.add_argument("--out", type=Path, default=Path("build/extracted"))
    ap.add_argument("--no-nitrofs", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    baseline = load_baseline(args.baseline)
    verify_target(args.rom, baseline)
    rom = args.rom.read_bytes()
    hdr = rom[:0x200]
    fat_off, fat_size = u32(hdr, 0x48), u32(hdr, 0x4C)
    fnt_off, fnt_size = u32(hdr, 0x40), u32(hdr, 0x44)
    fat = parse_fat(rom, fat_off, fat_size)
    files = parse_fnt(rom, fnt_off, fnt_size, fat)
    ov9 = parse_overlays(rom, u32(hdr, 0x50), u32(hdr, 0x54), fat)
    ov7 = parse_overlays(rom, u32(hdr, 0x58), u32(hdr, 0x5C), fat)
    summary = {"target": {"title": hdr[:12].split(b"\0", 1)[0].decode("ascii", "replace"), "game_code": hdr[0x0C:0x10].decode("ascii", "replace"), "rom_version_byte": hdr[0x1E], "verified_hashes": baseline.get("hashes", {})}, "arm9": {"rom_offset": u32(hdr, 0x20), "size": u32(hdr, 0x2C), "load_address": u32(hdr, 0x28), "entry_address": u32(hdr, 0x24)}, "arm7": {"rom_offset": u32(hdr, 0x30), "size": u32(hdr, 0x3C), "load_address": u32(hdr, 0x38), "entry_address": u32(hdr, 0x34)}, "nitrofs_file_count": len(files), "arm9_overlay_count": len(ov9), "arm7_overlay_count": len(ov7)}
    if args.dry_run:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return
    out = args.out
    out.mkdir(parents=True, exist_ok=True)
    manifest = dict(summary)
    manifest["components"] = []
    a9o, a9s = u32(hdr, 0x20), u32(hdr, 0x2C)
    a7o, a7s = u32(hdr, 0x30), u32(hdr, 0x3C)
    manifest["components"].append(write_blob(out / "arm9.bin", rom[a9o : a9o + a9s], offset=a9o))
    manifest["components"].append(write_blob(out / "arm7.bin", rom[a7o : a7o + a7s], offset=a7o))
    for cpu, rows in (("arm9", ov9), ("arm7", ov7)):
        for rec in rows:
            data = rom[rec["rom_start"] : rec["rom_end"]]
            manifest["components"].append(write_blob(out / "overlays" / cpu / f"overlay_{rec['overlay_id']:03d}.bin", data, offset=rec["rom_start"], extra={"overlay_id": rec["overlay_id"], "load_address": rec["ram_address"], "ram_size": rec["ram_size"], "bss_size": rec["bss_size"]}))
    if not args.no_nitrofs:
        fs_root = out / "nitrofs"
        for rec in files:
            data = rom[rec["start"] : rec["end"]]
            dest = safe_output(fs_root, rec["path"])
            manifest["components"].append(write_blob(dest, data, offset=rec["start"], extra={"file_id": rec["file_id"], "nitrofs_path": rec["path"]}))
    (out / "extraction-manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "arm9-overlays.json").write_text(json.dumps(ov9, indent=2) + "\n", encoding="utf-8")
    (out / "arm7-overlays.json").write_text(json.dumps(ov7, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
