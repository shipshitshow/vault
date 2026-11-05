# Artwork and web applications

Read [identity](identity.md), [tokens](tokens.json) and [inventory](inventory.json). Keep current recipes distinct from historical briefs.

## Channel artwork

**Main avatar:** red six-arm asterisk on charcoal. **Clips avatar:** white asterisk on charcoal. A square source must survive the destination’s actual circular crop. No faces, lettering or border around the standalone avatar mark.

**Banner:** approved hosts, Vincent left and Mitchell right, natural color on charcoal. Baseline is **Think AI**, optionally preceded by the standalone asterisk. No colon or oversized central logo block. Keep both full shoulders in the master and verify the actual desktop/mobile/TV crops.

**Personal PFPs:** matching three-quarter framing, natural color, charcoal background and consistent lighting/camera height. No asterisk on the person or backdrop. Preserve identity and natural proportions.

**Podcast cover:** full name, approved host imagery and a simple readable hierarchy. Check the small destination crop. Do not imply an unapproved sponsor relationship.

## Thumbnails and social

Use the actual episode or final edit for claims. The video title and art must promise the same truthful answer. **Topic first, no host faces** (decided 26 October 2026: viewers do not yet know the hosts, so a face carries no information). The hook is the topic: an official topic logo or source-grounded subject, with optional large brief text naming the business use or the head-to-head. Prefer operator/business-use and head-to-head framings; pure model-news framing is the weakest. That ranking comes from view counts of the channel inventory, without CTR or retention, so treat it as a hypothesis. Keep the background predominantly monochrome. Hosts stay in website, banner, avatar and podcast-cover work, not thumbnails, until the owner reverses this. Do not invent vendor logos or replace requested generated artwork with static SVG portraits.

The exact six-arm thumbnail signature is always **top-right**, inside the format-specific safe margins. At 1280×720 its viewport is x1120/y64, 96×96, with equal 64px top/right insets. For a 1080×1920 Short cover use the red master at x880/y230, 120×120 (centre x940/y290): 230px top and 80px right, the same mark as the Short video. Scale all coordinates uniformly with the canvas. Use the [thumbnail safe-zone contract](thumbnail-safe-zones.md), including crop and UI checks. White on dark (black on light) identifies edited videos; red identifies livestreams. No box, additional dot or waves. On website thumbnail presentations use the same proportional top-right placement. Existing approved default OG artwork retains its separately documented layout. If an image already contains the signature, do not add a duplicate.

Use the supplied red/white SVG master as an editable production layer. A subtle material finish, scene-matched edge light or restrained texture may connect the mark to the artwork; preserve its exact upright silhouette, proportions, base color, safe margins and small-size contrast. Keep it subordinate to the subject. Reserve its space while generating the scene, then composite the actual master; verify a generated preview against that master before final export.

Text is episode-specific, not mandatory. Large readable brief text may support a concept; avoid clutter, paragraphs and false outcomes. Keep exact production logos/type/signatures editable. Inspect the export at feed size for likeness, cropping, text, contrast and official logo accuracy. Three requested thumbnail variations are hypotheses, not proven winners.

**Website OG cards:** 1200×630 exports. The approved business card is monochrome “Your idea. We ship it.” The selected show card is host-led “Think AI” with the red bottom-right asterisk and **no top-left show wordmark**. Use stable versioned image URLs in both Open Graph and Twitter metadata. Preserve author/episode-specific metadata where provided.

**Shorts:** real selected footage, short editable captions and destination-safe placement. Keep brand art distinct from factual source footage. Check the actual platform UI and crop.

## Web and partners

Both sites start in dark mode. The show uses red primary actions; the commercial identity is monochrome. They share typography, the asterisk and photographic treatment while keeping distinct wordmarks and purpose. Public, auth, producer, secondary pages, favicons and topic/social cards consume the same applicable tokens. Do not fix one homepage while leaving a parallel local palette elsewhere.

Use semantic web tokens for brand color, text, surfaces, borders and action contrast. Prefer existing shared components. A status/category/vendor color is not automatically a brand violation. Photos use their native aspect ratio with integrated edges, full heads/shoulders and a stacked mobile composition.

An app’s **`/shipshitshow` page** introduces its actual connection to the show while retaining its own header. Use a truthful introduction, watch action and useful app-specific resource/action. Do not invent an offer or call an owned app a paid sponsor. Company names and URLs do not replace approved official logo files. Vincent coordinates external site updates; this guide authorizes no outreach or account changes.
