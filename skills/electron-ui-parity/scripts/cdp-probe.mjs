#!/usr/bin/env node
// Attach to a running Electron/Chromium app over CDP and report what it actually renders.
//
//   node cdp-probe.mjs <port> [out.png] [js-expression]
//
// No npm dependencies: Node 22+ has a global WebSocket.
// Uses fetch(), which ignores http_proxy, so localhost works even behind a proxy.
import { writeFileSync } from 'node:fs'

const PORT = Number(process.argv[2] || 9222)
const OUT = process.argv[3] || ''
const EXPR = process.argv[4] || ''
const log = (...a) => console.log('[cdp]', ...a)
setTimeout(() => { log('HARD_TIMEOUT'); process.exit(2) }, 60000)

const res = await fetch(`http://127.0.0.1:${PORT}/json/list`, { signal: AbortSignal.timeout(8000) })
const all = await res.json()
if (!all.length) { log('no targets — is the app running with --remote-debugging-port?'); process.exit(1) }

log('targets:')
for (const t of all) log(`  ${t.type} | ${t.title} | ${String(t.url).slice(0, 110)}`)

const page = all.find((t) => t.type === 'page')
if (!page) { log('no page target'); process.exit(1) }

const ws = new WebSocket(page.webSocketDebuggerUrl)
let id = 0
const pending = new Map()
ws.addEventListener('message', (e) => {
  const m = JSON.parse(e.data)
  if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id) }
})
const send = (method, params = {}) => new Promise((r) => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })) })
await new Promise((r) => ws.addEventListener('open', r))

const evalJs = async (expression) => {
  const r = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true })
  if (r.result?.exceptionDetails) return { __error: r.result.exceptionDetails.text }
  return r.result?.result?.value
}

// Default payload: state, design tokens, and a DOM outline of the shell.
const DEFAULT = `JSON.stringify((() => {
  const cs = getComputedStyle(document.documentElement);
  const v = (n) => cs.getPropertyValue(n).trim();
  const tokens = {};
  for (const sheet of document.styleSheets) {
    let rules; try { rules = sheet.cssRules } catch { continue }
    for (const r of rules) {
      if (!r.style) continue;
      for (const p of r.style) if (p.startsWith('--')) tokens[p] = v(p);
    }
  }
  const lines = [];
  const walk = (el, d) => {
    if (d > 3 || lines.length > 120) return;
    const c = getComputedStyle(el), r = el.getBoundingClientRect();
    lines.push({
      tag: el.tagName.toLowerCase(),
      cls: typeof el.className === 'string' ? el.className.slice(0, 80) : '',
      rect: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
      drag: c.webkitAppRegion, bg: c.backgroundColor, color: c.color,
      radius: c.borderRadius, font: c.fontFamily.split(',')[0], size: c.fontSize,
    });
    for (const k of el.children) walk(k, d + 1);
  };
  for (const k of document.body.children) walk(k, 0);
  return {
    title: document.title, url: location.href,
    visibility: document.visibilityState, focused: document.hasFocus(),
    theme: document.documentElement.dataset.theme || null,
    viewport: [innerWidth, innerHeight], screen: [screenX, screenY],
    bodyFont: getComputedStyle(document.body).fontFamily,
    tokens, outline: lines,
  };
})())`

const out = await evalJs(EXPR || DEFAULT)
log(typeof out === 'string' ? out : JSON.stringify(out, null, 1))

if (OUT) {
  const shot = await send('Page.captureScreenshot', { format: 'png' })
  if (shot.result?.data) { writeFileSync(OUT, Buffer.from(shot.result.data, 'base64')); log('screenshot ->', OUT) }
  else log('screenshot failed')
}
process.exit(0)
