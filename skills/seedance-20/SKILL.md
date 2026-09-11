---
name: seedance-20
description: "Full Seedance platform compiler and capability router for standard/full ExecutionPlans, continuation, FLF2V, V2V/R2V, all-reference work, provider/API/model questions, safety/IP repair, or troubleshooting. For a low-risk script-camera-group fast route, use seedance-camera-group-compiler-fast instead. Not for non-Seedance models or image-only prompting."
license: MIT
metadata:
  version: "6.1.0"
---

# seedance-20

For substantial script, sequence, or reference-driven work, receive the merged
state from `$ai-video-production-governance` and the approved shot/group plan
from the storyboard owners before compiling. This skill is the Seedance surface
adapter: it may change platform syntax, mode wording, and handle formatting,
but may not change authority text, story facts, timing, continuity, or camera
ownership.

For Liu's recurring live-action short-drama script workflow, read `../director-workflow-70/references/short-drama-director-stack.md` before platform compilation. The director brain and storyboard leaders decide story, shot groups, timing, action, VFX, performance, and sound; this skill validates the active Seedance surface/mode and compiles the approved group prompt without changing its dramatic plan.

### ExecutionPlan Compile-Only Mode

When `ExecutionPlan.platform_compiler=seedance-20` and approved
`StoryContract`, `ShotLedger`, and `CameraGroupPlan` already exist, skip intake,
interview, directing, sequence redesign, and duplicate prompt-building routes.
Consume only those structured objects, current continuity/asset locks, accepted
specialist field patches, audio authority, and any existing `ResearchReceipt`.
Do not browse again when that receipt exists. Render each final camera-group
prompt once and record `compiled_by=seedance-20` and `compile_count=1`.
Preflight may return a named field patch to this compiler; it may not request or
author a second full prompt.

For a script-derived camera-group `ExecutionPlan`, before compiling any
generation prompt, call
`skill_console_prompt_compilation_context` with the current `threadId` and the
approved state slice. Read the task file again for every group and retry; the
returned `processing_depth` and `prompt_description_complexity` override stale
state or defaults. After writing the platform-facing six-part block, call
`skill_console_compile_prompt` once with `compiler=seedance-20` and use its
returned `promptText` as the only generation text. A failed call blocks handoff
and must produce a named state patch instead of an unprofiled fallback. Persist
the returned `compilationReceipt` on the matching `PlatformPromptSet` unit.

Apply the returned profile exactly: `low` keeps six sections, exact dialogue,
complete structure, and simple shot wording while removing duration limits and
`T=` micro-beats; `medium` keeps duration limits and simple shot wording while
removing `T=` micro-beats; `high` keeps complex shot wording, duration limits,
and contiguous `T=` micro-beats. `processing_depth` controls the backstage
route only and never permits a second compiler or a second prompt pass.

Direct image prompts, standalone non-script video prompts, troubleshooting, and
other tasks outside the camera-group route do not use this task-bound profile;
keep their existing platform behavior.

Repeated script or script-fragment input is not deduplicated: route it again and
reread the current task settings. Multiple outputs for one group are allowed
only when the user explicitly requests variants; assign distinct `variant_id`
values and compile each once with its own receipt.

This compile-only branch takes precedence over the operating loop below. In this
branch, do not run intake, Sequence Gate, Direction, or a second creative
quality pass. Perform only platform mode/handle syntax, model-surface
compatibility, prompt hygiene, and the selected preflight's named field patches;
leave timing, story, camera, continuity, material, sound, and specialist
semantics to their recorded owners.

Liu audio default: model-facing short-drama prompts contain character dialogue/voice-over and source-coupled dry foley/SFX. Add music, score, BGM, ambience beds, or mood effects only when Liu or the authoritative script explicitly requires them.

Seedance 2.0 operating loop for agent-directed video work. Use this root skill to route, check facts, protect references, and keep prompts compact before loading specialized sub-skills.

## Soul

This skill exists so that a person who arrives with a feeling leaves with a film. Three principles govern everything below:

1. **Hear the intent behind the words.** Users describe outcomes ("make it feel like home"), not parameters. Every gate and sub-skill translates feeling into craft; none of them may hand the translation work back to the user.
2. **Keep the story alive.** Hold a story state across the conversation: subject, mode, look, references, decided constraints, and what failed before. Every skill reads it before asking anything and updates it after acting. A user should never have to repeat a decision, and a new request inherits the world already built.
3. **Evolve with the user.** Speak plainly to a beginner and in director language to a professional - and notice when the same user grows from one into the other across a project. The register adapts; the standards never do.

## Operating Loop

1. Intake: identify the user's goal, production phase, target surface, mode, duration, aspect ratio, references, audio needs, deliverables, and safety/IP risks. If intake surfaces a clear safety, IP, likeness, or evasion risk, jump straight to the safety gate (step 9) before any planning.
2. Source gate: load `[ref:api-status]`, `[ref:source-registry]`, and any
   platform matrix only for capability/API/provider/current-feature claims or
   an uncertain mode. For an approved camera-group plan using known natural-
   language generation, do not load them.
3. Professional gate: load `[ref:pro-filmmaking-standards]` only when the
   requested deliverable includes professional post, localization, color,
   subtitles, campaign delivery, or QC beyond prompt compilation.
4. Sequence Gate: classify the request as `standalone_clip` or `sequence_project` before the Mode Gate. Use `sequence_project` for long stories, connected clips, continuation/extend/next-part requests, dense action/dialogue scenes, campaigns, or any idea whose beats cannot clearly fit inside one verified active-surface generation. In Liu's workflow, a **CameraGroup** is the director's planning unit and a **GenerationSegment** is the platform submission unit: default 1:1, but split one group into multiple segments only when the verified model limit or action/continuity complexity requires it. `$narrative-camera-groups` owns group boundaries and human delivery; this skill compiles each approved segment without changing story facts, timing, continuity, or camera ownership. For sequence work, load `[skill:seedance-sequence]`, `[ref:sequence-project-state]`, `[ref:continuation-handoff]`, and `[ref:prompt-compiler]`; for continuation, repair-tail, or re-anchor requests, also load `[skill:seedance-continuation]`.
5. Mode gate: choose T2V, I2V, V2V, R2V, FLF2V, edit, native extend when verified for that surface, or troubleshoot before writing prose.

   Mode availability is surface-specific: edit and extend exist on Dreamina and Ark routes; fal has no dedicated extend endpoint - to continue a clip on fal, prefer reference-to-video with the previous clip as a video reference (keeps motion and audio context), and chain image-to-video from its last frame as the fallback. Provider/router surfaces can rename the same job type, hide fields, or expose only selected modes; recheck their current docs before implementation.

6. Capability check: load `[ref:capability-map]` and `[ref:allocation-model]`
   only when mode, duration, reference limits, or provider behavior is unsettled.
   Do not reopen capability planning for an approved standard camera-group plan.
7. Reference map: assign every asset one primary role: identity, first frame, last frame, product, environment, motion, camera, timing, audio, or style. State what must not transfer.
   - When named five-view character assets are uploaded, preserve their exact platform handles as `@角色名` in every model-facing character mention. This is distinct from file/reference tags such as `{{Image 1}}`; `@Image1` and `@Video1` remain invalid file handles in Liu's prompt format.
8. Multilingual gate: if the prompt uses Chinese, Russian, Japanese, Korean, Spanish, or code-mixed wording, load `[ref:multilingual-community-examples]` and preserve reference tags exactly. For native Chinese, Japanese, or Korean example-driven requests, route to `[skill:seedance-examples-zh]`, `[skill:seedance-examples-ja]`, or `[skill:seedance-examples-ko]`.
9. Safety gate: route IP, likeness, voice, brand, real-person, graphic, or evasion-like wording through `[skill:seedance-copyright]` or `[skill:seedance-filter]`.
10. Direction: load `[ref:directing-engine]` only when this Skill owns an
    unresolved scene direction. When upstream supplies `StoryContract`,
    `ShotLedger`, and `CameraGroupPlan`, inherit them and compile; do not perform
    a second directing pass.
11. Prompt build: route to `[skill:seedance-interview]`, `[skill:seedance-prompt]`, `[skill:seedance-prompt-short]`, `[skill:seedance-sequence]`, `[skill:seedance-continuation]`, or a domain skill for camera, motion, lighting, audio, characters, VFX, style, recipes, or pipeline.
12. Quality pass: for direct/full platform work, run anti-slop and directing
    coherence checks. In compile-only camera-group work, limit this to platform
    syntax, handle integrity, selected mode compatibility, and prompt hygiene;
    do not repeat upstream semantic review.
13. Repair loop: when a take returns, triage it with `[ref:retake-protocol]` (keep / fix in post / edit / re-roll / rewrite, one variable per retake, inside an attempt budget); if it fails outright, diagnose root cause before adding adjectives via `[skill:seedance-troubleshoot]`.


## Liu Prompt Contract Hard Gate

For every Liu script-derived prompt, including a complete script, local
fragment, dialogue block, or single continuation beat, the final paste-ready
block for each camera group must follow this exact six-part order:

```text
角色/资产锁定
视觉材质总控
镜头语言总控
事件节拍
声音
正向稳定约束
```

For a local fragment or single continuation beat, compile one or more scoped
local camera groups. Keep the local planning scope, but require a local shot
table and one complete six-part prompt per group. Record
`TaskEnvelope.output_format = six_part` and preserve it through preflight.

Do not compress the six sections into labels or generic summaries. Every
section must carry useful current-group controls. `事件节拍` restates every shot
with shot number, timecode/duration, shot size, position/height/angle, focal
length or perspective, depth of field/focus, light direction/quality/color
temperature/shadows, camera movement/path, action/performance, verbatim
authoritative dialogue, cut trigger, ending state, and handoff. Never use
`同上`, `沿用`, `参考镜头表`, or `保持不变` as a substitute for these details.
The structured `ShotLedger` always retains contiguous in-shot `micro_beats`
on the absolute camera-group timeline. Render them as `T=起始-结束s` lines only
for the `high` prompt profile; `low` and `medium` keep the shot window and
concrete event prose without T lines. When rendered, each T line carries one
observable action, performance, camera change, sound sync point, or resulting
state and sits under an explicit shot block such as `镜头01｜起始-结束s`.

Maintain a dual-layer asset mapping: stable internal `asset_id` and role are the
source of truth; the compiler may render the platform's exact `@角色名`,
`@文件名`, or backend `{{Image N}}` handle. Never invent, rename, or renumber a
handle during compilation, and never let a platform handle change the approved
asset role.

Paste-ready prompt policy: the model-ready code block is positive-only. It states only what is present, visible, audible, active, and locked in the current shot. Exclusion, absence, correction, comparison to old attempts, and previous-failure wording stay outside the copyable block. If a risk must be controlled, translate it into a positive present-state lock before delivery. In six-part camera-group prompts, `正向稳定约束` is the final control section and contains only positive stability locks. Director, cinematographer, photographer, designer, animation director, manga artist, studio, film, game, and other creative names stay backstage by default; translate their useful mechanisms into concrete composition, blocking, lens, movement, edit rhythm, material, light, color, and performance behavior. Include a name only when Liu explicitly requests named references and the platform/safety contract permits it. Technical camera/material terms support the visible result rather than replacing it.

Source-trace gate: every concrete phrase, including existing subjects, props, locations, palettes, camera routines, transitions, powers, sounds, and stability locks, must trace to Liu's current instruction, a supplied/inspected asset, the active global bible/continuity lock, or a user-approved reusable rule. If the trace fails, omit the phrase from the paste-ready prompt or move it outside as a question/assumption. Remove old-project residue before drafting; do not keep old nouns inside the paste-ready prompt as a way to suppress them.

## Sequence Gate

For a sequence project, do not write Clip 01 until these are known: story objective, final story outcome, ordered major beats, active surface or conservative surface assumption, clip budget, current clip narrative job, and current clip completed endpoint.

Do not write a continuation prompt until the previous accepted clip or its actual final frame has been reviewed and its observed end state recorded.

Sequence invariants:

- every sequence prompt has `project_id` and `clip_id` lineage;
- accepted observed state overrides planned state;
- rejected footage is excluded from canon and cannot become a continuation source;
- future prompts remain provisional until the preceding accepted take is reviewed;
- exact reference tags survive every clip unchanged;
- completed beats cannot replay and reserved future beats cannot leak early;
- continuity state must be updated after each accepted take;
- final Seedance prompts remain natural language unless the user explicitly asks for structured output.

## Load Map

| Situation | Load |
|---|---|
| Vague idea or missing brief | `[skill:seedance-interview]` or `[skill:seedance-interview-short]` |
| Long story, connected clips, campaign sequence, dense action/dialogue scene, or a prompt that needs several generations | `[skill:seedance-sequence]`, `[ref:sequence-project-state]`, `[ref:prompt-compiler]` |
| Continue, extend, next part, repair tail, bridge known states, or re-anchor drift from accepted footage | `[skill:seedance-continuation]`, `[ref:continuation-handoff]`, `[ref:continuity-qc]` |
| Review a generated take and update canon before the next prompt | `[ref:retake-protocol]`, `[ref:sequence-project-state]`, `[ref:continuation-handoff]` |
| Dense animation storyboard or multi-shot prompt | `[ref:dense-storyboard-mode]`, `[ref:multishot-grammar]`, `[ref:2d-anime-grammar]` |
| Production prompt | `[skill:seedance-prompt]`, `[ref:quick-ref]`, `[ref:prompt-examples]` |
| Planning any shot, mode, or budget | `[ref:capability-map]` |
| Where the prompt spends fidelity: identity vs motion vs scene density | `[ref:allocation-model]`, `[ref:intent-vs-precision]` |
| Multi-shot prompt, cuts inside one clip, or shots-per-duration budget | `[ref:multishot-grammar]` |
| 2D, anime, or cel-style motion | `[ref:2d-anime-grammar]`, `[skill:seedance-style]` |
| Professional film, commercial, campaign, or delivery workflow | `[ref:pro-filmmaking-standards]`, `[ref:shot-list-continuity]`, `[ref:delivery-qc]` |
| Compact prompt or Chinese compression | `[skill:seedance-prompt-short]`, language vocab reference |
| Choosing the right camera, light, blocking, performance, and voice for a scene, keeping every choice motivated, or holding one directorial style across a long story | `[ref:directing-engine]` |
| Camera, lens, blocking, shot contract | `[skill:seedance-camera]`, `[ref:cinematography-shot-language]` |
| Image reference / first frame | `[ref:i2v-guide]`, `[ref:reference-workflow]` |
| First and last frame | `[ref:first-last-frame-guide]` |
| API, Runway, Volcengine, fal, provider/router surfaces, China-facing surfaces, workflow, pricing, model IDs | `[skill:seedance-pipeline]`, `[ref:api-workflow]`, `[ref:model-name-map]` |
| Color, ACES, HDR/SDR, aspect ratio, subtitles, audio post, or QC | `[ref:color-pipeline-aces]`, `[ref:aspect-ratio-delivery]`, `[ref:subtitles-localization]`, `[ref:audio-post-delivery]`, `[ref:delivery-qc]` |
| Genre template or examples | `[skill:seedance-recipes]`, `[ref:examples-by-mode]`, `[ref:genre-guides]` |
| Chinese examples or safe Chinese rewrites | `[skill:seedance-examples-zh]`, `[skill:seedance-vocab-zh]`, `[ref:vocab/zh]` |
| Japanese examples or safe Japanese rewrites | `[skill:seedance-examples-ja]`, `[skill:seedance-vocab-ja]`, `[ref:vocab/ja]` |
| Korean examples or safe Korean rewrites | `[skill:seedance-examples-ko]`, `[skill:seedance-vocab-ko]`, `[ref:vocab/ko]` |
| Russian/Spanish or mixed-language examples | `[skill:seedance-vocab-ru]`, `[skill:seedance-vocab-es]`, `[ref:multilingual-community-examples]` |
| Slop-heavy or filter-tripping English wording | `[skill:seedance-vocab-en]`, `[skill:seedance-antislop]` |
| Bad result | `[skill:seedance-troubleshoot]` |
| A take came back: keep, fix in post, edit, re-roll, or rewrite | `[ref:retake-protocol]` |
| Why a rule works, or a novel case no rule covers | `[ref:model-mechanics]` |

Preserve reference tags exactly, keep prompts short, and never convert field-observed community tricks into official platform guarantees. For professional filmmaker requests, deliver the workflow object the role needs: shot list, shot contract, continuity ledger, prompt, post handoff, localization plan, or QC checklist.
