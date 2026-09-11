#!/usr/bin/env python3
"""Extract timestamped evidence and basic diagnostics from a video file."""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
from pathlib import Path


def load_dependencies():
    try:
        import cv2
        import imageio_ffmpeg
        import numpy as np
        from PIL import Image, ImageDraw, ImageFont
    except ImportError as exc:
        raise SystemExit(
            "Missing video-review dependencies. Run this script with the bundled Codex "
            "Python runtime or an environment containing opencv-python, numpy, Pillow, "
            f"and imageio-ffmpeg. Original error: {exc}"
        )
    return cv2, imageio_ffmpeg, np, Image, ImageDraw, ImageFont


cv2, imageio_ffmpeg, np, Image, ImageDraw, ImageFont = load_dependencies()


def find_program(name: str) -> str | None:
    resolved = shutil.which(name)
    if resolved:
        return resolved

    packages = (
        Path.home()
        / "AppData"
        / "Local"
        / "Microsoft"
        / "WinGet"
        / "Packages"
    )
    patterns = {
        "ffmpeg": "Gyan.FFmpeg_*/*/bin/ffmpeg.exe",
        "ffprobe": "Gyan.FFmpeg_*/*/bin/ffprobe.exe",
        "mediainfo": "MediaArea.MediaInfo_*/MediaInfo.exe",
    }
    candidates = list(packages.glob(patterns[name])) if name in patterns else []
    if candidates:
        return str(max(candidates, key=lambda path: path.stat().st_mtime))

    if name == "ffmpeg":
        return imageio_ffmpeg.get_ffmpeg_exe()
    return None


def run_json(command: list[str]) -> dict | None:
    proc = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if proc.returncode != 0:
        return None
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None


def timestamp(seconds: float) -> str:
    seconds = max(0.0, seconds)
    minutes = int(seconds // 60)
    remainder = seconds - minutes * 60
    return f"{minutes:02d}:{remainder:05.2f}"


def stream_metadata(video_path: Path) -> dict:
    ffprobe = find_program("ffprobe")
    ffmpeg = find_program("ffmpeg")
    mediainfo = find_program("mediainfo")
    ffprobe_data = None
    mediainfo_data = None

    if ffprobe:
        ffprobe_data = run_json(
            [
                ffprobe,
                "-v",
                "error",
                "-show_format",
                "-show_streams",
                "-of",
                "json",
                str(video_path),
            ]
        )
    if mediainfo:
        mediainfo_data = run_json([mediainfo, "--Output=JSON", str(video_path)])

    if ffprobe_data:
        streams = ffprobe_data.get("streams", [])
        video = next(
            (stream for stream in streams if stream.get("codec_type") == "video"), {}
        )
        audio = next(
            (stream for stream in streams if stream.get("codec_type") == "audio"), {}
        )
        format_data = ffprobe_data.get("format", {})
        return {
            "ffmpeg_executable": ffmpeg,
            "ffprobe_executable": ffprobe,
            "mediainfo_executable": mediainfo,
            "video_codec": video.get("codec_name"),
            "video_profile": video.get("profile"),
            "pixel_format": video.get("pix_fmt"),
            "color_space": video.get("color_space"),
            "color_transfer": video.get("color_transfer"),
            "color_primaries": video.get("color_primaries"),
            "audio_codec": audio.get("codec_name"),
            "audio_sample_rate": audio.get("sample_rate"),
            "audio_channels": audio.get("channels"),
            "has_audio": bool(audio),
            "reported_duration_seconds": float(format_data.get("duration"))
            if format_data.get("duration")
            else None,
            "bit_rate": int(format_data.get("bit_rate"))
            if format_data.get("bit_rate")
            else None,
            "ffprobe": ffprobe_data,
            "mediainfo": mediainfo_data,
        }

    if not ffmpeg:
        return {
            "ffmpeg_executable": None,
            "ffprobe_executable": None,
            "mediainfo_executable": mediainfo,
            "has_audio": False,
            "mediainfo": mediainfo_data,
        }
    proc = subprocess.run(
        [ffmpeg, "-hide_banner", "-i", str(video_path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    info = proc.stderr
    video_match = re.search(
        r"Video:\s*([^,\s]+).*?(\d{2,5})x(\d{2,5}).*?(\d+(?:\.\d+)?)\s*fps",
        info,
        re.I,
    )
    audio_match = re.search(r"Audio:\s*([^,\s]+)", info, re.I)
    duration_match = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", info)
    duration = None
    if duration_match:
        duration = (
            int(duration_match.group(1)) * 3600
            + int(duration_match.group(2)) * 60
            + float(duration_match.group(3))
        )
    return {
        "ffmpeg_executable": ffmpeg,
        "ffprobe_executable": None,
        "mediainfo_executable": mediainfo,
        "video_codec": video_match.group(1) if video_match else None,
        "audio_codec": audio_match.group(1) if audio_match else None,
        "has_audio": bool(audio_match),
        "reported_duration_seconds": duration,
        "mediainfo": mediainfo_data,
    }


def professional_scene_detection(video_path: Path) -> dict:
    try:
        from scenedetect import AdaptiveDetector, detect
    except ImportError:
        return {"available": False, "detector": None, "scenes": []}

    try:
        scenes = detect(
            str(video_path),
            AdaptiveDetector(),
            show_progress=False,
            start_in_scene=True,
        )
    except Exception as exc:
        return {
            "available": True,
            "detector": "PySceneDetect AdaptiveDetector",
            "error": str(exc),
            "scenes": [],
        }

    result = []
    for index, (start, end) in enumerate(scenes, start=1):
        start_frame = start.frame_num
        end_frame = max(start_frame, end.frame_num - 1)
        start_seconds = start.seconds
        end_seconds = end.seconds
        result.append(
            {
                "scene": index,
                "start_frame": start_frame,
                "end_frame": end_frame,
                "start_seconds": round(start_seconds, 3),
                "end_seconds": round(end_seconds, 3),
                "start_timecode": start.get_timecode(),
                "end_timecode": end.get_timecode(),
                "duration_seconds": round(end_seconds - start_seconds, 3),
            }
        )
    return {
        "available": True,
        "detector": "PySceneDetect 0.7 AdaptiveDetector",
        "scenes": result,
    }


def ffmpeg_signal_analysis(video_path: Path, has_audio: bool) -> dict:
    ffmpeg = find_program("ffmpeg")
    if not ffmpeg:
        return {"available": False}

    command = [
        ffmpeg,
        "-hide_banner",
        "-nostats",
        "-i",
        str(video_path),
        "-vf",
        "blackdetect=d=0.20:pix_th=0.10,freezedetect=n=-50dB:d=0.50",
    ]
    if has_audio:
        command += [
            "-af",
            "silencedetect=n=-45dB:d=0.35,ebur128=peak=true",
        ]
    command += ["-f", "null", "NUL"]
    proc = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    log = proc.stderr

    black_segments = [
        {
            "start_seconds": float(start),
            "end_seconds": float(end),
            "duration_seconds": float(duration),
        }
        for start, end, duration in re.findall(
            r"black_start:([0-9.]+)\s+black_end:([0-9.]+)\s+black_duration:([0-9.]+)",
            log,
        )
    ]
    freeze_events = [
        {"type": event, "seconds": float(seconds)}
        for event, seconds in re.findall(
            r"lavfi\.freezedetect\.freeze_(start|end|duration):\s*([0-9.]+)",
            log,
        )
    ]
    silence_events = [
        {
            "type": event,
            "seconds": float(seconds),
            "duration_seconds": float(duration) if duration else None,
        }
        for event, seconds, duration in re.findall(
            r"silence_(start|end):\s*([0-9.]+)(?:\s*\|\s*silence_duration:\s*([0-9.]+))?",
            log,
        )
    ]

    loudness = None
    summary = log.rsplit("Summary:", 1)[-1] if "Summary:" in log else ""
    integrated = re.search(r"\bI:\s*(-?[0-9.]+)\s+LUFS", summary)
    range_match = re.search(r"\bLRA:\s*([0-9.]+)\s+LU", summary)
    peak = re.search(r"\bPeak:\s*(-?[0-9.]+)\s+dBFS", summary)
    if integrated or range_match or peak:
        loudness = {
            "integrated_lufs": float(integrated.group(1)) if integrated else None,
            "loudness_range_lu": float(range_match.group(1)) if range_match else None,
            "true_peak_dbfs": float(peak.group(1)) if peak else None,
        }

    return {
        "available": True,
        "ffmpeg_executable": ffmpeg,
        "black_segments": black_segments,
        "freeze_events": freeze_events,
        "silence_events": silence_events,
        "loudness": loudness,
        "return_code": proc.returncode,
    }


def frame_metrics(frame_bgr, previous_gray=None) -> tuple[dict, object]:
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2HSV)
    brightness = float(gray.mean())
    saturation = float(hsv[:, :, 1].mean())
    sharpness = float(cv2.Laplacian(gray, cv2.CV_64F).var())
    black_ratio = float((gray < 8).mean())
    highlight_ratio = float((gray > 247).mean())
    motion = None
    if previous_gray is not None:
        resized = cv2.resize(gray, (previous_gray.shape[1], previous_gray.shape[0]))
        motion = float(cv2.absdiff(previous_gray, resized).mean())
    small = cv2.resize(gray, (8, 8), interpolation=cv2.INTER_AREA)
    hash_bits = "".join("1" if value >= small.mean() else "0" for value in small.flat)
    average_hash = f"{int(hash_bits, 2):016x}"
    return {
        "brightness_mean": round(brightness, 2),
        "saturation_mean": round(saturation, 2),
        "sharpness_laplacian": round(sharpness, 2),
        "black_ratio": round(black_ratio, 4),
        "highlight_clip_ratio": round(highlight_ratio, 4),
        "motion_from_previous_sample": round(motion, 2) if motion is not None else None,
        "average_hash": average_hash,
    }, gray


def scan_transitions(cap, fps: float, frame_count: int) -> tuple[list[dict], dict]:
    step = max(1, int(round(fps / 4))) if fps > 0 else max(1, frame_count // 200)
    previous_gray = None
    previous_hist = None
    candidates = []
    motion_values = []
    brightness_values = []

    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    index = 0
    while index < frame_count:
        cap.set(cv2.CAP_PROP_POS_FRAMES, index)
        ok, frame = cap.read()
        if not ok:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_small = cv2.resize(gray, (160, 90), interpolation=cv2.INTER_AREA)
        hist = cv2.calcHist([gray_small], [0], None, [32], [0, 256])
        cv2.normalize(hist, hist)
        brightness = float(gray_small.mean())
        brightness_values.append(brightness)

        if previous_gray is not None and previous_hist is not None:
            motion = float(cv2.absdiff(previous_gray, gray_small).mean())
            hist_distance = float(
                cv2.compareHist(previous_hist, hist, cv2.HISTCMP_BHATTACHARYYA)
            )
            motion_values.append(motion)
            score = hist_distance * 0.65 + min(motion / 64.0, 1.0) * 0.35
            candidates.append(
                {
                    "frame_index": index,
                    "time_seconds": round(index / fps, 3) if fps > 0 else None,
                    "timecode": timestamp(index / fps) if fps > 0 else None,
                    "transition_score": round(score, 4),
                    "histogram_distance": round(hist_distance, 4),
                    "frame_difference": round(motion, 2),
                }
            )
        previous_gray = gray_small
        previous_hist = hist
        index += step

    candidates.sort(key=lambda item: item["transition_score"], reverse=True)
    selected = []
    minimum_gap = max(0.35, step / fps if fps > 0 else 0.5)
    for item in candidates:
        if item["transition_score"] < 0.24:
            break
        if all(
            abs((item["time_seconds"] or 0) - (chosen["time_seconds"] or 0))
            >= minimum_gap
            for chosen in selected
        ):
            selected.append(item)
        if len(selected) >= 12:
            break
    selected.sort(key=lambda item: item["frame_index"])
    scan = {
        "scan_step_frames": step,
        "median_motion_difference": round(float(np.median(motion_values)), 2)
        if motion_values
        else None,
        "max_motion_difference": round(float(max(motion_values)), 2)
        if motion_values
        else None,
        "brightness_range": round(float(max(brightness_values) - min(brightness_values)), 2)
        if brightness_values
        else None,
    }
    return selected, scan


def choose_sample_indices(frame_count: int, samples: int) -> list[int]:
    if frame_count <= 0:
        return []
    count = min(max(3, samples), frame_count)
    return sorted({int(round(value)) for value in np.linspace(0, frame_count - 1, count)})


def extract_frames(
    cap,
    indices: list[int],
    fps: float,
    frames_dir: Path,
    prefix: str,
) -> list[dict]:
    items = []
    previous_gray = None
    for order, frame_index in enumerate(indices):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ok, frame = cap.read()
        if not ok:
            continue
        time_seconds = frame_index / fps if fps > 0 else 0.0
        metrics, previous_gray = frame_metrics(frame, previous_gray)
        filename = f"{prefix}_{order:02d}_{time_seconds:07.2f}s.jpg"
        frame_path = frames_dir / filename
        cv2.imwrite(str(frame_path), frame, [int(cv2.IMWRITE_JPEG_QUALITY), 94])
        items.append(
            {
                "frame_index": frame_index,
                "time_seconds": round(time_seconds, 3),
                "timecode": timestamp(time_seconds),
                "path": str(frame_path),
                "metrics": metrics,
            }
        )
    return items


def make_contact_sheet(items: list[dict], output_path: Path, metadata: dict) -> None:
    if not items:
        return
    columns = 4 if len(items) >= 8 else 3
    thumb_width = 420
    label_height = 58
    header_height = 72
    first = Image.open(items[0]["path"])
    ratio = first.height / first.width
    thumb_height = max(180, int(thumb_width * ratio))
    rows = math.ceil(len(items) / columns)
    sheet = Image.new(
        "RGB",
        (columns * thumb_width, header_height + rows * (thumb_height + label_height)),
        "#111111",
    )
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    header = (
        f"{metadata['filename']} | {metadata['width']}x{metadata['height']} | "
        f"{metadata['fps']:.3f} fps | {metadata['duration_seconds']:.2f}s | "
        f"audio: {'yes' if metadata.get('has_audio') else 'no'}"
    )
    draw.text((14, 12), header, fill="white", font=font)
    draw.text(
        (14, 38),
        "B=brightness  S=saturation  Sharp=Laplacian variance  M=sample-to-sample change",
        fill="#bbbbbb",
        font=font,
    )

    for position, item in enumerate(items):
        row, column = divmod(position, columns)
        x = column * thumb_width
        y = header_height + row * (thumb_height + label_height)
        image = Image.open(item["path"]).convert("RGB")
        image.thumbnail((thumb_width, thumb_height), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (thumb_width, thumb_height), "black")
        canvas.paste(
            image,
            ((thumb_width - image.width) // 2, (thumb_height - image.height) // 2),
        )
        sheet.paste(canvas, (x, y))
        metrics = item["metrics"]
        draw.text(
            (x + 8, y + thumb_height + 7),
            f"{item['timecode']}  frame {item['frame_index']}",
            fill="white",
            font=font,
        )
        motion = metrics["motion_from_previous_sample"]
        draw.text(
            (x + 8, y + thumb_height + 28),
            f"B {metrics['brightness_mean']:.1f}  S {metrics['saturation_mean']:.1f}  "
            f"Sharp {metrics['sharpness_laplacian']:.1f}  M {motion if motion is not None else '-'}",
            fill="#c8c8c8",
            font=font,
        )
    sheet.save(output_path, quality=92)


def technical_flags(
    samples: list[dict],
    scan: dict,
    signal_analysis: dict,
) -> list[dict]:
    flags = []
    if not samples:
        return [{"severity": "blocking", "message": "No sample frames were decoded."}]
    if any(item["metrics"]["black_ratio"] > 0.92 for item in samples):
        flags.append(
            {
                "severity": "major",
                "message": "At least one sampled frame is almost entirely black.",
            }
        )
    sharpness = [item["metrics"]["sharpness_laplacian"] for item in samples]
    if float(np.median(sharpness)) < 35:
        flags.append(
            {
                "severity": "review",
                "message": "Median sampled-frame sharpness is low; verify whether blur is intentional.",
            }
        )
    if scan.get("brightness_range") is not None and scan["brightness_range"] > 90:
        flags.append(
            {
                "severity": "review",
                "message": "Large brightness range detected; inspect for intentional cuts versus exposure flicker.",
            }
        )
    motion = [
        item["metrics"]["motion_from_previous_sample"]
        for item in samples
        if item["metrics"]["motion_from_previous_sample"] is not None
    ]
    if motion and float(np.median(motion)) < 1.2:
        flags.append(
            {
                "severity": "review",
                "message": "Very low change between sampled frames; inspect for frozen or repetitive motion.",
            }
        )
    if signal_analysis.get("black_segments"):
        flags.append(
            {
                "severity": "review",
                "message": "FFmpeg detected black-frame segments; verify whether they are intentional.",
            }
        )
    if signal_analysis.get("freeze_events"):
        flags.append(
            {
                "severity": "review",
                "message": "FFmpeg detected a possible frozen-frame interval.",
            }
        )
    loudness = signal_analysis.get("loudness") or {}
    if loudness.get("true_peak_dbfs") is not None and loudness["true_peak_dbfs"] > -1.0:
        flags.append(
            {
                "severity": "review",
                "message": "Audio true peak is above -1 dBFS; inspect for delivery headroom.",
            }
        )
    return flags


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create timestamped review evidence for an AI-generated video."
    )
    parser.add_argument("video", help="Input video path")
    parser.add_argument("--output", help="Output directory")
    parser.add_argument("--samples", type=int, default=12, help="Uniform sample count")
    args = parser.parse_args()

    video_path = Path(args.video).expanduser().resolve()
    if not video_path.exists():
        raise SystemExit(f"Video not found: {video_path}")
    output_dir = (
        Path(args.output).expanduser().resolve()
        if args.output
        else video_path.with_name(f"{video_path.stem}_review")
    )
    frames_dir = output_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise SystemExit(f"Could not decode video: {video_path}")

    fps = float(cap.get(cv2.CAP_PROP_FPS) or 0)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 0)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0)
    duration = frame_count / fps if fps > 0 else 0.0
    streams = stream_metadata(video_path)
    scenes = professional_scene_detection(video_path)
    signal_analysis = ffmpeg_signal_analysis(video_path, streams.get("has_audio", False))
    transitions, scan = scan_transitions(cap, fps, frame_count)

    sample_items = extract_frames(
        cap,
        choose_sample_indices(frame_count, args.samples),
        fps,
        frames_dir,
        "uniform",
    )
    scene_indices = [
        int(round((scene["start_frame"] + scene["end_frame"]) / 2))
        for scene in scenes.get("scenes", [])
    ]
    scene_items = extract_frames(cap, scene_indices, fps, frames_dir, "scene")
    cap.release()

    metadata = {
        "input": str(video_path),
        "filename": video_path.name,
        "width": width,
        "height": height,
        "fps": fps,
        "frame_count": frame_count,
        "duration_seconds": duration,
        **streams,
    }
    contact_sheet = output_dir / "contact_sheet.jpg"
    make_contact_sheet(sample_items, contact_sheet, metadata)
    scene_contact_sheet = output_dir / "scene_contact_sheet.jpg"
    make_contact_sheet(scene_items, scene_contact_sheet, metadata)
    result = {
        "metadata": metadata,
        "uniform_samples": sample_items,
        "scene_samples": scene_items,
        "professional_scene_detection": scenes,
        "possible_scene_changes": transitions,
        "ffmpeg_signal_analysis": signal_analysis,
        "scan_summary": scan,
        "technical_flags": technical_flags(sample_items, scan, signal_analysis),
        "interpretation_note": (
            "Metrics locate review points only. Verify cuts, flicker, blur, style, "
            "continuity, physics, and aesthetics by direct visual inspection."
        ),
        "outputs": {
            "contact_sheet": str(contact_sheet),
            "scene_contact_sheet": str(scene_contact_sheet)
            if scene_items
            else None,
            "frames_directory": str(frames_dir),
        },
    }
    json_path = output_dir / "review.json"
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "review_json": str(json_path),
                "contact_sheet": str(contact_sheet),
                "scene_contact_sheet": str(scene_contact_sheet)
                if scene_items
                else None,
                "sample_count": len(sample_items),
                "scene_count": len(scenes.get("scenes", [])),
                "possible_scene_changes": len(transitions),
                "duration_seconds": round(duration, 3),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
