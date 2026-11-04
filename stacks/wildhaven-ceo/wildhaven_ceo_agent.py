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
