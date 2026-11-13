#!/usr/bin/env python3
"""
Voiceover generator.

Speaks each scene's `voiceover` line with Kokoro (local, Apache-2.0) or Edge-TTS, measures how long each clip
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


# ---------- Kokoro-82M (Apache-2.0), runs locally via kokoro-onnx ----------
KOKORO_DIR = ROOT / "models" / "kokoro"
KOKORO_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
_KOKORO = None

def kokoro():
    global _KOKORO
    if _KOKORO is None:
        import urllib.request
        from kokoro_onnx import Kokoro
        KOKORO_DIR.mkdir(parents=True, exist_ok=True)
        for f in ("kokoro-v1.0.onnx", "voices-v1.0.bin"):
            if not (KOKORO_DIR / f).is_file():
                print(f"  downloading {f} ...")
                urllib.request.urlretrieve(KOKORO_URL + f, KOKORO_DIR / f)
        _KOKORO = Kokoro(str(KOKORO_DIR / "kokoro-v1.0.onnx"), str(KOKORO_DIR / "voices-v1.0.bin"))
    return _KOKORO

def speak_kokoro(text: str, voice: str, speed: float, lang: str, dst: Path):
    import soundfile as sf
    samples, sr = kokoro().create(text, voice=voice, speed=speed, lang=lang)
    sf.write(str(dst), samples, sr)

def speak_any(text: str, cfg: dict, dst_base: Path) -> Path:
    """cfg: {"engine": "kokoro"|"edge", "name", "speed"/"rate", "lang", "pitch"}. Returns the audio file written."""
    if cfg.get("engine") == "kokoro":
        out = dst_base.with_suffix(".k.wav")
        speak_kokoro(text, cfg.get("name", "bf_emma"), float(cfg.get("speed", 1.0)),
                     cfg.get("lang", "en-gb"), out)
    else:
        out = dst_base.with_suffix(".mp3")
        asyncio.run(speak(text, cfg.get("name", "en-US-BrianMultilingualNeural"),
                          cfg.get("rate", "+0%"), cfg.get("pitch", "+0Hz"), out))
    if not (out.exists() and out.stat().st_size > 0):
        raise RuntimeError("no audio written")
    return out

# when the main voice fails, the other engine takes over so a render never dies on TTS
BACKUPS = {
    "kokoro": {"engine": "edge", "name": "en-US-BrianMultilingualNeural", "rate": "+4%"},
    "edge": {"engine": "kokoro", "name": "bf_emma", "speed": 1.05, "lang": "en-gb"},
}


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
    voice = vcfg.get("name", "bf_emma" if vcfg.get("engine") == "kokoro" else "en-ZA-LukeNeural")
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

    print(f"voice: {vcfg.get('engine', 'edge')} / {voice}  "
          + (f"speed {vcfg.get('speed', 1.0)}" if vcfg.get('engine') == 'kokoro' else f"rate {rate}"))
    for kind, idx, text in blocks:
        tag = f"{kind}{idx}"
        text = strip_markup(text)

        pre = VO / f"{tag}-pre.wav"
        silence(lead_pad, pre)
        segments.append(pre)

        if text:
            sc = content["scenes"][idx] if kind == "scene" else content["endcard"]
            cfg = dict(vcfg); cfg.update(sc.get("voice", {}))   # a scene may override the voice
            cfg.setdefault("engine", "edge")
            try:
                mp3 = speak_any(text, cfg, VO / tag)
            except Exception as e:
                backup = vcfg.get("backup") or BACKUPS[cfg["engine"]]
                print(f"  {tag}: {cfg['engine']} voice {cfg.get('name')} failed ({e}); using backup {backup.get('name')}")
                try:
                    mp3 = speak_any(text, backup, VO / f"{tag}-b")
                except Exception as e2:
                    sys.exit(f"TTS produced no audio for {tag}: {e2}")
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
