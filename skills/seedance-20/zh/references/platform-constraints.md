# 平台约束（Platform Constraints）

last_verified: 2026-05-30

## 稳定约束（Stable constraints）

- 不要假设每个 Seedance 2.0 平台都有相同的功能。
- 不要凭记忆假设 API 访问、定价、模型 ID、区域访问、上传限制、时长或肖像授权。
- 不要从上传的图像、声音或视频推断同意。
- 不要在没有安全改写或明确授权语境的情况下，提供受保护角色、名人、品牌标识、歌曲抄袭、精确场景或声音模仿的指令。
- 不要把真人面孔输入当作普遍允许或普遍禁止。一些平台限制直接上传人脸，同时允许经验证的虚拟肖像资产、可信的同账户生成资产或已授权材料。
- 不要混用供应商特定的字段名：Volcengine 的首/尾帧角色、Runway 的 `promptImage` 位置和 wrapper schema 不可互换。

## 平台特定声明（Surface-specific claims）

当用户问及 Dreamina、即梦（Jimeng）、Volcengine Ark、BytePlus ModelArk、Runway、ComfyUI、Replicate、Higgsfield 或其他平台时，用平台名和日期作答。清晰标注非官方/社区工具。

## 面向用户的默认表述（User-facing default）

平台支持因平台而异。在生产规划前查阅当前官方文档。
