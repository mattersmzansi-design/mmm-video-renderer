"""Builds content-fastipo.json (long) and content-short-fastipo.json (Short):
"10 Companies That Went Public Fastest — and What Happened Next", per the LLM-council verdict (13 Nov 2026).
Rule: months from legal registration (incorporation) to first trading day of a traditional IPO on a major exchange.
SPACs and OTC boards excluded. "Fastest we could verify." Fate tags as of Nov 2026, only where a source supports them.
Every item shows a SOURCE receipt on screen; full links in the YouTube description.
"""
import json

def est(vo):
    return int(len(vo.split()) / 155 * 60000) + 1300

W = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

# r, name, country, sector, months (number), months_label, registered, ipo, receipt, story_vo, fate_tag, fate_head, fate_vo
C = [
 dict(r=10, name="PDD (Pinduoduo)", country="China", sector="E-commerce", m=34, ml="~34",
      reg="2015", ipo="26 Jul 2018",
      receipt="Founded 2015 → Nasdaq IPO 26 Jul 2018 · DealStreetAsia; Global Venturing",
      vo="Number ten. P D D, better known as Pinduoduo, from China. It's an online shopping platform built on group buying, and today it owns Temu. Founded in twenty fifteen, it listed on Nasdaq in July twenty eighteen, raising one point six billion dollars, about three years after it started.",
      tag="ALIVE", fh="Still listed, and now the owner of Temu",
      fvo="Unlike some on this list, it's still very much alive."),
 dict(r=9, name="Qutoutiao", country="China", sector="Mobile news app", m=27, ml="~27",
      reg="Jun 2016", ipo="14 Sep 2018",
      receipt="Founded Jun 2016 → Nasdaq IPO 14 Sep 2018 · Caixin; Renaissance Capital",
      vo="Number nine. Qutoutiao, a Chinese news app whose name means fun headlines. Founded in June twenty sixteen, it listed on Nasdaq in September twenty eighteen, about twenty-seven months later, and its shares more than doubled on day one.",
      tag="LEFT NASDAQ", fh="Agreed to leave Nasdaq in 2023",
      fvo="But the early excitement didn't last. In twenty twenty-three, it agreed to leave Nasdaq."),
 dict(r=8, name="Luckin Coffee", country="China", sector="Coffee chain", m=23, ml="~23",
      reg="Jun 2017", ipo="17 May 2019",
      receipt="Cayman holding co. registered Jun 2017 → Nasdaq IPO 17 May 2019 · Luckin SEC filings; TechCrunch",
      vo="Number eight. Luckin Coffee, a Chinese coffee chain built for app ordering and pickup. Its holding company was registered in June twenty seventeen, and it listed on Nasdaq in May twenty nineteen, raising about six hundred and fifty million dollars.",
      tag="FRAUD · DELISTED 2020", fh="Fabricated sales, then removed from Nasdaq",
      fvo="Then, in April twenty twenty, the company itself announced that some of its sales had been fabricated. Trading was halted, and it was removed from Nasdaq. The coffee shops kept running in China, but the listing didn't survive."),
 dict(r=7, name="Priceline", country="USA", sector="Online travel", m=20, ml="~20*",
      reg="Jul 1997*", ipo="30 Mar 1999",
      receipt="Incorporated 1997* → Nasdaq IPO 30 Mar 1999 · Encyclopedia.com; Benzinga  (*sources differ on 1996–97)",
      vo="Number seven. Priceline, the American name-your-own-price travel site. Incorporated in nineteen ninety-seven, it listed in March nineteen ninety-nine. On its first day, it was valued at around ten billion dollars.",
      tag="ALIVE", fh="Today it's part of Booking Holdings",
      fvo="It survived the dot-com crash, and today it's part of Booking Holdings, the company behind Booking dot com."),
 dict(r=6, name="Sycamore Networks", country="USA", sector="Telecom equipment", m=20, ml="20",
      reg="17 Feb 1998", ipo="21 Oct 1999",
      receipt="Incorporated 17 Feb 1998 → Nasdaq IPO 21 Oct 1999 · Sycamore SEC 10-K",
      vo="Number six. Sycamore Networks, an American maker of fibre-optic network equipment. Incorporated in February nineteen ninety-eight, it listed twenty months later, in October nineteen ninety-nine, with just a few products and one customer. Its shares almost quintupled on day one.",
      tag="WOUND DOWN 2013", fh="Sold its business and dissolved",
      fvo="When the telecom boom ended, so did its growth. In twenty thirteen, it sold its business and dissolved."),
 dict(r=5, name="Netscape", country="USA", sector="Web browser", m=16, ml="16",
      reg="4 Apr 1994", ipo="9 Aug 1995",
      receipt="Founded 4 Apr 1994 → Nasdaq IPO 9 Aug 1995 · Britannica; Wikipedia",
      vo="Number five. Netscape, the company whose web browser brought the internet to millions. Founded in April nineteen ninety-four, it went public just sixteen months later, in August nineteen ninety-five, without ever having made a profit.",
      tag="ACQUIRED 1998", fh="The IPO that started the dot-com rush",
      fvo="Its stock doubled on day one, and that moment kicked off the dot-com boom. In nineteen ninety-eight, it was bought by AOL."),
 dict(r=4, name="Akamai", country="USA", sector="Internet infrastructure", m=14, ml="~14",
      reg="20 Aug 1998", ipo="29 Oct 1999",
      receipt="Incorporated 20 Aug 1998 → Nasdaq IPO 29 Oct 1999 · Akamai company history; Encyclopedia.com",
      vo="Number four. Akamai, from the United States. It runs the networks of servers that make websites load faster around the world. Incorporated in August nineteen ninety-eight, it listed about fourteen months later.",
      tag="ALIVE", fh="Still a major internet company today",
      fvo="It survived the crash, and it's still a major internet company today."),
 dict(r=3, name="Yahoo", country="USA", sector="Internet portal", m=13, ml="~13",
      reg="2 Mar 1995", ipo="12 Apr 1996",
      receipt="Incorporated 2 Mar 1995 → Nasdaq IPO 12 Apr 1996 · History of Yahoo (Wikipedia); Entrepreneur",
      vo="Number three. Yahoo. It started as two Stanford students' list of websites, but the company was only registered in March nineteen ninety-five. Just over thirteen months later, in April nineteen ninety-six, it went public.",
      tag="ACQUIRED 2017", fh="Sold to Verizon for about $4.5 billion",
      fvo="Yahoo became one of the biggest names on the internet. In twenty seventeen, its main business was sold to Verizon for about four and a half billion dollars."),
 dict(r=2, name="Pets.com", country="USA", sector="Online pet supplies", m=12, ml="~12",
      reg="Feb 1999", ipo="Feb 2000",
      receipt="Incorporated Feb 1999 → Nasdaq IPO Feb 2000 · Wikipedia (Pets.com S-1); Business Insider",
      vo="Number two. Pets dot com, an American online pet shop famous for its sock-puppet mascot. Incorporated in February nineteen ninety-nine, it listed on Nasdaq exactly a year later.",
      tag="COLLAPSED", fh="Liquidated 268 days after its IPO",
      fvo="It lost money on almost every sale. Two hundred and sixty-eight days after its IPO, it shut down, and its shares, sold at eleven dollars, were worth nineteen cents."),
 dict(r=1, name="Lycos", country="USA", sector="Internet search", m=10, ml="~10",
      reg="Jun 1995", ipo="2 Apr 1996",
      receipt="Incorporated Jun 1995 → Nasdaq IPO 2 Apr 1996 · Lycos SEC 10-Q (1996); Encyclopedia.com",
      vo="And number one. Lycos, an American search engine that began as a Carnegie Mellon University project. The company was incorporated in June nineteen ninety-five, and it went public in April nineteen ninety-six, just ten months later, then the youngest company ever to list on Nasdaq.",
      tag="ACQUIRED 2000", fh="Sold to Terra Networks for $12.5 billion",
      fvo="Four years later, in twenty hundred, Lycos was bought by Spain's Terra Networks in a twelve and a half billion dollar deal."),
]

def months_stat(c):
    return {"value": c["ml"].replace("*", "") + " mo", "label": f"Registered {c['reg'].replace('*','')} → first trading day {c['ipo']}",
            "count": {"from": 0, "to": c["m"], "decimals": 0, "prefix": "~" if "~" in c["ml"] else "", "suffix": " mo"}}

scenes = [
 {"type": "intro", "eyebrow": "Startup → stock market", "headline": "10 companies that went public fastest",
  "body": "And what happened to them next.",
  "voiceover": "Most companies take ten years or more to reach the stock market. These ten did it in months. But speed didn't always mean success."},
 {"type": "plain", "eyebrow": "First, what's an IPO?", "headline": "IPO: the first time a company sells shares to the public",
  "body": "An initial public offering, on a stock exchange.",
  "voiceover": "First, a quick definition. An I P O, or initial public offering, is the first time a company sells its shares to the public on a stock exchange."},
 {"type": "plain", "eyebrow": "How we counted", "headline": "From legal registration to its first day of trading",
  "body": "Traditional IPOs on major exchanges only. No SPACs or over-the-counter listings. The fastest we could verify, as of November 2026.",
  "voiceover": "Here's how we counted: from the day each company was legally registered to its first day of trading on a major stock exchange. These are the fastest we could verify, and every one has its source on screen."},
]
for c in C:
    scenes.append({"type": "rank", "rank": c["r"], "eyebrow": f"{c['country']} · {c['sector']}", "headline": c["name"],
                   "voiceover": f"Number {W[c['r']]}."})
    scenes.append({"type": "point", "rank": c["r"], "name": c["name"], "eyebrow": "Registration to IPO",
                   "headline": f"{c['country']} · {c['sector']}", "stat": months_stat(c), "receipt": c["receipt"],
                   "voiceover": c["vo"].split(". ", 1)[1] if c["vo"].startswith("Number") or c["vo"].startswith("And number") else c["vo"]})
    scenes.append({"type": "point", "rank": c["r"], "name": c["name"], "eyebrow": "What happened next", "tag": c["tag"] + " (as of Nov 2026)",
                   "headline": c["fh"], "receipt": c["receipt"].split(" · ", 1)[1], "voiceover": c["fvo"]})
scenes += [
 {"type": "chart", "eyebrow": "Months from registration to IPO", "headline": "Speed didn't predict survival",
  "chart": {"kind": "bar", "labels": ["Lycos", "Pets.com", "Yahoo", "Akamai", "Netscape", "Sycamore", "Priceline", "Luckin", "Qutoutiao", "PDD"],
            "values": [10, 12, 13, 14, 16, 20, 20, 23, 27, 34], "display": ["10", "12", "13", "14", "16", "20", "20", "23", "27", "34"],
            "highlight": [1]},
  "voiceover": "Look at the pattern. Seven of the ten listed during America's nineteen nineties internet boom, and three during China's tech boom of twenty eighteen and nineteen. Some became giants. Others collapsed within a year or two. Going public fast told investors very little about who would survive."},
 {"type": "plain", "eyebrow": "And South Africa?", "headline": "No South African company made this list",
  "body": "Three questions to ask about any hyped new listing: How old is it? What does it earn? Who is selling shares at the IPO?",
  "voiceover": "No South African company made this list. But if you ever hear hype about a brand-new listing, ask three questions. How old is the business? What does it actually earn? And who's selling their shares at the I P O? This is education, not financial advice."},
 {"type": "plain", "eyebrow": "Your turn", "headline": "Which of these surprised you most?",
  "voiceover": "Which one surprised you most? Tell us in the comments. All our sources are in the description."},
]
# fix voiceover lead-ins: rank card already says "Number X."
for s in scenes:
    s["voiceover"] = s["voiceover"].replace("And number one. ", "")
    s["duration"] = est(s["voiceover"])

base = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
        "voice": {"name": "en-US-BrianMultilingualNeural", "rate": "+4%", "pitch": "+0Hz", "lead_pad": 400, "tail_pad": 900},
        "timing": {"lead_in": 900}}

SOURCES = """Sources (as of November 2026):
10 PDD — DealStreetAsia, "Pinduoduo: From Zero to $23B in Three Years"; Global Venturing (Tencent-backed IPOs)
9 Qutoutiao — Caixin Global (founded June 2016); Renaissance Capital (IPO 13–14 Sep 2018); Wikipedia (agreed to leave Nasdaq, 2023)
8 Luckin Coffee — TechNode; TechCrunch (May 2019 IPO, ~$651m); Luckin Form 6-K, 2 Apr 2020 (fabricated transactions); trading suspended 29 Jun 2020
7 Priceline — Encyclopedia.com; Benzinga "This Day in Market History" (IPO 30 Mar 1999); sources differ on 1996–97 incorporation
6 Sycamore Networks — SEC Form 10-K (incorporated 17 Feb 1998; IPO 21 Oct 1999); SEC Form 8-K/10-Q 2013 (asset sale and dissolution)
5 Netscape — Britannica; Wikipedia (founded 4 Apr 1994; IPO 9 Aug 1995); The 1995 Blog (AOL acquisition)
4 Akamai — Wikipedia (incorporated 20 Aug 1998; Nasdaq from 29 Oct 1999); Encyclopedia.com
3 Yahoo — History of Yahoo, Wikipedia (incorporated 2 Mar 1995; IPO 12 Apr 1996; sold to Verizon 2017 for $4.48bn)
2 Pets.com — Wikipedia (incorporated Feb 1999; IPO Feb 2000; liquidated Nov 2000); Business Insider
1 Lycos — Lycos SEC Form 10-Q, 1996 (incorporated June 1995); Encyclopedia.com (IPO April 1996, youngest Nasdaq listing); CNN (Terra deal, $12.5bn)
Excluded: SPAC mergers; OTC listings (e.g. UCAR on China's NEEQ board)."""

long = dict(base, slug="top10-fastest-ipos", countdown={"from": 10},
 disclaimer="Education, not financial advice. Status as of Nov 2026.",
 thumbnail={"kicker": "Startup → stock market", "big": "10 MONTHS", "line": "Who <em>survived</em>?", "photo": "stock exchange trading screen"},
 scenes=scenes,
 endcard={"title": "Speed isn't <em>success</em>", "subtitle": "Subscribe for South African money, explained.",
          "handle": "@MzansiMoneyMatters", "duration": 5000},
 youtube={"title": "10 Companies That Went Public Fastest — and What Happened Next", "privacy": "private",
  "synthetic_media": True, "category_id": "27",
  "tags": ["IPO", "fastest IPO", "Lycos", "Pets.com", "Yahoo", "Netscape", "Luckin Coffee", "Pinduoduo", "Mzansi Money Matters"],
  "description": ("From registration to the stock market in months: the 10 fastest IPOs we could verify, their country and sector, "
   "and what happened to each one next.\n\nHow we counted: months from legal registration (incorporation) to the first day of "
   "trading in a traditional IPO on a major exchange.\n\n{chapters}\n\n" + SOURCES +
   "\n\nEducation, not financial advice. Narration and some visuals are AI-generated. Stock footage from Pexels.")})

q = [
 {"type": "broll", "broll": "stock exchange trading screen", "eyebrow": "Startup → stock market", "headline": "Most companies take decades",
  "voiceover": "Most companies take decades to reach the stock market."},
 {"type": "point", "eyebrow": "One of them took", "headline": "Less than a year",
  "stat": {"value": "~10 mo", "label": "From registration to IPO", "count": {"from": 0, "to": 10, "decimals": 0, "prefix": "~", "suffix": " mo"}},
  "voiceover": "One did it in less than a year."},
 {"type": "plain", "eyebrow": "And the others?", "headline": "Some became giants. One was gone within a year.",
  "voiceover": "Some of the fastest became giants. One was gone within a year of listing. And one faked its sales."},
 {"type": "plain", "eyebrow": "Every claim. Every source.", "headline": "The full top 10 is on the channel",
  "voiceover": "Who were they? The full top ten, with every source, is on our channel."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-fastest-ipos", size=[1080, 1920], countdown={"from": 10},
 disclaimer="Education, not financial advice.",
 voice={"name": "en-US-BrianMultilingualNeural", "rate": "+6%", "pitch": "+0Hz", "lead_pad": 300, "tail_pad": 600},
 timing={"lead_in": 600}, scenes=q,
 endcard={"title": "Who <em>survived</em>?", "subtitle": "10 fastest IPOs, sources included",
          "handle": "@MzansiMoneyMatters", "voiceover": "Watch the full top ten on Mzansi Money Matters.", "duration": 3500},
 youtube={"title": "From startup to stock market in under a year #shorts", "privacy": "private", "synthetic_media": True,
  "category_id": "27", "tags": ["IPO", "stock market", "startups", "Mzansi Money Matters"],
  "description": "Most companies take decades to go public. One did it in about 10 months. Full top 10 with sources on Mzansi Money Matters.\n\nEducation, not financial advice. Narration is AI-generated. Stock footage from Pexels."})

json.dump(long, open("content-fastipo.json", "w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-fastipo.json", "w"), ensure_ascii=False, indent=2)
for n, d in (("long", long), ("short", short)):
    print(n, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"]) / 60000))
