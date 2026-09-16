#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PATH="$ROOT/vendor/bin:$PATH"
export GEN4_VENDOR_ROOT="$ROOT/vendor"

if [[ "${1:-}" == "--emulator" ]]; then
  shift
  ZIP="$ROOT/vendor/emulators/melonDS-1.1-appimage-x86_64.zip"
  CACHE="$ROOT/.vendor-cache/melonds-1.1"
  mkdir -p "$CACHE"
  if [[ ! -f "$CACHE/.ready" ]]; then
    rm -rf "$CACHE"/*
    unzip -q -o "$ZIP" -d "$CACHE"
    touch "$CACHE/.ready"
  fi
  APPIMAGE="$(find "$CACHE" -maxdepth 2 -type f \( -name '*.AppImage' -o -name 'melonDS' \) | head -n1)"
  if [[ -z "$APPIMAGE" ]]; then
    echo "melonDS executable not found in vendored archive" >&2
    exit 1
  fi
  chmod +x "$APPIMAGE"
  exec "$APPIMAGE" "$@"
fi

if [[ $# -eq 0 ]]; then
  echo "Vendored toolchain active. PATH begins with $ROOT/vendor/bin"
  echo "Run: source tools/use_vendor_toolchain.sh"
  echo "Or:  tools/use_vendor_toolchain.sh <command> [args...]"
  echo "Emulator: tools/use_vendor_toolchain.sh --emulator [ROM]"
  exit 0
fi

exec "$@"
