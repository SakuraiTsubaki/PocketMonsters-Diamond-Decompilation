# Decompilation Baseline — Diamond

This document records the first ROM-derived structural baseline for **Diamond**.

## Target identity

- Game title field: `POKEMON D`
- Game code: `ADAE`
- Region / language: USA / English
- Header ROM version byte: `5`
- ROM size: `67108864` bytes
- SHA-256: `e29bc6ebe431d7a6b238267b6b1521fec4a3bc14f2fa348798062f870c738454`
- SHA-1: `a46233d8b79a69ea87aa295a0efad5237d02841e`
- MD5: `02a1af2a677d101394b1d99164a8c249`
- Verification status: **Verified against pret/pokediamond SHA-1 target**

## Executable layout

- ARM9: ROM offset `0x4000`, size `1079076` bytes, RAM `0x02000000`, entry `0x02000800`
- ARM7: ROM offset `0x30D000`, size `168732` bytes, RAM `0x02380000`, entry `0x02380000`
- ARM9 overlays: `87`
- ARM7 overlays: `0`

## NitroFS / FAT

- FAT entries: `356`
- NitroFS named files: `269`
- Verified boundary: FAT entries = ARM9 overlays + NitroFS files = `87 + 269 = 356`
- Header CRC matches: `true`

### Top-level NitroFS counts

- `data`: 134
- `graphic`: 42
- `poketool`: 24
- `fielddata`: 16
- `battle`: 11
- `wazaeffect`: 9
- `demo`: 8
- `application`: 6
- `arc`: 6
- `contest`: 3
- `itemtool`: 3
- `msgdata`: 2
- `resource`: 2
- `dwc`: 1
- `particledata`: 1
- `pokeanime`: 1

## Diamond ↔ Pearl first-pass differential

- Shared NitroFS files with identical bytes: `268`
- Path-only version split: one `personal.narc` path per version
- The version-specific personal NARC contains 501 members; 6 member records differ (indices 125, 126, 239, 240, 466, 467).
- ARM7 identical: `true`
- ARM9 identical: `false`
- Differing ARM9 overlay IDs: `5, 6, 7, 8, 11, 12, 16, 17, 18, 48, 54, 62, 63, 64, 80, 81, 83, 84`

## Evidence status

- **Observed**: Values above were parsed directly from the supplied ROM image.
- **Reproduced**: Header CRC verification and FAT/overlay/NitroFS accounting were reproduced by `tools/nds_inventory.py`.
- **Matched**: Only targets explicitly noted as externally hash-matched should be treated as preservation-verified.

Raw ROM images are not stored in this repository.
