---
name: skill-bundle-release
agent_created: true
description: 把技能仓库发布成 GitHub 扁平分发包，并维护用户侧自动更新。触发：更新技能包、发布到 GitHub、重新打包、分发包、自动更新、update.ps1、install.ps1。 Publish a categorized skill repo as a flat GitHub distribution bundle (skills/ + manifest.json + install/update scripts) without destroying the existing auto-update mechanism.
---

# 技能包发布与用户侧自动更新

把一个**分类目录结构**的开发仓库，发布成**扁平结构**的 GitHub 分发包，并让用户侧能自动更新。

> **一句话铁律**：开发仓库与分发包**历史无关、结构不同** →
> **永远不要对分发包直接 `git push`**，否则会删掉远端的 `install.ps1` / `update.ps1` /
> `setup-auto-update.ps1`，把自动更新机制一起推没。

## 〇、先分清两个仓库

| 角色 | 结构 | 谁写 |
|---|---|---|
| **开发仓库** | 分类目录：`prompt/拆分镜`、`prompt/生图`、`prompt/全流程`、`其他/` | 人 + 同步器，日常在这里改 |
| **分发包**（GitHub） | 扁平 `skills/<name>/` + `manifest.json` + 安装脚本 | **只由发布流程写** |

判据：`git remote -v` 为空、或两边 commit 历史无共同祖先 → 是两套独立仓库，**别 push**。
开工前必做：`git log --oneline` 比两边历史，`git ls-remote <url>` 看远端是不是空仓库。

## 一、生成扁平包

用仓库自带的生成器，**不要手工 `cp -r`**：

```bash
node .workbuddy-ai/tmp/build-bundle.mjs --out .workbuddy-ai/tmp/bundle --version 2.0.0
```

- 只取 LAYERS 里的分类目录，平铺成 `skills/<dir-name>/`（目录名即技能名）。
- **刻意不做删除**：过期技能只**报告**，不自动清 —— 本机删除有守卫（safe-delete），
  脚本里跑 `rm` 会被拦。陈旧项由人工确认后再处理。
- 产出 `manifest.json`（`name` / `version` / `created` / `skills[]`）。

## 二、发布（五步）

```bash
git clone git@github.com:<owner>/<repo>.git .workbuddy-ai/tmp/<clone>
cd .workbuddy-ai/tmp/<clone>

# 1) 旧 skills/ 改名让位（改名 = 秒完成，且保留回滚能力；不要删）
mv skills ../_old-skills-<日期>

# 2) 拷入新包
cp -r ../bundle/skills ./skills
cp ../bundle/manifest.json ./manifest.json

# 3) 安装脚本与 README 原样保留 —— 除非本次就是要改它们
#    核对：git status --short -- install.ps1 update.ps1 setup-auto-update.ps1 README.md 应为空

# 4) 提交（先看清规模，再提交）
git add -A && git status --short | awk '{print $1}' | sort | uniq -c
git commit -m "chore(bundle): 技能包更新至 N 个（vX.Y.Z）"

# 5) 推送
git push origin main
```

**发布前必查**：`comm -23 <(远端技能名排序) <(本地技能名排序)` 应为空 ——
即**本地是远端的超集**，否则替换会丢技能。

## 三、用户侧自动更新（是轮询，不是实时）

`setup-auto-update.ps1` 注册 Windows 计划任务 `<repo>-AutoUpdate`，默认每天 03:00 跑 `update.ps1`：

```
git clone --depth 1 <repo> <tmp>  ->  平铺覆盖到各宿主 skills\  ->  写 qhj-manifest.json
```

- 三个脚本统一 `-Target codex|workbuddy|all`（默认 `all`），`-CodexHome` / `-WorkBuddyHome` 可覆盖目录。
- **只新增 / 覆盖，不删除**；不碰宿主系统目录。
- **回答用户「别的 agent 装完能不能实时同步」**：不能实时，是**下一次定时任务**才拿到；
  想立刻生效手动跑一次 `update.ps1`。
- **技能清单在会话启动时固定** → 更新完**必须新开一个会话**才看得到新技能。
- 版本以 `manifest.json` 为准：发新版就改版本号 + 提交 + 推送。

## 四、踩过的坑（都实测过）

1. **PS 5.1 + 原生命令 stderr**：`$ErrorActionPreference = 'Stop'` 配裸 `git clone`，
   上层一旦重定向错误流（`*>&1` / `2>&1`）就被误判成终止错误（`NativeCommandError`）。
   → git 调用前后**局部降级为 `Continue`**，只认 `$LASTEXITCODE`。
2. **分发包 `.ps1` 含中文必须 UTF-8 with BOM**，否则 PS 5.1 按 GBK 解码中文路径乱码。
3. **行尾**：clone 无 `.gitattributes` 且本机 `core.autocrlf=true` → `git add` 刷一屏
   `LF will be replaced by CRLF`。加 `.gitattributes`（`* -text`）后 `check-attr` 应为 `text: unset`、
   `git add` 幂等。诊断假 diff：`git diff --numstat` 与 `--ignore-cr-at-eol --numstat` 计数应相同。
4. **网络**：`github.com` 的 HTTPS 可能被本机代理挡（`CONNECT tunnel failed, 502`）→ 走 **SSH**
   （`git@github.com:...`）；`api.github.com` 通常仍可读，用来**复核推送结果**。
5. **临时目录**：`git clone` 的目标目录用 GUID 后缀（`<prefix>-<8位>`），避免残留/并发导致失败。

## 五、验证清单（别只看「命令返回 0」）

- [ ] `api.github.com/repos/<o>/<r>/commits/main` → sha 与本次提交一致
- [ ] `api.github.com/repos/<o>/<r>/contents/skills` → 条目数 == 预期技能数
- [ ] 根目录脚本仍在（`.gitattributes` / `README.md` / `install.ps1` / `manifest.json` /
      `setup-auto-update.ps1` / `update.ps1`）
- [ ] 三个脚本 `Parser::ParseFile` 语法 OK
- [ ] 用**临时目录**跑通 `install.ps1 -Target all`（不碰真实宿主），核对技能数
- [ ] `update.ps1 -Repo <本地包路径>` 能跑通（离线验证，不依赖 GitHub）
- [ ] 临时目录无残留
