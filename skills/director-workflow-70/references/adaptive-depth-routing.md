# Processing Depth Is an Input

**The execution layer never picks a depth.** `processing_depth` is judged by the
decision layer — **镜语**, the 镜头组架构师 expert run from `G:\工作\分镜` — and
reaches this layer through the console task-context (`prompt-context`); an
explicit user instruction overrides. It arrives here as an input. Read it; never
infer, judge, or re-tier it.

Depth controls backstage work only. It never changes the required camera-group
delivery, six-part prompt, explicit shot blocks, T micro-beats, authoritative
dialogue, or standalone copyability.

## Reading the Depth

1. Read `processing_depth` from the console task-context — the decision layer's
   channel (镜语's explicit selection, or the console's own fallback derivation
   from the recorded signals) — or from an explicit user instruction. Whatever
   it returns is authoritative: never re-derive or re-tier it.
2. Record it verbatim in `TaskEnvelope`, and set `depth_reasons` to **where it
   came from** (`console` / `user` / `caller`) — never to script signals that the
   execution layer derived on its own.
3. Load exactly the chain below that matches the received depth.
4. Re-read the depth for every new camera group and every generation call;
   never cache it across groups or retries.
5. If no depth is supplied, use `standard` **and label it an assumption**. Do
   not reverse-engineer the tier from the script.

The signal lists under Fast / Standard / Full below are **validation checklists,
not selection rules**: use them to confirm the received depth is executable and
to decide which conditional specialists it makes eligible. They never move the
depth by themselves.

Depth answers "how deep". There is **no genre axis**: a scene's genre reaches
this layer only as the signals below, which the decision layer already weighed
when it judged the depth. Never derive, record, or re-tier a genre label here,
and never let one promote the depth. A `depth_override` + `override_risk_signals`
pair sent by the caller always wins.

An observed script signal still gates execution. A scene with no fight, chase,
weapon, or stunt in the text must not load the action chain, whatever anyone
called its genre.

## Received `fast`

Load this chain only when the caller supplied `fast`. It is executable only when
all are true:

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

## Received `standard`

Load this chain for complete scripts and ordinary multi-group short drama,
two-person emotional/dialogue scenes, recurring characters with straightforward
continuity, moderate references, or local material whose risk is not clearly
low. Use the lightweight standard director for one global story, continuity,
space, information, and shot-planning pass. Do not load the full director,
governance, separate cinematography/material/sound baselines, or professional
storyboard owner. If the received depth cannot hold the material, return a named
blocker to the caller instead of re-tiering.

Exact standard chain:

```text
script-camera-group-router
-> camera-group-director-standard
-> narrative-camera-groups
-> exactly one selected platform compiler
-> camera-group-preflight-standard
```

## Received `full`

Load this chain when the caller supplied `full`. Require at least one of the
following to be true; otherwise return a named blocker to the caller:

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
performance -> live-action-performance-direction
emotion -> emotional-performance-direction
single_character_short -> performance-scene-director
relationship_or_dialogue -> relationship-dialogue-direction
ip_likeness_or_safety -> seedance-copyright + seedance-filter when Seedance
```

Scene signals fire these rows: dialogue/emotion/performance signals fire the
emotion, performance, and relationship_or_dialogue rows; a fight signal fires
the action row. These rows must stay in step with `conditionalBySignal` in
`config/routing-contract.json`.

In an `ExecutionPlan`, fight/VFX platform specialists return named fields or a
`state_patch_request`; they do not emit another complete camera-group prompt.
The selected platform compiler remains the only final compiler.

## Caller-Named Capabilities

Twelve skills serve this chain but have **no signal row and no depth of their own**.
They load only when the caller names them or the task plainly matches their single
lane. Four rules:

- They never change or re-tier the received depth.
- They sit **inside** the chain step they serve; they never replace a chain owner
  (`narrative-camera-groups` still owns packaging; the selected compiler still owns
  the final prompt).
- They return decisions or named field patches, never a second complete prompt.
- The four marked **named only** have implicit invocation switched off in both
  `SKILL.md` and `agents/openai.yaml`; the caller must name them explicitly.

| capability | skill | when it loads | lane |
|---|---|---|---|
| shot tension, framing, movement choice | `high-tension-shot-design` | a prompt needs stronger visual pressure than the default shot grammar gives | camera design, before `narrative-camera-groups` |
| film-language terms and mechanisms | `cinema-language-atlas` | a term, movement, lens, or editing mechanism must be chosen or explained precisely | research |
| reference breakdown (拉片) | `film-breakdown-distiller` | the caller supplies a film, clip, or reference video to distill into reusable rules | research, before story and shot design |
| candidate explore-and-select | `bounded-explore-select` | several concepts or variants must be explored and scored inside a fixed budget | concept gate |
| non-text input routing | `constraint-input-router` | text alone cannot hold composition, space, depth, action, or ratio, or reference roles conflict | intake, before shot design |
| cross-shot drift audit | `cross-shot-consistency-audit` | an accepted set of shots or mixed footage must be checked for identity/color/light/space drift | review, after generation |
| visual progression and color script | `visual-calibration-loop` | a script or shot list must be mapped to an emotion curve, color script, and drift-reset rules | cross-group scheduling |
| minimum visual contract | `minimum-visual-bible` | batch or multi-person generation needs a risk-trimmed visual contract first | project setup, before batch generation |
| pure-action showcase, no opponent | `action-showcase-direction` | the piece is a 10-60s weapon/ability showcase with no opponent | action lane — **named only** |
| whole-film kinetic visual master | `kinetic-action-visual-master` | a reusable high-energy visual master or opening style block is required | action lane style anchor — **named only** |
| live-action fantasy VFX | `cinematic-fantasy-vfx-director` | xianxia / ancient-fantasy VFX needs a dedicated director pass beyond the general VFX owner | VFX lane — **named only** |
| CG xianxia effect system | `cg-xianxia-vfx-design` | a CG/xianxia effect system's materials, formations, and rendering must be designed | VFX lane — **named only** |

Naming a capability never adds a chain owner and never widens the depth. If a named
capability cannot do its job at the received depth, that is a blocker, not an upgrade.

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

## Blockers, Not Self-Escalation

`fast` and `standard` do not upgrade themselves. When timing cannot fit without
compression, dialogue/action authority conflicts, spatial causality becomes
unclear, a reference role conflicts, or preflight finds a P0/P1 issue, **stop and
return a named blocker to the caller**: the received depth, the specific blocker,
and the smallest depth that would hold it. Keep all completed valid work. The
caller re-tiers; this layer never silently upgrades or downgrades, and never
loads an unplanned owner on its own.
