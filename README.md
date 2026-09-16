# PocketMonsters-Diamond-Decompilation

A complete, target-specific foundation for reproducible research, analysis, tooling, and source reconstruction related to **Pocket Monsters Diamond**.

| Field | Value |
| --- | --- |
| Working target | Pocket Monsters Diamond |
| Platform family | Nintendo DS |
| Series generation | Generation IV |
| Exact build identity | USA / English / `ADAE` / header ROM version 5 |
| Foundation status | Verified by complete-file public target match |

The selected target identity is recorded in `config/target.json` and `analysis/rom-identity.md`. Restricted ROM bytes are not committed. Structural inventory and source reconstruction remain pending.

## Repository areas

| Area | Responsibility |
| --- | --- |
| [`research/`](research/) | Target-specific references, experiments, questions, and methodology. |
| [`analysis/`](analysis/) | Symbols, structures, formats, comparisons, and verified findings. |
| [`tools/`](tools/) | Target adapters and extraction, inspection, conversion, build, and verification utilities. |
| [`src/`](src/) | Reviewed source reconstruction and source-linked data. |
| [`config/`](config/) | Target identity, symbols, mappings, and reproducible tool/build configuration. |
| [`tests/`](tests/) | Unit, regression, comparison, and build-verification checks. |
| [`progress/`](progress/) | Evidence-based milestones and unresolved blockers. |
| [`docs/`](docs/) | Target workflow and architecture documentation. |

Target-independent methods and tools belong in [`SakuraiTsubaki/Decompilation`](https://github.com/SakuraiTsubaki/Decompilation).

## Start here

1. Complete the identity checklist in [`PROJECT.md`](PROJECT.md).
2. Replace the unselected fields in [`config/target.json`](config/target.json) with verified identifiers.
3. Open a focused research record from [`research/template.md`](research/template.md).
4. Promote reproducible conclusions through [`analysis/template.md`](analysis/template.md).
5. Add target-specific tooling with tests and documented inputs/outputs.
6. Run `python scripts/check_repository.py .` and the unit tests before review.

## Non-negotiable rules

- Record provenance, hashes, versions, commands, environment, and confidence.
- Distinguish Confirmed, Probable, and Hypothesis conclusions.
- Never commit copyrighted game images, firmware, keys, credentials, or locally extracted proprietary content.
- Keep generated output separate from reviewed source and analysis.
- Add concrete work, not invented completion percentages or placeholder source trees.
