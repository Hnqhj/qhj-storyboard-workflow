# Evidence-Bound Material Transfer

Use this branch for replication or transfer, where the reference should constrain a fixed target. It is stricter than ordinary creative material design.

## Source roles

```text
base/white model: geometry, silhouette, camera, perspective and existing seams
mask or region map: editable ownership and boundaries
design reference: visible color relations, material classes and patterns
detail crop: one named small feature
palette measurement: diagnostic aid only
```

Resolve conflicts in that order unless the user specifies another owner. A color reference never gets authority to change target geometry; a base model never invents the design reference's hidden material.

## Region ledger

For each important surface, record:

```text
region ID and parent
adjacent regions and occluders
edge type: structural seam / soft transition / overlap / unknown
mapping confidence: observed / inferred / unknown
color relation and value range
material class and roughness/reflection family
pattern orientation and scale
micro-texture evidence
```

Split equal-color regions when their material response differs. Keep eyes, labels, fasteners, jewelry, emblems, trim and other semantically critical small parts in separate detail channels even when their area is tiny.

## Evidence-only rule

In replication mode, do not add pores, wear, patina, scratches, weave, embossing, dirt or micro-decoration merely to make the result feel premium. Add a micro-surface feature only when the source proves it at usable scale or the user explicitly authorizes interpretation. Record hidden backsides, occluded joins and unreadable patterns as unknown.

## Color boundary

A lit reference provides displayed color, not automatically intrinsic/base color. Sample only registered regions in a known or compatible color space; distinguish highlight, midtone and shadow contamination. HEX/RGB values are measurement anchors. They are not evidence that a generative model obeyed pixel color or that a PBR material is correct.

## Execution ladder

1. Verify that base and reference can be registered; if not, create a region correspondence or change tools.
2. Apply broad region color relationships.
3. Apply material response and patterns only inside owned regions.
4. Apply small detail through named crops/regions.
5. Repair seams, overlaps and occlusion boundaries.
6. Compare structure, region ownership, color relation, material behavior, pattern and small details separately.

Call a stage locked only when mask/region/layer control or before/after evidence proves unrelated layers stayed stable. Full-frame prompt wording alone does not lock pixels.

## QA boundary

- Edge comparison can flag change but cannot by itself distinguish correct color/pattern edges from geometry drift.
- Region median ΔE can flag color difference but cannot by itself judge material under different lighting or tone mapping.
- Fixed F1, ΔE, area and percentile thresholds require calibration on representative cases; do not import defaults as universal gates.
- Check mask overlap, coverage holes, feathering, registration, ICC/profile handling, output size and human-visible identity/product errors.

If reliable masks, registration or color management are unavailable, downgrade the claim to reference-guided interpretation and preserve the evidence/unknown ledger.
