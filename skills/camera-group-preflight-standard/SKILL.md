---
name: camera-group-preflight-standard
description: Standard-depth validator used only when script-camera-group-router selects standard processing for an ordinary complete script or multi-group dialogue/emotion scene. Check authority, timing, continuity, shot purpose, camera execution, material/light grounding, dialogue and foley, platform handles, six-part packaging, explicit shot blocks, and profile-aware micro-beats without rewriting the prompt. Escalate fights, VFX, complex continuity, research, retries, or commercial exhaustive work to ai-video-prompt-preflight.
---

# Camera Group Preflight Standard

Validate an ordinary short-drama camera-group package once. Treat the approved
`ShotLedger`, `CameraGroupPlan`, and compiled prompt as evidence; do not recreate
them in prose.

## Checks

1. Authority: story facts, dialogue, character state, and outcome match the
   accepted script.
2. Capacity: group and shot timing are continuous; dialogue, pauses, reactions,
   actions, and holds fit naturally.
3. Continuity: identity, costume, prop, axis, screen direction, opening state,
   endpoint, and next-group handoff agree.
4. Shot purpose: every shot adds information, proves action, reveals reaction,
   or creates a necessary handoff.
5. Camera: each shot has concrete position, height, angle, perspective/lens,
   focus/depth of field, movement path, and cut trigger.
6. Image grounding: visible materials have coherent light direction, contact
   shadows, reflection/roughness behavior, and stable texture.
7. Sound: authoritative dialogue and source-coupled dry foley are synchronized;
   other audio requires explicit authority.
8. Packaging: six sections in order, one explicit block per shot, contiguous T
   profile-aware micro-beats, exact handles, no cross-reference shortcuts,
   standalone group. Require visible T lines only for `high`; validate stored
   micro-beats for every profile.
9. Compiler: exactly one selected compiler authored each final prompt once.

Run the camera-group linter when structured files exist. Return findings and
named field patches only:

```text
status: pass | repair | escalate
hard_failures: []
field_patches: []
escalation_depth: full | none
reason: ...
```

Do not browse or launch separate research. Do not write a replacement prompt.
Escalate to `full` when a finding requires action physics, VFX lifecycle,
multi-reference arbitration, cross-scene/episode reconstruction, current
platform research, generated-output diagnosis, or commercial evidence.

