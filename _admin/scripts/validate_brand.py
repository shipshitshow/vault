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
if (mark['x'] + mark['width'] + mark['inset_right'], mark['y'] + mark['height'] + mark['inset_bottom']) != (width, height):
    errors.append('Thumbnail signature coordinates and insets disagree.')
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
    if asset['role'] == 'standalone-mark':
        svg = ET.fromstring(data)
        bars = svg.findall('.//{http://www.w3.org/2000/svg}rect')
        rotations = ['', 'rotate(60 48 48)', 'rotate(120 48 48)']
        if svg.attrib.get('viewBox') != '0 0 96 96' or len(bars) != 3:
            errors.append(f'Incorrect mark viewport/bars: {path.name}')
        elif any((bar.attrib.get('x'), bar.attrib.get('y'), bar.attrib.get('width'), bar.attrib.get('height'), bar.attrib.get('transform', '')) != ('38', '4', '20', '88', rotation) for bar, rotation in zip(bars, rotations)):
            errors.append(f'Incorrect mark geometry: {path.name}')
for name in ('README.md', 'identity.md', 'applications.md', 'editing.md', 'production.md'):
    text = (root / name).read_text()
    for obsolete in ('SH*W', 'upper-right', '#FF2D20', '#ff2d20', 'white app-specific'):
        if obsolete in text:
            errors.append(f'{name}: obsolete active brand rule {obsolete}')
if errors:
    raise SystemExit('\n'.join(errors))
print('Brand tokens, geometry, inventory and active guides are consistent.')
