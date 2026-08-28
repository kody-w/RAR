"""
Voice to CRM ServiceNow Agent — a template you are meant to mutate.

Creates ServiceNow-style incidents from voice input, searches knowledge
articles, routes assignments, and tracks status updates. The agent now
has a REAL ServiceNow-shaped backend: the Static ITSM desk serves the
incident and cmdb_ci tables in genuine Table-API shape, and each CI's
u_d365_customerassetid joins back to the CRM customer asset.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     sibling systems (synthetic data, no credentials, works anywhere):
       ITSM — the Static ITSM desk (real ServiceNow Table-API shape:
       {"result": [...]}, INC numbers, coded state/priority, reference
       fields as {display_value, link, value}):
         https://kody-w.github.io/static-itsm/api/now/table/
       CRM — the Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="status_update", incident_number="INC0010025")
     — a real desk incident ("AsterPrint M420 control panel
     intermittently restarts", Copper Kite Design); the output walks
     the join: incident -> cmdb_ci "Copper Kite Design AsterPrint
     M420 17" -> u_d365_customerassetid -> the SAME asset in the CRM
     (msdyn_customerassets), with account and product from the CRM
     side. CRM cases still resolve too (e.g. "CAS-260128").
  2. No network? Everything falls back to the embedded demo layer below
     (_INCIDENTS / _KB_ARTICLES) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     VOICE_TO_CRM_SERVICENOW_ITSM_URL to any ServiceNow Table-API-shaped
     endpoint (your real instance) and VOICE_TO_CRM_SERVICENOW_DATA_URL
     to any OData-shaped endpoint, or replace the fetchers with real
     clients. The fields the rest of the file needs are listed in
     _normalize_live_incident() / _normalize_itsm_incident() —
     assignment group, impact, and urgency are labeled "n/a —
     enrichment seam"; wire your priority rules there.

OPERATIONS
  incident_create | knowledge_search | assignment_routing
  | status_update
  kwargs: operation (required), incident_number (embedded 'INC-20001',
  a live desk incident like 'INC0010025', or a live CRM case number
  like 'CAS-260128')
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
    "version": "1.2.0",
    "display_name": "Voice to CRM (ServiceNow)",
    "description": "Tracks incidents from a simulated ServiceNow Table-API desk, joining each CI's u_d365_customerassetid to the live D365 asset; offline fallback.",
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
# The agent's NATIVE system: the Static ITSM desk — real ServiceNow
# Table API shape. Point at your own instance:
#   export VOICE_TO_CRM_SERVICENOW_ITSM_URL=https://your-instance/api/now/table
ITSM_SOURCE_URL = os.environ.get(
    "VOICE_TO_CRM_SERVICENOW_ITSM_URL",
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
    """Fetcher for the agent's native ServiceNow-shaped ITSM desk. Same
    rules as _fetch_collection — lazy, one bounded GET, [] on ANY
    failure — but parses the Table API envelope {"result": [...]} and
    caches in _LIVE_CACHE keyed by full URL."""
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


def _sn_value(ref):
    """Extract the sys_id side of a ServiceNow reference field."""
    return ref.get("value", "") if isinstance(ref, dict) else ""


def _normalize_itsm_incident(row):
    """Project a REAL ServiceNow Table-API incident row onto the shape
    this agent uses. Impact/urgency/assignment_group are not served by
    the desk export — enrichment seams."""
    return {
        "number": row.get("number", ""),
        "short_description": row.get("short_description", "Untitled incident"),
        "description": row.get("description", ""),
        "category": str(row.get("category", "incident")).title(),
        "subcategory": None,        # enrichment seam
        "impact": None,             # enrichment seam — wire your priority rules
        "urgency": None,            # enrichment seam
        "priority": _SN_PRIORITY.get(str(row.get("priority", "")), "P3-Medium"),
        "state": _SN_STATE.get(str(row.get("state", "")), str(row.get("state", ""))),
        "assigned_to": _sn_display(row.get("assigned_to")) or "unassigned",
        "assignment_group": None,   # enrichment seam
        "caller": row.get("company", "Unknown"),
        "opened_at": row.get("opened_at", ""),
        "sla_breach_at": "n/a",
        "work_notes": "",
        "cmdb_ci_name": _sn_display(row.get("cmdb_ci")),
        "cmdb_ci_sys_id": _sn_value(row.get("cmdb_ci")),
        "_live": True,
        "_itsm": True,
    }


def _live_itsm_incidents(active_only=False):
    """number-keyed dict of desk incidents; {} when offline."""
    rows = _fetch_itsm_table("incident")
    if active_only:
        rows = [r for r in rows if r.get("active") == "true"]
    return {
        i["number"]: i
        for i in (_normalize_itsm_incident(r) for r in rows)
        if i["number"]
    }


def _ci_join_section(inc):
    """For a desk incident, walk incident -> cmdb_ci -> the CRM customer
    asset via the CI's u_d365_customerassetid. Returns a markdown block,
    or '' for non-desk incidents."""
    if not inc.get("_itsm") or not inc.get("cmdb_ci_sys_id"):
        return ""
    ci = next(
        (c for c in _fetch_itsm_table("cmdb_ci")
         if c.get("sys_id") == inc["cmdb_ci_sys_id"]),
        None,
    )
    if ci is None:
        return (f"**Configuration Item:** {inc['cmdb_ci_name']} "
                f"(cmdb_ci table unreachable — join skipped)\n\n")
    asset_id = ci.get("u_d365_customerassetid", "")
    if asset_id:
        asset = next(
            (a for a in _fetch_collection("msdyn_customerassets")
             if a.get("msdyn_customerassetid") == asset_id),
            None,
        )
        if asset:
            crm_line = (
                f"| CRM asset (msdyn_customerassets) | {asset.get('msdyn_name', '')} |\n"
                f"| CRM account | {asset.get('msdyn_accountname', '')} |\n"
                f"| CRM product | {asset.get('msdyn_productname', '')} |\n"
            )
        else:
            crm_line = "| CRM asset | id not found in live CRM (tenant unreachable?) |\n"
        join_id_line = f"| u_d365_customerassetid | {asset_id} |\n"
    else:
        crm_line = ""
        join_id_line = "| u_d365_customerassetid | n/a — enrichment seam (service CI, no CRM asset) |\n"
    return (
        f"**Configuration Item -> CRM Asset Join (live cmdb_ci + live Dynamics 365):**\n\n"
        f"| Field | Value |\n|---|---|\n"
        f"| CI name | {ci.get('name', '')} |\n"
        f"| CI class | {ci.get('sys_class_name', '')} |\n"
        f"| CI company | {ci.get('company', '')} |\n"
        f"{join_id_line}"
        f"{crm_line}\n"
    )


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
    """Embedded demo incidents first, then the native ServiceNow-shaped
    desk, then live CRM cases. Returns (incident, source) with source
    in {'demo', 'itsm', 'crm'}."""
    if inc_num in _INCIDENTS:
        return _INCIDENTS[inc_num], "demo"
    desk = _live_itsm_incidents()
    if inc_num in desk:
        return desk[inc_num], "itsm"
    live = _live_incidents()
    if inc_num in live:
        return live[inc_num], "crm"
    return list(_INCIDENTS.values())[0], "demo"


_DETAIL_SOURCE = {
    "itsm": "LIVE incident from the ServiceNow-shaped ITSM desk",
    "crm": "LIVE case from the Aster Lane Dynamics 365 tenant",
    "demo": "embedded demo layer (simulated)",
}


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
    """Case-insensitive so desk categories ('Hardware' from 'hardware')
    match the embedded KB the same way embedded incidents do."""
    matches = [
        kb for kb in _KB_ARTICLES.values()
        if kb["category"].lower() == str(category).lower()
    ]
    return sorted(matches, key=lambda x: x["views"], reverse=True)


def _incident_queue():
    """The native ServiceNow-shaped desk when reachable, then live CRM
    cases, then embedded demo incidents. Returns
    (incidents_by_number, source) with source in {'demo','itsm','crm'}."""
    desk = _live_itsm_incidents(active_only=True)
    if desk:
        return desk, "itsm"
    live = _live_incidents()
    if live:
        return live, "crm"
    return _INCIDENTS, "demo"


def _queue_source_line(source):
    return {
        "itsm": "Queue source: LIVE active incidents from the ServiceNow-shaped ITSM desk (real Table-API shape)",
        "crm": "Queue source: LIVE open cases from the Aster Lane Dynamics 365 tenant (read as incidents)",
        "demo": "Queue source: embedded demo layer (simulated — live desk and tenant unreachable)",
    }[source]


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
        queue, q_source = _incident_queue()
        rows = ""
        for inc in list(queue.values())[:12]:
            rows += f"| {inc['number']} | {inc['short_description'][:40]} | {inc['priority']} | {inc['state']} | {_na(inc['assignment_group'])} |\n"
        more = f"(showing 12 of {len(queue)})\n" if len(queue) > 12 else ""
        inc, inc_source = _resolve_incident(inc_num)
        impact = _na(inc["impact"])
        urgency = _na(inc["urgency"])
        return (
            f"**Incident Queue**\n\n"
            f"| Number | Description | Priority | State | Group |\n|---|---|---|---|---|\n"
            f"{rows}{more}\n"
            f"**Detail: {inc['number']}** ({_DETAIL_SOURCE[inc_source]})\n\n"
            f"| Field | Value |\n|---|---|\n"
            f"| Short Description | {inc['short_description']} |\n"
            f"| Category | {inc['category']} / {_na(inc['subcategory'])} |\n"
            f"| Priority | {inc['priority']} (Impact: {impact}, Urgency: {urgency}) |\n"
            f"| State | {inc['state']} |\n"
            f"| Assigned To | {inc['assigned_to']} |\n"
            f"| Caller | {inc['caller']} |\n"
            f"| SLA Breach | {inc['sla_breach_at']} |\n\n"
            f"**Description:** {inc['description']}\n\n"
            f"{_ci_join_section(inc)}"
            f"{_queue_source_line(q_source)}\n"
            f"Source: [ServiceNow-Shaped ITSM Desk + Live Dynamics 365 Tenant]\nAgents: VoiceToCRMServiceNowAgent"
        )

    def _knowledge_search(self, inc_num):
        inc, _source = _resolve_incident(inc_num)
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
        inc, inc_source = _resolve_incident(inc_num)
        sla = _SLA_DATA.get(inc["priority"], _SLA_DATA["P3-Medium"])
        queue, q_source = _incident_queue()
        by_priority = {}
        for i in queue.values():
            by_priority.setdefault(i["priority"], []).append(i)
        summary_rows = ""
        for pri in ["P1-Critical", "P2-High", "P3-Medium", "P4-Low"]:
            count = len(by_priority.get(pri, []))
            summary_rows += f"| {pri} | {count} |\n"
        return (
            f"**Status Update: {inc['number']}** ({_DETAIL_SOURCE[inc_source]})\n\n"
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
            f"{_ci_join_section(inc)}"
            f"**Overall Queue:**\n\n"
            f"| Priority | Count |\n|---|---|\n"
            f"{summary_rows}\n"
            f"{_queue_source_line(q_source)}\n"
            f"Preview only — no incident record was written.\n"
            f"Source: [ServiceNow-Shaped ITSM Desk + Live Dynamics 365 Tenant]\nAgents: VoiceToCRMServiceNowAgent"
        )


if __name__ == "__main__":
    agent = VoiceToCRMServiceNowAgent()
    print("=" * 60)
    print("EMBEDDED DEMO INCIDENT (works offline)")
    print(agent.perform(operation="status_update", incident_number="INC-20001"))
    print()
    print("=" * 60)
    print("LIVE SERVICENOW-SHAPED DESK INCIDENT (fetched over HTTP;")
    print("walks incident -> cmdb_ci -> u_d365_customerassetid -> the")
    print("SAME asset in the live CRM; falls back offline)")
    print(agent.perform(operation="status_update", incident_number="INC0010025"))
    print()
    print("=" * 60)
    print("LIVE CRM CASE (the CRM side still resolves too)")
    print(agent.perform(operation="status_update", incident_number="CAS-260128"))
    print()
    print("=" * 60)
    print(agent.perform(operation="incident_create", incident_number="INC0010001"))
