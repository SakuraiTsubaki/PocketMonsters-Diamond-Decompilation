# Diamond / Pearl USA Rev 5 — ROM comparison baseline

**Date observed:** 2026-09-14  
**Verification:** Observed  
**Targets:** USA Rev 5 Diamond (`ADAE`) and Pearl (`APAE`) project-provided ROMs

The whole-ROM SHA-1 values match the already documented USA Rev 5 identities in this repository's version inventory. This note records direct binary observations from the two target ROMs.

## Container and executable overview

- Both ROMs are 64 MiB Nintendo DS images with header `ROM version = 5`.
- Both contain 87 ARM9 overlay records and no ARM7 overlay table.
- ARM7 is byte-identical between the two targets (`SHA-1 39aacbf97ae65b17783057aeed06b80049b18dee`).
- ARM9 has the same size but is not byte-identical.
- Each ROM has 356 FAT entries: 87 overlay-backed/unnamed entries plus 269 files represented by the FNT tree.
- Of the named files, 268 paths are shared and all 268 are byte-identical.
- The only version-unique named path is the personal-data archive location: Diamond uses `poketool/personal/personal.narc`; Pearl uses `poketool/personal_pearl/personal.narc`.

## ARM9 overlay comparison

The two builds contain 87 ARM9 overlays. 69 are byte-identical. The following 18 overlay IDs differ:

`5, 6, 7, 8, 11, 12, 16, 17, 18, 48, 54, 62, 63, 64, 80, 81, 83, 84`

A differing overlay must not automatically be treated as a distinct gameplay feature; code, constants, relocations, and version branches still need function-level reconstruction.

## Personal-data archive delta

Both personal archives contain 501 members of 44 bytes each. Exactly six species records differ:

| National Dex | Species | Difference observed |
| ---: | --- | --- |
| 125 | Electabuzz | held-item slot fields |
| 126 | Magmar | held-item slot fields |
| 239 | Elekid | held-item slot fields |
| 240 | Magby | held-item slot fields |
| 466 | Electivire | held-item slot fields |
| 467 | Magmortar | held-item slot fields |

No base-stat/type/ability fields differ in those six records. The changed words are the two held-item slots at record offsets `0x0C` and `0x0E`, involving item IDs `322` and `323` (`ITEM_ELECTIRIZER` and `ITEM_MAGMARIZER`). Diamond and Pearl exchange which held-item slot contains the relevant evolution item, encoding the version-dependent held-item probability directly in personal data.

## Debug/development-named resource

Both targets contain `wazaeffect/pt_debug/debug_particle.narc` (3,016 bytes, two archive members). Its path is explicitly debug-named. Presence is confirmed; whether it is referenced by normal runtime code remains a separate call-site/reachability question and is not yet classified as unused.

## Next reconstruction work

1. Decode every 44-byte personal-data field and produce semantic per-field diffs rather than raw offsets.
2. Reconstruct the 18 differing overlays and identify every version condition/data reference.
3. Trace `pt_debug/debug_particle.narc` references to classify it as used, unreachable, or development residue.
4. Extend the comparison to encounter tables, trainers, scripts, text, graphics, and event flags at member/record granularity.
