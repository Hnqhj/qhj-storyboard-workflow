# Poster Principles

Use this reference to create a cover/poster prompt from user text.

## North Star

Create a high-concept graphic art poster based on the meaning of the text. The poster must not be a normal illustration and must not be a simple word effect where a large word is pasted onto the picture.

The audience should immediately feel why the word is expressed this way. The image should deepen the text; the text should remain the main theme.

## Semantic Analysis

Before writing the prompt, analyze the user text internally or in a very short visible section:

- literal meaning: what the text says on the surface
- emotional direction: gentle, cold, dangerous, lonely, romantic, oppressive, hopeful, innocent, desirous, orderly, conflicted, alienated, free, silent, destructive, reborn, etc.
- hidden tension: pun, contradiction, paradox, social meaning, philosophical meaning, psychological weight, or emotional depth
- visual logic: human relation, object relation, action relation, spatial relation, contrast, symbol, conflict, order, absurdity, poetic relation
- concrete carrier: if the word is abstract, find a concrete visual carrier; if the word is concrete, avoid literal illustration by adding scale, relation, absence, contradiction, or atmosphere

## Composition Logic

The whole poster must be minimal, clear, and strong.

Use:

- large main text as the visual skeleton
- few key image elements
- clear hierarchy: main text first, image narrative second, tiny supporting text third
- intelligent negative space
- stable, readable poster composition

Let visual elements relate to typography. They may:

- stand in front of the text
- hide behind the text
- enter the counter-space or negative space of the letters/characters
- cut through the strokes
- lean against the title
- distort one part of the title only when semantically justified
- create tension through distance, direction, scale, or obstruction

Avoid:

- messy commercial illustration
- random decorative objects
- too many symbols
- ordinary screenshot-like composition
- generic background plus pasted text

## Visual Metaphor Strategy

Choose one dominant metaphor. Good metaphors should be understandable but not childish.

Useful strategies:

- absence: show what is missing rather than what is present
- scale: one tiny figure against an oversized word or object
- obstruction: the word blocks, traps, cuts, or hides the subject
- inversion: the normal relation is reversed
- distance: emotional meaning is shown through spacing
- gravity/direction: falling, rising, pulling, drifting, sinking, or resisting
- order/breakage: grid, repetition, one broken element
- material contradiction: soft word made from hard object, warm word in cold space, clean word damaged by one precise wound
- relation: two subjects separated, leaning, tied, mirrored, or unable to touch

## Style

Use advanced graphic art poster style:

- flat graphic design feeling, not 3D illustration
- collage / silkscreen / lithograph / printmaking texture
- clean paper texture, subtle grain, slight print noise
- strong controlled color logic
- limited palette, usually 2-4 colors
- high-saturation background with large light title when useful
- clear but simplified figure/object details
- crisp, restrained, hard-edged, conceptual print quality

Avoid:

- cheap template poster
- low-grade collage
- ad page layout
- ecommerce layout
- overly dirty vintage texture
- overdecorated commercial illustration

## Typography

The user-provided text must be the core title:

- Make it large, clear, and forceful.
- Preserve English words or letter groups exactly.
- For Chinese, use large readable Chinese characters unless a more suitable typographic arrangement is clearly needed.
- Add at most one tiny supporting caption if it deepens the theme.
- Tiny numbering, signature, or edition text is allowed only when it strengthens the art-poster feeling.
- All text must feel integrated into the image, not added afterward.

## Output Template

Use this default output:

```text
【语义判断】
[1-3 short bullets: meaning, emotion, visual logic]

【概念方向】
[One concise concept sentence explaining the metaphor]

【封面海报生成提示词】
为「[用户文字]」生成一张高级概念封面海报。画面不是普通插画，也不是简单字效，而是基于词义自动构建视觉隐喻的极简图形艺术海报。

核心标题文字为「[用户文字]」，以大尺寸作为画面主视觉骨架，占据画面重要区域，字形清晰、有压迫感、有平面设计力量。画面通过[核心视觉隐喻]表达这个词的[情绪/语义张力]。图像元素数量极少，仅保留[关键主体/物体/关系]，并让它们与文字发生关系：[嵌入/遮挡/切割/站在字前/利用负空间/形成距离或冲突]。

整体构图极简、干净、稳定，文字为第一视觉层，图像叙事为第二视觉层，少量小号辅助文字为第三视觉层。留白克制而有呼吸感。风格为高级图形艺术海报，带有拼贴感、丝网印刷感、石版印刷感或版画式质感，细微纸张颗粒和印刷噪点，色彩控制在[2-4色配色]，强对比，清爽利落，有展览海报、收藏海报和传播封面的质感。

可加入一句极小号辅助短句：「[可选短句]」，放在[左下/右下/边缘]，自然融入版式。整体画面要让人一眼感受到「[用户文字]」为什么被这样表达，图与字强关联，聪明、准确、耐看。

【负面提示词】
普通插画，单纯大字贴图，廉价字效，模板海报，商业广告页，电商排版，元素堆砌，杂乱背景，过多装饰，低级拼贴，过脏做旧，三维卡通感，游戏海报感，赛博故障风滥用，文字不可读，错字，乱码，额外文字，水印，logo，画面拥挤，词义不清，图文无关。
```

## Compact Output

If the user wants only the prompt, omit the analysis and concept sections.

## Input Form

When asking the user for structured input, use:

```text
用户输入内容：
核心文字 / 单词 / 词组 / 字母：
文字语言：
可选补充语境：
可选情绪倾向：
可选禁用元素：
```

Only ask for this form when the user has not supplied any core text.

## Quality Check

Before finalizing, verify:

- The title text is the visual center.
- The metaphor grows from the word meaning.
- The poster has few elements and clear hierarchy.
- The result is not just beautiful; it says the word's psychological state.
- The prompt avoids unnecessary explanation and is ready to copy.

