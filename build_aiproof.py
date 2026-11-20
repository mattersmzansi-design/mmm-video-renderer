"""Builds content-aiproof.json (long video) and content-short-aiproof.json (Short):
"Jobs AI Can't Easily Replace: 10 Businesses You Can Start in South Africa", following the LLM-council verdict of 21 Nov 2026.
Order: each business takes its position on Microsoft Research's 2025 list of the 40 US jobs where AI chatbots apply least
(lowest position = our #1); a business that combines two jobs takes its lower position.
Beat 1: why AI struggles (source: Microsoft row). Beat 2: what you need first (official SA source only if verified,
otherwise an "MMM starter checklist"). Beat 3: how AI can still help (MMM suggestion, not a study).
Excluded on purpose: home-based care, funeral services, asbestos removal, water refill. Cleaning is framed as private homes.
Footage: the owner's Google Flow clips (Veo 3.1 Fast, 16:9) in assets/broll/aiproof-*.mp4; the Short pads them (blurred background).
Narrator: Kokoro bf_emma.
"""
import json

def est(vo):
    return int(len(vo.split()) / 150 * 60000) + 1300

W = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
MS = "Microsoft Research, 'Working with AI' (2025 pre-print), US data"
CHECK = "MMM starter checklist, not a study"
SUGG = "MMM suggestion, not a study"

# r, name, rows (display), row (rank key), clip, clip start for beat 3, why (vo, head), need (vo, head, receipt), ai (vo, head)
C = [
 dict(r=10, name="Painting & plastering", rows="#37", row=37, clip="aiproof-10-painting.mp4",
      why_h="Every wall is different", why="Painting and plastering. On Microsoft's list, helpers to painters and plasterers sit at number thirty-seven. Every wall is different: cracks, damp, old paint, and a client standing next to you. A chatbot can describe a perfect finish, but it can't hold a roller.",
      need_h="Rollers, brushes, a ladder, and a good teacher", need_r=CHECK,
      need="To start, you need rollers, brushes, a ladder and drop sheets. The best way to learn is to work alongside an experienced painter first.",
      ai_h="Let AI work out the paint and the quote", ai="Where AI can help: give it the room sizes, and it can estimate how much paint you need and turn that into a neat written quote."),
 dict(r=9, name="Auto glass fitment", rows="#33", row=33, clip="aiproof-09-autoglass.mp4",
      why_h="Precise, physical, and done on the spot", why="Auto glass fitment. Automotive glass installers are number thirty-three on the list. Lifting a windscreen into a car and sealing it properly is careful, physical work, often done right at the customer's car.",
      need_h="Suction lifters, adhesive, and proper training", need_r=CHECK,
      need="You'd need suction lifters, the right adhesive and proper training in fitting, because a badly fitted windscreen is a safety problem.",
      ai_h="Never miss a WhatsApp booking", ai="AI can help you answer booking messages on WhatsApp quickly, even when your hands are full."),
 dict(r=8, name="Tyre fitment & repair", rows="#31", row=31, clip="aiproof-08-tyres.mp4", start=3,
      why_h="Hands on the wheel, every time", why="Tyre fitment and repair. Tyre repairers and changers come in at number thirty-one. Every car that rolls in needs real hands on the wheel, and no chatbot can fix a puncture.",
      need_h="Tools, and a plan for old tyres", need_r="Waste Tyre Regulations, 2017 (NEM: Waste Act) · gov.za",
      need="You'll need a tyre changer, a wheel balancer and a compressor. And in South Africa, the Waste Tyre Regulations of twenty seventeen set out duties for tyre dealers, including how old tyres must be handled.",
      ai_h="Track stock and get found on Google", ai="AI can help you keep track of your stock, and write your Google business listing so drivers nearby can find you."),
 dict(r=7, name="Forklift operation & hire", rows="#21", row=21, clip="aiproof-07-forklift.mp4",
      why_h="Real loads, real warehouses", why="Forklift operation and hire. Industrial truck and tractor operators, including forklift drivers, are number twenty-one. Moving real loads safely through a busy warehouse is not something a chatbot does.",
      need_h="A certificate from an accredited trainer", need_r="Driven Machinery Regulations, 2015, reg. 18(11) (OHS Act) · acts.co.za",
      need="Here the law is clear. Under South Africa's Driven Machinery Regulations, an operator of a listed lifting machine must hold a certificate of training from an accredited training provider.",
      ai_h="Scheduling and invoices, sorted", ai="AI can help you schedule jobs, and send invoices on time."),
 dict(r=6, name="Massage & spa", rows="#19", row=19, clip="aiproof-06-massage.mp4",
      why_h="Skilled hands and trust", why="Massage and spa. Massage therapists are number nineteen. People pay for skilled hands and a calm, trusted space, which a chatbot can't give them.",
      need_h="Training, and know the rules", need_r="AHPCSA · SAQA professional designation 472",
      need="Get proper training first. And know this: in South Africa, a registered therapeutic massage therapist is a professional registered with the Allied Health Professions Council, the A H P C S A.",
      ai_h="Bookings and reminders on autopilot", ai="AI can help with bookings and appointment reminders, so fewer clients forget to show up."),
 dict(r=5, name="Roofing", rows="#14 & #16", row=14, clip="aiproof-05-roofing.mp4",
      why_h="Up on the roof, in the sun and wind", why="Roofing. Roofers are number fourteen on the list, and their helpers number sixteen. The work happens up on the roof, in the sun and wind, on houses that are all built a little differently.",
      need_h="Safety gear first, then tools", need_r=CHECK,
      need="Start with safety gear for working at heights, then a good drill, ladders and the right fixings.",
      ai_h="Turn photos into neat quotes", ai="AI can help you turn your photos and measurements into a clear, professional quote."),
 dict(r=4, name="Home cleaning", rows="#12", row=12, clip="aiproof-04-cleaning.mp4",
      why_h="Every home is different", why="Home cleaning, for private households. Maids and housekeeping cleaners are number twelve. Every home is different, and the job needs someone physically there, someone the family trusts.",
      need_h="Supplies, reliability and references", need_r=CHECK,
      need="It's one of the cheapest businesses to start: good supplies, reliable transport, and references from happy clients.",
      ai_h="Plan routes and repeat bookings", ai="AI can help you plan the day's route between clients, and manage weekly repeat bookings."),
 dict(r=3, name="Paving & driveways", rows="#11", row=11, clip="aiproof-03-paving.mp4",
      why_h="Heavy, outdoor, site-by-site work", why="Paving and driveways. Paving and surfacing operators are number eleven. Every driveway has its own slope, soil and drainage, and the bricks have to be laid by hand.",
      need_h="A compactor, mallets and a good supplier", need_r=CHECK,
      need="You'll need a plate compactor, rubber mallets, a level, and a reliable supplier for bricks and sand.",
      ai_h="Show clients the pattern first", ai="AI image tools can help you show a client different paving patterns before the first brick goes down."),
 dict(r=2, name="Boat skipper & charter", rows="#9", row=9, clip="aiproof-02-boat.mp4",
      why_h="The sea doesn't follow a script", why="Boat skipper and charter. Motorboat operators are number nine. Weather, tides and passengers change every trip, and someone has to be in charge on the water.",
      need_h="A SAMSA certificate of competence", need_r="SAMSA (South African Maritime Safety Authority) small vessel rules",
      need="This one is regulated. For a commercial vessel in South Africa, the skipper must be over eighteen and hold a suitably endorsed certificate of competence, issued under SAMSA's rules.",
      ai_h="Bookings and forecasts, but you decide", ai="AI can help with bookings and summarise the forecast, but the skipper still makes the call."),
 dict(r=1, name="Floor finishing", rows="#7 & #23", row=7, clip="aiproof-01-floor.mp4",
      why_h="Every floor tells its own story", why="Floor finishing: sanding, screeding and polished concrete. Floor sanders and finishers are number seven on Microsoft's list, the lowest position of any business here, and cement masons and concrete finishers come in at twenty-three. Old wood, uneven concrete, dust and noise: every floor is different, and the finish depends on skilled hands.",
      need_h="A sander, an edger and dust extraction", need_r=CHECK,
      need="You'll need a floor sander, an edger, good dust extraction and a polisher, plus practice on real floors before you charge for it.",
      ai_h="Before-and-after posts that sell", ai="And AI can help you write the before-and-after posts that bring in your next client."),
]

def stat(c):
    return {"value": c["rows"], "label": "of 40 jobs AI applies to least (Microsoft, US)",
            "count": {"from": 40, "to": c["row"], "decimals": 0, "prefix": "#", "suffix": ""}}

scenes = [
 {"type": "broll", "broll": "aiproof-00-opening.mp4", "eyebrow": "Jobs AI can't easily replace", "headline": "ChatGPT can write your CV. It can't fix your roof.",
  "voiceover": "ChatGPT can write your CV. It can't fix your roof. Microsoft researchers studied two hundred thousand real conversations with an AI chatbot, to find the work it helps with the least. We turned that list into ten businesses you can start in South Africa. And number one is something you walk on every day."},
 {"type": "plain", "eyebrow": "How we ranked them", "headline": "Microsoft's 40 US jobs AI chatbots apply to least",
  "body": "Lowest position = our #1. Two-job businesses take the lower position. Hard to replace, not impossible.",
  "receipt": "Microsoft Research, 'Working with AI' (July 2025 pre-print), US data",
  "voiceover": "Here's how we ranked them. Microsoft listed the forty American jobs where AI chatbots apply the least. Our order follows each job's position on that list. It's a twenty twenty-five study that hasn't been peer reviewed yet, using US data, and the researchers say every kind of work has some exposure to AI. So think of these as hard to replace, not impossible."},
]
for c in C:
    if c["r"] == 1:
        scenes.append({"type": "plain", "eyebrow": "Before number one", "headline": "Why aren't plumbers and electricians here?",
                       "body": "They're not in Microsoft's bottom 40. That doesn't mean AI can do their jobs. They just weren't among the very lowest.",
                       "receipt": MS,
                       "voiceover": "Before number one, a question you might be asking: where are plumbers and electricians? They're not in Microsoft's bottom forty. That doesn't mean AI can do their jobs. It just means they weren't among the very lowest scores."})
    lead = f"Number {W[c['r']]}."
    scenes.append({"type": "rank", "rank": c["r"], "eyebrow": f"Microsoft list position {c['rows']}", "headline": c["name"], "voiceover": lead})
    scenes.append({"type": "broll", "broll": {"file": c["clip"], "start": c.get("start", 0)}, "rank": c["r"],
                   "eyebrow": "Why AI struggles here", "headline": c["why_h"], "receipt": f"{MS} · position {c['rows']}", "stat": stat(c),
                   "voiceover": c["why"]})
    scenes.append({"type": "point", "rank": c["r"], "name": c["name"], "eyebrow": "What you need first",
                   "headline": c["need_h"], "receipt": c["need_r"], "voiceover": c["need"]})
    scenes.append({"type": "point", "rank": c["r"], "name": c["name"], "eyebrow": "How AI can still help", "tag": "AI ASSIST",
                   "headline": c["ai_h"], "receipt": SUGG, "voiceover": c["ai"]})

scenes += [
 {"type": "broll", "broll": "aiproof-11-ending.mp4", "eyebrow": "The pattern", "headline": "Skilled hands. AI back office.",
  "voiceover": "See the pattern? The work itself needs skilled hands, in a real place, for a real person. But the back office, the quotes, bookings, invoices and marketing, is exactly where AI can make a small business faster. The owners who use both will have the edge."},
 {"type": "plain", "eyebrow": "Before you start", "headline": "Check the rules for your trade",
  "body": "Educational only, not financial advice. AI exposure isn't replacement, and no business is guaranteed.",
  "voiceover": "Before you start anything, check the rules and training for your trade, and talk to people already doing it. This video is education, not financial advice, and no business is guaranteed to succeed."},
 {"type": "plain", "eyebrow": "Your turn", "headline": "Which of these would you start?",
  "voiceover": "Which of these would you start? Tell us in the comments. All our sources are in the description."},
]
for s in scenes:
    s["duration"] = est(s["voiceover"])

EMMA = {"engine": "kokoro", "name": "bf_emma", "speed": 1.05, "lang": "en-gb", "lead_pad": 400, "tail_pad": 900}
base = {"template": "template-countdown.html", "brand": {"name": "Mzansi Money Matters", "logo": "logo.jpg"},
        "voice": EMMA, "timing": {"lead_in": 900}}

SOURCES = """Sources:
Ranking: Microsoft Research, Tomlinson et al., "Working with AI: Measuring the Occupational Implications of Generative AI" (pre-print, July 2025). It is based on 200,000 anonymised Bing Copilot conversations (US, 2024). We used its list of the 40 occupations with the lowest AI applicability. Positions used: floor sanders & finishers 7; cement masons & concrete finishers 23; motorboat operators 9; paving, surfacing & tamping equipment operators 11; maids & housekeeping cleaners 12; roofers 14; helpers–roofers 16; massage therapists 19; industrial truck & tractor operators 21; tire repairers & changers 31; automotive glass installers & repairers 33; helpers–painters, plasterers 37. The researchers note that all occupations have some potential for AI impact, and that overlap does not mean replacement.
Context: World Economic Forum, Future of Jobs Report 2025 (frontline roles such as farmworkers, delivery drivers and construction workers see the largest job growth to 2030). ILO Working Paper 140 (2025), Generative AI and Jobs: A Refined Global Index of Occupational Exposure.
SA rules mentioned: Waste Tyre Regulations, 2017 (National Environmental Management: Waste Act); Driven Machinery Regulations, 2015, regulation 18(11) (Occupational Health and Safety Act); Allied Health Professions Council of South Africa (AHPCSA), Registered Therapeutic Massage Therapist (SAQA designation 472); South African Maritime Safety Authority (SAMSA), small vessel certificates of competence.
"What you need first" checklists and "How AI can help" tips are MMM suggestions, not findings of any study."""

long = dict(base, slug="top10-ai-proof-businesses", countdown={"from": 10},
 disclaimer="Education, not financial advice. AI exposure isn't replacement.",
 thumbnail={"big": "AI CAN'T DO THIS", "line": "10 businesses you can <em>start</em>", "image": "aiproof-thumb.jpg", "focus": "center"},
 scenes=scenes,
 endcard={"title": "Skilled hands. <em>AI back office.</em>", "subtitle": "Subscribe for South African money, explained.",
          "handle": "@MzansiMoneyMatters", "duration": 15000},
 youtube={"title": "Jobs AI Can't Easily Replace: 10 Businesses You Can Start in South Africa", "privacy": "private",
  "synthetic_media": True, "category_id": "27",
  "tags": ["jobs AI can't replace", "businesses AI can't replace", "AI proof jobs", "AI proof business", "businesses to start in South Africa",
           "small business ideas South Africa", "future of work", "AI and jobs", "Mzansi Money Matters"],
  "description": ("Jobs AI can't easily replace: 10 hands-on businesses you can start in South Africa. For each one we cover why AI struggles with it, "
   "what you need first, and how AI can still help you run it.\n\nHow we ranked them: each business takes its position on Microsoft Research's "
   "2025 list of the 40 US jobs where AI chatbots apply least (lowest position = #1). A business that combines two jobs takes its lower position.\n\n"
   "{chapters}\n\n" + SOURCES +
   "\n\n#JobsAICantReplace #SmallBusiness #SouthAfrica #MzansiMoneyMatters\n\nIndependent channel. Education, not financial advice. "
   "Narration is AI-generated. Video clips were generated with Google Flow (Veo).")})

q = [
 {"type": "broll", "broll": "aiproof-00-opening.mp4", "eyebrow": "Jobs AI can't easily replace", "headline": "ChatGPT can write your CV.",
  "voiceover": "ChatGPT can write your CV."},
 {"type": "broll", "broll": "aiproof-05-roofing.mp4", "eyebrow": "Roofing", "headline": "It can't fix your roof.",
  "voiceover": "But it can't fix your roof."},
 {"type": "broll", "broll": {"file": "aiproof-08-tyres.mp4", "start": 3}, "eyebrow": "Tyre fitment", "headline": "Or change your tyre.",
  "voiceover": "Or change your tyre."},
 {"type": "broll", "broll": "aiproof-04-cleaning.mp4", "eyebrow": "Home cleaning", "headline": "Or clean your home.",
  "voiceover": "Or clean your home."},
 {"type": "plain", "eyebrow": "The research", "headline": "200,000 AI chats studied",
  "body": "Jobs like these scored among the lowest for AI help.", "receipt": "Microsoft Research, 2025 pre-print (US data)",
  "voiceover": "Microsoft studied two hundred thousand AI chats. Jobs like these scored among the lowest for AI help."},
 {"type": "plain", "eyebrow": "10 businesses", "headline": "You can start one in South Africa",
  "voiceover": "We ranked ten businesses like this that you can start in South Africa."},
 {"type": "plain", "eyebrow": "Every source on screen", "headline": "Full top 10 on the channel",
  "voiceover": "Number one might surprise you. The full top ten is on our channel."},
]
for s in q:
    s["duration"] = est(s["voiceover"])
short = dict(base, slug="short-ai-proof-businesses", size=[1080, 1920], countdown={"from": 10}, broll_fit="pad",
 disclaimer="Education, not financial advice.", voice=dict(EMMA, lead_pad=300, tail_pad=600), timing={"lead_in": 600}, scenes=q,
 endcard={"title": "AI <em>can't</em> do this", "subtitle": "10 businesses, sources included",
          "handle": "@MzansiMoneyMatters", "voiceover": "Watch the full top ten on Mzansi Money Matters.", "duration": 3500},
 youtube={"title": "ChatGPT can't fix your roof #shorts", "privacy": "private", "synthetic_media": True, "category_id": "27",
  "tags": ["jobs AI can't replace", "AI proof jobs", "small business South Africa", "Mzansi Money Matters"],
  "description": "ChatGPT can write your CV, but it can't fix your roof. Microsoft studied 200,000 AI chats to find the work AI helps with least (2025 pre-print, US data). Full top 10 with sources on Mzansi Money Matters.\n\n#JobsAICantReplace #Shorts\n\nEducation, not financial advice. Narration is AI-generated. Clips generated with Google Flow (Veo)."})

json.dump(long, open("content-aiproof.json", "w"), ensure_ascii=False, indent=2)
json.dump(short, open("content-short-aiproof.json", "w"), ensure_ascii=False, indent=2)
for n, d in (("long", long), ("short", short)):
    print(n, len(d["scenes"]), "scenes, ~%.1f min" % (sum(s["duration"] for s in d["scenes"]) / 60000))
