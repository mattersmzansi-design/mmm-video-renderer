"""Builds content-kingdoms.json (long) and content-short-kingdoms.json (Short):
"Richest Royal Families in the World: Top 10 by Net Worth & How They Made It", following the LLM-council verdict of 14 Nov 2026.
Rule: one entry per reigning monarchy. Each entry uses the latest published estimate for the current ruler or house that has a
named source, and entries are ranked by the low end of that estimate. Badges: FAMILY = the whole dynasty; PERSONAL = the monarch alone.
The two kinds are not like-for-like, and the video says so on screen.
Excluded by the rule: Kuwait (no reliable named source) and Luxembourg (its figure dates from before the current Grand Duke).
Left out on editorial grounds: eSwatini.
Neutral wording throughout: reported facts only.
Narrator: Kokoro bf_emma.
"""
import json

def est(vo):
    return int(len(vo.split()) / 150 * 60000) + 1300

W = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

def stat(value, label, to, prefix, suffix, dec=0):
    return {"value": value, "label": label, "count": {"from": 0, "to": to, "decimals": dec, "prefix": prefix, "suffix": suffix}}

# r, name, place, badge, stat, receipt, vo1 (figure), how_head, how_vo, broll query
C = [
 dict(r=10, name="King Charles III", place="United Kingdom", badge="PERSONAL",
      st=stat("£680m", "Personal wealth · ≈ $0.9bn", 680, "£", "m"),
      receipt="Sunday Times Rich List, May 2026 · personal assets only",
      vo="King Charles the Third of the United Kingdom. The Sunday Times Rich List puts his personal wealth at about six hundred and eighty million pounds, roughly nine hundred million US dollars.",
      hh="Private estates, plus an inherited portfolio",
      hvo="That figure counts his private estates, Sandringham and Balmoral, which he inherited from Queen Elizabeth the Second, along with an investment portfolio. It leaves out the Crown Estate and the Duchy of Lancaster, which the Sunday Times doesn't count as his personal property. That's why the most famous monarch in the world comes tenth on this list.",
      hr="Excludes the Crown Estate and the Duchy of Lancaster · Sunday Times Rich List 2026",
      broll="Scottish highlands castle"),
 dict(r=9, name="Prince Albert II", place="Monaco", badge="PERSONAL",
      st=stat("~$1bn", "Widely cited estimate", 1, "~$", "bn"),
      receipt="Widely cited estimate; no official disclosure · lovemoney (2025)",
      vo="Prince Albert the Second of Monaco. His fortune is widely estimated at around one billion dollars, though the palace has never published a figure.",
      hh="A 700-year-old dynasty in a tiny, expensive country",
      hvo="The Grimaldi family has ruled Monaco since twelve ninety-seven. Monaco is smaller than many South African suburbs, but it has some of the most expensive property on Earth, and it's a magnet for the world's wealthy, thanks largely to its tax rules.",
      hr="Grimaldi family, rulers of Monaco since 1297",
      broll="Monaco harbour yachts"),
 dict(r=8, name="Sheikh Mohammed bin Rashid", place="Dubai, UAE", badge="PERSONAL",
      st=stat("$4bn", "Personal wealth estimate", 4, "$", "bn"),
      receipt="Forbes richest royals, 2011 · the latest Forbes estimate",
      vo="Sheikh Mohammed bin Rashid Al Maktoum, the ruler of Dubai. Forbes last estimated his personal wealth at about four billion dollars, back in twenty eleven.",
      hh="From trading port to global hub",
      hvo="Dubai has little oil compared with its neighbours, so it built its wealth on trade, aviation, property and tourism instead. Sheikh Mohammed is linked to Dubai Holding, a large investment group, and he founded Godolphin, one of the best-known horse-racing operations in the world.",
      hr="Dubai Holding; Godolphin · Forbes 2011",
      broll="Dubai skyline aerial"),
 dict(r=7, name="King Mohammed VI", place="Morocco", badge="PERSONAL",
      st=stat("$5.7bn", "Personal wealth estimate", 5.7, "$", "bn", 1),
      receipt="Forbes, 2015 · the latest Forbes estimate",
      vo="King Mohammed the Sixth of Morocco. In twenty fifteen, Forbes estimated his wealth at five point seven billion dollars, which made him the richest monarch in Africa on its list.",
      hh="A holding company that spans Africa",
      hvo="Most of that wealth sits in Al Mada, the investment holding company formerly known as S N I. It holds a stake of almost half in Attijariwafa Bank, one of Africa's largest banks, along with interests in mining, energy and retail. It operates in about two dozen African countries.",
      hr="Al Mada (formerly SNI): ~46.5% of Attijariwafa Bank · company filings via TSA; Afrik.com",
      broll="Casablanca city aerial"),
 dict(r=6, name="Prince Hans-Adam II", place="Liechtenstein", badge="PERSONAL",
      st=stat("$9.2bn", "Personal wealth estimate", 9.2, "$", "bn", 1),
      receipt="Bloomberg Billionaires Index, Sep 2023",
      vo="Prince Hans-Adam the Second of Liechtenstein. Bloomberg's Billionaires Index put his fortune at about nine point two billion dollars in twenty twenty-three, the highest of any European royal.",
      hh="A private bank for the world's wealthy",
      hvo="His family owns LGT, a private bank that manages money for wealthy clients and institutions around the world, about three hundred billion dollars of it in twenty twenty-three. The family's wealth goes back to land it held in the twelfth century, which makes it the oldest fortune on Bloomberg's index.",
      hr="LGT Group, owned by the princely house · Bloomberg, Sep 2023",
      broll="Alps castle village"),
 dict(r=5, name="Sultan Hassanal Bolkiah", place="Brunei", badge="PERSONAL",
      st=stat("$20bn", "Personal wealth estimate", 20, "$", "bn"),
      receipt="Forbes richest royals, 2011 · later estimates up to $28bn",
      vo="Sultan Hassanal Bolkiah of Brunei. Forbes estimated his wealth at twenty billion dollars, and some later estimates go as high as twenty-eight billion.",
      hh="Oil, gas, and a reign since 1967",
      hvo="Brunei is a small country on the island of Borneo, built on oil and gas. Oil was found there in nineteen twenty-nine. The Sultan has reigned since nineteen sixty-seven, making him one of the longest-serving monarchs alive, and Brunei's state investment agency owns luxury hotels abroad, including The Dorchester in London.",
      hr="Oil & gas · Brunei Investment Agency owns the Dorchester Collection",
      broll="offshore oil platform"),
 dict(r=4, name="King Vajiralongkorn", place="Thailand", badge="PERSONAL",
      st=stat("$30bn+", "Estimates range up to $43bn", 30, "$", "bn+"),
      receipt="Forbes (Crown Property Bureau, $30bn+); CEOWORLD 2019 ($43bn); Reuters 2018",
      vo="King Maha Vajiralongkorn of Thailand. Estimates of his wealth start at about thirty billion dollars and reach forty-three billion.",
      hh="Land in Bangkok, and stakes in a bank and a cement giant",
      hvo="The wealth comes from the assets of the Crown Property Bureau. According to Reuters, those assets were registered in the King's name in twenty eighteen. They include prime land in Bangkok, about twenty-three percent of Siam Commercial Bank and about a third of Siam Cement Group, one of the country's biggest companies.",
      hr="Crown Property Bureau assets registered in the King's name, 2018 · Reuters",
      broll="Bangkok skyline night"),
 dict(r=3, name="The Al Thani family", place="Qatar", badge="FAMILY",
      st=stat("$199.5bn", "Whole family · estimate", 199.5, "$", "bn", 1),
      receipt="Bloomberg World's Richest Families, Dec 2025",
      vo="The Al Thani family of Qatar. Bloomberg puts the ruling family's wealth at one hundred and ninety-nine point five billion dollars. They've ruled Qatar since the mid eighteen hundreds.",
      hh="One of the world's biggest gas fields",
      hvo="Qatar sits on a share of one of the largest natural gas fields in the world, and it's one of the biggest exporters of liquefied natural gas. Over the years, that gas money has gone into assets around the world. Bloomberg points to property in London and a stake in the Italian fashion house Valentino.",
      hr="Offshore gas · London property; Valentino stake · Bloomberg, Dec 2025",
      broll="Doha skyline"),
 dict(r=2, name="The Al Saud family", place="Saudi Arabia", badge="FAMILY",
      st=stat("$213.6bn", "Whole family · estimate", 213.6, "$", "bn", 1),
      receipt="Bloomberg World's Richest Families, Dec 2025 · estimated from decades of royal-court payouts",
      vo="The Al Saud family of Saudi Arabia, at two hundred and thirteen point six billion dollars. Bloomberg bases this on about fifty years of payments from the royal court to family members, and it says the true figure may well be higher.",
      hh="Oil, since 1938",
      hvo="The source is oil. Commercial quantities were found in nineteen thirty-eight, and today Saudi Aramco is one of the most valuable companies in the world. The family has thousands of members, so this fortune is shared across a very large dynasty.",
      hr="Oil · Saudi Aramco · Bloomberg, Dec 2025",
      broll="oil refinery desert"),
 dict(r=1, name="The Al Nahyan family", place="Abu Dhabi, UAE", badge="FAMILY",
      st=stat("$335.9bn", "Whole family · estimate", 335.9, "$", "bn", 1),
      receipt="Bloomberg World's Richest Families, Dec 2025 · #2 family overall, after the Waltons",
      vo="And at number one, it isn't Saudi Arabia. It's the Al Nahyan family of Abu Dhabi, in the United Arab Emirates, at three hundred and thirty-five point nine billion dollars. That makes it the richest royal family on Bloomberg's list, and second only to America's Walton family, who own Walmart.",
      hh="Oil money, turned into a global investment machine",
      hvo="It started with oil. But the family turned that oil money into investments around the world. Members of the family are behind investment groups with stakes in everything from technology and A I to Manchester City football club. That's how a desert emirate's ruling family built the biggest royal fortune on Bloomberg's list.",
      hr="Oil · global investment groups; Manchester City · Bloomberg, Dec 2025",
      broll="Abu Dhabi skyline"),
]

scenes = [
 {"type": "intro", "eyebrow": "Royal wealth, explained", "headline": "The 10 richest royal families in the world",
  "body": "Their estimated net worth, and how they made it.",
  "voiceover": "Kings, sultans and sheikhs. These are the ten richest royal families in the world, how much they're estimated to be worth, and how they made it."},
 {"type": "plain", "eyebrow": "How we ranked them", "headline": "One entry per monarchy, ranked by the lowest published estimate",
  "body": "PERSONAL = the monarch alone. FAMILY = the whole dynasty. They're not like-for-like. Royal wealth is rarely disclosed, so every figure is an estimate, with its source and year on screen.",
  "voiceover": "Here's how we ranked them. One entry per monarchy, using the latest published estimate we could source, ranked by the low end of that estimate. Some figures cover one monarch personally. Others cover a whole family, so they're not like for like, and we'll label each one. Royal wealth is rarely disclosed, so every number here is an estimate, with its source on screen."},
]
for c in C:
    lead = f"Number {W[c['r']]}." if c['r'] != 1 else "Number one."
    if c["r"] == 3:
        scenes.append({"type": "chart", "eyebrow": "Now the scale changes", "headline": "From here, we count whole dynasties",
                       "chart": {"kind": "bar", "labels": ["UK", "Monaco", "Dubai", "Morocco", "Liecht.", "Brunei", "Thailand", "?", "?", "?"],
                                 "values": [0.9, 1, 4, 5.7, 9.2, 20, 30, 199.5, 213.6, 335.9],
                                 "display": ["0.9", "1", "4", "5.7", "9.2", "20", "30", "", "", ""], "highlight": [7, 8, 9]},
                       "voiceover": "Before the top three, a warning. Everything so far has been one person's wealth, topping out at around thirty billion dollars. The top three are whole ruling families, and they're worth around two hundred billion dollars and more."})
    scenes.append({"type": "rank", "rank": c["r"], "eyebrow": c["place"], "headline": c["name"], "voiceover": lead})
    scenes.append({"type": "point", "rank": c["r"], "name": c["name"], "eyebrow": f"{c['place']} · estimated net worth",
                   "tag": c["badge"] + " · ESTIMATE", "headline": c["name"], "stat": c["st"], "receipt": c["receipt"],
                   "voiceover": c["vo"].replace("And at number one, ", "")})
    scenes.append({"type": "broll", "broll": c["broll"], "eyebrow": "How they made it", "headline": c["hh"],
                   "receipt": c["hr"], "voiceover": c["hvo"]})

scenes += [
 {"type": "chart", "eyebrow": "Estimated wealth, US$ billions", "headline": "Families vs individuals: not like-for-like",
  "chart": {"kind": "bar", "labels": ["UK", "Monaco", "Dubai", "Morocco", "Liecht.", "Brunei", "Thailand", "Qatar", "Saudi", "Abu Dhabi"],
            "values": [0.9, 1, 4, 5.7, 9.2, 20, 30, 199.5, 213.6, 335.9],
            "display": ["0.9", "1", "4", "5.7", "9.2", "20", "30", "199.5", "213.6", "335.9"], "highlight": [9]},
  "voiceover": "Put them side by side, and you can see the pattern. Almost every big royal fortune rests on something the family has controlled for generations: oil and gas, land, a bank, or a stake in a nation's biggest companies. What made the top ones truly global was what came next, turning that income into investments around the world."},
 {"type": "plain", "eyebrow": "The money lesson", "headline": "Wealth that lasts comes from owning assets",
  "body": "Income from oil, land or a business, reinvested for decades, is what compounds.",
  "voiceover": "And there's a lesson in that for the rest of us, on a much smaller scale. Lasting wealth rarely comes from a salary alone. It comes from owning assets that earn an income, and reinvesting that income for a very long time. This is education, not financial advice."},
 {"type": "plain", "eyebrow": "Your turn", "headline": "Which fortune surprised you most?",
  "voiceover": "Which one surprised you most? Let us know in the comments. All our sources are in the description."},
]
for s in scenes:
    s["duration"] = est(s["voiceover"])

EMMA = {"engine": "kokoro", "name": "bf_emma", "speed": 1.05, "lang": "en-gb", "lead_pad": 400, "tail_pad": 900}
base = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
        "voice": EMMA, "timing": {"lead_in": 900}}

SOURCES = """Sources (published estimates; royal wealth is rarely disclosed):
1 Al Nahyan (Abu Dhabi) $335.9bn, 2 Al Saud $213.6bn, 3 Al Thani $199.5bn: Bloomberg, "World's Richest Families 2025" (net worth as of early Dec 2025). Al Saud is estimated from about 50 years of Royal Court payouts.
4 King Vajiralongkorn (Thailand): Forbes richest royals (Crown Property Bureau, $30bn+); CEOWORLD Magazine 2019 ($43bn); Reuters, 2018 (CPB assets registered in the King's name: SCB and Siam Cement stakes, Bangkok land)
5 Sultan Hassanal Bolkiah (Brunei): Forbes richest royals, 2011 ($20bn); CEOWORLD 2019 ($28bn)
6 Prince Hans-Adam II (Liechtenstein): Bloomberg Billionaires Index via Bloomberg/InvestmentNews, Sep 2023 ($9.2bn; LGT)
7 King Mohammed VI (Morocco): Forbes, 2015 ($5.7bn); Al Mada holdings: TSA Algérie; Afrik.com
8 Sheikh Mohammed bin Rashid Al Maktoum (Dubai): Forbes richest royals, 2011 (~$4bn)
9 Prince Albert II (Monaco): widely cited estimate (~$1bn), e.g. lovemoney 2025; no official disclosure
10 King Charles III (UK): Sunday Times Rich List, May 2026 (£680m, personal assets only; excludes the Crown Estate and the Duchy of Lancaster)
Not ranked: Kuwait (no reliable named estimate) and Luxembourg (the published figure predates the current Grand Duke)."""

long = dict(base, slug="top10-richest-royals", countdown={"from": 10},
 disclaimer="Published estimates, not audited figures. Education, not financial advice.",
 thumbnail={"kicker": "Richest royal families", "big": "$335.9 BN", "line": "#1 isn't <em>Saudi</em>", "photo": "gold crown jewels"},
 scenes=scenes,
 endcard={"title": "Own <em>assets</em>", "subtitle": "Subscribe for South African money, explained.",
          "handle": "@MzansiMoneyMatters", "duration": 5000},
 youtube={"title": "Richest Royal Families in the World: Top 10 by Net Worth & How They Made It", "privacy": "private",
  "synthetic_media": True, "category_id": "27",
  "tags": ["richest royal families", "richest royals", "richest kings in the world", "royal family net worth", "Al Nahyan",
           "Saudi royal family", "Sultan of Brunei", "King Charles net worth", "Mzansi Money Matters"],
  "description": ("The 10 richest royal families and monarchs in the world: their estimated net worth, and how each fortune was made, "
   "from oil and gas to banks, land and global investments.\n\nHow we ranked them: one entry per reigning monarchy, using the latest "
   "published estimate with a named source, ranked by the low end of that estimate. PERSONAL figures cover the monarch alone, and FAMILY "
   "figures cover the whole dynasty, so they are not like-for-like.\n\n{chapters}\n\n" + SOURCES +
   "\n\nIndependent channel, not affiliated with any government or royal house. Education, not financial advice. "
   "Narration and some visuals are AI-generated. Stock footage from Pexels.")})

q = [
 {"type": "broll", "broll": "royal palace gates gold", "eyebrow": "The world's richest royals", "headline": "The British King? About $0.9bn",
  "voiceover": "The King of the United Kingdom is worth about nine hundred million dollars personally. Among the world's richest royals, that's not even close."},
 {"type": "point", "eyebrow": "Saudi Arabia · whole family", "tag": "FAMILY · ESTIMATE", "headline": "The Al Saud family",
  "stat": stat("$213.6bn", "Bloomberg, Dec 2025", 213.6, "$", "bn", 1),
  "receipt": "Bloomberg World's Richest Families, Dec 2025",
  "voiceover": "Saudi Arabia's royal family is estimated at two hundred and thirteen billion dollars, built on oil."},
 {"type": "plain", "eyebrow": "But here's the twist", "headline": "#1 isn't Saudi",
  "body": "The top royal fortune is worth over $330 billion.",
  "voiceover": "But the richest royal family on Earth isn't Saudi. It's worth more than three hundred and thirty billion dollars."},
 {"type": "plain", "eyebrow": "Every figure. Every source.", "headline": "The full top 10 is on the channel",
  "voiceover": "Who is it, and how did they make it? The full top ten, with every source, is on our channel."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-richest-royals", size=[1080, 1920], countdown={"from": 10},
 disclaimer="Published estimates. Education, not financial advice.",
 voice=dict(EMMA, lead_pad=300, tail_pad=600), timing={"lead_in": 600}, scenes=q,
 endcard={"title": "#1 isn't <em>Saudi</em>", "subtitle": "10 richest royals, sources included",
          "handle": "@MzansiMoneyMatters", "voiceover": "Watch the full top ten on Mzansi Money Matters.", "duration": 3500},
 youtube={"title": "The richest royal family isn't Saudi #shorts", "privacy": "private", "synthetic_media": True,
  "category_id": "27", "tags": ["richest royal family", "royal family net worth", "richest royals", "Mzansi Money Matters"],
  "description": "King Charles: about $0.9bn personally. Saudi Arabia's royal family: $213.6bn (Bloomberg, Dec 2025). But #1 isn't Saudi. Full top 10 with sources on Mzansi Money Matters.\n\nPublished estimates. Education, not financial advice. Narration is AI-generated. Stock footage from Pexels."})

json.dump(long, open("content-kingdoms.json", "w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-kingdoms.json", "w"), ensure_ascii=False, indent=2)
for n, d in (("long", long), ("short", short)):
    print(n, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"]) / 60000))
