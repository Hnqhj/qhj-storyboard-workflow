# Camera Motion

Use this when the user asks for 运镜, camera movement, or image-to-video tension.

## Emotional Camera Moves

Slow push-in:

- Use for realization, dread, decision, intimacy, suppressed emotion.
- Prompt: `camera slowly pushes in toward the subject's eyes, shallow depth of field, tension building without changing composition too much`.

Pull-out:

- Use for isolation, helplessness, reveal of larger danger, emotional distance.
- Prompt: `camera slowly pulls back, revealing the subject as small inside a larger threatening space`.

Lateral tracking:

- Use for chase, surveillance, ritual walk, fashion runway energy, tactical motion.
- Prompt: `camera tracks sideways parallel to the subject, foreground objects sliding past to create parallax`.

Forward tracking:

- Use for pursuit, entering danger, heroic approach, momentum.
- Prompt: `camera glides forward behind/alongside the subject, environment rushing past in controlled parallax`.

Arc/orbit:

- Use for power shift, confrontation, unstable relationship, character aura.
- Prompt: `camera makes a slow 30-degree arc around the subject, background drifting to create unease`.

Whip pan:

- Use for sudden reveal, impact transition, action direction switch.
- Prompt: `a rapid whip pan snaps from [A] to [B], brief motion blur, landing on the new subject sharply`.

Dolly zoom / vertigo effect:

- Use for shock, realization, psychological rupture, supernatural pressure.
- Prompt: `subtle dolly zoom effect, the subject stays the same size while the background stretches and compresses, creating disorientation`.

Camera roll / dutch rotation:

- Use sparingly for collapse, madness, reality shift.
- Prompt: `very slight camera roll, horizon tilts slowly, creating unease without spinning`.

Handheld:

- Use for panic, documentary realism, danger, unstable body movement.
- Prompt: `controlled handheld camera, small human shake, urgent but readable`.

Locked-off:

- Use for dread, ritual, surveillance, absurdity, impact contrast.
- Prompt: `locked-off camera, no camera movement, tension comes from subject motion and silence`.

## AI Video Rules

For 5 seconds, choose one:

- slow push-in
- slow pull-out
- slight lateral slide
- controlled handheld
- small arc
- locked camera

Avoid stacking camera moves. If the prompt says "push in, orbit, tilt up, zoom, handheld, whip pan" in one shot, video models often drift or lose subject consistency.

## Action Camera Relay

For a combat exchange, pursuit contact, or weapon bind:

```text
track the initiator
-> let the fastest limb/weapon/vehicle layer cross the foreground ahead of the camera
-> briefly reduce camera speed at contact
-> continue along the receiver's recoil or redirected path
-> widen or stabilize on the changed spacing
```

Constraints:

- assign one tracking owner at a time;
- keep camera speed below the leading action layer;
- use a short arc only to reveal a contact plane or power shift;
- let jumps, falls, low sweeps, and terrain changes motivate elevation;
- never use sustained foreground coverage as a substitute for showing contact and consequence.

## Prompt Formula

```text
镜头为[时长]，相机[one camera move]，主体[one body/object action]，环境[one secondary motion]，速度[slow / sudden / controlled / accelerating]，最终落点为[emotion or visual reveal]。
```

## Negative Camera Constraints

```text
不要快速乱晃，不要突然拉远，不要无意义旋转，不要多重运镜叠加，不要镜头漂移，不要主体跑出画面，不要改变视角到无法识别角色。
```
