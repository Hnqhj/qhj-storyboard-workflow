# Visual Reference Map

Use this map to connect desired feeling with useful AI prompt vocabulary. Names are high-density semantic anchors: preserve selected names in the prompt and add concrete visual instructions only when they clarify role, prevent conflict, or correct a known failure.

## Fast Selection Matrix

| Desired effect | Useful references | Prompt-ready translation |
|---|---|---|
| Awe / wonder | Spielberg shot, slow push-in, reveal shot | slow push-in toward face, eye-line rises toward off-screen wonder, warm backlight, volumetric rays, gradual reveal of scale |
| Psychological shock | Hitchcock dolly zoom / Vertigo effect | subject holds center while background stretches, lens compression changes, sudden realization, unstable perspective |
| Heroic pressure | low-angle hero shot, Obari pose, triangular composition | extreme low angle, wide lens foreshortening, weapon/body forms a strong diagonal, cape/hair flares outward, triangular silhouette |
| Ritual / symmetry | Kubrick one-point perspective, central axis framing | dead-center composition, one-point perspective corridor, rigid symmetry, slow forward tracking, controlled unease |
| Lonely scale | negative space, Antonioni-style isolation | small figure in huge empty environment, wide static frame, large quiet negative space, muted color |
| Neon melancholy | Wong Kar-wai-style color mood, step-printing blur | saturated neon red/green, shallow focus, reflective glass, slow shutter smear, intimate close framing |
| Kinetic chaos | Tony Scott-style cutting, whip pan, handheld | compressed telephoto, aggressive contrast, fast pans, brief motion blur, energetic edits |
| Luxury product polish | tabletop macro, liquid light, controlled specular | macro lens, precise reflections, black cards, glossy highlights, slow slider move, clean negative space |
| Anime impact | Kanada effects, Obari pose, impact frame, speed lines | exaggerated perspective, sharp silhouette, dynamic smear, one-frame burst, debris arcs, high-contrast rim light |
| Pursuit / velocity | tracking shot, Russian arm, low road-level camera | low camera near ground, side tracking with subject, background streaks, stable subject center |
| Suspense reveal | rack focus, foreground occlusion, split diopter | foreground object hides part of frame, focus pulls to background clue, layered depth, controlled reveal |
| Epic scale | extreme wide shot, aerial pullback, silhouette | tiny figure against vast landscape, slow crane/backward pull, rim-lit silhouette, atmospheric depth |
| Screen-breaking impact | naked-eye 3D, FPV ultra-wide, foreground rush | weapon/arrow/fist/foot rushes toward camera, foreground becomes huge, subject silhouette remains readable, very brief peak |
| High-tension action frame | Trigger-like staging, Kanada perspective, Obari triangular pose | extreme low angle, barrel distortion, hard diagonal weapon line, sharp impact frame, black-red contrast, compressed action peak |

## Camera And Director Shorthands

### Spielberg Shot / Spielberg Push-In

Use when the user wants wonder, discovery, emotional reveal, or childlike awe.

Prompt translation:

```text
slow emotional push-in from medium shot to close-up, subject's eyes lift toward an off-screen wonder, warm backlight and floating dust, background gradually reveals a larger scale, gentle lens flare, stable camera
```

Avoid:

```text
random zoom, exaggerated facial morphing, over-bright fantasy glow, uncontrolled camera shake
```

### Hitchcock Dolly Zoom / Vertigo Effect

Use for panic, realization, fear, or the world collapsing around a character.

Prompt translation:

```text
dolly zoom effect, the character remains centered while the background appears to stretch away, uneasy perspective shift, controlled dread, no cutaway
```

Avoid:

```text
spinning camera, warped face, random fisheye distortion
```

### Kubrick One-Point Perspective

Use for ritual, control, dread, cold symmetry, institutional spaces, corridors.

Prompt translation:

```text
perfectly centered one-point perspective, symmetrical corridor, rigid central axis, slow forward tracking shot, cold controlled lighting, unsettling stillness
```

Avoid:

```text
busy angled framing, handheld wobble, random background clutter
```

### De Palma Split Diopter

Use when foreground and background must both matter.

Prompt translation:

```text
split-diopter-like composition, foreground face and distant background object both sharp, strong depth layering, tension between two planes of action
```

Avoid:

```text
flat depth, unclear focus priority, background melting
```

### Tarkovsky Slow Tracking / Sculpted Time

Use for spiritual, dreamlike, memory, rain, fire, water, ruins, slow emotional time.

Prompt translation:

```text
very slow meditative tracking shot, long take feeling, reflective water and drifting smoke, quiet natural textures, time feels suspended, no fast cuts
```

Avoid:

```text
music-video pacing, over-stylized VFX, random surreal objects
```

### Michael Bay Hero Orbit

Use for explosive hero entrance, machine reveal, commercial blockbuster power.

Prompt translation:

```text
low-angle circular dolly orbit around the hero, wide lens, strong backlight, dramatic parallax, moving debris and flaring highlights, heroic scale
```

Avoid:

```text
too many explosions, camera spinning too fast, unreadable subject
```

### Wong Kar-wai Neon Melancholy

Use for intimate urban romance, loneliness, neon nights, memory.

Prompt translation:

```text
close intimate framing, saturated red and green neon reflections, shallow depth of field, glass reflections, slow shutter motion smear, melancholic urban night mood
```

Avoid:

```text
generic cyberpunk, random neon overload, unreadable face
```

## Anime / Dynamic Composition Terms

### Obari Pose / 大张正己式张力构图 / 大张一刀

Use for heroic anime/mecha/body-action impact, weapon pose, oversized silhouette, power entrance.

Prompt translation:

```text
dynamic low-angle anime hero pose, extreme foreshortening, weapon forms a bold diagonal across the frame, chest and shoulders pushed forward, cape and hair flaring outward, triangular silhouette, sharp rim light, explosive stillness before attack
```

Avoid:

```text
broken anatomy, unreadable limbs, random extra weapons, pose too symmetrical
```

### Kanada Effects / 金田系动效

Use for explosive anime motion, lightning, debris, energy arcs, stylized impact.

Prompt translation:

```text
stylized anime impact effects, angular energy shapes, sharp debris arcs, high-contrast speed streaks, one-frame burst feeling, controlled smear frames
```

Avoid:

```text
messy particle soup, generic glowing aura, subject hidden by effects
```

### Itano Circus / 板野马戏

Use for missile swarms, projectile trails, aerial dogfights, chaotic but readable trajectories.

Prompt translation:

```text
dozens of curved missile trails weaving through 3D space, readable spiraling trajectories, camera tracks through the swarm, subject remains clear at center
```

Avoid:

```text
random lines, no depth, explosions covering the subject
```

### Impact Frame

Use for punch, slash, transformation, beat drop.

Prompt translation:

```text
single high-contrast impact frame, black-and-white flash with red accent, silhouette breaks the frame for one instant, then returns to full motion
```

Avoid:

```text
long strobing, text overlays, unclear action direction
```

### Naked-Eye 3D / Screen-Breaking Action

Use for the single strongest action peak: arrow release, blade thrust, chain snap, kick, punch, debris burst, or transformation lock. It should feel like the action crosses the screen plane.

Prompt translation:

```text
naked-eye 3D screen-breaking impact, ultra-wide FPV lens, strong barrel distortion only at the peak, foreground weapon/arrow/foot rushes directly toward camera and becomes huge, background body remains readable, depth lines and debris pull toward the lens, 0.1-second impact frame then return to stable action
```

Chinese:

```text
裸眼3D破屏感，FPV超广角镜头，峰值瞬间产生强烈桶形畸变，前景武器/箭矢/脚尖向镜头猛冲并占据画面，人物主体轮廓仍然清楚，景深线和碎屑朝镜头方向拉伸，0.1秒impact frame后回到稳定动作。
```

Avoid:

```text
全程鱼眼、主体被前景完全遮挡、只有粒子扑脸、没有动作峰值、破屏时间过长导致画面变形。
```

### Trigger / Kanada / Obari Action Pack

Use when the user wants "画面有张力" in action clips. Keep the names; add only the geometry needed for this specific scene.

Prompt translation:

```text
Trigger-like hyper-dynamic action staging, Kanada perspective distortion, Obari-style triangular composition, extreme low-angle ultra-wide lens, foreground weapon exaggerated by foreshortening, strong diagonal lines, black-red high-contrast palette, brief high-contrast impact frame, controlled smear frames and angular energy arcs
```

Avoid:

```text
只堆名字不写镜头、全程乱抖、透视夸张到身体崩坏、特效盖住动作路径。
```

## Composition Terms

### Triangular Composition

Use for power, hierarchy, heroic stance, product hero shots.

Prompt translation:

```text
strong triangular composition, subject forms a stable pyramid silhouette, key prop creates a diagonal leading line, low-angle framing
```

### Dutch Angle

Use for unease, instability, danger. Use sparingly.

Prompt translation:

```text
subtle dutch angle, horizon tilted slightly, controlled psychological tension, subject still readable
```

### Negative Space

Use for loneliness, premium minimalism, scale, quiet.

Prompt translation:

```text
large clean negative space around the subject, small figure placed off-center, quiet empty environment, restrained color palette
```

### Frame Within Frame

Use for voyeurism, entrapment, refined composition, mystery.

Prompt translation:

```text
frame-within-frame composition through a doorway/window/mirror, subject partially enclosed by architecture, layered depth
```

### Foreground Occlusion

Use for cinematic depth, surveillance, reveal, intimacy.

Prompt translation:

```text
soft foreground occlusion partially covers the frame, subject visible through a gap, shallow depth of field, layered cinematic depth
```

## Lighting Terms

### Chiaroscuro / 明暗对照

Use for drama, noir, power, moral conflict.

```text
strong chiaroscuro lighting, one side of the face falls into deep shadow, narrow key light, rich blacks, controlled highlights
```

### Rembrandt Lighting

Use for portrait depth and classic drama.

```text
Rembrandt portrait lighting, small triangle of light on the shadow cheek, soft key light, sculpted face volume
```

### Rim Light / Edge Light

Use to separate subject from dark background.

```text
sharp rim light tracing the hair, shoulders, and weapon edges, dark background separation, metallic highlights
```

### Motivated Lighting

Use for realism.

```text
motivated lighting from visible neon sign/window/fire/screen, light direction consistent with the scene, realistic falloff
```

## Lens / Texture Terms

### Telephoto Compression

Use for pressure, crowds, urban density, pursuit.

```text
telephoto compression, background layers feel close behind the subject, dense city depth, shallow focus
```

### Wide-Angle Foreshortening

Use for action, power, anime impact, dynamic limbs/props.

```text
wide-angle close camera, strong foreshortening, foreground weapon/hand appears large, body recedes dramatically but remains anatomically coherent
```

### Macro Product Lens

Use for tactile detail.

```text
macro lens close-up, shallow depth of field, tiny surface scratches, controlled specular highlights, slow slider movement
```

## Recommendation Patterns

If user says "好运镜":

```text
Offer 3 options: Spielberg push-in for emotional reveal, low-angle orbit for hero power, tracking shot for kinetic movement. Ask only if the shot goal is unclear.
```

If user says "张力构图":

```text
Offer Obari pose / triangular composition / dutch angle / foreground occlusion. Translate each into body pose, diagonal line, lens, and lighting.
```

If user says "高级感":

```text
Avoid vague luxury words. Offer negative space, controlled specular, macro lens, black-card reflections, slow slider, restrained palette.
```

If user says "压迫感":

```text
Offer telephoto compression, low ceiling framing, foreground occlusion, centered symmetry, slow push-in, reduced headroom.
```

If user says "史诗感":

```text
Offer extreme wide shot, aerial pullback, tiny silhouette, atmospheric depth, backlit scale reveal, slow crane movement.
```

## Name Handling

Named references are useful generation anchors, not merely search handles. Prefer anchor-first compression:

```text
Spielberg push-in：用于惊奇揭示，缓慢推近并逐步释放尺度。
```

Instead of:

```text
slow emotional push-in, eyes lifting toward off-screen wonder, warm backlight,
gradual scale reveal, emotional discovery, childlike awe...
```

When the user knows only part of the vocabulary, proactively recommend compatible missing anchors. For living artists/directors, keep any recommendation tightly scoped to a functional reference and provide a short descriptive fallback when useful.
