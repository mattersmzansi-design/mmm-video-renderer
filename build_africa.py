"""Africa's richest country? It depends how you measure. Long video + Short. Figures checked 28 Nov 2026."""
import json, subprocess

def est(vo):
    return int(len(vo.split()) / 150 * 60000) + 1300

PORTRAIT_CLIPS = {"africa-06-libya.mp4", "africa-07-joburg.mp4", "africa-08-cape.mp4", "africa-09-cairo.mp4", "africa-10-casablanca.mp4"}
def clip(name, canvas_portrait):
    f = name + ".mp4"
    is_p = f in PORTRAIT_CLIPS
    return {"file": f, "fit": "cover" if is_p == canvas_portrait else "pad"}

EMMA = {"engine": "kokoro", "name": "bf_emma", "speed": 1.0, "lang": "en-gb", "lead_pad": 400, "tail_pad": 800}
WB = "World Bank WDI, July 2026: GNI per capita 2025, Atlas method"
NWW = "New World Wealth, Africa Wealth Report 2026 (June 2026)"
HDR = "UNDP Human Development Report 2025 (2023 data)"
PIP = "World Bank Poverty & Inequality Platform (SA survey 2022)"

L = False
S = [
 {"type": "broll", "broll": clip("africa-01-earth", L), "eyebrow": "Mzansi Money Matters · 2026 data", "headline": "Is South Africa Africa's richest country?",
  "body": "1st… or 6th? It depends how you measure.",
  "voiceover": "Is South Africa Africa's richest country? It can be first, or sixth. It depends on what you measure. Today we test four measures, using the latest published data. The years differ by measure, and each one is shown on screen."},
 {"type": "plain", "eyebrow": "Four measures", "headline": "Income · Millionaires · Wellbeing · Fairness",
  "body": "Latest published data. Years differ by measure and are shown on screen.",
  "voiceover": "Average income per person. The number of dollar millionaires. Human development. And how evenly income is shared."},
 # Round 1
 {"type": "broll", "broll": clip("africa-02-seychelles", L), "rank": 1, "eyebrow": "Round 1 · Income per person", "headline": "Seychelles leads",
  "stat": {"value": "$19,200", "label": "average income per person, 2025", "count": {"from": 0, "to": 19200, "prefix": "$"}}, "receipt": WB,
  "voiceover": "Round one: average income per person, per year, for twenty twenty-five. The World Bank puts Seychelles first, at nineteen thousand two hundred US dollars. It is Africa's only high-income economy."},
 {"type": "broll", "broll": clip("africa-03-mauritius", L), "rank": 1, "eyebrow": "Round 1 · Income per person", "headline": "Mauritius is second",
  "stat": {"value": "$14,040", "label": "per person, 2025 · 1st after adjusting for local prices", "count": {"from": 0, "to": 14040, "prefix": "$"}}, "receipt": WB + "; PPP series",
  "voiceover": "Mauritius is second, at fourteen thousand and forty dollars. Adjust for what money actually buys locally, and Mauritius edges ahead of Seychelles."},
 {"type": "broll", "broll": clip("africa-04-gabon", L), "rank": 1, "eyebrow": "Round 1 · Income per person", "headline": "3. Gabon",
  "stat": {"value": "$7,530", "label": "average income per person, 2025", "count": {"from": 0, "to": 7530, "prefix": "$"}}, "receipt": WB,
  "voiceover": "Third is Gabon, at seven thousand five hundred and thirty dollars, an economy built largely on oil."},
 {"type": "broll", "broll": clip("africa-05-diamonds", L), "rank": 1, "eyebrow": "Round 1 · Income per person", "headline": "4. Botswana",
  "stat": {"value": "$7,390", "label": "average income per person, 2025", "count": {"from": 0, "to": 7390, "prefix": "$"}}, "receipt": WB,
  "voiceover": "Fourth is Botswana, at seven thousand three hundred and ninety dollars, with diamonds at the centre of its economy."},
 {"type": "broll", "broll": clip("africa-06-libya", L), "rank": 1, "eyebrow": "Round 1 · Income per person", "headline": "5. Libya",
  "stat": {"value": "$7,250", "label": "average income per person, 2025", "count": {"from": 0, "to": 7250, "prefix": "$"}}, "receipt": WB,
  "voiceover": "Fifth is Libya, at seven thousand two hundred and fifty dollars, also driven by oil."},
 {"type": "chart", "rank": 1, "rank": 1, "eyebrow": "Round 1 result · " + WB, "headline": "South Africa is 6th on income per person",
  "chart": {"kind": "bar", "labels": ["Seychelles", "Mauritius", "Gabon", "Botswana", "Libya", "S. Africa"],
            "values": [19200, 14040, 7530, 7390, 7250, 6270], "display": ["$19,200", "$14,040", "$7,530", "$7,390", "$7,250", "$6,270"], "highlight": [5]},
  "voiceover": "South Africa comes sixth, at six thousand two hundred and seventy dollars a year. On income per person, the two island nations lead."},
 # Round 2
 {"type": "broll", "broll": clip("africa-07-joburg", L), "rank": 2, "eyebrow": "Round 2 · Number of dollar millionaires", "headline": "South Africa leads by far",
  "stat": {"value": "48,200", "label": "US-dollar millionaires · 131 worth $100m+ · 10 billionaires · June 2026", "count": {"from": 0, "to": 48200}}, "receipt": NWW,
  "voiceover": "Round two: the number of dollar millionaires. That means people with at least one million US dollars they could invest, not counting their main home. On this count, South Africa leads by a wide margin: forty-eight thousand two hundred millionaires, one hundred and thirty-one people worth over a hundred million dollars, and ten billionaires, as at June twenty twenty-six. This is a total, not a per-person figure, so larger economies naturally count more."},
 {"type": "broll", "broll": clip("africa-08-cape", L), "rank": 2, "eyebrow": "Round 2 · Number of dollar millionaires", "headline": "Almost 4 in 10 of Africa's millionaires",
  "stat": {"value": "38%", "label": "of Africa's millionaires live in South Africa", "count": {"from": 0, "to": 38, "suffix": "%"}}, "receipt": NWW,
  "voiceover": "That is thirty-eight percent of all the dollar millionaires in Africa."},
 {"type": "broll", "broll": clip("africa-09-cairo", L), "rank": 2, "eyebrow": "Round 2 · Number of dollar millionaires", "headline": "2. Egypt",
  "stat": {"value": "15,100", "label": "US-dollar millionaires", "count": {"from": 0, "to": 15100}}, "receipt": NWW,
  "voiceover": "Egypt is second, with fifteen thousand one hundred."},
 {"type": "broll", "broll": clip("africa-10-casablanca", L), "rank": 2, "eyebrow": "Round 2 · Number of dollar millionaires", "headline": "3. Morocco",
  "stat": {"value": "8,300", "label": "US-dollar millionaires", "count": {"from": 0, "to": 8300}}, "receipt": NWW,
  "voiceover": "Morocco is third, with eight thousand three hundred, just ahead of Nigeria."},
 {"type": "broll", "broll": clip("africa-11-lagos", L), "rank": 2, "eyebrow": "Round 2 · Number of dollar millionaires", "headline": "4. Nigeria",
  "stat": {"value": "8,100", "label": "US-dollar millionaires · first rise since 2021", "count": {"from": 0, "to": 8100}}, "receipt": NWW,
  "voiceover": "Nigeria is fourth, with eight thousand one hundred, its first rise since twenty twenty-one."},
 {"type": "broll", "broll": clip("africa-12-nairobi", L), "rank": 2, "eyebrow": "Round 2 · Number of dollar millionaires", "headline": "5. Kenya",
  "stat": {"value": "6,500", "label": "US-dollar millionaires", "count": {"from": 0, "to": 6500}}, "receipt": NWW,
  "voiceover": "And Kenya is fifth, with six thousand five hundred. On millionaire numbers, the large mainland economies lead."},
 # Round 3
 {"type": "broll", "broll": clip("africa-13-school-clinic", L), "rank": 3, "eyebrow": "Round 3 · Human development", "headline": "Turning wealth into health and education",
  "body": "The UN's Human Development Index combines life expectancy, schooling and income on a scale of 0 to 1.",
  "voiceover": "Round three: human development. The United Nations' Human Development Index combines life expectancy, schooling and income, on a scale from zero to one. It asks whether wealth turns into longer, better-educated lives."},
 {"type": "chart", "rank": 3, "rank": 3, "eyebrow": "Round 3 result · " + HDR, "headline": "Seychelles and Mauritius lead · SA 6th",
  "chart": {"kind": "bar", "labels": ["Seychelles", "Mauritius", "Algeria", "Egypt", "Tunisia", "S. Africa"],
            "values": [0.848, 0.806, 0.763, 0.754, 0.746, 0.741], "display": ["0.848", "0.806", "0.763", "0.754", "0.746", "0.741"], "highlight": [5]},
  "voiceover": "Seychelles leads at zero point eight four eight, followed by Mauritius at zero point eight zero six. They are the only two African countries in the UN's top tier, above zero point eight. Algeria, Egypt and Tunisia follow. South Africa is sixth, at zero point seven four one."},
 # Round 4
 {"type": "point", "rank": 4, "eyebrow": "Round 4 · How evenly income is shared", "headline": "A check, not a race",
  "body": "Gini index: 0 = everyone has the same · 100 = one person has everything. Lower is more equal.",
  "stat": {"value": "54.1", "label": "South Africa's Gini index (2022 survey)", "count": {"from": 0, "to": 54.1, "decimals": 1}}, "receipt": PIP,
  "voiceover": "Round four is a check, not a race: how evenly income is shared. The Gini index runs from zero, where everyone has the same, to one hundred, where one person has everything. Here, lower means more equal. South Africa scores fifty-four point one, among the highest in the world. So South Africa ranks high on millionaires, and also high on inequality. Both are true at the same time."},
 # Verdict
 {"type": "broll", "broll": clip("africa-15-scale", L), "eyebrow": "The verdict", "headline": "No country wins every round",
  "body": "SA: 1st on millionaires · 6th on income and human development.",
  "voiceover": "So, is South Africa Africa's richest country? On millionaires, yes, by far. On average income and human development, it is sixth, behind Seychelles and Mauritius. No single country wins every round. It depends on what you measure."},
 {"type": "plain", "eyebrow": "What it means for you", "headline": "A country's average is not your number",
  "body": "Your own measure: income, savings and debt. Which round matters most to you? Comment 1, 2, 3 or 4.",
  "voiceover": "And one lesson for your own money. A country's average describes the country, not your household. Your own measure is your income, your savings, and your debt. Which round matters most to you? Tell us in the comments: one, two, three, or four."},
]
for s in S:
    s["duration"] = est(s["voiceover"])

SOURCES = """Sources
- Income per person: World Bank, World Development Indicators (15 July 2026): GNI per capita 2025, Atlas method (NY.GNP.PCAP.CD) and PPP (NY.GNP.PCAP.PP.CD). Seychelles $19,200; Mauritius $14,040 ($37,000 PPP); Gabon $7,530; Botswana $7,390; Libya $7,250; South Africa $6,270.
- Private wealth: New World Wealth, Africa Wealth Report 2026 (figures as at June 2026). South Africa 48,200 millionaires, 131 centi-millionaires, 10 billionaires, 38% of Africa's millionaires; Egypt 15,100; Morocco 8,300; Nigeria 8,100; Kenya 6,500. Millionaire = US$1m+ in liquid investable wealth.
- Human development: UNDP, Human Development Report 2025 (2023 data). Seychelles 0.848; Mauritius 0.806; Algeria 0.763; Egypt 0.754; Tunisia 0.746; South Africa 0.741.
- Inequality: World Bank Poverty and Inequality Platform, Gini index (SI.POV.GINI), South Africa 54.1 (2022 survey)."""

base = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
        "voice": EMMA, "timing": {"lead_in": 900}, "countdown": {"from": 4, "order": "up"}}
long = dict(base, slug="africa-richest-country-2026", scenes=S,
 disclaimer="Education, not financial advice. Figures: World Bank, New World Wealth, UNDP.",
 endcard={"title": "It depends <em>how you measure</em>", "subtitle": "Sources in the description", "handle": "@MzansiMoneyMatters",
          "voiceover": "All sources are in the description. Subscribe to Mzansi Money Matters for more.", "duration": 4500},
 thumbnail={"kicker": "Africa's richest country?", "big": "1ST OR 6TH?", "line": "South Africa, <em>4 measures</em>", "frame": 8},
 youtube={"title": "Is South Africa Africa's Richest Country? 1st… or 6th? (Latest Data)", "privacy": "private", "synthetic_media": True,
  "category_id": "27", "tags": ["richest country in Africa", "Africa richest countries 2026", "Seychelles", "Mauritius", "South Africa millionaires",
   "GNI per capita Africa", "Africa Wealth Report 2026", "Human Development Index Africa", "Mzansi Money Matters"],
  "description": "Is South Africa Africa's richest country? We test four measures with the latest published data (years differ by measure): income per person (World Bank), private wealth (New World Wealth), human development (UNDP) and inequality (World Bank). No single country wins every round.\n\n0:00 Africa's richest country?\nRound 1: Income per person\nRound 2: Number of dollar millionaires\nRound 3: Human development\nRound 4: How evenly income is shared\nThe verdict\nWhat it means for you\n\n" + SOURCES + "\n\n#Africa #RichestCountry #MzansiMoneyMatters\n\nEducation, not financial advice. Narration is AI-generated (Kokoro). Video clips generated with Google Flow (Veo)."})

P = True
Q = [
 {"type": "broll", "broll": clip("africa-01-earth", P), "eyebrow": "Latest data", "headline": "Is SA Africa's richest? 1st or 6th?",
  "voiceover": "Is South Africa Africa's richest country? First, or sixth? It depends what you measure."},
 {"type": "broll", "broll": clip("africa-02-seychelles", P), "eyebrow": "Average income per person", "headline": "Seychelles 1st · SA 6th",
  "stat": {"value": "$19,200", "label": "average income per person, 2025", "count": {"from": 0, "to": 19200, "prefix": "$"}}, "receipt": "World Bank WDI, July 2026",
  "voiceover": "On average income per person, Seychelles is first. South Africa is sixth."},
 {"type": "broll", "broll": clip("africa-07-joburg", P), "eyebrow": "Number of dollar millionaires", "headline": "South Africa 1st",
  "stat": {"value": "48,200", "label": "US-dollar millionaires, June 2026", "count": {"from": 0, "to": 48200}}, "receipt": "New World Wealth, Africa Wealth Report 2026",
  "voiceover": "On the number of dollar millionaires, South Africa is first, with forty-eight thousand two hundred."},
 {"type": "broll", "broll": clip("africa-13-school-clinic", P), "eyebrow": "Health & education", "headline": "Seychelles 1st · SA 6th",
  "stat": {"value": "0.848", "label": "Human Development Index"}, "receipt": "UNDP Human Development Report 2025",
  "voiceover": "On health and education, Seychelles leads again. South Africa is sixth."},
 {"type": "point", "eyebrow": "How evenly income is shared", "headline": "Lower is more equal",
  "stat": {"value": "54.1", "label": "South Africa's Gini index · among the world's highest", "count": {"from": 0, "to": 54.1, "decimals": 1}}, "receipt": "World Bank PIP, 2022 survey",
  "voiceover": "But South Africa also has one of the highest inequality scores in the world."},
 {"type": "broll", "broll": clip("africa-15-scale", P), "eyebrow": "The verdict", "headline": "No country wins every round",
  "voiceover": "No country wins every round. Full breakdown on our channel."},
]
for s in Q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-africa-richest", size=[1080, 1920], scenes=Q, voice=dict(EMMA, lead_pad=300, tail_pad=500),
 timing={"lead_in": 600}, disclaimer="Education, not financial advice.",
 endcard={"title": "It depends <em>how you measure</em>", "subtitle": "Full breakdown on the channel", "handle": "@MzansiMoneyMatters",
          "voiceover": "Follow Mzansi Money Matters.", "duration": 2800},
 youtube={"title": "Is South Africa Africa's richest country? 1st or 6th? #shorts", "privacy": "private", "synthetic_media": True,
  "category_id": "27", "tags": ["richest country in Africa", "Seychelles", "South Africa millionaires", "Mzansi Money Matters"],
  "description": "Seychelles leads on income per person ($19,200, World Bank) and human development (0.848, UNDP). South Africa leads on private wealth (48,200 dollar millionaires, New World Wealth 2026) but has one of the world's highest Gini indexes (54.1, World Bank). No country wins every round.\n\n#Africa #Shorts #MzansiMoneyMatters\n\nEducation, not financial advice. Narration is AI-generated. Video clips generated with Google Flow (Veo)."})

json.dump(long, open("content-africa.json", "w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-africa.json", "w"), ensure_ascii=False, indent=2)
print("long", len(S), "scenes ~%.1f min" % (sum(s["duration"] for s in S) / 60000), "| short ~%.0f s" % (sum(s["duration"] for s in Q) / 1000))
