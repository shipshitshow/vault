#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

cd "$ROOT"

biome format --write \
  biome.json \
  .obsidian \
  "00 Home.md" \
  "01 Content Map.md" \
  README.md \
  shipshitshow \
  shipshitshowclips \
  _admin/docs
