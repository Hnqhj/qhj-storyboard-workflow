---
name: camera-group-preflight-fast
description: 快速档轻量校验，仅在调用方给定 fast 档后使用。检查镜头组时长、六段顺序、显式镜头块、微节拍、对白权威性、参考句柄、音频策略、独立完整性与禁止的捷径。不用于打斗、VFX、变身、复杂连续性、重试。 Lightweight validator used only after the received processing depth is fast, for a low-risk script or fragment. Check camera-group timing, six-part order, explicit shot blocks, profile-aware micro-beats, authoritative dialogue, exact reference handles, audio policy, standalone completeness, and forbidden shortcuts. Do not use for fights, VFX, transformation, complex continuity, research, retries, or standard/full production review.
---

# Camera Group Preflight Fast

Validate the completed low-risk prompt without reopening creative design or
loading the full `ai-video-prompt-preflight` Skill.

## Checks

1. Every camera group is within its selected duration contract.
2. Shot times are continuous and sum to group duration.
3. Every prompt contains the six required sections in order.
4. `事件节拍` has one explicit `镜头NN｜起始-结束s` block per shot.
5. The structured plan always has contiguous micro-beats covering every shot
   exactly. Require visible `T=起始-结束s` lines only when the active prompt
   profile is `high`; `low` and `medium` prompts must omit those lines.
6. Authoritative dialogue is unchanged and has plausible speaking time.
7. Required `@角色名` and exact named reference handles are present.
8. Sound follows the active audio authority.
9. No `同上`, `沿用`, `参考镜头表`, `保持不变`, partial patch, or dependency on
   another prompt is present.
10. All six sections contain current-group control information.

Run
`../narrative-camera-groups/scripts/shot_group_linter.py --strict` when a
structured group JSON and prompt file are available.

## Result

Return only:

```text
status: pass | escalate
hard_failures: []
field_patches: []
escalation_depth: standard | full | none
reason: ...
```

Pass leaves the existing prompt unchanged. A mechanical defect returns the
smallest named field patch to the original compiler. A creative, physical,
continuity, reference, or platform uncertainty escalates instead of expanding
this validator. Never rewrite the full prompt.

