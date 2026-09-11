# Full-Body Locomotion Grounding

Use this reference only when a shot visibly depends on terrestrial full-body walking, running, pursuit, stair/terrain travel, landing, stopping, turning, or garments reacting around the legs. Do not activate it automatically for close-ups, flight, suspended motion, or abstract/stylized movement where foot support is not visible.

## Core Model

Treat believable locomotion as one coupled system:

```text
support/contact -> center-of-mass transfer -> push-off/flight
-> terrain response -> secondary motion -> camera-relative motion
```

Do not solve one layer in isolation. A dark shadow under the shoe cannot rescue a sliding pelvis; correct foot placement cannot rescue a camera whose parallax moves at the wrong speed.

## 1. Support And Gait Phase

For each visible step, preserve a readable phase relation:

```text
approach/swing -> foot placement -> load acceptance
-> center passes over support -> push-off -> next support
```

Visible checks:

- the planted foot accepts weight before the other leg becomes free;
- the pelvis travels over the support area instead of gliding as one rigid block;
- torso and arm swing counterbalance the pelvis rather than mirroring it;
- the rear foot pushes off before leaving the ground;
- start, stop, turn, and direction change include a catch step, lean, brace, or braking distance.

Body mass is not a number in the prompt. Translate it into stride compression, vertical rise/fall, footfall impulse, stopping distance, and secondary-motion lag.

## 2. Contact, Friction, And Surface Response

Bind contact cues to the actual surface and light:

- tight contact shadow and occlusion under the loaded foot;
- sole compression or slight edge roll where appropriate;
- friction-consistent grip, slip, scrape, or pivot;
- water, dust, gravel, mud, snow, grass, cloth, or debris responds at the contact point;
- cast-shadow direction remains consistent with the scene light.

Avoid a generic black sticker under every foot. Contact shadow is one cue among occlusion, sole deformation, surface displacement, body loading, and parallax.

## 3. Terrain Adaptation

On stairs, slopes, rubble, roofs, roots, or uneven ground:

- place the foot on a specific support plane;
- adapt ankle, knee, hip height, and stride length to that plane;
- let terrain constrain the body route rather than letting the body clip through it;
- show a recovery step or hand/weapon brace when support becomes uncertain.

Use `inverse-kinematics-like foot placement` only as a semantic shorthand. Prompt the visible result; do not imply that the generator exposes a real IK solver.

## 4. Camera-Subject Velocity Coupling

For walking/running follow shots:

- match the camera's average travel speed to the subject's route;
- preserve slight inertial lag, catch-up, and settle so the camera does not feel mechanically bolted to the hips;
- align background parallax with travel direction and distance;
- keep the support/contact area readable when foot grounding is the proof task;
- allow intentional relative drift only when it has a shot function: subject outruns camera, camera reveals destination, threat gains, or braking becomes visible.

Do not lock the camera literally to every footstep. Exact cadence locking can look robotic. Couple velocity and parallax; preserve human camera inertia.

## 5. Secondary Motion And Collision

Hair, skirts, coats, sleeves, straps, ornaments, tails, and carried props should follow this sequence:

```text
body impulse -> delayed drag -> contact/occlusion around limbs or props
-> overshoot -> gravity/wind settling
```

Keep a real air gap and material weight. Prevent penetration without gluing cloth to the body. The leg should displace fabric; fabric should not reveal an exposed collision mesh or ignore the leg entirely.

## 6. Starts, Stops, Turns, Jumps, And Landings

Walking quality is not enough. Audit transitions:

- **start:** body leans or falls into the first support step;
- **accelerate:** stride length/cadence and camera parallax increase coherently;
- **turn:** outside/inside foot, pelvis, torso, and gaze change line in an ordered way;
- **jump:** takeoff has a loaded support phase and a visible loss of ground contact;
- **gap jump proof:** when the destination is a separate roof, ledge, platform, or terrain plane, include one side/wide view that shows the departure edge, destination edge, short ballistic arc, apex, descent, and landing relation. A close follow shot alone can hide the arc and read as horizontal flight;
- **landing:** feet contact, joints compress, center lowers, secondary motion catches up;
- **stop:** braking step, friction, torso overshoot, and settle resolve the momentum.

## Prompt Translation Rule

Prefer one compact visible contract over a renderer/solver keyword dump:

```text
Full-body movement follows a grounded support cycle: each planted foot accepts weight before the center of mass passes over it and the rear foot pushes off. Ankles, knees, and stride length adapt to the uneven surface; contact points show light-consistent occlusion, sole compression, and material response. The tracking camera matches the subject's average travel velocity with slight inertial lag, while garments and hair react after the body impulse, clear the limbs, overshoot, and settle.
```

Select only the clauses visible in the shot. Do not spend prompt budget on feet, terrain, cloth, and camera coupling when the framing cannot show them.

## Anti-Jargon Gate

Terms such as `RTAO`, `IK`, `collision mesh`, `PBR cloth`, or `velocity matched` are optional compression anchors, not executable engine switches. Keep a term only when it is bound to a visible surface, motion phase, contact point, or camera result.
