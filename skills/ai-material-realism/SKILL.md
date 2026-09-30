---
name: ai-material-realism
description: "把 AI 图像与视频提示词转成物理可信的材质、光照、光学、运动真实感与渲染行为。触发：独立视觉提示词、图像批评、真实感修复，或涉及皮肤、金属、布料、玻璃、湿地面、反射、阴影、PBR、模糊或合成感输出的完整档影视工作。 Transform AI image/video prompts into physically believable material, lighting, optical, motion-realism, and render behavior. Use for standalone visual prompts, image critique, realism repair, or full-depth film/AI-video work involving skin, metal, fabric, glass, wet ground, reflections, shadows, PBR, blur, or synthetic-looking output. Do not invoke separately on script-camera-group fast or standard routes; their fused planners carry the compact material baseline."
---

# AI Material Realism

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Core Intent

Use this skill as a mandatory baseline for every visual prompt. Move prompts from generic "high definition, realistic" language to physically grounded material, lighting, optical, and motion-realism instructions. Focus on how light enters, scatters, reflects, absorbs, reveals microscopic surface structure, and how motion affects different image layers.

Material realism is subordinate to Liu's global image hierarchy: composition, light/shadow, and atmosphere come first. Use material response to strengthen the focal route, depth, silhouette, and lighting event; never require every surface to be equally legible, sharp, textured, or physically demonstrated. A valid final image may let nonessential materials merge into shadow, haze, distance, broad painterly masses, or quiet low-detail regions.

When the user provides a draft prompt, rewrite it. When they provide only an image goal, build a material stack before final prompt packaging. When they ask why an output feels fake, diagnose the missing physical controls. Do not wait for the user to say "texture" or "realism"; every image/video prompt needs this layer.

This skill does not replace audiovisual grammar. For video prompts, apply material/light/optical detail to a shot whose function, spatial path, camera angle, screen direction, and continuity logic are already defined. If those basics are missing, create or request an audiovisual scaffold first, then add the material layer.

## Mandatory Baseline Pass

For every visual prompt, include a compact material-light layer that answers. For video, answer these after the shot purpose and blocking are clear:

Before expanding this layer, identify one hero material/light interaction and at most one or two supporting material separations. Keep the rest compressed. Do not use this checklist as permission to display every available material property in the same frame.

- **Hero surfaces:** what are the main visible materials? skin, hair, fabric, leather, metal, glass, ceramic, wet ground, dust, smoke, paper, plastic, foliage, etc.
- **Light behavior:** where does the key light come from, what color temperature is it, where are rim/bounce/practical lights, and how do shadows contact the ground or object?
- **Surface response:** which areas are matte, glossy, translucent, rough, worn, wet, dry, dusty, scratched, or reflective?
- **Material separation:** when important objects share one hue, how do value, color temperature, roughness, highlight width, translucency, wear, edge response, and scale keep them distinct?
- **Exposure architecture:** what highlight detail must survive, where does white roll off, how much shadow detail remains, and which accent colors must not clip or shift hue?
- **Scale of detail:** macro pores, fabric weave, panel seams, tire grooves, fingerprints, scratches, chipped edges, dust in creases, or larger clean graphic surfaces.
- **Optics/motion:** depth of field, lens diffusion, reflection, motion blur, shutter feel, foreground wipe, atmospheric particles, or controlled light trails when relevant.
- **Fake-look avoidance:** what must not happen? plastic skin, global gloss, pasted texture, flat printed fabric, milky reflections, global blur, melted silhouettes.
- **Detail cleanup:** when enhancing or redrawing an image, make detail serve silhouette, material class, face readability, and prop identity. More detail should mean clearer seams, wear, weave, scratches, roughness variation, and edge highlights; it should not mean random noise, extra ornaments, muddy texture, or unnecessary small parts.

Keep the layer proportional. A calm portrait may need two sentences; a vehicle chase may need a full material-light-motion block.

## Anti-Artifact / Controlled Detail Pass

Use this pass whenever the user says an image feels 脏、暗水印感、脏纹、噪点、低对比残纹、ghost texture、latent artifacts, or whenever a prompt is likely to overproduce high-frequency grime, repeated micro-patterns, hidden watermark-like marks, or "iterative generation bloat." This is especially important for Midjourney, IM2, character sheets, scene concept art, dense fantasy backgrounds, ink/oil-paint hybrids, and dark atmospheric images.

Core principle: do not fix dirty images by asking for "more detail." Preserve the user's subject and style, but constrain where detail is allowed. More usable detail means cleaner material separation, readable silhouettes, natural texture, controlled highlights, and fewer random residual marks.

Default cleanup add-on for image prompts:

```text
clean rendering, balanced detail, realistic detail only, natural texture only, controlled material rendering, clean gradients, soft diffused lighting, controlled highlights, subtle reflections only, matte or natural surfaces, clean blurred background, minimal repetitive patterns, no watermark, no signature, no ghost texture, no latent artifacts, no repetitive micro-pattern noise, no hidden marks, no low-contrast residual textures
```

Use the shorter add-on when prompt length is tight:

```text
clean rendering, balanced detail, realistic detail only, natural texture only, controlled highlights, clean blurred background, minimal repetitive patterns, no watermark, no ghost texture, no latent artifacts, no low-contrast residual textures
```

Replace high-risk detail words instead of stacking them:

- `ultra detailed` -> `balanced detail`
- `hyper detailed` -> `selective fine detail`
- `insanely detailed` -> `realistic detail only`
- `micro detail everywhere` -> `realistic detail only`
- `wet glossy` -> `subtle reflections`
- `glossy reflective` -> `controlled highlights`
- `highly textured rendering` -> `controlled material rendering`
- `cinematic bokeh background` -> `clean blurred background`

Avoid unless the user explicitly needs that look: `hyper-polished`, `ultra glossy`, `wet skin`, `cinematic bokeh everywhere`, `highly textured surfaces`, `micro-detail everywhere`, `insanely detailed`.

Conditional cleanup modules:

- If highlights are blown out or plastic: add `soft specular highlights, no harsh glossy reflections, matte skin, controlled shine, no highlight artifacts`.
- If dark backgrounds become muddy/noisy: add `smooth dark tones, no noisy bokeh, no background artifacts, low texture background`.
- If textures repeat or look like hidden marks: add `minimal repetitive patterns, controlled texture density, no repeated micro motifs`.

Generation hygiene: when an image is dirty because of hidden texture artifacts, prefer clean-slate regeneration with the same subject and controlled-detail prompt. Do not repeatedly reprocess the same image unless the user explicitly asks for iterative cleanup; repeated image-to-image passes often amplify latent grime.

## Workflow

1. Identify the hero material: skin, metal, fabric, wet ground, glass, organic translucent matter, etc.
2. Confirm the shot or scene has a clear function, camera relation, and spatial direction; if not, establish that audiovisual scaffold first.
3. Choose only the material controls that matter for the shot. Do not stack every control blindly.
4. When the palette is monochrome or several important objects share one color, run the same-color material-separation pass in `references/material-control-stack.md` before adding more detail or effects.
5. Specify the lighting/camera condition that makes the material visible: macro view, grazing light, backlight, rim light, hard reflection, or dry/wet contrast.
6. Define exposure behavior: protected highlight texture, smooth highlight rolloff, readable shadow floor, and controlled accent-color emission.
7. If the shot includes speed or camera movement, specify motion readability: what stays sharp, what blurs, blur direction, foreground wipe blur, background streaking, wheel/prop rotation blur, and shutter feel.
8. Rewrite the prompt with concrete physical phrases, preferably in English for image/video models.
9. Add a short negative prompt or avoidance note for the common fake look.

For detailed control vocabulary and examples:

- Read `references/material-control-stack.md` when doing any substantial prompt rewrite or diagnosis.
- Read `references/evidence-bound-material-transfer.md` when color, pattern or material must be transferred from a design reference into fixed geometry, especially with masks, region maps, white models, small details, occlusion or strict no-invention requirements.
- Read `references/rendering-vocabulary.md` when the task benefits from game/CG/render-engine terms such as AO, PBR, global illumination, ray tracing, volumetrics, anisotropic highlights, normal maps, roughness maps, contact shadows, or NPR/toon rendering.

## Five Controls

Use these as a compact decision tree:

- **AO / ambient occlusion and contact shadows**: for grounding objects, creases, seams, corners, under feet/tires, and preventing pasted-on subjects.
- **SSS / subsurface scattering**: for skin, ears, wax, jade, leaves, grapes, translucent flesh. Needs backlight or strong side/rim light.
- **Roughness and anisotropy**: for metal, blades, stone, brushed surfaces, worn tools. Define which areas are matte and which edges catch sharp highlights.
- **Imperfections**: for dirt, smudges, oxidation, fingerprints, micro-scratches, wear. Keep defects on the surface; avoid breaking the object unless requested.
- **3D topology mapping**: for knitwear, woven cloth, paper grain, bark, embossed surfaces. Require geometry-aware texture, not a flat printed pattern.
- **Specular reflection**: for puddles, wet skin, glass, polished metal, glossy paint. Preserve strict wet/dry boundaries and dark absorption areas.

## Lighting And Motion Realism

Use this section whenever the user mentions 光影, 打光, 运动模糊, 速度感, motion blur, action, vehicles, chase scenes, or camera movement.

Lighting controls:

- Define the light source direction, color temperature, and purpose: key light, rim light, bounce light, practical light, scan light, or backlight.
- Describe how light interacts with materials: ceramic bounce, metal edge highlights, glass reflection, skin subsurface scattering, wet/dry contrast, dust in volumetric light.
- Keep shadows physical: contact shadows under feet/tires, soft occlusion in seams, cast shadows matching the light direction.

Motion controls:

- Do not ask for generic "motion blur" alone. Specify layer-based blur.
- Separate photographic motion blur from stylized animation traces. Photographic blur belongs to optical/camera realism; smears, afterimages, speed lines, impact frames, and ink/energy trails belong to the visual-style layer and must be controlled by the chosen medium.
- Keep the hero subject readable: face, hands, vehicle silhouette, weapon shape, product logo, or key action point should stay clear enough.
- Blur background architecture, ground lines, particles, rain, foreground occluders, wheels, propellers, or light trails according to the motion vector.
- State blur direction: horizontal, diagonal, radial, rotational, foreground wipe, trailing light, shutter smear.
- Avoid global blur, smeared faces, melted vehicle bodies, and unreadable action.

Ground-contact and secondary-motion controls:

- Bind grounding to the actual light and substrate: contact occlusion under the loaded foot or tire, sole/tire compression where visible, and a surface response such as water displacement, dust compression, gravel shift, mud deformation, or grass bending.
- Do not use a generic black contact patch as the only proof of weight. Match cast-shadow direction, contact softness, surface roughness, and exposure to the scene.
- For garments, hair, straps, and hanging props, preserve `body impulse -> delayed drag -> collision/clearance -> overshoot -> settle`. Prevent penetration without gluing the secondary layer to the body.
- Use AO, RTAO, collision mesh, or cloth-simulation terms only when attached to a visible contact point or material behavior; never as a loose realism spell.

Useful phrasing:

```text
realistic directional motion blur: the rider and vehicle silhouette stay readable while foreground pillars streak past as wipe blur, background architecture smears along the travel direction, wheels show rotational blur, and cyan tail lights leave short controlled light trails
```

```text
warm side-back key light with cyan rim light; ceramic surfaces bounce soft gold light into shadows, black metal armor stays mostly matte while exposed edges catch sharp anisotropic highlights, contact shadows stay tight under the tires
```

## Output Shapes

For prompt rewrites, use:

```text
Material diagnosis:
- Missing controls:
- Lighting required:
- Motion/blur readability:

Rewritten prompt:
...

Negative / avoid:
...
```

For quick creative work, output only:

```text
Prompt:
...

Avoid:
...
```

## Guardrails

- Do not rely on "8K", "ultra realistic", "high resolution", or "sharp details" as a substitute for material physics.
- Do not use material physics as a substitute for audiovisual basics. A prompt can have excellent texture and still fail if the shot function, blocking, axis, and screen direction are unclear.
- Do not over-polish every surface. Perfect cleanliness often reads as synthetic.
- Do not add SSS where light cannot pass through or where the camera cannot see the effect.
- Do not make everything glossy. Real materials mix absorption, roughness, and selective highlights.
- Do not separate same-color objects by adding random colors. Separate them first through material class, value, temperature, roughness, highlight geometry, edge behavior, wear, and lighting.
- Do not use fog, bloom, particles, sharpening, or contrast as a substitute for material and depth separation.
- For video prompts, include consistency language so scratches, grime, weave, and wet boundaries persist across frames.
