# Vendored portable tools

This directory is populated by `.github/workflows/vendor-portable-tools.yml` so a checked-out repository already contains the core open-source reverse-engineering tools needed for this project.

Committed portable payload:

- `vendor/bin/arm-none-eabi-{as,ld,objcopy,objdump,nm,readelf,size,strip}`
- `vendor/bin/gdb-multiarch`
- `vendor/bin/ndstool`
- `vendor/bin/xdelta3`
- `vendor/bin/bsdiff` and `bspatch`
- `vendor/bin/ninja`
- `vendor/emulators/melonDS-1.1-appimage-x86_64.zip`
- license/copyright notices and `vendor/SHA256SUMS`

Use the binaries directly through `tools/use_vendor_toolchain.sh`; no system-wide installation is required.

## Deliberately not vendored

Retail ROM images are never committed. Nintendo proprietary SDK files and proprietary Metrowerks compiler binaries are also not downloaded or redistributed by this repository. Matching-build work detects user-provided licensed copies separately.

The vendored bundle targets Linux x86_64, matching the current automated reverse-engineering environment. Other host architectures may use the bootstrap script or add a separately verified portable bundle.
