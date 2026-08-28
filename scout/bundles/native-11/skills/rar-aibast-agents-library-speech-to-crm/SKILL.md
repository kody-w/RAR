---
name: "rar-aibast-agents-library-speech-to-crm"
description: "Maps call transcripts to CRM fields grounded against live records in a simulated Dynamics 365 tenant, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/speech_to_crm", "rar_sha256": "6109a47956495120a36efec146400544f2ca20f7f857da1963d378f8dfcbbb6a", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["speech", "transcription", "crm", "entity-extraction", "nlp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/speech_to_crm`. The original RAPP
agent is preserved byte-for-byte in `speech_to_crm_agent.py` and in the RCI capsule.

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

Speech to CRM Agent — a template you are meant to mutate.

Transcribes sales calls, extracts entities, maps them to CRM fields,
and generates update previews. The field mapping and update preview are
grounded against a REAL CRM org: mapped target fields are shown next to
live example values from actual tenant records, and proposed updates
are pre-flight checked against the org's account roster.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live opportunities, accounts, and contacts
     over real HTTP from the globally hosted Static Dynamics 365 tenant
     (Aster Lane Office Systems — synthetic data, no credentials,
     works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="crm_mapping")
     — every mapped Dynamics field is shown with a live example value
     from a real tenant record (e.g. estimatedvalue from "Marigold
     Field Services — Mobile workstation expansion").
  2. No network? Everything falls back to the embedded demo layer below
     (_CALL_TRANSCRIPTS / _CRM_FIELD_MAPPINGS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SPEECH_TO_CRM_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org), or replace _fetch_collection() with your CRM
     client. The fields the rest of the file needs are listed in
     _normalize_live_examples(). The speech-to-text engine itself is an
     enrichment seam — wire Azure AI Speech or your recorder where the
     embedded transcript sits.

OPERATIONS
  transcribe_call | extract_entities | crm_mapping | update_preview
  kwargs: operation (required), call_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "call_id": {
      "description": "Call ID (e.g. 'CALL-T001')",
      "type": "string"
    },
    "operation": {
      "description": "The speech-to-CRM operation to perform",
      "enum": [
        "transcribe_call",
        "extract_entities",
        "crm_mapping",
        "update_preview"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `speech_to_crm_agent.py` and embedded as the fenced Python below (sha256 6109a47956495120…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `speech_to_crm_agent.py` first:

```bash
python3 speech_to_crm_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 speech_to_crm_agent.py   # or on stdin
python3 speech_to_crm_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Speech to CRM Agent — a template you are meant to mutate.

Transcribes sales calls, extracts entities, maps them to CRM fields,
and generates update previews. The field mapping and update preview are
grounded against a REAL CRM org: mapped target fields are shown next to
live example values from actual tenant records, and proposed updates
are pre-flight checked against the org's account roster.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live opportunities, accounts, and contacts
     over real HTTP from the globally hosted Static Dynamics 365 tenant
     (Aster Lane Office Systems — synthetic data, no credentials,
     works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="crm_mapping")
     — every mapped Dynamics field is shown with a live example value
     from a real tenant record (e.g. estimatedvalue from "Marigold
     Field Services — Mobile workstation expansion").
  2. No network? Everything falls back to the embedded demo layer below
     (_CALL_TRANSCRIPTS / _CRM_FIELD_MAPPINGS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SPEECH_TO_CRM_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org), or replace _fetch_collection() with your CRM
     client. The fields the rest of the file needs are listed in
     _normalize_live_examples(). The speech-to-text engine itself is an
     enrichment seam — wire Azure AI Speech or your recorder where the
     embedded transcript sits.

OPERATIONS
  transcribe_call | extract_entities | crm_mapping | update_preview
  kwargs: operation (required), call_id
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
    "name": "@aibast-agents-library/speech_to_crm",
    "version": "1.1.0",
    "display_name": "Speech to CRM",
    "description": "Maps call transcripts to CRM fields grounded against live records in a simulated Dynamics 365 tenant, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["speech", "transcription", "crm", "entity-extraction", "nlp"],
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
#   export SPEECH_TO_CRM_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_examples().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "SPEECH_TO_CRM_DATA_URL",
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


def _normalize_live_examples():
    """Project live tenant records onto the grounding shape this agent
    uses. THIS is the contract your replacement data source must meet —
    a dict with an example open opportunity, an example contact, and
    the account-name roster. Returns {} when offline."""
    opportunities = _fetch_collection("opportunities")
    contacts = _fetch_collection("contacts")
    accounts = _fetch_collection("accounts")
    if not (opportunities and contacts and accounts):
        return {}
    open_opps = [o for o in opportunities if o.get("statecode") == 0] or opportunities
    opp = open_opps[0]
    contact = contacts[0]
    return {
        "opportunity": {
            "name": opp.get("name", ""),
            "estimatedvalue": opp.get("estimatedvalue"),
            "estimatedclosedate": str(opp.get("estimatedclosedate", ""))[:10],
            "closeprobability": opp.get("closeprobability"),
            "customeridname": opp.get("customeridname", ""),
        },
        "contact": {
            "fullname": contact.get("fullname", ""),
            "jobtitle": contact.get("jobtitle", ""),
            "parentcustomeridname": contact.get("parentcustomeridname", ""),
            "emailaddress1": contact.get("emailaddress1", ""),
        },
        "account_names": {a.get("name", "") for a in accounts if a.get("name")},
    }


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_CALL_TRANSCRIPTS = {
    "CALL-T001": {
        "id": "CALL-T001", "duration_sec": 1847, "date": "2025-11-14",
        "participants": ["Alex Rivera (Sales)", "Jennifer Walsh (TechVantage Solutions)"],
        "transcript_segments": [
            {"speaker": "Alex Rivera", "timestamp": "00:00:15", "text": "Hi Jennifer, thanks for making time today. I wanted to follow up on our demo last Tuesday."},
            {"speaker": "Jennifer Walsh", "timestamp": "00:00:28", "text": "Hi Alex, yes absolutely. We really liked what we saw, especially the analytics dashboard. Our team has been struggling with reporting."},
            {"speaker": "Alex Rivera", "timestamp": "00:00:45", "text": "That's great to hear. Can you tell me more about the reporting challenges? How many people are affected?"},
            {"speaker": "Jennifer Walsh", "timestamp": "00:01:02", "text": "About 150 people across our operations and finance teams. We spend roughly 20 hours a week manually compiling reports from three different systems."},
            {"speaker": "Alex Rivera", "timestamp": "00:01:25", "text": "That's significant. At your team's average cost, that's roughly $50,000 a year in labor just on reporting. Our platform could automate about 80% of that."},
            {"speaker": "Jennifer Walsh", "timestamp": "00:01:48", "text": "That ROI is compelling. We have budget approval for up to $200,000 for this initiative. Our CEO, Mark Davidson, wants to see a formal proposal by December 15th."},
            {"speaker": "Alex Rivera", "timestamp": "00:02:15", "text": "Perfect. I'll have a proposal ready by December 10th. Should we schedule a review meeting with your team for December 12th?"},
            {"speaker": "Jennifer Walsh", "timestamp": "00:02:30", "text": "That works. Include our IT Director, Sam Patel, in that meeting. He'll need to evaluate the technical integration with our SAP system."},
        ],
        "confidence_score": 0.96,
    },
}

_ENTITY_EXTRACTION_RULES = {
    "person": {"pattern": "Named individuals mentioned", "examples": ["Jennifer Walsh", "Mark Davidson", "Sam Patel"]},
    "organization": {"pattern": "Company or department names", "examples": ["TechVantage Solutions", "Operations", "Finance"]},
    "money": {"pattern": "Dollar amounts or budget references", "examples": ["$200,000", "$50,000"]},
    "date": {"pattern": "Dates and deadlines", "examples": ["December 15th", "December 10th", "December 12th"]},
    "product": {"pattern": "Product or feature mentions", "examples": ["analytics dashboard", "reporting", "platform"]},
    "pain_point": {"pattern": "Challenges or problems described", "examples": ["manually compiling reports", "three different systems", "20 hours a week"]},
    "action_item": {"pattern": "Commitments or next steps", "examples": ["formal proposal", "review meeting", "evaluate technical integration"]},
    "competitor": {"pattern": "Competitor or alternative mentions", "examples": ["SAP"]},
}

_CRM_FIELD_MAPPINGS = {
    "opportunity": {
        "name": {"source": "organization + context", "mapped_value": "TechVantage Solutions - Enterprise Platform", "d365_field": "name"},
        "amount": {"source": "money entity", "mapped_value": 200000, "d365_field": "estimatedvalue"},
        "close_date": {"source": "date entity", "mapped_value": "2025-12-15", "d365_field": "estimatedclosedate"},
        "stage": {"source": "conversation context", "mapped_value": "Proposal", "d365_field": "stepname"},
        "probability": {"source": "engagement signals", "mapped_value": 65, "d365_field": "closeprobability"},
        "next_step": {"source": "action_item entity", "mapped_value": "Send proposal by Dec 10, review meeting Dec 12", "d365_field": "description"},
    },
    "contact": {
        "name": {"source": "person entity", "mapped_value": "Jennifer Walsh", "d365_field": "fullname"},
        "title": {"source": "inferred from context", "mapped_value": "VP of Operations", "d365_field": "jobtitle"},
        "account": {"source": "organization entity", "mapped_value": "TechVantage Solutions", "d365_field": "parentcustomerid"},
    },
    "activity": {
        "type": {"source": "call metadata", "mapped_value": "Phone Call"},
        "subject": {"source": "conversation summary", "mapped_value": "Discovery follow-up - proposal requested"},
        "description": {"source": "full transcript", "mapped_value": "Discussed reporting challenges, 150 users affected. Budget approved up to $200K. CEO Mark Davidson wants proposal by Dec 15. Technical review with IT Director Sam Patel needed."},
        "duration_min": {"source": "call metadata", "mapped_value": 31},
    },
    "new_contacts": [
        {"name": "Mark Davidson", "title": "CEO", "role": "Economic Buyer", "account": "TechVantage Solutions"},
        {"name": "Sam Patel", "title": "IT Director", "role": "Technical Evaluator", "account": "TechVantage Solutions"},
    ],
}

_EXTRACTED_ENTITIES = [
    {"type": "person", "value": "Jennifer Walsh", "confidence": 0.99, "context": "Primary contact, VP Operations"},
    {"type": "person", "value": "Mark Davidson", "confidence": 0.97, "context": "CEO, economic buyer, wants proposal by Dec 15"},
    {"type": "person", "value": "Sam Patel", "confidence": 0.98, "context": "IT Director, technical evaluator"},
    {"type": "organization", "value": "TechVantage Solutions", "confidence": 0.99, "context": "Prospect account"},
    {"type": "money", "value": "$200,000", "confidence": 0.98, "context": "Approved budget for initiative"},
    {"type": "money", "value": "$50,000", "confidence": 0.95, "context": "Annual cost of manual reporting"},
    {"type": "date", "value": "December 15", "confidence": 0.97, "context": "CEO deadline for proposal"},
    {"type": "date", "value": "December 12", "confidence": 0.96, "context": "Proposed review meeting date"},
    {"type": "pain_point", "value": "20 hours/week manual reporting", "confidence": 0.94, "context": "150 people affected across ops and finance"},
    {"type": "action_item", "value": "Send proposal by Dec 10", "confidence": 0.97, "context": "Alex committed to deliver proposal"},
    {"type": "action_item", "value": "Schedule Dec 12 review meeting", "confidence": 0.95, "context": "Include Sam Patel for technical evaluation"},
]


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _format_transcript(call_id):
    call = _CALL_TRANSCRIPTS.get(call_id)
    if not call:
        return "Transcript not found."
    lines = []
    for seg in call["transcript_segments"]:
        lines.append(f"[{seg['timestamp']}] **{seg['speaker']}:** {seg['text']}")
    return "\n\n".join(lines)


def _entity_summary():
    by_type = {}
    for e in _EXTRACTED_ENTITIES:
        by_type.setdefault(e["type"], []).append(e)
    return by_type


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class SpeechToCRMAgent(BasicAgent):
    """
    Speech-to-CRM pipeline agent.

    Operations:
        transcribe_call   - transcribe and display call recording
        extract_entities  - extract named entities from transcript
        crm_mapping       - map extracted entities to CRM fields
        update_preview    - preview CRM record updates before applying
    """

    def __init__(self):
        self.name = "SpeechToCRMAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "transcribe_call", "extract_entities",
                            "crm_mapping", "update_preview",
                        ],
                        "description": "The speech-to-CRM operation to perform",
                    },
                    "call_id": {
                        "type": "string",
                        "description": "Call ID (e.g. 'CALL-T001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "transcribe_call")
        call_id = kwargs.get("call_id", "CALL-T001")
        dispatch = {
            "transcribe_call": self._transcribe_call,
            "extract_entities": self._extract_entities,
            "crm_mapping": self._crm_mapping,
            "update_preview": self._update_preview,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(call_id)

    def _transcribe_call(self, call_id):
        call = _CALL_TRANSCRIPTS.get(call_id, list(_CALL_TRANSCRIPTS.values())[0])
        transcript = _format_transcript(call["id"])
        return (
            f"**Call Transcription: {call['id']}** (embedded demo transcript — "
            f"the speech-to-text engine is an enrichment seam)\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Date | {call['date']} |\n"
            f"| Duration | {call['duration_sec'] // 60}m {call['duration_sec'] % 60}s |\n"
            f"| Participants | {', '.join(call['participants'])} |\n"
            f"| Confidence | {call['confidence_score']:.0%} |\n\n"
            f"**Transcript:**\n\n{transcript}\n\n"
            f"Source: [Speech-to-Text Engine]\nAgents: SpeechToCRMAgent"
        )

    def _extract_entities(self, call_id):
        entity_rows = ""
        for e in _EXTRACTED_ENTITIES:
            entity_rows += f"| {e['type'].title()} | {e['value']} | {e['confidence']:.0%} | {e['context'][:45]} |\n"
        by_type = _entity_summary()
        summary = "\n".join(f"- {t.title()}: {len(entities)}" for t, entities in by_type.items())
        return (
            f"**Entity Extraction Results** (embedded demo transcript — simulated)\n\n"
            f"| Type | Value | Confidence | Context |\n|---|---|---|---|\n"
            f"{entity_rows}\n"
            f"**Summary by Type:**\n{summary}\n\n"
            f"**Total Entities:** {len(_EXTRACTED_ENTITIES)}\n\n"
            f"Source: [NLP Entity Extraction Engine]\nAgents: SpeechToCRMAgent"
        )

    def _crm_mapping(self, call_id):
        live = _normalize_live_examples()
        live_opp = live.get("opportunity", {})
        live_contact = live.get("contact", {})
        opp = _CRM_FIELD_MAPPINGS["opportunity"]
        contact = _CRM_FIELD_MAPPINGS["contact"]

        def live_example(d365_field, record, label_field=None):
            if not record:
                return "live tenant unreachable"
            value = record.get(d365_field, "")
            return f"{value}" if value not in ("", None) else "n/a"

        opp_rows = "\n".join(
            f"| {field} | {info['source']} | {info['mapped_value']} | "
            f"`{info.get('d365_field', 'n/a')}` | {live_example(info.get('d365_field', ''), live_opp)} |"
            for field, info in opp.items()
        )
        contact_rows = "\n".join(
            f"| {field} | {info['source']} | {info['mapped_value']} | "
            f"`{info.get('d365_field', 'n/a')}` | {live_example(info.get('d365_field', ''), live_contact)} |"
            for field, info in contact.items()
        )
        new_contacts = _CRM_FIELD_MAPPINGS["new_contacts"]
        new_rows = "\n".join(f"| {c['name']} | {c['title']} | {c['role']} |" for c in new_contacts)
        if live:
            grounding = (
                f"Live example values come from real tenant records: opportunity "
                f"\"{live_opp.get('name', '')}\" and contact "
                f"\"{live_contact.get('fullname', '')}\" (LIVE Dynamics 365 tenant).\n"
            )
        else:
            grounding = "Live tenant unreachable — target fields shown without live example values.\n"
        return (
            f"**CRM Field Mapping** (extracted values are from the embedded demo call)\n\n"
            f"**Opportunity Update:**\n\n"
            f"| Field | Source | Mapped Value | D365 Field | Live Example Value |\n|---|---|---|---|---|\n"
            f"{opp_rows}\n\n"
            f"**Contact Update:**\n\n"
            f"| Field | Source | Mapped Value | D365 Field | Live Example Value |\n|---|---|---|---|---|\n"
            f"{contact_rows}\n\n"
            f"**New Contacts to Create:**\n\n"
            f"| Name | Title | Role |\n|---|---|---|\n"
            f"{new_rows}\n\n"
            f"{grounding}"
            f"Source: [CRM Mapping Engine + Live Dynamics 365 Tenant]\nAgents: SpeechToCRMAgent"
        )

    def _update_preview(self, call_id):
        opp = _CRM_FIELD_MAPPINGS["opportunity"]
        activity = _CRM_FIELD_MAPPINGS["activity"]
        new_contacts = _CRM_FIELD_MAPPINGS["new_contacts"]
        live = _normalize_live_examples()
        target_account = _CRM_FIELD_MAPPINGS["contact"]["account"]["mapped_value"]
        if live:
            exists = target_account in live["account_names"]
            preflight = (
                f"**Pre-flight check (LIVE Dynamics 365 tenant, {len(live['account_names'])} accounts):** "
                + (f"account \"{target_account}\" EXISTS — updates would attach to it.\n\n"
                   if exists else
                   f"account \"{target_account}\" NOT FOUND — applying this update "
                   f"would create a new account record.\n\n")
            )
        else:
            preflight = "**Pre-flight check:** live tenant unreachable — existence check skipped.\n\n"
        return (
            f"**CRM Update Preview** (proposed values from the embedded demo call)\n\n"
            f"**1. Update Opportunity**\n"
            f"- Name: {opp['name']['mapped_value']}\n"
            f"- Amount: ${opp['amount']['mapped_value']:,}\n"
            f"- Stage: {opp['stage']['mapped_value']}\n"
            f"- Close Date: {opp['close_date']['mapped_value']}\n"
            f"- Probability: {opp['probability']['mapped_value']}%\n"
            f"- Next Step: {opp['next_step']['mapped_value']}\n\n"
            f"**2. Log Activity**\n"
            f"- Type: {activity['type']['mapped_value']}\n"
            f"- Subject: {activity['subject']['mapped_value']}\n"
            f"- Duration: {activity['duration_min']['mapped_value']} minutes\n\n"
            f"**3. Create Contacts ({len(new_contacts)}):**\n"
            + "\n".join(f"- {c['name']} ({c['title']}, {c['role']})" for c in new_contacts)
            + "\n\n"
            f"{preflight}"
            f"**Status:** Preview only — no record was written | Requires confirmation\n\n"
            f"Source: [CRM Update Engine + Live Dynamics 365 Tenant]\nAgents: SpeechToCRMAgent"
        )


if __name__ == "__main__":
    agent = SpeechToCRMAgent()
    print("=" * 60)
    print("EMBEDDED DEMO TRANSCRIPT (works offline)")
    print(agent.perform(operation="transcribe_call", call_id="CALL-T001"))
    print()
    print("=" * 60)
    print("LIVE-GROUNDED FIELD MAPPING (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="crm_mapping", call_id="CALL-T001"))
    print()
    print("=" * 60)
    print(agent.perform(operation="update_preview", call_id="CALL-T001"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
