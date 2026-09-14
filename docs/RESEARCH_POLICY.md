# Research Policy — Pocket Monsters Diamond

## Core premise

This project assumes that the researcher has **no original ROM image available**. Research must therefore be reconstructed from publicly accessible material and independently cross-checked wherever possible.

## Historical baseline

The primary baseline is the **earliest officially released Japanese version** of Pocket Monsters Diamond. Every officially released regional, language, and revision variant is investigated as a descendant or sibling of that Japanese-origin baseline.

The goal is not a representative sample. The goal is an **all-region, all-language, all-revision survey**.

## Required research scope

Research includes, without limitation:

- official manuals, websites, guides, announcements, distribution records, and archived material;
- public decompilation/disassembly projects and their history, forks, issues, pull requests, and commits;
- source-reconstruction projects, reverse-engineering notes, file-format research, script-command databases, and tooling;
- executable structures, ARM9/ARM7, overlays, NitroFS, NARC archives, scripts, text, maps, events, graphics, sprites, models, animation, palettes, audio, save data, communication systems, and unused/debug/development remnants;
- version-exclusive data, localization changes, censorship, bug fixes, event differences, distribution content, and regional service differences;
- specialist databases, wikis, forums, archived community research, and other publicly verifiable technical material.

## Comparison rule

Never infer that two versions are identical merely because no difference has yet been found. Use explicit evidence states:

- `CONFIRMED_IDENTICAL`
- `CONFIRMED_DIFFERENT`
- `UNVERIFIED`
- `CONFLICTING_EVIDENCE`

Every confirmed difference should record the Japanese baseline, compared release, component, source, evidence, and verification status.

## Source priority

Prefer, in order:

1. original/official material;
2. reproducible public decompilation/disassembly/source reconstruction;
3. verified reverse-engineering projects and technical tools;
4. specialist databases and wikis;
5. community research and archival material.

Conflicting sources must be preserved and explained rather than silently collapsed.

## GitHub-first results policy

**All research outputs belong in GitHub.** Research notes, source registries, manifests, comparison tables, scripts, extracted/reconstructed non-ROM assets where redistribution is appropriate, metadata, verification results, and changelogs must be committed to this repository or a clearly linked project repository.

ROM images, reconstructed commercial ROM binaries, and other material that should not be redistributed are excluded. Public availability does not automatically imply permission to republish verbatim; provenance and redistribution status must be tracked.

## Minimum provenance fields

Each source/result should record, where applicable:

`GAME / REGION / LANGUAGE / REVISION / RELEASE / COMPONENT / SOURCE / SOURCE_DATE / ORIGINAL_OR_DERIVED / REDISTRIBUTION_STATUS / CONFIDENCE / CROSS_CHECK / DIFFERENCE_FROM_JP_BASELINE`

This policy governs the project unless explicitly superseded by a later documented project-wide decision.
