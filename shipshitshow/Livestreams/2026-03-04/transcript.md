# Transcript

[[shipshitshow/Livestreams/2026-03-04/overview.md|<- Back to video]]

## [LIVE] Software Engineering Is DEAD

![[thumbnail.png|640]]

### Context

- Parent: [[shipshitshow/Livestreams/2026-03-04/overview.md|[LIVE] Software Engineering Is DEAD]]
- Description: [[shipshitshow/Livestreams/2026-03-04/description.md|Description]]
- Thumbnail: [[shipshitshow/Livestreams/2026-03-04/thumbnail.md|Thumbnail]]
- YouTube: https://www.youtube.com/watch?v=adYWnWTJibs

### Source

> Auto-imported from YouTube captions.

### Transcript

Cool.
Okay. Welcome back on the channel.
What's up, Michelle?
&gt;&gt; Yes. Yes. How are you?
&gt;&gt; Good. Uh, living my best life. Living
the the best timeline, man.
&gt;&gt; Yeah. Having so many AIs working for
you.
&gt;&gt; Yeah. Uh, yeah. like still like trying
to set them up like to not burn too too
much credit too much token because bro
like I'm uh I have like a enterprise
account on Codex and uh it's uh I think
it's too small
but I'm sharing with my girlfriend so
there's that and I I need but I need to
either buy more credits or have my own
personal 200x
account. Yeah, tell her to watch this
show and we will explain on her how to
not burn tokens.
&gt;&gt; She maybe she's watching. I don't know
but because she talked she talked about
it uh like 30 minutes ago but um yeah so
there's that and uh I'm trying to set up
like the free version of the open source
models on open but uh
not model
&gt;&gt; uh Gwen 3.
&gt;&gt; Mhm.
Uh so Sony 4.6 is trying to manage it by
itself but um it's
&gt;&gt; how long have you been trying to install
it because everybody on timeline says oh
it's like two minutes.
&gt;&gt; Yeah. Yeah know. So yeah in install it
it's fine. You you tell Clo to install
it then 15 minutes after it's done. Mhm.
&gt;&gt; But the orchestration between like um uh
like the the closed the closed source
models and then like triggering it uh
doesn't work like out of the box like
that. It's uh I mean not for me at least
like the first um tries was about
um I had a prom for it
&gt;&gt; and then Sony told me that um it just
say the prom back
&gt;&gt; but you can screenshot your installation
approval and just tell the world that
you did it.
&gt;&gt; Yeah, exactly.
&gt;&gt; But the actual news
&gt;&gt; I think it's basically what happened.
Yeah.
&gt;&gt; Yeah. You just like you just like
download um just download it, show the
the space on your hard drive and then
that's that's it. You have like
autonomous agents.
&gt;&gt; Yeah. Yeah. And otherwise use the answer
as a prompt and you can show people that
the answers.
&gt;&gt; Exactly. Yeah. Know exactly. But uh
yeah, other than that it's it's uh sort
of going okay just burning too much
token like uh yeah it's like when it's
too much autonomous like so I with son
and uh so I've done downgraded from open
uh from open opus 4.6 to son 4.6 on the
um on the open close setup because it
was building like too much too fast. uh
burning too much token uh on my
subscriptions. Oh, no, not on my
subscription, on my API keys. I'm using
API keys. Yes.
&gt;&gt; So, that's expensive.
&gt;&gt; That's that's really expensive.
&gt;&gt; Even not the incoming tokens, but the
outgoing tokens back to you.
&gt;&gt; Yeah.
&gt;&gt; It's like five 5x, right?
&gt;&gt; Yeah. No, it's Yeah, it's 5x more
expensive with like obus. It's just
mental like for example like um a
refactoring of a feature.
&gt;&gt; Mhm.
&gt;&gt; That's expensive
like because it goes into the whole
codebase and stuff. So I I think like
Yeah. Okay. So we're going to talk about
that but like software engineering and
like um orchestration is basically
managing the token and having the best
output
&gt;&gt; based on the output on the input and the
prompt that you have and the scope of
the uh issue. That's basically software
engineering right now.
&gt;&gt; Yeah. Yeah. Yeah. Making sure that you
stay within your context window
&gt;&gt; and be as cheap as possible.
&gt;&gt; Yeah. Exactly. like optimize the output
for the amount of inputs you know it's I
like it. Cool. It's cool. What about
you, man? What have you been done in the
last few few days?
&gt;&gt; Yeah, I've been setting up my my agents
and I'm trying to figure out how uh what
parts need to be sent to the AI and what
parts can we do with Python script or
whatever because repeating task
&gt;&gt; it is a waste of tokens if you keep
sending them to the AI.
So it is just adding skills and within
the skill creating the Python script or
whatever.
&gt;&gt; Yeah.
&gt;&gt; How do you pro productize that like
because there's business here?
&gt;&gt; Yeah. Well, that's a secret source,
right?
&gt;&gt; I mean, but yeah, like your skill and
all of that. It's that like the skills
of the AI, the setup, blah blah blah.
The productization of the open claw is a
business person like a like not for
sure.
&gt;&gt; Yeah. But it is yeah I've seen people
doing it manually and thinking about
everything but I just like to ask cloud
code hey see result what could we have
done locally sending it to an AI? What
is like static data that we can process
ourselves? How do we do it? And then it
will just say, "Hey,
&gt;&gt; we can do a Python script."
&gt;&gt; Yeah.
&gt;&gt; And if I say build it into a skill and
only trigger it when needed because you
want to have the context window as small
as possible.
&gt;&gt; So otherwise you can't scale your
company because people can say we have
five agents but you only have a context
window of 200,000 tokens, right?
&gt;&gt; Uh
but you have a context window per agent.
&gt;&gt; Yeah. But still if you keep processing
it locally and then send it as one big
prop that's not good.
&gt;&gt; Yes. Yeah. There's but that's why like
we have layers as open. I expected that
to do it for me.
&gt;&gt; Yeah. Yeah. But you need to set it up
properly.
&gt;&gt; Yeah. No. No. 100% 1%. I mean, yeah,
it's um so yeah, you have agents that
have the same context window, but then
they if they use the script to run a
chron job, then the chron job is a
script on the hard drive like like a
hard disk hard drive. I don't know what
English, but uh um then it doesn't use a
token except
&gt;&gt; Yeah, you froze. Oh, am I still frozen?
&gt;&gt; No, no, no. Not anymore.
&gt;&gt; Uh, fast.
Did I?
&gt;&gt; Yeah. No, I'm good. I'm good. I'm good.
I'm connected to internet. Let's go.
&gt;&gt; Cool.
&gt;&gt; Yeah. And the fiber. Okay. So, should be
okay. But yeah, I got some issues before
the stream, so that's not fun. Uh, tag.
Oh, we on the on the channel. Let's go.
Are we on X?
&gt;&gt; Yes, I'm streaming to X.
&gt;&gt; Nice. Okay. Oh, I'm going to don't
Okay, sound is okay. Okay. Okay. Let's
go. Let's go.
&gt;&gt; Let's go.
&gt;&gt; Okay. So, I'm going to do the
introduction. So,
because uh that's that's why people are
clicking.
&gt;&gt; That's good, right?
&gt;&gt; Yeah.
&gt;&gt; Getting ready.
Software engineering is dead. And you,
if you haven't lost your job yet, you're
g it's happening. It's happening in the
next 12 months. We got  Everyone
is  Oh, no. I can't say that.
It's not good.
&gt;&gt; Rewind.
&gt;&gt; Yeah, I can't say that because it's it's
too fast. They can say  in the last
in the first 10 second. Okay, do it
again. Okay.
Software engineering is dead. And if you
are uh if that's your job, you're going
to lose it in the next 12 months for
sure. Like Dio from Entropics said that.
So yeah, it's happening. And Jack, the
ex CEO of Twitter uh basically fired 40%
of his company even if the company is in
a good shape. So we cannot expect uh No,
that's not good. Whatever. We cannot
expect more people, more CEOs to do that
in the next few months. And yeah, that's
uh that's why you are going to lose your
job. But maybe there is hope. Maybe we
can find some ways of like working
differently.
Transition addition blah blah blah.
&gt;&gt; So that was it.
&gt;&gt; Yeah.
&gt;&gt; Thanks everybody. Bye.
&gt;&gt; I need to repro my introduction.
&gt;&gt; Yeah. Well, you have a whole day for
testing tomorrow if you want.
&gt;&gt; Yeah, that's okay. I can edit. But yeah,
being a streamer is hard. It's hard.
It's really hard.
Uh but okay. So that's uh tech. Oh, can
I also change the views? Wait. Yes,
that's going to be can have bigger
faces.
Okay. So puff puff. Nice. Cool. That's
pretty.
So yeah, last week Jack uh CEO of Bloxs
founder of Twitter uh posted this tweet.
Did you read it, Mitchell? Like are you
aware of it? Yeah, I've read it.
&gt;&gt; Yeah. And that's
&gt;&gt; and it was so much I forgot it. But
&gt;&gt; I have I have the conclusion.
&gt;&gt; Uh okay. So today we are making one of
the hardest decision of the history of
our company. We are reducing our
organization by nearly half from over
10,000 people to just 6,000. That means
over 4,000
employees of
because it was okay. It was a not for
the employees itself. So uh that means
over 4,000 will be asked to leave or
entering into a consultation. Uh I will
be straight about what's happening. So
which is cool because it's not like
corporate  to say oh no like
it's not the fault of investors blah
blah blah like is owning the decision.
So like it's kind of refreshing to see
that too, right?
&gt;&gt; Yeah. And he tells his people on like
you're losing your job.
&gt;&gt; Yeah. I mean they probably received a
note before and on Slack.
&gt;&gt; I hope so. so that you didn't sleep in
and and were late and that you open X
the first thing in the morning and see
oh
&gt;&gt; my job is gone
&gt;&gt; to to know what's happening in your
company you need to have like your CEO
on on X on notification
&gt;&gt; yeah exactly
&gt;&gt; or you can be a reply guy for your to
your CEO so you can get an an an
increase like get your paycheck
um okay so if you are one of the people
blah blah blah yeah compensation
whatever whatever I don't care about
that. Uh we're not making these
decisions because we are in trouble. Our
business is strong. Gross profit
continue to grow. We continue to serve
more and more customers and profit
profitability is improving. But
sometimes something has changed. AI we
have already seen that the intelligence
tool we are creating and using pair with
smaller and flatter teams are enable a
new way of working.
&gt;&gt; Yeah. So does it mean like they're
killing the management layer in between?
&gt;&gt; That's okay. It it doesn't say that it's
like yeah 4,000 engineers and dev. It's
like uh that's why I expect that that
basically you have the software
engineer, you have N plus one PM, N plus
the manager of PM. Those guys are gone.
&gt;&gt; Yes. You only have HR.
&gt;&gt; Yeah.
You have you have the dev and then you
have HR. Yeah, exactly.
&gt;&gt; Good luck to them.
&gt;&gt; Um, yeah. Okay. So, that that's
basically the news. Um, creating which
uh blah blah blah been built to run a
company that rapidly whatever. Uh, I had
two option cut it gradually over months
or years or doing all at once. Doing it
now. Uh, repeating around blah blah
blah. Okay. So, I think that's it.
decision is carry risk. Okay, fully
review. Um,
okay, that's uh we're going to do a
Slack has a bye-bye party
and I think that's it. Yeah. So
basically
cutting 40% of uh your uh company
because everything is going well but
everything could be better and the thing
is like uh in the two days after stock
went up.
&gt;&gt; I don't think he we he regretted a lot.
&gt;&gt; Yeah. No, exactly.
&gt;&gt; He he made a lot of money on it.
&gt;&gt; Block stock.
Uh,
that's not that this one.
&gt;&gt; Mhm.
&gt;&gt; Yes,
&gt;&gt; that's the one.
&gt;&gt; Yeah, that's the one. Okay. So, amounts
of that that's
XYZ. Yeah. Yeah, that's a block inc.
Yeah, that's that's that's this one.
&gt;&gt; So, that was the moment of the post.
&gt;&gt; Yes.
&gt;&gt; And a few minutes after.
&gt;&gt; So, Thursday 400 p.m. 26.
Nope. Not this one. And this one. Yeah.
Uh 26
10 p.m.
Oh, maybe. Yeah. Okay. So, maybe that's
the when the people knew about it, the
employees and then the post on Twitter.
Um
but that like the stock price
is telling us that it's a good decision
and the markets love that and the market
is seeing the future of all of the
companies doing the exactly the same
thing.
&gt;&gt; Yeah. So that the market is rewarding
the companies that actually do something
and not the SAS companies. They are
crashing. But these
&gt;&gt; Yeah.
&gt;&gt; these are scaling up.
&gt;&gt; Exactly. And uh like
another another company that went
obliterate obliterated
&gt;&gt; because of uh AI
&gt;&gt; is Monday.com and that's brutal. So in
uh the the stock was around 400 bucks
and now it's sitting at 70 uh dollar 75
and June yeah see like June July 25
that's basically
would that be like chat GPT no not 3.5
but which model was it at that time
maybe four right
&gt;&gt; yeah I don't know out of my head but it
was
&gt;&gt; and you can see it in the stuck.
&gt;&gt; Yeah. And uh so that
20 pieces.
So I watched this video from the 20 VC's
uh podcast.
Uh no, too much stuff. Uh what can I
&gt;&gt; Yeah. And June was the 03 pro model.
&gt;&gt; 03. Yeah. So the reasoning model then um
and so monday.com co went to um the
podcast on 20 VCs and um Harry is
interviewing about like bro what are you
going to do etc etc and I didn't find it
that it was really really good and the
answering because they're still trying
to figure out like for example in his
answers he said that um
uh we are going to hire like we have
hired a lot last year we're probably
going to reduce it. Um, but I don't want
to cut it too fast because we're still
trying to figure it out and etc etc. But
then you have like Jack do say like
decision where everything is going way
faster and the market reward the company
of like 20% up.
&gt;&gt; Well, the new ads for monday.com that
were on my social media that they were
showing me, they had a reason to sell
it. We are now including AI tools.
&gt;&gt; Yeah,
&gt;&gt; that's it. nothing else. And honestly,
the monday.com features that I did use
uh not by them but through others.
&gt;&gt; Mhm.
&gt;&gt; I had opus code them in one day.
&gt;&gt; Exactly.
&gt;&gt; And even integrated with my ticket
system and everything. So why would I do
the entire setup on Monday.com?
&gt;&gt; No. Exactly. Right. There is a lot of
SAS that can be bcoded and being an
equivalent of like a macro micro SAS for
individuals. Yeah. Like it's it's really
a ship.
&gt;&gt; You had different choices why you took a
SAS, right?
&gt;&gt; Again,
&gt;&gt; you have different choices why you made
to choose for a SAS. One option was it's
too complex for us to build, so let's
pay for it. But the other one was it is
taking too much time for us to build
&gt;&gt; and to keep updating and to make sure
that we have new features. So let's just
pay them like 20 or 30 dollars per
person.
&gt;&gt; But right now doing it in a day. All
those companies that don't have the
complex SAS but have the SAS that just
took too much time those are gone.
&gt;&gt; Yeah. No 100%. And like uh especially
when you have to sell per seat
&gt;&gt; when you have like 5,000 employees and
30 months
&gt;&gt; like that.
&gt;&gt; Even if the IT guy says it's taking
three months and he takes a leave after
three days of work and does it in three
months, nobody's complaining.
&gt;&gt; Yeah. Exactly. And especially like um
when you have like other
like that saying that yeah software
engineering will be solved in like six
to 12 months and um uh yeah Opus will do
all of the engineering uh lead work. So
&gt;&gt; yeah but then I have a question for you.
&gt;&gt; I still see companies who don't use AI
at all. They still have the devs. They
develop everything. So what what do you
think that's going to happen? Are they
eventually going to switch or are they
going to go bankrupt because other
people do it better with AI?
&gt;&gt; So
two things. First, I think it will take
more time that we think it will take.
Like for example, for me like all
software is dead like in six months. It
will probably take like two, three, five
years. But it will it will be faster
than the last 20 years of like uh the
SAS era for example like where we went
from like a personal computer plus uh
you need to install a software on your
computer to then the web and it took
like decades to to do that right so I
think the truth is is in the middle I
can see it still go faster than again
like five years but yeah like honestly I
don't have I have no idea what's going
to happen in the next six months. So
yeah, it's really it's really hard to
say, right?
&gt;&gt; But um still like I don't um and the
second point would again like to
companies who have a business unit uh
that is not like just having a software
or like a legal work or stuff. They're
not I don't think I don't think that
they're going to um v code a lawyer is
not going to vibe code or the majority
of the lawyers are not going to vibe
code a software and maintain it.
&gt;&gt; Mhm.
&gt;&gt; Even if
um there is a code who can uh maintain
it for for them. I
like the level of intelligence that will
required
that will be required for the AI to have
we are still
like a few years away from that for sure
because like for example even for open
claw like um it's not just you install
it and then it's done like uh I have to
go into my uh cloud CLI to fix open claw
every day.
&gt;&gt; Yeah. Yeah. even to update it because it
can't update itself because it needs a
restart.
&gt;&gt; Yeah.
&gt;&gt; But yeah, I think so. So maybe the first
step is a lot of devs who find a way to
create a perfect skill for example for a
lawyer
&gt;&gt; to do some of his task automatically
with an AI. So it's more like selling
skills and selling of a SAS.
&gt;&gt; Yeah. But like
Yeah. But like the the work of a lawyer
from one film to another, I don't think
they work the same way for example.
&gt;&gt; No, they don't. Not every everyone. And
if they have a different field or
something, then it will be more complex.
&gt;&gt; Yeah. But if if AI is able to harmonize
all of the lawyers
job that would be massive.
&gt;&gt; Yeah. Because like what what's a lawyer
in Malta will be different from
Netherland for example except the laws
but the laws is like a database
connection with like text file. So
&gt;&gt; you just need a good index.
&gt;&gt; Yeah. Exactly. just but yeah basically
yes but like companies like Legora and
stuff are working on that like having an
AI and LLM that is purposely focused on
laws and have the data and all of the
jurist prudence of everything to
just offer the AI for lawyers.
&gt;&gt; Yeah. So that will be the new size
because that will be too expensive to
create yourself
&gt;&gt; like exactly and for example for gen
like since last week like um I've I've
implemented like the uh intelligence
layer of having even like the all of the
trends that everything like that goes
from all of the platform uh all of the
the the trending video trending
topics that I can for the
And then um I can remix the content
based on those trends but like
completely autonomously with like an
open close orchestration
um and but it will it will build the
data set for the um
LLM models um
for content creation. Yeah, I think
that's a perfect example because people
will say, I can create a video myself,
but when you start to scale, you need to
automate so many things and people
didn't think of yet. And that's why it
took so much time to build.
&gt;&gt; Yeah.
&gt;&gt; So, if you can offer it like a plugin or
something that people can use.
&gt;&gt; Yeah.
&gt;&gt; Yeah. Then that's worth the money.
&gt;&gt; Yeah. Exactly. And even like Yeah. like
you you you
log into the software, you connect to
Instagram and then it's like pre-build
um your next 20 post because it can
analyze and again based on the trends
that you have blah blah blah and then
you prompt
&gt;&gt; 20 pictures without any prompting
anything. It's just like AI
orchestration behind the hood.
&gt;&gt; It's even more powerful than that. So
even if like yeah you go to a lawyers
and then you drop one prompt of your
issue to the lawyers and then like you
have the whole case built for you done.
&gt;&gt; Yeah. Instead of spending like 50 hours.
&gt;&gt; Exactly. But but that like what does it
mean for like software engineering per
se? Um yeah. What what do you build?
&gt;&gt; Yeah. It just changes the way of
building.
&gt;&gt; Yeah. Know 100%. Yeah. Yeah, we're
building software on Discord now.
&gt;&gt; Yeah, Discord, Telegram, doesn't matter.
It it works.
&gt;&gt; The bu building it like uh and
orchestrating talking to agent on
Discord. That's really powerful.
&gt;&gt; Yeah.
And I still think that everybody is just
reading X and thinks it's easy. But see,
I've seen a lot of people trying it and
struggling or stopping because it's too
expensive in API tokens.
I'm I'm like
I'm spending more per months in AI than
any subscription I ever have before.
&gt;&gt; Like the output is like
&gt;&gt; you don't Yeah. No, exactly. It's it's
not even like uh it's more it's
expensive because you have a good output
anyway.
Like it's expensive when you when you
pay for something and the output is
But it's like properly like if you
have like Yeah. Again, if you
&gt;&gt; pay for quality exactly and even like
with even without the quality if it's
like the cost of redoing it is free or
like close to zero then you don't care
if it's  because you can redo it um
again and again. And it just like while
you sleep the
when 3.5 run 25 times and it just like
take some compute power but you don't
care because it's part of your computer
anyway, you know. So
&gt;&gt; yeah. Yeah.
&gt;&gt; Yeah.
&gt;&gt; And so yeah, but like how how the how
the way you build software changed in
the last like since Christmas again?
Like what's the
&gt;&gt; it just keeps changing. It's insane. And
I think that's an issue for for many
devs who are just so used to working in
the setup that they always do.
&gt;&gt; Yeah.
&gt;&gt; And now I can just say, "Hey, do this
and try this and it's different." And if
they can't adapt, then Yeah.
&gt;&gt; But you cannot adapt as a dev
like like you you have to update your
package npm packages every day.
&gt;&gt; Yeah. Yeah. You do not adapt.
Like one of the most like adaptable prof
profession jobs should be dev.
&gt;&gt; Yeah.
&gt;&gt; The most flexible person ever.
&gt;&gt;
Oh
no.
Yeah. Well, I think it is.
&gt;&gt; Yeah.
&gt;&gt; You You should be able to change your
way of working every time. Yeah.
&gt;&gt; Because it will improve the output.
&gt;&gt; Exactly.
I know for sure
and especially when you go from like
codeex to uh opus to back to codeex and
all of the change like you go from dot
dot agent folders to prd on file and
then like for example for me like it
took I took a day just to upgrade
everything to GitHub issues again like
&gt;&gt; yeah have just a different other thing
because you're you're mentioning like
opus and CH GBT. Have you ever tried uh
planning mode and both for the same task
and see how they do a complete different
result?
&gt;&gt; Yeah. So what I did in the last few
weeks was to um
uh have a plan and I have a command to
CEX review to review the Opus plan.
&gt;&gt; Mhm. CEX jacket
and Opus is like repling after based on
the Codex uh updates.
&gt;&gt; Yeah. Yeah. Yeah. So I I did the same. I
had them made both both of version one
&gt;&gt; and then I gave the version ones to each
other and told use this to create a
version two and then I merged the
version twos into a final version.
&gt;&gt; Okay. So you you have two planes. You're
not reviewing the plan. You have two
planes. You merge the plan and it's
okay. Okay.
&gt;&gt; Yeah. Yeah. Because otherwise it's it's
only reviewing the the plan from the
other one. But it didn't have to think
himself.
&gt;&gt; Yeah. But I expect to burn less token
too.
&gt;&gt; Yes. But if you both let them do version
one on their own with the exact same
prompt, it will give totally different
results.
&gt;&gt; Okay. Okay. with Codeex I or and Opus
4.6 or do you even plan with Sony and
&gt;&gt; No, no, no. I just use all the the most
expensive models.
&gt;&gt; How do you not get limited? I don't get
it. I don't I don't understand. You're
coding as much as me and I have two
accounts. I'm getting limited after
three days. What the
&gt;&gt; Yeah. And I'm at 25%.
&gt;&gt; What the  But I spend a lot of time
in planning.
&gt;&gt; I don't let it just I don't let it go
refactor refactor refactor. I tell it
plan my refactor and I tell the same
thing to check GPT and then I have them
compare the refactoring debugging the
refactoring plan and when I think it's
done
I do one refactoring and then I have
them check my planning versus the
refactoring and do one debug.
Okay.
&gt;&gt; And that saves a lot of tokens.
&gt;&gt; Yeah.
&gt;&gt; Yeah. Because I don't do that.
&gt;&gt; Yeah. I I do it for everything. I think
most of my time like 80% working with my
AIS is planning.
&gt;&gt; But yeah, also like I think my workflow
will change when the SAS like with when
Genfeited will be stable
&gt;&gt; like more stable because I'm still
debugging and stuff. So I'm dropping
errors and stuff. um even like new
features blah blah blah um which I
should not add anymore but
&gt;&gt; no no it's best to have one stable
version
&gt;&gt; yeah exactly um and yeah and then build
on top of it for sure yeah
but uh yeah but right now it's still
green and uh yeah it's uh I yeah
and sometime I prompt yeah review the
codebase for any security issue
Yeah. If you do it branch by branch and
just one new feature, then reviewing the
code for security issues will be so much
cheaper on tokens.
&gt;&gt; Yeah. Yeah.
&gt;&gt; You only review the the the code that is
ready to commit.
&gt;&gt; Yeah. Yeah. Not 100%. Yeah. I need to
stop like working on the whole workspace
all the time.
&gt;&gt; Yeah. Yeah. For sure. Because even like
open CL, I think that  burns a lot
of tokens.
&gt;&gt; Yeah, it doesn't do it for me
&gt;&gt; because everybody is using heartbeats
and constant checking.
&gt;&gt; Uh I don't use heartbeats.
I only use web hooks.
I only wanted it to do an action and uh
burn tokens when it's actually needed.
&gt;&gt; Okay, you're right. Maybe I uh Okay, I I
had a flash about uh
per bit getting from 30 minutes to 5
minutes maybe.
&gt;&gt; Yeah, time six.
&gt;&gt; But I changed the model for
&gt;&gt; Yeah, you can still just set up a
cruncher. But that's why I like Discord
because I can have everything pushed to
Discord and instead of checking the
channel constantly, the channel triggers
a a sort of to the the cloud port a
signal.
&gt;&gt; So it only reacts. It never takes the
initiative to check if something is
needed.
&gt;&gt; Yeah, makes sense.
Okay. I I still need to do some
configuration. I can't wait to do the
the prompt like Yeah. Can you explain me
what's the architecture we have right
now because I'm kind of lost.
&gt;&gt; Yeah. Well, do you use Gabi?
&gt;&gt; Uh, yes. So, yes, I have I've migrated
all of the P on local to G is G github
issues and project because I have the
open CL on an EC2 instance. So I don't
have those on um on my local host and
also I had some issue with like uh
keeping them up to date. So now the now
the source of truth is the GitHub
issues.
So everything is centralized every and
so I can ask um I can prompt like uh
like the CTO on Discord to say oh yeah
uh uh check the issues and compare to
your localost version
&gt;&gt; um and then I can pick up the new
updated uh task uh on my own localost on
my computer etc etc. So
&gt;&gt; yes,
&gt;&gt; I like that. Plus like there is a couple
of like software
that I found like M dash. I didn't use
it at the end of the day, but they were
working on like GitHub issues and you
can run like the way the I think the way
you say maybe maybe you can try the the
ID but um
it works it it was working like it it
was taking a GitHub issue and then you
can prompt both um models at the same
time and exactly like to compare the the
the plan like you did. But um yeah, at
the end of the day, I didn't use it
because uh Terminal for me is doing it.
&gt;&gt; Yeah. Yeah, I'm using CLI a lot.
&gt;&gt; Yeah, 100%.
&gt;&gt; And I I even set up my own little system
that instead of cloudbot, I'm just using
my own Python script that scrapes an
inbox folder.
&gt;&gt; Yeah.
&gt;&gt; And does it in O to uh to CH GBT and in
O to cloud. So I'm not burning tokens on
all the coding.
&gt;&gt; Yeah, makes sense. And did you use CLI
before like pre AAI that much or where
you spending time in ID?
&gt;&gt; No, no, no. The only thing I was using
it for is SSH into serals to check logs
and everything. But coding like this, I
never did.
&gt;&gt; Yeah, that's nuts.
&gt;&gt; I I even disliked it because it was so
hard to one stupid typo and everything
is CLI. Then I just used auto sofa.
&gt;&gt; Yeah.
&gt;&gt; And I I I stopped all the subscriptions.
&gt;&gt; Yeah. Cursor like I I don't open like
Okay. I up I open cursor to see the work
trees and um which files have been
updated and if I have any leftover
branches and stuff like that. I like to
have the the the u the UI but I don't
know how cursor can
fight the CLI setup.
&gt;&gt; Yeah, I have not been using cursor for
like three or four months.
&gt;&gt; Yeah, that's that's bad.
&gt;&gt; I even find it confusing.
&gt;&gt; Oh yeah.
&gt;&gt; Yeah, it just shows me so much and then
it keeps switching and you have a
message here and a message there. CLI
just does it one by one.
&gt;&gt; Yeah. I mean, yeah.
&gt;&gt; Yeah. And other I I always tell him
every change that you make, put it into
an MD file and then I just have a full
MD file where I can say check this.
&gt;&gt; Exactly. No, I really like the
documentation inside the code. Like code
is documentation now.
&gt;&gt; Yeah.
&gt;&gt; Really powerful like it's it's really a
nice setup for sure. I love it. Um okay,
so yeah, software engineering. So yeah,
a lot of a lot of change, right?
&gt;&gt; Yeah, a lot of change. So I don't think
that that that the job of sofa engineer
will be gone, but I think it will change
and less people are needed to do the
same job.
&gt;&gt; Yeah. Do you believe like uh we need a
company with like 5,000 engineers? How
do you work in a company like that?
&gt;&gt; Yeah. I don't know. I I think it they
don't even notice if some people don't
work. who want to
&gt;&gt; but yeah imagine being the person
responsible for merging every branch.
&gt;&gt; Yeah. Like how do you how do you push a
feature on Facebook
when you have to have five review peer
review before you update a  icon?
&gt;&gt; Yeah. I just think a lot of dev servers.
&gt;&gt; Yeah. Like Yeah. It's nuts. And like
so Okay. So if there is like less um I
think it will we will have like less
developer in one company but I think we
will have more companies.
&gt;&gt; Yeah. Yeah. Yeah. And more dedicated
companies because still if AI keeps
going in this space and you need to make
sure that you understand everything and
know how it works, set up skills,
improve it and so much stuff is coming.
There will be more dedicated companies
of like just a few people who can advise
bigger companies.
&gt;&gt; Yeah. Yeah, but like also like
Salesforce will fight his way to survive
too, right? So yeah,
&gt;&gt; how okay imagine you are the CEO of
Salforce. What do you do at the AI age
now?
&gt;&gt; You just scale up and you scale up and
give everybody an AI. Let them create
the idea. see what sticks and even if
you kick like 50% of your devs out, but
if you can do a 3x and that's small, if
you have a dove understanding AI and
working full-time, he can do 10x of his
output.
&gt;&gt; But if you take half of your staff and
do a 3x, that's a 50% growth.
&gt;&gt; Yeah.
&gt;&gt; Yeah. And then just keep scaling and
keep automating and setting it up and
just improving and create a dedicated
team who just are working on the newest
technologies and make sure you're the
first on everything.
Yeah. And especially like when you you
pay like
Silicon Valley engineers and these
are are taking like half a
million. That's a  ton of token.
&gt;&gt; Yeah. Well, I still think they are
overpaid by a lot.
&gt;&gt; Oh yeah. No, for sure. I mean,
&gt;&gt; they're smart.
&gt;&gt; Yeah, they're smart. But honestly, kick
them out and and just take a deaf that's
taking like 100k and that's still a lot
in many com many countries
&gt;&gt; and then like your Dave hates you and
then he's is going to build an AI
company just to  you because he can
and he has all of the knowledge.
&gt;&gt; Yeah. Yeah. Yeah. But that's a risk of
every deaf right now.
&gt;&gt; Exactly. Yeah. I mean like the
open cloud dev got sign up for like
potentially 1 billion. I don't know if
this number is still um true but um yeah
if if you pay one dev 1 billion like the
output required
to uh to get to pay like I would be
stressed.
&gt;&gt; Yeah. You would go nervous to work every
day but on the other hand would you go
working for a big company again?
&gt;&gt; Yeah. if they pay you enough.
&gt;&gt; Honestly, I never worked for a big
company like um so what did I do? Yeah,
the biggest ones was like one of the um
so Sachi and Sachi it's like a it was it
is still in New Zealand where um I was
doing like ads but I was doing like HTML
banners ads. I I was doing like drag and
drop.
&gt;&gt; Yeah. And but like that paid well. So I
did that for 10 months and then I said
bye-bye. But um they had a guy it was 10
years ago but they had a guy a flash
developer.
&gt;&gt; Oh
&gt;&gt; they were doing like some
&gt;&gt; adult flash.
&gt;&gt; Yeah.
&gt;&gt; But bro like it was so three dev
counting these guys. So even like one
back end and me to manage all of the ads
that require that needed to be like
banners in HTML
like you know the one that I don't see
at all because I have ad blockers so I
never saw those ads whatsoever like for
the for the last 15 years and they
haven't had a a conversion rate of like
0.3% and they were happy with that.
Well,
&gt;&gt; depends on how how many views you have.
&gt;&gt; No, I have
&gt;&gt; but on this I I I don't have a tier, but
I've read today a topic on X for
somebody saying that he built like a
full affiliate flow with open glow.
&gt;&gt; Yeah. building banners, building landing
pages, promoting it, taking the the
programs in, switching everything to
different programs, optimizing and
getting leads and sales in
&gt;&gt; I it's a it's a X rate, right? So, it
can be something that only run on local
and that's it, right?
&gt;&gt; Yeah. Yeah. And he he he does it by FTP
uploading everything.
&gt;&gt; Exactly. But uh yeah, I know 100% like
um again it's like you know it's a parto
um parto scale like you do like 80% of
the of the app in like one afternoon and
then like the 20% will take you six
months to get it right.
&gt;&gt; Yeah.
&gt;&gt; But um no no like 1% like I think that
being an independent developer
it's it's a massive play right now. Like
where we are right now, it's perfect.
Like we we we we can scale our revenue
by uh a lot.
&gt;&gt; Yeah. Yeah. You just need to do it.
&gt;&gt; Yeah.
&gt;&gt; And don't spend like 50 hours like we do
on optimizing open claw.
&gt;&gt; Yeah. But it's fun, bro.
&gt;&gt; Yeah. Yeah. That's the issue. But on the
other hand, I am really sure because
I've had multiple conversations.
&gt;&gt; Yeah. And every time they have like a
real expert and he's doing stuff that we
were doing like four, five months ago
and it's already old.
&gt;&gt; Yeah.
&gt;&gt; Yeah. But also like the fact that if you
are at the cutting edge of like the
setup and stuff once you have a good
model like once we have Opus 4.6 but
open source
&gt;&gt; Mhm. And it will unlock like crazy uh
crazy output for sure because even if
like Entropic drops uh Opus 5 and we
have open source Opus 4 4.6 that's
that's a very good
&gt;&gt; it's good enough.
&gt;&gt; Exactly. Like it's going to be it's
going to be massive. Um
&gt;&gt; I'm stacking magnis. No, no. Yeah. No
one like um Yeah. I like the the next
six months will be amazing. But like if
every dev can have six max mini Mini at
home and like five Dave on Mac Mini
competition would be interesting.
&gt;&gt; Yeah. Well, yeah.
&gt;&gt; Yeah.
&gt;&gt; Let's see.
&gt;&gt; Yeah. Let's see how it goes. Uh, okay. I
think we do do I I think I have enough
stuff to uh make a video out of this
live stream. That's going to be cool.
&gt;&gt; Junior, stop optimizing your blah blah
blah blah blah blah blah blah blah. Oh,
yeah. Okay. Okay. Okay. Conclusion. So,
if you are a junior software developer,
what would you do right now? You start
working like Monday, what's today? Uh,
Tuesday. Next week, you have your first
job. What do you do?
&gt;&gt; Uh start for yourself. I make sure that
you take like jobs where you don't know
how it works and that you have like
crash course in learning how everything
needs to be set up, how a normal company
works with it and how to automate it.
&gt;&gt; Don't go to school and do everything old
school because they are already behind.
&gt;&gt; Is that what you say to your daughter
that stop going to school?
&gt;&gt; No, no, no, not yet. But I have some IT
people here who go who are in a second
or third year of a foury year uh
university school for for it and the
teachers are still saying no no no you
can't do everything with AI because you
need to know how it works
and then I tell them well you can also
have AI explain it to you
&gt;&gt; because when you're done with school in
two years
everything that you do right now in
school is already not done by anybody
anymore
&gt;&gt; and and and yeah and you can turn like
CEX learn and then learn programming
there and replace your teacher anyway.
&gt;&gt; Yeah. So just take every project you you
can do everything right now. I'm writing
coding languages. I never did and I'm
doing it perfectly with AI
&gt;&gt; or at least you're not aware it's it's a
it's wrong code but at least you know
&gt;&gt; No, you can have it checked right
and Okay. And as a senior software
engineer, what would what would you do?
How do you approach that in a big big
corporation company and stuff? Yeah. Ju
just get as much paid in salary as you
can for as long as it's as it's going to
be.
&gt;&gt; Yeah.
&gt;&gt; Okay. That's cool.
&gt;&gt; Don't sell don't move out.
&gt;&gt; Yeah. Yeah. Be the best one in the
company because otherwise somebody's
going to replace you with AI.
They always need like one or two people,
right, who operate the AI.
&gt;&gt; Yeah. Yeah. Yeah. If there is like two
person who have the same job in your
company,
&gt;&gt; you're screwed.
&gt;&gt; Have you watched Hunger Games?
&gt;&gt; Yeah. Here is a sword. He has a chill
shield and choose
&gt;&gt; 100%. But okay. Should we wrap it up
here?
&gt;&gt; Yes.
&gt;&gt; Nice. Okay. So, thank you everyone. Oh,
is that you to drop a message?
&gt;&gt; Did I? I already did at the beginning,
right?
&gt;&gt; Okay. What's up, Greg S? Greg. Yeah,
Rick, thank you.
&gt;&gt; Oh, no, that's my dad.
&gt;&gt; Oh, nice.
That's nice.
But, okay. So, thank you, Michelle.
Thank you so much. And everyone uh live,
subscribed. Um, I subscribed and thank
you for watching.
