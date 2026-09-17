# NARC and member inventory

## Provenance

- Input: `Pokémon Diamond Version (USA, ADAE, header ROM version 5)`
- ROM SHA-256: `e29bc6ebe431d7a6b238267b6b1521fec4a3bc14f2fa348798062f870c738454`
- Tool: `narc_inventory 1.0.0`
- ROM bytes committed: **no**

## Confirmed totals

| Metric | Count |
| --- | ---: |
| Top-level NARC candidates | 149 |
| Valid top-level NARCs | 149 |
| Malformed top-level NARCs | 0 |
| Nested NARCs | 0 |
| Total members, including nested containers | 33953 |
| Named members | 0 |
| Compression-marker members (Probable or Confirmed) | 3462 |
| Structurally decoded LZ10/LZ11 members (Confirmed) | 1885 |
| Invalid LZ-like leading markers | 286 |
| Huffman/RLE markers not decoded in this phase | 1291 |
| Unknown members | 23233 |

## Evidence language

Offsets, sizes, hashes, block layouts, and successful structural checks are **Confirmed**. A leading magic or compression marker without complete structural validation remains **Probable**. No semantic field names are inferred from payload shape alone.

No raw member payload is retained. `narc-inventory.json` and the CSV files preserve the complete reproducible structure and hash evidence.
