---
name: creative-production-ledger
description: 可追溯的生产台账：绑定提示词、参考资产与职责、模型模式与设置、版本、生成产出、评审证据、验收决策与受控的重试增量。触发：验片、重试、版本对比、生产记录、素材溯源，或任何需要创意结果与输入可复现的场景。 Create and maintain a traceable production ledger that binds prompts, reference assets and roles, model/mode/settings, versions, generated outputs, review evidence, acceptance decisions, and controlled retry deltas. Use for AI image/video projects, prompt iterations, generation tracking, 验片, 重试, 版本对比, 生产记录, 素材溯源, or whenever a creative result and its exact inputs must remain reproducible.
---

# Creative Production Ledger

## Core Intent

Close the production loop without replacing specialist creative skills:

```text
prompt + references + model/mode/settings
-> generated output
-> review evidence and verdict
-> isolated retry delta
-> next attempt
```

The ledger is an evidence index, not a media library. Keep original project files where they belong; record relative paths, SHA-256 hashes, sizes, roles, and relationships.

## Runtime

Prefer the verified isolated environment:

```powershell
$python = 'D:\CodexTools\creative-pipeline\venv\Scripts\python.exe'
$skill = 'C:\Users\liu1\.codex\skills\creative-production-ledger'
```

## Workflow

1. Initialize one ledger per creative project:

```powershell
& $python "$skill\scripts\ledger.py" init 'C:\project' --title 'Project title'
```

2. Record every paid or decision-relevant generation attempt:

```powershell
& $python "$skill\scripts\ledger.py" attempt 'C:\project' `
  --prompt 'prompts\v001.txt' `
  --reference 'identity=references\character.png' `
  --reference 'layout=references\blocking.png' `
  --model 'Seedance 2.0' --mode 'all-reference' `
  --setting 'duration=5s' --setting 'aspect_ratio=16:9' `
  --output 'outputs\v001.mp4'
```

For SD2 / Seedance all-reference or reference-driven work, record reference role and segment boundaries instead of treating a reference pack as one blob. Useful settings include:

```powershell
--reference 'motion_camera=references\ref01_0003-0008.mp4' `
--setting 'motion_camera_source=original_ref01.mp4' `
--setting 'motion_camera_range=00:03-00:08' `
--setting 'motion_camera_role=low-angle camera + vertical chase only' `
--setting 'do_not_copy=identity,outfit,scene,ui,watermark'
```

This matters because a successful prompt often depends less on the text itself and more on which reference supplied identity, scene, motion, first frame, end frame, or effects.

3. Attach deterministic and human review evidence:

```powershell
& $python "$skill\scripts\ledger.py" review 'C:\project' `
  --attempt A001 --evidence 'outputs\v001_review\review.json' `
  --verdict retry --issue '00:02.10 weapon silhouette drifts'
```

4. Record a controlled retry. Name only changed variables; everything else is inherited by intent:

```powershell
& $python "$skill\scripts\ledger.py" retry 'C:\project' --from A001 `
  --prompt 'prompts\v002.txt' --output 'outputs\v002.mp4' `
  --change 'camera: orbit -> locked tracking' `
  --change 'weapon lock moved to first sentence'
```

5. Verify that recorded files have not changed, then run `summary` before handoff or case extraction:

```powershell
& $python "$skill\scripts\ledger.py" verify 'C:\project'
& $python "$skill\scripts\ledger.py" summary 'C:\project'
```

Read [ledger-schema.md](references/ledger-schema.md) only when modifying the schema or consuming it programmatically.

## Color And Delivery Gate

Run before marking an output accepted:

```powershell
& $python "$skill\scripts\inspect_delivery.py" 'C:\project\outputs\v002.mp4' `
  --expected sdr-rec709 --json 'C:\project\outputs\v002_delivery.json'
```

For OCIO/ACES work, also pass the exact config:

```powershell
& $python "$skill\scripts\inspect_delivery.py" 'C:\project\frames\shot.exr' `
  --expected aces-exr --ocio-config 'C:\config\config.ocio'
```

An installed OCIO built-in config URI such as `ocio://cg-config-v4.0.0_aces-v2.0_ocio-v2.5` is also accepted; list locally available IDs through PyOpenColorIO before choosing one.

Treat missing or contradictory color metadata as a delivery failure when a target profile is declared. Do not infer a color space from appearance.

## Lightweight Pose Reference

Use pose extraction only to create a computable blocking/body-line reference. It is not identity, anatomy, performance, or choreography truth.

```powershell
& $python "$skill\scripts\extract_pose_reference.py" 'C:\references\pose.jpg' `
  --output 'C:\references\pose_extract' --download-model
```

Outputs:

- `pose.json`: 33 normalized and world landmarks with confidence;
- `pose_overlay.png`: source image with detected skeleton;
- `pose_skeleton.png`: clean machine-facing skeleton reference.

Assign `pose_skeleton.png` as `pose/blocking reference only`; forbid it from overriding identity, costume, materials, lighting, or world style. Do not install depth or segmentation models until a real project requires them.

## Routing

- Use `$ai-video-prompt-preflight` before recording a generation-ready attempt.
- Use `$ai-video-output-review` to produce timestamped review evidence.
- Use `$ai-video-iteration-doctor` to isolate the next retry delta.
- Use `$creative-casebook` only after at least two linked attempts or clear user-confirmed evidence.
- Use `$capsule-engine` only when repeated evidence supports a reusable rule.

## Guardrails

- Never record secrets, account tokens, private upload URLs, or raw credentials.
- Hash files at record time; if a later hash changes, treat it as a new version.
- Record reference roles explicitly. A path without a role is not reproducible context.
- Do not overwrite attempt history; append a retry linked by `parent_attempt`.
- Do not call a result accepted until review and delivery evidence are attached.
- Keep one ledger per project. Do not create a global activity log.
