import { mkdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import chalk from 'chalk';
import { Command } from 'commander';
import { episodeExists, getAllEpisodes, getEpisodePath } from '../utils/content.js';

export const newCommand = new Command('new')
  .description('Create a new episode folder')
  .argument('<slug>', 'Episode slug (e.g., 2026-02-08-ai-news-roundup)')
  .option('-t, --title <title>', 'Episode title')
  .option('--type <type>', 'Episode type (stream, short, podcast)', 'stream')
  .action((slug: string, options: { title?: string; type?: string }) => {
    if (episodeExists(slug)) {
      console.error(chalk.red(`Episode ${slug} already exists`));
      process.exit(1);
    }

    const episodePath = getEpisodePath(slug);
    mkdirSync(episodePath, { recursive: true });

    // Generate next episode ID
    const episodes = getAllEpisodes();
    const maxId = episodes.reduce((max, ep) => {
      const match = ep.metadata.id?.match(/sss-(\d+)/);
      return match ? Math.max(max, parseInt(match[1], 10)) : max;
    }, 0);
    const nextId = `sss-${String(maxId + 1).padStart(3, '0')}`;

    // Extract date from slug if it starts with YYYY-MM-DD
    const dateMatch = slug.match(/^(\d{4}-\d{2}-\d{2})/);
    const date = dateMatch ? dateMatch[1] : new Date().toISOString().split('T')[0];

    // Generate title from slug if not provided
    const title =
      options.title ||
      slug
        .replace(/^\d{4}-\d{2}-\d{2}-/, '')
        .split('-')
        .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');

    const indexContent = `---
id: ${nextId}
title: "${title}"
date: ${date}
type: ${options.type || 'stream'}
duration: ""
youtube_id: ""
topics: []
guests: []
chapters:
  - time: "00:00"
    title: "Intro"
thumbnail: ./thumbnail.png
---

## Summary

[Episode summary goes here]

## Key Takeaways

- Takeaway 1
- Takeaway 2
- Takeaway 3

## Resources Mentioned

- [Resource 1](url)
`;

    const notesContent = `# Show Notes: ${title}

## Pre-Show Prep

- [ ] Prepare demo
- [ ] Queue content

## Segments

### Segment 1: Introduction

[Notes]

### Segment 2: Main Content

[Notes]

### Segment 3: Wrap Up

[Notes]

## Post-Show

- [ ] Export transcript
- [ ] Generate thumbnail
- [ ] Create clips
`;

    const transcriptContent = `# Transcript: ${title}

> Use \`sss transcript <youtube-id>\` to fetch the transcript after publishing.
`;

    writeFileSync(join(episodePath, 'index.md'), indexContent);
    writeFileSync(join(episodePath, 'notes.md'), notesContent);
    writeFileSync(join(episodePath, 'transcript.md'), transcriptContent);

    console.log(chalk.green(`Created episode: ${slug}`));
    console.log(chalk.dim(`  ID: ${nextId}`));
    console.log(chalk.dim(`  Path: ${episodePath}`));
    console.log(chalk.dim(`  Files: index.md, notes.md, transcript.md`));
  });
