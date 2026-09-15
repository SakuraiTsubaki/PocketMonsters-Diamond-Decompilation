# Project Status

**Current stage:** Phase 0 — target identity / reproducibility baseline

Initial setup is complete. Metadata-only target inventory tooling and CI are active.

## Progress
- [x] Establish repository baseline and ROM/key exclusion rules
- [x] Add deterministic target inventory tooling
- [x] Add machine-readable version inventory and CI
- [ ] Inventory the first verified Diamond target
- [ ] Record region/language/revision/hash metadata
- [ ] Document NDS executable, overlay, NitroFS, and address-space layout
- [ ] Map symbols, functions, and major subsystems
- [ ] Document NARC/data formats and resource containers
- [ ] Begin bounded source reconstruction
- [ ] Add reconstruction matching verification

Machine-readable inventory: `manifests/version-inventory.json`

## Immediate next milestone
Run `tools/inventory_target.py` on the first local Diamond target, register exact identity, then begin ARM9/ARM7/overlay/NitroFS mapping. Retail bytes remain local and read-only.
