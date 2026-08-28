---
name: "rar-aibast-agents-library-time-entry-billing"
description: "Audits time entries and tracks receivables from a live simulated Dynamics 365 tenant invoice ledger, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/time_entry_billing", "rar_sha256": "93014aaa8e8a0bf9e43818e5eda920ca2b5f73a697cacbbc66d26765d6b7f712", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["billing", "time-entry", "invoicing", "audit", "professional-services"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/time_entry_billing`. The original RAPP
agent is preserved byte-for-byte in `time_entry_billing_agent.py` and in the RCI capsule.

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

Time Entry & Billing Agent — a template you are meant to mutate.

Processes consultant time entries, validates against project budgets and
billing rules, identifies unbilled hours, and prepares invoice packages
with audit-ready documentation.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's invoices feed the receivables view directly — e.g.
     invoice "INV-260102" for Marigold Field Services ($2,880, Active).
     Try: perform(operation="unbilled_report")
  2. No network? Everything falls back to the embedded demo layer below
     (TIME_ENTRIES / PROJECT_BUDGETS / INVOICE_HISTORY) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     TIME_ENTRY_BILLING_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your PSA/finance system), or
     replace _fetch_collection() with a QuickBooks/NetSuite AR client.
     Fields the rest of the file needs are listed in
     _normalize_live_invoice() — days outstanding is computed from the
     live due date; collection notes render as "n/a — enrichment seam"
     until you wire your AR workflow.

OPERATIONS
  unbilled_report | billing_summary | time_entry_audit
  | invoice_preparation | exception_resolution | billing_close_package
  kwargs: operation (required), record_id, entry_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "entry_id": {
      "description": "Time-entry identifier, such as TE-9004; selects its exception-resolution record.",
      "type": "string"
    },
    "operation": {
      "description": "Operation to run; defaults to unbilled_report when omitted.",
      "enum": [
        "unbilled_report",
        "billing_summary",
        "time_entry_audit",
        "invoice_preparation",
        "exception_resolution",
        "billing_close_package"
      ],
      "type": "string"
    },
    "record_id": {
      "description": "Evidence record identifier for exception_resolution or billing_close_package, such as TEB-701 or TEB-CLOSE-701.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `time_entry_billing_agent.py` and embedded as the fenced Python below (sha256 93014aaa8e8a0bf9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `time_entry_billing_agent.py` first:

```bash
python3 time_entry_billing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 time_entry_billing_agent.py   # or on stdin
python3 time_entry_billing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Time Entry & Billing Agent — a template you are meant to mutate.

Processes consultant time entries, validates against project budgets and
billing rules, identifies unbilled hours, and prepares invoice packages
with audit-ready documentation.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's invoices feed the receivables view directly — e.g.
     invoice "INV-260102" for Marigold Field Services ($2,880, Active).
     Try: perform(operation="unbilled_report")
  2. No network? Everything falls back to the embedded demo layer below
     (TIME_ENTRIES / PROJECT_BUDGETS / INVOICE_HISTORY) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     TIME_ENTRY_BILLING_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your PSA/finance system), or
     replace _fetch_collection() with a QuickBooks/NetSuite AR client.
     Fields the rest of the file needs are listed in
     _normalize_live_invoice() — days outstanding is computed from the
     live due date; collection notes render as "n/a — enrichment seam"
     until you wire your AR workflow.

OPERATIONS
  unbilled_report | billing_summary | time_entry_audit
  | invoice_preparation | exception_resolution | billing_close_package
  kwargs: operation (required), record_id, entry_id
"""

import sys
import os
import json
import urllib.request
from datetime import datetime, timezone
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/time_entry_billing",
    "version": "1.2.0",
    "display_name": "Time Entry & Billing Agent",
    "description": "Audits time entries and tracks receivables from a live simulated Dynamics 365 tenant invoice ledger, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["billing", "time-entry", "invoicing", "audit", "professional-services"],
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
#   export TIME_ENTRY_BILLING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your finance/AR client.
# Downstream code only needs the fields from _normalize_live_invoice().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "TIME_ENTRY_BILLING_DATA_URL",
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


_LIVE_INVOICE_STATE = {0: "outstanding", 1: "paid", 2: "cancelled"}


def _days_past_due(iso_date):
    """Real computation: whole days elapsed since the due date (0 if not
    yet due or unparseable)."""
    try:
        due = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - due).days)
    except (ValueError, TypeError):
        return 0


def _normalize_live_invoice(row):
    """Project a Dynamics invoice onto the receivables row this agent
    renders. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not knowable from the invoice
    record alone' and the renderer labels it as an enrichment seam (wire
    your AR workflow for collection notes)."""
    return {
        "invoice_id": row.get("invoicenumber", "?"),
        "client": row.get("customeridname", "Unknown"),
        "amount": float(row.get("totalamount") or 0),
        "due_date": str(row.get("duedate") or "")[:10] or "n/a",
        "status": _LIVE_INVOICE_STATE.get(row.get("statecode"), "unknown"),
        "days_outstanding": _days_past_due(row.get("duedate")),
        "collection_notes": None,  # enrichment seam — wire your AR workflow
        "_live": True,
    }


def _live_invoices():
    """Invoices from the live tenant ledger; [] when offline."""
    return [_normalize_live_invoice(r) for r in _fetch_collection("invoices")]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

TIME_ENTRIES = [
    {"id": "TE-9001", "consultant": "Elena Vasquez", "project": "TechCorp Transformation",
     "date": "2026-03-10", "hours": 8.0, "rate": 275, "category": "billable", "description": "Cloud architecture design workshop",
     "approved": True},
    {"id": "TE-9002", "consultant": "Elena Vasquez", "project": "TechCorp Transformation",
     "date": "2026-03-11", "hours": 9.5, "rate": 275, "category": "billable", "description": "Azure landing zone implementation",
     "approved": True},
    {"id": "TE-9003", "consultant": "Michael Chen", "project": "Apex Analytics Platform",
     "date": "2026-03-10", "hours": 7.5, "rate": 260, "category": "billable", "description": "Data pipeline development",
     "approved": True},
    {"id": "TE-9004", "consultant": "Michael Chen", "project": "Apex Analytics Platform",
     "date": "2026-03-11", "hours": 8.0, "rate": 260, "category": "billable", "description": "",
     "approved": False},
    {"id": "TE-9005", "consultant": "Priya Sharma", "project": "Pinnacle Energy ERP",
     "date": "2026-03-10", "hours": 10.0, "rate": 310, "category": "billable", "description": "Program status review and steering committee",
     "approved": True},
    {"id": "TE-9006", "consultant": "Priya Sharma", "project": "Pinnacle Energy ERP",
     "date": "2026-03-11", "hours": 8.0, "rate": 310, "category": "billable", "description": "Sprint planning and backlog grooming",
     "approved": True},
    {"id": "TE-9007", "consultant": "Lisa Tanaka", "project": "Atlas Security Audit",
     "date": "2026-03-10", "hours": 6.0, "rate": 290, "category": "billable", "description": "Identity and access management review",
     "approved": True},
    {"id": "TE-9008", "consultant": "Lisa Tanaka", "project": "Atlas Security Audit",
     "date": "2026-03-11", "hours": 8.5, "rate": 290, "category": "billable", "description": "Penetration test coordination",
     "approved": True},
    {"id": "TE-9009", "consultant": "Amanda Foster", "project": "Metro Transit Portal",
     "date": "2026-03-10", "hours": 8.0, "rate": 165, "category": "billable", "description": "User research session facilitation",
     "approved": True},
    {"id": "TE-9010", "consultant": "Amanda Foster", "project": "Metro Transit Portal",
     "date": "2026-03-11", "hours": 4.0, "rate": 165, "category": "non_billable", "description": "Internal design review",
     "approved": True},
    {"id": "TE-9011", "consultant": "Elena Vasquez", "project": "TechCorp Transformation",
     "date": "2026-03-12", "hours": 11.0, "rate": 412, "category": "billable", "description": "Weekend migration cutover",
     "approved": False},
    {"id": "TE-9012", "consultant": "David Okafor", "project": "Internal Training",
     "date": "2026-03-10", "hours": 8.0, "rate": 0, "category": "non_billable", "description": "Power BI certification prep",
     "approved": True},
]

BILLING_RATES = {
    "Elena Vasquez": {"standard": 275, "overtime": 412, "max_daily_hours": 10},
    "Michael Chen": {"standard": 260, "overtime": 390, "max_daily_hours": 10},
    "Priya Sharma": {"standard": 310, "overtime": 465, "max_daily_hours": 10},
    "Lisa Tanaka": {"standard": 290, "overtime": 435, "max_daily_hours": 10},
    "Amanda Foster": {"standard": 165, "overtime": 248, "max_daily_hours": 10},
}

PROJECT_BUDGETS = {
    "TechCorp Transformation": {"total_budget": 850000, "billed_to_date": 682400, "remaining": 167600,
                                  "contract_type": "T&M", "client": "TechCorp Industries"},
    "Apex Analytics Platform": {"total_budget": 520000, "billed_to_date": 398000, "remaining": 122000,
                                 "contract_type": "T&M", "client": "Apex Manufacturing"},
    "Pinnacle Energy ERP": {"total_budget": 1200000, "billed_to_date": 744000, "remaining": 456000,
                             "contract_type": "Fixed Fee", "client": "Pinnacle Energy"},
    "Atlas Security Audit": {"total_budget": 185000, "billed_to_date": 156600, "remaining": 28400,
                              "contract_type": "T&M", "client": "Atlas Financial Group"},
    "Metro Transit Portal": {"total_budget": 340000, "billed_to_date": 218000, "remaining": 122000,
                              "contract_type": "T&M", "client": "Metro Transit Authority"},
}

INVOICE_HISTORY = [
    {"invoice_id": "INV-2026-201", "client": "TechCorp Industries", "amount": 142500, "date": "2026-02-28",
     "status": "paid", "days_outstanding": 0},
    {"invoice_id": "INV-2026-202", "client": "Apex Manufacturing", "amount": 98800, "date": "2026-02-28",
     "status": "paid", "days_outstanding": 0},
    {"invoice_id": "INV-2026-203", "client": "Pinnacle Energy", "amount": 186000, "date": "2026-02-28",
     "status": "outstanding", "days_outstanding": 17},
    {"invoice_id": "INV-2026-204", "client": "Atlas Financial Group", "amount": 52200, "date": "2026-02-28",
     "status": "outstanding", "days_outstanding": 17},
    {"invoice_id": "INV-2026-205", "client": "Metro Transit Authority", "amount": 46200, "date": "2026-02-28",
     "status": "overdue", "days_outstanding": 45},
]

EVIDENCE_CAPABILITIES = {
    "exception_resolution": {
        "title": "Guided Billing Exception Resolution",
        "write": False,
        "records": [
            {
                "record_id": "TEB-701",
                "entry_id": "TE-9004",
                "classification": "billable / missing description",
                "draft_description": "Apex data-pipeline development supported by project backlog item AP-214",
                "contract_evidence": "T&M statement of work permits data engineering delivery",
                "review_action": "approve drafted description or return to consultant",
            },
            {
                "record_id": "TEB-702",
                "entry_id": "TE-9011",
                "classification": "premium billing / disputed hours",
                "draft_description": "Weekend Azure migration cutover under approved change order CO-18",
                "contract_evidence": "CO-18 authorizes weekend premium rate of $412 per hour",
                "review_action": "attach evidence and route for billing-manager approval",
            },
        ],
    },
    "billing_close_package": {
        "title": "Invoice, Revenue Recognition, and Audit Package",
        "write": True,
        "records": [
            {
                "record_id": "TEB-CLOSE-701",
                "client": "TechCorp Industries",
                "invoice_action": "issue approved entries; hold disputed TE-9011 for review",
                "write_off_exposure": "$0 approved; $4,532 pending evidence review",
                "revenue_recognition": "$4,812.50 approved for invoicing this cycle",
                "supporting_evidence": "contract clause, CO-18, Teams approval, and time-entry log",
                "audit_trail": "source, classification, reviewer, decision, and timestamp",
            },
            {
                "record_id": "TEB-CLOSE-702",
                "client": "Apex Manufacturing",
                "invoice_action": "issue approved TE-9003; hold TE-9004 until description approval",
                "write_off_exposure": "$2,080 pending description review",
                "revenue_recognition": "$1,950 approved for invoicing this cycle",
                "supporting_evidence": "T&M statement of work, backlog item AP-214, and time-entry log",
                "audit_trail": "source, classification, reviewer, decision, and timestamp",
            },
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _total_billable_hours():
    """Sum of billable hours across all entries."""
    return sum(te["hours"] for te in TIME_ENTRIES if te["category"] == "billable")


def _total_billable_value():
    """Sum of billable dollar value."""
    return sum(te["hours"] * te["rate"] for te in TIME_ENTRIES if te["category"] == "billable")


def _unbilled_entries():
    """Entries that are billable but not yet approved."""
    return [te for te in TIME_ENTRIES if te["category"] == "billable" and not te["approved"]]


def _audit_flags():
    """Return entries with potential issues."""
    flags = []
    for te in TIME_ENTRIES:
        issues = []
        if not te["description"]:
            issues.append("Missing description")
        rates = BILLING_RATES.get(te["consultant"], {})
        if te["hours"] > rates.get("max_daily_hours", 10):
            issues.append(f"Exceeds {rates.get('max_daily_hours', 10)}-hour daily limit")
        if te["rate"] > rates.get("overtime", 999) and te["category"] == "billable":
            issues.append("Rate exceeds overtime cap")
        if te["rate"] != rates.get("standard", te["rate"]) and te["rate"] != rates.get("overtime", te["rate"]):
            issues.append(f"Non-standard rate (${te['rate']}/hr)")
        if issues:
            flags.append({"entry": te, "issues": issues})
    return flags


def _budget_status(project_name):
    """Return budget consumption percentage."""
    budget = PROJECT_BUDGETS.get(project_name, {})
    if not budget or budget["total_budget"] == 0:
        return 0
    return round(budget["billed_to_date"] / budget["total_budget"] * 100, 1)


def _evidence_matches(user_input, records):
    """Match explicit billing IDs without substituting another client."""
    tokens = {
        "".join(ch for ch in token.upper() if ch.isalnum())
        for token in str(user_input).split()
    }
    return [
        record for record in records
        if "".join(ch for ch in record["record_id"].upper() if ch.isalnum()) in tokens
    ]


def _evidence_selector(capability, kwargs):
    """Resolve explicit evidence or time-entry identifiers to evidence record IDs."""
    if kwargs.get("record_id"):
        return kwargs["record_id"]
    if kwargs.get("entry_id"):
        record_ids = [
            record["record_id"]
            for record in EVIDENCE_CAPABILITIES[capability]["records"]
            if record.get("entry_id") == kwargs["entry_id"]
        ]
        return " ".join(record_ids) or kwargs["entry_id"]
    return kwargs.get("user_input", "")


def _render_evidence_operation(capability, user_input=""):
    spec = EVIDENCE_CAPABILITIES[capability]
    records = spec["records"]
    matches = _evidence_matches(user_input, records) if user_input else records
    lines = [f"## {spec['title']}\n"]
    if user_input and not matches:
        lines.append("No exact `record_id` match was found; no substitute billing record was used.")
    else:
        lines.append("Deterministic contract- and project-grounded billing records:")
        for record in matches:
            lines.append("- " + "; ".join(f"{key}: {value}" for key, value in record.items()))
    if spec["write"]:
        target = matches[0]["record_id"] if matches else "NO-MATCH"
        lines.extend([
            "\n### Simulated Write Receipt",
            f"- receipt_id: SIM-{capability.upper()}-{target}",
            "- status: simulated",
            "- target_systems: Dynamics 365, SharePoint, and Microsoft Teams",
            "- No invoice was issued and no revenue record changed; this is a preview-only write.",
        ])
    else:
        lines.append("\n_Read-only guided review; no external system changed._")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class TimeEntryBillingAgent(BasicAgent):
    """Processes time entries and generates billing reports."""

    def __init__(self):
        self.name = "TimeEntryBillingAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "operations": [
                "unbilled_report",
                "billing_summary",
                "time_entry_audit",
                "invoice_preparation",
                "exception_resolution",
                "billing_close_package",
            ],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "Operation to run; defaults to unbilled_report when omitted.",
                        "enum": [
                            "unbilled_report",
                            "billing_summary",
                            "time_entry_audit",
                            "invoice_preparation",
                            "exception_resolution",
                            "billing_close_package",
                        ],
                    },
                    "record_id": {
                        "type": "string",
                        "description": "Evidence record identifier for exception_resolution or billing_close_package, such as TEB-701 or TEB-CLOSE-701.",
                    },
                    "entry_id": {
                        "type": "string",
                        "description": "Time-entry identifier, such as TE-9004; selects its exception-resolution record.",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "unbilled_report")
        dispatch = {
            "unbilled_report": self._unbilled_report,
            "billing_summary": self._billing_summary,
            "time_entry_audit": self._time_entry_audit,
            "invoice_preparation": self._invoice_preparation,
            "exception_resolution": self._exception_resolution,
            "billing_close_package": self._billing_close_package,
        }
        handler = dispatch.get(operation)
        if handler is None:
            return f"**Error:** Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        return handler(**kwargs)

    # ------------------------------------------------------------------
    def _unbilled_report(self, **kwargs) -> str:
        lines = ["## Unbilled Hours Report\n"]
        unbilled = _unbilled_entries()
        total_unbilled_val = sum(te["hours"] * te["rate"] for te in unbilled)
        lines.append(f"**Unbilled entries:** {len(unbilled)}")
        lines.append(f"**Unbilled value:** ${total_unbilled_val:,.2f}\n")

        if unbilled:
            lines.append("| Entry ID | Consultant | Project | Date | Hours | Rate | Value | Issue |")
            lines.append("|----------|-----------|---------|------|-------|------|-------|-------|")
            for te in unbilled:
                val = te["hours"] * te["rate"]
                issue = "Needs approval"
                if not te["description"]:
                    issue += "; missing description"
                lines.append(
                    f"| {te['id']} | {te['consultant']} | {te['project'][:20]} | {te['date']} | "
                    f"{te['hours']} | ${te['rate']} | ${val:,.2f} | {issue} |"
                )
        else:
            lines.append("All billable entries are approved.")

        lines.append("\n### Outstanding Invoices\n")
        lines.append("| Invoice | Client | Amount | Date | Status | Days Out |")
        lines.append("|---------|--------|--------|------|--------|----------|")
        for inv in INVOICE_HISTORY:
            if inv["status"] != "paid":
                lines.append(
                    f"| {inv['invoice_id']} | {inv['client']} | ${inv['amount']:,.2f} | "
                    f"{inv['date']} | **{inv['status'].upper()}** | {inv['days_outstanding']} |"
                )
        total_outstanding = sum(inv["amount"] for inv in INVOICE_HISTORY if inv["status"] != "paid")
        lines.append(f"\n**Total outstanding:** ${total_outstanding:,.2f}")
        live = _live_invoices()
        if live:
            seam = "n/a — enrichment seam"
            lines.append("\n### Live Tenant Invoice Ledger (Dynamics invoices)\n")
            lines.append("| Invoice | Client | Amount | Due Date | Status | Days Past Due | Collection Notes |")
            lines.append("|---------|--------|--------|----------|--------|---------------|------------------|")
            for inv in live:
                lines.append(
                    f"| {inv['invoice_id']} | {inv['client']} | ${inv['amount']:,.2f} | "
                    f"{inv['due_date']} | **{inv['status'].upper()}** | {inv['days_outstanding']} | "
                    f"{inv['collection_notes'] or seam} |"
                )
            live_open = sum(i["amount"] for i in live if i["status"] == "outstanding")
            lines.append(f"\n**Live tenant outstanding:** ${live_open:,.2f} "
                         "(days past due computed from the live due dates)")
        else:
            lines.append("\n_Live tenant unreachable — showing embedded demo invoices only._")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _billing_summary(self, **kwargs) -> str:
        lines = ["## Billing Summary\n"]
        total_hrs = _total_billable_hours()
        total_val = _total_billable_value()
        non_billable = sum(te["hours"] for te in TIME_ENTRIES if te["category"] == "non_billable")
        total_all = total_hrs + non_billable
        billable_pct = round(total_hrs / total_all * 100, 1) if total_all else 0

        lines.append(f"**Total hours logged:** {total_all}")
        lines.append(f"**Billable hours:** {total_hrs} ({billable_pct}%)")
        lines.append(f"**Non-billable hours:** {non_billable}")
        lines.append(f"**Total billable value:** ${total_val:,.2f}\n")

        lines.append("### By Project\n")
        lines.append("| Project | Client | Type | Hours | Value | Budget Used | Remaining |")
        lines.append("|---------|--------|------|-------|-------|-------------|-----------|")
        project_hours = {}
        project_value = {}
        for te in TIME_ENTRIES:
            if te["category"] == "billable":
                project_hours[te["project"]] = project_hours.get(te["project"], 0) + te["hours"]
                project_value[te["project"]] = project_value.get(te["project"], 0) + te["hours"] * te["rate"]
        for proj in PROJECT_BUDGETS:
            hrs = project_hours.get(proj, 0)
            val = project_value.get(proj, 0)
            budget = PROJECT_BUDGETS[proj]
            used_pct = _budget_status(proj)
            lines.append(
                f"| {proj[:24]} | {budget['client'][:18]} | {budget['contract_type']} | "
                f"{hrs} | ${val:,.2f} | {used_pct}% | ${budget['remaining']:,.0f} |"
            )

        lines.append("\n### By Consultant\n")
        lines.append("| Consultant | Hours | Billable Value | Avg Rate |")
        lines.append("|-----------|-------|---------------|----------|")
        consultant_data = {}
        for te in TIME_ENTRIES:
            if te["category"] == "billable":
                name = te["consultant"]
                if name not in consultant_data:
                    consultant_data[name] = {"hours": 0, "value": 0}
                consultant_data[name]["hours"] += te["hours"]
                consultant_data[name]["value"] += te["hours"] * te["rate"]
        for name, data in sorted(consultant_data.items(), key=lambda x: x[1]["value"], reverse=True):
            avg_rate = round(data["value"] / data["hours"], 2) if data["hours"] else 0
            lines.append(f"| {name} | {data['hours']} | ${data['value']:,.2f} | ${avg_rate} |")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _time_entry_audit(self, **kwargs) -> str:
        lines = ["## Time Entry Audit Report\n"]
        flags = _audit_flags()
        lines.append(f"**Total entries reviewed:** {len(TIME_ENTRIES)}")
        lines.append(f"**Entries flagged:** {len(flags)}\n")

        if flags:
            lines.append("| Entry ID | Consultant | Date | Hours | Rate | Issues |")
            lines.append("|----------|-----------|------|-------|------|--------|")
            for f in flags:
                te = f["entry"]
                issues_str = "; ".join(f["issues"])
                lines.append(
                    f"| {te['id']} | {te['consultant']} | {te['date']} | {te['hours']} | "
                    f"${te['rate']} | {issues_str} |"
                )
        else:
            lines.append("All entries pass audit checks.")

        lines.append("\n### Budget Alert\n")
        lines.append("| Project | Budget Used | Remaining | Status |")
        lines.append("|---------|------------|-----------|--------|")
        for proj, budget in PROJECT_BUDGETS.items():
            used = _budget_status(proj)
            status = "CRITICAL" if used >= 95 else "WARNING" if used >= 80 else "OK"
            lines.append(f"| {proj[:24]} | {used}% | ${budget['remaining']:,.0f} | **{status}** |")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _invoice_preparation(self, **kwargs) -> str:
        lines = ["## Invoice Preparation\n"]
        lines.append("### Invoices Ready to Generate\n")

        # Group approved billable entries by project/client
        by_project = {}
        for te in TIME_ENTRIES:
            if te["category"] == "billable" and te["approved"]:
                proj = te["project"]
                if proj not in by_project:
                    by_project[proj] = {"hours": 0, "value": 0, "entries": 0}
                by_project[proj]["hours"] += te["hours"]
                by_project[proj]["value"] += te["hours"] * te["rate"]
                by_project[proj]["entries"] += 1

        lines.append("| Project | Client | Entries | Hours | Invoice Amount | Contract Type |")
        lines.append("|---------|--------|---------|-------|---------------|---------------|")
        grand_total = 0
        for proj, data in by_project.items():
            budget = PROJECT_BUDGETS.get(proj, {})
            client = budget.get("client", "Unknown")
            ctype = budget.get("contract_type", "T&M")
            grand_total += data["value"]
            lines.append(
                f"| {proj[:24]} | {client[:18]} | {data['entries']} | {data['hours']} | "
                f"${data['value']:,.2f} | {ctype} |"
            )
        lines.append(f"\n**Grand total ready to invoice:** ${grand_total:,.2f}")

        unbilled = _unbilled_entries()
        unbilled_val = sum(te["hours"] * te["rate"] for te in unbilled)
        lines.append(f"**Pending approval (not included):** ${unbilled_val:,.2f}")

        lines.append("\n### Invoice History\n")
        lines.append("| Invoice | Client | Amount | Date | Status |")
        lines.append("|---------|--------|--------|------|--------|")
        for inv in INVOICE_HISTORY:
            lines.append(
                f"| {inv['invoice_id']} | {inv['client']} | ${inv['amount']:,.2f} | "
                f"{inv['date']} | {inv['status']} |"
            )
        total_billed = sum(inv["amount"] for inv in INVOICE_HISTORY)
        total_collected = sum(inv["amount"] for inv in INVOICE_HISTORY if inv["status"] == "paid")
        lines.append(f"\n**Total billed (last cycle):** ${total_billed:,.2f}")
        lines.append(f"**Total collected:** ${total_collected:,.2f}")
        lines.append(f"**Collection rate:** {round(total_collected/total_billed*100,1)}%")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _exception_resolution(self, **kwargs) -> str:
        return _render_evidence_operation(
            "exception_resolution",
            _evidence_selector("exception_resolution", kwargs),
        )

    # ------------------------------------------------------------------
    def _billing_close_package(self, **kwargs) -> str:
        return _render_evidence_operation(
            "billing_close_package",
            _evidence_selector("billing_close_package", kwargs),
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = TimeEntryBillingAgent()
    print("=" * 72)
    print("EMBEDDED DEMO BILLING + LIVE TENANT INVOICE LEDGER")
    print("(live section fetched over HTTP; falls back offline)")
    print("=" * 72)
    print(agent.perform(operation="unbilled_report"))
    print()
    for op in agent.metadata["operations"][1:]:
        print("=" * 72)
        print(agent.perform(operation=op))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
