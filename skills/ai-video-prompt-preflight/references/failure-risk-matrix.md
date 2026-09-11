# Failure Risk Matrix

Use this to predict likely generation failures.

## Face Drift

Causes:

- too many close/far cuts
- strong motion blur over face
- reference role unclear
- style changes between shots

Fix:

- lock identity early
- keep face visible only in planned close-up
- reduce blur on face
- state no age/face/hair drift

## Prop Or Vehicle Morphing

Causes:

- vague silhouette
- multiple reference designs
- transformation language without mechanism
- action hides contact points

Fix:

- lock silhouette, color, material, light positions
- name current form at first frame
- forbid extra copies
- split transformation from action

## Camera Chaos

Causes:

- several camera moves in one shot
- action and camera both too fast
- no screen direction

Fix:

- one camera move per segment
- dominant screen direction
- action clarity beats between camera changes

## Style Drift

Causes:

- mixing photoreal, manga, anime, illustration, cinematic, 3D, and editorial without hierarchy

Fix:

- define one base medium
- define realism level
- define line/rendering/lighting relation
- forbid incompatible looks

## Flat Or Boring Result

Causes:

- no structural turn
- same shot function repeated
- no obstacle or change
- no final payoff

Fix:

- add hook/build/turn/payoff
- make each segment add new information
- add one visible obstacle or reversal

## Weightless Or Unsupported Action

Causes:

- "heavy/powerful" used without a physical profile
- weapon mass distribution not defined
- feet/support hidden or sliding
- contact has no equal-and-opposite response
- follow-through and braking omitted
- superhuman strength treated as zero inertia

Fix:

- define actor-to-load relationship
- classify weapon as grip-biased, balanced, tip-heavy, head-heavy, or flexible-delayed
- lock support, traction, and center path
- add receiver/body/environment response
- show braking and stable recovery
- keep camera wide through the consequence

## Martial Styles Look Identical

Causes:

- only style names were provided
- stance, range, force path, rhythm, defense, and recovery were not translated
- camera effects replaced performer mechanics

Fix:

- use `$action-choreography-reference`
- choose one primary system and at most one secondary
- state visible posture, distance, force path, footwork, response, and recovery signature

## Overloaded Prompt

Causes:

- too many references
- too many named styles
- too many actions
- long negative prompt

Fix:

- prioritize: identity > action > camera > world > material > effects
- remove decorative clauses
- split clip
