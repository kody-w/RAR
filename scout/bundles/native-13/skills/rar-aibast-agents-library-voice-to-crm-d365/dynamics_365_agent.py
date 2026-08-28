"""
Voice to CRM Dynamics 365 Agent — a template you are meant to mutate.

Captures voice recordings, extracts entities, previews D365 record
updates, and tracks synchronization status. Update previews are
pre-flight validated against a REAL Dynamics org: the agent checks
whether the accounts and contacts named in the voice note actually
exist before you apply anything.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live accounts and contacts over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="record_update", voice_id="VOC-001")
     — the preview is checked against the tenant's real 22-account
     roster and reports whether each target record exists.
  2. No network? Everything falls back to the embedded demo layer below
     (_VOICE_TRANSCRIPTS / _UPDATE_TEMPLATES) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     VOICE_TO_CRM_D365_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org), or replace _fetch_collection() with your Dataverse
     client. The fields the rest of the file needs are listed in
     _normalize_live_org(). The speech capture itself is an enrichment
     seam — wire Azure AI Speech where the embedded transcripts sit.

OPERATIONS
  voice_capture | entity_extraction | record_update | sync_status
  kwargs: operation (required), voice_id
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
    "name": "@aibast-agents-library/voice_to_crm_d365",
    "version": "1.1.0",
    "display_name": "Voice to CRM (D365)",
    "description": "Previews voice-driven Dynamics 365 updates pre-flight checked against a live simulated tenant, with sync status and offline fallback.",
    "author": "AIBAST",
    "tags": ["voice", "d365", "crm", "speech", "entity-extraction", "sync"],
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
#   export VOICE_TO_CRM_D365_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your Dataverse client.
# Downstream code only needs the fields produced by
# _normalize_live_org().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "VOICE_TO_CRM_D365_DATA_URL",
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


def _normalize_live_org():
    """Project the connected Dynamics org onto the validation shape
    this agent uses. THIS is the contract your replacement data source
    must meet — a dict with account names, contact names, and record
    counts. Returns {} when offline."""
    accounts = _fetch_collection("accounts")
    if not accounts:
        return {}
    contacts = _fetch_collection("contacts")
    opportunities = _fetch_collection("opportunities")
    return {
        "org_label": "Aster Lane Office Systems (live tenant)",
        "account_names": {a.get("name", "") for a in accounts if a.get("name")},
        "contact_names": {c.get("fullname", "") for c in contacts if c.get("fullname")},
        "counts": {
            "accounts": len(accounts),
            "contacts": len(contacts),
            "opportunities": len(opportunities),
        },
    }


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_VOICE_TRANSCRIPTS = {
    "VOC-001": {
        "id": "VOC-001", "date": "2025-11-14", "duration_sec": 245, "speaker": "Alex Rivera",
        "raw_text": "Just finished a call with Jennifer Walsh at TechVantage Solutions. She confirmed they have budget approval for two hundred thousand dollars. The CEO Mark Davidson wants our proposal by December fifteenth. We need to include Sam Patel their IT director in the next meeting. Set the opportunity stage to proposal and schedule a review meeting for December twelfth.",
        "confidence": 0.94,
    },
    "VOC-002": {
        "id": "VOC-002", "date": "2025-11-14", "duration_sec": 180, "speaker": "Sarah Kim",
        "raw_text": "Quick update on the Greenridge Partners deal. David Park confirmed they want to renew for another year. Amount stays at seventy two thousand. They also want to add analytics standard for an additional twelve thousand per year. Update the opportunity to negotiation stage with a close date of January tenth.",
        "confidence": 0.96,
    },
}

_D365_ENTITY_MAPPINGS = {
    "opportunity": {
        "entity_name": "opportunity",
        "fields": [
            {"voice_pattern": "opportunity stage", "d365_field": "stepname", "type": "String"},
            {"voice_pattern": "amount|budget|price", "d365_field": "estimatedvalue", "type": "Money"},
            {"voice_pattern": "close date|deadline", "d365_field": "estimatedclosedate", "type": "DateTime"},
            {"voice_pattern": "probability|confidence", "d365_field": "closeprobability", "type": "Integer"},
        ],
    },
    "contact": {
        "entity_name": "contact",
        "fields": [
            {"voice_pattern": "name|person", "d365_field": "fullname", "type": "String"},
            {"voice_pattern": "title|role|position", "d365_field": "jobtitle", "type": "String"},
            {"voice_pattern": "email", "d365_field": "emailaddress1", "type": "String"},
            {"voice_pattern": "phone|number", "d365_field": "telephone1", "type": "String"},
        ],
    },
    "phonecall": {
        "entity_name": "phonecall",
        "fields": [
            {"voice_pattern": "subject|topic", "d365_field": "subject", "type": "String"},
            {"voice_pattern": "description|notes", "d365_field": "description", "type": "String"},
            {"voice_pattern": "duration", "d365_field": "actualdurationminutes", "type": "Integer"},
        ],
    },
}

_UPDATE_TEMPLATES = {
    "VOC-001": {
        "target_account": "TechVantage Solutions",
        "opportunity_update": {"name": "TechVantage Solutions - Enterprise Platform", "stepname": "Proposal", "estimatedvalue": 200000, "estimatedclosedate": "2025-12-15", "closeprobability": 65},
        "activity_log": {"subject": "Discovery follow-up call with Jennifer Walsh", "description": "Budget confirmed at $200K. CEO wants proposal by Dec 15. Include IT Director Sam Patel in next meeting.", "actualdurationminutes": 4},
        "new_contacts": [{"fullname": "Mark Davidson", "jobtitle": "CEO", "account": "TechVantage Solutions"}, {"fullname": "Sam Patel", "jobtitle": "IT Director", "account": "TechVantage Solutions"}],
    },
    "VOC-002": {
        "target_account": "Greenridge Partners",
        "opportunity_update": {"name": "Greenridge Partners - Renewal + Expansion", "stepname": "Negotiation", "estimatedvalue": 84000, "estimatedclosedate": "2026-01-10", "closeprobability": 80},
        "activity_log": {"subject": "Renewal discussion with David Park", "description": "Renewal confirmed at $72K. Adding Analytics Standard at $12K/yr. Total new amount: $84K.", "actualdurationminutes": 3},
        "new_contacts": [],
    },
}

_SYNC_STATUS = [
    {"id": "SYNC-001", "voice_id": "VOC-001", "entity": "opportunity", "status": "Pending", "d365_record_id": "opp-a1b2c3", "timestamp": "2025-11-14T14:30:00Z", "attempts": 0, "error": None},
    {"id": "SYNC-002", "voice_id": "VOC-001", "entity": "phonecall", "status": "Synced", "d365_record_id": "act-d4e5f6", "timestamp": "2025-11-14T14:30:05Z", "attempts": 1, "error": None},
    {"id": "SYNC-003", "voice_id": "VOC-001", "entity": "contact", "status": "Synced", "d365_record_id": "con-g7h8i9", "timestamp": "2025-11-14T14:30:10Z", "attempts": 1, "error": None},
    {"id": "SYNC-004", "voice_id": "VOC-002", "entity": "opportunity", "status": "Failed", "d365_record_id": "opp-j1k2l3", "timestamp": "2025-11-14T15:00:00Z", "attempts": 3, "error": "Record locked by another user"},
    {"id": "SYNC-005", "voice_id": "VOC-002", "entity": "phonecall", "status": "Synced", "d365_record_id": "act-m4n5o6", "timestamp": "2025-11-14T15:00:05Z", "attempts": 1, "error": None},
]


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_voice_id(query):
    if not query:
        return "VOC-001"
    q = query.upper().strip()
    for key in _VOICE_TRANSCRIPTS:
        if key in q:
            return key
    return "VOC-001"


def _sync_summary():
    total = len(_SYNC_STATUS)
    synced = sum(1 for s in _SYNC_STATUS if s["status"] == "Synced")
    pending = sum(1 for s in _SYNC_STATUS if s["status"] == "Pending")
    failed = sum(1 for s in _SYNC_STATUS if s["status"] == "Failed")
    return total, synced, pending, failed


def _preflight_lines(update, org):
    """Real existence checks of the update's targets against the live
    org. Returns human-readable check lines."""
    if not org:
        return ["Live org unreachable — existence checks skipped (offline fallback)."]
    lines = []
    account = update.get("target_account", "")
    if account:
        if account in org["account_names"]:
            lines.append(f"Account \"{account}\": EXISTS in {org['org_label']} — update would attach to it.")
        else:
            lines.append(f"Account \"{account}\": NOT FOUND among {org['counts']['accounts']} accounts in {org['org_label']} — applying would create a new account.")
    for c in update.get("new_contacts", []):
        if c["fullname"] in org["contact_names"]:
            lines.append(f"Contact \"{c['fullname']}\": already exists — would update, not create.")
        else:
            lines.append(f"Contact \"{c['fullname']}\": not found among {org['counts']['contacts']} contacts — would be created.")
    return lines


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class VoiceToCRMD365Agent(BasicAgent):
    """
    Voice-to-CRM agent for Dynamics 365.

    Operations:
        voice_capture       - capture and transcribe voice input
        entity_extraction   - extract D365 entities from transcript
        record_update       - preview D365 record updates
        sync_status         - check synchronization status
    """

    def __init__(self):
        self.name = "VoiceToCRMD365Agent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "voice_capture", "entity_extraction",
                            "record_update", "sync_status",
                        ],
                        "description": "The voice-to-CRM operation to perform",
                    },
                    "voice_id": {
                        "type": "string",
                        "description": "Voice recording ID (e.g. 'VOC-001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "voice_capture")
        voice_id = _resolve_voice_id(kwargs.get("voice_id", ""))
        dispatch = {
            "voice_capture": self._voice_capture,
            "entity_extraction": self._entity_extraction,
            "record_update": self._record_update,
            "sync_status": self._sync_status,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(voice_id)

    def _voice_capture(self, voice_id):
        voc = _VOICE_TRANSCRIPTS[voice_id]
        return (
            f"**Voice Capture: {voc['id']}** (embedded demo recording — the "
            f"speech engine is an enrichment seam)\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Date | {voc['date']} |\n"
            f"| Speaker | {voc['speaker']} |\n"
            f"| Duration | {voc['duration_sec']}s |\n"
            f"| Confidence | {voc['confidence']:.0%} |\n\n"
            f"**Transcript:**\n\n\"{voc['raw_text']}\"\n\n"
            f"Source: [Voice Capture + Speech-to-Text]\nAgents: VoiceToCRMD365Agent"
        )

    def _entity_extraction(self, voice_id):
        mapping_rows = ""
        for entity, config in _D365_ENTITY_MAPPINGS.items():
            for field in config["fields"]:
                mapping_rows += f"| {entity} | {field['voice_pattern']} | {field['d365_field']} | {field['type']} |\n"
        update = _UPDATE_TEMPLATES.get(voice_id, {})
        opp = update.get("opportunity_update", {})
        extracted = "\n".join(f"- {k}: {v}" for k, v in opp.items()) if opp else "No entities extracted"
        return (
            f"**Entity Extraction: {voice_id}** (embedded demo transcript — simulated)\n\n"
            f"**Extracted Values:**\n{extracted}\n\n"
            f"**D365 Entity Mapping Rules:**\n\n"
            f"| Entity | Voice Pattern | D365 Field | Type |\n|---|---|---|---|\n"
            f"{mapping_rows}\n\n"
            f"Source: [NLP Extraction Engine + D365 Schema]\nAgents: VoiceToCRMD365Agent"
        )

    def _record_update(self, voice_id):
        update = _UPDATE_TEMPLATES.get(voice_id, {})
        opp = update.get("opportunity_update", {})
        activity = update.get("activity_log", {})
        new_contacts = update.get("new_contacts", [])
        opp_lines = "\n".join(f"- {k}: {v}" for k, v in opp.items())
        act_lines = "\n".join(f"- {k}: {v}" for k, v in activity.items())
        contact_lines = "\n".join(f"- {c['fullname']} ({c['jobtitle']}) at {c['account']}" for c in new_contacts) or "None"
        org = _normalize_live_org()
        preflight = "\n".join(f"- {line}" for line in _preflight_lines(update, org))
        return (
            f"**D365 Record Update Preview: {voice_id}**\n\n"
            f"**1. Opportunity Update:**\n{opp_lines}\n\n"
            f"**2. Activity Log:**\n{act_lines}\n\n"
            f"**3. New Contacts:**\n{contact_lines}\n\n"
            f"**Pre-flight validation (checked against the live org):**\n{preflight}\n\n"
            f"**Status:** Preview only — no record was written | Requires confirmation\n\n"
            f"Source: [D365 Update Engine + Live Dynamics 365 Tenant]\nAgents: VoiceToCRMD365Agent"
        )

    def _sync_status(self, voice_id):
        total, synced, pending, failed = _sync_summary()
        rows = ""
        for s in _SYNC_STATUS:
            error = s["error"] or "-"
            rows += f"| {s['id']} | {s['voice_id']} | {s['entity']} | {s['status']} | {s['attempts']} | {error[:30]} |\n"
        org = _normalize_live_org()
        if org:
            org_line = (
                f"**Target org connectivity (checked now over HTTP):** {org['org_label']} reachable — "
                f"{org['counts']['accounts']} accounts, {org['counts']['contacts']} contacts, "
                f"{org['counts']['opportunities']} opportunities.\n\n"
            )
        else:
            org_line = "**Target org connectivity (checked now over HTTP):** unreachable — sync would queue locally.\n\n"
        return (
            f"**Sync Status Dashboard** (sync ledger is embedded demo data — simulated)\n\n"
            f"| Metric | Count |\n|---|---|\n"
            f"| Total Syncs | {total} |\n"
            f"| Synced | {synced} |\n"
            f"| Pending | {pending} |\n"
            f"| Failed | {failed} |\n\n"
            f"{org_line}"
            f"**Detail:**\n\n"
            f"| ID | Voice | Entity | Status | Attempts | Error |\n|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Action Required:** SYNC-004 failed after 3 attempts (record locked). Manual retry recommended.\n\n"
            f"Source: [D365 Sync Engine + Live Dynamics 365 Tenant]\nAgents: VoiceToCRMD365Agent"
        )


if __name__ == "__main__":
    agent = VoiceToCRMD365Agent()
    print("=" * 60)
    print("EMBEDDED DEMO RECORDING (works offline)")
    print(agent.perform(operation="voice_capture", voice_id="VOC-001"))
    print()
    print("=" * 60)
    print("LIVE PRE-FLIGHT VALIDATION (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="record_update", voice_id="VOC-001"))
    print()
    print("=" * 60)
    print(agent.perform(operation="sync_status", voice_id="VOC-001"))
