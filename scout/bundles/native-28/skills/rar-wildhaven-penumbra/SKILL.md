---
name: "rar-wildhaven-penumbra"
description: "Returns any input as twin lines \u2014 the surface text plus a whispered heuristic read of what was almost said; no LLM or network calls."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/penumbra_agent", "rar_sha256": "00a2946996be36b9234c3e9cbf916eee70fed319104bff2aef7325e437343a6f", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "Wildhaven of America", "tags": ["eidolon", "subtext", "legendary", "penumbra", "introspection", "daemon", "caesura"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@wildhaven/penumbra_agent`. The original RAPP
agent is preserved byte-for-byte in `penumbra_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `penumbra_agent.py` and embedded as the fenced Python below (sha256 00a2946996be36b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `penumbra_agent.py` first:

```bash
python3 penumbra_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 penumbra_agent.py   # or on stdin
python3 penumbra_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
    "version": "1.0.2",
    "display_name": "Penumbra",
    "description": (
        "Returns any input as twin lines \u2014 the surface text plus a whispered heuristic read of what was almost said; no LLM or network calls."
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
