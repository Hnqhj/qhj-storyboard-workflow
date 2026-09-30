---
name: workbuddy-expert-package-source
agent_created: true
description: 给 WorkBuddy 自建专家包建"唯一编辑源"并打通同步。触发：专家改了不生效、专家包没有编辑源、重装专家就丢、marketplace 与 cache 不一致、要不要升版本号、自建专家进不了版本控制。 Give a WorkBuddy custom expert package a single edit source plus a mirror to the host's marketplace, cache, and installed_plugins.json.
---

# 自建专家包：唯一编辑源 + 同步

**适用**：用户在 `~/.workbuddy/plugins/marketplaces/<市场>/plugins/<专家>/` 下自建了专家包，
想把它纳入「仓库是唯一编辑源」的纪律（可版本控制、可复现、重装不丢）。

## 一、先搞清宿主怎么加载（这是所有坑的根）

三个位置，**作用完全不同**：

| 位置 | 作用 | 改了会生效吗 |
|---|---|---|
| `<宿主>/plugins/known_marketplaces.json` | 市场登记（source / installLocation） | 只是登记 |
| `<宿主>/plugins/marketplaces/<市场>/plugins/<专家>/` | **安装源**（清单 + 包体） | ❌ **不生效** |
| `<宿主>/plugins/cache/<市场>/<专家>/<版本>/` | **宿主实际加载的那一份** | ✅ 生效 |
| `<宿主>/plugins/installed_plugins.json` → `installPath` | 指向上面那个 cache 目录 | 决定加载哪份 |

> **最容易踩的坑**：只改 `marketplaces/` 下的源文件，专家行为毫无变化。
> 因为宿主按 `installed_plugins.json#installPath` 读 **cache**。
> 症状是「源文件明明改了，专家还是旧口径」——看起来像缓存没刷新，其实是改错了地方。

## 二、标准做法

1. **建编辑源**：在技能仓库放 marketplace 根，例如 `<repo>/plugins/`：
   ```
   <repo>/plugins/.codebuddy-plugin/marketplace.json
   <repo>/plugins/plugins/<专家>/.codebuddy-plugin/plugin.json
   <repo>/plugins/plugins/<专家>/agents/<专家>.md
   <repo>/plugins/plugins/<专家>/avatars/expert.png
   ```
2. **写同步器**（本机 `G:\工作\skills\.workbuddy-ai\tools\sync-expert.mjs`，可参照），一次刷三处：
   - 仓库 `plugins/` → `<宿主>/plugins/marketplaces/<市场>/`
   - 仓库插件目录 → `<宿主>/plugins/cache/<市场>/<专家>/<版本>/`
   - 更新 `<宿主>/plugins/installed_plugins.json` 的 `version` 与 `installPath`
   - 市场没登记过就补 `known_marketplaces.json`
3. **hook 分流**：编辑 `<repo>/plugins/**` 时走专家同步器，编辑技能文件时走技能同步器。
   ⚠️ 注意 `.codebuddy-plugin/` 是**隐藏目录**，通用的「跳过隐藏段」过滤会把
   `plugin.json` 的编辑**静默漏掉** —— 专家那条路径要允许隐藏段。
4. **校验/注册**（宿主内置脚本）：
   ```bash
   python <app>/resources/app.asar.unpacked/resources/plugins/workbuddy-builtin/skills/expert-manager/scripts/validate_expert.py <expert-dir>
   python .../register_expert.py <expert-dir>
   ```
5. 创建专家后**检查 `.created-by-session` 隐藏文件**是否落地（曾静默缺失）。

## 三、版本号：**不要为了"让改动生效"而升**

- 内容原地刷新 + cache 覆盖，就已生效（宿主每会话读 `installPath` 下文件）。
- **升版本会新建一个 cache 目录，旧的留在原地**；而本机非 Temp 路径的删除会被安全守卫拦下
  （`fs.rmSync` / `shutil.rmtree` / Bash `rm` 全拦），**升一次就多一份删不掉的旧副本**，
  反而制造新的「两个副本谁是活的」问题。
- **结论**：改内容 → 原地刷新；只有真正对外发布新版本时才升，并同步 `installed_plugins.json`。

## 四、验收（每次都跑）

```bash
# 1. 三份逐字节一致（源 / marketplace / cache）
diff --strip-trailing-cr <源> <marketplace> && diff --strip-trailing-cr <源> <cache>
# 2. 口径词命中（例：新词应有、旧词应为 0）
grep -c "<新说法>" <源>; grep -c "<旧说法>" <源>
# 3. 登记指向
grep -A4 "<专家>@<市场>" <宿主>/plugins/installed_plugins.json
```

## 五、边界

- 编辑源是**唯一可写处**；宿主侧两处一律视为镜像，不要手改。
- 专家包属**决策/引导层**，与「技能内容层只读」不冲突 —— 但改技能本体仍需另获授权。
