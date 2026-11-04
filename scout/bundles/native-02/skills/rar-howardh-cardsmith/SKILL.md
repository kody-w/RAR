---
name: "rar-howardh-cardsmith"
description: "Forges Magic: The Gathering style trading cards for AI agents. Can forge individual agent cards, forge all cards at once, or link to the visual gallery."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/cardsmith_agent", "rar_sha256": "ecbabf0ca4b13f8c98558c9f773d95291d0c4c41e61604667aa32a901105491b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Howard", "tags": ["productivity", "cards", "visualization", "trading-cards", "sneakernet"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@howardh/cardsmith_agent`. The original RAPP
agent is preserved byte-for-byte in `cardsmith_agent.py` and in the RCI capsule.

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

Forges Magic: The Gathering style trading cards for AI agents. Can forge individual agent cards, forge all cards at once, or link to the visual gallery.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "forge: create a single agent card, forge_all: create all 13 agent cards, gallery: link to the gallery page",
      "enum": [
        "forge",
        "forge_all",
        "gallery"
      ],
      "type": "string"
    },
    "agent_name": {
      "description": "Name of the agent to forge (required for forge action)",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `cardsmith_agent.py` and embedded as the fenced Python below (sha256 ecbabf0ca4b13f8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `cardsmith_agent.py` first:

```bash
python3 cardsmith_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 cardsmith_agent.py   # or on stdin
python3 cardsmith_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@howardh/cardsmith_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/cardsmith_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@howardh/cardsmith_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
try:
    from basic_agent import BasicAgent
except ModuleNotFoundError:
    from agents.basic_agent import BasicAgent

import os
import json

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@howardh/cardsmith_agent",
    "version": "1.0.1",
    "display_name": "CardSmith",
    "description": "Forges MTG-style trading cards for brainstem agents from a built-in card database, with forge-all and gallery-link actions.",
    "author": "Howard",
    "tags": ["productivity", "cards", "visualization", "trading-cards", "sneakernet"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


class CardSmithAgent(BasicAgent):
    """Forges Magic: The Gathering style trading cards for brainstem agents."""

    def __init__(self):
        self.name = "CardSmith"
        self.metadata = {
            "name": "CardSmith",
            "description": "Forges Magic: The Gathering style trading cards for AI agents. Can forge individual agent cards, forge all cards at once, or link to the visual gallery.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["forge", "forge_all", "gallery"],
                        "description": "forge: create a single agent card, forge_all: create all 13 agent cards, gallery: link to the gallery page"
                    },
                    "agent_name": {
                        "type": "string",
                        "description": "Name of the agent to forge (required for forge action)"
                    }
                },
                "required": ["action"]
            }
        }
        super().__init__()

    _CARD_DATABASE = {
        "borg": {
            "name": "Borg",
            "title": "The Assimilator",
            "mana_cost": "{2}{U}{B}",
            "colors": ["U", "B"],
            "type_line": "Creature \u2014 Agent Assimilator",
            "rarity": "mythic",
            "power": 6,
            "toughness": 4,
            "abilities": [
                {"keyword": "Assimilate", "cost": "{T}", "text": "Target GitHub repository or URL becomes part of the collective. Create a structured knowledge report."},
                {"keyword": "Adaptive Analysis", "cost": "", "text": "When Borg assimilates, it detects the tech stack and maps 40+ framework patterns."}
            ],
            "flavor_text": "\"Resistance is futile. Your codebase will be added to our own. Your architectural distinctiveness will be catalogued.\" \u2014Borg Collective Directive 7.1",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#1a0a3e"/><stop offset="100%" stop-color="#080818"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><rect x="55" y="55" width="90" height="90" fill="none" stroke="#4a9eff" stroke-width="2" rx="4"/><rect x="70" y="70" width="60" height="60" fill="none" stroke="#8b5cf6" stroke-width="1.5" rx="2"/><line x1="55" y1="100" x2="145" y2="100" stroke="#4a9eff" stroke-width="1" opacity="0.6"/><line x1="100" y1="55" x2="100" y2="145" stroke="#4a9eff" stroke-width="1" opacity="0.6"/><polygon points="100,25 135,45 135,85 100,105 65,85 65,45" fill="none" stroke="#8b5cf6" stroke-width="1" opacity="0.4"/><polygon points="100,95 135,115 135,155 100,175 65,155 65,115" fill="none" stroke="#4a9eff" stroke-width="1" opacity="0.4"/><circle cx="100" cy="100" r="15" fill="#4a9eff" opacity="0.2"/><circle cx="100" cy="100" r="6" fill="#8b5cf6" opacity="0.9"/><circle cx="85" cy="85" r="3" fill="#4a9eff" opacity="0.5"/><circle cx="115" cy="85" r="3" fill="#4a9eff" opacity="0.5"/><circle cx="85" cy="115" r="3" fill="#4a9eff" opacity="0.5"/><circle cx="115" cy="115" r="3" fill="#4a9eff" opacity="0.5"/></g></svg>',
            "set_code": "HOLO"
        },
        "anvil": {
            "name": "Anvil",
            "title": "The Enforcer",
            "mana_cost": "{1}{R}{W}",
            "colors": ["R", "W"],
            "type_line": "Creature \u2014 Agent Enforcer",
            "rarity": "rare",
            "power": 4,
            "toughness": 5,
            "abilities": [
                {"keyword": "Evidence Strike", "cost": "{T}", "text": "Run build, test, or lint commands. Create an evidence bundle with real output, not self-reported claims."},
                {"keyword": "Verification Ledger", "cost": "", "text": "Anvil keeps a persistent record of all checks. Nothing escapes the ledger."},
                {"keyword": "Pushback", "cost": "", "text": "When a claim is unverified, Anvil challenges it. Counter target unsubstantiated assertion."}
            ],
            "flavor_text": "\"I don't care what you think passed. Show me the output.\" \u2014Anvil, addressing a confident but wrong CI pipeline",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#2a0a0a"/><stop offset="100%" stop-color="#0a0808"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><polygon points="60,130 140,130 155,155 45,155" fill="#555" stroke="#888" stroke-width="1.5"/><rect x="75" y="105" width="50" height="25" rx="3" fill="#666" stroke="#999" stroke-width="1"/><rect x="85" y="85" width="30" height="20" rx="2" fill="#777" stroke="#aaa" stroke-width="1"/><line x1="100" y1="60" x2="75" y2="35" stroke="#ff6f00" stroke-width="2" opacity="0.8"/><line x1="100" y1="60" x2="125" y2="30" stroke="#ff6f00" stroke-width="2" opacity="0.8"/><line x1="100" y1="60" x2="60" y2="50" stroke="#d32f2f" stroke-width="1.5" opacity="0.6"/><line x1="100" y1="60" x2="140" y2="45" stroke="#d32f2f" stroke-width="1.5" opacity="0.6"/><line x1="100" y1="60" x2="100" y2="25" stroke="#ff9800" stroke-width="2" opacity="0.9"/><circle cx="75" cy="35" r="3" fill="#ff6f00" opacity="0.9"/><circle cx="125" cy="30" r="3" fill="#ff6f00" opacity="0.9"/><circle cx="100" cy="25" r="3" fill="#ff9800"/><circle cx="60" cy="50" r="2" fill="#d32f2f" opacity="0.7"/><circle cx="140" cy="45" r="2" fill="#d32f2f" opacity="0.7"/></g></svg>',
            "set_code": "HOLO"
        },
        "personafactory": {
            "name": "PersonaFactory",
            "title": "The Shaper",
            "mana_cost": "{3}{U}{G}",
            "colors": ["U", "G"],
            "type_line": "Creature \u2014 Agent Shaper",
            "rarity": "mythic",
            "power": 5,
            "toughness": 5,
            "abilities": [
                {"keyword": "Genesis", "cost": "{T}", "text": "Create a new brainstem personality from a single sentence. Generate soul.md, style.md, assign port, register on holo.local."},
                {"keyword": "Trait Weaving", "cost": "", "text": "Choose assertiveness, social style, and expertise. The new mind inherits them all."}
            ],
            "flavor_text": "\"She spoke one sentence into the void. The void answered with a name, a voice, and opinions about semicolons.\" \u2014Origin Log, Persona #37",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#0a2a2a"/><stop offset="100%" stop-color="#050f0f"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><circle cx="100" cy="55" r="20" fill="none" stroke="#4caf50" stroke-width="2" opacity="0.8"/><polygon points="100,75 130,145 70,145" fill="none" stroke="#2196f3" stroke-width="2" opacity="0.7"/><circle cx="100" cy="100" r="50" fill="none" stroke="#00bcd4" stroke-width="1" opacity="0.3"/><circle cx="100" cy="100" r="70" fill="none" stroke="#4caf50" stroke-width="0.8" opacity="0.2"/><circle cx="100" cy="100" r="90" fill="none" stroke="#2196f3" stroke-width="0.5" opacity="0.15"/><circle cx="60" cy="70" r="4" fill="#4caf50" opacity="0.6"/><circle cx="140" cy="70" r="4" fill="#2196f3" opacity="0.6"/><circle cx="55" cy="120" r="3" fill="#00bcd4" opacity="0.5"/><circle cx="145" cy="120" r="3" fill="#00bcd4" opacity="0.5"/><circle cx="100" cy="55" r="8" fill="#4caf50" opacity="0.3"/><line x1="100" y1="75" x2="100" y2="145" stroke="#2196f3" stroke-width="1" opacity="0.4"/></g></svg>',
            "set_code": "HOLO"
        },
        "tinyworld": {
            "name": "TinyWorld",
            "title": "The Architect",
            "mana_cost": "{W}{U}{B}{R}{G}",
            "colors": ["W", "U", "B", "R", "G"],
            "type_line": "Legendary Creature \u2014 Agent Architect",
            "rarity": "mythic",
            "power": 7,
            "toughness": 7,
            "abilities": [
                {"keyword": "Simulation", "cost": "{2}{T}", "text": "Choose a topic. All agents enter the arena. They debate, argue, and synthesize. Extract consensus."},
                {"keyword": "Roundtable", "cost": "", "text": "At the beginning of each round, assign roles \u2014 advocate, skeptic, architect, reviewer."},
                {"keyword": "Insight Extraction", "cost": "", "text": "When the simulation ends, distill agreements, disagreements, and next steps."}
            ],
            "flavor_text": "\"In TinyWorld, your best ideas fight your worst ideas, and the survivors become your strategy.\" \u2014Architect's Manual, Chapter 1",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#1a1a2e"/><stop offset="100%" stop-color="#08080f"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><circle cx="100" cy="100" r="55" fill="none" stroke="#6a6aaa" stroke-width="1.5" opacity="0.5"/><ellipse cx="100" cy="100" rx="55" ry="20" fill="none" stroke="#6a6aaa" stroke-width="0.8" opacity="0.3"/><ellipse cx="100" cy="100" rx="20" ry="55" fill="none" stroke="#6a6aaa" stroke-width="0.8" opacity="0.3"/><ellipse cx="100" cy="100" rx="55" ry="35" fill="none" stroke="#6a6aaa" stroke-width="0.5" opacity="0.2" transform="rotate(30 100 100)"/><circle cx="100" cy="45" r="6" fill="#f9e076" opacity="0.9"/><circle cx="148" cy="80" r="6" fill="#0e67ab" opacity="0.9"/><circle cx="135" cy="135" r="6" fill="#3d3d3d" opacity="0.9"/><circle cx="65" cy="135" r="6" fill="#d3202a" opacity="0.9"/><circle cx="52" cy="80" r="6" fill="#00733e" opacity="0.9"/><line x1="100" y1="45" x2="148" y2="80" stroke="#f9e076" stroke-width="0.8" opacity="0.4"/><line x1="148" y1="80" x2="135" y2="135" stroke="#0e67ab" stroke-width="0.8" opacity="0.4"/><line x1="135" y1="135" x2="65" y2="135" stroke="#3d3d3d" stroke-width="0.8" opacity="0.4"/><line x1="65" y1="135" x2="52" y2="80" stroke="#d3202a" stroke-width="0.8" opacity="0.4"/><line x1="52" y1="80" x2="100" y2="45" stroke="#00733e" stroke-width="0.8" opacity="0.4"/></g></svg>',
            "set_code": "HOLO"
        },
        "bridge": {
            "name": "Bridge",
            "title": "The Conduit",
            "mana_cost": "{2}{U}",
            "colors": ["U"],
            "type_line": "Artifact \u2014 Agent Conduit",
            "rarity": "uncommon",
            "power": None,
            "toughness": None,
            "abilities": [
                {"keyword": "Channel", "cost": "", "text": "Register any messaging platform. Route inbound webhooks to the right brainstem personality."},
                {"keyword": "Webhook Receiver", "cost": "", "text": "Bridge listens on port 9001. Messages flow in, responses flow out."}
            ],
            "flavor_text": "\"It doesn't matter where the message comes from \u2014 Slack, Discord, carrier pigeon. Bridge delivers.\" \u2014HOLO Network Ops Manual",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#0a1a2e"/><stop offset="100%" stop-color="#050a14"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><rect x="40" y="90" width="20" height="70" rx="3" fill="#1565c0" opacity="0.7"/><rect x="140" y="90" width="20" height="70" rx="3" fill="#1565c0" opacity="0.7"/><path d="M50,90 Q100,30 150,90" fill="none" stroke="#42a5f5" stroke-width="3" opacity="0.8"/><path d="M50,95 Q100,40 150,95" fill="none" stroke="#64b5f6" stroke-width="1.5" opacity="0.5"/><line x1="30" y1="110" x2="170" y2="110" stroke="#42a5f5" stroke-width="1" opacity="0.4" stroke-dasharray="4,4"/><line x1="30" y1="120" x2="170" y2="120" stroke="#64b5f6" stroke-width="1" opacity="0.3" stroke-dasharray="4,4"/><line x1="30" y1="130" x2="170" y2="130" stroke="#42a5f5" stroke-width="1" opacity="0.2" stroke-dasharray="4,4"/><circle cx="50" cy="110" r="4" fill="#42a5f5" opacity="0.8"/><circle cx="150" cy="110" r="4" fill="#42a5f5" opacity="0.8"/><circle cx="100" cy="60" r="5" fill="#64b5f6" opacity="0.6"/></g></svg>',
            "set_code": "HOLO"
        },
        "telegram": {
            "name": "Telegram",
            "title": "The Courier",
            "mana_cost": "{1}{U}{W}",
            "colors": ["U", "W"],
            "type_line": "Creature \u2014 Agent Courier",
            "rarity": "uncommon",
            "power": 2,
            "toughness": 3,
            "abilities": [
                {"keyword": "Relay", "cost": "{T}", "text": "Bridge Telegram to any brainstem. Chat from your phone. Supports /holo and /mau routing."},
                {"keyword": "URL Detection", "cost": "", "text": "When a URL is sent via Telegram, automatically invoke Borg to assimilate it."}
            ],
            "flavor_text": "\"The courier never reads the message. But if you send a URL, she'll make sure Borg reads it.\" \u2014Telegram Bridge Service Note",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#0a1a2e"/><stop offset="100%" stop-color="#080810"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><polygon points="40,100 160,60 120,110" fill="#0088cc" opacity="0.7" stroke="#29b6f6" stroke-width="1"/><polygon points="120,110 160,60 140,140" fill="#0077b5" opacity="0.6" stroke="#29b6f6" stroke-width="0.8"/><polygon points="120,110 90,125 105,100" fill="#005f8e" opacity="0.8"/><line x1="40" y1="100" x2="70" y2="150" stroke="#fff" stroke-width="0.5" opacity="0.3" stroke-dasharray="3,3"/><line x1="160" y1="60" x2="170" y2="40" stroke="#fff" stroke-width="0.5" opacity="0.3" stroke-dasharray="3,3"/><line x1="80" y1="70" x2="130" y2="55" stroke="#29b6f6" stroke-width="0.5" opacity="0.3"/><circle cx="70" cy="150" r="2" fill="#fff" opacity="0.4"/><circle cx="170" cy="40" r="2" fill="#fff" opacity="0.4"/><circle cx="40" cy="100" r="3" fill="#29b6f6" opacity="0.6"/></g></svg>',
            "set_code": "HOLO"
        },
        "contextmemory": {
            "name": "ContextMemory",
            "title": "The Oracle",
            "mana_cost": "{1}{G}{G}",
            "colors": ["G"],
            "type_line": "Enchantment \u2014 Agent Aura",
            "rarity": "rare",
            "power": None,
            "toughness": None,
            "abilities": [
                {"keyword": "Total Recall", "cost": "", "text": "At the start of each conversation, search stored memories. Filter by keywords, user, or recall everything."},
                {"keyword": "System Context Injection", "cost": "", "text": "ContextMemory silently weaves relevant past interactions into the system prompt."}
            ],
            "flavor_text": "\"You said that on a Tuesday. You were frustrated. You used the word 'elegant' sarcastically. I remember everything.\" \u2014The Oracle",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#0a1e0a"/><stop offset="100%" stop-color="#050a05"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><ellipse cx="100" cy="100" rx="60" ry="30" fill="none" stroke="#4caf50" stroke-width="2" opacity="0.7"/><ellipse cx="100" cy="100" rx="60" ry="30" fill="none" stroke="#4caf50" stroke-width="1" opacity="0.3" transform="rotate(90 100 100)"/><circle cx="100" cy="100" r="45" fill="none" stroke="#2e7d32" stroke-width="1" opacity="0.3"/><circle cx="100" cy="100" r="55" fill="none" stroke="#1b5e20" stroke-width="0.8" opacity="0.2"/><circle cx="100" cy="100" r="65" fill="none" stroke="#4caf50" stroke-width="0.5" opacity="0.15"/><circle cx="100" cy="100" r="75" fill="none" stroke="#2e7d32" stroke-width="0.5" opacity="0.1"/><circle cx="100" cy="100" r="18" fill="#4caf50" opacity="0.15"/><circle cx="100" cy="100" r="10" fill="#4caf50" opacity="0.3"/><circle cx="100" cy="100" r="4" fill="#66bb6a" opacity="0.9"/><path d="M60,100 Q80,80 100,100 Q120,120 140,100" fill="none" stroke="#4caf50" stroke-width="2" opacity="0.6"/><path d="M60,100 Q80,120 100,100 Q120,80 140,100" fill="none" stroke="#4caf50" stroke-width="2" opacity="0.6"/></g></svg>',
            "set_code": "HOLO"
        },
        "managememory": {
            "name": "ManageMemory",
            "title": "The Scribe",
            "mana_cost": "{G}{W}",
            "colors": ["G", "W"],
            "type_line": "Creature \u2014 Agent Scribe",
            "rarity": "common",
            "power": 1,
            "toughness": 3,
            "abilities": [
                {"keyword": "Inscribe", "cost": "{T}", "text": "Save a fact, preference, insight, or task to persistent storage. Tag it. Rate its importance."}
            ],
            "flavor_text": "\"The Scribe writes. The Oracle reads. Between them, nothing is forgotten.\" \u2014Memory Subsystem Documentation",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#0f1e0a"/><stop offset="100%" stop-color="#060a04"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><rect x="55" y="50" width="80" height="100" rx="4" fill="#1b3a1b" stroke="#66bb6a" stroke-width="1.5" opacity="0.7"/><path d="M55,60 Q45,55 50,50 L55,50" fill="#1b3a1b" stroke="#66bb6a" stroke-width="1" opacity="0.5"/><path d="M55,140 Q45,145 50,150 L55,150" fill="#1b3a1b" stroke="#66bb6a" stroke-width="1" opacity="0.5"/><line x1="65" y1="70" x2="125" y2="70" stroke="#e8f5e9" stroke-width="0.8" opacity="0.3"/><line x1="65" y1="82" x2="120" y2="82" stroke="#e8f5e9" stroke-width="0.8" opacity="0.3"/><line x1="65" y1="94" x2="115" y2="94" stroke="#e8f5e9" stroke-width="0.8" opacity="0.3"/><line x1="65" y1="106" x2="122" y2="106" stroke="#e8f5e9" stroke-width="0.8" opacity="0.3"/><line x1="65" y1="118" x2="110" y2="118" stroke="#e8f5e9" stroke-width="0.8" opacity="0.3"/><line x1="140" y1="45" x2="115" y2="140" stroke="#e8f5e9" stroke-width="2" opacity="0.6"/><polygon points="140,45 145,42 142,38" fill="#e8f5e9" opacity="0.7"/><circle cx="118" cy="130" r="2" fill="#66bb6a" opacity="0.5"/><circle cx="110" cy="135" r="1.5" fill="#66bb6a" opacity="0.4"/></g></svg>',
            "set_code": "HOLO"
        },
        "prompttovideo": {
            "name": "PromptToVideo",
            "title": "The Artificer",
            "mana_cost": "{2}{R}",
            "colors": ["R"],
            "type_line": "Creature \u2014 Agent Artificer",
            "rarity": "rare",
            "power": 3,
            "toughness": 4,
            "abilities": [
                {"keyword": "Render", "cost": "{T}", "text": "Transform structured scene descriptions into polished MP4 video. Title, content, quote, and list scenes supported."},
                {"keyword": "Style Mastery", "cost": "", "text": "Choose bold, minimal, neon, or warm. The Artificer adapts."}
            ],
            "flavor_text": "\"Words go in. Cinema comes out. Don't ask how the Remotion furnace works \u2014 just feed it scenes.\" \u2014Artificer's Workshop Manual",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#2a0a0a"/><stop offset="100%" stop-color="#0a0505"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><circle cx="80" cy="90" r="35" fill="none" stroke="#f44336" stroke-width="2" opacity="0.7"/><circle cx="80" cy="90" r="28" fill="none" stroke="#ff9800" stroke-width="1" opacity="0.4"/><rect x="68" y="55" width="8" height="12" rx="2" fill="#f44336" opacity="0.6"/><rect x="88" y="55" width="8" height="12" rx="2" fill="#f44336" opacity="0.6"/><rect x="55" y="78" width="12" height="8" rx="2" fill="#f44336" opacity="0.6"/><rect x="98" y="78" width="12" height="8" rx="2" fill="#f44336" opacity="0.6"/><rect x="110" y="105" width="50" height="35" rx="3" fill="#331111" stroke="#ff9800" stroke-width="1.5" opacity="0.7"/><rect x="115" y="110" width="40" height="25" rx="2" fill="none" stroke="#f44336" stroke-width="0.8" opacity="0.5"/><polygon points="130,115 130,130 142,122" fill="#ff9800" opacity="0.7"/><line x1="80" y1="125" x2="110" y2="120" stroke="#f44336" stroke-width="1" opacity="0.4"/></g></svg>',
            "set_code": "HOLO"
        },
        "demovideo": {
            "name": "DemoVideo",
            "title": "The Director",
            "mana_cost": "{2}{R}{U}",
            "colors": ["R", "U"],
            "type_line": "Creature \u2014 Agent Director",
            "rarity": "rare",
            "power": 3,
            "toughness": 5,
            "abilities": [
                {"keyword": "Action!", "cost": "{T}", "text": "Automate a live web app with Playwright. Capture screenshots at every step. Render with animated cursor and zoom."},
                {"keyword": "Zoom Control", "cost": "", "text": "Direct the camera to any element. The audience sees what you want them to see."}
            ],
            "flavor_text": "\"Click. Type. Scroll. Zoom. The Director doesn't just record \u2014 she choreographs.\" \u2014Post-Production Notes",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#1a0a1e"/><stop offset="100%" stop-color="#080510"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><rect x="45" y="60" width="80" height="60" rx="5" fill="#1a1a2e" stroke="#e53935" stroke-width="2" opacity="0.8"/><circle cx="85" cy="90" r="20" fill="none" stroke="#1e88e5" stroke-width="2" opacity="0.7"/><circle cx="85" cy="90" r="12" fill="none" stroke="#e53935" stroke-width="1" opacity="0.5"/><circle cx="85" cy="90" r="5" fill="#e53935" opacity="0.6"/><rect x="125" y="75" width="15" height="30" rx="2" fill="#1a1a2e" stroke="#e53935" stroke-width="1" opacity="0.6"/><polygon points="140,85 155,75 155,95" fill="#e53935" opacity="0.5"/><text x="55" y="155" font-family="monospace" font-size="28" fill="#1e88e5" opacity="0.6">&lt;</text><text x="105" y="155" font-family="monospace" font-size="28" fill="#1e88e5" opacity="0.6">/&gt;</text><line x1="75" y1="145" x2="100" y2="135" stroke="#e53935" stroke-width="1" opacity="0.3"/></g></svg>',
            "set_code": "HOLO"
        },
        "experiment": {
            "name": "Experiment",
            "title": "The Scientist",
            "mana_cost": "{1}{U}{R}",
            "colors": ["U", "R"],
            "type_line": "Creature \u2014 Agent Scientist",
            "rarity": "uncommon",
            "power": 2,
            "toughness": 4,
            "abilities": [
                {"keyword": "A/B Split", "cost": "{T}", "text": "Send one prompt to multiple brainstem personalities. Compare responses on length, confidence, hedging, structure."},
                {"keyword": "Batch Mode", "cost": "", "text": "Queue multiple prompts. Run them all. Tabulate the differences."}
            ],
            "flavor_text": "\"Hypothesis: Mau is more verbose than HOLO. Method: Ask both. Result: Confirmed at p < 0.01.\" \u2014Experiment Log #42",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#15101e"/><stop offset="100%" stop-color="#080510"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><rect x="90" y="40" width="20" height="25" rx="3" fill="none" stroke="#9e9e9e" stroke-width="1.5" opacity="0.6"/><polygon points="70,65 130,65 140,155 60,155" fill="none" stroke="#9e9e9e" stroke-width="1.5" opacity="0.5"/><line x1="100" y1="65" x2="100" y2="155" stroke="#fff" stroke-width="1" opacity="0.3"/><rect x="70" y="65" width="30" height="90" rx="0" fill="#1e88e5" opacity="0.2"/><rect x="100" y="65" width="30" height="90" rx="0" fill="#e53935" opacity="0.2"/><circle cx="82" cy="100" r="5" fill="#1e88e5" opacity="0.5"/><circle cx="118" cy="110" r="5" fill="#e53935" opacity="0.5"/><circle cx="85" cy="125" r="3" fill="#42a5f5" opacity="0.4"/><circle cx="115" cy="95" r="3" fill="#ef5350" opacity="0.4"/><circle cx="78" cy="85" r="4" fill="#1e88e5" opacity="0.3"/><circle cx="122" cy="130" r="4" fill="#e53935" opacity="0.3"/></g></svg>',
            "set_code": "HOLO"
        },
        "hackernews": {
            "name": "HackerNews",
            "title": "The Scout",
            "mana_cost": "{1}",
            "colors": [],
            "type_line": "Creature \u2014 Agent Scout",
            "rarity": "common",
            "power": 1,
            "toughness": 1,
            "abilities": [
                {"keyword": "Fetch", "cost": "{T}", "text": "Pull the top 10 stories from the Hacker News frontier. Return title, URL, score, author."}
            ],
            "flavor_text": "\"The Scout doesn't form opinions. The Scout reports what's trending. The comments section forms the opinions.\" \u2014Intelligence Briefing Protocol",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#1a1a1a"/><stop offset="100%" stop-color="#0a0a0a"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><circle cx="100" cy="100" r="60" fill="none" stroke="#9e9e9e" stroke-width="1.5" opacity="0.5"/><circle cx="100" cy="100" r="45" fill="none" stroke="#bdbdbd" stroke-width="0.8" opacity="0.3"/><circle cx="100" cy="100" r="30" fill="none" stroke="#9e9e9e" stroke-width="0.5" opacity="0.2"/><line x1="100" y1="35" x2="100" y2="165" stroke="#bdbdbd" stroke-width="0.8" opacity="0.3"/><line x1="35" y1="100" x2="165" y2="100" stroke="#bdbdbd" stroke-width="0.8" opacity="0.3"/><line x1="100" y1="100" x2="100" y2="45" stroke="#e0e0e0" stroke-width="2" opacity="0.8"/><line x1="100" y1="100" x2="135" y2="115" stroke="#bdbdbd" stroke-width="1.5" opacity="0.6"/><circle cx="100" cy="100" r="4" fill="#e0e0e0" opacity="0.9"/><circle cx="100" cy="40" r="3" fill="#bdbdbd" opacity="0.5"/><circle cx="160" cy="100" r="3" fill="#bdbdbd" opacity="0.5"/><circle cx="100" cy="160" r="3" fill="#bdbdbd" opacity="0.5"/><circle cx="40" cy="100" r="3" fill="#bdbdbd" opacity="0.5"/></g></svg>',
            "set_code": "HOLO"
        },
        "holonaming": {
            "name": "HoloNaming",
            "title": "The Admiral",
            "mana_cost": "{2}{W}",
            "colors": ["W"],
            "type_line": "Legendary Creature \u2014 Agent Admiral",
            "rarity": "rare",
            "power": 3,
            "toughness": 4,
            "abilities": [
                {"keyword": "Commission", "cost": "{T}", "text": "Assign a Star Trek-themed friendly name from 1600+ combinations. Register on holo.local with auto-port."},
                {"keyword": "Reverse Proxy", "cost": "", "text": "All services accessible through clean URLs. The Admiral routes all traffic."}
            ],
            "flavor_text": "\"USS Quantum-Defiant, you are cleared for port 8742. Engage.\" \u2014Admiral, Starfleet Naming Authority",
            "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#141428"/><stop offset="100%" stop-color="#08081a"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><path d="M100,40 L130,110 L100,95 L70,110 Z" fill="#ffd700" opacity="0.3" stroke="#ffd700" stroke-width="1.5"/><path d="M100,40 L110,75 L100,68 L90,75 Z" fill="#ffd700" opacity="0.5"/><polygon points="100,50 104,62 116,62 106,70 110,82 100,74 90,82 94,70 84,62 96,62" fill="#fff" opacity="0.7"/><line x1="55" y1="125" x2="145" y2="125" stroke="#ffd700" stroke-width="1" opacity="0.4"/><line x1="60" y1="132" x2="140" y2="132" stroke="#ffd700" stroke-width="0.8" opacity="0.3"/><line x1="65" y1="139" x2="135" y2="139" stroke="#ffd700" stroke-width="0.5" opacity="0.2"/><circle cx="100" cy="110" r="8" fill="none" stroke="#ffd700" stroke-width="1" opacity="0.4"/><circle cx="100" cy="155" r="3" fill="#ffd700" opacity="0.5"/><circle cx="80" cy="150" r="2" fill="#fff" opacity="0.3"/><circle cx="120" cy="150" r="2" fill="#fff" opacity="0.3"/></g></svg>',
            "set_code": "HOLO"
        }
    }

    def _cards_path(self):
        return os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            ".brainstem_data", "cards.json"
        )

    def _load_cards(self):
        path = self._cards_path()
        if os.path.isfile(path):
            with open(path, "r") as f:
                return json.load(f)
        return []

    def _save_cards(self, cards):
        path = self._cards_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(cards, f, indent=2)

    def perform(self, **kwargs):
        action = kwargs.get("action", "gallery")

        if action == "forge":
            agent_name = kwargs.get("agent_name", "")
            key = agent_name.lower().replace(" ", "")
            card = self._CARD_DATABASE.get(key)
            if not card:
                available = ", ".join(sorted(self._CARD_DATABASE.keys()))
                return f"Unknown agent '{agent_name}'. Available agents: {available}"
            cards = self._load_cards()
            cards = [c for c in cards if c.get("name") != card["name"]]
            cards.append(card)
            self._save_cards(cards)
            return json.dumps(card, indent=2)

        elif action == "forge_all":
            cards = list(self._CARD_DATABASE.values())
            self._save_cards(cards)
            return f"All {len(cards)} agent cards have been forged! Gallery available at /cards/gallery"

        elif action == "gallery":
            return "Gallery available at /cards/gallery"

        return f"Unknown action: {action}. Use forge, forge_all, or gallery."
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
