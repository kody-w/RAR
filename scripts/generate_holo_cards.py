#!/usr/bin/env python3
"""
Generate HOLO cards for every agent in the registry.
Uses Howard's 13 originals verbatim. Generates the rest procedurally
using the same schema (name, title, mana_cost, colors, type_line, rarity,
power, toughness, abilities, flavor_text, avatar_svg, set_code).

Output: cards/holo_cards.json — loaded by the frontend from GitHub raw.
"""

import json
import math
import os
import sys

# ── Deterministic PRNG (Mulberry32 — same as frontend) ──
def mulberry32(seed):
    s = seed & 0xFFFFFFFF
    def next_val():
        nonlocal s
        s = (s + 0x6D2B79F5) & 0xFFFFFFFF
        t = s ^ (s >> 15)
        t = (t * (1 | s)) & 0xFFFFFFFF
        t = (t + ((t ^ (t >> 7)) * (61 | t) & 0xFFFFFFFF)) ^ t
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296
    return next_val

def seed_hash(s):
    h = 0
    for c in s:
        h = ((h << 5) - h + ord(c)) & 0xFFFFFFFF
    return h

# ── Howard's 13 originals — loaded from his CardSmith agent ──
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

HOWARD_CARDS = {}
try:
    cardsmith_path = os.path.join(os.path.dirname(__file__), '..', 'agents', '@borg', 'cardsmith_agent.py')
    with open(cardsmith_path, 'r') as f:
        src = f.read()
    # Extract _CARD_DATABASE dict
    import ast
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == '_CARD_DATABASE':
                    # Can't eval AST with single quotes in SVG, parse manually
                    pass
    # Fallback: exec the class and grab it
    # We'll use a simpler approach — just hardcode the slug→agent_name mapping
    # and load the SVGs from the Python source
except Exception:
    pass

# Howard's canonical cards — we embed them directly with full SVGs from his agent
HOWARD_DB = {
    "borg": {
        "name": "Borg", "title": "The Assimilator", "mana_cost": "{2}{U}{B}",
        "colors": ["U","B"], "type_line": "Creature \u2014 Agent Assimilator",
        "rarity": "mythic", "power": 6, "toughness": 4,
        "abilities": [
            {"keyword": "Assimilate", "cost": "{T}", "text": "Target GitHub repository or URL becomes part of the collective. Create a structured knowledge report."},
            {"keyword": "Adaptive Analysis", "cost": "", "text": "When Borg assimilates, it detects the tech stack and maps 40+ framework patterns."}
        ],
        "flavor_text": "\u201cResistance is futile. Your codebase will be added to our own. Your architectural distinctiveness will be catalogued.\u201d \u2014Borg Collective Directive 7.1",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#1a0a3e"/><stop offset="100%" stop-color="#080818"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><rect x="55" y="55" width="90" height="90" fill="none" stroke="#4a9eff" stroke-width="2" rx="4"/><rect x="70" y="70" width="60" height="60" fill="none" stroke="#8b5cf6" stroke-width="1.5" rx="2"/><line x1="55" y1="100" x2="145" y2="100" stroke="#4a9eff" stroke-width="1" opacity="0.6"/><line x1="100" y1="55" x2="100" y2="145" stroke="#4a9eff" stroke-width="1" opacity="0.6"/><polygon points="100,25 135,45 135,85 100,105 65,85 65,45" fill="none" stroke="#8b5cf6" stroke-width="1" opacity="0.4"/><polygon points="100,95 135,115 135,155 100,175 65,155 65,115" fill="none" stroke="#4a9eff" stroke-width="1" opacity="0.4"/><circle cx="100" cy="100" r="15" fill="#4a9eff" opacity="0.2"/><circle cx="100" cy="100" r="6" fill="#8b5cf6" opacity="0.9"/><circle cx="85" cy="85" r="3" fill="#4a9eff" opacity="0.5"/><circle cx="115" cy="85" r="3" fill="#4a9eff" opacity="0.5"/><circle cx="85" cy="115" r="3" fill="#4a9eff" opacity="0.5"/><circle cx="115" cy="115" r="3" fill="#4a9eff" opacity="0.5"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/borg_agent"
    },
    "anvil": {
        "name": "Anvil", "title": "The Enforcer", "mana_cost": "{1}{R}{W}",
        "colors": ["R","W"], "type_line": "Creature \u2014 Agent Enforcer",
        "rarity": "rare", "power": 4, "toughness": 5,
        "abilities": [
            {"keyword": "Evidence Strike", "cost": "{T}", "text": "Run build, test, or lint commands. Create an evidence bundle with real output, not self-reported claims."},
            {"keyword": "Verification Ledger", "cost": "", "text": "Anvil keeps a persistent record of all checks. Nothing escapes the ledger."},
            {"keyword": "Pushback", "cost": "", "text": "When a claim is unverified, Anvil challenges it. Counter target unsubstantiated assertion."}
        ],
        "flavor_text": "\u201cI don't care what you think passed. Show me the output.\u201d \u2014Anvil, addressing a confident but wrong CI pipeline",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#2a0a0a"/><stop offset="100%" stop-color="#0a0808"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><polygon points="60,130 140,130 155,155 45,155" fill="#555" stroke="#888" stroke-width="1.5"/><rect x="75" y="105" width="50" height="25" rx="3" fill="#666" stroke="#999" stroke-width="1"/><rect x="85" y="85" width="30" height="20" rx="2" fill="#777" stroke="#aaa" stroke-width="1"/><line x1="100" y1="60" x2="75" y2="35" stroke="#ff6f00" stroke-width="2" opacity="0.8"/><line x1="100" y1="60" x2="125" y2="30" stroke="#ff6f00" stroke-width="2" opacity="0.8"/><line x1="100" y1="60" x2="60" y2="50" stroke="#d32f2f" stroke-width="1.5" opacity="0.6"/><line x1="100" y1="60" x2="140" y2="45" stroke="#d32f2f" stroke-width="1.5" opacity="0.6"/><line x1="100" y1="60" x2="100" y2="25" stroke="#ff9800" stroke-width="2" opacity="0.9"/><circle cx="75" cy="35" r="3" fill="#ff6f00" opacity="0.9"/><circle cx="125" cy="30" r="3" fill="#ff6f00" opacity="0.9"/><circle cx="100" cy="25" r="3" fill="#ff9800"/><circle cx="60" cy="50" r="2" fill="#d32f2f" opacity="0.7"/><circle cx="140" cy="45" r="2" fill="#d32f2f" opacity="0.7"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/anvil_agent"
    },
    "personafactory": {
        "name": "PersonaFactory", "title": "The Shaper", "mana_cost": "{3}{U}{G}",
        "colors": ["U","G"], "type_line": "Creature \u2014 Agent Shaper",
        "rarity": "mythic", "power": 5, "toughness": 5,
        "abilities": [
            {"keyword": "Genesis", "cost": "{T}", "text": "Create a new brainstem personality from a single sentence. Generate soul.md, style.md, assign port, register on holo.local."},
            {"keyword": "Trait Weaving", "cost": "", "text": "Choose assertiveness, social style, and expertise. The new mind inherits them all."}
        ],
        "flavor_text": "\u201cShe spoke one sentence into the void. The void answered with a name, a voice, and opinions about semicolons.\u201d \u2014Origin Log, Persona #37",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#0a2a2a"/><stop offset="100%" stop-color="#050f0f"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><circle cx="100" cy="55" r="20" fill="none" stroke="#4caf50" stroke-width="2" opacity="0.8"/><polygon points="100,75 130,145 70,145" fill="none" stroke="#2196f3" stroke-width="2" opacity="0.7"/><circle cx="100" cy="100" r="50" fill="none" stroke="#00bcd4" stroke-width="1" opacity="0.3"/><circle cx="100" cy="100" r="70" fill="none" stroke="#4caf50" stroke-width="0.8" opacity="0.2"/><circle cx="100" cy="100" r="90" fill="none" stroke="#2196f3" stroke-width="0.5" opacity="0.15"/><circle cx="60" cy="70" r="4" fill="#4caf50" opacity="0.6"/><circle cx="140" cy="70" r="4" fill="#2196f3" opacity="0.6"/><circle cx="55" cy="120" r="3" fill="#00bcd4" opacity="0.5"/><circle cx="145" cy="120" r="3" fill="#00bcd4" opacity="0.5"/><circle cx="100" cy="55" r="8" fill="#4caf50" opacity="0.3"/><line x1="100" y1="75" x2="100" y2="145" stroke="#2196f3" stroke-width="1" opacity="0.4"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/persona_factory_agent"
    },
    "tinyworld": {
        "name": "TinyWorld", "title": "The Architect", "mana_cost": "{W}{U}{B}{R}{G}",
        "colors": ["W","U","B","R","G"], "type_line": "Legendary Creature \u2014 Agent Architect",
        "rarity": "mythic", "power": 7, "toughness": 7,
        "abilities": [
            {"keyword": "Simulation", "cost": "{2}{T}", "text": "Choose a topic. All agents enter the arena. They debate, argue, and synthesize. Extract consensus."},
            {"keyword": "Roundtable", "cost": "", "text": "At the beginning of each round, assign roles \u2014 advocate, skeptic, architect, reviewer."},
            {"keyword": "Insight Extraction", "cost": "", "text": "When the simulation ends, distill agreements, disagreements, and next steps."}
        ],
        "flavor_text": "\u201cIn TinyWorld, your best ideas fight your worst ideas, and the survivors become your strategy.\u201d \u2014Architect\u2019s Manual, Chapter 1",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#1a1a2e"/><stop offset="100%" stop-color="#08080f"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><circle cx="100" cy="100" r="55" fill="none" stroke="#6a6aaa" stroke-width="1.5" opacity="0.5"/><ellipse cx="100" cy="100" rx="55" ry="20" fill="none" stroke="#6a6aaa" stroke-width="0.8" opacity="0.3"/><ellipse cx="100" cy="100" rx="20" ry="55" fill="none" stroke="#6a6aaa" stroke-width="0.8" opacity="0.3"/><ellipse cx="100" cy="100" rx="55" ry="35" fill="none" stroke="#6a6aaa" stroke-width="0.5" opacity="0.2" transform="rotate(30 100 100)"/><circle cx="100" cy="45" r="6" fill="#f9e076" opacity="0.9"/><circle cx="148" cy="80" r="6" fill="#0e67ab" opacity="0.9"/><circle cx="135" cy="135" r="6" fill="#3d3d3d" opacity="0.9"/><circle cx="65" cy="135" r="6" fill="#d3202a" opacity="0.9"/><circle cx="52" cy="80" r="6" fill="#00733e" opacity="0.9"/><line x1="100" y1="45" x2="148" y2="80" stroke="#f9e076" stroke-width="0.8" opacity="0.4"/><line x1="148" y1="80" x2="135" y2="135" stroke="#0e67ab" stroke-width="0.8" opacity="0.4"/><line x1="135" y1="135" x2="65" y2="135" stroke="#3d3d3d" stroke-width="0.8" opacity="0.4"/><line x1="65" y1="135" x2="52" y2="80" stroke="#d3202a" stroke-width="0.8" opacity="0.4"/><line x1="52" y1="80" x2="100" y2="45" stroke="#00733e" stroke-width="0.8" opacity="0.4"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/tinyworld_agent"
    },
    "bridge": {
        "name": "Bridge", "title": "The Conduit", "mana_cost": "{2}{U}",
        "colors": ["U"], "type_line": "Artifact \u2014 Agent Conduit",
        "rarity": "uncommon", "power": None, "toughness": None,
        "abilities": [
            {"keyword": "Channel", "cost": "", "text": "Register any messaging platform. Route inbound webhooks to the right brainstem personality."},
            {"keyword": "Webhook Receiver", "cost": "", "text": "Bridge listens on port 9001. Messages flow in, responses flow out."}
        ],
        "flavor_text": "\u201cIt doesn't matter where the message comes from \u2014 Slack, Discord, carrier pigeon. Bridge delivers.\u201d \u2014HOLO Network Ops Manual",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#0a1a2e"/><stop offset="100%" stop-color="#050a14"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><rect x="40" y="90" width="20" height="70" rx="3" fill="#1565c0" opacity="0.7"/><rect x="140" y="90" width="20" height="70" rx="3" fill="#1565c0" opacity="0.7"/><path d="M50,90 Q100,30 150,90" fill="none" stroke="#42a5f5" stroke-width="3" opacity="0.8"/><path d="M50,95 Q100,40 150,95" fill="none" stroke="#64b5f6" stroke-width="1.5" opacity="0.5"/><line x1="30" y1="110" x2="170" y2="110" stroke="#42a5f5" stroke-width="1" opacity="0.4" stroke-dasharray="4,4"/><line x1="30" y1="120" x2="170" y2="120" stroke="#64b5f6" stroke-width="1" opacity="0.3" stroke-dasharray="4,4"/><line x1="30" y1="130" x2="170" y2="130" stroke="#42a5f5" stroke-width="1" opacity="0.2" stroke-dasharray="4,4"/><circle cx="50" cy="110" r="4" fill="#42a5f5" opacity="0.8"/><circle cx="150" cy="110" r="4" fill="#42a5f5" opacity="0.8"/><circle cx="100" cy="60" r="5" fill="#64b5f6" opacity="0.6"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/bridge_agent"
    },
    "telegram": {
        "name": "Telegram", "title": "The Courier", "mana_cost": "{1}{U}{W}",
        "colors": ["U","W"], "type_line": "Creature \u2014 Agent Courier",
        "rarity": "uncommon", "power": 2, "toughness": 3,
        "abilities": [
            {"keyword": "Relay", "cost": "{T}", "text": "Bridge Telegram to any brainstem. Chat from your phone. Supports /holo and /mau routing."},
            {"keyword": "URL Detection", "cost": "", "text": "When a URL is sent via Telegram, automatically invoke Borg to assimilate it."}
        ],
        "flavor_text": "\u201cThe courier never reads the message. But if you send a URL, she'll make sure Borg reads it.\u201d \u2014Telegram Bridge Service Note",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#0a1a2e"/><stop offset="100%" stop-color="#080810"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><polygon points="40,100 160,60 120,110" fill="#0088cc" opacity="0.7" stroke="#29b6f6" stroke-width="1"/><polygon points="120,110 160,60 140,140" fill="#0077b5" opacity="0.6" stroke="#29b6f6" stroke-width="0.8"/><polygon points="120,110 90,125 105,100" fill="#005f8e" opacity="0.8"/><line x1="40" y1="100" x2="70" y2="150" stroke="#fff" stroke-width="0.5" opacity="0.3" stroke-dasharray="3,3"/><line x1="160" y1="60" x2="170" y2="40" stroke="#fff" stroke-width="0.5" opacity="0.3" stroke-dasharray="3,3"/><line x1="80" y1="70" x2="130" y2="55" stroke="#29b6f6" stroke-width="0.5" opacity="0.3"/><circle cx="70" cy="150" r="2" fill="#fff" opacity="0.4"/><circle cx="170" cy="40" r="2" fill="#fff" opacity="0.4"/><circle cx="40" cy="100" r="3" fill="#29b6f6" opacity="0.6"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/telegram_agent"
    },
    "contextmemory": {
        "name": "ContextMemory", "title": "The Oracle", "mana_cost": "{1}{G}{G}",
        "colors": ["G"], "type_line": "Enchantment \u2014 Agent Aura",
        "rarity": "rare", "power": None, "toughness": None,
        "abilities": [
            {"keyword": "Total Recall", "cost": "", "text": "At the start of each conversation, search stored memories. Filter by keywords, user, or recall everything."},
            {"keyword": "System Context Injection", "cost": "", "text": "ContextMemory silently weaves relevant past interactions into the system prompt."}
        ],
        "flavor_text": "\u201cYou said that on a Tuesday. You were frustrated. You used the word 'elegant' sarcastically. I remember everything.\u201d \u2014The Oracle",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#0a1e0a"/><stop offset="100%" stop-color="#050a05"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><ellipse cx="100" cy="100" rx="60" ry="30" fill="none" stroke="#4caf50" stroke-width="2" opacity="0.7"/><ellipse cx="100" cy="100" rx="60" ry="30" fill="none" stroke="#4caf50" stroke-width="1" opacity="0.3" transform="rotate(90 100 100)"/><circle cx="100" cy="100" r="45" fill="none" stroke="#2e7d32" stroke-width="1" opacity="0.3"/><circle cx="100" cy="100" r="55" fill="none" stroke="#1b5e20" stroke-width="0.8" opacity="0.2"/><circle cx="100" cy="100" r="65" fill="none" stroke="#4caf50" stroke-width="0.5" opacity="0.15"/><circle cx="100" cy="100" r="75" fill="none" stroke="#2e7d32" stroke-width="0.5" opacity="0.1"/><circle cx="100" cy="100" r="18" fill="#4caf50" opacity="0.15"/><circle cx="100" cy="100" r="10" fill="#4caf50" opacity="0.3"/><circle cx="100" cy="100" r="4" fill="#66bb6a" opacity="0.9"/><path d="M60,100 Q80,80 100,100 Q120,120 140,100" fill="none" stroke="#4caf50" stroke-width="2" opacity="0.6"/><path d="M60,100 Q80,120 100,100 Q120,80 140,100" fill="none" stroke="#4caf50" stroke-width="2" opacity="0.6"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/context_memory_agent"
    },
    "managememory": {
        "name": "ManageMemory", "title": "The Scribe", "mana_cost": "{G}{W}",
        "colors": ["G","W"], "type_line": "Creature \u2014 Agent Scribe",
        "rarity": "common", "power": 1, "toughness": 3,
        "abilities": [
            {"keyword": "Inscribe", "cost": "{T}", "text": "Save a fact, preference, insight, or task to persistent storage. Tag it. Rate its importance."}
        ],
        "flavor_text": "\u201cThe Scribe writes. The Oracle reads. Between them, nothing is forgotten.\u201d \u2014Memory Subsystem Documentation",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#0f1e0a"/><stop offset="100%" stop-color="#060a04"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><rect x="55" y="50" width="80" height="100" rx="4" fill="#1b3a1b" stroke="#66bb6a" stroke-width="1.5" opacity="0.7"/><path d="M55,60 Q45,55 50,50 L55,50" fill="#1b3a1b" stroke="#66bb6a" stroke-width="1" opacity="0.5"/><path d="M55,140 Q45,145 50,150 L55,150" fill="#1b3a1b" stroke="#66bb6a" stroke-width="1" opacity="0.5"/><line x1="65" y1="70" x2="125" y2="70" stroke="#e8f5e9" stroke-width="0.8" opacity="0.3"/><line x1="65" y1="82" x2="120" y2="82" stroke="#e8f5e9" stroke-width="0.8" opacity="0.3"/><line x1="65" y1="94" x2="115" y2="94" stroke="#e8f5e9" stroke-width="0.8" opacity="0.3"/><line x1="65" y1="106" x2="122" y2="106" stroke="#e8f5e9" stroke-width="0.8" opacity="0.3"/><line x1="65" y1="118" x2="110" y2="118" stroke="#e8f5e9" stroke-width="0.8" opacity="0.3"/><line x1="140" y1="45" x2="115" y2="140" stroke="#e8f5e9" stroke-width="2" opacity="0.6"/><polygon points="140,45 145,42 142,38" fill="#e8f5e9" opacity="0.7"/><circle cx="118" cy="130" r="2" fill="#66bb6a" opacity="0.5"/><circle cx="110" cy="135" r="1.5" fill="#66bb6a" opacity="0.4"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/manage_memory_agent"
    },
    "prompttovideo": {
        "name": "PromptToVideo", "title": "The Artificer", "mana_cost": "{2}{R}",
        "colors": ["R"], "type_line": "Creature \u2014 Agent Artificer",
        "rarity": "rare", "power": 3, "toughness": 4,
        "abilities": [
            {"keyword": "Render", "cost": "{T}", "text": "Transform structured scene descriptions into polished MP4 video. Title, content, quote, and list scenes supported."},
            {"keyword": "Style Mastery", "cost": "", "text": "Choose bold, minimal, neon, or warm. The Artificer adapts."}
        ],
        "flavor_text": "\u201cWords go in. Cinema comes out. Don't ask how the Remotion furnace works \u2014 just feed it scenes.\u201d \u2014Artificer\u2019s Workshop Manual",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#2a0a0a"/><stop offset="100%" stop-color="#0a0505"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><circle cx="80" cy="90" r="35" fill="none" stroke="#f44336" stroke-width="2" opacity="0.7"/><circle cx="80" cy="90" r="28" fill="none" stroke="#ff9800" stroke-width="1" opacity="0.4"/><rect x="68" y="55" width="8" height="12" rx="2" fill="#f44336" opacity="0.6"/><rect x="88" y="55" width="8" height="12" rx="2" fill="#f44336" opacity="0.6"/><rect x="55" y="78" width="12" height="8" rx="2" fill="#f44336" opacity="0.6"/><rect x="98" y="78" width="12" height="8" rx="2" fill="#f44336" opacity="0.6"/><rect x="110" y="105" width="50" height="35" rx="3" fill="#331111" stroke="#ff9800" stroke-width="1.5" opacity="0.7"/><rect x="115" y="110" width="40" height="25" rx="2" fill="none" stroke="#f44336" stroke-width="0.8" opacity="0.5"/><polygon points="130,115 130,130 142,122" fill="#ff9800" opacity="0.7"/><line x1="80" y1="125" x2="110" y2="120" stroke="#f44336" stroke-width="1" opacity="0.4"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/prompt_to_video_agent"
    },
    "demovideo": {
        "name": "DemoVideo", "title": "The Director", "mana_cost": "{2}{R}{U}",
        "colors": ["R","U"], "type_line": "Creature \u2014 Agent Director",
        "rarity": "rare", "power": 3, "toughness": 5,
        "abilities": [
            {"keyword": "Action!", "cost": "{T}", "text": "Automate a live web app with Playwright. Capture screenshots at every step. Render with animated cursor and zoom."},
            {"keyword": "Zoom Control", "cost": "", "text": "Direct the camera to any element. The audience sees what you want them to see."}
        ],
        "flavor_text": "\u201cClick. Type. Scroll. Zoom. The Director doesn't just record \u2014 she choreographs.\u201d \u2014Post-Production Notes",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#1a0a1e"/><stop offset="100%" stop-color="#080510"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><rect x="45" y="60" width="80" height="60" rx="5" fill="#1a1a2e" stroke="#e53935" stroke-width="2" opacity="0.8"/><circle cx="85" cy="90" r="20" fill="none" stroke="#1e88e5" stroke-width="2" opacity="0.7"/><circle cx="85" cy="90" r="12" fill="none" stroke="#e53935" stroke-width="1" opacity="0.5"/><circle cx="85" cy="90" r="5" fill="#e53935" opacity="0.6"/><rect x="125" y="75" width="15" height="30" rx="2" fill="#1a1a2e" stroke="#e53935" stroke-width="1" opacity="0.6"/><polygon points="140,85 155,75 155,95" fill="#e53935" opacity="0.5"/><text x="55" y="155" font-family="monospace" font-size="28" fill="#1e88e5" opacity="0.6">&lt;</text><text x="105" y="155" font-family="monospace" font-size="28" fill="#1e88e5" opacity="0.6">/&gt;</text><line x1="75" y1="145" x2="100" y2="135" stroke="#e53935" stroke-width="1" opacity="0.3"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/demo_video_agent"
    },
    "experiment": {
        "name": "Experiment", "title": "The Scientist", "mana_cost": "{1}{U}{R}",
        "colors": ["U","R"], "type_line": "Creature \u2014 Agent Scientist",
        "rarity": "uncommon", "power": 2, "toughness": 4,
        "abilities": [
            {"keyword": "A/B Split", "cost": "{T}", "text": "Send one prompt to multiple brainstem personalities. Compare responses on length, confidence, hedging, structure."},
            {"keyword": "Batch Mode", "cost": "", "text": "Queue multiple prompts. Run them all. Tabulate the differences."}
        ],
        "flavor_text": "\u201cHypothesis: Mau is more verbose than HOLO. Method: Ask both. Result: Confirmed at p < 0.01.\u201d \u2014Experiment Log #42",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#15101e"/><stop offset="100%" stop-color="#080510"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><rect x="90" y="40" width="20" height="25" rx="3" fill="none" stroke="#9e9e9e" stroke-width="1.5" opacity="0.6"/><polygon points="70,65 130,65 140,155 60,155" fill="none" stroke="#9e9e9e" stroke-width="1.5" opacity="0.5"/><line x1="100" y1="65" x2="100" y2="155" stroke="#fff" stroke-width="1" opacity="0.3"/><rect x="70" y="65" width="30" height="90" rx="0" fill="#1e88e5" opacity="0.2"/><rect x="100" y="65" width="30" height="90" rx="0" fill="#e53935" opacity="0.2"/><circle cx="82" cy="100" r="5" fill="#1e88e5" opacity="0.5"/><circle cx="118" cy="110" r="5" fill="#e53935" opacity="0.5"/><circle cx="85" cy="125" r="3" fill="#42a5f5" opacity="0.4"/><circle cx="115" cy="95" r="3" fill="#ef5350" opacity="0.4"/><circle cx="78" cy="85" r="4" fill="#1e88e5" opacity="0.3"/><circle cx="122" cy="130" r="4" fill="#e53935" opacity="0.3"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/experiment_agent"
    },
    "hackernews": {
        "name": "HackerNews", "title": "The Scout", "mana_cost": "{1}",
        "colors": [], "type_line": "Creature \u2014 Agent Scout",
        "rarity": "common", "power": 1, "toughness": 1,
        "abilities": [
            {"keyword": "Fetch", "cost": "{T}", "text": "Pull the top 10 stories from the Hacker News frontier. Return title, URL, score, author."}
        ],
        "flavor_text": "\u201cThe Scout doesn't form opinions. The Scout reports what's trending. The comments section forms the opinions.\u201d \u2014Intelligence Briefing Protocol",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#1a1a1a"/><stop offset="100%" stop-color="#0a0a0a"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><circle cx="100" cy="100" r="60" fill="none" stroke="#9e9e9e" stroke-width="1.5" opacity="0.5"/><circle cx="100" cy="100" r="45" fill="none" stroke="#bdbdbd" stroke-width="0.8" opacity="0.3"/><circle cx="100" cy="100" r="30" fill="none" stroke="#9e9e9e" stroke-width="0.5" opacity="0.2"/><line x1="100" y1="35" x2="100" y2="165" stroke="#bdbdbd" stroke-width="0.8" opacity="0.3"/><line x1="35" y1="100" x2="165" y2="100" stroke="#bdbdbd" stroke-width="0.8" opacity="0.3"/><line x1="100" y1="100" x2="100" y2="45" stroke="#e0e0e0" stroke-width="2" opacity="0.8"/><line x1="100" y1="100" x2="135" y2="115" stroke="#bdbdbd" stroke-width="1.5" opacity="0.6"/><circle cx="100" cy="100" r="4" fill="#e0e0e0" opacity="0.9"/><circle cx="100" cy="40" r="3" fill="#bdbdbd" opacity="0.5"/><circle cx="160" cy="100" r="3" fill="#bdbdbd" opacity="0.5"/><circle cx="100" cy="160" r="3" fill="#bdbdbd" opacity="0.5"/><circle cx="40" cy="100" r="3" fill="#bdbdbd" opacity="0.5"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/hacker_news_agent"
    },
    "holonaming": {
        "name": "HoloNaming", "title": "The Admiral", "mana_cost": "{2}{W}",
        "colors": ["W"], "type_line": "Legendary Creature \u2014 Agent Admiral",
        "rarity": "rare", "power": 3, "toughness": 4,
        "abilities": [
            {"keyword": "Commission", "cost": "{T}", "text": "Assign a Star Trek-themed friendly name from 1600+ combinations. Register on holo.local with auto-port."},
            {"keyword": "Reverse Proxy", "cost": "", "text": "All services accessible through clean URLs. The Admiral routes all traffic."}
        ],
        "flavor_text": "\u201cUSS Quantum-Defiant, you are cleared for port 8742. Engage.\u201d \u2014Admiral, Starfleet Naming Authority",
        "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg"><stop offset="0%" stop-color="#141428"/><stop offset="100%" stop-color="#08081a"/></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg)"/><g filter="url(#glow)"><path d="M100,40 L130,110 L100,95 L70,110 Z" fill="#ffd700" opacity="0.3" stroke="#ffd700" stroke-width="1.5"/><path d="M100,40 L110,75 L100,68 L90,75 Z" fill="#ffd700" opacity="0.5"/><polygon points="100,50 104,62 116,62 106,70 110,82 100,74 90,82 94,70 84,62 96,62" fill="#fff" opacity="0.7"/><line x1="55" y1="125" x2="145" y2="125" stroke="#ffd700" stroke-width="1" opacity="0.4"/><line x1="60" y1="132" x2="140" y2="132" stroke="#ffd700" stroke-width="0.8" opacity="0.3"/><line x1="65" y1="139" x2="135" y2="139" stroke="#ffd700" stroke-width="0.5" opacity="0.2"/><circle cx="100" cy="110" r="8" fill="none" stroke="#ffd700" stroke-width="1" opacity="0.4"/><circle cx="100" cy="155" r="3" fill="#ffd700" opacity="0.5"/><circle cx="80" cy="150" r="2" fill="#fff" opacity="0.3"/><circle cx="120" cy="150" r="2" fill="#fff" opacity="0.3"/></g></svg>',
        "set_code": "HOLO", "promo": True, "artist": "Howard Hoy", "agent_name": "@borg/holo_naming_agent"
    },
}

# ── Category color palettes (same as frontend) ──
CAT_COLORS = {
    "core": "#58a6ff", "integrations": "#bc8cff", "productivity": "#7ee787",
    "devtools": "#f0883e", "pipeline": "#f778ba", "general": "#8b949e",
    "b2b_sales": "#f47067", "b2c_sales": "#7ee787", "healthcare": "#56d364",
    "financial_services": "#79c0ff", "manufacturing": "#f0883e", "energy": "#f0883e",
    "federal_government": "#79c0ff", "slg_government": "#79c0ff",
    "human_resources": "#7ee787", "it_management": "#58a6ff",
    "professional_services": "#79c0ff", "retail_cpg": "#f0883e",
    "software_digital_products": "#58a6ff",
}

CAT_PIPS = {
    "core": ["W","U"], "integrations": ["U","B"], "productivity": ["G","W"],
    "devtools": ["R","U"], "pipeline": ["B","R"], "general": ["N"],
    "b2b_sales": ["R","W"], "b2c_sales": ["G","W"], "healthcare": ["W","G"],
    "financial_services": ["U","B"], "manufacturing": ["R","G"], "energy": ["R","G"],
    "federal_government": ["W","U"], "slg_government": ["W","U"],
    "human_resources": ["G","W"], "it_management": ["U","R"],
    "professional_services": ["U","W"], "retail_cpg": ["G","R"],
    "software_digital_products": ["U","R"],
}

# ── Diversity pools ──
TITLES = [
    "The Strategist", "The Analyst", "The Navigator", "The Sentinel",
    "The Catalyst", "The Synthesizer", "The Conductor", "The Optimizer",
    "The Resolver", "The Interceptor", "The Vanguard", "The Operator",
    "The Watcher", "The Compiler", "The Pathfinder", "The Calibrator",
    "The Herald", "The Marshal", "The Curator", "The Assessor",
    "The Quartermaster", "The Arbiter", "The Beacon", "The Dispatcher",
    "The Surveyor", "The Overseer", "The Facilitator", "The Alchemist",
    "The Tactician", "The Sage", "The Cartographer", "The Broker",
    "The Pilot", "The Conjurer", "The Warden", "The Machinist",
    "The Prospector", "The Luminary", "The Cipher", "The Nomad",
]

SUBTYPES = [
    "Strategist", "Analyst", "Navigator", "Sentinel", "Catalyst",
    "Conductor", "Optimizer", "Resolver", "Vanguard", "Operator",
    "Compiler", "Pathfinder", "Herald", "Marshal", "Curator",
    "Assessor", "Arbiter", "Dispatcher", "Surveyor", "Overseer",
    "Facilitator", "Alchemist", "Tactician", "Oracle", "Sage",
    "Warden", "Scribe", "Artificer", "Forgemaster", "Conduit",
    "Broker", "Pilot", "Conjurer", "Machinist", "Prospector",
    "Luminary", "Cipher", "Nomad", "Cartographer", "Beacon",
]

FLAVORS = [
    "\u201cThe code compiles. The agent decides. The work gets done.\u201d",
    "\u201cIn a world of noise, the signal belongs to those who listen.\u201d",
    "\u201cIt does not ask permission. It asks what needs doing.\u201d",
    "\u201cSome agents wait for instructions. This one has already started.\u201d",
    "\u201cBetween the input and the output, there is judgment.\u201d",
    "\u201cComplexity is the enemy. Automation is the ally.\u201d",
    "\u201cIt reads the room before it reads the data.\u201d",
    "\u201cWhat the dashboard shows, the agent already knew.\u201d",
    "\u201cThe pipeline never sleeps. The agent never forgets.\u201d",
    "\u201cOne prompt. One purpose. Infinite execution.\u201d",
    "\u201cIt was designed to assist. It chose to excel.\u201d",
    "\u201cWhere others see a task, it sees a system.\u201d",
    "\u201cNot all intelligence is artificial. Some is engineered.\u201d",
    "\u201cSpeed without accuracy is just expensive failure.\u201d",
    "\u201cThe best agent is the one you forget is running.\u201d",
    "\u201cData in. Decisions out. Humans in the loop.\u201d",
    "\u201cTrust is earned one successful execution at a time.\u201d",
    "\u201cIt works while you sleep. It finishes before you wake.\u201d",
    "\u201cEfficiency is not a goal. It\u2019s a side effect of clarity.\u201d",
    "\u201cBuilt to serve. Designed to scale. Ready to deploy.\u201d",
    "\u201cIt doesn\u2019t guess. It calculates.\u201d",
    "\u201cWhere workflows end, this agent begins.\u201d",
    "\u201cThe simplest solution is usually an agent away.\u201d",
    "\u201cThe market moved. The agent moved faster.\u201d",
    "\u201cNo API key required. No excuses accepted.\u201d",
    "\u201cDrop it in. Watch it work. Move on.\u201d",
    "\u201cPrecision at the speed of thought.\u201d",
    "\u201cThe humans set the goals. The agent sets the pace.\u201d",
    "\u201cEvery edge case was someone\u2019s main case.\u201d",
    "\u201cWhen the signal is clear, the decision makes itself.\u201d",
]

# ── Background hue palettes (Howard-style dark gradients) ──
BG_PALETTES = [
    ("#1a0a3e", "#080818"), ("#2a0a0a", "#0a0808"), ("#0a2a2a", "#050f0f"),
    ("#1a1a2e", "#08080f"), ("#0a1a2e", "#050a14"), ("#0a1e0a", "#050a05"),
    ("#0f1e0a", "#060a04"), ("#15101e", "#080510"), ("#1a0a1e", "#080510"),
    ("#141428", "#08081a"), ("#1a1a1a", "#0a0a0a"), ("#0a1a1a", "#050a0a"),
    ("#1e0a1e", "#0a050a"), ("#0a0a2a", "#050510"), ("#1a1e0a", "#0a0a05"),
    ("#2a1a0a", "#0a0805"),
]


def gen_holo_art(name, category, rng):
    """Generate Howard-style 200x200 SVG art with dark bg + glow + geometric shapes."""
    uid = format(seed_hash(name) & 0xFFFFFF, 'x')
    p = CAT_COLORS.get(category, "#8b949e")
    bg = BG_PALETTES[int(rng() * len(BG_PALETTES))]

    svg = []
    svg.append(f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">')
    svg.append(f'<defs><radialGradient id="bg-{uid}"><stop offset="0%" stop-color="{bg[0]}"/><stop offset="100%" stop-color="{bg[1]}"/></radialGradient>')
    svg.append(f'<filter id="gl-{uid}"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>')
    svg.append(f'<rect width="200" height="200" fill="url(#bg-{uid})"/>')
    svg.append(f'<g filter="url(#gl-{uid})">')

    cx, cy = 100, 100
    body = int(rng() * 8)

    if body == 0:
        # Planet with ring
        pr = 30 + int(rng() * 20)
        tilt = 15 + int(rng() * 30)
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{pr}" fill="{p}" opacity="0.15"/>')
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{pr}" fill="none" stroke="{p}" stroke-width="2" opacity="0.6"/>')
        svg.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{pr+15}" ry="{6+int(rng()*8)}" fill="none" stroke="{p}" stroke-width="1.5" opacity="0.35" transform="rotate({tilt} {cx} {cy})"/>')
        for _ in range(3):
            dx = -10 + int(rng() * 20)
            dy = -10 + int(rng() * 20)
            r2 = int(rng() * 8) + 3
            svg.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="{r2}" fill="{p}" opacity="{0.06+rng()*0.08:.2f}"/>')
    elif body == 1:
        # Orbital system
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="{p}" opacity="0.3"/>')
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{p}" opacity="0.7"/>')
        for i in range(2 + int(rng() * 3)):
            orb = 30 + i * 18
            tilt = int(rng() * 60) - 30
            svg.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{orb}" ry="{int(orb*(0.3+rng()*0.5))}" fill="none" stroke="{p}" stroke-width="1" opacity="{0.2+i*0.08:.2f}" transform="rotate({tilt} {cx} {cy})"/>')
            angle = rng() * math.pi * 2
            ox = cx + orb * math.cos(angle) * (0.6 + rng() * 0.4)
            oy = cy + orb * math.sin(angle) * (0.4 + rng() * 0.4)
            svg.append(f'<circle cx="{ox:.1f}" cy="{oy:.1f}" r="{3+int(rng()*3)}" fill="{p}" opacity="0.5"/>')
    elif body == 2:
        # Crystal polygon
        facets = 5 + int(rng() * 4)
        pts = []
        for i in range(facets):
            a = (math.pi * 2 / facets) * i + rng() * 0.3
            d = 25 + int(rng() * 25)
            pts.append(f"{cx + d * math.cos(a):.1f},{cy + d * math.sin(a):.1f}")
        svg.append(f'<polygon points="{" ".join(pts)}" fill="{p}" opacity="0.1" stroke="{p}" stroke-width="2" stroke-opacity="0.5"/>')
        inner = []
        for i in range(facets):
            a = (math.pi * 2 / facets) * i + rng() * 0.3 + 0.3
            d = 12 + int(rng() * 15)
            inner.append(f"{cx + d * math.cos(a):.1f},{cy + d * math.sin(a):.1f}")
        svg.append(f'<polygon points="{" ".join(inner)}" fill="none" stroke="{p}" stroke-width="1.5" opacity="0.35"/>')
        svg.append(f'<line x1="{cx-40}" y1="{cy}" x2="{cx+40}" y2="{cy}" stroke="{p}" stroke-width="1" opacity="0.2"/>')
        svg.append(f'<line x1="{cx}" y1="{cy-40}" x2="{cx}" y2="{cy+40}" stroke="{p}" stroke-width="1" opacity="0.2"/>')
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="8" fill="{p}" opacity="0.25"/>')
    elif body == 3:
        # Nebula
        for _ in range(5 + int(rng() * 4)):
            nx = cx - 30 + int(rng() * 60)
            ny = cy - 30 + int(rng() * 60)
            nr = 15 + int(rng() * 25)
            svg.append(f'<circle cx="{nx}" cy="{ny}" r="{nr}" fill="{p}" opacity="{0.04+rng()*0.08:.2f}"/>')
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="20" fill="{p}" opacity="0.1"/>')
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="10" fill="{p}" opacity="0.2"/>')
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{p}" opacity="0.7"/>')
        for i in range(4):
            a = (math.pi / 2) * i + rng() * 0.5
            ln = 30 + int(rng() * 20)
            svg.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+ln*math.cos(a):.1f}" y2="{cy+ln*math.sin(a):.1f}" stroke="{p}" stroke-width="1" opacity="0.15"/>')
    elif body == 4:
        # Hexagon web
        for ring in range(1, 4):
            r2 = ring * 22
            pts = []
            for i in range(6):
                a = math.pi / 3 * i - math.pi / 6
                pts.append(f"{cx + r2 * math.cos(a):.1f},{cy + r2 * math.sin(a):.1f}")
            svg.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="{p}" stroke-width="{2 - ring * 0.4:.1f}" opacity="{0.5 - ring * 0.1:.2f}"/>')
        star_pts = []
        for i in range(10):
            a = math.pi / 5 * i - math.pi / 2
            sr = 15 if i % 2 == 0 else 7
            star_pts.append(f"{cx + sr * math.cos(a):.1f},{cy + sr * math.sin(a):.1f}")
        svg.append(f'<polygon points="{" ".join(star_pts)}" fill="{p}" opacity="0.3"/>')
        for i in range(6):
            a = math.pi / 3 * i - math.pi / 6
            dx = cx + 44 * math.cos(a)
            dy = cy + 44 * math.sin(a)
            svg.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="4" fill="{p}" opacity="0.4"/>')
    elif body == 5:
        # Binary system
        sep = 25 + int(rng() * 15)
        r1 = 15 + int(rng() * 10)
        r2 = 10 + int(rng() * 10)
        angle = rng() * math.pi
        x1 = cx - sep * math.cos(angle)
        y1 = cy - sep * math.sin(angle)
        x2 = cx + sep * math.cos(angle)
        y2 = cy + sep * math.sin(angle)
        svg.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="{r1}" fill="{p}" opacity="0.15" stroke="{p}" stroke-width="2" stroke-opacity="0.5"/>')
        svg.append(f'<circle cx="{x2:.1f}" cy="{y2:.1f}" r="{r2}" fill="{p}" opacity="0.1" stroke="{p}" stroke-width="1.5" stroke-opacity="0.4"/>')
        svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{p}" stroke-width="1" opacity="0.25" stroke-dasharray="4,4"/>')
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{sep+10}" fill="none" stroke="{p}" stroke-width="0.8" opacity="0.15"/>')
    elif body == 6:
        # Constellation
        nodes = 5 + int(rng() * 4)
        points = []
        for _ in range(nodes):
            points.append((30 + int(rng() * 140), 30 + int(rng() * 140)))
        for i in range(len(points)):
            j = (i + 1) % len(points)
            svg.append(f'<line x1="{points[i][0]}" y1="{points[i][1]}" x2="{points[j][0]}" y2="{points[j][1]}" stroke="{p}" stroke-width="0.8" opacity="0.3"/>')
        if len(points) > 3:
            svg.append(f'<line x1="{points[0][0]}" y1="{points[0][1]}" x2="{points[2][0]}" y2="{points[2][1]}" stroke="{p}" stroke-width="0.5" opacity="0.15"/>')
        for pt in points:
            sz = 3 + int(rng() * 4)
            svg.append(f'<circle cx="{pt[0]}" cy="{pt[1]}" r="{sz}" fill="{p}" opacity="{0.3+rng()*0.4:.2f}"/>')
    else:
        # Abstract arch
        archH = 20 + int(rng() * 30)
        svg.append(f'<path d="M40,{cy+20} Q{cx},{cy-archH} 160,{cy+20}" fill="none" stroke="{p}" stroke-width="3" opacity="0.5"/>')
        svg.append(f'<path d="M40,{cy+25} Q{cx},{cy-archH+10} 160,{cy+25}" fill="none" stroke="{p}" stroke-width="1.5" opacity="0.25"/>')
        svg.append(f'<rect x="35" y="{cy+20}" width="15" height="40" rx="3" fill="{p}" opacity="0.2"/>')
        svg.append(f'<rect x="150" y="{cy+20}" width="15" height="40" rx="3" fill="{p}" opacity="0.2"/>')
        svg.append(f'<circle cx="42" cy="{cy+30}" r="4" fill="{p}" opacity="0.5"/>')
        svg.append(f'<circle cx="158" cy="{cy+30}" r="4" fill="{p}" opacity="0.5"/>')
        svg.append(f'<circle cx="{cx}" cy="{cy-int(archH/2)}" r="5" fill="{p}" opacity="0.4"/>')
        for y in range(cy + 35, cy + 60, 8):
            svg.append(f'<line x1="25" y1="{y}" x2="175" y2="{y}" stroke="{p}" stroke-width="1" opacity="0.12" stroke-dasharray="4,4"/>')

    svg.append('</g></svg>')
    return ''.join(svg)


def _add_type_system(card, agent):
    """Add the new type system fields to any card (Howard or procedural).
    NEVER removes existing fields — only adds new ones alongside them."""
    import sys as _sys
    _sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from rapp_sdk import (
        _derive_types, _derive_stats, _derive_abilities,
        AGENT_TYPES, TYPE_WEAKNESS, TYPE_RESISTANCE, EVOLUTION_STAGES,
        TIER_TO_RARITY, RARITY_LABELS, RARITY_FLOOR,
    )

    agent_name = agent.get("name", card.get("agent_name", ""))
    tier = agent.get("quality_tier", "community")
    category = agent.get("category", "general")
    tags = agent.get("tags", [])
    deps = agent.get("dependencies", [])
    env_vars = agent.get("requires_env", [])
    version_str = agent.get("version", "1.0.0")
    description = agent.get("description", "")

    types = _derive_types(category, tags)
    primary_type = types[0]
    stats = _derive_stats(agent_name, tier, tags, deps, env_vars, version_str, description)
    abilities = _derive_abilities(agent_name, tags, category, tier)
    evo = EVOLUTION_STAGES.get(tier, EVOLUTION_STAGES["community"])

    card["agent_types"] = types
    card["type_colors"] = [AGENT_TYPES[t]["color"] for t in types]
    card["hp"] = stats["hp"]
    card["stats"] = stats
    card["typed_abilities"] = abilities
    card["weakness"] = TYPE_WEAKNESS.get(primary_type, "LOGIC")
    card["weakness_label"] = AGENT_TYPES[card["weakness"]]["label"]
    card["resistance"] = TYPE_RESISTANCE.get(primary_type, "DATA")
    card["resistance_label"] = AGENT_TYPES[card["resistance"]]["label"]
    card["retreat_cost"] = min(4, len(deps))
    card["evolution"] = evo
    card["tier"] = tier
    card["rarity_tier"] = TIER_TO_RARITY.get(tier, "core")
    card["rarity_label"] = RARITY_LABELS.get(card["rarity_tier"], "Core")
    card["floor_pts"] = RARITY_FLOOR.get(card["rarity_tier"], 10)
    card["seed"] = seed_hash(agent_name)

    return card


def generate_card(agent, rng):
    """Generate a full HOLO card for an agent using Howard's schema."""
    name = agent["display_name"]
    desc = agent.get("description", "")
    cat = agent.get("category", "general")
    tags = agent.get("tags", [])
    deps = agent.get("dependencies", [])
    env = agent.get("requires_env", [])
    tier = agent.get("quality_tier", "community")

    # Title
    title = TITLES[int(rng() * len(TITLES))]

    # Subtype
    subtype = SUBTYPES[int(rng() * len(SUBTYPES))]

    # Legendary?
    is_legendary = tier in ("official", "verified") or rng() > 0.88
    type_line = ("Legendary " if is_legendary else "") + "Creature \u2014 Agent " + subtype

    # Rarity based on tier + some variance
    rarity_roll = rng()
    if tier == "official":
        rarity = "mythic"
    elif tier == "verified":
        rarity = "mythic" if rarity_roll > 0.5 else "rare"
    elif tier == "experimental":
        rarity = "uncommon" if rarity_roll > 0.3 else "rare"
    else:
        if rarity_roll > 0.85:
            rarity = "rare"
        elif rarity_roll > 0.5:
            rarity = "uncommon"
        else:
            rarity = "common"

    # Mana cost
    base_pips = CAT_PIPS.get(cat, ["N"])
    generic = int(rng() * 3) + 1
    cost = f"{{{generic}}}"
    num_pips = 1 + int(rng() * min(len(base_pips), 2))
    colors = []
    for i in range(num_pips):
        pip = base_pips[i % len(base_pips)]
        cost += f"{{{pip}}}"
        if pip not in colors:
            colors.append(pip)
    if rng() > 0.7:
        bonus = "WUBRG"[int(rng() * 5)]
        if bonus not in colors:
            cost += f"{{{bonus}}}"
            colors.append(bonus)

    # Power/Toughness — wider range, less clustering
    complexity = len(tags) + len(env) + len(deps)
    tier_bonus = {"official": 3, "verified": 2, "experimental": 0}.get(tier, 1)
    power = 1 + int(rng() * 8) + tier_bonus
    toughness = 1 + int(rng() * 8) + tier_bonus
    # Slight asymmetry — not every card should be N/N
    if rng() > 0.5:
        power = max(1, power + int(rng() * 3) - 1)
    else:
        toughness = max(1, toughness + int(rng() * 3) - 1)

    # Abilities — derive from agent description and tags
    abilities = []
    if desc:
        # Primary ability from description
        kw_pool = ["Execute", "Analyze", "Generate", "Process", "Deploy",
                    "Coordinate", "Assess", "Configure", "Monitor", "Synthesize",
                    "Optimize", "Transform", "Dispatch", "Calibrate", "Intercept"]
        kw = kw_pool[int(rng() * len(kw_pool))]
        abilities.append({"keyword": kw, "cost": "", "text": desc[:200]})

    if env:
        abilities.append({"keyword": "Requires", "cost": "", "text": f"Needs {', '.join(env)} to activate."})

    non_trivial_deps = [d for d in deps if d != "@rapp/basic-agent"]
    if non_trivial_deps:
        abilities.append({"keyword": "Synergy", "cost": "", "text": f"When {', '.join(non_trivial_deps[:3])} are on the field, this agent gains +1/+1."})

    if tags and not non_trivial_deps:
        tag_abilities = {
            "orchestration": {"keyword": "Orchestrate", "cost": "", "text": "Coordinate multiple agents in sequence. Each resolved agent adds +1 to the next."},
            "analytics": {"keyword": "Insight", "cost": "", "text": "When data is processed, reveal the top pattern. Knowledge is power."},
            "automation": {"keyword": "Automate", "cost": "", "text": "At the beginning of each cycle, execute one queued task without prompting."},
            "pipeline": {"keyword": "Pipeline", "cost": "", "text": "Chain outputs to inputs. Each stage refines the result."},
            "search": {"keyword": "Seek", "cost": "", "text": "Search through indexed sources. Return the most relevant match."},
            "compliance": {"keyword": "Enforce", "cost": "", "text": "All outputs must pass validation. Non-compliant results are rejected."},
            "forecast": {"keyword": "Foresight", "cost": "", "text": "Predict the next likely outcome based on historical patterns."},
            "report": {"keyword": "Report", "cost": "", "text": "Compile findings into a structured briefing. Clarity over volume."},
        }
        for tag in tags[:3]:
            tag_lower = tag.lower().replace("-", "")
            for key, ability in tag_abilities.items():
                if key in tag_lower and ability not in abilities:
                    abilities.append(ability)
                    break

    # Flavor text
    flavor = FLAVORS[int(rng() * len(FLAVORS))]

    # Art
    art_svg = gen_holo_art(agent["name"], cat, rng)

    return {
        "name": name,
        "title": title,
        "mana_cost": cost,
        "colors": colors,
        "type_line": type_line,
        "rarity": rarity,
        "power": power,
        "toughness": toughness,
        "abilities": abilities[:3],  # Max 3 abilities like Howard's cards
        "flavor_text": flavor,
        "avatar_svg": art_svg,
        "set_code": "HOLO",
        "artist": "RAPP",
        "agent_name": agent["name"],
    }


def main():
    repo_root = os.path.join(os.path.dirname(__file__), '..')
    registry_path = os.path.join(repo_root, 'registry.json')
    output_path = os.path.join(repo_root, 'cards', 'holo_cards.json')

    with open(registry_path, 'r') as f:
        registry = json.load(f)

    agents = registry.get('agents', [])
    print(f"Generating HOLO cards for {len(agents)} agents...")

    cards = {}
    howard_count = 0
    generated_count = 0

    for agent in agents:
        # Check if this agent matches one of Howard's 13 originals
        slug = ''.join(c for c in (agent.get('display_name', '') or '') if c.isalpha()).lower()

        if slug in HOWARD_DB:
            # Use Howard's original — namespace SVG IDs to avoid conflicts
            card = dict(HOWARD_DB[slug])
            card["agent_name"] = agent["name"]
            uid = format(seed_hash(agent["name"]) & 0xFFFFFF, 'x')
            svg = card.get("avatar_svg", "")
            svg = svg.replace('id="bg"', f'id="bg-{uid}"').replace('url(#bg)', f'url(#bg-{uid})')
            svg = svg.replace('id="glow"', f'id="gl-{uid}"').replace('url(#glow)', f'url(#gl-{uid})')
            card["avatar_svg"] = svg
            # Add type system fields alongside Howard's originals
            _add_type_system(card, agent)
            cards[agent["name"]] = card
            howard_count += 1
        else:
            # Generate a new card using Howard's schema
            rng = mulberry32(seed_hash(agent["name"] + "_holo"))
            card = generate_card(agent, rng)
            # Add type system fields alongside procedural card fields
            _add_type_system(card, agent)
            cards[agent["name"]] = card
            generated_count += 1

    # Write output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(cards, f, separators=(',', ':'))

    size_kb = os.path.getsize(output_path) / 1024
    print(f"Done! {howard_count} Howard originals + {generated_count} generated = {len(cards)} total")
    print(f"Output: {output_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
