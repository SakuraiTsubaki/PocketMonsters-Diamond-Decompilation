# Generation IV Bug/Glitch/Error Elimination Program

## Goal

This repository treats unintended, reproducible defects as first-class reconstruction targets. The goal is to eliminate confirmed bugs, glitches, data errors, unsafe debug leftovers, corruption paths, and other unintended failures while preserving intended Generation IV mechanics, content, compatibility, and historical evidence.

"Fix everything" does **not** mean guessing. A reported issue remains `research_required` until it is reproduced or established from source/ROM evidence. Intentional mechanics, balance choices, discontinued-service behavior, and external-server behavior are classified separately so that a historical feature is not silently deleted under the label of a bug.

## Exact target baseline

- Title: **Pokémon Diamond Version**
- Game code: `ADAE`
- Region/language: **USA English**
- Header ROM version: `5`
- SHA-256: `e29bc6ebe431d7a6b238267b6b1521fec4a3bc14f2fa348798062f870c738454`
- Identity status: **canonical public hash match confirmed**
- FAT/NitroFS file entries: **356**
- ARM9 overlays: **87**

The ROM image itself stays outside Git. Only reproducible non-ROM evidence, source, scripts, manifests, patches, tests, and hashes are committed.

## Mandatory fix pipeline

Every defect must pass all of these gates before it is marked fixed:

1. **Scope** — identify exact game, language/region, revision, and whether the issue crosses link-battle/communication boundaries.
2. **Reproduction** — record deterministic steps or a minimal state fixture. Random/timing issues need repeated-run evidence.
3. **Root cause** — identify the responsible ARM9/ARM7 routine, overlay, NitroFS/NARC member, script, map/tile data, message/text data, or protocol state.
4. **Regression test first** — preserve a test that fails on the original target and passes after the fix whenever automation is technically possible.
5. **Semantic patch** — patch the cause, not a symptom or a hard-coded address copied from a different revision.
6. **Cross-version audit** — inspect the corresponding path in D/P/Pt/HG/SS and later/localized revisions to detect an existing official correction.
7. **Binary-diff verification** — use `scripts/nds_inventory.py` and target-specific hashes to prove exactly which executable/overlay/archive changed.
8. **Gameplay verification** — verify normal gameplay, save/load, link behavior where applicable, and adjacent mechanics are unchanged.
9. **Documentation** — update `manifests/bugfix-matrix.csv` with evidence, target applicability, root cause, patch reference, and test reference.

## Classification

The registry deliberately separates `confirmed_public`, `region_specific`, `research_required`, `assessment_required`, and `discovery_track`. A public report is only the start of the investigation; ROM/source evidence takes precedence. Network/service exploits are not automatically treated as local code defects. Debug/unused material is preserved as historical data even when a reachable unsafe path is disabled or corrected.

## Current exhaustive seed registry

`manifests/bugfix-matrix.csv` seeds the investigation with documented Generation IV battle, overworld, save/storage, GTS/link, Pal Park, Pokéwalker, UI/text, map, graphics/audio, timing, and data-error families, plus systematic discovery sweeps for defects that are not yet in public glitch lists. This is a living registry, not a claim that internet lists are complete.

Primary public survey sources used to seed the queue:

- https://bulbapedia.bulbagarden.net/wiki/List_of_battle_glitches_in_Generation_IV
- https://bulbapedia.bulbagarden.net/wiki/List_of_overworld_glitches_in_Generation_IV
- https://bulbapedia.bulbagarden.net/wiki/List_of_glitches_in_Generation_IV
- https://www.smogon.com/ingame/guides/gen4_glitches

## Completion rule

A target is not declared "bug-free" merely because every known wiki entry is checked off. Completion requires: all confirmed registry entries resolved or explicitly proven non-applicable; all `research_required` entries either reproduced and fixed or closed with evidence; systematic audit tracks completed; deterministic rebuild/patch verification; and no unresolved regression introduced by the fixes.
