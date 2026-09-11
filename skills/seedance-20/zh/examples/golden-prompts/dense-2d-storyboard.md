# 黄金提示词：密集 2D 分镜

## 来源 brief

创作一个带三个剪切的短 2D 动画分镜板。

## 内部提示词规格

媒介：2d_animation。镜头结构：dense_multishot。使用动画版式词汇，避免真人实拍的镜头行为。

## 编译后的自然语言提示词

镜头 1：手绘赛璐珞动画，前景雨层向下滑动而背景街道保持静止；快递员剪影入画并停在招牌下。镜头 2：角色近景版式，两帧眨眼保持，围巾随风从左到右拖影，结束于她的目光锁定在箱子上。镜头 3：俯视动画版式，水洼倒影层涟漪一次后在箱子周围平复。不使用摄影镜头或传感器语言。

## Lint 结果

lint: pass

## 控制关键句

为何保留：`foreground rain layer` 和 `background street holds` 使用动画层语法。

为何保留：`No photographic lens or sensor language` 保护 2D 媒介合同。
