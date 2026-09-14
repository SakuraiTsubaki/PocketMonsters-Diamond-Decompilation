#!/usr/bin/env python3
"""Emit a reproducible Nintendo DS ROM baseline inventory as JSON.

The tool records identifiers, whole-ROM hashes, executable/table offsets, NitroFS
counts, and banner metadata. It does not extract or redistribute ROM contents.
"""
from __future__ import annotations
import argparse
import collections
import hashlib
import json
import os
import struct
import zlib


def u16(data: bytes, off: int) -> int:
    return struct.unpack_from('<H', data, off)[0]


def u32(data: bytes, off: int) -> int:
    return struct.unpack_from('<I', data, off)[0]


def hashes(data: bytes) -> dict[str, str]:
    return {
        'crc32': f'{zlib.crc32(data) & 0xffffffff:08x}',
        'md5': hashlib.md5(data).hexdigest(),
        'sha1': hashlib.sha1(data).hexdigest(),
        'sha256': hashlib.sha256(data).hexdigest(),
    }


def parse_fnt(rom: bytes, fnt_off: int, fnt_size: int, fat_off: int, fat_size: int):
    fnt = rom[fnt_off:fnt_off + fnt_size]
    dir_count = u16(fnt, 6) if len(fnt) >= 8 else 0
    dirs = [struct.unpack_from('<IHH', fnt, i * 8) for i in range(dir_count)]
    entries = {}
    for idx, (sub_off, first_file_id, _parent) in enumerate(dirs):
        p = sub_off
        file_id = first_file_id
        cur = []
        while p < len(fnt):
            flags_len = fnt[p]
            p += 1
            if flags_len == 0:
                break
            is_dir = bool(flags_len & 0x80)
            name_len = flags_len & 0x7f
            name = fnt[p:p + name_len].decode('ascii', 'replace')
            p += name_len
            if is_dir:
                child_id = u16(fnt, p) - 0xf000
                p += 2
                cur.append(('dir', name, child_id))
            else:
                cur.append(('file', name, file_id))
                file_id += 1
        entries[idx] = cur

    paths = {}
    def walk(dir_id: int, prefix: str):
        for kind, name, value in entries.get(dir_id, []):
            if kind == 'file':
                paths[value] = prefix + name
            else:
                walk(value, prefix + name + '/')
    if dirs:
        walk(0, '')

    fat = [struct.unpack_from('<II', rom, fat_off + i * 8) for i in range(fat_size // 8)]
    return paths, fat, dir_count


def parse_banner(rom: bytes, off: int) -> dict:
    if not off or off + 0x840 > len(rom):
        return {}
    version = u16(rom, off)
    title_count = 6 if version == 1 else 7 if version == 2 else 8
    langs = ['ja', 'en', 'fr', 'de', 'it', 'es', 'zh', 'ko']
    titles = {}
    for i, lang in enumerate(langs[:title_count]):
        raw = rom[off + 0x240 + i * 0x100: off + 0x340 + i * 0x100]
        text = raw.decode('utf-16le', 'replace').split('\x00', 1)[0]
        if text:
            titles[lang] = text
    return {'version': version, 'titles': titles}


def inventory(path: str) -> dict:
    rom = open(path, 'rb').read()
    h = rom[:0x200]
    fnt_off, fnt_size, fat_off, fat_size = struct.unpack_from('<IIII', h, 0x40)
    ov9_off, ov9_size, ov7_off, ov7_size = struct.unpack_from('<IIII', h, 0x50)
    paths, fat, dir_count = parse_fnt(rom, fnt_off, fnt_size, fat_off, fat_size)
    ext_counts = collections.Counter()
    top_counts = collections.Counter()
    for file_id, (start, end) in enumerate(fat):
        name = paths.get(file_id, f'__unnamed__/{file_id:04d}')
        top_counts[name.split('/', 1)[0]] += 1
        ext_counts[os.path.splitext(name)[1].lower() or '<none>'] += 1
    return {
        'filename': os.path.basename(path),
        'size_bytes': len(rom),
        'hashes': hashes(rom),
        'header': {
            'title': h[:12].rstrip(b'\0').decode('ascii', 'replace'),
            'game_code': h[0x0c:0x10].decode('ascii', 'replace'),
            'maker_code': h[0x10:0x12].decode('ascii', 'replace'),
            'unit_code': h[0x12],
            'device_capacity': h[0x14],
            'rom_version': h[0x1e],
            'arm9': {'offset': u32(h,0x20), 'entry': u32(h,0x24), 'ram': u32(h,0x28), 'size': u32(h,0x2c)},
            'arm7': {'offset': u32(h,0x30), 'entry': u32(h,0x34), 'ram': u32(h,0x38), 'size': u32(h,0x3c)},
            'fnt': {'offset': fnt_off, 'size': fnt_size},
            'fat': {'offset': fat_off, 'size': fat_size},
            'overlay9': {'offset': ov9_off, 'size': ov9_size, 'count': ov9_size // 32},
            'overlay7': {'offset': ov7_off, 'size': ov7_size, 'count': ov7_size // 32},
            'banner_offset': u32(h, 0x68),
            'used_rom_size': u32(h, 0x80),
            'header_size': u32(h, 0x84),
        },
        'nitrofs': {
            'directory_count': dir_count,
            'fat_file_count': len(fat),
            'named_file_count': len(paths),
            'top_level_counts': dict(sorted(top_counts.items())),
            'extension_counts': dict(sorted(ext_counts.items())),
        },
        'banner': parse_banner(rom, u32(h, 0x68)),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('rom')
    ap.add_argument('-o', '--output')
    args = ap.parse_args()
    text = json.dumps(inventory(args.rom), ensure_ascii=False, indent=2) + '\n'
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(text)
    else:
        print(text, end='')

if __name__ == '__main__':
    main()
