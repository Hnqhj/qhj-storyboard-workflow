# AI Video Shot Planning

Use this when the final answer must be a paste-ready AI video prompt.

## Prompt Order

Use Liu's fixed six-part positive-only order:

1. `角色/资产锁定`: exact scoped handles, identity, costume, prop, current form, and continuity facts.
2. `视觉材质总控`: medium, palette, material/light/render behavior.
3. `镜头语言总控`: complete whole-film camera style—compatible named anchors, perspective, lens family, distortion, movement energy, framing/edit rhythm, transition language, and reveal logic.
4. `事件节拍`: spatial route, action physics, state change, contact, and consequence. Ordinary beats inherit the master; only a genuine special-camera beat adds a local trigger plus concrete visible result.
5. `声音`: ambience, cue changes, impact, silence, and dialogue.
6. `正向稳定约束`: present-state identity, prop, world, camera, material, and action-path locks.

## Backstage Shot Formula

Use this ledger for internal design, then compile the default camera grammar into `镜头语言总控`. Do not paste every camera field into every final event beat.

```text
[optional time or relative position] Function: [why this shot exists].
View: [shot size, camera height, angle, lens feel].
Action: [one readable subject action].
Camera style: [X风格 + concrete visible camera result].
Camera contract: [tracking owner + one controlled movement path + action/impact/occlusion trigger + proof job + handoff/endpoint].
Continuity: [screen direction, axis, identity/prop lock].
Physics: [support, weight transfer, contact response, inertia resolution].
Transition/Sound: [cut reason, J/L cut, impact, silence, wipe].
```

## Continuous Prompt Formula

Use when the tool wants one paragraph:

```text
【角色/资产锁定】[identity and scoped references]. 【视觉材质总控】[rendering and material]. 【镜头语言总控】[complete camera style: named aesthetic anchors + perspective + lens family + distortion + movement energy + framing/edit rhythm + reveal logic]. 【事件节拍】The scene begins at [start geography] and moves [dominant vector] toward [end geography]. First: [action/state change]. Then: [action/contact/consequence]. Finally: [endpoint]. Only if one beat needs a special camera, add [trigger + special movement + concrete visible result] to that beat. 【声音】[sound progression]. 【正向稳定约束】[continuity rules].
```

## Good 15s Beat Count

For most AI video tools, plan 4-7 visual beats for a 15-second sequence. A beat is not necessarily a separate hard-timed shot:

- 3 shots: usually too sparse unless each shot is complex and deliberate.
- 4-7 beats: useful balance for action, travel, entrance, fashion, or reveal.
- 8+ shots: use only if cuts are simple and the tool supports clear timecodes.

Do not assign durations by habit. Use exact segment allocation when well-supported; otherwise give total duration, causal order, and peak/ending relationships.

## City Motorcycle Traversal Template

This is an untimed generation sequence:

```text
X风格 + extreme-wide route reveal; the city entrance triggers the camera to follow the road centerline in a descending push, proving destination and scale, then handing off through an overpass wipe.
X风格 + ground-level speed pressure; the motorcycle drops beneath the overpass and triggers the camera to follow the front wheel in a low Z-axis chase, proving suspension, road contact, and speed, then handing off through a foreground pillar pass.
X风格 + readable side track; acceleration triggers the camera to follow rider and vehicle laterally along the travel vector, proving silhouette, lane position, and route, then handing off when an obstacle enters foreground.
X风格 + overhead geography restoration; the near miss triggers the camera to follow the motorcycle from above along the curved road, proving the changed route and pursuer distance, then handing off through the rider's head turn.
X风格 + identity/control insert; the rider's hand or gaze triggers the camera to follow the control gesture in a short push, proving intent and machine response, then handing off through matched handlebar motion.
X风格 + release wide or near-camera pass; the exit action triggers the camera to follow the motorcycle toward the route endpoint in a widening pullback, proving consequence and final geography, then ending on the visible destination state.
```

## Rewrite Rule For Weak Camera Design

When a user says the camera design is bad:

1. Do not defend the previous prompt.
2. Identify whether the failure is function, geography, rhythm, or style.
3. Rewrite with fewer but stronger shot functions.
4. Add a short note explaining the new cinematic logic.

## Positive Stability Locks For AI Video

Write current visible stability facts: the compact name-style camera anchor set remains consistent; screen direction and geography stay readable; the named subject stays in camera attention; face and prop geometry remain anchored; motion blur stays directional and localized; setup and recovery keep foot support visible; weapon inertia resolves through follow-through and braking; impacts show receiver recoil, spacing change, and environment response before the camera hands off.
