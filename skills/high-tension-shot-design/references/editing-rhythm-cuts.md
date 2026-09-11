# Editing Rhythm And Cuts

Use this when the user asks for 节奏, 剪辑节奏, 卡点, 转场, rhythm, pacing, or how to make a short video feel sharper.

## Rhythm Principle

Rhythm is controlled by shot duration, cut timing, eye trace, and contrast. Shorter cuts can raise intensity; longer holds can create pressure, dread, intimacy, or relief.

Do not cut only because something is happening. Cut when the emotional information changes.

Build a density curve instead of equal-duration coverage:

```text
orient with longer shots
-> shorten as distance closes or options narrow
-> compress around the decisive exchange
-> lengthen for recoil, consequence, or reveal
```

The most energetic sequence is not necessarily the one with the most cuts. A long action-led move can contain tracking-owner handoffs, foreground rupture, contact lock, and spatial recovery without becoming visually flat.

## Duration Presets

Quiet pressure:

- 1 long hold, 4-5 seconds
- tiny subject motion
- slow push-in or locked camera

Rising tension:

- 2 shots
- 3 seconds hold + 2 seconds close-up/reveal

Action pop:

- 3 beats
- 1s anticipation + 2s burst + 2s held impact/reaction

Fast montage:

- 4-6 very short beats
- only for compressing time or ritual preparation
- not ideal for fragile AI video unless generating separate clips

## Cut Types For AI Storyboards

Match cut:

- Continue a shape, action, or sound into the next shot.
- Prompt: `cut from [shape/action] to a matching [shape/action], preserving screen direction`.

Match on action:

- Cut in the middle of a movement so the motion continues.
- Prompt: `cut on the action as the hand/weapon/vehicle crosses frame, next shot continues the same movement`.

Smash cut:

- Abrupt contrast, shock, comedy, horror, reveal.
- Prompt: `sudden hard cut from quiet stillness to violent motion / bright light / close-up impact`.

Jump cut:

- Time skips, obsession, anxiety, discontinuity.
- Prompt: `stylized jump cuts compress repeated action, the subject appears to snap forward in time`.

Invisible cut:

- Hide transition in darkness, foreground wipe, motion blur, whip pan.
- Prompt: `foreground object fills frame for a moment, hiding an invisible cut into the next shot`.

Cutaway:

- Object detail reveals meaning.
- Prompt: `brief cutaway to [object/detail], then return to the subject with new emotional meaning`.

Cross-cut:

- Parallel actions build urgency.
- Prompt: `intercut between [A] and [B], each cut shorter, tension rises as the two actions converge`.

## Eye Trace

Use eye trace to keep fast edits readable:

- Keep the main subject near the same screen area across cuts.
- Put the next important object where the viewer is already looking.
- Use light, color, motion, or face direction to guide the eye.

Prompt:

```text
剪辑保持眼动连续：每个镜头的视觉重点都落在画面中心/同一侧，动作方向一致，观众不用重新找主体。
```

## AI Video Translation

If a platform struggles with multi-shot editing, generate separate clips:

1. shot A prompt
2. shot B prompt
3. shot C prompt

Then edit manually. Do not force a single 5-second generation to perform complex montage, jump cuts, and scene changes.

## Avoid

- cutting before the action is readable
- every shot the same size
- every cut on the beat with no emotional reason
- changing screen direction randomly
- adding many cuts inside one fragile image-to-video prompt
