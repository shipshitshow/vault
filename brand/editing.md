# Editing, captions and broadcast

This is the one source of the edit rules for Ship Sh*t Show recaps, edited videos and Shorts, and for the broadcast scenes. It is the owner's decisions (Vincent), 3 to 14 November 2026, taken from the 261103 recap and the 261111 recap and Shorts. The show repo keeps only build values and script names in `docs/show-prep/edit-style.md` ([source](https://github.com/shipshitshow/show.shipshit.dev/blob/master/docs/show-prep/edit-style.md)) and points here. If the two disagree, this page wins.

Use [identity](identity.md), [tokens](tokens.json), [placement](placement.md) and [inventory](inventory.json) with the actual recording and project. This kit does not replace the selected editor, streaming tool or an existing approved motion project.

## How this page is changed

- Change a rule only when the owner asks. The owner tells Claude "change rule X to Y"; Claude edits that one line, adds a row to the change log at the bottom, opens a PR and merges it when CI is green. Nothing else changes a rule.
- Every rule carries its date. A rule without a date is a default, not a decision.
- Claude follows the page as written. If a request conflicts with a rule, Claude says so in one line and asks on a card before breaking it.
- The `recap`, `overlays`, `dialogue` and `clips` skills load this page first, so a change here reaches them without editing them.

## The job

Input: the raw livestream recording (one composited 1080p stream, no separate cam tracks), dropped on the Mac Studio. Output per episode, all private until the owner says go:

| Deliverable | Spec |
| --- | --- |
| Recap video | About 10 minutes by default. Longer (15 to 20) is fine when the story holds; length never beats storytelling (13 Nov). 1080p60 master plus a 720p review proxy |
| Chapters, captions, description, tags | From the final timeline, never the full-stream clock |
| 5 Shorts | 9:16, 45 to 90 s each (14 Nov), with covers, titles and descriptions |
| Title | About 45 characters at most, short and radical, in Title Case: every word capitalised (13 Nov). No "[LIVE]" |
| Thumbnails | Hosts at the edges, topic person centred behind them, no title text (11 to 13 Nov). Rules in [applications](applications.md) |
| Tweet | Take first, one real receipt from the episode, link in the first reply (14 Nov). See [Tweet and X copy](#tweet-and-x-copy) |
| X copy | The final video with captions burned in, at full quality, attached to the tweet (13 Nov) |
| Upload | Private, with metadata, only after the owner approves |

## Pipeline and gates

A gate is where Claude stops and shows the owner something before going on.

1. **Ingest.** The raw stays in `~/DeCod3rs/_raws/`. Create `~/content/brands/shipshitshow/projects/<YYYY-MM-DD>_<YYMMDD>/` with `raw/` (a link, never a copy), `out/video`, `out/shorts`, `project.md` and `episode.json`, with `editing/scripts/workspace.py init`. Never use the repo's old `editing/projects/`, which is retired.
2. **Transcript.** Local only. Word timestamps. Fix ASR names (Claude, Claude Code, Grok, PHP, Cloudflare, Ship Sh*t Show). Flag every proper noun that cannot be verified; none goes on screen unverified.
3. **Drop the dead parts.** The first 30 seconds (a deliberate countdown), greetings, tech fiddling, logistics.
4. **Edit plan and cut map.** The opening line, chapters with source ranges, one animation per idea change, claims to protect. **Gate 1: the owner sees the plan and transcript before any render.**
5. **Rough cut.** Hosts-first two-shot, filler removed, cuts on word boundaries, split edits where they help.
6. **Motion.** Build each planned animation, matte the hosts, lay the graphics in the visible zones, measure coverage.
7. **Sound.** Music bed, SFX, split edits, loudness.
8. **Chapter 1 sample. Gate 2:** the owner reviews chapter 1 with music and motion before the rest is rendered. Skipped only when the owner has approved the same recipe earlier in the series.
9. **Chapter review. Gate 2b:** the cut is split at its chapter boundaries into one 720p clip per chapter (`ch1-<slug>.mp4`, and so on). The owner reviews and gives notes chapter by chapter. A fix re-sends only the chapter clips it touches, plus any chapter a changed beat falls in. The full render waits until every chapter is approved.
10. **Full render and checks.** Probe, loudness, SAR and DAR, caption sync, filler at cut edges, subscribe asset and end screen.
11. **Shorts.** Plan first: candidate takes with source ranges, and one layout example. **Gate 3: the owner approves the Shorts plan before a batch is cut.**
12. **Package.** Title, description, chapters, tags, Shorts copy, the tweet and the burned-caption X copy.
13. **Upload private with metadata. Gate 4:** nothing is scheduled or made public without the owner's OK on a card. Each Short sets the full episode as its Related video once it is live.

Render success is not review. Report technical checks separately from whether anyone has watched and listened; nobody has listened unless the owner says so.

## Recaps and edited videos (16:9)

| Rule | Detail | Decided |
| --- | --- | --- |
| Hosts first | The default shot is Vincent left, Mitchell right, a steady 50/50. In screenshare stretches, rebuild the 50/50 from the cam tiles (static crop, no zoom). Hosts on screen at least 80% of the runtime | 11 Nov |
| Calm cutting | Adult pacing. No micro-cuts under about 0.5 s; cuts closer than 2 s apart are merged. No jumpy cutaway churn | 11 Nov |
| Hard cuts only | No fade to black, no dissolves, no alpha fades on overlays. The show's slash transition is the one exception (below) | 3 Nov |
| No text cards | No title cards, no topic-label cards between segments, no topic label on screen | 3 Nov |
| No zoom on people | Zoom on screen content only, and only on a proving number or a specific point | 4 to 5 Nov |
| Key-stat punch-in | When a host says a proving number (views, impressions), punch in about 4x on the stat on screen, a fast eased push timed to the spoken word, hold, then hard cut back. Never on people | 11 Nov |
| Keep the context | When a host shows a page to say who someone is, keep it with name and employer in frame. Never cut a sentence mid-thought | 11 Nov |
| Misclicks | Cut any clip that starts to play and is unusable | 12 Nov |
| Colour | Every recording is measured and corrected from its own footage before the recap and the Shorts are cut. No fixed look: the host cameras are brought to a natural result (exposure and skin tone) automatically, the shared screen is not touched, and the original stays untouched in `raw/`. Tool: `editing/scripts/grade/` in the show repo | 14 Nov |
| Dialogue cuts | Drop back-channels ("yeah", "exactly", "mhm") and restarts. Keep every qualification or opposing view that changes the answer | 3 Nov |

**Opening (11 Nov).** No greeting, chit-chat or filler. Open on the strongest lines from anywhere in the transcript (the central question, the bold answer, the counter-argument), not the chronological start. The first sound is a word, never "hmm", "uh", "yeah" or "so". No cut starts or ends on a filler word; a mid-sentence "um" is hidden under a planned cutaway or cut. The first sentence is the viewer promise (a claim plus the stake, under 15 seconds). Then 30 to 45 seconds of the 50/50 before any screenshare, with the first useful point by about 45 seconds. No subscribe ask before the first payoff. On a topic board, `## Cold Open` means the on-air first sentence.

**Ending (12 Nov).** Keep the hosts' real goodbye from the end of the stream, ending on a natural laugh or wave. Never a flat black card with an asterisk and "SUBSCRIBED". The last 10 to 12 seconds leave clean space for YouTube's end-screen elements (a video slot and a subscribe circle). The end screen is part of every recap and comes from the outro template below.

**Subscribe asset (12 Nov).** The real subscribe asset plays at about 2:00 and in the end screen.

**Chapters.** From the final timeline. The first at 0:00, at least three, each 10 seconds or more apart.

## Motion design

- **Built with Claude, not Codex (11 Nov).** HTML and SVG with GSAP, rendered frame by frame, at the quality bar of `yihui-dev/awesome-opus5-5-videos`. One animation per idea change, planned before rendering. The renderer is Playwright with Chromium or Brave. HeyGen's HyperFrames (Apache-2.0) can also render transparent MOV and WebM; it is an allowed alternative, not the default.
- **Integrated, not overlaid (11 Nov).** Matte the hosts with Apple Vision person segmentation (`editing/scripts/matte/` in the show repo). The layer order is plate, then motion, then the hosts on top.
- **Visible zones only (12 Nov).** The key element of each beat sits above the heads, on the centre seam, or at the edges. Measure how much of it the host matte covers. More than 15% means move or rescale it. If a beat cannot read behind the hosts, put it in front, clear of faces.
- **Motion from the first seconds (12 Nov).** No static opening.
- **No zoom or scale on the hosts.** Brand colours only: charcoal, white, red `#E83B3B`. Generated art has no text, no faces and no logos, and is logged in the episode's `assets/manifest.json` with prompt, tool, date and rights.
- **The Claude pixel mascot (11 to 12 Nov)** animates over the Claude jokes, kept off faces, in front of the matte when it interacts with a hand (track the fingertip).
- **B-roll** is planned at least once a minute of talking. Real screen captures stay still.

## Transition

The show transition is the red slash, tightened (13 Nov, option 1): 1920x1080, 60 fps, ProRes 4444 with alpha, 0.40 s, the picture hard-cuts at frame 10, with its whoosh embedded. Master: `~/content/brands/shipshitshow/_assets/transitions/stinger-standard.mov` (builder in `src/`). Used between chapters and idea changes; never recolored. It is the only fade-like exception to the hard-cuts rule, and picture cuts inside it stay hard.

## Outro and end screen

Built from the template in `~/content/brands/shipshitshow/_assets/outro/` (`src/build_outro.py --src <episode.mp4> --ss <goodbye start> --dur 12`). The goodbye footage eases from full screen into a framed panel on the brand backdrop; the real subscribe pill plays; the right column stays empty for YouTube end-screen elements; the canonical asterisk is small and top-right. Per episode, only the goodbye range changes.

## Audio

- **Music bed (12 Nov).** Real, rights-safe, instrumental, no vocals, no synthesized drone. Starts on the first frame with a quick fade-in, about 28 dB under the voices (about -42 LUFS-S under speech), ducked under speech, dropped out for the key lines, continuous across chapter boundaries, lifted slightly under the goodbye and end screen. Track: "On The Flip" (The Grey Room), YouTube Audio Library, attribution not required, downloaded 2026-11-12, file in `_assets/music/` with a `LICENSE.md`. The bed is the same on every episode until the owner changes it.
- **SFX.** Our own short UI sounds, one family: a soft whoosh on a beat's entry, a light tick or pop on key hits. About 4 dB below the first approved level, never over a word, no cartoon boings.
- **Split edits (J and L).** At turns and reactions the audio may lead or trail the picture by 0.3 to 0.8 s, with a few frames of audio crossfade. The picture stays a hard cut. Never mid-word, never to hide a changed claim, never into the transition. Used where it helps, not on every cut.
- **Cleanup.** High-pass at about 80 Hz; denoise only if the room floor needs it.
- **Voice.** After cleanup the voice is brought to a reference level measured from the recording itself, then compressed and de-essed, automatically, before the master. This is a default, not an owner decision: it was added on 14 Nov 2026 after the owner asked which editing steps were missing, and the values were set by meter and have not been confirmed by ear. The step and its values live in the show repo's chapter runner (`editing/scripts/chapters/`) and Shorts finalize step (`editing/scripts/shorts/finalize.py`).
- **Master.** About -14.5 LUFS integrated per chapter and true peak at or below -1.5 dBTP, by riding the voice, not the music.

## Captions

Sidecar SRT from the final timeline. Fix grammar, spelling and ASR names even where it no longer matches the voice word for word. Verify sync by re-transcribing the final audio; sample five words per piece, with the offset under 0.1 s. A coloured word must not change a claim's meaning.

## Shorts (9:16, 1080x1920)

The layout below is what the approved 261111 Short 01 v2 does (12 Nov). It replaces the 5 Nov "speaker fills the frame" layout.

| Element | Rule |
| --- | --- |
| Selection | One hot take or founder lesson. Never a feature walkthrough, product compliment or install demo (those can go to LinkedIn as they are). Host opinion stays phrased as opinion. A claim that belongs to a guest is held until they confirm it, with the reason in `HOLD.txt` |
| Open and length | The take is in the first 2 seconds, strongest line pulled forward. Clean held ending of about 0.7 s after the last word. 45 to 90 seconds (14 Nov; was under 60). First line makes sense to a stranger: never start on "and", "but", "because", "that's why", "so" or an "it" with no subject |
| Layout | Two hosts stacked, each filling a full half. No black band, no zoom, nobody cut in half. Captions on the middle seam. Animation sits off the seam, in a visible zone, at 15% matte coverage or less |
| Dynamics | Faster cuts than the video, more b-roll, mascot beats, the same SFX family and music bed at the same levels |
| Captions | Bold uppercase, 2 to 4 words per chunk, white with the spoken word in red `#E83B3B`, timed per word. No title text on the video. Never end a chunk on a weak word |
| Asterisk | The red master, unmodified, 120 px, centre x940 / y290. Never redrawn, moved or resized per Short |
| Technical | SAR 1:1 and DAR 9:16 on every export. Re-transcribe the final audio to check joins. -14 LUFS integrated, true peak at or below -1.5 dBTP (14 Nov; was -1) |
| Cover | Custom cover on every Short: host close-up looking at the viewer plus the subject person, the red asterisk (red is the rule on all Shorts covers, 13 Nov) at x880 / y345, 120 px. The expression matches the topic's mood (12 Nov). Real logos and real profile pictures only, never generated. Layout rules in [applications](applications.md) |
| Destination | Main channel. The clips channel is kept but not maintained. Every Short sets the full episode as its Related video and links it in the description once the episode is live |
| Order | A plan and one layout example before any batch is recut |

The edited-video asterisk is white on dark and black on light, from the exact masters, at the 16:9 row of [placement](placement.md). A recap is an edited video even when its footage came from a livestream. There is no persistent watermark over screen shares.

## Tweet and X copy

Decided by the owner on 14 Nov 2026.

- **Shape.** Open on the take. One real receipt from the episode: a real line, a number or the hosts' clash. The burned-caption copy of the video is attached.
- **Link.** The episode's YouTube link goes in the first reply, not in the tweet.
- **Three checks before it reaches the owner.** It quotes a real line, number or host clash from the episode. It leads with the opinion, not with how the video was made. It is short and blunt, in the owner's voice, and does not read as AI-written.
- **X copy.** The final video with captions burned in, at full quality. It is not recompressed or downscaled to fit a smaller upload size (owner, 13 Nov). Caption style is not specified yet (see known gaps).
- Nothing is posted or scheduled without the owner's OK on a card.

## Livestream scenes and broadcast

Faces, dialogue and readable demos take priority. Use the exact standalone six-arm asterisk and modest names. Livestream signatures are red. Use the canonical top-right token placement and [format-specific safe margins](thumbnail-safe-zones.md) for thumbnail and slate exports; verify broadcast camera, caption and UI placement in the actual scene. No extra dot, waves or boxed mark.

At 1920x1080, use the proportionally scaled 144x144 signature viewport at x1680 / y96 for a 1920x1080 thumbnail or slate, with equal 96 px top and right clearance and a narrow partner strip only when required. These are house starting values, not platform guarantees. Check the actual camera, caption and UI and screen readability; do not copy coordinates from a board.

| Scene | Composition | Check |
| --- | --- | --- |
| Two hosts | Balanced cameras, compact names and signature | Faces stay large; no oversized header |
| Solo | Camera fills useful frame | Labels avoid face and microphone |
| Screen share | Product dominates; small host cameras alongside | Real product text readable |
| Guests | Native layout for actual source count | All active people and names preserved |
| Starting / ending / break | Full name, approved still, concise state | No invented start time or countdown |
| Partner | Supported read or demo, one CTA | Approved logo, exact URL, accurate disclosure |

The first 30 seconds of a stream are a deliberate countdown before going live; remove it from the replay and the recap. A draft Restream kit (looping background, timer overlay, break and ending overlays, a slash transition clip, a 512 px red logo) is in `_assets/restream/`. Restream shows one overlay at a time with a manual Show and Hide, so a transition cannot fire on a scene change, and a video graphic plays without audio. Recheck [Restream graphics](https://support.restream.io/en/articles/8540835-add-graphics-to-your-stream-in-studio) before relying on it.

If company logos and URLs stay on air, use a narrow optically balanced strip and keep captions above it. Company names in a brief are not approved logo files. Do not put a large sponsor panel on every recap or Short. Private on-air concepts are not distributed. Build each scene from actual footage and editable layers.

## Files, handoff and housekeeping

Separate background, transparent overlay, mark, captions and audible media. A JPG cannot provide transparent camera windows. Never crop a board into a logo master or flatten an entire edit into one generated frame.

New motion needs frame rate, duration, codec, alpha, transition-point and playback receipts in its own manifest. Render success is not a watch-and-listen review.

Media lives only in `~/content` on the Mac Studio (episodes in `brands/shipshitshow/projects/`, shared assets in `brands/shipshitshow/_assets/`, experiments in `_labs/shipshitshow/`). One copy of everything; no archive or backup copies in other places. Thumbnail masters live on S3 under `masters/{livestreams,videos,shorts}/<id>/`. Native projects, recordings and large renders stay out of the repos. Clean up temp files, scratch clones and worktrees. Record kit revision, logo hash, fonts, caption style and approved deviations with the edit.

Vincent cannot play local files in the app: every render goes into the thread as a playable 720p copy (under 90 MB) or a private artifact, per chapter for the long video.

Follow [editing handoff](../production/editing-workflow.md), [overlay](https://github.com/shipshitshow/skills/tree/master/overlays), [dialogue](https://github.com/shipshitshow/skills/tree/master/dialogue), [recap](https://github.com/shipshitshow/skills/tree/master/recap) and [library](https://github.com/shipshitshow/skills/tree/master/library) contracts.

## Known gaps

- The chapter-by-chapter runner exists for plain cuts (`editing/scripts/chapters/` in the show repo: `plan`, `chapter <n>`, `all`, `stitch`; one 720p clip per chapter, only changed chapters re-render, stinger between chapters plus the outro). A chapter may carry an optional `motion` list in `chapters.json` (b-roll overlay or cut-away, mascot at a corner, layout switch to a named closeup or two-up, keyword pop in white or red); `plan` validates it against the rules on this page (overlaps, out-of-range times, missing assets, nothing over faces, the 5% safe margin, the asterisk box, the lower-third band, no zoom on people without the owner's approval on the layout) and chapters without it render as before. It does not yet do a host matte, J/L split edits, the music lift under the goodbye or independent caption sync; those still come from the per-episode plan scripts. Motion was checked on still frames of one 36 second slice of 261111 only: the animation (slide in and out, pop scale) was not watched and no audio was heard; the faces rects that keep overlays off the hosts are written by hand per layout, not detected. Only dry-run on 261111 so far, never listened to on a real episode.
- `tsrct` (Tesseract) is not installed on the Studio; the 261111 edit was built with ffmpeg and the scripts.
- The 261111 end-screen backdrop was never code; the template matches it by look, not by pixel.
- The Restream kit is a first draft and waits on the owner's check in Restream Studio.
- `editing/scripts/shorts/stacked.py` in the show repo now builds the stacked two-host Shorts layout (seam captions, red asterisk, hard cuts, `--still` check). Only one 25 second Short from 261111 was rendered with it, and nobody has listened to the audio. Its true peak after AAC measured -1.4 dBFS against the -1.5 dBTP rule (the `finalize.py` chain); that is open. It does not place animation or b-roll, and `build.py` there still builds the 261103 single-speaker layout.
- A take-picker exists (`editing/scripts/takes/pick.py` in the show repo): it scores the transcript with the `clips` rubric heuristics and writes ranked candidate Shorts with source ranges and a `segs` fragment for `short.json`. It reads text only, so it cannot judge delivery, does not map takes to the planned Short cards or report which planned Shorts were said, and has only been run on the 261111 transcript. The owner still picks the Shorts at the gate, after listening.
- A revisions log and a b-roll credits file exist (`editing/scripts/revisions/revlog.py` in the show repo): `add` appends a hash-chained record (source and output hashes, loudness, an EDL summary) to `out/revisions.jsonl` and renders `revisions.md`; `diff` compares two versions; `credits` writes `credits.md` from per-clip sidecars. A clip is credited only with a creator and a licence (or `original: true`), otherwise it prints as UNVERIFIED. The 261111 scratch run listed 9 b-roll clips, 0 credited, 9 UNVERIFIED, because no episode has sidecar metadata yet. The EDL reader is generic and has not been run against the trimmer's real output. The kit revision, logo hash, fonts and caption style are not recorded by the script, so that part of the rule above is still by hand.
- A package check and a dual render exist (`editing/scripts/package/check.py` and `editing/scripts/render/dual.py` in the show repo, PR 245). The check reports PASS, WARN or FAIL for the title (about 45 characters, Title Case, no [LIVE]), the tweet (link in the first reply, hashtags), five Shorts of 45 to 90 seconds, three thumbnails and the caption safe zones, and cites the rule for each; where the vault is silent it says so and invents no rule. It cannot judge whether a title or a tweet is good, and it does not check the three tweet checks (a real line, the opinion first, short and blunt). The render makes a clean YouTube copy and a burned-caption X copy from one master at full quality, with one shared audio encode at about -14 LUFS under a limiter. The X copy now has a house caption style (the Shorts style: karaoke white with a red active word when word timing exists, plain white from an SRT) and a landscape caption zone measured on the 261111 two-shot (faces end at about y650, name labels from y920, caption centred on y872, 96 px margin); the owner has not approved either, so they are starting values, not rules. Run on 261111 (a 30 second slice, source untouched): stills show captions in the zone and none in the clean copy, and the clean video stream is identical to the master; nobody has listened to either copy, the stacked and full caption renders were only dry-run, and the karaoke path was tried on synthetic word timing, not a real whisper file. The check flagged all five 261111 Shorts as 19 to 35 seconds against the 45 to 90 rule, and a tweet draft was never supplied, so the tweet checks were exercised on synthetic text only.
- A Short's Related video and its "Full episode" link are set by hand after publish.
- [Placement](placement.md) still shows the 5 Nov Short video layout next to the 12 Nov stacked layout on this page. A note there marks the superseded rows.
- The `clips` skill named at the top of this page lives in the show repo's `skills/`, not in the public skills repo linked above, and its layout section predates 12 Nov.

## Proposed, not decided

Nothing in this section is a rule. The [14 Nov editing automation audit](../_admin/docs/audits/2026-11-14/editing-automation-audit.md) holds the detail and records what the owner decided on 14 Nov.

- The owner's decision on the caption style and zone for the burned-caption X copy (a house default is built, see Known gaps).
- Automation for the next episode: matching picked takes to the planned Short cards, the rest of the chapter runner layers (host matte, J/L split edits, music lift, caption sync), a cut audit (now built: `editing/scripts/cutaudit/audit.py`, reports only, never applies its nudges, nobody has listened to a flagged join yet), a package check (now built: `editing/scripts/package/check.py`; it validates a package but does not generate title options, tweet drafts, descriptions or chapters).
- Ideas from the ForwardEditor study: one standing brief per episode, a syllable-to-waveform cut audit (built, see above), a privacy sweep before upload (now built: `editing/scripts/privacy/sweep.py`, review the flagged ranges before upload). (Versioned outputs with a revisions log and b-roll credits now exist, see Known gaps.)

## Change log

- 2026-11-13: merged `docs/show-prep/edit-style.md` and the earlier version of this page with the 11 to 13 Nov decisions: hosts first, Claude-built integrated motion, music bed, split edits, the stacked two-host Shorts layout, the goodbye and outro template, the standard transition, chapter gates, red asterisk on all Shorts covers, length by story.
- 2026-11-13: known gaps updated: a chapter-by-chapter runner now exists for plain cuts.
- 2026-11-14: no rule changed. Known gaps extended from the editing automation audit (Shorts builder, take-picking, title check, tweet and X copy, Related video, true peak mismatch, stale placement and skill references) and a "Proposed, not decided" section added that points to the audit.
- 2026-11-14: owner decisions locked. Shorts length is 45 to 90 seconds (was under 60). Shorts true peak is -1.5 dBTP (was -1). Tweet standard added: take first, one real receipt, burned-caption video attached, link in the first reply, three checks. Tweet and X copy added to the deliverables. The thumbnails row now points to the host-and-topic layout in applications (owner, 11 to 13 Nov). The 16:9 safe zone and no persistent corner watermark on screen shares are confirmed in placement. The radical-take prep steps are rules in show preparation.
- 2026-11-14: three owner rules from 13 and 14 Nov recorded. Titles are in Title Case (13 Nov). The X copy is full quality and is not shrunk to fit a smaller upload size (13 Nov). The thumbnail masters folder keeps only validated thumbnails (14 Nov, in applications).
- 2026-11-14: no rule changed. Known gap on the stacked Shorts builder updated: `stacked.py` exists in the show repo and is removed from the proposed automation list.
- 2026-11-14: colour rule added (owner, 14 Nov): every recording is measured and colour-corrected automatically from its own footage before the recap and the Shorts are cut, with no fixed look. The step is `editing/scripts/grade/` in the show repo.
- 2026-11-14: no rule changed. Audio section notes a new default: the voice is levelled from its own measured loudness, compressed and de-essed automatically before the master. It is not an owner decision yet; the values were set by meter and wait on the owner's ear.
- 2026-11-14: no rule changed. Known gaps updated: a transcript take-picker now exists in the show repo (`editing/scripts/takes/`). It ranks candidates by the `clips` rubric; the 45 to 90 second length rule and the owner's pick are unchanged.
- 2026-11-14: no rule changed. Known gaps updated: a revisions log and a b-roll credits file now exist in the show repo (`editing/scripts/revisions/`) and are removed from the proposed automation list. Nothing is credited until a clip has a creator and licence recorded.
- 2026-11-14: no rule changed. Known gaps updated: the chapter runner now has an optional per-chapter motion layer (b-roll, mascot, layouts, keyword pops) in the show repo (`editing/scripts/chapters/`). It enforces the hard cuts, no-zoom, safe-zone and 80 percent hosts rules by validation; the animation has not been watched.
- 2026-11-14: no rule changed. Known gaps updated: a package check (`editing/scripts/package/`) and a dual render (`editing/scripts/render/`) now exist in the show repo. The title length and Title Case check and the X copy build are no longer open; the X copy caption style and the landscape caption zone are house defaults awaiting the owner. The link-in-the-first-reply rule is enforced as written.
