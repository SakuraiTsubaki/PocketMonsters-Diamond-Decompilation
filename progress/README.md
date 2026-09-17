# Progress

Track evidence-backed milestones rather than estimated percentages.

| Subsystem | State | Evidence | Remaining work |
| --- | --- | --- | --- |
| Exact ROM identity | Verified | [ROM identity](../analysis/rom-identity.md) | Preserve revision-specific comparisons |
| Standard NDS header | Verified | [Structure analysis](../analysis/rom-structure.md) | DSi-only fields are out of scope for this NDS target |
| ARM9 / ARM7 regions | Verified | [Generated structure JSON](../analysis/generated/rom-structure/structure.json) | Executable disassembly and symbols |
| FNT / FAT | Verified | [Files and directories](../analysis/generated/rom-structure/) | Semantic archive relationships |
| NitroFS file inventory | Verified | [File table](../analysis/generated/rom-structure/nitrofs-files.csv) | Per-format parsers |
| ARM9 / ARM7 overlays | Verified | [Overlay tables](../analysis/generated/rom-structure/) | Decompression, disassembly, relocation and call graph |
| Banner/icon/title | Verified | [Structure JSON](../analysis/generated/rom-structure/structure.json) | Rendered visual comparison if needed |
| Secure area | Analysis | [Structure analysis](../analysis/rom-structure.md) | Decrypt and validate secure-area CRC |
| Padding/alignment/gaps | Analysis | [Range table](../analysis/generated/rom-structure/unreferenced-ranges.csv) | Prove code references before calling ranges unused |
| Signature classification | Analysis | [NitroFS table](../analysis/generated/rom-structure/nitrofs-files.csv) | Parse unknown and compressed payloads |
| Source reconstruction | Not started | Structural prerequisites are now recorded | Begin ARM9/overlay function and data reconstruction |
