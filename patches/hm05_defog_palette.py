#!/usr/bin/env python3
"""Fix G4-UI-003 (HM05 Defog uses the Water palette) for the exact ADAE Rev 5 target."""
import argparse
import hashlib
import struct
from pathlib import Path

EXPECTED_SHA256 = "e29bc6ebe431d7a6b238267b6b1521fec4a3bc14f2fa348798062f870c738454"
TABLE_ARM9_REL = 0xF938C
TABLE_FIRST_ITEM = 420
HM02 = 421
HM05 = 424
WATER_PALETTE_ID = 358
FLYING_PALETTE_ID = 350


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def entry_offset(arm9_off, item_id):
    return arm9_off + TABLE_ARM9_REL + (item_id - TABLE_FIRST_ITEM) * 8


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    args = ap.parse_args()

    data = bytearray(Path(args.input).read_bytes())
    if sha256(data) != EXPECTED_SHA256:
        raise SystemExit("input SHA-256 does not match the exact ADAE Rev 5 baseline")

    arm9_off = struct.unpack_from("<I", data, 0x20)[0]
    hm02 = entry_offset(arm9_off, HM02)
    hm05 = entry_offset(arm9_off, HM05)
    hm02_id, _, hm02_palette, _ = struct.unpack_from("<HHHH", data, hm02)
    hm05_id, _, hm05_palette, _ = struct.unpack_from("<HHHH", data, hm05)
    if (hm02_id, hm02_palette) != (HM02, FLYING_PALETTE_ID):
        raise SystemExit("HM02/Flying reference entry does not match expected table data")
    if (hm05_id, hm05_palette) != (HM05, WATER_PALETTE_ID):
        raise SystemExit("HM05 entry does not match the known buggy table data")

    struct.pack_into("<H", data, hm05 + 4, FLYING_PALETTE_ID)
    Path(args.output).write_bytes(data)
    print(sha256(data))


if __name__ == "__main__":
    main()
