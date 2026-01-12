#!/usr/bin/env node

import { Command } from 'commander';
import { listCommand } from './commands/list.js';
import { newCommand } from './commands/new.js';
import { thumbnailCommand } from './commands/thumbnail.js';
import { transcriptCommand } from './commands/transcript.js';

const program = new Command();

program.name('sss').description('Ship Sh!t Show CLI - YouTube content management').version('0.1.0');

program.addCommand(newCommand);
program.addCommand(thumbnailCommand);
program.addCommand(transcriptCommand);
program.addCommand(listCommand);

program.parse();
