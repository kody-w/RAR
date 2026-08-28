---
name: "rar-aibast-agents-library-voice-to-crm-d365"
description: "Previews voice-driven Dynamics 365 updates pre-flight checked against a live simulated tenant, with sync status and offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/voice_to_crm_d365", "rar_sha256": "3a680551c0a075d834a73e2940d47ea69d7e9c6be7035f8c32864bc541c76ee9", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["voice", "d365", "crm", "speech", "entity-extraction", "sync"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/voice_to_crm_d365`. The original RAPP
agent is preserved byte-for-byte in `dynamics_365_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The voice-to-CRM operation to perform",
      "enum": [
        "voice_capture",
        "entity_extraction",
        "record_update",
        "sync_status"
      ],
      "type": "string"
    },
    "voice_id": {
      "description": "Voice recording ID (e.g. 'VOC-001')",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dynamics_365_agent.py` and embedded as the fenced Python below (sha256 3a680551c0a075d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dynamics_365_agent.py` first:

```bash
python3 dynamics_365_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dynamics_365_agent.py   # or on stdin
python3 dynamics_365_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
