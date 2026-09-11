# Material Control Stack

Use this reference when rewriting or diagnosing prompts for material realism. Prefer concise physical phrasing over broad aesthetic adjectives.

## Prompt Recipe

Build prompts in this order:

1. Subject and hero material
2. Material hierarchy and same-color separation
3. Micro-surface behavior
4. Lighting angle that reveals the behavior
5. Exposure and local contrast: matte vs glossy, wet vs dry, clean vs dirty
6. Camera scale and motion readability
7. Restrained post/finishing
8. Negative prompt for the fake failure mode

Useful sentence skeleton:

```text
The [material] shows [physical behavior] under [lighting condition], with [local imperfections/topology] visible at [camera scale]; [specific areas] remain [matte/dry/absorbing] while [specific edges/surfaces] catch [sharp/soft/specular/anisotropic] highlights.
```

## Same-Color Material Separation

Use this whenever important subjects share one hue: white-on-white products, snow and clothing, black vehicles at night, gray architecture and armor, monochrome fashion, sterile interiors, ceramic characters, or any intentionally restrained palette.

Do not solve same-color readability by adding unrelated accent colors. Assign every major surface a distinct physical identity across at least four of these controls:

```text
role/age:
base value:
color temperature:
material class:
roughness:
highlight width and intensity:
translucency or absorption:
edge response:
wear/contact zones:
micro-detail scale:
```

Example separation logic:

```text
environment = broad, slightly warm, diffuse, large-scale texture
hero object = neutral, denser, cleaner, controlled medium-width highlights
damaged/aged object = warmer or dirtier undertone, broken roughness, localized wear
authority/threat object = slightly colder, harder edge response, sparse severe highlights
```

The color differences may be subtle. The primary separation should come from light behavior:

- matte surfaces use broad low-intensity highlights and absorb reflections;
- satin surfaces use soft controlled highlight bands;
- polished edges use narrow high-intensity highlights;
- translucent layers show internal scattering only where light can pass through;
- porous, worn, or oxidized areas break up the highlight instead of becoming uniformly darker;
- foreground, midground, and background lose contrast and detail at different rates.

Prompt pattern:

```text
Although the palette is nearly monochrome, every major surface remains distinct through physical response: [surface A] is [value/temperature/material/roughness], [surface B] is [different response], and [surface C] is [different response]. Separate them with grazing light, controlled highlight width, contact shadows, and depth-dependent contrast rather than new colors or heavy outlines.
```

Avoid:

```text
all same-color objects merging into one plastic mass, random color accents added for separation, black outlines around every object, identical roughness, identical highlight width, identical exposure across foreground and background
```

## Exposure And Highlight Architecture

Define exposure as part of material design, especially for white, reflective, emissive, snowy, metallic, glass, or high-key scenes.

- Preserve texture in the brightest hero surfaces; pure clipping is reserved for tiny motivated light sources.
- Use smooth highlight rolloff instead of hard white patches.
- Keep multiple value families inside a nominally white or black palette.
- Preserve a readable shadow floor in joints, folds, hair masses, machinery, and architecture.
- Keep emissive accent colors saturated at the core without shifting to pastel white, orange, or pink.
- Let reflections lose contrast according to surface roughness and distance; do not make every floor a perfect mirror.

Prompt pattern:

```text
Protect highlight texture and use smooth cinematic highlight rolloff; the brightest material remains readable, shadow-side structure retains low-contrast detail, and emissive accents keep their intended hue without clipping. Reflections obey distance and roughness rather than becoming milky or globally mirror-like.
```

## Lighting Stack For Material Readability

Use a small motivated lighting system:

1. a broad key establishes form and overall exposure;
2. a grazing side/back light reveals roughness, edges, cracks, weave, or machining;
3. bounce or fill preserves shadow-side information without flattening form;
4. practical/accent light affects only nearby surfaces with distance falloff.

Do not use rim light on every edge. Assign each light a visible job and preserve one dominant direction.

For high-key or low-key monochrome scenes, create depth through:

- value grouping;
- material response;
- scale;
- overlap and occlusion;
- depth-dependent contrast;
- reflection falloff;
- selective atmosphere.

Use atmosphere sparingly. Clean air, slight aerial perspective, or a few particles in motivated light often reads as more premium than full-frame fog.

## Grounding, Optics, Motion, And Finish

Grounding:

- Place AO only in true creases, seams, overlaps, joints, and contact zones.
- Use precise contact shadows under feet, tires, hands, props, and compressed surfaces.
- Avoid global black outlines or dirty AO halos.

Optics and motion:

- Keep faces, hands, product silhouette, weapon line, cable anchor, or other story-critical contact points readable.
- Apply directional blur by depth layer: foreground wipes fastest, background trails along the motion vector, hero contours retain enough definition.
- Let impact or revelation briefly sharpen only when the rhythm calls for it; do not globally sharpen the whole clip.
- Use restrained depth of field. Do not hide weak geometry or action behind extreme blur.

Finishing:

- Use neutral or intentionally motivated white balance.
- Apply bloom or halation only around genuinely bright sources or emissive accents.
- Add fine grain primarily to midtones and shadows, not as noisy texture across clean highlights.
- Keep chromatic aberration subtle and limited to lens edges or one designed impact.
- Preserve the same material, scratch, roughness, reflection, and exposure logic across video frames.

Universal quality block:

```text
Use physically distinct material classes even inside a restrained or monochrome palette. Preserve highlight texture with smooth rolloff, readable shadow-side structure, localized AO/contact shadows, distance- and roughness-correct reflections, motivated grazing light, restrained atmosphere, layer-based directional motion blur, and subtle finishing. No uniform plastic gloss, no identical roughness across objects, no clipped white masses, no crushed black masses, no milky reflections, no dirty AO outlines, no full-frame fog, no global bloom, no global sharpening, and no game-engine screenshot look.
```

## 1. Subsurface Scattering / SSS

Use for skin, ears, fingers, wax, grapes, jade, leaves, petals, translucent resin, thin organic material.

Write:

```text
extreme subsurface scattering, warm translucent red glow through the ear cartilage, blood-tinted light diffusing under the skin, rim light passing through thin tissue, soft internal scattering rather than plastic surface shine
```

Avoid:

```text
plastic smooth skin, waxy mannequin surface, flat beige skin, over-smoothed pores, white blown-out highlights
```

Lighting requirement:
SSS needs backlight, rim light, strong side light, or macro close-up. In flat front light it may not be visible.

## 2. Roughness and Anisotropic Highlights

Use for rusted blades, brushed steel, cookware, tools, stone, leather, matte ceramics, worn machinery.

Write:

```text
extreme physical surface roughness, sharp anisotropic highlight along the sharpened edge, oxidized rust absorbing light, uneven roughness map, matte corroded areas contrasted with cold razor-thin edge reflections
```

Avoid:

```text
uniform glossy metal, glass-like reflection across the rust, decorative flat rust pattern, clean CG sword, global shiny surface
```

Key distinction:
Rough material is not simply "low quality". Define where reflection dies and where it becomes sharp.

## 3. Imperfections / Wear

Use for vehicles, helmets, old books, glass lenses, industrial objects, cyberpunk props, used tools, human-handled surfaces.

Write:

```text
wipe smudges, micro-scratches, fingerprints, dust trapped in seams, blue-purple high-temperature oxidation, chipped paint only on exposed edges, grime gathered around bolts and tire treads, uneven rain dirt on lower panels
```

Avoid:

```text
perfect showroom clean object, random damage, broken body shape, chaotic dirt everywhere, sterile 3D model export
```

Rule:
Imperfection should sit on micro-surfaces and contact zones. Keep the silhouette intact unless damage is the subject.

## 4. 3D High-Frequency Topology Mapping

Use for knitwear, woven cloth, rope, bark, handmade paper, leather grain, embossed material, concrete pores, sand, hair-like fibers.

Write:

```text
high-frequency knitted grid mapped to 3D topology, every yarn strand casts tiny contact shadows, fibers wrap naturally over folds, raised weave structure visible in grazing light, deep occlusion between threads, geometry-aware fabric texture
```

Avoid:

```text
flat printed fabric texture, stretched pattern over folds, blurry cloth, smooth sweater surface, texture sliding across the shape
```

Lighting requirement:
Use grazing light or side light to reveal relief. A front-lit fabric may look flat even with a good texture phrase.

## 5. Specular Reflection and Wet/Dry Boundaries

Use for puddles, wet asphalt, rain streets, glossy paint, glass, wet skin, polished stone, product surfaces.

Write:

```text
perfect specular mirror reflections in shallow puddles, strict dry/wet boundary, black asphalt absorbs light outside the water, neon signs reflected with crisp inverted geometry, tiny ripples only inside the wet area, transparent water surface over dark ground
```

Avoid:

```text
global wetness, glowing white reflective floor, milky puddles, reflection pasted onto dry areas, blurry generic rain street
```

Rule:
Wet reflection works because dry areas remain dark and absorbing. Preserve the contrast.

## Compact Rewrite Patterns

Skin close-up:

```text
macro close-up portrait, realistic skin with visible pores and fine peach fuzz, warm subsurface scattering through the ear and fingertips under strong rim light, soft blood-tinted translucency under the skin, natural oil only on high points, not plastic, not waxy
```

Rusted blade:

```text
ancient rusted blade on black stone, extreme physical surface roughness and oxidized pitting, rusted flats absorb light, sharpened bevel catches a cold sharp anisotropic highlight, micro-scratches along the edge, no uniform glossy reflection
```

Used cyberpunk vehicle:

```text
used cyberpunk motorcycle in rainy alley, wipe smudges, micro-scratches, dust in panel seams, blue-purple heat oxidation on exhaust pipes, mud trapped in tire grooves, worn edges only where hands and boots touch, intact silhouette, not showroom clean
```

Knitted fabric:

```text
close-up wool sweater folds, high-frequency knitted grid mapped to real 3D topology, individual yarn strands bend around folds, grazing side light reveals raised fibers and deep thread occlusion, tiny lint and stray hairs, no flat printed texture
```

Rainy street:

```text
night street after rain, shallow puddles with perfect specular mirror reflections of neon signs, strict dry/wet boundaries, dry asphalt stays black and light-absorbing, tiny ripples only in water, crisp inverted signage, no milky glowing floor
```
