# Reference Image Mode

Use this reference when the user provides or mentions a character image, object image, scene image, style reference, or layout reference.

## Core Rule

The reference image is not the whole poster. The poster is still led by the core title and its meaning. The reference image becomes a semantic carrier, identity anchor, visual texture, or layout constraint.

Never produce a simple pasted-character cover. Integrate the reference with typography and metaphor.

## Reference Type Logic

角色图:

- Preserve identity cues the user requests: face, hair, costume, posture, silhouette, weapon, prop, or attitude.
- Let the character interact with the title: standing in front of the text, half-hidden by strokes, trapped in negative space, leaning against a letter, cut by a character stroke, or scaled against the word.
- Keep the title readable and dominant. The character should not become a generic portrait that ignores the word.

物体图:

- Use the object as the metaphor carrier.
- Connect the object to the title through scale, material, shadow, fracture, reflection, absence, or placement inside letterforms.
- Avoid literal product poster treatment unless the user asks for advertising.

风格图:

- Borrow palette, texture, line quality, print feel, lighting mood, and design density.
- Do not copy the original composition or subject unless allowed.
- Translate the style into the current word's meaning.

版式参考:

- Borrow hierarchy, margin logic, title placement, grid density, caption style, or visual balance.
- Replace the content with the current semantic concept.
- Keep the result original and tied to the word.

场景图:

- Use the scene as atmosphere or spatial metaphor.
- Let the title inhabit the scene: as signage, architectural mass, shadow, cutout, wall text, object scale, or negative space.
- Avoid making the scene a normal background.

## Preservation Map

When user says "保留角色", default to preserving:

- face identity
- hairstyle
- outfit silhouette
- major accessories
- overall pose attitude
- color mood if it matters

When user says "只参考风格", do not preserve identity, specific subject, exact pose, or scene content.

When user says "保留版式", preserve layout hierarchy but not exact text or imagery.

## Image-Assisted Output Template

```text
【参考图判断】
[参考图提供的价值：角色/物体/风格/版式/场景]

【概念方向】
[核心文字如何与参考图形成隐喻关系]

【封面海报生成提示词】
基于我提供的参考图，为「[核心文字]」生成一张高级概念封面海报。参考图用于[保留/参考内容]，但画面不能只是把参考图贴在背景上，必须让「[核心文字]」成为主视觉标题和语义核心。

核心标题「[核心文字]」以大尺寸出现在画面中，字形清晰、强烈、可读，成为封面的视觉骨架。参考图中的[角色/物体/场景/风格]与标题发生关系：[遮挡、嵌入、穿过、站在字前、藏进负空间、被字形切割、与字形成距离或冲突]，用来表达[语义情绪和隐喻]。

保留参考图的[需要保留项]，允许重新设计[可改变项]。整体构图极简、强概念、强排版，元素克制，留白明确。风格为高级图形艺术封面，平面设计感强，带细微纸张纹理、印刷颗粒、拼贴/丝网印刷/石版印刷质感，色彩控制在[配色]，标题、图像和辅助小字自然融为一体。

【负面提示词】
直接贴图，角色贴纸感，参考图抢主题，标题不可读，图文无关，普通插画，廉价模板，广告页，电商排版，元素堆砌，杂乱背景，过多装饰，低级拼贴，过脏做旧，三维塑料感，错字，乱码，额外文字，水印，logo。
```

## Quality Check

Confirm:

- The title remains the first visual layer.
- The reference image has a clear job.
- The image and text physically or conceptually interact.
- The result can still be understood without reading a long explanation.

