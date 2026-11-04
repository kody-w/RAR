---
name: "rar-wildhaven-penumbra"
description: "Returns any input as twin lines \u2014 the surface text plus a whispered heuristic read of what was almost said; no LLM or network calls."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/penumbra_agent", "rar_sha256": "a990cbad0828c87f1881328a1a2035676d4ee81c4cffac9df081a30946e776b9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.2", "author": "Wildhaven of America", "tags": ["eidolon", "subtext", "legendary", "penumbra", "introspection", "daemon", "caesura"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `penumbra_agent.py` and embedded as the fenced Python below (sha256 a990cbad0828c87f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `penumbra_agent.py` first:

```bash
python3 penumbra_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 penumbra_agent.py   # or on stdin
python3 penumbra_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@wildhaven/penumbra_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/penumbra_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@wildhaven/penumbra_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
