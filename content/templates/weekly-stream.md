# Ship Sh!t Show - Weekly Stream Template

## Show Structure (60 min)

| Segment | Duration | Description |
|---------|----------|-------------|
| Cold Open | 1 min | Hook, no intro |
| AI News #1 | 10 min | News + hot take |
| AI News #2 | 10 min | News + hot take |
| AI News #3 | 10 min | News + hot take |
| Demo | 25 min | Build something live |
| Wrap Up | 4 min | Recap, next week, CTA |

---

## Pre-Show Checklist

### Content
- [ ] 3 AI news stories selected
- [ ] Hot takes written
- [ ] Demo project ready
- [ ] Demo goal defined

### Tech
- [ ] Stream software ready
- [ ] Screen share configured
- [ ] Claude Code / Cursor ready
- [ ] Browser tabs loaded

### Environment
- [ ] Notifications off
- [ ] Water ready

---

## Segment Templates

### Cold Open (1 min)
```
[Jump straight in, no intro]

"[Biggest news hook]. [Second hook]. [Demo hook].
Let's go."
```

### AI News (10 min each)
```
1. WHAT HAPPENED (1 min)
   - Headline
   - One sentence why it matters

2. CONTEXT (2 min)
   - Background
   - Who's affected

3. DETAILS (4 min)
   - Technical breakdown
   - Show screenshots/demos

4. HOT TAKE (3 min)
   - Your opinion
   - What to do about it
```

### Demo (25 min)
```
1. GOAL (1 min)
   - What we're building
   - Why it's useful

2. BUILD (20 min)
   - Code live
   - Show AI interactions
   - Mistakes are content

3. RESULT (4 min)
   - Show it working
   - Push to repo
```

### Wrap Up (4 min)
```
"That's it.

News: [one-liner each]
Built: [what we shipped]

Next week: [tease]

Subscribe. See you next week."
```

---

## Episode Metadata Template

```yaml
---
id: sss-XXX
title: "[Hook Title]"
date: YYYY-MM-DD
type: stream
duration: "1:00:00"
youtube_id: ""
topics: []
guests: []
news:
  - title: ""
    source: ""
    url: ""
    hot_take: ""
  - title: ""
    source: ""
    url: ""
    hot_take: ""
  - title: ""
    source: ""
    url: ""
    hot_take: ""
demo:
  project: ""
  repo: ""
  goal: ""
  continuation: false
chapters:
  - time: "00:00"
    title: "Cold Open"
  - time: "00:01"
    title: "AI News #1"
  - time: "00:11"
    title: "AI News #2"
  - time: "00:21"
    title: "AI News #3"
  - time: "00:31"
    title: "Demo"
  - time: "00:56"
    title: "Wrap Up"
thumbnail: ./thumbnail.png
---
```

---

## Post-Show

- [ ] `sss transcript <yt-id> --episode <slug>`
- [ ] `sss thumbnail <slug>`
- [ ] Cut clips for Shorts
- [ ] Tweet recap
- [ ] Update timestamps
