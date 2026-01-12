# Ship Sh!t Show YouTube - AI Agent Context

**Channel:** https://www.youtube.com/@ShipShitDev

This directory provides context for AI assistants working with this repository.

## Repository Purpose

Open-source content repository for the Ship Sh!t Show YouTube channel, including:
- Episode metadata and transcripts
- CLI tool for content management
- Thumbnail generation via GenFeed.ai

## Key Paths

| Path | Description |
|------|-------------|
| `content/episodes/` | Episode folders (YYYY-MM-DD-slug format) |
| `content/episodes/*/index.md` | Episode metadata + summary |
| `content/episodes/*/transcript.md` | Full episode transcript |
| `content/episodes/*/notes.md` | Show notes |
| `prompts/thumbnail.default.md` | Default thumbnail prompt |
| `packages/cli/` | CLI tool source |

## Episode Metadata Schema

```typescript
interface Episode {
  id: string;           // Format: sss-XXX
  title: string;
  date: string;         // YYYY-MM-DD
  type: 'stream' | 'short' | 'podcast';
  duration: string;     // HH:MM:SS or MM:SS
  youtube_id: string;
  topics: string[];
  guests: string[];
  chapters: { time: string; title: string }[];
  thumbnail?: string;
}
```

## Common Tasks

### Find episodes by topic
```bash
grep -r "topics:.*claude" content/episodes/*/index.md
```

### Get episode metadata
Read `content/episodes/YYYY-MM-DD-slug/index.md` and parse YAML frontmatter.

### Generate thumbnail
```bash
sss thumbnail <episode-slug>
```

### Fetch transcript
```bash
sss transcript <youtube-id> --episode <episode-slug>
```

## GenFeed.ai Integration

Thumbnail generation uses GenFeed.ai API:
- Endpoint: `POST https://api.genfeed.ai/v1/images`
- Auth: Bearer token via `GENFEED_API_KEY` env var
- Models: flux-pro, imagen-4-ultra, klingai-2.5
