# Cinema Language Atlas Iteration Synthesis

Updated: 2026-07-02 Asia/Shanghai

Use this reference when resuming the paused cinema self-iteration loop, applying the latest prompt-writing contract stack, or checking what has already been consolidated into this global skill.

## Pause State

- `automation-3` was paused on 2026-07-02 at the user's request.
- Do not continue autonomous research until the user explicitly asks to resume.
- If resumed, start from this skill first, then use local `work/rolling-state.md`, `work/research-notes.md`, and `work/rollover-handoff.md` only as auxiliary handoff files.

## Authoritative Skill Files

- `prompt-writing-techniques.md`: main prompt-control library. Contains the reusable contracts, prompt blocks, failure boundaries, and quick translation table.
- `source-map.md`: source quality map, search scope, and round map.
- `case-cards.md`: round-by-round change cards, validation status, and non-promoted mechanisms.
- `iteration-synthesis.md`: compact current-state index; keep this short.

## Covered Blocks

- R1-R18: shot breakdown, shot language, lighting/color, dialogue, action, sound/editing rhythm, style anchors, applied breakdown validation.
- R44-R59: prompt-writing transfer, clip-to-prompt loop, continuity, lens distance, generated-output review.
- R60-R95: prompt-transfer contracts for danger, listening POV, lighting transitions, constrained dialogue, cut permission, style anchors, insert types, subjective inserts, unreliable reveals, clue/evidence systems, blocking, eyeline, reaction ownership, silence/pause, sound distance, offscreen sound reveal, sound bridge/prelap, postlap/audio-tail, and audio match cut/sonic match.

Latest completed round: R95 audio match cut / sonic match prompt contracts.

## Current Contract Pattern

Most reusable mechanisms should be stored in this shape:

```text
source/example -> observation -> mechanism -> executable control or prompt wording -> applicable scenes -> misuse boundary -> validation status
```

For AI video prompts, prefer this operational shape:

```text
mechanism -> positive prompt control -> timing/spatial lock -> negative or positive boundary -> output review gate
```

## Active Audio Transition Stack

- Held silence / pause: silence owner, removed layers, remaining cue, pressure object/space, decision state, release cue, payoff.
- Sound perspective / distance: source status, listener point, distance, obstruction/filter, acoustic quality, reveal policy, image consequence.
- Offscreen sound reveal / misdirection: assumed source, actual source, delay, acoustic clue, correction beat, reveal evidence, listener reaction.
- Sound bridge / prelap: outgoing image, incoming source, lead duration, transition point, incoming image answer, payoff.
- Postlap / audio-tail: outgoing source, carry duration, incoming image relation, cutoff/replacement, new-scene sound takeover.
- Audio match cut / sonic match: outgoing sound shape, incoming matching source, sonic cut/blend point, difference cue, image answer, payoff.

## Validation Standard

After editing this skill, run:

```powershell
python '<skill-creator>\scripts\quick_validate.py' '<skills-root>\cinema-language-atlas'
python '<optional-capsule-engine>\scripts\capsule_engine.py' validate
rg -n '<maintenance-marker-pattern>' '<skills-root>\cinema-language-atlas' 'work'
```

`rg` exit code 1 is clean for the marker scan.

## Capsule Boundary

All R60-R95 prompt-contract additions are source-backed scaffolds, not capsule-promoted rules. Promote only after inspected generated outputs or repeated real cases show that the contract reduces failures within a clear boundary.

## Resume Candidate

If the user asks to resume, the next useful lane is:

```text
silence-to-sound rupture clue contracts -> silence owner, rupture source, threshold moment, reaction, payoff, review gate
```
