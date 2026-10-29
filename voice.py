#!/usr/bin/env python3
"""
Voiceover generator.

Speaks each scene's `voiceover` line with Edge-TTS, measures how long each clip
actually is, and rebuilds the timing so every scene stays on screen for exactly
as long as its narration takes. Writes an audio track padded with silence so the
audio and the visuals line up frame for frame.

Outputs:
    build/voiceover.m4a          the full narration track
    build/content.timed.json     content.json with durations replaced

Usage:
    python voice.py
    python voice.py --content content.json
    python voice.py --list-voices
"""

import argparse
import asyncio
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
BUILD = ROOT / "build"
VO = BUILD / "vo"

SR = 24000  # sample rate used throughout


def ffprobe_ms(path: Path) -> int:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True, check=True).stdout.strip()
    return int(round(float(out) * 1000))


def to_wav(src: Path, dst: Path):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(src),
                    "-ar", str(SR), "-ac", "1", str(dst)], check=True)


def silence(ms: int, dst: Path):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi",
                    "-i", f"anullsrc=r={SR}:cl=mono",
                    "-t", f"{ms/1000:.4f}", str(dst)], check=True)


async def speak(text: str, voice: str, rate: str, pitch: str, dst: Path):
    import edge_tts
    kwargs = {}
    if rate:
        kwargs["rate"] = rate
    if pitch:
        kwargs["pitch"] = pitch
    await edge_tts.Communicate(text, voice, **kwargs).save(str(dst))


async def list_voices():
    import edge_tts
    voices = await edge_tts.list_voices()
    za = [v for v in voices if v["Locale"].startswith("en-ZA")]
    print("South African English voices:")
    for v in za:
        print(f"  {v['ShortName']:<24} {v['Gender']}")
    print("\nOther useful English voices:")
    for v in voices:
        if v["Locale"] in ("en-GB", "en-US") and "Neural" in v["ShortName"]:
            print(f"  {v['ShortName']:<24} {v['Gender']}  {v['Locale']}")


def strip_markup(text: str) -> str:
    """content.json headlines carry <em> and <br> for the visuals; the narration
    lines are plain, but strip anything that slips through."""
    import re
    return re.sub(r"<[^>]+>", " ", text).replace("  ", " ").strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--content", default="content.json")
    ap.add_argument("--list-voices", action="store_true")
    args = ap.parse_args()

    if args.list_voices:
        asyncio.run(list_voices())
        return

    content_path = (ROOT / args.content).resolve()
    content = json.loads(content_path.read_text(encoding="utf-8"))

    vcfg = content.get("voice", {})
    voice = vcfg.get("name", "en-ZA-LukeNeural")
    rate = vcfg.get("rate", "+0%")
    pitch = vcfg.get("pitch", "+0Hz")
    lead_pad = vcfg.get("lead_pad", 400)    # silence before each line
    tail_pad = vcfg.get("tail_pad", 900)    # breathing room after
    lead_in = content.get("timing", {}).get("lead_in", 900)

    if VO.exists():
        shutil.rmtree(VO)
    VO.mkdir(parents=True)

    # every narrated block, in order: scenes then end card
    blocks = []
    for i, sc in enumerate(content["scenes"]):
        blocks.append(("scene", i, sc.get("voiceover", "")))
    blocks.append(("endcard", 0, content["endcard"].get("voiceover", "")))

    segments = []          # wav files, in playback order
    durations = {}         # (kind, index) -> total scene duration in ms

    silence(lead_in, VO / "lead.wav")
    segments.append(VO / "lead.wav")

    print(f"voice: {voice}  rate {rate}")
    for kind, idx, text in blocks:
        tag = f"{kind}{idx}"
        text = strip_markup(text)

        pre = VO / f"{tag}-pre.wav"
        silence(lead_pad, pre)
        segments.append(pre)

        if text:
            mp3 = VO / f"{tag}.mp3"
            # a scene may override the voice (used for voice comparison tests)
            sc = content["scenes"][idx] if kind == "scene" else content["endcard"]
            sv = sc.get("voice", {})
            s_voice = sv.get("name", voice)
            s_rate = sv.get("rate", rate)
            s_pitch = sv.get("pitch", pitch)
            try:
                asyncio.run(speak(text, s_voice, s_rate, s_pitch, mp3))
                ok = mp3.exists() and mp3.stat().st_size > 0
            except Exception as e:
                print(f"  {tag}: voice {s_voice} failed ({e})")
                ok = False
            if not ok and s_voice != voice:
                print(f"  {tag}: falling back to {voice}")
                sc["body"] = f"{s_voice} is not available. This line uses {voice} instead."
                asyncio.run(speak(text, voice, rate, pitch, mp3))
                ok = mp3.exists() and mp3.stat().st_size > 0
            if not ok:
                sys.exit(f"TTS produced no audio for {tag}. Check network/voice name.")
            wav = VO / f"{tag}.wav"
            to_wav(mp3, wav)
            spoken = ffprobe_ms(wav)
            segments.append(wav)
            print(f"  {tag:<10} {spoken/1000:5.2f}s  {text[:52]}")
        else:
            # no narration for this block: keep whatever duration was authored
            spoken = 0
            print(f"  {tag:<10}  (silent)")

        if spoken:
            total = lead_pad + spoken + tail_pad
        else:
            authored = (content["scenes"][idx].get("duration", 4500)
                        if kind == "scene" else
                        content["endcard"].get("duration", 4800))
            total = authored

        post = VO / f"{tag}-post.wav"
        silence(max(total - lead_pad - spoken, 0), post)
        segments.append(post)

        durations[(kind, idx)] = total

    # concatenate and encode
    listfile = VO / "list.txt"
    listfile.write_text("".join(f"file '{p.name}'\n" for p in segments),
                        encoding="utf-8")
    track = BUILD / "voiceover.m4a"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", str(listfile), "-c:a", "aac", "-b:a", "192k",
                    str(track)], cwd=VO, check=True)

    # write timed content
    for i, sc in enumerate(content["scenes"]):
        sc["duration"] = durations[("scene", i)]
    content["endcard"]["duration"] = durations[("endcard", 0)]

    timed = BUILD / "content.timed.json"
    timed.write_text(json.dumps(content, indent=2, ensure_ascii=False),
                     encoding="utf-8")

    total_ms = lead_in + sum(durations.values())
    print(f"\ntrack:   {track}  ({ffprobe_ms(track)/1000:.1f}s)")
    print(f"timing:  {timed}  (video will be {total_ms/1000:.1f}s)")
    print("\nnow run:")
    print("  python render.py --content build/content.timed.json "
          "--audio build/voiceover.m4a")


if __name__ == "__main__":
    main()
