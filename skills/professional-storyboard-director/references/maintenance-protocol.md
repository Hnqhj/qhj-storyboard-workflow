# Maintenance Protocol

Use this only for auditing, updating, pausing, or resuming the professional storyboard skill. Do not load it for ordinary storyboard generation unless the user asks how the skill is maintained.

## Evidence Gate

Before changing the skill, inspect the smallest available evidence set:

- recent user corrections or approved outputs;
- generated-video failure reports or reviewed outputs;
- `references/source-map.md` for source-backed mechanisms already added;
- current structure checks for missing references, unresolved placeholders, or broken routing;
- capsule/case evidence only when it contains a concrete result, boundary, and verification point.

Do not edit the skill when the only evidence is a scheduled heartbeat or a clean audit. Record the clean state outside the skill if needed.

Research current sources only when new information could change storyboard structure, shot function, spatial continuity, tension mechanism, AI-video packaging, or retry strategy. Interesting but unactionable findings remain notes, not rules.

## Current Distilled Mechanisms

These mechanisms are already represented in the skill and should be preserved during future edits:

- AI-video feasibility: add reference role, first-frame anchor for image-to-video, clip split, action load, dominant camera move, motion budget, and platform-aware negative strategy.
- Segment split and handoff: split by location, time, lighting, axis/viewpoint, reference role, action phase, style shift, or overloaded motion/camera demand; each split needs previous end state, next first-frame anchor, locks, allowed changes, and cut reason.
- Dialogue and quiet emotion: treat listening, hesitation, delayed reply, residue objects, J/L cuts, and sound bridges as story action when they carry the scene change.
- Reference breakdown: extract whole-reference grammar first; transfer function, spatial logic, rhythm, transition trigger, depth strategy, and information ladder, not surface arrangements.
- Product/prop advertising: use need/context, early product recognition, scale/hand relation, material or mechanism proof, benefit/result, memory frame, and CTA; beauty shots must prove something concrete.
- High-speed action: assign an eye-trace anchor before camera aggression; create speed through layer contrast and reset geography after occlusion, blur, whip pan, subjective POV, or close detail.

## Regression Prompts

Use 1-4 compact forward tests after meaningful edits:

1. Quiet emotion: "Two people break up in a rainy convenience store, 15 seconds, restrained but with aftershock."
2. High-tension action: "A lone character carries a long spear through a collapsing corridor, 15 seconds, no enemies, danger must read."
3. Product reveal: "Storyboard a 30-second ad for futuristic headphones with material proof and usage context."
4. AI image-to-video: "From one character still, make a 5-second image-to-video board with only micro-action and camera push-in."

Passing output should include storyboard mode, audiovisual goal, information ladder, spatial lock, shot function, rhythm curve, continuity locks, and AI attention or negative constraints when relevant. It should not over-escalate normal scenes into action or stack camera moves without a story job.

## Failure Mode Entry Shape

Add or update a failure mode only with real generated output, repeated user correction, or a reviewed failed storyboard:

```text
symptom -> evidence -> root cause -> storyboard control -> AI negative/positive lock -> verification point
```

Current watch item: AI-video multi-segment drift. Add a rule only if outputs show identity, layout, axis, time-state, or action-phase drift across generated segments despite existing handoff notes.

## Cross-Skill Boundary

- Use `cinematic-audiovisual-language` for axis, staging, continuity, cut logic, shot function, and sound-image grammar.
- Use `high-tension-shot-design` after readable base staging when the user wants pressure, danger, awe, instability, or impact.
- Use `action-choreography-reference` before weapon-heavy, body-weight, chase, combat, or impact boards where support, center path, force chain, inertia, braking, or recovery affect readability.
- Use `ai-video-prompt-director` when the storyboard must become a full AI-video prompt package.
- Use `ai-material-realism` when material behavior, texture, object construction, lighting, or physical plausibility must be locked for AI image/video generation.

## Pause And Resume

If context pressure is high, stop expanding the thread and preserve only a compact handoff. On resume, read this file plus `source-map.md` before adding rules. Do not replay long heartbeat logs into the chat or into the skill.
