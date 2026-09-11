# 黄金提示词：续接中的观察偏差

## 来源 brief

计划说主体到达了门口，但被接受的片段在距门两步处结束。

## 内部提示词规格

使用 observed_end_state，而非 planned_end_state。把未完成的节拍带入当前片段。

## 编译后的自然语言提示词

从被接受的末帧开始：旅客仍距敞开的后车门两步，正迈步中，手提箱在身后。先只完成这两步，然后让她够到门把手。保持相同的从左到右移动、黑色轿车、雨中反光和跟拍镜头。不要假设她已经在门口。在这两步完成之前，不要把她置于车内。

## Lint 结果

lint: pass

## 控制关键句

为何保留：`still two steps from the open rear door` 保留了观察到的偏差。

为何保留：`Do not assume she is already at the door` 防止计划状态泄露。
