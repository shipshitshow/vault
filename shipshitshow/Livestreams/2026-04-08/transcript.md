# Transcript

[[shipshitshow/Livestreams/2026-04-08/overview.md|<- Back to video]]

## [LIVE] We Need to Talk About Anthropic

![[thumbnail.png|640]]

### Context

- Parent: [[shipshitshow/Livestreams/2026-04-08/overview.md|[LIVE] We Need to Talk About Anthropic]]
- Description: [[shipshitshow/Livestreams/2026-04-08/description.md|Description]]
- Thumbnail: [[shipshitshow/Livestreams/2026-04-08/thumbnail.md|Thumbnail]]
- YouTube: https://www.youtube.com/watch?v=MJp8l5ZBlI4

### Source

> Auto-imported from YouTube captions.

### Transcript

And we are live. Let's go. Cool. Nice.
What's up, man? Yes, yes, all good. How
are you? I'm doing great. Uh
better than Anthropic, I guess.
Yeah.
You didn't leak anything, right? I mean,
no, I did not.
Because now I'm moving like Gen 3 to
open source and Claude made the first
commit and published my production keys.
Like the first commit of the migration
to public. Poof.
I received like 10 emails.
Uh yeah, we disabled your key. We
disabled your key. We disabled your key
because we found it on GitHub. I said,
"Okay, bro. Thank you." Thank you. Thank
you for being secure. It's better than
you doing the job for yourself.
I mean, honestly, I was surprised. That
that was the first time I received those
emails, but like yeah, all of the apps
boom boom boom boom.
Well, normally when you try to put it
in, Claude will give you an
an error as well because they say we
cannot put it in.
Uh I don't know. Like Claude just copy
paste my dot env.production file and
merge it and then I opened the repo to
public and then
Yeah. So, you you didn't actually put
the the keys in, you just copy pasted
them. Yeah. Yeah, because I was like my
doing the migration from one project to
another, new repo, and boom. Like yeah,
I think the Git ignore was not copy
paste yet.
And committed pushed. Yeah. You know it
goes.
&gt;&gt; Yeah.
Trust the AI.
Yes.
&gt;&gt;
&gt;&gt; Well,
Yeah. I think they did it as well.
The what? Trust the AI. Oh yeah, maybe
too much.
But I think it's like what they had it
was the
a human error.
Because
Yeah. It was a human who published the
package. But anyway, introduction.
Let's go.
Uh what was my first sentence?
Let me check the mic first.
Laugh.
Boop.
Live.
Cool.
Uh I check. Very good. Are we good? Very
good. I chat. Hi. Subscribe.
If they Yeah. 140.
On X? No, no, subscribers.
Oh yes, yeah. Good morning, bro. Yeah.
Yeah.
Uh 900,000 uh
What? It's a 40% growth. Mhm.
Mhm. One one day it will be our human
error, but uh
later.
&gt;&gt;
&gt;&gt; Anyway.
Um okay.
Did you ever leak your production key?
Okay, no, that was me. Uh
&gt;&gt;
&gt;&gt; Did you ever leak your
source code in a NPM package, increase
your price, or even better, ban open
source project uh and
uh
Oh yeah, and have your product
completely unusable for days? No?
Maybe not you, but Anthropic did that in
the last few days and we need to talk
about it.
Subscribe.
Boom. Noise.
Okay, okay, okay, okay.
Thanks, Claude, for
writing this introduction. Fantastic.
So,
uh what are we going to talk about?
Where are the tweets? Where are the
tweets?
What did I do with them?
Yes.
Laugh. Yes, green.
Yes, green. Like
boof.
This week
um on
Yeah, so yeah, exactly 7 days ago.
Appears to a that a big chunk of Claude
code source has been exposed to NPM via
the dot map file accidentally uploaded
to the public registry.
thousand line of code, almost 2,000
file.
Your jobs to the Anthropic team, this is
brutal.
I mean,
uh
So, yeah, what
What What What did we saw when you saw
that
Mitchell? I was first like, when you
commit your changes and you see so many
lines of code, you know that you made a
mistake, right?
Uh
No, but but I mean,
Oh yeah, the You You're talking about
the source map?
Yeah, 512,000 lines of code. You should
have seen it. No, but that's the that's
the total package, right? Yeah, yeah, it
is. The source map, you you have less
than that, I guess.
I mean, maybe they didn't have an open
cursor and they just like trust the AI
commit and boom. Yeah, probably that was
it. That's
That's possible. No, I don't want to do
that. I want to change.
I will do that later.
&gt;&gt;
&gt;&gt; Okay, come back.
Well, yeah, the first thing I checked
is, okay, what did they leak? Yeah. And
do we need to disable Claude code and
everything?
True.
Uh Do you have your crypto on your AI
computer? No, no, no. Yeah,
separated fully.
Yeah, it's segregated. I mean, yeah,
that's brutal. But like I mean, okay,
it's Claude code the desktop app, right?
So, it's not the weight of the model or
whatever, right? Like
Yeah, it had some logic in it, but it's
not a Claude model itself. Yeah, no,
exactly. So, okay, it's the app. Like
yeah, there is like Codex is open
source.
So, yeah.
But still like people were having fun
with
the files because you can study that
Yeah, well, I've seen so many
tweets about people telling everybody
what they found out. Yeah. Now, exactly.
Okay, so Anthropic blah blah blah.
Claude Claude code.
Yeah, that was a copyright. Yeah. Yeah,
that's a fork. And okay, so also when
you have that,
like
if you take a closed source project and
you ask the AI to rewrite the same
software in another language or even
just rewrite the software,
it's not the same code.
So, you don't have
It's not even a fork, it's just a new
software that you wrote, right? So,
there is no right anymore. So, if Claude
code tries to disable your
GitHub repository, it's not possible.
Yeah, they can't because it's not the
same  It's not the same
Claude code app, it's Claude code now.
Yeah. So, what did people do? They were
fast. They just rewrote everything.
Yeah.
I mean, uh
When you have the spec of the software
and you Okay, you prompt you prompt
Claude to rewrite Claude code
&gt;&gt;
&gt;&gt; and you say, "Okay, change the variables
name." Yeah.
Well, maybe Claude code itself said,
"Okay, this looks familiar. I know what
to do."
I I have the source map now, so I know
what to do.
Um okay, so yeah, it's of
Anthropic is not officially more open
than OpenAI. Vibe coding vulnerability
service. Who started? Who's going?
Uh correct. The last
30 day my contribution to Claude code
were written by Claude code. Claude code
sourcing.
Yeah, that was that was a bad day for
Anthropic. Yeah.
Uh and it was not over because they had
they got more  Okay, so we have
that. So, this was first thing. What was
the second?
Uh okay, so you Yeah, unusable at
So, Claude code leak. Oh yeah, also
what do we have next?
Uh
Can't believe.
I want to to see the features of I
forgot where I I put them, but
there is hidden features in the source
code called Caros and it's basically
show you Anthropic end game.
Um is a always on proactive Claude that
does thing without you asking. It run
24/7 while you work.
Basically open Claude.
Uh Anthropic hasn't telling the public
yet, but the code is fully built and so
it works. And also like that's
interesting because um they built the
features and that's why they release
something every day. It's because it was
built like boof.
And they keep like they keep features
in the build and they just flag it on
off. Yeah, so they have like an on off
switch and that just enables it
everywhere. Exactly. Which is like it's
massive because yeah, on Twitter
uh you have a new release every day.
Mhm. You're always on the timeline
because
even a small thing
you have something to push again and
again and again. So, they just have a
big dashboard with like thousand
switches. It
Uh yeah, like I I watched a
few video about it and
he explain
They probably use
growth because I I implemented it.
Uh
Growth book.
Yes.
Like boof.
So, the number one open source feature
flag and experimental platform.
So, in React, you can add a flag to a
page or a feature or like a you have a
provider and on top of it,
uh yeah, you put the like for example
here exactly like a pricing flow, it's a
feature, whatever. Uh okay, no, small
project, but uh yes. So, you see winter
banner, you can
toggle inside the
the dashboard and the route will be
activated or not.
It's It's really powerful for a startup
because again, you can say, "Okay,
uh you you go MVP, but your MVP has way
more features
that
uh that's initial launch, but then
you're you're all team that ship every
day. Yeah, yeah, you can just keep on
building and just when the marketing is
ready, you you just enable it. Exactly.
And it's uh yeah, it's it's a really
product
proactive no, but like
smart way to push features
um
to the public. Mhm. So, you know, Keros
get gets a hair hair bit. Basically, it
prevents anything was doing right now.
So, exactly exactly open Claude, man.
Yeah, I just hope that their heartbeat
spends less tokens.
Oh, yeah, yeah.
Oh, sorry, what wait, what? So, they say
that this one is going to get a
heartbeat as well. Yeah, I just hope
this one spends less tokens. Yeah, like
uh
I hope they going to use a queue or
something inside Claude to
They have to to use a router anyway.
Yeah, yeah, they have to, but
&gt;&gt; Yeah. get a cheap one. Mhm.
Uh basically, anything Claude Claude can
do already do just without you telling
uh you telling it to, but here what
makes Claude different from regular
Claude code, it has at least three
exclusive tools that regular Claude
doesn't get. Push notification, okay.
File delivery, so it can send you thing
it created with
uh created without you asking for them.
Pull request subscriptions, so it can
watch your GitHub and react to code
change on its own. Yeah, well, that's
not specific for this one. You can just
create a webhook and Yeah.
So, it is just easier to use. Yeah, and
and like a habit is just like a nice way
of saying, "Okay, we have a cron job
every second." Yeah,
we just keep on asking
when when
And and then and then you burn your
weekly subscription and it's Tuesday.
Yeah.
And then says, "When do you upgrade?"
Yeah.
Uh yeah, and then you pray for for a
reset.
You pray for for a new bug so you can
get a reset. But maybe the only
difference is and he didn't tell it is
that this one is inside your
subscription, the heartbeat.
&gt;&gt; Mhm.
You don't need an external API or just
an API with additional cost. Yeah, yeah,
it's just like one more tool they put
inside, but yeah.
Uh Keros feature product blah blah blah.
Okay, so that was the tweet.
Uh
No, not all. Uh another one something
Claude listener Damon. Okay, so Keros we
have Keros.
Keros
uh tac tac
paf this one.
What do we have here? From the massive
cleaner undercover mode there, it's uh
safety system that kicks automatically
whenever a Claude code
is used to contribute to code to public
or open source repo. Uh interesting.
Huh? What?
That that kicks Okay, the goal is to
stop the AI from accidentally leaking
Anthropic's Oh, yeah, okay.
Uh leaking Anthropic's secret internal
information like for example, uh not
telling that you are Claude code.
Mhm.
You are undercover in the public open
source repo. Never include internal code
code name, animal name,
unrealized model version.
Okay. Oh, office Oh, let's go. You can
just add your own name and never see
have anybody see that you use Claude.
But what if my name is Claude?
And then you are banned forever.
&gt;&gt;
&gt;&gt; Like
And if your last name is code, then
you're you're Yeah, then you have a big
issue. Yeah, what what if my end or is
like Claude code dot
fra? Yeah.
&gt;&gt;
&gt;&gt; That And also like we're going to see it
with like uh open open Claude ban, but
like they are looking at
the system prompt
of saying, "Yeah, if the system prompt
is say is saying, 'Oh, you are open
Claude blah blah blah, don't process
the API request.'"
It feels weak.
Well,
a little bit of creativity and you can
do a workaround.
Yeah.
Yeah, no, exactly. I like uh yeah, you
rename open Claude to mult book. Mult
mult
uh Yeah.
Mult whatever Yeah, it was mult mult,
right?
Like it it's weird.
Um okay, imagine Codex if Codex were
open source, that would be the real
bomb.
Anthropic is playing permanent game
among us, yeah.
Yeah, but
most of the people using open Claude are
the ones who don't know how to code or
to set up any more complex system. So, I
think they might as well just catch 90%
of the people using open Claude doing
just this.
I don't know for sure, but
uh
also the system prompt like you can't
edit the system prompt of the tool you
use, right? Because like the user don't
have access to that. No, exactly.
But uh yeah. Also, yeah, Keros we
already talked about that. The buddy
system, Tamagotchi style companion
creator with ASCII. I think it was like
the part of April Fool, I don't know. Uh
coordinator mode, multi-agent
orchestration. If they put that in But
we have sub agents, but if
we have multi-agent orchestration, then
we don't need paper clip anymore.
Open Claude.
Uh team memory system, interesting. Uh
Claude apps builder, okay.
Uh undercover mode, okay.
Uh every release feature every code name
every direction they're building toward
just sitting there on a competitor to
read. Yeah, I mean, yeah, if you if you
leak it. Yeah, and they are just waiting
for the right moment to publish it.
Yeah.
So, yeah, it's
definitely uh
what?
Oh, I want to Yeah. screen I want to
stop it.
So, yeah, like is there any features
that you're waiting from like open
Claude or Claude to be able to do?
Uh not really. Yeah. I'm just waiting
for them to impress me even more.
Because we have said it so many times,
it's getting better and better and
Um
But And
For me like what what you were doing
with like the plan mode and having check
checked by Codex,
that's the real like killer for sure.
Oh, yeah. AI is really good at finding
Claude.
I think that's also why Codex created
the plugin for in in Claude.
Which is smart because you use the model
inside your competitor CLI. Yeah. Good.
Right. You make them spend tokens. Yeah.
I don't know, it's it's really really
smart. Uh maybe I will have it. Uh so,
Codex uh advance AI review. I'm only
using this one. Yeah, and you can even
take over the entire coding with Codex
in Claude.
What? You can just say to Codex, "Okay,
when you're running Claude code
and you have the Codex plugin, you can
have Codex do the coding for you. It can
take over the entire session."
Oh. So, you can have Codex
running in Claude code
and just only use Codex. So, it's so
weird.
That's Okay, I have a tweet here.
It's not the official one, but
whatever.
Um
OpenAI just shipped a code Codex plugin
for Claude code. You can now have Codex
review code that Claude wrote inside
Claude environment.
Uh plugin marketplace, add OpenAI
whatever
uh review. Okay, wait.
So, review add the agent uh okay, no.
I want to first need to install. Yeah.
What the  Okay. Yeah, when you
installed it, you need to do a a
restart.
Set up review status, rescue result,
cancel, okay.
But the big one. So, review is reviewing
the uncommitted change, right?
Yes. Yeah, standard code review.
Yeah, that's that's really good.
Delegate, ask Codex to fix Oh, also that
that works.
Mhm.
Codex thread, okay, cool.
Nice video.
But yeah, so Codex review standard code
review actively try to break your code.
Uh that's What? No, I Oh, it's not
for the plan? It's not
only for the plan? No, no, it actually
does even more, but in plan mode, it's
also perfect for usage.
Okay, I have my weekly reset tomorrow at
10:00 a.m., so let's go.
And the third one, the Codex rescue, it
just takes over and it starts coding.
Really? So, if you have
Claude code going into a loop and you
have already He him like five times and
then apologized five times.
Ask Codex to rescue you and it will do
it.
That's dope. So, that's that's a cool
name for the function.
That's a cool for sure.
Uh adversarial review catches catches
things
the right team or they're wrong
different training different bias. Yeah.
Uh Claude write the code collects review
it. Oh, what?
Okay, so it's not even that the way we
are using it.
Um AI coding. Yeah, because you can even
review after you can review uh
Hmm.
Yeah. I think that's that's AI, right?
They give you so many options and
everybody uses differently. Yeah.
Uh everyone collects adversarial review
against uh Claude design spec and it
give it a 66.
Go to fix and run the review collects
give it 66. Okay.
Uh
Uh lighting composer to Oh, yeah, are
you using cursor?
Composer Yeah, yeah. No, no. I even
deleted the app. Yeah. Okay, fair
enough.
That's
Okay.
Yeah.
Uh tac
So, yeah, that was that's a smart Do you
do you think like
um
Anthropic will write a plugin for
collects to use Claude code inside?
Yeah, well.
I think it would be cool, but Codex can
just burn them down on X. So easy. Yeah,
well, I would
if I were Anthropic I would retweet the
launch of the Codex plugin. Retweet boom
Oh, we did the same.
Boom. Yeah.
You can run Claude code inside Codex.
Um okay. So,
that was
a little
tool that we were using better than
Keras or whatever.
Common left in production. What about
this one?
Tac.
Baf.
K
just like NPM memo memoization here
increase complexity by a lot and I'm not
sure really improve performance.
What?
Okay.
&gt;&gt; I don't know what he's doing. Me
neither.
Neither.
Um Anthropic guys
So, yes, okay. Uh Claude code being
closed source. Yeah. Um
baf from Theo.
Uh Claude code being closed source is
the biggest bug from ball in the AI era.
If Claude code was on GitHub, this thing
would be trivial to identify and fix.
Instead, we are stuck reverse
engineering their incompetence. Okay,
boom. Eat that.
I mean
Would you put Claude code open source
after that?
Nah. Why would you do that?
Uh
Because uh then it will be easy to
uh
fix the issues by the community.
That's true, but on the other hand, they
already
They got funded with so much money. Hmm.
Do they even care?
Yeah, no. Yeah, but I mean I mean it's
like what do you hide in your
desktop app that the secret? Like Okay,
so again, I watched the Theo video. So,
yeah, watch subscribe to Theo channel if
you are not cuz it's really good. Um
He said the only reason I see that
they are not open source right now is
because they the code is so
because it was coded by AI from Sony 3.5
time blah blah blah. That's not a
gigantic mess and
they are ashamed of it.
Yeah, that that's a good possibility.
&gt;&gt;
&gt;&gt; But uh eventually, you can just have
your own AI rewrite it. Yeah, yeah, no,
exactly. Yeah, you can probably you can
probably rewrite at at the speed of the
other guys
from the source map to to have a new
software that works better. Yeah, well.
Theo recreated like
T3 code and the performance are really
good. So, they should fork T3 code and
rename it
Claude code. Yeah, well, even I think in
their own systems, they don't have any
limits on using the AI. They can just
do whatever we cannot. Yeah.
Oh, for sure. Oh, yeah. Right, working
at Anthropic would be probably cool.
Yeah, well, what if they already have uh
testing two models further who are even
smarter and we are just using this one
and we are happy with everything we
code. So, the developers are using the
better ones.
They're probably using
uh the new model they are launching now.
Yeah, what they are telling everybody to
be scared of? Yeah.
And they can't release it yet because of
the big issues. Exactly. Okay, we can
talk about that right now because that's
a nice transition. And I hope my AI will
pick it up for editing.
Cuz that was definitely a good
transition.
&gt;&gt;
&gt;&gt; Yeah.
Uh Anthropic Okay, now I'm going to put
the frame. Tac.
Anthropic launch
announced announced a new model via the
initiative project glass wing
uh like 2 hours ago. Yeah, okay. Yeah, 3
hours ago.
Urgent initiative to help secure the
world's most critical software is
powered by our newest frontier model
Claude Metis which was also leaked in
the document
stuff.
Uh which can find software vulnerability
better than all but the most skilled
human. Um and yeah, it's a model focused
for for security and they don't want to
release it because it's too powerful.
And yeah. Uh okay, we partner with
Amazon. Okay. Metis preview has already
found thousands of high security blah
blah blah. Uh we can watch bit of the
every single  day.
Can you hear the video? Mhm.
&gt;&gt;
&gt;&gt; So, software has always had flaws and
vulnerabilities. That's not new. For an
average person
the bugs are by and large not
&gt;&gt; something they notice on a daily basis
because if they do, they get fixed. But
then every so often, there are
vulnerabilities that have real severe
impacts.
&gt;&gt; Like  one single bug that works
its way into shared uh software
that many many many different products
or websites use. So, one issue just gets
magnified out around the world. So,
historically Do you write bugs?
We all write bugs, right?
I have a skin for that. Yeah. And
finding and patching vulnerabilities has
been a slow, time-consuming,  and
expensive process. If LLMs are now able
to write code at the level of some of
the greatest software developers in the
world it can also be used to find bugs
and exploit that  software
equally effectively. These models have
capabilities which are raising the bar
from a cybersecurity point of view with
their ability to  help defenders
as well as potentially help adversaries.
You announce a model and you're saying,
"Oh, yeah, bro, it's too powerful."
We are we Like do you think it's a good
strategy?
Oh, yeah. I'm for sure thinking that
every security officer is now contacting
them and saying, "Hey, can we use it? We
only want to use it internally to find
our own bugs and our own mistakes just
so that we can improve it."
How long before that security guy sells
the key to Anthropic to North Korea?
Yeah, maybe in a weekend he is a hacker.
You don't know.
Hey.
But He recently
Mhm. Have it leaked on the dark web once
and
it's done.
Yeah, no, exactly. Even like you can
resell that Like yeah.
They developed a new model, Claude Metis
preview. Early on, it was clear to us
that this model was going to be
meaningfully better at cybersecurity
capabilities. There's a kind of
accelerating exponential, but along that
exponential, there are there are points
of significance. Claude Metis preview is
a particularly big jump along that
point. We haven't trained it
specifically to be good at cyber. We
trained  it to be good at code,
but as a side effect of being good at
code, it's also good at cyber. The model
that we're experimenting with
is by and large as good as a
professional human at identifying bugs.
&gt;&gt;
&gt;&gt; It's good for us because we can find
more vulnerabilities sooner and we can
fix them. It has
I mean, if the model is good at
security, no  it can do like a SAS.
Like fast.
Security is hard. It's It could be the
hardest branch in computer science.
Exactly. Yeah.
Rocket engineering and like that, but uh
That's the next step. Yeah, I mean I
mean you still need to have some
security, right? Uh
even in the rocket, right? So, Yeah,
yeah, but but seeing this
how good is that security?
Um
&gt;&gt;
&gt;&gt; I mean
I mean
They are sharing some benchmark and
uh kind of crazy.
Uh so, that's that's in the paper. Maybe
they're going to show it in the demo,
but uh that's on the links like
official document. Uh software like
Bench Pro 78%
almost and opus is at 53.
That's a big leap. That's massive.
Terminal
bench, I think it's all of the task that
computer guys like a software
engineering are supposed to do.
65 to 82. Yeah, and right now if you
have an issue on your Mac, you just ask
Cloud Go to search for it and it fixes
it. Okay. So much faster. So imagine
what this one can do.
It rewrites your operating system. It
says I I increase the performance by
50%.
Bro, I found some documents you have
deleted like 6 months ago.
You didn't delete them. Yeah, you should
have deleted better.
Um yeah, so bench multi-model
multi-model I think it's like the voice
and stuff like that. Mhm.
&gt;&gt;
&gt;&gt; Uh
3% like double
&gt;&gt;
&gt;&gt; multilingual okay. It
So maybe you can you can talk to Cloud
in Dutch this time.
Yeah, that would be perfect. And right
now it's already doing really good but
Yeah, but you still has better you have
better performance with English right
yeah.
&gt;&gt; Yeah, yeah, yeah. And benchmark verified
93.9
and plus 14%.
It's it's
massive. Yeah, so this is the next model
that we just say check every GitHub
repository I have.
Yeah.
And then you do you do one prompt and
then poof weekly weekly stuff.
&gt;&gt;
&gt;&gt; Okay, so It's the ability to chain
together vulnerabilities. So what this
means is you find two vulnerabilities
either of which doesn't really get you
very much independently but this model
is able to create exploits out of three,
four, sometimes five vulnerabilities
that in sequence give you some kind of
very sophisticated end outcome. And we
think that this model can do this really
well because we noticed that this model
is very autonomous. It's just generally
better at pursuing really long-range
tasks that  are kind of like the
Autonomous at security task.
It wasn't supposed to do security right?
They wanted it to be autonomous in
coding.
Yeah. Yeah, I don't know. Yeah, I I we
wanted to build a model to build the SAS
but it built the atomic bomb. Yeah.
By accident.
task that a human security researcher
would do throughout the course of an
entire day. Obviously, capabilities in a
model like this could do harm if in the
wrong hands and so we won't be releasing
this model widely. More That's nuts.
That's  crazy. So now they
choose who gets the model but when you
have the model, you're outperforming
everybody. Yeah.
That's that that's insane. I think it's
going to
bring that Powerful models are going to
come from us and from others and so we
do need a plan to to respond to this.
That's why we're launching what we're
calling project Glasswing where we
partner with a number of the
organizations that power some of the
world's most critical code to put the
model into their hands to allow them to
look at how they can use models like
this to bring down risk and protect
everyone. And by giving these software
developers advanced tools before anyone
else,
&gt;&gt;
&gt;&gt; it gives all of us a collective head
start. It allows us to find things What?
They just want to be the big ones to to
be secure.
Every government possibly gets it to
make sure that their security is up to
date before they release it to the
public. Yeah, and and if you
um
it quarter is in Beijing, you you're not
going to get it. No, so you're behind.
Yeah, it's
&gt;&gt; Yeah.
Imagine all the people in the office
who used to code like 60 hours a week
and are now doing it 20 hours a week.
And they are using this on the side for
personal projects. Yeah.
Yeah, I know.
It's like it feels like we are even like
at the threshold of uh
Yeah, intelligence is a commodity until
level of IQ but if you get too smart,
only
Elon Musk can access it. Yeah, something
like that or CEOs with big companies who
have influence. Yeah. But how then how
do you compete?
You don't. Yeah.
Until open source.
Well, the question is how fast are
others going to build it as well?
I mean that's definitely a play with
open AI can say okay,
we have the same  but we're going to
open to everyone because we believe in
the power of the people.
Yeah. Well,
the only thing we can do is wait. Yeah.
that we couldn't find before and it
helps us fix these things
much Maybe they say it's dedicated to
security to just have an excuse to not
give it to the people like everyone
else. But oh yeah, you're not in
security so you don't you can't use this
model. Yeah, but then people just start
a security company.
Who did that?
How easy it
And then and then and then we put it to
your customers Gen feed blah blah blah
and then super smart.
Yeah, but this product it is when you
have it, you have a security company.
You don't need to do anything.
Yeah. Oh, then you so then you can run
like
Gen feed videos about security company
and resell that to
this $100,000
per year. more quickly. Working with our
partners, we've been  finding
vulnerabilities across essentially every
major platform. I found more bugs in the
last
couple of weeks than I found in the rest
of my life combined. We've
Yeah, so this makes every dev know how
bad he was before AI came. Jesus.
And and like what did you test bro? Like
did you test Bank of America?
Oh. I I think you don't want to know.
Oh. Because imagine all the big
companies who are here running the world
and all the software all over the world,
they have been building for more than 30
years.
Yeah. So I'm really sure that the code
is buggy as hell. Oh, like I had a
teacher in security who were explaining
to us that
he hacked the front end of one of the um
like before Shopify and stuff like that
in e-commerce because like the
um
the the cart was checking the price on
the front end. The price was edited from
the front end.
So if you change the price in your HTML
editor, Yeah, you could just pay less.
&gt;&gt; that price. Yeah.
And he got like some he says a couple of
bikes and stuff like that for 10 bucks.
Yeah.
Oh, yeah, but that's
it this kind of model will probably
found harder bug than that. Yeah, yeah,
these are the easy ones yeah? Or when
you need to do a payout, you put in a
minus number and it puts the money for
free in your account. Oh, yeah.
&gt;&gt;
&gt;&gt; Yeah, I mean I'm sure you can find some
websites still
running those issues. Yeah.
used the models to scan a bunch of open
source code and the thing that we went
for first was operating systems
&gt;&gt;
&gt;&gt; because this is the code that underlies
the entire internet infrastructure. For
OpenBSD,
we found a bug that's been present for
27 years
where I can send a couple of pieces of
data to any OpenBSD server and crash it.
On Linux, Wow.
How many people knew it before they
found it?
We found a number of vulnerabilities
&gt;&gt;
&gt;&gt; where as a user with no permissions, I
can elevate myself to the administrator
by just running some binary on my
machine. For each of these bugs, we we
told the maintainers who actually run
the software about them and they went
and fixed them and have deployed
the patches so that or not.
Yeah. I mean pull request open since 2
weeks and it's from Entropic. I said no,
I don't like the PR.
&gt;&gt;
&gt;&gt; Your code is messy. Yeah,
please document a less line, please.
&gt;&gt;
&gt;&gt; Anyone who runs the software is is no
longer vulnerable to these attacks.
For a developer who tirelessly maintains
software,
a model that can help them discover
vulnerabilities in their own code and
fix them  before they can be
exploited,
that is an invaluable tool. We've spoken
to officials across the US government
and we've offered to work with them and
and collaborate to assess  the
risks of these models and to help defend
against the risks of these models.
Everything that we do in our lives now
depends on software. Software kind of
ate the world. Every analog aspect
of our life is somehow
represented in digital domain. And so
all of our daily lives run on the idea
that we can rely on the systems that
power them. Cyber security is
the security of our society.
&gt;&gt; It is essential that we come together
and work together
across industry to help build better
defensive capabilities.
No single organization sees the whole
picture and can tackle this on their
own. This is not going to be done as
part of a few week program. This is
going to be the work of certainly
months, perhaps years. But what I do
hope is that at the at the end of this
we can be in a position where the
world's software, its customer
data, its financial transactions, its
critical infrastructure are safer than
they were before.
Reverse that and say attack.
What? As a software developer for the
past 10, 20, 25 years, do you need to
now look back at every code you ever
created because you know everything is
going to get hacked? Like
I know the code that I wrote last week
was
Oh, like it's it's
That's I don't know, man. Like all of
the legacy system and stuff, like
Yeah.
All the people who can't update because
they need to change so much, they have
so many bugs in it. Yeah, but like it's
not even you'll have to hack on it
because then it this AI will check your
it will check / attack your app
/
uh
you will have 1,000 other agents doing
the same
We're going to get DDoS'd by AI.
Yeah, everywhere. Yeah.
But yeah.
Well,
let's see if they ever make public or
they only hire a fair rented out to
companies and governments.
&gt;&gt; use software every day.
Don't want to hear you again. I'm good.
Uh the video was starting again. But um
I mean they have
I think we would have access to a model
that will have
uh
90% on SW bench verified blah blah blah
90% 95 99%.
Like it will always get better.
Yes.
So,
yeah, we'll  we'll we'll see
those numbers like
like 100%.
But um yeah, what does that mean when
everyone has the same cap I mean
um
Yeah. So, you just need to know how to
use it. That's it.
But I but like
And we're using it for the last two two
years, three years now, every day.
Yeah, we are way ahead of everybody
who's just starting.
Yeah.
I I I
even like people
who didn't start it.
Yeah.
The people who are still coding
manually.
Bro.
Yeah, I know people. Yeah, me too.
I don't know. Those uh
yeah, those team are not
with us anymore.
Yeah, yeah.
&gt;&gt;
&gt;&gt; I don't know. And you Everybody uses AI
now, but that's not the case. Yeah, I
yeah, not not everyone. Like even in the
dev like I think it was
72%. I saw that in a tweet on the while
preparing the show. That was like 70 70%
of the dev
are using AI every day. But why is that
not 100%?
Yeah, I don't know. I don't even
remember how I worked before AI.
Yeah, it just took so much longer. I got
the
Like
Yeah. Only thing you need now is to
understand the problem. Yeah. Not
to be able to fix it.
You just ask the AI to give you five
solutions on how to fix it and then
filter out the best one.
Yeah.
Yeah, exactly exactly. And honestly it's
it's it feel like coding talking to
eight different
cloud provider.
So, I still have the same like building
vibe stuff. Except now I say, "What the
have you done? Have you done? Why
is that not working?"
&gt;&gt;
&gt;&gt; Yeah. Yeah. So, the question is how long
is it going to take before everything
gets hacked? Or will
everything be fixed before?
Or do you even think that the model can
be this good?
Oh, yeah. So, yeah. So, first yeah, 100%
it's it's like a video announcing the
model, right? So, they probably sell it
like good. Plus, if you don't have
access, you can't really verify it,
maybe.
Um
Yeah, the problem is like okay,
uh
Anthropic is no god and they're going to
give
access to the super model to their
friends
or who paid the most.
Yes.
We're going back to  like a king
and peasants
society.
Yeah, so just make sure that you know
how it works and you can use it optimal.
And if you're in a company who has it,
let us know.
Yes,  please
comment in chat.
Comment below the the video.
Um yeah, I I could see a a society when
we trade tokens.
Like computer power.
Yeah, yeah.
Instead of money. Yeah.
Energy resources. Yeah.
And
I mean yeah, you you you use dollars to
buy a Anthropic subscription, but why
not trading
Anthropic tokens? So, then our new job
will be to optimize everything and make
sure people use Yeah.
as low amount of tokens as possible.
Exactly.
And uh make sure like you don't use
paper clip.
Yeah.
&gt;&gt;
&gt;&gt; It burns everything, all the tokens.
No, that's
I mean 100% I can know in a company who
haven't goes like via API access and
stuff. Like if you can optimize that,
um
or you can have a model that optimize
your consumption too or like better
memory and stuff. Like
Yeah, I know. It's
just
that's
Yeah, so
to ask you the question, what do we
think of it?
What is our conclusion?
Um
I I don't know. I'm speechless a bit
like
&gt;&gt;
&gt;&gt; Because yeah, like the model again, like
the model is like really really good. It
If the if the benchmark are true,
uh those numbers,
that's crazy.
Uh so, that means even like without
talking about security and okay,
reasoning
reasoning. Okay, Mito's preview. Okay,
so that's less humanity last exam A.
Agentic search.
Mito prose comp. Okay, West World
verified. Yeah, okay. So, it's less uh
impressive. But like for example,
uh yeah, the first one, right? Uh bench
pro 70 from 53. Who is what you know
about Opus 4.6 and Opus 4.6 is at 53
and Mito's is at almost 78.
Yeah, that's a big one. That's uh
I mean
that's massive.
And it's
it will only get better. So, maybe it
was not the worst week at Anthropic at
the end of the day.
No, no, no. I think they
they are still doing good.
Do you think their leak were like a
marketing stunt when they leak some
documents to prepare that? Everybody was
talking about Anthropic and everybody
found Mito's name. Yeah. And now they
now when they push the the blog live,
everybody knows what it is and is going
to read it.
Yeah, yeah, but like
it's a weird stunt because it's like uh
it's a mi- it's supposed to be a mistake
about a model that is about security.
It like the narrative is weird as
Yeah, I don't think people care. Yeah.
Yeah, I
yeah, maybe maybe I I don't know. But
yeah, okay. So, yeah,
now to so, tomorrow we live in a Mito's
world where everyone can
find security
bug. Mhm.
Are we getting Yeah, are we getting
attacked every day?
Yeah, we will. But on the other hand,
it also is a big opportunity. Oh, for
sure.
I mean, yeah. You you can you can't do
anything about it anyway, right? You're
not going to stop it. You have to
embrace it, right? Like you have to ride
the wave.
So, first of all, just make sure that
your own code is optimized and you find
every leak that you ever created and you
solve it.
And after that, people can contact
contact us and we will fix it for them.
Uh may may uh please give us a key a
Mito's key. We need a Mito's key. Yes.
We are going to make the whole internet
safe. Yes, again.
&gt;&gt;
&gt;&gt; Again, one more time.
Okay, so yeah, that's a great
conclusion.
Yes. We should wrap it up. Okay, thank
you. Thank you, Michel, for your time
again. And uh yeah, everyone in the in
the comment section, if you like the
stream, subscribe. Uh yeah, like the
video, subscribe to the channel, follow
us on Twitter because
uh yeah, we are big Twitter guy now.
And uh yeah, see you next week.
See you next week.
Cheers.
