# Source Map

## 2026-06-29 - AI Video Storyboard Feasibility

Research question: should this skill output a full production storyboard, or add a separate AI-video generation storyboard gate?

Sources:

- OpenAI Sora 2 Prompting Guide, official cookbook: https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide
  Source-backed platform note that video prompts benefit from clear subject, action, scene, style, camera, and timing language; Sora-specific facts are not generalized into durable rules.
- Runway Gen-4 Video Prompting Guide, official help center: https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide
  Prompt guidance emphasizes describing what should happen, concise positive direction, camera/action clarity, and reference consistency; avoid relying on unsupported negative wording as the main control.
- Google Vertex AI Veo prompt guide, official documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide
  Prompt components include subject, context, action, style, camera motion, composition, ambiance, and audio; negative prompts should be separated and worded carefully when the platform supports them.
- The Science Behind Pixar, Story and Art, Pixar-affiliated educational exhibit: https://sciencebehindpixar.org/pipeline/story-and-art
  Storyboard/storyreel practice supports early visual sequencing, rhythm, and audience understanding before final production.

Mechanism extracted:

- A professional storyboard may contain richer production intent, but an AI-video-ready storyboard needs a second feasibility layer: reference role, first-frame anchor, segment split, action load, dominant camera move, and platform-aware negative strategy.
- For image-to-video, the still image should be treated as the starting visual authority; the text prompt should mainly specify motion, camera behavior, expression or prop changes, and what must remain locked.
- Platform guidance is current and model-specific; keep it as a source-backed prompt-control note, not as an active capsule until validated by generated outputs.

## 2026-06-29 - AI Video Segment Split And Handoff

Research question: when should an AI-video storyboard stay as one generated segment, use continuous extension, or split into separate prompts/cuts?

Sources:

- OpenAI Sora 2 Prompting Guide, official cookbook: https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide
  Source-backed notes: shorter clips can follow instructions more reliably; each shot block should keep one camera setup, one subject action, and one lighting recipe; extension uses the full original clip as context.
- Google Cloud Veo prompt guide, official documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide
  Prompt components include subject, camera angle, camera movement, lighting, style, and environment; advanced camera instructions may vary in reliability.
- Google DeepMind, How to create effective prompts with Veo 3: https://deepmind.google/models/veo/prompt-guide/
  Prompt design asks creators to decide shot framing, subject motion, style, and camera movement explicitly.
- Luma Ray2 FAQ, official learning hub: https://lumalabs.ai/learning-hub/dream-machine-guide-ray2
  Ray2 supports 5 or 10 second videos and extension for longer output, with quality risk after repeated extension.
- Luma Ray, official product page: https://lumalabs.ai/ray
  Multi-keyframe controls support directing what changes, what holds, and how the story lands inside a clip.

Mechanism extracted:

- One generated segment is safest when it has one location/time state, one subject/action focus, one dominant camera move, and a duration the model supports.
- Continuous extension is for the same scene continuing forward; the previous end frame must logically become the next first-frame anchor.
- Hard cuts or separate prompts are safer for location/time jumps, lighting changes, axis/viewpoint changes, new reference roles, major action phase changes, or style shifts.
- Each split needs a handoff note: previous end state, next first-frame anchor, continuity locks, allowed changes, and cut reason.

## 2026-06-29 - Dialogue Reaction And Split-Edit Timing

Research question: in dialogue or quiet emotional scenes, should storyboard priority stay on the speaker, or shift toward listener reaction, pauses, and sound-image bridges?

Sources:

- Pixar in a Box / Khan Academy, Storyboarding scene: https://www.khanacademy.org/partner-content/hass-storytelling/storytelling-pixar-in-a-box/ah-piab-film-grammar/v/storyboarding-scene
  Storyboarding is framed as finding visual balance for scene emotion and message before production.
- Adobe, L cut and J cut in film: https://www.adobe.com/creativecloud/video/post-production/cuts-in-film/l-and-j-cut.html
  Split edits are described as audio/visual shifts that improve flow and allow reaction shots, especially in dialogue scenes.
- Walter Murch, ProVideo Coalition interview: https://www.provideocoalition.com/aotc-murch-books/
  Practitioner interview context for editing around brevity, rhythm, and scene feel.
- Walter Murch, The Guardian essay on editing The Conversation: https://www.theguardian.com/film/2025/feb/28/i-spent-12-hours-a-day-for-16-months-with-gene-hackman-but-never-met-him-the-conversations-walter-murch-pays-tribute
  First-person account that actor rhythm and micro-behavior can guide pacing and cut decisions.
- StoryboardArt, Cinematography for Storyboard Artists: https://storyboardart.org/storyboard-tutorials/cinematography-and-film-for-storyboard-artists/
  Storyboard-focused source defining reaction shots as showing emotional response to story-significant information, with camera position affecting audience relation.
- Barry Salt, How Top Editors Cut Dialogue Scenes: https://ochre.lib.uchicago.edu/ochre?load=&uuid=b3c2546c-f0d8-473f-a012-531171718682
  Empirical sample of dialogue-scene edits tracking L-edits, J-edits, pauses, and reaction-shot proportions; useful as evidence of variation, not as a universal formula.

Mechanism extracted:

- Dialogue storyboard should treat listening, hesitation, delayed reply, and offscreen sound as visible story events, not filler between lines.
- J-cut/L-cut or sound-bridge notes are useful when the reaction or pressure begins before the image changes, or when the speaker's audio should continue over a listener/object/detail shot.
- Do not turn this into a fixed editing formula. Use it only when it clarifies emotion, power relation, pacing, or subtext.

## 2026-06-29 - Reference Breakdown To Storyboard Transfer

Research question: when a user asks for 拉片转分镜, should the skill extract attractive shots directly, or first build a whole-reference grammar and then transfer only mechanisms?

Sources:

- Pixar in a Box / Khan Academy, Storyboarding scene: https://www.khanacademy.org/partner-content/hass-storytelling/storytelling-pixar-in-a-box/ah-piab-film-grammar/v/storyboarding-scene
  Storyboarding is treated as visual scene construction through composition, character dynamics, and film grammar rather than isolated images.
- Pixar in a Box / Khan Academy, Storytelling: https://www.khanacademy.org/computing/pixar/storytelling
  Film grammar is framed as a visual language where scene, shot, and frame choices tell story.
- Adobe, Continuity Editing: https://www.adobe.com/creativecloud/video/hub/ideas/what-is-continuity-editing-in-film.html
  Continuity work grounds viewers in time and space through eyeline, 180-degree axis, match cuts, and eye trace.
- DGA, How to Design Shootable Sequences While Working with a Storyboard Artist: https://www.dga.org/events/2024/july2024/ddi_storyboarding-0524
  Storyboarding is described as a tool for communicating artistic vision under production constraints.
- StoryboardArt, Cinematography for Storyboard Artists: https://storyboardart.org/storyboard-tutorials/cinematography-and-film-for-storyboard-artists/
  Storyboard panels function as pre-editing: ordered camera, depth, movement, and transition choices.
- David Bordwell, Observations on Film Art / Editing norms: https://www.davidbordwell.net/blog/category/technique-editing/
  Editing norms are contextual options; a reference pattern should be understood as a choice within a menu, not copied as a universal rule.
- StudioBinder, Movie Storyboard Examples: https://www.studiobinder.com/blog/storyboard-examples-film/
  Public storyboard examples show directional arrows, pacing notes, background/action information, and department-facing continuity cues.

Mechanism extracted:

- Reference-to-storyboard work should begin with whole-clip grammar: purpose, geography, shot-size rhythm, transition logic, and sound/visual bridge.
- Transfer mechanisms, not surface arrangements: shot function, spatial relation, rhythm curve, transition trigger, depth strategy, and information ladder.
- Mark non-transferable risks explicitly: original plot business, character identity, scene-specific composition, copyrighted arrangement, or reference-specific production constraints.

## 2026-06-29 - Product / Prop Ad Storyboard Proof Ladder

Research question: in product or prop advertising storyboards, should the skill prioritize beauty shots, or use/scale/material proof plus early product recognition?

Sources:

- Google Ads Help, About the ABCDs of effective video ads: https://support.google.com/google-ads/answer/14783551?hl=en
  Official creative guidance supports early product/brand presence, focused messaging, attention, connection, and clear direction.
- Think with Google, YouTube ABCDs: Video ad best practices: https://business.google.com/us/think/future-of-marketing/youtube-video-ad-creative/
  Applies ABCD principles at storyboard stage; useful as evidence that execution choices such as opening, product presence, sound, and CTA belong in the board.
- Nielsen Norman Group, UX Guidelines for Ecommerce Product Pages: https://www.nngroup.com/articles/ecommerce-product-pages/
  Product pages fail when shoppers cannot decide whether the item fits their needs; storyboard product shots should answer purchase-relevant questions, not only look polished.
- Baymard Institute, Product Page UX research overview: https://baymard.com/research/product-page
  Large-scale PDP research highlights how product information, images, video, and product details affect user decisions; useful for deciding which visual proof shots matter.
- Baymard Institute, UX Research on Product Page Videos: https://baymard.com/blog/embedding-product-page-videos
  Product videos help some users imagine how a product fits into their lives, but only if the video is discoverable and tied to the product evaluation path.
- TikTok Ads Manager, Creative best practices for performance ads: https://ads.tiktok.com/help/article/creative-best-practices
  Platform-specific guidance supports visible content, vertical format, early proposition, hook, and CTA; keep as platform note rather than universal cinema rule.

Mechanism extracted:

- Product/prop ad storyboards should run a proof ladder: need/context -> early product or brand recognition -> scale/hand relation -> material or mechanism proof -> benefit/result -> memory frame or CTA.
- A beauty shot is valid only when it proves something concrete: scale, material, craftsmanship, mechanism, use, comparison, benefit, or brand memory.
- Platform/social variants need explicit first-seconds hook, safe-zone/aspect-ratio, audio/text reinforcement, and CTA notes.
- This remains a normal storyboard mode by default. Do not escalate to high-tension treatment unless the product concept itself relies on danger, speed, pursuit, or conflict.

## 2026-06-29 - High-Speed Action Spatial Readability

Research question: in high-speed chase/action storyboards, how can speed and pressure increase without collapsing spatial readability, especially for AI video?

Sources:

- StoryboardArt, Cinematography for Storyboard Artists: https://storyboardart.org/storyboard-tutorials/cinematography-and-film-for-storyboard-artists/
  Storyboard panels act as pre-editing; camera placement, depth, motion, and transition choices must preserve readable staging.
- Every Frame a Painting, Jackie Chan - How to Do Action Comedy: https://vimeo.com/113439313
  Action readability is strengthened by showing full-body mechanics, holding impacts long enough, and cutting on clear physical causes and consequences.
- VashiVisuals, The Editing of Mad Max: Fury Road: https://vashivisuals.com/the-editing-of-mad-max-fury-road/
  The Mad Max: Fury Road case supports eye-trace control, centered action, and editorial discipline for fast visual comprehension.
- American Cinematographer, John Seale ASC ACS - Framing Mad Max: Fury Road: https://theasc.com/video/john-seale-asc-acs-framing-mad-max-fury-road/
  Cinematographer-facing source for how framing choices support fast action readability.
- David Bordwell, Off-center: Mad Max's headroom: https://www.davidbordwell.net/blog/2016/02/10/off-center-mad-maxs-headroom/
  Close analysis of Fury Road framing shows that centered eye-trace is one tactic among broader continuity and composition choices.
- Frontiers in Psychology, Continuity editing and event segmentation: https://www.frontiersin.org/articles/10.3389/fpsyg.2012.00515/full
  Cognitive evidence supports the idea that coherent action and spatial-temporal cues help viewers parse film events.

Mechanism extracted:

- High-speed storyboard design should assign one eye-trace anchor per beat before adding aggressive camera movement.
- Speed reads best through layered contrast: stable subject/silhouette, fast foreground pass, slower background parallax, visible route obstacle, and one peak rupture.
- After occlusion, subjective POV, heavy blur, whip pan, or close detail, insert a geography reset before the next maneuver.
- For AI video, each generated segment should keep one dominant motion vector and one dominant camera move; piling multiple camera devices into one segment increases spatial drift and action unreadability.

## 2026-07-08 - Local Imported Suspense / Seedance / Qianchuan Materials

Research question: how should the skill absorb user-supplied local craft manuals for suspense storyboard design, Seedance prompt packaging, and conversion-focused ad storyboards without bloating SKILL.md or conflicting with Liu's existing asset-handle rules?

Local sources inspected from the user's supplied files:

- `顶级悬疑导演分镜运镜·构图光影一体化训练手册（3天精通版）(1).pdf`
  - Extracted a suspense-control model: first choose the suspense type and information state, then make composition, light, camera, editing, sound, VFX, and transition serve the same release/withholding job.
- `3.4分镜设计（优化）(1).zip`
  - Inspected Markdown/TXT/DOCX/PDF/XLSX previews including Seedance prompt templates, storyboard-to-prompt conversion, official-style prompt guidance, prompt hygiene, and title-font prompt examples.
- `分镜策划师（千川-广告的）.md`
  - Extracted a Qianchuan ad storyboard workflow: classify frame type, preserve exact copy/dialogue, bind voice to visible action nodes, and segment by 15-second commercial beats.
- `SKILL_vYZJJu.md`
  - Extracted SaaS/software motion-design ad patterns: first-two-second hooks, UI/device/product proof sequences, style lanes, motion transitions, and CTA structure.
- `Quill_GPT电影感提示词_v5.0.md`
  - Extracted clean still/keyframe prompt hygiene: one visual center, style selection, reference preservation, and practical fixes for dirty, over-sharp, gray, fake-face, or unclear product outputs.

Mechanism extracted:

- Suspense boards need a dedicated control reference because the imported manual treats all shot components as a unified suspense machine.
- Seedance packaging needs a dedicated reference because imported materials mix `@图片N` and `@material[...]` dialects; the skill must preserve their reference-role logic while defaulting Liu's local final prompts to `{{Image 1}} / {{Video 1}} / {{Audio 1}}` unless a target surface explicitly requires `@` handles.
- Qianchuan / ad boards need a dedicated reference because conversion-focused ad storyboards use a proof ladder and sound-picture synchronization that differs from normal narrative coverage.
- The detailed imported manuals stay in references, not SKILL.md, to preserve progressive disclosure.

## 2026-07-08 - Bilibili Fight Storyboard Lessons: Action, Dynamic Line, Scene Design

Research question: how should this skill design fight/action storyboards so they are not just camera-move lists, but character-driven, physically readable, and visually spectacular through line movement and scene-line organization?

Sources reviewed in order from the user's supplied links:

- `【打戏分镜】01 动作设计` - https://www.bilibili.com/video/BV1mwzkBbExz/
  - Reviewed through low-resolution public playback, local frame sheets, and local ASR transcript. Transferable mechanism: fight choreography starts from character posture and shape language; action is performance, not only event coverage.
- `【打戏分镜】02 动态线设计` - https://www.bilibili.com/video/BV1HC6kBsEYK/
  - Reviewed through low-resolution public playback, local frame sheets, and local ASR transcript. Transferable mechanism: fight spectacle comes from visible line movement that makes force travel readable; camera can be shot-first for information or action-first to support the performer line.
- `【打戏分镜】 03 场面设计` - https://www.bilibili.com/video/BV15AFWzzEC8/
  - Reviewed through low-resolution public playback, local frame sheets, and local ASR transcript. Transferable mechanism: scene scale is built from interlaced body, weapon, costume, crowd, spatial, and perspective lines; a small space can produce a large scene when line movement fills frame depth clearly.

Mechanism extracted:

- Fight boards should start with a role/value and silhouette contract. Pre-fight and post-impact poses are useful when they tell the audience who the fighters are, what values conflict, and what changed.
- Dynamic line is the visible path of force. Every action phrase should identify force source, dominant carrier, contact/near-miss, receiver response, and recovery or changed spacing.
- Camera-first fight coverage splits information; action-first fight coverage protects the performer's line and asks the camera to reveal it. Choose deliberately per beat.
- Large scene design is not equal to large location or many extras. Scale comes from organized line density across body, weapon, costume, crowd, environment perspective, and camera motion.
- For AI video, translate fight beats into one main action spine, one camera owner, explicit posture/line carriers, and positive silhouette locks.

Implementation:

- Added `references/imported-fight-storyboard-line-system.md`.
- Added fight routing to `SKILL.md` and a fight/action line storyboard template to `references/output-templates.md`.
- 2026-07-08 follow-up readability patch: added a model-executable interpretation layer so abstract terms such as posture, dynamic line, force transfer, and big scene must be converted into concrete fields: carrier, source, path, target, result, camera duty, and AI segment limit.
