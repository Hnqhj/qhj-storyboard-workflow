---
name: wails-windows-desktop-build
description: Wails v2 (Go + WebView2) Windows 桌面应用的构建、托盘、图标与便携化踩坑清单。触发：wails build 秒退、OnStartup 不执行、托盘图标 set icon 失败、go build 出来的 exe 没图标、想把外部 exe/资产打进单文件、WebView2 报 Process failed with kind N。
agent_created: true
---

# Wails v2 Windows 构建踩坑清单

本机实测环境（2026-09-30）：Go 1.25.0 在 `C:\go-sdk\go`（**不在 PATH**，要全路径调用）；
Wails v2.16.0；无 gcc（必须 `CGO_ENABLED=0`）；无 `rc.exe` / 无 Windows SDK。

## 0. 构建命令（本机模板）

```bash
cd <proj> && GOROOT="C:/go-sdk/go" GOMODCACHE="G:/工作/wbegg/.gocache/mod" \
GOCACHE="G:/工作/wbegg/.gocache/build" GOPROXY=off GOFLAGS=-mod=mod GOSUMDB=off \
GOTOOLCHAIN=local CGO_ENABLED=0 "C:/go-sdk/go/bin/go.exe" build \
  -tags "desktop,production" -ldflags="-H windowsgui" -o build/App.exe .
```

缓存放 G 盘：C 盘常年只剩几百 MB，Go 模块缓存会把它撑爆。

## 1. 必加 `-tags "desktop,production"`，否则程序秒退且无任何日志

- `internal/app/app_dev.go` 是 `//go:build dev`，`app_production.go` 是 `//go:build production`。
- **两个 tag 都不给时，两者都不编译**，落到 `app_default_windows.go` 桩实现：
  `CreateApp` 返回 `(nil, nil)`、`Run()` 直接 `return nil`。
- 症状：进程**正常退出码 0**、不创建窗口、**`OnStartup` 从不执行**、不打任何日志
  （连 `-ldflags` 的 debug logger 也不输出，因为根本没进 Wails）。
- 极易误判成"托盘库有问题"或"embed 失败"。先查 tag。

## 2. 托盘图标必须传 ICO，不能传 PNG

`energye/systray`（v1.0.3，Windows 纯 Go 无 cgo）的 `SetIcon` 把字节写进
**无扩展名**的临时文件，再交给 Win32 `LoadImage` —— 后者只认 ICO/BMP。
传 PNG 只打一行极具误导性的日志：

```
unable to set icon: The operation completed successfully.
```

→ 生成 ICO 多尺寸帧（16/24/32/48/64/128/256）再 `//go:embed`。

## 3. exe 图标：用 go-winres 生成 .syso（本机没有 rc.exe）

```bash
go install github.com/tc-hib/go-winres@latest   # 需要联网
go-winres init                                   # 生成 winres/winres.json
# 把 icon.png 放进 winres/，编辑 winres.json 指向它
go-winres make --arch=amd64 --product-version=1.0.0.0 --file-version=1.0.0.0
# → 生成 rsrc_windows_amd64.syso，放在项目根目录，go build 会自动链接
```

`-H windowsgui` 去掉控制台闪烁。

## 4. 托盘与 Wails 共存：用 `systray.Run`，不要用 `RunWithExternalLoop`

`energye/systray` 的 Windows 实现里，`Register`（建托盘窗口+菜单）和 `nativeLoop`
（消息泵）**必须在同一 goroutine 连续执行**，否则点击事件收不到。

```go
go systray.Run(app.systrayReady, app.systrayExit)   // 整体一个 goroutine
err := wails.Run(&options.App{ /* ... */ })
if err != nil { log.Printf("界面失败: %v", err); select{} }  // 别让进程死
```

`HideWindowOnClose: true` + `StartHidden`（自启时 `--hidden`）实现"关窗收托盘"。

## 5. 外部 exe / 资产打包：embed 后必须解包到可写目录

`//go:embed all:embedded` 打进单 exe 没问题，但引擎类程序要写 `data/state.json`，
**只读的 embed FS 上跑不起来**。做法：首次启动解包到 exe 同级 `<name>_runtime/`，
大小一致的文件跳过（用户改过的 `config.json` / `auths/` 会被保留）。

启动子进程用独立进程组 + 隐藏窗口，这样父进程被回收后子进程仍能存活：

```go
cmd.SysProcAttr = &syscall.SysProcAttr{
    HideWindow: true, CreationFlags: 0x00000200, // CREATE_NEW_PROCESS_GROUP
}
```

停进程用 `taskkill /T /F /PID`，并用 `netstat -ano` 反查端口占用做兜底
（能接管"不是自己拉起"的实例）。

## 6. WebView2 `Process failed with kind N` 的含义

Wails 只打日志、不会自杀（源码：`internal/frontend/desktop/windows/frontend.go:530`）。
kind 对应关系（COREWEBVIEW2_PROCESS_FAILED_KIND）：

| kind | 含义 |
|---|---|
| 0 | browser process exited（致命，窗口出不来） |
| 1 | render process exited |
| 3 | frame render process exited |
| 4 | utility process exited |
| 6 | GPU process exited |

在**非交互式会话**（CI / 工具起的 shell / 无 GPU 沙箱）里常见 kind 4+6 循环后 kind 0。
**这不是代码 bug**：前台跑同一个二进制能稳定存活（实测 45s 不退出）。
判据：`timeout 45 ./app.exe` 前台跑，退出码 124（被 timeout 杀）＝程序本身没问题；
退出码 0 且很快返回 ＝ 真挂了。

## 6.1 ⚠️ kind 0 是硬退出，兜不住

```go
// internal/frontend/desktop/windows/frontend.go:531-539
case edge.COREWEBVIEW2_PROCESS_FAILED_KIND_BROWSER_PROCESS_EXITED:
    winc.Errorf(f.mainWindow, "%s", messages.WebView2ProcessCrash)
    os.Exit(-1)          // ← 无法拦
```

所以 `err := wails.Run(...); if err != nil { select{} }` 是**死代码**：
浏览器进程一挂，进程直接从回调里被干掉，`wails.Run` 根本不返回。
弹框文案可换：`windows.Options{Messages: &windows.Messages{WebView2ProcessCrash: "..."}}`。

## 6.2 根因常见于「未签名 DLL 被注入浏览器主进程」

查 Windows 事件日志 `Microsoft-Windows-CodeIntegrity/Operational`（ID 3033）：

```
Code Integrity determined that a process
(\Device\...\EdgeWebView\Application\<ver>\msedgewebview2.exe) attempted to load
\Device\...\<某程序>\...\tsbx.dll that did not meet the Microsoft signing level requirements.
```

特征与判据：
- 被拒的是**第三方 DLL**（不是 msedgewebview2 自己的），说明有程序往浏览器进程注入。
- 先排除 `AppInit_DLLs`（`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows`）
  与 IFEO（`...\Image File Execution Options\msedgewebview2.exe`）——两者为空则是
  **进程树内注入**，于是「**谁启动决定了会不会中招**」：
  从注入方派生的进程会中招，从资源管理器双击的不会。
- **`WebviewDisableRendererCodeIntegrity: true` 对此无效**（实测）。它加的是
  `--disable-features=RendererCodeIntegrity`，作用于渲染/工具进程；
  而拦截发生在**浏览器主进程**。别在这上面浪费时间。

### 必须准备一条不依赖 WebView2 的界面通路
因为拦不住 `os.Exit(-1)`，唯一可靠的兜底是：
1. 在 `wails.Run` **之前**启动引擎/业务逻辑（独立进程组，父进程死了还能活）；
2. 内置一个本地 HTTP 界面（如 `127.0.0.1:17863`），前端用 `fetch` 走同一套方法名；
3. 提供 `--web` 模式：完全跳过 `wails.Run`，托盘 + HTTP 服务 + 打开默认浏览器；
4. 检测到自己在注入方沙箱里（特征环境变量，如 `LSBOX_*`/`SANDBOX_CENTER_IPC_ADDRESS`）
   就自动切网页模式，避免每次启动弹崩溃框。


## 7. 排查手法：不要只看后台进程

用 `( ./app.exe & )` 起的后台进程**会在 Bash 工具调用之间被回收**，
看起来像"程序自己崩了"。要判断存活与否，**前台 + `timeout` + 看退出码**，
或者用工具的 `run_in_background: true`（进程受管，不会被回收）。

诊断期建议额外编一个**不带 `-H windowsgui`** 的控制台版，日志才看得见
（windowsgui 子系统下 `log.Printf` 全部丢进黑洞）。

## 8. 起服务/引擎后的验证（带凭据）

本机有 HTTP 代理，**curl 访问 localhost 必须加 `--noproxy '*'`**。
带 Bearer 才拿得到数据，否则返回 `invalid_api_key`：

```bash
curl -s --noproxy '*' -m 6 -H "Authorization: Bearer <key>" http://127.0.0.1:7863/status
```

## 9. 子进程输出的乱码：不要「非法就整段当 GBK」

Windows 上的中文控制台程序常按**字节数**对齐列宽，会把多字节字符截成半个：
实测 `获嘉青年` 的 `年`（UTF-8 `E5 B9 B4`）被切成 `E5 B9` + 空格 → 整段出现极少量非法序列。
此时若按「非法 → 整体 GBK 解码」，**正常的 UTF-8 中文会全部变成乱码**
（`获嘉青年` → `鑾峰槈闈掑`，因为 GBK 把 UTF-8 字节当双字节解）。

正确做法：先统计非法序列占比，少量才当截断修补：

```go
if utf8.Valid(b) { return string(b) }
bad := 0
for i := 0; i < len(b); {
    r, size := utf8.DecodeRune(b[i:])
    if r == utf8.RuneError && size == 1 { bad++ }
    i += size
}
if float64(bad)/float64(len(b)) < 0.05 {
    return strings.ToValidUTF8(string(b), "")   // 丢掉残缺字节，保留 UTF-8
}
// 否则才用 GBK 解码
```

## 10. 界面聚合多个子服务状态时（实测踩坑）

**a. 上游同族服务的响应字段可能不一致，必须容错解析。**
实测两个引擎：`wb2api` 的 `/status` 有 `total/healthy/cooling/disabled` 和
`credits_total/realm/credits_earliest_expiry`；`tw2api` **只有一个 `accounts` 数组**。
结构体解析后缺的字段是零值，**必须额外给一个 `creditsKnown bool`**：
否则界面上「上游没提供额度」和「额度真的是 0」长得一模一样，读数骗人。
汇总值（总数/健康数）也要在缺失时自行推导。

**b. 子服务的 Web 面板路径必须运行时探测，不能硬编码。**
实测：`wb2api` 的面板在 **`/panel/`**（`/panel` 301 跳转），**根路径 `/` 是 404**；
`tw2api` **完全没有面板**（只有 API）。
所以 `OpenPanel()` 要按 `/panel/` → `/` 顺序探测，命中才打开；
结果缓存（**成功 60s / 失败 10s** —— 引擎刚拉起时面板路由可能还没注册，
长缓存会让按钮一直不可用）。没面板的引擎返回明确错误，界面按钮置灰并给替代入口。

**c. Wails 的 `Width`/`Height` 是逻辑像素（DPI-aware）。**
本机系统缩放 150%，窗口 700×920 逻辑像素 ≠ 700×920 设备像素。
判断内容放不放得下**不要用命令行截图目测**（见 `web-visual-verify-headless`
的 dpr 坑：同尺寸两次截图元素能差 1.5 倍），用 CDP 的 `--eval` 量
`document.body.scrollHeight > clientHeight`。

**d. 动态信息（托盘提示 / 窗口标题）要「变化才刷新」。**
```go
systray.SetTooltip(tip)                    // 托盘悬停提示
wruntime.WindowSetTitle(a.ctx, title)      // 标题栏 + 任务栏悬停
```
状态轮询 5s 一次，不比较就去调会在托盘/窗口 API 上做无谓往返。

**e. 无原生窗口时（`--web` 模式）窗口类调用要短路。**
`WindowShow/WindowHide/Quit` 在 `ctx == nil` 或没有窗口时无效/会炸：
先判断 `hasWindow()`，"显示窗口"可退化为"用浏览器打开界面"，
"退出"则走自己的 shutdown + `os.Exit(0)`。

**f. 纯前端的小坑（这个界面踩过）**：日志区只写 `max-height` 时，
内容只有一行就会被压成一行高、版面跳动 —— 要配 `min-height`；
`button.pri:disabled` 必须单独写样式，否则主按钮在禁用态仍是醒目高亮。

---

## 11. 换配色（深 ↔ 浅）时必须同时改三处

前端 CSS 只改一层是不够的，另外两处在 Go 侧，漏了就出现「闪一下」和「割裂感」：

| 位置 | 写法 | 不改的症状 |
|---|---|---|
| 前端 `body` 底色 | `--bg:#f4f4f1` | —— |
| `options.App.BackgroundColour` | `options.NewRGBA(244,244,241,255)` | WebView2 起来之前窗口是一块**旧配色底色**，浅色界面闪黑 |
| `windows.Options.Theme` | `windows.Light`（或 `windows.Dark`） | 标题栏/系统控件仍按深色画，压在浅色页面上很割裂 |

**浅色下禁用态要重写，不能靠 opacity。** 深色里 `button:disabled{opacity:.45}`
还能看出是个按钮；浅色底上白底 + 半透明 = 空白占位符，用户以为渲染坏了。
要给明确的三件套：`background:surface-2; color:明度更低的灰; border-color:line`。
主按钮（`button.pri:disabled`）同样要显式覆盖成普通按钮外观。

**浅色主题的分层靠阴影，不靠描边。** 深色卡片常靠 1px 亮边分区；浅色下
`border:1px solid #e7e6e0` + `box-shadow: 0 1px 2px rgba(28,26,18,.05)`
比加深边框更干净。语义色也要换：`#34d399`（深色发光绿）在浅底上刺眼，
改用 `#12855a`；发光类 `box-shadow` 换成低透明度的「外环」`0 0 0 3px rgba(...,.14)`。

