---
name: "rar-wildhaven-penumbra"
description: "Returns any input as twin lines \u2014 the surface text plus a whispered heuristic read of what was almost said; no LLM or network calls."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/penumbra_agent", "rar_sha256": "a990cbad0828c87f1881328a1a2035676d4ee81c4cffac9df081a30946e776b9", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.2", "author": "Wildhaven of America", "tags": ["eidolon", "subtext", "legendary", "penumbra", "introspection", "daemon", "caesura"]}
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
