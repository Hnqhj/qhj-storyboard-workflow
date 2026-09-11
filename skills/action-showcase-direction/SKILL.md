---
name: action-showcase-direction
description: Direct pure-action AI videos built around weapons, armor functions, mechanical abilities, movement systems, or character combat language, especially 10-60 second showcases with no opponent. Use for 纯动作展示, 武器动作展示, 技能展示, 角色能力展示, 无敌方动作短片, action reel, weapon showcase, transformation showcase, or when a result has repetitive moves, weak shot-size design, disconnected effects, idle pacing, unclear weapon identity, or an unconvincing finish.
---

# Action Showcase Direction

## Core Intent

Design a pure action showcase as a progression of visible states, not a fight missing an opponent. Make the body, weapon, camera, effects, sound, and edit jointly reveal what the action system is, how it behaves, how it escalates, and what final icon remains.

Apply `think-one-step-further`: preserve successful identity and style, isolate the next control variable, and convert verified lessons into reusable rules rather than project-specific imitation.

## Route Guard: Showcase Versus Character PV

Before using this skill, check whether the user actually wants a pure action showcase or a character PV with action.

- **Pure action showcase**: action system is primary. Use chapters to prove functions, handling, movement grammar, weapon load, effects, and final spatial consequence.
- **Character PV with action**: character identity is primary. Use action as a signature proof, but preserve face, expression, attitude, color ownership, styling, and a short poster icon. Route the final packaging through `$jimeng-sd2-prompting` with character-PV structure.

If the user says "角色PV", "人设展示", "卖角色", "表情", "气质", or "这个角色风格我喜欢", do not fill the whole 15 seconds with attacks. If the user says "纯动作展示", "测试动作", "动作多一点", "武器动作展示", or complains that the action is too little, treat it as a showcase and increase functional peaks.

## Specialist Stack

Use only the layers the task needs:

1. `$kinetic-action-visual-master`: whole-film high-energy camera, composition, shot-scale, animation-exaggeration, physics, and coherence envelope when the showcase should feel aggressive.
2. `$cinematic-audiovisual-language`: shot function, spatial path, screen direction, continuity, and cut reason.
3. `$action-choreography-reference`: actor/load relation, support, weapon balance, force chain, inertia, braking, and recovery.
4. `$action-rhythm-editing`: chapter timing, peak density, contrast, music sync, and settling.
5. `$high-tension-shot-design`: one dominant tension mechanism per beat.
6. `$mechanical-transformation-design`: source, deployment, lock, mass migration, regrip, and new handling when a form changes.
7. `$ai-material-realism`: material, lighting, optics, motion blur, contact shadow, and render credibility.
8. `$cinematic-music-sound-design`: chapter contrast, mechanical cues, impacts, silence, and final decay.
9. `$jimeng-sd2-prompting`: final Seedance / 即梦 packaging and reference roles.

Read `references/pure-action-showcase-grammar.md` for detailed structures, shot ladders, effect-transition logic, failure diagnosis, and prompt controls.

## Workflow

### 0. Lock The Global Visual Master

Before detailed action or shot language, define the whole-film generation domain:

For aggressive anime-cinematic action, POV bursts, unconventional framing, or extreme shot-scale contrast, build this block with `$kinetic-action-visual-master`. Keep its camera family bounded and let each later beat use only the mechanism it needs.

```text
medium and realism level:
primary aesthetic family:
palette ownership and forbidden colors:
line, shape, and silhouette language:
material and lighting system:
rendering hierarchy and optical character:
forbidden style drift:
```

Write this block near the beginning of the final generation prompt. Every chapter inherits it; individual shots may not independently change style.

### 1. Define The Display Contract

State:

```text
subject and action system:
weapon or ability family:
primary movement/martial basis:
visible action grammar:
actor strength relative to load:
main movement signature:
3-6 functions to prove:
strongest final state:
```

An opponent is optional. Every peak must still create a visible change in at least one of:

- body position, facing, level, or support;
- weapon path, grip, balance, configuration, or state;
- environment, route, depth, scale relation, or available space;
- camera relation, visual information, or sound state.

Do not begin with a list of actions alone. Assign one primary movement grammar that persists through entry, traversal, attack, transition, and recovery. For multiple performers, give each a contrasting grammar.

### 2. Build Chapters Before Shots

For 10-15 seconds:

```text
identity hook -> handling proof -> escalation -> dominant peak -> recovery/icon
```

For 20-30 seconds:

```text
identity -> first action phrase -> state/mechanism bridge
-> second action phrase -> ultimate -> short hero closure
```

For 30-60 seconds:

```text
3-5 chapters, each with a different action contract, silhouette,
support logic, trajectory vocabulary, tempo, shot function, and end state
```

Do not extend runtime by repeating the same attack with larger trails.

Use a timing-confidence gate. If a reviewed reference, previous successful output, animatic, edit map, or physical phase budget lets you determine how long each major chapter should last, write exact chapter ranges. Keep the cuts and camera changes inside each chapter flexible. If chapter duration is uncertain, use approximate proportions or untimed order instead.

### 3. Use A Shot-Function Ladder

Select only the steps the film needs:

```text
identity detail
-> full-body handling proof
-> perspective scale proof
-> path/geography proof
-> depth or axial proof
-> mechanism/state-change proof
-> ultimate spatial consequence
-> stable body-and-weapon closure
```

Every shot must answer a new question. Close-ups prove one mechanism or decision; wides prove support, trajectory, scale, displacement, or recovery.

### 4. Differentiate Action Chapters

Change at least four columns between major chapters:

```text
silhouette / base of support / body level / dominant path
weapon function / trajectory plane / tempo / camera height
shot scale / screen direction / effect behavior / sound envelope / end state
```

When the weapon changes mass class, require:

```text
visible mode change -> lock proof -> regrip -> stance adjustment
-> brief settling beat -> new timing and braking behavior
```

Run a topology audit before delivery:

```text
chapter / trajectory plane / weapon end or function / support state
/ body level / travel vector / braking method / end guard
```

At least one structural field must change decisively between adjacent peaks. A low circle, overhead circle, body orbit, camera orbit, and circular effect are not five actions; they are one loop repeated across layers.

### 5. Make Effects And Transitions Causal

Every major effect needs:

```text
source -> path -> interaction or state change -> decay
```

Every transition needs:

```text
outgoing action source -> screen coverage or matched vector
-> incoming image that inherits direction, shape, material, or sound
```

Useful sourced transitions include blade-edge wipes, shield/body occlusion, debris or cloth passes, red-line match cuts, mechanism inserts, light-state changes, impact whites, and sound bridges.

Do not add an effect or transition only because the shot needs excitement.

### 6. Design A Real Finish

The final peak must be stronger by consequence, not only brightness. It may:

- change weapon configuration;
- alter the floor, air, architecture, or graphic space;
- resolve a large trajectory into a stable axis;
- reveal a new silhouette;
- return abstract spectacle to a readable body-and-weapon relation.

After the peak, show inertia resolution, sound decay, and a stable final icon. Keep the beauty epilogue shorter than the action payoff unless character portraiture is the main goal.

For 15-second showcases, audit the terminal hold. If the character reaches the final pose before the last 1-1.5 seconds, the action budget is being wasted. Add a mid-late function proof or move the final icon later rather than extending the pose.

## Output Contract

For a direct-generation request, provide:

```text
Creative judgment:
Display contract:
Chapter rhythm:
Shot and action plan:
Effects and transition causality:
Sound:
Paste-ready prompt:
  [positive instructions]
  [negative constraints appended inside the same block]
Preflight:
```

Keep negative constraints in the same paste-ready prompt block so the user can copy once.

## Quality Gate

Before delivery, verify:

- The clip works without inventing an enemy.
- A global visual master appears before the detailed action and shot list.
- When the master is high-energy, unconventional framing remains spatially readable and every camera disruption has an action, occlusion, gaze, impact, or orientation trigger.
- The weapon or ability family has a recognizable movement signature.
- Every principal performer has a recurring movement grammar, not only a job list.
- Each chapter changes function, not merely effect intensity.
- Each chapter changes movement topology, weapon function, or support state rather than restaging the same arc from another camera.
- Shot sizes and angles reveal different information.
- Full-body shots show support, route, follow-through, and braking.
- Close-ups prove a grip, release, lock, mechanism, material, or decision.
- Effects have a source and follow the action path.
- Transitions inherit a visible or audible element from the outgoing shot.
- A transformed form receives new handling and timing.
- The strongest peak changes the spatial or functional state.
- The ending settles into a clear final relationship.

## Guardrails

- Do not criticize a pure showcase for lacking an opponent.
- Do not let camera motion replace performer displacement.
- Do not let effect paths change while the body repeats the same motion.
- Do not make all weapons converge on circular windmilling.
- Do not hide every support point, grip, transformation lock, and brake.
- Do not use close-ups as decorative catalog shots; each must add functional information.
- Do not let a large weapon move like a light baton unless active assistance and damping are visible.
- Do not let a long final pose consume the payoff.
- Do not hard-time every shot by habit; wrong durations can create idle motion, rushed mechanics, premature climax, or missing recovery.
- Do not confuse precise chapter allocation with precise cut timing. The former can improve emphasis; the latter can overconstrain motion.
- Do not write only “run, jump, climb, attack, block, finish.” State the posture, geometry, support changes, rhythm, and recovery that make those events visually distinctive.
