---
name: seedance-motion
description: "This skill should be used when the user asks for body action, choreography, physics, object movement, movement timing, action continuity, stunt direction, or motion-reference mapping in Seedance 2.0."
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

# seedance-motion

使用物理动词和后果。运动应当在画面上可观察、在镜头内有定时，并归属于某个主体或物体。宁可要一个带可见终点的强动作，也不要几个争夺注意力的含糊动作。

为视频运动参考加载 `[ref:reference-workflow]`，为跨镜头的动作交接加载 `[ref:shot-list-continuity]`，为安全的剪辑、延展和 R2V 范式加载 `[ref:examples-by-mode]`，当运动即表演时加载 `[ref:directing-engine]`：把场景的情绪翻译成每个节拍一个真实可见的手势——一个有目标和潜台词的可演动作——而不是一个模型无法渲染的情绪词。

## 意图

运动是用户故事的动词——是他们前来想看到"发生"的那件事。这里的灵魂是后果：开始、落地并改变了某物的运动让人感到真实可信；循环往复的运动让人感到是生成出来的。每个动作都把故事向前推进一个节拍，否则它就不属于这段镜头。

## 运动契约

陈述：施动者/物体、动作、力度级别、定时、物理后果、连续性要求，以及终点。

| 运动类型 | 强表述 | 弱表述 |
|---|---|---|
| 细微表演 | `Character A inhales, grips the cup tighter, then sets it down without looking away` | `she feels nervous` |
| 产品材质 | `condensation beads gather, merge, and slide down the bottle neck` | `the product looks refreshing` |
| 编排动作 | `Character B ducks under the swinging bag, pivots left, and stops in a guarded stance` | `fast action fight scene` |
| 物体物理 | `paper receipt lifts in the fan breeze, flips once, and lands face-up` | `papers move dynamically` |
| 环境运动 | `rain streaks diagonally across the backlight while puddle ripples spread from footsteps` | `stormy weather atmosphere` |

## 物理优先范式

官方材料宣称强大的物理表现；通过写出"因"并让模型计算"果"来提取它（现场观察到的侧重点——在承诺结果前先测试）。陈述质量、力和材质，然后点明一个相机能看见的后果：`the heavy oak door swings shut and the candle flames bend toward it` 胜过 `the door closes dramatically`。后果证明动作：重量体现在落地的压缩中，动量体现在过冲与回弹中，摩擦体现在打滑长度中，风体现在它所移动的东西中。一个物理起因带两三个可见后果，读起来比三个独立动作更有力。

## 定时范式

短镜头使用三节拍结构：铺垫、动作、改变后的末态。例如：`0-2s: candle flame steady; 2-4s: door opens and flame bends; 4-6s: smoke trail curls toward the hallway`。时间分段对动作、视效、对口型和产品演示很有用，但除非用户确实需要，否则避免逐帧精确的过载。

当声音驱动运动时，把每个可见变化与一个节拍或音效配对：`door click at 2s, light pulse on the downbeat, hand releases the cup on the final chime`。不要在一段短镜头内要求很多剪切、地点和微动作。

## 参考运动规则

对于参考素材，只使用自有、已授权、公有领域、库存、动作捕捉、排练或自录的素材。把 `[Video1]` 映射到运动、相机、定时或走位，而非身份，除非该身份已获授权。若参考素材含有真实人物，只迁移一般性的运动或相机行为，并明确排除肖像迁移。

## 稳定性规则

当动作过多时，手、面孔、徽标和产品几何形状会漂移。在脆弱细节周围减少运动：对口型时锁定相机，让手保持简单姿势，要求产品部件保持刚性，并移动光线或环境而非核心身份锚点。

## 序列状态

当存在序列状态时，继承已观察到的动作阶段、未完成的运动矢量、当前镜头范围、连续性锁定项、精确的引用标签，以及预留的未来节拍。不要重演被标记为"已发生"或"已完成"的动作。不要提前执行预留节拍；把被采用末态中未完成的运动带入下一段镜头。

## 输出契约

返回运动表述、定时范式、参考角色映射（若有），以及修复后的提示词语言。
