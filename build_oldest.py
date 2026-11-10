"""Builds content-oldest.json (long) and content-short-oldest.json (Short):
the 10 oldest companies still operating, ranked by founding year (10 = youngest of the ten, 1 = oldest).
Durations are estimates; voice.py recalculates them from the narration.
"""
import json

def est(vo):
    return int(len(vo.split()) / 155 * 60000) + 1300

W = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

# r, name, place, year, year_vo, what, founded_head, founded_vo, own_head, own_body, own_vo, test_head, test_body, test_vo, (broll query, head, vo) optional
C = [
 dict(r=10, name="Berenberg", place="Hamburg, Germany", year="1590", yv="fifteen ninety",
      fh="A bank founded by two refugee brothers",
      fvo="Berenberg was founded in Hamburg around fifteen ninety by Hans and Paul Berenberg, Protestant brothers who had fled Antwerp. It calls itself the world's oldest merchant bank, and still employs about sixteen hundred people.",
      oh="Berenberg → Gossler → partners", ob="The Berenberg line ended in 1822. Gossler descendants still own about 30%.",
      ovo="Johann Hinrich Gossler married into the family and became a partner in seventeen sixty-nine, and the bank took the name Berenberg, Gossler and Company. The last Berenberg died in eighteen twenty-two. Today the Berenberg-Gossler family holds about thirty percent, alongside the managing partners.",
      th="The Napoleonic Wars", tb="It lost half its capital, then rebuilt.",
      tvo="Its biggest test was the Napoleonic Wars, when it lost half its capital. It rebuilt, and grew bigger than before. And the tests haven't stopped: in June twenty twenty-six, Germany's banking regulator suspended its managing partners over possible governance breaches and appointed special commissioners.",
      br=("Hamburg harbour", "From refugees to a global bank", "Today it has offices in London, Frankfurt and New York.")),
 dict(r=9, name="Beretta", place="Gardone Val Trompia, Italy", year="1526", yv="fifteen twenty-six",
      fh="Gun barrels for the Venetian Republic",
      fvo="Beretta traces its history to fifteen twenty-six, in the iron-working valley of Gardone Val Trompia in northern Italy. This year, it turned five hundred.",
      oh="One family, 500 years", ob="Now in its 16th generation. Beretta Holding owns brands like Benelli and Sako.",
      ovo="Ownership has never left the Beretta family. It's now run by the sixteenth generation, and the wider Beretta Holding group earned more than one point seven billion euros in twenty twenty-four.",
      th="Plague, and a business that rises and falls with war", tb="In 1631 plague killed about a third of the town.",
      tvo="In sixteen thirty-one, plague killed about a third of Gardone's people. And because its customers were armies, its sales rose and fell with every war. Selling hunting guns to civilians kept the family business alive in peacetime."),
 dict(r=8, name="Monte dei Paschi di Siena", place="Siena, Italy", year="1472", yv="fourteen seventy-two",
      fh="The world's oldest bank",
      fvo="Monte dei Paschi was founded in fourteen seventy-two by the Republic of Siena, to lend to the poor and fight loan sharks. It's the oldest bank in the world still operating.",
      oh="City → foundation → state → stock market", ob="The Italian state owned most of it after 2017; it now holds about 6%.",
      ovo="For centuries it was tied to the city of Siena, and later controlled by a local foundation. After a state rescue in twenty seventeen, the Italian government became its biggest owner. The state has since sold most of its shares, and in twenty twenty-five, Monte dei Paschi took over its rival Mediobanca.",
      th="An expensive deal, a scandal and a bailout", tb="Losses after buying Antonveneta in 2007, a derivatives scandal, then a 2017 state rescue.",
      tvo="Its near-death came this century. It paid about nine billion euros for the bank Antonveneta just before the two thousand and eight crash. Then came hidden derivative losses, failed stress tests, and finally a state bailout in twenty seventeen.",
      br=("Siena Italy", "Survived 550 years. Nearly killed in ten.", "Bad deals and hidden losses did what wars couldn't.")),
 dict(r=7, name="Stora Enso", place="Falun, Sweden (now Helsinki)", year="1288", yv="twelve eighty-eight",
      fh="The world's oldest known share",
      fvo="In twelve eighty-eight, a document gave the Bishop of Västerås one eighth of the Stora Kopparberg copper mine in Falun, Sweden. It's the oldest known share certificate in the world.",
      oh="Copper mine → company → merger", ob="Royal charter in 1347. Incorporated in 1862. Merged with Finland's Enso in 1998.",
      ovo="The king granted it a charter in thirteen forty-seven. It became a modern shareholder company in eighteen sixty-two, and in nineteen ninety-eight it merged with the Finnish company Enso to form Stora Enso, now based in Helsinki with about nineteen thousand employees.",
      th="The mine ran out", tb="The Great Pit collapsed in 1687. Mining ended in 1992.",
      tvo="Its biggest test was its own mine. The Great Pit collapsed in sixteen eighty-seven, and the copper slowly ran out. So the company moved into forests, timber and paper. Mining in Falun ended in nineteen ninety-two, but the company lived on.",
      br=("copper mine", "Reinvented: from copper to paper", "Today it makes paper, packaging and wood products.")),
 dict(r=6, name="The Royal Mint", place="Llantrisant, Wales", year="c. 886", yv="around eight eighty-six",
      fh="Making Britain's money for 1,100 years",
      fvo="The Royal Mint traces its origins to around eight eighty-six, under King Alfred the Great. For centuries it worked inside the Tower of London, and Isaac Newton served as its Warden.",
      oh="Always the Crown's", ob="It became a company in 2009, still owned by HM Treasury.",
      ovo="It has always been owned by the Crown and the state. It moved to Llantrisant in Wales from nineteen sixty-eight, to make the new decimal coins, and in two thousand and nine it became a limited company owned by His Majesty's Treasury.",
      th="People stopped using cash", tb="In 2024 it struck no new coins for circulation.",
      tvo="Its biggest test is happening now. People are using less cash, and in twenty twenty-four it struck no new coins for circulation at all. So the Mint is reinventing itself, selling gold and recovering precious metals from old electronics."),
 dict(r=5, name="Monnaie de Paris", place="Paris, France", year="864", yv="eight sixty-four",
      fh="France's oldest institution",
      fvo="The Monnaie de Paris was created in eight sixty-four by the Edict of Pîtres, under King Charles the Bald. It's France's oldest institution.",
      oh="Kings → Republic → state enterprise", ob="Under the finance ministry from 1796. A state-owned commercial enterprise since 2007.",
      ovo="It has always belonged to the French state, first the kings, then the Republic. In seventeen ninety-six it came under the finance ministry, and since two thousand and seven it has been run as a state-owned commercial enterprise.",
      th="The end of the franc", tb="In 2002 France switched to the euro.",
      tvo="Its biggest modern test was the end of the French franc. When France adopted the euro in two thousand and two, the Mint had to make an entirely new currency, and it now helps fight euro counterfeiting across Europe."),
 dict(r=4, name="St. Peter Stiftskulinarium", place="Salzburg, Austria", year="803", yv="eight hundred and three",
      fh="The world's oldest restaurant",
      fvo="The St. Peter restaurant in Salzburg, Austria, was first mentioned in eight hundred and three. It started as the wine cellar of St. Peter's Abbey, and grew into an inn for pilgrims and travellers.",
      oh="Still inside the abbey", ob="Run by outside operators on a lease since the early 1990s.",
      ovo="It still sits inside the Benedictine abbey's walls. Since the early nineteen nineties it has been leased to outside operators, who renovated the kitchen and the menu. Mozart is said to have dined there.",
      th="Staying relevant for 1,200 years", tb="From a monks' wine cellar to a tourist landmark.",
      tvo="Its test has been staying relevant for twelve hundred years: from a monastery cellar, to a pilgrims' inn, to a restaurant that now hosts Mozart dinner concerts for tourists."),
 dict(r=3, name="Hōshi Ryokan", place="Komatsu, Ishikawa, Japan", year="718", yv="seven eighteen",
      fh="A hot spring inn, 1,300 years old",
      fvo="Hōshi Ryokan, a hot spring inn in Japan's Ishikawa Prefecture, was founded in seven eighteen.",
      oh="One family, 46 generations", ob="Passed from father to son, or adopted son, for 46 generations.",
      ovo="It has been owned and run by the same family for forty-six generations, passed down to a son, or when there was no son, to an adopted son.",
      th="Who takes over?", tb="The next owner is set to be the first woman in over 1,300 years.",
      tvo="Its biggest test is succession. Every family business must find the next leader, and for the first time in its history, the heir is expected to be a woman: the owner's daughter."),
 dict(r=2, name="Nishiyama Onsen Keiunkan", place="Yamanashi, Japan", year="705", yv="seven oh five",
      fh="The world's oldest hotel",
      fvo="Nishiyama Onsen Keiunkan was founded in seven oh five by Fujiwara Mahito, beside a hot spring in the mountains of Yamanashi, Japan. Guinness World Records recognises it as the oldest hotel in the world.",
      oh="One family, 52 generations", ob="Including adopted heirs, to keep the line going.",
      ovo="It has been run by the same family for fifty-two generations, including adopted heirs, when the family needed one. It has just thirty-five rooms.",
      th="Never closing", tb="Same family, same spring, through 1,300 years of Japanese history.",
      tvo="Its test is the hardest kind: thirteen centuries of wars, earthquakes and economic crashes, without changing hands. The hot spring that started it still feeds the baths today.",
      br=("Japanese hot spring onsen", "The water that built a business", "The same spring has fed its baths for 1,300 years.")),
 dict(r=1, name="Kongō Gumi", place="Osaka, Japan", year="578", yv="five seventy-eight",
      fh="Temple builders for 1,400 years",
      fvo="Kongō Gumi was founded in five seventy-eight, when Prince Shōtoku invited the carpenter Kongō Shigemitsu from Korea's Baekje kingdom to build the Shitennō-ji temple in Osaka. It's the oldest company in the world still operating.",
      oh="40 Kongōs, then a takeover", ob="Led by 40 generations of the Kongō family. Bought by Takamatsu Construction in 2006.",
      ovo="Forty generations of the Kongō family led it. Then in January two thousand and six, its business was bought by Takamatsu Construction Group, and it still operates today as a Takamatsu subsidiary.",
      th="Debt", tb="After 1,400 years, it couldn't service its debts. The old company owed about ¥4 billion.",
      tvo="What wars and earthquakes couldn't do, debt nearly did. By the early two thousands it couldn't service its loans. The old company went bankrupt owing about four billion yen. Its craft survived only because another company bought it.",
      br=("Japanese temple wood", "Still building temples", "Its carpenters still build and restore temples and shrines.")),
]

scenes = [
 {"type": "intro", "eyebrow": "Survivors", "headline": "The 10 oldest companies still in business",
  "body": "Kongō Gumi. The Royal Mint. Beretta. And seven more.",
  "voiceover": "Most companies don't outlive their founders. These ten have survived for centuries, some for more than a thousand years."},
 {"type": "plain", "eyebrow": "How we ranked them", "headline": "By the year they were founded",
  "body": "Number one is the oldest.",
  "voiceover": "We've ranked them by the year they were founded, counting down to the oldest. For each one: when it started, who has owned it, and the biggest test it survived."},
]
for c in C:
    nm = c["name"]
    scenes += [
     {"type": "rank", "rank": c["r"], "eyebrow": c["place"], "headline": nm,
      "voiceover": f"Number {W[c['r']]}. {nm.replace('The Royal Mint','The Royal Mint')}. Founded {c['yv']}."},
     {"type": "point", "rank": c["r"], "name": nm, "eyebrow": "Founded", "headline": c["fh"],
      "stat": {"value": c["year"], "label": c["place"]}, "voiceover": c["fvo"]},
     {"type": "point", "rank": c["r"], "name": nm, "eyebrow": "Ownership", "headline": c["oh"], "body": c["ob"], "voiceover": c["ovo"]},
     {"type": "point", "rank": c["r"], "name": nm, "eyebrow": "Biggest test", "headline": c["th"], "body": c["tb"], "voiceover": c["tvo"]},
    ]
    if c.get("br"):
        q, h, vo = c["br"]
        scenes.append({"type": "broll", "broll": q, "eyebrow": nm, "headline": h, "voiceover": vo})

scenes += [
 {"type": "plain", "eyebrow": "What the survivors share", "headline": "Slow growth. Low debt. A plan for the next generation.",
  "voiceover": "What do the survivors have in common? They grew slowly, they planned who would take over next, and when their main business faded, they changed. And the two that came closest to dying, Kongō Gumi and Monte dei Paschi, were both brought down by debt."},
 {"type": "plain", "eyebrow": "Your turn", "headline": "Which South African business will last 500 years?",
  "voiceover": "Which South African business do you think could still be around in five hundred years? Tell us in the comments."},
]
for s in scenes:
    s["duration"] = est(s["voiceover"])

base = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
        "voice": {"name": "en-US-BrianMultilingualNeural", "rate": "+4%", "pitch": "+0Hz", "lead_pad": 400, "tail_pad": 900},
        "timing": {"lead_in": 900}}

long = dict(base, thumbnail={"kicker": "Top 10", "big": "1,448", "line": "years old. <em>Still open.</em>", "photo": "japanese temple"}, slug="top10-oldest-companies", countdown={"from": 10},
 disclaimer="Education, not financial advice.", scenes=scenes,
 endcard={"title": "Built to <em>last</em>", "subtitle": "Subscribe for South African money, explained.",
          "handle": "@MzansiMoneyMatters", "duration": 5000},
 youtube={"title": "The 10 Oldest Companies Still in Business (One Is 1,448 Years Old)", "privacy": "private",
  "synthetic_media": True, "category_id": "27",
  "tags": ["oldest companies", "Kongo Gumi", "oldest bank", "Monte dei Paschi", "Royal Mint", "family business", "Mzansi Money Matters"],
  "description": ("The 10 oldest companies in the world that are still operating, ranked by founding year: when they started, "
   "who has owned them, and the biggest test each one survived.\n\n{chapters}\n\n"
   "Sources: company histories and annual reports; Guinness World Records; Reuters and The Star (Monte dei Paschi/Mediobanca, 2025); "
   "Wikipedia company articles.\n\nEducation, not financial advice. Narration and some visuals are AI-generated. Stock footage from Pexels.")})

q = [
 {"type": "broll", "broll": "Japanese temple wood", "eyebrow": "Founded 578", "headline": "The oldest company on earth",
  "voiceover": "This company was founded in the year five seventy-eight. It's the oldest company on earth."},
 {"type": "point", "rank": 1, "name": "Kongō Gumi", "eyebrow": "Osaka, Japan", "headline": "Temple builders for 1,400 years",
  "stat": {"value": "40", "label": "Generations of the Kongō family"},
  "voiceover": "Kongō Gumi built Japan's temples, led by forty generations of the same family."},
 {"type": "point", "rank": 1, "name": "Kongō Gumi", "eyebrow": "It survived", "headline": "Wars. Earthquakes. Empires.",
  "voiceover": "It survived wars, earthquakes, and the rise and fall of empires."},
 {"type": "point", "rank": 1, "name": "Kongō Gumi", "eyebrow": "What nearly killed it", "headline": "Debt.",
  "stat": {"value": "¥4bn", "label": "Debt when the old company went bust, 2006"},
  "voiceover": "What finally nearly killed it? Debt. In two thousand and six, it was sold to save the business."},
 {"type": "plain", "eyebrow": "The lesson", "headline": "1,400 years of survival. Undone by borrowing.",
  "voiceover": "Fourteen hundred years of survival, undone by borrowing."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-kongo-gumi", size=[1080, 1920], countdown={"from": 10},
 disclaimer="Education, not financial advice.",
 voice={"name": "en-US-BrianMultilingualNeural", "rate": "+6%", "pitch": "+0Hz", "lead_pad": 300, "tail_pad": 600},
 timing={"lead_in": 600}, scenes=q,
 endcard={"title": "All ten on the <em>channel</em>", "subtitle": "The oldest companies still in business",
          "handle": "@MzansiMoneyMatters", "voiceover": "Watch all ten on Mzansi Money Matters.", "duration": 3500},
 youtube={"title": "The oldest company on earth was nearly killed by debt #shorts", "privacy": "private", "synthetic_media": True,
  "category_id": "27", "tags": ["Kongo Gumi", "oldest company", "debt", "Mzansi Money Matters"],
  "description": "Kongō Gumi, founded in 578, survived 1,400 years, then nearly died of debt. Full top 10 on Mzansi Money Matters.\n\nEducation, not financial advice. Narration is AI-generated. Stock footage from Pexels."})

json.dump(long, open("content-oldest.json", "w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-oldest.json", "w"), ensure_ascii=False, indent=2)
for n, d in (("long", long), ("short", short)):
    print(n, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"]) / 60000))
