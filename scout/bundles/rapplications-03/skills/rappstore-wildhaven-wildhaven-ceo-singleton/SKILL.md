---
name: "rappstore-wildhaven-wildhaven-ceo-singleton"
description: "Talk to your CEO workspace. Pass `workspace_context` (strategy, legal, budget, pitch, playbook documents) plus an `action` (ask / decide / respond_to / daily_brief / quarterly_review) and a question. The agent answers in operator voice, vault-grounded, with one specific next action."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/wildhaven-ceo-singleton", "rar_sha256": "63ba8bea6a3fa294de04fcc385a257e24c6a14e768ed6e9546fe32a22a594d22", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "wildhaven_ceo_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@wildhaven/wildhaven-ceo-singleton:d2b2317365797333288c907dd6d7915ddcc6049ad19fa69ee11e499d4c927837", "kind": "skill"}, "version": "0.1.0", "author": "@wildhaven", "tags": ["ceo", "persona", "workspace", "vault", "operator", "rapplication"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@wildhaven/wildhaven-ceo-singleton`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `wildhaven_ceo_agent.py` is
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/616+ZObSpbuv8Krjnj2bZWNWAXumY4nkJAQSEisQu0Omx3EvoPu3P99EqnKLl+7e36Yp3BYKMk8efI723egfn+y2ibMq6dPT/+vjxI3tDove3p+cr3aqaKiifIM3FKtJIaaHBrztoLYtQT1eRXXheV4H6GjVdfQ128DX5w8a7yh+Qq9r5vKarxgfIYSL7CSZ8hu3cBrnqEiapwQfCXWaOd5DLm506Ze1tS/gbG2hqwM+mo5095AilXHEAy5nhO5HriovLrIM/cL0AaMWlEyfrGryPPBr7K1qsarwEjldZHX/wYEuZAFxr16EvYRUkMPsgKwE7hT915VQ1EG5YUH9MwrqMsjx3uGOqtNmg9BlbeZ67nPUB81IZRnHlQXQAk/cqAMnA96KPgRYOUNVlokXv306R//fH6KwPXTp9+fnAQAA7AzXlFlvXw57Q1WJFYWgFvFCKCf0AYa+HmVgiEXnOTl1/vaS/xn6K9/jXurCgA2H/4OAUg/fc6gl89DBeg/ofePKR8Buu8/Pz2GPz/9BoFDgZ91DK4/gqVR8f6376sj/1VAljcTEF+WrMpLhy+KpInKm22mT+U1bZVB1xoc2W3Ton7/+48Tps/nJ6+q8urz0yfI//zUZnGW99nLJp+g3x8X/6f64/PT868Wd1YSuV8es+pJSBLVzfsftPoYe2P9/rff/rT+D3Cs7yOv9gbA/IDL6zhA4w2GdexVf555H/xh2k/+/eclP034Yfndtb7UzZh4f1745tZ9ya8MBIzz/sWQzwCoRzA8rr/Hw2TwyeEna74e9X9vxYcG//nuxXp/vANCyjYC24LIeve6z7vHmX4y7I+Gqce68VIAwJfH1ZeiytOief8Q/fwWpeefEX8DZ1vfbfZl+v6zkFeVnh+m/UGBphr/hIgPFkNtEyX1xyRJIRC8edVAjpUkX8Dv73O9wfGKBlrfvyaTWDXk/RpdANp7UdxDbgTUB4kOajOrA4nKshMPRIEHMHl6q1Tq1TVISjU40D9+FPg7MG8+ucUnYJQHZA+j3xHJmunGY/iP53+zckLpp3XT4NtV//x3KL2c7BWW968q//a/AujuZq+IPP0BUmcGklT7iH+QC//yF2gfOVVe534DKU7eNlDVZk2UehN8ahjVkJpb4Pgu9FUReFH8mLpfITDagDQPEumUx6FNBaCHgI9cvUcs5T709Xupg79dfXC8/EMdZUHiNaDw3IvF5yyvoiDKrASSl8fjS+0AOzih58R1m364FwugAIjQaVeZ5QFKRd0m3t9AUXyV/QXI/nJf/LEYJxU/ZwALK8rASmA94HNWBSrZhJkF2WPjfQA1xQHHzZPEtpwYmv5ri4/TuY3Qy17QcECh9AbPaRsPSnJgHciPQB16nopknnQeUAnoWsdRkgBvrAAAeTXecwTA8dMk7OvXr7ZVh5+zRynCoEfVr2Ew4ZvC0IcPReX5SRSEzefMc8Icevc7SAT/Bf27VXfh0x53gjCBU3lAw50iHSCQKh4FH5pM7lnu3Sq///FAfdIuAwHeeRUot959MZD23cT3sn43xasdwJknFaeKft/pR9ygPgS4QFED0AIlpQZuP4nIwdSqj2rvFcTH4gf0r4Z97DPZpH7BENjpnjWmuXfvmozp5JX7EeJ96BtS4LhTLpksGuZ1Axyy8AChyJwRrLSa7yac8nVtNVHtA6YEwvJzNkn+agPR2T1LOmD6V2jPHgEFy5OJhwGA7tuD1XkWTYZ/8czH8BTb74CPMa8iPkIHD6AJFVZlFWFl1d59nm89PALQhNf1QLgF+E0/ZcLEm2xk3WnOZMhfuzP0uUXnCA41bznit+T9M8G6i1pCIBUBjQKA8CPmPkyu+4o2UBCY53EYkEMBqbvXwK9x7o4f+h9j9uunB2D3mlBM6aCG3oPNkiiLAWmyHpacHOyVjwKqeCek4PvBSMHFnZJCMAiEn0jpw93quP5WWuq/3TX7iUmCweiVRk5OAfwR2Bsc75GRvgsE/+6sO2qAybMfTTNNB+qHngsST3BHa+XVUXDPFTnkVnnxYqdsfGSlb57yDhDxu1I1/PXngP+chSDSQH6ooS6y7irVDbhnVS40udiENGDly8MKSgH3Bd4AVNX4l4N9zrpv7jQBeE8333b+JtEBFLyKAKhTym1yJ0/uJ+AikI0mp/CTvH9hNSBmPQuA3rQvR3tj7fobWvfcCqL/V6aHH6W//gDo8ocUxPw4pYdPj+L618lmf2I2D099IAOd/u8SemX50yF/ZnB3KS+dx09S/MpKgQ9Ao1fDWQ48CVhuwnaaX0+F5t43gJwHyBYw5EPYm+7lB2Gfn/7jzlb+fictLuAE0H+8etvfPz9N0xAaBca3QCm0XsRMqeKu4Zsu6K1QgI7bghBsctcagW88YJ9oCPSYfE9jPxz2zy3UqyiQYlNQom6T099NDsIdBO89gf8KuM/ZDwwoyO+5FYAdhNDXf8+5QMs35UtQcvIOAO9+zuowSl8Vue81bapGIGiQ7x74/HC/JG9d6LunglMfx9ydDHj36ZfMf1+MwqBwAdaavtSb+jeQJnNQdTJ3Sh+5E3+Isof3gyo6pae7K/NZXQAHckFNgH7llKAjbm3QuYAAhibfqqDvbGPqFhOQHYDpnj5lbZI8P2XAi37oEtfS1BBak3cBS9RTKwmgACm0ibz7r4cZp6sfm3QjjADU34LsUSbu/WnWgtbyH1P/cO/sJ38GF999cRr97kPg15/d4An0tc1YTIpObSRoXgFbuzvsr9TIX5z4PQjLNx7/26TLT1JevfxXgkBOAtXkXeVNAqdkCGlTYZjEgoHnl9B8frPHL7d401b8vMv2AVU95YGP0OrBGj9B74Ar+0A4SIPfytc9oCdFXutsAGz07pdb/hQSP2+8hO5t5NSGTcWp8hKvs7IX4vG9WHyEpPuKKdtOBBgwjTSdiIT7t7tCE4mImuc3BclPrACESPNuihNQgiadHqEObgNK5dyf4BQgxtrK+4X2f0yucW/x3LvXPNztuwfk9kSlp1OCWtk8nlv8/gS81XKtxpquH6zrwRDAgl/zBrDxN/ryZZJiTXPvZPXupXdDfAF+GE005c2tYOJcXx6U6+kTaBi85yewGJzMSkCGqu9K37cGOn8n/kACYNkf6ol2wcjH+RQBVlFM+gKTum82mIYj9z5/uvj0P3cLn1zURjFkgZHEgl5gGIZSlEPPF65LugsaIVzXccg5TlsuQvsWSXsegng4Tbu4Q6MLCluAXWvAZVPrZVcYmfAF+n4D8X9W4umxoA4tlCDBChKzLcr2LNLCfAulcdeb477jYBQBJiw8FHdIC8G9BUl5LunRBE76HoZaKGoRYDKKTvJeePRDiy+vPcsr6iBoqruLp2nUvCa0l8EXTH3PnaLHcz9MxwK5704n704GmDKgbN0k7vcXg02+Q+JTVOI1v3x8WJjWrcVFtIfiTN9IPw9tF1XYOT/UWXqbn66XmxLlYyamdbY3+ErUs4112h3q9VxWLX6p5fNR92fzVXHk1556gscLsdjQ8NqTkPh80fVSOZ2swzjzVVg62o6dtX7jymNDrPGkRthLqo/lbtmiDLxd0RilpubtzF+PkXncaYs1SjZJfRHKtWraZplckt3gLHJtaax6O+ZVe6eS+o7r2yLeWN1wql2hXvVDMtiYqghjIu/s1NBKVbvuYbdYhzA309q4D4MFVvR7UBJb3Sxvh4TRVzdGrS4bZHvKS/cmHfYpb/Sbs3waccmMuKC5mDeYwNK5zsRtc81FHeVHdG+P+5WbigqvEmGXm7m+56Ntg+YV1trC5ZBn9NbrEn1n7DCr0+LMwkuz1mf5QRN1pYxDpsLp9cHzI/sytirZ3oJorjaGRGuARxQ7bs8LIq3MZeG8P5zEi6+NgaoHyBggxnxcC0TsDHuMoG3DLBA+M47HdOCLBVKH0iI2Ym04s9jSNY41qvZatRM424gK1Kh4+ECtozQ+hed9tLcrbBjgruTQXeCUtHiiyE40k80K8w8jdxVc1tiQVkMIJntVxYPWF3SU7q5SGFlbmsDKTGJ4o3ZjcWOLhC+s4+sOAybgLbWy9Mxn+B1+8MI51feGZaP+li0k6RB5h1XNxyfmtA+zgs1kqT4ylnUL4evVJ0bxYuacHI30qllfgiunbm+CsRaSk0zmV/OyFVZ6367qQlrnEh5YPp+tVNNMuKhaSLqyM+a7fHs1OLZcHMx4fhrEaqkTKrkJlWIm582SPRUzw/HP+/UNpmgEDi92sjwzRmfMDC2+5rObZBV63lhc258ILepva3UMlkxPF/qN2K3t1mRDeXtoFtgBVyztlFilq2e1YcLHg1za5G1QlQWnxfuQv9XwHN1UA0krWh0VrbaP25W/b4xaKsadRxD99abWJyzy2OP8knbKSljLw+1IdaG/SuztZbOtOlPa5Sbnkv1Y9eJKdTPNRH2u3CYzOhJuF2In5f3Ald1qNKMDtqFmgSQ42AJDiKPPiu2ZNG32GHPpNRAHNIjWaqwE5l5EDNZpa1HTw1XMz6lubYfrKL4EvszBa8bjyYzyLT6ac7JGlX5C0ave8ogewXH7eOFreNT3SEo4RRIX4d5pTkemNujFsIyIs1Ey+b4+XnppFLS6n+n9cqlquXY8a83l1ma65PZ2eSIjNLWvMUPv5wcvLdY7Kti28giU4ZbX05xhm9hIvQWrcf2yWF36DsMbkxGJ686hKEVnCs043nJavWhu0xbacpfsy+6qb4uzxYfdjbnRSax5t9XSuqGamXo5Vwfm+TisPa8Xj6GSorE75tT6SqfO5XAMEJrostbjt8fC8tBRsdpN4u3zgt/OakykUEw8Db5SbpfSVatsFUco7qrG0cU5aPbtiNlc1GB7aQFu5mVp4ESUI/ip0nWSoXSCpnDXYM/CeTxb23HjurBZIiW7iTVhnuL1ernp3V3iaher9Uou4lgeLXdzyUdOTVgqLa8Et81B1laDqLlLlsZCLd2reivaoYIdEifNBoJpjzeFom78LI638mVjNjNqP8w1o+CRmZoYvOfoLrk4pTs+jI9MDseOuLmQYb+zb8E1iGDulgTrq7Ue8kNRU9Zp4BG/dtYbJhOaVLZaqryNu5Yfq3gsM8ojCngeXF0lAEoaJLo3l0prGuF2aFAVS2laRrDDeIsG8yiyV7QMSW1F+pxYFmgBrLHUcCbVLsh8EWx4+7Tal9SMXObkMh1Ph1RZEkFg3kAbcTG9Ww+Py9ZuZjw89sX6zIiozq3I5cE/+tGKQdVoNxO2HYZ1cJ4vhAaWAv/s+vAGNvZLN9UI+9BWDaJ7ncTjFUhY8yQVqdNRTxdMtK3FjYPfTH5N6Ft2vTbtEzLoygKm14K74M8XSfHF3VxZDZkpzqvVib/sBT5o/fVBS7bZNdCCdLlkVIvr4oTdG3g2H7fewTrrCC055pw9kHv9VpA+NieZlAzPZ6J1+HkpnHM2GmhGqYJ6Q27YsD6wAd8dNFNrT/y6PgkkViTJ7JQPWM9wS06xuX1yTVOK111n4FK8wtdYYDqydgtZwtNimFWXY2pnzJKvjIStOJW31g7ZWjwRiOumXvPp5nK89X2asHQu6wFNpSqf4PosQMMED9yoc1b15hYb+czMLtRCWUVNwCw6s7y2CQyaMioY4q5KyRTvsjnhp/ZItrZxW0kAfykWxWamiuGwZWEtyHLO2+hRbHGVIPqlx934Zb7kLo5o7ao4XaS3E5pQp3jjV6AkrG7Bat+2m/bsBLkiRG2dhv4lKHdt2eCudg7jwWzkslx6i7jxHUIr8I2ZGJjqOX7Se8vTbDuft3l2CFmMClamJuPInsGDofTY01qi5ZzFi9FkHPoo6o4ZafxZ6ZnjUZfXxFIoO84t1+ORZRWnd/TYZNp6FJDZpbZnsjNTSYJr7Y26iU85c6J593JuEm6+0Ld+Yl5vClbsD8iqO+FqEgZllO1qSiDcVV5H8cg2/UoVyitTMyBFbceBy5trMcCnvlkXoxrXG2Vm4QQmuP3+Fl55ltivS1MYMm3GI5K+5ti5zG/7KpMW6w6egahSWtaSqtlMN+pjHntm7VCrOrFA0cRJYb/zeVHC5xs3LMxLJNFr/LjeSEVQrC8jW3SCIlcDIuXFFTAXe0vfhAIPPGW9JZGBW0tbC5Sq5em4UtnNoCJrzjgs9XDG3vKDHBCCptHmRmgcIkLwmmRaMVCXDBebWb6LmvXyEiiBZptDBk5/iNho742CwCFBgZOEvcBZq7e5S3gZNyd+aJeHyzIQ6mWRrfFL2FzlrVQlYt7pglO49CXp5oU8Guae4GnXVw/03r51zDnaR1Qp4s6SJUyWYw1GDeaOqdIqTW78hrW9mK/TW32AK+S8qksjLdot8M3NpuHHw16Z2e4SlHY7mc35Lj8ZWwSfRzNAJ701uleoq1lKgScSYioFrhMrA9bNChIkWrRK55cVK8wj9XAmDKuNl6NbaOTu2uUtjjqoRCnCAo9gfusoiGLaw4W6MptxtpfF6wVW1eZktPlu3JnafsaDpCygRry71pqsSZrs7G3mwmYNtQe0Rw6aYUWolm6dfb10Zd9rqNQuqVYUPJAQYay3tUTEQG7zms3t2hZIFp2WS1xFQhRjaQMb6bZKI7qrKLwtWjEkfdWn58TcvASooWn7Zj7rUjlc8Ys1eVBLTjBmF9Vvncsily5bK9HFED7uj52qqAa+bvk6R4XKnwoQ321XG/OoOq13lFeZe8r9HcZs4bH0CSowxzZT/L51+biTl1Y2W0mUkLcyaui+uVdD75I2YQ1LYku1FTL0IDI2y7oPq/NC8fz90ZnRGK9oK4uIGDsLXYrBcvrCr69F1XTb8dD1NXJeoKqMRWedvgZms7HKDWJZtavFbX0l4MNZR5HD4HcNZ6GJZ3q44muLEivJPGmZhbwUzHZRDjKthLxD6DO33NNs1c+3XuoiRMN1cyUOU5p193Zd9ruBcQVbXxMhh8iz+YJRFUbYbQ67435/3sAJc9l2qyssrOmR2fmVwYfVkFbWMk3yvJ5FVJ/TfJSTeZXfUHIgMdzMimFmiBYobqqp25KHyavVTbOKfR8eEV8PS1mz9YzTK4I8VX2OXee6SnH+wMvmEKuBE9/C48B1u9Oo74hUGi4zDzTCtGA7EuUL3QBTXOjx5tG0O2yltE2EyFtyKWcbETlyl61Wye6pZ87HUViytoDbGwM3xaRGxz3FY2Fa6QODCk5qnEH0WWR1idLxukXL2DHsnL0e24YsDjfcp+nVgT7aJNkZIuoiOjpvsUt5yKtoU/h7elH4zpXZERta4uT6FKrE6ZCL3uy8SBxuZcC8mVLX/SYdABOY47LBi1jmx43EFawUatVZSzqbC6/VhVd62a1OMkqw84OxwG6DI4g2TgiSgVp5s7kQXFnWl7lAgEoCb/J4CBmNuF5xW2YOpMUziFa3auYue2eFjjLa48rGZrYbFvBUJw0XG/xCDvXJ9Rk5W1IiR9ADJe1J2ws7QibEDAalAlkcswPhqze6nbXKAk3JM75wr9xlkR1XfDfsKvnY0v6i4E352hBt1gGu4sLc2eYyGJAy14KbWSSmNoov1jzKRQs9RHQ646Wx8UFnY7qnaxcPnMxGyjWm9biomP0pjVdnzEHVK+kHglB0JlfeuiI+h1IVhgCGEotNBbFcDT0NQqMyACdMWgjoMQ0yRDgresLOl3LHwlG9jyKZupyXMiwH8m4ZLmfMmAn4bWs4zRnT7CvaooHbYedrngUOtQ1lGJYqikgJMqBYPLVJIhMXDeiPkVBi+8zSjaFPtRS77fULXinsAlnporZeAfpx3aS6oLsBdToTziJjgt5qL8npQkbjngkQXsxtU4HlsWfn5x2joIk9LPtw5wI822iGNF4pH4jLiA7ILCV9WxdrjMpV071ch124iq4adVG4vMtCK8WdFci8paM3KeMtVrJfDjBIu3wrSqA/5k/n3a3mLpt8v9YqRd9ca+KQjgpirzZLkmeLNsHEFimqYe5i6QwvFueFczzEvuk4KjzOsAp0TZu4GrF0TC4y2erO+RxQ+iI5+lrB6VQYN11xlNg4r2pKQptzR1XLOFX7IzsG5ZZ3pdNcaLvlbMx9UPtZeuwaWKE3Bc9KxS3WN2fO1Beq1Ml4bID8w3Wo48Ixk9VER9K75ZbBMPaabKLzjOeWIbyvrVWxO+UnVFjst7WmbDR+i/tzgcPH9gwLjTATKSk+pLy1R6I1oibHRsy3kmnMRTpZefv5LoGJTGfbbGvSRzrBF/meurHGKFVktM4v59rrz43IpxfxZlqmmjlIeqIrf+NqaVFQDEJtbreMO3t90GukGI1WyZUGe5XYtmK2Z4ln8AVX1oTnS2LsXozDbqYYZw5GjqrnIsVKvynStQY8AD1vL6h2xfZNk91Wp/Jcn1Pfc2pEnmOqw8Qz6wKXMiKs4CKm5UO229pLsglGaV5uM4SfR1IBn7hDM7/hB92tbaxCKpM4c5XiX1ellMP44Zw7M5lyjWvmeE02bKzW9nNfJoZFw5yzDUmsF4djZzfcVZP6Y+k3qBll69HIOhhX+DM5RO7c3xUGb1b+KVXglYnMVouInhFrAg3Wh+GwCZzDGXSDkXDg3WLWaxR9oEHsq3RGX0Nl75IepblZL2vjeMCijXj2w63jRxLqz3ClFVe02ZV2HuCSAhqF0d0eEVvs5OPpPN9ecXLNYtl4wNUREw5ITWrrRq+2tkbcgui859T5TlqIanI+MjQdFWfVHVXuWrGCnzgIc6tu0oAMHbw3/TS8XXN8qabDdU0uPLyXgvXqBoukIHSWGFDG5prNvHFoF704yJ6IYJ4R7BSQisv+hFaSlNnhaO0XBsFm8LgXpJHQzwS2XmUxW9T+wVcoOlmeiXAoV5rL6G5bwDuQ4PRIk/221p3dNsBzHd/OY2Rj56sM9Y5c1pGqxB06PSGT8nRYcXMeC26NLiPDfhTXR88cG3N9HYoaFUZki1WWkR4YQrraJc8ofU8sypyMbngRlLxx3mGqFieqrQ2wy6jheB4xa9TDbT0T8pU3ux4cnNxQcuXaq5WmOOS2LypHPpyojrrNVXnFuNMjM0y0e/q25NKjpOKVnVNwWFYk5lk7xW+bS2XOdQGmlwy19xcnSsp37KREcYY3qrGwauLIHk9Ulne3PROpebEDPS+LsR59wxdZL5SzOV0auat12bYpAUEhaviCYbTpzi2uRQITtg0C2+o0Oh79VjdXynwWXbrRR+WZVHdV4/nsZmHOyrpX29NBzBWKWLtdaXqqjoI26hZIIzq6Li1514SozEBZ2pF+E7k4yudistielPI8bsSGmwUSjoWLAcfkxYZ3AEvQ6qN8RPEdYROFCxqM7Xzpr/ADIgbL5dPz0/3PM54+IQhFY89P06u6l9dq//LVQ3CLii8vy3CUWDw//f97bv54uJ2DXS0Q2tPriMqz3E/33T/9C43++fxUORHY/fFmok7a4OVVQN3klffh+zP/f/30/+WP6r69cXo8j2+s4P5KBMx+/KVpnWfW05tXVOD6/s4JfL++6np5CfLtcT3QrgMLH29R5h8nHf/4b5Ka+sA6LAAA -->
