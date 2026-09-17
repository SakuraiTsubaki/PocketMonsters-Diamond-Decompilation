# ROM structure inventory: Pokémon Diamond Version (USA, ADAE, header ROM version 5)

## Provenance

- Tool: `nds_rom_analyzer 1.0.0`
- Input basename: `Pokemon_Diamond_USA_NDS-LGC.nds`
- Input SHA-256: `e29bc6ebe431d7a6b238267b6b1521fec4a3bc14f2fa348798062f870c738454`
- ROM bytes committed: no
- Confidence: **Confirmed** for directly parsed offsets, fields, hashes, and CRC results.

## Core structure

| Field | Value |
| --- | --- |
| Game code | `ADAE` |
| ROM/header size | `67108864` / `16384` bytes |
| ARM9 ROM / RAM / entry / size | `0x4000` / `0x02000000` / `0x02000800` / `1079076` |
| ARM7 ROM / RAM / entry / size | `0x30d000` / `0x02380000` / `0x02380000` / `168732` |
| FNT / FAT files / directories | `0x336400` / `356` / `69` |
| ARM9 / ARM7 overlays | `87` / `0` |
| NARC archives | `149` |
| Recognized signatures | `208` |
| Header/logo CRC valid | `True` / `True` |
| Structural validation checks | `True` |
| Secure-area raw encrypted bytes / decrypted CRC validation | `25be33695b95ed688fc83d62be4baa4930f5d430c4e28e42e1fb67adb3890f7a` / `not performed` |

## Outputs

- `structure.json`: complete machine-readable inventory.
- `nitrofs-files.csv`: every FAT file with path, offsets, size, SHA-256, extension, and detected signature.
- `directories.csv`: complete FNT directory table.
- `overlays-arm9.csv` and `overlays-arm7.csv`: complete overlay tables and RAM placement.
- `unreferenced-ranges.csv`: physical gaps and trailing padding. `unreferenced` does not prove unused.

## Reproduction

```console
python tools/nds_rom_analyzer/analyzer.py /path/to/input.nds --output analysis/generated/rom-structure --label "Pokémon Diamond Version (USA, ADAE, header ROM version 5)"
```

## Unknowns

The secure-area bytes and header checksum field are recorded, but decrypted secure-area CRC validation is not performed; a mismatch against CRC of encrypted raw bytes is not corruption evidence. Magic detection identifies only known leading signatures and compression markers. Unknown or extensionless files remain unclassified rather than receiving inferred names. Semantic analysis of NARC members, text, maps, scripts, Pokémon, moves, and items is deferred.
