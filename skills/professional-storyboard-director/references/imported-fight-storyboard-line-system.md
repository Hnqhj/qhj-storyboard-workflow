# Imported Fight Storyboard Line System

Use this reference for 打戏分镜, 动作分镜, 武打/功夫/近身格斗/兵器战, action-PV, or any sequence where fight readability and spectacle depend on posture, force lines, body trajectory, crowd/space lines, or scene-scale impact.

Source basis: three user-supplied Bilibili lessons were reviewed in order: `【打戏分镜】01 动作设计`, `【打戏分镜】02 动态线设计`, `【打戏分镜】 03 场面设计`. This file distills transferable mechanisms only; do not reproduce the original examples or transcript.

## Core Principle

A professional fight storyboard is not built from "cool moves" first. It is built from a readable ladder:

```text
character posture -> force line -> receiver/consequence -> scene-line expansion -> camera/edit support
```

The fight must first say who the fighters are, then show how force travels through bodies, weapons, costumes, crowds, space, and camera perspective.

## Model-Executable Interpretation Layer

When this reference is loaded, convert every abstract craft term into visible, promptable fields. Do **not** output phrases like "strong dynamic line", "big scene", "character posture", or "force transfer" by themselves.

Use this mini-schema for each important fight beat:

```text
Beat function:
Character contrast:
Loaded pose:
Line carrier:
Force path:
Contact / near miss:
Receiver result:
Camera duty:
AI segment limit:
```

Translate terms this way:

- **Posture** = visible stance + weight + guard + torso direction. Example: "low wide stance, rear foot planted, left shoulder forward, elbows folded close."
- **Dynamic line** = `[carrier] moves from [start point] to [end point] in [shape/direction]`. Example: "the spear draws a bottom-left to top-right diagonal from the foreground floor to the opponent's chest."
- **Force transfer** = cause chain + visible result. Example: "right heel plants -> torso twists -> staff sweeps left-to-right -> opponent's upper body folds backward and slides half a step."
- **Scene line** = named foreground / midground / background line. Example: "foreground railing, midground spear row, background corridor beams all point toward the impact."
- **Big scene** = organized line density, not adjectives. State what lines fill foreground, midground, background, and what remains the eye anchor.

Before writing camera movement, fill these five fields:

```text
carrier:
source:
path:
target:
result:
```

If any field is vague, simplify the action instead of adding more camera, VFX, crowd, smoke, blur, or speed words.

### Bad-To-Good Rewrite Rules

Bad:

```text
强动态线，镜头很燃，人物打得很快，场面很大。
```

Good:

```text
主导动态线是长枪：枪尖从右下前景横扫到左上敌人胸口；主角右脚踩稳、腰胯带动枪杆，敌人被扫得向左后方折腰退半步。镜头低位三分之四全身，保持枪杆全长和受力反应都在画面内。
```

Bad:

```text
角色动作阴险，运镜压迫。
```

Good:

```text
角色双肘收紧、重心藏在后脚，先假装后撤；对手前压后，他从对手右肋外侧绕出一条弧线短刺。镜头不抢动作，只做半步侧移，让弧线偷袭和对手转身过慢同时可见。
```

## 1. Action Design Starts From Character

Before designing punches, flips, big perspective, VFX, or camera moves, define the fighters' performance contract.

For each fighter, lock:

- **role/value conflict**: what kind of person enters the fight; what the viewer should support, dislike, fear, or enjoy;
- **shape language**: square/heavy/open, narrow/straight, round/slippery, triangle/sharp, folded/twisted, loose/frantic, compressed/controlled;
- **signature stance**: a readable pose that expresses temperament before contact;
- **movement grammar**: direct, coiling, evasive, explosive, ceremonial, dirty, playful, heavy, floating, precise, reckless;
- **contrast pair**: the opponent's stance and movement must oppose or reveal this fighter, not merely mirror it.

Combat poses are audience-facing information. A stance before or after impact is useful when it creates expectation, value conflict, character bias, or aftermath proof. It is empty decoration when it only copies a martial-arts silhouette without telling us who the character is.

### Shape-to-Action Examples To Reuse

- upright / square / heavy role -> broad base, stable torso, direct line, slower but committed motion;
- elegant / restrained role -> compact guard, smaller preparation, precise line, clean recovery;
- thief / trickster / sneak role -> folded limbs, curved approach, hidden line, delayed reveal;
- arrogant / showy role -> open chest, exposed axis, exaggerated flourish, riskier recovery;
- desperate / feral role -> broken silhouette, low center, uneven rhythm, sudden burst.

If a project gives you similar-looking characters, differentiate them with action silhouettes and force grammar: one straightens, one coils; one plants, one slides; one attacks along a clean line, one creates crooked lines.

## 2. Dynamic Line: Make Force Visible

Fight spectacle comes from visible **line movement**: the viewer sees a clear line form, stretch, travel, collide, bend, or break. The line can be carried by the body, a limb, a weapon, clothing, hair, crowd bodies, architecture, or moving perspective.

Design each action phrase around one dominant force line:

```text
stance / loaded shape
-> force source and direction
-> long readable body or weapon line
-> contact / near miss / bind
-> receiver line response
-> recovery or changed spacing
```

The line is not just a graphic arrow. It is the visible path of force through a performer. When this line reads clearly, the viewer feels impact without needing every punch explained by close-up reactions.

### Line Carriers

Choose the cleanest carrier for the beat:

- **limb line**: fist, forearm, leg, shoulder-to-hand extension;
- **spine/torso line**: twist, bow, lean, recoil, center transfer;
- **weapon line**: blade, staff, spear, pole, chain, rope, firearm barrel, shield edge;
- **costume line**: robe hem, sleeve, sash, coat, dress, scarf, braid, hair, armor tail, ribbon;
- **crowd line**: repeated bodies, unified uniforms, falling extras, group recoil, formation flow;
- **space line**: corridor, scaffold, stairs, beams, rails, doorway, floor grid, city/room perspective;
- **camera line**: push/pull, dolly, crane, spin, whip, or parallax that moves perspective lines.

Do not stack all carriers at once. One primary line plus one supporting line is usually stronger than a noisy frame full of unrelated motion.

## 3. Shot-First Vs Action-First

There are two valid ways to design fight coverage. Pick deliberately.

### Shot-first information design

Use when story information, cause/effect, danger, or geography is the priority.

```text
relationship full shot
-> intent/detail
-> attack
-> reaction/defense
-> result/geography reset
```

Here action performance is a component inside the edit. This is useful for simple beats, comedy beats, damage proof, or when the scene must prioritize narrative clarity.

### Action-first line design

Use when fight spectacle, martial skill, character performance, or physical rhythm is the priority.

```text
pose/line grammar first
-> choose camera that reveals the line
-> cut only when initiative, force, or spatial relation changes
```

Here the camera serves the performance. Avoid cutting a line into fragments before the viewer understands its full force path. The camera should not replace the action; it should make the action readable.

## 4. Scene Design: Scale Comes From Interlaced Lines

A "big fight scene" is not automatically a giant location, huge perspective, many extras, or constant big camera movement. Scene scale comes from how many readable lines are organized across frame depth and time.

Build scale in this order:

```text
single character posture
-> limb/weapon line
-> longer weapon or costume extension
-> spine/torso line externalized by costume/prop
-> group/crowd line field
-> environment perspective lines
-> camera movement animating those perspective lines
```

A small space can feel like a big scene when:

- line movement fills foreground, midground, and background;
- the space has clear directional perspective lines;
- bodies/weapons/costumes repeatedly cross, bend, or answer those lines;
- crowd or extras are simplified into readable moving shapes;
- the camera move adds one clean perspective change instead of random shake.

A large space can feel weak when the lines are unclear, the crowd is just clutter, or the camera movement has no line relationship to the action.

## 5. Practical Fight Storyboard Workflow

When asked for a fight board, use this sequence before drafting shots:

1. **Define the duel contract**
   - Who is direct, who is indirect? Who is heavy, who is flexible? Who owns moral/visual appeal?
2. **Assign signature silhouettes**
   - one static stance, one loaded pose, one recovery pose for each important fighter.
3. **Choose the line carriers**
   - body, weapon, costume, crowd, space, or camera; name the dominant carrier per beat.
4. **Map action phrases**
   - each phrase needs load -> line -> contact/near miss -> receiver response -> changed state.
5. **Lock geography**
   - start/end positions, screen direction, axis, obstacles, route, reset points.
6. **Board camera as support**
   - wider/full-body when the line matters; closer only for trigger, grip, eyes, breath, pain, or consequence.
7. **Escalate line density**
   - do not start at maximum chaos; move from clear character line toward multi-line scene pressure.
8. **Cut by force transfer**
   - cut when initiative changes, line finishes, impact lands, receiver redirects force, or geography must reset.
9. **Hold aftermath**
   - let a pose, displacement, broken object, changed spacing, or silence prove the action.

## 6. AI Video Prompt Translation

For AI-video-ready fight segments:

- one segment should carry one main action phrase and one dominant camera behavior;
- specify the body/weapon/costume line in positive language, not just "fast fight" or "cool martial arts";
- lock fighter silhouettes and screen direction;
- name who owns the camera tracking in the segment;
- avoid asking for several complex attacks, multiple camera moves, crowd chaos, and environment destruction in the same short generation;
- if using first-frame/image-to-video, treat the image as the stance or loaded pose and describe only how the line unfolds.

Useful prompt phrasing:

```text
The fight is designed around one clear force line: [carrier] stretches from [source] to [target], then [receiver/consequence]. Camera [supporting move] keeps the full body/weapon line readable. [Costume/space/crowd] adds one secondary line, not visual clutter.
```

## 7. Fight Storyboard Quality Gate

Before finalizing, check:

- Does the first readable stance tell us character, temperament, or value conflict?
- Are the opponents differentiated by geometry, rhythm, and force grammar?
- Can the viewer see where force starts, where it travels, and what it changes?
- Is at least one full-body or full-weapon view used before fragmenting the action?
- Does each cut happen because information, force, initiative, space, or rhythm changes?
- Does the camera reveal the line rather than hide it behind shake, blur, or random close-ups?
- Does the scene become bigger through organized line density, not only more extras or bigger lens distortion?
- Is the aftermath visible enough to prove impact?
- For AI video, can the segment be generated as one main action spine with one camera owner?

## Avoid

- Starting a fight board with big perspective, big VFX, or flashy camera movement before character and line logic.
- Treating martial poses as generic decoration disconnected from role/personality.
- Cutting every strike into attack/reaction fragments when the performance line should be seen.
- Using crowd, smoke, fabric, weapons, and camera movement all at once without a dominant line.
- Making a "large scene" by adding bodies while the frame lacks clear foreground/midground/background line hierarchy.
- Letting camera aggression replace readable support, contact, receiver response, and recovery.
