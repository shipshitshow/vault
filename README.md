# Ship Sh!t Show Vault

This repo is a pure Obsidian vault for the two YouTube channels:

- `shipshitshow`
- `shipshitshowclips`

## Entry Points

- [00 Home](./00 Home.md)
- [01 Content Map](./01 Content Map.md)
- [02 Content Canvas](./02 Content Canvas.canvas)
- [shipshitshow](./shipshitshow/index.md)
- [shipshitshowclips](./shipshitshowclips/index.md)

## Vault Layout

### Main channel

- [shipshitshow/index.md](./shipshitshow/index.md)
- [shipshitshow/Livestreams](./shipshitshow/Livestreams)
- [shipshitshow/Videos](./shipshitshow/Videos)

### Clips channel

- [shipshitshowclips/index.md](./shipshitshowclips/index.md)
- [shipshitshowclips/Shorts](./shipshitshowclips/Shorts)

### Admin

- [_admin/docs](./_admin/docs)
- [_admin/scripts](./_admin/scripts)
- [_admin/templates](./_admin/templates)

## Content Model

Each content chain is linked together:

- livestream -> recap video -> derived shorts
- overview notes link to related entries in the other channel folders
- transcripts live beside each entry as `transcript.md`
- Notion notes, where imported, live beside the livestream as `notes.md`

Navigation notes:

- [01 Content Map](./01 Content Map.md) is the note-based MOC
- [02 Content Canvas](./02 Content Canvas.canvas) is the manual canvas layout
- Obsidian Graph View is configured through [.obsidian/graph.json](./.obsidian/graph.json)

## Formatting

Biome is used for vault-side formatting with spaces, not tabs.

- Config: [biome.json](./biome.json)
- Formatter script: [_admin/scripts/format_vault.sh](./_admin/scripts/format_vault.sh)

Run:

```bash
./_admin/scripts/format_vault.sh
```

## Frontmatter Rules

YouTube keyword phrases must use `youtube_tags`, not `tags`.

See:

- [_admin/docs/FRONTMATTER.md](./_admin/docs/FRONTMATTER.md)

## Current State

- YouTube videos are imported
- YouTube livestreams are imported
- YouTube shorts are imported
- thumbnails are stored beside imported YouTube entries
- transcripts were backfilled from available captions
- completed livestream notes from Notion were imported where available

## Notes

- `shipshitshow` and `shipshitshowclips` are the actual vault roots for channel content
- `_admin` is only support material for maintaining the vault
- `.obsidian` contains the Obsidian workspace, graph, and plugin config
