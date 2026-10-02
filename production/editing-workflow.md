# Editing library and public handoff

Canonical media workspace on Studio: `~/www/tesseract`. Editing uses the installed Tesseract plugin with GPT/Claude. The workspace is local-only; do not initialize/publish the whole media library as a Git repository.

## Folder ownership

```text
tesseract/
  assets/                         shared host photos, logos and licensed media
  projects/<YYMMDD[-slug]>/
    project.json                  source identity, recording date, derivative IDs
    raws/                         original recording and source transcript/captions
    assets/audio/                 episode treatment assets/recipes
    outputs/                      current work; previews/ and work/ intermediates
      shorts/
        working/<slug>/
        versions/vNNN/<slug>/
        final/<slug>/             portrait; optional landscape/; captions/copy/cuts
    versions/vNNN/                meaningful long-form checkpoints
    final/                        approved native project/export, transcript,
                                  captions, cuts, context, audio notes and manifest
  _labs/                          branding/motion experiments
```

This follows the existing September 29 project. Preserve working media references; folder improvements do not require moving old recordings. Date keys refer to recording, not publication. Add a slug for same-date collisions. Keep the project's own supported schema; store source livestream ID and published recap/Short IDs when known.

`outputs` holds current work; `versions` preserves milestones; `final` is an identified reviewed version. A finished render is not sufficient approval. Record technical metadata, source-meaning comparison, playback, listening and sync checks independently. Preserve replacement history and external mastering recipes so the final remains reproducible from its native project and sources.

Make checkpoints for meaningful changes: first assembly, reviewed cut, audio/captions and approved export. Do not automatically delete historical versions. September 29 currently has 62 packaged native archives and uses about 37 GB; choose retention after identifying authoritative deliverables.

## Tool and audio checks

Before the next edit, verify the installed CLI matches the installed plugin's supported version. October 2 audit found CLI 0.3.0 versus plugin/runtime pin 0.3.1. Use the official plugin instructions for operations; this handbook does not duplicate its API schema.

Treat audio per recording. Preserve raw audio and processing chain/tool versions. Measure export levels where available, then listen to speech, difficult passages and changed joins and check lip sync. Do not reuse a previous episode's EQ or sample offset blindly. Mark listening unavailable when it was not performed.

## Public handoff

Vault owns public transcripts, captions, cut maps, description context, metadata and episode relationships. Skills owns reusable instructions; examples owns demo code linked to a livestream. Keep recordings, large exports and `.tsrct` packages in the media library. Public manifests omit private absolute paths, credentials and signed URLs.

The September 29 source stream and October 1 recap have different clocks. Preserve their own transcript/captions and `cuts.csv` mapping. Shorts have their own clocks and source links.

## Legacy media

Preserve `~/DeCod3rs/_raws`, `2026/Pr` and `2026/finals` as the legacy Premiere library. Native project references, autosaves, captions and unexported prepared Shorts remain useful. Reconcile them without folder moves or deletion.
