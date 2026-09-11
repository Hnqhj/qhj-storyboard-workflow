# 智能体兼容性

last_verified: 2026-06-12

在审查本仓库是否被正确塑造为一个 Agent Skill 包时，使用本文件。这关乎打包与智能体行为，而非 Seedance 模型能力。

## 当前的 Agent-Skill 形态

Codex 当前的 Agent Skills 文档把一个技能描述为：一个含有必需的 `ZH_REFERENCE.md` 文件，外加可选的 `scripts/`、`references/`、`assets/` 和 `agents/` 文件夹的目录。它还描述了渐进式披露：智能体先看到名称、描述和路径，然后仅在技能匹配任务时才加载完整的 `ZH_REFERENCE.md`。

本仓库遵循该模式：

| Agent-skill 期望 | 仓库位置 | 状态 |
|---|---|---|
| 根技能元数据与路由 | `ZH_REFERENCE.md` | 存在 |
| 任务特定的子技能 | `skills/*/ZH_REFERENCE.md` | 存在 |
| 密集参考材料 | `references/*.md` | 存在 |
| 验证与维护脚本 | `scripts/*.py` | 存在 |
| 面向 README 的视觉资源 | `assets/*` | 存在 |
| Codex UI 元数据 | `agents/openai.yaml` | 存在 |
| 行为评测 | `evals/evals.json` | 存在 |
| CI 验证 | `.github/workflows/validate-skills.yml` | 存在 |
| 本地 Codex 安装器 | `scripts/install_codex_skill.py` | 存在 |

## 兼容性规则

- 让每个活跃的 `description` 保持第三人称激活措辞，以便工具能从缩短的技能列表中匹配它。
- 让根 `ZH_REFERENCE.md` 保持精简。路由到子技能和参考，而非把长表格复制进根文件。
- 把易变的事实放在带日期的参考中，如 `api-status.md` 和 `source-registry.md`。
- 若生成的位图被 README 引用，则把它们保留在 `assets/` 内。
- 让 `agents/openai.yaml` 与根技能名称保持一致，并使默认提示词调用 `$seedance-20`。
- 使用 `scripts/install_codex_skill.py --force` 在 `$CODEX_HOME/skills/seedance-20` 或 `~/.codex/skills/seedance-20` 安装或刷新本地用户级 Codex 副本。
- 让脚本保持确定性且本地化。它们应能验证结构、schema、设计和来源元数据，而无需私有凭据。
- 不要在技能包中存储 API 密钥、账号 cookie 或私有提示词语料。

## 跨智能体矩阵

于 2026-06-12 从各智能体的公开文档核实；安装路径易变——在承诺行为前重新核实当前客户端。把本仓库安装为一个根技能（`seedance-20`）；子技能和参考通过相对于根的相对路径加载。

| 智能体 | 技能位置 | 安装途径 | 备注 |
|---|---|---|---|
| Claude Code / claude.ai | `.claude/skills/`（工作区）、托管技能 | 复制或市场 | ZH_REFERENCE.md 形态的起源平台。 |
| Codex | `.agents/skills/` 向上扫描 + 用户/系统目录 | `scripts/install_codex_skill.py --force` | `agents/openai.yaml` 提供 UI 元数据。 |
| Google Antigravity | `.agents/skills/`（工作区）、`~/.gemini/antigravity-cli/skills/`（全局） | 复制该文件夹，重启会话 | 与 Codex 工作区相同的目录约定；ZH_REFERENCE.md + scripts/references/assets 形态与本仓库匹配。 |
| OpenClaw | 工作区 `skills/`、`~/.openclaw/skills/`（全局） | `openclaw skills install`（git/本地要求源根有 `ZH_REFERENCE.md`——本仓库符合） | ClawHub 是公开注册表（用 `clawhub` CLI 发布）。这里每个技能都已带有 `openclaw:` 元数据。 |
| Hermes Agent (Nous Research) | 项目 `skills/`、`~/.hermes/skills/` | `hermes skills install`（运行一次安全扫描） | 依据 frontmatter 的 `description` 激活——本仓库的第三人称激活措辞正是它所匹配的。 |
| Gemini CLI / Cursor / Windsurf / Copilot | `.gemini/`、`.cursor/`、`.windsurf/`、`.github/` + `skills/` | 复制该文件夹 | 视为安装目标，而非独立的源树。 |

## 跨客户端说明

不同的智能体客户端扫描不同的本地路径。Codex 文档说 Codex 从当前目录向上扫描 `.agents/skills` 位置，外加用户/管理员/系统技能位置。一个含 `ZH_REFERENCE.md` 的仓库根具备正确的技能文件夹形态，但除非被安装在被扫描的技能目录下或通过相关的插件/分发路径打包，否则它不会被自动发现为一个仓库技能。其他智能体客户端可能使用 `.claude/skills`、`.gemini/skills`、`.github/skills`、`.cursor/skills` 或 `.windsurf/skills`。把它们视为安装目标，而非独立的源树。

Runway MCP 是一个独立的智能体连接器界面。它能在 MCP 兼容的智能体内通过 Runway 暴露 Seedance 2.0，但它不会使本仓库成为 Runway 插件，也不会改变 Codex 的技能安装规则。

## 来源信号

- OpenAI Codex Agent Skills 文档: https://developers.openai.com/codex/skills
- OpenAI Codex Plugins 文档: https://developers.openai.com/codex/plugins
- OpenAI Academy 插件与技能讲解: https://openai.com/academy/codex-plugins-and-skills/
- OpenAI 技能目录: https://github.com/openai/skills
- Agent Skills 开放标准概览: https://agentskills.io/
- Google Antigravity 技能文档: https://antigravity.google/docs/cli-plugins 和 https://codelabs.developers.google.com/getting-started-with-antigravity-skills
- OpenClaw 技能文档: https://docs.openclaw.ai/tools/skills
- Hermes Agent 技能文档: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Runway MCP 公告: https://runwayml.com/news/mcp

## 不要主张

- 不要主张每个智能体客户端都能直接从本仓库 URL 安装。
- 不要主张 ClawHub 或任何注册表列出了本技能，除非它确实已在那里发布。
- 不要主张每个客户端都遵循超出 `name` 和 `description` 之外的相同元数据字段。
- 不要主张本仓库提供一个实时的 Seedance API 封装。它是一个智能体技能工作流与参考包。
- 不要主张某个智能体对一个序列项目拥有隐藏的跨会话记忆。使用项目状态胶囊来恢复故事目标、最终结局、被采用的镜头、当前实际状态、未完成的运动、已完成节拍、下一镜头任务、连续性锁定项、允许的变化、预留的未来节拍、延展深度和未解决的不确定性。
