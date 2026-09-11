# Output Contract

Choose the lightest response mode that satisfies the user. User-facing explanation may use the user's language. The master prompt must be English except for exact non-English text that must visibly appear in the image.

## Guided default

Use this structure.

### Concept direction

In three to six concise lines, state:

- absolute subject and category
- intended emotional effect
- selected scale strategy and reference object
- camera and framing logic
- environment, material language, light, and palette

Label meaningful assumptions from an underspecified brief. Do not expose or quote internal source-rule text.

### Master prompt

Provide one copyable block of coherent natural English. Use this internal order without visibly numbering it:

1. visual language and emotional target
2. subject form, physical dimensions, construction or anatomy, and micro-scale surface density
3. environment, physical anchoring, atmospheric layers, and implied event
4. distant scale reference and its spatial relationship to the subject
5. composition percentages, negative space, crop behavior, viewpoint, focal length, and depth behavior
6. materials, light, color grading, realism, and concise failure-prevention constraints

Use only details that change the image. Avoid repeating synonyms for size or quality. Keep provider parameters outside the prompt.

### Negative prompt

Include only when the selected model or workflow benefits from one. Target likely failures:

- foreground scale reference
- ordinary-sized subject
- toy-like miniature appearance
- complete isolated architecture when an endless crop is required
- incoherent perspective or contradictory depth
- malformed anatomy or duplicated limbs
- material violations in pure-organic mode
- random text, logos, frames, watermarks, UI, or signatures

Prefer a short focused list over a second full prompt.

### Model recommendations

Recommend two to four suitable models. For each, include:

- role: primary, visual alternative, efficient baseline, or editing option
- why it fits this concept
- verified model ID or UI mode when known
- aspect ratio and resolution or size
- relevant quality or prompt-optimization mode
- number of independent runs

End with a fair comparison plan using the same master prompt, ratio, approximate resolution, and run count.

## Prompt-only mode

When the user explicitly requests only the prompt, return only the English master prompt. Omit concept analysis, rule names, recommendations, and commentary. Keep the first-use note only if the user did not ask for absolutely no surrounding text.

## Multiple concepts

Vary the physical thesis, scale reference, frame logic, environment, and emotional effect rather than swapping adjectives. Keep user-mandated identity and exclusions fixed. Recommend models once after all concepts unless their needs differ materially.

## Reference-analysis mode

Separate observable scale cues, transferable visual rules, preserved elements, and intended changes. Then provide a standalone English prompt unless the same image will be uploaded to the generator.

## Existing-concept iteration

State what remains stable and what changes. Return a complete copyable master prompt unless the user asks for only a surgical replacement section.

## Model adaptation

Keep one semantic master prompt across models. Add only the minimum provider adapter outside it: aspect ratio, resolution, quality mode, reference fidelity, prompt optimization, seed, or negative prompt. Do not rewrite the whole prompt merely to change parameter syntax.

