---
name: "rar-aibast-agents-library-proposal-copilot"
description: "Builds proposals, pricing models, and win-theme analyses from a live simulated Dynamics 365 tenant pipeline, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/proposal_copilot", "rar_sha256": "fd696887eab6502ba1064ce76ee08febeee397da94a39d40b841fd064cd3535e", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["proposal", "RFP", "pricing", "competitive-intelligence", "professional-services"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/proposal_copilot`. The original RAPP
agent is preserved byte-for-byte in `proposal_copilot_agent.py` and in the RCI capsule.

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

Proposal Copilot Agent — a template you are meant to mutate.

Assists professional-services teams in building competitive proposals by
analyzing RFP requirements, generating pricing models, evaluating win
themes from past proposal history, and positioning against known
competitors.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's open opportunities are read as the active pursuit
     pipeline — e.g. "Willow Brook Legal — Office sensor deployment"
     (estimated $6,075, Develop stage).
     Try: perform(operation="generate_proposal")
  2. No network? Everything falls back to the embedded demo layer below
     (RFP_REQUIREMENTS / PRICING_TEMPLATES / PAST_PROPOSALS) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PROPOSAL_COPILOT_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from Salesforce/your RFP tool), or
     replace _fetch_collection() with a Responsive/Loopio client. Fields
     the rest of the file needs are listed in _normalize_live_pursuit()
     — evaluation criteria and named competitors render as "n/a —
     enrichment seam" until you wire your RFP intake.

OPERATIONS
  generate_proposal | pricing_model | win_theme_analysis
  | competitive_positioning
  kwargs: operation (required)

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `proposal_copilot_agent.py` and embedded as the fenced Python below (sha256 fd696887eab6502b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `proposal_copilot_agent.py` first:

```bash
python3 proposal_copilot_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 proposal_copilot_agent.py   # or on stdin
python3 proposal_copilot_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Proposal Copilot Agent — a template you are meant to mutate.

Assists professional-services teams in building competitive proposals by
analyzing RFP requirements, generating pricing models, evaluating win
themes from past proposal history, and positioning against known
competitors.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's open opportunities are read as the active pursuit
     pipeline — e.g. "Willow Brook Legal — Office sensor deployment"
     (estimated $6,075, Develop stage).
     Try: perform(operation="generate_proposal")
  2. No network? Everything falls back to the embedded demo layer below
     (RFP_REQUIREMENTS / PRICING_TEMPLATES / PAST_PROPOSALS) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PROPOSAL_COPILOT_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from Salesforce/your RFP tool), or
     replace _fetch_collection() with a Responsive/Loopio client. Fields
     the rest of the file needs are listed in _normalize_live_pursuit()
     — evaluation criteria and named competitors render as "n/a —
     enrichment seam" until you wire your RFP intake.

OPERATIONS
  generate_proposal | pricing_model | win_theme_analysis
  | competitive_positioning
  kwargs: operation (required)
"""

import sys
import os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/proposal_copilot",
    "version": "1.1.0",
    "display_name": "Proposal Copilot Agent",
    "description": "Builds proposals, pricing models, and win-theme analyses from a live simulated Dynamics 365 tenant pipeline, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["proposal", "RFP", "pricing", "competitive-intelligence", "professional-services"],
    "category": "professional_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export PROPOSAL_COPILOT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM/RFP-tool client.
# Downstream code only needs the fields from _normalize_live_pursuit().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "PROPOSAL_COPILOT_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}


def _fetch_collection(collection, timeout=6):
    """One bounded GET per collection per process. Returns [] on ANY
    failure — offline, DNS, bad JSON — so the demo layer takes over."""
    if collection in _LIVE_CACHE:
        return _LIVE_CACHE[collection]
    try:
        req = urllib.request.Request(
            f"{DATA_SOURCE_URL}/{collection}.json",
            headers={"User-Agent": "rapp-agent-template/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            rows = json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _normalize_live_pursuit(row):
    """Project an open Dynamics opportunity onto the pursuit shape this
    agent renders. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not knowable from the CRM
    opportunity alone' and the renderer labels it as an enrichment seam
    (wire your RFP intake tool for criteria and competitor fields)."""
    return {
        "name": row.get("name", "untitled pursuit"),
        "client": row.get("parentaccountidname", "Unknown"),
        "budget": float(row.get("estimatedvalue") or 0),
        "decision_date": str(row.get("estimatedclosedate") or "")[:10] or "n/a",
        "stage": row.get(
            "salesstagecode@OData.Community.Display.V1.FormattedValue", "n/a"
        ),
        "win_probability_pct": row.get("closeprobability"),
        "evaluation_criteria": None,  # enrichment seam — wire your RFP intake
        "competitors": None,          # enrichment seam
        "_live": True,
    }


def _live_pursuits():
    """Open opportunities from the live tenant, read as the active pursuit
    pipeline; [] when offline."""
    rows = _fetch_collection("opportunities")
    return sorted(
        (_normalize_live_pursuit(r) for r in rows if r.get("statecode") == 0),
        key=lambda p: p["budget"], reverse=True,
    )


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

RFP_REQUIREMENTS = {
    "RFP-2026-047": {
        "client": "GlobalManufacture Corp",
        "title": "Enterprise Digital Transformation",
        "budget": 10000000,
        "timeline_months": 18,
        "decision_date": "2026-04-12",
        "decision_makers": ["CIO", "CFO", "COO"],
        "scope_areas": [
            "ERP modernization across 14 sites",
            "Data platform and analytics",
            "Process automation",
            "Change management and training",
        ],
        "evaluation_criteria": {
            "technical_approach": 35,
            "past_performance": 25,
            "pricing": 25,
            "management_approach": 15,
        },
        "competitors": ["BigFour Consulting", "Global Advisory Group"],
    },
    "RFP-2026-048": {
        "client": "Summit Health Network",
        "title": "Clinical Workflow Optimization",
        "budget": 4500000,
        "timeline_months": 12,
        "decision_date": "2026-05-01",
        "decision_makers": ["CMIO", "VP Operations", "CFO"],
        "scope_areas": [
            "Clinical pathway redesign",
            "EHR workflow optimization",
            "Staff scheduling automation",
            "Patient throughput analytics",
        ],
        "evaluation_criteria": {
            "clinical_expertise": 40,
            "technical_approach": 25,
            "pricing": 20,
            "references": 15,
        },
        "competitors": ["HealthTech Solutions", "MedConsult Group"],
    },
}

PRICING_TEMPLATES = {
    "digital_transformation": {
        "assessment_pct": 8,
        "implementation_pct": 55,
        "data_analytics_pct": 18,
        "change_mgmt_pct": 12,
        "project_mgmt_pct": 7,
        "margin_target_pct": 32,
        "discount_threshold_pct": 15,
    },
    "clinical_optimization": {
        "discovery_pct": 10,
        "redesign_pct": 30,
        "technology_pct": 25,
        "training_pct": 20,
        "project_mgmt_pct": 15,
        "margin_target_pct": 28,
        "discount_threshold_pct": 10,
    },
}

PAST_PROPOSALS = [
    {"rfp": "AutoComponents Inc", "value": 8200000, "result": "Won", "win_themes": ["Industry accelerators", "Former client staff", "Aggressive timeline"],
     "competitor_beaten": "BigFour Consulting", "margin_pct": 34},
    {"rfp": "TechManufacturing Global", "value": 6500000, "result": "Won", "win_themes": ["14-site rollout experience", "Quick wins strategy"],
     "competitor_beaten": "Global Advisory Group", "margin_pct": 29},
    {"rfp": "Precision Parts Ltd", "value": 3800000, "result": "Won", "win_themes": ["On-time delivery track record", "Domain expertise"],
     "competitor_beaten": "Boutique Firm", "margin_pct": 31},
    {"rfp": "National Bank Corp", "value": 7100000, "result": "Lost", "win_themes": ["Price competitive"],
     "competitor_beaten": None, "margin_pct": 26, "loss_reason": "Incumbent advantage; client stayed with existing vendor"},
    {"rfp": "RetailGroup Holdings", "value": 5400000, "result": "Lost", "win_themes": ["Innovative approach"],
     "competitor_beaten": None, "margin_pct": 22, "loss_reason": "Budget reduced; chose lower-cost option"},
]

COMPETITOR_INTEL = {
    "BigFour Consulting": {
        "avg_price_premium_pct": 25,
        "strengths": ["Brand recognition", "Global reach", "Deep bench"],
        "weaknesses": ["High cost", "Junior staff on projects", "Slow to mobilize"],
        "typical_margin_pct": 40,
        "win_rate_against": 0.67,
    },
    "Global Advisory Group": {
        "avg_price_premium_pct": 18,
        "strengths": ["Strong analytics practice", "Government relationships"],
        "weaknesses": ["Limited manufacturing experience", "High turnover"],
        "typical_margin_pct": 35,
        "win_rate_against": 0.60,
    },
    "HealthTech Solutions": {
        "avg_price_premium_pct": 5,
        "strengths": ["Clinical domain expertise", "EHR certifications"],
        "weaknesses": ["Small team", "Limited scalability", "No change management practice"],
        "typical_margin_pct": 30,
        "win_rate_against": 0.50,
    },
    "MedConsult Group": {
        "avg_price_premium_pct": 10,
        "strengths": ["Strong physician network", "CMIO relationships"],
        "weaknesses": ["Technology integration gaps", "Limited data analytics capability"],
        "typical_margin_pct": 32,
        "win_rate_against": 0.55,
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _win_rate():
    """Overall win rate from past proposals."""
    wins = sum(1 for p in PAST_PROPOSALS if p["result"] == "Won")
    return round(wins / len(PAST_PROPOSALS) * 100, 1)


def _avg_margin():
    """Average margin on won proposals."""
    won = [p for p in PAST_PROPOSALS if p["result"] == "Won"]
    if not won:
        return 0
    return round(sum(p["margin_pct"] for p in won) / len(won), 1)


def _top_win_themes():
    """Aggregate win themes from won proposals."""
    themes = {}
    for p in PAST_PROPOSALS:
        if p["result"] == "Won":
            for t in p["win_themes"]:
                themes[t] = themes.get(t, 0) + 1
    return sorted(themes.items(), key=lambda x: x[1], reverse=True)


def _pricing_breakdown(template_key, budget):
    """Generate a pricing breakdown from a template and budget."""
    tpl = PRICING_TEMPLATES.get(template_key, {})
    result = {}
    for key, pct in tpl.items():
        if key.endswith("_pct") and key not in ("margin_target_pct", "discount_threshold_pct"):
            label = key.replace("_pct", "").replace("_", " ").title()
            result[label] = round(budget * pct / 100, 2)
    return result


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class ProposalCopilotAgent(BasicAgent):
    """Generates competitive proposals with pricing and win-theme analysis."""

    def __init__(self):
        self.name = "ProposalCopilotAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "operations": [
                "generate_proposal",
                "pricing_model",
                "win_theme_analysis",
                "competitive_positioning",
            ],
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "generate_proposal")
        dispatch = {
            "generate_proposal": self._generate_proposal,
            "pricing_model": self._pricing_model,
            "win_theme_analysis": self._win_theme_analysis,
            "competitive_positioning": self._competitive_positioning,
        }
        handler = dispatch.get(operation)
        if handler is None:
            return f"**Error:** Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        return handler(**kwargs)

    # ------------------------------------------------------------------
    def _generate_proposal(self, **kwargs) -> str:
        lines = ["## Active RFP Pipeline\n"]
        for rfp_id, rfp in RFP_REQUIREMENTS.items():
            lines.append(f"### {rfp_id} -- {rfp['client']}: {rfp['title']}")
            lines.append(f"- **Budget:** ${rfp['budget']:,.0f}")
            lines.append(f"- **Timeline:** {rfp['timeline_months']} months")
            lines.append(f"- **Decision date:** {rfp['decision_date']}")
            lines.append(f"- **Decision makers:** {', '.join(rfp['decision_makers'])}")
            lines.append(f"- **Competitors:** {', '.join(rfp['competitors'])}")
            lines.append("\n**Scope areas:**")
            for area in rfp["scope_areas"]:
                lines.append(f"- {area}")
            lines.append("\n**Evaluation weights:**")
            lines.append("| Criterion | Weight |")
            lines.append("|-----------|--------|")
            for crit, weight in rfp["evaluation_criteria"].items():
                label = crit.replace("_", " ").title()
                lines.append(f"| {label} | {weight}% |")
            lines.append("")

        lines.append(f"\n**Our overall win rate:** {_win_rate()}%")
        lines.append(f"**Our average margin on wins:** {_avg_margin()}%")
        live = _live_pursuits()
        if live:
            seam = "n/a — enrichment seam"
            lines.append("\n### Live Tenant Pursuit Pipeline (open Dynamics opportunities)\n")
            lines.append("| Pursuit | Client | Budget | Stage | Win % | Decision Date | Eval Criteria | Competitors |")
            lines.append("|---------|--------|--------|-------|-------|---------------|---------------|-------------|")
            for p in live:
                win = f"{p['win_probability_pct']}%" if p["win_probability_pct"] is not None else seam
                lines.append(
                    f"| {p['name'][:40]} | {p['client'][:24]} | ${p['budget']:,.0f} | {p['stage']} | "
                    f"{win} | {p['decision_date']} | {p['evaluation_criteria'] or seam} | "
                    f"{p['competitors'] or seam} |"
                )
            live_total = sum(p["budget"] for p in live)
            lines.append(f"\n**Live open pipeline value:** ${live_total:,.0f} across {len(live)} pursuits")
        else:
            lines.append("\n_Live tenant unreachable — showing embedded demo RFPs only._")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _pricing_model(self, **kwargs) -> str:
        lines = ["## Pricing Models\n"]
        models = [
            ("RFP-2026-047", "digital_transformation", RFP_REQUIREMENTS["RFP-2026-047"]),
            ("RFP-2026-048", "clinical_optimization", RFP_REQUIREMENTS["RFP-2026-048"]),
        ]
        for rfp_id, tpl_key, rfp in models:
            breakdown = _pricing_breakdown(tpl_key, rfp["budget"])
            tpl = PRICING_TEMPLATES[tpl_key]
            our_price = round(rfp["budget"] * (100 - tpl["discount_threshold_pct"]) / 100)
            lines.append(f"### {rfp_id} -- {rfp['client']}")
            lines.append(f"- **Client budget:** ${rfp['budget']:,.0f}")
            lines.append(f"- **Our proposed price:** ${our_price:,.0f}")
            lines.append(f"- **Target margin:** {tpl['margin_target_pct']}%\n")
            lines.append("| Phase | Allocation |")
            lines.append("|-------|-----------|")
            for label, amount in breakdown.items():
                lines.append(f"| {label} | ${amount:,.0f} |")
            lines.append(f"| **Total** | **${our_price:,.0f}** |")
            lines.append(f"\n**Pricing advantage vs competitors:** ${rfp['budget'] - our_price:,.0f} below budget")
            lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _win_theme_analysis(self, **kwargs) -> str:
        lines = ["## Win Theme Analysis\n"]
        lines.append("### Historical Performance\n")
        lines.append("| Proposal | Value | Result | Margin | Themes |")
        lines.append("|----------|-------|--------|--------|--------|")
        for p in PAST_PROPOSALS:
            themes_str = "; ".join(p["win_themes"][:2])
            lines.append(
                f"| {p['rfp']} | ${p['value']:,.0f} | **{p['result']}** | {p['margin_pct']}% | {themes_str} |"
            )

        lines.append(f"\n**Win rate:** {_win_rate()}%")
        lines.append(f"**Average winning margin:** {_avg_margin()}%\n")

        top_themes = _top_win_themes()
        lines.append("### Top Win Themes (from won proposals)\n")
        lines.append("| Theme | Frequency |")
        lines.append("|-------|-----------|")
        for theme, count in top_themes:
            lines.append(f"| {theme} | {count} |")

        lines.append("\n### Loss Analysis\n")
        for p in PAST_PROPOSALS:
            if p["result"] == "Lost":
                lines.append(f"- **{p['rfp']}** (${p['value']:,.0f}): {p.get('loss_reason', 'Unknown')}")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _competitive_positioning(self, **kwargs) -> str:
        lines = ["## Competitive Positioning\n"]
        for comp, intel in COMPETITOR_INTEL.items():
            lines.append(f"### {comp}")
            lines.append(f"- **Our win rate against:** {intel['win_rate_against']*100:.0f}%")
            lines.append(f"- **Their price premium:** +{intel['avg_price_premium_pct']}% vs us")
            lines.append(f"- **Their typical margin:** {intel['typical_margin_pct']}%")
            lines.append("\n**Strengths to counter:**")
            for s in intel["strengths"]:
                lines.append(f"- {s}")
            lines.append("\n**Weaknesses to exploit:**")
            for w in intel["weaknesses"]:
                lines.append(f"- {w}")
            lines.append("")

        lines.append("### Positioning Summary\n")
        lines.append("| Competitor | Price Premium | Win Rate | Key Differentiator |")
        lines.append("|------------|-------------|----------|-------------------|")
        for comp, intel in COMPETITOR_INTEL.items():
            diff = intel["weaknesses"][0] if intel["weaknesses"] else "N/A"
            lines.append(
                f"| {comp} | +{intel['avg_price_premium_pct']}% | {intel['win_rate_against']*100:.0f}% | Target: {diff} |"
            )
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = ProposalCopilotAgent()
    print("=" * 72)
    print("EMBEDDED DEMO RFPS + LIVE TENANT PURSUIT PIPELINE")
    print("(live section fetched over HTTP; falls back offline)")
    print("=" * 72)
    print(agent.perform(operation="generate_proposal"))
    print()
    for op in agent.metadata["operations"][1:]:
        print("=" * 72)
        print(agent.perform(operation=op))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
