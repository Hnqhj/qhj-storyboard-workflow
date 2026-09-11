# 序列方案：机场抵达

## 项目摘要

旅客走出机场，穿过雨水和人群的压力，抵达一辆等候的黑色轿车。完整的故事只有在轿车载着旅客驶离车流时才得到解决。

## 故事脊线

初始条件：航站楼出口和人群压力。
目标：抵达等候的车。
升级：雨、人群和距离拖慢了接近过程。
最终结局：旅客在轿车内，车辆离开。

## 序列图

Clip 01：走出航站楼并接近敞开的后车门。计划端点本是在敞开车门旁。被接受的观察端点是距门两步。

Clip 02：从两步外开始，完成接近，进入车内，关上车门。不要重播航站楼出口。不要展示车辆离开。

Clip 03：车辆驶离路缘并消失在车流中。在 Clip 02 被接受之前，此条保持临时性。

## 项目状态胶囊

PROJECT ID: seq_airport_arrival
STORY GOAL: traveler reaches waiting car and escapes airport crowd
FINAL OUTCOME: black sedan leaves traffic with traveler inside
SURFACE: unknown conservative generic profile
REFERENCE TAGS: @Image 1, [Video 1]
CANONICAL REFERENCES: @Image 1 controls traveler identity and wardrobe
ACCEPTED CLIPS: clip_01 accepted_with_deviation
CURRENT ACTUAL STATE: traveler is two steps from the open rear car door
OPEN MOTION: traveler and camera continue left-to-right
COMPLETED BEATS: terminal exit
NEXT CLIP JOB: finish approach, enter car, close door
CONTINUITY LOCKS: identity, wardrobe, travel direction, sedan, curbside environment
ALLOWED CHANGES: traveler may enter rear seat and close door
RESERVED FUTURE BEATS: vehicle departure
EXTENSION DEPTH: 1
UNRESOLVED UNCERTAINTIES: exact active surface limits
