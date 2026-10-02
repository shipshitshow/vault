# Ship Sh!t Show Vault

Public episode transcripts, notes and resources for [the main show](https://www.youtube.com/@shipshitshow) and [the clips channel](https://www.youtube.com/@ShipShitShowClips). Open this repository as an Obsidian vault or browse its Markdown on GitHub.

## Start here

- [Production handbook](production/index.md): source-led shows, editing folders, packaging and public handoff.
- [Upload catalog](catalog.json) and [coverage ledger](_admin/data/youtube-coverage.csv).
- [Main-channel livestreams](shipshitshow/Livestreams/_Index.md), [edited videos](shipshitshow/Videos/_Index.md) and [Shorts](shipshitshowclips/Shorts/_Index.md).
- [Brand kit](brand/README.md): current direction, colors and asset inventory.
- [Viewer production skills](https://github.com/shipshitshow/skills) and [episode examples](https://github.com/shipshitshow/examples).
- [Obsidian home](00%20Home.md), [content map](01%20Content%20Map.md) and [manual canvas](02%20Content%20Canvas.canvas).

## Archive state — October 2, 2026

All **147 identified uploads** have a transcript: 56 main-channel livestreams/videos and 91 clips. The catalog unions historical inventory, current public tabs and verified episode links. This is a lower bound on uploads; it does not establish completeness for inaccessible or unlisted account content.

Recovered local ASR is explicitly unreviewed. Check names, numbers and wording before quoting. Every transcript has provenance and a source hash; raw captions or local ASR source files are preserved when available. Historical imports retain their original text and identify capture details that are unknown.

The dated [audit snapshot](_admin/docs/audits/2026-10-02/README.md) records the gaps before recovery. The maintained catalog and ledger record the current state.

## Content model

Each YouTube asset has its own `overview.md`, `transcript.md` and `provenance.json`. Captions, descriptions, notes and cut maps live alongside it when available. Source livestream, recap and Shorts use separate clocks. Relationships require evidence; similar dates/titles alone do not establish a derivative link.

Existing vault links are preserved. New folder names include publication date and YouTube ID; recording date is separate. Unknown dates remain explicit. Original preparation notes are distinguished from what happened on air.

Media and native editing projects stay in the Studio library. Public GitHub handoff contains text, captions, cut maps and sanitized provenance. See [the editing architecture](production/editing-workflow.md).

## Maintain the vault

Support scripts, templates and documentation live under `_admin`. [Frontmatter rules](_admin/docs/FRONTMATTER.md) reserve `youtube_tags` for YouTube keywords. `.obsidian` contains the owner's editor configuration.

Validate the archive with `python3 _admin/scripts/validate_archive.py`. Import an authorized local ASR handoff with `python3 _admin/scripts/import_local_asr.py --recovery-dir <text-handoff>`. This importer does not download or upload media. See [the transcript contract](production/transcript-archive.md) before importing.

Vault formatting uses [Biome](biome.json) through `_admin/scripts/format_vault.sh`.
