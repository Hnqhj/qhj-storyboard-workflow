---
name: kinetic-action-visual-master
description: 高能动作片整片视觉母版：融合电影写实、风格化动画动势、特殊多分镜表达、大景别与角度变化、动作与镜头耦合、因果剪辑与保物理夸张。触发：高速战斗、高能动作视觉母版、多分镜、多景别、多特殊角度、激烈运镜、动作转场、POV 动作、机甲动作。 Establish a reusable whole-film visual master for high-energy AI action videos by combining cinematic realism, stylized animation dynamics, special multi-shot storyboard expression, large shot-scale and angle variation, action-camera coupling, causal cuts and transitions, and physics-preserving exaggeration. Use for 高速战斗, 高能动作视觉母版, 特殊分镜表现手法, 多分镜, 多景别, 多特殊角度, 人物动作与镜头配合, 激烈运镜, 动作转场, 非常规构图, POV动作, giant combat, mecha action, weapon showcases, chases, vehicle action, or when a prompt needs an authoritative opening style block before detailed choreography and shots.
disable-model-invocation: true
---

# Kinetic Action Visual Master

## Purpose

Create the upstream visual generation domain for an entire high-energy action clip. Preserve the excitement of aggressive animation and camera language while keeping materials, bodies, spatial logic, and action causality readable.

This skill writes the compact global block that belongs near the beginning of a final prompt. It does not replace choreography, audiovisual grammar, rhythm, material design, or detailed shots.

## Reference Routing

Read `references/kinetic-action-master-language.md` when building, adapting, or diagnosing a high-energy visual master. It contains the translation table, intensity modes, prompt template, examples, and failure corrections.

## Workflow

1. Lock the medium blend:
   - choose the realism level and the permitted animation exaggeration;
   - default to large-format cinematic material and light behavior plus stylized animation timing.
2. Inventory the user's named anchors, identify what each controls, and proactively fill meaningful gaps through `$creative-anchor-director`; route visual candidates to `$visual-reference-vocabulary` and research uncertain or unfamiliar candidates through `$creative-research-first`.
3. Set the image hierarchy:
   - define contrast, palette ownership, silhouette clarity, highlight control, depth, and scale.
4. Set the kinetic camera envelope:
   - choose a limited family of aggressive camera behaviors appropriate to the action;
   - require every move or cut to inherit a physical, spatial, or editorial trigger.
5. Set the expressive storyboard chain:
   - design multiple shots as one continuous action phrase rather than isolated cool images;
   - vary shot size, camera height, angle, lens relation, foreground/background order, and subjective/objective viewpoint;
   - preserve motion vector, eye trace, action phase, axis, and spatial causality across the changes.
6. Set the shot-scale envelope:
   - allow extreme close-up through extreme wide;
   - make adjacent shots change function, information, scale, or power relation.
7. Couple performer and camera:
   - let body pose, trajectory, acceleration, reversal, contact, and recovery motivate framing and camera response;
   - require the camera to reveal, oppose, chase, receive, or punctuate the action rather than move independently.
   - assign a tracking owner for each force phase: initiator during commitment, contact point at impact, receiver or changed route after force transfer.
8. Set the effects-and-transition envelope:
   - choose a small family of action-sourced transitions;
   - require the incoming shot to inherit direction, shape, occlusion, material, light, or sound from the outgoing shot;
   - use transitions to preserve motion or mark a real state change, not as decoration.
   - keep transition coverage momentary and require the incoming shot to restore subject count, geography, and the changed physical state.
9. Set the density envelope:
   - use longer shots to establish identity, ability ownership, geography, and support;
   - compress shot duration only during escalation, exchange, or decisive transformation;
   - release into a wider consequence, recovery, or stable reveal;
   - do not divide the full duration into equal-length action nodes by default.
10. Bind exaggeration to reality:
   - allow foreshortening, dynamic stretch, speed smear, graphic impact frames, and abrupt scale change;
   - preserve anatomy, support, center path, inertia, contact reaction, braking, and recovery.
11. Lock coherence:
   - preserve axis, screen direction, target relation, scene geography, identity, costume, weapon, and material system.
12. Write one compact paste-ready block:
   - positive direction first;
   - targeted negative constraints in the same block;
   - detailed action beats and shot list come afterward.

## Intensity Selection

- **Controlled cinematic**: unusual framing and scale contrast, restrained camera acceleration, maximum spatial clarity.
- **Aggressive anime-cinematic**: strong foreshortening, near-lens passes, rapid reframing, short controlled rolls, impact-frame accents, and broad shot-scale jumps. Use as the default for high-speed combat.
- **Subjective rupture**: POV or body-adjacent camera, foreground collisions, occlusion cuts, and severe scale distortion. Reserve for short peaks, not the entire clip.

Do not keep every mechanism at maximum intensity. Escalate from a stable spatial anchor into disruption, then return to a legible result or hero frame.

## Evidence-Backed Kinetic Rules

Use these defaults unless the intended style requires a deliberate exception:

```text
stable orientation
-> action-led camera pursuit
-> body/weapon briefly outruns the lens
-> contact lock
-> tracking handoff to recoil or redirected movement
-> readable consequence
```

- Keep camera speed below the leading body, weapon, vehicle, or effect layer.
- Change camera height only when body height, terrain, fall, jump, or scale relation changes.
- Use short arcs around a contact plane; avoid continuous orbit around a centered performer.
- Let extreme close-ups show intent or mechanism, full-body shots prove trajectory and support, and wide shots prove consequence.
- Use effects as color-owned action paths and causal bridges. Never allow a transition effect to erase the performer, weapon, or geography for a sustained interval.
- For transformation, show the old state, active boundary, and completed new state together whenever possible. Move one transformation frontier through the body or object rather than changing everything simultaneously.

## Semantic Anchor Rules

- Preserve deliberate director, studio, film, genre, cinematography, animation, and movement-style names in the final prompt. Treat them as high-density semantic anchors, not disposable labels.
- Use anchor-first syntax: keep the user's compact term verbatim, then add only the minimum visible controls needed to resolve ambiguity, conflict, or a known generation failure.
- Do not automatically replace one effective named anchor with a long descriptive paragraph. Expansion can dilute model attention and lose the reference prior.
- Combine a small number of compatible anchors. If two anchors conflict, keep the primary anchor and state the intended division of labor, such as material realism from one and motion language from another.
- Do not expect the user to know every useful reference. Audit missing medium, camera, animation/editing, body-movement, weapon-movement, and partner-interaction lanes; propose only anchors that add a distinct function.
- Apply the same rule to movement systems: preserve names such as Capoeira, tricking, fencing, or Peking-opera movement as the action basis; append brief mechanics only when needed for identity, physics, or interaction.
- Interpret “break conventional composition” as asymmetry, obstruction, severe perspective, unusual height, axial depth, negative-space imbalance, or abrupt scale contrast—not loss of geography.
- Interpret “free camera” as a permitted motion envelope—not simultaneous orbit, roll, crash zoom, shake, and whip pan.
- Interpret “fast and overwhelming” as high information density with hierarchy—not random cuts.
- Interpret “many cuts” as a non-uniform density curve—readable setup, compressed escalation, brief peak, and visible consequence—not equal-duration slicing.
- Interpret “special storyboard expression” as a designed chain of contrasting shot functions, scales, heights, angles, foreground relations, and viewpoints whose action vector and spatial logic remain continuous.
- Interpret “action works with the camera” as reciprocal choreography: the performer's pose and path create the camera opportunity, while framing and camera motion clarify or amplify that same physical action.
- Interpret “physical but exaggerated” as realistic force and recovery beneath stylized poses, timing, smears, and impact frames.
- Interpret “special effects and transitions” as a causal bridge: outgoing action/effect source -> frame coverage or matched feature -> incoming image inherits the vector/shape/light/sound -> geography or changed state becomes readable.
- Replace ambiguous rotation labels with a visible range such as a short controlled 45–90° partial roll. Avoid continuous spinning unless the subject itself motivates it.

## Combination Order

For action-video work, combine this skill with:

1. `$visual-style-aesthetic-direction` for the broader aesthetic and palette system.
2. `$kinetic-action-visual-master` for the whole-film kinetic envelope.
3. `$cinematic-audiovisual-language` for shot function, axis, geography, staging, and cut reason.
4. `$action-choreography-reference` for movement grammar and physical causality.
5. `$action-rhythm-editing` for timing, peaks, impact, and settling.
6. `$high-tension-shot-design` for one dominant tension mechanism per beat.
7. `$ai-material-realism` for material, light, optics, contact, and motion credibility.

Planning may follow that order. In the final generation prompt, place the completed visual-master block before detailed action and shot instructions.

## Output Contract

Return:

1. `【高能动作视觉母版】` — one authoritative whole-film block.
2. Optional intensity label and one-sentence rationale when useful.
3. The rest of the prompt only if requested.

Keep it compact enough to remain authoritative. Prefer three dense paragraphs over a long vocabulary dump.

## Quality Gate

- The medium blend is visible and internally compatible.
- Aggressive camera language has a limited envelope and causal triggers.
- Unconventional framing preserves action axis, geography, and target relation.
- Shot-scale variety changes information, not only decoration.
- Multi-shot, multi-scale, and special-angle changes form one continuous readable phrase rather than a collection of disconnected hero shots.
- Performer action and camera behavior visibly amplify each other without the camera replacing the action.
- Animation exaggeration preserves anatomy and action physics.
- Deliberate named references and martial/movement bases remain visible as compact anchors; support language clarifies rather than replaces them.
- Fast editing still reveals approach, contact, reaction, displacement, and end state.
- Camera tracking ownership follows initiative and force transfer; the lens does not attempt to follow every participant simultaneously.
- Shot density has an intentional rise and release.
- Effects and transitions originate from visible action or sound and carry at least one readable element across the cut.
- The master block controls every later shot and appears before them.
- Negative constraints target camera chaos, spatial drift, anatomy failure, weight loss, and unreadable effects.

## Guardrails

- Do not promise defect-free generation; write observable anatomical and continuity constraints.
- Do not use constant POV, fisheye, Dutch angle, camera roll, or shake across the full clip.
- Do not let the camera provide all the energy while performers remain generic.
- Do not let effects conceal body mechanics, contact, weapon path, or environmental response.
- Do not use unrelated portal, glitch, flash, particle, or whip transitions merely because the edit needs energy.
- Do not reopen the medium, palette, material family, or realism level inside individual shots.
