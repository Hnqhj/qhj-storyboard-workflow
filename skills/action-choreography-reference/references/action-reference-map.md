# Action Reference Map

Use this map to proactively suggest practical movement-name anchors for fictional AI-video action. Preserve the selected name and add visible motion or camera language only when it improves differentiation, physics, or readability.

Before selecting a named move:

- read `weapon-body-dynamics.md` when weight, balance, contact, strength difference, or transformed handling matters;
- read `martial-arts-visual-mechanics.md` when choosing among martial systems or when styles keep looking identical.

## Fast Selection Matrix

| Desired action feeling | Useful references | Prompt-ready translation |
|---|---|---|
| Heavy brutal punch | boxing cross, overhand, hammer fist | shoulder and hip rotate together, weight drops into strike, short explosive contact, head snaps from impact, strong follow-through |
| Fast evasive striking | boxing slip + counter, Wing Chun chain punches, Jeet Kune Do intercept | small head movement, tight centerline, quick counterattack, minimal wind-up, close camera |
| Ruthless close combat | Muay Thai clinch knee, elbow strike, dirty boxing | close-range body lock, short knees/elbows, sweat and cloth movement, cramped handheld frame |
| Elegant leg attack | Taekwondo spinning hook kick, wushu crescent kick, capoeira meia lua | circular leg arc, torso rotation, hair/cloth trail, freeze at peak extension |
| Throw / slam | judo osoto gari, hip throw, aikido irimi-tenkan | off-balance entry, body rotation, opponent lifted/redirected, clear floor impact beat |
| Ground scramble | wrestling sprawl, shoulder roll, parkour safety roll | low center of gravity, hands touch ground, body rolls through shoulder, quick recovery |
| Sword precision | iaido nukitsuke, kesa-giri, HEMA oberhau/zornhau | blade flashes out of scabbard, diagonal cut line, hips lead, clean follow-through |
| Heavy sword power | zweihander moulinet, greatsword descending cut | broad two-handed arc, weapon weight pulls body, delayed recovery, sparks on contact |
| Staff flow | bo staff figure-eight, quarterstaff moulinet | continuous figure-eight arcs, both hands slide along shaft, spinning parallax trail |
| Spear reach | spear thrust, naginata sweeping cut | long linear extension or wide crescent sweep, back foot drives forward, weapon tip leads |
| Knife tension | reverse-grip slash, close parry, ice-pick silhouette | compact arm motion, blade stays near body, sudden short slash, intense close framing |
| Chain / flexible weapon | rope dart, meteor hammer, kusarigama-inspired arc | circular momentum, delayed trailing weapon, chain forms readable curve, dangerous orbit |
| Bow action | kyudo draw, horseback archery silhouette, trick-shot release | slow ceremonial draw, shoulder line opens, string tension visible, arrow release and recoil |
| Chase / escape | parkour vault, wall run, kong vault, slide under obstacle | hands plant on obstacle, knees tuck, camera follows low and close, quick landing recovery |
| Anime superhuman | wushu aerial, capoeira spin, Obari pose + impact frame | real move base plus exaggerated hang time, sharp silhouette, speed smear, impact pause |

## Reality-To-Fantasy Escalation Pattern

Use this when a realistic movement reference feels too plain for fantasy/action AI video. Real action should supply body mechanics, not limit the idea.

Build each action in three passes:

1. **Reality base**: choose footwork, leverage, grip, shoulder line, center of gravity, landing, recoil, or weapon arc from a real action.
2. **Fantasy weapon function**: add one clear fictional use of the prop: bow as double-edged blade, shield/parry frame, chain hook, energy string lash, ground anchor, telescoping strike, recoil jump, or magnetic return.
3. **Cinematic exaggeration**: add a short peak with foreground pass, over-perspective, impact frame, airflow/debris, or naked-eye 3D rush.

Prompt pattern:

```text
动作以[真实参考]作为重心和发力基础，但武器按幻想功能运作：[功能1] + [功能2]；每个幻想功能都有清晰身体支点、武器轨迹和短促峰值，不是普通武术演示。
```

Examples:

```text
bow action -> moving archer shoulder line + parkour slide footwork + bow-blade close slash + energy arrow release
heavy weapon -> greatsword body weight + ground-anchor lock + recoil shockwave
chain weapon -> rope-dart orbit + hook-and-chain delayed follow-through + foreground 3D chain snap
```

Avoid:

```text
只写真实武术名称、只做普通武器使用、幻想功能没有身体支点、动作峰值全靠粒子特效。
```

## Multi-Participant Interaction Loop

Use this for any fight involving two or more bodies. Treat the fight as one causal system rather than separate performers.

```text
readable guard and distance
-> attacker transfers weight and commits to one path
-> defender evades, blocks, parries, absorbs, or is displaced
-> contact produces recoil in both bodies and the environment
-> both recover into a changed distance, angle, or advantage
```

Every exchange must answer:

- Who initiates?
- What exact line or arc enters the shared space?
- Does the defender evade, interrupt, block, absorb, or lose balance?
- Where does each body end relative to the other?
- What visible contact evidence appears: recoil, foot slide, cloth snap, dust, water, debris, sparks, breath, or sound?
- Who owns the next beat?

Prompt pattern:

```text
The attacker commits from [start distance] along [clear line/arc]. The defender [specific readable response], causing [contact or near-miss evidence]. Both bodies show equal-and-opposite recoil and recover into [new distance/angle/power relation], ready for the next beat.
```

For three or more participants, use a relay rather than simultaneous chaos:

```text
A pressures B -> B redirects A while C enters -> B must turn or change level to answer C -> the formation resolves into a new readable triangle.
```

Avoid:

```text
everyone attacks at once, each character performs a solo combo, blows land without receiver reaction, defender waits motionless, bodies overlap without depth order, contact has no recoil, camera cuts before the spatial result is visible
```

## Empty-Hand Striking

### Boxing Cross / Overhand

Use for direct power, grounded realism, street-level impact.

Body path:
Rear foot drives, hip and shoulder rotate, fist travels straight or arcing over the guard, torso compresses on contact.

Prompt:

```text
grounded boxing cross, rear hip and shoulder rotate together, short explosive contact beat, knuckles land with visible recoil, sweat and jacket fabric snap from the force, no exaggerated wind-up
```

Avoid:

```text
rubbery arms, slow floating punch, fist missing target, random spinning
```

### Boxing Slip + Counter

Use for smart, fast, realistic close combat.

Prompt:

```text
fighter slips just outside the incoming punch by a few inches, head moves off the centerline, immediately returns a compact counterpunch, tight footwork, close handheld camera
```

Avoid:

```text
huge dodge, teleporting body, unclear attack direction
```

### Muay Thai Clinch Knee / Elbow

Use for brutal close-range fight beats.

Prompt:

```text
close-range Muay Thai clinch, one fighter controls the opponent's posture, short upward knee strike, sharp elbow follow-through, sweat spray and fabric tension, cramped handheld frame
```

Avoid:

```text
long-range flying knees, tangled unreadable limbs, gore-focused detail
```

### Wing Chun Chain Punch / Centerline Pressure

Use for rapid forward pressure in narrow spaces.

Prompt:

```text
rapid centerline chain punches, elbows tucked, shoulders relaxed, small advancing steps, opponent driven backward through a narrow corridor, hands blur but torso remains stable
```

Avoid:

```text
windmill arms, extra hands, no body weight behind strikes
```

## Kicks And Acrobatics

### Taekwondo Spinning Hook Kick

Use for elegant high-impact head-level attacks.

Prompt:

```text
spinning hook kick, torso turns first, kicking leg whips in a horizontal arc, heel passes across the target line, hair and coat trail behind, brief freeze at full extension
```

Avoid:

```text
broken knees, impossible hip angle, endless spinning
```

### Capoeira Meia Lua de Compasso

Use for beautiful low-to-high circular attacks and stylized evasive motion.

Prompt:

```text
capoeira meia lua de compasso inspired movement, hands briefly touch the floor, torso folds low, leg sweeps in a wide circular arc, camera stays low to emphasize the spinning line
```

Avoid:

```text
random breakdance, no target line, body floating without hand support
```

### Wushu Butterfly Kick / Aerial

Use for fantasy, wuxia, anime exaggeration, elegant evasion.

Prompt:

```text
wushu butterfly kick, body travels horizontally through the air, torso nearly parallel to the ground, both legs carve a sweeping arc, silk sleeves trail in a spiral, landing controlled
```

Avoid:

```text
gravityless endless flight, folded limbs, unclear landing
```

## Grappling, Throws, Falls

### Judo Osoto Gari / Outer Reap

Use for clean, readable takedown.

Prompt:

```text
judo outer reap inspired throw, attacker steps close, shoulder line breaks the opponent's balance, rear leg reaps behind the opponent's leg, opponent falls in a clean arc, mat/floor impact beat
```

Avoid:

```text
teleport throw, no contact, tangled legs
```

### Hip Throw / Shoulder Throw Silhouette

Use for heroic or street-fight throws.

Prompt:

```text
hip-throw silhouette, attacker turns their back under the opponent's center of gravity, hips load the opponent, then a sharp rotation flips them over the shoulder, clear airborne arc
```

Avoid:

```text
spine-twisting anatomy, opponent levitating without leverage
```

### Parkour Roll / Safety Roll

Use for landings after jumps, falls, chase scenes.

Prompt:

```text
parkour shoulder roll, character lands into one shoulder, body rolls diagonally across the back, momentum continues into a low crouch and immediate run
```

Avoid:

```text
flat face-first fall, frozen landing, no recovery step
```

## Blades

### Iaido Nukitsuke

Use for sudden draw-cut, assassin, samurai, clean first strike.

Prompt:

```text
iaido-inspired draw cut, left hand anchors the scabbard, blade flashes out in one smooth horizontal line, hips turn with the draw, cut finishes in a controlled low guard, minimal wasted motion
```

Avoid:

```text
blade already floating outside the scabbard, extra swords, messy random slashes
```

### Kesa-Giri / Diagonal Cut

Use for readable sword attack across the body.

Prompt:

```text
kesa-giri diagonal sword cut, blade travels from high shoulder to opposite low hip, body weight drops through the cut, cloth and hair follow the diagonal line, clear follow-through
```

Avoid:

```text
unclear edge direction, sword bending, repeated random slashes
```

### HEMA Oberhau / Zornhau Inspired Cut

Use for grounded European longsword action.

Prompt:

```text
two-handed longsword descending cut, hands high then drive diagonally downward, hips and front foot commit to the strike, blade edge catches a sharp highlight, heavy controlled recovery
```

Avoid:

```text
one-handed greatsword, weightless weapon, anime-only float unless requested
```

### Knife Reverse-Grip Slash

Use for tense close-up danger, stealth, cramped fights.

Prompt:

```text
compact reverse-grip knife slash silhouette, elbow stays close to the ribs, blade arcs only a short distance, sudden close-range motion, face and blade share the frame
```

Avoid:

```text
large theatrical swings, tactical instruction detail, gore focus
```

## Staff, Spear, Polearms

### Bo Staff Figure-Eight

Use for flowing defensive/offensive staff motion.

Prompt:

```text
bo staff figure-eight flow, both hands guide the staff through continuous crossing arcs, the wooden tip traces a clean motion trail, stance shifts forward and back, robe sleeves trail behind
```

Avoid:

```text
staff clipping through body, extra hands, random baton twirling with no stance
```

### Spear Thrust

Use for reach, precision, military formation, monster hunting.

Prompt:

```text
long spear thrust, rear foot drives forward, hands slide to extend reach, spear tip leads in a straight line toward the target, body remains behind the weapon, strong recoil recovery
```

Avoid:

```text
short sword-like swinging, spear bending, no line of attack
```

### Naginata / Glaive Sweeping Cut

Use for elegant wide arcs with a long blade.

Prompt:

```text
naginata-inspired sweeping cut, long polearm blade travels in a wide crescent arc, hips rotate first, lower stance anchors the motion, blade edge flashes through the air
```

Avoid:

```text
unreadable weapon length, blade passing through floor, weightless spin
```

## Flexible And Unusual Weapons

### Rope Dart / Meteor Hammer Inspired Arc

Use for supernatural assassins, fantasy weapons, chain blades.

Prompt:

```text
rope-dart inspired circular momentum, weighted blade trails behind the hand, chain forms a readable curved orbit, weapon accelerates around the body before snapping forward, camera holds wide enough to see the full arc
```

Avoid:

```text
chain spaghetti, random glowing lines, weapon clipping through face/body
```

### Kusarigama-Inspired Hook And Chain

Use for hooked blade plus chain control, gothic weapons, scythes.

Prompt:

```text
hook-and-chain weapon choreography, sickle blade stays close in the lead hand while the chain weight circles outside the body, delayed chain follow-through, dark cloth strips whip with the motion
```

Avoid:

```text
too many chains, unreadable silhouette, practical trapping instructions
```

### Axe / Hammer Heavy Arc

Use for brutal fantasy, heavy warrior, monster impact.

Prompt:

```text
heavy axe overhead swing, weapon weight pulls the shoulders back before the drop, knees bend, torso folds into the impact, floor cracks/debris react at the contact beat, slow recovery
```

Avoid:

```text
weightless fast fluttering, tiny impact, broken wrists
```

## Bow And Projectile Choreography

### Kyudo-Inspired Ceremonial Draw

Use for elegant, ritualistic archery.

Prompt:

```text
kyudo-inspired slow ceremonial draw, archer opens the shoulders into a wide T-shape, bow arm steady, string hand draws to the cheek, breath pauses before release, arrow leaves with subtle string recoil
```

Avoid:

```text
rubbery bow, arrow appearing from nowhere, impossible grip
```

### Horseback / Moving Archery Silhouette

Use for dynamic fantasy riders or running archers.

Prompt:

```text
moving archer silhouette, torso twists opposite the running direction, bow remains level while the lower body keeps moving, cloth and hair trail backward, release timed at the peak of motion
```

Avoid:

```text
unstable bow size, arrow bending, character changing direction every frame
```

### Fantasy Bow-Blade Mobile Showcase

Use for stylized mechanical bows, scythe-bows, bladed bows, energy-string bows, or other fantasy weapons that should not feel like ordinary archery.

Visual goal:
Real movement supplies weight, foot contact, and shoulder mechanics; fantasy design supplies the weapon functions and exaggerated visual peaks.

Prompt:

```text
mobile fantasy bow-blade choreography, the character keeps changing position while using the small mechanical bow as a short bow, double-edged blade, guard, and energy-string weapon; moving shots happen during sprinting, sliding, retreating, turning, and landing, with short red energy-arrow releases, clear bowstring recoil, foreground blade passes, and sharp anime-impact silhouettes
```

Useful body bases:

```text
moving archer silhouette for shoulder line and release timing; parkour slide or low dodge for displacement; reverse-grip short-blade slash for close transitions; wushu aerial only as a brief jump-and-land accent, not floating flight
```

Avoid:

```text
standing in place, long aiming holds, repeated draw-and-release poses, ordinary archery demonstration, weapon used only as a bow, no foot displacement, weapon scale drift, extra bow copies
```

### Giant Bow Borrowed-Force Draw

Use when the bow is too large or heavy to draw by hand. The action should show leverage, support points, and strain rather than effortless archery.

Useful body bases:

```text
kyudo shoulder opening for clean aim; compound-bow cam tension for mechanics; gymnastics handstand or capoeira inverted support for leg-powered draw; strongman deadlift posture for full-body strain; parkour landing recovery after release
```

Prompt:

```text
giant bow borrowed-force draw, the archer cannot pull by hand alone; she braces the bow against the ground or her body, hooks both feet into red cable stirrups, uses core and leg extension to pull the string while arms stabilize the central grip, cams and pulleys rotate under heavy tension, airflow spirals toward the arrow before release
```

Hero variation:

```text
inverted hero archery pose, one or both hands support the body near the bow grip, legs open in a powerful V-shape, both feet hook the red bowstring loops and draw backward, the giant bow towers around her like a crescent frame, extreme low-angle wide lens, triangular Obari silhouette
```

Avoid:

```text
ordinary standing archery, one-hand draw, relaxed posture, no support point, feet clipping through string, broken hips/knees, bow changing size during draw
```

## Chase And Stunt Movement

### Kong Vault

Use for fast obstacle crossing.

Prompt:

```text
parkour kong vault, both hands plant on the obstacle, knees tuck tightly between the arms, body passes forward over the barrier, lands into a run without stopping
```

Avoid:

```text
floating over obstacle, no hand contact, broken knee path
```

### Slide Under Obstacle

Use for chase, gunfire avoidance, narrow escapes.

Prompt:

```text
low slide under a closing obstacle, one leg extended, one knee bent, torso leans back, coat drags across the floor, camera tracks at ground level
```

Avoid:

```text
body clipping through floor, obstacle not aligned, no momentum
```

### Wall Run / Wall Kick

Use for wuxia, parkour, fantasy escape.

Prompt:

```text
brief wall run, character plants one foot against the wall, pushes off diagonally, body rotates back into the corridor, lands in a low crouch
```

Avoid:

```text
endless wall walking, gravityless float, no contact shadow
```

## Prompt Assembly Pattern

Use this for action video:

```text
[Character] performs a [reference action] in [scene].
Start pose: [stance/readable silhouette].
Motion path: [body path + weapon/prop arc].
Peak beat: [impact/contact/pause].
Follow-through: [recovery/landing/recoil].
Camera: [wide enough to read full body, or close enough for impact].
Constraints: keep anatomy coherent, one clear action beat, no extra limbs/weapons, no teleporting, no gore unless requested.
```

## AI Video Stability Rules

- For 5 seconds, use one move: setup -> execution -> recovery.
- Keep full-body framing for acrobatics, throws, staffs, chains, and weapons with large arcs.
- Use close framing only for punches, knife tension, eye-line, or impact reactions.
- Add "brief impact pause" when the action needs weight.
- Add "clear follow-through" so weapons do not stop unnaturally.
- For chain/flexible weapons, force a readable arc and wide framing.
- For throws, specify contact and leverage visually, not tactical steps.
- For bow shots, lock bow size, string tension, arrow position, and release recoil.
- For fantasy weapons, make the real-world reference the motion base, not the ceiling. Add one or two explicit fictional functions so the result feels designed instead of merely realistic.
- For 15-second action showcases, include mobile footwork and cross-frame travel; otherwise AI video tends to turn the clip into repeated standing poses.

## Common Negative Blocks

```text
禁止肢体变形、额外手臂、额外武器、武器穿模、动作漂浮、无重力旋转、人物瞬移、镜头乱切、目标方向不清、血腥细节、文字水印。
```

For weapon actions:

```text
保持武器长度和握持方式稳定，刀刃/枪尖/棍端轨迹清晰，禁止武器忽大忽小、穿过身体、凭空复制。
```

For acrobatics:

```text
保持起跳点、最高点、落地点连续，禁止空中停滞过久、膝盖反折、落地无接触阴影。
```
