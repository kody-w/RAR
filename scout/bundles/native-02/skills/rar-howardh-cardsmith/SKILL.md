---
name: "rar-howardh-cardsmith"
description: "Forges Magic: The Gathering style trading cards for AI agents. Can forge individual agent cards, forge all cards at once, or link to the visual gallery."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/cardsmith_agent", "rar_sha256": "ecbabf0ca4b13f8c98558c9f773d95291d0c4c41e61604667aa32a901105491b", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Howard", "tags": ["productivity", "cards", "visualization", "trading-cards", "sneakernet"]}
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
