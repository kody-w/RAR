"""
Rappterpedia Agent — Community wiki & forum content engine for the RAR ecosystem.

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
    "name": "@kody/rappterpedia-agent",
    "version": "1.0.0",
    "display_name": "RappterpediaAgent",
    "description": "Community wiki & forum content engine. Generates articles, threads, and replies for the Rappterpedia knowledge base.",
    "author": "Kody Wildfeuer",
    "tags": ["wiki", "forum", "content", "community", "rappterpedia", "engine"],
    "category": "productivity",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
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
                "**{agent_display}** (`{agent_name}`) is a {category} agent in the RAR registry. {description}\n\nPublished by `{publisher}`, it's at version {version} with **{quality_tier}** quality tier.",
            ]),
            ("Installation", [
                "### From the Agent Store\n\nBrowse to the agent card and download the `.py` file. Drop it into your `agents/` folder.\n\n### Direct Fetch\n\n```bash\ncurl -O https://raw.githubusercontent.com/kody-w/RAR/main/agents/{agent_path}\n```\n\n### From Chat\n\nAsk the RAR Remote Agent: *\"Install {agent_name}\"*",
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
                "- Python 3.11+\n- A text editor\n- The RAR repo cloned or forked\n- About 15 minutes",
            ]),
        ],
        "topics": [
            "Writing Your First Agent", "The __manifest__ Dict — Every Field Explained",
            "Testing Agents Locally Before Publishing", "Using the Agent Workbench",
            "Publishing to the RAR Registry", "Agent Versioning with Semver",
            "Debugging Common Manifest Errors", "The Single-File Principle and Why It Matters",
            "Working with the Agent Store Offline", "Setting Up Environment Variables for Agents",
            "Forking RAR for Your Organization", "Creating Integration Agents for External APIs",
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
                "This article covers a proven pattern for **{topic_lower}** in the RAR ecosystem.",
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
            "How {topic} Works in RAR",
            "Inside RAR: {topic}",
        ],
        "sections": [
            ("Overview", [
                "This article explains **{topic_lower}** — a core architectural decision in RAR. Understanding this helps you build better agents.",
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
        "bodies": ["I think {idea_lower} would make RAR significantly better."],
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
            "Good start! Look at how `@kody/context_memory.py` handles similar patterns — clean reference.",
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
        "description": agent.get("description", "An agent in the RAR registry."),
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
