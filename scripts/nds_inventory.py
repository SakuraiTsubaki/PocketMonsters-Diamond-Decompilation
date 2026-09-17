#!/usr/bin/env python3
"""Print a deterministic metadata/hash summary for a Nintendo DS image."""
import argparse, hashlib, json, struct, zlib
from pathlib import Path

def u32(data, off):
    return struct.unpack_from('<I', data, off)[0]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def inspect(path):
    p = Path(path)
    data = p.read_bytes()
    if len(data) < 0x200:
        raise ValueError('input is too small for an NDS image')
    arm9_off, arm9_size = u32(data, 0x20), u32(data, 0x2C)
    arm7_off, arm7_size = u32(data, 0x30), u32(data, 0x3C)
    fat_size = u32(data, 0x4C)
    return {
        'input_name': p.name,
        'title': data[:12].rstrip(b'\0').decode('ascii', 'replace'),
        'game_code': data[12:16].decode('ascii', 'replace'),
        'rom_version': data[0x1E],
        'size': len(data),
        'crc32': f'{zlib.crc32(data) & 0xffffffff:08x}',
        'sha256': digest(data),
        'arm9_sha256': digest(data[arm9_off:arm9_off + arm9_size]),
        'arm7_sha256': digest(data[arm7_off:arm7_off + arm7_size]),
        'fat_file_count': fat_size // 8,
        'arm9_overlay_count': u32(data, 0x54) // 32,
        'arm7_overlay_count': u32(data, 0x5C) // 32,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('rom', nargs='+')
    ap.add_argument('-o', '--output')
    args = ap.parse_args()
    text = json.dumps([inspect(p) for p in args.rom], indent=2) + '\n'
    if args.output:
        Path(args.output).write_text(text, encoding='utf-8')
    else:
        print(text, end='')

if __name__ == '__main__':
    main()
