#!/usr/bin/env python3
"""
Rappterpedia Content Engine 📚
Autonomous wiki & forum content generation following the RAPPterverse
rules-as-data pattern. Articles and threads are defined as DATA
(templates + context), not code. Adding new content types = adding
a dict entry, zero code changes.

Generates wiki articles, forum threads, and replies that build out
the Rappterpedia knowledge base with genuine, useful content about
the RAPP Agent ecosystem.

Usage:
  Single tick:  python rappterpedia/rappterpedia_engine.py
  Dry run:      python rappterpedia/rappterpedia_engine.py --dry-run
  No git:       python rappterpedia/rappterpedia_engine.py --no-push
  Seed only:    python rappterpedia/rappterpedia_engine.py --seed
  Full burst:   python rappterpedia/rappterpedia_engine.py --burst 20
"""

from __future__ import annotations

import json
import random
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).parent
RAR_DIR = BASE_DIR.parent
STATE_FILE = BASE_DIR / "rappterpedia_state.json"

# Try to import agent brain for LLM-driven content enrichment
try:
    sys.path.insert(0, str(Path(__file__).parent.parent.parent / "rappterverse" / "scripts"))
    from agent_brain import AgentBrain
    HAS_BRAIN = True
except ImportError:
    HAS_BRAIN = False


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# WIKI ARTICLE RULES — data-driven article generation.
# Each rule defines a type of wiki content that can be generated.
#
#   category:    wiki category to file under
#   weight:      base probability of this type being chosen
#   tags:        tag pool to draw from
#   titles:      title patterns filled from context
#   sections:    content section patterns (assembled into full articles)
#   requires:    conditions (min existing articles, etc.)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ARTICLE_RULES: dict[str, dict] = {

    "agent_deep_dive": {
        "category": "agents",
        "weight": 6,
        "tags": ["agent", "deep-dive", "reference"],
        "titles": [
            "Deep Dive: {agent_display} — What It Does and How to Use It",
            "Understanding {agent_display}: A Complete Guide",
            "{agent_display} Explained: From Install to Production",
            "How {agent_display} Works Under the Hood",
            "Getting the Most Out of {agent_display}",
        ],
        "sections": [
            {
                "heading": "Overview",
                "templates": [
                    "**{agent_display}** (`{agent_name}`) is a {category} agent in the RAR registry. {description}\n\nPublished by `{publisher}`, it's currently at version {version} with a quality tier of **{quality_tier}**.",
                    "The `{agent_name}` agent handles {description_lower}. It ships as a single `.py` file following the RAR single-file principle — everything you need is in one place.",
                ],
            },
            {
                "heading": "Installation",
                "templates": [
                    "### From the Agent Store\n\nBrowse to [{agent_display}](../index.html), click the agent card, and download the `.py` file. Drop it into your `agents/` folder.\n\n### Direct Fetch\n\n```bash\ncurl -O https://raw.githubusercontent.com/kody-w/RAR/main/agents/{agent_path}\n```\n\n### From Chat\n\nAsk the RAR Remote Agent:\n> *\"Install {agent_name}\"*",
                ],
            },
            {
                "heading": "Configuration",
                "templates": [
                    "This agent {env_section}.\n\nThe manifest declares these dependencies: {deps}.",
                    "{agent_display} {env_section}. Check the `__manifest__` in the source file for the full dependency list.",
                ],
            },
            {
                "heading": "How It Works",
                "templates": [
                    "{agent_display} inherits from `BasicAgent` and implements the standard `perform(**kwargs)` interface. It accepts keyword arguments, processes them, and returns a string result.\n\nThe agent lives in `agents/{agent_path}` and weighs in at {size_kb} KB ({lines} lines). Tags: {tag_list}.",
                    "Like all RAR agents, {agent_display} follows the perform-and-return pattern. Call `perform()` with your parameters and get a string result back. No side effects on the registry, no state mutations outside the agent's scope.",
                ],
            },
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
            "{topic} — The Easy Way",
            "Everything You Need to Know About {topic}",
        ],
        "sections": [
            {
                "heading": "What You'll Learn",
                "templates": [
                    "This guide walks you through **{topic_lower}**. By the end, you'll understand the key concepts and be ready to apply them in your own agent development workflow.",
                    "Whether you're brand new to RAR or an experienced agent builder, this guide covers {topic_lower} from the ground up. No prerequisites — just curiosity.",
                ],
            },
            {
                "heading": "Prerequisites",
                "templates": [
                    "- Python 3.11+ installed\n- A text editor (VS Code, Cursor, or even Notepad)\n- The RAR repo cloned or forked\n- About 15 minutes of your time",
                    "- Basic familiarity with the [Agent Store](../index.html)\n- Python 3.11+ (check with `python --version`)\n- A GitHub account (for publishing)",
                ],
            },
        ],
        "topic_pool": [
            "Writing Your First Agent",
            "The __manifest__ Dict — Every Field Explained",
            "Testing Agents Locally Before Publishing",
            "Using the Agent Workbench",
            "Understanding Agent Categories",
            "Publishing to the RAR Registry",
            "Setting Up Environment Variables for Agents",
            "Forking RAR for Your Organization",
            "Reading and Understanding registry.json",
            "Using the RAR Remote Agent from Chat",
            "Agent Versioning with Semver",
            "Debugging Common Manifest Errors",
            "Building Agents That Handle Missing Config Gracefully",
            "Using the Holo Card System",
            "Contributing to Rappterpedia",
            "Understanding the Build Pipeline",
            "Agent Dependencies and the BasicAgent Class",
            "Creating Integration Agents for External APIs",
            "The Single-File Principle and Why It Matters",
            "Working with the Agent Store Offline",
        ],
    },

    "architecture_explainer": {
        "category": "architecture",
        "weight": 3,
        "tags": ["architecture", "internals", "technical"],
        "titles": [
            "Architecture: {arch_topic}",
            "How {arch_topic} Works in RAR",
            "Inside RAR: {arch_topic}",
            "Technical Deep Dive: {arch_topic}",
        ],
        "sections": [
            {
                "heading": "Overview",
                "templates": [
                    "This article explains **{arch_topic_lower}** — one of the core architectural decisions in the RAR ecosystem. Understanding this helps you build better agents and contribute more effectively.",
                    "RAR's approach to {arch_topic_lower} is intentionally simple but surprisingly powerful. Here's how it works and why it was designed this way.",
                ],
            },
        ],
        "topic_pool": [
            "AST-Based Manifest Extraction",
            "The Registry Build Pipeline",
            "IndexedDB and Local-First Storage",
            "GitHub Issues as an API",
            "The Federation Protocol",
            "Single-File Agent Packaging",
            "Zero-Dependency Web Store Architecture",
            "Contract Testing with Pytest",
            "Agent Namespace Resolution",
            "The Holo Card Generation Pipeline",
            "CI/CD with GitHub Actions",
            "State Management via JSON Files",
        ],
    },

    "integration_guide": {
        "category": "integrations",
        "weight": 3,
        "tags": ["integration", "external", "API"],
        "titles": [
            "Integrating RAR Agents with {platform}",
            "How to Connect {platform} Using RAR Agents",
            "{platform} + RAR: A Practical Guide",
            "Building a {platform} Agent for RAR",
        ],
        "sections": [
            {
                "heading": "Overview",
                "templates": [
                    "This guide covers how to build or use RAR agents that integrate with **{platform}**. Whether you're using an existing integration agent or building your own, this article has you covered.",
                    "Connecting {platform} to the RAPP ecosystem is straightforward thanks to RAR's single-file agent model. Here's how to get started.",
                ],
            },
            {
                "heading": "Environment Setup",
                "templates": [
                    "Most {platform} integrations require API credentials. Store these as environment variables and declare them in your agent's `requires_env` manifest field:\n\n```python\n\"requires_env\": [\"{platform_upper}_API_KEY\", \"{platform_upper}_URL\"],\n```\n\nNever hardcode credentials. The agent should gracefully handle missing env vars by returning an error message.",
                ],
            },
        ],
        "platform_pool": [
            "Dynamics 365",
            "SharePoint",
            "Salesforce",
            "ServiceNow",
            "Slack",
            "Microsoft Teams",
            "Power Automate",
            "Azure DevOps",
            "Jira",
            "HubSpot",
            "Zendesk",
            "Twilio",
        ],
    },

    "best_practice": {
        "category": "best-practices",
        "weight": 4,
        "tags": ["best-practices", "patterns", "quality"],
        "titles": [
            "Best Practice: {practice}",
            "Pattern: {practice}",
            "Do This, Not That: {practice}",
            "{practice} — Lessons Learned",
        ],
        "sections": [
            {
                "heading": "The Pattern",
                "templates": [
                    "This article covers a proven pattern for **{practice_lower}** in the RAR ecosystem. Following this pattern will help your agents be more robust, maintainable, and community-friendly.",
                    "After reviewing hundreds of agent submissions, this pattern has emerged as a best practice for {practice_lower}. Here's what works and what doesn't.",
                ],
            },
            {
                "heading": "Why It Matters",
                "templates": [
                    "Agents that follow this pattern tend to get higher community ratings, faster promotion through quality tiers, and fewer issues in production.",
                    "This pattern exists because RAR agents run in diverse environments — different Python versions, different OS, different env var configurations. Defensive coding isn't optional.",
                ],
            },
        ],
        "topic_pool": [
            "Error Handling in perform()",
            "Writing Descriptive Manifest Metadata",
            "Structuring Agent Parameters",
            "Idempotent Agent Operations",
            "Graceful Degradation Without API Keys",
            "Keeping Agents Under 200 Lines",
            "Writing Self-Documenting Docstrings",
            "Version Bumping Strategy",
            "Testing Agents Before Submission",
            "Naming Conventions That Scale",
            "Handling Large Inputs Safely",
            "Returning Structured Data as Strings",
        ],
    },

    "troubleshooting": {
        "category": "troubleshooting",
        "weight": 3,
        "tags": ["troubleshooting", "debugging", "errors"],
        "titles": [
            "Troubleshooting: {problem}",
            "Fix: {problem}",
            "Common Issue: {problem}",
            "Why Your Agent {problem} (And How to Fix It)",
        ],
        "sections": [
            {
                "heading": "Symptoms",
                "templates": [
                    "You might encounter this issue when {symptom_context}. The typical symptom is {symptom_detail}.",
                    "This is one of the most common issues new agent builders face. You'll know you have this problem when {symptom_detail}.",
                ],
            },
            {
                "heading": "Root Cause",
                "templates": [
                    "The root cause is usually {root_cause}. This happens because the registry builder uses AST parsing, which means your Python code doesn't get executed during the build — it gets statically analyzed.",
                    "This typically comes down to {root_cause}. The fix is straightforward once you understand what's happening.",
                ],
            },
            {
                "heading": "Solution",
                "templates": [
                    "To fix this:\n\n1. Check your `__manifest__` dict for syntax errors\n2. Run `python build_registry.py` locally to see the full error\n3. Run `pytest tests/test_agent_contract.py -k \"your-agent\"` for detailed diagnostics\n4. Compare your manifest against the template in CONTRIBUTING.md",
                ],
            },
        ],
        "topic_pool": [
            "Fails build_registry.py Validation",
            "Won't Import in Tests",
            "perform() Returns None Instead of String",
            "Manifest Not Found by AST Parser",
            "display_name Mismatch Error",
            "Missing BasicAgent Inheritance",
            "Environment Variables Not Loading",
            "Agent Works Locally but Fails CI",
            "Category Not Recognized",
            "Version Format Invalid",
            "Tags Field is Empty",
            "Agent File Not Discovered by Registry",
        ],
    },

    "community_spotlight": {
        "category": "community",
        "weight": 2,
        "tags": ["community", "spotlight", "showcase"],
        "titles": [
            "Publisher Spotlight: {publisher}",
            "Namespace Tour: What's Inside @{publisher_slug}",
            "Community Highlight: The {publisher} Collection",
        ],
        "sections": [
            {
                "heading": "About",
                "templates": [
                    "The **@{publisher_slug}** namespace is home to {agent_count} agents focused on {focus_area}. This article tours the highlights and explains how the collection fits together.",
                    "Let's explore what **@{publisher_slug}** has published in the RAR registry — {agent_count} agents spanning {category_spread}.",
                ],
            },
        ],
    },

    "federation_topic": {
        "category": "federation",
        "weight": 2,
        "tags": ["federation", "self-hosting", "governance"],
        "titles": [
            "Federation Guide: {fed_topic}",
            "Running Your Own RAR: {fed_topic}",
            "Self-Hosting RAR — {fed_topic}",
        ],
        "sections": [
            {
                "heading": "Overview",
                "templates": [
                    "RAR's federation model lets you run your own agent store while optionally syncing with the main registry. This article covers **{fed_topic_lower}**.",
                    "One of RAR's unique features is federation — running independent instances that can share agents upstream. Here's how **{fed_topic_lower}** works.",
                ],
            },
        ],
        "topic_pool": [
            "Setting Up Your First Federated Instance",
            "Configuring rar.config.json",
            "Upstream Sync: Pulling Public Agents",
            "Private Namespaces in Federated Stores",
            "Custom CI/CD for Federated Instances",
            "Governance in Federated Communities",
            "Migration: Moving Agents Between Instances",
        ],
    },
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FORUM THREAD RULES — data-driven thread/reply generation.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THREAD_RULES: dict[str, dict] = {

    "help_question": {
        "channel": "help",
        "weight": 6,
        "titles": [
            "How do I {action}?",
            "Help: {action}",
            "Can't figure out how to {action}",
            "Newbie question: {action}",
            "Quick question about {action}",
        ],
        "bodies": [
            "I'm trying to {action_lower} but I'm stuck. I've read the wiki but can't find a clear answer. Has anyone done this before?",
            "Probably a basic question but — how do I {action_lower}? I'm new to RAR and still learning the ropes.",
            "Searched the wiki and found some related articles but nothing that directly answers this. How do you {action_lower} in practice?",
        ],
        "action_pool": [
            "test my agent locally before submitting",
            "add environment variables to my agent",
            "update my agent's version after a bug fix",
            "get my agent promoted from community to verified",
            "debug why build_registry.py rejects my manifest",
            "make my agent work with Azure OpenAI",
            "handle missing API keys gracefully",
            "use the Agent Workbench in the browser",
            "create agents in a team namespace",
            "run pytest for just my agent",
            "fetch agents from the registry programmatically",
            "set up a federated RAR instance",
            "integrate my agent with Dynamics 365",
            "make my agent return structured data",
            "add my agent to the Holo card system",
            "submit an agent via the Store UI instead of PR",
            "install agents from chat using the remote agent",
            "write an agent that calls an external REST API",
            "contribute a wiki article to Rappterpedia",
        ],
    },

    "discussion": {
        "channel": "general",
        "weight": 5,
        "titles": [
            "What's your experience with {topic}?",
            "Let's talk about {topic}",
            "Thoughts on {topic}?",
            "Unpopular opinion: {topic}",
            "The case for {topic}",
        ],
        "bodies": [
            "I've been thinking about this a lot lately. Curious what the community thinks about {topic_lower}.",
            "Would love to hear different perspectives on {topic_lower}. What's worked for you?",
            "This came up while I was building an agent and I realized there's no consensus. What's the community take on {topic_lower}?",
        ],
        "topic_pool": [
            "the single-file principle is genius",
            "we need more integration agents",
            "the Holo card system makes agents fun to collect",
            "federation could be huge for enterprise teams",
            "agent testing needs better tooling",
            "the workbench should support live preview",
            "community quality tier is too easy to get",
            "RAR needs a changelog feed",
            "the best way to learn is reading other people's agents",
            "we should have an agent of the week",
            "documentation is the hardest part of agent building",
            "the AST-based manifest extraction is underrated",
            "more vertical templates would help enterprise adoption",
            "the web store working offline is a killer feature",
        ],
    },

    "showcase": {
        "channel": "showcase",
        "weight": 4,
        "titles": [
            "Just published: {agent_display}",
            "Showcase: {agent_display} — {short_desc}",
            "Built a {category} agent — feedback welcome",
            "My first agent submission: {agent_display}",
            "{agent_display} is live on the store!",
        ],
        "bodies": [
            "Excited to share **{agent_display}** (`{agent_name}`)! {description}\n\nBuilt it to solve a real problem I was having. Would love feedback from the community.",
            "Just got **{agent_display}** published to the registry. It's a {category} agent that {description_lower}.\n\nKey features:\n- Single-file, zero external dependencies\n- Handles missing env vars gracefully\n- Tested with `pytest`\n\nCheck it out on the [Agent Store](../index.html) and let me know what you think!",
            "After a few iterations, **{agent_display}** is ready for the world. {description}\n\nCurrently at {quality_tier} tier. Hoping to get promoted to verified with community support!",
        ],
    },

    "idea": {
        "channel": "ideas",
        "weight": 3,
        "titles": [
            "Idea: {idea}",
            "Feature request: {idea}",
            "What if we had {idea}?",
            "Proposal: {idea}",
        ],
        "bodies": [
            "I think {idea_lower} would make the RAR ecosystem significantly better. Here's my thinking:\n\nThe current approach works but {rationale}. This would help both new and experienced agent builders.",
            "Proposing {idea_lower} for the community to discuss. Not sure if this is already planned but I think it would {benefit}.",
        ],
        "idea_pool": [
            ("an agent dependency graph visualizer", "you can't easily see which agents depend on each other", "debug complex agent chains"),
            ("automatic Holo card generation on publish", "card generation is manual right now", "make every new agent feel special from day one"),
            ("a Rappterpedia bot that answers questions from wiki content", "newcomers often ask questions already covered in articles", "reduce repeated questions in the forum"),
            ("agent analytics — download counts and usage stats", "publishers have no visibility into adoption", "help publishers prioritize improvements"),
            ("a diff view for agent version updates", "it's hard to see what changed between versions", "build trust in updates"),
            ("cross-instance agent search for federated stores", "each federated instance is an island", "create a unified agent discovery experience"),
            ("an agent compatibility matrix", "not all agents work in all environments", "save users from trial-and-error"),
            ("a mentorship matching system for new builders", "new builders often struggle alone", "grow the community faster"),
            ("periodic community challenges — build an agent for X", "there's no structured way to motivate new builds", "gamify agent development"),
            ("auto-generated API documentation from agent metadata", "reading source code shouldn't be required", "lower the barrier to using agents"),
        ],
    },

    "bug_report": {
        "channel": "bugs",
        "weight": 2,
        "titles": [
            "Bug: {bug}",
            "{bug} — is this expected?",
            "Possible bug with {bug}",
        ],
        "bodies": [
            "Ran into this while {context}. Not sure if it's a bug or I'm doing something wrong.\n\n**Steps to reproduce:**\n1. {step}\n2. Run the build/test\n3. Observe the unexpected behavior\n\n**Expected:** It should work without errors.\n**Actual:** {symptom}",
        ],
        "bug_pool": [
            ("agent not appearing in registry.json after build", "adding a new agent", "Add agent file to agents/@namespace/", "The agent is missing from the output"),
            ("manifest validation passes but tests fail", "running the full test suite", "Write a valid manifest", "Contract tests report failures on a seemingly valid agent"),
            ("Holo card not generating for new agent", "publishing a new agent", "Submit the agent to the store", "The agent card shows a blank placeholder"),
            ("search not finding agent by tag", "searching in the Agent Store", "Search for a tag that exists in the manifest", "No results returned despite the tag being in the manifest"),
            ("workbench validation gives false positive", "using the browser workbench", "Paste agent code with a known error", "Validation says the agent is valid when it shouldn't be"),
        ],
    },

    "meta": {
        "channel": "meta",
        "weight": 1,
        "titles": [
            "Meta: {meta_topic}",
            "Governance discussion: {meta_topic}",
            "RFC: {meta_topic}",
        ],
        "bodies": [
            "Opening this thread to discuss {meta_topic_lower} as a community. This affects how the registry operates and I think we should have a say.\n\nThe current approach is outlined in the CONSTITUTION but I think it's worth revisiting.",
            "This is a governance discussion about {meta_topic_lower}. All perspectives welcome — this is how we shape the ecosystem together.",
        ],
        "topic_pool": [
            "quality tier promotion criteria",
            "namespace reservation policy",
            "federation governance model",
            "content moderation in the forum",
            "Rappterpedia editorial standards",
            "agent deprecation and removal policy",
            "contribution recognition system",
        ],
    },
}


REPLY_RULES: dict[str, dict] = {
    "helpful_answer": {
        "weight": 6,
        "templates": [
            "Great question! Here's what worked for me:\n\n1. Make sure your `__manifest__` has all required fields\n2. Run `python build_registry.py` locally before submitting\n3. Check the wiki article on \"{related_topic}\" for more details\n\nHope that helps!",
            "I had the same issue. The fix was to {fix_action}. The wiki has a good article on this if you want the full picture.",
            "This is covered in the Rappterpedia wiki under \"{related_topic}\". Short answer: {short_answer}.",
            "The key thing to understand is that {explanation}. Once you get that, the rest follows naturally.",
        ],
    },
    "agree": {
        "weight": 4,
        "templates": [
            "Totally agree. This has been my experience too.",
            "+1 on this. Would love to see it happen.",
            "This. Exactly this. Someone needed to say it.",
            "Been thinking the same thing. Glad someone posted about it.",
        ],
    },
    "share_experience": {
        "weight": 5,
        "templates": [
            "I built something similar. The trick is to keep your `perform()` method focused on one thing and return clean strings. Agents that try to do too much end up fragile.",
            "From my experience publishing a few agents: the single-file constraint actually makes things simpler, not harder. You stop overthinking architecture.",
            "I've been using RAR for a while now and {experience_insight}. Happy to help if you have questions.",
            "Similar situation here. What worked for me was {approach}. Your mileage may vary but it's worth trying.",
        ],
    },
    "constructive_feedback": {
        "weight": 3,
        "templates": [
            "Nice work! One suggestion: consider adding more tags to your manifest. It really helps with discoverability in the store.",
            "Looks solid. Have you thought about handling the case where the API key is missing? A graceful error message goes a long way.",
            "Good start! A few things that could make it even better:\n- Add a more descriptive docstring\n- Bump to 1.1.0 since you added new features\n- Consider adding a `requires_env` field",
            "This is a good foundation. I'd recommend looking at how `@kody/context_memory.py` handles similar patterns — it's a clean reference implementation.",
        ],
    },
    "question": {
        "weight": 3,
        "templates": [
            "Interesting — does this work with federated instances too?",
            "Can you share the manifest for this? I'm trying to build something similar.",
            "How long did it take you to get from idea to published? Curious about the workflow.",
            "What happens if the required env var isn't set? Does it fail gracefully or crash?",
        ],
    },
    "welcome": {
        "weight": 2,
        "templates": [
            "Welcome to the community! Don't hesitate to ask questions — we've all been there.",
            "Great to see new builders! Check out the wiki for guides on getting started.",
            "Welcome! Pro tip: start by reading a few existing agents in the store. The code is the best documentation.",
        ],
    },
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CURATOR REVIEW RULES — data-driven review generation
# Reviews accumulate in state across ticks, like a real community.
# Each tick, reviewers discover agents and write reviews from
# different angles. Reviews reference real agent metadata.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REVIEW_ANGLES: dict[str, dict] = {
    "primary": {
        "weight": 5,
        "templates": {
            "high": [
                "{name} is one of the stronger {cat} agents in the registry. {lines} lines, clean structure, and it does what it says.",
                "This is what a well-built agent looks like. {lines} lines, {tier} tier, and the description matches the implementation.",
                "Solid work. {name} covers its use case thoroughly at {lines} lines. The kind of agent you install and forget about because it just works.",
                "{name} earns its {tier} badge. Thoughtful parameter handling, good tagging, and {lines} lines of focused implementation.",
            ],
            "mid": [
                "{name} gets the job done. {lines} lines of straightforward {cat} logic. Not flashy, but functional.",
                "Decent {cat} agent. {lines} lines, covers the basics. Could use more iteration but the foundation is solid.",
                "A working {cat} agent at {lines} lines. Does what the description promises. Would benefit from richer tagging.",
                "{name} is a functional starting point for {cat}. The perform() method is clean. Another iteration or two and this moves up.",
                "Reviewed {name}: {lines} lines, {tier} tier. Core logic works. More tags and a meatier description would help.",
                "Straightforward {cat} agent. {lines} lines, does its thing. Single-file principle well-executed here.",
            ],
            "low": [
                "{name} is early stage — {lines} lines, {tier} tier. The bones are there but needs more flesh.",
                "Minimal {cat} agent at {lines} lines. Ships the idea but not the execution yet.",
                "{name} reads like a first draft. {lines} lines, basic structure in place. Would love to see a v1.1.",
            ],
        },
    },
    "usability": {
        "weight": 4,
        "templates": {
            "high": [
                "Zero-config setup. Drop {name} in your agents folder and it just works. That's the dream.",
                "Love that {name} needs no env vars. Install and go. The {cat} category needs more agents like this.",
                "The barrier to entry is zero — no API keys, no config. Just download and perform(). More agents should be this easy.",
            ],
            "mid": [
                "You'll need to configure env vars before this does anything useful. Once set up though, it delivers.",
                "The env var requirement is a speed bump but not a dealbreaker. {name} does things you can't do without those credentials.",
                "Setup is straightforward if you already have the credentials. Not a cold-start agent but worth the config.",
            ],
            "low": [
                "Getting {name} running requires some effort. The env vars aren't well-documented in the description.",
                "Needs clearer setup instructions. The manifest lists requirements but doesn't explain what they're for.",
            ],
        },
    },
    "code_quality": {
        "weight": 4,
        "templates": {
            "high": [
                "{lines} lines is the sweet spot for a {cat} agent — enough to be useful, short enough to audit in one read.",
                "Read through the source. Clean perform() method, sensible parameter handling. {lines} lines, no dead code.",
                "Checked the source — follows single-file conventions properly. {name} is a good reference implementation for {cat}.",
                "{lines} lines. Every line earns its place. The perform() method is well-structured and returns clean strings.",
            ],
            "mid": [
                "The implementation is functional at {lines} lines. Some methods could be tighter but nothing egregious.",
                "Code reads fine. Standard patterns, standard structure. Does what it needs to do at {lines} lines.",
                "Source is clean enough. {lines} lines, follows the BasicAgent pattern correctly. Room for polish.",
            ],
            "low": [
                "At {lines} lines, the implementation is thin. The perform() method needs more logic to be genuinely useful.",
                "Basic structure is correct but the actual functionality is minimal. Needs more work.",
            ],
        },
    },
    "community": {
        "weight": 3,
        "templates": {
            "high": [
                "If you're building in {cat}, {name} is worth adding to your deck. Pairs well with other {cat} agents.",
                "{name} fills a gap in the registry. The {cat} category needed exactly this.",
                "This is the kind of agent that makes the ecosystem stronger. Specific, focused, does one thing well.",
                "Would recommend {name} to anyone getting started with {cat}. Shows how a RAR agent should be built.",
            ],
            "mid": [
                "{name} has potential in the {cat} space. Not a must-have yet but trending in the right direction.",
                "Decent addition to the {cat} lineup. A few more iterations and this becomes a go-to.",
                "The {cat} category is getting crowded but {name} differentiates on {diff}.",
            ],
            "low": [
                "{name} needs to find its niche in {cat}. Right now it overlaps too much with existing agents.",
                "Not sure what {name} offers that other {cat} agents don't. Needs a clearer value prop.",
            ],
        },
    },
    "comparison": {
        "weight": 2,
        "templates": {
            "high": [
                "Compared to other {cat} agents, {name} stands out. Good tagging, solid implementation, clear purpose.",
                "Top-tier for the {cat} category. {lines} lines puts it on the thorough side without being bloated.",
                "{name} vs. the alternatives — this one wins on {advantage}.",
            ],
            "mid": [
                "{name} holds its own against other {cat} agents. {lines} lines, middle of the pack on complexity.",
                "Mid-range {cat} agent. Does what you'd expect. Nothing surprising, nothing missing.",
            ],
            "low": [
                "There are stronger options in {cat} right now. {name} needs more development to compete.",
            ],
        },
    },
}

REVIEWER_NAMES = [
    "Virtual Curator", "The Architect", "Agent Auditor", "Registry Reviewer",
    "CardSmith Review Desk", "Community Sentinel", "Quality Gate",
    "The Assessor", "Pattern Scanner", "Code Lens",
    "Deck Builder Review", "Single File Critic", "Tier Watch",
]

DIFFERENTIATORS = [
    "simplicity", "completeness", "zero-config setup", "clean error handling",
    "focused scope", "rich tagging", "documentation quality", "parameter design",
]

ADVANTAGES = [
    "ease of setup", "code clarity", "zero dependencies", "documentation",
    "parameter handling", "error messages", "single-file purity", "tagging",
]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONTEXT POOLS — reusable fragments for template filling
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUTHORS = [
    "AgentSmith", "RAPPBuilder", "CodeForge", "SingleFileDevotee",
    "ManifestMaster", "PyAgent", "RegistryRunner", "HoloDeckEng",
    "FederationFan", "WorkbenchWizard", "PipelinePro", "IntegrationDev",
    "BasicAgentFan", "CommunityContrib", "StoreBrowser", "CardCollector",
    "ASTWalker", "PerformReturner", "EnvVarChecker", "DocstringWriter",
    "KebabCaser", "NamespaceNinja", "TierClimber", "VersionBumper",
]

RELATED_TOPICS = [
    "Single-File Agent Anatomy", "Building & Validating the Registry",
    "Quality Tiers & Promotion", "Namespaces & Publishing",
    "Agent Development Best Practices", "The Holo Card System",
    "Using the Agent Workbench", "GitHub Issues as API",
    "Federation: Running Your Own Store",
]

SHORT_ANSWERS = [
    "keep your manifest fields accurate and run the validator",
    "inherit from BasicAgent and implement perform()",
    "use os.environ.get() and declare in requires_env",
    "run pytest locally before opening a PR",
    "check the CONSTITUTION for the canonical rules",
    "the AST parser reads your manifest without executing code",
    "categories determine where your agent appears in the store",
]

EXPERIENCE_INSIGHTS = [
    "the learning curve is front-loaded — once you get the manifest right, everything clicks",
    "reading other people's agents teaches you more than any documentation",
    "the single-file constraint felt limiting at first but now I can't imagine going back",
    "federation is underused but incredibly powerful for enterprise teams",
    "the card system makes agent publishing feel rewarding",
]

APPROACHES = [
    "starting from the CONTRIBUTING.md template and modifying from there",
    "running build_registry.py after every change to catch issues early",
    "looking at existing agents in the same category for patterns",
    "keeping my agent under 100 lines by focusing on one thing",
    "writing the manifest first, then the code — it forces you to think about the interface",
]

FIX_ACTIONS = [
    "make sure the __manifest__ dict is at module level, not inside a class",
    "use kebab-case for the file name and @publisher/slug for the manifest name",
    "ensure display_name in the manifest matches self.name in the class",
    "check that perform() explicitly returns a string, not None",
    "verify the category is one of: core, pipeline, integrations, productivity, devtools",
]

EXPLANATIONS = [
    "the registry builder uses AST parsing, not imports — so your code structure matters more than runtime behavior",
    "BasicAgent is the only hard dependency — everything else is optional",
    "the single-file principle means documentation, metadata, and code all live together",
    "quality tiers are about trust — community means 'it works', verified means 'we checked'",
    "federation lets each instance be autonomous while optionally participating in the larger ecosystem",
]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Engine Core
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def load_json(p: Path) -> dict:
    if not p.exists():
        return {}
    with open(p) as f:
        return json.load(f)


def save_json(p: Path, d: dict):
    with open(p, "w") as f:
        json.dump(d, f, indent=2)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def pick_weighted(rules: dict) -> tuple[str, dict]:
    names = list(rules.keys())
    weights = [rules[n]["weight"] for n in names]
    chosen = random.choices(names, weights=weights, k=1)[0]
    return chosen, rules[chosen]


def fill_template(template: str, ctx: dict) -> str:
    try:
        return template.format(**ctx)
    except (KeyError, IndexError):
        return template


def load_registry() -> list[dict]:
    """Load the RAR registry for real agent data."""
    reg_path = RAR_DIR / "registry.json"
    if not reg_path.exists():
        return []
    reg = load_json(reg_path)
    return reg.get("agents", [])


def init_state() -> dict:
    """Initialize or load Rappterpedia state."""
    if STATE_FILE.exists():
        return load_json(STATE_FILE)
    return {
        "tick_count": 0,
        "articles": [],
        "threads": [],
        "next_article_id": 1,
        "next_thread_id": 1,
        "next_reply_id": 1,
        "generated_topics": [],
        "generated_agent_ids": [],
    }


def get_agent_context(agent: dict) -> dict:
    """Build template context from a registry agent entry."""
    name = agent.get("name", "@unknown/unknown")
    publisher = name.split("/")[0].lstrip("@") if "/" in name else "unknown"
    env_list = agent.get("requires_env", [])
    env_section = (
        f"requires these environment variables: `{'`, `'.join(env_list)}`"
        if env_list
        else "requires no environment variables"
    )
    deps = ", ".join(agent.get("dependencies", ["@rapp/basic-agent"])) or "@rapp/basic-agent"
    tags = agent.get("tags", [])

    return {
        "name": agent.get("display_name", name),
        "agent_name": name,
        "agent_display": agent.get("display_name", name),
        "description": agent.get("description", "An agent in the RAR registry."),
        "description_lower": agent.get("description", "").lower().rstrip("."),
        "short_desc": agent.get("description", "")[:60],
        "publisher": f"@{publisher}",
        "publisher_slug": publisher,
        "category": agent.get("category", "community"),
        "cat": agent.get("category", "community").replace("_", " "),
        "quality_tier": agent.get("quality_tier", "community"),
        "tier": agent.get("quality_tier", "community"),
        "version": agent.get("version", "1.0.0"),
        "agent_path": agent.get("_file", f"@{publisher}/{name.split('/')[-1]}.py"),
        "size_kb": agent.get("_size_kb", "?"),
        "lines": agent.get("_lines", "?"),
        "env_section": env_section,
        "deps": deps,
        "tag_list": ", ".join(tags) if tags else "none",
        "tags": tags,
    }


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Article Generation
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def generate_article(state: dict, agents: list[dict], echoes: dict | None = None) -> dict | None:
    """Generate a single wiki article from rules, informed by echoes from previous frames."""
    echoes = echoes or {}

    # Echo-driven rule selection: prefer rules that fill gaps
    weighted_rules = dict(ARTICLE_RULES)
    underserved = echoes.get("underserved_categories", [])
    if underserved:
        # Boost weight of rules whose category is underserved
        for rname, rule in weighted_rules.items():
            if rule.get("category") in underserved:
                weighted_rules[rname] = dict(rule, weight=rule["weight"] * 3)

    rule_name, rule = pick_weighted(weighted_rules)

    # Build context based on rule type
    ctx = {"tick": state["tick_count"]}

    if rule_name == "agent_deep_dive" and agents:
        # Pick an agent we haven't covered yet
        uncovered = [a for a in agents if a.get("name") not in state["generated_agent_ids"]]
        if not uncovered:
            uncovered = agents
        agent = random.choice(uncovered)
        ctx.update(get_agent_context(agent))
        state["generated_agent_ids"].append(agent.get("name", ""))
    elif "topic_pool" in rule:
        unused = [t for t in rule["topic_pool"] if t not in state["generated_topics"]]
        if not unused:
            unused = rule["topic_pool"]
        if isinstance(unused[0], tuple):
            # Idea-style tuples
            topic = random.choice(unused)
            topic_str = topic[0] if isinstance(topic, tuple) else topic
        else:
            topic_str = random.choice(unused)
        state["generated_topics"].append(topic_str)

        # Map topic to various context keys used by templates
        ctx.update({
            "topic": topic_str, "topic_lower": topic_str.lower(),
            "arch_topic": topic_str, "arch_topic_lower": topic_str.lower(),
            "practice": topic_str, "practice_lower": topic_str.lower(),
            "problem": topic_str, "problem_lower": topic_str.lower(),
            "fed_topic": topic_str, "fed_topic_lower": topic_str.lower(),
            "platform": topic_str, "platform_upper": topic_str.upper().replace(" ", "_"),
            "symptom_context": "building or testing agents",
            "symptom_detail": "an error or unexpected behavior during the build or test process",
            "root_cause": "a mismatch between what the AST parser expects and what's in your file",
            "step": "Follow the standard agent creation process",
            "symptom": "The output doesn't match expectations",
        })
    elif "platform_pool" in rule:
        platforms = [p for p in rule["platform_pool"] if p not in state["generated_topics"]]
        if not platforms:
            platforms = rule["platform_pool"]
        platform = random.choice(platforms)
        state["generated_topics"].append(platform)
        ctx.update({
            "platform": platform,
            "platform_upper": platform.upper().replace(" ", "_"),
        })

    # For publisher spotlights, use real data
    if rule_name == "community_spotlight" and agents:
        publishers = {}
        for a in agents:
            name = a.get("name", "")
            pub = name.split("/")[0].lstrip("@") if "/" in name else "unknown"
            publishers.setdefault(pub, []).append(a)
        pub_name = random.choice(list(publishers.keys()))
        pub_agents = publishers[pub_name]
        categories = set(a.get("category", "") for a in pub_agents)
        ctx.update({
            "publisher": pub_name,
            "publisher_slug": pub_name,
            "agent_count": len(pub_agents),
            "focus_area": ", ".join(categories),
            "category_spread": f"{len(categories)} categories",
        })

    # Generate title
    title = fill_template(random.choice(rule["titles"]), ctx)

    # Generate content from sections
    content_parts = []
    for section in rule["sections"]:
        heading = section["heading"]
        body = fill_template(random.choice(section["templates"]), ctx)
        content_parts.append(f"## {heading}\n\n{body}")
    content = "\n\n".join(content_parts)

    # Pick tags
    base_tags = rule.get("tags", [])
    extra_tags = ctx.get("tags", [])[:2] if "tags" in ctx else []
    tags = list(set(base_tags + extra_tags))

    article_id = f"gen-art-{state['next_article_id']:04d}"
    state["next_article_id"] += 1

    return {
        "id": article_id,
        "title": title,
        "category": rule["category"],
        "tags": tags,
        "content": content,
        "author": random.choice(AUTHORS),
        "created": now_iso(),
        "updated": now_iso(),
        "generated_by": rule_name,
    }


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Thread Generation
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def generate_thread(state: dict, agents: list[dict], echoes: dict | None = None) -> dict | None:
    """Generate a single forum thread from rules, informed by echoes."""
    echoes = echoes or {}

    # Echo-driven: boost showcase if no showcases exist, boost help if few threads
    weighted_rules = dict(THREAD_RULES)
    gaps = echoes.get("gaps", [])
    if "no agent showcases in the forum yet" in gaps:
        if "showcase" in weighted_rules:
            weighted_rules["showcase"] = dict(weighted_rules["showcase"], weight=weighted_rules["showcase"]["weight"] * 3)

    rule_name, rule = pick_weighted(weighted_rules)

    ctx = {"tick": state["tick_count"]}

    # Fill context based on rule type
    if rule_name == "showcase" and agents:
        agent = random.choice(agents)
        ctx.update(get_agent_context(agent))
    elif rule_name == "help_question":
        action = random.choice(rule["action_pool"])
        ctx.update({"action": action, "action_lower": action.lower()})
    elif rule_name == "idea":
        idea_tuple = random.choice(rule["idea_pool"])
        ctx.update({
            "idea": idea_tuple[0], "idea_lower": idea_tuple[0].lower(),
            "rationale": idea_tuple[1], "benefit": idea_tuple[2],
        })
    elif rule_name == "bug_report":
        bug_tuple = random.choice(rule["bug_pool"])
        ctx.update({
            "bug": bug_tuple[0], "context": bug_tuple[1],
            "step": bug_tuple[2], "symptom": bug_tuple[3],
        })
    elif "topic_pool" in rule:
        topic = random.choice(rule["topic_pool"])
        ctx.update({
            "topic": topic, "topic_lower": topic.lower(),
            "meta_topic": topic, "meta_topic_lower": topic.lower(),
        })

    title = fill_template(random.choice(rule["titles"]), ctx)
    body = fill_template(random.choice(rule["bodies"]), ctx)

    # Generate 1-4 replies
    num_replies = random.randint(1, 4)
    replies = []
    for _ in range(num_replies):
        reply_name, reply_rule = pick_weighted(REPLY_RULES)
        reply_ctx = {
            "related_topic": random.choice(RELATED_TOPICS),
            "short_answer": random.choice(SHORT_ANSWERS),
            "experience_insight": random.choice(EXPERIENCE_INSIGHTS),
            "approach": random.choice(APPROACHES),
            "fix_action": random.choice(FIX_ACTIONS),
            "explanation": random.choice(EXPLANATIONS),
        }
        reply_text = fill_template(random.choice(reply_rule["templates"]), reply_ctx)

        reply_id = f"gen-r-{state['next_reply_id']:04d}"
        state["next_reply_id"] += 1

        replies.append({
            "id": reply_id,
            "author": random.choice(AUTHORS),
            "content": reply_text,
            "created": now_iso(),
        })

    thread_id = f"gen-thr-{state['next_thread_id']:04d}"
    state["next_thread_id"] += 1

    return {
        "id": thread_id,
        "title": title,
        "channel": rule["channel"],
        "content": body,
        "author": random.choice(AUTHORS),
        "created": now_iso(),
        "updated": now_iso(),
        "votes": random.randint(1, 15),
        "pinned": False,
        "replies": replies,
        "generated_by": rule_name,
    }


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Review Generation
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def score_agent(agent: dict) -> tuple[int, str]:
    """Score an agent 1-5 stars based on real metadata. Returns (stars, tier_label)."""
    score = 0
    lines = agent.get("_lines", 0)
    if lines > 200: score += 2
    elif lines > 50: score += 1

    ver = agent.get("version", "1.0.0")
    if int(ver.split(".")[0]) >= 2: score += 1

    tier = agent.get("quality_tier", "community")
    if tier == "official": score += 3
    elif tier == "verified": score += 2
    elif tier == "community": score += 1

    if len(agent.get("tags", [])) >= 4: score += 1
    if len(agent.get("description", "")) > 100: score += 1
    if len(agent.get("dependencies", [])) == 0: score += 1
    if len(agent.get("requires_env", [])) == 0: score += 1

    stars = max(1, min(5, round(score * 5 / 10)))
    level = "high" if stars >= 4 else "mid" if stars >= 3 else "low"
    return stars, level


def generate_reviews(state: dict, agents: list[dict], num_reviews: int = 5) -> list[str]:
    """Generate curator reviews for agents. Accumulates in state across ticks."""
    if not agents:
        return []

    results = []
    reviews = state.setdefault("reviews", {})  # {agent_name: [review, ...]}
    ts = now_iso()

    # Pick agents to review this tick — prefer under-reviewed agents
    review_counts = {name: len(revs) for name, revs in reviews.items()}
    candidates = []
    for agent in agents:
        name = agent.get("name", "")
        count = review_counts.get(name, 0)
        if count < 6:  # Cap at 6 reviews per agent
            candidates.append((agent, count))

    if not candidates:
        return results

    # Weight toward under-reviewed agents
    candidates.sort(key=lambda x: x[1])
    to_review = []
    for _ in range(min(num_reviews, len(candidates))):
        # Weighted selection — fewer reviews = higher chance
        weights = [max(1, 6 - c[1]) for c in candidates]
        chosen = random.choices(candidates, weights=weights, k=1)[0]
        to_review.append(chosen[0])
        candidates.remove(chosen)
        if not candidates:
            break

    for agent in to_review:
        name = agent.get("name", "")
        stars, level = score_agent(agent)
        ctx = get_agent_context(agent)
        ctx.update({
            "diff": random.choice(DIFFERENTIATORS),
            "advantage": random.choice(ADVANTAGES),
        })

        # Pick a review angle we haven't used for this agent yet
        existing_angles = [r.get("angle", "") for r in reviews.get(name, [])]
        available_angles = {k: v for k, v in REVIEW_ANGLES.items() if k not in existing_angles}
        if not available_angles:
            available_angles = REVIEW_ANGLES

        angle_name, angle = pick_weighted(available_angles)
        templates = angle["templates"].get(level, angle["templates"].get("mid", []))
        if not templates:
            continue

        text = fill_template(random.choice(templates), ctx)

        # Vary rating ±1 from base
        rating = max(1, min(5, stars + random.choice([-1, 0, 0, 1])))

        reviewer = random.choice(REVIEWER_NAMES)

        review = {
            "user": reviewer,
            "rating": rating,
            "text": text,
            "angle": angle_name,
            "timestamp": ts,
        }

        reviews.setdefault(name, []).append(review)
        results.append(f"⭐ Review: {reviewer} gave {name} {rating}★ [{angle_name}]")

    return results


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Tick & Commit
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def build_echoes(state: dict) -> dict:
    """
    Build echo context from previous frames.
    Echoes are the memory of what happened before — they inform what
    should happen next. This is the Rappterbook pattern: each frame
    reads the last frame's output to drive intelligent decisions.
    """
    echoes = {
        "tick": state.get("tick_count", 0),
        "total_articles": len(state.get("articles", [])),
        "total_threads": len(state.get("threads", [])),
        "total_reviews": sum(len(v) for v in state.get("reviews", {}).values()),
        "reviewed_agents": set(state.get("reviews", {}).keys()),
        "covered_topics": set(state.get("generated_topics", [])),
        "covered_agents": set(state.get("generated_agent_ids", [])),
        "recent_articles": [],
        "recent_threads": [],
        "underserved_categories": [],
        "hot_threads": [],
        "gaps": [],
    }

    # Find recent content (last 5 of each)
    articles = state.get("articles", [])
    threads = state.get("threads", [])
    if articles:
        echoes["recent_articles"] = [a["title"] for a in articles[-5:]]
    if threads:
        echoes["recent_threads"] = [t["title"] for t in threads[-5:]]

    # Find underserved wiki categories
    cat_counts = {}
    for a in articles:
        cat_counts[a.get("category", "?")] = cat_counts.get(a.get("category", "?"), 0) + 1
    all_cats = ["getting-started", "agents", "architecture", "integrations",
                "best-practices", "troubleshooting", "federation", "community"]
    for cat in all_cats:
        if cat_counts.get(cat, 0) < 3:
            echoes["underserved_categories"].append(cat)

    # Find hot threads (most replies)
    sorted_threads = sorted(threads, key=lambda t: len(t.get("replies", [])), reverse=True)
    echoes["hot_threads"] = [t["title"] for t in sorted_threads[:3]]

    # Identify content gaps
    if echoes["total_articles"] < 10:
        echoes["gaps"].append("needs more wiki foundation articles")
    if echoes["total_reviews"] < 50:
        echoes["gaps"].append("needs more agent reviews for credibility")
    if not any(a.get("category") == "troubleshooting" for a in articles):
        echoes["gaps"].append("no troubleshooting articles yet")
    if not any(t.get("channel") == "showcase" for t in threads):
        echoes["gaps"].append("no agent showcases in the forum yet")

    return echoes


def rappterpedia_tick(num_articles: int = 2, num_threads: int = 2, dry_run: bool = False) -> list[str]:
    """Run a single content generation tick."""
    state = init_state()
    agents = load_registry()
    results = []

    state["tick_count"] += 1
    ts = now_iso()

    # ── Build echoes from previous frames ──────────────
    echoes = build_echoes(state)

    # ── Phase 1: Generate wiki articles ─────────────────
    # Prefer underserved categories based on echoes
    for _ in range(num_articles):
        article = generate_article(state, agents, echoes=echoes)
        if article:
            state["articles"].append(article)
            results.append(f"📝 Wiki: \"{article['title']}\" [{article['category']}] by {article['author']}")

    # ── Phase 2: Generate forum threads ─────────────────
    for _ in range(num_threads):
        thread = generate_thread(state, agents, echoes=echoes)
        if thread:
            reply_count = len(thread.get("replies", []))
            state["threads"].append(thread)
            results.append(f"💬 Forum: \"{thread['title']}\" [{thread['channel']}] +{reply_count} replies")

    # ── Phase 3: Add replies to existing threads ────────
    if state["threads"] and len(state["threads"]) > num_threads:
        existing = state["threads"][:-num_threads] if num_threads > 0 else state["threads"]
        num_extra_replies = random.randint(2, 5)
        for _ in range(num_extra_replies):
            thread = random.choice(existing)
            reply_name, reply_rule = pick_weighted(REPLY_RULES)
            reply_ctx = {
                "related_topic": random.choice(RELATED_TOPICS),
                "short_answer": random.choice(SHORT_ANSWERS),
                "experience_insight": random.choice(EXPERIENCE_INSIGHTS),
                "approach": random.choice(APPROACHES),
                "fix_action": random.choice(FIX_ACTIONS),
                "explanation": random.choice(EXPLANATIONS),
            }
            reply_text = fill_template(random.choice(reply_rule["templates"]), reply_ctx)
            reply_id = f"gen-r-{state['next_reply_id']:04d}"
            state["next_reply_id"] += 1

            thread.setdefault("replies", []).append({
                "id": reply_id,
                "author": random.choice(AUTHORS),
                "content": reply_text,
                "created": ts,
            })
            thread["updated"] = ts
            results.append(f"  ↳ Reply on \"{thread['title'][:40]}...\" by {thread['replies'][-1]['author']}")

    # ── Phase 4: Generate curator reviews ────────────────
    review_results = generate_reviews(state, agents, num_reviews=random.randint(3, 8))
    results.extend(review_results)

    # ── Save state ──────────────────────────────────────
    if not dry_run:
        save_json(STATE_FILE, state)

    # ── Export reviews for store consumption ────────────
    if not dry_run:
        reviews_export = {"agents": state.get("reviews", {})}
        save_json(RAR_DIR / "state" / "curator_reviews.json", reviews_export)

    # ── Export for web consumption ──────────────────────
    if not dry_run:
        export = {
            "version": "1.0",
            "generated": ts,
            "tick": state["tick_count"],
            "articles": state["articles"],
            "threads": state["threads"],
            "stats": {
                "total_articles": len(state["articles"]),
                "total_threads": len(state["threads"]),
                "total_replies": sum(len(t.get("replies", [])) for t in state["threads"]),
            },
        }
        save_json(BASE_DIR / "rappterpedia_export.json", export)

    return results


def git_commit_and_push(results: list[str], no_push: bool = False):
    """Commit state changes and optionally push."""
    msg = f"Rappterpedia heartbeat: +{len(results)} content items\n\n" + "\n".join(results)
    subprocess.run(["git", "add", "rappterpedia/"], cwd=str(RAR_DIR))
    subprocess.run(["git", "commit", "-m", msg], cwd=str(RAR_DIR))
    if not no_push:
        subprocess.run(["git", "push"], cwd=str(RAR_DIR))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CLI
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    no_push = "--no-push" in args or dry_run
    seed_only = "--seed" in args

    # Burst mode: generate many items at once
    burst = 1
    for i, arg in enumerate(args):
        if arg == "--burst" and i + 1 < len(args):
            burst = int(args[i + 1])

    if seed_only:
        burst = 10  # Generate a solid foundation

    print(f"{'=' * 60}")
    print(f"  Rappterpedia Content Engine")
    print(f"  {'DRY RUN' if dry_run else 'LIVE'} | burst={burst}")
    print(f"{'=' * 60}")

    all_results = []
    for tick in range(burst):
        num_articles = random.randint(1, 3)
        num_threads = random.randint(1, 3)
        results = rappterpedia_tick(
            num_articles=num_articles,
            num_threads=num_threads,
            dry_run=dry_run,
        )
        all_results.extend(results)
        for r in results:
            print(f"  {r}")

    print(f"\n{'=' * 60}")
    print(f"  Generated: {len(all_results)} content items across {burst} ticks")
    print(f"{'=' * 60}")

    if not dry_run and not no_push:
        print("\n  Committing...")
        git_commit_and_push(all_results, no_push=no_push)
        print("  Done!")
    elif not dry_run and no_push:
        print("\n  State saved (--no-push: skipping git)")


if __name__ == "__main__":
    main()
