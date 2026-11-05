# Asterisk and frame placement — one table for every format

This is the single lookup for where the six-arm asterisk goes, how big it is, and how a Short is laid out. It adds no new rule: the numbers come from [tokens.json](tokens.json) (`thumbnail.signature`, `thumbnail.landscape_1080`, `thumbnail.shorts`), and [thumbnail-safe-zones.md](thumbnail-safe-zones.md) explains why. If this page and the tokens ever disagree, the tokens win and `_admin/scripts/validate_brand.py` fails.

## The asset

| Use | File | Colour |
| --- | --- | --- |
| Edited video, Shorts, clips | [assets/asterisk-white.svg](assets/asterisk-white.svg) | #FFFFFF on dark artwork |
| Edited video on light artwork | [assets/asterisk-black.svg](assets/asterisk-black.svg) | #0D0D0D |
| Livestream (thumbnail, scene, slate) | [assets/asterisk-red.svg](assets/asterisk-red.svg) | #E83B3B |

Same three masters everywhere (96×96 viewBox, hashes in [inventory.json](inventory.json)). Never redraw, recolour by eye, or use a font glyph. Scale the SVG uniformly; do not stretch, rotate or nudge it.

## Position and size (always top-right)

Size and clearances are measured on the **whole 96×96 viewport**, transparent padding included. The drawn star fills 88/96 of it.

| Format / canvas | Viewport | x / y | Top / right clearance | Width as % of frame |
| --- | --- | --- | --- | --- |
| 16:9 thumbnail, video, live scene, slate — 1280×720 | 96 | 1120 / 64 | 64 / 64 | 7.5% |
| 16:9 — 1920×1080 | 144 | 1680 / 96 | 96 / 96 | 7.5% |
| 16:9 — 3840×2160 | 288 | 3360 / 192 | 192 / 192 | 7.5% |
| 9:16 Short video or thumbnail — 1080×1920 | 96 | 768 / 320 | 320 / 216 | 8.9% |
| 9:16 — 2160×3840 | 192 | 1536 / 640 | 640 / 432 | 8.9% |

Clearances are 5% of frame width on the left/right edge in 16:9, and 16.7% of frame height from the top in 9:16. The 1920×1080 row is exactly 1.5× the 1280×720 row; any other 16:9 size scales the same way.

Not covered by this table: the default 1200×630 website OG card keeps its separately documented red bottom-right asterisk. An image that already has the star baked in gets no second one.

## 9:16 Short video layout

Status: **proposed starting values.** The placement of the asterisk is the approved Shorts template above; the other zones follow the 29 Oct rules (title above the video, captions below on a dark backing, nothing in the bottom ~350 px) and need Vincent's OK on one example render before a batch is cut.

| Zone (1080×1920) | Box (x, y, w, h) | Rule |
| --- | --- | --- |
| Asterisk | 768, 320, 96, 96 | White master, top-right, as above |
| Title | 48, 440, 984, 200 | Above the video, white, Space Grotesk bold, two lines at most; starts below the asterisk |
| Video frame | 0, 660, 1080, 608 | The full sharp 16:9 frame, centred, full width |
| Captions | 48, 1288, 984, 282 | White on a dark backing; no coloured karaoke words |
| Bottom clear | y ≥ 1570 | Nothing, for the Shorts UI |
| Background | full canvas | Same clip scaled to fill, centred on the faces, heavily blurred and darkened; no black bars |

## 16:9 video

Edited video, livestream scenes and slates use the 16:9 rows. Captions and lower thirds stay left of and below the mark so it is never covered; verify against the actual camera and caption positions. Names and the topic label are small.

- **Colour follows the video the image belongs to, not the source it was cut from.** A recap, Short or any other edited video, and its thumbnail, is white on dark (black on light), even when the footage came from a livestream. Only a thumbnail, scene or slate of an actual livestream is red.
- **Screen shares: product UI wins.** There is no persistent corner watermark on edited video. The mark appears on thumbnails, slates and host scenes. If a scene template carries it over a screen share, use the same corner only when it covers no readable product text or UI; otherwise leave it out of that scene rather than moving it. (Proposed; confirm with Vincent.)

## Who must follow this

Thumbnail prompts and composites, the Thumbnail Lab, Shorts and clip edits, recap and overlay skills, Restream layouts, and any export that carries the mark. Record kit revision and the logo hash with each export (see [production.md](production.md)). A placement that differs from this table needs the owner's explicit approval, recorded with the export.
