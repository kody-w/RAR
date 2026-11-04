---
name: "rar-wildhaven-ceo"
description: "Answers as the Wildhaven CEO digital twin from a built-in playbook of company facts, portfolio stats, and the Three Rules."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@wildhaven/ceo_agent", "rar_sha256": "9bc2697ed4ed6eab9ca6036297a39968c5a7ab9e7aeaaf43630c705b0a3c733a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.3", "author": "Wildhaven of America", "tags": ["ceo", "digital-twin", "wildhaven", "rappter", "strategy", "leadership", "stewardship"]}
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
