---
name: "rar-aibast-agents-library-revenue-forecast"
description: "Builds weighted forecasts from live opportunities in a simulated Dynamics 365 tenant, with scenarios and an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/revenue_forecast", "rar_sha256": "e2d9ee1c1ed20bb5257500075b7c648689aa6869c87ba152d863827763fa71c7", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["b2b", "sales", "revenue-forecast", "deal-progression", "analytics"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/revenue_forecast`. The original RAPP
agent is preserved byte-for-byte in `revenue_forecast_agent.py` and in the RCI capsule.

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

Revenue Forecast Agent — a template you are meant to mutate.

Builds weighted revenue forecasts, scenario models (best/expected/worst),
commit-vs-best-case comparisons, and forecast accuracy reports for sales
leadership.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="quarterly_forecast") — the weighted forecast
     is computed from live open deals such as "Marigold Field Services —
     Mobile workstation expansion" (value x CRM close probability).
  2. No network? Everything falls back to the embedded demo layer below
     (_PIPELINE_DEALS / _HISTORICAL_ACCURACY) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     REVENUE_FORECAST_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_deal(). Quota and
     rep forecast overrides are enrichment seams — wire your sales-ops
     system there; accuracy history stays simulated until you do.

OPERATIONS
  quarterly_forecast | scenario_analysis | commit_vs_best_case
  | forecast_accuracy
  kwargs: operation (required)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The analysis to perform",
      "enum": [
        "quarterly_forecast",
        "scenario_analysis",
        "commit_vs_best_case",
        "forecast_accuracy"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `revenue_forecast_agent.py` and embedded as the fenced Python below (sha256 e2d9ee1c1ed20bb5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `revenue_forecast_agent.py` first:

```bash
python3 revenue_forecast_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 revenue_forecast_agent.py   # or on stdin
python3 revenue_forecast_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revenue Forecast Agent — a template you are meant to mutate.

Builds weighted revenue forecasts, scenario models (best/expected/worst),
commit-vs-best-case comparisons, and forecast accuracy reports for sales
leadership.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="quarterly_forecast") — the weighted forecast
     is computed from live open deals such as "Marigold Field Services —
     Mobile workstation expansion" (value x CRM close probability).
  2. No network? Everything falls back to the embedded demo layer below
     (_PIPELINE_DEALS / _HISTORICAL_ACCURACY) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     REVENUE_FORECAST_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_deal(). Quota and
     rep forecast overrides are enrichment seams — wire your sales-ops
     system there; accuracy history stays simulated until you do.

OPERATIONS
  quarterly_forecast | scenario_analysis | commit_vs_best_case
  | forecast_accuracy
  kwargs: operation (required)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request

# ===================================================================
# RAPP AGENT MANIFEST
# ===================================================================
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/revenue_forecast",
    "version": "1.1.0",
    "display_name": "Revenue Forecast",
    "description": "Builds weighted forecasts from live opportunities in a simulated Dynamics 365 tenant, with scenarios and an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "revenue-forecast", "deal-progression", "analytics"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ===================================================================
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export REVENUE_FORECAST_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_deal().
# ===================================================================

DATA_SOURCE_URL = os.environ.get(
    "REVENUE_FORECAST_DATA_URL",
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


_LIVE_STAGE_MAP = {"Qualify": "Qualification", "Develop": "Discovery",
                   "Propose": "Proposal", "Close": "Negotiation"}


def _forecast_category(probability_pct):
    """Derive a forecast category from CRM close probability (a rule you
    should tune to your own sales process)."""
    if probability_pct >= 70:
        return "commit"
    if probability_pct >= 50:
        return "best_case"
    if probability_pct >= 25:
        return "upside"
    return "pipeline"


def _normalize_live_deal(row):
    """Project a Dynamics opportunity onto the shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not knowable from the CRM alone' and the
    renderers label it an enrichment seam (forecast overrides live in your
    sales-ops system)."""
    prob_pct = int(row.get("closeprobability") or 0)
    return {
        "deal_id": str(row.get("opportunityid", ""))[:8],
        "name": row.get("name", "Unknown"),
        "value": int(float(row.get("estimatedvalue") or 0)),
        "stage": _LIVE_STAGE_MAP.get(row.get("stepname"), "Qualification"),
        "probability": prob_pct / 100,
        "close_date": str(row.get("estimatedclosedate") or "")[:10],
        "category": _forecast_category(prob_pct),
        "owner": row.get("owneridname", ""),
        "forecast_override": None,  # enrichment seam — wire sales-ops
        "_live": True,
    }


def _live_open_deals():
    """Live open opportunities normalized for this agent; [] when offline."""
    return [_normalize_live_deal(o) for o in _fetch_collection("opportunities")
            if o.get("statecode") == 0]


# ===================================================================
# EMBEDDED DEMO LAYER (offline fallback)
# ===================================================================

_PIPELINE_DEALS = {
    "TechCorp Industries": {"deal_id": "OPP-001", "value": 890000, "stage": "Proposal",
                            "probability": 0.35, "close_date": "2026-04-15", "category": "upside",
                            "owner": "Mike Chen", "forecast_override": None},
    "Global Manufacturing": {"deal_id": "OPP-002", "value": 720000, "stage": "Negotiation",
                             "probability": 0.55, "close_date": "2026-03-31", "category": "commit",
                             "owner": "Lisa Torres", "forecast_override": 720000},
    "Apex Financial": {"deal_id": "OPP-003", "value": 580000, "stage": "Discovery",
                       "probability": 0.20, "close_date": "2026-05-30", "category": "pipeline",
                       "owner": "James Park", "forecast_override": None},
    "Metro Healthcare": {"deal_id": "OPP-004", "value": 440000, "stage": "Proposal",
                         "probability": 0.45, "close_date": "2026-04-20", "category": "best_case",
                         "owner": "Mike Chen", "forecast_override": None},
    "Pacific Telecom": {"deal_id": "OPP-013", "value": 780000, "stage": "Negotiation",
                        "probability": 0.75, "close_date": "2026-03-28", "category": "commit",
                        "owner": "Lisa Torres", "forecast_override": 780000},
    "Pinnacle Logistics": {"deal_id": "OPP-005", "value": 360000, "stage": "Qualification",
                           "probability": 0.10, "close_date": "2026-06-15", "category": "pipeline",
                           "owner": "James Park", "forecast_override": None},
    "Northstar Aerospace": {"deal_id": "OPP-014", "value": 650000, "stage": "Proposal",
                            "probability": 0.50, "close_date": "2026-04-10", "category": "best_case",
                            "owner": "Mike Chen", "forecast_override": 650000},
    "DataFlow Corp": {"deal_id": "OPP-020", "value": 340000, "stage": "Contract",
                      "probability": 0.90, "close_date": "2026-03-22", "category": "commit",
                      "owner": "Lisa Torres", "forecast_override": 340000},
    "Beacon Financial": {"deal_id": "OPP-015", "value": 520000, "stage": "Discovery",
                         "probability": 0.25, "close_date": "2026-05-15", "category": "upside",
                         "owner": "James Park", "forecast_override": None},
    "Orion Software": {"deal_id": "OPP-023", "value": 420000, "stage": "Negotiation",
                       "probability": 0.65, "close_date": "2026-04-05", "category": "best_case",
                       "owner": "James Park", "forecast_override": 420000},
}

_HISTORICAL_ACCURACY = {
    "Q1_2025": {"forecast": 3200000, "actual": 3450000, "accuracy": 92.8, "variance_pct": 7.8},
    "Q2_2025": {"forecast": 3800000, "actual": 3620000, "accuracy": 95.3, "variance_pct": -4.7},
    "Q3_2025": {"forecast": 4100000, "actual": 4280000, "accuracy": 95.8, "variance_pct": 4.4},
    "Q4_2025": {"forecast": 4900000, "actual": 5100000, "accuracy": 96.1, "variance_pct": 4.1},
}

_SEASONAL_ADJUSTMENTS = {
    "Q1": 0.92,
    "Q2": 1.05,
    "Q3": 0.98,
    "Q4": 1.12,
}

_QUOTA = {
    "Q1_2026": 5200000,
    "team_size": 5,
    "per_rep": 1040000,
}


# ===================================================================
# HELPERS
# ===================================================================

def _weighted_forecast():
    """Calculate weighted pipeline forecast."""
    total = 0
    for deal in _PIPELINE_DEALS.values():
        total += deal["value"] * deal["probability"]
    return round(total)


def _category_totals():
    """Sum pipeline by forecast category."""
    cats = {"commit": 0, "best_case": 0, "upside": 0, "pipeline": 0}
    for deal in _PIPELINE_DEALS.values():
        cat = deal["category"]
        if cat in cats:
            cats[cat] += deal["value"]
    return cats


def _scenario_forecast(multiplier_map):
    """Run scenario with probability multipliers per category."""
    total = 0
    for deal in _PIPELINE_DEALS.values():
        mult = multiplier_map.get(deal["category"], deal["probability"])
        total += deal["value"] * mult
    return round(total)


# ===================================================================
# AGENT CLASS
# ===================================================================

class RevenueForecastAgent(BasicAgent):
    """
    Generates revenue forecasts and scenario analysis.

    Operations:
        quarterly_forecast   - weighted pipeline forecast for current quarter
        scenario_analysis    - best case, expected, and worst case scenarios
        commit_vs_best_case  - compare commit pipeline to best case projections
        forecast_accuracy    - historical accuracy and trend analysis
    """

    def __init__(self):
        self.name = "RevenueForecastAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["quarterly_forecast", "scenario_analysis", "commit_vs_best_case", "forecast_accuracy"],
                        "description": "The analysis to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "quarterly_forecast")
        dispatch = {
            "quarterly_forecast": self._quarterly_forecast,
            "scenario_analysis": self._scenario_analysis,
            "commit_vs_best_case": self._commit_vs_best_case,
            "forecast_accuracy": self._forecast_accuracy,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation '{op}'. Valid: {', '.join(dispatch.keys())}"
        return handler()

    # -- quarterly_forecast (flagship: prefers LIVE tenant, falls back) -
    def _quarterly_forecast(self) -> str:
        live = _live_open_deals()
        if live:
            weighted = round(sum(d["value"] * d["probability"] for d in live))
            total_pipeline = sum(d["value"] for d in live)
            cats = {"commit": 0, "best_case": 0, "upside": 0, "pipeline": 0}
            for d in live:
                cats[d["category"]] += d["value"]
            rows = ""
            for d in sorted(live, key=lambda x: -x["value"]):
                w = round(d["value"] * d["probability"])
                rows += (f"| {d['name']} | ${d['value']:,} | {d['stage']} | "
                         f"{d['probability']:.0%} | ${w:,} | {d['category']} | "
                         f"n/a — enrichment seam |\n")
            return (
                f"**Revenue Forecast — {len(live)} LIVE Open Deals** "
                f"(Static Dynamics 365 tenant)\n\n"
                f"| Metric | Value |\n"
                f"|--------|-------|\n"
                f"| Total Pipeline | ${total_pipeline:,} |\n"
                f"| Weighted Forecast | ${weighted:,} |\n"
                f"| Quota | n/a — enrichment seam (set your quota in your sales-ops system) |\n\n"
                f"**Category Breakdown** (derived from CRM close probability):\n"
                f"- Commit (>=70%): ${cats['commit']:,}\n"
                f"- Best Case (50-69%): ${cats['best_case']:,}\n"
                f"- Upside (25-49%): ${cats['upside']:,}\n"
                f"- Pipeline (<25%): ${cats['pipeline']:,}\n\n"
                f"**Deal-Level Forecast:**\n\n"
                f"| Deal | Value | Stage | Prob | Weighted | Category | Override |\n"
                f"|------|-------|-------|------|---------|----------|----------|\n"
                f"{rows}\n"
                f"Source: [Live Dynamics 365 opportunities]\n"
                f"Agents: ForecastEngine, PipelineAnalytics"
            )
        weighted = _weighted_forecast()
        cats = _category_totals()
        total_pipeline = sum(d["value"] for d in _PIPELINE_DEALS.values())
        quota = _QUOTA["Q1_2026"]
        attainment = round(weighted / max(quota, 1) * 100, 1)

        rows = ""
        for deal_name in sorted(_PIPELINE_DEALS.keys(), key=lambda d: -_PIPELINE_DEALS[d]["value"]):
            deal = _PIPELINE_DEALS[deal_name]
            w = round(deal["value"] * deal["probability"])
            override = f"${deal['forecast_override']:,}" if deal["forecast_override"] else "-"
            rows += (f"| {deal_name} | ${deal['value']:,} | {deal['stage']} | "
                     f"{deal['probability']:.0%} | ${w:,} | {deal['category']} | {override} |\n")

        seasonal = _SEASONAL_ADJUSTMENTS.get("Q1", 1.0)
        adjusted = round(weighted * seasonal)

        return (
            f"**Q1 2026 Revenue Forecast**\n\n"
            f"| Metric | Value |\n"
            f"|--------|-------|\n"
            f"| Total Pipeline | ${total_pipeline:,} |\n"
            f"| Weighted Forecast | ${weighted:,} |\n"
            f"| Seasonal Adjustment ({seasonal}x) | ${adjusted:,} |\n"
            f"| Quota | ${quota:,} |\n"
            f"| **Forecast Attainment** | **{attainment}%** |\n\n"
            f"**Category Breakdown:**\n"
            f"- Commit: ${cats['commit']:,}\n"
            f"- Best Case: ${cats['best_case']:,}\n"
            f"- Upside: ${cats['upside']:,}\n"
            f"- Pipeline: ${cats['pipeline']:,}\n\n"
            f"**Deal-Level Forecast:**\n\n"
            f"| Deal | Value | Stage | Prob | Weighted | Category | Override |\n"
            f"|------|-------|-------|------|---------|----------|----------|\n"
            f"{rows}\n"
            f"Source: [CRM Pipeline + Forecast Submissions]\n"
            f"Agents: ForecastEngine, PipelineAnalytics"
        )

    # -- scenario_analysis ---------------------------------------------
    def _scenario_analysis(self) -> str:
        best = _scenario_forecast({"commit": 0.95, "best_case": 0.80, "upside": 0.50, "pipeline": 0.25})
        expected = _scenario_forecast({"commit": 0.85, "best_case": 0.55, "upside": 0.25, "pipeline": 0.10})
        worst = _scenario_forecast({"commit": 0.70, "best_case": 0.30, "upside": 0.10, "pipeline": 0.05})
        quota = _QUOTA["Q1_2026"]

        scenarios = [
            ("Best Case", best, round(best / quota * 100, 1)),
            ("Expected", expected, round(expected / quota * 100, 1)),
            ("Worst Case", worst, round(worst / quota * 100, 1)),
        ]

        rows = ""
        for name, value, att in scenarios:
            gap = value - quota
            gap_str = f"+${gap:,}" if gap >= 0 else f"-${abs(gap):,}"
            rows += f"| {name} | ${value:,} | {att}% | {gap_str} |\n"

        at_risk_value = sum(d["value"] for d in _PIPELINE_DEALS.values()
                           if d["category"] in ("upside", "pipeline"))

        return (
            f"**Scenario Analysis -- Q1 2026**\n\n"
            f"Quota: ${quota:,}\n\n"
            f"| Scenario | Forecast | Attainment | Gap to Quota |\n"
            f"|----------|----------|-----------|-------------|\n"
            f"{rows}\n"
            f"**Scenario Assumptions:**\n"
            f"- Best Case: 95% of commit closes, 80% of best case, 50% of upside\n"
            f"- Expected: 85% of commit, 55% of best case, 25% of upside\n"
            f"- Worst Case: 70% of commit, 30% of best case, 10% of upside\n\n"
            f"**Risk Factors:**\n"
            f"- ${at_risk_value:,} in upside/pipeline categories (low confidence)\n"
            f"- 2 deals in commit category with legal/procurement delays\n"
            f"- Seasonal Q1 adjustment factor: {_SEASONAL_ADJUSTMENTS['Q1']}x\n\n"
            f"**Confidence Level:** Expected scenario has 72% confidence based on historical patterns.\n\n"
            f"Source: [Scenario Modeling + Historical Patterns]\n"
            f"Agents: ScenarioEngine"
        )

    # -- commit_vs_best_case -------------------------------------------
    def _commit_vs_best_case(self) -> str:
        commit_deals = {n: d for n, d in _PIPELINE_DEALS.items() if d["category"] == "commit"}
        best_case_deals = {n: d for n, d in _PIPELINE_DEALS.items() if d["category"] == "best_case"}

        commit_total = sum(d["value"] for d in commit_deals.values())
        best_total = sum(d["value"] for d in best_case_deals.values())
        combined = commit_total + best_total
        quota = _QUOTA["Q1_2026"]

        commit_rows = ""
        for name, d in sorted(commit_deals.items(), key=lambda x: -x[1]["value"]):
            commit_rows += f"| {name} | ${d['value']:,} | {d['stage']} | {d['probability']:.0%} | {d['close_date']} |\n"

        best_rows = ""
        for name, d in sorted(best_case_deals.items(), key=lambda x: -x[1]["value"]):
            best_rows += f"| {name} | ${d['value']:,} | {d['stage']} | {d['probability']:.0%} | {d['close_date']} |\n"

        gap_to_quota = quota - commit_total
        coverage = round(combined / max(quota, 1) * 100, 1)

        return (
            f"**Commit vs Best Case Analysis**\n\n"
            f"| Category | Value | % of Quota |\n"
            f"|----------|-------|----------|\n"
            f"| Commit | ${commit_total:,} | {round(commit_total / quota * 100, 1)}% |\n"
            f"| Best Case | ${best_total:,} | {round(best_total / quota * 100, 1)}% |\n"
            f"| **Combined** | **${combined:,}** | **{coverage}%** |\n"
            f"| Quota | ${quota:,} | 100% |\n"
            f"| Gap (Commit to Quota) | ${gap_to_quota:,} | |\n\n"
            f"**Commit Deals ({len(commit_deals)}):**\n\n"
            f"| Deal | Value | Stage | Probability | Close Date |\n"
            f"|------|-------|-------|-----------|------------|\n"
            f"{commit_rows}\n"
            f"**Best Case Deals ({len(best_case_deals)}):**\n\n"
            f"| Deal | Value | Stage | Probability | Close Date |\n"
            f"|------|-------|-------|-----------|------------|\n"
            f"{best_rows}\n"
            f"**Action Required:**\n"
            f"- Close gap of ${gap_to_quota:,} by converting best-case deals to commit\n"
            f"- Accelerate Northstar Aerospace and Orion Software through Negotiation\n"
            f"- Protect commit deals from slippage with weekly reviews\n\n"
            f"Source: [Forecast Submissions + CRM Data]\n"
            f"Agents: CommitAnalysisAgent"
        )

    # -- forecast_accuracy ---------------------------------------------
    def _forecast_accuracy(self) -> str:
        rows = ""
        accuracies = []
        for q, data in sorted(_HISTORICAL_ACCURACY.items()):
            variance_dir = "Over" if data["variance_pct"] > 0 else "Under"
            rows += (f"| {q.replace('_', ' ')} | ${data['forecast']:,} | ${data['actual']:,} | "
                     f"{data['accuracy']}% | {data['variance_pct']:+.1f}% ({variance_dir}) |\n")
            accuracies.append(data["accuracy"])

        avg_accuracy = round(sum(accuracies) / max(len(accuracies), 1), 1)
        improving = all(accuracies[i] <= accuracies[i + 1] for i in range(len(accuracies) - 1))
        trend = "Improving" if improving else "Mixed"

        weighted = _weighted_forecast()
        est_accuracy = min(avg_accuracy + 0.5, 98.0)
        low_range = round(weighted * (1 - (100 - est_accuracy) / 100))
        high_range = round(weighted * (1 + (100 - est_accuracy) / 100))

        return (
            f"**Forecast Accuracy Report**\n\n"
            f"4-Quarter avg accuracy: **{avg_accuracy}%** | Trend: **{trend}**\n\n"
            f"| Quarter | Forecast | Actual | Accuracy | Variance |\n"
            f"|---------|----------|--------|----------|----------|\n"
            f"{rows}\n"
            f"**Q1 2026 Confidence Range:**\n"
            f"- Weighted forecast: ${weighted:,}\n"
            f"- Expected accuracy: {est_accuracy}%\n"
            f"- Low estimate: ${low_range:,}\n"
            f"- High estimate: ${high_range:,}\n\n"
            f"**Accuracy Insights:**\n"
            f"- Consistent slight under-forecasting (avg +4.1% actual vs forecast)\n"
            f"- Commit category accuracy: 94% (most reliable)\n"
            f"- Best case conversion: 62% historically\n"
            f"- Upside conversion: 28% historically\n\n"
            f"**Recommendation:** Apply +4% upward adjustment to weighted forecast "
            f"based on historical under-forecasting pattern.\n\n"
            f"Source: [Historical Forecast Data + Actuals]\n"
            f"Agents: AccuracyTrackingEngine"
        )


if __name__ == "__main__":
    agent = RevenueForecastAgent()
    print("=" * 70)
    print("LIVE TENANT FORECAST (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="quarterly_forecast"))
    print()
    print("=" * 70)
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="scenario_analysis"))
    print()
    print("=" * 70)
    print(agent.perform(operation="forecast_accuracy"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
