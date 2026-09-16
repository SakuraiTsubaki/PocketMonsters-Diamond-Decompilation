#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class Check:
    name: str
    kind: str
    required: bool
    path: str | None
    version: str | None
    ok: bool
    note: str = ""


def first_command(*names: str) -> str | None:
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    return None


def command_version(path: str | None, args: list[str]) -> str | None:
    if not path:
        return None
    try:
        p = subprocess.run([path, *args], text=True, capture_output=True, timeout=8, check=False)
    except Exception:
        return None
    text = (p.stdout or p.stderr).strip().splitlines()
    return text[0][:240] if text else None


def main() -> int:
    specs = [
        ("git", ("git",), ["--version"], True),
        ("python3", ("python3",), ["--version"], True),
        ("make", ("make",), ["--version"], True),
        ("cmake", ("cmake",), ["--version"], False),
        ("ninja", ("ninja",), ["--version"], False),
        ("clang", ("clang",), ["--version"], True),
        ("llvm-objdump", ("llvm-objdump",), ["--version"], True),
        ("llvm-objcopy", ("llvm-objcopy",), ["--version"], True),
        ("arm-none-eabi-objdump", ("arm-none-eabi-objdump",), ["--version"], True),
        ("arm-none-eabi-gcc", ("arm-none-eabi-gcc",), ["--version"], False),
        ("gdb", ("arm-none-eabi-gdb", "gdb-multiarch", "gdb"), ["--version"], False),
        ("wine", ("wine64", "wine"), ["--version"], False),
        ("ndstool", ("ndstool",), ["-?"], False),
        ("melonDS", ("melonDS", "melonds"), ["--help"], True),
        ("DeSmuME", ("desmume", "desmume-cli"), ["--version"], False),
        ("dkp-pacman", ("dkp-pacman",), ["--version"], False),
    ]

    checks: list[Check] = []
    for label, commands, args, required in specs:
        path = first_command(*commands)
        checks.append(Check(label, "command", required, path, command_version(path, args), bool(path)))

    for module, required in (("capstone", False), ("construct", False), ("ndspy", False), ("lief", False)):
        spec = importlib.util.find_spec(module)
        checks.append(Check(module, "python-module", required, getattr(spec, "origin", None) if spec else None, None, spec is not None))

    devkitpro = Path(os.environ.get("DEVKITPRO", "/opt/devkitpro"))
    devkitarm = Path(os.environ.get("DEVKITARM", devkitpro / "devkitARM"))
    checks.append(Check("DEVKITPRO", "directory", False, str(devkitpro), None, devkitpro.is_dir()))
    checks.append(Check("DEVKITARM", "directory", False, str(devkitarm), None, devkitarm.is_dir()))

    mwcc = os.environ.get("MWCCARM_ROOT")
    nitro = os.environ.get("NITROSDK_ROOT")
    checks.append(Check("MWCCARM_ROOT", "proprietary", False, mwcc, None, bool(mwcc and Path(mwcc).exists()), "user-supplied only"))
    checks.append(Check("NITROSDK_ROOT", "proprietary", False, nitro, None, bool(nitro and Path(nitro).exists()), "user-supplied only"))

    for c in checks:
        flag = "OK" if c.ok else ("MISSING" if c.required else "optional")
        print(f"{flag:8} {c.name:22} {c.path or '-'}")

    out = Path("build/toolchain-report.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"schema_version": 1, "checks": [asdict(c) for c in checks]}, indent=2) + "\n", encoding="utf-8")
    print(f"Report: {out}")

    missing = [c.name for c in checks if c.required and not c.ok]
    if missing:
        print("Missing required tools: " + ", ".join(missing))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
