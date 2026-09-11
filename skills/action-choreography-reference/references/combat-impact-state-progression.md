# Combat Impact And State Progression

Read this reference when a fight contains several exchanges and an earlier hit, fatigue, damaged equipment, altered terrain, or lost initiative must change what can happen later. It owns **impact evidence allocation, irreversible combat-state mutation, and visible counter opportunities**. It does not own platform prompt syntax, exact edit timing, or general entity asset management.

## 1. Scale Impact Evidence To Narrative Weight

Treat impact as a causal evidence ladder rather than a mandatory checklist:

```text
commitment cue
-> visible contact or near-miss relation
-> local material response
-> body/weapon recoil and spacing change
-> delayed secondary inertia
-> environment propagation
-> tactical consequence
```

Use only the layers the framing can prove. A blocked wrist contact in a medium shot may need weapon deflection, foot correction, and a changed line; it does not need debris, a camera shock, or a full-body launch. Reserve the longest chain for the decisive peak.

### Impact Grades

| Grade | Minimum visible allocation | Typical consequence |
| --- | --- | --- |
| Probe | contact/near-miss relation + micro correction | information gained, guard tested, line exposed |
| Effective | local deformation/deflection + forced step, fold, or guard change | distance, line, or initiative changes |
| Major | body/weapon displacement + delayed inertia + equipment or environment proof | balance breaks, route closes, capability degrades |
| Decisive | full readable chain + brief audiovisual accent + persistent tactical consequence | objective access, disarm, collapse, escape, capture, or clear reversal |

The grade is an allocation decision, not a demand for larger effects. A quiet decisive contact can be proved by a broken stance, dropped object, failed grip, interrupted breath, and the opponent taking the route.

## 2. Build A Combat Mutation Ledger

For multi-exchange fights, track only changes that constrain later choices:

```text
beat:
body/support state A | body/support state B:
fatigue/breath:
weapon/equipment function:
environment/route state:
distance/initiative/objective access:
irreversible mutation:
next action source:
```

Compact table form:

| Beat | Body/support | Breath/fatigue | Weapon/equipment | Environment/route | Distance/initiative | Persistent mutation | Next source |
| --- | --- | --- | --- | --- | --- | --- | --- |

### Persistence Rules

1. **Body state persists.** A compromised support leg changes stance width, route, braking, or preferred side. A strained grip changes guard and legal weapon functions. Describe the visible performance consequence, not anatomical injury instructions.
2. **Fatigue changes grammar.** As exertion rises, recovery lengthens, breath becomes visible, amplitude shrinks, posture lowers, and economical answers replace decorative motion. Do not merely add sweat while preserving identical movement.
3. **Equipment changes the action vocabulary.** A bent guard, loose strap, damaged shield, shortened weapon, or lost prop removes some options and creates others.
4. **Environment remembers contact.** A displaced table, wet patch, broken railing, dust cloud, fallen cloth, or cracked surface remains in the geography and can redirect later movement.
5. **Initiative and objective access persist.** A fighter who lost the inside line, route, high ground, or protected object does not regain it without a visible reversal source.
6. **Every mutation must pay off.** If a change never alters a later choice, remove it from the ledger and keep it as local texture.

When a mutation must persist across shots, clips, episodes, or tools, hand the approved state change to `$entity-continuity-system` as an entity/state update. Per-hit micro-reactions stay here and do not enter the long-term asset record.

## 3. Design Counter Opportunities From Recovery

A counter must arise from an observable temporary loss of control, not from a timer appearing in the prompt.

### Counter-Window Families

| Window | Visible condition | Plausible answer | Required state change |
| --- | --- | --- | --- |
| Overcommitment/recovery | swing passes the line, weight travels too far, weapon needs braking | exit the threat line, jam, redirect, take the outside route | initiative or angle changes |
| Balance loss | foot skids, stance narrows, support point fails, torso crosses the base | displace, pin, force a level change, deny the recovery step | balance, elevation, or route changes |
| Breath/regrip/hand switch | breath breaks, grip loosens, hand changes position, equipment must reset | close distance, steal the line, deny the prop, escape | weapon function, distance, or objective access changes |

The counter window is open only while the condition is visible. Once braking, support, breath, or grip is restored, the window closes. The response should use the exact state created by the prior exchange.

## 4. Timing Confidence And Coverage

For generative-video prompts, default to relative causal timing:

```text
readable preload -> short commitment -> contact/deflection
-> delayed response -> brake/recovery -> counter opportunity or stable state
```

Use exact frames or milliseconds only when a real clock controls the work: animation blocking, mocap cleanup, previs, edit design, or synchronization to inspected audio. Otherwise hand relative timing and mass profile to `$action-rhythm-editing`; invented millisecond precision reduces reliability without increasing physical accuracy.

Contact does not automatically require its own shot. Keep it in the same shot when framing already proves the line, contact, reaction, and changed state. Add an insert or coverage cut only when the decisive relation would otherwise be unreadable. Shot density follows the proof task and generation budget, not a universal shots-per-second rule.

## 5. Compact Downstream Handoff

Before platform compilation, reduce the design to:

```text
impact grade:
contact plane and visible relation:
local material response:
forced body/weapon/spacing change:
delayed inertia or environment propagation:
persistent mutation:
counter window or next-action source:
end state:
```

The downstream prompt should express these as natural visible causality. It should not expose the ledger, grade labels, frame calculations, or analytical headings unless the user explicitly asks for a technical breakdown.

## Quality Gate

- Each important contact has enough evidence for its grade and framing.
- At least one body, weapon, spacing, route, environment, initiative, or objective state changes after an effective-or-higher impact.
- Persistent changes constrain later action instead of resetting between beats.
- A counter uses a visible recovery, balance, breath, grip, or equipment condition created by the prior exchange.
- Exact timing appears only when an inspected clock, edit, previs, mocap, or audio reference justifies it.
- Camera shock, particles, and sound accents support the physical result rather than replacing it.
