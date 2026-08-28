"""
FOIA Request Assistant Agent — a template you are meant to mutate.

Supports FOIA request processing with request analysis, document
search, redaction review, and response preparation for government
records officers.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records-request cases over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="request_analysis")
     — with network up, the queue surfaces the tenant's live public-
     records cases such as CAS-260131 "Records request backlog exceeds
     statutory deadline" plus the open tasks tracking it. In this
     template a FOIA/public-records request is represented as a Dynamics
     case (incident) and its work items as Dynamics tasks.
  2. No network? Everything falls back to the embedded demo layer below
     (FOIA_REQUESTS / EXEMPTION_CATEGORIES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FOIA_REQUEST_ASSISTANT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from GovQA/NextRequest), or
     replace _fetch_collection() with your records system API. The
     fields the rest of the file needs are listed in
     _normalize_live_foia_request() — page counts and fee estimates stay
     "n/a — enrichment seam" until you wire your records repository.

OPERATIONS
  request_analysis | document_search | redaction_review |
  response_preparation
  kwargs: operation (required), request_id
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
    "name": "@aibast-agents-library/foia_request_assistant",
    "version": "1.1.0",
    "display_name": "FOIA Request Assistant Agent",
    "description": "Analyzes FOIA queues and drafts responses from a live simulated Dynamics 365 tenant's records cases, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["FOIA", "public-records", "redaction", "transparency", "government"],
    "category": "slg_government",
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
#   export FOIA_REQUEST_ASSISTANT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your records-system client.
# Downstream code only needs the fields from
# _normalize_live_foia_request().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "FOIA_REQUEST_ASSISTANT_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}

# Case-title keywords that mark a tenant case as a public-records item.
_FOIA_KEYWORDS = ("records request", "record request", "foia", "public records")


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


def _normalize_live_foia_request(row, tasks):
    """Project a Dynamics case (incident) record onto the shape this agent
    uses — in this template a FOIA/public-records request IS a Dynamics
    case, and its work items are Dynamics tasks. THIS is the contract
    your replacement data source must meet — a dict with these keys.
    None means 'not available from the case system alone' and the
    renderers label it as an enrichment seam."""
    title = row.get("title", "untitled")
    open_tasks = [
        t for t in tasks
        if t.get("regardingobjectidname") == title and t.get("statecode") == 0
    ]
    return {
        "request_id": row.get("ticketnumber", row.get("incidentid", "")),
        "requester": row.get("customeridname", "Unknown"),
        "subject": title,
        "status": row.get(
            "statecode@OData.Community.Display.V1.FormattedValue", "Active"
        ),
        "priority": row.get(
            "prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"
        ),
        "assigned_analyst": row.get("owneridname", "Unassigned"),
        "due_date": str(row.get("resolveby") or "")[:10] or None,
        "age_days": _age_days(row.get("createdon")),
        "open": row.get("statecode") == 0,
        "open_tasks": len(open_tasks),
        "estimated_pages": None,  # enrichment seam — wire records repository
        "fee_estimate": None,     # enrichment seam
        "_live": True,
    }


def _age_days(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


def _live_foia_queue():
    """Live tenant cases whose titles look records-request-shaped."""
    rows = [
        row for row in _fetch_collection("incidents")
        if any(kw in str(row.get("title", "")).lower() for kw in _FOIA_KEYWORDS)
    ]
    if not rows:
        return []
    tasks = _fetch_collection("tasks")
    queue = [_normalize_live_foia_request(row, tasks) for row in rows]
    return [r for r in queue if r["request_id"]]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Synthetic domain data
# ---------------------------------------------------------------------------

FOIA_REQUESTS = {
    "FOIA-2025-0301": {
        "requester": "Metro Times Newspaper — Rachel Adams",
        "requester_type": "media",
        "submitted": "2025-02-10",
        "subject": "Police department overtime records for FY2024",
        "scope": "All overtime authorization forms, payroll records showing OT for sworn officers, Jan-Dec 2024",
        "status": "document_search",
        "due_date": "2025-03-12",
        "complexity": "high",
        "estimated_pages": 2400,
        "fee_estimate": 360.00,
        "assigned_analyst": "Jennifer Brooks",
    },
    "FOIA-2025-0302": {
        "requester": "Greenway Environmental Coalition — Mark Stanton",
        "requester_type": "nonprofit",
        "submitted": "2025-02-18",
        "subject": "Environmental impact assessments for Riverside development project",
        "scope": "EIA documents, correspondence with developers, planning commission minutes related to project #DP-2024-089",
        "status": "redaction_review",
        "due_date": "2025-03-20",
        "complexity": "medium",
        "estimated_pages": 580,
        "fee_estimate": 87.00,
        "assigned_analyst": "Carlos Vega",
    },
    "FOIA-2025-0303": {
        "requester": "Alan Whitfield — Private Citizen",
        "requester_type": "individual",
        "submitted": "2025-02-25",
        "subject": "Building inspection records for 445 Birch Lane",
        "scope": "All inspection reports, code violation notices, and compliance letters for parcel 034-112-005",
        "status": "response_ready",
        "due_date": "2025-03-27",
        "complexity": "low",
        "estimated_pages": 45,
        "fee_estimate": 6.75,
        "assigned_analyst": "Jennifer Brooks",
    },
    "FOIA-2025-0304": {
        "requester": "Davidson & Associates LLP — Attorney Inquiry",
        "requester_type": "legal",
        "submitted": "2025-03-01",
        "subject": "Communications regarding water utility rate increase proposal",
        "scope": "All internal memos, emails, and meeting notes discussing proposed rate increase from Oct 2024 to present",
        "status": "intake",
        "due_date": "2025-03-31",
        "complexity": "high",
        "estimated_pages": 1800,
        "fee_estimate": 270.00,
        "assigned_analyst": None,
    },
}

DOCUMENT_INVENTORY = {
    "police_records": {"repository": "Records Management System (RMS)", "custodian": "Police Records Unit", "avg_retrieval_days": 3, "digital": True},
    "planning_documents": {"repository": "ProjectDox / Physical Files", "custodian": "Planning Division", "avg_retrieval_days": 5, "digital": True},
    "building_inspections": {"repository": "Accela Permit System", "custodian": "Building Division", "avg_retrieval_days": 1, "digital": True},
    "financial_records": {"repository": "Tyler Munis ERP", "custodian": "Finance Department", "avg_retrieval_days": 2, "digital": True},
    "correspondence": {"repository": "Microsoft 365 / Exchange", "custodian": "IT Department", "avg_retrieval_days": 4, "digital": True},
    "council_minutes": {"repository": "Granicus / City Clerk", "custodian": "City Clerk", "avg_retrieval_days": 1, "digital": True},
    "utility_records": {"repository": "CIS Infinity", "custodian": "Utility Billing", "avg_retrieval_days": 2, "digital": True},
}

EXEMPTION_CATEGORIES = {
    "EX-1": {"code": "Personnel Privacy", "description": "Personal information of employees (SSN, home address, medical)", "statute": "Gov. Code 6254(c)"},
    "EX-2": {"code": "Law Enforcement", "description": "Records of investigations, intelligence, or security procedures", "statute": "Gov. Code 6254(f)"},
    "EX-3": {"code": "Attorney-Client Privilege", "description": "Communications between agency and legal counsel", "statute": "Gov. Code 6254(k)"},
    "EX-4": {"code": "Deliberative Process", "description": "Preliminary drafts, notes, and internal deliberations", "statute": "Gov. Code 6255(a)"},
    "EX-5": {"code": "Trade Secrets", "description": "Proprietary business information submitted by third parties", "statute": "Gov. Code 6254(k)"},
    "EX-6": {"code": "Critical Infrastructure", "description": "Security plans, vulnerability assessments", "statute": "Gov. Code 6254(aa)"},
}

RESPONSE_TEMPLATES = {
    "full_grant": "All responsive documents are provided herein. No exemptions have been applied.",
    "partial_grant": "Responsive documents are provided with redactions applied pursuant to the exemptions noted below.",
    "denial": "After thorough review, the requested records are exempt from disclosure under the exemptions cited below.",
    "no_records": "A diligent search has been conducted and no records responsive to your request were located.",
    "fee_notice": "The estimated cost for processing this request is {fee}. Please remit payment to proceed.",
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _request_metrics():
    """Calculate FOIA processing metrics."""
    total = len(FOIA_REQUESTS)
    by_status = {}
    for r in FOIA_REQUESTS.values():
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    total_pages = sum(r["estimated_pages"] for r in FOIA_REQUESTS.values())
    total_fees = sum(r["fee_estimate"] for r in FOIA_REQUESTS.values())
    return {"total": total, "by_status": by_status, "total_pages": total_pages, "total_fees": total_fees}


def _applicable_exemptions(request):
    """Determine potentially applicable exemptions based on request subject."""
    exemptions = []
    subject_lower = request["subject"].lower()
    if "police" in subject_lower or "officer" in subject_lower:
        exemptions.extend(["EX-1", "EX-2"])
    if "correspondence" in request["scope"].lower() or "memo" in request["scope"].lower():
        exemptions.extend(["EX-3", "EX-4"])
    if "development" in subject_lower or "developer" in request["scope"].lower():
        exemptions.append("EX-5")
    if not exemptions:
        exemptions.append("EX-1")
    return exemptions


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class FOIARequestAssistantAgent(BasicAgent):
    """FOIA request assistant for government records management."""

    def __init__(self):
        self.name = "FOIARequestAssistantAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "FOIA Request Assistant Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "request_analysis",
                            "document_search",
                            "redaction_review",
                            "response_preparation",
                        ],
                    },
                    "request_id": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "request_analysis")
        dispatch = {
            "request_analysis": self._request_analysis,
            "document_search": self._document_search,
            "redaction_review": self._redaction_review,
            "response_preparation": self._response_preparation,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _live_request_analysis(self, queue):
        """Records-request queue from live tenant cases (preferred online)."""
        lines = [
            "# FOIA Request Analysis — Live Tenant Cases\n",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "In this template a public-records request is a Dynamics case.",
            "Pass `request_id` (e.g. FOIA-2025-0301) for the embedded demo view.\n",
            f"**Matched Requests:** {len(queue)} "
            f"({sum(1 for r in queue if r['open'])} open)\n",
            "## Request Queue\n",
            "| Case | Requester | Subject | Priority | Status | Due | Open Tasks | Pages | Fees |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
        for r in sorted(queue, key=lambda x: x["request_id"]):
            pages = "n/a — enrichment seam" if r["estimated_pages"] is None else f"{r['estimated_pages']:,}"
            fees = "n/a — enrichment seam" if r["fee_estimate"] is None else f"${r['fee_estimate']:,.2f}"
            lines.append(
                f"| {r['request_id']} | {r['requester']} | {r['subject']} "
                f"| {r['priority']} | {r['status']} | {r['due_date'] or 'n/a'} "
                f"| {r['open_tasks']} | {pages} | {fees} |"
            )
        overdue = [
            r for r in queue
            if r["open"] and r["due_date"] and r["age_days"] > 0
        ]
        lines.append("")
        lines.append(
            f"**Analyst load:** " + ", ".join(
                sorted({f"{r['assigned_analyst']}" for r in queue})
            )
        )
        lines.append(
            "Page counts and fee estimates need your records repository — "
            "wire it at the LIVE DATA SEAM."
        )
        return "\n".join(lines)

    def _request_analysis(self, **kwargs) -> str:
        if not kwargs.get("request_id"):
            queue = _live_foia_queue()
            if queue:
                return self._live_request_analysis(queue)
        metrics = _request_metrics()
        lines = ["# FOIA Request Analysis\n"]
        lines.append(f"**Active Requests:** {metrics['total']}")
        lines.append(f"**Total Estimated Pages:** {metrics['total_pages']:,}")
        lines.append(f"**Total Estimated Fees:** ${metrics['total_fees']:,.2f}\n")
        lines.append("## Request Queue\n")
        lines.append("| Request ID | Requester | Subject | Complexity | Status | Due |")
        lines.append("|---|---|---|---|---|---|")
        for rid, r in FOIA_REQUESTS.items():
            lines.append(
                f"| {rid} | {r['requester']} | {r['subject']} "
                f"| {r['complexity'].title()} | {r['status'].replace('_', ' ').title()} | {r['due_date']} |"
            )
        lines.append("\n## Status Breakdown\n")
        for status, count in metrics["by_status"].items():
            lines.append(f"- {status.replace('_', ' ').title()}: {count}")
        return "\n".join(lines)

    def _document_search(self, **kwargs) -> str:
        request_id = kwargs.get("request_id", "FOIA-2025-0301")
        req = FOIA_REQUESTS.get(request_id, list(FOIA_REQUESTS.values())[0])
        lines = [f"# Document Search: {request_id}\n"]
        lines.append(f"**Subject:** {req['subject']}")
        lines.append(f"**Scope:** {req['scope']}")
        lines.append(f"**Estimated Pages:** {req['estimated_pages']:,}\n")
        lines.append("## Relevant Document Repositories\n")
        lines.append("| Repository | Custodian | Retrieval Est. | Digital |")
        lines.append("|---|---|---|---|")
        for repo_id, repo in DOCUMENT_INVENTORY.items():
            digital = "Yes" if repo["digital"] else "No"
            lines.append(
                f"| {repo['repository']} | {repo['custodian']} "
                f"| {repo['avg_retrieval_days']} days | {digital} |"
            )
        exemptions = _applicable_exemptions(req)
        lines.append("\n## Potentially Applicable Exemptions\n")
        for ex_id in exemptions:
            ex = EXEMPTION_CATEGORIES[ex_id]
            lines.append(f"- **{ex_id} ({ex['code']}):** {ex['description']} — {ex['statute']}")
        return "\n".join(lines)

    def _redaction_review(self, **kwargs) -> str:
        lines = ["# Redaction Review Guide\n"]
        lines.append("## Exemption Categories\n")
        lines.append("| Code | Category | Description | Statute |")
        lines.append("|---|---|---|---|")
        for ex_id, ex in EXEMPTION_CATEGORIES.items():
            lines.append(f"| {ex_id} | {ex['code']} | {ex['description']} | {ex['statute']} |")
        lines.append("\n## Requests in Redaction Review\n")
        in_review = {k: v for k, v in FOIA_REQUESTS.items() if v["status"] == "redaction_review"}
        if in_review:
            for rid, req in in_review.items():
                exemptions = _applicable_exemptions(req)
                lines.append(f"### {rid}: {req['subject']}\n")
                lines.append(f"- **Analyst:** {req['assigned_analyst']}")
                lines.append(f"- **Pages:** {req['estimated_pages']}")
                lines.append(f"- **Due:** {req['due_date']}")
                lines.append(f"- **Applicable Exemptions:** {', '.join(exemptions)}\n")
        else:
            lines.append("No requests currently in redaction review.")
        lines.append("\n## Redaction Best Practices\n")
        practices = [
            "Apply exemptions narrowly — redact only information covered by statute",
            "Log each redaction with exemption code and page reference",
            "Use Vaughn index format for withheld documents",
            "Review redactions for consistency across document set",
            "Verify no metadata leakage in redacted PDFs",
        ]
        for p in practices:
            lines.append(f"- {p}")
        return "\n".join(lines)

    def _response_preparation(self, **kwargs) -> str:
        request_id = kwargs.get("request_id", "FOIA-2025-0303")
        req = FOIA_REQUESTS.get(request_id, list(FOIA_REQUESTS.values())[2])
        exemptions = _applicable_exemptions(req)
        lines = [f"# Response Preparation: {request_id}\n"]
        lines.append(f"- **Requester:** {req['requester']}")
        lines.append(f"- **Subject:** {req['subject']}")
        lines.append(f"- **Pages:** {req['estimated_pages']}")
        lines.append(f"- **Fee Estimate:** ${req['fee_estimate']:,.2f}")
        lines.append(f"- **Status:** {req['status'].replace('_', ' ').title()}\n")
        lines.append("## Response Templates\n")
        for tpl_name, tpl_text in RESPONSE_TEMPLATES.items():
            display_text = tpl_text.replace("{fee}", f"${req['fee_estimate']:,.2f}")
            lines.append(f"### {tpl_name.replace('_', ' ').title()}\n")
            lines.append(f"> {display_text}\n")
        lines.append("## Response Checklist\n")
        checklist = [
            "Responsive documents identified and compiled",
            "Exemption review completed",
            "Redactions applied and logged",
            "Vaughn index prepared (if applicable)",
            "Fee calculation finalized",
            "Response letter drafted",
            "Supervisory review completed",
            "Response mailed/emailed to requester",
        ]
        for item in checklist:
            lines.append(f"- [ ] {item}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = FOIARequestAssistantAgent()
    print("LIVE TENANT RECORDS-REQUEST QUEUE (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="request_analysis"))
    print("\n" + "=" * 80 + "\n")
    print("EMBEDDED DEMO REQUEST (works offline)")
    print(agent.perform(operation="request_analysis", request_id="FOIA-2025-0301"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="document_search", request_id="FOIA-2025-0301"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="redaction_review"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="response_preparation", request_id="FOIA-2025-0303"))
