# World Image Medium Profiles

Use one profile across a world board or asset family. Do not mix photographic pores, toon shadows, painterly brush textures, and glossy game-CG materials without a deliberate hybrid contract.

## Shared World Contract

All profiles keep:

- cultural causality;
- foreground/midground/background and current action;
- geometry, scale anchors, occlusion, atmospheric distance;
- distinct materials and motivated light;
- clean hierarchy and controlled detail;
- the same approved world rules across all frames.

Only the image-construction language changes.

---

## Profile P — Photographic Realism

Use when the world should look photographed with real performers, practical sets, real weather, and optical imperfections.

### Construction

- physically plausible live-action lens and exposure behavior;
- natural skin, fibers, weathering, practical light, and atmospheric scattering;
- fine grain/halation/diffusion only when the photographic stock or lens treatment calls for it;
- imperfect but coherent real-world detail.

### Optional base header

```text
A cinematic live-action photograph, large-format cinema camera, natural lens breathing and optical depth, protected highlight rolloff, readable shadow detail, practical and environmental light sources, physically plausible materials and atmosphere,
```

### Avoid

```text
Avoid: synthetic game-render surfaces, uniform digital sharpness, plastic skin, impossible reflections, shadowless lighting, overprocessed HDR, full-frame fog, decorative CGI particles.
```

This profile corresponds broadly to the original `mokeaigc-v9` photographic lane, but fixed camera brands, film stock, and skin clauses remain optional rather than universal.

---

## Profile C — High-End Cinematic CG

Use for premium CG feature-film stills, fantasy/sci-fi world development, creature environments, complex architecture, and production assets that should remain clearly authored 3D rather than imitate live-action photography.

### Medium Contract

```text
high-end cinematic CG feature-film still, large-format virtual cinematography, physically based path-traced global illumination, ACEScg-style filmic color pipeline, authored production design, clean large-scale geometry, physically distinct material classes, restrained atmospheric compositing
```

### Geometry And Scale

- clean silhouette groups and intentional negative space;
- believable architectural thickness, structural load, joint and fastener logic;
- consistent bevel scale relative to object size;
- scale anchors embedded in doors, stairs, workers, tools, vehicles, vegetation, debris, or repeated modules;
- foreground occlusion and measurable depth, not a flat concept-art backdrop.

### Lighting

- one motivated key source plus physically plausible bounce;
- path-traced-style GI or equivalent soft indirect illumination without flattening form;
- volumetric scattering limited to visible dust, smoke, mist, steam, rain, or underwater medium;
- filmic highlight rolloff, protected bright texture, readable shadow floor;
- emission affects nearby surfaces and does not create global neon bloom.

### Material Lookdev

- microfacet PBR response bound to named surfaces;
- roughness variation and distance-correct reflections;
- metal: dark body response with narrow anisotropic highlights on worked or sharpened edges;
- cloth: geometry-aware folds and weave only at visible scale;
- skin: restrained SSS and soft specular response, no pore noise unless close enough;
- wood/stone/clay: porous absorption, structural grain, chipped wear only at exposure/contact zones;
- glass/water: strict transmission, refraction, and reflection boundaries.

### Texture And Detail

- large form groups first, mid-frequency construction second, fine detail only at focal surfaces;
- production wear follows use, weather, heat, tools, hands, feet, or impact;
- hand-authored variation rather than procedural speckle everywhere;
- stable texture scale across the world board.

### Compositing

- restrained bloom/halation only at bright sources;
- clean depth separation without excessive bokeh;
- subtle atmospheric perspective and color falloff;
- no forced analog grain unless it belongs to the chosen finish.

### Prompt Base

```text
High-end cinematic CG feature-film still, large-format virtual cinematography, physically based path-traced global illumination, ACEScg-style filmic color pipeline, authored production design, clean readable silhouette groups, measurable spatial depth and scale anchors, physically distinct material classes, roughness-correct reflections, coherent contact shadows and ambient occlusion, protected highlight texture, readable shadow-side structure, restrained volumetric atmosphere, selective fine detail, clean rendering.
```

### Avoid

```text
Avoid: real-time game screenshot look, asset-store kitbash repetition, game UI, uniform plastic gloss, over-sharpened edges, noisy GI, excessive tessellation, identical bevels at every scale, random micro-scratches, global fog, global bloom, crushed blacks, clipped highlights, ghost texture, latent artifacts.
```

---

## Profile N — High-End 3D Cel-Shaded / NPR

Use for premium three-render-two worlds, stylized animation-film stills, hand-painted 3D, graphic fantasy, and world boards that need dimensional space without photoreal surface treatment.

### Medium Contract

```text
high-end 3D cel-shaded animated feature-film still, dimensional 3D staging, art-directed toon shading, hand-painted surface language, selective PBR-assisted material accents, designed shadow shapes, controlled line hierarchy, cinematic atmospheric depth
```

### Geometry And Silhouette

- clear, slightly stylized 3D forms with readable planes;
- silhouette and overlap matter more than micro-topology;
- architecture uses large shape rhythm and intentional edge hierarchy;
- scale remains proven through perspective, repeated modules, characters, stairs, doors, tools, vegetation, or vehicles;
- no miniature-diorama look unless requested.

### Value And Toon Shading

- organize each main object into 2-4 stable value bands, adjusted to the art direction rather than used mechanically;
- shadow shapes follow form and one motivated light direction;
- light terminators are clean but not arbitrary sticker shapes;
- local color remains stable between light and shadow, with deliberate cool/warm shift when appropriate;
- contact shadows and subtle AO ground feet, props, architecture, and overlapping costume layers.

### Line System

- strongest line on outer silhouettes and critical overlaps;
- medium line around joints, props, facial features, and architectural intersections;
- sparse or absent internal lines on broad lit surfaces;
- line weight thins with distance and can break on the light-facing side;
- far-background geometry may rely on value grouping instead of outlines.

### Material Separation

Do not make every surface the same flat toon plastic.

- metal: one dark body tone plus narrow designed edge/specular shapes;
- silk/satin: controlled directional highlight ribbons along folds;
- matte cloth: broad diffuse value blocks with sparse weave cues;
- stone/clay/wood: hand-painted grain, chips, and porous value variation following form;
- skin: clean facial planes, restrained warm secondary light, soft controlled highlight, no photoreal pore field;
- eyes, blades, lacquer, glass, water: selective sharper PBR-assisted highlights where the material requires them.

### Texture And Brushwork

- hand-painted texture follows geometry and material class;
- broad brush breakup in large shadow or weathered zones;
- focal surfaces may carry stronger painterly marks;
- distant areas lose line density and texture frequency;
- no random grunge, screen-wide hatch noise, or repeated decorative strokes.

### Depth And Atmosphere

- depth comes from perspective, overlap, value grouping, chroma/contrast falloff, line-density falloff, and restrained atmospheric layers;
- do not depend on shallow DOF or opaque fog;
- volumetric light is simplified into clean graphic shafts with clear source and obstruction.

### Prompt Base

```text
High-end 3D cel-shaded animated feature-film still, dimensional 3D staging with clear perspective and scale anchors, clean stylized geometry, 2-4 art-directed value bands, designed shadow shapes following a motivated key light, selective silhouette and overlap linework with distance-based line-weight falloff, hand-painted material textures following form, subtle contact shadows and ambient occlusion, selective PBR-assisted highlights on metal, eyes, lacquer, glass and water, cinematic atmospheric depth through value and chroma falloff, large readable shape groups, bold but controlled brush texture, clean rendering.
```

### Avoid

```text
Avoid: cheap mobile-game promo look, PVC figure plastic, uniform thick black outlines, flat sticker shadows, photoreal texture pasted onto toon geometry, glossy toon material everywhere, chibi simplification, oversaturated rainbow palette, line noise across distant scenery, muddy AO halos, excessive bloom, full-frame speed lines, random grunge, ghost texture, latent artifacts.
```

---

## Hybrid Rule

Use a hybrid only when the division of labor is explicit.

Examples:

```text
CG geometry and physically based environment lighting + cel-shaded characters and selective graphic impact accents.
```

```text
Cel-shaded world with PBR-assisted blades, eyes, lacquer and water only; all other surfaces remain hand-painted and toon-lit.
```

Never write only “CG + anime + realistic + painterly.” State which layer owns geometry, shading, texture, light, line, atmosphere, and effects.

## Board Consistency Gate

Across all 6/9 world frames, preserve:

- the same profile;
- the same palette ownership;
- stable material treatment;
- stable line/shadow behavior for NPR;
- stable exposure/highlight behavior for CG;
- consistent architecture, craft process, and texture scale.

Vary lens, camera height, shot size, weather moment, and action only when the frame function needs it.
