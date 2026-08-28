---
name: "rar-howardh-cardsmith"
description: "Forges Magic: The Gathering style trading cards for AI agents. Can forge individual agent cards, forge all cards at once, or link to the visual gallery."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/cardsmith_agent", "rar_sha256": "d7389ce10549693f4f97098379ca86c4ddbb22c9b4b93f891c99ae2f1aa0d4d4", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Howard", "tags": ["productivity", "cards", "visualization", "trading-cards", "sneakernet"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `cardsmith_agent.py` and embedded as the fenced Python below (sha256 d7389ce10549693f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `cardsmith_agent.py` first:

```bash
python3 cardsmith_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 cardsmith_agent.py   # or on stdin
python3 cardsmith_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
