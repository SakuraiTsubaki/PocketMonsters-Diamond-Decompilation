# Public Source Registry — Pocket Monsters Diamond

This registry tracks public material used to reconstruct and compare Pocket Monsters Diamond without assuming access to an original ROM image.

## Rules

- Japanese earliest retail release is the historical baseline.
- Record every official region, language, and revision separately.
- Do not mark releases identical without positive evidence.
- Preserve conflicting claims and their sources.
- Record redistribution/licensing status before copying external material into this repository.
- Every research result derived from a source should link back to a registry entry.
- An externally published hash or revision label is evidence, not an automatic project-level `Observed` or `Matched` result.

## Evidence status

- `CONFIRMED_IDENTICAL`
- `CONFIRMED_DIFFERENT`
- `UNVERIFIED`
- `CONFLICTING_EVIDENCE`

## Source registry

| ID | Source | Source type | Game | Region | Language | Revision | Component / scope | Original or derived | Redistribution status | Verification | Cross-check | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `D-SRC-0001` | [Nintendo Japan — Nintendo DS software list, 2006](https://www.nintendo.co.jp/ds/softlist/n2006.html) | Official Nintendo web page | Diamond | Japan | Japanese | retail launch | Release date / title | Original official | Citation/link only | Official source | `D-SRC-0002` | Confirms Japanese release on 2006-09-28. |
| `D-SRC-0002` | [Nintendo Co., Ltd. IR — major product release schedule, 2006](https://www.nintendo.co.jp/ir/pdf/2006/061027.pdf) | Official Nintendo IR PDF | Diamond | Japan | Japanese / English corporate material | retail launch | Release schedule | Original official | Citation/link only | Official source | `D-SRC-0001` | Independently corroborates the Japanese launch date. |
| `D-SRC-0003` | [GameFAQs — Pokémon Diamond Version release data](https://gamefaqs.gamespot.com/ds/925601-pokemon-diamond-version/data) | Secondary release / packaging database | Diamond | Multi-region | Multi-language | multiple | Release dates, product IDs, packaging/barcodes | Derived | Citation/link only | Cross-check required per field | Nintendo regional pages; retail catalogs | Useful index for JP/US/CA/AU/DE/ES/FR/IT/EU/KR product identifiers. Do not treat binary identity as established by packaging data. |
| `D-SRC-0004` | [OpenRetro — Pocket Monsters Diamond metadata](https://openretro.org/game/251950a9-c150-457d-8974-12b3d5a2294c/edit) | Public game metadata catalog | Diamond | Japan | Japanese | base, Rev 5, Rev 6 | Public dump labels, sizes, SHA-1 | Derived; imports preservation metadata | Metadata citation only; no ROM redistribution | External reference only | `D-SRC-0006` | Records untagged Japan build plus Rev 5 and Rev 6 with distinct hashes. Untagged entry is not silently renamed Rev 0 here. |
| `D-SRC-0005` | [PRET — pokediamond README](https://github.com/pret/pokediamond/blob/master/README.md) | Public source-reconstruction project | Diamond | United States | English | matching target | Source reconstruction target and SHA-1 | Derived / reproducible source project | Follow upstream repository/license terms; no ROMs | Strong external technical reference | `D-SRC-0007` | Diamond target SHA-1 is `a46233d8b79a69ea87aa295a0efad5237d02841e`. Public catalog metadata identifies this hash as USA Rev 5. |
| `D-SRC-0006` | [Project Pokémon — Diamond/Pearl/Platinum Mining Museum modifier research](https://projectpokemon.org/home/forums/topic/55107-pokemon-diamondpearlplatinum-mining-museum-pokemon-modifier-codes/) | Community reverse-engineering research | Diamond | Japan and other regions | Multi-language | multiple | RAM/code address differences by revision | Derived technical research | Citation/link only | Cross-checked with distinct public hashes | `D-SRC-0004` | Separates Japanese `Rev 0-5` and `Rev 6` code bases; supports real layout/address differences. The grouped label does not prove every intermediate revision exists as a preserved retail dump. |
| `D-SRC-0007` | [OpenRetro — Pokémon Diamond Version metadata](https://openretro.org/game/bb5d1b99-e0a0-4bec-a90e-541038fceb77/edit) | Public game metadata catalog | Diamond | United States / Europe | English | USA Rev 5; Europe Rev 13 | Revision labels and SHA-1 | Derived; imports preservation metadata | Metadata citation only; no ROM redistribution | External reference only | `D-SRC-0005`, `D-SRC-0014` | USA Rev 5 hash matches PRET target; English Europe is labeled Rev 13. |
| `D-SRC-0008` | [Nintendo Germany — 2007 Pokémon Diamond/Pearl announcement](https://www.nintendo.com/de-de/News/2007/Brandneue-Pokemon-Abenteuer--250170.html) | Official Nintendo Europe web page | Diamond | Germany / Europe | German | retail launch | European release date / localization | Original official | Citation/link only | Official source | `D-SRC-0003`, `D-SRC-0014` | Confirms 2007-07-27 European/German launch context. |
| `D-SRC-0009` | [Nintendo Spain — Pokémon Diamond game page](https://www.nintendo.com/es-es/Juegos/Nintendo-DS/Pokemon-Edicion-Diamante-272354.html) | Official Nintendo Europe web page | Diamond | Spain / Europe | Spanish | retail launch | Spanish release | Original official | Citation/link only | Official source | `D-SRC-0003`, `D-SRC-0014` | Used for Spanish regional release confirmation; revision/hash still require separate evidence. |
| `D-SRC-0010` | [RetroVault — Pokémon Diamond French metadata](https://retrovault.ch/rom/1015-pok-mon-diamond) | Secondary preservation/catalog page | Diamond | France | French | Rev 5 reported | Revision label and SHA-1 metadata | Derived | Metadata citation only; do not redistribute or link ROM payloads | Provisional external reference | stronger preservation catalog still required | Reports French Rev 5 SHA-1 `e961e632ca6f72f81e19c5be3d93936772e8544a`; retain as provisional until independently corroborated. |
| `D-SRC-0011` | [Nintendo Italy/Switzerland — Pokémon Diamond game page](https://www.nintendo.com/it-ch/Giochi/Nintendo-DS/Pokemon-Versione-Diamante-272354.html) | Official Nintendo Europe web page | Diamond | Italy / Europe | Italian | retail launch | Italian release | Original official | Citation/link only | Official source | `D-SRC-0003`, `D-SRC-0014` | Used for Italian regional release confirmation; revision/hash still require separate evidence. |
| `D-SRC-0012` | [Gamechosun — Korean Nintendo announcement mirror](https://www.gamechosun.co.kr/webzine/article/view.php?no=50842) | Contemporary press report reproducing Korea Nintendo material | Diamond | South Korea | Korean | retail launch | Korean localization, release date, price | Derived from Korea Nintendo press material | Citation/link only | Contemporary secondary source | `D-SRC-0003`, `D-SRC-0013` | States Korean localization and official release on 2008-02-14 at KRW 39,000. |
| `D-SRC-0013` | [Suruga-ya — Korean Diamond product listing](https://www.suruga-ya.jp/product/detail/176002367) | Secondary retail catalog | Diamond | South Korea | Korean | retail | Product code | Derived retail metadata | Citation/link only | Cross-check source | `D-SRC-0003`, `D-SRC-0012` | Lists model/product code `NTR-ADAK-KOR`; a related catalog record lists JAN `8809208140332`. |
| `D-SRC-0014` | [Nintendo UK — 2007 Pokémon Diamond/Pearl news](https://www.nintendo.com/en-gb/News/2007/Treasure-trove--250170.html) | Official Nintendo Europe web page | Diamond | Europe | English | retail launch | Europe release date | Original official | Citation/link only | Official source | `D-SRC-0008`, `D-SRC-0009`, `D-SRC-0011` | Confirms European launch timing independently of packaging databases. |
| `D-SRC-0015` | [OpenRetro — German Pokémon Diamond metadata](https://openretro.org/game/518d4142-9691-4bd4-a37a-e2cd313c1f7a/edit) | Public game metadata catalog | Diamond | Germany | German | Rev 5 | Revision label and SHA-1 | Derived; imports preservation metadata | Metadata citation only; no ROM redistribution | External reference only | `D-SRC-0008` | Labels German build Rev 5 with SHA-1 `432dbe312bc51e36bb8cb6fcb5e08f6968f124a4`. |
| `D-SRC-0016` | [GameDonga / Daum — Korean Nintendo announcement report](https://v.daum.net/v/20080118134015830) | Contemporary press report | Diamond | South Korea | Korean | retail launch | Korean localization / release date | Derived from Korea Nintendo announcement | Citation/link only | Contemporary secondary source | `D-SRC-0012` | Independently reports Korean localization and 2008-02-14 release. |

## Difference registry

| ID | Japanese baseline | Compared release | Component | Difference class | Evidence status | Source IDs | Notes |
|---|---|---|---|---|---|---|---|
| `D-DIFF-0001` | Japan base / no revision tag | Japan Rev 6 | Retail binary identity and RAM/code layout | `CODE_OR_LAYOUT_CHANGE` | `CONFIRMED_DIFFERENT` | `D-SRC-0004`, `D-SRC-0006` | Distinct public SHA-1 identities plus revision-specific code-address research establish a real difference. Exact changed functions/data remain unmapped. |
| `D-DIFF-0002` | Japan base / no revision tag | USA Rev 5 | Region/language/product binary | `REGIONAL_LOCALIZATION_AND_BINARY` | `CONFIRMED_DIFFERENT` | `D-SRC-0001`, `D-SRC-0003`, `D-SRC-0004`, `D-SRC-0005`, `D-SRC-0007` | Distinct product identity/language and public binary hash. Exact code/data/localization delta is not yet enumerated. |
| `D-DIFF-0003` | Japan base / no revision tag | South Korea retail | Language/product identity | `REGIONAL_LOCALIZATION` | `CONFIRMED_DIFFERENT` | `D-SRC-0003`, `D-SRC-0012`, `D-SRC-0013`, `D-SRC-0016` | Official Korean localization is established; exact revision and code/data differences remain unverified. |

## Immediate source gaps

- Establish stronger preservation metadata for Spanish and Italian Rev 5 builds and independently corroborate the provisional French Rev 5 hash.
- Identify Australia and Korea revision labels and hashes from preservation metadata without acquiring or redistributing ROM images.
- Resolve whether Taiwan had a distinct Diamond build or distribution of the Japanese build; separately investigate Hong Kong.
- Identify exact product/build metadata for the English European Rev 13 release beyond the currently reported packaging code.
- Establish provenance and identities for public beta/development labels and the USA kiosk demo before adding them as formal target rows.
- Enumerate Japanese revisions between the untagged baseline, Rev 5, and Rev 6 without inferring missing revisions from a cheat-code grouping label.

## Coverage backlog

The registry is expected to cover official documentation and archives; release/revision inventories; public decompilation/disassembly/source reconstruction; executable and overlay research; NitroFS/NARC formats; scripts; text; maps; events; Pokémon/trainer/item/move/encounter data; graphics/sprites/models/animation; audio; save structures; local wireless/Nintendo Wi-Fi Connection/GTS/Mystery Gift; distribution/event data; bugs and fixes; unused/dummy/debug/development remnants; localization/censorship; tooling; specialist databases/wikis; and archival community research.
