# Creative Anchor Framework

## Principle

The user supplies taste, goals, constraints, and any references they happen to know. Codex supplies the missing professional vocabulary.

```text
brief -> known anchors -> functional coverage -> missing identity
-> specialist/research candidates -> compatibility -> division of labor
-> compact anchor stack -> generated evidence -> scoped learning
```

## Functional Audit

| Creative need | Candidate source classes | Specialist |
|---|---|---|
| capture and image finish | film format, lens family, photography process, cinematographer | visual style / material realism |
| composition and camera | director, cinematographer, shot school, documentary/commercial grammar | visual reference / audiovisual language |
| animation energy | animator, studio, animation school, effects tradition | visual reference / kinetic visual master |
| editing rhythm | editor, montage school, genre cutting grammar | audiovisual language / rhythm editing |
| world and objects | production designer, architect, fashion house, craft tradition, design movement | production design |
| character movement | martial art, dance, sport, acting method, stunt discipline | action choreography |
| weapon/prop movement | historical fencing, weapon art, circus/object manipulation, industrial mechanism | action choreography / mechanical transformation |
| partner/ensemble movement | contact improvisation, partner acrobatics, dance partnering, formation systems | action choreography |
| music | composer, genre, regional tradition, ensemble, production school | music and sound |
| sound | sound designer, recording aesthetic, material Foley tradition, mix perspective | music and sound |

## Stack Architecture

Separate the stack into scopes:

```text
global anchors:
  medium + broad aesthetic + broad motion/camera identity

sequence anchors:
  one scene's editing, horror, comedy, chase, ritual, or action behavior

performer anchors:
  body movement + weapon handling + optional partner relation

audio anchors:
  score identity + sound-design identity
```

This permits diversity without forcing every name into the opening sentence.

## Compatibility

Compatible anchors usually control different layers:

```text
large-format cinema -> material and scale
animation studio -> timing and graphic exaggeration
action director -> geography and coverage
martial art -> performer movement grammar
weapon system -> prop trajectory and braking
composer/tradition -> music identity
```

Potential conflict:

- two primary visual mediums;
- two incompatible camera philosophies;
- multiple body systems with opposing stance and rhythm;
- music references with conflicting ensemble, harmony, and production space;
- minimalist design plus uncontrolled maximalist decoration.

Resolve conflict by:

1. choosing a primary anchor;
2. limiting the secondary anchor to one layer;
3. moving a secondary anchor to one sequence or performer;
4. offering separate routes instead of blending.

## Prompt Compression

Preferred:

```text
[anchor]负责[role]，[anchor]负责[role]；[performer]采用[body basis]，
[weapon]采用[weapon basis]，[audio]采用[audio basis]。
```

More compact when roles are obvious:

```text
[媒介/质感锚点]，[视觉或动画锚点]；
[角色A身体基底]＋[角色A武器基底]，[角色B身体/武器基底]，
双人采用[伙伴运动基底]。
```

Add mechanics only when:

- two anchors could conflict;
- the name is niche or inconsistently understood;
- the generated result previously misread the anchor;
- physical or spatial behavior needs a hard guardrail.

## Cross-Genre Examples

These are structural examples, not defaults.

### Restrained Science Fiction

```text
global medium anchor + architectural/design movement
+ cinematography anchor for scale and stillness
+ sound anchor for sparse mechanical space
```

### Historical Or Chinese-Fantasy Drama

```text
period/craft reference + painting or theatrical aesthetic
+ movement basis appropriate to costume and weapon
+ regional instrumentation or opera/rhythm anchor
```

### Fashion Film

```text
fashion house/editorial photography anchor
+ choreographer or dance-form anchor
+ music-production anchor
```

### Horror

```text
horror subgenre/director anchor
+ camera or sound-perspective anchor
+ performer movement basis for creature or possession
```

### Product Or Vehicle Film

```text
industrial-design/brand-language anchor
+ automotive/tabletop cinematography anchor
+ material Foley and engine/mechanical sound anchor
```

### Action

```text
medium/finish anchor + action/animation coverage anchor
+ each performer receives a body basis
+ each unusual weapon receives a handling basis
+ partnership receives a shared-movement basis when relevant
```

## Research Triggers

Research before recommending when:

- the user enters an unfamiliar culture, period, craft, sport, or music tradition;
- a name's actual role is uncertain;
- the anchor is obscure, misspelled, or possibly conflated;
- a current platform's response to names matters;
- the work needs historically or culturally accurate attribution;
- several candidates appear similar and the distinction changes the direction.

Research output should remain compact:

```text
name -> verified contribution -> why it fits -> risk
```

## Learning Boundaries

After output review:

- record what visibly transferred from the anchor;
- separate successful image, camera, movement, and audio layers;
- keep failed interpretations conditional on model/mode;
- store accepted combinations under their genre/use-case;
- never turn one successful stack into a universal house style unless the user explicitly requests one.
