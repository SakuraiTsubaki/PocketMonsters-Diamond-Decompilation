# ARM9 entrypoint — Phase 1

Target: `ADAE` / USA English / ROM version byte `5`.

## Observed boundaries

| Address | Working identity | Evidence |
|---:|---|---|
| `0x02000800` | `_start` | Exact entrypoint; instruction sequence matches NitroSDK startup reconstruction |
| `0x0200093C` | `INITi_CpuClear32` | Three direct calls from startup; exact instruction sequence match |
| `0x02000950` | `MIi_UncompressBackward` | Direct call from startup; exact instruction sequence match |
| `0x020009FC` | `do_autoload` | Direct call from startup; exact instruction sequence match |
| `0x02000A78` | `init_cp15` | First startup call; exact instruction sequence match |
| `0x02000B64` | `NitroStartUp` | Startup call order and reference match |
| `0x020EC5CC` | `_fp_init` | Startup call order and reference match |
| `0x020EC694` | `__call_static_initializers` | Startup call order and reference match |

The `NitroMain` literal used by `_start` is `0x02000C55`; bit 0 marks a Thumb entry, giving code address `0x02000C54`.

## Startup behavior

The entrypoint disables IME, waits for VCOUNT zero, initializes CP15, creates SVC/IRQ/system stacks, clears DTCM/palette/OAM, decompresses and loads autoload blocks, clears static BSS and cache lines, installs the interrupt vector, runs floating-point/static initialization, then transfers to `NitroMain`.

## Cross-version fingerprint

The first `0x200` bytes (`0x02000800`–`0x02000A00`) are byte-for-byte identical between the verified Diamond and Pearl targets. This makes the block a strong shared-runtime anchor before game-specific reconstruction.

## Confidence

- Addresses and bytes: **Observed** from the verified local ROM.
- Function identities above: **Reference-supported** by the matching `pret/pokediamond` NitroSDK `crt0.c` reconstruction.
- Game-specific semantic functions beyond this startup chain remain address-named until separately verified.
