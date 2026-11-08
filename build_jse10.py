"""Builds content-jse10.json (long video) and content-short-jse10.json (Short):
the 10 biggest South African companies on the JSE, closing prices Friday 6 November 2026.

Rule: headquartered in South Africa, with the JSE as its main listing.
Values: closing price x shares in issue (Mansa Markets JSE board, 6 Nov 2026),
cross-checked against Yahoo Finance, Morningstar and Simply Wall St.
Script approved in the Claude doc "10 Biggest SA Companies on the JSE (2026) - Script".
Durations are estimates for preview only; voice.py recalculates them.
"""
import json

def est(vo):
    return int(len(vo.split()) / 155 * 60000) + 1300

WORDS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

# rank, name, spoken name, hq, value card, value spoken, facts [(eyebrow, headline, body, voiceover)], known-for broll scene
C = [
 dict(rank=10, name="Sanlam", say="Sanlam", hq="Cape Town", mv="R187bn", mv_vo="about one hundred and eighty-seven billion rand",
      facts=[("Founded 1918", "A Cape Town insurer, over 100 years old", None,
              "Sanlam is a Cape Town insurer, founded in nineteen eighteen.")],
      kh="A photo finish for tenth", kb="Discovery and Shoprite are within about R6 billion.",
      kvo="But number ten is a photo finish. Discovery and Shoprite are right behind Sanlam, all three within about six billion rand of each other. One good week for either, and the order flips.",
      broll="insurance office meeting"),
 dict(rank=9, name="Absa", say="Absa", hq="Johannesburg", mv="R200bn", mv_vo="about two hundred billion rand",
      facts=[("Renamed 2018", "Once Barclays Africa", None,
              "Absa was once known as Barclays Africa, and took back its South African name in twenty eighteen.")],
      kh="The smallest of four banks on this list", kb="Four of the ten biggest are banks.",
      kvo="It's the smallest of the four banks on this list. And yes, four of South Africa's ten biggest companies are banks.",
      broll="bank atm city street"),
 dict(rank=8, name="Valterra Platinum", say="Valterra Platinum", hq="Johannesburg", mv="R302bn", mv_vo="about three hundred and two billion rand",
      facts=[("Split off in 2025", "Formerly Anglo American Platinum", None,
              "You may know it by its old name, Anglo American Platinum. In twenty twenty-five it was split off from Anglo American and renamed Valterra.")],
      kh="Platinum swings hard", kb="Worth about R347 billion in early October.",
      kvo="It produces the platinum group metals used in car catalytic converters and jewellery. Platinum prices swing hard, and so does this share. It was worth about three hundred and forty-seven billion rand in early October.",
      broll="platinum mine underground"),
 dict(rank=7, name="Vodacom", say="Vodacom", hq="Midrand", mv="R310bn+", mv_vo="over three hundred and ten billion rand",
      facts=[("Controlled by Vodafone", "But headquartered in Midrand", "Its main listing is the JSE, so it makes our list.",
              "Vodacom is controlled by Britain's Vodafone, but it's headquartered in Midrand and its main listing is the JSE, so it makes our list.")],
      kh="One of two telecom giants", kb="Vodacom and MTN both make the top ten.",
      kvo="It's one of two telecom giants in this top ten. The other one is next.",
      broll="cell tower sunset"),
 dict(rank=6, name="MTN", say="M T N", hq="Johannesburg", mv="R391bn", mv_vo="about three hundred and ninety-one billion rand",
      facts=[("The yellow network", "The bigger of SA's two telecom giants", None,
              "The yellow network is the bigger of South Africa's two telecom giants on the JSE.")],
      kh="A pan-African business", kb="Its value moves with currencies far beyond the rand.",
      kvo="It operates across Africa, which means its value moves with currencies far beyond the rand.",
      broll="african city mobile phone"),
 dict(rank=5, name="Standard Bank", say="Standard Bank", hq="Johannesburg", mv="R510bn", mv_vo="about five hundred and ten billion rand",
      facts=[("Founded 1862", "Older than the JSE itself", None,
              "Now we enter the half-trillion club. Standard Bank was founded in eighteen sixty-two, before the JSE even existed.")],
      kh="Welcome to the half-trillion club", kb="The top five are each worth over R500 billion.",
      kvo="From here on, every company on this list is worth more than half a trillion rand.",
      broll="johannesburg skyline"),
 dict(rank=4, name="FirstRand", say="FirstRand", hq="Johannesburg", mv="R541bn", mv_vo="about five hundred and forty-one billion rand",
      facts=[("The group behind", "FNB, RMB and WesBank", None,
              "You may not know the name FirstRand, but you know its brands: F N B, R M B and WesBank.")],
      kh="The top four are within 3%", kb="Any of them could be number one next week.",
      kvo="And here's the twist. The top four companies are all within about three percent of each other. Any of them could be number one next week.",
      broll="banking app on phone"),
 dict(rank=3, name="Gold Fields", say="Gold Fields", hq="Sandton", mv="R555bn", mv_vo="about five hundred and fifty-five billion rand",
      facts=[("Founded 1887", "The same year as the JSE", None,
              "Gold Fields was founded in eighteen eighty-seven, the same year as the JSE itself.")],
      kh="A possible mega-merger", kb="A proposed tie-up with Australia's Northern Star.",
      kvo="It's also weighing a proposed tie-up with Australia's Northern Star, which could create the world's second-largest gold producer. Watch this space.",
      broll="gold bars"),
 dict(rank=2, name="Naspers", say="Naspers", hq="Cape Town", mv="R566bn", mv_vo="about five hundred and sixty-six billion rand",
      facts=[("Founded 1915", "From newspapers to global tech", None,
              "Naspers started as a Cape Town newspaper publisher in nineteen fifteen. Today it's a global tech investor."),
             ("A rough 2026", "Shares down about 30% this year", "Roughly R249 billion of value lost.",
              "But twenty twenty-six has been rough. Its share price fell about thirty percent between January and early November, wiping roughly two hundred and forty-nine billion rand off its value.")],
      kh="Number one on Thursday", kb="By Friday's close, it had slipped.",
      kvo="On Thursday, it was still number one. By Friday's close, it had slipped.",
      broll="newspaper printing press"),
 dict(rank=1, name="Capitec", say="Capitec", hq="Stellenbosch", mv="R568bn", mv_vo="about five hundred and sixty-eight billion rand",
      facts=[("Opened 2001", "Now officially Capitec Limited", "The new name took effect in October 2026.",
              "And the most valuable South African company on the JSE is Capitec. It opened in two thousand and one, and in October twenty twenty-six officially changed its name to Capitec Limited."),
             ("Five-year rise", "Shares up about 191%", "In the five years to July 2026.",
              "Its shares rose about one hundred and ninety-one percent in the five years to July twenty twenty-six.")],
      kh="About R2 billion ahead of Naspers", kb="Closing prices, Friday 6 November 2026.",
      kvo="On the sixth of November, it was worth about five hundred and sixty-eight billion rand, just ahead of Naspers.",
      broll="bank branch customers"),
]

scenes = [
 {"type":"intro","eyebrow":"Friday, 6 November 2026","headline":"R568 billion: South Africa's new number one",
  "body":"Capitec vs Naspers. About R2 billion apart.",
  "voiceover":"On Thursday, the most valuable South African company on the JSE was a media giant founded in nineteen fifteen. By Friday's close, it was a bank that only opened its doors in two thousand and one."},
 {"type":"plain","eyebrow":"The gap","headline":"About R2 billion apart.","body":"Both worth more than half a trillion rand.",
  "voiceover":"The gap between them? About two billion rand. That sounds like a lot, until you realise both are worth more than half a trillion."},
 {"type":"plain","eyebrow":"Today","headline":"The 10 biggest homegrown companies on the JSE",
  "body":"Education only. Not financial advice.",
  "voiceover":"Today we count down the ten biggest homegrown companies on the Johannesburg Stock Exchange, using closing prices from Friday, the sixth of November twenty twenty-six. Quick note before we start: this video is for education only. It is not financial advice. Do your own research, or speak to a registered financial adviser, before you invest."},
 {"type":"broll","broll":"stock exchange trading screen","eyebrow":"Not on our list","headline":"BHP, AB InBev, BAT and more",
  "body":"Global giants that also trade on the JSE.",
  "voiceover":"First, the elephants in the room. The biggest listings on the JSE are global companies that also trade here. B H P is worth about three point three trillion rand. A B InBev, the world's biggest brewer, about two point five trillion. British American Tobacco, two point two trillion. Then Richemont, Prosus, Glencore, Anglo American and AngloGold Ashanti."},
 {"type":"plain","eyebrow":"Our rule","headline":"Headquartered in South Africa. JSE as its main listing.",
  "voiceover":"Some have deep South African roots. Anglo American was founded in Johannesburg in nineteen seventeen. AngloGold Ashanti moved its head office to the United States in twenty twenty-three. But today, their main home is somewhere else. So here's our rule: to make this list, a company must be headquartered in South Africa, with the JSE as its main listing. Let's go."},
]
for c in C:
    r, nm = c["rank"], c["name"]
    scenes.append({"type":"rank","rank":r,"eyebrow":c["hq"],"headline":nm,
                   "voiceover":f"Number {WORDS[r]}. {c['say']}."})
    scenes.append({"type":"point","rank":r,"name":nm,"eyebrow":"Market value","headline":f"Worth {c['mv']}",
                   "stat":{"value":c["mv"],"label":"Market value, close 6 Nov 2026"},
                   "voiceover":f"Market value: {c['mv_vo']}."})
    for eb, hd, body, vo in c["facts"]:
        s = {"type":"point","rank":r,"name":nm,"eyebrow":eb,"headline":hd,"voiceover":vo}
        if body: s["body"] = body
        scenes.append(s)
    scenes.append({"type":"broll","broll":c["broll"],"eyebrow":"Why it matters","headline":c["kh"],"body":c["kb"],
                   "voiceover":c["kvo"]})

total_bn = 187 + 200 + 310 + 302 + 391 + 510 + 541 + 555 + 566 + 568
scenes += [
 {"type":"plain","eyebrow":"The top ten","headline":"Together: about R4.1 trillion",
  "body":"Four banks, two telecoms, two miners, an insurer and a tech investor.",
  "voiceover":"So that's the top ten: four banks, two telecom companies, two miners, an insurer and a tech investor. Together they're worth about four point one trillion rand."},
 {"type":"plain","eyebrow":"Your turn","headline":"Will Capitec still be number one by year-end?",
  "voiceover":"And the top spot is a coin toss. Will Capitec still be number one by the end of twenty twenty-six, or will Naspers or Gold Fields take it back? Tell us in the comments."},
 {"type":"plain","eyebrow":"One last reminder","headline":"Values change every day. Not financial advice.",
  "voiceover":"If you want more videos like this, subscribe and check out our J S E Top Tens playlist. One last reminder: share values change every day, and this video is not financial advice. Do your own research before you invest. This is Mzansi Money Matters."},
]
for s in scenes:
    s["duration"] = est(s["voiceover"])

base = {
 "template":"template-countdown.html",
 "brand":{"name":"Mzansi Money Matters","logo":"logo.jpg"},
 "voice":{"name":"en-US-BrianMultilingualNeural","rate":"+4%","pitch":"+0Hz","lead_pad":400,"tail_pad":900},
 "timing":{"lead_in":900},
}
SOURCES = ("Sources: closing prices and shares in issue from Mansa Markets (JSE close, 6 November 2026), cross-checked with "
           "Yahoo Finance, Morningstar and Simply Wall St. Naspers figures from MyBroadband (7 Nov 2026); Capitec facts from its "
           "public company record.")
long = dict(base, slug="jse10-biggest-sa-companies-2026", countdown={"from":10},
 disclaimer="Education, not financial advice. JSE closing prices, 6 November 2026.",
 scenes=scenes,
 endcard={"title":"Subscribe for the <em>next</em> ten","subtitle":"South African money, explained.","handle":"@MzansiMoneyMatters","duration":5000},
 youtube={"title":"10 Biggest South African Companies on the JSE (2026)","privacy":"private","synthetic_media":True,"category_id":"27",
  "tags":["JSE","biggest companies South Africa","Capitec","Naspers","Gold Fields","FirstRand","Standard Bank","MTN","market cap","Mzansi Money Matters"],
  "description":("The 10 biggest South African companies on the Johannesburg Stock Exchange by market value, using closing prices from "
   "Friday 6 November 2026. Our rule: headquartered in South Africa, with the JSE as its main listing. Capitec edged past Naspers "
   "by about R2 billion.\n\n{chapters}\n\n" + SOURCES +
   "\n\nEducation, not financial advice. Values change every day. Narration and some visuals are AI-generated. Stock footage from Pexels.")})

# Short: Capitec vs Naspers photo finish (teaser of #1)
q = [
 {"type":"broll","broll":"johannesburg skyline","eyebrow":"Friday, 6 November 2026","headline":"South Africa's most valuable company just changed",
  "voiceover":"South Africa's most valuable homegrown company just changed, and the gap is tiny."},
 {"type":"point","rank":2,"name":"Naspers","eyebrow":"Founded 1915","headline":"Naspers","stat":{"value":"R566bn","label":"Market value"},
  "voiceover":"Naspers, a media giant founded in nineteen fifteen, was number one on Thursday. It's down about thirty percent this year, and now it's worth about five hundred and sixty-six billion rand."},
 {"type":"point","rank":1,"name":"Capitec","eyebrow":"Opened 2001","headline":"Capitec","stat":{"value":"R568bn","label":"Market value"},
  "voiceover":"By Friday's close, Capitec, a bank that only opened in two thousand and one, had squeezed past. About five hundred and sixty-eight billion rand."},
 {"type":"plain","eyebrow":"The gap","headline":"About R2 billion apart.","body":"It could flip any day.",
  "voiceover":"About two billion rand apart. It could flip any day. Who's number one by year-end? Not financial advice."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-jse10-capitec-naspers", size=[1080,1920], countdown={"from":2},
 disclaimer="Education, not financial advice. JSE close, 6 Nov 2026.",
 voice={"name":"en-US-BrianMultilingualNeural","rate":"+6%","pitch":"+0Hz","lead_pad":200,"tail_pad":400},
 timing={"lead_in":500}, scenes=q,
 endcard={"title":"Full top 10 on the <em>channel</em>","subtitle":"SA's 10 biggest companies on the JSE","handle":"@MzansiMoneyMatters",
          "voiceover":"Full top ten on Mzansi Money Matters.","duration":3500},
 youtube={"title":"Capitec vs Naspers: R2 billion apart #shorts","privacy":"private","synthetic_media":True,"category_id":"27",
  "tags":["Capitec","Naspers","JSE","Mzansi Money Matters"],
  "description":"Capitec edged past Naspers as South Africa's most valuable homegrown company on the JSE, closing prices Friday 6 November 2026. Full top 10 on Mzansi Money Matters.\n\n" + SOURCES +
   "\n\nEducation, not financial advice. Narration is AI-generated. Stock footage from Pexels."})

json.dump(long, open("content-jse10.json","w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-jse10.json","w"), ensure_ascii=False, indent=2)
for name, d in (("long", long), ("short", short)):
    print(name, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"])/60000))
print("top-ten total R%dbn" % total_bn)
