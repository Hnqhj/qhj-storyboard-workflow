#!/usr/bin/env node
// Route sweep + "query-only change must NOT remount" regression, over CDP.
//
//   node cdp-nav-check.mjs <port> <baseUrl> '<json-config>'
//
// config = {
//   "routes":    [["/explore", "发现广场"], ["/dashboard", "今天想了解什么？"]],
//   "titleSelector": "h1",                 // optional, default "h1"
//   "queryTest": {                          // optional
//     "base": "/explore", "param": "section", "values": ["market", "library"]
//   },
//   "pathTest":  { "from": "/explore", "to": "/dashboard" }   // optional
// }
//
// Two traps this script exists to avoid — both produce convincing FALSE failures:
//
//  1. NEVER drive SPA navigation with `await import('/src/router.ts')` from the page.
//     That returns a SECOND router instance: it writes history (so location.href changes)
//     but the app's <RouterView> is bound to the primary instance, so the UI never moves.
//     Its currentRoute even reads "/" — print it and you will see. Drive the real router
//     with pushState + popstate, which is what vue-router's web history listens to.
//
//  2. A `window.__marker` CANNOT detect a component remount. window is document-scoped:
//     only a full page reload clears it, so it survives every remount and the assertion
//     passes vacuously. Detect remounts by DOM node identity instead (see remounted()).
//
// No npm dependencies: Node 22+ has a global WebSocket.
import { readFileSync } from 'node:fs'

const PORT = Number(process.argv[2] || 9222)
const BASE = process.argv[3] || 'http://127.0.0.1:5173'
const ARGV4 = process.argv[4] || '{}'
const CONFIG = ARGV4.endsWith('.json') ? JSON.parse(readFileSync(ARGV4, 'utf8')) : JSON.parse(ARGV4)

const TITLE_SEL = CONFIG.titleSelector || 'h1'
const log = (...a) => console.log('[nav]', ...a)
setTimeout(() => { log('HARD_TIMEOUT'); process.exit(2) }, 180000)

const report = { steps: [], consoleErrors: [] }
const record = (step, ok, detail) => {
  report.steps.push({ step, ok, detail })
  console.log(`${ok ? 'PASS' : 'FAIL'}  ${step}${detail ? ` — ${detail}` : ''}`)
}

const list = await (await fetch(`http://127.0.0.1:${PORT}/json/list`, { signal: AbortSignal.timeout(8000) })).json()
const page = list.find((t) => t.type === 'page')
if (!page) { log('no page target — is the app running with --remote-debugging-port?'); process.exit(1) }

const ws = new WebSocket(page.webSocketDebuggerUrl)
let id = 0
const pending = new Map()
ws.addEventListener('message', (e) => {
  const m = JSON.parse(e.data)
  if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); return }
  if (m.method === 'Runtime.consoleAPICalled' && m.params.type === 'error') {
    report.consoleErrors.push(m.params.args.map((a) => a.value ?? a.description ?? a.type).join(' ').slice(0, 200))
  }
})
const send = (method, params = {}) => new Promise((r) => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })) })
await new Promise((r) => ws.addEventListener('open', r))
await send('Runtime.enable')
await send('Page.enable')

const evalJs = async (expression) => {
  const r = await send('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true })
  if (r.result?.exceptionDetails) throw new Error(r.result.exceptionDetails.exception?.description || 'in-page exception')
  return r.result?.result?.value
}
const wait = (ms) => new Promise((r) => setTimeout(r, ms))

/**
 * Poll until the app has actually painted something.
 *
 * A fixed sleep is not enough and it fails in the worst place: the FIRST navigation
 * after a cold start, where the dev server is still transforming modules and the app is
 * still showing its booting state. Measured: 900 ms was fine for every later route and
 * too short for the first two — which reads as "the route is broken".
 * Threshold is on rendered text, not on the title, so pages that legitimately have no
 * <h1> (a full-bleed editor) do not burn the whole timeout.
 */
async function waitForBoot(timeout = 15000) {
  const deadline = Date.now() + timeout
  while (Date.now() < deadline) {
    const len = await evalJs('document.body.innerText.trim().length')
    if (len > 40) { await wait(150); return }
    await wait(150)
  }
  log('warning: app still looks empty after', timeout, 'ms')
}

async function goto(path) {
  await send('Page.navigate', { url: `${BASE}${path}` })
  await waitForBoot()
}

/** Drive the APP's own router. popstate is the event vue-router's web history subscribes to. */
async function spaGoto(path) {
  await evalJs(`(() => {
    history.pushState({}, '', ${JSON.stringify(path)})
    window.dispatchEvent(new PopStateEvent('popstate', { state: {} }))
  })()`)
  await wait(700)
}

const title = () => evalJs(`document.querySelector(${JSON.stringify(TITLE_SEL)})?.textContent?.trim() ?? ''`)

/** Park a DOM reference, then ask whether the same node is still the live one. */
async function parkRef(name, selector = TITLE_SEL) {
  await evalJs(`window.${name} = document.querySelector(${JSON.stringify(selector)})`)
}
const stillSameNode = (name, selector = TITLE_SEL) =>
  evalJs(`document.querySelector(${JSON.stringify(selector)}) === window.${name} && !!window.${name} && window.${name}.isConnected`)
const oldNodeDetached = (name) => evalJs(`!!window.${name} && window.${name}.isConnected === false`)

/* ── routes ─────────────────────────────────────────────────────────────── */
// Entry forms:
//   ["/explore", "发现广场"]              → assert the title selector reads exactly this
//   ["/canvas",  null, ".vue-flow"]       → no <h1> on this page; assert this selector exists
//   ["/canvas",  null]                    → just assert the page rendered something
for (const entry of CONFIG.routes || []) {
  const [path, expected, probe] = Array.isArray(entry) ? entry : [entry, null]
  await goto(path)
  const got = await title()
  if (expected === null && probe) {
    const found = await evalJs(`Boolean(document.querySelector(${JSON.stringify(probe)}))`)
    record(`route ${path}`, found === true, `${probe} present=${found} (no ${TITLE_SEL} expected)`)
  } else if (expected === null) {
    const len = await evalJs('document.body.innerText.trim().length')
    record(`route ${path}`, len > 40, `rendered ${len} chars of text`)
  } else {
    record(`route ${path}`, got === expected, `${TITLE_SEL}="${got}" (want "${expected}")`)
  }
}

/* ── query-only change: must update reactively, must NOT remount ─────────── */
if (CONFIG.queryTest) {
  const { base, param, values, expectedTitles } = CONFIG.queryTest
  await goto(`${base}?${param}=${values[0]}`)
  const before = await title()
  await parkRef('__navRef')
  for (let i = 1; i < values.length; i += 1) {
    await spaGoto(`${base}?${param}=${values[i]}`)
    const got = await title()
    const want = expectedTitles?.[i]
    record(`query-only → ${param}=${values[i]} updates the view`,
      want === undefined ? got !== before : got === want, `${before} → ${got}`)
    record(`query-only → ${param}=${values[i]} does NOT remount`,
      (await stillSameNode('__navRef')) === true)
  }
}

/* ── path change: the view really is replaced ───────────────────────────── */
if (CONFIG.pathTest) {
  const { from, to, expectTitle } = CONFIG.pathTest
  await goto(from)
  await parkRef('__navRef2')
  await spaGoto(to)
  const got = await title()
  record(`path change ${from} → ${to} swaps the view`,
    expectTitle === undefined ? Boolean(got) : got === expectTitle, `${TITLE_SEL}="${got}"`)
  record(`path change ${from} → ${to} unmounts the old view`,
    (await oldNodeDetached('__navRef2')) === true)
}

record('no console errors', report.consoleErrors.length === 0, JSON.stringify(report.consoleErrors.slice(0, 4)))

const failed = report.steps.filter((s) => !s.ok)
console.log(`\n===== ${report.steps.length - failed.length}/${report.steps.length} passed =====`)
if (failed.length) console.log('failed: ' + failed.map((f) => f.step).join(' | '))
process.exit(failed.length ? 1 : 0)
