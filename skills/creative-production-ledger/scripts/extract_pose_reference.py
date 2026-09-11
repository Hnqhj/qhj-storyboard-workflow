#!/usr/bin/env python3
"""Extract a lightweight MediaPipe pose reference from an image or video frame."""

from __future__ import annotations

import argparse
import json
import urllib.request
from pathlib import Path
from typing import Any

import cv2
import mediapipe as mp
import numpy as np


MODEL_URL = (
    "https://storage.googleapis.com/mediapipe-models/pose_landmarker/"
    "pose_landmarker_lite/float16/latest/pose_landmarker_lite.task"
)
DEFAULT_MODEL = Path(r"D:\CodexTools\creative-pipeline\models\pose_landmarker_lite.task")


def load_frame(path: Path, time_seconds: float) -> np.ndarray:
    if path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}:
        image = cv2.imread(str(path), cv2.IMREAD_COLOR)
        if image is None:
            raise SystemExit(f"Could not decode image: {path}")
        return image
    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        raise SystemExit(f"Could not decode video: {path}")
    cap.set(cv2.CAP_PROP_POS_MSEC, max(0.0, time_seconds) * 1000)
    ok, frame = cap.read()
    cap.release()
    if not ok:
        raise SystemExit(f"Could not read frame at {time_seconds:.3f}s: {path}")
    return frame


def ensure_model(path: Path, download: bool) -> None:
    if path.exists():
        return
    if not download:
        raise SystemExit(f"Model not found: {path}. Re-run once with --download-model.")
    path.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(MODEL_URL, path)


def connections() -> list[tuple[int, int]]:
    values = mp.tasks.vision.PoseLandmarksConnections.POSE_LANDMARKS
    result = []
    for value in values:
        start = getattr(value, "start", value[0] if isinstance(value, tuple) else None)
        end = getattr(value, "end", value[1] if isinstance(value, tuple) else None)
        if start is not None and end is not None:
            result.append((int(start), int(end)))
    return result


def landmark_record(item: Any) -> dict[str, float]:
    return {
        "x": round(float(item.x), 6),
        "y": round(float(item.y), 6),
        "z": round(float(item.z), 6),
        "visibility": round(float(item.visibility or 0.0), 6),
        "presence": round(float(item.presence or 0.0), 6),
    }


def draw_pose(
    image: np.ndarray,
    landmarks: list[Any],
    output: Path,
    clean: bool,
    min_visibility: float,
) -> None:
    height, width = image.shape[:2]
    canvas = np.zeros_like(image) if clean else image.copy()
    line_color = (255, 255, 255) if clean else (0, 255, 255)
    point_color = (255, 255, 255) if clean else (0, 80, 255)
    for start, end in connections():
        a, b = landmarks[start], landmarks[end]
        if (a.visibility or 0) < min_visibility or (b.visibility or 0) < min_visibility:
            continue
        p1 = (int(a.x * width), int(a.y * height))
        p2 = (int(b.x * width), int(b.y * height))
        cv2.line(canvas, p1, p2, line_color, 3 if clean else 2, cv2.LINE_AA)
    for index, item in enumerate(landmarks):
        if (item.visibility or 0) < min_visibility:
            continue
        point = (int(item.x * width), int(item.y * height))
        cv2.circle(canvas, point, 5 if clean else 4, point_color, -1, cv2.LINE_AA)
        if not clean:
            cv2.putText(
                canvas,
                str(index),
                (point[0] + 4, point[1] - 4),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35,
                (255, 255, 255),
                1,
                cv2.LINE_AA,
            )
    cv2.imwrite(str(output), canvas)


def midpoint(a: Any, b: Any) -> dict[str, float]:
    return {"x": round((a.x + b.x) / 2, 6), "y": round((a.y + b.y) / 2, 6)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("--output", required=True)
    parser.add_argument("--model", default=str(DEFAULT_MODEL))
    parser.add_argument("--download-model", action="store_true")
    parser.add_argument("--time", type=float, default=0.0, help="Video frame time in seconds")
    parser.add_argument("--min-visibility", type=float, default=0.35)
    parser.add_argument("--num-poses", type=int, default=1)
    args = parser.parse_args()

    source = Path(args.input).expanduser().resolve()
    if not source.exists():
        raise SystemExit(f"Input not found: {source}")
    output = Path(args.output).expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    model = Path(args.model).expanduser().resolve()
    ensure_model(model, args.download_model)
    frame = load_frame(source, args.time)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    options = mp.tasks.vision.PoseLandmarkerOptions(
        base_options=mp.tasks.BaseOptions(model_asset_path=str(model)),
        running_mode=mp.tasks.vision.RunningMode.IMAGE,
        num_poses=args.num_poses,
        min_pose_detection_confidence=0.5,
        min_pose_presence_confidence=0.5,
    )
    with mp.tasks.vision.PoseLandmarker.create_from_options(options) as detector:
        result = detector.detect(image)
    if not result.pose_landmarks:
        raise SystemExit("No pose detected. Try a clearer full/three-quarter-body frame.")

    poses = []
    for index, landmarks in enumerate(result.pose_landmarks):
        world = result.pose_world_landmarks[index] if result.pose_world_landmarks else []
        pose = {
            "index": index,
            "landmarks": [landmark_record(item) for item in landmarks],
            "world_landmarks": [landmark_record(item) for item in world],
            "derived": {
                "shoulder_midpoint": midpoint(landmarks[11], landmarks[12]),
                "hip_midpoint": midpoint(landmarks[23], landmarks[24]),
                "left_wrist": landmark_record(landmarks[15]),
                "right_wrist": landmark_record(landmarks[16]),
                "left_ankle": landmark_record(landmarks[27]),
                "right_ankle": landmark_record(landmarks[28]),
            },
        }
        poses.append(pose)
        if index == 0:
            draw_pose(frame, landmarks, output / "pose_overlay.png", False, args.min_visibility)
            draw_pose(frame, landmarks, output / "pose_skeleton.png", True, args.min_visibility)

    report = {
        "input": str(source),
        "source_time_seconds": args.time,
        "model": str(model),
        "mediapipe_version": mp.__version__,
        "image_size": {"width": frame.shape[1], "height": frame.shape[0]},
        "pose_count": len(poses),
        "poses": poses,
        "usage_note": (
            "Use pose_skeleton.png as pose/blocking reference only. "
            "Do not let it override identity, costume, materials, lighting, or world style."
        ),
    }
    (output / "pose.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "pose_json": str(output / "pose.json"),
                "overlay": str(output / "pose_overlay.png"),
                "skeleton": str(output / "pose_skeleton.png"),
                "pose_count": len(poses),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
