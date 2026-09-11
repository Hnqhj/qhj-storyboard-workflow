# Image Model Routing and Parameters

Baseline reviewed: 2026-08-10. Treat rankings, pricing, availability, and parameters as time-sensitive. Refresh current official documentation and an independent benchmark when the user asks for the latest answer.

## Select from the finished concept

Prioritize the demands that actually determine success:

- global spatial coherence and convincing scale
- architectural geometry and repeated human-scale detail
- creature anatomy and unfamiliar biological texture
- photorealistic material, atmosphere, and cinematic light
- reference-image adherence and identity preservation
- editing, iteration speed, output resolution, and cost

Recommend two to four models by default:

1. primary quality choice
2. a model with a contrasting visual strength
3. an efficient baseline when speed matters
4. an editing or reference specialist only when useful

Use at least two independent generations per model. Use four for serious selection because one image does not establish a model's capability.

## Routing baseline

### GPT Image 2

Prefer as the primary choice when the prompt depends on strict spatial instructions, measurable composition, coherent relationships between subject and reference object, or a complex hybrid concept. Include it in architecture and creature comparisons, but do not assume it will always produce the most dramatic cinematic texture.

Verified OpenAI API settings:

- model: `gpt-image-2`
- vertical: `size="1024x1536"`
- landscape: `size="1536x1024"`
- square: `size="1024x1024"`
- exploration: `quality="medium"`
- final: `quality="high"`
- editable or lossless delivery: `output_format="png"`
- runs: 2 for comparison, 4 for final selection

The API exposes the three listed sizes plus `auto`. For a different ratio, choose the closest orientation and crop or extend deliberately afterward.

Official references: [GPT Image 2](https://developers.openai.com/api/docs/models/gpt-image-2), [Images API fields](https://developers.openai.com/api/reference/resources/images).

### Seedream 5.0 Pro

Prefer as a strong visual alternative for photorealistic cinematic scale, atmospheric depth, dense materials, creatures, Chinese-language creative direction, and workflows that may require precise editing. Compare it directly with GPT Image 2 for the final aesthetic decision.

Verified BytePlus settings:

- model: `dola-seedream-5-0-pro-260628`
- final prompt optimization: `optimize_prompt_options.mode="standard"`
- rapid exploration: use `fast` only when speed matters
- seed: random for exploration; fixed for controlled iteration when the provider exposes it
- final output: use the highest available resolution matching the ratio, preferably 2K or above
- runs: 2 for comparison, 4 for final selection

Seedream 5.0 Pro does not support streaming or `guidance_scale` in the verified BytePlus interface. Provider wrappers may expose different aliases and controls; name the provider before giving additional fields.

Official references: [BytePlus Seedream](https://www.byteplus.com/en/product/Seedream), [BytePlus image API](https://docs.byteplus.com/api/docs/ModelArk/1541523).

### Nano Banana 2

Use as an efficient baseline for high-volume exploration, conversational iteration, multi-reference workflows, and fast comparison of composition ideas. It is useful for discovering promising directions even when another model is the final-quality favorite.

Verified Gemini API settings:

- model: `gemini-3.1-flash-image`
- aspect ratio: match the brief, such as `"2:3"`, `"4:5"`, `"1:1"`, `"16:9"`, or `"9:16"`
- exploration: `image_size="2K"`
- final comparison: `image_size="4K"`
- output: request image-only PNG when the interface supports it
- runs: 2 for comparison, 4 when judging consistency

Official reference: [Gemini image generation](https://ai.google.dev/gemini-api/docs/image-generation).

### Nano Banana Pro

Use when reference fidelity, factual or search-grounded context, precision editing, or consistency across a professional asset set matters. Treat it as a specialist, not an automatic aesthetic winner for colossal imagery.

Verified Gemini API settings:

- model: `gemini-3-pro-image`
- aspect ratio: match the brief
- exploration: `image_size="2K"`
- final: `image_size="4K"`
- use search grounding only when current factual information is actually required
- runs: 2 for comparison, 3 to 4 for final selection

Official references: [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image), [Gemini image generation](https://ai.google.dev/gemini-api/docs/image-generation).

## Concept-specific shortlist

### Architecture or mechanical megastructure

Start with GPT Image 2 for instruction and geometry adherence, then Seedream 5.0 Pro for a cinematic material alternative. Add Nano Banana 2 when rapid composition exploration is useful.

### General creature or pure-organic entity

Start with Seedream 5.0 Pro and GPT Image 2 in parallel. Judge anatomy, silhouette, surface coherence, and the tiny reference object separately rather than choosing on mood alone.

### Cosmic horror

Compare GPT Image 2 for semantic control with Seedream 5.0 Pro for atmosphere and organic texture. Add Nano Banana 2 when the user wants many divergent concepts quickly.

### Reference-led work or iterative editing

Add Nano Banana 2 or Nano Banana Pro according to the available interface and precision needs. Keep the same reference set and preservation instructions across the comparison.

## Aspect ratio guidance

- `2:3` or `4:5`: towering vertical structures, standing entities, portrait-oriented concept art
- `16:9` or `3:2`: continent-spanning architecture, horizontal creatures, cinematic environments
- `1:1`: neutral exploration and social previews
- `9:16`: extreme vertical height, mobile display, or a deliberate abyss-to-summit composition

Choose the ratio from the subject's dominant axis and negative-space plan, not from habit.

## Fair test protocol

Keep fixed:

- semantic master prompt
- aspect ratio and approximate resolution
- reference inputs and preservation instructions
- number of independent runs
- negative prompt, when the compared interfaces support it equivalently

Score separately:

- immediate perception of impossible scale
- subject and material fidelity
- reference-object distance and readability
- architecture or anatomy coherence
- composition, negative space, and crop behavior
- atmospheric depth, light, texture, and emotional fit
- production usability and editability

Choose the winner for the specific concept, not the global leaderboard.

