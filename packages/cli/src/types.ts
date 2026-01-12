export interface EpisodeMetadata {
  id: string;
  title: string;
  date: string;
  type: 'stream' | 'short' | 'podcast';
  duration: string;
  youtube_id: string;
  topics: string[];
  guests: string[];
  chapters: Chapter[];
  thumbnail?: string;
}

export interface Chapter {
  time: string;
  title: string;
}

export interface ThumbnailPromptConfig {
  model: string;
  width: number;
  height: number;
  outputs: number;
}

export interface Episode {
  slug: string;
  path: string;
  metadata: EpisodeMetadata;
  content: string;
}
