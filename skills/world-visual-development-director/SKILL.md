---
name: world-visual-development-director
description: "世界优先的图像开发总控：IM2 与 GPT Image 2、Midjourney、概念图、电影级世界板、大环境、反复出现的地点、怪物栖息地、文化丰富场景设计。触发：世界观图、世界板、场景图、大场景、环境设定、怪物生态、文化沉淀、空间透视、可信空间、诗性巨构。 Fused world-first image-development director for IM2/GPT Image 2, Midjourney, concept art, cinematic world boards, large environments, recurring locations, creature habitats, and culture-rich scene design. Use when Liu asks to build or visualize a world, 世界观图/世界板/场景图/大场景/环境设定/怪物生态/文化沉淀/空间透视/可信空间/氛围感/高审美/诗性巨构, wants a reference image expanded into a coherent world, or needs atmosphere-first composition, research, MOKE-style multi-still exploration, production design, geometry/optics/material-science spatial evidence, clean rendering, and downstream asset/video handoff to work as one system rather than pasted skill blocks."
---

# World Visual Development Director

Treat `sophia-mode` and `concise-user-facing-output` as already on. This skill owns the final static world-visual-development result. Its ingredients advise; they do not each emit competing blocks.

## Purpose

Turn a concept, culture, location, creature, mood, name, or reference image into a world that looks lived in, spatially measurable, materially differentiated, culturally caused, and clean enough to become stable image/video assets.

The key synthesis is:

```text
cultural mechanism
-> lived-world visual exploration
-> production-design rules
-> geometry + optics + material-science evidence
-> clean image packaging
-> asset/video handoff
```

Do not solve this with decorative lore, copied cultural symbols, fake scientific language, generic cinematic adjectives, or random micro-detail.

## Liu Default: Composition, Light, Atmosphere Before Information

For Liu's world images, treat composition, light/shadow, and atmosphere as the upstream image system, not finishing effects. Unless the current request explicitly prioritizes design explanation, technical display, or asset clarity, use this priority ladder:

For world-series continuity, first lock the visual family through **base tonal color, lighting ratio, and light hardness/light shape**. These three are the dominant style invariants. Then lock the motivated light-source family and material-response rules. Architecture, locations, weather, camera position, and focal mechanisms may vary, but they must remain inside this shared color-and-light envelope unless a deliberate chapter break is requested.

```text
composition, framing, and dominant silhouette
-> light/shadow and broad value masses
-> emotional atmosphere and color field
-> depth and environmental motion
-> world mechanism
-> localized design detail
```

Build the image so it reads first as a composed light-and-atmosphere event, then as a world. A frame that explains the technology clearly but lacks a strong composition, motivated light, mystery, silence, tension, scale, or visual poetry has failed.

Apply these defaults:

- Let sky, darkness, mist, water, dust, snow, cloud, rain, smoke, or empty terrain occupy meaningful negative space; do not fill the frame merely to prove production value.
- Use one dominant silhouette, one principal spatial event, and one motivated light event. Keep secondary forms subordinate.
- Organize the frame into a few broad value masses before adding architecture or machinery. Prefer a restrained palette with one controlled accent or temperature conflict.
- Let atmosphere produce depth through density, occlusion, contrast falloff, edge loss, reflection, and slow environmental movement; fog alone is not depth.
- Integrate technology into scale, silhouette, infrastructure, energy flow, ritual, weather control, or material behavior. Avoid decorative circuitry and exposed machinery that turns the world into a design showroom.
- Concentrate fine detail only where it clarifies the focal mechanism. Preserve calm areas and visual breathing room.
- Do not make every building, bridge, costume, mechanism, material, or background layer equally clear. Lock one focal detail zone, allow at most one or two subordinate zones, and let the rest simplify through shadow, haze, distance, broad masses, occlusion, or painterly edge loss.
- For myth-and-technology worlds, preserve the mythic reading at first glance; reveal the technological explanation on second reading.
- When people are not requested, prove scale through terrain, water, cloud layers, architecture, birds, lights, or infrastructure rather than inserting a token figure.

Read [atmosphere-first-world-images.md](references/atmosphere-first-world-images.md) when the user asks for 氛围感、审美更高、诗性、巨构、神话科技、无人物环境，or when a technically coherent result still feels generic or overdesigned.

## Medium Profile Selection

Before choosing the board or single-image mode, lock one primary image medium:

- **Photographic realism** — observed live-action world, lens/film behavior, natural imperfection.
- **Cinematic CG** — high-end authored 3D world with physically based light/materials, filmic exposure, clean large-scale geometry, and no game-screenshot drift.
- **3D cel-shaded / NPR** — dimensional 3D staging with designed value bands, selective line hierarchy, hand-painted surface language, controlled material accents, and no cheap plastic-toon drift.

The world logic stays constant; only the rendering and image-construction profile changes. A medium profile owns camera preset language, shading, texture density, skin treatment, linework, reflections, atmosphere, and its avoid block.

Read [medium-profiles.md](references/medium-profiles.md) whenever the user asks for CG、三渲二、NPR、真实摄影风格切换，or when `mokeaigc-v9` photographic defaults conflict with the approved medium.

## Ownership And Routing

Use the smallest active stack that changes a real decision:

- `creative-research-first`: culture, craft, profession, ecology, architecture, ritual, material process.
- `mokeaigc-v9`: multi-still discovery of a world that appears observed rather than displayed.
- `production-design-worldbuilding`: world laws, color ownership, shape language, social use, location pressure, prop logic.
- this skill: synthesis, mode selection, spatial-evidence contract, final still-image system, handoff.
- `ai-material-realism`: physically plausible light and surface response.
- `im2-clean-image`: controlled detail, anti-artifact hygiene, IM2 prompt order.
- `visual-style-aesthetic-direction`: only when the medium or aesthetic family is not already locked.
- `blue-gold-mineral-fantasy-style`: use as the approved visual preset when Liu asks for 蓝金岩彩幻想风、蓝色岩彩、上面那张蓝色画风，or continues the approved indigo folded-page world.
- `character-continuity-bible`: only after a recurring character, creature, weapon, or location asset is approved.

Do not activate the full world workflow for a simple isolated portrait, minor edit, or already locked asset unless the user asks for cultural/world expansion.

## Mode Selection

Choose one primary mode before writing.

### A. World Discovery Board

Use for “展开这个世界”, a reference image with an implied world, or a concept that lacks cultural and environmental depth.

- Default: 6 high-value cinematic stills.
- Use 9 only when the user asks for a complete world board or the concept genuinely needs the full `mokeaigc-v9` spread.
- Each still must reveal a different world function, not repeat the same hero composition.
- When direction is not yet approved, request `mokeaigc-v9` Planning-only output first: world concept, continuity bible, aspect matrix and open decisions, without final platform prompts.
- If the user wants the same locked scene repeated through different camera positions, route to `cinematic-ai-image-prompt-library` instead of treating camera variations as world functions.

### B. Hero Environment

Use for one large scene, environment keyframe, establishing image, or main battle arena.

- Build the hidden world bible first.
- Deliver one decisive image prompt with scale proof, depth planes, material separation, current action, and environmental story evidence.
- Do not force a 6/9-image board when the user needs one image.

### C. Asset Emergence

Use when a monster, vehicle, weapon, building, costume, or prop should grow out of the world rather than look pasted into it.

- Derive silhouette, materials, fasteners, repairs, ergonomics, motifs, and wear from the approved world rules.
- Then hand the recurring asset to `character-continuity-bible` or the relevant design skill.
- Read [world-to-asset-handoff.md](references/world-to-asset-handoff.md) when deriving a recurring asset or handing approved world laws to image/video production.

### D. Video Handoff

Use when the world board already exists and the user is moving into SD2/Seedance/storyboard work.

- Distill the world into 3-6 stable laws: geography, climate, material family, color ownership, architecture/prop logic, atmosphere/light behavior.
- Do not paste world-board prose or all still prompts into a video prompt.

## Core Workflow

### 1. Lock The World Promise

Write one sentence answering:

```text
What should the viewer understand about this world from one frame?
```

Then define three visible rules:

- survival/social rule;
- craft/technology/ritual rule;
- visual/material rule.

Also lock one **atmosphere sentence**: what should the viewer feel before they understand what they are seeing? This sentence controls negative space, value grouping, weather medium, palette, edge behavior, and the light event. Do not answer it with style labels alone.

### 2. Research Mechanisms, Not Stickers

For every major culture, craft, profession, creature ecology, architecture, weapon, ritual, or material, capture:

```text
who made or uses it
why it exists
how it is produced or maintained
how bodies interact with it
what wear/residue proves repeated use
what status, taboo, memory, or danger it carries
what visible scene evidence can show this without exposition
```

Keep research short and source-backed. Translate it into structure, behavior, residue, material, and spatial use; do not paste explanatory history into prompts.

### 3. Explore The World As Lived Space

When using `mokeaigc-v9`, choose only the aspects that expose the current project's missing information. Candidate functions:

- inhabitants or labor;
- architecture in use;
- geography as a force;
- daily maintenance;
- travel or material transport;
- sound/culture made visible;
- power/tension;
- intimate portrait;
- creature ecology;
- before/after evidence.

Every frame requires foreground, midground, background, a current action, and evidence of what happened before or will happen after. It must read as a discovered film still, not a concept-art catalog plate.

### 4. Build The Production-Design Bible

For each major element, define:

```text
maker/user
purpose
material/process
visible wear/adaptation
color/motif owner
behavior/ergonomics
scene proof
generic drift to prevent
```

Also lock:

- shape language;
- material family;
- repair/fastener logic;
- color ownership;
- location pressure;
- allowed variation;
- forbidden drift.

### 5. Apply The Three-Layer Spatial Evidence Stack

Use “数学/物理/化学” as a useful mnemonic, but express it more accurately as:

1. **Geometry and projection** — coordinate relationships, ground plane, eye height, horizon, vanishing points, scale anchors, overlap, occlusion, depth planes, proportion, parallax evidence.
2. **Optics and light transport** — motivated light source, cast-shadow agreement, atmospheric scattering, contrast/color falloff, reflection/refraction boundaries, volumetric visibility only where the source and medium justify it.
3. **Materials science and surface response** — material class, roughness, absorption, translucency, anisotropy, moisture, oxidation, wear, micro-topology, contact/ambient occlusion.

Read [spatial-evidence-stack.md](references/spatial-evidence-stack.md) for prompt-ready patterns and failure corrections.

Do not dump textbook explanations into the final prompt. Convert each layer into visible evidence relevant to the current frame.

### 6. Finish For IM2 Or The Target Image Model

For IM2/GPT Image 2, order the prompt:

1. subject, action, setting, composition;
2. style/medium;
3. world evidence and spatial proof;
4. material-light response;
5. controlled-detail clean layer;
6. compact current-risk avoid block.

Keep `clean rendering`, `balanced detail`, `selective fine detail`, `natural texture`, `controlled highlights`, coherent contact shadows, and sparse purposeful patterning, but bind them to actual surfaces.

Do not blindly inherit `mokeaigc-v9` defaults such as `no CGI look`, analog-film language, a fixed camera body, or a fixed lens family when they conflict with the approved medium. Preserve its lived-world mechanism, not every preset phrase.

### 7. Distill And Handoff

After image exploration, produce a concise reusable handoff:

```text
world promise
3-6 visual laws
location scale map
material/color ownership
approved recurring assets
location pressure/action affordances
continuity risks
```

Store project-specific details in the project bible, not in this global skill.

## Model-Executable Quality Gates

Before delivery, verify:

1. **Cultural causality:** at least three visible elements share a real process, use, ritual, economy, ecology, or repair logic.
2. **Spatial proof:** the frame contains scale anchors, coherent ground/eye-height geometry, overlap, and distance falloff.
3. **Optical consistency:** light, shadow, reflection, atmosphere, and exposure agree.
4. **Material separation:** important same-color surfaces remain distinct by roughness, value, highlight width, edge behavior, translucency, or wear.
5. **Lived evidence:** someone or something is using, repairing, carrying, avoiding, hearing, maintaining, or surviving the world.
6. **Narrative pressure:** the location changes behavior instead of serving as wallpaper.
7. **Clean hierarchy:** large shape groups read first; detail is concentrated at focal architecture, hero props, faces, or action interfaces.
8. **Mode honesty:** a single-image request does not receive an unwanted nine-board; a video request receives distilled laws rather than static-board prose.
9. **Atmosphere-first read:** squinting or thumbnail view still produces a distinct emotion, dominant silhouette, negative-space pattern, and light event before small design information is visible.
10. **Second-read technology:** in mythic or poetic worlds, engineering logic rewards inspection without replacing the first-glance mythic image.

If any gate fails, revise the world mechanism or composition before adding more adjectives or detail.

## Output Contracts

### World Discovery Board

```text
world name and promise
three world laws
selected 6/9 frame functions
one prompt per frame
world bible handoff
```

### Hero Environment

```text
short design judgment
one complete copyable image prompt
compact avoid block when needed
```

### Asset Emergence

```text
world-derived design logic
one complete asset prompt or direct image generation
continuity locks
```

### Video Handoff

```text
3-6 stable world laws
location pressure and action affordances
asset/reference role mapping
```

## Guardrails

- Do not use “mathematics, physics, chemistry” as empty prestige words.
- Do not claim exact equations, refractive indices, focal lengths, or physical values unless they materially control the image and are known.
- Do not make culture equal costume motifs, kanji, talismans, ornaments, or architecture labels.
- Do not make every frame a clean empty establishing shot; a credible world is being used.
- Do not increase depth using fog alone. Geometry, overlap, scale, contrast falloff, and material response must also work.
- Do not turn material realism into uniform gloss or micro-detail everywhere.
- Do not repeatedly clean an already dirty generation; prefer a clean-slate regeneration with controlled density.
- Do not let underlying skills output separate competing sections. Fuse them into one image/world system.
