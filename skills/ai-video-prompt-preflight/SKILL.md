---
name: ai-video-prompt-preflight
description: "完整档终检：打斗、VFX、变身、困难连续性与参考、依赖研究的制作、商业交付、成片重试。仅在调用方给定 full 档或用户明确要求穷尽式提示词质检时使用。只返回字段补丁，绝不写第二份完整提示词。 Full-depth final validator for fights, VFX, transformations, difficult continuity/reference work, research-dependent production, commercial delivery, or generated-output retries. Use when the received processing depth is full, or when the user explicitly requests exhaustive prompt QA. Do not invoke on fast or standard camera-group routes; use their lightweight preflight owners instead. Validate and return field patches, never author a second full prompt."
---
# Portable Profile Note

When installed from `director-workflow-portable-70`, route through `$director-workflow-70` and use only bundled skills. Missing private-memory, automation, tool-control, or archive handoffs are optional and must not block prompt work.


# AI Video Prompt Preflight

For Liu's真人短剧 Seedance workflow, apply the project audio and duration
contract before generic checks: camera groups are 14-28 seconds and never over
30; copy-ready prompts default to character dialogue/voice-over and
source-coupled dry foley/SFX. Music, score, ambience beds, and mood effects are
valid only when Liu or the authoritative script explicitly requires them.

Read `../director-workflow-70/references/liu-short-drama-contract.md` as the canonical contract before preflight. If another reference conflicts on duration, audio, dialogue speed, framing, @handles, or complete-prompt delivery, flag the conflict and follow the contract.

Read `../director-workflow-70/references/orchestration-contract.md` as the
shared state and ownership contract. Preflight validates the merged route; it
does not create a second routing schema or assign a competing final owner.

For Liu's complete-script or connected multi-shot workflow, verify the upstream
`../director-workflow-70/references/short-drama-director-stack.md` gate:
reference sufficiency was reported, three concepts were offered or a
direct-execution override was explicit, and one owner was assigned per control
surface. For a local fragment, require only the scoped asset/capacity/continuity
check and selected compiler before local shot planning, but still require the
same shot-table plus detailed six-part package for every resulting local camera
group. Preflight validates the approved result; it does not choose a new concept
or silently fill a P0 reference gap.

## Review Boundary

The `ExecutionPlan.review_budget` is authoritative. The director and specialists
have already completed planning and domain checks; this skill owns the single
full-depth final QA pass. Do not rerun standard planning, camera, continuity,
audio, or packaging reviews unless the route receipt shows that the assigned
owner did not run them or a full-risk finding invalidates their evidence.

Apply `think-one-step-further` only as a delta check for the next likely full-
risk failure and for handoff usability. Do not repeat its general correctness,
transfer, aftercare, or failure-forecast checklist when no new risk is present.

## Purpose

Use this skill as the final gate before generation. It catches contradictions, overloaded shots, missing locks, unclear reference roles, impossible timing, model-risk language, and likely drift before the user spends attempts.

Use it after structure, story, audiovisual grammar, continuity, art direction/aesthetic direction, action, rhythm, material/render realism, and model packaging.

Run only when the `ExecutionPlan` selects `full`, or for an explicit exhaustive
diagnosis. Fast and standard routes have separate preflight owners. Validate the
single compiled prompt and return findings or named field patches; do not create
a second prompt version.

## Reference Routing

Read only the file needed for the task:

- `references/preflight-checklist.md`: use for full-depth final prompt checks.
- `references/feasibility-and-splitting.md`: use for 10s+ videos, complex action, multi-shot sequences, transformations, or prompt overload.
- `references/failure-risk-matrix.md`: use to diagnose what is likely to fail and what to simplify.
- `references/retry-control.md`: use when preparing controlled next-round adjustments.
- `../narrative-camera-groups/scripts/shot_group_linter.py`: run when a structured JSON shot plan is available; use its output as deterministic evidence for timing, fields, handles, and audio compliance.
- Use `--strict` only for a final delivery gate; during ideation, keep soft-budget and proof-task findings as warnings so justified one-takes or intentionally sparse groups remain possible.

## Workflow

0. Verify the backstage Route Receipt from `$director-workflow-70`.
   - It must state the task class, applicable mandatory layers, conditional triggers, one owner per active control surface, exact current Skill/reference files actually read, skipped conditional layers with reasons, and route status.
   - Independently compare it with `../director-workflow-70/references/mandatory-stack.md`; do not accept the receipt merely because it says `complete`.
   - A skill name, description, or route-plan mention is not proof that its current instructions were read.
   - If the receipt is absent but the task, owners, and applicable layers are otherwise unambiguous, build a minimal internal receipt and continue. Stop and repair the route only when an active surface has no owner or competing owners, a selected owner was not actually read, or a conditional trigger disappeared without a reason.
   - Verify that `delivery_contract` is selected before timing and that the
     required state chain is present for the output mode: `StoryContract`,
     `ContinuityContract`, `InformationLedger`, `SpaceContract`, `ShotLedger`,
     and, for camera-group delivery, `CameraGroupPlan`.
1. Identify the target model and generation mode if known.
   - For SD2 / Seedance-style workflows, classify the mode before approving the prompt: pure text, image-to-video, first/last frame, all-material/all-reference, multi-segment stitching, or prompt diagnosis.
   - If the user asks for directly copyable output, verify that each generation unit has one standalone `完整可复制提示词` code block. A single clip has one block; a narrative camera-group package has one complete block per group. Put only model-ready prompt text inside each block, with that group's positive stability locks included; keep planning tables, generation mode, asset inventory, and preflight notes outside.

    - In Liu's workflow, verify reference files supplied alongside the script use the exact name-based `@图片名`、`@视频名`、`@音频名` handles with a scoped role on first mention. `{{Image N}}`等编号只作后台映射，不作为最终提示词主引用；reject invented or generic names, unless the user explicitly supplied that exact asset name.
    - Distinguish platform character handles from file handles: when the user supplied five-view assets for the cast, `@角色名` (for example `@苏凌月`, `@苏建国`, `@刘大龙`, `@黑衣小弟甲`) is required for every distinct character mention inside the copy-ready prompt; named reference files use `@图片名`、`@视频名`、`@音频名` and are not converted into character handles.
    - If `@视频名` is a whitebox / Blender previs / mocap reference, verify its role is motion/camera only: action rhythm, body weight, shot scale, camera distance, cut logic, and transition triggers. It must not control final character design, material, scene, grid floor, capsule body, labels, or preview render style.
   - For Liu's 15-second素材段 workflow, verify that the prompt has one main segment objective and 3-4 required state changes. If it tries to include a complete storyboard, multiple action chapters, transformation, fight, climax, and ending in one clip, mark it overloaded and reduce or split it.
   - Require `TaskEnvelope.output_format = six_part` for every script-derived
     unit. A local fragment or single continuation beat uses scoped local
     planning, but it still requires a local shot table and a detailed six-part
     prompt per camera group. If several action chapters, transformation, fight,
     climax, and ending compete inside one short segment, mark it overloaded and
     split at a natural boundary.
   - The legacy 15-second素材段 calibration is advisory only and never
     overrides the inferred complete-script versus local-fragment route.
   - Run a prompt-budget check before approving: Liu allows substantial copyable prompts up to roughly 3000 Chinese characters by default, so do not force arbitrary shortness. Preserve one primary fidelity spend, one secondary spend, one compact visual/material master, one compact camera master, minimum world identity, coverage-critical cuts, and event beats that add temporal change. If later beats repeat the masters or specialist layers read like pasted independent paragraphs, compress repetition rather than removing necessary control layers.
2. Check reference roles:
   - identity, outfit, prop, vehicle, environment, style, pose, lighting.
   - Before inventing any new plot-critical prop, search the current project brief, continuity bible, asset registry, and prior prompts for an established object that already performs the same narrative function. Reuse the established object when its function overlaps; a new prop is allowed only when it adds a clearly distinct function and does not dilute the existing motif.
3. Check asset readiness:
   - what already exists, what is required, what is optional, what must be generated first, and whether every asset has one clear control role.
4. Check research readiness for substantive prompts:
   - supplied/local truth was inspected; unresolved domain/reference/platform questions were researched; current model claims use official sources.
   - if the user supplied reference videos/links or asked for 拉片/整个都看, the reference was inspected or clearly access-limited, classified by whole-work grammar, and translated into prompt mechanisms before final wording.
   - if the prompt responds to repeated action, camera, or aesthetic failure, confirm that the next attempt is evidence-backed by output review, reference breakdown, or explicit user-provided successful examples rather than another intuition-only rewrite.
5. Check structure and full-risk deltas:
   - hook, build, turn, payoff; no repeated beat doing the same job. Treat
     standard route evidence as accepted and inspect only full-risk additions:
     complex action/VFX lifecycle, cross-scene or cross-episode continuity,
     research freshness, reference conflicts, retry evidence, and commercial
     delivery constraints.
    - distinguish the internal planning map from the literal generation prompt. When `$narrative-camera-groups` is active, require the human table to stay outside the prompt while every prompt shot restates its audited time window, duration, shot size, camera setup/movement, visible action/dialogue, and handoff in prose.
    - for film-level Liu boards, require each major shot to state camera position/height/angle, focal-length or lens perspective, aperture/depth-of-field and focus subject, plus light source/direction/quality/color temperature/shadow behavior. Reject a bare list of lens numbers or "电影级布光" without a visible proof task.
    - for action-led clips, verify the first second is not wasted on a default static lineup, face-off, mutual stare, or slow preparation unless that standoff is the explicit hook.
    - for Liu's 14-28 second camera groups, compare shot count and complexity with the soft coverage budget: dialogue 4-8, emotion 3-6, action 5-10, hybrid 5-9 as review ranges, not fixed quotas. Flag unresolved overload when several shots repeat the same information, multiple major events share one shot, or dialogue/action lacks breath, reaction, contact, or recovery time. Treat `CameraGroupPlan` as a planning unit and `GenerationSegmentPlan` as a platform unit; verify their mapping is 1:1 unless a model-limit or complexity reason is recorded.
    - run a readability triad on every major shot: subject/relationship is identifiable, action or dialogue target is readable, and the changed state or next question is visible. If one fails, widen/reframe, simplify, add a motivated reaction/insert, or split the shot.
6. Check temporal/emotional logic when relevant:
   - emotional or behavioral turns have a cause: past residue, present action, incoming pressure, and final consequence.
   - run an ontology/agency check for every nonhuman or constructed entity: sentient being, instinctive creature, possessed body, memory echo, illusion, automated defense, or environmental mechanism. Its behavior, facial response, hesitation, sacrifice, protection, and tactical choice must stay within that declared agency model.
7. Check audiovisual grammar:
   - each visual beat has a shot function, shot size, camera position/angle, spatial path, axis or screen direction, continuity bridge, and reason to cut.
   - each emphasized transition has an outgoing source and an inherited incoming element—action, vector, shape, occlusion, material, light, or sound—and does not conceal required contact or consequence.
   - any effect/foreground wipe covers the subject only briefly; the incoming image immediately restores subject count, axis, geography, and the changed physical state.
   - when the prompt requests special storyboard expression, verify that multiple shots, scales, and special angles form one continuous action phrase; adjacent shots contrast in viewpoint but inherit action vector, phase, eye trace, axis, and geography.
   - verify action-camera coupling: performer pose/path motivates the camera, and camera behavior reveals or amplifies a real movement feature rather than manufacturing empty energy.
8. Check shot feasibility:
   - one main action per short shot, one main camera move per shot, clear timing.
   - verify duration at four levels: total clip duration, segment allocation, structural peak placement, and action-phase feasibility.
   - identify timing evidence: reviewed reference/output, animatic/edit map, external synchronization, or physical action budget.
   - assign timing confidence: high / medium / low.
   - if segment ranges are high-confidence, preserve them; if not, soften or remove them.
   - verify exact ranges sum to the requested duration, contain no accidental gaps/overlaps, and do not hold simple content too long or compress complex action below its physical needs.
   - distinguish segment ranges from individual shot durations. For the user-calibrated narrative-camera-group workflow, exact shot durations are required; verify that they are plausible and sum cleanly instead of removing them.
   - verify the density curve: longer orientation, compressed escalation, brief peak, readable consequence. Reject equal-duration slicing unless synchronization or evidence requires it.
   - for a large morphology change, evaluate source/target reference collision. When start-state and distant end-state references compete for identity or anatomy control, split the bridge: one clip keeps the source form stable and ends on the activation trigger; the following clip begins from an approved target-state asset or a separately controlled reveal.
9. Check action physics when relevant:
   - before style names or special moves, verify the foundation: support, center path, distance/angle, setup, contact or near miss, reaction cost, braking/recovery, and changed end state;
   - each principal performer retains a primary named movement/martial basis when one is selected, with only the visible mechanics needed for differentiation, adaptation, or physical credibility;
   - event verbs inherit a recurring stance, body level, path geometry, support pattern, rhythm, and recovery signature;
   - actor strength relative to body/weapon/vehicle load;
   - center of mass and base/support path;
   - weapon length, grip, and mass distribution;
   - force chain and traction;
   - contact response, recoil, follow-through, braking, and stable end state.
   - for each principal hit, verify complete hit acknowledgment: structural force transfer, visible receiver performance/physiology when the face is readable, and synchronized contact/breath/foot/environment sound when audio is part of the output. Body deformation alone is not sufficient.
   - verify impact grading: reserve full facial, physiological, structural, and sonic acknowledgment for one to three hero hits; keep minor contacts compressed so the fight remains fast.
   - for multiple action peaks, compare trajectory plane, weapon end/function, support state, body level, travel vector, braking method, and end guard; reject cosmetic variation around one repeated loop.
   - for tip-heavy/head-heavy weapons, every change of plane has a visible brake/catch and regrip or new guard. “Continuous momentum” must not override legal redirection.
   - for complex exchanges, assign camera tracking ownership: initiator during commitment, contact plane at impact, receiver or redirected path after force transfer.
   - for transformation, require a readable frontier with old state, active boundary, and completed new state; assign distinct exit/reveal/assembly behavior to each material.
10. Check continuity:
   - face, costume, prop, vehicle, world, color, lighting, direction, form state.
   - if body-proportion locks are used, verify they are appropriate for an adult character and do not conflict with age, identity, costume, action credibility, or safety boundaries.
11. Check aesthetic direction:
   - medium domain, style family, relevant industry control vocabulary, rendering hierarchy, color ownership, line/shape/texture logic, and forbidden style drift.
   - verify that a global visual master appears before detailed shot instructions and remains authoritative across all shots.
   - for high-energy action, verify that the master defines a limited camera family, shot-scale range, permitted animation exaggeration, physics contract, spatial locks, and targeted anti-chaos constraints.
   - verify that user-provided anchors were treated as backstage mechanism references by default and translated into concrete visual/camera behavior. Include a name in the paste-ready prompt only when the user explicitly requests named references and the platform/safety contract permits it.
   - when named director, studio, manga, game, martial-art, or cinematography anchors are explicitly requested, give each one a distinct function such as shot geometry, impact pose, montage rhythm, material style, or action logic. Avoid name salad and preserve the user's useful names.
   - when the prompt is substantial, verify that `$creative-anchor-director` or an equivalent audit considered all relevant—not all possible—style, world, camera, animation/editing, movement/weapon/partner, and audio lanes.
12. Check music and sound when relevant:
   - dramatic function, cue in/out, sound focus, dialogue priority, ambience, foley/effects, music or silence, selective sync points, and audio assets.
13. Check material/light/render completeness:
   - visible materials, key/rim/bounce light direction, AO/contact shadows, PBR roughness/specular/metallic behavior when useful, anisotropic highlights when relevant, reflection/texture response, optical behavior, fake-look avoidance, and motion blur readability when relevant.
14. Check contradictions:
   - camera, style, lighting, weather, time, movement, prompt-negative conflict.
15. Check risk:
   - what is most likely to break, what evidence supports that risk, and whether it comes from the prompt/workflow, missing assets, or a verified model limitation.
   - whether specialist layers are organically linked: structure, reference continuity, audiovisual grammar, aesthetic anchors, action/rhythm, material/render, and platform packaging must serve the same event. If they read as independent pasted blocks or compete for control, rewrite before generation.
16. Return either:
   - pass with minor notes, or a simplified safer prompt.
17. Only when an actual generation will be submitted, hand the final prompt,
reference-role map, model/mode, settings, and expected deliverable to
`$creative-production-ledger` as one attempt. Prompt drafting alone does not
create a ledger attempt.

## Severity And Repair Protocol

Classify every finding before returning the report:

```text
P0 hard block: stop delivery and name the responsible owner plus repair action.
P1 required revision: apply the named patch before delivery.
P2 advisory: preserve the route and record the optional improvement.
```

Use stable rule IDs when possible:

```text
ROUTE-001  missing owner or incomplete RouteReceipt
STATE-001  required state object missing
TIME-001   group/shot timing outside the selected contract
SPACE-001  axis, position, path, or handoff conflict
REF-001    missing or ambiguous plot-critical reference role
PROMPT-001 non-standalone generation unit or mixed planning text
AUDIO-001  audio contract violation
PATCH-001  specialist returned a competing full draft instead of a named patch
```

Every finding must include `owner`, `evidence`, and `repair_action`. Preflight
may block delivery or request a patch, but it may not silently redesign the
concept, rewrite dialogue, or choose new camera-group boundaries.

## Hard-Fail Checks

- The backstage Route Receipt is absent or still marked `incomplete` for a substantial film/AI-video task.
- `delivery_contract` is absent, or the group/segment duration conflicts with the selected contract.
- A required state object is absent from the merged route for the requested output mode.
- For a new Liu complete-script/connected-sequence request, the
  reference-sufficiency report and three-concept/direct-execution gate are
  missing, or a P0 reference gap is hidden inside a confident final prompt. A
  local-fragment route is exempt from the three-concept gate but not from its
  scoped P0 evidence check.
- A plot/script-to-AI-video task has no single final delivery owner. Use `$narrative-camera-groups` for grouping and visible packaging, `$professional-storyboard-director` for shot design, and the platform compiler only for wording inside each group prompt.
- The receipt omits an applicable layer required by `../director-workflow-70/references/mandatory-stack.md`, or lists a final owner whose current `SKILL.md` / authoritative reference was not actually read.
- An active control surface—structure, continuity, performance, action, camera, style, material, VFX, sound, platform packaging, or review—has no owner or competing owners.
- A specialist returns a conflicting full draft or silently changes a field outside its declared ownership instead of submitting a named patch.
- A visible conditional trigger such as action, VFX, transformation, continuity, sound, output review, or platform-specific packaging is neither routed nor explicitly skipped with a concrete reason.
- Final prompt drafting or packaging began before the route became complete.

Mark the prompt as "needs revision" if any of these appear:

- A substantial camera-sensitive prompt lacks compact concrete camera grammar;
  named anchors are not required by default. For `视觉材质总控`, mark revision
  when concrete material/light/render controls are missing. When the user
  explicitly requests named references, verify each permitted anchor is paired
  with a concrete visible result.
- The final copyable prompt contains exclusion, absence, correction, old-failure, or comparison wording inside the paste-ready block. Rewrite those lines as current positive visible/audible facts before delivery.
- The final copyable prompt uses any legacy exclusion slot instead of `正向稳定约束`. Rewrite the final section as positive subject/camera/material/action stability locks.
- Any script-derived camera-group prompt, including one built from a local fragment, does not follow Liu's fixed six-part order: `角色/资产锁定 -> 视觉材质总控 -> 镜头语言总控 -> 事件节拍 -> 声音 -> 正向稳定约束`.
- Any of the six sections is empty, generic filler, or too abbreviated to control the current group.
- `事件节拍` fails to restate every shot with shot number, timecode/duration, shot size, camera position/height/angle, focal length or perspective, depth of field/focus, lighting direction/quality/color temperature/shadows, camera movement/path, action/performance, verbatim authoritative dialogue, cut trigger, ending state, and handoff.
- A group prompt uses `同上`, `沿用`, `参考镜头表`, `保持不变`, or equivalent cross-reference wording instead of complete standalone detail.
- A shot window has no nested `T=起始-结束s` micro-beats, or its T ranges have gaps, overlaps, fall outside the shot window, or contain multiple unbounded actions that cannot be timed.
- `事件节拍` merges two or more shots into one unlabeled paragraph instead of
  using an explicit `镜头01`/`镜头02` block with nested T lines for each shot.
- Any concrete prompt element fails source tracing: it comes from an old project, old template, previous failure, default scene grammar, or assistant habit rather than the current instruction, supplied asset/reference, active global bible/continuity lock, or user-approved reusable rule. This includes positive stability locks; old-context nouns in any paste-target clause are still contamination.
- The prompt imports a familiar/default template from a previous task—scene type, floor, staging, transformation room, opening routine, transition, or display grammar—that was not requested and that competes with the current explicit scene, movement path, active character state, or final handoff state. Treat this as template contamination / priority failure, not as a local wording issue.
- Reference roles are missing or ambiguous, especially in multi-reference / 全能参考 mode.
- Liu's paste-ready prompt uses invented/generic reference names, bare `{{Image N}}`编号 in place of the user's exact `@图片名`, or pseudo-layer tags.
- When named platform character assets are supplied, a copy-ready prompt uses bare character names where `@角色名` is required, or inconsistently mixes bare names and `@角色名`; rewrite all model-facing character mentions to the exact user-supplied `@` handles. For named reference files, preserve the exact `@图片名`/`@视频名`/`@音频名` handles.
- A supplied reference is called `参考图1`, `图1`, `第一张图`, bare `image1`, or similar generic prose instead of the exact user-supplied `@图片名`/`@视频名`/`@音频名`. On first mention, require the exact @name plus a parenthesized role scope, e.g. `@废墟夜景.png（场景布局与光线参考）`.
- A whitebox, Blender previs, or mocap reference video is allowed to control final character appearance, material, scene design, grid floor, capsule-body look, labels, or preview-render lighting instead of being limited to motion/camera/edit evidence.
- The target generation mode is ambiguous even though the prompt depends on mode-specific behavior such as first/last frame, all-reference, multi-segment stitching, or image-to-video preservation.
- The user asked for complete copyable prompts, but a generation unit lacks its own standalone code block, positive stability locks are outside that block, planning/preflight notes or a Markdown shot table are mixed into the paste target, or a camera-group prompt refers to another group or to the table instead of remaining self-contained.
- The paste-ready prompt contains agent-only self-check language, workflow explanations, internal production notes, nonexistent reference placeholders, excessive unassigned director/studio anchors, or generic exclusion spam instead of generation-facing scene controls.
- The prompt depends on an identity, vehicle/prop, environment, first/last frame, or layout reference that is not available, while still being presented as ready to generate.
- A prompt applies adult body-proportion language such as hourglass figure, waist-hip ratio, lifted hips, or mature chest line to a minor, childlike, school-age, or ambiguous-age character.
- A substantial new prompt claims professional, historical, cultural, physical, musical, or current model accuracy without inspecting supplied truth or researching the unresolved knowledge gap.
- A prompt claims to follow a supplied reference video, external link, or the user's previous successful work, but that reference has not been inspected, role-classified, or access-limited honestly.
- The user asked to "整个都看" or "拉片", but the new prompt only cherry-picks current-project fragments without first considering the reference's whole aesthetic, camera, action, editing, effects, sound, and prompt grammar.
- A repeated action/camera/style failure gets another long prompt patch based mainly on adjectives or intuition, without output evidence, reference research, or a narrowed controlled variable.
- A newly discussed or newly learned camera, rhythm, transition, VFX, or slow-motion device leaks into the next prompt without a current-shot source trace, explicit user request, or indispensable visible function.
- A VFX beat has no indispensable information job and exists only as generic spectacle: detached particles, glow, rings, fog, trails, sparks, or camera shake with no force/state/ownership meaning.
- An important effect does not define a visible source/owner, primary shape/read, path or spatial layer, contact/collision, receiver/environment change, and decay/residue. Minor effects may compress phases; hero effects may not skip causality.
- The prompt never selects a medium-aware motion-effect family, or uses the same generic motion blur/glow/particles for photoreal CG, stylized 2.5D/NPR, and pure 2D.
- VFX hides the contact point, weapon/body relationship, receiver acknowledgment, or action geography that it is supposed to strengthen.
- Every contact is graded as a hero effect, so impact frames, hitstop, shake, exposure changes, debris, and large shockwaves have no escalation hierarchy.
- An emissive effect does not illuminate or occlude nearby surfaces according to distance, direction, color, and scene depth, making it read as a pasted overlay.
- Destruction is not material-specific, debris appears before impact or from untouched surfaces, or fragments ignore local velocity, collision, gravity, and settling.
- A weapon/body smear persists as a new design, changes grip/handle count/striking side, or remains wrong immediately before and after the presentation deformation.
- The final prompt adds a detached generic VFX block instead of integrating effect medium/light into `视觉材质总控`, camera coupling into `镜头语言总控`, lifecycle into `事件节拍`, and synchronization into `声音`.
- A standalone clip depends on prior history instead of defining the visible first-frame state.
- For Liu's paste-ready video prompts, the first visible state is written as a detached "first-frame state" block instead of being embedded in the opening event beat. Preferred order: reference locks -> global visual/material/light master -> global camera/storyboard master -> event beats, with "开场：第一帧就是..." inside the first event.
- The prompt puts long generic positive stability locks ahead of actual control layers, or uses positive stability locks as a substitute for reference-role clarity, material/light master, camera master, and event-state changes.
- The final prompt is overloaded: it gives several competing elements equal priority, repeats global style/material/camera language inside later beats, or concatenates specialist outputs instead of selecting one primary and one secondary fidelity spend.
- A prompt set in an approved recurring/original world has no environment reference and compresses that world into a generic location label. Require a minimum world-identity packet: world scale/function, palette/light state, 2-4 silhouette or architecture invariants, density/atmosphere state, and one distinctive anomaly/environment signature.
- In I2V/R2V, the prompt redundantly re-describes spatial appearance already carried by an inspected reference image, creating a second competing visual specification instead of spending text on motion, timing, camera path, sound, and endpoint.
- A continuation prompt tries to hard-match the previous generated final frame instead of carrying only the story state and hiding inevitable visual drift with a different shot size, angle, insert, occlusion, foreground wipe, smoke/dust/sound bridge, impact bridge, or chosen reference transition.
- A continuation prompt opens with a shot that visually contradicts the previous segment, replays the previous ending, resets character/creature form state, or re-reveals an event that already happened, such as a monster that was already revealed emerging from smoke again.
- A paste-ready continuation prompt contains internal production/meta language such as "do not hard-match the previous final frame", "avoid mismatch", "do not replicate the previous composition", or "carry story state not exact frame". Rewrite those as concrete filmable shots: insert, angle change, occlusion, foreground wipe, smoke/dust/sound bridge, impact bridge, and visible current state.
- A paste-ready prompt contains conversation-dependent wording that a stateless generator cannot use cleanly, such as "延续前面片子", "上一段", "之前", "现在这个", "已经脱离", "不要像上次", or "本段". Rewrite them as direct visible scene/style/action facts and keep only targeted negatives for likely on-screen failures.
- An action-led short clip opens with characters standing still, facing off, posing, or slowly preparing without a clear ritual/standoff purpose, wasting the hook before any pressure, consequence, or near-contact appears.
- An emotion-driven prompt commands a naked transition such as "from happy to broken" without a temporal hinge or visible cues: past residue, present action, incoming pressure, and final consequence.
- A one-scene prompt has no fixed blocking: no stable left/right/foreground/background relationship for character, vehicle, prop, and main set piece.
- A fight prompt lists attacks but does not define starting distance or formation, defender responses, receiver displacement, or the changed state after each exchange.
- An action prompt relies on martial-art, weapon, director, studio, or VFX names while the basics are missing: support, center of mass path, distance/angle, contact/near miss, reaction, braking, recovery, or changed state.
- An action prompt lists only task verbs such as run, jump, climb, attack, block, and slash, but defines no movement/martial basis or recurring visible action grammar.
- A heavy, long, head-loaded, flexible, transformed, or superhuman weapon action has no actor-relative load, support, mass distribution, follow-through, braking, or recovery.
- A character's center of mass visibly leaves the support area without a step, slide, fall, brace, cable, wall, vehicle, powered assist, or airborne phase.
- A motion depends on support, grip, body contact, seat, tether, hinge, rail, landing surface, or another constraint, but the related bodies/props are described as independent animation layers with no load transfer, relative-motion limit, shared response, or release/new-constraint state.
- A full-body terrestrial walk, run, pursuit, stair/slope/rubble traversal, landing, stop, or turn is a primary proof task but the prompt treats locomotion as body translation: no support phase, center-of-mass transfer, push-off/braking, terrain adaptation, or contact response.
- A follow camera and a walking/running subject move with unrelated speed or parallax, producing background drift or foot sliding; or the prompt overcorrects by mechanically locking the camera to every footstep with no inertial lag.
- Long garments, coats, hair, straps, or hanging props intersect the legs/body or float independently because the prompt supplies no delayed drag, collision/clearance, overshoot, and settling relation when that interaction is visible.
- Render/solver terms such as RTAO, IK, collision mesh, PBR cloth, or velocity matching are used as executable magic words rather than being attached to a visible contact point, motion phase, surface response, or camera result.
- Contact is represented only by sparks, particles, camera shake, or sound while bodies, weapons, stance, and spacing do not respond.
- A principal hit produces body squash or silhouette deformation but the receiver keeps an unchanged expression, uninterrupted gaze/guard/breath, and no synchronized human or environmental sound; this reads as rubber deformation rather than a confirmed hit.
- A transformed weapon changes size or mass distribution but keeps the same grip, stance, acceleration, stopping distance, and recovery.
- A group-fight prompt asks all participants to attack simultaneously without relay order, foreground/midground/background ownership, or a funnel/triangle formation.
- A mounted, vehicle, animal, or giant-creature action merges carrier/body motion with the attack and provides no support, traction, gait, suspension, or environmental force response.
- A 10-15s prompt has only 2-3 repeated actions with no turn, new information, displacement, or payoff.
- Several segments use different names but repeat the same circular topology through footwork, blade path, body turn, camera orbit, and effects.
- A heavy weapon is required to preserve uninterrupted momentum while changing from horizontal sweep to vertical wheel or reverse direction without a brake, catch, plant, regrip, or new guard.
- Detailed shot instructions appear before any coherent global visual master, allowing later camera/action language to define an inconsistent default look.
- A substantial AI-video prompt has action, event, creature, vehicle, PV, transformation, or material beats but omits the global camera / shot-style master near the beginning. If Liu asks for 镜头、分镜、运镜、张力, or has recently corrected that camera style was forgotten, the prompt must state the camera family, named anchors with functions, special storyboard language, shot-scale range, transition logic, and proof jobs before timed beats. Generic "dynamic camera" is not enough.
- `镜头语言总控` omits the complete whole-film camera identity: compatible style anchors, perspective system, lens family, distortion, movement energy, framing/edit rhythm, transition language, or reveal logic.
- Normal `事件节拍` lines repeat the camera-master style names, lens vocabulary, or routine movement contract instead of inheriting it. Local camera wording belongs only to a genuine special-camera beat and must state its action/impact/occlusion trigger plus concrete visible result; vague, unmotivated, or master-conflicting local camera clauses fail.
- The camera master promises inserts, close-ups, multi-cut coverage, or a wide spatial proof, but no event beat explicitly instantiates the required cut. When coverage is indispensable, require a concise local `cut trigger -> changed scale/height/angle/lens relation -> proof task -> continuity handoff`; master-only wording such as `穿插特写`, `多景别`, or `快速切镜` does not pass.
- The global visual master is a long name/adjective dump with no stable medium, palette ownership, material-light system, or rendering hierarchy.
- A high-energy visual master says “free camera,” “unconventional,” “POV,” “many cuts,” or “extreme motion” without bounding the permitted moves or preserving axis, screen direction, target relation, geography, anatomy, and action causality.
- Named style anchors are listed without functional roles, conflict with each other, or are being used as a substitute for action causality and shot grammar.
- The prompt relies only on the few names the user happened to know even though camera, movement, weapon, partner, or sound identity remains generic and a well-matched anchor could compress the missing direction.
- Project-specific anchors from a previous job are reused as defaults despite a different genre, medium, movement system, or emotional goal.
- A multi-reference or SD2 all-reference prompt uses a whole long video/image set without role labels, time ranges, trim strategy, or "do not copy" boundaries, especially when only camera/action/style should be transferred.
- Exact shot timecodes are used without a timing audit, do not sum cleanly to total duration, create gaps/overlaps, stretch a simple gesture into an idle hold, or compress preload/action/reaction/recovery into an implausible interval.
- A Liu camera group exceeds the soft shot-count range without a clear script-based reason, or combines dialogue, reaction, effects, and complex blocking beyond the available motion and attention budget.
- Exact segment ranges are presented with no evidence, timing rationale, physical budget, or prior result supporting that precision.
- A 10-15 second action prompt mechanically divides the runtime into equal action nodes despite uncertain topology, continuity, or model capacity.
- High-confidence segment timing is unnecessarily removed even though a reviewed reference, successful output, animatic, or edit map provides a reliable duration template.
- Adjacent beats repeat the same shot size, camera height, camera path, and action verb.
- When camera variety is a requested or evidence-backed risk, the prompt must contain a compact coverage phase map rather than only lens numbers, director names, or “multi-cut” language. Geography may lock axis and direction, but camera position, height, scale, path, tracking owner, and proof task must still vary deliberately; adjacent major phases should change at least two visible camera attributes.
- When Liu asks for action frames that are not level or orthogonal, verify the camera coordinate system as a separate layer: horizon/architecture/body/weapon lines should form action-motivated oblique compositions, and camera roll/pitch/yaw should inherit force vectors rather than become random repeated Dutch angles. Stable geography must not be mistaken for gravity-locked camera-up.
- “Multi-shot, multi-scale, special angles” produces disconnected coverage, repeated hero poses, or random camera teleportation rather than a continuous action phrase.
- The prompt calls for extreme character action and extreme camera motion independently, so neither has a readable causal relationship.
- A prompt has rich style/material/texture language but no clear audiovisual scaffold: no shot function, shot size, spatial path, axis/screen direction, continuity bridge, or cut reason.
- Camera instructions conflict: locked-off plus handheld plus orbit plus crash zoom in the same short beat.
- Transitions are generic templates—portal, glitch, flash, particles, or whip—without an outgoing source, inherited direction/shape/light/sound, or narrative/spatial job.
- A transition or effect is allowed to hide the performer, weapon, or environment for a sustained interval with no explicit re-entry state.
- A transformation changes the whole subject simultaneously, has no active frontier, or gives no material-specific rule for old surface withdrawal, internal reveal, new surface assembly, and final settling.
- Style says both "flat cartoon" and "realistic cinematic material" without defining a 3D cel-shaded / semi-real hybrid.
- A prompt asks for 风格化/高级感/画风 but has no medium domain, aesthetic family, color ownership, rendering hierarchy, or anti-cheapness constraints.
- A prompt uses industry terms such as editorial, couture, brutalist, letterpress, ergonomic, typographic grid, cinematic, documentary, dashboard, or data visualization as loose labels without visible industry-specific structure or behavior.
- The prompt asks for face close-up, vehicle stunt, city-scale wide shot, and complex transformation in one unsplit beat.
- Positive stability locks are generic spam but do not target the actual risk: face drift, prop drift, vehicle deformation, background morphing, camera chaos, text artifacts.
- A visual prompt has no material/light realism layer: no clear visible materials, light direction, contact shadows, reflection/roughness/texture response, optical behavior, or fake-look avoidance.
- A prompt says only "cinematic", "high quality", "realistic", "8K", or "高级质感" without concrete material and light behavior.
- A prompt uses render terms such as AO, PBR, ray tracing, anisotropic highlights, SSS, GI, or volumetric light as a keyword dump without attaching them to visible surfaces, contact points, materials, or light sources.
- The prompt uses many shot changes in one room/location without saying inserts stay on the same axis and return to the same master position.
- A layout/blocking reference is supplied but its role is not isolated from identity, style, lighting, or material references.
- An abstract color-board/CAD reference is supplied but the prompt does not map colors/shapes to subjects, objects, set pieces, action path, or camera/view hints.
- A diagram reference with labels/arrows/grids is uploaded without saying not to copy the labels, arrows, grid, color blocks, or diagram style into the final video.
- A large or elongated object is controlled only by a point or vague phrase such as "near the character" without footprint, long-axis orientation, front/nose/end direction, and front/back layer.
- A prompt depends on occlusion or staging such as "object in front of subject" or "subject behind object" but does not explicitly lock foreground/midground/background hierarchy.
- A new plot-critical prop duplicates or replaces the narrative function of an established series object without an explicit story reason. Treat this as a continuity hard fail: restore the approved object, its state, and its future payoff before delivery.
- A non-sentient illusion, projection, defense construct, clone shell, or environmental mechanism is given personal affection, fear, hesitation, recognition, sacrifice, or independent choice that contradicts its approved ontology. Rewrite the beat as system priority, trigger-response, inherited memory playback, instinct, external control, or another established causal mechanism.
- A short clip asks one unstable character to obey both a source-body reference and a highly divergent target-body reference while also performing action, camera changes, and environmental destruction, despite prior morphology drift. Remove the target reference from the bridge clip, lock the source body, and stop at a clear activation handoff.
- The task requires audio but supplies only generic phrases such as "epic BGM", "cinematic music", or "strong sound effects" without cue function, timing, sound focus, or silence.
- A Liu short-drama prompt contains background music, score, BGM, ambience beds,
  or tension/emotional/mood effects without an explicit user or authoritative-
  script requirement; remove them and return to dialogue/voice-over plus
  source-coupled dry foley. If music or ambience is authoritative, validate its
  concrete cue function and timing instead of deleting it.
- A Liu camera group is shorter than 14 seconds or longer than 28 seconds without an explicit single-shot/test override; choose a natural duration inside 14-28 seconds or split at a stable handoff.

When a hard fail appears, return the smallest named field patch to the owning
planner or selected compiler. Do not rewrite the prompt inside preflight.

## Output Shape

```text
Preflight：
通过/需修改：
最大风险：
风险依据：
归因类型：提示词/素材/工作流/已验证模型限制/不确定
冲突项：
缺失锁定：
音乐与声音：
建议拆段：
字段补丁：
返回 Owner：
下一轮只调：
```

## Quality Gate

- Is there a complete Route Receipt, independently reconciled against `../director-workflow-70/references/mandatory-stack.md`?
- Were the current instructions of every applicable mandatory layer and final surface owner actually read rather than inferred from names or descriptions?
- Does every active control surface have exactly one owner, and does every skipped conditional layer have a concrete reason?
- Are reference roles explicit?
- Are named reference assets written in Liu's exact `@图片名` / `@视频名` / `@音频名` format rather than invented or generic prose?
- Does each supplied asset's first mention use the exact @name plus a parenthesized role scope, such as `@废墟夜景.png（角色身份与外观参考）`, rather than `参考图1` or `图1`?
- If a reference video is a whitebox/previs/mocap render, is it restricted to motion, body weight, camera distance, shot scale, cut logic, and action rhythm only?
- Is the generation mode explicit and compatible with the available assets?
- If the output is meant to be pasted directly, does every generation unit have its own standalone `完整可复制提示词` code block containing only that unit's model-ready prompt, with positive stability locks included?
- Can the model know the first frame state?
- For action clips, is the first frame already in motion, pressure, aftermath, near-contact, or a purposeful standoff rather than a boring neutral lineup?
- If emotion changes, does the prompt include visible time-state cues rather than only emotion labels?
- Is each time segment visually different?
- Does `镜头语言总控` carry the complete camera style—named aesthetic anchors, perspective, lens family, distortion, movement energy, framing/edit rhythm, transition language, and reveal logic?
- Do ordinary `事件节拍` lines inherit that master without repetition, while only genuine special-camera beats add a motivated trigger + concrete visible result compatible with the master?
- If any insert, close-up, POV, wide proof shot, or scale jump is indispensable, is that cut instantiated in the relevant event beat rather than merely promised by the camera master?
- What is the timing confidence and its evidence? Are exact segment ranges justified, and are total duration, peak location, content density, and physical action timing compatible?
- For ordinary prompts, are micro-shot timings being confused with useful macro-segment timing? For `$narrative-camera-groups`, are the required exact per-shot durations physically plausible, present in the prose prompt, and arithmetically consistent with the group total?
- Does shot density rise and release deliberately instead of remaining uniform?
- Does the global visual master appear before the detailed shot list and control every later beat?
- Is the global visual/material master compact but authoritative, with one compact camera master and no repeated restatement inside later beats?
- Is there one primary fidelity spend and one secondary spend, with the remaining specialist detail deliberately economized?
- Under a character limit, were identity, minimum world identity, event path, coverage-critical cuts, and end state preserved before decorative adjectives, repeated render synonyms, lore, secondary flourishes, and generic stability boilerplate?
- Does the global camera / shot-style master appear before timed beats when the task is action, monster, chase, PV, transformation, or otherwise camera-sensitive? Does it include director/cinematographer/film/studio anchors with clear jobs, and does the visual/material master include material/light/color/render anchors?
- For high-energy action, does the master preserve deliberate style names as compact anchors, avoid excessive name stacking, and add only the camera, composition, material, or physics clarification actually needed?
- If named anchors are used, what is each anchor doing?
- Does each beat have audiovisual grammar before material/style detail?
- If action weight matters, are support, mass distribution, contact response, and inertia resolution explicit?
- For each hero hit, does the receiver acknowledge it through structure, performance/physiology, and synchronized sound without turning every minor contact into a long reaction beat?
- When VFX is active, what information job does each principal effect perform, and which one is the primary read?
- Does each hero effect have an owner/source, formation or anticipation, path/spatial layer, collision, receiver/environment/light response, and decay/residue?
- Is the chosen motion-effect family compatible with the medium: photographic blur, designed smear, pose echo, graphic lines, anchored trail, physical wake, or impact image?
- Is effect intensity graded across minor, medium, and hero beats rather than kept uniformly maximal?
- Does the effect preserve contact, anatomy, weapon identity, geography, exposure, depth occlusion, and nearby light behavior?
- Are destruction, debris, smoke, water, sparks, cloth, and residue driven by the actual material and event rather than a generic particle preset?
- If full-body terrestrial locomotion is visually important, do support phase, center-of-mass transfer, terrain/contact response, camera-relative velocity, and visible secondary motion form one coherent loop rather than five disconnected keyword clauses?
- For each important contact or attachment, what supports or constrains what, where does load travel, what proves the relation, and how does it release or become the next relation?
- Before named style/action anchors, do the basic action mechanics stand on their own?
- Does every principal performer have a visually persistent action grammar, and do multiple performers remain distinct?
- If the prompt is substantial, did research materially inform the result?
- If external or user-made references were supplied, were they classified by scope and role before being used?
- If references are used, what exact role and segment does each reference own?
- If this is a retry after repeated failure, is the change evidence-backed and narrow enough to test?
- Is action readable and not overpacked?
- Does the camera instruction contradict itself?
- Does action-camera tracking ownership follow initiative and force transfer?
- Are style and realism level stable?
- Does the prompt include aesthetic direction when style matters?
- Are industry-specific terms tied to visible objects, layouts, construction details, materials, or motion rather than used as labels?
- Does the prompt include a material/light/render realism layer for every visual scene?
- Are render terms bound to visible surfaces and shot conditions rather than used as loose keywords?
- Are positive stability locks specific, not generic spam?
- Does the same character/weapon keep a stable physical identity across shots?
- For Liu's short-drama mode, are dialogue/voice-over, source-coupled foley,
  silence, and sync points prioritized, with music/ambience/mood effects present
  only when explicitly required by Liu or the authoritative script?
- Is there a controlled retry variable?
- If using a layout board, are object footprints, front/back layers, long-axis orientations, facing/gaze directions, and action paths explicitly mapped?
- Are model-limit claims supported by current documentation or repeated inspected evidence rather than inferred from one overloaded prompt?

## Avoid

- Do not rewrite everything if one variable is the problem.
- Do not add more adjectives when the prompt is already overloaded.
- Do not hide feasibility problems to sound encouraging.
- Do not recommend multi-shot generation as one clip when splitting would clearly be safer.
- Do not label a likely prompt, reference, or workflow failure as a model limitation without evidence.
