#!/usr/bin/env python3
"""Render A/B/C thumbnail variants for YouTube's Test & compare.
Reads thumb-variants.json: {"<file-name-stem>": [ {thumbnail block}, ... ]}; writes thumbs/<stem>-B.jpg, -C.jpg ..."""
import json
from pathlib import Path
from thumbnail import render_thumb, ROOT

spec = json.loads((ROOT / "thumb-variants.json").read_text(encoding="utf-8"))
logo = ROOT / "assets" / "logo.jpg"
for stem, variants in spec.items():
    for letter, t in zip("BCDE", variants):
        out = ROOT / "thumbs" / f"{stem}-{letter}.jpg"
        render_thumb(t, logo, out)
        print("made", out.relative_to(ROOT))
