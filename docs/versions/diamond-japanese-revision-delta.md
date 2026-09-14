# Japanese Diamond Revision Delta Research

This note tracks what can and cannot currently be established about the Japanese retail lineage of **Pocket Monsters Diamond**:

`base / no revision tag -> Rev 5 -> Rev 6`

The project has no local retail ROM. External hashes, behavioral reports, and technical addresses are therefore reference evidence unless promoted under `VERIFICATION.md`.

## Known binary identities

| Target | Public identity | Project status |
| --- | --- | --- |
| Japanese historical baseline | SHA-1 `fb0bba9fca12d418c8b430e8950171cc356ee981` | External reference; historical baseline |
| Japanese Rev 5 | SHA-1 `32d9bb56070be14b74c7447c8b46de55cc93ac27` | External reference |
| Japanese Rev 6 | SHA-1 `85e5f59ea521c1b1d7026db813cca9997ad32693` | External reference |

The first public catalog identity has no revision tag. This project therefore keeps it as **base / no revision tag** instead of silently converting that catalog label into `Rev 0`.

## What is strongly established about Rev 6

Public technical research independently shows that Rev 6 is not merely a preservation filename alias. Multiple code/data targets move relative to the base/Rev 5 builds.

Examples from Project Pokémon technical research:

| Subsystem / patch target | Base / Rev 5 | Rev 6 | Implication |
| --- | ---: | ---: | --- |
| Trade-evolution routine patch site | around `0x0206C34A` | around `0x0206C44A` | Executable code moved/changed |
| Mining Museum-related target | around `0x021C60FC` | around `0x021C623C` | RAM/data layout differs |
| Dual-slot mode save/base data | grouped Rev 0-5 base | distinct Rev 6 base | RAM layout differs |
| Pal Park timing-related targets | Rev 5 addresses | distinct Rev 6 addresses | Executable/data layout differs |

References:

- Trade-evolution comparison: <https://projectpokemon.org/home/forums/topic/67211-pokemon-diamondpearlplatinumheartgoldsoulsilver-bypass-trade-requirement-for-trade-evolutions-codes/>
- Revision-specific technical research is cross-linked in `../SOURCE_REGISTRY.md` under `D-SRC-0006` and related Project Pokémon entries.

This establishes a **real Rev 6 code/layout delta**. It does **not** by itself identify which changed functions implement any particular bug fix.

## Rev 5: changes currently unknown

Current specialist version tables describe Japanese `1.5` / Rev 5 as having **unknown changes**.

More importantly, the technical examples found so far frequently give the same address for the untagged Japanese build and Rev 5, while Rev 6 shifts. That is useful evidence that some structures remained in the same place through Rev 5, but it does **not** prove the two binaries are functionally identical.

Current project status for Rev 5 changes:

`UNVERIFIED / UNKNOWN`

Do not fill the gap with assumptions such as “Rev 5 only changes the ROM header” unless direct evidence is found.

## Candidate Rev 6 gameplay changes

The current Bulbapedia Diamond/Pearl version table attributes the following changes to Japanese version `1.6`:

- fixes the **Surf glitch**;
- fixes the **broken escalator oversight**;
- disables the ability to open the menu in a **Mystery Zone**.

Reference:

- <https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Diamond/Pearl>

These are important candidate functional deltas, but this project currently classifies the attribution as:

`SECONDARY-SOURCE CLAIM / TECHNICAL BINARY DIFF NOT YET MAPPED`

The claim is plausible and consistent with a distinct Rev 6 executable, but the project has not yet mapped the exact changed instructions/scripts/data that implement those behaviors.

## Surf glitch evidence

The Surf glitch is a Japanese Diamond/Pearl bug that allows Surf through Aaron's Elite Four room doorway into the void.

Specialist glitch documentation establishes that:

- the glitch exists in Japanese Diamond/Pearl;
- Nintendo officially acknowledged the problem;
- Nintendo distributed a save-recovery program beginning in late October 2006 for players who became trapped;
- international releases removed the Surf glitch.

References:

- Bulbapedia Surf glitch: <https://bulbapedia.bulbagarden.net/wiki/Surf_glitch>
- Nintendo/Pokémon official recovery notices are registered as `D-SRC-0031` and `D-SRC-0032`.

However, older technical/gameplay communities usually describe the exploit as working on **early Japanese copies**, and TASVideos material often uses phrases such as `early Japanese copies` or `JP V1.0 only` rather than an exact cartridge revision number.

References:

- <https://tasvideos.org/Forum/Topics/7309>
- <https://tasvideos.org/5771S>

This terminology creates a revision-identification ambiguity:

- it is compatible with the claim that Rev 6 fixed the glitch;
- but it does not independently prove whether Rev 5 still contains the glitch;
- `V1.0` in an emulator/TAS context must not automatically be equated to the preservation project's untagged/base hash without checking the exact submitted binary identity.

Therefore the project does **not** yet state `Surf glitch present in Rev 5` or `Surf glitch fixed in Rev 5` as fact.

## Broken escalator oversight

The second officially acknowledged issue can leave the player trapped in a wall after Union Room / Pokémon Center-related state interactions in early Japanese copies.

References:

- Bulbapedia Gen IV overworld glitches: <https://bulbapedia.bulbagarden.net/wiki/List_of_overworld_glitches_%28Generation_IV%29>
- official recovery notices: `D-SRC-0031`, `D-SRC-0032`.

Bulbapedia's current version table attributes its retail fix to Japanese `1.6`, but the exact code or script delta has not yet been independently isolated in public source reconstruction.

Current project state:

`Rev 6 fix attribution = UNVERIFIED technical implementation; supported by specialist secondary documentation`

## Mystery Zone menu restriction

Bulbapedia documents that on Japanese version `1.0`, the menu and Explorer Kit can be used in a Mystery Zone, while the version table says version `1.6` disables menu opening there.

References:

- Mystery Zone behavior: <https://bulbapedia.bulbagarden.net/wiki/---->
- Diamond/Pearl version table: <https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Diamond/Pearl>

This is potentially a particularly useful revision marker because it is behavioral and can eventually be tied to a specific menu-permission check in code/data.

Current status:

- version 1.0 menu behavior: specialist secondary documentation;
- Rev 6 menu restriction: specialist secondary documentation;
- exact Rev 5 behavior: **TBD**;
- exact changed function/table/flag: **TBD**.

## Official recovery chronology does not prove cartridge revision causation

The known chronology is:

1. Japanese launch: **2006-09-28**.
2. Official Nintendo/Pokémon issue notice: **2006-10-24**.
3. Recovery program distribution reported from **2006-10-27**.
4. Later public preservation metadata contains Japanese Rev 5 and Rev 6 retail identities.

This chronology makes a later retail fix plausible, but chronology alone does not establish that Rev 5 or Rev 6 was produced specifically to fix the two officially acknowledged bugs.

The recovery program itself is service software and remains separate from the retail cartridge lineage; see `diamond-non-retail-software.md`.

## Current evidence matrix

| Claim | Evidence level | Current project treatment |
| --- | --- | --- |
| Rev 6 binary differs from base/Rev 5 | Multiple external hashes + revision-specific technical addresses | Strong external evidence; `CONFIRMED_DIFFERENT` in comparison registry |
| Rev 5 has changes from base | Distinct public hash only; functional delta not mapped | Difference in binary identity established externally; functional changes `UNKNOWN` |
| Rev 6 fixes Surf glitch | Current specialist version table | `UNVERIFIED` functional attribution pending code/binary mapping |
| Rev 6 fixes broken escalator oversight | Current specialist version table | `UNVERIFIED` functional attribution pending code/binary mapping |
| Rev 6 disables Mystery Zone menu | Current specialist version table + documented 1.0 menu behavior | `UNVERIFIED` functional attribution pending code/binary mapping |
| Rev 5 still has Surf glitch | Historical community wording is not revision-precise | `TBD` |
| International releases remove Surf glitch | Specialist glitch documentation | Strong secondary behavioral evidence; implementation comparison still TBD |

## Code-level investigation targets

The next technical pass should try to identify public code/data corresponding to:

1. **Surf field-move eligibility** at Aaron's doorway / door collision context.
2. **Mystery Zone menu permission** check, including map-ID or map-header restrictions.
3. **Union Room / Pokémon Center escalator state** and the save-state recovery condition.
4. The exact inserted/removed code responsible for the recurring Rev 6 address shift seen in multiple technical patches.
5. Whether Rev 5 differs from the base build in code, data, text, metadata, padding, or another region despite some important addresses remaining unchanged.

The USA PRET source reconstruction can be used as a structural reference for locating relevant subsystems, but its USA Rev 5 matching target must **not** be treated as proof of Japanese Rev 6 implementation.

## Open verification tasks

- Find authenticated behavior reports tied to the exact Japanese Rev 5 hash.
- Find authenticated behavior reports tied to the exact Japanese Rev 6 hash.
- Locate a public source-level or binary-diff analysis of base -> Rev 5 and Rev 5 -> Rev 6.
- Map the Surf fix to exact code/data changes.
- Map the broken-escalator fix to exact code/script/state changes.
- Map the Mystery Zone menu restriction to exact code/data changes.
- Determine whether all three candidate changes were introduced together in Rev 6 or whether current secondary tables have compressed a more complex history.
