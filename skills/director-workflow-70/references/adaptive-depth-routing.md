# Adaptive Processing Depth

Select processing depth automatically before loading conditional specialists.
Depth controls backstage work only. It never changes the required camera-group
delivery, six-part prompt, explicit shot blocks, T micro-beats, authoritative
dialogue, or standalone copyability.

## Decision Order

1. Start at `standard`.
2. Upgrade to `full` when any full-depth trigger is present.
3. Downgrade to `fast` only when every fast-path condition is satisfied.
4. Record `processing_depth` and concise `depth_reasons` in `TaskEnvelope`.
5. Escalate during execution if a new risk appears; never silently downgrade.

## Fast

Use only when all are true:

- local fragment or one straightforward scene;
- no more than two active speaking/performing characters;
- dialogue, restrained emotion, or simple non-contact movement;
- one location and no cross-episode continuity dependency;
- assets and reference roles are sufficient and non-conflicting;
- target platform/mode is known;
- no fight, chase, weapon contact, stunt, transformation, destruction, fantasy
  VFX, complex crowd blocking, generated-output diagnosis, or current-fact
  research need.

Run one fused planning pass for story function, continuity, space, ShotLedger,
CameraGroupPlan, detailed six-part packaging, and mechanical preflight. Apply
the compact camera/material/sound baselines already present in the delivery
contract. Do not load separate research, worldbuilding, action, VFX, advanced
performance, entity-registry, or review layers unless a trigger appears.

Exact fast chain, including the already active router:

```text
script-camera-group-router
-> narrative-camera-groups
-> seedance-camera-group-compiler-fast
-> camera-group-preflight-fast
```

Any additional director, storyboard, material, sound, research, full-platform,
delivery, or full-preflight Skill invalidates `fast` and requires escalation.

## Standard

Use by default for complete scripts and ordinary multi-group short drama,
two-person emotional/dialogue scenes, recurring characters with straightforward
continuity, moderate references, or local material whose risk is not clearly
low. Use the lightweight standard director for one global story, continuity,
space, information, and shot-planning pass. Do not load the full director,
governance, separate cinematography/material/sound baselines, or professional
storyboard owner unless the route escalates to `full`.

Exact standard chain:

```text
script-camera-group-router
-> camera-group-director-standard
-> narrative-camera-groups
-> exactly one selected platform compiler
-> camera-group-preflight-standard
```

## Full

Use when any condition is true:

- fight, chase, weapon/body contact, stunt, heavy physical interaction, or
  complex action causality;
- fantasy/CG VFX, transformation, destruction, creature, vehicle, or complex
  material simulation;
- three or more simultaneously active performers with meaningful blocking,
  crowd action, multiple locations, cross-group/episode state, or fragile
  identity/prop continuity;
- several references with overlapping/conflicting roles, missing P0 evidence,
  uncertain generation mode, or current platform capability research;
- commercial/final delivery requiring evidence, a generated-output review or
  retry, performance/emotion direction, relationship/dialogue direction,
  IP/likeness or safety review, or an explicit request for exhaustive
  professional analysis.

Run the full applicable specialist stack, source/research checks, ownership
arbitration, linter, and full preflight.

Use this full base chain, then add only specialists whose signal fired:

```text
script-camera-group-router
-> ai-video-prompt-director
-> ai-video-production-governance
-> cinematic-audiovisual-language
-> professional-storyboard-director
-> ai-material-realism
-> cinematic-music-sound-design
-> narrative-camera-groups
-> exactly one selected platform compiler
-> ai-video-prompt-preflight
```

```text
continuity -> character-continuity-bible
action -> action-choreography-reference + action-rhythm-editing
          + seedance-fight-director when Seedance
VFX -> cinematic-vfx-director + vfx-effect-construction-engine
       + seedance-vfx when Seedance
research -> creative-research-first
generated output -> ai-video-output-review
retry -> ai-video-output-review + ai-video-iteration-doctor
```

In an `ExecutionPlan`, fight/VFX platform specialists return named fields or a
`state_patch_request`; they do not emit another complete camera-group prompt.
The selected platform compiler remains the only final compiler.

## Single-Pass Budget

- `narrative-camera-groups` owns canonical group packaging and prompt structure.
- Load exactly one of `seedance-camera-group-compiler-fast`, `seedance-20`, or
  `jimeng-sd2-prompting` for one final prompt.
- Set `max_prompt_compile_count=1`; preflight returns findings or field patches,
  never a rewritten full prompt.
- When research is required, run `creative-research-first` once, write one
  `ResearchReceipt`, and require every downstream Skill to reuse it.
- Pass only the approved state slice and named specialist patches between
  owners. Do not replay the whole script, imported mega-prompt, or previous
  conversation transcript to each downstream Skill.
- Run one authoritative review per owned surface. A P1/P0 finding reopens only
  the named owner with one field patch; it does not restart the entire stack.

## Escalation Guard

Fast and standard routes immediately escalate when timing cannot fit without
compression, dialogue/action authority conflicts, spatial causality becomes
unclear, a reference role conflicts, or preflight finds a P0/P1 issue. Keep all
completed valid work and add only the newly required owner.
