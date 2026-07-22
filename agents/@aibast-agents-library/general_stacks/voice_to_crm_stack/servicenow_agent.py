"""
Voice to CRM ServiceNow Agent — a template you are meant to mutate.

Creates ServiceNow-style incidents from voice input, searches knowledge
articles, routes assignments, and tracks status updates. In this
template a Dynamics 365 CASE is read as the incident record — same
triage shape, different label — until you point the seam at a real
ServiceNow instance.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live cases over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="status_update", incident_number="CAS-260128")
     — the tenant's real seeded case "Substation feeder fault flagged
     in telemetry export" (Prairie Wind Energy Cooperative, High).
  2. No network? Everything falls back to the embedded demo layer below
     (_INCIDENTS / _KB_ARTICLES) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     VOICE_TO_CRM_SERVICENOW_DATA_URL to any OData-shaped endpoint, or
     replace _fetch_collection() with a ServiceNow Table API client.
     The fields the rest of the file needs are listed in
     _normalize_live_incident() — assignment group, impact, and
     urgency are labeled "n/a — enrichment seam"; wire your CMDB and
     priority rules there.

OPERATIONS
  incident_create | knowledge_search | assignment_routing
  | status_update
  kwargs: operation (required), incident_number (embedded 'INC-20001'
  or a live case number like 'CAS-260128')
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/voice_to_crm_servicenow",
    "version": "1.1.0",
    "display_name": "Voice to CRM (ServiceNow)",
    "description": "Tracks incidents over live cases from a simulated Dynamics 365 tenant with KB search, routing, and status updates; offline fallback.",
    "author": "AIBAST",
    "tags": ["servicenow", "itsm", "incidents", "knowledge-base", "routing"],
    "category": "general",
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
#   export VOICE_TO_CRM_SERVICENOW_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with a ServiceNow Table API client.
# Downstream code only needs the fields produced by
# _normalize_live_incident().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "VOICE_TO_CRM_SERVICENOW_DATA_URL",
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


# Dynamics case priority has no P1 tier, so the mapping is deliberately
# conservative: High -> P2, Normal -> P3, Low -> P4.
_PRIORITY_MAP = {"High": "P2-High", "Normal": "P3-Medium", "Low": "P4-Low"}


def _normalize_live_incident(row):
    """Project a Dynamics case record onto the ServiceNow incident shape
    this agent uses. THIS is the contract your replacement data source
    must meet — a dict with these keys. None means 'not available from
    the case alone' and renderers label it as an enrichment seam."""
    priority = row.get("prioritycode@OData.Community.Display.V1.FormattedValue", "Normal")
    return {
        "number": row.get("ticketnumber", row.get("incidentid", "")),
        "short_description": row.get("title", "Untitled case"),
        "description": row.get("description", ""),
        "category": row.get("casetypecode@OData.Community.Display.V1.FormattedValue", "Case"),
        "subcategory": None,        # enrichment seam
        "impact": None,             # enrichment seam — wire your priority rules
        "urgency": None,            # enrichment seam
        "priority": _PRIORITY_MAP.get(priority, "P3-Medium"),
        "state": row.get("statuscode@OData.Community.Display.V1.FormattedValue", "Open"),
        "assigned_to": row.get("owneridname", "unassigned"),
        "assignment_group": None,   # enrichment seam — wire your CMDB
        "caller": row.get("primarycontactidname") or row.get("customeridname", "Unknown"),
        "opened_at": row.get("createdon", ""),
        "sla_breach_at": row.get("resolveby") or "n/a",
        "work_notes": "",
        "_live": True,
    }


def _live_incidents():
    """number-keyed dict of live OPEN tenant cases; {} when offline."""
    rows = _fetch_collection("incidents")
    return {
        i["number"]: i
        for i in (_normalize_live_incident(r) for r in rows if r.get("statecode") == 0)
        if i["number"]
    }


def _resolve_incident(inc_num):
    """Embedded demo incidents first, then live tenant cases.
    Returns (incident, is_live)."""
    if inc_num in _INCIDENTS:
        return _INCIDENTS[inc_num], False
    live = _live_incidents()
    if inc_num in live:
        return live[inc_num], True
    return list(_INCIDENTS.values())[0], False


def _na(value):
    return "n/a — enrichment seam" if value is None else value


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_INCIDENTS = {
    "INC-20001": {
        "number": "INC-20001", "short_description": "Email server unresponsive - 500+ users affected",
        "description": "Exchange Online hybrid connector failing. Users unable to send/receive emails since 8:15 AM. Cloud-to-on-prem sync broken.",
        "category": "Infrastructure", "subcategory": "Email",
        "impact": 1, "urgency": 1, "priority": "P1-Critical",
        "state": "In Progress", "assigned_to": "Sarah Chen",
        "assignment_group": "Network Operations",
        "caller": "Marcus Thompson", "opened_at": "2025-11-14T08:20:00Z",
        "sla_breach_at": "2025-11-14T09:20:00Z",
        "work_notes": "Exchange hybrid connector logs show certificate expiry. Renewing certificate now.",
    },
    "INC-20002": {
        "number": "INC-20002", "short_description": "VPN authentication failing for remote workers",
        "description": "Pulse Secure VPN returning authentication errors for users with MFA enabled. Started after last night's Azure AD update.",
        "category": "Network", "subcategory": "VPN",
        "impact": 2, "urgency": 2, "priority": "P2-High",
        "state": "Assigned", "assigned_to": "Mike Torres",
        "assignment_group": "Network Operations",
        "caller": "Lisa Wong", "opened_at": "2025-11-14T08:45:00Z",
        "sla_breach_at": "2025-11-14T12:45:00Z",
        "work_notes": "Investigating Azure AD conditional access policy changes from last night.",
    },
    "INC-20003": {
        "number": "INC-20003", "short_description": "Printer offline on Floor 3 - Board room",
        "description": "HP LaserJet Pro M428 in Board Room 3A showing offline. Executive presentation at 10 AM requires printing.",
        "category": "Hardware", "subcategory": "Printer",
        "impact": 3, "urgency": 2, "priority": "P3-Medium",
        "state": "Open", "assigned_to": "unassigned",
        "assignment_group": "Desktop Support",
        "caller": "Jennifer Walsh", "opened_at": "2025-11-14T09:00:00Z",
        "sla_breach_at": "2025-11-14T17:00:00Z",
        "work_notes": "",
    },
}

_KB_ARTICLES = {
    "KB0010234": {"number": "KB0010234", "title": "Exchange Hybrid Connector - Certificate Renewal", "category": "Email", "views": 1247, "rating": 4.8, "resolution_steps": ["Open Exchange Admin Center", "Navigate to Organization > Sharing", "Renew federation certificate", "Restart MSExchangeHybridService", "Verify mail flow with Test-MailFlow cmdlet"], "last_updated": "2025-10-15"},
    "KB0010198": {"number": "KB0010198", "title": "VPN MFA Authentication Troubleshooting", "category": "Network", "views": 2340, "rating": 4.5, "resolution_steps": ["Check Azure AD Conditional Access policies", "Verify MFA service health at status.azure.com", "Clear VPN client cached credentials", "Re-register MFA method at aka.ms/mfasetup", "Test with basic authentication first"], "last_updated": "2025-11-01"},
    "KB0010156": {"number": "KB0010156", "title": "HP LaserJet Printer Offline Recovery", "category": "Hardware", "views": 3890, "rating": 4.2, "resolution_steps": ["Power cycle the printer (30 second wait)", "Check network cable / WiFi connection", "Run printer troubleshooter on client PC", "Reinstall printer driver if needed", "Clear print queue and restart spooler"], "last_updated": "2025-09-20"},
    "KB0010301": {"number": "KB0010301", "title": "ServiceNow Incident Escalation Procedures", "category": "Process", "views": 890, "rating": 4.6, "resolution_steps": ["Verify incident priority matrix", "Contact assignment group lead", "Update incident with escalation notes", "Notify management per escalation policy", "Track response time against SLA"], "last_updated": "2025-10-28"},
}

_ASSIGNMENT_GROUPS = {
    "Network Operations": {"manager": "David Kim", "members": 6, "active_incidents": 8, "avg_resolution_hours": 3.5, "sla_met_pct": 96.2},
    "Desktop Support": {"manager": "Lisa Park", "members": 8, "active_incidents": 22, "avg_resolution_hours": 5.2, "sla_met_pct": 92.8},
    "Application Support": {"manager": "James Mitchell", "members": 5, "active_incidents": 12, "avg_resolution_hours": 4.8, "sla_met_pct": 94.5},
    "Database Administration": {"manager": "Maria Santos", "members": 3, "active_incidents": 4, "avg_resolution_hours": 6.1, "sla_met_pct": 97.0},
    "Security Operations": {"manager": "Frank O'Brien", "members": 4, "active_incidents": 3, "avg_resolution_hours": 2.8, "sla_met_pct": 98.5},
}

_SLA_DATA = {
    "P1-Critical": {"response_min": 15, "resolution_hours": 1, "notification": "VP IT + On-Call Manager", "update_frequency_min": 15},
    "P2-High": {"response_min": 30, "resolution_hours": 4, "notification": "Assignment Group Manager", "update_frequency_min": 30},
    "P3-Medium": {"response_min": 60, "resolution_hours": 8, "notification": "Assignment Group", "update_frequency_min": 60},
    "P4-Low": {"response_min": 240, "resolution_hours": 24, "notification": "Queue", "update_frequency_min": 240},
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _match_kb_article(category):
    matches = [kb for kb in _KB_ARTICLES.values() if kb["category"] == category]
    return sorted(matches, key=lambda x: x["views"], reverse=True)


def _incident_queue():
    """Live open cases when reachable, embedded demo incidents otherwise.
    Returns (incidents_by_number, is_live)."""
    live = _live_incidents()
    if live:
        return live, True
    return _INCIDENTS, False


def _queue_source_line(is_live):
    if is_live:
        return "Queue source: LIVE open cases from the Aster Lane Dynamics 365 tenant (read as incidents)"
    return "Queue source: embedded demo layer (simulated — live tenant unreachable)"


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class VoiceToCRMServiceNowAgent(BasicAgent):
    """
    Voice-to-CRM agent for ServiceNow.

    Operations:
        incident_create     - create a new incident from voice input
        knowledge_search    - search KB articles for resolution
        assignment_routing  - route incidents to appropriate teams
        status_update       - update incident status and work notes
    """

    def __init__(self):
        self.name = "VoiceToCRMServiceNowAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "incident_create", "knowledge_search",
                            "assignment_routing", "status_update",
                        ],
                        "description": "The ServiceNow operation to perform",
                    },
                    "incident_number": {
                        "type": "string",
                        "description": "Incident number (e.g. 'INC-20001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "incident_create")
        inc_num = kwargs.get("incident_number", "INC-20001")
        dispatch = {
            "incident_create": self._incident_create,
            "knowledge_search": self._knowledge_search,
            "assignment_routing": self._assignment_routing,
            "status_update": self._status_update,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(inc_num)

    def _incident_create(self, inc_num):
        queue, is_live = _incident_queue()
        rows = ""
        for inc in list(queue.values())[:12]:
            rows += f"| {inc['number']} | {inc['short_description'][:40]} | {inc['priority']} | {inc['state']} | {_na(inc['assignment_group'])} |\n"
        more = f"(showing 12 of {len(queue)})\n" if len(queue) > 12 else ""
        inc, inc_is_live = _resolve_incident(inc_num)
        impact = _na(inc["impact"])
        urgency = _na(inc["urgency"])
        detail_source = (
            "LIVE case from the Aster Lane Dynamics 365 tenant" if inc_is_live
            else "embedded demo layer (simulated)"
        )
        return (
            f"**Incident Queue**\n\n"
            f"| Number | Description | Priority | State | Group |\n|---|---|---|---|---|\n"
            f"{rows}{more}\n"
            f"**Detail: {inc['number']}** ({detail_source})\n\n"
            f"| Field | Value |\n|---|---|\n"
            f"| Short Description | {inc['short_description']} |\n"
            f"| Category | {inc['category']} / {_na(inc['subcategory'])} |\n"
            f"| Priority | {inc['priority']} (Impact: {impact}, Urgency: {urgency}) |\n"
            f"| State | {inc['state']} |\n"
            f"| Assigned To | {inc['assigned_to']} |\n"
            f"| Caller | {inc['caller']} |\n"
            f"| SLA Breach | {inc['sla_breach_at']} |\n\n"
            f"**Description:** {inc['description']}\n\n"
            f"{_queue_source_line(is_live)}\n"
            f"Source: [Incident Queue + Live Dynamics 365 Tenant]\nAgents: VoiceToCRMServiceNowAgent"
        )

    def _knowledge_search(self, inc_num):
        inc, is_live = _resolve_incident(inc_num)
        matches = _match_kb_article(inc["category"])
        kb_rows = ""
        for kb in matches:
            kb_rows += f"| {kb['number']} | {kb['title'][:40]} | {kb['category']} | {kb['rating']}/5 | {kb['views']:,} |\n"
        if not kb_rows:
            kb_rows = "| No matches | - | - | - | - |\n"
        top = matches[0] if matches else None
        steps = ""
        if top:
            steps = "\n".join(f"{i+1}. {s}" for i, s in enumerate(top["resolution_steps"]))
        else:
            steps = (
                f"No KB articles cover category \"{inc['category']}\" yet — the "
                "embedded KB is demo data; wire your real knowledge base at the "
                "LIVE DATA SEAM."
            )
        return (
            f"**Knowledge Search: {inc['category']}** (KB library is embedded demo data — simulated)\n\n"
            f"For Incident: {inc['number']} - {inc['short_description'][:40]}\n\n"
            f"| Article | Title | Category | Rating | Views |\n|---|---|---|---|---|\n"
            f"{kb_rows}\n"
            f"**Top Match: {top['title'] if top else 'None'}**\n\n"
            f"**Resolution Steps:**\n{steps}\n\n"
            f"Last Updated: {top['last_updated'] if top else 'n/a'}\n\n"
            f"Source: [Knowledge Base]\nAgents: VoiceToCRMServiceNowAgent"
        )

    def _assignment_routing(self, inc_num):
        group_rows = ""
        for name, grp in _ASSIGNMENT_GROUPS.items():
            group_rows += f"| {name} | {grp['manager']} | {grp['members']} | {grp['active_incidents']} | {grp['avg_resolution_hours']}h | {grp['sla_met_pct']}% |\n"
        sla_rows = ""
        for pri, sla in _SLA_DATA.items():
            sla_rows += f"| {pri} | {sla['response_min']}m | {sla['resolution_hours']}h | {sla['notification']} | {sla['update_frequency_min']}m |\n"
        return (
            f"**Assignment Routing** (embedded demo data — simulated)\n\n"
            f"**Assignment Groups:**\n\n"
            f"| Group | Manager | Members | Active | Avg Resolution | SLA Met |\n|---|---|---|---|---|---|\n"
            f"{group_rows}\n"
            f"**SLA Targets:**\n\n"
            f"| Priority | Response | Resolution | Notification | Updates |\n|---|---|---|---|---|\n"
            f"{sla_rows}\n\n"
            f"Source: [CMDB + SLA Engine]\nAgents: VoiceToCRMServiceNowAgent"
        )

    def _status_update(self, inc_num):
        inc, inc_is_live = _resolve_incident(inc_num)
        sla = _SLA_DATA.get(inc["priority"], _SLA_DATA["P3-Medium"])
        queue, is_live = _incident_queue()
        by_priority = {}
        for i in queue.values():
            by_priority.setdefault(i["priority"], []).append(i)
        summary_rows = ""
        for pri in ["P1-Critical", "P2-High", "P3-Medium", "P4-Low"]:
            count = len(by_priority.get(pri, []))
            summary_rows += f"| {pri} | {count} |\n"
        detail_source = (
            "LIVE case from the Aster Lane Dynamics 365 tenant" if inc_is_live
            else "embedded demo layer (simulated)"
        )
        return (
            f"**Status Update: {inc['number']}** ({detail_source})\n\n"
            f"| Field | Current | Updated |\n|---|---|---|\n"
            f"| State | {inc['state']} | {inc['state']} |\n"
            f"| Assigned To | {inc['assigned_to']} | {inc['assigned_to']} |\n"
            f"| Priority | {inc['priority']} | {inc['priority']} |\n\n"
            f"**Work Notes:** {inc['work_notes'] or 'No work notes yet'}\n\n"
            f"**SLA Status:**\n"
            f"- Response SLA: {sla['response_min']} minutes\n"
            f"- Resolution SLA: {sla['resolution_hours']} hours\n"
            f"- Breach Time: {inc['sla_breach_at']}\n"
            f"- Update Frequency: Every {sla['update_frequency_min']} minutes\n\n"
            f"**Overall Queue:**\n\n"
            f"| Priority | Count |\n|---|---|\n"
            f"{summary_rows}\n"
            f"{_queue_source_line(is_live)}\n"
            f"Preview only — no incident record was written.\n"
            f"Source: [Incident Queue + Live Dynamics 365 Tenant]\nAgents: VoiceToCRMServiceNowAgent"
        )


if __name__ == "__main__":
    agent = VoiceToCRMServiceNowAgent()
    print("=" * 60)
    print("EMBEDDED DEMO INCIDENT (works offline)")
    print(agent.perform(operation="status_update", incident_number="INC-20001"))
    print()
    print("=" * 60)
    print("LIVE TENANT CASE (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="status_update", incident_number="CAS-260128"))
    print()
    print("=" * 60)
    print(agent.perform(operation="incident_create", incident_number="INC-20001"))
