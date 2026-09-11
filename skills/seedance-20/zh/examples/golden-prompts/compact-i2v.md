# 黄金提示词：紧凑 I2V

## 来源 brief

在不改变产品的前提下让一张产品静帧动起来。

## 内部提示词规格

模式：I2V。参考：`[Image1]` 控制产品身份。当前片段动作：一次光线扫过。端点：logo 保持可读。

## 编译后的自然语言提示词

[Image1] 是产品身份参考；精确保留其 logo、形状、颜色和材质。只有一道狭窄的暖光扫过玻璃，结束时标签清晰可读。镜头保持固定。声音：在最终高光处一声柔和的轻响。

## Lint 结果

lint: pass

## 控制关键句

为何保留：`[Image1] is the product identity reference` 将静帧仅绑定到身份。

为何保留：`Only a narrow warm light sweep moves` 防止静态产品细节被重新生成。
