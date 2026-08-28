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
