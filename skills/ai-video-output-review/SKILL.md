---
name: ai-video-output-review
description: Inspect and diagnose generated AI video outputs after rendering by probing metadata, extracting timestamped frames, building contact sheets, comparing the result with the prompt and references, and reviewing prompt adherence, identity/count continuity, blocking, camera, motion, physics, aesthetics, material/light, story, audio, and delivery integrity. Proactively use when the user uploads or points to a video and says 看看, 检查一下, 验片, 成片质检, 逐帧分析, 抽帧, 穿帮, 两个主角, 人脸变了, 站位漂移, 红线落地, 动作不对, 画风不一致, 音画不同步, or asks what failed and how to retry.
---

# AI Video Output Review

## Bottom-Layer Reasoning

Apply `sophia-mode`, `think-one-step-further`, and attribution-before-blame:

- Inspect the rendered artifact before diagnosing it.
- Separate observed evidence, likely cause, and unknown cause.
- Preserve successful layers and change the smallest useful variable.
- Convert confirmed output evidence into a case; promote only repeated validated lessons.

## Core Intent

Close the loop after generation:

```text
prompt + references + rendered video
-> deterministic probe and timestamped frames
-> creative/technical review
-> root-cause attribution
-> controlled retry
-> case evidence
```

This skill is the post-generation counterpart to `$ai-video-prompt-preflight`. It does not replace direct visual judgment with an automatic score.

## Evidence Order

Use the smallest available evidence set:

1. Rendered video.
2. Prompt and intended timed beats.
3. Reference assets and their assigned roles.
4. Platform/model/mode, duration, aspect ratio, and generation settings.
5. User's exact judgment.

If only the video exists, review visible facts and mark prompt-level causes as tentative.

## Deterministic Inspection

Run the professional local toolchain before a detailed review:

```powershell
python .\scripts\inspect_video.py `
  '<clip.mp4>' --samples 12 --out-dir '<review-output>'
```

The script writes:

- `review.json`: ffprobe/MediaInfo metadata, PySceneDetect shots, FFmpeg black/freeze/silence/loudness analysis, sample metrics, and technical flags;
- `contact_sheet.jpg`: uniformly sampled timestamped frames;
- `scene_contact_sheet.jpg`: one representative frame from every detected shot;
- `frames/`: reviewable JPEG frames.

Preferred tools:

- FFmpeg/ffprobe 8.1.1 or newer compatible release;
- MediaInfo CLI;
- PySceneDetect AdaptiveDetector;
- OpenCV for frame metrics and optical analysis.

The script automatically falls back to bundled FFmpeg and heuristic shot candidates when professional tools are unavailable. Do not claim a detector ran when its result says `available: false`.

Use the host Python environment with the pinned packages in `scripts/requirements.txt`; `ffmpeg` and `ffprobe` must be available on PATH.

Inspect the contact sheet with the image viewer. Open individual frames around a suspected timestamp when the sheet is insufficient.

Use the bundled `scripts/inspect_video.py`. It accepts both `--out-dir` and `--output`; prefer `--out-dir` in new runs.

## Review Workflow

1. State the intended result and what evidence is available.
2. Run the probe and inspect uniform samples, the per-shot contact sheet, first/middle/last frames, and FFmpeg/PySceneDetect candidates.
3. Map the intended beat timeline against what visibly occurred.
4. Review only relevant dimensions from [review-rubric.md](references/review-rubric.md).
5. Record each issue as:
   - timestamp/range;
   - observed fact;
   - severity;
   - likely cause;
   - confidence;
   - preserve/fix decision.
6. Distinguish cause level:
   - prompt;
   - reference assignment;
   - source asset;
   - shot/workflow design;
   - platform/model limitation;
   - encoding/delivery;
   - unknown.
7. Route the smallest fix to `$ai-video-iteration-doctor`.
8. Run `$ai-video-prompt-preflight` on the revised prompt before the next paid generation when risk is meaningful.
9. If the project has a `$creative-production-ledger`, attach `review.json`, contact sheets or decisive frames, verdict, and delivery report to the inspected attempt.
10. After the retry is inspected, use `$creative-casebook`; use `$capsule-engine` only when the lesson has evidence, boundaries, and reuse value.

## Completed-Output Learning Mode

For Liu's own completed/generated clips, when the purpose is to review what the finished result teaches rather than immediately author the next retry, switch the review from patch mode to reusable-learning mode.

In this mode:

- inspect the artifact normally and preserve timestamped evidence;
- do not spend the response proposing the next shot, next choreography, or a clip-specific prompt rewrite unless Liu explicitly asks for one;
- separate what visibly improved from what still failed;
- abstract the failure one level below the visible symptom: identify the design, causality, timing, camera, motion, VFX, material, continuity, or prompt-architecture mechanism that produced it;
- express the lesson without project nouns, character names, location names, exact props, or one-off plot details;
- state the applicability boundary so one result does not become a universal rule;
- write the validated general solution into the smallest relevant Skill instead of duplicating it across the whole stack;
- if evidence is suggestive but not yet sufficient, record it as a case/hypothesis rather than promoting it as a hard rule.

Use this extraction shape:

```text
observed evidence -> root mechanism -> reusable rule
-> applicability / boundary -> target Skill delta
```

The user-facing result should emphasize the reusable mechanism and which Skill was updated. Do not include a `next retry` section by default in this mode.

## Review Priorities

Use intent-weighted priorities rather than a universal numeric score.

- **Blocking failures**: wrong subject count, identity break, duplicated protagonist, missing key action, broken anatomy, severe prop morphing, unreadable story, corrupted file.
- **Major failures**: spatial drift, axis confusion, repeated/weak action, camera contradiction, style collapse, material/light mismatch, implausible contact, audio-video mismatch.
- **Minor failures**: one soft frame, small exposure jump, secondary texture drift, nonessential background mutation.

For a character-led clip, identity and performance outrank background polish. For an action clip, readable motion and contact outrank decorative detail. For an art-direction clip, style ownership and material/light consistency may outrank literal realism.

For weight-sensitive action, inspect the complete causal envelope: support/preload, center shift, acceleration, contact or near miss, receiver/environment response, follow-through, braking, and stable recovery. Do not infer weight from shake, blur, sparks, or loudness alone.

For fight choreography, do not accept "looks continuous" as success. Pause on sampled frames and inspect whether each exchange has plausible range, line, contact/near-miss relationship, receiver answer, body cost, and a physical source for the next move. Mark "smooth but imagined" as a major action-design failure when the motion flows visually but the combat relationship collapses under close inspection.

For principal hits, audit the complete hit-acknowledgment triad: structural force transfer, receiver performance/physiology, and synchronized sound. When the face is readable, inspect expression change, gaze interruption, jaw/cheek/eyelid response, breath, and guard recovery—not only body silhouette deformation. Mark body squash with an unchanged face and no breath/impact confirmation as rubbery incomplete acknowledgment, even if the pose visibly bends. Also verify grading: one to three hero hits may carry full acknowledgment, while minor contacts should remain compressed enough to preserve speed.

When VFX is present, audit it as a causal system rather than a beauty layer. For each principal effect, inspect: information job and primary read; source/ownership; formation or anticipation; path and foreground/midground/background placement; contact/collision; receiver and environment response; nearby light/shadow/reflection; medium-appropriate blur/smear/trail choice; intensity grade; and dissipation/residue. Mark detached glow/particles, contact-obscuring flashes, uniform hero grading, wrong-material debris, unlit emissive energy, infinite trails, or persistent weapon deformation as major when they damage action readability or medium consistency.

Separate effect failure from action failure. If the body/weapon relationship is already wrong before the effect appears, route to choreography first. If the force event is correct but the effect lacks ownership, hierarchy, integration, or lifecycle, route to VFX. If the effect is structurally correct but looks pasted into the plate, route to material/compositing integration.

For character PVs and action showcases, run an action-density and ending audit:

- did the first frame match the requested start state?
- did the required beat order happen, or did the clip begin from the second action?
- how many seconds are spent on identity reveal, weapon/mechanism proof, action peaks, and final pose?
- did the final poster pose begin before the last 1-1.5 seconds?
- are later seconds adding new state changes, or repeating/holding a finished image?
- is the clip the intended mode: character PV, pure action showcase, fight/duel, or story beat?

Mark early terminal posing, wrong action order, or mode mismatch as major when it consumes the action budget even if the still frames look attractive.

## Output Shape

```text
验片结论：
可用状态：可用 / 有条件可用 / 建议重做

证据：
- 00:00.00-00:02.40 | 观察 | 严重度 | 置信度

保留：
- ...

主要问题：
1. 时间码 | 看到什么 | 最可能原因 | 原因层级

下一轮只改：
- 主变量：
- 次变量：
- 不要动：

提示词补丁：
...

负面限制补丁：
...
```

Do not list every tiny artifact. Lead with the few issues that determine whether the clip is usable.

## Coordination

- Use `$ai-video-iteration-doctor` for the retry patch.
- Use `$cross-shot-consistency-audit` after media inspection when the decision concerns drift across an already selected sequence; this Skill owns timestamped evidence extraction, while the audit owns the shot-by-dimension matrix and severity route.
- Use `$bounded-explore-select` when the inspected outputs are still a candidate batch and the next decision is scoring, elimination, primary/backup choice, or stopping—not sequence repair.
- Use `$cinematic-audiovisual-language` when the failure is shot logic, axis, staging, or cut design.
- Use `$character-continuity-bible` for identity, count, prop, outfit, world, or position drift.
- Use `$action-choreography-reference` for weapon weight, mass distribution, balance, traction, recoil, martial-style mechanics, and inertia-resolution failures.
- Use `$cinematic-vfx-director` for effect hierarchy, ownership, source/path/collision/decay, medium routing, impact grading, motion-effect-family selection, destruction causality, and effect/camera/sound coupling failures.
- Use `$visual-style-aesthetic-direction` for cheap, generic, or inconsistent art direction.
- Use `$ai-material-realism` for grounding, contact, texture, light, optical, or motion-realism failures.
- Use `$cinematic-music-sound-design` for sound perspective, cue, foley, silence, mix, or synchronization failures.
- Use `$creative-casebook` only after the rendered result and prompt delta can be compared.

## Guardrails

- Do not diagnose from the prompt alone when the video is available.
- Do not treat sharpness, brightness, histogram, or motion metrics as aesthetic truth.
- Do not treat PySceneDetect boundaries as editorial truth; fast movement and graphic transitions can cause false cuts.
- Do not treat silence, black, or freeze detections as defects until the intended edit is checked.
- Do not call a cut merely because frame difference is high; verify visually.
- Do not blame the model before checking prompt overload, reference conflict, source assets, mode, and workflow.
- Do not rewrite the whole prompt when one failed layer is isolated.
- Do not save private videos or extracted frames outside the task unless the user asks.
- Do not promote one ambiguous artifact into a universal rule.
