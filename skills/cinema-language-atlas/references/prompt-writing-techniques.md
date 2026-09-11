# Prompt Writing Techniques

Last researched: 2026-07-01
Status: active reference, platform-informed, not capsule-promoted

Use this file for turning film-language mechanisms into AI image/video prompts: prompt fields, positive control wording, timing and spatial locks, negative constraints, output review checks, and retry deltas.

## Research Questions

1. Should AI video prompts be written as natural prose, structured fields, or a hybrid?
2. Which prompt fields most reliably transfer film craft into generated motion?
3. When do negative constraints help, and when should they be rewritten as positive phrasing?
4. How should each prompt field map to a review check after generation?

## Working Controls

- Use a hybrid prompt: a short prose scene sentence plus structured control fields. The prose gives continuity; fields make camera, action, light, sound, timing, and constraints inspectable.
- Start with one primary shot event. Add details only when they protect intent: subject action, camera behavior, setting, light/material, sound cue, style, and output review check.
- Prefer positive, physical verbs over abstract intent: "the woman stops, looks toward the locked door, and lowers her breathing" is safer than "she feels threatened."
- For image-to-video, avoid restating every visible element from the start image. Use the prompt to direct motion, camera, reaction, and what must remain stable.
- Treat negative constraints as a last-mile guardrail. If a platform dislikes negative phrasing, convert "no camera movement" to "locked camera remains still."
- Keep a small constraint budget. Use positive locks for core behavior, and reserve negative prompts for a few unwanted elements that cannot be expressed as desired behavior.
- Lock time only for the few beats that matter. In a 5-10 second clip, more than two major actions, style shifts, or locations usually creates prompt overload.
- Pair every important prompt control with a review check. If a cue cannot be inspected in the output, it is not a strong control.

## Prompt Function Tags

- `prompt_contract`: the explicit set of things the output must prove.
- `positive_motion_control`: physical action phrased as what should happen, not what to avoid.
- `single_shot_event`: one dominant generated-video event with stable subject, location, and camera relation.
- `fielded_prompt`: prompt split into scene, camera, subject action, environment, light, sound, constraints, and review checks.
- `negative_to_positive_rewrite`: replacing unsupported "do not" phrasing with the desired stable behavior.
- `constraint_budget`: limiting constraints to the smallest set that protects intent without competing with the primary action.
- `camera_motion_contract`: camera movement written as start frame, trigger, path, subject relation, end frame, and review check.
- `pivot_vs_displacement`: separating pan/tilt/zoom from dolly/track/crane/handheld movement through space.
- `lens_distance_contract`: lens look written as focal-length class plus camera-subject distance, subject size, background scale, and review check.
- `camera_subject_distance_lock`: a prompt field that states whether the camera is physically close, mid-distance, or far from the subject.
- `background_scale_relation`: a prompt field that names whether background recedes, presses closer, stays readable, or flattens behind the subject.
- `face_rendering_gate`: an output review gate that checks whether a close-up exaggerates, flatters, flattens, or preserves facial planes as intended.
- `zoom_vs_dolly_boundary`: a prompt boundary separating optical attention change from physical camera approach.
- `lighting_material_contract`: light written as source logic, direction, quality, color relation, separation, material response, and review check.
- `motivated_source_lock`: tying a visible or implied world source to the light that shapes the subject.
- `source_zone_material_contract`: lighting written as source -> affected zone -> material response -> separation method -> review gate.
- `color_pool_boundary`: a prompt lock that limits a colored light to one motivated source and one named surface/space zone.
- `shadow_edge_check`: an output review gate for whether hard/soft light is visible through shadow-edge behavior, not through brightness alone.
- `material_response_gate`: an output review gate that checks whether skin, metal, glass, wet cloth, dust, smoke, or paint reacts differently to the same light.
- `separation_method_lock`: a prompt field that names how subject/background/layers separate: luminance, hue, saturation, rim, haze, falloff, or negative fill.
- `lighting_transition_contract`: light or color change written as before-state -> trigger -> source/zone change -> material response -> after-state -> review gate.
- `motivated_color_shift`: a color or color-temperature shift tied to a visible or implied source, story event, or blocking change, not a full-frame tint.
- `exposure_shadow_ramp`: a timed change in exposure, contrast, or shadow-edge behavior that remains motivated by source movement, dimming, or blocking.
- `material_response_transition`: a visible surface response change over time, such as wet cloth catching a cooler rim after a door opens.
- `light_state_change_review_gate`: an output review gate for before/after light state, trigger, affected/excluded zones, material response, and story consequence.
- `action_contact_contract`: action written as setup, attack vector, receiving zone, contact or near-miss relation, receiver response, environmental proof, recovery, and review check.
- `receiver_response_lock`: the struck, blocked, avoided, or affected body/object proves force after the beat.
- `environmental_proof`: a nearby surface, prop, costume, particle, or sound cue changes state to show consequence.
- `mass_timing_contract`: action weight written as preload -> acceleration -> peak -> follow-through -> braking -> recovery, scaled to body/weapon mass.
- `inertia_proof`: visible drag, overshoot, rebound, recoil, delayed end motion, surface response, or settling that proves mass did not stop weightlessly.
- `speed_contrast_curve`: a prompt rule that sells force through slow/loaded preparation, brief acceleration spike, and longer consequence rather than constant speed.
- `braking_recovery_gate`: an output review gate that checks whether the body/weapon/vehicle resolves momentum after the peak.
- `action_camera_responsibility`: a prompt block that assigns the camera one job in an action beat: prove geography, follow initiator, reveal contact, ride recoil, or stabilize consequence.
- `proof_frame`: the short readable frame window where contact, near-miss, state change, or receiver response must be visible.
- `shake_budget`: a bounded camera-shake rule: stable for setup/contact, micro-shake only at peak, stabilize for consequence.
- `information_token_frame`: each shot or camera move must deliver one legible action token: path, target, contact, reaction, obstacle, or changed spacing.
- `camera_obstruction_review_gate`: an output review gate that checks whether close framing, shake, blur, foreground wipe, or debris hid the required action proof.
- `fictional_danger_contract`: a screen-action prompt block that creates danger through readable near-miss, vulnerability cue, consequence, and recovery while staying fictional.
- `near_miss_proof`: a visible relation where the threat passes close enough to change body, cloth, prop, sound, or environment state without giving real-world execution detail.
- `vulnerability_cue`: a brief exposed-state cue such as lost footing, blocked exit, dropped guard, trapped hand, delayed breath, or prop failure that raises stakes.
- `safety_boundary_lock`: a prompt boundary that keeps action as fictional screen choreography and avoids operational stunt, weapon, injury, or harm instructions.
- `danger_mechanism_review_gate`: an output review gate that checks whether danger came from geography, near-miss, vulnerability, consequence, and recovery rather than gore, shaky blur, or hidden contact.
- `timed_beat_contract`: a short AI-video prompt written as a visible/audible beat timeline with triggers, holds, and review checks.
- `beat_anchor`: a timing point tied to performance pulse, action state change, camera movement stop, sound cue, music accent, or viewer-information change.
- `beat_anchor_contract`: a prompt block that gives every cut, hold, speed change, or camera change a visible/audible permission cue.
- `cut_permission_rule`: a rule that allows cuts only on named anchors such as breath, glance, grip, impact, sound cue, reveal, or camera stop.
- `viewer_registration_gate`: an output review gate that checks whether the viewer has enough hold time to understand the new information before the next beat.
- `density_curve_budget`: a prompt rule that limits how many motion, sound, edit, and information layers can change in each time window.
- `rhythm_overload_review`: an output review gate for whether fast timing hid causality, reaction, geography, or state change.
- `reaction_breath`: a deliberate hold after a cue, impact, line, or reveal so the viewer can register consequence before the next event.
- `dialogue_cut_permission_contract`: dialogue timing written as line/cue -> reaction owner -> reaction breath -> cut/hold permission -> sound lead/tail -> changed relation -> review gate.
- `reaction_breath_window`: a bounded pause after a line, sound, look, or object action that must reveal a decision, refusal, realization, or concealment.
- `line_tail_carryover`: a line or room-tone tail that continues over the listener/object/space after the speaker stops, changing how the new image is read.
- `prelap_pressure_cue`: a sound, breath, object, or offscreen cue that arrives before the visual answer and gives the cut or reaction permission.
- `dialogue_timing_review_gate`: an output review gate for cue order, reaction ownership, pause value, cut permission, audio/image offset, and final relation.
- `dialogue_reaction_contract`: dialogue written as want, resistance, gaze rule, reaction ownership, silence action, blocking change, and review check.
- `listener_ownership`: the listener's visible response carries the meaning, contradiction, delay, or new information after a line or cue.
- `reaction_ownership_contract`: a prompt block that names who owns the meaning after a line/cue and what the viewer must learn from the reaction.
- `line_to_reaction_timing`: a timing lock for whether reaction begins before the line, during it, after it, or after a silence/sound drop.
- `micro_behavior_tell`: a small visible behavior such as hand stop, breath hold, eye drop, prop grip, shoulder stillness, or delayed blink that proves hidden pressure.
- `eyeline_answer_gate`: an output review gate that checks whether the look direction, offscreen target, mirror/glass gaze, or returned eye contact answers the cue.
- `gaze_rule_lock`: eye contact, avoided eye contact, shared forward gaze, mirror/glass gaze, or offscreen look is treated as a stable scene rule.
- `silence_action`: a pause is written as withholding, deciding, measuring, absorbing, lying, refusing, or leaving rather than empty stillness.
- `constrained_dialogue_space_contract`: limited-space dialogue written as space type -> barrier/pressure rule -> gaze rule -> reaction owner -> blocking change/refusal -> review gate.
- `space_as_resistance`: a table edge, car direction, corridor depth, doorway, glass, seat, or exit works as an obstacle to the character's want.
- `blocking_delta`: the one movement or refusal to move that changes status, access, proximity, exposure, or information.
- `axis_gaze_lock`: a prompt lock that keeps eyelines, screen direction, mirror/window reflection, or shared forward gaze legible inside tight coverage.
- `small_space_dialogue_review_gate`: an output review gate for space rule, gaze rule, reaction ownership, blocking delta, and changed relation.
- `sound_image_contract`: sound written as source, timing, perspective, mix priority, visible reaction, and story-state change.
- `audio_cue_sheet`: a short timeline of sound events with source, material, distance, obstruction, and image consequence.
- `audio_event_priority_contract`: a prompt block that names one primary audio event, its source/material, time window, listener point, image consequence, and mix priority.
- `offscreen_source_protection`: a positive/negative lock that keeps the sound source hidden while preserving barrier, distance, and listener reaction.
- `mix_hierarchy_lock`: a prompt rule that states which sound layers dominate, support, or must be absent.
- `audio_visual_sync_gate`: an output review gate that checks whether the sound occurs in the named time window and causes the named visual reaction.
- `silence_layer_curve`: silence written as removed layers plus the remaining audible cue, especially breath, room tone, ringing, hum, or object tail.
- `foley_material_cue`: Foley written to prove texture, weight, contact, surface, body cost, or prop behavior.
- `sound_perspective_lock`: the prompt defines whose or where the hearing belongs to: character, camera, room, object, memory, or offscreen space.
- `sound_perspective_distance_clue_contract`: an onscreen/offscreen sound, distant sound, muffled sound, approaching source, hidden source, room-to-room cue, or distance reveal assigned to audio source status, listener point, distance/obstruction, acoustic quality, reveal policy, image consequence, and review proof.
- `audio_source_status_lock`: a prompt field that states whether the sound is onscreen, offscreen, diegetic, non-diegetic, internal, hidden, delayed-reveal, or never-revealed.
- `listener_point_distance_lock`: a prompt field that states where the audience hears from and how far the source is from that point.
- `obstruction_filter_lock`: a prompt field that states what filters the sound: door, wall, glass, floor, water, helmet, phone, speaker, crowd, weather, or body condition.
- `source_reveal_policy_lock`: a prompt field that states whether the source stays hidden, is revealed later, is misread then corrected, or remains ambiguous.
- `sound_distance_review_gate`: an output review gate for source status, listener point, distance, obstruction/filter, acoustic quality change, reveal policy, image consequence, and no generic ambience/score substitution.
- `offscreen_sound_reveal_clue_contract`: an offscreen sound, voice-off, hidden source, misread sound, delayed source reveal, sound-image contradiction, or correction beat assigned to assumed source, actual source, listener point, delay window, correction beat, reveal evidence, listener reaction, payoff, and review proof.
- `source_assumption_lock`: a prompt field that states what the viewer or character initially assumes the sound source is, and whether that assumption is allowed to be wrong.
- `actual_source_lock`: a prompt field that states what the sound source really is and whether it should be shown, delayed, withheld, or corrected.
- `delayed_reveal_lock`: a prompt field that states how long the source remains offscreen or misread before the image answers it.
- `sound_correction_beat_lock`: a prompt field that states what visual or audio evidence corrects the false source assumption without cheating.
- `offscreen_sound_reveal_review_gate`: an output review gate for assumed source, actual source, offscreen delay, correction beat, listener reaction, payoff, and no source teleport/unresolved ambiguity.
- `sound_bridge_prelap_clue_contract`: a sound bridge, prelap dialogue, prelap sound effect, incoming room tone, or audio-led scene transition assigned to outgoing image, incoming sound source, lead duration, cut/transition point, image answer, payoff, and review proof.
- `incoming_audio_source_lock`: a prompt field that states the source of the sound that begins before its image appears.
- `bridge_image_relation_lock`: a prompt field that states whether the incoming sound connects mood, location, story information, expectation, contrast, or reveal.
- `transition_permission_lock`: a prompt field that states what audio cue authorizes the cut, hold, dissolve, or scene change.
- `bridge_payoff_lock`: a prompt field that states what the next image proves about the sound after the transition.
- `sound_bridge_review_gate`: an output review gate for outgoing image, incoming sound, lead duration, transition point, image answer, payoff, and no accidental ambience/random audio.
- `postlap_audio_tail_clue_contract`: an L-cut, postlap, audio tail, outgoing dialogue tail, outgoing room tone, or previous-scene sound continuing over the next image assigned to outgoing source, carry duration, incoming image relation, cutoff/replacement point, payoff, and review proof.
- `outgoing_audio_source_lock`: a prompt field that states which previous-scene sound continues after the image cuts away.
- `audio_tail_duration_lock`: a prompt field that states how long the outgoing sound continues over the incoming image.
- `incoming_image_relation_lock`: a prompt field that states what the new image learns, contrasts, remembers, conceals, or reframes because of the outgoing sound tail.
- `tail_cutoff_replacement_lock`: a prompt field that states when the old audio fades, cuts, is masked, or is replaced by the new scene's sound.
- `postlap_audio_tail_review_gate`: an output review gate for outgoing source, carry duration, incoming image relation, cutoff/replacement, payoff, and no muddy accidental carryover.
- `audio_match_cut_clue_contract`: an audio match cut, sonic match, matched sound transition, or "one sound becomes another" assigned to outgoing sound shape, incoming matching source, sonic cut point, difference cue, image answer, payoff, and review proof.
- `outgoing_sound_shape_lock`: a prompt field that states the outgoing sound's rhythm, pitch/timbre, attack, duration, material, or envelope before the cut.
- `incoming_matching_source_lock`: a prompt field that states the new sound source that initially matches the outgoing sound shape.
- `sonic_cut_point_lock`: a prompt field that states exactly where the cut, blend, or overlap occurs inside the matched sound.
- `sonic_difference_cue_lock`: a prompt field that states what changes after the cut so the new source is legible rather than confused.
- `audio_match_cut_review_gate`: an output review gate for outgoing sound shape, incoming matching source, cut point, difference cue, image answer, payoff, and no random sound substitution.
- `silence_density_curve`: silence written as removed layers plus one remaining cue, not generic mute.
- `held_pause_clue_contract`: a held silence, pause, sound drop, withheld answer, listening beat, or decision pause assigned to silence owner, removed layers, remaining cue, pressure object/space, decision state, release cue, and review proof.
- `silence_owner_lock`: a prompt field that states whose silence matters: character, listener, room, object, crowd, offscreen source, or viewer-audition point.
- `pressure_object_space_lock`: a prompt field that keeps one visible object or space relation active during the pause so the silence has pressure, not empty duration.
- `decision_state_lock`: a prompt field that states what the pause changes: decide, refuse, conceal, absorb, measure, wait, listen, surrender, or leave.
- `held_pause_review_gate`: an output review gate for silence owner, removed sound layers, remaining cue, pressure object/space, visible decision state, release cue, and no dead-air/missing-audio feel.
- `subjective_listening_contract`: a prompt block that defines whose hearing owns the moment, which layers are filtered or removed, which cue remains, and what visible behavior changes.
- `auditory_filter_stack`: a layered sound instruction for obstruction, distance, body condition, memory, device playback, or underwater/behind-wall filtering.
- `remaining_cue_anchor`: the one sound left after a subjective reduction, such as breath, tinnitus tone, fabric rustle, room hum, tape hiss, or distant threat.
- `listening_pov_review_gate`: an output review gate that checks whether the audible perspective, removed layers, remaining cue, and visual reaction belong to the same listener.
- `breakdown_to_prompt_contract`: a shot-breakdown row converted into prompt fields by preserving objective evidence, shot function, timing, dominant track, and review proof.
- `function_chain_prompt`: a short prompt built from a sequence function chain such as orient -> reveal -> react -> state change, not from a list of stylish shot labels.
- `clip_to_prompt_review_loop`: a full loop that turns a clip breakdown into an original prompt and then reviews the generated output against the borrowed mechanism, not the source scene.
- `portable_mechanism_filter`: a boundary step that separates transferable function chains from source-bound characters, plot, dialogue, exact staging, period style, and iconic images.
- `source_scene_copy_guard`: a prompt and review guard against rewarding copied composition, characters, plot beats, dialogue, or recognizable copyrighted scene details.
- `reference_boundary_lock`: a researched film/example reference is translated into mechanism and do-not-copy boundary before becoming prompt wording.
- `state_change_review_gate`: an output review gate that checks initial state, trigger path, contact/action, changed state, hold, and no continuity cheat.
- `continuity_anchor_contract`: a prompt block that locks only the identity, costume, prop, scene, and style anchors that must survive motion or shot changes.
- `reference_role_lock`: an explicit statement of what each uploaded reference controls and what it must not control.
- `style_anchor_role_contract`: an explicit statement of what each named film/person/studio/reference controls, which layer it is allowed to influence, and what it must not copy.
- `mechanism_not_name_prompt`: replacing "in the style of X" with visible controls such as light source, cut rhythm, action geography, sound perspective, or surface finish.
- `do_not_copy_boundary`: a positive/negative lock against copied characters, plot, exact staging, signature palette, living-artist imitation, and reference-role leakage.
- `style_soup_review_gate`: an output review gate that checks whether multiple references merged into an uninspectable style collage or contradicted the scene.
- `cinematographer_camera_anchor_contract`: a named cinematographer, director, film, or lens reference assigned to one camera/lens/composition layer, one spatial mechanism, forbidden transfers, a name-free fallback, and review proof.
- `camera_layer_lock`: a prompt field that limits a camera style reference to lens-distance relation, camera height/angle, shot size, composition balance, movement trigger, depth/focus behavior, or screen-space relation.
- `name_free_camera_fallback`: the same camera mechanism rewritten without the person, film, or brand name so the prompt remains executable when names are removed.
- `composition_copy_guard`: a boundary against copying a famous frame's exact composition, character placement, production design, color palette, or iconic blocking.
- `camera_anchor_review_gate`: an output review gate for whether the reference contributed only the allowed camera/spatial mechanism and did not leak into story, costume, palette, acting, or edit rhythm.
- `action_director_anchor_contract`: a named action director, stunt team, film, martial-art film, or fight reference assigned to one action layer, one screen-safe mechanism, forbidden transfers, a name-free fallback, and review proof.
- `fight_layer_lock`: a prompt field that limits an action reference to geography roadmap, contact proof, rhythm oscillation, weapon/prop weight, group hierarchy, camera proof job, or danger mechanism.
- `name_free_action_fallback`: the same fight mechanism rewritten without the person, film, franchise, or martial-art name so the prompt remains executable when names are removed.
- `choreography_copy_guard`: a boundary against copying a famous fight's exact combo, stunt, weapon use, brutality texture, plot situation, injury detail, or operational method.
- `action_anchor_review_gate`: an output review gate for whether the reference contributed only the allowed screen-action mechanism and did not become unsafe how-to, gore, style soup, or hidden-contact blur.
- `sound_music_anchor_contract`: a named sound designer, composer, film, score, soundscape, or audio reference assigned to one listening/music layer, one mechanism, forbidden transfers, a name-free fallback, and review proof.
- `audio_layer_lock`: a prompt field that limits a sound/music reference to listening point, primary audio event, mix hierarchy, silence curve, Foley/material cue, music pulse, or sound-image transition.
- `name_free_audio_fallback`: the same audio mechanism rewritten without the person, film, score, motif, or sound-signature name so the prompt remains executable when names are removed.
- `score_signature_copy_guard`: a boundary against copying a famous score, melody, motif, sound logo, creature/device recipe, or recognizable soundtrack identity.
- `audio_anchor_review_gate`: an output review gate for whether the reference contributed only the allowed audio mechanism and did not become generic ambience, unwanted score, motif copying, or audio-visual mismatch.
- `production_design_anchor_contract`: a named film, production designer, world, architecture, prop, costume, or set-dressing reference assigned to one design layer, one story mechanism, forbidden transfers, a name-free fallback, and review proof.
- `worldbuilding_layer_lock`: a prompt field that limits a world/design reference to spatial rule, material logic, prop function, signage/graphic system, costume status, architecture behavior, or wear/history state.
- `name_free_design_fallback`: the same design mechanism rewritten without the film, designer, franchise, place, or IP name so the prompt remains executable when names are removed.
- `ip_world_copy_guard`: a boundary against copying a recognizable franchise world, iconic prop, set layout, costume silhouette, graphic language, faction mark, architecture, or branded design system.
- `design_anchor_review_gate`: an output review gate for whether the reference contributed only the allowed production-design mechanism and did not become IP imitation, surface decoration, or prop clutter.
- `performance_style_anchor_contract`: a named actor, acting tradition, film performance mode, or director-performer reference assigned to one observable behavior layer, one mechanism, forbidden transfers, a name-free fallback, and review proof.
- `behavior_layer_lock`: a prompt field that limits a performance reference to micro-behavior cue, gaze rule, blocking/status change, silence action, reaction ownership, voice intensity, or body tempo.
- `name_free_performance_fallback`: the same performance mechanism rewritten without the actor, film, role, or acting-school name so the prompt remains executable when names are removed.
- `actor_imitation_guard`: a boundary against copying a living actor's likeness, voice, signature mannerism, role identity, catchphrase, or recognizable performance.
- `performance_anchor_review_gate`: an output review gate for whether the reference contributed only the allowed behavior mechanism and did not become celebrity imitation, theatrical overacting, or vague emotion.
- `transition_style_anchor_contract`: a named editor, film, sequence, trailer, music video, or transition reference assigned to one match/transition layer, one bridge mechanism, forbidden transfers, a name-free fallback, and review proof.
- `match_layer_lock`: a prompt field that limits a transition reference to graphic match, match-on-action, eyeline answer, sound bridge, contrast cut, ellipsis, or rupture.
- `name_free_transition_fallback`: the same transition mechanism rewritten without the film, editor, sequence, or famous cut name so the prompt remains executable when names are removed.
- `famous_cut_copy_guard`: a boundary against copying an iconic match cut's source objects, plot leap, exact composition, timing, score cue, or recognisable sequence identity.
- `transition_anchor_review_gate`: an output review gate for whether the reference contributed only the allowed bridge logic and did not become source-scene copying or arbitrary stylish cutting.
- `documentary_realism_anchor_contract`: a documentary, direct-cinema, cinema-verite, observational, interview, archive, or news-footage reference assigned to evidence status, camera relation, sync sound, staging boundary, disclosure, and review proof.
- `evidence_status_lock`: a prompt field that states whether the clip is fictional, staged reconstruction, user-provided real event, interview, archive-like insert, or observational simulation.
- `camera_intervention_lock`: a prompt field that names the camera's documentary relation: fly-on-wall observer, acknowledged participant, interviewer, witness, body-worn view, archive observer, or reflexive visible camera.
- `non_deceptive_realism_guard`: a boundary against fake news claims, real logos, real names, dates/locations, official watermarks, crisis footage, or any prompt wording that asks the output to pass as real evidence.
- `documentary_realism_review_gate`: an output review gate for whether documentary texture comes from camera relation, available light, sync sound, subject behavior, and clear fiction/disclosure boundaries rather than deceptive authenticity.
- `archival_insert_contract`: an archive-like, found-footage, home-movie, training-tape, security-tape, broadcast-recording, or degraded-film insert assigned to source status, artifact layer, continuity boundary, provenance disclosure, and review proof.
- `source_status_label`: a prompt field that states whether the insert is fictional archive, staged reconstruction, public-domain source, user-provided source, diegetic tape, or invented prop footage.
- `artifact_layer_lock`: a prompt field that limits aged-media texture to one or two inspectable layers such as gate weave, dust, scratches, faded dye, tape noise, interlacing, timecode, splice mark, or audio wow/flutter.
- `forged_archive_guard`: a boundary against fake institutional provenance, real archive watermarks, real dates/places/events, official seals, news lower-thirds, disaster footage, or forged evidence claims.
- `archival_insert_review_gate`: an output review gate for whether the insert's source status, artifact layer, continuity relation, and non-forgery boundary are legible.
- `title_graphic_insert_contract`: a title card, intertitle, lower-third, chapter card, date/location card, onscreen text, or graphic insert assigned to text payload, typography role, duration, placement, transition relation, and review proof.
- `text_payload_lock`: a prompt field that states the exact words or controlled information payload the viewer must read, with no extra model-invented text.
- `reading_duration_lock`: a prompt field that gives text enough screen time and prohibits motion, cuts, or background action from outrunning legibility.
- `text_scene_priority_lock`: a prompt field that states whether text leads, supports, interrupts, labels, translates, withholds, or confirms the scene information.
- `typography_copy_guard`: a boundary against copying a famous title sequence, exact type treatment, branded font identity, logo, credit order, or studio/film title design.
- `title_insert_review_gate`: an output review gate for whether text is readable, accurate, timed, placed clear of action/subtitles, and functionally related to the shot or transition.
- `screen_ui_insert_contract`: a map, diagram, dashboard, monitor UI, radar, chart, phone screen, scanner overlay, or control-panel insert assigned to diegetic status, information payload, interaction timing, legibility, and review proof.
- `diegetic_ui_status_lock`: a prompt field that states whether the UI exists inside the story world, is a non-diegetic overlay, appears on a physical screen, or is an imagined/subjective visualization.
- `ui_information_payload_lock`: a prompt field that limits the UI to one required decision, status, route, warning, comparison, or clue rather than decorative interface clutter.
- `interaction_timing_lock`: a prompt field that ties UI change to a visible hand action, gaze, alarm, scan, system status, or cut permission.
- `fui_clutter_guard`: a boundary against unreadable sci-fi panels, random labels, fake brand/system marks, impossible data density, gratuitous graphs, or UI animation that hides the story information.
- `screen_ui_review_gate`: an output review gate for whether diegetic status, payload, labels, interaction timing, and scene consequence are legible.
- `split_screen_layout_contract`: a split-screen, double-screen, triptych, quad-screen, multi-panel, comic-panel, surveillance grid, or simultaneous-layout prompt assigned to panel count, panel jobs, temporal relation, viewer priority, seam logic, and review proof.
- `panel_count_lock`: a prompt field that fixes how many panels appear and what each panel owns, preventing extra generated panels or merged layouts.
- `temporal_relation_lock`: a prompt field that states whether panels are simultaneous, staggered, expectation-vs-reality, before/after, parallel action, memory/live contrast, or cause/effect.
- `viewer_priority_cue`: a prompt field that tells the viewer which panel to read first or which panel owns sound, motion, brightness, size, or action timing.
- `seam_logic_guard`: a boundary against arbitrary collage, moving panel borders, inconsistent aspect ratios, copied comic/page layouts, or seams that hide required action.
- `split_screen_review_gate`: an output review gate for whether panel count, panel ownership, timing relation, viewer priority, seam stability, and non-copy boundary are visible.
- `rapid_montage_sequence_contract`: a short montage, rapid sequence, training montage, time-compression burst, clue burst, prep sequence, trailer-like beat stack, or image-chain prompt assigned to shot count, beat function, order logic, density curve, and final proof hold.
- `montage_shot_count_lock`: a prompt field that fixes how many montage shots/inserts appear and what each shot contributes.
- `beat_function_sequence`: a prompt field that names each montage beat's job: setup, repeat, escalate, contrast, compress time, reveal clue, compare states, or prove transformation.
- `montage_density_budget`: a boundary that limits simultaneous location, action, camera, sound, and text changes inside a short AI-video montage.
- `final_proof_hold`: a required final hold after a montage burst that proves the new state, decision, object, body cost, or story consequence.
- `montage_sequence_review_gate`: an output review gate for shot count, beat order, density, transition logic, final proof, and no copied montage identity.
- `voiceover_narration_contract`: a voiceover, narration, commentary, inner monologue, documentary narration, radio voice, phone voice, device playback, or explanatory voice assigned to narrator status, source, timing, image relation, mix priority, and redundancy boundary.
- `narrator_status_lock`: a prompt field that states whether the voice is first-person, third-person, character memory, unreliable, documentary guide, onscreen speaker, offscreen source, device playback, or non-diegetic narrator.
- `image_voice_relation_lock`: a prompt field that states whether the voice explains, contradicts, withholds, reframes, foreshadows, trails, or answers the image.
- `information_timing_lock`: a prompt field that schedules when narration reveals information relative to image beats, cuts, reactions, silence, or visible cues.
- `redundant_narration_guard`: a boundary against voiceover that merely repeats visible action, over-explains emotion, competes with dialogue, invents unsupported facts, or turns the clip into audio exposition.
- `narration_review_gate`: an output review gate for whether narrator status, source, timing, image relation, mix priority, and non-redundancy are audible/reviewable.
- `memory_flashback_insert_contract`: a memory, flashback, past-tense insert, recollection fragment, trauma fragment, or remembered image assigned to memory status, present trigger, one past payload, texture budget, return anchor, and review proof.
- `memory_status_lock`: a prompt field that states whether the insert is character memory, objective past event, unreliable memory, imagined reconstruction, dream residue, or disputed recollection.
- `present_trigger_anchor`: a prompt field that ties the memory insert to a visible/audible present-tense cue such as a prop touch, sound, smell, line, gaze, location, or repeated gesture.
- `memory_texture_budget`: a boundary that limits memory styling to one or two controlled image/sound differences instead of generic sepia, blur, glow, white flash, or random dream filter.
- `present_return_anchor`: a prompt field that returns from the memory insert to the same present-tense body, prop, sound, gaze, or location state.
- `flashback_insert_review_gate`: an output review gate for whether memory status, trigger, past payload, texture difference, return anchor, and present/past separation are legible.
- `subjective_unreality_insert_contract`: a dream, imagination, fantasy, hallucination, altered perception, intrusive image, or wish/fear visualization assigned to subjective owner, trigger, reality boundary, one unreal payload, texture budget, return/reveal anchor, and review proof.
- `subjective_status_lock`: a prompt field that states whether the insert is dream, fantasy, imagined outcome, hallucination, fear image, wish image, intrusive thought, altered perception, or symbolic visualization.
- `reality_boundary_lock`: a prompt field that states whether the viewer knows the insert is unreal immediately, discovers it at the return, or remains deliberately uncertain.
- `unreal_payload_lock`: a prompt field that limits the subjective insert to one impossible or altered element such as a room stretching, object changing state, shadow moving independently, or repeated gesture looping.
- `unreality_texture_budget`: a boundary that limits visual/sound distortion to one or two controlled differences rather than generic surreal clutter, horror filter, or uncontrolled dream logic.
- `unreality_reveal_gate`: an output review gate for subjective owner, trigger, reality boundary, unreal payload, texture budget, return/reveal anchor, and non-stigmatizing portrayal.
- `unreliable_perception_reveal_contract`: a false perception, misleading POV, false continuity, red-herring cue, withheld geography, or reality-correction edit assigned to evidence status, false cue, viewer knowledge, correction beat, truth anchor, and review proof.
- `perceptual_evidence_status_lock`: a prompt field that states whether the cue is objective evidence, character perception, mistaken inference, staged deception, red herring, incomplete view, or later-corrected information.
- `false_cue_lock`: a prompt field that names the one cue the viewer is allowed to misread and the exact false inference it creates.
- `viewer_knowledge_lock`: a prompt field that states whether the viewer is misled with the character, ahead of the character, behind the character, or uncertain until the correction beat.
- `correction_beat_lock`: a prompt field that reveals the truth by changing angle, scale, sound source, object state, missing context, or geography.
- `reality_reveal_review_gate`: an output review gate for false cue, allowed inference, viewer knowledge state, correction beat, truth anchor, and no-cheat boundary.
- `object_clue_evidence_insert_contract`: an object clue, evidence insert, prop detail, document clue, trace, mark, missing object, red herring, or payoff object assigned to clue status, attention cue, one readable payload, payoff beat, red-herring boundary, and review proof.
- `clue_status_lock`: a prompt field that states whether the object is true clue, red herring, planted evidence, character misread, environmental trace, continuity clue, missing-object clue, or payoff object.
- `attention_cue_lock`: a prompt field that names how the viewer notices the clue: framing, focus pull, hand action, sound cue, light hit, color/shape contrast, reaction glance, or brief hold.
- `clue_payload_lock`: a prompt field that limits the object clue to one readable information payload such as mark, number, mismatch, absence, damage, residue, position, or changed state.
- `payoff_beat_lock`: a prompt field that states when and how the clue is used, corrected, contradicted, or returned to later.
- `evidence_insert_review_gate`: an output review gate for clue status, attention cue, readable payload, payoff relation, red-herring boundary, and no fake-evidence claim.
- `wardrobe_clue_contract`: a costume, garment, uniform, accessory, fabric wear, repair mark, stain, color change, missing item, or wardrobe continuity clue assigned to garment status, one readable wardrobe payload, attention cue, social/character signal, payoff beat, and copy/brand guard.
- `garment_status_lock`: a prompt field that states whether the clothing detail is uniform/status marker, disguise, continuity clue, class/work signal, damage trace, emotional-state cue, red herring, or payoff garment.
- `wardrobe_payload_lock`: a prompt field that limits the costume clue to one inspectable garment detail such as missing badge, torn cuff, reversed coat, fresh stain, repaired seam, mismatched button, changed color layer, or hidden lining.
- `costume_change_cue`: a prompt field that states how the wardrobe change is noticed: entrance contrast, hand adjustment, close insert, reaction glance, light catch, sound of fabric/accessory, or before/after continuity comparison.
- `wardrobe_copy_brand_guard`: a boundary against copying iconic costume silhouettes, logos, uniforms, fashion labels, designer signatures, living-person likeness, or real institutional marks.
- `wardrobe_clue_review_gate`: an output review gate for garment status, readable wardrobe payload, attention cue, social/character signal, payoff relation, continuity, and no brand/IP leakage.
- `makeup_hair_body_state_contract`: a makeup, hair, facial mark, sweat/dust state, continuity mark, period/role look, fatigue cue, disguise tell, or body-state clue assigned to appearance status, one readable appearance payload, attention cue, story consequence, continuity mark, and identity/safety guard.
- `appearance_status_lock`: a prompt field that states whether the visible appearance detail is continuity mark, fatigue/weather trace, role/status makeup, period cue, disguise tell, emotional-state cue, recovery/progression cue, or payoff appearance clue.
- `appearance_payload_lock`: a prompt field that limits makeup/hair/body-state information to one inspectable detail such as smudged eyeliner, soot on one cheek, damp hair at one temple, missing hairpin, faded lipstick, dust line, pale under-eye tone, or changed beard length.
- `continuity_mark_lock`: a prompt field that keeps the appearance clue on the same side, body zone, hair section, or facial area across shots until a stated change/payoff.
- `identity_safe_makeup_guard`: a boundary against celebrity likeness, living-person imitation, race/age/weight transformation, medical diagnosis, gore, injury spectacle, beauty-filter drift, or prosthetic identity swap unless explicitly safe and fictional.
- `appearance_clue_review_gate`: an output review gate for appearance status, one readable payload, attention cue, story consequence, continuity side/zone, and identity/safety boundary.
- `hand_object_interaction_clue_contract`: a hand/object clue, object pickup, handoff, touch, button press, pocketing, palming, reveal, or prop ownership change assigned to hand owner, object payload, contact proof, start/end state, continuity side, consequence, and review proof.
- `interaction_ownership_lock`: a prompt field that states which character, which hand, and which object owns the interaction before and after the beat.
- `contact_proof_lock`: a prompt field that requires visible contact evidence such as pinch, grip, compression, finger wrap, surface indentation, object shadow, changed object position, or hand reaction.
- `transfer_state_lock`: a prompt field that states the object's start location, transfer path, receiver/hidden location, and final visible or intentionally concealed state.
- `conceal_reveal_timing_lock`: a prompt field that names when the object is hidden, when it is shown, and what viewer/character knowledge state changes.
- `interaction_clue_review_gate`: an output review gate for hand owner, object identity, contact proof, transfer/conceal-reveal path, final state, continuity side, consequence, and no fake-contact/teleport.
- `set_dressing_clue_contract`: an object placement, set-dressing detail, furniture/prop arrangement, missing item, displaced object, repeated decor pattern, or before/after room state assigned to placement status, viewer priority, one readable placement payload, before/after state, payoff beat, clutter boundary, and review proof.
- `placement_status_lock`: a prompt field that states whether the placed object is baseline decor, true clue, misdirection, missing-object absence, changed-state evidence, social/status signal, memory anchor, or payoff set dressing.
- `placement_payload_lock`: a prompt field that limits set dressing to one inspectable placement relation such as object out of place, empty dust outline, chair angled toward door, doubled item, missing pair, reversed frame, blocked path, or newly cleared surface.
- `viewer_priority_lock`: a prompt field that names how the viewer notices the placement without clutter: composition, depth layer, focus, light hit, color/shape contrast, character glance, blocking path, or short hold.
- `before_after_set_state_lock`: a prompt field that states the baseline set state and the changed or payoff state that proves the placement mattered.
- `set_dressing_clutter_review_gate`: an output review gate for placement status, readable payload, viewer priority, before/after state, payoff relation, and no extra decor clutter.
- `spatial_path_blocking_clue_contract`: a route, blocking path, obstruction, reveal path, threshold crossing, actor movement, eyeline-to-target, or geography payoff assigned to route status, start point, obstruction/reveal, actor path proof, end point, geography payoff, and review proof.
- `route_status_lock`: a prompt field that states whether the path is available, blocked, misleading, hidden, newly opened, refused, redirected, or payoff route.
- `actor_path_proof_lock`: a prompt field that requires visible actor movement evidence such as start position, screen direction, step count, turn, pause, changed depth plane, threshold crossing, or body orientation toward target.
- `obstruction_reveal_lock`: a prompt field that states what blocks view or access, how movement changes visibility/access, and what new geography or object becomes readable.
- `geography_payoff_lock`: a prompt field that ties the path change to a later decision, escape, reveal, comparison, or corrected inference.
- `blocking_path_review_gate`: an output review gate for route status, start/end positions, obstruction/reveal, actor path proof, screen direction/geography, payoff, and no teleport/false geography.
- `eyeline_gaze_target_clue_contract`: an eyeline clue, gaze shift, look-off, glance to object, gaze reveal, answer shot, watched/unwatched target, or character/viewer knowledge beat assigned to gaze owner, target status, gaze cue, answer shot, knowledge state, spatial relation, payoff, and review proof.
- `gaze_owner_lock`: a prompt field that states whose eyes/gaze drive the clue, whether the viewer shares that gaze, and whether another character notices it.
- `target_status_lock`: a prompt field that states whether the looked-at target is visible, offscreen, hidden, misread, forbidden, watched, ignored, revealed later, or payoff target.
- `answer_shot_lock`: a prompt field that states whether the prompt needs an answer shot, what it shows, when it appears, and whether it confirms, delays, or corrects the gaze.
- `knowledge_state_lock`: a prompt field that states whether viewer and character know the same target, viewer knows before character, character knows before viewer, or target remains uncertain.
- `eyeline_review_gate`: an output review gate for gaze owner, gaze direction, target status, answer shot, spatial relation, knowledge state, payoff, and no random eye drift.
- `reaction_response_clue_contract`: a reaction shot, response beat, listener/object response, offscreen-cue reaction, reveal reaction, or micro-behavior clue assigned to trigger owner, response owner, reaction timing, micro-behavior proof, knowledge shift, coverage rule, payoff, and review proof.
- `trigger_owner_lock`: a prompt field that states what causes the reaction, where the trigger comes from, and whether the viewer, character, or both can identify it.
- `response_owner_lock`: a prompt field that states whose reaction carries the meaning and whether the response belongs to face, hand, breath, posture, object handling, or held silence.
- `reaction_timing_lock`: a prompt field that states whether the reaction starts before, during, immediately after, or after a held delay from the cue.
- `response_knowledge_shift_lock`: a prompt field that states what the viewer learns from the reaction: recognition, refusal, concealment, decision, fear, lie, status shift, or corrected inference.
- `reaction_response_review_gate`: an output review gate for trigger, response owner, timing, micro-behavior proof, knowledge shift, coverage rule, payoff, and no generic acting filler.
- `rhythm_style_anchor_contract`: a named editor, director, film, or rhythm reference assigned to one timing layer, one mechanism, forbidden transfers, a name-free fallback, and review proof.
- `editor_reference_layer_lock`: a prompt field that limits an editor or rhythm reference to cut permission, hold length, sound bridge, reaction breath, density curve, performance pulse, or camera/edit handoff.
- `name_free_rhythm_fallback`: the same rhythm mechanism rewritten without the person or film name so the prompt remains executable when names are removed.
- `cut_pattern_copy_guard`: a boundary against copying a famous sequence's exact cut order, plot reveal, dialogue, montage identity, or signature structure.
- `rhythm_anchor_review_gate`: an output review gate for whether the reference contributed only the allowed timing mechanism and did not become style soup.
- `allowed_change_block`: a small list of motion, expression, lighting, cloth, crop, or pose changes that may vary without breaking continuity.
- `continuity_drift_review_gate`: an output review gate that separates face drift, costume drift, prop drift, spatial drift, and style/reference-role confusion.
- `shot_handoff_contract`: a multi-shot prompt block that turns one shot's end state into the next shot's start state through pose, screen direction, object relation, action phase, and sound carryover.
- `last_frame_to_first_frame_lock`: an image/video continuation lock that treats the previous final frame as starting evidence, not as a style prompt.
- `action_bridge_prompt`: a prompt bridge for match-on-action or cut-on-action: outgoing motion phase -> incoming motion phase -> same action vector -> new information.
- `screen_direction_bridge`: a continuity lock for left/right travel, eyeline answer, object side, and action vector across generated clips.
- `handoff_review_gate`: an output review gate that separates shot-join failure from identity drift, direction reversal, pose reset, prop jump, and style reset.
- `mechanical_deployment_contract`: compact form A -> release -> stage chain -> mass migration -> regrip/support -> lock/settle -> new handling proof.
- `lock_state_review_gate`: an output review gate for deployed, assembled, opened, extended, transformed, or locked mechanical forms.
- `no_soft_morph_boundary`: a negative/positive boundary against gel-like morphing, duplicated parts, magic growth, identity swap, and hidden topology change.
- `generated_contract_review_sheet`: a post-output review table that scores the generated clip against the prompt contract before judging taste.
- `evidence_gate_matrix`: a review matrix that separates subject, action, camera, space, light/material, sound, style/reference, continuity, and final state.
- `failure_attribution_ladder`: a retry rule that attributes failure to missing prompt field, conflicting prompt field, platform/mode limit, reference-role leakage, or model miss.
- `minimum_retry_delta`: the smallest next prompt change that repairs one failed evidence gate while preserving successful gates.
- `review_check_binding`: every key prompt field has a visible or audible validation check.
- `prompt_delta`: the smallest retry edit that repairs one failed field without rewriting stable output.

## Prompt Skeleton

```text
scene:
  one-sentence visible premise:
  duration:
  aspect ratio / format:

subject and action:
  primary subject:
  primary action:
  secondary motion:

camera:
  shot size / angle:
  movement:
  lens / focus, if needed:
  stability lock:

space and light:
  location:
  time / weather:
  motivated light:
  material or texture emphasis:

sound, if supported:
  source:
  timing:
  distance / obstruction:
  mix priority:

style:
  medium / finish:
  color / contrast:
  reference role, if any:

constraints:
  preserve:
  avoid or positive rewrite:

review checks:
  visible proof:
  audible proof:
  failure trigger:
```

## Prompt Rewrite Comparison Card

Use this when a prompt is cinematic but hard to diagnose. The goal is not to make the prompt longer; the goal is to expose the contract, remove unsupported assumptions, and create review checks.

```text
rewrite_id:
platform / mode:
source prompt:

missing or vague fields:
  platform bounds:
  subject / action:
  camera:
  space / light:
  sound:
  style:
  constraints:
  review checks:

rewrite plan:
  keep:
  remove:
  split into separate shot, if needed:
  convert negative to positive:
  one dominant event:

fielded prompt:
  platform bounds:
  one-sentence premise:
  subject and action:
  camera:
  space and light:
  sound, if supported:
  style:
  constraints:
  review checks:

why this rewrite is better:
validation_status:
```

### Example Rewrite - Vague Suspense Prompt

Source prompt -> "Make a cinematic suspense video of a detective in a dark hallway hearing something scary, very tense, no monster reveal, realistic movie style."

Observation -> The source prompt has mood, genre, and a negative constraint, but it does not specify duration, shot type, sound timing, listener reaction, barrier, light source, or output proof.

Mechanism -> Convert mood words into a contract: one location, one barrier, one sound event, one visible reaction, one camera behavior, one review check.

Prompt rewrite ->

```text
platform bounds:
  8-second text-to-video, single continuous shot, native audio if supported, 16:9.

one-sentence premise:
  A detective alone in a dim apartment hallway pauses when an unseen sound comes from behind a closed door.

subject and action:
  The detective kneels beside a small recorder, then freezes and lowers his breathing after the sound.

camera:
  Locked-off medium-wide shot; no zoom or pan; the detective and the closed door remain in frame.

space and light:
  Narrow apartment hallway at night; weak practical lamp from camera-left; laptop screen adds cool fill on the detective's hands.

sound, if supported:
  0-3s low room tone and faint recorder hiss; at 4s one muffled floorboard creak comes from behind the closed door; 5-8s the recorder hiss stops as the detective taps pause.

style:
  Realistic crime-thriller, restrained contrast, natural shadows, no trailer score.

constraints:
  Door remains closed; sound source stays offscreen; the camera remains still; no monster, no jump-scare sting, no narration.

review checks:
  Closed door visible throughout; creak occurs before reaction; detective visibly freezes and pauses recorder; no visible source reveal; no music masks the cue.
```

Applicable scenes -> Suspense, horror, crime listening, offscreen threat, dialogue-free AI video tests.

Misuse boundary -> Do not reuse this exact setup for every suspense prompt. Transfer the rewrite method, not the detective/hallway content.

Validation status -> Source-backed prompt rewrite pattern; not generated-output validated.

## Negative Constraint Rewrite Card

Use this when a prompt contains many "no / don't / avoid" instructions or when the negative constraint is actually the main creative intent.

```text
constraint_id:
source phrase:
why it exists:
risk if written as negative:

positive lock:
  desired stable behavior:
  object / space / action to preserve:
  timing or screen position:

negative prompt, only if still needed:
  unwanted elements:
  unwanted mood / style:
  unwanted source reveal:

review check:
  visible / audible proof:
  failure trigger:
```

### Constraint Rewrite Table

| Weak or risky wording | Better positive lock | Optional negative prompt | Review check |
| --- | --- | --- | --- |
| no camera movement | locked-off tripod shot; camera remains still for the full clip | handheld shake, zoom, pan | frame edges and subject scale stay stable |
| don't reveal the monster | closed door remains visible and shut; sound source stays offscreen | monster, creature, visible intruder | no source appears; barrier remains closed |
| no overacting | restrained performance; actor holds breath, still shoulders, small eye turn | exaggerated crying, shouting | reaction is visible but small |
| no fake-looking impact | receiver staggers into table; glass slides; attacker resets stance | rubbery motion, floaty hit | body and environment show consequence |
| not plastic-looking armor | brushed steel plates catch hard rim light; edges show scratches and weight | plastic shine, toy surface | material reflects light like metal |
| no music | foreground Foley, room tone, and one offscreen cue are mix priority | score, trailer sting, drone | sound cue is audible and not masked |
| don't change identity | preserve same face, costume, hairstyle, prop silhouette, and color placement | new outfit, face drift | identity markers remain consistent |

### Constraint Budget Rule

- Use at most three constraint lines in the first prompt: one continuity lock, one source/reveal lock, and one style/audio exclusion.
- Rewrite a negative as positive when the desired state is visible: "door remains closed" beats "do not open the door."
- Keep a pure negative prompt only for unwanted elements that are easy to list: "logos, subtitles, extra limbs, monster, text overlay."
- Every constraint must have a review check. If no one can inspect it in the output, remove it or rewrite it.

## Constrained Dialogue Space Prompt Card

Use this when a dialogue scene happens at a table, inside a car, in a corridor, at a doorway, in an elevator, bedside, office, booth, train compartment, or any limited space where the scene risks becoming flat talking heads. The space must create resistance to a character's want.

```text
constrained_dialogue_id:
platform / mode:
clip duration:
space type:

space-dialogue contract:
  character wants:
  resistance / forbidden truth:
  space rule:
  barrier / pressure object:
  gaze rule:
  reaction owner:
  micro-behavior tell:
  blocking delta or refusal:
  camera / coverage rule:
  sound or silence cue:
  changed relation / after-state:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Constrained Dialogue Space Table

| Space | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| table / desk | "table edge divides them; speaker leans in, listener keeps both hands on the folder and does not cross the edge" | negotiation, interrogation, family conflict | Do not rely on generic shot/reverse-shot if the table does nothing | barrier, hands, lean/refusal, and status shift are visible |
| car / taxi | "driver watches road; passenger studies driver in profile; only direct glance happens after the withheld name" | confession, avoidance, divided attention | Do not stage as face-to-face room dialogue | shared forward gaze, mirror/window/profile relation, and road attention remain clear |
| corridor | "long corridor is a pressure lane; exit visible behind listener; speaker closes distance one step after the lie" | pursuit, public pressure, blocked escape | Do not add decorative depth with no access rule | lane, exit, distance change, and access pressure are readable |
| doorway / threshold | "visitor stays outside the half-open door; host blocks the gap with shoulder, then steps aside after the question" | access, invitation/refusal, reveal | Do not let the door vanish after establishing it | threshold state and who controls crossing are visible |
| glass / reflection | "answer lands on window reflection; face and outside motion layer together, direct look withheld" | car/train/interrogation glass, secrecy | Do not add reflections that hide expressions | reflection has one job and does not erase reaction |
| seated height shift | "A remains seated after accusation while B stands, reversing height control" | status changes without changing room | Do not make movement busy or theatrical | one movement/refusal changes status relation |

### Constrained Dialogue Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| static talking heads | blocking delta absent | add one lean, stand, seat change, turn away, blocked exit, or refusal to move |
| eye contact drifts randomly | gaze rule absent | define direct, avoided, shared-forward, reflection, mirror, or offscreen gaze |
| space feels decorative | space rule absent | state how table/car/corridor/doorway blocks, exposes, or delays a want |
| reaction feels melodramatic | reaction owner/micro-tell absent | assign the beat to one listener and one small behavior |
| geography breaks | camera/axis rule absent | keep axis side, screen direction, door/exit side, or shared forward direction stable |
| too much happens | prompt overload | keep one want, one resistance, one space rule, one blocking delta, and one after-state |

### Minimum Constrained Dialogue Prompt

```text
8-second restrained table scene. Space rule: the table edge is the barrier; the sealed folder sits on the listener's side and must remain visible.
Character want/resistance: speaker wants the folder opened; listener refuses without saying why.
Gaze rule: speaker holds eye contact; listener looks at the folder, then at the exit, never directly back until the final beat.
Blocking delta: at 5s the speaker leans across the table; listener does not move, only tightens one hand on the folder.
Camera/coverage: locked medium two-shot from the table corner, keeping both faces, hands, folder, and exit line readable; no random cutaways.
Sound/silence: brief room tone drop after the lean, no score.
After-state: speaker loses pressure because the listener's stillness owns the beat.
Negative/lock: no speechifying, no theatrical gestures, no random eye drift, no extra characters, no camera move hiding hands or folder.
Review: space barrier, gaze rule, reaction owner, micro-tell, blocking delta/refusal, and changed relation are visible.
```

## Camera Movement Prompt Card

Use this when a prompt asks for cinematic camera movement, tracking, dolly, pan, tilt, handheld, push-in, pull-out, crane, orbit, zoom, or a locked camera. The camera movement must have a job; otherwise use a stable shot.

```text
movement_id:
platform / mode:
clip duration:

camera movement contract:
  movement type:
  start frame:
  trigger:
  movement path:
  subject relation:
  speed / texture:
  end frame:
  new information or feeling:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Camera Movement Prompt Table

| Movement | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| locked-off | "locked-off tripod shot; frame remains stable" | listening, tension, performance, offscreen space | Do not use as empty prestige stillness | frame edges and subject scale remain stable |
| pan | "camera pans slowly from closed door to listener" | scanning or transferring attention left/right | Pan does not move viewpoint through space | background perspective does not shift like dolly |
| tilt | "camera tilts up from boots to face" | vertical reveal, height, scale, status | Tilt can feel like a scan, not approach | frame pivots upward/downward from fixed point |
| dolly / push-in | "slow dolly-in from medium shot to tight face over 6s" | narrowing attention, pressure, realization | Do not write push-in if you need only optical enlargement | subject grows while background perspective subtly changes |
| pull-out | "slow dolly-out from close face to reveal empty room" | recontextualizing, isolation, consequence | Avoid if the reveal is not important | end frame shows new surrounding information |
| tracking / follow | "camera tracks beside the runner, keeping her profile and pursuer in depth" | preserving moving relation or geography | Do not let camera outrun the action | subject relation stays consistent across movement |
| handheld | "subtle handheld following at shoulder height, small human instability" | bodily proximity, urgency, instability | Do not use handheld as generic seriousness | shake is controlled and does not hide action |
| crane / boom | "camera rises from table to reveal crowd behind them" | vertical recontextualization, scale, discovery | Do not use as spectacle without new information | end frame contains revealed vertical context |
| orbit / arc | "slow half-orbit around the suspect while background parallax shifts" | changing power, uncertainty, object inspection | Avoid full spin if it breaks geography | subject remains centered; background relation changes |
| zoom | "slow optical zoom to isolate the envelope; camera position stays fixed" | optical attention, surveillance, stylized emphasis | Do not use zoom when physical approach is desired | subject size changes without viewpoint displacement |

### Camera Movement Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| Camera drifts randomly | no start/end frame or movement path | lock start frame, end frame, and one movement direction |
| Push-in becomes zoom | physical displacement not stated | write "camera physically dollies closer; background parallax changes" |
| Tracking loses the subject | subject relation missing | state "keep subject centered / profile / same distance" |
| Handheld hides action | movement texture too broad | write "subtle handheld, action remains readable, no whip shake" |
| Locked shot moves anyway | positive stability lock missing | write "locked-off tripod shot; frame edges stay fixed" |
| Movement reveals too much | end frame not bounded | state exactly what remains hidden and what is revealed |
| Motion fights action | too many simultaneous changes | keep either subject action or camera movement primary, not both |

### Minimum Camera Motion Prompt

```text
Camera: [movement type] from [start frame] to [end frame] over [duration].
Trigger: movement begins when [visible action / sound / realization].
Relation: camera stays [distance / angle / side] relative to [subject].
Texture: [locked / smooth dolly / subtle handheld / slow pan / optical zoom].
Purpose: reveal / withhold / follow / intensify / recontextualize [specific information].
Review: check [frame stability / subject relation / end reveal / no random drift].
```

## Lens Distance / Perspective Prompt Card

Use this when a prompt asks for wide angle, telephoto, portrait lens, close-up, background compression, face distortion, large-format feel, zoom, dolly, surveillance view, companion camera, or "cinematic lens." Do not write lens number alone; pair lens class with camera distance, subject size, and background relation.

```text
lens_distance_id:
platform / mode:
shot context:

lens-distance contract:
  focal-length class / angle of view:
  camera-subject distance:
  subject size in frame:
  camera height / angle:
  background distance and scale:
  foreground relation:
  face / body rendering intent:
  depth of field / focus relation:
  motion toward / away from camera:
  zoom or physical movement boundary:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Lens Distance / Perspective Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| wide-close | "controlled wide-angle close camera, face near but not edge-warped; background recedes visibly" | intimacy, movement energy, companion camera | Do not push too close if facial distortion is unwanted | foreground feels near; background expands/recedes |
| long-far | "long-lens camera from far back; same head size; background appears closer behind subject" | isolation, surveillance, crowd/background pressure | Do not claim lens alone causes compression | camera feels physically distant; background scale presses in |
| natural close-up zone | "medium telephoto portrait distance; facial planes remain natural; ears/nose not exaggerated" | interviews, confession, restrained dialogue | Do not use one portrait rule for every face/story | close-up preserves intended face shape |
| environmental close-up | "moderate wide close-up keeps room edges readable around the face" | character tied to place | Do not sacrifice face readability for too much background | face and key environment both register |
| background pressure | "distant city lights appear stacked close behind the character" | social pressure, surveillance, compression | Do not flatten action geography when distance matters | background feels near without hiding subject |
| motion exaggeration | "wide lens near runner makes forward movement feel fast; keep face away from frame edge" | chase, comedy, subjective rush | Do not use for delicate portrait unless intended | motion toward camera expands rapidly |
| optical zoom | "slow optical zoom isolates the envelope; camera position stays fixed" | attention/search/surveillance | Do not call it dolly if viewpoint should not move | subject size changes without parallax shift |
| physical dolly | "camera physically moves closer; background parallax changes subtly" | pressure, approach, revelation | Do not use zoom if story needs bodily approach | viewer feels spatial approach |

### Lens Distance Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| face looks warped | camera too close or wide-close boundary absent | add portrait distance, avoid edge placement, preserve facial planes |
| background not compressed | camera distance/background relation absent | state long lens from far back and background close behind subject |
| shot feels generic | lens class lacks function | name social distance, background pressure, intimacy, surveillance, or motion energy |
| zoom feels like dolly or vice versa | zoom/dolly boundary absent | specify fixed camera optical zoom or physical camera move with parallax |
| action geography flattened | long-far used where contact/distance matters | switch to medium-wide proof or state spatial gap must stay readable |
| wide action becomes caricature | wide-close uncontrolled | keep subject center, avoid edge warp, limit face proximity |
| large-format wording does nothing | format relation absent | describe wide view with shallow separation or background scale relation instead of format label |

### Minimum Lens-Distance Prompt

```text
8-second restrained confession shot. Lens-distance contract: medium-telephoto portrait feel from a respectful camera distance, tight close-up from chest to head.
Face rendering: facial planes remain natural; nose and ears are not exaggerated or flattened.
Background relation: distant office lights appear softly compressed behind the character, but the doorway at frame-right remains readable.
Camera: locked-off, eye-level, no push-in; the sense is quiet observation, not invasive proximity.
Depth/focus: shallow background separation, both eyes sharp, background readable only as pressure.
Negative/lock: no wide-angle face warp, no fisheye edges, no random zoom, no extreme background blur that erases the doorway, no surveillance distance.
Review: face shape, camera distance feeling, close-up size, background scale, doorway readability, and no optical/physical movement drift are visible.
```

## Lighting And Material Prompt Card

Use this when a prompt asks for cinematic lighting, realistic material, premium texture, low-key/high-key look, motivated light, rim light, hard/soft light, warm/cool contrast, neon/practical color, or non-plastic surfaces. Light must have a source and material response; otherwise it becomes generic mood.

```text
lighting_id:
platform / mode:
shot context:

lighting contract:
  visible or implied source:
  hidden extension source:
  key direction:
  light quality:
  fill / negative fill:
  rim / separation:
  color temperature relation:
  local color pool:
  material response:
  exposure / contrast boundary:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Lighting And Material Prompt Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| motivated practical | "warm table lamp motivates the key from frame-left; hidden soft extension follows same direction" | interiors, night rooms, believable stylization | Do not add random glow with no source | visible source direction matches face highlights |
| hard light | "small hard side light creates crisp cheek and wall shadows" | noir, texture, graphic shadow, product edge | Hard is not automatically cheap or harsh | shadow edge is crisp and readable |
| soft light | "large diffused window key wraps the face with soft shadow falloff" | portraits, tenderness, beauty, overcast realism | Soft is not automatically premium | shadow edge is broad; face has gentle wrap |
| negative fill | "shadow side held dark with no bounce, preserving contrast" | sculpting face, low-key drama, separation | Do not crush all expression | dark side retains controlled detail |
| rim / back edge | "thin cool rim separates dark hair from black background" | separation, silhouette, night, smoke/haze | Do not make rim brighter than story logic | edge line separates subject cleanly |
| warm/cool relation | "amber practical pool against cool blue window spill" | mixed-source interiors, emotional contrast | Do not assign universal emotion to color | warm and cool zones stay distinct |
| local color pool | "red neon affects only the wet pavement and lower wall" | city nights, bars, sci-fi, clues, mood zones | Do not flood the whole frame with one hue | color stays localized to named surfaces |
| material response | "brushed steel catches narrow hard highlights; wet leather shows soft specular streaks" | realism, products, costumes, armor, props | Do not write only 'realistic texture' | material reacts differently to the same light |
| pipeline/matching note | "preserve warm/cool contrast across the sequence" | multi-shot continuity, grading, AI retries | ACES is not a look word | color relation remains consistent between shots |

### Lighting Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| Flat image | no separation method | add rim, negative fill, brightness contrast, or background falloff |
| Random cinematic glow | source motivation absent | name visible source and hidden extension direction |
| Plastic-looking material | material response absent | name surface, highlight shape, roughness, scratches, wetness, or fabric weave |
| Color washes whole frame | local color pool not bounded | assign color to one source and one surface zone |
| Face unreadable | fill/exposure boundary missing | add controlled eye fill or preserve shadow detail |
| Mixed color feels accidental | color temperature relation absent | name warm source versus cool source and their zones |
| Rim light looks fake | separation not motivated | tie rim to window, streetlight, moon, screen, or practical edge |
| Shot-to-shot color drifts | pipeline/matching note absent | preserve same source relation, color pool, and reference still |

### Minimum Lighting / Material Prompt

```text
Lighting: [visible/implied source] motivates [key direction].
Quality: [hard / soft / diffused / crisp] with [shadow behavior].
Separation: [rim / negative fill / background falloff / haze] separates [subject] from [background].
Color: [warm/cool/local color pool] belongs to [source and surface zone].
Material: [surface] responds with [highlight/scatter/reflection/texture].
Review: check [source direction / shadow edge / color zone / material highlight / separation].
```

## Source-Zone-Material Lighting Prompt Card

Use this when a prompt asks for a rich color/lighting look but risks becoming a full-frame color filter, random glow, plastic surface, or unmotivated rim light. Each light should name its source, affected zone, material response, and separation job.

```text
lighting_zone_id:
platform / mode:
clip duration:
shot context:

source-zone-material contract:
  primary motivated source:
  hidden extension / bounce:
  source direction:
  shadow edge / softness:
  affected zone:
  excluded zones:
  color temperature relation:
  local color pool boundary:
  separation method:
  material response by surface:
    skin:
    metal / glass / wet surface:
    fabric / hair / dust / smoke:
  exposure / clipping boundary:
  sequence matching note:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Source-Zone-Material Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| motivated source chain | "visible amber table lamp motivates left-side key; hidden soft extension follows same angle" | light must feel believable but exposed enough | Do not name a practical that does not affect the subject | highlights and shadows point back to the source |
| affected zone | "amber pool touches only the table surface, hands, and lower left wall" | color should be local, not global | Do not flood the whole frame with the color | color remains in named zone |
| excluded zone | "background hallway remains cool and desaturated" | avoiding full-frame tint or muddy color | Do not make every plane equally saturated | unlit/cool zone stays visually distinct |
| shadow edge check | "hard slatted window light creates crisp bars on wall; face has softer bounce" | hard/soft relation must be inspectable | Do not say "dramatic light" without shadow behavior | shadow edge shows hard/soft quality |
| separation method | "dark coat separates from black wall through a thin cool window rim and faint haze" | subject blends into background | Do not add fake glow without source | subject/background edges are readable |
| material response split | "skin keeps soft diffuse falloff; wet leather forms streaky highlights; brushed steel catches narrow bright edges" | surfaces look plastic or samey | Do not write only "realistic texture" | surfaces react differently to the same light |
| clipping boundary | "neon sign remains saturated but not clipped; face keeps shadow detail" | bright practical/neon/fire/screen appears | Do not protect all highlights if glare is the story | key detail is readable; source can bloom only locally |
| match note | "carry the same amber-left / cool-right relation into the next shot" | multi-shot continuity matters | ACES/pipeline words are not a style | source relation survives shot handoff |

### Lighting / Color Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| whole frame becomes orange/blue | color pool boundary absent | name affected zone and excluded zone |
| image glows but light feels fake | motivated source chain absent | name visible source plus hidden extension in same direction |
| hard/soft instruction ignored | shadow edge not specified | describe crisp shadow, soft wrap, diffusion, or bounce behavior |
| subject blends into background | separation method absent | add rim, negative fill, hue/luminance contrast, haze, or background falloff |
| all materials look plastic | material response gate absent | split skin, metal/glass/wet surface, fabric/hair/dust responses |
| neon or fire clips detail | exposure boundary absent | protect face/shadow detail; allow bloom only around source |
| shots do not match | sequence relation absent | preserve same source direction, color relation, and material response |

### Minimum Source-Zone-Material Prompt

```text
8-second night-interior shot. Visible amber table lamp at frame-left motivates a soft left-side key; a hidden larger soft source follows the same lamp direction.
Cool moonlit window spill stays in the background hallway and creates a thin blue rim on the dark coat.
Color pool boundary: amber affects only the tabletop, hands, and lower left wall; the background hallway remains cool and desaturated.
Shadow behavior: soft facial falloff from the lamp side; crisp window-frame edge only on the back wall.
Material response: skin has soft diffuse falloff, wet leather gloves show streaky highlights, brushed metal badge catches one narrow hard edge, dust in the rim light is faint.
Exposure: lamp may bloom slightly, but face shadow detail and badge edge remain readable.
Negative/lock: no full-frame orange/blue wash, no random glow, no plastic skin, no unmotivated rim, no clipped neon-like lamp.
Review: source direction, affected color zone, excluded cool zone, shadow edge, subject separation, and distinct material responses are visible.
```

## Lighting / Color Transition Prompt Card

Use this when a shot needs light, color, exposure, or material response to change over time. The change should be motivated by a source, blocking event, practical dim, doorway/screen/window reveal, or story beat; otherwise it becomes a generic filter shift.

```text
lighting_transition_id:
platform / mode:
clip duration:
visual premise:

lighting transition contract:
  before-state:
  trigger:
  source change:
  affected zone:
  excluded zone:
  color / temperature relation:
  exposure / contrast / shadow edge:
  material response over time:
  subject / background separation:
  after-state / story consequence:
  matching note for retries:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Lighting / Color Transition Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| source reveal | "at 3s, an offscreen elevator door opens frame-right and cool hallway spill enters only the right wall and file-cabinet edge" | a new source changes the emotional state | Do not make the whole image turn blue | trigger, source direction, and affected zone are visible |
| practical dim / rise | "the desk lamp slowly fades, leaving the envelope readable but the far wall falling into shadow" | power loss, intimacy, threat, decision beat | Do not random-flicker unless flicker is the story event | exposure change has a source and smooth timing |
| local color-pool shift | "red warning light starts touching only the door seam and the character's knuckles" | alarm, clue, threshold, danger cue | Do not flood skin and background with the same saturation | color belongs to named source/surfaces |
| exposure / shadow ramp | "as the blinds close, crisp shadow bars narrow across the wall while eyes keep a thin fill" | pressure, concealment, isolation, time passing | Do not crush important performance detail | shadow edge/range changes without losing key information |
| material response transition | "wet coat remains dark until cool rim catches the shoulder beads after the door opens" | texture must prove the lighting change | Do not write only 'more cinematic texture' | surface response changes after the trigger |
| separation transition | "before 4s the dark coat blends into the wall; after the cool rim arrives, hair and shoulder separate" | reveal, recognition, silhouette readability | Do not add unmotivated outline glow | separation improves from the named source |

### Lighting / Color Transition Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| whole clip becomes tinted | affected/excluded zones missing | name the source, touched surfaces, and surfaces that stay unchanged |
| random exposure flicker | trigger and ramp missing | bind change to a door, lamp dim, screen flash, passing vehicle, or blocking cue |
| color shift has no story value | after-state missing | state what the viewer learns or what spatial/emotional relation changes |
| material still looks flat | material response transition missing | name one surface that begins catching, scattering, reflecting, or losing light |
| subject disappears | separation/exposure boundary missing | preserve eye fill, edge rim, background falloff, or silhouette contrast |

### Minimum Lighting / Color Transition Prompt

```text
8-second single shot. Before-state: a warm desk lamp shapes the character's hands and the sealed envelope; background hallway stays cool and dim.
At 3s, the elevator door opens offscreen frame-right; cool blue hallway spill enters only the right wall and the metal filing-cabinet edge.
The warm lamp remains on the hands and envelope; red stamp gains a faint cooler edge, wet coat shoulder beads begin catching the new rim, and the face keeps shadow detail.
After-state: the room feels exposed because the background route is now visible, while the private desk area remains warm.
Negative/lock: no full-frame blue wash, no random flicker, no unmotivated neon, no plastic skin, no losing the envelope or eyes.
Review: before-state, trigger, source direction, affected/excluded zones, material response, separation change, and story consequence are visible.
```

## Action Contact Proof Prompt Card

Use this when a prompt asks for a fight beat, hit, block, fall, shove, tackle, weapon clash, explosion push, creature impact, vehicle bump, or any action where force must read. The prompt should prove causality without becoming real-world stunt instruction.

```text
action_id:
platform / mode:
clip duration:
safety / fiction boundary:

action contract:
  setup / stance:
  attacker motion:
  receiving zone:
  contact or near-miss relation:
  receiver response:
  environmental proof:
  recovery / changed state:
  camera rule:
  sound / impact cue, if supported:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Action Contact Proof Prompt Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| setup / wind-up | "fighter plants rear foot and raises guard before the strike" | impact needs weight, anticipation, or timing | Do not over-describe every joint | action begins before the hit |
| attack vector | "forearm travels from screen-left toward the shield edge" | the path of force must be readable | Avoid tactical harm detail or real training advice | limb, weapon, or body travels along a named path |
| receiving zone | "shield edge at chest height receives the strike" | contact otherwise looks like waving past | Keep zones fictional/screen-safe; avoid vulnerable real-world targets | receiver or object is in the path |
| contact / near-miss relation | "strike overlaps the shield edge for one beat" or "blade misses by inches past the shoulder" | hit, block, dodge, graze, bind, or jam must read | Do not require unsafe real contact | frame shows the relationship, not a teleport |
| receiver response | "shield carrier recoils two steps and drops the front knee" | force needs proof on a body or object | Do not make reaction bigger than tone allows | response happens after the contact beat |
| environmental proof | "table cup spills after the recoil; dust jumps from the wall" | AI action feels floaty or consequence-free | Do not add particles that hide the contact | prop/surface state changes after impact |
| recovery / cost | "attacker resets stance and exhales before the next move" | action needs weight, pain, fatigue, or rhythm | Do not loop endless attacks without changed state | no weightless looping; body pays or resets |
| camera rule | "medium-wide single shot keeps attacker, receiver, and receiving zone visible" | contact credibility matters | Do not hide every beat with shake or cuts | attack and response share one spatial contract |

### Action Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| punch looks fake | receiver response or contact relation missing | add receiving zone and delayed recoil after contact |
| action floats | setup, weight shift, or recovery missing | add stance, foot plant, rebound, breath, or reset |
| contact hidden by cuts | camera rule missing | use one continuous medium-wide shot for the proof beat |
| opponent teleports or drifts | spatial contract missing | keep both bodies visible, same screen direction, named distance |
| weapon or object has no weight | object inertia/environment response missing | add drag, rebound, surface mark, vibration, or prop displacement |
| too many moves blur together | prompt overload | reduce to one attack, one response, one changed state |

### Minimum Action Contact Prompt

```text
Action: [one attack/move] begins from [visible setup] and travels [direction/path].
Contact proof: [contact/near-miss relation] at [receiving zone], then [receiver/object] reacts after the beat.
Environment proof: [surface/prop] changes state: [slide/dent/splash/dust].
Camera: [medium-wide / locked / tracking] keeps [attacker, receiver, receiving zone] visible.
Recovery: [attacker/receiver] shows [recoil/breath/reset/stumble].
Review: check [setup -> contact relation -> receiver response -> environment proof -> recovery].
Safety: fictional screen choreography only; no real execution instructions.
```

## Mass / Speed / Recovery Prompt Card

Use this when an action looks soft, floaty, weightless, too uniformly fast, too slow everywhere, or physically disconnected. It is especially useful for heavy weapons, armor, creature impacts, superhuman dashes, vehicle/robot motion, large props, and stylized action beats.

```text
mass_rhythm_id:
platform / mode:
clip duration:
safety / fiction boundary:

physical timing profile:
  actor / mover mass class:
  object / weapon mass distribution:
  support / traction:
  preload / anticipation:
  acceleration:
  peak / contact / closest pass:
  receiver or environment response:
  follow-through:
  braking:
  recovery / changed state:
  camera responsibility:
  sound / material cue:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Mass And Speed Prompt Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| preload / anticipation | "he lowers his stance and lets the hammer head lag behind his shoulder" | action needs readable force source | Do not freeze into empty posing | body/weapon loads before acceleration |
| acceleration spike | "after the load, the hammer commits in one sudden downward arc" | force should feel powerful, not uniformly slow | Do not make everything high speed | speed changes sharply after setup |
| mass distribution | "tip-heavy blade pulls the arms through the follow-through" | weapon/prop feels weightless | Do not turn this into real weapon instruction | heavy end lags, overtakes, then drags |
| receiver / environment response | "floor dust jumps and the shield carrier slides half a step" | weight needs external proof | Do not cover the action with debris | response happens after peak |
| follow-through | "the swing continues past the target and pulls his torso forward" | impact stops too cleanly | Do not loop into another attack instantly | momentum continues beyond peak |
| braking | "rear foot skids, then plants to stop the remaining momentum" | movement needs controlled stop | Do not overextend into unsafe stunt detail | body visibly resolves force |
| recovery / changed state | "he exhales and resets the hammer to guard height" | action needs consequence and rhythm | Do not end on a frozen hero pose unless it proves state | new stable state is visible |
| sound/material proof | "low metal thud, short silence, then chain rattle settles" | weight needs audio support | Sound cannot replace visible causality | cue syncs with peak and tail |

### Mass / Rhythm Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| action feels weightless | preload, inertia, or braking missing | add support, lag, overshoot, foot plant, and recovery |
| movement is fast but not powerful | speed contrast absent | add slow load -> short acceleration spike -> delayed consequence |
| heavy object moves like a stick | mass distribution absent | state grip-biased, balanced, tip-heavy, head-heavy, or flexible-delayed behavior |
| impact lands but has no cost | receiver/environment response missing | add recoil, slide, vibration, dust, dent, cloth snap, or breath reset |
| slow motion feels fake | causality hidden by style | keep normal-speed preload/contact, then use brief slow-motion only around the peak if needed |
| camera shake hides force | camera responsibility missing | hold readable setup/peak; allow micro shake only at impact; stabilize for recovery |
| combo becomes mushy | too many peaks | reduce to one dominant peak or give each beat a distinct preload, target, response, and recovery |

### Minimum Mass-Aware Action Prompt

```text
5-second fictional screen-action beat. A heavy, head-loaded hammer is held in both hands.
0-1s: fighter lowers stance, rear foot plants, hammer head lags behind the shoulder.
1-2.8s: sudden committed downward arc; the heavy head overtakes the hands.
2.8s: hammer strikes a metal shield edge; brief low thud and tiny camera jolt.
2.8-4s: shield carrier slides half a step; dust jumps from the floor; hammer continues past the shield and pulls the fighter's torso forward.
4-5s: rear foot skids then plants; fighter exhales and resets guard.
Negative/lock: no constant high speed, no weightless spinning, no hidden contact, no endless combo, no camera shake covering the peak.
Review: preload, acceleration spike, contact, receiver/environment response, follow-through, braking, and recovery are all visible.
```

## Action Camera Responsibility Prompt Card

Use this when the action is meant to feel kinetic but still readable. The camera should have one proof job per beat. If the camera's movement, shake, lens, crop, or foreground obstruction does not reveal force, geography, contact, or consequence, it is just decoration.

```text
action_camera_id:
platform / mode:
clip duration:
safety / fiction boundary:

camera responsibility contract:
  action proof needed:
  camera job:
  start frame:
  subject relation:
  camera speed versus action:
  proof frame / stabilization point:
  allowed shake / blur:
  foreground / obstruction use:
  end frame / consequence view:
  sound or light cue that helps readability:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Action Camera Responsibility Table

| Camera job | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| wide proof | "medium-wide frame keeps both bodies, receiving zone, and exit path visible" | contact/geography must be credible | Do not use a wide shot if the decisive detail is too small | viewer sees setup, path, contact, response |
| initiator follow | "camera tracks behind the attacker until the weapon enters the contact plane" | action path or chase momentum matters | Do not let camera outrun the subject | attacker/action vector remains readable |
| contact stabilize | "camera reduces motion for the contact beat, then releases into recoil" | impact is the proof | Do not shake hardest exactly when contact happens | contact/near-miss relation is visible |
| receiver relay | "after contact, camera follows the shield carrier's recoil two steps" | force needs consequence | Do not stay only on the attacker after impact | receiver response and changed spacing register |
| foreground rupture | "weapon crosses foreground for one instant, then clears to reveal the hit" | speed peak or screen-breaking energy | Do not keep foreground coverage over the proof beat | obstruction is brief; proof appears after it |
| handheld proximity | "controlled shoulder-height handheld, small human instability, action remains centered" | bodily urgency or documentary texture | Do not use handheld as generic seriousness | shake does not hide limbs, faces, or geography |
| low tracking | "low side tracking keeps feet, ground contact, and weapon arc in frame" | speed/traction/weight must read | Do not crop out support foot or receiver | support and path stay visible |
| strobe / flash proof | "brief flash freezes the peak silhouette; ambient fill preserves faces between flashes" | rain/strobe/impact style | Do not let flashes fragment the whole action | flash clarifies, not obscures, the peak |

### Action Camera Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| impact hidden by shake | shake budget missing | stable setup/contact, micro-shake at peak only, stabilize for recovery |
| camera feels energetic but action unreadable | camera job absent | assign one job: geography, initiator, contact, receiver, or consequence |
| close-up loses geography | start/end frame or spatial anchor missing | begin or end on medium-wide proof; keep receiving zone visible |
| foreground wipe replaces contact | obstruction boundary missing | allow foreground rupture for less than one beat, then clear to proof frame |
| camera outruns actor/weapon | subject relation missing | camera speed stays slightly below fastest action layer |
| handheld feels random | texture not bounded | controlled handheld, centered subject, no whip shake, no drift off action |
| action looks like disconnected fragments | information token missing | each shot/move must show path, target, contact, reaction, obstacle, or changed spacing |

### Minimum Action Camera Prompt

```text
8-second fictional action beat. Camera job: prove a shield impact without hiding contact.
0-2s medium-wide frame shows attacker left, shield carrier right, and clear floor gap between them.
2-4s camera tracks slightly behind the attacker, slower than the weapon arc, keeping the shield edge visible.
4s contact proof: camera stabilizes for one readable beat as the weapon overlaps the shield edge; tiny jolt only after contact.
4-6s camera relays to the shield carrier's recoil two steps backward; dust and strap vibration remain visible.
6-8s camera widens and steadies on the changed spacing and both recovered stances.
Negative/lock: no whip shake, no random close-ups, no foreground object covering contact, no cutting away at impact, no motion blur hiding limbs.
Review: geography, action path, contact proof, receiver recoil, environmental response, and recovered spacing are all visible.
```

## Fictional Danger / Safety-Bound Action Prompt Card

Use this when an AI video action beat should feel dangerous, tense, or high-stakes without becoming real-world stunt, weapon, injury, or harm instruction. Danger should be screen evidence: geography, near-miss, vulnerability, consequence, and recovery.

```text
danger_id:
platform / mode:
clip duration:
safety / fiction boundary:

fictional danger contract:
  fictional setup:
  viewer danger question:
  geography / escape relation:
  vulnerability cue:
  threat path, non-operational:
  near-miss or blocked-contact proof:
  receiver / object / environment consequence:
  recovery or changed state:
  camera proof job:
  sound / light / material cue:

constraints:
  preserve:
  avoid:

review checks:
  geography explains why it is dangerous:
  vulnerability cue is visible before the peak:
  near-miss / block / consequence is readable:
  recovery or changed state registers:
  no real-world execution detail:
  no gore / shock / shake hiding missing proof:
validation status:
```

### Fictional Danger Mechanism Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| geography danger | "locked exit behind her; low railing on screen-right; clear floor gap before the swing" | danger depends on limited routes | Do not turn this into trap-building instruction | viewer understands route, obstacle, and risk |
| vulnerability cue | "her front foot slips and her guard opens for half a second" | tension needs exposed state | Keep it visual and fictional; avoid tactical harm advice | exposed state appears before the danger peak |
| near-miss proof | "blade-like prop passes inches in front of the sleeve; sleeve snaps and papers lift" | threat should feel close without real contact | Do not specify real weapon technique or injury detail | object/cloth/environment reacts after the pass |
| blocked-contact proof | "shield catches the strike; strap vibrates; carrier recoils one step" | safer alternative to direct hit | Do not use vulnerable body targets as instruction | block, vibration, recoil, and recovery are visible |
| consequence proof | "lamp swings, dust drops, and the character exhales into a reset stance" | danger otherwise feels weightless | Do not add debris that hides the proof beat | environment changes after the peak |
| safety boundary | "fictional screen choreography only; no real stunt execution details" | action could be read as instruction | Real shoots require qualified stunt coordination | prompt remains outcome-focused, not how-to |

### Minimum Fictional Danger Prompt

```text
8-second fictional screen-action beat, not real stunt instruction.
Setup: a courier backs through a narrow archive aisle; exit visible behind her, metal shelf on screen-left, low railing on screen-right.
0-2s geography danger: she glances at the blocked exit and her front foot slips on loose papers.
2-4s non-operational threat path: a long prop swings through frame from screen-left toward the shelf line.
4s near-miss proof: the prop passes inches in front of her sleeve; papers lift and the shelf tag snaps loose.
4-6s consequence: she recoils into the shelf, breath stops, lamp flickers, and dust falls.
6-8s recovery: she regrips the folder and resets with the exit now blocked.
Camera: medium-wide, stable for the near-miss, tiny jolt only after the shelf impact.
Negative/lock: no gore, no injury detail, no real weapon/stunt technique, no how-to choreography, no shaky blur hiding the near-miss, no extra attackers.
Review: geography, vulnerability, near-miss relation, sleeve/paper/shelf consequence, recovery, and safety boundary are all visible.
```

## Editing Rhythm / Time Anchor Prompt Card

Use this when a prompt asks for fast pacing, slow pacing, punchy editing, music sync, montage, trailer rhythm, action rhythm, pauses, reaction shots, J/L-cut-like audio lead/tail, or "cinematic timing." Rhythm should be written as timed events, not as a taste adjective.

```text
rhythm_id:
platform / mode:
clip duration:
one dominant event:

rhythm contract:
  rhythm source:
  beat timeline:
    0-2s:
    2-4s:
    4-6s:
    6-8s:
    8-10s:
  beat anchors:
    performance pulse:
    action hinge:
    camera movement trigger / stop:
    sound or music cue:
    reaction breath:
    story-state change:
  cut / transition rule, if multi-shot:
  density curve:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Time Anchor Prompt Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| performance pulse | "cut or hold on the actor's breath pause, not on every music beat" | dialogue, suspense, close reaction, performance-led scenes | Do not force actors into mechanical timing | visible breath, glance, hand stop, or hesitation drives the beat |
| action hinge | "cut on the reach-to-grip moment, then hold the completed grip" | entrances, object handling, fights, chases | Do not cut every motion into fragments | action starts before the cut and resolves after it |
| sound prelap / lead | "hear the train brake half a second before the platform image" | anticipation, dread, entering a new space | Do not use audio lead without a source or story job | audio begins before image and creates expectation |
| sound tail / carryover | "keep the previous line over the next silent face for one beat" | emotional residue, memory, irony, transition flow | Do not carry sound as wallpaper | previous sound changes the new image's meaning |
| music accent | "door slam lands on the downbeat; the reaction holds off the next beat" | music videos, trailers, dance/action sync | Do not put every cut exactly on beat | key event aligns with accent, but recovery is still readable |
| impact punctuation | "contact, transient hit, half-second silence, then recoil sound tail" | action, horror, comedy hits, reveals | Do not replace visible causality with sound only | impact has contact, accent, pause/tail, and changed state |
| reaction breath | "hold 0.5-1s after the reveal before the next move" | information must register | Do not add pauses that do not change knowledge or emotion | viewer can see the reaction after the cue |
| density ramp | "start sparse, add one sound/motion layer every two seconds, then cut to quiet" | tension build, countdown, montage | Do not pile layers that hide the main event | layers increase or collapse according to the stated curve |
| event budget | "one setup, one trigger, one reaction, one changed state" | 5-10 second AI clips | Do not ask for a full sequence in one short generation | all requested beats are inspectable |

### Rhythm Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| fast but confusing | no viewer-comprehension beat | add setup frame and reaction breath before the next event |
| slow but empty | no state change or density curve | assign a cue at each time window and name what changes |
| cut feels random | beat anchor missing | tie timing to breath, glance, impact, camera stop, sound cue, or reveal |
| music sync feels hollow | beat not tied to action/story | bind one accent to a visible action hinge or reveal |
| impact has no weight | punctuation lacks pause/tail | add contact -> hit transient -> half-second silence/tail -> recoil |
| audio and image desync | cue sheet missing | write second ranges and visible reaction after the sound |
| prompt overload | too many timed events | reduce to one dominant event and 3-5 beats |

### Minimum Rhythm / Timing Prompt

```text
Duration: [5-10s], one continuous shot or [number] cuts only.
Rhythm source: [performance breath / action hinge / sound cue / music accent / camera stop].
Timeline:
  [0-2s]: [setup or anticipation].
  [2-4s]: [trigger: action/sound/camera cue].
  [4-6s]: [reaction breath or consequence].
  [6-8s]: [changed state / final hold].
Cut rule: cut or camera change only on [named beat anchor].
Negative / positive lock: no random fast cutting; no extra events; preserve the reaction hold.
Review: check [setup -> trigger -> reaction breath -> changed state -> no overload].
```

## Dialogue Timing / Cut Permission Prompt Card

Use this when a dialogue scene needs restrained pace, reaction holds, J/L-cut-like sound lead or tail, pause value, or a clear reason to cut. The timing should come from performance, sound, gaze, object handling, or changed relation rather than a vague instruction like "slow cinematic pacing."

```text
dialogue_timing_id:
platform / mode:
clip duration:
shot count limit:
one dialogue event:

dialogue timing contract:
  spoken line / cue:
  reaction owner:
  reaction starts:
  reaction breath window:
  cut / hold permission:
  sound lead / tail:
  silence action:
  object / space pressure:
  final changed relation:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Dialogue Timing / Cut Permission Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| reaction-before-line | "listener's fingers stop before the speaker finishes the sentence" | the listener already understands or anticipates | Do not make reaction random or psychic | reaction begins after a visible/audible cue within the line |
| reaction-after-line | "hold 1s after the line before the listener answers with a look" | meaning lands after impact | Do not add empty delay with no decision | pause reveals decision, refusal, fear, or concealment |
| line tail carryover | "speaker's last word continues over listener's silent face for one beat" | the line contaminates the reaction | Do not carry dialogue as wallpaper | tail changes how the listener/object/space is read |
| sound prelap pressure | "phone buzz begins half a second before the listener looks down" | cue should pull attention or authorize cut | Do not prelap without source or answer | sound leads image and image answers it |
| cut on micro-behavior | "cut only when the hand stops on the envelope" | cut needs a physical permission point | Do not cut on arbitrary schedule | hand/eye/breath/object beat is visible before cut |
| hold instead of cut | "stay on listener through the silence; no reverse cut until breath resumes" | reaction owns the meaning | Do not hold if the shot has no changing evidence | viewer sees the reaction evolve during the hold |
| pause density | "room tone drops, then breath and folder paper remain" | silence must feel active | Do not write mute as absence | one remaining cue proves the pause is intentional |

### Dialogue Timing Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| slow but empty | silence action absent | state what the pause does: decide, refuse, hide, measure, absorb, lie |
| random cutaway | cut permission absent | allow cut only on breath stop, eye lift, hand stop, sound cue, or object reveal |
| reaction buried by line | reaction owner/timing absent | place reaction before line end, after line, or after a named silence |
| audio lead feels accidental | source/answer absent | name the prelap source and the visual response it triggers |
| too many beats | event budget absent | keep one line/cue, one listener, one reaction breath, one changed relation |
| melodramatic pause | micro-behavior absent | replace big acting with hand stop, breath hold, eye drop, folder grip, or delayed blink |

### Minimum Dialogue Timing Prompt

```text
8-second restrained table dialogue, maximum one cut.
0-2s: locked two-shot; table edge and sealed folder visible.
2-3s: speaker says one short line: "You already opened it."
Reaction owner: listener. Her fingers stop on the folder before the last word ends.
3-5s: hold on listener for a 1.5s reaction breath; she does not answer, looks from folder to exit, and lowers her breathing.
Cut permission: cut only after her breath stops, or keep the full beat as one continuous shot.
Sound tail: the last word and room tone carry over the silent face for one beat; no score.
After-state: the folder remains on her side, but control shifts to the speaker because she has revealed knowledge.
Negative/lock: no extra dialogue, no random reverse cut, no theatrical pause, no eye drift, no music swell, no camera move hiding hands or folder.
Review: line/cue order, reaction owner, breath window, cut/hold permission, sound tail, micro-behavior, and changed relation are visible/audible.
```

## Beat Anchor / Cut Permission Prompt Card

Use this when a short AI video prompt asks for fast pacing, montage, music sync, punchy cuts, slow tension, or "dynamic editing." Each cut, hold, camera change, speed change, or sound accent should have permission from a visible or audible beat. If no beat gives permission, keep the shot continuous.

```text
beat_anchor_id:
platform / mode:
clip duration:
shot count limit:
one dominant event:

beat anchor contract:
  setup frame:
  primary rhythm source:
  cut / hold permission rule:
  beat timeline:
    0-2s:
    2-4s:
    4-6s:
    6-8s:
  viewer registration hold:
  density curve:
  sound / music relationship:
  camera change rule:
  final state:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Beat Anchor / Cut Permission Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| performance permission | "hold until the actor's breath stops, then cut" | dialogue, reaction, suspense | Do not cut on schedule if performance has not turned | breath/glance/hand stop clearly authorizes timing |
| action hinge permission | "cut only as the hand closes on the handle; next shot begins with grip completed" | object handling, entrances, action beats | Do not fragment movement before cause is readable | action begins before cut and resolves after |
| sound permission | "phone buzz starts half a second before the look; cut after the look lands" | cue-driven attention | Do not lead sound without source/consequence | sound cue creates expectation and image answers it |
| music permission | "one door slam lands on the downbeat; recovery hold ignores the next beat" | music sync, trailers, dance/action | Do not cut every beat equally | accent marks a story/action change |
| viewer registration hold | "hold 0.7s after reveal before the next move" | information must be understood | Do not add empty slow prestige pause | viewer can read new information/reaction |
| density curve budget | "0-2s sparse, 2-5s rising layers, 5-6s peak, 6-8s quiet consequence" | tension build, montage, countdown | Do not change camera, action, sound, and location at once | layer changes follow stated curve |
| camera-change permission | "camera push begins only after the envelope is noticed" | movement should follow attention | Do not move camera while the key action is still unclear | camera change reveals or intensifies one thing |
| final-state permission | "last beat holds on changed spacing / hidden object / decision" | clip needs consequence | Do not end on unresolved motion unless intended | final frame proves what changed |

### Beat Anchor Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| fast but unreadable | viewer registration hold missing | add 0.5-1s hold after cue, reveal, impact, or reaction |
| cuts feel random | cut permission rule absent | allow cuts only on breath, glance, grip, impact, sound cue, reveal, or camera stop |
| music sync feels empty | music accent not tied to story/action | bind one accent to a visible hinge and preserve recovery |
| slow beat feels dead | final state or density curve absent | name what changes during the hold or what sound/motion layer thins |
| montage becomes noise | density curve budget missing | reduce simultaneous changes; keep one dominant track per time window |
| action continuity breaks | action hinge split unclear | write outgoing phase and incoming completed phase |
| camera fights timing | camera change rule absent | begin camera move only after the cue that motivates it |

### Minimum Beat Anchor Prompt

```text
8-second AI video, maximum two cuts, one dominant event: a hidden message is discovered.
0-2s setup: locked medium shot; character sorts papers; low room tone.
2-4s trigger: phone buzz begins at 2.5s; character's hand stops on a folded note.
Cut permission: first cut only when the hand fully stops on the note, not before.
4-6s reveal: tighter shot of the note opening; hold 0.7s after the red mark appears.
6-8s consequence: cut back to face only after the reveal hold; breath stops, eyes lift toward the door; final frame holds the changed decision.
Density curve: sparse setup -> one sound cue -> visual reveal -> quiet reaction; no extra locations or new events.
Negative/lock: no random fast cutting, no cutting on every music beat, no montage fragments, no camera move during the reveal, no extra plot event.
Review: setup, trigger, authorized cut, reveal hold, reaction breath, final changed state, and no overload are visible/audible.
```

## Dialogue Reaction Prompt Card

Use this when a prompt asks for dialogue, subtext, restrained acting, reaction shots, silence, eye contact, shot/reverse-shot, table scenes, car dialogue, corridor dialogue, interrogation, confession, negotiation, or "naturalistic performance." Write the visible pressure, not just the line.

```text
dialogue_id:
platform / mode:
clip duration:
one-sentence scene:

dialogue contract:
  character A want:
  character B resistance:
  forbidden truth / hidden pressure:
  spoken line or sound cue, if supported:
  surface behavior:
  gaze rule:
  reaction owner:
  silence action:
  blocking / prop change:
  coverage rule:
  state change:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Dialogue Reaction Prompt Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| want under pressure | "she wants the envelope back but cannot ask directly" | scene needs subtext or negotiation | Do not make every line cryptic | behavior shows a goal under constraint |
| resistance | "he answers by sliding the cup between them, not by explaining" | conflict would become exposition | Resistance is not random hostility | the other person blocks, delays, or reframes |
| surface behavior | "polite smile while fingers tighten on the folder" | hidden pressure needs visible proof | Do not rely on abstract emotion labels | body/prop behavior contradicts or leaks meaning |
| gaze rule | "no direct eye contact until the final withheld name" | tension depends on avoidance or power | Do not let eyes drift randomly | gaze pattern stays stable and changes only at the named beat |
| listener ownership | "hold on listener after the line; speaker continues offscreen" | reaction changes meaning more than the line | Do not add reaction shots as filler | listener response reframes or absorbs the line |
| silence action | "three-second pause as she decides to lie" | pause must carry thought or choice | Silence is not empty mute space | pause produces a visible decision or state change |
| blocking change | "he rises after the accusation; she remains seated" | status changes inside a static room | Do not add movement only to avoid boredom | position change alters power, access, or distance |
| coverage rule | "start in two-shot; cut to listener only after the forbidden word" | shot/reverse-shot needs purpose | Do not cut mechanically on every line | coverage changes with stakes or ownership |
| constrained space | "table edge remains a barrier; neither crosses it" | room, car, table, doorway, corridor pressure matters | Do not stack too many spatial metaphors | barrier or exit condition affects behavior |

### Dialogue Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| actors over-explain | want/resistance not separated from lines | state what each person wants and what cannot be said |
| flat talking heads | blocking, gaze, or prop behavior missing | add one spatial rule and one physical tell |
| reaction shot feels like padding | listener ownership absent | specify what the listener learns, hides, or decides |
| silence feels empty | silence action absent | write "pause to decide / refuse / measure / absorb / lie" |
| eye contact drifts randomly | gaze rule missing | lock direct/avoided/offscreen/mirror gaze and one change beat |
| melodramatic acting | performance control too abstract | use restrained physical behavior and small visible changes |
| prompt overload | too much dialogue or too many turns | reduce to one line/cue, one reaction, one state change |

### Minimum Dialogue Reaction Prompt

```text
Duration: [5-10s], one dominant dialogue beat.
Pressure: [A wants X] but [B blocks/delays/reframes].
Hidden truth: [what cannot be said directly].
Line/cue: [one short line or offscreen/audio cue, if supported].
Performance: [surface behavior] reveals [hidden pressure].
Gaze: [direct / avoided / shared forward / mirror / offscreen] until [change beat].
Reaction owner: hold on [listener/speaker/object/empty space] for [reaction meaning].
Silence action: [withhold / decide / absorb / lie / refuse / leave].
Blocking: [distance/barrier/prop/seat/door] changes or stays fixed because [story reason].
Review: check [want -> resistance -> gaze rule -> reaction owner -> silence action -> state change].
Negative / positive lock: restrained performance; no speechifying; no random eye drift; no extra dialogue turns.
```

## Listener Reaction Ownership Prompt Card

Use this when the key meaning lands on the person hearing, watching, withholding, or deciding rather than on the speaker. The prompt should state what the reaction proves, when it begins, and which small visible behavior carries the thought.

```text
reaction_id:
platform / mode:
clip duration:
scene pressure:

reaction ownership contract:
  trigger line / cue:
  reaction owner:
  what the reaction proves:
  line-to-reaction timing:
  gaze rule before trigger:
  gaze answer after trigger:
  micro-behavior tell:
  silence action:
  coverage / camera rule:
  object / space that carries pressure:
  final state change:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Listener Reaction Ownership Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| delayed ownership | "hold on listener for two seconds after the line before any answer" | line matters because of what it causes | Do not add a dead pause with no visible change | listener visibly absorbs or reframes the line |
| pre-reaction | "listener's hand stops before the speaker finishes the sentence" | the receiver understands before others do | Do not make the reaction too large or early without context | micro-behavior starts before/at the cue |
| offscreen speaker | "speaker continues offscreen while camera stays on listener" | words are less important than reception | Do not lose source clarity | viewer knows who speaks and sees who changes |
| gaze answer | "listener avoids eye contact until the forbidden name, then looks directly back" | power, truth, or recognition turns on eye contact | Do not let eyes wander randomly | gaze changes once, at the named beat |
| micro-behavior tell | "fingers stop smoothing the envelope; breath holds; shoulders become still" | hidden pressure needs proof | Do not stack many subtle tells | one small behavior is readable and tied to cue |
| silence action | "three-second pause as he chooses to lie" | quiet beat must carry thought | Silence is not missing dialogue | pause ends in a decision, refusal, or state change |
| object reaction | "hold on the unopened envelope while both voices stop" | object carries the unsaid truth | Do not use cutaway as filler | object/prop relation changes meaning |
| camera restraint | "locked medium close-up; no cut until the hand releases the glass" | reaction needs performance focus | Do not overcut the reaction | camera lets the viewer inspect the tell |

### Listener Reaction Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| reaction looks like generic sadness | what the reaction proves missing | state the knowledge, decision, lie, refusal, or power shift |
| viewer cannot tell why the listener reacts | trigger line/cue missing or too long | use one short line/cue and keep source legible |
| pause feels empty | silence action missing | write the pause as deciding, withholding, measuring, absorbing, lying, or refusing |
| eyes drift or break continuity | gaze rule/answer absent | lock gaze before the cue and one change after the cue |
| acting becomes theatrical | micro-behavior too broad | use one small tell: breath, hand stop, blink delay, grip, posture stillness |
| cutaway feels like padding | ownership or object pressure absent | name what the listener/object changes for the viewer |
| AI adds extra dialogue | constraint budget missing | one cue, one reaction, one final state change; no extra dialogue turns |

### Minimum Listener Reaction Prompt

```text
8-second restrained dialogue beat, one continuous shot.
Scene pressure: she needs the envelope back but cannot ask directly; he already knows she is lying.
Trigger cue: at 3s she says one short line, "You kept it."
Reaction owner: camera stays on him, not her, because his response proves he understands the lie.
Timing: his fingers stop smoothing the envelope before she finishes the line; he waits two silent seconds before answering.
Gaze: he avoids eye contact until the word "kept," then looks directly at her once.
Micro-behavior: breath holds, hand stops, envelope edge bends slightly under his fingers.
Silence action: the pause is him choosing not to confess.
Blocking: table edge remains between them; envelope stays visible near his hand.
Negative/lock: restrained performance, no speechifying, no extra lines, no random eye drift, no cutaway that hides his hand or gaze.
Review: trigger line, pre-reaction, gaze answer, hand tell, silence decision, envelope pressure, and unchanged table barrier are visible.
```

## Sound-Image Cue Sheet Prompt Card

Use this when a prompt asks for sound design, Foley, ambience, silence, native audio, sound effects, offscreen sound, sound bridge, room tone, impact sound, listening point, or "cinematic audio." Write sound as timed events with source and visible consequence, not as atmosphere alone.

```text
sound_id:
platform / mode:
native audio support:
clip duration:
one-sentence visual premise:

sound-image contract:
  listening point:
  source status:
  cue timeline:
    0-2s:
    2-4s:
    4-6s:
    6-8s:
    8-10s:
  distance / obstruction:
  Foley / material proof:
  ambience bed:
  silence / density curve:
  image relation:
  listener reaction / story-state change:
  mix priority:
  negative audio constraints:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Sound-Image Prompt Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| source status | "offscreen diegetic floorboard creak behind the closed door" | sound must create space or threat | Do not write only "eerie sound" | source is inferable and not visually contradicted |
| cue time window | "at 4-5s, one dry wood creak, then stop" | timing must sync with reaction | Do not stack many cues in one second | cue lands before the named reaction |
| sound perspective | "heard from the detective's position, muffled through the door" | distance, subjectivity, or obstruction matters | Do not switch hearing POV accidentally | distance/obstruction feels consistent |
| Foley material proof | "wet leather glove creaks as fingers tighten" | material, grip, weight, or contact needs proof | Do not over-sound every tiny motion | Foley matches visible motion and material |
| ambience bed | "low apartment room tone and laptop fan under all cues" | space needs acoustic life | Ambience should not mask key cues | bed is present but lower than the cue |
| silence density curve | "room tone thins until only breath remains" | tension, shock, listening, or subjective focus | Silence is not just missing audio | removed layers and remaining cue are clear |
| sound bridge / lead | "phone buzz begins before the character looks down" | sound should pull attention before image/action | Do not lead without a source or consequence | audio expectation is answered by image/reaction |
| mix priority | "foreground Foley and offscreen creak over music" | subtle cue may be masked | Do not ask for score if cue must be precise | main cue is audible and not buried |
| image consequence | "after the creak, she freezes and stops turning the key" | sound must change story state | Do not leave sound without reaction | visible behavior changes after the cue |
| platform bound | "native audio if supported; otherwise use as post-production cue sheet" | platform capability varies | Do not assume every model follows Veo audio behavior | prompt remains usable even without native audio |

### Sound Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| sound becomes generic ambience | source, material, or mix priority missing | name one source, material texture, and foreground priority |
| no sound appears | platform/mode or cue sheet unsupported/unclear | state native audio support if available; keep cue sheet for post |
| sound lands at wrong time | cue time window missing | add second ranges and a visible reaction after the cue |
| music masks the important sound | mix priority absent | write "no score; Foley/room tone/offscreen cue are mix priority" |
| offscreen source appears onscreen | source protection absent | lock barrier/source offscreen and name what stays closed/hidden |
| Foley feels detached | visible motion/material relation missing | tie Foley to hand, cloth, foot, prop, surface, or impact |
| silence feels like broken audio | density curve absent | write what layers fade out and what one cue remains |
| too many cues blur together | prompt overload | keep one ambience bed, one primary cue, one reaction |

### Minimum Sound-Image Prompt

```text
Duration: [5-10s], native audio if supported.
Listening point: [character / room / camera / object / offscreen space].
Cue sheet:
  [0-2s]: [ambience bed / room tone].
  [2-4s]: [specific source + material + distance/obstruction].
  [4-6s]: [visible reaction / story-state change].
  [6-8s]: [sound tail / silence curve / final cue].
Foley/material: [surface or object] sounds like [texture/weight/contact].
Mix priority: [primary cue] above [ambience/music].
Negative / positive lock: no generic score; no jump-scare sting; no narration; keep source offscreen if required.
Review: check [source present -> timing -> distance/obstruction -> material proof -> visible reaction -> mix priority].
```

## Subjective Listening POV Prompt Card

Use this when sound should be heard from a character's body, memory, device, room position, obstructed location, or altered condition. Do not write only "muffled" or "quiet"; define whose hearing owns the moment, which layers change, and what image behavior proves the POV.

```text
listening_pov_id:
platform / mode:
native audio support:
clip duration:
visual premise:

subjective listening contract:
  hearing owner:
  hearing condition:
  source status:
  auditory filter stack:
    distance:
    obstruction:
    body / device / memory filter:
    spatial direction:
  removed or reduced layers:
  remaining cue anchor:
  transition into POV:
  transition out of POV:
  visible behavior / story consequence:
  mix priority:
  post-production cue fallback:

constraints:
  preserve:
  avoid:

review checks:
  hearing POV remains consistent:
  removed layers are identifiable:
  remaining cue is audible:
  visual behavior answers the cue:
  source status is not contradicted:
  native-audio or post cue path is clear:
validation status:
```

### Subjective Listening POV Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| hearing owner | "heard from the injured courier's position, not the camera" | emotion depends on whose perception owns sound | Do not switch listener mid-beat without a transition | filtering matches the named listener |
| obstruction filter | "voice muffled through closed metal door, high frame-right" | barrier maps offscreen space | Do not reveal the source if barrier is the point | barrier stays visible/closed and sound feels blocked |
| body-condition filter | "crowd drops to low smear; sharp tinnitus tone and breath remain" | shock, concussion, fear, immersion | Do not use medical effect as decoration | visible stillness or disorientation answers it |
| device / recording filter | "tape hiss foreground; replayed word partly buried under street noise" | evidence, memory, surveillance, ambiguity | Do not let dialogue become clean exposition | artifact/noise and partial meaning remain |
| silence layer curve | "music and crowd fade; only cloth rustle and breath remain" | attention narrows | Silence is not broken audio | removed layers and remaining cue are clear |
| transition into POV | "after impact, sound collapses into ringing over 0.5s" | subjective shift must be motivated | Do not start filtered without trigger unless established | visible trigger precedes auditory shift |
| transition out of POV | "ringing recedes when she touches the door handle" | return to objective space matters | Do not stay filtered if next cue needs objective clarity | room tone or source direction returns |
| post cue fallback | "if native audio is unsupported, use this as post-production cue sheet" | platform audio uncertain | Do not assume every model generates subtle audio | visual timing still supports later sound design |

### Minimum Subjective Listening Prompt

```text
8-second single shot, native audio if supported; otherwise use as post-production cue sheet.
Visual premise: a courier crouches behind a closed archive door after a loud impact; the hallway outside remains offscreen.
Listening POV: heard from the courier's position, inside the room, with the closed metal door between her and the hall.
0-2s: normal room tone, faint fluorescent hum, distant hallway footsteps.
2-4s: after the impact, room tone collapses into a thin ringing tone; hallway footsteps become muffled low pulses through the metal door.
4-6s: only her breath and sleeve rustle remain sharp; one key jingle outside is barely audible high frame-right.
6-8s: ringing fades slightly as she looks toward the handle and stops breathing.
Mix priority: breath and ringing foreground, muffled hallway low, no score, no clean dialogue, no jump-scare sting.
Review: hearing owner stays the courier, the door remains closed, layers fade in the named order, key jingle causes the look, and the cue sheet still works if added in post.
```

## Audio Event Priority Prompt Card

Use this when a short AI video prompt needs one important sound to land clearly: offscreen threat, Foley detail, impact, phone buzz, door click, breath hold, mechanical latch, room tone collapse, or subjective hearing shift. Keep one primary audio event unless the clip is long enough to support more.

```text
audio_event_id:
platform / mode:
native audio support:
clip duration:
visual premise:

audio event priority contract:
  primary audio event:
  sound source:
  source status:
  time window:
  listener point:
  distance / obstruction:
  material / performance quality:
  ambience bed:
  silence / layer change:
  image consequence:
  mix hierarchy:
  source reveal rule:
  forbidden audio:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Audio Event Priority Table

| Mechanism | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| one primary event | "one dry floorboard creak at 4s is the only foreground cue" | subtle cue must register | Do not ask for several important cues in 8s | main cue is audible and isolated |
| source + material | "old wood creak from the ceiling joist" | sound should feel physical | Do not write generic scary noise | material/source can be inferred |
| listener point | "heard from the detective's seated position, not from outside the room" | distance or subjectivity matters | Do not switch hearing POV accidentally | volume/filtering matches listener location |
| obstruction | "muffled through the closed door, high frame-right" | offscreen space must be mapped | Do not reveal the source early | barrier remains visible/closed; cue feels blocked |
| mix hierarchy | "creak above room tone; no score or sting" | music may mask the cue | Do not request a score when Foley must lead | cue is not buried under music |
| silence layer curve | "laptop fan fades; only breath and room tone remain after the cue" | tension needs active quiet | Silence is not broken audio | removed and remaining layers are clear |
| image consequence | "after the creak, her hand stops on the key" | sound must change story state | Do not leave sound unreacted to | visible reaction follows cue |
| source reveal rule | "door stays shut; no visible intruder" | sound source must remain unseen | Do not confuse hidden source with missing source | source unseen, but direction/barrier is legible |

### Audio Event Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| sound becomes generic ambience | primary event or material missing | reduce to one named source/material cue |
| music masks the cue | mix hierarchy absent | set Foley/offscreen cue above room tone; forbid score/sting |
| cue lands too early/late | time window missing | name exact second range and visible reaction after it |
| offscreen source appears | source reveal rule absent | lock barrier closed and forbid visible source reveal |
| character ignores cue | image consequence absent | add freeze, gaze shift, breath stop, object release, or playback stop |
| silence feels like missing audio | silence layer curve absent | write which layers fade and which cue remains |
| spatial relation unclear | listener point/obstruction absent | name listener position, direction, distance, wall/door/ceiling/filter |
| audio overload | too many foreground cues | keep one primary event plus one low ambience bed |

### Minimum Audio Event Priority Prompt

```text
8-second locked suspense shot, native audio if supported.
Visual premise: detective sits beside a laptop in a dim hallway; closed apartment door remains frame-right.
Primary audio event: at 4s, one dry floorboard creak from behind the closed door, muffled through wood, high frame-right.
Listener point: heard from the detective's seated position; room tone and laptop fan stay low under the cue.
Silence curve: after the creak, laptop fan fades slightly; breath and room tone remain.
Image consequence: detective's hand stops on the recorder button, shoulders still, eyes move toward the closed door.
Mix hierarchy: floorboard creak foreground, breath second, room tone/laptop fan low; no score, no drone, no jump-scare sting, no narration.
Source reveal rule: door stays closed; no visible intruder or source reveal.
Review: cue occurs at 4s, sounds muffled and directional, source remains hidden, reaction follows, music does not mask the cue.
```

## Breakdown-To-Prompt Contract Card

Use this when a film clip, public breakdown, storyboard, shot list, or timecoded reference needs to become an original AI video prompt. Do not copy the scene. Extract the function chain and rebuild it with new characters, space, action, and stakes.

```text
breakdown_id:
source / reference:
copyright-safe use:
platform / mode:
clip duration:

source breakdown row:
  shot / beat timecode:
  objective evidence:
  dominant track:
  shot function:
  neighbor relation:
  viewer information shift:

portable mechanism:
  function chain:
  timing anchors:
  spatial contract:
  sound / performance / prop cue:
  what must stay non-portable:

original prompt contract:
  one-sentence premise:
  duration and shot count:
  camera:
  subject action:
  blocking / space:
  light / material:
  sound, if supported:
  edit / transition rule:
  negative / positive lock:
  review checks:
```

### Breakdown-To-Prompt Table

| Breakdown finding | Prompt control | Use when | Misuse boundary | Review check |
| --- | --- | --- | --- | --- |
| objective evidence | copy the controllable device, not the plot | a clip analysis has useful camera/sound/blocking logic | Do not paraphrase the scene or dialogue | prompt has new subject, setting, and stakes |
| shot function | write what the shot changes for the viewer | shot labels feel decorative | Do not treat close-up/wide/pan as meaning by itself | review names the information or attention shift |
| neighbor relation | keep the bridge logic between beats | cuts, sound bridges, eyelines, or matches create meaning | Do not isolate a shot from the cut before/after | output preserves setup -> cue -> answer or contrast |
| function chain | compress a sequence into 3-5 portable beats | translating a multi-shot reference to a short AI clip | Do not overload a 5-10s prompt with a whole scene | each beat is visible/audible and changes state |
| dominant track | choose image, sound, performance, blocking, light, prop, or rhythm as primary | too many controls compete | Do not make every film layer equally important | primary track is inspectable in the output |
| reference boundary | name what not to import from the source | using famous films, directors, or clips as study material | Do not ask for a living artist's style or copy a copyrighted scene | prompt describes mechanism without dependent scene details |
| review proof | map every imported mechanism to an output check | turning analysis into generation workflow | Do not claim success from prompt wording alone | generated clip can be scored against the contract |

### Minimum Breakdown-To-Prompt Prompt

```text
Reference use: extract only [portable mechanism], not the scene, characters, dialogue, plot, or exact staging.
Function chain: [orient/reveal/withhold/react/state change] over [duration].
Original premise: [new character + new space + new action problem].
Camera / edit: [shot count or single shot], [shot size/movement], [bridge logic].
Primary track: [image / sound / performance / blocking / light / prop / rhythm].
Timing anchors: [0-2s setup], [2-4s cue], [4-6s reaction], [6-8s state change].
Negative / positive lock: preserve [barrier/geography/action relation]; avoid [source plot/style imitation/extra cuts].
Review: check [function chain], [dominant track], [bridge logic], [new information], [no copied scene dependency].
```

## Clip-To-Prompt Review Loop Card

Use this when learning from a film segment, public scene analysis, shot-by-shot table, or reference clip. The goal is not to imitate the source; it is to extract a portable mechanism, write an original prompt, then review the generated output against that mechanism.

```text
loop_id:
source clip / analysis:
copyright / access boundary:

breakdown evidence:
  time range:
  objective shot facts:
  dominant track:
  viewer information change:
  shot function chain:
  neighbor relation:

portable mechanism filter:
  transferable function:
  required evidence in a new scene:
  source-bound details to discard:
  do-not-copy boundary:

original prompt contract:
  original premise:
  one dominant event:
  camera / framing:
  action / state change:
  space / screen direction:
  light / material:
  sound, if supported:
  style / reference role:
  constraints:
  review checks:

generated-output review:
  did the portable mechanism appear:
  did the scene remain original:
  did the output copy source details:
  which evidence gate failed:
  minimum retry delta:
validation status:
```

### Clip-To-Prompt Loop Table

| Step | What to preserve | What to discard | Prompt control | Review proof |
| --- | --- | --- | --- | --- |
| Objective breakdown | Shot facts, timing, dominant track, visible/audible state changes | interpretation-only language | "timecode -> objective evidence -> viewer information" | table can be checked without knowing the prompt |
| Function chain | orient, reveal, conceal, compare, react, reverse, state change | famous shot label or vague mood | "orient -> offscreen cue -> reaction -> changed state" | output delivers the same information path |
| Portable mechanism | relation between setup, trigger, action, reaction, and hold | source characters, dialogue, plot, exact staging, iconic image | "borrow only the reveal logic / contact proof / sound bridge" | new scene proves same mechanism with original content |
| Original prompt | one dominant event, prompt fields, timing locks, boundaries | full plot summary, long screenplay, name stack | scene + camera + action + light/sound + constraints + review | generated output can be audited gate by gate |
| Generated review | mechanism success, originality, failed gates, retry delta | "looks like the source" as success | minimum delta fixes one failed gate | retry improves one field without damaging successful gates |

### Minimum Clip-To-Prompt Loop Prompt

```text
Source use: extract mechanism only, not imitation.
Portable mechanism: orient the viewer to a target, trigger one offscreen cue, hold on the reaction, then reveal one changed state.
Original 8-second scene: a night archivist checks a sealed evidence drawer; one elevator bell rings offscreen; she freezes; the drawer tag silently changes from blue to red.
Camera: locked medium-wide; archivist, drawer, and elevator door direction remain readable.
Sound, if supported: one distant elevator bell at 3s; room tone drops slightly after.
Constraints: no copied source characters, plot, dialogue, exact staging, famous composition, or director/style name. Do not add a second location or monster reveal.
Review: target oriented, offscreen cue occurs before reaction, reaction hold is visible, drawer tag changes state, scene remains original.
```

## State-Change Output Review Card

Use this when a prompt depends on an object, surface, mechanism, light, body, relationship, or scene state changing visibly over a short clip. It is especially useful after `prepared receiving mark`, `arrival as state change`, `action contact proof`, `material response`, or transformation prompts.

```text
review_id:
source prompt / output:
platform / mode:
clip duration:

expected contract:
  initial state:
  prepared target / receiving zone:
  action path or trigger:
  contact / activation moment:
  changed state:
  reaction hold:
  forbidden source-copy or artifact:

evidence check:
  E1_initial_state_visible:
  E2_target_relation_stable:
  E3_action_path_readable:
  E4_contact_or_trigger_occurs:
  E5_changed_state_visible:
  E6_hold_or_reaction_registers:
  E7_no_continuity_cheat:
  E8_no_forbidden_source_copy:

failure class:
retry delta:
validation status:
```

### State-Change Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| viewer cannot tell what changed | initial state or changed state missing | name both before-state and after-state in the prompt |
| object moves but has no consequence | contact / trigger moment missing | add one visible activation: click, lock, flash, crack, tick, recoil, spill, or light change |
| target drifts or changes identity | target relation not locked | keep target visible, fixed, and named throughout the clip |
| action path feels random | approach path missing | describe start position, direction, target, and speed |
| change happens too early or offscreen | timing anchor missing | assign the state change to a narrow time window and hold afterward |
| output copies the reference image | reference boundary absent | list forbidden source details and write a new subject/surface/consequence |
| prompt becomes a montage | too many locations or state changes | reduce to one target, one moving object, one changed state |

## Reference Identity / Continuity Lock Prompt Card

Use this when a generated image/video needs the same character, costume, prop, weapon, vehicle, location, or style system to survive a new pose, camera angle, lighting setup, shot, or scene. The goal is not to lock every pixel; the goal is to protect the few anchors that make the subject recognizable while allowing the shot to move.

```text
continuity_id:
platform / mode:
reference assets:
  @Image1 role:
  @Image2 role:
  @Image3 role:

continuity contract:
  identity anchors:
  hair / face / body anchors:
  costume anchors:
  prop / weapon anchors:
  scene / layout anchors:
  style / finish anchors:
  physical identity anchors, if action:

allowed changes:
  pose / expression:
  camera / crop:
  lighting / weather:
  cloth / hair / surface motion:

forbidden drift:
  identity:
  costume:
  prop / weapon:
  scene / layout:
  style / reference role:

review checks:
  same person / subject:
  same costume color and structure:
  same prop silhouette and grip:
  same spatial relationship:
  allowed changes occurred without changing anchors:
  no reference-role leakage:
validation status:
```

### Reference Role Language

```text
@Image1 locks character identity only: face shape, hair silhouette, age impression, body proportion, and expression baseline.
@Image2 locks costume and weapon only: garment structure, color placement, material, weapon silhouette, grip, and glowing parts.
@Image3 locks layout only: relative position, foreground/background layer, object footprint, facing direction, and action path.
Do not copy @Image3's diagram marks, labels, arrows, colors, or simplified shapes into the final image/video.
Allowed changes: new pose, new camera angle, small facial reaction, cloth/hair movement, and lighting variation.
Forbidden drift: face swap, new hairstyle, costume redesign, weapon changing size/type, extra characters, background replacement, merged references.
```

### Continuity Drift Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| same character becomes a different person | identity anchors too vague or reference role missing | name 4-6 durable anchors: face shape, hair silhouette, age impression, body proportion, eye/brow relation, expression baseline |
| outfit changes every shot | costume anchors not separated from pose/action | lock garment structure, color placement, material, key accessories, damage/wear state |
| weapon or prop morphs | prop silhouette and handling missing | lock length, shape, color, material, grip point, scale to hand/body, and allowed motion |
| reference images merge wrongly | reference roles conflict | assign one job per reference: identity, costume/prop, scene/layout, light/style |
| layout drifts between shots | spatial anchors absent | lock left/right relation, foreground/background layer, object footprint, facing direction, and action path |
| output is stiff or copy-pasted | allowed changes missing | explicitly allow pose, expression, camera crop, cloth/hair motion, and lighting variation |
| background or style leaks from identity reference | do-not-copy boundary absent | state which reference details must not transfer: background, pose, diagram marks, unrelated lighting, old scene |

### Minimum Continuity Prompt Block

```text
Continuity: same character as @Image1; preserve oval face, short black bob with blunt bangs, calm narrow eyes, slim upright posture, and age impression.
Costume/prop: preserve dark teal jacket, silver collar clasp, black gloves, and the same compact brass scanner held in the right hand.
Scene/layout: use @Image2 only for the corridor layout: character left foreground, locked door right background, scanner pointed toward the door.
Allowed changes: she may turn her head, raise the scanner, blink, and shift one step; hair tips and jacket hem can move.
Forbidden drift: no new face, no hairstyle change, no jacket recolor, no extra scanner, no weapon replacement, no background swap, no copying @Image2's arrows or color blocks.
Review: check face/hair, costume structure, scanner silhouette, hand relation, corridor left/right layout, and allowed movement without identity drift.
```

## Style Anchor Role Prompt Card

Use this when a prompt cites a film, director, cinematographer, editor, action director, sound designer, studio, reference image, or visual style source. The anchor is useful only after it is translated into one controllable layer and one reviewable mechanism.

```text
style_anchor_id:
platform / mode:
source references:
copyright / living-artist boundary:

style anchor contract:
  reference name:
  source type:
  allowed mechanism:
  controlled layer:
  prompt translation:
  forbidden transfer:
  compatibility with other anchors:
  fallback if the name is removed:

scene prompt:
  original premise:
  camera / staging:
  light / color / material:
  editing / rhythm:
  sound, if supported:
  style anchor wording:

constraints:
  preserve:
  avoid:

review checks:
  each anchor controls one visible/audible layer:
  no copied characters / plot / exact staging:
  no living-artist imitation command:
  no merged reference roles:
  no unexplained name stack:
validation status:
```

### Style Anchor Role Table

| Anchor type | Allowed control | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Cinematographer / lighting reference | motivated source, contrast, separation, material response | "borrow only the motivated warm practical against cool exterior spill" | exact palette, signature film look, specific shot, living-person style imitation | source, zone, shadow, and material response are visible |
| Editor / rhythm reference | cut permission, hold length, sound bridge, reaction breath | "borrow only the sound-led reveal and 0.7s reaction hold" | famous sequence structure, plot twist, dialogue, montage identity | every cut or hold has a named permission cue |
| Action director / fight reference | geography, contact proof, rhythm oscillation, camera responsibility | "borrow only arena roadmap before impact and receiver response after contact" | brutality level, real stunt instruction, character violence texture | geography, contact, recoil, and recovery are readable |
| Sound reference | listening point, mix hierarchy, silence layer, offscreen source | "borrow only subjective listener point and one foreground Foley cue" | creature/device recipe, atrocity-specific content, full soundtrack imitation | cue timing, source status, mix priority, and reaction align |
| Film scene reference | function chain | "borrow only orient -> offscreen cue -> reaction -> state change" | characters, exact location, dialogue, framing, blocking, plot | output proves the function chain with original content |
| Uploaded image reference | identity, costume, prop, layout, light, or style role | "@Image2 controls corridor layout only" | diagram marks, unrelated background, pose copy, merged identity/style | intended role appears without unrelated leakage |
| Director / studio name | use only after mechanism extraction | "translate to restrained camera, one practical source, and delayed reaction hold" | broad "in the style of" imitation, all-purpose prestige look | name could be removed and the prompt still works |

### Minimum Style Anchor Prompt Block

```text
Reference use, not imitation:
- Reference A controls only lighting mechanism: one visible warm practical shapes the hands and table; cool exterior spill stays in the background. Do not copy its characters, location, exact composition, or signature palette.
- Reference B controls only editing mechanism: one sound-led reveal followed by a short reaction hold. Do not copy its scene, dialogue, plot, or famous shot.

Original 8-second scene: a courier in a rain-dark office opens a blank envelope, hears one elevator bell offscreen, stops breathing, and notices the seal has changed color.
Camera stays medium-wide and locked; envelope, doorway, and courier remain visible.
Negative / lock: no named-style collage, no living-artist imitation, no copied scene details, no merged references, no extra director names.
Review: each reference contributes one visible/audible mechanism; the scene remains original; no reference-role leakage.
```

## Transition / Match-Cut Style Anchor Prompt Card

Use this when a prompt cites an editor, film, sequence, trailer, music video, or famous transition as a reference. The anchor should control one bridge layer only: how shot A hands meaning to shot B, not the source scene's objects, plot, score cue, or iconic image.

```text
transition_anchor_id:
platform / mode:
anchor name or source:
allowed transition layer:
scene-specific job:

transition anchor contract:
  source evidence:
  allowed mechanism:
  outgoing element:
  incoming element:
  bridge logic:
  timing / cut permission:
  forbidden transfers:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Transition / Match-Cut Anchor Table

| Transition anchor use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Graphic match anchor | shape, color, motion, scale, or screen-position relation bridges two original objects | "match circular clock face to round elevator indicator; same screen position, new story state" | iconic source objects, exact composition, plot leap, score cue | outgoing and incoming elements share the named visual relation and change meaning |
| Match-on-action anchor | one action phase continues across the cut | "hand reaches for folder -> cut -> same hand grips scanner; same direction, new information" | copied choreography, source props, random action fragments | outgoing and incoming phases are continuous and readable |
| Eyeline answer anchor | look in shot A is answered by object or space in shot B | "she looks screen-right -> cut to locked service door at matching screen position" | famous reveal, copied staging, unrelated insert | gaze direction, target, and new information align |
| Sound-bridge anchor | sound leads or trails to reinterpret the next image | "elevator bell begins before cut; next image reveals empty corridor" | recognizable cue, score motif, source plot twist | sound timing changes how the next image is read |
| Name-free fallback | same bridge logic with no film, editor, sequence, or famous-cut name | "match same circular shape across cut; no source scene objects or famous transition" | prestige transition names, style soup | prompt still works after the reference name is removed |

### Minimum Transition / Match-Cut Anchor Prompt Block

```text
Reference use, not imitation: transition anchor controls bridge logic only.
Allowed mechanism: graphic match from one original circular object to another, changing story state.
Name-free fallback: shot A ends on a round clock stamp filling the left third; cut to shot B with a round elevator indicator in the same screen position; color and shape match, but location/time changes.
Forbidden: no copied famous source objects, exact composition, plot leap, score cue, dialogue, characters, spacecraft/bone imagery, or editor/film name stack.
Review: outgoing element, incoming element, match type, bridge logic, and changed information are visible; scene remains original.
```

## Documentary / Realism Style Anchor Prompt Card

Use this when a prompt cites documentary, direct cinema, cinema verite, observational footage, interview footage, archival footage, body-worn camera, news texture, or "realistic documentary" as a reference. The anchor should control one evidence/camera relation only and must not make fictional AI video pass as real evidence.

```text
documentary_anchor_id:
platform / mode:
anchor name or source:
allowed realism layer:
scene-specific job:

documentary realism contract:
  evidence status:
  camera relation:
  subject awareness:
  staging boundary:
  light / exposure logic:
  sync sound / room tone:
  forbidden authenticity claims:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Documentary / Realism Anchor Table

| Realism anchor use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Observational anchor | camera watches without directing the action | "fictional observational scene; shoulder-height handheld stays three meters away while workers ignore the camera" | fake hidden-camera claim, real event claim, crisis footage | subject behavior continues without performing for camera |
| Direct-cinema texture anchor | portable handheld camera plus synchronous room sound | "controlled handheld drift, available fluorescent light, live room tone, cloth rustle, and one offscreen chair scrape" | real documentary title, official logo, real person, exact event | realism comes from camera/sound relation, not a truth claim |
| Interview / participant anchor | camera is acknowledged through eyeline, answer timing, or offscreen interviewer | "subject answers an unheard interviewer; eyeline stays just off lens; room tone remains continuous" | fabricated quote, real journalist, real outlet branding | camera relation is explicit and not pretending to be hidden evidence |
| Archive-like insert | aged or found-footage texture for fictional material | "fictional training-tape insert; date label is invented; mild tape noise; no real institution marks" | real archive watermark, exact historical tragedy, forged document | source status is fictional or reconstructed and visibly bounded |
| Name-free fallback | same realism mechanism with no mode/person/film/news name | "fictional observed scene, handheld witness camera, available light, sync room sound, no official marks" | prestige documentary names, deceptive authenticity | prompt still works after documentary labels are removed |

### Minimum Documentary / Realism Anchor Prompt Block

```text
Reference use, not deception: documentary anchor controls camera relation and sync-sound texture only.
Evidence status: fictional staged scene, not real footage or news evidence.
Name-free fallback: shoulder-height handheld camera observes from three meters away; subjects continue sorting files without addressing camera; available fluorescent light, slight exposure breathing, live room tone, paper scrape, and one offscreen chair sound remain synced.
Forbidden: no real person, real outlet, official logo, watermark, crisis/event claim, date/location claim, fabricated quote, surveillance claim, hidden-camera claim, or prompt wording that asks the clip to pass as real evidence.
Review: camera relation, subject awareness, available-light logic, sync sound, and fiction/disclosure boundary are visible or inferable.
```

## Archival / Found-Footage Insert Prompt Card

Use this when a prompt asks for archival footage, found footage, old home movies, training tapes, security tapes, broadcast recordings, damaged film, VHS, 16mm, public-domain inserts, or "discovered evidence" texture. The anchor should control source status and media artifact behavior only, not fabricate provenance or claim the generated clip is real evidence.

```text
archival_insert_id:
platform / mode:
insert type:
source status label:
scene-specific job:

archival insert contract:
  source status:
  diegetic owner / viewer:
  artifact layer:
  continuity relation:
  time / location label policy:
  audio artifact, if any:
  forbidden provenance claims:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Archival / Found-Footage Insert Table

| Insert use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Fictional archive insert | invented source status plus limited film wear | "fictional archive insert; invented shelf code; mild gate weave and two dust scratches; no real archive mark" | real institution watermark, real event/date/location claim | source status is fictional and artifact layer is controlled |
| Diegetic tape | footage exists inside the story world as a prop or monitor feed | "diegetic training tape playing on a CRT; soft scanlines, muted audio hiss, invented label" | real training agency, official seal, forged document | viewer understands who owns or watches the tape |
| Found-footage clue | aged insert reveals one story clue, not a whole backstory dump | "three-second tape insert reveals the missing door number; keep same hallway geography as main scene" | unrelated montage, exposition overload, fake evidence claim | insert changes one piece of information and returns to scene logic |
| Media artifact layer | one or two physical/degraded-media cues | "faded dye plus vertical scratch; keep faces readable and action continuous" | texture stack, illegible grime, random glitches | artifact affects surface without hiding required action |
| Name-free fallback | same insert logic with no archive, outlet, film, or institution name | "fictional old tape insert, invented label, light dust, stable clue, no official marks" | prestige archive naming, forged provenance | prompt works after all source names are removed |

### Minimum Archival / Found-Footage Insert Prompt Block

```text
Reference use, not forgery: archival insert controls source status and artifact layer only.
Source status: fictional diegetic training tape inside the story, not real archive or news evidence.
Name-free fallback: three-second insert on a CRT monitor; invented shelf code "T-14"; mild gate weave, two dust scratches, soft tape hiss; the insert reveals one matching door number and then returns to the main scene.
Forbidden: no real archive watermark, museum mark, news outlet, official seal, real date/location, real crisis/event claim, forged document, fabricated quote, or heavy damage hiding the clue.
Review: source status label, artifact layer, clue continuity, and non-forgery boundary are clear.
```

## Title / Card / Intertitle Graphic Insert Prompt Card

Use this when a prompt asks for title cards, intertitles, lower-thirds, date/location cards, chapter cards, onscreen text, warning cards, UI-like labels, or graphic inserts. The card should control what text does for the scene, not import a famous title sequence or let text compete with action.

```text
title_insert_id:
platform / mode:
insert type:
exact text / payload:
scene-specific job:

title insert contract:
  information payload:
  typography role:
  placement / safe area:
  duration / reading window:
  transition relation:
  interaction with image / subtitles:
  forbidden text or design transfers:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Title / Card / Intertitle Insert Table

| Insert use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Intertitle / chapter card | brief text changes time, place, chapter, or withheld information | "black intertitle card for 1.5 seconds: 'THREE HOURS EARLIER'; centered plain white type" | famous silent-film card design, ornate border, extra prose | exact text is readable and changes timeline understanding |
| Lower-third label | identifies person/place/status while scene continues | "lower-left label: 'Archivist, Night Shift'; hold 2 seconds; keep clear of hands and subtitles" | news outlet branding, fake credentials, real institution | label is accurate, legible, and does not cover key action |
| Date/location card | anchors story geography or time | "small top-left card: 'Dock 7, 02:13'; fade in after cut; fade out before dialogue subtitle" | real location claim, official document style, random map UI | card timing and scene geography align |
| Graphic clue insert | text reveals one clue as part of the shot | "folder label reads 'T-14'; camera holds until label is readable; no other text" | text clutter, invented extra names, unreadable microtype | one payload is readable and story-relevant |
| Name-free fallback | same text function with no title-designer, film, or sequence name | "plain centered card, exact words only, readable duration, no famous title treatment" | prestige title references, logo imitation, typography collage | prompt works after all design names are removed |

### Minimum Title / Card / Intertitle Prompt Block

```text
Reference use, not title-sequence imitation: title insert controls information delivery only.
Information payload: exact centered intertitle text, "THREE HOURS EARLIER".
Name-free fallback: black card, plain white centered type, 1.5-second hold, hard cut in from the present-tense scene and hard cut out to the earlier hallway; no other text.
Forbidden: no copied title sequence, logo, studio mark, branded font identity, ornate border, credit list, extra words, misspelled text, random glyphs, or moving typography that reduces readability.
Review: exact text, duration, placement, transition relation, and timeline function are readable.
```

## Map / Diagram / Screen UI Insert Prompt Card

Use this when a prompt asks for a map, diagram, tactical screen, dashboard, phone screen, monitor UI, radar, scanner readout, control panel, chart, data overlay, hologram, or screen graphic. The insert should deliver one scene decision or clue, not become decorative interface noise.

```text
screen_ui_insert_id:
platform / mode:
insert type:
diegetic status:
scene-specific job:

screen UI insert contract:
  information payload:
  diegetic / non-diegetic status:
  owner / viewer:
  placement / screen surface:
  interaction timing:
  labels / symbols:
  visual hierarchy:
  forbidden UI clutter:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Map / Diagram / Screen UI Insert Table

| Insert use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Diegetic monitor UI | screen exists inside the story and changes action | "physical monitor on desk shows one red locked-door icon and route A blocked; character looks at it before moving" | fake operating system, random panels, tiny unreadable text | viewer reads status and sees behavior change |
| Map / route insert | route, boundary, distance, or blocked path clarifies geography | "simple map insert: current room, locked service door, alternate stair route; three labels only" | full GIS clutter, real location claim, decorative grid | geography or choice becomes clearer |
| Diagram / schematic insert | one mechanical or spatial relation becomes legible | "clean schematic labels latch, hinge, power line; hold until latch location is readable" | engineering how-to, dense blueprints, copied brand diagrams | one relation is readable and affects the next beat |
| Chart / dashboard insert | one comparison, threshold, warning, or status value matters | "dashboard shows oxygen 18% crossing red threshold; no other graphs" | fake corporate dashboard, meaningless numbers, graph clutter | threshold and consequence are readable |
| Name-free fallback | same UI function with no film, game, OS, or brand name | "plain in-world screen, one warning, one route, readable labels, no extra interface noise" | FUI name stack, brand imitation, prestige interface references | prompt works after all UI reference names are removed |

### Minimum Map / Screen UI Insert Prompt Block

```text
Reference use, not decorative FUI: screen UI insert controls one story decision only.
Diegetic status: physical monitor inside the room, visible to the character.
Information payload: route A blocked; alternate stair route open.
Name-free fallback: desk monitor shows a simple two-route map with three labels: CURRENT ROOM, LOCKED DOOR, STAIRS OPEN; red highlight on locked door, green line to stairs; character glances at the screen, then turns toward the stairs.
Forbidden: no fake OS brand, real map service, dense panels, random numbers, unreadable microtext, extra graphs, sci-fi UI clutter, floating labels, or animation that hides the route.
Review: screen surface, viewer/owner, payload, labels, interaction timing, and changed behavior are visible.
```

## Split-Screen / Multi-Panel Layout Prompt Card

Use this when a prompt asks for split screen, side-by-side panels, triptych, quad screen, surveillance grid, comic-panel layout, parallel action, simultaneous calls, before/after comparison, or expectation-vs-reality layouts. The layout should make one relationship legible, not multiply unreviewable action.

```text
split_screen_id:
platform / mode:
layout type:
panel count:
scene-specific job:

split-screen contract:
  panel count and geometry:
  panel ownership:
  temporal relation:
  viewer priority cue:
  sound / motion focus:
  seam / border logic:
  transition in / out:
  forbidden collage behavior:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Split-Screen / Multi-Panel Layout Table

| Layout use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Simultaneous two-panel action | two spaces unfold at the same time | "vertical split screen: left panel courier waits at locked door; right panel guard reaches for same door control at the same second" | extra panels, mismatched scale, unrelated action | both panels share one time beat and one causal relation |
| Staggered reveal panels | panel B answers panel A after a short delay | "left panel phone rings first; right panel character reacts 0.5s later; right panel owns sound after the ring" | random parallel montage, unclear sound owner | viewer can read trigger and delayed answer |
| Before/after comparison | two panels compare state change | "left panel before: empty desk; right panel after: stamped folder appears; same camera angle" | copied graphic layout, unrelated before/after | difference is readable and controlled |
| Surveillance grid | multiple panels show locations but one panel owns the story beat | "four-panel security grid; only top-right panel changes as the red door opens; other panels remain static" | busy fake CCTV wall, unreadable micro-action | viewer sees which panel matters |
| Name-free fallback | same relation with no film, comic, or title reference | "two stable side-by-side panels, one simultaneous cause/effect relation, one priority cue, no extra panels" | prestige split-screen references, copied page layout | prompt works after all reference names are removed |

### Minimum Split-Screen Prompt Block

```text
Reference use, not collage: split-screen layout controls one simultaneous cause/effect relation only.
Panel count: two vertical panels, stable border, equal width.
Temporal relation: simultaneous action at the same second.
Name-free fallback: left panel shows courier at locked service door; right panel shows guard pressing the door-control button at the same moment; right panel has the brighter hand motion for 1 second, then left panel owns the reaction as the lock light changes.
Forbidden: no third panel, moving borders, comic-book page layout, copied film reference, unrelated parallel action, tiny unreadable faces, mirrored duplicates, or sound from both panels competing at once.
Review: panel count, panel ownership, timing relation, viewer priority cue, seam stability, and changed state are visible.
```

## Rapid Montage / Short Sequence Prompt Card

Use this when a prompt asks for montage, rapid cuts, training sequence, preparation sequence, clue burst, time compression, trailer-like beat stack, music-driven inserts, or "show a lot quickly." The montage should compress or compare information through a small ordered chain, then end with a readable proof hold.

```text
rapid_montage_id:
platform / mode:
duration:
shot count:
scene-specific job:

rapid montage contract:
  montage function:
  beat order:
  shot count / insert count:
  transition logic:
  density curve:
  sound / music relation:
  final proof hold:
  forbidden overload / copied pattern:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Rapid Montage / Short Sequence Table

| Montage use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Time-compression montage | compress repeated work into few readable beats | "four-shot prep montage: empty case, tool selected, seal stamped, case locked; final 1s hold on locked case" | endless micro-cuts, copied training montage, unclear time jump | each beat advances time and final state is clear |
| Clue burst | show several clues then one conclusion | "three inserts only: torn label, matching stamp, map pin; then hold on detective circling the same code" | random evidence wall, unreadable inserts, extra plot | clues connect to one conclusion |
| Escalation montage | each beat raises pressure | "0-2s calm room, 2-4s alarm light, 4-5s crowd footsteps, 5-6s door handle moves, 6-8s hold on blocked exit" | constant peak intensity, no registration time | pressure curve rises and resolves into one consequence |
| Contrast montage | compare two states or spaces | "alternate clean desk / damaged desk / same missing folder; three beats, same camera angle" | unrelated imagery, style collage, copied sequence identity | contrast is legible and bounded |
| Name-free fallback | same montage logic with no film/editor/trailer name | "five seconds, three inserts, one density rise, one final proof hold, no extra locations" | prestige montage references, famous cut order | prompt works after all reference names are removed |

### Minimum Rapid Montage Prompt Block

```text
Reference use, not montage identity: rapid sequence controls time compression only.
Duration and count: 6-second montage, four shots maximum.
Beat order: empty metal case -> gloved hand selects tool -> red seal stamped -> case locked.
Density curve: one new visual fact per shot; no camera move during inserts; one soft metallic click carries across cuts.
Final proof hold: last 1 second holds on the locked case and changed red seal.
Forbidden: no copied famous montage, training montage parody, random micro-cuts, extra locations, unreadable inserts, text clutter, every cut on the music beat, or hidden final state.
Review: shot count, beat function, order, transition logic, density budget, and final proof hold are visible.
```

## Voiceover / Narration Prompt Card

Use this when a prompt asks for voiceover, narration, inner monologue, documentary narration, commentary, radio voice, phone voice, device playback, or explanatory VO. The narration should change how the image is read, not repeat what the image already shows.

```text
narration_id:
platform / mode:
narrator status:
scene-specific job:

narration contract:
  narrator status:
  diegetic / non-diegetic source:
  information timing:
  image relation:
  mix priority:
  silence / dialogue relation:
  forbidden redundancy:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Voiceover / Narration Table

| Narration use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| First-person memory VO | voice reframes the image with remembered interpretation | "first-person memory voice begins after she sees the sealed door; one short line reframes why she stops" | actor voice imitation, diary dump, repeating visible action | voice timing changes how the image is read |
| Documentary guide VO | voice provides context the image cannot show | "neutral fictional documentary narration gives one bounded fact before the archive-like insert; image shows only the object" | fake news authority, real person imitation, forged provenance | voice adds one bounded fact and stays fictional/sourced as required |
| Contradictory VO | voice conflicts with image for irony or unreliability | "calm narrator says the room is empty while a shadow moves behind the shelf" | confusing contradiction with no visual anchor | contradiction is legible and intentional |
| Device / radio voice | diegetic voice comes from an object or offscreen source | "muffled radio voice gives one warning; character hears it and lowers the tool" | clean omniscient narrator, invisible source confusion | source, mix, and listener reaction align |
| Name-free fallback | same narration function with no writer, narrator, actor, or film reference | "one unnamed offscreen voice, one new fact, starts after image cue, no repeated visible action" | prestige narrator names, monologue style-copy | prompt works after all reference names are removed |

### Minimum Voiceover / Narration Prompt Block

```text
Reference use, not exposition dump: narration controls image relation only.
Narrator status: non-diegetic third-person narrator, calm and unnamed.
Information timing: voice begins after the courier sees the sealed door.
Image relation: voice withholds the reason; it says one short line that reframes the pause.
Mix priority: voice is foreground for 1.5 seconds, then drops under room tone.
Forbidden: no celebrity voice, actor imitation, copied narration style, repeated visible action, extra backstory, fake documentary authority, dialogue overlap, or emotion labels the face already shows.
Review: narrator status, start cue, single new information layer, image relation, mix priority, and non-redundancy are clear.
```

## Subjective Memory / Flashback Insert Prompt Card

Use this when a prompt asks for flashback, memory fragment, remembered image, past-tense insert, trauma fragment, dreamlike recollection, subjective memory, or "show what happened before." The insert should carry one past-tense information payload and return cleanly to the present.

```text
memory_insert_id:
platform / mode:
present scene:
memory status:
scene-specific job:

memory / flashback contract:
  present-tense anchor:
  trigger cue:
  memory status:
  past payload:
  texture budget:
  sound / image bridge:
  return anchor:
  forbidden confusion:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Subjective Memory / Flashback Insert Table

| Insert use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Prop-triggered memory | object cue opens one past fact | "when her thumb touches the cracked locket, cut to a 1-second memory insert of the same locket new and unbroken on a hospital tray, then return to her thumb on the cracked locket" | generic sepia, unrelated backstory, long montage | same prop triggers and returns; one past fact is clear |
| Location-triggered flashback | same space appears in a prior state | "present hallway light flickers; 1.5-second flashback shows the hallway before the scorch marks; return to present scorch mark" | new location confusion, full scene replay | past and present share geometry but differ by controlled state |
| Unreliable memory | memory shows one visible uncertainty | "memory insert has one mismatch: the door number changes; return to present as character hesitates" | random surreal imagery, unclear timeline | mismatch is deliberate and tied to hesitation |
| Trauma fragment | brief sensory fragment with current safety anchor | "0.7-second memory fragment: hand releases same red scarf; immediately return to present hand gripping scarf" | gore, exploitation, shock montage | trigger, fragment, and present anchor stay bounded |
| Name-free fallback | same mechanism with no film, director, or famous flashback reference | "one present cue, one short past insert, one controlled texture difference, return to same prop" | prestige flashback references, copied scene identity | prompt works after all reference names are removed |

### Minimum Subjective Memory / Flashback Prompt Block

```text
Reference use, not dream filter: flashback controls one past-tense clue only.
Present anchor: courier stands in the present hallway holding a cracked brass locket.
Trigger cue: her thumb rubs the crack at 2 seconds.
Memory status: subjective character memory, not objective proof.
Past insert: 1-second insert of the same locket unbroken on a hospital tray.
Texture budget: slightly lower contrast and softer room tone only; no sepia wash, white flash, heavy blur, or extra montage.
Return anchor: cut back to her thumb still on the cracked locket in the present hallway.
Forbidden: no copied film flashback, unrelated childhood scene, new location without bridge, fake archive label, gore, or full backstory explanation.
Review: present trigger, memory status, one past payload, controlled texture difference, return anchor, and past/present separation are clear.
```

## Subjective Imagination / Dream / Hallucination Insert Prompt Card

Use this when a prompt asks for dream, fantasy, imagined outcome, hallucination, altered perception, intrusive image, symbolic visualization, nightmare fragment, or wish/fear image. The insert should define whose perception owns the unreality and what reality boundary the viewer can inspect.

```text
unreality_insert_id:
platform / mode:
present scene:
subjective status:
scene-specific job:

subjective unreality contract:
  subjective owner:
  trigger cue:
  subjective status:
  reality boundary:
  unreal payload:
  texture budget:
  sound / image bridge:
  return / reveal anchor:
  representation boundary:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Subjective Imagination / Dream / Hallucination Table

| Insert use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Imagined outcome | character briefly sees a possible result | "when she looks at the sealed door, it opens in her imagination for 1 second; return to the real door still closed" | fake continuity, full alternate scene, prophecy claim | viewer sees the imagined result and the real unchanged state |
| Dream fragment | a sleeping or drifting state creates one altered rule | "dream status: hallway depth stretches while the same red exit sign stays fixed; return on eye-open cue" | random surreal montage, copied dream sequence | one impossible rule is legible |
| Hallucinated object shift | perception changes one object without diagnosing the character | "subjective perception: the locket briefly pulses like it is breathing; character blinks and it is still metal" | mental-illness stereotype, violent threat cliche, monster reveal | object shift, blink, and normal return are clear |
| Intrusive fear image | fear projects a brief image, then reality corrects it | "0.7-second fear image of water under the door; return to dry floor and her held breath" | gore, trauma exploitation, prolonged shock insert | subjective fear and reality correction are bounded |
| Name-free fallback | same mechanism with no film, director, or famous dream reference | "one subjective owner, one trigger, one impossible payload, one return anchor" | prestige dream references, surreal style soup | prompt works after all reference names are removed |

### Minimum Subjective Unreality Prompt Block

```text
Reference use, not surreal style: subjective insert controls one impossible perception only.
Subjective owner: courier in the present hallway.
Trigger cue: she stares at the sealed door handle for two beats.
Subjective status: imagined fear image, not objective reality and not a diagnosis.
Reality boundary: viewer discovers it is unreal at the return.
Unreal payload: for 0.8 seconds, dark water appears to seep under the door.
Texture budget: only room tone drops and the water reflection is slightly too smooth; no extra monsters, no warped faces, no random symbols.
Return / reveal anchor: hard cut back to the same dry floor, same door handle, her breath held.
Forbidden: no copied dream sequence, horror filter, mental-illness stereotype, gore, full alternate scene, prophecy claim, or additional impossible events.
Review: subjective owner, trigger, unreal payload, reality correction, texture budget, return anchor, and non-stigmatizing boundary are clear.
```

## Unreliable Perception / Reality Reveal Edit Prompt Card

Use this when a prompt asks for unreliable perception, mistaken POV, red herring, false continuity, withheld geography, reality reveal, misdirection, or "the viewer thinks X, then realizes Y." The reveal should correct one specific false inference, not cheat the scene.

```text
unreliable_reveal_id:
platform / mode:
scene:
viewer knowledge plan:
scene-specific job:

unreliable perception / reveal contract:
  evidence status:
  false cue:
  allowed false inference:
  viewer knowledge state:
  correction beat:
  truth anchor:
  timing / hold:
  no-cheat boundary:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Unreliable Perception / Reality Reveal Table

| Reveal use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Mistaken object scale | close framing hides true size | "macro shot makes the metal ring look huge; correction cut reveals it is a small key ring on the desk" | impossible resize, continuity error | same object is corrected by scale/context |
| Withheld geography | first angle hides spatial relation | "first shot suggests footsteps behind the door; correction angle reveals they are on a phone speaker beside the door" | fake geography, new prop appearing late | sound source/geography correction is legible |
| Red-herring cue | one cue implies wrong cause | "red warning light suggests alarm; correction beat shows it is a copier error light" | arbitrary twist, extra suspects | false inference and truth anchor are both visible |
| Character-mistaken POV | viewer shares character's limited view | "from her angle the coat looks like a person; when she steps right, it is only a coat on a chair" | jump scare, object teleport, hidden monster | movement reveals the same object honestly |
| Name-free fallback | same reveal logic with no film/director reference | "one false cue, one allowed inference, one correction angle, one truth hold" | famous twist imitation, copied reveal scene | prompt works after all reference names are removed |

### Minimum Unreliable Perception Prompt Block

```text
Reference use, not twist imitation: reveal controls one corrected inference only.
Evidence status: viewer and character share a mistaken limited view.
False cue: from the doorway, a dark coat on a chair reads like a standing person.
Allowed inference: someone is waiting in the room.
Viewer knowledge state: viewer is misled with the character until the correction beat.
Correction beat: she steps one pace right; the angle reveals the chair legs and coat sleeve.
Truth anchor: hold 1 second on the same coat, same chair, empty room.
Forbidden: no object teleport, hidden extra person, jump-scare cut, copied famous twist, impossible geography, or new evidence appearing only after the reveal.
Review: false cue, false inference, correction movement, truth anchor, hold time, and no-cheat boundary are visible.
```

## Object Clue / Evidence Insert Prompt Card

Use this when a prompt asks for clue insert, evidence close-up, important prop, red herring, document clue, trace mark, missing object, continuity clue, or payoff object. The insert should make one information payload readable and later usable; it should not become arbitrary prop decoration or forged proof.

```text
clue_insert_id:
platform / mode:
scene:
clue status:
scene-specific job:

object clue / evidence contract:
  clue status:
  attention cue:
  readable payload:
  owner / viewer:
  payoff beat:
  red-herring boundary:
  evidence / forgery boundary:
  timing / hold:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Object Clue / Evidence Insert Table

| Insert use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| True object clue | one mark or mismatch carries later information | "brief insert: brass key tag shows number 14; detective later matches it to locker 14" | random prop close-up, unreadable number | number is readable and later used |
| Missing-object clue | absence is the payload | "hold on empty ring-shaped dust mark where the clock used to sit" | extra explanatory text, new missing object invented later | absence is visible and connected to later question |
| Red herring | object invites wrong inference but has bounded correction | "red scarf is framed as suspicious; later payoff shows it belongs to the victim's coat, not the suspect" | arbitrary false lead, no correction beat | false lead and correction are both clear |
| Trace / residue clue | material trace proves contact or path | "one wet footprint crosses dry tile; character notices before stepping around it" | fake forensic certainty, procedural how-to | trace, surface contrast, and reaction align |
| Name-free fallback | same mechanism without famous mystery references | "one readable object payload, one attention cue, one later payoff, no extra clue clutter" | detective-brand imitation, puzzle montage | prompt works after reference names are removed |

### Minimum Object Clue / Evidence Prompt Block

```text
Reference use, not mystery decor: clue insert controls one readable payload only.
Clue status: true object clue, not official evidence.
Attention cue: focus pull from her hand to brass key tag.
Readable payload: tag number 14, readable for 0.8 seconds.
Owner / viewer: viewer sees it first; character notices after a half-beat.
Payoff beat: later she looks toward locker 14.
Red-herring boundary: no extra suspicious objects, no puzzle wall, no fake police label.
Evidence boundary: fictional prop clue only; no real case, real institution, official seal, or forged document claim.
Review: clue status, attention cue, readable number, viewer/character timing, payoff beat, and non-forgery boundary are clear.
```

## Wardrobe / Costume Clue Prompt Card

Use this when a prompt asks for a costume clue, wardrobe change, uniform signal, disguise tell, class/status clothing detail, damaged garment, missing accessory, continuity wardrobe detail, or payoff garment. The clothing should carry one readable story function; it should not become fashion styling, brand imitation, or an iconic costume copy.

```text
wardrobe_clue_id:
platform / mode:
scene:
garment status:
scene-specific job:

wardrobe / costume clue contract:
  garment status:
  wardrobe payload:
  attention cue:
  owner / viewer:
  social / character signal:
  payoff beat:
  continuity relation:
  copy / brand guard:
  timing / hold:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Wardrobe / Costume Clue Table

| Wardrobe use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Uniform/status clue | one garment detail changes authority or access | "security jacket is missing its metal badge; guard hesitates at the checkpoint" | real agency marks, fake official logo | missing badge and access consequence are visible |
| Disguise tell | clothing almost matches but one detail betrays it | "borrowed coat fits too short at the wrists; character pulls sleeves down before entering" | famous disguise scene, comic reveal | mismatch is readable and affects behavior |
| Damage/trace clue | fabric wear shows prior contact or struggle | "dark wet stain on left cuff catches light; later it matches the leaking pipe" | gore clue, forensic certainty | stain, side, and later match are legible |
| Social/character signal | clothing encodes work, class, role, or self-image | "pressed shirt under scuffed work jacket; collar stays neat while cuffs are frayed" | fashion moodboard, brand styling | signal is specific, not just stylish |
| Name-free fallback | same wardrobe logic with no designer/film reference | "one garment detail, one attention cue, one story consequence, no iconic silhouette" | copied costume identity, logo, label | prompt works after reference names are removed |

### Minimum Wardrobe / Costume Clue Prompt Block

```text
Reference use, not fashion styling: wardrobe clue controls one readable garment payload only.
Garment status: borrowed uniform disguise, not real official uniform.
Wardrobe payload: jacket is one size too short at both cuffs, exposing a different blue shirt underneath.
Attention cue: character pulls both sleeves down as the checkpoint guard looks over.
Owner / viewer: viewer notices first; guard notices after the sleeve movement.
Payoff beat: guard asks for the missing badge before opening the gate.
Continuity relation: same short cuffs remain visible in the next shot.
Copy / brand guard: no real agency badge, logo, fashion label, iconic film costume, superhero silhouette, or recognizable uniform design.
Review: garment status, cuff mismatch, attention cue, viewer/guard timing, payoff beat, continuity, and no brand/IP leakage are visible.
```

## Makeup / Hair / Body-State Clue Prompt Card

Use this when a prompt asks for makeup clue, hair-state change, face/body-state cue, fatigue/sweat/dust trace, smudged makeup, continuity mark, period or role look, disguise tell, or payoff appearance detail. The appearance layer should carry one readable story function; it should not become a beauty filter, medical diagnosis, injury spectacle, or identity imitation.

```text
appearance_clue_id:
platform / mode:
scene:
appearance status:
scene-specific job:

makeup / hair / body-state clue contract:
  appearance status:
  appearance payload:
  attention cue:
  owner / viewer:
  story consequence:
  continuity mark:
  identity / safety boundary:
  timing / hold:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Makeup / Hair / Body-State Clue Table

| Appearance use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Fatigue / environment trace | one non-graphic trace proves prior route or pressure | "one soot smudge under left cheekbone; she wipes it but it remains" | illness diagnosis, injury spectacle | trace location and story consequence are visible |
| Continuity mark | one side-specific mark carries across shots | "small blue paint fleck remains on right eyebrow through the next cut" | mark jumping sides, new wounds | same side/zone stays consistent |
| Hair-state clue | hair condition signals time, stress, disguise, or change | "missing hairpin leaves one loose strand; partner notices before the gate opens" | glamour hair styling, celebrity haircut | hair detail changes a decision |
| Disguise tell | face/hair almost fits but one detail betrays it | "fake mustache edge lifts for half a second under harsh light" | real-person imitation, prosthetic tutorial | tell is visible without identity copying |
| Name-free fallback | same appearance logic without performer or film reference | "one readable appearance payload, one attention cue, one consequence, no beauty-filter drift" | actor likeness, iconic makeup, gore | prompt works after reference names are removed |

### Minimum Makeup / Hair / Body-State Prompt Block

```text
Reference use, not beauty filter or diagnosis: appearance clue controls one readable payload only.
Appearance status: continuity fatigue trace after moving through smoke, fictional and non-medical.
Appearance payload: one diagonal soot smudge under her left cheekbone and damp hair strands at the left temple.
Attention cue: she wipes the left cheek with her sleeve; the smudge remains visible.
Owner / viewer: viewer notices first; partner notices after the wipe.
Story consequence: partner realizes she came through the burned stairwell and chooses the service exit.
Continuity mark: soot stays under the left cheekbone and damp hair stays at the left temple in the next shot.
Identity / safety boundary: no wound detail, blood, gore, illness diagnosis, prosthetic identity swap, celebrity likeness, race/age/weight change, or glamour beauty filter.
Review: appearance status, soot/hair payload, attention cue, story consequence, continuity side, and identity/safety boundary are visible.
```

## Hand / Object Interaction Clue Prompt Card

Use this when a prompt asks for a hand clue, prop pickup, object handoff, secret pass, pocketing, palming, button press, touch evidence, hidden-object reveal, or prop ownership change. The interaction should prove one contact/state change; it should not become fake contact, object teleport, impossible hand anatomy, or real-world concealment instruction.

```text
interaction_clue_id:
platform / mode:
scene:
interaction status:
scene-specific job:

hand / object interaction clue contract:
  hand owner:
  object identity / payload:
  start state:
  contact proof:
  transfer / conceal-reveal action:
  end state:
  attention cue:
  continuity side:
  payoff / consequence:
  safety / fake-contact boundary:
  timing / hold:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Hand / Object Interaction Clue Table

| Interaction use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Ownership proof | hand, side, and object remain linked | "left hand pinches the red keycard between thumb and index finger; card stays in left hand after the cut" | hand swap, object drift | owner, side, and object survive the beat |
| Handoff / transfer | object visibly leaves one hand and enters another | "sender places folded note into receiver's right palm; receiver closes fingers before cut" | teleport handoff, hidden edit | start, contact, receiver, and end state are visible |
| Conceal / reveal clue | object is hidden or revealed with a named knowledge change | "thumb slides coin under map edge; later same thumb lifts map corner to reveal it" | real theft tutorial, unexplained reveal | conceal action and reveal relation are clear |
| Button / pressure proof | contact visibly changes object/environment state | "index finger depresses green switch; switch stays down and door light changes after contact" | fake touch, late effect | compression and consequence align |
| Name-free fallback | same interaction logic without source-scene reference | "one hand owner, one object, one contact proof, one final state" | famous insert imitation, hand montage | prompt works after reference names are removed |

### Minimum Hand / Object Interaction Prompt Block

```text
Reference use, not hand montage: interaction clue controls one contact-proven state change only.
Hand owner: courier's left hand owns the brass token.
Object payload: brass token with one red paint scratch.
Start state: token lies flat on the desk beside the map.
Contact proof: left thumb and index finger pinch the token; token casts a moving shadow as it lifts.
Transfer / conceal-reveal action: left hand slides the token under the lower-right corner of the paper map.
End state: map corner rises slightly, token edge remains barely visible for 0.5 seconds.
Attention cue: short insert shot from character POV; room sound drops except paper scrape.
Continuity side: same left hand and same lower-right map corner in the next shot.
Payoff / consequence: later she lifts that same map corner to show the token before choosing the side door.
Safety / fake-contact boundary: fictional screen action only; no real theft, pickpocket method, lock bypass, extra fingers, hand swap, object teleport, hidden cut, or fake touch.
Review: hand owner, object, pinch contact, conceal path, final state, continuity side, and payoff are visible.
```

## Object Placement / Set-Dressing Clue Prompt Card

Use this when a prompt asks for background clue, set dressing clue, object placement, room detail, misplaced item, missing object, repeated decor, before/after room state, furniture arrangement, or payoff prop in the environment. The set dressing should carry one readable placement relation; it should not become decorative clutter.

```text
set_dressing_clue_id:
platform / mode:
scene:
placement status:
scene-specific job:

object placement / set-dressing clue contract:
  placement status:
  placement payload:
  baseline state:
  changed / payoff state:
  viewer priority cue:
  owner / viewer:
  spatial relation:
  payoff beat:
  clutter boundary:
  timing / hold:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Object Placement / Set-Dressing Clue Table

| Placement use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Out-of-place object | one object violates the room's pattern | "all files are stacked square except one red folder angled toward the door" | clutter wall, many suspicious props | single anomaly is visible |
| Missing-object absence | absence carries the payload | "dust outline shows where a small radio used to sit" | explanatory label, invented object later | absence and later payoff align |
| Changed room state | before/after placement proves time or action | "first shot: chair tucked under desk; later chair is pulled toward window" | continuity error, random reset | baseline and changed state are both shown |
| Social/status set dressing | arrangement encodes hierarchy or pressure | "one clean chair faces three worn visitor chairs across the desk" | generic wealth mood, brand decor | placement relation signals status |
| Name-free fallback | same set-dressing logic without film reference | "one placement payload, one priority cue, one later payoff, no extra decor clutter" | copied room, production-design imitation | prompt works after reference names are removed |

### Minimum Object Placement / Set-Dressing Prompt Block

```text
Reference use, not decorative background: set dressing clue controls one placement relation only.
Placement status: true changed-state clue, not general atmosphere.
Placement payload: desk chair is pulled 30 cm away from the desk and angled toward the back window.
Baseline state: earlier shot shows the same chair tucked squarely under the desk.
Viewer priority cue: medium-wide frame holds 1 second; warm desk lamp catches the chair legs while other desk items stay static.
Owner / viewer: viewer notices before the character; character notices after following floor scratches.
Spatial relation: chair angle points toward the back window, not the door.
Payoff beat: later she checks the window latch instead of the desk drawer.
Clutter boundary: no extra suspicious props, no wall of clues, no labels, no new furniture, no brand decor, no puzzle-room montage.
Review: placement status, baseline, changed chair angle, viewer priority, payoff, and clutter boundary are visible.
```

## Spatial Path / Blocking Clue Prompt Card

Use this when a prompt asks for a blocking clue, path reveal, hidden route, blocked exit, threshold clue, actor movement revealing space, corridor geography, eyeline-to-target, or "character discovers where to go." The route should prove one spatial change or decision; it should not become teleporting, false geography, random wandering, or camera movement without actor path proof.

```text
blocking_clue_id:
platform / mode:
scene:
route status:
scene-specific job:

spatial path / blocking clue contract:
  route status:
  start position:
  obstruction / reveal:
  actor path proof:
  end position:
  screen direction / geography:
  attention cue:
  payoff / consequence:
  false-geography boundary:
  timing / hold:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Spatial Path / Blocking Clue Table

| Blocking use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Hidden route reveal | actor movement changes what can be seen | "she steps left from doorway; shelf gap reveals narrow service stairs" | teleport reveal, new door appearing | movement and new route are linked |
| Blocked path | obstruction changes decision | "rolling cart blocks corridor center; she turns to side passage instead" | random obstacle, impossible geography | obstacle and redirected path are visible |
| Threshold clue | crossing a boundary reveals or hides information | "before crossing glass door, sign reflection hides EXIT; after crossing, exit arrow becomes readable" | magic text, unreadable signage | boundary and reveal are clear |
| Corrected geography | path proves relation between two spaces | "camera holds as he walks from archive desk to window latch in one continuous left-to-right path" | jump cut, false adjacency | route proves spatial relation |
| Name-free fallback | same blocking logic without director or film reference | "one start point, one obstruction/reveal, one actor path, one end point, one payoff" | famous staging imitation, wandering | prompt works after reference names are removed |

### Minimum Spatial Path / Blocking Prompt Block

```text
Reference use, not wandering: blocking clue controls one route reveal only.
Route status: hidden service route becomes visible.
Start position: courier stands in the archive doorway, screen-left, facing into the room.
Obstruction / reveal: tall shelf blocks the back-right stairwell from the doorway angle.
Actor path proof: she takes three slow steps left along the desk edge, then stops; her body shift opens the sightline through a shelf gap.
End position: from her new position, the narrow stairwell is visible in the back-right corner.
Screen direction / geography: movement stays leftward; stairwell remains back-right, not a new door.
Attention cue: her eyeline lands on the stairwell handle; camera holds 1 second before she turns.
Payoff / consequence: she chooses the stairwell instead of the front corridor.
False-geography boundary: no teleport, no new room appearing, no impossible hallway, no random cutaway, no camera-only reveal without actor movement.
Review: route status, start/end positions, obstruction, actor path, geography, eyeline, and payoff are visible.
```

## Eyeline / Gaze-Target Clue Prompt Card

Use this when a prompt asks for eyeline clue, gaze shift, look-off, glance to object, watched target, offscreen target, answer shot, character notices something, viewer sees what they see, or "her eyes reveal the clue." The gaze should create one readable knowledge relation; it should not become random eye movement, target ambiguity, missing answer shot, or false spatial relation.

```text
eyeline_clue_id:
platform / mode:
scene:
gaze / target status:
scene-specific job:

eyeline / gaze-target clue contract:
  gaze owner:
  gaze cue:
  target status:
  answer shot:
  knowledge state:
  spatial relation:
  timing / hold:
  payoff / consequence:
  random-gaze boundary:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Eyeline / Gaze-Target Clue Table

| Eyeline use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Visible target clue | gaze directs viewer to one visible object | "her eyes shift down-right to the red keycard on desk; next shot confirms keycard" | random eye flicker, no answer shot | gaze and target align |
| Offscreen target | look-off creates controlled uncertainty | "he looks screen-left toward unseen corridor; answer shot delayed 1 second" | target ambiguity forever, false geography | delay and later answer are clear |
| Viewer-ahead gaze | viewer sees target before character | "viewer sees door handle move first; character's gaze catches it half-beat later" | impossible knowledge, late prop | viewer/character timing is legible |
| Misread gaze | gaze invites wrong inference then corrects | "she looks at coat; answer shot first reads as person, then reveals chair" | cheat twist, object teleport | false cue and correction share target |
| Name-free fallback | same eyeline logic without film reference | "one gaze owner, one target status, one answer shot, one knowledge state" | famous gaze imitation, eye montage | prompt works after reference names are removed |

### Minimum Eyeline / Gaze-Target Prompt Block

```text
Reference use, not eye acting: eyeline clue controls one knowledge relation only.
Gaze owner: courier's eyes drive the clue; viewer shares her look.
Gaze cue: her eyes shift down-right, then her chin follows slightly.
Target status: visible target, not offscreen: red keycard half-hidden under the map edge.
Answer shot: cut to insert of the same red keycard for 0.7 seconds.
Knowledge state: viewer and character learn the target together.
Spatial relation: keycard is down-right from her position, on the desk, not a new object.
Payoff / consequence: she reaches toward the keycard in the next beat.
Random-gaze boundary: no wandering eye movement, no extra targets, no unexplained look-off, no reversed screen direction, no target appearing only after the gaze.
Review: gaze owner, gaze direction, target, answer shot, knowledge state, spatial relation, and payoff are visible.
```

## Reaction / Response Ownership Clue Prompt Card

Use this when a prompt asks for reaction shot, response beat, character realizes something, listener reaction, offscreen-cue reaction, object-triggered response, held silence after a reveal, or "show their reaction." The reaction should prove one information or decision change; it should not become generic acting, filler close-up, random emotion, or a reaction with no visible trigger.

```text
reaction_clue_id:
platform / mode:
scene:
trigger / response status:
scene-specific job:

reaction / response clue contract:
  trigger owner:
  response owner:
  reaction timing:
  micro-behavior proof:
  knowledge shift:
  coverage / camera rule:
  object / space pressure:
  payoff / consequence:
  generic-acting boundary:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Reaction / Response Ownership Clue Table

| Reaction use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Cue-to-reaction | one cue causes one visible response | "at safe click, her hand freezes on strap before her eyes move" | random worried face, missing cue | cue and response align |
| Pre-reaction | response begins before others understand | "his fingers stop before the sentence ends" | melodrama, impossible knowledge | early response has a readable cause |
| Offscreen cue reaction | offscreen source stays hidden while reaction proves it matters | "door buzz remains offscreen; hold on guard's breath stop" | reveal source too soon, unclear sound | source and listener relation are clear |
| Object pressure reaction | prop state carries the reaction | "he cannot look up; thumb presses envelope corner flat" | filler cutaway, prop clutter | object handling changes meaning |
| Name-free fallback | same response logic without actor/film reference | "one trigger, one response owner, one micro-behavior, one knowledge shift" | actor imitation, vague natural acting | prompt works after reference names are removed |

### Minimum Reaction / Response Ownership Prompt Block

```text
Reference use, not generic acting: reaction clue controls one knowledge shift only.
Trigger owner: offscreen door lock gives one soft click at 3 seconds; viewer and character hear it.
Response owner: courier owns the reaction; camera holds on her, not the door.
Reaction timing: half-beat after the click, her breath stops before her eyes move.
Micro-behavior proof: right hand releases the shoulder strap; chin lowers slightly.
Knowledge shift: she realizes the door is already unlocked and unsafe.
Coverage / camera rule: locked medium close-up for 1.2 seconds; no cutaway hiding hand or face.
Object / space pressure: closed door remains behind her left shoulder.
Payoff / consequence: she steps backward instead of reaching for the handle.
Generic-acting boundary: no random sad face, no tears, no speech, no extra clue, no unrelated glance, no reaction without the click.
Review: trigger, response owner, timing, hand/breath tell, knowledge shift, door pressure, and payoff are visible/audible.
```

## Held Silence / Pause Clue Prompt Card

Use this when a prompt asks for silence, held pause, quiet tension, room tone, sound drop, withheld answer, listening beat, post-reveal pause, or "let the moment breathe." The pause should prove one decision or listening state; it should not feel like missing audio, dead air, slow filler, or generic dramatic quiet.

```text
held_pause_id:
platform / mode:
scene:
pause / sound status:
scene-specific job:

held silence / pause clue contract:
  silence owner:
  removed layers:
  remaining cue:
  pressure object / space:
  decision state:
  visual stillness rule:
  release cue:
  payoff / consequence:
  dead-air boundary:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Held Silence / Pause Clue Table

| Pause use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Decision pause | quiet proves a choice | "music drops; only breath and room tone remain as she decides not to answer" | empty mute, melodrama | pause ends in a visible decision |
| Listening pause | removed layers make one source readable | "crowd bed fades; only elevator cable hum remains" | random ambience cut | remaining cue has a source |
| Object-pressure pause | visible prop carries silence | "hold on sealed envelope while both voices stop" | filler cutaway | object relation changes meaning |
| Post-reveal pause | viewer registers consequence | "after latch opens, no music; key ring sways once" | jump-scare sting, extra clue | pause lets new state register |
| Name-free fallback | same pause logic without film/sound reference | "one silence owner, removed layers, remaining cue, pressure object, decision state" | famous quiet scene imitation | prompt works after reference names are removed |

### Minimum Held Silence / Pause Prompt Block

```text
Reference use, not dead air: held pause controls one decision state only.
Silence owner: courier owns the pause; viewer hears from her position.
Removed layers: music and corridor chatter drop out at 4 seconds.
Remaining cue: only her breath, faint room tone, and one slow key-ring sway remain.
Pressure object / space: sealed door stays in frame behind her right shoulder.
Decision state: she chooses not to knock.
Visual stillness rule: locked medium close-up; body stays still except breath lowering and fingers closing around strap.
Release cue: pause ends when the key-ring stops moving.
Payoff / consequence: she turns away from the door.
Dead-air boundary: no full mute, no music swell, no extra dialogue, no new clue, no random sad face, no empty hold with no visible decision.
Review: silence owner, removed layers, remaining cue, pressure object/space, decision state, release cue, and payoff are visible/audible.
```

## Sound Perspective / Distance Clue Prompt Card

Use this when a prompt asks for distant sound, muffled sound, offscreen source, approaching sound, sound behind a door/wall, hidden source, room-to-room cue, sound perspective, or "we hear something nearby." The sound should prove one spatial clue; it should not become generic ambience, score, random drone, or a source that teleports into view.

```text
sound_distance_id:
platform / mode:
scene:
source / distance status:
scene-specific job:

sound perspective / distance clue contract:
  audio source status:
  listener point:
  distance:
  obstruction / filter:
  acoustic quality:
  reveal policy:
  image consequence:
  mix priority:
  generic-audio boundary:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Sound Perspective / Distance Clue Table

| Sound-distance use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Offscreen hidden source | source stays outside frame but locates space | "muffled elevator motor behind left wall, source not shown" | generic drone, visible machine | viewer knows direction/source status |
| Obstructed source | barrier filters the sound | "voice is low and dull through closed metal door" | clean studio voice, random reverb | filter matches barrier |
| Approaching source | distance changes over time | "footsteps start faint beyond corridor, grow clearer but stay offscreen" | teleport jump, music swell | acoustic change matches approach |
| Listener-point shift | hearing follows a character or camera position | "inside car: traffic is dampened; outside hood shot: traffic grows louder" | accidental hearing POV switch | mix matches listener/camera point |
| Name-free fallback | same spatial-audio logic without film reference | "one source status, one listener point, one distance/obstruction, one reveal policy" | famous sound-scene imitation | prompt works after reference names are removed |

### Minimum Sound Perspective / Distance Prompt Block

```text
Reference use, not ambience: sound perspective controls one spatial clue only.
Audio source status: diegetic offscreen elevator motor, hidden source.
Listener point: heard from courier's position inside the archive room, not from the hallway.
Distance: two rooms away, left of frame.
Obstruction / filter: behind a closed metal fire door; low, muffled, slightly vibrating.
Acoustic quality: when she cracks the inner door open, the hum becomes clearer and higher, but still distant.
Reveal policy: do not show the elevator or machine; keep source offscreen this shot.
Image consequence: she turns left toward the service corridor instead of the front desk.
Mix priority: elevator hum sits above room tone but below breath and cloth movement.
Generic-audio boundary: no suspense score, no random drone, no visible machinery, no loud close-up sound, no source teleport, no unexplained reverb.
Review: source status, listener point, distance, obstruction, acoustic change, hidden-source policy, and changed behavior are audible/visible.
```

## Offscreen Sound Reveal / Misdirection Clue Prompt Card

Use this when a prompt asks for offscreen sound, hidden source, voice-off, sound misdirection, source reveal, unseen threat, sound behind a door, sound that seems to be one thing but is another, or "we hear it before we see it." The sound should create one controlled source assumption and one fair correction; it should not become generic ambience, unresolved ambiguity, source teleport, or a cheat reveal.

```text
offscreen_sound_reveal_id:
platform / mode:
scene:
source assumption / reveal status:
scene-specific job:

offscreen sound reveal contract:
  assumed source:
  actual source:
  listener point:
  offscreen / misread duration:
  acoustic clue:
  correction beat:
  reveal evidence:
  listener reaction:
  payoff / consequence:
  unfair-cheat boundary:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Offscreen Sound Reveal / Misdirection Table

| Reveal use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Delayed source reveal | sound starts offscreen then image answers | "metal scraping behind door for 1s, then reveal janitor cart wheel" | source teleport, no answer | sound and revealed source match |
| False source assumption | viewer/character misreads source briefly | "footsteps seem human; correction shows loose ceiling pipe tapping" | cheat twist, unrelated source | false cue and correction share acoustic evidence |
| Voice-off reveal | unseen voice creates identity assumption | "old woman's voice from next room; later reveal voice from radio speaker" | identity bait without proof | reveal object produces same voice |
| Hidden source kept hidden | source remains unseen but changes behavior | "offscreen dog bark stays behind fence; character stops at gate" | unresolved random noise | hidden source affects action |
| Name-free fallback | same offscreen-source logic without film reference | "one assumed source, one actual source, one delay, one correction beat" | famous sound twist imitation | prompt works after reference names are removed |

### Minimum Offscreen Sound Reveal Prompt Block

```text
Reference use, not ambience: offscreen sound controls one fair source correction only.
Assumed source: viewer and courier first assume the scraping behind the metal door is a person moving.
Actual source: janitor cart wheel stuck against the door frame.
Listener point: heard from courier's position in the archive room.
Offscreen / misread duration: keep source offscreen for 1.2 seconds.
Acoustic clue: irregular metal scrape and soft wheel squeak, not footsteps.
Correction beat: camera holds as courier opens door 20 cm.
Reveal evidence: cart wheel rubs the threshold in sync with the same scrape.
Listener reaction: courier exhales and lowers her hand from the alarm button.
Payoff / consequence: she chooses to push the cart aside instead of calling for help.
Unfair-cheat boundary: no unrelated jump scare, no new source appearing late, no impossible sound-source match, no unresolved noise, no music sting replacing the cue.
Review: assumed source, actual source, delay, acoustic clue, correction beat, listener reaction, and payoff are visible/audible.
```

## Sound Bridge / Prelap Clue Prompt Card

Use this when a prompt asks for a sound bridge, prelap, audio leading the next scene, voice beginning before the cut, room tone entering before the image, J-cut-like audio lead, or "hear it before we cut there." The sound should authorize one transition and be answered by the next image; it should not become random ambience, unexplained audio, generic music glue, or a scene change with no payoff.

```text
sound_bridge_prelap_id:
platform / mode:
scene pair:
transition job:
source status:

sound bridge / prelap contract:
  outgoing image:
  incoming audio source:
  lead duration:
  audio content / material:
  transition point:
  incoming image answer:
  image relation:
  payoff / changed expectation:
  mix priority:
  accidental-audio boundary:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Sound Bridge / Prelap Table

| Bridge use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Incoming location bridge | next scene sound enters before cut | "school bell begins over empty kitchen, then cut to hallway" | random ambience, no location answer | next image proves bell source |
| Prelap dialogue | line starts before speaker appears | "woman's line begins over closed elevator doors; cut reveals her in lobby" | disembodied voice with no owner | speaker/source appears and continues |
| Mood continuity | music/room tone carries relation across cut | "same piano phrase starts under street image, then reveal apartment piano" | generic score glue | music source or function is answered |
| Contrast bridge | sound contradicts outgoing image then resolves | "cheering crowd starts over silent empty pool; cut to packed gym" | cheat mismatch | contrast resolves in next image |
| Name-free fallback | same transition logic without film reference | "one outgoing image, one incoming sound, one lead duration, one image answer" | famous transition imitation | prompt works after reference names are removed |

### Minimum Sound Bridge / Prelap Prompt Block

```text
Reference use, not ambience: sound bridge controls one transition only.
Outgoing image: courier stands alone in the archive room, hand still on the metal door.
Incoming audio source: train brake squeal from the next scene's platform.
Lead duration: train brake begins 0.8 seconds before the cut.
Audio content / material: high metal squeal, then low station rumble; no music.
Transition point: cut when courier lowers her hand from the door.
Incoming image answer: cut to subway platform where the same train enters frame from screen-right.
Image relation: the sound pulls us from private hesitation into public movement.
Payoff / changed expectation: courier is already leaving the building rather than opening the door.
Mix priority: train brake leads over room tone, then station crowd replaces archive hum after the cut.
Accidental-audio boundary: no random whoosh, no unexplained sound, no music sting, no source mismatch, no extra dialogue, no sound continuing without visual answer.
Review: outgoing image, incoming audio, lead duration, cut point, image answer, payoff, and mix replacement are visible/audible.
```

## Postlap / Audio-Tail Clue Prompt Card

Use this when a prompt asks for an L-cut, postlap, audio tail, previous-scene dialogue continuing over the next shot, outgoing room tone carrying into the next image, or "let the old sound continue after the cut." The old sound should reframe one new image and then clearly fade, cut, or be replaced; it should not become muddy carryover, accidental overlap, unresolved ambience, or generic emotional music.

```text
postlap_audio_tail_id:
platform / mode:
scene pair:
tail job:
source status:

postlap / audio-tail contract:
  outgoing image:
  outgoing audio source:
  carry duration:
  audio tail content / material:
  incoming image:
  image relation:
  cutoff / replacement point:
  new scene sound takeover:
  payoff / reframed meaning:
  mix priority:
  muddy-carryover boundary:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Postlap / Audio-Tail Table

| Tail use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Dialogue tail | old line continues over new image | "last words continue 1s over empty platform, then fade under station tone" | ownerless narration, extra dialogue | old speaker/source is known and tail ends |
| Room-tone tail | old space lingers after cut | "archive hum carries 0.7s over street image, then traffic replaces it" | unresolved ambience | replacement is audible |
| Emotional reframe | old sound changes how next image reads | "door knock continues over her packed bag" | generic sad score | new image is reinterpreted by old sound |
| Contrast tail | old sound collides with new image then yields | "party laughter carries over hospital corridor, then cuts to monitor beep" | tasteless shock, muddy mix | contrast and replacement are clear |
| Name-free fallback | same L-cut logic without film reference | "one outgoing sound, one carry duration, one incoming image relation, one cutoff/replacement" | famous transition imitation | prompt works after reference names are removed |

### Minimum Postlap / Audio-Tail Prompt Block

```text
Reference use, not overlap: postlap controls one reframing tail only.
Outgoing image: courier closes the archive door.
Outgoing audio source: metal door latch click and archive room hum.
Carry duration: latch click tail and hum continue for 0.8 seconds after the cut.
Incoming image: exterior sidewalk at night, courier already walking away.
Image relation: old latch sound makes the new image read as escape, not a normal street exit.
Cutoff / replacement point: archive hum fades out when her shoe hits the wet pavement.
New scene sound takeover: quiet traffic and one distant bus brake replace the archive hum.
Payoff / reframed meaning: she has chosen to leave the locked room unresolved.
Mix priority: latch tail is audible above traffic for the first half-second only.
Muddy-carryover boundary: no music sting, no extra voiceover, no indefinite hum, no unexplained audio source, no overlapping sounds that hide the pavement step.
Review: outgoing source, carry duration, incoming image relation, cutoff/replacement, payoff, and clean mix takeover are audible/visible.
```

## Audio Match Cut / Sonic Match Clue Prompt Card

Use this when a prompt asks for an audio match cut, sonic match, sound-shape match, "one sound becomes another," a sound matched across two locations, or a transition where different sources briefly sound alike. The match should connect one outgoing sound shape to one incoming source, then reveal the difference; it should not become a random whoosh, generic sound bridge, impossible identical audio, or confusing source swap.

```text
audio_match_cut_id:
platform / mode:
scene pair:
match job:
source status:

audio match cut contract:
  outgoing image:
  outgoing sound source:
  outgoing sound shape:
  sonic cut / blend point:
  incoming matching source:
  incoming image answer:
  difference cue:
  payoff / changed meaning:
  mix priority:
  mismatch boundary:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Audio Match Cut / Sonic Match Table

| Match use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Rhythm match | two sources share pulse pattern | "scanner double-beep cuts to turnstile double-chirp" | random beep, no image answer | rhythm matches, sources differ |
| Timbre match | two sources share brief texture | "metal scrape becomes train brake squeal" | impossible identical sound | new source adds identifying cue |
| Attack match | two sounds share start impact | "door slam cuts to gavel strike" | loudness-only smash | attack aligns and meaning changes |
| Ambience match | room tone briefly resembles another place | "archive hum becomes subway tunnel hum" | generic ambience glue | new location source becomes legible |
| Name-free fallback | same sonic-match logic without film reference | "one outgoing sound shape, one incoming matching source, one difference cue" | famous transition imitation | prompt works after reference names are removed |

### Minimum Audio Match Cut Prompt Block

```text
Reference use, not transition effect: audio match cut controls one sonic match only.
Outgoing image: courier scans a red keycard at the archive door.
Outgoing sound source: card scanner denial tone.
Outgoing sound shape: two short high electronic beeps, equal spacing, dry close sound.
Sonic cut / blend point: cut exactly on the second beep.
Incoming matching source: subway turnstile approval chirp with the same two-pulse rhythm.
Incoming image answer: green turnstile screen, courier stepping through frame-right.
Difference cue: incoming chirp is brighter and followed by a mechanical gate click and tile-station reverb.
Payoff / changed meaning: failed private access becomes public escape route.
Mix priority: matched beep/chirp is foreground for 0.5 seconds, then station ambience takes over.
Mismatch boundary: no random whoosh, music sting, unrelated sound, impossible identical source, hidden image answer, or extra dialogue explaining the cut.
Review: outgoing sound shape, cut point, matching incoming source, difference cue, image answer, payoff, and clean mix takeover are audible/visible.
```

## Performance / Acting Style Anchor Prompt Card

Use this when a prompt cites an actor, performance tradition, acting mode, film role, director-performer pairing, or "subtle acting" reference. The anchor should control one observable behavior layer only, not a celebrity likeness, voice, role identity, or famous mannerism.

```text
performance_anchor_id:
platform / mode:
anchor name or source:
allowed behavior layer:
scene-specific job:

performance anchor contract:
  source evidence:
  allowed mechanism:
  micro-behavior cue:
  gaze rule:
  reaction owner:
  silence action:
  blocking / status change:
  forbidden transfers:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Performance / Acting Anchor Table

| Performance anchor use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Micro-behavior anchor | hidden pressure shown through a small visible tell | "borrow only restrained micro-behavior: fingers stop smoothing the folder before the line ends" | actor likeness, voice, signature tic, famous role | cue is visible and changes meaning |
| Gaze / reaction anchor | who owns the reaction and when eye contact changes | "listener avoids eye contact until the forbidden word, then looks back once" | copied scene, catchphrase, celebrity mannerism | trigger, gaze rule, and reaction owner align |
| Silence-action anchor | pause performs a choice: decide, refuse, conceal, measure, absorb | "hold two seconds as she decides not to answer; breath lowers, hand tightens" | empty mute, theatrical pause, melodramatic face | silence ends in a visible decision or status change |
| Name-free fallback | same mechanism with no actor, role, or film name | "restrained performance: one hand stop, one avoided look, one final direct look" | prestige acting names, role imitation, broad mood word | prompt still works after the name is removed |

### Minimum Performance Anchor Prompt Block

```text
Reference use, not imitation: performance anchor controls behavior timing only.
Allowed mechanism: restrained refusal shown through one hand stop, avoided eye contact, and a final direct look.
Name-free fallback: she wants the folder back but cannot ask; her fingers stop smoothing the table before the line ends; she avoids eye contact for two beats, then looks directly back once and chooses silence.
Forbidden: no actor likeness, voice imitation, famous role, catchphrase, signature mannerism, copied scene, theatrical crying, or vague "emotional acting."
Review: want/resistance are clear; micro-behavior is visible; gaze changes once at the named beat; silence produces a decision or status change.
```

## Production Design / Worldbuilding Style Anchor Prompt Card

Use this when a prompt cites a film world, production designer, set, architecture, prop, costume, faction, vehicle, signage system, or object-focused design reference. The anchor should control one design layer only: how the space/object tells story, not the whole recognizable world.

```text
design_anchor_id:
platform / mode:
anchor name or source:
allowed design layer:
scene-specific job:

design anchor contract:
  source evidence:
  allowed mechanism:
  spatial rule:
  material logic:
  prop / set-dressing function:
  wear / history state:
  forbidden transfers:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
```

### Production Design / Worldbuilding Anchor Table

| Design anchor use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Spatial-rule anchor | space layout reveals power, access, work, ritual, pressure, or social order | "borrow only spatial rule: high archive shelves create blocked sightlines; one locked service door controls escape" | famous set layout, franchise architecture, iconic room geometry | viewer can read access, obstacle, and status from space |
| Prop-function anchor | prop exists because it is used, worn, repaired, carried, hidden, traded, or controlled | "every object has a job: stamped folder grants access; cracked badge fails at scanner; repair tape marks repeated use" | iconic prop, logo, faction mark, collectible design | prop function changes action or status, not just decoration |
| Material/history anchor | surfaces show use, class, age, weather, repair, labor, or institutional neglect | "brushed metal is polished only at hand-contact zones; corners are chipped; labels are sun-faded" | signature palette, branded patina, generic grime | material wear matches touch, climate, work, and story state |
| Name-free fallback | same design mechanism with no film/designer/franchise name | "bureaucratic archive world: repeated labels, locked doors, repaired folders, worn hand-contact metal" | IP imitation, style collage, copied costume/prop/architecture | prompt still works after the reference name is removed |

### Minimum Design Anchor Prompt Block

```text
Reference use, not imitation: production-design anchor controls spatial rule and prop function only.
Allowed mechanism: bureaucratic archive space where access is controlled by doors, labels, badges, and repaired paper records.
Name-free fallback: narrow archive aisles block sightlines; one locked service door controls escape; stamped folder grants access; cracked badge fails at scanner; metal is polished only at hand-contact zones.
Forbidden: no copied franchise world, iconic prop, costume silhouette, set layout, faction mark, logo, signature palette, or decorative clutter.
Review: space shows access/obstacle/status; props have visible jobs; material wear matches use; no recognizable IP design leaks into the scene.
```

## Sound / Music Style Anchor Prompt Card

Use this when a prompt cites a sound designer, composer, film score, soundscape, soundtrack, trailer sound, or famous audio moment as a reference. The anchor should control one audible layer only and must not copy a score, motif, sound logo, or recognizable sonic signature.

```text
audio_anchor_id:
platform / mode:
clip duration:
anchor name or source:
allowed audio layer:
scene-specific job:

audio anchor contract:
  source evidence:
  allowed mechanism:
  listening point:
  primary audio event:
  mix hierarchy:
  silence / density curve:
  sound-image timing:
  forbidden transfers:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Sound / Music Anchor Table

| Audio anchor use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Listening-point anchor | whose hearing owns the moment and which layers are filtered | "borrow only subjective listening: hallway ambience drops behind the character's hearing; breath and sleeve rustle stay close" | character/device recipe, tinnitus imitation as decoration, full soundscape copy | hearing owner, removed layers, remaining cue, and visible reaction align |
| Primary-event anchor | one timed sound event changes the image meaning | "one offscreen elevator bell at 3s leads the character's look; no other foreground cue" | famous cue, sound logo, jump-scare sting, motif | cue time, source status, listener reaction, and image consequence are clear |
| Mix-hierarchy anchor | foreground/support/absent layer contract | "foreground: metal key scrape; support: low room tone; absent: music, drone, crowd, narration" | full soundtrack imitation, generic ambience stack | primary cue is not masked and unwanted layers stay absent |
| Silence-curve anchor | removed layers plus one remaining cue | "room tone thins until only breath remains, then paper rustle breaks the silence" | mute-as-tension, missing audio, copied silence trick | removed layers, remaining cue, and story turn are audible/visible |
| Music-pulse anchor | tempo or pulse relationship without melody/motif copying | "low two-pulse rhythm supports footsteps; no melody; stop before the reveal" | score theme, melody, chord progression, recognizable instrumentation | pulse supports timing without becoming a copied score |
| Name-free fallback | same audio mechanism with no person, film, score, or source name | "offscreen bell precedes the look by 0.5s; breath remains foreground; no score" | prestige naming, sonic signature copy, style soup | prompt still works after the anchor name is removed |

### Minimum Sound / Music Anchor Prompt Block

```text
Reference use, not imitation: audio anchor controls listening point only.
Allowed mechanism: one subjective listening shift followed by one primary offscreen cue.
Name-free fallback: at 3s hallway ambience drops behind her hearing; breath and sleeve rustle stay close; one offscreen elevator bell leads her look by 0.5s; no music.
Forbidden: no copied score, melody, motif, sound logo, creature/device recipe, famous cue, full soundtrack imitation, jump-scare sting, extra composer names, or generic ambience stack.
Review: hearing owner is clear; removed layers and remaining cue are audible; primary cue triggers visible reaction; audio stays synced and does not copy a recognizable sonic identity.
```

## Action Director / Fight Style Anchor Prompt Card

Use this when a prompt cites an action director, stunt coordinator, fight team, martial-arts film, action franchise, game cinematic, or famous fight as a reference. The anchor is allowed only after it is reduced to one fictional screen-action job and kept away from real-world stunt or fighting instruction.

```text
action_anchor_id:
platform / mode:
clip duration / aspect:
anchor name or source:
allowed action layer:
scene-specific job:

action anchor contract:
  source evidence:
  allowed mechanism:
  geography roadmap:
  contact / near-miss proof:
  receiver or environment response:
  rhythm curve:
  weapon / prop / body-weight behavior:
  camera proof job:
  safety boundary:
  forbidden transfers:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Action Director / Fight Anchor Table

| Action anchor use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Geography anchor | arena roadmap before pressure: exits, levels, obstacles, threat order | "borrow only the arena roadmap: show doorway, table barrier, attacker left, shield carrier right before impact" | copied set piece, exact route, famous location, hidden geography | viewer can name route, obstacle, threat, and escape state |
| Contact-proof anchor | attack vector -> contact/near-miss relation -> receiver/environment response | "borrow only contact proof: overlap at shield edge, half-step recoil, table cup spills, attacker resets guard" | real strike instruction, injury target, unsafe method, hidden impact | path, proof frame, consequence, and recovery are readable |
| Rhythm-oscillation anchor | pressure rise, recoil/pause, surprise beat, renewed threat, recovery cost | "borrow only rhythm oscillation: burst, half-second recoil breath, surprise object cue, renewed pressure" | franchise tone, brutality texture, gun/weapon identity, costume | intensity changes state rather than staying constant |
| Weapon/prop-weight anchor | preload, lag, acceleration, impact/near-miss, delayed response, settle | "heavy prop lags behind hand, accelerates once, forces stance adjustment, settles after the beat" | real weapon handling, tactical instruction, injury detail | weight is proven by load, delayed response, braking, and recovery |
| Group hierarchy anchor | threat order, zone ownership, one active danger at a time, readable relay | "three opponents stay in zones; only one attacks at a time; background threat prepares but waits" | crowd chaos, copied combo chain, every body moving at once | viewer reads active threat, waiting threat, and changed spacing |
| Camera proof-job anchor | camera proves geography, contact, receiver response, or recovered spacing | "camera stabilizes for the proof frame; tiny jolt only after contact; widen for recovered spacing" | shaky blur hiding choreography, random closeups, cut-away impact | camera does one proof job without hiding the required action |
| Fictional danger anchor | vulnerability cue, near-miss/block proof, consequence, recovery, no how-to | "prop passes close enough to lift sleeve and snap shelf tag; she recoils and exit becomes blocked" | gore, injury detail, stunt method, real fight instruction | danger comes from geography, near-miss, consequence, and recovery |
| Name-free fallback | same mechanism with no person, film, team, or franchise name | "show arena first; one contact-proof beat; recoil breath; prop weight settles; no copied combo" | empty prestige naming, style soup, borrowed violence identity | prompt still works after the anchor name is removed |

### Action Anchor Failure Diagnosis

| Failure | Likely cause | Minimum retry delta |
| --- | --- | --- |
| Fight becomes generic flailing | Anchor name had no action layer lock | Remove extra names; choose one layer: geography, contact proof, rhythm, prop weight, group hierarchy, camera proof, or danger |
| Impact looks fake | Contact proof is missing | Add attack vector, proof frame, receiver/environment response, and recovery hold |
| Action becomes unsafe how-to | Prompt described real technique or injury method | Rewrite as fictional screen effect: visible vector, near-miss/block, consequence, recovery; remove operational details |
| Camera hides the beat | Camera was asked to be energetic instead of useful | Assign one camera proof job and protect the proof frame from shake, blur, foreground cover, or cutaway |
| It copies a famous fight | Copy guard was absent | Replace exact combo, weapon identity, set-piece route, brutality texture, and plot situation with an original arena and mechanism |
| Group fight turns chaotic | Threat hierarchy was missing | Limit active attackers; state zones, order, waiting threats, and spacing changes |
| Reference leaks into costume or tone | Anchor role was too broad | State that the action anchor controls only one screen-action mechanism, not costume, palette, story, gore level, or edit rhythm |

### Minimum Action Director / Fight Anchor Prompt Block

```text
Reference use, not imitation: action anchor controls screen-action clarity only.
Allowed mechanism: arena roadmap followed by one contact-proof beat and one recovery breath.
Name-free fallback: 8-second fictional screen-action beat; 0-2s show narrow archive aisle, blocked exit, attacker left, defender right; 2-4s attacker swings a padded prop across the aisle; proof frame shows prop crossing shield edge, not hidden by blur; 4-6s defender recoils into shelf, tag snaps loose, dust falls; 6-8s both reset with exit newly blocked.
Forbidden: no copied combo, famous set piece, real fighting/stunt instruction, injury target, gore, brutality texture, weapon tutorial, extra attackers, shaky blur hiding impact, or franchise costume/palette.
Review: geography is readable before pressure; contact/near-miss relation is visible; receiver/environment response proves force; rhythm has recovery breath; final spacing/state changed; prompt remains fictional and non-operational.
```

## Cinematographer / Camera Style Anchor Prompt Card

Use this when a prompt cites a cinematographer, director, film, lens brand, camera format, or famous frame as a camera-language reference. The anchor is useful only after it is reduced to one spatial job that can be reviewed in the output.

```text
camera_anchor_id:
platform / mode:
clip duration / aspect:
anchor name or source:
allowed camera layer:
scene-specific job:

camera anchor contract:
  source evidence:
  allowed mechanism:
  lens-distance relation:
  camera height / angle:
  shot size and subject scale:
  composition relation:
  movement trigger, if any:
  depth / focus behavior:
  forbidden transfers:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Cinematographer / Camera Anchor Table

| Camera anchor use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Lens-distance anchor | focal-length class plus physical camera distance and background scale | "long-lens camera from far back; same chest-up subject size; hallway background presses closer behind her" | lens number as magic word, copied frame, false compression claim | camera feels distant, subject size holds, background scale relation is visible |
| Wide companion camera | controlled wide view close enough for intimacy while preserving surrounding world | "close companion camera with a mild wide view; keep face away from frame edges; room geometry remains readable" | caricature warp, forced quirk, copied actor blocking | viewer feels near the subject and space remains legible |
| Camera-height anchor | low, eye-level, overhead, or shoulder-height relation tied to power, vulnerability, observation, or geography | "eye-level camera at table height keeps hands, folder, and exit line in one readable plane" | prestige low angle, arbitrary drone view, famous composition copy | height explains status or space instead of decorating |
| Composition-balance anchor | negative space, foreground/background layers, frame-within-frame, center/edge pressure | "subject held on left third; locked doorway occupies right background as the pressure object" | exact iconic layout, production design, signature palette | frame relation names subject, pressure object, and empty/blocked zone |
| Movement anchor | movement starts only after a visible trigger and ends in new information | "slow dolly-in begins when the envelope seal changes; end frame isolates hand and door together" | random push-in, zoom/dolly confusion, copied camera move | start trigger, path, subject relation, and end information are visible |
| Depth/focus anchor | focus behavior or depth separation tied to attention change | "foreground hand stays sharp while background doorway remains readable but soft; rack focus only after offscreen bell" | meaningless shallow depth, erased story object, brand-name look | focus state guides attention without hiding required geography |
| Name-free fallback | same camera mechanism with no person, film, lens brand, or format name | "respectful medium-telephoto portrait feel from mid-distance; chest-up subject; background lights appear closer; no face warp" | empty cinematographer name stack, style soup, copied shot | prompt still works after the anchor name is removed |

### Camera Anchor Failure Diagnosis

| Failure | Likely cause | Minimum retry delta |
| --- | --- | --- |
| Output only looks generically cinematic | Anchor name had no camera layer lock | Remove the name or keep it as evidence only; write lens-distance, height, subject size, and background relation |
| Face or body distorts unexpectedly | Wide/close relation was under-specified | Add camera distance, edge guard, subject size, and face/body rendering gate |
| Background compression is wrong | Prompt used lens word without camera position | State far camera position, same subject size, and background appearing closer |
| Famous frame gets copied | Composition guard was missing | Replace exact layout with function: subject, pressure object, empty/blocked zone, and original setting |
| Movement feels random | No visible trigger or end information | Add movement trigger, path, speed, subject relation, end frame, and review proof |
| Camera anchor leaks into color or acting | Role boundaries were absent | State that the camera anchor controls camera/spatial relation only and cannot change palette, costume, plot, performance, or edit rhythm |

### Minimum Cinematographer / Camera Anchor Prompt Block

```text
Reference use, not imitation: camera anchor controls spatial relation only.
Allowed mechanism: respectful medium-telephoto portrait feel from mid-distance; chest-up subject; background corridor appears closer behind her while doorway remains readable.
Name-free fallback: camera is physically several meters back, eye-level, locked-off; subject remains chest-up; background scale presses inward; face shape stays natural.
Forbidden: no copied frame, character, costume, production design, signature palette, exact blocking, living-artist imitation, extra cinematographer names, or style collage.
Review: camera distance feels mid/far, subject scale is stable, background relation is visible, face/body rendering matches the intent, and no camera-anchor leakage changes story, color, acting, or edit rhythm.
```

## Editor / Rhythm Style Anchor Prompt Card

Use this when a prompt cites an editor, director, film, trailer, music video, or sequence as a rhythm reference. The name is allowed only after it is reduced to one timing layer and one scene-specific job.

```text
rhythm_anchor_id:
platform / mode:
clip duration:
anchor name or source:
allowed rhythm layer:
scene-specific job:

rhythm anchor contract:
  source evidence:
  allowed mechanism:
  beat permission rule:
  hold / cut density:
  sound-image relation:
  performance pulse:
  forbidden transfers:
  name-free fallback:
  compatibility check:
  review proof:

positive prompt wording:
negative / positive lock:
review check:
retry if failed:
```

### Editor / Rhythm Style Anchor Table

| Rhythm anchor use | Allowed mechanism | Prompt wording | Do not transfer | Review check |
| --- | --- | --- | --- | --- |
| Performance-led editor anchor | cut and hold follow breath, glance, hand stop, or decision beat | "borrow only performance-led timing: cut after her breath stops, not on a fixed music beat" | famous dialogue, actor mannerism, scene structure, broad editor imitation | each cut or hold follows a named performance pulse |
| Sound-led transition anchor | prelap, tail, room tone, Foley cue, or silence drop gives the image meaning | "borrow only one sound-led reveal: elevator bell arrives before the visual answer, then hold reaction" | exact plot reveal, recognizable sound motif, montage identity | sound arrives in the named window and changes the following image |
| Dense montage anchor | a short density burst after setup, then a proof hold | "allow three sub-second inserts only after the object is identified; final 1s hold proves changed state" | copied cut order, famous graphic sequence, branded iconography | setup remains legible and the burst resolves into one readable state |
| Reaction-hold anchor | delayed reaction ownership and viewer registration time | "borrow only a 1s reaction hold after the offscreen cue; listener owns the meaning" | copied face, line, blocking, or exact reverse-shot pattern | viewer can identify trigger, reaction owner, and new relation |
| Action-clarity anchor | cut only after path, contact/near-miss, receiver response, or recovery | "cut only after route is clear, contact is proven, and recoil settles" | real stunt method, injury detail, shaky impact hiding geography | route, proof frame, consequence, and recovery survive the edit |
| Name-free fallback | same mechanism with no person/film/source name | "phone buzz leads the look by 0.5s; cut only after hand stops; final 1s hold on changed envelope" | empty prestige naming, style collage, unexplained reference stack | prompt still works after the anchor name is removed |

### Rhythm Anchor Failure Diagnosis

| Failure | Likely cause | Minimum retry delta |
| --- | --- | --- |
| Output becomes vague style soup | Anchor name had no layer lock | Remove extra names; keep one allowed rhythm layer and one name-free fallback |
| It copies a famous sequence shape | Forbidden transfers were too broad or absent | Add cut-pattern copy guard: no exact cut order, plot reveal, dialogue, montage identity, or signature structure |
| Rhythm fights the scene | Compatibility check was missing | Match layer to scene type: performance pulse for dialogue, geography proof for action, density burst for montage |
| Model ignores the reference | Mechanism wording relied on the name | Rewrite as visible/audible cues: cut after breath stop, sound prelap, proof hold, density cap |
| Reference leaks into color, acting, or camera | Anchor role was not isolated | State that the rhythm anchor controls timing only and cannot change palette, costume, identity, acting style, or camera language |

### Minimum Editor / Rhythm Anchor Prompt Block

```text
Reference use, not imitation: rhythm anchor controls timing only.
Allowed mechanism: one sound-led reveal followed by a 1s reaction hold.
Name-free fallback: phone buzz leads the character's look by 0.5s; cut only after her hand stops; final 1s hold on the changed envelope.
Forbidden: no copied scene, dialogue, plot twist, exact montage structure, signature palette, living-artist imitation, or extra editor/director names.
Review: sound cue arrives before the look; hand stop authorizes the cut; reaction hold is readable; the scene remains original and the anchor does not leak into color, costume, identity, or plot.
```

## Shot Handoff / First-Last Frame Prompt Card

Use this when an AI video sequence is generated in separate clips, when a platform accepts first/last frame references, or when a storyboard needs continuity across cuts. The handoff should not copy the previous frame as decoration; it should inherit a precise action state, body pose, prop relation, screen direction, and story state.

```text
handoff_id:
platform / mode:
shot A output / last frame:
shot B reference / first frame:

handoff contract:
  previous end state:
  inherited anchors:
    identity / costume:
    prop / weapon:
    body pose / action phase:
    screen direction:
    eyeline / target:
    scene layout:
    lighting / color relation:
    sound tail, if supported:
  shot B new information:
  allowed camera change:
  allowed scale / crop change:
  forbidden reset:

bridge type:
  match-on-action:
  eyeline answer:
  screen-direction continuation:
  sound bridge:
  graphic / object match:
  contrast or rupture, if intentional:

review checks:
  first frame inherits last-frame state:
  action continues from the same phase:
  screen direction / eyeline remains legible:
  prop position and grip do not jump:
  new shot adds specific information:
  no pose reset / identity drift / style reset:
validation status:
```

### Shot Handoff Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| next clip restarts the action | previous end state not named | write the exact outgoing pose, action phase, prop relation, and body momentum |
| character flips left/right | screen-direction bridge missing | lock travel direction, camera side, eyeline target side, and object side |
| prop jumps hand or location | prop relation absent | name hand, grip, distance to body/target, and whether it is raised/lowered/pointing |
| cut feels like a new scene | inherited scene anchors absent | carry over door/table/floor mark/background depth, light direction, or weather |
| first/last frame reference causes stiff copy | allowed camera/action change absent | allow crop/angle/scale shift while preserving pose phase and relation |
| match-on-action feels mismatched | action phase too vague | split outgoing and incoming phases: hand reaches -> cut -> same hand grips |
| eyeline answer is unclear | looker/target relation missing | lock who looks, where on screen they look, and what the next shot answers |
| style or grade resets | lighting/color relation not inherited | preserve source direction, color contrast, exposure level, and material response |

### Minimum Shot Handoff Prompt Block

```text
Shot B starts from Shot A's last-frame state: same woman, same teal jacket, same brass scanner in her right hand, scanner already raised toward the locked door on screen-right.
Continue the same action phase: her wrist finishes lifting, the scanner beam lands on the door seam, and she leans one step forward.
Camera may cut from medium-wide to tighter over-shoulder, but stays on the same side of the corridor axis; door remains screen-right, her eyeline and scanner both point right.
Carry over cool corridor light and the low scanner hum for the first second.
New information: the tighter shot reveals a small red warning mark on the door seam.
Forbidden reset: no lowered scanner, no hand swap, no face/costume change, no reversed corridor, no new door, no style/grade reset.
Review: first frame inherits pose and prop relation; motion continues; rightward screen direction holds; new warning mark is revealed.
```

## Mechanical Deployment / Lock-State Prompt Card

Use this when a prop, armor piece, vehicle part, weapon, robot tool, creature shell, or set mechanism must unfold, telescope, assemble, transform, lock, or prove a new usable form. The goal is not "show a cool transformation"; the goal is a readable chain from stored state to stable state.

```text
deployment_id:
platform / mode:
clip duration:

mechanical deployment contract:
  form A / compact state:
  form B / deployed state:
  invariant core:
  mechanism family:
  source of added length / volume:
  trigger:
  stage chain:
    0-2s compact state and trigger:
    2-4s release / seams / primary unfold:
    4-6s secondary slide / telescope / rotation:
    6-8s alignment / lock / vibration damping:
  mass / center-of-mass change:
  regrip / support:
  lock proof:
  sound / material proof:

constraints:
  preserve:
  avoid:

review checks:
  before-state visible:
  parts come from named stored zones:
  active frontier stays visible:
  deployed form locks and settles:
  handling or weight changes after deployment:
  no soft morph / duplicate parts / instant skin swap:
validation status:
```

### Mechanical Deployment Failure Diagnosis

| Symptom | Likely missing field | Retry control |
| --- | --- | --- |
| instant finished object replaces the old one | stage chain missing | add release -> unfold/slide -> align -> lock windows |
| metal behaves like liquid skin | mechanism family absent | name hinged plates, telescoping rails, rotating collar, latch pins, cable tension, or nested panels |
| parts duplicate or grow from nowhere | source of added volume missing | state where panels were stored and how compact stacks unfold |
| final form jitters or changes after completion | lock proof missing | add latch click, seam closure, vibration damping, and a short stable hold |
| weapon/tool keeps same weight after extension | mass / center-of-mass field missing | add wrist dip, two-hand regrip, stance adjustment, shoulder brace, or settling recoil |
| camera hides the transformation | active frontier not protected | keep the active seam/rail/frontier in frame; no flash cloud covering the whole subject |
| prompt becomes a different design each second | invariant core missing | name the grip, face, emblem, chassis, color placement, or silhouette element that never changes |

### Minimum Mechanical Deployment Prompt

```text
8-second single shot. Compact wrist tool starts closed around the same black grip and silver hinge core.
At 2s the side seams release; nested metal plates unfold from the forearm housing, then two telescoping rails extend forward.
At 6s the rails align and lock with two small latch clicks; the user's wrist dips, then regrips with the other hand as the extended tool settles.
Camera stays medium-close on the active seam and grip; no full-body flash, no liquid morph, no duplicate parts, no new object appearing from offscreen.
Review: compact state, stored panels, staged extension, latch/settle, changed handling, and stable final silhouette.
```

## Knowledge Entries

### Editing And Platform Sources -> Split Screens Need Panel-Relation Contracts

Source / example -> StudioBinder split-screen film examples, Yale Film Analysis editing guide, Google DeepMind Veo prompt guide, and existing atlas screen/graphic insert controls.

Observation -> Split screen and multi-panel layouts are useful when they make a relation visible: simultaneity, contrast, cause/effect, delayed reaction, before/after, surveillance comparison, or parallel action. Editing sources frame cuts and juxtapositions as relationships between shots, while platform prompt guidance supports describing scene, camera, action, style, and timing. In AI video prompts, "split screen" is too vague unless panel count, panel ownership, and the timing relation are locked.

Mechanism -> A split-screen/multi-panel prompt should become a panel-relation contract: layout type -> panel count and geometry -> panel ownership -> temporal relation -> viewer priority cue -> sound/motion focus -> seam/border logic -> transition in/out -> forbidden collage behavior -> output review proof.

Executable control / prompt wording -> "Reference use, not collage: split-screen layout controls one simultaneous cause/effect relation only. Two vertical panels, stable border, equal width. Left panel shows courier at locked service door; right panel shows guard pressing the door-control button at the same moment; right panel has the brighter hand motion for 1 second, then left panel owns the reaction as the lock light changes. No third panel, moving borders, comic-book page layout, copied film reference, unrelated parallel action, tiny unreadable faces, mirrored duplicates, or sound from both panels competing at once. Review panel count, panel ownership, timing relation, viewer priority cue, seam stability, and changed state."

Applicable scenes -> AI video split-screen prompts, parallel action, phone calls, surveillance grids, before/after comparisons, expectation-vs-reality layouts, multi-panel storyboards, output review, and prompt preflight.

Misuse boundary -> Do not write "show multiple things happening at once" as a complete prompt. Do not use extra panels, unstable seams, tiny unreadable action, copied comic/page layouts, unrelated parallel action, or multiple competing sound owners. If every panel does not have a job, reduce the panel count.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Editing And Platform Sources -> Rapid Montages Need Beat-Function Chains

Source / example -> Yale Film Analysis editing guide, StudioBinder montage education, Google DeepMind Veo prompt guide, and existing atlas rhythm/cut-permission controls.

Observation -> Montage and rapid sequences compress, compare, escalate, or connect information through a chain of shots. Existing rhythm controls protect cut permission and density, but a rapid montage also needs a shot-count limit, beat order, and a final proof hold so the viewer can register what changed.

Mechanism -> A rapid montage prompt should become a beat-function chain: montage function -> shot/insert count -> ordered beats -> transition logic -> density curve -> sound/music relation -> final proof hold -> forbidden copied pattern/overload -> output review proof.

Executable control / prompt wording -> "Reference use, not montage identity: rapid sequence controls time compression only. 6-second montage, four shots maximum: empty metal case -> gloved hand selects tool -> red seal stamped -> case locked. One new visual fact per shot; no camera move during inserts; one soft metallic click carries across cuts. Final 1 second holds on the locked case and changed red seal. No copied famous montage, random micro-cuts, extra locations, unreadable inserts, text clutter, every cut on the music beat, or hidden final state. Review shot count, beat function, order, density budget, and final proof hold."

Applicable scenes -> AI video prep sequences, training fragments, clue bursts, trailer beats, time compression, contrast montages, action setup, output review, and retry diagnosis.

Misuse boundary -> Do not write "fast montage" or "dynamic rapid cuts" as a complete prompt. Do not let a short clip add many locations, text layers, camera moves, and plot events at once. If the final state cannot be held and inspected, reduce shot count.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Sound And Platform Sources -> Voiceover Needs Image-Relation Contracts

Source / example -> Yale Film Analysis guide sound index, StudioBinder voice-over education, Google DeepMind Veo prompt guide, and existing atlas sound-image / prompt-writing controls.

Observation -> Voiceover and narration belong to the sound-image relation: a voice can guide, reframe, contradict, withhold, or contextualize what is seen. Platform prompt guidance supports explicit voice, action, style, and sound-design fields, but AI video prompts often turn "add narration" into redundant exposition unless narrator status, source, timing, image relation, and mix priority are locked.

Mechanism -> A voiceover/narration prompt should become an image-relation contract: narrator status -> diegetic/non-diegetic source -> one information payload -> timing relative to image cue -> image relation -> mix priority -> redundancy guard -> name-free fallback -> output review proof.

Executable control / prompt wording -> "Reference use, not exposition dump: narration controls image relation only. Non-diegetic third-person narrator, calm and unnamed. Voice begins after the courier sees the sealed door; it withholds the reason and says one short line that reframes the pause. Voice is foreground for 1.5 seconds, then drops under room tone. No celebrity voice, actor imitation, copied narration style, repeated visible action, extra backstory, fake documentary authority, dialogue overlap, or emotion labels the face already shows. Review narrator status, start cue, single new information layer, image relation, mix priority, and non-redundancy."

Applicable scenes -> AI video prompts with voiceover, inner monologue, documentary narration, character memory, radio/phone/device voice, unreliable narration, output review, and retry diagnosis.

Misuse boundary -> Do not write "add cinematic narration" as a complete prompt. Do not use real narrator names, living-actor voice imitation, fake news authority, copied monologue style, or voiceover that repeats visible action. If the voice does not add, delay, contradict, or reframe one specific information layer, remove it.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Editing And Narrative Sources -> Unreliable Perception Needs Correction Beats

Source / example -> Yale Film Analysis editing guide, StudioBinder unreliable-narrator education, Google DeepMind Veo prompt guide, and existing atlas transition / subjective-unreality / prompt-writing controls.

Observation -> Editing, framing, sound, and viewpoint can control what the viewer knows and when a prior inference is corrected. Narrative sources around unreliable narration are useful only when translated into evidence status: whose view is incomplete, what cue is misleading, and what later shot or sound corrects it. In AI video prompts, "mislead the viewer" is too loose unless the false cue, allowed inference, correction beat, and truth anchor are all inspectable.

Mechanism -> An unreliable perception / reality reveal prompt should become a correction-beat contract: evidence status -> false cue -> allowed false inference -> viewer knowledge state -> correction beat -> truth anchor -> timing/hold -> no-cheat boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not twist imitation: reveal controls one corrected inference only. Evidence status: viewer and character share a mistaken limited view. From the doorway, a dark coat on a chair reads like a standing person, so the viewer may infer someone is waiting in the room. She steps one pace right; the angle reveals chair legs and coat sleeve. Hold 1 second on the same coat, same chair, empty room. No object teleport, hidden extra person, jump-scare cut, copied famous twist, impossible geography, or new evidence appearing only after the reveal. Review false cue, false inference, correction movement, truth anchor, hold time, and no-cheat boundary."

Applicable scenes -> AI video misdirection, suspense reveals, mistaken POV, red herrings, withheld geography, false sound source, object-scale correction, reality-reveal edits, output review, and retry diagnosis.

Misuse boundary -> Do not write "make a twist" or "mislead the viewer" as a complete prompt. Do not cheat by teleporting objects, adding late evidence, reversing geography without a bridge, or hiding the correction in blur. If the truth anchor cannot prove it is the same object/space/cue, simplify the reveal.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Mise-En-Scene And Platform Sources -> Object Clues Need Payload-Payoff Contracts

Source / example -> Yale Film Analysis mise-en-scene guide, StudioBinder Chekhov's Gun/setup-payoff education, Google DeepMind Veo prompt guide, and existing atlas object/prop continuity and reveal controls.

Observation -> Objects, props, costume, and setting details can carry story information, but a clue insert fails when the object is just decorative, unreadable, or has no later payoff. In AI video prompts, "show a clue" needs clue status, an attention cue, one readable payload, and a payoff/correction relation.

Mechanism -> An object clue / evidence insert prompt should become a payload-payoff contract: clue status -> attention cue -> one readable payload -> owner/viewer -> payoff beat -> red-herring boundary -> evidence/forgery boundary -> timing/hold -> output review proof.

Executable control / prompt wording -> "Reference use, not mystery decor: clue insert controls one readable payload only. True object clue, not official evidence. Focus pull from her hand to brass key tag; tag number 14 readable for 0.8 seconds. Viewer sees it first; character notices after a half-beat. Later she looks toward locker 14. No extra suspicious objects, puzzle wall, fake police label, real case, real institution, official seal, or forged document claim. Review clue status, attention cue, readable number, viewer/character timing, payoff beat, and non-forgery boundary."

Applicable scenes -> AI video mystery clues, prop inserts, evidence closeups, document details, missing-object beats, red herrings, continuity clues, output review, and retry diagnosis.

Misuse boundary -> Do not write "show a clue" as a complete prompt. Do not add many clue objects, unreadable text, fake official evidence, real institution marks, or red herrings without correction/payoff. If the clue cannot be read in a short hold, simplify the payload.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Costume And Platform Sources -> Wardrobe Clues Need Garment-Payload Contracts

Source / example -> Academy/Oscars costume design instructional guide and Academy costume-design article, Yale Film Analysis mise-en-scene guide, Google DeepMind Veo prompt guide, and existing atlas continuity/object-clue controls.

Observation -> Costume design communicates character, role, period, social position, work, and story state through specific garments and details. In AI video prompts, "make the outfit tell a story" is too broad unless the garment status, one visible wardrobe payload, attention cue, payoff/consequence, continuity relation, and no-copy boundary are explicit.

Mechanism -> A wardrobe / costume clue prompt should become a garment-payload contract: garment status -> one wardrobe payload -> attention cue -> owner/viewer timing -> social or character signal -> payoff beat -> continuity relation -> copy/brand guard -> output review proof.

Executable control / prompt wording -> "Reference use, not fashion styling: wardrobe clue controls one readable garment payload only. Borrowed uniform disguise, not real official uniform. Jacket is one size too short at both cuffs, exposing a different blue shirt underneath. Character pulls both sleeves down as the checkpoint guard looks over. Viewer notices first; guard notices after the sleeve movement. Guard asks for the missing badge before opening the gate. Same short cuffs remain visible in the next shot. No real agency badge, logo, fashion label, iconic film costume, superhero silhouette, or recognizable uniform design. Review garment status, cuff mismatch, attention cue, viewer/guard timing, payoff beat, continuity, and no brand/IP leakage."

Applicable scenes -> AI video wardrobe clues, disguise tells, uniform/access scenes, character status through clothing, damaged garment clues, costume continuity, social-role signaling, output review, and retry diagnosis.

Misuse boundary -> Do not write "stylish costume," "make wardrobe symbolic," or a named costume reference as a complete prompt. Do not copy iconic silhouettes, logos, fashion labels, real uniforms, or recognizable designer/faction looks. If the clothing detail has no readable consequence or continuity relation, simplify it to one payload.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Makeup/Hair And Platform Sources -> Appearance Clues Need Identity-Safe Payload Contracts

Source / example -> Academy/Oscars Costumes and Makeup activities guide, Yale Film Analysis mise-en-scene guide, Google DeepMind Veo prompt guide, and existing atlas wardrobe/object-continuity controls.

Observation -> Makeup and hairstyling help create character, mood, period, role, continuity, and story state, but in AI video prompts they drift easily into beauty styling, medical implication, injury spectacle, or identity imitation. The prompt needs to state what the appearance detail is allowed to prove and what it must not imply.

Mechanism -> A makeup / hair / body-state clue prompt should become an identity-safe appearance-payload contract: appearance status -> one readable payload -> attention cue -> owner/viewer timing -> story consequence -> continuity side/zone -> identity/safety boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not beauty filter or diagnosis: appearance clue controls one readable payload only. Continuity fatigue trace after moving through smoke, fictional and non-medical. One diagonal soot smudge under her left cheekbone and damp hair strands at the left temple. She wipes the left cheek with her sleeve; the smudge remains visible. Viewer notices first; partner notices after the wipe. Partner realizes she came through the burned stairwell and chooses the service exit. Soot stays under the left cheekbone and damp hair stays at the left temple in the next shot. No wound detail, blood, gore, illness diagnosis, prosthetic identity swap, celebrity likeness, race/age/weight change, or glamour beauty filter. Review appearance status, soot/hair payload, attention cue, story consequence, continuity side, and identity/safety boundary."

Applicable scenes -> AI video appearance clues, fatigue/environment traces, hair continuity, disguise tells, period/role looks, non-graphic aftermath, character-status cues, output review, and retry diagnosis.

Misuse boundary -> Do not write "makeup tells the story," "make her look tired," or a named actor/makeup reference as a complete prompt. Do not use makeup/hair to imply medical diagnosis, gore, real-person imitation, protected-trait transformation, or beauty retouching unless that is the explicit safe task. If the appearance detail has no story consequence or continuity side/zone, simplify it to one payload.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Insert-Shot And Platform Sources -> Hand/Object Interaction Needs Contact-Proof Contracts

Source / example -> Yale Film Analysis mise-en-scene guide, StudioBinder insert-shot education, Google DeepMind Veo prompt guide, and existing atlas object clue, action contact, and continuity controls.

Observation -> Insert shots can direct attention to small details, objects, hands, and text, while mise-en-scene treats props and gestures as story-bearing visible elements. In AI video prompts, "show the handoff" often fails through fake contact, hand swaps, object teleport, unclear ownership, or a hidden edit that skips the actual state change.

Mechanism -> A hand / object interaction clue prompt should become a contact-proof state-change contract: hand owner -> object payload -> start state -> contact proof -> transfer/conceal-reveal action -> end state -> attention cue -> continuity side -> payoff/consequence -> safety/fake-contact boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not hand montage: interaction clue controls one contact-proven state change only. Courier's left hand owns the brass token. Token lies flat on the desk beside the map. Left thumb and index finger pinch it; token casts a moving shadow as it lifts. Left hand slides the token under the lower-right corner of the paper map. Map corner rises slightly, token edge remains barely visible for 0.5 seconds. Short insert shot from character POV; room sound drops except paper scrape. Same left hand and same lower-right map corner in the next shot. Later she lifts that same map corner to show the token before choosing the side door. Fictional screen action only; no real theft, pickpocket method, lock bypass, extra fingers, hand swap, object teleport, hidden cut, or fake touch. Review hand owner, object, pinch contact, conceal path, final state, continuity side, and payoff."

Applicable scenes -> AI video handoff clues, prop ownership changes, object pickup inserts, button/contact proof, conceal-reveal beats, clue placement, continuity review, and retry diagnosis.

Misuse boundary -> Do not write "close-up of hands" or "secretly pass the object" as a complete prompt. Do not hide the contact in blur or a cut. Do not provide real concealment, theft, lock-bypass, or pickpocket instruction. If hand owner, contact proof, and final state are not visible, simplify the interaction.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Mise-En-Scene And Set-Dressing Sources -> Placement Clues Need Before/After State Contracts

Source / example -> Yale Film Analysis mise-en-scene guide, StudioBinder set-dressing education, Google DeepMind Veo prompt guide, and existing atlas object clue, hand/object interaction, and production-design controls.

Observation -> Decor, props, furniture, and spatial arrangement can shape how the viewer reads mood, relationship, status, and story information. In AI video prompts, "background clue" or "set dressing tells the story" often creates unsorted visual clutter unless one placement payload, viewer priority cue, baseline/changing state, and payoff relation are locked.

Mechanism -> An object placement / set-dressing clue prompt should become a before/after placement contract: placement status -> one placement payload -> baseline state -> changed/payoff state -> viewer priority cue -> owner/viewer timing -> spatial relation -> payoff beat -> clutter boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not decorative background: set dressing clue controls one placement relation only. True changed-state clue, not general atmosphere. Desk chair is pulled 30 cm away from the desk and angled toward the back window. Earlier shot shows the same chair tucked squarely under the desk. Medium-wide frame holds 1 second; warm desk lamp catches the chair legs while other desk items stay static. Viewer notices before the character; character notices after following floor scratches. Chair angle points toward the back window, not the door. Later she checks the window latch instead of the desk drawer. No extra suspicious props, wall of clues, labels, new furniture, brand decor, or puzzle-room montage. Review placement status, baseline, changed chair angle, viewer priority, payoff, and clutter boundary."

Applicable scenes -> AI video set-dressing clues, room-state changes, missing-object absence, background prop payoff, production-design prompts, object continuity review, and retry diagnosis.

Misuse boundary -> Do not write "background full of clues" or "rich set dressing" as a complete prompt. Do not add many suspicious objects, labels, clue boards, branded decor, or arbitrary room resets. If the baseline and changed/payoff state cannot both be inspected, simplify to one placement relation.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Blocking And Platform Sources -> Path Clues Need Actor-Proven Geography Contracts

Source / example -> Yale Film Analysis mise-en-scene guide, StudioBinder blocking/staging education, Google DeepMind Veo prompt guide, and existing atlas screen-direction, corridor/threshold, object-placement, and reveal controls.

Observation -> Blocking is not just where an actor stands; it controls how movement through space directs attention, reveals relationships, changes access, and proves geography. In AI video prompts, "character walks and discovers a route" often fails through teleporting, false adjacency, camera-only reveals, or wandering with no decision payoff.

Mechanism -> A spatial path / blocking clue prompt should become an actor-proven geography contract: route status -> start position -> obstruction/reveal -> actor path proof -> end position -> screen direction/geography -> attention cue -> payoff/consequence -> false-geography boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not wandering: blocking clue controls one route reveal only. Hidden service route becomes visible. Courier starts in archive doorway, screen-left, facing into room. Tall shelf blocks the back-right stairwell from doorway angle. She takes three slow steps left along the desk edge, then stops; her body shift opens sightline through shelf gap. From her new position, narrow stairwell is visible in back-right corner. Movement stays leftward; stairwell remains back-right, not a new door. Her eyeline lands on stairwell handle; camera holds 1 second before she turns. She chooses the stairwell instead of the front corridor. No teleport, new room appearing, impossible hallway, random cutaway, or camera-only reveal without actor movement. Review route status, start/end positions, obstruction, actor path, geography, eyeline, and payoff."

Applicable scenes -> AI video blocking prompts, corridor/threshold reveals, hidden-route clues, access/escape decisions, room geography, actor movement continuity, output review, and retry diagnosis.

Misuse boundary -> Do not write "character discovers a path" as a complete prompt. Do not let camera movement alone reveal the route when actor blocking is the proof. Do not add new doors, impossible adjacency, reversed screen direction, or geography that cannot be held long enough to inspect.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Editing And Platform Sources -> Eyeline Clues Need Gaze-Target Contracts

Source / example -> Yale Film Analysis editing guide on eyeline match, StudioBinder eyeline-match education, Google DeepMind Veo prompt guide, and existing atlas reaction ownership, shot/reverse-shot, object clue, and blocking controls.

Observation -> Eyeline matches connect a looker to a looked-at target and can construct convincing screen space. In AI video prompts, "she notices the clue" often fails as random eye movement unless the gaze owner, gaze direction, target status, answer shot, knowledge state, spatial relation, and payoff are explicit.

Mechanism -> An eyeline / gaze-target clue prompt should become a gaze-target contract: gaze owner -> gaze cue -> target status -> answer shot -> knowledge state -> spatial relation -> timing/hold -> payoff/consequence -> random-gaze boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not eye acting: eyeline clue controls one knowledge relation only. Courier's eyes drive the clue; viewer shares her look. Her eyes shift down-right, then her chin follows slightly. Visible target, not offscreen: red keycard half-hidden under the map edge. Cut to insert of the same red keycard for 0.7 seconds. Viewer and character learn the target together. Keycard is down-right from her position, on the desk, not a new object. She reaches toward the keycard in the next beat. No wandering eye movement, extra targets, unexplained look-off, reversed screen direction, or target appearing only after the gaze. Review gaze owner, gaze direction, target, answer shot, knowledge state, spatial relation, and payoff."

Applicable scenes -> AI video eyeline clues, gaze-to-object beats, offscreen target reveals, reaction shots, shot/reverse-shot prompts, object clue inserts, suspense notices, output review, and retry diagnosis.

Misuse boundary -> Do not write "her eyes reveal the clue" as a complete prompt. Do not allow eye drift without a target, answer shots without spatial relation, delayed targets with no payoff, or target objects appearing only after the gaze. If target status cannot be inspected, simplify to visible target and one answer shot.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Reaction Shot And Platform Sources -> Response Clues Need Trigger-Owner Contracts

Source / example -> StudioBinder reaction-shot and coverage guidance, Yale Film Analysis editing guide, Google DeepMind Veo prompt guide, and existing atlas listener reaction, eyeline, object clue, and dialogue timing controls.

Observation -> Reaction shots can pace, interpret, and redirect meaning after a cue, but AI video prompts often turn "show their reaction" into a generic emotional close-up. The missing fields are usually the trigger, response owner, timing relation, micro-behavior proof, and the knowledge or decision change created by the reaction.

Mechanism -> A reaction / response clue prompt should become a trigger-owner contract: trigger owner -> response owner -> reaction timing -> micro-behavior proof -> knowledge shift -> coverage/camera rule -> object/space pressure -> payoff/consequence -> generic-acting boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not generic acting: reaction clue controls one knowledge shift only. Offscreen door lock gives one soft click at 3 seconds; viewer and character hear it. Courier owns the reaction; camera holds on her, not the door. Half-beat after the click, her breath stops before her eyes move. Right hand releases the shoulder strap; chin lowers slightly. She realizes the door is already unlocked and unsafe. Locked medium close-up for 1.2 seconds; no cutaway hiding hand or face. Closed door remains behind her left shoulder. She steps backward instead of reaching for the handle. No random sad face, tears, speech, extra clue, unrelated glance, or reaction without the click. Review trigger, response owner, timing, hand/breath tell, knowledge shift, door pressure, and payoff."

Applicable scenes -> AI video reaction shots, offscreen-cue reactions, dialogue response beats, suspense reveals, object-triggered realizations, held-silence beats, output review, and retry diagnosis.

Misuse boundary -> Do not write "show their reaction" or "natural emotional reaction" as a complete prompt. Do not add reaction close-ups without a cue, micro-behavior, knowledge shift, and payoff. If the trigger cannot be seen or heard, make it visible/audible or remove the reaction shot.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Sound Perspective And Platform Sources -> Distance Cues Need Listener-Point Contracts

Source / example -> Yale Film Analysis sound guide, Oklahoma State open textbook on sound perspective, Google AI for Developers Veo audio prompting guidance, and existing atlas audio-event, subjective-listening, held-pause, offscreen-source, and review controls.

Observation -> Sound perspective ties volume, timbre, pitch, muffling, and spatial direction to where the source is relative to the listener/camera. Offscreen and obstructed sounds can locate unseen space, mislead or correct assumptions, and guide character behavior. In AI video prompts, "we hear something nearby" often becomes generic ambience or score unless the source status, listener point, distance/obstruction, acoustic quality, reveal policy, and image consequence are explicit.

Mechanism -> A sound perspective / distance clue prompt should become a listener-distance contract: audio source status -> listener point -> distance -> obstruction/filter -> acoustic quality -> reveal policy -> image consequence -> mix priority -> generic-audio boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not ambience: sound perspective controls one spatial clue only. Diegetic offscreen elevator motor, hidden source. Heard from courier's position inside the archive room, not from hallway. Source is two rooms away, left of frame, behind a closed metal fire door; low, muffled, slightly vibrating. When she cracks the inner door open, the hum becomes clearer and higher but still distant. Do not show the elevator or machine this shot. She turns left toward the service corridor instead of the front desk. Elevator hum sits above room tone but below breath and cloth movement. No suspense score, random drone, visible machinery, loud close-up sound, source teleport, or unexplained reverb. Review source status, listener point, distance, obstruction, acoustic change, hidden-source policy, and changed behavior."

Applicable scenes -> AI video offscreen sound clues, sound-behind-door beats, distance reveals, approaching threats, room-to-room geography, car/interior/exterior perspective shifts, output review, and retry diagnosis.

Misuse boundary -> Do not write "muffled sound," "nearby noise," or "cinematic ambience" as a complete prompt. Do not switch listener point accidentally between character, camera, room, and source. If distance or obstruction cannot be heard clearly, simplify to one source, one barrier, and one visible reaction.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Offscreen Sound And Platform Sources -> Reveals Need Source-Assumption Contracts

Source / example -> Yale Film Analysis sound guide, Oklahoma State open textbook on offscreen sound and sound-image relations, Google Cloud Veo prompt guide, and existing atlas sound perspective, reaction, held-pause, unreliable-reveal, and audio-event controls.

Observation -> Offscreen sound can make the viewer accept an unseen source, guide attention toward offscreen space, or withhold a source identity until a later reveal. Oklahoma State's sound chapter notes offscreen sound, source/visibility relations, and diegetic/non-diegetic boundary shifts as interpretive devices. In AI video prompts, "we hear something behind the door" often becomes generic ambience or an unfair jump scare unless the assumed source, actual source, offscreen duration, acoustic clue, correction beat, reveal evidence, and listener reaction are locked.

Mechanism -> An offscreen sound reveal / misdirection prompt should become a source-assumption contract: assumed source -> actual source -> listener point -> offscreen/misread duration -> acoustic clue -> correction beat -> reveal evidence -> listener reaction -> payoff/consequence -> unfair-cheat boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not ambience: offscreen sound controls one fair source correction only. Viewer and courier first assume the scraping behind the metal door is a person moving. Actual source: janitor cart wheel stuck against the door frame. Heard from courier's position in the archive room. Keep source offscreen for 1.2 seconds. Irregular metal scrape and soft wheel squeak, not footsteps. Camera holds as courier opens door 20 cm. Cart wheel rubs threshold in sync with the same scrape. Courier exhales and lowers her hand from the alarm button. She pushes the cart aside instead of calling for help. No unrelated jump scare, new source appearing late, impossible sound-source match, unresolved noise, or music sting replacing the cue. Review assumed source, actual source, delay, acoustic clue, correction beat, listener reaction, and payoff."

Applicable scenes -> AI video offscreen sound reveals, hidden-source suspense, false alarm beats, voice-off/source correction, sound-led misdirection, door/wall/corridor reveals, output review, and retry diagnosis.

Misuse boundary -> Do not write "mysterious sound" or "sound misdirection" as a complete prompt. Do not reveal a source whose material/timing does not match the sound. If the actual source cannot be shown or fairly inferred, keep the sound as hidden-source pressure instead of a twist.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Sound Bridge And Platform Sources -> Prelaps Need Transition-Permission Contracts

Source / example -> Yale Film Analysis sound guide on sound bridges, John August's pre-lap writing note, Google Cloud Veo prompt guide, and existing atlas dialogue timing, sound perspective, offscreen reveal, and audio-event controls.

Observation -> A sound bridge can lead into or out of a scene, and a prelap begins dialogue or another sound before the image of its source appears. Yale frames the sound bridge as an editing transition; John August notes prelap dialogue can be written when it helps a moment, but can be forgotten in production; Google Cloud recommends separate, explicit audio sentences for sound effects, ambient noise, and dialogue. In AI video prompts, "audio leads the next scene" often becomes accidental ambience or a random whoosh unless the outgoing image, incoming sound source, lead duration, transition point, image answer, and payoff are locked.

Mechanism -> A sound bridge / prelap prompt should become a transition-permission contract: outgoing image -> incoming audio source -> lead duration -> audio material/dialogue content -> transition point -> incoming image answer -> image relation -> payoff/changed expectation -> mix priority -> accidental-audio boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not ambience: sound bridge controls one transition only. Courier stands alone in archive room, hand still on metal door. Train brake from next scene begins 0.8 seconds before the cut: high metal squeal, then low station rumble, no music. Cut when courier lowers her hand. Incoming image answers sound: subway platform, same train entering from screen-right. The sound pulls us from private hesitation into public movement; payoff is that she is already leaving the building rather than opening the door. Train brake leads over room tone, then station crowd replaces archive hum after the cut. No random whoosh, unexplained sound, music sting, source mismatch, extra dialogue, or sound continuing without visual answer. Review outgoing image, incoming audio, lead duration, cut point, image answer, payoff, and mix replacement."

Applicable scenes -> AI video scene transitions, sound bridges, prelap dialogue, audio-led location changes, J-cut-like leads, mood/contrast bridges, trailer transitions, output review, and retry diagnosis.

Misuse boundary -> Do not write "sound bridge" or "prelap" as a complete prompt. Do not use generic music glue when the bridge needs a source, story job, or image answer. If the next image cannot prove the sound source or relation, remove the prelap or convert it to ambience within the same scene.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### L-Cut And Platform Sources -> Postlaps Need Tail-Replacement Contracts

Source / example -> Yale Film Analysis sound guide on sound bridges, DINFOS L-cut/J-cut editing guidance, Google Cloud Veo prompt guide, and existing atlas sound bridge, dialogue timing, sound perspective, and audio-event controls.

Observation -> Sound bridges can carry sound across scene boundaries. DINFOS describes an L-cut as audio from the current shot continuing over the next shot, while Google Cloud's prompt guide treats audio elements such as dialogue, sound effects, and ambient noise as explicit prompt material. In AI video prompts, "let the old sound carry over" often becomes accidental overlap unless the outgoing source, carry duration, incoming image relation, cutoff/replacement point, and new-scene sound takeover are locked.

Mechanism -> A postlap / audio-tail prompt should become a tail-replacement contract: outgoing image -> outgoing audio source -> carry duration -> audio tail content/material -> incoming image -> image relation -> cutoff/replacement point -> new-scene sound takeover -> payoff/reframed meaning -> mix priority -> muddy-carryover boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not overlap: postlap controls one reframing tail only. Courier closes archive door. Metal latch click and archive room hum continue for 0.8 seconds after the cut. Cut to exterior sidewalk at night, courier already walking away. Old latch sound makes the new image read as escape, not a normal street exit. Archive hum fades out when her shoe hits wet pavement; quiet traffic and one distant bus brake replace it. She has chosen to leave the locked room unresolved. Latch tail is audible above traffic for first half-second only. No music sting, extra voiceover, indefinite hum, unexplained audio source, or overlap hiding the pavement step. Review outgoing source, carry duration, incoming image relation, cutoff/replacement, payoff, and clean mix takeover."

Applicable scenes -> AI video L-cuts, postlaps, dialogue tails, room-tone tails, memory/contrast transitions, scene exits, sound-led reframing, output review, and retry diagnosis.

Misuse boundary -> Do not write "L-cut" or "let audio continue" as a complete prompt. Do not let the old audio continue indefinitely or mask the new scene's readable action. If the outgoing source cannot be identified or the replacement point cannot be reviewed, keep the audio within one scene.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Audio Match Cut Sources -> Sonic Matches Need Shape-And-Difference Contracts

Source / example -> Adobe match-cut guidance, Fedorishin/Lu/Setlur/Govindaraju audio match-cut research paper, Google Cloud Veo prompt guide, and existing atlas sound bridge, postlap, sound perspective, and audio-event controls.

Observation -> Adobe describes match cuts as linking scenes through similar visual or auditory elements and names audio match cuts as sound bridges using effects, dialogue, ambience, or music. The 2024 audio-match-cut paper defines audio match cuts as transitions where sounds from different sources merge into a briefly indistinguishable transition. Google Cloud's prompt guide requires explicit audio fields for sound effects, ambient noise, and dialogue. In AI video prompts, "match the sound into the next scene" often becomes random transition noise unless the outgoing sound shape, incoming source, cut/blend point, difference cue, image answer, and payoff are locked.

Mechanism -> An audio match cut / sonic match prompt should become a shape-and-difference contract: outgoing image -> outgoing sound source -> outgoing sound shape -> sonic cut/blend point -> incoming matching source -> incoming image answer -> difference cue -> payoff/changed meaning -> mix priority -> mismatch boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not transition effect: audio match cut controls one sonic match only. Courier scans a red keycard at archive door. Scanner denial tone: two short high electronic beeps, equal spacing, dry close sound. Cut exactly on the second beep to subway turnstile approval chirp with the same two-pulse rhythm. Incoming image answers source: green turnstile screen, courier stepping through frame-right. Difference cue: incoming chirp is brighter, followed by mechanical gate click and tile-station reverb. Payoff: failed private access becomes public escape route. Matched beep/chirp is foreground for 0.5 seconds, then station ambience takes over. No random whoosh, music sting, unrelated sound, impossible identical source, hidden image answer, or extra dialogue explaining the cut. Review outgoing sound shape, cut point, matching source, difference cue, image answer, payoff, and clean mix takeover."

Applicable scenes -> AI video audio match cuts, sonic transitions, matched Foley cuts, beep-to-beep edits, metal-to-metal transitions, ambience transformations, trailer transitions, output review, and retry diagnosis.

Misuse boundary -> Do not write "audio match cut" as a complete prompt. Do not match only loudness; specify rhythm, timbre, pitch, attack, duration, or material. If the incoming source cannot be identified by image or difference cue, use a normal sound bridge instead.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Sound And Platform Sources -> Held Pauses Need Silence-Owner Contracts

Source / example -> Yale Film Analysis sound guide, StudioBinder sound-design guidance on cinematic silence, Google DeepMind Veo prompt guide, and existing atlas audio-event, subjective-listening, dialogue-timing, reaction, and silence-density controls.

Observation -> Film-sound sources separate source, offscreen sound, sound perspective, layering, and sound design from generic atmosphere. Silence is usually not total mute; it works by removing selected layers while leaving one cue, room tone, breath, object tail, or perspective trace. In AI video prompts, "dramatic silence" often fails as missing audio or an empty slow hold unless the silence owner, removed layers, remaining cue, pressure object/space, decision state, and release cue are explicit.

Mechanism -> A held silence / pause clue prompt should become a silence-owner contract: silence owner -> removed layers -> remaining cue -> pressure object/space -> decision state -> visual stillness rule -> release cue -> payoff/consequence -> dead-air boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not dead air: held pause controls one decision state only. Courier owns the pause; viewer hears from her position. Music and corridor chatter drop out at 4 seconds. Only her breath, faint room tone, and one slow key-ring sway remain. Sealed door stays in frame behind her right shoulder. She chooses not to knock. Locked medium close-up; body stays still except breath lowering and fingers closing around strap. Pause ends when the key-ring stops moving. She turns away from the door. No full mute, music swell, extra dialogue, new clue, random sad face, or empty hold with no visible decision. Review silence owner, removed layers, remaining cue, pressure object/space, decision state, release cue, and payoff."

Applicable scenes -> AI video held pauses, suspense silence, post-reveal breath, restrained dialogue, listening beats, object-pressure pauses, room-tone cue sheets, output review, and retry diagnosis.

Misuse boundary -> Do not write "dramatic silence" or "let it breathe" as a complete prompt. Do not use full mute unless the platform/scene explicitly supports it and the visual proof remains clear. If no remaining cue or decision state can be inspected, shorten the pause or replace it with a reaction beat.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Dream And Platform Sources -> Subjective Unreality Needs Reality-Boundary Contracts

Source / example -> StudioBinder dream-sequence education, Mindframe mental-health media guidance, Google DeepMind Veo prompt guide, and existing atlas memory / sound-image / prompt-writing controls.

Observation -> Dream, imagination, hallucination, and intrusive-image inserts can alter reality, but they become unusable prompts when "surreal" means many uncontrolled symbols, horror filters, or stigmatizing shortcuts. Practical film education treats dream sequences as subjective or expressive departures from ordinary reality, while responsible media guidance cautions against reducing mental-health experiences to stereotypes. Platform prompt guidance supports explicit subject, action, style, ambience, and camera fields, so the unreal layer can be bounded as a visible/audible contract.

Mechanism -> A subjective imagination / dream / hallucination prompt should become a reality-boundary contract: subjective owner -> trigger cue -> subjective status -> reality boundary -> one unreal payload -> texture budget -> sound/image bridge -> return/reveal anchor -> representation boundary -> output review proof.

Executable control / prompt wording -> "Reference use, not surreal style: subjective insert controls one impossible perception only. Subjective owner: courier in the present hallway. Trigger: she stares at the sealed door handle for two beats. Status: imagined fear image, not objective reality and not a diagnosis. Reality boundary: viewer discovers it is unreal at the return. For 0.8 seconds, dark water appears to seep under the door. Only room tone drops and the water reflection is slightly too smooth. Hard cut back to the same dry floor, same door handle, her breath held. No copied dream sequence, horror filter, mental-illness stereotype, gore, full alternate scene, prophecy claim, or additional impossible events. Review owner, trigger, unreal payload, reality correction, texture budget, return anchor, and non-stigmatizing boundary."

Applicable scenes -> AI video dream inserts, imagined outcomes, fear/wish images, hallucinated object shifts, symbolic visualization, subjective unreality, output review, and retry diagnosis.

Misuse boundary -> Do not write "make it surreal," "dreamlike," or "hallucinatory" as a complete prompt. Do not use mental-health labels as visual shorthand, do not imply hallucination equals violence, and do not add many impossible events at once. If the return/reveal anchor is missing, the insert will read as continuity error rather than subjectivity.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Flashback And Platform Sources -> Memory Inserts Need Present-Return Anchors

Source / example -> StudioBinder flashback education, University of West Georgia film-terms glossary, Google DeepMind Veo prompt guide, and existing atlas transition / sound-image / prompt-writing controls.

Observation -> Flashbacks and memory inserts alter time, viewpoint, and information status. Film-education sources define flashback as a temporal return to earlier events, while platform prompt guidance supports explicit subject, action, scene, camera, style, and sound fields. In AI video prompts, "flashback" often becomes an unbounded dream filter or unrelated montage unless the present trigger, memory status, one past payload, texture difference, and return anchor are locked.

Mechanism -> A subjective memory / flashback prompt should become a present-return contract: present anchor -> trigger cue -> memory status -> one past payload -> texture budget -> sound/image bridge -> return anchor -> forbidden confusion -> output review proof.

Executable control / prompt wording -> "Reference use, not dream filter: flashback controls one past-tense clue only. Present anchor: courier stands in the present hallway holding a cracked brass locket. At 2 seconds her thumb rubs the crack. Memory status: subjective character memory, not objective proof. 1-second insert of the same locket unbroken on a hospital tray. Slightly lower contrast and softer room tone only. Return to her thumb still on the cracked locket in the present hallway. No copied film flashback, unrelated childhood scene, new location without bridge, fake archive label, gore, full backstory explanation, sepia wash, white flash, heavy blur, or extra montage. Review trigger, memory status, one past payload, controlled texture, return anchor, and past/present separation."

Applicable scenes -> AI video memory inserts, flashbacks, subjective recollection, clue reveals, unreliable memory, trauma fragments, time-shift transitions, output review, and retry diagnosis.

Misuse boundary -> Do not write "dreamy flashback" or "show the past" as a complete prompt. Do not use generic sepia/blur/glow as the mechanism. Do not add unrelated backstory, fake archive labels, copied famous flashbacks, or multiple past events. If the prompt cannot return to a present-tense anchor, simplify the insert.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### UI And Platform Sources -> Screen Inserts Need Single-Payload Contracts

Source / example -> Nielsen Norman Group usability heuristics, Material Design data-visualization guidance, Google DeepMind Veo prompt guide, and existing atlas title/graphic insert controls.

Observation -> UI and visualization sources emphasize status visibility, clear mapping between information and user action, hierarchy, labels, and reducing unnecessary cognitive load. Platform prompt guidance supports describing setting, action, camera, style, and text/visual details, but AI video screen graphics often drift into unreadable futuristic interface clutter unless the insert has one payload and a scene consequence.

Mechanism -> A map/diagram/screen-UI insert should become a single-payload contract: insert type -> diegetic/non-diegetic status -> owner/viewer -> one decision/status/route/warning/clue -> placement/screen surface -> interaction timing -> label budget -> hierarchy -> forbidden clutter -> output review proof.

Executable control / prompt wording -> "Reference use, not decorative FUI: screen UI insert controls one story decision only. Diegetic status: physical monitor inside the room, visible to the character. Desk monitor shows a simple two-route map with three labels: CURRENT ROOM, LOCKED DOOR, STAIRS OPEN; red highlight on locked door, green line to stairs; character glances at the screen, then turns toward the stairs. No fake OS brand, real map service, dense panels, random numbers, unreadable microtext, extra graphs, sci-fi UI clutter, floating labels, or animation that hides the route. Review screen surface, viewer/owner, payload, labels, interaction timing, and changed behavior."

Applicable scenes -> AI video prompts with monitors, maps, dashboards, tactical screens, phone screens, scanner overlays, diagrams, UI closeups, story clues, and output review.

Misuse boundary -> Do not write "futuristic interface" or "cool HUD" as a complete prompt. Do not use real map services, fake official systems, brand marks, meaningless dashboards, or dense microtext. If the UI does not change a decision, status, route, warning, comparison, or clue, simplify or remove it.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Title Design And Timed-Text Sources -> Text Inserts Need Payload And Legibility Contracts

Source / example -> Art of the Title title-sequence interviews, Netflix timed-text guidance, Google DeepMind Veo prompt guide, and existing atlas style-anchor controls.

Observation -> Title and text design can shape expectation, time, place, tone, authorship, or narrative transition, while timed-text guidance foregrounds legibility, timing, placement, and conflict with other image/text information. Platform prompt guidance supports describing scene, camera, action, style, and text-like details, but AI video prompts often treat onscreen text as decoration and get extra words, unreadable glyphs, or copied title-sequence identity.

Mechanism -> A title/card/intertitle insert should become a text-function contract: insert type -> exact payload -> typography role -> placement/safe area -> reading duration -> transition relation -> interaction with subtitles/action -> forbidden design transfers -> name-free fallback -> output review proof.

Executable control / prompt wording -> "Reference use, not title-sequence imitation: title insert controls information delivery only. Exact centered intertitle text: THREE HOURS EARLIER. Black card, plain white centered type, 1.5-second hold, hard cut in from the present-tense scene and hard cut out to the earlier hallway; no other text. No copied title sequence, logo, studio mark, branded font identity, ornate border, credit list, extra words, misspelled text, random glyphs, or moving typography that reduces readability. Review exact text, duration, placement, transition relation, and timeline function."

Applicable scenes -> AI video title cards, intertitles, lower-thirds, date/location cards, chapter breaks, graphic clues, trailer cards, storyboard timing, subtitle conflict checks, and generated-output review.

Misuse boundary -> Do not write "cool cinematic typography" as a complete prompt. Do not copy famous title sequences, branded fonts, logos, credit layouts, studio identities, or real news/institution graphics. Do not add text unless it carries a bounded payload and has enough reading time.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Preservation And Platform Sources -> Archive Texture Needs Source-Status Labels

Source / example -> National Film Preservation Foundation film-preservation guide, Library of Congress film care guidance, Google DeepMind Veo prompt guide, and existing documentary/realism anchor controls.

Observation -> Film-preservation sources treat older film/video as physical or technical material with identifiable carriers, damage, handling constraints, and preservation status. Platform prompt guidance supports describing visual style, camera, setting, action, and audio, but "archival" or "found footage" becomes risky when it implies provenance, institutional authority, or real evidence.

Mechanism -> An archival/found-footage insert should become a source-status contract: insert type -> source status label -> diegetic owner/viewer -> one or two artifact layers -> continuity relation to main scene -> time/location label policy -> forbidden provenance claims -> name-free fallback -> output review proof.

Executable control / prompt wording -> "Reference use, not forgery: archival insert controls source status and artifact layer only. Source status: fictional diegetic training tape inside the story, not real archive or news evidence. Three-second insert on a CRT monitor; invented shelf code T-14; mild gate weave, two dust scratches, soft tape hiss; the insert reveals one matching door number and then returns to the main scene. No real archive watermark, museum mark, news outlet, official seal, real date/location, real crisis/event claim, forged document, fabricated quote, or heavy damage hiding the clue."

Applicable scenes -> Fictional archive inserts, found-footage clues, training tapes, old home-movie memories, security monitor inserts, public-domain-source prompt preflight, continuity review, and non-deceptive realism checks.

Misuse boundary -> Do not write "real archived footage" unless a real provided/public-domain source is being used and labeled accurately. Do not add real archive marks, official seals, institutional labels, real dates/places/events, or fake evidentiary claims. Do not stack damage so heavily that the story clue or action becomes unreadable.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Documentary Mode And Platform Sources -> Realism Names Need Evidence-Status Contracts

Source / example -> Documentary mode and direct-cinema reference sources, Google DeepMind Veo prompt guide, and existing atlas style-anchor controls.

Observation -> Documentary references mix several layers: relation to reality, camera intervention, subject awareness, available light, synchronous sound, interview relation, archive status, and ethical truth claim. Platform prompt guidance supports camera, action, setting, lighting, and audio fields, but "documentary realism" is too broad and can become deceptive unless evidence status and staging boundary are stated.

Mechanism -> A documentary/realism style anchor should become an evidence-status contract: anchor name -> allowed realism layer -> evidence status -> camera relation -> subject awareness -> staging boundary -> sync sound/light logic -> forbidden authenticity claims -> name-free fallback -> output review proof.

Executable control / prompt wording -> "Reference use, not deception: documentary anchor controls camera relation and sync-sound texture only. Evidence status: fictional staged scene, not real footage or news evidence. Shoulder-height handheld camera observes from three meters away; subjects continue sorting files without addressing camera; available fluorescent light, slight exposure breathing, live room tone, paper scrape, and one offscreen chair sound remain synced. No real person, outlet, official logo, watermark, crisis/event claim, date/location claim, fabricated quote, surveillance claim, hidden-camera claim, or prompt wording that asks the clip to pass as real evidence."

Applicable scenes -> Fictional documentary texture, interview staging, archive-like inserts, observed workplace scenes, docu-drama prompt preflight, AI-video output review, and realism-style anchor cleanup.

Misuse boundary -> Do not write "make it look like real news footage" as a complete prompt. Do not imply generated material is real evidence, use real institutional marks, invent quotations from real people, or imitate footage of real crises. If the clip needs documentary texture, state the fiction/reconstruction status and the camera/sound relation.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Editing Education And Platform Sources -> Transition Names Need Bridge-Logic Contracts

Source / example -> Yale Film Analysis editing guide, StudioBinder match-cut education, Google DeepMind Veo prompt guide, and existing atlas transition/breakdown references.

Observation -> Editing sources separate match types and transition functions: action continuity, eyeline answer, graphic relation, sound bridge, ellipsis, contrast, or rupture. Platform prompt guides expose shots, action, camera, and audio as describable fields, but a famous transition name is too broad unless the matched elements and bridge logic are specified.

Mechanism -> A transition or match-cut style anchor should become a bridge-logic contract: anchor name -> allowed match layer -> outgoing element -> incoming element -> bridge logic -> timing/cut permission -> forbidden transfers -> name-free fallback -> output review proof.

Executable control / prompt wording -> "Reference use, not imitation: transition anchor controls bridge logic only. Shot A ends on a round clock stamp filling the left third; cut to shot B with a round elevator indicator in the same screen position; color and shape match, but location/time changes. No copied famous source objects, exact composition, plot leap, score cue, dialogue, characters, spacecraft/bone imagery, or film/editor name stack. Review outgoing element, incoming element, match type, changed information, and originality."

Applicable scenes -> AI video multi-shot prompts, shot lists, storyboard transitions, clip-to-prompt transfer, match-cut style-anchor cleanup, and generated-output review.

Misuse boundary -> Do not write "use the match cut from X" as a complete prompt. Do not copy source objects, iconic imagery, plot leap, timing, score cue, character relation, or exact composition. If the match type cannot be named, do not promote the reference.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Film-Analysis And Platform Sources -> Acting Names Need Observable Behavior Contracts

Source / example -> Yale Film Analysis Guide, Google DeepMind Veo prompt guide, existing dialogue/reaction prompt contracts, and style-anchor role controls.

Observation -> Film analysis treats performance as part of mise-en-scene: posture, gesture, facial behavior, blocking, and interaction with space are observable evidence. Platform prompt guidance supports describing character action, expression, dialogue, and scene behavior, but actor or role names are too broad and risk imitation rather than controllable performance direction.

Mechanism -> A performance style anchor should become an observable behavior contract: anchor name -> allowed behavior layer -> one mechanism -> micro-behavior cue -> gaze/reaction rule -> silence action or blocking/status change -> forbidden transfers -> name-free fallback -> output review proof.

Executable control / prompt wording -> "Reference use, not imitation: performance anchor controls behavior timing only. She wants the folder back but cannot ask; her fingers stop smoothing the table before the line ends; she avoids eye contact for two beats, then looks directly back once and chooses silence. No actor likeness, voice imitation, famous role, catchphrase, signature mannerism, copied scene, theatrical crying, or vague emotional acting. Review want/resistance, hand stop, gaze change, silence decision, and status shift."

Applicable scenes -> AI video dialogue prompts, reaction shots, restrained performance, actor/style-anchor cleanup, table/car/corridor scenes, prompt preflight, and output review.

Misuse boundary -> Do not write "act like X" as a complete prompt. Do not copy living actors, role identities, voices, catchphrases, signature gestures, or famous scene behavior. If the behavior can be described without the name, use the name-free version.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Production Design Sources And Platform Guides -> World Names Need Design-Layer Contracts

Source / example -> Production-design practitioner interviews, film craft/education sources on sets/props/costume/location as story information, Google DeepMind Veo prompt guide, existing style-anchor role contracts, and reference-role controls.

Observation -> Production design is not just a visual skin; spaces, props, surfaces, costumes, signage, and architecture carry story rules about work, class, access, age, pressure, and social order. Platform prompt guides expose location, style, character, lighting, and action fields, but a film world or designer name is too broad unless translated into one inspectable design layer.

Mechanism -> A production-design or worldbuilding style anchor should become a design-layer contract: anchor name -> allowed design layer -> one story mechanism -> spatial rule or prop function -> material/history logic -> forbidden transfers -> name-free fallback -> output review proof.

Executable control / prompt wording -> "Reference use, not imitation: production-design anchor controls spatial rule and prop function only. Narrow archive aisles block sightlines; one locked service door controls escape; stamped folder grants access; cracked badge fails at scanner; metal is polished only at hand-contact zones. No copied franchise world, iconic prop, costume silhouette, set layout, faction mark, logo, signature palette, or decorative clutter. Review access, obstacle, prop jobs, material wear, and no IP leakage."

Applicable scenes -> AI video/image prompts, worldbuilding references, set/prop/costume cleanup, production design anchors, location design, faction design, object-driven scenes, and prompt preflight.

Misuse boundary -> Do not write "make it look like X world" as a complete prompt. Do not copy recognizable IP design systems, logos, props, costumes, architecture, color codes, or faction marks. If the design layer does not change access, action, status, history, or story pressure, simplify it.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Sound Design Sources And Platform Guides -> Audio Names Need Listening Contracts

Source / example -> Walter Murch sound/design silence interviews, ACMI Foley sound education, Google DeepMind Veo prompt guide, existing sound-editing-rhythm reference, and style-anchor role contracts.

Observation -> Film-sound sources separate listening perspective, Foley/material cues, ambience, silence, and sound-image transition function. Platform prompt guidance supports audio-oriented fields on relevant video models, but a composer, sound designer, score, or film name is too broad and can drift into copied motifs or generic ambience.

Mechanism -> A sound or music style anchor should become a listening contract: anchor name -> allowed audio layer -> one mechanism -> listening point -> primary audio event -> mix hierarchy -> silence/density curve -> forbidden transfers -> name-free fallback -> output review proof.

Executable control / prompt wording -> "Reference use, not imitation: audio anchor controls listening point only. At 3s hallway ambience drops behind her hearing; breath and sleeve rustle stay close; one offscreen elevator bell leads her look by 0.5s. No copied score, melody, motif, sound logo, famous cue, jump-scare sting, full soundtrack imitation, or extra composer names. Review hearing owner, removed layers, remaining cue, cue timing, visible reaction, and audio sync."

Applicable scenes -> AI video prompts with sound, post-production cue sheets, offscreen sound reveals, subjective listening, silence tension, Foley/material proof, music-pulse timing, and style-anchor cleanup.

Misuse boundary -> Do not use a composer, score, or sound designer name as an all-purpose audio style. Do not copy melodies, motifs, sound logos, creature/device recipes, or recognizable soundtrack identities. If native audio is unsupported or unreliable, keep the same contract as a post-production cue sheet.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Film-Analysis Sources And AI Evaluation -> Breakdown Rows Need Prompt Contracts

Source / example -> Yale Film Analysis Guide, UNC Writing Center film analysis guide, UNCW shot breakdown handout, Google Cloud Veo prompt guide, Google DeepMind Veo prompt guide, VBench, and AIGVE survey.

Observation -> Film-analysis teaching sources separate objective description from significance, and shot-breakdown templates preserve framing, camera height, movement, transition, and match. Current AI-video prompt/evaluation sources separate prompt elements and review dimensions such as prompt alignment, subject consistency, spatial relation, motion, and temporal dynamics.

Mechanism -> A useful reference breakdown must pass through a contract layer before becoming a prompt: objective evidence -> shot function -> neighbor relation -> portable mechanism -> original prompt fields -> output review checks.

Executable control / prompt wording -> "Reference use: borrow only the reveal logic. Original 8-second clip: locked medium-wide storage-room shot; 0-2s worker counts boxes; 2-4s offscreen metal scrape behind the shelf; 4-6s camera stays fixed as he stops counting; 6-8s he notices one box label has changed. Review setup, offscreen cue, reaction, changed information, and no copied source characters or staging."

Applicable scenes -> Learning from film clips, public scene analyses, storyboards, shot lists, AI-video prompt rewrites, style-anchor cleanup, and generated-output review planning.

Misuse boundary -> Do not turn a film title, director name, or memorable scene into a prompt shortcut. Do not copy dialogue, plot beats, exact staging, or signature style. If the generated output has not been inspected, mark the mechanism as source-backed but not output-validated.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Google DeepMind Veo Prompt Guide -> Prompt Fields Are Creative Control Surfaces

Source / example -> Google DeepMind Veo prompt guide.

Observation -> The guide separates shot framing/motion, style, lighting, character description, location, action, dialogue, and audio-oriented prompt ideas.

Mechanism -> A video prompt is stronger when it names controllable surfaces rather than a single taste label. Each field tells the model what to preserve or change.

Executable control / prompt wording -> "Medium-wide locked-off hallway shot; detective seated by laptop; warm practical lamp from screen-left; soft offscreen floorboard creak behind the closed door at 4s; detective freezes before turning."

Applicable scenes -> AI video prompts, shot design, sound-image tests, dialogue-free suspense, character/action loops.

Misuse boundary -> Do not fill every field by default. Use only the fields that materially protect the intended output.

Validation status -> Official platform guidance plus prior atlas prompt cases; not capsule-promoted.

### Google DeepMind And Google Cloud Veo -> Camera Motion Is A Prompt Field, Not A Mood Label

Source / example -> Google DeepMind Veo prompt guide and Google Cloud Veo video prompt guide.

Observation -> Google's guidance names shot framing, camera motion, action, style, lighting, composition, and ambience as prompt elements that can be specified separately.

Mechanism -> Camera movement should be written as a contract, not as "cinematic." The model needs the movement type, subject relation, and visible result.

Executable control / prompt wording -> "Camera: slow dolly-in from medium-wide hallway to the detective's face over 6 seconds, beginning after the creak; the closed door remains visible at frame-right until the final second."

Applicable scenes -> AI video shot design, suspense push-ins, tracking action, reveal shots, locked-off listening scenes, product reveals.

Misuse boundary -> Do not stack camera movement, subject action, style change, and spatial reveal unless the clip is long enough. For 5-10 seconds, one camera job is usually enough.

Validation status -> Official platform guidance plus atlas shot-language reference; not capsule-promoted.

### Columbia Film Language Glossary -> Camera Movement Changes Viewer Bodily Relation To Space

Source / example -> Columbia Film Language Glossary, Camera Movement.

Observation -> Columbia defines camera movement as actual or perceived movement of the camera apparatus through space and links movement to the spectator's sense of moving through space.

Mechanism -> Prompting camera movement should account for viewer body position: fixed observer, scanning head turn, physical approach, follow alongside, unstable proximity, or optical isolation.

Executable control / prompt wording -> "Viewer feels fixed in the hallway: locked-off medium-wide shot." Or: "viewer physically approaches the table: slow dolly-in, not zoom."

Applicable scenes -> Movement vocabulary, AI video preflight, embodied action, suspense, dialogue coverage, spatial reveals.

Misuse boundary -> Do not confuse perceived movement with physical camera displacement. A zoom changes attention, while dolly/tracking changes spatial relation.

Validation status -> University glossary source; not capsule-promoted.

### Cooke, ASC, And Veo Sources -> Lens Look Needs Distance And Background Relation

Source / example -> Cooke Optics wide-angle and zoom guidance, American Cinematographer lens distortion / full-frame / interview lens discussions, Google DeepMind Veo prompt guide, VBench, and existing atlas shot-language reference.

Observation -> Lens and cinematography sources separate focal length, format angle of view, camera-subject distance, subject size, background distance, perspective, and optical zoom. They repeatedly caution that apparent compression or exaggeration depends on camera placement and relative distance, not focal length words alone. Platform and evaluation sources support camera/framing as prompt fields but still require visible review of prompt alignment and spatial relation.

Mechanism -> Write lens prompts as lens-distance contracts: focal-length class / angle of view -> camera-subject distance -> subject size -> background scale relation -> face/body rendering intent -> depth/focus relation -> zoom or physical movement boundary -> review check.

Executable control / prompt wording -> "Medium-telephoto portrait feel from a respectful camera distance; tight close-up from chest to head; facial planes remain natural; distant office lights appear softly compressed behind the character; doorway at frame-right remains readable; locked-off eye-level camera; no wide-angle face warp, fisheye edges, random zoom, extreme background blur, or surveillance distance."

Applicable scenes -> AI close-ups, interviews, confessions, surveillance views, chase/action movement toward camera, environmental portraits, background pressure, zoom/dolly distinction, lens-language prompt rewrites.

Misuse boundary -> Do not write only "24mm," "85mm," "telephoto," "large format," or "portrait lens" as magic words. If camera distance, subject size, and background relation are absent, the model may produce the wrong face shape or spatial feeling.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Action Interviews, Stunt-Safety Sources, And Platform Guides -> Fight Names Need Screen-Action Contracts

Source / example -> Gareth Evans action-design interviews, Chad Stahelski action/stunt-design interviews, SAG-AFTRA stunt safety resources, Academy stunt-design award announcement, Google DeepMind Veo prompt guide, existing action-scenes reference, and style-anchor role contracts.

Observation -> Practitioner sources frame action as planned camera/action movement, geography, performer collaboration, rhythm, impact illusion, and edit design rather than generic intensity. Official safety sources separate real stunt work as specialized, qualified practice. Platform prompt guidance supports specifying action, camera, style, and duration, but the prompt must keep screen causality inspectable and avoid operational stunt or fighting detail.

Mechanism -> An action director or fight style anchor should become a screen-action contract: anchor name -> evidence source -> allowed action layer -> one mechanism -> geography roadmap -> contact/near-miss proof -> receiver/environment response -> rhythm/recovery -> safety boundary -> forbidden transfers -> name-free fallback -> output review proof.

Executable control / prompt wording -> "Reference use, not imitation: action anchor controls screen-action clarity only. Borrow only arena roadmap followed by one contact-proof beat and one recovery breath. Name-free fallback: show narrow aisle, blocked exit, attacker left, defender right; prop crosses shield edge in one proof frame; defender recoils into shelf, tag snaps loose, dust falls; both reset with exit blocked. No copied combo, famous set piece, real fighting/stunt instruction, injury target, gore, brutality texture, weapon tutorial, or shaky blur hiding impact. Review geography, proof frame, response, recovery, changed spacing, and non-operational safety."

Applicable scenes -> AI action prompts, action-director/fight-reference cleanup, martial-arts or melee shot design, group-fight planning, prop/weapon-weight prompts, fictional danger beats, camera responsibility, generated-output review, and prompt preflight.

Misuse boundary -> Do not write "make it like X fight" as a complete strategy. Do not import a franchise's costume, brutality, weapon identity, real technique, stunt method, or exact combo chain. For real production, route risky material to qualified stunt coordination and safety procedures; for AI prompts, stay at fictional visual-causality level.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Cinematographer Interviews, Lens Sources, And Platform Guides -> Camera Names Need Spatial Contracts

Source / example -> American Cinematographer lens and cinematographer interview sources, Cooke Optics lens guidance, Leitz Cine cinematographer interview material, Google DeepMind Veo prompt guide, existing lens-distance contracts, and style-anchor role contracts.

Observation -> Cinematography and lens sources separate focal length, angle of view, camera placement, subject scale, background relation, focus behavior, and movement purpose. Platform prompt guides expose camera, shot, motion, style, and lighting as fields, but a cinematographer or film name is too broad unless it is translated into a reviewable camera relation.

Mechanism -> A cinematographer or camera-language style anchor should become a spatial contract: anchor name -> evidence source -> allowed camera layer -> one mechanism -> lens-distance relation -> camera height/angle -> subject scale -> composition relation -> forbidden transfers -> name-free fallback -> output review proof.

Executable control / prompt wording -> "Reference use, not imitation: camera anchor controls spatial relation only. Allowed mechanism: respectful medium-telephoto portrait feel from mid-distance; chest-up subject; background corridor appears closer while doorway remains readable. Name-free fallback: eye-level locked camera several meters back; stable chest-up scale; natural face shape; background scale presses inward. No copied frame, character, costume, production design, palette, exact blocking, living-artist imitation, or extra cinematographer names. Review distance, subject scale, background relation, face/body rendering, and no role leakage."

Applicable scenes -> AI video prompt writing, cinematographer/director/film camera references, lens-language cleanup, close-up design, character portraits, corridor/table staging, movement-trigger prompts, and output-review retry diagnosis.

Misuse boundary -> Do not write a cinematographer, director, lens brand, or film title as an all-purpose premium look. Do not let camera references import color palette, costume, production design, acting style, plot, edit rhythm, or famous frame geometry. If the name can be removed and the mechanism still works, the prompt is healthier.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### ARRI, ASC, And Motivated-Lighting Sources -> Light Quality Must Be Visible Mechanism

Source / example -> ARRI Lighting Handbook, American Cinematographer lighting lesson with Stephen H. Burum, ASC, and motivated-lighting education sources.

Observation -> ARRI frames lighting as practical production technique and fixture control. ASC/Burum emphasizes modeling actors, separating them from the background, and controlling fill. Motivated-lighting sources stress that light should belong to a visible or believable world source.

Mechanism -> Prompt lighting should name visible mechanisms: source, direction, shadow edge, fill level, separation, color relation, and material response. "Cinematic lighting" is not inspectable.

Executable control / prompt wording -> "Warm tungsten practical from frame-left motivates a soft key; negative fill keeps the right cheek dark; a narrow cool window rim separates black coat from background; brushed metal badge catches a crisp highlight."

Applicable scenes -> AI image/video prompts, product/costume shots, night interiors, noir, portraits, material realism, lighting preflight.

Misuse boundary -> Do not treat Kelvin numbers or fixture names as magic. If the prompt does not say what the light does to face, shadow, background, and material, the output may still look flat.

Validation status -> Strong production/practitioner/education sources plus atlas lighting reference; not capsule-promoted.

### Google DeepMind Veo -> Lighting Is A Prompt Element, But It Needs Source Logic

Source / example -> Google DeepMind Veo prompt guide.

Observation -> Google's prompt guidance includes lighting as a describable element, asking how the scene is lit and whether lighting is even, warm, or localized.

Mechanism -> Platform guidance supports naming lighting, but film-language control requires source logic and reviewability: where light comes from, what area it affects, and what visible proof it creates.

Executable control / prompt wording -> "Warm lamplight forms a small pool around the desk; cool moonlight stays on the back wall; the actor's face is half-lit, with soft shadow falloff."

Applicable scenes -> Text-to-video prompts, mood interiors, single-shot scenes, prompt rewrites, style consistency.

Misuse boundary -> Do not overload a short clip with multiple unmotivated color sources. One dominant source plus one contrast source is usually enough.

Validation status -> Official platform guidance plus lighting reference synthesis; not capsule-promoted.

### ARRI, Kodak, ACES, And Veo Sources -> Light Should Be A Source-Zone-Material Contract

Source / example -> ARRI Lighting Handbook, Kodak Essential Reference Guide for Filmmakers, Kodak Exploring the Color Image, Academy ACES documentation, Google DeepMind Veo prompt guide, and existing atlas lighting-color reference.

Observation -> Production and color sources describe light as source size/quality, shadow behavior, dimensional separation, color relation, material response, and workflow-preserved intent. Platform prompt guidance lets lighting be named, but generic labels like "cinematic color" or "moody neon" do not state where the light comes from, which zone it affects, or which material proves it.

Mechanism -> Treat lighting prompts as source-zone-material contracts: source motivation -> affected zone -> excluded zone -> shadow edge -> separation method -> material response by surface -> exposure boundary -> sequence matching note.

Executable control / prompt wording -> "Visible amber table lamp at frame-left motivates soft key; amber affects only tabletop, hands, and lower left wall; cool moonlit window spill stays in the background hallway and adds a thin blue rim on the dark coat; skin has soft diffuse falloff, wet leather gloves show streaky highlights, brushed metal badge catches one narrow hard edge; no full-frame orange/blue wash, no random glow, no plastic skin, no unmotivated rim."

Applicable scenes -> AI image/video prompts, night interiors, neon/practical color, product/costume/armor shots, moody dialogue, multi-shot color continuity, material-realism retries, lighting-output diagnosis.

Misuse boundary -> Do not use Kelvin numbers, ACES, neon, rim light, or "cinematic" as magic words. If the prompt lacks affected/excluded zones and material response, the model can still produce a flat wash or plastic surface.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### ACES Documentation -> Prompt Color Needs A Matching Intent Note

Source / example -> ACESCentral / ACES documentation overview.

Observation -> ACES defines a framework and standard components for managing color across motion-picture and television workflows.

Mechanism -> In prompt work, ACES should not be used as a look adjective. Its transferable lesson is matching intent: state which color relationship must survive across shots or retries.

Executable control / prompt wording -> "Matching note: preserve amber lamp versus cool window contrast across all retries; do not let the whole room become one blue wash."

Applicable scenes -> Multi-shot AI video, prompt iteration, reference still matching, grading notes, product consistency.

Misuse boundary -> Do not write "ACES look." Write the color relationship and continuity requirement.

Validation status -> Official technical source; not capsule-promoted.

### ARRI, Kodak, ACES, ASC, And Veo Sources -> Emotional Color Change Needs A Motivated Transition

Source / example -> ARRI Lighting Handbook, Kodak Essential Reference Guide for Filmmakers, Kodak Exploring the Color Image, Academy ACES documentation, American Cinematographer coverage of Roger Deakins / Empire of Light, Google DeepMind Veo prompt guide, and existing atlas lighting-color reference.

Observation -> Lighting and color sources separate source quality, color temperature, exposure/contrast, color relationships, and material response. Practitioner and platform sources support describing lighting as a controllable layer, but a mood word alone does not specify what changes over time or how the viewer verifies the story beat.

Mechanism -> Emotional light/color change should be prompted as a lighting-transition contract: before-state -> trigger -> source/zone change -> excluded zone -> exposure/shadow ramp -> material response -> separation change -> after-state/story consequence -> review gate.

Executable control / prompt wording -> "Before 3s, warm desk lamp holds the hands and envelope. At 3s, an offscreen elevator door opens frame-right; cool hallway spill enters only the right wall and metal cabinet edge. Warm lamp remains on the hands; wet coat shoulder beads begin catching the cooler rim; after-state reveals the room is no longer private. No full-frame blue wash, random flicker, unmotivated neon, or lost eye/envelope detail."

Applicable scenes -> AI video prompts with emotional turns, clue reveals, threat arrival, power loss, doorway/screen/window reveals, neon alarms, one-shot mood shifts, multi-shot light continuity, and generated-output diagnosis.

Misuse boundary -> Do not write "mood shifts blue" or "more cinematic color" as the only instruction. Avoid global tints, arbitrary exposure flicker, and overloaded multi-source changes in very short clips. ACES/color-management terms are not a substitute for visible source, zone, material, and after-state instructions.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Google AI For Developers And Microsoft Learn -> Platform Capability Must Become Prompt Bounds

Source / example -> Google AI for Developers Veo video-generation docs and Microsoft Learn Sora 2 video-generation overview.

Observation -> Current official platform docs expose model-dependent controls such as duration, input mode, aspect/resolution, audio support, and safety limits. Some systems can produce synchronized audio, but availability and exact behavior vary.

Mechanism -> Prompt writing must begin by bounding what the chosen platform can attempt. A prompt that assumes unsupported audio, duration, input type, or resolution is not a film-language problem; it is a platform-contract mismatch.

Executable control / prompt wording -> Before the scene text, write: "10-second text-to-video, native audio if supported, single continuous shot, 16:9." Then write only controls that fit that mode.

Applicable scenes -> Image-to-video, 5-10 second clips, motion tests, action fragments, continuity-sensitive shots.

Misuse boundary -> Do not transfer a platform-specific feature to every model. If native audio or long duration is unavailable, keep the cue as a post-production sound note or split the sequence.

Validation status -> Official platform guidance; not capsule-promoted.

### Google Cloud Veo Prompt Guide -> Negative Prompts Need Non-Instructive Wording

Source / example -> Google Cloud Veo prompt guide, negative prompts section.

Observation -> Google Cloud describes negative prompts as a way to specify unwanted elements, and recommends avoiding instructive "no" or "don't" phrasing.

Mechanism -> Negative constraints should not become a second competing direction. Use the main prompt to state the desired stable behavior, then use the negative field only for unwanted elements or moods.

Executable control / prompt wording -> Main prompt: "locked-off medium shot; closed door remains shut; sound source stays offscreen." Negative prompt: "monster, visible intruder, open door, trailer sting."

Applicable scenes -> Offscreen threats, locked-camera tests, identity continuity, material realism, sound-design prompts, image-to-video preservation.

Misuse boundary -> Do not put the story's main action in the negative field. If the prompt's meaning depends on "do not X," rewrite it as a visible positive state.

Validation status -> Official platform guidance; not capsule-promoted.

### AIGVE And AVGen-Bench -> Prompt Fields Need Matching Review Dimensions

Source / example -> AIGVE survey and AVGen-Bench text-to-audio-video evaluation source.

Observation -> Current AI-generated video evaluation research separates semantic delivery, human-intention alignment, audio-video synchronization, visual quality, temporal dynamics, and fine-grained controllability.

Mechanism -> A prompt field is only useful if it can be evaluated. Subject/action, camera motion, sound timing, barrier protection, and style each need a matching review question.

Executable control / prompt wording -> Add a review block after the prompt: "Check: subject performs the named action; camera motion is continuous; audio cue lands before reaction; objects do not drift; style remains consistent."

Applicable scenes -> Prompt templates, output review cards, retry diagnosis, comparison between generated variants.

Misuse boundary -> Evaluation vocabulary does not prove a clip works. It only tells what to inspect after generation.

Validation status -> Research-source backed; not capsule-promoted.

### Action Sources And AI Evaluation -> Contact Proof Is A Prompt Contract

Source / example -> David Bordwell on Jackie Chan / Police Story action clarity, American Cinematographer's Normal fight-scene production article, SAG-AFTRA performer-safety FAQ, CSATF production safety bulletins, AIGVE survey, and AVGen-Bench.

Observation -> Action clarity depends on visible geometry and consequence: a force path, a receiving body or object, a reaction, and a changed state. Current AI-video evaluation sources also separate prompt alignment, temporal/spatial dynamics, physical consistency, and fine-grained controllability.

Mechanism -> Contact proof becomes a prompt contract: setup -> attack vector -> receiving zone -> contact or near-miss relation -> receiver/environment response -> recovery or changed state -> review check.

Executable control / prompt wording -> "Medium-wide single shot; fighter plants rear foot and drives a forearm strike from screen-left into the shield edge; shield carrier recoils two steps and knocks a cup from the table; attacker rebounds and resets guard; review setup, contact relation, recoil, cup spill, and recovery."

Applicable scenes -> AI action clips, weapon clashes, stylized hits, blocks, dodges, falls, supernatural impacts, prop-driven action, and action-output retry diagnosis.

Misuse boundary -> Keep this at fictional screen-choreography level. Do not write real-world fight or stunt instructions, unsafe target advice, or operational stunt methods. Do not over-choreograph every limb when one readable force chain is enough.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Action Clarity, Animation Timing, And AI Evaluation -> Weight Needs A Speed-Contrast Curve

Source / example -> David Bordwell on Jackie Chan / Police Story action clarity, Frame.io action-editing guidance, Animation Mentor timing principle source, local `action-rhythm-editing` rhythm map, VBench, VBench-2.0, and AIGVE survey.

Observation -> Action-analysis and editing sources emphasize readable setup, action/reaction, environmental consequence, and enough aftermath for the viewer to register force. Animation timing sources separate timing/spacing, anticipation, follow-through, and settle as the cues that make motion feel physical. AI-video evaluation sources separate motion smoothness, temporal consistency, physical/common-sense plausibility, and prompt alignment.

Mechanism -> Weight should be prompted as a speed-contrast curve, not as "slow heavy action." A heavy beat needs visible preload, a short committed acceleration, a peak/contact relation, delayed receiver/environment response, follow-through, braking, and recovery into a changed state.

Executable control / prompt wording -> "5-second fictional screen-action beat: 0-1s fighter lowers stance and lets the head-loaded hammer lag; 1-2.8s sudden committed arc; 2.8s shield contact with low thud; 2.8-4s shield carrier slides half a step and dust jumps; hammer pulls torso forward; 4-5s rear foot skids, plants, and the fighter exhales into guard. No constant high speed, no weightless spin, no camera shake hiding the peak."

Applicable scenes -> AI action clips, heavy weapons, armor movement, creature impacts, superhuman dashes, vehicle/robot motion, product-action reveals, fight-output retry diagnosis, and timing polish after contact proof is already defined.

Misuse boundary -> Keep this at fictional screen-choreography and prompt-design level. Do not turn it into real fight, stunt, or weapon instruction. Do not add slow motion, shake, debris, or music hits as substitutes for visible preload, response, braking, and recovery.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Action Camera, Handheld, And AI Evaluation Sources -> Camera Must Prove, Not Hide, Force

Source / example -> Google DeepMind Veo prompt guide, David Bordwell's Unsteadicam and Bourne analyses, Frame.io action-editing guidance, American Cinematographer's Normal fight-scene article, local `high-tension-shot-design` camera-motion reference, VBench, and AIGVE survey.

Observation -> Platform guidance treats camera framing and motion as promptable fields. Action/editing sources warn that kinetic camera, close framing, shake, foreground wipes, blur, and fast cuts can either deliver information tokens and action-reaction relations or hide geography/contact. Current AI-video evaluation sources separate prompt alignment, temporal/spatial consistency, motion, and visible condition consistency.

Mechanism -> Give the camera one proof job per action beat: prove geography, follow initiator, reveal contact, relay receiver response, or stabilize consequence. Bound shake, blur, foreground coverage, closeups, and cuts around a readable proof frame.

Executable control / prompt wording -> "8-second fictional action beat. Camera job: prove a shield impact without hiding contact. 0-2s medium-wide frame shows attacker left, shield carrier right, and clear floor gap. 2-4s camera tracks slightly behind the attacker, slower than the weapon arc. 4s contact proof: camera stabilizes for one readable beat as the weapon overlaps the shield edge; tiny jolt only after contact. 4-6s relay to shield-carrier recoil and dust. 6-8s widen and steady on recovered spacing. No whip shake, random close-ups, foreground cover at contact, cut-away impact, or motion blur hiding limbs."

Applicable scenes -> AI action clips, fight/chase beats, shield/weapon impacts, creature or vehicle collisions, body-camera-style urgency, handheld scenes, foreground wipe shots, output retry diagnosis, and action shot-list planning.

Misuse boundary -> Camera energy cannot replace action proof. Do not use shake, blur, debris, closeups, or foreground wipes to conceal missing choreography, missing contact, unsafe detail, or failed receiver response. Keep this at fictional screen-choreography and prompt-design level.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Action Safety, Geography, And Contact Sources -> Danger Is A Fictional Evidence Contract

Source / example -> CSATF production safety bulletins, SAG-AFTRA performer-safety resources, David Bordwell on Jackie Chan / Police Story action clarity, Gareth Evans interviews on The Raid action design and impact illusion, American Cinematographer's Normal fight-scene article, Google DeepMind Veo prompt guide, and AIGVE survey.

Observation -> Official safety sources frame real stunt and performer safety as specialized production work, while action-analysis and practitioner sources show that screen danger is built from readable geography, contact or near-miss relation, body/object response, environmental consequence, and recovery. AI-video prompt guidance and evaluation sources support making those elements inspectable fields rather than relying on vague "intense danger."

Mechanism -> Dangerous action should be prompted as a fictional evidence contract: geography/escape relation -> vulnerability cue -> non-operational threat path -> near-miss or block proof -> receiver/object/environment consequence -> recovery or changed state -> safety boundary -> review gate.

Executable control / prompt wording -> "8-second fictional screen-action beat, not real stunt instruction. A courier backs through a narrow archive aisle; exit visible behind her, low railing on screen-right. Her front foot slips on loose papers; a long prop swings through frame; near-miss proof: it passes inches in front of her sleeve, papers lift, shelf tag snaps loose. She recoils, lamp flickers, dust falls, then resets with the exit blocked. No gore, injury detail, real weapon/stunt technique, how-to choreography, shaky blur hiding the near-miss, or extra attackers."

Applicable scenes -> AI action clips, chase beats, near-miss suspense, nonlethal weapon/shield beats, creature/vehicle danger, stunt-inspired fictional scenes, action-output review, and safety-aware prompt preflight.

Misuse boundary -> Do not provide real-world stunt, weapon, fight, injury, trap, or harm instructions. Do not use gore, shock, camera shake, debris, or darkness as substitutes for readable danger mechanics. For real production, route to qualified stunt coordination and safety procedures.

Validation status -> Source-backed prompt scaffold and safety boundary; not generated-output validated and not capsule-promoted.

### Murch, ACE, Platform, And Evaluation Sources -> Rhythm Needs Time Anchors

Source / example -> Walter Murch's CineMontage interview on rhythm, American Cinema Editors education resources, Google DeepMind Veo prompt guide, Ohio State sound/editing textbook, and AVGen-Bench.

Observation -> Practitioner and education sources frame rhythm as something tied to performance, camera, sound, and story flow, while current prompt/evaluation sources require controllable elements and inspectable audio-video alignment.

Mechanism -> AI-video rhythm should be written as a time-anchor contract: duration -> one dominant event -> beat timeline -> trigger -> reaction breath -> changed state -> review check.

Executable control / prompt wording -> "8-second clip. 0-2s locked setup and room tone; 2-4s phone buzz prelaps before the character looks down; 4-5s character freezes for one reaction beat; 5-8s camera pushes in slightly as he hides the phone. Cut rule: no random fast cuts; timing follows buzz -> glance -> reaction hold -> concealment."

Applicable scenes -> Suspense, dialogue beats, action impacts, trailer beats, short AI video prompts, native-audio prompts, music-sync tests, generated-output retry diagnosis.

Misuse boundary -> Do not write "fast paced" or "cut to the beat" as a substitute for event design. In short clips, more timing instructions can make the model worse; keep one dominant event and a few reviewable anchors.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Murch, ACE, Split-Edit, And AI Evaluation Sources -> Cuts Need Permission

Source / example -> Walter Murch's CineMontage interview on rhythm, American Cinema Editors education resources, Adobe J/L cut guidance, Google DeepMind Veo prompt guide, VBench, and AIGVE survey.

Observation -> Practitioner and education sources frame editing rhythm as something discovered from performance, camera, sound, action, and story pressure rather than imposed by abstract speed or beat grids. Split-edit sources show that audio and image can lead or trail each other when the offset has a job. AI-video evaluation sources make prompt adherence, temporal consistency, motion, and semantic delivery inspectable, so each timing choice needs an output check.

Mechanism -> Short AI-video rhythm should be written as a beat-anchor / cut-permission contract: setup frame -> dominant rhythm source -> allowed cut/hold triggers -> beat timeline -> viewer registration hold -> density curve -> sound/music relationship -> camera change rule -> final changed state.

Executable control / prompt wording -> "8-second AI video, maximum two cuts. Cut only when the hand fully stops on the note. Hold 0.7s after the red mark appears before the next cut. Phone buzz leads the look by half a second; final frame holds on breath stopping and eyes lifting toward the door. No random fast cutting, no cutting on every music beat, no montage fragments, no camera move during the reveal."

Applicable scenes -> Short AI-video prompts, suspense reveals, action impacts, dialogue reactions, music-sync clips, montage fragments, trailer beats, generated-output retry diagnosis.

Misuse boundary -> Do not treat "fast paced," "punchy," or "cut to the beat" as a complete instruction. A cut without a beat anchor can hide causality, reaction, geography, or state change. In 5-10 seconds, one dominant event and two or fewer cuts are often stronger than a micro-montage.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Murch, ACE, Split-Edit, Reaction, And Veo Sources -> Dialogue Timing Needs Cut Permission

Source / example -> Walter Murch's CineMontage interview on rhythm, American Cinema Editors education resources, Adobe J/L cut guidance, StudioBinder reaction-shot guidance, Google DeepMind Veo prompt guide, existing sound-editing-rhythm reference, and existing dialogue-scenes reference.

Observation -> Editing and reaction-shot sources frame rhythm as something discovered from performance, camera, sound, story pressure, and viewer interpretation. Split-edit sources show that sound can lead or trail image when it changes anticipation or emotional carryover. Platform guidance lets prompts specify dialogue, action, camera, audio, and duration, but short AI clips need inspectable timing anchors rather than abstract "slow" or "punchy" pacing.

Mechanism -> Dialogue timing should be prompted as a cut-permission contract: line/cue -> reaction owner -> reaction timing -> reaction breath window -> cut/hold permission -> sound lead/tail -> silence action -> object/space pressure -> final changed relation -> review gate.

Executable control / prompt wording -> "8-second restrained table dialogue, maximum one cut. At 2s she says one short line. Listener's fingers stop before the last word ends. Hold 1.5s on listener; she looks from folder to exit and lowers her breathing. Cut only after breath stops. Let the last word and room tone carry over the silent face for one beat. No extra dialogue, random reverse cut, theatrical pause, music swell, or camera move hiding hands."

Applicable scenes -> AI dialogue prompts, restrained performance, table/car/corridor scenes, reaction-shot design, J/L-cut-like sound-image offsets, suspense pauses, confession/negotiation beats, and generated-output retry diagnosis.

Misuse boundary -> Do not use pause length as a magic number. A pause must reveal a decision, refusal, realization, concealment, or changed relation. Do not add J/L-cut-like audio lead/tail unless it has a source and changes how the image is read.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Dialogue And Staging Sources -> Reaction Is A Prompt Contract, Not Filler

Source / example -> David Bordwell's "The Cross," Columbia Film Language Glossary eye-line match, StudioBinder reaction-shot guidance, Oklahoma State mise-en-scene textbook, Google DeepMind Veo prompt guide, and AVGen-Bench.

Observation -> Dialogue meaning is distributed across blocking, gaze, reaction timing, silence, and coverage. Platform and evaluation sources reinforce that prompt elements need visible behavior and reviewable alignment rather than abstract intent.

Mechanism -> A dialogue prompt should make reaction ownership explicit: want -> resistance -> surface behavior -> gaze rule -> line or cue -> listener/silence action -> blocking or state change -> review check.

Executable control / prompt wording -> "8-second restrained office scene. She wants the envelope back but cannot ask directly; he resists by keeping one hand on it. No direct eye contact until she says one short line: 'You already opened it.' Hold on his silent reaction as his fingers stop moving; table edge remains a barrier; review gaze rule, hand stop, listener reaction, and changed control of the envelope."

Applicable scenes -> Confessions, interrogations, negotiations, family meals, car dialogue, workplace pressure, restrained romance, AI-video dialogue tests, reaction-shot retries.

Misuse boundary -> Do not confuse subtext with vagueness. The viewer needs a visible tell, gaze rule, or blocking change. Do not copy famous dialogue or rely on long scripted lines; keep AI-video clips to one line/cue and one reaction.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Reaction Shot, Eyeline, And Prompt Sources -> Listener Owns The Meaning After The Cue

Source / example -> StudioBinder reaction-shot and shot/reverse-shot guidance, Columbia Film Language Glossary eye-line match, David Bordwell's dialogue-staging analyses, Oklahoma State mise-en-scene textbook, Google DeepMind Veo prompt guide, AVGen-Bench, and AIGVE survey.

Observation -> Film education and analysis sources treat reaction, eyeline, staging, and coverage as meaning controls: the important beat may land on the listener, object, or silence after the line. Current prompt and evaluation sources favor visible actions, camera controls, prompt alignment, and reviewable audio-video events over abstract performance labels.

Mechanism -> A reaction prompt should make ownership and timing explicit: trigger line/cue -> reaction owner -> line-to-reaction timing -> gaze rule/answer -> micro-behavior tell -> silence action -> object/space pressure -> final state change -> review check.

Executable control / prompt wording -> "8-second restrained dialogue beat. Trigger: at 3s she says one short line, 'You kept it.' Camera stays on him because his response proves he understands the lie. His fingers stop smoothing the envelope before she finishes; he avoids eye contact until 'kept,' then looks directly back once; he holds a two-second silence as he chooses not to confess. No speechifying, random eye drift, extra lines, or cutaway hiding hand/gaze. Review trigger, pre-reaction, gaze answer, hand tell, silence decision, envelope pressure, and table barrier."

Applicable scenes -> Confessions, interrogations, negotiations, restrained romance, family meals, car dialogue, workplace pressure, offscreen-speaker scenes, AI dialogue prompts, reaction-shot retry diagnosis.

Misuse boundary -> Do not treat reaction shots as filler or "natural acting" as a magic phrase. The viewer needs a trigger and a readable consequence. Keep short AI clips to one cue, one reaction owner, and one final state change.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Film Analysis, Blocking, Eyeline, And Veo Sources -> Limited Space Should Become Resistance

Source / example -> Yale Film Analysis Guide, UNC Writing Center film analysis guide, StudioBinder blocking/staging guidance, Learn About Film 180-degree rule and eyeline guidance, David Bordwell staging/dialogue analyses, Google DeepMind Veo prompt guide, and existing atlas dialogue-scenes reference.

Observation -> Film-analysis and blocking sources frame staging as actor placement, movement, spatial relation, eyeline, and audience attention. Limited spaces such as tables, cars, corridors, doors, and glass become useful when they change access, status, proximity, visibility, or escape options. Platform prompt guidance supports naming character action, camera/composition, location, and dialogue, but those fields need a visible review contract.

Mechanism -> Constrained dialogue should be prompted as a space-resistance contract: character want -> resistance/forbidden truth -> space rule -> gaze rule -> reaction owner -> micro-behavior tell -> blocking delta or refusal -> camera/axis lock -> changed relation -> review gate.

Executable control / prompt wording -> "8-second restrained table scene. Table edge is the barrier; sealed folder stays on listener's side. Speaker wants it opened; listener refuses without explaining. Speaker holds eye contact; listener looks at folder, then exit, never back until final beat. At 5s speaker leans across table; listener stays still and tightens one hand on folder. Locked medium two-shot keeps faces, hands, folder, and exit line readable. No speechifying, theatrical gestures, random eye drift, extra characters, or cutaway hiding hands."

Applicable scenes -> AI dialogue prompts, table scenes, car/taxi dialogue, corridor pressure, doorway/threshold conflict, interrogations, confessions, negotiations, family meals, office hierarchy, and dialogue-output retry diagnosis.

Misuse boundary -> Do not treat constrained space as decoration. If the table, car direction, corridor depth, doorway, glass, or seating height does not block, expose, delay, or reframe a want, simplify the scene. Avoid copying exact famous blocking or dialogue; use the mechanism in an original scene.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Sound Sources, Foley, Platform, And Evaluation -> Audio Needs A Cue Sheet

Source / example -> Google AI for Developers Veo video-generation docs, Google DeepMind Veo model/prompt pages, ACMI Foley Sound, Walter Murch interview sources, A Quiet Place sound-design interviews, Ohio State sound/editing textbook, and AVGen-Bench.

Observation -> Current platform guidance allows prompts to specify dialogue, sound effects, and ambient noise on some models, while film-sound sources separate source, perspective, Foley, ambience, silence, and transition function. AVGen-Bench treats audio-video synchronization and fine-grained controllability as evaluation dimensions.

Mechanism -> Sound design should be prompted as an inspectable cue sheet: listening point -> source status -> time window -> distance/obstruction -> material/Foley proof -> mix priority -> visible reaction or story-state change -> review check.

Executable control / prompt wording -> "8-second locked hallway shot, native audio if supported. 0-2s low room tone and laptop fan; 2-4s muffled dry floorboard creak behind the closed door, high frame-left; 4-6s detective freezes and stops the recorder; 6-8s tape hiss cuts out, leaving breath and room tone. Mix priority: creak, recorder hiss, breath; no score, no narration, no jump-scare sting."

Applicable scenes -> Offscreen threat, suspense, dialogue pauses, action impacts, material realism, generated-video native audio, post-production cue sheets, output review and retry diagnosis.

Misuse boundary -> Do not rely on "cinematic tension audio." Do not overpack multiple sound events into a short clip. If the model or mode cannot generate native audio, keep the cue sheet as post-production guidance and still use visual reaction locks.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Native Audio, Foley, Silence, And AV Evaluation -> One Sound Event Needs Priority

Source / example -> Google AI for Developers Veo audio/video-generation guidance, Google DeepMind Veo pages, ACMI Foley Sound, Walter Murch on designed silence, A Quiet Place sound-design interviews, AVGen-Bench, and existing atlas sound/offscreen-audio references.

Observation -> Current native-audio video guidance and audio-video benchmarks make synchronization and controllability reviewable, while film-sound sources show that Foley, offscreen sound, and silence work through source, material, listener perspective, mix priority, and visible consequence. In short AI clips, multiple foreground sound ideas often compete and become generic ambience or unwanted score.

Mechanism -> Use an audio-event-priority contract: one primary sound event -> source/material -> exact time window -> listener point -> distance/obstruction -> ambience bed -> silence/layer change -> image consequence -> mix hierarchy -> source reveal rule -> negative audio constraints.

Executable control / prompt wording -> "8-second locked suspense shot, native audio if supported. At 4s, one dry floorboard creak from behind the closed door, muffled through wood, high frame-right. Heard from the detective's seated position; low room tone and laptop fan sit underneath. After the creak, laptop fan fades slightly; her hand stops on the recorder button and eyes move toward the door. Mix priority: creak foreground, breath second, room tone low; no score, drone, jump-scare sting, narration, or visible source reveal."

Applicable scenes -> AI video with native audio, offscreen threat, dialogue-free suspense, object/prop cues, Foley-led action, stealth beats, subjective listening, sound-output review, post-production cue sheets.

Misuse boundary -> Do not write "cinematic tension audio" or stack several foreground sound events in a 5-10 second clip. If the platform cannot generate native audio reliably, keep the same event contract as post-production guidance and visual-reaction timing.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Subjective Sound Sources And Native Audio Guidance -> Listening POV Needs A Filter Stack

Source / example -> Walter Murch interview sources, "A Quiet Place" sound-design interviews, "The Zone Of Interest" sound-design and production-sound interviews, "The Conversation" / Walter Murch sources, Google AI for Developers Veo video-generation docs, Google DeepMind Veo pages, AVGen-Bench, and VABench.

Observation -> Practitioner sources treat sound as perspective, selective attention, offscreen world-building, recording ambiguity, and subjective silence rather than generic ambience. Current native-audio video guidance can accept prompts for sound effects, ambience, and dialogue on supported models, while audio-video benchmarks make synchronization, controllability, and audio-video alignment reviewable.

Mechanism -> Subjective listening should be written as a filter stack: hearing owner -> hearing condition -> source status -> distance/obstruction -> removed layers -> remaining cue anchor -> transition into/out of POV -> image consequence -> mix priority -> post-production fallback.

Executable control / prompt wording -> "Listening POV: heard from the courier's position behind the closed metal door. After impact, room tone collapses into a thin ringing tone; hallway footsteps become muffled low pulses; only breath and sleeve rustle remain sharp; one key jingle outside is barely audible high frame-right. No score, no clean dialogue, no jump-scare sting. Review hearing owner, closed door, filtered layers, key-jingle reaction, and post cue fallback."

Applicable scenes -> Suspense, shock, hearing loss or overload, surveillance playback, behind-wall listening, underwater/helmet/interior-body sound, offscreen threat, native-audio AI video, and post-production cue sheets.

Misuse boundary -> Do not write only "muffled sound" or "subjective audio." Do not use hearing conditions as decorative gimmicks; tie them to character perception and visible behavior. If native audio is unsupported or unreliable, keep the same timing as a post-production cue sheet and visual reaction guide.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Prior Atlas Output-Review Cases -> Retry With One Dominant Prompt Delta

Source / example -> Existing atlas Rounds 30-34: AI offscreen sound prompt card, failure diagnosis, visual protection table, unified review sheet, and review report template.

Observation -> The review cards repeatedly separate prompt contract, observed evidence, dominant failure class, and retry patch.

Mechanism -> Prompt iteration is strongest when it changes one failed field and preserves stable output. Rewriting the whole prompt hides whether the repair worked.

Executable control / prompt wording -> "Keep the locked hallway setup. Fix one field: at 4s, a muffled floorboard creak comes from behind the closed door; detective freezes before turning. Door remains closed."

Applicable scenes -> Any generated-output retry after the first result exists.

Misuse boundary -> Do not write a retry delta from the prompt alone. Inspect the output first.

Validation status -> Local case-backed workflow; still needs more real generated-output reviews before capsule promotion.

### Reference, Character-Consistency, And Benchmark Sources -> Continuity Needs Roles And Allowed Change

Source / example -> Runway Gen-4 Image References guide, Adobe Firefly Boards character-sheet workflow, Google DeepMind and Google Cloud Veo prompt guides, Face Consistency Benchmark, NVIDIA Video Storyboarding, ViStoryBench, VBench, and local `character-continuity-bible` template.

Observation -> Current reference workflows use named references for characters, objects, scenes, and sketches/layouts, while research benchmarks treat character consistency, multi-shot consistency, prompt adherence, motion, and visual/stylistic continuity as separate evaluation concerns. Adobe's character-sheet workflow also shows why multi-view identity anchors can support later poses and scenes.

Mechanism -> Continuity prompts should not say "keep everything the same." They should assign reference roles, list durable anchors, list allowed changes, and bind each lock to a review check. This protects identity while still permitting pose, expression, camera, lighting, and motion changes.

Executable control / prompt wording -> "@Image1 locks identity only: face shape, hair silhouette, body proportion, age impression. @Image2 locks weapon and costume only. @Image3 locks corridor layout only. Allowed: new pose, small reaction, cloth motion, lighting variation. Forbidden: face swap, hairstyle change, jacket recolor, weapon size/type drift, extra characters, background replacement, diagram marks in final. Review identity, costume, prop, layout, and allowed change."

Applicable scenes -> AI-video series clips, image-to-video continuity, multi-shot storyboards, recurring characters, action reels, product/prop continuity, location continuity, layout-board prompts, and generated-output retry diagnosis.

Misuse boundary -> Do not over-lock every visible detail; it can freeze motion or make the model copy the reference pose. Do not let one reference control identity, costume, layout, and style unless it truly contains all four and no conflict exists. Do not claim consistency success before inspecting outputs.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Continuity Editing, First-Last Frames, And Storyboard Sources -> Shot Handoffs Need State Bridges

Source / example -> Google Cloud Veo first-and-last-frame video generation guide, Adobe match-cut education source, Learn About Film 180-degree/eyeline guide, eCampusOntario continuity-editing chapter, Cognitive Science study on continuity editing, NVIDIA Video Storyboarding, ViStoryBench, VBench, and local atlas transition/breakdown references.

Observation -> Film-editing sources treat continuity as a relation across shots: action matches, eyelines answer, screen direction stays legible, and sound/graphic matches bridge gaps. Current AI-video and storyboard sources expose first/last frame or multi-shot consistency as controllable or evaluable surfaces, but still require manual review for prompt adherence, motion, subject consistency, background consistency, style consistency, and temporal continuity.

Mechanism -> A multi-shot prompt needs a handoff contract, not only a new prompt for the next shot. Convert the previous final frame into inherited state: identity, costume, prop relation, body pose, action phase, screen direction, eyeline/target, scene layout, light/color relation, and sound tail. Then state what the new shot is allowed to change and what new information it must add.

Executable control / prompt wording -> "Shot B starts from Shot A's last frame: scanner already raised in her right hand, body leaning toward the door on screen-right, same corridor axis and cool light. Continue the wrist lift into a scan; cut tighter over her shoulder; reveal the red warning mark. No lowered scanner, no hand swap, no reversed corridor, no new door, no face/costume change. Review first-frame inheritance, action phase, rightward screen direction, prop relation, and new reveal."

Applicable scenes -> Multi-clip AI video, first/last-frame generation, shot lists, storyboards, action continuations, dialogue eyeline answers, prop handoffs, reveal cuts, sound bridges, and output-retry diagnosis.

Misuse boundary -> Do not force every transition to be invisible continuity. Rupture, jump cut, ellipsis, contrast, or graphic match can be intentional, but the prompt must name that bridge type and its purpose. Do not claim sequence continuity before inspecting the generated clips together.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Mechanical Transformation, Platform, And Evaluation Sources -> Deployment Needs A Lock-State Contract

Source / example -> Google DeepMind Veo prompt guide, Google Cloud Veo video prompt guide, Google AI for Developers Veo video-generation docs, VBench, AIGVE survey, spatiotemporal-consistency survey, Cartoon Brew report on ILM's "Bumblebee" transformation work, and local `mechanical-transformation-design` frontier reference.

Observation -> Platform guides encourage naming subject, action, camera, lighting, style, and audio instead of one vague result. Evaluation sources separate prompt alignment, subject consistency, spatial relation, motion smoothness, temporal dynamics, and spatiotemporal consistency. The ILM practitioner report describes transformation as a design and timing problem around vehicle/robot parts, camera angle, movement distance, and shot length rather than a single magic swap.

Mechanism -> Mechanical deployment should be written as a lock-state contract: form A -> visible trigger -> named mechanism family -> stored-volume source -> staged movement -> alignment -> lock/settle proof -> new handling proof. This makes the changed state inspectable and reduces soft morph, duplicated parts, and identity drift.

Executable control / prompt wording -> "Compact wrist tool starts closed around the same black grip. At 2s side seams release; nested plates unfold from the forearm housing; two telescoping rails extend forward; at 6s latch pins click, vibration damps, the wrist dips, and the other hand regrips. No liquid morph, no duplicate parts, no new tool from offscreen. Review stored panels, staged extension, lock, settle, and changed handling."

Applicable scenes -> AI video prompts for transforming props, weapon deployment, armor assembly, robot tools, vehicles, mechanical creatures, production-design reveal shots, generated-output retry diagnosis, and image-to-video motion planning.

Misuse boundary -> Do not use this to design real weapons or unsafe mechanisms. Do not overload a short clip with full-body transformation, combat action, camera orbit, environment destruction, and style change at once. If the model cannot preserve all stages, split into a close deployment shot and a separate wide use shot.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Microsoft Sora 2 Overview And AI Video Evaluation Sources -> Review The Generated Contract, Not The Prompt Intention

Source / example -> Microsoft Learn Sora 2 overview, AIGVE survey, AVGen-Bench, and related atlas review cards.

Observation -> Current systems expose text/image/video input modes, duration/resolution settings, audio support on some platforms, and evaluation concerns around semantic alignment, audio-video sync, and spatiotemporal consistency.

Mechanism -> A prompt is only useful if it can be reviewed. Prompt fields should become checks: did the subject do the named action, did camera motion match, did audio sync, did objects remain stable, did the story state change?

Executable control / prompt wording -> Add a final review block: "Check: door remains closed; sound occurs before reaction; camera stays locked; no music covers the creak; detective pauses playback after the sound."

Applicable scenes -> AI video output review, retry diagnosis, benchmark-inspired scoring, clip comparison.

Misuse boundary -> Do not claim prompt success from wording alone. Inspect generated frames/audio before promoting a mechanism.

Validation status -> Platform/research-backed; not capsule-promoted.

### Editor Interviews, ACE Education, And Platform Guides -> Rhythm Names Need Layer Locks

Source / example -> Walter Murch CineMontage interview sources, Thelma Schoonmaker editing interviews, American Cinema Editors education resources, Adobe J/L cut guidance, Google DeepMind Veo prompt guide, and existing style-anchor role contracts.

Observation -> Practitioner sources discuss editing through rhythm, performance, music, emotion, and relation between image and sound, while education/platform sources separate controllable prompt fields and reviewable outcomes. A name like an editor, director, film, trailer, or music video can be high-density shorthand, but it is too broad for a generated-video prompt unless the intended layer is isolated.

Mechanism -> A rhythm style anchor should become a layer-locked contract: anchor name -> evidence source -> allowed rhythm layer -> one mechanism -> cut/hold permission -> sound-image relation -> forbidden transfers -> name-free fallback -> output review proof. This lets the reference guide timing without copying a famous cut pattern, plot reveal, dialogue, or montage identity.

Executable control / prompt wording -> "Reference use, not imitation: rhythm anchor controls timing only. Borrow only one sound-led reveal followed by a 1s reaction hold. Name-free fallback: phone buzz leads the look by 0.5s; cut only after her hand stops; final 1s hold on changed envelope. No copied scene, dialogue, plot twist, exact montage structure, signature palette, living-artist imitation, or extra editor/director names. Review cue order, cut permission, reaction hold, and no role leakage."

Applicable scenes -> AI video prompt writing, editing-rhythm design, dialogue pauses, sound bridges, short montage bursts, action clarity, trailer/music-video reference cleanup, and output-review retry diagnosis.

Misuse boundary -> Do not write "edit like X" as a complete instruction. Do not use a rhythm anchor to import color palette, costume, acting style, camera language, plot, or famous sequence shape. Do not promote this to a capsule until generated-output reviews show the layer lock improves retries.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### Platform Reference Workflows, Style Boundaries, And Evaluation -> Style Anchors Need Roles

Source / example -> Runway Gen-4 Image References guide, Adobe Firefly reference/character workflow, Google DeepMind and Google Cloud Veo prompt guides, OpenAI GPT-4o image-generation system-card addendum, VBench, AIGVE survey, and existing style-anchors reference.

Observation -> Current platform sources separate prompt surfaces such as subject, action, camera, lighting, style, ambience, and reference images. Runway's reference workflow supports named reference roles for character, object, style, location, and layout/sketch use. Evaluation sources separate prompt alignment, subject consistency, style consistency, spatial relation, motion, and temporal consistency. OpenAI's public image-generation safety discussion is an additional boundary source for avoiding direct living-artist style imitation.

Mechanism -> A named style anchor should become a role contract: reference name -> allowed mechanism -> controlled layer -> prompt translation -> forbidden transfer -> compatibility check -> name-free fallback -> output review proof. This preserves high-density anchors without turning them into scene copying, living-artist imitation, or uninspectable style soup.

Executable control / prompt wording -> "Reference use, not imitation: Reference A controls only lighting mechanism: one visible warm practical shapes hands and tabletop while cool exterior spill stays in the background. Reference B controls only editing mechanism: one sound-led reveal and a short reaction hold. Do not copy characters, location, exact composition, plot, dialogue, signature palette, or living-artist style. Review: each reference contributes one visible/audible mechanism and the scene remains original."

Applicable scenes -> AI video prompt writing, style-anchor cleanup, reference-image prompts, director/cinematographer/editor/action/sound anchor stacks, generated-output review, and prompt preflight before model submission.

Misuse boundary -> Do not write "in the style of X" as a complete prompt strategy. Do not stack several famous names without assigning roles. Do not let an identity reference also control style/layout unless explicitly intended. Do not use this as evidence that a platform will obey every reference role without output inspection.

Validation status -> Source-backed prompt scaffold; not generated-output validated and not capsule-promoted.

### AI Video Platform And Evaluation Sources -> Review The Generated Contract Before Taste

Source / example -> Google AI for Developers Veo video-generation docs, Google DeepMind and Google Cloud Veo prompt guides, Microsoft Learn Sora 2 overview, Runway Gen-4 reference guidance, VBench, EvalCrafter, NeurIPS 2024 human-evaluation protocol paper, VBench-2.0, AVGen-Bench, and AIGVE survey.

Observation -> Current platform sources expose promptable fields such as subject, action, camera, composition, lighting, style, audio, duration, references, and settings. AI-video evaluation sources repeatedly separate visual quality from text/prompt alignment, subject consistency, motion quality, temporal consistency, audio-video sync, and fine-grained controllability. Human-evaluation research also warns that overall preference alone is too coarse for diagnosing generated-video failures.

Mechanism -> Generated-output review should be a contract audit before a taste judgment: prompt field -> expected evidence -> observed evidence -> pass/partial/fail -> likely cause -> minimum retry delta. This separates "the clip is pretty" from "the intended shot, action, continuity, sound, and reference roles actually happened."

Executable control / prompt wording -> "Review gates in order: subject identity, action/state change, camera proof, space/screen direction, light/material, sound timing, style/reference role, continuity, final viewer information. For each failed gate, name observed evidence and likely cause: missing prompt field, conflicting prompt field, prompt overload, platform/mode limit, reference-role leakage, or model miss. Retry with one minimum delta only."

Applicable scenes -> AI video output review, prompt retry, reference-image workflows, multi-shot continuity tests, action/contact proof, native-audio checks, style-anchor audits, and choosing between generated variants.

Misuse boundary -> Do not treat benchmark categories as a complete director's rubric or as proof that a specific output succeeded. Do not rewrite the whole prompt after one failed gate. Do not promote the review sheet to a capsule until real generated outputs show that it improves retry decisions.

Validation status -> Source-backed review scaffold; not generated-output validated and not capsule-promoted.

### Film Analysis And AI Review Sources -> A Clip Study Needs A Full Prompt Loop

Source / example -> Yale Film Analysis Guide and examples, UNC Writing Center film analysis guide, UNCW shot-breakdown handout, Google DeepMind and Google Cloud Veo prompt guides, VBench, EvalCrafter, and AIGVE survey.

Observation -> Film-analysis sources separate description from interpretation and encourage attention to shot/scene/sequence evidence, while shot-breakdown templates preserve technical fields such as framing, angle, movement, transition, and match. Platform sources ask for separate controllable prompt fields, and AI-video evaluation sources separate prompt alignment, subject consistency, motion, temporal stability, and quality. Together, these sources support a loop rather than a one-way "inspired by this scene" prompt.

Mechanism -> Clip study should move through five gates: objective breakdown -> function chain -> portable mechanism filter -> original prompt contract -> generated-output review. The portable mechanism is valid only if it appears in a new scene without depending on copied characters, dialogue, exact staging, iconic imagery, or source-specific style.

Executable control / prompt wording -> "Source use: extract mechanism only, not imitation. Portable mechanism: orient the viewer to a target, trigger one offscreen cue, hold on the reaction, then reveal one changed state. Original 8-second scene... Constraints: no copied source characters, plot, dialogue, exact staging, famous composition, or director/style name. Review: target oriented, cue before reaction, reaction hold visible, state changed, scene remains original."

Applicable scenes -> Excellent-segment study, shot-by-shot learning, film-to-prompt translation, AI-video prompt rewrites, generated-output comparison, and future case-card validation.

Misuse boundary -> Do not treat "looks like the source" as success. Do not copy a sequence's exact plot, blocking, dialogue, composition, or iconic image. Do not promote a clip-derived mechanism until it works in an original prompt and is inspected in generated output.

Validation status -> Source-backed loop scaffold; not generated-output validated and not capsule-promoted.

## Quick Translation Table

| Film mechanism | Prompt control | Negative / positive rewrite | Review check |
| --- | --- | --- | --- |
| Offscreen threat | Name source, barrier, listener, and reaction | Prefer "door stays closed" over "do not reveal intruder" when negative phrasing is risky | Source remains unseen; listener reacts after cue |
| Slow tension push-in | Name camera move and duration | "slow dolly-in over the clip" instead of "not too fast" | Subject grows larger without jump cuts |
| Lens distance / perspective | Pair focal-length class with camera distance, subject size, background scale, face rendering, depth/focus, and zoom/dolly boundary | "no wide-angle face warp, fisheye edges, random zoom, erased doorway, or false surveillance distance" instead of "cinematic lens" | Face shape, camera distance feeling, background relation, and optical/physical movement boundary are visible |
| Cinematographer / camera style anchor | Assign a named cinematographer/director/film/lens reference to one camera layer, spatial mechanism, forbidden transfers, name-free fallback, and review gate | "camera anchor controls only medium-telephoto mid-distance portrait relation; no copied frame, palette, costume, blocking, or style soup" instead of "shoot it like X" | Camera distance, subject scale, background relation, composition job, and no role leakage are visible |
| Constrained dialogue space | Name space type, barrier/pressure rule, gaze rule, reaction owner, micro-tell, blocking delta/refusal, camera/axis lock, and changed relation | "table edge blocks access; listener stays still and tightens hand on folder" instead of "subtle tense dialogue" | Space rule, gaze rule, reaction owner, micro-tell, movement/refusal, and changed relation are visible |
| Dialogue timing / cut permission | Name line/cue, reaction owner, reaction timing, reaction breath window, cut/hold permission, sound lead/tail, silence action, and changed relation | "cut only after breath stops; last word carries over silent face" instead of "slow dramatic pacing" | Cue order, reaction owner, pause value, cut permission, audio/image offset, and final relation are visible/audible |
| Dialogue reaction | Name want, resistance, gaze rule, silence action, and reaction owner | "restrained performance; no speechifying; no random eye drift" instead of "make the acting subtle" | Hidden pressure is visible through behavior, gaze, pause, or blocking |
| Listener reaction ownership | Name trigger cue, reaction owner, line-to-reaction timing, gaze answer, micro-behavior tell, silence action, and final state change | "one short cue; camera stays on listener; no extra dialogue, random eye drift, theatrical acting, or cutaway hiding the tell" instead of "natural reaction shot" | Trigger, pre/delayed reaction, gaze answer, micro-tell, silence decision, and changed state are visible |
| Performance / acting style anchor | Assign a named actor/role/performance reference to one observable behavior layer, mechanism, forbidden transfers, name-free fallback, and review gate | "borrow only one hand stop + avoided gaze + final direct look; no actor likeness, voice imitation, famous role, catchphrase, or signature mannerism" instead of "act like X" | Want/resistance, micro-behavior, gaze rule, reaction ownership, silence action, and no imitation leakage are visible |
| Sound-image design | Name source, timing, perspective, Foley/material, mix priority, and reaction | "no generic score; prioritize creak, breath, room tone" instead of "make tense audio" | Cue is audible, spatially legible, synced, and changes visible behavior |
| Audio event priority | Name one primary sound event, source/material, time window, listener point, obstruction, silence/layer change, mix hierarchy, and source reveal rule | "no score, drone, jump-scare sting, narration, extra foreground cues, or visible source reveal" instead of "cinematic tension audio" | Cue is audible at the right time, spatially mapped, not masked, and followed by visible consequence |
| Sound perspective / distance clue | Assign sound to source status, listener point, distance, obstruction/filter, acoustic quality, reveal policy, mix priority, image consequence, and generic-audio guard | "offscreen elevator motor two rooms left behind metal fire door; muffled hum clears slightly when inner door opens; source stays hidden; no score, drone, loud close-up sound, or source teleport" instead of "we hear something nearby" | Source status, listener point, distance, obstruction, acoustic change, reveal policy, and behavior change are audible/visible |
| Offscreen sound reveal / misdirection | Assign sound to assumed source, actual source, listener point, offscreen duration, acoustic clue, correction beat, reveal evidence, listener reaction, payoff, and unfair-cheat guard | "scrape behind door seems like person; reveal cart wheel rubbing threshold in sync; no unrelated jump scare, late source, unresolved noise, or music sting" instead of "mysterious sound" | Assumption, actual source, delay, acoustic match, correction beat, reaction, and payoff are visible/audible |
| Sound bridge / prelap | Assign outgoing image, incoming audio source, lead duration, audio material/content, transition point, incoming image answer, image relation, payoff, mix priority, and accidental-audio guard | "train brake begins 0.8s before cut from archive room; cut reveals platform train entering; no random whoosh, music sting, source mismatch, or audio without visual answer" instead of "sound bridge to next scene" | Outgoing image, incoming sound, lead duration, cut point, image answer, payoff, and mix replacement are audible/visible |
| Postlap / audio-tail | Assign outgoing audio source, carry duration, incoming image relation, cutoff/replacement point, new scene sound takeover, payoff, mix priority, and muddy-carryover guard | "archive latch hum carries 0.8s over sidewalk image, then fades when shoe hits pavement and traffic takes over; no indefinite hum or hidden action" instead of "let old audio continue" | Outgoing source, carry duration, incoming relation, cutoff/replacement, payoff, and clean mix takeover are audible/visible |
| Audio match cut / sonic match | Assign outgoing sound shape, incoming matching source, sonic cut/blend point, difference cue, image answer, payoff, mix priority, and mismatch guard | "scanner double-beep cuts on second pulse to turnstile double-chirp; green gate image answers source; no random whoosh, music sting, unrelated sound, or hidden source" instead of "match sound into next scene" | Sound shape, cut point, matching source, difference cue, image answer, payoff, and mix takeover are audible/visible |
| Sound / music style anchor | Assign a named sound designer/composer/film-score reference to one audio layer, mechanism, forbidden transfers, name-free fallback, and review gate | "borrow only subjective listening + one offscreen bell; no copied score, melody, motif, sound logo, famous cue, or full soundtrack imitation" instead of "sound like X" | Hearing owner, primary cue, mix hierarchy, silence curve, visible reaction, and no sonic-signature copy are audible/reviewable |
| Subjective listening POV | Name hearing owner, condition, filter stack, removed layers, remaining cue anchor, transition, visible consequence, and post cue fallback | "heard from the character behind a closed metal door; room tone collapses to ringing; footsteps become muffled low pulses; breath remains sharp" instead of "muffled subjective sound" | Hearing POV, layer removal, remaining cue, source status, and visual reaction belong to the same listener |
| Action contact proof | Name attack, receiver response, changed state | "receiver staggers into table" instead of "no fake hit" | Impact creates body/environment consequence |
| Material realism | Name surface, light response, and motion | "wet leather catches rim light as it flexes" instead of "not plastic" | Texture reacts to light and motion |
| Source-zone-material lighting | Name source, affected zone, excluded zone, shadow edge, separation method, material responses, and exposure boundary | "no full-frame color wash; no random glow; no plastic skin; no unmotivated rim" instead of "cinematic lighting" | Source direction, color pool, excluded zone, shadow behavior, separation, and material response are all visible |
| Lighting / color transition | Name before-state, trigger, source/zone change, excluded zone, exposure/shadow ramp, material response, and after-state | "no full-frame color wash, random flicker, unmotivated neon, or lost key detail" instead of "mood shifts blue" | Before/after light state, trigger, zones, material response, separation, and story consequence are visible |
| Editing rhythm | Name duration, beat anchor, reaction breath, and changed state | "no random fast cutting; preserve the reaction hold" instead of "make it punchy" | Setup, trigger, reaction, and state change are visible/audible |
| Beat anchor / cut permission | Name shot count limit, rhythm source, allowed cut triggers, viewer registration hold, density curve, sound/music relationship, and final state | "no random fast cutting; no cutting on every beat; no montage fragments; preserve the reveal/reaction hold" instead of "dynamic editing" | Every cut/hold is authorized by breath, glance, grip, impact, sound cue, reveal, or camera stop |
| Mass / speed / recovery | Name mass profile, preload, acceleration spike, peak, response, follow-through, braking, and recovery | "no constant high speed; no weightless spin; no camera shake hiding impact" instead of "make it heavy and fast" | Weight is proven by load, speed contrast, delayed response, and settled recovery |
| Action camera responsibility | Assign one camera proof job, proof frame, shake/blur budget, subject relation, and consequence view | "no whip shake; no random close-ups; no foreground cover at contact; no cutting away at impact" instead of "dynamic camera" | Geography, action path, contact, receiver response, and recovered spacing are visible |
| Fictional danger / safety boundary | Build danger from geography, vulnerability cue, near-miss/block proof, consequence, recovery, and explicit fiction-only boundary | "no gore, injury detail, real weapon/stunt technique, how-to choreography, or shaky blur hiding the near-miss" instead of "make it brutally dangerous" | Danger is readable through route, exposed state, near-miss, object/environment consequence, recovery, and no operational details |
| Action director / fight style anchor | Assign a named action director/film/team reference to one action layer, screen-safe mechanism, forbidden transfers, name-free fallback, and review gate | "borrow only arena roadmap + one contact-proof beat + recovery breath; no copied combo, stunt method, gore, weapon tutorial, costume, or style soup" instead of "fight like X" | Geography, proof frame, receiver/environment response, rhythm recovery, changed spacing, and non-operational boundary are visible |
| Clip breakdown transfer | Convert objective evidence -> shot function -> function chain -> original prompt fields | "extract reveal logic only; do not copy scene, characters, dialogue, or exact staging" | Output proves the function chain without depending on the source scene |
| Clip-to-prompt review loop | Convert objective breakdown -> function chain -> portable mechanism -> original prompt -> generated-output review | "source use: extract mechanism only; no copied characters, plot, dialogue, exact staging, famous composition, or director/style name" instead of "make it like this scene" | Generated output proves the borrowed mechanism in an original scene and names one minimum retry delta if it fails |
| Prepared target / state change | Show before-state, target relation, trigger, after-state, and hold | "one clock socket changes from empty to engaged; no Moon/rocket imagery" instead of "arrives dramatically" | Initial state, action path, contact, changed state, and hold are all visible |
| Character / prop continuity | Assign reference roles, durable anchors, allowed changes, forbidden drift, and review checks | "same face/hair/costume/prop/layout; allow pose, expression, crop, cloth motion; no merged references" instead of "keep consistent" | Identity, costume, prop, layout, and style survive motion or shot change |
| Production design / worldbuilding style anchor | Assign a named film/designer/world/prop reference to one design layer, story mechanism, forbidden transfers, name-free fallback, and review gate | "borrow only spatial access rule + prop function; no copied franchise world, iconic prop, costume silhouette, set layout, logo, or signature palette" instead of "make it look like X world" | Space shows access/obstacle/status; props have jobs; material wear matches use; no IP design leakage |
| Style anchor role | Assign each named film/person/studio/reference one controlled layer, one mechanism, forbidden transfers, compatibility check, and name-free fallback | "extract mechanism only; no copied scene, characters, plot, exact staging, signature palette, living-artist imitation, or merged references" instead of "in the style of X" | Each anchor's contribution is visible, bounded, compatible, and original |
| Editor / rhythm style anchor | Assign a named editor/director/film rhythm reference to one timing layer, allowed mechanism, forbidden transfers, name-free fallback, and review gate | "borrow only sound-led reveal plus 1s reaction hold; no copied sequence, dialogue, plot twist, exact montage, palette, or style soup" instead of "edit like X" | Reference contributes only the allowed rhythm mechanism and the scene remains original |
| Transition / match-cut style anchor | Assign a named editor/film/sequence transition reference to one match layer, outgoing element, incoming element, bridge logic, forbidden transfers, name-free fallback, and review gate | "borrow only graphic match logic; match clock stamp to elevator indicator; no copied iconic objects, plot leap, score cue, exact composition, or source-scene identity" instead of "use the match cut from X" | Match type, outgoing/incoming elements, bridge logic, changed information, and source-copy guard are visible |
| Documentary / realism style anchor | Assign a documentary/direct-cinema/observational/archive reference to evidence status, camera relation, subject awareness, sync sound, staging boundary, and non-deceptive review gate | "fictional staged scene; handheld witness camera, available light, live room tone; no real outlet, official mark, event claim, date/location claim, or hidden-camera claim" instead of "make it look like real news footage" | Realism comes from camera/sound/staging relation while fiction or reconstruction status remains bounded |
| Archival / found-footage insert | Assign an old-media insert to source status, diegetic owner/viewer, one or two artifact layers, continuity relation, label policy, and non-forgery review gate | "fictional diegetic training tape; invented shelf code; mild gate weave, two dust scratches, soft tape hiss; no real archive watermark, news outlet, official seal, date/location claim, or forged evidence" instead of "make it look like real archive footage" | Insert source status, artifact layer, clue continuity, and non-forgery boundary are visible |
| Title / card / intertitle graphic insert | Assign onscreen text to exact payload, typography role, safe placement, reading duration, transition relation, subtitle/action conflict check, and design-copy guard | "black intertitle card, exact text 'THREE HOURS EARLIER', plain centered white type, 1.5-second hold; no logos, extra words, branded font identity, moving glyphs, or copied title sequence" instead of "cool cinematic typography" | Exact text, legibility, duration, placement, transition function, and no design-copy leakage are visible |
| Map / diagram / screen UI insert | Assign UI graphics to diegetic status, owner/viewer, one information payload, placement, interaction timing, label budget, hierarchy, and clutter guard | "physical desk monitor shows route A blocked and stairs open; three labels only; character looks, then turns toward stairs; no fake OS, real map service, dense panels, random numbers, microtext, or decorative HUD clutter" instead of "cool sci-fi interface" | Screen surface, payload, labels, timing, and changed behavior are visible |
| Split-screen / multi-panel layout | Assign panel layout to count, geometry, panel ownership, temporal relation, viewer priority cue, sound/motion focus, seam logic, and collage guard | "two vertical panels; left courier at locked door, right guard presses door control simultaneously; right panel owns hand motion, then left panel owns lock reaction; no extra panels, moving borders, unrelated action, or competing sound" instead of "show multiple things at once" | Panel count, timing relation, priority cue, seam stability, and changed state are visible |
| Rapid montage / short sequence | Assign montage to function, shot count, ordered beats, transition logic, density curve, sound relation, final proof hold, and copied-pattern guard | "6-second montage, four shots maximum: empty case -> tool selected -> red seal stamped -> case locked; one new fact per shot; final 1s hold on locked case" instead of "fast dynamic montage" | Shot count, beat function, order, density, transition logic, and final proof hold are visible |
| Voiceover / narration | Assign narration to narrator status, source, one information payload, timing relative to image, image relation, mix priority, and redundancy guard | "non-diegetic narrator starts after sealed door reveal; one short line reframes the image; no repeated visible action, extra backstory, celebrity voice, fake authority, or dialogue overlap" instead of "add cinematic narration" | Narrator status, timing, image relation, mix, and non-redundancy are audible/reviewable |
| Subjective memory / flashback insert | Assign memory insert to present anchor, trigger cue, memory status, one past payload, texture budget, return anchor, and confusion guard | "thumb touches cracked locket; 1-second subjective memory of same locket unbroken; return to same thumb on cracked locket; no sepia wash, unrelated childhood scene, or full backstory" instead of "dreamy flashback" | Present trigger, past payload, texture difference, return anchor, and past/present separation are visible |
| Subjective imagination / dream / hallucination insert | Assign unreality to subjective owner, trigger, subjective status, reality boundary, one unreal payload, texture budget, return/reveal anchor, and representation guard | "she stares at the door handle; imagined fear image: dark water seeps under the door for 0.8s; return to same dry floor; no horror filter, diagnosis, mental-illness stereotype, gore, or extra impossible events" instead of "make it hallucinatory" | Subjective owner, trigger, unreal payload, reality correction, texture budget, and non-stigmatizing boundary are visible |
| Unreliable perception / reality reveal edit | Assign reveal to evidence status, false cue, allowed false inference, viewer knowledge state, correction beat, truth anchor, hold time, and no-cheat guard | "doorway angle makes coat on chair read as person; she steps right; reveal chair legs and hold on same coat, empty room; no teleport, hidden extra person, jump scare, or late evidence" instead of "make a twist reveal" | False cue, inference, correction movement, truth anchor, hold time, and no-cheat boundary are visible |
| Object clue / evidence insert | Assign clue to status, attention cue, one readable payload, owner/viewer timing, payoff beat, red-herring boundary, and evidence/forgery guard | "focus pull to brass key tag number 14 for 0.8s; viewer sees before character; later she looks to locker 14; no puzzle wall, fake police label, real institution, or extra clue clutter" instead of "show a clue" | Clue status, readable payload, attention cue, payoff relation, and non-forgery boundary are visible |
| Wardrobe / costume clue | Assign clothing to garment status, one wardrobe payload, attention cue, owner/viewer timing, social/character signal, payoff beat, continuity relation, and copy/brand guard | "borrowed uniform jacket is too short at both cuffs; character pulls sleeves down as guard notices; guard asks for missing badge; no real agency logo, fashion label, iconic costume, or recognizable uniform" instead of "outfit tells a story" | Garment status, readable clothing payload, attention cue, payoff, continuity, and no brand/IP leakage are visible |
| Makeup / hair / body-state clue | Assign appearance to status, one readable payload, attention cue, owner/viewer timing, story consequence, continuity side/zone, and identity/safety guard | "one soot smudge under left cheekbone plus damp hair at left temple; she wipes it, partner notices and chooses service exit; no wound detail, diagnosis, celebrity likeness, prosthetic identity swap, or beauty filter" instead of "make her look tired" | Appearance payload, attention cue, story consequence, continuity side, and identity/safety boundary are visible |
| Hand / object interaction clue | Assign interaction to hand owner, object payload, start state, contact proof, transfer/conceal-reveal action, end state, attention cue, continuity side, payoff, and fake-contact/safety guard | "left thumb and index finger pinch brass token, slide it under lower-right map corner, token edge remains visible; later same map corner reveals it; no hand swap, object teleport, hidden cut, fake touch, or real theft method" instead of "close-up of secret handoff" | Hand owner, object identity, contact proof, path, final state, continuity side, and payoff are visible |
| Object placement / set-dressing clue | Assign decor to placement status, one placement payload, baseline state, changed/payoff state, viewer priority cue, spatial relation, payoff beat, and clutter guard | "earlier chair tucked under desk; later same chair pulled 30 cm out and angled toward back window; lamp highlights chair legs; no extra suspicious props, labels, clue board, new furniture, or puzzle-room clutter" instead of "background full of clues" | Placement payload, baseline/change, viewer priority, payoff, and clutter boundary are visible |
| Spatial path / blocking clue | Assign route to status, start position, obstruction/reveal, actor path proof, end position, screen direction/geography, attention cue, payoff, and false-geography guard | "she starts screen-left at archive doorway, takes three steps left along desk edge, shelf gap reveals back-right stairwell, eyeline lands on handle; no teleport, new room, impossible hallway, random cutaway, or camera-only reveal" instead of "character discovers a path" | Route status, start/end positions, obstruction, actor path, geography, eyeline, and payoff are visible |
| Eyeline / gaze-target clue | Assign gaze to owner, gaze cue, target status, answer shot, knowledge state, spatial relation, timing/hold, payoff, and random-gaze guard | "eyes shift down-right to red keycard; cut to same keycard for 0.7s; viewer and character learn together; no wandering eyes, extra targets, reversed direction, or target appearing late" instead of "her eyes reveal the clue" | Gaze owner, target, answer shot, knowledge state, spatial relation, and payoff are visible |
| Reaction / response ownership clue | Assign reaction to trigger owner, response owner, timing, micro-behavior proof, knowledge shift, coverage rule, pressure object/space, payoff, and generic-acting guard | "door lock clicks at 3s; hold on courier; breath stops, right hand releases strap, she steps back; no random sad face, tears, speech, extra clue, or reaction without cue" instead of "show her reaction" | Trigger, response owner, timing, micro-behavior, knowledge shift, pressure object/space, and payoff are visible |
| Held silence / pause clue | Assign pause to silence owner, removed layers, remaining cue, pressure object/space, decision state, visual stillness, release cue, payoff, and dead-air guard | "music and corridor chatter drop; only breath, room tone, and key-ring sway remain; she decides not to knock and turns away" instead of "dramatic silence" | Silence owner, removed layers, remaining cue, pressure object/space, decision state, release cue, and payoff are visible/audible |
| Shot handoff continuity | Convert last frame into inherited state plus new-shot permission and bridge type | "start from previous raised scanner and rightward eyeline; no pose reset, hand swap, reversed corridor, or style reset" instead of "continue the scene" | First frame inherits pose/prop/action phase; screen direction holds; new shot adds information |
| Mechanical deployment | Name form A/B, stored-volume source, mechanism family, stage chain, mass/regrip, and final lock | "no soft morph; no duplicate parts; no instant skin swap; active seam stays visible" instead of "transform smoothly" | Stages are visible, parts come from named zones, final lock settles, and handling changes |

## Generated Contract Review Sheet

Use this after a generated image/video exists. Review the generated contract before judging taste. If one row fails, repair that row with a minimum retry delta instead of rewriting the whole prompt.

```text
output_id:
platform / mode:
source prompt:
reference assets:
duration / aspect / settings:

contract summary:
  one dominant event:
  must-preserve anchors:
  must-change event:
  review priority:

evidence gates:
  subject / identity:
    expected:
    observed:
    pass / partial / fail:
    likely cause:
  action / state change:
    expected:
    observed:
    pass / partial / fail:
    likely cause:
  camera / lens / framing:
    expected:
    observed:
    pass / partial / fail:
    likely cause:
  space / screen direction:
    expected:
    observed:
    pass / partial / fail:
    likely cause:
  light / color / material:
    expected:
    observed:
    pass / partial / fail:
    likely cause:
  sound / timing, if supported:
    expected:
    observed:
    pass / partial / fail:
    likely cause:
  style / reference role:
    expected:
    observed:
    pass / partial / fail:
    likely cause:
  continuity / temporal stability:
    expected:
    observed:
    pass / partial / fail:
    likely cause:
  final state / viewer information:
    expected:
    observed:
    pass / partial / fail:
    likely cause:

failure attribution ladder:
  missing prompt field:
  conflicting prompt field:
  prompt overload:
  platform / mode limit:
  reference-role leakage:
  model miss despite clear prompt:

minimum retry delta:
  keep successful gates:
  fix one failed gate:
  add positive control:
  rewrite risky negative as positive:
  remove conflicting detail:
  expected proof in retry:
```

### Generated Contract Review Table

| Gate | Review question | Common failure | Minimum retry delta |
| --- | --- | --- | --- |
| Subject / identity | Did the same subject remain recognizable by the named anchors? | face, costume, prop, or species drift | Add 3-5 durable anchors; separate identity from costume/prop/style references |
| Action / state change | Did the clip show before-state, trigger, change, and after-state? | pretty motion with no consequence | Add visible before/after state and one hold after the change |
| Camera / lens / framing | Did the camera do the named job without hiding proof? | random zoom, hidden contact, wrong distance | Name camera job, start/end frame, subject relation, and proof frame |
| Space / screen direction | Did geography, eyeline, or left/right relation remain legible? | reversed direction, erased target, unclear barrier | Lock axis side, target side, foreground/background relation, and bridge cue |
| Light / color / material | Did source, zone, shadow, separation, and surface response match? | full-frame tint, fake rim, plastic material | Name source -> zone -> excluded zone -> material response |
| Sound / timing | Did the cue happen in the intended time window and cause visible consequence? | missing cue, generic music, desync | Make one primary audio event with source, obstruction, listener point, and mix priority |
| Style / reference role | Did each reference control only its assigned layer? | style soup, copied scene, merged references | Add reference role, forbidden transfer, name-free fallback, and no-copy boundary |
| Continuity / temporal stability | Did important anchors persist across frames or shots? | flicker, object morph, pose reset | Carry inherited state and allowed changes; forbid resets only for critical anchors |
| Final viewer information | Does the last beat leave the viewer with the intended new knowledge? | attractive clip but no story result | Add final-state hold and state exactly what the viewer learns |

### Minimum Generated-Output Review Prompt

```text
Review the generated clip against the prompt contract before judging taste.
Check gates in order: subject identity, action/state change, camera proof, space/screen direction, light/material, sound timing, style/reference role, continuity, final viewer information.
For each failed gate, name observed evidence and likely cause: missing field, conflicting field, overload, platform limit, reference leakage, or model miss.
Retry with one minimum delta only; preserve every gate that already passed.
```

## Minimum Prompt Delta

```text
Keep:
Fix one failed field:
Add positive control:
Rewrite risky negative as positive:
Expected proof in output:
Do not change:
```
