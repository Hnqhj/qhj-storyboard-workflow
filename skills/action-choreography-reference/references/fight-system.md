# Fight System

Use this when designing more than one isolated move. It turns action into a controllable dramatic and spatial system.

When viewer expectation depends on a planted tactical advantage, threatened objective, environmental affordance, reversal source, or finishing opportunity, also read `fight-dramaturgy-and-payoff.md`. Keep promise/payoff status separate from the physical mutation ledger: a promise tracks what the viewer expects; a mutation tracks what the fight state now permits.

When earlier contact, fatigue, equipment damage, altered terrain, or lost initiative must change later options, also read `combat-impact-state-progression.md`. Keep a compact mutation ledger; local reactions that do not constrain later choices stay out of it.

## State Before Moves

Define:

```text
objective: escape / capture / protect / delay / disarm / reach / survive / dominate
initiative: who forces the first response?
advantage: reach / speed / mass / numbers / terrain / weapon / information
distance: contact / close / medium / long / pursuit
formation: line / triangle / encirclement / corridor / vertical stack
constraint: injury / hostage / fragile object / narrow space / moving platform / low visibility
```

The beat must end with a changed distance, initiative, route, balance, elevation, weapon state, formation, or objective access. If only poses change, the beat is decorative.

## Physical Profile Before Exchanges

Read `weapon-body-dynamics.md` when bodies or weapons differ meaningfully in mass, reach, strength, or balance.

Define:

```text
actor A mass/strength:
actor B mass/strength:
weapon load and mass distribution:
support surfaces and traction:
who can stop directly and who must redirect:
expected braking/recovery distance:
```

Do not choreograph light and heavy characters with identical startup, contact response, and recovery. A lighter system usually changes angle, distance, or route; a heavier system usually owns direct collision but requires more visible inertia resolution.

## Pressure Geometry

### Duel

```text
shared axis -> attacker takes the centerline -> defender exits at an angle
-> attacker must turn -> counter changes initiative
```

### Group Fight

Use:

- relay: one primary attacker enters; the next arrives during recovery;
- wedge: protagonist drives between opponents and splits the formation;
- funnel: a door, vehicle, table, stair, or alley limits simultaneous attackers;
- rotating triangle: participants exchange foreground, midground, and background roles.

Do not place many equally important attacks in one instant.

Before writing exchanges, make a compact activation ledger. It is a scheduling aid, not extra prose for the final prompt:

| Participant | Distinct silhouette/weapon | Entry and advance cue | Single tactical duty | Active condition | Inactive reason | Exit/end state |
| --- | --- | --- | --- | --- | --- | --- |

Give each opponent one primary duty for the current phrase: initiate pressure, force a turn, threaten a weapon line, block a route, or deliver the peak. Seed the next entry with a visible or audible cue such as a doorway, shadow, reflection, footstep, frame-edge movement or displaced object. Keep non-active opponents out of the immediate lane through distance, obstacles, formation or the previous opponent; do not make them visibly wait for choreography. Once an opponent falls, loses the route or exits, that state persists until a visible recovery source changes it.

### Pursuit

```text
route narrows -> obstacle redirects -> pursuer gains
-> near miss -> elevation or route changes -> escape/interception state
```

### Mounted Or Vehicle Action

Separate:

```text
carrier path and speed
+ rider balance/support points
+ weapon or body action
+ environmental reaction
```

Do not let upper-body action erase traction, gait, suspension, or momentum.

### Creature Or Giant-Opponent Fight

- use scale asymmetry rather than human-sized trading;
- let giant force reach terrain and atmosphere before secondary bodies;
- give smaller actors access points, blind zones, routes, or objectives;
- alternate readable scale with contact evidence.

## Exchange Grammar

```text
intent cue
-> commitment
-> defense/contact
-> receiver reaction
-> recoil and environmental response
-> recovery into a changed state
```

Response families:

- evade: slip, duck, sidestep, retreat, vault, drop level;
- interrupt: intercept, jam, check, redirect;
- defend: block, parry, brace, shield, absorb;
- lose: stagger, slide, fall, drop object, lose route;
- convert: catch momentum, redirect into terrain, turn defense into movement.

Use only responses readable in the chosen framing.

For weapon exchanges, expand the contact:

```text
support/preload
-> weapon acceleration with visible lag or guidance
-> contact orientation
-> both weapons and bodies deflect
-> feet/stance absorb torque
-> weapons settle into new lines
```

### Feed-And-Answer Technique Readability

Use this when the user needs recognizable martial techniques, 套招, 喂招, 对练, or a generated fight has degraded into vague pushing, sticky hands, mutual posing, or unreadable flashes.

Design the fight as clear questions and answers, not free sparring:

```text
attacker feeds one named attack with a readable silhouette
-> defender gives one named answer from a different angle, level, or line
-> contact or near miss is visible at one body point or weapon line
-> both bodies react
-> distance, facing, initiative, or screen position changes
-> only then start the next feed
```

For each exchange, specify:

- feeder: which character starts and what technique silhouette they show;
- receiver: which character answers and how the answer differs in path, level, or range;
- contact point: wrist, forearm, elbow, shoulder, chest line, hip line, weapon edge, or ground;
- consequence: slide, turn, recoil, step-out, loss of centerline, position swap, forced guard, or exposed flank;
- camera job: full-body read before contact, insert only for the contact point, then a wide or medium shot proving the changed state.

Prefer three strong paired exchanges in a 15-second duel. Avoid long continuous forearm contact, undefined clinch, symmetrical hand-fighting, simultaneous attacks with no owner, and energy effects that hide the contact.

### Pressure-Chain Anti-Stiffness

Use this when a generated duel looks rigid, repetitive, push-hands-like, or when one fighter only guards while the other performs.

Design one continuous pressure chain instead of separate "first move / second move / third move" demonstrations:

```text
attacker starts with a disadvantage or urgent objective
-> attacker commits pressure into a clear line
-> defender is clipped, displaced, or forced to answer under cost
-> defender converts that forced movement into one counter
-> attacker adjusts and keeps pressure, with visible fatigue or recoil
-> final beat resolves into a new distance, side, or initiative
```

Every peak must define:

- target body zone: forearm line, shoulder line, ribs line, hip line, guard edge, weapon line, floor, wall, or prop;
- attack method: elbow wedge, shoulder/body check, long-arm whip, palm cut, low step, frame, parry, slip, jam, or redirect;
- receiver reaction: torso fold, shoulder turn, half-step slide, hand touches floor, foot skids, guard collapses, breath breaks, or route changes.

Prefer "pressure-owner versus escape-counter" roles for asymmetric duels. The pressure-owner forces the other person to move; the escape-counter does not look untouchable and should be visibly clipped, rushed, or displaced before countering. If both fighters move beautifully without cost, the exchange reads like dance or posing rather than combat.

For AI-video prompts, avoid phrasing action as a martial-arts syllabus. Say what the current problem is: "male is trying to drive female out of the light lane", "female must survive the centerline pressure and steal the outside angle", "the next hit happens because the previous hit displaced the body." This gives the model causality and removes mannequin-like alternation.

Negative controls:

```text
no equal turn-taking demonstration, no long hand contact, no standing guard receiver, no repeated arm circles, no energy ribbons replacing body contact, no perfect evasion without cost, no final pose before the last second
```

## Environment As Third Participant

Give the environment one functional role per short beat:

- obstacle;
- leverage;
- hazard;
- concealment;
- consequence surface.

It must alter path, timing, support, visibility, or consequence. Decorative sparks do not count.

## Camera Responsibility

Give each beat one camera job:

- orient distance and formation;
- reveal initiative;
- preserve attack line;
- show contact and receiver reaction;
- expose route or obstacle;
- register the changed state.

Use wide/full-body framing for footwork, throws, long weapons, groups, mounted action, and giant scale. Use close framing only for one contact, grip, expression, breath, or decisive object.

Do not cut before receiver reaction and the new spatial state are visible. Do not use camera movement to replace body movement.

## Transfer Matrix

| Mechanism | Transfer target | Control |
| --- | --- | --- |
| punch recoil | sword bind, collision, animal charge | equal-and-opposite response plus changed path |
| footwork angle | chase route, mounted turn, creature evasion | screen direction and support-point change |
| guard and distance | vehicle spacing, formation, predator-prey relation | visible threat zone before commitment |
| impact reaction | debris, cloth, water, crowd, architecture | delayed environmental propagation |
| initiative change | story reversal, route control, objective access | next beat has a new owner |
| recovery | landing, braking, regrouping, weapon reset | inertia resolves before next peak |

## Duration Packaging

- 3-5 seconds: one exchange and one changed state.
- 6-10 seconds: two exchanges with one reversal.
- 13-15 seconds: 4-6 peaks connected by one objective and path; every peak changes position, height, direction, formation, weapon function, or initiative.

Treat these durations as packaging guidance, not a universal action quota. Before generation, budget complexity across shared dimensions:

```text
independent body action
+ support/level change
+ weapon pickup, release or switch
+ newly active opponent
+ camera-side/height/path change
+ major environment-state change
```

A beat is overloaded when several independent transitions must be solved at once or when one transition lacks a readable completion state. Degrade in this order: remove simultaneous secondary actions; merge repeated exchanges; reduce active participants; keep one weapon state; replace a high-complexity throw or ground transition with a clearer displacement; simplify the camera path; localize environment destruction; keep one decisive peak. Preserve identity, geography, the primary action and its consequence before decoration.

For a continuous one-take or multi-phase camera move, extend the mutation ledger only with camera phase and the dominant environmental medium when their current position/direction constrains the next beat. Do not duplicate every local texture into continuity state.

On retry, write a local patch contract:

```text
failed layer:
change only:
preserve unchanged: identity / geography / action order / camera / environment / timing
new completion check:
```

Freeze every unrelated layer explicitly. Rebuild the whole choreography only when the objective, geography or pressure route itself is invalid.

## Failure Diagnosis

| Failure | Missing layer | Next retry variable |
| --- | --- | --- |
| fast but meaningless | objective/state change | add objective and end-state |
| attacker performs alone | response ownership | add defender response and displacement |
| group becomes a pile | formation/depth order | use relay, funnel, or triangle |
| impact feels soft | receiver/environment response | add recoil and delayed consequence |
| camera hides action | too many camera jobs | assign one responsibility |
| weapons feel weightless | support/inertia/recovery | add support and delayed reset |
| heavy and light characters feel identical | actor-relative load missing | assign strength class, direct-stop versus redirect behavior, and different recovery |
| feet skate during contact | traction/base missing | lock foot contact and surface response |
| heavy weapon stops in empty air | braking path missing | add continuation, step, pivot, circular reset, or mechanical damper |
| block has sparks but no force | contact system missing | add weapon deflection, body recoil, and changed spacing |
| giant fight feels tiny | scale asymmetry | make environment receive force first |
| mounted action floats | carrier/rider motions merged | separate path, balance, and action |
| action repeats | state never changes | change distance, elevation, route, or initiative |

Change one primary variable per retry. Preserve successful identity, style, environment, and action layers.

## Preflight

- objective and initiative are explicit;
- starting distance and formation are readable;
- every attack has a response;
- each beat ends in a changed state;
- environment has one functional role per short beat;
- framing can show required body and weapon arcs;
- camera has one responsibility;
- contact evidence has a visible source and correct depth;
- recovery exists;
- persistent combat mutations are inherited by later beats when the fight depends on cumulative damage, fatigue, equipment, terrain, or initiative;
- negatives target the likely failure.
