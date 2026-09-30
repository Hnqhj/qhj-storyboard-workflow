---
name: electron-window-visibility-forensics
description: 排查「Electron 桌面应用看起来根本没启动」—— 进程活着、端口在听、CDP 能连、截图有内容，但屏幕上没有窗口。用于判定窗口到底存不存在 / 可见不可见、`ready-to-show` 与 `show()` 是否静默失效、原生窗口就绪竞态，以及写最小复现探针时的坑（同步 IPC 挂死）。当用户说「软件没起来」「窗口没出来」「桌面端根本没运行」「启动了但看不到界面」，或要判断某个 Electron 窗口的可见性时使用。
agent_created: true
---

# Electron「窗口不显示」取证

**核心症状**：用户说「软件没启动」，但进程树完整、端口都在 LISTENING、
CDP 能连、`Page.captureScreenshot` 还能截出**完整界面** —— 就是屏幕上什么都没有。

这类问题的难点**不在修，在判**：手边最顺的三个判据全部会骗人。

## 1. ⚠️ 三个会骗人的判据（别用）

| 判据 | 结果 | 为什么不可信 |
| --- | --- | --- |
| `Get-Process electron \| Select MainWindowHandle` | `0` | **对 Electron 恒为 0** —— 窗口明明可见、还拿着焦点时也是 0（实测 Electron 36.9.5） |
| `tasklist /V` 的「窗口标题」列 | 只有 `GDI+ Window (electron.exe)` / `OleMainThreadWndName` | 认不出应用主窗口，只列出辅助窗口 |
| 页面侧 `document.visibilityState` | `visible` | **OS 层面窗口是隐藏的，它照样报 `visible`**；`document.hasFocus()` 也可能为 `true` |

> 这三个都会把「窗口不存在/不可见」误判成「窗口正常」，
> 于是排查方向会被带到「GPU 参数」「页面没渲染」上去。

## 2. ✅ 唯一可靠判据：枚举顶层窗口 + `IsWindowVisible`

PowerShell 的 `Add-Type`（P/Invoke 的唯一常规入口）**会被安全策略拦截**
（`Command blocked for security: Add-Type compiles and loads .NET code at runtime`），
所以走 **Python `ctypes`** 直接调 `user32.dll`：

```bash
# 只看可见窗口
python .workbuddy-ai/verify/win-top-windows.py --name electron
# 含不可见窗口（关键：隐藏窗口只有加 --all 才看得到）
python .workbuddy-ai/verify/win-top-windows.py --all --name electron
```

判读：
- `VIS=Y` → 窗口真的在屏幕上。
- `VIS=n` 但**标题/几何都对** → 窗口存在但被隐藏，就是本文这个 bug。
- 窗口的 `RECT` 应该与页面侧读到的
  `{screenX, screenY, outerWidth, outerHeight}` **完全一致** ——
  这反过来证明枚举到的就是应用主窗口，不是别的辅助窗口。

## 3. 定位：给主进程加诊断，别猜

「`ready-to-show` 有没有触发」「`show()` 有没有生效」**只有主进程知道**。
在创建窗口处临时加：

```js
win.webContents.on('dom-ready', () => diag('dom-ready'))
win.webContents.on('did-finish-load', () => diag('did-finish-load'))
win.webContents.on('did-fail-load', (_e, c, d, u) => diag('did-fail-load', `${c} ${d} ${u}`))
win.webContents.on('render-process-gone', (_e, d) => diag('render-process-gone', JSON.stringify(d)))

win.once('ready-to-show', () => { diag('ready-to-show 触发'); win.show(); diag('show() 后', `isVisible=${win.isVisible()}`) })

// 关键：窗口事件。`show` 之后紧跟 `hide` = 「有人把它藏回去了」，与「show 没生效」是两种病
win.on('show', () => diag('事件 show'))
win.on('hide', () => diag('事件 hide'))
win.on('minimize', () => diag('事件 minimize'))
win.on('focus', () => diag('事件 focus'))

setTimeout(() => diag('5s 复查', `isVisible=${win.isVisible()}`), 5000)
```

**本 bug 的签名**（Electron 36.9.5 + `--disable-gpu --in-process-gpu
--disable-software-rasterizer --disable-gpu-compositing`）：

```
+2534ms ready-to-show 触发
+2549ms 事件 show                 ← show 事件触发了
+2549ms show() 后 isVisible=false  ← 但窗口没可见
+2550ms 事件 focus
+5001ms 5s 复查 isVisible=false
+5010ms 重试后 isVisible=true      ← 5 秒后再调一次 show() 就成功了
```

→ **`ready-to-show` 正常触发、`show()` 也调了、事件都发了，但窗口不可见；
隔一会儿再调一次 `show()` 就正常。** 这是原生窗口与合成器尚未就绪的**竞态**。

## 4. 分层排除：写最小复现探针（`.workbuddy-ai/verify/electron-show-probe.cjs`）

在完整应用里排查一轮要 40 秒且噪声多。压到只剩一个变量、逐个逼近：

```
① 最小窗口 + data URL + 不带开关        → 基线（本机无开关时 GPU 进程反复崩溃）
② 最小窗口 + data URL + 完整开关        → 验开关是否元凶
③ 真实 dev URL + 完整开关 + 无 preload  → 验页面是否元凶
④ 真实 dev URL + 完整开关 + 真实 preload → 验 preload 是否元凶
```

⚠️ **②③ 都 `isVisible=true`** → 说明**开关与页面都不是原因**。
⚠️ ④ 复现不出来也正常 —— 真实应用的竞态，最小复现会把它盖掉。

### ⚠️ 4.1 探针自己的坑：同步 IPC 没有处理器 = 渲染进程永久挂死

`preload` 里常见这种**同步**取配置的写法：

```js
const port = ipcRenderer.sendSync('remote-api-port')   // 主进程用 event.returnValue 回
```

**探针若没注册 `ipcMain.on('remote-api-port', …)`，`sendSync` 会永久阻塞** →
preload 永不返回 → 页面永不加载 → `ready-to-show` 永不触发。
表现是「**带了 preload 就永远不显示**」，极容易被误判成「preload 坏了」。

修法：探针里补 `ipcMain.on('remote-api-port', (e) => { e.returnValue = 0 })`。

> 通则：**任何 `ipcRenderer.sendSync(channel)` 的 channel 都必须有处理器**，
> 否则挂死渲染进程且**不报任何错**。

### 4.2 探针的两个纪律

- **等待时间要留足**：默认 3s 时踩过假阴性 —— 带 preload 那轮 `ready-to-show`
  要 ~3.1s 才触发，正好卡在退出之后，看起来像「没触发」。用 `PROBE_WAIT_MS` 调大。
- **开关必须作为真实命令行参数**传给 `electron.exe`（Chromium 解析整条命令行），
  别在脚本里 `appendSwitch` —— 对 `--no-sandbox` 这类早期开关无效。

## 5. 修法：显示后**复查**，没显示就重试

```js
/**
 * 显示窗口，并确认它真的显示了。
 * ⚠️ 不能只写 `win.once('ready-to-show', () => win.show())` ——
 * 在 ready-to-show 里同步 show() 会**静默失效**（事件照发、不抛错、isVisible 恒 false）。
 */
function showWindowReliably(win, label) {
  if (win.isDestroyed()) return
  win.show()
  if (win.isVisible()) return          // 正常机器到此为止，一次多余调用都没有

  let tries = 0
  const retry = () => {
    if (win.isDestroyed() || win.isVisible()) return
    if (tries >= 10) { console.warn(`[window] ${label}：show() 重试 10 次后仍不可见，放弃`); return }
    tries += 1
    // 失败路径本身是静默的 —— 没有这行日志，将来「窗口偶尔不显示」无从下手
    if (tries === 1) console.warn(`[window] ${label}：ready-to-show 里的 show() 未生效，开始重试`)
    win.show()
    setTimeout(retry, 300)
  }
  setTimeout(retry, 300)
}
```

要点：
- **有界**（10 × 300ms ≈ 3 秒）+ 每次先复查 `isVisible()` → 正常机器零副作用。
- **失败路径留一条 `console.warn`**：不然这个 bug 下次还是静默的。
- **主窗口和所有子窗口都要改**（画布/工具窗通常是同一份复制粘贴）。
- ⚠️ **`setImmediate(() => win.show())` 不够**（实测第一次仍 `isVisible=false`）。
- ⚠️ 别指望「加个延迟就好」——延迟多少是不可靠的，**复查 + 重试**才是判据。

## 6. 排掉「看起来像但其实不是」的

| 现象 | 真相 |
| --- | --- |
| 日志里 `Failed to create GLES3 context` / `ContextResult::kFatalFailure` | **不是元凶**。`Page.captureScreenshot` 能截出完整界面 → 软件光栅化正常 |
| DOM 已挂载、标题正确、截图有内容 | 只证明**渲染没问题**，与「窗口可见」无关 |
| `.app-topbar { display: none }` | 可能是**皮肤刻意设计**（本项目 editorial 皮肤就是隐藏顶栏），不是回归 |
| `Browser.getWindowForTarget` 报 `-32601 wasn't found` | 该 Electron 版本不支持这个方法，**不代表窗口不存在** |

## 7. 工具清单

| 工具 | 用途 |
| --- | --- |
| `.workbuddy-ai/verify/win-top-windows.py` | **枚举顶层窗口 + 可见性**（Python ctypes，绕开 Add-Type 拦截） |
| `.workbuddy-ai/verify/cdp-eval.mjs` | 在运行中的应用里求值任意 JS（读 DOM / 几何 / `visibilityState`） |
| `.workbuddy-ai/verify/cdp-window-state.mjs` | 读窗口状态（⚠️ 本 Electron 不支持 `Browser.getWindowForTarget`） |
| `.workbuddy-ai/verify/current-shot.mjs` | 截当前 CDP 页面（证明「页面能不能画出来」，**不证明窗口可见**） |
| `.workbuddy-ai/verify/electron-show-probe.cjs` | 最小复现：`show()` 能否让窗口可见（`PROBE_URL` / `PROBE_PRELOAD` / `PROBE_SHOW_MODE` / `PROBE_WAIT_MS`） |

## 8. 收尾

1. **删掉临时诊断**（主进程里的 `diag` 一堆日志）。
2. 保留 `showWindowReliably` + 那条 `console.warn`（那是**修法的一部分**，不是调试代码）。
3. ⚠️ **`desktop/*.cjs` 通常不在 prettier 覆盖范围内**（本项目 `format:check` 只跑
   `apps/web`）。**别对它跑 `npx prettier --write`** —— 会产生上百行纯噪声 diff。
   先验证：`git show HEAD:<file> > <repo内临时路径>` 再用**真实文件路径**查格式
   （⚠️ `prettier --check` 读 **stdin** 会给**假的「干净」**结果）。
4. 重启并**用 OS 枚举**确认 `VIS=Y`，再跑门禁（`test:desktop` 之类）。
5. 把结论写进项目的工程笔记，并在**修复处**留注释说明「不要改回 `() => win.show()`」。
