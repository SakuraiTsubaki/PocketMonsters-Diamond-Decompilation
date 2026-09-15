#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, re, shutil, subprocess
from pathlib import Path

LINE_RE = re.compile(r"^\s*([0-9a-fA-F]+):\s+[0-9a-fA-F ]+\s+(.+)$")
IMM_CALL_RE = re.compile(r"\b(blx|bl)\s+0x([0-9a-fA-F]+)")
REG_CALL_RE = re.compile(r"\bblx\s+(r\d+|lr|ip)\b", re.I)

def parse_int(value: str) -> int:
    return int(value, 0)

def main() -> None:
    ap = argparse.ArgumentParser(description="Extract Thumb BL/BLX call sites from an ARM ELF using llvm-objdump.")
    ap.add_argument("elf", type=Path)
    ap.add_argument("--start", type=parse_int, required=True)
    ap.add_argument("--end", type=parse_int, required=True, help="exclusive virtual address")
    ap.add_argument("-o", "--out", type=Path, required=True)
    ap.add_argument("--objdump", default="llvm-objdump")
    args = ap.parse_args()
    objdump = shutil.which(args.objdump) or args.objdump
    proc = subprocess.run([objdump, "-D", "-j", ".data", "--triple=thumbv5te-none-eabi", "--adjust-vma=0x02000000", str(args.elf)], check=True, text=True, capture_output=True)
    rows = []
    for line in proc.stdout.splitlines():
        m = LINE_RE.match(line)
        if not m:
            continue
        addr = int(m.group(1), 16)
        if not (args.start <= addr < args.end):
            continue
        ins = m.group(2)
        cm = IMM_CALL_RE.search(ins)
        if cm:
            rows.append({"site": f"0x{addr:08X}", "kind": cm.group(1), "target": f"0x{int(cm.group(2),16):08X}", "notes": "direct immediate target"})
            continue
        rm = REG_CALL_RE.search(ins)
        if rm:
            rows.append({"site": f"0x{addr:08X}", "kind": "blx_reg", "target": "", "notes": f"indirect call via {rm.group(1).lower()}"})
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["site", "kind", "target", "notes"])
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} call sites to {args.out}")

if __name__ == "__main__":
    main()
