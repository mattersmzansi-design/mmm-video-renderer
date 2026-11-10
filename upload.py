#!/usr/bin/env python3
"""
Upload a rendered video to YouTube.

Reads the "youtube" block of a content file (title, description, tags, privacy,
synthetic-media label) and uploads out/<slug>-<w>x<h>.mp4 with it.

Credentials come from environment variables, which GitHub Actions fills from
repository secrets. Nothing secret is ever stored in this repo:
    YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN

Usage:
    python upload.py --content content.json
    python upload.py --content content-short.json --dry-run   # print, don't upload

Safety: privacy defaults to "private". A video only goes public if the content
file explicitly says "privacy": "public".
"""

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()


def load(content_path: Path):
    content = json.loads(content_path.read_text(encoding="utf-8"))
    yt = content.get("youtube")
    if not yt:
        print(f"{content_path.name} has no \"youtube\" block; skipping upload.")
        sys.exit(0)
    w, h = content.get("size", [1920, 1080])
    video = ROOT / "out" / f"{content.get('slug', 'video')}-{w}x{h}.mp4"
    if not video.exists():
        sys.exit(f"rendered video not found: {video}")
    return content, yt, video


def chapters(timed_path: Path) -> str:
    """0:00 Intro, then one chapter per rank, from the voice-timed content."""
    if not timed_path.exists():
        return ""
    c = json.loads(timed_path.read_text(encoding="utf-8"))
    t = c.get("timing", {}).get("lead_in", 900)
    lines = ["0:00 Intro"]
    for sc in c["scenes"]:
        if sc.get("type") == "rank":
            sec = int(t / 1000)
            name = sc.get("headline", "")
            lines.append(f"{sec // 60}:{sec % 60:02d} {sc['rank']}. {name}")
        elif sc.get("type") == "plain" and len(lines) > 1 and sc.get("eyebrow") == "The pattern":
            sec = int(t / 1000)
            lines.append(f"{sec // 60}:{sec % 60:02d} What they have in common")
        t += sc.get("duration", 5000)
    return "\n".join(lines) if len(lines) >= 3 else ""


def build_body(yt: dict, chapter_text: str = "") -> dict:
    privacy = yt.get("privacy", "private")
    if privacy not in ("private", "unlisted", "public"):
        sys.exit(f"privacy must be private, unlisted or public, not {privacy!r}")
    status = {
        "privacyStatus": privacy,
        "selfDeclaredMadeForKids": False,
        "containsSyntheticMedia": bool(yt.get("synthetic_media", True)),
    }
    if yt.get("publish_at"):                 # scheduled: must be private until then
        status["privacyStatus"] = "private"
        status["publishAt"] = yt["publish_at"]
    return {
        "snippet": {
            "title": yt["title"][:100],
            "description": yt.get("description", "").replace("{chapters}", chapter_text)[:5000],
            "tags": yt.get("tags", []),
            "categoryId": str(yt.get("category_id", "27")),   # 27 = Education
            "defaultLanguage": "en",
            "defaultAudioLanguage": "en",
        },
        "status": status,
    }


def youtube_client():
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    missing = [k for k in ("YT_CLIENT_ID", "YT_CLIENT_SECRET", "YT_REFRESH_TOKEN")
               if not os.environ.get(k)]
    if missing:
        sys.exit("missing secrets: " + ", ".join(missing))
    creds = Credentials(
        token=None,
        refresh_token=os.environ["YT_REFRESH_TOKEN"],
        client_id=os.environ["YT_CLIENT_ID"],
        client_secret=os.environ["YT_CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token",
        scopes=["https://www.googleapis.com/auth/youtube.upload",
                "https://www.googleapis.com/auth/youtube"],
    )
    return build("youtube", "v3", credentials=creds, cache_discovery=False)


def upload(yt_api, video: Path, body: dict) -> str:
    from googleapiclient.http import MediaFileUpload

    media = MediaFileUpload(str(video), mimetype="video/mp4",
                            chunksize=8 * 1024 * 1024, resumable=True)
    req = yt_api.videos().insert(part="snippet,status", body=body, media_body=media)
    resp = None
    while resp is None:
        status, resp = req.next_chunk()
        if status:
            print(f"  uploaded {int(status.progress() * 100)}%", flush=True)
    return resp["id"]


def set_thumbnail(yt_api, video_id: str, thumb: Path):
    from googleapiclient.http import MediaFileUpload
    try:
        yt_api.thumbnails().set(videoId=video_id,
                                media_body=MediaFileUpload(str(thumb))).execute()
        print(f"  thumbnail set: {thumb.name}")
        return True
    except Exception as e:   # custom thumbnails need a phone-verified channel
        print(f"  thumbnail not set ({e}). The video is uploaded; add it in YouTube Studio.")
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--content", default="content.json")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--thumbnail-only", metavar="VIDEO_ID",
                    help="don't upload; just set this video's thumbnail from out/thumb-<slug>.jpg")
    args = ap.parse_args()

    if args.thumbnail_only:
        content = json.loads((ROOT / args.content).read_text(encoding="utf-8"))
        thumb = ROOT / "out" / f"thumb-{content.get('slug', 'video')}.jpg"
        if not thumb.is_file():
            sys.exit(f"no thumbnail at {thumb}; run thumbnail.py first")
        if not set_thumbnail(youtube_client(), args.thumbnail_only, thumb):
            sys.exit(1)
        return

    content_path = (ROOT / args.content).resolve()
    content, yt, video = load(content_path)
    body = build_body(yt, chapters(ROOT / "build" / "content.timed.json"))

    print(f"video:   {video.name} ({video.stat().st_size / 1e6:.1f} MB)")
    print(f"title:   {body['snippet']['title']}")
    print(f"privacy: {body['status']['privacyStatus']}"
          + (f", publishes {body['status']['publishAt']}" if 'publishAt' in body['status'] else ""))
    print(f"AI label: {body['status']['containsSyntheticMedia']}")
    if args.dry_run:
        print("description:\n" + body["snippet"]["description"])
        print("dry run: nothing uploaded.")
        return

    api = youtube_client()
    vid = upload(api, video, body)
    print(f"uploaded: https://youtu.be/{vid}")

    thumb = yt.get("thumbnail")
    made = ROOT / "out" / f"thumb-{content.get('slug', 'video')}.jpg"
    if thumb and (ROOT / "assets" / thumb).exists():
        set_thumbnail(api, vid, ROOT / "assets" / thumb)
    elif made.is_file() and not content.get("size"):     # long videos only; Shorts use a frame
        set_thumbnail(api, vid, made)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(f"### Uploaded to YouTube ({body['status']['privacyStatus']})\n"
                    f"**{body['snippet']['title']}**  \nhttps://youtu.be/{vid}\n\n"
                    f"Review it in YouTube Studio, then publish.\n")


if __name__ == "__main__":
    main()
