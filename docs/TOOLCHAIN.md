# Toolchain — Diamond

This repository uses a layered Nintendo DS reverse-engineering toolchain. Open-source tools are installed reproducibly; proprietary matching-build components are detected but never downloaded or committed automatically.

## Install

```sh
bash tools/bootstrap_nds_toolchain.sh
source "$HOME/.local/share/pokemon-gen4-nds-toolchain/toolchain.env"
python3 tools/check_toolchain.py
```

Set `GEN4_TOOL_ROOT=/custom/path` before running the bootstrap script if the default user-space install location is not desired.

## Common open-source layer

The bootstrap installs or prepares:

- Git, Python 3, Make, CMake, Ninja
- Clang/LLVM and LLD
- GNU Arm Embedded binutils, optional GCC, and multi-arch GDB
- Wine for Windows-hosted matching compilers when a legally obtained compiler is supplied locally
- `libpng`, `pkg-config`, and `pugixml` development dependencies
- `ndstool` for Nintendo DS image unpack/build inspection
- devkitPro `nds-dev` / devkitARM / libnds for NDS development and auxiliary test programs
- Python RE helpers: Capstone, Construct, ndspy, with LIEF as an optional extra
- melonDS as the primary emulator; DeSmuME is installed from the host package manager when available as a secondary emulator
- xdelta3 and bsdiff when available for patch/diff workflows

## Emulator policy

Primary emulator: **melonDS 1.1**. The bootstrap downloads the official Linux release for the host architecture and verifies the release-provided SHA-256 when GitHub exposes it. For Linux x86_64, the 1.1 Ubuntu asset SHA-256 is `99465129f5413b2aad332e4377e523cf3cda905dc329d47dcb1ad01ce2cb3f66`.

BIOS, firmware, retail ROM images, save files copied from retail hardware, and other proprietary console data are not downloaded or committed by the setup script. Supply such material locally only when a test explicitly requires it.

## Matching-build layer

External US D/P matching reference uses Metrowerks MWCC 2.0/sp1 plus 1.2/sp2p3 and NitroSDK 3.2-060901. Treat this as reference evidence for the current USA target, not as proof for every reconstructed source unit.

Use these environment variables when those user-supplied components are available:

```sh
export MWCCARM_ROOT=/path/to/mwccarm
export NITROSDK_ROOT=/path/to/NitroSDK
```

`tools/check_toolchain.py` records whether those paths are present but does not require them for normal analysis.

## Verification

`python3 tools/check_toolchain.py` writes `build/toolchain-report.json`. The report is local build output and should not be committed as authoritative project data.

The repository must continue to distinguish:

- analysis-capable open-source toolchain
- externally referenced matching toolchain
- independently verified matching toolchain for this exact region/language/revision

Do not promote a reference compiler/SDK version to verified status without executable/build evidence for this target.
