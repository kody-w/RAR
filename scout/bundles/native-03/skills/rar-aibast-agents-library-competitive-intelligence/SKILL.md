---
name: "rar-aibast-agents-library-competitive-intelligence"
description: "Builds competitive landscape analyses, win/loss reviews, and battlecards for enterprise deals from built-in demo data."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/competitive_intelligence", "rar_sha256": "f97b7a55aa7c6eabaf26e0b624c1a2d92ca024abf881212080c0da5fbef3f8e4", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "AIBAST", "tags": ["b2b", "sales", "competitive-intelligence", "battlecards", "win-loss"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/competitive_intelligence`. The original RAPP
agent is preserved byte-for-byte in `competitive_intelligence_agent.py` and in the RCI capsule.

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

Competitive Intelligence Agent

Analyzes competitive landscapes, reviews win/loss records, generates
positioning guides, and builds battlecards for enterprise B2B sales
engagements. Provides actionable competitive insights and counter-
positioning strategies.

Where a real deployment would call competitive intelligence platforms
and CRM APIs, this agent uses a synthetic data layer so it runs anywhere
without credentials.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "account_name": {
      "description": "Account name (e.g. 'Acme Corporation')",
      "type": "string"
    },
    "competitor": {
      "description": "Specific competitor name for battlecard",
      "type": "string"
    },
    "operation": {
      "description": "The competitive intelligence operation",
      "enum": [
        "landscape_analysis",
        "win_loss_review",
        "positioning_guide",
        "battlecard"
      ],
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `competitive_intelligence_agent.py` and embedded as the fenced Python below (sha256 f97b7a55aa7c6eab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `competitive_intelligence_agent.py` first:

```bash
python3 competitive_intelligence_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 competitive_intelligence_agent.py   # or on stdin
python3 competitive_intelligence_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Competitive Intelligence Agent

Analyzes competitive landscapes, reviews win/loss records, generates
positioning guides, and builds battlecards for enterprise B2B sales
engagements. Provides actionable competitive insights and counter-
positioning strategies.

Where a real deployment would call competitive intelligence platforms
and CRM APIs, this agent uses a synthetic data layer so it runs anywhere
without credentials.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
from datetime import datetime, timedelta

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/competitive_intelligence",
    "version": "1.0.1",
    "display_name": "Competitive Intelligence",
    "description": "Builds competitive landscape analyses, win/loss reviews, and battlecards for enterprise deals from built-in demo data.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "competitive-intelligence", "battlecards", "win-loss"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# SYNTHETIC DATA LAYER
# ═══════════════════════════════════════════════════════════════

_ACCOUNTS = {
    "acme": {"id": "acc-001", "name": "Acme Corporation", "industry": "Manufacturing", "opportunity_value": 2_400_000},
    "contoso": {"id": "acc-002", "name": "Contoso Ltd", "industry": "Technology", "opportunity_value": 1_100_000},
    "fabrikam": {"id": "acc-003", "name": "Fabrikam Industries", "industry": "Manufacturing", "opportunity_value": 890_000},
    "northwind": {"id": "acc-004", "name": "Northwind Traders", "industry": "Retail", "opportunity_value": 540_000},
}

_COMPETITORS = {
    "acme": [
        {
            "name": "DataForge Solutions", "relationship": "Medium", "product_fit": 78,
            "pricing": "-15% below market", "impl_weeks": 14,
            "activity": "On-site demo last week, aggressive discount offered",
            "strengths": ["Lower upfront cost", "Established in automotive manufacturing", "Local implementation team"],
            "weaknesses": ["Limited API ecosystem", "No real-time analytics", "Poor mobile experience"],
        },
        {
            "name": "CloudOps Platform", "relationship": "Weak", "product_fit": 82,
            "pricing": "+10% above market", "impl_weeks": 10,
            "activity": "Early conversations only, no formal proposal",
            "strengths": ["Modern cloud architecture", "Strong analytics suite", "Good developer tools"],
            "weaknesses": ["No manufacturing references", "Longer sales cycle", "Limited ERP integration"],
        },
    ],
    "contoso": [
        {
            "name": "DataForge Solutions", "relationship": "Strong", "product_fit": 85,
            "pricing": "Market rate", "impl_weeks": 12,
            "activity": "Incumbent on analytics module, pushing expansion",
            "strengths": ["Existing relationship", "Analytics depth", "Familiar to IT team"],
            "weaknesses": ["Platform fragmentation", "Scaling challenges", "Limited innovation pace"],
        },
    ],
    "fabrikam": [
        {
            "name": "ValueStack Inc", "relationship": "Weak", "product_fit": 70,
            "pricing": "-20% below market", "impl_weeks": 18,
            "activity": "Low-cost proposal submitted, basic feature set",
            "strengths": ["Lowest price point", "Simple deployment", "Basic manufacturing templates"],
            "weaknesses": ["Limited customization", "No enterprise support", "Feature gaps in analytics"],
        },
    ],
    "northwind": [],
}

_OUR_PROFILE = {
    "name": "TechVenture Solutions",
    "relationship": "Strong", "product_fit": 94, "pricing": "Market rate",
    "impl_weeks": 8,
    "strengths": [
        "Deepest ERP integration ecosystem",
        "Real-time analytics with AI insights",
        "94% customer retention rate",
        "Fastest implementation in category",
    ],
    "weaknesses": [
        "Premium pricing vs low-cost alternatives",
        "Complex initial configuration",
    ],
}

_WIN_LOSS_RECORDS = {
    "DataForge Solutions": {
        "total_encounters": 28, "wins": 18, "losses": 10,
        "win_rate": 0.643,
        "avg_deal_size_won": 1_850_000, "avg_deal_size_lost": 920_000,
        "common_win_reasons": ["Superior integration", "Customer references", "Implementation speed"],
        "common_loss_reasons": ["Price sensitivity", "Existing relationship", "Feature parity perception"],
        "recent_trend": "Improving — won 4 of last 5 encounters",
    },
    "CloudOps Platform": {
        "total_encounters": 15, "wins": 11, "losses": 4,
        "win_rate": 0.733,
        "avg_deal_size_won": 2_100_000, "avg_deal_size_lost": 1_400_000,
        "common_win_reasons": ["Manufacturing expertise", "Faster deployment", "Better support"],
        "common_loss_reasons": ["Cloud-native preference", "Developer tooling", "Modern UI"],
        "recent_trend": "Stable — consistent 70%+ win rate",
    },
    "ValueStack Inc": {
        "total_encounters": 12, "wins": 9, "losses": 3,
        "win_rate": 0.750,
        "avg_deal_size_won": 780_000, "avg_deal_size_lost": 340_000,
        "common_win_reasons": ["Enterprise features", "Scalability", "Support quality"],
        "common_loss_reasons": ["Price-driven buyer", "SMB scope", "Budget constraints"],
        "recent_trend": "Strong — rarely lose on enterprise deals",
    },
}

_FEATURE_COMPARISON = {
    "Real-time Analytics": {"us": "Full", "DataForge Solutions": "Limited", "CloudOps Platform": "Full", "ValueStack Inc": "None"},
    "ERP Integration": {"us": "Native (SAP, Oracle, D365)", "DataForge Solutions": "Partial (SAP only)", "CloudOps Platform": "API-based", "ValueStack Inc": "CSV Import"},
    "Mobile Experience": {"us": "Native iOS/Android", "DataForge Solutions": "Web only", "CloudOps Platform": "Progressive web app", "ValueStack Inc": "None"},
    "AI/ML Capabilities": {"us": "Predictive + Prescriptive", "DataForge Solutions": "Basic reporting", "CloudOps Platform": "Predictive only", "ValueStack Inc": "None"},
    "Implementation Time": {"us": "8 weeks", "DataForge Solutions": "14 weeks", "CloudOps Platform": "10 weeks", "ValueStack Inc": "18 weeks"},
    "Customer Support": {"us": "24/7 dedicated CSM", "DataForge Solutions": "Business hours", "CloudOps Platform": "24/7 ticketing", "ValueStack Inc": "Email only"},
    "Security Certifications": {"us": "SOC2, ISO27001, GDPR", "DataForge Solutions": "SOC2", "CloudOps Platform": "SOC2, ISO27001", "ValueStack Inc": "SOC2"},
    "API Ecosystem": {"us": "500+ integrations", "DataForge Solutions": "120 integrations", "CloudOps Platform": "300+ integrations", "ValueStack Inc": "40 integrations"},
}

_PRICING_INTEL = {
    "DataForge Solutions": {"base_per_user": 85, "enterprise_discount": "15-25%", "typical_tcl_3yr": 1_200_000, "pricing_model": "Per user/month", "hidden_costs": "Implementation services billed separately"},
    "CloudOps Platform": {"base_per_user": 120, "enterprise_discount": "10-15%", "typical_tcl_3yr": 1_800_000, "pricing_model": "Per user/month + data volume", "hidden_costs": "Data egress fees, premium support tier"},
    "ValueStack Inc": {"base_per_user": 45, "enterprise_discount": "5-10%", "typical_tcl_3yr": 650_000, "pricing_model": "Flat per user/month", "hidden_costs": "Customization professional services"},
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_account(query):
    if not query:
        return "acme"
    q = query.lower().strip()
    for key in _ACCOUNTS:
        if key in q or q in _ACCOUNTS[key]["name"].lower():
            return key
    return "acme"


def _competitive_threat_score(competitor):
    """Score 0-100 threat level from competitor attributes."""
    rel_scores = {"Strong": 30, "Medium": 20, "Weak": 10}
    fit_score = competitor["product_fit"] * 0.4
    rel_score = rel_scores.get(competitor["relationship"], 10)
    price_score = 20 if "-" in competitor["pricing"] else 10 if "Market" in competitor["pricing"] else 5
    return min(100, int(fit_score + rel_score + price_score))


def _overall_competitive_position(key):
    """Assess our overall position vs competitors for an account."""
    comps = _COMPETITORS.get(key, [])
    if not comps:
        return "Dominant", 95
    max_threat = max(_competitive_threat_score(c) for c in comps)
    if max_threat >= 70:
        return "Contested", 100 - max_threat + 30
    if max_threat >= 50:
        return "Favorable", 100 - max_threat + 40
    return "Strong", 90


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class CompetitiveIntelligenceAgent(BasicAgent):
    """
    Provides competitive intelligence for enterprise deals.

    Operations:
        landscape_analysis  - competitive landscape for an account
        win_loss_review     - win/loss analysis per competitor
        positioning_guide   - positioning recommendations
        battlecard          - detailed competitor battlecard
    """

    def __init__(self):
        self.name = "CompetitiveIntelligenceAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "landscape_analysis", "win_loss_review",
                            "positioning_guide", "battlecard",
                        ],
                        "description": "The competitive intelligence operation",
                    },
                    "account_name": {
                        "type": "string",
                        "description": "Account name (e.g. 'Acme Corporation')",
                    },
                    "competitor": {
                        "type": "string",
                        "description": "Specific competitor name for battlecard",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "landscape_analysis")
        key = _resolve_account(kwargs.get("account_name", ""))
        dispatch = {
            "landscape_analysis": self._landscape_analysis,
            "win_loss_review": self._win_loss_review,
            "positioning_guide": self._positioning_guide,
            "battlecard": self._battlecard,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation `{op}`."
        return handler(key, **kwargs)

    # ── landscape_analysis ────────────────────────────────────
    def _landscape_analysis(self, key, **kwargs):
        acct = _ACCOUNTS[key]
        comps = _COMPETITORS.get(key, [])

        if not comps:
            return (
                f"**Competitive Landscape: {acct['name']}**\n\n"
                f"No active competitors identified for this account.\n"
                f"This represents a greenfield opportunity.\n\n"
                f"Source: [Competitive Intel Database]\nAgents: CompetitiveIntelligenceAgent"
            )

        position, confidence = _overall_competitive_position(key)

        header = "| Factor | {name} |".format(name=_OUR_PROFILE["name"]) + "".join(f" {c['name']} |" for c in comps) + "\n"
        sep = "|---|---|" + "".join("---|" for _ in comps) + "\n"
        rows_data = [
            ("Relationship", _OUR_PROFILE["relationship"], [c["relationship"] for c in comps]),
            ("Product Fit", f"{_OUR_PROFILE['product_fit']}%", [f"{c['product_fit']}%" for c in comps]),
            ("Pricing", _OUR_PROFILE["pricing"], [c["pricing"] for c in comps]),
            ("Implementation", f"{_OUR_PROFILE['impl_weeks']} weeks", [f"{c['impl_weeks']} weeks" for c in comps]),
        ]
        rows = ""
        for label, ours, theirs in rows_data:
            rows += f"| {label} | {ours} |" + "".join(f" {t} |" for t in theirs) + "\n"

        activity = "\n**Competitor Activity:**\n" + "".join(f"- {c['name']}: {c['activity']}\n" for c in comps)

        threat_rows = ""
        for c in comps:
            score = _competitive_threat_score(c)
            level = "High" if score >= 65 else "Medium" if score >= 45 else "Low"
            threat_rows += f"| {c['name']} | {score}/100 | {level} |\n"

        return (
            f"**Competitive Landscape: {acct['name']}**\n\n"
            f"**Our Position: {position}** (confidence: {confidence}%)\n"
            f"Opportunity value: ${acct['opportunity_value']:,}\n\n"
            f"{header}{sep}{rows}"
            f"{activity}\n"
            f"**Threat Assessment:**\n\n"
            f"| Competitor | Threat Score | Level |\n|---|---|---|\n"
            f"{threat_rows}\n"
            f"Source: [Competitive Intel + Win/Loss Database + Field Intelligence]\n"
            f"Agents: CompetitiveIntelligenceAgent"
        )

    # ── win_loss_review ───────────────────────────────────────
    def _win_loss_review(self, key, **kwargs):
        acct = _ACCOUNTS[key]
        comps = _COMPETITORS.get(key, [])
        comp_names = [c["name"] for c in comps] if comps else list(_WIN_LOSS_RECORDS.keys())

        output = f"**Win/Loss Review: {acct['name']}**\n\n"

        for name in comp_names:
            record = _WIN_LOSS_RECORDS.get(name)
            if not record:
                continue

            output += (
                f"---\n**vs {name}:**\n\n"
                f"| Metric | Value |\n|---|---|\n"
                f"| Total Encounters | {record['total_encounters']} |\n"
                f"| Wins | {record['wins']} |\n"
                f"| Losses | {record['losses']} |\n"
                f"| Win Rate | {record['win_rate']:.0%} |\n"
                f"| Avg Deal Won | ${record['avg_deal_size_won']:,} |\n"
                f"| Avg Deal Lost | ${record['avg_deal_size_lost']:,} |\n"
                f"| Trend | {record['recent_trend']} |\n\n"
                f"**Why We Win:**\n"
                + "".join(f"- {r}\n" for r in record["common_win_reasons"])
                + f"\n**Why We Lose:**\n"
                + "".join(f"- {r}\n" for r in record["common_loss_reasons"])
                + "\n"
            )

        output += (
            f"Source: [Win/Loss Database + CRM Deal History]\n"
            f"Agents: CompetitiveIntelligenceAgent"
        )
        return output

    # ── positioning_guide ─────────────────────────────────────
    def _positioning_guide(self, key, **kwargs):
        acct = _ACCOUNTS[key]
        comps = _COMPETITORS.get(key, [])

        output = (
            f"**Positioning Guide: {acct['name']}**\n\n"
            f"**Our Key Differentiators:**\n"
            + "".join(f"- {s}\n" for s in _OUR_PROFILE["strengths"])
            + "\n"
        )

        for c in comps:
            record = _WIN_LOSS_RECORDS.get(c["name"], {})
            pricing = _PRICING_INTEL.get(c["name"], {})

            output += (
                f"---\n**vs {c['name']}:**\n\n"
                f"**Attack Points (their weaknesses):**\n"
                + "".join(f"- {w}\n" for w in c["weaknesses"])
                + f"\n**Defend Against (their strengths):**\n"
                + "".join(f"- {s}\n" for s in c["strengths"])
                + "\n**Recommended Talk Track:**\n"
            )

            if "-" in c["pricing"]:
                output += (
                    f"- Reframe from upfront cost to TCO: their 3-year TCO is ${pricing.get('typical_tcl_3yr', 0):,} vs our superior value\n"
                    f"- Highlight hidden costs: {pricing.get('hidden_costs', 'N/A')}\n"
                )
            else:
                output += "- Focus on differentiated capabilities and faster time-to-value\n"

            output += (
                f"- Reference win rate: {record.get('win_rate', 0):.0%} when we compete directly\n"
                f"- Key proof point: {record.get('common_win_reasons', ['Superior platform'])[0]}\n\n"
            )

        if not comps:
            output += "No active competitors — focus on value creation vs status quo.\n\n"

        output += (
            f"Source: [Sales Playbook + Win/Loss Analysis + Field Intelligence]\n"
            f"Agents: CompetitiveIntelligenceAgent"
        )
        return output

    # ── battlecard ────────────────────────────────────────────
    def _battlecard(self, key, **kwargs):
        acct = _ACCOUNTS[key]
        comps = _COMPETITORS.get(key, [])
        target_name = kwargs.get("competitor", "")

        # Find the target competitor or use first one
        target = None
        for c in comps:
            if target_name.lower() in c["name"].lower():
                target = c
                break
        if not target and comps:
            target = comps[0]
        if not target:
            return f"**Battlecard: {acct['name']}**\n\nNo competitors identified for this account."

        record = _WIN_LOSS_RECORDS.get(target["name"], {})
        pricing = _PRICING_INTEL.get(target["name"], {})
        threat = _competitive_threat_score(target)

        # Feature comparison for this competitor
        feature_rows = ""
        for feature, scores in _FEATURE_COMPARISON.items():
            our_val = scores.get("us", "N/A")
            their_val = scores.get(target["name"], "N/A")
            advantage = "Us" if our_val != "None" and (their_val == "None" or their_val == "Limited") else "Them" if our_val == "None" else "Even"
            feature_rows += f"| {feature} | {our_val} | {their_val} | {advantage} |\n"

        return (
            f"**Battlecard: {_OUR_PROFILE['name']} vs {target['name']}**\n"
            f"Account: {acct['name']} | Opportunity: ${acct['opportunity_value']:,}\n\n"
            f"**Threat Level: {threat}/100**\n\n"
            f"| Attribute | Us | Them |\n|---|---|---|\n"
            f"| Relationship | {_OUR_PROFILE['relationship']} | {target['relationship']} |\n"
            f"| Product Fit | {_OUR_PROFILE['product_fit']}% | {target['product_fit']}% |\n"
            f"| Pricing | {_OUR_PROFILE['pricing']} | {target['pricing']} |\n"
            f"| Implementation | {_OUR_PROFILE['impl_weeks']} weeks | {target['impl_weeks']} weeks |\n"
            f"| Win Rate (head-to-head) | {record.get('win_rate', 0):.0%} | {1 - record.get('win_rate', 0):.0%} |\n\n"
            f"**Feature Comparison:**\n\n"
            f"| Feature | Us | {target['name']} | Advantage |\n|---|---|---|---|\n"
            f"{feature_rows}\n"
            f"**Their Strengths (defend):**\n"
            + "".join(f"- {s}\n" for s in target["strengths"])
            + f"\n**Their Weaknesses (attack):**\n"
            + "".join(f"- {w}\n" for w in target["weaknesses"])
            + f"\n**Pricing Intel:**\n"
            f"- Base price: ${pricing.get('base_per_user', 0)}/user/month\n"
            f"- Enterprise discount: {pricing.get('enterprise_discount', 'Unknown')}\n"
            f"- 3-year TCO: ${pricing.get('typical_tcl_3yr', 0):,}\n"
            f"- Hidden costs: {pricing.get('hidden_costs', 'None identified')}\n\n"
            f"**Killer Questions to Ask the Prospect:**\n"
            f"1. \"How important is real-time analytics for your operations team?\"\n"
            f"2. \"What's your timeline for ERP integration — weeks or months?\"\n"
            f"3. \"Have you factored in implementation services and hidden costs?\"\n\n"
            f"Source: [Competitive Intel + Win/Loss + Pricing Intelligence]\n"
            f"Agents: CompetitiveIntelligenceAgent"
        )


if __name__ == "__main__":
    agent = CompetitiveIntelligenceAgent()
    for op in ["landscape_analysis", "win_loss_review", "positioning_guide", "battlecard"]:
        print("=" * 60)
        print(agent.perform(operation=op, account_name="Acme Corporation"))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
