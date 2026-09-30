---
name: cg-xianxia-vfx-design
description: "高级 CG 与仙侠玄幻特效系统设计：能量材质、剑气、符箓、法阵、元素之力、空间扭曲、召唤构造、环境破坏、镜头尺度、光照整合与电影级渲染。触发：炫酷但高级的 CG 玄幻特效，拒绝廉价粒子、单一发光、扁平贴图与无物理反馈。 Design premium CG and xianxia fantasy effect systems for film, TV, games, and AI video: energy materials, sword qi, talismans, formations, elemental forces, spatial distortions, summoned constructs, environmental destruction, camera scale, lighting integration, and cinematic rendering. Use when the user wants炫酷但高级的CG玄幻特效，拒绝廉价粒子、单一发光、扁平贴图和无物理反馈。"
disable-model-invocation: true
---

# CG仙侠特效设计

构建具有世界规则、材质逻辑和空间尺度的 CG 玄幻特效。每个特效都必须有“谁在驱动、以什么材质存在、如何运动、改变什么、如何结束”的答案。

## 特效系统五要素

1. **能量身份**：颜色、明度、纹理、符号和运动方式服务于人物/门派/法器身份；颜色不是唯一识别手段。
2. **材质表现**：区分等离子、火焰、电弧、液态灵气、晶体、金属、纸符、烟尘和空间折射；为每种材质指定边缘、体积、透明度、反射和衰减。
3. **空间层级**：前景遮挡、中景主体、背景环境和体积雾中分别放置特效，保持景深、遮挡和尺度参照。
4. **动力曲线**：预备/压缩 → 爆发/传播 → 接触/反馈 → 余势/回收；速度必须有对比，不能全程同速发光。
5. **世界响应**：衣摆、发丝、尘土、水面、树叶、墙体、阴影和反射对能量做出方向一致的反馈。

## 高级 CG 画面规则

- 一个镜头只设置一个主视觉焦点和一个主特效族，最多搭配一个辅助族。
- 主形态先以轮廓、明暗和路径读清，再增加纹理、细粒子和装饰符文。
- 能量越亮，周围曝光和反射越受控；保留黑位、皮肤细节、服装纹理和空间层次。
- 拖尾必须绑定速度、方向、遮挡和源头，源头停止后拖尾按惯性衰减，不悬浮残留。
- 法阵、符箓和纹样遵循统一几何语法；符文只在执行束缚、分流、净化、召唤、交换或封锁时出现。
- 巨大能量必须提供尺度参照：人物、建筑、地面裂纹、尘雾层和远景受光共同证明规模。
- 高级感来自因果、材质、光照、合成和节奏，不来自堆叠更多颜色、粒子和镜头抖动。

## 仙侠特效模块

- **灵气/能量流**：从丹田、掌心、剑脊、阵眼或天地节点产生；沿明确路径形成丝、带、环、刃或体积流；触碰目标后留下温度、压力、裂纹或光痕。
- **飞剑/剑阵**：先建立剑体与阵列关系，再展示加速、转向、锁定和回收；剑影数量有限且保持真实间距与遮挡。
- **符箓/法印**：纸张、墨线、火痕或金属刻纹有真实材质；激活时出现折叠、燃烧、展开或投影过程，不瞬间贴屏。
- **雷劫/天象**：云层、空气电离、地面反光和人物轮廓先建立，再让主雷束命中；雷电分叉服从空间结构，避免随机树枝状贴图。
- **空间裂隙/传送**：边缘折射、背景视差、粒子吸入和落点回弹共同证明空间变化；不要只用黑色裂缝或旋转圆环。

## 交付结构

```text
CG特效任务：
能量身份与材质：
来源/激活：
形态与主路径：
空间层级与尺度参照：
接触/操作与受体反应：
灯光、反射、阴影、体积雾：
峰值与衰减：
镜头耦合与连续性：
```

把最终内容交给 `$cinematic-fantasy-vfx-director` 做影视级审查，再由 `$vfx-effect-construction-engine` 和 `$seedance-vfx` 编译为平台提示词。

交付前读取 `references/cg-quality-gate.md`，淘汰扁平发光、无环境交互、无衰减、无空间层级和同质粒子堆叠。

## 参考入口

- SideFX Houdini Gallery: https://www.sidefx.com/gallery/
- Unreal Niagara Documentation: https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-overview
- Blender Open Movies: https://studio.blender.org/films/
- ArtStation Fantasy VFX search: https://www.artstation.com/search?sort_by=relevance&query=fantasy%20vfx
- The Rookies VFX gallery: https://www.therookies.co/contests/
