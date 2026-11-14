# Editing, captions and broadcast

This is the one source of the edit rules for Ship Sh*t Show recaps, edited videos and Shorts, and for the broadcast scenes. It is the owner's decisions (Vincent), 3 to 13 November 2026, taken from the 261103 recap and the 261111 recap and Shorts. The show repo keeps only build values and script names in `docs/show-prep/edit-style.md` ([source](https://github.com/shipshitshow/show.shipshit.dev/blob/master/docs/show-prep/edit-style.md)) and points here. If the two disagree, this page wins.

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
| 5 Shorts | 9:16, under 60 s each, with covers, titles and descriptions |
| Title | About 45 characters at most, short and radical. No "[LIVE]" |
| Thumbnails | The thumbnails thread owns the art direction. Not part of this process |
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
12. **Package.** Title, description, chapters, tags, Shorts copy.
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
- **Master.** About -14.5 LUFS integrated per chapter and true peak at or below -1.5 dBTP, by riding the voice, not the music.

## Captions

Sidecar SRT from the final timeline. Fix grammar, spelling and ASR names even where it no longer matches the voice word for word. Verify sync by re-transcribing the final audio; sample five words per piece, with the offset under 0.1 s. A coloured word must not change a claim's meaning.

## Shorts (9:16, 1080x1920)

The layout below is what the approved 261111 Short 01 v2 does (12 Nov). It replaces the 5 Nov "speaker fills the frame" layout.

| Element | Rule |
| --- | --- |
| Selection | One hot take or founder lesson. Never a feature walkthrough, product compliment or install demo (those can go to LinkedIn as they are). Host opinion stays phrased as opinion. A claim that belongs to a guest is held until they confirm it, with the reason in `HOLD.txt` |
| Open and length | The take is in the first 2 seconds, strongest line pulled forward. Clean held ending of about 0.7 s after the last word. No fixed length, under 60 seconds. First line makes sense to a stranger: never start on "and", "but", "because", "that's why", "so" or an "it" with no subject |
| Layout | Two hosts stacked, each filling a full half. No black band, no zoom, nobody cut in half. Captions on the middle seam. Animation sits off the seam, in a visible zone, at 15% matte coverage or less |
| Dynamics | Faster cuts than the video, more b-roll, mascot beats, the same SFX family and music bed at the same levels |
| Captions | Bold uppercase, 2 to 4 words per chunk, white with the spoken word in red `#E83B3B`, timed per word. No title text on the video. Never end a chunk on a weak word |
| Asterisk | The red master, unmodified, 120 px, centre x940 / y290. Never redrawn, moved or resized per Short |
| Technical | SAR 1:1 and DAR 9:16 on every export. Re-transcribe the final audio to check joins. -14 LUFS integrated, true peak at or below -1 dBTP |
| Cover | Custom cover on every Short: host close-up looking at the viewer plus the subject person, the red asterisk (red is the rule on all Shorts covers, 13 Nov) at x880 / y345, 120 px. Real logos and real profile pictures only, never generated. The thumbnails thread owns the template |
| Destination | Main channel. The clips channel is kept but not maintained. Every Short sets the full episode as its Related video and links it in the description once the episode is live |
| Order | A plan and one layout example before any batch is recut |

The edited-video asterisk is white on dark and black on light, from the exact masters, at the 16:9 row of [placement](placement.md). A recap is an edited video even when its footage came from a livestream. There is no persistent watermark over screen shares.

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

- The chapter-by-chapter runner exists for plain cuts (`editing/scripts/chapters/` in the show repo: `plan`, `chapter <n>`, `all`, `stitch`; one 720p clip per chapter, only changed chapters re-render, stinger between chapters plus the outro). It does not yet do matte, b-roll or mascot layers, J/L split edits, the music lift under the goodbye or independent caption sync; those still come from the per-episode plan scripts. Only dry-run on 261111 so far, never listened to on a real episode.
- `tsrct` (Tesseract) is not installed on the Studio; the 261111 edit was built with ffmpeg and the scripts.
- The 261111 end-screen backdrop was never code; the template matches it by look, not by pixel.
- The Restream kit is a first draft and waits on the owner's check in Restream Studio.
- No tracked script builds the stacked two-host Shorts layout. `editing/scripts/shorts/` in the show repo still builds the 261103 single-speaker layout; the approved 261111 Short 01 v2 came from per-episode scripts.
- Take-picking is done by reading the transcript in a session with the `clips` rubric. No script scores the transcript or writes the ranked Gate 3 plan.
- Nothing checks the title automatically. Two of the three 261111 title options were 50 characters against "about 45 at most".
- The 261111 package also shipped a tweet and a burned-caption X copy of the video. Neither is in the deliverables table and neither has a spec on this page.
- A Short's Related video and its "Full episode" link are set by hand after publish.
- The Shorts table says true peak at or below -1 dBTP; the Shorts scripts and the recap master use -1.5 dBTP. Waits on the owner.
- [Placement](placement.md) still shows the 5 Nov Short video layout next to the 12 Nov stacked layout on this page. A note there marks the superseded rows.
- The `clips` skill named at the top of this page lives in the show repo's `skills/`, not in the public skills repo linked above, and its layout section predates 12 Nov.

## Proposed, not decided

Nothing in this section is a rule. The [14 Nov editing automation audit](../_admin/docs/audits/2026-11-14/editing-automation-audit.md) holds the detail and the list of decisions for the owner.

- A standard for the tweet and the burned-caption X copy.
- Title Case and an automatic length check for titles.
- Radical-take prep: a headline-shaped verdict per host, provocation questions and a headline cue at each segment close.
- Automation for the next episode: take-picking from the transcript, a stacked Shorts builder, chapter runner layers, a cut audit, a package generator with checks.
- Ideas from the ForwardEditor study: one standing brief per episode, a syllable-to-waveform cut audit, versioned outputs with a revisions log, a privacy sweep before upload.

## Change log

- 2026-11-13: merged `docs/show-prep/edit-style.md` and the earlier version of this page with the 11 to 13 Nov decisions: hosts first, Claude-built integrated motion, music bed, split edits, the stacked two-host Shorts layout, the goodbye and outro template, the standard transition, chapter gates, red asterisk on all Shorts covers, length by story.
- 2026-11-13: known gaps updated: a chapter-by-chapter runner now exists for plain cuts.
- 2026-11-14: no rule changed. Known gaps extended from the editing automation audit (Shorts builder, take-picking, title check, tweet and X copy, Related video, true peak mismatch, stale placement and skill references) and a "Proposed, not decided" section added that points to the audit.
