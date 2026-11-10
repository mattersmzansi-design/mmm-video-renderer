"""Builds content-top10.json (long video) and content-short-top10.json (Short):
the 10 largest companies in the world by market value, early November 2026.

Market values: TradingView world's largest companies, early November 2026.
Staff numbers: latest annual reports (10-K/annual filings) as cited per company.
Durations are estimates for preview only; voice.py recalculates them.
"""
import json

def est(vo):
    return int(len(vo.split()) / 155 * 60000) + 1300

# rank, name, hq, value_short, value_spoken, founders_line, founders_vo, year,
# industry_head, industry_vo, staff_value, staff_label, staff_vo, known_head, known_body, known_vo, broll
C = [
 dict(rank=10, name="Broadcom", hq="Palo Alto, USA", mv="$1.57tn", mv_vo="about one point five seven trillion dollars",
      founded="1961 roots in HP. Broadcom name from 1991.", year="1961",
      founders_vo="Its roots go back to Hewlett-Packard's chip division in nineteen sixty-one, which became Avago. The Broadcom name comes from a company Henry Samueli and Henry Nicholas founded in nineteen ninety-one. Avago bought it in twenty sixteen and took the name.",
      ind="Chips and software for data centres",
      ind_vo="Broadcom designs the networking and custom AI chips inside the world's data centres, and since buying VMware it's also a major software company.",
      staff="33,000", staff_l="Employees, end of 2025", staff_vo="It does all this with about thirty-three thousand employees.",
      kh="The quiet giant of AI", kb="It helps big tech firms design their own AI chips.",
      kvo="Most people have never heard of Broadcom, yet it helps companies like Google build their own artificial intelligence chips. That's why its value has soared.",
      broll="data center server racks"),
 dict(rank=9, name="Meta Platforms", hq="Menlo Park, USA", mv="$1.6tn", mv_vo="about one point six trillion dollars",
      founded="2004: Mark Zuckerberg and four Harvard roommates", year="2004",
      founders_vo="Mark Zuckerberg started Facebook in two thousand and four from his Harvard dorm room, with Eduardo Saverin, Andrew McCollum, Dustin Moskovitz and Chris Hughes. The company renamed itself Meta in twenty twenty-one.",
      ind="Social media and online advertising",
      ind_vo="Meta owns Facebook, Instagram, WhatsApp and Threads, and makes almost all of its money from advertising.",
      staff="78,865", staff_l="Employees, end of 2025", staff_vo="It employs just under seventy-nine thousand people.",
      kh="Over 3.5 billion people a day", kb="Use at least one Meta app daily, including WhatsApp.",
      kvo="More than three and a half billion people use at least one of its apps every single day. If you've sent a WhatsApp today, you're one of them.",
      broll="scrolling social media on phone"),
 dict(rank=8, name="Saudi Aramco", hq="Dhahran, Saudi Arabia", mv="$1.65tn", mv_vo="about one point six five trillion dollars",
      founded="1933 oil concession. Fully Saudi-owned by 1980.", year="1933",
      founders_vo="Aramco began in nineteen thirty-three, when the Saudi government granted an oil concession to an American company, Standard Oil of California. The Saudi state took full ownership by nineteen eighty.",
      ind="Oil and gas",
      ind_vo="It's the world's biggest oil producer, and for years one of the most profitable companies on earth. The Saudi government still owns the vast majority of it.",
      staff="75,000+", staff_l="Employees, over 90 nationalities", staff_vo="Aramco employs more than seventy-five thousand people from over ninety nationalities.",
      kh="The only non-tech giant in the top 10", kb="Its 2019 listing was the world's biggest, until SpaceX.",
      kvo="It's the only company in the top ten that isn't a technology business. Its twenty nineteen stock market listing was the biggest in history, until this year.",
      broll="oil refinery at dusk"),
 dict(rank=7, name="TSMC", hq="Hsinchu, Taiwan", mv="$1.9tn", mv_vo="about one point nine trillion dollars",
      founded="1987: Morris Chang", year="1987",
      founders_vo="Taiwan Semiconductor Manufacturing Company was founded in nineteen eighty-seven by Morris Chang, with backing from the Taiwanese government.",
      ind="Making chips for other companies",
      ind_vo="TSMC doesn't sell its own brand. It manufactures chips designed by others, including Apple and Nvidia.",
      staff="83,825", staff_l="Employees, latest annual report", staff_vo="It has nearly eighty-four thousand employees.",
      kh="The factory behind your phone", kb="It makes most of the world's most advanced chips.",
      kvo="The chip in your phone was very likely made by TSMC. It makes most of the world's most advanced processors, which is why it matters so much to global politics.",
      broll="semiconductor wafer"),
 dict(rank=6, name="SpaceX", hq="Starbase, Texas, USA", mv="$2.0tn", mv_vo="about two trillion dollars",
      founded="2002: Elon Musk", year="2002",
      founders_vo="Elon Musk founded Space Exploration Technologies in two thousand and two, with the goal of cutting the cost of getting to space.",
      ind="Rockets and satellite internet",
      ind_vo="SpaceX launches most of the world's rockets, and its Starlink satellites now sell internet to more than twelve million customers in over a hundred and sixty countries.",
      staff="22,000+", staff_l="Employees, at its 2026 listing", staff_vo="It has more than twenty-two thousand employees.",
      kh="The biggest stock market listing ever", kb="It listed on Nasdaq in June 2026, valued at about $2 trillion.",
      kvo="SpaceX only joined the stock market in June twenty twenty-six, in the biggest listing in history. It went straight into the top ten.",
      broll="rocket launch"),
 dict(rank=5, name="Amazon", hq="Seattle, USA", mv="$2.7tn", mv_vo="about two point seven trillion dollars",
      founded="1994: Jeff Bezos, in a garage", year="1994",
      founders_vo="Jeff Bezos founded Amazon in nineteen ninety-four, in a garage outside Seattle, as an online bookshop.",
      ind="Online shopping and cloud computing",
      ind_vo="Amazon is the world's biggest online store, but most of its profit comes from Amazon Web Services, the cloud computers that run much of the internet.",
      staff="1.58m", staff_l="Employees, end of 2025", staff_vo="It employs about one point five eight million people, more than any other company on this list.",
      kh="Now shipping in South Africa", kb="Amazon.co.za launched in 2024.",
      kvo="And it's close to home. Amazon launched its South African store in twenty twenty-four, and its cloud has run a data centre region in Cape Town since twenty twenty.",
      broll="warehouse boxes conveyor"),
 dict(rank=4, name="Alphabet", hq="Mountain View, USA", mv="$3.9tn", mv_vo="about three point nine trillion dollars",
      founded="1998: Larry Page and Sergey Brin", year="1998",
      founders_vo="Larry Page and Sergey Brin founded Google in nineteen ninety-eight, while they were PhD students at Stanford. Alphabet was created in twenty fifteen as the parent company.",
      ind="Search, advertising, YouTube and cloud",
      ind_vo="Alphabet owns Google Search, Android, Google Cloud, and YouTube, and it earns most of its money from advertising.",
      staff="190,800", staff_l="Employees, end of 2025", staff_vo="It has around one hundred and ninety thousand employees.",
      kh="You're on its platform right now", kb="Google bought YouTube in 2006.",
      kvo="And if you're watching this on YouTube, you're using one of its products right now. Google bought YouTube in two thousand and six.",
      broll="typing on laptop search"),
 dict(rank=3, name="Microsoft", hq="Redmond, USA", mv="$4.0tn", mv_vo="about four trillion dollars",
      founded="1975: Bill Gates and Paul Allen", year="1975",
      founders_vo="Childhood friends Bill Gates and Paul Allen founded Microsoft in nineteen seventy-five.",
      ind="Software and cloud computing",
      ind_vo="Microsoft makes Windows and Office, and runs Azure, one of the world's biggest cloud platforms. It's also a major investor in OpenAI.",
      staff="223,000", staff_l="Employees, mid-2026", staff_vo="It employs about two hundred and twenty-three thousand people.",
      kh="On almost every office computer", kb="Its products are sold in more than 190 countries.",
      kvo="Its software runs on almost every office computer in the world, and it sells in more than one hundred and ninety countries.",
      broll="office computers work"),
 dict(rank=2, name="Apple", hq="Cupertino, USA", mv="$5.0tn", mv_vo="about five trillion dollars",
      founded="1976: Steve Jobs, Steve Wozniak, Ronald Wayne", year="1976",
      founders_vo="Steve Jobs, Steve Wozniak and Ronald Wayne founded Apple in nineteen seventy-six. Wayne sold his ten percent share just days later, for eight hundred dollars.",
      ind="Phones, computers and services",
      ind_vo="Apple makes the iPhone, Mac, iPad and Apple Watch, and earns a fast-growing share of its money from services like the App Store and iCloud.",
      staff="166,000", staff_l="Employees, 2025 annual report", staff_vo="It has about one hundred and sixty-six thousand employees.",
      kh="First to a trillion dollars", kb="The first US company worth $1 trillion, in 2018.",
      kvo="Apple was the first American company to be worth a trillion dollars, in twenty eighteen. It and Nvidia now swap the number one spot almost week to week.",
      broll="smartphone close up"),
 dict(rank=1, name="Nvidia", hq="Santa Clara, USA", mv="$5.2tn", mv_vo="about five point two trillion dollars",
      founded="1993: Jensen Huang, Chris Malachowsky, Curtis Priem", year="1993",
      founders_vo="Jensen Huang, Chris Malachowsky and Curtis Priem founded Nvidia in nineteen ninety-three. They planned it over meals at a roadside diner.",
      ind="Chips that power artificial intelligence",
      ind_vo="Nvidia started out making graphics chips for video games. Today its processors power most of the world's artificial intelligence.",
      staff="42,000", staff_l="Employees in 38 countries", staff_vo="It has about forty-two thousand employees in thirty-eight countries.",
      kh="First company worth $5 trillion", kb="It crossed $5 trillion in October 2025.",
      kvo="In October twenty twenty-five, Nvidia became the first company ever worth five trillion dollars. That's about twelve times the size of South Africa's entire economy.",
      broll="computer chip circuit board"),
]

scenes = [
 {"type":"intro","eyebrow":"Early November 2026","headline":"The 10 most valuable companies on earth",
  "body":"Nvidia. Apple. Microsoft. SpaceX. Aramco. And five more.",
  "voiceover":"Ten companies on earth are each worth more than one and a half trillion dollars."},
 {"type":"broll","broll":"stock market trading screen","eyebrow":"Put in perspective","headline":"Together: about $30 trillion",
  "voiceover":"Together, they're worth about thirty trillion dollars. That's roughly ten times the size of Africa's entire economy. Here they are, counted down from ten to one."},
 {"type":"plain","eyebrow":"How we ranked them","headline":"By market value: share price × shares.",
  "body":"Values as at early November 2026. They move every day.",
  "voiceover":"We ranked them by market value, which is the share price multiplied by the number of shares. These figures are from early November twenty twenty-six, and they change every day. For each one: where it's based, who founded it, what it does, and what it's known for."},
]
for c in C:
    r, nm = c["rank"], c["name"]
    scenes += [
     {"type":"rank","rank":r,"eyebrow":c["hq"],"headline":nm,
      "voiceover":f"Number {['','one','two','three','four','five','six','seven','eight','nine','ten'][r]}. {nm.replace('TSMC','T S M C')}. Based in {c['hq'].replace(', USA',', in the United States')}."},
     {"type":"point","rank":r,"name":nm,"eyebrow":"Market value","headline":f"Worth {c['mv_vo'].replace('about ','about ').split(' trillion')[0].replace('about ','about $').replace('one point five seven','1.57').replace('one point six five','1.65').replace('one point six','1.6').replace('one point nine','1.9').replace('two point seven','2.7').replace('three point nine','3.9').replace('five point two','5.2').replace('two','2').replace('four','4').replace('five','5')} trillion",
      "stat":{"value":c["mv"],"label":"Market value, early November 2026"},
      "voiceover":f"Market value: {c['mv_vo']}."},
     {"type":"point","rank":r,"name":nm,"eyebrow":f"Founded {c['year']}","headline":c["founded"],
      "voiceover":c["founders_vo"]},
     {"type":"point","rank":r,"name":nm,"eyebrow":"What it does","headline":c["ind"],
      "stat":{"value":c["staff"],"label":c["staff_l"]},
      "voiceover":c["ind_vo"]+" "+c["staff_vo"]},
     {"type":"broll","broll":c["broll"],"eyebrow":"Known for","headline":c["kh"],"body":c["kb"],
      "voiceover":c["kvo"]},
    ]
scenes += [
 {"type":"plain","eyebrow":"The pattern","headline":"Eight of the ten are American tech companies.",
  "voiceover":"Notice the pattern. Eight of the ten are American, and nine of them are technology businesses. The only oil company left is Aramco. Twenty years ago, this list was full of oil companies and banks."},
 {"type":"plain","eyebrow":"Just outside the top 10","headline":"Tesla, Eli Lilly and Berkshire Hathaway",
  "voiceover":"Just missing out: Tesla, only a few billion dollars behind Broadcom, followed by Eli Lilly and Warren Buffett's Berkshire Hathaway. With prices moving every day, this list could look different by next month."},
 {"type":"plain","eyebrow":"Your turn","headline":"Which company will be number one next year?",
  "voiceover":"So which company do you think will be number one this time next year? Tell us in the comments."},
]
for s in scenes:
    s["duration"] = est(s["voiceover"])

base = {
 "template":"template-countdown.html",
 "brand":{"name":"Mzansi Money Matters","logo":"logo.jpg"},
 "voice":{"name":"en-US-BrianMultilingualNeural","rate":"+4%","pitch":"+0Hz","lead_pad":400,"tail_pad":900},
 "timing":{"lead_in":900},
}
long = dict(base, thumbnail={"kicker": "World's biggest", "big": "$5.2tn", "line": "One company. <em>12× SA's economy.</em>", "photo": "computer chip circuit board"}, slug="top10-largest-companies-2026", countdown={"from":10},
 disclaimer="Education, not financial advice. Market values as at early November 2026.",
 scenes=scenes,
 endcard={"title":"Subscribe for the <em>next</em> ten","subtitle":"South African money, explained.","handle":"@MzansiMoneyMatters","duration":5000},
 youtube={"title":"The 10 Most Valuable Companies in the World (2026)","privacy":"private","synthetic_media":True,"category_id":"27",
  "tags":["largest companies","market cap","Nvidia","Apple","Microsoft","SpaceX","Saudi Aramco","Mzansi Money Matters"],
  "description":("The 10 most valuable companies in the world by market value, as at early November 2026: where they're based, who founded them, "
   "what they do, how many people they employ, and what they're known for. Nvidia alone is worth about 12 times South Africa's economy.\n\n"
   "{chapters}\n\nSources: market values from TradingView (early November 2026); employee numbers from each company's latest annual report; "
   "South Africa GDP from Trading Economics / World Bank (2025).\n\nEducation, not financial advice. Narration and some visuals are AI-generated. Stock footage from Pexels.")})

# Short: quick-fire 10 to 1
q = [{"type":"broll","broll":"city skyline night timelapse","eyebrow":"Early November 2026",
      "headline":"The world's 10 most valuable companies in 60 seconds",
      "voiceover":"The ten most valuable companies on earth, in sixty seconds. Go."}]
for c in C:
    q.append({"type":"point","rank":c["rank"],"name":c["name"],"eyebrow":c["hq"],"headline":c["name"],
              "stat":{"value":c["mv"],"label":"Market value"},
              "voiceover":f"{['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten'][c['rank']]}: {c['name'].replace('TSMC','T S M C').replace('Meta Platforms','Meta')}, {c['mv_vo'].replace('about ','')}."})
q.append({"type":"plain","eyebrow":"Put in perspective","headline":"Nvidia is worth about 12× South Africa's economy.",
          "voiceover":"Nvidia alone is worth about twelve times South Africa's entire economy."})
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-top10-companies", size=[1080,1920], countdown={"from":10},
 disclaimer="Education, not financial advice.",
 voice={"name":"en-US-BrianMultilingualNeural","rate":"+6%","pitch":"+0Hz","lead_pad":200,"tail_pad":400},
 timing={"lead_in":500}, scenes=q,
 endcard={"title":"Full breakdown on the <em>channel</em>","subtitle":"Founders, staff and what each one does","handle":"@MzansiMoneyMatters",
          "voiceover":"Full breakdown on Mzansi Money Matters.","duration":3500},
 youtube={"title":"The world's 10 most valuable companies in 60 seconds #shorts","privacy":"private","synthetic_media":True,"category_id":"27",
  "tags":["largest companies","market cap","Nvidia","Apple","Mzansi Money Matters"],
  "description":"The 10 most valuable companies in the world, early November 2026. Nvidia alone is worth about 12 times South Africa's economy. Full breakdown on Mzansi Money Matters.\n\nEducation, not financial advice. Narration is AI-generated. Stock footage from Pexels."})

json.dump(long, open("content-top10.json","w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-top10.json","w"), ensure_ascii=False, indent=2)
for name, d in (("long", long), ("short", short)):
    print(name, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"])/60000))
for s in scenes:
    if s.get("eyebrow")=="Market value": print("  ", s["headline"])
