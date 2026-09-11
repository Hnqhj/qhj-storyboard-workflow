# Rule Routing

Use this file for every request. Select one primary source module and read it completely before drafting. Load no unrelated source files.

## Route by subject

| User intent | Primary source | Composition choice |
| --- | --- | --- |
| Giant building, city, wall, temple, machine-city, arcology, bridge, habitat, artificial structure | `source-megastructure-infinite-frame.txt` or `source-megastructure-partial-reveal.txt` | Choose between an unbounded fragment and one revealed dimension |
| Broad architectural exploration without a clear crop strategy, or a deliberately rendered architectural concept | `source-megastructure-foundation.txt` | Use as the broad foundation; resolve its rendering vocabulary against the requested medium |
| Kaiju, mythic giant, alien fauna, giant beast, recognizable creature family | `source-colossal-creature.txt` | Complete silhouette or monumental partial anatomy |
| Cthulhu, eldritch god, unknowable cosmic entity, cosmic horror | `source-cosmic-horror.txt` | Preserve unreadable scale and unfamiliar anatomy without forcing gore |
| Entirely original biological entity with no known species and no inorganic body matter | `source-pure-organic-entity.txt` | Enforce the strict organic vocabulary and inorganic reference-object rule |

## Choose the architecture variant

### Unbounded fragment

Read `source-megastructure-infinite-frame.txt` when the concept should feel impossible to survey. Use multiple cropped edges, 10–40% environmental negative space, and a distant reference object. Do not reveal the whole isolated structure.

Typical requests:

- an endless city wall crossing a continent
- only one portion of an orbital elevator or planetary machine
- a structure that should feel oppressive because its limits cannot be seen

### One dimension revealed

Read `source-megastructure-partial-reveal.txt` when one complete measurement is essential to the idea. Show one full height, width, cross-section, opening, support, or terrace while another dimension continues beyond the frame. Keep 10–40% environmental negative space.

Typical requests:

- show the complete height from ground to summit
- reveal the full diameter of a gate while the wall continues beyond both sides
- show one entire support leg beneath a chassis that exits the frame

### Broad foundation

Read `source-megastructure-foundation.txt` when the request is exploratory or specifically asks for a rendered concept rather than photographic realism. This module contains useful core logic but also includes legacy renderer vocabulary. The requested medium controls the final wording:

- photorealistic or documentary result: omit `UE5`, `3D render`, and `CG`
- deliberate concept render or digital illustration: rendering language is allowed

## Distinguish creature modes

### General colossal creature

Use `source-colossal-creature.txt` when known animal families, mythological creatures, or recognizable kaiju anatomy are allowed. A comparison such as reptilian, mammalian, crustacean, or whale-like may be used only when it helps the user's concept.

### Cosmic horror

Use `source-cosmic-horror.txt` when fear comes from unknowable anatomy, alien scale, cosmic context, repetition of organs, or a failure of ordinary spatial understanding. Do not automatically add tentacles, eyes, slime, or decay; choose only details that support the brief.

### Pure-organic original entity

Use `source-pure-organic-entity.txt` only when the creature itself must be fully biological and unlike any named real species. Enforce these rules strictly:

- no known animal or species name in the creature description or reference object
- no metal, stone, crystal, soil, machinery, architecture, or other inorganic body material
- environment may contain inorganic matter
- scale references must be inorganic, such as buildings, ships, trains, vehicles, or industrial equipment

Generic biological anatomy and tissues remain allowed: flesh, muscle, hide, keratin, chitin, scales, fur, bone, pores, glands, membranes, veins, tendrils, sensory pits, and respiratory openings.

## Mixed subjects

Load a second module only when the mixture is the concept rather than decoration.

- **Living architecture:** define which parts are habitable construction and which are living tissue. Read one architecture module plus `source-pure-organic-entity.txt` only if the biological portion must obey pure-organic constraints.
- **Entity attached to a city or machine:** keep the creature and environment materially separate. Do not accidentally describe metal or masonry as part of a pure-organic body.
- **Cosmic entity beside a megastructure:** choose which one is the absolute subject and keep the other as a scale reference or secondary system.

## Reference-image routing

- If the image supplies only visual language, choose the source category from the user's desired new subject.
- If the image contains the subject to preserve, route from the observed subject and state which identity features must remain stable.
- If the image is not passed to the generator, make the final prompt standalone and remove reference-dependent wording.

## Source-use discipline

The source files retain strong wording and examples. Apply their structural logic, but do not copy example-specific subjects, dimensions, colors, environments, or comparison objects unless independently justified by the user request.

