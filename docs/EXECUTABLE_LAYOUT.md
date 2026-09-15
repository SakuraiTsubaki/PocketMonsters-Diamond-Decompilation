# Executable layout — Diamond

This is the first executable-mapping checkpoint for the decompilation. It records values observed directly from the verified target ROM; it does **not** infer SDK function names or source-level identities.

| Component | ROM offset | Size | Load / RAM address | Entry |
|---|---:|---:|---:|---:|
| ARM9 | `0x4000` | `0x107724` (1,079,076) | `0x02000000` | `0x02000800` |
| ARM7 | `0x30D000` | `0x2931C` (168,732) | `0x02380000` | `0x02380000` |

ARM9 overlays: **87** entries (`0x10B800`, table size `0xAE0`). ARM7 overlays: **0**.

## Phase 1 decompilation boundary

1. Treat the retail ROM as a local, read-only verification input.
2. Extract executable/data components locally; do not commit the ROM image.
3. Keep functions address-named (`sub_XXXXXXXX`) until identity is supported by evidence.
4. Recover function boundaries and call relationships before assigning semantic names.
5. Reconstruct one bounded unit at a time and add matching/reproduction checks as units become source-controlled.

Machine-readable values are in `manifests/executable-layout.json`; the first observed entrypoint window is in `analysis/arm9-entrypoint.md`.
