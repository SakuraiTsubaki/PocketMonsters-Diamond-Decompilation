# Diamond Retail Revision Research

This note records detailed public-source research behind the compact inventory in `../VERSIONS.md`. It follows the repository's no-ROM premise: external hashes and labels are research references, not local `Observed` or `Matched` claims.

## Scope

- Historical origin: earliest Japanese retail release.
- All known official regional/language branches.
- Revision-label semantics and conflicts.
- Distribution versus dedicated-binary distinctions.
- Public preservation metadata only; no retail ROM images are stored or linked for redistribution.

## Japanese baseline and revisions

The earliest Japanese retail release is dated **2006-09-28**. Public preservation metadata currently distinguishes:

| Target | Public label | SHA-1 | Project treatment |
| --- | --- | --- | --- |
| Japan | no revision tag | `fb0bba9fca12d418c8b430e8950171cc356ee981` | Historical baseline; do not silently rename to Rev 0 |
| Japan | Rev 5 | `32d9bb56070be14b74c7447c8b46de55cc93ac27` | External reference |
| Japan | Rev 6 | `85e5f59ea521c1b1d7026db813cca9997ad32693` | External reference |

Public RAM/code research separates Japan `Rev 0-5` from `Rev 6` and uses different base addresses for multiple systems. This supports a real code/layout distinction for Rev 6, but the grouped label `Rev 0-5` must **not** be interpreted as proof that every intermediate revision has a preserved retail dump.

Primary research references:

- Nintendo Japan 2006 DS software list: <https://www.nintendo.co.jp/ds/softlist/n2006.html>
- OpenRetro metadata imported from preservation data: <https://openretro.org/game/251950a9-c150-457d-8974-12b3d5a2294c/edit>
- Project Pokémon revision-specific RAM research: <https://projectpokemon.org/home/forums/topic/55107-pokemon-diamondpearlplatinum-mining-museum-pokemon-modifier-codes/>

## USA Rev 5

PRET's `pokediamond` reconstruction target uses SHA-1:

`a46233d8b79a69ea87aa295a0efad5237d02841e`

Current public technical metadata identifies this binary as **USA Rev 5**. This is a high-value source-reconstruction reference for the USA branch, but it is not the Japanese historical baseline.

References:

- PRET: <https://github.com/pret/pokediamond/blob/master/README.md>
- No-Intro official Wiki, USA undumped/revision notes: <https://wiki.no-intro.org/index.php?title=Nintendo_-_Nintendo_DS%28i%29_USA_undumped>

The No-Intro Wiki is especially important because it distinguishes the Nintendo lot-check revision field from the dumped retail cart label: it lists `ADAE` revision 0 as an undumped/expected revision and notes that the cart dumped before street date is Rev 5. Therefore `Rev 5` must not be simplified into “fifth retail patch after Rev 0” without further evidence.

## English Europe: Rev 5 versus legacy Rev 13 label

A single stable binary identity is involved:

- SHA-1: `66d2fbfb0dbc1f86a3d726971196989b950092bc`
- MD5: `ca7620b92665a2565b5c1831f5f66ec0`

### Evidence for `Rev 5`

Current/modern technical sources identify this binary as **Europe / EUR English Rev 5**:

- No-Intro official Wiki's Europe undumped/revision table states that `ADAP` revision 0 is an undumped/likely-nonexistent revision and that **day-1 carts are all revision 5**: <https://wiki.no-intro.org/index.php?title=Nintendo_-_Nintendo_DS%28i%29_Europe_undumped>
- Current Dat-o-Matic record 1284 is cited by preservation/authentication discussions as `Pokemon - Diamond Version (Europe) (Rev 5)`.
- Project Pokémon My Pokémon Ranch restoration documentation explicitly identifies the SHA-1 above as `EUR English Rev 5`: <https://projectpokemon.org/home/files/file/5900-wiiware-my-pok%C3%A9mon-ranch-platinum-version-english-usa-update-patch/>
- RetroAchievements' current No-Intro-tagged compatibility metadata uses Rev 5 naming for the supported regional Diamond set: <https://retroachievements.org/game/9852/hashes>

### Evidence for `Rev 13`

Older metadata ecosystems identify the **same SHA-1** as `Rev 13`:

- OpenRetro imported a **2017-11-14 No-Intro** record as `Pokemon - Diamond Version (Europe) (Rev 13)`: <https://openretro.org/game/bb5d1b99-e0a0-4bec-a90e-541038fceb77/edit>
- Older No-Intro ROM-set indexes and DeadSkullzJr-era cheat databases preserve the same `Rev 13` naming.

### Current interpretation

**Current evidence strongly favors `Rev 5` as the present No-Intro/technical label for the known English-European binary.** `Rev 13` appears to be a legacy/obsolete label retained from an older No-Intro metadata snapshot and downstream databases.

However, the exact historical reason for the `13 -> 5` relabeling has not yet been found in an authoritative No-Intro changelog. Until that provenance is located:

- do not create separate Rev 5 and Rev 13 binary targets;
- use the cryptographic hash as the stable identity;
- record `Rev 5` as the current favored label;
- preserve `Rev 13` as a historical alias / legacy metadata label;
- keep the relabeling reason as `TBD` rather than inventing one.

## Continental Europe

Current public compatibility/preservation metadata identifies the following language builds as Rev 5:

| Region/language | Product code | MD5 | CRC32 | SHA-1 status |
| --- | --- | --- | --- | --- |
| Germany / German | `NTR-ADAD-NOE` | `0683ef614f0cef8228db7676c074c18e` | `87CF7B1F` | `432dbe312bc51e36bb8cb6fcb5e08f6968f124a4` publicly catalogued |
| Spain / Spanish | `NTR-ADAS-ESP` | `1dea9d321d8413a43dbd6e793bdfdec0` | `AA3E6B39` | TBD |
| France / French | `NTR-ADAF-FRA` | `da0382f57cee0f6807f43a61a68c0520` | `2E6901A8` | `e961e632ca6f72f81e19c5be3d93936772e8544a` from secondary preservation metadata; cleaner corroboration desired |
| Italy / Italian | `NTR-ADAI-ITA` | `1920fc6a66b3bf4bff2062044f61f4eb` | `1ED511AB` | TBD |

The separate language builds must remain separate targets even where they share a revision number.

## South Korea

Established public facts:

- Korean retail title: `포켓몬스터DP 디아루가` / public technical naming `Pocket Monsters DP - Dialga (Korea)`.
- Product code: `NTR-ADAK-KOR`.
- Release date: **2008-02-14**.
- Korean localization was officially announced/released.
- Public No-Intro-style indexes list the Korean Dialga build as a distinct target.
- Project Pokémon RAM/cheat research uses a Korean-specific address base, independently supporting that the Korean executable/layout cannot be treated as byte-identical to JP/US/EU builds.

References:

- Release/product metadata: <https://gamefaqs.gamespot.com/ds/925601-pokemon-diamond-version/data>
- Contemporary Korean release report: <https://www.gamechosun.co.kr/webzine/article/view.php?no=50842>
- Project Pokémon Korean-specific RAM research: <https://projectpokemon.org/home/profile/57610-deadskullzjr/content/?change_section=1&type=forums_topic_post>

### Hash leads not yet promoted

Public filename/hash lists contain at least two MD5-like values associated with filenames named `Pocket Monsters DP - Dialga (Korea)`:

- `F1AC83C7D2A9368F88EA3848A5E09048`
- `FF3EE65F48530D643FA0BEA83FBD28D7`

These values are **not** currently entered into `VERSIONS.md` because the source does not establish which representation/dump/normalization each value describes. They remain `Unverified leads` until tied to stronger preservation metadata or an independently documented clean-dump identity.

## Australia

Established:

- Product code: `NTR-ADAE-AUS`.
- Release date: **2007-06-21**.
- Barcode reported as `045496738495`, matching the US barcode in some databases even though the packaging/product suffix is Australian.

Revision and binary hash remain `TBD`. Shared barcode, language, or game ID prefix is not sufficient evidence of binary identity with the US build.

## Taiwan and Hong Kong

Taiwan must be modeled as two separate questions:

1. Was the Japanese product distributed/supported in Taiwan?
2. Was there a distinct Taiwan-coded or localized binary?

Contemporary Taiwanese sources support **local distribution and distributor support** by 博優 from the Japanese launch period. No distinct Taiwan-language/Taiwan-coded Diamond binary has yet been established. Later specialist wikis conflict on whether to call Taiwan a “release”; this likely reflects different definitions of local distribution versus dedicated localized edition, but that interpretation remains to be proven.

Hong Kong remains unresolved separately; no equivalent contemporary distribution record has yet been established in this research set.

## Open questions

1. Locate an authoritative No-Intro changelog or database history explaining the English-Europe `Rev 13 -> Rev 5` relabeling.
2. Identify Korean clean-dump SHA-1/MD5/CRC metadata and the underlying revision field from a preservation source.
3. Identify Australian binary identity/revision and test whether it matches any US/EU English build using public metadata only.
4. Locate SHA-1 identities for Spanish and Italian Rev 5.
5. Expand the Japanese revision history without inferring nonexistent intermediate retail revisions.
6. Resolve the exact Japanese revision distributed in Taiwan and investigate Hong Kong independently.

## Verification state

Everything in this note is external-reference research unless a stronger level is explicitly stated elsewhere. No retail ROM was locally observed for this research pass.
