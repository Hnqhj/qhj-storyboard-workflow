# Continuity, Space, And Editing

Use this for multi-shot sequences, especially travel, chase, fight, dialogue, or any moving subject.

## Screen-Geometry Contract

Before designing coverage, write one compact contract for what the viewer is expected to keep stable:

```text
subject positions / gaze or action targets / dominant screen vector /
camera side or allowed zone / expected off-screen space / reset conditions
```

Each new shot must either preserve that contract or visibly renegotiate it. A reset is readable when the viewer can see the camera or subject cross the axis, receives a neutral/on-axis or overhead view, returns to a re-establishing shot, or gets a strong action/sound cue that rebuilds the map.

If disorientation is intentional, name which orientation fact is being withheld and what replacement cue—identity, sound, motion, landmark, or graphic match—still lets the viewer read the intended effect.

`shot-information-progression` owns the dramatic question and viewer-knowledge delta. This reference owns how that approved information is realized as screen position, direction, gaze, and cut geometry.

## Axis Of Action

Create an imaginary line through two interacting subjects or along the path of a moving subject. Keep cameras on one side of that line when you want stable screen direction. Crossing the line is allowed only when the shot makes the crossing visible or when disorientation is intentional.

Safe ways to cross:

- show the camera physically crossing the axis in a continuous move
- insert a neutral front/back shot before changing sides
- cut through an overhead map-like shot
- use a strong action beat that reorients the viewer

## Screen Direction

For travel and chase, assign a dominant direction:

```text
dominant vector: left-to-right, right-to-left, toward camera, away from camera, upward, downward
```

Keep the vector stable across cuts. If a subject exits frame right while moving left-to-right, the next shot usually has them enter from frame left and keep moving right.

For vehicles:

- define road direction before close-ups
- let at least one wide or overhead shot update geography
- keep the vehicle nose, lane, and turn direction readable
- do not reverse direction unless the story says it turned around

## Continuity Editing Tools

- Establishing shot: lets the viewer understand the place before details.
- Eyeline match: character looks off-screen, next shot shows what they see.
- Match on action: cut during the same physical motion so the cut feels invisible.
- Shot/reverse shot: keeps relation readable in conversation or confrontation.
- Insert: isolates a meaningful object or detail.
- Cutaway: briefly leaves the main action to show a reaction or related detail.
- J-cut: sound from the next shot begins before the picture cuts.
- L-cut: sound from the previous shot continues after the picture cuts.
- Sound bridge: diegetic sound connects two scenes.

## Shot-Pair Expectation Transaction

Treat a cut as a response to an outgoing cue, not only as a join between two clips:

```text
outgoing cue -> expected answer -> next-shot response -> readability proof -> next handoff
```

The cue may be a gaze, gesture, movement, sound, exit, impact, or emerging detail. The next shot can:

- **confirm** the expected object, direction, or consequence;
- **withhold** it to extend suspense while preserving a readable relation;
- **reframe** it by revealing a larger or different context;
- **contradict** it with evidence that changes the viewer's interpretation.

For each important cut, state which response is intended and what visible or audible proof makes that response legible. Do not force a literal POV or matched reverse shot when withholding or reframing is the dramatic choice.

## Spatial Clarity Checklist

Before writing the final prompt, answer:

- Where is the subject at the start?
- Where is the subject at the end?
- What is the dominant movement direction?
- What is the obstacle or turn?
- Where is the camera relative to the axis?
- Which shot updates the viewer's map?
- Which shot gives identity/emotion?
- What cue does the current shot leave, and how does the next shot answer it?
- If the contract changes, what lets the viewer update the map?

## Chase And City Travel Pattern

Use this when the user wants a character moving through a city:

```text
1. extreme wide map: city scale and route vector
2. low ground/underpass: speed and mass
3. side tracking: body/vehicle readability
4. obstacle/near miss: danger beat
5. overhead/telephoto: geography update or compression
6. close-up/insert: identity, control, wheel, hand, eyes
7. release wide: subject exits, city remains changed
```

## Common AI Failures

- Repeating the same "cool" angle without spatial development.
- Teleporting the subject between unrelated backgrounds.
- Losing direction after a close-up.
- Making every shot close and fast, so no shot feels fast.
- Breaking vehicle or prop shape during cuts.
- Using too many camera moves in one shot.
