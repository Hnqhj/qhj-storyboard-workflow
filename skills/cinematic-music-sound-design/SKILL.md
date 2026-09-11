---
name: cinematic-music-sound-design
description: "Design cinematic dialogue, foley, ambience, impact, silence, music, mix hierarchy, rhythm, and sound-image relationships for film and AI video. In Liu's script-camera-group workflow, use as a separate Skill only on full depth; fast and standard planners already enforce dialogue/voice-over plus source-coupled dry foley, with music or mood layers only under explicit authority."
---

# Cinematic Music And Sound Design

## Liu Short-Drama Audio Override

When used for Liu's真人短剧 Seedance prompts, operate in **dialogue/foley
default mode**. Design clearly sourced dialogue/voice-over and dry physical
Foley/SFX: breath caused by exertion, footsteps, cloth, hand/prop handling,
weapon movement, impacts, fractures, debris, body contact, and surface response
directly caused by visible action. Add background music, score, BGM, ambience,
tension, emotional, or mood sound only when the user or authoritative script
explicitly requires it, with a concrete cue function and timing. In the default
mode, the final audio block states the audible dialogue and physical foley only;
do not insert exclusion prose into the copy-ready block.

## Bottom-Layer Reasoning

Apply `think-one-step-further` and `creative-research-first`:

- Research the musical tradition, instrumentation, production vocabulary, and current target-platform controls when the task is substantial.
- Define what music and sound do to story, not only what genre they resemble.
- Convert emotions into musical and acoustic controls.
- Preserve dialogue intelligibility, visual readability, silence, and dynamic contrast.
- Name what the user still needs: generated track, stems, sound effects, voice, edit points, or platform prompt.

## Core Intent

Treat audio as a narrative system:

```text
story function -> cue map -> musical language -> sound layers -> synchronization -> mix perspective -> generation prompt
```

For general projects, music may reveal, anticipate, contradict, transform, or release the image. In Liu's short-drama mode, use only source-coupled sound to establish material, distance, movement, scale, point of view, and consequence; no musical layer is present.

Do not add wall-to-wall music by default. In Liu's short-drama mode, omit music entirely.

## Reference Routing

Read only the useful files:

- `references/film-scoring-workflow.md`: spotting, cue boundaries, hit points, motifs, dramatic function, and score architecture.
- `references/music-control-vocabulary.md`: translate mood into rhythm, harmony, melody, orchestration, texture, dynamics, and production controls.
- `references/sound-design-and-mix.md`: dialogue, ambience, room tone, foley, hard effects, designed effects, silence, perspective, and mix hierarchy.
- `references/ai-music-prompting.md`: package prompts for Suno, Udio, and similar music generators.
- `references/source-map.md`: current source anchors and research notes.

If an existing song is already the fixed final track and the user wants the complete MV picture, choreography, formations, and edits designed around it, inspect and pass duration, tempo family, section boundaries, and selective cue evidence to `$reference-track-mv-director`. Do not redesign or replace the supplied music. This Skill remains the owner of musical interpretation and sound hierarchy; the MV Skill owns the picture contract.

## Workflow

1. Define the audiovisual job:
   - What should the audience feel, understand, anticipate, or misread?
   - Whose point of view controls the sound?
   - Use `$creative-anchor-director` when the user knows only part of the composer, genre, regional tradition, ensemble, recording, sound-design, or mix vocabulary. Preserve selected names and supplement missing audio roles.
2. Spot the scene:
   - cue in, cue out, physical hit points, transitions, dialogue priority, and final button. In Liu mode the whole cue is a no-music zone.
3. Build the musical identity when the user explicitly requests a music task or
the authoritative script requires it. Otherwise in Liu's default short-drama
mode, skip this step and build a physical Foley identity instead:
   - motif or interval shape;
   - tempo range and meter;
   - rhythmic engine;
   - harmonic language and tonal center;
   - instrumentation and register;
   - texture, density, dynamics, articulation, and production space.
4. Build sound layers:
   - dialogue/voice;
- ambience and room tone only when it is a direct physical consequence of visible action; omit generic atmosphere in Liu mode;
   - foley/body/clothing;
   - hard effects and mechanical sources;
   - designed or subjective effects;
   - music only for a separately requested music task or authoritative-script cue;
   - deliberate silence.
5. For weighted action, translate the physical profile from `$action-choreography-reference` into sound:
   - preload/support strain;
   - acceleration and air displacement;
   - material-specific contact transient;
   - body/weapon resonance;
    - receiver and environmental reaction;
    - braking, scrape, vibration, and settling.
   For a principal body hit, build one synchronized acknowledgment event rather than a generic impact layer: contact transient + clothing/body resonance + involuntary breath, restrained grunt, or breath interruption + foot/ground correction + room or environmental tail. Match the vocal intensity to the hit grade and visible facial/physiological response. Minor contacts receive shorter, quieter proof so audio density does not slow or flatten a fast exchange.
   For visible terrestrial locomotion, place the main footfall transient at load acceptance rather than at arbitrary leg motion; match the substrate, weight, pace, and distance perspective, then let clothing, hair ornaments, gear, water, gravel, or debris answer with a short delayed layer. Do not exaggerate every step equally.
6. Design sound-image relation:
   - synchronize, anticipate, trail, bridge, contradict, mask, reveal, or drop out.
7. Map time:
   - attach changes to story beats, not every cut.
8. Protect the mix:
   - establish foreground, midground, background, frequency space, transient priority, and dynamic headroom.
9. Package:
   - audiovisual cue sheet;
- AI music prompt only for a separately requested music task; omit in Liu mode;
   - sound-design prompt;
   - optional editing/stem plan.

## Musical Translation Rule

Skip this section in Liu's default short-drama mode unless an explicit music or
ambience cue is authorized; otherwise use physical Foley descriptions instead.

Never stop at an adjective:

- "紧张" -> unstable pulse, narrow repeated cell, low pedal, rising register, compressed harmony, restrained dynamics before rupture.
- "悲伤" -> choose grief type: numb, intimate, regretful, ceremonial, or catastrophic; then define tempo, contour, harmony, register, and space.
- "高级" -> restrained motif count, intentional silence, controlled orchestral density, coherent timbre family, clean transient hierarchy, and no trailer-cliche overload.
- "速度感" -> subdivision, syncopation, ostinato, acceleration illusion, bass articulation, transient design, and contrast against held moments.
- "未来感" -> define synthesis method, modulation, spectral texture, rhythmic machine logic, and acoustic/electronic relationship.

## Short-Form Audio Contract

For 5-15 second video, use one memorable audio idea and a clear change:

```text
orientation -> pulse/motif enters -> pressure grows -> hit/drop/reveal -> aftermath or sonic button
```

Possible 15-second map:

```text
0-2s: room tone, source sound, or motif seed
2-5s: rhythmic engine appears
5-8s: instrumentation or register expands
8-11s: interruption, false drop, or harmonic turn
11-13s: impact/reveal with transient focus
13-15s: tail, silence, unresolved tone, or logo/end button
```

Do not force this template when the scene needs sustained dread, realism, comedy timing, or silence.

## Output Shapes

For a scene:

```text
声音叙事目标：
主观视角：
Spotting / 配乐进入退出：
主题动机：
节奏与速度：
和声与旋律：
配器与音色：
声音层：
声画同步点：
静默与留白：
混音层级：
```

For an AI music prompt:

```text
用途与时长：
结构：
音乐身份：
节奏/BPM/拍号：
和声/调式：
旋律/动机：
配器/音色：
演奏法/人声：
动态与制作：
情绪弧线：
排除项：

完整提示词：
...
```

For video handoff:

```text
音乐提示词：
声音设计提示词：
时间码与卡点：
需要准备的音频素材：
```

## Quality Gate

- Does the cue have a dramatic function?
- Are cue-in and cue-out intentional?
- Is the music perspective compatible with the character or world?
- Does the motif change when the character or meaning changes?
- Are tempo, meter, rhythm, harmony, orchestration, register, density, and dynamics specified only as needed?
- In Liu mode, are dialogue/voice-over, source-coupled foley, and silence
  prioritized, with music, ambience beds, and mood effects present only when
  explicitly authorized?
- Are hit points selective rather than every cut being synchronized?
- Is there contrast before impact?
- For weighted action, do startup, contact, resonance, environmental response, and settling sound like one causal event?
- Can the audio plan be generated, edited, and mixed with the available tools?

## Guardrails

- Do not use only genre names, moods, BPM, or "cinematic epic".
- Do not make every action produce a huge impact.
- For Liu's short-drama mode, include no music unless the user or authoritative
  script explicitly authorizes a concrete cue.
- Do not let bass, impacts, and score mask dialogue or important source sounds.
- Do not ask for contradictory production such as intimate dry chamber music and enormous wet arena reverb without a transition.
- Do not make the user supply complete music and sound reference vocabulary. Preserve useful composer, genre, tradition, ensemble, recording, and sound-design anchors; add mechanics only to clarify their role or keep the result original and coherent.
- Do not assume current AI music controls; check official documentation when the target platform matters.
