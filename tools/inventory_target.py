#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from datetime import datetime,timezone
from pathlib import Path
SENSITIVE_FILENAMES={"prod.keys","title.keys"}; SENSITIVE_SUFFIXES={".keys"}; CHUNK=1024*1024
def digest(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(CHUNK),b''): d.update(b)
 return d.hexdigest()
def sensitive(p): return p.name.lower() in SENSITIVE_FILENAMES or p.suffix.lower() in SENSITIVE_SUFFIXES
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('target',type=Path); ap.add_argument('--target-id',required=True); ap.add_argument('--product',required=True); ap.add_argument('--region',default='TBD'); ap.add_argument('--language',default='TBD'); ap.add_argument('--version',default='TBD'); ap.add_argument('--update',default='base'); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); t=a.target.resolve()
 if not t.exists(): raise SystemExit(f'Target does not exist: {t}')
 pairs=[(t,Path(t.name))] if t.is_file() else [(p,p.relative_to(t)) for p in sorted(x for x in t.rglob('*') if x.is_file())]
 files=[]; omitted=0; total=0
 for p,r in pairs:
  if sensitive(p): omitted+=1; continue
  s=p.stat().st_size; total+=s; files.append({'path':r.as_posix(),'size':s,'sha256':digest(p),'suffix':p.suffix.lower()})
 out={'schema_version':1,'target_id':a.target_id,'product':a.product,'region':a.region,'language':a.language,'version':a.version,'update':a.update,'verification':'Observed','generated_at_utc':datetime.now(timezone.utc).isoformat(),'source_kind':'file' if t.is_file() else 'directory','source_name':t.name,'file_count':len(files),'total_bytes':total,'omitted_sensitive_files':omitted,'files':files,'notes':['Metadata only; no retail payloads, keys, or absolute paths are embedded.']}
 a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
if __name__=='__main__': main()
