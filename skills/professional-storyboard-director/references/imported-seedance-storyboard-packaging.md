# Imported Seedance Storyboard Packaging

For Liu's recurring真人短剧 workflow, `../director-workflow-70/references/short-drama-director-stack.md` is the upstream authority. The generic 4-15s guidance below applies only when the active Seedance surface or an explicit user request requires short segments; script-to-camera-group delivery targets 20-23 seconds, normally 18-24, never over 30.

Use this reference when a storyboard, shot table, rough idea, or reference pack must become a Seedance-ready prompt package, especially 分镜转 Seedance 提示词, 4-15s prompt splitting, multi-modal reference mapping, first/last-frame handoff, or prompt hygiene.

This distills supplied local materials from `3.4分镜设计（优化）(1).zip`, `AIGC_video_prompt_skill.md`, `Seedance 2.0提示词指南.docx`, `Seedance 2.0 提示词优化技能 火山官方Skill.md`, `008 通用视频Prompt规则与元模板.md`, `seedance_video_prompt_meta_template_v2（梦长）.md`, `轻量化sd提示词转换器.md`, and `Quill_GPT电影感提示词_v5.0.md`.

## 0. Asset-handle dialect warning

Imported source docs use `@图片N`, `@视频N`, `@音频N`, and sometimes `@material[...]`.

For Liu's current local paste-ready workflow, file references use:

```text
{{Image 1}}, {{Video 1}}, {{Audio 1}}
```

Use the imported `@` syntax only when the user explicitly targets a surface whose UI/docs require it. Otherwise, transfer the reference-role logic, not the literal handle syntax.

Named five-view character assets use a separate platform handle: every character mention in model-facing text is written as the exact `@角色名` supplied by the user. This does not change file-reference syntax and must not be confused with `@Image1`.

## 1. Segment split rules

For generic Seedance-style generation, keep each generated segment inside the active surface's verified model budget. For Liu's camera-group workflow, use the 20-23s group contract from the upstream overlay; use the shorter ranges below only for explicit single-shot tests or surface-imposed limits:

- safest segment range: 4-15 seconds;
- single static image/pose: 2-3s, normally merge with another beat;
- single completed action: 3-5s;
- several continuous small actions: 5-10s;
- long line of dialogue: spoken duration + 2-3s buffer;
- complex staging with turn/walk/dialogue: 8-15s.

Rules:

- merge beats under 4s unless they must be separate cuts;
- split before a segment exceeds 15s;
- do not split a continuous action chain or one line of dialogue;
- split on emotional beat, action phase, location/time change, axis change, or reference-role change;
- give every split a handoff: previous end state, next first-frame anchor, continuity locks, allowed changes, and cut reason.

## 2. Storyboard-to-prompt mapping

When translating an upstream board, do not redesign unless asked. Map fields:

| Storyboard field | Prompt destination |
|---|---|
| event / story job | split decision and prompt title, usually not literal wording |
| scene/location | base setting or scene lock |
| character positions | current state / blocking lock |
| emotional tone | style core, light, rhythm, physical behavior |
| focal length + aperture + camera position | shot size, lens feel, camera placement |
| composition | composition sentence, frame position, proportion, foreground/midground/background |
| camera movement | one dominant camera behavior |
| action / expression / dialogue | visible event content, dialogue inline |
| constraints | positive locks first; short target negatives only when the surface supports them |
| cross-segment card | opening state or handoff lock for the next segment |

## 3. Two prompt packaging shapes

### A. Dense continuous paragraph

Use when the user needs a copyable generation prompt:

```text
[STYLE LOCK]
visual/material/style master...
audio rule...

{{Image 1}} as identity / product / environment / first-frame anchor...
{{Video 1}} as motion/camera/timing reference only...

Shot 1 continuous paragraph: composition + camera state + subject action + dialogue + sound.
[HARD CUT / WHIP PAN / motivated transition]
Shot 2 continuous paragraph: composition + camera state + subject action + dialogue + sound.

targeted constraints...
```

### B. Seedance three-module structure

Use when the target workflow expects a structured Seedance prompt:

```text
【基础设定】角色 / 场景 / sound / asset roles
[氛围与画质] style core / camera-lens / light / palette / reference jobs
[画面内容] shot 1..N with shot size + composition + camera + action/dialogue/sound
```

If a strict 2000-character surface is in play, aim for 1700-1900 characters:

- base setting: 300-400;
- atmosphere/visual: 300-400;
- image content: 800-1000;
- constraints: 100-200.

Do not apply this limit if the active surface, user request, or local workflow does not require it.

## 4. Multi-modal reference map

Assign every asset exactly one primary job:

- identity / face;
- full-body costume;
- product/object;
- environment;
- first frame;
- last frame;
- motion;
- camera;
- timing/rhythm;
- sound / voice / music;
- style / color / lighting.

Best practices:

- Important assets go first.
- A character often works better as face close-up + full-body/costume than as a multi-view collage.
- Use 4-5 well-labeled assets rather than filling every available slot.
- If a video is a motion/camera reference, explicitly prevent transfer of placeholder bodies, debug marks, grids, low-quality lighting, or unrelated style.
- Long images, contact sheets, and nine-grid boards should be split or role-labeled; otherwise the model may treat the grid itself as the scene.

## 5. Prompt hygiene rules

### Lock composition to reduce lottery

Every shot paragraph should answer:

- where is the subject in frame;
- how much of the frame it occupies;
- shot size plus foreground/midground/background;
- subject facing direction and visible body parts;
- what must remain stable.

### Translate abstraction into physical behavior

Replace abstract emotions with visible body facts:

- fear -> weight drops, arms draw inward, jaw freezes, breath breaks;
- sadness -> brow tightens, jaw held, wet eyes, hand stops its task;
- tenderness -> slower motion, light breath, softened gaze;
- hesitation -> micro-pause, gaze shift, hand starts then withdraws;
- realization -> pupil focus, breath pause, expression loosens;
- resolve -> fist closes, jaw flexes, eyes fix on target.

### One shot, one dominant camera move

Avoid combining push, pull, pan, orbit, handheld, and crane in the same short beat. If camera complexity is the concept, split into phases or pick one tracking owner.

### Use positive locks first

Imported docs differ on negative prompts. Resolve by target surface:

- If the surface supports negatives, keep them short and risk-specific.
- If negative support is weak or unknown, rewrite as positive locks.
- Never rely on "do not" language as the only protection for identity, count, layout, or camera.

### Avoid prompt contamination

Before delivery, delete:

- previous-project template fragments;
- repeated character appearance in every shot when the reference already controls it;
- unassigned director/studio/name salad;
- meta language such as "this is segment N", "hint at the next scene", "continue the previous one";
- bilingual duplicates of the same term;
- prevention spam for failures that have not appeared;
- abstract quality words that do not bind to visible surface, light, camera, or action.

## 6. Action, space, and physics locks

When the shot is spatially fragile:

- put the first-frame pose/action in the first sentence when possible;
- define head direction, hand grip, foot support, gaze target, and object contact;
- for two people, use exact relation: facing, back-to-back, left/right, foreground/background, distance, weapon/object direction;
- for 360-orbit, state that the camera reveals real back and side planes; the subject does not spin to face camera;
- for Dutch angle, lock diagonal horizon while gravity remains vertical for hair, cloth, liquid, smoke, and falling objects;
- for weapons/props, lock rigid material, grip, contact, collision moment, recoil/follow-through, and no object-body fusion.

## 7. Audio and dialogue

Integrate audio with the visual event:

- sound follows the visible source or offscreen cue;
- action SFX belongs immediately after the physical action;
- dialogue is inline with the speaking action and sync point;
- music/BGM sets emotional bed, but should not replace necessary on-screen action;
- if no music is desired, write "only environment and action sound" in the audio rule.

Use special notation only when the target surface benefits from it:

- background music: parentheses;
- sound effects: angle brackets;
- dialogue: braces or quotes;
- title/subtitle text: bracketed text.

## 8. First/last-frame and continuation

For first/last-frame mode:

- treat the first and last images as locked endpoints;
- write the transition between them, not a duplicate description of both frames;
- avoid language that freezes motion unless a still endpoint is required;
- if the last frame locks the final pose, keep residual dynamic details: breathing, cloth, smoke, light flicker, small environmental motion.

For continuation:

- do not use conversation-dependent wording such as "上一段" inside the paste prompt;
- write the visible current state as the opening event;
- use insert, occlusion, angle change, sound bridge, smoke/dust bridge, or impact bridge to hide unavoidable drift.

## 9. Clean keyframe / image-prompt hygiene

When a storyboard needs keyframes or reference stills:

- choose one visual center before adding detail;
- define subject, scene, shot angle, depth layers, main light source, palette, and a few relevant details;
- for realism, prefer captured moment, motivated light, natural highlights/shadows, and limited background detail over poster-like over-polish;
- for anime/illustration, use clear shapes, reduced random texture, and a controlled palette;
- for product, preserve silhouette, proportion, material reflection, contact shadow, and the main selling surface;
- fix dirty images by reducing background texture/noise; fix over-sharp images by softening hard edges and microcontrast; fix gray images by clarifying main/secondary/accent colors; fix fake faces by removing over-smoothing and letting the face obey the scene light.

## 10. Packaging QA

Before handing off:

- Are asset roles clear and non-overlapping?
- Is the first visible state known?
- Does each generated segment have one action spine and one camera owner?
- Are dialogue and SFX synced to visible actions?
- Are reference handles in the user's required dialect?
- Did you remove meta, old-template contamination, abstract emotion, ungrounded negatives, and repeated appearance descriptions?
- If exact times are used, do they add up and have evidence? If not, use causal order instead of fake precision.
