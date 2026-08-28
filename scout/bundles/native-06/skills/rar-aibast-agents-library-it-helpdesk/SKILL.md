---
name: "rar-aibast-agents-library-it-helpdesk"
description: "Runs IT support \u2014 diagnostics, remediation, technician booking \u2014 over a live simulated D365 tenant plus a ServiceNow-shaped ITSM desk; offline-safe."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/it_helpdesk", "rar_sha256": "284e3ddc0ff20be638380775607d58b29b8e3e08b358992aa18292ad550e5a17", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.2.0", "author": "AIBAST", "tags": ["it", "helpdesk", "troubleshooting", "itsm", "support"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/it_helpdesk`. The original RAPP
agent is preserved byte-for-byte in `it_helpdesk_agent.py` and in the RCI capsule.

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

IT Helpdesk Agent — a template you are meant to mutate.

AI-powered IT support with automated diagnostics, remote remediation,
knowledge base search, escalation routing, and ticket management.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     sibling systems (synthetic data, no credentials, works anywhere):
       CRM — the Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       (its field-service bookable resources are reinterpreted as the
       IT technician bench, e.g. technician "Riley Chen")
       ITSM — the Static ITSM desk (real ServiceNow Table-API shape,
       30 INC records):
         https://kody-w.github.io/static-itsm/api/now/table/
     Try: perform(operation="session_summary", user_name="Michael Chen")
     — the summary now closes with the live desk queue: real INC
     numbers with state/priority, and repeat-CI clusters joined to CRM
     cases (INC0010001 + INC0010027 both hit "Lakeview University
     Benefits Portal" and join to CAS-260137).
  2. No network? Everything falls back to the embedded demo layer below
     (_USERS / _TECHNICIANS / _KB_ARTICLES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set IT_HELPDESK_DATA_URL
     to any OData-shaped endpoint and IT_HELPDESK_ITSM_URL to any
     ServiceNow Table-API-shaped endpoint (your real instance), or
     replace the fetchers with your ITSM client. Fields the rest of the
     file needs are listed in _normalize_live_technician() — specialty
     renders as "n/a — enrichment seam" until you wire your skills matrix.
     Device telemetry stays simulated until you wire Intune/RMM.

OPERATIONS
  device_diagnostics | quick_remediation | process_analysis
  | schedule_technician | knowledge_search | session_summary
  kwargs: operation (required), user_name

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The support action to perform",
      "enum": [
        "device_diagnostics",
        "quick_remediation",
        "process_analysis",
        "schedule_technician",
        "knowledge_search",
        "session_summary"
      ],
      "type": "string"
    },
    "user_name": {
      "description": "User reporting the issue (e.g. 'Michael Chen')",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `it_helpdesk_agent.py` and embedded as the fenced Python below (sha256 284e3ddc0ff20be6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `it_helpdesk_agent.py` first:

```bash
python3 it_helpdesk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 it_helpdesk_agent.py   # or on stdin
python3 it_helpdesk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
IT Helpdesk Agent — a template you are meant to mutate.

AI-powered IT support with automated diagnostics, remote remediation,
knowledge base search, escalation routing, and ticket management.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     sibling systems (synthetic data, no credentials, works anywhere):
       CRM — the Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       (its field-service bookable resources are reinterpreted as the
       IT technician bench, e.g. technician "Riley Chen")
       ITSM — the Static ITSM desk (real ServiceNow Table-API shape,
       30 INC records):
         https://kody-w.github.io/static-itsm/api/now/table/
     Try: perform(operation="session_summary", user_name="Michael Chen")
     — the summary now closes with the live desk queue: real INC
     numbers with state/priority, and repeat-CI clusters joined to CRM
     cases (INC0010001 + INC0010027 both hit "Lakeview University
     Benefits Portal" and join to CAS-260137).
  2. No network? Everything falls back to the embedded demo layer below
     (_USERS / _TECHNICIANS / _KB_ARTICLES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set IT_HELPDESK_DATA_URL
     to any OData-shaped endpoint and IT_HELPDESK_ITSM_URL to any
     ServiceNow Table-API-shaped endpoint (your real instance), or
     replace the fetchers with your ITSM client. Fields the rest of the
     file needs are listed in _normalize_live_technician() — specialty
     renders as "n/a — enrichment seam" until you wire your skills matrix.
     Device telemetry stays simulated until you wire Intune/RMM.

OPERATIONS
  device_diagnostics | quick_remediation | process_analysis
  | schedule_technician | knowledge_search | session_summary
  kwargs: operation (required), user_name
"""

import sys, os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
from datetime import datetime, timedelta

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/it_helpdesk",
    "version": "1.2.0",
    "display_name": "IT Helpdesk",
    "description": "Runs IT support \u2014 diagnostics, remediation, technician booking \u2014 over a live simulated D365 tenant plus a ServiceNow-shaped ITSM desk; offline-safe.",
    "author": "AIBAST",
    "tags": ["it", "helpdesk", "troubleshooting", "itsm", "support"],
    "category": "it_management",
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
#   export IT_HELPDESK_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your ITSM client. Downstream
# code only needs the fields from _normalize_live_technician().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "IT_HELPDESK_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
# Sibling system: the Static ITSM desk — real ServiceNow Table API
# shape ({"result": [...]}, INC numbers, coded state/priority). Point
# at your own instance:
#   export IT_HELPDESK_ITSM_URL=https://your-instance/api/now/table
ITSM_SOURCE_URL = os.environ.get(
    "IT_HELPDESK_ITSM_URL",
    "https://kody-w.github.io/static-itsm/api/now/table",
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


def _fetch_itsm_table(table, timeout=6):
    """Sibling fetcher for the ServiceNow-shaped ITSM desk. Same rules
    as _fetch_collection — lazy, one bounded GET, [] on ANY failure —
    but parses the Table API envelope {"result": [...]} and caches in
    _LIVE_CACHE keyed by full URL."""
    url = f"{ITSM_SOURCE_URL}/{table}.json"
    if url in _LIVE_CACHE:
        return _LIVE_CACHE[url]
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "rapp-agent-template/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            rows = json.loads(resp.read().decode("utf-8")).get("result", [])
    except Exception:
        rows = []
    _LIVE_CACHE[url] = rows
    return rows


# ServiceNow incident coded values -> labels (Table API returns codes).
_SN_STATE = {"1": "New", "2": "In Progress", "3": "On Hold",
             "6": "Resolved", "7": "Closed", "8": "Canceled"}
_SN_PRIORITY = {"1": "P1-Critical", "2": "P2-High",
                "3": "P3-Medium", "4": "P4-Low"}


def _sn_display(ref):
    """ServiceNow reference fields arrive as {display_value, link, value}
    dicts (or "" when empty) — extract the display value."""
    return ref.get("display_value", "") if isinstance(ref, dict) else ""


def _itsm_desk_section(limit=8):
    """Markdown section for the live ITSM desk: active incidents with
    real INC numbers/state/priority, plus repeat-CI clusters joined to
    the CRM case queue by company. One line when the desk is offline."""
    rows = _fetch_itsm_table("incident")
    if not rows:
        return ("**Helpdesk Desk Queue:** ITSM desk unreachable — live "
                "ServiceNow-shaped section skipped\n")
    active = [r for r in rows if r.get("active") == "true"]
    active.sort(key=lambda r: (str(r.get("priority", "9")), str(r.get("number", ""))))
    inc_rows = ""
    for r in active[:limit]:
        inc_rows += (
            f"| {r.get('number', '')} "
            f"| {_SN_PRIORITY.get(str(r.get('priority', '')), r.get('priority', ''))} "
            f"| {_SN_STATE.get(str(r.get('state', '')), r.get('state', ''))} "
            f"| {r.get('company', '')} "
            f"| {str(r.get('short_description', ''))[:40]} |\n"
        )
    more = f"(showing {min(limit, len(active))} of {len(active)} active)\n" if len(active) > limit else ""
    by_ci = {}
    for r in active:
        ci = _sn_display(r.get("cmdb_ci"))
        if ci:
            by_ci.setdefault(ci, []).append(r)
    crm_cases = _fetch_collection("incidents")
    cluster_lines = ""
    for ci, hits in sorted(by_ci.items(), key=lambda kv: -len(kv[1])):
        if len(hits) < 2:
            continue
        nums = ", ".join(sorted(h.get("number", "") for h in hits))
        company = hits[0].get("company", "")
        related = [c for c in crm_cases if c.get("customeridname") == company]
        if related:
            c = related[0]
            join = (f" <-> CRM {c.get('ticketnumber', '')} "
                    f"\"{str(c.get('title', ''))[:45]}\"")
        else:
            join = " <-> CRM case: none found for this company"
        cluster_lines += f"- {ci} ({company}): {nums}{join}\n"
    if not cluster_lines:
        cluster_lines = "- No repeat-CI clusters among active incidents\n"
    return (
        f"**Helpdesk Desk Queue (LIVE ServiceNow-shaped incident table — "
        f"{len(active)} active of {len(rows)}):**\n\n"
        f"| Number | Priority | State | Company | Short Description |\n"
        f"|---|---|---|---|---|\n"
        f"{inc_rows}{more}\n"
        f"**Repeat-CI Clusters (joined to the CRM case queue by company):**\n"
        f"{cluster_lines}"
    )


def _normalize_live_technician(row, bookings):
    """Project a Dynamics bookable resource onto the technician shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not knowable from the
    scheduling record alone' and the renderer labels it as an enrichment
    seam (wire your skills matrix / ITSM assignment groups)."""
    name = row.get("name", "Unknown")
    scheduled = sorted(
        (b for b in bookings
         if b.get("resourcename") == name
         and b.get("bookingstatusname") in ("Scheduled", "In Progress")),
        key=lambda b: str(b.get("starttime", "")),
    )
    next_slot = str(scheduled[0].get("starttime", ""))[:16].replace("T", " ") if scheduled else None
    return {
        "name": name,
        "specialty": None,   # enrichment seam — wire your skills matrix
        "available": not any(
            b.get("bookingstatusname") == "In Progress" for b in scheduled
        ),
        "next_slot": next_slot,
        "_live": True,
    }


def _live_technicians():
    """Tenant bookable resources reinterpreted as the IT technician bench;
    [] when offline."""
    rows = _fetch_collection("bookableresources")
    bookings = _fetch_collection("bookableresourcebookings") if rows else []
    return [_normalize_live_technician(r, bookings) for r in rows]


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_USERS = {
    "michael": {
        "id": "usr-4201", "name": "Michael Chen", "title": "Marketing Manager",
        "department": "Marketing", "location": "Building A, Floor 3",
        "email": "michael.chen@company.com",
        "device": {
            "type": "Dell Latitude 5520", "os": "Windows 11 Pro",
            "age_years": 2.5, "last_restart_days": 8,
            "disk_free_pct": 12, "memory_used_pct": 94,
            "running_processes": 127, "pending_updates": 3,
        },
        "ticket_history": [
            {"id": "INC-2024-44100", "issue": "VPN connection drops", "resolved_days_ago": 45},
            {"id": "INC-2024-43800", "issue": "Outlook search not working", "resolved_days_ago": 90},
        ],
    },
    "lisa": {
        "id": "usr-4202", "name": "Lisa Torres", "title": "Sales Director",
        "department": "Sales", "location": "Building B, Floor 2",
        "email": "lisa.torres@company.com",
        "device": {
            "type": "MacBook Pro 14-inch", "os": "macOS Sonoma 14.3",
            "age_years": 1.0, "last_restart_days": 2,
            "disk_free_pct": 45, "memory_used_pct": 62,
            "running_processes": 78, "pending_updates": 1,
        },
        "ticket_history": [
            {"id": "INC-2024-44050", "issue": "Teams audio echo", "resolved_days_ago": 30},
        ],
    },
    "james": {
        "id": "usr-4203", "name": "James Park", "title": "Financial Analyst",
        "department": "Finance", "location": "Building A, Floor 5",
        "email": "james.park@company.com",
        "device": {
            "type": "HP EliteBook 840 G9", "os": "Windows 11 Pro",
            "age_years": 0.8, "last_restart_days": 1,
            "disk_free_pct": 68, "memory_used_pct": 45,
            "running_processes": 54, "pending_updates": 0,
        },
        "ticket_history": [],
    },
}

_PROCESSES = {
    "michael": [
        {"name": "Chrome (14 tabs)", "cpu_pct": 18, "memory_mb": 2400, "status": "High usage"},
        {"name": "Teams", "cpu_pct": 12, "memory_mb": 1100, "status": "Normal"},
        {"name": "Outlook", "cpu_pct": 8, "memory_mb": 680, "status": "Normal"},
        {"name": "OneDrive sync", "cpu_pct": 15, "memory_mb": 420, "status": "Syncing"},
    ],
    "lisa": [
        {"name": "Safari (6 tabs)", "cpu_pct": 8, "memory_mb": 900, "status": "Normal"},
        {"name": "Teams", "cpu_pct": 10, "memory_mb": 800, "status": "Normal"},
        {"name": "Excel", "cpu_pct": 5, "memory_mb": 400, "status": "Normal"},
    ],
    "james": [
        {"name": "Excel (3 workbooks)", "cpu_pct": 12, "memory_mb": 600, "status": "Normal"},
        {"name": "Outlook", "cpu_pct": 4, "memory_mb": 350, "status": "Normal"},
    ],
}

_TECHNICIANS = [
    {"name": "Sarah Martinez", "specialty": "Hardware", "available": True, "next_slot": "Today, 3:00 PM"},
    {"name": "Kevin Park", "specialty": "Network", "available": True, "next_slot": "Today, 4:30 PM"},
    {"name": "Amy Chen", "specialty": "Software", "available": False, "next_slot": "Tomorrow, 9:00 AM"},
]

_KB_ARTICLES = {
    "slow_laptop": {"id": "KB-IT-2341", "title": "Slow laptop troubleshooting", "steps": [
        "Clear temp files and browser cache",
        "End unnecessary background processes",
        "Check disk space (keep >20% free)",
        "Restart device if uptime >3 days",
        "Run Windows Update",
    ]},
    "vpn_issues": {"id": "KB-IT-1890", "title": "VPN connection troubleshooting", "steps": [
        "Verify network connectivity",
        "Restart VPN client",
        "Clear DNS cache",
        "Check VPN certificate expiration",
    ]},
    "email_sync": {"id": "KB-IT-2100", "title": "Email sync issues", "steps": [
        "Check Outlook connection status",
        "Repair Outlook profile",
        "Clear Outlook cache",
        "Verify Exchange connectivity",
    ]},
}

_TICKET_COUNTER = 45892


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_user(query):
    if not query:
        return "michael"
    q = query.lower().strip()
    for key in _USERS:
        if key in q or q in _USERS[key]["name"].lower():
            return key
    return "michael"


def _diagnose_device(user_key):
    dev = _USERS[user_key]["device"]
    issues = []
    if dev["disk_free_pct"] < 20:
        issues.append({"check": "Disk space", "status": "Critical", "finding": f"Only {dev['disk_free_pct']}% free"})
    if dev["memory_used_pct"] > 85:
        issues.append({"check": "Memory usage", "status": "Warning", "finding": f"{dev['memory_used_pct']}% utilized"})
    if dev["running_processes"] > 100:
        issues.append({"check": "Running processes", "status": "Warning", "finding": f"{dev['running_processes']} active"})
    if dev["last_restart_days"] > 3:
        issues.append({"check": "Last restart", "status": "Warning", "finding": f"{dev['last_restart_days']} days ago"})
    if dev["pending_updates"] > 0:
        issues.append({"check": "Updates pending", "status": "Info", "finding": f"{dev['pending_updates']} updates ready"})
    if not issues:
        issues.append({"check": "All systems", "status": "OK", "finding": "No issues detected"})
    return issues


def _remediation_results(user_key):
    dev = _USERS[user_key]["device"]
    actions = []
    freed_disk = 0
    freed_mem = 0
    if dev["disk_free_pct"] < 30:
        actions.append({"action": "Clear temp files", "result": "4.2 GB freed"})
        actions.append({"action": "Clear browser cache", "result": "1.8 GB freed"})
        freed_disk = 12
    if dev["memory_used_pct"] > 80:
        actions.append({"action": "End background processes", "result": "12 processes closed"})
        freed_mem = 22
    if dev["running_processes"] > 100:
        actions.append({"action": "Pause OneDrive sync", "result": "15% CPU freed"})
    new_disk = min(100, dev["disk_free_pct"] + freed_disk)
    new_mem = max(0, dev["memory_used_pct"] - freed_mem)
    return actions, new_disk, new_mem


def _find_technician(specialty=None):
    for tech in _TECHNICIANS:
        if tech["available"]:
            if specialty is None or tech["specialty"].lower() == specialty.lower():
                return tech
    return _TECHNICIANS[0]


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class ITHelpdeskAgent(BasicAgent):
    """
    AI-powered IT helpdesk with diagnostics and remediation.

    Operations:
        device_diagnostics    - scan device for performance issues
        quick_remediation     - apply automated fixes
        process_analysis      - analyze running processes
        schedule_technician   - book in-person support
        knowledge_search      - search IT knowledge base
        session_summary       - generate support session summary
    """

    def __init__(self):
        self.name = "ITHelpdeskAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "device_diagnostics", "quick_remediation",
                            "process_analysis", "schedule_technician",
                            "knowledge_search", "session_summary",
                        ],
                        "description": "The support action to perform",
                    },
                    "user_name": {
                        "type": "string",
                        "description": "User reporting the issue (e.g. 'Michael Chen')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "device_diagnostics")
        key = _resolve_user(kwargs.get("user_name", ""))
        dispatch = {
            "device_diagnostics": self._device_diagnostics,
            "quick_remediation": self._quick_remediation,
            "process_analysis": self._process_analysis,
            "schedule_technician": self._schedule_technician,
            "knowledge_search": self._knowledge_search,
            "session_summary": self._session_summary,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(key)

    # ── device_diagnostics ────────────────────────────────────
    def _device_diagnostics(self, key):
        user = _USERS[key]
        dev = user["device"]
        issues = _diagnose_device(key)

        diag_table = "| Check | Status | Finding |\n|---|---|---|\n"
        for i in issues:
            diag_table += f"| {i['check']} | {i['status']} | {i['finding']} |\n"

        causes = []
        if dev["disk_free_pct"] < 20:
            causes.append(f"**Low disk space** ({dev['disk_free_pct']}% free)")
        if dev["memory_used_pct"] > 85:
            causes.append(f"**High memory usage** ({dev['memory_used_pct']}%)")
        if dev["last_restart_days"] > 3:
            causes.append(f"**Needs restart** ({dev['last_restart_days']} days uptime)")
        if dev["running_processes"] > 100:
            causes.append(f"**Too many processes** ({dev['running_processes']} running)")

        cause_lines = "\n".join(f"{i}. {c}" for i, c in enumerate(causes, 1)) if causes else "No significant issues detected."

        return (
            f"**Device Diagnostics: {user['name']}**\n\n"
            f"| Detail | Value |\n|---|---|\n"
            f"| Device | {dev['type']} |\n"
            f"| OS | {dev['os']} |\n"
            f"| Age | {dev['age_years']} years |\n"
            f"| Last restart | {dev['last_restart_days']} days ago |\n"
            f"| Disk space | {dev['disk_free_pct']}% free |\n\n"
            f"**Diagnostics:**\n\n{diag_table}\n"
            f"**Likely Causes (Ranked):**\n{cause_lines}\n\n"
            f"Source: [Asset Management + Remote Diagnostics]\nAgents: ITHelpdeskAgent"
        )

    # ── quick_remediation ─────────────────────────────────────
    def _quick_remediation(self, key):
        user = _USERS[key]
        dev = user["device"]
        actions, new_disk, new_mem = _remediation_results(key)

        if not actions:
            return f"**Quick Remediation: {user['name']}**\n\nNo remediation needed - device is healthy.\n\nSource: [Remote Management]\nAgents: ITHelpdeskAgent"

        action_table = "| Action | Result |\n|---|---|\n"
        for a in actions:
            action_table += f"| {a['action']} | {a['result']} |\n"

        return (
            f"**Quick Remediation: {user['name']}**\n\n"
            f"**Actions Completed:**\n\n{action_table}\n"
            f"**Performance Improvement:**\n\n"
            f"| Metric | Before | After |\n|---|---|---|\n"
            f"| Disk space | {dev['disk_free_pct']}% free | {new_disk}% free |\n"
            f"| Memory usage | {dev['memory_used_pct']}% | {new_mem}% |\n\n"
            f"**Recommended:** Restart after current work for full optimization.\n\n"
            f"Source: [Remote Management + Automation Scripts]\nAgents: ITHelpdeskAgent"
        )

    # ── process_analysis ──────────────────────────────────────
    def _process_analysis(self, key):
        user = _USERS[key]
        procs = _PROCESSES.get(key, [])

        if not procs:
            return f"**Process Analysis: {user['name']}**\n\nNo process data available.\n\nSource: [Remote Diagnostics]\nAgents: ITHelpdeskAgent"

        proc_table = "| Process | CPU | Memory | Status |\n|---|---|---|---|\n"
        for p in procs:
            proc_table += f"| {p['name']} | {p['cpu_pct']}% | {p['memory_mb']} MB | {p['status']} |\n"

        total_cpu = sum(p["cpu_pct"] for p in procs)
        total_mem = sum(p["memory_mb"] for p in procs)
        high_usage = [p for p in procs if p["status"] == "High usage"]

        recs = []
        for p in high_usage:
            recs.append(f"- **{p['name']}**: Using {p['memory_mb']} MB - consider closing unused tabs/windows")
        if not recs:
            recs.append("- All processes within normal ranges")

        return (
            f"**Process Analysis: {user['name']}**\n\n"
            f"{proc_table}\n"
            f"**Totals:** {total_cpu}% CPU, {total_mem} MB memory\n\n"
            f"**Recommendations:**\n" + "\n".join(recs) + "\n\n"
            f"Source: [Remote Diagnostics + KB Article #IT-2341]\nAgents: ITHelpdeskAgent"
        )

    # ── schedule_technician ───────────────────────────────────
    def _schedule_technician(self, key):
        user = _USERS[key]
        ticket_id = f"INC-2024-{_TICKET_COUNTER}"
        seam = "n/a — enrichment seam"

        # Prefer the live tenant technician bench; fall back to embedded.
        live = _live_technicians()
        available = [t for t in live if t["available"]] or live
        if available:
            tech = available[0]
            source = "Live Static Dynamics 365 tenant — bookableresources + bookings"
            specialty = tech["specialty"] or seam
            slot = tech["next_slot"] or f"{seam} (no scheduled booking on the tenant calendar)"
        else:
            tech = _find_technician("Hardware")
            source = "ITSM + Technician Scheduling (embedded demo fallback)"
            specialty = tech["specialty"]
            slot = tech["next_slot"]

        return (
            f"**Technician Visit Scheduled: {user['name']}**\n\n"
            f"| Detail | Value |\n|---|---|\n"
            f"| Technician | {tech['name']} |\n"
            f"| Specialty | {specialty} |\n"
            f"| Time | {slot} |\n"
            f"| Location | {user['location']} |\n"
            f"| Ticket # | {ticket_id} (simulated — no ITSM write) |\n\n"
            f"**Technician Will Check:**\n"
            f"- Hardware diagnostics\n"
            f"- Full system optimization\n"
            f"- Pending updates installation\n"
            f"- Upgrade assessment if needed\n\n"
            f"Source: [{source}]\nAgents: ITHelpdeskAgent"
        )

    # ── knowledge_search ──────────────────────────────────────
    def _knowledge_search(self, key):
        user = _USERS[key]
        dev = user["device"]
        # Auto-detect relevant KB article from device issues
        if dev["disk_free_pct"] < 20 or dev["memory_used_pct"] > 80:
            article = _KB_ARTICLES["slow_laptop"]
        else:
            article = _KB_ARTICLES["vpn_issues"]

        steps = "\n".join(f"{i}. {s}" for i, s in enumerate(article["steps"], 1))

        return (
            f"**Knowledge Base: {article['title']}**\n"
            f"Article: {article['id']}\n\n"
            f"**Recommended Steps:**\n{steps}\n\n"
            f"**Self-Service Tips:**\n"
            f"- Restart weekly (prevents performance buildup)\n"
            f"- Keep 20%+ disk space free\n"
            f"- Close unused apps and tabs\n"
            f"- Check for updates regularly\n\n"
            f"Source: [IT Knowledge Base + Vendor Documentation]\nAgents: ITHelpdeskAgent"
        )

    # ── session_summary ───────────────────────────────────────
    def _session_summary(self, key):
        user = _USERS[key]
        dev = user["device"]
        actions, new_disk, new_mem = _remediation_results(key)
        issues = _diagnose_device(key)
        tech = _find_technician("Hardware")
        ticket_id = f"INC-2024-{_TICKET_COUNTER}"

        action_table = "| Fix | Result |\n|---|---|\n"
        for a in actions:
            action_table += f"| {a['action']} | {a['result']} |\n"

        issue_count = len([i for i in issues if i["status"] in ("Critical", "Warning")])

        return (
            f"**Support Session Summary: {user['name']}**\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Issues found | {issue_count} |\n"
            f"| Fixes applied | {len(actions)} |\n"
            f"| Resolution | Remote fix + scheduled service |\n\n"
            f"**Actions Taken:**\n\n{action_table}\n"
            f"**Performance Improvement:**\n\n"
            f"| Metric | Before | After |\n|---|---|---|\n"
            f"| Disk space | {dev['disk_free_pct']}% | {new_disk}% |\n"
            f"| Memory | {dev['memory_used_pct']}% | {new_mem}% |\n\n"
            f"**Follow-Up:** {tech['name']} scheduled for {tech['next_slot']}\n"
            f"**Ticket:** {ticket_id}\n\n"
            f"{_itsm_desk_section()}\n"
            f"Source: [All IT Systems + ITSM Desk (ServiceNow-shaped)]\nAgents: ITHelpdeskAgent"
        )


if __name__ == "__main__":
    agent = ITHelpdeskAgent()
    print("=" * 60)
    print("EMBEDDED DEMO DIAGNOSTICS (works offline)")
    print(agent.perform(operation="device_diagnostics", user_name="Michael Chen"))
    print()
    print("=" * 60)
    print("LIVE TENANT TECHNICIAN BOOKING (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="schedule_technician", user_name="Michael Chen"))
    print()
    for op in ["quick_remediation", "process_analysis", "knowledge_search"]:
        print("=" * 60)
        print(agent.perform(operation=op, user_name="Michael Chen"))
        print()
    print("=" * 60)
    print("LIVE ITSM DESK QUEUE (session summary closes with real INC")
    print("numbers/state/priority from the ServiceNow-shaped desk and")
    print("joins repeat-CI clusters — e.g. the Lakeview Benefits Portal")
    print("pair INC0010001 + INC0010027 — to CRM cases; falls back offline)")
    print(agent.perform(operation="session_summary", user_name="Michael Chen"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/62759LjVtImeCuMmh8tDVQiQBBOE9/uwhLeEYbkaqIa3hDeEKan730O3ypJ1ZJiNzZi3yhDACfz5EnzPJlV4L8+BfOUt8OnXz7REkNfnU8/fYqTMRqKbiraBty252Y8SM5hnLuuHabDr/MJRs6HuAiyph2nIhp/OgxJnYAbb4mfDlMS5U0RFUFzCNv2WTTZbzLtKxkOwaEqXslhLOq5CqYkPnAojgGhJmimQ1fNI1hxTYZXESV6u3we86ADiyTnqh2AYc//cWjTtCqa5PMYpMnPwNxkDequSsZPv/zf//OnTwX4/OmXf32KqmAEtz5JjphU3VuSzpJmAuuroMnAg24D527AdZcMaTvU4FacpIdvVz+MSZX+dPjv//25BEM2/nj4/H8cxmn45dfm8O2n7Q7/dfj69OcsmX749VMLZD988Ounnw6/Am3vM3z5zlG/fvrxD/lnsgEFX4ZkbKtX8mUek+GH/1D3vvOlCerkqzog/J10XIxdMEU5UPGvP+6+f/5+418O7wP9/OWvz376s3g/F9Hzy3ch/UP6L4/+ItwNbZSM45egCaptLL7b+c9P/iI6RnkSz1Xy5Y8E+kP6bx7+RcGzaZcqibPky5gEQ5T/If3nJ3/dG1gGjvNlnOs6GLbv9v3PB98J/vuPj3nQxBVI7f/6PSwfIWy77wJWpIemnX5b+st/GjAk0zw0h/TXT27ztrU5/J5Lvxz+1Xb/BuFv/rT4m6YfQB79+OnfIPEbkJ9z9JZ55/1/+28HrYiGdmzT6XCN2nk6DHMzFSCdml8bJy/GA/g15QnQB8pyLMIq+bYORKpMPhSBWjv88/8KijAYp8/Bu37Gz1URDsATx2L6kn+rrH/+fHCAonYosgJE92DTpvlr87H+vUkHchwUNKjicJuSz6C8Pr8/HIrm8M/vtHz5EPi52/55AEd7P31bZ7PSIQq6EcT+57flfp403+yMAMIkaxLNQFfVRmDjtAA48Iajj5oC8mD38VlUFQjMAI7UDtuHbuCJX97K/vnPf4Kj5b82X8EAPXwFvvEIFvxuzuHzZ3ACgDlZPv3agPRrD//417//cfhfh/8nqQ/l7z1MgEPf/AwslK+GfgBFPtdvZx7eQUuC+MPP//r3Nz8CNQ3IJhCVIi2Sr8IA8Z5J/JtTryL9+YThhzABzgSOrN/I/AbaYvr5IKWH3+0Fm74fvTE1B+UOELRLmjhpog1oDcBxfvfkOzlHkHFjuv10ANDzses/Qag/TKy/RGD5Pw8aax6mtq3AH28zPxYB4RZUZFD9HvKv99/49Y/xwPym4ueD/s60QxcMQZcPwbc90uBrXFpADd/EgfLg0CTLr80bzZO3qz5q4at7wCLgmehbSD+/Y36IWlCeTTz+tvfHmg92cVqQu8nwazN+S+lgeIcienPRdsjmIg6aKPkf31JqzNu5ij/8Byx9a/oWhfhbVD5yELDhb6Ry+GCV3wguADwGLAYbH7Z2/tiqTt68Bk5Uz+AQX3OYlj537ZIMH7z2O7EuxZQfABu39YfhfybYdkoO/4m8v6PaIXw78xu0HQB7B9XHmsMAzgTS4qePpAeansl0AH4Cfn779MMW0fAPjihdDw6vmSrt8AffsJXrG26Qnw8G8AnIzbcjwnYF6XXo5qoav1L424sD8PkHrX9kt+g45iEd2vrg+MY3xHojyzs1x+2dBOPhh3FrgL7pHcFgCn4CsHiIgCuAQUVQgbMu7fAECdtsSw5c9OMfUMna2m+Ofht0fSdFdOA2wJHASYfv2ogf6HfMD2rQJAcjTQHjHa5ft//xe+TNp6kbfzken228fV5+zkAA5vDnoj2OH6o/x99Ufwaqj0FXHN8GH1/Uz6fj71p+KEB1gQSp4s/j167lo+sJ3nD6xqF5AKz3LelAZicDyK13eIOPuv5dDciD7/smUKHvSP6c/fz97V8/2SDZtwMLMPD7XuKjOfqrZ37vmQ4/fETnj67q4Lzt+0yb0uGjv/qD1lD4IOnsb6H9/+Qt4Ij6w0sgLY/Te4PfvOQM2y+/N1a/M9t//Q3tfkDP164HPAYElgdJ9afzfnfQb3IghZZDVLVA3dcq+oqYIEU/Tt/PyZz88jVDweG+qWnmOgS891XgfYTk2A0F4LBp+1ovADqTYPr85h/QlU7vtWULGs/4Xc0gF7/piYL3tj8AxTCMwOD3ATr8dnEiQDIA9TkonF8/qcETdF/JcnCb4oNyp+2bDgbAVfpOJBMAAQDSTx8GvHf72Iu+fj7hMIISP/78FjgBJG0BPk7vSvk/D/wbyQDVgRpLg3dxhkH0fMu9vZCAQ8bxG04AghyqYANlESZVu3zb+Ycv7pW3r4fj4YvDs6IusRKtf1wqzBfadiRW5a8/fu/zryDdfEB5BFA8T8Zvur415h82oj8fNHDcN2IAJASuC6YPaVXy+ANHO/ThytPaV1PevdYEsvWLyKsmx1+VL+8FX1xb/ab4zQfNdjA4UH6/DQSAxjrgn+nDU9/LvrP+LftN6puKv8v9v6j64W3q1zx5U9abGH78CRDTNx0gIaog+sZaCejyfk+fD7mPcouq4o2sB+GNCL/x/vgbiH5T9EFZTZLEX4GhKsY3IoBgf2lAhQRVsSdf3un7XbP7w+8xGLsE3Kh+z53hTehvB48gxZpj8Nu6pAEkmb9x/s0MNcipd/tXfRDTAqjzq9Ef3dEISGEaivXnbyq5jyEBIM+beydQX8AX2/jdyPYnTVIzzU1ytDXtg1IMk7dpRzL0Dxb568QBOqe/DBLvburPowMQ/l+Hv2n8wd0/N/TvhX/CEiD9dZz65Y9m+g2EYGvANj9+hzTvmRCYCDqET780gN5++vRx9+9mx3fvAlwC/P2eMYHFQPNUJB9Xv+/yvvjPGdr5wKqvNB98bUNAdv42eIIRFoARGF//ZnIDD//iq7cdf/IVuPU3jgJ3/+yo98L/dNQnMDRPW/c+LxggAIq8h4k/fPOXs7jjB9v/1nG+M7wYxzk5/PBBV//4HrT/8eOnvygH2n8LwvvIf3jtDzva8D1/vO1491Jfh/N/fQJ+D94E/M3z30YUsByMI5/Hd/t2RH6GwYbg+msbDp79vw8v3wQAFoCOGkicyHOCxnEEp+kJDhMcJVESJggMh4kYI8MTFZIJmsBkiGIkRZ2CACFP4K8Yw+AECxDi7eEP1v/ybkqLtxEwQp3xcxKgJwwF8lic4FR4DlKcogicSjEEQ5LTCTn9Ifosmvjbyb6e5O223+eotwe+HfBfn0L8DFaK51Giv/6wRwqmTqgU6oT6grLBndUHvxW24IZyGSERdoUreFC9WaFkOYzqsbd5ucg1/YEV2PXyaL0ZbhopokwiT8EEGS40s0uuixlx7cyXVW1oPijdMIUtetqoFidCE0XlWU9ExzSaNCqp+gjahBc2sHfnlCQ8qp24Va1zedVnS3udz4z+XItEJ4KT0aeIn3KStWMFzXrKY9CyUq/LCwzdn6TDCEKvn7QcIV4LaDiQ3LtoebPcab7BloTBicw7hvMr4ewzZBJlQcRX1ZBmnF/gWif9sk30K5+7/HU+YnHpNFBBX7Jkxfc+0Yh44S7lcrEpLDqOJkHAKzHEJPTay4FSX6+cfHVceJ7XlxUQzkXyS+FJZtaF3clNP1339SXlGJHphZbtrBtdWWYlWIaMSwK0iMp+N7KtGY4oLfMGY2I6hmscrmK5YMm+4gXGmTM0li8f+713+OOdNzK64EojxzRy5yViM+kYeIpOOve0SNqdTG8YbMer4oo2bdEyaqa1JU8nkxg8mNnFUxXhEX2WnGlPNWD0SUdZBRVgpnXvmHZunrcJjVHizl1f5h7OmbGD2Gt6XBjsjaHkTfTpl/HSUAHl4zTNw8BA+jPjolxe3LGYaNGBX5Yowrm7RHRIyG1Ph3GfZ4zhp3TMYxFlg9zeb4hULWzWKoOIavlqpmLYG/sJxxzydZsv873EkQGB9D0u9/xV3TzzNgrZRO/n8a4MbmxK4t02VQmSqvB1k09bYKhawp+Ykw9t8Hkqp0dotraopXAP0zYRlfaF7Hj42Kjpo5TSUpJXcJBCMEzRAnDjLlfqVPFb45QFGhQLs00VHdywtglfXBEZ1M46HnGxxLvsifrLYjNW45mYtGVKcVO4Oy/TzPK+oNDtNXUuFKboY3luVlQYOgbXHrtkS3mD8s2QQyk9W7x/jQtzCWZuGQU4a0mZpDXR3mC6ZsM9hOvjRXvV6WBB2d0Xe8a0uH7UoCQByUs+byhMh/ySNTyfs+ZM7pdtZ27SnOgPnSsM29Dh5HXzcShMjmXqMaX90uNcWMQlabedFKCRbcUnaV2fgbHl1EQSizi88iPXaOFuszdL7LNbY4hyeayaF9OuxeneHMc4oIhQTh/HhFih88s5U6bB3FAyutjo8Jqb9ZTGt9KvJl5XdiNq4ci0iuud5BuWJe2Sr1n9BC3IiRt0/gEOxCVlteoOSpgOoZavjuLmEYFOEbs5QSvLxZ1/EWmajnjvhNCJKenjq6QeT5rFNPrqJzd5Y5LYVzU+MaGAfsDFvWIfVfoM56VPlqf0uK5JJtiMTXvNzGFL5hyfiN2qVsazvsbslriufK0l3BZ1C0KjfN/nGK7gD4OyzsBaNyq8KLeXtWArixshvlZfsy0qBr4txF17GjJBaERi33x4OuUeAwE4Oj+MJmFdfmV40WV8/wVNFg/hosRe2hERVWc7+ZmmwptGk3PB33o+RNWXJF6ko3WMF2vhz2c8CO4Jzq13jC5qkyTpASYdZ9m0sqI7FI8gcUeh1xKVmll5aYLDO0S9eIbQWFma6ot7YhLLGOju/fmsP0eO51DbCe4Xn0zmKGdvSMbHDFw1ZUUkchtowuuu1tvds00LSgmbTaBCf04IG7TohSk1e/IsqRr92rCmGO59wVj0QWSf5ut8Z0ICN60ntRPIJNH5fSmQ9vTIMDKwmEETuVlX+XSW5K2OhdQuMOmOX9PmMUvH9TH6COi055kuML89XarjNr4kVemRAJ60dsq6+JSrga3dG4MvyRzjeZSGWwZpRBW5NadZS9fjqqL3U9zhS0pQ5vFIQUdYhQQKHXrsjhEgXA8ojjfMQFGPOMZHargsoclOKMev1QnaLNXNaNV3yN43kNp28REBhjZAnrrAOX06PZVmITwyFqisFLJTYQxMyxrbEQcMb5v9vc+iRzVyotPMetXe4ajQs1mtJ4kZ5iBu+ZtmWk3kbxB6K2w8PELXqtPTyGAbrMEbpm6Y2xJPdL05xJNxBlasX1VUK+dHqS2jzrDBaas6xEAB9Sj7ZJUPcgnZuloKNmYKMz85LYm/QgwXywnlnY0a4+WOuSeH9XAGXV6+JLc8HfZHiC4pIV067NTqsmzlktjeMu54XcvgFLeEp3Fk1aqvcrZPRCPTd2bSu/OoOYhL9y1Z1sfMLDS4kE1X14mMitUXRyqoSg89z/NSUyE5xTSN6Tf4HrQ7YDCoYOt14x15ynirG193JpHRfZQFIpJbHccWHz3rR+10tbKNaIwNhkqWZjd4NhpWMvJ4I0ii3UIyTBPMuglKxuXGHkMNtW0KUji93mVHi7FY4yxs46Us94usL8pRFBdWHAIQOpPUlkqr/WnvubUhBNJchmlkaDHOdgYx6n0zjDU/ixVZcNJFHXkFhTTelaoC1Gph0uuloV3I5aezaFxJ1kj4XcvwBjfXGUpQNZAR4qiW1O1yu2kyN+nPLK3Pd0iCCbFKeEa+TyWmBsOZZGhX8q56qeZqOJFPWmMCHhZqM+tpyTo/H75/p6+FS19dHoYvLcqMz0deW2saDE7UIgtNYyueJ+fJEoViD3ZlQVC5I3tzfykd3t11PAxaMtWkIWFe1zkvJP7JT9WlOmlJfD7Gsa4AOH3G5I2VFqhKc2nx5NTMA3tQM74i8Iv8bMxcXebTOZWAZ2aKEfEQJD/nm8+V0c4jTD+kCVFfGGNpAYC/W3aZ9eCa6d59i24vezhHiGI/1bPDP552obmWfG7IK61T7tmpyhFlNKe0YMphYjg/1wY1xwrJ6JZ+Q+v9yFN0i1PZaRhvZpERXXQlfKmIiI06CfmAjK0Sj4gjU/K0M4lhL/cbzD+8tnnst2Gnrt4Akmb3ZNShNM/qm0qTruZZNwlcQ4fuoR17vFita14T1jLfU/q+eJa9ne83QzHarIbpttTY1QkLhc085dyIlJNmcW6IfgYZ1cIAmgYWmGUjPY7CwI/Huy5dROsGX2CxEJKryEz5vCFZC3V77pzsvgb9sfWCbmMfXiVO7UF2yH59RQrKzsyUm326sCuNpnvBslhfFvdjhXG9oFWvaagHT58K4O2lOQc8LtUWxkuTd+XFEYqEpfUm5ioomim6NERXhMGf0Zjcn1qyT82ZdPaLyQRKFizkk7nctSBKM6GWRVk2K6vIyFMqXV/WkYlkNrx25uMI+k5yfXlbdyND5KqVHmESrH5pZ4Bh9/Xh10VtzfeX98osCoBpshZz0LiX7hHSDYR0YTwTDJG6C5VhOEp1nCQcFztNXT93eAjQMGdguZVrxxMZ19VOnUW0KJpeLpG6lwIxcxPAZXcon8hIWmXrOJzzEi+a1MyWh3J5DS30CheISCmuRHHE28kLC42GeD0K577zUuiYOKlUnnuWh2MPOtp70Ul2UdI6HlX0kV3xCREZ4VXApS4U0Bjwgs6IuWGR+Z3PKeMaaVpAs0NVtLh0bv2zTm8E9GIdSd3zGVvWUuJYEPGpLHNz1GbGIBmZh6B8E/eKfuKFlcFO4l1VH07Z/SzvWrSPdd8WV/x5k9yIkZDLcFPuEo8t0KbW7LMzKduPC3uajNhA03IpHwQ822ZSUkz8vCJXFEg9lGE+ZRvoOxLl5dq1U0ujNqDKlRp0DI06gHg30HLjdBYKu3XTyHv71Op2ZE25LkvqpYlWChuS+sxajkPPsc25vYx1V1fKbdhi7mxTP070fYOegkZYUz9c1IlQbOJapGeUIruBOO33vfAKi9pFGJNavvSksz9KteYT96KIG+e1z9wuY95QIdZFvrKjK5V9BTq2TQpYCbbCu2Ry1rIt2XW82BN1YUSsZhwHapNYC2HAf9QIWMHL7fThb2dlpPSQfcjN6vZbdubUs4SXT+6EyO6zyQRA1ufnKZwvfRY88lNyaySyJkyBuFvZ6aQu4WMIxZmYx80u4/5xbS94wG8o4th8DAYpKDW8iG9M7M5fz9A9rzNKXaLq9KzMGwhZFFjK8GCmh8Q1tJPOGZuE5Lal6dbVa2Azmza5Hm7OEjp2Bf7sGaaA+fy5jUwhPUq9YRNVcVnEFXotF9divMQZn3dyz4kyi5m3qwAGmQ0V+0fvCZfGaufLExOnhWP6ugWDHH6qd7/W+bY8vwRJZsjewhLtQZuj8YrFyuNgsX04/mknRDnkRaWSbEShO1FZ3av59Jkwd1BuYPCAtUZZFO4XroBrhe03MOPdUOBD34bV2KT2kQuGS96BxphX+nGAFq95+AvJmjeHkvX1YSu2lNQSXpvqPUoqxTU0ecvmzI54mNq8lmaqY6TTyXWflRW/LK0mixu9wptg6pdC7kF9XDcTo3ugwBK9S/3Mr0rOPZduG3OsCJRjm59pK69uk3C6PEvodJGPdBRxVdqxnPqc4oG4XUPcr3nSv7p7oB2Dc9XJtwxym4gKpRcEbypnGYYJnwJxWyTfhFfF76JNQ4I7mCjbKWmn0rtbxPysXH98XbZTfVdv+rta4yCd5ETLe4+TnBM7svTNPqEXfhpBv6JbmrPbVaS37e5W/cPvw6oQolYUZsTEi9ulTy8bd2GqU2F6Sl8++p2jmgdivvq6cbU4hrV+UyG6Y0tYe52kOR9N8042AklfERFXukmg/LN1yZIBSSA5nsaKuTyGikbCUntN6GN2sS7p19afeGKr55hzLsh+YR+xNysecqsePWKQlgDpDz8rCcdhfAIucY6uFcPpWz9g7pkhP7DLUFHP/sE0eeQ3XLDwndrmwTOOeEcp+EJC3e1BKJEnJ9i94EHjVGuKm1+a/CbctJaZH+HccoFLl/aQqUT7Cup7PkmoWYYFn1+3yphSvo/X0Nal5waWn2FRCCt1t5wCnbtFJjaB5ncJ5+RreOn6ll5luOvx/e7UPrFkwt6OBUWeqmt8ulg7y9Kudc4CMGKo7jMuqFavDFsUV+E2dGHA8p6u3LxtBi7wEcmY8AxDUrnDLKlIO1BnsK0ODtXRuz0VjnFzbPfOS/fnc0ZiitMJNqN4+L6tCx3Lkl37ePjQxW7k2SPHXhQdXDveNDjqmTfguxslqp7lsVs1jdBbqQGF1EQMlqttjnbrzyetpjNMVxvJe7Ke5oW25HpuGKQ555CMQlFhLtyCeYm0G5Qg8HmUPBanGMOCDBwBE/fzhAtP64Sf/FlyQJfMBjbl9A1PXY3qLEDX5xi5R2R+samdozFFaqlw3p1kZ58CydlXO6Zvpy2rGHeqVrerPLc7yhWN0ivvDxYkOColc4/aUBSPhf1tv/U9cmf4oAxzrivpZ0htI4yxl3RcL6akHVcRi6jj1oJO9mr6fIOmuhpPIWYfk8BLrM21n7aQC156JEMrVCAlRkCD0eJaB5rW3ThL5C7KgnA3TxlCISzWs+jm6M8Hkc/lBEevhqEje7A6jLBykellkdrvTAojldUwE/tkSUnJWzS8lat6u2wXyWlPFLnI2djADttBrDEKJ36OLgqtHodtWGkO2i0cDBqP2j/RRrovZcpDGEbQ26XsNPuBU8n06CXnzhH7dDeHkmL5uAmt4wmM3MxD4ypi72CrJu7BgNKGkzuhrxPPu7K3uynqNbK8WBWdiZsozQ4cSvnt5E/Muo18VU+v7CLtzzMRifMNy8+viearaQZVeoEEYrhAhbbYCXT176XSdd2IojFC5ddRsl7hWdv5dpog7KXx9IyhSnRbj54/op5l7uU9WCUEZXOlEMr0hpyyAVLVhwaI+xK4frZW546uQ2dCaceCEtUfTUs4HmHYONbuNSEKRr3MASw8MuVBPZ+hbKNloLu+Q2WAiRKfeA6G2FRjYz4o1qfumrWOxRKRx9VS6zST3JCeBJ/cFcQnG9E+96aPe2QpZad7PpAB1ZxR5plIiU87VJNYNkIS96Y+48/9ZWzrbaZFd0kT/RXexlROWqJmK28yR1NlekT20wkNMtk/Jp6pbLf5KBQReju52GAdDZYoti3K9AtToHfGOxLBMR9WiIlxCeHUx0ubynTkLgTd+bdzQKFqmbn4JVm5/EatwfRwOKdytpfq4Z5mTxlICY5Cjuod2l4+FW93Hjcowy82gsKgMsBGfcLHu8pS8lqO1GO6MpkBJdjA3PKTq1X57i6hEywU1DYIkt6aiEh9vLMergZpxS0lSta1E14nXqJP8yKg1EjTH2270Voodup9CCzbqFyxZG3xhYaZwkgUZ6PszSelOo1gJjQChkj2OhMgp6osw+3LTNXaY43vqUkb5c5TvVMkIaRJadeva8TLZw1lMNi6ahltQRs7gGmmRBpCsuaeWEAzEkOXGkqtR7RZZbyT+pmkV2xW0O6R0F4/0C66XeqyRnxu1FrI93QYXUatNhIPISDXs7CNNuPUdHhZYOcdMTFrH+0IpthHJoyPbDxKKR5cbTANTPGZOCelzboVU+d8Y9/KR6ZzPYMzW1BvR9Tfth41hNwmehrPWZO6+bXPz6sJCOy8brB+fom4uzdBZMSXQLuVrLHh4ba3QjY4meLKz6t3olYjh0HzKK0kfmVd7zYwd+iEkXtxl4LgVvUjB6cIjOLUdIOW6uhBLcc7pVfJgBJdEql9LFhLjrDIJjGK8YVJD8FaTM3ppet61ljEQMhoSxq6sdxXadm+Njg0xkgQQpRhQBOXC0VkJrsRBaeMtHJMop0q0CEJ0oveyz1APz/Pbv4NMxGb3kFjc4w7yF4cMZRLzBHmpbxYKRb3rHaMTG0iK6Kgu+cJfe1T98x9EtPRdt3Qo2mJ0dHDHz58PBtzRaJaMQYZPUZadi9JeaMhxmvVU8WjXC7B8SBAAvmKbiJ/kjgqj/J1dKe7YHbCajlDrg73ao3Oz9J7LAx0yV7ixtmC9HoYdwDwyxJarzEzV7e5jIrKUenVpazUNsUXpFcMg0jBct7IXgynM/kyEQKW4uXISMdij1++uClxFvkCb6TH40sDnq4dsWzx9CRW3fkqRlgdPLHxTCm5delY/PGy2ACr21tkchF+9YLCUCw09vsgJMpXTDpPz6lYUSZYU9F3KpdS2ZxHWDeZY8SqLuRemL1yM1bwi7N37x+NQpOWxkxtaPUxfxeNZ9WSjLOnF9miLOxSdThxNSSZjW3keqfRl3qUwXjBoXQ3XQajvNXtKz7xOkh2UMpy729TuWgI2xCCmpYuKbZGipHog36m0d5uZ9PLFNmHp36tSTIjAIaiKjrsAa3qO14U1DlbZ3MvcnX3wYg+0EoZJefHjQejMmGjTVR0PH/P0j5cTHh4eimMyVN50XPUODGnKVRbJNM6hhOOFmyZkpE45oNkalygbR49as/loWF5dYbOvBrrBZtokWY/j9uKd8fzWdGiSV/XQm6OQt+nNsrTJnV372mmw0Z3xtNOCNdoNH3XoQfEZQ1DWk/MS3cRtV7jefIUo8rP9ujenvf0cbOMky1yQSVe7dcDY9t47MOV1bNjGsqBnixhsdl5QCgSg8u0ZrzmzbkqiugjXN5O1HSyL0Js368GbdxBv6I2t0TQFG0301ccOpc6AO0NWD3j3qNjetxJi0505bBVlyF+7EK0ANXnqGa0wdbvl3t/hFYJf5l1KGOpLtrXYgS7jRb7DF/cte2HWUncLd7XmzfAZTp32J6/mup2aTuudAWth1kG4TcKe11nI7P07VJdBTpnVSvnTwtf2lVZWshcmkz3VG/SzPv93dAg0zg9rkSG2mXhXxonKp5LWiETdsfv0tptWHENffS42A0/rZx5Ow+6SdAAjiyCGRLl4XiJZ6G3Tmh21a9JDtbQ0SycjlXcdt1lMzn3OO9pT3TqS7Rzeju0i/RZmwWppEbbi2W/0f7FOya8dMHuF08TpLJobxJDV5ZoXG4gptcVopq2cqjTXlmvo7nsTddIhiN3O6HseJw5LrxkNerReqS2TrdESOTaUGQO0ZPD2KR4vB6UUAIkOI+YayMZmLRic4dMBcyvaW5Hg7zAPc40IRWj96kYbYoMLu//FMv7VRxvqgbsCp1bM7piY9wdLFdfGqEEK+mX015NGXkUN+f9jzDUY8Qki+O2PmfLEgemUPPoFd1g0InXsJfFIV85zEzwOLJeGcqcFDL8sWt6ZAIz49Of6kwZ7kNUYsG46MzAVNK+m/SW+JOgNrDiyBjHujt06QJPoh9DL/PEVcfTQHkgD7VtXVaB7m1eQQDWXzGXI0iPiQp2buhEhc+KRb2SdZFuMIe/rNV5hY8nSseNt2P8mPSBmUv7AA3ec7ORuux2TGAM0JFzZy8K29ZextI9y0TNgJhVdwPPzkkqUKWxvwqxhXtxbJm2rio+Wmlq9FQ3Yp98cPKixvEGmuK6HXdgjs7x0HVzjwiuQ35Olke73VVfsSswX7IExPaN33ZbN7Q+Ol89tyIyT0vJAtmOWi+4N/eVYLf2hgk6sodHqcR653xzeMLUtqnraTmNaZomHDlgPbYOHm0DJrv6psKZY/mMi+DP6WEJBXeKVeWBw0+BWx5S9XRuyno82iZUNU/lPCIvEolC+CoVbv2AKX4Q6cIoauAkDYMTUxglDuRneA0cLyrUIJCk+sbNq8znk96lNZ/tBazWDHsMk2taRPgKePuUcwruFYsgmEVtXc4XZSOgJb/NYLp5Mjt3kcpNGlruqA4aezJyqCjIdg05vaCi0x6rPcpmyRqb7Zhw1sm+PU6gaOJjj/SeBUq68zllhW567zd2/jA45HR9sGNIkQ1A4IYWUJD10NYwyCmubYkwT+49ZFi6gkyLWxSSF9kZ9RX9emlwp8R4WVWiliZvtJxI2hbf1YEaR81bFKtL0Ed7Fu4KJIgAtO+CVSaI1z9sZ+yss3CzbE3ZkK4EfiKJpl3bi7yGhhzkfSo2BHKv/VBgHFkJw0D2MvPVOIzR8YvV3F0q4vg0SziYqW0FJw0Lhe0g0GCneew51Lo1/EpONSEJw4NtdmQSqiA+KxP+SDezvve6cSL1SXhwz6jZEK3FXEVC7yOdGefLYvmCgAyoqk14ozaoKCnEneTpyn+BHiAqo6tc3EPuNtYbKeaukJ1fXpGy0JyaMJsfT8/qpAa7pud0kKZSz2WM59vPB+YivnYVKfWKuauXeW5aeeHk9LucbuS9a9GANJ7ExjGDScdgDIPKzqQnT8y20b8CCu3qWff0lTshlEGRdG7it9f60AkaKZ7hxt1uqcrM20139AVZHlv+mtS5ngPMpfsyEEXvOjrcxAlrFeewFTTtTFxXUsisqZ5qb6sRTsof1XA1dgJsuY06m25+Kfd95TZdJV8QozvRN7EtIMLzAjAUcDEX8KxNrJp9fjKP3iDDoI5tQvO2LJ8qbgzmotLqDS5dKq/mU3m9cwtbQi5/vARn2MsS1ZK2KHatu86R61jf7yWen9rsyaEAHBZ6D1NiJIts8LwnY50vTny3k+vxuTGEMCJQtVndY5yo+9P3YN/GHxjebgQPGbE3SFeN1yZGRG+z4/GDl/aP68xwwZbrvu7N7bMI72fk8aix54TA0uMk71rpLm7XqIR1fKbKUr4nlepag06s9du+Dtu1qmR1RK+bI27X6sYoSh10L359jbGIPW9rz9DwA7NdcUzMB03fzKy4Odu81GpwDjGZHbCyletNI3C7J5EYrs9aGlpDlstdU50K3qRZFsPAvMMj1cVIBtpTS+4mXB1rkjlMrdpALL04DPY7xmwPPNXN5wOOVZxPG3fE703E+62u4kxd3I9BwbdQvFKC8Yg9VqPWTQcUQOPnUzCj5M6W3KpZMi7fC9Xjn0nDDoS11XAl3Dpt0kXDu3QSpJYintebPY7FVX9VPZ5V/W27WpKeOdeqnK2JZvyJ9YzMZgDhCk88RYbrZYKNG8cnM09yL2ldpof3ypDLEI8xxB/by6TCYjHP3a3CDFxSWxtgmTtGnddcUUNcXD6/NbU+JsFRwLmeNO9hatXay5jXyFSssoeq6sQOLEGHytU20Yt9jV6YPaMdwGjjvp6kVBj9cAbtT3AKufjOEX1aKoImwql3vwTOC3XVo44iAHhhOj1XlzgnXPR0NTC2j6rs+nJAd/6YjWdCXoQVX9PVRuUmOWfc3CvrMF6rtWCPJ5GQlQbLGo3xPOJ8eZVL5rSZIVok6OrWIDhhwlO0OkJ6DdGc9mw52H0y3wbl+GiVyEyFBPReUMOsM5hHN71QFaYpLeuo4zoqFxWD78cSkYw01QrC8vNBQlD/HifXLCAF/kH5+uVcbrfLiSbqF66CKWODMhLlGd1nms5tKc0F51yyUnZPtBMCTLiXp8V04KA95jWh9fgYRRcTMokikSmlmq+ja+sj7iJrTdT1bbrNt47xrhcfogbj5Cm6rCiE2d6L3fSpBjpDyxzzj3NtJzXuPgEs1E0tBlPktdLdy6Ey5TtCEI8yhVImpxyDOSwYy5PiB5+s7FRANBgQd64oS6c4NxhSOYPkMdt4BS2nNW3tsW3HYt0HzdR0dk8e5NJz+q3bvBtUhhNl2dU1vHXdWt6cix519c1wJZ1QltRlMWRB4dM5gav5IqmD/VB4bivyLUeOsqYycDsSTyIbHuY62dkl46lnSpaOEMO4xatI4gkaziQPOSkopTkfZXFPTkdDGQzLpBgqqu/xVsCJ9VxrxJFo8chKdv/COiytFwt5VqF6iQ0jI2eTke1I0I3SqoigLm0sUiu0SqwU10ynDtYbFzyoyltuI2bGtGkxMJ8tjsddnmUI2kUS9XpzPyWFObz80IZSyCKpdUlAOEyF08UERk7RhBJzeoyN/nq9aGZG2uKwtK8o7FZyn91YmZ/8I3Uwx669EO/P/dnQK8ExvVqAO6Nyd5TR5Bd+vzRsVGopIdiaFe9D/n7VdZTAPgzqq/ql8pe524h+K8YsbTxBJAZL56sdtq99WQsIgD7Afe21L46DS2AUhhHEi6LgcA+deSNkCH45M0SyHLyejomuYWy2oYNfGy9lS/q6YEJ5lkHnv4VXump6qAtq5/kCzEhOyIwQ2XiWOlencFKQzjtqhT7uLYw3IdbJWDBfRqTofH+RCy/QrQ+pNRR603Re8GWBlar3mGKkWAHFEa6ATgtCotoI7brOJk2TkLPazBmC9uC0BOHE2BWwMGY7UTBU4jb4SsXcouGFlBpjPp9dcxVvIUXAYdNqCHrapfOs7lB0a3ZRmdWA6MQznoNOZhiPNXK0qHDtKiZETT9KNunJYNf8tY2tvsGjwh490W4E7OJfkuaZLcmqDhiO02fjMROLSUBkOq/bmS+ouj9pK7r0lZo5ujuR3Yvl8dfzOmO9zPatJjQbKTMC8YKvtaiEsXijZh5tg+cri6Yj7o0XoYPVW+rr0esqhLyAez4HX/d8IPFj3J8ISj2To+6ifpTR9KefPr3foP/2kvbffYPw/SLt/2/v83599bZ9vb9aFCXvd5aHJIh/+djrl7/d/X/+9GmICrD31/eRx2rOfnuZ9+/eRv5cTJ+/exv56xelvkRtMyXr9Nsr6VOQvb/hDI4Llny3ehraOQSlkLft+31scOf9PZy3mq/vm7+N+fiyycer0sjPJ2DSv/83F8Y3ifY9AAA= -->
