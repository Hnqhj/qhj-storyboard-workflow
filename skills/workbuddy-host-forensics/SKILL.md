---
name: workbuddy-host-forensics
agent_created: true
description: WorkBuddy 宿主机制取证：反查技能目录、扫描顺序、开关、MCP 与 hooks、多宿主同步漏目标。触发：技能没生效、同步没同步过去、另一个 App 还是旧版、项目级技能、MCP 没连上、hook 不触发、description 被截断。 Determine WorkBuddy host behavior (skill dirs, scan order, product flags, MCP lifecycle, hooks, multi-host sync targets) from app.asar and product.json instead of guessing.
---

# WorkBuddy 宿主机制取证

当 WorkBuddy 的行为与预期不符（技能不加载、被截断、MCP 连不上、项目级不生效），
**不要靠猜也不要靠文档**——宿主是 Electron 应用，机制全在 `app.asar` 里，可直接取证。

## 〇、宿主身份（先确认在查哪一个）

> **⚠️ 本机现状（2026-09-23 起）：只保留一个 WorkBuddy 宿主 —— `D:\workbuddy` → `~/.workbuddy`。**
> 旧宿主 `~/.workbuddy-ai`（`D:\workbuddyai`）**已冻结**，不再是同步目标；
> 同步允许名单单点在技能仓库根 `sync-hosts.json#workbuddyAllow`
> （`install.ps1` / `sync-skills.mjs` / `sync-expert.mjs` 都读它）。
> **下面这张表仍要保留** —— 多宿主并存在别的机器/别的时期照样会出现，
> 取证方法（定位 dataFolderName、确认当前进程归属）不随本机现状改变。

| App | 程序目录 | 数据目录 | `dataFolderName` | 用户级技能目录 |
|---|---|---|---|---|
| WorkBuddy AI（本机已冻结） | `D:\workbuddyai` | `~/.workbuddy-ai` | `.workbuddy-ai` | `~/.workbuddy-ai/skills` |
| WorkBuddy（本机在用的这个） | `D:\workbuddy` | `~/.workbuddy` | `.workbuddy` | `~/.workbuddy/skills` |

多宿主并存时两套**资产不互通**：技能、插件（含专家包）、task-context、
**`settings.json`（含 hooks / MCP / 插件开关）**各自独立，工作区里也会并排出现
`.workbuddy/` 与 `.workbuddy-ai/` 两份，**两个 App 可能同时在跑**。
**一旦确定只留一个宿主，就该把允许名单收窄到单点配置**，而不是靠"记得两边都同步"。

先确认当前会话归属，再决定去哪个目录取证：

```bash
echo "[$WORKBUDDY_CONFIG_DIR] [$WORKBUDDY_DATA_FOLDER_NAME] [$WORKBUDDY_APP_PATH]"
ls -d /c/Users/Administrator/.workbuddy*
tasklist | grep -i workbuddy      # 两个 App 可能同时在跑
```

> ⚠️ **本技能最容易踩的前提**：任何「安装 / 同步 / 改配置」的动作，
> 只要目标是「由 `WORKBUDDY_CONFIG_DIR` 决定的那一个目录」，就**只覆盖当前这一个 App**，
> 另一个会静默停在旧状态且**没有任何报错**。详见第十节。

## 一、先定位两个文件

```
<程序目录>\resources\app.asar                                  ← 主程序（含全部机制代码）
<程序目录>\resources\app.asar.unpacked\cli\product.json        ← 产品配置（决定目录名与开关）
```

`app.asar` 是二进制包，但内含明文 JS，**用 `grep -a` 或 Python 按文本读即可**，无需解包工具。

## 二、第一条永远先查 product.json

很多「机制」其实是配置。`product.json` 里最关键的几项：

| 键 | 作用 |
|---|---|
| `dataFolderName` | **项目级数据目录名，随构建而变** —— `D:\workbuddyai` 是 `.workbuddy-ai`、`D:\workbuddy` 是 `.workbuddy`。**不要按单个 App 的值写死进脚本**（`install.ps1` 的 `-ProjectDataFolder` 已因此改为自动推导） |
| `isOversea` | 海外版标志，会影响 config 目录名 |
| `customUserDataDir` | 用户数据目录名 |
| `productFeatures.SkillManage` | `false` = SkillManage 工具被关闭 |
| `productFeatures.DisableMultimodalGeneration` | `true` = 无图像/视频生成 |
| `disabledBuiltinSkills` | 被下线的内置技能目录名清单 |

```bash
cat "D:/workbuddyai/resources/app.asar.unpacked/cli/product.json" | head -c 4000
```

## 三、查「项目级技能目录到底叫什么」

这是最容易搞错的一点，因为它**不是硬编码**：

```js
const projectFolder = process.env.WORKBUDDY_DATA_FOLDER_NAME?.trim() || ".workbuddy";
await scanSkillsDirectory(node_path.join(params.cwd, projectFolder, "skills"), "project", ...);
```

而环境变量来自 product.json：

```js
process.env.WORKBUDDY_DATA_FOLDER_NAME = require_workbuddy_paths._internalGetDefaultConfigDirname();
// resolveDataFolderName(): productConfig?.["dataFolderName"] || ".workbuddy"
```

**所以项目级技能目录 = `<项目根>/<product.json#dataFolderName>/skills`。**
本机实测：旧构建 = `G:\工作\分镜\.workbuddy-ai\skills`；新构建 = `G:\工作\分镜\.workbuddy\skills`。

⚠️ 同一份 asar 里可能有**两套**扫描实现且目录名不一致（本机实测：
`[SkillsService]` 用 `WORKBUDDY_DATA_FOLDER_NAME`，`[SkillsDomainService]` 硬编码 `.workbuddy`）。
**以 `WORKBUDDY_DATA_FOLDER_NAME` 那套为准**，并留意注释里写的官方意图。

## 四、查「扫描顺序与去重」

```bash
grep -ao '.\{0,300\}scanSkillsDirectory[^$].\{0,500\}' app.asar | sort -u
```

本机实测顺序（`[SkillsService].getSkillList()`）：

```
1. <cwd>/<dataFolderName>/skills   source=project   ← 先扫，重名胜出
2. <configDir>/skills              source=user
3. <buddySkillsDir>                source=user      （行业模式）
4. builtinSkillsDir                source=builtin   （受 disabledBuiltinSkills 过滤）
5. <configDir>/connectors/skills   source=connector
6. 已启用插件的 skills/            source=plugin
```

**去重是按技能 `name`（不是路径）**：

```js
if (loadedNames && loadedNames.has(skill.name)) continue;
```

→ 同名技能**不会重复出现**；项目级先扫，所以**项目副本静默覆盖用户副本**。
→ 后果：只同步用户级、不同步项目级，项目会继续用旧副本（静默失效）。

## 五、查「MCP 到底连没连上」

**看会话日志，不要看 `mcp-approvals.json`**——有信任记录 ≠ 已连接。

```bash
cd "C:/Users/Administrator/.workbuddy-ai/logs/$(date +%Y-%m-%d)"
grep -a "getConnectedServers() returning" <会话日志>.log | tail -3
grep -a "serverManager.delete" <会话日志>.log          # 被剔除的服务器
grep -a "buildMcpServers" <会话日志>.log | tail -3      # 曾经连上过的
```

日志文件名形如 `skills__<hash>.log`（按工作区名）或 `<项目名>__<hash>.log`。

典型故障形态：先 `connected servers=[...,skill-console] (count=4)`，
随后 `config scope=dynamic changed` → `serverManager.delete("skill-console")`
→ `projected (retained=3, evicted=1)`。

**可疑根因**：磁盘 `mcp.json` 里的 server 形态（含 `env`、`disabled`）与桌面推给 CLI 的
`--mcp-config` 形态（常只有 `command/args/timeout`）不一致，导致信任哈希对不上。

### MCP 连不稳时的替代判断法（2026-09-23 实证）

不要死磕 MCP。先问一句：**这个 MCP 是不是只是个传输薄壳？**

1. 打开它的 `server.js`。如果里面只有 JSON-RPC 的 `tools/list` / `tools/call` 分发，
   每个 tool 的 handler 都是一行 `(args) => someFunction(args)`——
   **那真逻辑全在被 require 的模块里，跟 MCP 无关。**
2. 去那个模块看导出。如果是**纯函数**（入参出参都是普通对象，不依赖 MCP 上下文），
   就可以直接在 CLI / 脚本里调，**彻底绕开 MCP 传输层、信任哈希与 reconcile 剔除**。
3. 落地方式：给该项目的 CLI 加几个子命令包一层即可（实测约 100 行）。

本例：`director-skill-console` 的 MCP 只是 `src/orchestration.js` 的薄壳，
加了 4 个子命令（`prompt-context` / `prompt-preflight` / `prompt-status` / `prompt-compile`）。

⚠️ **但迁移并未做完（2026-09-23 复核）**：技能里**仍残留 11 处 `skill_console_*` 工具名**——
`script-camera-group-router` 5 处、`narrative-camera-groups` 2 处、`seedance-20` 1 处、
`seedance-camera-group-compiler-fast` 1 处、`jimeng-sd2-prompting` 1 处、镜语专家 md 2 处。
router 里甚至在 CLI 映射表**旁边**还写着 MCP 工具名。
→ **用这些技能前先确认它引用的工具是否真实存在**，别默认"已改完"。

⚠️ 两个必须注意的点：
- **长文本参数不要走命令行**（Windows 上限约 8k）。用 `--xxx-file <路径>` 或 `-` 读 stdin。
- **注意副作用**：本例 `prompt-compile` 会回写回执文件，
  冒烟测试必须用一次性的 id，否则污染真实数据。

## 六、查「技能清单实际长什么样」

系统提示里注入的清单不在会话 jsonl 的正文里，别去正文里 grep 字面量（会命中讨论内容）。
**最可靠的是会话日志里的 `SkillExtensionLoader` 行**：

```bash
grep -a "SkillExtensionLoader\|PluginLoaderManager" <会话日志>.log | head -20
```

它只覆盖插件技能；用户级/项目级核心技能不逐条打日志。

## 七、查「Hooks 机制」（不在 app.asar 里！）

**关键事实：hooks 由 agent 侧 CLI 执行，不在桌面主进程。**
在 `app.asar` 里 grep `PostToolUse` 会得到 **0 次命中**——别据此判断「不支持 hooks」。
真身在：

```
D:\workbuddyai\resources\app.asar.unpacked\cli\dist\codebuddy.js   ← 约 23MB
```

```bash
grep -ao 'PreToolUse\|PostToolUse\|PostToolUseFailure\|UserPromptSubmit\|SessionStart\|SessionEnd\|SubagentStart\|SubagentStop\|PreCompact\|PostCompact\|StopFailure\|Notification\|ConfigChange\|InstructionsLoaded\|PermissionRequest\|PermissionDenied\|Elicitation\|WorktreeCreate\|WorktreeRemove' \
  "D:/workbuddyai/resources/app.asar.unpacked/cli/dist/codebuddy.js" | sort -u
```

事件全集（20 个）：`PreToolUse`、`PostToolUse`、`PostToolUseFailure`、`UserPromptSubmit`、
`SessionStart`、`SessionEnd`、`SubagentStart`、`SubagentStop`、`PreCompact`、`PostCompact`、
`Stop`、`StopFailure`、`Notification`、`ConfigChange`、`InstructionsLoaded`、
`PermissionRequest`、`PermissionDenied`、`Elicitation`、`WorktreeCreate`、`WorktreeRemove`。

**配置形状**（写在 settings 文件的顶层 `hooks` 键）：

```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "Edit|Write|MultiEdit|NotebookEdit",
        "hooks": [{ "type": "command", "command": "node \"<绝对路径>.mjs\"", "timeout": 60 }] }
    ]
  }
}
```

- **`matcher` 是正则**，只对**工具名**做 `new RegExp(matcher).test(toolName)`。
  不要写路径模式，它匹配不到。
- 命令**从 stdin 收到 JSON**，字段含 `session_id` / `transcript_path` / `cwd` /
  `hook_event_name` / `tool_name` / `tool_input` / `tool_response` / `call_id` / `tool_use_id`。
- **hook 脚本硬契约**：① **绝不往 stdout 写内容**（stdout 会被当 `additionalContext`
  注入，污染上下文）；② **永远 `exit 0`**（hook 失败不得阻断 agent）。
- settings 作用域：`USER` / `PROJECT` / `PROJECT_LOCAL` / `CLI`；
  文件 `settings.json` 与 `settings.local.json`；目录 `WORKBUDDY_CONFIG_DIR || ~/.workbuddy`。
  **本机有两份**：`~/.workbuddy/settings.json`（App `D:\workbuddy`）与
  `~/.workbuddy-ai/settings.json`（App `D:\workbuddyai`）——
  **改了一份不代表另一份也改了**，排查「hook 不触发」时两份都要看。
- ✅ **hook 配置是随取随读的，不需要重启 App。**
  2026-09-23 实测：`~/.workbuddy/settings.json` 是在该 App 启动（11:21:46）**之后**
  才补上 `hooks` 键的（11:34），而**同一进程内** 11:37 的 `Write` 就已经触发了同步。
  → 此前「必须开新会话才生效」的说法**是错的**，不要再据此排除故障。
  唯一可靠的判定办法：**让 hook 自己写日志文件，再去查那行日志**。

## 八、查「同一份资产被复制成了几份」（多副本一致性审计）

本机资产会同时出现在**最多 5 个位置**，且**没有任何自动校验**：

| 位置 | 说明 |
|---|---|
| 内容层源 `G:\工作\skills` | 唯一编辑源（**只覆盖技能，不含专家包**） |
| 新宿主 `~/.workbuddy/skills` | 由 `install.ps1` / sync hook 镜像 |
| 旧宿主 `~/.workbuddy-ai/skills` | 同上 |
| 工作区级 `<项目>/.workbuddy{,-ai}/` | 项目副本，**加载时胜出、静默覆盖用户级** |
| `~/plugins/{marketplaces,cache}/` | 专家包 —— **无源、靠手工 cp** |

一次完整审计的最小检查集：

```bash
# 1) 名单差集：源 vs 两宿主
ls -d /g/工作/skills/prompt/*/*/ | xargs -n1 basename | sort -u > /tmp/src.txt
ls -d ~/.workbuddy/skills/*/     | xargs -n1 basename | sort -u > /tmp/new.txt
comm -23 /tmp/src.txt /tmp/new.txt   # 源有、宿主没有 = 同步漏了
comm -13 /tmp/src.txt /tmp/new.txt   # 宿主有、源没有 → 先判「漂移 vs 外来资产」，见 §十一

# 2) 内容漂移：逐技能 diff，不是只看名单
for d in ~/.workbuddy-ai/skills/*/; do
  n=$(basename "$d")
  diff -q "$d/SKILL.md" ~/.workbuddy/skills/$n/SKILL.md >/dev/null 2>&1 || echo "漂移: $n"
done

# 3) 专家包：市场源 vs 缓存 必须字节一致
```

**已知易漏的三处**（2026-09-23 实测）：
- 专家包**不在**任何编辑源或同步脚本的覆盖范围内 —— 重装/迁移即丢失；
- 缓存**版本目录名**可能与 `plugin.json` 的 `version` 不一致（目录名不会自动跟着改）；
- 工作区级两份 `.workbuddy{,-ai}/memory/` 会各自漂移 —— **双写而无同步 = 记忆污染源**。
  `G:\工作\skills` 已用**目录联接** `.workbuddy → .workbuddy-ai` 把两边统一
  （`New-Item -ItemType Junction -Path <link> -Target <target>`），实测双向可见。
  ⚠️ 联接**不是副本**：`rm -rf` 链接路径会连带删掉目标目录的真实内容；
  拆除请只删链接本身：`(Get-Item <link> -Force).Delete()`。

⚠️ 审计前先看 `ls -la --time-style=long-iso` 的**修改时间**：
若有文件在**本次操作前几分钟**刚被写入，说明**有另一个会话在动同一批文件**，
此时任何改动都可能被对方覆盖 —— 先确认对方是否收工。

## 九、判定纪律（重要）

- **源码证据 > 文档 > 推测**。每条结论都要能指到 asar 里的具体字符串。
- 会话级注入（技能清单、工具清单）**在本会话内不会刷新**，
  改完必须**开新会话**才能观察效果。
- 同一功能存在两套实现时，**不要假定哪套生效**，标为待验证并给出可验证的下一步。
- 关键环境变量实测：
  ```bash
  echo "[$WORKBUDDY_CONFIG_DIR] [$WORKBUDDY_DATA_FOLDER_NAME] [$WORKBUDDY_APP_PATH]"
  env | grep -i workbuddy
  ```
  （2026-09-23 实测：在 Bash 工具里这三个变量**都有值**，足以判定当前会话属于哪个 App。
  若某处为空，不要据此推断默认值，回落到 `product.json#dataFolderName`。）
- **判断「宿主技能数对不对」时不要用相等比较**：各宿主的 `SKILL.md` 计数口径不同，
  差异来自「漂移技能」与 Codex 自带的 `.system/`。要对齐的是**同名技能的内容**，
  不是总数。2026-09-23 实测（把 9 个漂移技能入库后）：

  | 位置 | 顶层 | SKILL.md 计数 |
  |---|---|---|
  | 仓库 `G:\工作\skills` | 92 | 120（92 + 28 嵌套） |
  | `~/.workbuddy/skills` | 92 | 120 |
  | `~/.codex/skills` | 92 | 126（120 + 6 自带 `.system/`） |
  | `~/.workbuddy-ai/skills` | 89 | 117（**已冻结**，不必对齐） |

  一句话判据：`顶层技能数` 应当相等（当前 92/92），**漂移数应当为 0** —— 见 §十一。

## 十、查「同步/安装的目标宿主是否漏了」（2026-09-23 实证，P0 级）

**症状**：改完技能，宿主里却是旧版本；或者「明明同步了，另一个 App 还是旧的」；
或更糟 —— **完全没有任何报错**，`sync.log` 也在正常增长。

**根因模式（值得记牢）**：同步/安装脚本用**环境变量**选目标，

```js
const wbRoot = process.env.WORKBUDDY_CONFIG_DIR?.trim() || ~/.workbuddy-ai;
```

而该变量由**当前进程所属的那个 App** 注入，只指向它自己。于是：

| 在哪个 App 里编辑 | 实际被更新 | 被静默落下的 |
|---|---|---|
| `D:\workbuddy` | `.workbuddy` + `.codex` | **`.workbuddy-ai`** |
| `D:\workbuddyai` | `.workbuddy-ai` + `.codex` | **`.workbuddy`** |

**两个 App 都在用时，谁没在运行谁就永远陈旧。**

**指纹（怎么快速判断中没中）**：

```bash
# 1) 同步器的 manifest 里如果出现多个目标根，而当前代码只解析一个 → 就是它
node -e "const m=require('<tools>/.sync-manifest.json');const s=new Set(Object.keys(m).map(k=>k.split('::')[0]));console.log([...s].join('\n'))"

# 2) hook 日志的 writes 数应等于宿主数
#    本机应写 3 个宿主 → writes=3；若只有 writes=2，说明漏了一个
tail -3 "<tools>/sync.log"
```

**正确写法：枚举全部宿主，而不是取「当前那一个」。**

```js
// 扫 HOME 下所有 .workbuddy / .workbuddy-*，要求像数据目录（有 settings.json 或 skills/）
// 再并上 CODEX_HOME || ~/.codex
// 名字 = 数据目录去掉前导点：.workbuddy -> workbuddy、.workbuddy-ai -> workbuddy-ai
```

注意那个「像数据目录」的判据是必要的：本机还有 `.workbuddy-key-fallback` 这类
**同前缀但非数据目录**的兄弟目录，只按前缀匹配会把它误当宿主。

**顺带一条**：支撑同步的脚本本身要在版本控制里。若它们住在被 `.gitignore`
整目录忽略的 `.workbuddy-ai/` 下，就等于**没有任何副本**，该目录一被清理，
hook 会指向一个不存在的脚本 —— 表现是「改完毫无反应、日志也不再增长」的静默失效。
可用 `.gitignore` 的 `目录/*` + `!目录/子目录/` 例外把脚本单独纳入。

## 十一、查「宿主里有没有仓库不认识的技能」（漂移审计，2026-09-23 实证）

**先分清两种「宿主有、源没有」** —— 处置完全相反：

| 类型 | 判据 | 处置 |
|---|---|---|
| **漂移**（该入库没入库） | frontmatter 有 `agent_created: true` | **入库**（本节流程） |
| **外来资产** | 无该字段，或属别人发的插件 / 内置技能 | 不动，勿删 |

`agent_created: true` 是模型自建标记 —— 说明它本来就是这个仓库的产出，
只是**建错了地方**（在宿主目录里直接建，没回到编辑源）。

**为什么必须入库**：宿主的 `skills/` 是**镜像，不是源**。留在那里的技能
应用重装/迁移即丢；不进版本控制；不享受双宿主同步；而且会在另一宿主永久缺失。

**一条命令查漂移**（本仓库常驻脚本）：

```bash
node .workbuddy-ai/tools/skill-health.mjs --hosts
# 输出末尾的「宿主对照」段：
#   workbuddy: 仓库 92 / 宿主 92  缺 0 多 0 描述不一致 0
#                                ↑「多」= 漂移数   ↑「缺」= 同步漏了
#                                  「描述不一致」= hook 没跑到
```

不看脚本时的等价手动查法：

```bash
comm -13 <(ls -d /g/工作/skills/*/*/ /g/工作/skills/其他/*/ | xargs -n1 basename | sort -u) \
         <(ls -d ~/.workbuddy/skills/*/ | xargs -n1 basename | sort -u)
```

**入库四步**（本轮实测流程）：

1. 确认目标分类不冲突：`ls "G:\工作\skills\其他"`（工具类技能统一放 `其他/`）
2. 整目录复制（**保留 `scripts/`、`references/` 等全部子文件**）：
   `cp -r ~/.workbuddy/skills/<name> "G:/工作/skills/其他/"`
3. 同步：`node .workbuddy-ai/tools/sync-skills.mjs --all`
4. 验证归零：`node .workbuddy-ai/tools/skill-health.mjs --hosts` → 两宿主「多 0 / 缺 0」

⚠️ **宿主里的原目录不要手工删** —— 同步器会按仓库内容覆盖它；
手工删反而可能删到仓库的内容（若存在目录联接）。
⚠️ 入库会让该技能**顺带出现在 `.codex`**（同步器的目标）。若某技能只对
WorkBuddy 有意义（如本技能自己），这是可接受的：技能是文档，在另一宿主里
不会被误触发，而「两边一致」这个性质更重要。

**这是持续漏洞，不是一次性问题**：本机漂移数实测
`6 个（2026-09-23 早）→ 9 个（同日晚）`，新增的三个
（`web-liquid-glass-refraction`、`web-visual-verify-headless`、`workbuddy-expert-package-source`）
都是同一个动作造成的 —— **在宿主里新建技能**。

**根因与对策**：模型在宿主目录里建技能，动因通常是"当前会话里最顺手的位置"。
正确做法只有一条 —— **新建技能时直接在 `G:\工作\skills` 里建**，
再推给宿主（方向不能反）：

```bash
# 正确：仓库建好 -> 推给宿主
mkdir -p "G:/工作/skills/其他/<new-skill>"   # 然后写 SKILL.md
node .workbuddy-ai/tools/sync-skills.mjs --all

# 错误：在宿主里建 -> 忘了回流  ==  第 10、11 个漂移
```

**定期体检**：用 automation 每天跑一次
`node .workbuddy-ai/tools/skill-health.mjs --hosts`，漂移一出现就报，
不要等攒到 9 个才发现。
