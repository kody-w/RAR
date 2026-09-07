---
name: "rar-kody-w-rappterpedia"
description: "Generates wiki articles, forum threads, and replies for the Rappterpedia knowledge base from rules-as-data templates."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rappterpedia_agent", "rar_sha256": "8c34061cf1ed1fa86071adb0c21896e629879d155405908404d5d6a390233fbb", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.1.1", "author": "Kody Wildfeuer", "tags": ["wiki", "forum", "content", "community", "rappterpedia", "engine"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rappterpedia_agent.py` and embedded as the fenced Python below (sha256 8c34061cf1ed1fa8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rappterpedia_agent.py` first:

```bash
python3 rappterpedia_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rappterpedia_agent.py   # or on stdin
python3 rappterpedia_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
