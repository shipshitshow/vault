#!/usr/bin/env python3
"""Import an authorized local ASR text handoff; never uploads or downloads media."""
from pathlib import Path
import argparse,csv,hashlib,json,shutil
from datetime import datetime,timezone
parser=argparse.ArgumentParser()
parser.add_argument('--recovery-dir',type=Path,required=True)
parser.add_argument('--vault',type=Path,default=Path(__file__).resolve().parents[2])
parser.add_argument('--import-date',default=datetime.now(timezone.utc).date().isoformat())
args=parser.parse_args();root=args.vault.resolve();recovery=args.recovery_dir.resolve()
ledger=root/'_admin/data/youtube-coverage.csv';rows=list(csv.DictReader(ledger.open()))
by_id={r['youtube_id']:r for r in rows}
channels={'UCxuriP32znodU-8N7zkwuew':'shipshitshow','UCYX8Z9u0cP4T7Dpnm0EcT5Q':'shipshitshowclips'}
imported=0
for source in sorted(recovery.glob('*.txt')):
 id=source.stem;mp=recovery/(id+'.metadata.json')
 if not mp.is_file() or not source.read_text().strip():continue
 meta=json.loads(mp.read_text())
 if meta.get('channel_id') not in channels:raise ValueError('Unexpected channel for '+id)
 if meta.get('id')!=id:raise ValueError('Identity mismatch for '+id)
 channel=channels[meta['channel_id']];date=meta.get('upload_date','')
 published=date[:4]+'-'+date[4:6]+'-'+date[6:] if len(date)==8 else ''
 fmt='short' if channel=='shipshitshowclips' else 'livestream' if meta.get('live_status')=='was_live' else 'video'
 r=by_id.get(id)
 if r is None:
  r={k:'' for k in rows[0]};r.update(youtube_id=id,channel=channel,format=fmt,title=meta['title'],url='https://www.youtube.com/watch?v='+id,seen_in_july_inventory='no',seen_in_public_tab_2026_10_02='no',visibility_note='Located through original episode notes and verified channel metadata; public-tab visibility unresolved')
  rows.append(r);by_id[id]=r
 if r['channel'] != channel or r['format'] != fmt:
  raise ValueError('Ledger channel/format mismatch for '+id)
 if r['vault_transcript']:continue
 r.update(title=meta['title'],published_at=published)
 base='shipshitshowclips/Shorts' if channel=='shipshitshowclips' else 'shipshitshow/'+('Livestreams' if r['format']=='livestream' else 'Videos')
 d=root/base/(published+'-'+id if published else 'unknown-date/'+id)
 old=root/r['vault_overview'] if r['vault_overview'] else None
 if old and old.parent!=d:
  if d.exists():raise ValueError('Destination collision: '+str(d))
  d.parent.mkdir(parents=True,exist_ok=True);old.parent.rename(d)
 else:d.mkdir(parents=True,exist_ok=True)
 fields={'title':meta['title'],'type':'stream' if r['format']=='livestream' else r['format'],'date':published or None,'published_at':published or None,'youtube_id':id,'youtube_url':r['url'],'channel':channel,'channel_id':meta['channel_id'],'transcript_status':'asr-unreviewed','source':'youtube','youtube_tags':meta.get('tags') or []}
 (d/'overview.md').write_text('---\n'+'\n'.join(k+': '+json.dumps(v,ensure_ascii=False) for k,v in fields.items())+'\n---\n\n# '+meta['title']+'\n\n## Links\n\n- YouTube: '+r['url']+'\n\n## Archive state\n\nAutomatic local transcription; wording, names and numbers require review. Source clock belongs to this published asset.\n')
 (d/'transcript.md').write_text('# Transcript\n\nLocal Whisper automatic English transcription (model recorded in provenance), imported '+args.import_date+'. No speaker identities inferred. ASR names, numbers and wording are unreviewed. This uses the published asset\'s own clock.\n\n'+source.read_text().strip()+'\n')
 shutil.copyfile(source,d/'transcript.raw.txt')
 for suffix,target in [('.srt','captions.srt'),('.vtt','captions.vtt'),('.json','transcript.asr.json')]:
  p=recovery/(id+suffix)
  if p.is_file():
   if suffix=='.json':
    raw=json.loads(p.read_text())
    for key in ['file','model']:
     if isinstance(raw.get('params',{}).get(key),str):raw['params'][key]=Path(raw['params'][key]).name
    (d/target).write_text(json.dumps(raw,indent=2)+'\n')
   else:shutil.copyfile(p,d/target)
 if meta.get('description'):(d/'description.md').write_text(meta['description'].rstrip()+'\n')
 provenance={'youtube_id':id,'channel_id':meta['channel_id'],'imported_on':args.import_date,'method':'local-whisper.cpp','model':meta.get('asr_model','unknown'),'language':'en','clock':'published-asset','review_status':'asr-unreviewed','source_url':r['url'],'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'audio_sha256':meta.get('audio_sha256'),'visibility_note':r['visibility_note']}
 (d/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
 r.update(vault_overview=(d/'overview.md').relative_to(root).as_posix(),vault_transcript=(d/'transcript.md').relative_to(root).as_posix(),coverage_status='archived_in_vault')
 imported+=1
with ledger.open('w') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
(root/'catalog.json').write_text(json.dumps({'observed_on':args.import_date,'completeness':'known-tabs-plus-historical-inventory-and-verified-episode-links; lower-bound','items':[{'youtube_id':r['youtube_id'],'channel':r['channel'],'format':r['format'],'title':r['title'],'url':r['url'],'published_at':r['published_at'] or None,'overview':r['vault_overview'],'transcript':r['vault_transcript'] or None,'transcript_status':r['coverage_status'],'visibility_note':r['visibility_note']} for r in rows]},indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'imported':imported,'known_uploads':len(rows),'archived':sum(bool(r['vault_transcript']) for r in rows)}))
