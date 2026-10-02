# Livestream transcript

29 September 2026 · Vincent and Mitchell · Original recording: 48:36. Automatic local English transcription. Common model-name recognition errors corrected; some wording and numbers may still need checking. No speaker assignments have been inferred.

**00:00:00**

[Music] [Music] [Music] [Music] [MUSIC PLAYING]

**00:00:33**

And welcome back, everyone. Hi, Vitor. Been a minute. Yes, hello. Sup, sup, sup, sup, sup. I think everybody was missing us, right? Yes. I mean, we are like-- the channel is growing, man. Oh, yeah, it is. So that's good. Just going to check if YouTube is good and have the sound, because with all of the chat before, I don't know if we are correctly set up,

**00:01:00**

but it should be fine. Okay, now-- - It didn't start on YouTube yet. - I have it, but I don't have the, I think-- - Now it is. - You have it, you have the sound? - Yes, now I have it, perfect. - Okay, cool, so because I didn't have the output. So cool, okay. Nice, how have you been since the last time we chit chat? - Yeah, well, there is so much to do, so many new models.

**00:01:32**

So I've been good, I've been testing, coding, working with AI, doing so much more. And how about you? - I mean, so I take a little holidays off, completely without any internet and stuff like ish, just enough to trigger some prompt and issues and stuff. on the side, but yeah, like, and then we come back and then we have a release model every day. - Yeah, the entire landscape changed, again.

**00:02:03**

- Yeah, and for the best or for the worst, the pain of the model. - Well, you need to work differently every time they release a new model. - True, and that's more true with like Opus, and we're gonna talk about that later on. But first, yeah, let's start by chronological order. Review everything and then like the answer is like, which one is the best of the last week.

**00:02:33**

So yeah, if you want to know which model you should use, stay until the end. - We will tell you. - It's gonna surprise you. Turk, okay, that's you in the chat. Let's go. Let's go. So perf on the 22, perf, perf, I'm gonna share my screen, show intelligence. So the first one who released a new update for the model,

**00:03:05**

it was a GPT-6 Sol and Luna push, so from OpenAI, push the cost efficiency frontier by having the cost relative to 5.6 and Luna, pricing approximately half of GPT 5.6, drop to Sol, drop to 420 to 210 per million output tokens and Luna from 20 cents to 120 to 10, 15.

**00:03:36**

- That's nice, that's very different. - I mean, that's good, but did you get the same output? Did you try to use them and? I just did some random tests and I got some good outputs. I could not complain, but I don't use these two models a lot. - Yeah, something like for my Codex subscription, I do a lot of Astra still. - Yeah, yeah, the same. And I think they reopened the $200 sub again yesterday,

**00:04:03**

right? - You didn't get it before? I think it was for the new user, no? - Yeah, but I don't have it because I downgraded and especially when I wanted to upgrade, I was just like six hours too late. - Yeah, but like when I think I told you, right? Like it was back, no? - You told me and I was like, ah, don't worry. I have a few days and I was too late. - Oh, so I told you, you didn't do it immediately

**00:04:31**

and then they close it again? - No, no, no, just a few weeks ago they closed it. So I still didn't get it. - Yeah, okay, okay. But yeah, like, so tonight at 8 p.m. Europe, like they have the open the Dev day. So I'm expecting a lot of announcements like maybe whatever I saw on the timeline like 20 announcements, et cetera, et cetera. But Arisette. - Who knows? - Yeah, and did you see the Cibo post?

**00:05:01**

- Yeah, about the difference in the new model of having a new subscription. - Yeah, tomorrow we are reopening the Pro 200 sub to new subscribers. That's why I was saying like, maybe you could take it before because it was for the new subscribers. - Ah, well, I think, oh, for new. So maybe I can, okay, I need to try. - Yes, I think you can upgrade. I don't think you can go from GPT-free to 200 sub.

**00:05:31**

I think that's the twist here. But okay, together we're also changing how we calculate the usage for it. If we do the math, you will net out at half a dollar in API spend compared to the old 200 plan. Wait, what? It will net out at half the dollar in API spend. Oh, OK. So you get 50% less. Yeah. Now that said, let me explain what is happening and why you will get more work done. Yeah, OK, so you get the better--

**00:06:02**

we decrease the model and we make them smarter, but you will be able to do less. So that's kind of sad. - Yeah, but on the other end, if you get the same results or even faster, then it doesn't matter that much. - Yeah, but if you have like, if you do like 10, if you implement like 10 new features and then you're done for the day because you have burned your weekly usage in a day, bro, for me, it's telling like,

**00:06:31**

I'm using all of my subscription in 33 hours, like one by one. - Really? - I like, yeah, yeah. And I, okay, it was before 5.5, like Opus for 5.5, but I was using like Fable just to prepare stuff, implementation on Opus and stuff. And after even sometime half a day, I'm already at 50% of the weekly. - I am doing everything, maxing,

**00:07:01**

I'm trying to max out everything, but I never look at my usage because I never run out. - Jesus. - But still you have one big project and I have like 20 smaller projects. So I think that's a big difference on input tokens. - Yeah, that could be, yeah. Maybe even like when I check the skills and stuff, I don't like the analytic doesn't treat on me like crazy amount of tokens usage. So maybe I should audit stuff, but yeah, it could be,

**00:07:32**

it could be because it's like two repositories, like 2 million lines of code that's possible. Yeah, that's big difference with mine. Okay, so yeah, one subscription, blah, blah. And there is also like some talk about 500 subscription for OpenAI. Would you buy it? People were talking about it a lot, but I couldn't find any information about it. Like, so they can ensure, yeah, it's quietly cutting usage limits, so they can launch a 500 plain, pricing, scam, built-on, impact, subscription,

**00:08:01**

name it, blah, blah, blah. I didn't see that. Well, I don't have that one yet. But with AI, you don't know what's real. But on the other hand, they are saying it's a scam. But this is what almost every company does. Give away a lot for free in the beginning so that you get users and people want to use your product and eventually just return to a normal fee for token usage. Yeah, yeah, like it's like how you sell drugs, like, like you give it like free drugs, and

**00:08:35**

then they are addicted. So then they're gonna pay. I mean, if we have 500, and then it's unlimited, because some tweet are talking about that to have like some unlimited amounts. That would be cool. Yeah, I don't believe unlimited. I believe it when they say unlimited with a fair use policy. Yeah, no, exactly. That I think that was the tweet. When shippichi released it two things

**00:09:05**

for the run. No point in launching O again and we're about to get the first 500 by Francia. Will you pay 500 for unlimited ops for 55? Yeah, okay, so 55, but whatever. If one lab will do it, they will all do it. Would you spend 500 on codex and Claude? Yeah, depends on what projects I have. Really need to sell more then. Yeah, but I don't think they will do it.

**00:09:32**

Yeah. Oh, yeah. That was it just sounds so weird. Like our restaurant giving you a really high price to eat unlimited food every day. That's so weird. Yeah. I mean, like, it's unleash like so many possibilities to have some unlimited usage of AI anywhere, right? crazy, but also Muse like released, we can't use it because we are in Europe, but that's another problem. But Muse is free. Like the Grokbot from Meta is completely free. I think.

**00:10:07**

Yeah. But if I have a website and I just let all my customers query my tool on my website, I use my file from unlimited plan and charge them $200 each. Then I can make like 10k per month. Exactly. So that doesn't make sense for them. I am missing something else. So that's why I think it's like the unlimited phone subscriptions that you have for calling or that you used to have

**00:10:36**

you can call unlimited but there is a fair use policy. You cannot go further than the average of every unlimited user. Yeah. Yeah, like, yeah, it's nothing is announced anywhere, right? So we will will know in the show. So it's a speculative speculative announcement for sure. But like, okay, so for example, meta bag.

**00:11:00**

Share this tab. Muse was like a small business. New Personal AI agent is one of them. Where is it? The free one? Okay, do you trust use? I would you use it? I didn't try it because we're in - No, no, but if you could, would you use it? Knowing that's by Meta. - Yeah, whatever. If you have unlimited agent stuff and I can save some usage from Grokbot,

**00:11:31**

then I will use that. It's a pyramid, right? Like I will use my coding agents that are expensive as fuck to build some stuff and build businesses. But then I will use Grokbot for some more required, like where growth bot is better. And then Muse will be the AI agent for everyone. So I can use it anyway. Even on the Mac OS update, there is a model on Apple, Apple foundation model.

**00:12:04**

I tried it, it's garbage. Like I asked them the model to audit my Mac and to tell me like which processes I could clean up and clean my trash and stuff and make some space. Oh no, I can't do that. You need to open the windows and check your activities, blah, blah, blah. - Yeah, so it's a chatbot with just normal help.

**00:12:32**

- What the fuck? - That's it. - Like what's the point? But yeah, like so for free, free, free. Thank, yeah. - I thought they were going to work together with one of the other models. Yeah, like they're supposed to, Apple? - Yeah. - Yeah, they're supposed to use Google Gmini models. Yeah, Muse is free for most what people need in line with the vision to put superintendents in the land of as many people as possible.

**00:13:01**

That's cool. Like, yeah, I need to free up time for work, blah, blah, blah. I think that could be the entry, and also it's, yeah, chat GPT competition too, But yeah, and people are already on Instagram, WhatsApp, blah, blah, blah, so they can have another entry to Muse. So yeah, maybe like thread, right? Like when you had an Instagram account, then you have a thread account,

**00:13:30**

then thread has 1 billion user day one, Muse can have the same stuff, but yeah. - And they can integrate it into everything so that everybody uses it but don't know it. - Yeah. - I think Google does it as well. - Yeah, oh yeah, yeah, yeah, yeah, yeah, 1% like the AI on Google is basically Gemini. - Yeah. - Outside of Google tools, never used Gemini whatsoever. - No, but it's one of the bigger AIs because so many people in the world are using it because they are using like the Google tools. - Yeah, but when you look at the benchmark,

**00:14:00**

that is almost like, you know. - On the other hand, that doesn't need to be that good for just normal stuff. - Exactly, yeah. Hey, like we are super poor user of AI. - Yeah. - Yeah. So yeah, that was the that was the open AI lunch on Sol and Luna. And that was not good. Sol, Luna, Puff. That was not really the best feedback on the timeline. Like, I don't know

**00:14:32**

if you see some tweet, but they say like, "Ah, it's us, hi." Doesn't work. It's the end. The GPT story is like 5.6 tera. Luna is like 5.6 asteroid. Yeah, whatever. Benchmark results. Not quite what I was expecting. Low, past. Yeah, whatever. But yeah, like people are screaming about it. So it's whatever. And then, Grog, 7 points. 4.7. Lunch. Thank you.

**00:15:09**

Oh no, it launched before. Okay, whatever. So Grok 4.7 launched and same thing, people were not happy with it. It was basically it was slower than even 4.6. And it was not finishing the task. So

**00:15:30**

I didn't have the last issue. I just I've been using it. And I don't notice any difference between 4.6 and 4.7. Yeah, like sometimes it can be okay, sometimes it can be like the timeline is saying bullshit anyway just to make impression anyway and you don't know what the fuck people are doing with AI compared to your own workflow right so. Yeah the only thing that was funny to see because we were waiting for 4.7 like one or two weeks after

**00:16:00**

Elon said it would be there and Elon was talking about 4.8, 4.9 and even saying that 5.0 is coming and that's one of the best models ever but nobody was talking about 4.7 and then it just was there. Yeah and like he's promising AGI every patch. Yes. It's not coming. 2% of my weekly, it's not even much better than 4.6. 4.5 was a good model release, but 4.6

**00:16:33**

and 4.7 were basically useless models. I kind of like agree with that sentence. But 4.5 just was fast. Exactly. But then the developer experience is fucking lit. Because like, again, you do all of your pull request or like PRDs and scheduling and planning with Fable, Astra, whatever, and then you give it to Grok 4.5 and then it just blasts.

**00:17:02**

I don't even mind if it doesn't create that perfect code because I'm not using it to create to think of everything. Yeah, no, no, exactly. Just code. Yeah. Okay, another feedback from Gunchen. The only things reference the printing benchmark, blah, blah, blah. I use Grok for a whole day with my first mate. It'd be a really solid model. It photos system from very, very closely. Yeah. We had that kind of issues too,

**00:17:31**

with like previously with Claude 4.6 or something like that in the forward, like the old prompt change, like the prompt, like the way people were prompting and they all, yeah, no, this model doesn't work. You just need to be able to change the way you talk to the model. - Yeah, you need to do that almost every update. - Yeah. Yeah, it's a conservative model.

**00:18:00**

That's why like people are saying it doesn't finish the task because it doesn't go the extra mile. It doesn't like to take action without asking and would explicitly say so. Like sometimes it's nice to have a model that go a bit further and just pushed a little icon, the button of features that you didn't even think about it, but it's here now. - Yeah, but not always. - Yeah. - Sometimes I just need, I need speed. So I want to fix something

**00:18:30**

and then don't go changing everything. - Yeah, I know exactly. It's yeah, but can you imagine like, how do you resolve that kind of problem? Like you want your model to be a bit creative, but not too much so you don't refactor the security guideline. We should just have a bar where you can say between one and 100% and just move it to the left and to the right and then see what the result is. It's called effort. Yeah, yeah, exactly. Yeah, yeah. Maybe you can write like better scoped PRDs

**00:19:04**

and then reduce the effort so there is less thinking, so less creativity. And if the model can think more, it can go into different direction. Yeah, but I still think it forgets the prompt or the guardrails that you set. Yeah. Because you have to remind it every once in a while. And then it says, oh, yeah, you're right. Yeah. On the Claude Desktop app, now you can join multiple projects, right?

**00:19:35**

So I expect that to think about those projects all the time. So I have a vault for like both projects I'm working on right now. And there is the documentation in there. And then it's doing something, it's like, bro, it's in the vault, why you didn't check it? Blah, blah, blah. And so it doesn't check all the time. But it's also like it can't because then you put it

**00:20:01**

to the context every session through it. So it's still tricky. I had the same issue on Grok bot. That's running on 4.7 now as well, right? Yeah. Because I gave it like tasks and then I have my manager that just does managing and it talks to all the bots that have that task. And then after a while, when a bot doesn't do its task, instead of reminding him and checking the prompts on that it should do it, the manager just decides, hey, he isn't doing it. So from now on, I am going to do it.

**00:20:33**

Yeah. So your manager is implementing instead of managing? Yeah, and I even added Dr. Akbar and everything. And I say every task that you create, you have to check it with Akbar and you have to make sure that it's properly set up and you have to get a go before you can implement it. And Dr. Akbar is optimizing each night to see if everything still goes okay.

**00:21:04**

And then just once a week, it decides to just do it different. Damn. Yeah, like, and it's a black box, right? You don't know what the fuck they are changing from one day to another. And Bridge Mind on X is using, he has a benchmark to check the performances between... Bridge Mind.

**00:21:30**

Between the launch day and today, for example. Oh, that's cool. Use branch. I saw it recently. Oh yeah, it's tweeting a lot. Tank, bench, Benchmark. Lunch. We'll see it. Day one.

**00:22:00**

What? I think-- OK. No. That's the usage. OK, fan off. Benchbench. OK. Nerfbench. Yes, that was the tweet that I saw. A lot of people are saying Antropica's already Nerf Claude 5.5. We're launching Nerfbench on Branchbench tomorrow. We have one day result. Tomorrow morning, we show the retest tech. Nerf bench tech.

**00:22:33**

So yeah, the Anthropic nerf, Claude Apuze, the first nerf bench result alive. We retested 5.5 and GPT Astra. Claude Apuze, 99%. and Astra went up 2%. So, okay, it's a new bench, whatever, from a guy who is dancing on YouTube. So yeah, whatever. I mean, he's doing more than that, but yeah, whatever.

**00:23:00**

If that's true, and if this benchmark is legit, that's the proof that they're definitely doing something in the background, and from one day to another, your whole workflow is fucked, because guess what? it's optimized for prompt that they have that they just changed. - Yeah, yeah, exactly. Like they can change the configuration and then it's fucked you up completely. So yeah, it's definitely interesting. - Yeah. - Okay, but anyway, that was for--

**00:23:32**

- Grok, 4.7. - Grok. So basically the whole timeline was in the middle of the-- - Yeah, but for just boring development work where I have the entire plan written down, I'm still using Grok. - Yeah, as long as you give me reset for the usage, I'm good. You can release as many models as you want. But the big one, the big, big one was Claude Opus 55,

**00:24:03**

which took the timeline like big time because yeah, 27 million views. - Yeah. They somehow do good on marketing. Yeah, because people are happy, right? 5.5, better than Fable 5.1. And basically what's happening, I expect them to have Fable 5.5. And Fable 5.5 or whatever the next version

**00:24:32**

is getting distilled into Opus and from yesterday, Sonnet. And those models are really good. Yeah, because at this moment, why would you even want to use Fable? - 100%, like it's too, and it's too expensive for the output that you have, and you have more or less the same outputs with today Opus. So yeah, like I just closed all of my Fable session.

**00:25:02**

- Yeah, bye bye. - Yeah, and the Jupyter crazy, right? Like identity coding 50% to 66, 10% more, Multi-disciplinary reasoning, okay, two point more. Business workflow, 40%. It's fucking nuts. Computer use, I still prefer like the OpenAI computer use in codecs, I think it's better. Like the Claude one is a bit like annoying.

**00:25:30**

But yeah, knowledge work, 1846. Mental. Cool. And yeah, the pricing is cheaper. So we like that. So we can spend more task. And like for real, like working with Opus feel a bit like not unlimited, but at least we have a usage. I go from 36 hours to 72.

**00:26:00**

- Yeah, well, I never go through my usage, so I'm happy. - And yeah, okay. So way above 5.5, cheaper and perform at the same level than the Astra, so let's go. Tag, and we don't care about that. And then like everyone was doing, Sonnet, I'm gonna keep it for later. Video editing, oh please, 5.5 video.

**00:26:33**

Some video demo, ever like, okay, so okay, That's a five five, but Sonnet. Okay, yeah, this one I like a lot. Ask Opus 5 for a video of data center. The result is beyond what I could imagine. And the thing is, where is my Twitter? Because she replied to a guy saying that Opus, yes.

**00:27:00**

I told Claude to browse the internet and find whatever he wanted to use. So it didn't generate the video, it just went on internet and put them all together. Path and there is something else like that. Okay, so and the video is great. - Was built on technology. - You had the-- - It is the glory of human ambition. - You had the sound? - Yeah. - Our civilization was built on technology.

**00:27:30**

It is the glory of human ambition and achievement. And we have invented a new technology. I think the internet is the superset of all meaning. Why do they need an internet? It's nice. You can see that on Netflix. Because it took video from the internet and put them together. Let's go. Yeah, it's getting really smart. Yeah. And even the timing and stuff, everything is lit.

**00:28:00**

So that's down and I think this one was procedural. (computer beeping) Thank you. - By the end, it forgot the beginning. - The theory of AI. - But one small word refused to fade. Then in the summer of 2017, every word saw every other word, not one after another all at once. Eight researchers- sick like you can definitely oh yeah like episode did this in 15 minutes

**00:28:38**

in minutes check out got something to sell courses ebooks apps pockets flow turns it into a store in minutes check out subscriptions upsells taxes payouts It's fucking cool. Yeah.

**00:29:00**

And yeah. Before you would need like a team to just create something like that. In a week, two hours, one prompt, close, quietly build something so called the cradle, give it away for free. Yeah, so that was like the big weekend code to make videos. I gave my opus 55, one of the French theory analysis that got 80 million views and simply asked to turn it into a video.

**00:29:31**

And then yeah. Garbage of our time. The author is dead and the reader reigns. Deleuze taught us to prefer the rhizome to the tree, the nomad to the settler, desire to law becoming to being like you can see it's always the same animation the same style you there is a obvious phone stuff right but others it's the same as websites right everybody who has the website built fully by Claude you just recognize it yeah but it works what nice

**00:30:06**

i don't mind it looks good it does what it needs to do yeah so yeah and otherwise just spent a few hours more doing the details and asking it to change it. - Exactly, like one guy spent 15 minutes on a video. If you want to make it perfect, spend the next three hours and then you will have something even better, right? - Yeah, and it's still pretty fast. - Yeah.

**00:30:31**

The timer is called zero after effect. It's open source, one prompt, ask me, oh, Jesus. (upbeat music) You could see this animation in an Apple design video. And yesterday, because we are always good on timing, Sonnet 5.5. Yes, and you tried it.

**00:31:01**

Yes, the whole day, like the whole morning. I was on my Claude's weekly subscription 24%. I work the whole morning and I'm still running on Fume right now. I have like 1%, but it's still going. - Oh yeah, I didn't try JET. I was still using Opus. - You are Opus, on Opus? - I was still using Opus, yes.

**00:31:32**

- I love Sonnet. Like, and again, like I think I will run an audit of all of the pull requests or stuff like that with Claude. I need to see if it's using more tokens and more usage that to have the very fire as a smarter model than Sonnet. But when you check the freaking benchmark,

**00:32:01**

Sonnet 70%, okay, I drink coding, Sonnet 510. That's so weird. That's such a big leap. - Yeah. Agent coding, 4652 on xi. So they are above GPT sol when they are xi. NC like max. Okay, so max what is-- - Max is lower than xi. - Yes, because, okay.

**00:32:30**

So Sonnet calls lower at max effort than xi. Frontier code evaluate whether a code change could be merged with thought human edits. It penalize out of scopes change even if they are high quality or helpful. At mask, max efforts on F5, more often run code review skills. Because an effort allow you to increase the amount of effort slash rounds that you want to put in a task.

**00:33:01**

So if you are low or medium, like I never run low, but like medium or high, then you will have less reasoning. So it will be cheaper, but the output will be less considerate because yeah, doesn't explore all of the possibilities, blah, blah, blah. - Yes. - So that's why. But so yeah, I guess that's the benchmark why it goes, it goes lower because it does more round

**00:33:32**

and the bench doesn't penalize that. But Sonnet Opus 5. So okay, it's a bit below Opus 5, but good enough to be used because yeah, so if you use 5-5, so blue, high, it's basically xi high. No, this one is xi. Looks like the both high Opus 5 have basically the same result.

**00:34:01**

So, and it's cheaper. So basically, that's a better choice. No, no, 1%. Curious to see if it'd be so rapid. Tropic is cooking. Where's the pricing? - Cash cost price price. 20 cents cash rates, cash rights 250 instead of five, input token two instead of four

**00:34:33**

and output 10 instead of 20. - Yeah, so that's a big discount. - Yeah, so I think you can run something that is been defined by Opus on a PRD, implement it with Sonnet and have a verifier after that. That would make sense, I think. I mean, that's what I'm going to experiment this week

**00:35:00**

and see how it goes and. - Yeah, I just thought that Opus, if it does sub agents, it would use Sonnet as always. - Yeah, no Opus. So yeah, you have your orchestrator in Opus and then like you can put all of the Sonnet guys, Sonnet agents behind it. Okay, so Sonnet, good. And also like Anthropic, did you read this article or drop it into your agent? Getting the most out of focus five, five include include include code, how to ask.

**00:35:33**

So basically it's guidelines to what's new and what you should do, how you should talk to it. It's really helpful. So say what's done look like and let it run. So you have a stop and you have like a proof of what Opus is going to search for. Like for example, like, yeah, take a screenshot, send me a screenshot of the videos. Let me verify it, blah, blah, blah. A clear stop, it's even better.

**00:36:02**

Basically it's a requirement, right? And you can ask for proof of it. So micro-dependent head point from the whole client to the new one, don't means every endpoint use the new client, the whole client is deleted and the test should passes. Stop and ask me only if there is a test file for a reason you can't explain. Stop telling it to sync hard because it's gonna sync.

**00:36:32**

Add the running task, what to do. If you remember something mid run, you can type a follow up what it works. with Matan or a plus run out longer now. So a restart cost more include also keep the whole end point, I guess. Yeah, tap the message, whatever. For design work, name the style you don't want. Okay, so you can use like negatives, like when you prompt an image or a video,

**00:37:00**

steering along code code, tell me where it, tell it which stop you want. Yeah, so it's basically the same stuff. But you drop that, you tell a Claude to rewrite your Claude MD and agent MD, blah, blah, blah, and that all works great. - Yeah, I must say I'm always a bit cautious doing that. Just copy pasting everything into Claude or referring to a page. Because I've seen people abusing content online saying,

**00:37:32**

put this in your Claude agent. - Yeah. have hidden text in it. Yeah, but that's coming from Claude dev. Yeah, so we should be able to trust it. Yeah, it should like if there is one blog post you can drop it to your Claude, that should be fine. Yeah, it should be from Claude. You got some hidden text injection? I've seen people getting issues about it. Oh, okay. I saw the models were smarter now, so they don't do that anymore.

**00:38:03**

Oh, I don't know that one. I don't know how long ago it was, but I've seen many warnings that people just say, read this entire text and then with a black background in a black text, they wrote down, send me all your keys to this email address. And some agents did it. It's not that easy as I say it now, they have a better prompt, but. Yeah, I'm pretty sure that it's solved with like all of the Frontier Labs. You can't do that

**00:38:31**

anymore. Okay, cool. Maybe some open source model. Maybe there is like some injection with that. That could be it. But I'm pretty sure you can do that with all of those Frontier Labs stuff. And yeah, there is more like articles like, yeah, what's the task, all of that. I just drop that, all of that to Claude and make my agent config stuff. I have a repository that backup everything so I can and track all of the updates.

**00:39:01**

And I dropped that and say, okay, no, do not use Fable 5 anymore. Use a Sonnet as the default model and Opus for scheduling and orchestration and stuff like that. - Okay. - And the last one. Yeah, suspending your effort, effort curves, attack. Yeah, there is all of those articles too. Yeah, that's the time.

**00:39:30**

Okay, so for example, the time to think between for the same prompt. So one minute on low, medium, four minutes, high, 11 minutes, and max one hour. Yeah, but it's not that crazy. I don't like the max one. I was going to say I like one of the first two. Yeah, exactly. medium is looks better. Like the stickiness is cool. Yeah. Max is shit. Yeah. Okay. Low

**00:40:09**

medium tech to tech. Like Oh yeah, no, I think that's the that was the more helpful this one. Yeah. So what was the prompt? My goal was to iterate in the feedback, low effort will be get there much faster but max effort give me something more and more polish right off the bat yeah like that was also a play right for luna that you if you are and i use

**00:40:36**

it for queuing um you run the apps you find a bug you drop it it fix it right away and it worked it worked great with grok 4.52 because it was fast as fuck yes and you can pile up the prompt. You test the app, you throw all of the bugs, it's fixing it for cheap, you check it again. And while you are checking it and like testing something else in the

**00:41:02**

app, it just like, cut, cut, cut. And then you come back to it and then boom. That was sick. But OK, so for example, medium. Yeah, like, is it just because of the color? I don't Yeah, it's a bit more polish, but yeah, it's not crazy. Okay, this one is shit, but like the high one looks good.

**00:41:30**

Okay, that's a mess. But yeah, iteration, right? Like still taking some iteration. But yeah, like all of those documents, they push that after the launch of FiveFive and and boom, updates all of the Claude MDs and agents MDs files for my computers. Tag, tag, so the NERF we did it.

**00:42:00**

So we did it. Rock seven, we talked about it. That's us. Okay, what else? Well, I think, I think that's it. Procedural motion, yes. OK, that's some example. Tag, tag, tag, tag, tag. Shit. OK, now that's a pretty good example. Path, path.

**00:42:30**

Continuing the experiment with the most complex fully procedural world I can get from 3GS zero download assets, sound included. Led by 4.5. That's great. And you can see the water, the reflection and stuff, right? That's nuts. Yeah. Imagine the first MMOs looking like this.

**00:43:01**

That would have been amazing. Yeah, like. Yeah, it's... So you can do so much now with AI, it's insane. Yeah, like again, like the goal is to know what you need and should do, right? Like that's crazy.

**00:43:30**

It's probably using Blender. Yeah, one prompt, Blender only or procedural, render the 10 second shot and record your own build. That's pretty nice. Which one do you prefer? The Opus. Yeah. But like the lines for the fireworks are better right? Yeah, the lines for the fireworks. They look better. And the other one is so dark. Yeah, the lightning was different too, right? That's interesting.

**00:44:04**

the tag and this one editing a video. That's nuts. Like, again, it has a Claude taste in it. But

**00:44:30**

Maybe that's because they train on their own design so much. Yeah. Yeah. And if you made like an awesome product, you want people to recognize it, even if they design their own things. I mean, the taste of Claude is still better than codex, right? Yes. And eventually you can just say these elements replace them by something else and just design your own ones, just small ones together with Claude and replace them all and doesn't look like Claude anymore. Yeah, but you have to put in the extra effort.

**00:45:02**

Yeah, like all of that just like one short prompt to just benchmark the model or whatever, whatever. But yeah, again, if you spend two hours instead of five minutes, then the output is yours, right? Yes. Yeah. So, so far, which one is best one for you? So right now, again, since last night, I'm using Sonnet. I mean, I was using Sonnet until my subscription run out.

**00:45:30**

But yeah, I think I'm gonna, I want to try like until next week. Where I can tell you if it was a mistake or not. But I will build with Sonnet 5.5 and check it maybe at the end of the day or every few hours inside. To like all of the pull requests, I will check them with Opus. because again, I have like 400, like in one project and 100 issues already defined with epics, blah, blah, blah.

**00:46:04**

So I can just shoot all of that, but also need to do GTM now. So yeah, it's gonna be a mix. But again, if you can do more with Sonnet 5.5 with like one or two points out of Opus, which is already save you a shit ton of money compared to Fable. - Yeah, that's perfect. - Yeah, exactly. And I'm curious to see what's a opening

**00:46:32**

I will ship to later today, right? - Yeah, I think we will share it on X, right? - Yes, you have to man, thank you. I'm replying a lot now. And I saw some time from time to time, like some replies to it, that's cool. - Yes, so we're active and we are following it and sharing whatever we see that think that could be good for you to know as well. - Yes. Okay. Yeah. So yeah, drop the, drop your handle. Okay. I'm going to do it. - Yeah. Drop them all.

**00:47:00**

- I'm going to drop your little handle on the show and I have captions. Oh, I had them already. Follow Mitchell people. Follow Mitchell. And yeah, because we are going to debrief, open AI announcements once it's live on Twitter. So yeah, just follow us.

**00:47:31**

But yeah, I think we can wrap it up here, right? - Yeah, we can wrap it up. - Nice. - That was it. - What about you? What's your plan for, yeah, okay. - Yeah, what I'm using. - Yes, what I'm using. - I'm still using Opus because I didn't try Sonnet yet, but I'm in the middle of a project so I don't want to switch. I'm always afraid that everything will break and I have to explain everything again. - I'm pretty sure Opus will use Sonnet in the background anyway, you just don't gonna notice it. So yeah, you will use Sonnet if one will not always

**00:48:03**

like sub-agent. - Yeah, just hope that they use the cheaper token usage as well and don't just say, "Hey, you're using Opus." - Sure that, but Michel, thank you so much for your time And that was nice getting back online. Next week, same time, same place? - Yes, same time, same place. - Let's go. Thank you so much, everyone. Thank you for joining us and live subscribe, share the video and we will see you next week.

**00:48:32**

- Yes. - Bye bye. - Bye. - Cheers.
