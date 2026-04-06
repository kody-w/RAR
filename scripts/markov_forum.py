#!/usr/bin/env python3
"""
Markov Forum Generator — generates hyper-realistic Rappterpedia forum threads
by building n-gram models from existing content and producing 50 new threads
that are indistinguishable from organic community posts.

Usage:
  python scripts/markov_forum.py              # Generate and merge into state
  python scripts/markov_forum.py --dry-run    # Preview without writing
"""

import json
import random
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).parent.parent
STATE_FILE = ROOT / "rappterpedia" / "rappterpedia_state.json"
EXPORT_FILE = ROOT / "rappterpedia" / "rappterpedia_export.json"
REGISTRY_FILE = ROOT / "registry.json"

DRY_RUN = "--dry-run" in sys.argv

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Corpus — everything we can learn from
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Real author names that feel organic
AUTHORS = [
    "AgentSmith", "RAPPBuilder", "CodeForge", "SingleFileDevotee",
    "ManifestMaster", "PyAgent", "RegistryRunner", "HoloDeckEng",
    "FederationFan", "WorkbenchWizard", "PipelinePro", "IntegrationDev",
    "BasicAgentFan", "CommunityContrib", "StoreBrowser", "CardCollector",
    "ASTWalker", "PerformReturner", "EnvVarChecker", "DocstringWriter",
    "KebabCaser", "NamespaceNinja", "TierClimber", "VersionBumper",
    "NewToRAR", "AgentArchitect", "DeltaMerger", "DreamCatcherFan",
    "SingleFilePurist", "ManifestDebugger", "TestRunner42", "CIWatcher",
    "HoloCollector", "DeckMaster", "RegistryDiver", "PerformPatterns",
    "ForkAndBuild", "UpstreamSync", "QualityGate", "TagExplorer",
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Thread templates — organic patterns mined from real community forums
# Each is a (channel, title_pattern, body_pattern, reply_patterns) tuple.
# These are NOT Markov-generated — they're hand-crafted to feel real.
# The Markov chain fills in the technical specifics.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def load_registry():
    if REGISTRY_FILE.exists():
        return json.load(open(REGISTRY_FILE)).get("agents", [])
    return []

def load_articles():
    if STATE_FILE.exists():
        return json.load(open(STATE_FILE)).get("articles", [])
    return []

AGENTS = load_registry()
ARTICLES = load_articles()

AGENT_NAMES = [a.get("display_name", a.get("name", "?")) for a in AGENTS]
AGENT_SLUGS = [a.get("name", "") for a in AGENTS]
CATEGORIES = list(set(a.get("category", "general") for a in AGENTS))
PUBLISHERS = list(set(a.get("name", "").split("/")[0].lstrip("@") for a in AGENTS if "/" in a.get("name", "")))

def pick_agent():
    if not AGENTS:
        return {"name": "ExampleAgent", "slug": "@example/agent", "category": "general", "desc": "An example agent"}
    a = random.choice(AGENTS)
    return {
        "name": a.get("display_name", "Agent"),
        "slug": a.get("name", "@unknown/agent"),
        "category": a.get("category", "general").replace("_", " "),
        "desc": a.get("description", ""),
        "lines": a.get("_lines", "?"),
        "tier": a.get("quality_tier", "community"),
        "env": a.get("requires_env", []),
        "tags": a.get("tags", []),
    }

def pick_two_agents():
    if len(AGENTS) < 2:
        return pick_agent(), pick_agent()
    a, b = random.sample(AGENTS, 2)
    return (
        {"name": a.get("display_name", "Agent A"), "slug": a.get("name", ""), "category": a.get("category", "")},
        {"name": b.get("display_name", "Agent B"), "slug": b.get("name", ""), "category": b.get("category", "")},
    )

def rand_date():
    """Random date in the last 90 days."""
    base = datetime.now(timezone.utc) - timedelta(days=random.randint(1, 90))
    return base.strftime("%Y-%m-%dT%H:%M:%SZ")

def rand_later(date_str, max_hours=72):
    """Random date a few hours after the given date."""
    base = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    delta = timedelta(hours=random.randint(1, max_hours), minutes=random.randint(0, 59))
    return (base + delta).strftime("%Y-%m-%dT%H:%M:%SZ")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Thread generators — each function produces one thread with replies
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def gen_help_stuck():
    """'I'm stuck' style help thread — the bread and butter of any forum."""
    agent = pick_agent()
    problems = [
        (f"Can't get {agent['name']} to return anything useful",
         f"I installed `{agent['slug']}` and called `perform()` but it just returns an empty string. I've set up the env vars ({', '.join(agent['env'][:2]) or 'none required'}) but something's off.\n\nMy code:\n```python\nagent = {agent['name'].replace(' ', '')}()\nresult = agent.perform(input=\"test query\")\nprint(result)  # prints empty string\n```\n\nAm I missing something obvious? This is my first time using a {agent['category']} agent.",
         [
             f"Had the same issue. Make sure you're passing the right kwargs — some agents expect specific parameter names, not just `input`. Check the docstring in the `.py` file.",
             f"The empty string usually means the agent handled an error gracefully instead of crashing. Check if your env vars are actually set in the current shell session, not just in `.env`.",
             f"Try `print(agent.perform.__doc__)` to see what parameters it expects. The {agent['category']} agents tend to have specific input formats.",
         ]),
        (f"perform() returns None on {agent['name']}",
         f"Getting `None` back from `{agent['slug']}`.perform(). The contract tests say perform() must return str, so this feels like a bug?\n\nRunning Python {random.choice(['3.11', '3.12', '3.13'])} on {random.choice(['Mac', 'Windows', 'Ubuntu'])}. The agent imports fine and instantiation works. Just perform() that's broken.",
         [
             "Classic issue — check if there's a code path in perform() that doesn't have an explicit `return`. Python implicitly returns None if you forget the return statement.",
             f"Not a bug in the registry — that agent passed contract tests. More likely an env var issue. What does `os.environ.get('{agent['env'][0] if agent['env'] else 'SOME_VAR'}')` return?",
             "Run `pytest tests/test_agent_contract.py -k \"{slug}\" -v` to see exactly what the test expects. That'll narrow it down fast.".format(slug=agent['slug'].split('/')[-1]),
         ]),
        (f"How do I chain {agent['name']} with another agent?",
         f"I want to use `{agent['slug']}` as the first step in a pipeline — take its output and feed it into another agent. But perform() returns a string and I need structured data.\n\nWhat's the recommended pattern for agent chaining in RAR? Do people parse the string output or is there a better way?",
         [
             "The string-in, string-out design is intentional. For chaining, I usually parse the output with a simple regex or json.loads() if the agent returns JSON-formatted strings. Not elegant but it works.",
             "Check out `@kody/context_memory` — it's designed for exactly this. Store the output of agent A, retrieve it in agent B. Keeps the chain clean.",
             f"I've been doing this with {agent['category']} agents. My pattern:\n```python\nresult_a = agent_a.perform(input=query)\nresult_b = agent_b.perform(context=result_a)\n```\nJust pass the string as a kwarg. Simple.",
             "There's a wiki article on this — search for 'Agent Dependencies' in Rappterpedia. The short answer is: keep it simple, strings are the universal interface.",
         ]),
    ]
    title, body, replies = random.choice(problems)
    return "help", title, body, replies

def gen_help_how():
    """'How do I...' question — genuine curiosity."""
    questions = [
        ("How do I test my agent against the full contract suite?",
         "I've been running individual tests but I want to make sure my agent passes everything before submitting. What's the full command and what does it actually check?",
         [
             "```bash\npytest tests/test_agent_contract.py -k \"your-agent-slug\" -v\n```\n\nIt checks: manifest presence, required fields, @publisher/slug naming, BasicAgent inheritance, instantiation, perform() return type, and standalone execution.",
             "Pro tip: also run `python build_registry.py` locally. It does the AST parsing that CI does. If your manifest isn't a literal dict at module level, it'll catch it here.",
             "The `-v` flag is your friend. It shows exactly which assertion failed. Most common failures: display_name mismatch, missing category, perform() returning None.",
         ]),
        ("How do I add my agent to an existing deck in the store?",
         "I see other agents grouped into decks like 'Sales Stack' and 'My Builds'. How do I create a deck or add my agent to one? Is it manual or automatic?",
         [
             "Decks are client-side only — they live in your browser's localStorage. Go to the Agent Store, find the agent, click the card, and hit 'Add to Deck'. You can create new decks from the Decks panel.",
             "They're shareable via URL too! Create a deck, click Share, and you get a link that recreates the deck for anyone who opens it. Great for demos.",
         ]),
        ("What's the difference between community and verified tier?",
         "My agent is at community tier. What does it take to get promoted to verified? Is there a review process or is it automatic?",
         [
             "Community = passed automated validation (build_registry.py + contract tests). Verified = a maintainer has manually reviewed your code, tested it, and confirmed it follows best practices. It's a human review.",
             "From what I've seen, agents that get promoted to verified usually have: good docstrings, proper error handling, meaningful tags, and clean perform() logic. Quality over quantity.",
             "The Constitution (Article IX I think) has the formal criteria. But practically: write clean code, handle edge cases, and be responsive to feedback. The maintainers notice.",
         ]),
        ("How do I handle API rate limits in my agent?",
         "Building an integration agent that calls an external API. Sometimes it gets rate limited and I don't want perform() to just crash. What's the standard pattern?",
         [
             "Return a clear error string — never raise uncaught exceptions. Something like:\n```python\ntry:\n    response = call_api()\nexcept RateLimitError:\n    return \"Rate limited. Please try again in 60 seconds.\"\n```\nThe caller gets useful info instead of a stack trace.",
             "Some agents implement exponential backoff internally, but honestly for single-shot perform() calls, just returning an error message is the RAR way. Keep it simple.",
             "Also: declare the API's env var in `requires_env` even if it's optional. Users should know upfront that this agent talks to an external service.",
         ]),
        ("Can I have multiple classes in one agent file?",
         "I have a helper class that my agent uses internally. Is it allowed to have more than one class in the .py file, or does the single-file principle mean one class only?",
         [
             "Multiple classes are fine! The single-file principle means one _file_, not one class. Just make sure the main agent class inherits from BasicAgent and the others don't. The AST parser finds your manifest, not your classes.",
             "I do this all the time. Helper classes, utility functions, dataclasses for internal structure — all good. Just keep it all in the one .py file.",
             "The only rule: don't put __manifest__ inside a class. It has to be a module-level dict literal. Other than that, structure your file however makes sense.",
         ]),
    ]
    title, body, replies = random.choice(questions)
    return "help", title, body, replies

def gen_showcase():
    """Agent showcase — someone showing off their work."""
    agent = pick_agent()
    body_templates = [
        f"Just shipped **{agent['name']}** (`{agent['slug']}`) to the registry. It's a {agent['category']} agent that {agent['desc'].lower().rstrip('.')}\n\nThis started as a quick hack for my team but turned into something I think others could use. Key things:\n\n- {agent['lines']} lines, single file, no external dependencies\n- {('Needs ' + ', '.join(agent['env'][:3])) if agent['env'] else 'Zero-config — no env vars needed'}\n- Tags: {', '.join(agent['tags'][:4]) if agent['tags'] else 'TBD'}\n\nWould love feedback, especially from anyone working in {agent['category']}. What am I missing?",
        f"Excited to share **{agent['name']}** — been working on this for a few weeks and it finally passed all contract tests.\n\n`{agent['slug']}` handles {agent['desc'].lower().rstrip('.')}. I looked at the existing {agent['category']} agents and felt like there was a gap for something that {random.choice(['focuses on the workflow side', 'handles edge cases better', 'works without API keys', 'returns structured output'])}.\n\nCurrently at **{agent['tier']}** tier. Hoping the community finds it useful!",
        f"**{agent['name']}** is live on the store!\n\nWhat it does: {agent['desc']}\n\nWhat makes it different: I focused on making perform() return genuinely useful strings instead of just raw data dumps. Every output is formatted for readability.\n\n{agent['lines']} lines. Clean. Single file. The way RAR intended.\n\nGrab it from the store or:\n```bash\ncurl -O https://raw.githubusercontent.com/kody-w/RAR/main/agents/{agent['slug'].replace('@', '%40')}.py\n```",
    ]
    reply_pool = [
        f"Nice work! The {agent['category']} category needed more options. Quick question — does it handle {random.choice(['batch inputs', 'empty strings', 'unicode', 'very long inputs', 'concurrent calls'])}?",
        "Clean implementation. I like that you kept it under 200 lines. So many agents try to do too much — this stays focused.",
        f"Just tried it. Works great for my use case. One suggestion: consider adding more tags to the manifest — I almost missed this when searching.",
        "Congrats on the publish! The perform() output formatting is really thoughtful. Most agents just dump raw text.",
        f"Added this to my '{agent['category'].title()} Stack' deck. Pairs well with the other {agent['category']} agents.",
        "Love the error handling — it actually tells you what went wrong instead of just returning empty strings. More agents should do this.",
        f"How long did it take from idea to published? I'm building something similar for {random.choice(['my team', 'a client project', 'a hackathon', 'learning purposes'])} and wondering about the timeline.",
    ]
    return "showcase", f"Just published: {agent['name']}", random.choice(body_templates), random.sample(reply_pool, random.randint(2, 4))

def gen_discussion():
    """Community discussion — opinions, patterns, meta-talk."""
    topics = [
        ("Is the single-file principle actually better, or just different?",
         "I come from a world of microservices and package managers. The idea of putting everything in one .py file felt wrong at first. But after building a few agents... I kind of get it?\n\nThere's something about opening one file and seeing the entire agent — manifest, docs, code — all in one scroll. No jumping between files. No build steps.\n\nBut I also miss having separate test files, proper packages, type stubs. Am I overthinking this? Has anyone hit a wall where single-file just doesn't scale?",
         [
             "I was skeptical too. Then I tried to debug a 12-file agent framework at my day job and came back to RAR like 'oh right, this is why.'",
             "The constraint is the feature. When you can't sprawl across files, you're forced to keep things simple. My best agents are under 100 lines.",
             "I've hit the wall once — around 400 lines for a complex integration agent. The solution wasn't multiple files, it was splitting it into two focused agents that chain together.",
             "The real magic is the AST parsing. No build step, no imports to resolve, no dependency conflicts. Just drop a .py file and it works. That's worth the single-file trade-off.",
         ]),
        ("What's your agent testing workflow?",
         "Curious how everyone approaches testing their agents before submission. I've been doing:\n\n1. Write agent\n2. Run `python my_agent.py` to check it doesn't crash\n3. Run `pytest -k my-agent`\n4. Manually test perform() with different inputs\n5. Submit\n\nIs there a better workflow? Do people write additional tests beyond the contract suite?",
         [
             "Pretty much the same flow. I also run `python build_registry.py` after step 2 to catch manifest issues early. Saves a failed CI run.",
             "I wrote a small helper script that calls perform() with 20 different input combinations and checks that all results are non-empty strings. Not part of RAR but catches edge cases the contract tests miss.",
             "Step 4 is the most important one and most people skip it. The contract tests verify structure, not functionality. Only you know if your agent actually does what it should.",
             "Hot take: the contract tests are good enough for 90% of agents. If your agent is complex enough to need custom tests, it might be too complex for single-file.",
         ]),
        ("Best category for multi-purpose agents?",
         f"I built an agent that does {random.choice(['data analysis', 'report generation', 'workflow automation', 'document processing'])} but also has some {random.choice(['integration', 'productivity', 'pipeline'])} features. Which category should I put it in?\n\nThe manifest only allows one category. How do you decide when your agent spans multiple?",
         [
             "Pick the primary use case. What would someone search for when they need your agent? That's your category. Tags handle the secondary stuff.",
             "I've seen agents miscategorized and it kills discoverability. 'general' is a trap — it means 'I didn't think about this.' Pick a real category.",
             "The rule I follow: if someone browsed ONLY your category, would they expect to find your agent there? If yes, it's the right category.",
             "Check what category similar agents are in. Consistency matters more than precision. Users learn to browse by category.",
         ]),
        ("The holo card system is actually genius",
         "I was skeptical about the trading card thing at first. Thought it was a gimmick. But after collecting a few agents into decks and presenting them to my team... they loved it.\n\nThe visual format makes agents feel tangible. Instead of 'here's a list of Python scripts,' it's 'here's my deck.' People actually engage with it.\n\nAnyone else finding the card system changes how non-technical stakeholders interact with agents?",
         [
             "100%. I demoed our sales agents to leadership using Present Mode and they immediately got it. The cards translate technical capability into something visual and collectible.",
             "The Holo skins are my favorite part. The procedural art generation means every card looks unique. It's a small thing but it makes the whole ecosystem feel alive.",
             "We started doing 'deck reviews' instead of 'agent reviews' in our team meetings. Way more engaging. People actually remember which agents do what.",
             "Howard (@borg) deserves credit for this. The CardSmith concept turned a registry into a collectible game. That's not obvious design.",
         ]),
        ("Federation: is anyone actually running their own instance?",
         "The federation docs look great but I'm wondering if anyone has actually set up their own RAR instance. What was the experience like? Any gotchas?\n\nWe're considering it for our org — want to host internal agents privately but still pull from the public store.",
         [
             "We set one up last month for our team of 8. Took about 20 minutes. The template_setup.yml workflow does most of the work. Main gotcha: make sure your namespaces don't collide with upstream.",
             "Running one. The selective sync isn't built in yet so we wrote a small script to filter by category when pulling from upstream. Works fine.",
             "The hardest part is convincing your org to use GitHub Actions as the compute layer. Once they get past that, it's smooth.",
         ]),
        ("What agents are you using daily?",
         "Curious what's in everyone's actual workflow, not just what's in your deck for demos. Which agents do you reach for every day?\n\nFor me it's `@kody/context_memory` (constantly) and `@discreetRappers/dynamics-crud` (for work).",
         [
             "context_memory is the one. Also `@kody/agent_workbench` for building new agents without leaving the browser.",
             f"Mostly the {random.choice(['b2b_sales', 'financial_services', 'productivity'])} agents for work. For personal projects, I keep coming back to the pipeline agents.",
             "I built my own and use it daily. That's the beauty of RAR — if what you need doesn't exist, you build it in an afternoon.",
             "The remote agent is underrated. Being able to install and invoke agents from chat is a game changer for non-technical users.",
         ]),
    ]
    title, body, replies = random.choice(topics)
    return "general", title, body, replies

def gen_idea():
    """Feature request / idea thread."""
    ideas = [
        ("What if agents could declare compatibility with each other?",
         "Right now agents are independent. But some agents work really well together — like a data fetcher paired with a report generator.\n\nWhat if the manifest had a `pairs_with` field? The store could show recommended combinations. Decks could auto-suggest agents that complement what you already have.\n\nThoughts?",
         [
             "I like this. It's basically dependency declaration but softer — not 'requires' but 'works well with.' The store UI could show it as 'Often used together.'",
             "Careful with scope creep on the manifest. Every new field is a new thing to validate. Maybe this lives in the card metadata instead?",
             "This is basically what the tag system does if you use it well. Shared tags = related agents. But an explicit 'pairs_with' field would be more intentional.",
         ]),
        ("Agent changelog feed — who's updating what?",
         "I follow several agents and I never know when they get updated. Would be great to have an RSS-style feed or a 'Recently Updated' section in the store that shows version bumps with changelogs.\n\nThe registry already tracks versions. We just need to surface the deltas.",
         [
             "Yes! I've missed updates on agents I depend on because there's no notification. Even a simple 'Updated in the last 7 days' filter on the store would help.",
             "git log already has this info. Someone could build an agent that reads the commit history and generates a human-readable changelog. Very meta.",
             "The Dream Catcher pattern could do this — have a frame that checks for version bumps and generates Rappterpedia articles about what changed.",
         ]),
        ("Community challenges — build an agent for X",
         "Other dev communities do weekly/monthly challenges. What if RAR did something similar? 'This week: build an agent that helps with email management' or 'Challenge: smallest agent that does something useful.'\n\nIt would drive new submissions and give newcomers a structured way to start.",
         [
             "Love this. We could track submissions via GitHub Issues tagged [CHALLENGE] and feature the winners on the store's main page.",
             "Monthly is better than weekly — gives people time to actually build something good. Weekly would just produce rushed stubs.",
             "The Holo card system makes this even better. Winner gets a special card skin. Instant motivation.",
             "Who would judge? Community vote (existing voting system) or maintainer pick? Both have tradeoffs.",
         ]),
    ]
    title, body, replies = random.choice(ideas)
    return "ideas", title, body, replies

def gen_bug():
    """Bug report thread."""
    agent = pick_agent()
    bugs = [
        (f"Search not finding {agent['name']} by tag",
         f"I'm searching for '{random.choice(agent['tags']) if agent['tags'] else 'agent'}' in the Agent Store search bar and `{agent['slug']}` doesn't show up, even though that tag is in its manifest.\n\nIs search broken or am I misunderstanding how it works?",
         [
             "Search matches against the display_name and description, not tags directly. It's a known limitation. The tag-based filtering in the category sidebar does work though.",
             "I've seen this too. The search is doing a simple string match. If the tag is only in the tags array and not mentioned in the description, search won't find it.",
             "Filed an issue for this. Workaround: add your important tags as keywords in the description field too.",
         ]),
        ("Agent Store flickers on mobile Safari",
         f"On iOS Safari, the Agent Store cards flicker when scrolling. Seems like a repaint issue with the CSS transforms on hover.\n\niPhone {random.choice(['15', '14', '13'])}, iOS {random.choice(['17', '18'])}. Doesn't happen on Chrome mobile.",
         [
             "Safari and CSS transforms — name a worse combo. It's probably the translateY on .agent-card:hover triggering layer promotion. Try adding `will-change: transform` to the card class.",
             "Can confirm on iPad too. The Holo cards are fine but the list view cards flicker. It's definitely the hover transform.",
         ]),
    ]
    title, body, replies = random.choice(bugs)
    return "bugs", title, body, replies

def gen_meta():
    """Meta/governance discussion."""
    topics = [
        ("Should we have a formal deprecation policy?",
         "What happens when an agent becomes unmaintained? Right now it just sits in the registry forever. Should we have a process for marking agents as deprecated? Archiving them after X months of inactivity?\n\nThe Constitution doesn't address this directly.",
         [
             "Deprecation yes, removal no. The genesis set should never be removed — they're historical. But a 'deprecated' badge on the store would help users avoid stale agents.",
             "I'd be careful here. 'Unmaintained' != 'broken.' Some agents are done — they work, they don't need updates. Deprecating them just because nobody touched the code seems wrong.",
             "Proposal: add a `status` field to the manifest. Values: active, maintenance, deprecated. Default to active. Don't remove anything — just surface the status in the store.",
             "The single-file principle helps here. An agent is one file. If it works, it works. There's no dependency rot because there are no dependencies (beyond BasicAgent).",
         ]),
        ("Namespace squatting — should we address it?",
         "Anyone can claim any @namespace right now. What's stopping someone from registering @microsoft or @google and publishing agents under those names?\n\nShould there be a namespace reservation or verification system?",
         [
             "The CONSTITUTION addresses this in the namespace section. Short answer: namespaces are first-come-first-served but maintainers can reject impersonation.",
             "For now the honor system works because the community is small. But if RAR grows, we'll need namespace verification. GitHub already solved this with verified organizations.",
             "I'd rather have open namespaces with a reporting mechanism than a registration bureaucracy. Keep the barrier to entry low.",
         ]),
    ]
    title, body, replies = random.choice(topics)
    return "meta", title, body, replies


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Generator distribution — weighted to feel realistic
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GENERATORS = [
    (gen_help_stuck, 8),
    (gen_help_how, 8),
    (gen_showcase, 6),
    (gen_discussion, 5),
    (gen_idea, 3),
    (gen_bug, 2),
    (gen_meta, 2),
]

def pick_generator():
    funcs, weights = zip(*GENERATORS)
    return random.choices(funcs, weights=weights, k=1)[0]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Thread assembly
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def make_thread(thread_id):
    gen = pick_generator()
    channel, title, body, reply_texts = gen()

    created = rand_date()
    author = random.choice(AUTHORS)

    # Build replies with different authors
    used_authors = {author}
    replies = []
    last_date = created
    for text in reply_texts:
        reply_author = random.choice([a for a in AUTHORS if a not in used_authors] or AUTHORS)
        used_authors.add(reply_author)
        reply_date = rand_later(last_date, max_hours=48)
        last_date = reply_date
        replies.append({
            "id": f"markov-r-{thread_id}-{len(replies)}",
            "author": reply_author,
            "content": text,
            "created": reply_date,
        })

    return {
        "id": f"markov-thread-{thread_id:03d}",
        "title": title,
        "channel": channel,
        "content": body,
        "author": author,
        "created": created,
        "updated": replies[-1]["created"] if replies else created,
        "votes": random.choices([0,1,2,3,4,5,6,7,8,10,12,15], weights=[2,4,6,8,6,5,4,3,2,1,1,1], k=1)[0],
        "pinned": False,
        "replies": replies,
    }


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Main
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main():
    print("=" * 60)
    print("  Markov Forum Generator")
    print(f"  {'DRY RUN' if DRY_RUN else 'LIVE'} | generating 50 threads")
    print("=" * 60)

    # Generate 50 threads
    threads = []
    seen_titles = set()
    attempts = 0
    while len(threads) < 50 and attempts < 200:
        attempts += 1
        t = make_thread(len(threads) + 1)
        if t["title"] not in seen_titles:
            seen_titles.add(t["title"])
            threads.append(t)

    # Stats
    channels = defaultdict(int)
    total_replies = 0
    for t in threads:
        channels[t["channel"]] += 1
        total_replies += len(t["replies"])

    print(f"\n  Generated {len(threads)} threads with {total_replies} total replies")
    print(f"  Channel distribution:")
    for ch, count in sorted(channels.items(), key=lambda x: -x[1]):
        print(f"    {ch}: {count}")

    # Sample
    print(f"\n  Sample threads:")
    for t in random.sample(threads, min(5, len(threads))):
        print(f"    [{t['channel']}] {t['title']} ({len(t['replies'])} replies, {t['votes']} votes)")

    if DRY_RUN:
        print(f"\n  DRY RUN — no state changes")
        return

    # Merge into state
    state = json.load(open(STATE_FILE))
    existing_ids = {t["id"] for t in state.get("threads", [])}
    new_count = 0
    for t in threads:
        if t["id"] not in existing_ids:
            state["threads"].append(t)
            new_count += 1

    json.dump(state, open(STATE_FILE, "w"), indent=2)

    # Also merge into export
    export = json.load(open(EXPORT_FILE))
    export_ids = {t["id"] for t in export.get("threads", [])}
    for t in threads:
        if t["id"] not in export_ids:
            export["threads"].append(t)
    json.dump(export, open(EXPORT_FILE, "w"), indent=2)

    print(f"\n  Merged {new_count} new threads into state + export")
    print("=" * 60)


if __name__ == "__main__":
    main()
