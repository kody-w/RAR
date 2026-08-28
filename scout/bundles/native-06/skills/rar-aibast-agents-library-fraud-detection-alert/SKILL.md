---
name: "rar-aibast-agents-library-fraud-detection-alert"
description: "Triages fraud alerts and tracks investigations from a live simulated Dynamics 365 tenant (cases as fraud cases), with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/fraud_detection_alert", "rar_sha256": "b2ef284db2b4e93836c6668a16feeafcd78f49cd2a8913f9ce54dbeb128b214a", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["fraud", "detection", "alerts", "transactions", "investigation", "financial-services"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/fraud_detection_alert`. The original RAPP
agent is preserved byte-for-byte in `fraud_detection_alert_agent.py` and in the RCI capsule.

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

Fraud Detection & Alert Agent — a template you are meant to mutate.

Provides alert triage, transaction analysis, pattern detection, and
investigation summaries for financial fraud operations teams. In this
template a fraud investigation is represented as a Dynamics 365 case —
the tenant has no native fraud-case entity, so the service-case queue
stands in for the fraud ops investigation queue (its seeded "Disputed
card transaction under investigation" case is exactly that story).

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `investigation_summary` operation pulls
     live case records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="investigation_summary")
     and look for Bluegrass Credit Union's "Disputed card transaction
     under investigation" case.
  2. No network? Everything falls back to the embedded demo layer below
     (TRANSACTIONS / INVESTIGATION_CASES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FRAUD_DETECTION_ALERT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your fraud case manager),
     or replace _fetch_collection() with your own client. The fields the
     rest of the file needs are listed in _normalize_live_case() — the
     fraud pattern column stays "n/a — enrichment seam" until you wire
     your detection models.

OPERATIONS
  alert_triage | transaction_analysis | pattern_detection
  | investigation_summary | fraud_ring_analysis
  | account_takeover_investigation | case_action | performance_report
  kwargs: operation (required), case_id, account, user_input, key

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "account": {
      "type": "string"
    },
    "case_id": {
      "type": "string"
    },
    "key": {
      "description": "Optional exact record key for direct lookup on the v1.1.0 fraud-monitoring capabilities.",
      "type": "string"
    },
    "operation": {
      "enum": [
        "alert_triage",
        "transaction_analysis",
        "pattern_detection",
        "investigation_summary",
        "fraud_ring_analysis",
        "account_takeover_investigation",
        "case_action",
        "performance_report"
      ],
      "type": "string"
    },
    "user_input": {
      "description": "Optional free-text request; an exact record key (e.g. ALERT-4471, RING-90, CUST-5014, CASE-2201, PERF-Q3) mentioned here triggers an exact-key lookup.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `fraud_detection_alert_agent.py` and embedded as the fenced Python below (sha256 b2ef284db2b4e938…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `fraud_detection_alert_agent.py` first:

```bash
python3 fraud_detection_alert_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 fraud_detection_alert_agent.py   # or on stdin
python3 fraud_detection_alert_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Fraud Detection & Alert Agent — a template you are meant to mutate.

Provides alert triage, transaction analysis, pattern detection, and
investigation summaries for financial fraud operations teams. In this
template a fraud investigation is represented as a Dynamics 365 case —
the tenant has no native fraud-case entity, so the service-case queue
stands in for the fraud ops investigation queue (its seeded "Disputed
card transaction under investigation" case is exactly that story).

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `investigation_summary` operation pulls
     live case records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="investigation_summary")
     and look for Bluegrass Credit Union's "Disputed card transaction
     under investigation" case.
  2. No network? Everything falls back to the embedded demo layer below
     (TRANSACTIONS / INVESTIGATION_CASES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FRAUD_DETECTION_ALERT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your fraud case manager),
     or replace _fetch_collection() with your own client. The fields the
     rest of the file needs are listed in _normalize_live_case() — the
     fraud pattern column stays "n/a — enrichment seam" until you wire
     your detection models.

OPERATIONS
  alert_triage | transaction_analysis | pattern_detection
  | investigation_summary | fraud_ring_analysis
  | account_takeover_investigation | case_action | performance_report
  kwargs: operation (required), case_id, account, user_input, key
"""

import sys
import os
import hashlib

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json as _json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/fraud_detection_alert",
    "version": "1.2.0",
    "display_name": "Fraud Detection & Alert Agent",
    "description": "Triages fraud alerts and tracks investigations from a live simulated Dynamics 365 tenant (cases as fraud cases), with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["fraud", "detection", "alerts", "transactions", "investigation", "financial-services"],
    "category": "financial_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ---------------------------------------------------------------------------
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export FRAUD_DETECTION_ALERT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your fraud-case-manager client.
# Downstream code only needs the fields produced by _normalize_live_case().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "FRAUD_DETECTION_ALERT_DATA_URL",
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
            rows = _json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _normalize_live_case(row):
    """Project a Dynamics case onto the investigation shape this agent
    uses. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not knowable from the CRM alone'
    and the renderers label it as an enrichment seam."""
    state_map = {0: "open", 1: "resolved", 2: "canceled"}
    priority_map = {1: "high", 2: "medium", 3: "low"}
    return {
        "customer": row.get("customeridname", "Unknown"),
        "title": row.get("title", "untitled"),
        "pattern": None,  # enrichment seam — wire your fraud detection models
        "status": state_map.get(row.get("statecode"), "open"),
        "analyst": row.get("owneridname", ""),
        "opened": str(row.get("createdon", ""))[:10],
        "priority": priority_map.get(row.get("prioritycode"), "medium"),
        "_live": True,
    }


def _live_investigations():
    """case-keyed dict of live tenant investigations; {} when offline."""
    rows = _fetch_collection("incidents")
    if not rows:
        return {}
    return {
        f"INV-{str(row.get('incidentid', ''))[:8]}": _normalize_live_case(row)
        for row in rows
        if row.get("incidentid")
    }


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
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

        live = _live_investigations()
        if live:
            open_first = sorted(
                live.items(),
                key=lambda kv: (kv[1]["status"] != "open", kv[1]["priority"] != "high"),
            )
            lines = ["# Investigation Case Summary (live tenant)\n"]
            lines.append("| Case ID | Customer | Title | Pattern | Status | Priority | Analyst | Opened |")
            lines.append("|---|---|---|---|---|---|---|---|")
            for cid, case in open_first:
                pattern = case["pattern"].replace("_", " ").title() if case["pattern"] else "n/a — enrichment seam"
                lines.append(
                    f"| {cid} | {case['customer']} | {case['title']} | {pattern} "
                    f"| {case['status'].title()} | {case['priority'].title()} "
                    f"| {case['analyst']} | {case['opened']} |"
                )
            lines.append(
                "\n_Source: live Static Dynamics 365 tenant — service cases "
                "reinterpreted as the fraud ops investigation queue. The pattern "
                "column is an enrichment seam (wire your detection models)._"
            )
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
        lines.append("\n_Source: embedded demo layer (offline fallback)._")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = FraudDetectionAlertAgent()
    print("=" * 80)
    print("EMBEDDED DEMO TRIAGE (works offline)")
    print(agent.perform(operation="alert_triage"))
    print("\n" + "=" * 80 + "\n")
    print("LIVE TENANT INVESTIGATION QUEUE (cases fetched over HTTP; falls back offline)")
    print(agent.perform(operation="investigation_summary"))
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
