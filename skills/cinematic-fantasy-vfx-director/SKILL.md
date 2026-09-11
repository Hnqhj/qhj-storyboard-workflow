---
name: cinematic-fantasy-vfx-director
description: "Direct film/TV-grade fantasy VFX for live-action short dramas: xianxia, ancient Chinese fantasy, cultivation, talismans, formations, energy attacks, weapon auras, teleportation, destruction, weather and supernatural environments. Use when VFX must feel premium, cinematic, physically integrated, high-end CG/composite rather than cheap glow, random particles, flat overlays, or generic AI effects."
---

# 影视级玄幻特效导演

把玄幻特效设计成可拍、可合成、可生成的因果系统。目标是让观众同时看懂力量来源、运动路径、接触关系、人物受力和环境响应，再用电影级光学、材质和合成完成高级感。

## 设计顺序

1. **特效任务**：一句话说明特效要证明什么：攻击方向、能力归属、空间变化、威胁规模、封印/召唤、状态转变或环境破坏。
2. **来源与媒介**：锁定力量从人物、兵器、法阵、符箓、地面、天气或空间裂隙的哪个位置产生；说明载体材质与形态。
3. **运动生命周期**：预兆/聚集 → 形成 → 沿路径传播 → 接触/碰撞 → 受体与环境反应 → 峰值 → 衰减/残留。
4. **合成关系**：写清遮挡、景深、反射、阴影、局部曝光、体积光、烟尘和镜头运动如何共同受影响。
5. **质量分级**：每个镜头只设一个主特效峰值；次级粒子、拖尾、火花和尘雾为证据，不得喧宾夺主。

## 影视级质量标准

- 先保证人物、兵器、接触点和空间轴线清楚，再添加光效。
- 发光体必须照亮附近衣料、皮肤、金属、石墙、地面或雾气，且随距离、角度和遮挡衰减。
- 粒子、烟尘、碎片必须有来源、受力方向、寿命和落点；禁止凭空生成、均匀喷洒或全画面闪烁。
- 破坏按材质区别：石材粉尘与块状碎片、木材纤维、金属弯折与火花、玻璃断裂、布料撕裂不可混用。
- 镜头冲击、光闪、运动模糊、景深变化和速度变化只在接触峰值短暂出现，并立即恢复可读性。
- 特效峰值后必须有衰减和稳定残留：裂纹、余光、落尘、残火、符文暗灭、能量回流或空间闭合。
- 禁止“金光一闪”“高级粒子”“大片感”等无法执行的空泛词作为主要设计。

## 玄幻类型语法

- **法阵/封印**：阵基与符文先定位，能量沿阵线运行，封锁或转移目标，受阻处出现反馈，最后留下熄灭或残留纹路。
- **剑气/兵器能量**：力量从握持和刃口产生，沿挥击方向形成可读轨迹，接触点产生切割/压迫，目标和地面留下方向一致的结果。
- **掌力/冲击波**：身体重心和手掌先完成发力，空气压缩或尘雾前缘可见，命中后目标位移、衣料拉扯、墙面受力和碎屑延迟出现。
- **雷火/元素**：先有环境征兆和能量来源，再有主路径与分叉；电光、火焰、烟尘和反射共享同一光照逻辑。
- **空间/传送**：边界先扭曲或折叠，人物局部逐步穿越，遮挡和景深保持连续，落点有空气、尘埃、衣摆和地面反馈。

## 镜头与提示词接口

把设计编入现有六段提示词：视觉材质总控写媒介和光学，镜头语言总控写特效与摄影机耦合，事件节拍写来源/路径/接触/反应/衰减，声音只写人物台词和有物理来源的拟声。不要额外创建泛化的“特效段落”。

交付前输出内部卡：

`任务 → 来源 → 形态/材质 → 路径 → 接触 → 受体/环境反应 → 峰值 → 衰减 → 合成约束`

需要具体词汇时，交给 `$cinematic-vfx-director`、`$vfx-effect-construction-engine` 和 `$seedance-vfx` 编译；本技能负责影视级质量和因果审查，不替代动作编舞或镜头轴线设计。

需要寻找或评估玄幻特效参考图时，读取 `references/xianxia-vfx-reference-board.md`，按全景尺度、接触受力和材质衰减三类证据选图。

## 参考入口

- Sony Pictures Imageworks: https://www.imageworks.com/
- Framestore VFX: https://www.framestore.com/work
- Industrial Light & Magic: https://www.ilm.com/work/
- Weta FX: https://www.wetafx.co.nz/films/
- Houdini Gallery: https://www.sidefx.com/gallery/
- Unreal Engine Niagara: https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-overview
