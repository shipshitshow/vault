import chalk from 'chalk';
import { Command } from 'commander';
import { getAllEpisodes } from '../utils/content.js';

export const listCommand = new Command('list')
  .description('List all episodes')
  .option('-j, --json', 'Output as JSON')
  .action((options: { json?: boolean }) => {
    const episodes = getAllEpisodes();

    if (episodes.length === 0) {
      console.log(chalk.yellow('No episodes found'));
      return;
    }

    if (options.json) {
      console.log(
        JSON.stringify(
          episodes.map((ep) => ep.metadata),
          null,
          2
        )
      );
      return;
    }

    console.log(chalk.bold(`\nShip Sh!t Show Episodes (${episodes.length})\n`));

    for (const episode of episodes) {
      const { metadata } = episode;
      const hasThumb = metadata.thumbnail ? chalk.green('[thumb]') : chalk.dim('[no thumb]');
      const hasYt = metadata.youtube_id ? chalk.green('[yt]') : chalk.dim('[no yt]');

      console.log(`${chalk.cyan(metadata.id)} ${chalk.white(metadata.title)} ${hasThumb} ${hasYt}`);
      console.log(
        chalk.dim(
          `  ${metadata.date} | ${metadata.type} | ${metadata.topics.join(', ') || 'no topics'}`
        )
      );
      console.log();
    }
  });
