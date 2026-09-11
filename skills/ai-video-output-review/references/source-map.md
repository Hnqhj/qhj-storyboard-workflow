# Source Map

Reviewed: 2026-06-18

## Current Platform Context

- ByteDance Seed, Seedance 2.0  
  https://seed.bytedance.com/zh/seedance2_0  
  Mechanism used: multimodal text/image/audio/video references, motion stability, physical-law restoration, audio-visual synchronization, and director-level control make reference-role and audio review part of output acceptance.

- ByteDance Seed, Official Launch of Seedance 2.0  
  https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0  
  Mechanism used: review composition, camera language, motion rhythm, sound characteristics, performance, lighting, and shadow against assigned references rather than judging only frame quality.

## Evaluation Taxonomy

- VBench++  
  https://arxiv.org/abs/2411.13503  
  Mechanism used: decompose generated-video quality into interpretable dimensions such as subject consistency, motion smoothness, temporal flicker, spatial relationships, and aesthetics.

- VBench-2.0  
  https://arxiv.org/abs/2503.21755  
  Mechanism used: include human structure, identity, clothing, physics, and temporal consistency rather than relying on generic visual quality.

- Benchmarking and Evaluating Large Video Generation Models  
  https://arxiv.org/abs/2310.11440  
  Mechanism used: separate visual quality, motion quality, temporal consistency, and text-video alignment.

- VISTA: A Test-Time Self-Improving Video Generation Agent  
  https://arxiv.org/abs/2510.15831  
  Mechanism used: add audio quality, audio-video alignment, physical commonsense, engagement, and beginning/ending/transitions to review.

## Technical Probe

- FFmpeg documentation  
  https://ffmpeg.org/ffmpeg.html  
  Mechanism used: inspect stream metadata and decode frames with a reproducible local toolchain; use blackdetect, freezedetect, silencedetect, and ebur128 as review locators.

- MediaInfo  
  https://mediaarea.net/MediaInfo  
  Mechanism used: report container, codec, frame-rate mode, color, bit-depth, audio, subtitle, and technical tag details in machine-readable form.

- PySceneDetect 0.7 detectors  
  https://www.scenedetect.com/docs/latest/api/detectors.html  
  Mechanism used: AdaptiveDetector compares content change against a rolling average, reducing false cut detections during fast motion compared with a single fixed threshold.

These sources define review dimensions and technical mechanisms. They do not replace project-specific taste or direct visual inspection.
