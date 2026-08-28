---
name: "rar-aibast-agents-library-foia-request-assistant"
description: "Analyzes FOIA queues and drafts responses from a live simulated Dynamics 365 tenant's records cases, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/foia_request_assistant", "rar_sha256": "18fd8a77430845666b98e622f50fea1c65cff93a06ca536d7193f8d1a4917eb1", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["FOIA", "public-records", "redaction", "transparency", "government"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/foia_request_assistant`. The original RAPP
agent is preserved byte-for-byte in `foia_request_assistant_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "enum": [
        "request_analysis",
        "document_search",
        "redaction_review",
        "response_preparation"
      ],
      "type": "string"
    },
    "request_id": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `foia_request_assistant_agent.py` and embedded as the fenced Python below (sha256 18fd8a7743084566…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `foia_request_assistant_agent.py` first:

```bash
python3 foia_request_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 foia_request_assistant_agent.py   # or on stdin
python3 foia_request_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/617ac+jWJbmX7FiPnRWOSMwizHkqGeG1WCzbwY6W5Hsi9kXY6iu/z7Xjjcis7JL3RpprFDIhnvPPetzniPd92+fgnnK2+HTL58okaZM69PPn+JkjIaim4q2eT1ugmrdknHHqyK16+dkBt+DJt7FQ5BO425Ixq5tRvAwHdp6F+yq4pHsxqKeq2BK4h27NkFdROMOxY+7KWmCZvqX166oHeJxFwVg58+7pZhyIHTXpmlVNMkuTup2lwZVFQbR/QvQKXkGdVcl46df/u3ff/5UgO+ffvnbp6gKRvDo00s1IwG6jRM1jsU4gUOoLGkmsLMKmgws6VZgZgN+d8mQtkMNHsVJuvv49dOYVOnPu7/+9b4EQzb+Zff5f+3Gafjl12b38WnByuDlkt2/7r4t+pIl00+/fvrx4tdPP+9+/TR8U+Nr8HIbUOXXT3/5XUhcjF0wRTmQ8bffn74+/2zjL7uXVl++/vnNz3/eGrfRXANrv45JMET57zv/9OLn/3xmHEQv3cEZjyJZ/njmP775J1u/hf1rNyRd8N0Dv2//z2//IOLvv3/NQSpVyQA88t05b7/+8OofvFeku6advu/45R81GpJpHppd+uunv/6VG4Z2+OWvf93Zzb1pl+YPwfvtbz++//23L79++l3Ih4AP6T/9SIVPfwf51oBkmN/+eKXb//gfO7mIhnZs02lnRu087Ya5mYo6+bX5tbHyYtyBf1OeAKGPZBiLsEo+1nVDWyZvQSDXd7/9n6AIg3H6HLySdfxcFeEQDCuUtkXwe9i/Z/RvX3YWkNkORVaAVNgZlKb92ry3vs4Drh6T4QFKLlyn5DNI68+vL7sCWP3PBX597/3Srb+9CxosfOlsMCIoy26cq+TLy55bnjQf2kegRJNnEs1AbNVGQIe0qF71C45uK1D208v28V5UFQgnqPGpHda3bOCfX17CfvvtN2Bw/mvzrR7R3TeoGSGw4Ic6u8+fgTEACbJ8+rVJorzd/cvf/v4vu//Y/Ve73sJfZ2jAwA/vAw0vpqrsQCTfhQACA0KZBPHb+3/7+4dLgZgG5CCIVZEWybfNAIfuSfzdv6ZAfUaO+C5MgF+BT+uuHaaiyXbF9GUnprsf+oJDX68ARO7ydpwAknVJEydNtAKpATDnhydfuTyCTBzT9efdPCbvU38DCfBWsf4ageW/7WRG201tW4H/Xmq+F4HNbVMA9/+I/rfnQMgAsJX+LuLLTnnl3+5VgV0+BB9npMG3uLTD7vt2IDzYNQAAmhe0Ji9XvWvkm3vAIuCZ6COkn18x30VtXYPAjt/Pfq95A77VgoxOhl9B+X9L9GBI3ngPVFl32VzEQRMl//Mjpca8nav47T+g6UvSRxTij6i8c/Ddez4QfvcD4ndvjN/9OiMHGAMGAJO7V9PZre38PrVOXquAcfUM7PmWzubcfQvQW+ZHTbzqMkqAXBDRdy/6/vwH5u6+Y+nLrjeY7n5g5O4DI79l+gf07f4AfTuQNLvs5YDmm4jv7Q/0uyICCPHWTFBvO0sQzZ3FyZpEWdzuphpX8wVR8JedCpwFkvblobB9grzbdXNVjd/a7Ye8z9/VfrfV3evAb0UgWJb2AXXvLv2OWNWGoMOu7zwF7jZfIY/+Wb/e/US9IrqTgib5kKK+Fd+Z6yvPxu8hGNcGSH5JiYMp+BnA9S4CXgImF0H1avPtcH+Rh3XJkyH5y3cIz6epG3+BoHsbr5+XLxkIwBx+KVpofKv0Of5Q6TNQCQq6AnpJhx7kFwT6kGAN6y8/evkPhP/X/6odf6j8jnaTTC/VdnP389s1b5azG+cBlMoHHPxgLm9/d3NYAcU+RP0DmQHbQIMPxh1DmZ8R/ACjMGiXxseS7wF68ZqqzQCaRkkSjx+CXvbO79qMAUa9mNCvn3ZdNX9TAdgFai0YgQunAez/AT/NG3c/ZPwoguCd4dCHqsOfFCheX98to3kFP3gB1vfQf0h6mbP7qWii4hXBv3zrEaBw3q4q3nEH237ky1uzL6+9CACe9rtT//eOexU+0BCo+6J049v4V1W+jErqMIljoMGb8lXBCvIsTKp2+VDip5cRXw1OtznTMnfQjnNBdViiqnxlQImcVUPkzL98j+ZL4jdMa97IFwHQy5PvBn2wy7eO6JedHNyTVx0BtBiAKdN7tyQ63I6lLGpncpT8TZUXq5k+ZPxRna+UaYqmRSnW19eOr7YhvcwC+b1TWZCin8c86IBpoAF0bfGqo9dRP5IG1OUP57VD9vMLkN/dKnm+EApsfNfquX3oFKQkz+kDAP/yWvlDCgg2KMSvaQKo09eorapvqPvTX76l9uvEHwk6vst1R2niG9i/I0KRVPH3jjn+QJk3zDev7HxjaVW8UaJoPnZ9bUCtBVWxJV9fJfH1jxTjpx8B6UA0QK+YX633lT9pAkI+AqoEMnR85fv6vRw/NVDwfVfSgHaTv6ASeD6oQRG86FX1xvUFNKF/tOrVccfiVTZvGFU1zqBeCfJGzj8DACARf2LF4Mmf2e7uP75t/ScUFzz/Rgx/+QOr/Ol1CtAr/svPPw4s4tfwAUASSPj0SwOw+udPINjJfzOuvA6qE4C242vAAW0JHDIVyfvXjwNfP5JmBkPMv/0nhHsNcP9oIHjyZwPfj/6zdZ/AbDWt3UtHQHhBwb7I7x8MAsf+6fXH+5ftL2V+1/B3SW34YrwvSS9c+jZ7/e0TsDF4wfiHlR+kGCwHBPjz+KIGEPzl8NIzGL5RPPDu/4kuf+wFNQiIG9gME2lMBKcThh4I7IjjeEgSCY4g6fGQJgEc4ccoTUk0OOBRcETx+ASTaErEcICR8CkJYSBvBGkXJV9f3Kd46ROm4RGJQjg9nIiEPGHJET7gSUzCeHhM44QkcDJEyWPy+1YA2vGHkd+MennwB3N/OePD1r99CnEMrBSwUaS+fRiIdKIE1UKjkyD3SBbMhOF3BzOTqVYdOL3mvt8ap8fNO7gB4q+33Fsp0bobjMA+7/Im9kOvRQIUpZFAXpQ0lp8FYVrVc6g7a356l03TD8nQQZCfnaXoEQBFnmpNu1i+7wpaRoqz7F+2lbI2mYag0/aAcCHyA/EZS01xYwb5bBNcveQRl5nj/RYsgnMKkNmWujivZFNeuVuAsuLV1bl79qxPFdFErhrRJJwsdkseW3+cvettumms2KRxVshpbIgenUq9hQ2YkG0oJjAQK9I+ZZvP4/PcUIq4eZK0WLZN2eJ8Pt+NZIvY3hnavMDU4VQ8IW+vPSzOGLVtPaUs4bPkqPGwQ55v2DYhyVJYN2o09wGDemZaUwZik3utNqEHrWjcPm8EqSX4uxjyGB2iSJqWhHnTs3Rf22GWiaUMPdTz/oFIm8zh3PPgZee5Xu+wS/HkVUGi81Ct7IViXPccMWIhoU3m0JzU5o1SDTRpO7LXki7l0DyTH7VEJHjRVWhVY+73x5jN6bjMLUyr18dp9nKOhCmjLtKLXJ4iJLwrD8eF0A6nYUUOb5h3kl3BIjcdTRO6zleoYnMpndPZeoT7khHXEjb5EMyP3LwvOELk7+nN6HSr9OGqihXj6HfhQTFEcRxdyxdRgSJ4c1FFpBYEk5L6ukFJr3B7D9Ua5r6ezbDb61G3xyPCz2L2EJKQk5ySJT5t0mCKJzGeE2EeDEittfLOzAJfZMve93vu4HXHrJn3rGjxVYP3VZs0jFMy3pMOuZEfHW72EXWxhxGvupo+NL7cn5Bsbomh58o9I48gvU6suzAjquIHEfPVpcyeUeE+bhfrdvMY6n7hmpCVVDnO6VS5b/FEVseaazaNzHTnjPEn6vywsVNfRHula2PtQnvo8lCy1CZGfQ433iydMmXZhHAY+ghRszHsyUhZFBp/ClZInMmS3mtWgbL3s4fmaOTauCA4HXPkgstR1mimP54hHpMeZplxt/x6OZ+o4xwTzkzD2SXjZG67sBYKJY0gWqNfUvGo0Gt0NT31Zi6mEQhiwcpeaR8FjBCOiMxdtjYZSCgjWrkZscw8jAak7Y1rYupWIndGK4W52RV+lhz82rOsYbGgccNVKSIplmYYz1jCozRsJxxhG1d4XhXJgKObcaYFzxtkxC9GM1aRU7vHxKwjFadvt+HsIfJqhj6mSbY/q8dpSjpewpuJ6Zg4pjC5u+0p6syo+UXed1dKp/z+nquU5fIpVIiRQtHN+T7Mgej2/Rn2lhxblAMoCibga33wjmxhMCQrniXn1Nm5v+h4w5hXsWMnAaKUnMBc3rsOByYoH75pXctF1ITRMzddXYjksiasQ7k2hQ18i+6RVUccQWT5SFbY8VpPVVP3tY6Y90yG1/0jSQ2JPd7pO+/RZERVw3Pe1qV5mAfJVZibq7JJGxRbiZyJSXfSk+lox8Hj9pVgIp49wXy8p0e39XmCOHs8w2hqjBIWNu1lbKb36gGzHSmekU3a+6WuinEYi+7tiEk8LJw9tsYoOBGLvUekxsaK+1rDE+NEjOFt24tidtGZpiA5uuZP7CMT0+1kLnn22NsY8zyJVwsnFuzkUQjS8OG0jQl7E0O5eFQbUnj7WHMfLt43p72QY+Q2zlmscKxXnhZO4FrSUW2fi5qhWUL26kXLEmaahp6oi2ERXpb7N4tzCJe5ZEex8crZXg4P/dyvK8kkKMyk1xvqjmZj3lZbhP3zarjLE70a7aMgL9MeE/yY1O29f6GIlecvXg4XonnOm0bjDrUXGbLr4iDBA5+MLK195Hhpk0J93J9j9llM/HBoEZHGqf1dLyPePWnU8hzae40v2iiXVOYWEOLbz6IwoKWkLUVz7lhBh8I9byf+PDJOKDJIHmfGYsCrsgkrbRA8NF4dvRFIwRw4686Rd+8hDAHcnC4QtCchaH4QLFSMSXa4JskJuzuHNW88b6aEhV+ch+YpwaUGOW8tOKSq4ooZur4G6iOYGf5gUFTgmk0qDBfheHZ163BmZvJONDC+rMfc3IvzXrT1G5U/+OiRpx6too8Yt0S2L+ZMv5Ts1Gz+cenlMeMUM3Xp5WhSylV0jWqrl0fjZ0NB0unL3y7lXVban+kc5+iIFzmpmnzdEsk9AGSTPJwk6Gg4z2LVgU35Elvr3VZ1sdFXr/M2Zrngl+4qjxGh7n0vJPG98mgVNo4mqhfZ7AQ1uIi2nAwZeTZeIJHmrtLtdMYvSC4fcxqVrJy7l5sViS161fEpvy5eQHYhW6KUi3mQnvkHOZMKIRjNw9q2T+7BX09lqt6etZm5BkQGtwvuKdcuhxwBe1gXtXS2lqRuMcTdGLzSPW8KsbAsBcfT7va+7zcjnyPbv5x1fVsYdrjScwRxHddVKHZt9UORP7yL5vqrNvc0T8Y3s2YKfTYY//KksGu3qvRcsr1edYTL+xF1PePUds1a7+5BYFqZCLg1zxefQvgohKjFiNicH0/O/eTnOllAjn4IIaHxkojsVUX20tuQrJB60xFMuWpCv2gZb5BHn5RaW4YYlALdvJQ7NFUu2PXCtOnCO/KdVax1iBVoxvMAlzHNPD05zD3IJdZFSHMSH2HBehhVkAsVaaKAHQbB9JUOYkPuVvsK/IRgO+O62Hrqp1qmJm4L7hrE6rR17/Epvj4ZtMgXDgv7ebFTI8b3Eb4XL0/Nd7Bj2h3Png1Re4dRq1Q6SqaRi4K6jBl0lUgeK2LzantkL8am78eaZT41g3RkrksfShBoHmU6EM87Kq4zUR5hOft0iUCJqfKumnli94BcYVx2uwYrwTHisBcy88JRPdUYxZKjV8uo713L9RBhjOqS05YQZ2W6nEe5sXU7j5C5WgTCf3CQetm6Q8EKVGGfmQXAtCX7CgdTfd9769PWHXKSp2uWZIyXS7X6YI3DyRYd/igc0yRTuEDi2rbmplZ8nKs507imqMW7X26rKEdqiLJbZ0fPyI9iIWkcXBfsG2Wsh3qC02MqWt7Qkwh9G7ULR6/rgaDYebALhpcklLkAgiGTNsuF7AETaPLc29cLduDgzZtQKhfHwwLATEepMEN7tIDZoupA/EmW5VU4mwt9tE0iiLV9h/JU6T/huxcc9y0qC/v5nECGrkiituG9igbnluJOmOm0h2P+vNn3ZclYLPTgceHTx7wcb+6wjV1mb7qU47oO6rA1njzgOWyAXTj9wetYHbOU5fWJWuswxkMditUej2d0Tw8TkoYFqhKCFjATL9S+6HluEQ+SphoHV6bVhJ6Y/aQi7eHg1D3ZuedgsIU1xDJVA2Am8cNly1QnHxdJ4C6IpvV50AbobARMlh01s9bLzN98gAs4424rN+ajUF4V20zGbUHu+flZcBeXU7Y14pgqMzIMrpnQ1BBQSR1u6wJJpPJUunUcbNBTQUlsf5qxBJuPj4NzPJ2y5sRSB5Y7LN6C3+Lj3GFN6LtwwJNLMPLx6hqoudw4O3fOWunEEhnyIbPSyIilsmsI1XZBIyjcBFq66wddyHRULCvVZvzz9WYHlYJDG4ed3VrxprliKB1CrqK9PHxWY7y+PzLGEx/VITp0uLXSDWSAMgEQlGUnguJhJV875T5hjKoblz3NKv69PcIEPRGKxQyO8zDsyLgnRN/sH2ZGuRLBIUpizO0B5W9upkjt3D7i+9jenokGDZCe2nkdP/IiapangsjlevJewVvwx42JhgjRHbayPUG9NVRyZqgj1D4GYtXhRxUNZzDMCRUExgVofOxPozALXTnpJyUcxyPHtc7Icp41ospTWIlj/tBEKHfQ454d6OcxffKB5aBgWKPn+2hQySVfqtPppjOagTno+YmSUDgZbdwItr/vSi2BC8mi8qOs4E1fLWdvKJ0QJTizAMOP8tRli10gd1X7Yri4xEofVmkeTScFieMmnoMJ07FM02NhSUbJKBwTLYPjoVCtpyQ3X1fEm31isPsOvnWICg05C3WnPWEbYZY/u7S4p9cWrk6aCbEDmO0hT3J7hWkWAGI9bEJRqF1T2H/yGWspRbhKVIs82dgH3bJLSSUZVikXi1mNBqWyfKXtqf1+wZ6q6K/5CB+X1UJp/ibe54stajV95qg6UexLN8NH9CaRne7fvbF6HpaMzguV8AdAkKYL79jalDxVXe64YPDtxFZLM4M1Gg8iNmvpWy8DrcuWWwcV7sGEG9Fp5j7pNqTH61ke0eHKs7xIUG3B9d2TwXve9WVSlSohkqD+NECQPfCQszwONR0/0tCJlkkmD6Nz4t3hmLTI+fEg69GTo8iezl7qmUt6gVcheBpDxon39LBUS+2Mh8KRCuWYL40n30pXQq6sMjbUHU1Ncz0XgN6p+5UMYbVSrg2iWXnNJky92vtDlDs4kchNYrLPaHG6+/XZO/4kd8mBcE7z8Y4z050aomtAq4Ny4RBLkGzJIajxyAeswRq0viWaWxoo+QhPe0Bb6s3iG6TI4IYIenVOFXW+Pqlw4BObX6GQTEA/ilBpwGJWIoN2zWqh9I508difn088v+7r5ZSiJ5O8BrouPcOCvp1Yi6ofcP+IB6yVrqGiBhkL44fbTTn0s2YO/RXGT6uNuvJ4C5LLU5B5vucCnaTO6kEnOfPMHX2nWpeWux/48S5lD72iTMo4c8PR5kf0GFGsLgpTb8mJacMSk/eUZFd0UioawXhUlBsEpwueiOLP67iBYfCSH3BEGye2Rh+k1QvTA1L8NrldkF6LpXyNGoHAbk9Ma3x12yCmweZBgJQs4O503mmObp+HgV0GvQ02rbW3liWtzvDheaRwB0lKaQyVSvLZmpZtsfNHpI0pe0IclICzu2maWAuqOT5iB1kpQZi4E26C9rv58hHKzyxkLZd+Dn2Ea8hMnY/rw6uoQ3NCnDvf2EjURweqobzroj2fvZ9MzRUW0bO2xsLIBAhdnDKuTlwwx0iH6NoTN3WJGRlKcDAhMe7dubEJ1A3TGScJWdI3Wb6C9kXMAboSF6NnAOUVx+PNgBwwX+Q8RT3j5tDCjHnOLHXUgiWR2oaKNvumNbG22FaFj5ip80VaqGVBBDfh7kY6c1coby5z/lTeuf202ft1SPYRTxyGK+pXiWZxCfU40fu4dcIb1INJwUMPoqsGaVztM+mOxpF7p0uIuB3JVWjnXqozH+NZVqRo18zOvFoEsyCug2zkLN23bWZjeMNeR8qLBsouw7OHqgmyJF4n5UlAKZkceTeM57l70FqFHxA8jPkHxWapEwSnJ4l/Imh9dA/3EIBeDT32FswdTsz9+hCRSPCreTYpMO1xa1etSgmv3MrS56S9k7HLLXfkyfex6kvLwS5LY5v6w1Pp6CJ05RIKNNxkzJxKAXM38aW2eDbGxSN9NOmgn+d1Wm97o+kdueYfR7yrj5IlHVrZtYtUqFjB7FCqLIoIT+oTwJAb4DbReRlbMjg3zdWbCzzdO6l259T7jdCcdcEeERhYnoqNYSU9XmS2uozomHOg/eiWP9sNfVs092IfNl1PTrdE6PS9kZMXwMPSyeWn28BVmtBSzV0iKFV8Yo2dtHVLc8pJRGSkpTTKEOLOxSh9qAyn6sSO9DbAjsSFYx55r0kFpBkHuQlU6lGrNkyix4p3LwjNmtnUQZkDplRM39qBMpGzTu25LEMsGcC+CnEXi790iL+xJf0wx9XlNjg31uMyrC3mVkMTzKIxx6RzdI6r4csAPSst1rgxTrUGQDST4N26ESge6vQluHlyR7e0V+qlhcTL4Ym3qkLf+KQIjjrv2b5xe3hOJjDGLaln6RLARox0Ltx56gLy5XaRGLMV+evsF+sm1GOn3pjzosSLiF1G0c4k3pRK38qC1KYrdqhmMGEKeVxcDofZb7fIYS6sUbLajSQWwJXA8I/nnV+osN4qNQA4TOHrasP4vhOo4CxdnKfJ9O7iqwfnOUdp2vol+kiZJ1LafHroGCgeeNVsI//pXui0RZQVs8t2fzzBF7dKBv7a5peSQLXDQRzDfDM4+9xhfXztt2gwCPfRZ2fa6usNq/Nu5g7C7AXCYdoGnB0kqvAxvZ5mm7odI0kT4uExlsjyOB42nrSoxgLzx5gPi7UFz8OK6nXbFr1z6QG04ohfJ4ZuPVkKhaiG8Q3sMhxLGbmrtnb34BtKLKQvD9FSQEdMT4pcfAi9fZwbAyHxtEoaLOO8vU0RlLdkz4GBDFe6PGNlj/kle08qCrFbdRoPeEV5AXYKSKMQiseEkdehdrvJjn3JgUIVf4y4JLHteJXRs77xMXtF082xG5+Qb82eyR8yDjMDjKvj6h/Pk7PUSY+D0eiacjCkCGutAUwJb0apa8qzHYsz5q4uMW01PiQVTqgzVg/9nslu27Jf9Xiqh7ypXB0TIP20XEjcJSx4CWEoTPSyrc373KZn5ZqabYcQ9hah9/gyXK9eNT2ka6HxNnNUhzt81znrItKbrD73FXVn79OJVvZTKlDn88YGtQuICiEIamjHAm/3nO4g6KjA7hXacLKDZbSp7tfNe6TPOGmSjhW12+nuMqzy7F26PtUpLE32YjuVI+zNEiuS/h46qmjNqzPyK35kTS+nD3ZzcrVK5HBdOvnVJFRSu27SOD5St0QIsrmNBVpNU/ic4hBXUrm2rDSp1717PtJJUF7Hmr+BqWB0ybpsZoOA137kz97+OPSplAv38KxIvewLc4BvG4OrZhWaW3BYkud4OUGpR+zTHvXEGUf30pG8Hp0kfJzzrSMX8pBhaT4RcYAiGjOZ5l5ZmDyMYCo4qofRGpwz7A79mquAbq6PMIHdBlrhqEWDhxyQTJHeTpA/8fDGqBcyevS+yhWi0QYVnfEHA+2YziT1xF87Ml2OpC1GWgOp8XkyPX/aJyWTCihoX7dOyq5hJFtTQp09/HQlry4yikLCuQe6zaBgWNWOwI9BGq1XEnYFgzJ4mRb18Gy52Q3dXJp74IJDtAo/WKIMh+dj8lTO5ZNtryAlnZZF0KZ8wJEC+DSuEVvHCZdbsBymRxl7uLM9kMq9aziKCmEADAy7uF+M+aBrEC+rF2v/LAe6UYoZpXsw90K9FATFEI9yqaHkPs/a83KybG8yLfrwlGEa28v9uHapSo3pM/FO0FkpPSK0yYxvTi2cB4emPGwIpLgN76WEXyM5iqpPIEY7qUYxP7ID7szWqErXe4pv3NEUhD19egZq7zbViLYTpeH7Z7KVEXJQmHOLQAOxBDdxX3uJitsH9BLoSVxHyd59PjFUQHCfJq+PZIrl+Vybjnsy93ofB24yefztLikNIQn2yg5UYsTnUCfVZCGd0pe1cw2b9eV2S1pt5v0nwxzvpwMxBEc+9mf+sXmO4oEmaxV4eIru5RU+WLZ7vDyhC7bc+qpK7Z7vAwNYk46kOoe3VkQp7xleibIW0jEwxLsDdVxiiq2NVDM7et4B7ftL0MpP2pGuMWwvfXRbsArfUhC7I7E5hy3FWoPsySlekc7nhqcTXctJxa7I8KRWL87QsvEfo0WsyR3Q8BkfVrscIFExH0nbCWMp9eXWe6eYd+5kfpC6aL969aNALbLGqqvbHZt169vRUI94gPr6nAxkcAso/nz1OH042C6iSiQyy+UpZKTW4eir2VF31/Vgd3T6teOqhRz2uJ3qnJ1uyTHIwtXv9cmZz8W0VS76qA8qv1i3tuvvsWKGruahSScMYTCILePDyFLLvQv6kOhclkd7lu+OCFGXFWevOpLv+6PC7mVyZQ1kyZHEKpDWCy5ErFpwS6IDdyyv0PEhhMxg49MN0MLDPMJ8wrYnz1cNY59mM8gAHBGbR5SEHDnijTbF14cXlv11OqKTME01QqL9Sm8wvNLI7eZDLMI2k7ClhiilSU711RZot2yC7z6/MPrNvdp1fi6rY/ZYa6cjSFy8jHtSoeY7aOeGg8kriFM3K/3FYG3Gma4IbQG/ckiPECHv3kSmXev9nUzyM3SApeoR47FyZSVYltCLcrNGmiMZLys7qMaEOjhQBjcvVzCJ9zCbPbkbnc0W6CTnqw2LxkUNs0FRFvUsqYensYlK6ttHxR77lb3XMrlo8kqdGsZxD6L1LBoR1Vv9lD0Wfd8PFB2Q5xnLokPW9CdrkC+4pEAlF0P5hbktOZFFNySgCq/HBktd1r0mXQQ9zjHOl3K2OiDoUg5L6wvwI7tFWbM36hkQr6Cwi0czPZdqsJNija7essqEnbc+w/ohdzkZydkyb13uhAt3tGrChi0fGQ18aLYn2Z5VEyIongbNf8Av1xnDHEY0ND5POdeN42ZFbCm5d5lj4lsomot3f66+i0M4N5CmHJwcoS8EE9UJ8dmK6XxvnqHnn48HU8OOZ+yAxMerJAoaIMeZYtw95rQXzkvoIad4tR7ys6lmNPLhMJrn5+An8t45xdOmq3pf+7nAXnzefV4yRSL88W4kp4z0hbQHTk/ScyZpTyo5Pa6s2WxhX+F+si5nGAmM8b6tNhURlb6tXnQoIN6pUUaC/JUqmXZUAwRvLxcM7vpkm5T1oZydxMKvh9UiyLu+cU1ZG3pvwU857qjSLHLyrFGtEa0KstYKdRoUHiXoyVdoeVOwQ5HxAmWzw/EK7ds6hC9DqOXhRhEPwnQT6UzOhCXLwxRIB7fQ8eN1MG2iAG3UxW91kTdwv0B8V3BusBS9b+bD2lf2MJ3KDYGfE8l67aOLNq7vJQO1/LTNxbUvDzk/5TElEJKYJlYftpuDUez1ymyi07GlUD0Q4n6y19uiDG04no+nxgsyMdfQm+il8T1kyuwE007hLvbdX+eRR/lGfhw5wSsRJGTla4YnxozC8/WmKta44D6WQHXl9nkyamSczTU7PCv5dCD3wcaYRky6iA3t3STUIEjXhTMKaJ5+dHNrWx5Bey5SqM/KPRghZi/tQtFejjptMwX3LPeuRlJHtrw+GEh10biiTy1rVI12JB1mMa0u2bf6hhIVUL+6WjcESgOsUeDtjm5ltl4gCk6CB8VAwc0kaPV+mD1D3gLQlkF6T2ShXPBtD1uGEO35BBvPDj08/CodbOXkBUG+v5ypPo7GmC8Odyh7MnQirSMvCVrf4/fYENzJDvmguSjdpuCtIi1XlGIiHyUEOPf2UowXhh3ACdor56Fir9mEeuFNORd2T8y9G4b7gTKaYkhXoyhRAta6Q1MEK8QgT6GXII87ziCbbhwRFG0/xnXJWjS0meFImRHJJAiU5A/17Kc0vMehe5yJgLwwGnwXbAuUrU3pOJxfebVzCex0U9Ss1c2lZHxi6htEy/cJS2xctmznvUie3LK16Mdzfx447ZHOWneFMPOSnkx8INwUmszHysaT190LvTmZIRneZvEcZ6YmeNhIdiuJjjftWUpwoV0kJK8bIXW3/rQ3qr34EI2TY1bP9FmXQz+4c5XuNeM2+4cpKlFFHw/QUaRP5QotAr4vMRLnM4qi/vVfP/386XVx7uOm139z7/51L+j/2/WkbzeJ2sfromqUfLsaFsS/vM/65b9T5N9//jRExUuN96WrsZqz79eU/tmVq88ved9vG3/+45Wrb1cMv0ZtMyXP6fvFtynIXn+687759rrk9g93Uv94Pw18n4agGbtgeN2ZBz9/vzb9UvL95xTve2Lwl5eqf/+/9sHI1cE0AAA= -->
