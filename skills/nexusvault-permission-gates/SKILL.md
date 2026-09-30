---
name: nexusvault-permission-gates
description: nexusvault-post 的身份/权限门禁清单：两套会话（本机 vs 线上）的判定口径、壳层卡片入口的门禁落点、管理员章节过滤、以及「登录着却弹需要登录」的误报排查
use_when: 在 nexusvault-post 改任何「谁能用/谁看不到」的逻辑（游客/成员/管理员）、新增壳层卡片入口、页面改成卡片、或排查「需要登录」卡片误报时
agent_created: true
---

# nexusvault-post 权限门禁清单（2026-09-28 实战沉淀）

## 1. 先分清两套会话（一半的 bug 从这里来）

| | 本机会话 | 线上会话 |
| --- | --- | --- |
| 存哪 | 内存（`setAccessToken`，**不落盘**） | `localStorage`（`nexusvault.remote-access-token` / `remote-user`） |
| 读取 | `auth.isAuthenticated` | `isRemoteSignedIn()` |
| 谁在用 | 侧栏账号卡、Assistant、本地接口 | **广场（发现）的读写全部** |
| 稳定性 | **易失**：重启即丢、`session-expired` 会清 | 落盘，重启后仍在 |

半登录态（线上还在、本机已是访客）会让**只看本机**的守卫误报「需要登录」。
→ 判一个**走线上接口**的动作，必须用线上会话；用户主动路径一律走
`auth.requireLogin(cb)`（它会先试本机静默恢复、再 `adoptRemoteSession()` 补认领）。

## 2. `requireLogin` 的调用约定（最容易写错）

语义：**已登录 → 返回 true 且 `onAuthenticated` 不回调**；恢复/补认领成功 →
**回调**并返回 true；都不行 → 弹「需要登录」卡片、返回 false（登录成功后再回调）。

所以「打开某个东西」只能写进回调，且函数体要先判 `isAuthenticated`：

```ts
function openThing() {
  if (!auth.isAuthenticated) {
    void auth.requireLogin(() => openThing())   // 登录后自动重入
    return
  }
  thingOpen.value = true                        // 这里不要复制「打开」逻辑
}
```

把「打开」也写在函数体里 → 已登录时不会走回调，但恢复路径会回调一次，行为不一致。

## 3. 三条身份判定

- 游客：`auth.isAuthenticated === false`
- 成员：`isAuthenticated` 且 `user.is_system_admin !== true`
- 管理员：`auth.isAdmin`（= `user.is_system_admin === true`）

## 4. ⚠️ 页面 → 壳层卡片 = 路由守卫**静默失效**

`router.ts` 的 `needsAccount`（`meta.requiresAuth` / `meta.admin`）只对**页面**有效 ——
它读 `to.meta`。`notifications` / `settings` 改成壳层卡片后路径只剩 `redirect`，
守卫再也看不到，门禁**不报错、不失败地消失**（症状：游客点得开卡、里面全 401）。

**规矩**：壳层卡片的门禁一律写在**入口函数**里（`AppLayout.openSettings` /
`openNotifications`），不要指望加 meta。当前无任何路由声明这两个 meta，守卫那段
是**备用机制**（页面门禁），不是死代码。

## 5. 卡片内的第二道过滤（管理员章节）

站点参数打的是 `/admin/settings`，非管理员必 403。做法（`SettingsCard.vue`）：

- `canSeeGeneral = computed(() => auth.isAdmin)`，导航项 `v-if="canSeeGeneral"`；
- `openSection('general')` 里再 `if (!canSeeGeneral.value) return`；
- `onMounted` **非管理员直接 `loading = false`、不发请求** —— 否则一开卡就是一条
  必 403 的红错误，用户看着像「功能坏了」。**这条比「界面上看不见」更值得断言**。

入口 + 卡片**判两次是刻意的**：入口那次避免弹出全 403 的卡，卡片那次兜住「将来
多一个入口」。

## 6. 入口不隐藏（产品口径）

用户明确要求：功能**不能因为没登录就从界面消失**（不要用 `v-if="isAuthenticated"`
把入口藏起来）。判定发生在**点下去之后**。改前需确认，别自作主张隐藏入口。

## 7. 测试写法（`apps/web/src/App.test.ts`）

- 挂载整个壳层时**守卫与组件必须共用同一个 pinia**：
  `const pinia = createPinia(); setActivePinia(pinia); app.use(pinia)`
  —— 文件里其它用例是两个实例（只断言渲染，看不出差别），一旦要读
  `auth.isAdmin` 就会各说各话、直接失败。
- 门前断言三件套：`.auth-prompt-card` 出现 ｜ 目标卡为 `null` ｜
  `vi.mocked(globalThis.fetch).mock.calls` 里**没有** `/admin/settings`。
- 侧栏通用入口是 `<button class="sidebar-link">`（卡片型入口没有 `to`），
  按 `textContent` 找；`.settings-nav button` 的 textContent 可用来断言章节列表。

## 8. 门禁命令

```
npm --workspace @nexusvault/web run typecheck
npm --workspace @nexusvault/web run lint
npm run format:check            # 只覆盖 web workspace
npm --workspace @nexusvault/web run test
npm run test:desktop
```

文档同步：`docs/engineering-notes.md` **§43**（三态定义 / 双会话表 / 能力×身份矩阵 /
每个能力的守卫代码位置 / 收口记录）。改权限后必须同步这一节，否则下一个读代码的人
会照着旧矩阵改。
