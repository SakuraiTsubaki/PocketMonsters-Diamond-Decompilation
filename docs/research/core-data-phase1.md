# Core data Phase 1 — Diamond baseline and Generation IV deltas

## Target status

The locally observed Pokémon Diamond Version image is the USA Rev 5 build (`ADAE`, ROM version 5) and matches the PRET whole-ROM SHA-1 target exactly: `a46233d8b79a69ea87aa295a0efad5237d02841e`.

See `manifests/clean_reference.json` and `manifests/observed_rom_baseline.json`.

## Core NARC inventory

| Dataset | Diamond members | Record form |
| --- | ---: | --- |
| personal | 501 | 44-byte fixed records |
| evolution | 501 | 44-byte fixed records; seven 6-byte evolution entries plus padding |
| level-up learnsets | 501 | variable length; packed 16-bit entries + `0xFFFF` sentinel |
| move table | 471 | 16-byte fixed records |
| item table | 442 | 34-byte fixed records |
| growth tables | 8 | 404-byte fixed records |

The personal layout is the Generation IV `SpeciesData` structure: base stats, types, catch/base EXP, EV yield, two wild-held-item fields, gender/hatch/friendship/growth, egg groups, two abilities, Safari flee rate, color/flip bit, and four TM/HM masks.

## Diamond ↔ Pearl

The six core archives other than the version-specific personal archive are byte-identical. `personal.narc` differs in exactly six species records:

| Species ID | Species | Diamond held slots | Pearl held slots |
| ---: | --- | --- | --- |
| 125 | Electabuzz | common = Electirizer (322), rare = none | common = none, rare = Electirizer |
| 126 | Magmar | common = none, rare = Magmarizer (323) | common = Magmarizer, rare = none |
| 239 | Elekid | common = Electirizer, rare = none | common = none, rare = Electirizer |
| 240 | Magby | common = none, rare = Magmarizer | common = Magmarizer, rare = none |
| 466 | Electivire | common = Electirizer, rare = none | common = none, rare = Electirizer |
| 467 | Magmortar | common = none, rare = Magmarizer | common = Magmarizer, rare = none |

No other byte in these six 44-byte records changes.

## Diamond → Platinum

Shared-index archive comparison:

- evolution: 0 changed records; Platinum adds 7 form records.
- growth tables: byte-identical.
- level-up learnsets: 81 changed shared records; Platinum adds 7 form learnsets.
- move table: exactly 1 changed record, move 95 (Hypnosis).
- personal: 6 changed shared records; Platinum adds 7 form records.
- item table: raw index comparison produces 242 differing records plus 4 additional Platinum records, but this includes record insertion/index-realignment effects and must not be interpreted as 242 semantic item changes.

### Hypnosis

Diamond: accuracy 70. Platinum: accuracy 60. Every other field in the 16-byte move record is identical.

### Personal changes visible from the Diamond branch

- Tangela (114): Safari flee rate `0 → 90`.
- Kecleon (352): Safari flee rate `0 → 120`.
- Tropius (357): Safari flee rate `0 → 60`.
- Electabuzz (125), Elekid (239), Electivire (466): Electirizer moves from the common slot to the rare slot.

### Platinum extra data-form slots

Diamond has five post-base data-form records: Deoxys Attack/Defense/Speed and Wormadam Sandy/Trash. Platinum adds seven more at indexes 501–507:

1. Giratina Origin
2. Shaymin Sky
3. Rotom Heat
4. Rotom Wash
5. Rotom Frost
6. Rotom Fan
7. Rotom Mow

All seven added evolution records are zero-filled; these are alternate-form data/learnset slots, not new evolution targets.

## Verification status

All counts and deltas above are **Observed** directly from the locally provided Diamond/Pearl/Platinum images. Claims using the Diamond whole-ROM target can be promoted to exact-match evidence because the Diamond image matches the clean PRET target. Platinum whole-ROM exact-match claims remain separate because the locally available Korean Platinum image is retained only as a comparison source.
