#!/usr/bin/env python3
"""
MMM video renderer.

Reads content.json + template.html, seeks the page animation frame by frame in
headless Chromium, and encodes the captured frames into an MP4 with ffmpeg.

Frames are captured by seeking the Web Animations timeline, not by recording in
real time, so output is identical on every machine regardless of how fast or slow
the render is.

Usage:
    python render.py
    python render.py --content content.json --fps 30 --out out/video.mp4
    python render.py --preview        # writes build/index.html only, no render
"""

import argparse
import base64
import json
import mimetypes
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
BUILD = ROOT / "build"
FRAMES = BUILD / "frames"

WIDTH, HEIGHT = 1920, 1080


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def font_face_css(fonts_dir: Path) -> str:
    """Embed any .ttf/.woff2 in fonts/ so the render never depends on system fonts."""
    if not fonts_dir.is_dir():
        return ""
    blocks = []
    for f in sorted(fonts_dir.iterdir()):
        if f.suffix.lower() not in (".ttf", ".otf", ".woff2", ".woff"):
            continue
        # Expect names like: Archivo-Bold.ttf  /  IBMPlexMono-Regular.ttf
        stem = f.stem
        family, _, style = stem.partition("-")
        family = {"IBMPlexMono": "IBM Plex Mono"}.get(family, family)
        weight = {
            "Thin": 100, "ExtraLight": 200, "Light": 300, "Regular": 400,
            "Medium": 500, "SemiBold": 600, "Bold": 700,
            "ExtraBold": 800, "Black": 900,
        }.get(style, 400)
        fmt = {"ttf": "truetype", "otf": "opentype",
               "woff2": "woff2", "woff": "woff"}[f.suffix.lower().lstrip(".")]
        blocks.append(
            f"@font-face{{font-family:'{family}';font-weight:{weight};"
            f"font-style:normal;font-display:block;"
            f"src:url('{data_uri(f)}') format('{fmt}');}}"
        )
    return "\n".join(blocks)


def build_html(content_path: Path) -> Path:
    content = json.loads(content_path.read_text(encoding="utf-8"))
    template = (ROOT / content.get("template", "template.html")).read_text(encoding="utf-8")

    assets_dir = ROOT / "assets"
    assets = {}
    if assets_dir.is_dir():
        for f in sorted(assets_dir.iterdir()):
            if f.is_file() and not f.name.startswith("."):
                assets[f.name] = data_uri(f)

    html = (template
            .replace("__CONTENT__", json.dumps(content))
            .replace("__ASSETS__", json.dumps(assets))
            .replace("__FONTS__", font_face_css(ROOT / "fonts")))

    BUILD.mkdir(parents=True, exist_ok=True)
    out = BUILD / "index.html"
    out.write_text(html, encoding="utf-8")
    return out


def capture(html_path: Path, fps: int) -> int:
    from playwright.sync_api import sync_playwright

    if FRAMES.exists():
        shutil.rmtree(FRAMES)
    FRAMES.mkdir(parents=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--force-color-profile=srgb",
                                          "--disable-lcd-text"])
        page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT},
                                device_scale_factor=1)
        page.goto(html_path.as_uri())
        page.wait_for_function("window.READY === true")
        page.wait_for_timeout(400)          # let fonts and images settle

        total_ms = page.evaluate("window.TOTAL_MS")
        n = int(round(total_ms / 1000 * fps))
        print(f"  duration {total_ms/1000:.1f}s -> {n} frames at {fps}fps")

        for i in range(n):
            page.evaluate("ms => window.seek(ms)", i * 1000 / fps)
            page.screenshot(path=str(FRAMES / f"f{i:05d}.jpg"), type="jpeg", quality=92)
            if i % 60 == 0:
                print(f"  frame {i}/{n}", flush=True)

        browser.close()
    return n


def encode(out_path: Path, fps: int, audio: Path | None):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["ffmpeg", "-y",
           "-framerate", str(fps),
           "-i", str(FRAMES / "f%05d.jpg")]
    if audio and audio.exists():
        cmd += ["-i", str(audio), "-c:a", "aac", "-b:a", "192k", "-shortest"]
    cmd += ["-c:v", "libx264",
            "-preset", "slow",
            "-crf", "18",
            "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            str(out_path)]
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--content", default="content.json")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--out", default=None)
    ap.add_argument("--audio", default=None, help="optional voiceover/music track")
    ap.add_argument("--preview", action="store_true",
                    help="build build/index.html and stop (open it in a browser)")
    args = ap.parse_args()

    content_path = (ROOT / args.content).resolve()
    if not content_path.exists():
        sys.exit(f"content file not found: {content_path}")

    print("building html...")
    html = build_html(content_path)
    print(f"  {html}")

    if args.preview:
        print("preview built. open it in your browser.")
        return

    slug = json.loads(content_path.read_text(encoding="utf-8")).get("slug", "video")
    out = Path(args.out) if args.out else ROOT / "out" / f"{slug}-1920x1080.mp4"

    print("capturing frames...")
    capture(html, args.fps)

    print("encoding...")
    encode(out, args.fps, Path(args.audio) if args.audio else None)
    print(f"done: {out}")


if __name__ == "__main__":
    main()