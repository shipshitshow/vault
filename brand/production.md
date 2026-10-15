# Export and production handoff

Platform guidance verified **15 October 2026**; recheck linked specifications at release. House layout values are starting points, not platform rules.

| Asset | Target/guidance | Release check |
| --- | --- | --- |
| Avatar | Square master; YouTube display 98×98, JPG/PNG accepted | Real circular crop and file limit |
| YouTube banner | Recommended 2560×1440; minimum 2048×1152. Safe text/logo area at that minimum: 1235×338; maximum 6 MB | Mobile/desktop/TV crops; label scaled guides as scaled |
| Video thumbnail | Current YouTube recommendation 3840×2160, 16:9; minimum width 640 | Feed-size readability, source/title match, upload-device file limit |
| Shorts artwork | Current YouTube recommendation 2160×3840, 9:16; minimum height 640 | Actual crop and available desktop upload workflow |
| Podcast cover | Apple prefers 3000×3000 JPG/PNG, no alpha; RSS accepts 1400–3000 square | Full name, official template/safe area, no extra platform logos |
| Broadcast graphic | 1920×1080 starting canvas; transparent PNG for overlay | Alpha and actual camera/caption fit |

Sources: [YouTube branding](https://support.google.com/youtube/answer/10456525?hl=en), [thumbnails](https://support.google.com/youtube/answer/72431?hl=en), [Apple cover](https://podcasters.apple.com/support/5514-show-cover-template), [Restream](https://support.restream.io/en/articles/8540835-add-graphics-to-your-stream-in-studio). YouTube thumbnail file limits vary by upload device; do not assume a universal old 2 MB limit.

## Status and receipt

Read [inventory.json](inventory.json). `working-export` supplies a usable composition reference, without implying all destination checks passed. `draft-reference` is for design discussion, not release, logo extraction or live footage. Reserve `approved-export` for an actual release with approval/check receipts; no board has this status.

The red/black logo is a standalone JPG with actual dimensions recorded in the inventory. No vector master or transparent unboxed variants are included yet.

For every new export record:

- ID/version, relative file, hash, actual dimensions/format/alpha and destination.
- Authorized source/photo/logo IDs, rights, tool/model if exposed, prompt/recipe, native project and fonts.
- Kit revision/commit, overrides and reason.
- Spelling, source-claim, likeness, real-size, responsive-crop and contrast checks.
- For motion: duration, frame rate, codec/audio, alpha and transition point.
- Technical validation, actual playback/listening/Studio checks and approval/date separately.

Do not infer PASS from generation/render success, or invent a model ID, seed or approval. Keep masters, previews and exports separate; preserve old versions and update hashes when files change.

## Repository handoff

1. Update this kit, tokens and inventory first.
2. Update public skills' canonical `profiles/shipshitshow.md`, then run its existing `scripts/sync-profiles.py`.
3. Refresh producer adapters using `scripts/sync-content-skills.py --source <skills-checkout>` and its lockfile.
4. Copy only authorized required assets into the edit; record hashes and kit revision. Keep private originals/native media outside public repositories.
5. Run affected checks on the permitted verification host and retain current-head CI. Documentation merge does not update live channel art or deploy a website.
