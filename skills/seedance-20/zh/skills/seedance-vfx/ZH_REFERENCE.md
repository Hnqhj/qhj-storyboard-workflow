---
name: seedance-vfx
description: "This skill should be used when the user asks for VFX, particles, energy, destruction, transformation, weather effects, magical effects, explosions, smoke, fire, water, or physically plausible effects in Seedance 2.0."
license: MIT
metadata:
  version: "6.1.0"
  updated: "2026-06-22"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-vfx

视效提示词需要材质行为、来源、定时和后果。把每个效果都当作物理的：它从某处开始，与光线和物体相互作用，随时间变化，并以一个可见的状态结束。避免诸如魔法的、爆炸性的或电影感的之类的泛泛词，除非它们被翻译成粒子、流体、烟雾、光线、碎屑、形变或能量行为。

## 意图

用户想要的是惊奇，而惊奇在它不再服从物理的那一刻就死了。本技能的目的是用因果的预算造魔法：每个效果都有一个来源、一段旅程和一个结尾，使那不可能之物读起来像被目睹的，而非被渲染的。

## 效果契约

陈述：效果来源、材质、运动路径、与光线的相互作用、与物体的相互作用、消散，以及终点。

| 效果 | 可直接用于提示词的短语 | 稳定性说明 |
|---|---|---|
| 产品粒子 | `gold dust particles spiral from behind the logo, catch the backlight, then settle on the table` | 让徽标和瓶子保持刚性。 |
| 能量 | `thin blue electrical arcs crawl along the cable, briefly illuminating fingerprints on the plug` | 让弧光附着在来源上。 |
| 烟雾 | `cold white vapor rolls over the rim, sinks down the glass, and thins near the tabletop` | 描述密度和方向。 |
| 变换 | `paper edge chars inward from the corner, flakes curl and fall, final logo remains untouched` | 保护身份锚点。 |
| 天气 | `wind pushes rain diagonally across the frame, puddles ripple outward from each step` | 把天气与表面绑定。 |

## 视效整合规则

每段镜头使用一个核心效果。把来源锚定到一个清晰的物体或身体部位。让效果遵从重力、风、碰撞、反射和遮挡。对于面孔、手、徽标或文字附近的视效，让核心身份保持稳定，并把效果放在其周围而非穿过它。

## 定时与消散

效果需要一个终点：沉降、淡出、蒸发、冻结、坍塌、辉光熄灭，或留下残留。若效果复杂，使用三步定时短语：`forms -> travels -> dissipates`。避免没有后果的永久效果，因为它们常常变成嘈杂的叠加层。

## 输出契约

返回视效契约、稳定性约束，以及一句紧凑的、可直接用于提示词的短语。
