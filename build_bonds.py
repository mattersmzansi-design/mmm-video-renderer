"""Builds content-bonds.json (long) and content-short-bonds.json (Short):
"10 Times Government Bonds Weren't Risk-Free", per the LLM-council verdict (12 Nov 2026).
Ranking: by mechanism, from far from a SA rand-bond holder to closest:
foreign-currency debt -> can't print its own money -> local-currency debt.
Counters only for Moody's figures (via Damodaran / Visual Capitalist) and the Greek 53.5% face-value cut.
Wording: restructured / suspended payments, not "didn't pay"; outcomes dated "as of 2026";
SA 1985 = debt standstill, never "default" or "never defaulted".
"""
import json

def est(vo):
    return int(len(vo.split()) / 155 * 60000) + 1300

W = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

def money(to, dec=1):
    return {"from": 0, "to": to, "decimals": dec, "prefix": "$", "suffix": "bn"}

ITEMS = [
 (10, "Zambia, 2020", "Foreign-currency debt", [
   dict(type="point", eyebrow="November 2020", headline="Missed a $42.5 million bond payment",
        body="The first African government to default in the COVID era.",
        vo="In November twenty twenty, Zambia missed a payment of about forty-two and a half million dollars on its dollar bonds. It became the first African government to default in the COVID era."),
   dict(type="point", eyebrow="As of 2026", headline="Restructured, after almost four years of talks",
        vo="It wasn't a lot of money. The problem was what it signalled: the debt was too big to keep paying. Bondholders accepted new terms in twenty twenty-four, after almost four years of negotiation."),
 ]),
 (9, "Ecuador, 2008", "Foreign-currency debt", [
   dict(type="point", eyebrow="December 2008", headline="Refused to pay $3.2 billion of bonds",
        body="The government called the debt illegitimate, then offered about 35 cents per dollar.",
        vo="In twenty oh eight, Ecuador's government stopped paying three point two billion dollars of bonds, not because it couldn't, but because it called the debt illegitimate. Then it offered to buy the bonds back at about thirty-five cents per dollar."),
 ]),
 (8, "Ukraine, 2015", "Foreign-currency debt", [
   dict(type="point", eyebrow="October 2015, after the war in the east began", headline="Bondholders accepted a restructuring",
        stat={"value": "$13.3bn", "label": "Debt in default (Moody's)", "count": money(13.3)},
        vo="In twenty fifteen, after conflict broke out in its east and its economy shrank, Ukraine restructured about thirteen point three billion dollars of debt. War is one of the oldest reasons governments stop paying on time."),
 ]),
 (7, "Venezuela, 2017", "Foreign-currency debt", [
   dict(type="point", eyebrow="November 2017", headline="An oil giant that ran out of dollars",
        stat={"value": "$31.1bn", "label": "Debt in default (Moody's)", "count": money(31.1)},
        vo="Venezuela has some of the world's largest oil reserves. But when oil prices fell and production collapsed, it ran out of the dollars it needed. In twenty seventeen it defaulted on about thirty-one billion dollars of debt."),
   dict(type="broll", broll="oil refinery", eyebrow="Venezuela", headline="One of the longest-running defaults of recent years",
        vo="It became one of the longest-running defaults of recent years."),
 ]),
 (6, "Lebanon, 2020", "Foreign-currency debt", [
   dict(type="point", eyebrow="March 2020: its first-ever default", headline="Then the banks froze people's savings",
        stat={"value": "$31.3bn", "label": "Debt in default (Moody's)", "count": money(31.3)},
        vo="Lebanon had never defaulted. Then in March twenty twenty, it missed a one point two billion dollar bond payment, and about thirty-one billion dollars went into default. Its banks, which held much of that debt, restricted people's access to their own savings."),
 ]),
 (5, "Sri Lanka, 2022", "Foreign-currency debt", [
   dict(type="point", eyebrow="April 2022", headline="Suspended about $51 billion of foreign debt",
        body="Inflation hit 69.8% in September 2022. The rupee lost about 80% of its value.",
        vo="In April twenty twenty-two, Sri Lanka ran so low on dollars it couldn't import enough fuel or medicine. It suspended payments on about fifty-one billion dollars of foreign debt. Inflation hit almost seventy percent, and the president fled the country."),
   dict(type="point", eyebrow="As of 2026", headline="Mostly restructured, with an IMF programme",
        vo="As of twenty twenty-six, most of that debt has been restructured, under an IMF programme."),
 ]),
 (4, "Argentina, 2001", "Foreign-currency debt", [
   dict(type="point", eyebrow="December 2001", headline="The record default of its time",
        stat={"value": "$82.3bn", "label": "Debt in default (Moody's)", "count": money(82.3)},
        vo="Argentina had tied its peso one to one with the US dollar, and borrowed heavily in dollars. In December two thousand and one, it defaulted on about eighty-two billion dollars, the biggest default of its time."),
   dict(type="broll", broll="bank vault door", eyebrow="The corralito", headline="Bank deposits frozen. Unemployment near 25%.",
        vo="Banks froze people's deposits. The economy shrank by about eleven percent in a year. And Argentina has defaulted nine times since independence."),
 ]),
 (3, "Greece, 2012", "Couldn't print its own money", [
   dict(type="point", eyebrow="March 2012: the largest restructuring ever", headline="Bondholders accepted a 53.5% cut to face value",
        stat={"value": "53.5%", "label": "Cut to the face value of private bondholders' Greek bonds",
              "count": {"from": 0, "to": 53.5, "decimals": 1, "suffix": "%"}},
        vo="Greece borrowed in euros, a currency it couldn't print. In March twenty twelve, private bondholders accepted a fifty-three point five percent cut to the face value of their bonds, the largest debt restructuring in history."),
   dict(type="chart", eyebrow="Debt in default, Moody's (1983–2022)", headline="Greece dwarfs every other default",
        chart={"kind": "bar", "labels": ["Greece 2012", "Argentina 2001", "Russia 1998", "Lebanon 2020"],
               "values": [264.2, 82.3, 72.7, 31.3], "display": ["$264bn", "$82bn", "$73bn", "$31bn"], "highlight": [0]},
        vo="Measured by the debt involved, about two hundred and sixty-four billion dollars, nothing else comes close. And here's the detail that matters for us: most of those bonds were issued under Greek law, and Greece changed its own law to make all holders accept the deal."),
 ]),
 (2, "Russia, 1998", "Its own currency", [
   dict(type="point", eyebrow="August 1998", headline="Defaulted on bonds in its own currency",
        body="Short-term ruble bonds called GKOs. The ruble then lost about three quarters of its value.",
        vo="Here's the one that breaks a common belief: that a government can always pay debt in its own currency, because it can print it. In August nineteen ninety-eight, Russia defaulted on its own ruble bonds, and the ruble lost about three quarters of its value."),
   dict(type="point", eyebrow="And in 2022", headline="Willing to pay, but blocked by sanctions",
        vo="And in twenty twenty-two, Russia was ruled in default for a different reason: it had the money, but sanctions blocked the payments. Risk isn't only about money."),
 ]),
]

ONE = (1, "Ghana, 2022", "Its own currency, its own savers", [
   dict(type="point", eyebrow="December 2022", headline="Local bonds held by local institutions were restructured too",
        body="More than $11bn of cedi bonds, held largely by banks, pension funds and insurers.",
        vo="And number one. In December twenty twenty-two, Ghana suspended payments on about thirteen billion dollars of foreign bonds. But it also exchanged more than eleven billion dollars' worth of its own local-currency bonds, held largely by local banks, pension funds and insurers, for new bonds that paid less and later."),
   dict(type="point", eyebrow="Why it's number one", headline="It happened at home, in the local currency",
        vo="That's why it's number one for us. It's close to home, it's recent, and it hit local savers' institutions in the local currency. As of twenty twenty-six, Ghana has restructured its bonds and is paying again."),
])

SA = [
 {"type": "plain", "eyebrow": "Closer to home: 1985", "headline": "South Africa's debt standstill",
  "body": "About $13.6 billion of mostly bank and private-sector short-term foreign debt (SARB).",
  "voiceover": "Before number one, a story from closer to home. In August nineteen eighty-five, after P W Botha's Rubicon speech, foreign banks refused to roll over South Africa's short-term loans. The country declared a standstill on repaying about thirteen point six billion dollars of foreign debt, mostly owed by banks and companies."},
 {"type": "plain", "eyebrow": "Closer to home: 1985", "headline": "Fully repaid in 2001, 16 years to the day",
  "body": "Historians disagree on whether it counts as a sovereign default.",
  "voiceover": "Historians still disagree on whether it counts as a sovereign default. The last payment was made in August two thousand and one, sixteen years to the day after the speech."},
]

scenes = [
 {"type": "intro", "eyebrow": "Risk-free?", "headline": "10 times government bonds weren't risk-free",
  "body": "Greece. Argentina. Sri Lanka. Ghana. And one story from South Africa.",
  "voiceover": "You've probably heard that lending to the government is risk-free. Here are ten times it wasn't, and what risk-free really means for your money."},
 {"type": "plain", "eyebrow": "How we ranked them", "headline": "From far away to close to your rand bond",
  "body": "Foreign-currency debt → couldn't print its own money → local-currency debt.",
  "voiceover": "We've ranked them not by size, but by how close they come to a South African holding a government bond in rands. First, governments that borrowed in someone else's currency. Then one that couldn't print its own money. Then the ones that hit bonds in their own currency."},
]
def add(r, title, eb, items):
    scenes.append({"type": "rank", "rank": r, "eyebrow": eb, "headline": title,
                   "voiceover": f"Number {W[r]}. {title.replace(', ', ', ')}." if r != 1 else f"Number one. {title}."})
    for it in items:
        s = {"type": it["type"], "eyebrow": it["eyebrow"], "headline": it["headline"], "voiceover": it["vo"]}
        if it["type"] in ("point", "chart"): s.update(rank=r)
        if it["type"] == "point": s["name"] = title
        for k in ("body", "stat", "broll", "chart"):
            if it.get(k): s[k] = it[k]
        scenes.append(s)
for item in ITEMS:
    add(*item)
scenes += SA
add(*ONE)
scenes += [
 {"type": "plain", "eyebrow": "So what does 'risk-free' mean?", "headline": "Low credit risk. Not zero risk. Not inflation-proof.",
  "body": "Credit risk: will you be paid back? Inflation risk: will the money still buy as much?",
  "voiceover": "So what does risk-free really mean? Usually, low credit risk: the government is very likely to pay you back. It doesn't mean zero risk, and it doesn't mean your money keeps its value. Weimar Germany and Zimbabwe paid people back in money that had become worthless."},
 {"type": "plain", "eyebrow": "For South Africans", "headline": "RSA Retail Savings Bonds: lower credit risk, not none",
  "body": "About 90% of SA government debt is in rand. Fixed-rate bonds carry more inflation risk; inflation-linked bonds are designed to reduce it.",
  "voiceover": "About ninety percent of South Africa's government debt is in rands, so RSA Retail Savings Bonds carry lower credit risk, but not none. They come in fixed-rate and inflation-linked types. Fixed-rate bonds carry more inflation risk. Inflation-linked bonds are designed to reduce it. This is education, not financial advice."},
 {"type": "plain", "eyebrow": "Your turn", "headline": "Did you know government bonds could fail?",
  "voiceover": "Did you know government bonds could fail? Tell us in the comments."},
]
for s in scenes:
    s["duration"] = est(s["voiceover"])

base = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
        "voice": {"name": "en-US-BrianMultilingualNeural", "rate": "+4%", "pitch": "+0Hz", "lead_pad": 400, "tail_pad": 900},
        "timing": {"lead_in": 900}}

long = dict(base, slug="top10-bonds-not-risk-free", countdown={"from": 10},
 disclaimer="Education, not financial advice. Outcomes as of 2026.",
 thumbnail={"kicker": "Government bonds", "big": "RISK-FREE?", "line": "10 times they <em>weren't</em>", "photo": "torn paper document"},
 scenes=scenes,
 endcard={"title": "Know your <em>risk</em>", "subtitle": "Subscribe for South African money, explained.",
          "handle": "@MzansiMoneyMatters", "duration": 5000},
 youtube={"title": "10 Times Government Bonds Weren't Risk-Free", "privacy": "private", "synthetic_media": True, "category_id": "27",
  "tags": ["government bonds", "sovereign default", "risk-free", "RSA Retail Savings Bonds", "Greece", "Argentina", "Ghana", "Mzansi Money Matters"],
  "description": ("They say lending to the government is risk-free. Here are 10 times it wasn't, from Zambia and Argentina to Greece, "
   "Russia and Ghana, plus South Africa's 1985 debt standstill, and what 'risk-free' really means for your money.\n\n{chapters}\n\n"
   "Ranking: by how close each case comes to a South African holding a rand government bond (foreign-currency debt, then a "
   "country that couldn't print its own money, then local-currency debt). Default amounts: Moody's data via Aswath Damodaran / "
   "Visual Capitalist (1983–2022). SA 1985 standstill: South African Reserve Bank. Outcomes as of 2026.\n\n"
   "Education, not financial advice. Narration and some visuals are AI-generated. Stock footage from Pexels.")})

q = [
 {"type": "broll", "broll": "bank vault door", "eyebrow": "Risk-free?", "headline": "They told you government bonds are risk-free",
  "voiceover": "They told you government bonds are risk-free."},
 {"type": "point", "rank": 3, "name": "Greece, 2012", "eyebrow": "Greece, 2012", "headline": "Bondholders accepted a 53.5% cut",
  "stat": {"value": "53.5%", "label": "Cut to face value", "count": {"from": 0, "to": 53.5, "decimals": 1, "suffix": "%"}},
  "voiceover": "In twenty twelve, Greek bondholders accepted a fifty-three point five percent cut to the face value of their bonds."},
 {"type": "plain", "eyebrow": "And number one?", "headline": "Local-currency bonds. Local pension funds.",
  "voiceover": "But number one on our list happened to a country's own-currency bonds, held by its own pension funds."},
 {"type": "plain", "eyebrow": "And South Africa?", "headline": "We have our own 1985 story.",
  "voiceover": "And South Africa has its own story, from nineteen eighty-five."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-bonds-risk-free", size=[1080, 1920], countdown={"from": 10},
 disclaimer="Education, not financial advice.",
 voice={"name": "en-US-BrianMultilingualNeural", "rate": "+6%", "pitch": "+0Hz", "lead_pad": 300, "tail_pad": 600},
 timing={"lead_in": 600}, scenes=q,
 endcard={"title": "All 10 on the <em>channel</em>", "subtitle": "10 times government bonds weren't risk-free",
          "handle": "@MzansiMoneyMatters", "voiceover": "Watch all ten on Mzansi Money Matters.", "duration": 3500},
 youtube={"title": "Government bonds are risk-free... right? #shorts", "privacy": "private", "synthetic_media": True,
  "category_id": "27", "tags": ["government bonds", "risk-free", "Greece", "Mzansi Money Matters"],
  "description": "Greek bondholders accepted a 53.5% cut in 2012. Number one on our list is even closer to home. Full video on Mzansi Money Matters.\n\nEducation, not financial advice. Narration is AI-generated. Stock footage from Pexels."})

json.dump(long, open("content-bonds.json", "w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-bonds.json", "w"), ensure_ascii=False, indent=2)
for n, d in (("long", long), ("short", short)):
    print(n, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"]) / 60000))
