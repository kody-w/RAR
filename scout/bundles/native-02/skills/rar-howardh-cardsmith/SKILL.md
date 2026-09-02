---
name: "rar-howardh-cardsmith"
description: "Forges Magic: The Gathering style trading cards for AI agents. Can forge individual agent cards, forge all cards at once, or link to the visual gallery."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/cardsmith_agent", "rar_sha256": "d7389ce10549693f4f97098379ca86c4ddbb22c9b4b93f891c99ae2f1aa0d4d4", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "cardsmith_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@howardh/cardsmith:78b081e93ee3180dd48e0d2432279e08d28f7e38f317612bdc6453b6a74215fe", "kind": "skill"}, "version": "1.0.1", "author": "Howard", "tags": ["productivity", "cards", "visualization", "trading-cards", "sneakernet"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@howardh/cardsmith_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `cardsmith_agent.py` is
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
