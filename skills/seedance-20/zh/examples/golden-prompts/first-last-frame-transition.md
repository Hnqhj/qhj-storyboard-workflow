# 黄金提示词：首末帧过渡

## 来源 brief

从一个已知的产品状态移动到另一个。

## 内部提示词规格

模式：FLF2V。`[Image1]` 是首帧。`[Image2]` 是最终视觉目标。无不相关的故事节拍。

## 编译后的自然语言提示词

[Image1] 是首帧，[Image2] 是最终视觉目标。保留相同的产品身份、logo、标签和桌面几何。只生成连续过渡：瓶身上凝结水珠，沿前方玻璃滑落一次，停止时产品与 [Image2] 精确对齐。镜头保持固定；声音是端点处一声柔和的玻璃轻响。

## Lint 结果

lint: pass

## 控制关键句

为何保留：`[Image2] is the final visual target` 锁定端点角色。

为何保留：`Generate only the continuous transition` 防止额外故事泄露进来。
