---
name: jimeng-sd2-prompting
description: "Platform-language compiler for an explicitly selected Jimeng/Dreamina/即梦 SD2 target in a standard/full ExecutionPlan, including its UI-specific reference, layout, prompt, and temporal-hinge behavior. Do not trigger merely because a request says Seedance, 分镜, 运镜, or AI视频提示词; Seedance uses seedance-20, and low-risk Seedance camera groups use seedance-camera-group-compiler-fast."
---

# Jimeng SD2 Prompting

For Liu's live-action short-drama workflow, follow
`../ai-video-production-governance` and
`../director-workflow-70/references/short-drama-director-stack.md` as the
upstream orchestration contract. Every script-derived input preserves the
selected concept or local scope, camera-group boundaries, per-shot durations,
and detailed six-part prompt order. A complete script uses global grouping; a
local fragment or single continuation beat uses scoped local grouping. Act only
as the platform-language compiler.

## ExecutionPlan Compile-Only Mode

When `ExecutionPlan.platform_compiler=jimeng-sd2-prompting` and approved
`StoryContract`, `ShotLedger`, and `CameraGroupPlan` already exist, skip the
general intake, prompt-workbench, story diagnosis, research, and alternate
output routes below. Consume only those structured objects, current
continuity/asset locks, accepted specialist field patches, audio authority, and
any existing `ResearchReceipt`. Compile each camera-group prompt once, using
exact 即梦 handles, and record `compiled_by=jimeng-sd2-prompting` plus
`compile_count=1`. Preflight returns field patches to this compiler and never a
second full prompt.

For a script-derived camera-group `ExecutionPlan`, before compiling, call
`skill_console_prompt_compilation_context` with the
current `threadId` and approved state slice. Re-read the task settings for each
generation group and retry, and treat the returned `processing_depth`,
`prompt_description_complexity`, and `prompt_compilation_profile` as
authoritative. After the 即梦 six-part block is written, call
`skill_console_compile_prompt` exactly once with
`compiler=jimeng-sd2-prompting`; use the returned `promptText` verbatim and
carry its `generationSettings` and `compilationReceipt` into the matching
`PlatformPromptSet` unit. If the call fails, block handoff
instead of emitting a stale or unprofiled prompt.

The profile is binding for script-derived camera-group prompts: `low` uses
simple shot wording, no duration limit, and
no `T=` lines; `medium` uses simple shot wording with duration limits and no
`T=` lines; `high` uses complex shot wording with duration limits and contiguous
`T=` micro-beats. All three retain the six sections, exact dialogue, and complete
structure. `processing_depth` changes backstage orchestration only.

Direct image prompts, standalone non-script video prompts, troubleshooting, and
other tasks outside the camera-group route do not use this task-bound profile;
keep their existing 即梦 behavior.

Repeated script or script-fragment input is routed again with a fresh settings
read. Multiple outputs for one group require an explicit user request and
distinct `variant_id` values; compile and receipt each requested variant once.

This compile-only branch takes precedence over the rest of this file. For a
camera-group `ExecutionPlan`, do not run the prompt workbench, story diagnosis,
research, alternate output, or global `think-one-step-further` pass. Check only
即梦 syntax, reference/character handle mapping, selected mode compatibility,
and compiler hygiene, then return the single compiled prompt or a named field
patch.

## Direct Invocation Reasoning

Apply the `think-one-step-further` mechanism only for direct invocation or when
the execution plan explicitly sets `global_reasoning=delta-only`:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Core Intent

Use this skill to turn loose visual ideas into controllable 即梦 SD2 / Seedance 2.0 prompts. Treat the model like a director-level multimodal video system: define references, subject, action, camera, light, rhythm, sound, and constraints.

Default to Chinese prompts for 即梦 UI unless the user asks for English. Keep prompts production-ready, compact, and directly pasteable.

## First Decision

Liu override: every script-derived request is downstream of
`$narrative-camera-groups`; completeness beats compactness. Emit one standalone
detailed six-part prompt per 14-28 second group and preserve all required fields
from the upstream contract. Record `TaskEnvelope.output_format = six_part` for
both complete-script and local-fragment routes.

Choose the output type:

- **Text-to-video**: no assets; build scene, action, camera, and style from scratch.
- **Image-to-video**: user has one image; preserve identity/composition, add motion and camera.
- **First/last-frame video**: user has start/end frames; describe transition, path, and what must stay consistent.
- **Multi-reference**: user has images, videos, or audio; explicitly assign each reference role.
- **All-material / all-reference**: user wants SD2/Seedance to read many references. Build a reference-role table before the prompt; text is glue, not the only controller.
- **Multi-segment stitching**: user wants several generated segments. Separate shared locks from segment-specific prompt blocks; do not cram one long film into one fragile prompt.
- **Prompt workbench output**: user wants a directly usable prompt but also needs preparation clarity. Output generation mode, asset-role map, a standalone full copy block, and preflight notes in one package.
- **Shot list**: user wants a sequence; write ordered prompts. When `$narrative-camera-groups` is active, preserve its required exact per-shot seconds in the model-facing event prose.
- **Prompt diagnosis**: explain why the current prompt may cause drift, weak motion, or fake visuals, then rewrite.

## User Workflow Defaults

- Default to Chinese, paste-ready output.
- Default one generation unit to one standalone copyable block. For
  `$narrative-camera-groups`, compile one complete block per group and preserve
  the human shot table outside every block. Put each group's positive stability
  locks inside its own block; keep diagnostics and risk notes outside. All
  script-derived groups, including local fragments, use the six-part block.
- Act as the platform-language compiler, not the narrative delivery owner. Preserve camera-group boundaries, durations, shot order, and visible output format supplied by `$narrative-camera-groups`; compile the contents of each group without merging groups or replacing the table/prompt separation.
- For Liu's final prompt format, use the exact uploaded name-based handles
  `@图片名`、`@视频名`、`@音频名` for references supplied alongside the script.
  The first mention must immediately carry a parenthesized role scope. Do not
  output generic replacements or invented names. `{{Image N}}`、`{{Video N}}`、
  `{{Audio N}}` are backend mapping only. The six paste-ready headings apply to
  every script-derived camera group, including local fragments. Internally
  retain the stable `asset_id` and role, then compile to the exact platform
  handle.
- When the user has uploaded named five-view character assets, every character mention inside the copy-ready prompt uses the exact platform handle `@角色名` (for example `@苏凌月`, `@苏建国`, `@刘大龙`). Apply it in identity locks, event beats, dialogue speaker labels, sound, and stability locks. Keep named reference files in the separate exact `@图片名` / `@视频名` / `@音频名` format; do not confuse `@角色名` with file handles.
- When upstream skills use imported `@material[...]` terminology, treat it as an internal reference-role concept only. Convert final paste-ready output to Liu's exact name-based `@图片名` / `@视频名` / `@音频名` handles while preserving the same asset roles: identity, environment, motion, style, material, layout, or endpoint.
- For whitebox, Blender previs, or mocap reference videos, map the exact uploaded `@视频名` as action and shot reference only: it controls action rhythm, body weight/center, camera scale, shot-size changes, cut logic, and transition triggers. It must not control final character design, materials, scene, white-model/capsule look, grid floor, time labels, debug markers, or viewport preview lighting.
- For Liu's explicitly requested 15-second素材段 or short validation test, do not turn every prompt into a complete finished mini-film: choose one segment purpose and 3-4 required state changes. For script-to-camera-group work, defer to `short-drama-director-stack.md` and `$narrative-camera-groups`: use 14-28 second groups, exact per-shot durations, one complete prompt per group, and the default dialogue/foley audio contract. If the target is edit material, optimize for several strong usable shots instead of forcing an 8-beat storyboard to appear in order.

- In Liu's default audio mode, write named dialogue/voice-over and dry source-coupled foley/SFX. Add music, score, BGM, ambience beds, or mood effects only when Liu or the authoritative script explicitly requires them. Keep absence rules backstage; the `声音` block lists only sounds that are present.
- Organic skill linkage is mandatory for substantial prompts: structure first, continuity/reference roles second, audiovisual/camera grammar third, aesthetic/material/action/rhythm layers after they have a clear job, and SD2/Seedance packaging last. Do not paste independent skill outputs together. Compress them into one coherent prompt where every layer serves the same segment objective.
- Before writing ordered beats, declare the clip mode internally and let it govern the prompt: character PV sells identity/expression/attitude/signature prop; pure action showcase proves a weapon or ability through state changes; fight/duel proves initiative and response; image-only design should not contain video action.
- For new clean-slate prompts, run a contamination pass: remove prior project-specific props, motion modes, enemies, locations, palettes, and old failure terms unless the user explicitly reuses them. Keep only general stability constraints.
- Run a keyword-contamination pass whenever a prompt uses negation, correction language, loaded role labels, camera labels, or abstract action/intent words. Do not keep a fixed blacklist from prior examples. For the current prompt, infer which nouns or verbs carry a strong unwanted association cluster, then replace them with positive visible evidence of the desired frame.
- Treat context rewrites and exclusion wording as the highest-risk contamination points. Do not use the exclusion prompt to explain the old wrong image, and do not rewrite by saying "not the old context." Convert both into current positive visual facts. For Liu copyable prompts, translate every risk into current positive visible facts and stability locks before delivery.
- When changing context, reset the frame instead of contrasting with the previous one: write the new subject, environment, prop state, action path, palette, camera relation, and visible constraints as if the model has no memory. Remove old nouns unless they are still physically present in the desired shot.
- Treat abstract relations as weaker than visible evidence. If a word describes intention, attention, role, task, absence, or camera concept rather than pixels, translate it into what the lens can actually see: which side/surface is visible, which part is hidden, what the hands/body/object are doing, what occupies the foreground/background, how large the subject is in frame, and which material/edge/light cues prove the angle.
- To control camera distance or angle, allocate descriptive attention to the surfaces that would appear from that view. For closer framing, bias toward small surfaces, facial/hand/prop details, reflections, seams, texture, and partial occlusion; for wider framing, bias toward floor footprint, surrounding set pieces, horizon, scale relation, and subject frame occupancy; for top/back/side views, bias toward the specific top/back/side surfaces, shadows, overlaps, and hidden/revealed edges that prove the view.
- Put a compact global visual master near the beginning of the final prompt, after reference-role declarations when references exist and before shot-by-shot detail. This block controls the whole clip: medium domain, aesthetic family, palette ownership, line/shape language, material-light rules, rendering hierarchy, optical character, and forbidden style drift.
- Put a compact global camera / shot-style master immediately after the visual
  master for every substantial AI-video prompt. It owns perspective, lens
  family, distortion, movement energy, shot-size range, framing/edit rhythm,
  transition language, and reveal logic. Keep named film, animation, director,
  cinematographer, studio, or work anchors backstage by default and translate
  them into those visible mechanisms. Include names only when Liu explicitly
  requests them and the platform/safety contract permits them. Do not use name
  salad or generic "dynamic camera". Place the master before timed beats.
- Event-beat camera sparsity gate: `事件节拍` inherits the global camera master. Normal beats write action, state change, contact, consequence, and handoff without repeating style names, lens vocabulary, or routine movement grammar. Add a local camera clause only when a beat needs a genuine special device—FPV dive, extreme-perspective rupture, weapon-to-lens pass, impact lock, distortion surge, overhead reveal, POV switch, or transition—and state the action/impact/occlusion trigger plus concrete visible result. The local clause must remain compatible with the master.
- Liu mandatory video-prompt architecture: reference locks first; then global visual/material/light master; then global camera/storyboard master; then event beats. Do not make "first-frame state" a separate front block inside the final paste prompt unless the user explicitly asks for a first-frame asset note. Put the first visible state into the opening event beat, e.g. "开场：第一帧就是...". Platform hard parameters such as duration/aspect ratio should be omitted when the user says they will set them separately. The final stability section should be short, positive, and targeted to proven drift risks.
- Run a paste-ready self-check immediately before the final copy block. The model-ready prompt must contain only generation-facing controls: reference locks, global visual/material/light master, global camera master, required event/state changes, and short positive stability locks. Remove internal QA language, workflow explanations, excessive named anchors, repeated anti-cheapness lines, generic exclusion spam, and nonexistent reference placeholders. If a note is needed for the user, put it outside the copyable block.
- For Liu's copyable prompts, assume each generation is stateless and has no conversation memory. The paste-ready prompt must be self-contained through references and visible scene facts, but must not mention conversation continuity such as "延续前面片子", "上一段", "之前", "现在这个", "已经脱离", "不要像上次", or "本段". Convert these into direct visual rules: e.g. "高级CG巫女怪谈电影质感", "怪物以蛇形妖物方式运动", "开场为湿石倒影极近特写". Do not describe prior failures inside the copyable prompt; write only current visual rules and stability locks.
- For multi-segment continuation, treat continuity-dodge reasoning as internal planning, not final prompt text. Do not write meta lines like "do not hard-match the previous final frame", "avoid mismatch", "do not replicate the last composition", or "carry story state not exact frame" inside the paste-ready prompt. Translate that reasoning into concrete filmable instructions only: a new shot size/angle, insert, occlusion, foreground wipe, smoke/dust/sound bridge, impact bridge, or a chosen reference transition, plus the visible current fact such as "the monster is already in a hunting posture" or "the character is already transformed".
- Before writing camera/action beats for a stylized video, map the visual style to a presentation bias: which shot rhythm, motion density, transition type, and PV/showcase balance the style naturally favors. This is a weighted tendency, not a hard restriction. If the prompt borrows a non-native form such as live-action handheld for ink wash or comic impact frames for cinematic realism, state the borrowed layer's job and keep it subordinate to the base style.
- Do not launch research from this compiler. When the full-depth
  `ExecutionPlan` includes `$creative-research-first`, consume its
  `ResearchReceipt`; otherwise compile from approved local state. Escalate
  unresolved platform capability claims to the router instead of researching
  them a second time.
- Every video prompt needs audiovisual grammar before render polish: shot function, spatial path, blocking, axis/screen direction, camera relation, and cut logic must be readable before ordered beats.
- For emotion-driven or story-driven prompts, include a temporal hinge line before ordered beats: "角色刚刚..., 正在..., 即将...". This gives the model a natural behavioral slope instead of a flat emotion command.
- Every visual prompt needs an aesthetic direction layer and a material/light/render layer by default. Do not wait for the user to ask for texture. After the audiovisual scaffold is clear, include medium domain, style rules, rendering hierarchy, visible materials, light direction, AO/contact shadows, reflection/roughness/texture response, optical behavior, and fake-look avoidance before final packaging.
- If the user uses SD2 全能参考, declare every uploaded image/video role before the prompt:
  - identity/outfit
  - vehicle/prop
  - environment/palette
  - scene layout
  - motion/camera
  - texture/material
- If a reference is only for style or mood, explicitly say "do not copy text/layout/identity from this reference".
- Before a final reference-based prompt, inventory what the user already has and what is still missing. Separate required assets from optional enhancement assets; do not make the user infer the preparation list from the prompt.
- For standalone generation, write the first-frame state directly inside the opening event beat: "开场：第一帧就是..." or "开场：画面已经处于...". Do not rely on conversation history such as "上一段之后", and do not isolate the first-frame state as a detached instruction block when the user wants a natural paste-ready prompt.
- For ordinary 15-second prompts, decide timing confidence and normally reserve exact ranges for supported segments or synchronization. For `$narrative-camera-groups`, retain the user's required exact per-shot duration and rewrite each shot as concrete prose inside `事件节拍`; audit dialogue speed, action phases, and total duration before compilation.
- For one-scene clips, add a fixed blocking paragraph before ordered beats: where the main background, character, vehicle/prop, screen panels, and action path stay in the 16:9 frame. Use "同一场景、同一轴线、同一空间关系" language.
- When using a reference to control position, name it `layout/blocking reference`: it controls relative positions, scale, left/right relationship, and camera framing only. It must not override identity, outfit, rendering style, palette, or lighting unless explicitly assigned.
- For strong blocking control, allow an abstract color-board / CAD-style layout reference. Treat it as a spatial control map, not a visual style reference. It may define color blocks, zones, arrows, object footprints, front/back layer, long-axis orientation, facing direction, gaze direction, action path, target points, and optional camera direction.
- If a layout reference contains labels, prefer a clean no-text version for model upload and keep the labeled version only for human checking. In the prompt, explain what each color/shape means.
- For elongated objects such as vehicles, long props, tables, doors, platforms, screens, bridges, or weapons, do not describe only "near the character". Lock the object's footprint, long axis, front/nose/end direction, and whether it is in front of, beside, or behind the subject.
- When the user asks for 光影, 打光, 质感, 真实感, 渲染, 游戏渲染, PBR, AO, 环境光遮蔽, 各向异性高光, 运动模糊, 速度感, or high-speed vehicle/action shots, first lock shot function and spatial/camera logic, then include a separate material/light/render/motion-realism layer. State what stays readable, what blurs, blur direction, light source direction, AO/contact shadows, reflections, roughness, anisotropic highlights, and material response.
- For camera changes inside one scene, use wide shots to establish position and close-up/insert/occlusion shots to hide minor position drift. Do not force every close-up to restate full geography.

- For fantasy powers such as shadow, qi, cursed energy, psychic force, magic, or elemental force, define the power's visual ownership, source, function, and consequence, but leave micro-mechanics open unless the user asks for exact design. Avoid over-writing a fragile mechanism list. A good control line is: "the power serves [stealth / misdirection / pressure / protection / displacement], emerges from [motivated source], appears as [visual behavior], and causes [clear state change]."
- For shadow / darkness powers specifically, do not default to blue, purple, neon, smoke, or black-screen effects. Unless the user asks otherwise, treat shadow as near-colorless light absorption: swallowed highlights, delayed silhouettes, broken reflections, matte black shape fields, and local exposure drop. For Liu copyable prompts, describe shadow as near-colorless light absorption, swallowed highlights, delayed silhouettes, broken reflections, matte black shape fields, and local exposure drop.
- For clean-slate tests, do not include positive stability locks that name prior project-specific characters, scenes, props, monsters, or failed concepts. Keep only positive stability locks relevant to the new test. If the user wants to test action, do not spend prompt budget on broad lore; keep setting simple and allocate detail to movement, angle, contact, reaction, and changed state.
- For complex action prompts, action retries, or when the user asks for a directly copyable prompt, use a hybrid format by default: natural-language role/style/scene lock first, then a compact JSON-like action state machine inside the same paste-ready prompt. Use JSON-like structure as an organization aid, not as a magic mode. Keep it short enough to remain executable: prefer `core_rule`, `spatial_rules`, `action_beats`, and `positive_stability_locks`; add `continuous_state`, `camera_logic`, or `effect_rules` only when they prevent a proven failure. Each beat must specify action, camera, and `state_change`. Use this to lock force direction, front/back relations, receiver state, contact proof, and no-reset constraints. If a JSON-like attempt makes action worse, causes subject reset, or turns the receiver into a posed target, reduce the JSON to 3-5 macro beats, reduce repeated stability wording, and/or split the action into multiple clips rather than adding more fields. Keep positive stability locks inside the same copyable block; put risk explanations outside the paste target.
- For AI action generation, do not over-choreograph every micro-action by default. The model often performs better when the prompt controls only the necessary boundaries: global visual style, fixed spatial relationship, movement grammar, the receiver's state, 3-5 required state changes, camera proof points, and hard failure bans. Leave secondary hit shapes, exact limb choices, and internal cut timing for the model to improvise unless a reviewed failure proves that one detail must be locked.
- For character PV prompts, do not accidentally turn the clip into a pure action showcase. A PV may contain action, but its primary job is to sell the character: identity, body type, color ownership, attitude, facial expression, signature prop/weapon, personal visual rhythm, and one memorable final icon. Structure character PVs around entrance/presence -> personality reveal -> signature motion or prop proof -> style-specific transition -> short payoff, rather than continuous attacks from start to finish.
- For character PVs, bind camera, transitions, motion density, and expression to the specific character instead of reusing one universal action-template. A playful rogue needs glances, smirks, misdirection, and quick off-axis cuts; a sunny extrovert needs open body language, bright graphic wipes, and confident eye contact; a cold character needs stillness, controlled close-ups, and restrained movement. Prompt facial performance explicitly with 2-4 expression beats such as glance, smirk, narrowed eyes, breath, eye contact, or micro-reaction, and prevent the face from being hidden by constant motion blur.
- For PV/action hybrids, state the intended action density. Example: "PV first, action second: first 2-3 seconds sell face/body/attitude; middle proves signature weapon; last 1 second forms the poster icon." If the previous output entered the poster icon too early, move the static pose to the last 1-1.5 seconds and add one more mid-late state-change beat.
- For high-tension action camera, build 4-6 backstage proof points—stillness-before-burst, contact-proof extreme close-up, ground/foreground rupture, vertical-axis proof, extreme-wide scale proof, consequence/recovery framing—then compile the default camera grammar into `镜头语言总控` once. Event beats inherit it; only a special-camera beat states its trigger, movement, proof job, and visible result locally.
- For motion trails and VFX, do not write generic "运动模糊/速度线/残影/特效" as interchangeable decorations. Classify the trace as photographic motion blur, animation smear, afterimage/pose echo, graphic speed/focus lines, impact frame, physical debris, energy/ink/brush trail, or foreground wipe; define its source anchor, layer/depth, direction, duration, what stays sharp, what it proves, and how it decays.
- When the same action prompt produces widely different outputs across seeds, treat it as an over-open or internally conflicted prompt. First remove contradictions between "free camera/free action" and locked shot timing, reduce the clip length or split the sequence, and lock only the essential action-state transitions. Do not add more adjectives or more exclusion clauses before resolving the positive-side conflict.
- If a prompt says effects are restrained but also names a mythic creature or large special effect such as dragon, phoenix, giant aura, or energy beast, choose one role explicitly. Either make it the primary spectacle, or downgrade it to an abstract motion-path / pressure silhouette / negative-space trail. Do not ask for "克制" and a large literal creature-effect in the same beat unless the user deliberately wants that contradiction.
- When the user supplies deliberate director, cinematographer, studio,
  animation, manga, film, or shot-style references, preserve them in backstage
  analysis and assign each a distinct function. Translate the result into
  concrete suspense, scale, speed-ramp, action-clarity, mechanical-insert, hero-
  pose, transition, material, impact, verticality, or transformation behavior.
  Repeat names inside the final prompt only when the user explicitly requests
  named references and the platform/safety contract permits them.

For prompt architecture, camera vocabulary, and examples, read `references/prompt-architecture.md` before doing substantial prompt writing.

## Generation Mode Packaging

Before writing a final SD2 / Seedance prompt, choose and state the generation mode. This mirrors real prompt workbenches but keeps the reasoning under Codex control:

```text
生成模式：纯文本 / 图生视频 / 首尾帧 / 全素材参考 / 多段拼接 / 提示词诊断
时长与比例：[duration, aspect ratio]
素材映射：
  @图片名（[identity / outfit / style / material / scene / first frame / end frame] 参考）：...
  @视频名（[motion-camera / action rhythm / edit logic] 参考）：...
  素材职责：[...]
  迁移范围：[...]
缺失素材：必需[...]；可选增强[...]
```

Default final packaging for directly copyable output. Generation mode and asset
inventory may appear as short planning notes outside the paste target. A
script-derived camera-group unit gets one standalone code block using the
six-part contract; a `$narrative-camera-groups` package therefore gets one block
per group, including scoped groups built from local fragments.
Do not add `生成模式` or a detached `素材映射` as extra prompt sections:

【完整可复制提示词（单独复制下面代码块）】

```text
【角色/资产锁定】
@图片名（...参考）：...
【视觉材质总控】
...
【镜头语言总控】
X风格 + [全片可见镜头结果]；...
【事件节拍】
...action/state/contact/consequence beats; only a genuine special-camera beat adds its trigger + visible camera result...
【声音】
...
【正向稳定约束】
...
```

【生成前质检】
...

If the user says “直接给我全部”, “完整复制”, or “以后都这样”, provide all useful sections, but keep `【完整可复制提示词】` as a separate code block. Put the positive stability locks inside that code block and keep any commentary outside the block very short.

Mode-specific rules:

- **纯文本**: do not invent unavailable references. Use first-frame state, global visual master, action/camera rules, and positive stability locks.
- **图生视频**: identify what the image locks and what may move. Do not ask for a new costume, new face, or unrelated camera angle unless the user wants transformation.
- **首尾帧**: describe the visible transition path and continuity locks between frame A and frame B; avoid adding a third unrelated scene.
- **全素材参考**: every asset needs one primary role. If one asset has two roles, name the priority order. For motion/camera reference videos, record the time range or segment role when known.
- **多段拼接**: write shared locks once, then segment prompts. Each segment needs its own first state, end state, and handoff state.
- **续段转场**: internally carry the previous clip's story state, not its exact final-frame composition; in the final prompt, write only the concrete transition shot and the visible current state. Avoid meta-production phrases. Example final wording: "开场：湿铁轨极近特写，刀尖低垂，烟尘擦过镜头；切到越肩，怪物已经在前方压低车头进入捕食姿态。"
- **提示词诊断**: separate workflow failure from prompt wording failure. If reference roles or mode choice are wrong, fix that before rewriting adjectives.

## Default Workflow

1. Extract the creative objective: subject, story beat, output platform, duration, aspect ratio, and whether audio/dialogue matters.
2. Consume an existing `ResearchReceipt` when selected by the upstream full
   route; otherwise do not add a research pass.
3. Inventory available and missing references, then assign roles: identity/outfit, vehicle/prop, environment/palette, layout/blocking, style/material, motion/camera, audio, first frame, last frame.
4. Write the final prompt in layers:
   - subject and locked identity
   - reference roles and fixed blocking/layout if references exist
   - global visual master: medium, aesthetic family, palette ownership, line/shape language, material-light system, rendering hierarchy, optics, forbidden drift
   - global camera / shot-style master: named anchors with functions, shot-size range, camera family, special storyboard method, cut/transition logic, and proof jobs
   - continuation bridge when relevant: internally decide the previous story state and the chosen transition/shot-size dodge; final prompt states only the filmable opening shot, visible current state, and new action pressure
   - event beats: the opening beat contains the first visible state; later beats contain the action result chain
   - temporal hinge only when it helps emotion or story: just happened, present action, incoming pressure/reversal
   - audiovisual shot grammar inside each event beat: shot function, spatial path, axis/screen direction, camera relation, and cut logic
   - action physics when relevant: actor-to-weapon strength, center/base of support, mass distribution, force chain, contact response, braking, and recovery
   - material/light/render/optical realism baseline: AO/contact shadows, PBR roughness/specular/metallic behavior, anisotropic highlights, GI/bounce light, volumetrics, DOF, motion blur where useful
   - action progression
   - environment and production design
   - camera movement and framing
   - music, sound focus, ambience, effects, silence, or dialogue; use `$cinematic-music-sound-design` when audio matters
   - consistency and positive stability locks
5. For clips over 10 seconds or multi-beat ideas outside `$narrative-camera-groups`, choose one:
   - high-confidence: exact segment ranges, flexible internal cuts;
   - medium-confidence: approximate ranges or proportions;
   - low-confidence: untimed ordered segments.
   Exact micro-shot times remain exceptional. In `$narrative-camera-groups`, exact per-shot timing is mandatory and overrides this default.
6. For image-to-video, avoid asking for impossible transformations that contradict the input image; preserve the image's pose, outfit, camera angle, and spatial logic unless the user explicitly wants a transformation.
7. Always include aesthetic logic from `$visual-style-aesthetic-direction` when style matters, and material/render logic from `$ai-material-realism` for visual prompts. Never use either as a substitute for audiovisual grammar. Make render vocabulary compact for simple scenes and detailed for hero characters, products, vehicles, close-ups, cinematic shots, or anything the user will judge visually.
8. If the prompt involves speed, vehicles, chase, impact, fast camera movement, foreground wipe, rain, sparks, dust, light trails, magic trails, or stylized action, explicitly separate motion traces into layers. Use photographic blur for camera/CG realism; use smear frames, pose echoes, speed lines, impact frames, debris, or ink/energy trails for stylized animation. Keep face, hands, weapon silhouette, foot support, and contact point readable.
9. If weapons, armor, creatures, robots, transformations, collisions, throws, or superhuman strength matter, use `$action-choreography-reference` before packaging. Do not let "heavy", "powerful", or "strong" remain unsupported adjectives.
10. For final generation prompts, keep explanation short. The deliverable is the prompt, reference roles, audio plan when relevant, positive stability locks, and one controlled retry note.
11. If the user complains that standing positions drift in one scene, add a layout/blocking reference if available; otherwise rewrite as master-wide shots plus close-up inserts that conceal micro-drift and re-establish position only at key beats.

## Action Physics Packaging

Add this block before ordered action beats when action weight matters:

```text
动作物理：
角色力量等级与武器负载关系：[...]
武器质量分布与握持：[...]
支撑与重心路径：[...]
接触后的双方/环境反应：[...]
惯性延展、制动与最终稳定姿态：[...]
```

For transformed weapons, state the physical profile before and after transformation and require a visible regrip/rebalance before use.

When the upstream action plan comes from `$seedance-fight-director`, preserve its imported A/B/C/D action classification:

- A/D actions need start-state or start+end-state anchors in the prompt.
- B actions can remain simple continuous motion.
- C actions upgrade only when emotion, plot importance, slow motion, or endpoint continuity demands it.
- For HEAVY/RUSH/CHASE timing, carry over hit-stop, recoil, environment proof, and final stable pose without pasting the whole fight-analysis table into the final prompt.

## Reference Asset Readiness

Before delivering a multi-reference or image-to-video prompt, provide a compact asset plan:

- **Already available**: files/images/videos the user has supplied or clearly named.
- **Required before generation**: assets without which identity, vehicle/prop, environment, or blocking cannot be controlled reliably.
- **Optional enhancement**: style, material, motion, lighting, or camera references that improve quality but are not required.
- **Generate first**: missing stills or boards that Codex can create before the video attempt.
- **Reference role**: one explicit role per asset; state what it controls and what it must not override.

Use the minimum sufficient set. Do not demand five references when one strong character image and one layout board can control the scene.

For the user's common SD2 全能参考 workflow, consider this order:

1. character identity/outfit
2. main vehicle/weapon/prop
3. environment/palette
4. layout/blocking board
5. optional style/material detail
6. optional motion/camera reference

## Layout Reference Packaging

Use this as an internal packaging pattern when an abstract board is supplied. Replace `N` with the real uploaded asset number before delivery:

```text
@图片名（color-board / CAD 场面调度参考）：锁定物体占地、前后层级、长轴方向、朝向、视线、动作路径、目标点、左右关系、距离比例、尺度与镜头构图。成片继承真实角色身份、服装、渲染风格、色彩、光线和材质；色块、箭头、标注、网格与简化几何仅作为空间控制信息。
```

When the board uses colors, translate it explicitly:

```text
Color/shape mapping:
cyan = main subject standing zone + facing/gaze arrows
black/dark = vehicle or large prop footprint + long-axis/nose direction
gold = fixed set piece + action path + interaction target
red = warning/control/authority panel or fixed UI/set element
gray = optional camera/view direction hint
```

Revise the mapping to match the actual board. Do not reuse the example mapping blindly.

## Output Formats

For quick rewrite:

```text
【角色/资产锁定】...
【视觉材质总控】...
【镜头语言总控】X风格 + [全片可见镜头结果]；...
【事件节拍】
镜头01｜0-2s｜景别、机位、焦段、景深、光线、运镜、动作、表演、台词、切点、结束状态与承接。
T=0-1s：单一可观察动作或表演变化。
T=1-2s：动作结果、反应或承接状态。
【声音】...
【正向稳定约束】...
```

For production prompt:

【生成模式】

【已有素材 / 还缺素材】

【素材映射 / 参考角色表】

【参数建议】

【时间铰链 / 动作状态链】

【音乐与声音】

【完整可复制提示词（单独复制下面代码块）】

```text
【角色/资产锁定】
@实际图片名（...参考）：...  # 使用用户上传的真实图片名
【视觉材质总控】
...
【镜头语言总控】
X风格 + [全片可见镜头结果]；...
【事件节拍】
镜头01｜0-2s｜景别、机位、焦段、景深、光线、运镜、动作、表演、台词、切点、结束状态与承接。
T=0-1s：单一可观察动作或表演变化。
T=1-2s：动作结果、反应或承接状态。
【声音】
...
【正向稳定约束】
...
```

【生成前质检】

【下一轮只调】

For multi-shot:

```text
【角色/资产锁定】
@实际图片名（...参考）：...  # 使用用户上传的真实图片名
【视觉材质总控】
...
【镜头语言总控】
X风格 + [全片可见镜头结果]；镜头家族 / 焦段范围 / 轴线 / 切镜触发 / 主要运镜语法 / 证明任务。
【事件节拍】
开场：[第一帧状态、距离、姿态与压力关系]。
推进：[动作路线与状态变化，形成明确因果]。
转折：[攻防、情绪或空间关系发生变化]。
高潮：[峰值动作、接触证据与直接后果]；若此处需要特殊镜头，补写“[冲击/遮挡]触发[特殊运镜]，形成[可见结果]”。
结尾：[制动、余波与清晰终态]。
【声音】
...
【正向稳定约束】
...
```

## Guardrails

- Do not write only aesthetic adjectives such as "高级感", "电影感", or "氛围感"; translate them into medium domain, style rules, camera, light, motion, material, render vocabulary, rhythm, and composition.
- Do not command emotional transitions only as labels such as "from happy to broken". Use temporal hinge language and visible cues: past residue, present action, incoming pressure, final consequence.
- Do not write texture-rich prompts whose shot function, blocking, axis, screen direction, or edit logic is missing. Fix the audiovisual scaffold first.
- Do not bury the global visual style after the detailed shot list. Later shots inherit the visual master; they should not repeatedly redefine style.
- Do not omit the camera / shot-style master from a substantial copyable video prompt. If the prompt only has event beats, action, material, and stability locks, it is incomplete. The user expects the reusable camera language to appear near the beginning, not be implied.
- Do not let action effects cover the action. Trails must have a source, direction, layer, duration, and decay; they must prove speed, contact, route, force, or transition rather than merely decorate the frame.
- Do not use exact timestamps as decoration. In narrative camera groups, timestamps are required production allocations: derive them from dialogue, action, reaction, and edit needs, then verify the sum.
- Do not confuse useful segment allocation with arbitrary micro-management. Preserve exact shot timing when `$narrative-camera-groups` owns the delivery; otherwise avoid subdividing every cut unless necessary.
- Do not overload a short clip with too many actions. Within each beat, one clear action plus one motivated camera move usually beats five competing instructions; across the whole clip, connect the camera moves through action, impact, occlusion, or receiver handoff.
- Do not describe a heavy weapon without actor-relative load, mass distribution, support, follow-through, and braking.
- Do not let superhuman strength erase traction, recoil, environmental force, or settling.
- Do not turn fantasy power prompts into either pure physics or pure VFX. Keep the power's dramatic function clear, but leave the model room to invent the exact micro-gesture when the user wants looser generation.
- Do not make shadow powers blue/purple by default, or describe them as glowing lines, black fog, black screens, tentacles, or magic explosions unless explicitly requested. Shadow should usually read through absence of light, reflection suppression, silhouette delay, occlusion, and exposure contrast.
- Do not mention old project-specific items inside a new unrelated prompt just to prevent them. If they are not part of the current concept, keep them out of both positive and exclusion prompt.
- For identity consistency, lock visible traits: face, hairstyle, clothing, body type, prop, color, and lighting.
- For first/last frames, describe the transition path rather than inventing a new unrelated scene.
- For multi-reference prompts, state the role of each asset instead of assuming the model knows why it was uploaded.
- Do not present a reference-dependent prompt as ready when a required identity, prop, environment, first/last frame, or layout asset is missing. Name the missing asset and whether it must be generated first.
- Avoid using protected characters, living public figures, brand marks, or copyrighted scenes unless the user has a legitimate reason and asks for them directly; prefer original alternatives.


## Liu Standard Copyable Video Prompt Architecture - Mandatory Positive-Only Gate

This is the mandatory output structure for Liu's copyable AI-video prompts, including Jimeng SD2, Seedance 2.0, all-reference mode, image-to-video, continuation, added shots, transformation clips, action clips, monster clips, character PVs, and camera/shot prompts.

Use this exact order inside every final copyable script-derived camera-group block:

```text
角色/资产锁定
...

视觉材质总控
...

镜头语言总控
...

事件节拍
...

声音
...

正向稳定约束
...
```

Hard rules:

- Do not deliver a substantial video prompt as loose natural paragraphs. The six headings are part of Liu's prompt contract.
- Keep the content inside the paste-ready code block as plain model-ready text. The six Chinese section labels may remain, but do not place Markdown tables, `#` headings, `>` quotes, `**` emphasis, citations, diagnostics, or workflow commentary inside the block.
- In a six-part camera-group prompt, do not omit `镜头语言总控`. It must
  contain the whole-film perspective, lens family, distortion, movement energy,
  framing/edit rhythm, transition language, and reveal logic in concrete visible
  terms. `事件节拍` inherits the global camera identity, but each explicit shot
  block must still state its local camera setup and execution result. Write a
  local camera clause whenever it identifies that shot's position, height,
  angle, lens, focus, path, or cut proof. Repeating a generic style label is a
  formatting failure; omitting shot execution detail is also a failure.
- Every section must contain substantive current-group controls. `事件节拍`
  restates every shot with shot number, timecode/duration, shot size, camera
  position/height/angle, focal length or perspective, depth of field/focus,
  lighting direction/quality/color temperature/shadows, camera movement/path,
  action/performance, verbatim authoritative dialogue, cut trigger, ending
  state, and handoff. Empty headings and `同上`/`沿用`/`参考镜头表`/`保持不变`
  shortcuts fail compilation.
- The structured shot plan always retains contiguous `micro_beats`. Render
  them as visible `T=起始-结束s` lines only for the `high` profile; `low` and
  `medium` keep concrete shot event prose without T lines. Stored ranges still
  cover each parent shot exactly and each range carries one observable change.
- Each shot's T lines must sit under an explicit shot boundary such as
  `镜头01｜0-2s`. Several shots may not be merged into one unlabelled event
  paragraph.
- Keep `视觉材质总控`. Put concrete material/light/render controls before events. Use named visual-material anchors only when they clarify a decisive material/light/color/render identity; otherwise write direct visible material behavior.
- If no character reference exists, use `角色/资产锁定` for subject, prop, environment, identity, form state, or continuity locks rather than deleting the section.
- Put the first visible frame/state inside the opening sentence of `事件节拍`, e.g. `开场：第一帧就是...`.
- Do not include platform hard parameters in the copyable prompt when Liu says he will set them separately.
- `正向稳定约束` replaces the old exclusion slot. It contains only positive stability locks: subject identity, camera attention, scene relationship, color ownership, material response, sound focus, and readable action path.
- Paste-ready prompt policy: the model-ready code block is positive-only. It states only what is present, visible, audible, active, and locked in the current shot. Exclusion, absence, correction, comparison to old attempts, and previous-failure wording stay outside the copyable block. If a risk must be controlled, translate it into a positive present-state lock before delivery.
- Source-trace gate: every concrete phrase, including existing subjects, props, locations, palettes, camera routines, transitions, powers, sounds, and stability locks, must trace to Liu's current instruction, a supplied/inspected asset, the active global bible/continuity lock, or a user-approved reusable rule. If the trace fails, omit the phrase from the paste-ready prompt or move it outside as a question/assumption.
- If the prompt is missing these sections, contains paste-target exclusion wording, or fails traceability, rewrite it instead of explaining.

Internal ASCII anchors only:

- ROLE_ASSET_LOCK = 角色/资产锁定
- VISUAL_MATERIAL_MASTER = 视觉材质总控
- CAMERA_STYLE_MASTER = 镜头语言总控
- EVENT_BEATS = 事件节拍
- SOUND = 声音
- POSITIVE_STABILITY_LOCKS = 正向稳定约束


