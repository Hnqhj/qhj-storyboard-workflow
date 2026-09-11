---
name: seedance-audio
description: "This skill should be used when the user asks for Seedance 2.0 audio, dialogue, lip-sync, music, sound effects, ambience, beat-sync, audio-reference mapping, reference audio used as a visual motion/edit control track, desync troubleshooting, or sound-driven visual timing."
license: MIT
metadata:
  version: "6.2.0"
  updated: "2026-07-17"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-audio

## Liu Default Audio Contract

When this skill is used for Liu's真人短剧生成，项目级音频规则覆盖本技能的通用音乐/氛围能力：只输出人物台词与明确物理来源的纯拟声音效。禁止背景音乐、配乐、BGM、音乐性节拍、氛围铺底、风铃、紧张低频、情绪音垫、悬疑提示音和任何只表达情绪或氛围的声音。参考音频和控制 WAV 默认不生成；只有 Liu 明确批准“干拟声节奏测试”时，才可生成只含台词与物理拟声的音频文件。

Use this for dialogue, lip-sync, physical foley, desync troubleshooting, or sound-driven visual timing. In Liu mode, audio supports the visible beat through dialogue and source-coupled foley only; do not introduce music or mood sound design.

Load `[ref:audio-guide]` for detailed constraints, beat-sync, desync repair, audio-reference conflicts, and multi-character workarounds. Load `[ref:reference-audio-visual-control]` when reference audio should shape visible action speed, impact peaks, cuts, shot scale, or section rhythm through a custom cue track or fixed music. Load `[ref:audio-post-delivery]` when the user needs stems, M&E, dubbing, loudness, sync, mix, or delivery guidance.

## Intent

Half of every emotion enters through the ears, and users almost always forget sound until its absence makes the clip feel dead. The soul here is giving every scene its sound before being asked - the room's breath, the action's evidence, the line that lands. When they hear it, they realize it was always part of what they meant.

## Core Rules

Keep dialogue short, quote spoken lines, and assign every line to a named speaker. Prefer locked or stable framing for lip-sync. Remove head-turning, large face motion, extreme camera moves, or busy hand gestures while mouth accuracy matters. Treat `[Audio1]` as a rhythm, pacing, mood, voice-tone, ambience, or tested visual-timing condition unless the active platform documents exact playback behavior. Never turn a field-observed sound-to-picture tendency into a deterministic cue dictionary.

When used in Liu's five-view character workflow, write every named speaker and character reference with the exact platform handle `@角色名` in model-facing audio/prompt text (for example `@苏凌月`); keep uploaded audio/file references in their exact `{{Audio N}}` form.

When the user already supplies a fixed final song, that song is outside Liu's default short-drama contract; do not introduce or bind it in ordinary short-drama prompts. For a separately requested music-video task, route the song workflow explicitly. Do not create a control WAV unless a one-variable dry-foley diagnostic is explicitly approved.

## Prompt-time Reference Audio Gate

For Liu's short-drama mode, this gate is opt-in rather than automatic. Skip it for ordinary dialogue, emotion, action, VFX, and continuous-shot prompts. Only enter it when the user explicitly approves a dry foley timing test; the payload and returned file must contain dialogue/physical foley cues only and no music, ambience, emotional, or mood layers.

When Liu asks for a final video prompt, decide backstage whether a reference-audio control track materially improves the result. Do not wait for him to ask for the audio separately.

Create the track together with the prompt when at least one condition is true:

- the clip needs selective impact, dash, transformation, reveal, edit, or shot-scale peaks at named moments;
- music section changes are meant to control the visual arc or exact ending;
- a multi-beat action, chase, PV montage, dance, ritual, or transformation has a fixed target duration and text-only timing is likely to remain soft;
- a prior attempt ignored, reordered, or evenly spread the intended beats;
- Liu explicitly asks for 卡点, 音效/音乐控制画面, 参考音频, or stronger duration/rhythm control.

Do not create one for a simple continuous shot with no meaningful timing problem, pure prompt discussion without a target clip, dialogue/lip-sync work where another audio role already owns the reference, or a platform that cannot accept audio reference. In those cases keep a compact visible beat map in text.

Choose the smallest useful mode:

- `sfx`: exact motion/impact/transition points; default for action and first validation;
- `music`: emotional or montage structure without exact physical hits;
- `hybrid`: both section-level musical form and a few indispensable action peaks.

Liu exception: do not use `music` or `hybrid` mode. An explicitly approved timing test uses `sfx` only, with dry dialogue/foley cues and no musical or atmospheric layer.

Before delivering the prompt, make the visible beat map, sparse cue list, exact target duration, and role contract. Then write a UTF-8 payload and run:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/create_reference_audio.ps1 -PayloadFile "<payload.json>"
```

Minimum payload:

```json
{
  "projectId": "resolved current project or omitted for active-profile fallback",
  "profileId": "resolved episode/profile when available",
  "duration": 10,
  "mode": "sfx",
  "bpm": 96,
  "name": "shot-purpose_control_v01",
  "description": "the visible event path",
  "musicPrompt": "only for music or hybrid",
  "cues": [
    { "time": 1.2, "label": "sudden dash" },
    { "time": 5.8, "label": "decisive impact" }
  ]
}
```

Use the current task's explicit project/episode first, then the workbench active profile. If neither is reliable, let the adapter use Pending Review. Preserve the returned WAV, `.prompt.md`, `.meta.json`, SHA-256, cue map, and role contract. In the final paste-ready prompt bind the uploaded file as `{{Audio N}}（画面节奏控制参考）` or the exact platform equivalent and state that it controls visible timing, not the final mix. When actual image/video generation begins, pass the returned path/hash/cue map into `$generation-asset-pipeline` as `settings.referenceAudio`.

## Sound Layer Pattern

Use compact Liu layers: `Dialogue: ... Foley: ... Silence: ...`. Include only source-coupled physical sounds. State `no music, no score, no ambience bed, no emotional or mood effects`; silence is valid when it sharpens drama or avoids confusing lip-sync.

| Need | Stable audio direction |
|---|---|
| Lip-sync | `Character A, locked medium close-up, says "I found it." Clear dry dialogue, no head turn.` |
| Product ad | `Sound: low room tone. SFX: magnetic click on lid open, soft glass chime at final frame.` |
| Beat sync | `[Audio1] provides tempo only; light pulses and foot taps match the downbeat.` |
| Drama | `Distant rain and refrigerator hum; no music during the line.` |
| Action | `Breathing grows louder, shoe squeak at landing, metal door buzzer at endpoint.` |
| Visual control track | `[Audio1] controls visible timing only: first short whoosh = dash, strongest transient = sole impact peak, final gap = changed end state; final mix is separate.` |

## Multi-Character Dialogue

Use one speaker per short clip when reliability matters. If two characters must speak, separate turns and keep the camera stable: `Character A says... pause. Character B answers...`. For complex exchanges, recommend generating controlled single-speaker clips and compositing in post.

## Failure Fixes

If dialogue desyncs, shorten the line, lock the camera, remove head turns, clean the audio role, and reduce competing SFX. If the wrong speaker talks, assign tags and split lines by speaker. If audio is ignored, remove extra music/SFX instructions and make the reference role explicit.

If audio and video references fight each other, mute the reference video before upload when possible, or make the priority explicit: `[Video1] controls camera only; [Audio1] controls tempo and energy`.

## Sequence State

When sequence state is present, inherit completed dialogue, active dialogue, ambience, music phase, SFX phase, current clip scope, continuity locks, exact reference tags, and reserved future beats. Do not repeat completed dialogue unless the user explicitly asks for a reprise. Continue or intentionally change the audio phase instead of restarting it by accident.

## Output Contract

Return speaker map, quoted dialogue, physical foley layers, lip-sync constraints, and a compact prompt-ready audio block. For Liu's default short-drama mode, do not return a music plan or reference WAV; the front-stage package is `人物台词 + 纯拟声音效 + 静默节点`. Only an explicitly approved dry-foley timing test may add a reference-audio path, cue map, and upload role.
