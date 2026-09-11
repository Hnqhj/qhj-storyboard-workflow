# AI Video Structure Packaging

Use this to turn a structure into AI-video prompts or shot-planning handoff.

## Structure Block First

Before the visual prompt, write:

```text
Video job:
Viewer promise:
Dominant question:
Structure archetype:
Duration map:
Turn:
Payoff:
```

Then write the ordered visual plan. Exact timings are optional.

## AI 15-Second Prompt Structure

```text
Create a 15-second video with this progression:
opening immediately: [visual promise]
early beat: [context]
middle build: [action/proof]
late complication: [obstacle/scale shift]
near the end: [strongest change]
final image: [payoff/loop/CTA]

Keep [identity/style/prop locks].
Each segment must add new information or pressure.
Avoid repeating the same shot function.
```

## Handoff To Shot Design

Convert structure to shot functions:

```text
hook -> first image / anomaly / cold open
orientation -> establishing or relation shot
build -> tracking, montage, demo, proof
complication -> obstacle, reversal, new scale
turn -> perspective change, reveal, choice, impact
payoff -> final image, result, exit, CTA, loop
```

## Handoff To Screenwriting

Convert structure to story beats:

```text
hook -> dramatic question
orientation -> protagonist/context
build -> pursuit or strategy
complication -> obstacle
turn -> choice/reversal
payoff -> consequence
```

## Prompt Guardrails

For AI video, write structure commands explicitly:

- `the middle must not repeat the opening`
- `each time segment adds new visual information`
- `maintain one continuous route or transformation logic`
- `use one clear turn at [time]`
- `end with a payoff image that answers the opening promise`

Avoid:

- excessive timecodes with tiny sub-beats
- unverified hard intervals that stretch simple actions or rush complex ones
- too many cuts for one generation
- structure that demands dialogue if the model cannot handle dialogue
- ending that introduces a brand new unrelated idea
