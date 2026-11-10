"""Builds content-fiat.json (long) and content-short-fiat.json (Short):
Top 10 fiat currency failures in history (Ntokozo's list, fact-checked).
Peak monthly rates and doubling times: Hanke-Krus Hyperinflation Table (Cato).
Durations are estimates; voice.py recalculates them from the narration.
"""
import json

def est(vo):
    return int(len(vo.split()) / 155 * 60000) + 1300

WORDS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

# rank, name, where/period, stat(value,label), stat_vo, how_head, how_vo, cause_head, cause_body, cause_vo, broll(optional: query, head, body, vo)
C = [
 dict(r=10, name="Polish marka", where="Poland, 1917–1924",
      sv="275%", sl="Prices in one month, October 1923", hh="Millions of marks to one dollar",
      hvo="After the First World War, a US dollar cost about nine Polish marks. By late nineteen twenty-three it cost millions. At the peak, prices rose two hundred and seventy-five percent in a single month.",
      ch="A new country with no money to run it",
      cb="Poland was rebuilt from three war-ruined pieces, then fought the 1920 Polish–Soviet war on printed money.",
      cvo="Poland had just been rebuilt from three territories ruined by war. It paid for its government, and for the Polish–Soviet war of nineteen twenty, by printing money. In nineteen twenty-four the marka was replaced by the złoty, at one point eight million marks each."),
 dict(r=9, name="Nationalist Chinese yuan", where="China, 1935–1949",
      sv="5 days", sl="Time for prices to double, April 1949", hh="A brand-new currency, dead within months",
      hvo="By April nineteen forty-nine, prices in China were doubling roughly every five days. A new gold yuan, launched in nineteen forty-eight to fix the problem, collapsed within months.",
      ch="Paying for a civil war with the printing press",
      cb="The government printed money to fight Mao's communists as its tax base shrank.",
      cvo="The Nationalist government was fighting a civil war against Mao Zedong's communists, and paid for most of it by printing money, while the territory it could tax kept shrinking. Many historians see the hyperinflation as one reason the Nationalists lost mainland China.",
      broll=("old paper banknotes", "Confidence lost", "When people stop trusting money, they spend it as fast as they can.",
             "Once people expect money to lose value, they spend it the moment they get it. That makes prices rise even faster.")),
 dict(r=8, name="Argentine peso", where="Argentina, 1989–90 and 2001–02",
      sv="197%", sl="Prices in one month, July 1989", hh="Two collapses in one generation",
      hvo="In July nineteen eighty-nine, prices in Argentina rose nearly two hundred percent in one month. Then, in two thousand and two, the peso, which had been fixed at one to the US dollar, crashed to nearly four.",
      ch="Deficits, then a peg that couldn't hold",
      cb="Chronic deficits funded by the central bank, then a rigid dollar peg that broke in 2002.",
      cvo="For decades, the central bank funded government deficits. A fixed one-to-one dollar peg in nineteen ninety-one stopped inflation, but made the economy uncompetitive. In two thousand and one came a bank run, a freeze on withdrawals, and what was then the biggest government debt default in history."),
 dict(r=7, name="Confederate dollar", where="Confederate States, 1861–1865",
      sv="92×", sl="Southern prices by 1865 vs 1861", hh="Money backed by a war it lost",
      hvo="By the end of the American Civil War, prices in the Confederate South were about ninety times higher than in eighteen sixty-one.",
      ch="A war paid for with paper",
      cb="The South had little industry to tax, and the Union blockade choked its cotton exports.",
      cvo="The South had little industry to tax, and the Union naval blockade choked off its cotton exports. So it paid for the war mostly by printing money. When the Confederacy lost, its dollars became worthless.",
      broll=("cotton field", "Cotton couldn't save it", "The blockade cut off the South's biggest export.",
             "Cotton was the South's great export, and the blockade cut it off.")),
 dict(r=6, name="Soviet and Russian rouble", where="USSR to Russia, 1989–1993",
      sv="2,500%", sl="Consumer price rise in Russia, 1992", hh="Life savings wiped out in a year",
      hvo="When Russia freed prices in January nineteen ninety-two, prices jumped two hundred and forty-five percent in that month alone. Over the year, consumer prices rose about two thousand five hundred percent, and Soviet-era savings were wiped out.",
      ch="An empire ends, the printing press doesn't",
      cb="Late-Soviet deficits were funded by printing. Then price controls ended overnight.",
      cvo="In the last years of the Soviet Union, the government covered growing deficits by printing roubles, while price controls hid the damage. When the Soviet Union broke up and prices were freed, years of pent-up inflation hit at once."),
 dict(r=5, name="Venezuelan bolívar", where="Venezuela, crisis from 2016",
      sv="1.7m%", sl="Inflation in 2018, National Assembly estimate", hh="Fourteen zeros removed",
      hvo="Venezuela's National Assembly measured inflation of about one point seven million percent in twenty eighteen. The government has cut zeros off the currency three times: three in two thousand and eight, five in twenty eighteen, and six in twenty twenty-one.",
      ch="Oil wealth, spent and printed away",
      cb="Expropriations, price controls and printed deficits, then the oil price crash.",
      cvo="Venezuela has some of the world's biggest oil reserves. But nationalisations and price controls hurt production, the government funded huge deficits with printed money, and when the oil price crashed in twenty fourteen, the dollars stopped coming in. Sanctions made it worse.",
      broll=("oil pump jack", "Rich in oil, poor in money", "An oil giant whose currency collapsed anyway.",
             "It's a warning that natural resources alone can't protect a currency.")),
 dict(r=4, name="Yugoslav dinar", where="Yugoslavia, 1992–1994",
      sv="1.4 days", sl="Time for prices to double, January 1994", hh="A 500 billion dinar note",
      hvo="In January nineteen ninety-four, prices in Yugoslavia doubled roughly every one and a half days. In one month they rose three hundred and thirteen million percent. The central bank printed a five hundred billion dinar note.",
      ch="Break-up, war and sanctions",
      cb="The country split apart, the UN imposed sanctions, and the state printed money to pay for war and wages.",
      cvo="As Yugoslavia broke apart, wars began in Croatia and Bosnia, the United Nations imposed sanctions, and much of the economy stopped working. The government printed money to pay soldiers and state salaries."),
 dict(r=3, name="Weimar papiermark", where="Germany, 1914–1923",
      sv="4.2tn", sl="Marks to one US dollar, November 1923", hh="Prices doubled every 3.7 days",
      hvo="By November nineteen twenty-three, one US dollar cost four point two trillion German marks. At the peak, prices doubled about every three point seven days. Workers were paid twice a day, and rushed to spend their wages before they lost value.",
      ch="War debt, reparations and the Ruhr",
      cb="WWI was paid for with debt; then came Versailles reparations and the 1923 Ruhr occupation.",
      cvo="Germany paid for the First World War with debt, then owed huge reparations under the Treaty of Versailles. When France and Belgium occupied the Ruhr in nineteen twenty-three, the government printed money to pay striking workers. Confidence collapsed.",
      broll=("printing press", "The printing press ran day and night", "Germany's mint couldn't print notes fast enough.",
             "The printing presses ran day and night, and still couldn't keep up.")),
 dict(r=2, name="Zimbabwe dollar", where="Zimbabwe, 1980–2009",
      sv="79.6bn%", sl="Prices in one month, November 2008", hh="A 100 trillion dollar note",
      hvo="In November two thousand and eight, prices in Zimbabwe rose an estimated seventy-nine point six billion percent in a month, doubling about every twenty-five hours. In January two thousand and nine, the Reserve Bank issued a one hundred trillion dollar note.",
      ch="Farms seized, money printed",
      cb="Land seizures crushed farm output and tax revenue; deficits were paid with printed money.",
      cvo="From two thousand, a fast-track land reform programme seized commercial farms, and food and export production collapsed. Spending on the war in the Congo and on patronage was funded by printing money, as tax revenue fell.",
      broll=("empty supermarket shelves", "Shelves empty. Shops closed.", "In 2009 Zimbabwe dropped its own currency for the US dollar and the rand.",
             "In two thousand and nine, Zimbabwe gave up its own currency and started using the US dollar and the South African rand. Many Zimbabweans came to South Africa to survive.")),
 dict(r=1, name="Hungarian pengő", where="Hungary, 1927–1946",
      sv="15 hours", sl="Time for prices to double, July 1946", hh="The worst hyperinflation ever recorded",
      hvo="In July nineteen forty-six, prices in Hungary rose by forty-one thousand trillion percent in a single month. That's prices doubling every fifteen hours. It's the worst hyperinflation ever recorded.",
      ch="War ruin, reparations, and printing",
      cb="WWII destroyed industry; Hungary owed reparations and printed money to cope.",
      cvo="The Second World War destroyed Hungary's factories, railways and bridges. The country owed war reparations, mainly to the Soviet Union, and the government printed money to keep going. The largest note ever printed was one hundred quintillion pengő. In August nineteen forty-six, the forint replaced it, and the forint is still Hungary's currency today."),
]

scenes = [
 {"type": "intro", "eyebrow": "Hyperinflation", "headline": "10 currencies that collapsed",
  "body": "Hungary. Zimbabwe. Germany. Venezuela. And six more.",
  "voiceover": "In nineteen forty-six, prices in Hungary doubled every fifteen hours. A salary paid on Monday morning had lost about ninety percent of its value by Wednesday."},
 {"type": "plain", "eyebrow": "How we ranked them", "headline": "Speed, scale and lasting damage",
  "body": "Peak rates: Hanke–Krus Hyperinflation Table.",
  "voiceover": "These are the ten worst currency failures in history, ranked by how fast prices rose, how far the money fell, and how long the damage lasted. For each one: how bad it got, and what caused it."},
]
for c in C:
    nm = c["name"]
    scenes += [
     {"type": "rank", "rank": c["r"], "eyebrow": c["where"], "headline": nm,
      "voiceover": f"Number {WORDS[c['r']]}. The {nm}. {c['where'].split(',')[0]}."},
     {"type": "point", "rank": c["r"], "name": nm, "eyebrow": "How bad it got", "headline": c["hh"],
      "stat": {"value": c["sv"], "label": c["sl"]}, "voiceover": c["hvo"]},
     {"type": "point", "rank": c["r"], "name": nm, "eyebrow": "What caused it", "headline": c["ch"],
      "body": c["cb"], "voiceover": c["cvo"]},
    ]
    if c.get("broll"):
        q, h, b, vo = c["broll"]
        scenes.append({"type": "broll", "broll": q, "eyebrow": nm, "headline": h, "body": b, "voiceover": vo})

scenes += [
 {"type": "plain", "eyebrow": "Honourable mentions", "headline": "Greece 1944. Peru 1990. Brazil before 1994.",
  "voiceover": "Honourable mentions: Greece in nineteen forty-four, where prices rose thirteen thousand eight hundred percent in one month, Peru in nineteen ninety, and Brazil's string of failed currencies before the real in nineteen ninety-four."},
 {"type": "broll", "broll": "money counting machine", "eyebrow": "The common thread",
  "headline": "Governments printed money faster than the economy could grow.",
  "voiceover": "Every one of these failures has the same root. Governments printed money to pay for war, reparations or spending, faster than the economy could produce goods. Once people lost confidence, the collapse fed itself."},
 {"type": "plain", "eyebrow": "Closer to home", "headline": "Why central bank independence matters",
  "body": "The SA Reserve Bank's independence is protected by the Constitution.",
  "voiceover": "That's why South Africa's Constitution protects the independence of the Reserve Bank. Its job is to protect the value of the rand, not to fund the government."},
 {"type": "plain", "eyebrow": "Your turn", "headline": "Which of these surprised you most?",
  "voiceover": "Which of these surprised you most? Tell us in the comments."},
]
for s in scenes:
    s["duration"] = est(s["voiceover"])

base = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
        "voice": {"name": "en-US-BrianMultilingualNeural", "rate": "+4%", "pitch": "+0Hz", "lead_pad": 400, "tail_pad": 900},
        "timing": {"lead_in": 900}}

long = dict(base, thumbnail={"kicker": "Hungary, 1946", "big": "15 HOURS", "line": "for prices to <em>double</em>", "photo": "old paper money banknotes"}, slug="top10-currency-failures", countdown={"from": 10},
 disclaimer="Education, not financial advice.", scenes=scenes,
 endcard={"title": "Protect your <em>money</em>", "subtitle": "Subscribe for South African money, explained.",
          "handle": "@MzansiMoneyMatters", "duration": 5000},
 youtube={"title": "10 Currencies That Collapsed: The Worst Hyperinflations in History", "privacy": "private",
  "synthetic_media": True, "category_id": "27",
  "tags": ["hyperinflation", "currency collapse", "Zimbabwe dollar", "Weimar Germany", "Hungarian pengo", "Venezuela", "Mzansi Money Matters"],
  "description": ("From Hungary's pengő, where prices doubled every 15 hours, to the Zimbabwe dollar's 100 trillion note: "
   "the 10 worst fiat currency failures in history, how bad they got, and what caused them.\n\n{chapters}\n\n"
   "Sources: Hanke & Krus, World Hyperinflations / Hyperinflation Table (Cato Institute); IMF; historical records.\n\n"
   "Education, not financial advice. Narration and some visuals are AI-generated. Stock footage from Pexels.")})

q = [
 {"type": "broll", "broll": "old paper banknotes", "eyebrow": "Hungary, 1946", "headline": "Prices doubled every 15 hours",
  "voiceover": "In nineteen forty-six, prices in Hungary doubled every fifteen hours."},
 {"type": "point", "rank": 1, "name": "Hungarian pengő", "eyebrow": "Your salary", "headline": "Paid on Monday. Worth a ninth by Wednesday.",
  "voiceover": "Get paid on Monday morning, and by Wednesday your money buys about a ninth of what it did."},
 {"type": "point", "rank": 1, "name": "Hungarian pengő", "eyebrow": "In one month", "headline": "The worst hyperinflation ever recorded",
  "stat": {"value": "41 quadrillion %", "label": "Price rise, July 1946"},
  "voiceover": "In July that year, prices rose forty-one thousand trillion percent in a single month. The worst hyperinflation ever recorded."},
 {"type": "point", "rank": 1, "name": "Hungarian pengő", "eyebrow": "The biggest note ever printed", "headline": "100 quintillion pengő",
  "voiceover": "The government printed a one hundred quintillion pengő note. That's a one with twenty zeros."},
 {"type": "broll", "broll": "printing press", "eyebrow": "The cause", "headline": "War ruin, reparations, and the printing press",
  "voiceover": "War had wrecked the economy, the country owed reparations, and the government just kept printing."},
 {"type": "plain", "eyebrow": "And number two?", "headline": "It happened right next door.",
  "voiceover": "And number two on the list happened right next door to South Africa."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-pengo", size=[1080, 1920], countdown={"from": 10},
 disclaimer="Education, not financial advice.",
 voice={"name": "en-US-BrianMultilingualNeural", "rate": "+6%", "pitch": "+0Hz", "lead_pad": 300, "tail_pad": 600},
 timing={"lead_in": 600}, scenes=q,
 endcard={"title": "All ten on the <em>channel</em>", "subtitle": "The worst currency collapses in history",
          "handle": "@MzansiMoneyMatters", "voiceover": "Watch all ten on Mzansi Money Matters.", "duration": 3500},
 youtube={"title": "Prices doubled every 15 hours #shorts", "privacy": "private", "synthetic_media": True, "category_id": "27",
  "tags": ["hyperinflation", "Hungary", "pengo", "Mzansi Money Matters"],
  "description": "Hungary, 1946: the worst hyperinflation ever recorded. Full top 10 on Mzansi Money Matters.\n\nSource: Hanke & Krus Hyperinflation Table (Cato Institute).\n\nEducation, not financial advice. Narration is AI-generated. Stock footage from Pexels."})

json.dump(long, open("content-fiat.json", "w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-fiat.json", "w"), ensure_ascii=False, indent=2)
for n, d in (("long", long), ("short", short)):
    print(n, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"]) / 60000))
