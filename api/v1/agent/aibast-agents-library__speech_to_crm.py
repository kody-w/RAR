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
