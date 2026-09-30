#!/usr/bin/env python3
"""Check declared delivery contents. Mechanical checks never certify visual quality."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff"}
TEXT_SUFFIXES = {".txt", ".md"}
ALLOWED_KINDS = {"prompt", "image", "document", "audio", "video", "file"}
FORBIDDEN_DIRS = {"候选稿", "失败稿", "未采用", "临时文件", "返工历史"}
CAMERA = re.compile(r"全景|近景|特写|中景|远景|俯拍|俯视|过肩|镜头|跟拍|POV", re.I)


def valid_relative(value):
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and ".." not in path.parts and path.as_posix() == value and value != "."


def load_image_info(path):
    try:
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError("Image checks unavailable: install requirements-test.txt in an isolated venv") from exc
    with Image.open(path) as image:
        image.verify()
    with Image.open(path) as image:
        return image.size, image.format


def prompt_content(path):
    """A minimal sanity check, not proof of script fidelity or shot quality."""
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return False
    try:
        text = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError):
        return False
    # If fenced blocks exist, inspect those rather than surrounding instructions.
    blocks = re.findall(r"\x60{3}(?:text)?\s*\n(.*?)\n\x60{3}", text, re.S)
    candidates = blocks or [text]
    for candidate in candidates:
        paragraphs = [p.strip() for p in re.split(r"\n\s*\n", candidate) if p.strip()]
        if len(paragraphs) >= 2 and len(candidate.strip()) >= 30 and CAMERA.search(candidate):
            return True
    return False


def parse_manifest(manifest):
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        raise ValueError("manifest must have schema_version 1")
    entries = manifest.get("files")
    if not isinstance(entries, list) or not entries:
        raise ValueError("manifest files must be a nonempty list")
    by_path = {}
    for entry in entries:
        if not isinstance(entry, dict) or not valid_relative(entry.get("path")):
            raise ValueError("manifest contains an invalid relative path")
        name = entry["path"]
        if name in by_path:
            raise ValueError(f"duplicate manifest path: {name}")
        if entry.get("kind") not in ALLOWED_KINDS:
            raise ValueError(f"missing or invalid kind: {name}")
        by_path[name] = entry
    return by_path


def storyboard_problems(name, entry):
    """Check declared storyboard identity/filing, not the visual cut or image quality."""
    if entry.get("role") != "storyboard_reference":
        return []
    problems = []
    path = PurePosixPath(name)
    scene, shot = entry.get("scene"), entry.get("shot")
    valid_scene = (isinstance(scene, str) and bool(scene.strip()) and
                   not any(c in scene for c in '/\\\n\r') and scene not in {".", ".."})
    valid_shot = type(shot) is int and shot > 0
    if entry.get("kind") != "image" or path.suffix.lower() not in IMAGE_SUFFIXES:
        problems.append(f"storyboard must be an image: {name}")
    if not valid_scene or not valid_shot:
        problems.append(f"storyboard needs valid scene and positive integer shot: {name}")
    elif path.stem != f"{scene}，分镜{shot}":
        problems.append(f"storyboard filename must be scene，分镜N: {name}")
    if path.parent.name != "分镜参考":
        problems.append(f"storyboard must be inside scene/分镜参考: {name}")
    elif valid_scene:
        scene_folder = path.parent.parent.name
        if not (scene_folder == scene or scene_folder.startswith(scene + "_")):
            problems.append(f"storyboard scene folder mismatch: {name}")
    return problems


def audit_tree(root, *, formal_delivery=False, require_prompts=False, manifest=None,
               canonical_assets=False):
    root = Path(root)
    problems, warnings = [], []
    entries = {}
    if manifest is not None:
        try:
            entries = parse_manifest(manifest)
        except ValueError as exc:
            problems.append(str(exc))
    if formal_delivery and manifest is None:
        problems.append("formal delivery requires --manifest with the agreed expected contents")

    files = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            problems.append(f"symlink not allowed in delivery: {relative}")
            continue
        if path.is_dir():
            if next(path.iterdir(), None) is None:
                problems.append(f"empty directory: {relative}")
            continue
        files[relative] = path
        if path.name in {".DS_Store", "Thumbs.db"} or path.name.startswith("._") or "__MACOSX" in path.parts:
            problems.append(f"hidden metadata: {relative}")
        if path.stat().st_size == 0:
            problems.append(f"empty file: {relative}")
        # Only dedicated nonformal directories are rejected, never plot words inside filenames.
        if formal_delivery and any(part in FORBIDDEN_DIRS for part in Path(relative).parts[:-1]):
            problems.append(f"nonformal directory in delivery: {relative}")
    if not files:
        problems.append("delivery is empty")

    if canonical_assets:
        by_digest = {}
        for name, path in files.items():
            if path.stat().st_size == 0:
                continue
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            by_digest.setdefault(digest, []).append(name)
        for names in by_digest.values():
            if len(names) > 1:
                problems.append("duplicate canonical asset content: " + " | ".join(sorted(names)))

    if entries:
        for name in entries.keys() - files.keys():
            problems.append(f"missing expected file: {name}")
        for name in files.keys() - entries.keys():
            problems.append(f"unexpected file: {name}")

    prompt_paths = []
    for name, path in files.items():
        entry = entries.get(name, {})
        problems.extend(storyboard_problems(name, entry))
        if formal_delivery and entries:
            statuses = {"adopted"}
            if entry.get("role") == "storyboard_reference" and entry.get("kind") == "image":
                statuses.add("self_reviewed")
            if entry.get("status") not in statuses:
                problems.append(f"file is not explicitly adopted: {name}")
            digest = entry.get("sha256")
            if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                problems.append(f"missing valid source sha256: {name}")
        digest = entry.get("sha256")
        if digest and hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            problems.append(f"source hash mismatch: {name}")

        is_image = path.suffix.lower() in IMAGE_SUFFIXES
        if entry.get("kind") == "image" and not is_image:
            problems.append(f"unsupported image extension: {name}")
        if is_image:
            if entries and entry.get("kind") != "image":
                problems.append(f"image must be declared as image: {name}")
            spec = entry.get("image", {})
            if not isinstance(spec, dict):
                problems.append(f"invalid image specification: {name}")
                spec = {}
            if formal_delivery and (not isinstance(spec.get("width"), int) or
                                    not isinstance(spec.get("height"), int) or
                                    spec.get("width", 0) <= 0 or spec.get("height", 0) <= 0 or
                                    not isinstance(spec.get("format"), str)):
                problems.append(f"formal image needs expected width height format: {name}")
            try:
                (width, height), fmt = load_image_info(path)
                for key, actual in (("width", width), ("height", height), ("format", fmt)):
                    if key in spec and spec[key] != actual:
                        problems.append(f"image {key} expected {spec[key]} got {actual}: {name}")
                if not spec:
                    warnings.append(f"image has no target specification; observed {width}x{height} {fmt}: {name}")
            except (RuntimeError, OSError, ValueError, SyntaxError) as exc:
                problems.append(f"image inspection failed: {name}: {exc}")

        declared_prompt = entry.get("kind") == "prompt"
        if declared_prompt:
            if prompt_content(path):
                prompt_paths.append(name)
            else:
                problems.append(f"declared prompt lacks readable prompt content: {name}")
        elif not entries and prompt_content(path):
            prompt_paths.append(name)
    if require_prompts and not prompt_paths:
        problems.append("delivery is missing readable prompt content")

    if manifest is not None and isinstance(manifest, dict):
        required = manifest.get("required_scenes", [])
        scenes = manifest.get("scenes", {})
        if not isinstance(required, list) or any(not isinstance(s, str) or not s for s in required):
            problems.append("required_scenes must be a list of scene identifiers")
        elif not isinstance(scenes, dict):
            problems.append("scenes must map scene identifiers to expected file paths")
        else:
            for scene in required:
                paths = scenes.get(scene)
                if not isinstance(paths, list) or not paths:
                    problems.append(f"scene has no declared coverage: {scene}")
                    continue
                for name in paths:
                    if not isinstance(name, str) or name not in entries or name not in files:
                        problems.append(f"scene references missing or undeclared file: {scene}: {name}")
            if not required:
                warnings.append("no scene scope supplied; scene completeness is NOT checked")
    return sorted(set(problems)), sorted(set(warnings))


def safe_extract(archive, destination):
    destination = destination.resolve()
    with zipfile.ZipFile(archive) as bundle:
        members = bundle.infolist()
        if len(members) > 20000 or sum(m.file_size for m in members) > 20 * 1024**3:
            raise ValueError("archive exceeds inspection limit; inspect in approved batches")
        seen = set()
        for member in members:
            name = member.filename.rstrip("/")
            if not valid_relative(name) or name in seen:
                raise ValueError(f"unsafe or duplicate zip member: {member.filename}")
            seen.add(name)
            if stat.S_ISLNK(member.external_attr >> 16):
                raise ValueError(f"zip symlink not allowed: {name}")
            target = (destination / name).resolve()
            if destination not in target.parents:
                raise ValueError(f"unsafe zip member: {name}")
        bundle.extractall(destination)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path)
    parser.add_argument("--formal-delivery", action="store_true")
    parser.add_argument("--require-prompts", action="store_true")
    parser.add_argument("--canonical-assets", action="store_true",
                        help="Reject same-content files in a canonical master asset directory; do not use on per-scene copies")
    parser.add_argument("--manifest", type=Path, help="External JSON describing agreed expected files, hashes and sizes")
    args = parser.parse_args()
    target = args.target.expanduser().resolve()
    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8")) if args.manifest else None
        if target.is_dir():
            problems, warnings = audit_tree(target, formal_delivery=args.formal_delivery,
                                            require_prompts=args.require_prompts, manifest=manifest,
                                            canonical_assets=args.canonical_assets)
        elif target.is_file() and target.suffix.lower() == ".zip":
            with tempfile.TemporaryDirectory(prefix="seedance-delivery-") as temp:
                safe_extract(target, Path(temp))
                problems, warnings = audit_tree(Path(temp), formal_delivery=args.formal_delivery,
                                                require_prompts=args.require_prompts, manifest=manifest,
                                                canonical_assets=args.canonical_assets)
        else:
            raise ValueError("target must be an existing directory or zip")
    except (ValueError, OSError, zipfile.BadZipFile) as exc:
        print(f"CHECK UNAVAILABLE: {exc}")
        return 2
    print("DELIVERY CHECK FAILED" if problems else "MECHANICAL CHECK PASSED — visual and script review still required")
    for problem in problems:
        print(f"- ERROR: {problem}")
    for warning in warnings:
        print(f"- WARNING: {warning}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
