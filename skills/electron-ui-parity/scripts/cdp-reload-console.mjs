/**
 * 重载页面并在整段时间内捕获控制台输出与异常。
 *
 * 用途：确认「边恢复失败」时 Vue Flow 到底有没有报错。
 * 已有的驱动脚本是在页面就绪之后才挂上监听的，重载瞬间的错误会被漏掉。
 */
const [, , portArg, url, payloadJson] = process.argv
const PORT = Number(portArg || 9334)
const BASE = `http://127.0.0.1:${PORT}`

const sleep = (ms) => new Promise((r) => setTimeout(r, ms))

async function listTargets() {
  const res = await fetch(`${BASE}/json/list`)
  return res.json()
}

class Cdp {
  constructor(ws) {
    this.ws = ws
    this.id = 0
    this.pending = new Map()
    this.events = []
    ws.addEventListener('message', (ev) => {
      const msg = JSON.parse(ev.data)
      if (msg.id && this.pending.has(msg.id)) {
        const { resolve, reject } = this.pending.get(msg.id)
        this.pending.delete(msg.id)
        if (msg.error) reject(new Error(JSON.stringify(msg.error)))
        else resolve(msg.result)
      } else if (msg.method) {
        this.events.push(msg)
      }
    })
  }
  send(method, params = {}) {
    const id = ++this.id
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject })
      this.ws.send(JSON.stringify({ id, method, params }))
    })
  }
}

async function connect(wsUrl) {
  const ws = new WebSocket(wsUrl)
  await new Promise((resolve, reject) => {
    ws.addEventListener('open', resolve)
    ws.addEventListener('error', reject)
  })
  return new Cdp(ws)
}

async function main() {
  const targets = await listTargets()
  const page = targets.find((t) => t.type === 'page' && t.url.startsWith('http://127.0.0.1:5179'))
  if (!page) throw new Error('找不到 5179 的页面目标')
  const cdp = await connect(page.webSocketDebuggerUrl)
  await cdp.send('Runtime.enable')
  await cdp.send('Log.enable')
  await cdp.send('Page.enable')

  // 注入存档
  await cdp.send('Runtime.evaluate', {
    expression: `window.localStorage.setItem('nexusvault-canvas', ${JSON.stringify(payloadJson)})`,
    returnByValue: true,
  })

  cdp.events.length = 0
  await cdp.send('Page.reload', { ignoreCache: false })
  await sleep(6000)

  const logs = []
  for (const ev of cdp.events) {
    if (ev.method === 'Runtime.consoleAPICalled') {
      logs.push({
        type: ev.params.type,
        text: (ev.params.args || [])
          .map((a) => a.value ?? a.description ?? a.type)
          .join(' ')
          .slice(0, 300),
      })
    } else if (ev.method === 'Runtime.exceptionThrown') {
      logs.push({
        type: 'exception',
        text: (ev.params.exceptionDetails?.exception?.description || '').slice(0, 300),
      })
    } else if (ev.method === 'Log.entryAdded') {
      logs.push({
        type: `log:${ev.params.entry.level}`,
        text: String(ev.params.entry.text || '').slice(0, 300),
      })
    }
  }

  const state = await cdp.send('Runtime.evaluate', {
    expression: `(() => ({
      nodes: document.querySelectorAll('.vue-flow__node').length,
      edges: document.querySelectorAll('.vue-flow__edge').length,
      edgeIds: [...document.querySelectorAll('.vue-flow__edge')].map(e => e.getAttribute('data-id')),
      storedEdges: (JSON.parse(window.localStorage.getItem('nexusvault-canvas'))||{}).edges,
    }))()`,
    returnByValue: true,
  })

  console.log(JSON.stringify({ state: state.result.value, logs }, null, 2))
  process.exit(0)
}

main().catch((err) => {
  console.error('PROBE FAILED:', err.message)
  process.exit(1)
})
