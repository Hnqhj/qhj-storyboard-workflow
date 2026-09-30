#!/usr/bin/env node
// Sweep every route of a CDP-reachable SPA and report, per route:
//   · which nav item is active        (exactly one is expected; zero = orphan page)
//   · the page title tag/font/size    (catches pages a typography rule missed)
//   · whether an overlay drag strip hides interactive elements (real hit test)
//   · console errors accumulated during the sweep
//
// Usage:
//   node route-sweep.mjs <cdpPort> <baseUrl> <route1,route2,...> [outPrefix]
//
// Example:
//   node route-sweep.mjs 9222 http://127.0.0.1:5178 "/explore,/canvas,/settings" outputs/sweep
//
// Selector tuning via env (comma lists are fine — they are resolved in JS, never
// string-concatenated into a bigger selector):
//   NAV_ITEM_SEL   default '.sidebar-link, .nav-link, [data-nav-item]'
//   NAV_ACTIVE_SEL default '.is-active'
//                  NOTE: do NOT rely on '[aria-current="page"]'. Vue Router (and most
//                  routers) mark every link whose *path* matches as exact-active and
//                  ignore the query string, so query-based tabs (`?section=library`)
//                  all light up at once. Apps with query tabs add their own
//                  `is-active` class — use that.
//   CONTENT_SEL    default '.page-content, main, #app'
//   OVERLAY_SEL    default '.window-drag-region, .drag-strip, [data-drag-region]'
import { writeFileSync } from 'node:fs'

const [port, base, routeArg, outPrefix] = process.argv.slice(2)
if (!port || !base || !routeArg) {
  console.error('usage: node route-sweep.mjs <cdpPort> <baseUrl> <route1,route2,...> [outPrefix]')
  process.exit(1)
}
const ROUTES = routeArg.split(',').map((s) => s.trim()).filter(Boolean)
const list = (v, fallback) => (v ? v.split(',').map((s) => s.trim()).filter(Boolean) : fallback)
const NAV_ITEM = list(process.env.NAV_ITEM_SEL, ['.sidebar-link', '.nav-link', '[data-nav-item]'])
const NAV_ACTIVE = list(process.env.NAV_ACTIVE_SEL, ['.is-active'])
const CONTENT = list(process.env.CONTENT_SEL, ['.page-content', 'main', '#app'])
const OVERLAY = list(process.env.OVERLAY_SEL, ['.window-drag-region', '.drag-strip', '[data-drag-region]'])
const INTERACTIVE = list(process.env.INTERACTIVE_SEL, ['button', 'a', 'input', 'select', 'textarea', '[role="button"]'])

const log = (...a) => console.log('[sweep]', ...a)
setTimeout(() => { log('HARD_TIMEOUT'); process.exit(2) }, 600000)

const targets = await (await fetch(`http://127.0.0.1:${port}/json/list`, { signal: AbortSignal.timeout(8000) })).json()
const page = targets.find((t) => t.type === 'page')
if (!page) { log('no page target'); process.exit(1) }

const ws = new WebSocket(page.webSocketDebuggerUrl)
let id = 0
const pending = new Map()
const consoleErrors = []
ws.addEventListener('message', (e) => {
  const m = JSON.parse(e.data)
  if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); return }
  if (m.method === 'Runtime.exceptionThrown') {
    const d = m.params?.exceptionDetails
    consoleErrors.push(`EXCEPTION: ${(d?.exception?.description ?? d?.text ?? '').slice(0, 300)}`)
  }
  if (m.method === 'Runtime.consoleAPICalled' && m.params?.type === 'error') {
    consoleErrors.push(`CONSOLE: ${(m.params.args ?? []).map((a) => a.value ?? a.description ?? '').join(' ').slice(0, 300)}`)
  }
})
const send = (method, params = {}) => new Promise((r) => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })) })
const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
await new Promise((r) => ws.addEventListener('open', r))
await send('Runtime.enable')
await send('Page.enable')

async function ev(expression) {
  const r = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true })
  if (r.result?.exceptionDetails) return { __error: (r.result.exceptionDetails.exception?.description ?? r.result.exceptionDetails.text).slice(0, 400) }
  return r.result?.result?.value
}

// Selector lists travel as JSON arrays and are expanded in-page. Never build one big
// selector string from comma lists — `.a, .b` + ' button' silently becomes
// `.a, .b button`, which also matches the bare `.b` container.
const PROBE = `(() => {
  const SEL = ${JSON.stringify({ navItem: NAV_ITEM, navActive: NAV_ACTIVE, content: CONTENT, overlay: OVERLAY, interactive: INTERACTIVE })}
  const qa = (list, root) => list.flatMap((s) => { try { return [...(root || document).querySelectorAll(s)] } catch { return [] } })
  const uniq = (els) => [...new Set(els)]
  const txt = (el) => el.innerText.replace(/\\s+/g, ' ').trim()

  const navItems = uniq(qa(SEL.navItem))
  const active = navItems.filter((el) => SEL.navActive.some((s) => { try { return el.matches(s) } catch { return false } }))

  // 第一个可见的内容容器，标题只在它内部找
  const content = qa(SEL.content).find((el) => el.offsetHeight > 0) || document.body
  // 标题取第一个，并**必须**回报可见性。
  // 踩过的坑：一个 display:none 的 h2 依然会返回正确的 font-family / font-size，
  // 探针据此会误报「标题排版规则已覆盖」。必须逐级回溯祖先，确认没有被
  // display:none / visibility:hidden 吃掉。
  const title = content.querySelector('h1, h2, h3')
  const isVisible = (el) => {
    if (!el) return false
    const r = el.getBoundingClientRect()
    if (!(r.width > 0 && r.height > 0)) return false
    for (let n = el; n && n !== document.body; n = n.parentElement) {
      const s = getComputedStyle(n)
      if (s.display === 'none' || s.visibility === 'hidden') return false
    }
    return true
  }

  const overlay = uniq(qa(SEL.overlay)).find((el) => getComputedStyle(el).display !== 'none' && el.getBoundingClientRect().height > 0)
  let blocked = []
  if (overlay) {
    const r = overlay.getBoundingClientRect()
    blocked = uniq(qa(SEL.interactive, content))
      .filter((el) => {
        if (overlay === el || overlay.contains(el)) return false
        const b = el.getBoundingClientRect()
        if (!(b.top < r.bottom && b.bottom > r.top && b.width > 1 && b.height > 1)) return false
        const hit = document.elementFromPoint(b.left + b.width / 2, Math.min(b.top + b.height / 2, r.bottom - 2))
        return hit && (hit === overlay || overlay.contains(hit))
      })
      .map((el) => (el.tagName + (el.className ? '.' + String(el.className) : '')).slice(0, 70))
  }
  return {
    navCount: navItems.length,
    active: active.map(txt),
    title: title ? { tag: title.tagName, font: getComputedStyle(title).fontFamily.split(',')[0], size: getComputedStyle(title).fontSize, visible: isVisible(title) } : null,
    overlayHidden: !overlay,
    blocked,
  }
})()`

const report = []
for (const route of ROUTES) {
  await send('Page.navigate', { url: base.replace(/\/$/, '') + route })
  await sleep(3600)
  const info = await ev(PROBE)
  report.push({ route, ...info })
  const flags = []
  if (info.__error) flags.push(`⚠ ${info.__error}`)
  else {
    if (!info.active?.length) flags.push('⚠ 无激活项（孤儿页？）')
    if (info.active?.length > 1) flags.push(`⚠ 多个激活项 ${info.active.length}`)
    if (info.blocked?.length) flags.push(`⚠ 被拖拽层遮挡 ${info.blocked.length}`)
    if (info.title && !info.title.visible) flags.push('⚠ 标题被隐藏（display:none 祖先）')
  }
  const t = info.title ? `${info.title.tag}/${info.title.font}/${info.title.size}${info.title.visible ? '' : ' [隐藏]'}` : '(无)'
  log(`${route.padEnd(28)} 激活=[${(info.active ?? []).join(',')}]  标题=${t}  ${flags.join(' ')}`)
}

if (outPrefix) writeFileSync(outPrefix + '.json', JSON.stringify({ report, consoleErrors: [...new Set(consoleErrors)] }, null, 1))

log('')
log('=== 控制台错误 ===')
if (!consoleErrors.length) log('无')
else [...new Set(consoleErrors)].forEach((e) => log(' -', e))
log('')
log(`汇总：${report.length} 条路由；无激活项 ${report.filter((r) => r.active && !r.active.length).length} 条；有遮挡 ${report.filter((r) => r.blocked?.length).length} 条`)
process.exit(0)
