"""Short: How the rand reaches your pocket (Nov 2026). Metro-map explainer, bf_emma narration."""
import json

def est(vo):
    return int(len(vo.split()) / 150 * 60000) + 1300

EMMA = {"engine": "kokoro", "name": "bf_emma", "speed": 1.05, "lang": "en-gb", "lead_pad": 300, "tail_pad": 600}
O, P, G, R = "#EF4C00", "#9B6BE0", "#2FB574", "#E0344B"
metro = {"view": [1000, 840], "hub": {"x": 480, "y": 50, "label": "The rand"},
 "lines": [
  {"id": "fuel", "color": O, "d": "M480,50 L240,230",
   "stations": [{"x": 240, "y": 230, "label": "Fuel", "sub": "+R85 a barrel", "anchor": "end"}]},
  {"id": "imports", "color": P, "d": "M480,50 L740,230",
   "stations": [{"x": 740, "y": 230, "label": "Imports", "sub": "+R475 a phone", "anchor": "start"}]},
  {"id": "food", "color": G, "d": "M480,50 L480,450",
   "stations": [{"x": 480, "y": 250, "label": "Transport", "frac": 0.5},
                {"x": 480, "y": 450, "label": "Food prices"}]},
  {"id": "in-o", "color": O, "d": "M240,230 L240,560 L320,640 L480,640"},
  {"id": "in-p", "color": P, "d": "M740,230 L740,560 L660,640 L480,640"},
  {"id": "in-g", "color": G, "d": "M480,450 L480,640",
   "stations": [{"x": 480, "y": 640, "label": "Inflation", "sub": "5.2% (Oct)", "big": True, "dx": 40, "dy": -100}]},
  {"id": "bank", "color": R, "d": "M480,640 L480,770",
   "stations": [{"x": 480, "y": 770, "label": "Reserve Bank", "sub": "repo rate 7.25%", "dy": 4}]},
 ]}
ALL = ["fuel", "imports", "food", "in-o", "in-p", "in-g", "bank"]
q = [
 {"type": "map", "map": {"show": []}, "eyebrow": "Rand per US dollar, November 2026", "headline": "How the rand reaches your pocket",
  "stat": {"value": "R17.55", "label": "20 Nov (R16.60 on 11 Nov)", "count": {"from": 16.60, "to": 17.55, "decimals": 2, "prefix": "R"}},
  "receipt": "MTFX daily USD/ZAR rates, 11 and 20 Nov 2026",
  "voiceover": "In November, the rand slipped from about sixteen rand sixty to seventeen rand fifty-five to the US dollar. That one number travels through your whole budget."},
 {"type": "map", "map": {"show": ["fuel"]}, "eyebrow": "1 · Fuel", "headline": "Oil is priced in dollars",
  "stat": {"value": "+R85", "label": "on a $90 barrel", "count": {"from": 0, "to": 85, "prefix": "+R"}},
  "receipt": "Calculation: $90 × R0.95 more per dollar",
  "voiceover": "Fuel first. Oil is priced in dollars, so a ninety-dollar barrel now costs about eighty-five rand more."},
 {"type": "map", "map": {"show": ["fuel", "imports"]}, "eyebrow": "2 · Imports", "headline": "Imported goods cost more",
  "stat": {"value": "+R475", "label": "on a $500 phone", "count": {"from": 0, "to": 475, "prefix": "+R"}},
  "receipt": "Calculation: $500 × R0.95 more per dollar",
  "voiceover": "Imports next. A phone priced at five hundred dollars costs about four hundred and seventy-five rand more."},
 {"type": "map", "map": {"show": ["fuel", "imports", "food"]}, "eyebrow": "3 · Transport and food", "headline": "Dearer fuel moves everything",
  "stat": {"value": "15.2%", "label": "transport inflation, Oct 2026", "count": {"from": 0, "to": 15.2, "decimals": 1, "suffix": "%"}},
  "receipt": "Stats SA CPI, October 2026 (via SAnews)",
  "voiceover": "Dearer fuel raises transport costs and, over time, food prices. Transport inflation hit fifteen point two percent in October."},
 {"type": "map", "map": {"show": ["fuel", "imports", "food", "in-o", "in-p", "in-g"]}, "eyebrow": "4 · Inflation", "headline": "It all flows into inflation",
  "stat": {"value": "5.2%", "label": "Oct 2026, up from 4.5%", "count": {"from": 4.5, "to": 5.2, "decimals": 1, "suffix": "%"}},
  "receipt": "Stats SA CPI, October 2026",
  "voiceover": "It all flows into inflation, which rose to five point two percent in October, up from four point five."},
 {"type": "map", "map": {"show": ALL}, "eyebrow": "5 · Interest rates", "headline": "The Reserve Bank watches inflation",
  "stat": {"value": "7.25%", "label": "repo rate, held 19 Nov 2026"},
  "receipt": "SARB MPC statement, 19 Nov 2026",
  "voiceover": "Inflation is what the Reserve Bank watches. On the nineteenth of November it held the repo rate at seven point two five percent."},
 {"type": "map", "map": {"show": ALL}, "eyebrow": "It works both ways", "headline": "When the rand firms, these costs ease",
  "voiceover": "The rand moves both ways. When it firms, these costs ease."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
 "slug": "short-rand-reaches-your-pocket", "size": [1080, 1920], "countdown": {"from": 5}, "metro": metro,
 "disclaimer": "Education, not financial advice.",
 "voice": EMMA, "timing": {"lead_in": 600}, "scenes": q,
 "endcard": {"title": "Know where your <em>money</em> goes", "subtitle": "Sources in the description", "handle": "@MzansiMoneyMatters",
             "voiceover": "Follow Mzansi Money Matters for more.", "duration": 3200},
 "thumbnail": {"kicker": "Rand at R17.55", "big": "YOUR POCKET", "line": "How the rand <em>reaches you</em>"},
 "youtube": {"title": "How the weaker rand reaches your pocket (Nov 2026) #shorts", "privacy": "private", "synthetic_media": True,
  "category_id": "27", "tags": ["rand", "rand dollar", "inflation South Africa", "repo rate", "fuel price", "Mzansi Money Matters"],
  "description": "The rand went from about R16.60 to R17.55 per US dollar between 11 and 20 November 2026. Here's how that one number reaches fuel, imports, transport, food, inflation and interest rates.\n\nSources:\n- Rand: MTFX daily USD/ZAR rates (11 Nov: R16.61; 20 Nov: R17.56)\n- Inflation 5.2% in Oct 2026, up from 4.5%; transport inflation 15.2%: Stats SA CPI October 2026 (P0141), SAnews\n- Repo rate held at 7.25% on 19 Nov 2026: SARB MPC statement\n- Fuel and phone examples: own calculation, about R0.95 more per dollar\n\n#Rand #Inflation #RepoRate #Shorts\n\nEducation, not financial advice. Narration is AI-generated."}}
json.dump(short, open("content-short-rand.json", "w"), ensure_ascii=False, indent=2)
print(len(q), "scenes, ~%.0f s" % (sum(s["duration"] for s in q) / 1000))
