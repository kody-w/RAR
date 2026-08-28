---
name: "rar-aibast-agents-library-voice-to-crm-servicenow"
description: "Tracks incidents from a simulated ServiceNow Table-API desk, joining each CI's u_d365_customerassetid to the live D365 asset; offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/voice_to_crm_servicenow", "rar_sha256": "b2128e1ecda8d8cd29fc5da99be371a0bd0c914aab05cd0825b77e4c57a19210", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.2.0", "author": "AIBAST", "tags": ["servicenow", "itsm", "incidents", "knowledge-base", "routing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/voice_to_crm_servicenow`. The original RAPP
agent is preserved byte-for-byte in `servicenow_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "incident_number": {
      "description": "Incident number (e.g. 'INC-20001')",
      "type": "string"
    },
    "operation": {
      "description": "The ServiceNow operation to perform",
      "enum": [
        "incident_create",
        "knowledge_search",
        "assignment_routing",
        "status_update"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `servicenow_agent.py` and embedded as the fenced Python below (sha256 b2128e1ecda8d8cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `servicenow_agent.py` first:

```bash
python3 servicenow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 servicenow_agent.py   # or on stdin
python3 servicenow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/6276bLbSLIm+Co09Y+qbKSEhcSW12pmsAPEvpEAr66psAMk9oUgkV3v3sFzjqTKrLoz1mZz8keSiAgPD18+/5wK/P4pWuayGz/99olRWMb1Pv36Kc2mZKz6uepa8Ngbo+Q27ao2qdKsnaddPnbNLtpNVbPU0ZylOzcb71WSGd2686K4zj4zlrIDQm6/7q5d1VZtscuipNxxyl+m3fIt3RP4t2SZ5q7JxmiasrlKd3O3m8tsV1f3bMeDCbu3gf/YdXleV222y6O6joEiX4B+2SNq+jqbPv32n//166cKfP702++fkhosAfqeOqCL13GO/lMvpgCag5V11BZgSv8ER27B9z4b825swKM0y3cf3/46ZXX+6+5//s/bGo3F9Mvu8/+1m+bxt6/t7uOv63d/272Pfimy+a9fP3VgbfQy2NdPv+6+fvpurG/JmAETff30y8/FYOxbuzR/lvBjCRiLs/FdjmJwnzEEQdA/SEirqY9mYNC/7X7/+fT19292/m33Os6Xb38a+PXPC29tt9ZZWmTfpiwak/Lnyj+P/MtSYPeqaJuX8LFbZuDvn4v/dexflk9zNC/Tt6VP/6DwHx7/06J//PxYRm1aZyOww3eTvBmz6//Z3Pmu7ebvU3/74+ZjNi9ju8u/fvLb1zHb3Q9H/rb7vev/8fXTzwUfkz8k/fXDj798+geIwRYEyJK81r1C8H/8j51eJWM3dfm8cxNw7t24tHPVZF/br61XViCdprd4H7N7Nk4VSJqPef3YXbM3QSD0d3//f6Iqjqb5c/QK4OlzXcVjND7h+yvGv80dcGYDvPIW5kD9v3/ZeUBoN1ZF1Ub1zmEs62v7tva1YT9mr7kgY+PnnH0Gsf759QFE5O7vP4V8e5v/pX/+fQdO+hp8Kepwyi6J+mmpsy+vQ5zLrP1QOYnaXfbIkgWIqrsE7JtXIDt/BYebuhrk8/w68HSr6hr4aQSn68bnm2xglN9ewv7+97+DU5Zf2/fE3O/e8WeCwYQf6uw+fwYHAGhQlPPXNkvKbveX3//xl93/2v2/rXoT/trDApH4YXKg4dE1jR3IvqV5g7SX/7IofTP57//4MCMQ04LgAg6q8iqbPvCpvWXpd5u6MvMZw4ldnAFbAjs2fTe+QnxXzV92Sr77oS/Y9DU0Adgsu2kG4NhnLcjG5AmkRuA4Pyz5itUJBOCUP3/dLVP2tuvfgdffVGy+JWD633c6ZwHE7OoXbAI13yaBxV1bAfP/8Pj7cyBkBLjLfhfxZWe8gm7XR2PUlwCA3/fIo3e/dOPu+3IgPNq12fq1fWFs9jLVW2q8mwdMApZJPlz6+eXzXdI1DXDs9H3vtzlvNcLrQBgDWGunj+iOxpcrkg6o8twVS5VGbZL9x0dITWW31Omb/YCmL0kfXkg/vPIWg29I/zIBwPp/LkJvaL/7umAIegAnAGfuX4Vq9+yWt22bLALjYF2zgAO9xzP3horTP4n5PM3POvtz3XvLPPCwX+Zfd+94CFb9gEhgexAByXv4g5OAsZ8ICJ69on5+L6jv+LZ7x7fp3abvlgfCvrZl9IoWR2C0P+hURv0rf4EEEEC/vZnGfXkl2Smeq79V3d1bkr/FK/Dch/pvOydNGn9Lqt38qtJvTgL7La/y+rNuv+3wruiPov21/W+q9qu8T2/afC/gL1d8n/Vew9/MK5vnnScr7s4TdEtjPGF3Nh3VfYEr+mVnApeD1Hutj7sHyJ5dv9T19M4GXkEygpB6Rcp78sqeZ717wzubH/j8wtBX5k3PV4xPu79OzxbIexkG2Df6FRh1ByrfyxRVVANPrN0InBC1z7XMxuyXn4XhzY4fwfNvzfvXNyX+Lel5M95PUb9//QQwcKnnV1X7zy9fvvzXP37dgZq+e6/xQIukS4E7X6GQwf1YAeSeny/gBGEP0CH7IQmEfp2+Ymn3+6vU1dHz2z2qF+CoFyL9unv78o9f/rm8lfPcT7/B8K1Ln5/XL0U1l0v8perg6e1An6t5auCor2AQbvBbRMA/Vr+8+K8m4J9t1FTJtHvxszlrX1n0V+aV1jstAkFk5vkrOdx3F/wfKZN+iP4MRL8p9XIafKe/YN+V8sbnbz8Y2o8q/bd/oQ+/7v7EpP72RqMAh0IQDP/Jo37Aw5s33xz7I1cAHXs7ljUCENzpBwwBjmrnEQBuDw5af4gAg9nYVDMwxVw/X+VuBtk/vXTguh6ouFMrADt89gKAX/7jzZQAEwB07Naovk0fYl6PX4n0208FAOP8nqtfP/2rrN1P7T5kvOmIkl8/vZb+N8kKRt6cyejCe2Z+R2ng7Q8xf20m4Ik/rpx+AckC/LWLEoDNH0gCaEoK+M57Fv5RxgSO8OUdB0BteeHcq/D/4AJdt/tr9qX48joY437GCATFKOCWL6/lGChOHSg58ys7/++d8CoOgD2AvH7x/z8iTQacm76yJ82abgcyAtgozuoXdr6f5Rtwu8ILhufu4N03lf3GOJ7CaYL7yz/H9gfkvpXEBJz4BecfTcebSvsvOz26ZS9QAvVjBDk4v63TlJOw4xmP2bkCo7/v/KKu3z1yMhVO+OaZ34AlvrmCcwJfDfP87YUj33xHex0DoM+/xZEPmP+QBIC+716B+NeXAu/x+irlr4L5y5s3/ru9Xuq99voeaO87mjzIre+V5LvwX1+FH7CUOko++EAG6DTAqHffvzb9kJLU1auWvResD1x651XTDxR/IwNtlr0ga3yxpunFAar2Q8S3FiRxVFdb9u0F8T96k7/+8vLUz8EXRP3z4LvbPoT8rKu7ApTa/tcX/wIk5r12LWPxRq/eto+Ad8D+Xz+1cPRHIVkLKEz5JgQU8+brp/8A5x3fqAJgSB+ADDhH/V5Px3eyYFqCw3iKabwVsD91VoCQ/rljAo/+TY8Elv6v3R/RCzx6bwp/+9mIvOrNsACl0l/+BdtAKn3Pgr/86BX/8tYsRe/V84/AVlcgkv/yEw7/8ub2j6nfU/ajOr2EvM//mad/+eXVRL/6hCn79FsLivSvnwBwZ/8fbfeLajYZgKzp1agD7ABnm6vs7dufTvR69MffH5Tvyv848gs9/um4L53mZ/9SAnRhwLKvjuyH+f5V4Ctu/ynrfhoa5Mf3HwR+/QSIUfPpt//8c0MNRv7sXfDoX70LHv7BtZ/+61+UBFp+9+xro58a/5zaxa9m8HWeF4N9/6ni90/AlNGrPn4Y86NfBNNBb/h5ehFoGP2CAA3A9/dGCIz9n3WSH4sBSID+BqyOMeD9DM2SNKJSKkkxOk/wNKLpONuTaITEKZLQ6CGKYgRPUoTC8Jgks0OCkxFKY+hLmQmkFNjq1SJUL4UQlD4QhyzaY/geo2M8zQg6PkQ5QdMkQec4iqMZBrb9ufRWtenHKd9P9TLhj6b2ZY2Pw/7+KSYOYKZ8mBTm/Y+DaYSO9lbs9FoOuUtz0zq3u3C2YzTmijtYTcTdWRMy6yhhEUI7nc9WrqSITLEybnO5nVLUWhh6n+9Z+BkE+43hePF5woPgHCx8OAp9KXskTS5N2klCfA2h0jD9mUNHigqferZPtICCOZPOQso1ChiGTbhJdPdeb7g3aZdjvW5H6Dg9HfTAXbAzsbrZ+YBKFqStSnqRIj0/PpZc54go4xBLjNlIdPcXDdm3bNRjyFl/ppE2MME1ZTMz3VLqEHu9c/BxWNacSIwem12djbtcPR4le9mYPqlvnklXp5suEPR1rgncVGHxUdxNWVEuj6abZPN61IqMRh4PgcNyMfAiFmxQpPWNy/1wvV7T+ghZjhQYeM4YjBMnq0Y+RtUo+/3Sum1aetdnYLImxx89LowzRGyV/cONp70lCUhhc0ADXQScb3ooGEo6BJQ1tYXuBVdrbwIHqUecPMKleLCF51NxGVtUIzbSz51UyeieChtjj2M6Jpercd3mq51PCBXUECrxk21qQbR64kR01NOjNu0pjGkEyZuVL5A/HWZ9TRr9vJ+Oq80S+d1ZrPKg6AcgQGc0qiKxI7meNrGhq07W9OYuNIUp2MeQDfs1CC+GqSiPkHqsibtXfCc0qKPRJprcSpt6uJRMJytaf1LiVKOkdjolx9BMMFqwRJKsUrE+4Zc68CAE02u8XYMRDx1ZtxAkVSTOlZ/QfBgo3VJdPmfUdhXW9eKO4TnMaBS9yW18z67CSlIRlOYrijCXc0YbFW36ZYETD+eiToeFzPa3fRfP/R6dH5q4LEc8PJF6hNWkGzySib5kwZ0J2rvA7JdBp9V5srSrlzHT/dzqhaUUViGpLqnLqkKGg61PySbFnfPUWSPKmUMyOhjJPxnbujXtnb5lowIJFwefljMsduIt1i5FkXfiFMpszYXSWupCOIr+Iz5YscLw2518wBO5TzNpCEP3VsC3kOgavecRgkN5Trfu/ZMmzJUPQuXGtRhWzAEO4I460LLrYjxexRAb2hynKnVJtMSBGa9httL+8yrKkHeBleXJPhWjCuXMzB+mZudM7966fUNudI3a52t+VDTF0K8CX8j5owg1KvJDe+9o9wzzeUX2h30tFA9X1i8MpG3yWfd6RlZWfOsN8aFpsaTabUJ7oevjYaQwQa89tcJLUKdoF+p6ummwWJ7W53FMmnpZ+5no9kGD5jSLx5fiTJtoSPKPG+PTNm2RKlvxZoO5rH2dN98oUTFRgeVwtdKXQLFNjIUcfWGAju7Gs5WaywxsPp4m9oC2fQxtGZ5Xt3zrwsa9ye4zUP3zrIfRuWsp68KbAM02VxaB7Ph6HaSRkYSkDO0ZNb3tYGKyeN9L5tXOaN0zOvHiDj1lyVXPQ+vjkWCKzmS8e4DXOd8qAPBDcSVXyO+1gvPd4aze5D7mGVfNHn6FbadHNklJJxQeS3j5kdV8LwyYw8l1p8ShRCoprKlbB02MNd117DNWRKEnbkHBpUV3dmFPMhO/8GmaX5/udKVtHGNxPHDbprHTs24ywMRS6M0UD7c2e+ElTg650BzJvUmmTpQu6hOfGqEqySrr5XxtfaEwbnQvG+vZXWyNC1QsizhuQa4dFyEHLMRsqVoNR5rM9AYHNztLdZG20+3OO1BxPUkX83btS3uq6AjSlZuD3QftkHFPYwO4KSRjrQ6OGtwYUpibTULLPSQ67OAalxI9iPseCr3mxAr0QvaPTm7TyzAGdnx/YmxbJhPhrra4+hNEMScyISGCo1PQT1w5awpQvIacw0r6RHPYR8pTU/vbre8vGKMj3uo9HGwLQ26PMvytrCUOLzXise4PEYElF0lgOVjpooy8+rAgzKeLlwcSzRk25pEUeXtcYaNBYiwxMe9U5eGplqA7rOJhZyDYirjHWW+NKsZuCnV0yjvFinhUDGtOOWXHE3eFhvfHMqoEq3ogeWXCuQHDy2JBG8TApLKXNS3bCA7GxPYOm94c8h60ErA696l50DHGHmPjOhd0FflOQeIXc2FE6SJt5/F8JNpJRkfSERbIaWB+3j9WC+IUh88UDOHnZzch2ZLWmNAdfW1BQ0K0bZf241Se9EPn87JYpbHo1SrROgklsjptGZd5YB+0pZyfp+ekyetmT9B9NbGYrKW4jcbA53yUjS5Z7AxDliYXgqhH1zpafihXKEn16uo3vo9UfcQh9a2tNpZj5KmN98N1CobMtPRQ9lH+8WBA/uZuQPo6fDwOsxcXEoy0NtY9D+hgGp0vbpPRFbDOGDabBcgewR4DkmnqQzhQnmQY63JaZUqw0ZsE+Fxbr9WDTXu4TIuTwIkZ/mCyNr+xe8wQzwyyUQhcbFyQMwXCQkcSX0+I0fFOcaxbp6aECEHunZE99ltja2tRjA0uIwQDsQvG6a0a3y0JQRiZHVp0426KUEllRYvCVu8Pl8B5eOVqKvA2HTP4LGyh0Ex2AzF6WbB8xh15fll5/jjTs54RpZChHEtyVIvUmgVFi6w2CqOnQ0kLFAkHvH8ctrA32/BG83so9WqhX8XQtc69QpW90spsoVF2aT+KukiR20MsJt5WQdrimr448qIlsS1BpUeSjzDfl1DM8pDzSHKtEwhCZbLu7MtU7la6xjeWdFO5ANNzYeTuG7EUD1G3pYxYbUmlnC3RHsxZsUMUehSddQCkAkmPrk/rsSaUZmqYt1EaqCHKH2qg5hS9DU5XyRuzHyw56FDPoE+uX98MzB7ORjXFCw2Pd7Yp737QELkYlubcyuJtoY52Suewoz5AV8qLB2Exlyc/MzzAmfXRV/HltO/Uw1Wr9cSW0e15YRFRd0tM4LazCVMk7x03S6aM7Rq5bjncxesEyWTAoLg1lLFbTHIauceUYbkQS6sNcas2Au2LZ8PPQfOsOOgKhb/v01Maj03f1Yh/ucOPe6GatHLu8yrerHjWOUA2E7EK2nChYCkfeVvHz74LJ8Rimtxxf0Ti/cqI6dQ4W3ynRvckI09oQ6zz3l/hW9CNNlPmShgqujwqLpfDzXCV19RdlmsddndmKQe/qo9hbjZk8uDDtVtMzmx1XJ3OzeTjTWxfNS87not95Kzs+bCUcUHptHe/jWFhkUx39alqlu6s0o8IQxmTiPLKw6E3WGjZUBM2YU/AyHjOuXt1itWoisI90zNachzVM6H22MiHnLzCjK2IechNt8a2T/Boko9FSe9HDjFG7nAx0LW+mKIyK/5sCB0jHJBhoaAweWgKsqXnKjd1+Ewql/uTdR9YOu6lmE3UYs8wCmsc9IZ7FlJ2VB/HtHbdgsJyxdNsWIRc8Qzo1ZXcAPmvcr/p88MeFy4yGlhQSo7mrYi3kHFjp9rL7XUM0XCOdYhr3Gd5iYurdZ6EvKWbSj9DWUF2CO9YCn5EILjAaYu5Rvp6vU0Vu9H2/oEJMbvvMupMs/4WLLLmkmKLY9oowyy7X+krlfto7gceSwrcjXm2ck1kgfjMrhaUbd6BiqzkyiMrAObCrRqpBWEQa4duOwy2gOTcmieXNEYw52nPBDUcaa4QtWiEq/UYPyScvdfVjefDtrfahrAdXBxYJsPcrL2dHncwNxU2Vw1jjmRtKkyk7Ck4iwwD+nNJHLNjHwotILXfS+dt9WBcjXnDuTXuoAQqDaoQLVVnH5FYM9RnFHbrk7qH+U6Wiq2Q0putZuA/iOTxeMuZ8jgo+Ro9zQ4jFe6qIxyLwQe2Gt2kM47coffSDnw8se0ThNm5KTJeGYVgVg4PeH/ilj1OJpNx9+j50WEoixWCvt48UV84eIBQlCqjukEyZDMp5XHzhX2UJFF3nfWGlQpRKTzvUI7SeYp1286fKZaPSUGeDIhLEZhVmgDSHE+9co5E0E2vK+Hi4lHG4A/vas23jQyUlvSTq0PrZKbQvh3j/EOIkT0EEYQyR88AUw5zOlwXJ6/u2B4GnZcjjGW/cU92MMyqGZ4BZxeHa+QbnJLh+mXq2nKF9XVqHVeDzuXjaKB8hY6w47BZ+kQRnANUMIiGYdxPNqLnBxTtRCI6etJzcJiVLs6OIkb03UgsG2MrXZQoLlhYxscdlaPZcwU8CHmWux4LCA5va7VffDvYH/mgS0KKxyq31C4Ub2HGJi89HNcqrheYUxD9MFh2RaojqoqxiR4LHtrLglOIpCfPt6yx/E2/pcURIZ1kb9v8qmaHXtZQ1JZOzbMG8KBdVvzEtd1ImnG6ly1Eso/V03zezFq61QexAd360bjhmdHrRycVIGEA7E5AKqOTkTrrMLxgOsJsjjKTdPsxaoIOcM46pdE6uHfhAz6teymiE4/fJiyH5MuQxkZBtZ0ULZIxPLZjVGYSAnDgKW03ZK6q+dzXUp3X1j0nCiUwNEuS9m1lZCgGHy+FtKyA9qSmVVmTJvBEsi+uN6bpkfQMsIldECrNfUUsEP8OwF3cHtKhR0lg7XqC3OEJi0XoJxOjU7eEJGJ/PVbuhEPNuXa5pKR05jn2MeEiT+HKcI/A8arFiIXymFpKLvsJCxq0vkzq7Dht4T7by2u4xSRxziLK2xv5ZX8O9qZhmto9JAXWvxwd+nG5Ohvt1pN84bguobvTkT2d5e06unyk7ykjL/Y3pWsYgutSJnSqLvVvYt1NohtftNOiHY5+tRZtz1dyily4JY6V8HSp0dY+DsDViXOeRZE5e02QlTo63sJnhlbt2pXWzXUrJZnOoViPkH1TKvQ0J8LEwVMwe4uirWRXIM5Y+M+QJ1aNpCTnvlem3i2iksfJqb4OJ1UYRvm2EOj1EpXckUzOntckuSQzLvCVTq+erQwtBKy/l6+BaZn3S4ufkSbLBiSWyhR0qYYbdZovZQ5uykkcmfHFUHLrdnSzWU0NsWOl3qr69D6GyTEdLnJU+cnJpTENlTFrEsvYOUqi5cIaqifY7cKzus8g9WoT+eF8eNSMWVmRYTvXCp7T/g6pZDy1gJSZ0NGu7qCJdWCFrvUcHdK9fURlHkLlZR0DN6MmmQ6QZU56+siS3fNKdPIQzsJiK13qQmrrXfkzYx/3JZOYyBmZ5+5JpKg9eleVM4IMJ4Xnih54otGJsDzexXsUQtNzYyKwpW4+97ZyrnAincsKkX3PofOzsvcrMraym65SXKOgkIFfQIPeu0xWwJmqa4elRxXPXsJAw0Zo6rhHVBi1+2CPZRhl2BG6VhWh91gQXZ2jfmTs6rherEu8T4XKlTWvDvBIuz1S+SwqKw/K9l1El1tJ1KshheTAScmZyrenhzvcDRU70tYfh1wyUY8VGhnSKS2S6LFb4+46mohe1eplKYUeDulQjTRWjiTYt0mLGCZ/lP3Jkq7j4SCjYivlR2OjB+kIu959e4Lm7HBD76CoS2tWb2WA1+6FSuSTnjTdogh+kOvseFYa0IT00ynfiDN0OyvwzS2niixLNZtIy3UWvgiIgbzihIUyt6MCqim23TRjObBye5ud0J0CDp9zyV6DyZhgc09smneQaoWP74h0KnLJLRSbog9PvJdbY5UfT8Bahie9qlqFS0hzC86nEMfsAoA8XtaQldoNFz9AE1Nq7G2uIKnYG6dEYE8tQhmXwJdNd+b1HEafmlH41BYtxyyUxPpsGjnprbN6TIlNyhgeff3DJeniXH2e/anSwq50BMo2sE4iTscgrIiIU85DPNCwpw97QzMPp/7Wne2mxLjHhb4fjKLjMi5xeYh16CuOSJab+aoq98cByzUikhH0EkyJgXKPeNWvjlMdJfhEduVFd86YhmAcIMyl6nON07lit6nWqXvqnt9dD4hBX3SW2zpYHIB+mVG4xCVrohM5X6B5MsztusblPqk6L65vaEOvsz5cheP+JCDl2Gt5rdTZLBeGzeCcemvjIGrDjmiJhx2HtwEhiuEmEQ1+rkMUD/HwRnh1VeMnDFlQwRbZQb1gw3QIIFsiDCnvrviYWJcmkVfKlGK5IHUtnUcSgjjXCCc0hcL8DrPygIuW5BWzzoTZ0GrwzERz1FKmyMKH5anRQi3YskoBROXwODYDCL7n3bqYeO5uknuFYP6CJZFnCfxBTjbmzmQiNF0a5uyfZSvklk6nHsR6KK+TDyFHvuAJLuZdkeV1EpEnW5HVvOZEXg8L2gsjiGSf9IWkHlXu0ckCIbdYSdnscWJLtr8XVRM7pmDwz+cV63TE65TLQ0eP85Hgrkf2sW0LE95FgqS9k4lde6/sIQR/3nM1QkhJOCVkisNUEZqgvw9lZAV97o0NH1sSDxzIfpXaKvhktqskpSarHHTpSRWlgok2oZKacHn9gPDMA9622uKxb+GUBN0sDefwSlcYHdF7SJMqm8Y9161zZXz9DCb53OG69deHej82MqZnU1umM8KBVpwh+OCO1KYIqZ2mrsclqLbGmPZDXVMHmE8OMTqX18HTT1KJOfLhPDBYd8aTU8s09RLmWimRXlv5zzVffUmEp9ODm6xNfXUoLuAUynWCjTaWh7K7yFuwLuqBM2e2ddqIK+mwtn27lYyjZ9L7VmX3mkC56Kge8COj7ou4UK8NeYOsyeulzYVb6KrOZOQO48M4thmHl7IQM1QKqT0C0Zgk5WvDQxyfwZl1S+Ir2Z1kT0lg45jo9+vjOJFnIUoFWw2xOyBiUy7DJ8aO41DNzxARhhp+OZ1wZ/IJ7YpTV2WyIrIJt45ih+d1Y5sNQwuIXVecPZPUsU0KMd/qJF7kPEWs1Q2ZNIeE41AVVHkPo70LO5CjEBOlZ667LsHN52OLuZjHAxWgHAQaXW/NDHMtSMz2qO3kViZzhphMnWtMTtYNR70h3NdENeB0y5AoFsZn9kS5ILWbc5a3xwm9TvLVpZSTRKDBWcHtLYJgiuEtF/EmYDe5IlAdeurrQTNDustUvg/YQ6Hj1b07LtPjklmUtD1KlB9FFUfx6wKtuHznQGlG056kPHPEcuJuYwR2H5rWPahsNUzqpi9WcJD94wGR2weD46aiNhz5hCYULk4MqaNUrxjw/ajK3IXJRhGBe4JkLXJKKCHqeCg5446RlOvSjTcv0yjtcl816YklT1ZXCwpQaYgYFHSJKke+E2nRmo+lrxKb6BPI8jzy+TzOs2TVsv6gdYlrVz1wphYcZYbLbmkBqHZJ2igSp1GQvjgtTc8ToMdndtA9ZA2hu/psmG3vq518YhNa1jDcfyScn9EnQghdJThjui2aAztbM45q0GRvyOGYmrFn5qhx2QfI3s7k+13RFYcZ5o0vrhOE3v2WKt0Uz9gQvbq3e3aGNhxTNjUCEZSIgN1DtTjZ/WP/WPzEERkCwvVblcqijVPRo77LWdJdyKLiEoQtjsqt5B8IrZ7KAwhqRDCbik/QtUD0OUBtl8O3gaXG3o/MUBsutzvkeGPHpyK1gHyl5Zayzhab9wixFBtvQmsrTxud+EfkeE7mtjnwT4cRKNARc9SDS2vB3deMuHHGdg8zCHJp+uLyxzYtNDplzZoDzUwSNTfWieYiqFVx0GnaMskyHJzUqfuVF1JM3wyXg+O4EeRF1QK9TEq2KNVii7DmCT/NcLWPBn876yDDjp1dzn7fd03oe2LKWOHMu0W5SGerXcbKYu/79mpvwcOsUfUi1yfnEfaceTvb4zgve9d9WrNuslJ8U8/8ZD9Wx7+StnhVHhV3xsu2s+fA27dURYtasQlBw2B3Yr7EnObKl1UBfax+QVq9XxrPAET9MqXGGA9jQowr2nvBcEWS1sKxxM7mDg5QnJKkDusT9WI/uyOmlPqD4JYgjzMFrvNk7O7M5XBVm6B3ycjhuKv8INPtTFlPpqO3Dndt9KZsXDYyQS8GlKmPA2Edeqm6cXvONrcaKaVYP8hlyvtZ66+w4j40i6mYlCB9rtfSCPJHEmX4rSJ1IYBafd0fD3uK5mlNibpOnwWmjs8do8zyU5Wq9EHJVTGp5+K0nueqZlnRvOGxaQuuc21Db5jKpRYtv7qPiv50eTqE1u5WDaxtLx2OY/sbq7MXE6MqDy7vkrfeh0XARwXodjhX6MGuLrJgs9cuqgMJk5fj/uEIjFApsa5cb+qxtA0bWsyiqntcltrlcds0vBURibwS4+apByc4Da65n6VTrhUYAQrf9uwzdeVK3aKjks1OCm8/Sc/cCAeVu7zUVQDONRrYljSw3Rh4B7Z6Qs/7NNeiMvYVMRFaM97Ik3s9pJsjnLFIQBwSlMP0vF9RszxYGuLQMIIb2F2XFLt2EJ2Ua81/GJc422gGbbK7eJBBIb1Smm+yLs6nN18W4/NelE30cFDQIDkT46y4BkNB+azuR8phMzxsZK2NNYAbYazwqYnwzJ4ZAmW7psZyHAEvkqnVJ3Tx0jRPe6KLvf9c9AG+YXfN2Z9nty8WrTYMdHjkvnHKD1KYHTra9W+auz5NWUnx0EMxKV+gbasDZxnv4lO5PpbtQK39GRQI4Ug09hmPARFM4rWmn/7qZS0/K9FwYyKvJ04Vy92ccrMHCkP7rluJXm+e2BGfcAsBPrxt1jlpfCwSr0aDOcc0A9Zdlah2GgglTr06GqNxuqW8atwblGZPTlmUVQWd3PkkeodBBD23Wd3q5UY/3WxZFEAIy5XyCMFBjxk1qtNaoJdLc9iO6hALccrhzIn3qKeNBA6y8IiIUNs9OrT6OSCeZHBDEp9Z76Erjg0ynnKoPzvE8lD5IF8HTZEOLXGBOA2G5XkdKrKjF8Zp5E5EnuMQXKtpP8F9rRepmBPd8QL2NHqm2046fsmJmSU9tTVYKzl0oBCrsIGzmXwILp7Vnae924Tn0KqOvo1U1qo/bnGqPytPmIYNSZYLtyXnMICIG8p4F/IhRONZtYuSjyJdvyJLbUPOYuCahV01oxOBLsGk+77draoFaOi5PqlNUd/4Mgvr2cCsZSNdN4Ufg++17S1+Ln3Y2854oDMzNMVcSKOg1+8oCDHvlLv1PjzQl/s4tuo9nhZanHDBfp6r47W6g+ZYiO6mr2eCQDyGke/4yr9KV/+UWaEyyNNYjUnXLEnLIIaJBS2qyT0z5nUQ28sVtjS40brF2WtpfQPNz6L1p346qwYcn/hWoi92K3L78WlE8sU53ZlnrpnrcTjKQ5dLh1O8xIcTUcxrj8466KbzTDxn6QIFUOCu6oPooX2aYI2nQmrFnCO0TcuODAbYtknH5fwzbiYAf7i6N6nx2PbtcR6HSUihPWYSy8LExoPtr7ZoNwQkqKwYUZ4Cha7PxhcvRNLwpD48GN9uATfndlUO69ZW1DUlsZt66Dx3PJUifghOgng0RHd/6GbuvnaO7+21ce1p6qDeluWcnWoRY/zxwmIh6fYi0zBzsPgFF+F1/aTUPluEfqvdMnxeZoWzSrea5/q5r1WpNVo1prmtOo1H5T5OBoxrTwyTYDdHTvfFKXtRh6DonFwHSVkbpRsm0Bj4BTSjw0wiWrMsfFtke9G38cdJmJ9Cj3v+DVW5NMuJ4T5XAbaUaStud4/rVZYuVCekAa3TU4LQ8DU7h65rXq/OKbqfiwI6h/R2sB7yqLMPnfC1p201R3g9x4OmJY2xarLkHUcCQIjXO8ojDt3oCJYmZDSI02X2wwGPBlQtkdJPUsVvTorWtg9dKYhsLyyG6Qd3Nj2FDgHx6dmEnIzQi8oqwspQ73ulsvA8yx5kb428FWlElz+wFE7C03Fr08OkT/Fda+45zk3SyGv3gMdi1OxxbBLOqFxJm3i5JM9DeCpxskOVQYdnc4muE5NBj55UqxpNlmQQYk8QyYYewsPcQYeuoCwtv7AJo1C36/YIxdAa9TKoj9kwDwPAP6rxNwzRLOR8kvhz4OtCPqCz5Y3z5CX+HjsVRFpjWCxFF1QlLmaSUZQ7EG2ZZ/aGdelzkg1/lM81KOus4ox1cO4LCJmOiKdIK0nXPXUuzhJq+hmMjraE7/fSyUr0GrVOFFIAnGhbz5sejjc3oCYtiYejrUd6rIeh7gaAWcCkyAuhy1wsw3XTNaOXmBPFyLUQnPiCoVHzYlqOqNjy8qRPCt2F2L5d5mlIVAl5BBoR9dduNWi84bQrhzi3JYcRxjGei+R5A9CpFUT0KC7sKcajRU8D1gfl61FceaSNeCl0U8rmsv2Yy8B8JI9DumIb8VUiiPV65bchQzunHKfugpznDXuAinWyTubpwhTOQfDXPo0zccFUWnIzmI5GzrBMTjwjY+0TmXTvT9oFWs7KBfGRJ+X3HTbXenLpk/EGp8IJpPO91LzBG/IzNrV7wrevwnBZzhfs6tnHAx6fe05OofCwVBdt4DUXcUb0yGfGIztnZ3dvm1g22c5wvVCWL6QHfXpwxV0D3tR8z5YvpVQfvFY6H3quz/ysxKsVEM7TUz6qHue3HEHmoBnMs+iKmfvLXkP1hbUnURaq9pRBR8mdgqzr0ZxTWpLoe/rk4El+KTa66WWuPGFlm+5Xjs9j5KlNyWnOhvBuCNHJbapVbpBucgQ1Se9ZcHUiw9I5gsI6Q72aDNk7znWIbnkTE+dBVGgBqy/wSd9SfMZPR5kvYfc4d9zpccgbGL/41/vwyDS42GvBw3iiAb5fAFZ3Zmf4x5wB3KkwyWDqGWYVj7Bv39B76nm3QMVpbR2kZy2hl/Q0IE/Q+A91yMS+fIJqLVD5W66nKbRQmdnEw2Y/8/LolzeKvp0whgd8FrD1NNE9k+JL6HoaOlAiLwh6GtjHAyUV1mtmjx/2DVkTXYTfpmyRTcO22FNlEdvpWFaASwwMQ81Fb0o+A3FmXFIBQR2TehKxPfYEfZCmcqXc9FvBFyYeYu2FDPwx22M1apevO1zbeiePjzkyXYOCa53S8MmC7roz3CMsPBLEIY/bHs8kermG8+VwCk5bQsdROx4vB1AGkti06hMVhBTpsjR5ryhNTLoYEFdiM01Vi4Pw4svp2iCw6VdmVKlZV0nZvqqqsjqOwcYiBkXAJnbvDldvc3n31IcCfr09DtdEk3rKcbGDUXJLfnLvlocXjZkkiOuE/eUaRAeOLGLfKg5S3Iuykw57ROpSWzj4VSs6C6JvvqTF91PdtawMPx9DPy6Dt/gSwXarU9ID23Pl7FxjvH6ePGkal64hHluudlYgelQ60UgCWkGcaFgyhfNKrCCYpgIIFQ3dOdFJNhpoDKWZSLuyulSZCOmWciCcXrt2soJigjTsta4nDZMARQIVadaQ0DtMazeZX7e1WDr54D6kwuYFlqXdlY8E3rmQaCQsEFrb+4vOtgeqLABPPeULfoG7Zzv0YuHl0hjAql81bZefyzPxnOFEGGoJtll5PbuHSZuCO48RInp3Oc7aN1NR0fCUJIHVQsK9hTGfoZdCxpthWfGZWGkRT5IexgZ/mALczSG2byBrgT156QnL0jeV3i9X5rwMGQ13/ewlHnos0+udOi38cMdaVJbZ8fJc2+A8O0frOuarIGHuzSfl1zXZv/3t06+fXrf3P251/5vXQl/3cf9/uxb8foO3u79eJkqy1zXoMYvS3972+u3fbf5fv34akwps/X7DeaqX4vuV4H93v/nz2/3mz3P3ORmbz3+43/z+pti314s92WP+fpt9jorXe+Wf/jD19R7C63/fXwX850vgn8Gur1vh3+99AwXfXul9u5CNfsGAmv/43yKsZeJlPwAA -->
