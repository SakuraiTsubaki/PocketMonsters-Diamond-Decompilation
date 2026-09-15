# ARM9 `NitroMain` analysis

## Verified target
- Game: Pokémon Diamond
- Game code: `ADAE`
- Region/language: USA / English
- ROM identity: `manifests/rom-baseline.json`

## Entry and boundary
- `_start` loads `0x02000C55`; bit 0 selects Thumb state.
- `NitroMain` Thumb entry: `0x02000C54`.
- Observed main-function instruction/literal boundary: `0x02000C54..0x02000DCF`.
- Literal pool begins at `0x02000DD0`.
- Code span size: `0x17C` (380) bytes.
- SHA-256 of that observed code span: `5692ce498a0043e64315558ef7fc303ead87b3fcfeeafd7a2f369444887d24e7`.
- Call sites in the observed body: 46 total, including one register-indirect `BLX` callback site.

## Matched high-level flow
The local machine code matches the `NitroMain` organization reconstructed by `pret/pokediamond`: system/graphics/input setup, backlight and RTC initialization, main overlay state initialization, font heap setup, save-data creation, sound/timer startup, WFC/save checks, reset-parameter based first-overlay selection, RNG/brightness/play-time initialization, then the permanent per-frame loop.

The main loop performs communication/update work, overlay-manager execution, task processing, VBlank waits/counters, RTC/play-time updates, brightness and sound updates, and an optional VBlank callback before looping.

## Cross-version result
The complete 380-byte observed `NitroMain` code span is byte-for-byte identical in the uploaded Pearl USA target. The D/P split therefore occurs outside this common main loop for the targets currently under analysis.

## Evidence
- Local target disassembly produced from the uploaded ROM.
- Startup literal target and Thumb-state bit from `_start`.
- Cross-check: `pret/pokediamond`, `arm9/src/main.c` and NitroSDK `crt0.c`.

## Next mapping pass
1. Assign verified names to every direct-call target in this function.
2. Separate SDK/runtime calls from Game Freak engine calls.
3. Follow `Main_RunOverlayManager` and the first title/start overlays.
4. Build a machine-readable direct-call manifest and cross-version correspondence table.
