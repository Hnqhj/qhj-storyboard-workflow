# Style Presentation Affordance

Use this reference when an AI video/image prompt has a strong visual style and the presentation form—camera, editing, motion density, transition, VFX, pose holds, or action type—must fit that style.

Core rule:

```text
Style suggests presentation bias, not presentation prison.
```

A style has affordances: some shot grammar, rhythm, and motion treatments feel more native to it. But the project goal can override the default. When overriding, name the borrowed layer, keep the style's native visual language dominant, and reduce the incompatible technique to a controlled accent.

## Decision Model

Before writing shots or action, decide:

```text
base medium:
style job:
native presentation bias:
project goal:
borrowed presentation layer, if any:
blend ratio:
must-preserve style language:
must-avoid incompatible drift:
```

Example:

```text
base medium: ink wash + oil paint
style job: ritual pressure and painterly impact
native bias: held silhouettes, decisive brush wipes, negative space, fewer but stronger action peaks
project goal: energetic action PV
borrowed layer: brief action-camera proof shots from live-action fight grammar
blend ratio: 70% painterly/graphic, 30% physical action camera
must-preserve: clean paper space, brush hierarchy, strong silhouette, restrained palette
avoid: continuous handheld chase, full 3D orbit, noisy effects, random camera spin
```

## Common Style Families And Suitable Biases

Treat these as defaults. Do not force them when the user's target clearly needs another presentation form.

### 1. Ink Wash / Xuan Paper / Shui-mo

Best bias:

- large negative space, restrained shot count, decisive silhouette holds;
- brush-wipe transitions, ink bloom, dry-brush trails, paper-layer parallax;
- one or two strong action peaks instead of constant combo density;
- camera should feel like sliding across a scroll, breath, or theatrical reveal.

Useful borrowed layers:

- short impact-frame flashes;
- one functional low-angle or close contact shot if action clarity matters;
- subtle parallax depth for video.

Avoid drift:

- continuous shaky handheld;
- too many cuts;
- full-frame gray mud or mist;
- neon VFX, game-camera orbit, particle explosions.

Prompt line:

```text
画风以水墨宣纸的留白、墨色层次和决定性剪影为主；动作镜头只借用少量近身接触证明，不把全片变成真人动作片式连续跟拍。
```

### 2. Oil-Paint / Painterly Illustration / Thick Brushwork

Best bias:

- pose clarity, readable value blocks, slower premium camera, texture close-ups;
- fewer but heavier peaks, visible brush smear at impact;
- transitions through paint strokes, cloth/hair foreground wipes, light-state changes;
- camera should preserve face, hands, prop silhouette, and material strokes.

Useful borrowed layers:

- stylized action bursts, but reset quickly to readable painterly composition;
- extreme close-ups for texture or mechanism proof.

Avoid drift:

- constant motion blur that destroys brushwork;
- dirty all-over noise;
- hyper-real 3D lighting replacing painterly planes;
- over-detailed micro-actions that the style cannot display cleanly.

Prompt line:

```text
厚涂笔触是主体语言，镜头以清晰姿态、材质近景和强剪影为主；高速动作只在峰值短促爆发，之后回到可读的油画体积和笔触。
```

### 3. 2.5D Cel-Real / Fortiche-Arcane-Like Hybrid

Best bias:

- character face, expression, material hierarchy, short action phrases;
- controlled 3D camera is acceptable, but shots should keep hand-painted surface readable;
- close-ups and medium shots can carry emotion; action works best with clear contact proof and silhouette.

Useful borrowed layers:

- live-action blocking and camera grammar;
- restrained anime impact frames and hand-drawn VFX accents.

Avoid drift:

- photoreal face drift;
- flat anime simplification;
- every shot becoming a game cinematic;
- glow VFX covering acting or contact.

Prompt line:

```text
三渲二厚涂以角色表演和材质层次为核心，允许电影镜头运动，但每次高速切换后都要回到清晰脸部、身体剪影和接触点。
```

### 4. Comic / Manga / Spider-Verse-Like Graphic Animation

Best bias:

- panel-like composition, abrupt shot-scale contrast, impact frames, graphic holds;
- motion can use stepped timing, smear frames, halftone, speed-line accents, caption-free graphic rhythm;
- action can be more exaggerated because the style supports graphic discontinuity.

Useful borrowed layers:

- one continuous camera move can be used as contrast, but should not erase panel grammar;
- live-action contact proof can be reduced to one insert.

Avoid drift:

- full 24fps smooth realism everywhere;
- random comic symbols;
- excessive cuts that break screen direction;
- readable text unless required.

Prompt line:

```text
漫画感以分格式构图、极端景别跳变和短促impact frame为主；连续运镜只作为局部连接，不替代图形化剪辑节奏。
```

### 5. Stop-Motion / Cut-Paper / Shadow-Box

Best bias:

- layered depth, parallax, tactile material, controlled physical camera;
- deliberate, slightly mechanical timing; action density lower, object motion clearer;
- transitions via foreground layers, paper wipes, shadow occlusion.

Useful borrowed layers:

- action peaks can be stylized, but must remain layer-readable;
- macro close-ups of texture/material are powerful.

Avoid drift:

- fluid CG camera flying through layers;
- too many simultaneous particles;
- flattening into sticker art;
- complex fight choreography that exceeds layer readability.

Prompt line:

```text
剪纸/定格感以层间景深、材质投影和可触摸运动为主；动作保持少而清楚，镜头偏物理推拉和层间视差，不变成流体CG飞镜。
```

### 6. Woodcut / Linocut / Hard Graphic Print

Best bias:

- violent silhouettes, high contrast, carved negative shapes;
- strong diagonal action, hard pose holds, graphic match cuts;
- fewer colors and fewer effects; impact comes from shape violence.

Useful borrowed layers:

- brief anime timing or impact frame;
- limited camera moves that preserve figure-ground clarity.

Avoid drift:

- soft painterly rendering;
- gray midtone mush;
- decorative fragment clutter;
- realistic glossy material everywhere.

Prompt line:

```text
木刻/版画感以硬黑白剪影、刻痕边缘和强图形构成为主；动作可激烈，但必须以大形和负形变化表现，不靠满屏粒子。
```

### 7. Editorial Fashion / Character PV

Best bias:

- face, body line, outfit, attitude, short prop proof;
- camera slower and more composed; action is a signature gesture, not full fight;
- transitions through pose match, graphic wipe, cloth/hair, light sweep.

Useful borrowed layers:

- one or two action accents to prove weapon/personality;
- music-video montage if color and expression stay dominant.

Avoid drift:

- turning the whole clip into training-room action;
- hiding face behind blur;
- losing body/outfit readability;
- generic fight-camera language.

Prompt line:

```text
这是角色PV，镜头优先展示脸、身材线条、服装和性格；动作只作为签名能力证明，不让连续打斗吞掉角色展示。
```

### 8. Live-Action Cinematic / IMAX / Practical-Light Film Look

Best bias:

- continuous blocking, real camera physics, motivated light, lens and material realism;
- stronger tolerance for handheld, tracking, dolly, crane, POV, and spatially complex fights;
- action should preserve geography, support, contact, recoil, and environmental reaction.

Useful borrowed layers:

- graphic impact frames only as tiny accents;
- stylized color rules can override full realism.

Avoid drift:

- cartoon pose holds without reason;
- effects replacing physical contact;
- style-name salad that makes the look neither film nor animation.

Prompt line:

```text
真人电影感以真实机位、连续场面调度、物理光影和接触反应为主；图形化impact frame只在命中瞬间短促出现，不改变全片媒介。
```

## Blend Ratio Heuristic

When style and desired presentation conflict, set a rough ratio:

```text
80/20: style almost fully controls form; borrowed technique is a tiny accent.
70/30: style stays dominant; borrowed shot grammar appears in key proof beats.
60/40: hybrid; both style and borrowed grammar are visible but each has a role.
50/50 or lower: risky; only use when the prompt clearly names the hybrid logic.
```

Example:

```text
水墨油画 + 高速动作 = 70% painterly staged impact + 30% action-camera contact proof.
```

## Prompt Patch

Use this when the prompt risks overfitting style to one presentation form:

```text
画风只决定展现形式的默认倾向，不是硬性限制。全片保持[base style]为主语言；镜头、动作和转场向[style-native presentation]偏移，但允许为[project goal]借用[borrowed layer]。借用部分只服务[proof/function]，不改变基础画风、不覆盖角色身份、不让全片漂移成另一种媒介。
```

## Quality Gate

Before finalizing, check:

- Did you identify the style's native presentation bias?
- Did you keep it as a tendency, not a hard prison?
- If borrowing another presentation grammar, did you name the borrowed layer and its job?
- Did you set an implicit or explicit blend ratio?
- Does the global visual master stay more authoritative than local camera/action tricks?
- Would the clip still feel like the chosen style if the action/effects were reduced?
- Would the action still be understandable if the decorative style layer were reduced?

