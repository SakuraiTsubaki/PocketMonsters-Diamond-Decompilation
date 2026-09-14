# Manifests

This directory stores inventories for reconstructed source, extracted/recreated assets, hashes, version coverage, and reproducibility metadata.

## Required ideas
- identify the material
- identify the verified target
- record source location or identifier
- record generation/extraction method
- record hashes when identity matters
- record verification level
- record shared byte-identical usage when deduplicated

Use JSON, YAML, CSV, or Markdown tables as appropriate. Do not invent unknown metadata; use `null`, `unknown`, or `TBD` explicitly.

Recommended fields include `id`, `path`, `kind`, `target`, `source`, `size`, `hashes`, `generated_by`, `verification`, `shared_with`, and `notes`.

Do not deduplicate files merely because they look or sound identical. Verify identity using hashes or byte comparison when practical.

See `example.asset-manifest.json` and `../docs/PROJECT_STANDARDS.md`.
