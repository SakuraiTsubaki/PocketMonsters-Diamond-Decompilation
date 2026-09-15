#!/usr/bin/env python3
"""Verify the local target ROM and extract ARM9/ARM7 into ignored build output."""
from __future__ import annotations
import argparse, hashlib, json, struct
from pathlib import Path

CHUNK = 1024 * 1024

def u32(buf: bytes, off: int) -> int:
    return struct.unpack_from("<I", buf, off)[0]

def hashes(path: Path) -> dict[str, str]:
    hs = {n: hashlib.new(n) for n in ("md5", "sha1", "sha256")}
    with path.open("rb") as f:
        for block in iter(lambda: f.read(CHUNK), b""):
            for h in hs.values(): h.update(block)
    return {n: h.hexdigest() for n, h in hs.items()}

def bytes_hashes(data: bytes) -> dict[str, str]:
    return {n: hashlib.new(n, data).hexdigest() for n in ("md5", "sha1", "sha256")}

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("rom", type=Path)
    ap.add_argument("--baseline", type=Path, default=Path("manifests/rom-baseline.json"))
    ap.add_argument("--out", type=Path, default=Path("build/extracted/executable"))
    args = ap.parse_args()
    baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
    if args.rom.stat().st_size != baseline["file_size"]:
        raise SystemExit("target size does not match manifests/rom-baseline.json")
    actual = hashes(args.rom)
    for name, expected in baseline["hashes"].items():
        if actual.get(name, "").lower() != expected.lower():
            raise SystemExit(f"target {name} mismatch")
    rom = args.rom.read_bytes(); hdr = rom[:0x200]
    specs = {
        "arm9": (u32(hdr,0x20), u32(hdr,0x2C), u32(hdr,0x28), u32(hdr,0x24)),
        "arm7": (u32(hdr,0x30), u32(hdr,0x3C), u32(hdr,0x38), u32(hdr,0x34)),
    }
    args.out.mkdir(parents=True, exist_ok=True); manifest = {"target_hashes": actual, "components": {}}
    for name, (off, size, load, entry) in specs.items():
        if off + size > len(rom): raise SystemExit(f"{name} range exceeds ROM")
        data = rom[off:off+size]; (args.out/f"{name}.bin").write_bytes(data)
        manifest["components"][name] = {"rom_offset":off,"size":size,"load_address":load,"entry_address":entry,"hashes":bytes_hashes(data)}
    (args.out/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(manifest,indent=2))

if __name__ == "__main__": main()
