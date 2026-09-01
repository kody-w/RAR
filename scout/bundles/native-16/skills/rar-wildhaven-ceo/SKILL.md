---
name: "rar-wildhaven-ceo"
description: "Answers as the Wildhaven CEO digital twin from a built-in playbook of company facts, portfolio stats, and the Three Rules."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/ceo_agent", "rar_sha256": "c1e49265becbe104dceacd371dcbc6cce39aa53f3a36075fd47f06d9cf476896", "source_kind": "rar-agent", "source_commit": "d28a518312990c33b2d787dc051ae7c8cb90a2bb", "version": "1.0.3", "author": "Wildhaven of America", "tags": ["ceo", "digital-twin", "wildhaven", "rappter", "strategy", "leadership", "stewardship"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ceo_agent.py` and embedded as the fenced Python below (sha256 c1e49265becbe104…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ceo_agent.py` first:

```bash
python3 ceo_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ceo_agent.py   # or on stdin
python3 ceo_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
