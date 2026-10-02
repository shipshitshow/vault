# October 2 audit

- [Project and production audit](project-audit.md): findings, evidence, proposed folders and skills, and decisions still to settle.
- [Transcript coverage ledger](transcript-coverage.csv): 144 known YouTube uploads, identified by channel and YouTube ID.

The ledger combines the app's July 13 main-channel inventory with public main-channel and Clips-channel tabs observed October 2. It is a lower bound, not a complete account-owner export. An older upload absent from current public tabs has unresolved visibility; it is not assumed deleted or private.

Coverage statuses:

| Status | Count | Meaning |
| --- | ---: | --- |
| `archived_in_vault` | 47 | Nonempty transcript already present in the vault |
| `transcript_available_to_import` | 29 | Missing from vault; an app or Studio transcript was located |
| `transcript_not_located` | 68 | Missing from vault; no transcript located in audited sources |

App transcript paths are relative to `show.shipshit.dev`. Studio source labels identify the media library and project; they are not portable filesystem paths. Vault paths are relative to this repository. Blank publication dates were not recovered from the tab listing. Availability does not assert corrected ASR, complete coverage or a verified source-to-derivative relationship.

This is the initial audit snapshot, preserved for history. Follow the [maintained coverage ledger](../../../data/youtube-coverage.csv) and [production handbook](../../../../production/index.md) for subsequent recovery and implementation. The October 2 working catalog now contains transcripts for all 147 identified uploads; publication/review status is tracked in GitHub pull requests.
