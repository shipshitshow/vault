# Ship Sh!t Show — project and production audit

Audited: 2026-10-02. Status: findings and proposed design, before implementation.

The show has useful material and an operational Tesseract editing workspace. The main gaps are stale public guidance, an incomplete public archive, and preparation that asks the hosts to read scripts instead of organizing the sources they actually use.

This audit covers the local show, skills and vault repositories; GitHub's `shipshitshow` organization; the retired Premiere checkout and its newer remote history; the Studio media libraries; September 1, 8 and 29 livestream transcripts; and the September 29 edited video published October 1. It also checks current platform documentation. Transcript observations are approximate ASR timestamps, not a playback or listening review. Model names, prices and capabilities mentioned in the recordings are historical speaker claims, not independently verified product facts.

## Decisions already supplied

- `send.shipshit.dev` replaces `live.shipshit.dev`, per Vincent. Documentation should reflect that decision.
- Premiere is retired from the editing workflow. Editing uses Tesseract through GPT/Claude and its plugin.
- Example code should be public after a publication audit and attached to its livestream.
- Skills should be usable by viewers, including metadata, three thumbnail test variants, PFP/banner, Restream layouts and partner ad scripts.
- Hosts use the Ressources links and discuss them naturally. Reading a talking-points script is not the intended workflow.
- A demo is desirable, but model usage has prevented it. Audit the existing folders before changing the editing architecture.

## Repository and documentation state

| Repository | Observed state | Required follow-up |
| --- | --- | --- |
| `show.shipshit.dev` | Public; active October 1. Local origin still uses the old `live.git` URL. README and some memory retain the old domain. | Update canonical domain and repository links; reconcile public skills with app guidance. |
| `skills` | Public; last push April 15. Four skills, with April channel snapshots and scripted preparation. | Create one maintained viewer skill pack with an optional Ship Sh!t Show profile. |
| `vault` | Public; last push April 15. Nine streams, nine videos, 29 Shorts. | Import available transcripts, record gaps, and document production and examples. |
| `premiere` | Public and still unarchived. Remote master is newer than the retired local checkout; open documentation PR #14. | Preserve local work, document retirement and resolve the open PR before archival. |
| `opus48` | Public; three standalone demonstrations linked from the root README to a YouTube episode. | Consolidate into an episode-indexed examples repository after license and asset review. |
| `opensoraxyz` | Private. GitHub main contains workflow scaffolding, while the Studio has the application history. | Audit the actual Studio code before publishing a curated copy. |
| `.github` | Public org profile links an absent `youtube` repository and presents Premiere as current. | Link the maintained site, vault, skills and examples after they exist. |

No `examples` repository currently exists. Skills and vault have no GitHub Actions workflows. The app's graph was built before the current checkout and uses old paths, so filesystem evidence was used where graph coverage was stale.

The reported domain migration is accepted as the intended state. A host TLS request to `send.shipshit.dev` failed during this audit; that is insufficient evidence to judge the deployment. `show.shipshit.dev` returned HTTP 200. Confirm the intended public links before publishing documentation updates.

Existing user changes were preserved: Obsidian settings and a deleted tracked Python cache in vault; untracked `.DS_Store` files in skills; and changes in the retired Premiere checkout. Scoped branches were created, but no workflow implementation, repository publication, media relocation or archival was performed.

## Public transcript coverage

The adjacent [coverage ledger](transcript-coverage.csv) records YouTube IDs, observed visibility, existing vault notes and located transcript sources. It deliberately omits mutable view counts and does not infer that an upload was deleted simply because it is absent from a public tab.

| Catalog | Known uploads | Already in vault | Missing from vault |
| --- | ---: | ---: | ---: |
| Main channel: historical July inventory plus current public streams/videos | 53 | 18 | 35 |
| Clips channel: current public Shorts tab | 91 | 29 | 62 |
| Total known catalog | 144 | 47 | 97 |

These are a lower bound on all uploads: current public tabs cannot enumerate inaccessible or unlisted uploads. Twenty-six July inventory entries were not observed in the current main-channel tabs; their visibility remains unresolved.

All 47 existing vault entries have nonempty, Git-tracked transcript files. The app contains 43 usable clean transcripts and their raw VTT files for its 44-entry July inventory. The missing inventory transcript is `b9Re90K4By8`. Three additional clean files in the app belong to other creators' benchmark videos and must not become Ship Sh!t Show episodes.

Four additional main-channel transcripts were located on the Studio:

| YouTube ID | Located source | Meaning |
| --- | --- | --- |
| `LbCRcGRLYaU` | September 1 Premiere source transcript JSON | Full livestream clock |
| `KPAyE6KSrQU` | September 8 Premiere source transcript JSON | Full livestream clock |
| `uSuqoiEaB1k` | September 29 Tesseract `raws/transcript.md` | Full livestream clock |
| `WOTzkAWvb0w` | September 29 Tesseract `final/transcript.md` | Edited video clock; published October 1 |

There are 47 located main-channel transcripts across the app and Studio. Of the 97 missing vault entries, 29 have a located transcript ready for an import and provenance review; 68 do not yet have a transcript located. The ledger's availability status does not mean the ASR has been corrected.

The current app refresh script adds uploads newer than its newest existing item and preserves curated historical exclusions. It is not an all-upload archive synchronizer and does not cover the Clips channel. Its YouTube API request hit an IP restriction from this host. Public tab enumeration succeeded, but caption requests for the four recent recordings returned HTTP 429. Those endpoints were not repeatedly retried; local transcripts supplied the audit evidence.

Proposed archive contract:

1. Use channel ID plus YouTube ID as identity, with separate recording and publication dates.
2. Preserve raw ASR, normalized readable text, timestamped captions and provenance. Record corrections without silently rewriting what was said.
3. Keep source, edited recap and each Short on their own clocks. Attach source-to-edit cut maps where available.
4. Link every derivative and example back to the source livestream. Keep unresolved mappings explicit.
5. Track missing captions and visibility in a durable ledger. Never substitute a description or invented summary for a transcript.
6. Publish text, manifests and links in GitHub; retain recordings, native project packages and large renders in the media library.

Keep existing vault links working. Retain `Livestreams`, `Videos` and `shipshitshowclips/Shorts`; add ID-based identity to metadata and handle same-date collisions explicitly rather than moving all historical notes during the first import.

## What the shows actually do

### September 29 — comparison delayed behind chronology

Source: [full livestream](https://www.youtube.com/watch?v=uSuqoiEaB1k). The source recording lasts about 48½ minutes.

| Approximate time | Observed progression |
| --- | --- |
| 0:00–0:33 | Music |
| 0:33–2:03 | Greetings, YouTube/audio checks, setup |
| 2:03–3:05 | Chronological model order; viewer asked to stay until the end for the answer |
| 3:05–10:36 | Model pricing, subscription limits, resets and speculation |
| 10:36–14:00 | Other model/company tangents |
| 14:00–23:32 | Grok and agent/workflow stories; useful firsthand material around 20:01 |
| 23:32 onward | Main Opus/Sonnet comparison finally starts |
| Around 35:00–42:00 | Prompting, completion checks, effort versus iteration and motion examples |
| 45:02–47:31 | Different host conclusions: implementation/review routing versus keeping the existing model mid-project |

The disagreement and operator experience are strengths. The answer promised by the comparison packaging arrives late. The 11:38 edited version moves the verdict earlier and concentrates that material. This is evidence about structure, not proof that structure caused low views.

### September 8 — useful practical stories mixed with live searching

Source: [full livestream](https://www.youtube.com/watch?v=KPAyE6KSrQU). Around 3:29 the hosts search for dates/tweets; around 6:39–8:17 they work through a puzzle live. Practical editing/computer-use discussion begins around 10:17. Later workflow savings around 34:02 and integration/business discussion around 39:38–43:16 provide clearer viewer applications. Strong preparation should make those useful examples easier to reach and put the timeline evidence within reach before going live.

### September 1 — the demo failure was foreseeable

Source: [full livestream](https://www.youtube.com/watch?v=LbCRcGRLYaU). Both hosts discuss exhausted usage from around 0:47. They discuss reset timing before the show and perform sound/image checks around 4:28. The demo is deferred around 50:14, with a suggestion to record it later around 50:44. The closing also acknowledges the opening tangent. A demo slot needs a prepared fallback or a usage reservation; writing a demo into a script does not provide one.

### Proposed preparation format

Use one clear viewer question as the episode spine. Present the problem and preliminary answer early, then use model chronology only where it explains the decision. Prepare three to five source clusters, each containing:

- A question the hosts can answer naturally.
- Primary evidence and the relevant X link, with the important passage already located.
- One firsthand example, uncertainty or disagreement to explore.
- The practical decision or consequence for the viewer.
- A rough time budget and an exit cue, plus a parking area for tangents.

This is a source board for Ressources, not prose to read aloud. Do not manufacture clip lines, require a publishable artifact every week, or force every news item into an artificial build episode. In the current app, source headings can be displayed in Ressources without first changing the UI; verify the exact output against the renderer when implementing.

A pilot could put the viewer promise within roughly 30 seconds and bring the principal proof into the first segment. Those timings are editorial hypotheses, not platform guarantees. A short recorded/local demonstration is the recommended fallback when quotas are unavailable. Live demonstrations should have a prechecked account, fixture, expected result, time limit and recovery plan.

YouTube recommends checking whether the opening delivers the title/thumbnail promise, moving compelling later moments earlier, and examining retention dips and spikes. This supports testing the opening and order rather than scripting every sentence. [YouTube retention guidance](https://support.google.com/youtube/answer/9314415?hl=en)

Spotify's creator guidance supports a repeatable format and comparing episodes of similar formats and lengths. Its performance guidance also identifies ads, tangents and technical quality as things to inspect around drop-offs. These are diagnostic prompts, not a diagnosis of this channel. [Video podcast formats](https://creators.spotify.com/resources/create/video-podcast-examples), [episode performance](https://creators.spotify.com/resources/grow/understanding-your-episode-performance)

Before claiming an improvement, compare like-for-like live and on-demand performance: opening retention, segment dips, average view duration, concurrent viewers and return viewers; inspect impressions, CTR and traffic sources for packaging. Public cumulative views alone cannot establish why a show underperformed. YouTube provides live-stream metrics and post-stream retention. [Live metrics](https://support.google.com/youtube/answer/2853833/see-your-live-stream-s-metrics?hl=en-GB)

## Skills: conflicting and stale guidance

| Existing surface | Finding | Proposed correction |
| --- | --- | --- |
| Public `talking-points` | Scripted intro, sections, quotations and clip lines; hosts do not read it. | Source board, episode question, evidence and segment exits. |
| App talking-points skill | Long build-first contract, forced artifacts/capsules and obsolete model examples. Some live-reaction guidance conflicts with its mandatory structure. | Align with the actual show and the public canonical skill. |
| Public `youtube-metadata` | April view-count ranking labels winners/losers; analyzer includes videos/Shorts but excludes livestreams. | Use the actual transcript and current channel examples. Distinguish live, recap and Short. Treat historical patterns as descriptive, not causal. |
| Public `thumbnail-prompt-variations` | Four to six variants, rigid two-host composition and old palette. | Exactly three purposeful test candidates; preserve host identity and separate live/recap/Short formats. |
| Public trend research | Requires every platform and carries old conflict/hype framing. | Relevant X resources plus primary evidence; select sources by usefulness, not a platform quota. |
| App metadata/thumbnails | More recent transcript and identity rules, but differ from public skills. | Preserve useful rules in one maintained profile; use thin app adapters. |
| Studio Tesseract helper skills | Four useful local helpers with machine-specific paths and some stale examples. | Adapt project, recap and dialogue recipes for viewers; delegate actual editing mechanics to the official plugin. |

Proposed public pack:

| Skill | Reviewable output |
| --- | --- |
| Show preparation / replacement talking-points | Source board, segment order, demo/fallback plan and host cue sheet |
| Channel-fit research | Shortlist with primary evidence, relevance and uncertainties |
| YouTube metadata | Titles, description, chapters, tag list and source links, grounded in the actual asset |
| Thumbnail variations | Exactly three distinct hypotheses, prompts and evaluation plan |
| Channel branding | PFP and banner prompts, editable/export assets, crop previews and identity checks |
| Restream layouts | Scene plan, backgrounds, transparent overlays, logo and live preview checks |
| Partner ad script | Host-read script, substantiated claims, disclosure, CTA and placement variants |
| Transcript archive | Coverage reconciliation, source/edited clocks, correction provenance and episode links |
| Tesseract project workflow | Folder initialization, manifests, versions and promotion |
| Tesseract recap | Edit brief, cuts, source/edited transcripts, chapters and export review |
| Tesseract dialogue | Conditional audio recipe, sync checks and listening review |

Each skill should work with a viewer's channel profile. Ship Sh!t Show's voice, host photos, links and approved branding should be optional reference material rather than hardcoded personal folders. Do not duplicate the Tesseract plugin's changing schema or promise actions its tools do not support.

YouTube currently supports up to three title/thumbnail test candidates and judges results by watch time. Eligible long-form uploads and completed live archives can be tested; scheduled lives and Shorts cannot. Inconclusive results are possible. Use three deliberate hypotheses, and avoid interpreting a tiny CTR difference as a proven winner. [YouTube A/B tests](https://support.google.com/youtube/answer/16391400?hl=en)

## Studio folders and editing state

### Preserve the Premiere library

The existing Studio library is under `~/DeCod3rs`:

```text
DeCod3rs/
  _raws/2609/{260901,260908,260929}.mp4
  assets/assets.db
  2026/Pr/2609/<episode>/
    <episode> - livestream.prproj
    source transcripts, assets, autosaves and previews
    shorts/<short>/vertical/ and 16x9/
  2026/finals/2609/<episode>/
    YouTube/X exports and transcript JSON
```

September 8 includes three prepared Shorts in portrait and landscape, with captions and edit plans. Its recorded status says they were not exported or fully reviewed. Premiere's referenced captions/assets and autosaves should stay in place; moving them to make folders look tidier can break project links.

### Adopt and document the existing Tesseract structure

Yesterday's work is in `~/www/tesseract/projects/260929`. The workspace is intentionally local and is not a Git repository. Its local instructions prohibit initializing/publishing the whole workspace as organization code.

```text
tesseract/
  assets/{pfps,logos,...}/
  scripts/workspace.py
  projects/260929/
    project.json
    raws/
      livestream.mp4
      transcript.{txt,md,srt,vtt}
    assets/audio/
    outputs/
      video.mp4, project.tsrct
      previews/, work/
      shorts/
        working/, work/, previews/, assets/, pilot/
        versions/vNNN/
        final/<short-slug>/
          video.mp4, project.tsrct
          landscape/{video.mp4,project.tsrct}
          transcript.txt, captions.srt, cuts.csv
          title.txt, linkedin.txt, twitter.txt, post.txt
          cover.jpg, manifest.json
    versions/{v001,v002,v003,broad-draft}/
    final/
      video.mp4, project.tsrct
      transcript.{txt,md,srt,vtt}
      cuts.{csv,md}, description-context.md
      audio-treatment.md, manifest.json
  _labs/
    branding and motion experiments
```

This tree is the observed arrangement, not a migration performed by this audit. A future contract should define which working export is authoritative, what creates a version, and what qualifies for promotion to `final`. A manifest should hold identity, recording date, published derivatives, media references, tool version, hashes and verification state. Keep the existing episode date key; add a slug if another recording on the same day would collide.

Fresh `workspace.py audit --project 260929` checked 62 native archives and three manifests with no reported errors. Fresh `ffprobe` confirmed the long final: 698.400 seconds, 1920×1080, 30 fps, H.264, stereo AAC at 48 kHz, and a subtitle stream. Five current Shorts have portrait and landscape exports recorded in their manifests. These checks establish structure/technical metadata, not full playback or subjective quality.

The project uses about 37 GB, including roughly 11 GB of long-form versions and 12 GB of Shorts. Native archives embed media; the final native project alone is about 3.4 GB. Sixty-two archives are a storage-policy signal, not authorization to delete versions. Recommend snapshots at meaningful milestones and a reviewed retention policy after the authoritative deliverables are defined.

The installed Studio `tsrct` reports 0.3.0 while the plugin/runtime version file specifies 0.3.1. Resolve the mismatch deliberately before the next edit; do not upgrade or rerender during an audit. The root README and helper examples have stale project/branding paths after moves into `_labs`.

Audio treatment and a timing correction are recorded in the existing manifests/recipes. Some mastering happens outside the native project. Keep those recipes with the final export so reopening `.tsrct` does not silently imply an identical render. Do not turn one recording's sample offset or EQ settings into universal defaults. Prior notes explicitly lacked an audio audition; word joins and subjective dialogue quality need an actual listening review.

SSH could read these libraries, but access to the Studio Desktop was denied by macOS privacy controls. No bypass was attempted. Desktop thumbnail exports were therefore not visually audited.

### Proposed division of responsibility

| Location | Owns |
| --- | --- |
| Local Studio Tesseract workspace | Source recordings, native projects, shared media, working renders, version snapshots and final media |
| Vault GitHub repository | Public transcripts, episode relationships, sources, metadata, production documentation and coverage ledger |
| Skills GitHub repository | Reusable viewer instructions and configurable channel/brand references |
| `shipshitshow/examples` | Public runnable demonstrations and prompt/experiment examples, indexed by source livestream |
| Show application | Producer display and publication UI, consuming the maintained contracts |

Do not put multi-gigabyte projects into vault or examples. Avoid copying the same recordings into each repository. Legacy Premiere remains a preserved source library until media references, transcripts and any needed deliverables have been reconciled.

## Branding, Restream and partners

The Studio already contains a newer Ship Sh!t Show direction: photographic indie rock'n'roll, red/black/warm ivory, grain/gig-poster energy, real hosts at computers and a build/check/ship/improve story. The exact show name is **Ship Sh!t Show**, with no final exclamation mark. Earlier illustrated/cube concepts were rejected. The newer approved direction should inform the channel profile instead of reviving April thumbnail defaults.

Production experiments under `_labs` remain drafts. The observed motion preview is 852×480 at 24 fps, and the final folder is empty. Do not label those as a completed broadcast package. The existing brief describes short transitions and a bump after the spoken hook; these are starting concepts, not mandatory timings for every show.

The branding skill should produce separate PFP and banner assets, use supplied identity references, preview the circular crop and responsive banner crops, and record export dimensions and sizes. YouTube recommends a 2560×1440 banner, requires at least 2048×1152, and specifies a 1235×338 text/logo safe area at that minimum size; banner files must be at most 6 MB. Profile pictures render at 98×98 and have a 15 MB limit. Recheck the platform requirements when generating. [YouTube branding specifications](https://support.google.com/youtube/answer/10456525?hl=en)

The Restream skill should define camera, discussion, browser/screen demo, partner and closing scenes, then generate only the needed assets. Native controls remain native controls. Review camera windows, screen legibility, name labels and caption clearance in Studio. Restream recommends 1920×1080 overlays/backgrounds and 512×512 logos; custom graphics require a paid plan. Uploaded video graphics do not play audio, so an audible intro needs the appropriate clip/media path. [Restream graphics](https://support.restream.io/en/articles/8540835-add-graphics-to-your-stream-in-studio)

The partner skill should request the offer, audience, evidence for claims, relationship, actual host experience, CTA and length. Create a natural host-read draft with an explicit disclosure and a clean return to the episode. Never invent personal endorsement or unsupported results. YouTube requires branded-content disclosure in Studio and clear disclosure to viewers; the skill must recheck current policy and the relevant market before publication. [YouTube branded content policy](https://support.google.com/youtube/answer/17596007?hl=en)

## Premiere: latest remote state matters

The retired local checkout is at `f113dff`, eight commits behind remote master `30ef8523ec1be340f48852842c66af89beeb942c`. It has local modifications. Do not reset or treat it as the complete latest repository.

Later remote work added bounded preflight/dry runs, foreground confirmation before destructive keystrokes, overlay roles, per-lane verification, localhost proxy restrictions and removal of unsafe tools. The docs also consolidated the operational contract. This safety history is useful retirement context, not a reason to port Premiere's controls into Tesseract.

[PR #14](https://github.com/shipshitshow/premiere/pull/14) adds newer native computer-use weekly/Shorts documentation. It remains open, with successful recorded checks at head `147ab872fef8e2dd384abf3f2aaf315007f8d5cd`. Latest September guidance still presents Premiere as the active workflow. A retirement update should distinguish historical recipes from current instructions, preserve useful cut/transcript contracts, then resolve that PR and archive only after reconciliation. No PR was merged/closed and no GitHub archival occurred in this audit.

## Examples: candidates and publication checks

| Candidate | Actual source | Audit result and remaining work |
| --- | --- | --- |
| Agent flow debugger, PocketCAD, FPS arena | Public `opus48`; Studio directory is named `opus84` | Selected public snapshot secret scan found no leaks. No root license found; review asset/font provenance and runnable setup. FPS requires a PartyKit host. |
| OpenSora application | Clean Studio Git history; private remote has only workflow scaffolding | Full 20-commit local-history secret scan found no leaks. README claims NestJS/Clerk but code uses Fastify/JWT/MongoDB. Document real dependencies, paid providers, credentials/mock mode and license before publishing. |
| Free-model comparison | Studio `openrouterfree`, largely untracked | Curated 90-file candidate scan found no leaks. Excluded `_private`, temporary runs, dependencies and environment files. Review root/runtime instructions, assets and episode mapping. |
| ShieldCheck plan comparison | Studio `mdtohtml` | A Markdown/HTML planning artifact, not a completed scanner application. Publish with that status and verified context. |

Secret scans have bounded coverage and do not establish license, asset rights or runtime quality. No license was selected on Vincent's behalf. No code was copied into a new public repository or private repository made public.

Proposed repository structure:

```text
examples/
  README.md
  catalog.json
  episodes/
    <recording-date>-<livestream-youtube-id>/
      README.md
      episode.json
      <demo-slug>/
        README.md
        source files and lockfile
        prompt.md
        .env.example (placeholders only, when needed)
```

Each episode page links the livestream, recap and vault note. Each demo records the original source/commit, prompt, model as used at recording time, setup/run commands, required services and costs, license/credits, verification and known limits. Keep apps independently runnable; a shared monorepo build is unnecessary unless multiple examples genuinely need it. Preserve original repository history and add redirects after the curated migration is verified. Do not attach a demo to a guessed episode.

## Delivery sequence after design is settled

1. Settle the primary audience, demo fallback and canonical editing-library boundary.
2. Establish the channel profile and one public skill contract; replace competing scripts and stale references.
3. Document the existing Studio structure and adapt its helper workflows without moving media.
4. Import the 29 located missing transcripts with provenance and publish the complete coverage ledger; obtain the remaining transcripts through available captions or authorized local transcription.
5. Audit/run the example candidates, settle licensing, create the public episode-indexed repository and link it from vault and the org profile.
6. Update Premiere retirement documentation and resolve its remaining history/PR before archival.
7. Validate skills and links, obtain independent review of implementation, and publish scoped PRs with required checks. Run a small production pilot and evaluate comparable analytics before claiming improved performance.

The design interview currently asks about audience, demo fallback and the media-library boundary. Further decisions such as example licensing and version retention depend on that structure. This audit does not mark the requested skill pack, full transcript archive or example migration complete.
