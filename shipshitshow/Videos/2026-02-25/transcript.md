# Transcript

[[shipshitshow/Videos/2026-02-25/overview.md|<- Back to video]]

## How to Install OpenClaw Agent Swarm on Discord

![[thumbnail.png|640]]

### Context

- Parent: [[shipshitshow/Videos/2026-02-25/overview.md|How to Install OpenClaw Agent Swarm on Discord]]
- Description: [[shipshitshow/Videos/2026-02-25/description.md|Description]]
- Thumbnail: [[shipshitshow/Videos/2026-02-25/thumbnail.md|Thumbnail]]
- YouTube: https://www.youtube.com/watch?v=WJJZHyhlAuI

### Source

> Auto-imported from YouTube captions.

### Transcript

Yeah, you have already installed Open
CL. You know how to use it. You use it
on Telegram, but Telegram is So
now we switching to Discord. The Yeah,
Discord is cool. Coding on Discord is
the new meta, man.
&gt;&gt; Yeah, you just ask it. You don't even
code anymore. They do it for you. It
doesn't matter how how you prompt it.
It's all about finding the way that you
can work the most optimized way and have
the best productivity and and what
what's best for you. And so what what
are you doing with the that little uh
Mac Mini? Like how do you interact with
it?
&gt;&gt; Uh well, I'm adding it I've added it to
the Discord and I made it like my uh
it's it's the new team lead in my
company and it's my personal assistant.
&gt;&gt; Since you told me that uh I did it too
on my like Discord and it's way more
user friendly than Telegram.
&gt;&gt; Yeah. Yeah. Telegram is just one channel
and that's hard. And in Discord, you can
still have one channel, but you let it
go to different topics.
&gt;&gt; So, you have groups on Telegram when you
can create topics and it's kind of the
same setup. But I'm I don't know like
the user like the fact to switch the UIX
to switch from one channel to another,
it's way easier on this.
&gt;&gt; I've been using it for a few years. So
um for the systems that we host instead
of logging everything to uh to a local
text file and need to open it or using
some paid software online where you can
just scrape everything. I'm pushing uh
error logging to my discord server. And
it was more like normally when you set
up a server and you do the logging and
you want to have Laravel or any other
system, Python system on it, you need to
pay for the for the actual services
&gt;&gt; and it isn't that that expensive like
$25 per month, but if you have 10, 15 or
25 servers running, it adds up.
&gt;&gt; Yeah. No, for sure. So, and the cool
thing is when you put all the
notifications for logging, for errors,
for 500 errors into one channel,
&gt;&gt; Cloudbot can read them all, knows what
the the GitHub repository is, and just
starts creating new branches with bug
fixes.
&gt;&gt; I haven't done that, but
&gt;&gt; yeah. So, we automate the error logging
without any expensive services. We just
do it with a Mac Mini and Discord.
&gt;&gt; Damn.
Can you show us your little Discord with
all of your swarm agents?
&gt;&gt; Yeah. And this is the moment that we
have already set up Cloudbot on the Mac
Mini, right?
&gt;&gt; Yeah.
&gt;&gt; I've set up a Discord bot. I've
connected it. Um I've given it access uh
to some channels. But the Discord
channel, the Discord that you're seeing
right now, this one, this is a demo. We
have set it up today just to show you
how it works. And we even made a
separate workspace. So the AI bot that's
added here. The cloudbot uh does not
have all these settings and the setup
that I did for myself. And what I'm
doing in my my other because I already
mentioned the the logging the error
logging and everything.
&gt;&gt; Mhm.
&gt;&gt; So what I did is at wizard
I have an logging channel.
Can you uh watch it full time and
fix every bug reported
in it? What info do you need?
Can we set up a separate
flow for that channel to
do bug fixes in new branches in the
GitHub repo.
Okay, let's see what it does because
this is how I started. I just added a
new channel. I set up the web hooks to
have the the box incoming. I asked the
AI, okay, what information for me do you
need
&gt;&gt; to fix the bug? And then it said in my
other in my own setup, it said, okay, we
need to have a a title bug so that I
know that's a bug. Um, we need to make
sure that we know what GitHub repository
it is. Well, I know where the error
logging is coming from. So, I'm adding
it manually in in in the code. It's
adding it automatically into the Discord
logging.
&gt;&gt; Mhm. And
it also added some additional and here
it comes
u error channel watcher. It monitors the
error channel creates concise summaries
and optional auto triggers GitHub issue
fix and then we create a bug fix
pipeline so it takes a new box creates a
dedicated branch fix and an issue name
opens a pull request and it can keep
watching and handle pull request reviews
comments too.
So this is the first setup for your
entire buck fixing pipeline.
&gt;&gt; Wow.
&gt;&gt; You only need to to push it here.
&gt;&gt; Yeah.
&gt;&gt; So what I do is uh it is possible that I
get multiple notifications.
Can you make sure you only handle it
once? I don't ask for debugging. I sorry
for uh uh making sure it's not double or
whatever. I only say handle it.
I hope it's as smart as the last time.
And it says build a fingerprint from
service plus error text with top stack
frames and environment.
If same fingerprint appears again in
window, no new fix flow.
&gt;&gt; Wow.
&gt;&gt; And it just does it. So you need to ask
the correct questions.
&gt;&gt; Yeah.
And in my setup I said okay well
messages are coming in but some messages
in that channel can be a reply for me or
something else and I don't want you to
handle then as buck report. So we we set
up the entire flow if it contains bug do
this otherwise if it contains otherwise
if it contains otherwise do this. The
way I set up my own swarm of agents, I
have all of the uh channel that I have
uh notification like you basically where
like see like for example I have the
message card here which is um I ask to
keep the format the same everywhere. So
it should always display that and on the
right I have so blaze is my personal
assistant co of Genfe and same same
setup for ship sheet dev plus a content
producer and here I have the whole team
of genfit talking to each other for each
channel yeah I have a different uh
missions basically so what's your
mission personality and soul good
question let me pull that up from my
soulmally helpful I have all of those
GitHub subs notification blah blah blah
I have the comments and stuff what's the
CTO is going to say identity CTO AI CTO
of gened on the clone monor repo ship
the closest loop content engine make it
work make it fast make it secure because
yeah don't make mistake
&gt;&gt; user MD founder of genon wants to move
fast preer action over discussion let's
go
&gt;&gt; with these few uh lines of of text it
does it correctly already.
&gt;&gt; Okay.
&gt;&gt; It's a new world. It's a new world. Did
we conclude?
&gt;&gt; Yeah, I did. What What was What was your
conclusion?
&gt;&gt; Uh I mean like uh
I can feel the agent swam on Discord
even more than Telegram. And that's all
I want to do. I want to control like 200
Discord boat that will provide me
a million uh in revenue. Uh, next year
uh, next week.
&gt;&gt; Next week. Why not?
&gt;&gt; That's my conclusion. Mitchell, thank
you so much for your time. Really
appreciate it. Everyone who watched this
stream, thank you so much. Uh, you were
a lot in the chat. And yeah, thank you
for everyone who watched this video,
too. Thank you. Bye-bye. Cheers. Peace.
Bye. Bye.
