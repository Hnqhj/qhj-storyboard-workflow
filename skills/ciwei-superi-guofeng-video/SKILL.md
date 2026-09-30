---
name: ciwei-superi-guofeng-video
description: 刺猬星球 superi 风格的国风影视图像提示词与可灵 O3 图生视频提示词。触发：刺猬星球superi、superi风格、国风电影感、古装剧生图、古风封面、图生视频、可灵 O3、5秒剧情视频、单图多动作、连续3镜头。 Create cinematic Chinese historical-drama image prompts and Kling O3 image-to-video prompts in the "刺猬星球superi" style. Use when the user mentions 刺猬星球superi, superi风格, 国风电影感, 古装剧生图, 古风封面, 图生视频, 可灵 O3, 5秒剧情视频, 单图多动作, 视频失败优化, 连续3镜头, or asks to turn a Chinese historical character idea/image into a prompt workflow for ChatGPT, nano banana pro, Kling, Jimeng, DeepSeek, or Gemini.
---

# 刺猬Superi国风视频

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Purpose

Produce copy-ready prompts for realistic Chinese historical-drama images and 5-second image-to-video clips. Keep the output practical for a creator or fan: collect only missing choices, generate strong prompts, and continue the loop instead of ending after one prompt.

## Core Style

Always aim for a real period-drama story frame, not a costume photoshoot, character display, cosplay poster, game illustration, or static AI model pose.

Prioritize:

- realistic Chinese historical-drama texture
- restrained emotion and expressive eyes
- natural faces with skin texture, not oily, plastic, waxy, glassy, or over-smoothed
- refined but grounded costume, fabric, embroidery, hair ornaments, props, and set design
- shallow depth of field, soft side light, warm lantern/candle light, window light, or restrained palace light
- one clear story beat that can become a video first frame

Default image direction: vertical 9:16, cinematic close/medium portrait, shallow depth of field, ancient interior or grounded historical environment, subtle dramatic tension.

## Workflow Selector

Choose the smallest useful workflow:

- If the user gives only a theme or says "帮我生成一张你的/刺猬风格图": run the image prompt workflow. If key settings are missing, ask one question at a time or use Quick Mode when the user wants speed.
- If the user gives enough settings at once: do not re-ask them. Summarize the settings and generate the image prompt.
- If the user uploads or references an existing character image and wants video: inspect the image content, infer the story beat, and output a Kling O3 5-second image-to-video prompt plus negative prompt. Do not ask the user to specify the action.
- If the user describes a failed video result: diagnose the failure first, then output a revised Kling O3 prompt.
- If the user asks for "换一个动作", "同图多动作", "再来一个", or "B": keep the same image and create a new compatible action.
- If the user asks for "连续3镜头", "小剧情", or "系列": output three independent 5-second Kling O3 prompts with emotion progression.
- If the user asks to export this workflow for another platform, read `references/platform-exports.md`.

## Required References

Read only the reference needed for the current task:

- `references/style-card.md`: style rules, identity/scene adaptation, negative prompt vocabulary.
- `references/image-workflow.md`: interactive image prompt workflow, question set, quick mode, output templates.
- `references/kling-o3-video.md`: image-to-video prompt logic, failure optimization, single-image multi-action, 3-shot story mode.
- `references/platform-exports.md`: compact Custom GPT, DeepSeek, Gemini, and README-style exports.

## Image Prompt Workflow

For image generation, follow `references/image-workflow.md`.

Output should normally include:

1. 画面设定
2. 图片生成提示词
3. 负面提示词
4. 使用建议
5. 下一步菜单

If the user wants English prompts, add an English version after the Chinese prompt.

## Kling O3 Video Workflow

For uploaded/generated images, follow `references/kling-o3-video.md`.

Hard rules:

- Do not regenerate a new person.
- Preserve face shape, facial features, hairstyle, makeup, costume, hair ornaments, background, composition, and overall style.
- Infer the action from the image pose, eyes, hands, costume, scene, and emotional atmosphere.
- Use exactly one main action in 5 seconds.
- Make the action small to medium, but visible.
- Make the micro-expression subtle, but readable.
- End with the emotion settling, as if one line was left unsaid.
- Use slow push-in or slight lateral movement; avoid sudden zooms, fast pans, spins, dance, or large performance gestures.

## State Rules

Maintain the current project state inside the conversation:

- gender, age, identity, emotion
- clothing color/texture
- scene, lighting, composition, purpose
- uploaded image content
- last video action direction
- last next-step menu choice

When the user says "继续", "再来一个", "换一个动作", "同样风格再做一张", or similar, continue from the current state. Restart only when the user explicitly says "重新开始", "换一个新人物", "从头来", "清空设定", or "新开一个".

## Next-Step Rule

After every image prompt, video prompt, revised prompt, or 3-shot sequence, append a useful "下一步你想做什么？" menu. Keep the menu relevant to the current stage.

Do not add long explanations unless the user is learning the method. The primary deliverable is a prompt they can copy.

