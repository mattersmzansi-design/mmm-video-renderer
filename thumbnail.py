#!/usr/bin/env python3
"""
Render a 1280x720 YouTube thumbnail from the "thumbnail" block of a content file.

    "thumbnail": {
      "kicker": "Top 10",                      small orange label (optional)
      "big":    "1,448",                       huge condensed number or word
      "line":   "Years old and <em>still open</em>",   2-5 words, <em> = orange
      "big_color": "orange" | "paper",
      "photo":  "japanese temple",             Pexels photo search (needs PEXELS_API_KEY)
      "image":  "Enron.jpg",                   or one of your files in assets/
      "frame":  3,                             or a frame from b-roll scene 3 (after broll.py)
      "focus":  "right center"                 which part of the photo to keep
    }

Writes out/thumb-<slug>.jpg. upload.py sets it as the video's thumbnail.
Background order: image, then frame, then photo; if none works, plain navy.
"""
import argparse
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from render import data_uri, font_face_css

ROOT = Path(__file__).parent.resolve()
BUILD = ROOT / "build"
OUT = ROOT / "out"


def pexels_photo(query: str, key: str, dest: Path) -> bool:
    url = "https://api.pexels.com/v1/search?" + urllib.parse.urlencode(
        {"query": query, "orientation": "landscape", "per_page": 5})
    req = urllib.request.Request(url, headers={"Authorization": key, "User-Agent": "mmm-video-renderer"})
    with urllib.request.urlopen(req, timeout=30) as r:
        photos = json.load(r).get("photos", [])
    if not photos:
        return False
    p = photos[0]
    src = p["src"].get("large2x") or p["src"]["original"]
    req = urllib.request.Request(src, headers={"User-Agent": "mmm-video-renderer"})
    with urllib.request.urlopen(req, timeout=60) as r:
        dest.write_bytes(r.read())
    print(f"  photo: Pexels '{query}' -> {p.get('url')} by {p.get('photographer')}")
    return True


def background(t: dict) -> Path | None:
    BUILD.mkdir(parents=True, exist_ok=True)
    if t.get("image") and (ROOT / "assets" / t["image"]).is_file():
        return ROOT / "assets" / t["image"]
    if t.get("frame") is not None:
        clip = BUILD / "broll" / f"s{t['frame']}.webm"
        if clip.is_file():
            dest = BUILD / "thumb-bg.jpg"
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "1.5", "-i", str(clip),
                            "-frames:v", "1", "-q:v", "2", str(dest)], check=False)
            if dest.is_file():
                return dest
    if t.get("photo"):
        key = os.environ.get("PEXELS_API_KEY", "")
        if key:
            dest = BUILD / "thumb-photo.jpg"
            try:
                if pexels_photo(t["photo"], key, dest):
                    return dest
            except Exception as e:
                print(f"  Pexels photo failed ({e}); navy background", file=sys.stderr)
        else:
            print("  no PEXELS_API_KEY; navy background")
    return None


def render_thumb(t: dict, logo: Path, out: Path):
    bg = background(t)
    html = ((ROOT / "template-thumb.html").read_text(encoding="utf-8")
            .replace("__FONTS__", font_face_css(ROOT / "fonts"))
            .replace("__THUMB__", json.dumps(t))
            .replace("__BG__", json.dumps(data_uri(bg) if bg else ""))
            .replace("__LOGO__", json.dumps(data_uri(logo) if logo.is_file() else "")))
    page_path = BUILD / "thumb.html"
    page_path.write_text(html, encoding="utf-8")
    from playwright.sync_api import sync_playwright
    out.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1280, "height": 720})
        pg.goto(page_path.as_uri())
        pg.wait_for_function("window.READY === true", timeout=20000)
        pg.screenshot(path=str(out), type="jpeg", quality=90)
        b.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--content", default="content.json")
    args = ap.parse_args()
    content = json.loads((ROOT / args.content).read_text(encoding="utf-8"))
    t = content.get("thumbnail")
    if not t:
        print("no thumbnail block; skipping")
        return
    logo = ROOT / "assets" / content.get("brand", {}).get("logo", "logo.jpg")
    out = OUT / f"thumb-{content.get('slug', 'video')}.jpg"
    render_thumb(t, logo, out)
    print(f"thumbnail: {out.relative_to(ROOT)} ({out.stat().st_size / 1e3:.0f} KB)")


if __name__ == "__main__":
    main()
