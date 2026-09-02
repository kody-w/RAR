---
name: "rar-wildhaven-penumbra"
description: "Returns any input as twin lines \u2014 the surface text plus a whispered heuristic read of what was almost said; no LLM or network calls."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/penumbra_agent", "rar_sha256": "00a2946996be36b9234c3e9cbf916eee70fed319104bff2aef7325e437343a6f", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "penumbra_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@wildhaven/penumbra:8e5f0966bf70785fac912772bf4672bd526c9bb893ccafdc5d5f7f5579070efb", "kind": "skill"}, "version": "1.0.2", "author": "Wildhaven of America", "tags": ["eidolon", "subtext", "legendary", "penumbra", "introspection", "daemon", "caesura"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@wildhaven/penumbra_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `penumbra_agent.py` is
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
