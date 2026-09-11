# Short-Form Retention Editing

Last researched: 2026-06-28
Status: active reference, research-synthesized, not capsule-promoted

Use this file for modern trailers, teasers, ads, Shorts, Reels, TikTok-style clips, AI-video structures, hooks, retention curves, beat density, information release, loops, CTAs, and analytics-informed editing decisions.

## Research Questions

1. What does current platform guidance actually say about early hooks and retention, and what should not be overgeneralized?
2. How should a cinematic short-form structure differ from a traditional setup-build-climax arc?
3. Which retention signals should guide editing: intro drop, spike, dip, traffic source, CTA, or replay loop?
4. How can AI video prompts express retention structure without turning into an overloaded shot list?

## Working Controls

- Treat the first 1-3 seconds as a promise, not an intro. Show the central question, contradiction, danger, object, face, result, or sensory hook immediately.
- Renew attention every few seconds with one useful reset: new information, scale shift, obstacle, sound beat, graphic/text cue, camera move, performance turn, or reveal.
- Use "hook -> proposition -> proof/escalation -> turn -> payoff/loop" for short-form structures; do not default to slow exposition.
- Match thumbnail/title/ad promise to opening content. A strong click promise that the opening does not fulfill creates retention loss.
- Design for retention graph diagnostics: steep early drop means promise mismatch or slow intro; dip means confusing or low-value segment; spike means replay/share/unclear moment.
- Use text and audio as reinforcement, not competing layers. On-screen words should clarify the proposition, twist, or CTA.
- For ads, make the next action explicit; for cinematic teasers, make the final image or unanswered question explicit.
- For AI video, lock macro beat order and one or two visible retention resets. Avoid demanding exact edits that the model may not obey.

## Retention Function Tags

- `first-frame_promise`: the opening image states why to keep watching.
- `proposition_fast`: the viewer understands the subject/value/conflict within the first few seconds.
- `attention_reset`: a new cue renews attention before the beat goes flat.
- `spike_design`: a moment is designed for replay, surprise, clarity, or shareability.
- `dip_risk`: a segment may cause confusion, repetition, slow exposition, or promise mismatch.
- `loop_button`: ending links back to the start or leaves an immediate rewatch reason.
- `cta_clarity`: the viewer knows what to do next, when the format needs action.
- `platform_fit`: structure, framing, text, audio, and duration fit the target surface.

## Knowledge Entries

### YouTube Audience Retention -> Structure Must Be Diagnosed Moment By Moment

Source / film example -> YouTube Help, "Measure key moments for audience retention," and YouTube Blog creator metrics guidance.

Observation -> YouTube separates flat sections, gradual declines, spikes, dips, intro performance, and traffic/viewer segments; its blog frames retention as feedback on video structure and storytelling.

Mechanism -> Retention is not one average number. A video's structure can be diagnosed by where attention holds, drops, spikes, or mismatches the entry promise.

Executable control -> Before revising a video, label the retention curve: intro drop, middle dip, replay spike, late drop, or traffic-source mismatch. Then revise only the corresponding beat: opening promise, confusing segment, payoff placement, or expectation match.

Applicable scenes -> YouTube videos, Shorts when analytics are available, trailers, explainers, AI videos with inspected output, any repeated video format.

Misuse boundary -> Do not infer creative truth from one metric alone. A spike can mean a strong moment or an unclear moment that viewers rewatch to understand.

Validation status -> Strong official analytics source; not capsule-promoted.

### TikTok Creative Best Practices -> Hook And Proposition Are Separate Beats

Source / film example -> TikTok Ads creative best practices.

Observation -> TikTok recommends introducing the content proposition in the first 3 seconds, prioritizing the hook in the first 6 seconds, using captions/text for context, transitions/graphics for engagement, and ending with a clear CTA for ads.

Mechanism -> The viewer must understand what the clip is and why it matters before the hook window closes. Hook is not only shock; it can be suspense, surprise, emotion, or value.

Executable control -> For a 15-second prompt or storyboard, write: 0-3s proposition, 0-6s hook pressure, 6-12s proof/escalation, 12-15s CTA/payoff/loop. Add captions only where they clarify the proposition or turn.

Applicable scenes -> TikTok ads, social shorts, product clips, character reveals, short AI video prompts, fast explainers.

Misuse boundary -> Do not force ad CTA logic onto pure cinematic pieces. For story teasers, replace CTA with payoff, cliffhanger, or loop.

Validation status -> Strong official platform ad source; not capsule-promoted.

### Google / YouTube ABCDs -> Jump In And Sustain Attention With Multisensory Reinforcement

Source / film example -> Think with Google / Google Ads Help, YouTube ABCDs.

Observation -> Google frames effective video ads through Attention, Branding, Connection, and Direction; Attention includes jumping into the story faster, tight framing, pacing, audio, supers, and high-contrast visuals.

Mechanism -> Modern video ads often invert the traditional arc. They put the attention-grabbing premise up front and use audio/text/framing to keep the promise legible on mobile.

Executable control -> Open with a close-up, mid-action state, result-before-cause, striking sound, or bright/high-contrast visual. Then use a small number of repeated identity/proposition cues rather than waiting for a late reveal.

Applicable scenes -> YouTube ads, trailers, social commerce, brand films, product reveals, AI-generated promo clips.

Misuse boundary -> Do not treat ABCD as a universal story formula. It is ad effectiveness guidance, not a replacement for drama, scene logic, or noncommercial pacing.

Validation status -> Strong official/Google source; not capsule-promoted.

### Meta Video Ad Help -> Short Duration And Early Message For Feed/Reels Contexts

Source / film example -> Meta Business Help Center on video ad best practices.

Observation -> Meta guidance emphasizes showing brand/key message early, keeping videos concise, and designing for mobile surfaces.

Mechanism -> Feed/Reels viewers often evaluate clips before narrative context accumulates. Early message clarity and mobile framing reduce avoidable early drop.

Executable control -> For social versions, crop and stage for vertical/square readability, put the primary object/person/action in the first frame, and avoid tiny text or delayed context.

Applicable scenes -> Instagram/Facebook Reels ads, feed ads, mobile-first promos, AI video variants that need platform-specific framing.

Misuse boundary -> Do not make every filmic sequence into a compressed ad. Use this only when the distribution surface rewards immediate clarity.

Validation status -> Official platform guidance, but page access may redirect; use with current-source caution.

### Video Structure Design Skill -> Beat Skeleton Before Shot List

Source / film example -> Local `video-structure-design` skill.

Observation -> The skill separates video macro skeleton from shot design: hook, viewer promise, temporal hinge, structure archetype, duration map, retention resets, and ending button.

Mechanism -> Short-form retention problems are often structural before they are visual. More shots do not fix a weak promise, missing turn, or absent payoff.

Executable control -> Build the structure first: viewer promise -> beat order -> reset points -> turn -> payoff/loop. Only then assign camera, sound, and visual style.

Applicable scenes -> AI video prompts, short trailers, character reels, product videos, social clips, music/action edits.

Misuse boundary -> Do not overfit exact timestamps when generation timing is uncertain. Use macro beat order unless tested outputs support precise timing.

Validation status -> Local workflow source; not capsule-promoted.

## Short-Form Structure Templates

### 10-Second Cinematic Teaser

```text
0-1s first-frame promise: striking state, danger, impossible object, or aftermath
1-3s orientation: who/where/what rule, kept minimal
3-6s escalation: new pressure, motion, or contradiction
6-8s turn: reveal, obstacle, reversal, or scale shift
8-10s payoff/loop: consequence image or unanswered question that points back to the first frame
```

### 15-Second Social Ad / Product Reveal

```text
0-3s proposition: product/value/problem visible immediately
0-6s hook pressure: surprise, suspense, emotion, before/after, or claim
6-10s proof: demonstration, transformation, comparison, or social proof
10-13s turn: stronger benefit, objection answer, or reveal
13-15s CTA/loop: clear next action or final memory image
```

### 30-Second Trailer / Character Reel

```text
0-3s promise image
3-8s world/character rule
8-14s pressure or conflict
14-20s escalation montage with one new information beat
20-25s turn or identity reveal
25-30s peak image, title/card/CTA, or loopable final question
```

## Retention Diagnosis Checklist

```text
Entry promise:
Expected viewer question:
First 3 seconds proposition:
First 6 seconds hook:
Attention resets:
Dip risks:
Designed spike:
Turn:
Payoff / CTA / loop:
Sound/text reinforcement:
Platform fit:
Evidence source:
```

## AI Prompt Packaging

For AI video, convert retention structure into visible beat order:

```text
Duration:
First-frame promise:
Beat order:
Retention reset 1:
Retention reset 2:
Turn:
Payoff / loop:
Camera/sound reinforcement:
Do not overload:
```

Avoid writing:

```text
make it viral, highly engaging, retain viewers, lots of fast cuts
```

Write instead:

```text
open on the final impossible image, reveal the cause after 2 seconds, add one sound reset at the midpoint, end with the object returning to its starting position so the clip loops cleanly
```

