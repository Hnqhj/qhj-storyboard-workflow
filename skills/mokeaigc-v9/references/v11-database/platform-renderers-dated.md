# V11 平台 Renderer 快照（查询用）

来源：`references/platform-renderers.md`；纳入日期：2026-07-19。

本文件完整保留原包的平台意图，但不宣称当前仍有效。执行前由对应 adapter 或官方资料复核。

## Generic

- 用用户要求的语言写一段干净的场景描述；
- 正向可见事实优先；
- 只有可能发生的失败才加简短排除句；
- 不自造平台参数。

## Midjourney（V11 源快照）

原包建议：参数置于末尾；已知比例时可加 `--ar`；只有用户提供时才加 `--sref` 和 `--profile`；模型版本只在用户指定时写；HD、stylize、排列组合和 `--no` 按任务选择；不输出空参数。

原包候选顺序：

```text
[scene] --ar [ratio] [--sref value] [--profile value] [--stylize value] [--v value] [--hd] --no [simple exclusions]
```

**使用门**：版本、参数名、HD 条件、style/profile 兼容、排列组合是否扩成多任务、负面词解析均必须由 `$midjourney-generation-adapter` 当天复核。

## Nano Banana（V11 源快照）

- 自然语言描述场景与排除项；
- 比例只陈述一次；
- 不混入 Midjourney 的 `--ar / --no / --sref / --profile / --stylize`；
- 不把“英文一定更好”当规律。

**使用门**：名称、入口、支持的设置和执行方式必须用当前平台资料复核。

## GPT Image（V11 源快照）

- 直接描述构图、动作、连续性锚点、光、材质与期望排除；
- 比例/方向作为设置或自然语言说明；
- 正向事实优先，负面项压成一个短块；
- 不复制 Midjourney 参数。

执行提示词仍由 `$im2-clean-image` 和当前图像执行器完成。

