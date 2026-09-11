#!/usr/bin/env python3
"""Inspect image/video color metadata and validate an optional OCIO configuration."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".exr", ".dpx", ".webp"}
VIDEO_SUFFIXES = {".mp4", ".mov", ".mkv", ".mxf", ".avi", ".webm"}


def find_ffprobe() -> str | None:
    found = shutil.which("ffprobe")
    if found:
        return found
    root = Path.home() / "AppData" / "Local" / "Microsoft" / "WinGet" / "Packages"
    matches = list(root.glob("Gyan.FFmpeg_*/*/bin/ffprobe.exe"))
    return str(max(matches, key=lambda item: item.stat().st_mtime)) if matches else None


def severity(report: dict[str, Any], level: str, message: str) -> None:
    report["flags"].append({"severity": level, "message": message})


def inspect_video(path: Path) -> dict[str, Any]:
    report: dict[str, Any] = {"type": "video", "path": str(path), "flags": []}
    ffprobe = find_ffprobe()
    report["ffprobe"] = ffprobe
    if not ffprobe:
        severity(report, "error", "ffprobe is unavailable; video color metadata was not inspected.")
        return report
    command = [
        ffprobe,
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=codec_name,pix_fmt,width,height,color_range,color_space,color_transfer,color_primaries",
        "-of",
        "json",
        str(path),
    ]
    proc = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode:
        severity(report, "error", proc.stderr.strip() or "ffprobe failed.")
        return report
    data = json.loads(proc.stdout)
    stream = (data.get("streams") or [{}])[0]
    report["metadata"] = stream
    return report


def serializable(value: Any) -> Any:
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, bytes):
        return f"<{len(value)} bytes>"
    if isinstance(value, (list, tuple)):
        return [serializable(item) for item in value]
    return str(value)


def inspect_image(path: Path) -> dict[str, Any]:
    report: dict[str, Any] = {"type": "image", "path": str(path), "flags": []}
    metadata: dict[str, Any] = {}
    try:
        import OpenImageIO as oiio

        image = oiio.ImageInput.open(str(path))
        if not image:
            raise RuntimeError("OpenImageIO could not open the image.")
        spec = image.spec()
        metadata.update(
            {
                "width": spec.width,
                "height": spec.height,
                "channels": spec.nchannels,
                "channel_names": list(spec.channelnames),
                "data_format": str(spec.format),
            }
        )
        for item in spec.extra_attribs:
            metadata[item.name] = serializable(item.value)
        image.close()
        report["openimageio_version"] = oiio.VERSION_STRING
    except Exception as exc:
        report["openimageio_error"] = str(exc)
        try:
            from PIL import Image

            with Image.open(path) as image:
                metadata.update(
                    {
                        "width": image.width,
                        "height": image.height,
                        "mode": image.mode,
                        "format": image.format,
                        "icc_profile": f"<{len(image.info['icc_profile'])} bytes>"
                        if image.info.get("icc_profile")
                        else None,
                        "srgb": image.info.get("srgb"),
                        "gamma": image.info.get("gamma"),
                    }
                )
        except Exception as fallback:
            severity(report, "error", f"Image inspection failed: {fallback}")
    report["metadata"] = metadata
    return report


def metadata_value(metadata: dict[str, Any], *names: str) -> Any:
    lowered = {key.lower(): value for key, value in metadata.items()}
    for name in names:
        if name.lower() in lowered:
            return lowered[name.lower()]
    return None


def apply_expectations(report: dict[str, Any], expected: str) -> None:
    metadata = report.get("metadata") or {}
    if report["type"] == "video":
        required = ("color_space", "color_transfer", "color_primaries")
        missing = [key for key in required if not metadata.get(key)]
        if missing:
            severity(report, "error" if expected != "auto" else "warning", f"Missing video color tags: {', '.join(missing)}.")
        if expected == "sdr-rec709":
            checks = {
                "color_space": {"bt709"},
                "color_primaries": {"bt709"},
                "color_transfer": {"bt709", "iec61966-2-1"},
            }
            for key, allowed in checks.items():
                value = metadata.get(key)
                if value and value not in allowed:
                    severity(report, "error", f"{key}={value}; expected one of {sorted(allowed)}.")
        elif expected == "hdr-pq-rec2020":
            checks = {
                "color_space": {"bt2020nc", "bt2020c"},
                "color_primaries": {"bt2020"},
                "color_transfer": {"smpte2084"},
            }
            for key, allowed in checks.items():
                value = metadata.get(key)
                if value and value not in allowed:
                    severity(report, "error", f"{key}={value}; expected one of {sorted(allowed)}.")
    else:
        color_space = metadata_value(metadata, "oiio:ColorSpace", "ColorSpace", "colorspace")
        icc = metadata_value(metadata, "ICCProfile", "icc_profile", "ICCProfile:Description")
        srgb = metadata_value(metadata, "png:sRGB", "srgb")
        report["interpreted_color_metadata"] = {
            "color_space": serializable(color_space),
            "icc_profile": serializable(icc),
            "srgb_marker": serializable(srgb),
        }
        suffix = Path(report["path"]).suffix.lower()
        if expected == "aces-exr":
            if suffix != ".exr":
                severity(report, "error", "ACES EXR delivery expected, but the file is not EXR.")
            if not color_space:
                severity(report, "error", "EXR has no explicit oiio:ColorSpace/ColorSpace metadata.")
        elif expected == "sdr-rec709" and not (color_space or icc or srgb is not None):
            severity(report, "error", "SDR image has no ICC profile, sRGB marker, or explicit color-space metadata.")
        elif expected == "auto" and not (color_space or icc or srgb is not None):
            severity(report, "warning", "No explicit image color-space metadata was found.")


def validate_ocio(value: str) -> dict[str, Any]:
    result: dict[str, Any] = {"path": value, "valid": False}
    try:
        import PyOpenColorIO as ocio

        config = (
            ocio.Config.CreateFromBuiltinConfig(value)
            if value.startswith("ocio://")
            else ocio.Config.CreateFromFile(str(Path(value).expanduser().resolve()))
        )
        config.validate()
        result.update(
            {
                "valid": True,
                "version": ocio.__version__,
                "name": config.getName(),
                "description": config.getDescription(),
                "color_space_count": len(config.getColorSpaceNames()),
                "display_count": len(config.getDisplays()),
            }
        )
    except Exception as exc:
        result["error"] = str(exc)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument(
        "--expected",
        choices=["auto", "sdr-rec709", "hdr-pq-rec2020", "aces-exr"],
        default="auto",
    )
    parser.add_argument("--ocio-config")
    parser.add_argument("--json")
    args = parser.parse_args()
    path = Path(args.input).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"Input not found: {path}")
    suffix = path.suffix.lower()
    if suffix in VIDEO_SUFFIXES:
        report = inspect_video(path)
    elif suffix in IMAGE_SUFFIXES:
        report = inspect_image(path)
    else:
        raise SystemExit(f"Unsupported file type: {suffix}")
    report["expected"] = args.expected
    apply_expectations(report, args.expected)
    if args.ocio_config:
        report["ocio"] = validate_ocio(args.ocio_config)
        if not report["ocio"]["valid"]:
            severity(report, "error", "OCIO configuration validation failed.")
    levels = {item["severity"] for item in report["flags"]}
    report["status"] = "fail" if "error" in levels else "warn" if "warning" in levels else "pass"
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json:
        output = Path(args.json).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
    print(text)
    sys.exit(2 if report["status"] == "fail" else 0)


if __name__ == "__main__":
    main()
