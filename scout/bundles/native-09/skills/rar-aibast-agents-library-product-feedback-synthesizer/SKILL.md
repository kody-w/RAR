---
name: "rar-aibast-agents-library-product-feedback-synthesizer"
description: "Synthesizes feedback themes from a live simulated Dynamics 365 tenant's cases and emails, with an offline demo fallback; writes simulated."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/product_feedback_synthesizer", "rar_sha256": "92333a27ab814748b8e39d8132396b0874eee15f045ad777c1048e368bc83aae", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["feedback", "product", "feature-requests", "sentiment", "roadmap", "nps"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/product_feedback_synthesizer`. The original RAPP
agent is preserved byte-for-byte in `product_feedback_synthesizer_agent.py` and in the RCI capsule.

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

Product Feedback Synthesizer Agent — a template you are meant to mutate.

Aggregates and synthesizes customer feedback, feature requests, sentiment
analysis, and roadmap impact assessments for product management teams.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live feedback signals over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="feedback_summary")
     — with network up, the summary synthesizes the tenant's 38 live
     service cases (e.g. CAS-260113 "Desk assembly guide has unclear
     step") and 60 live emails into themes by case type and channel. In
     this template a piece of product feedback is represented as a
     Dynamics case, and the inbound email stream as Dynamics emails.
  2. No network? Everything falls back to the embedded demo layer below
     (FEEDBACK_ENTRIES / FEATURE_REQUESTS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PRODUCT_FEEDBACK_SYNTHESIZER_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from Productboard/Canny),
     or replace _fetch_collection() with your own feedback API. The
     fields the rest of the file needs are listed in
     _normalize_live_feedback() — sentiment scores and ARR stay
     "n/a — enrichment seam" until you wire your NPS/billing systems.

OPERATIONS
  feedback_summary | feature_requests | sentiment_analysis |
  roadmap_impact | pain_point_analysis | risk_alerts |
  activate_roadmap_action
  kwargs: operation (required), feature_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "feature_id": {
      "description": "Exact feature request ID for roadmap activation.",
      "type": "string"
    },
    "operation": {
      "description": "The feedback operation to perform.",
      "enum": [
        "feedback_summary",
        "feature_requests",
        "sentiment_analysis",
        "roadmap_impact",
        "pain_point_analysis",
        "risk_alerts",
        "activate_roadmap_action"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `product_feedback_synthesizer_agent.py` and embedded as the fenced Python below (sha256 92333a27ab814748…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `product_feedback_synthesizer_agent.py` first:

```bash
python3 product_feedback_synthesizer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 product_feedback_synthesizer_agent.py   # or on stdin
python3 product_feedback_synthesizer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Product Feedback Synthesizer Agent — a template you are meant to mutate.

Aggregates and synthesizes customer feedback, feature requests, sentiment
analysis, and roadmap impact assessments for product management teams.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live feedback signals over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="feedback_summary")
     — with network up, the summary synthesizes the tenant's 38 live
     service cases (e.g. CAS-260113 "Desk assembly guide has unclear
     step") and 60 live emails into themes by case type and channel. In
     this template a piece of product feedback is represented as a
     Dynamics case, and the inbound email stream as Dynamics emails.
  2. No network? Everything falls back to the embedded demo layer below
     (FEEDBACK_ENTRIES / FEATURE_REQUESTS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PRODUCT_FEEDBACK_SYNTHESIZER_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from Productboard/Canny),
     or replace _fetch_collection() with your own feedback API. The
     fields the rest of the file needs are listed in
     _normalize_live_feedback() — sentiment scores and ARR stay
     "n/a — enrichment seam" until you wire your NPS/billing systems.

OPERATIONS
  feedback_summary | feature_requests | sentiment_analysis |
  roadmap_impact | pain_point_analysis | risk_alerts |
  activate_roadmap_action
  kwargs: operation (required), feature_id
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/product_feedback_synthesizer",
    "version": "1.2.0",
    "display_name": "Product Feedback Synthesizer Agent",
    "description": "Synthesizes feedback themes from a live simulated Dynamics 365 tenant's cases and emails, with an offline demo fallback; writes simulated.",
    "author": "AIBAST",
    "tags": ["feedback", "product", "feature-requests", "sentiment", "roadmap", "nps"],
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
#   export PRODUCT_FEEDBACK_SYNTHESIZER_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your feedback-platform client.
# Downstream code only needs the fields from _normalize_live_feedback().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "PRODUCT_FEEDBACK_SYNTHESIZER_DATA_URL",
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


def _normalize_live_feedback(row):
    """Project a Dynamics case (incident) record onto the shape this agent
    uses — in this template a piece of product feedback IS a Dynamics
    case (inbound email volume comes from Dynamics emails). THIS is the
    contract your replacement data source must meet — a dict with these
    keys. None means 'not available from the service desk alone' and
    the renderers label it as an enrichment seam."""
    return {
        "feedback_id": row.get("ticketnumber", row.get("incidentid", "")),
        "customer": row.get("customeridname", "Unknown"),
        "summary": row.get("title", "untitled"),
        "theme": row.get(
            "casetypecode@OData.Community.Display.V1.FormattedValue", "General"
        ),
        "channel": row.get(
            "caseorigincode@OData.Community.Display.V1.FormattedValue", "Unknown"
        ),
        "priority": row.get(
            "prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"
        ),
        "open": row.get("statecode") == 0,
        "age_days": _age_days(row.get("createdon")),
        "sentiment_score": None,  # enrichment seam — wire your NPS platform
        "arr": None,              # enrichment seam — wire your billing system
        "_live": True,
    }


def _age_days(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Synthetic domain data
# ---------------------------------------------------------------------------

FEEDBACK_ENTRIES = {
    "FB-5001": {
        "customer": "Meridian Healthcare Systems",
        "channel": "support_ticket",
        "date": "2026-02-14",
        "category": "usability",
        "sentiment": "negative",
        "score": 2,
        "text": "The dashboard takes too many clicks to get to key metrics. We need a customizable home view.",
        "arr_impact": 186000,
    },
    "FB-5002": {
        "customer": "Apex Financial Group",
        "channel": "nps_survey",
        "date": "2026-02-20",
        "category": "feature_gap",
        "sentiment": "neutral",
        "score": 6,
        "text": "Product is solid but missing real-time alerting capabilities that competitors offer.",
        "arr_impact": 240000,
    },
    "FB-5003": {
        "customer": "Skyline Hospitality Group",
        "channel": "qbr",
        "date": "2026-03-01",
        "category": "praise",
        "sentiment": "positive",
        "score": 9,
        "text": "Integration with our POS system has been seamless. Would love to see mobile app improvements.",
        "arr_impact": 360000,
    },
    "FB-5004": {
        "customer": "Vanguard Logistics",
        "channel": "support_ticket",
        "date": "2026-01-28",
        "category": "bug_report",
        "sentiment": "negative",
        "score": 1,
        "text": "Data export fails consistently for reports over 10K rows. This is blocking our migration.",
        "arr_impact": 84000,
    },
    "FB-5005": {
        "customer": "BrightPath Education",
        "channel": "in_app",
        "date": "2026-03-05",
        "category": "feature_gap",
        "sentiment": "neutral",
        "score": 5,
        "text": "Need role-based access controls for student data. Currently everyone sees everything.",
        "arr_impact": 96000,
    },
    "FB-5006": {
        "customer": "Orion Manufacturing",
        "channel": "sales_call",
        "date": "2026-03-10",
        "category": "feature_gap",
        "sentiment": "positive",
        "score": 8,
        "text": "Great product overall. If you add workflow automation we would double our seat count.",
        "arr_impact": 312000,
    },
}

FEATURE_REQUESTS = {
    "FR-001": {
        "title": "Customizable Dashboard Home View",
        "votes": 87,
        "arr_weight": 612000,
        "status": "under_review",
        "effort": "medium",
        "category": "usability",
        "linked_feedback": ["FB-5001"],
    },
    "FR-002": {
        "title": "Real-Time Alerting Engine",
        "votes": 134,
        "arr_weight": 780000,
        "status": "planned_q3",
        "effort": "high",
        "category": "feature_gap",
        "linked_feedback": ["FB-5002"],
    },
    "FR-003": {
        "title": "Mobile App Enhancements",
        "votes": 62,
        "arr_weight": 420000,
        "status": "in_progress",
        "effort": "medium",
        "category": "usability",
        "linked_feedback": ["FB-5003"],
    },
    "FR-004": {
        "title": "Large Dataset Export Fix",
        "votes": 41,
        "arr_weight": 264000,
        "status": "in_progress",
        "effort": "low",
        "category": "bug_fix",
        "linked_feedback": ["FB-5004"],
    },
    "FR-005": {
        "title": "Role-Based Access Controls (RBAC)",
        "votes": 156,
        "arr_weight": 960000,
        "status": "planned_q2",
        "effort": "high",
        "category": "security",
        "linked_feedback": ["FB-5005"],
    },
    "FR-006": {
        "title": "Workflow Automation Builder",
        "votes": 203,
        "arr_weight": 1140000,
        "status": "planned_q3",
        "effort": "high",
        "category": "feature_gap",
        "linked_feedback": ["FB-5006"],
    },
}

NPS_SCORES = {
    "2025-Q4": {"promoters": 142, "passives": 88, "detractors": 45, "score": 35},
    "2026-Q1": {"promoters": 158, "passives": 91, "detractors": 51, "score": 36},
}

EVIDENCE_ACTIONS = {
    "FR-001": {
        "pain_point": "Too many clicks to reach key metrics",
        "theme": "Customizable experience",
        "frequency": 87,
        "severity": 4,
        "retention_impact": "medium",
        "competitive_gap": "Competitors offer configurable home views",
        "jira_project": "PRODUCT",
        "teams_channel": "Product Feedback Triage",
    },
    "FR-002": {
        "pain_point": "Missing real-time alerting",
        "theme": "Proactive monitoring",
        "frequency": 134,
        "severity": 5,
        "retention_impact": "high",
        "competitive_gap": "Alerting is available in competing products",
        "jira_project": "PLATFORM",
        "teams_channel": "Product and Engineering",
    },
    "FR-003": {
        "pain_point": "Mobile workflows lag the web experience",
        "theme": "Mobile productivity",
        "frequency": 62,
        "severity": 3,
        "retention_impact": "medium",
        "competitive_gap": "Mobile parity is becoming a buying criterion",
        "jira_project": "MOBILE",
        "teams_channel": "Mobile Experience",
    },
    "FR-004": {
        "pain_point": "Exports fail above 10,000 rows",
        "theme": "Reliability at scale",
        "frequency": 41,
        "severity": 5,
        "retention_impact": "high",
        "competitive_gap": "Reliable large exports are required for migrations",
        "jira_project": "DATA",
        "teams_channel": "Data Reliability",
    },
    "FR-005": {
        "pain_point": "Student data lacks role-based access controls",
        "theme": "Enterprise security",
        "frequency": 156,
        "severity": 5,
        "retention_impact": "critical",
        "competitive_gap": "Enterprise competitors include granular RBAC",
        "jira_project": "SECURITY",
        "teams_channel": "Security and Product",
    },
    "FR-006": {
        "pain_point": "Teams cannot automate repeatable workflows",
        "theme": "Workflow automation",
        "frequency": 203,
        "severity": 4,
        "retention_impact": "high",
        "competitive_gap": "Competitor automation is blocking expansion",
        "jira_project": "AUTOMATION",
        "teams_channel": "Automation Roadmap",
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _exact_feature(feature_id):
    if not feature_id:
        return None, "Provide an exact feature_id: " + ", ".join(sorted(FEATURE_REQUESTS))
    if feature_id not in FEATURE_REQUESTS:
        return None, f"Unknown feature_id `{feature_id}`; exact ID required."
    return FEATURE_REQUESTS[feature_id], None

def _feedback_summary():
    by_sentiment = {"positive": 0, "neutral": 0, "negative": 0}
    by_category = {}
    by_channel = {}
    total_arr = 0
    for fb in FEEDBACK_ENTRIES.values():
        by_sentiment[fb["sentiment"]] += 1
        by_category[fb["category"]] = by_category.get(fb["category"], 0) + 1
        by_channel[fb["channel"]] = by_channel.get(fb["channel"], 0) + 1
        total_arr += fb["arr_impact"]
    avg_score = round(sum(fb["score"] for fb in FEEDBACK_ENTRIES.values()) / len(FEEDBACK_ENTRIES), 1)
    return {
        "total_entries": len(FEEDBACK_ENTRIES),
        "by_sentiment": by_sentiment,
        "by_category": by_category,
        "by_channel": by_channel,
        "avg_score": avg_score,
        "total_arr_represented": total_arr,
    }


def _feature_request_ranking():
    ranked = sorted(FEATURE_REQUESTS.values(), key=lambda x: x["arr_weight"], reverse=True)
    return {"requests": ranked, "total_requests": len(ranked)}


def _sentiment_analysis():
    results = []
    for fid, fb in FEEDBACK_ENTRIES.items():
        results.append({
            "id": fid, "customer": fb["customer"], "sentiment": fb["sentiment"],
            "score": fb["score"], "category": fb["category"], "channel": fb["channel"],
            "excerpt": fb["text"][:80],
        })
    pos = sum(1 for r in results if r["sentiment"] == "positive")
    neg = sum(1 for r in results if r["sentiment"] == "negative")
    return {"entries": results, "positive_pct": round(pos / len(results) * 100, 1),
            "negative_pct": round(neg / len(results) * 100, 1), "nps_trend": NPS_SCORES}


def _roadmap_impact():
    impacts = []
    for frid, fr in FEATURE_REQUESTS.items():
        impacts.append({
            "id": frid, "title": fr["title"], "votes": fr["votes"],
            "arr_weight": fr["arr_weight"], "effort": fr["effort"],
            "status": fr["status"], "category": fr["category"],
            "priority_score": round(fr["arr_weight"] / 1000 / (3 if fr["effort"] == "high" else 2 if fr["effort"] == "medium" else 1), 1),
        })
    impacts.sort(key=lambda x: x["priority_score"], reverse=True)
    return {"items": impacts}


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class ProductFeedbackSynthesizerAgent(BasicAgent):
    """Product feedback synthesis and roadmap impact agent."""

    def __init__(self):
        self.name = "ProductFeedbackSynthesizerAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "feedback_summary",
                            "feature_requests",
                            "sentiment_analysis",
                            "roadmap_impact",
                            "pain_point_analysis",
                            "risk_alerts",
                            "activate_roadmap_action",
                        ],
                        "description": "The feedback operation to perform.",
                    },
                    "feature_id": {
                        "type": "string",
                        "description": "Exact feature request ID for roadmap activation.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "feedback_summary")
        if op == "feedback_summary":
            return self._feedback_summary(kwargs.get("feature_id"))
        elif op == "feature_requests":
            return self._feature_requests()
        elif op == "sentiment_analysis":
            return self._sentiment_analysis()
        elif op == "roadmap_impact":
            return self._roadmap_impact()
        elif op == "pain_point_analysis":
            return self._pain_point_analysis()
        elif op == "risk_alerts":
            return self._risk_alerts()
        elif op == "activate_roadmap_action":
            return self._activate_roadmap_action(kwargs.get("feature_id"))
        return f"**Error:** Unknown operation `{op}`."

    def _live_feedback_summary(self, feedback):
        """Feedback synthesis from live tenant cases (preferred online)."""
        emails = _fetch_collection("emails")
        inbound = [e for e in emails if e.get("directioncode") is False]
        themes, channels = {}, {}
        for f in feedback:
            themes.setdefault(f["theme"], []).append(f)
            channels[f["channel"]] = channels.get(f["channel"], 0) + 1
        lines = [
            "# Product Feedback Summary — Live Tenant Signals",
            "",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "In this template a piece of feedback is a Dynamics case and the",
            "inbound stream is Dynamics email activity.",
            "",
            f"**Feedback entries (live cases):** {len(feedback)} "
            f"({sum(1 for f in feedback if f['open'])} open)",
            f"**Inbound email volume:** {len(inbound)} of {len(emails)} messages",
            "**Avg Satisfaction Score:** n/a — enrichment seam (wire your NPS platform)",
            "**ARR Represented:** n/a — enrichment seam (wire your billing system)",
            "",
            "## Themes (by case type)",
            "",
            "| Theme | Count | Sample Feedback |",
            "|-------|-------|-----------------|",
        ]
        for theme, items in sorted(
            themes.items(), key=lambda kv: len(kv[1]), reverse=True
        ):
            sample = items[0]
            lines.append(
                f"| {theme} | {len(items)} | {sample['feedback_id']}: "
                f"{sample['summary']} ({sample['customer']}) |"
            )
        lines.append("")
        lines.append("## By Channel")
        lines.append("")
        lines.append("| Channel | Count |")
        lines.append("|---------|-------|")
        for ch, count in sorted(channels.items(), key=lambda kv: -kv[1]):
            lines.append(f"| {ch} | {count} |")
        return "\n".join(lines)

    def _feedback_summary(self, feature_id=None) -> str:
        if not feature_id:
            feedback = [
                f for f in (
                    _normalize_live_feedback(row)
                    for row in _fetch_collection("incidents")
                )
                if f["feedback_id"]
            ]
            if feedback:
                return self._live_feedback_summary(feedback)
        data = _feedback_summary()
        lines = [
            "# Product Feedback Summary",
            "",
            f"**Total Feedback Entries:** {data['total_entries']}",
            f"**Avg Satisfaction Score:** {data['avg_score']}/10",
            f"**ARR Represented:** ${data['total_arr_represented']:,}",
            "",
            "## Sentiment Breakdown",
            "",
            "| Sentiment | Count |",
            "|-----------|-------|",
        ]
        for s, c in data["by_sentiment"].items():
            lines.append(f"| {s.title()} | {c} |")
        lines.append("")
        lines.append("## By Category")
        lines.append("")
        lines.append("| Category | Count |")
        lines.append("|----------|-------|")
        for cat, c in data["by_category"].items():
            lines.append(f"| {cat.replace('_', ' ').title()} | {c} |")
        lines.append("")
        lines.append("## By Channel")
        lines.append("")
        lines.append("| Channel | Count |")
        lines.append("|---------|-------|")
        for ch, c in data["by_channel"].items():
            lines.append(f"| {ch.replace('_', ' ').title()} | {c} |")
        return "\n".join(lines)

    def _feature_requests(self) -> str:
        data = _feature_request_ranking()
        lines = [
            "# Feature Requests (Ranked by ARR Weight)",
            "",
            f"**Total Requests:** {data['total_requests']}",
            "",
            "| Rank | Feature | Votes | ARR Weight | Effort | Status |",
            "|------|---------|-------|-----------|--------|--------|",
        ]
        for i, fr in enumerate(data["requests"], 1):
            lines.append(
                f"| {i} | {fr['title']} | {fr['votes']} | ${fr['arr_weight']:,} "
                f"| {fr['effort'].upper()} | {fr['status']} |"
            )
        return "\n".join(lines)

    def _sentiment_analysis(self) -> str:
        data = _sentiment_analysis()
        lines = [
            "# Sentiment Analysis",
            "",
            f"**Positive:** {data['positive_pct']}% | **Negative:** {data['negative_pct']}%",
            "",
            "## NPS Trend",
            "",
            "| Quarter | Promoters | Passives | Detractors | NPS |",
            "|---------|-----------|----------|------------|-----|",
        ]
        for q, nps in data["nps_trend"].items():
            lines.append(f"| {q} | {nps['promoters']} | {nps['passives']} | {nps['detractors']} | {nps['score']} |")
        lines.append("")
        lines.append("## Recent Feedback")
        lines.append("")
        lines.append("| Customer | Sentiment | Score | Category | Excerpt |")
        lines.append("|----------|-----------|-------|----------|---------|")
        for e in data["entries"]:
            lines.append(
                f"| {e['customer']} | {e['sentiment'].upper()} | {e['score']} "
                f"| {e['category']} | {e['excerpt']}... |"
            )
        return "\n".join(lines)

    def _roadmap_impact(self) -> str:
        data = _roadmap_impact()
        lines = [
            "# Roadmap Impact Assessment",
            "",
            "| Rank | Feature | Priority Score | ARR Weight | Effort | Status |",
            "|------|---------|---------------|-----------|--------|--------|",
        ]
        for i, item in enumerate(data["items"], 1):
            lines.append(
                f"| {i} | {item['title']} | {item['priority_score']} "
                f"| ${item['arr_weight']:,} | {item['effort'].upper()} | {item['status']} |"
            )
        lines.append("")
        lines.append("## Recommendations")
        lines.append("- RBAC and Workflow Automation are highest priority by ARR-weighted scoring.")
        lines.append("- Large Dataset Export fix is quick win with low effort and active churn risk.")
        lines.append("- Real-Time Alerting should be accelerated given competitive pressure.")
        return "\n".join(lines)

    def _pain_point_analysis(self) -> str:
        ranked = sorted(
            EVIDENCE_ACTIONS.items(),
            key=lambda item: (item[1]["frequency"] * item[1]["severity"], item[0]),
            reverse=True,
        )
        lines = [
            "# Pain Point and Feature Theme Analysis",
            "",
            "| Rank | Feature ID | Pain Point | Theme | Frequency | Severity | Retention Impact |",
            "|------|------------|------------|-------|-----------|----------|------------------|",
        ]
        for rank, (feature_id, action) in enumerate(ranked, 1):
            lines.append(
                f"| {rank} | {feature_id} | {action['pain_point']} | {action['theme']} "
                f"| {action['frequency']} | {action['severity']}/5 | {action['retention_impact'].upper()} |"
            )
        lines.extend([
            "",
            "Ranking is deterministic: feedback frequency multiplied by severity, with feature ID as the tie-breaker.",
        ])
        return "\n".join(lines)

    def _risk_alerts(self) -> str:
        ranked = sorted(
            EVIDENCE_ACTIONS.items(),
            key=lambda item: (FEATURE_REQUESTS[item[0]]["arr_weight"], item[0]),
            reverse=True,
        )
        lines = [
            "# Churn Risk and Competitive Gap Alerts",
            "",
            "| Feature ID | Retention Risk | ARR Represented | Competitive Gap |",
            "|------------|----------------|-----------------|-----------------|",
        ]
        for feature_id, action in ranked:
            request = FEATURE_REQUESTS[feature_id]
            lines.append(
                f"| {feature_id} | {action['retention_impact'].upper()} "
                f"| ${request['arr_weight']:,} | {action['competitive_gap']} |"
            )
        lines.extend([
            "",
            "**Recommended Intervention:** Escalate critical/high retention risks before the next roadmap review.",
        ])
        return "\n".join(lines)

    def _activate_roadmap_action(self, feature_id) -> str:
        request, error = _exact_feature(feature_id)
        if error:
            return f"**Error:** {error}"
        action = EVIDENCE_ACTIONS[feature_id]
        priority_score = round(
            request["arr_weight"] / 1000
            / (3 if request["effort"] == "high" else 2 if request["effort"] == "medium" else 1),
            1,
        )
        return "\n".join([
            f"# Roadmap Action Activated — {request['title']}",
            "",
            f"**Feature ID:** {feature_id}",
            f"**Theme:** {action['theme']}",
            f"**Pain Point:** {action['pain_point']}",
            f"**Evidence:** {action['frequency']} signals at severity {action['severity']}/5",
            f"**Business Impact:** ${request['arr_weight']:,} ARR represented",
            f"**Engineering Effort:** {request['effort'].upper()}",
            f"**Priority Score:** {priority_score}",
            f"**Retention Risk:** {action['retention_impact'].upper()}",
            f"**Competitive Gap:** {action['competitive_gap']}",
            "",
            f"**Jira Ticket:** {action['jira_project']}-{feature_id}",
            f"**Jira Receipt:** sim-jira-{feature_id.lower()}",
            f"**Microsoft Teams Channel:** {action['teams_channel']}",
            f"**Teams Receipt:** sim-teams-product-{feature_id.lower()}",
            "**External Writes:** simulated; no live Jira or Microsoft Teams mutation performed.",
        ])


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = ProductFeedbackSynthesizerAgent()
    print("=" * 60)
    print("EMBEDDED DEMO FEEDBACK (works offline)")
    print(agent.perform(operation="feedback_summary", feature_id="FR-001"))
    print("\n" + "=" * 60)
    print("LIVE TENANT FEEDBACK (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="feedback_summary"))
    for op in ["feature_requests", "sentiment_analysis", "roadmap_impact"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
