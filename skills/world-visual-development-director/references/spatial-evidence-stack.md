# Spatial Evidence Stack

Use this reference when a world image, large environment, interior, architecture, creature habitat, or establishing shot feels flat, toy-like, scale-less, materially uniform, or atmospherically vague.

## 1. Geometry And Projection

### Required questions

- Where is the ground plane?
- What is the observer height?
- Where is the horizon?
- Which parallel edges converge, and toward which vanishing direction?
- What known-size anchor proves scale?
- What overlaps what?
- Which foreground object creates parallax or occlusion?
- How many distinct depth planes are readable?

### Prompt-ready language

```text
The space is organized around a readable ground plane and a low observer height; long structural edges converge toward one distant vanishing zone, repeated columns diminish by distance, and a human-sized doorway plus workers provide scale proof. A dark foreground beam partially occludes the midground furnace, while the far wall loses contrast and chroma through distance.
```

```text
Extreme wide elevated view with a visible horizon and three depth bands: oversized foreground roof structure, the active settlement in the valley midground, and compressed mountain ridges in the distance; roads, carts, smoke plumes, and figure size make the geography measurable.
```

### Failure correction

- Flat image -> add ground plane, overlap, scale anchor, converging structure, depth bands.
- Miniature/toy look -> lower or raise observer height intentionally, reduce excessive shallow DOF, add full-size human/door/vehicle reference.
- False giant scale -> show repeated known-size elements and environmental consequence, not only a low angle.
- “High aerial view” ignored -> state observer altitude, visible terrain map, tiny scale anchors, horizon placement, and broad ground coverage.

## 2. Optics And Light Transport

### Required questions

- What is the motivated key source?
- Which surfaces face it?
- Where do cast shadows fall?
- What blocks the light?
- What medium fills the air: clear air, mist, smoke, rain, dust, steam?
- How do distance, scattering, and exposure change contrast and color?
- Which surfaces reflect, refract, transmit, or absorb?

### Prompt-ready language

```text
Cold daylight enters through the roof breach from camera-left, producing matching cast shadows across the floor and narrow edge light on raised metal; the furnace contributes a weak low warm bounce only near its mouth. Suspended charcoal dust catches the shaft locally, while distant structures lose contrast without turning into opaque fog.
```

```text
Wet stone reflects only at shallow angles and inside thin puddles; dry porous areas remain dark and absorbing. Glass and polished metal carry bounded highlights, while rough clay and soot-black timber break the reflection into soft uneven patches.
```

### Failure correction

- Flat lighting -> assign one motivated source, cast-shadow direction, local bounce, and occlusion.
- Foggy depth with no structure -> reduce fog; restore geometry and use mild distance contrast/chroma falloff.
- Global glow -> restrict emission to named sources and nearby surfaces.
- Mirror-floor contamination -> specify strict wet/dry boundaries and angle-dependent reflections.

## 3. Materials Science And Surface Response

### Required questions

- What material class is each hero surface?
- What is its roughness and reflectance behavior?
- Is it porous, metallic, translucent, fibrous, layered, oxidized, wet, dry, or heat-affected?
- What process formed it?
- Where would use, weather, heat, hands, feet, tools, salt, moisture, or impact alter it?
- Which details are geometric and which are surface-only?

### Prompt-ready language

```text
Forged steel stays dark and mostly matte, with narrow anisotropic highlights only along hammered edges; oxidized flats absorb light and carry sparse reddish corrosion in joints. Rammed-earth furnace walls are porous and chalky, with heat-darkened gradients near vents and chipped edges only at repeated tool-contact zones.
```

```text
Silk, lacquered wood, paper, iron, wet stone, and skin remain visibly separate despite a restrained palette: silk shows soft directional sheen along folds, lacquer holds bounded reflections, paper scatters light diffusely, iron catches narrow hard highlights, and wet stone reflects only in shallow depressions.
```

### Failure correction

- Everything plastic -> diversify roughness, absorption, highlight width, and edge response.
- Dirty fantasy concept art -> reserve wear for contact/weather zones; remove random speckle and micro-pattern repetition.
- Pasted texture -> make weave, grain, cracks, and hammer marks follow geometry and deformation.
- Same-color merging -> separate by value, temperature, roughness, translucency, contact shadows, and depth instead of adding random colors.

## 4. Combined Scene Formula

Use only the clauses relevant to the frame:

```text
[current action and spatial function]. The scene has a measurable ground plane, observer height, vanishing structure, known-size anchors, foreground occlusion, and three readable depth bands. [motivated light source] creates coherent cast shadows and local bounce; atmospheric scattering reduces distant contrast and chroma without hiding geometry. Each hero material has a distinct roughness, absorption, reflection, translucency, wear, and edge response derived from how it was made and used. Large shape groups remain clean; fine detail appears only on focal surfaces and action interfaces.
```

## 5. Compression Rule

Do not paste all three layers at full length into every prompt.

- Large exterior: emphasize geometry + atmospheric depth + scale anchors.
- Interior: emphasize vanishing structure + occlusion + motivated practical light.
- Material close-up: emphasize formation process + roughness/topology + grazing light.
- Creature habitat: emphasize scale proof + environmental adaptation + residue.
- Stylized/painted medium: preserve the chosen medium, but keep spatial and material causality visible through value groups, edge hierarchy, pigment behavior, and controlled texture.
