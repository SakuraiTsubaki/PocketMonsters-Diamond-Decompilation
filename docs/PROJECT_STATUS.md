# Project Status

**Current stage:** Phase 0 — Target definition / public-source inventory (**in progress**)

This document tracks decompilation progress, target-version coverage, validation level, and the next major milestones.

The project assumes no local retail ROM access. Publicly documented identities and hashes therefore remain `Reference only` unless they satisfy the independent verification requirements in `VERIFICATION.md`.

## Version inventory

| Target | Region | Language | Revision / update | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| Pocket Monsters Diamond | Japan | Japanese | base / no revision tag | Reference only | Historical baseline; release 2006-09-28. Public SHA-1 recorded in `VERSIONS.md`. |
| Pocket Monsters Diamond | Japan | Japanese | Rev 5 | Reference only | Distinct public catalog identity recorded. |
| Pocket Monsters Diamond | Japan | Japanese | Rev 6 | Reference only | Distinct public identity; revision-specific RAM/code addresses differ from the public `Rev 0-5` grouping. |
| Pokémon Diamond Version | United States | English | Rev 5 | Reference only | PRET matching target; SHA-1/MD5/CRC identities cross-checked in public technical metadata. |
| Pokémon Diamond Version | Europe | English | **label conflict: Rev 5 / Rev 13** | Reference only | Same SHA-1 is assigned two revision labels by public technical sources; tracked as `CONFLICTING_EVIDENCE`, not as two binaries. |
| Pokémon Diamant-Edition | Germany | German | Rev 5 | Reference only | SHA-1/MD5/CRC metadata cross-checked; official regional release page located. |
| Pokémon Edición Diamante | Spain | Spanish | Rev 5 | Reference only | MD5/CRC identity located; SHA-1 still TBD. |
| Pokémon Version Diamant | France | French | Rev 5 | Reference only | MD5/CRC cross-check plus provisional SHA-1; cleaner preservation-source SHA-1 corroboration still desired. |
| Pokémon Versione Diamante | Italy | Italian | Rev 5 | Reference only | MD5/CRC identity located; SHA-1 still TBD. |
| Pokémon Diamond Version | Australia | English | unknown | Unverified | Product/release identity located; revision/hash still TBD. |
| 포켓몬스터DP 디아루가 | South Korea | Korean | unknown | Unverified | Korean localization/release/product code established; revision/hash still TBD. |
| Pocket Monsters Diamond local distribution | Taiwan | Japanese | dedicated build unresolved | Reference only | Contemporary local records establish 博優 distribution/support of D/P; no distinct Taiwan binary is established. Secondary sources conflict over whether to call this a Taiwan “release.” |
| Diamond regional distribution | Hong Kong | TBD | unresolved | Unverified | No conclusion until official/local archival evidence is exhausted. |

See `VERSIONS.md` for the authoritative detailed inventory and `SOURCE_REGISTRY.md` for provenance.

## Progress

- [~] Establish authoritative version/revision inventory — **in progress**; Japanese baseline, major English branches, continental Europe Rev 5 identities, Korean release metadata, and Taiwan distribution evidence are now recorded.
- [ ] Document executable and section layout
- [ ] Map symbols, functions, and major subsystems
- [ ] Document game-data formats and resource containers
- [ ] Reconstruct scripts, events, and behavior
- [ ] Reconstruct asset pipelines and metadata
- [ ] Add reproducible extraction/repacking tooling
- [ ] Add automated verification where practical

## Phase 0 findings so far

- The Japanese retail lineage cannot be represented as a single undifferentiated build: public preservation metadata distinguishes an untagged Japanese build, Rev 5, and Rev 6.
- Public technical research uses different RAM/code address bases for Japan Rev 6 versus a Japan `Rev 0-5` grouping, establishing a meaningful revision distinction even though the exact binary delta is not yet mapped.
- PRET's Diamond source-reconstruction target is the USA hash that public preservation metadata labels Rev 5. It is a critical USA reference, but it is not the Japanese historical baseline.
- Continental European German, Spanish, French, and Italian builds have public technical metadata identifying Rev 5 binaries. Their identities remain separate by language.
- The English-European SHA-1 `66d2fbfb0dbc1f86a3d726971196989b950092bc` has a **revision-label conflict**: some preservation/technical sources call it Rev 13 while other compatibility/restoration sources call that exact same hash Rev 5. Cryptographic identity is stable; revision-number semantics remain unresolved.
- Korean localization and the `NTR-ADAK-KOR` product identity are established from contemporary press and retail metadata, but the Korean revision/hash remains unresolved.
- Taiwan must be modeled as a **distribution question separate from a binary-localization question**: contemporary Taiwanese records show local Nintendo distributor 博優 selling/supporting D/P, while no distinct Taiwan-coded/localized Diamond build has yet been identified and some later wikis call Taiwan “not released.” The conflicting terminology is preserved in `SOURCE_REGISTRY.md` rather than collapsed.

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly in a specific target build, executable, extracted file, or runtime observation.
- **Reproduced** — the observation can be recreated using documented steps, tooling, inputs, and target information.
- **Matched** — reconstructed output is verified against the intended target using an explicit exact-match criterion.
- **Reference only** — externally documented identity, hash, revision, or comparison target retained for research without claiming local project observation.

## Next milestones

1. Resolve the English-Europe `Rev 5 / Rev 13` label semantics for the already-fixed SHA-1 identity.
2. Complete the remaining retail inventory: Australia and Korea revision/hash evidence, plus any still-missing SHA-1 values for continental Europe.
3. For Taiwan, determine the exact Japanese product/revision distributed by 博優; investigate Hong Kong separately from Taiwan.
4. Catalogue non-retail Diamond references separately: kiosk demo, public beta/development labels, recovery/service utilities, and distribution/event software.
5. Expand the Japanese revision history without inferring undocumented revisions from grouped cheat-code labels.
6. Only after the retail lineage is sufficiently stable, begin Phase 1 executable/container mapping against the Japanese-origin baseline and regional branches.

Update this file whenever the project reaches a meaningful milestone or adds a new supported target.
