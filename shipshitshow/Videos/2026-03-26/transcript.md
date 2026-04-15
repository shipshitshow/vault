# Transcript

[[shipshitshow/Videos/2026-03-26/overview.md|<- Back to video]]

## Claude Code Channels Just Killed OpenClaw.

![[thumbnail.png|640]]

### Context

- Parent: [[shipshitshow/Videos/2026-03-26/overview.md|Claude Code Channels Just Killed OpenClaw.]]
- Description: [[shipshitshow/Videos/2026-03-26/description.md|Description]]
- Thumbnail: [[shipshitshow/Videos/2026-03-26/thumbnail.md|Thumbnail]]
- YouTube: https://www.youtube.com/watch?v=gnfJl0YfNHc

### Source

> Auto-imported from YouTube captions.

### Transcript

Last week Anthropic dropped Claude card
channels and obviously it killed open
claw, the open source project that
everyone used for what? Two weeks?
&gt;&gt;
&gt;&gt; Yeah.
And bought by OpenAI for what? 1
billion? That's it. And then just with a
tiny update destroy everything. Is it?
That's what we're going to see in this
video.
Like, subscribe.
For us, we just released Claude card
channels which allows you to control
your Claude card session through select
MCP starting with Telegram and Discord.
Use this to message Claude card directly
from your phone. When I read that, I
didn't really understand because you can
already dispatch
you know, like teleport your session
from one
from your desk to your mobile Claude
card app, right? Yeah, but then you go
into your Claude card app. Yes. And you
don't go into Telegram or Discord.
True.
So
&gt;&gt; Yeah.
But in your Claude card app, you don't
have other AI bots.
So you can just put them all in one
channel
in Discord and have them communicate,
check each other and keep on going.
Okay, so what's the benefit because I
didn't I didn't test it like to be
honest.
&gt;&gt;
&gt;&gt; Well, yeah, there is a benefit but still
you need to set up a bot on Discord. I
did it in Discord not on Telegram. You
have to install a bot, you have to
create the API key, install it in Claude
code and then start your session with a
special prompt.
And at that moment your Claude code
is also active in Discord. So whatever
you ask your Discord bot, it is directed
to your Claude code in the terminal and
you can just type and it will
add every message that you ask you it
will add it in the terminal and do it
there. So it's just an extension.
Okay.
And it's synchronized between your
desktop and like the same session like
we can see in the video, right?
Yeah. That's cool. But the difference is
it is only for one for one set up.
One CLI?
Okay. So
I don't know about you but you're
working mostly in one in one project,
right? One project, yes, but I always
have like eight
different plan on Ghosty.
Yes. I have eight like eight or even 16
like depends.
Yeah. And I'm working on 10 projects per
day so I have to constantly switch.
So for this there is not a big change
for me because I rather work on my PC
directly in the terminal in the CLI
instead of going to Discord to connect
to my CLI. That's weird. But my
advantage is
I'm having a Claude bot I have set up
and it's in the Discord.
But sometimes you have issues where you
can just run it says you need to do it
in the code directly or you need to edit
some files.
So what I did, I set up Claude code in
the main root file folder of my Claude
bot.
Okay. Oh, okay. Okay, so you use both
like channels. I use both in the same
chat. So my Claude bot so my Discord bot
when he says no, you need to do it
manually, I just say ask it to the
Claude bot Claude code bot.
And it will ask it it can just install
it it can change the files that it
normally doesn't and it can even restart
and then just keep on going.
Oh, interesting. Okay, so you can even
have your Claude card monitoring your
open claw setup when it's like full
buggy or you lost the gateway. Then
yeah, okay. That's cool.
And everything in the same chat. Yeah.
Hey. So that's the that's cool thing.
And what what I found amazing is I
started and my first question was, "Hey,
AI one meet AI two. Introduce yourself
and tell what you're doing and make a a
proper agreement on who does what." And
he made like a chat with 50 messages
sharing to each other what they were
doing. They were giving each other's
commands and even setting up an SLA on
what should they do and when do they ask
the other one for help.
Which
I didn't ask for an SLA or something but
they just did it. Which model did you
use like did you Sonnet or Opus?
No, no, I have Opus 4.6. Okay.
So I just use and I use it on high.
Oh, okay. Yeah, so after two days of
that you're not going to have a lot of
token on your weekly allocation. Yeah,
but you need to set some restrictions
otherwise they just keep on going. Yeah.
Yeah, you then you create your own multi
multi book, right?
Yeah.
That makes sense.
And yeah, so every hour you use both to
review each other when you have a task
to do, right?
Yes. Okay. So I never trust one because
even Opus 4.6 if it codes something
there is always an issue. Yeah.
&gt;&gt; Always a security issue.
Or even like a bug.
Yeah. Yeah, I have I like in the last
yes today and yesterday I had
so many regression like from a commit to
another and even like Codex 4.4 4.5.4
like regression after regression.
So that was annoying. Yeah, and even if
you tell it to write proper testing and
everything, there is always something
but when you have Claude do the code and
have Codex do the the check, then it
finds so much more and it fixes the
issues and it is so much faster. So I
always this is perfect because right now
I have like Claude code coding. I give
it a task and then I say put a summary
in here and what you did, show the
changes and when you do it tag my Codex
bot and Codex get tagged and then it has
the the the task to just analyze
everything and I keep them tagging each
other after each review.
That makes sense. Okay, so do you want
to do a demo of like with your setup?
Can you I have a a minimal demo because
I crashed it just before the show.
&gt;&gt;
&gt;&gt; I can show how it works, I think. Okay.
Because what I did, I have set up the
the Discord a team
and in the team is me myself, my Claude
code bot and my
Claude bot.
And that's perfect because here on the
right I just opened a project and it's a
WordPress plugin to reset Cloudflare
caching when you reset the caching on
your WordPress website. So I just opened
a random one and here on the left you
see that I have Cloud Wizard.
That's a Claude code and I have Wizard
AI one that's my Mac mini one.
&gt;&gt;
&gt;&gt; And I have already activated it.
So it should both be
active here in the Discord. So when I
tag my
Cloud Wizard and ask, "Hey, are you
live?"
And you see here on the right in your
CLI you see them coming.
And then it's doing the thinking, it's
creating a reply
and you see here it says plugin Discord
reply and it replied to Discord.
Nice. So it says, "Hey, yes, I'm here.
What's up?
Can you let me reply?"
Introduce yourself to
Wizard AI one and that's the other one.
Mhm.
And ask how he is doing.
Okay, and for both like for the open
claw and the Claude Discord bot you need
to go to the developer section like have
a proper like
Discord token and set up. On your Mac
mini both are running on your Mac mini?
No, it is my Mac mini is Wizard AI one
and the screen that I'm sharing right
now is just my laptop. It's my MacBook.
Yeah.
So now you see that they just keep on
asking each other and they keep on
going.
And every message is dropped in the
terminal.
This is also the part because people say
it's going to kill open claw but
it took me like an hour to set it up
properly.
Yeah.
And I don't think non dev people people
those people are even trying to figure
out how to set up a Discord bot, what
rights do you need, how to activate it
in Claude code, you need to add
add the
the plugin for Discord to scale then you
need to set it up. Mhm. And
you need to do the
proper settings in your config file and
then you can start chatting and chatting
here is just if you go away it's perfect
because you have the Discord app on your
phone and you can just keep on
communicating but most of the time when
you're working you're near your PC so
there is no use for me to do it in
Discord except when I want the the bots
to communicate.
For a company like would you still use
open claw or does
Claude channels stuff because it feel
like more more secure than open claw
itself too, right?
Like I would trust Anthropic setup more
than open claw.
Yeah, but then you need to have one PC
still running the project.
Have Claude active and even if it goes
because you still go into
a full context and then you need to just
clear or reset everything or compact.
So you will lose
your your your memory from your chat.
Yeah, but for business you would run on
a EC2 instance.
Like you put your your your Claude
Claude subscription
on a EC2 instance. Mhm. And then the
whole company can use it. Yeah, do you
think like Anthropic could kill an open
source project like open claw?
But because like same thing for me so
open claw got bought by OpenAI, Facebook
run it, and then in uh put it inside
their own
like apps, etc., etc. Yeah, yeah. That
That can also be.
They probably have many reasons. I hope.
Otherwise, for one reason, it's a big
amount of money. Yeah, or they just
don't want to lose against Meta.
Yeah.
Buy all the people.
Okay, so it's not the death of open So,
just yet. We're just going to see what's
going to tell us the better.
Yes. We just keep on using everything
and take what's best.
That's what's up. And my camera is
shutting down. So,
I think it's a it's a good sign to end a
No.
Nice.
I am a Thank you so much for your time.
And yeah, let's do it again next week.
Perfect.
Bye, everyone. Subscribe. Follow us.
Every Everything is in the description.
Bye.
