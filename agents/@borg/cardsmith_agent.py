try:
    from basic_agent import BasicAgent
except ModuleNotFoundError:
    from agents.basic_agent import BasicAgent

import os
import json

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@borg/cardsmith_agent",
    "version": "1.0.0",
    "display_name": "CardSmith",
    "description": "Forges trading cards for AI agents. Turn any agent into a collectible card with stats, abilities, and art.",
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
