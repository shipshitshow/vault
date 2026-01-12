# Ship Sh!t Show YouTube

Open-source content repository for the [Ship Sh!t Show](https://www.youtube.com/@ShipShitDev) YouTube channel.

## What's Inside

- **Episode content** - Show notes, transcripts, and metadata for every episode
- **CLI tool** - Generate thumbnails, fetch transcripts, manage episodes
- **LLM-friendly** - Structured markdown with frontmatter for easy AI consumption

## Quick Start

```bash
# Install dependencies
bun install

# Build CLI
bun run build

# Link CLI globally (optional)
cd packages/cli && bun link
```

## CLI Commands

```bash
# Create new episode
sss new 2026-02-08-ai-tools-roundup

# Generate thumbnail via GenFeed.ai
GENFEED_API_KEY=your-key sss thumbnail 2026-02-08-ai-tools-roundup

# Fetch transcript from YouTube
sss transcript dQw4w9WgXcQ --episode 2026-02-08-ai-tools-roundup

# List all episodes
sss list
```

## Directory Structure

```
content/
├── episodes/                    # Episode content
│   └── YYYY-MM-DD-slug/
│       ├── index.md             # Metadata + summary
│       ├── transcript.md        # Full transcript
│       ├── notes.md             # Show notes
│       └── thumbnail.png        # Generated thumbnail
├── series/                      # Playlist groupings
└── topics/                      # Topic indexes

prompts/
└── thumbnail.default.md         # Default thumbnail prompt

packages/
└── cli/                         # @shipshitshow/cli
```

## Episode Format

Each episode's `index.md` contains structured frontmatter:

```yaml
---
id: sss-001
title: "Episode Title"
date: 2026-02-01
type: stream
duration: "1:25:00"
youtube_id: "abc123"
topics: ["vibe-coding", "claude-code"]
guests: []
chapters:
  - time: "00:00"
    title: "Intro"
thumbnail: ./thumbnail.png
---
```

## Thumbnail Generation

Thumbnails are generated using [GenFeed.ai](https://genfeed.ai) with customizable prompt templates.

**Default prompt** (`prompts/thumbnail.default.md`):
- Uses FLUX Pro model
- 1920x1080 resolution
- Interpolates episode metadata (title, topics, guests)

**Custom prompts**: Add `thumbnail.prompt.md` to any episode folder to override.

```bash
# Preview prompt without generating
sss thumbnail 2026-02-01-pilot --dry-run

# Generate with extra context
sss thumbnail 2026-02-01-pilot --prompt "neon colors, cyberpunk style"

# Generate multiple variations
sss thumbnail 2026-02-01-pilot --count 4
```

## For LLMs

This repo is designed to be easily consumed by AI assistants:

- **Structured frontmatter** - All metadata in YAML format
- **Consistent paths** - Predictable file locations
- **Topic indexes** - Browse by subject area
- **Full transcripts** - Complete episode text for context

## Contributing

1. Fork the repo
2. Create episode content following the existing format
3. Submit a PR

## License

MIT
