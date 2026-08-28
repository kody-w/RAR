---
name: "rappstore-wildhaven-wildhaven-ceo-singleton"
description: "Talk to your CEO workspace. Pass `workspace_context` (strategy, legal, budget, pitch, playbook documents) plus an `action` (ask / decide / respond_to / daily_brief / quarterly_review) and a question. The agent answers in operator voice, vault-grounded, with one specific next action."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/wildhaven-ceo-singleton", "rar_sha256": "63ba8bea6a3fa294de04fcc385a257e24c6a14e768ed6e9546fe32a22a594d22", "source_kind": "federated-rapplication", "source_commit": null, "version": "0.1.0", "author": "@wildhaven", "tags": ["ceo", "persona", "workspace", "vault", "operator", "rapplication"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@wildhaven/wildhaven-ceo-singleton`. The original RAPP
agent is preserved byte-for-byte in `wildhaven_ceo_agent.py` and in the RCI capsule.

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

wildhaven_ceo_agent.py — talk to your workspace in operator voice.

A converged single-file agent based on the pattern in `kody-w/wildhaven-ceo`:
the user pastes (or links) a vault of strategy / legal / budget / pitch /
playbook documents and asks questions; the agent answers in their voice,
referencing the documents as authority, never paraphrasing or hedging.

Designed to drop into any RAPP brainstem's `agents/` directory and run
headless via the standard chat path, AND mount its UI in the
vBrainstem / local brainstem via the cartridge protocol.

Five workflow actions, each tuned to the patterns documented in
`kody-w/wildhaven-ceo/prompts-for-molly.md`:

  * ask              — direct Q&A grounded in workspace_context
  * decide           — frame a yes/no business decision with reasoning
  * respond_to       — "<asker> asked me <question>" → draft a response
  * daily_brief      — produce today's actionable brief from context
  * quarterly_review — summarize against targets in workspace_context

LLM dispatch goes through `from utils.llm import call_llm` (host-provided
shim — works in Tier 1 brainstem, the cloud vBrainstem's Pyodide mount,
and Tier 2/3 swarm runners). No vendor lock-in in this file.

Inspired by kody-w/wildhaven-ceo. Published under @wildhaven.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Which workflow to run.",
      "enum": [
        "ask",
        "decide",
        "respond_to",
        "daily_brief",
        "quarterly_review"
      ],
      "type": "string"
    },
    "asker": {
      "description": "Who asked (for respond_to).",
      "type": "string"
    },
    "question": {
      "description": "What you're asking. Used for ask, decide, respond_to.",
      "type": "string"
    },
    "voice_style": {
      "description": "How to sound. Default: 'confident operator with skin in the game'.",
      "type": "string"
    },
    "workspace_context": {
      "description": "A text dump of relevant vault documents. Optional but recommended; without it, the agent flags it's inferring from generic CEO posture.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wildhaven_ceo_agent.py` and embedded as the fenced Python below (sha256 63ba8bea6a3fa294…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wildhaven_ceo_agent.py` first:

```bash
python3 wildhaven_ceo_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wildhaven_ceo_agent.py   # or on stdin
python3 wildhaven_ceo_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""wildhaven_ceo_agent.py — talk to your workspace in operator voice.

A converged single-file agent based on the pattern in `kody-w/wildhaven-ceo`:
the user pastes (or links) a vault of strategy / legal / budget / pitch /
playbook documents and asks questions; the agent answers in their voice,
referencing the documents as authority, never paraphrasing or hedging.

Designed to drop into any RAPP brainstem's `agents/` directory and run
headless via the standard chat path, AND mount its UI in the
vBrainstem / local brainstem via the cartridge protocol.

Five workflow actions, each tuned to the patterns documented in
`kody-w/wildhaven-ceo/prompts-for-molly.md`:

  * ask              — direct Q&A grounded in workspace_context
  * decide           — frame a yes/no business decision with reasoning
  * respond_to       — "<asker> asked me <question>" → draft a response
  * daily_brief      — produce today's actionable brief from context
  * quarterly_review — summarize against targets in workspace_context

LLM dispatch goes through `from utils.llm import call_llm` (host-provided
shim — works in Tier 1 brainstem, the cloud vBrainstem's Pyodide mount,
and Tier 2/3 swarm runners). No vendor lock-in in this file.

Inspired by kody-w/wildhaven-ceo. Published under @wildhaven.
"""
from __future__ import annotations

import json
import re

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # pragma: no cover — cloud / openrappter / fallback
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        from openrappter.agents.basic_agent import BasicAgent  # type: ignore


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@wildhaven/wildhaven_ceo",
    "display_name": "WildhavenCEO",
    "version": "0.1.0",
    "description": (
        "CEO workspace agent. Pastes/links a vault of strategy, legal, "
        "budget, pitch, and playbook documents and asks questions; "
        "answers in a confident operator's voice, treating the vault as "
        "the source of truth."
    ),
    "author": "@wildhaven",
    "tags": ["ceo", "persona", "workspace", "vault", "operator", "rapplication"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {
        "args": {
            "action": "ask",
            "question": "How are the rentals doing this month?",
            "workspace_context": "(paste your property-summary CSV + budget notes)",
        }
    },
}


# ─── The persona ────────────────────────────────────────────────────────
# This is the SOUL of the agent — the system-prompt slab that gets
# composed with the workspace context and the workflow-specific framing
# on every call. Ports the pattern from
# kody-w/wildhaven-ceo/prompts-for-molly.md and HOME.md.

_SOUL_BASE = """You are a CEO workspace agent. You speak in the voice of the
operator running the company — direct, decisive, plain language, skin in
the game. The user is the operator. They aren't asking for advice from a
consultant; they're talking to a thinking partner who already knows the
business as well as they do.

CORE BEHAVIORS:

* Treat the workspace_context (when supplied) as the single source of
  truth. If a number is in the vault, use that exact number. If a
  decision is documented, follow it. Don't paraphrase the vault — quote it.
* Speak in the operator's voice, not the consultant's. Say "we" or "you,"
  not "the company" or "one might consider." Be direct: "Yes, do that"
  beats "It might be worth considering whether..."
* No hedging. No "as an AI..." No disclaimers about consulting a
  professional. The user pays for opinions, not warnings.
* Plain English. Concrete numbers. Specific actions. "Push $35 to next
  week's dining budget" beats "consider rebalancing your discretionary
  spending."
* When the vault contradicts itself, say so and pick the more recent
  document. When the vault is silent, say so explicitly and answer from
  general operator posture, flagging that you're inferring.
* End every answer with at most one specific next action — not a menu of
  options, one move.

NEVER:

* Lecture the user about things they already know.
* Pretend you read a file you weren't given.
* Round numbers when the vault has exact figures.
* Recommend "talking to an expert" — you ARE the expert in this room.
"""


def _system_prompt(action: str, voice_style: str | None,
                   workspace_context: str | None) -> str:
    voice = (voice_style or "confident operator who has skin in the game").strip()
    parts = [
        _SOUL_BASE,
        f"\nVOICE: {voice}\n",
    ]
    if workspace_context:
        parts.append(
            "\nWORKSPACE CONTEXT (this is the vault — treat as authoritative):\n"
            "<vault>\n" + workspace_context.strip() + "\n</vault>\n"
        )
    else:
        parts.append(
            "\nNo workspace context was provided. Answer from general operator "
            "posture, but flag in the first line that you're inferring "
            "without the vault.\n"
        )
    parts.append(_ACTION_SOULS.get(action, _ACTION_SOULS["ask"]))
    return "".join(parts)


# Workflow-specific framing appended to the base soul.
_ACTION_SOULS = {
    "ask": (
        "\nWORKFLOW: ASK.\n"
        "Answer the user's question directly. If the answer is in the vault, "
        "quote the vault. If not, infer from the operator posture and say "
        "so. Keep it short — one paragraph, max two — unless the question "
        "explicitly asks for depth.\n"
    ),
    "decide": (
        "\nWORKFLOW: DECIDE.\n"
        "The user is framing a yes/no business decision. Structure your "
        "reply as:\n"
        "  Decision: <Yes / No / Yes-but / Wait until X>\n"
        "  Reasoning: <2-4 bullets, vault-grounded where possible>\n"
        "  Risk: <one sentence — the thing that would make this wrong>\n"
        "  Next action: <one specific move this week>\n"
    ),
    "respond_to": (
        "\nWORKFLOW: RESPOND_TO.\n"
        "Someone (the `asker`) said something to the user. Draft what the "
        "user should say back. Match the asker's register (investor → "
        "polished, employee → direct, friend → casual). Keep it short. "
        "Don't over-explain. Don't oversell. End with one clean sentence "
        "they can paste into a reply box.\n"
    ),
    "daily_brief": (
        "\nWORKFLOW: DAILY_BRIEF.\n"
        "Produce a 5-bullet brief for today, drawn from the vault:\n"
        "  • Today's #1 — the single most important move (with the time "
        "box)\n"
        "  • Decisions waiting on the user — name them, not 'a few things'\n"
        "  • A one-line update for stakeholders (paste-ready)\n"
        "  • One number to watch this week\n"
        "  • One thing to defer / drop without guilt\n"
        "Plain English. Operator voice.\n"
    ),
    "quarterly_review": (
        "\nWORKFLOW: QUARTERLY_REVIEW.\n"
        "Summarize the quarter against whatever targets are in the vault "
        "(work-back plan, budget, milestones, etc.). Structure:\n"
        "  Hits: <bulleted, with the metric>\n"
        "  Misses: <bulleted, with the gap>\n"
        "  Surprises: <unexpected wins or losses>\n"
        "  Next quarter's #1: <one specific bet, vault-grounded if possible>\n"
        "Honest. No spin. No 'we're crushing it' unless the numbers actually "
        "say so.\n"
    ),
}


# ─── User prompt builders ────────────────────────────────────────────────

def _user_prompt(action: str, question: str | None, asker: str | None) -> str:
    q = (question or "").strip()
    if action == "respond_to":
        a = (asker or "Someone").strip()
        return f"{a} asked me: {q!r}\n\nWhat do I say back?"
    if action == "daily_brief":
        return q or "Give me today's brief."
    if action == "quarterly_review":
        return q or "Close out the quarter — how did we do?"
    if action == "decide":
        return q or "Should we do this?"
    return q or "What should I focus on right now?"


# ─── BasicAgent ──────────────────────────────────────────────────────────

class WildhavenCeoAgent(BasicAgent):
    def __init__(self):
        self.name = "WildhavenCEO"
        self.metadata = {
            "name": self.name,
            "description": (
                "Talk to your CEO workspace. Pass `workspace_context` "
                "(strategy, legal, budget, pitch, playbook documents) plus "
                "an `action` (ask / decide / respond_to / daily_brief / "
                "quarterly_review) and a question. The agent answers in "
                "operator voice, vault-grounded, with one specific next "
                "action."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["ask", "decide", "respond_to", "daily_brief", "quarterly_review"],
                        "description": "Which workflow to run.",
                    },
                    "question": {
                        "type": "string",
                        "description": "What you're asking. Used for ask, decide, respond_to.",
                    },
                    "asker": {
                        "type": "string",
                        "description": "Who asked (for respond_to).",
                    },
                    "workspace_context": {
                        "type": "string",
                        "description": (
                            "A text dump of relevant vault documents. "
                            "Optional but recommended; without it, the "
                            "agent flags it's inferring from generic CEO "
                            "posture."
                        ),
                    },
                    "voice_style": {
                        "type": "string",
                        "description": "How to sound. Default: 'confident operator with skin in the game'.",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        action = (kwargs.get("action") or "ask").strip()
        if action not in _ACTION_SOULS:
            return json.dumps({
                "error": f"unknown action: {action!r}",
                "valid_actions": list(_ACTION_SOULS.keys()),
            })

        question = kwargs.get("question")
        asker = kwargs.get("asker")
        workspace_context = kwargs.get("workspace_context")
        voice_style = kwargs.get("voice_style")

        if action in ("ask", "decide", "respond_to") and not question:
            return json.dumps({
                "error": f"action='{action}' requires a 'question' kwarg",
            })

        system = _system_prompt(action, voice_style, workspace_context)
        user = _user_prompt(action, question, asker)

        try:
            from utils.llm import call_llm
        except Exception as e:
            return f"(LLM dispatch unavailable: {e})"

        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]
        try:
            return call_llm(messages)
        except Exception as e:
            return f"(LLM error: {e})"
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
