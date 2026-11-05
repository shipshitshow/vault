# Asterisk and frame placement — one table for every format

This is the single lookup for where the six-arm asterisk goes, how big it is, and how a Short video is laid out. It adds no new rule: the numbers come from [tokens.json](tokens.json) (`thumbnail.signature`, `thumbnail.landscape_1080`, `thumbnail.shorts`), and [thumbnail-safe-zones.md](thumbnail-safe-zones.md) explains why. If this page and the tokens ever disagree, the tokens win and `_admin/scripts/validate_brand.py` fails.

## The asset

| Use | File | Colour |
| --- | --- | --- |
| Edited video and clip thumbnails | [assets/asterisk-white.svg](assets/asterisk-white.svg) | #FFFFFF on dark artwork |
| Edited video on light artwork | [assets/asterisk-black.svg](assets/asterisk-black.svg) | #0D0D0D |
| Livestream (thumbnail, scene, slate); Short video and Short cover | [assets/asterisk-red.svg](assets/asterisk-red.svg) | #E83B3B |

Same three masters everywhere (96×96 viewBox, hashes in [inventory.json](inventory.json)). Never redraw, recolour by eye, or use a font glyph. Scale the SVG uniformly; do not stretch, rotate or nudge it.

## Position and size (always top-right)

Size and clearances are measured on the **whole 96×96 viewport**, transparent padding included. The drawn star fills 88/96 of it.

| Format / canvas | Viewport | x / y | Top / right clearance | Width as % of frame |
| --- | --- | --- | --- | --- |
| 16:9 thumbnail, video, live scene, slate — 1280×720 | 96 | 1120 / 64 | 64 / 64 | 7.5% |
| 16:9 — 1920×1080 | 144 | 1680 / 96 | 96 / 96 | 7.5% |
| 16:9 — 3840×2160 | 288 | 3360 / 192 | 192 / 192 | 7.5% |
| 9:16 Short cover and Short video — 1080×1920 | 120 | 880 / 230 (centre 940 / 290) | 230 / 80 | 11.1% |
| 9:16 — 2160×3840 | 240 | 1760 / 460 | 460 / 160 | 11.1% |

Clearances are 5% of frame width on the left/right edge in 16:9. In 9:16 the Short cover and the Short video share one mark, the red master at 120 px (owner decision, 5 Nov 2026), so a Short looks the same as its cover. The 1920×1080 row is exactly 1.5× the 1280×720 row; any other 16:9 size scales the same way.

Not covered by this table: the default 1200×630 website OG card keeps its separately documented red bottom-right asterisk. An image that already has the star baked in gets no second one.

## 9:16 Short video (locked by the owner, 5 Nov 2026)

The edited Short itself has its own locked template, set by Vincent after the 261103 Shorts and recorded in the show repo's `docs/show-prep/edit-style.md`. Since 5 Nov 2026 the Short cover uses the same mark (the 9:16 row above).

| Element (1080×1920) | Locked value |
| --- | --- |
| Asterisk | [Red master](assets/asterisk-red.svg), unmodified, 120×120 viewport centred at x940 / y290 (x880, y230; clearance 230 top, 80 right). Never moved or resized per Short |
| Frame | The speaker fills the whole 9:16 frame (static cam crop, no blur, tile or bars). No title text |
| Captions | White, bold uppercase, spoken word in #E83B3B, centred at about y1480, at most ~920 px wide |
| Bottom clear | Nothing below y≈1570 |

If the asterisk hides the subject, move the crop, not the mark.

## 16:9 video

Edited video, livestream scenes and slates use the 16:9 rows. Captions and lower thirds stay left of and below the mark so it is never covered; verify against the actual camera and caption positions. Names and the topic label are small.

- **Colour follows the video the image belongs to, not the source it was cut from.** A recap or other edited video, and its thumbnail, is white on dark (black on light), even when the footage came from a livestream. Only a thumbnail, scene or slate of an actual livestream is red. The one exception is Shorts: the Short video and its cover both use the red master.
- **Screen shares: product UI wins.** There is no persistent corner watermark on edited video. The mark appears on thumbnails, slates and host scenes. If a scene template carries it over a screen share, use the same corner only when it covers no readable product text or UI; otherwise leave it out of that scene rather than moving it. (Proposed; confirm with Vincent.)

## Who must follow this

Thumbnail prompts and composites, the Thumbnail Lab, Shorts and clip edits, recap and overlay skills, Restream layouts, and any export that carries the mark. Record kit revision and the logo hash with each export (see [production.md](production.md)). A placement that differs from this table needs the owner's explicit approval, recorded with the export.
