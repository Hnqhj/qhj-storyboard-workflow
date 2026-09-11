# Shot Breakdown Method

Last researched: 2026-06-28
Route: shot-by-shot breakdown method + shot function classification + practical validation
Status: foundation reference, research-synthesized, not capsule-promoted

## Research Questions

1. What is the smallest shot-by-shot record that still supports real analysis?
2. How should shot function differ from technical labels such as shot size, angle, or camera movement?
3. How can a breakdown become executable camera/editing/staging controls for AI video prompts?
4. Can the table support real teaching examples and close-analysis sources without becoming bloated?
5. What evidence is needed before a mechanism can move from reference note to capsule?

## Minimal Shot Breakdown Workflow

1. Watch once without pausing and write the scene-level dramatic change.
2. Write the `scene_question`: what dramatic, informational, spatial, emotional, or rhythmic problem does this scene solve?
3. Watch shot by shot and log objective evidence before interpretation.
4. Divide each shot into technical description, viewer-information change, dominant track, and function tag.
5. Compare neighboring shots: ask what the cut, movement, match, sound change, or hold does that a single still frame cannot.
   - Name the bridge logic: action continuity, eyeline answer, graphic match, sound bridge, causal result, ellipsis, contrast, or rupture.
6. Summarize the sequence as a function chain, then translate only the useful chain into prompt controls.
7. Mark which details are portable mechanisms and which are tied to this film's story, performer, period, or production context.

## Minimum Table Fields

Use these columns for a durable shot-by-shot breakdown table:

```text
shot_id
timecode_in
timecode_out
duration_seconds
transition_or_match_from_previous
bridge_logic_from_previous
shot_scale
camera_height_angle_level
camera_movement_or_reframing
lens_focus_depth_if_visible
blocking_space_relation
onscreen_action
sound_change_or_sound_perspective
dominant_track
new_information_or_attention_shift
shot_function
neighbor_relation
evidence_note
prompt_control
misuse_boundary
validation_status
```

Keep `shot_function` separate from `shot_scale`: a close-up can reveal a clue, isolate emotion, create a false POV, punctuate rhythm, or hide geography. The function is not contained in the size label.

## Shot Function Taxonomy

- `orient_space`: establishes or reestablishes spatial relations among figures, objects, and setting.
- `route_attention`: uses framing, movement, focus, sound, gesture, or contrast to direct attention to a specific element.
- `reveal_or_withhold`: reveals, delays, hides, or retrospectively clarifies information.
- `connect_look_object`: binds a looker to what is looked at through eyeline, POV, reaction, or false-POV construction.
- `carry_action_continuity`: makes physical movement readable across cuts through match-on-action, screen direction, or repeated motion.
- `build_space_constructively`: lets the viewer assemble space mentally without a full establishing view.
- `isolate_subjectivity`: narrows the viewer into a character's perception, emotion, uncertainty, or bodily state.
- `contrast_parallel`: compares people, spaces, times, or forces through parallel cutting, graphic match, scale contrast, or sound contrast.
- `modulate_rhythm`: changes pace through shot duration, movement speed, sound density, silence, or repeated setup.
- `punctuate_transition`: marks a scene turn, ellipsis, beat ending, entrance, exit, or tonal break.
- `motif_texture`: makes a recurring object, color, sound, architectural feature, or material carry meaning.
- `prove_contact_or_causality`: shows that one action physically causes another; especially important in action scenes.

## Dominant Track Tags

Use one or two per row when useful:

- `image`: framing, angle, scale, movement, lens, focus, visual reveal.
- `cut`: transition, match, duration, order, ellipsis, simultaneity.
- `sound`: sound source, perspective, bridge, silence, music, Foley, impact.
- `performance`: look, pause, gesture, posture, breath, reaction, line delivery.
- `blocking`: spatial relation, entrance/exit, grouping, isolation, axis, proximity.
- `light_color`: motivated source, contrast, color pool, silhouette, material response.
- `prop_material`: object use, texture, surface, clue, motif, tactile action.
- `rhythm`: beat duration, repetition, acceleration, pause, punctuation.

## Knowledge Entries

### Yale Film Analysis Guide -> Technical Vocabulary Scaffold

Source / film example -> Yale Film Analysis Guide, especially Basic Terms, Cinematography, Editing, and Analysis.

Observation -> The guide separates shot, scene, sequence, mise-en-scene, cinematography, editing, sound, and analysis examples.

Mechanism -> Good shot-by-shot breakdown starts by naming units and devices consistently before making interpretive claims.

Executable control -> In analysis, first log unit boundaries and device labels; in prompts, specify "one continuous shot", "cut-in", "eyeline match", "reestablishing shot", "sound bridge", or "tracking shot" only when that device has a narrative job.

Applicable scenes -> Any scene breakdown, especially when multiple techniques overlap.

Misuse boundary -> Do not stop at terminology lists. A correct label without function is only inventory, not analysis.

Validation status -> Source-backed foundation; needs repeated scene applications before capsule promotion.

### UNCW Shot Breakdown -> Objective Field Discipline

Source / film example -> Todd Berliner, FST 200 shot breakdown handout, using The Apartment and His Girl Friday as classroom examples.

Observation -> The handout asks students to record distance of framing, height, angle, movement/zoom, transition, and match, and to note variations inside moving shots.

Mechanism -> A minimum shot log must preserve changes inside a shot, not just one static label per shot.

Executable control -> When breaking down a moving shot, record start-state -> movement -> end-state, e.g. "LS becomes MLS as characters approach; pan right follows group; reframing keeps them centered."

Applicable scenes -> Moving masters, ensemble blocking, long takes, comedy staging, action beats with reframes.

Misuse boundary -> This is a technical inventory layer; add function separately or the table will not explain why the shot works.

Validation status -> Source-backed method; operationally useful, not a capsule yet.

### UNC Writing Center -> From Description To Argument

Source / film example -> UNC Writing Center film analysis guide.

Observation -> The guide warns against merely describing elements; the analyst must explain significance and avoid confusing shot, scene, and sequence.

Mechanism -> Every observation should answer "so what changed for the viewer or argument?"

Executable control -> Add `new_information_or_attention_shift` and `shot_function` columns to every shot-by-shot table.

Applicable scenes -> Written analysis, scene diagnosis, prompt extraction, teaching notes.

Misuse boundary -> Do not force symbolism into every prop or color; tie significance to the scene's actual dramatic or informational work.

Validation status -> Source-backed analysis guardrail; not capsule-promoted.

### Bordwell On Analytical / Constructive Cutting -> Space Assembly

Source / film example -> David Bordwell, Lau Kar-leung analysis in Observations on Film Art.

Observation -> Analytical cutting can establish layout and move into partial views; constructive cutting can omit a complete establishing view and make viewers assemble space from cues.

Mechanism -> Shot function can be spatial cognition, not just emotional emphasis.

Executable control -> For readable action or complex blocking, decide whether to use `orient_space` first, or `build_space_constructively` through eyelines, body position, prop cues, and matched movement.

Applicable scenes -> Action geography, chase scenes, multi-character blocking, suspense reveals, spatial puzzles.

Misuse boundary -> Constructive cutting requires strong cues. Without screen direction, eyelines, prop anchors, or motion matches, the viewer loses geography.

Validation status -> Strong scholarly/practitioner analysis source; candidate mechanism for future action-scene validation.

### Yale Analysis Examples -> Multi-Track Shot Rows

Source / film example -> Yale analyses of Rocco and His Brothers and Il grido, referenced in Duke and McGill teaching materials.

Observation -> Each shot row combines editing, cinematography, sound, mise-en-scene, and interpretive analysis.

Mechanism -> A useful shot-by-shot row is multi-track: image, cut, sound, space, and interpretation must be visible together.

Executable control -> For each shot, write one compact sentence for technical evidence and one compact sentence for function. Example pattern: "ELS/high angle/silence isolates figure in industrial space -> makes social force dwarf the character."

Applicable scenes -> Any sequence where sound/image relation and space carry meaning.

Misuse boundary -> Multi-track rows can become bloated. Keep each cell evidence-based and avoid unsupported psychology.

Validation status -> Source-backed example; not capsule-promoted.

### StudioBinder Shot List -> Production-Side Translation

Source / film example -> StudioBinder shot list template and shot list anatomy.

Observation -> Production shot lists commonly include scene number, shot number, description, shot size/type, camera movement, lens, gear, and scheduling details.

Mechanism -> Analysis fields and production fields overlap, but analysis must add function, viewer information, and misuse boundary.

Executable control -> When translating analysis into AI video prompts, keep production-like fields: shot size, angle, movement, lens/focus, duration, subject action, sound cue; then add purpose: "to reveal X", "to withhold Y", "to reorient geography."

Applicable scenes -> Prompt writing, shot plans, storyboards, director notes.

Misuse boundary -> A shot list is not a scene analysis by itself; "close-up, dolly in" is incomplete without the beat it controls.

Validation status -> Practical production source; not capsule-promoted.

### Ohio State Sound And Editing -> Sound Belongs In The Shot Table

Source / film example -> Ohio State Pressbooks chapter on Sound and Editing.

Observation -> The chapter shows how music, sound, and transitions can connect separate images into a continuous spatial or emotional sequence.

Mechanism -> A visual cut can be understood through sound. A shot row without sound perspective or sound transition may miss the actual continuity mechanism.

Executable control -> Always log whether sound leads, follows, bridges, contradicts, or punctuates the cut. Add `sound_change_or_sound_perspective` even for "quiet" shots, noting room tone, silence, or ambience changes.

Applicable scenes -> Montage, transitions, action, suspense, offscreen threat, subjective listening, memory.

Misuse boundary -> Do not treat sound as background decoration. Also do not over-explain every ambience layer unless it changes attention or meaning.

Validation status -> Source-backed validation of table field; not capsule-promoted.

## Practical Breakdown Checklist

Before starting:

```text
film / sequence:
scene_question:
dramatic change:
analysis focus:
source quality:
copyright boundary:
```

For each shot row:

```text
objective evidence:
dominant_track:
viewer information shift:
function tag:
neighbor relation:
prompt control:
boundary:
```

After the table:

```text
sequence_function_chain:
portable mechanisms:
non-portable details:
candidate capsule? yes/no + why:
next validation context:
```

## Prompt Translation Template

```text
Scene beat:
Viewer should know / not know:
Spatial relation to establish:
Shot function:
Dominant track:
Technical controls:
  - shot scale:
  - angle / height:
  - movement / reframing:
  - lens / focus:
  - blocking:
  - transition / match:
  - bridge logic:
  - sound:
Portable mechanism:
Boundary:
```

## Quick Function Chain Example

```text
orient_space -> route_attention -> reveal_or_withhold -> connect_look_object
-> isolate_subjectivity -> reestablish_space -> punctuate_transition
```

Use this as a design chain, not a mandatory formula.

## Upgrade Gate

A breakdown lesson can become a capsule candidate only when:

- the source clip or analysis evidence is inspectable;
- the mechanism changes a future analysis or prompt decision;
- the mechanism is not dependent on one film's plot, star image, or historical context;
- at least one boundary is stated;
- it survives one more independent scene or prompt-output test.
