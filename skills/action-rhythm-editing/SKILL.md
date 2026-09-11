---
name: action-rhythm-editing
description: "Mandatory rhythm/editing baseline for substantial film/AI-video action, fight, chase, weapon, action storyboard, and kinetic character-PV tasks. Design timing, pacing, editing beats, slow motion, hit-stop/impact frames, music sync, and mass-aware action rhythm. Use for 动作, 打斗, action timing, 节奏, 卡点, 打击感, weapon-weight timing, inertia, braking, recoil, HEAVY/RUSH/CHASE-like pacing, 3s/5s/8s/15s action structure, or when action feels soft, weightless, rushed, idle, uniformly paced, or physically disconnected."
---

# Action Rhythm Editing

## Liu Short-Drama Override

For Liu's Seedance short-drama work, rhythm is visual and physical rather than musical. Do not plan music sync, score hit points, BGM, ambience beds, or mood sound cues. Use only dialogue timing, dry source-coupled foley, impact transients, breath caused by exertion, and purposeful silence. Camera-group duration follows the 14-28 second project contract; choose the shortest complete group.

## Bottom-Layer Reasoning

Apply `think-one-step-further`:

- Make the action peak readable and causally complete.
- Scale timing to actor strength, weapon inertia, distance, and response.
- Preserve the successful spatial/action path.
- Add one guardrail for the next likely failure.

## Core Intent

Turn an action idea into timed beats: anticipation, acceleration, peak, response, follow-through, braking, and recovery.

Rhythm strengthens an established spatial and physical path. It does not replace blocking, screen direction, martial mechanics, or sound design.

For 10-60 second pure weapon, armor-function, transformation, movement-system, or character-ability reels with no required opponent, get the chapter structure and action-state progression from `$action-showcase-direction` before timing individual peaks.

## Workflow

1. Determine duration, aspect ratio, and delivery format.
2. Confirm objective, path, screen direction, obstacle/reversal, and strongest peak.
3. Get the physical profile from `$action-choreography-reference`:
   - actor strength relative to weapon;
   - weapon mass distribution and length;
   - support and traction;
   - required recoil, braking, and recovery.
4. Choose the rhythm family: sharp, heavy, graceful, pressure, chase, anime impact, mechanical, or commercial reveal.
5. Time the causal phases:
   - support/preload;
   - commitment/acceleration;
   - contact, near miss, release, or change of direction;
   - receiver and environment response;
   - follow-through and braking;
   - recovery into a changed state.
6. For multi-participant action, reserve time for the receiver. The attacker cannot consume the whole beat.
7. Assign one camera responsibility per beat and selective physical foley hit points. In Liu mode, use `$seedance-audio` only after explicit approval for a dry foley timing test; this Skill still owns physical timing and does not manufacture platform audio behavior.
8. Output segment timing according to confidence:
   - high: exact macro ranges with flexible internal cuts;
   - medium: approximate ranges/proportions;
   - low: causal order only.
   Use exact micro-shot timestamps only for necessary synchronization.
9. Build a density envelope:
   - longer readable setup;
   - shorter beats only during escalation or exchange;
   - a brief decisive peak;
   - enough consequence and recovery to prove the changed state.
   Do not distribute the whole duration into equal action blocks by default.

Read `references/rhythm-map.md` for duration templates and mass-aware timing.

When close-range exchanges, hand-fighting, weapon binds, clinches, or short control sequences feel slow, turn-based, uniformly paced, or unreadable, read `references/close-exchange-density.md`. Choose one density family, preserve receiver time, and treat any post-retime as a bounded single-variable test rather than a universal speed multiplier.

## Mass-Aware Timing

Use relative timing, not a universal speed:

```text
light/grip-biased: short preload -> fast peak -> short brake
balanced/medium: clear preload -> fast peak -> moderate recovery
tip-heavy/head-heavy: longer preload -> committed acceleration -> long follow-through and brake
flexible-delayed: handle starts -> weighted end peaks later -> returning tension wave settles last
superhuman: compressed startup is allowed, but environmental force and active damping must remain visible
giant mass: terrain reacts before the system fully settles
```

Do not make a heavy action slow everywhere. Weight is usually sold by contrast:

```text
controlled preload -> sudden committed acceleration -> brief peak
-> delayed environmental response -> longer braking and settling
```

## Speed Contrast for Animated Power

For stylized action, especially animation-reference action with clear 力量感, speed should form a curve rather than staying intense throughout:

```text
readable preload / anticipation
-> very short acceleration spike
-> impact, release, or direction change
-> delayed follow-through
-> braking / recovery into the next source
```

Useful timing ratios:

- light strike: 2-4 frames preload, 1-3 frames peak, short recovery;
- heavy or oversized weapon: 8-18 frames preload, 2-5 frames peak, 8-20 frames follow-through/brake;
- superhuman dash: 6-12 frames compression, 1-3 frames smear/burst, then a catch step, slide, wall touch, crouch, or rebound that proves the body handled the speed;
- combo phrase: each hit needs a different preload source, not repeated identical "fast hits".

If the user praises "动作速度" or "运动前置", preserve:

- a visible slow-to-fast jump;
- one pre-impact coil, crouch, reverse swing, or weapon lag;
- a clear post-impact drag, overshoot, or brake.

Avoid prompts that say the character "keeps constant high speed" unless the desired effect is weightless sprinting. Constant speed often kills force.

## Momentum-First Slow Motion

For an explosive opening or decisive attack, slow motion may begin **after** the action has already acquired momentum. Do not misread every slowed passage as preload or charge-up.

Default state: **off**. Activate this device only when at least one condition is true:

- Liu explicitly asks for slow motion, speed ramp, or temporal magnification;
- an inspected reference is assigned to transfer this exact rhythm mechanism;
- the current beat already has visible momentum and a brief slowdown has one indispensable readability job that normal-speed coverage cannot perform.

A mechanism discussed or learned in the previous turn is not permission to carry it into the next scene. If the trigger and evidence task are absent, keep the action at its natural speed curve.

Use this rhythm when the scene should enter in medias res:

```text
high-speed action already underway
-> camera catches or is crossed by the moving body/weapon
-> brief dynamic slow motion reveals intent, force path, attack line, or power source
-> continuous trajectory resumes at high speed
-> collision, release, forced response, or changed spatial state
```

Rules:

- Establish acceleration before the slowdown; slow motion must magnify existing momentum, not manufacture it.
- Preserve carrier path, screen direction, body commitment, and weapon trajectory through the slowdown. No pose reset, hovering, or new stationary charge.
- Give the slowed interval one evidence task: expose eyes, support chain, weapon lag, energy origin, near-contact distance, or the receiver's imminent danger.
- Exit the slowed interval into a visible consequence. A speed ramp that returns only to another pose is incomplete.
- Use short contrastive slow motion selectively. Repeated speed ramps flatten the rhythm and turn action into a montage effect.

Distinguish the two valid patterns:

```text
preload-led power: readable support/preload -> acceleration -> peak
momentum-led power: immediate burst -> dynamic slowdown for readability -> resumed burst -> consequence
```

Choose from the actual action state. Do not force a standing preload when the desired hook is an attack already in progress.

## 15-Second Action Rhythm

```text
opening: physical profile and first hook; when justified, enter with momentum already underway rather than a standing setup
then: first displacement/commitment
middle: obstacle or exchange with response
afterward: tactical or level change
near the climax: strongest peak with full causal reaction
ending: inertia resolution, consequence, exit, or cliffhanger
```

For an action showcase, choose the smallest number of distinct peaks that the model, weapon, and continuity burden can sustain. Three to five clear phrases are often stronger than six forced nodes. Use 5-6 peaks only when each has a distinct function, visible displacement, and enough continuity budget. For one dramatic heavy action, use fewer peaks and give more time to support, contact response, and recovery.

Prefer:

```text
stable hook -> rising exchange -> compressed climax -> visible consequence
```

Avoid equal-duration segmentation unless explicit dry-foley synchronization, mechanical timing, or inspected evidence justifies it.

When inspected AI-video attempts repeatedly insert idle holds, reset the receiver, or produce different action orders from the same prompt, reduce the duration or split the action before adding more micro-choreography. For one highly stylized superhuman action phrase, a 7-10 second validation clip is often more stable than a 15 second version. Use short macro beats that each prove one state change: capture/contact, displacement, level change, climax, consequence. Avoid long 3-second wide shots that are supposed to prove close contact; they usually become empty scale shots or standing resets.

## Output Shape

```text
Physical timing profile:
preload/support:
acceleration:
peak and receiver response:
follow-through/braking:
recovery/end state:
Camera rhythm:
Sound/foley:
Paste-ready prompt:
```

## Guardrails

- One short clip should have one dominant peak unless it is explicitly a showcase.
- A peak is incomplete until the receiver/environment reacts and the spatial state changes.
- Scale preload and braking to mass distribution, not merely total weight.
- Preserve foot contact, carrier motion, or named support continuously.
- Keep impact pauses brief; heavy does not mean frozen.
- Do not stretch one move across 15 seconds.
- Do not use slow motion, camera shake, speed ramps, or particles as substitutes for force preparation and recovery.
- If action is complex, split it rather than removing response clarity.
- For Liu mode, specify selective physical foley hit points, anticipation, trails, and silence; never force cuts onto a musical beat.
- Reference audio is a soft generative condition, not a substitute for support, contact, receiver response, braking, or continuity. Use `$seedance-audio` for the control-track/A-B loop and keep cue-to-picture mappings empirical.
- Precise macro-segment allocation is allowed without an external clock when supported by inspected evidence or a credible action-phase budget.
- Keep individual cut duration flexible unless synchronization requires otherwise.
- Concentrate the shortest cuts around escalation or the decisive peak; do not keep the whole clip at one density.
