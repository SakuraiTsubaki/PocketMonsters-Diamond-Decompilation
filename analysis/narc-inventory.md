# NARC and member analysis

This repository records the complete NARC/member inventory for the verified input in `config/target.json`.

- Top-level NARCs: **149**
- Valid top-level NARCs: **149**
- Malformed top-level NARCs: **0**
- Nested NARCs: **0**
- Total members: **33953**
- Confirmed LZ10/LZ11 members: **1885**
- Unknown members: **23233**

The common parser and tests are pinned to [SakuraiTsubaki/Decompilation commit `7fa6668ce738bb02d858d2979aaddc02e2c87795`](https://github.com/SakuraiTsubaki/Decompilation/commit/7fa6668ce738bb02d858d2979aaddc02e2c87795). Complete per-member records are in ordered CSV shards under `analysis/generated/narc-inventory/members/`. ROM and raw member payload bytes are not committed.

Evidence terms follow Confirmed / Probable / Hypothesis. A known magic or compression marker remains Probable until its structure or stream is validated.
