---
name: web-liquid-glass-refraction
description: 在网页上实现「真液态玻璃」——背景像素被边缘弯折的折射效果，而不是一层模糊。当需要 Apple Liquid Glass / 毛玻璃升级 / backdrop-filter 折射 / 玻璃拟态（glassmorphism）做出高级感，或现有的"液态玻璃"被评价为"其实就是磨砂玻璃、很土"时使用。触发：液态玻璃、liquid glass、玻璃拟态、毛玻璃、backdrop-filter、折射、feDisplacementMap、玻璃质感。
agent_created: true
---

# 网页真液态玻璃（折射）

## 先纠正一个常见误判

**`backdrop-filter: url(#svgfilter)` 在 Chromium 里是真的生效的。**
用 `CSS.supports('backdrop-filter','url(#f)')` 检测返回 `true`，并且像素级确实位移了。

实测对照（Edge / Chrome 145，竖条纹背景 + 大字）：

| 滤镜 | 渲染结果 |
|---|---|
| `blur(7px)` | 条纹糊成均匀灰 → **这就是磨砂玻璃** |
| `url(#lens)` | 条纹向内弯折成同心环、字形被拉伸 → **真折射** |
| `url(#wobble)`（feTurbulence） | 条纹呈液态波纹扭曲 |

所以当用户说"这不是液态玻璃，是磨砂玻璃"时，**问题几乎从来不在技术支不支持**，
而在**参数和质感层设计不对**。按下面的顺序排查，不要先去换技术方案。

## 真折射的三层结构

一块像样的玻璃由三层叠出来，缺一层就会退化成模糊：

1. **折射层**（`backdrop-filter`）：背景位移 + 轻微模糊
2. **玻璃体的料**（元素的 `background` + `::before` 渐变）：极淡的上下渐变，
   上沿亮、下沿稍暗，给玻璃"厚度"
3. **边缘层**（`box-shadow`）：`inset 0 1px 1px` 上沿强高光 + 四边弱高光 + 外投影托浮
   ＋**`0 0 0 1px` 极淡外描边**

> ⚠️ 最后那圈外描边不能省。浅色底上纯白高光**完全看不见**，
> 玻璃会直接消失，看起来像"页面上凭空飘了几个字"。

## 参数标定（已用对照实验验证，直接用）

```js
const G = {
  band:   0.26,   // 折射带宽度 = min(w,h) × band
  power:  3.2,    // 衰减幂，越大越集中在最边缘
  scaleF: 0.38,   // 最大位移 = min(w,h) × scaleF  ← 磨砂感的主开关
  maxScale: 46,   // 位移上限 px
  blur:   0.4,    // 次表面散射
  sat:    1.7,    // 透过玻璃的颜色增饱和（见下）
  res:    0.5     // 贴图分辨率倍率
};
```

| band | scaleF | blur | 观感 |
|---|---|---|---|
| .26 | .38 | 0.4 | **边缘弯折明显、内部清晰 ← 采用** |
| .32 | .115 | 1.5 | 太柔，看着像磨砂（旧版参数） |
| .42 | .065 | 1.5 | 完全退化成模糊 |
| .20 | .15 | 0.5 | 位移方向感偏弱 |

### ⚠️ 修正一条流传很广的错做法：细长元素不是「位移要小」

网上常见的推理是「吸顶标签栏很矮（40–55px），折射带占了高度的大头，
所以位移要调小」——**这个推理是错的，而且正是"液态玻璃做成磨砂玻璃"的主因**。

真实原因在于：`feDisplacementMap` 的 `scale` 属性映射到的是 **`[-scale/2, +scale/2]`**，
所以实际位移只有 `scale` 的一半。给一个 45px 高的标签栏配 `scaleF .072`，
算出来 `scale ≈ 3px`，**实际位移 1.5px** —— 小于 2px 的位移肉眼等于没有，
剩下的就只有 `blur` 了，那就是一块磨砂玻璃。

**正解：细长元素照旧给足位移（`scaleF .38`，45px 高 → `scale 17px`，实际 ±8.5px），
真正要收窄的是 `band`。** 矮元素用 `band .26` 而不是 `.32`，
让强位移集中在最外面 3–4px，中间依然锐利。

```js
const thin = m < 90;                    // 吸顶栏 / 底部工具条
const scale = Math.round(clamp(m * (thin ? G.scaleF : G.scaleF * 0.7), 3, G.maxScale));
const blur  = G.blur;                   // 不要给 thin 单独加 blur
```

### `saturate()` 是消掉「死奶白」的关键

玻璃底色是一层半透明纸色（`color-mix(--bg …)`），它会拉低透过来颜色的纯度，
于是整块看起来发灰发白 = 磨砂感。**在 `backdrop-filter` 里补一道增饱和**：

```js
el.style.backdropFilter =
  `blur(${blur}px) saturate(${G.sat}) url(#${id})`;   // 顺序即物理顺序
```

1.7 左右足够；补上之后可以放心把底色再降一档，玻璃感和可读性同时拿回来。

### `blur` 必须接近 0

`blur > 1px` 在 45px 高的元素上就是肉眼可见的糊。
`blur 0.4px` 已经是「次表面散射」的量级，再多就不叫散射叫磨砂了。
**想让背景"柔"一点不能靠 blur，要靠缩小 `scale` 或收窄 `band`。**

## 玻璃的透明度由「它压着什么」决定（比参数更重要）

同一套玻璃参数，压画面和压文字是**两套完全不同的取值**。
写错这一条，效果会从"高级"直接掉到"穿帮"。

| 玻璃压着的东西 | 底色 | 理由 |
|---|---|---|
| **画面**（图片、封面、视频） | `color-mix(in srgb, var(--bg) 30%, transparent)` | 透一点才像玻璃；不透就是一块板 |
| **正文**（滚动经过的文字） | `color-mix(in srgb, var(--bg) 88%, transparent)` | 文字被切一半看起来就是坏了，可读性优先 |

用同一个变量按元素给不同值，不要复制两套 `.glass` 规则：

```css
.glass { --tint-el: var(--tint); background: var(--tint-el); }
.seg   { --tint-el: color-mix(in srgb, var(--bg) 30%, transparent); }  /* 压作品封面 */
.dock  { --tint-el: color-mix(in srgb, var(--bg) 88%, transparent); }  /* 压正文 */
```

**同理，玻璃上的文字颜色不能用次级色。** 次级色（如 `--mid: #7b756c`）
压在中间调的玻璃上对比度只有 ~2:1，根本读不出来：

```css
.seg__b { color: color-mix(in srgb, var(--text) 68%, transparent); }
/* 用"正文色的透明度"代替次级色 —— 无论玻璃底下是浅底还是深底都站得住 */
```

**高光/渐变要走变量**，否则子元素想单独调会被更高优先级的主题规则压回去：

```css
.glass::before { background: var(--sheen, <默认>); }
.glass::after  { background: var(--spec,  <默认>); }
html[data-theme='night'] .glass { --sheen: …; --spec: …; }   /* 特异性 0,2,0 */
.seg { --sheen: …; }   /* 0,1,0，能生效，因为 `html[data-theme]` 只覆盖 .glass 的默认值 */
```

## 形状：优先做「紧凑胶囊」，不要通栏玻璃条

通栏的玻璃条有两个问题：**右侧一大片玻璃没有任何内容，纯粹在挡画面**；
而且**玻璃面积越大、白纱总量越大，越像一块奶白板**。

```
.seg { width: max-content; }   /* 包住内容即可 */
```

胶囊形式才是液态玻璃的正统形态：小、厚、边缘折射明显。
如果设计上确实需要通栏（例如整行都要可点），就把高度压矮、`band` 收窄，
并且接受它会更像一条「材质带」而不是一块玻璃。

## 位移贴图（canvas 逐像素）

R 通道 = x 位移，G 通道 = y 位移，128 = 不位移。边缘处采样点朝内侧偏移。

```js
/* 圆 / 胶囊 / 圆角矩形由同一条 SDF 统一覆盖 */
function buildMap(w, h, r, band, power, res) {
  const W = Math.max(2, Math.round(w * res));
  const H = Math.max(2, Math.round(h * res));
  const c = document.createElement('canvas'); c.width = W; c.height = H;
  const ctx = c.getContext('2d');
  const img = ctx.createImageData(W, H); const px = img.data;

  const R  = Math.min(r, Math.min(w, h) / 2);
  const bw = Math.max(2, Math.min(w, h) * band);
  const cx = w / 2, cy = h / 2;

  for (let y = 0; y < H; y++) {
    const Y = (y + 0.5) / res;
    const qy = Math.abs(Y - cy) - (cy - R);
    for (let x = 0; x < W; x++) {
      const X = (x + 0.5) / res;
      const qx = Math.abs(X - cx) - (cx - R);

      // ⚠️ 末尾的 - R 不能漏
      const d = Math.hypot(Math.max(qx, 0), Math.max(qy, 0))
              + Math.min(Math.max(qx, qy), 0) - R;

      const t = Math.min(1, Math.max(0, 1 - d / bw));
      const f = t <= 0 ? 0 : Math.pow(t, power);

      const dx = X - cx, dy = Y - cy;
      const L = Math.hypot(dx, dy) || 1;
      const i = (y * W + x) * 4;
      px[i]     = 128 - (dx / L) * f * 127;
      px[i + 1] = 128 - (dy / L) * f * 127;
      px[i + 2] = 128;
      px[i + 3] = 255;
    }
  }
  ctx.putImageData(img, 0, 0);
  return c.toDataURL('image/png');
}
```

`res 0.5` 是安全的：位移场本身平滑，半分辨率贴图肉眼无差，开销省 4 倍
（`feImage preserveAspectRatio="none"` 会把它拉伸回去）。

## ⚠️ 两个会让折射悄悄失效的几何陷阱

这两个都**看不出报错**，只表现为"效果很土"，靠肉眼排查极难。

### 陷阱 1：`<feImage>` 会铺满整个滤镜区域

`feImage` 不写 `x/y/width/height` 时，几何默认铺满**滤镜区域**（filter region），
不是元素框。而滤镜区域默认是 `-10% / 120%`。

如果把滤镜 region 写成 `x=-14% width=128%`，位移贴图就被**拉伸 1.28 倍并整体偏移**，
横向的折射带直接被推出元素之外。表现：**整条被抹平 + 左右不对称**。

**正解：滤镜区域严格等于元素框。**

```js
f.setAttribute('x', '0');        f.setAttribute('y', '0');
f.setAttribute('width', '100%');  f.setAttribute('height', '100%');
```

在 Chromium 上试过写 `x=-14%`（看起来能扩大滤镜输出范围，是常见直觉），是错的。
**只有用棋盘格背景做 A/B 对照才能看出来**：region `0/100%` 保留了清晰的格子结构，
region `-14%/128%` 整条糊成平滑渐变。

### 陷阱 2：圆角矩形 SDF 漏掉 `- R`

漏掉圆角半径那一项会让整个距离场偏移，**在长胶囊上表现为一圈"菱形锯齿"伪影**
（边缘出现锯齿状的斜向花纹，而不是干净的环形折射带）。
补上 `- R` 之后，圆 / 胶囊 / 圆角矩形由同一条式子统一覆盖，
**不再需要单独判断形状**（早期版本用 `Math.abs(w-h) < 4 && radius >= ...` 去猜是不是圆，
既脆弱又容易把长胶囊误判成圆形）。

## 完整应用

```js
function makeFilter(id, w, h, r, scale) {
  const NS = 'http://www.w3.org/2000/svg';
  const f = document.createElementNS(NS, 'filter');
  f.setAttribute('id', id);
  f.setAttribute('x', '0'); f.setAttribute('y', '0');
  f.setAttribute('width', '100%'); f.setAttribute('height', '100%');
  f.setAttribute('color-interpolation-filters', 'sRGB');

  const im = document.createElementNS(NS, 'feImage');
  im.setAttribute('href', buildMap(w, h, r, G.band, G.power, G.res));
  im.setAttribute('preserveAspectRatio', 'none');
  im.setAttribute('result', 'map');

  const dm = document.createElementNS(NS, 'feDisplacementMap');
  dm.setAttribute('in', 'SourceGraphic');
  dm.setAttribute('in2', 'map');
  dm.setAttribute('scale', String(scale));
  dm.setAttribute('xChannelSelector', 'R');
  dm.setAttribute('yChannelSelector', 'G');

  f.appendChild(im); f.appendChild(dm);
  document.querySelector('.lg-defs').appendChild(f);   // 页面里的 <svg class="lg-defs">
}

function applyGlass(el) {
  const w = el.offsetWidth, h = el.offsetHeight;
  if (w < 10 || h < 10) return;
  const r = parseFloat(getComputedStyle(el).borderTopLeftRadius) || 0;
  const m = Math.min(w, h);
  const thin = m < 90;                                   // 吸顶栏 / 工具条
  const scale = Math.round(Math.min(G.maxScale, Math.max(3, m * G.scaleF)));
  const blur  = G.blur;                                  // 不要给 thin 单独加 blur

  // ⚠️ 缓存键必须带上 band/power —— 否则调参时命中旧贴图，
  //    会误判成「改了参数没反应」
  const key = `${w}_${h}_${Math.round(r)}_${scale}_${G.band}_${G.power}`;
  let id = cache.get(key);
  if (!id) { id = 'lg' + (++uid); makeFilter(id, w, h, r, scale); cache.set(key, id); }

  // 顺序即物理顺序：先次表面散射 → 增饱和 → 边缘透镜
  el.style.backdropFilter = `blur(${blur}px) saturate(${G.sat}) url(#${id})`;
}
```

容器必须是**零尺寸但存在**的 SVG：

```html
<svg class="lg-defs" aria-hidden="true" width="0" height="0"></svg>
```
```css
.lg-defs { position: absolute; width: 0; height: 0; overflow: hidden; }
/* ⚠️ 绝不能用 display:none —— 那会让整条滤镜链失效 */
```

尺寸变化要重建（`ResizeObserver` + `resize`，防抖 90ms），
字体加载完也要重建一次（`document.fonts.ready`），因为文字宽度会变。

### ⚠️ 元素尺寸**每帧都在变**时（拖拽中的框选矩形 / 拖拽预览），防抖救不了

单帧重建 = createImageData 逐像素 SDF + toDataURL 编 PNG + 重建滤镜链，
实测 10~25ms —— 拖动直接掉到 30fps 以下。解法是**量化缓存**：

1. 尺寸先量化到 8px 网格（`Math.round(w/8)*8`）再查缓存。真实拖动每帧只挪
   几个像素，绝大多数帧直接命中缓存、一次都不重建。
2. 贴图 `preserveAspectRatio="none"` 拉回元素精确尺寸 —— ≤8px 的拉伸误差
   （480px 上 1.7%）肉眼看不出来。
3. ResizeObserver 回调里只读 `borderBoxSize`（**别碰 offsetWidth**，强制 layout）；
   圆角读一次进 WeakMap。
4. 缓存上限几十条，超了整套丢弃重建。
5. 另外注意：**Chromium 会把 `url(#x)` 序列化成 `url("#x")`（带引号）**——
   验收探针的正则要容引号，别写成 `/url\(#x\)/` 然后误判成没生效。

实例：nexusvault-post 的框选矩形曾用本方案（量化缓存，探针 12/12 PASS）；
后来用户终判「不要液态效果」改回纯 CSS 磨砂（`blur(6px) saturate(1.15)` + 极低着色），
折射模块整套删除。教训：折射在大面积板 + 高对比内容上容易显脏（残影像撕裂），
且用户审美只能实机确认 —— 大改动先出最便宜的一版让用户做加减法。

## 降级与开关

```js
const SUPPORTS = CSS.supports('backdrop-filter', 'url(#x)');
```

不支持时加 `html.no-refract`，CSS 里退回纯磨砂：

```css
html.no-refract .glass { backdrop-filter: blur(15px) saturate(180%); }
```

**另外给用户一个 `C` 键 / 按钮手动切换玻璃**（关掉后走同一套降级）。
既方便 A/B 对比，也是低配设备的逃生口。

## 用在哪里

玻璃要**盖在有内容滚动经过的位置**才有意义——背景是纯色时折射看不见。

- ✅ 吸顶的标签栏 / 分段控制器（作品从底下滚过）
- ✅ 底部浮动工具条（正文从底下滚过）
- ✅ 弹层与卡片的边缘
- ❌ 静态的标题、正文块、分隔线 → 用纯 CSS 点缀，别用玻璃

**"液态玻璃不要全部使用"是对的方向**：玻璃面越多，越廉价。
一两处真折射 + 别处的纯 CSS 质感，比满页玻璃高级得多。

## 先量化，再调参（不要靠肉眼）

「磨砂感有点强」这种反馈，肉眼调参效率极低，而且很容易**归错因**——
实测过一例：标签栏玻璃的白纱量≈0、锐度保留 0.86，**玻璃本身根本不糊**；
真正的"磨砂感"来自封面上的半调网点叠层和整体被压进中间调的调色。
如果一开始就去改玻璃参数，永远调不好。

**三步定量法**（先做一个「裸基线」：撤掉玻璃的料层与折射，露出原始背景）：

```css
/* 用 ?bare=1 之类的方式注入 */
html.bare [data-glass] {
  background: none !important; backdrop-filter: none !important; box-shadow: none !important;
}
html.bare [data-glass]::before, html.bare [data-glass]::after { background: none !important; }
```

> ⚠️ **选择器要用 `[data-glass]`，不能只写 `.glass`。** 玻璃元素的 class
> 常常是分开挂的（比如标签栏只有 `.seg`、工具条才有 `.glass`），
> 只匹配 `.glass` 会让基线里仍然留着 blur，量出来全是 0，白忙一场。

然后对同一块区域量三个数（在 2x DPR 裁切图上算）：

| 指标 | 算法 | 判据 |
|---|---|---|
| **白纱量** | 玻璃区 vs 基线同点位的平均 ΔRGB | 越低越好；>8 说明底色太重 |
| **锐度保留** | 局部对比度（相邻像素梯度均值）玻璃/基线 | **<0.4 = 磨砂**；>0.8 正常 |
| **边缘位移** | 玻璃列与基线列做互相关，求最佳垂直位移 | 顶边 ≠ 0 且正中 ≈ 0 = **真折射** |

三个数一起看才能定位问题：白纱高 + 锐度低 = 底色太重；
白纱低 + 锐度高 + 位移≈0 = 参数没生效（先查缓存键和滤镜区域）；
三者都正常但用户仍说"磨砂" = **问题不在玻璃身上，去查别的叠层**。

调参时给 `G` 加个 URL 覆盖（`?g=band,power,scaleF,blur,sat`），
一次运行就能拍多组对照，不用反复改文件。

## 验证（放大看）

玻璃的位移细节在整页截图上**看不出来**，必须 2x DPR + 局部裁切：

```bash
node {项目}/.workbuddy/verify/shot.mjs --url "<url>" --out _z.png \
  --w 1440 --h 900 --dpr 2 --clip "370,0,700,180"
```

判定标准（用棋盘格或高对比条纹做背景）：
1. 左右两端的弯折**等量对称**
2. 上下边缘的弯折**对称**
3. 内部区域**保持清晰锐利**，只有边缘一圈在弯

第 3 条是关键：如果整条都被抹平，就是**陷阱 1**（滤镜区域不匹配）或 scale 太大。
详见 skill `web-visual-verify-headless`。

## 反例清单（做完自查）

- [ ] 滤镜区域是不是写成了 `-14% / 128%`？→ 改回 `0 / 100%`
- [ ] SDF 末尾的 `- R` 有没有漏？
- [ ] 边框圆角是不是只靠 `border-radius`、贴图却按直角矩形算？
- [ ] **`blur` 是不是 > 1px？**→ 降到 0.4 上下；想让背景柔就收 `band`，不是加 blur
- [ ] **细长元素是不是只给了 `scaleF .07` 左右？**→ 那实际位移不到 2px＝没折射。
      记住 `scale` 映射到 `[-scale/2, +scale/2]`，矮元素要照旧给 `.3–.4`
- [ ] `backdrop-filter` 里有没有 `saturate(1.7)`？没有就会是"死奶白"
- [ ] 底色是不是按「压画面 / 压正文」分别取的？（~30% vs ~88%）
- [ ] 玻璃上的文字是不是用了次级色？→ 改 `color-mix(--text 68%)`
- [ ] `--sheen / --spec` 有没有走变量？否则子元素调不动高光
- [ ] 浅色底上有没有那圈 `0 0 0 1px` 外描边？没有的话玻璃会隐形
- [ ] 玻璃条是不是通栏但右侧空着？→ 改 `width: max-content` 做紧凑胶囊
- [ ] 缓存键里有没有 `band` / `power`？漏了会导致"改了参数没反应"
- [ ] 玻璃是不是铺得太多了？
- [ ] **说"磨砂"之前，先量化白纱量 / 锐度保留 / 边缘位移** ——
      确认问题真的出在玻璃上，再去查封面叠层、网点、调色和整体灰度
