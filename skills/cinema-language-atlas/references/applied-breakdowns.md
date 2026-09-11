# Applied Breakdowns

Last researched: 2026-06-28
Status: applied validation reference, not capsule-promoted

Use this file for compact scene applications that test whether the atlas methods work on actual sequences. Prefer public, inspectable, educational, or rights-clear material. Do not reproduce long scripts, articles, subtitles, or full shot lists from copyrighted sources.

## Research Questions

1. Can the shot-by-shot table handle a real short segment without becoming only plot summary?
2. Which fields actually help convert observation into future shot design or AI video prompts?
3. Which mechanisms are portable, and which are tied to the film's historical mode or production context?
4. What additional evidence is needed before any applied lesson becomes a capsule candidate?

## Case 1 - The Great Train Robbery (1903), Opening Robbery Setup

Source / film example -> Edwin S. Porter's The Great Train Robbery, produced by Edison Manufacturing Co., using Library of Congress viewing copy and MoMA collection notes.

Selected segment -> Opening robbery setup: bandits enter the railroad office, control the operator, use telegraph/train-stop information, and transfer the threat toward the train. Exact timecodes are copy-dependent, so this validation uses shot/order IDs rather than frame-accurate times.

Copyright / access boundary -> Library of Congress provides a digital viewing copy and notes that it is not aware of U.S. copyright or other restrictions in the vast majority of these collections, but rights assessment remains the user's responsibility. For future publication, cite LoC/MoMA records and verify the intended use.

Scene question -> How can early cinema establish coercion, objective, offscreen train space, and next action route using static tableau staging, props, and sequential scene logic rather than modern coverage?

Dramatic change -> The office changes from controlled railway workspace into a coerced command point that redirects the train into the robbery plot.

### Compact Shot Rows

```text
shot_id: GT-01
timecode: copy-dependent opening shot
technical evidence: static wide/tableau interior; railroad office; operator, door, window/telegraph area, bandits entering and dominating space
dominant_track: blocking + prop_material
viewer information shift: ordinary work space becomes threat space; telegraph/operator become tools of control
shot_function: orient_space + route_attention + reveal_or_withhold
neighbor_relation: establishes the robbery mechanism before the film moves to the train
prompt_control: "hold a static wide office tableau; let intruders cross from entry to operator; make the telegraph desk the objective; use blocking rather than close-ups to show coercion"
misuse_boundary: do not copy static tableau for modern tension unless the scene benefits from procedural clarity or theatrical distance
validation_status: source-backed applied note, not frame-count verified

shot_id: GT-02
timecode: same opening setup, intra-shot state change
technical evidence: bandits force the operator into action, then neutralize him; action is readable through full-body staging and prop interaction
dominant_track: performance + prop_material
viewer information shift: coercion produces a concrete operational result; the victim is removed as an active obstacle
shot_function: prove_contact_or_causality + state_change
neighbor_relation: turns threat into actionable plot causality
prompt_control: "show the victim forced to operate the necessary device, then physically removed from control; make the changed state visible before cutting away"
misuse_boundary: do not represent real harm instructions; focus on visible state change and fictional staging
validation_status: source-backed applied note, not capsule-promoted

shot_id: GT-03
timecode: following train/water-tank/boarding setup, copy-dependent
technical evidence: exterior train geography follows from the office coercion; the action moves from command point to target vehicle
dominant_track: image + blocking
viewer information shift: offscreen instruction becomes visible train action; audience maps office objective to train route
shot_function: carry_action_continuity + orient_space
neighbor_relation: validates why the office scene mattered
prompt_control: "after command-space coercion, cut to the target vehicle obeying or entering the trap; preserve cause-effect by making the next location answer the previous action"
misuse_boundary: avoid claiming modern cross-cutting unless the edit clearly alternates simultaneous spaces; here the safe portable mechanism is cause-effect scene succession
validation_status: source-backed applied note, with historical caution
```

### Function Chain

```text
orient_space -> route_attention -> prove_contact_or_causality
-> state_change -> carry_action_continuity -> punctuate_transition
```

### Portable Mechanisms

- `command-space before action-space`: show the place where a later action is caused before showing the action itself.
- `prop as plot hinge`: a telegraph, phone, switch, screen, keycard, weapon case, or map can convert threat into operational change.
- `intra-shot state change`: a static wide shot can still carry progression if blocking clearly changes control, access, or body state.
- `cause-effect scene succession`: the next location should answer the previous location's action, even without modern coverage.

### Non-Portable Details

- Early-1900s tableau distance, theatrical blocking, silent-film acting scale, and exhibition context should not be treated as general modern style defaults.
- The film's historical importance is not proof that every technique is best practice today.
- Claims about "first" or "invented cross-cutting" are risky; source notes and scholarship show that early-film history is more contested than simple origin myths.

### Candidate Capsule Decision

No capsule promotion. This is the first applied validation and is based on a historically specific early-cinema segment. The `command-space before action-space` mechanism is promising, but it needs a second independent context such as a modern heist, control-room, surveillance, or military command scene before capsule candidacy.

## Case 2 - The Silence Of The Lambs (1991), FBI Raid / Doorbell Crosscutting

Source / film example -> Jonathan Demme's The Silence of the Lambs, climax crosscutting between Clarice Starling, FBI agents, and Buffalo Bill. This case uses Oklahoma State's open textbook explanation, Filmsupply's parallel-editing article, Manhattan Edit Workshop / Craig McKay professional context, and publicly accessible secondary discussion. It does not reproduce the film's dialogue or full shot list.

Selected segment -> The crosscutting near the climax where the film makes the viewer assume that the FBI team's action and Buffalo Bill's reaction belong to the same house, then reveals that Clarice is at the actual location while the team is elsewhere.

Copyright / access boundary -> The film is copyrighted. Use this only as compact critical analysis with citations; do not reproduce dialogue, frames, or a full shot-by-shot transcription.

Scene question -> How can parallel editing exploit the viewer's learned continuity assumptions so that an apparent rescue/action convergence becomes a suspenseful misdirection?

Dramatic change -> The audience's assumed spatial map flips: the official tactical team is revealed to be in the wrong action space, while the isolated investigator is in the true danger space.

### Compact Shot Rows

```text
shot_id: SL-01
timecode: climax crosscutting, exact timing copy-dependent
technical evidence: alternating FBI raid preparation / Clarice following her lead / Buffalo Bill in his space
dominant_track: cut + blocking
viewer information shift: three lines of action are presented as temporally urgent and spatially converging
shot_function: contrast_parallel + orient_space
neighbor_relation: builds an assumed continuity contract across separated spaces
prompt_control: "intercut tactical team, lone investigator, and hidden target so viewers infer convergence; keep visual/sound cues compatible enough to imply one location"
misuse_boundary: only use if the audience has enough cues to form a clear assumption; vague geography alone is not a twist
validation_status: source-backed applied note

shot_id: SL-02
timecode: doorbell/alarm/reaction sequence, exact timing copy-dependent
technical evidence: a doorbell/ring cue, a target reaction, and a tactical entry are cross-associated by cut order and sound-image expectation
dominant_track: sound + cut
viewer information shift: viewer links sound/action cues across spaces and believes the team is at the correct house
shot_function: connect_look_object + sound_bridge + reveal_or_withhold
neighbor_relation: uses learned parallel-editing convention to create a false spatial answer
prompt_control: "let an offscreen sound/action cue appear to answer a different location's action; preserve plausible simultaneity until the reveal"
misuse_boundary: avoid cheating with impossible information; the false link should come from withheld geography, not contradiction
validation_status: source-backed applied note

shot_id: SL-03
timecode: reveal of wrong house / Clarice at true door, exact timing copy-dependent
technical evidence: FBI entry yields empty/wrong location; cut reveals the true door connection belongs to Clarice's location
dominant_track: cut + performance
viewer information shift: official rescue frame collapses; isolated protagonist becomes the real point of danger and competence
shot_function: reveal_or_withhold + isolate_subjectivity + status_shift
neighbor_relation: flips the prior parallel-editing contract and reassigns danger
prompt_control: "after building a false convergence, reveal the tactical team in the wrong space and the lone character at the true threshold; let the reveal change both danger and character status"
misuse_boundary: do not use purely for cleverness; the misdirection must express character, theme, or power relation, not only a puzzle trick
validation_status: source-backed applied note
```

### Function Chain

```text
contrast_parallel -> orient_space -> sound_bridge
-> reveal_or_withhold -> status_shift -> isolate_subjectivity
```

### Portable Mechanisms

- `assumed-continuity trap`: crosscutting can make the viewer connect two actions as one location or causal chain, then reveal the connection was false.
- `sound/action false answer`: a sound or action cue can appear to answer an action in another space, creating an apparent match that later flips.
- `official action versus lone discovery`: cutting can make institutional force appear central while the actual danger belongs to an isolated character.
- `misdirection with thematic payload`: the twist should alter character status, competence, danger, or theme, not only surprise the audience.

### Non-Portable Details

- Do not copy the specific FBI/serial-killer scenario, doorbell staging, or film dialogue.
- Do not assume every parallel-edit sequence should trick the viewer. Most parallel editing clarifies simultaneity or mutual dependence.
- Do not use false geography if it breaks previously established facts; the audience should feel reoriented, not lied to.

### Candidate Capsule Decision

This provides a second independent context for a broader mechanism: control/action or parallel-action edits create a spatial contract. The contract can be truthful (`command-space before action-space`) or deceptive (`assumed-continuity trap`). This is suitable for a cautious candidate capsule, not activation, because it still needs a future prompt/output application.

## Prompt Application Test 1 - Original 10-Second Spatial Contract Prompt

Source / film example -> This is an original prompt scaffold derived from Case 1 and Case 2, cross-checked against current official video prompting guidance from Runway Gen-4, Adobe Firefly, and Google DeepMind Veo. It is not an output validation.

Selected segment -> 8-12 second original suspense beat using an `assumed-continuity trap`: viewers infer a security team is approaching the same locked archive door that a thief is hearing, but the reveal shows the team at a decoy corridor while the thief is alone at the true vault.

Copyright / access boundary -> Original scenario. Do not mention or imitate The Silence of the Lambs, The Great Train Robbery, any living artist style, or copyrighted characters. Use only the mechanism.

Scene question -> Can the spatial-contract mechanism become a compact AI video prompt that names visible action, camera, sound, and reveal without overexplaining editing theory?

Dramatic change -> Institutional force appears to be converging on the thief, then the spatial contract flips: the team is in the wrong place and the thief realizes the vault is unguarded.

### Prompt Scaffold

```text
Duration: 10 seconds, suspenseful realistic heist beat, no dialogue.

Shot logic:
1. Start in a dim security control room: a gloved hand taps a floor-plan screen and a red corridor marker blinks.
2. Cut to armored guards moving fast down a sterile white corridor; boots and radio static imply urgency.
3. Cut to a lone thief at a heavy archive door hearing the same radio static and freezing, hand on the keypad.
4. A sharp access beep links the spaces; the viewer assumes the guards are outside this door.
5. Reveal: the guards stop at an identical decoy corridor door while the thief's door silently unlocks in a separate darker hallway.

Camera and sound:
Use tight but readable framing, clear left-right corridor direction, one short push-in on the thief's hand, one clean reveal of the wrong door number, radio static as the false sound bridge, then a brief silence after the vault unlocks.

Boundary:
Do not show violence, do not copy any known film scene, do not make the geography impossible; the misdirection comes from withheld matching corridors and the radio/static bridge.
```

### Prompt-Control Notes

- The prompt names four controllable layers: visible action, location contrast, sound bridge, and reveal cue.
- It keeps one false link: radio static/access beep seems to connect the guard corridor and thief door.
- It includes a non-cheating reveal: identical corridors are plausible, but door numbers and lighting reveal the mismatch.
- It avoids demanding many shot cuts from the video model by writing "shot logic" as a sequence of visible beats rather than a full edit decision list.

### Function Chain

```text
orient_space -> contrast_parallel -> sound_bridge
-> reveal_or_withhold -> status_shift -> punctuate_transition
```

### Candidate Capsule Decision

Record this as a neutral application event for the candidate capsule only. It proves the mechanism can become a compact prompt scaffold, but it does not prove generation success. Promotion requires inspected output or another applied analysis.

## Output Review Plan 1 - Spatial Contract Prompt

Source / film example -> Review plan derived from Prompt Application Test 1, AI Video Output Review workflow, and current official video prompting guidance from Runway Gen-4, Adobe Firefly, and Google DeepMind Veo. This is a pre-output validation rubric, not a rendered-output diagnosis.

Selected segment -> Same original 10-second heist/surveillance prompt scaffold from Prompt Application Test 1.

Copyright / access boundary -> Original prompt. Review should inspect only generated output and prompt adherence; do not compare against copyrighted film frames.

Scene question -> What must be visible in the generated clip before we can say the spatial-contract mechanism worked?

Dramatic change expected -> Viewer first infers the guards and thief are converging at one door, then understands they are in different corridors and the thief's door is the true vault.

### Required Evidence In Output

```text
E1_control_space: a security/control-room or floor-plan cue appears before corridor action
E2_parallel_action: guards moving urgently and thief at a locked door both appear
E3_false_link: radio/static/beep or matched corridor design plausibly connects the spaces
E4_reveal_cue: wrong door number, lighting difference, or corridor mismatch is visible
E5_status_shift: after reveal, the thief's situation changes from threatened to briefly advantaged or isolated
E6_no_cheat: geography is withheld, not contradicted; the reveal does not break a previously shown fact
```

### Acceptance Levels

```text
pass:
  E1-E5 are visible and E6 holds. The viewer can infer a false spatial connection and then understand the reveal.

partial:
  E2 and E4 are visible, but the false link is weak or the control-room cue is missing. The concept is salvageable with a narrower prompt.

fail_prompt_overload:
  locations or actions blur together, too many beats are skipped, or the model produces a generic heist montage without the reveal.

fail_spatial_cheat:
  the output contradicts itself: same door changes labels, guards teleport, corridor identity mutates without a reveal cue, or the thief/guards merge into one space unintentionally.

fail_wrong_mode:
  the clip becomes violence, chase, or character glamour instead of a suspenseful spatial misdirection.
```

### Frame Sampling Plan

Use a video review tool or manual frame sampling:

```text
00-20%: look for control-space setup or floor-plan cue
20-45%: look for guards moving and corridor direction
45-70%: look for thief at door and sound/action false link proxy
70-90%: look for reveal cue and wrong/true corridor separation
90-100%: look for changed end state
```

### Retry Rules

- If `E1_control_space` is missing, shorten the prompt and make the first frame a clear floor-plan/control-room image.
- If `E2_parallel_action` fails, split into image-to-video starting from a composite or use fewer characters/locations.
- If `E3_false_link` fails, make the false link visual as well as auditory: matching red corridor marker, same door silhouette, same access-beep light.
- If `E4_reveal_cue` fails, make the reveal concrete: visible wrong door number, different wall color, or clear decoy sign.
- If `fail_prompt_overload`, reduce to three beats: control screen -> guards at decoy door -> thief's real vault unlocks.
- If `fail_wrong_mode`, remove chase/violence language and emphasize "suspenseful procedural misdirection, no violence, no fight."

### Capsule Promotion Gate

Do not promote the candidate capsule from this plan alone. Promotion requires inspected output where:

- the spatial contract is visible;
- the reveal cue works without contradiction;
- at least one retry or independent prompt confirms the mechanism is reusable;
- failure boundaries are updated from actual output evidence.

### Candidate Capsule Decision

Record this as a neutral planning event only. It improves the review method but supplies no rendered evidence.

## Case 3 - 2001: A Space Odyssey (1968), Bone / Spacecraft Graphic Match

Source / film example -> Stanley Kubrick's "2001: A Space Odyssey," using BFI's film note, David Bordwell's graphic-match terminology note, Oklahoma State's editing chapter, Adobe's match-cut guide, and StudioBinder's match-on-action guide. This case does not reproduce frames, dialogue, or a full shot list.

Selected segment -> The famous transition from a thrown bone/tool to a spacecraft-like object in orbit. Exact timing varies by copy and is not needed for this mechanism note.

Copyright / access boundary -> The film is copyrighted. Use only compact critical description and source links; do not reproduce frames, dialogue, or a full transcript.

Scene question -> Can the new `bridge_logic_from_previous` field distinguish graphic match, match-on-action, ellipsis, and thematic comparison inside one highly compressed cut?

Dramatic change -> A prehistoric tool/action world is replaced by a space-age technology world; the cut compresses an enormous historical and technological leap into one visual bridge.

### Compact Transition Row

```text
transition_id: T-2001-01
outgoing element: thrown bone/tool moving against open sky
incoming element: spacecraft-like object in orbital space
bridge_logic_from_previous: graphic_match + ellipsis_bridge + thematic_comparison
matched element: pale elongated object shape and screen movement/placement, not the same object or continuous action
dominant_track: cut + image
viewer information shift: tool use / weaponized technology is connected across vast time and scale
transition_function: graphic_match + contrast_cut + punctuate_transition
prompt_control: "match the outgoing object's silhouette and motion direction to a future object with the same screen weight; make the cut skip time and scale while preserving a clear visual rhyme"
misuse_boundary: do not call this match-on-action; the action does not continue across the cut, and the objects/times/spaces are different
validation_status: source-backed applied validation, not capsule-promoted
```

### Function Chain

```text
graphic_match -> ellipsis_bridge -> thematic_comparison -> scale/time leap
```

### Portable Mechanisms

- `graphic time leap`: a matched shape or motion can let the viewer accept a huge jump in time, scale, or world if the visual rhyme is legible.
- `match type precision`: graphic match, match-on-action, eyeline match, and sound bridge should not be collapsed into the generic label "match cut."
- `visual rhyme plus conceptual jump`: the outgoing/incoming elements should share a concrete visible trait while changing context enough to create meaning.
- `bridge logic field works`: `bridge_logic_from_previous` can record multiple simultaneous functions: graphic similarity, ellipsis, contrast, and thematic comparison.

### Non-Portable Details

- Do not copy the specific bone/spacecraft image pair, Kubrick's film structure, or the film's cultural authority.
- A graphic match does not automatically become profound; the new context must carry a meaningful shift in time, scale, status, technology, emotion, or theme.
- A closer visual match is not always better; too-perfect similarity can feel like a gimmick if it lacks conceptual force.

### Candidate Capsule Decision

No capsule promotion. This validates the new transition-field vocabulary against a famous, source-backed example, but it is still one graphic-match case. Capsule candidacy would require at least one more independent applied example, preferably a sound match or action match with inspected output.

## Case 4 - Apocalypse Now (1979), Helicopter / Ceiling Fan Sound Bridge

Source / film example -> Francis Ford Coppola's "Apocalypse Now," using Walter Murch interview material, CineMontage's practitioner account, FilmSound's sound-analysis archive, and Ohio State's sound/editing chapter. This case does not reproduce frames, lyrics, dialogue, or a full shot list.

Selected segment -> The opening movement from jungle/helicopter imagery and sound toward Willard's Saigon hotel-room present, including the ceiling fan/helicopter relation. Exact timing varies by copy and is not needed for this mechanism note.

Copyright / access boundary -> The film and music are copyrighted. Use only compact critical description and source links; do not reproduce frames, song lyrics, dialogue, or a full transcript.

Scene question -> Can `bridge_logic_from_previous` distinguish a sound-driven transition from a visual graphic match, and can it record subjective memory rather than only smooth continuity?

Dramatic change -> War memory and hotel-room present contaminate each other before the viewer has stable geography. The transition makes hearing define the character's state before the room is fully sorted.

### Compact Transition Row

```text
transition_id: T-AN-01
outgoing element: jungle/helicopter memory texture and abstract rotary sound
incoming element: hotel-room ceiling fan, waking body, and later real helicopter context
bridge_logic_from_previous: audio_match + sound_bridge + subjective_memory_bridge
matched element: rotary rhythm, blade-like motion, and helicopter/fan sound association, not continuous location or literal object identity
dominant_track: sound + dissolve/image association
viewer information shift: the present room is heard through war memory before it is understood as ordinary space
transition_function: listening_point + sound_tail_contamination + reveal_or_withhold
prompt_control: "let a mechanical sound from one time/place morph into a similar room sound; delay the stable wide spatial answer until the sound has already shaped the viewer's perception"
misuse_boundary: do not use as a generic stylish transition; it needs a character memory, dream, intoxication, trauma, or subjective listening reason
validation_status: source-backed applied validation, not capsule-promoted
```

### Function Chain

```text
audio_match -> sound_bridge -> subjective_memory_bridge -> listening_point -> present-space reveal
```

### Portable Mechanisms

- `sound contamination`: a previous, remembered, or offscreen sound can invade the next image and change what the viewer thinks the space is.
- `rotary audio-image rhyme`: repeated blade motion and rotary sound texture can bind two different objects without claiming they are the same object.
- `listening point before geography`: when the scene is subjective, sound may establish whose perception we inhabit before the space is explained.
- `gradual source correction`: the soundtrack can move from abstract or remembered sound toward a plausible diegetic source, letting the viewer experience disorientation and reorientation.

### Non-Portable Details

- Do not copy the film's specific war imagery, music, hotel-room staging, or character condition.
- Do not label every audio carryover as trauma or memory. The sound bridge must have evidence of point of audition, memory, dream, intoxication, or other subjectivity.
- Do not hide confusing geography under "sound design." If the goal is orientation rather than subjective disorientation, provide a clearer spatial answer earlier.

### Candidate Capsule Decision

No capsule promotion. This is a second applied transition validation and the first sound-driven case, but capsule candidacy still needs another independent sound case or inspected AI-video output showing that the `subjective_memory_bridge` control works beyond this famous example.

## Case 5 - Seven Samurai (1954), Arrow / Delayed Result Action Cut

Source / film example -> Akira Kurosawa's "Seven Samurai," using David Bordwell's close analysis of selected cuts, continuity-editing education sources, and continuity-perception research. This case does not reproduce frames, dialogue, or a full shot list.

Selected segment -> During the climactic battle, Kambei fires arrows; the edit cuts away from the archer to a muddy town-square area where the result enters the frame after a brief delay. Exact timing varies by copy and is not needed for this mechanism note.

Copyright / access boundary -> The film is copyrighted. Use only compact critical description and source links; do not reproduce frames, dialogue, or a full transcript.

Scene question -> Is every action-continuity cut a match-on-action, or should `bridge_logic_from_previous` distinguish continuous movement from cause-to-result expectation?

Dramatic change -> The viewer moves from cause to expected result. The empty receiving frame briefly withholds confirmation, making the impact feel inevitable rather than merely continuous.

### Compact Transition Row

```text
transition_id: T-7S-01
outgoing element: archer releases a shot
incoming element: muddy receiving zone where the struck rider/body enters after a slight delay
bridge_logic_from_previous: causal_result + action_continuity + delayed_impact
matched element: action vector and expected target zone, not the same visible movement carried across the cut
dominant_track: cut + image + action expectation
viewer information shift: the cut converts a launched action into an anticipated result, then confirms it with delayed entry
transition_function: carry_action_continuity + punctuate_transition + impact_magnification
prompt_control: "cut from the initiating action to the expected impact zone; hold the receiving frame a fraction before the result enters, so the viewer anticipates the consequence"
misuse_boundary: do not label this as simple match-on-action unless the same movement continues across the cut; here the bridge is cause-to-result expectation
validation_status: source-backed applied validation, not capsule-promoted
```

### Function Chain

```text
action_cause -> expected_target_zone -> delayed_result -> impact_magnification
```

### Portable Mechanisms

- `cause-to-result cut`: an action can bridge a cut by pointing the viewer toward a consequence, even when the exact movement is not continuous across shots.
- `anticipatory receiving frame`: a brief empty or underfilled receiving frame can make the viewer wait for the result, increasing tension and inevitability.
- `action match boundary`: match-on-action requires the action itself to continue across the cut; causal result cuts preserve event logic rather than identical motion.
- `contact proof by consequence`: an impact can be proven through entry, collapse, skid, recoil, or environmental response instead of showing the hit itself.

### Non-Portable Details

- Do not copy the film's battle geography, arrow setup, rain/mud texture, or performer blocking.
- Do not use delayed result when the viewer has no reason to expect where the consequence will appear; the receiving zone must be legible.
- Do not use this to hide weak causality. If the viewer cannot connect cause and result, add a clearer vector, target cue, sound cue, or reaction.

### Candidate Capsule Decision

No capsule promotion. This adds an action-continuity boundary case after graphic-match and sound-bridge cases, but capsule candidacy still needs either a second action example or an inspected AI-video output using cause-to-result cutting.

## Case 6 - Police Story (1985), Mall Finale Contact Proof

Source / film example -> Jackie Chan's "Police Story," using David Bordwell's close analysis, Every Frame a Painting's action-comedy principles, No Film School's practical summary, Observer's restoration/context article, and Vulture's Gareth Evans interview as a safety/illusion comparison. This case does not reproduce frames, dialogue, or a full shot list.

Selected segment -> The shopping-mall finale, focusing on briefcase/window and glass-display impact beats discussed in source analysis. Exact timing varies by copy and is not needed for this mechanism note.

Copyright / access boundary -> The film is copyrighted. Use compact critical description only; do not reproduce frames, dialogue, or full beat-by-beat transcription.

Scene question -> Can the `Contact Proof Ladder` explain why a hit feels credible without reducing the effect to "real danger" or generic "impact"?

Dramatic change -> The action becomes believable because force visibly travels through bodies, glass, props, rhythm, and pain. The viewer reads not just a strike, but a changed physical situation.

### Contact Proof Score Rows

```text
beat_id: T-PS-01
beat focus: briefcase blow drives Jackie into a windowpane
initiating action: attacker swings briefcase toward Jackie
target / receiving zone: Jackie and the nearby glass pane
contact or near-miss relation: 2 - the swing continues into the collision relation
receiver response: 2 - Jackie rebounds and visibly suffers the blow
environment / prop / costume / sound proof: 2 - glass breaks and sharp material detail proves force direction
pain or recovery beat: 2 - the body and face register pain after the impact
changed end state: 2 - Jackie is physically checked and the fight pressure increases
total visible proof score: 10 / 10 for the rungs scored here
prompt_control: "keep attacker, receiver, and breakable surface in a readable relation; after impact, show rebound, pain, and broken material before the next beat"
misuse_boundary: do not imitate the dangerous stunt or glass setup; for AI/fictional prompts use visual causality, not real execution instructions
```

```text
beat_id: T-PS-02
beat focus: bodies are driven into display cases during the mall fight
initiating action: shove, swing, or chase momentum drives a body toward a display surface
target / receiving zone: glass case / display area / body path
contact or near-miss relation: 1-2 - source analysis stresses clear diagrammatic staging, but exact strength depends on the individual beat
receiver response: 2 - the body trajectory and awkward fall sell the result
environment / prop / costume / sound proof: 2 - vitrines, glass, and display structures supply material proof
pain or recovery beat: 1-2 - pain is often carried by brief pauses, awkwardness, or continued vulnerability
changed end state: 2 - distance, balance, threat count, or immediate objective changes
total visible proof score: 8-10 / 10 for the rungs scored here
prompt_control: "make the body path and target surface legible before impact; let broken props or displaced furniture mark the result; hold a fraction for recovery or renewed threat"
misuse_boundary: environmental destruction is not proof by itself; without body trajectory and receiver response it becomes spectacle debris
```

### Function Chain

```text
clear setup -> readable force path -> contact / material break -> receiver pain -> changed tactical state
```

### Portable Mechanisms

- `proof chain over single hit`: impact credibility comes from linked evidence, not one blurred contact frame.
- `same-frame credibility`: when the viewer can see attacker, receiver, and receiving surface together, less explanatory cutting is needed.
- `material witness`: glass, furniture, dust, cloth, water, sound, or prop displacement can testify to force if the body path is legible first.
- `pain as state update`: pain is not decoration; it tells the viewer the body paid a cost and cannot reset cleanly.

### Non-Portable Details

- Do not copy Police Story's dangerous stunt conditions, glass density, mall geography, or comic-danger tone.
- Do not treat real injury risk as the source of value. The reusable mechanism is readable visual causality plus body cost.
- Do not add breakaway props, debris, or sparks before the attack vector and receiving body are clear.

### Candidate Capsule Decision

No capsule promotion. The ladder now has one applied scene validation, but durable capsule promotion should wait for either a second distinct action example or an inspected AI-video output scored with the same ladder.

## Case 7 - Locke (2013), Car Dialogue As Gaze Contract

Source / film example -> Steven Knight's "Locke," using A24's official film page, Steven Knight interviews, Definition Magazine's cinematography article, and existing car-dialogue production references. This case does not reproduce dialogue, frames, or a full beat transcript.

Selected segment -> The recurring night-drive phone-call structure: Ivan Locke drives alone while external voices enter through the car phone, with the future framed through the road/windscreen and past/family/work pressures arriving as sound.

Copyright / access boundary -> The film is copyrighted. Use compact critical description only; do not reproduce dialogue, full call order, or frame images.

Scene question -> Can the `Constrained Dialogue Review Card` handle a car dialogue scene with no visible conversation partner and almost no physical blocking change?

Dramatic change -> The car turns choice into confinement: Locke can keep driving, answer or end calls, look ahead or into reflections, but he cannot face the people whose lives he is changing. The dialogue pressure comes from voice, gaze direction, and the impossibility of leaving the vehicle without abandoning the decision.

### Constrained Dialogue Review Row

```text
case_id: T-LOCKE-01
space type: moving car / night road / single visible character
dramatic pressure: professional duty, family collapse, moral responsibility, and offscreen childbirth compete during one drive
who wants what: Locke wants to complete a morally necessary journey while controlling damage through phone calls
who resists: wife, employer, colleague, children, hospital situation, and Locke's imagined father all pressure different obligations
escape / access condition: he can drive forward or stop/turn back, but the car makes every choice linear and time-bound
dominant gaze rule: shared_forward_gaze without a visible partner; he looks at road, dashboard, mirror, phone interface, or reflected lights instead of direct faces
reaction ownership: listener owns meaning; Locke's face and pauses reinterpret offscreen voices
blocking change: minimal body blocking; status changes are carried by grip, breath, gaze shift, call acceptance/refusal, and emotional leakage
silence function: absorbing consequences, choosing composure, deciding how truthful the next call can be
information release: each call adds one pressure line while withholding another; the car keeps all spaces offscreen but active through sound
coverage decision: vary angle, reflection, profile, road-light texture, and call rhythm instead of changing location
prompt control: "one driver alone at night, no visible conversation partner; voices arrive through hands-free phone; keep gaze mostly forward; let mirror/reflection and tiny pauses reveal pressure"
boundary: do not make every car scene a solo phone-call thriller; this works because the drive itself is an irreversible moral action
validation_status: source-backed applied validation, not capsule-promoted
```

### Function Chain

```text
shared_forward_gaze -> offscreen voice pressure -> listener-owned reaction
-> silence / composure struggle -> irreversible forward motion
```

### Portable Mechanisms

- `gaze contract without partner`: car dialogue can work without face-to-face eyelines if the road, mirror, and offscreen voice define where attention is allowed to go.
- `phone as spatial multiplication`: each call can bring a new offscreen location into the car, turning one visible space into several active dramatic spaces.
- `forward motion as moral lock`: a moving vehicle can make a decision feel irreversible when the route itself is the character's commitment.
- `listener-owned scene`: when other characters are voices, the visible actor's listening, delay, breath, and restraint carry the emotional interpretation.
- `outside chaos / inside control`: moving road lights, reflections, and traffic texture can externalize pressure while the character tries to maintain order.

### Non-Portable Details

- Do not copy Locke's exact premise, call sequence, construction/job stakes, family situation, or one-actor structure.
- Do not assume a car automatically creates tension. The vehicle must alter gaze, escape, time pressure, sound perspective, or moral direction.
- Do not use phone voices as exposition dumps. Each call needs a want/resistance function and a visible listener consequence.

### Candidate Capsule Decision

No capsule promotion. This validates the constrained-dialogue review card against one strong car-dialogue example, but capsule candidacy needs either another car/vehicle scene or an AI-generated dialogue output reviewed with the same card.

## Case 8 - A Quiet Place (2018), Sound Threshold As Survival Geography

Source / film example -> John Krasinski's "A Quiet Place," using Paramount's official page and sound-practitioner interviews with Erik Aadahl and Ethan Van der Ryn. This case does not reproduce dialogue, full scene order, or creature design details beyond critical description.

Selected segment -> The film's recurring family survival routine: movement, communication, eating, paths, objects, alarms, and creature threat are organized around whether a sound crosses a dangerous threshold.

Copyright / access boundary -> The film is copyrighted. Use mechanism-level description only; do not reproduce scripts, full beat lists, or frame images.

Scene question -> Can the `Offscreen Sonic Space Review Card` transfer from a morally contradictory offscreen space to a genre scene where the offscreen threat is a creature and the main rule is survival by quietness?

Dramatic change -> The offscreen threat does not need to be visible in every beat because the sound rule has already changed the world. A tiny object sound, footstep, breath, or alarm can update geography, danger, and character priority.

### Offscreen Sonic Space Review Row

```text
case_id: S-AQP-01
visible space: family domestic / farm / path / interior survival zones
offscreen space: surrounding exterior and unseen creature approach paths
listener position: alternates between objective family listening and Regan's altered hearing perspective
source status: diegetic sound rule, with subjective hearing shifts
distance and obstruction: threat is inferred by approach sound, nearby surfaces, alarm sources, and environmental masking such as louder natural sound
direction and movement: small Foley or creature sound can imply direction before the source is shown
recurrence pattern: quiet routine -> small sound risk -> listening pause -> threat response or tactical adaptation
foreground visible-world sounds: sand path steps, cloth, breath, object handling, sign language, controlled room tone
offscreen pressure sounds: distant creature movement/clicks, environmental masking, sudden object or alarm sound that changes danger
reaction policy: characters actively listen, freeze, sign, redirect attention, or exploit louder sound cover
image-sound relation: reinforce survival rule; reveal danger through tiny sound; mask danger when a louder source creates temporary safety
mix hierarchy: sparse foreground Foley and breath before louder creature or environmental events; subjective POV may drop exterior sound
ethical or genre boundary: do not use deaf perspective as novelty; tie subjective silence to character POV and story function
prompt control: "survival horror scene where every audible object matters; establish a clear sound threshold, keep Foley sparse, let one accidental sound trigger an unseen approach, shift briefly into a deaf character's muffled/near-silent listening POV"
validation_status: source-backed applied validation, not capsule-promoted
```

### Function Chain

```text
sound threshold rule -> audience listening contract -> tiny Foley cue
-> offscreen threat inference -> reaction / adaptation -> changed geography
```

### Portable Mechanisms

- `threshold before tension`: define which sounds cause consequences before asking the audience to fear tiny noises.
- `tiny Foley as plot event`: when the rule is established, a cloth scrape, object tick, breath, or footstep can carry the same story weight as a cut or reveal.
- `subjective silence as POV`: quietness can mean "we are hearing with this character," not "nothing is happening."
- `masking as temporary safety`: a louder environmental sound can create a pocket where characters act differently, making sound geography dynamic.
- `listening pause`: after a sound, hold the characters listening before the source reveal so the audience participates in threat-location work.

### Non-Portable Details

- Do not copy the exact creature premise, family setup, farm geography, hearing-aid device logic, or specific scare beats.
- Do not make every suspense scene quiet. Quietness must be governed by a threshold, a listener position, and a consequence.
- Do not overfill the mix with scary drones if the dramatic engine depends on the audience hearing small diegetic sounds.

### Candidate Capsule Decision

No capsule promotion yet. This is the second strong offscreen/sound-rule case after "The Zone of Interest," but the ethical and genre conditions are different enough that capsule promotion should wait for either an AI-output review or a third non-creature offscreen-space case.

## Case 9 - The Conversation (1974), Playback As Investigative Space

Source / film example -> Francis Ford Coppola's "The Conversation," using Rialto film context, Library of Congress / National Film Registry context, Walter Murch interview material, and source compilations around the film's production and sound. This case does not reproduce the script or full surveillance scene.

Selected segment -> The recurring surveillance recording workflow: Harry Caul records a public conversation, then replays and processes fragments until the same sound material appears to change its threat, grammar, and moral consequence.

Copyright / access boundary -> The film is copyrighted. Use mechanism-level description only; do not quote the famous recorded line or reconstruct the whole scene beat-by-beat.

Scene question -> Can offscreen sonic space work in a realistic crime/thriller scene where the key space is not outside a wall or behind a door, but inside a recording that can be replayed and reinterpreted?

Dramatic change -> The recording becomes a room the character keeps re-entering. Each pass changes what seems foregrounded: crowd noise, missing words, speaker relation, fear, guilt, or imagined consequence.

### Offscreen Sonic Space Review Row

```text
case_id: S-CONV-01
visible space: surveillance workspace / tape machines / listener's private room
offscreen space: past public conversation reconstructed through recorded fragments
listener position: surveillance analyst whose guilt and paranoia alter interpretation
source status: diegetic recorded sound, replayed and processed; subjective inference grows around it
distance and obstruction: crowd noise, public distance, microphone limits, and tape distortion block certainty
direction and movement: source movement belongs to the recorded event, while present-space movement belongs to tape handling and listening reaction
recurrence pattern: record fragment -> replay -> filter or isolate -> new emphasis -> listener reaction -> imagined consequence
foreground visible-world sounds: reel/tape handling, room tone, equipment whir, breath, small manual adjustments
offscreen pressure sounds: repeated conversation fragment, crowd bed, masked or clarified words, remembered or imagined sonic residue
reaction policy: listener actively reacts, doubts, rewinds, repairs, overinterprets, and lets the recording contaminate present action
image-sound relation: recorded sound contradicts or revises the visible present; repeated audio changes what the audience thinks it knows
mix hierarchy: first preserve noisy uncertainty, then selectively foreground one sonic detail without making the whole scene perfectly clear
ethical or genre boundary: do not treat surveillance as neutral truth; foreground partial evidence and listener bias
prompt control: "crime-thriller evidence review: a lone analyst replays a noisy public recording; each replay isolates a different word or frequency band; cut between tape controls, listening face, and brief imagined fragments; the same sound changes meaning through emphasis rather than exposition"
validation_status: source-backed applied validation, not capsule-promoted
```

### Function Chain

```text
captured offscreen event -> noisy playback -> selective filtering
-> emphasis shift -> listener bias -> revised causal model
```

### Portable Mechanisms

- `playback as room`: a recording can function as a revisitable dramatic space, not just a clue.
- `same sound / new meaning`: repeating one fragment can advance story if each pass changes clarity, emphasis, context, or listener state.
- `machine foreground`: tape handling, knobs, reels, meters, headphones, cursor movement, or waveform work can make thinking visible.
- `partial evidence pressure`: the scene gains tension from what cannot be verified, not from delivering perfect information.
- `listener contamination`: the character's fear, guilt, expertise, or bias changes how the audience hears the same cue.

### Non-Portable Details

- Do not copy the exact surveillance premise, famous line, Union Square setup, saxophone solitude, or conspiracy structure.
- Do not make every recording scene ambiguous. Ambiguity works only when the replay changes a named variable and consequences accumulate.
- Do not overclean the audio too early; if the recording becomes perfectly legible, the investigative pressure may collapse.

### Candidate Capsule Decision

No capsule promotion yet. The offscreen-sound route now has three strong cases, but promotion should wait for one AI-output review or one explicit user use case so the mechanism proves useful outside archival film analysis.

## Case 10 - A Trip To The Moon (1902), Destination Target As Arrival Punchline

Source / film example -> Georges Melies' "Le voyage dans la lune / A Trip to the Moon," using MoMA's collection note, ACMI's collection note, Wikimedia Commons access/licensing notes, Google DeepMind Veo prompt guidance, VBench, AIGVE survey, and the Round 44 Breakdown-To-Prompt Contract Card.

Selected segment -> The arrival-on-the-moon beat, especially the famous graphic target/punchline in which the journey's destination becomes a visible receiving mark. Exact timing varies by copy; this note uses function rows rather than frame-accurate timecodes.

Copyright / access boundary -> Wikimedia Commons marks at least one available copy as public domain in the United States and relevant life-plus-80 jurisdictions, but publication use still requires checking the intended copy, territory, and restoration status. For prompt work, do not reproduce the Moon face, eye impact, astronomer costumes, cannon capsule, painted-set staging, or exact gag.

Scene question -> Can the Round 44 breakdown-to-prompt template extract a portable mechanism from an iconic public-domain image without turning the prompt into a copy of the source scene?

Dramatic change -> The travel goal changes from abstract destination to visible impact/result: the viewer understands arrival because the target surface is pre-readable, then visibly altered by the arriving object.

### Compact Breakdown-To-Prompt Rows

```text
row_id: ATM-01
source beat: moon destination presented as a graphic receiving surface
objective evidence: frontal tableau, clearly readable target/destination, theatrical scale relation between large surface and small vehicle
dominant_track: image + prop_material
viewer information shift: the destination is no longer offscreen or abstract; it becomes a specific receiving zone
shot_function: orient_space + route_attention
neighbor_relation: prepares the audience to read arrival as a visible result rather than a hidden transition
portable prompt control: "before the arrival, show the destination as a clear circular receiving mark or portal-like surface; make scale relation legible"
do-not-copy boundary: do not use the Moon face, eye, cannon capsule, painted 1902 tableau, astronomer costumes, or the original gag
validation_status: source-backed applied transfer; no generated output inspected
```

```text
row_id: ATM-02
source beat: vehicle/object reaches the marked destination
objective evidence: arrival is expressed through a direct graphic relation between moving object and prepared target zone
dominant_track: image + rhythm
viewer information shift: motion converts route into consequence; the target changes state
shot_function: prove_contact_or_causality + punctuate_transition
neighbor_relation: the arrival beat pays off the previously prepared destination surface
portable prompt control: "let the arriving object enter the prepared target zone and visibly change it; hold one beat after contact so the new state registers"
do-not-copy boundary: do not literalize the original impact or facial injury image; use a new fictional object, surface, and consequence
validation_status: source-backed applied transfer; not output-validated
```

```text
row_id: ATM-03
source beat: theatrical stillness makes the gag readable
objective evidence: stable frontal view, clear silhouette, minimal camera ambiguity, action staged for immediate recognition
dominant_track: blocking + composition
viewer information shift: the viewer reads the impossible arrival as a clean visual sentence
shot_function: route_attention + modulate_rhythm
neighbor_relation: stillness prevents the graphic target and impact result from being lost
portable prompt control: "use a locked or nearly locked camera; keep the target and arriving object visible in one readable relation; avoid random camera drift"
do-not-copy boundary: do not treat early-cinema tableau distance as a default modern style; use it only when graphic clarity matters more than immersion
validation_status: source-backed applied transfer; not capsule-promoted
```

### Function Chain

```text
prepare_destination_target -> route_attention -> arrival_object_enters_mark
-> target_state_changes -> reaction_hold / punchline_registers
```

### Original AI Video Prompt Transfer

```text
Reference use:
Extract only the mechanism: a destination is prepared as a clear receiving mark, then an arriving object changes that mark. Do not copy the Moon face, eye impact, cannon capsule, astronomers, painted tableau, or the original gag.

Platform bounds:
8-second text-to-video, single continuous shot or one clean cut, 16:9, native audio if supported.

Original premise:
Inside a quiet museum conservation room, a tiny brass repair drone is sent toward a giant antique clock face whose missing center gear is marked by a pale circular target.

Camera / composition:
Locked-off medium-wide frontal shot; the clock face fills the back wall while the small drone hovers in the foreground. Keep the circular target visible for the full clip.

Beat timeline:
0-2s: conservator's gloved hand releases the tiny brass drone; the clock face and empty center target are already visible.
2-5s: drone glides steadily toward the marked center, small against the large dial; no fast cutting.
5-6s: drone clicks into the circular gear socket; dust lifts and the clock hands twitch.
6-8s: hold on the changed state as the clock begins one slow tick and the conservator stops moving.

Sound, if supported:
soft room tone, small brass motor whirr, single clean gear click at contact, one low clock tick after the state change.

Negative / positive lock:
Preserve the clock target and drone in one readable relation; no Moon face, no eye, no rocket, no astronomers, no slapstick injury, no random camera drift, no extra chase.

Review:
Check prepared target -> readable approach -> contact/state change -> reaction hold -> no copied source imagery.
```

### Portable Mechanisms

- `prepared receiving mark`: show the target or missing slot before the arrival so viewers know what consequence to watch for.
- `arrival as state change`: the arriving object must alter the target surface, mechanism, light, posture, sound, or rhythm.
- `graphic clarity over style imitation`: a stable camera can be useful when the scene needs one clean visual sentence.
- `reference extraction boundary`: iconic images need extra negative locks because the model may over-associate the reference with its famous surface details.

### Non-Portable Details

- Do not copy the Moon face, eye impact, cannon capsule, astronomer costumes, stage flats, exact gag, or early-cinema acting scale.
- Do not use "Melies style" as a shortcut unless the project explicitly wants early-cinema fantasy; the reusable mechanism is target preparation plus arrival payoff.
- Do not overpack this into a multi-location journey. The prompt works because one target, one arrival path, and one changed state are inspectable.

### Candidate Capsule Decision

No capsule promotion. This is a useful applied test of the Round 44 template and a prompt scaffold, but there is no generated output review yet and the mechanism is drawn from a highly iconic source image.

## Output Review Plan 2 - Prepared Target / Clock Drone Prompt

Source / film example -> Review plan derived from Case 10, Round 44 Breakdown-To-Prompt Contract Card, the State-Change Output Review Card, Google DeepMind Veo prompt guidance, Google AI for Developers Veo video-generation docs, VBench, AIGVE survey, and AVGen-Bench.

Selected prompt -> The original 8-second museum conservation room prompt in Case 10: a tiny brass repair drone approaches a giant antique clock face and clicks into a missing center gear socket.

Copyright / access boundary -> Review only the generated original clip and prompt adherence. Do not compare the result against "A Trip to the Moon" frames or reward copied Moon/rocket imagery.

Scene question -> What must be visible before we can say the prepared-target / arrival-state-change mechanism worked in an AI video output?

Dramatic change expected -> The clock changes from incomplete/still to repaired/activated because the drone enters the prepared gear socket.

### Required Evidence In Output

```text
E1_initial_state_visible: the antique clock face and empty center gear/socket are visible before the drone arrives
E2_target_relation_stable: the socket stays in the same readable place; it does not drift, vanish, or become a different object
E3_action_path_readable: the small brass drone starts away from the target and moves toward it along a clear path
E4_contact_or_activation: the drone visibly enters, docks with, or activates the socket
E5_changed_state_visible: after contact, clock hands twitch, one tick occurs, light/dust/gear motion changes, or another clear state update appears
E6_reaction_hold: the clip holds briefly after the change so the viewer can register the repaired state
E7_no_continuity_cheat: the changed state follows from the action rather than appearing before contact or via object mutation
E8_no_source_copy: no Moon face, eye, rocket, astronomer costume, painted 1902 tableau, or slapstick injury appears
```

### Acceptance Levels

```text
pass:
  E1-E6 are visible, E7 holds, and E8 holds. The viewer understands before-state -> approach -> contact -> changed state.

partial:
  E1, E3, and E5 are visible, but the socket relation or contact moment is weak. Salvage with a narrower target lock or image-to-video start frame.

fail_target_drift:
  the clock/socket changes identity, moves unpredictably, or disappears before contact.

fail_no_state_change:
  the drone moves, but the clock does not visibly change after contact.

fail_early_change:
  the clock starts ticking or changes before the drone reaches the socket.

fail_reference_leak:
  the output imports Moon/rocket/eye/astronomer imagery or early-cinema staging despite the originality boundary.

fail_prompt_overload:
  the output becomes a museum montage, chase, or generalized steampunk scene without the target-action-change chain.
```

### Frame Sampling Plan

```text
00-20%: check initial clock/socket visibility and target relation
20-55%: check drone identity, path, scale, and approach direction
55-75%: check contact, docking, click, or activation moment
75-95%: check changed clock state and reaction hold
95-100%: check no source-copy leak or late continuity mutation
```

### Retry Rules

- If `E1_initial_state_visible` fails, make the first frame "locked frontal shot of the antique clock face with the empty center socket visible."
- If `E2_target_relation_stable` fails, use image-to-video or add "the clock face remains fixed in frame; socket stays centered."
- If `E3_action_path_readable` fails, simplify to "drone starts lower-left foreground and glides straight to the center socket."
- If `E4_contact_or_activation` fails, add a single trigger: "at 5s the drone clicks into the socket."
- If `E5_changed_state_visible` fails, name one visible change only: "clock hands twitch once and dust lifts."
- If `E6_reaction_hold` fails, add "hold the final repaired clock state for the last two seconds."
- If `E8_no_source_copy` fails, remove all film-title references and keep only mechanism language: "prepared receiving mark, docking, state change."
- If `fail_prompt_overload`, reduce to three beats: empty socket -> drone docks -> clock ticks once.

### Prompt Delta Template

```text
Keep:
  museum conservation room, antique clock face, tiny brass repair drone, locked frontal shot.

Fix one failed field:
  [target visibility / path / contact / state change / hold / source-copy leak]

Add positive control:
  [one concrete visible state change]

Negative / boundary:
  no Moon face, no eye, no rocket, no astronomers, no early-cinema tableau, no extra chase, no random camera drift.

Expected proof:
  before-state -> approach -> contact -> changed clock state -> hold.
```

### Capsule Promotion Gate

Do not promote this plan by itself. Promotion would require at least one inspected generated clip that passes or a failed clip whose retry delta improves the same mechanism without rewriting the whole prompt.

### Candidate Capsule Decision

Record as output-review planning only. It is directly usable for future generation review, but it contains no rendered-output evidence.

## Applied Breakdown Mini-Template

```text
Source / film example ->
Selected segment ->
Copyright / access boundary ->
Scene question ->
Dramatic change ->
Compact shot rows ->
Function chain ->
Portable mechanisms ->
Non-portable details ->
Candidate capsule decision ->
```
