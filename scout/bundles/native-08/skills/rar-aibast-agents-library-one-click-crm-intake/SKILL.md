---
name: "rar-aibast-agents-library-one-click-crm-intake"
description: "Runs CRM intake with duplicate checks against a live simulated Dynamics 365 tenant's leads, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/one_click_crm_intake", "rar_sha256": "d025351a091cb6883853cdae93a6f645317936844f5a781e11352d0fd9527bb5", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["crm", "intake", "data-validation", "duplicate-detection", "import"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/one_click_crm_intake`. The original RAPP
agent is preserved byte-for-byte in `one_click_crm_intake_agent.py` and in the RCI capsule.

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

One-Click CRM Intake Agent — a template you are meant to mutate.

Streamlined CRM data intake with form generation, validation, duplicate
detection, and import preview capabilities. In this template duplicate
detection runs against real CRM records: the live tenant's lead list is
scanned for actual repeated contact names across companies.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `duplicate_check` operation pulls live
     lead records over real HTTP from the globally hosted Static Dynamics
     365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="duplicate_check", template_name="new_lead")
     and look for Remy Hayes, who appears on leads for both Blue Heron
     Stationery and Juniper Ridge Furnishings.
  2. No network? Everything falls back to the embedded demo layer below
     (_INTAKE_TEMPLATES / _SAMPLE_INTAKE_BATCH) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ONE_CLICK_CRM_INTAKE_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your CRM), or replace
     _fetch_collection() with your own client. The fields the rest of
     the file needs are listed in _normalize_live_lead() — everything
     else keeps working untouched.

OPERATIONS
  intake_form | data_validation | duplicate_check | import_preview
  kwargs: operation (required), template_name

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The intake operation to perform",
      "enum": [
        "intake_form",
        "data_validation",
        "duplicate_check",
        "import_preview"
      ],
      "type": "string"
    },
    "template_name": {
      "description": "Template name (e.g. 'new_lead', 'new_account', 'support_case')",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `one_click_crm_intake_agent.py` and embedded as the fenced Python below (sha256 d025351a091cb688…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `one_click_crm_intake_agent.py` first:

```bash
python3 one_click_crm_intake_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 one_click_crm_intake_agent.py   # or on stdin
python3 one_click_crm_intake_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
One-Click CRM Intake Agent — a template you are meant to mutate.

Streamlined CRM data intake with form generation, validation, duplicate
detection, and import preview capabilities. In this template duplicate
detection runs against real CRM records: the live tenant's lead list is
scanned for actual repeated contact names across companies.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `duplicate_check` operation pulls live
     lead records over real HTTP from the globally hosted Static Dynamics
     365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="duplicate_check", template_name="new_lead")
     and look for Remy Hayes, who appears on leads for both Blue Heron
     Stationery and Juniper Ridge Furnishings.
  2. No network? Everything falls back to the embedded demo layer below
     (_INTAKE_TEMPLATES / _SAMPLE_INTAKE_BATCH) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ONE_CLICK_CRM_INTAKE_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your CRM), or replace
     _fetch_collection() with your own client. The fields the rest of
     the file needs are listed in _normalize_live_lead() — everything
     else keeps working untouched.

OPERATIONS
  intake_form | data_validation | duplicate_check | import_preview
  kwargs: operation (required), template_name
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json as _json
import urllib.request

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/one_click_crm_intake",
    "version": "1.1.0",
    "display_name": "One-Click CRM Intake",
    "description": "Runs CRM intake with duplicate checks against a live simulated Dynamics 365 tenant's leads, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["crm", "intake", "data-validation", "duplicate-detection", "import"],
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
#   export ONE_CLICK_CRM_INTAKE_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_lead().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "ONE_CLICK_CRM_INTAKE_DATA_URL",
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
            rows = _json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _normalize_live_lead(row):
    """Project a Dynamics lead onto the intake-record shape this agent
    uses for duplicate scanning. THIS is the contract your replacement
    data source must meet — a dict with these keys."""
    return {
        "name": row.get("fullname", ""),
        "company": row.get("companyname", ""),
        "email": row.get("emailaddress1", ""),
    }


def _live_lead_duplicates():
    """Scan the live tenant's leads for repeated contact names.
    Returns (total_leads, {name: [companies]}); (0, {}) when offline."""
    rows = _fetch_collection("leads")
    leads = [_normalize_live_lead(r) for r in rows if r.get("fullname")]
    by_name = {}
    for lead in leads:
        by_name.setdefault(lead["name"], []).append(lead["company"] or "(no company)")
    duplicates = {name: companies for name, companies in by_name.items() if len(companies) > 1}
    return len(leads), duplicates


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_INTAKE_TEMPLATES = {
    "new_lead": {
        "name": "New Lead Intake", "entity": "lead",
        "fields": [
            {"name": "first_name", "label": "First Name", "type": "text", "required": True, "max_length": 50},
            {"name": "last_name", "label": "Last Name", "type": "text", "required": True, "max_length": 50},
            {"name": "email", "label": "Email", "type": "email", "required": True, "max_length": 100},
            {"name": "company", "label": "Company", "type": "text", "required": True, "max_length": 160},
            {"name": "phone", "label": "Phone", "type": "phone", "required": False, "max_length": 20},
            {"name": "source", "label": "Lead Source", "type": "picklist", "required": True, "options": ["Website", "Referral", "Trade Show", "Cold Call", "LinkedIn"]},
            {"name": "interest", "label": "Product Interest", "type": "picklist", "required": False, "options": ["Platform", "Analytics", "Integration", "Support"]},
            {"name": "notes", "label": "Notes", "type": "textarea", "required": False, "max_length": 2000},
        ],
        "auto_assign_rule": "Round-robin by territory",
    },
    "new_account": {
        "name": "New Account Intake", "entity": "account",
        "fields": [
            {"name": "company_name", "label": "Company Name", "type": "text", "required": True, "max_length": 160},
            {"name": "industry", "label": "Industry", "type": "picklist", "required": True, "options": ["Technology", "Healthcare", "Finance", "Manufacturing", "Retail"]},
            {"name": "revenue", "label": "Annual Revenue", "type": "currency", "required": False},
            {"name": "employees", "label": "Number of Employees", "type": "number", "required": False},
            {"name": "website", "label": "Website", "type": "url", "required": False, "max_length": 200},
            {"name": "city", "label": "City", "type": "text", "required": True, "max_length": 80},
            {"name": "state", "label": "State/Province", "type": "text", "required": True, "max_length": 50},
        ],
        "auto_assign_rule": "Territory-based assignment",
    },
    "support_case": {
        "name": "Support Case Intake", "entity": "incident",
        "fields": [
            {"name": "contact_email", "label": "Contact Email", "type": "email", "required": True, "max_length": 100},
            {"name": "subject", "label": "Subject", "type": "text", "required": True, "max_length": 200},
            {"name": "description", "label": "Description", "type": "textarea", "required": True, "max_length": 5000},
            {"name": "priority", "label": "Priority", "type": "picklist", "required": True, "options": ["Critical", "High", "Medium", "Low"]},
            {"name": "category", "label": "Category", "type": "picklist", "required": True, "options": ["Technical", "Billing", "Feature Request", "General"]},
        ],
        "auto_assign_rule": "Priority-based queue routing",
    },
}

_VALIDATION_RULES = {
    "email": {"pattern": "contains @ and valid domain", "error": "Invalid email format"},
    "phone": {"pattern": "10-15 digits with optional country code", "error": "Invalid phone number"},
    "url": {"pattern": "starts with http:// or https://", "error": "Invalid URL format"},
    "currency": {"pattern": "numeric, non-negative", "error": "Invalid currency value"},
    "required": {"pattern": "non-empty value", "error": "Required field cannot be empty"},
    "max_length": {"pattern": "within character limit", "error": "Value exceeds maximum length"},
}

_DUPLICATE_RULES = {
    "lead": {
        "rules": [
            {"name": "Email Match", "fields": ["email"], "match_type": "exact", "confidence": "High"},
            {"name": "Name + Company", "fields": ["first_name", "last_name", "company"], "match_type": "fuzzy", "confidence": "Medium"},
            {"name": "Phone Match", "fields": ["phone"], "match_type": "exact", "confidence": "High"},
        ],
        "action_on_duplicate": "Flag for review",
    },
    "account": {
        "rules": [
            {"name": "Company Name", "fields": ["company_name"], "match_type": "fuzzy", "confidence": "Medium"},
            {"name": "Website Domain", "fields": ["website"], "match_type": "domain_match", "confidence": "High"},
            {"name": "Name + City", "fields": ["company_name", "city"], "match_type": "fuzzy", "confidence": "Low"},
        ],
        "action_on_duplicate": "Merge suggestion",
    },
    "incident": {
        "rules": [
            {"name": "Subject + Contact", "fields": ["subject", "contact_email"], "match_type": "fuzzy", "confidence": "Medium"},
        ],
        "action_on_duplicate": "Link to existing case",
    },
}

_SAMPLE_INTAKE_BATCH = [
    {"first_name": "Elena", "last_name": "Kowalski", "email": "elena.k@techstart.io", "company": "TechStart Inc", "source": "LinkedIn", "status": "Valid"},
    {"first_name": "Marcus", "last_name": "Thompson", "email": "marcus.t@healthpro.com", "company": "HealthPro Solutions", "source": "Trade Show", "status": "Valid"},
    {"first_name": "Rachel", "last_name": "Chen", "email": "rachel.chen@existing-customer.com", "company": "Existing Customer LLC", "source": "Referral", "status": "Duplicate Detected"},
    {"first_name": "David", "last_name": "", "email": "david@newcorp.com", "company": "NewCorp", "source": "Website", "status": "Validation Error: Last name required"},
    {"first_name": "Sarah", "last_name": "Williams", "email": "sarah.w@summit.com", "company": "Summit Partners", "source": "Cold Call", "status": "Valid"},
]


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _validate_batch(records):
    valid = sum(1 for r in records if r["status"] == "Valid")
    duplicates = sum(1 for r in records if "Duplicate" in r["status"])
    errors = sum(1 for r in records if "Error" in r["status"])
    return valid, duplicates, errors


def _get_template_fields_summary(template):
    required = sum(1 for f in template["fields"] if f["required"])
    optional = len(template["fields"]) - required
    return required, optional


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class OneClickCRMIntakeAgent(BasicAgent):
    """
    One-click CRM intake agent.

    Operations:
        intake_form      - generate intake form for a specific entity
        data_validation  - validate intake data against rules
        duplicate_check  - check for duplicate records
        import_preview   - preview import results before committing
    """

    def __init__(self):
        self.name = "OneClickCRMIntakeAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "intake_form", "data_validation",
                            "duplicate_check", "import_preview",
                        ],
                        "description": "The intake operation to perform",
                    },
                    "template_name": {
                        "type": "string",
                        "description": "Template name (e.g. 'new_lead', 'new_account', 'support_case')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "intake_form")
        template_name = kwargs.get("template_name", "new_lead")
        dispatch = {
            "intake_form": self._intake_form,
            "data_validation": self._data_validation,
            "duplicate_check": self._duplicate_check,
            "import_preview": self._import_preview,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(template_name)

    # ── intake_form ────────────────────────────────────────────
    def _intake_form(self, template_name):
        template = _INTAKE_TEMPLATES.get(template_name)
        if not template:
            keys = ", ".join(_INTAKE_TEMPLATES.keys())
            return f"Template '{template_name}' not found. Available: {keys}"
        req, opt = _get_template_fields_summary(template)
        field_rows = ""
        for f in template["fields"]:
            req_str = "Yes" if f["required"] else "No"
            type_info = f["type"]
            if "options" in f:
                type_info += f" ({', '.join(f['options'][:3])}...)"
            field_rows += f"| {f['label']} | {f['name']} | {type_info} | {req_str} |\n"
        return (
            f"**{template['name']}**\n"
            f"Target Entity: {template['entity']} | Assignment: {template['auto_assign_rule']}\n\n"
            f"| Label | Field Name | Type | Required |\n|---|---|---|---|\n"
            f"{field_rows}\n"
            f"**Summary:** {req} required fields, {opt} optional fields\n\n"
            f"Source: [CRM Intake Engine]\nAgents: OneClickCRMIntakeAgent"
        )

    # ── data_validation ────────────────────────────────────────
    def _data_validation(self, template_name):
        rule_rows = ""
        for rule_name, rule in _VALIDATION_RULES.items():
            rule_rows += f"| {rule_name} | {rule['pattern']} | {rule['error']} |\n"
        valid, dups, errors = _validate_batch(_SAMPLE_INTAKE_BATCH)
        batch_rows = ""
        for r in _SAMPLE_INTAKE_BATCH:
            status_icon = "Pass" if r["status"] == "Valid" else "Fail"
            batch_rows += f"| {r['first_name']} {r['last_name']} | {r['email']} | {status_icon} | {r['status']} |\n"
        return (
            f"**Data Validation Report**\n\n"
            f"**Validation Rules:**\n\n"
            f"| Rule | Pattern | Error Message |\n|---|---|---|\n"
            f"{rule_rows}\n"
            f"**Batch Validation Results ({len(_SAMPLE_INTAKE_BATCH)} records):**\n\n"
            f"| Name | Email | Result | Details |\n|---|---|---|---|\n"
            f"{batch_rows}\n"
            f"**Summary:** {valid} valid, {dups} duplicates, {errors} errors\n\n"
            f"Source: [Validation Engine]\nAgents: OneClickCRMIntakeAgent"
        )

    # ── duplicate_check ────────────────────────────────────────
    def _duplicate_check(self, template_name):
        template = _INTAKE_TEMPLATES.get(template_name)
        entity = template["entity"] if template else "lead"
        dup_config = _DUPLICATE_RULES.get(entity, _DUPLICATE_RULES["lead"])
        rule_rows = ""
        for rule in dup_config["rules"]:
            fields = ", ".join(rule["fields"])
            rule_rows += f"| {rule['name']} | {fields} | {rule['match_type']} | {rule['confidence']} |\n"

        total_live, live_dups = _live_lead_duplicates()
        if total_live:
            dup_lines = "\n".join(
                f"- **{name}** appears on {len(companies)} leads: {', '.join(companies)}"
                for name, companies in sorted(live_dups.items())
            ) or "- No duplicate contact names found."
            return (
                f"**Duplicate Detection: {entity.title()} (live tenant)**\n\n"
                f"**Detection Rules:**\n\n"
                f"| Rule | Fields | Match Type | Confidence |\n|---|---|---|---|\n"
                f"{rule_rows}\n"
                f"**Action on Duplicate:** {dup_config['action_on_duplicate']}\n\n"
                f"**Scan Results (live lead list):**\n"
                f"- Records scanned: {total_live}\n"
                f"- Contacts appearing on multiple leads: {len(live_dups)}\n"
                f"{dup_lines}\n"
                f"- Recommended action: Review and merge or link duplicate leads\n\n"
                f"Source: [live Static Dynamics 365 tenant — real name-match scan]\nAgents: OneClickCRMIntakeAgent"
            )

        return (
            f"**Duplicate Detection: {entity.title()}**\n\n"
            f"**Detection Rules:**\n\n"
            f"| Rule | Fields | Match Type | Confidence |\n|---|---|---|---|\n"
            f"{rule_rows}\n"
            f"**Action on Duplicate:** {dup_config['action_on_duplicate']}\n\n"
            f"**Scan Results (sample batch, simulated):**\n"
            f"- Records scanned: {len(_SAMPLE_INTAKE_BATCH)}\n"
            f"- Potential duplicates: 1\n"
            f"- Match: rachel.chen@existing-customer.com (Email Match, High confidence)\n"
            f"- Recommended action: Review and merge with existing record\n\n"
            f"Source: [embedded demo layer (offline fallback)]\nAgents: OneClickCRMIntakeAgent"
        )

    # ── import_preview ─────────────────────────────────────────
    def _import_preview(self, template_name):
        valid, dups, errors = _validate_batch(_SAMPLE_INTAKE_BATCH)
        total = len(_SAMPLE_INTAKE_BATCH)
        preview_rows = ""
        for r in _SAMPLE_INTAKE_BATCH:
            action = "Create" if r["status"] == "Valid" else ("Review" if "Duplicate" in r["status"] else "Skip")
            preview_rows += f"| {r['first_name']} {r['last_name']} | {r['company']} | {action} | {r['status']} |\n"
        return (
            f"**Import Preview**\n\n"
            f"| Metric | Count |\n|---|---|\n"
            f"| Total Records | {total} |\n"
            f"| Ready to Import | {valid} |\n"
            f"| Duplicates (Review) | {dups} |\n"
            f"| Validation Errors (Skip) | {errors} |\n\n"
            f"**Record Actions:**\n\n"
            f"| Name | Company | Action | Status |\n|---|---|---|---|\n"
            f"{preview_rows}\n"
            f"**Estimated Import Time:** 2 seconds\n"
            f"**Auto-Assignment:** Round-robin by territory\n\n"
            f"Confirm to proceed with importing {valid} records.\n\n"
            f"Source: [CRM Import Engine]\nAgents: OneClickCRMIntakeAgent"
        )


if __name__ == "__main__":
    agent = OneClickCRMIntakeAgent()
    print("=" * 60)
    print("EMBEDDED DEMO INTAKE (works offline)")
    for op in ["intake_form", "data_validation"]:
        print("=" * 60)
        print(agent.perform(operation=op, template_name="new_lead"))
        print()
    print("=" * 60)
    print("LIVE TENANT DUPLICATE SCAN (leads fetched over HTTP; falls back offline)")
    print(agent.perform(operation="duplicate_check", template_name="new_lead"))
    print()
    print("=" * 60)
    print(agent.perform(operation="import_preview", template_name="new_lead"))
    print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
