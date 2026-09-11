# Rendering Vocabulary

Use this when game/CG/rendering terms can improve an AI image or video prompt. These terms are useful because they tell the model how light, shadow, surface, depth, and motion should behave. Use only the terms that are visible in the shot.

## Core Rule

Do not dump render terminology. Attach every term to a visible subject, material, or lighting condition.

Weak:

```text
PBR, AO, ray tracing, SSS, anisotropic highlights, high quality
```

Strong:

```text
PBR black brushed metal with uneven roughness; tight ambient occlusion in panel seams and under bolts; sharp anisotropic highlights along worn bevels; soft global illumination bounce from the ivory floor
```

## Shadow And Grounding

### Ambient Occlusion / AO / 环境光遮蔽

Use for:
- creases, seams, corners, under shoes, under tires, armor joints, cloth folds, object contact

Prompt:

```text
tight ambient occlusion in contact areas, under the boots, inside panel seams, and where fabric overlaps; objects feel grounded rather than pasted on
```

Avoid:

```text
overdark AO halos, dirty outlines everywhere, black smudges unrelated to contact
```

### Contact Shadows / 接触阴影

Use for:
- feet, hands touching surfaces, vehicles on ground, props on tables, layered paper, product photography

Prompt:

```text
precise contact shadows under the feet and weapon, soft occlusion where the coat overlaps the body
```

### Global Illumination / GI / 全局光照

Use for:
- realistic bounce light, indoor scenes, pale floors/walls, 3D spaces

Prompt:

```text
soft global illumination bounce from the warm ivory floor fills the shadow side without flattening the main form
```

Avoid:

```text
flat shadowless lighting, same brightness everywhere
```

### Bounce Light / 反弹光

Use for:
- colored floors, neon signs, wet streets, ceramic interiors

Prompt:

```text
subtle cyan bounce light from the wet pavement touches the underside of the black vehicle panels
```

## Surface And PBR Terms

### PBR Material Response

Use for:
- products, vehicles, armor, hard-surface props, architecture, realistic 3D scenes

Prompt:

```text
physically based material response: roughness, metallic edge highlights, contact shadows, and reflections obey the same light direction
```

Avoid:

```text
all surfaces equally glossy, plastic CG material, material changing between shots
```

### Roughness Map / 粗糙度

Use for:
- metal, leather, ceramic, stone, painted plastic, wet/dry boundaries

Prompt:

```text
uneven roughness map: matte worn flats absorb light while polished edges catch narrow highlights
```

### Metallic / Specular / 金属度与高光

Use for:
- brushed metal, chrome, blades, hardware, jewelry, machinery

Prompt:

```text
metallic surfaces remain dark and absorbing except for controlled specular highlights on bevels and contact-worn edges
```

### Fresnel Rim / 菲涅尔边缘高光

Use for:
- curved metal, glass, helmets, glossy plastic, wet skin, product edges

Prompt:

```text
subtle Fresnel edge highlight along the curved black helmet, strongest at grazing angles
```

### Anisotropic Highlights / 各向异性高光

Use for:
- brushed metal, blades, hair, satin, carbon fiber, machined surfaces

Prompt:

```text
sharp anisotropic highlights running along the brushed metal grain and sharpened blade edge
```

Avoid:

```text
uniform mirror shine, random glitter, chrome everywhere
```

### Clearcoat

Use for:
- car paint, motorcycle bodywork, lacquer, polished product shells

Prompt:

```text
black clearcoat paint with deep dark absorption and a narrow controlled highlight band, micro-scratches visible only in grazing light
```

## Texture And Geometry

### Normal Map / Bump Map

Use for:
- leather grain, fabric weave, stone pores, tire tread, bark, paper fibers

Prompt:

```text
fine normal-map-like leather grain with tiny highlights and occlusion following the folds, not a flat printed texture
```

### Displacement / 3D Topology

Use for:
- fabric, knitwear, carved stone, embossed panels, rope, paper relief

Prompt:

```text
raised weave structure with real 3D topology; individual threads cast tiny shadows in grazing light
```

### Micro-Surface Imperfections

Use for:
- realism, premium products, used tools, skin, vehicles

Prompt:

```text
micro-scratches, fingerprints, dust in seams, chipped paint only on exposed edges, intact silhouette
```

## Skin, Hair, And Organic Material

### Subsurface Scattering / SSS

Use for:
- skin, ears, fingers, wax, jade, leaves, fruit, translucent resin

Prompt:

```text
subsurface scattering through ears and fingertips under warm rim light; skin has pores and natural oil only on high points, not waxy plastic
```

### Hair Shading

Use for:
- anime-real hybrid, fashion, portraits

Prompt:

```text
hair has layered strand groups, dark mass shape, controlled rim highlights, and fine flyaway strands around the face
```

### Velvet / Satin / Fabric Anisotropy

Use for:
- fashion and costume materials

Prompt:

```text
satin fabric shows directional sheen along folds; velvet absorbs light in broad dark areas with soft grazing highlights
```

## Glass, Water, And Translucency

### Refraction

Use for:
- glass, water, lenses, transparent casing

Prompt:

```text
clear glass chamber with accurate refraction and faint edge distortion, not milky transparent plastic
```

### Caustics

Use for:
- underwater scenes, glass, pools, jewelry, wet ceramic

Prompt:

```text
subtle caustic light patterns ripple across stone and bronze, visible only where sunlight passes through water
```

### Transmission / Translucency

Use for:
- thin paper, cloth, leaves, resin, wax

Prompt:

```text
thin rice paper transmits soft backlight, revealing fibers and uneven thickness
```

## Atmosphere And Light

### Volumetric Lighting

Use for:
- smoke, dust, underwater, fog, temples, stage light, shafts of sunlight

Prompt:

```text
volumetric light shafts reveal suspended dust; air has depth but does not hide the subject silhouette
```

Avoid:

```text
generic fog covering everything, white haze flattening the scene
```

### Bloom

Use sparingly for:
- bright practical lights, neon, strong highlights

Prompt:

```text
controlled bloom only around overexposed practical lights; no global glow on all edges
```

### Halation

Use for:
- filmic bright red/orange light, analog warmth

Prompt:

```text
subtle film halation around the warm backlight, not a digital glow filter
```

### Lens Diffusion

Use for:
- beauty, dream, memory, premium soft light

Prompt:

```text
slight lens diffusion softens highlight rolloff while pores, eyes, and jewelry edges remain readable
```

## Camera And Post Terms

### Depth Of Field / DOF

Use for:
- close-ups, product, portrait, isolating details

Prompt:

```text
shallow depth of field isolates the hand and blade edge; background compresses into soft tonal shapes
```

### Motion Blur / Shutter Feel

Use for:
- action, vehicles, fast camera, cloth trails

Prompt:

```text
directional motion blur follows the movement vector; face and weapon silhouette stay readable, foreground wipes blur fastest
```

### Film Grain

Use for:
- analog cinema, print texture, reducing AI plastic smoothness

Prompt:

```text
fine film grain in midtones and shadows, not noisy compression artifacts
```

### Chromatic Aberration

Use rarely:
- lens edge realism, glitch, high-energy impacts

Prompt:

```text
very subtle chromatic aberration only at frame edges during the impact, not across the face
```

## NPR / Toon / Stylized Rendering

### Cel Shading

Use for:
- anime/三渲二/NPR characters

Prompt:

```text
cel-shaded character planes with crisp shadow boundaries, but realistic rim light and contact shadows ground the body in the 3D scene
```

### Rim Light / Edge Light

Use for:
- silhouette separation, action, character covers

Prompt:

```text
thin cyan rim light separates the black silhouette from the pale background
```

### Matcap / Clay Render Feel

Use for:
- concept sculpt, form study, minimal CG

Prompt:

```text
matte clay-render material emphasizing form and ambient occlusion, no colored texture distraction
```

### Toon Outline

Use for:
- stylized CG, game key art, readable characters

Prompt:

```text
subtle toon outline only on outer silhouette and key overlaps; no thick sticker border
```

## Game / Real-Time Rendering Terms

Use carefully because they can help but also create "game screenshot" cheapness.

Good uses:

```text
PBR materials, screen-space contact shadows, ambient occlusion in creases, volumetric fog, physically plausible reflections, Lumen-like soft global illumination, ray-traced-style mirror reflections
```

Avoid:

```text
game UI, HUD, Unreal Engine screenshot look, oversharpened asset store scene, plastic real-time render, TAA ghosting, low-poly unless intended
```

## Common Bundles

### Premium Hard-Surface Object

```text
PBR hard-surface material, uneven roughness map, tight ambient occlusion in panel seams, brushed metal anisotropic highlights, controlled clearcoat reflections, micro-scratches only on contact-worn edges
```

### 2.5D Character In 3D Scene

```text
cel-shaded character planes with stable line accents; realistic contact shadows under feet, soft global illumination bounce from the environment, rim light separating hair and shoulders, fabric folds with subtle AO
```

### Wet Night Street

```text
strict wet/dry boundaries, specular puddle reflections, dry asphalt absorbs light, tiny ripples only in water, neon bounce light on lower panels, tire grooves with mud and contact shadows
```

### Underwater Myth

```text
volumetric underwater scattering, green-blue absorption over distance, caustic light across stone and scales, silt particles in light shafts, metal oxidation and AO in engraved grooves
```

### Fashion Close-Up

```text
skin SSS under soft rim light, visible pores and peach fuzz, satin anisotropic sheen along folds, brushed silver jewelry with sharp edge highlights, shallow DOF but eyes remain crisp
```

## Render Vocabulary Negative Blocks

```text
no overdark AO halos, no global plastic gloss, no flat printed texture, no uniform mirror metal, no milky reflections, no random bloom, no full-frame fog, no global motion blur, no game-asset screenshot look
```

For stylized/NPR:

```text
no sticker outline, no chibi simplification, no live-action face drift, no plastic toon material, no 3D background ignoring character contact shadows
```
