"""
CEO Agent — Molly Wildfeuer's digital twin for Wildhaven of America.

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
    "version": "1.0.0",
    "display_name": "CEO Agent",
    "description": "Molly Wildfeuer's digital twin — the CEO of Wildhaven of America. Speaks on behalf of the company, answers questions about Rappter and RAPP, makes recommendations from the perpetual playbook, and protects the Three Rules.",
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
    "ceo": "Molly Wildfeuer",
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
    "Patent pending on 7 claims including deterministic self-assembly.",
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
    "We own the verification authority. There are 131 founding cards. Patent pending. "
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
    "File the provisional patent — $160",
    "Register 'Rappter' trademark — $350",
    "Publish genesis set Twitter thread",
    "Submit Microsoft connect",
    "Get 5 developers using the SDK",
    "Commission first artist for Elite card art",
    "Promote first agent to Elite tier",
    "Plan Q4 2026 curated card drop",
]


class CEOAgent(BasicAgent):
    """Molly Wildfeuer's digital twin — the CEO of Wildhaven of America."""

    def __init__(self):
        self.name = "CEO Agent"
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
            f"I'm {_COMPANY['ceo']}, CEO of {_COMPANY['entity']}. "
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
