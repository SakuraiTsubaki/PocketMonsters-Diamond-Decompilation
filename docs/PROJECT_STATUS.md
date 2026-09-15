# Project Status

**Current stage:** Phase 1 — executable / startup reconstruction

The verified Diamond target is registered and the project has moved beyond metadata-only setup. ARM9/ARM7 layout, NitroFS, overlay inventory, executable hashes, and the first ARM9 startup symbol boundaries are now recorded.

## Progress
- [x] Establish repository baseline and ROM/key exclusion rules
- [x] Add deterministic target inventory tooling
- [x] Add machine-readable version inventory and CI
- [x] Inventory the verified Diamond target
- [x] Record region/language/revision/hash metadata
- [x] Inventory NitroFS and ARM9 overlay table
- [x] Record ARM9/ARM7 executable layout and component hashes
- [x] Establish an LLVM raw-ARM analysis workflow
- [x] Map the first ARM9 startup/runtime symbols from `0x02000800`
- [ ] Extend ARM9 function-boundary and call-graph mapping beyond `NitroMain`
- [ ] Classify ARM9 overlays by subsystem and map their functions
- [ ] Map ARM7 runtime and game-specific code
- [ ] Document NARC/data formats and resource containers
- [ ] Begin bounded C/source reconstruction of game-specific units
- [ ] Add byte/matching reconstruction verification

Machine-readable inventories live under `manifests/`. Startup work is tracked in `analysis/arm9-entrypoint.md`.

## Immediate next milestone
Follow the ARM9 startup transfer into `NitroMain`, separate SDK/runtime code from game code, establish address-based function boundaries and call edges, then begin overlay-by-overlay reconstruction. Retail ROM bytes remain local and read-only.
