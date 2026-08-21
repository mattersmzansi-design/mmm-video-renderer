# MMM Video Renderer

Turns a JSON file into a branded 1920×1080 MP4 for YouTube.

The video is an animated HTML page. The renderer opens it in headless Chromium,
steps the animation forward one frame at a time, screenshots each frame, and
hands the frames to ffmpeg. Because it seeks the timeline rather than recording
in real time, the output is identical every run — no dropped frames, no timing
drift between your laptop and the CI runner.

```
content.json  ->  build/index.html  ->  frames  ->  out/*.mp4
```

## Files

| File | What it does |
|---|---|
| `content.json` | The script. Scenes, copy, ticker, end card. **This is the only file you edit day to day.** |
| `template.html` | The design. Layout, brand colours, animation timing. |
| `voice.py` | Generates the narration and recalculates scene timing from it. |
| `render.py` | Build, capture, encode. |
| `assets/` | Logo, headshot, photos. Anything here is available to `content.json` by filename. |
| `.github/workflows/render.yml` | Renders on GitHub and uploads the MP4. |

## Run it on GitHub (no local setup)

1. Create a new **empty** repo on GitHub — keep this separate from JSE Analyst so
   a broken render can never affect your Reddit posting.
2. Push these files to it.
3. Go to **Actions → Render video → Run workflow**.
4. When it finishes, download the MP4 from the **Artifacts** section at the
   bottom of the run page.

It also renders automatically whenever you push a change to `content.json`,
`template.html`, or `assets/`.

## Run it locally

```bash
pip install -r requirements.txt
python -m playwright install chromium
# ffmpeg must be on your PATH

python render.py
```

Output lands in `out/`.

### Preview without rendering

```bash
python render.py --preview
```

Builds `build/index.html`. Open it in Chrome to check the design — it plays
straight through. Much faster than a full render when you're adjusting copy.

## Editing the script

Each scene takes:

```json
{
  "eyebrow": "Small orange label above the headline",
  "headline": "Big text. <em>Wrap words in em</em> to make them orange. <br> breaks the line.",
  "body": "Optional supporting line underneath.",
  "media": "some-image.jpg",
  "duration": 4800
}
```

`media` is optional — with it the scene splits into text-left / image-right,
without it the text runs full width. `duration` is milliseconds. Drop the
`backdrop` key to lose the opening photo entirely.

Total runtime is just the sum of the scene durations plus the end card, so the
chart line along the bottom always finishes drawing exactly as the video ends.

## Adding new videos

Make `content-<topic>.json`, then:

```bash
python render.py --content content-jse-week.json
```

On GitHub, put the filename into the **content** box when you run the workflow.

## Voiceover

Narration drives the timing. You never set scene durations by hand — you write
the line, and the scene stays up for exactly as long as it takes to say it.

Give each scene a `voiceover` line:

```json
{
  "eyebrow": "The setup",
  "headline": "Bitcoin's technicals are <em>strong.</em>",
  "voiceover": "Bitcoin is showing strong technical patterns right now."
}
```

Then:

```bash
python voice.py
python render.py --content build/content.timed.json --audio build/voiceover.m4a
```

`voice.py` speaks each line, measures it, pads it with silence, and writes two
things: `build/voiceover.m4a` (the full track) and `build/content.timed.json`
(your content with every duration recalculated). The audio and the visuals line
up frame for frame because they come from the same measurement.

On GitHub this is automatic — the workflow runs both steps in order.

### Choosing a voice

```bash
python voice.py --list-voices
```

`en-ZA-LukeNeural` (male) and `en-ZA-LeahNeural` (female) are the South African
options. Set it in `content.json`:

```json
"voice": {
  "name": "en-ZA-LukeNeural",
  "rate": "+4%",
  "pitch": "+0Hz",
  "lead_pad": 400,
  "tail_pad": 950
}
```

`rate` speeds up or slows down delivery. `tail_pad` is the beat of silence after
each line — raise it if the cuts feel rushed, lower it if the video drags.

Edge-TTS is free and needs no account or API key. It is Microsoft's service, so
the render step needs network access, which GitHub Actions has.

### Writing narration that sounds right

Read it aloud before you commit it. Short sentences. Say "seventeen rand eighty
four" rather than "R17.84" — the synthesiser handles words better than symbols.
Numbers, acronyms, and currency are where these voices most often stumble.

### Silent version

Skip `voice.py` and run `render.py` on its own, or untick **voiceover** when you
run the workflow. Scenes then use whatever `duration` you set in the JSON.

## Wiring it to the Content Adapter

The Content Adapter already returns per-platform copy plus video suggestions.
Mapping that JSON onto the `scenes` array here is the last link — one small
transform script, and a generated post becomes a rendered video without you
touching either file.
