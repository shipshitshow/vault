import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import chalk from 'chalk';
import { Command } from 'commander';
import matter from 'gray-matter';
import Handlebars from 'handlebars';
import type { ThumbnailPromptConfig } from '../types.js';
import { getEpisode } from '../utils/content.js';

const PROMPTS_DIR = resolve(process.cwd(), 'prompts');
const DEFAULT_PROMPT = join(PROMPTS_DIR, 'thumbnail.default.md');

interface GenFeedImageResponse {
  id: string;
  status: string;
  url?: string;
}

async function generateThumbnail(
  prompt: string,
  config: ThumbnailPromptConfig
): Promise<GenFeedImageResponse> {
  const apiKey = process.env.GENFEED_API_KEY;
  if (!apiKey) {
    throw new Error('GENFEED_API_KEY environment variable is not set');
  }

  const response = await fetch('https://api.genfeed.ai/v1/images', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      prompt,
      model: config.model,
      width: config.width,
      height: config.height,
      outputs: config.outputs,
      category: 'image',
    }),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`GenFeed API error: ${error}`);
  }

  return response.json();
}

async function waitForImage(id: string): Promise<string> {
  const apiKey = process.env.GENFEED_API_KEY;
  if (!apiKey) {
    throw new Error('GENFEED_API_KEY environment variable is not set');
  }

  const maxAttempts = 60;
  let attempts = 0;

  while (attempts < maxAttempts) {
    const response = await fetch(`https://api.genfeed.ai/v1/images/${id}`, {
      headers: {
        Authorization: `Bearer ${apiKey}`,
      },
    });

    if (!response.ok) {
      throw new Error(`Failed to check image status: ${response.statusText}`);
    }

    const data = (await response.json()) as { status: string; url?: string };

    if (data.status === 'completed' && data.url) {
      return data.url;
    }

    if (data.status === 'failed') {
      throw new Error('Image generation failed');
    }

    await new Promise((r) => setTimeout(r, 2000));
    attempts++;
  }

  throw new Error('Timeout waiting for image generation');
}

async function downloadImage(url: string, destPath: string): Promise<void> {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to download image: ${response.statusText}`);
  }

  const buffer = await response.arrayBuffer();
  writeFileSync(destPath, Buffer.from(buffer));
}

export const thumbnailCommand = new Command('thumbnail')
  .description('Generate thumbnail for an episode using GenFeed.ai')
  .argument('<episode>', 'Episode slug')
  .option('-p, --prompt <text>', 'Additional prompt text')
  .option('-c, --count <n>', 'Number of variations to generate', '1')
  .option('--dry-run', 'Show prompt without generating')
  .action(
    async (episodeSlug: string, options: { prompt?: string; count?: string; dryRun?: boolean }) => {
      const episode = getEpisode(episodeSlug);
      if (!episode) {
        console.error(chalk.red(`Episode not found: ${episodeSlug}`));
        process.exit(1);
      }

      // Load prompt template
      const episodePromptPath = join(episode.path, 'thumbnail.prompt.md');
      const promptPath = existsSync(episodePromptPath) ? episodePromptPath : DEFAULT_PROMPT;

      if (!existsSync(promptPath)) {
        console.error(chalk.red(`No prompt template found at ${promptPath}`));
        process.exit(1);
      }

      const promptFile = readFileSync(promptPath, 'utf-8');
      const { data: promptConfig, content: promptTemplate } = matter(promptFile);

      // Compile template with episode data
      const template = Handlebars.compile(promptTemplate);
      let finalPrompt = template({
        ...episode.metadata,
        topics: episode.metadata.topics.join(', '),
        guests: episode.metadata.guests.join(', '),
      });

      // Add custom prompt if provided
      if (options.prompt) {
        finalPrompt += `\n\nAdditional requirements: ${options.prompt}`;
      }

      const config: ThumbnailPromptConfig = {
        model: (promptConfig.model as string) || 'flux-pro',
        width: (promptConfig.width as number) || 1920,
        height: (promptConfig.height as number) || 1080,
        outputs: parseInt(options.count || '1', 10),
      };

      console.log(chalk.bold(`\nGenerating thumbnail for: ${episode.metadata.title}\n`));
      console.log(chalk.dim('Prompt:'));
      console.log(chalk.dim(finalPrompt.trim()));
      console.log();
      console.log(chalk.dim(`Model: ${config.model}`));
      console.log(chalk.dim(`Size: ${config.width}x${config.height}`));
      console.log(chalk.dim(`Outputs: ${config.outputs}`));

      if (options.dryRun) {
        console.log(chalk.yellow('\n--dry-run: Skipping generation'));
        return;
      }

      try {
        console.log(chalk.cyan('\nSubmitting to GenFeed.ai...'));
        const result = await generateThumbnail(finalPrompt, config);

        console.log(chalk.cyan(`Waiting for generation (ID: ${result.id})...`));
        const imageUrl = await waitForImage(result.id);

        const destPath = join(episode.path, 'thumbnail.png');
        console.log(chalk.cyan('Downloading image...'));
        await downloadImage(imageUrl, destPath);

        console.log(chalk.green(`\nThumbnail saved: ${destPath}`));
      } catch (error) {
        console.error(chalk.red(`\nError: ${(error as Error).message}`));
        process.exit(1);
      }
    }
  );
