# Domain Control Vocabulary

Use this when a prompt needs industry-specific control terms. These terms work like AO/PBR in rendering: they are not decorative; they encode how a thing is made, lit, structured, touched, worn, organized, edited, or experienced.

## Core Rule

Use a control term only when it is tied to a visible or audible result.

Weak:

```text
premium, cinematic, editorial, professional, detailed
```

Strong:

```text
editorial fashion lighting with soft key light, clean garment drape, visible topstitching at seams, controlled accessory density, and negative space around the silhouette
```

Prompt formula:

```text
[domain term] appears in/on [specific object or layer], causing [visible behavior], while [failure mode] is avoided.
```

## 1. Photography Control Terms

Use for portraits, product shots, fashion, documentary, realism.

Useful terms:
- dynamic range / highlight rolloff
- color temperature
- key light, fill light, rim light, practical light
- lens compression, focal length, shallow depth of field
- bokeh shape, focus falloff
- film grain, halation, gate weave
- exposure latitude, black point, shadow detail

Prompt examples:

```text
soft highlight rolloff on skin, no blown-out forehead; shallow depth of field isolates the eyes while jewelry edges remain crisp
```

```text
long-lens compression makes the background city feel close behind the subject, but the face remains undistorted
```

Avoid:
- "cinematic lens" without shot distance or focus target
- blur that destroys identity
- beauty light that erases texture

## 2. Cinematography And Color Grading

Use for moving images, film stills, trailers, narrative scenes.

Useful terms:
- motivated lighting
- practical light source
- three-point lighting
- chiaroscuro
- high-key / low-key lighting
- contrast curve
- color separation
- teal-orange only when motivated
- bleach bypass, film emulation, print stock look
- shutter angle, motion cadence
- rack focus

Prompt examples:

```text
motivated warm practical light from the table lamp shapes the face; cool moonlight rim separates the shoulders from the dark room
```

```text
low-key chiaroscuro with deep black fields and controlled eye highlights; shadow detail remains readable near the hands
```

Avoid:
- generic teal-orange grading everywhere
- "film look" without grain, contrast, halation, or highlight rolloff rules

## 3. Graphic Design And Typography

Use for posters, covers, dashboards, branding, editorial layout.

Useful terms:
- hierarchy
- baseline grid
- modular grid
- typographic scale
- kerning, tracking, leading
- optical alignment
- rag, measure, column width
- negative space
- figure-ground relationship
- visual weight

Prompt examples:

```text
strict modular grid, large primary title, one secondary information block, generous negative space, optical alignment between image edge and typography
```

```text
typographic hierarchy uses three levels only: masthead, short deck, micro caption; no random decorative text
```

Avoid:
- fake text clutter
- "magazine layout" without grid and hierarchy
- too many font styles

## 4. Print And Publishing

Use for posters, book covers, zines, packaging, tactile printed aesthetics.

Useful terms:
- paper stock
- letterpress impression
- emboss / deboss
- foil stamping
- spot UV varnish
- overprint
- halftone
- CMYK misregistration
- risograph grain
- screenprint ink density
- deckled edge

Prompt examples:

```text
thick uncoated paper stock with subtle tooth; black ink slightly sinks into fibers; small red mark uses spot color overprint
```

```text
letterpress impression visible around the title, shallow debossed edges catching side light, no glossy digital poster finish
```

Avoid:
- random grunge
- print terms without paper/ink behavior
- fake text artifacts

## 5. Product And Industrial Design

Use for vehicles, props, weapons, gadgets, furniture, tools.

Useful terms:
- silhouette
- chamfer, bevel radius
- parting line
- seam, gasket, fastener
- CNC-milled, anodized aluminum
- injection-molded plastic
- knurling, grip texture
- tolerance, flush fit
- venting, heat sink fins
- ergonomic contact zones
- wear zones

Prompt examples:

```text
CNC-milled aluminum body with tiny bevel radius, flush seams, visible fasteners only at service panels, and knurled grip texture where fingers touch
```

```text
motorcycle design has a long low silhouette, functional vents near heat sources, rubberized foot pegs, worn contact zones, and no decorative greebles
```

Avoid:
- random sci-fi panels
- meaningless vents
- overdesigned glowing seams

## 6. Architecture And Interior Design

Use for buildings, rooms, cities, public spaces, sci-fi worlds.

Useful terms:
- massing
- circulation
- threshold
- fenestration
- clerestory light
- atrium
- cantilever
- plinth
- shadow gap
- material junction
- human scale
- axial symmetry
- wayfinding

Prompt examples:

```text
brutalist massing with heavy concrete volumes, narrow clerestory light, deep shadow gaps at material junctions, and a human figure showing scale
```

```text
interior circulation is clear: entry threshold, long sightline, central atrium, and warm wayfinding light pulling the viewer forward
```

Avoid:
- random futuristic building shapes
- architecture with no entrances, scale, or circulation
- plants pasted on glass towers as "eco"

## 7. Fashion And Textile

Use for characters, costumes, editorial covers, historical clothing.

Useful terms:
- silhouette
- drape
- bias cut
- dart, pleat, gusset
- lapel, cuff, hem
- topstitching
- seam allowance
- selvedge
- rib knit, jacquard, twill, satin, velvet
- garment layering
- technical shell, bonded seams
- patina and wear at stress points

Prompt examples:

```text
oversized technical shell jacket with bonded seams, matte nylon crinkle, visible topstitching at cuffs, and worn edges only at pocket openings
```

```text
silk satin dress cut on the bias, fabric drapes diagonally across the body with directional sheen along folds
```

Avoid:
- random accessories
- fabric behaving like plastic
- clothing details changing shot to shot

## 8. Beauty, Makeup, And Hair

Use for portraits, covers, character close-ups.

Useful terms:
- skin finish: matte, satin, dewy
- soft glam
- tightline
- contour, blush placement
- highlight on high points
- flyaway hairs
- hair strand grouping
- wet look, glass skin, velvet skin

Prompt examples:

```text
satin skin finish with natural pores; highlight only on cheekbone, nose bridge, and cupid's bow; no plastic beauty filter
```

```text
hair has large dark strand groups plus fine flyaway hairs around the face, rim light catching only outer edges
```

Avoid:
- over-smoothed skin
- glitter everywhere
- makeup changing between shots

## 9. UI / UX / Interface Design

Use for dashboards, apps, diegetic sci-fi UI, product interfaces.

Useful terms:
- information architecture
- affordance
- progressive disclosure
- density
- spacing scale
- design tokens
- focus state, hover state
- affordance contrast
- hierarchy, grouping, scan path
- data ink ratio
- accessibility contrast

Prompt examples:

```text
operational dashboard with compact density, clear grouping, one primary action, muted status colors, and a predictable left-to-right scan path
```

```text
diegetic interface lines originate from fixed wall emitters, align to the body as measurement marks, and disappear after scanning
```

Avoid:
- random floating UI
- decorative cards
- fake text noise

## 10. Data Visualization

Use for infographics, reports, UI, analytical visuals.

Useful terms:
- preattentive attributes
- small multiples
- shared axis
- uncertainty band
- annotation layer
- sequential/diverging/categorical color scale
- outlier labeling
- baseline
- chartjunk
- visual encoding

Prompt examples:

```text
editorial chart uses a shared axis and one red preattentive highlight for the outlier; annotations explain the turning point, no chartjunk
```

Avoid:
- colorful charts with no argument
- decorative 3D charts
- unreadable labels

## 11. Food, Culinary, And Beverage

Use for food photography, restaurant scenes, product ads.

Useful terms:
- Maillard crust
- crumb structure
- translucency
- condensation
- meniscus
- oil sheen
- char marks
- steam backlight
- plating negative space
- ceramic glaze

Prompt examples:

```text
bread crust shows Maillard browning and blistered texture; crumb structure remains soft and uneven; grazing warm light reveals flour dust
```

```text
cold glass has condensation droplets of varied size, clear meniscus at the liquid edge, and controlled specular highlights
```

Avoid:
- glossy food everywhere
- fake steam clouds
- overgarnished plating

## 12. Sound And Music Vocabulary For Video Prompts

Even when the tool does not generate audio, sound terms can guide visual rhythm.

Useful terms:
- transient
- reverb tail
- low-pass / muffled
- diegetic sound
- foley
- silence drop
- beat drop
- syncopation
- crescendo
- staccato
- legato

Prompt examples:

```text
visual rhythm behaves like staccato percussion: short held pose, sudden cut, brief impact frame, fast recovery
```

```text
sound-image cue: silence drops for one impact frame, then debris and cloth motion continue as the reverb tail returns
```

Avoid:
- vague "match music" without beat positions
- sound words unrelated to visual pacing

## 13. Craft And Material Culture

Use for handmade objects, historical design, regional aesthetics.

Useful terms:
- joinery
- weave structure
- warp/weft
- glaze crackle
- patina
- hand-thrown ceramic
- hammer marks
- burnished surface
- carved relief
- natural dye variation

Prompt examples:

```text
hand-thrown ceramic bowl with slight asymmetry, glaze pooling near the foot ring, crackle visible in side light, and worn lip edge from use
```

```text
woven textile shows warp and weft variation, natural dye irregularity, frayed selvedge, and raised fiber texture
```

Avoid:
- superficial cultural symbols
- fake handmade randomness without construction logic

## 14. Automotive And Vehicle Design

Use for cars, motorcycles, aircraft, spacecraft, mecha vehicles.

Useful terms:
- stance
- wheelbase
- overhang
- rake
- aerodynamic fairing
- diffuser
- intake
- heat vents
- suspension travel
- tire sidewall
- brake caliper
- carbon fiber weave

Prompt examples:

```text
aggressive low stance, long wheelbase, short rear overhang, functional side intakes, visible brake calipers, and carbon fiber weave only on aero panels
```

Avoid:
- glowing wheels everywhere
- fake vents
- unstable vehicle proportions

## 15. Medical / Scientific / Lab Visuals

Use for trustworthy technical visuals.

Useful terms:
- sterile field
- frosted glass
- powder-coated metal
- gasket seal
- calibrated markings
- sample chamber
- amber safety indicator
- cleanroom lighting
- transparent tubing

Prompt examples:

```text
lab instrument uses powder-coated white metal, transparent sample chamber with accurate refraction, amber safety indicator, and calibrated markings that feel functional
```

Avoid:
- blue sci-fi glow everywhere
- fake unreadable medical UI
- sterile scene with no human usability

## 16. Cross-Domain Transfer Examples

### Fashion + Rendering

```text
technical nylon jacket with bonded seams and matte crinkle texture; AO in folds and under straps; satin inner layer catches anisotropic sheen along movement lines
```

### Architecture + Cinema

```text
brutalist atrium with clerestory light and long axial circulation; low-key cinematography makes concrete mass feel oppressive while preserving wayfinding depth
```

### Product + Photography

```text
CNC-milled object in macro product photography; chamfered edges catch narrow specular highlights, black rubber grip absorbs light, and contact shadow anchors it on matte stone
```

### UI + Film Scene

```text
diegetic scanning interface uses fixed emitters, clear measurement hierarchy, and restrained amber status color; UI light casts subtle bounce on nearby glass
```

### Food + Print

```text
restaurant poster uses letterpress black typography on warm paper stock; food image shows Maillard crust and ceramic glaze, with no glossy template styling
```

## 17. Anti-Keyword-Dump Checklist

Before using domain terms, check:

- Is the term from the right industry?
- Is it attached to a visible object, surface, layout, motion, or sound cue?
- Does it explain cause and effect?
- Does it prevent a known failure mode?
- Can the model see it in the frame?
- Are there too many terms competing?

Good final line:

```text
Use industry terms only where visible: [term] on [object], [term] in [layout], [term] from [light/source], [term] during [motion].
```
