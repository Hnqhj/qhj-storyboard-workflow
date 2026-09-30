---
name: visual-style-aesthetic-direction
description: "通用高级视觉风格与审美系统：覆盖摄影、电影、插画、动画、3D、平面、产品、时尚、建筑、UI 与实验媒介。触发：风格化、审美、画风、美术风格、高级感、视觉风格、风格参考、style bible、art direction，或结果廉价、卡通、通用、审美弱。 Direct universal advanced visual style and aesthetic systems for AI image/video/design prompts across photography, cinema, illustration, animation, 3D, graphic design, product, fashion, architecture, UI, and experimental media. Use when the user asks for 风格化, 审美, 画风, 美术风格, 高级感, 视觉风格, 风格参考, 审美例子, 通用审美, style bible, art direction, aesthetic direction, non-generic looks, premium stylization, or complains that a result is cheap, cartoonish, generic, aesthetically weak, inconsistent, or not高级."
---

# Visual Style Aesthetic Direction

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Core Intent

Use this skill to choose, diagnose, and lock a visual style as a coherent art-direction system across any visual medium, not a pile of style adjectives.

## Liu Style-Consistency Control Hierarchy

For a single image or a multi-image set, visual-style consistency is controlled primarily by the image-wide lighting and color system, not by repeating subjects, architecture, or decorative motifs.

Lock these variables in this order:

1. **Base tonal color / 基调色** — the dominant hue family, temperature relationship, saturation ceiling, and shadow/highlight color bias across the whole frame.
2. **Lighting ratio / 光比** — the key-to-fill relationship and the resulting distribution of bright, middle, and dark value masses.
3. **Light hardness and light shape / 光硬度与光型** — the size, directionality, edge softness, falloff, and concentration of the principal light.
4. **Motivated light-source type / 逻辑光源类型** — sun, skylight, overcast diffusion, fire, lantern, fluorescent practical, screen, emissive architecture, reflected water light, and so on.
5. **Material response / 画面元素质感** — roughness, gloss, translucency, oxidation, moisture, wear, scattering, and edge response.

The first three variables dominate the perceived family resemblance. The last two make the world physically credible inside that family. Across a batch, keep the first three tightly locked; allow content, location, camera angle, and focal objects to vary. Change the first three only when intentionally entering a new visual chapter.

Do not mistake repeated red buildings, costumes, motifs, render detail, or prompt adjectives for style consistency. If the base tonal color, lighting ratio, or light hardness drifts, the set has changed visual style even when the subject matter remains identical.

For Liu's image generation, composition, light/shadow, and atmosphere outrank comprehensive detail display. Establish the large silhouette, negative/occupied-space relationship, focal route, value masses, motivated light event, atmospheric depth, and emotional color field before surface design. Use one primary detail zone and allow secondary elements to simplify or disappear into shadow, haze, distance, broad marks, or quiet material fields. Do not turn a cinematic image into an evenly illuminated design catalog.

Treat advanced stylization as **reduction + rule + consequence**:
- reduction: fewer colors, fewer motifs, fewer effects
- rule: a stable medium, palette, line, texture, shape, lighting, and motion language
- consequence: every visual choice changes hierarchy, emotion, readability, or world logic

## Model-Executable Style Layer

### Live-Action Base, Game-Effect Boundary

For action videos, keep the base medium physically photographed and performance-led: natural human acceleration, foot support, recoil, cloth drag, rain exposure, practical light, and restrained lens behavior. If the user asks for game-like effects, scope that request to the **kill-impact layer only**. The effect may use brief graphic hit sparks, stylized bloodless energy fragments, HUD-like impact geometry, or a single-frame emphasis, but it must not control character anatomy, environment rendering, camera movement, color palette, or the whole scene. Explicitly forbid game-CG skin, rigid animation cycles, floating bodies, neon outlines, persistent UI, damage bars, collectible particles, and full-frame toon shading.

For a user-specified reference such as the Chinese film *Animal World* (2018), treat it as a scoped effects anchor: keep live-action bodies and locations dominant; borrow only high-contrast practical lighting, aggressive perspective, graphic color accents, and stylized kill-impact punctuation. Do not copy named characters, logos, or franchise assets.

Do not leave style direction as taste words. Every aesthetic label must become generation-facing controls.

Before final prompt writing, convert the chosen style into this schema:

```text
Medium domain:
Palette ownership:
Line/shape rule:
Texture owner:
Lighting behavior:
Composition hierarchy:
Motion/effect behavior if video:
Forbidden drift:
```

Translation rules:

- **高级感 / premium** = restrained palette + clear hierarchy + controlled negative space + material/light specificity.
- **电影感 / cinematic** = shot/lens/light behavior, not a magic word.
- **质感 / texture** = named surface + where it appears + roughness/gloss/wear/edge response.
- **氛围 / mood** = light direction + color temperature + haze/weather/sound/context, not just emotion.
- **风格参考 / anchor** = `anchor -> layer controlled -> visible rule -> prompt phrase -> boundary`.

Bad:

```text
高级电影感，强烈视觉风格，质感很好。
```

Good:

```text
Muted bone-white and oxidized black palette; matte ceramic skin, brushed dark steel joints, soft top-left practical light with narrow rim highlights, large empty negative space above the figure, no neon gradients, no random glossy plastic, no full-frame dirty speckles.
```

For AI-video prompts, treat the global visual master as an upstream control, not decorative copy. In the user's workflow, a strong visual master often affects the output more than detailed micro-shot wording. Put medium, aesthetic family, color ownership, material-light system, and forbidden drift before shot/action detail.

## Baseline Aesthetic Research Requirement

For substantial visual-master work, do not start from internal taste alone. If the user asks for 基础审美, 画面质感, 高级感, 小众风格, 风格母版, or complains the output looks cheap, first use `$creative-research-first` to browse current and historical references before finalizing the style.

The research must be broader than one familiar anchor:

- sample multiple lanes: cinematography/light, animation/render surface, production design, photography/editorial finish, VFX/compositing, graphic design, game/CG lookdev, fashion/product/architecture when relevant;
- compare at least 4-8 candidate references when taste is open or the current aesthetic is failing;
- reject anchors that are famous but functionally redundant, incompatible, too colorful, too chaotic, or likely to destabilize the model;
- keep the final stack small: one primary aesthetic system plus at most 1-3 scoped layer anchors.

Translate each retained reference into a control, not a citation:

```text
anchor -> layer it controls -> visible rule -> prompt phrase -> boundary
```

Example:

```text
Fortiche / Arcane -> hand-painted 3D surface hierarchy
John Wick 4 -> hard practical light pools and dark negative space
The Raid / John Wick -> readable action coverage and contact proof
Spider-Verse -> ultra-brief impact-frame graphic hold only, not full comic palette
```

When a reference is useful only for a narrow layer, explicitly say what it must not control.

For original character, costume, weapon, creature, faction, or world visuals, treat cultural/design sedimentation as part of the visual master. Browse before writing, then convert the research into visible rules: silhouette lineage, material/craft process, color ownership, motif placement, body/weapon ergonomics, scene affordance, and anti-cliché boundaries. Do not reserve this step only for the current failed image; apply it by default to all future substantial creative visual work.

This skill complements, but does not replace:
- `$creative-anchor-director` for discovering and assigning missing named references across visual, action, world, and audio lanes
- `$cinematic-audiovisual-language` for shot grammar, space, axis, and editing
- `$production-design-worldbuilding` for world rules and color ownership
- `$ai-material-realism` for physical light/material response
- `$ai-material-realism/references/rendering-vocabulary.md` for render-engine terms such as AO, PBR, anisotropic highlights, global illumination, volumetrics, normal maps, and NPR/cel shading controls
- `$jimeng-sd2-prompting` for final SD2 / Seedance packaging

## Reference Routing

Read only the reference needed for the task:

- `references/style-taxonomy.md`: use when choosing or translating an aesthetic style family.
- `references/universal-aesthetic-atlas.md`: use when the task is broad, unfamiliar, cross-medium, or needs a universal style map beyond the user's common AI-video looks.
- `references/aesthetic-quality-gates.md`: use when diagnosing whether a style feels高级, cheap, generic, overdesigned, or incoherent.
- `references/stylized-ai-video-consistency.md`: use for AI video, multi-shot prompts, style drift, graphic effects, energy/thread/ribbon elements, consistency locks, or when the same prompt looks substantially more stylized on another platform and the user wants the likely hidden style layer inferred and reproduced.
- `references/style-presentation-affordance.md`: use when a visual style must guide, but not rigidly dictate, camera language, action density, editing rhythm, transition style, PV/showcase balance, or motion grammar.
- `references/motion-trail-fx-grammar.md`: use when action speed, drag trails, smears, afterimages, speed lines, impact frames, particles, ink/brush trails, energy trails, or motion blur must fit the visual style.
- `references/aesthetic-example-library.md`: use when the user asks for examples, wants a richer style prompt, or needs high/low aesthetic comparisons.
- `references/domain-control-vocabulary.md`: use when the task needs industry-specific "control terms" beyond rendering, such as photography, cinema, print, typography, product design, architecture, fashion, UI, data visualization, food, sound, or craft terminology.
- `references/eterna-inspired-look.md`: use only when the user requests an ETERNA-like restrained cinema palette, compares prompt-level styling with a real LUT/grade, or needs an honest route from look inspiration to color-managed finishing.

## Workflow

1. Use `$creative-anchor-director` when the user knows only part of the relevant reference vocabulary. For substantial, unfamiliar, failing, or quality-critical style work, use `$creative-research-first` to research the medium, craft tradition, production process, relevant examples, and current model behavior before selecting the aesthetic system. Do this especially for 基础审美 / 画面质感 / 高级感 decisions.
2. Define the visual job:
   - What should the style make the viewer feel or understand?
   - Is the job action clarity, fashion attitude, dread, ritual, luxury, innocence, violence, memory, speed, or abstraction?
   - For video, decide the style's presentation bias before shot/action writing: what camera, editing, motion density, transition, and effect language the style naturally supports. Treat this as an affordance, not a prison. If the project needs a non-native presentation form, name the borrowed layer and keep the base style dominant. Read `references/style-presentation-affordance.md` for the bias/blend model.
   - If motion traces or effects matter, classify them before writing the prompt: photographic motion blur, animation smear, afterimage/pose echo, graphic speed/focus lines, impact frame, physical debris, energy/ink/brush trail, or foreground wipe. Read `references/motion-trail-fx-grammar.md`.
3. Choose the medium domain first:
   - photography, cinema, illustration, animation, 3D/CG, graphic design, product, fashion, architecture/interior, UI/data, craft/material culture, or experimental media.
4. Choose one primary style family:
   - Use at most one secondary influence.
   - Keep deliberate named references as compact semantic anchors. Use visible rules to clarify their role, not to replace them.
   - If using a secondary influence, state the division of labor briefly: for example, one anchor controls material/lighting while the other controls animation motion.
   - Do not stack names that all control the same layer. If several names are tempting, pick the one with the clearest job and save alternates as future routes.
5. Build the style stack:
   - base medium: 2.5D cel-real, ink wash, woodcut, risograph, editorial photo-illustration, cut-paper, collage, noir, etc.
   - color system: who owns each color, and what colors are forbidden
   - line and shape: hard edge, broken contour, thick outline, thin editorial line, calligraphic stroke, geometric block
   - texture: paper grain, ink bleed, halftone, print misregistration, brush fiber, 3D surface, matte/gloss contrast
   - lighting: flat graphic, chiaroscuro, soft editorial, rim-light silhouette, overexposed surveillance, colored practicals
   - render vocabulary: ambient occlusion, contact shadows, PBR roughness, anisotropic highlights, SSS, volumetric scattering, DOF, bloom/halation, NPR/cel shading when useful
   - domain vocabulary: choose precise terms from the relevant industry, then bind each term to a visible surface, behavior, layout, or experience
   - composition: negative space, grid, asymmetry, poster hierarchy, deep space, frame-within-frame
   - motion language for video: smear frames, held poses, match cuts, parallax layers, paper cut movement, hand-drawn jitter, slow editorial glide, pose echoes, graphic speed lines, impact frames, or layer-based photographic blur only when the style supports it
   - for stylized animation with mixed temporal behavior, assign cadence by motion class instead of globally: subject/solid painted forms may use held or stepped redrawing while snow, smoke, breath, ember glow, or other atmospheric media move more continuously. Verify shape stability and atmosphere continuity by frame stepping; keep this scoped to the chosen medium rather than applying it to live action by default.
6. Lock style continuity:
   - State which visual rules persist across shots.
   - State allowed variation: camera angle, distance, action, cloth/hair, particles.
   - State forbidden drift: new palette, new rendering style, random 3D realism, random cartoon simplification, unrelated texture.
   - When reproducing a stronger platform look, compile the inferred controls as a **toggleable stylization booster** rather than silently rewriting the base aesthetic. Preserve identity, weapon structure, action contact, geography, and the user's primary style anchor; let the booster control abstraction, line/shape, shading, palette compression, motion exaggeration, and impact-frame language only.
7. Check for cheapness:
   - If the style depends on effects instead of hierarchy, reduce effects.
   - If the style is an internally conflicting name salad, choose a primary anchor and keep only compatible secondary anchors. Do not remove a useful name merely because it is named.
   - If graphic elements lose spatial logic, define their anchor, layer, occlusion, and interaction.
   - If the user asks for thick painting, bold brushwork, graffiti energy, or smeared painterly texture, separate deliberate stroke design from dirt/noise. Use large value planes, directional strokes, broken edges, controlled splatter, clean silhouettes, and readable face/weapon areas. Avoid random full-frame speckle, muddy backgrounds, over-busy graffiti, texture crawling, or noise that hides material and shape.
   - Prefer clean-first generation over post-cleanup. Before generating, assign every texture type a visual owner: paper grain belongs to the canvas, splatter belongs to the background or effect layer, impasto belongs to skin/fabric/metal highlights, grime belongs only to intentional weathering. Forbid unowned noise, dirty haze, texture over the face, clutter behind the silhouette, and random speckles that would need secondary cleanup.
8. Package prompt language:
   - Write the visual style as a compact global visual master near the beginning of the final prompt, before detailed shots.
   - Treat it as the upstream generation domain: medium, palette, line/shape, texture, lighting, material response, rendering hierarchy, optics, and forbidden drift.
   - Let later shots vary framing, scale, movement, and local light response without redefining the aesthetic system.
   - For video, put style locks before the shot list and repeat only the fragile constraints at the end.

## Aesthetic Research Output

When the user is actively developing taste or asks to improve 审美, return a compact research-to-style bridge before the final prompt:

```text
审美判断：
- 当前廉价点 / 风险：
- 保留的方向：

参考筛选：
- [anchor] -> [controls this layer] -> [what to import] -> [what not to import]

推荐视觉母版：
[compact visual master]

负面限制补丁：
[anti-cheapness negatives]
```

Do not bury the user in a bibliography. Cite sources only when browsing materially changed the decision, and keep the usable prompt block dominant.

## Graphic Element Rule

For red lines, energy strings, ribbons, chains, brush trails, ink slashes, UI lines, and other graphic elements, always define:

- source anchor: wrist, weapon, vehicle tail, wall hook, sky tear, target point
- spatial layer: foreground, midground, behind subject, above ground, touching ground only if intended
- tension state: slack, taut, whipping, coiling, retracting, snapping
- interaction: wraps, pulls, slices, reveals, blocks, ties, drags, reflects
- visibility: whether it casts shadow, occludes objects, reflects in water, or stays flat graphic

Do not let a meaningful line become a decorative floor stripe unless that is the concept.

## Output Shape

For style selection:

```text
审美方向：
媒介域：
主风格：
辅助风格：
为什么适合：
风格规则：
禁止漂移：
可直接进提示词：
```

For diagnosis:

```text
诊断：
保留：
主要问题：
下一轮只改：
风格补丁：
负面限制补丁：
```

For final prompt blocks:

```text
Art direction / 视觉风格锁定：
...

Style consistency / 一致性锁定：
...
```

## Quality Gate

Before finalizing, check:

- At thumbnail or squint scale, do composition, light/shadow, and atmosphere already create a complete image before fine detail is visible?
- Is there one primary focal zone with controlled detail falloff, rather than equal clarity and micro-detail across the whole frame?

- If this is base aesthetic or premium-style work, did you browse and compare enough references instead of relying on memory?
- If this is an original character/weapon/costume/world, did you browse enough to give it cultural, material, craft, professional, or social depth instead of only surface beauty?
- Is the intended style captured by a strong named anchor and/or a compact coherent rule set, without the supporting description diluting the anchor?
- Does the palette have ownership and restraint?
- Does the composition have hierarchy and negative space?
- Do textures support the medium instead of becoming random dirt?
- Did the prompt prevent dirty output before generation: controlled negative space, clean subject silhouette, readable face/hands/weapon, texture ownership, no random noise/speckle/muddy haze?
- Does lighting belong to the style and world?
- For video, does the style persist across shot size and camera changes?
- If style was inferred from a cross-platform comparison, did you distinguish observable style transformations from unknowable hidden prompt/model/adapter details, and package only the reproducible controls?
- Does the global visual master appear before detailed camera/action instructions and remain more authoritative than local shot decoration?
- For video, did you treat the style's presentation form as a weighted tendency rather than a hard restriction, and did any borrowed camera/action grammar have a clear job and boundary?
- Do graphic effects have cause, anchor, layer, and consequence?
- For action traces, did you avoid generic "motion blur" and instead define the trace type, source anchor, depth layer, direction, duration, readability target, proof function, and decay?
- Does the final image still read if all decorative extras are removed?

## Dirty Output Gate

After generating or reviewing a stylized image, run a quick dirt check before deciding whether to edit.

Treat the image as dirty if any of these are visible:

- random full-frame speckles, muddy gray haze, texture crawling, or unowned noise;
- background splatter competing with the subject silhouette;
- texture pollution over face, hands, weapon, key accessories, or readable costume structure;
- dirty edges around hair, transparent fabric, limbs, props, or foreground details;
- brush strokes that do not belong to a defined layer such as paper, background ink, fabric impasto, metal highlights, weathering, or effect trail.

If the image is not dirty, do not run a cleanup pass; preserve the accepted result. If the image is dirty but the concept is good, do a single targeted cleanup/edit pass before redesigning. The cleanup prompt must preserve identity, pose, costume, composition, palette, and style while removing only unowned noise, muddy haze, clutter, and dirty edges.

Use this cleanup language:

```text
Clean the image without redesigning it. Preserve the exact character, face, pose, costume, props, composition, palette, and painterly style. Remove random speckles, muddy haze, uncontrolled splatter, dirty edges, and texture pollution over the face/hands/weapon/accessories. Keep deliberate brushwork, paper grain, controlled ink strokes, and impasto highlights. Increase clean negative space and subject-background separation. Do not over-clean into plastic or flat anime.
```

## Avoid

- Do not equate stylized with more saturation, more effects, more particles, or more brush strokes.
- Do not mix photoreal, flat cartoon, manga panel, oil painting, 3D game CG, and editorial poster without a hierarchy.
- Do not hide weak composition behind texture.
- Do not let style break audiovisual continuity.
- Preserve useful director, studio, film, photographer, artist, design-school, and genre names when the user chose them deliberately. Add medium, shape, color, light, motion, or texture controls only when they resolve ambiguity, divide responsibilities, or prevent a known failure.
- Do not mistake priority for length. The global visual master should be compact, concrete, and internally coherent, not a large pile of aesthetic adjectives that crowds out action and spatial instructions.
