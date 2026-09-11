## Liu Asset-Token And Whitebox Reference Check

For Liu's final prompts, first-use asset references supplied with the script must be scoped as exact name-based handles `@图片名（...参考）`, `@视频名（...参考）`, and `@音频名（...参考）`; do not leave generic `参考图1/图1/image1`, invented names, bare `{{Image N}}`编号, or pseudo-layer tags in the copyable prompt.

For a whitebox / Blender previs / mocap reference:

```text
@动作预演.mp4（动作、身体重心、镜头远近与切镜逻辑参考）：迁移动作节奏与运镜证据。
```

# Preflight Checklist

Use this for every final AI video prompt check.


## Liu Six-Part Positive-Only Prompt Contract And Contamination Gate

Before approving any copyable AI-video / SD2 / Seedance prompt for Liu, verify the prompt block uses this order unless Liu explicitly requests another format:

```text
角色/资产锁定
视觉材质总控
镜头语言总控
事件节拍
声音
正向稳定约束
```

Paste-ready prompt policy: the model-ready code block is positive-only. It states only what is present, visible, audible, active, and locked in the current shot. Exclusion, absence, correction, comparison to old attempts, and previous-failure wording stay outside the copyable block. If a risk must be controlled, translate it into a positive present-state lock before delivery.

Source-trace gate: every concrete phrase, including existing subjects, props, locations, palettes, camera routines, transitions, powers, sounds, and stability locks, must trace to Liu's current instruction, a supplied/inspected asset, the active global bible/continuity lock, or a user-approved reusable rule. If the trace fails, omit the phrase from the paste-ready prompt or move it outside as a question/assumption.

Approve only when the paste-ready prompt describes the desired current frame/clip directly. A risk control must become a positive stability lock, not a list of absent things.

Hard-fail and rewrite when either condition appears:

- a supplied asset's first mention is not the exact scoped handle `@图片名（...参考）`, `@视频名（...参考）`, or `@音频名（...参考）`;
- `镜头语言总控` lacks a complete whole-film camera identity: compatible style anchors, perspective, lens family, distortion, movement energy, framing/edit rhythm, transition language, or reveal logic;
- ordinary `事件节拍` lines repeat the camera master, or a genuine special-camera beat lacks a motivated trigger plus concrete visible result compatible with the master.

## Reference Roles

Check:

- which image locks identity?
- which image locks outfit?
- which image locks prop/vehicle?
- which image locks scene?
- which image locks style?
- which image should be ignored for unrelated details?

Prompt block:

```text
@角色立绘.png（角色身份与服装参考）锁定角色；@载具设计.png（载具设计参考）锁定载具；@环境建筑.jpg（环境色彩与建筑参考）锁定场景。每项素材仅迁移已分配职责。
```

## First Frame State

State what exists at the start:

- current form
- location
- pose
- prop state
- weather/lighting
- action phase

State the visible start directly inside the prompt.

## Timing

First distinguish:

- total clip duration: hard requirement;
- structural timing: approximate hook/turn/peak/ending placement;
- physical timing: preload, action, consequence, braking, recovery;
- macro-segment duration: exact when timing confidence is high;
- individual shot duration: omit by default; hard-code only for synchronization or necessary edit control.

First determine timing evidence:

- reviewed reference footage or a successful previous output;
- animatic, storyboard timing, or edit map;
- music/dialogue/first-last-frame/edit synchronization;
- credible physical action-phase and content-density budget.

Then assign confidence:

- high: exact macro-segment ranges;
- medium: approximate ranges or proportions;
- low: causal order only.

For each exact segment, check:

- duration is enough for the action
- one main action per segment
- one dominant camera move per segment
- segment adds new information or pressure
- all intervals sum to total duration without accidental gaps or overlaps
- simple actions are not stretched into idle holds
- heavy or transforming actions are not compressed below their physical stages

Keep individual shot timing flexible unless a specific cut requires synchronization.

## Global Visual Master

Check that the prompt defines before detailed shots:

- medium and realism level;
- primary aesthetic family;
- palette ownership and forbidden drift;
- line/shape/silhouette language;
- material-light system;
- rendering hierarchy and optical character.

Local shots may vary scale and angle but must inherit this master.


## Named Camera And Conditional Material Anchor Gate

Check that `镜头语言总控` contains the complete camera-style stack when the prompt is substantial and camera-sensitive. Ordinary `事件节拍` lines must inherit it without repetition; only genuine special-camera beats add a local trigger and concrete visible result.

Check `视觉材质总控` in two layers:

1. Concrete material-light controls are present when the scene needs visual realism, surface identity, or render consistency.
2. Name-style visual-material anchors are used only when material, light, color, render finish, production-design surface, or atmosphere is a decisive creative variable, the source lacks a clear material identity, or Liu requests named aesthetic references.

Accepted shape:

```text
视觉材质总控: direct visible material/light/color/render behavior; optional [person/work/studio/reference name]风格 + concrete visible material/light/render result.
镜头语言总控: [director/cinematographer/film/studio name]风格 + concrete composition/blocking/camera movement/edit rhythm/reveal result.
```

Valid anchor types include director names, cinematographer names, photographer names, production designer names, animation director names, manga artist names, studio names, film/game/work titles, and art/design references. Technical words such as low angle, dolly-in, wet reflection, PBR, AO, volumetric light, foreground occlusion, and rack focus support the names; they do not replace camera grammar or concrete material behavior.

Each used anchor must be written as `风格` syntax plus one concrete visible result, and must pass source trace or user-approved reusable-rule trace.

## Action Physics

Check when the scene includes weapons, armor, robots, creatures, throws, collisions, transformations, vehicles, or superhuman force:

- actor strength is defined relative to the load;
- weapon length, grip, and mass distribution are stable;
- center of mass remains supported or a step/slide/brace/airborne phase is shown;
- force starts from a visible support chain;
- contact moves both systems or intentionally redirects one;
- follow-through, braking, and recovery fit the load;
- the environment reacts from a visible source;
- transformed forms receive new handling behavior;
- camera holds long enough to see support and consequence.

Prompt block:

```text
Action physics: [actor/load relation], [mass distribution], [support and center path],
[contact response], [follow-through/braking], [stable end state].
```

## Continuity Locks

Lock:

- face and age
- hair silhouette
- outfit structure
- prop/vehicle silhouette
- color ownership
- world material rules
- lighting direction
- screen direction

## Contradiction Scan

Look for:

- locked camera + handheld + orbit + zoom in same shot
- no camera movement + rapid tracking
- daylight + neon night + pitch-black rain alley
- realistic 3D + flat 2D manga + photoreal live action
- slow motion + extremely fast continuous action with many cuts
- negative prompt forbids something the positive prompt requires

## Keyword Contamination Scan

Check whether any current prompt word is likely to pull the model toward an unwanted association cluster. Do not check against a fixed example blacklist; infer the contaminating word from the current concept.

Risk signs:

- negative phrasing keeps a risky noun alive even while trying to remove it;
- a loaded activity, profession, genre, tool, or role label imports default props, costumes, locations, or screen-facing proof;
- an abstract verb requires invisible intent, attention, gaze, awareness, orientation, or interaction;
- a camera/shot label is asked for without visible proof through surfaces, scale, occlusion, or frame occupancy;
- the prompt asks the model to avoid an old failure by naming that failure.
- a context rewrite describes the old context in order to reject it, instead of stating the new current frame.

Repair before approval:

```text
Replace contaminated keywords with positive visible facts:
[who/what is visible] + [which side/surface is visible] + [what is hidden] + [contact/pose/path details]
Replace abstract actions with what the camera sees:
[visible body/object axis] + [target placement if needed] + [surface/edge/light proof]
Replace shot-size labels with frame occupancy and visible surfaces.
```

Approve only when the prompt describes the desired image directly rather than explaining which wrong image to avoid.

## Positive-Only Context Rewrite Gate

Before approving the final copyable prompt, inspect every phrase that tries to correct a previous context or suppress an unwanted association.

Rewrite when:

- the phrase names an old subject, prop, location, costume, creature, style, palette, action mode, or camera setup that is not part of the current shot;
- the phrase describes the old context in order to reject it;
- a concrete noun has no source trace in the current request, inspected asset, active continuity lock, or user-approved reusable rule;
- an abstract camera/action word lacks visible proof through surfaces, scale, occlusion, frame occupancy, contact, path, or material response.

Approve when:

- the prompt states the current visible target state directly;
- every stability control is written as something that remains present and consistent;
- old-context concerns have been translated into current subject, environment, prop state, action path, palette, camera relation, material/light, or sound facts.

## Positive Stability Lock Examples

Write the final section as compact positive locks:

```text
正向稳定约束: subject identity remains anchored to @角色立绘.png（角色身份与外观参考）; camera attention stays on the named subject; costume color blocks, prop silhouette, scene layout, and light direction remain consistent; material response stays coherent across motion; action path remains readable from opening state to endpoint.
```

