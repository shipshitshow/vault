#!/usr/bin/env python3
"""Check catalog identity, honest coverage and imported source hashes."""
from pathlib import Path
import csv,json,hashlib
root=Path(__file__).resolve().parents[2]
items=json.loads((root/'catalog.json').read_text())['items']
rows=list(csv.DictReader((root/'_admin/data/youtube-coverage.csv').open()))
assert len({(i['channel'],i['youtube_id']) for i in items})==len(items),'Duplicate catalog identity'
assert {r['youtube_id'] for r in rows}=={i['youtube_id'] for i in items},'Catalog and ledger mismatch'
errors=[]
for i in items:
 p=root/i['overview']
 if not p.is_file():errors.append('Missing overview: '+i['youtube_id']);continue
 t=root/i['transcript'] if i['transcript'] else None
 if t and (not t.is_file() or not t.read_text().strip()):errors.append('Missing/empty transcript: '+i['youtube_id'])
 if bool(t)!=(i['transcript_status']=='archived_in_vault'):errors.append('Coverage mismatch: '+i['youtube_id'])
 if t:
  pp=t.parent/'provenance.json'
  if not pp.is_file():errors.append('Missing provenance: '+i['youtube_id']);continue
  prov=json.loads(pp.read_text())
  if prov['youtube_id']!=i['youtube_id']:errors.append('Provenance identity mismatch: '+i['youtube_id'])
  candidates=list(t.parent.glob('transcript.raw.*'))
  if prov['method']=='historical-vault-import':candidates=[t]
  if not any(hashlib.sha256(p.read_bytes()).hexdigest()==prov['source_sha256'] for p in candidates):errors.append('Source hash mismatch: '+i['youtube_id'])
if errors:raise SystemExit('\n'.join(errors))
print(json.dumps({'known_uploads':len(items),'archived':sum(bool(i['transcript']) for i in items),'validation':'passed'}))
