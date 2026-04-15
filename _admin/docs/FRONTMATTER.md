# Vault Frontmatter

`overview.md` files use `youtube_tags`, not `tags`.

Why:
- Obsidian treats `tags` as a special property.
- Phrase keywords like `ai experiment gone wrong` are valid YouTube tags but invalid Obsidian tags.
- `youtube_tags` preserves the original YouTube keyword phrases without Obsidian trying to coerce them.

Required shape for imported YouTube entries:

```yaml
youtube_id: "..."
youtube_url: "https://www.youtube.com/watch?v=..."
source: "youtube"
youtube_tags:
  - "openclaw"
  - "ai agents"
  - "ai experiment gone wrong"
aliases:
  - "Video Title"
```

If an external importer writes `tags:` by mistake, run:

```bash
python3 _admin/scripts/normalize_youtube_frontmatter.py
```
