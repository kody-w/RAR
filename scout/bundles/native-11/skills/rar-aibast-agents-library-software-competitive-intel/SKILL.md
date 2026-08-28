---
name: "rar-aibast-agents-library-software-competitive-intel"
description: "Maps market landscape and threats from a live simulated Dynamics 365 tenant's accounts and pipeline, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/software_competitive_intel", "rar_sha256": "962b38fd4f10ef48c6eb7a3e0076ccc0f7f53126e5e6dffa4da292bfc3721baa", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["competitive-intel", "market-analysis", "saas", "pricing", "threat-assessment"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/software_competitive_intel`. The original RAPP
agent is preserved byte-for-byte in `competitive_intel_agent.py` and in the RCI capsule.

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

Competitive Intelligence Agent — a template you are meant to mutate.

Provides competitive intelligence including market landscape analysis,
feature comparisons, pricing analysis, and threat assessments for SaaS
companies operating in competitive enterprise software markets.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM accounts and opportunities over
     real HTTP from the globally hosted Static Dynamics 365 tenant
     (Aster Lane Office Systems — synthetic data, no credentials, works
     from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="market_landscape")
     — with network up, the landscape is built from the tenant's 22 live
     accounts (e.g. Summit Trail Software) grouped by industry, with
     observed open-pipeline value per segment. In this template the
     competitive landscape is read from CRM accounts; market share and
     revenue stay enrichment seams.
  2. No network? Everything falls back to the embedded demo layer below
     (COMPETITORS) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SOFTWARE_COMPETITIVE_INTEL_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from Crayon/Klue), or
     replace _fetch_collection() with your own intel API. The fields the
     rest of the file needs are listed in _normalize_live_company() —
     market share, revenue, and growth stay "n/a — enrichment seam"
     until you wire your market-data provider.

OPERATIONS
  market_landscape | feature_comparison | pricing_analysis |
  threat_assessment
  kwargs: operation (required), competitor_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "competitor_id": {
      "description": "Optional competitor ID to filter results.",
      "type": "string"
    },
    "operation": {
      "description": "The competitive intelligence operation to perform.",
      "enum": [
        "market_landscape",
        "feature_comparison",
        "pricing_analysis",
        "threat_assessment"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `competitive_intel_agent.py` and embedded as the fenced Python below (sha256 962b38fd4f10ef48…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `competitive_intel_agent.py` first:

```bash
python3 competitive_intel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 competitive_intel_agent.py   # or on stdin
python3 competitive_intel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Competitive Intelligence Agent — a template you are meant to mutate.

Provides competitive intelligence including market landscape analysis,
feature comparisons, pricing analysis, and threat assessments for SaaS
companies operating in competitive enterprise software markets.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM accounts and opportunities over
     real HTTP from the globally hosted Static Dynamics 365 tenant
     (Aster Lane Office Systems — synthetic data, no credentials, works
     from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="market_landscape")
     — with network up, the landscape is built from the tenant's 22 live
     accounts (e.g. Summit Trail Software) grouped by industry, with
     observed open-pipeline value per segment. In this template the
     competitive landscape is read from CRM accounts; market share and
     revenue stay enrichment seams.
  2. No network? Everything falls back to the embedded demo layer below
     (COMPETITORS) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SOFTWARE_COMPETITIVE_INTEL_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from Crayon/Klue), or
     replace _fetch_collection() with your own intel API. The fields the
     rest of the file needs are listed in _normalize_live_company() —
     market share, revenue, and growth stay "n/a — enrichment seam"
     until you wire your market-data provider.

OPERATIONS
  market_landscape | feature_comparison | pricing_analysis |
  threat_assessment
  kwargs: operation (required), competitor_id
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/software_competitive_intel",
    "version": "1.1.0",
    "display_name": "Competitive Intelligence Agent",
    "description": "Maps market landscape and threats from a live simulated Dynamics 365 tenant's accounts and pipeline, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["competitive-intel", "market-analysis", "saas", "pricing", "threat-assessment"],
    "category": "software_digital_products",
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
#   export SOFTWARE_COMPETITIVE_INTEL_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your market-intel client.
# Downstream code only needs the fields from _normalize_live_company().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "SOFTWARE_COMPETITIVE_INTEL_DATA_URL",
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


def _normalize_live_company(row, opportunities):
    """Project a Dynamics account record onto the shape this agent uses —
    in this template the competitive landscape is read from CRM
    accounts. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not available from CRM
    alone' and the renderers label it as an enrichment seam."""
    name = row.get("name", "Unknown")
    open_pipeline = sum(
        float(o.get("estimatedvalue") or 0)
        for o in opportunities
        if name in (o.get("parentaccountidname"), o.get("customeridname"))
        and o.get("statecode") == 0
    )
    return {
        "name": name,
        "segment": row.get("industrycode", "Unknown"),
        "hq": f"{row.get('address1_city', '?')}, {row.get('address1_stateorprovince', '?')}",
        "primary_contact": row.get("primarycontactidname", ""),
        "open_pipeline": open_pipeline,
        "market_share_pct": None,  # enrichment seam — wire your market data
        "revenue_mm": None,        # enrichment seam
        "growth_rate_pct": None,   # enrichment seam
        "_live": True,
    }


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Synthetic domain data
# ---------------------------------------------------------------------------

COMPETITORS = {
    "COMP-001": {
        "name": "DataFlow AI",
        "segment": "Enterprise AI/ML Platform",
        "market_share_pct": 24.3,
        "revenue_mm": 312.0,
        "growth_rate_pct": 41.2,
        "founded_year": 2017,
        "headcount": 1420,
        "funding_mm": 285.0,
        "hq": "San Francisco, CA",
        "features": {
            "automl": True,
            "no_code_ui": True,
            "model_monitoring": True,
            "explainability": False,
            "on_prem_deploy": False,
            "soc2": True,
            "hipaa": False,
            "fedramp": False,
        },
        "pricing_tiers": {
            "starter": 999,
            "professional": 2999,
            "enterprise": 4999,
        },
        "recent_moves": [
            "Launched AutoML 3.0 with 25% price cut",
            "AWS Marketplace native listing",
            "340 new mid-market customers in Q1",
        ],
        "threat_level": "high",
    },
    "COMP-002": {
        "name": "NeuralStack",
        "segment": "Vertical AI Solutions",
        "market_share_pct": 15.8,
        "revenue_mm": 198.0,
        "growth_rate_pct": 28.5,
        "founded_year": 2018,
        "headcount": 870,
        "funding_mm": 195.0,
        "hq": "Boston, MA",
        "features": {
            "automl": True,
            "no_code_ui": False,
            "model_monitoring": True,
            "explainability": True,
            "on_prem_deploy": True,
            "soc2": True,
            "hipaa": True,
            "fedramp": False,
        },
        "pricing_tiers": {
            "starter": 1299,
            "professional": 3299,
            "enterprise": 5999,
        },
        "recent_moves": [
            "Expanded into healthcare vertical",
            "Suffered 4-hour production outage",
            "Acquired NLP startup for $32M",
        ],
        "threat_level": "medium",
    },
    "COMP-003": {
        "name": "Quantum ML",
        "segment": "Open Core ML Platform",
        "market_share_pct": 11.2,
        "revenue_mm": 142.0,
        "growth_rate_pct": 55.8,
        "founded_year": 2019,
        "headcount": 540,
        "funding_mm": 120.0,
        "hq": "Austin, TX",
        "features": {
            "automl": True,
            "no_code_ui": True,
            "model_monitoring": False,
            "explainability": True,
            "on_prem_deploy": True,
            "soc2": False,
            "hipaa": False,
            "fedramp": False,
        },
        "pricing_tiers": {
            "starter": 0,
            "professional": 1999,
            "enterprise": 3999,
        },
        "recent_moves": [
            "Open-sourced core inference engine",
            "Rapid fintech vertical growth",
            "Community reached 48K developers",
        ],
        "threat_level": "medium",
    },
}

OUR_COMPANY = {
    "name": "IntelliStack Technologies",
    "market_share_pct": 18.0,
    "revenue_mm": 228.0,
    "growth_rate_pct": 32.0,
    "features": {
        "automl": True,
        "no_code_ui": False,
        "model_monitoring": True,
        "explainability": True,
        "on_prem_deploy": True,
        "soc2": True,
        "hipaa": True,
        "fedramp": True,
    },
    "pricing_tiers": {
        "starter": 1499,
        "professional": 3499,
        "enterprise": 6999,
    },
    "model_accuracy_pct": 94.2,
    "avg_deal_size": 127000,
    "enterprise_win_rate_pct": 67,
    "midmarket_win_rate_pct": 31,
    "overall_win_rate_pct": 38,
    "data_residency_regions": 12,
}

PRODUCT_ROADMAPS = {
    "COMP-001": [
        {"initiative": "Enterprise SSO integration", "quarter": "Q2 2026", "impact": "high"},
        {"initiative": "On-prem deployment option", "quarter": "Q3 2026", "impact": "high"},
        {"initiative": "Model versioning 2.0", "quarter": "Q2 2026", "impact": "medium"},
    ],
    "COMP-002": [
        {"initiative": "Financial services vertical", "quarter": "Q2 2026", "impact": "medium"},
        {"initiative": "Real-time inference API", "quarter": "Q3 2026", "impact": "high"},
        {"initiative": "Automated compliance reports", "quarter": "Q4 2026", "impact": "medium"},
    ],
    "COMP-003": [
        {"initiative": "SOC2 certification", "quarter": "Q2 2026", "impact": "high"},
        {"initiative": "Managed cloud offering", "quarter": "Q3 2026", "impact": "high"},
        {"initiative": "Plugin marketplace", "quarter": "Q2 2026", "impact": "medium"},
    ],
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _compute_market_landscape():
    """Build market landscape summary from competitor data."""
    total_market = sum(c["revenue_mm"] for c in COMPETITORS.values()) + OUR_COMPANY["revenue_mm"]
    players = []
    for cid, comp in COMPETITORS.items():
        players.append({
            "id": cid,
            "name": comp["name"],
            "market_share_pct": comp["market_share_pct"],
            "revenue_mm": comp["revenue_mm"],
            "growth_rate_pct": comp["growth_rate_pct"],
            "threat_level": comp["threat_level"],
            "recent_moves": comp["recent_moves"],
        })
    players.sort(key=lambda x: x["market_share_pct"], reverse=True)
    return {
        "total_addressable_market_mm": round(total_market / 0.692, 1),
        "our_position": 2,
        "our_share_pct": OUR_COMPANY["market_share_pct"],
        "competitors": players,
    }


def _compute_feature_comparison():
    """Build feature-by-feature comparison grid."""
    feature_labels = {
        "automl": "AutoML",
        "no_code_ui": "No-Code UI",
        "model_monitoring": "Model Monitoring",
        "explainability": "Explainability",
        "on_prem_deploy": "On-Prem Deployment",
        "soc2": "SOC2 Type II",
        "hipaa": "HIPAA Compliance",
        "fedramp": "FedRAMP Authorization",
    }
    rows = []
    for key, label in feature_labels.items():
        row = {"feature": label, "us": OUR_COMPANY["features"].get(key, False)}
        for cid, comp in COMPETITORS.items():
            row[comp["name"]] = comp["features"].get(key, False)
        rows.append(row)
    our_count = sum(1 for v in OUR_COMPANY["features"].values() if v)
    comp_counts = {}
    for cid, comp in COMPETITORS.items():
        comp_counts[comp["name"]] = sum(1 for v in comp["features"].values() if v)
    return {"features": rows, "our_feature_count": our_count, "competitor_counts": comp_counts}


def _compute_pricing_analysis():
    """Compute pricing gaps across tiers."""
    analysis = []
    for tier in ["starter", "professional", "enterprise"]:
        our_price = OUR_COMPANY["pricing_tiers"][tier]
        for cid, comp in COMPETITORS.items():
            their_price = comp["pricing_tiers"][tier]
            gap_pct = round(((our_price - their_price) / their_price) * 100, 1) if their_price > 0 else 0
            analysis.append({
                "tier": tier,
                "competitor": comp["name"],
                "our_price": our_price,
                "their_price": their_price,
                "gap_pct": gap_pct,
            })
    avg_gap = round(sum(a["gap_pct"] for a in analysis) / len(analysis), 1)
    return {"tier_comparison": analysis, "average_gap_pct": avg_gap}


def _compute_threat_assessment():
    """Assess threat level and strategic recommendations per competitor."""
    assessments = []
    for cid, comp in COMPETITORS.items():
        roadmap = PRODUCT_ROADMAPS.get(cid, [])
        high_impact_items = [r for r in roadmap if r["impact"] == "high"]
        assessments.append({
            "competitor": comp["name"],
            "threat_level": comp["threat_level"],
            "market_share_pct": comp["market_share_pct"],
            "growth_rate_pct": comp["growth_rate_pct"],
            "roadmap_high_impact_count": len(high_impact_items),
            "roadmap_items": roadmap,
            "recent_moves": comp["recent_moves"],
        })
    assessments.sort(key=lambda x: x["growth_rate_pct"], reverse=True)
    return {"assessments": assessments, "highest_threat": "DataFlow AI"}


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class CompetitiveIntelAgent(BasicAgent):
    """Competitive intelligence agent for SaaS market analysis."""

    def __init__(self):
        self.name = "CompetitiveIntelAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "market_landscape",
                            "feature_comparison",
                            "pricing_analysis",
                            "threat_assessment",
                        ],
                        "description": "The competitive intelligence operation to perform.",
                    },
                    "competitor_id": {
                        "type": "string",
                        "description": "Optional competitor ID to filter results.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "market_landscape")
        if operation == "market_landscape":
            return self._market_landscape(kwargs.get("competitor_id"))
        elif operation == "feature_comparison":
            return self._feature_comparison()
        elif operation == "pricing_analysis":
            return self._pricing_analysis()
        elif operation == "threat_assessment":
            return self._threat_assessment()
        return f"**Error:** Unknown operation `{operation}`."

    # ------------------------------------------------------------------
    def _live_market_landscape(self, companies):
        """Landscape built from live tenant accounts (preferred online)."""
        segments = {}
        for c in companies:
            seg = segments.setdefault(
                c["segment"], {"accounts": 0, "pipeline": 0.0}
            )
            seg["accounts"] += 1
            seg["pipeline"] += c["open_pipeline"]
        lines = [
            "# Competitive Market Landscape — Live Tenant Accounts",
            "",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "In this template the landscape is read from CRM accounts. Pass",
            "`competitor_id` (e.g. COMP-001) for the embedded demo view.",
            "",
            f"**Companies tracked:** {len(companies)} across {len(segments)} segments",
            "",
            "| Segment | Companies | Observed Open Pipeline | Market Share |",
            "|---------|-----------|------------------------|--------------|",
        ]
        for seg, data in sorted(
            segments.items(), key=lambda kv: kv[1]["pipeline"], reverse=True
        ):
            lines.append(
                f"| {seg} | {data['accounts']} | ${data['pipeline']:,.0f} "
                f"| n/a — enrichment seam |"
            )
        watchlist = [
            c for c in companies
            if any(t in str(c["segment"]) for t in ("Software", "Technology"))
        ]
        if watchlist:
            lines.append("")
            lines.append("## Software Segment Watchlist")
            lines.append("")
            lines.append("| Company | HQ | Primary Contact | Open Pipeline | Revenue | Growth |")
            lines.append("|---------|----|-----------------|---------------|---------|--------|")
            for c in sorted(watchlist, key=lambda x: x["name"]):
                lines.append(
                    f"| {c['name']} | {c['hq']} | {c['primary_contact']} "
                    f"| ${c['open_pipeline']:,.0f} "
                    f"| n/a — enrichment seam | n/a — enrichment seam |"
                )
        lines.append("")
        lines.append(
            "Market share, revenue, and growth need your market-data provider "
            "— wire it at the LIVE DATA SEAM."
        )
        return "\n".join(lines)

    def _market_landscape(self, competitor_id=None) -> str:
        if not competitor_id:
            rows = _fetch_collection("accounts")
            if rows:
                opportunities = _fetch_collection("opportunities")
                companies = [
                    _normalize_live_company(r, opportunities)
                    for r in rows if r.get("name")
                ]
                if companies:
                    return self._live_market_landscape(companies)
        data = _compute_market_landscape()
        lines = [
            "# Competitive Market Landscape",
            "",
            f"**Total Addressable Market:** ${data['total_addressable_market_mm']:.0f}M",
            f"**Our Position:** #{data['our_position']} with {data['our_share_pct']}% share",
            "",
            "| Rank | Competitor | Share | Revenue | Growth | Threat |",
            "|------|-----------|-------|---------|--------|--------|",
        ]
        for i, c in enumerate(data["competitors"], 1):
            threat_icon = "HIGH" if c["threat_level"] == "high" else "MED"
            lines.append(
                f"| {i} | {c['name']} | {c['market_share_pct']}% | ${c['revenue_mm']:.0f}M "
                f"| {c['growth_rate_pct']}% | {threat_icon} |"
            )
        lines.append("")
        lines.append("## Recent Competitor Moves")
        for c in data["competitors"]:
            lines.append(f"\n**{c['name']}**")
            for move in c["recent_moves"]:
                lines.append(f"- {move}")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _feature_comparison(self) -> str:
        data = _compute_feature_comparison()
        comp_names = [c["name"] for c in COMPETITORS.values()]
        header = "| Feature | Us | " + " | ".join(comp_names) + " |"
        sep = "|---------|----| " + " | ".join(["---"] * len(comp_names)) + " |"
        lines = ["# Feature Comparison Matrix", "", header, sep]
        for row in data["features"]:
            us_val = "YES" if row["us"] else "NO"
            cells = [us_val]
            for cn in comp_names:
                cells.append("YES" if row.get(cn, False) else "NO")
            lines.append(f"| {row['feature']} | " + " | ".join(cells) + " |")
        lines.append("")
        lines.append(f"**Our Feature Coverage:** {data['our_feature_count']}/8")
        for name, count in data["competitor_counts"].items():
            lines.append(f"- {name}: {count}/8")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _pricing_analysis(self) -> str:
        data = _compute_pricing_analysis()
        lines = [
            "# Pricing Analysis",
            "",
            f"**Average Price Gap:** {data['average_gap_pct']}% above competitors",
            "",
            "| Tier | Competitor | Our Price | Their Price | Gap |",
            "|------|-----------|-----------|-------------|-----|",
        ]
        for row in data["tier_comparison"]:
            lines.append(
                f"| {row['tier'].title()} | {row['competitor']} "
                f"| ${row['our_price']:,}/mo | ${row['their_price']:,}/mo | {row['gap_pct']:+.1f}% |"
            )
        lines.append("")
        lines.append("## Recommendations")
        lines.append("- Consider matching enterprise tier pricing to defend large accounts.")
        lines.append("- Evaluate a free/community tier to compete with open-core entrants.")
        lines.append("- Emphasize compliance value to justify premium in regulated verticals.")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _threat_assessment(self) -> str:
        data = _compute_threat_assessment()
        lines = [
            "# Threat Assessment",
            "",
            f"**Highest Overall Threat:** {data['highest_threat']}",
            "",
        ]
        for a in data["assessments"]:
            level_label = "HIGH" if a["threat_level"] == "high" else "MEDIUM"
            lines.append(f"## {a['competitor']} [{level_label}]")
            lines.append(f"- Market Share: {a['market_share_pct']}%")
            lines.append(f"- Growth Rate: {a['growth_rate_pct']}%")
            lines.append(f"- High-Impact Roadmap Items: {a['roadmap_high_impact_count']}")
            lines.append("")
            lines.append("**Roadmap:**")
            for item in a["roadmap_items"]:
                lines.append(f"- [{item['quarter']}] {item['initiative']} (impact: {item['impact']})")
            lines.append("")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = CompetitiveIntelAgent()
    print("=" * 60)
    print("EMBEDDED DEMO LANDSCAPE (works offline)")
    print(agent.perform(operation="market_landscape", competitor_id="COMP-001"))
    print("\n" + "=" * 60)
    print("LIVE TENANT LANDSCAPE (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="market_landscape"))
    ops = ["feature_comparison", "pricing_analysis", "threat_assessment"]
    for op in ops:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        result = agent.perform(operation=op)
        print(result)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
