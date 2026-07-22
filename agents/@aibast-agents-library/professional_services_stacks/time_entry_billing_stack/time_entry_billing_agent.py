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
