#!/usr/bin/env python3
"""Check the maintained brand contract, standalone marks and inventory integrity."""
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[2] / 'brand'
tokens = json.loads((root / 'tokens.json').read_text())
errors = []
if tokens['identity']['show_name'] != 'Ship Sh*t Show':
    errors.append('The display name must be Ship Sh*t Show, with an asterisk.')
if tokens['identity']['avatar_main'] != 'red asterisk on charcoal':
    errors.append('The main/show avatar must be red on charcoal.')
if tokens['identity']['compact_mark'] != 'six-arm-asterisk':
    errors.append('The active compact mark must be the six-arm asterisk.')
if tokens['identity']['baseline'] != 'Think AI':
    errors.append('The baseline must be Think AI without punctuation.')
if tokens['brands']['show']['primary'] != tokens['colors']['accent_red']:
    errors.append('Show primary and accent token differ.')
if tokens['brands']['business']['primary'] != tokens['colors']['white']:
    errors.append('Business primary must be monochrome.')
mark = tokens['thumbnail']['signature']
width, height = tokens['thumbnail']['reference_canvas']
if (mark['x'] + mark['width'] + mark['inset_right'], mark['y']) != (width, mark['inset_top']):
    errors.append('Thumbnail top-right coordinates and insets disagree.')
if mark['inset_top'] != mark['inset_right'] or mark['inset_top'] < 50 or mark['y'] + mark['height'] > height:
    errors.append('Landscape thumbnails need equal top/right safe margins of at least 50px.')
shorts = tokens['thumbnail']['shorts']
short_width, short_height = shorts['reference_canvas']
short_mark = shorts['signature']
safe = shorts['reference_ad_safe_area']
if (short_mark['x'] + short_mark['width'] + short_mark['inset_right'], short_mark['y']) != (short_width, short_mark['inset_top']):
    errors.append('Shorts top-right coordinates and insets disagree.')
if not short_mark['inset_top'] > short_mark['inset_right'] >= 50:
    errors.append('Shorts need greater top than right clearance, both at least 50px.')
if not (safe['x'] <= short_mark['x'] and safe['y'] <= short_mark['y'] and short_mark['x'] + short_mark['width'] <= safe['x'] + safe['width'] <= short_width and short_mark['y'] + short_mark['height'] <= safe['y'] + safe['height'] <= short_height):
    errors.append('Shorts signature must fit inside the reference ad safe area.')
land = tokens['thumbnail']['landscape_1080']
land_mark = land['signature']
scale = land['reference_canvas'][0] / width
if any(land_mark[key] != mark[key] * scale for key in ('x', 'y', 'width', 'height', 'inset_right', 'inset_top')):
    errors.append('The 1920x1080 landscape template must be the 1280x720 template scaled uniformly.')
layout = shorts['video_layout']
if layout['bottom_clear_from_y'] < short_height - 400:
    errors.append('Short video layout must leave the bottom ~350px clear.')
if not (short_mark['y'] + short_mark['height'] <= layout['title']['y'] and layout['title']['y'] + layout['title']['height'] <= layout['frame']['y'] and layout['frame']['y'] + layout['frame']['height'] <= layout['captions']['y'] and layout['captions']['y'] + layout['captions']['height'] <= layout['bottom_clear_from_y']):
    errors.append('Short video zones must stack asterisk, title, frame, captions, clear area without overlap.')
if layout['frame']['width'] != short_width or abs(layout['frame']['height'] * 16 - layout['frame']['width'] * 9) > 16:
    errors.append('Short video frame must be the full-width 16:9 frame.')
palette = json.loads((root / 'colors.json').read_text())
if palette['brands'] != tokens['brands']:
    errors.append('Color summary and canonical brand roles differ.')
if palette['colors'] != tokens['colors']:
    errors.append('colors.json and tokens.json differ.')
for asset in json.loads((root / 'inventory.json').read_text())['assets']:
    path = root / asset['file']
    if not path.is_file():
        errors.append(f'Missing asset {path.name}')
        continue
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != asset['sha256'] or len(data) != asset['bytes']:
        errors.append(f'Inventory hash/size drift: {path.name}')
    if asset['id'] == 'avatar-main':
        svg = ET.fromstring(data)
        background = svg.find('{http://www.w3.org/2000/svg}rect')
        inner = svg.find('{http://www.w3.org/2000/svg}svg')
        if background.attrib.get('fill') != tokens['colors']['ink'] or inner.attrib.get('fill') != tokens['colors']['accent_red']:
            errors.append('Main avatar export must be red on charcoal.')
    if asset['role'] == 'standalone-mark':
        svg = ET.fromstring(data)
        bars = svg.findall('.//{http://www.w3.org/2000/svg}rect')
        rotations = ['', 'rotate(60 48 48)', 'rotate(120 48 48)']
        if svg.attrib.get('viewBox') != '0 0 96 96' or len(bars) != 3:
            errors.append(f'Incorrect mark viewport/bars: {path.name}')
        elif any((bar.attrib.get('x'), bar.attrib.get('y'), bar.attrib.get('width'), bar.attrib.get('height'), bar.attrib.get('transform', '')) != ('38', '4', '20', '88', rotation) for bar, rotation in zip(bars, rotations)):
            errors.append(f'Incorrect mark geometry: {path.name}')
for name in ('README.md', 'identity.md', 'applications.md', 'editing.md', 'production.md', 'thumbnail-safe-zones.md', 'placement.md'):
    text = (root / name).read_text()
    for obsolete in ('SH*W', 'Ship Sh!t Show', 'black asterisk on red', 'x1136/y576', 'fixed bottom right', 'canonical bottom-right token', '#FF2D20', '#ff2d20', 'white app-specific'):
        if obsolete in text:
            errors.append(f'{name}: obsolete active brand rule {obsolete}')
if errors:
    raise SystemExit('\n'.join(errors))
print('Brand tokens, geometry, inventory and active guides are consistent.')
