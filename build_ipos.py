"""Builds content-ipos.json (long video) and content-short-ipos.json (Short):
"The 10 Biggest IPOs in History (2026): SpaceX, Anthropic, Aramco & More", following the LLM-council verdict of 24 Nov 2026.
Rule: Renaissance Capital base deal size (no over-allotment, nominal USD). Both option totals are shown (SpaceX ~$86bn exercised;
Anthropic up to ~$93.5bn, option pending).
CONFLICT OF INTEREST: researched with Claude (made by Anthropic, #1 here). Safeguards: identical template and similar length per entry,
no praise adjectives, Anthropic's unflattering open-vs-close fact included, disclosure spoken + on screen + in the description,
and a thumbnail with no company names or numbers.
Clips: assets/broll/ipo-XX.mp4 (owner's Google Flow clips, Veo 3.1 Fast, 16:9); the Short pads them into 9:16.
Narrator: Kokoro bf_emma.
"""
import json

def est(vo):
    return int(len(vo.split()) / 150 * 60000) + 1300

W = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
RC = "Renaissance Capital, All Time Largest Global IPOs (base deal size)"
DISC = "Research assisted by Claude, an AI made by Anthropic, which appears in this list. Ranking follows Renaissance Capital's published rule."

def amt(v, label):
    return {"value": f"${v}bn", "label": label, "count": {"from": 0, "to": float(v), "decimals": 1 if v != "81.34" else 2, "prefix": "$", "suffix": "bn"}}

# r, name, where/when, clip, what (vo, head), money (vo), stat, receipt, extra receipt
C = [
 dict(r=10, name="Enel", tag="Italy · 1999 · Milan & NYSE", clip="ipo-02-power-lines.mp4",
      head="Italy sells its power company",
      what="Enel. It's basically Italy selling shares in its state electricity company, in November nineteen ninety-nine.",
      money="It raised sixteen and a half billion dollars, and a record three point eight million Italians signed up to buy shares. But the first day of trading was weak.",
      st=amt("16.5", "Nov 1999"), src=f"{RC}; CNN Money (Nov 1999)"),
 dict(r=9, name="AIA", tag="Hong Kong · 2010", clip="ipo-03-harbour.mp4",
      head="An insurer born from a crisis",
      what="AIA, an Asian life insurer. It was spun out of the American insurer AIG, which had to sell assets after the two thousand and eight financial crisis.",
      money="It raised seventeen point eight billion dollars in Hong Kong in October twenty ten, and set a record for the most shares of one company traded on that exchange's first day.",
      st=amt("17.8", "Oct 2010"), src=f"{RC}; HKEX statistics (29 Oct 2010)"),
 dict(r=8, name="Visa", tag="USA · 2008 · NYSE", clip="ipo-04-card.mp4",
      head="A payments giant, mid-crisis",
      what="Visa, the card payments network. It went public in March two thousand and eight, right in the middle of the financial crisis.",
      money="It raised seventeen point nine billion dollars. Priced at forty-four dollars a share, it closed its first day at fifty-six fifty, up about twenty-eight percent.",
      st=amt("17.9", "Mar 2008"), src=f"{RC}; vivid.money; ValueWalk"),
 dict(r=7, name="NTT DoCoMo", tag="Japan · 1998 · Tokyo", clip="ipo-05-flip-phones.mp4",
      head="Japan's mobile phone pioneer",
      what="NTT DoCoMo, Japan's biggest mobile network, split off from the national phone company. It listed in Tokyo in October nineteen ninety-eight.",
      money="It raised eighteen point one billion dollars and rose nineteen percent on its first day. In twenty twenty, its parent company NTT took it private again.",
      st=amt("18.1", "Oct 1998"), src=f"{RC}; Goldman Sachs; The Motley Fool"),
 dict(r=6, name="SoftBank Corp", tag="Japan · 2018 · Tokyo", clip="ipo-06-telecom-towers.mp4",
      head="A telecom giant's rough start",
      what="SoftBank Corp, the Japanese mobile phone business of the SoftBank group. It listed in Tokyo in December twenty eighteen.",
      money="It raised twenty-one point three billion dollars, but its shares fell fourteen and a half percent on the first day.",
      st=amt("21.3", "Dec 2018"), src=f"{RC}; TechCrunch"),
 dict(r=5, name="Alibaba", tag="China · 2014 · NYSE", clip="ipo-07-parcels.mp4",
      head="China's online shopping giant",
      what="Alibaba, China's online shopping giant. It listed in New York in September twenty fourteen.",
      money="It raised twenty-one point eight billion dollars at sixty-eight dollars a share, and jumped thirty-eight percent on day one. With extra shares sold later, the total reached twenty-five billion.",
      st=amt("21.8", "Sep 2014 · $25bn with extra shares"), src=f"{RC}; Fortune; Bloomberg"),
 dict(r=4, name="Saudi Aramco", tag="Saudi Arabia · 2019 · Riyadh", clip="ipo-08-pumpjacks.mp4",
      head="The world's biggest oil company",
      what="Saudi Aramco, the Saudi state oil company. It listed on the Riyadh exchange in December twenty nineteen.",
      money="It raised twenty-five point six billion dollars and rose ten percent on day one, the most the exchange allows in one day. With extra shares, the total reached twenty-nine point four billion.",
      st=amt("25.6", "Dec 2019 · $29.4bn with extra shares"), src=f"{RC}; Fortune; Anadolu Agency"),
 dict(r=3, name="SK hynix", tag="South Korea · 2026 · Nasdaq", clip="ipo-09-wafer.mp4",
      head="The memory chips behind AI",
      what="SK hynix, a South Korean maker of the memory chips used in AI computers. It listed in New York in July twenty twenty-six.",
      money="It raised twenty-six point five billion dollars, the biggest US listing ever by a foreign company, and closed its first day up about thirteen percent.",
      st=amt("26.5", "Jul 2026"), src=f"{RC}; IPOScoop; The Motley Fool"),
 dict(r=2, name="SpaceX", tag="USA · 2026 · Nasdaq", clip="ipo-10-rocket.mp4",
      head="Rockets, satellites and AI",
      what="SpaceX, the rocket and satellite company that also owns the AI firm x A I. It listed in June twenty twenty-six, at one hundred and thirty-five dollars a share.",
      money="It raised seventy-five billion dollars and closed day one up nineteen percent. With extra shares sold later, it reached about eighty-six billion, which would make it number one on that measure. It also reported a four point three billion dollar loss in early twenty twenty-six.",
      st=amt("75.0", "Jun 2026 · ~$86bn with extra shares"), src=f"{RC}; NPR; Al Jazeera; Dealroom"),
 dict(r=1, name="Anthropic", tag="USA · 2026 · Nasdaq", clip="ipo-11-data-centre.mp4",
      head="The AI company behind Claude",
      what="Anthropic, the AI company that makes the Claude assistant. It listed in November twenty twenty-six, selling nine hundred and eighty million shares at eighty-three dollars each.",
      money="It raised eighty-one point three four billion dollars. Its shares opened at one hundred and eleven fifty, but closed the day at ninety-seven seventeen. An option for its banks to sell up to one hundred and forty-seven million more shares is still pending. If fully used, about ninety-three and a half billion.",
      st=amt("81.34", "Nov 2026 · up to ~$93.5bn if option used"), src=f"{RC}; Anthropic press release (18 Nov 2026); CNBC"),
]

scenes = [
 {"type": "broll", "broll": "ipo-01-trading-hall.mp4", "eyebrow": "Biggest IPOs in history", "headline": "2026 rewrote the record books",
  "voiceover": "In twenty twenty-six, three companies broke into the top three biggest IPOs of all time. And who's number one depends on how you count. An IPO is when a company sells pieces of itself to the public for the first time. Here are the ten biggest ever."},
 {"type": "plain", "eyebrow": "Disclosure", "headline": "Researched with help from Claude, an AI made by Anthropic",
  "body": "Anthropic appears in this list. Ranking follows Renaissance Capital's published rule, and every company gets the same treatment.",
  "voiceover": "A quick disclosure: this video was researched with help from Claude, an AI made by Anthropic, which appears in this list. So we use a published ranking rule and give every company the same treatment."},
 {"type": "plain", "eyebrow": "How we ranked them", "headline": "Money raised when the IPO was priced",
  "body": "Renaissance Capital's rule: not counting extra shares banks may sell later. US dollars at the time, not adjusted for inflation.",
  "receipt": RC,
  "voiceover": "The rule: we rank by the money raised when each IPO was priced, as listed by Renaissance Capital. That doesn't count extra shares that banks can sell afterwards, and it's in dollars at the time, not adjusted for inflation. We'll show the extra-share totals too, where they matter."},
]
for c in C:
    scenes.append({"type": "rank", "rank": c["r"], "eyebrow": c["tag"], "headline": c["name"], "voiceover": f"Number {W[c['r']]}."})
    scenes.append({"type": "broll", "broll": c["clip"], "rank": c["r"], "eyebrow": c["tag"], "headline": c["head"],
                   "receipt": DISC if c["r"] == 1 else None, "voiceover": c["what"]})
    scenes.append({"type": "point", "rank": c["r"], "name": c["name"], "eyebrow": "Raised at IPO", "headline": c["name"],
                   "stat": c["st"], "receipt": c["src"], "voiceover": c["money"]})
for s in scenes:
    if s.get("receipt") is None:
        s.pop("receipt", None)

scenes += [
 {"type": "chart", "eyebrow": "Raised at IPO, US$ billions · Renaissance Capital", "headline": "Then 2026 happened",
  "chart": {"kind": "bar", "labels": ["Enel", "AIA", "Visa", "DoCoMo", "SoftBank", "Alibaba", "Aramco", "SK hynix", "SpaceX", "Anthropic"],
            "values": [16.5, 17.8, 17.9, 18.1, 21.3, 21.8, 25.6, 26.5, 75.0, 81.34],
            "display": ["16.5", "17.8", "17.9", "18.1", "21.3", "21.8", "25.6", "26.5", "75.0", "81.3"], "highlight": [8, 9]},
  "voiceover": "Put them side by side, and you can see it. For decades, the record sat between about sixteen and twenty-six billion dollars. Then two companies in twenty twenty-six raised around three times that."},
 {"type": "plain", "eyebrow": "The lesson", "headline": "A first-day jump isn't your gain",
  "body": "Most people can't buy at the IPO price. They buy when trading opens.",
  "receipt": "Anthropic: opened $111.50, closed $97.17 on 19 Nov 2026 (CNBC)",
  "voiceover": "One lesson. Most ordinary investors don't get the IPO price. They buy when trading opens. Anyone who bought Anthropic at the one hundred and eleven fifty opening price was about thirteen percent down by the close. A first-day jump isn't your gain."},
 {"type": "broll", "broll": "ipo-12-bell.mp4", "eyebrow": "What's next", "headline": "OpenAI could be next",
  "receipt": "CNBC (reported 2027 plan); GovInfoSecurity",
  "voiceover": "And what's next? OpenAI delayed its own IPO, and CNBC reports a plan to list in twenty twenty-seven. This video is education, not investment advice. Which IPO surprised you most? Tell us in the comments."},
]
for s in scenes:
    s["duration"] = est(s["voiceover"])
bell_idx = len(scenes) - 1

EMMA = {"engine": "kokoro", "name": "bf_emma", "speed": 1.05, "lang": "en-gb", "lead_pad": 400, "tail_pad": 900}
base = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
        "voice": EMMA, "timing": {"lead_in": 900}}

SOURCES = """Ranking: Renaissance Capital, "All Time Largest Global IPOs by Deal Size" (deal size excludes underwriter over-allotment; nominal US dollars).
1 Anthropic: Anthropic press release "Anthropic prices initial public offering" (18 Nov 2026: 980,000,000 shares at $83; 30-day underwriter option for up to 147,000,000 additional shares); first-day open $111.50 and close $97.17 (Nasdaq/CNBC); ~$1.5T valuation (Al Jazeera/AP); ~$93.5bn if the option is fully exercised (techi.com estimate).
2 SpaceX: NPR (11–12 Jun 2026: $75bn, $135/share, first-day close $160.95, Q1 2026 net loss $4.3bn); Al Jazeera/Dealroom (~$85.7–86.2bn after additional shares).
3 SK hynix: IPOScoop (9–10 Jul 2026: $26.51bn at $149/ADS; first-day close $168.01); The Motley Fool (largest US listing by a foreign company).
4 Saudi Aramco: Fortune (11 Dec 2019: +10% first day); Anadolu Agency ($29.4bn including greenshoe).
5 Alibaba: Fortune/Bloomberg (Sep 2014: $68, +38% first day; $25bn including greenshoe).
6 SoftBank Corp: TechCrunch (Dec 2018: −14.5% first day).
7 NTT DoCoMo: Goldman Sachs (Oct 1998: +19% first day); The Motley Fool (taken private 2020).
8 Visa: vivid.money/ValueWalk (Mar 2008: $44 IPO price, $56.50 first-day close).
9 AIA: HKEX statistics (29 Oct 2010: record first-day turnover for a single company); spin-off from AIG (G2/Investopedia).
10 Enel: CNN Money (Nov 1999: weak debut; 3.8 million Italians signed up).
OpenAI: CNBC via Alhurra (reported 2027 IPO plan); GovInfoSecurity (IPO delayed)."""

long = dict(base, slug="biggest-ipos-in-history", countdown={"from": 10},
 disclaimer="Education, not investment advice. Researched with Claude (made by Anthropic, #1 in this list).",
 thumbnail={"kicker": "10 biggest IPOs ever", "big": "WHO'S #1?", "line": "It depends <em>how you count</em>", "frame": bell_idx},
 scenes=scenes,
 endcard={"title": "Biggest IPOs <em>ever</em>", "subtitle": "Subscribe for money, explained.", "handle": "@MzansiMoneyMatters", "duration": 15000},
 youtube={"title": "The 10 Biggest IPOs in History (2026): SpaceX, Anthropic, Aramco & More", "privacy": "private",
  "synthetic_media": True, "category_id": "27",
  "tags": ["biggest IPO", "biggest IPOs in history", "largest IPO in history", "largest IPO ever", "SpaceX IPO", "Anthropic IPO",
           "Saudi Aramco IPO", "Alibaba IPO", "SK hynix IPO", "IPO explained", "Mzansi Money Matters"],
  "description": ("Disclosure: this video was researched with help from Claude, an AI made by Anthropic, which appears in this list. "
   "The ranking follows Renaissance Capital's published rule, and every company gets the same treatment.\n\n"
   "The 10 biggest IPOs in history, from Enel in 1999 to SpaceX and Anthropic in 2026: how much each raised, how the first day went, "
   "and who's really #1 depending on how you count.\n\n{chapters}\n\n" + SOURCES +
   "\n\n#BiggestIPO #IPO #SpaceX #Anthropic #MzansiMoneyMatters\n\nEducation, not investment advice. Narration is AI-generated. "
   "Video clips were generated with Google Flow (Veo).")})

q = [
 {"type": "broll", "broll": "ipo-12-bell.mp4", "eyebrow": "Biggest IPO ever?", "headline": "SpaceX or Anthropic?",
  "voiceover": "Who had the biggest IPO in history? SpaceX, or Anthropic?"},
 {"type": "point", "eyebrow": "Raised when priced", "headline": "Anthropic $81.3bn · SpaceX $75.0bn",
  "stat": {"value": "$81.3bn", "label": "Anthropic, Nov 2026 · SpaceX $75.0bn, Jun 2026", "count": {"from": 0, "to": 81.3, "decimals": 1, "prefix": "$", "suffix": "bn"}},
  "receipt": "Renaissance Capital",
  "voiceover": "Count the money raised when the shares were priced, and it's Anthropic, at eighty-one billion, ahead of SpaceX at seventy-five."},
 {"type": "point", "eyebrow": "With extra shares", "headline": "SpaceX ~$86bn · Anthropic up to ~$93.5bn",
  "stat": {"value": "~$86bn", "label": "SpaceX, after extra shares · Anthropic's option still pending", "count": {"from": 0, "to": 86, "decimals": 0, "prefix": "~$", "suffix": "bn"}},
  "receipt": "Al Jazeera; Anthropic press release (147M-share option)",
  "voiceover": "But add the extra shares banks sold later, and SpaceX reached about eighty-six billion. Anthropic's own option, worth up to about ninety-three billion in total, is still pending."},
 {"type": "plain", "eyebrow": "So who's #1?", "headline": "It depends how you count",
  "body": "Researched with Claude, an AI made by Anthropic. Education, not investment advice.",
  "voiceover": "So who's number one? It depends how you count. Full top ten on our channel."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-spacex-vs-anthropic-ipo", size=[1080, 1920], countdown={"from": 10}, broll_fit="pad",
 disclaimer="Education, not investment advice. Researched with Claude (made by Anthropic).",
 voice=dict(EMMA, lead_pad=300, tail_pad=600), timing={"lead_in": 600}, scenes=q,
 endcard={"title": "Who's <em>#1</em>?", "subtitle": "10 biggest IPOs, sources included", "handle": "@MzansiMoneyMatters",
          "voiceover": "Watch the full top ten on Mzansi Money Matters.", "duration": 3500},
 youtube={"title": "SpaceX or Anthropic: who had the biggest IPO? #shorts", "privacy": "private", "synthetic_media": True,
  "category_id": "27", "tags": ["biggest IPO", "SpaceX IPO", "Anthropic IPO", "largest IPO ever", "Mzansi Money Matters"],
  "description": "Anthropic raised $81.34bn when its IPO was priced (Nov 2026), and SpaceX $75bn (Jun 2026) (Renaissance Capital). With extra shares, SpaceX reached ~$86bn (Al Jazeera); Anthropic's option for up to 147M more shares is pending (Anthropic press release). It depends how you count.\n\nDisclosure: researched with Claude, an AI made by Anthropic.\n\n#BiggestIPO #Shorts\n\nEducation, not investment advice. Narration is AI-generated. Clips generated with Google Flow (Veo)."})

json.dump(long, open("content-ipos.json", "w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-ipos.json", "w"), ensure_ascii=False, indent=2)
for n, d in (("long", long), ("short", short)):
    print(n, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"]) / 60000))
# equal-treatment check: words per entry
for c in C:
    print(f"#{c['r']:>2} {c['name']:<14} {len((c['what'] + ' ' + c['money']).split())} words")
