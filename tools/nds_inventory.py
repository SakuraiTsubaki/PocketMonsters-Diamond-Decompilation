#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, struct, csv
from pathlib import Path
from collections import Counter


def u16(b,o): return struct.unpack_from('<H', b, o)[0]
def u32(b,o): return struct.unpack_from('<I', b, o)[0]

def crc16_nintendo(data: bytes, init=0xFFFF):
    crc = init
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = (crc >> 1) ^ (0xA001 if crc & 1 else 0)
    return crc & 0xFFFF

def hash_file(path: Path):
    hs={k:hashlib.new(k) for k in ('md5','sha1','sha256')}
    with path.open('rb') as f:
        while True:
            c=f.read(1024*1024)
            if not c: break
            for h in hs.values(): h.update(c)
    return {k:h.hexdigest() for k,h in hs.items()}

def parse_fnt(rom: bytes, fnt_off: int, fnt_size: int, fat_entries):
    fnt=rom[fnt_off:fnt_off+fnt_size]
    if len(fnt)<8: return []
    dir_count=u16(fnt,6)
    dirs={}
    for i in range(dir_count):
        off=i*8
        if off+8>len(fnt): break
        dir_id=0xF000+i
        dirs[dir_id]={'subtable_offset':u32(fnt,off),'first_file_id':u16(fnt,off+4),'parent':u16(fnt,off+6)}
    files=[]; visiting=set()
    def walk(dir_id, prefix=''):
        if dir_id in visiting or dir_id not in dirs: return
        visiting.add(dir_id); ent=dirs[dir_id]; pos=ent['subtable_offset']; fid=ent['first_file_id']
        while pos < len(fnt):
            tag=fnt[pos]; pos += 1
            if tag==0: break
            is_dir=bool(tag & 0x80); nlen=tag & 0x7F
            if pos+nlen>len(fnt): break
            name=fnt[pos:pos+nlen].decode('ascii','replace'); pos += nlen
            if is_dir:
                if pos+2>len(fnt): break
                sub=u16(fnt,pos); pos += 2; walk(sub, prefix+name+'/')
            else:
                start=end=None
                if fid < len(fat_entries): start,end=fat_entries[fid]
                files.append({'file_id':fid,'path':prefix+name,'start':start,'end':end,'size':None if start is None else end-start}); fid += 1
        visiting.remove(dir_id)
    walk(0xF000,''); return files

def parse_overlays(rom, off, size, fat_entries):
    out=[]
    for p in range(off, off+size, 32):
        if p+32>len(rom): break
        ov_id,ram_addr,ram_size,bss,si_start,si_end,file_id,flags=struct.unpack_from('<8I',rom,p)
        fs=fe=None
        if file_id < len(fat_entries): fs,fe=fat_entries[file_id]
        out.append({'overlay_id':ov_id,'ram_address':ram_addr,'ram_size':ram_size,'bss_size':bss,'static_init_start':si_start,'static_init_end':si_end,'file_id':file_id,'flags':flags,'file_start':fs,'file_end':fe,'file_size':None if fs is None else fe-fs})
    return out

def decode_ascii(raw): return raw.split(b'\0',1)[0].decode('ascii','replace').rstrip()

def inventory(path: Path):
    rom=path.read_bytes(); hdr=rom[:0x200]; fat_off,fat_size=u32(hdr,0x48),u32(hdr,0x4C)
    fat=[(u32(rom,p),u32(rom,p+4)) for p in range(fat_off,fat_off+fat_size,8) if p+8<=len(rom)]
    info={'file_name':path.name,'file_size':len(rom),'hashes':hash_file(path),'title':decode_ascii(hdr[0:12]),'game_code':decode_ascii(hdr[0x0C:0x10]),'maker_code':decode_ascii(hdr[0x10:0x12]),'unit_code':hdr[0x12],'device_type':hdr[0x13],'device_capacity_code':hdr[0x14],'rom_version':hdr[0x1E],'autostart':hdr[0x1F],'arm9':{'rom_offset':u32(hdr,0x20),'entry_address':u32(hdr,0x24),'ram_address':u32(hdr,0x28),'size':u32(hdr,0x2C)},'arm7':{'rom_offset':u32(hdr,0x30),'entry_address':u32(hdr,0x34),'ram_address':u32(hdr,0x38),'size':u32(hdr,0x3C)},'fnt':{'offset':u32(hdr,0x40),'size':u32(hdr,0x44)},'fat':{'offset':fat_off,'size':fat_size,'entry_count':len(fat)},'arm9_overlay_table':{'offset':u32(hdr,0x50),'size':u32(hdr,0x54)},'arm7_overlay_table':{'offset':u32(hdr,0x58),'size':u32(hdr,0x5C)},'banner_offset':u32(hdr,0x68),'declared_rom_size':u32(hdr,0x80),'header_size':u32(hdr,0x84),'header_crc_stored':u16(hdr,0x15E),'header_crc_calculated':crc16_nintendo(hdr[:0x15E])}
    info['header_crc_match']=info['header_crc_stored']==info['header_crc_calculated']
    files=parse_fnt(rom,info['fnt']['offset'],info['fnt']['size'],fat); info['nitrofs']={'file_count':len(files)}
    ext=Counter(); top=Counter()
    for f in files:
        p=Path(f['path']); ext[p.suffix.lower() or '<none>']+=1; top[f['path'].split('/',1)[0] if '/' in f['path'] else '<root>']+=1
    info['nitrofs']['extensions']=dict(ext.most_common()); info['nitrofs']['top_level_counts']=dict(top.most_common())
    a9o=parse_overlays(rom,info['arm9_overlay_table']['offset'],info['arm9_overlay_table']['size'],fat); a7o=parse_overlays(rom,info['arm7_overlay_table']['offset'],info['arm7_overlay_table']['size'],fat); info['overlays']={'arm9_count':len(a9o),'arm7_count':len(a7o)}
    return info,files,a9o,a7o

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('roms',nargs='+'); ap.add_argument('-o','--out',required=True); args=ap.parse_args(); out=Path(args.out); out.mkdir(parents=True,exist_ok=True); allinfo=[]
    for rp in args.roms:
        p=Path(rp); info,files,a9o,a7o=inventory(p); allinfo.append(info); stem=info['game_code'] or p.stem
        (out/f'{stem}.inventory.json').write_text(json.dumps(info,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        for name,rows in [('nitrofs',files),('arm9_overlays',a9o),('arm7_overlays',a7o)]:
            if not rows: continue
            with (out/f'{stem}.{name}.csv').open('w',newline='',encoding='utf-8') as f:
                w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    (out/'gen4_inventory.json').write_text(json.dumps(allinfo,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(allinfo,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
