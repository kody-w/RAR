"""
IT Helpdesk Agent — a template you are meant to mutate.

AI-powered IT support with automated diagnostics, remote remediation,
knowledge base search, escalation routing, and ticket management.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template the tenant's field-service bookable resources are
     reinterpreted as the IT technician bench, and their bookings as the
     technician calendar — e.g. technician "Riley Chen".
     Try: perform(operation="schedule_technician",
                  user_name="Michael Chen")
  2. No network? Everything falls back to the embedded demo layer below
     (_USERS / _TECHNICIANS / _KB_ARTICLES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set IT_HELPDESK_DATA_URL
     to any OData-shaped endpoint (your real Dynamics org, or JSON you
     export from ServiceNow/Jira Service Management), or replace
     _fetch_collection() with your ITSM client. Fields the rest of the
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
    "version": "1.1.0",
    "display_name": "IT Helpdesk",
    "description": "Runs IT support \u2014 diagnostics, remediation, KB search, technician booking \u2014 from a live simulated Dynamics 365 tenant, with an offline fallback.",
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
            f"Source: [All IT Systems]\nAgents: ITHelpdeskAgent"
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
    for op in ["quick_remediation", "process_analysis",
               "knowledge_search", "session_summary"]:
        print("=" * 60)
        print(agent.perform(operation=op, user_name="Michael Chen"))
        print()
