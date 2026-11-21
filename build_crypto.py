"""Builds content-crypto.json (long video) and content-short-crypto.json (Short):
"Crypto Crash Explained: Bitcoin's 7 Worst Crashes Ever", following the LLM-council verdict of 21 Nov 2026.
Rule: ranked by how far Bitcoin fell from a peak to its next low, whether that took days or months, with each fall counted once.
7 entries, because the verified facts give only 7 distinct falls.
Terra/Celsius/FTX sit inside the 2022 entry. 10/10 (Oct 2025 liquidations) sits inside the 2025-26 entry as its trigger.
Mt. Gox's one-cent flash crash sits inside the 2011 entry and is labelled "one exchange".
No predictions, no rand conversions, no MTI/FSCA claims (unverified). "As of" dates are on screen.
Footage: the owner's Google Flow clips assets/broll/crypto-XX.mp4 (Veo 3.1 Fast, 16:9); the Short pads them into 9:16.
Narrator: Kokoro bf_emma.
"""
import json

def est(vo):
    return int(len(vo.split()) / 150 * 60000) + 1300

W = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven']

def fall(pct, label, dec=0):
    return {"value": f"−{pct}%", "label": label, "count": {"from": 0, "to": pct, "decimals": dec, "prefix": "−", "suffix": "%"}}

C = [
 dict(r=7, name="Black Thursday", when="March 2020", clip="crypto-02-red-desk.mp4",
      story_h="A pandemic panic, and half the price gone in two days",
      story="Number seven: Black Thursday, March twenty twenty. As COVID-19 shut the world down, investors sold almost everything. Bitcoin went from around eight thousand dollars to under four thousand, losing about half its value in two days.",
      st=fall(50, "In about two days · ~$8,000 → under ~$4,000"), src="GOBankingRates; Banxa",
      why_h="Borrowed money made it worse",
      why="What made it so fast? Many traders were using borrowed money. When prices fell, exchanges automatically sold their positions, and those forced sales pushed prices down even further."),
 dict(r=6, name="China crackdown + Tesla U-turn", when="May 2021", clip="crypto-07-mining-rigs.mp4",
      story_h="A record high, then a one-two punch",
      story="Number six: May twenty twenty-one. Bitcoin had just hit a record of around sixty-four thousand dollars. Then Tesla stopped accepting Bitcoin, citing energy concerns, and China cracked down on Bitcoin mining.",
      st=fall(53, "From ~$64,000 · May 2021"), src="GOBankingRates; Fortune (CoinGecko data)",
      why_h="Nearly $1 trillion gone in a week",
      why="Bitcoin fell fifty-three percent. Across the whole crypto market, nearly one trillion dollars in value disappeared in a single week."),
 dict(r=5, name="The 2025–26 crash", when="Oct 2025 – still open", clip="crypto-03-collapsing-bars.mp4",
      story_h="The crash we're living through",
      story="This is the one many of you are living through right now. In October twenty twenty-five, Bitcoin hit a record of about one hundred and twenty-six thousand dollars. On the tenth of October, after a US threat of one hundred percent tariffs on China, about nineteen billion dollars in borrowed trading bets were wiped out in a single day, the largest liquidation on record.",
      st=fall(53.5, "So far · ~$126,000 → $58,570 low (1 Jul 2026)", 1), src="Bloomberg; CoinGlass; CryptoTicker (CoinGecko data) · as of 21 Nov 2026",
      why_h="Biggest in dollars, but not in percent",
      why="By February, Bitcoin had fallen to about sixty thousand dollars, and in July twenty twenty-six it touched fifty-eight thousand five hundred. That's a fall of about fifty-three and a half percent so far. Bitcoin Magazine calls it the largest dollar drop in Bitcoin's history. But in percentage terms, Bitcoin has fallen further before. This crash isn't over, so this number could still change."),
 dict(r=4, name="The 2022 collapse", when="Nov 2021 – Nov 2022", clip="crypto-11-chain-snapping.mp4",
      story_h="Terra, Celsius, FTX: one chain breaking",
      story="Number four: twenty twenty-two. In May, a so-called stablecoin, UST, that was meant to stay at one dollar fell to just twelve cents, and its partner coin LUNA collapsed with it. An estimated forty billion dollars was wiped out. Next, the crypto lenders Celsius and Three Arrows Capital failed.",
      st=fall(77, "Peak to low · Nov 2021 → Nov 2022"), src="Bitget; NerdWallet (−74%); Yahoo Finance; Chainalysis",
      why_h="Then FTX: an $8 billion hole",
      why="Then, in November, the exchange FTX collapsed, with an eight billion dollar hole in its accounts. Customer money had allegedly been moved to a sister trading firm. From its peak, Bitcoin fell seventy-seven percent."),
 dict(r=3, name="Crypto winter", when="Dec 2017 – Dec 2018", clip="crypto-10-frost-grid.mp4",
      story_h="The ICO bubble bursts",
      story="Number three: the crypto winter of twenty eighteen. In late twenty seventeen, Bitcoin reached about nineteen thousand seven hundred dollars, in a frenzy of new coins being sold to the public, called I C Os.",
      st=fall(84, "From ~$19,700 · Dec 2017 → Dec 2018"), src="Bitget; NerdWallet (−83%)",
      why_h="A whole year of falling",
      why="Then the bubble burst. Over the following year, Bitcoin lost eighty-four percent of its value. It took about two years to reach a new high."),
 dict(r=2, name="China ban + Mt. Gox", when="2013 – 2015", clip="crypto-05-vault-door.mp4",
      story_h="A ban, then the biggest exchange goes dark",
      story="Number two: twenty thirteen to twenty fifteen. In December twenty thirteen, China's central bank barred banks from handling Bitcoin, and its price halved in about two days, from over twelve hundred dollars to under six hundred.",
      st=fall(85, "From ~$1,100 peak · 2013 → 2015"), src="Bitget; Decrypt; GOBankingRates",
      why_h="850,000 bitcoins: gone",
      why="Then, in February twenty fourteen, Mt. Gox, the exchange that once handled most Bitcoin trading, froze withdrawals. It later revealed that about eight hundred and fifty thousand bitcoins had been lost. Bitcoin's fall reached eighty-five percent."),
 dict(r=1, name="The 2011 crash", when="2011", clip="crypto-04-server-dark.mp4",
      story_h="From $32 to one cent",
      story="And number one: twenty eleven, when Bitcoin was barely two years old. In June, a hacker broke into Mt. Gox, which handled about ninety percent of all Bitcoin trading, and sold stolen coins at any price. On that one exchange, Bitcoin's price crashed from about thirty-two dollars to one cent.",
      st=fall(94, "Across 2011 · from a ~$32 peak"), src="Bitget; Decrypt",
      why_h="The worst fall in Bitcoin's history",
      why="The one-cent price only happened on that one exchange. But over the whole of twenty eleven, Bitcoin lost ninety-four percent of its value. By this rule, it's the worst crash in Bitcoin's history."),
]

scenes = [
 {"type": "broll", "broll": "crypto-01-falling-coin.mp4", "eyebrow": "Crypto crash explained · as of 21 Nov 2026",
  "headline": "Bitcoin is down about half from its high",
  "receipt": "CryptoTicker (CoinGecko data), Nov 2026; Bloomberg",
  "voiceover": "If you're searching crypto crash, here's where things stand. In October twenty twenty-five, Bitcoin hit about one hundred and twenty-six thousand dollars. In mid-November twenty twenty-six, it's trading at roughly half of that. Is that normal? Bitcoin has fallen further before. These are its seven worst crashes, ranked by one simple rule."},
 {"type": "plain", "eyebrow": "How we ranked them", "headline": "How far Bitcoin fell from a peak to its next low",
  "body": "Days or months, each fall counted once. Education, not financial advice. No predictions.",
  "voiceover": "The rule: how far Bitcoin's price fell from a peak to its next low, whether that took two days or a whole year. And each fall is counted only once. This is education, not financial advice, and we won't be making any predictions."},
]
for c in C:
    scenes.append({"type": "rank", "rank": c["r"], "eyebrow": c["when"], "headline": c["name"], "voiceover": f"Number {W[c['r']]}." if c["r"] > 1 else "Number one."})
    scenes.append({"type": "broll", "broll": c["clip"], "rank": c["r"], "eyebrow": c["when"], "headline": c["story_h"],
                   "voiceover": c["story"].replace(f"Number {W[c['r']]}: ", "").replace("And number one: ", "")})
    scenes.append({"type": "point", "rank": c["r"], "name": c["name"], "eyebrow": "Bitcoin's fall", "headline": c["why_h"],
                   "stat": c["st"], "receipt": c["src"], "voiceover": c["why"]})

scenes += [
 {"type": "chart", "eyebrow": "Bitcoin's fall, peak to low (%) · *still open, as of 21 Nov 2026", "headline": "Seven crashes, one rule",
  "chart": {"kind": "bar", "labels": ["2020", "2021", "2025–26*", "2022", "2018", "2013–15", "2011"],
            "values": [50, 53, 53.5, 77, 84, 85, 94], "display": ["50", "53", "53.5", "77", "84", "85", "94"], "highlight": [6]},
  "voiceover": "Here they are side by side. The crash happening now is the biggest ever in dollars, but by percentage, four earlier crashes were deeper."},
 {"type": "broll", "broll": "crypto-06-hourglass.mp4", "eyebrow": "Red flag 1", "headline": "A promise of fixed value",
  "receipt": "Yahoo Finance (UST fell to $0.12, May 2022)",
  "voiceover": "So what can we learn, without predicting anything? Red flag one: a promise that something can't lose value. UST was meant to stay at one dollar. It fell to twelve cents."},
 {"type": "broll", "broll": "crypto-08-glass-tower.mp4", "eyebrow": "Red flag 2", "headline": "Not knowing who holds your coins",
  "receipt": "Mt. Gox (2014); FTX (2022)",
  "voiceover": "Red flag two: not knowing who actually holds your coins. When Mt. Gox and FTX failed, people who kept coins there were stuck."},
 {"type": "broll", "broll": "crypto-09-coin-dominoes.mp4", "eyebrow": "Red flags 3 & 4", "headline": "Frozen withdrawals. Borrowed money.",
  "receipt": "Mt. Gox froze withdrawals (Feb 2014); CoinGlass ($19bn liquidated, 10 Oct 2025)",
  "voiceover": "Red flag three: withdrawals being frozen. That's how the Mt. Gox collapse began. And red flag four: borrowed money. On the tenth of October twenty twenty-five, about nineteen billion dollars of borrowed bets were wiped out in a day."},
 {"type": "broll", "broll": "crypto-12-dawn-city.mp4", "eyebrow": "Is Bitcoin history repeating?", "headline": "History, not a forecast",
  "receipt": "Axios, Feb 2026",
  "voiceover": "And is Bitcoin history repeating? Three earlier cycles each saw Bitcoin fall roughly eighty percent before reaching new highs. That's history, not a forecast. Nobody knows what happens next, and anyone who says they do is guessing."},
 {"type": "plain", "eyebrow": "Your turn", "headline": "Which crash surprised you most?",
  "body": "Education, not financial advice. We can't answer \"should I buy?\" questions.",
  "voiceover": "Which crash surprised you most? Tell us in the comments. This is education, not financial advice, so we can't answer should-I-buy questions. All our sources are in the description."},
]
for s in scenes:
    s["duration"] = est(s["voiceover"])

EMMA = {"engine": "kokoro", "name": "bf_emma", "speed": 1.05, "lang": "en-gb", "lead_pad": 400, "tail_pad": 900}
base = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
        "voice": EMMA, "timing": {"lead_in": 900}}

SOURCES = """Sources (figures as of 21 November 2026):
Ranking rule: Bitcoin's fall from a peak to its next low, each fall counted once.
7 Black Thursday, Mar 2020 (~50% in two days): GOBankingRates, "7 of the Biggest Bitcoin Crashes in History"; Banxa.
6 May 2021 (−53% from ~$64,000; nearly $1 trillion lost across crypto in a week): GOBankingRates; Fortune (CoinGecko data).
5 2025–26 (still open; ~$126,000 in Oct 2025 to ~$60,000 on 6 Feb 2026 (Bloomberg) and a $58,570 low on 1 Jul 2026 (CryptoTicker, CoinGecko data)): the 10 Oct 2025 record ~$19bn liquidations come from CoinGlass via Decrypt/Cointelegraph. "Largest dollar drawdown" is a claim by Bitcoin Magazine.
4 2021–22 (−77%, Bitget; −74%, NerdWallet): Terra UST to $0.12 and ~$40bn wiped (Yahoo Finance); Celsius/3AC and FTX realized losses (Chainalysis); FTX $8bn shortfall (CoinMarketCap, Blockworks).
3 2017–18 (−84% from ~$19,700, Bitget; −83%, NerdWallet).
2 2013–15 (−85% from ~$1,100, Bitget): China bank ban, Dec 2013 (Decrypt; GOBankingRates); Mt. Gox froze withdrawals in Feb 2014 and lost ~850,000 BTC (Coinpedia; Cointelegraph).
1 2011 (−94% from $32, Bitget): Mt. Gox flash crash to $0.01 on that exchange, which handled ~90% of trading (Decrypt).
"Three earlier cycles ~80%": Axios, 5 Feb 2026."""

long = dict(base, slug="crypto-crash-explained", countdown={"from": 7},
 disclaimer="Education, not financial advice. No predictions. Figures as of 21 Nov 2026.",
 thumbnail={"big": "BITCOIN −94%", "line": "7 <em>worst</em> crashes", "frame": 0},
 scenes=scenes,
 endcard={"title": "History, <em>not a forecast</em>", "subtitle": "Subscribe for money, explained.",
          "handle": "@MzansiMoneyMatters", "duration": 15000},
 youtube={"title": "Crypto Crash Explained: Bitcoin's 7 Worst Crashes Ever", "privacy": "private",
  "synthetic_media": True, "category_id": "27",
  "tags": ["crypto crash", "crypto crash explained", "bitcoin crash", "bitcoin history", "bitcoin crash history", "crypto crash today",
           "Mt Gox", "FTX collapse", "Terra Luna crash", "crypto winter", "Mzansi Money Matters"],
  "description": ("Crypto crash explained: Bitcoin's 7 worst crashes in history, ranked by one rule (how far Bitcoin fell from a peak to its next low), "
   "from the 2011 Mt. Gox crash to the 2025–26 crash that's still going. Plus four red flags every crypto user should know.\n\n{chapters}\n\n" + SOURCES +
   "\n\n#CryptoCrash #Bitcoin #BitcoinHistory #MzansiMoneyMatters\n\nEducation, not financial advice. No price predictions. "
   "Narration is AI-generated. Video clips were generated with Google Flow (Veo).")})

q = [
 {"type": "broll", "broll": "crypto-04-server-dark.mp4", "eyebrow": "Bitcoin history · June 2011", "headline": "Bitcoin was worth about $32.",
  "voiceover": "In June twenty eleven, one Bitcoin was worth about thirty-two dollars."},
 {"type": "broll", "broll": "crypto-05-vault-door.mp4", "eyebrow": "Mt. Gox", "headline": "Then a hacker hit the biggest exchange.",
  "voiceover": "Then a hacker broke into Mt. Gox, which handled about ninety percent of all Bitcoin trading."},
 {"type": "point", "eyebrow": "On that one exchange", "headline": "Bitcoin's price hit one cent",
  "stat": {"value": "$0.01", "label": "Mt. Gox, June 2011", "count": {"from": 32, "to": 0.01, "decimals": 2, "prefix": "$", "suffix": ""}},
  "receipt": "Decrypt",
  "voiceover": "The stolen coins were dumped, and on that exchange the price crashed to one cent."},
 {"type": "point", "eyebrow": "Across 2011", "headline": "Bitcoin fell 94%",
  "stat": fall(94, "From a ~$32 peak"), "receipt": "Bitget",
  "voiceover": "Across that year, Bitcoin fell ninety-four percent. It's still the worst crash in its history."},
 {"type": "plain", "eyebrow": "Crypto crash explained", "headline": "All 7 worst crashes on the channel",
  "voiceover": "We ranked Bitcoin's seven worst crashes, including the one happening now. Full video on our channel."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-bitcoin-one-cent", size=[1080, 1920], countdown={"from": 7}, broll_fit="pad",
 disclaimer="Education, not financial advice.", voice=dict(EMMA, lead_pad=300, tail_pad=600), timing={"lead_in": 600}, scenes=q,
 endcard={"title": "Bitcoin fell to <em>1 cent</em>?", "subtitle": "7 worst crashes, sources included",
          "handle": "@MzansiMoneyMatters", "voiceover": "Watch the full countdown on Mzansi Money Matters.", "duration": 3500},
 youtube={"title": "Bitcoin fell to 1 cent? #shorts", "privacy": "private", "synthetic_media": True, "category_id": "27",
  "tags": ["bitcoin history", "bitcoin crash", "Mt Gox", "crypto crash", "Mzansi Money Matters"],
  "description": "In June 2011, a hack at Mt. Gox (about 90% of Bitcoin trading) sent Bitcoin's price on that exchange from about $32 to one cent (Decrypt). Across 2011, Bitcoin fell 94% (Bitget). Full countdown of Bitcoin's 7 worst crashes on Mzansi Money Matters.\n\n#BitcoinHistory #CryptoCrash #Shorts\n\nEducation, not financial advice. Narration is AI-generated. Clips generated with Google Flow (Veo)."})

json.dump(long, open("content-crypto.json", "w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-crypto.json", "w"), ensure_ascii=False, indent=2)
for n, d in (("long", long), ("short", short)):
    print(n, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"]) / 60000))
