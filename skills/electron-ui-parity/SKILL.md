---
name: electron-ui-parity
agent_created: true
description: Electron UI 对齐：用 CDP 从运行中的 Electron/Chromium 应用提取真实设计规格（tokens、计算样式、几何、窗口与拖拽行为），移植到另一个前端使两者逐值一致；也校验无边框窗口拖拽区与「点了没反应」的交互。 Extract the real design spec (tokens, computed styles, geometry, window/drag behaviour) from a RUNNING Electron or Chromium app via CDP, and port it to another frontend so the two match value-by-value. Also verifies frameless-window `-webkit-app-region` drag regions, and diagnoses UI state changes that "do nothing" (router-key remounts, CDP false failures). Use when the user says a UI "should look like" another app, asks to align/parity/unify two frontends, wants a design audit of a packaged Electron app, reports that a frameless window cannot be dragged, or reports that a UI interaction has no visible effect.
---

# Electron UI Parity via CDP

Comparing screenshots by eye is unreliable. Measure the reference app instead: connect to it
over CDP, read computed styles and geometry, then write an override layer that matches.

## 0. Decide what the reference actually is

Before measuring, confirm the reference binary/page. Common traps:

- A packaged app's `app.asar` may already have been overwritten by an auto-updater.
  Check `md5sum app.asar app.asar.bak-*` — **identical hashes mean the backup is not a
  pre-change snapshot**, so it tells you nothing about "before".
- A `*.rd-bak` / `*-backup` folder may hold the *post*-change state, not the original.
- Grep the reference's own CSS for its design-token prefix (`--rd-`, `--accent-`, …).
  If both apps define the same prefix but with different values, the reference is a
  newer iteration of the same design system — that is the thing to port.

## 1. Run the reference app

```bash
# borrowed Electron from another project, app dir as the entry
cd "<app-dir>"
"<electron>/dist/electron.exe" . --no-sandbox --disable-gpu --in-process-gpu --remote-debugging-port=9333
```

- `--no-sandbox --disable-gpu --in-process-gpu` are needed on GPU-less / virtualised Windows
  hosts, all three together. Do **not** add `--disable-software-rasterizer` (blank window).
- Native-module ABI errors (`NODE_MODULE_VERSION 140 vs 135`) and `spawn EPERM` are usually
  non-fatal — the UI still renders.
- Launch it with `run_in_background`; a normal tool call kills the process group on return.

## 2. Probe it

Use `scripts/cdp-probe.mjs` (no npm deps — Node 22+ global `WebSocket`).

```bash
node scripts/cdp-probe.mjs <port> <out.png>            # target list + meta + screenshot
node scripts/cdp-probe.mjs <port> <out.png> "<js expr>"  # run your own expression
```

It prints every target's `type | title | url` first. Always read that line — a page may be
blank, or you may be attached to the wrong target.

For a full style dump, pass an expression that walks the shell and returns
`getBoundingClientRect()` plus the computed properties you care about
(`backgroundColor`, `backgroundImage`, `borderRadius`, `fontFamily`, `fontSize`,
`fontWeight`, `letterSpacing`, `padding`, `gap`, `boxShadow`, `webkitAppRegion`,
`position`, `zIndex`, `backdropFilter`). Filter out `none`/`normal`/`0px`/`rgba(0,0,0,0)`
so the output stays readable.

**Also dump the DOM outline** (tag + class + rect, depth 3–4). Class names tell you the
reference's structural vocabulary — that is what you map onto the target app's selectors.

### 2b. Probing pitfalls that produce false conclusions

Two mistakes cost real time. Both make a correct fix look broken:

- **Never drop the pseudo-element argument.** `getComputedStyle(el, '::before')` needs the
  second argument. A helper written as `const cs = (el) => getComputedStyle(el)` silently
  returns the *host* element's style, so `cs(el, '::before').opacity` reads the host's `1`
  and you conclude the overlay change never applied. Write the helper as
  `(el, pseudo) => getComputedStyle(el, pseudo)`.
- **`getComputedStyle` returns *used* values for borders.** Chromium rounds border widths to
  whole device pixels at DPR=1, so a `1.5px` border reads back as `1px`. Do not conclude the
  rule was dropped — check a different property the rule also sets (`borderTopColor` flipping
  to your token colour proves the rule won). `1.5px` is still the right value: it renders as
  `1.5px` at the 125%/150% scaling common on Windows.

Verify *which* rule won, don't guess. Walk `document.styleSheets`, skip sheets whose
`cssRules` throws, and collect every `CSSStyleRule` where `el.matches(r.selectorText)` is true
and the declaration you care about is present. An empty result means **no rule matches that
element at all** — which is itself the answer (see the container-vs-child trap in §4).

### 2c. Verifying auth-gated / role-gated UI without an account

Admin-only sidebars, gated routes and permission-dependent chrome are invisible to a guest
session, so a guest-only sweep proves nothing about them.

- Look for a preview / demo switch first — a `VITE_UI_PREVIEW`-style build flag plus a
  hard-coded `previewUser` (often `is_system_admin: true`) is common, and the router guard
  usually short-circuits in preview mode.
- Start a **second** dev server on another port with the flag set, then point your CDP probe at
  it. One command, no accounts, no database writes:
  ```bash
  VITE_UI_PREVIEW=true <vite> --host 127.0.0.1 --port 5179   # run_in_background
  ```
- Expect collateral noise and do not report it as a bug: API calls return 401 (pages show a
  "please sign in" banner) and any Electron IPC that validates `event.senderFrame.url` against
  the original dev port will fail with a permission error.
- Kill that server when done, then re-run the sweep against the real instance.

## 3. Verify `-webkit-app-region` drag regions

This is where people waste the most time. Rules:

- **`-webkit-app-region` is NOT inherited.** Setting `drag` on a container does nothing if any
  child element covers it. Blank-area spacers (`div.sidebar-spacer`, `div.rail-spacer`, …)
  must be set to `drag` themselves, or the container is effectively not draggable.
- **`pointer-events: none` makes a `drag` region inert.** Overlay headers are often built as
  `position: absolute; pointer-events: none` with interactive children re-enabling
  `pointer-events: auto`. Such a header is not hit-testable, so setting `drag` on it does
  nothing — and you cannot just flip it to `auto` if the element below it (a canvas, a
  scrollable stage) legitimately occupies that band.
- **Synthetic input cannot start an OS window drag.** On Windows, Electron implements
  app-region drags through `WM_NCHITTEST` → `HTCAPTION`, which only real OS mouse messages
  reach. CDP `Input.dispatchMouseEvent` will NOT move the window. Do not conclude "the fix
  failed" from a CDP drag test, and do not trust a "moved = YES" result either — the window
  may have been moved by the user.
- **Check `document.visibilityState` before testing.** When the window is occluded it reports
  `hidden` and Chromium ignores drags entirely. Bring it to front and confirm `visible`.
- **A minimised window is a trap in a different way.** `IsWindowVisible` is still TRUE for a
  minimised window, so the window proc keeps answering `WM_NCHITTEST` with plausible values —
  but `GetWindowRect` returns the `-32000` series, so **the client origin you compute from it is
  garbage and every probe point lands on the wrong pixel**. Restore the window
  (`ShowWindow(hwnd, SW_RESTORE)` = 9, or `--restore`) and re-run before drawing any conclusion.
  Corollary: **never filter candidate windows by size** (`w > 200 and h > 200`) — a minimised
  window measures 160×28 and gets filtered out, after which the script quietly picks some other
  process's window (in practice: `explorer.exe`'s desktop) and you end up testing that.
  Rank by `IsIconic` instead.
- **Two-level verification — and only the second one is authoritative.**
  1. *Cheap pre-check, DOM level.* Sample points across the intended drag strip and assert the
     topmost element computes to `drag`. This is a **necessary but not sufficient** condition:
     it cannot see an element that is `display: none` / `visibility: hidden` / zero-sized, and it
     cannot see whether the app-region actually merged into a title bar.
  2. *The real oracle: `WM_NCHITTEST`.* Send `0x0084` to the window and read the code back.
     Only this proves what the OS will do with a pixel.

```bash
node scripts/cdp-drag-check.mjs <port>                  # DOM-level scan (pre-check)
python scripts/nchittest-probe.py --scan 600            # OS-level truth: scan a column
python scripts/nchittest-probe.py 8,20 60,20 600,40     # specific client points
python scripts/nchittest-probe.py --restore             # un-minimise first, then re-run
```

```
HTCAPTION(2)  → title bar: press starts a window drag, renderer never sees the event
HTCLIENT(1)   → client area: renderer gets the event (buttons work, canvas works)
HTTOP(12) …   → window resize border
```

Read the probe's header comment before trusting a run — it documents the two traps that each
cost real time: the `IsIconic` / `-32000` coordinate trap, and the "restored it, but the window
went back to minimised" false negative.

**`HTCAPTION` starting a few px below the top is normal, not a bug.** Frameless windows keep an
invisible resize border (`HTTOP`), so a 40 px drag strip measures as `HTCAPTION: y = 5..39`.
Assert on the *sum* (5 + 35 = 40), not on `y == 0`.

**A synthetic click is a valid test for clicks, even though it is invalid for drags.** Those two
facts are independent and easy to conflate. `Input.dispatchMouseEvent` (or simply `el.click()`)
does fire Vue/React handlers and does trigger router navigation — so after you set a container to
`drag`, use a synthetic click on a child link to prove the child's `no-drag` still wins:

```js
const hit = document.elementFromPoint(cx, cy)
getComputedStyle(hit).webkitAppRegion   // must be 'no-drag'
```

Only the *window movement* assertion is off-limits to synthetic input.

A useful control: run the same scan against the reference app. A drag strip that is
`position:absolute; z-index: low` and sits *before* the content in DOM order is often fully
covered by the page container and receives zero hits — the reference may be less draggable
than your port. Report that, it is a real finding.

### The overlay-strip trap (check this before shipping)

A fixed full-width drag strip across the top of the content area is the easiest way to get a
draggable window — and the easiest way to silently break buttons. Two failure modes:

1. **Stacking context is not beatable by the *page*, but it does not need to be.**
   If the page container is `position: relative; z-index: 1` (very common), every descendant —
   including a page header you try to lift to `z-index: 61` — is confined to that context, so a
   root-level overlay at `z-index: 60` wins and swallows clicks on the header's buttons.
   The tempting fix is to **disable the overlay on that route**:
   ```css
   /* ⚠️ DO NOT DO THIS — it looks harmless and is a landmine */
   body:has(.app-shell.canvas-shell) .window-drag-region { display: none !important; }
   ```
   **That is a trap.** It silently assumes some other element owns the drag on that route. The
   moment that other element disappears — a sidebar switched to `v-if="!isCanvasRoute"`, a rail
   collapsed, a header hidden at a breakpoint — the route is left with **zero** draggable region
   and the user reports "the window cannot be dragged on this page any more". Give the *user* a
   route they can't drag and they will find it.

   **The correct fix keeps both abilities at once**, because the two mechanisms are independent:
   - **DOM hit-testing** honours `z-index` → drop the overlay *below* the page container:
     `z-index: 0 !important` (page container is usually `z-index: 1`). The header's buttons are
     hit again.
   - **`-webkit-app-region` merging ignores `z-index` completely and goes by document order
     only** → the overlay still registers as `drag`, so the strip stays draggable.
   - Then carve the page's own interactive elements back out, since router content comes **after**
     the overlay in document order and later `no-drag` wins:
     ```css
     .canvas-page .ref-title,
     .canvas-page .canvas-project-menu,
     .canvas-page .canvas-menu-card { -webkit-app-region: no-drag; }
     ```
   "Either the buttons work or the window drags" is a false dilemma — check the `z-index` and the
   document order separately and you get both.

   **Also re-check every `left`/`right`/`top`/`inset` the overlay inherits.** A rule like
   `body:has(.app-shell.topnav-shell) .window-drag-region { left: var(--rd-sidebar-w) }` pushes the
   strip to start after the sidebar; on a route where the sidebar is not rendered, the left N px
   are a dead zone (symptom: "only the right half of the top can drag"). Same-specificity rules are
   resolved by **file order in the entry CSS** — verify that order in `main.ts`/`index.js` before
   relying on it, and say so in the comment, because reordering imports silently reverts the fix.
2. **The overlay may not be a descendant of the app shell.** In a Vue/React root, the drag
   element is often a sibling of the router outlet, so `.app-shell.x .window-drag-region`
   never matches. Use `body:has(.app-shell.x) .window-drag-region` instead.

**Sweep every route after adding an overlay — in both directions.** An overlay covering the top
*N* px will block any control whose own header lives in that band. For each route:

- *Can I still click?* Collect interactive elements inside the content area, flag those with
  `rect.top < N`, then confirm with `document.elementFromPoint(centerX, centerY)` — geometry alone
  gives false positives once the overlay is behind the page, so the DOM hit test is the authority
  here.
- *Can I still drag, and can I still not accidentally drag?* Run
  `python scripts/nchittest-probe.py --scan <x>` per route and assert the band is **non-empty**,
  and that the carved-out controls answer `HTCLIENT`. A route whose band is empty is a route the
  user cannot move the window on.
- *Does it still work when the route's own chrome is absent?* This is the case the disable-the-
  overlay shortcut misses. Test the route in its **narrow** / collapsed / empty variants too, since
  that is where the sidebar or a header quietly drops out of the DOM.


## 4. Write a parity layer, don't rewrite

Add one new stylesheet imported **last** (after the existing redesign/theme files) and keep the
original file intact for rollback comparison. Header it with the three sources you measured:
the token file, the rule block, and the rendered reference.

While porting, expect these specific breakages:

- **Compressing a multi-row widget.** A trigger built as `display: grid` with two stacked
  lines (`<strong>探索</strong><small>EXPLORE</small>`) overflows when you force the
  reference's single-line height. Hide the second line and pin
  `grid-template-columns: auto minmax(0,1fr) auto` + `text-align: left`.
- **Assuming the indicator is a pill.** Check its measured size first: a 26×2 px box is an
  **underline**, not a segmented-control pill. Give it the reference's colour but keep the
  geometry.
- **Invisible ink.** Dark-theme accents like `--accent-ink` (`#06301A`) are meant for text
  *on* a filled accent surface. Reusing them as a foreground colour on a dark background makes
  the label disappear. Use the accent itself.
- **A token used in more than one place.** Changing `--sidebar-w` propagates only if the grid
  references the same variable — verify both, or the layout gets a 1px seam.
- **Container vs. child: the same widget can be built two ways.** Two pages had a search box;
  on one the styled element was the wrapper `<label class="x-search">` with a bare, classless
  `<input>` inside (no rule matched that input at all), on the other the inner `<input>` carried
  the border itself. Styling only the input leaves one page borderless; styling only the wrapper
  leaves the other double-bordered. **Make the wrapper own border/background and force the inner
  control transparent + borderless.** Use `:focus-within` on the wrapper for the focus ring.

## 4b. Sweeping the sweep: extend parity past the shell

A parity layer that only restyles the app shell leaves every inner page looking like the *old*
design. Budget for a second pass over page-level components. Two independent axes:

- **Letterforms** — dot-matrix / display fonts belong on eyebrows, labels, metadata, counts,
  table headers, filter chips, empty states and system messages. Leave body copy and card
  titles in the UI font, or the whole app becomes unreadable.
- **Geometry** — hard 1.5px edges, 6–8px radii, and `0 3px 0` / `0 4px 0` hard shadows on
  cards, panels, covers, buttons and inputs.

**Never touch `padding`, `height` or `line-height` in a blanket sweep.** Size changes break
layouts that were tuned for the old metrics (a two-row grid widget will overflow). Font-family,
font-size on *label-sized* text, border, radius and shadow are safe; box metrics are not.

### A styled element may be invisible — check before you claim coverage

The nastiest false positive in this whole workflow. A heading that is inside a `display: none`
subtree still returns **correct** `font-family`, `font-size` and `color` from
`getComputedStyle`. Your probe prints "H2/FusionPixel/19px" and you report "typography rule
covered this page" — while nothing is on screen.

Always verify visibility by walking the ancestor chain:

```js
const isVisible = (el) => {
  const r = el.getBoundingClientRect()
  if (!(r.width > 0 && r.height > 0)) return false
  for (let n = el; n && n !== document.body; n = n.parentElement) {
    const s = getComputedStyle(n)
    if (s.display === 'none' || s.visibility === 'hidden') return false
  }
  return true
}
```

`route-sweep.mjs` reports `[隐藏]` for this. When it fires, find *which* rule hides it —
there are two distinct causes and they need different fixes:

1. **A deliberate "remove page chrome" block.** Early stylesheets in a long cascade often
   contain something like
   ```css
   .page-intro > div:first-child { display: none }
   .page-intro:has(> div:only-child) { display: none }
   .page-intro:not(:has(button)) { display: none }
   ```
   and **no later stylesheet re-enables it** (28 sheets after it in one project). Re-enable in
   your parity layer with `!important` plus enough specificity to beat `:has()` (which
   contributes its argument's specificity).
2. **A base-class rule you did not notice.** `.page-content .eyebrow { display: none }` hides
   only elements whose class is *exactly* `eyebrow`. Variants like `explore-intro-eyebrow` or
   `skills-eyebrow` are unaffected — which is why one page shows its eyebrow and another does
   not. When a variant works and the base does not, grep for the base class alone, not the
   variant.

Grep for the *base* class name across every stylesheet before concluding a component is
unstyled.

### Teleported children escape the shell scope

Modals, composers and popovers are often `Teleport`-ed to `document.body`, making them
**siblings** of the app shell rather than descendants. `.app-shell.x .my-widget` will never
match. Use `body:has(.app-shell.x) .my-widget`. Note the asymmetry: theme rules written as
`:root[data-theme='dark'] .my-widget` **do** match a teleported node (`:root` is `<html>`),
so such a component can be correctly dark-themed while still missing every shell-scoped rule.

### Adding a child to a single-row grid

If the container is `display: grid` with `grid-template-rows: minmax(0, 1fr)` and exactly one
child, inserting a header as a new first child gives the header the full `1fr` row and pushes
the real content into an implicit `auto` row. Set `grid-template-rows: auto minmax(0, 1fr)`
explicitly. Check the *resolved* value first — `getComputedStyle(el).gridTemplateRows` returns
pixels, and a stale multi-row declaration from an earlier stylesheet may already have been
overridden by a later one.

### Screenshots are not evidence for colour

A CDP screenshot may come back **downscaled** (`Page.captureScreenshot` at a clip, or a window
at a fractional device pixel ratio). A dark panel can read as light grey, and a light CTA
inside it makes the whole block look inverted. One project almost got a correct dark-theme
component "fixed" into a broken one this way. **Read computed styles for colour; use
screenshots only for layout and composition.**

Enumerate the target's real class vocabulary before writing selectors — grep every view file for
`class="..."`, split on whitespace, dedupe. Then write attribute-substring sweeps
(`[class*='-label']`, `[class*='-meta']`, `[class*='-panel']`) **anchored under the page-content
container** so they cannot leak into the shell. Prefer a handful of well-anchored sweeps over
one selector per class.

Scope the heaviest effects away from precision surfaces: turn the CRT/scanline/vignette overlay
**off** on canvas/editor routes, and dial it down an order of magnitude on light themes (black
scanlines on white read as dirty paper, not as CRT).

## 5. Verify

1. Reload the target (`location.reload()` via CDP), wait, then re-read the computed values and
   diff them against the reference table.
2. Screenshot both at the same viewport and look at them side by side.
3. Report what is verified by measurement vs. what still needs a human (real-mouse drag,
   subjective intensity of textures/effects).

### 5b. If you also reorganise the navigation, audit for orphan routes first

Aligning the shell usually turns into "and fix the sidebar". Before restructuring tabs, diff the
router table against the navigation definition — pages reachable by URL but absent from any menu
are extremely common and are the real defect:

- Grep the router for every `path:` / `name:`, then grep the layout for the nav item list. The
  set difference is your orphan list (in this project: three orphans — an assistant, a
  notifications centre and a settings page — plus a "management" array whose filter excluded
  every item it contained, i.e. dead code that always rendered nothing).
- Also check the *path → section* resolver. A hand-written `if/else` chain listing three or four
  paths silently mislabels every other route; replace it with one regex-per-section map and a
  single `resolve(path)` function, so new routes cannot fall through.
- After the rewrite, sweep **every** route and assert that exactly one nav item is active.
  "Zero active items" is the symptom of an unassigned page and is worth fixing even when the page
  itself renders fine.

Use `scripts/route-sweep.mjs` for this (and for the §3 overlay sweep — it does both):

```bash
node scripts/route-sweep.mjs <cdpPort> <baseUrl> "/explore,/canvas,/settings" [outPrefix]
```

Two false positives to expect from that report, neither of which is a bug:

- **"No active item" on a role-gated route.** If the nav item itself is `v-if`-gated
  (signed-in-only notifications, admin-only settings), a guest sweep correctly finds nothing
  active. Re-run against the preview instance from §2c before reporting it.
- **A page with genuinely no title.** Chat/editor surfaces often have no `h1`–`h3`; the sweep
  prints `(无)`. That is a finding about the page, not about your sweep.

### Never build a selector by concatenating comma lists

The single most expensive bug in the sweep script. `('.page-content, main, #app') + ' button'`
does **not** scope to those containers — it parses as
`.page-content, main, #app button`, so it also matches the bare `<main>` and `#app` elements
themselves. The overlay then "hides" containers that merely overlap it, and every route reports
false occlusion. Pass selector lists as arrays, expand them in-page with
`list.flatMap((s) => [...root.querySelectorAll(s)])`, and dedupe.

### Check the guard order on role-gated routes

While sweeping routes you may find an admin page rendering for a guest. Read the navigation
guard top to bottom — early returns shadow later checks:

```js
if (!to.meta.guest && !auth.isAuthenticated) return true   // ← returns first
if (to.meta.admin && !auth.isAdmin) return '/403'          // ← unreachable for guests
```

The page renders (its API calls 401, so no data leaks — it just shows defaults behind a
"please sign in" banner), which is why it survives casual testing. Fix by moving the role check
above the pass-through, and keep the guest-first intent: send unauthenticated users to the
workbench (where the sign-in dialog lives) rather than to a 403 page, which is meant for
*signed-in but under-privileged* users.

```js
if (to.meta.admin && !auth.isAdmin) return auth.isAuthenticated ? '/403' : '/dashboard'
```

Flag this to the user explicitly — it is an auth-behaviour change, not a visual one, and it is
outside the scope of a parity task even though you found it while doing one.

### Your test fixture may itself be invalid

Before concluding "the feature is broken", prove the input is legal. A round of debugging a
"edges vanish on reload" bug ended with the fixture being the bug: the payload connected an
`image` output to a `text`-only input, so the app's validator was rejecting it **correctly**.
Re-read the error message and check it against the domain rules before touching the code.

Related: read the *whole* error, not just the first line. Vue Flow's
`An edge needs a source and a target` is emitted for `EDGE_INVALID` (your own validator said no)
**and** for `EDGE_SOURCE_TARGET_MISSING` (node lookup failed). Same prose, different causes —
check the error *code*, or read the library's message templates.

### HMR can hand you a stale closure

A `ReferenceError: <newly added variable> is not defined` right after you added that variable is
usually **not** your code — it is a hot-reload artefact: an old component instance still holds a
callback from the previous module version. Restart the dev server and re-run before believing it.
If the error disappears on a clean load, it was never real.

## 6. Migrating a hand-rolled canvas onto a graph library

When replacing a bespoke pan/zoom/edge implementation with Vue Flow / React Flow, these are the
traps that cost the most time.

**Restored data must not be re-validated.** The library calls your `isValidConnection` for
*programmatic* edges too, not just user drags. If you re-run validation on load, then the day you
tighten a rule, every stored edge that no longer passes is silently dropped — and the autosave
that follows writes the loss to disk permanently. Gate the validator on a `restoring` flag:

```ts
let restoring = false
function isValidConnection(c: Connection) {
  if (restoring) return true          // stored edges were legal when created
  …
}
// hydrate():  restoring = true; try { addEdges(saved) } finally { restoring = false }
```

Validation exists to stop a user's *current* mistake, not to audit existing data.

**Resolve ports from the persisted payload, not from the store.** `addEdges` internally looks up
each edge's source/target node and drops the edge if either is missing — and right after
`addNodes` the store may not be populated yet. Build a `Map<id, card>` from the saved cards and
pass it in. Also make sure the serializer **and the migrator** both carry `sourceHandle`/
`targetHandle`: losing them makes multi-port nodes unresolvable and the edge silently disappears
(observed as "1 edge saved, 0 edges after reload").

**`fitView()` before nodes are measured does nothing.** Node dimensions are only known after the
browser lays them out. A `nextTick` is not enough — the viewport stays at identity and the user
opens a canvas that looks empty. Use the library's readiness hook:

```ts
onNodesInitialized(() => {
  if (pendingViewport === undefined) return   // one-shot switch
  const target = pendingViewport
  pendingViewport = undefined
  target ? applyViewport(target) : fitView({ padding: 0.2 })
})
```

The one-shot switch matters: the hook re-fires whenever the node set is re-measured (e.g. the
user adds their first node), so without it the view snaps back on every edit. Also note a
`default-viewport` prop is applied at init and will overwrite a `setViewport` you called too early.

**Probe the element that actually carries the value.** The pan/zoom transform is on
`.vue-flow__transformationpane`, not `.vue-flow__viewport` (which only holds
`-webkit-tap-highlight-color` and reports `transform: none`). Guessing the class name produced a
confident, wrong "fitView is broken" reading. Dump candidate selectors and their computed styles
first.

**Synthetic `MouseEvent`s cannot drive panning.** Extends §3: a synthetic `click` reaches
handlers, but a synthetic `pointerdown`/`pointermove` sequence does **not** move the viewport —
the library's drag path relies on real pointer-event identity. Use CDP
`Input.dispatchMouseEvent`, which produces trusted events:

```js
await cdp.send('Input.dispatchMouseEvent', { type: 'mousePressed', x, y, button: 'middle', buttons: 4, clickCount: 1 })
// … mouseMoved steps …
await cdp.send('Input.dispatchMouseEvent', { type: 'mouseReleased', x, y, button: 'middle', buttons: 0, clickCount: 1 })
```

**Persist the viewport alongside the graph.** Without it, reload puts the user back at the default
view — the nodes are all there, just outside the visible area, which reads as "the canvas is
empty". Debounce the save (the viewport changes every frame while panning) and flush on
`pagehide`, not `beforeunload` — `pagehide` also fires on mobile backgrounding and bfcache entry.

## 7. Verify the verifier before you trust it

The most expensive mistakes in this work are **believing a check that cannot fail**. From the
outside they look identical to success: green output, zero errors, broken app.

### A typecheck script that checks nothing

A scaffold's root `tsconfig.json` is usually:

```json
{ "files": [], "references": [{ "path": "./tsconfig.app.json" }, { "path": "./tsconfig.node.json" }] }
```

Run `tsc --noEmit` — or `vue-tsc --noEmit` — against *that* file and it compiles **zero input
files** and exits 0. It never fails, so it can never tell you anything. The scaffold's own `build`
script normally uses the correct form (`vue-tsc -b && vite build`), which is why `npm run build`
catches what `npm run typecheck` does not.

**Prove the check can fail before you cite it.** Inject a deliberate error
(`const x: number = 'definitely not a number'`), run the command, and confirm it reports it. Do
this once per project, early. A one-word fix (`"typecheck": "vue-tsc -b --noEmit"`) turned a no-op
into **52 real errors** across modules I had already written — every one of which I had reported as
"type check passed".

While you are there: if the repo declares `strict` but the errors you just surfaced are mostly
*correct* complaints (missing index signatures, an un-narrowed type predicate), that is normal —
a project whose typecheck never ran accumulates them.

### A headless browser cannot see the desktop-only branch

When the same code has a desktop path *and* a browser fallback, a headless-browser run silently
exercises only the fallback — and the desktop path is the one that ships.

Real case: `openCanvas()` calls `window.nexusvaultDesktop.openCanvasWindow(projectId, cardId)`
when the preload bridge exists, and otherwise just navigates in the current window. Headless Edge
has no bridge, so the run covered the fallback and reported green — while preload → IPC → main
process `createCanvasWindow` → route query → node focus, the entire desktop-only chain, was never
executed.

**Test it in the real runtime.** Launch with `--remote-debugging-port` and count CDP page targets:
the desktop branch must *add a window*.

```js
const before = (await listTargets()).filter(t => t.type === 'page').length
await evalJs(`window.<bridge>.openCanvasWindow(${JSON.stringify(projectId)}, ${cardId})`)
const after  = (await listTargets()).filter(t => t.type === 'page').length
// assert after === before + 1
```

`after > before` is what separates "opened a window" from "navigated in place" — both end up with
the same URL, so asserting the URL alone proves nothing. Then attach to the **new** target and
assert its internal state (rendered nodes, selection, stripped query params).

Assert the bridge surface too (`typeof bridge.openCanvasWindow === 'function'`, plus any flags the
renderer branches on). If preload and renderer disagree on a method name nothing errors — the
renderer just takes the fallback forever, and every test keeps passing.

### Click helpers must scroll, re-measure, and hit-test

Synthetic-coordinate clicking breaks in three ways that all present as "the button does nothing":

1. **The element sits below the fold of a scroll container** (`max-height` + `overflow-y: auto`).
   `getBoundingClientRect()` still returns a plausible point — one that lies on the clip edge.
2. **Layout shifted** since you measured. Re-measure *after* scrolling; never reuse a cached point.
3. **Something covers it.** Ports at `-6px` under an `overflow: hidden` card are the canonical case.

A correct helper does: `scrollIntoView({ block: 'nearest' })` → wait two rAFs → re-read the rect →
`document.elementFromPoint(centre)` and assert the hit is the element or a descendant. When it
isn't, report *what was actually hit* — that string is what identifies the occlusion.

Assert **every** step, not just the final state. A script whose first assertion already failed will
report success if it only inspects the end.

### A verification script must print its evidence when it fails

If readings accumulate in a local object and the script throws before printing, one failed
assertion erases the whole run. Keep the report at module scope and print it from `catch`.
A run that says "step 3 failed, here are steps 0–2" is diagnosable; `Cannot read properties of
null (reading 'x')` is not.

### Run `node --check` on every probe before running it

Probes are throwaway code written fast. A syntax error surfaces as a confusing CDP failure.
`node --check <script>` costs nothing.

## 8. When the user says "ugly", measure before you restyle

"It looks bad" is usually a geometry defect with a styling symptom. Measure first — the numbers
name the real problem, and they also tell you which of your previous rules silently lost.

A worked example: a two-value workspace switch built as a **dropdown**.

- 44px tall, 231px wide, containing two words and a chevron. Two mutually exclusive values do not
  need a menu. The shape was the bug, not the colour.
- Switching cost two clicks (`open menu` → `choose`) to flip a boolean.
- The chevron was `ChevronsUpDown`, which everywhere else means *sort* or *expandable*.
- The selected value had no emphasis, so you could not see which workspace you were in.
- **And the height was not what the parity layer said it was.** The parity sheet set
  `height: 38px !important`; an earlier sheet set `min-height: 44px !important`. Both won —
  they are different properties and they compose. The control sat at 44px directly above a 38px
  primary capsule, so the two never lined up.

### `min-height` / `max-height` beat your `height` — read them together

Two `!important` declarations on *different* properties do not conflict; the stricter one wins.
When you audit a height that "didn't apply", read `height`, `min-height`, **and** `max-height`,
and check the *earlier* stylesheets — not just the one you last edited. A stale override from a
sheet you thought you had superseded is the usual culprit.

### Segmented control recipe (width-independent by construction)

Make the sliding indicator's width equal to one slot and move it with `translateX(100%)`:

```css
.switch      { position: relative; display: grid; grid-template-columns: 1fr 1fr; padding: 3px; }
.switch-thumb{ position: absolute; top: 3px; left: 3px;
               width: calc(50% - 3px); height: calc(100% - 6px);
               transition: transform .3s cubic-bezier(.34, 1.45, .5, 1);
               pointer-events: none; }
.switch[data-mode='b'] .switch-thumb { transform: translateX(100%); }
```

Why it needs no per-slot offset arithmetic: inner width is `100% - 6px`, so one slot is
`(100% - 6px) / 2 = 50% - 3px` — exactly the thumb's width. `translateX(100%)` is therefore the
thumb's own width, which is also the slot width. Both ends land exactly.

Verify it anyway, at several widths — "provably width-independent" has been wrong before:

```js
for (const w of [150, 200, 227, 260, 320]) { el.style.width = w + 'px'; /* compare thumb rect to checked-slot rect */ }
```

Two details that are easy to miss:

- `pointer-events: none` on the thumb. It sits over the options; without this the click lands on
  the indicator. Assert the hit layer, don't assume it:
  `document.elementFromPoint(cx, cy)?.closest('.switch-option')` must be the option you aimed at.
- Keep the transition's easing slightly overshooting (`cubic-bezier(.34, 1.45, .5, 1)`). A little
  bounce is where "modern and premium" gets its playfulness; a linear slide reads as a form control.

### Do not spend your primary accent twice

If a solid-accent primary CTA sits directly below the control, do **not** make the selected
segment solid accent too — you get two primary buttons competing. Use a tinted surface plus
accent-coloured text/icon for the selection, and keep the solid accent for the single real CTA.

### Accessibility for a segmented control

- `role="radiogroup"` on the container, `role="radio"` + `aria-checked` on each option.
- Roving tabindex: only the checked option is `tabindex="0"`, the rest `-1`.
- Arrow keys move focus **and** select (standard radiogroup behaviour). `Home` / `End` jump to the
  ends. With only two options there is no "accidentally slid past everything" cost, so follow the
  standard rather than inventing a two-step confirm.
- Give the sliding indicator `aria-hidden="true"` — it is decoration; `aria-checked` carries the
  meaning.
- Move the descriptions the old menu showed into each option's `title`, or you silently delete
  information when you flatten a menu into segments.

### Retiring a component

1. Archive the old file before deleting it (a machine with no recycle bin makes `rm` irreversible).
2. Rename the root class. Old selectors then go inert instead of half-matching.
3. Delete the dead rule block — but assert the range first. Filter the candidate lines and abort
   if anything in them is *not* one of the retired class names:

```js
const offenders = lines.slice(start, end)
  .filter((l) => l.trim() && !l.trim().startsWith('/*') && !l.trim().startsWith('*'))
  .filter((l) => !l.includes('old-class') && l.trim() !== '}' && !/^[a-z-]+:/.test(l.trim()))
if (offenders.length) throw new Error(`range contains foreign rules:\n${offenders.slice(0,5).join('\n')}`)
```

4. Leave a **tombstone comment** where the block was, naming the replacement file. A silent
   deletion makes the next reader wonder whether the component still exists.
5. Grep the whole tree for the retired class name afterwards; the only hit should be the tombstone.

### jsdom: a detached container cannot hold focus

`focus()` on an element inside a container that was never appended to `document` does **not**
update `document.activeElement`. If you assert "the arrow key moved focus" against a detached
container you will get `<body>` and blame the component. Append to `document.body` and clean up in
`afterEach`. (The failure is at least honest: it proves the assertion was testing something real.)

## 9. When a state change "does nothing", suspect the router key

A change that lands in the store but never shows up in the DOM has three usual causes. Check them
in this order — the third one is the one nobody thinks of.

**1. Is the change actually being made?** Instrument both sides at the same moment and at a later
tick:

```ts
console.info('[trace]', { store: nodes.filter((n) => n.selected).map((n) => n.id) })
setTimeout(() => console.info('[trace] later', {
  store: nodes.filter((n) => n.selected).map((n) => n.id),
  dom: document.querySelectorAll('.vue-flow__node.selected').length,
}), 900)
```

`store: [2], dom: 0` at +900ms does **not** mean "the renderer ignores this property" — do not stop
there and rewrite your state code. Keep going.

**2. Did something undo it?** Log a DOM reference you hold across the interval. If a `ref` that was
non-null becomes null, the component was **unmounted**, not merely re-rendered:

```ts
console.info('[trace]', { hasStage: !!stageRef.value })   // true at t≈0, false at t+600ms ⇒ remount
```

**3. Is the layout's `<RouterView>` keyed on something that changes?** This is the one that cost
the most time:

```vue
<RouterView :key="`${route.fullPath}:${auth.currentTeamId}`" />   <!-- fullPath INCLUDES the query -->
```

`fullPath` includes the query string, so **every** query-only navigation remounts the whole page.
The visible symptom in that session: "open canvas at node X" applied the selection, then stripped
`?card=` from the URL for cleanliness — the strip itself changed `fullPath`, remounted the view, and
destroyed the selection. From the outside it looked exactly like "the feature does nothing".

- Key on `route.path` (+ team id) instead. Path changes and team switches still remount; query
  changes do not.
- Any page that read `route.query` **at setup** and was relying on the remount to re-sync must now
  `watch(() => route.query.x)`. Grep `route.query` across all views and classify each hit; do not
  assume only the page you were working on is affected.
- Verify the fix with DOM node identity, not a `window` marker — see §9b.
- Remaining gap to document rather than paper over: with `path` in the key, `?a=1 → ?a=2` on the
  **same path** no longer reloads. If that transition is unreachable from the UI, say so in a
  comment; if it is reachable, the component has to become re-entrant.

### 9b. Two CDP traps that produce convincing false failures

**Never drive SPA navigation by importing the router module.** `await import('/src/router.ts')`
in the page hands you a **second** router instance. It writes to `history`, so `location.href`
changes — but the app's `<RouterView>` is bound to the primary instance, so the UI does not move.
Its `currentRoute` even reads `/` (it never navigated), which is the tell if you print it. You will
conclude the app is broken. Drive the real instance with a popstate, which is what vue-router's web
history listens to:

```js
history.pushState({}, '', '/explore?section=library')
window.dispatchEvent(new PopStateEvent('popstate', { state: {} }))
```

**A `window.__marker` cannot detect a component remount.** `window` is document-scoped — only a
full page reload clears it, so it survives every remount and every assertion built on it passes
vacuously. Detect remounts by **DOM node identity**:

```js
window.__nodeRef = document.querySelector('.page-header-title')
// after navigation:
document.querySelector('.page-header-title') === window.__nodeRef && window.__nodeRef.isConnected
```

Same node ⇒ the component survived. Old node `isConnected === false` ⇒ it really was replaced.

**Assertion hygiene, again.** Two of the failures in that session were the script's fault, not the
app's: `/canvas` is a full-bleed editor with no `<h1>`, and the `window` marker above. When a sweep
fails, first ask whether the assertion could ever have been true.

**Never sleep a fixed interval after `Page.navigate`.** 900 ms was fine for every route except the
first one after a cold start — where the dev server is still transforming modules and the app is
still on its booting screen. It failed exactly the two routes that ran first, which reads as "the
router is broken". Poll for rendered content instead:

```js
const deadline = Date.now() + 15000
while (Date.now() < deadline) {
  if (await evalJs('document.body.innerText.trim().length') > 40) { await wait(150); return }
  await wait(150)
}
```

Threshold on rendered **text**, not on your title selector, or pages that legitimately lack the
selector burn the whole timeout. And when a route has no `<h1>` by design, give the config an
explicit probe selector (`.vue-flow`) rather than asserting an empty string is truthy.

## Reporting

State the measured reference values as a table, list every file you changed, and separate
"verified by computed style" from "needs human confirmation". When a deliberate difference
remains (e.g. keeping a sidebar drag area the reference lacks), say so explicitly.

Report a *shape* change as a shape change, not as a restyle. "It is now a segmented control
instead of a dropdown, and here is why that is the right shape for two values" is a design
decision the user can disagree with; "I made it prettier" is not.

### Verification scripts

Reusable CDP helpers live in `scripts/`:

| script | use |
|---|---|
| `cdp-probe.mjs` | dump computed styles / geometry for a set of selectors |
| `cdp-drag-check.mjs` | confirm a drag region really moves the window |
| `cdp-reload-console.mjs` | reload a page and capture console + exceptions **during** the reload |
| `cdp-shot.mjs` | clipped high-DPI screenshot of one region; pass a final `preJs` arg to click something open first |
| `route-sweep.mjs` | per-route active nav / title / occlusion / console-error sweep |
| `cdp-nav-check.mjs` | route titles + the "query-only change must not remount" regression; drives the app's **own** router via popstate and detects remounts by DOM node identity (see §9b) |

`cdp-nav-check.mjs` takes `<port> <baseUrl> '<json>'`; see its header for the config shape. Its
`waitForBoot()` polls for rendered text instead of sleeping — a fixed sleep is too short on the
**first** navigation after a cold start, which reads as "this route is broken" (§9b).

`cdp-reload-console.mjs` exists because a probe attached *after* load misses the errors that
happen during hydration — which is exactly where data-restore bugs live.

`cdp-shot.mjs`'s `preJs` exists for the same reason in reverse: it navigates before capturing, so
any state that requires a click (an open panel, a selected node) is gone by the time the shutter
fires unless you re-create it after navigation.

Per-project interaction scripts belong in the project, not here — they assert project-specific
selectors. Keep them under `<workspace>/.workbuddy-ai/verify/` (reusable) and
`verify/archive/` (one-shot probes), and reuse the skeleton from `history-check.mjs`:
connect → `Runtime.enable`/`Page.enable` → evaluate / click / key helpers → a module-scope
`report` object printed by `catch` so a failed assertion still shows every reading it collected.

Three assertions that have each caught a real defect and are worth copying into every such script:

- **Hit-test before you click.** `elementFromPoint` at the target centre must resolve to the
  element you aimed at. This caught ports clipped by `overflow: hidden`, and a panel item scrolled
  out of its `max-height` fold.
- **Assert geometry, not a class.** Compare the indicator's `getBoundingClientRect()` against the
  selected slot's — pixel equality is the only proof they line up.
- **Probe the layout at several widths.** A control that is correct at one width can be broken at
  another; changing the element's own `width` in-page is enough and avoids window resizing.
