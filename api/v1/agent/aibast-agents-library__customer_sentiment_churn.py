"""
Customer Sentiment & Churn Agent — Financial Services Stack

Analyzes customer sentiment, predicts churn risk, recommends retention
actions, and provides segment-level insights for financial institutions.
"""

import sys
import os
import hashlib

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/customer_sentiment_churn",
    "version": "1.1.0",
    "display_name": "Customer Sentiment & Churn Agent",
    "description": "Customer sentiment analysis, churn prediction, retention action planning, and segment analytics for financial services.",
    "author": "AIBAST",
    "tags": ["sentiment", "churn", "retention", "NPS", "analytics", "financial-services"],
    "category": "financial_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# Synthetic domain data
# ---------------------------------------------------------------------------

CUSTOMER_INTERACTIONS = {
    "CUST-8001": {
        "name": "Elizabeth Warren-Hayes",
        "segment": "affluent",
        "tenure_years": 12,
        "products": ["checking", "savings", "mortgage", "investment"],
        "nps_score": 9,
        "last_survey": "2025-02-01",
        "recent_interactions": [
            {"date": "2025-02-15", "channel": "branch", "type": "inquiry", "sentiment": "positive"},
            {"date": "2025-01-20", "channel": "phone", "type": "account_service", "sentiment": "neutral"},
        ],
        "monthly_transactions": 48,
        "digital_engagement_score": 72,
        "complaint_count_12m": 0,
    },
    "CUST-8002": {
        "name": "Marcus Johnson",
        "segment": "mass_market",
        "tenure_years": 3,
        "products": ["checking", "credit_card"],
        "nps_score": 4,
        "last_survey": "2025-01-15",
        "recent_interactions": [
            {"date": "2025-03-01", "channel": "phone", "type": "complaint", "sentiment": "negative"},
            {"date": "2025-02-10", "channel": "chat", "type": "fee_dispute", "sentiment": "negative"},
            {"date": "2025-01-25", "channel": "phone", "type": "complaint", "sentiment": "negative"},
        ],
        "monthly_transactions": 15,
        "digital_engagement_score": 35,
        "complaint_count_12m": 5,
    },
    "CUST-8003": {
        "name": "Priya Sharma",
        "segment": "emerging_affluent",
        "tenure_years": 5,
        "products": ["checking", "savings", "credit_card", "auto_loan"],
        "nps_score": 7,
        "last_survey": "2025-02-20",
        "recent_interactions": [
            {"date": "2025-02-28", "channel": "mobile", "type": "transfer", "sentiment": "neutral"},
            {"date": "2025-02-05", "channel": "email", "type": "inquiry", "sentiment": "positive"},
        ],
        "monthly_transactions": 32,
        "digital_engagement_score": 88,
        "complaint_count_12m": 1,
    },
    "CUST-8004": {
        "name": "Gerald Thompson",
        "segment": "mass_market",
        "tenure_years": 8,
        "products": ["checking"],
        "nps_score": 3,
        "last_survey": "2024-11-01",
        "recent_interactions": [
            {"date": "2024-12-15", "channel": "branch", "type": "withdrawal", "sentiment": "neutral"},
        ],
        "monthly_transactions": 4,
        "digital_engagement_score": 12,
        "complaint_count_12m": 2,
    },
    "CUST-8005": {
        "name": "Diana Castellano",
        "segment": "small_business",
        "tenure_years": 6,
        "products": ["business_checking", "business_credit", "merchant_services"],
        "nps_score": 6,
        "last_survey": "2025-01-10",
        "recent_interactions": [
            {"date": "2025-02-20", "channel": "phone", "type": "fee_dispute", "sentiment": "negative"},
            {"date": "2025-01-30", "channel": "branch", "type": "inquiry", "sentiment": "neutral"},
        ],
        "monthly_transactions": 120,
        "digital_engagement_score": 55,
        "complaint_count_12m": 3,
    },
}

CHURN_INDICATORS = {
    "low_nps": {"threshold": 5, "weight": 25, "description": "NPS score below 5 indicates detractor status"},
    "declining_transactions": {"threshold": 10, "weight": 20, "description": "Monthly transactions below segment average"},
    "high_complaints": {"threshold": 3, "weight": 20, "description": "3+ complaints in last 12 months"},
    "low_engagement": {"threshold": 30, "weight": 15, "description": "Digital engagement score below 30"},
    "single_product": {"threshold": 1, "weight": 10, "description": "Only one active product"},
    "stale_survey": {"threshold": 90, "weight": 10, "description": "Last survey response over 90 days ago"},
}

RETENTION_ACTIONS = {
    "fee_waiver": {"description": "Waive monthly maintenance fees for 6 months", "cost": 72, "success_rate": 45},
    "rate_upgrade": {"description": "Offer premium savings rate for 12 months", "cost": 150, "success_rate": 35},
    "personal_outreach": {"description": "Schedule call with relationship manager", "cost": 25, "success_rate": 55},
    "product_bundle": {"description": "Offer discounted product bundle with waived fees", "cost": 200, "success_rate": 60},
    "loyalty_bonus": {"description": "Credit loyalty bonus to account", "cost": 100, "success_rate": 50},
    "complaint_resolution": {"description": "Escalate to service recovery team", "cost": 50, "success_rate": 65},
}

SEGMENT_BENCHMARKS = {
    "affluent": {"avg_nps": 8.2, "avg_products": 4.1, "avg_tenure": 10, "avg_transactions": 55},
    "emerging_affluent": {"avg_nps": 7.0, "avg_products": 3.2, "avg_tenure": 5, "avg_transactions": 35},
    "mass_market": {"avg_nps": 6.5, "avg_products": 2.0, "avg_tenure": 4, "avg_transactions": 20},
    "small_business": {"avg_nps": 6.8, "avg_products": 3.0, "avg_tenure": 5, "avg_transactions": 90},
}


# ---------------------------------------------------------------------------
# Extended capability library (v1.1.0)
#
# Self-contained data for the five newer sentiment/churn capabilities derived
# from the external agent spec. Each entry carries the spec `response` line,
# the `knowledge` citations, three synthetic `records`, the exact-lookup
# `key_field`, and the `write`/`generative` flags. Nothing external is called:
# `write` capabilities return a simulated receipt only — no live mutations.
# ---------------------------------------------------------------------------

CAPABILITY_LIBRARY = {
    "churn_risk_scoring": {
        "display_name": "Churn Risk Scoring",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "account_id",
        "response": "Here is the sentiment-driven churn risk analysis across your customer base, prioritized by risk level and account value.",
        "knowledge": [
            "Analyze sentiment across all customer touchpoints (one-pager, Slide 1).",
            "Score churn risk by unifying sentiment, behavior, and all activity (one-pager, Slide 1).",
            "In moments the agent processes a large volume of diverse data and identifies customers with elevated churn risk with minimal effort (demo 00:00:52-00:01:01).",
            "The manager receives a prioritized list of high-risk accounts and key drivers, insights that used to be difficult to obtain (demo 00:01:01-00:01:08).",
        ],
        "records": [
            {"account_id": "ACCT7781", "customer": "Northwind Freight", "churn_risk": "High", "sentiment_score": "-0.62", "primary_driver": "Repeated billing disputes"},
            {"account_id": "ACCT4419", "customer": "Larkspur Retail", "churn_risk": "Medium", "sentiment_score": "-0.18", "primary_driver": "Slow support response"},
            {"account_id": "ACCT9903", "customer": "Cedarworks Manufacturing", "churn_risk": "Low", "sentiment_score": "0.34", "primary_driver": "Stable engagement"},
        ],
    },
    "early_warning_signals": {
        "display_name": "Early Warning Signals",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "signal_id",
        "response": "These are the early-warning signals and real-time alerts for your higher-risk customers, with the most critical conditions flagged first.",
        "knowledge": [
            "Detect early warning triggers in real time to enable timely, proactive intervention (one-pager, Slide 1).",
            "The agent highlights predictive signals affecting higher-risk customers and zeros in on the critical conditions (demo 00:01:12-00:01:21).",
            "The agent highlights real-time alerts and flags customers for urgent follow up so the manager can act before issues escalate (demo 00:01:21-00:01:28).",
        ],
        "records": [
            {"signal_id": "SIGNAL3310", "customer": "Northwind Freight", "indicator": "Login frequency dropped 40 percent", "severity": "Critical", "alert_status": "Real-time alert sent"},
            {"signal_id": "SIGNAL5582", "customer": "Larkspur Retail", "indicator": "Two escalated complaints in seven days", "severity": "Elevated", "alert_status": "Added to watchlist"},
            {"signal_id": "SIGNAL7048", "customer": "Beacon Logistics", "indicator": "Contract renewal overdue", "severity": "Critical", "alert_status": "Real-time alert sent"},
        ],
    },
    "customer_snapshot": {
        "display_name": "Customer 360 Snapshot",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "snapshot_id",
        "response": "Here is the consolidated customer snapshot bringing CRM and core banking context together into one decision-ready view.",
        "knowledge": [
            "The agent consolidates CRM and core banking data into a single customer snapshot, surfacing only the most relevant context (demo 00:01:31-00:01:39).",
            "Instead of playing detective across multiple systems, the manager gets a rapid decision-ready view with risks clearly defined (demo 00:01:40-00:01:48).",
            "Predict churn risk to pinpoint critical and high-risk customers (one-pager, Slide 1).",
        ],
        "records": [
            {"snapshot_id": "SNAP2205", "customer": "Northwind Freight", "relationship": "Commercial Lending", "balances": "4.2M deposits", "open_items": "3 open service tickets"},
            {"snapshot_id": "SNAP6613", "customer": "Larkspur Retail", "relationship": "Business Banking", "balances": "0.9M deposits", "open_items": "1 open service ticket"},
            {"snapshot_id": "SNAP8890", "customer": "Beacon Logistics", "relationship": "Treasury Services", "balances": "7.8M deposits", "open_items": "5 open service tickets"},
        ],
    },
    "retention_strategy": {
        "display_name": "Retention Strategy Generation",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": True,
        "exact_key_required": True,
        "key_field": "strategy_id",
        "response": "Here are tailored retention strategies for each customer, covering outreach approach, messaging, offers, and timing.",
        "knowledge": [
            "Generate targeted retention strategies and recommended outreach plans (one-pager, Slide 1).",
            "Generate tailored retention and outreach plans to speed up preparation workflows (one-pager, Slide 1).",
            "The agent generates tailored recommendations for each customer, including outreach approach, messaging, offers, and timing (demo 00:01:48-00:01:58).",
        ],
        "records": [
            {"strategy_id": "PLAN1120", "customer": "Northwind Freight", "outreach": "Executive outreach call", "offer": "Fee waiver plus dedicated relationship manager", "timing": "Within 48 hours"},
            {"strategy_id": "PLAN3345", "customer": "Larkspur Retail", "outreach": "Personalized email", "offer": "Loyalty rate offer", "timing": "This week"},
            {"strategy_id": "PLAN5567", "customer": "Beacon Logistics", "outreach": "In-person account review", "offer": "Treasury optimization package", "timing": "Next 5 business days"},
        ],
    },
    "retention_coordination": {
        "display_name": "Retention Coordination and Tracking",
        "source_system": "Dynamics 365 CRM",
        "write": True,
        "generative": False,
        "exact_key_required": True,
        "key_field": "task_id",
        "response": "I have coordinated and updated tracking for your priority retention tasks, flagging delays and escalating blockers in Microsoft Teams.",
        "knowledge": [
            "To wrap up the workflow, the agent automates coordination and tracking for the priority customers (demo 00:02:04-00:02:10).",
            "It surfaces updates, flags delays, and escalates blockers, keeping retention efforts on track (demo 00:02:10-00:02:16).",
            "The unified view of churn risk is delivered by connecting to Dynamics 365 and driving communication through Microsoft Teams (demo 00:00:28-00:00:33).",
        ],
        "records": [
            {"task_id": "TASK4401", "customer": "Northwind Freight", "action": "RM follow-up call", "status": "In progress", "tracking": "On track"},
            {"task_id": "TASK6622", "customer": "Larkspur Retail", "action": "Send loyalty offer", "status": "Delayed", "tracking": "Escalated to team lead"},
            {"task_id": "TASK8833", "customer": "Beacon Logistics", "action": "Schedule treasury review", "status": "Not started", "tracking": "Blocker flagged"},
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _churn_score(customer):
    """Calculate churn risk score (0-100)."""
    score = 0
    if customer["nps_score"] < CHURN_INDICATORS["low_nps"]["threshold"]:
        score += CHURN_INDICATORS["low_nps"]["weight"]
    if customer["monthly_transactions"] < CHURN_INDICATORS["declining_transactions"]["threshold"]:
        score += CHURN_INDICATORS["declining_transactions"]["weight"]
    if customer["complaint_count_12m"] >= CHURN_INDICATORS["high_complaints"]["threshold"]:
        score += CHURN_INDICATORS["high_complaints"]["weight"]
    if customer["digital_engagement_score"] < CHURN_INDICATORS["low_engagement"]["threshold"]:
        score += CHURN_INDICATORS["low_engagement"]["weight"]
    if len(customer["products"]) <= CHURN_INDICATORS["single_product"]["threshold"]:
        score += CHURN_INDICATORS["single_product"]["weight"]
    return min(100, score)


def _sentiment_breakdown():
    """Compute overall sentiment distribution."""
    sentiments = {"positive": 0, "neutral": 0, "negative": 0}
    total = 0
    for cust in CUSTOMER_INTERACTIONS.values():
        for interaction in cust["recent_interactions"]:
            sentiments[interaction["sentiment"]] += 1
            total += 1
    return sentiments, total


def _humanize(text):
    """Turn a snake_case field name into a Title Case label."""
    return text.replace("_", " ").title()


def _normalized_lookup_tokens(value):
    """Normalize whitespace-delimited tokens without permitting embedded IDs."""
    normalized = []
    for token in str(value or "").casefold().split():
        cleaned = "".join(char for char in token if char.isalnum())
        if cleaned:
            normalized.append(cleaned)
    return normalized


def _contains_normalized_key(user_input, key):
    """Return True only when the complete normalized key is a token sequence."""
    query = _normalized_lookup_tokens(user_input)
    expected = _normalized_lookup_tokens(key)
    width = len(expected)
    return bool(width) and any(
        query[index:index + width] == expected
        for index in range(len(query) - width + 1)
    )


def _find_record(entry, user_input):
    """Return the uniquely matched record for a complete normalized key."""
    if not user_input:
        return None
    matches = [
        record for record in entry["records"]
        if _contains_normalized_key(user_input, record[entry["key_field"]])
    ]
    return matches[0] if len(matches) == 1 else None


def _write_receipt(op_key, entry, record):
    """Simulated write receipt — no live system is mutated."""
    ref = record[entry["key_field"]]
    digest = hashlib.sha256(f"{op_key}|{ref}".encode("utf-8")).hexdigest()[:8].upper()
    lines = [
        "## Simulated Write Receipt",
        "",
        "> No live systems were modified. This is a simulated coordination receipt.",
        "",
        f"- **Receipt ID:** SIM-{digest}",
        f"- **{_humanize(entry['key_field'])}:** {ref}",
        f"- **Recorded status:** {record.get('status', 'n/a')}",
        f"- **Channel:** Microsoft Teams (simulated)",
        f"- **Mode:** dry-run (no live mutation)",
    ]
    return "\n".join(lines)


def _capability_report(op_key, **kwargs):
    """Deterministic handler for an extended capability.

    With a `user_input` that contains an exact key value, returns the detail
    for that single record (plus a simulated receipt for write capabilities).
    Without a matching key, returns a useful no-input summary of all records.
    """
    entry = CAPABILITY_LIBRARY[op_key]
    user_input = kwargs.get("user_input") or ""
    record = _find_record(entry, user_input)
    key_field = entry["key_field"]

    if record is not None:
        lines = [f"# {entry['display_name']}\n", f"_{entry['response']}_\n"]
        lines.append(f"## Record {record[key_field]}\n")
        for field, value in record.items():
            lines.append(f"- **{_humanize(field)}:** {value}")
        if entry["write"]:
            lines.append("")
            lines.append(_write_receipt(op_key, entry, record))
        return "\n".join(lines)

    if str(user_input).strip():
        return (
            f"# {entry['display_name']}\n\n"
            f"No exact normalized `{key_field}` matched the request."
        )

    lines = [f"# {entry['display_name']}\n", f"_{entry['response']}_\n"]
    lines.append(f"**Source system:** {entry['source_system']}  ")
    lines.append(f"**Write:** {'yes' if entry['write'] else 'no'}  ")
    lines.append(f"**Generative:** {'yes' if entry['generative'] else 'no'}  ")
    lines.append(
        f"**Exact key required:** {'yes' if entry['exact_key_required'] else 'no'} "
        f"(key: `{key_field}`)\n"
    )
    headers = list(entry["records"][0].keys())
    lines.append("| " + " | ".join(_humanize(h) for h in headers) + " |")
    lines.append("|" + "|".join("---" for _ in headers) + "|")
    for rec in entry["records"]:
        lines.append("| " + " | ".join(str(rec[h]) for h in headers) + " |")
    lines.append("\n## Knowledge\n")
    for item in entry["knowledge"]:
        lines.append(f"- {item}")
    lines.append(
        f"\n_Provide `user_input` containing a `{key_field}` value "
        f"(e.g. `{entry['records'][0][key_field]}`) for an exact record lookup._"
    )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class CustomerSentimentChurnAgent(BasicAgent):
    """Customer sentiment and churn prediction agent."""

    def __init__(self):
        self.name = "CustomerSentimentChurnAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Customer Sentiment & Churn Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "sentiment_dashboard",
                            "churn_prediction",
                            "retention_actions",
                            "segment_analysis",
                            "churn_risk_scoring",
                            "early_warning_signals",
                            "customer_snapshot",
                            "retention_strategy",
                            "retention_coordination",
                        ],
                    },
                    "customer_id": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "sentiment_dashboard")
        dispatch = {
            "sentiment_dashboard": self._sentiment_dashboard,
            "churn_prediction": self._churn_prediction,
            "retention_actions": self._retention_actions,
            "segment_analysis": self._segment_analysis,
            "churn_risk_scoring": self._churn_risk_scoring,
            "early_warning_signals": self._early_warning_signals,
            "customer_snapshot": self._customer_snapshot,
            "retention_strategy": self._retention_strategy,
            "retention_coordination": self._retention_coordination,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _sentiment_dashboard(self, **kwargs) -> str:
        sentiments, total = _sentiment_breakdown()
        avg_nps = sum(c["nps_score"] for c in CUSTOMER_INTERACTIONS.values()) / len(CUSTOMER_INTERACTIONS)
        lines = ["# Customer Sentiment Dashboard\n"]
        lines.append(f"**Average NPS:** {avg_nps:.1f}")
        lines.append(f"**Total Interactions Analyzed:** {total}\n")
        lines.append("## Sentiment Distribution\n")
        for sent, count in sentiments.items():
            pct = round((count / total) * 100, 1) if total else 0
            lines.append(f"- **{sent.title()}:** {count} ({pct}%)")
        lines.append("\n## Customer NPS Scores\n")
        lines.append("| Customer | Segment | NPS | Products | Complaints (12m) |")
        lines.append("|---|---|---|---|---|")
        for cid, c in CUSTOMER_INTERACTIONS.items():
            lines.append(
                f"| {c['name']} ({cid}) | {c['segment'].replace('_', ' ').title()} "
                f"| {c['nps_score']} | {len(c['products'])} | {c['complaint_count_12m']} |"
            )
        return "\n".join(lines)

    def _churn_prediction(self, **kwargs) -> str:
        lines = ["# Churn Prediction Report\n"]
        lines.append("| Customer | Segment | Churn Score | NPS | Transactions | Complaints |")
        lines.append("|---|---|---|---|---|---|")
        at_risk = []
        for cid, c in CUSTOMER_INTERACTIONS.items():
            score = _churn_score(c)
            risk = "High" if score >= 50 else "Medium" if score >= 25 else "Low"
            lines.append(
                f"| {c['name']} ({cid}) | {c['segment'].replace('_', ' ').title()} "
                f"| {score} ({risk}) | {c['nps_score']} | {c['monthly_transactions']} | {c['complaint_count_12m']} |"
            )
            if score >= 50:
                at_risk.append((cid, c, score))
        if at_risk:
            lines.append("\n## High-Risk Customers\n")
            for cid, c, score in at_risk:
                lines.append(f"### {c['name']} ({cid}) — Score: {score}\n")
                lines.append(f"- Segment: {c['segment'].replace('_', ' ').title()}")
                lines.append(f"- Tenure: {c['tenure_years']} years")
                lines.append(f"- Products: {', '.join(c['products'])}")
                lines.append(f"- Recent sentiment: {c['recent_interactions'][-1]['sentiment'] if c['recent_interactions'] else 'N/A'}\n")
        lines.append("\n## Churn Indicators Reference\n")
        for ind_id, ind in CHURN_INDICATORS.items():
            lines.append(f"- **{ind_id.replace('_', ' ').title()}** (weight: {ind['weight']}): {ind['description']}")
        return "\n".join(lines)

    def _retention_actions(self, **kwargs) -> str:
        lines = ["# Retention Action Recommendations\n"]
        lines.append("## Available Actions\n")
        lines.append("| Action | Description | Cost | Success Rate |")
        lines.append("|---|---|---|---|")
        for action_id, action in RETENTION_ACTIONS.items():
            lines.append(
                f"| {action_id.replace('_', ' ').title()} | {action['description']} "
                f"| ${action['cost']} | {action['success_rate']}% |"
            )
        lines.append("\n## Recommended Actions by Customer\n")
        for cid, c in CUSTOMER_INTERACTIONS.items():
            score = _churn_score(c)
            if score < 25:
                continue
            lines.append(f"### {c['name']} ({cid}) — Churn Score: {score}\n")
            if c["complaint_count_12m"] >= 3:
                lines.append(f"1. **Complaint Resolution** — {RETENTION_ACTIONS['complaint_resolution']['description']}")
            if c["nps_score"] < 5:
                lines.append(f"2. **Personal Outreach** — {RETENTION_ACTIONS['personal_outreach']['description']}")
            if len(c["products"]) <= 2:
                lines.append(f"3. **Product Bundle** — {RETENTION_ACTIONS['product_bundle']['description']}")
            else:
                lines.append(f"3. **Loyalty Bonus** — {RETENTION_ACTIONS['loyalty_bonus']['description']}")
            lines.append("")
        return "\n".join(lines)

    def _segment_analysis(self, **kwargs) -> str:
        lines = ["# Segment Analysis\n"]
        lines.append("## Segment Benchmarks\n")
        lines.append("| Segment | Avg NPS | Avg Products | Avg Tenure | Avg Transactions |")
        lines.append("|---|---|---|---|---|")
        for seg, bench in SEGMENT_BENCHMARKS.items():
            lines.append(
                f"| {seg.replace('_', ' ').title()} | {bench['avg_nps']} "
                f"| {bench['avg_products']} | {bench['avg_tenure']} yrs | {bench['avg_transactions']}/mo |"
            )
        segments = {}
        for cid, c in CUSTOMER_INTERACTIONS.items():
            seg = c["segment"]
            if seg not in segments:
                segments[seg] = []
            segments[seg].append(c)
        lines.append("\n## Current Customer Performance vs Benchmark\n")
        for seg, customers in segments.items():
            bench = SEGMENT_BENCHMARKS.get(seg, {})
            avg_nps = sum(c["nps_score"] for c in customers) / len(customers)
            avg_products = sum(len(c["products"]) for c in customers) / len(customers)
            lines.append(f"### {seg.replace('_', ' ').title()} ({len(customers)} customers)\n")
            lines.append(f"- NPS: {avg_nps:.1f} (benchmark: {bench.get('avg_nps', 'N/A')})")
            lines.append(f"- Products: {avg_products:.1f} (benchmark: {bench.get('avg_products', 'N/A')})")
            lines.append("")
        return "\n".join(lines)

    # -- Extended capabilities (v1.1.0) --------------------------------------

    def _churn_risk_scoring(self, **kwargs) -> str:
        return _capability_report("churn_risk_scoring", **kwargs)

    def _early_warning_signals(self, **kwargs) -> str:
        return _capability_report("early_warning_signals", **kwargs)

    def _customer_snapshot(self, **kwargs) -> str:
        return _capability_report("customer_snapshot", **kwargs)

    def _retention_strategy(self, **kwargs) -> str:
        return _capability_report("retention_strategy", **kwargs)

    def _retention_coordination(self, **kwargs) -> str:
        return _capability_report("retention_coordination", **kwargs)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = CustomerSentimentChurnAgent()
    print(agent.perform(operation="sentiment_dashboard"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="churn_prediction"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="retention_actions"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="segment_analysis"))
