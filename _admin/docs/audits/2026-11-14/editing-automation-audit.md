# Editing automation audit

Audited: 2026-11-14. Status: findings and proposals, before implementation.

Nothing on this page is a rule. The edit rules are in [brand/editing.md](../../../../brand/editing.md) and change only when the owner asks. Everything marked "proposed" here waits on the owner.

## Owner direction

Vincent, 14 Nov 2026: more automation and more radical takes, so the Shorts get better. The goal for the next episode is that the edit and the release package need his hands only where a human is required: recording, approving, watching and listening, publishing.

## Sources and limits

| Checked | How |
| --- | --- |
| ForwardEditor's "How to vibe edit" video on X ([post](https://x.com/ForwardEditor/status/2120596951175463322), 10 min 52 s) | Downloaded, transcribed with whisper, one frame sampled every 5 seconds |
| This vault | `brand/` and `production/` pages at master on 14 Nov |
| The show repo | `editing/scripts/`, `docs/show-prep/` and `skills/` at master on 14 Nov |
| The 261111 project in the content tree | Folder layout, publish plan, Shorts copy, X post drafts, thumbnail drafts |

Not verified: nobody ran the chapter runner on a real episode for this audit; the X video was read from its transcript and frames, not watched with sound; whether the YouTube API can set a Short's Related video; what exactly the owner disliked about the 261111 tweet.

## How ForwardEditor edits

Brian's post was the topic of episode 261111. His video is a sponsored demo: he dictates prompts to an AI agent that cuts a Short and builds it into DaVinci Resolve. This is a reference study, the same way [brand/references.md](../../../../brand/references.md) is: take the method, not the look or the tools.

### His process

- One long first brief, dictated, not typed. It names the footage folder, the format (9:16), where captions sit (a safe zone away from the edges), the type (bold sans, no stroke), where b-roll goes (one half of the frame) and asks the agent to find the through-line from the transcript itself.
- He judges a pass from its first few seconds. A mistake there is repeated through the rest, so he stops, fixes the cause and re-runs the whole pass.
- He reviews with the microphone on: watch, pause, speak, keep watching, then, in his words, "send one big long prompt". About four minutes per prompt and about fifteen minutes of his own time across versions V1 to V7. The first cut took the agent 16.5 minutes and the revision 21.
- Corrections are numbers and positions, not adjectives. When words fail he pastes a link to an earlier post as the visual reference.
- Fixes become standing rules the agent must never break again (the safe zone, blurring street signs and other privacy leaks).
- The cut audit he asks for: match every syllable in the transcript to a syllable in the waveform, and treat steady background noise (a passing car) as silence when trimming pauses.
- The screen is never empty: bold, slower text and real footage instead of text-only b-roll.
- Audio: clean wind and hiss, then mask what is left with a music bed.
- He does not publish what he has not watched. A weak pass goes back.

### How the tutorial itself is cut

- Cold open on the title in bold condensed white type, then an animated timeline graphic around his head for the first 20 seconds.
- The layout changes every 5 to 15 seconds: full talking head, head with floating app icons, a full-screen card, screen recording with a rounded picture-in-picture, picture-in-picture left with the Short previewing right.
- The background colour changes per section, with a diagonal wipe as the chapter marker.
- Key terms pop as text when he says them. The first prompt appears on a card. Red arrows and circles point at what he is criticising.
- Scene detection found only 16 hard cuts in almost 11 minutes. The pace comes from layout changes over one continuous take, not from cutting.

### What the agent reports back

- It says plainly what it could not check: it could not listen, placed the audio cuts in the quietest spots of the waveform and asked for a listen at the joins.
- Versioned outputs, with a revisions log and a credits file for stock b-roll.
- A privacy sweep with a count (102 candidate spots flagged).
- A loudness line (-14 LUFS).

### The Short he builds

9:16, b-roll in the top half and the speaker in the bottom half, captions in lowercase bold white sans without a stroke, two to four words at a time, mid-frame. He rejects stacked text label cards.

### What fits this show

| Idea | Fit |
| --- | --- |
| One standing brief per episode, kept with the project | Fits. The rulebook plus `chapters.json` already play this role; the brief should be one file the agent reads first |
| Judge the first seconds, then fix the whole pass | Fits the chapter gates |
| Syllable-to-waveform cut audit, background noise counted as silence | Fits. Extends the "filler at cut edges" check in step 10 |
| Visual references and numeric corrections in review notes | Fits |
| Versioned outputs with a revisions log and b-roll credits | Fits |
| Automated privacy and text sweep before upload | Fits. New check |
| The agent states what it could not hear | Already the rule ("nobody has listened unless the owner says so") |
| Layout change every 5 to 15 seconds, keyword pops, red arrow and circle annotations | Proposed. Works with "hosts first" only as integrated motion |
| Text cards and coloured section slabs | Conflicts with "No text cards" (3 Nov). Owner's call |
| Punch-ins and zoom on the speaker | Does not fit ("No zoom on people", 4 to 5 Nov) |
| DaVinci Resolve through an MCP, the sponsored agent harness | Does not fit. The show's edit is ffmpeg plus the scripts in the show repo |

## Current workflow, as audited

| Stage | What exists | State |
| --- | --- | --- |
| Prep | `prep`, `hooks` and `cues` skills, `bun run show:prep save`, `docs/show-prep/editorial-format.md` (stance check, planned Short cards, one controversial angle per episode) | Documented in the show repo only. Not in this vault |
| Workspace | `editing/scripts/workspace.py init`, one content tree | Works |
| Transcript | whisper, `bun run transcripts:import --write` | Works |
| Long video | `editing/scripts/chapters/run_chapters.py` (`plan`, `chapter <n>`, `all`, `stitch`) from `chapters.json` | Plain cuts only, dry-run on 261111. Motion, matte, b-roll, mascot, J/L edits, music lift and caption sync still come from per-episode scripts |
| Host matte | `editing/scripts/matte/` | Works as a separate step |
| Shorts | `editing/scripts/shorts/` (`align.py`, `build.py`, `finalize.py`) | Builds the 261103 single-speaker layout. The stacked two-host layout approved on 12 Nov has no tracked builder |
| Take-picking | `clips` skill: rubric, first-line test, clip types | Done by reading the transcript in a session. No script, no ranked output file |
| Package | `metadata` skill, `bun run youtube:metadata` | Title, description, chapters and Shorts copy written per episode. No length or Title Case check |
| Thumbnails | `bun run thumbnail:stamp`, a draft template of 12 Nov | Template not locked. The checks it lists (size, mark position, OCR, faces, small-size legibility) are not scripted |
| X | `x` skill (drafts only) | The 261111 drafts did not go through the skill's quality gate. The burned-caption X copy was made by hand |
| Upload | `bun run youtube:upload` (private by default) | Works. Related video and the "Full episode" link are set by hand after publish |

## Gap list

### Undocumented in the vault

1. The tweet. No page says what the X post must contain. The only standard is the `x` skill in the show repo (take first, one concrete receipt, one link, under about 240 characters, every claim traceable to the transcript).
2. The burned-caption X copy of the video. Shipped on 261111, specified nowhere (size, caption style, length limit, where the mark goes).
3. The tweet and the X copy are not in the deliverables table or in step 12 of the pipeline.
4. Title Case for titles, and any check on length. The rule says about 45 characters at most; two of the three 261111 options were 50.
5. Three thumbnails per episode as a deliverable, and the podcast-layout template (drafted 12 Nov, not locked).
6. The publish schedule (Shorts spaced around the main video on release day).
7. The take-picking rubric and the channel data behind the first-line test. Only in the `clips` skill.
8. The editorial format: one controversial angle per episode (8 Oct), stance check, planned Short cards and clean recording boundaries (10 Nov). Only in the show repo. This PR adds a pointer in [show preparation](../../../../production/show-preparation.md).
9. Which script builds the stacked Shorts layout. None is tracked.

### Pages that disagree

| Topic | One page says | Another says |
| --- | --- | --- |
| Short video layout | `brand/placement.md`: speaker fills the frame, uppercase captions at y1480 (5 Nov) | `brand/editing.md`: stacked two-host layout (12 Nov), which replaces it. The `clips` skill still shows the 5 Nov layout |
| Host faces | `brand/applications.md`: topic first, no host faces in thumbnails (26 Oct) | `brand/editing.md`: Shorts cover is a host close-up (13 Nov). The draft thumbnail template puts both hosts on every thumbnail |
| Shorts true peak | `brand/editing.md` Shorts table: -1 dBTP | The Shorts scripts and the recap master: -1.5 dBTP |
| Shorts length | `brand/editing.md` and the `clips` skill: under 60 seconds (5 Nov) | `editorial-format.md` in the show repo: roughly 45 to 90 seconds |
| 16:9 safe zone, screen-share watermark | `brand/placement.md`: both still "proposed" | `brand/editing.md`: no persistent watermark over screen shares |
| X link | 261111 drafts: link in the first reply, no tag | `x` skill: one link, last, UTM-tagged |
| Skill links | `brand/editing.md` links the overlay, dialogue, recap and library contracts to the public skills repo and says the `clips` skill loads the page | `clips`, `hooks`, `cues` and `x` exist only in the show repo's `skills/` |

### Stale pages

- [production/editing-workflow.md](../../../../production/editing-workflow.md) and the show repo's `editing/README.md` and `editing/AGENTS.md` still describe the Tesseract (`tsrct`) path, which is not installed and was not used on 261111.
- The `clips` skill's layout and cover sections predate 12 Nov.
- The show repo's `editorial-format.md` length line predates the under-60-seconds decision.

### Still needs the owner's hands

- Recording and going live.
- Before the show: his own one-line verdict per segment and approval of the first sentence.
- The gates: chapter plan, Shorts plan with one layout example, thumbnails, private uploads.
- Watching and listening. A render is not a review.
- Making uploads public, posting on X.
- Setting each Short's Related video in YouTube Studio (until an API route is verified).
- The decisions listed at the end of this page.

### Can be automated

In the order that removes the most hand work for the next episode:

1. **Take-picking pass.** A script that scores every sentence in the word-level transcript with the `clips` rubric and the first-line test, maps hits to the planned Short cards, and writes the ranked Gate 3 plan with source ranges. It also reports which planned Shorts were actually said on air.
2. **Stacked Shorts builder.** Port the 261111 Short 01 v2 build into `editing/scripts/shorts/` so the approved layout comes from a tracked script with the caption chunking, the mark position and the loudness target built in.
3. **Chapter runner layers.** Move matte, b-roll, mascot, J/L split edits, the music lift under the goodbye and independent caption sync from the per-episode scripts into `run_chapters.py`, driven by `chapters.json`.
4. **Cut audit.** After each chapter render: filler words at cut edges, and every transcript word matched to speech in the waveform, with steady background noise treated as silence.
5. **Package generator with checks.** Title options that fail the build when over 45 characters or not in Title Case; description and chapters from the final timeline; Shorts copy; three tweet drafts built from real quotes and numbers in the episode, checked against the `x` quality gate.
6. **Burned-caption X copy.** One command from the final master and the caption file.
7. **Thumbnail checks.** The script checks the draft template already lists.
8. **Privacy and text sweep.** Flag frames with readable personal data, keys or third-party names in screen shares before upload.
9. **After publish.** Add the "Full episode" link to each Short's description. Related video stays manual until an API route is verified.

## Radical takes (proposed)

Update, 14 Nov 2026: the owner made steps 1 to 3 rules for every episode. They now live in `production/show-preparation.md`. Steps 4 to 6 stay proposals.

The limits already decided stay: plan the question, not the disagreement; nobody writes a view for a host; a host never defends a view they do not hold; nothing is stitched into a stronger claim than what was said; the title must describe what the recording supports. Inside those limits, what is missing is not opinions but sentences. On 261111 the takes existed, and the Shorts still had to be found afterwards.

1. **Headline verdict at prep.** Each host turns their own one-line verdict per segment into a headline-shaped sentence: a named target, a number, or an absolute ("X is dead"). The prep board runs the `clips` first-line test on it and reports pass or fail. It never rewrites it.
2. **Provocation questions.** `prep` and `hooks` generate two or three questions per segment: the strongest uncomfortable version of the question, never an answer. The host who asks does not have to hold the view.
3. **Headline cue.** `cues` adds one cue at the close of each segment: say the verdict to the lens as one standalone sentence that names the subject, then pause for one second. That sentence is the Short's first line and the pause is the clean cut point.
4. **Live markers.** Hosts log a rough marker when a take lands. The take-picking pass reads the markers as hints.
5. **Automated take-picking.** Item 1 under "Can be automated". The ranked plan reaches the owner for Gate 3 the same day.
6. **Weekly review.** Track which take shapes earn views (absolute, number, named target, host disagreement) and feed that back into the prep questions.

## Decisions for the owner

All six were answered by the owner on 14 Nov 2026. Each outcome follows its question.

1. Thumbnails and covers: reverse "no host faces" (26 Oct) and lock the podcast-layout template, or keep topic-first. **Outcome:** already decided on 11 to 13 Nov, before this audit: hosts appear, large at the edges, with the topic person centred behind them and no title text. The audit missed it because the vault still carried the 26 Oct rule. Now in `brand/applications.md`.
2. Adopt the radical-take steps 1 to 3 as dated rules. **Outcome:** adopted, 14 Nov.
3. The tweet standard: take first, one real quote or number from the episode, the burned-caption video attached; and where the link goes (last line with a UTM tag, or first reply). **Outcome:** adopted, 14 Nov, with the link in the first reply and three checks: a real line, number or host clash; the opinion first; short and blunt in the owner's voice.
4. Shorts true peak: -1 or -1.5 dBTP. **Outcome:** -1.5 dBTP, 14 Nov.
5. Confirm the 16:9 safe zone in `brand/placement.md`. **Outcome:** confirmed, 14 Nov, together with no persistent corner watermark on screen shares.
6. Shorts length in the planned Short cards: under 60 seconds everywhere, or keep 45 to 90 for planning. **Outcome:** 45 to 90 seconds, 14 Nov; the rulebook now says the same.
