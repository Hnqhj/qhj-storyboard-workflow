# AI Prompt Packaging

Use this to turn shot design into final AI image/video prompt language.

## Image Prompt Package

For a still image:

```text
画面目标：[one sentence]
主体：[who/what]
张力机制：[composition / angle / lens / effect]
构图：[specific frame]
光影：[specific lighting]
材质/环境：[only details that matter]

最终提示词：
[subject], [action or pose], [environment], [composition tension], [camera angle/lens], [lighting], [effect], [style/material], clean readable frame, one visual focus

负面限制：
杂乱构图，主体不清，元素堆砌，随机文字，过度特效，廉价赛博，过多眩光，动作不可读，手指畸形，脸部崩坏，水印，logo。
```

## Image-to-Video Package

For video from an input image, do not re-describe every static detail. Focus on movement:

```text
请基于原图生成[时长]视频，保持原图角色身份、服装、构图、光影和场景一致。镜头采用[one camera movement]，主体只做一个主要动作：[action]。环境只有一个辅助动态：[secondary motion]。动作从[起点]到[落点]，节奏[slow / sudden / controlled]，最终停在[final emotional image]。

负面限制：
不要换脸，不要换衣服，不要改变场景，不要多重运镜，不要快速乱晃，不要突然拉远，不要主体漂移，不要动作过大，不要新增无关人物，不要文字水印。
```

## Text-to-Video Package

For text-to-video:

```text
[Subject] [mid-action verb] in [setting], [one secondary motion], camera [one specific movement], [lighting/mood], [composition/lens], [final emotional endpoint].
```

## Tool-Specific Notes

Runway-style:

- Keep prompt simple and positive.
- For image-to-video, focus on camera motion, subject action, and environmental motion.
- Avoid overloading negative phrasing inside the main prompt.

Luma-style:

- Describe temporal movement directly.
- Use clear camera movement phrases: slow push-in, slow pan right, camera dollies forward, aerial descending shot.
- Avoid vague beauty words; name the motion and visible result.

General AI video:

- One shot, one main action, one camera movement.
- Put continuity locks before creative motion if identity matters.
- Put avoid list at the end.
- When a shot is failing, revise one variable at a time.

## Tension Presets

压迫感:

```text
低机位近景，主体占据画面大部分，前景有暗色遮挡，背景空间被长焦压缩，镜头缓慢推进，阴影从画面边缘压入。
```

孤独感:

```text
极远景，人物很小，被巨大负空间包围，镜头缓慢后退，环境声音般的微动持续，最终人物停在空旷画面一角。
```

速度感:

```text
低角度广角跟拍，前景快速掠过形成视差，主体沿对角线冲入画面，短暂方向性运动模糊，最后切到稳定落点。
```

危险感:

```text
轻微荷兰角，前景黑影遮挡，主体半张脸在阴影里，镜头缓慢横移，背景威胁从负空间显露。
```

史诗感:

```text
极远景建立尺度，人物作为小剪影站在巨大结构前，逆光轮廓，镜头缓慢上仰或拉远，强调人和环境的悬殊比例。
```

