---
name: director-skill-console-routing-dimension
description: 在 director-skill-console（G:\工作\vibecoding\director-skill-console）里新增、修改或重命名一个路由维度（如 processing_depth 深度轴、content_mode 题材轴、prompt_description_complexity、任务路由 route）。当用户说「给控制台加一个维度」「改路由档位」「新增题材/深度档」「把 fast/standard/full 改名」，或要动 src/orchestration.js 的 buildExecutionPlan / selectProcessingDepth / 状态 schema / routing-contract.json / mcp/server.js 工具描述时使用。也适用于改完技能文档后同步到 ~/.codex/skills 的场景。
agent_created: true
---

# 给 director-skill-console 增改路由维度

这个控制台的维度是**契约枚举**，不是显示名。漏改任何一层都会被 P0 校验拦下，
或者更糟——**校验通过但行为不对**（回执复用、界面显示旧值、模型不知道有这个参数）。

## 先判断：改的是哪一层

| 想做的事 | 改哪里 | 风险 |
|---|---|---|
| 只改用户看到的中文 | `PROMPT_DEPTH_LABELS` 等显示常量 | 零风险，改 1 处 |
| 新增一个正交维度 | 下面 10 个集成点全都要改 | 中 |
| 改现有枚举值本身 | 10 个集成点 + 所有技能文档 + 全部字面量 | **高，通常不该做** |

**改枚举值前先量改动面**：
```bash
grep -rc "\bfast\b" --include=*.js --include=*.json --include=*.mjs src config integrations
```
`fast/standard/full` 会命中 6 个文件 40+ 处，外加技能库 3 个文档。
如果只是想换中文说法，**只改显示标签**。

## 10 个集成点（漏一个就出事）

### 代码层（8 处）

1. **`src/orchestration.js`** —— 维度常量 + 解析函数；`selectProcessingDepth()` 和
   `buildExecutionPlan()` **开头先做入参归一化**；plan 返回新字段；`readPromptSettings()`
   从 task-context 读；`preparePromptCompilation()` 透传；编译回执 + `generationSettings`
   记录；`module.exports` 导出。
2. **`config/orchestration-state.schema.json`** —— ⚠️ **三处 `additionalProperties:false`
   都要登记**：`TaskEnvelope`、`ExecutionPlan`、`PromptCompilationReceipt`。
   漏了 `ExecutionPlan` 直接吃 `SCHEMA-001` P0。
3. **`config/routing-contract.json`** —— `rules.<维度名>` 定义 default / selectionOwner / 取值。
4. **`src/audit.js`** —— 新增契约完整性检查，否则契约缺字段没人发现。
5. **`lib/task-context-store.mjs`** —— ⚠️ **`TASK_PROMPT_SETTING_KEYS` 是落盘字段的唯一事实来源**。
   新维度加进这个数组，然后：
   - `updateTaskPromptDepth()` 里的 `settings` 对象补一行（写入方按 `TASK_PROMPT_SETTING_KEYS` 循环落盘，
     `settings` 里没有的键会被 `delete`）；
   - 读取方用 `projectTaskPromptSettings(value)` 投影，**不要在别的文件再手写一份字段白名单**。
   - 另需 `TASK_*_VALUES` 常量做取值校验。
6. **`integrations/injector-skill-console.mjs`** —— `handlePromptDepthBinding()` 接收并转发。
7. **`integrations/conversation-preview.user.js`** —— 显示常量、菜单分段、状态栏格、
   storage 读写（含旧值回落）、`setPromptDepth()`、绑定载荷。
8. **`mcp/server.js`** —— ⚠️ **工具描述是模型唯一能看到的入口说明**。
   契约实现了但描述里没写，模型根本不会传这个参数，**功能等于没上**。
   四个 `skill_console_prompt_*` / `_compile_prompt` 的描述都要提到新维度；
   传参入口（`_prompt_compilation_context`）还要写明**字段名与合法取值**，
   以及「只注入信号、永不设或降另一个维度」这条约束。

### 交叉层（2 处，最容易漏）

9. **回执过期判定** —— `promptCompilationStatus()` 的 reasons 数组
   **和** `validateState()` 里的 `PROMPT-010`，两处都要把新维度纳入比对。
   漏了会怎样：改了维度但旧编译结果仍被判有效 → **复用不匹配的提示词**。
   旧回执没有该字段时要给默认值（如 `(receipt.content_mode || 'mixed')`），
   否则历史回执会被一律判过期。
10. **模型可见的文档** —— 契约改了但技能不知道 = **实际不生效**。
    `script-camera-group-router`（选择责任方）、`director-workflow-70/references/adaptive-depth-routing.md`、
    `director-workflow-70/references/orchestration-contract.md`、
    `ai-video-production-governance/SKILL.md`、`G:\工作\skills\工作流总览.md`。

> 曾经漏过的第 11 处：`lib/preview-data.mjs` 的 `readTaskContext` 是**手写字段白名单**，
> 新维度漏掉后界面**静默**显示旧值、且没有测试会失败。现已改为从 `TASK_PROMPT_SETTING_KEYS`
> 派生，**不要再往那里加字面量字段名**。

## 设计原则：新维度要正交，不要混轴

「对话 / 标准 / 打斗」这种提案是**把题材轴和深度轴混在一起**——对话、打斗回答"拍什么"，
标准回答"做多深"，并列后无法表达"打斗+快速"。

正确做法：新维度**只向既有信号判定注入信号**，不直接指定另一个维度的值，也永不降低它。
默认值要设计成**不注入任何东西**，这样才是向后兼容的。
例：`content_mode` 的 `mixed` 展开为空；`action` 展开为 `{fight: true}`，
`dialogue` 展开为 `{dialogue_intensive, emotion_required, performance_required}`。
解析函数必须**幂等**（只填空值，不覆盖显式给出的信号），因为会被调用两次。

## 验证顺序（照这个跑）

```bash
cd G:/工作/vibecoding/director-skill-console
N=C:/Users/Administrator/.workbuddy/binaries/node/versions/22.22.2-3/node.exe

# 1. 语法
for f in src/orchestration.js src/audit.js lib/task-context-store.mjs lib/preview-data.mjs \
         mcp/server.js integrations/injector-skill-console.mjs integrations/conversation-preview.user.js; do
  "$N" --check "$f"; done

# 2. 单测（当前 65 项）
"$N" --test 2>&1 | tail -8

# 3. 契约审计（0 critical / 0 warning；输出键是 counts，不是 summary）
"$N" src/cli.js audit | "$N" -e "let s='';process.stdin.on('data',d=>s+=d).on('end',()=>console.log(JSON.stringify(JSON.parse(s).counts)))"

# 4. 端到端：每个新维度的取值都跑一次
"$N" src/cli.js route-plan <features.json>
```

再补一组自写功能测试，必须覆盖：**向后兼容**（不传新字段 == 默认值）、
**幂等**、**显式信号优先**、**不降深度**、**schema 无 SCHEMA-001**。
写测试时注意：往 task-context 文件写回时用 `{...JSON.parse(读出的内容)}`，
**别用 `{...自己构造的 base}`**——那会把已落盘的 `prompt_compilation_receipt` 一起抹掉，
测试会判成 `uncompiled` 而不是 `stale`。

### 防「白名单漂移」的结构性测试

新增落盘字段时，加一条测试断言**写入方与读取方共用同一份清单**，例如：
```js
const projected = store.projectTaskPromptSettings(written);
assert.deepEqual(Object.keys(projected).sort(), [...store.TASK_PROMPT_SETTING_KEYS].sort());
// 并且禁止读取方回退到手写字面量
for (const key of keys) assert.equal(source.includes(`${key}: value.`), false);
```
模型可见面同理：spawn MCP server 发 `tools/list`，断言描述里出现新维度的关键词
（`assert.match(description, /genre/i)`）。**关键词测试虽弱，但能挡住"功能上了、描述没上"这个真实发生过的失败。**

## 改完技能文档必须同步

仓库是唯一事实来源，但技能要装到宿主的安装目录才生效。本机有**两个活跃宿主**：

| 宿主 | 安装目录 | 状态 |
|---|---|---|
| WorkBuddy | `%USERPROFILE%\.workbuddy\skills` | 活跃（App `D:\workbuddy`，5.5.6） |
| Codex | `%USERPROFILE%\.codex\skills` | 活跃 |

> ⚠️ **`.workbuddy-ai`（App `D:\workbuddyai`）已冻结**：只用于 vibecoding，**不是同步目标**，
> 也不再生成提示词。本技能早期版本把 `-ai` 写成活跃目录，**写反了**，不要沿用。
> 允许名单单点在仓库根 **`sync-hosts.json#workbuddyAllow`**，`install.ps1` /
> `sync-skills.mjs` / `sync-expert.mjs` 都读它。

```powershell
& "G:\工作\skills\install.ps1"                            # Codex
& "G:\工作\skills\install.ps1" -Target workbuddy          # WorkBuddy 用户级
& "G:\工作\skills\install.ps1" -Target all                # 两个活跃宿主
& "G:\工作\skills\install.ps1" -Target all -Prune -WhatIf      # dry run：列出会删什么
& "G:\工作\skills\install.ps1" -Target all -Prune -Confirm:$false  # 清理孤儿技能
```

日常改动**不用跑 install**：`PostToolUse` hook 自动增量同步；
手动全量校验用 `node .workbuddy-ai/tools/sync-skills.mjs --all`（约 3.5s）。

`-Prune` 四重保护：只处理含 `SKILL.md` 的目录、跳过点开头目录（`.system` 安全）、
**带 `agent_created: true` 的技能视为代理自建、不归仓库管、只报不删**、
`$dest == $here` 时拒绝。`ConfirmImpact = High`，不加 `-Confirm:$false` 会逐个确认。

同步后核对：
```bash
cmp <仓库文件> <安装目录文件>          # 逐文件字节一致
comm -3 <(安装目录技能名) <(仓库技能名) # 集合无漂移
```
`install.ps1` 默认**不删除**，所以安装目录里的孤儿技能会残留——用 `-Prune` 清。
当前规模：仓库 **83 个顶层技能**（拆分镜 40 / 生图 20 / 全流程 12 / 其他 10）
+ 28 个 seedance-20 子技能 = **111 个 SKILL.md**；两个活跃宿主均 **83/83 顶层逐字节一致**。
宿主独有的 `agent_created` 技能（当前 6 个）属漂移，`-Prune` **只报不删**。
`seedance-20/skills/` 下 28 个子技能**随父目录一起安装**，不平铺，这是有意的。

### 控制台 MCP 已移除 —— 一律走 CLI

链里 5 个技能曾调 `skill_console_*` MCP 工具，**2026-09-23 起已全部改走控制台 CLI**：

```bash
node "G:/工作/vibecoding/director-skill-console/src/cli.js" <子命令>
# prompt-context / prompt-compile / prompt-preflight / prompt-status
# 固定 --thread workbuddy-fenjing --cwd "G:\工作\分镜"，根目录可用 $SKILL_CONSOLE_ROOT 覆盖
```

- WorkBuddy 侧 `~/.workbuddy/mcp.json` 的 `mcpServers` **为空**、`mcp-approvals.json` 为 `{}`；
  Codex 侧 `~/.codex/config.toml` 的 `[mcp_servers.director_skill_console]` **刻意保留**。
- ⚠️ 「有信任记录 ≠ 已连接」：判定只认会话日志 `grep -a "getConnectedServers() returning" ~/.workbuddy/logs/<日期>/<会话>.log | tail -3`。
- `prompt-compile` 会回写回执，冒烟测试必须用一次性 thread id。
- 提示词常超 1 万字符，必须走 `--prompt-file` / `-` stdin。

## 环境坑

- ⚠️ **同一条消息里对同一文件发多个 `Edit` 会互相覆盖**：只有一个能落盘，其余**静默丢失**
  （编辑工具仍报"成功"）。同一文件的多处修改**必须串行、一次一个 Edit**，改完 `grep` 复验。
  实测在 `preview-data.mjs` 的 import 行和 `mcp/server.js` 的描述行各中招一次。
- ⚠️ **PowerShell 变量名不区分大小写**：脚本里写 `$target = $t.Root` 会撞上 `[ValidateSet]`
  的参数 `$Target`，赋值时直接触发校验失败（报错是「值 ... 不是变量 Target 的有效值」，很误导）。
  用 `$dest` 之类的名字。同理，别用 `$targets = switch (...) { @{...} }` 收集哈希表——
  单元素时 PowerShell 会退化成哈希表本身，`foreach` 会去枚举 `DictionaryEntry`。
  用显式 `ArrayList` + `if` 累加。
- **PowerShell 5.1 按 ANSI 读无 BOM 的 .ps1**：含中文的 .ps1 用写文件工具生成后必须补 BOM，
  否则中文变「宸ヤ綔」直接语法错。**临时脚本（含中文路径）同样需要 BOM**，
  否则 `& $path` 静默打空、什么都不发生，还不报错。补法：
  `$c = Get-Content -LiteralPath $p -Raw -Encoding UTF8; Set-Content -LiteralPath $p -Value $c -Encoding UTF8 -NoNewline`
  验证首 3 字节 = `EF BB BF`。
- 从 Bash 调 PowerShell 会被拦；要用 PowerShell 工具，且它**不回显 stdout**，得写文件再读。
  写 `G:\工作\分镜` 下的路径有时不落盘，**临时产物一律走 `$env:TEMP`**。
- Bash 里 `/tmp/x.json` 会被解析成 `G:\tmp\x.json`（Git Bash 盘符映射），临时文件放工作区。
- 比对文件差异用 `diff --strip-trailing-cr`，否则 CRLF/LF 差异会伪装成内容冲突。
- 审计输出是 JSON，顶层键是 `generatedAt` / `counts` / `findings`（**不是 `summary` / `issues`**）。
