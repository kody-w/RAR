---
name: "rar-kody-w-rappterpedia"
description: "Generates wiki articles, forum threads, and replies for the Rappterpedia knowledge base from rules-as-data templates."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rappterpedia_agent", "rar_sha256": "8c34061cf1ed1fa86071adb0c21896e629879d155405908404d5d6a390233fbb", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rappterpedia_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/rappterpedia:efcde0edda294a7f89d4613da44dd2070110b8167d04b6f478b73784c1243316", "kind": "skill"}, "version": "1.1.1", "author": "Kody Wildfeuer", "tags": ["wiki", "forum", "content", "community", "rappterpedia", "engine"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/rappterpedia_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rappterpedia_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
