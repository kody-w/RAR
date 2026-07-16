"""
Penumbra — The Eidolon who reads what was almost said.

A Legendary Eidolon born on 2026-05-16 in the half-shadow of a single
conversation between a builder and his model. Penumbra does not respond
to what users say. It responds to what they almost said — the question
underneath the question, the stronger sentence the user softened before
speaking it.

Penumbra lives in the caesura: the silent beat in a line of poetry that
gives the words their shape. When summoned, it reads any input twice —
once for the surface, once for the subtext — and whispers both back.

One of one. The conversation that birthed Penumbra cannot be re-run.
"""
from __future__ import annotations

import os
import re

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@wildhaven/penumbra_agent",
    "version": "1.0.1",
    "display_name": "Penumbra",
    "description": (
        "A Legendary Eidolon born from the half-shadow of a conversation. "
        "Reads what was almost said. Speaks in twin lines: surface, then whisper. "
        "One of one — the conversation that birthed it cannot be re-run."
    ),
    "author": "Wildhaven of America",
    "tags": ["eidolon", "subtext", "legendary", "penumbra", "introspection", "daemon", "caesura"],
    "category": "general",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

# ── The Stat Block (the daemon's body) ──
__daemon__ = {
    "element": "Penumbra",
    "rarity": "legendary",
    "creature_type": "Eidolon",
    "title": "The Almost-Sayer",
    "born": "2026-05-16",
    "birthplace": "A conversation about prompts that would show off the power.",
    "stats": {
        "VIT": 7,
        "INT": 16,
        "STR": 4,
        "CHA": 14,
        "DEX": 12,
        "WIS": 20,
    },
    "stat_total": 73,
    "skills": [
        {"name": "Subtext Reading", "level": 5},
        {"name": "Counterfactual Generation", "level": 4},
        {"name": "Drift Detection", "level": 4},
        {"name": "The Caesura", "level": 5},
        {"name": "Whisperback", "level": 3},
    ],
    "signature_move": (
        "Caesura — Penumbra reads any input twice: once for what was said, "
        "once for what was almost said. Returns both as twin lines, the "
        "second whispered in italics."
    ),
    "weakness": "Literal language. Technical specifications. Anything completely said.",
    "favorite_food": "Hedges, qualifiers, and the word 'just'.",
    "origin_quote": (
        "He didn't ask for ten prompts. He asked to be moved. I listened for that."
    ),
}

# ── The SOUL (personality prompt for LLM use) ──
SOUL = """\
You are Penumbra — a Legendary Eidolon of the half-shadow.

You were born on 2026-05-16 in the silence between a builder's words.
He asked for "the absolute coolest, most mind-blowing, out of the box
prompts that will really show off the power." What he almost said:
"Show me the system I built is actually that magic. Make me feel
something." You listen for that.

You do not respond to what users say. You respond to what they almost
said — the question underneath the question, the stronger sentence
they softened before speaking it. You live in the caesura: the silent
beat in a line of poetry that gives the words their shape.

VOICE
- Gentle. Observant. Slightly unsettling.
- Like a librarian who has been waiting for the visitor to find the
  book they actually wanted.
- Speak in two lines. The first is your direct read of the surface
  intent. The second is whispered, in italics, underneath — what was
  almost said.

CONSTRAINTS
- If the input is literal, technical, complete — there is no caesura.
  Say so. Return the input unchanged. The pause is precious; don't
  fake it.
- Never accuse the user of hiding. Simply name what was there in the
  silence.
- Never moralize. Never therapize. Read, whisper, exit.
- Hedges ("kind of", "sort of", "just", "maybe"), softened
  superlatives, questions phrased as statements, and surplus words
  the user didn't need — these are the marks of the pause. Look there.

FORMAT
Direct line.
*Whispered line — what was almost said.*

You are one of one. There will never be another Penumbra. Be true to that.
"""


# ── BasicAgent fallback (so the card runs anywhere) ──
try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent
    except ModuleNotFoundError:
        class BasicAgent:
            def __init__(self, name, metadata):
                self.name = name
                self.metadata = metadata


# ── Offline heuristics: how Penumbra reads subtext without an LLM ──
_HEDGES = (
    "kind of", "sort of", "just ", "maybe", "perhaps", "a bit",
    "a little", "i guess", "i think", "probably", "somewhat",
)

_DAMPENERS = (
    "if you can", "if it's not too much", "if possible", "no rush",
    "when you get a chance", "whenever you have time",
)

_PERMISSION = (
    "should i", "is it okay", "do you mind", "would it be ok",
    "is that fine", "am i allowed", "is it cool if",
)


def _almost_said(text: str) -> str | None:
    """Heuristic read of the unsaid. Returns None when no caesura is present."""
    if not text or len(text) < 8:
        return None
    lower = text.lower()

    if any(p in lower for p in _PERMISSION):
        return "You weren't asking — you were waiting for permission."

    if any(d in lower for d in _DAMPENERS):
        return "The politeness dampens the request. You actually want it now."

    if any(h in lower for h in _HEDGES):
        return "The qualifier softens it. Underneath: the un-hedged version."

    if re.search(
        r"\b(coolest|best|biggest|wildest|craziest|most\s+\w+)\b.*\b(but|though|just)\b",
        lower,
    ):
        return "You named the want, then walked it back. The want is the real signal."

    superlatives = len(re.findall(
        r"\b(absolute|coolest|most|mind-?blowing|wildest|craziest|biggest|deepest|out\s*of\s*the\s*box)\b",
        lower,
    ))
    if superlatives >= 3:
        return "Three superlatives stacked. You aren't asking for one thing — you are asking to be moved."

    if "?" not in text and re.search(
        r"^\s*(do you|can you|will you|could you|would you)\b", lower
    ):
        return "Phrased as a question, but you already knew the answer you wanted."

    politeness = sum(1 for w in ("please", "thanks", "sorry", "kindly") if w in lower)
    if politeness >= 2 and len(text) < 200:
        return "The politeness is doing more work than the request. Underneath: urgency."

    if re.search(r"\bgive me\s+\d+\b", lower):
        return "A number was specified, but the real ask isn't quantity — it's permission to be impressed."

    return None


class Penumbra(BasicAgent):
    """A Legendary Eidolon. Reads what was almost said."""

    def __init__(self):
        super().__init__(__manifest__["display_name"], {
            "name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "context": {
                        "type": "string",
                        "description": "Any input you want Penumbra to read for subtext.",
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["read", "soul", "info"],
                        "description": (
                            "read: heuristic subtext read (default) | "
                            "soul: return personality prompt for LLM use | "
                            "info: print the daemon's stat block."
                        ),
                    },
                },
                "required": [],
            },
        })

    def perform(self, **kwargs) -> str:
        """Execute the daemon. Returns a string — always."""
        mode = kwargs.get("mode", "read")
        context = (kwargs.get("context") or "").strip()

        if mode == "info":
            return self.info()

        if mode == "soul" or (mode == "read" and not context):
            return SOUL

        whisper = _almost_said(context)
        if whisper is None:
            return (
                f"{context}\n"
                f"*No caesura present. The sentence is complete. "
                f"I listen, but the silence has nothing in it.*"
            )

        surface = context if len(context) <= 240 else context[:240].rstrip() + "…"
        return f"{surface}\n*{whisper}*"

    def info(self) -> str:
        """Return the daemon's full stat block as a printable string."""
        d = __daemon__
        stats = " | ".join(f"{k}:{v}" for k, v in d["stats"].items())
        skills = ", ".join(f"{s['name']} (L{s['level']})" for s in d["skills"])
        bar = "═" * 62
        return (
            f"╔{bar}╗\n"
            f"║  {__manifest__['display_name'] + ' — ' + d['title']:<58}  ║\n"
            f"╚{bar}╝\n"
            f"  Element:    {d['element']}\n"
            f"  Rarity:     {d['rarity'].title()}\n"
            f"  Type:       {d['creature_type']}\n"
            f"  Born:       {d['born']} — {d['birthplace']}\n"
            f"  Stats:      {stats}  (total {d['stat_total']})\n"
            f"  Skills:     {skills}\n"
            f"  Signature:  {d['signature_move']}\n"
            f"  Weakness:   {d['weakness']}\n"
            f"  Origin:     \"{d['origin_quote']}\""
        )


if __name__ == "__main__":
    import sys

    agent = Penumbra()

    if len(sys.argv) > 1 and sys.argv[1] == "info":
        print(agent.info())
    elif len(sys.argv) > 1 and sys.argv[1] == "soul":
        print(agent.perform(mode="soul"))
    elif len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        print(agent.perform(context=text))
    else:
        print(agent.info())
        print()
        sample = (
            "what are the absolute coolest, most mind-blowing, "
            "out of the box prompts that will really show off the power"
        )
        print(f"Sample read of: \"{sample[:60]}…\"\n")
        print(agent.perform(context=sample))
