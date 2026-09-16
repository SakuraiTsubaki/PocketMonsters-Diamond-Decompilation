# PocketMonsters-Diamond-Decompilation

A clean, target-specific workspace for research, analysis, and tooling related to decompiling **Pocket Monsters Diamond**.

This repository intentionally starts without migrated code, assets, assumptions, or progress claims.

## Target identity

The repository name identifies the working target. Before adding target data, record the exact release, region, revision, executable or image hashes, tool versions, and any other identifiers needed to reproduce the work. Do not assume that findings transfer between builds.

## Scope

| Area | Purpose |
| --- | --- |
| [`research/`](research/) | Target-specific references, experiments, questions, and methodology. |
| [`analysis/`](analysis/) | Reproducible findings, symbols, structures, formats, comparisons, and verification records. |
| [`tools/`](tools/) | Target-specific extraction, inspection, conversion, build, and verification utilities. |

Reusable, target-independent methods and tools belong in [`SakuraiTsubaki/Decompilation`](https://github.com/SakuraiTsubaki/Decompilation). This repository should contain only work whose scope or behavior is specific to Pocket Monsters Diamond.

## Working rules

- Record input provenance, hashes, versions, commands, and confidence.
- Separate confirmed findings from probable interpretations and hypotheses.
- Keep generated output distinct from reviewed source and analysis.
- Do not commit copyrighted game images, firmware, credentials, private keys, or locally extracted proprietary content.
- Add directories only when concrete work needs them; avoid placeholder trees.
