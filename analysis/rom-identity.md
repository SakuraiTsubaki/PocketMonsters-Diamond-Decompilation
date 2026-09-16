# Analysis: ROM identity baseline

## Target and applicability

This record applies only to the selected Pokémon Diamond Version input identified by the
complete-file hashes below. The user-supplied ROM remains outside Git.

## Claim

The repository target is the USA English Nintendo DS build with
game code `ADAE` and raw header ROM-version byte `5`.
Complete-file SHA-1 matches the documented pokediamond.us.nds build target.

## Evidence

| Field | Observed value |
| --- | --- |
| Header title | `POKEMON D` |
| Game code | `ADAE` |
| Maker code | `01` |
| Unit code | `0` |
| Device-capacity exponent | `9` |
| Nominal and actual size | `67108864` bytes |
| Header ROM version | `5` |
| Header CRC-16 | stored `ca37`, calculated `ca37`, valid |
| SHA-256 | `e29bc6ebe431d7a6b238267b6b1521fec4a3bc14f2fa348798062f870c738454` |
| SHA-1 | `a46233d8b79a69ea87aa295a0efad5237d02841e` |
| MD5 | `02a1af2a677d101394b1d99164a8c249` |

## Method

Recorded environment: Windows `10.0.26200`, PowerShell Core `7.6.5`, Python
`3.12.14`. The reusable standard-library tool is maintained in
[`SakuraiTsubaki/Decompilation`](https://github.com/SakuraiTsubaki/Decompilation/tree/a9b6a98ab90304c34b8049cf3c157a9db9045b71/tools/nds_rom_inventory).

```console
python tools/nds_rom_inventory/rom_inventory.py /path/to/input.nds
```

The tool streams the complete file through SHA-256, SHA-1, and MD5; parses the
first 512 bytes; and recalculates the Nintendo DS header CRC over
`0x0000..0x015D`. It does not modify or extract the ROM.

## Findings

- Actual size equals the nominal capacity derived from the header.
- Stored and calculated header CRC values agree.
- The raw ROM-version byte is reported without inferring undocumented content
  differences.
- Public comparison status: **matched** against
  [pret/pokediamond](https://github.com/pret/pokediamond).

## Confidence

**Confirmed.** The local whole-file SHA-1 matches the independently documented public build target, and the locally recalculated header CRC matches the stored value.

## Verification

The observed values are stored in `config/target.json`. Re-running the shared
tool on the selected input must reproduce every complete-file hash and header
field in this record.

## Unknowns

Secure-area validation, ARM9/ARM7 ranges, FNT/FAT, overlay tables, banner,
NitroFS inventory, padding, and per-file hashes remain for the next analysis
unit.
