# Reference Audio as a Visual Control Track

Load this reference only when an actual audio reference should influence visible motion, impact peaks, cuts, shot scale, or section rhythm. This is a field-observed generation technique, not a guaranteed platform contract. Recheck the current surface and validate with outputs before making claims.

## Control Boundary

Reference audio can carry a time structure that the visual branch may interpret as movement, cuts, or energy changes. It does not replace:

- physical choreography, support, contact, receiver response, or recovery;
- identity, wardrobe, geometry, or spatial continuity control;
- final score, foley, dialogue, stems, loudness, or delivery mix;
- current platform capability verification.

`seedance-audio` owns audio role mapping and the control-track experiment. `action-rhythm-editing` supplies the approved physical beat map. A fight/prompt skill compiles the result. Output review verifies the actual cue-to-picture response.

## Choose the Input Mode

### Sparse custom SFX track

Use when the main problem is timing: a dash, one impact peak, a reversal, a pause, or an endpoint. Sparse cues are easier to attribute and revise.

### Complete music track

Use when the final music direction already exists or the whole visual style should follow its sections. Music is never tempo alone: instrumentation, dynamics, emotion, phrasing, and drops can also bias action style, shot scale, cut density, and lyrical holds.

### Two-pass mode

When both precision and style matter, validate the action with sparse SFX first, then test the complete music as a separate condition. Do not rewrite prompt, references, and audio together.

## Build from Visible Beats

Write 3-6 visible state changes before opening an audio editor:

```text
time/proportion | visible event | responsible actor/object | peak type | allowed camera response
```

Reject abstract targets such as “more epic” or “better rhythm.” Use observable targets: first displacement, sole heavy impact, receiver change, level change, brief reset, changed endpoint.

## Cue Families

Begin with the fewest cue types possible:

| Cue family | First test hypothesis | Common risk |
|---|---|---|
| Short whoosh / pass-by pulse | displacement, dash, speed spike | repeated cues may spread high-speed behavior across the whole clip |
| Strong transient | impact peak, contact emphasis, cut | may create too many close-ups, cuts, or frame-skipping feel |
| Drop / sudden gap | reversal, pause, endpoint | may become a lyrical hold or idle freeze |
| Sustained melody/harmony | emotion, footwork, whole-section behavior | can rewrite camera and narrative style, not just timing |

These are hypotheses, not a permanent dictionary. Model version, surface, mix, visual references, and prompt can change the mapping.

## Construction Rules

1. Match control-track duration to the target generation.
2. Place the single strongest peak first.
3. Add only the motion pulses required to reach it.
4. Add silence or reset space when the end state must read.
5. Avoid dense drums, vocals, and multiple competing timing systems.
6. Keep a cue sheet with exact cue positions and intended visible events.

The track passes the construction gate when a listener can point to its 3-6 main structural landmarks without seeing the video.

## Reference Role Contract

Use the real reference handle and state its visual role:

```text
{{Audio 1}} (visual timing control): controls action tempo, speed energy,
major peaks, and section turns only. Do not copy melody, lyrics, voice,
or final mix. Final sound will be produced separately.
```

Bind only indispensable landmarks:

```text
first short whoosh = first dash;
strongest transient = the sole impact peak plus receiver response;
final gap = brief reset and changed end state.
```

One cue should have one primary visible job. If video, timestamps, and audio all control timing, choose one master clock or state the priority explicitly.

## One-Variable A/B

Keep prompt, identity/environment references, duration, mode, and controllable settings stable:

- **A**: no audio reference or a neutral pulse.
- **B**: sparse control track.
- **Optional C**: complete target music.

Keep comparable sample counts. Do not compare only the best cherry-picked take.

## Cue-to-Picture Review

Record:

```text
cue time | intended visible event | actual response | delay/spread | side effect | one next change
```

Inspect motion peaks, receiver response, displacement, shot scale, cuts, expression close-ups, identity/wardrobe drift, geography, and whether reference audio leaked into the result. Preserve non-response and side effects; they are part of the evidence.

## Repair Map

| Symptom | Next single-variable change |
|---|---|
| Whole clip stays uniform | strengthen section contrast or add one clean gap; do not add many micro-cues |
| Too many close-ups/cuts | reduce strong transients or remove competing cue timbres |
| Speed spreads everywhere | shorten or separate continuous whoosh material |
| Impact is weak | keep one stronger transient and ensure the physical beat includes contact plus receiver response |
| Lyrical hold consumes action time | shorten the musical soft section or switch back to sparse SFX mode |
| Reference audio appears in output | separate/replace the track in post; the “do not output” phrase is not a guarantee |
| Wardrobe/identity drifts | reduce action/reference load and repair continuity; audio cannot own this failure |

## Music-Bias Heuristics

Treat these only as exploration priors from a limited tutorial sample:

- fast electronic material may favor two-character coverage and balanced action density;
- strong percussion may increase impact, cuts, or close-ups;
- epic orchestral phrasing may favor scale, close-ups, and interior/emotional holds;
- piano-led phrasing may favor footwork and dance-like continuity;
- rock may favor stronger impact and cut energy;
- non-action music can still control the image but may place long lyrical shots at unpredictable points.

Never promise that a genre will produce a specific camera or action result. Test the actual track.

## Output Template

```text
Visible control target:
Mode: sparse SFX / complete music / two-pass
Visible beat map:
Cue sheet:
Audio reference role:
A/B conditions:
Review fields:
Leakage and post fallback:
```

## Evidence and Limits

Distilled from a local 11:59 Seedance 2 tutorial archived in 2026-07. The tutorial showed a weak text-only action baseline, a custom wind/percussion control-track comparison, multiple music swaps under a nominally unchanged prompt, and occasional reference-audio leakage. The source did not publish seeds, all settings, repeated-trial counts, or all failures. Treat the method as an experimental loop, not a deterministic law.
