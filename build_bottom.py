"""Builds content-bottom.json (long video) and content-short-bottom.json (Short):
"Has Bitcoin Hit Bottom? 10 Signals Analysts Watch (Nov 2026)", following the LLM-council verdict of 22 Nov 2026.
Five rounds, each a 'might be' then a 'might not be' signal. No verdict and no dollar scenarios.
Every signal carries a date label and a weakness note. Fear & Greed and Hash Ribbons are counted once (Galaxy's 4-of-13 refers back to them).
Depth figures are cited to Bitget/NerdWallet, not to our own crash video. FAIS-safe disclaimer at the start and end. Scam warning.
Clips: reused crypto-05/06/07/08/10, plus 4 new neutral Flow clips bottom-a..d (balance, magnifier, gauge, checklist).
Narrator: Kokoro bf_emma.
"""
import json

def est(vo):
    return int(len(vo.split()) / 150 * 60000) + 1300

DISC = ("This is general education, not financial advice. Mzansi Money Matters is not an authorised financial services provider. "
        "We make no price predictions and never tell you to buy or sell. Crypto can lose value fast. "
        "Speak to an FSCA-authorised adviser before you decide anything.")

def pt(eyebrow, head, vo, receipt, tag=None, stat=None, rank=None):
    s = {"type": "point", "eyebrow": eyebrow, "headline": head, "receipt": receipt, "voiceover": vo}
    if tag: s["tag"] = tag
    if stat: s["stat"] = stat
    return s

MIGHT = "MIGHT BE THE BOTTOM"
NOT = "MIGHT NOT BE"

scenes = [
 {"type": "broll", "broll": "bottom-a-balance-scale.mp4", "eyebrow": "Bitcoin bottom · as of 19 Nov 2026", "headline": "Nobody knows where the bottom is until after",
  "receipt": "Fortune (BTC $63,747.99, 19 Nov 2026, 6am ET)",
  "voiceover": "Your cousin says Bitcoin has hit bottom and it's time to buy the dip. The honest answer is that nobody knows where the bottom is until after it has passed. Not analysts, not us. On the nineteenth of November twenty twenty-six, Bitcoin was about sixty-three thousand seven hundred dollars, roughly half its October twenty twenty-five high. So we won't guess. We'll look at ten signals analysts watch: what each one measures, when it was recorded, and where it can be wrong."},
 {"type": "plain", "eyebrow": "Before we start", "headline": "Education, not financial advice",
  "body": "MMM is not an authorised financial services provider. No price predictions. Never buy or sell advice. Speak to an FSCA-authorised adviser.",
  "voiceover": DISC},
 {"type": "chart", "eyebrow": "Bitcoin price, US$ · Bloomberg; CoinGecko; Fortune · as of 19 Nov 2026", "headline": "From the peak to now",
  "chart": {"kind": "line", "labels": ["Peak, Oct 25", "6 Feb 26", "Low, 1 Jul 26", "19 Nov 26"],
            "values": [126000, 60000, 58570, 63748], "display": ["~$126k", "~$60k", "$58,570", "$63,748"], "highlight": [3]},
  "voiceover": "Quick recap. About one hundred and twenty-six thousand dollars at the peak. About sixty thousand in February. A low of fifty-eight thousand five hundred and seventy on the first of July. And around sixty-three thousand seven hundred this week. Now, round one."},

 # Round 1: clock vs ruler
 {"type": "broll", "broll": "crypto-06-hourglass.mp4", "eyebrow": "Round 1 · The clock", "tag": MIGHT, "headline": "Past lows came about 60 weeks after the peak",
  "receipt": "Blockworks Research (via KuCoin), ~Jul 2026",
  "voiceover": "Round one: the clock. Blockworks Research found that past bear markets bottomed around sixty weeks after the all-time high. That would put this low at about the end of November twenty twenty-six. The weakness: it's based on only about three past cycles. And if prices keep falling into December, this signal simply runs out."},
 pt("Round 1 · The ruler", "Past bear markets fell further",
    "Now the ruler. Past Bitcoin bear markets fell between seventy-seven and eighty-five percent from their peaks. This one is about fifty to fifty-three and a half percent so far. The weakness: there's no rule that says this cycle must copy the old ones.",
    "Bitget; NerdWallet · past cycles 2014, 2018, 2022", tag=NOT),
 {"type": "chart", "eyebrow": "Bitcoin's fall from peak (%) · Bitget; NerdWallet; CoinGecko", "headline": "Past bear markets vs this one (so far)",
  "chart": {"kind": "bar", "labels": ["2013–15", "2018", "2022", "2025–26 so far"], "values": [85, 84, 77, 53.5],
            "display": ["85", "84", "77", "53.5"], "highlight": [3]},
  "voiceover": "Here's how that looks side by side."},

 # Round 2: cost
 {"type": "broll", "broll": "crypto-05-vault-door.mp4", "eyebrow": "Round 2 · What people paid", "tag": MIGHT, "headline": "The July low landed in one analyst's range",
  "receipt": "CryptoQuant's Julio Moreno via Cointelegraph (late 2025)",
  "voiceover": "Round two: what people paid. The realized price is roughly the average price everyone paid for their Bitcoin. Based on it, CryptoQuant's Julio Moreno said in late twenty twenty-five that the bottom could be between fifty-six and sixty thousand dollars. The July low of fifty-eight thousand five hundred and seventy landed inside that range. But be careful: this is one forecast that happened to land, not proof."},
 pt("Round 2 · What's missing", "Only 4 of 13 bottom signs had appeared",
    "On the other side, Galaxy Research tracked thirteen signs that have appeared at past bottoms. As of the ninth of June, only four had appeared. The strongest ones, like the price falling below what holders paid, and a big wave of panic selling, had not. This is from June, so it's old, but those missing signs matter.",
    "Galaxy Research, published 12 Jun 2026 (data as of 9 Jun 2026)", tag=NOT,
    stat={"value": "4 / 13", "label": "bottom signs present · Galaxy, as of 9 Jun 2026", "count": {"from": 0, "to": 4, "decimals": 0, "prefix": "", "suffix": " / 13"}}),

 # Round 3: mood
 {"type": "broll", "broll": "bottom-c-gauge.mp4", "eyebrow": "Round 3 · The mood", "tag": MIGHT, "headline": "The fear gauge hit a record low of 5",
  "receipt": "Crypto Fear & Greed Index via CoinGabbar (6 Feb 2026; 4 Nov 2026)",
  "stat": {"value": "5", "label": "Fear & Greed, 6 Feb 2026 · record low since 2018", "count": {"from": 50, "to": 5, "decimals": 0, "prefix": "", "suffix": ""}},
  "voiceover": "Round three: the mood. The Crypto Fear and Greed Index scores market mood from zero to one hundred. On the sixth of February it hit five, its lowest reading since tracking began in twenty eighteen. Extreme fear has often come near past lows. It's also one of Galaxy's four signs. But note: by early November it was back at thirty-four. That's ordinary fear, not panic."},
 pt("Round 3 · The bets", "Big bets on, or insurance against, $60k",
    "Meanwhile, on the options exchange Deribit, the most popular contract is one that pays out if Bitcoin falls below sixty thousand dollars. Some traders are betting on a drop. Others are simply buying insurance. Either way, many expect more risk ahead.",
    "CryptoPotato (Deribit data), 16 Nov 2026", tag=NOT),

 # Round 4: miners and big money
 {"type": "broll", "broll": "crypto-07-mining-rigs.mp4", "eyebrow": "Round 4 · The miners", "tag": MIGHT, "headline": "Miners stopped switching machines off",
  "receipt": "Galaxy Research (Hash Ribbons, early Jun 2026); NewsBTC (difficulty cut, 14 Nov 2026)",
  "voiceover": "Round four: the miners. A signal called Hash Ribbons fired in early June. In plain words: after a stretch where miners were switching machines off, they started switching them back on. That has come before past lows. But on the fourteenth of November, the network's mining difficulty was cut, which can mean some miners are under pressure again. So this one cuts both ways."},
 {"type": "broll", "broll": "crypto-08-glass-tower.mp4", "eyebrow": "Round 4 · The big funds", "tag": NOT, "headline": "US Bitcoin funds lost $1.07bn in a week",
  "receipt": "CryptoTicker, week to 13 Nov 2026",
  "voiceover": "And the big money? US exchange-traded funds that hold Bitcoin saw about one point zero seven billion dollars pulled out in the week to the thirteenth of November, with seven trading days of outflows in a row. Big investors were leaving, not arriving."},

 # Round 5: one data house, two readings
 {"type": "broll", "broll": "bottom-b-magnifier.mp4", "eyebrow": "Round 5 · Same data house, two readings", "tag": MIGHT, "headline": "CryptoQuant: a \"value zone\"",
  "receipt": "CryptoQuant via The Block, 18 Nov 2026",
  "voiceover": "Round five shows how messy this is. On the eighteenth of November, the analytics firm CryptoQuant said Bitcoin had reached what it calls a value zone."},
 pt("Round 5 · Same report", "…but demand is shrinking fastest since July",
    "But in the very same update, CryptoQuant said Bitcoin is back in a bearish phase, with demand growth shrinking at its fastest pace since July. Same firm, same day, two readings. That's what analysis really looks like.",
    "CryptoQuant via The Block, 18 Nov 2026", tag=NOT),

 # Ending
 {"type": "broll", "broll": "bottom-d-checklist.mp4", "eyebrow": "What to watch, not who to believe", "headline": "The signs every true bottom has shown",
  "body": "Price below what holders paid · holders in loss overall · sustained loss-selling · a panic flush",
  "receipt": "Galaxy Research (as of 9 Jun 2026)",
  "voiceover": "So, has Bitcoin hit bottom? We don't know, and neither does anyone else. Instead of watching for someone's call, watch for what Galaxy says every true bottom has shown, and which hadn't happened as of June: the price falling below what holders paid, holders in loss overall, sustained loss-selling, and a panic flush. Galaxy's own scenarios differ widely. Even they don't know."},
 {"type": "broll", "broll": "crypto-10-frost-grid.mp4", "eyebrow": "Red flag", "headline": "Guaranteed returns? Coin \"recovery\"? Walk away.",
  "voiceover": "And one warning. Crashes bring scammers. Anyone promising guaranteed crypto returns, or offering to recover coins you've lost, is a red flag."},
 {"type": "plain", "eyebrow": "Education only", "headline": "We can't answer \"should I buy?\"",
  "body": "Which watch-list signs have shown up since? Tell us in the comments.",
  "voiceover": DISC + " Which of the watch-list signs have shown up since this video? Tell us in the comments."},
]
import re
for s in scenes:
    m = re.match(r"Round (\d) · (.*)", s.get("eyebrow", ""))
    if m:
        s["rank"] = int(m.group(1)); s["name"] = "Round " + m.group(1)
for s in scenes:
    s["duration"] = est(s["voiceover"])

EMMA = {"engine": "kokoro", "name": "bf_emma", "speed": 1.05, "lang": "en-gb", "lead_pad": 400, "tail_pad": 900}
base = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
        "voice": EMMA, "timing": {"lead_in": 900}}

SOURCES = """Sources (as of 19–22 November 2026; signals change quickly):
Price: Fortune, "Current price of Bitcoin for November 19, 2026" ($63,747.99 at 6am ET); Bloomberg (Feb 2026 low ~$60k, ATH ~$126k); CryptoTicker/CoinGecko (12-month low $58,570 on 1 Jul 2026; ETF outflows week to 13 Nov 2026).
Round 1: Blockworks Research via KuCoin (week-60 pattern, ~Jul 2026); Bitget and NerdWallet (past bear-market depths).
Round 2: Julio Moreno, CryptoQuant, via Cointelegraph (late 2025: $56k–$60k realized-price range); Galaxy Research, "Bitcoin's four-year cycle: where is the bottom?" (published 12 Jun 2026, data as of 9 Jun 2026: 4 of 13 bottoming signs).
Round 3: Crypto Fear & Greed Index via CoinGabbar (5 on 6 Feb 2026; 34 on 4 Nov 2026); CryptoPotato (largest put open interest at the $60k strike on Deribit, 16 Nov 2026).
Round 4: Galaxy Research (Hash Ribbons recovery cross, early Jun 2026); NewsBTC (difficulty reduction, 14 Nov 2026); CryptoTicker (US spot BTC ETFs −$1.07bn, week to 13 Nov 2026).
Round 5: CryptoQuant via The Block, 18 Nov 2026."""

long = dict(base, slug="bitcoin-bottom-signals", countdown={"from": 5, "order": "up"},
 disclaimer="Education, not financial advice. No predictions. Data as of 19 Nov 2026.",
 thumbnail={"big": "BOTTOM?", "line": "Nobody <em>knows</em> yet · 10 signals", "frame": 0},
 scenes=scenes,
 endcard={"title": "Watch the <em>signs</em>, not the calls", "subtitle": "Subscribe for money, explained.",
          "handle": "@MzansiMoneyMatters", "duration": 15000},
 youtube={"title": "Has Bitcoin Hit Bottom? 10 Signals Analysts Watch (Nov 2026)", "privacy": "private",
  "synthetic_media": True, "category_id": "27",
  "tags": ["bitcoin bottom", "has bitcoin hit bottom", "bitcoin bottom signals", "bitcoin crash", "crypto crash", "bitcoin analysis",
           "fear and greed index", "bitcoin ETF outflows", "Mzansi Money Matters"],
  "description": ("Has Bitcoin hit bottom? Nobody knows until after. So instead of guessing, we look at 10 signals analysts watch, five that "
   "might point to a bottom and five that might not, with what each one measures and when it was recorded.\n\n"
   "General education, not financial advice. Mzansi Money Matters is not an authorised financial services provider. We make no price "
   "predictions and never tell you to buy or sell. Speak to an FSCA-authorised adviser.\n\n{chapters}\n\n" + SOURCES +
   "\n\n#BitcoinBottom #Bitcoin #CryptoCrash #MzansiMoneyMatters\n\nNarration is AI-generated. Video clips were generated with Google Flow (Veo).")})

q = [
 {"type": "broll", "broll": "bottom-c-gauge.mp4", "eyebrow": "Bitcoin's fear gauge", "headline": "It hit 5. A record low.",
  "stat": {"value": "5", "label": "6 Feb 2026", "count": {"from": 50, "to": 5, "decimals": 0, "prefix": "", "suffix": ""}},
  "receipt": "Crypto Fear & Greed Index (via CoinGabbar)",
  "voiceover": "Bitcoin's fear gauge hit five out of one hundred in February. The lowest since tracking began in twenty eighteen."},
 {"type": "point", "eyebrow": "Early November 2026", "headline": "Now it's 34",
  "stat": {"value": "34", "label": "4 Nov 2026 · \"fear\", not panic", "count": {"from": 5, "to": 34, "decimals": 0, "prefix": "", "suffix": ""}},
  "receipt": "Crypto Fear & Greed Index (via CoinGabbar)",
  "voiceover": "By early November it was back at thirty-four. Still fear, but not panic."},
 {"type": "plain", "eyebrow": "What it measures", "headline": "Mood, not the future",
  "body": "It scores price swings, volume, momentum and social buzz from 0 to 100.",
  "voiceover": "It measures the market's mood: price swings, trading volume, momentum and social buzz. It does not tell you what happens next."},
 {"type": "plain", "eyebrow": "Not a buy signal", "headline": "Education, not financial advice",
  "voiceover": "It's not a buy signal, and this isn't advice. We looked at ten signals analysts watch. Full video on our channel."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-bitcoin-fear-gauge", size=[1080, 1920], countdown={"from": 5}, broll_fit="pad",
 disclaimer="Education, not financial advice.", voice=dict(EMMA, lead_pad=300, tail_pad=600), timing={"lead_in": 600}, scenes=q,
 endcard={"title": "Bitcoin <em>bottom</em>?", "subtitle": "10 signals, sources included", "handle": "@MzansiMoneyMatters",
          "voiceover": "Watch the full video on Mzansi Money Matters.", "duration": 3500},
 youtube={"title": "Bitcoin's fear gauge hit a record low #shorts", "privacy": "private", "synthetic_media": True, "category_id": "27",
  "tags": ["bitcoin bottom", "fear and greed index", "bitcoin", "Mzansi Money Matters"],
  "description": "The Crypto Fear & Greed Index hit 5 on 6 Feb 2026, its lowest since 2018, and was 34 on 4 Nov 2026 (via CoinGabbar). What it measures, and why it isn't a buy signal. Full video: 10 signals analysts watch.\n\n#BitcoinBottom #Shorts\n\nEducation, not financial advice. MMM is not an authorised financial services provider. Narration is AI-generated. Clips generated with Google Flow (Veo)."})

json.dump(long, open("content-bottom.json", "w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-bottom.json", "w"), ensure_ascii=False, indent=2)
for n, d in (("long", long), ("short", short)):
    print(n, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"]) / 60000))
