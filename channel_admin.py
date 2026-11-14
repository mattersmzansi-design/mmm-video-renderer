#!/usr/bin/env python3
"""
Small channel admin jobs, run from the "Channel admin" GitHub workflow.

    python channel_admin.py list                     # print every upload: id, privacy, title
    python channel_admin.py retitle titles.json      # {"VIDEO_ID": "New title", ...}

Retitling keeps each video's description, tags and category; only the title changes.
"""
import json
import sys
from pathlib import Path

from upload import youtube_client


def all_uploads(api):
    ch = api.channels().list(part="contentDetails", mine=True).execute()
    uploads = ch["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    out, token = [], None
    while True:
        r = api.playlistItems().list(part="contentDetails", playlistId=uploads, maxResults=50, pageToken=token).execute()
        ids = [i["contentDetails"]["videoId"] for i in r["items"]]
        if ids:
            v = api.videos().list(part="snippet,status,contentDetails", id=",".join(ids)).execute()
            out += v["items"]
        token = r.get("nextPageToken")
        if not token:
            return out


def main():
    api = youtube_client()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "list":
        for v in all_uploads(api):
            print(f"{v['id']}  {v['status']['privacyStatus']:<8} {v['contentDetails']['duration']:<9} {v['snippet']['title']}")
    elif cmd == "retitle":
        titles = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
        for vid, title in titles.items():
            if len(title) > 100:
                print(f"SKIP {vid}: title over 100 characters"); continue
            cur = api.videos().list(part="snippet", id=vid).execute()["items"]
            if not cur:
                print(f"SKIP {vid}: not found"); continue
            sn = cur[0]["snippet"]
            old = sn["title"]
            body = {"id": vid, "snippet": {"title": title, "description": sn.get("description", ""),
                                            "categoryId": sn["categoryId"], "tags": sn.get("tags", [])}}
            if sn.get("defaultLanguage"):
                body["snippet"]["defaultLanguage"] = sn["defaultLanguage"]
            api.videos().update(part="snippet", body=body).execute()
            print(f"OK {vid}\n   was: {old}\n   now: {title}")
    else:
        sys.exit("usage: channel_admin.py list | retitle titles.json")


if __name__ == "__main__":
    main()
