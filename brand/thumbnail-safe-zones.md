# Thumbnail signature and safe margins

Owner direction and primary sources checked **3 November 2026**. These are the show’s house templates. The numeric source of truth is `tokens.json`: `thumbnail.signature` for 16:9 and `thumbnail.shorts` for 9:16.

## Fixed signature placement

Always place the exact upright six-arm asterisk in the **top-right of the format’s safe area**. On landscape thumbnails the top and right clearances are equal. On Shorts the top clearance is larger than the right. Every reference margin exceeds 50px; scale the entire template uniformly for other resolutions.

| Format / canvas | Mark viewport | x / y | Top / right clearance |
| --- | --- | --- | --- |
| Video/live, 1280×720 | 96×96 | 1120 / 64 | 64 / 64 |
| Video/live, 1920×1080 | 144×144 | 1680 / 96 | 96 / 96 |
| Video/live, 3840×2160 | 288×288 | 3360 / 192 | 192 / 192 |
| Short, 1080×1920 | 96×96 | 768 / 320 | 320 / 216 |
| Short, 2160×3840 | 192×192 | 1536 / 640 | 640 / 432 |

Clearance is measured from the **whole SVG viewport**, including its transparent padding. Do not stretch, rotate or shift the mark to suit a scene. Reserve its area before composing the image. Keep the bottom-right free of essential detail for duration/UI overlays.

Use the [red SVG](assets/asterisk-red.svg) for livestreams and the [white SVG](assets/asterisk-white.svg) on dark edited-video artwork; the existing black master supplies contrast on light artwork. Keep the silhouette and base color intact. Scene-matched edge lighting, a thin material finish or restrained texture may integrate it, while the subject stays dominant. Composite the actual master as an editable layer for final exports, rather than relying on a generated approximation. Review at 160px and 320px wide.

## YouTube guidance versus house templates

[YouTube’s thumbnail help](https://support.google.com/youtube/answer/72431?hl=en) recommends 3840×2160 for video, 2160×3840 for Shorts, JPG/PNG, 16:9 and 9:16 respectively. Desktop uploads allow up to 50MB; mobile video thumbnails have a 2MB limit. The current help page describes custom Shorts uploads in desktop Studio for verified accounts. Verify the actual account’s controls before promising an upload workflow.

The thumbnail help does **not** specify a universal numeric safe rectangle for organic thumbnails. These house margins are not an official YouTube thumbnail requirement or a guarantee across all surfaces.

[Google’s Universal Video Ad Safe Zones](https://services.google.com/fh/files/misc/universalsafezones-youtube.pdf) provides a useful conservative **video-ad** reference. Its 1080×1920 vertical example reserves 48px left, 192px right, 288px top and 672px bottom. The Shorts template deliberately places the whole mark inside that reference region, with additional top/right clearance. The ad document warns that device differences can still cut off elements. Do not apply its horizontal ad overlay to organic video thumbnails as though it were the same surface.

## Composition and export checks

[YouTube’s thumbnail/title tips](https://support.google.com/youtube/answer/12340300?hl=en) favor simple compositions, relevant recognizable imagery, readable text when used, and strong color/composition without clutter. For this show, lead with the topic, keep hosts out of thumbnails, and honor an episode’s no-text direction. A familiar subject plus one clear action should survive feed size; preserve factual source/title alignment.

1. Compose independently for 16:9 and 9:16; do not crop a finished landscape signature into a Short.
2. Keep the whole mark within its template, with the clearances in the table. Maintain exact geometry and red/white contrast.
3. Check the actual channel grid, search/feed thumbnail and Shorts player UI on desktop/mobile. Inspect any surface-specific crop; a safe area in the original does not guarantee survival of a different crop. Adjust the artwork/template deliberately before approval, preserving top-right placement and the larger Shorts top inset.
4. Preview at feed size, inspect export dimensions/alpha/file size, and retain a clean scene plus editable exact signature layer. A generated preview is not a checked final composite.
5. Record approval separately. Creating assets or changing this contract does not authorize uploading, scheduling or publishing artwork.
