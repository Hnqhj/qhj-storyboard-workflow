---
name: nexusvault-css-override-chain
description: nexusvault-post 桌面端改页面/卡片/画布样式前的覆盖链排查清单：已知的全局 CSS 沉积层、反压写法、CDP matched-styles 排查法、按钮归一豁免类陷阱；含画布页专节（深色底 + 点阵被 zoom 吃参、深色面板按钮的 appearance:auto、拖拽带只能降层挖洞不能关、pane 光标：默认箭头而 .selection 常驻不可作判据、多选包围盒与「小数长度被取整」）
use_when: 在 nexusvault-post 改任何 .vue 组件的 scoped 样式、新增/换卡片样式、动画布页配色或点阵、或 scoped 样式/窗口拖动"改了没生效"时
agent_created: true
---

# nexusvault-post 覆盖链排查清单（2026-09-28 实战沉淀）

## 已知的全局覆盖层（按 main.ts 引入顺序，越后越强）

`main.ts` 引入顺序决定胜负（同等特异性后者赢）：
`explore.css → … → editorial-redesign(27) → blaze-parity(28) → … → design-unify.css`（最后引入，事实赢家层）。
另有 soluna-theme / neutral-accent / layout-refinement / project-management-polish 等沉积层，
用 `:root[data-theme=…] .app-shell .page-content …` 这类 (0,5,1) 高特异性埋伏。

## 组件 scoped 样式被压时的标准处理

1. **先诊断再动手**：CDP `CSS.getMatchedStylesForNode` 列出所有命中规则
   （`m.rule.style.cssProperties` 里找目标属性，看谁带 `!important`、选择器多长）。
2. **优先"摘除"**：把该类名从全局文件的选择器组里删掉（skills-card / project-card 都这么处理过），
   让组件 scoped 成为唯一样式源。摘除时把 light 主题 / :hover / 文字规则一并摘。
3. **摘不动时反压**：scoped 选择器升到 `.projects-page .project-grid .xxx[data-v]`（约 (0,4,0)），
   并显式接管 padding / min-height / display（沉积层会塞这些）。
4. **警惕 `:root[data-theme='dark'] …` 前缀变体**——特异性 +1 个 attr，scoped 经常输给它
   （实测：soluna 1382 的 bg、neutral-accent 1154 的 box-shadow）。

## design-unify §3 按钮归一的坑

- §3b `button:not(.projects-create):not([class*='tab'])…` 会把页内普通 button 压成 `--r-sm`(8px)。
- **`projects-create` 是 §3a 主行动胶囊的豁免类（白色 pill CTA，带 !important），
  绝对不要把这个类挂到别的元素上**——挂上就被刷成胶囊（2026-09-28 实测翻车）。
- 新建画布卡（`.project-create`）的豁免写法：在 §3b 排除链加 `:not(.project-create)`。

## 排查时的其他坑

- HMR 改 `components/lucide-animated/index.ts`（加新图标）会出现瞬时
  `XxxIcon is not defined` 黑屏，整页 reload 恢复，不是持久 bug。
- CDP matched-styles 里 `m.rule.style.cssText` 可能 undefined，用 `cssProperties` 数组取属性。
- CDP 截图前确认页面在目标路由（用户可能切走了页面）：
  `history.pushState + popstate` 导航（探针模板 `_projects-shot.mjs` / `_skills-shot.mjs`）。
- 已完成"摘除"的类（不要再往全局加）：`.skills-card`、`.project-card`、
  `.canvas-shell`（整面摘除，写法见 `design-unify.css` 的 `.editorial-shell:not(.canvas-shell)`）。

---

# 画布页专节（2026-09-29 新增）

画布页（`/app/canvas` / `.canvas-shell`）是独立视觉体系，覆盖链上与别处不同，三条都是实测踩出来的。

## 1. 拉深色底 + 点阵：三个数要一起改，且 `gap/size` 会被 zoom 吃掉

- stage 底色在 **两处**（`canvas-editorial.css` 的 `.canvas-page .canvas-stage` 赢，`canvas-flow.css`
  的 `.canvas-page` 只有 (0,1,0) 会输）——脚本改一处后观感没变，就是漏了另一处。
- 点阵由 `<Background variant="dots" :gap :size color>` 画。**Vue Flow 会把 gap 与 size 乘上
  `viewport.zoom`**（读 `@vue-flow/background` 源码：`scaledGap = gap * zoom`、`circle r = size*zoom/2`），
  而 `size` 是**点直径不是半径**。画布进页面会 fitView 到 0.39，于是设的 28/2 上屏只剩 `10.9px / 0.78px`，
  实测反差只有 5/255 —— 表现为「参数明明对，点阵就是看不见」。
  → 喂 `目标屏幕值 / zoom`（两个 computed），屏幕尺寸恒定，pattern 相位仍跟 viewport 走。
- 量测陷阱：**刚进页面读 pattern 属性会读到「都对」**（那时 zoom 还是 1）；`.vue-flow__viewport`
  的 computed transform **量不出真实 zoom**，要读界面右下角读数或用 `.canvas-stage` 的 `zoom-lod-*` 反推。
- 判别手法：把嫌疑元素 `display:none` 前后各截一张相减 → 差异图里只剩目标图案。

## 2. 深色面板里的 `<button>` 必须显式 `appearance: none`

`appearance: auto`（UA 默认）下 Blink 直接画原生 `buttonface` 底色，`background: transparent`
**压不住**它。判据是「计算出的底色是不是 transparent」而不是「有没有写 background」。
写法与仓库其它层一致：`appearance: none; -webkit-appearance: none;`。

## 3. 拖拽带（`-webkit-app-region`）：不能关，只能「降层 + 挖洞」

**别再用 `display:none` 关掉画布页的 `.window-drag-region`。** 那条老写法假定「画布页靠侧栏空白区
拖窗口」，而 AppLayout 里侧栏是 `v-if="!isCanvasRoute"` —— 画布路由下它**整个不进 DOM**，
于是页面上零 drag 区，窗口拖不动。

三条缺一不可（都在 `blaze-parity.css` §D）：

1. `left: 0 !important` —— 外壳带 `topnav-shell`，`editorial-redesign.css` 的
   `body:has(.app-shell.topnav-shell) .window-drag-region { left: var(--rd-sidebar-w) }`
   会把带推到 248px 起；画布没有侧栏 ⇒ 左边空洞。**两条规则特异性都是 (0,3,1)，靠文件顺序决胜**
   （main.ts：editorial 27 < blaze 28）。**顺序若被调换，这条静默失效。**
2. `z-index: 0 !important` —— 必须低于 `.canvas-page`(z-index:1)。原来 fixed+z-index:60 时画布顶栏
   （z-index:10，困在页内层叠上下文）反超不了 ⇒ `elementFromPoint` 命中拖拽带、标题点不动。
3. 页内交互元素显式 `no-drag`（`.ref-title` / `.canvas-project-menu` / `.canvas-menu-card`）——
   RouterView 内容文档顺序更晚，difference 后发生效，把标题从带里挖回来。

⚠️ **两个机制互相独立，别混**：DOM 命中看 `z-index`；`-webkit-app-region` 的合并
**不看 z-index、只按文档顺序**（App.vue 有详注）。所以「降 z-index」只解决点击，
不会削弱拖拽 —— 「要么按钮能点、要么窗口能拖」是伪命题。

验收只能用 `WM_NCHITTEST`（CDP 合成事件绕过系统命中判定）：
`python <repo>/verify/nchittest-probe.py --scan 600`。修复前该列 0..160 全 HTCLIENT，
修复后 `HTCAPTION: y = 5..39`（0..4 是 5px 窗口缩放边框 → HTTOP，不是漏掉的）。
详见技能 `electron-ui-parity` 的 §3 与 `scripts/nchittest-probe.py`。

## 4. 画布 pane 的光标：平时箭头，`dragging` 才变手；`.selection` 是常驻类

画布平移**只走中键**（`CanvasView.vue` 早就是 `:pan-on-drag="[1]"`），左键在空白处是框选。
两个结论：

- **别加无条件的 `.vue-flow__pane { cursor: grab }`。** 手型在说「左键能拖」，而左键实际是框选。
  库自带的 `.vue-flow__pane.draggable { cursor: grab }` 在本配置下**是死规则** ——
  `draggable` 判定 = `panOnDrag === true || panOnDrag.includes(0)`（`vue-flow-core.mjs:8702`），
  传 `[1]` 不含 0 ⇒ 该类压根不出现。**常驻手型一定是你自己写的**，去 grep `cursor: grab`。
- ⚠️ **`.vue-flow__pane.selection` 是常驻类，语义是「当前可框选」而不是「正在框选」。**
  判据 `isSelecting`（`vue-flow-core.mjs:8471`）在本配置下**恒为 true**：
  `selectionKeyCode === true`（免按键框选，本项目给 `true`）+ `panOnDrag = [1]`
  （**数组严格 `!==` 布尔 `true`**）⇒ `shouldSelectOnDrag` 恒成立。
  给它设任何 cursor = 画布永远停在那个光标上（实测翻车：整页变十字）。
  它还与 `.dragging` **同特异性 (0,3,0)**，后写的赢 —— 写在后面会连中键拖动一起盖掉。
- **「正在拖动」用 `.dragging`**：判定是 `dragging: paneDragging`（`vue-flow-core.mjs:8701`），
  与 `panOnDrag` 无关，中键真拖起来时会挂上。正确两条：
  ```css
  .canvas-stage .vue-flow__pane { cursor: default; }
  .canvas-stage .vue-flow__pane.dragging { cursor: grabbing; }
  ```
- 区域选择 / 落位模式的十字（`.is-marquee` / `.is-placing`，写在 `canvas-chrome.css`）
  是 (0,4,0)，优先级高于上面两条，不受影响；库自带 `.selection { cursor: pointer }`
  与第一条同 (0,2,0)，靠**加载顺序**取胜（库 `style.css` 引在 `main.ts` 最前），不需要 `!important`。
- 验收探针：`_cursor-probe.mjs`（默认 `default` / 真实中键拖动 `grabbing` / 释放回 `default` /
  两个模式 `crosshair` 回归）。详见 `docs/engineering-notes.md` §52。

## 5. 多选包围盒：自带的组件是「透明」的；小数长度会被取整

「框选后什么都没有」先别急着写新组件 —— Vue Flow 有 `NodesSelection`，框选结束后
**它确实渲染**（实测 `present: true`、`rectBox` 与选中节点联合 bbox 完全重合、紧贴无内边距）。
全透明是因为 `main.ts` 只引了 `@vue-flow/core/dist/style.css`（**结构**：定位/层级），
**没引 `theme-default.css`**（**视觉**：蓝色点线 + 淡蓝底）。项目里的
`.vue-flow__selection`（框选矩形）当初也是同样原因才自己补样式的。

- **必须往外让一圈** —— 这是**硬约束不是审美**：`.vue-flow__viewport` 是 z-index:4，
  `.vue-flow__nodesselection` 是 3，包围盒在所有卡片**下面**，零间距时框线被整条盖住。
- **反缩放**：rect 的 `top/left/width/height` 是**画布坐标系**里的内联值，父级
  `.vue-flow__nodesselection` 带 `scale(zoom)`。尺寸用 `calc(Npx / var(--zoom))` 拉回屏幕空间。
- ⚠️ **别用 `outline`**。`NodesSelection` 挂载时会 `el.focus({preventScroll:true})`
  （`vue-flow-core.mjs:8138`），而 Vue Flow 自带样式有
  `.vue-flow__nodesselection-rect:focus { outline: none }`（`style.css:59`）。
  症状**极具误导性**：`outline-offset` 生效、`outline` 不生效 —— 同一条规则「半条活下来」，
  看起来像选择器没命中（翻 `cssText` 能看到 outline 明明在）。一律改用**伪元素 + border**。
- ⚠️⚠️ **小数长度会被向下取整到整数 CSS 像素 —— 是真实渲染，不是上报值。**
  对照实验（注入测试元素 + 截图逐像素量）：`border-top: 1.434px` → 画出 **1.000px**；
  `background-size: 100% 1.434px` → 同样 **1.000px**；而 `border-width: 2px`（整数）精确
  （屏幕量到 1.498px）。**两种画法都躲不掉。**
  → 后果：`calc(1.5px / zoom)` 在 zoom ≥ 1.5 时 < 1 → 取整成 **0，线整条消失**。
  → **要屏幕恒定线宽，必须在 JS 里先 `round` 成整数**再交给 CSS。
  → **DPR=1 屏幕上根本不存在「恒定 1.5px」**，屏幕线宽只能是 `N × zoom` 的离散点；
    别再试图用纯 CSS 调出小数线宽。
- **四角方块只能用背景图**：伪元素只有 2 个，`box-shadow` 的偏移依赖元素宽度
  （CSS 里表达不了），都不是「四个角」的正解。

**验收纪律**：线宽真值必须用**截图逐像素量**（`_measure-line.py` 之类），
`getComputedStyle` 报的是取整后的值，会骗人。探针 `_box-probe.mjs`。
详见 `docs/engineering-notes.md` §53。
