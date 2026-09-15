#!/usr/bin/env python3
"""Wrap a raw ARM binary in a temporary ELF for analysis with LLVM tools.

This does not modify the binary. It is intended for build/ or another ignored
local directory and is not a matching-linker workflow by itself.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def require(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise SystemExit(f"required tool not found in PATH: {name}")
    return path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("binary", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--load-address", required=True, type=lambda x: int(x, 0))
    ap.add_argument("--entry-address", required=True, type=lambda x: int(x, 0))
    args = ap.parse_args()

    objcopy = require("llvm-objcopy")
    lld = require("ld.lld")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw_obj = args.output.with_suffix(args.output.suffix + ".raw.o")

    subprocess.run(
        [
            objcopy,
            "-I", "binary",
            "-O", "elf32-littlearm",
            "-B", "arm",
            str(args.binary),
            str(raw_obj),
            "--rename-section", ".data=.text,alloc,load,readonly,code",
        ],
        check=True,
    )
    subprocess.run(
        [
            lld,
            "-m", "armelf",
            f"-Ttext=0x{args.load_address:08x}",
            "-e", f"0x{args.entry_address:08x}",
            "-o", str(args.output),
            str(raw_obj),
        ],
        check=True,
    )
    raw_obj.unlink(missing_ok=True)
    print(args.output)


if __name__ == "__main__":
    main()
