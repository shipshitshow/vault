#!/usr/bin/env python3
"""Import YouTube-caption transcripts kept by the show app into the vault.

Reads `<app>/transcripts/index.json` and the cleaned text and raw VTT files that
`bun run transcripts:import` saved in shipshitshow/show.shipshit.dev. It never
downloads or uploads media and makes no network calls. Only ids that are not yet
in the coverage ledger are added; existing entries are never rewritten.

  python3 _admin/scripts/import_app_captions.py --app-transcripts <path>/apps/app/data/transcripts --since 2026-10-02
  python3 _admin/scripts/import_app_captions.py ... --ids a,b --write

Without --write it lists what would be imported. All ids are main-channel
uploads; verify the channel (for example through YouTube oEmbed) before adding
another source channel here.
"""
from pathlib import Path
import argparse, csv, hashlib, json, shutil
from datetime import datetime, timezone

parser = argparse.ArgumentParser()
parser.add_argument('--app-transcripts', type=Path, required=True)
parser.add_argument('--vault', type=Path, default=Path(__file__).resolve().parents[2])
parser.add_argument('--since', default='', help='Only entries published on or after YYYY-MM-DD')
parser.add_argument('--ids', default='', help='Comma-separated ids to import regardless of --since')
parser.add_argument('--import-date', default=datetime.now(timezone.utc).date().isoformat())
parser.add_argument('--visibility-note', default='Public title and channel verified through YouTube oEmbed; channel-tab listing not checked')
parser.add_argument('--write', action='store_true')
args = parser.parse_args()
root = args.vault.resolve()
app = args.app_transcripts.resolve()
MAIN = 'UCxuriP32znodU-8N7zkwuew'
ledger = root / '_admin/data/youtube-coverage.csv'
rows = list(csv.DictReader(ledger.open()))
known = {r['youtube_id'] for r in rows}
wanted = {i for i in args.ids.split(',') if i}
index = json.loads((app / 'index.json').read_text())['videos']
todo = sorted(
    ((v['date'], k, v) for k, v in index.items()
     if k not in known and (k in wanted or (args.since and v['date'] >= args.since))),
    key=lambda t: (t[0], t[1]))
if not args.write:
    for date, k, v in todo:
        print(date, k, v['type'], v['title'])
    print(len(todo), 'to import')
    raise SystemExit(0)

folders = {'livestream': 'shipshitshow/Livestreams', 'video': 'shipshitshow/Videos', 'short': 'shipshitshow/Shorts'}
for date, id, v in todo:
    fmt = v['type']
    if fmt not in folders:
        raise ValueError('Unsupported type for ' + id + ': ' + fmt)
    clean = app / 'clean' / f'{date}-{fmt}-{id}.txt'
    vtt = app / ('shorts' if fmt == 'short' else '.') / f'{id}.{v.get("lang", "en")}.vtt'
    if not clean.is_file() or not clean.read_text().strip():
        raise ValueError('Missing or empty cleaned transcript for ' + id)
    url = 'https://www.youtube.com/watch?v=' + id
    d = root / folders[fmt] / f'{date}-{id}'
    if d.exists():
        raise ValueError('Destination collision: ' + str(d))
    d.mkdir(parents=True)
    fields = {'title': v['title'], 'type': 'stream' if fmt == 'livestream' else fmt, 'youtube_id': id,
              'youtube_url': url, 'channel': 'shipshitshow', 'channel_id': MAIN, 'published_at': date,
              'transcript_status': 'archived', 'source': 'youtube', 'youtube_tags': [], 'date': date}
    (d / 'overview.md').write_text(
        '---\n' + '\n'.join(k + ': ' + json.dumps(x, ensure_ascii=False) for k, x in fields.items())
        + '\n---\n\n# ' + v['title'] + '\n\n## Links\n\n- YouTube: ' + url + '\n\n## Archive state\n\n'
        + 'Transcript imported from YouTube captions with provenance; ASR wording is unreviewed.\n')
    body = clean.read_text().strip()
    (d / 'transcript.md').write_text(
        '# Transcript\n\nImported normalized YouTube captions; ASR wording is unreviewed. '
        'Timestamps, when present, use this asset\'s clock.\n\n' + body + '\n')
    shutil.copyfile(clean, d / 'transcript.raw.txt')
    if vtt.is_file():
        shutil.copyfile(vtt, d / 'captions.raw.vtt')
    prov = {'youtube_id': id, 'channel_id': MAIN, 'imported_on': args.import_date,
            'method': 'youtube-captions-normalized',
            'source_sha256': hashlib.sha256(clean.read_bytes()).hexdigest(),
            'source_file': 'show.shipshit.dev/apps/app/data/transcripts/clean/' + clean.name,
            'language': v.get('lang', 'en'),
            'clock': 'full-livestream' if fmt == 'livestream' else 'published-asset',
            'review_status': 'asr-unreviewed', 'visibility_note': args.visibility_note}
    (d / 'provenance.json').write_text(json.dumps(prov, indent=2) + '\n')
    r = {k: '' for k in rows[0]}
    r.update(youtube_id=id, channel='shipshitshow', format=fmt, title=v['title'], url=url, published_at=date,
             seen_in_july_inventory='no', seen_in_public_tab_2026_10_02='no',
             vault_overview=(d / 'overview.md').relative_to(root).as_posix(),
             vault_transcript=(d / 'transcript.md').relative_to(root).as_posix(),
             app_clean_transcript='apps/app/data/transcripts/clean/' + clean.name,
             coverage_status='archived_in_vault', visibility_note=args.visibility_note)
    rows.append(r)

with ledger.open('w') as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)
(root / 'catalog.json').write_text(json.dumps({
    'observed_on': args.import_date,
    'completeness': 'known-tabs-plus-historical-inventory-and-verified-episode-links; lower-bound',
    'items': [{'youtube_id': r['youtube_id'], 'channel': r['channel'], 'format': r['format'], 'title': r['title'],
               'url': r['url'], 'published_at': r['published_at'] or None, 'overview': r['vault_overview'],
               'transcript': r['vault_transcript'] or None, 'transcript_status': r['coverage_status'],
               'visibility_note': r['visibility_note']} for r in rows]}, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'imported': len(todo), 'known_uploads': len(rows), 'archived': sum(bool(r['vault_transcript']) for r in rows)}))
