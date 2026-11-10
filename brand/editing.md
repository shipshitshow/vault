# Editing, captions and broadcast

These are the edit rules for Ship Sh*t Show recaps, edited videos and Shorts, and the broadcast scene rules. The edit rules are the owner's locked decisions of 3 to 5 November 2026 (Vincent), taken from the 261103 recap and Shorts. The show repo keeps the build values and scripts in `docs/show-prep/edit-style.md` ([source](https://github.com/shipshitshow/show.shipshit.dev/blob/master/docs/show-prep/edit-style.md)); this page and that one carry the same rules and must not disagree. Change a rule only when the owner asks, and change both.

Use [identity](identity.md), [tokens](tokens.json), [placement](placement.md) and [inventory](inventory.json) with the actual recording/project. This kit does not replace the selected editor, streaming tool or an existing approved motion project.

## Recaps and edited videos (16:9)

- **No text cards.** No title cards and no topic-label cards between segments, and no topic label on screen. Mark an idea change with b-roll, a real screenshot or the show's existing red slash-stinger wipe.
- **Hard cuts only.** No fade to black, no dissolves, no alpha fades on overlays. The slash-stinger is the one exception, and it is the approved existing one; do not recolor or replace it.
- **No zoom on people.** No zoom or push-in on the hosts. Zoom on screen content only when it lands on a specific point.
- **Open strong, then talk.** Start with the strongest 15 to 20 seconds of the conversation as a cold open (the 5 November 2026 recap is the model), then 30 to 45 seconds of proper 50/50 two-person conversation before any screenshare. The cold open must flow into the conversation, not read as a trailer. No subscribe ask before the first payoff and no blooper in the first 20 seconds.
- **Default layout is 50/50.** Screenshare only while something is shown. Product UI stays readable.
- **B-roll at least every minute.** Never let more than about a minute of talking pass without it. Full-frame is fine. For the show, b-roll is an animated SVG made with Codex CLI, one per idea change, planned before rendering. Not static images with a push-in. Real screen captures stay still.
- **Generated art** has no text, no faces and no brand logos, uses charcoal with a muted red, and is logged in the episode's `assets/manifest.json` with prompt, tool, date and rights. A real logo or screenshot comes from a supplied file. Detailed generated illustration explains an actual spoken beat; it does not replace real people or facts.
- **Dialogue is cut for the viewer.** Drop back-channels ("yeah", "exactly", "mhm") and restarts. Keep a reaction that moves the story and every qualification or opposing view that changes the answer.
- **Show before rendering.** Send Vincent the edit plan and transcript first, and one sample before cutting a batch. Render success is not a watch/listen review.

The edited-video asterisk is white on dark and black on light, from the exact masters, at the 16:9 row of [placement](placement.md). A recap is an edited video even when its footage came from a livestream. There is no persistent watermark over screen shares.

## Shorts (9:16)

Locked on 5 November 2026. Reference values for 1080×1920; the asterisk values come from [placement](placement.md).

| Element | Rule |
| --- | --- |
| Frame | The speaker fills the whole frame: a static crop of their cam, face centred. No blur, centred tile or bars. When two people speak, cut between their crops on the speaker turn; never move the crop. No zoom or punch-in |
| Title | No title text on the video |
| Asterisk | The red master, unmodified, 120 px, centre x940 / y290. Never redrawn, moved or resized per Short. If it hides the subject, move the crop, not the mark |
| Captions | Bold uppercase, 2 to 4 words per chunk, about y1480, white with the spoken word in red `#E83B3B`, thin dark outline and no box. Timed per word and snapped to real pauses. Never all red or all white. Nothing below y≈1570 |
| Caption text | Fix grammar, spelling and ASR names (Grok, Claude, PHP, Cloudflare) even where it no longer matches the voice word for word. Never end a chunk on a weak word ("the", "a", "to") |
| B-roll | 2 to 3 hard-cut cutaways of 2 to 3 seconds on the lines they illustrate, built or cropped for 9:16 with the subject centred. Captions and asterisk stay on top |
| Open | The take is in the first 2 seconds. Pull the strongest line forward when it sits later in the segment |
| First line | Must make sense to a stranger. If it starts with "and", "but", "because", "that's why", "so" or an "it" with no subject, pull a later line forward or pick another range |
| Length | No fixed length: the take decides, under 60 seconds. Prefer the shortest cut that keeps the take; on the channel, Shorts of 60 words or fewer did better (a correlation on a small channel) |
| Audio | Cuts in silence, 15 to 20 ms audio fades at joins only, no video fades. Two-pass loudnorm to -14 LUFS integrated, true peak at or below -1 dBTP |
| Cover | Custom cover on every Short, red asterisk per [placement](placement.md), no host faces. It shows the subject of the take, and the covers of one batch differ in colour so they can be told apart. Art direction follows the thumbnail rules |
| Destination | Shorts publish on the main channel. The clips channel is kept but not maintained. Every Short sets the full episode as its YouTube Related video and links it in the description once the episode is live |

Pick takes that give the viewer a founder lesson or a hot take, never a feature walkthrough, a product compliment or an install demo; those can go to LinkedIn as they are. Keep a host's opinion phrased as opinion.

## Livestream scenes and broadcast

Faces, dialogue and readable demos take priority. Use the exact standalone six-arm asterisk and modest names. Livestream signatures are red. Use the canonical top-right token placement and [format-specific safe margins](thumbnail-safe-zones.md) for thumbnail/slate exports; verify broadcast camera/caption/UI placement in the actual scene. No extra dot, waves or boxed mark.

At 1920×1080, use the proportionally scaled 144×144 signature viewport at x1680/y96 for a 1920×1080 thumbnail/slate, with equal 96px top/right clearance and a narrow partner strip only when required. These are house starting values, not platform guarantees. Check the actual camera/caption/UI and screen readability; do not copy coordinates from a board.

| Scene | Composition | Check |
| --- | --- | --- |
| Two hosts | Balanced cameras, compact names and signature | Faces stay large; no oversized header |
| Solo | Camera fills useful frame | Labels avoid face/microphone |
| Screen share | Product dominates; small host cameras alongside | Real product text readable |
| Guests | Native layout for actual source count | All active people/names preserved |
| Starting / ending / break | Full name, approved still, concise state | No invented start time/countdown |
| Partner | Supported read/demo, one CTA | Approved logo, exact URL, accurate disclosure |

The first 30 seconds of a stream are a deliberate countdown before going live; remove it from the replay and the recap.

If company logos and URLs stay on air, use a narrow optically balanced strip and keep captions above it. Company names in a brief are not approved logo files. Do not put a large sponsor panel on every recap/Short.

Private on-air concepts are not distributed. Build each scene from actual footage and editable layers; implement and check company-strip placement separately for every scene.

## Captions and motion

Keep typography and shapes native and editable. Captions use the final timeline; verify names, numbers, qualifications and sync against the recording. The word-by-word red highlight is the locked Shorts caption style above. A colored word must not change a claim's meaning.

Use brief purposeful motion with legible holds. Avoid constant movement, excessive glitching/flashing and intros that delay the useful opening.

New motion needs frame rate, duration, codec, alpha, transition-point and playback receipts in its own manifest. Render success is not a watch/listen review.

## Files and editor handoff

Separate background, transparent overlay, mark, captions and audible media. A JPG cannot provide transparent camera windows. Never crop a board into a logo master or flatten an entire edit into one generated frame.

Use native OBS/Restream layouts/names when practical. Test exact placement in the chosen canvas. Restream graphics do not play embedded audio; an audible intro needs the appropriate media source. Recheck [graphics guidance](https://support.restream.io/en/articles/8540835-add-graphics-to-your-stream-in-studio).

Native projects, recordings and large renders stay in the media library. Record kit revision, logo hash, fonts, caption style and approved deviations with the edit. Follow [editing handoff](../production/editing-workflow.md), [overlay](https://github.com/shipshitshow/skills/tree/master/overlays), [dialogue](https://github.com/shipshitshow/skills/tree/master/dialogue) and [recap](https://github.com/shipshitshow/skills/tree/master/recap) contracts.
