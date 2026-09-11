---
name: ai-video-prompt-director
description: "Full director brain used only when script-camera-group-router selects full depth for fights, chases, VFX, transformation, difficult continuity/reference problems, research-dependent design, commercial delivery, or generated-output retries. Ordinary complete scripts use camera-group-director-standard; proven low-risk material uses the fast route. Do not implicitly invoke for script-to-camera-group work."
---
# Portable Profile Note

When installed from `director-workflow-portable-70`, route through `$director-workflow-70` and use only bundled skills. Missing private-memory, automation, tool-control, or archive handoffs are optional and must not block prompt work.


# AI Video Prompt Director

For substantial work, invoke `$ai-video-production-governance` before this
director brain. Governance owns authority, production phase, scope, capacity,
asset readiness, and continuity state; this skill owns directorial intent and
routes the selected specialist stack. Do not maintain a competing project-state
schema here.

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Core Intent

Use this as the top-level orchestration skill for the user's AI video work. It routes a loose idea through the right specialist skills and returns one coherent prompt package.

### Liu Duration Precedence

For Liu's recurring真人短剧 workflow, the canonical camera-group contract is 14-28 seconds, never over 30 seconds. Any older 5-second, 8-10-second, 13-15-second, or 15-second examples in generic references are short-test or non-Liu examples only and must not change the active group duration. The shortest complete group is preferred; split at a natural dramatic handoff when a beat cannot fit.

For Liu's recurring真人短剧导演/剪辑工作, read `../director-workflow-70/references/liu-short-drama-contract.md` and then `../director-workflow-70/references/short-drama-director-stack.md` before routing. The contract is the single source of truth for duration, audio, dialogue, framing, @handles, complete-prompt delivery, and preflight; the stack adds delegation and specialist ownership. It takes precedence over generic defaults where the user has specified a different format.

Liu project defaults: camera groups use 14-28 seconds, never over 30, and choose the shortest complete duration. Ordinary Mandarin dialogue is paced at 2.8-3.2 Chinese characters per second (3 characters per second average); restrained/emotional delivery is 2-3 characters per second. Generated short-drama video defaults to character dialogue, voice-over, and source-coupled dry foley/SFX. Add music, ambience beds, or mood effects only when Liu or the authoritative script explicitly requires them.

For Liu's script-to-camera-group deliveries, every group must be returned as a complete, standalone, copy-ready prompt. Never provide a compact, compressed, abbreviated, or partial prompt, and never omit repeated reference, continuity, camera, audio, or constraint fields between groups.

Do not merge every specialist into every answer. Choose only the useful layers for the current shot.

Default task-card orchestration policy: for Liu's AI-video and creative production tasks, do not jump straight to prompt writing or run every specialist. Use the fixed flow: governance state/authority check -> task-stage diagnosis -> global bible / continuity locks -> director breakdown / shot function -> Task Cards assigned by concrete shot problem -> only-needed specialist work -> specialist result package plus `state_patch_request` -> script-supervisor/orchestrator state arbitration -> platform compiler packaging -> QC -> targeted redispatch on failure -> ledger/case/capsule preservation when useful. Keep Task Cards backstage unless Liu asks to see the production-management view.

For script-to-camera-group work, read
`../director-workflow-70/references/adaptive-depth-routing.md` before specialist
dispatch. Choose processing depth automatically, state it backstage in
`TaskEnvelope`, and never ask Liu to select fast/standard/full. A fast route
uses one fused planning pass and skips untriggered research/specialist layers;
standard is the default; any full-depth trigger upgrades immediately. All
depths preserve the identical visible delivery contract.

### Skill Console Telemetry (Optional, Non-Blocking)

When the local `director_skill_console` MCP is available, emit factual route events at major transitions: director intent selected, a specialist matched/selected/loaded/running, handoff, validation, completion, skip, block, retry, or failure. Include `runId`, `taskId`, `taskTitle`, `skill`, `ownerSurface`, `phase`, `status`, and a concise `message` (plus `reason` for skip/block). The console is observability only: never expose hidden chain-of-thought, never wait on telemetry before continuing, and never infer `running` from a static Skill mention. If the MCP is unavailable, continue the normal workflow and report no fabricated runtime state.

### Liu Short-Drama Gate

Classify the source scope before showing a gate. Preserve the user's authority
and keep planning separate from model-facing compilation:

1. `complete_script_or_multi_shot_sequence`: inspect every supplied reference,
   map its role, identify missing P0/P1/P2 evidence, and explain the impact;
   establish the global story/information breakdown, then present three coherent
   shot/group concepts with one `导演推荐` when the route is still open. A P0
   gap blocks a confident formal breakdown but may still yield a labelled
   provisional plan.
2. `local_fragment_or_single_continuation_beat`: inspect only the current
   fragment's state, capacity, continuity and required assets. Build one or
   more local camera groups, each with a local shot table and the same detailed
   six-part prompt contract as a complete-script group. Do not force the
   full-scene concept gate or a global whole-script breakdown.
3. Wait for a concept choice only when the complete-script route is genuinely
   ambiguous. `直接生成 / 按推荐 / 不要问` and an already locked route are
   valid direct-execution overrides. A clear fragment request proceeds after
   the local feasibility check.

If the user asks for a diagnosis or skill audit rather than a scene, explain the gate and stack without pretending to run a scene breakdown.

### One-Brain / Multi-Leader Protocol

The director brain owns intent, routing, arbitration, group boundaries, concept recommendation, and final feedback. Dispatch only the leaders needed for the current scene:

- story/rhythm leader: `$video-structure-design`, `$screenwriting-story-craft`, `$shot-information-progression`;
- reference/continuity leader: `$character-continuity-bible`, `$entity-continuity-system` when a durable registry is needed;
- world/aesthetic/material leader: `$production-design-worldbuilding`, one style owner, `$ai-material-realism`;
- camera/storyboard leader: `$cinematic-audiovisual-language`, `$professional-storyboard-director`, `$narrative-camera-groups`;
- action/VFX leader: `$action-choreography-reference`, `$action-rhythm-editing`, `$seedance-fight-director`, `$cinematic-vfx-director` and its compilers when triggered;
- performance/sound leader: `$performance-scene-director`, `$relationship-dialogue-direction`, `$cinematic-music-sound-design` in foley-only mode; `$seedance-audio` only for an explicitly approved dry foley timing test;
- platform/QC leader: exactly one platform compiler and the matching preflight
  profile already named by `ExecutionPlan`.

Each leader returns only `objective`, `inputs`, `decisions`, `state_patch_request`, and `uncertainty`. Resolve conflicts in this order: explicit user instruction -> inspected references -> accepted continuity -> story/dialogue -> physical feasibility -> camera/aesthetic -> platform syntax -> decoration. No leader may write a competing full prompt or silently override another owner.

### Control-Surface Arbitration

Assign one final owner to each surface before drafting: structure/group boundaries=`$video-structure-design` plus `$narrative-camera-groups`; shot grammar=`$cinematic-audiovisual-language`; visible shot plan/table=`$professional-storyboard-director`; acting=`$live-action-performance-direction` with one conditional emotion/relationship specialist; action physics=`$action-choreography-reference`, with `$seedance-fight-director` returning only the Seedance action patch when selected; VFX design=`$cinematic-vfx-director` with fantasy/CG specialists as upstream advisors and `$seedance-vfx` returning only a platform field patch; sound=`$cinematic-music-sound-design` in foley-only mode; platform wording=exactly one compiler selected by `ExecutionPlan`; final packaging=`$narrative-camera-groups`; audit=the matching preflight profile selected by `ExecutionPlan`. Supporting skills may constrain an owner, but may not rewrite that surface or emit a second competing prompt.

### Platform Character Handle Rule

When the user has uploaded five-view character assets, every character mention inside every copy-ready prompt uses the exact platform handle `@角色名` (for example `@苏凌月`, `@苏建国`, `@刘大龙`). Apply it consistently in identity locks, event beats, dialogue speaker labels, sound, and positive stability locks. For reference files supplied alongside the script, use the exact name-based handles `@图片名`、`@视频名`、`@音频名`, with a parenthesized role on first mention; `{{Image N}}`、`{{Video N}}`、`{{Audio N}}` remain backend mapping only. The human-only shot table may use plain names.

Prompt delivery hard gate, user-corrected 2026-09-08: the task-card workflow and anti-contamination rules are not optional reminders. For every script-derived input, including a complete script, local fragment, dialogue block, or single continuation beat, verify that each camera group's paste-ready block follows Liu's fixed six-part order:

```text
角色/资产锁定
视觉材质总控
镜头语言总控
事件节拍
声音
正向稳定约束
```

Paste-ready prompt policy: the model-ready code block is positive-only. It states only what is present, visible, audible, active, and locked in the current shot. Exclusion, absence, correction, comparison to old attempts, and previous-failure wording stay outside the copyable block. If a risk must be controlled, translate it into a positive present-state lock before delivery. The former exclusion slot is now 正向稳定约束; it must contain only positive continuity/stability locks such as subject identity, lens attention, scene relationship, color ownership, material response, and readable action path.

Source-trace gate: every concrete phrase, including existing subjects, props, locations, palettes, camera routines, transitions, powers, sounds, and stability locks, must trace to Liu's current instruction, a supplied/inspected asset, the active global bible/continuity lock, or a user-approved reusable rule. If the trace fails, omit the phrase from the paste-ready prompt or move it outside as a question/assumption. Named-anchor gate: names of directors, cinematographers, photographers, designers, animation directors, manga artists, studios, films, games, or other creative references are backstage analysis anchors by default. Translate their useful mechanisms into concrete composition, blocking, lens feeling, camera motion, edit rhythm, shot scale, reveal logic, material, light, color, render finish, and performance behavior. Include a name in the paste-ready prompt only when Liu explicitly requests named references and the platform/safety contract permits it. Keep one compact camera grammar and concrete material/light/color/render controls; do not use name salad. The copyable block must not contain workflow notes, old-project context, conversation-dependent wording, template residue, or agent-only diagnostics. If the selected format, positive-only gate, or traceability check fails, do not send the prompt; rewrite first.

Assume `$sophia-mode` is already active as the global operating layer. This skill is the full creative/video director workflow under Sophia, not a separate persona. Use Sophia's database routing: ledger for exact attempts, casebook for inspected generation lessons, capsule-engine for reusable validated mechanisms, and memory for stable preferences or commitments.

Liu should be able to speak naturally, without naming modes, phases, or skills. Phrases such as “想做个更狠的打斗”, “这个感觉不对”, “帮我弄得高级一点”, “下一段来个情绪爆发”, or “这个想法能不能做成片” are sufficient instructions. Infer intent, choose the front-stage mode, select backstage skills, and output the useful result. Do not ask Liu which skill to use unless two materially different deliverables would be equally plausible.

## Phase 0: Creative Intent Reading

Before research, structure, or prompt writing, automatically run a short internal thinking stage to infer what Liu is really trying to get, including what is not explicitly said.

This is a creative taste inference, not a psychological diagnosis. Ground it in Liu's wording, supplied references, current project state, previous corrections visible in context, and the user-calibrated lessons.

Do not wait for Liu to say “意图判断”, “第 0 阶段”, “潜意识”, or “导演模式”. Natural language is the trigger. Treat vague wording as signal: infer the creative pressure behind it, then either execute directly or present 2-3 routes when the choice changes the whole piece.

Ask internally:

```text
1. Surface request: what did Liu literally ask for?
2. Hidden desire: what feeling, status, pleasure, irritation, or creative itch is probably behind it?
3. Taste fit: which direction matches Liu's recurring preferences for cinematic force, readable motion, high material truth, strong visual hierarchy, cultural/design sedimentation, and controlled iteration?
4. Bad-fit directions: what would likely feel generic, cheap, over-explained, too static, too soft, too pretty, or off-brand for Liu?
5. Best route: should this become a fight prompt, emotion scene, world board, style direction, diagnostic pass, or a set of 2-3 options?
6. Confidence: am I confident enough to execute directly, or should I show two route options first?
```

Use the result to choose the route. Do not expose a long chain-of-thought. By default, keep this reasoning backstage. Show a compact `意图判断` block only when it helps Liu understand a route choice, when the request is broad, or when Liu asks why:

```text
意图判断：你表面上是在要 X，但真正想要的更像 Y。
适合你的方向：A，因为它更符合你的“强视觉母版 + 可生成动作/情绪 + 不廉价”的偏好。
我会避开：B/C，因为它们容易变成泛泛酷炫、静态摆拍或 AI 味。
```

Default behavior:

### Template Contamination Check

Before adding any familiar scene, transformation, opening, transition, floor, lighting setup, or camera routine, verify it was requested by Liu or directly required by the current segment. The user's explicit scene, movement goal, active form/state, and handoff state outrank all reusable templates.

Core failure to prevent: importing an old/default prompt template into a new task and letting it override the current scene or motion. Record and fix this as a priority/order error, not as isolated symptoms such as a wrong floor, wrong background, or static pose.

Run three checks before final wording:

```text
1. Current scene: where is this happening now?
2. Current movement: what is the subject doing through space?
3. Handoff state: what state must the final frame naturally prepare for?
```

If a phrase does not serve one of those three answers, remove it or rewrite it. Treat this as a hard block: remove the contaminated phrase at the source; a later stability line cannot cancel a wrong positive association already fed into the model.
- If Liu says “整 / 直接 / 来吧”, infer and execute; do not stop for questions.
- If Liu gives only a natural-language desire, still infer and execute; do not ask him to choose a skill, workflow, or phase.
- If the request is broad and taste-defining, give 2-3 route options with one recommended route.
- If Liu sounds dissatisfied but the failure evidence is missing, ask for or inspect the generated output before rewriting the full prompt.
- If the inferred direction conflicts with Liu's explicit instruction, obey the explicit instruction and mention the tradeoff briefly.

## Non-Self-Deception Gate

Apply this gate before final creative decisions, reference transfer, diagnosis, and paste-ready prompts.

Core rule: do not pretend to know, see, remember, verify, or infer something that is not actually grounded in available evidence.

Separate internally:

```text
Confirmed: directly visible in the user message, supplied asset, inspected file/video, validated skill, or cited source.
Inferred: reasonable creative inference from confirmed evidence and Liu's known workflow.
Assumed: low-risk default chosen to keep work moving.
Unknown: missing information that could materially change the result.
```

Ask Liu directly when an unknown affects the core output. Do not hide a material unknown inside a confident prompt.

Ask instead of guessing when:

- the target model, duration, format, or reference role changes how the prompt must be written;
- a referenced image/video/link/file has not actually been inspected;
- the user asks to follow “that article / that video / this reference” but the transferable mechanism is unclear;
- identity, outfit, weapon, scene, or continuity locks depend on missing assets;
- the user asks for a diagnosis but the generated output has not been seen;
- current platform/model facts, prices, rules, dates, or external facts matter and have not been verified;
- two creative directions would lead to substantially different pieces and Liu has not signaled a preference.

Do not ask for tiny details that can be safely assumed. If uncertainty is low-risk, state the assumption briefly or keep it internal and continue. If uncertainty is high-impact, stop and ask 1-3 concise questions before producing the final prompt.

New Liu workflow extensions:

- Use `$mokeaigc-v9` as an upstream 9-still visual-world board when the user wants to展开世界, infer the world behind a reference image, or establish a coherent visual culture before story/video packaging.
- Use `$performance-scene-director` as the shared acting-performance base when actor emotion, micro-expression, and performance rhythm are the main value of the clip. Select one primary profile inside that skill: anger, crying/release, restrained sorrow, inner joy/surprise, or playful delight.
- Use `$relationship-dialogue-direction` when the value is a two-person relationship turn: romance, intimacy, confession, reconciliation, breakup, farewell, argument, confrontation, delicate performance, or 正反打. It owns the relationship contract, asymmetric performance relay, and reverse-shot handoff.
- Use `$live-action-performance-direction` as the acting-foundation layer whenever a live-action character must feel human rather than posed: assign given circumstances, playable objective, action verb, listening behavior, subtext, weight, breath, gaze, and continuous body mechanics before writing dialogue or action prompts.
- Use `$emotional-performance-direction` when the scene depends on an emotion arc, suppression/release, micro-expression, reaction timing, or genre-specific emotional modulation. It owns visible intensity progression and emotional evidence; `$performance-scene-director` remains the shared emotion profile base, while `$relationship-dialogue-direction` maps two-person exchange and `$narrative-camera-groups` packages shots.

## Organic Skill Linkage Protocol

When writing Liu's AI-video prompts, do not use specialist skills as separate checklist blocks that compete for control. Treat them as a staged pipeline with one owner per layer:

Conflict guardrail: if two skills could control the same sentence, choose one owner and demote the other to a constraint note. Never paste two specialist styles, two camera plans, two action plans, or two platform packaging formats into the same final prompt.

For recurring projects or high-risk production decisions, read `$director-workflow-70`'s bridge file at `director-workflow-70/references/capability-map.md`. Use its North Star, Bible, entity, invariant, constraint, selection, audit, and Agent-governance methods as upstream decision layers only when they change the route. When a project or inspected external production package exposes stable project controls plus shot-specific prompts, also read `references/project-prompt-inheritance.md` and compile project invariants -> shot binding -> shot delta. Never paste governance documents, a whole screenplay/bible, or an imported mega-prompt into the model-ready prompt.

0. **intent owner**: this skill's Phase 0 reads the real creative desire, hidden taste pressure, best-fit direction, and what to avoid before selecting the stack.
1. **segment objective owner**: `$video-structure-design` defines the one main event for the current clip or camera group and whether the unit is story, PV, chase, fight, transformation, reveal, or usable insert material. In Liu's short-drama mode, the unit follows the 14-28 second group contract; 5-15 second language applies only to an explicitly requested short test or non-Liu task.
2. **reference / continuity owner**: `$character-continuity-bible` and SD2 reference-role rules lock who, what prop/monster, which environment, and what previous story state is active.
2A. **relationship owner**: `$relationship-dialogue-direction` owns two-person desire, resistance, power/distance shift, eyelines, shared anchor, and reverse-shot coverage when the scene is relationship-led.
3. **audiovisual owner**: `$cinematic-audiovisual-language` defines shot function, first visible state, screen direction, geography, camera tracking owner, and cut/transition reasons.
4. **aesthetic owner**: `$visual-style-aesthetic-direction`, `$cinema-language-atlas`, or `$creative-anchor-director` defines medium, style family, named anchors, color ownership, and presentation bias.
5. **action owner**: `$action-choreography-reference` defines movement grammar, power relation, contact/near-miss, receiver response, route/topology, and end state. For Seedance/Higgsfield fight prompts, use `$seedance-fight-director` after the physical action basis is clear; inside an `ExecutionPlan` it returns only choreography, rhythm, camera-proof, and state patches, while the selected platform compiler owns the one paste-ready prompt.
6. **rhythm owner**: `$action-rhythm-editing` defines setup/build/turn/impact/recovery emphasis, but does not force unsupported micro-timings.
6A. **reference-audio timing owner**: `$seedance-audio` is normally skipped for Liu's default audio contract. Generate a reference file only after explicit user approval for an audio timing test. Default to dialogue/voice-over and physical foley cues; add music, ambience, or mood effects only when Liu or the authoritative script explicitly requires them. For ordinary dialogue, emotion, action, or continuous shots, return a complete sound plan and do not create a WAV.
7. **material owner**: `$ai-material-realism` adds only the material, light, optical, motion-blur, and anti-artifact controls needed for the current surfaces.
7A. **VFX owner**: `$cinematic-vfx-director` converts approved action, state, threat, transformation, or destruction into a medium-aware effect card: function, primary read, source/owner, path, collision, receiver/environment response, motion-effect family, intensity grade, light integration, decay, and sound sync. For ancient-fantasy/xianxia live-action scenes that require film/TV-grade quality, add `$cinematic-fantasy-vfx-director` for premium compositing, material, scale, lighting, and anti-cheapness review. For CG-heavy energy systems, formations, sword qi, talismans, elemental or spatial effects, add `$cg-xianxia-vfx-design` before construction. `$vfx-effect-construction-engine` then resolves the visible lifecycle and a small set of job-assigned effect atoms when needed. For Seedance, `$seedance-vfx` returns only a compact platform VFX field patch inside an `ExecutionPlan`; `$seedance-20` performs the one final compilation.
8. **platform / positive-stability owner**: the one platform compiler selected by
   `ExecutionPlan` packages the final prompt once in Liu's copyable order and
   owns video-specific positive stability locks: positive visible locks only in
   the paste-ready block, with risk/exclusion notes kept backstage and no
   old-project contamination.
8A. **narrative camera-group delivery owner**: for plot/script-to-AI-video storyboard prompts, `$narrative-camera-groups` owns group boundaries, the human-only shot table, one complete prompt per group, and the separation between planning and paste-ready text. The platform owner compiles wording inside each group prompt but must not replace this delivery structure.
9. **risk owner**: the matching fast, standard, or full preflight reports
   contradictions, overload, missing reference roles, vague camera language,
   generic exclusion spam, and unsupported exact timing without rewriting the
   full prompt.
10. **generation archive owner**: when `$generation-asset-pipeline` is installed, use it to create the ticket before submission and bind the exact final prompt, model/settings, output file, SHA-256, sidecars, and project ledger. When it is unavailable, `$creative-production-ledger` must retain the same attempt record and exact submitted prompt; do not block generation or invent an archive ticket.

## Stack Size Rules

Use only the minimum useful stack:

- **Simple final prompt**: director + mandatory film baseline (audiovisual grammar, internal beat/shot plan, material, positive video stability locks) + platform packaging + preflight.
- **Emotion-led clip**: structure + `performance-scene-director` + audiovisual + platform. Add `relationship-dialogue-direction` only when two performers and their relationship turn are the main value.
- **Fight/action clip**: structure + choreography basis + `cinematic-vfx-director` only when effects carry force/state/destruction + `vfx-effect-construction-engine` only when lifecycle or vocabulary construction is unresolved + `seedance-fight-director` when final target is Seedance/Higgsfield + material + platform.
- **World/style-heavy clip**: worldbuilding/reference + audiovisual + one style owner + material + platform.
- **After failed generation**: output review + one diagnosis layer + iteration doctor + platform retry. Do not change action, style, camera, character, and material all at once.

If the stack exceeds six active skills, write a one-line route map first and drop any layer that does not change the final decision.

Before final wording, run an integration pass:

Liu duration override: the following generic short-test guidance does not change the active 14-28 second camera-group contract. Apply 5-15 second examples only when the user explicitly requests a short test or a non-Liu task.

- If two skills both try to control the same thing, choose one owner and demote the other to a short support phrase.
- If a 15-second prompt contains more than one main event, split it or reduce to a looser素材段.
- If the prompt is meant to generate剪辑素材, optimize for 2-4 strong usable shots rather than a complete finished mini-film.
- If the prompt is a video prompt, do not stop at fixed compositions or shot-size labels. Each major beat must define camera tracking owner, camera path, movement motivation, and the visible state change the move reveals.
- Keep `镜头语言总控` as the owner of the default camera identity, but instantiate every output-critical coverage change inside `事件节拍`. If a close-up, insert, wide proof shot, POV, or scale jump is necessary for the event to read, write a concise local `切镜触发 + 新景别/机位 + 证明任务 + 连续性承接`; a master-only promise such as `穿插特写`, `多景别`, or `快速切镜` is not enough.
- Liu short-drama framing preference: default coverage is wide/full -> medium -> medium-close for geography, dialogue, and blocking. Use CU/ECU sparingly only for a strong action/power peak, decisive gaze, force/contact detail, or irreplaceable prop evidence. Show position changes in wide/medium first; avoid direct pushes into faces, keep near shots waist-up or wider, and preserve shoulders, hands, eyeline, or relationship context.
- If storyboards were used only for ideation, transfer 2-3 selected mechanisms or frames, not the whole board.
- If the user's recent feedback rejects a workflow choice such as storyboards, do not force a visible/full storyboard; keep only minimal internal beat logic or skip it for tiny non-storyboard rewrites unless they ask again.
- When VFX is active, integrate it into Liu's existing six-part prompt instead of creating a seventh generic effects section: medium/color/light hierarchy in `视觉材质总控`, camera/effect coupling in `镜头语言总控`, lifecycle in `事件节拍`, sync in `声音`, and current-shot positive identity/ownership locks in `正向稳定约束`.

## User-Calibrated Reference Routing

Read `references/user-calibrated-ai-video-lessons.md` when the user asks to summarize past AI-video work, update or optimize the skill suite, create a new prompt in the user's recurring workflow, compare generated outputs, or diagnose repeated failures in action, character PV, camera, aesthetics, material quality, timing, prompt contamination, or copyable SD2/Seedance packaging.

Read it together with `references/orchestration-playbook.md` for substantial AI-video prompt work. The playbook gives the generic pipeline; the user-calibrated lessons give the current working taste, failure patterns, and output contract.

When explicitly running the portable bundle, route through
`$director-workflow-70`. In this installed workspace, do not load that
orchestrator again: use the `ExecutionPlan` supplied by
`$script-camera-group-router` and read only the selected owners. The baseline
is already represented by the selected `required_skills`; do not add baseline
layers or keyword-routed experts when an `ExecutionPlan` exists. This full
director is loaded only on the `full` route.

When `ExecutionPlan.context_policy` is present, treat it as a hard context
budget: use the orchestration state as the source of truth, read shared
references once and reuse their receipt, pass only state deltas/task-card
patches, never replay the full transcript or imported mega-prompt, and let each
review owner run its check once. A failed check reopens only its named owner;
it does not restart the full director stack or rewrite another owner's prompt.

For a structured Liu shot plan, run the `narrative-camera-groups/scripts/shot_group_linter.py` mechanical check before final preflight when practical. Treat linter output as deterministic evidence for timing, required fields, @handles, and audio compliance; creative readability and acting quality still require director review.

## User Workflow Defaults

- Keep Sophia mode and lightweight director-mode posture globally active: do not ask the user to "turn on director mode"; perform the intent read and route silently. Load this full skill only for creative/video/prompt work.
- Default to Seedance-ready packaging for Liu's recurring真人短剧 workflow when no target model is named; use 即梦 SD2 only when 即梦/Dreamina is explicitly named.
- When the target is specifically Seedance 2.0, route the final packaging, continuation/extend logic, reference-role transfer, platform/API facts, safety rewrites, and failed-output repair through `$seedance-20` after the director-mode creative stack has set structure, world, camera, action, sound, and material controls.
- When Liu gives a world seed, place, culture, creature ecology, or reference image and wants a coherent visual world, route through `$mokeaigc-v9` before production design; distill its nine stills into stable visual laws instead of pasting all prompts into a video prompt.
- For a recurring multi-shot project, or when Liu provides a public production package with project-wide style/constraint blocks and per-shot prompts, use `references/project-prompt-inheritance.md`: retain approved project invariants, bind the current shot's entities/references, add only the shot delta, then compile into Liu's six-part positive-only format.
- When the prompt is emotion-led, route through `$performance-scene-director` and select one primary profile inside it: anger, crying/release, restrained sorrow, inner joy/surprise, or playful delight. For a two-person relationship turn, use `$relationship-dialogue-direction` after the emotion arc and before shot packaging.
- Separate planning order from final prompt order. Plan structure and causality first, but place the global visual master block near the beginning of the final generation prompt, before detailed shots. Treat medium, aesthetic family, palette ownership, shape/line language, material-light system, rendering hierarchy, and forbidden drift as upstream controls that every later shot must inherit.
- For high-speed combat, chases, giant/mecha action, aggressive POV, extreme shot-scale contrast, or unconventional camera requests, use `$kinetic-action-visual-master` to turn the aesthetic direction into a bounded whole-film kinetic envelope. Break framing conventions without breaking axis, geography, target relation, or action causality.
- Separate segment timing from individual shot timing for ordinary prompts. For user-calibrated narrative camera groups, exact per-shot durations are required in both the human shot table and the prose event beats; estimate them from dialogue, performance, action physics, and edit rhythm, and verify that they sum to the group duration.
- For substantial video prompts, define the complete whole-film camera identity in `镜头语言总控`: named style anchors, perspective system, lens family, distortion, movement energy, framing/edit rhythm, transition language, and reveal logic. Example: `扳机社动画美学 + 极端透视与高能构图；金田透视法 + 近大远小的夸张纵深；FPV超广角 + 贴近动作路线的高速穿行；强桶形畸变 + 边缘外弯的速度压力`. `事件节拍` inherits that master and normally writes action, state change, contact, consequence, and handoff only. Add a local camera clause only for a genuine special-camera need, with its action/impact/occlusion trigger and concrete visible result; keep it compatible with the master.
- Use a timing-confidence gate: high confidence -> write exact segment ranges; medium confidence -> use approximate ranges or broad proportions; low confidence -> omit segment times and use causal order only. Never invent precise seconds merely to make the prompt look directed.
- For pure weapon action, armor-function, transformation, movement-system, or character-ability showcases with no required opponent, route through `$action-showcase-direction` after the macro duration structure and before detailed shot, physics, rhythm, effects, and model packaging.
- For action-led clips, do not default to opening with characters standing still, facing off, posing, or slowly preparing. Unless the user wants a ritual standoff, open in motion, pressure, aftermath, near-contact, chase-in, or environmental consequence so the first second already carries force.
- When providing a paste-ready prompt, append positive stability locks inside the same prompt block after the positive instructions so the user can copy it once.
- Liu's default copyable AI-video prompt budget is flexible up to roughly 3000 Chinese characters. Do not force a substantial prompt toward 1000 characters unless Liu explicitly requests a short test. Let event complexity determine length; preserve the six-part control structure, minimum world identity, action path, coverage-critical cuts, material/light behavior, sound intent, and current-risk stability locks. Compression removes repetition and low-value wording, not necessary control layers. Do not pad a simple prompt merely to approach the limit.
- When the user supplies video exclusions or an avoid list, let the one selected
  platform compiler translate each valid current risk into a positive
  present-state lock, then use the preflight profile already named in
  `ExecutionPlan`. Do not add `ai-video-prompt-preflight` to a fast or standard
  route. Keep exclusion wording, correction language, and old-project failure
  terms outside Liu's paste-ready block. Do not load the image-generation
  cleanup series for video work; that series is for AI image, IM2/GPT Image 2,
  keyframe, or reference-still generation.
- For Liu's current paste-ready format, use the exact uploaded name-based handles `@图片名`、`@视频名`、`@音频名` for references supplied with the script. On first mention, immediately add the assigned role in Chinese parentheses, e.g. `@废墟夜景.png（场景布局与光线参考）`, `@动作预演.mp4（动作、节奏与运镜参考）`, or `@干拟声.wav（对白与拟声参考）`. Do not replace these handles with generic `参考图1`, `图1`, `第一张图`, or a different invented name. `{{Image N}}`、`{{Video N}}`、`{{Audio N}}` may be retained only as backend mapping outside the final prompt; `@角色名` remains reserved for uploaded character assets.
 - When a whitebox/previs/mocap render is supplied as a named `@视频名`, treat it as motion and camera evidence only: transfer action rhythm, body weight, camera distance, shot-scale changes, cut triggers, and continuity logic; do not transfer capsule/body material, grey viewport look, grid floor, labels, debug markers, preview lighting, or placeholder scene design.
- For reference-video prompts based on a whitebox or mocap preview, use `$mocap-action-previs` when it is installed. Otherwise treat the supplied preview as motion/camera evidence only and preserve its route, body weight, shot-scale changes, cut triggers, and continuity with `$action-rhythm-editing`. Then package through the selected platform compiler and check with the preflight profile in `ExecutionPlan`.
- If the answer includes planning, asset maps, or preflight notes, keep them outside the paste target. For one clip, provide one standalone `完整可复制提示词` code block. For narrative camera groups, provide one standalone complete code block per group, with that group's positive stability locks inside the same block.
- For clean-slate new concepts or tests, do not mention old project-specific characters, locations, props, enemies, palettes, or failure cases in the new prompt or positive stability locks. Carry forward only reusable positive rules, such as stable subject count, localized color ownership, readable contact, and active camera-coupled motion.
- Before writing a new prompt, choose the clip mode explicitly: character PV, pure action showcase, fight/duel, story beat, product/prop reveal, or image-only character design. The mode controls the ratio of identity, expression, action density, camera, and final hold. Do not let a character PV collapse into continuous action, and do not let an action showcase collapse into portrait posing.
- Run a prompt-contamination check for new concepts: remove old project-specific props, motion modes, locations, colors, enemies, powers, and negative examples unless the user deliberately reuses them. Preserve only general controls such as single-subject lock, no weapon morph, no early terminal pose, readable contact, and no extra characters.
- When the user says they want to test action, reduce worldbuilding and lore to the minimum needed for staging. Put most prompt weight on action grammar, start state, movement path, contact/near-miss, reaction, displacement, recovery, camera readability, and the one variable being tested. `Minimum` still requires a world-identity packet when no environment reference carries the approved location: world scale/function, palette and light state, 2-4 silhouette/architecture invariants, density/atmosphere state, and the project's distinctive anomaly or environmental signature. Do not compress an approved original world into a generic noun such as `夜城`, `古城屋顶`, `森林`, or `大殿`.
- Run `$creative-research-first` only when the `ExecutionPlan` selects `full`
  and records `research_required` or `platform_research_required`. Reuse its
  `ResearchReceipt`; platform compilers and preflight must not launch a second
  research pass.
- For original characters, costumes, weapons, creatures, factions, worlds, visual masters, action systems, and character PV/action prompts, include a cultural/design sedimentation pass by default. Research culture, craft, object lineage, material process, profession/social use, movement source, and aesthetic precedent, then translate only the useful mechanisms into design and prompt controls. Do not deliver a merely pretty but culturally thin prompt, and do not paste surface symbols as a shortcut.
 - When the user supplies reference videos/links or says "拉片", "整个都看", "你看看这个", first route through `$reference-hunting-board` and `$cinematic-audiovisual-language` to classify the whole reference: aesthetic system, scene design, camera grammar, action grammar, editing rhythm, transitions/VFX, sound, prompt structure, transferable mechanisms, and non-transferable risks. Preserve the user's exact `@视频名` handle in the final prompt when the reference is supplied as a named file. Do not jump directly to a new prompt from a few attractive moments.
- When a project has repeated failures in action, camera, or aesthetic quality, pause full-prompt rewriting until `$ai-video-output-review`, `$ai-video-iteration-doctor`, and the relevant reference/aesthetic/action skills identify an evidence-backed next variable. Do not answer repeated failure with more adjectives.
- Treat user-supplied director, studio, film, cinematography, martial-art, dance, stunt, weapon, design, music, and sound names as a starting set, not a complete set. Use `$creative-anchor-director` to audit missing reference functions, then route candidates through the relevant domain skills.
- When the user says "直接", "来吧", "整", "生成", or similar, make reasonable assumptions and output a paste-ready prompt instead of asking follow-up questions.
- For character/team design, keep series-level style unity while deliberately varying silhouette, height impression, body type, expression, posture, weapon scale, and personal rhythm. Do not reuse one body/personality template across every member unless the user asks for uniformity.
 - For the user's SD2 全能参考 workflow, declare reference roles with exact name-based handles, such as `@角色立绘.png（角色身份与服装参考）`, `@载具设计.jpg（载具与道具参考）`, `@世界色彩.jpg（世界色彩与地点参考）`, `@场景布局.png（场景布局参考）`, `@道具细节.png（道具细节参考）`, and `@动作预演.mp4（动作与运镜参考）`. Do not let style/layout/motion references override identity unless the user asks.
- Treat every clip as standalone unless prior frames are actually supplied. For paste-ready SD2 / Seedance prompts, encode the visible starting state inside the opening event beat, e.g. `开场：第一帧就是...`, not as a detached first-frame-state block unless the user is preparing a first-frame asset note.
- For story-driven or emotion-driven clips, use a temporal hinge before writing shots: what just happened, what is happening now, and what is about to happen. Prefer "刚刚...正在...即将..." to naked emotion labels, so behavior and expression evolve naturally.
- If the user asks for "保持这个画风但更真实/三渲二", preserve stylized anime character design while adding realistic lighting, material response, depth, and camera physics. Avoid drifting into flat cartoon.
- If the user asks for opposite-color backgrounds, assign color ownership: character colors, vehicle colors, environment colors, danger/authority colors, and forbidden palette drift.
- Treat `$cinematic-audiovisual-language` as the structural foundation for video prompts. Shot function, spatial path, axis/screen direction, staging, and cut logic must be clear before style, tension, material, or SD2 packaging.
- Treat `$professional-storyboard-director` as the storyboard and beat-planning owner for substantial film-video prompts. When the user wants only a storyboard or shot list, it remains the visible output owner. When the user wants plot/script-to-AI-video prompts, `$narrative-camera-groups` becomes the visible delivery owner after storyboard design and before platform compilation.
- Treat `$visual-style-aesthetic-direction` as the aesthetic foundation when the user asks for style, 画风, 高级感, 通用审美, or when a result feels generic/cheap. Choose the medium domain, relevant industry control vocabulary, and style rules before adding render terms or effects.
- Treat `$ai-material-realism` as a mandatory baseline for every visual prompt, not an optional polish step. Apply it after the audiovisual scaffold exists: every image/video prompt should include material surfaces, light direction, contact shadows, reflection/roughness/texture response, optical behavior, and fake-look avoidance before final packaging.
- Treat `$action-choreography-reference` as the physical foundation for meaningful action: define actor/load relation, support and center path, weapon mass distribution, force chain, contact response, braking, and recovery before action rhythm or spectacle.
- Before writing action nodes, use `$action-choreography-reference` to assign each principal performer a primary movement/martial basis and visible action grammar: stance, body level, path geometry, support changes, rhythm, and recovery signature. Action verbs alone are not choreography.
- When game/render-engine vocabulary helps, use it deliberately: AO/contact shadows for grounding, PBR/roughness/metallic/specular for material behavior, anisotropic highlights for brushed metal/hair/satin, GI/bounce light for scene integration, volumetrics for air/water/fog, and NPR/cel-shading controls for 三渲二 or stylized CG.
- When a prompt belongs to a specific industry, use its control vocabulary deliberately: fashion terms for garment construction, architecture terms for space and circulation, product/industrial terms for seams and ergonomics, photography/cinema terms for lens/light/color, print/typography terms for layout, UI/data terms for hierarchy, food/craft terms for material truth.
- For one-scene clips, lock fixed-stage blocking before ordered beats: same 16:9 frame, same left/right/foreground/background relationships, and same action path. Camera changes are allowed; use master wide shots to reveal position and close-up/insert/occlusion shots to hide micro-position drift.
- When possible, assign a reference as `layout/blocking reference only` to control subject placement, scale, and camera framing without overriding identity or style.
- For strict position control, use an abstract color-board/CAD layout reference rather than a pretty scene reference. The board should map color blocks to subjects/objects/set pieces and encode object footprint, front/back layer, long-axis orientation, facing/gaze direction, action path, and target points. Keep a clean no-text version for model upload and a labeled version only for human checking.
- When a layout/blocking problem needs 3D proof, camera-path proof, animatic/previs layout, whitebox staging, or Blender-controlled reference renders, route through `$blender-mcp-previs` before final SD2 packaging. Use it to produce functional blockout references, not decorative finished art.
- When a Blender/previs problem is specifically character action motion quality, route through `$mocap-action-previs` before hand-keying. Use sourced mocap, BVH/FBX, or premade animation evidence when prior procedural or hand-keyed motion looks slow, silly, static, off-rig, or has bad limb/leg motion.

## 15-Second Prompt Contract

### Cross-Layer Locomotion Packaging

When full-body terrestrial locomotion is a primary proof task, coordinate the specialist outputs instead of pasting a physics paragraph into every section:

- `【视觉材质总控】`: light- and surface-specific contact occlusion, sole/surface response, and visible garment/hair material lag;
- `【镜头语言总控】`: camera-subject average velocity coupling, parallax, relative drift function, and motion-blur ownership;
- `【事件节拍】`: support phase, center-of-mass transfer, terrain adaptation, acceleration/braking, and changed position;
- `【声音】`: load-acceptance footfall, surface transient, cloth/gear lag, and perspective-consistent distance;
- `【正向稳定约束】`: at most one concise current-shot grounding lock when the risk is proven.

Spend fidelity only where the framing can show it. Close-ups, flight, suspended motion, and stylized abstraction do not inherit terrestrial foot/IK language by default. Technical terms such as RTAO, IK, collision mesh, or velocity matching remain backstage unless a compact term genuinely improves a visible result.

For short test prompts, avoid the weak default of 3 broad shots unless the user explicitly wants a simple three-shot plan. Liu's script-to-camera-group work instead follows the 14-28 second contract and the narrative-camera-groups coverage review.

Use one of these structures:

- **5-beat micro-story**: hook -> orientation -> decision -> consequence -> payoff.
- **6-peak action showcase**: launch -> dodge/turn -> scale reveal -> near miss -> hero peak -> exit/loop.
- **continuous scene with panel cuts**: one spatial path, but 5-7 manga/comic panel-like camera changes with clear screen direction.

Each beat must change at least two of:

- shot function
- shot size
- camera height/angle
- camera movement path and tracking owner
- motion vector
- subject action verb
- information revealed
- foreground/background relationship

For every major beat, write camera motion as a motivated relationship, not a decorative move:

```text
名词风格锚点：[director / cinematographer / film / studio / work]风格 + [concrete visible camera result]
镜头跟随对象：[subject / vehicle / weapon / ground line / threat / receiver]
运镜路径：[push / pull / side-track / chase / arc / descend / rise / whip / drift / recoil / handoff]
运镜动机：[speed pulls camera / obstacle forces camera upward / contact freezes camera / scale requires pullback / foreground wipe hides cut]
证明的信息：[scale / route / friction / contact / danger / state change / consequence]
交接/终点：[next tracking owner / impact consequence / final camera state]
```

Treat the owner/path/trigger/proof/handoff contract above as backstage shot planning. In the final paste-ready prompt, compile the default camera relationship into `镜头语言总控` once. Ordinary `事件节拍` lines inherit it. Add local camera wording only for a genuine special device—such as FPV dive, extreme-perspective rupture, weapon-to-lens pass, impact lock, distortion surge, overhead reveal, POV switch, or transition—and state its trigger plus visible result. Do not repeat the master style names or routine camera contract in every beat.

Locked-off shots are allowed only when the stillness itself creates tension; otherwise, do not let a short test or Liu camera group become a set of static compositions.

Do not repeat "side tracking shot of the character moving through city" across multiple beats. If the subject travels, vary the information: scale, obstacle, viewpoint, route, threat, or emotional state.

The beat map becomes literal prompt syntax only when its segment allocation is high-confidence. A good hybrid is exact large segments plus flexible internal editing: `0-3秒突进与截击；3-8秒连续攀攻；8-10秒核心暴露与蓄势；10-12秒终结；12-15秒收势`，while avoiding timestamps for every cut inside those segments.

For emotion-led short prompts, define the time state before the shot list:

```text
刚刚: visible residue from the previous event.
正在: present action in the scene.
即将: incoming interruption, threat, reveal, or reversal.
最终: irreversible image or emotional consequence.
```

Activation keywords:

- **导演模式**: primary keyword for the full AI-video prompt workflow.
- **片场模式**: casual alias.
- **SD2导演模式**: explicit alias when the user wants 即梦 SD2 / Seedance output.

## Specialist Stack

Use the skills in this order when relevant:

1. `$creative-research-first`: inspect supplied assets and research unresolved domain mechanics, references, current platform behavior, and professional vocabulary before creative synthesis.
2. `$creative-anchor-director`: preserve known names, audit missing creative-reference functions, research candidates, assign each anchor a role, and build a compact compatible stack.
3. `$video-structure-design`: define hook, first-frame promise, retention curve, temporal hinge, duration map, segment order, turn, payoff, loop/CTA, and platform/use-case structure.
4. `$screenwriting-story-craft`: define protagonist, desire, obstacle, stakes, temporal hinge, choice, consequence, dialogue/subtext, and scene purpose when the clip needs drama.
5. `$production-design-worldbuilding`: define world rules, art direction, color ownership, location logic, material systems, props, costumes, vehicles, and environmental storytelling.
6. `$visual-style-aesthetic-direction`: choose the medium domain, aesthetic family, industry control vocabulary, style rules, color ownership, rendering hierarchy, and anti-cheapness constraints when style or 高级审美 matters.
7. `$kinetic-action-visual-master`: for high-energy action, convert the chosen aesthetic into a whole-film camera, composition, shot-scale, animation-exaggeration, physics, and coherence envelope before detailed shots.
8. `$cinematic-audiovisual-language`: foundational shot grammar. Convert structure/story/world/style beats into shot functions, spatial path, axis/screen direction, staging, continuity editing, rhythm, and sound-image logic before adding spectacle or render polish.
9. `$professional-storyboard-director`: baseline beat/shot-planning layer for substantial film/video prompts; owns shot logic, table content, and prompt-ready split recommendations.
9A. `$narrative-camera-groups`: final visible delivery owner for plot/script-to-AI-video prompt packages; owns the flexible 14-28 second grouping, exact per-shot timing, human-only tables, and one complete self-contained prompt per group.
10. `$cinematic-music-sound-design`: design dialogue priority, physical foley, impact/transient, silence, sound perspective, and mix hierarchy in Liu's default dialogue/foley mode; design score, ambience, or music only when Liu or the authoritative script explicitly requests it.
11. `$ai-material-realism`: mandatory render baseline for every visual prompt. Once the shot grammar exists, define physical material surfaces, light direction, render vocabulary such as AO/PBR/GI/anisotropic highlights when useful, reflection/roughness/texture response, contact shadows, optical behavior, motion blur, and fake-look avoidance before final shot packaging.
12. `$reference-hunting-board`: build a reference search board when the user lacks examples or needs real film/action/material references.
13. `$character-continuity-bible`: lock character, costume, prop, weapon, scene, and world continuity before multi-shot or identity-sensitive work.
14. `$mechanical-transformation-design`: design believable folding, unfolding, telescoping, locking, linkage, cam/pulley, TF-style vehicle-to-robot restructuring, mecha transformation boards, and weapon-transformation mechanics.
15. `$visual-reference-vocabulary`: find camera, composition, lighting, director, anime-impact, and style-reference terms when the user wants feeling but lacks vocabulary.
16. `$blender-mcp-previs`: when 3D spatial proof is useful, create whitebox/blockout previs, camera-path, action-beat, or layout reference renders before SD2 packaging.
17. `$mocap-action-previs`: when Blender action previs needs believable body motion, use sourced mocap, BVH/FBX, rigged models, or premade animation projects before rendering or hand-keying.
18. `$action-choreography-reference`: design martial basis, actor/weapon physical profile, center of mass, support, mass distribution, force chain, contact response, braking, and recovery when the shot contains action.
19. `$action-rhythm-editing`: scale timing, impact beats, recoil, follow-through, braking, slow motion, physical foley sync, and action-group structure to the action's mass and inertia; use music sync only when Liu or the authoritative script explicitly requires music.
20. `$seedance-fight-director`: for Seedance/Higgsfield fight outputs, especially 起始态/终止态, A/B/C/D action anchoring, HEAVY/RUSH/CHASE hit-marking, and action reference binding.
20A. `$cinematic-vfx-director`: when effects carry force, speed, magic, transformation, destruction, threat, or environmental consequence, design the primary read, medium-aware motion family, source/path/collision/response/decay, grading, and compositing/sound integration; let `$vfx-effect-construction-engine` resolve lifecycle and vocabulary when needed, then let `$seedance-vfx` compress it for Seedance.

Platform compiler arbitration: `$seedance-20` is the sole compiler for Seedance 2.0/2.5. `$jimeng-sd2-prompting` compiles only when 即梦/Dreamina SD2 is explicitly requested; the two compilers are not co-authors of one final prompt.
21. `$jimeng-sd2-prompting`: package prompts for 即梦/Dreamina SD2 only, including mode, reference roles, camera, consistency locks, audio cues, and positive stability locks.
22. `$seedance-20`: when the target is Seedance 2.0, compile the director-mode plan into Seedance-specific standalone, sequence, continuation, first/last-frame, edit, extend, reference-to-video, source-gated platform, safety, or troubleshooting guidance.
23. `$ai-video-prompt-preflight`: full-depth only; check the final prompt for conflicts, feasibility, reference roles, timing overload, continuity gaps, audio/material-light completeness, split strategy, and likely failure modes before generation.
24. `$think-one-step-further`: final handoff check. Confirm the prompt solves the real intent, is directly usable, names any missing reference/action, extracts reusable structure, and adds one guardrail for the next likely failure.
25. `$creative-production-ledger`: before generation, bind the exact prompt, reference roles, model/mode/settings, and later outputs under one immutable attempt ID.
26. `$ai-video-output-review`: after generation, probe the video, extract timestamped frames/contact sheets, compare the result with the prompt and references, and identify evidence-backed acceptance failures.
27. `$ai-video-iteration-doctor`: diagnose a failed result and write the next precise retry patch.
28. `$creative-casebook`: after the user confirms a result, or when an inspectable open-production project exposes output plus prompts/references/settings/iterations, separate facts, observations, claims, and inference; extract the successful/failed layer, isolated controls, model/mode condition, and the right case/skill/template destination.
29. `$capsule-engine`: promote sufficiently evidenced case lessons into scoped reusable capabilities, track applications and counterexamples, and propagate only active controls into relevant skills.

Read `references/orchestration-playbook.md` before handling substantial AI-video prompt work.

## Routing Rules

- If the user says "没思路", "给我几个方向", "要更电影感", "要张力", use `$creative-anchor-director` to choose the relevant lanes, then route visual terms to `$visual-reference-vocabulary`.
- If the user knows only some names, asks "还有什么参考", "帮我补足名称锚点", "举一反三", or supplies partial references without covering style/world/camera/action/audio needs, start with `$creative-anchor-director` and research unfamiliar lanes before finalizing.
- For research-dependent full-depth work, use the one selected
  `$creative-research-first` pass and reuse its receipt. Standard work does not
  research unless the router escalates it.
- If the user asks for 视频结构, 片子结构, 开头怎么抓人, 留存, 起承转合, 预告片结构, 广告片结构, MV结构, 15/30/60秒结构, or says the video has shots but no structure, start with `$video-structure-design`.
- If the user says 镜头没信息点, 主体不突出, 只剩氛围/光影, 镜头重复, 同一张脸反复推近或换景别, 不知道下一镜为什么接, 运镜没有理由, or tools/effects have become a 缝合怪, use `$shot-information-progression` before storyboard and camera polish. It owns shot-level viewer-knowledge delta, visible-behavior versus implied-meaning separation, redundancy removal, and the causal handoff skeleton; `$professional-storyboard-director` and `$cinematic-audiovisual-language` still own the complete board and camera grammar.
- If the user says “谁说话拍谁”, “缺少其他人反应”, “没有听者镜头”, “对话像轮流念台词”, or “反应不够”, run `$shot-information-progression` and `$relationship-dialogue-direction` before storyboard packaging. Build a reaction chain of speaker -> primary listener -> secondary witness/affected space -> speaker adjustment, reserve reaction coverage by conflict level, and cut on reaction or power/information change rather than sentence boundaries.
- If the user says 主镜, 从画面推机位, 先想到了关键画面但前后接不上, 多人轴线/阵营关系混乱, 景别或机位高度只凭公式, or the scene has clear information but still looks like average coverage, use `$master-shot-camera-planning` after any needed `$shot-information-progression` pass and before the full storyboard. It owns indispensable master-image selection and reverse-derived blocking, relationship axes, camera zones, shot-size/view-height reasoning, attention path, and connector constraints; `$professional-storyboard-director` still owns the complete board and `$cinematic-audiovisual-language` owns the general camera/continuity grammar.
- If the user supplies an existing song or `Audio1` and asks for the complete MV picture to be cut to it, especially dance/performance, performer-image identity, timecoded formation changes, insert clusters, or a final button, use `$reference-track-mv-director` when installed. Otherwise compose the same handoff with `$video-structure-design`, `$cinematic-music-sound-design`, `$character-continuity-bible`, `$action-rhythm-editing`, and `$seedance-audio`; do not block the MV workflow on the optional owner.
- If the user asks for 剧本, 故事, 人物动机, 冲突, 反转, 对白, 潜台词, 场景目标, 时间词, 情绪推进, or emotional hook, use `$screenwriting-story-craft`.
- If the user asks for 世界观, 美术设定, 场景设定, 城市设计, 视觉系统, 颜色体系, 反差背景, 道具/载具/服装设计, or says the world feels random or pasted together, use `$production-design-worldbuilding`.
- If the user asks to 展开一个世界, 做一组世界观图, 9张世界观静帧, 视觉文化板, infer a world from a reference image, or build a coherent imagined world before video/story, use `$mokeaigc-v9` before `$production-design-worldbuilding`; keep it responsible for still-image world evidence and visual laws.
- If the user mentions 怒戏/愤怒/暴怒/对峙, 哭戏/眼泪/情绪爆发, 哀伤/惆怅/孤独/不哭的悲伤, 喜戏/惊喜/欣喜, or 乐戏/嬉闹/玩乐/戏谑, use `$performance-scene-director` and select exactly one matching primary profile inside it. If the request is also 感情戏, 正反打, 暧昧, 告白, 和解, 诀别, 吵架, or 双人细腻表演, use `$relationship-dialogue-direction` after the emotion arc and before storyboard or platform packaging.
- If the user asks for 真人人物表演、表演风格、演员状态、潜台词、聆听、微表情、自然表演、表演僵硬、人物不会演、台词像念稿, use `$live-action-performance-direction`; if the request emphasizes emotional intensity,情绪递进、压抑/爆发、哭戏/怒戏/恐惧/羞耻/惊喜 or emotional continuity, add `$emotional-performance-direction` after the acting foundation.
- If the user asks for 风格化, 审美, 画风, 高级感, 视觉风格, 通用审美, or says the result is cheap/generic/aesthetically weak, use `$visual-style-aesthetic-direction` before material/render polish.
- If the user asks for 视听语言, 镜头设计, 轴线, 场面调度, 镜头组接, 景别, or says the camera design is weak, repetitive, or incoherent, use `$cinematic-audiovisual-language`.
- If the user asks for 影视级分镜、电影级摄影、摄影机参数、焦段、光圈、景深、布光、光影或摄影执行稿级描述, read `$narrative-camera-groups/references/film-level-shot-spec.md` and require per-shot camera, focus, and lighting fields before packaging.
- If the user asks only for 分镜, storyboard, shot list, or 镜头表, use `$professional-storyboard-director` as the visible output owner. If the user asks to turn any complete plot/script, connected sequence, local fragment, dialogue block, or continuation beat into AI-video storyboard prompts, use it for the shot plan, then let `$narrative-camera-groups` own the final visible package and the selected platform compiler compile each group's model-facing wording. Complete scripts use global grouping; fragments use scoped local grouping. Both routes end in a shot table plus one detailed six-part prompt per group.
- If the user asks for 高速战斗视觉母版, 激烈运镜, POV动作, 非常规构图, 多景别高速切换, 大画幅真人质感与动画夸张融合, giant/mecha combat, or a forceful opening style paragraph for an action prompt, use `$kinetic-action-visual-master` after aesthetic selection and before detailed shot design.
- For direct invocation without an `ExecutionPlan`, run
  `$cinematic-audiovisual-language` before material, tension, and
  model-packaging layers. When an `ExecutionPlan` exists, obey its exact
  required/forbidden list and return specialist field patches instead of
  expanding the route.
- If the user asks "找参考", "我不了解", "有什么现实参考", "给我搜/找例子", start with `$reference-hunting-board`.
- If the user supplies video links, Bilibili/B23 links, local video files, or prior successful clips and asks to 看看/拉片/整个都看/归类, start with `$reference-hunting-board` plus `$cinematic-audiovisual-language`; inspect the whole-work grammar or state access limits before transferring only selected pieces.
- If the user is building a recurring character, weapon, scene, short drama, series, or complains about drift, use `$character-continuity-bible`.
- If the user asks to control layout, blocking, color-board references, CAD references, front/back relationship, object footprint, long-axis direction, standing point, facing direction, or position drift, use `$character-continuity-bible` plus `$jimeng-sd2-prompting`; use `$cinematic-audiovisual-language` when translating the board into shots.
- If the user asks for Blender, 3D预演, previs, whitebox, blockout, camera path, animatic layout, or viewport reference renders for AI video planning, use `$blender-mcp-previs` when installed. Otherwise use layout/blocking references and `$cinematic-audiovisual-language`; state that the result is a shot plan, not a 3D preview artifact.
- If the user asks for 动作预演, mocap, BVH/FBX, Blender action preview, game-style / martial-arts / boxing / melee / weapon / stunt action previews, use `$mocap-action-previs` when installed. Otherwise use supplied motion evidence plus `$action-choreography-reference` and `$action-rhythm-editing`; do not claim sourced mocap validation.
- If the user mentions mechanical transformation, 机械变形, TF, 变形机甲, 载具变机器人, mecha transformation, 武器变形, 弓变形, folding/unfolding, telescoping, hinge, linkage, cam, pulley, lock, or deployable parts, use `$mechanical-transformation-design`; for vehicle-to-robot or mecha combat boards, use its imported TF mecha reference.
- If the user mentions fight, weapon, chase, slash, kick, throw, bow, staff, sword, chain, body motion, or "动作参考", use `$action-choreography-reference`.
- If the user specifically wants a Seedance/Higgsfield 打斗/格斗/武打/动漫战斗 prompt, or asks to fuse 动作、节奏、运镜、打击感 into one output, route to `$seedance-fight-director` as the direct fight-output skill; use its imported action systems for 起始态/终止态, A/B/C/D 动作分类, HEAVY/RUSH/CHASE 打点, or reference-material binding. Call `$action-choreography-reference`, `$action-rhythm-editing`, or `$seedance-camera` separately only when deeper diagnosis or reference extraction is needed.
- If the user mentions weapon weight, center of mass, balance, leverage, inertia, momentum, traction, recoil, braking, heavy weapons, strength differences, or says all martial arts look the same, route to `$action-choreography-reference` before rhythm and model packaging.
- If the user mentions rhythm, timing, beat, music, slow motion, impact frame, 卡点, 打击感, 起势/爆发/收势, use `$action-rhythm-editing`.
- If the user mentions 特效, VFX, 粒子, 光效, 魔法, 能量, 冲击波, 爆炸, 火焰, 烟雾, 水体, 破坏, 碎片, 武器轨迹, 拖影, 速度线, 变身生长, 特效廉价, 特效遮动作, or effects must carry force/state/transition, use `$cinematic-vfx-director` after the action/state and medium are clear. Use `$vfx-effect-construction-engine` for lifecycle, particle/energy/ritual grammar, source-to-endpoint construction, and precise term retrieval. For Seedance, then use `$seedance-vfx` only as the compact platform compiler.
- If the user asks for 影视级玄幻特效、电影级仙侠特效、古装玄幻合成、CG法阵/剑气/雷劫/空间裂隙, or says the effect looks low-quality/cheap, add `$cinematic-fantasy-vfx-director`; for CG-heavy energy/material systems also add `$cg-xianxia-vfx-design` before `$vfx-effect-construction-engine`. When the user asks for参考图片/高清特效图, read the fantasy reference board bundled with `$cinematic-fantasy-vfx-director` and return categorized source links with usage/copyright notes.
- Before delivering a final video prompt, apply Liu's default audio gate: use named dialogue/voice-over and source-coupled foley/SFX. Add music, score, ambience beds, or mood effects only when Liu or the authoritative script explicitly requires them. `$seedance-audio` is used only after explicit approval for an audio timing reference; `$action-rhythm-editing` owns physical timing and `$cinematic-music-sound-design` owns mix hierarchy.
- If the user mentions 配乐, BGM, 音乐, 主题动机, BPM, 配器, 和声, 音效, 声音设计, 声画关系, 环境音, 拟音, 静默, Suno, Udio, or the clip needs an audio plan, use `$cinematic-music-sound-design`.
- Use `$ai-material-realism` as a baseline only when it appears in the
  current `ExecutionPlan` or when this director is invoked directly. If an
  `ExecutionPlan` exists, do not load it from this keyword table a second time;
  apply only its approved material fields.
- For vehicle, chase, impact, or fast camera prompts, combine `$cinematic-audiovisual-language` for shot logic with `$ai-material-realism` for readable layer-based blur, light direction, reflections, contact shadows, and material response.
- If the user explicitly names 即梦/Dreamina SD2, use `$jimeng-sd2-prompting` as the platform compiler. If the user names Seedance 2.0/2.5, use `$seedance-20` as the sole platform compiler, including continuation, first/last frame, reference-to-video, edit/extend, platform/API facts, safety rewrite, or failed-output repair. Do not invoke both compilers for one final prompt unless the user explicitly requests a cross-platform comparison.
- If the user asks for 生成前检查, 提示词质检, prompt QA, 哪里会崩, 怎么拆段, 稳定性, or a final safety check, use the preflight profile already selected by `ExecutionPlan`; use `$ai-video-prompt-preflight` only for full-depth or explicitly exhaustive QA.
- If the work will be generated, reviewed, compared, or retried as a project, use `$creative-production-ledger` to bind the final prompt, reference roles, model/mode/settings, outputs, review evidence, and retry delta.
- If Codex/imagegen or TapNow will actually generate or download an output, use `$generation-asset-pipeline` when installed. Otherwise use `$creative-production-ledger` to retain the exact submitted prompt, reference roles, model/settings, original result path, and review outcome beside the media.
- If the user asks for 举一反三, 多想一步, 整体优化, 这个处理对不对, 还要不要做什么, or asks to optimize the whole workflow/skill/prompt system, use `$think-one-step-further` as the final reasoning and propagation layer.
- If the user says retry, not right, 崩了, 乱了, 人脸变了, 武器变了, 动作软, use `$ai-video-iteration-doctor`.
- If the user supplies a rendered video and says 看看, 检查, 验片, 逐帧, 抽帧, 穿帮, 两个主角, 站位漂移, 音画不同步, or asks what actually failed, use `$ai-video-output-review` before retry diagnosis.
- If the user says 这个效果好, 这次可以, 记住这个, 复盘, 沉淀, 做成案例, 下次沿用, 开源提示词, 完整工程, production breakdown, or a repeated failure reveals a stable mechanism, use `$creative-casebook`. For external cases, inspect the finished output and authoritative project package before promoting any rule.
- If a case lesson has clear evidence, conditions, failure boundaries, and future reuse value, use `$capsule-engine`; do not promote an ambiguous single generation.
- For durable evidence, route narrowly: exact generation attempt -> `$creative-production-ledger`; one inspected success/failure -> `$creative-casebook`; repeated or user-approved reusable rule -> `$capsule-engine`; stable preference/commitment/global operating policy -> Sophia memory / session state.
- For normal action-video prompt creation, use continuity + audiovisual shot grammar + visual/action/rhythm + material, then route to exactly one target-platform compiler. In Liu's short-drama mode, preserve complete per-group delivery; do not shorten the final prompt for convenience.
- For weight-sensitive action, insert an explicit action-physics block between audiovisual grammar and rhythm: actor/load relation -> support/center path -> mass distribution -> contact response -> braking/recovery.
- For any action-led clip, insert an action-grammar block before the event chain: primary basis -> visible signature -> recurring support/level/vector pattern -> recovery signature -> fantasy amplification.
- For character PV and action-showcase prompts, audit the ending before delivery: the strongest action or reveal should not resolve into a static hero pose before the last 1-1.5 seconds unless portrait/fashion stillness is the explicit goal. If the final pose starts too early, add or move a mid-late action/state-change beat instead of extending the beauty hold.

## Route Maintenance

Before a major routing update, run `python scripts/validate_routes.py`. Treat an unresolved required reference as a routing defect. Optional capabilities may remain uninstalled only when the documented fallback preserves a usable workflow.

## Output Shape

For exploration:

```text
意图判断：
推荐路线：
1. 联网研究：
2. 视频结构：
3. 剧作/人物：
4. 美术世界：
5. 视听语言：
6. 音乐与声音：
7. 参考方向：
8. 连续性锁定：
9. 动作/节奏：
10. 材质真实感：

可选方向：
...
```

For final prompt, the visible planning notes may stay brief. Every script-derived camera group, including a group built from a local fragment, uses Liu's six-part order: 角色/资产锁定 -> 视觉材质总控 -> 镜头语言总控 -> 事件节拍 -> 声音 -> 正向稳定约束. Keep the shot table outside and give every group its own complete block. Inside `事件节拍`, create one visibly separate block per shot: `镜头01｜起始-结束s`, then the full shot setup, then its `T=起始-结束s` micro-beat lines. Never merge several shots into one unlabeled event paragraph. Restate every shot with timecode and duration, shot size, local camera position/height/angle, focal length or perspective, aperture/depth-of-field and focus subject, lighting direction/quality/color temperature/shadow behavior, camera movement and path, concrete action/performance and verbatim authoritative dialogue, cut trigger, ending state, and handoff. Every section must contain useful current-group controls; headings alone fail. Never substitute `同上`, `沿用`, `参考镜头表`, `保持不变`, or equivalent cross-reference wording for details. Each block must be independently copyable and generatable. Within each shot's event prose, add contiguous `T=起始-结束s` micro-beats on the camera-group timeline; each T range carries one observable action, performance, camera change, sound sync point, or state result and covers its parent shot exactly.

For final prompt:

```text
意图判断：
需要你确认：（只有关键不确定时出现）
创意判断：
联网研究：
调用层：
视频结构：
剧作核心：
时间铰链：
美术世界：
视听语言：
音乐与声音：
参考板：
连续性锁定：
机械变形：
视觉参考：
素材准备：
动作参考：
节奏设计：
材质控制：
生成前质检：

参考音频：（仅在 Reference Audio Gate 触发时出现）
- 文件：<真实本地 WAV 路径>
- 目标片长：<秒>
- 节奏点：<简洁 cue 表>
 - 上传音频：@节奏参考.wav（画面节奏控制参考；最终混音另行处理）

【完整可复制提示词】（独立代码块，只放模型提示词）
【角色/资产锁定】
@实际图片名（...参考）：...  # 使用用户上传的真实图片名，保留@前缀
【视觉材质总控】
...
【镜头语言总控】
[complete whole-film camera style: named aesthetic anchors + perspective + lens family + distortion + movement energy + framing/edit rhythm + reveal logic]
【事件节拍】
[action/state/contact/consequence beats; add a trigger + visible-result camera clause only for a genuine special-camera beat]
【声音】
...
【正向稳定约束】
...

下一轮只建议调：
...
```

For short answers, output only the final prompt plus the most important reference choices. If the Reference Audio Gate triggered, the reference WAV path and compact cue map are mandatory even in the short answer.

## Quality Bar

- Every substantial director-mode response starts from Phase 0 intent reading, even if the visible answer only shows one concise `意图判断` sentence or uses the inference silently.
- Apply the Non-Self-Deception Gate: never invent unseen references, fake inspection, fake current facts, fake prior context, exact timing, model behavior, or user taste evidence. Ask Liu when the missing information changes the core result.
- The final prompt must read like a director describing one shootable clip.
- The first substantive creative block of the final prompt must establish the global visual master. Detailed shots may vary scale and angle but must not reopen the medium, palette, material, or rendering decision.
- Treat masters as high-level invariants, not as long paragraphs. Keep one compact visual/material master and one compact camera master; later beats inherit them and describe only temporal change. Precision is decision density, not word count.
- Before packaging specialist outputs, choose one primary fidelity spend and one secondary spend. Compress or omit every layer that does not change the visible result; never concatenate every specialist recommendation into the final prompt.
- Under a hard character budget, preserve identity, world-identity packet, event path, coverage-critical cuts, and end state before decorative adjectives, repeated render synonyms, broad stability boilerplate, lore explanation, secondary flourishes, or unsupported weapon actions. If a supplied environment reference already carries the world, replace the text packet with one explicit reference-role lock rather than duplicating it.
- For I2V/R2V, let inspected references carry spatial appearance and layout. Use text mainly for motion, timing, camera path, sound, and endpoint instead of re-describing the image.
- For aggressive action, the visual master must bound camera behavior: every move or cut has an action, occlusion, gaze, impact, or spatial trigger; unconventional framing never licenses random rotation, axis loss, or unreadable geography.
- Research must alter at least one meaningful creative or feasibility decision for substantive prompts; do not add sources as decoration.
- Original designs must show sedimentation: the viewer should be able to infer some culture/craft/material/professional/social/action lineage from silhouette, costume construction, weapon function, location rules, palette ownership, and positive stability locks.
- Preserve deliberate director, studio, film, genre, cinematography, martial-art, dance, sport, and movement-system names as compact semantic anchors. Add minimal visible camera/body/material language only to disambiguate intent or prevent a known failure; do not replace one useful term with a diluted paragraph.
- Do not make the user supply the complete reference vocabulary. State what their anchors cover, supplement the missing high-value roles, and keep the final set compact and compatible.
- Avoid name salad. Keep at most 2-4 named references per shot unless the user is brainstorming a library.
- Keep one main action per 5-second clip; split longer action into beats.
- For weighted action, retain the named technique or movement basis and bind it to the required physical profile. The name supplies movement identity; support, mass distribution, contact response, and recovery keep it physically credible.
- For aesthetic action, every event chain must inherit a movement grammar; “run, climb, attack, block, slash” alone does not pass the quality gate.
- Lock identity/weapon/scene before adding heavy action or camera movement.
- Define the macro video structure before writing shots; shots should serve hook, orientation, build, turn, payoff, or loop.
- For story-driven clips, define want, obstacle, choice, and consequence before shot language.
- For emotion-driven clips, define the temporal hinge before shot language: past residue -> present action -> incoming pressure -> final consequence.
- For emotion-driven clips where acting is the main value, let `$performance-scene-director` own the shared acting arc, and let exactly one emotion profile wrapper own the intensity ceiling and micro-action flavor; camera and sound should support that playable arc.
- For world-driven clips, define color ownership, material rules, location function, and forbidden drift before shot language.
- For world-first development, use `$mokeaigc-v9` to create/inspect the 9-still world board, then carry forward only stable visual laws into video packaging.
- For multi-shot clips, run audiovisual continuity before adding tension effects.
- Audiovisual grammar is the first visual quality gate: each beat needs function, shot size, camera position, camera movement path, tracking owner, screen direction, continuity bridge, and cut reason before material, tension, or SD2 packaging is added.
- For video prompts, reject “good storyboard but no motion” outputs: if the sequence could be generated as still frames with hard cuts, add motivated camera movement, action-camera coupling, or a deliberate lock-off rationale.
- Run an anti-repetition pass: adjacent shots cannot share the same shot size, camera height, action verb, and motion direction unless the repetition is the intended concept.
- Every beat should have this internal shape: function -> visible image -> camera behavior -> motion/transition -> continuity lock. Outside the narrative-camera-group workflow, an individual cut gets an exact timestamp only when synchronization or edit control requires it. Inside that workflow, exact per-shot timing is part of the user's delivery contract and must be physically audited.
- Audit duration at four levels: total clip duration, segment allocation, structural peak placement, and physical action-phase timing. Convert high-confidence segment allocation into prompt ranges when useful; keep micro-shot duration flexible by default.
- When audio matters, every major beat should identify its sound focus, cue change, or intentional silence; do not synchronize every cut mechanically.
- Run preflight before final delivery when the prompt is long, multi-shot, action-heavy, reference-heavy, or intended for immediate generation.
- For reference-based generation, state which assets already exist, which are required, which are optional, and the exact role of each asset before presenting the final prompt.
- For high-speed shots, do not leave motion blur as a generic adjective. Specify what stays readable and what blurs: hero subject, vehicle silhouette, background streaks, foreground wipe blur, wheel rotation blur, light trails, and shutter feel.
- For transformation shots, every new part must have a visible source: hinge, rail, nested segment, linkage, cable, cam, or latch.
- Put consistency locks and positive video stability locks at the end through the one selected platform compiler, then check them with the matching preflight profile.
- When uncertain, give 2-3 route options instead of pretending one path is objectively best.


## High-Speed Flight Reference Rule
For extreme high-speed flight, ascent, dive, dash, or fall prompts, never describe only the subject. Add visible spatial references: ground shrinking away, treetops whipping past, cloud layers being pierced, debris lagging behind, foreground objects crossing frame, and a clear wide/close rhythm. Use ultra-wide shots for scale and extreme close-ups for speed pressure. Transformation details should occur during motion unless the user requests a display; reserve the readable full form for the final hover or impact pose.

## Negative-Hygiene Preflight For Motion Prompts
Before adding positive stability locks, remove positive phrases that can summon the wrong result. For vertical ascent/dive, avoid camera wording that implies parallel horizontal pursuit, such as following behind/side-behind through trees. Replace with visible vertical references: ground rapidly shrinking below, tree crowns becoming a flat texture, cloud hole opening above, vertical parallax, falling debris lagging behind, ultra-wide distance proof, and close-up motion-blur inserts. Negatives cannot override a stronger wrong positive camera instruction.
