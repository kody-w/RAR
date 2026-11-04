---
name: "rar-kody-w-rappterpedia"
description: "Generates wiki articles, forum threads, and replies for the Rappterpedia knowledge base from rules-as-data templates."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rappterpedia_agent", "rar_sha256": "078d5bbb37e91cb052e9cfdc540aa5024d6a573f0be14df860c7df4c4ba08f69", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.1", "author": "Kody Wildfeuer", "tags": ["wiki", "forum", "content", "community", "rappterpedia", "engine"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rappterpedia_agent`. The original RAPP
agent is preserved byte-for-byte in `rappterpedia_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Rappterpedia Agent — Community wiki & forum content engine for the RAPP ecosystem.

Generates wiki articles, forum threads, and replies using rules-as-data templates.
Can be harnessed by the Virtual Brainstem or any CommunityRAPP runtime to pump
high-quality, contextual content into the Rappterpedia knowledge base.

Operations:
  - search:            Search articles and threads by keyword
  - generate_article:  Generate a wiki article from rules-as-data templates
  - generate_thread:   Generate a forum thread with replies
  - list_articles:     List existing wiki articles (optionally by category)
  - list_threads:      List existing forum threads (optionally by channel)
  - generate_burst:    Generate multiple articles and threads in one call
  - export:            Export all generated content as JSON
  - stats:             Show content generation statistics

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "category": {
      "description": "Filter by category/channel",
      "type": "string"
    },
    "count": {
      "description": "Number of items to generate (for burst)",
      "type": "integer"
    },
    "operation": {
      "description": "The operation to perform",
      "enum": [
        "search",
        "generate_article",
        "generate_thread",
        "list_articles",
        "list_threads",
        "generate_burst",
        "export",
        "stats"
      ],
      "type": "string"
    },
    "query": {
      "description": "Search query (for search operation)",
      "type": "string"
    },
    "topic": {
      "description": "Optional topic hint for generation",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rappterpedia_agent.py` and embedded as the fenced Python below (sha256 078d5bbb37e91cb0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rappterpedia_agent.py` first:

```bash
python3 rappterpedia_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rappterpedia_agent.py   # or on stdin
python3 rappterpedia_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/rappterpedia_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rappterpedia_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/rappterpedia_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Rappterpedia Agent — Community wiki & forum content engine for the RAPP ecosystem.

Generates wiki articles, forum threads, and replies using rules-as-data templates.
Can be harnessed by the Virtual Brainstem or any CommunityRAPP runtime to pump
high-quality, contextual content into the Rappterpedia knowledge base.

Operations:
  - search:            Search articles and threads by keyword
  - generate_article:  Generate a wiki article from rules-as-data templates
  - generate_thread:   Generate a forum thread with replies
  - list_articles:     List existing wiki articles (optionally by category)
  - list_threads:      List existing forum threads (optionally by channel)
  - generate_burst:    Generate multiple articles and threads in one call
  - export:            Export all generated content as JSON
  - stats:             Show content generation statistics
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rappterpedia_agent",
    "version": "1.1.1",
    "display_name": "RappterpediaAgent",
    "description": "Generates wiki articles, forum threads, and replies for the Rappterpedia knowledge base from rules-as-data templates.",
    "author": "Kody Wildfeuer",
    "tags": ["wiki", "forum", "content", "community", "rappterpedia", "engine"],
    "category": "productivity",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

import json
import os
import random
from datetime import datetime, timezone
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ARTICLE RULES — data-driven wiki article generation
# Adding new article types = adding a dict entry, zero code changes
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ARTICLE_RULES = {
    "agent_deep_dive": {
        "category": "agents",
        "weight": 6,
        "tags": ["agent", "deep-dive", "reference"],
        "titles": [
            "Deep Dive: {agent_display} — What It Does and How to Use It",
            "Understanding {agent_display}: A Complete Guide",
            "{agent_display} Explained: From Install to Production",
        ],
        "sections": [
            ("Overview", [
                "**{agent_display}** (`{agent_name}`) is a {category} agent in the RAPP registry. {description}\n\nPublished by `{publisher}`, it's at version {version} with **{quality_tier}** quality tier.",
            ]),
            ("Installation", [
                "### From the Agent Store\n\nBrowse to the agent card and download the `.py` file. Drop it into your `agents/` folder.\n\n### Direct Fetch\n\n```bash\ncurl -O https://raw.githubusercontent.com/kody-w/RAR/main/agents/{agent_path}\n```\n\n### From Chat\n\nAsk the RAPP Remote Agent: *\"Install {agent_name}\"*",
            ]),
            ("How It Works", [
                "{agent_display} inherits from `BasicAgent` and implements `perform(**kwargs)`. Call it with your parameters and get a string result back. Tags: {tag_list}.",
            ]),
        ],
    },
    "how_to_guide": {
        "category": "getting-started",
        "weight": 5,
        "tags": ["howto", "guide", "tutorial"],
        "titles": [
            "How To: {topic}",
            "Step-by-Step: {topic}",
            "A Beginner's Guide to {topic}",
        ],
        "sections": [
            ("What You'll Learn", [
                "This guide walks you through **{topic_lower}**. By the end you'll understand the key concepts and be ready to apply them.",
            ]),
            ("Prerequisites", [
                "- Python 3.11+\n- A text editor\n- The RAPP repo cloned or forked\n- About 15 minutes",
            ]),
        ],
        "topics": [
            "Writing Your First Agent", "The __manifest__ Dict — Every Field Explained",
            "Testing Agents Locally Before Publishing", "Using the Agent Workbench",
            "Publishing to the RAPP Registry", "Agent Versioning with Semver",
            "Debugging Common Manifest Errors", "The Single-File Principle and Why It Matters",
            "Working with the Agent Store Offline", "Setting Up Environment Variables for Agents",
            "Forking RAPP for Your Organization", "Creating Integration Agents for External APIs",
        ],
    },
    "best_practice": {
        "category": "best-practices",
        "weight": 4,
        "tags": ["best-practices", "patterns", "quality"],
        "titles": [
            "Best Practice: {topic}",
            "Pattern: {topic}",
            "Do This, Not That: {topic}",
        ],
        "sections": [
            ("The Pattern", [
                "This article covers a proven pattern for **{topic_lower}** in the RAPP ecosystem.",
            ]),
            ("Why It Matters", [
                "Agents that follow this pattern get higher community ratings, faster tier promotion, and fewer issues in production.",
            ]),
        ],
        "topics": [
            "Error Handling in perform()", "Writing Descriptive Manifest Metadata",
            "Graceful Degradation Without API Keys", "Keeping Agents Under 200 Lines",
            "Testing Agents Before Submission", "Returning Structured Data as Strings",
        ],
    },
    "troubleshooting": {
        "category": "troubleshooting",
        "weight": 3,
        "tags": ["troubleshooting", "debugging", "errors"],
        "titles": [
            "Troubleshooting: {topic}",
            "Fix: {topic}",
            "Why Your Agent {topic} (And How to Fix It)",
        ],
        "sections": [
            ("Symptoms", [
                "You'll encounter this when building or testing agents. The typical symptom is an error or unexpected behavior.",
            ]),
            ("Solution", [
                "1. Check your `__manifest__` for syntax errors\n2. Run `python build_registry.py` locally\n3. Run `pytest tests/test_agent_contract.py -k \"your-agent\"`\n4. Compare against the template in CONTRIBUTING.md",
            ]),
        ],
        "topics": [
            "Fails build_registry.py Validation", "perform() Returns None Instead of String",
            "Manifest Not Found by AST Parser", "display_name Mismatch Error",
            "Agent Works Locally but Fails CI", "Agent File Not Discovered by Registry",
        ],
    },
    "architecture_explainer": {
        "category": "architecture",
        "weight": 3,
        "tags": ["architecture", "internals", "technical"],
        "titles": [
            "Architecture: {topic}",
            "How {topic} Works in RAPP",
            "Inside RAPP: {topic}",
        ],
        "sections": [
            ("Overview", [
                "This article explains **{topic_lower}** — a core architectural decision in RAPP. Understanding this helps you build better agents.",
            ]),
        ],
        "topics": [
            "AST-Based Manifest Extraction", "The Registry Build Pipeline",
            "GitHub Issues as an API", "The Federation Protocol",
            "Zero-Dependency Web Store Architecture", "Contract Testing with Pytest",
        ],
    },
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# THREAD RULES — data-driven forum thread generation
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THREAD_RULES = {
    "help_question": {
        "channel": "help", "weight": 6,
        "titles": ["How do I {action}?", "Help: {action}", "Quick question about {action}"],
        "bodies": [
            "I'm trying to {action_lower} but I'm stuck. Has anyone done this?",
            "Probably basic but — how do I {action_lower}? Still learning the ropes.",
        ],
        "actions": [
            "test my agent locally before submitting", "add environment variables to my agent",
            "get my agent promoted to verified", "debug why build_registry.py rejects my manifest",
            "handle missing API keys gracefully", "use the Agent Workbench in the browser",
            "run pytest for just my agent", "install agents from chat using the remote agent",
            "write an agent that calls an external REST API",
        ],
    },
    "discussion": {
        "channel": "general", "weight": 5,
        "titles": ["What's your experience with {topic}?", "Thoughts on {topic}?", "The case for {topic}"],
        "bodies": ["Curious what the community thinks about {topic_lower}.", "What's worked for you with {topic_lower}?"],
        "topics": [
            "the single-file principle", "the Holo card system", "federation for enterprise",
            "agent testing tooling", "community quality standards", "documentation best practices",
        ],
    },
    "showcase": {
        "channel": "showcase", "weight": 4,
        "titles": ["Just published: {agent_display}", "Showcase: {agent_display}", "My first agent: {agent_display}"],
        "bodies": [
            "Excited to share **{agent_display}** (`{agent_name}`)! {description}\n\nFeedback welcome!",
            "Just got **{agent_display}** published. A {category} agent that {description_lower}.\n\nCheck it out on the Agent Store!",
        ],
    },
    "idea": {
        "channel": "ideas", "weight": 3,
        "titles": ["Idea: {idea}", "Feature request: {idea}", "What if we had {idea}?"],
        "bodies": ["I think {idea_lower} would make RAPP significantly better."],
        "ideas": [
            "an agent dependency graph visualizer", "automatic Holo card generation on publish",
            "agent analytics with download counts", "a diff view for version updates",
            "cross-instance agent search", "periodic community build challenges",
        ],
    },
}


REPLY_RULES = {
    "helpful_answer": {
        "weight": 6,
        "templates": [
            "Here's what worked for me:\n\n1. Check your `__manifest__`\n2. Run `python build_registry.py` locally\n3. Check the wiki for more details\n\nHope that helps!",
            "I had the same issue. The fix was to check the manifest fields match what the AST parser expects.",
            "Short answer: the key thing is that the registry builder uses AST parsing, not imports. Your code structure matters.",
        ],
    },
    "agree": {
        "weight": 4,
        "templates": ["Totally agree. Same experience.", "+1 on this.", "This. Someone needed to say it."],
    },
    "share_experience": {
        "weight": 5,
        "templates": [
            "I built something similar. Keep `perform()` focused on one thing and return clean strings.",
            "The single-file constraint actually makes things simpler. You stop overthinking architecture.",
            "From my experience publishing agents: reading other people's code teaches you more than docs.",
        ],
    },
    "constructive_feedback": {
        "weight": 3,
        "templates": [
            "Nice work! Consider adding more tags for discoverability.",
            "Looks solid. Have you thought about handling missing API keys gracefully?",
            "Good start! Look at how `@kody-w/context_memory.py` handles similar patterns — clean reference.",
        ],
    },
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# AUTHORS — simulated community members
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUTHORS = [
    "AgentSmith", "RAPPBuilder", "CodeForge", "SingleFileDevotee",
    "ManifestMaster", "PyAgent", "RegistryRunner", "HoloDeckEng",
    "FederationFan", "WorkbenchWizard", "PipelinePro", "IntegrationDev",
]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ENGINE CORE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def _uid():
    return f"{int(datetime.now(timezone.utc).timestamp())}-{random.randint(1000,9999)}"

def _pick_weighted(rules):
    names = list(rules.keys())
    weights = [rules[n]["weight"] for n in names]
    chosen = random.choices(names, weights=weights, k=1)[0]
    return chosen, rules[chosen]

def _fill(template, ctx):
    try:
        return template.format(**ctx)
    except (KeyError, IndexError):
        return template

def _load_registry():
    """Load agents from registry.json for real agent data."""
    reg_path = Path(__file__).parent.parent / "registry.json"
    if not reg_path.exists():
        return []
    with open(reg_path) as f:
        data = json.load(f)
    return data.get("agents", [])

def _agent_context(agent):
    name = agent.get("name", "@unknown/unknown")
    pub = name.split("/")[0].lstrip("@") if "/" in name else "unknown"
    tags = agent.get("tags", [])
    return {
        "agent_name": name,
        "agent_display": agent.get("display_name", name),
        "description": agent.get("description", "An agent in the RAPP registry."),
        "description_lower": agent.get("description", "").lower().rstrip("."),
        "publisher": f"@{pub}", "publisher_slug": pub,
        "category": agent.get("category", "community"),
        "quality_tier": agent.get("quality_tier", "community"),
        "version": agent.get("version", "1.0.0"),
        "agent_path": agent.get("_file", f"@{pub}/{name.split('/')[-1]}.py"),
        "tag_list": ", ".join(tags) if tags else "none",
        "tags": tags,
    }


class RappterpediaAgent(BasicAgent):
    def __init__(self):
        self.name = __manifest__["display_name"]
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "The operation to perform",
                        "enum": [
                            "search", "generate_article", "generate_thread",
                            "list_articles", "list_threads",
                            "generate_burst", "export", "stats",
                        ],
                    },
                    "query": {
                        "type": "string",
                        "description": "Search query (for search operation)",
                    },
                    "category": {
                        "type": "string",
                        "description": "Filter by category/channel",
                    },
                    "count": {
                        "type": "integer",
                        "description": "Number of items to generate (for burst)",
                    },
                    "topic": {
                        "type": "string",
                        "description": "Optional topic hint for generation",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)
        self._articles = []
        self._threads = []
        self._agents = _load_registry()
        self._tick = 0

    def perform(self, **kwargs):
        """Dispatch to operation handlers."""
        operation = kwargs.get("operation", "stats")
        handlers = {
            "search": self._search,
            "generate_article": self._generate_article,
            "generate_thread": self._generate_thread,
            "list_articles": self._list_articles,
            "list_threads": self._list_threads,
            "generate_burst": self._generate_burst,
            "export": self._export,
            "stats": self._stats,
        }
        handler = handlers.get(operation)
        if not handler:
            return f"Unknown operation: {operation}. Available: {', '.join(handlers.keys())}"
        return handler(kwargs)

    # ── Operations ────────────────────────────────────

    def _search(self, params):
        query = params.get("query", "").lower()
        if not query:
            return "Please provide a 'query' parameter to search."
        results = []
        for a in self._articles:
            text = (a["title"] + " " + a["content"] + " " + " ".join(a.get("tags", []))).lower()
            if query in text:
                results.append(f"[WIKI] {a['title']} ({a['category']})")
        for t in self._threads:
            text = (t["title"] + " " + t["content"]).lower()
            if query in text:
                results.append(f"[FORUM] {t['title']} ({t['channel']})")
        if not results:
            return f"No results found for '{query}'."
        return f"Found {len(results)} results:\n\n" + "\n".join(results[:20])

    def _generate_article(self, params):
        self._tick += 1
        rule_name, rule = _pick_weighted(ARTICLE_RULES)
        ctx = {"tick": self._tick}

        topic = params.get("topic", "")
        if topic:
            ctx.update({"topic": topic, "topic_lower": topic.lower()})
        elif rule_name in ("agent_deep_dive", ) and self._agents:
            agent = random.choice(self._agents)
            ctx.update(_agent_context(agent))
        elif "topics" in rule:
            chosen = random.choice(rule["topics"])
            ctx.update({"topic": chosen, "topic_lower": chosen.lower()})

        title = _fill(random.choice(rule["titles"]), ctx)
        parts = []
        for heading, templates in rule["sections"]:
            body = _fill(random.choice(templates), ctx)
            parts.append(f"## {heading}\n\n{body}")
        content = "\n\n".join(parts)

        article = {
            "id": _uid(), "title": title, "category": rule["category"],
            "tags": rule.get("tags", []), "content": content,
            "author": random.choice(AUTHORS), "created": _now(), "updated": _now(),
        }
        self._articles.append(article)
        return f"Generated wiki article:\n\nTitle: {title}\nCategory: {rule['category']}\nAuthor: {article['author']}\n\n{content}"

    def _generate_thread(self, params):
        self._tick += 1
        rule_name, rule = _pick_weighted(THREAD_RULES)
        ctx = {"tick": self._tick}

        if rule_name == "showcase" and self._agents:
            ctx.update(_agent_context(random.choice(self._agents)))
        elif rule_name == "help_question":
            action = random.choice(rule["actions"])
            ctx.update({"action": action, "action_lower": action.lower()})
        elif rule_name == "idea":
            idea = random.choice(rule["ideas"])
            ctx.update({"idea": idea, "idea_lower": idea.lower()})
        elif "topics" in rule:
            ctx.update({"topic": random.choice(rule["topics"]), "topic_lower": random.choice(rule["topics"]).lower()})

        title = _fill(random.choice(rule["titles"]), ctx)
        body = _fill(random.choice(rule["bodies"]), ctx)

        replies = []
        for _ in range(random.randint(1, 3)):
            rn, rr = _pick_weighted(REPLY_RULES)
            replies.append({
                "id": _uid(), "author": random.choice(AUTHORS),
                "content": random.choice(rr["templates"]), "created": _now(),
            })

        thread = {
            "id": _uid(), "title": title, "channel": rule["channel"],
            "content": body, "author": random.choice(AUTHORS),
            "created": _now(), "updated": _now(),
            "votes": random.randint(1, 12), "replies": replies,
        }
        self._threads.append(thread)

        reply_text = "\n".join(f"  - {r['author']}: {r['content'][:60]}..." for r in replies)
        return f"Generated forum thread:\n\nTitle: {title}\nChannel: {rule['channel']}\nAuthor: {thread['author']}\nReplies: {len(replies)}\n\n{body}\n\nReplies:\n{reply_text}"

    def _list_articles(self, params):
        cat = params.get("category", "")
        filtered = [a for a in self._articles if not cat or a["category"] == cat]
        if not filtered:
            return "No articles found." + (f" (category: {cat})" if cat else "")
        lines = [f"- [{a['category']}] {a['title']} (by {a['author']})" for a in filtered]
        return f"{len(filtered)} articles:\n\n" + "\n".join(lines)

    def _list_threads(self, params):
        chan = params.get("category", "")  # accept 'category' as alias for channel
        filtered = [t for t in self._threads if not chan or t["channel"] == chan]
        if not filtered:
            return "No threads found." + (f" (channel: {chan})" if chan else "")
        lines = [f"- [{t['channel']}] {t['title']} ({len(t.get('replies',[]))} replies)" for t in filtered]
        return f"{len(filtered)} threads:\n\n" + "\n".join(lines)

    def _generate_burst(self, params):
        count = int(params.get("count", 5))
        results = []
        for _ in range(count):
            if random.random() < 0.5:
                r = self._generate_article(params)
                results.append("ARTICLE: " + r.split("\n")[2] if len(r.split("\n")) > 2 else r[:80])
            else:
                r = self._generate_thread(params)
                results.append("THREAD: " + r.split("\n")[2] if len(r.split("\n")) > 2 else r[:80])
        return f"Burst complete: generated {count} items.\n\n" + "\n".join(results)

    def _export(self, params):
        export = {
            "version": "1.0",
            "exported": _now(),
            "articles": self._articles,
            "threads": self._threads,
            "stats": {
                "total_articles": len(self._articles),
                "total_threads": len(self._threads),
                "total_replies": sum(len(t.get("replies", [])) for t in self._threads),
            },
        }
        return json.dumps(export, indent=2)

    def _stats(self, params):
        total_replies = sum(len(t.get("replies", [])) for t in self._threads)
        categories = {}
        for a in self._articles:
            categories[a["category"]] = categories.get(a["category"], 0) + 1
        channels = {}
        for t in self._threads:
            channels[t["channel"]] = channels.get(t["channel"], 0) + 1

        cat_lines = "\n".join(f"  - {k}: {v}" for k, v in sorted(categories.items()))
        chan_lines = "\n".join(f"  - {k}: {v}" for k, v in sorted(channels.items()))

        return (
            f"Rappterpedia Stats\n"
            f"==================\n"
            f"Wiki Articles: {len(self._articles)}\n"
            f"Forum Threads: {len(self._threads)}\n"
            f"Total Replies:  {total_replies}\n"
            f"Registry Agents: {len(self._agents)}\n\n"
            f"Articles by Category:\n{cat_lines}\n\n"
            f"Threads by Channel:\n{chan_lines}"
        )


# ── Standalone execution ─────────────────────────────
if __name__ == "__main__":
    agent = RappterpediaAgent()
    print(agent.perform(operation="stats"))
    print()
    print(agent.perform(operation="generate_article"))
    print()
    print(agent.perform(operation="generate_thread"))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
