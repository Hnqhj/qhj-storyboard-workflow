---
name: seedance-fight-director
description: 为 Seedance 2.0/Higgsfield 生成、诊断、迭代高强度打斗、动作、武术、剑斗、追逐、超能力战斗、动漫战斗和动作分镜视频提示词。融合动作编舞、动作物理、A/B/C/D 起始态与终止态锚点、HEAVY/RUSH/CHASE 打点节奏、镜头总控集中风格与特殊节拍局部运镜、Liu 本地 `{{Image 1}}` / `{{Video 1}}` 参考格式、失败复盘和 Git/版本迭代方法。触发于打斗、格斗、动作戏、武打、动作分解、起始态、终止态、打点、运镜、连招、动作基底、打击感、Seedance fight、Higgsfield fight、anime fight、choreography、camera、prompt iteration。
---

# Seedance Fight Director

When this skill is used inside Liu's live-action short-drama workflow, follow `../director-workflow-70/references/short-drama-director-stack.md` and preserve the director brain's selected concept, group boundary, and continuity state. This skill owns fight-specific action, physics, rhythm, and camera-proof decisions inside the plan; it must not replace the human shot table, group-level prompt packaging, or selected platform compiler.

## ExecutionPlan Specialist Mode

When an upstream `ExecutionPlan` names a separate `platform_compiler`, act only
as the fight specialist. Do not emit a complete prompt, a second six-part block,
or alternate platform wording. Return one `TASK_CARD` containing only:

```text
objective
action_spine_patch
per_shot_contact_and_state_changes
rhythm_patch
camera_proof_patch
continuity_and_endpoint_patch
sound_foley_patch
state_patch_request
```

Patch the approved `ShotLedger` and `CameraGroupPlan` fields without changing
group boundaries, authoritative dialogue, asset handles, or story outcome. The
selected platform compiler consumes those accepted fields once. Use the direct
prompt output contract below only when this Skill is the explicitly requested
standalone output owner and no separate compiler is selected.

Liu audio override: fight prompts contain character dialogue plus dry, source-coupled foley only: footfalls, cloth strain, exertion breath, weapon movement, impacts, debris, body contact, and surface response. Do not add music, score, BGM, ambience beds, tension risers, emotional drones, wind chimes, suspense stingers, or mood-only effects. Reference-audio generation is skipped unless Liu explicitly approves a dry foley timing test.

## 核心定位

把“打一场很帅的架”升级成一个可复用的**打斗导演系统**：先确定动作基底与物理因果，再设计节奏峰值，再选择证明动作的运镜，最后编译成 Seedance 2.0 / Higgsfield 可粘贴提示词，并保留可迭代的版本记录。

融合顺序固定为：

```text
动作基底与物理可信度 -> 路线/攻防因果 -> 节奏与打击感 -> 运镜合同 -> Seedance 提示词 -> 复盘迭代
```

不要只堆“dynamic / cinematic / fast / powerful”。每个打斗节拍必须能回答：谁在迫使谁改变状态，力量从哪里来，镜头如何让观众看清，结尾状态如何变了。

## 按需参考路由

不要一上来加载所有资料。只在对应任务需要时读取：

- `references/imported-fight-action-systems.md`：当用户要高控制打斗、动作分解、起始态/终止态、HEAVY/RUSH/CHASE 打点、多素材角色/动作/场景绑定、动漫战斗、武侠剑斗、追逐闪避、超能力战斗或失败复盘时读取。上游资料中的 `@material[...]` 仅作内部角色分工概念，最终统一编译为 Liu 的 `{{Image N}}（...参考）` / `{{Video N}}（...参考）` 格式。
- `references/camera-geography-coverage-topology.md`：当用户要求多切镜、强运镜、特殊分镜，或成片出现长时间固定侧拍、切了却像没切、焦段变化但观感相同、摄影机追不上动作时读取。它负责区分地理不变量与摄影覆盖拓扑，并建立摄影相位图。
- 当多轮交锋必须继承伤势、体力、装备、地形或主动权变化时，先接收 `$action-choreography-reference` 的“打击等级 + 战斗状态变化 + 反击来源”压缩结果；只把可见因果和持续状态编译进提示词，不把分析标签或无依据的毫秒表写进成稿。
- 当近身对招、高密度短打或兵器绑定显得回合制、全程同速或只剩模糊乱挥时，接收 `$action-rhythm-editing` 的近身节奏短语；把“接触集群—节奏标点—状态后果”转译成自然动作，不把每秒击数、固定招数或内部节奏标签写进成稿。

## 一轮必须产出什么

除非用户只要短答，否则一次使用本 skill 必须输出：

1. **导演判断**：战斗类型、动作基底、时长、T2V/I2V/V2V、主要风险。
2. **动作物理**：支撑、重心路线、距离/角度、控制点、接触或擦身、反应成本、收势。
3. **节奏表**：起势、爆发、峰值、受击/环境反应、拖尾、刹车、恢复。
4. **镜头合同**：把景别、角度、焦段感、畸变、相机支撑、运动能量、构图/剪辑节奏和揭示逻辑集中到镜头总控；仅特殊节拍补局部运镜。
5. **可复制 Seedance Prompt**：按镜头/时间分段，包含精确素材句柄、全片镜头总控、动作事件节拍、声音与正向稳定约束。
6. **迭代记录**：如果是基于已生成视频修改，写明失败原因、保留点、下一版测试目标。

## 参考图与素材强制规则

当用户提供任何图片、参考图、角色图、场景图、风格图、动作图、分镜图或产品图：

1. 最终 Seedance/Higgsfield 提示词必须显式使用 Liu 的精确素材句柄：`{{Image N}}`、`{{Video N}}`、`{{Audio N}}`。
2. 素材第一次出现时必须紧跟中文括号标注用途，例如 `{{Image 1}}（角色身份、外观、服装与武器参考）`、`{{Video 1}}（动作、节奏与运镜参考）`。
3. 在 `角色/资产锁定` 正文中把素材绑定到具体控制对象；`参考图1`、`图1`、裸写 `image1` 与 `@material[...]` 均不作为最终交付格式。
4. 多素材必须分别分配角色、场景、风格、动作、构图、材质或光影职责，保持编号与真实上传顺序一致。
5. 素材用途能从用户指令和画面明确判断时直接绑定；用途会实质改变结果且无法可靠判断时再简短确认。
6. 参考视频必须限定迁移范围：镜头节奏、动作节奏、走位、风格、材质或氛围；身份只有在用户明确指定时才由视频控制。
7. Liu默认不生成参考音频，且不自动运行音乐/节奏音频流程。只有用户明确批准“干拟声节奏测试”时，才运行 `$seedance-audio` Reference Audio Gate；该参考文件只能包含人物台词和物理拟声音效，不得包含音乐、配乐、氛围铺底或情绪化音效。本 Skill 只把已批准的干拟声结果编译进打斗提示词；普通打斗直接输出人物台词与纯拟声音效计划。

模板：

```text
【角色/资产锁定】
{{Image 1}}（角色A身份、外观、服装与武器参考）：锁定角色A。
{{Image 2}}（角色B身份、外观、服装与武器参考）：锁定角色B。
{{Image 3}}（场景空间、地面材质与光线参考）：锁定战斗空间。
{{Video 1}}（动作、重心、节奏与运镜参考）：迁移动作与镜头证据。
```

## 文章式迭代方法：把经验“烘焙”进 skill

当用户说“按某篇文章/某个案例迭代 skill”“做 v2/v9/v15”“保留 secret sauce”“同步 Git”时，按以下流程：

1. **定义本次 skill 的职责**：这一版专门解决什么？例如动漫打斗、真实武术、重武器、追逐、群战、运镜混乱、打击感弱。
2. **收集可迁移机制**：不要只复制一个 prompt。提炼动作机制、节奏结构、镜头合同、失败类型、正向稳定锁与素材引用方式。
3. **小版本试验**：每版只强化 1–2 个变量：动作路线、武器重量、镜头总控、特殊节拍运镜、节奏峰值、正向稳定约束之一。
4. **分支保留**：高表现版本不要覆盖；用 Git branch 或清晰版本名保存。实验版从好版本分支出去。
5. **复盘回写**：测试视频后记录：成功点、失败点、下版锁定项、下版放松项。把稳定规律写回 skill，把单次偶然效果写进案例库而不是硬编码。
6. **不要把最好版本稀释掉**：高成功率短语和结构可以保留为“强制门”；风格装饰词不要长期堆积。

## 输入不足时的默认假设

默认：Seedance 2.0/Higgsfield、15 秒、16:9、无对白、动作优先、中文说明 + 可粘贴英文 prompt。用户明显面向中文平台时，用中文 prompt。

只在以下情况提问：

- 用户提供了图但用途不明。
- 角色/武器/场景完全缺失且会改变动作基底。
- 用户要求连续多条片段但没有说明上一条末态。

否则直接合理假设并产出。

## 动作基底：先选运动系统，再写连招

不要从“帅气连招列表”开始。先为每个角色选一个动作基底：

| 目标感觉 | 推荐动作基底 | 画面特征 |
|---|---|---|
| 近身压迫 | Boxing / Wing Chun / Muay Thai | 中线压力、短距离、肩胯发力、格挡反击 |
| 干净剑斗 | HEMA / Kenjutsu / Fencing | 剑线、距离、试探、绑定、反弹、步伐 |
| 动漫爆发 | Wushu + anime spacing | 大姿态、预备压缩、短爆发、smear、hit-stop |
| 重武器 | Axe/Hammer/Greatsword dynamics | 慢起势、重心拖拽、长刹车、环境破坏 |
| 追逐/跑酷 | Parkour / stunt chase | 路线、障碍、落地吸收、镜头跟拍 |
| 群战 | Stunt feed-and-answer | 清晰路线、一个主威胁、其他人只制造压力 |
| 超能力 | power-as-movement-tool | 能力改变视线/路线/平衡，不替代接触因果 |

动作基底必须转成可见机制：站姿高度、攻击平面、距离、支撑脚、武器功能、重心路线、收势方式。

## 反“假打”门

每个攻防交换都必须通过：

```text
入距：攻击者如何进入有效距离？
控制点：控制的是手、刀线、重心、角度、视线还是环境？
防守答案：对方是格挡、闪避、被顶开、失衡、滑步、跌撞还是反打？
接触证明：命中、格挡、擦身、绑定、近失误是否可见？
力量路径：力量来自脚、胯、肩、坠落、武器惯性、地面反作用或能力源？
代价：攻击者/防守者付出了什么步伐、后坐、滑移、转体、刹车、落地或恢复？
下一招来源：上一状态如何自然生成下一动作？
状态变化：距离、角度、平衡、武器线、路线、高低位或主动权必须改变。
```

如果只写“攻击、闪避、反击、连招”，它就是假打。改成动作因果句：

```text
A 从左侧切入，刀背压住 B 的武器线，B 的肩线被带偏并后滑半步；A 顺着这股偏转绕到内侧，第二击从低位斜上挑出，把 B 逼到断柱旁。
```

## 路线优先：先让压力移动

短片打斗最容易变成原地回合制。先锁一条路线，再变化拓扑。

路线问题：

```text
压力从画面哪边推向哪边？
谁在推动路线？谁被迫后退/转向/降低/升高？
什么事件导致反转？
最终两人的距离、角度、武器线、平衡在哪里？
```

至少变化三类拓扑：

- 高低位：低扫 / 中线顶压 / 高位下劈
- 攻击平面：水平、斜线、垂直、上挑、坠落、突刺、碾压
- 距离：长距离威胁、近身挤压、绑定、脱离追逐
- 支撑状态：站立、低伏、滑步、跪地、腾空、墙面/地面辅助
- 武器功能：刃、背、柄、护手、尖端、平面、拖拽质量、落地刹车
- 环境证明：地面划痕、尘土爆开、水面切开、柱体碎裂、墙面接触

## 起势、爆发、收势：节奏编辑

强动作不是全程快，而是速度曲线清晰：

```text
可读预备/压缩 -> 极短爆发 -> 接触/擦身/转向 -> 延迟拖尾 -> 刹车/恢复成下一状态
```

质量感时间规则：

| 类型 | 时间感 |
|---|---|
| 轻快短兵/拳脚 | 短预备、极快峰值、短恢复 |
| 中等武器 | 明确预备、快峰值、中等收势 |
| 头重/巨剑/锤斧 | 长预备、承诺式加速、明显拖尾、长刹车 |
| 柔性武器 | 手柄先动、末端后到、张力波最后收束 |
| 超人速度 | 可压缩启动，但必须有接地、滑步、墙触、落地或环境反应证明 |

15 秒默认节奏：

```text
0–1s：主动开场；不要默认静态对峙。可从近失误、落地、刚被打退、追击中开始。
1–4s：第一条压力路线，证明距离和动作基底。
4–8s：对方付出代价并尝试反转，加入高度/平面/距离变化。
8–11s：升级；环境参与或武器功能变化。
11–14s：最强峰值；短 hit-stop 或慢动作只给决定性一击。
14–15s：后果和收势；尘土、喘息、武器线、站位成为下一段首帧。
```

8 秒默认节奏：

```text
0–1s：动作中开场。
1–3s：第一接触和位移。
3–5s：反转或路线改变。
5–7s：决定性峰值。
7–8s：清楚结尾状态。
```

## 持续交战闭环（高强度打斗强制门）

当用户要求高速对打、ACT、连招、压制战或近身武器战时，默认在“正向稳定约束”中加入一段紧凑的持续交战锁：

- 双方维持高攻击频率与有效交战距离，动作链持续围绕攻击、接招、闪避、反击和重新夺取中线推进。
- 每次位移必须改变攻击角度、距离、站位、高度或优势关系；跑动本身不作为动作内容。
- 接触可以有极短 hit-stop、武器压缩、身体受力或摄影机震动，但接触后立即进入反弹、滑退、追击或反击，不进入长停顿和站桩摆姿。
- 摄影机必须追上压力路线，让双方持续留在同一可读战斗空间；低机位贴地追拍、短促甩镜和快速切镜由攻击、受击或遮挡触发。
- 反馈按力量等级分配：轻接触用武器振动、衣料抽动和脚步修正；中等命中用受击位移、尘土或空气压缩；重击才使用音爆、碎石爆散、地裂或大范围气流冲击。避免每次碰撞机械重复整套特效。

一致性门：事件节拍不得同时要求长距离追逐、反复冲出交战区、连续撞击多个远处建筑、扩大到新场地或提前对峙定格。上游事件如果主动让双方分开，“持续交战”稳定锁无法补救；先把动作改写为同一战斗半径内的角度变化、短位移和连续反击。

内部检查：暂停任意连续三次交锋，每次都应看见“有效进攻关系 → 接触或明确闪避 → 一方被迫改变状态 → 下一动作从该结果自然发动”。最终提示词只写自然可见的因果，不暴露诊断公式。

### 重点命中的受击确认门

高速打斗不能把“身体产生形变”当成完整受击。每段先指定一至三次承担叙事或节奏峰值的重点命中；这些命中必须同时编译出：

- 接触点的局部压缩、偏转及其向头肩、脊柱、髋部、护手和脚底传播的结构反应；
- 当脸部可见时，与受力方向和强度一致的微表情、生理反应和注意力中断，例如眼睑收紧、眉间压缩、下颌偏转、视线短暂脱锁、骤然吐气、护手延迟回收，随后恢复下一动作意图；
- 与画面同步的肉体/衣料接触声、呼气或压抑痛哼、脚底刮擦、地面或空间回响。

重点命中的摄影证明按“接触局部 → 极短受击表演 → 位移结果”交接，不能只停在攻击者的英雄姿态。普通擦碰只给简化反馈，避免每次接触都大幅表演、长 hit-stop 或重复整套音效。若重击后人物表情完全不变、没有呼吸或声音确认，即使身体发生夸张形变，也按“橡胶形变式假打”处理。

## 非对称尺度与非人运动门

当一方明显大于另一方，或其身体结构已经怪物化：

- 不要用“双方全程完整同框”证明连续性。把较小角色作为持续摄影锚点，允许巨物被画框裁切，以手、前臂、头颈、胸腹或足部局部压入镜头；只安排一次短促全貌镜头证明尺度。
- 尺度锁必须使用角色相对值和局部可见关系，例如“展开高度约为女主2.5倍、前臂长于女主全身、腹部横跨街道”，而不是只写绝对身高。
- “非人”必须转化为运动拓扑：支撑点数量与交替顺序、腹部高度、脊柱驱动方式、肩带转向、颈部独立运动、重心路径和制动方式。仅写长肢、反关节或诡异会被模型还原成人形格斗。
- 避免把人形武术词平均分配给怪物。怪物用其结构发动捕食、压制、包围和承重转换；人类角色再用步法、武器与支点回应。
- 镜头覆盖应按功能分配：接触局部、运动机制、受害者/对手视角、一次尺度全貌、结果反击。若事件节拍没有为这些镜头分工，模型容易回退到连续平视双人全身镜头。

## 运镜融合：相机负责证明动作

每个镜头或节拍只保留一个主意图，但 15 秒动作段默认由多个因果相连的镜头阶段组成，或由一条持续运镜中的多个明确相机相位组成。身份稳定不等于固定镜头。把完整镜头风格集中写进 `镜头语言总控`：兼容的导演/摄影师/影片/工作室/作品锚点，以及透视、镜头家族、畸变、运动能量、构图/剪辑节奏和揭示逻辑，例如 `扳机社动画美学 + 极端透视与高能构图；金田透视法 + 近大远小的夸张纵深；FPV超广角 + 贴近动作路线的高速穿行；强桶形畸变 + 边缘外弯的速度压力`。`事件节拍`默认继承，不重复风格名；当镜头变化本身是用户目标或已验证风险时，事件节拍必须用简短摄影相位写清机位、路径、跟随对象、动作触发和证明任务。

地理连续与摄影变化分层控制：动作轴、朝向、推进方向和场景参照物属于地理不变量；机位方位、高度、距离、运动路径、跟随对象和证明任务属于覆盖拓扑。动作轴同侧是允许摄影机移动的半空间，不是固定侧面机位。相邻主要相位若重复机位方位、高度、景别、运动路径和证明任务中的多数，即使改焦段或发生切镜，观感仍等同于同一镜头；此时至少改变两项可见摄影属性。

再单独控制画面坐标系：稳定空间不代表摄影机上方向必须锁定世界重力。高张力动作可让 camera up 跟随刀线、身体冲势或受力弧线，以动作触发 roll / pitch / yaw，令地平线、建筑线、人物轴和武器线形成非正交构图。非正交不是随机荷兰角；倾斜必须继承动作向量、眼线和轴线，并在冲击、遮挡、翻转或受力变化时改变。

运镜选择：

| 动作需求 | 推荐镜头 | 作用 |
|---|---|---|
| 证明两人距离/脚步 | 宽/中远景，侧向或三分之二角度，轻跟拍 | 看清路线和接触关系 |
| 追逐/推进压力 | 横向 tracking / steadicam follow | 让观众跟着压力移动 |
| 决定性命中 | 短 push-in / insert / brief locked impact frame | 放大峰值，不隐藏因果 |
| 重武器 | 低角度中景，轻微后撤或侧跟 | 显示拖尾、重心和刹车 |
| 群战 | 宽镜头建立路线 + 少量插入 | 防止人物融合和空间混乱 |
| I2V 保角色 | 受控推近、侧跟或短弧绕，主体持续清晰 | 在身份稳定前提下建立真实镜头运动 |

提示词中的镜头句式：

```text
《浪客剑心》风格 + 35mm低机位侧跟让双方脚步、刀线与接触面持续清晰；A向右推进时触发镜头跟随A的压力路线横移，命中后镜头交接给B的滑退轨迹，最终停在B抵住断柱的低角度三分之二构图。
```

每个镜头保持一个主运动；需要改变运镜时，用动作、冲击、遮挡、前景掠过或受力者位移触发切换，并把新镜头的跟随对象与证明任务写清楚。接触瞬间可以短暂锁镜，锁镜之后立即由受力者位移、武器拖尾或环境后果重新带动相机。

摄影复杂度与动作复杂度共享生成预算。每个摄影相位默认只承载“一个动作状态变化 + 一个摄影证明任务”。当角色身份、怪物结构、微动作、环境破坏与摄影变化同时过密时，优先减少微动作数量或拆分素材，不要让模型用固定主镜换取动作完成度。

## 声音和打击感

声音要和物理同步，不要当装饰：

- 预备：吸气、脚掌摩擦、衣料绷紧、武器拖地。
- 爆发：短 whoosh，不要覆盖接触点。
- 接触：钝击、金属叮当、木裂、沙尘爆、火花。
- 反应：与受力同步的短促吐气、压抑痛哼、喘息中断、滑步、撞墙、碎石落地；重点命中要让人物声音、接触声和脚底位移声组成同一个因果事件。
- 收势：风声、尘土、武器余震、观众或环境延迟反应。

对重击使用短 hit-stop，随后立即给受击者/环境反应。不要把 slow motion 拉满整段。

## Seedance Prompt 编译模板

按用户需求输出中文或英文。Liu 的最终可粘贴提示词使用六段正向结构，并在正文中绑定精确素材句柄：

```text
【角色/资产锁定】
{{Image 1}}（角色身份、外观、服装与武器参考）：...
{{Video 1}}（动作、节奏与运镜参考）：...  # 仅在真实提供时出现

【视觉材质总控】
...

【镜头语言总控】
[完整全片镜头风格：名词美学锚点 + 透视 + 镜头家族 + 畸变 + 运动能量 + 构图/剪辑节奏 + 揭示逻辑]。

【事件节拍】
开场：第一帧就是[距离、姿态、武器线与压力关系]。
推进：[动作路线、攻防响应与状态变化]。
转折：[距离、支撑、高度或主动权发生变化]。
峰值：[决定性动作、清晰接触证据与直接后果]；若此拍需要特殊运镜，补写“[冲击/遮挡]触发[特殊运镜]，形成[可见结果]”。
收势：[制动、余波与最终距离、姿态、武器和环境状态]。

【声音】
...

【正向稳定约束】
...
```

素材句柄硬规则：首提必须写成 `{{Image N}}（...参考）`、`{{Video N}}（...参考）` 或 `{{Audio N}}（...参考）`。`参考图1`、`图1`、裸写 `image1`、`@Image1` 与 `@material[...]` 均不进入 Liu 的最终可粘贴提示词。用户上传五视图角色后，模型面对的每个角色称谓统一使用精确平台句柄 `@角色名`，例如 `@苏凌月`、`@刘大龙`；该句柄与 `{{Image N}}` 文件句柄职责不同。镜头风格必须完整集中在 `镜头语言总控`；事件节拍默认继承。若普通节拍重复总控风格，或特殊镜头节拍没有写清触发原因与可见结果，停止交付并重写。

## 内部失败诊断与正向改写库

下列负向短语只用于后台识别失败类型，禁止直接复制进 Liu 的最终提示词。交付前把它们转换为当前可见的正向动作、镜头、身份与材质锁。

通用动作：

```text
no idle posing, no turn-based fighting, no teleporting without visible motion path, no hits without body reaction, no attacks that miss the visible range, no reset to neutral between exchanges, no weightless floating, no foot sliding, no merged bodies, no extra limbs, no warped faces, no weapon changing shape, no unreadable overlapping silhouettes
```

动漫/2D：

```text
no smooth plastic 3D render, no glossy video-game cutscene look, no uniform interpolation, no lifeless locked poses, no screen-filling FX that hides contact, no long whiteout frames
```

参考图连续性：

```text
{{Image 1}}（角色A身份、服装与武器参考）锁定角色A；{{Image 2}}（角色B身份、服装与武器参考）锁定角色B；双方轮廓、武器与色彩关系持续清晰。
```

运镜：

```text
no chaotic camera, no competing drone/orbit/dolly/zoom stack, no close-up that hides feet during contact, no shaky blur covering the decisive hit
```

## 失败复盘与下一版修法

| 失败 | 优先修法 |
|---|---|
| 看不清谁打谁 | 拉开角色差异；用中远景证明距离；减少同时动作 |
| 像跳舞不打人 | 加入控制点、接触证明、受击/格挡反应 |
| 动作软 | 加预备压缩、短爆发、受击者位移、拖尾和刹车 |
| 原地回合制 | 先设计压力路线和反转来源，再写招式 |
| 武器轻 | 明确质量分布、重心拖拽、接地刹车、 regrip/catch step |
| 运镜乱 | 每镜一个主运动；跨节拍用动作/冲击/遮挡触发切换，并写清新镜头跟随对象 |
| 特效糊住动作 | 把 VFX 设为接触证据，不设为主角 |
| 角色漂移 | 强化 `{{Image N}}（角色身份与外观参考）` 锁；让复杂运镜保持清楚主体轮廓和可读接触面 |
| 15 秒撑不住 | 改 7–10 秒验证片段，先证明一条完整动作因果 |

## Git / 版本管理建议

当用户让你“把这个版本保存”“同步 Git”“做 v2/v3 分支”时：

1. 先说明本次改动范围。
2. 更新本 skill 或相关参考文件。
3. 运行基础校验。
4. 提交到 skills 备份仓库；重要版本用清晰 commit message，例如 `Iterate Seedance fight director workflow`。
5. 如果是高风险试验，先建分支，不要覆盖稳定 main。

## 最终自检

输出前检查：

- [ ] 是否有动作基底，而不只是“帅气打斗”？
- [ ] 是否有一条压力路线和至少一个状态变化？
- [ ] 每次接触是否有对方或环境反应？
- [ ] 速度是否有起势、爆发、峰值、拖尾、刹车？
- [ ] `镜头语言总控`是否完整写出全片镜头风格，普通事件节拍是否避免重复，只有特殊镜头节拍补写触发原因与可见结果？
- [ ] 所有已提供素材是否用 `{{Image N}}（...参考）` / `{{Video N}}（...参考）` / `{{Audio N}}（...参考）` 在正文中精确绑定？
- [ ] 最终六段提示词是否保持正向描述，并把稳定要求写进 `正向稳定约束`？
- [ ] 是否给出下一版可测试目标？

## Verified Fight Prompt Pattern: Environmental-Feedback Duel
Use this pattern when a fight needs to become readable and physically convincing.
Core mechanism: role asymmetry + one pressure route + one environmental feedback medium + one camera grammar + one consequence beat.
Do not over-specify every technique. Let the model solve micro-motion while locking intention and state changes.
Compile the final prompt into Liu's six sections: 角色/资产锁定 / 视觉材质总控 / 镜头语言总控 / 事件节拍 / 声音 / 正向稳定约束.
Required checks:
- One fighter has a clear pressure role; the other has a clear response/counter role.
- The environment proves movement and impact: water, mud, snow, sand, ash, dust, gravel, rain, hanging cloth, debris, etc.
- Each timeline beat changes distance, pressure, posture, weapon line, or consequence.
- `镜头语言总控` owns the complete camera identity: named aesthetic anchors, perspective, lens family, distortion, movement energy, framing/edit rhythm, and reveal logic. Event beats inherit it; only a genuine special-camera beat adds a local trigger and visible result.
- The finishing blow can be implied by posture, silence, object drop, collapse, or environment response; it does not need visible gore.
- Positive stability locks remain compact: identity stays anchored, combat contact stays readable, anatomy and weapon geometry stay coherent, and effects remain localized around the contact proof.
Do not copy rain/samurai/waterfield into unrelated scenes; transfer the mechanism only.

## Finisher Priority Rule: Impact Before Ritual Geometry
For cinematic finishing moves, the first readable event must be physical or spatial impact: approach vector, contact point, receiver deformation/displacement, environment reaction, and follow-through. Do not let magic circles, top-down geometry, or ritual diagrams appear before impact. Early circular geometry can turn long monsters into rings and make the hero stand still at the center. Treat seals/rituals as consequence layers after the hit, or split sealing into a separate clip.

## High-Density Multi-Cut Environment Fight Gate

For dense two-person action with many cuts and a prop-rich location, read `references/high-density-environment-fight-pattern.md` before compiling the prompt.

Minimum gate:

```text
visual contract
+ geography contract
+ prop affordance chain
+ one-function-per-shot map
+ setup/payoff micro-inserts
+ cumulative environment state
+ sound bridge
```

Keep left/right and the action axis stable when they are the cheapest way to preserve readable geography; allow only motivated axis resets. Vary coverage by function rather than forcing every shot to change every camera parameter. Treat environmental objects as causal action tools, not decorative inventory. Use very short inserts only when they prepare, redirect, measure, or pay off a later action. If the requested cut density exceeds reliable single-generation control, plan best-of-many selection or split the sequence into edit-friendly clips instead of pretending one prompt guarantees all cuts.
