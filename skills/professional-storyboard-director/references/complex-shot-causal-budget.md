# Complex-Shot Causal Budget

Use this before packaging a multi-event beat for generation.

## Capacity gate

Default to one primary subject event, one primary camera intention and one visible state change per beat. A secondary reaction is allowed only when caused by the primary event.

Count state transitions rather than prompt length. Crossing a threshold, picking up or releasing a prop, sitting or standing, changing support, introducing another active actor, moving the camera to a new side or height, changing focus/light/VFX state, and causing major environment change all consume the same generation budget. When several happen together, split or simplify before adding detail.

## Completion evidence

For every indispensable action, name the visible condition that proves it finished:

```text
action -> completion evidence -> resulting position/state
```

Examples: the door is fully open before the body crosses the threshold; the prop leaves its source and is visibly held before travel; the prop contacts the table before the hand releases; the body reaches the chair and settles before the next relationship beat. Start/end labels without completion evidence still permit teleporting or skipped contact.

## Topology before prose

Map subject and camera start/end, travel axis, foreground occlusion, middle-ground readability, background landmarks, light direction and the spatial bridge to the next shot. If the path cannot be sketched simply, the prompt is not ready.

For movement through connected space, reverse-build only the geography the action requires:

```text
subject start -> traversable channel -> threshold/turn -> interaction point -> end state
```

Lock the smallest set of landmarks that proves this route. A door, table, vehicle, stair or corridor keeps one relative position across layout references and generated shots. Do not force a fixed landmark count.

Plan two routes separately:

```text
actor route: start -> pass/avoid/cross -> action point -> end
camera route: start side/height -> travel/turn trigger -> proof point -> stop/landing frame
```

They share geography but not instructions. “Camera follows” is incomplete unless its starting side, path or turn trigger, proof task and landing state are clear.

Use an empty multi-view board or top-down blocking board only when connected geography is itself a failure risk. Simple fixed-space beats do not need a nine-view asset. When used, the board controls routes, footprints, long axes, entrances and relative positions—not character appearance or final visual style.

## Causal phase contract

```text
build: establish geography, direction and cause
breathe: hold the action/product evidence in a readable window
resolve: decelerate camera/action/focus/light into a landing frame or transition
```

Use shared event anchors so camera, light, VFX and transition respond to the subject event instead of performing independently.

## Fallback ladder

1. remove competing secondary actions;
2. lock first/last frame or strengthen identity reference;
3. reduce camera axes or speed changes;
4. split at occlusion, action peak or stable landing;
5. generate subject/environment/effect as separate layers;
6. finish the illusion through edit, VFX, sound and color.

On retry, first test whether the parent space and locked landmarks are still valid. If they are, preserve the space/layout asset and repair only the failed action, route or camera phase. Rebuild the parent space only when its connectivity or invariant positions are contradictory.

Static tableaux, packshots and intentional holds are valid. VFX may support contact and consequence but never replace them. Action force and body mechanics remain owned by the action specialist Skills.
