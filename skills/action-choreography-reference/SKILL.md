---
name: action-choreography-reference
description: "Mandatory action-physics baseline for substantial film/AI-video action, fight, chase, weapon, martial-arts, action storyboard, and kinetic character-PV tasks. Select and preserve martial-art, dance, sport, stunt, partner-movement, and weapon-system anchors, then design choreography using body mechanics, weapon weight, center of mass, balance, leverage, momentum, inertia, traction, recoil, braking, and recovery. Also use for audience-facing fight dramaturgy: 打戏伏笔, 战术道具, 主动权, 翻盘, 可见承诺与兑现. Use for 动作, 打斗, 武戏, 追逐, 武器, 剑斗, 身体运动, fight/chase/choreography, impact plausibility, blocking continuity, or anti-fake-fight diagnosis."
---

# Action Choreography Reference

## Bottom-Layer Reasoning

Apply `think-one-step-further`:

- Solve the dramatic action goal, not only the named technique.
- Make the result directly usable in an image/video prompt.
- Preserve causality from support to motion to consequence.
- Add one guardrail for the next likely generation failure.

## Core Intent

Turn vague action ideas into grounded cinematic movement. Select real martial-arts, stunt, sport, dance, or weapon-handling mechanics, then translate them into safe fictional choreography and AI-video prompt language.

Do not provide practical instructions for harming real people. Focus on visible posture, body line, support, weapon trajectory, rhythm, contact response, camera readability, and fictional performance.

## Foundation Before Style

Always solve the basics before adding style names, weapon names, camera spectacle, or VFX. A named anchor is useful only after the underlying action can stand.

Foundation checklist:

```text
support: what carries the body or weapon weight?
center path: where does the center of mass travel?
distance and angle: who owns the line, who changes line?
setup: why does this action happen now?
contact or near miss: what relation is visible?
reaction cost: what changes in both bodies, prop, or environment?
braking and recovery: how does the action stop or become the next action?
new state: distance, facing, balance, weapon line, initiative, route, or elevation changed?
```

If the answer is unclear, fix the foundation first. Do not add more martial-art names, director names, impact frames, camera moves, particles, or "powerful/dynamic" adjectives to compensate.

When credibility depends on a foot, hand, weapon, partner, wall, ledge, seat, vehicle, creature, hinge, cable, cloth layer, or landing surface, also read `references/contact-constraint-topology.md`. Treat the relation as a temporary physical system:

```text
support/attachment -> load transfer -> relative-motion limit
-> reaction/lag -> release or new constraint
```

Do not animate related bodies or props as independent layers and then try to hide the separation with blur, particles, or camera motion.

When a close exchange repeats clean evasions, silently restores a broken guard, randomizes both hands, or stalls on a grip/bind/control point, read `references/exchange-response-logic.md`. Escalate the response from the current pressure and available space, assign temporary active/support roles, preserve guard-state memory, and convert control into a changed relation or visible release.

## Anti-Imagined-Fight Gate

Do not accept a fight because it feels smooth at first glance. Many AI or intuition-written fights read as continuous in motion but fail under close inspection: the range is wrong, the defender has no real answer, the attacker teleports into a better angle, the receiver reacts before contact, or the next move has no physical source.

For the user's SD2/Seedance prompts, do not present choreography as a visible five-part analytical formula such as "tactical intent -> preload -> attack-line proof -> forced response -> new state." That structure can be used internally to catch missing logic, but it often generates fake-looking posed action when written directly into the prompt. Convert it into the tested natural action-causality style:

```text
When A does [one clear visible action], B is forced into [one visible result].
A immediately uses that result to [next action].
The scene ends this beat at [new spacing / angle / elevation / balance / prop state].
```

In Chinese prompt blocks, prefer "动作因果 → 画面结果" prose:

```text
她从左侧切入，刀背压住纸傀儡手臂，傀儡肩线被带偏，身体被甩向右后方；她不停止，顺着这股偏转绕到背后……
```

This should read like an action director describing the visible shot, not like a martial-arts analysis note.

Before writing or approving choreography, run this check for every exchange:

```text
entry: how did the attacker enter range without gifting a free counter?
control point: what body part, weapon line, balance point, or angle is being controlled?
answer: what does the receiver do—block, evade, jam, get displaced, lose balance, or get forced?
contact proof: is the visible relation a real hit/bind/near miss, not just parallel motion?
range and line: are both bodies close enough, angled correctly, and facing a plausible threat?
force path: where does power come from—foot, hip, shoulder, falling body, weapon inertia, or fantasy source?
cost: what does the action cost either body—step, recoil, slide, turn, brace, stumble, landing, or recovery?
next source: how does the previous state create the next move instead of resetting to a new pose?
state change: distance, angle, balance, elevation, weapon line, initiative, or environment must change.
```

If an exchange only says "attack, dodge, counter, combo" without these relationships, it is an imagined fight. Replace it with a smaller exchange whose control point and receiver response are visible.

## Attack Intent Layer

When ACT / POV / first-person / close action solves motion stutter but the fight still feels fake, inspect the attacker's intent. AI action often fails because it describes movement labels but not the committed purpose of the strike.

For each important attack, define:

```text
tactical intent -> pre-commitment cue -> attack line proof -> forced response -> changed state
```

Use concise, visible intent cues:

- tactical intent: force retreat, break the guard line, steal the inside angle, pin the weapon, cut off escape, lift the target, knock the receiver off-axis, create a finishing window;
- pre-commitment cue: eyes lock on the target line, breath shortens, shoulders/hips coil, grip tightens, stance lowers, front foot bites the floor, weapon is drawn back just enough to load;
- attack line proof: blade edge parts air, cloth snaps behind the strike, water/dust splits along the path, camera/foreground flinches from near-contact, weapon tip or fist has a readable vector;
- forced response: defender's guard is jammed, target is driven a half step, torso folds or rotates, weapon line opens, feet scramble, environment marks the impact;
- changed state: new distance, angle, balance, elevation, weapon line, initiative, or objective access.

Prompt rule: do not write only "he attacks quickly" or "she slashes powerfully". Write the attack as a decision that threatens a specific space:

```text
She commits to cutting off his right-side escape; her stance drops, shoulder and hip coil before release, the short blade tears a narrow line through dust, forcing his guard inward and changing their angle before the next move.
```

Use one or two strong intent cues per beat. Do not overload every limb. For AI video, the model should understand why the action happens and what it forces, while keeping freedom for secondary motion.

## Control Boundaries For AI Video

Do not over-choreograph every limb, hit, cut, and micro-second by default. For AI video, the most reliable action prompts usually lock the boundaries and let the model improvise secondary motion:

```text
movement basis -> start state -> spatial relationship
-> 3-5 required state changes -> contact/mechanism proof points
-> receiver/prop/environment response -> recovery/end state
```

Only hard-lock a micro-action when a reviewed output proved that the model failed that exact detail, such as reversed drag direction, missing foot-triggered activation, wrong first/second action order, weapon morphing, or early terminal pose.

## Action-Budget Integrity

Every required action in a short validation clip must serve the one proof objective. Do not add a decorative slash, flourish, pose, spin, or weapon display merely because the character carries a weapon.

Before retaining a secondary action, ask:

```text
target or obstacle: what does it act on?
contact or near-miss: what visible relation proves it happened?
consequence: what route, spacing, support, object, or state changes?
objective value: does it test the current variable or consume its screen time?
```

If a weapon action has no target/obstacle, no contact relation, and no consequence, remove it from a locomotion, camera, or grounding test. Otherwise the generator may convert it into an idle hero pose and spend the remaining duration displaying the character instead of completing the route.

### Physical Objective Before Graphic Payoff

Do not build the choreography around an abstract graphic objective—crossing slash marks, completing a glowing symbol, drawing a circle around the target, symmetrical hit marks, or "collecting" several decorative contacts—unless the story has already established a concrete mechanism that makes that geometry physically necessary. These ideas often turn the opponent into a passive canvas and replace combat causality with a delayed visual trigger.

For normal fight design, choose the action objective from an immediate physical problem instead:

```text
redirect the committed mass -> exploit the unfinished recovery
disable the loaded limb -> force a support change
enter after the missed swing -> attack the newly exposed line
remove mobility -> lower the target or open the core
use the receiver's reaction -> source the next action
```

VFX may reveal or intensify a result that the bodies, weapon, support, and environment have already made credible. It must not invent the result after a sequence of otherwise inconsequential hits.

## Route-First Topology Variety Gate

When a fight becomes standing exchange, turn-taking, or visually repetitive, do not fix it by adding more named attacks. First lock a continuous route and then vary the action topology inside that route.

Route-first questions:

```text
route: which screen/world direction is pressure traveling?
initiative: who is forcing movement now?
receiver cost: how is the receiver displaced, lowered, turned, lifted, pinned, or destabilized?
reversal source: what physical event allows initiative to change?
finish state: where do both bodies, weapons, and balance end?
```

For short AI fights, phrase the whole beat as pressure travel rather than an equal list of moves:

```text
A drives B from left to right with three different pressures. B never resets to neutral; each contact forces a visible step, slide, crouch, weapon drop, or balance break. At the right edge B plants/brakes/rebounds from the previous impact, then reverses the route and drives A back left. The finish is the route's consequence, not a new unrelated attack.
```

Action variety means changing topology, not merely adding actions. Audit at least three of these axes:

- height: low sweep / midline jam / high descending strike;
- attack plane: horizontal, diagonal, vertical, rising, falling, thrusting, crushing;
- distance: long reach, close body check, weapon bind, disengaged chase;
- support state: standing, crouched, sliding, planted, kneeling, airborne, wall/floor assisted;
- weapon function: edge, spine, pommel, guard, tip, flat, planted brake, dragged mass;
- route direction: press forward, retreat under force, lateral cut, rebound, reversal;
- recovery: over-swing, catch step, weapon drag, regrip, ground plant, torso pullback;
- environment proof: floor scratch, dust burst, water split, object displacement, wall/floor contact.

If several exchanges share the same height, distance, support, weapon function, and route direction, they are one repeated action even if the verbs differ. Reduce named moves and add a route event that changes state.

Avoid writing prompts as:

```text
A attacks, B blocks, A attacks again, B counters, A attacks again.
```

This often generates static crossed weapons and turn-based posing. Prefer:

```text
A's low drag forces B to step over and retreat; the rebound becomes a high descending strike that bends B's guard; A closes the distance and body-checks the weapon line, pushing B to the edge. B plants the weapon tip to stop the slide, drops under A's overcommitment, and uses a rising rebound to steal the route.
```

For fixed-camera or stick-figure tests, the choreography must remain readable without camera cuts, character detail, or VFX. If a simple side-view silhouette cannot prove contact, displacement, reversal, and finish, the full cinematic version will likely become fake action.

## Active Opening Rule

Do not default to a static face-off before action. For most short action clips, start after the pressure has already begun:

```text
mid-action entry / just-hit aftermath / near-contact threat / chase-in / landing recovery / weapon foreground pass / environmental impact already happening
```

Use a standstill guard, mutual stare, or slow pre-fight pose only when the dramatic purpose is ritual, dread, intimidation, or a clearly designed stillness-before-burst beat. Otherwise, the first exchange should begin from an active support state, not a neutral lineup.

## Power Preload and Speed Curve

For action that needs 力量感, 爆发力, or BIP-style animation weight, do not write only "fast" or "high-speed". Strong speed usually reads through contrast:

```text
preload / compression -> short committed burst -> contact or direction change
-> delayed weapon/limb/body follow-through -> visible braking or recovery
```

The preload must be visible before the peak. Use one or more of these readable cues:

- body lowers, widens, coils, or shifts weight into one supporting leg;
- torso/hip turns before the arm or weapon catches up;
- heavy weapon, long limb, cloth, tail, or effect trail lags behind the body line;
- the attack briefly travels opposite its final direction to "load" the strike;
- feet take a small catch step, slide, stomp, wall contact, or crouch before release.

The burst should be brief, not uniformly fast for the whole clip. After the peak, preserve the lag:

- weapon tip/body part continues later than the torso;
- attacker is pulled slightly off-line by the weapon or impact;
- feet chase the center of mass back under the body;
- the next move is sourced by the previous rebound, not by a reset to neutral.

Prompt rule: describe the speed curve and force source, e.g. "a low compressed preload, then one-frame-like dash burst; the oversized blade trails behind and snaps through after the hips turn; he brakes with a sliding catch step." This is usually more reliable than stacking "extremely fast, powerful, dynamic".

## Power-Action Reference Stack

When the user asks to "多找找这种", "自己刷一下", "拉动作", or when a project needs stronger force/spacing, do not rely on one spectacular clip. Build a small reference stack with different jobs:

```text
physical truth reference -> real support, foot pressure, center-of-mass cost, braking
animation spacing reference -> anticipation, smear/burst, pose contrast, readable silhouette
combo structure reference -> how 7-15 seconds change support state, height, route, and peak
weapon-type reference -> how short blade, long pole, heavy sword, shield, fist, or flexible weapon changes body grammar
```

Transfer only the mechanism, not the costume or scene. A good action prompt should borrow:

- from mocap / stunt: support, recovery cost, traction, balance loss;
- from stylized animation: big pose contrast, speed curve, intentional frame density, impact pause;
- from game move sets: distinct attack families and weapon-specific silhouettes;
- from short combo reels: environment-assisted route changes, height changes, and a clear final punctuation.

Guardrail: if every reference is a polished fantasy/game clip, the prompt may become weightless. If every reference is real-life mocap, it may become too ordinary. Keep at least one physical reference and one stylized-spacing reference for high-tension fantasy action.

## Fantasy Power Action Gate

When magic, shadow, qi, psychic force, cursed energy, elemental force, or other fantasy powers participate in an action beat, treat the power as a movement tool with readable cause and effect, not as a replacement for choreography.

Use this compact contract:

```text
source -> tactical function -> visible behavior -> physical/story consequence
```

Keep enough freedom for the video model to perform. Define the power's role and failure boundaries, but avoid writing a mechanical instruction manual unless the user asks for exact mechanism design.

Good prompt control:

- "shadow power misleads the defender, interrupts sightline, and enables off-angle entry";
- "the shadow appears through existing darkness, reflection loss, delayed silhouettes, or swallowed light";
- "the result is a changed weapon line, dropped object, broken balance, changed position, or lost initiative."

Avoid over-controlling:

- naming every sub-mechanism such as shadow cable, shadow nail, shadow hand, shadow clone when only the general power behavior matters;
- turning the power into a black-screen transition that hides the required contact or consequence;
- letting supernatural force skip response cost, contact evidence, displacement, or recovery;
- using a color-coded energy effect that contradicts the intended world palette.

For stealth / rogue / assassin fantasy action, use powers as concealment, misdirection, line theft, repositioning, or objective access. Do not let the character become a frontal mage, projectile caster, or armored duelist unless that is the user's new intent.

## Action Reference Research Gate

For nontrivial fights, repeated action failures, unfamiliar martial systems, or when the user says "联网搜动作戏", "套招", "喂招", "招式看不出来", "动作僵", "打法/体态有问题", do not keep inventing choreography from intuition.

Before the next prompt, use `$creative-research-first` and/or `$reference-hunting-board` to inspect real action references: martial demonstrations, fight choreography, stunt breakdowns, dance/sport movement, weapon handling, game/animation action studies, or the user's own successful clips.

Extract movement grammar rather than move names alone:

- stance height, guard, shoulder/hip relation, foot pressure, and recovery posture;
- attack line, defensive answer, contact plane, rebound, displacement, and initiative change;
- support/base path, center-of-mass route, traction, braking, and loss/recovery of balance;
- partner distance, angle, timing, feint, entry, exit, and why the next exchange begins;
- environmental proof: floor marks, clothing drag, object displacement, dust/water/steam reaction, crowd or creature response;
- camera proof: which shot needs feet, which needs contact point, which needs two-body spacing, and which can become an insert.

After two failed action retries on the same project, stop producing another full prompt until there is a reference-backed action grammar or a clearly inspected output diagnosis.

## Motion-To-Prompt Extraction Gate

When the user asks to read existing actions, 单招, 动势, whitebox previews, mocap clips, game animations, or "总结动作提示词怎么写", read `references/action-prompt-grammar-from-motion.md` before writing.

Use the source action as a movement grammar reference, not as a filename or move-name label. Extract:

```text
intent -> start state -> preload -> route -> speed curve
-> peak -> follow-through -> brake -> end state -> next-source
```

For single actions, preserve force source, route, peak, inertia, and recovery. For combos, connect actions by reusing the previous end state as the next preload; do not write unrelated moves as a list.

In final prompt language, prefer natural action causality over analysis headings:

```text
上一刀拖到身后低位，不回正；后脚滑步追上重心，借剑身回弹把身体带成反向转髋，第二刀从背后低位斜上挑出。
```

Reject wording that only says "fast", "powerful", "dynamic", "cool", or "combo" without support, route, peak, follow-through, braking, and connectable end state.

## Full-Body Locomotion Grounding Gate

When full-body walking, running, pursuit, stairs, slopes, rubble travel, landing, stopping, turning, or leg-garment interaction is visible and important, read `references/full-body-locomotion-grounding.md`.

Treat locomotion as one coupled loop:

```text
support/contact -> center-of-mass transfer -> push-off/flight
-> terrain response -> secondary motion -> camera-relative motion
```

Activate only the layers the framing can prove. Do not inject foot IK, contact-shadow, cloth-collision, or camera-cadence jargon into close-ups, flight, or unrelated action. Translate technical names into visible outcomes and keep renderer/solver terms only as optional compression anchors.

## Workflow

1. Identify the action goal: power, speed, elegance, brutality, evasion, precision, ritual, stealth, monster scale, or anime exaggeration.
2. Identify the moving system: empty hand, kick, grappling, blade, staff, spear, bow, chain, axe, hammer, shield, transforming weapon, vehicle, creature, or chase.
   - When a generated reference image exists, treat its visible geometry as authoritative over the earlier design prompt. Reclassify the weapon from the image: total length, blade-to-handle ratio, grip spacing, center-of-mass tendency, edge orientation, and likely braking space.
3. Inventory any movement names supplied by the user. Do not assume the list is complete. When a recurring character already has an approved combat identity from `$character-continuity-bible`, inherit its primary basis, role, preferred range, force/rhythm/recovery signature, and drift boundary; vary tactics for the current opponent without silently replacing the durable profile.
4. Run a movement-anchor gap audit for each performer:
   - body locomotion or martial basis;
   - weapon-handling basis;
   - partner interaction or mounted/carrier relation;
   - fantasy amplification.
   Proactively recommend the most suitable names from martial arts, dance, sport, stunt, circus, historical fencing, or object manipulation. Research unfamiliar or uncertain systems before using them.
   If the user is criticizing stiffness, unclear technique, repeated action, bad 套招/喂招, or weak body method, run the Action Reference Research Gate before writing the next choreography.
5. Define the action grammar before listing action events:
   - one primary movement or martial basis;
   - at most one secondary basis for route, weapon, or fantasy function;
   - stance and body level;
   - force path and dominant geometry;
   - rhythm and recovery signature;
   - recurring support-state or silhouette motif.
   Preserve the selected basis name as a compact semantic anchor. Add visible mechanics only when needed to distinguish its expression, adapt it to a weapon/body, or prevent a known failure. “Run, climb, attack, block, slash” describes tasks but does not create a distinctive performance language.
   For showcases with several peaks, audit movement topology as well as style: each peak should differ in trajectory plane, weapon end/function, support state, body level, travel direction, or recovery state. Several circularly worded actions are still one repeated action.
6. Build a physical profile when weight or contact matters. Read `references/weapon-body-dynamics.md`:
   - actor mass and strength relative to the prop;
   - weapon length, grip, and mass distribution;
   - support/base of support and traction;
   - force chain, peak relation, braking, and recovery.
   - If terrestrial full-body travel is a primary proof task, also read `references/full-body-locomotion-grounding.md` and audit support phase, surface contact, terrain adaptation, secondary motion, and camera-relative velocity as one system.
   - If the beat depends on carrying, gripping, riding, climbing, bracing, grappling, tethering, hinging, sliding, jumping, landing, or body-surface support, also read `references/contact-constraint-topology.md` and define the relation, load path, visible proof, and release state.
7. Choose and retain a martial or stunt basis by name, then verify that its visible mechanics suit the scene:
   - read `references/martial-arts-visual-mechanics.md` for broad style selection;
   - read `references/action-reference-map.md` for concrete actions and prompt phrases.
8. For each action, describe:
   - visual purpose;
   - stance, body path, and center-of-mass change;
   - prop or weapon line, arc, lag, or tension;
   - defender/receiver/environment response;
   - follow-through, braking, and stable end state;
   - prompt-ready wording and failure-specific negatives.
   For a head-heavy or tip-heavy weapon, name the legal hinge between different planes: brake, plant, catch, widen grip, slide one hand, shorten the lever, or settle into a new guard. Do not demand uninterrupted momentum through an impossible horizontal-to-vertical direction change.
9. For two or more participants, assign contrasting but compatible grammars, then use the interaction loop in `references/action-reference-map.md`. When the exchange has repeated evasion, instant guard reset, random limb use, or stalled control, also read `references/exchange-response-logic.md` and define response escalation, active/support roles, guard-state memory, and control conversion. Consider Contact Improvisation or Partner Acrobatics when shared weight, catches, shoulder support, counterbalance, or linked rotation is central. Never choreograph each person as an unrelated solo.
10. For a full fight, group fight, pursuit, mounted action, creature fight, or retry, read `references/fight-system.md`. When the sequence depends on a planted advantage, threatened objective, tactical reversal, environmental setup/payoff, or finishing opportunity, also read `references/fight-dramaturgy-and-payoff.md`; keep a visible promise/payoff ledger backstage. When an earlier impact, fatigue, equipment damage, altered terrain, or lost initiative must constrain later exchanges, also read `references/combat-impact-state-progression.md`; retain a compact mutation ledger and impact grade rather than prescribing every microsecond.
11. Hand timing to `$action-rhythm-editing`, shot readability to `$cinematic-audiovisual-language`, audio mass to `$cinematic-music-sound-design`, and final packaging to `$jimeng-sd2-prompting`.

## Action Physics Contract

Before finalizing a weighted action, answer:

```text
Actor versus weapon strength:
Weapon mass distribution:
Support/base of support:
Force chain:
Contact or near-miss response:
Follow-through and braking:
Stable end state:
```

If any field is missing, the action may look stylish but will probably read as weightless or unsupported.

## Hit-Acknowledgment Triad

For every **principal hit** whose job is to prove that someone was truly struck, do not stop at body squash, pose displacement, camera shake, or particles. The receiver must acknowledge the hit through three coordinated channels:

1. **Structural response**: local compression or deflection at the contact point propagates through the head/shoulder/spine/hip/guard and into a corrective step, slide, fold, turn, or loss of line.
2. **Performance and physiological response**: when the face is readable, the expression changes in the direction and intensity of the impact—blink or eyelid squeeze, brow compression, jaw or cheek displacement, gaze break, breath interruption, short exhale, delayed guard return, or brief loss of focus—then recovers into the next intention. Do not keep an unchanged cool face through a confirmed heavy hit.
3. **Synchronized audio response**: contact transient, clothing/body sound, breath or restrained grunt, foot scrape, surface response, and room/space resonance align with the visible hit and its aftermath. Sound confirms material, distance, and consequence rather than decorating the cut.

Body deformation without performance and audio acknowledgment often reads as rubbery animation rather than impact. Conversely, facial acting or loud sound without structural force transfer reads as a fake hit. The three channels may be distributed across a contact view and a very short reaction view, but they must belong to the same causal event.

Do not apply the full triad at maximum intensity to every touch. In a dense short fight, normally designate only one to three hero hits for full acknowledgment. Minor contacts use compressed proof such as guard vibration, cloth snap, micro-blink, breath tick, foot correction, or short recoil so the fight stays fast. Reaction duration scales with impact grade and must not turn the receiver into a frozen performer.

## Output Shape

```text
Action objective:
Physical profile:
Action grammar:
Primary martial/stunt basis:
Optional secondary basis:
Visible signature:
Start and support:
Body and weapon path:
Peak/contact response:
Follow-through and recovery:
Camera readability:
Paste-ready prompt:
Negative constraints:
```

For a complete beat:

```text
Setup -> commitment -> contact/near miss -> receiver response
-> shared recoil/environment response -> braking -> changed end state
```

## Guardrails

- Prefer one readable exchange per short clip; split complex fights.
- Avoid boring default openings where fighters stand posed before starting. Begin from active pressure unless a standoff is the explicit hook.
- Do not let reference names replace foundation. First prove support, center path, distance, contact/near miss, reaction, braking, recovery, and changed state.
- Define a recurring movement grammar before writing action verbs. Do not expect a list of tasks to create beautiful choreography.
- Do not continue prompt-patching a failed fight from imagination after repeated action failures. Inspect the output and at least one relevant movement/action reference, then redesign the exchange grammar.
- Do not wait for the user to name the movement system. Proactively recommend one primary body basis and, when useful, one separate weapon or partner basis.
- Keep martial-arts, dance, sport, and stunt names in the prompt as high-density movement anchors. Clarify them with a few signature mechanics when useful; do not replace a precise name such as Capoeira with a long generic paraphrase.
- Treat weight as mass distribution plus actor-relative load, not one adjective.
- Do not stack circular footwork, circular sweep, body orbit, overhead wheel, circular camera, and circular effects as if they create variety. They reinforce one repeated loop.
- For heavy weapons, continuity does not mean motion never stops. Use intentional punctuation: committed action -> visible brake/catch -> regrip or guard -> different action plane.
- Do not animate the weapon originally requested if the generated reference visibly produced a different weapon class. Preserve the actual asset and redesign the movement grammar around it.
- Keep the center of mass supported or show the required step, slide, fall, brace, cable, wall, vehicle, or airborne phase.
- Keep anatomy and intent readable: start pose, force line, peak, follow-through, recovery.
- Do not trust apparent continuity alone. If the range, control point, receiver answer, force path, cost, and next-source logic are not visible, the fight is probably imagined even if it looks fluid.
- If a fight becomes standing, turn-based, or repetitive, solve route and topology before adding more attacks: one continuous pressure path, one visible reversal source, and varied height/plane/distance/support/weapon function.
- Map every attack to a defense, contact, near miss, or displacement response.
- Require a state change in distance, angle, balance, weapon state, route, elevation, initiative, or objective access.
- Describe weapon edge/point direction, grip-relative balance, support, inertia, braking, and recovery rather than tactical harm details.
- Superhuman strength must move force into the weapon, floor, air, target, or environment; it must not erase recoil and inertia.
- Use camera shake, sparks, particles, and blur only as secondary evidence.
- For principal hits, require structural force transfer, receiver performance/physiology, and synchronized impact sound. Treat unchanged facial expression, silent contact, or body squash alone as incomplete hit acknowledgment.
- Mark uncertain niche techniques with `?` and provide a descriptive alternative.
