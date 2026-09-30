#!/usr/bin/env node
// Find which points in a window actually accept a frameless-window drag.
//
//   node cdp-drag-check.mjs <port> [x0] [x1] [y0] [y1]
//
// A point is draggable when the TOPMOST element there computes to
// -webkit-app-region: drag. This is the only reliable check: synthetic CDP mouse
// events cannot start an OS-level window drag (Windows needs a real mouse message
// to reach WM_NCHITTEST -> HTCAPTION), so never judge the fix by whether the
// window moved in an automated test.
const PORT = Number(process.argv[2] || 9222)
const X0 = Number(process.argv[3] ?? 260)
const X1 = Number(process.argv[4] ?? 1080)
const Y0 = Number(process.argv[5] ?? 4)
const Y1 = Number(process.argv[6] ?? 70)
const log = (...a) => console.log('[drag]', ...a)
setTimeout(() => { log('HARD_TIMEOUT'); process.exit(2) }, 60000)

const res = await fetch(`http://127.0.0.1:${PORT}/json/list`, { signal: AbortSignal.timeout(8000) })
const page = (await res.json()).find((t) => t.type === 'page')
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

const state = await evalJs('JSON.stringify({v:document.visibilityState,f:document.hasFocus()})')
log('state:', state)
const parsed = typeof state === 'string' ? JSON.parse(state) : {}
if (parsed.v !== 'visible') {
  log('WARNING: document.visibilityState is not "visible" — the window is occluded or minimised.')
  log('Chromium ignores drags in that state. Restart/bring the app to front and re-run,')
  log('otherwise any "no drag points" result is meaningless.')
}

const scan = await evalJs(`JSON.stringify((() => {
  const hits = [], blocked = {};
  for (let y = ${Y0}; y <= ${Y1}; y += 6) {
    for (let x = ${X0}; x <= ${X1}; x += 60) {
      const e = document.elementFromPoint(x, y);
      if (!e) continue;
      const region = getComputedStyle(e).webkitAppRegion;
      const key = e.tagName.toLowerCase() + '.' + String(e.className).split(' ')[0];
      if (region === 'drag') hits.push([x, y, key]);
      else blocked[key] = (blocked[key] || 0) + 1;
    }
  }
  return { draggable: hits.length, samples: hits.slice(0, 12), blockedBy: Object.entries(blocked).sort((a,b)=>b[1]-a[1]).slice(0,8) };
})())`)

const r = typeof scan === 'string' ? JSON.parse(scan) : scan
log(`draggable points found: ${r.draggable}`)
for (const s of r.samples || []) log(`  (${s[0]},${s[1]}) -> ${s[2]}`)
if (r.draggable === 0) {
  log('nothing is draggable. Usual cause: -webkit-app-region is NOT inherited, so a child')
  log('element covering the intended region wins the hit test. Set `drag` on that child too')
  log('(or on the blank-area spacer). Top blockers at the sampled points:')
  for (const [k, n] of r.blockedBy || []) log(`  ${n}x ${k}`)
}
process.exit(0)
