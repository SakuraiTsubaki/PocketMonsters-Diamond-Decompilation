# Diamond Non-Retail Software and Demo Lineage

This note separates non-retail software associated with Pokémon Diamond/Pearl from the retail revision lineage in `../VERSIONS.md`.

The project assumes no local retail or kiosk ROM access. All identities below are public-reference evidence and remain `Unverified` under the repository verification model unless explicitly promoted by reproducible evidence later.

## Why this is separate

A kiosk demo, repair/service utility, distribution cartridge, Download Play payload, or development build is **not** a retail revision simply because it shares code or data with the retail game. Each lineage must keep its own identity, provenance, purpose, and verification state.

## USA Diamond + Pearl kiosk demo

Public technical databases identify a combined demo:

**Pokémon Diamond Version + Pokémon Pearl Version (USA) (Demo) (Kiosk)**

### Identity evidence

| Field | Public value | Source / status |
| --- | --- | --- |
| Game/serial ID | `Y23E` | GameHacking.org and GameTDB agree |
| Region | USA / NTSC-U | Both technical databases agree |
| Language | English | Both technical databases agree |
| Nominal ROM size | 64 MiB / 67,108,864 bytes | GameHacking.org / GameTDB |
| Version field | `0` | GameTDB |
| CRC32 | `D5EC81A9` | GameHacking.org |
| CRC32 | `5F554D97` | GameTDB |
| MD5 | `33275dba9e3b2be23793817b71f5ccb4` | GameTDB |
| SHA-1 | `05d121fbe1cdc4bda313599e063d171ae8029e19` | GameTDB |

References:

- GameHacking.org: <https://gamehacking.org/game/23363>
- GameTDB: <https://www.gametdb.com/DS/Y23E>
- Project Pokémon demo-specific RAM research: <https://projectpokemon.org/home/forums/topic/46406-pokemon-diamondpearlplatinum-starter-modifier-codes/?comment=260528&do=findComment>

### Hash conflict handling

The two technical databases report different CRC32 values for what they both identify as `Y23E`. Do **not** silently choose one.

Nintendo DS preservation commonly distinguishes encrypted and decrypted ROM representations, and No-Intro documents derivation of encrypted/decrypted DS versions with NDecrypt. That makes representation differences a plausible explanation, but the project has not yet proven which public hash corresponds to which representation.

Reference for DS preservation representation rules:

- No-Intro DS dat notes: <https://wiki.no-intro.org/index.php?title=Nintendo_-_Nintendo_DS_dat_notes>

Until the representation is proven, record:

- `Y23E` identity: strong external reference;
- GameTDB SHA-1/MD5/CRC: one public representation;
- GameHacking CRC: second public representation;
- relation between them: `TBD`.

### Evidence that the demo differs from retail

Project Pokémon cheat/RAM research has demo-specific addresses. For example, the demo starter table is documented around `0x021D8C68`, while USA/Europe retail uses a different table location around `0x021D9068` in the same research. Other demo-specific save/RAM base addresses are also documented separately.

This establishes that Y23E must be treated as its own executable/data target rather than an alias of the USA retail Rev 5 build.

## Japanese save-recovery program

Nintendo and The Pokémon Company officially documented a recovery path for Diamond/Pearl saves affected by two wall/out-of-bounds progression problems.

Official notice:

- Nintendo Japan: <https://www.nintendo.co.jp/ds/adaj/info/index.html>
- Pokémon official site mirror/notice: <https://www.pokemon.co.jp/info/2009_2005/news15.html>

### Officially documented behavior

The notice dated **2006-10-24** describes two cases that can leave the player inside walls or otherwise unable to return normally. If the affected state had already been saved, Nintendo provided a way to repair the save **without deleting obtained Pokémon/data**.

The service path included a distributed **修復プログラム (recovery/repair program)** at Nintendo station infrastructure and service-center handling. Contemporary 2006 reports state that distribution began **2006-10-27** at DS Station / Pokémon Center locations.

The official page was later updated to state that both repair support and distribution of the recovery program had ended; the added notice says this support ended by **February 2018**.

### Classification

This recovery program is tracked as:

- service/recovery software;
- related to the Japanese Diamond/Pearl retail lineage;
- **not** a retail game revision;
- **not** evidence by itself that the retail cartridge was permanently patched;
- separate from later Rev 5 / Rev 6 cartridge identities.

Public community preservation reports refer to a captured/released `Pocket Monsters Diamond and Pearl Recovery Program` payload, but its exact origin/representation must be independently established before hashes are entered as project facts.

### Important historical question

The chronology is potentially significant:

1. Japanese retail launch: 2006-09-28.
2. Official wall-progression notice: 2006-10-24.
3. Recovery program distribution reported from 2006-10-27.
4. Later Japanese retail identities labeled Rev 5 and Rev 6 exist in public preservation metadata.

The project must determine whether Rev 5/Rev 6 changed either documented wall issue, other bugs, or unrelated code/data. Do **not** assume causation merely from chronology.

## Development/debug leads

Public cheat/technical research references Japanese beta/debug variants and provides target-specific addresses. These are useful leads but require separate provenance work before formal target registration.

Current known labels encountered in public research include dated Japanese beta references such as:

- `20060630`
- `20060709`
- `20060713`
- `20060717`
- `20060801`
- `20060807`

A public widescreen-cheat changelog also references `Pocket Monsters - Diamond (Japan) (Debug Version)` as a distinct target. None of these labels should be treated as authenticated development builds solely from a cheat-database name.

## Next verification tasks

1. Determine the encrypted/decrypted representation corresponding to each Y23E checksum set.
2. Find a stronger preservation record for Y23E including SHA-1 for both representations, dump provenance, and cart/revision metadata.
3. Catalogue Y23E content differences from retail: maps, scripts, available Pokémon, Pokétch apps, barriers, text, executable layout, and save behavior.
4. Identify the recovery program's serial/content identity and preserved checksums without redistributing the payload.
5. Determine the exact transport mechanism used by the original 2006 DS Station recovery service and distinguish later 3DS Station service wording.
6. Compare known Japanese retail Rev 5/Rev 6 bug behavior against the launch build before attributing either revision to the wall-progression fixes.
7. Authenticate beta/debug build labels from preservation provenance rather than filenames alone.
