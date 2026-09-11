# Contact And Constraint Topology

Use this reference when motion credibility depends on two or more bodies, props, vehicles, creatures, garments, or environmental surfaces remaining physically related through support, attachment, collision, guidance, or release.

## Core Question

Do not animate each object independently. Build the relation first:

```text
support/attachment -> load transfer -> relative motion limit
-> reaction/lag -> release or new constraint
```

For every important relation, answer:

- what touches, supports, holds, carries, guides, or blocks what?
- where is the contact point or contact area?
- which degrees of freedom remain available?
- where does load, recoil, drag, or torque travel?
- what visible response proves the relation?
- how does the relation release, break, slide, pivot, or become the next relation?

## Common Topologies

### Foot / Ground

The loaded foot supports the center of mass; friction limits slip; surface response and contact occlusion prove weight. Use the full-body locomotion reference for gait.

### Hand / Prop Or Weapon

Grip position, finger wrap, palm contact, wrist line, and object inertia must agree. A carried object can lag or pull the arm, but it cannot float beside the hand. Regrip, hand slide, or release must be visible when leverage changes.

### Body / Wall, Seat, Ledge, Or Floor

Define the supporting area: palm, shoulder, hip, back, knee, or pelvis. The supported body compresses or redirects around that area; the surface receives pressure, scrape, vibration, or deformation.

### Body / Body

A grab, bind, throw, carry, clinch, collision, or linked rotation creates one temporary mechanical system. Contact changes both bodies. Show shared recoil, displaced balance, grip maintenance, and a clear separation or new hold.

### Rider / Vehicle Or Creature

The pelvis/feet/hands form support points; suspension, gait, or vehicle acceleration reaches the rider with a delay. The rider counterbalances instead of floating in a fixed pose. Reins, seat, stirrups, handlebars, saddle, or body grip should have a visible function when present.

### Airborne Body / Gravity

Takeoff defines initial velocity and rotation; gravity bends the trajectory; limbs and cloth reorient around angular momentum; landing creates compression, recoil, and settling. Camera movement cannot replace a readable launch and landing relation.

### Hinged, Sliding, Tethered, Or Flexible Object

Doors rotate around hinges; drawers and rails translate along guides; cables and chains carry tension; cloth and flexible weapons transmit waves with delay. Preserve the pivot, guide, anchor, slack/tension state, and propagation direction.

## Prompt Translation

Write the visible relation, not a solver name:

```text
Her palm and forearm stay loaded against the wall as her center swings around that support; the shoulder compresses, the coat trails behind, then the hand releases only after both feet recover beneath her.
```

```text
The rider's hips remain seated while the mount's stride lifts and drops the saddle; hands and knees absorb the delayed motion, cloth and reins react one beat later, and the camera follows the pair as one moving mass.
```

Use one or two decisive constraint relations per beat. Do not turn the final prompt into a physics report.

## Failure Fingerprints

- foot, hand, weapon, or rider floats near its support without carrying load;
- contact affects only one participant;
- cloth/chain/tail moves without an anchor or propagation delay;
- a door, wheel, limb, or tool ignores its pivot or joint;
- a jump begins without takeoff or ends without landing compression;
- a grip, bind, seat, or tether vanishes between frames with no release event;
- camera movement fakes travel while the physical relation remains unchanged.

