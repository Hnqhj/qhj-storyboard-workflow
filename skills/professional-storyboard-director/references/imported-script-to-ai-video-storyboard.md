# Imported Script-to-AI-Video Storyboard Systems

## User-Calibrated Packaging Override

When `$narrative-camera-groups` is active, preserve this reference's story, shot, continuity, and feasibility methods but replace its generic 4-15 second generation-unit and front-stage format defaults. Use approximately 20-second camera groups, normally 18-24 seconds and never over 30 seconds; show exact per-shot timing in a human-only table; then provide one complete prompt per group that independently restates every shot in concrete prose.

Use this reference when the task is closer to "剧本转 AI 视频分镜" than a normal shot list: short drama, 漫剧, 15S beat, Jimeng/Dreamina/Seedance/Kling/Sora/Veo/Runway/Pixverse-ready boards, or a script that must become clip prompts.

This distills the imported `分镜.zip` material:

- `凡是皆可-剧本转分镜SKILL5.0_Core`
- `凡是皆可-剧本转分镜SKILL5.0_ReferenceManual`
- `Jimeng Video Pipeline`
- `小蔡/阿咩剧本转分镜`
- selected short-drama and text-to-video prompt templates

Do not paste this whole reference into outputs. Use it as a routing and quality-control layer.

## 1. Core contract

Convert script language into things a camera can see, a microphone can hear, or an AI video model can preserve.

Hard rules:

1. Tell the truth when the script cannot be shot. Do not force weak drama into decorative shots.
2. Every shot choice must answer "why this shot, now?"
3. Do not put abstract psychology directly into a frame. Translate it into gaze, breath, posture, distance, object handling, silence, light, or spatial behavior.
4. Lock the platform output style before final formatting:
   - universal shot table;
   - Seedance/Dreamina continuous prose;
   - 15S beat board;
   - image-to-video director-frame plan;
   - prompt-ready clip package.
5. Do not repeat every character's full appearance in every shot. Declare assets once, then only mention changed state or continuity-critical details.
6. Avoid negative prompt clutter. Prefer designing the correct positive action and constraints directly.

## 2. Intake defaults

If the user does not specify format, assume:

```text
type: AI vertical short drama / AI video storyboard
aspect: 9:16 unless the project is film/trailer/commercial, then ask or infer 16:9/2.35:1
clip length: 5-15s per generated segment
language: Chinese explanation + paste-ready prompt in the user's preferred language when needed
dialogue: preserve original wording
subtitles/on-screen text: off unless requested
reference images: optional; create text asset anchors if absent
```

Ask only when missing information changes the core output:

- character, location, or action is too absent to shoot;
- the user demands strict reference-image continuity but provides no asset or text anchor;
- pure dialogue needs added business/action and the user has not authorized it;
- a platform-specific limit is material and not known.

## 3. Workflow: script to usable AI-video storyboard

Use this sequence for substantial script-to-storyboard tasks:

1. **Recognize the material**: script, prose, outline, scene beat, image prompt, existing shot list, or vague idea.
2. **Detect pressure zones**: fight/action, emotion-heavy beats, reveal/turn/payoff, dialogue bottlenecks, reference-image continuity needs.
3. **State story job per scene**: what the audience must know, feel, anticipate, or misunderstand by the end.
4. **Build asset anchors**:
   - characters: invariant appearance, costume, silhouette, status state;
   - locations: geography, light, palette, blocking affordances;
   - props: story function, scale, material, hand relation;
   - style: render/genre grammar without overloading the prompt.
5. **Plan scene/beat structure**:
   - information ladder: orientation -> intent -> obstacle -> turn -> consequence -> hook/release;
   - emotional ladder: neutral state -> disturbance -> choice/reaction -> changed state;
   - action ladder: preparation -> entry -> contact/change -> recovery/end state.
6. **Cut into generation-sized units**:
   - each clip is normally 4-15s under the generic imported workflow; use 18-24 second groups when `$narrative-camera-groups` owns delivery;
   - keep one clear action spine per clip;
   - avoid splitting a single cause-effect exchange across clips unless the endpoint is a stable continuation state.
7. **Write shot/beat cards**:
   - visual target;
   - lens/shot size/camera placement;
   - blocking and subject action;
   - camera movement;
   - sound/dialogue;
   - continuity lock;
   - AI feasibility note.
8. **Run the golden gate** before final output:
   - Is there new information or changed state?
   - Can the frame be seen or heard, not merely understood?
   - Is the camera choice motivated?
   - Can an AI video model execute it within the segment budget?

## 4. 15S beat mode

Use for vertical short drama, manhua/drama clips, or when the user says "15秒一个 beat".

Each 15S beat must include:

```text
Beat ID:
time range:
scene/location:
required characters:
required assets:
story function:
emotional turn:
camera baseline:
lighting/color:
performance timeline:
clip endpoint / continuation state:
AI video feasibility note:
```

Rules:

- A beat may be 12-18s if the scene breathes better, but do not call it 15S if the timing is wildly different.
- Keep dialogue intact.
- If the beat contains a high-precision action, use start/end state anchors from the fight/action reference.
- For multi-clip stories, the endpoint of Beat N becomes the starting state of Beat N+1.

## 5. Shot value quick map

Use natural language shot decisions, not sterile lens math, unless the user asks for cinematography tables.

Lens/space:

- 14-16mm: extreme spatial distortion, danger, impossible proximity, surreal environment.
- 24-35mm: environment, group blocking, movement through space, mixed action.
- 50mm: neutral observation, human-scale dialogue, grounded reality.
- 85mm: portrait compression, two-person pressure, contained conflict.
- 135-200mm: surveillance, isolation, facial compression, emotional distance.
- macro: object, eye, injury-free impact detail, prop transition, clue.

Aperture:

- f/1.2-1.8: extreme isolation, dark environments, micro-expression.
- f/2.0-2.8: subject emphasis, impact moment, face/object focus.
- f/4-5.6: balanced staging, two-person relation, readable action.
- f/8-11: geography, ensemble, complex blocking.

Camera placement:

- OTS/reverse: power relation and listening behavior.
- low angle: scale, threat, dominance, mythic arrival.
- high angle/top-down: tactical route, vulnerability, trapped relation.
- side 45°: body action and face readable together.
- POV: subjective pressure or tactical limitation.
- Dutch angle: instability; use sparingly.

Movement:

- push-in: narrowing attention, commitment, threat approaching.
- pull-back: reveal consequence, isolation, changed relation.
- track/follow: prove route and continuity.
- orbit: relationship shift or object/character reveal; do not overuse.
- whip pan: fast transfer of attention, action linkage.
- handheld: instability, proximity, breath, pursuit.
- static: pressure through stillness, ritual, dread, decisive evidence.

## 6. AI-video feasibility rules

For prompt-ready storyboards:

1. One dominant camera move per generated segment.
2. One main action spine per generated segment.
3. Do not ask a single clip to establish location, introduce three characters, reveal a prop, perform a fight exchange, and deliver a dialogue turn unless it is intentionally montage-like.
4. If using image-to-video, write from the first frame outward:
   - first-frame state;
   - motion initiation;
   - peak action;
   - final state.
5. If using first+last frame, design the final frame as a real stable pose, not only "after something happened".
6. If using reference images, assign each reference one primary role: identity, environment, style, motion, lighting, composition, product, or endpoint.

## 7. Output templates

### Compact scene-to-storyboard table

```text
| Beat | Time | Story job | Frame/action | Camera | Sound/dialogue | Continuity / AI note |
```

### Prompt-ready 15S beat

```text
【Beat ID / 时长】
【资产锚定】
【画面与表演时间线】
0-3s:
3-7s:
7-12s:
12-15s:
【镜头与光线】
【声音/台词】
【结尾状态】
【负向约束】only if necessary
```

### Full pipeline handoff

```text
project premise:
confirmed assets:
scene list:
beat map:
shot/clip table:
reference material plan:
continuity locks:
prompt package:
review checklist:
```

## 8. Common failure fixes

- **Decorative coverage**: replace with a shot function and a changed state.
- **Unshootable inner thought**: translate into a visible behavior, object relation, silence, or spatial change.
- **Jumping geography**: add a geography reset shot or continuous route.
- **Overlong prompt**: declare assets once, remove repeated adjectives, compress camera to one dominant move.
- **Weak dialogue scene**: add listening behavior, status shift, hand/prop business, and motivated cut points.
- **AI clip feels like slideshow**: reduce shot count, turn shots into phases inside one motion path, or split into separate clips.
