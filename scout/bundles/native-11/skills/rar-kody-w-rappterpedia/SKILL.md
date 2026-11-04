---
name: "rar-kody-w-rappterpedia"
description: "Generates wiki articles, forum threads, and replies for the Rappterpedia knowledge base from rules-as-data templates."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rappterpedia_agent", "rar_sha256": "078d5bbb37e91cb052e9cfdc540aa5024d6a573f0be14df860c7df4c4ba08f69", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.1", "author": "Kody Wildfeuer", "tags": ["wiki", "forum", "content", "community", "rappterpedia", "engine"]}
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
