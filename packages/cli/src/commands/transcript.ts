import { execSync } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import chalk from 'chalk';
import { Command } from 'commander';
import matter from 'gray-matter';
import { getEpisode } from '../utils/content.js';

function checkYtDlp(): boolean {
  try {
    execSync('yt-dlp --version', { stdio: 'ignore' });
    return true;
  } catch {
    return false;
  }
}

function fetchTranscript(youtubeId: string): string {
  try {
    // Fetch auto-generated captions
    const result = execSync(
      `yt-dlp --skip-download --write-auto-sub --sub-format vtt --sub-lang en -o - "https://www.youtube.com/watch?v=${youtubeId}" 2>/dev/null`,
      { encoding: 'utf-8', maxBuffer: 10 * 1024 * 1024 }
    );

    // Convert VTT to plain text
    return convertVttToText(result);
  } catch (error) {
    throw new Error(`Failed to fetch transcript: ${(error as Error).message}`);
  }
}

function convertVttToText(vtt: string): string {
  const lines = vtt.split('\n');
  const textLines: string[] = [];
  let lastLine = '';

  for (const line of lines) {
    // Skip VTT headers, timestamps, and empty lines
    if (
      line.startsWith('WEBVTT') ||
      line.startsWith('Kind:') ||
      line.startsWith('Language:') ||
      line.includes('-->') ||
      line.trim() === '' ||
      /^\d+$/.test(line.trim())
    ) {
      continue;
    }

    // Remove HTML tags and timing metadata
    const cleanLine = line
      .replace(/<[^>]+>/g, '')
      .replace(/\[.*?\]/g, '')
      .trim();

    // Avoid duplicate consecutive lines
    if (cleanLine && cleanLine !== lastLine) {
      textLines.push(cleanLine);
      lastLine = cleanLine;
    }
  }

  return textLines.join('\n');
}

export const transcriptCommand = new Command('transcript')
  .description('Fetch transcript from YouTube using yt-dlp')
  .argument('<youtube-id>', 'YouTube video ID')
  .option('-e, --episode <slug>', 'Episode slug to save transcript to')
  .option('-o, --output <file>', 'Output file path')
  .action((youtubeId: string, options: { episode?: string; output?: string }) => {
    if (!checkYtDlp()) {
      console.error(chalk.red('yt-dlp is not installed. Install with: brew install yt-dlp'));
      process.exit(1);
    }

    console.log(chalk.cyan(`Fetching transcript for: ${youtubeId}`));

    try {
      const transcript = fetchTranscript(youtubeId);

      if (!transcript.trim()) {
        console.error(chalk.red('No transcript found for this video'));
        process.exit(1);
      }

      // Determine output path
      let outputPath: string;
      let updateEpisode = false;

      if (options.episode) {
        const episode = getEpisode(options.episode);
        if (!episode) {
          console.error(chalk.red(`Episode not found: ${options.episode}`));
          process.exit(1);
        }
        outputPath = join(episode.path, 'transcript.md');
        updateEpisode = true;
      } else if (options.output) {
        outputPath = options.output;
      } else {
        // Output to stdout if no destination specified
        console.log(chalk.green('\n--- Transcript ---\n'));
        console.log(transcript);
        return;
      }

      // Format as markdown
      const transcriptMd = `# Transcript

> Auto-generated from YouTube captions for video: ${youtubeId}
> Generated: ${new Date().toISOString()}

${transcript}
`;

      writeFileSync(outputPath, transcriptMd);
      console.log(chalk.green(`Transcript saved: ${outputPath}`));

      // Update episode youtube_id if saving to episode
      if (updateEpisode && options.episode) {
        const episode = getEpisode(options.episode);
        if (episode && !episode.metadata.youtube_id) {
          const indexPath = join(episode.path, 'index.md');
          const content = readFileSync(indexPath, 'utf-8');
          const { data, content: body } = matter(content);
          data.youtube_id = youtubeId;
          const updated = matter.stringify(body, data);
          writeFileSync(indexPath, updated);
          console.log(chalk.dim(`Updated episode youtube_id: ${youtubeId}`));
        }
      }
    } catch (error) {
      console.error(chalk.red(`Error: ${(error as Error).message}`));
      process.exit(1);
    }
  });
