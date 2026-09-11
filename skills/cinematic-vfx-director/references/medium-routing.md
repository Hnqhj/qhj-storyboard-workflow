# Medium-Aware VFX Routing

The same event should not be described identically across photoreal CG, stylized 3D, 2.5D, and pure 2D.

## Premium Photoreal / Cinematic CG

Prioritize:

- photographic shutter behavior and directional vector blur;
- physical wake, material fracture, gravity, drag, collision, and settling;
- controlled refraction, heat distortion, volumetric density, and emissive light spill;
- depth-correct occlusion and environment reflections;
- restrained effect count and localized high-frequency detail.

Failure mode: a technically detailed simulation with no clear silhouette, timing hierarchy, or directed force.

## Stylized CG / 2.5D / NPR

Prioritize:

- expressive key poses and limited interpolation where appropriate;
- geometry smears, pose multiples, speed/focus lines, and one-frame graphic accents;
- 2D hand-drawn effects layered over stable 3D contact, depth, and camera;
- artist-controlled shadow, rim light, and silhouette deformation;
- temporal stability of lines, hatching, and graphic shapes.

Failure mode: photoreal particles pasted over toon characters, or generic bloom used instead of designed shape language.

## Pure 2D / Hand-Drawn Animation

Prioritize:

- clear silhouette and line of action;
- contrast between held anticipation and fast release;
- smear drawings, contour break, shape rhythm, line-weight change, and directional debris;
- impact frames used selectively and designed to match the palette;
- effects animated as shapes with life cycles, not as transparent overlays.

Failure mode: smooth interpolation that erases key-pose contrast, or full-screen glow that flattens drawing hierarchy.

## Mixed Media

Assign roles explicitly:

```text
3D layer: camera, depth, body/prop contact, gross simulation
2D layer: graphic smear, line, accent shapes, impact image
composite layer: occlusion, light spill, atmosphere, grain, color integration
```

Failure mode: each layer follows a different frame cadence, blur model, black level, and light direction.

## Motion-Effect Selection Matrix

| Device | Photoreal CG | Stylized CG/2.5D | Pure 2D |
|---|---:|---:|---:|
| Shutter blur | primary | support | rare/imitated |
| Geometry smear | rare/subtle | primary | drawn smear equivalent |
| Pose multiples | special case | strong | strong |
| Speed/focus lines | restrained | strong | strong |
| Ribbon trail | physical/volumetric | graphic + depth | drawn shape |
| Impact image | rare/selective | strong | strong |
| Physical wake | primary | primary with simplification | designed debris shapes |

Use one dominant device per beat. More devices do not automatically create more tension.
