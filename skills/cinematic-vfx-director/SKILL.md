---
name: cinematic-vfx-director
description: "电影级 VFX 设计、路由、编译与审计：冲击闪光、冲击波、武器轨迹、速度拖影、魔法能量、烟火水、天气、变身生长、破坏、碎屑、火花、环境响应、自发光与合成整合。触发：特效廉价、脱节、不可读、过曝或遮挡动作。 Design, route, compile, and audit cinematic visual effects for AI video and film prompts. Use when a shot involves impact flashes, shockwaves, weapon trails, speed smears, magic or energy, smoke, fire, water, weather, transformation growth, destruction, debris, sparks, environmental response, emissive light, compositing integration, or when effects look cheap, detached, unreadable, overbright, or hide the action. Own the general VFX mechanism and medium-aware art direction; hand Seedance wording to seedance-vfx and physical body/weapon causality to action-choreography-reference."
---

# Cinematic VFX Director

## Core Intent

Treat VFX as **visible force, state, ownership, and consequence**, not decoration.

The effect must answer:

```text
what causes it -> where it begins -> how it travels -> what it touches ->
what changes -> how the world/light/sound respond -> how it decays or remains
```

Do not add sparks, rings, glow, particles, shake, fog, or trails merely because the shot is energetic.

## Ownership Boundary

- `$action-choreography-reference` owns body mechanics, range, contact, weapon mass, receiver response, support, recoil, braking, and recovery.
- `$cinematic-vfx-director` owns how approved force/state becomes a readable effect system.
- `$vfx-effect-construction-engine` owns lifecycle selection, causal effect construction, and precise bilingual atom retrieval after the job, primary read, medium, and intensity are approved.
- `$ai-material-realism` owns surface, optical, lighting, grounding, and render behavior.
- `$cinematic-audiovisual-language` owns shot function, axis, geography, and cut reason.
- `$cinematic-music-sound-design` owns transient, resonance, room/environment tail, silence, and mix hierarchy.
- `$seedance-vfx` compiles this design into concise Seedance-ready wording; it does not invent a second effect concept.
- For live-action ancient-fantasy/xianxia work that explicitly requires film/TV-grade quality, route the approved card through `$cinematic-fantasy-vfx-director` for premium compositing, scale, lighting, material response, and anti-cheapness review. For CG-heavy cultivation energy, formations, sword qi, talismans, elemental or spatial systems, add `$cg-xianxia-vfx-design` before construction.

Never let VFX replace missing contact, receiver acknowledgment, or environmental consequence.

## Fast Routing

Use the smallest relevant branch:

| Shot problem | Primary branch |
|---|---|
| Hit lacks weight | impact / force propagation |
| Fast motion is unreadable | motion-effect family |
| Magic feels generic | ownership / shape language / lifecycle |
| Magic, 阴阳术, or 修仙 effects feel interchangeable | supernatural system grammar / ritual logic / scale hierarchy |
| Destruction feels fake | material fracture / constraints / debris causality |
| Transformation feels like a dissolve | active frontier / growth / lock-settle |
| Effect feels pasted on | depth / occlusion / light spill / shared image pipeline |
| Full frame is noisy | hierarchy / density / decay |

Read [mechanism-atlas.md](references/mechanism-atlas.md) for branch mechanics. Read [medium-routing.md](references/medium-routing.md) whenever the medium is 2D, 2.5D/NPR, stylized CG, or mixed-media rather than neutral CG. Read [supernatural-vfx-language.md](references/supernatural-vfx-language.md) whenever the effect belongs to magic, 阴阳术, 修仙/仙侠, occult ritual, divine manifestation, summoned entities, formations, seals, or supernatural transformations.

## Workflow

### 1. Define the Effect Job

Write one sentence:

```text
The viewer must understand [force/state/threat/ownership/transition] at [beat],
without losing [contact/anatomy/geography/identity].
```

If the effect has no indispensable information job, reduce or remove it.

### 2. Lock the Primary Read

Choose one primary read per beat:

- contact and hit direction;
- speed and travel path;
- area, threat, or scale;
- transformation frontier;
- source identity or faction;
- destruction material and force route;
- transition from one state to another.

Secondary and tertiary layers may support this read but cannot compete with it.

### 3. Build the Event Envelope

For any important effect, cover only the phases that are visible and useful:

1. **Anticipation** — pressure, charge, suction, pose compression, environmental warning.
2. **Contact / release** — exact origin and directional peak.
3. **Propagation** — cone, arc, ribbon, fracture line, wavefront, wake, or volume path.
4. **Receiver response** — displacement, deformation, interruption, break, or state change.
5. **Environment response** — water, dust, cloth, debris, foliage, light, shadow, nearby objects.
6. **Dissipation / residue** — decay, cooling, settling, smoke tail, scorch, crack, drifting fragments.

Not every hit needs all six. Hero beats need a complete causal envelope; minor contacts should remain compressed.

For supernatural effects, first lock the **system grammar**: source of power, activation protocol, governing symbols/materials, spatial behavior, cost or resistance, result, and residue. A formation, talisman, spell, sword aura, dharma image, or summoned spirit must perform a specific operation rather than merely decorate the frame.

### 4. Establish Hierarchy

Use three levels:

- **Primary**: the effect shape that communicates the event.
- **Secondary**: material and environmental force evidence.
- **Tertiary**: atmosphere, fine particles, residue, or decorative accent.

Primary must remain readable in silhouette and value before color or detail is added. Tertiary detail is the first layer to remove when the frame becomes noisy.

### 5. Choose One Motion-Effect Family

Do not stack every fast-motion device. Select by medium and proof task:

- photographic shutter blur;
- animation smear or controlled geometry deformation;
- pose echo / stroboscopic multiples;
- graphic speed or focus lines;
- ribbon / weapon trail;
- physical wake: dust, water, fog, leaves, cloth;
- one-frame impact image;
- motivated foreground wipe.

Different beats may use different families, but each beat needs one dominant family. Distinguish photographic blur from a designed smear.

### 6. Route by Medium

- **Photoreal / premium CG**: physical wake, refractive compression, material debris, restrained emissive light spill, shutter-aware blur, depth-correct compositing.
- **Stylized CG / 2.5D / NPR**: designed geometry smears, pose multiples, speed lines, graphic shapes, 2D FX layered over stable 3D depth and contact.
- **Pure 2D / hand-drawn**: shape rhythm, held keys, drawing-on-twos where appropriate, line-weight change, contour break, graphic impact frames, designed directional debris.
- **Mixed media**: explicitly assign which layer is 2D, which is simulated/3D, and how occlusion, grain, color, and light unify them.

Do not translate every medium into generic glow, particles, and motion blur. See [medium-routing.md](references/medium-routing.md).

### 7. Grade Intensity

Use relative grades rather than giving every beat equal spectacle:

- **Minor**: local cloth/hair snap, small wake, brief directional line, compressed sound.
- **Medium**: readable local flash/cone/ring, receiver displacement, delayed debris, short camera impulse.
- **Hero**: selective anticipation contrast, impact image or hitstop, large environment response, strong receiver acknowledgment, clear decay.

For a 10–15 second action clip, normally allow one dominant hero beat and at most one or two secondary peaks. Preserve escalation.

### 8. Preserve Identity Under Stylized Deformation

For expressive animation, a weapon or body may bend, stretch, multiply, or smear for a very short presentation frame, but:

- the grip, handle count, cutting/striking side, anchor point, and mass direction stay legible;
- the object is correct immediately before and after the smear;
- deformation follows the actual force path;
- the smear cannot become a new weapon design or persistent morphology.

This separates **presentation deformation** from **identity deformation**.

### 9. Integrate with Camera, Light, and Sound

- Keep contact visible before using a flash, foreground wipe, or dense particles.
- Camera shake is a brief event impulse with decay, not a global camera mode.
- Emissive effects illuminate nearby surfaces according to distance, direction, color, and occlusion.
- Bright effects require controlled exposure so the source, body, and environment remain layered.
- The effect shares the scene's depth, black level, grain/noise character, atmospheric density, and motion cadence.
- Align onset, peak, and decay with sound transient, breath/effort, material resonance, and room/environment tail.

### 10. Compile the VFX Card

Before final prompt wording, reduce the design to:

```text
Function:
Medium:
Owner/source anchor:
Primary shape/read:
Path and spatial layer:
Contact/collision:
Receiver change:
Environment/light response:
Motion-effect family:
Intensity grade:
Decay/residue:
Sound sync:
```

Only decisions that change the visible result enter the final prompt. Keep research, rejected options, and diagnostic language backstage.

### 11. Construct the Effect Language

Hand the approved card to `$vfx-effect-construction-engine` when the shot needs a specific lifecycle, particle/energy/ritual grammar, or precise effect vocabulary. It may select one dominant family, one linked lifecycle, and 4–8 job-assigned atoms, but it cannot change this Skill's approved function, primary read, medium, hierarchy, or intensity grade.

For Seedance, pass the resulting construction to `$seedance-vfx` for compact model-ready wording. The chain is:

```text
cinematic-vfx-director -> vfx-effect-construction-engine -> seedance-vfx
```

## Prompt Integration

Do not add a seventh top-level block to Liu's fixed six-part prompt structure.

- Put global effect medium, color ownership, emissive behavior, material interaction, and density hierarchy inside **视觉材质总控**.
- Put camera/effect coupling and transition grammar inside **镜头语言总控**.
- Put source, path, collision, response, and decay inside the relevant **事件节拍**.
- Put onset/peak/decay synchronization inside **声音**.
- Put only positive, current-shot stability facts inside **正向稳定约束**.

## Hard Failures

Rewrite before delivery when:

- the effect has no source, path, contact, endpoint, or decay;
- particles, glow, rings, fog, trails, or shake are detached from force/state;
- the effect hides the contact point, receiver response, or action geography;
- every contact is graded as a hero hit;
- medium-specific motion language is replaced by generic motion blur;
- emissive energy does not affect nearby light, shadow, reflection, or atmosphere;
- debris appears before impact, from untouched surfaces, or with the wrong material behavior;
- destruction uses one generic fragment type for stone, metal, glass, wood, and cloth;
- a trail remains after the source stops or ignores occlusion and depth;
- stylized weapon deformation changes persistent identity;
- density never falls after the peak, leaving no readable endpoint.

## Research Basis

The mechanism library is grounded in official or primary material from Sony Pictures Imageworks, Riot Games, Disney Animation, Pixar RenderMan, SideFX Houdini, Epic Niagara, Foundry Nuke, Blender, Arc System Works, GDC animation/VFX talks, and Disney Research. See [research-sources.md](references/research-sources.md).
