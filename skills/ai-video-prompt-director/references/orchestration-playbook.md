# AI Video Prompt Orchestration Playbook

This playbook combines the user's specialist skills into one practical workflow.

## Core Pipeline

Use this order for most prompt work after applying the current routing overlay below:

```text
Phase 0 Intent Reading -> Video Structure -> Story Craft -> Production Design -> Universal Aesthetic Direction -> Audiovisual Grammar -> Reference Board -> Continuity Locks -> Mechanical Transformation -> Visual Language -> Action Reference -> Rhythm -> Material/Render Physics -> Model Packaging -> Preflight QA -> Iteration Diagnosis
```

Current routing overlay, updated 2026-06-29:

- For substantial new creative prompts, run `$creative-research-first` before ideation; if the user has partial named anchors, asks for stronger aesthetic/camera/action vocabulary, or leaves reference functions uncovered, use `$creative-anchor-director` before specialist work.
- When the user asks for 分镜, storyboard, shot list, 镜头表, or a shot-by-shot board, route through `$professional-storyboard-director` after macro structure and before final prompt packaging; pair it with `$cinematic-audiovisual-language` for continuity and `$high-tension-shot-design` only when tension is actually required.
- When strict layout, camera path, action blocking, scale relation, or animatic/previs proof needs a 3D reference, route through `$blender-mcp-previs` before model packaging. Use whitebox/blockout renders as functional references, not as style references.
- When music, sound, dialogue, ambience, foley, silence, or sound-image timing matters, insert `$cinematic-music-sound-design` between audiovisual grammar and material/render, not as a final BGM afterthought.
- For high-energy action, aggressive POV, giant/mecha motion, or extreme shot-scale contrast, add `$kinetic-action-visual-master` before detailed shot/action/rhythm design. For pure weapon, armor, movement-system, or character-ability showcases without an opponent, use `$action-showcase-direction` before the detailed action chain.
- If the output will be generated, reviewed, compared, or retried as a project, bind the exact prompt and reference roles with `$creative-production-ledger` before generation, then close the loop with `$ai-video-output-review` -> `$ai-video-iteration-doctor` -> `$creative-casebook`; use `$capsule-engine` only when evidence, boundaries, and reuse value are clear.
- For SD2 / Seedance behavior, check current official/platform documentation before relying on duration, audio/reference, or mode-specific limits. Keep the prompt architecture role-based rather than parameter-specific unless the current endpoint has been verified.
- When the target is specifically Seedance 2.0, keep director mode responsible for structure/world/camera/action/sound/material decisions, then route final packaging, continuation/extend, first-last-frame, reference-to-video, platform/API facts, safety rewrites, and failed-output repair through `$seedance-20`. Use `$jimeng-sd2-prompting` for generic 即梦 SD2 packaging or when the target tool is unclear.

Meaning:

1. **Phase 0 Intent Reading**: What is Liu literally asking for, what feeling or creative itch is probably behind it, which direction fits Liu's taste, and what directions should be avoided before stack selection?
2. **Video Structure**: What are the hook, duration map, escalation, turn, payoff, loop/CTA, and retention resets?
3. **Story Craft**: Who wants what, what blocks them, what choice/cost changes the scene?
4. **Production Design**: What world rules, color ownership, locations, materials, props, vehicles, costumes, and forbidden drift keep the scene coherent?
5. **Universal Aesthetic Direction**: What medium domain, style family, visual rules, color ownership, rendering hierarchy, and anti-cheapness constraints define the look?
6. **Audiovisual Grammar**: Which shot functions, screen direction, staging, continuity edits, and sound-image beats make the structure readable?
7. **Reference Board**: What should the user look at or search for before prompting?
8. **Continuity Locks**: What must stay identical across frames or clips?
9. **Mechanical Transformation**: If an object changes form, where do parts unfold, slide, rotate, tension, and lock?
10. **Visual Language**: Which camera/composition/reference terms create that feeling?
11. **Action Reference**: Which real or stylized movement basis makes the action believable?
12. **Rhythm**: Where are the anticipation, peak, impact, and recovery?
13. **Material/Render Physics**: What AO/contact shadow/PBR/roughness/reflection/volumetric/motion controls prevent AI plasticity?
14. **Model Packaging**: How should this be structured for 即梦 SD2 / Seedance or another video model?
15. **Preflight QA**: Is the final prompt feasible, non-contradictory, properly locked, and worth generating as one clip?
16. **Iteration Diagnosis**: If the result fails, what single variable changes next?

## Planning Order Versus Prompt Order

Keep two different orders:

```text
planning:
phase-0 intent reading -> structure -> causality -> visual system -> shots -> timing

final generation prompt:
角色/资产锁定（含 `@图片名（...参考）`、`@视频名（...参考）` 等精确句柄）
-> 视觉材质总控 -> 镜头语言总控
-> 事件节拍（动作/状态/接触/后果；仅特殊镜头节拍补触发与可见运镜结果）
-> 声音 -> 正向稳定约束
```

Structure is designed first, but the global visual master is written early in the final prompt because it defines the visual domain inherited by every later shot.

Timing maps are directing tools with a confidence gate:

```text
high confidence: exact macro-segment ranges + flexible internal cuts
medium confidence: approximate ranges or duration proportions
low confidence: untimed causal order
```

High confidence may come from reviewed reference footage, a successful prior output, an animatic/edit map, external synchronization, or a defensible action-phase budget.

## Skill Roles

### `$video-structure-design`

Use for:

- 视频结构, 开头钩子, 留存, 时长分配, 预告片/广告片/MV/角色出场/15秒/30秒/60秒结构.
- Complaints that a clip has shots but no structure, repeats the same idea, starts too slow, or lacks payoff.

Output contribution:

```text
视频任务：角色出场。开场异象钩子 -> 空间定向 -> 行动启动 -> 障碍/尺度转折 -> 最强峰值 -> 结尾按钮/循环点。
```

### `$screenwriting-story-craft`

Use for:

- 剧本, 故事, 人物动机, 冲突, 反转, 对白, 潜台词, 场景目标, emotional hook.

Output contribution:

```text
角色想穿过封锁区取回被城市删除的身份码；阻力是会抹除记忆的白色交通系统；她选择公开越界，代价是被全城标记。
```

### `$cinematic-audiovisual-language`

Use for:

- 视听语言, 镜头功能, 景别, 机位, 轴线, 屏幕方向, 场面调度, 镜头组接, 声画关系.
- Complaints that camera design is weak, repetitive, incoherent, or only "cool words."

Output contribution:

```text
克里斯托弗·诺兰风格 + IMAX尺度的大远景与低机位仰拍建立城市压迫；这条完整镜头风格只写入 `镜头语言总控`，普通事件节拍默认继承。
```

### `$production-design-worldbuilding`

Use for:

- 世界观, 美术设定, 场景统一, 城市设计, 道具/载具/服装设计, 颜色体系, 反差背景.
- Complaints that a world feels generic, pasted together, random, or visually inconsistent.

Output contribution:

```text
世界拥有象牙白陶瓷高架、珊瑚红管制面板和金色日光；角色独占黑色、电光青和银色。城市规则是“公共空间不允许阴影”，所以她的哑光黑车身像非法阴影穿过系统。
```

### `$visual-style-aesthetic-direction`

Use for:

- 风格化, 审美, 画风, 高级感, 通用审美, visual style, aesthetic direction.
- Complaints that a result feels cheap, generic, AI-looking, aesthetically weak, or inconsistent.

Output contribution:

```text
媒介域是2.5D角色+真实3D场景；主审美是editorial cyber fashion，辅助为minimal industrial futurism。角色使用cel-shaded平面和稳定线稿，场景使用PBR陶瓷/金属/玻璃材质，同一侧逆光把两层粘合。禁止霓虹赛博泛滥、随机UI、塑料CG和风格跳变。
```

### `$reference-hunting-board`

Use for:

- "I need references but don't know what to search."
- Film frames, action videos, weapon movement, materials, lighting, moodboards.

Output contribution:

```text
参考板分区：核心镜头参考搜 "low angle sword draw rain night cinematic shot"；动作参考搜 "iaido draw cut slow motion reference"；材质参考搜 "wet black leather metal scratches macro".
```

### `$character-continuity-bible`

Use for:

- Identity, costume, weapon, prop, scene, and multi-shot continuity.
- Complaints about face, clothes, weapon, or background changing.

Output contribution:

```text
全程保持同一角色五官、黑色长皮衣、红色机械弓、雨夜霓虹巷道；只允许发丝、衣摆、水面和金属高光变化。
```

### `$mechanical-transformation-design`

Use for:

- Transforming weapons, deployable armor, folding bows, telescoping limbs, hinge/rail/cam/pulley mechanics.
- "Small bow becomes large bow" or any object changing scale.

Output contribution:

```text
小弓红色核心亮起，卡扣解锁；上下弓臂沿铰链分段展开，伸缩轨道拉长，剪式连杆撑开弧度，凸轮滑轮旋转拉紧红色弓弦，最后锁止机构咔哒闭合。
```

### `$visual-reference-vocabulary`

Use for:

- "I want tension but don't know the term."
- Camera, composition, lighting, director shorthand, anime impact, commercial polish.
- Examples: Spielberg push-in, Kubrick one-point perspective, Hitchcock dolly zoom, Obari pose, negative space, foreground occlusion.

Output contribution:

```text
大张克己风格 + 低机位短弧绕与三角构图让武器强斜线形成英雄压迫感；起势触发镜头跟随武器侧肩线移动，峰值后交接收势轮廓。
```

### `$action-choreography-reference`

Use for:

- Fight/action/weapon/chase movement.
- Real movement basis: boxing cross, kesa-giri, iaido draw cut, bo staff figure-eight, rope-dart arc, parkour vault.

Output contribution:

```text
动作以 kesa-giri diagonal cut 为基础，刀刃从右上肩线斜切到左下髋线，身体重心随刀势下沉，收势有清晰 follow-through。
```

### `$ai-material-realism`

Use for:

- Anything that must look real, tactile, or commercial.
- Skin, metal, fabric, rain, wet street, glass, rust, scratches, dirt, reflections.

Output contribution:

```text
黑色金属刀身有不均匀粗糙度，刃口形成冷色锐利高光，握柄有磨损和指纹油污，雨水只在局部形成镜面反射。
```

Render vocabulary contribution:

```text
使用tight ambient occlusion固定脚底、衣料重叠和装甲缝隙；PBR roughness map区分哑光黑涂层与磨亮边缘；brushed metal使用anisotropic highlights；场景用soft global illumination bounce和contact shadows让角色不贴片。
```

### `$jimeng-sd2-prompting`

Use for:

- Final prompt structure for 即梦 / SD2 / Seedance.
- Mode selection: text-to-video, image-to-video, first-last frame, multi-reference, shot list.

Output contribution:

```text
模式：图生视频。以@角色构图.png（角色外观与构图参考）锁定角色，生成5秒动作镜头...
```

### `$action-rhythm-editing`

Use for:

- Timing, beats, slow motion, impact frames, music sync, action pacing.

Output contribution:

```text
短暂起势后突然爆发，冲击峰值出现极短 impact pause，随后完成 follow-through 和稳定收势；不指定秒数，除非必须与音乐重拍同步。
```

### `$ai-video-iteration-doctor`

Use for:

- Results that failed, drifted, flickered, felt soft, or need retry.

Output contribution:

```text
下一轮只改动作峰值：保留人物和构图，加入0.2秒impact pause和武器follow-through，不改场景和镜头。
```

### `$ai-video-prompt-preflight`

Use for:

- Final checks before generation, prompt QA, feasibility, splitting, contradictions, model-risk diagnosis, and retry plan.

Output contribution:

```text
最大风险：15秒内镜头过多且车辆跳跃+城市远景+面部特写容易漂移。建议保留5-6段，明确@人物身份.png（人物身份与服装参考）、@摩托设计.png（摩托设计参考）、@城市空间.jpg（城市空间与色调参考）。
```

## Combination Recipes

### 1. Action Hero Shot

Use:

```text
$video-structure-design + $production-design-worldbuilding + $visual-style-aesthetic-direction + $cinematic-audiovisual-language + $character-continuity-bible + $visual-reference-vocabulary + $action-choreography-reference + $action-rhythm-editing + $ai-material-realism + $jimeng-sd2-prompting + $ai-video-prompt-preflight
```

Recipe:

```text
视觉：大张克己风格 + 低机位短弧绕与三角英雄剪影
动作：weapon diagonal cut / spear thrust / rope-dart arc
节奏：起势 -> 爆发 -> impact pause -> follow-through
材质/渲染：AO/contact shadows + metal roughness + anisotropic highlights + sparks + cloth follow-through
模型：5秒，one action beat；镜头总控写完整风格，事件节拍写动作与状态；只有特殊镜头需求才补 trigger + visible result
```

Example final block:

```text
5秒图生视频。以@角色五视图.png（角色五官、服装与武器外形参考）锁定角色。角色从静止起势进入一记 kesa-giri diagonal cut：刀刃从右上肩线斜切到左下髋线，身体重心随刀势下沉，披风和发丝沿斜线甩动。《浪客剑心》风格 + 低机位35mm推近与15度短弧绕让脚底支撑、刀线和接触面持续清楚；动作启动触发镜头跟随持刀侧肩线靠近，命中拖尾带动镜头交接到收势方向。黑色金属刀身有不均匀粗糙度和冷色刃口高光，雨水在地面形成局部镜面反射。同一人物、同一服装与同一武器长度持续稳定。
```

### 2. Emotional Reveal

Use:

```text
$visual-reference-vocabulary + $ai-material-realism + $jimeng-sd2-prompting
```

Recipe:

```text
视觉：史蒂文·斯皮尔伯格风格 + 缓慢推近完成表情揭示
材质：skin SSS / eye moisture / dust light
模型：眼线上抬触发镜头跟随面部轴线推近，证明情绪变化并停在稳定近景
```

### 3. Product / Commercial Shot

Use:

```text
$video-structure-design + $visual-reference-vocabulary + $ai-material-realism + $jimeng-sd2-prompting
```

Recipe:

```text
视觉：苹果产品广告摄影风格 + 微距滑轨与受控高光在负空间中揭示产品轮廓
材质：roughness map / micro scratches / wet-dry boundary / glass clarity
模型：产品转动触发镜头跟随边缘沿滑轨路径移动，证明材质与结构并停在品牌英雄角度
```

### 4. Chase / Parkour Shot

Use:

```text
$action-choreography-reference + $visual-reference-vocabulary + $jimeng-sd2-prompting
```

Recipe:

```text
动作：kong vault / wall run / slide under obstacle
视觉：《暴力街区》风格 + 低机位贴身追拍保持跑酷路线、脚底与障碍接触清晰
模型：动作触发镜头跟随身体重心沿路线追踪，穿越障碍后交接落地制动；full-body framing, one movement per clip
```

### 5. Anime Impact Shot

Use:

```text
$visual-reference-vocabulary + $action-choreography-reference + $jimeng-sd2-prompting
```

Recipe:

```text
视觉：Obari pose / Kanada effects / impact frame
动作：real movement base plus exaggerated timing
模型：brief impact pause, sharp silhouette, no anatomy collapse
```

### 6. Reference Research Pass

Use:

```text
$reference-hunting-board + $visual-reference-vocabulary + $action-choreography-reference
```

Recipe:

```text
参考板：核心镜头 / 动作 / 材质 / 避免方向
提炼：把参考变成镜头、动作、材质词
下一步：再进入 SD2 prompt packaging
```

### 7. Retry / Fix Pass

Use:

```text
$ai-video-iteration-doctor + the broken layer's specialist skill
```

Examples:

```text
脸变了 -> $character-continuity-bible
动作软 -> $action-choreography-reference + $action-rhythm-editing
质感假 -> $ai-material-realism
运镜乱 -> $visual-reference-vocabulary
提示词结构乱 -> $jimeng-sd2-prompting
```

### 8. Transforming Weapon Showcase

Use:

```text
$character-continuity-bible + $mechanical-transformation-design + $action-choreography-reference + $action-rhythm-editing + $ai-material-realism + $jimeng-sd2-prompting
```

Recipe:

```text
小形态：轻、快、单手、连射、旋身。
变形段：解锁 -> 铰链展开 -> 伸缩轨道 -> 凸轮拉紧 -> 锁止。
大形态：重、慢、借力、脚踩/地面锚定/双手拉弓。
稳定：同一角色、同一核心握把、同一红色弓弦、同一黑红机械材质。
```

## Prompt Assembly Template

Keep mode, timing confidence, missing assets, risk notes, specialist routing, and preflight outside the paste target. Compile the final generation prompt into this fixed six-part pattern:

```text
【角色/资产锁定】
@实际图片名（...参考）：...  # 使用用户上传的真实图片名

【视觉材质总控】
[medium / aesthetic family / palette ownership / material-light system / rendering hierarchy]

【镜头语言总控】
[complete camera style: named aesthetic anchors / perspective / lens family / distortion / movement energy / framing-edit rhythm / transition-reveal logic]

【事件节拍】
[current visible opening state + causal state changes]
[action/state/contact/consequence beats; local trigger + visible camera result only for a genuine special-camera need]

【声音】
[sound focus / cue change / silence / impact / ambience]

【正向稳定约束】
[present-state identity / prop / world / camera / material / action-path locks]
```

## 15-Second Structure And Shot Discipline

When the user asks for a 15-second generated clip, do not default to 3 shots. First choose a structure, then design shots.

Default 15s planning rhythm; do not paste these intervals into the generation prompt unless synchronization is required:

```text
0-1.5s hook image
1.5-4s orientation / rule of the world
4-7s escalation / first action
7-10s turn / obstacle / scale change
10-13s strongest peak
13-15s payoff / exit / loop
```

For each beat, fill:

```text
function -> visible image -> X风格 + concrete visible camera result -> tracking owner -> shot size/camera height/lens -> camera path -> action/impact/occlusion trigger -> screen direction -> subject action -> proof/new information -> handoff/endpoint
```

Revise if adjacent beats repeat the same shot size, camera height, camera path, and action verb. If the subject is moving through a city, one beat can be a side track, but the next should change viewpoint or information: low launch, extreme wide scale, overhead route reveal, foreground rupture, reflection pass, obstacle, or consequence.

For manga/comic-style cutting, preserve screen direction and make the cuts feel like panel composition: different scale, different silhouette, clear graphic contrast, but one readable spatial path.

## Standalone Segment Protocol

Use this whenever the user generates clips one by one, even if the conversation has a story order. Assume the video model only sees the current references and the current prompt.

Before writing the final prompt, declare:

```text
独立生成；以@当前参考图.png（人物身份、外观与当前场景参考）为主要视觉基准；开场第一帧已经处于[当前形态/当前场景/当前姿势]。
```

Rules:

- Do not write "上一段之后", "小弓刚刚变成大弓", or "承接前面" unless the model is actually receiving the prior clip or tail frame.
- If a prior state matters, encode it as a visible starting state: "开头就是巨型弓形态", "开头弓体已经完全展开".
- Lock the form state separately from the identity: small bow, giant bow, damaged armor, wet street, charged energy, etc.
- For a sequence, write each clip as self-contained, then use editing to connect them.

Standalone prompt skeleton:

```text
【角色/资产锁定】
@当前参考图.png（人物身份、服装、武器与色调参考）：开场第一帧已经是[明确形态]。
【视觉材质总控】
[当前可见材质、光线、色彩与渲染行为]
【镜头语言总控】
[complete camera style: named aesthetic anchors / perspective / lens family / distortion / movement energy / framing-edit rhythm / transition grammar]
【事件节拍】
[写动作、状态、接触与后果；仅特殊镜头节拍补写触发原因与可见运镜结果]
【声音】
[ambience / cue / impact / silence]
【正向稳定约束】
[身份、形态、武器、场景、镜头锚点与动作路径持续锁定]
```

## Diagnostic Checklist

When rewriting a weak prompt, check:

- Is the intended feeling named?
- Are reference roles clear?
- Are identity/prop/background locks explicit?
- Is there one readable action?
- Is the action grounded in a real reference?
- Does the action have anticipation, peak, and follow-through?
- Is camera movement limited and purposeful?
- Are material details physical, not just "high quality"?
- Are negatives specific to likely failure modes?
- For a 13-15 second action showcase, is the character visibly changing position every beat instead of standing in place?
- Are there enough distinct action peaks to fill the duration, rather than one or two moves stretched into slow, weak motion?
- If the weapon is fantastical, does the choreography use real motion only as the weight/footwork base, then add stylized weapon functions, exaggerated perspective, and readable anime-impact peaks?
- If the clip is generated independently, does the prompt state the current form at frame 1 instead of relying on conversation history?
- Does each 15-second action segment contain enough different verbs, positions, weapon functions, and camera tension peaks?
- Does the strongest moment have a planned hero composition, not just "cool action"?
- Does the world have color/material/design rules, not just a list of aesthetics?
- Has the final prompt passed preflight for contradictions, timing overload, reference roles, and split strategy?

## User-Proven Action Showcase Lesson

For 15-second weapon/action showcase clips, avoid "one pose plus a few repeated attacks." That often becomes standing, slow, and weightless in AI video. Design the clip as mobile action:

- Require visible displacement: run, slide, retreat, dodge, jump, land, change direction, or cross the frame.
- Use 5-6 distinct action peaks across 15 seconds, usually one peak every 2-3 seconds.
- Keep peak pauses very short: about 0.08-0.12 seconds for impact frames, not long slow motion.
- If the weapon can do more than one thing, name those functions: shooting, blade sweep, guard, hook, chain arc, energy string, or melee transition.
- Use real actions only as the body mechanics base. Add fantasy style through exaggerated lens perspective, foreground weapon passes, energy trails, Obari/Kanada-style silhouettes, and impossible-but-readable weapon arcs.
- When a first version feels good but stands still, preserve the successful visual language and change only the spatial action variable: add moving shots, moving attacks, and moving camera.

## Reality-To-Fantasy Escalation

When the user wants action that is interesting rather than merely realistic, build in three layers:

1. **Reality base**: footwork, balance, leverage, draw mechanics, blade arc, shoulder line, landing, recoil.
2. **Fantasy function**: what the prop can do beyond reality: bow as blade, bow as shield, chain arc, energy string, telescoping limb, ground anchor, foot loop, recoil burst.
3. **Visual exaggeration**: low-angle wide lens, foreground weapon breaking the frame, Kanada smear, Obari triangular silhouette, impact frame, airflow/debris response.

Prompt rule:

```text
以真实动作作为身体力学基础，但不要停留在普通武器演示；加入1-2个清晰的幻想武器功能，并用夸张透视和短促峰值让功能可见。
```

## Hero Peak / Naked-Eye 3D Trigger

Use screen-breaking or naked-eye 3D language only at the strongest beat, not throughout the entire clip.

Good triggers:

- giant weapon tip, arrow, blade, chain, fist, foot, or debris rushes toward camera for 0.5-1.5 seconds;
- camera is ultra-wide/FPV, close foreground object is huge, body remains readable behind it;
- impact frame or release beat happens as the object almost breaks the screen plane.

Prompt block:

```text
在最强峰值加入裸眼3D破屏感：超广角近距离透视，武器/箭矢/能量轨迹从画面深处猛冲向镜头，前景巨大但主体轮廓保持清晰，短促impact frame后立刻回到完整动作。
```

Avoid:

```text
全程破屏、持续鱼眼变形、主体被特效挡住、只有粒子飞向镜头但动作本身没有峰值。
```

## Default Strategy For User's Workflow

When the user asks for help with an AI-video idea, respond like this:

1. Give 2-3 creative route options if the idea is broad.
2. Pick the strongest route if the user asks for execution.
3. Output a final 即梦 SD2 prompt by default when the target tool is unclear, because the user's current workflow uses it.
4. Keep a short "下一轮只调什么" note so iteration stays controlled.
