#!/usr/bin/env python3
"""
Refresh transcript and thumbnail note wrappers for the Ship Sh!t Show vault.

- Rewrites `transcript.md` notes into a more readable format with parent links.
- Creates/updates `thumbnail.md` wrapper notes so thumbnails backlink to overview.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CHANNEL_DIRS = [
    ROOT / "shipshitshow" / "Videos",
    ROOT / "shipshitshow" / "Livestreams",
    ROOT / "shipshitshowclips" / "Shorts",
]


def load_overview_title(overview_path: Path) -> str:
    text = overview_path.read_text(encoding="utf-8")
    match = re.search(r'^title:\s*"(.*)"\s*$', text, re.MULTILINE)
    if match:
        return match.group(1)

    heading = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if heading:
        return heading.group(1).strip()

    return overview_path.parent.name


def to_vault_link(path: Path) -> str:
    """Convert an absolute path to a vault-relative posix path for wikilinks."""
    return path.relative_to(ROOT).as_posix()


def load_overview_youtube_url(overview_path: Path) -> str | None:
    text = overview_path.read_text(encoding="utf-8")
    match = re.search(r'^youtube_url:\s*"(.*)"\s*$', text, re.MULTILINE)
    return match.group(1) if match else None


def normalize_transcript_body(existing_text: str) -> tuple[str | None, str]:
    transcript_section = existing_text
    if "\n### Transcript\n" in existing_text:
        transcript_section = existing_text.rsplit("\n### Transcript\n", 1)[1]

    lines = transcript_section.splitlines()
    source_line: str | None = None
    body_lines: list[str] = []

    for line in lines:
        stripped = line.strip()
        if stripped == "# Transcript":
            continue
        if stripped.startswith("> Auto-imported from YouTube captions for "):
            source_line = stripped.removeprefix("> ").strip()
            continue
        if stripped.startswith("[[/Users/") or stripped.startswith("[[shipshitshow") or stripped.startswith("[[shipshitshowclips"):
            continue
        if stripped in {"### Context", "### Source", "### Transcript"}:
            continue
        if stripped.startswith("- Parent: [[") or stripped.startswith("- Description: [[") or stripped.startswith("- Thumbnail: [["):
            continue
        if stripped.startswith("- YouTube: http"):
            continue
        if stripped.startswith("## "):
            continue
        if stripped.startswith("![[thumbnail.png"):
            continue
        body_lines.append(line.rstrip())

    body = "\n".join(body_lines).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    return source_line, body


def build_transcript_note(overview_path: Path, transcript_path: Path) -> str:
    title = load_overview_title(overview_path)
    youtube_url = load_overview_youtube_url(overview_path)
    source_line, body = normalize_transcript_body(transcript_path.read_text(encoding="utf-8"))
    overview_link = to_vault_link(overview_path)
    description_link = to_vault_link(overview_path.parent / "description.md")
    thumbnail_note_link = to_vault_link(overview_path.parent / "thumbnail.md")
    has_thumbnail = overview_path.parent.joinpath("thumbnail.png").exists()

    parts = [
        "# Transcript",
        "",
        f"[[{overview_link}|<- Back to video]]",
        "",
        f"## {title}",
        "",
    ]

    if has_thumbnail:
        parts.extend([
            "![[thumbnail.png|640]]",
            "",
        ])

    parts.extend([
        "### Context",
        "",
        f"- Parent: [[{overview_link}|{title}]]",
        f"- Description: [[{description_link}|Description]]",
    ])

    if has_thumbnail:
        parts.append(f"- Thumbnail: [[{thumbnail_note_link}|Thumbnail]]")
    if youtube_url:
        parts.append(f"- YouTube: {youtube_url}")

    parts.extend([
        "",
        "### Source",
        "",
        f"> {source_line or 'Auto-imported from YouTube captions.'}",
        "",
        "### Transcript",
        "",
        body,
        "",
    ])

    return "\n".join(parts)


def build_thumbnail_note(overview_path: Path) -> str:
    title = load_overview_title(overview_path)
    youtube_url = load_overview_youtube_url(overview_path)
    overview_link = to_vault_link(overview_path)
    transcript_link = to_vault_link(overview_path.parent / "transcript.md")
    description_link = to_vault_link(overview_path.parent / "description.md")

    parts = [
        "# Thumbnail",
        "",
        f"[[{overview_link}|<- Back to video]]",
        "",
        f"## {title}",
        "",
        "![[thumbnail.png]]",
        "",
        "### Context",
        "",
        f"- Parent: [[{overview_link}|{title}]]",
        f"- Transcript: [[{transcript_link}|Transcript]]",
        f"- Description: [[{description_link}|Description]]",
    ]

    if youtube_url:
        parts.append(f"- YouTube: {youtube_url}")

    parts.append("")
    return "\n".join(parts)


def refresh_directory(content_dir: Path) -> int:
    changed = 0
    for overview_path in sorted(content_dir.glob("**/overview.md")):
        asset_dir = overview_path.parent
        transcript_path = asset_dir / "transcript.md"
        thumbnail_image_path = asset_dir / "thumbnail.png"
        thumbnail_note_path = asset_dir / "thumbnail.md"

        if transcript_path.exists():
            new_transcript = build_transcript_note(overview_path, transcript_path)
            if transcript_path.read_text(encoding="utf-8") != new_transcript:
                transcript_path.write_text(new_transcript, encoding="utf-8")
                changed += 1

        if thumbnail_image_path.exists():
            new_thumbnail_note = build_thumbnail_note(overview_path)
            if not thumbnail_note_path.exists() or thumbnail_note_path.read_text(encoding="utf-8") != new_thumbnail_note:
                thumbnail_note_path.write_text(new_thumbnail_note, encoding="utf-8")
                changed += 1

    return changed


def main() -> int:
    changed = 0
    for content_dir in CHANNEL_DIRS:
        changed += refresh_directory(content_dir)
    print(f"Updated {changed} asset notes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
