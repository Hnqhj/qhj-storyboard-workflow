# Reference Sovereignty And Fidelity Routing

Read this when several references can compete, when an image must be enlarged without semantic drift, when visible evidence is converted into a reconstruction prompt, or when color/material should transfer into fixed geometry.

## 1. Assign ownership before merging references

Every reference gets a narrow contract:

| Field | Decision |
| --- | --- |
| reference ID/version | stable source handle |
| owns | identity, geometry, layout, pose, color relation, material class, pattern, lighting, small detail, comparison only |
| must not control | layers that must not transfer |
| evidence scope | visible region, angle, state and resolution actually proved |
| confidence | observed / inferred / unknown |
| conflict priority | which source wins and why |
| validation | visible check in the result |

Default conflict order:

```text
explicit user instruction
-> identity/product geometry and supplied copy
-> approved layout/region ownership
-> intended action/pose
-> style, light and surface treatment
```

Do not blend two references just because both contain the subject. A real-person identity reference owns facial relationships and stable asymmetry; a character-design reference may own hair silhouette, costume construction, palette, accessories and role, but not replace the person's face, age or ethnicity unless explicitly requested.

## 2. Use one edit contract

```text
Preserve: source-proved variables that must remain.
Change: the only layer this pass may edit.
Exclude: likely failure classes that would break the target.
Unknown: occluded, unreadable or unproved facts that must not be invented as observations.
```

An observation becomes a generation instruction only when it serves the user's target. Compression artifacts, accidental background faces, unreadable text and source mistakes do not automatically transfer.

## 3. Reverse prompting is reconstruction, not recovery

An image does not uniquely reveal its original prompt, model, seed, reference weights, lens, edit history or hidden geometry. Deliver a **visual reconstruction brief / generation estimate**, never a recovered original prompt.

Analyze in this order:

```text
identity/product anchors
-> composition and spatial grammar
-> material, palette and light behavior
-> control locks and reference roles
-> uncertainty register
```

Mark unreadable copy as `unreadable—replace with supplied copy`. Mark focal-length, material, off-camera geometry and hidden surfaces as inferred or unknown unless independent evidence exists.

## 4. Fidelity upscale routing

First decide the implementation class:

| Risk | Preferred route | Acceptance |
| --- | --- | --- |
| text, logo, UI, signature, ticket, precise label | deterministic resample or specialized non-generative reconstruction | glyph/shape and placement comparison; no guessed copy |
| product geometry, garment pattern, mechanical detail | conservative upscale plus region comparison | silhouette, count, label, pattern and seam stability |
| face, hands, recurring identity | identity-aware conservative enhancement | face relationships, expression, anatomy and pose unchanged |
| natural texture with no semantic identity | perceptual enhancement allowed within limits | no new object, edge or material-class drift |

Define the target in pixels and format; “4K” alone is incomplete. Check dimensions, crop, alpha, color profile, compression and sharpening. If sharper output requires invented text, identity or product features, keep the ambiguity or route to an explicit reconstruction task. Do not call generative enhancement lossless.

## 5. Region-bound color and material transfer

Separate the sources of truth:

```text
target/base image -> geometry, camera, perspective and silhouette
mask/region map -> editable ownership
design reference -> visible color relation, material class and pattern
detail crop -> one named small feature only
palette sample -> measurement aid, not pixel obedience
```

For each meaningful region track:

```text
region ID / parent / adjacency / occlusion / edge type
mapping confidence / color relation / material class
micro-texture evidence / reflection family / pattern
```

Split same-color regions when material response differs. Keep small identity- or product-critical parts in their own detail channel. Decide detail importance from semantic value, available pixels and failure history; do not use a universal area threshold.

Colors sampled from a lit image are display evidence, not automatically PBR base color. Sampling requires registered regions and known or compatible color space. HEX, RGB and ΔE can aid measurement but do not guarantee prompt compliance or material correctness.

## 6. Local edit honesty gate

Call a pass “local repair” only when a mask, region binding, layer edit or before/after comparison proves non-target layers stayed stable. A full-frame generative retry with preserve wording is a targeted retry, not a pixel lock.

When a region fails:

```text
failed layer:
change only:
preserve unchanged:
unknown evidence:
visible acceptance check:
fallback tool/input:
```

Escalate from prompt/reference to mask or region control, then to registered compositing/3D/UV/color-managed tools when the required accuracy exceeds generative control.

## Quality gate

- Every reference owns a layer and is prevented from controlling unrelated layers.
- Observed, inferred and unknown statements are separated.
- Fidelity claims name an implementation and a visible comparison.
- Text, logos, identity and product geometry never rely on unverified generative guessing.
- Region transfer tracks adjacency, occlusion, confidence and material response, not only color names.
- “Local,” “lossless,” “pixel-accurate,” “official grade,” and “original prompt” appear only when the evidence and toolchain support them.
