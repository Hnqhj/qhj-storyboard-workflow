# Retry Control

Use this after a generation fails or before planning controlled iterations.

## One-Variable Retry

Change one main variable per retry:

- action intensity
- camera distance
- shot duration
- material realism
- identity lock strength
- background complexity
- motion blur amount
- style realism level

Do not change story, character, style, camera, and world at once unless the output is unusable.

## Retry Patch Format

The retain/change diagnosis stays outside the paste target. Recompile the final model-facing text into Liu's six-part positive-only prompt. Any camera retry must preserve or replace the complete camera-style master. Event beats inherit it; revise a local beat-camera clause only when that beat has a genuine special-camera need.

```text
保留：
只修改：
不修改：
新提示词补丁：
```

## Common Patches

Face changed:

```text
保留原动作和场景，只加强身份锁定：same face, same amber eyes, same black hair with cyan underlayer, face remains sharp during motion, no age drift, no hairstyle change.
```

Action too soft:

```text
保留角色和场景，只加强动作峰值：short anticipation, sudden acceleration, one 0.1s impact hold, clear follow-through, environment reacts to speed.
```

Camera messy:

```text
外部修改说明：保留动作因果，只修改镜头语言。
镜头语言总控：大卫·芬奇风格 + 低机位精确侧跟保持空间几何与主体轮廓稳定。
事件节拍：大卫·芬奇风格 + 低机位侧跟让脚步和接触面持续清晰；动作推进触发镜头跟随主角压力路线横移，命中后交接到受力者位移，最终停在可读后果构图。
```

Too cartoon:

```text
保留anime design，只提高真实感：3D cel-shaded semi-realistic lighting, physical materials, realistic cloth folds, skin SSS, no chibi, no flat manga panel look.
```

Background drift:

```text
保留人物动作，只加强世界锁定：same city palette, same architecture material, same lighting direction, no location teleport.
```
