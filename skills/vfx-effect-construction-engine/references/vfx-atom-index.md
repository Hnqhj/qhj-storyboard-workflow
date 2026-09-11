# VFX Atom Bank Index

The searchable bank contains **566 bilingual atoms**. Use `../scripts/search_vfx_atoms.py`; do not paste this full bank into a generation prompt.

## Categories

| Category | Count | Role | Family |
|---|---:|---|---|
| 生成 | 40 | formation | energy |
| 运动 | 37 | path | particle-motion |
| 爆发 | 34 | peak | impact-energy |
| 视觉类型 | 25 | carrier | particle |
| 技能释放 | 20 | formation | skill |
| 流动 | 20 | path | energy |
| 科技 | 20 | system-family | technology |
| 聚散 | 20 | path | particle-motion |
| 聚集与吸附 | 20 | formation | energy |
| 自然 | 20 | system-family | elemental-natural |
| 释放后的余韵 | 20 | decay | energy |
| 高级表现 | 20 | presentation | particle-presentation |
| 魔法 | 20 | system-family | magic-ritual |
| 速度变化 | 18 | path | motion-curve |
| 元素 | 16 | system-family | elemental-natural |
| 变化 | 15 | state-change | color-light |
| 生命周期 | 15 | decay | lifecycle |
| 空间分布 | 15 | path | particle-depth |
| 能量聚集 | 15 | formation | energy |
| 射击 | 14 | contact-peak | projectile |
| 终极大招 | 14 | peak | ultimate |
| 斩击 | 13 | contact-peak | weapon-motion |
| 空间 | 13 | system-family | space-time |
| 冲击波 | 12 | contact-peak | impact |
| 命中 | 12 | contact-peak | impact |
| 收尾 | 12 | decay | lifecycle |
| 能量 | 12 | carrier | color-light |
| 光效 | 11 | light-color | color-light |
| 持续技能 | 11 | sustain | sustained-field |
| 时间 | 11 | system-family | space-time |
| 特殊 | 11 | light-color | color-light |
| 召唤 | 10 | system-family | summoning |

## Role Counts

| Role | Count |
|---|---:|
| path | 110 |
| system-family | 110 |
| formation | 95 |
| contact-peak | 51 |
| peak | 48 |
| decay | 47 |
| carrier | 37 |
| light-color | 22 |
| presentation | 20 |
| state-change | 15 |
| sustain | 11 |

## Family Counts

| Family | Count |
|---|---:|
| energy | 115 |
| particle-motion | 57 |
| color-light | 49 |
| elemental-natural | 36 |
| impact-energy | 34 |
| lifecycle | 27 |
| particle | 25 |
| impact | 24 |
| space-time | 24 |
| magic-ritual | 20 |
| particle-presentation | 20 |
| skill | 20 |
| technology | 20 |
| motion-curve | 18 |
| particle-depth | 15 |
| projectile | 14 |
| ultimate | 14 |
| weapon-motion | 13 |
| sustained-field | 11 |
| summoning | 10 |

## Retrieval Examples

```powershell
python scripts/search_vfx_atoms.py "magic circle seal" --limit 8
python scripts/search_vfx_atoms.py "weapon trail" --family weapon-motion --limit 6
python scripts/search_vfx_atoms.py "fade dissipate" --role decay --json
```

Select 4-8 atoms and assign each one a distinct construction job. IDs are internal audit handles and should not enter final prompts.
