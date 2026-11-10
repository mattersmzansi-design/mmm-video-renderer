"""Builds content-poverty.json (long) and content-short-poverty.json (Short) from
Page & Pande (2018), "Ending Global Poverty: Why Money Isn't Enough", Journal of Economic Perspectives 32(4),
following the LLM-council verdict (11 Nov 2026):
- counters only for verified numbers; unverified figures voiced and attributed ("the paper estimates");
- our ranking rule shown on screen; leakage, never theft; 41% is a relative cut;
- one factual mention of South Africa, no commentary; dated-data caveat; Short withholds the fix.
"""
import json

def est(vo):
    return int(len(vo.split()) / 155 * 60000) + 1300

W = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

# r, title, eyebrow(for rank card), scenes
ITEMS = [
 (10, "Citizens can't see where money goes", "Information", [
   dict(type="point", eyebrow="The problem", headline="You can't hold anyone accountable for spending you can't see",
        vo="If poor citizens can't see how public money is spent, they can't push for better services. The authors argue that information is part of the plumbing."),
   dict(type="point", eyebrow="What worked", headline="Report cards on politicians, printed in local newspapers",
        body="Delhi, India: candidate report cards built from Right to Information data.",
        vo="In Delhi, researchers worked with civil society groups to publish report cards on politicians in local newspapers, using right to information data. Politicians shifted spending towards the public services voters wanted."),
 ]),
 (9, "Prestige projects", "Political will", [
   dict(type="point", eyebrow="What the authors call vanity projects", headline="High-visibility spending vs the basics",
        stat={"value": "£30m", "label": "Rwanda's 'Visit Rwanda' Arsenal deal, 2018",
              "count": {"from": 0, "to": 30, "decimals": 0, "prefix": "£", "suffix": "m"}},
        vo="Governments also choose where money goes. The authors point to prestige spending, such as Rwanda's roughly thirty million pound tourism sponsorship deal with Arsenal football club in twenty eighteen, while basic services remain thin."),
   dict(type="point", eyebrow="What worked", headline="One boss, clear accountability",
        body="Indian districts where officials answered to a single politician ran the workfare programme better.",
        vo="Their fix is about accountability. In India, districts where officials answered to a single politician delivered the national workfare programme better than districts with several competing bosses."),
 ]),
 (8, "Campaigns that go around the health system", "Health", [
   dict(type="point", eyebrow="1920s: two hookworm campaigns", headline="One bypassed the government. One built on it.",
        stat={"value": "1927", "label": "Costa Rica's public health ministry founded"},
        vo="Donors love single-disease campaigns because the results are easy to count. But in the nineteen twenties, a hookworm campaign in Madras, India, worked around the government and left little behind. In Costa Rica, a similar campaign worked through schools and local health boards, and helped lay the foundation for its health ministry, created in nineteen twenty-seven."),
 ]),
 (7, "Weak 'invisible infrastructure'", "Regulation", [
   dict(type="point", eyebrow="Invisible infrastructure", headline="Schools, clinics, property rights, and rules on lending",
        vo="The authors call it invisible infrastructure: working schools and clinics, property rights, and rules that protect people from bad lenders. Roads and buildings are easy to see. These aren't."),
   dict(type="point", eyebrow="When the state doesn't regulate", headline="Microfinance boom, then crash",
        body="Andhra Pradesh, India, 2010: aggressive lending, then a crisis and a credit collapse.",
        vo="In the Indian state of Andhra Pradesh, a boom in for-profit microloans led to aggressive lending and a crisis in twenty ten. When credit then dried up, household earnings fell. And in Liberia, when public schools were handed to private operators, one operator pushed weaker pupils back to public schools."),
 ]),
 (6, "Cash alone isn't enough", "Cash transfers", [
   dict(type="point", eyebrow="Cash helps, for a while", headline="One illness or flood can wipe it out",
        vo="Giving poor families cash works. Studies show it raises spending and savings. But one illness, flood or lawsuit can wipe it out."),
   dict(type="broll", broll="goats farm village", eyebrow="What lasts longer", headline="Assets, coaching, savings and health, together",
        vo="So-called graduation programmes combine a productive asset, like livestock, with coaching, savings accounts and health support. Tested across six countries, they produced gains that lasted for years."),
 ]),
 (5, "Poverty moved to middle-income countries", "Geography", [
   dict(type="point", eyebrow="The paper's data, 1987 vs 2013", headline="Most of the extreme poor now live in middle-income countries",
        body="The paper lists South Africa among eight countries holding about half the world's extreme poor.",
        vo="In nineteen eighty-seven, most of the world's extremely poor people lived in low-income countries. By twenty thirteen, the paper estimates more than sixty percent lived in middle-income countries, which get little aid per poor person. It lists eight countries holding about half of them, and South Africa is one of the eight."),
   dict(type="plain", eyebrow="A note on dates", headline="Data 2013–2018. The poverty line has since been revised.",
        body="The World Bank's extreme poverty line has risen from $1.90 to $3.00 a day.",
        vo="A note on dates. This research uses data up to twenty thirteen, and the World Bank's poverty line has since been raised from one dollar ninety to three dollars a day. More recent data shows extreme poverty concentrating again in sub-Saharan Africa."),
 ]),
 (4, "Aid that bypasses the state", "Foreign aid", [
   dict(type="point", eyebrow="Going around government", headline="When donors avoid the state, the state never learns",
        vo="Donors often route money through charities and contractors instead of governments, to avoid red tape and corruption. The paper estimates that in twenty thirteen, less than half of social aid and only about seven percent of humanitarian aid went through recipient governments' own systems."),
   dict(type="point", eyebrow="The authors' fix", headline="Work through government, with a plan to hand over",
        vo="That can make sense in a disaster. But long term, the authors argue, ministries that never run programmes never get better at running them. Their fix: work through government, with a clear plan to hand over."),
 ]),
 (3, "The tax gap", "Tax", [
   dict(type="point", eyebrow="Too little, collected the wrong way", headline="Middle-income countries lean on taxes that hit the poor hardest",
        vo="The paper estimates that high-poverty middle-income countries collect only about seventeen percent of their economy in tax, and lean on taxes like VAT that hit poor households hardest."),
   dict(type="point", eyebrow="A surprising finding", headline="Paying tax made citizens demand more",
        stat={"value": "+28%", "label": "Rise in political participation after door-to-door tax collection, DRC (Weigel)",
              "count": {"from": 0, "to": 28, "decimals": 0, "prefix": "+", "suffix": "%"}},
        vo="Here's the surprise. In the Democratic Republic of the Congo, economist Jonathan Weigel found that when the government collected property tax door to door, citizens' political participation rose by five percentage points, about twenty-eight percent. People who pay tax start demanding something back."),
 ]),
 (2, "Growth captured at the top", "Inequality", [
   dict(type="chart", eyebrow="India, share of total income growth since 1980", headline="The top 10% took six times more than the bottom half",
        chart={"kind": "bar", "labels": ["Top 10%", "Bottom 50%"], "values": [66, 11], "display": ["66%", "11%"], "highlight": [0]},
        vo="Growth lifts many people, but not evenly. In India, according to the World Inequality Report, the top ten percent of earners captured about sixty-six percent of all income growth since nineteen eighty. The bottom half got about eleven percent."),
   dict(type="point", eyebrow="The authors' point", headline="Growth needs to be paired with targeted support",
        vo="The authors argue that growth alone won't reach the poorest. It needs to come with targeted support and protection for groups that keep getting left behind."),
 ]),
 (1, "The leaky human chain", "Leakage", [
   dict(type="point", eyebrow="The human chain", headline="Every link between budget and citizen is a chance for money to leak",
        vo="And number one. Public money passes through a long human chain: politicians, senior officials, district offices, and the clerk who finally pays you. Every link is a chance for money to leak away before it reaches the people it was meant for."),
   dict(type="point", eyebrow="India's rural jobs programme", headline="Payments that didn't match real work",
        vo="India's huge rural jobs programme showed it clearly. The paper cites survey data suggesting that only about half of the work recorded on paper in two thousand seven and eight matched real workers."),
   dict(type="point", eyebrow="Fix one: biometric smartcards", headline="Leakage cut by about 41%",
        stat={"value": "41%", "label": "Relative drop in leakage, Andhra Pradesh (Muralidharan, Niehaus & Sukhtankar)",
              "count": {"from": 0, "to": 41, "decimals": 0, "suffix": "%"}},
        vo="The fix wasn't more money. In Andhra Pradesh, paying wages through biometric smartcards cut leakage by about forty-one percent, payments arrived faster, and workers' incomes went up."),
   dict(type="point", eyebrow="Fix two: digital fund flows", headline="Spending down 24%, wages unchanged",
        stat={"value": "24%", "label": "Drop in programme spending, Bihar (Banerjee et al.)",
              "count": {"from": 0, "to": 24, "decimals": 0, "suffix": "%"}},
        vo="In Bihar, sending funds digitally, skipping layers of officials, cut programme spending by twenty-four percent, with no drop in wages paid to real workers. Same money in, more of it arriving."),
 ]),
]

scenes = [
 {"type": "intro", "eyebrow": "Page & Pande, 2018", "headline": "Why money alone can't end poverty",
  "body": "10 places poverty money disappears before it reaches the poor.",
  "voiceover": "Over three decades, the world achieved something extraordinary. And then progress started to slow. Two economists asked why money alone isn't finishing the job."},
 {"type": "point", "eyebrow": "The good news", "headline": "The share of people in extreme poverty fell by 34 points",
  "stat": {"value": "−34 pts", "label": "Fall in the share of the world in extreme poverty, 1981–2013",
           "count": {"from": 0, "to": 34, "decimals": 0, "prefix": "−", "suffix": " pts"}},
  "rank": 0, "name": "1981–2013",
  "voiceover": "Between nineteen eighty-one and twenty thirteen, the share of the world living in extreme poverty fell by thirty-four percentage points, to about eleven percent."},
 {"type": "plain", "eyebrow": "Our source, and our ranking", "headline": "Ranked by how directly money is lost before it reaches the poor",
  "body": "Lucy Page (MIT) and Rohini Pande (then Harvard Kennedy School, now Yale). Journal of Economic Perspectives, 2018. The ranking is ours, not the authors'.",
  "voiceover": "This video is based on research by economists Lucy Page and Rohini Pande, published in the Journal of Economic Perspectives. They describe the obstacles. The ranking is ours: by how directly money is lost before it reaches the poor."},
]
for r, title, eb, items in ITEMS:
    scenes.append({"type": "rank", "rank": r, "eyebrow": eb, "headline": title,
                   "voiceover": f"Number {W[r]}. {title.replace(chr(39) + 'invisible infrastructure' + chr(39), 'invisible infrastructure')}."})
    for it in items:
        s = {"type": it["type"], "eyebrow": it["eyebrow"], "headline": it["headline"], "voiceover": it["vo"]}
        if it["type"] in ("point",): s.update(rank=r, name=title)
        if it["type"] == "chart": s.update(rank=r, chart=it["chart"])
        for k in ("body", "stat", "broll"):
            if it.get(k): s[k] = it[k]
        scenes.append(s)
scenes += [
 {"type": "plain", "eyebrow": "The big idea", "headline": "More money helps. Fixing the pipe helps more.",
  "voiceover": "The big idea: ending poverty isn't only about how much money there is. It's about whether the pipes carrying it work, and whether citizens can see inside them."},
 {"type": "plain", "eyebrow": "Your turn", "headline": "Which of these surprised you most?",
  "voiceover": "Which of these surprised you most? Tell us in the comments."},
]
# the intro stat scene has no real rank; drop the badge
scenes[1].pop("rank"); scenes[1].pop("name")
for s in scenes:
    s["duration"] = est(s["voiceover"])

base = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
        "voice": {"name": "en-US-BrianMultilingualNeural", "rate": "+4%", "pitch": "+0Hz", "lead_pad": 400, "tail_pad": 900},
        "timing": {"lead_in": 900}}

long = dict(base, slug="top10-poverty-money-leaks", countdown={"from": 10},
 disclaimer="Education, not financial or political advice. Research data 2013–2018.",
 thumbnail={"kicker": "Economists found", "big": "WHERE DID", "line": "the <em>poverty money</em> go?", "photo": "water pipe leak"},
 scenes=scenes,
 endcard={"title": "Follow the <em>money</em>", "subtitle": "Subscribe for South African money, explained.",
          "handle": "@MzansiMoneyMatters", "duration": 5000},
 youtube={"title": "10 Places Poverty Money Disappears Before It Reaches the Poor", "privacy": "private",
  "synthetic_media": True, "category_id": "27",
  "tags": ["poverty", "economics", "foreign aid", "corruption", "development", "Rohini Pande", "Mzansi Money Matters"],
  "description": ("Why money alone hasn't ended extreme poverty: 10 places it leaks between the budget and the people it's meant for, "
   "and the fixes that worked.\n\n{chapters}\n\n"
   "Source: Lucy Page (MIT) and Rohini Pande (then Harvard Kennedy School, now Yale), \"Ending Global Poverty: Why Money Isn't Enough\", "
   "Journal of Economic Perspectives 32(4), 2018. Also cited: World Inequality Report 2018; Muralidharan, Niehaus & Sukhtankar (2016); "
   "Banerjee et al. (2016); Weigel (2020). The ranking is ours, not the authors'. Research data covers 2013–2018; the World Bank's "
   "extreme poverty line has since been revised to $3.00 a day.\n\n"
   "Education, not financial or political advice. Narration and some visuals are AI-generated. Stock footage from Pexels.")})

q = [
 {"type": "broll", "broll": "water pipe leak", "eyebrow": "Economists found", "headline": "Money for the poor leaks on the way",
  "voiceover": "Money meant for the poor doesn't always reach them. It leaks on the way."},
 {"type": "point", "rank": 1, "name": "The leaky human chain", "eyebrow": "India's rural jobs programme", "headline": "Payments that didn't match real work",
  "voiceover": "In one of the world's biggest jobs programmes, researchers found that payments often didn't match real work."},
 {"type": "plain", "eyebrow": "The fix", "headline": "It wasn't more money.",
  "voiceover": "The fix that worked wasn't more money. It was cheaper, and simpler."},
 {"type": "plain", "eyebrow": "Number 1 of 10", "headline": "See what it was in the full video.",
  "voiceover": "It's number one of ten in our full video."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-poverty-leak", size=[1080, 1920], countdown={"from": 10},
 disclaimer="Education, not financial or political advice.",
 voice={"name": "en-US-BrianMultilingualNeural", "rate": "+6%", "pitch": "+0Hz", "lead_pad": 300, "tail_pad": 600},
 timing={"lead_in": 600}, scenes=q,
 endcard={"title": "The full top <em>10</em>", "subtitle": "Where poverty money disappears",
          "handle": "@MzansiMoneyMatters", "voiceover": "Watch the full top ten on Mzansi Money Matters.", "duration": 3500},
 youtube={"title": "The fix wasn't more money #shorts", "privacy": "private", "synthetic_media": True, "category_id": "27",
  "tags": ["poverty", "economics", "Mzansi Money Matters"],
  "description": "Money meant for the poor leaks on the way. Based on Page & Pande (2018), Journal of Economic Perspectives. Full top 10 on Mzansi Money Matters.\n\nEducation, not financial or political advice. Narration is AI-generated. Stock footage from Pexels."})

json.dump(long, open("content-poverty.json", "w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-poverty.json", "w"), ensure_ascii=False, indent=2)
for n, d in (("long", long), ("short", short)):
    print(n, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"]) / 60000))
