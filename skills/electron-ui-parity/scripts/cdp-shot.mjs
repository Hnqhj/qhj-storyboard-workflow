#!/usr/bin/env node
// Capture a clipped region of a CDP page at high DPI, for close-up inspection.
// usage: node tmp-shot.mjs <port> <url> <out.png> <x> <y> <w> <h> [scale]

import { writeFileSync } from 'node:fs'

const [port, url, out, x, y, w, h, scale = '2'] = process.argv.slice(2)
const sleep = (ms) => new Promise((r) => setTimeout(r, ms))

const targets = await (
  await fetch(`http://127.0.0.1:${port}/json/list`, { signal: AbortSignal.timeout(8000) })
).json()
const page = targets.find((t) => t.type === 'page')
const ws = new WebSocket(page.webSocketDebuggerUrl)
let id = 0
const pending = new Map()
ws.addEventListener('message', (e) => {
  const m = JSON.parse(e.data)
  if (m.id && pending.has(m.id)) {
    pending.get(m.id)(m)
    pending.delete(m.id)
  }
})
await new Promise((res) => ws.addEventListener('open', res))
const send = (method, params = {}) =>
  new Promise((res) => {
    const i = ++id
    pending.set(i, res)
    ws.send(JSON.stringify({ id: i, method, params }))
  })

await send('Page.enable')
await send('Runtime.enable')
await send('Emulation.setDeviceMetricsOverride', {
  width: 1440,
  height: 960,
  deviceScaleFactor: 2,
  mobile: false,
})
await send('Page.navigate', { url })
await sleep(4500)
const shot = await send('Page.captureScreenshot', {
  format: 'png',
  clip: { x: +x, y: +y, width: +w, height: +h, scale: +scale },
})
writeFileSync(out, Buffer.from(shot.result.data, 'base64'))
console.log('wrote', out)
ws.close()
process.exit(0)
