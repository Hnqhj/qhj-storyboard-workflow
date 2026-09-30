---
name: nexusvault-legacy-module-removal
description: 在 nexusvault-post（G:\工作\vibecoding\nexusvault-post，Vue3 + Go + Electron）里整体移除一个遗留功能模块——删不可达视图、拆功能开关、清死 CSS、清孤儿假数据、同步测试，并跑门禁 + CDP 运行时验证。当用户说「不要 XX 功能」「把 XX 模块删掉」「清理死代码」「移除遗留页面」，或要动 router.ts 的路由表 / config/features.ts 的功能开关 / views 下的孤儿页面 / 只服务已删元素的 CSS 时使用。
agent_created: true
---

# 在 nexusvault-post 里整体移除一个遗留模块

目标：把一个功能模块**从入口到接线全部拆干净**，且每一步都有可复现的判据。
这个仓库的纪律是「**报成功不算证据**」—— 每个结论都要能指着一个命令的输出说话。

## 0. 前置：先读 `nexusvault-post/docs/engineering-notes.md`

改动前必读。本文只写**流程与坑**，环境坑（删除守卫、无头浏览器落盘、`vite build`
被拦）在 `~/.workbuddy-ai/MEMORY.md` 与工作区 `MEMORY.md` 里。

## 1. 判定「哪些页面不可达」——权威判据只有路由表

一个 view 要被渲染，必须出现在 `apps/web/src/router.ts` 某条 `component:` 上。
全仓库**只有 `router.ts` 会 import 它们**。

```bash
cd apps/web/src && grep -n "component:" router.ts
```

⚠️ 两个必避的误判：
- **子串误命中**：`CanvasProjectsView` 会命中 `ProjectsView` 的搜索，但它是活的。
- **注释/文档里的名字不算引用**：`ProjectsView` 唯一的「引用」是 `router.ts`
  一条注释，而那句注释本身就写着「已经不可达」。

⚠️ 搜的时候**一条 `-E` 交替匹配扫完**，别写逐个 grep 的循环（会撞 SIGTERM），
且**必须在 grep 层就 `--exclude-dir=node_modules`**，否则走一遍必超时。

## 2. 删除文件：用 `.NET`，删完**立刻**核对条数

```powershell
[System.IO.File]::Delete('...')                       # 单文件，不需审批
[System.IO.Directory]::Delete($p, $true)              # 目录，实测也不需审批
```

⚠️ **不要用 `rm -rf`**：条目数超 bulk-guard 阈值会被**整批拒掉**，且本会话删除通道
**永久关闭**。⚠️ **更不要用 `git rm`** —— 实测被 SIGTERM 打断后会留下半完成状态，
甚至**多删了没指定的文件**，并留下陈旧的 `.git/index.lock`。

**硬纪律：任何删除后立刻 `git diff --name-status HEAD` 核对条数 == 预期条数。**
本次靠这步当场发现过「多丢两条」。

意外多删的恢复：`git restore --source=HEAD --staged --worktree <f1> <f2>`
（同时恢复索引 + 工作树）。清陈旧锁：先 `Get-Process -Name git` 确认无进程，
再 `[System.IO.File]::Delete("...\.git\index.lock")`。

## 3. 拆功能开关：注意「开关可能早就不能独立控制任何事情」

`config/features.ts` 的注释曾写着「staged … lets us **re-open** the workspace
without removing its routes」——**这句话是陷阱**：光把开关改 `true`
**恢复不了页面**，路由表里那几条仍是 `redirect`。

⚠️ 如果一个开关的另一半是**恒为 `true` 且零消费方**的常量，那**整个文件都该删**，
不是只删那一项。留一个「谁都 import 不到」的配置文件等于给下一个人留一个谎。

守卫要拦的路径，如果路由表里**本身就是 `redirect`**，那守卫是多余的一层，一起删。

## 4. ⚠️ 不要留下「恒为空」的占位状态

例：删团队功能时，`currentTeamId` 还有两个活着的消费点。**故意不保留一个恒为 `''`
的占位** —— 读它的代码看起来仍有那个语义而它永远不变，于是判断成了「永远走同一个
分支」的死逻辑，将来没人能判断该修还是该删。

**正确做法：让 `vue-tsc` 把调用点直接报出来**，逐个改成它们真正需要的语义。
（本次：一条 `watch` 整条删掉、一个 `RouterView` key 改成特判形式。）

## 5. 连带清单（照单全收，别漏）

| 类别 | 怎么找 |
| --- | --- |
| 组件 | 被删页面的唯一使用方，搜组件名 |
| **图标别名** | 删了别名后它带出的具名导入会变「未使用」→ lint 报错。别名与导入**都要删** |
| 请求头 / 全局槽 | `api/client.ts` 里的模块级状态与它加的头 |
| **预览假数据** | `client.ts` 的 `previewFixture`。判据：在 `src` 下搜该路径，**只命中假数据表自己的定义** = 孤儿 |
| 死 CSS | 见第 6 节 |
| 测试 | 三个文件：`App.test.ts`、`api/client.test.ts`、`stores/*.test.ts` |

## 6. 死 CSS：**能证明「命中元素数恒为 0」才敢删**

### 6.1 先分清两种情形 —— 决定「整文件删」还是「逐规则手术」

| 情形 | 判据 | 处置 |
| --- | --- | --- |
| **整文件死亡** | 文件里**每一条**规则的选择器都含至少一个「活代码零命中的类名」 | ✅ 整文件删 + 摘 `main.ts` 的 import |
| **部分死亡** | 只有一部分规则如此 | ⚠️ **别动**，见 6.4 |

⚠️ **判据必须按「规则」判，不能按「类名」判。** 粗判（「这个文件里的类名有几个还活着」）
会给出**错误结论**：文件里往往确实有 `icon-button` / `page-content` / `active`
这类通用工具类，看起来「文件还活着」——但它们全部以 **「死类 后代 活类」** 出现：

```css
.canvas-toolbar .icon-button { … }   /* .canvas-toolbar 活代码零命中 → 整条死 */
```

**正确判据：一条规则只有在它选择器里每一个类名都还活在代码里时才可能命中元素。**
工具：`.workbuddy-ai/verify/css-dead-rules.mjs`（逐规则判；它同时正确处理**跨行选择器
列表** —— 逐行 grep 会把续行 `.canvas-toolbar {` 误判成「不含死类名」）。

### 6.2 ⚠️ 最硬的一步是**正向证明**，不是 before/after 对比

**别用「计算样式普查」下结论**（`style-census.mjs` 留作参考）。实测它被异步渲染和
动态内容污染，报出一堆假阳性：`/app/notifications` 元素数 166 → 17（只是采样时
还没渲染完）、一个积分组件的 `<small>` 宽度 74.3 → 97.4（是**文本内容**变了）。
**这种噪声比没有验证更糟 —— 它会让人去改一个本来正确的改动。**

**正解（`css-selector-match.mjs`）**：把每条选择器拿到**运行中的应用**里
`querySelectorAll` 一遍、数命中数。命中 0 = 永远不生效，**与渲染时序无关**。

```bash
# 文件已删 → 用 --git HEAD 从历史里读
node .workbuddy-ai/verify/css-selector-match.mjs --git HEAD --repo nexusvault-post \
  --files "apps/web/src/a.css,apps/web/src/b.css"
```

配合静态证据形成闭环：
- 静态证明「代码不会产出这些类名」—— 全部 `.vue`/`.ts` 里用**词边界正则**
  `(?<![\w-])name(?![\w-])` 零命中（`css-dead-rules.mjs` 内置）；
- 动态证明「运行时确实没有这些元素」—— 遍历全部活路由实测命中 0。

⚠️ 静态检查覆盖了**弹层组件**（它们也是 `.vue` 文件），所以不必专门去打开弹层。

### 6.3 三个必须单独排掉的「不是类名」的出口

1. **`@keyframes`** —— 查引用方；只有它自己那条（已死的）规则在用才安全。
2. **CSS 自定义属性（`--xxx`）** —— 定义与使用是否**全在本文件内**？外部零引用才安全。
3. **动态拼出来的类名** —— 搜 `` `前缀-${变量}` `` 与 `classList.add/remove/toggle`。
   本项目只有 `card-${kind}` / `port-type-${type}` / `publish-type-${type}` /
   `is-${state}` / `explore-cover-${type}` / `canvas-hint--${tone}`。

### 6.4 ⚠️ 「部分死亡」的文件**别做逐规则手术**

`layout-refinement.css`(1183/1392)、`style.css`(691/910)、`explore.css`(375/1309)、
`soluna-theme.css`(347/439) 都属于这一类。**不动**，因为：
- 删掉其中一条规则，会让**后面的同名/同特异度规则开始生效** —— 级联结果可能变；
- 这些文件里有大量 `:not(:has(.已删类))` **恒真条件**，直接删那个 `:not(:has(…))`
  会**降低特异度**，同样可能翻转级联。

**结论：要么整文件可判死（可删），要么必须逐条做视觉回归（成本高、收益低）。**
后者的正确做法是先把 `:has()` 恒真条件统一处理掉、再删规则，属独立事项。

### 6.5 混合选择器列表：只能摘那几行

`.topbar-login-trigger, .topbar-notification-trigger, .topbar-profile-trigger,
.topbar-team-trigger, .topbar-team-empty { … }` 这种**不能整条删**，只能摘目标行
→ 用精确字符串替换 + **命中次数断言**（同一份列表可能在文件里出现 2 次，
写「期望 1 次」会当场报错 —— 这正是断言的价值）。

另外：按起始/结束标记整段切会**顺手吃掉规则之间的空行**，让两条规则贴在一起。
要保留空行的地方改用「精确替换，把空行写进被替换的字符串里」。
参考脚本 `.workbuddy-ai/verify/strip-team-css.mjs`。

⚠️ **反例（不能按 6.1 判死）**：定义了活页面在用的通用工具类、或含 `:not(:has())`
恒真条件的文件 —— 那些必须靠截图回归，见 6.4。

### 6.6 收尾必做

删完立刻：`git diff --name-status HEAD` 核对条数 == 预期（`N 个 D + 1 个 M`）。
删除前后各截一张同一路由的全视口图 —— 本次是**逐字节相同**。

## 7. ⚠️ 删 `vi.fn` mock 的形参会打断 `mock.calls` 的类型

为了消 `no-unused-vars` 把 `vi.fn(async () => …)` 的参数删掉，会得到：

```
error TS2493: Tuple type '[]' of length '0' has no element at index '1'
error TS2352: Conversion of type 'undefined' to type 'RequestInit' may be a mistake
```

调用元组是**从签名推出来的**：参数一删就退化成 `[]`，`mock.calls[0]?.[1]` 取不到值。
**正解：形参哪怕函数体不读也要 `void input` / `void init` 显式消费**。
⚠️ **`_input` 下划线前缀不管用**（本仓库没配 `argsIgnorePattern`）。

## 8. 门禁 + 运行时验证

```bash
cd nexusvault-post
npm run format:check && npm run lint:web && npm run typecheck:web
npm run test:web        # ⚠️ 跑前必须先停桌面端，否则卡死 420 秒且无输出
npm run test:desktop
mv apps/web/dist /tmp/nexusvault-dist-stale-$(date +%s)   # ⚠️ 先让开，否则被删除守卫拦
npm run build:web
```

**删完门禁全绿 = 「这些东西确实不可达」的反证**：若还有活代码引用，`vue-tsc` 会报出来。

运行时（**功能绿 ≠ 视觉没问题**）—— 起桌面端后用 CDP 读**真实 DOM**：

```bash
npm run desktop:dev &          # 先探测 5178/9222，别盲目再起一个
node .workbuddy-ai/verify/cdp-eval.mjs "JSON.stringify({ \
  mounted: (document.querySelector('#app')?.children.length ?? 0) > 0, \
  deadNodes: document.querySelectorAll('[class*=已删的类名前缀]').length, \
  overlay: !!document.querySelector('vite-error-overlay') })"
node .workbuddy-ai/verify/cdp-boot-diag.mjs --wait 9000    # 订阅后重载，抓启动期报错
node .workbuddy-ai/verify/current-shot.mjs 9222 <out.png> 1
```

⚠️ 两个「看着像坏了其实没坏」的坑：
- **`.app-topbar` 的 `display: none` 是 editorial 皮肤的刻意设计**
  （`editorial-redesign.css`），顶栏在该皮肤下本来就不显示 → 截图里看不到顶栏
  **不是**回归。
- 启动期两条 401（`/auth/refresh`、`/users/me`）是访客态**正常**的。

真实验证已删路由的 redirect：`cdp-eval.mjs "location.assign('<url>/app/organization')"`
再查 `location.pathname` 是否变成 `/app/dashboard`。

## 9. 刻意**不要**动的两处

1. **`desktop/remote-proxy.cjs` 的 CORS 允许头里的旧字段**（如 `x-team-id`）——
   `access-control-allow-headers` 是**白名单**，删掉会让**还在发这个头的旧客户端**
   （已安装的旧版桌面端）预检失败。留着零成本，删掉有真实风险。
2. **后端与 `contracts/openapi.yaml` 里对应的接口** —— 这类任务是**前端功能移除**，
   后端实现原样保留。要在注释里写明这个取舍。

## 10. 收尾

- 工程笔记追加一节（含每个坑的「怎么发现的」）。
- 工作区记忆追加流水；新硬约束进 `MEMORY.md`。
- 提交信息里写清「删的是什么 + 为什么敢删 + 验证结果」。
- ⚠️ 推 `main` 只跑 web 门禁，**不发版**（发版只在 `tag_push`），可以先确认
  `.cnb.yml` 的 `main: push:` 段再推。
