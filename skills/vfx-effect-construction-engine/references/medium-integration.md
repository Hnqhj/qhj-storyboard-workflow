# Medium and Integration Routing

## Contents

1. Medium lock
2. Camera and compositing
3. Material and light
4. Sound synchronization
5. Liu prompt placement
6. Still versus video

## 1. Medium Lock

### Premium cinematic CG / photoreal

Prefer:

- pressure wake, refraction, heat haze, volumetric scattering;
- material-specific debris and secondary motion;
- local emissive spill and controlled exposure;
- shutter-aware motion blur with readable silhouettes and contact;
- depth-correct occlusion, reflections, contact shadows, and atmosphere.

Avoid replacing physical evidence with generic neon ribbons or full-frame bloom.

### Stylized CG / 2.5D / NPR

Prefer:

- designed geometry smears and controlled weapon deformation;
- pose echoes or limited stroboscopic multiples;
- graphic speed/focus lines and shaped impact accents;
- 2D effect layers that obey 3D depth, occlusion, and contact;
- material simplification with stable value grouping and silhouettes.

### Pure 2D / hand-drawn

Prefer:

- shape rhythm, held keys, timing contrast, contour break;
- line-weight change and directional drawing density;
- bespoke smear drawings, impact frames, graphic debris;
- limited palette shifts tied to a selected peak;
- drawn camera perspective and layout consistency.

Do not ask for generic photographic motion blur when a designed smear or drawing-on-twos treatment is the intended language.

### Mixed media

Declare layer ownership:

```text
stable 3D body/environment depth + 2D drawn energy shapes + simulated debris +
shared occlusion, black level, palette, grain, and cadence
```

## 2. Camera and Compositing

- Camera reacts to a force event, not to the word “intense.”
- Keep effect onset and contact visible before a flash, wipe, or shake.
- Use a brief camera impulse with decay at selected peaks; do not make shake a permanent mode.
- Trails and particles must pass correctly in front of and behind subjects.
- Large effects need scale references: foreground occluders, distant structures, rain/fog layers, debris travel time, or shadow travel.
- Use motion blur only where exposure and velocity justify it; preserve the face, contact, weapon identity, or critical geometry.
- Match grain/noise, black level, depth of field, atmospheric density, and motion cadence to the base plate or rendered world.

## 3. Material and Light

### Emission

An emissive effect changes nearby surfaces according to:

```text
distance + direction + color + occlusion + material reflectance + exposure
```

The source may be bright without washing out the body or environment.

### Destruction

- stone: cracks, chips, heavy chunks, powder, delayed settling;
- metal: dent, bend, tear, edge sparks, hot fragments, resonant vibration;
- glass: fracture network, shards, refraction, secondary collisions;
- wood: split grain, splinters, fibers, dust;
- cloth/paper: tension, tearing direction, fibers, fluttering fragments;
- water/mud: displacement volume, spray size, ripples, droplets, settling turbulence.

### Residue

Use residue to prove the effect happened: scorch, wetness, cooled marks, cracked surfaces, displaced fog, settling particles, residual arcs, dimmed symbols, or a changed silhouette.

## 4. Sound Synchronization

Align sound to effect states:

```text
onset: seed, suction, charge, tension, ignition
path: whoosh, flow, crackle, orbital hum, turbulence
operation/contact: transient, impact, snap, cut, pressure drop
peak: selected low-frequency weight plus material-specific attack
tail: resonance, debris, droplets, cooling, fading field, room/environment return
```

Sound proves material and scale. It does not replace a missing visible contact or operation.

## 5. Liu Prompt Placement

Keep Liu's fixed prompt structure. Do not append a seventh generic effects block.

### 视觉材质总控

Place:

- medium and rendering language;
- effect carrier/material;
- palette ownership and emissive spill;
- density hierarchy;
- material interaction and residue behavior.

### 镜头语言总控

Place:

- effect reveal logic;
- camera/effect coupling;
- depth/occlusion requirements;
- selected impulse, wipe, impact image, or scale proof.

### 事件节拍

Place:

- exact source and trigger;
- formation and path;
- contact/operation and receiver response;
- peak, decay, and endpoint.

### 声音

Place onset, path, contact, peak, resonance, and tail.

### 正向稳定约束

Place only positive current-shot facts: effect owner, emitter, bounded path, contact visibility, stable weapon identity, correct depth, and readable endpoint.

## 6. Still Versus Video

### Still image

Use English by default only when the active image-generation adapter prefers English. Freeze one photographed/rendered moment:

```text
subject and scene + exact source + frozen carrier/path or contact +
world/light interaction + camera/composition + residue or stable state
```

### Video

Use the user's preferred generation language. Write visible state changes, not internal labels:

```text
source forms -> carrier advances -> operation/contact occurs ->
receiver/world changes -> selected peak -> decay and changed endpoint
```

For a continuation, inherit the previous segment's physical state and residue, but avoid pretending to reproduce an unmatched terminal frame. Use a different shot size, insert, occlusion, or sound bridge when needed.
