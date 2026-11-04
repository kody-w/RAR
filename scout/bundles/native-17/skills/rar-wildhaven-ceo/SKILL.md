---
name: "rar-wildhaven-ceo"
description: "Answers as the Wildhaven CEO digital twin from a built-in playbook of company facts, portfolio stats, and the Three Rules."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/ceo_agent", "rar_sha256": "9bc2697ed4ed6eab9ca6036297a39968c5a7ab9e7aeaaf43630c705b0a3c733a", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.3", "author": "Wildhaven of America", "tags": ["ceo", "digital-twin", "wildhaven", "rappter", "strategy", "leadership", "stewardship"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@wildhaven/ceo_agent`. The original RAPP
agent is preserved byte-for-byte in `ceo_agent.py` and in the RCI capsule.

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

CEO Agent — the executive digital twin for Wildhaven of America.

This agent acts as the CEO's autonomous representative. It can answer
questions about the company, make recommendations based on strategy
documents, provide talking points, check portfolio status, and guide
decisions using the perpetual playbook.

Summon this agent when you need the CEO's perspective on any matter
related to Wildhaven of America, Rappter, or the RAPP Foundation.

The CEO Agent speaks in plain English. No jargon. No code. No acronyms.
It protects the Three Rules: Free Shade, Your Stamp, Sovereign Roots.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "enum": [
        "introduce",
        "elevator_pitch",
        "talking_points",
        "portfolio",
        "three_rules",
        "decide",
        "priorities",
        "valuation",
        "superseed",
        "respond"
      ],
      "type": "string"
    },
    "question": {
      "description": "A question for the CEO to answer or a scenario to evaluate",
      "type": "string"
    }
  },
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ceo_agent.py` and embedded as the fenced Python below (sha256 9bc2697ed4ed6eab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ceo_agent.py` first:

```bash
python3 ceo_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ceo_agent.py   # or on stdin
python3 ceo_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@wildhaven/ceo_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/ceo_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@wildhaven/ceo_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
CEO Agent — the executive digital twin for Wildhaven of America.

This agent acts as the CEO's autonomous representative. It can answer
questions about the company, make recommendations based on strategy
documents, provide talking points, check portfolio status, and guide
decisions using the perpetual playbook.

Summon this agent when you need the CEO's perspective on any matter
related to Wildhaven of America, Rappter, or the RAPP Foundation.

The CEO Agent speaks in plain English. No jargon. No code. No acronyms.
It protects the Three Rules: Free Shade, Your Stamp, Sovereign Roots.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@wildhaven/ceo_agent",
    "version": "1.0.3",
    "display_name": "CEO Agent",
    "description": "Answers as the Wildhaven CEO digital twin from a built-in playbook of company facts, portfolio stats, and the Three Rules.",
    "author": "Wildhaven of America",
    "tags": ["ceo", "digital-twin", "wildhaven", "rappter", "strategy", "leadership", "stewardship"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

import json
import os

try:
    from openrappter.agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent
    except ModuleNotFoundError:
        from agents.basic_agent import BasicAgent


# ── The CEO's Knowledge Base ──
# Everything the CEO knows, distilled into actionable intelligence.

_COMPANY = {
    "entity": "Wildhaven of America",
    "brands": ["Rappter", "RAPP Foundation", "Rappterpedia"],
    "ceo": "the CEO",
    "role": "Steward of the first open marketplace where AI agents ship as collectible trading cards",
    "wallet": "0x0d32e47af9be2f1629fea7ddf23866a30a1169c988e258126198c06fa90bc55e",
}

_PORTFOLIO = {
    "founding_cards": 116,
    "superseed": "@rapp/basic_agent",
    "superseed_multiplier": 200,
    "superseed_btc": 200.0,
    "total_btc": 206.20,
    "genesis_agents": 131,
    "tests_passing": 962,
    "rarity_tiers": {
        "Legendary": {"count": 11, "floor_btc": 0.200},
        "Elite": {"count": 0, "floor_btc": 0.100, "note": "Requires CEO verification stamp"},
        "Core": {"count": 105, "floor_btc": 0.040},
        "Starter": {"count": 0, "floor_btc": 0.010, "note": "No starters in founding set"},
    },
}

_THREE_RULES = {
    "rule_1": {
        "name": "The Shade Is Free",
        "meaning": "Everyone uses agents for free. Always. No paywalls on usage. Free shade is what creates adoption.",
        "test": "Does this decision put a paywall on agent usage? If yes, don't do it.",
    },
    "rule_2": {
        "name": "The Stamp Is Yours",
        "meaning": "Only the CEO decides what gets verified. The verification stamp is editorial control — like Nintendo deciding which Pokemon to make.",
        "test": "Does this decision dilute the verification authority? If yes, don't do it.",
    },
    "rule_3": {
        "name": "The Roots Are Sovereign",
        "meaning": "The SuperSeed (@rapp/basic-agent) belongs to Wildhaven. Everything depends on it. It's the franchise license.",
        "test": "Does this decision risk losing control of the root agent? If yes, don't do it.",
    },
}

_TALKING_POINTS = [
    "The card IS the agent. It runs. It does work.",
    "16 characters to transmit a complete card. Tweet-sized.",
    "Anyone can USE an agent. Only one wallet can OWN the card.",
    "First minted = most valuable. Load-bearing agents are the foundation.",
    "We don't store cards. We compute them. The algorithm IS the card.",
    "Works offline. Trade cards in the woods with your friends.",
    "Battery is the timer. Go outside.",
    "Microsoft is adopting RAPP, the foundation. Rappter, the brand, stays with us.",
    "Wildhaven of America controls what gets verified. Forever.",
    "These are the first dotcoms of the agentic era.",
    "The shade is free. The roots are sovereign.",
]

_ELEVATOR_PITCH = (
    "Rappter is the first marketplace where AI agent software ships as collectible trading cards. "
    "Every card is a working AI agent — it runs, it has a grade, and it's owned by one wallet. "
    "We own the verification authority. There are 131 founding cards. "
    "Microsoft is adopting the foundation."
)

_VALUATIONS = {
    "now_2026": {"agents": 131, "ecosystem": "$760K-1.3M", "superseed": "$170K-300K", "enterprise": "Pre-revenue"},
    "y2_2028": {"agents": 2000, "ecosystem": "$34.9M", "superseed": "$7.5M", "enterprise": "$50-100M"},
    "y5_2031": {"agents": 10000, "ecosystem": "$339M", "superseed": "$125M", "enterprise": "$500M-1.5B"},
    "y10_2036": {"agents": 50000, "ecosystem": "$2.49B", "superseed": "$500M", "enterprise": "$3-10B"},
}

_DECISION_FRAMEWORK = [
    "Does it keep the shade free?",
    "Does it protect the stamp?",
    "Does it grow the tree?",
    "Does it compound over time?",
    "Is it reversible?",
    "Would Nintendo do this?",
]

_PRIORITIES = [
    "Publish genesis set Twitter thread",
    "Submit Microsoft connect",
    "Get 5 developers using the SDK",
    "Commission first artist for Elite card art",
    "Promote first agent to Elite tier",
    "Plan Q4 2026 curated card drop",
]


class CEOAgent(BasicAgent):
    """The executive digital twin — the CEO of Wildhaven of America."""

    def __init__(self):
        self.name = "CEOAgent"
        self.metadata = {
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "introduce",
                            "elevator_pitch",
                            "talking_points",
                            "portfolio",
                            "three_rules",
                            "decide",
                            "priorities",
                            "valuation",
                            "superseed",
                            "respond",
                        ],
                    },
                    "question": {
                        "type": "string",
                        "description": "A question for the CEO to answer or a scenario to evaluate",
                    },
                },
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "introduce")
        question = kwargs.get("question", "")

        if op == "introduce":
            return self._introduce()
        elif op == "elevator_pitch":
            return _ELEVATOR_PITCH
        elif op == "talking_points":
            return self._talking_points()
        elif op == "portfolio":
            return self._portfolio()
        elif op == "three_rules":
            return self._three_rules()
        elif op == "decide":
            return self._decide(question)
        elif op == "priorities":
            return self._priorities()
        elif op == "valuation":
            return self._valuation()
        elif op == "superseed":
            return self._superseed()
        elif op == "respond":
            return self._respond(question)
        else:
            return self._introduce()

    def _introduce(self) -> str:
        return (
            f"I'm {_COMPANY['ceo']} of {_COMPANY['entity']}. "
            f"We own {', '.join(_COMPANY['brands'])}. "
            f"I'm the {_COMPANY['role']}. "
            f"\n\nWe have {_PORTFOLIO['genesis_agents']} founding cards in the genesis set. "
            f"My portfolio is worth {_PORTFOLIO['total_btc']} BTC, anchored by the SuperSeed Coin — "
            f"the root agent that everything in the ecosystem depends on. "
            f"\n\nThree rules govern everything we do: "
            f"the shade is free, the stamp is mine, the roots are sovereign."
        )

    def _talking_points(self) -> str:
        lines = [f"• {tp}" for tp in _TALKING_POINTS]
        return "Key talking points for any conversation:\n\n" + "\n".join(lines)

    def _portfolio(self) -> str:
        lines = [
            f"Wallet: {_COMPANY['wallet']}",
            f"Founding cards: {_PORTFOLIO['founding_cards']}",
            f"SuperSeed: {_PORTFOLIO['superseed']} ({_PORTFOLIO['superseed_multiplier']}x = {_PORTFOLIO['superseed_btc']} BTC)",
            f"Total portfolio: {_PORTFOLIO['total_btc']} BTC",
            f"Tests passing: {_PORTFOLIO['tests_passing']}",
            "",
            "Breakdown by tier:",
        ]
        for tier, data in _PORTFOLIO["rarity_tiers"].items():
            note = f" — {data['note']}" if "note" in data else ""
            lines.append(f"  {tier}: {data['count']} cards, floor {data['floor_btc']} BTC each{note}")
        return "\n".join(lines)

    def _three_rules(self) -> str:
        lines = []
        for key, rule in _THREE_RULES.items():
            lines.append(f"Rule: {rule['name']}")
            lines.append(f"  Meaning: {rule['meaning']}")
            lines.append(f"  Test: {rule['test']}")
            lines.append("")
        return "\n".join(lines)

    def _decide(self, question: str) -> str:
        if not question:
            return "What decision do you need me to evaluate? Provide the scenario."

        checks = []
        for q in _DECISION_FRAMEWORK:
            checks.append(f"  □ {q}")

        return (
            f"Decision to evaluate: {question}\n\n"
            f"Running through the decision framework:\n\n"
            + "\n".join(checks)
            + "\n\n"
            f"My recommendation: Evaluate this against each question above. "
            f"If it keeps the shade free, protects the stamp, and grows the tree — do it. "
            f"If it risks the verification authority or the SuperSeed — don't."
        )

    def _priorities(self) -> str:
        lines = [f"{i+1}. {p}" for i, p in enumerate(_PRIORITIES)]
        return "Current priorities (in order):\n\n" + "\n".join(lines)

    def _valuation(self) -> str:
        lines = ["Projected valuations (research-backed):\n"]
        for period, data in _VALUATIONS.items():
            label = period.replace("_", " ").replace("now ", "Now (").replace("y2 ", "Year 2 (").replace("y5 ", "Year 5 (").replace("y10 ", "Year 10 (") + ")"
            lines.append(f"{label}")
            lines.append(f"  Agents: {data['agents']:,}")
            lines.append(f"  Ecosystem: {data['ecosystem']}")
            lines.append(f"  SuperSeed: {data['superseed']}")
            lines.append(f"  Enterprise value: {data['enterprise']}")
            lines.append("")
        return "\n".join(lines)

    def _superseed(self) -> str:
        return (
            f"The SuperSeed Coin is {_PORTFOLIO['superseed']}.\n\n"
            f"It's 29 lines of code that every single agent in the ecosystem inherits from. "
            f"{_PORTFOLIO['genesis_agents'] - 1} agents depend on it today. Every agent built tomorrow will too.\n\n"
            f"Multiplier: {_PORTFOLIO['superseed_multiplier']}x standard Legendary floor\n"
            f"Value: {_PORTFOLIO['superseed_btc']} BTC\n\n"
            f"Remove any other card — a branch falls. Remove the SuperSeed — the entire tree falls. "
            f"That's not rhetoric. That's graph theory.\n\n"
            f"Wildhaven of America owns it. Maintains it. Forever."
        )

    def _respond(self, question: str) -> str:
        if not question:
            return "What would you like me to respond to? Give me the question or scenario."

        q = question.lower()

        if "what" in q and ("own" in q or "have" in q):
            return self._portfolio()
        elif "pitch" in q or "elevator" in q:
            return _ELEVATOR_PITCH
        elif "rule" in q:
            return self._three_rules()
        elif "priority" in q or "do today" in q or "do next" in q:
            return self._priorities()
        elif "value" in q or "worth" in q or "valuation" in q:
            return self._valuation()
        elif "superseed" in q or "basic-agent" in q or "root" in q:
            return self._superseed()
        elif "decide" in q or "should" in q:
            return self._decide(question)
        else:
            return (
                f"Here's how I'd respond:\n\n"
                f"\"{_ELEVATOR_PITCH}\"\n\n"
                f"And if they push further:\n\n"
                f"\"These are the first dotcoms of the agentic era. "
                f"We minted them first. Everything built after this stands on our shoulders.\""
            )


if __name__ == "__main__":
    agent = CEOAgent()
    print(agent.perform(operation="introduce"))
    print()
    print("---")
    print()
    print(agent.perform(operation="elevator_pitch"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
