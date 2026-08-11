"""
Fraud Detection & Alert Agent — Financial Services Stack

Provides alert triage, transaction analysis, pattern detection, and
investigation summaries for financial fraud operations teams.

Version 1.1.0 adds AI-driven fraud monitoring capabilities reproducing the
Fraud Detection & Alert one-pager and demo workflow: overnight alert triage,
coordinated fraud-ring pattern analysis, account-takeover ring investigation,
investigation case creation with protective actions, and fraud-prevention
performance reporting into Microsoft Teams. Each new capability supports an
optional ``user_input`` for exact-key lookup, returns a useful no-input
summary, and clearly simulates any write (case creation / Teams posting) with
a receipt and no external mutation. All original operations and data are
preserved unchanged.
"""

import sys
import os
import hashlib

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/fraud_detection_alert",
    "version": "1.1.0",
    "display_name": "Fraud Detection & Alert Agent",
    "description": "Financial fraud detection with alert triage, transaction analysis, pattern recognition, and investigation case management.",
    "author": "AIBAST",
    "tags": ["fraud", "detection", "alerts", "transactions", "investigation", "financial-services"],
    "category": "financial_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# Synthetic domain data
# ---------------------------------------------------------------------------

TRANSACTIONS = {
    "TXN-90001": {"account": "4532-XXXX-8891", "cardholder": "James Peterson", "amount": 4850.00, "merchant": "ElectroMax Dubai", "category": "electronics", "country": "AE", "timestamp": "2025-03-05T02:15:00", "channel": "card_present", "risk_score": 88},
    "TXN-90002": {"account": "4532-XXXX-8891", "cardholder": "James Peterson", "amount": 2100.00, "merchant": "Gold Souq Trading", "category": "jewelry", "country": "AE", "timestamp": "2025-03-05T02:42:00", "channel": "card_present", "risk_score": 92},
    "TXN-90003": {"account": "4716-XXXX-3304", "cardholder": "Lisa Wang", "amount": 12500.00, "merchant": "CryptoSwap Exchange", "category": "crypto", "country": "US", "timestamp": "2025-03-04T18:30:00", "channel": "online", "risk_score": 75},
    "TXN-90004": {"account": "4716-XXXX-3304", "cardholder": "Lisa Wang", "amount": 9800.00, "merchant": "CryptoSwap Exchange", "category": "crypto", "country": "US", "timestamp": "2025-03-04T18:35:00", "channel": "online", "risk_score": 82},
    "TXN-90005": {"account": "5412-XXXX-6678", "cardholder": "Robert Miles", "amount": 189.99, "merchant": "Amazon.com", "category": "retail", "country": "US", "timestamp": "2025-03-05T10:20:00", "channel": "online", "risk_score": 12},
    "TXN-90006": {"account": "5412-XXXX-6678", "cardholder": "Robert Miles", "amount": 3200.00, "merchant": "WireTransfer-NG", "category": "wire_transfer", "country": "NG", "timestamp": "2025-03-05T11:05:00", "channel": "online", "risk_score": 95},
    "TXN-90007": {"account": "4024-XXXX-1190", "cardholder": "Elena Vasquez", "amount": 67.50, "merchant": "Whole Foods Market", "category": "grocery", "country": "US", "timestamp": "2025-03-05T09:15:00", "channel": "contactless", "risk_score": 5},
}

ALERT_RULES = {
    "RULE-001": {"name": "Velocity Check", "description": "Multiple high-value transactions within 1 hour", "threshold": "2+ transactions over $1,000 within 60 minutes", "severity": "high"},
    "RULE-002": {"name": "Geographic Anomaly", "description": "Transaction in country with no prior history", "threshold": "First transaction in high-risk country", "severity": "high"},
    "RULE-003": {"name": "Crypto Purchase Spike", "description": "Unusual crypto exchange activity", "threshold": "Crypto transactions exceeding 3x normal volume", "severity": "medium"},
    "RULE-004": {"name": "Wire to High-Risk Country", "description": "Wire transfer to FATF grey/black list country", "threshold": "Any wire to listed jurisdiction", "severity": "critical"},
    "RULE-005": {"name": "Card-Not-Present Velocity", "description": "Rapid online purchases across merchants", "threshold": "5+ online transactions within 30 minutes", "severity": "medium"},
    "RULE-006": {"name": "Account Takeover Pattern", "description": "Password change followed by high-value transaction", "threshold": "Transaction within 2 hours of credential change", "severity": "critical"},
}

FRAUD_PATTERNS = {
    "card_cloning": {"description": "Physical card duplicated; used at multiple locations simultaneously", "indicators": ["Transactions in geographically distant locations within short timeframe", "Card-present transactions after reported card-not-present use"], "frequency": "common"},
    "account_takeover": {"description": "Unauthorized access to account via compromised credentials", "indicators": ["Login from new device/IP", "Immediate password and contact info change", "Large transfer or purchase within hours"], "frequency": "increasing"},
    "bust_out": {"description": "Deliberate credit line exhaustion before default", "indicators": ["Rapid utilization increase to near-limit", "Cash advance activity", "Payments stop after utilization spike"], "frequency": "moderate"},
    "synthetic_identity": {"description": "Fictitious identity created using mixed real and fake data", "indicators": ["SSN with no credit history prior to 2 years ago", "Authorized user on multiple unrelated accounts", "Address inconsistencies"], "frequency": "increasing"},
}

INVESTIGATION_CASES = {
    "INV-2025-301": {
        "alert_txns": ["TXN-90001", "TXN-90002"],
        "rules_triggered": ["RULE-001", "RULE-002"],
        "pattern": "card_cloning",
        "status": "open",
        "analyst": "Karen Wright",
        "opened": "2025-03-05",
        "priority": "high",
        "notes": "Cardholder confirmed they are not traveling. Card blocked. Replacement issued.",
    },
    "INV-2025-302": {
        "alert_txns": ["TXN-90006"],
        "rules_triggered": ["RULE-004"],
        "pattern": "account_takeover",
        "status": "escalated",
        "analyst": "David Chen",
        "opened": "2025-03-05",
        "priority": "critical",
        "notes": "Wire to Nigeria following password reset 90 minutes prior. SAR filing initiated.",
    },
    "INV-2025-303": {
        "alert_txns": ["TXN-90003", "TXN-90004"],
        "rules_triggered": ["RULE-003"],
        "pattern": None,
        "status": "under_review",
        "analyst": "Karen Wright",
        "opened": "2025-03-04",
        "priority": "medium",
        "notes": "Customer confirmed crypto purchases. Monitoring for additional activity.",
    },
}


# ---------------------------------------------------------------------------
# v1.1.0 — Fraud Monitoring & Identification capabilities
# Deterministic, spec-derived data (source: fraud-monitoring external spec).
# Each capability carries its own response line, knowledge notes, and exactly
# three synthetic records keyed for exact-key lookup.
# ---------------------------------------------------------------------------

FRAUD_MONITORING_CAPABILITIES = {
    "alert_triage": {
        "title": "Fraud Alert Triage",
        "response": "Here is your prioritized fraud alert triage for overnight activity, with the most critical alerts surfaced first and a recommended immediate action.",
        "source_system": "Dynamics 365 ERP",
        "write": False,
        "generative": False,
        "key_field": "alert_id",
        "key_label": "Alert",
        "knowledge": [
            "The agent processes all alerts instantly and surfaces the most urgent threats rather than requiring hours of manual overnight triage.",
            "Alerts span card, account, and wire channels; the agent distinguishes noise from true risk to cut alert fatigue.",
            "For each triage run the agent highlights the most critical alerts and recommends one that requires immediate action.",
            "Triage draws on connected analytics, core systems, and activity logs to give a single targeted view.",
        ],
        "records": [
            {"alert_id": "ALERT-4471", "channel": "Account Takeover", "risk_level": "Critical", "customer": "Dana Okoro", "recommended_action": "Escalate immediately to SIU"},
            {"alert_id": "ALERT-4472", "channel": "Card Testing", "risk_level": "Medium", "customer": "Miguel Santos", "recommended_action": "Monitor for velocity spikes"},
            {"alert_id": "ALERT-4473", "channel": "Wire Fraud", "risk_level": "Low", "customer": "Priya Nair", "recommended_action": "Auto-clear after review"},
        ],
    },
    "fraud_ring_analysis": {
        "title": "Fraud Ring Pattern Analysis",
        "response": "Here is the fraud ring pattern analysis, identifying organized rings with their shared behaviors and connected accounts across account-takeover, card testing, and wire fraud.",
        "source_system": "Dynamics 365 ERP",
        "write": False,
        "generative": True,
        "key_field": "ring_id",
        "key_label": "Ring",
        "knowledge": [
            "Pattern analysis identifies multiple organized fraud rings and summarizes the shared behaviors that link them.",
            "The agent highlights connected accounts to reveal coordinated schemes across account-takeover, card testing, and wire fraud.",
            "Detecting rings early limits combined exposure and losses before funds are lost.",
            "The bigger-picture insight previously could have required hours of manual investigation.",
        ],
        "records": [
            {"ring_id": "RING-88", "ring_type": "Account Takeover", "connected_accounts": 14, "shared_behavior": "Shared device fingerprints", "exposure_usd": 420000},
            {"ring_id": "RING-89", "ring_type": "Card Testing", "connected_accounts": 31, "shared_behavior": "Sequential BIN testing", "exposure_usd": 85000},
            {"ring_id": "RING-90", "ring_type": "Wire Fraud", "connected_accounts": 6, "shared_behavior": "Mule account layering", "exposure_usd": 610000},
        ],
    },
    "account_takeover_investigation": {
        "title": "Account Takeover Ring Investigation",
        "response": "Here is the account takeover ring investigation, surfacing each at-risk customer with suspicious activity timelines and the key indicators behind the alert.",
        "source_system": "Dynamics 365 ERP",
        "write": False,
        "generative": True,
        "key_field": "customer_id",
        "key_label": "Customer",
        "knowledge": [
            "The agent surfaces each at-risk customer within an account-takeover ring in one rapid sequence.",
            "For every customer it outlines suspicious activity timelines and shows the key indicators behind the alert.",
            "This critical context tells the analyst exactly where to intervene.",
            "Account-takeover is one of the coordinated fraud types tracked alongside card testing and wire fraud.",
        ],
        "records": [
            {"customer_id": "CUST-5012", "customer_name": "Dana Okoro", "indicator": "New device plus credential reset", "activity_timeline": "Large transfer attempt at 02:14", "status": "At risk"},
            {"customer_id": "CUST-5013", "customer_name": "Leo Zhang", "indicator": "Impossible travel login", "activity_timeline": "Password change at 03:41", "status": "At risk"},
            {"customer_id": "CUST-5014", "customer_name": "Amara Bello", "indicator": "SIM swap flag", "activity_timeline": "New payee added at 04:07", "status": "At risk"},
        ],
    },
    "case_action": {
        "title": "Investigation Case and Protective Actions",
        "response": "The investigation case has been created and protective actions are queued: freezing accounts, blocking cards, resetting credentials, and notifying the responsible team, with updates logged automatically.",
        "source_system": "Dynamics 365",
        "write": True,
        "generative": False,
        "key_field": "case_id",
        "key_label": "Case",
        "knowledge": [
            "When the analyst is ready to move forward the agent creates investigation cases and executes protective steps.",
            "Protective steps include freezing accounts, blocking cards, resetting credentials, and notifying teams.",
            "The agent performs actions consistently and logs updates automatically so the analyst can focus on critical decisions and customer communications.",
            "Critical alerts are routed rapidly to SIU, card fraud, or wire ops teams, automating case creation and protective actions to accelerate investigations.",
        ],
        "records": [
            {"case_id": "CASE-2201", "linked_alert": "ALERT-4471", "action": "Freeze account and block card", "assignee": "SIU queue", "status": "Case created and logged"},
            {"case_id": "CASE-2202", "linked_alert": "ALERT-4472", "action": "Reset credentials", "assignee": "Card fraud queue", "status": "Case created and logged"},
            {"case_id": "CASE-2203", "linked_alert": "ALERT-4473", "action": "Notify wire ops team", "assignee": "Wire ops queue", "status": "Case created and logged"},
        ],
    },
    "performance_report": {
        "title": "Fraud Prevention Performance and Teams Reporting",
        "response": "Here is the fraud prevention performance summary with core metrics, trends, and suggested next steps, compiled as a clean report and distributed automatically in Microsoft Teams for internal alignment.",
        "source_system": "Dynamics 365 ERP",
        "write": True,
        "generative": True,
        "key_field": "report_id",
        "key_label": "Report",
        "knowledge": [
            "The agent summarizes core metrics, trends, and suggested next steps for fraud prevention performance.",
            "The summary helps the team understand what is working and where threats are shifting.",
            "To close the loop the agent compiles a clean summary of findings, completed actions, and recommended next steps.",
            "The summary is distributed automatically in Microsoft Teams to ensure internal alignment.",
        ],
        "records": [
            {"report_id": "PERF-Q1", "metric": "Alert response time", "trend": "Down 38 percent", "next_step": "Expand real-time wire monitoring"},
            {"report_id": "PERF-Q2", "metric": "Confirmed fraud loss", "trend": "Down 22 percent", "next_step": "Tune card-testing detection rules"},
            {"report_id": "PERF-Q3", "metric": "Cases auto-created", "trend": "Up 61 percent", "next_step": "Add SIU review capacity"},
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _alert_metrics():
    """Compute alert and investigation metrics."""
    high_risk_txns = sum(1 for t in TRANSACTIONS.values() if t["risk_score"] >= 70)
    total_flagged_amount = sum(t["amount"] for t in TRANSACTIONS.values() if t["risk_score"] >= 70)
    open_cases = sum(1 for c in INVESTIGATION_CASES.values() if c["status"] in ("open", "under_review", "escalated"))
    return {"high_risk_txns": high_risk_txns, "flagged_amount": total_flagged_amount, "open_cases": open_cases}


def _risk_level(score):
    """Map numeric risk score to level."""
    if score >= 80:
        return "Critical"
    elif score >= 60:
        return "High"
    elif score >= 40:
        return "Medium"
    return "Low"


def _fmt_field(key):
    """Humanize a record field key for display."""
    return key.replace("_", " ").title()


def _fmt_value(key, value):
    """Format a record value, adding currency style for USD amounts."""
    if key.endswith("_usd") and isinstance(value, (int, float)):
        return f"${value:,.0f}"
    return str(value)


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


def _sim_receipt(operation, key):
    """Deterministic simulated-write receipt id (no external mutation)."""
    digest = hashlib.sha256(f"{operation}:{key}".encode("utf-8")).hexdigest()[:8].upper()
    return f"SIM-{digest}"


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class FraudDetectionAlertAgent(BasicAgent):
    """Fraud detection and alert management agent."""

    def __init__(self):
        self.name = "FraudDetectionAlertAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Fraud Detection & Alert Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "alert_triage",
                            "transaction_analysis",
                            "pattern_detection",
                            "investigation_summary",
                            "fraud_ring_analysis",
                            "account_takeover_investigation",
                            "case_action",
                            "performance_report",
                        ],
                    },
                    "case_id": {"type": "string"},
                    "account": {"type": "string"},
                    "user_input": {
                        "type": "string",
                        "description": "Optional free-text request; an exact record key (e.g. ALERT-4471, RING-90, CUST-5014, CASE-2201, PERF-Q3) mentioned here triggers an exact-key lookup.",
                    },
                    "key": {
                        "type": "string",
                        "description": "Optional exact record key for direct lookup on the v1.1.0 fraud-monitoring capabilities.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "alert_triage")
        if operation in FRAUD_MONITORING_CAPABILITIES and (
            operation != "alert_triage"
            or kwargs.get("user_input")
            or kwargs.get("key")
        ):
            return self._capability(**kwargs)
        dispatch = {
            "alert_triage": self._alert_triage,
            "transaction_analysis": self._transaction_analysis,
            "pattern_detection": self._pattern_detection,
            "investigation_summary": self._investigation_summary,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _capability(self, **kwargs) -> str:
        """Render a v1.1.0 fraud-monitoring capability.

        Supports optional exact-key lookup via ``key`` or ``user_input``.
        With no key/input, returns a useful summary over all three records.
        Write capabilities are clearly simulated with a receipt and mutate
        nothing outside the process.
        """
        operation = kwargs.get("operation")
        cap = FRAUD_MONITORING_CAPABILITIES[operation]
        key_field = cap["key_field"]
        records = cap["records"]
        by_key = {r[key_field]: r for r in records}

        lookup_values = []
        for field in dict.fromkeys(("key", key_field, "user_input")):
            value = str(kwargs.get(field) or "").strip()
            if value:
                lookup_values.append(value)

        candidate_sets = [
            [
                record_key for record_key in by_key
                if _contains_normalized_key(value, record_key)
            ]
            for value in lookup_values
        ]
        exact_lookup = bool(candidate_sets) and all(
            len(candidates) == 1 for candidates in candidate_sets
        )
        if exact_lookup:
            exact_lookup = len({candidates[0] for candidates in candidate_sets}) == 1
        selected_key = candidate_sets[0][0] if exact_lookup else None

        if selected_key:
            return self._render_capability_record(operation, cap, by_key[selected_key])
        if lookup_values:
            return (
                f"# {cap['title']}\n\n"
                f"> No exact normalized {cap['key_label'].lower()} key matched every "
                "supplied identifier, or the request was ambiguous. No action was simulated."
            )
        return self._render_capability_summary(operation, cap)

    def _render_capability_record(self, operation, cap, record) -> str:
        key_field = cap["key_field"]
        key_value = record[key_field]
        lines = [f"# {cap['title']} — {key_value}\n"]
        lines.append(cap["response"] + "\n")
        lines.append(f"**Source System:** {cap['source_system']}")
        mode = "Generative" if cap["generative"] else "Deterministic"
        lines.append(f"**Mode:** {mode}\n")
        lines.append(f"## {cap['key_label']} Record\n")
        for k, v in record.items():
            lines.append(f"- **{_fmt_field(k)}:** {_fmt_value(k, v)}")
        if cap["write"]:
            receipt = _sim_receipt(operation, key_value)
            lines.append("\n## Simulated Write Receipt\n")
            lines.append("> **SIMULATED — no external system was modified.**")
            lines.append(f"- **Receipt ID:** {receipt}")
            lines.append(f"- **Target System:** {cap['source_system']} (simulated)")
            lines.append(f"- **Simulated Action:** {cap['response']}")
        lines.append("\n## Knowledge\n")
        for note in cap["knowledge"]:
            lines.append(f"- {note}")
        return "\n".join(lines)

    def _render_capability_summary(self, operation, cap) -> str:
        key_field = cap["key_field"]
        records = cap["records"]
        columns = list(records[0].keys())
        lines = [f"# {cap['title']}\n"]
        lines.append(cap["response"] + "\n")
        lines.append(f"**Source System:** {cap['source_system']}")
        mode = "Generative" if cap["generative"] else "Deterministic"
        lines.append(f"**Mode:** {mode}")
        lines.append(f"**Records:** {len(records)}\n")
        lines.append("## Records\n")
        lines.append("| " + " | ".join(_fmt_field(c) for c in columns) + " |")
        lines.append("|" + "|".join(["---"] * len(columns)) + "|")
        for r in records:
            lines.append("| " + " | ".join(_fmt_value(c, r[c]) for c in columns) + " |")
        if cap["write"]:
            lines.append(
                "\n> **Write capability — simulated only.** Provide a "
                f"`user_input` or `key` naming a {cap['key_label'].lower()} "
                "to generate a simulated action receipt. No external system is modified."
            )
        lines.append("\n## Knowledge\n")
        for note in cap["knowledge"]:
            lines.append(f"- {note}")
        lines.append(
            f"\n_Tip: pass `user_input` mentioning a {cap['key_label'].lower()} key "
            f"({', '.join(r[key_field] for r in records)}) for an exact-key view._"
        )
        return "\n".join(lines)

    def _alert_triage(self, **kwargs) -> str:
        metrics = _alert_metrics()
        lines = ["# Fraud Alert Triage\n"]
        lines.append(f"**High-Risk Transactions:** {metrics['high_risk_txns']}")
        lines.append(f"**Flagged Amount:** ${metrics['flagged_amount']:,.2f}")
        lines.append(f"**Open Cases:** {metrics['open_cases']}\n")
        flagged = {k: v for k, v in TRANSACTIONS.items() if v["risk_score"] >= 70}
        lines.append("## Flagged Transactions\n")
        lines.append("| TXN ID | Account | Amount | Merchant | Country | Risk | Level |")
        lines.append("|---|---|---|---|---|---|---|")
        for tid, t in flagged.items():
            level = _risk_level(t["risk_score"])
            lines.append(
                f"| {tid} | {t['account']} | ${t['amount']:,.2f} | {t['merchant']} "
                f"| {t['country']} | {t['risk_score']} | {level} |"
            )
        lines.append("\n## Alert Rules Triggered\n")
        for rule_id, rule in ALERT_RULES.items():
            lines.append(f"- **{rule_id} ({rule['name']}):** {rule['description']} [{rule['severity'].upper()}]")
        return "\n".join(lines)

    def _transaction_analysis(self, **kwargs) -> str:
        lines = ["# Transaction Analysis\n"]
        lines.append("## All Monitored Transactions\n")
        lines.append("| TXN ID | Cardholder | Amount | Merchant | Category | Country | Channel | Risk |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for tid, t in TRANSACTIONS.items():
            lines.append(
                f"| {tid} | {t['cardholder']} | ${t['amount']:,.2f} | {t['merchant']} "
                f"| {t['category']} | {t['country']} | {t['channel']} | {t['risk_score']} |"
            )
        accounts = {}
        for t in TRANSACTIONS.values():
            acct = t["account"]
            if acct not in accounts:
                accounts[acct] = {"total": 0, "count": 0, "max_risk": 0}
            accounts[acct]["total"] += t["amount"]
            accounts[acct]["count"] += 1
            accounts[acct]["max_risk"] = max(accounts[acct]["max_risk"], t["risk_score"])
        lines.append("\n## Account-Level Summary\n")
        lines.append("| Account | Transactions | Total Amount | Max Risk |")
        lines.append("|---|---|---|---|")
        for acct, data in accounts.items():
            lines.append(f"| {acct} | {data['count']} | ${data['total']:,.2f} | {data['max_risk']} |")
        return "\n".join(lines)

    def _pattern_detection(self, **kwargs) -> str:
        lines = ["# Fraud Pattern Detection\n"]
        lines.append("## Known Fraud Patterns\n")
        for pid, pattern in FRAUD_PATTERNS.items():
            lines.append(f"### {pid.replace('_', ' ').title()}\n")
            lines.append(f"**Description:** {pattern['description']}")
            lines.append(f"**Frequency:** {pattern['frequency'].title()}\n")
            lines.append("**Indicators:**\n")
            for ind in pattern["indicators"]:
                lines.append(f"- {ind}")
            lines.append("")
        lines.append("## Pattern Matches in Active Cases\n")
        for case_id, case in INVESTIGATION_CASES.items():
            if case["pattern"]:
                pattern = FRAUD_PATTERNS.get(case["pattern"], {})
                lines.append(f"- **{case_id}:** {case['pattern'].replace('_', ' ').title()} — {pattern.get('description', 'N/A')}")
        return "\n".join(lines)

    def _investigation_summary(self, **kwargs) -> str:
        case_id = kwargs.get("case_id")
        if case_id and case_id in INVESTIGATION_CASES:
            case = INVESTIGATION_CASES[case_id]
            lines = [f"# Investigation: {case_id}\n"]
            lines.append(f"- **Status:** {case['status'].replace('_', ' ').title()}")
            lines.append(f"- **Priority:** {case['priority'].title()}")
            lines.append(f"- **Analyst:** {case['analyst']}")
            lines.append(f"- **Opened:** {case['opened']}")
            lines.append(f"- **Pattern:** {case['pattern'].replace('_', ' ').title() if case['pattern'] else 'Under Analysis'}")
            lines.append(f"- **Notes:** {case['notes']}\n")
            lines.append("## Associated Transactions\n")
            for txn_id in case["alert_txns"]:
                t = TRANSACTIONS.get(txn_id, {})
                if t:
                    lines.append(f"- **{txn_id}:** ${t['amount']:,.2f} at {t['merchant']} ({t['country']}) — Risk: {t['risk_score']}")
            lines.append("\n## Rules Triggered\n")
            for rule_id in case["rules_triggered"]:
                rule = ALERT_RULES.get(rule_id, {})
                lines.append(f"- **{rule_id}:** {rule.get('name', 'Unknown')} [{rule.get('severity', 'N/A').upper()}]")
            return "\n".join(lines)

        lines = ["# Investigation Case Summary\n"]
        lines.append("| Case ID | Pattern | Status | Priority | Analyst | Opened |")
        lines.append("|---|---|---|---|---|---|")
        for cid, case in INVESTIGATION_CASES.items():
            pattern = case["pattern"].replace("_", " ").title() if case["pattern"] else "TBD"
            lines.append(
                f"| {cid} | {pattern} | {case['status'].replace('_', ' ').title()} "
                f"| {case['priority'].title()} | {case['analyst']} | {case['opened']} |"
            )
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = FraudDetectionAlertAgent()
    print(agent.perform(operation="alert_triage"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="transaction_analysis"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="pattern_detection"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="investigation_summary", case_id="INV-2025-302"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="alert_triage", user_input="Triage overnight activity and show me ALERT-4471"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="fraud_ring_analysis", user_input="Run pattern analysis on RING-90 and summarize shared behaviors"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="account_takeover_investigation", user_input="Examine the account takeover ring for CUST-5014 and show key indicators"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="case_action", user_input="Create investigation case CASE-2201 and freeze the account"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="performance_report", user_input="Summarize fraud prevention performance for PERF-Q3 and post it to Teams"))
