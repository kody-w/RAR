---
name: "rar-wildhaven-ceo"
description: "Answers as the Wildhaven CEO digital twin from a built-in playbook of company facts, portfolio stats, and the Three Rules."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/ceo_agent", "rar_sha256": "c1e49265becbe104dceacd371dcbc6cce39aa53f3a36075fd47f06d9cf476896", "source_kind": "rar-agent", "source_commit": "d28a518312990c33b2d787dc051ae7c8cb90a2bb", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ceo_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@wildhaven/ceo:72ff644be80091502e9c0ea3c3a1690c98e79e8f0933898db2c6ca0982e9a577", "kind": "skill"}, "version": "1.0.3", "author": "Wildhaven of America", "tags": ["ceo", "digital-twin", "wildhaven", "rappter", "strategy", "leadership", "stewardship"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@wildhaven/ceo_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ceo_agent.py` is
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
