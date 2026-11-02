#!/usr/bin/env python3
"""
Prepare b-roll footage for every "broll" scene in a content file.

For each scene with "type": "broll", the "broll" field says where the clip
comes from:

    "broll": "vault.mp4"                 your own clip in assets/broll/
    "broll": "bank vault door"           a Pexels search
    "broll": {"query": "bank vault", "pick": 2}   the 2nd Pexels result
    "broll": {"file": "vault.mp4", "start": 3}    your clip, from 3 s in

Your own file always wins when it exists. Each clip is trimmed, cropped to
fill the video frame, and saved as build/broll/s<index>.webm, which the
template plays and loops under the scene. Every clip used is recorded in
build/broll-sources.json (link, author, licence) as proof of licence.

Pexels search needs the PEXELS_API_KEY environment variable (a GitHub
secret). Without it, only your own clips are used; other b-roll scenes show
the navy background instead of footage.

Content rule for this channel: search for objects, places and screens, not
people. Pexels does not allow identifiable people to be shown in a criminal
or negative light, and these videos are about fraud and collapse.
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
BUILD = ROOT / "build"
OUT = BUILD / "broll"
OWN = ROOT / "assets" / "broll"
MAX_CLIP = 12.0          # seconds kept per clip; the template loops it


def pexels_search(query: str, orientation: str, key: str):
    url = "https://api.pexels.com/videos/search?" + urllib.parse.urlencode(
        {"query": query, "orientation": orientation, "size": "medium", "per_page": 15})
    req = urllib.request.Request(url, headers={"Authorization": key,
                                               "User-Agent": "mmm-video-renderer"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r).get("videos", [])


def best_file(video: dict, w: int, h: int):
    """The smallest MP4 that is still at least as big as the frame (or the biggest)."""
    files = [f for f in video.get("video_files", [])
             if f.get("file_type") == "video/mp4" and f.get("width") and f.get("height")]
    if not files:
        return None
    big = [f for f in files if f["width"] >= w * 0.9 and f["height"] >= h * 0.9]
    pool = big or files
    return min(pool, key=lambda f: f["width"] * f["height"]) if big else max(pool, key=lambda f: f["width"] * f["height"])


def download(url: str, dest: Path):
    req = urllib.request.Request(url, headers={"User-Agent": "mmm-video-renderer"})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
        while chunk := r.read(1 << 20):
            f.write(chunk)


def to_webm(src: Path, dest: Path, w: int, h: int, start: float, length: float):
    tmp = dest.with_suffix(".part.webm")
    cmd = ["ffmpeg", "-y", "-v", "error", "-ss", f"{start:.2f}", "-i", str(src),
           "-t", f"{length:.2f}", "-an",
           "-vf", f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps=30,format=yuv420p",
           "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "33", "-deadline", "realtime",
           "-cpu-used", "8", "-row-mt", "1", "-g", "15", str(tmp)]
    subprocess.run(cmd, check=True)
    tmp.replace(dest)


def probe_seconds(path: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", str(path)],
                         capture_output=True, text=True).stdout.strip()
    try:
        return float(out)
    except ValueError:
        return 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--content", default="content.json")
    args = ap.parse_args()

    content = json.loads((ROOT / args.content).read_text(encoding="utf-8"))
    w, h = content.get("size", [1920, 1080])
    orientation = "portrait" if h > w else "landscape"
    key = os.environ.get("PEXELS_API_KEY", "")
    OUT.mkdir(parents=True, exist_ok=True)
    (BUILD / "dl").mkdir(parents=True, exist_ok=True)

    sources, used_ids = [], set()
    scenes = [(i, s) for i, s in enumerate(content["scenes"]) if s.get("type") == "broll"]
    if not scenes:
        print("no b-roll scenes")
        return

    for i, sc in scenes:
        spec = sc.get("broll", "")
        if isinstance(spec, str):
            spec = {"file": spec} if (OWN / spec).is_file() else {"query": spec}
        start = float(spec.get("start", 0))
        dest = OUT / f"s{i}.webm"

        own = OWN / spec["file"] if spec.get("file") else None
        if own and own.is_file():
            length = min(MAX_CLIP, max(probe_seconds(own) - start, 1.0))
            to_webm(own, dest, w, h, start, length)
            sources.append({"scene": i, "source": "own", "file": f"assets/broll/{own.name}"})
            print(f"  scene {i:>2}: your clip {own.name}")
            continue
        if spec.get("file"):
            print(f"  scene {i:>2}: assets/broll/{spec['file']} not found", file=sys.stderr)

        query = spec.get("query") or sc.get("headline", "")
        if not key:
            print(f"  scene {i:>2}: no PEXELS_API_KEY, skipping search for '{query}' (navy background)")
            continue
        try:
            results = [v for v in pexels_search(query, orientation, key)
                       if v.get("duration", 0) >= 4 and v["id"] not in used_ids]
        except Exception as e:
            print(f"  scene {i:>2}: Pexels search failed ({e}); navy background", file=sys.stderr)
            continue
        pick = max(1, int(spec.get("pick", 1)))
        if len(results) < pick:
            print(f"  scene {i:>2}: no Pexels result for '{query}'; navy background", file=sys.stderr)
            continue
        video = results[pick - 1]
        f = best_file(video, w, h)
        if not f:
            print(f"  scene {i:>2}: no usable file for '{query}'", file=sys.stderr)
            continue
        raw = BUILD / "dl" / f"pexels-{video['id']}.mp4"
        download(f["link"], raw)
        length = min(MAX_CLIP, max(video.get("duration", MAX_CLIP) - start, 1.0))
        to_webm(raw, dest, w, h, start, length)
        used_ids.add(video["id"])
        sources.append({"scene": i, "source": "pexels", "query": query,
                        "url": video.get("url"), "author": video.get("user", {}).get("name"),
                        "author_url": video.get("user", {}).get("url"),
                        "licence": "Pexels License (https://www.pexels.com/license/)"})
        print(f"  scene {i:>2}: Pexels '{query}' -> {video.get('url')}")

    (BUILD / "broll-sources.json").write_text(json.dumps(sources, indent=2), encoding="utf-8")
    print(f"b-roll ready: {len(sources)} of {len(scenes)} scenes have footage")


if __name__ == "__main__":
    main()
