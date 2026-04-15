#!/usr/bin/env python3
"""
Normalize imported vault frontmatter for Obsidian compatibility.

This rewrites `tags:` to `youtube_tags:` in overview frontmatter so YouTube
keyword phrases do not get treated as invalid Obsidian tags.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
TARGET_GLOB = "**/overview.md"


def replace_frontmatter_tags(content: str) -> tuple[str, bool]:
    """Rename the special Obsidian `tags` property to `youtube_tags`."""
    if not content.startswith("---\n"):
        return content, False

    frontmatter_end = content.find("\n---\n", 4)
    if frontmatter_end == -1:
        return content, False

    frontmatter = content[: frontmatter_end + 5]
    updated_frontmatter = frontmatter.replace("\ntags:\n", "\nyoutube_tags:\n", 1)
    if updated_frontmatter == frontmatter:
        return content, False

    return updated_frontmatter + content[frontmatter_end + 5 :], True


def normalize_file(file_path: Path, check_only: bool) -> bool:
    """Normalize a single overview file."""
    original = file_path.read_text(encoding="utf-8")
    updated, changed = replace_frontmatter_tags(original)
    if not changed:
        return False

    if not check_only:
        file_path.write_text(updated, encoding="utf-8")

    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize YouTube vault frontmatter")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report files that would change without writing them",
    )
    args = parser.parse_args()

    changed_files: list[Path] = []

    for file_path in sorted(WORKSPACE_ROOT.glob(TARGET_GLOB)):
        if normalize_file(file_path, check_only=args.check):
            changed_files.append(file_path.relative_to(WORKSPACE_ROOT))

    if args.check:
        if changed_files:
            print("Files requiring normalization:")
            for path in changed_files:
                print(f" - {path}")
            return 1

        print("All overview frontmatter is normalized.")
        return 0

    if changed_files:
        print("Normalized frontmatter in:")
        for path in changed_files:
            print(f" - {path}")
    else:
        print("No changes needed.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
