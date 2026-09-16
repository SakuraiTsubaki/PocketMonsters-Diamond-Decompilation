# Target Profile: Pocket Monsters Diamond

## Known repository scope

- Repository: `SakuraiTsubaki/PocketMonsters-Diamond-Decompilation`
- Working target name: Pocket Monsters Diamond
- Platform family: Nintendo DS
- Series generation: Generation IV
- Exact release, region, revision, and build: **USA English, game code `ADAE`, header ROM version `5`; complete-file public target match confirmed**

The repository name is a working label, not proof of a particular binary. No address, symbol, format, or behavior should be treated as target fact until the exact build is identified.

## Selected identifiers

- Official/localized title: Pokémon Diamond Version
- Game code: `ADAE`
- Header title: `POKEMON D`
- Region and language: USA, English
- Header ROM version: `5`
- Complete ROM size: `67108864` bytes
- SHA-256: `e29bc6ebe431d7a6b238267b6b1521fec4a3bc14f2fa348798062f870c738454`
- Evidence record: [`analysis/rom-identity.md`](analysis/rom-identity.md)

## Identity checklist

Record all available items before substantive reconstruction:

- official title and product identifier;
- platform and execution environment;
- region, language, revision, update, and distribution form;
- hashes for user-supplied images, executables, modules, or manifests;
- executable/container layout and relevant segment identifiers;
- analysis, extraction, compiler, linker, and SDK tool versions;
- legal provenance and distribution constraints for every input;
- differences from related versions that affect addresses, formats, or behavior.

Store machine-readable identifiers in `config/target.json`. Store restricted inputs outside Git.

## Initial research priorities

- Fingerprint the exact game revision and inventory the ROM header, FNT/FAT, NitroFS, and overlay tables.
- Separate ARM9, ARM7, and overlay code/data with explicit load addresses and build identifiers.
- Document Nitro and target-specific archives, compression, graphics, text, audio, maps, and scripts.
- Identify compiler/SDK fingerprints and preserve version-specific symbol and address mappings.
- Build deterministic extraction, overlay, and comparison tools around user-supplied inputs.

## First milestone

The foundation milestone is complete when the exact target build is recorded, the initial file/executable map is reproducible, at least one research record has been promoted to an analysis with stated confidence, and all commands needed to repeat that result are documented.
