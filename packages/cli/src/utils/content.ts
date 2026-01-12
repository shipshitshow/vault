import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import matter from 'gray-matter';
import type { Episode, EpisodeMetadata } from '../types.js';

const CONTENT_DIR = resolve(process.cwd(), 'content/episodes');

export function getContentDir(): string {
  return CONTENT_DIR;
}

export function getEpisodePath(slug: string): string {
  return join(CONTENT_DIR, slug);
}

export function episodeExists(slug: string): boolean {
  const indexPath = join(getEpisodePath(slug), 'index.md');
  return existsSync(indexPath);
}

export function getEpisode(slug: string): Episode | null {
  const episodePath = getEpisodePath(slug);
  const indexPath = join(episodePath, 'index.md');

  if (!existsSync(indexPath)) {
    return null;
  }

  const fileContent = readFileSync(indexPath, 'utf-8');
  const { data, content } = matter(fileContent);

  return {
    slug,
    path: episodePath,
    metadata: data as EpisodeMetadata,
    content,
  };
}

export function getAllEpisodes(): Episode[] {
  if (!existsSync(CONTENT_DIR)) {
    return [];
  }

  const entries = readdirSync(CONTENT_DIR, { withFileTypes: true });
  const episodes: Episode[] = [];

  for (const entry of entries) {
    if (entry.isDirectory() && !entry.name.startsWith('.')) {
      const episode = getEpisode(entry.name);
      if (episode) {
        episodes.push(episode);
      }
    }
  }

  return episodes.sort((a, b) => b.metadata.date.localeCompare(a.metadata.date));
}
