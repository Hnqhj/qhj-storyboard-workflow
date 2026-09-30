---
name: web-visual-verify-headless
description: 用无头 Edge/Chromium 对本地网页做视觉验证与迭代——截图、诊断、定位布局与样式问题。当写/改完 HTML+CSS 页面需要"看一眼实际渲染效果"、需要验证视觉效果是否生效、或需要排查布局错乱时使用。触发：截图验证、看看效果、渲染出来什么样、视觉回归、无头浏览器验证网页。
agent_created: true
---

# 无头浏览器视觉验证网页

在 Windows 上用无头 Edge 对本地网页截图验证。核心目标是**可靠拿到"页面真实渲染的样子"**，
而不是凭代码想象。写 CSS/SVG 滤镜/动画这类"看不见效果"的代码时尤其必要。

## ⭐ 首选方案：CDP 验证器（几何相关的问题必须用它）

`msedge --headless --screenshot=... --window-size=W,H` 这条路有个**会误导判断的陷阱**：

> `--window-size` 是**窗口**尺寸，含浏览器 chrome（本机实测约 126px）。
> 实际视口比它小，于是截图底部多出一条 `html` canvas 底色。
> 你会以为"页面底部有一条色带 / 背景穿帮"，其实是截图工具的假象，真浏览器里没有。

CDP 方案用 `Emulation.setDeviceMetricsOverride` 精确设定视口，没有这个问题，
还能把 DOM 测量结果直接打回终端。**已经封装好，直接复制用**：

```
{项目}/.workbuddy/verify/shot.mjs
```

```bash
NODE="/c/Users/Administrator/.workbuddy/binaries/node/versions/22.22.2-3/node.exe"
"$NODE" .workbuddy/verify/shot.mjs --url "http://127.0.0.1:8788/index.html?theme=day" \
  --out _s1.png --w 1440 --h 900 --wait 2600
```

| 参数 | 用途 |
|---|---|
| `--w --h` | **精确视口**（不是窗口尺寸） |
| `--dpr 2` | 高倍截图。**判断细节质感必须用它** |
| `--clip x,y,w,h` | 真实裁切，配合 `--dpr 2` 就是放大镜。**图像的像素坐标 = `(css坐标 - clip起点) × dpr`** |
| `--full` | 整页长图 |
| `--wait ms` | 等 JS / 动画 / 滤镜建好贴图 |
| `--eval "<js>"` | 在页面里求值并把结果打回 terminal，可重复多次。**支持返回 Promise（会自动 await）** |
| `--print` | 用打印媒体查询渲染，用来验证 `@media print` |

### ⚠️ 这个工具自身的四个坑（都在真机上踩过）

**1. `clip.scale` 不能再乘一次 DPR。**
`Emulation.setDeviceMetricsOverride` 的 `deviceScaleFactor` 已经让整页按 DPR 渲染，
`Page.captureScreenshot` 的 `clip.scale` 若再传 DPR，会得到 **`dpr²` 倍**的图
（`--dpr 2 --clip 720,0,720,230` 本该是 1440×460，实际出 2880×920）。
后果不只是文件大：**按 `×dpr` 换算的采样坐标会全错一倍**，量化分析直接失效。
→ `shotArgs.clip = { x, y, width, height, scale: 1 }`。

**2. 必须禁用缓存。**
profile 是持久复用的，改了 `app.js` / `styles.css` 后浏览器可能仍用旧文件，
表现是"改了参数完全没变化"，**极容易误判成"这个参数没用"**：
```js
await cdp.send('Network.enable');
await cdp.send('Network.setCacheDisabled', { cacheDisabled: true });
```

**3. `--eval` 的表达式不能直接 `JSON.stringify()`。**
如果表达式返回的是 Promise，`JSON.stringify(promise)` 会先同步序列化成 `"{}"`，
`awaitPromise: true` 就白设了 —— 你会看到 `{}` 而不是结果，
然后误以为是"页面里没这个数据"。正解是先摊平再序列化：
```js
const wrapped =
  'Promise.resolve((function(){ try { return (' + expr + '); } ' +
  'catch(e){ return "ERR " + e.message; } })()).then(' +
  'function(v){ return typeof v === "string" ? v : JSON.stringify(v); },' +
  'function(e){ return "ERR " + (e && e.message); })';
await this.send('Runtime.evaluate', { expression: wrapped, returnByValue: true, awaitPromise: true });
```
有了这个，`--eval` 就能等页面里的异步动作（点击后的过渡、rAF、setTimeout）：
```bash
--eval "(function(){return new Promise(function(r){document.querySelector('#themeBtn').click();
  setTimeout(function(){r({theme:document.documentElement.dataset.theme});},1000);});})()"
```
⚠️ 只点一下、紧接着用**第二个 `--eval`** 去读结果是不行的 —— 两次求值之间只隔几毫秒，
异步回调还没跑，你会读到切换前的值。

**4. 做量化之前，先自检坐标系。**
先用差分图确认"我采样的区域确实是我想测的那个元素"，再开始量：
```python
from PIL import Image, ImageChops
d = ImageChops.difference(Image.open(a).convert('RGB'), Image.open(b).convert('RGB')).convert('L')
print(d.getbbox(), d.getextrema())   # bbox 为 None = 两张图完全一样 → 说明改动没生效/采错区域
```
本机实测：坐标算错一倍时，五组截然不同的参数会量出**完全相同**的读数，
如果不去自检，就会得出"参数没用"的错误结论。

**硬性经验：判断"好不好看"必须放大到 2x DPR + 局部裁切看。**
整页缩略图会把所有位移、边缘、1px 发丝线的细节全糊掉 ——
本机实测：整页图看不出问题，2x 裁切图立刻暴露"折射带被推出元素之外"。

```bash
# 放大镜用法：只截 tab 那一块，2 倍像素
"$NODE" .workbuddy/verify/shot.mjs --url ".../index.html" --out _z.png \
  --w 1440 --h 900 --dpr 2 --clip "370,0,700,180" \
  --eval "(function(){document.querySelector('#worksScroll').scrollTop=150;return 1;})()"
```

`--eval` 拿几何比截图猜快得多：

```bash
--eval "(function(){const R=s=>{const n=document.querySelector(s);const r=n.getBoundingClientRect();return Math.round(r.left)+','+Math.round(r.width);};return R('#seg')+' | '+R('#dock');})()"
```

**`--eval` 里滚动某一段（而不是整页）也是安全的**，因为分段滚动的容器不是
`position: fixed`，不受下面第 3 步那个假象影响。

## 第 0 步：先探测环境（别假设）

```powershell
# Edge 路径（本机实测在 x86 目录下）
Test-Path "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
# C 盘可用空间（无头浏览器会写缓存，满盘会让整条工具链瘫痪）
(Get-PSDrive C).Free
```

**⚠️ `--user-data-dir` 必须放在数据盘（如 G:），绝不能放 `$TMP`（在 C:）。**
反复用 `$TMP` 起无头浏览器会把 C 盘写满，之后 Bash / PowerShell / Node 全部报
`ENOSPC`，看起来像"工具坏了"，极难定位。

## 第 1 步：起本地静态服务器

`file://` 下相对路径的 `<script src>` / `<link>` 通常能加载，但中文路径 + 命令行编码
容易出问题，**用 HTTP 服务器最稳**：

```powershell
Set-Location "G:\工作\my-project"
& "C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\python.exe" -m http.server 8788 --bind 127.0.0.1
# run_in_background = true
```

## 第 2 步：截图（备用方案：命令行 `--screenshot`，一次跑多张）

⚠️ 只在**不关心几何精度**（只要个大概样子）时用。几何/对齐/背景穿帮类问题走上面的 CDP 方案。

```powershell
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
function Shot($url, $file, $w, $h, $d) {
  $a = @(
    "--headless=new","--no-proxy-server","--no-first-run","--no-default-browser-check",
    "--disable-sync","--disable-extensions","--enable-unsafe-swiftshader","--hide-scrollbars",
    "--user-data-dir=G:\path\to\.edge-tmp","--disk-cache-dir=G:\path\to\.edge-tmp\cache",
    "--window-size=$w,$h","--force-device-scale-factor=$d","--virtual-time-budget=9000",
    "--force-prefers-reduced-motion","--screenshot=$file",$url
  )
  & $edge @a 2>&1 | Out-Null
}
Shot 'http://127.0.0.1:8788/' "G:\path\to\_s1.png" 1500 950 1
```

### 关键参数为什么这么写

| 参数 | 作用 / 不写会怎样 |
|---|---|
| `--headless=new` | 新版无头模式，支持 backdrop-filter 等合成特性 |
| `--enable-unsafe-swiftshader` | 无 GPU 时用软件合成。**不要用 `--disable-gpu`**，会让 backdrop-filter / filter 失效 |
| `--no-proxy-server` | 本机常有 HTTP 代理，不写会连不上 127.0.0.1 |
| `--force-prefers-reduced-motion` | **最有用的一个**：CSS 动画直接落终态，截图稳定不闪。前提是页面里写了 `@media (prefers-reduced-motion: reduce)` 兜底 |
| `--force-device-scale-factor` | <1 可截超长视口（配合大 window-size）；2~3 可做高倍细节截图 |
| `--virtual-time-budget=9000` | 等 JS 跑完。太短会截到未初始化状态 |
| `--user-data-dir` / `--disk-cache-dir` | 隔离 profile，放数据盘 |
| 末尾 URL **用单引号** | URL 里的 `&` 在 PowerShell 双引号里可能被解析出问题 |

## 第 3 步：拿到"页面下方"的内容（最大的坑）

**`position: fixed` 元素在无头滚动截图下会错位**——背景、导航会停在文档顶部，
截出来一片黑/白，让你误判成布局 bug。

**正确做法：不要滚动，把目标区块提到页面顶部。**
在页面里加一个调试参数（`app.js` 里已有实现可参考）：

```js
const q = new URLSearchParams(location.search);
if (q.has('only')) {
  const sec = String(q.get('only')).replace(/[^a-z]/gi, '');
  const s = document.createElement('style');
  s.textContent = 'main > section:not(#' + sec + '){display:none!important}' +
                  '.hero{min-height:auto!important;padding-block:100px 40px!important}';
  document.head.appendChild(s);
}
```

然后 `?only=works` 截图，区块就在 y=0，不需要滚动。
同理 `?open=<id>` 可直接打开弹层、`?filter=x` 触发筛选、`?theme=light` 切主题——
**用 JS 主动触发状态，比模拟用户操作可靠得多**。

## 第 4 步：诊断（截图不对劲时）

先别改代码，先抓 DOM——区分"渲染问题"和"代码问题"：

```powershell
$dom = & $edge @dumpArgs 2>&1 | Out-String   # 参数同 Shot，把 --screenshot 换成 --dump-dom
"cards = " + ([regex]::Matches($dom, 'class="work glass')).Count
"light theme => " + ($dom -match 'data-theme="light"')
```

再在页面里挂一个 `?debug=1` 的角标面板，直接打印运行时状态
（能力检测结果、生成的元素数、`getComputedStyle` 取到的实际值）。
比反复猜快得多。

## 第 4.5 步：当"看"不够时——用像素量化

审美可以靠眼睛，但"某某感有点强""不够深/不够浅"这类反馈**靠眼睛调参效率极低，
而且很容易归错因**。做法：先做一个「裸基线」（把所有待测的装饰层撤掉，露出原始背景），
再用 Pillow 对同一区域算指标。

```python
# 关键：不要凭印象取坐标，先在 2x 裁切图上确认元素的实际像素范围
im = Image.open(path).convert('RGB'); px = im.load()

def patch(im, x, y, n=5):        # 邻域平均，抗噪
    ...                          # 返回 (r,g,b)

def local_std(im, x0, x1, y0, y1):   # 局部对比度 = 相邻像素梯度均值
    ...                              # 模糊会让它骤降；是判断"糊没糊"的硬指标
```

三个万能指标：

| 指标 | 算法 | 读法 |
|---|---|---|
| **偏色/遮盖量** | 处理后 vs 基线同点位的平均 ΔRGB | 量化"加了多少层" |
| **细节保留率** | 局部对比度（处理/基线） | **<0.4 = 糊了**，>0.8 正常 |
| **位移量** | 两列像素做互相关，求最佳偏移 | 判断"是位移还是模糊" |

```python
def best_shift(ref, test, y_in, win=10, maxlag=20):
    def err(lag):
        s = n = 0
        for t in range(-win, win + 1):
            a, b = y_in + t, y_in + t + lag
            if 0 <= a < len(ref) and 0 <= b < len(test):
                s += sum(abs(test[b][k] - ref[a][k]) for k in range(3)); n += 1
        return s / max(n, 1)
    return min(range(-maxlag, maxlag + 1), key=err)
```

**这套方法最值钱的地方是"排除法"**：本机实测过一个案例，用户说"磨砂感有点强"，
量化后发现目标元素的细节保留率 0.86、遮盖量≈0 —— **根本不是它的问题**，
真正的元凶是另一个叠层。若一开始就去调它的参数，会白忙很久。

## 第 5 步：清理（别把验证残留留在交付目录）

本机回收站不可用，`rm` 守卫对非 Temp 路径会 fail-closed。**单个文件用 .NET 直删，不需要批准**：

```powershell
[System.IO.File]::Delete($path)
Get-ChildItem "$dir\_*.png" | ForEach-Object { [System.IO.File]::Delete($_.FullName) }
[System.IO.Directory]::Delete("$dir\.edge-tmp", $true)   # 目录可能需要用户批准
```

验证用的临时文件统一加 `_` 前缀，清理时一条通配符搞定。
**交付目录最后只应剩下真正的交付物**。

## 注意

- **PowerShell 工具不回显 stdout**，把结果写进临时文件再读。
- 逐字/逐项动画的入场元素在动画未跑完时是"不可见"的——用
  `--force-prefers-reduced-motion` 绕开，不要去调大 `--virtual-time-budget` 硬等。
  走 CDP 方案时更简单：页面里本来就有 `@media (prefers-reduced-motion: reduce)` 兜底，
  直接等 `--wait` 或在 `--eval` 里给元素补 `.is-in` 即可。
- 缓存问题已经由 CDP 方案的 `Network.setCacheDisabled` 解决，**不要再靠"删 profile 重跑"**。
- 页面里加 `?theme=` `?only=` `?filter=` `?open=` `?debug=1` 这类**调试参数**很划算：
  用 JS 主动把页面切到目标状态，比模拟点击/滚动可靠得多，也让截图脚本能一条命令复现。
  再配一个每次都注入的 `?bare=1`（撤掉装饰层）就能把「视觉判断」升级成「数值判断」。
