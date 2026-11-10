"""Builds content-money.json (long) and content-short-money.json (Short):
the evolution of money in nine stages, barter to digital currencies.
Also writes out/money-script.md (the narration as a readable script).
"""
import json, os

def est(vo):
    return int(len(vo.split()) / 155 * 60000) + 1300

W = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# each stage: rank card + list of scenes (type, eyebrow, headline, body/stat, voiceover)
STAGES = [
 (1, "Before money", "Barter and favours", [
   dict(type="point", eyebrow="The problem", headline="You need someone who wants what you have",
        body="Economists call it the double coincidence of wants.",
        vo="Imagine you have a goat and you need shoes. You'd have to find a shoemaker who also happens to want a goat, today. Economists call this the double coincidence of wants, and it's the problem money was invented to solve."),
   dict(type="point", eyebrow="What really happened", headline="Most early communities ran on trust and IOUs",
        body="Anthropologists have found few pure barter economies. Neighbours kept track of who owed whom.",
        vo="But here's a twist. Anthropologists have found very few societies that ran purely on barter. In most villages, people gave each other things and kept track of who owed whom. Money began as a way of keeping score."),
 ]),
 (2, "c. 3000 BC onwards", "Commodity money", [
   dict(type="broll", broll="cattle herd", eyebrow="Things everyone valued", headline="Cattle, grain, salt and shells",
        vo="The first money was made of things everyone already valued: cattle, grain, salt, and shells. Cowrie shells were used as money across Africa and Asia for thousands of years."),
   dict(type="point", eyebrow="Mesopotamia", headline="The shekel: a weight of barley, then silver",
        stat=dict(value="c. 3000 BC", label="Earliest recorded unit of account"),
        vo="In ancient Mesopotamia, around three thousand BC, the shekel was a set weight of barley, and later of silver. Temples recorded debts in shekels on clay tablets. Some of the oldest writing we have is accounting."),
   dict(type="point", eyebrow="Closer to home", headline="Cattle as wealth", body="In many Southern African cultures, cattle were, and still are, a store of wealth.",
        vo="Closer to home, in many Southern African cultures, cattle were the main store of wealth, and they still carry that meaning today, in lobola."),
 ]),
 (3, "c. 600 BC", "Coins", [
   dict(type="point", eyebrow="Lydia, modern-day Turkey", headline="The first official coins",
        stat=dict(value="c. 600 BC", label="Lydian electrum coins"),
        vo="Around six hundred BC, the kingdom of Lydia, in today's Turkey, stamped lumps of electrum, a mix of gold and silver, with a royal seal. These were among the first official coins. The stamp meant you didn't have to weigh the metal. The king guaranteed it."),
   dict(type="broll", broll="ancient coins", eyebrow="Why coins won", headline="Small, durable, countable, trusted",
        vo="At about the same time, China was using bronze coins shaped like tools. Coins spread because they were small, durable, easy to count, and backed by someone people trusted."),
 ]),
 (4, "c. 1024", "Paper money", [
   dict(type="point", eyebrow="China", headline="From flying money to the first government banknotes",
        stat=dict(value="1024", label="Song dynasty jiaozi, Sichuan"),
        vo="Coins are heavy. In China, merchants began using paper receipts called flying money, and in ten twenty-four, the Song dynasty issued the first government paper money, the jiaozi."),
   dict(type="point", eyebrow="The first warning", headline="Easy to print. Easy to over-print.",
        body="Later Chinese dynasties printed too much, and the notes lost their value.",
        vo="Paper had a new danger. It's easy to print, and later Chinese governments printed too much of it. Prices soared and the notes lost their value, a story we covered in our video on currency collapses."),
 ]),
 (5, "1600s", "Banks and banknotes", [
   dict(type="point", eyebrow="Goldsmiths and bankers", headline="A receipt for your gold becomes money",
        vo="In Europe, merchants left their gold with goldsmiths and bankers for safekeeping, and got a paper receipt. Soon people traded the receipts themselves, because they were easier to carry than gold."),
   dict(type="point", eyebrow="Sweden", headline="Europe's first banknotes",
        stat=dict(value="1661", label="Stockholms Banco banknotes"),
        vo="In sixteen sixty-one, Stockholms Banco in Sweden issued Europe's first banknotes. It printed more notes than it could back, and within a few years it collapsed."),
 ]),
 (6, "1668 onwards", "Central banks", [
   dict(type="point", eyebrow="Learning from failure", headline="The Riksbank: the world's oldest central bank",
        stat=dict(value="1668", label="Sveriges Riksbank founded"),
        vo="That collapse led Sweden to create the Riksbank in sixteen sixty-eight, the oldest central bank still operating. England followed with the Bank of England in sixteen ninety-four, set up to lend the government money for war."),
   dict(type="point", eyebrow="South Africa", headline="The South African Reserve Bank",
        stat=dict(value="1921", label="SARB founded"),
        vo="The United States created the Federal Reserve in nineteen thirteen, and the South African Reserve Bank opened in nineteen twenty-one. Today it alone issues our banknotes and coins."),
   dict(type="plain", eyebrow="What a central bank does", headline="Issues the currency. Sets interest rates. Rescues the system.",
        body="Its main job: keep prices stable, so your rand holds its value.",
        vo="Central banks do three big things. They issue the currency, they set interest rates, like the repo rate, and they act as lender of last resort when banks get into trouble. Their main job is to keep prices stable, so your money holds its value."),
 ]),
 (7, "1870s–1971", "The gold standard, briefly", [
   dict(type="broll", broll="gold bars", eyebrow="Backed by gold", headline="Notes you could swap for gold",
        vo="For about a century, many currencies were tied to gold. In theory, you could swap your notes for a fixed amount of it. Gold mined right here in South Africa helped keep that system running."),
   dict(type="point", eyebrow="The end", headline="1971: the dollar cuts its link to gold",
        stat=dict(value="1971", label="End of dollar convertibility to gold"),
        vo="But the link was hard to keep. In nineteen seventy-one, the United States stopped swapping dollars for gold, and the world moved to fiat money: money that's valuable because governments declare it so, and people trust it."),
 ]),
 (8, "1950 onwards", "Cards and electronic money", [
   dict(type="broll", broll="credit card payment", eyebrow="Plastic", headline="Cards, ATMs and electronic transfers",
        vo="In nineteen fifty, Diners Club launched one of the first charge cards. The first cash machine opened in London in nineteen sixty-seven. Money slowly became numbers in a bank's computer."),
   dict(type="point", eyebrow="Africa leads", headline="M-Pesa: money on a basic phone",
        stat=dict(value="2007", label="M-Pesa launched in Kenya"),
        vo="Africa leapfrogged. In two thousand and seven, Kenya's M-Pesa let people send money by text message, without a bank account. And in South Africa, PayShap now lets you pay instantly using just a phone number."),
 ]),
 (9, "2009 onwards", "Digital currencies", [
   dict(type="broll", broll="bitcoin", eyebrow="Bitcoin", headline="Money with no central bank",
        stat=dict(value="2009", label="Bitcoin network launched"),
        vo="In two thousand and nine, someone using the name Satoshi Nakamoto launched Bitcoin, digital money with no central bank and a fixed supply, recorded on a public ledger called a blockchain. Thousands of cryptocurrencies followed, along with stablecoins tied to the dollar."),
   dict(type="point", eyebrow="Central banks respond", headline="Digital versions of national money",
        body="The Bahamas' Sand Dollar (2020), Nigeria's eNaira (2021), China's e-CNY pilots, and the SARB's Project Khokha trials.",
        vo="Central banks are responding with digital versions of their own money. The Bahamas launched the Sand Dollar in twenty twenty, Nigeria launched the eNaira in twenty twenty-one, and China is piloting a digital yuan. Our own Reserve Bank has tested the technology through Project Khokha."),
 ]),
]

scenes = [
 {"type": "intro", "eyebrow": "From goats to Bitcoin", "headline": "The evolution of money, in 9 stages",
  "body": "Barter. Shells. Coins. Paper. Banks. Cards. Crypto.",
  "voiceover": "The note in your wallet is just paper. So why will a shop give you bread for it? To answer that, we need to go back more than five thousand years."},
]
for r, era, title, items in STAGES:
    scenes.append({"type": "rank", "rank": r, "eyebrow": era, "headline": title,
                   "voiceover": f"Stage {W[r]}. {title.replace(', briefly','')}."})
    for it in items:
        s = {"type": it["type"], "eyebrow": it["eyebrow"], "headline": it["headline"], "voiceover": it["vo"]}
        if it["type"] == "point": s.update(rank=r, name=title.replace(", briefly", ""))
        if it.get("body"): s["body"] = it["body"]
        if it.get("stat"): s["stat"] = it["stat"]
        if it.get("broll"): s["broll"] = it["broll"]
        scenes.append(s)
scenes += [
 {"type": "plain", "eyebrow": "The common thread", "headline": "Money has always been about trust.",
  "voiceover": "Cattle, shells, coins, paper, plastic, code. The form keeps changing, but the idea doesn't. Money works because we trust that someone else will accept it tomorrow. When that trust breaks, money fails."},
 {"type": "plain", "eyebrow": "Your turn", "headline": "Will cash still exist in 20 years?",
  "voiceover": "So what's next? Will you still carry cash in twenty years? Tell us in the comments."},
]
for s in scenes:
    s["duration"] = est(s["voiceover"])

base = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
        "voice": {"name": "en-US-BrianMultilingualNeural", "rate": "+4%", "pitch": "+0Hz", "lead_pad": 400, "tail_pad": 900},
        "timing": {"lead_in": 900}}

long = dict(base, thumbnail={"kicker": "9 stages", "big": "5,000", "line": "years of <em>money</em>", "photo": "ancient coins"}, slug="evolution-of-money", countdown={"from": 9, "order": "up"},
 disclaimer="Education, not financial advice.", scenes=scenes,
 endcard={"title": "Money is <em>trust</em>", "subtitle": "Subscribe for South African money, explained.",
          "handle": "@MzansiMoneyMatters", "duration": 5000},
 youtube={"title": "The Evolution of Money: From Goats to Bitcoin in 9 Stages", "privacy": "private",
  "synthetic_media": True, "category_id": "27",
  "tags": ["history of money", "evolution of money", "central banks", "SARB", "Bitcoin", "CBDC", "Mzansi Money Matters"],
  "description": ("How money evolved, from barter and cattle to coins, paper, banks, central banks, cards and digital currencies, "
   "and why it all comes down to trust.\n\n{chapters}\n\n"
   "Education, not financial advice. Narration and some visuals are AI-generated. Stock footage from Pexels.")})

q = [
 {"type": "broll", "broll": "cattle herd", "eyebrow": "5,000 years of money", "headline": "From cows to crypto in 45 seconds",
  "voiceover": "Five thousand years of money, in forty-five seconds."},
 {"type": "point", "rank": 2, "name": "Commodity money", "eyebrow": "First", "headline": "Cattle, grain, salt and shells",
  "voiceover": "First, money was things everyone valued: cattle, grain, salt and shells."},
 {"type": "point", "rank": 3, "name": "Coins", "eyebrow": "Then", "headline": "Coins, stamped by a king",
  "stat": {"value": "600 BC", "label": "Lydia's first coins"},
  "voiceover": "Around six hundred BC, kings started stamping metal coins."},
 {"type": "point", "rank": 4, "name": "Paper", "eyebrow": "Then", "headline": "Paper money, invented in China",
  "stat": {"value": "1024", "label": "Song dynasty jiaozi"},
  "voiceover": "China invented government paper money in ten twenty-four."},
 {"type": "point", "rank": 6, "name": "Central banks", "eyebrow": "Then", "headline": "Central banks, to keep it all stable",
  "stat": {"value": "1668", "label": "Sweden's Riksbank"},
  "voiceover": "Then came central banks, starting with Sweden's in sixteen sixty-eight."},
 {"type": "broll", "broll": "credit card payment", "eyebrow": "Then", "headline": "Cards, phones, and now code",
  "voiceover": "Then cards, phones, and now Bitcoin and digital currencies."},
 {"type": "plain", "eyebrow": "The secret", "headline": "Every form of money runs on one thing: trust.",
  "voiceover": "The form keeps changing. But every kind of money runs on one thing: trust."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-evolution-of-money", size=[1080, 1920], countdown={"from": 9, "order": "up"},
 disclaimer="Education, not financial advice.",
 voice={"name": "en-US-BrianMultilingualNeural", "rate": "+6%", "pitch": "+0Hz", "lead_pad": 300, "tail_pad": 600},
 timing={"lead_in": 600}, scenes=q,
 endcard={"title": "All 9 stages on the <em>channel</em>", "subtitle": "The evolution of money",
          "handle": "@MzansiMoneyMatters", "voiceover": "Watch all nine stages on Mzansi Money Matters.", "duration": 3500},
 youtube={"title": "5,000 years of money in 45 seconds #shorts", "privacy": "private", "synthetic_media": True,
  "category_id": "27", "tags": ["history of money", "Bitcoin", "central bank", "Mzansi Money Matters"],
  "description": "From cattle and shells to coins, paper, central banks, cards and crypto. Full video on Mzansi Money Matters.\n\nEducation, not financial advice. Narration is AI-generated. Stock footage from Pexels."})

json.dump(long, open("content-money.json", "w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-money.json", "w"), ensure_ascii=False, indent=2)

# readable script
os.makedirs("out", exist_ok=True)
lines = ["# The Evolution of Money: From Goats to Bitcoin in 9 Stages", "", "*Mzansi Money Matters, narration script*", ""]
for s in scenes:
    if s["type"] == "rank":
        lines += ["", f"## Stage {s['rank']}: {s['headline']} ({s['eyebrow']})", ""]
    else:
        lines += [f"**[{s.get('eyebrow','')}: {s['headline']}]**", "", s["voiceover"], ""]
lines += ["", "---", "", "# Short: 5,000 years of money in 45 seconds", ""]
for s in q:
    lines += [f"**[{s['headline']}]** {s['voiceover']}", ""]
lines.append("*Watch all nine stages on Mzansi Money Matters.*")
open("out/money-script.md", "w").write("\n".join(lines))
for n, d in (("long", long), ("short", short)):
    print(n, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"]) / 60000))
