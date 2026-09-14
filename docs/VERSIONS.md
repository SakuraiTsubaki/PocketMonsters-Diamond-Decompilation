# Version Coverage

Use this document as the authoritative inventory of game versions targeted by this decompilation project.

Because this project assumes no local retail ROM access, identities, revision labels, and hashes learned from public catalogs or external matching projects are recorded conservatively as **Reference only** until they can satisfy the verification requirements in `VERIFICATION.md`.

## Historical baseline

The historical baseline is the earliest officially released Japanese retail edition of **Pocket Monsters Diamond**, released on **2006-09-28**.

Public dump catalogs distinguish an untagged Japanese retail build plus later `Rev 5` and `Rev 6` variants. The untagged entry is recorded here as **base / no revision tag** rather than silently relabeling it `Rev 0`.

## Retail release inventory

| Status | Region | Language | Revision / update | Platform / build | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Reference only | Japan | Japanese | base / no revision tag | Nintendo DS; `NTR-ADAJ-JPN`; 2006-09-28 | SHA-1 `fb0bba9fca12d418c8b430e8950171cc356ee981` | Japanese historical baseline. Public catalog identity; not independently observed by this project. Sources `D-SRC-0001`, `D-SRC-0002`, `D-SRC-0004`. |
| Reference only | Japan | Japanese | Rev 5 | Nintendo DS; `NTR-ADAJ-JPN` | SHA-1 `32d9bb56070be14b74c7447c8b46de55cc93ac27` | Public catalog variant. Public technical research groups several code addresses under Japan `Rev 0-5`. Sources `D-SRC-0004`, `D-SRC-0006`. |
| Reference only | Japan | Japanese | Rev 6 | Nintendo DS; `NTR-ADAJ-JPN` | SHA-1 `85e5f59ea521c1b1d7026db813cca9997ad32693` | Public catalog variant. Public technical research uses different address bases from the `Rev 0-5` grouping. Sources `D-SRC-0004`, `D-SRC-0006`. |
| Reference only | United States | English | Rev 5 | Nintendo DS; `NTR-ADAE-USA`; 2007-04-22 | SHA-1 `a46233d8b79a69ea87aa295a0efad5237d02841e` | PRET matching target; public catalog metadata identifies the same hash as USA Rev 5. Sources `D-SRC-0003`, `D-SRC-0005`, `D-SRC-0007`. |
| Planned | Canada | English | unknown | Nintendo DS; `NTR-ADAE-USA` reported; 2007-04-22 | TBD | Canadian packaging/barcode is separately reported; binary identity with the USA release has not been established. Source `D-SRC-0003`. |
| Planned | Australia | English | unknown | Nintendo DS; `NTR-ADAE-AUS`; 2007-06-21 | TBD | Product identifier/date are publicly catalogued; revision/hash still require stronger verification. Source `D-SRC-0003`. |
| Reference only | Europe | English | Rev 13 | Nintendo DS; `NTR-ADAP-EUR` reported; 2007-07-27 | SHA-1 `66d2fbfb0dbc1f86a3d726971196989b950092bc` | Public catalog metadata labels the English European build Rev 13. Exact packaging suffix conventions still require direct documentation. Sources `D-SRC-0003`, `D-SRC-0007`, `D-SRC-0014`. |
| Reference only | Germany | German | Rev 5 | Nintendo DS; `NTR-ADAD-NOE`; 2007-07-27 | SHA-1 `432dbe312bc51e36bb8cb6fcb5e08f6968f124a4` | Revision/hash from public catalog metadata; release date corroborated by Nintendo Europe/Germany. Sources `D-SRC-0003`, `D-SRC-0008`, `D-SRC-0015`. |
| Planned | Spain | Spanish | Rev 5 reported | Nintendo DS; `NTR-ADAS-ESP`; 2007-07-27 | TBD | Rev 5 appears in public technical/revision databases; hash still to identify from stronger catalog evidence. Sources `D-SRC-0003`, `D-SRC-0006`, `D-SRC-0009`. |
| Reference only | France | French | Rev 5 | Nintendo DS; `NTR-ADAF-FRA`; 2007-07-27 | SHA-1 `e961e632ca6f72f81e19c5be3d93936772e8544a` | Hash currently comes from a secondary catalog mirror and must be rechecked against a stronger catalog source. Sources `D-SRC-0003`, `D-SRC-0010`, `D-SRC-0014`. |
| Planned | Italy | Italian | Rev 5 reported | Nintendo DS; `NTR-ADAI-ITA`; 2007-07-27 | TBD | Rev 5 appears in public technical/revision databases; hash still to verify. Sources `D-SRC-0003`, `D-SRC-0006`, `D-SRC-0011`. |
| Planned | South Korea | Korean | unknown | Nintendo DS; `NTR-ADAK-KOR`; 2008-02-14 | TBD | Korean-localized retail release is documented; revision/hash still to identify. Sources `D-SRC-0003`, `D-SRC-0012`, `D-SRC-0013`. |
| Planned | Taiwan | TBD | unresolved | Reported availability/distribution 2006-09-28; dedicated build not established | TBD | Secondary sources report Taiwan availability, but a distinct Taiwan binary/product code is not established in the current evidence set. Determine whether the Japanese build was distributed there. |
| Planned | Hong Kong | TBD | unresolved | No dedicated retail build established in the current evidence set | TBD | Keep open until official and local archival evidence is exhausted. Do not infer nonexistence from present absence of evidence. |

## Non-retail and development references

These are intentionally separated from the retail lineage.

- Public technical databases reference Japanese development/beta builds labeled with dates including `20060630`, `20060709`, `20060713`, `20060717`, `20060801`, and `20060807`. Their provenance, hashes, and exact status remain **Unverified** for this project.
- A USA Diamond/Pearl kiosk demo is separately identified by public technical databases. Its exact identity and hashes still require verification.
- Official recovery/service utilities and event/distribution software are tracked separately from retail game revisions.

## Known revision implications

- Japan `Rev 6` is not treated as merely a filename label: public RAM/code research uses different address bases than the Japan `Rev 0-5` grouping for multiple systems. The exact binary changes still need to be mapped.
- PRET's current Diamond matching target is the USA SHA-1 listed above. Public catalog metadata identifies that hash as `Rev 5`; PRET therefore provides a major source-reconstruction reference for the USA branch, not direct proof of the Japanese-baseline binary.
- A shared product code or release date does **not** establish byte identity. Regional packaging records and binary identities remain separate questions.

## Status vocabulary

- **Planned** — intended for investigation but not yet verified.
- **Verified** — identity and hashes confirmed under this project's verification standard.
- **Mapped** — executable/data layout documented.
- **In progress** — active source reconstruction.
- **Matched** — reconstruction verified against the target.
- **Reference only** — external identity, hash, revision, or comparison target used as evidence but not independently verified by this project.

## Recording rules

1. Record exact revision/update information whenever known.
2. Prefer cryptographic hashes over filenames as identity evidence.
3. Do not commit retail game images or console keys.
4. Record regional or language differences instead of assuming two releases are identical.
5. Link version-specific findings to the relevant documentation or verification issue.
6. Do not convert an external catalog's revision label into project fact without preserving its provenance.
7. Keep retail, demo, development, distribution, and service/recovery software lineages distinct.
