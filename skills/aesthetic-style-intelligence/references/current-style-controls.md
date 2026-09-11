# Current Style Controls

Purpose: compact reusable controls distilled from `style-intelligence-ledger.md`. Use this file for actionable style direction. Use the ledger for evidence and status history.

## Use Rules

- Pick one primary control family per task.
- Add secondary controls only when they affect different layers: material, motion, typography, interface, space, sound, identity, or prompt workflow.
- Keep negative boundaries. They are part of the style control, not optional cleanup.
- Route final execution to companion skills. This file supplies style intelligence, not complete prompts.
- Prefer `tracked` controls for production. Use `candidate` controls only with validation or explicit exploration.

## Control Families

### Prompt And AI Video Control

Status: tracked
Use when: AI video/image workflows need consistency, camera discipline, or reference planning.
Controls:
- Reference-scoped continuity stack: identity, object, location, material, lighting, and mood references must each control only their assigned layer.
- Shot-grammar-first prompting: define shot type, camera movement, character, action, location/weather, then add one bounded aesthetic layer.
- Audio-image coupled shot: sound cues should describe texture, impact, distance, rhythm, and space, not generic soundtrack mood.
- Reference authority hierarchy: composition and motion references can override manual prompt text; do not write conflicting camera instructions.
Companion skills: character-continuity-bible, ai-video-prompt-preflight, cinematic-audiovisual-language, cinematic-music-sound-design, jimeng-sd2-prompting
Prompt/control phrase: "shot grammar first; reference stack assigns identity/object/location/material/light/mood separately; motion reference controls camera path; sound is coupled to visible action."
Negative boundary: no style soup, no moodboard as character lock, no contradictory reference and camera instructions, no generic "cinematic audio".
Misuse risk: identity bleed, camera drift, audio clutter, and overfitted style mimicry.

### Interface And Procedural Design Systems

Status: tracked
Use when: UI, product systems, design tools, motion specs, shader effects, or interactive surfaces need non-generic direction.
Controls:
- Context-responsive glass UI: translucent controls must remain legible, adaptive, and hierarchically separate from content.
- Canvas-native procedural material: code layers, motion timelines, shader parameters, and generative tools should be editable on the design canvas with inspectable values.
- Everyday action interface staging: ordinary behavior becomes understandable through modular stations, icons, props, and cause-effect feedback.
Companion skills: figma:figma-generate-design, figma:figma-implement-motion, visual-style-aesthetic-direction, ai-material-realism, visual-reference-vocabulary
Prompt/control phrase: "interactive control layer remains readable; procedural effects expose parameters; everyday actions are staged as modular feedback stations."
Negative boundary: no decorative glass blobs, no hidden effects posing as systems, no generic gamification.
Misuse risk: weak information hierarchy, unbounded effects, or toy-like clutter.

### Material And Product Surface Logic

Status: tracked
Use when: products, interiors, craft, material studies, fashion objects, or physical props need believable surface rules.
Controls:
- Optical material overlay lab: surface is a stack of substrate, translucent overlay, viewing angle, color shift, and crisp sample edge.
- Adaptive affordance as product geometry: accessibility is expressed through step-in structure, pull zones, tactile cues, low-pressure closure, and stability.
- Korean material heritage as contemporary surface engine: retain process operations such as bind, layer, fire, lacquer, wrap, patch, weave, or contrast old substrate with industrial support.
Companion skills: ai-material-realism, production-design-worldbuilding, visual-reference-vocabulary, visual-style-aesthetic-direction
Prompt/control phrase: "material is a process stack; accessibility is product geometry; craft lineage is shown through operation, not motif."
Negative boundary: no rainbow holographic sludge, no medicalized accessibility aesthetics, no decorative heritage pattern dumping.
Misuse risk: flattened shiny gradients, symbolic inclusivity, or cultural stereotypes.

### Architecture And Public Space

Status: mixed; use tracked controls freely, validate candidates.
Use when: buildings, pavilions, exhibitions, facades, urban installations, or environmental design need spatial rules.
Controls:
- Porous structural wall as climate filter: curved/repeated units, narrow gaps, shade, airflow, and procession turn walls into filters.
- Site-data facade sculpture: local measured data drives large distance-readable architectural media.
- One-to-one civic prototype urbanism: test public-space ideas at body scale with touch, shade, sound, play, ecology, and resident reinterpretation.
- Reclaimed offcut public pause field: material reuse becomes legible through occupied topography, seating edges, circulation, provenance, and planting.
- Furniture as architectural signal: furniture sets spatial logic through supports, voids, shells, tubular lines, and wall-plane extensions.
Companion skills: production-design-worldbuilding, ai-material-realism, cinematic-audiovisual-language, visual-style-aesthetic-direction
Prompt/control phrase: "public space is tested at body scale; material systems show structure, climate response, provenance, and human affordance."
Negative boundary: no speculative render-only pavilion, no generic AI swirl, no fortress wall when the goal is permeability, no decorative reuse without occupation.
Misuse risk: photogenic but unusable forms, impossible construction, or data-art without data source.

### Graphic Identity And Brand Systems

Status: tracked
Use when: branding, editorial, typography, packaging, motion identity, or exhibition graphics need system-level control.
Controls:
- Cross-format graphic identity stress test: type, mark, layout, and hierarchy must survive package, poster, website, film title, and spatial sign.
- Object-photo-flat-space graphic loop: build identity by cycling object arrangement, photographed light, flat print, book, and exhibition space.
- Physical-optical brand mnemonic: real optical behavior anchors brand mark, motion, color, and sound.
Companion skills: visual-style-aesthetic-direction, visual-reference-vocabulary, ai-material-realism, cinematic-music-sound-design
Prompt/control phrase: "identity must survive across formats; physical light or optics should mediate the graphic form before motion extension."
Negative boundary: no poster-only taste, no logo pasted everywhere, no generic glossy logo animation, no flat vector geometry without light behavior.
Misuse risk: inconsistent mockup sets, weightless vector graphics, or attractive effects that do not function as a mnemonic.

### Moving Image, Animation, And Sound

Status: tracked
Use when: animation, installation, gallery cinema, music-image systems, or stylized video need temporal rules.
Controls:
- Controlled instability painterly animation: visible brush texture and slight edge shimmer are allowed only while silhouette, costume, and shot rhythm stay coherent.
- Parallel-time audiovisual installation: image and sound can avoid literal sync if each has a legible temporal grammar and meet through spatial immersion.
- Live media design as urban facade cinema: public-screen video needs distance-readable silhouettes, slow architectural motion, and facade-aware contrast.
Companion skills: cinematic-audiovisual-language, cinematic-music-sound-design, action-rhythm-editing, jimeng-sd2-prompting, ai-material-realism
Prompt/control phrase: "temporal style must specify what is stable, what drifts, and how sound/image rhythms relate."
Negative boundary: no random AI warping, no music visualizer pulse, no phone-first dense edits for facade media.
Misuse risk: continuity failure mistaken for texture, arbitrary desync, or overpacked detail that disappears at scale.

### Fashion, Body, And Figurative Realism

Status: mixed; validate candidates.
Use when: garments, bodies, performance humans, figurative sculpture, or character realism need material and scale discipline.
Controls:
- Heat-adaptive formalwear: preserve formal cues while using breathable fabric, short hems, air gaps, vented layers, and cooling props.
- Portable real-time human asset discipline: face, body, groom, wardrobe, and performance are separate locked layers.
- Scale-distorted hyperreal figure: anatomical realism remains stable while body scale, isolation, and viewer distance are deliberately broken.
Companion skills: character-continuity-bible, production-design-worldbuilding, ai-material-realism, cinematic-audiovisual-language, visual-style-aesthetic-direction
Prompt/control phrase: "body design locks identity and material realism; garment or figure distortion must specify which layer changes and which remains stable."
Negative boundary: no generic beachwear, no waxy perfect skin, no interchangeable influencer face, no horror doll exaggeration.
Misuse risk: loss of formality, over-smoothed humans, grotesque anatomy, or costume/body identity contamination.

### Real-Time And Interactive Proof

Status: candidate
Use when: game cinematics, live demos, interactive tools, virtual production, or real-time graphics need evaluation criteria.
Controls:
- Live-audience real-time proof: expose visible control, immediate response, repeatable state change, and performance-safe visuals.
Companion skills: cinematic-audiovisual-language, production-design-worldbuilding, visual-style-aesthetic-direction
Prompt/control phrase: "show what is controllable, what changes in response, and how the state can be repeated live."
Negative boundary: no offline render lookbook, no fake UI overlay, no cinematic camera move that hides interaction.
Misuse risk: glossy stills that fail to prove real-time behavior.

## Deprecated Or Rejected Patterns

- Empty taste labels: premium, cinematic, dreamy, edgy, elegant, immersive, futuristic.
- Viral trend terms without visible rules: glassmorphism comeback, AI data art, sustainable material trend, urban intervention trend.
- National or regional shorthand without mechanisms: Japanese graphic design look, Korean style, Asian aesthetics.
- Prompt-pack language that hides control layers: cinematic audio, reference style, high-end render, generative swirl.

## Promotion Rules

- Promote `candidate` to `tracked` only after repeated credible evidence or a successful applied task.
- Promote `tracked` to `stable` only when the rule is bounded, reusable across at least two contexts, and still useful without the named source.
- Mark `deprecated` when a signal becomes overused, misleading, model-dirtying, culturally flattening, or no longer technically reliable.
