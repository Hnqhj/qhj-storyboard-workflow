# Camera / Director Anchor Atlas

Use when the user asks for director, cinematography, animation-director, or camera-style name anchors such as Hitchcock, Zack Snyder, Hideaki Anno, Kubrick, Kurosawa, Obari, Trigger, or similar.

Do not use names as decoration. Use `anchor-first + scoped role`:

```text
[Name]式[function]: [one visible mechanism].
```

## Suspense / psychological pressure

- **Alfred Hitchcock / 希区柯克** -> subjective suspense, information gap, POV/reaction, Hitchcock zoom / Vertigo effect.
  - Prompt: `希区柯克式主观悬念镜头：先让观众看见危险来源，再切角色反应；短促POV、反应特写和必要时的Hitchcock zoom表现心理失衡。`
  - Avoid: using it as a generic horror filter or applying dolly zoom throughout the clip.
- **Brian De Palma / 德·帕尔玛** -> voyeuristic suspense, foreground/background threat, split-focus / split-screen thinking.
  - Prompt: `德·帕尔玛式前后景窥视构图：前景目标和远景威胁同时清楚，观众提前看见危险但角色仍在行动。`
- **Stanley Kubrick / 库布里克** -> one-point perspective, central symmetry, cold architectural pressure.
  - Prompt: `库布里克式单点透视压迫构图：巨大建筑轴线吞没角色，中心对称和缓慢凝视制造不可逃避的压迫。`

## Hero action / speed ramp / spectacle

- **Zack Snyder / 扎克施耐德** -> speed-ramp hero action, comic-panel slow motion, backlit silhouette.
  - Prompt: `扎克施耐德式速度坡变英雄动作：高速进入，接触前一瞬短暂慢动作展示强剪影和身体张力，命中后立即恢复速度。`
  - Avoid: making the whole sequence slow motion or replacing contact/result with pose.
- **Michael Bay / 迈克尔贝** -> low-angle hero orbit, wide commercial scale, backlight, explosive background motion.
  - Prompt: `迈克尔贝式低机位英雄环绕：超宽画幅、低角度、强背光和短促环绕，背景有巨构和尘埃但主体轮廓清楚。`
- **Tony Scott / 托尼斯科特** -> long-lens compression, high-contrast heat, smoke/reflection, anxious action rhythm.
  - Prompt: `托尼斯科特式高反差动作影像：长焦压缩、强反差色彩、烟尘和反光切割画面，剪辑躁动但围绕同一行动目标。`

## Anime / tokusatsu / graphic action

- **Hideaki Anno / 庵野秀明** -> mechanical insert shots, static pressure, hard cuts, tokusatsu scale, body-part/operation close-ups.
  - Prompt: `庵野秀明式机械与静止压迫镜头：手、脚、护甲、锁扣、武器边缘等局部特写证明动作机制；静止构图与突然硬切交替。`
  - Avoid: copying Eva/Ultraman symbols or turning action into static montage.
- **Hiroyuki Imaishi / 今石洋之** -> extreme momentum, graphic body distortion, explosive perspective, hot-blooded edit energy.
  - Prompt: `今石洋之式极端动势动画镜头：角色身体、衣摆和特效被压成强方向图形，镜头随动作冲破画面；只在爆发段使用夸张透视。`
- **Masami Obari / 大张正己** -> Obari pose, foreground weapon/limb exaggeration, V/X diagonal hero silhouette.
  - Prompt: `大张正己式英雄必杀构图：前景肢体或武器夸张放大，身体形成强斜线和剪影，像一格高张力动画海报。`
- **Satoshi Kon / 今敏** -> match cuts, shape/action inheritance, psychological transitions.
  - Prompt: `今敏式匹配转场：用相同动作方向、形状或前景遮挡完成切换，让上一镜头运动线继承到下一镜头。`
- **Mamoru Oshii / 押井守** -> cold mechanical stillness, rain/reflection/empty-city inserts, aftermath silence.
  - Prompt: `押井守式冷静机械空镜：雨、水面反射、建筑空镜和机械细节给动作前后留下沉默余韵。`

## Spatial movement / staging

- **Akira Kurosawa / 黑泽明** -> environment as motion layer: wind, dust, rain, flags, crowds, clear staging.
  - Prompt: `黑泽明式运动调度：人物动作、风/尘/雨/碎片和背景层形成同向运动，环境证明力量和空间关系。`
- **Steven Spielberg / 斯皮尔伯格** -> point-of-thought, camera follows realization, reaction-to-wonder/threat reveal.
  - Prompt: `斯皮尔伯格式point-of-thought镜头：从角色反应出发，顺着意识转向刚刚发现的威胁或奇观。`
- **Alfonso Cuarón / 阿方索卡隆** -> immersive long take, continuous spatial pressure.
  - Prompt: `卡隆式沉浸长镜头：镜头持续跟随角色穿过空间，危险从前景、侧面或背景不断进入画面。`

## Subjective impact / montage

- **Sam Raimi / 山姆雷米** -> subjective rush camera, Dutch angle, sudden push-in, comic-horror impact.
  - Prompt: `山姆雷米式主观冲撞镜头：镜头像一股有实体的力量高速冲向角色，短促荷兰角和突然推近制造失衡感。`
- **Edgar Wright / 埃德加赖特** -> rhythmic montage, prop/hand/foot inserts, sound-synced action.
  - Prompt: `埃德加赖特式节奏蒙太奇：手、脚、护甲、道具和眼神用快速特写卡点连接，动作与声音同步。`

## Common stacks

- Dark temple / pressure: `库布里克式单点透视压迫 + 庵野秀明式机械局部特写 + 希区柯克式主观悬念`.
- Superhuman fantasy impact: `扎克施耐德式速度坡变 + 大张正己式必杀构图 + sakuga impact frame + 黑泽明式环境运动层`.
- Rogue / first-person ambush: `希区柯克式信息差悬念 + 山姆雷米式主观冲撞 + 德·帕尔玛式前后景窥视构图`.
- Mechanical / biomecha action: `庵野秀明式机械局部特写 + 押井守式机械空镜 + PGR式机械动作节奏`.

Guardrail: names do not replace shot grammar. Every selected anchor must still serve a shot function: establish, reveal, contact, displacement, scale, consequence, transition, or final icon.
