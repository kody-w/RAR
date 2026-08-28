---
name: "rar-aibast-agents-library-dynamics-365-connector"
description: "Queries live entities from a simulated Dynamics 365 tenant over HTTP, with simulated writes and an offline schema/demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/dynamics_365_connector", "rar_sha256": "20284436e19fe975c867b9c69d3720eee9b56cc5fb2b6fa6f398a88122d5fa7a", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["dynamics-365", "crm", "d365", "entity", "bulk-import", "schema"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/dynamics_365_connector`. The original RAPP
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

Dynamics 365 Connector Agent — a template you are meant to mutate.

Provides entity querying, record creation, bulk import, and schema
inspection for Microsoft Dynamics 365 CRM environments. This is the most
literal template in the library: entity queries run against a real
OData-shaped Dynamics endpoint out of the box, and writes stay simulated
until you wire real credentials.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `entity_query` operation pulls live
     entity records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="entity_query", entity_name="account")
     and look for Prairie Wind Energy Cooperative in the 22 live accounts.
  2. No network? Everything falls back to the embedded demo layer below
     (_ENTITY_SCHEMAS / _SAMPLE_RECORDS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     DYNAMICS_365_DATA_URL to your real org's Web API base (adding auth
     headers in _fetch_collection()), or replace _fetch_collection()
     entirely. The record shape flows straight through — the query
     renderer works with whatever columns your entity returns.
     record_create and bulk_import remain simulated receipts until you
     wire a writable endpoint.

OPERATIONS
  entity_query | record_create | bulk_import | schema_inspect
  kwargs: operation (required), entity_name

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "entity_name": {
      "description": "D365 entity logical name (e.g. 'account', 'contact', 'opportunity')",
      "type": "string"
    },
    "operation": {
      "description": "The D365 operation to perform",
      "enum": [
        "entity_query",
        "record_create",
        "bulk_import",
        "schema_inspect"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dynamics_365_agent.py` and embedded as the fenced Python below (sha256 20284436e19fe975…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dynamics_365_agent.py` first:

```bash
python3 dynamics_365_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dynamics_365_agent.py   # or on stdin
python3 dynamics_365_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
Dynamics 365 Connector Agent — a template you are meant to mutate.

Provides entity querying, record creation, bulk import, and schema
inspection for Microsoft Dynamics 365 CRM environments. This is the most
literal template in the library: entity queries run against a real
OData-shaped Dynamics endpoint out of the box, and writes stay simulated
until you wire real credentials.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `entity_query` operation pulls live
     entity records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="entity_query", entity_name="account")
     and look for Prairie Wind Energy Cooperative in the 22 live accounts.
  2. No network? Everything falls back to the embedded demo layer below
     (_ENTITY_SCHEMAS / _SAMPLE_RECORDS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     DYNAMICS_365_DATA_URL to your real org's Web API base (adding auth
     headers in _fetch_collection()), or replace _fetch_collection()
     entirely. The record shape flows straight through — the query
     renderer works with whatever columns your entity returns.
     record_create and bulk_import remain simulated receipts until you
     wire a writable endpoint.

OPERATIONS
  entity_query | record_create | bulk_import | schema_inspect
  kwargs: operation (required), entity_name
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
    "name": "@aibast-agents-library/dynamics_365_connector",
    "version": "1.1.0",
    "display_name": "Dynamics 365 Connector",
    "description": "Queries live entities from a simulated Dynamics 365 tenant over HTTP, with simulated writes and an offline schema/demo fallback.",
    "author": "AIBAST",
    "tags": ["dynamics-365", "crm", "d365", "entity", "bulk-import", "schema"],
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
#   export DYNAMICS_365_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with an authenticated D365 Web API
# client. _live_entity_records() maps entity logical names onto
# collection endpoints.
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "DYNAMICS_365_DATA_URL",
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


_ENTITY_COLLECTIONS = {
    "account": "accounts",
    "contact": "contacts",
    "opportunity": "opportunities",
    "lead": "leads",
    "incident": "incidents",
    "quote": "quotes",
    "salesorder": "salesorders",
    "invoice": "invoices",
    "product": "products",
    "task": "tasks",
    "email": "emails",
    "systemuser": "systemusers",
}


def _live_entity_records(entity):
    """Live records for a D365 entity logical name; [] when offline or
    the entity has no mapped collection. THIS mapping is the contract —
    extend it when your org adds custom entities."""
    collection = _ENTITY_COLLECTIONS.get(entity)
    if not collection:
        return []
    return _fetch_collection(collection)


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_ENTITY_SCHEMAS = {
    "account": {
        "logical_name": "account", "display_name": "Account",
        "primary_key": "accountid", "primary_name": "name",
        "attributes": [
            {"name": "accountid", "type": "Uniqueidentifier", "required": True},
            {"name": "name", "type": "String", "max_length": 160, "required": True},
            {"name": "accountnumber", "type": "String", "max_length": 20, "required": False},
            {"name": "industrycode", "type": "Picklist", "required": False},
            {"name": "revenue", "type": "Money", "required": False},
            {"name": "numberofemployees", "type": "Integer", "required": False},
            {"name": "telephone1", "type": "String", "max_length": 50, "required": False},
            {"name": "emailaddress1", "type": "String", "max_length": 100, "required": False},
            {"name": "websiteurl", "type": "String", "max_length": 200, "required": False},
            {"name": "address1_city", "type": "String", "max_length": 80, "required": False},
            {"name": "address1_stateorprovince", "type": "String", "max_length": 50, "required": False},
            {"name": "ownerid", "type": "Lookup", "target": "systemuser", "required": True},
        ],
        "record_count": 1247,
    },
    "contact": {
        "logical_name": "contact", "display_name": "Contact",
        "primary_key": "contactid", "primary_name": "fullname",
        "attributes": [
            {"name": "contactid", "type": "Uniqueidentifier", "required": True},
            {"name": "firstname", "type": "String", "max_length": 50, "required": False},
            {"name": "lastname", "type": "String", "max_length": 50, "required": True},
            {"name": "emailaddress1", "type": "String", "max_length": 100, "required": False},
            {"name": "telephone1", "type": "String", "max_length": 50, "required": False},
            {"name": "jobtitle", "type": "String", "max_length": 100, "required": False},
            {"name": "parentcustomerid", "type": "Lookup", "target": "account", "required": False},
            {"name": "ownerid", "type": "Lookup", "target": "systemuser", "required": True},
        ],
        "record_count": 4532,
    },
    "opportunity": {
        "logical_name": "opportunity", "display_name": "Opportunity",
        "primary_key": "opportunityid", "primary_name": "name",
        "attributes": [
            {"name": "opportunityid", "type": "Uniqueidentifier", "required": True},
            {"name": "name", "type": "String", "max_length": 300, "required": True},
            {"name": "estimatedvalue", "type": "Money", "required": False},
            {"name": "estimatedclosedate", "type": "DateTime", "required": False},
            {"name": "stepname", "type": "String", "max_length": 200, "required": False},
            {"name": "parentaccountid", "type": "Lookup", "target": "account", "required": False},
            {"name": "parentcontactid", "type": "Lookup", "target": "contact", "required": False},
            {"name": "closeprobability", "type": "Integer", "required": False},
            {"name": "ownerid", "type": "Lookup", "target": "systemuser", "required": True},
        ],
        "record_count": 892,
    },
}

_SAMPLE_RECORDS = {
    "account": [
        {"accountid": "a1b2c3d4-0001", "name": "Contoso Ltd", "accountnumber": "ACC-10001", "industrycode": "Technology", "revenue": 45000000, "numberofemployees": 320, "address1_city": "Seattle", "address1_stateorprovince": "WA"},
        {"accountid": "a1b2c3d4-0002", "name": "Fabrikam Inc", "accountnumber": "ACC-10002", "industrycode": "Manufacturing", "revenue": 89000000, "numberofemployees": 650, "address1_city": "Portland", "address1_stateorprovince": "OR"},
        {"accountid": "a1b2c3d4-0003", "name": "Adventure Works", "accountnumber": "ACC-10003", "industrycode": "Retail", "revenue": 12000000, "numberofemployees": 95, "address1_city": "Denver", "address1_stateorprovince": "CO"},
    ],
    "contact": [
        {"contactid": "c1d2e3f4-0001", "firstname": "Alex", "lastname": "Rivera", "emailaddress1": "alex.rivera@contoso.com", "jobtitle": "CTO", "parentcustomerid": "a1b2c3d4-0001"},
        {"contactid": "c1d2e3f4-0002", "firstname": "Kim", "lastname": "Park", "emailaddress1": "kim.park@fabrikam.com", "jobtitle": "VP Operations", "parentcustomerid": "a1b2c3d4-0002"},
        {"contactid": "c1d2e3f4-0003", "firstname": "Jordan", "lastname": "Hayes", "emailaddress1": "jordan.hayes@adventureworks.com", "jobtitle": "Purchasing Manager", "parentcustomerid": "a1b2c3d4-0003"},
    ],
    "opportunity": [
        {"opportunityid": "o1p2q3r4-0001", "name": "Contoso - Cloud Migration", "estimatedvalue": 125000, "stepname": "Proposal", "closeprobability": 60, "parentaccountid": "a1b2c3d4-0001", "estimatedclosedate": "2025-12-15"},
        {"opportunityid": "o1p2q3r4-0002", "name": "Fabrikam - IoT Platform", "estimatedvalue": 89000, "stepname": "Qualification", "closeprobability": 30, "parentaccountid": "a1b2c3d4-0002", "estimatedclosedate": "2026-02-28"},
    ],
}

_IMPORT_TEMPLATES = {
    "account_import": {
        "entity": "account", "format": "CSV",
        "required_columns": ["name", "accountnumber"],
        "optional_columns": ["industrycode", "revenue", "numberofemployees", "telephone1", "emailaddress1", "websiteurl", "address1_city", "address1_stateorprovince"],
        "max_batch_size": 1000, "estimated_time_per_1000": "45 seconds",
        "duplicate_detection_fields": ["name", "accountnumber"],
    },
    "contact_import": {
        "entity": "contact", "format": "CSV",
        "required_columns": ["lastname"],
        "optional_columns": ["firstname", "emailaddress1", "telephone1", "jobtitle", "parentcustomerid"],
        "max_batch_size": 2000, "estimated_time_per_1000": "30 seconds",
        "duplicate_detection_fields": ["emailaddress1", "firstname+lastname"],
    },
    "opportunity_import": {
        "entity": "opportunity", "format": "CSV",
        "required_columns": ["name"],
        "optional_columns": ["estimatedvalue", "estimatedclosedate", "stepname", "parentaccountid", "closeprobability"],
        "max_batch_size": 500, "estimated_time_per_1000": "60 seconds",
        "duplicate_detection_fields": ["name", "parentaccountid"],
    },
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _format_schema_attributes(entity_name):
    schema = _ENTITY_SCHEMAS.get(entity_name, {})
    attrs = schema.get("attributes", [])
    rows = ""
    for a in attrs:
        req = "Yes" if a.get("required") else "No"
        extra = ""
        if "max_length" in a:
            extra = f"max: {a['max_length']}"
        elif "target" in a:
            extra = f"-> {a['target']}"
        rows += f"| {a['name']} | {a['type']} | {req} | {extra} |\n"
    return rows


def _format_records(entity_name):
    records = _SAMPLE_RECORDS.get(entity_name, [])
    if not records:
        return "No records found."
    keys = list(records[0].keys())[:6]
    header = " | ".join(keys)
    sep = " | ".join(["---"] * len(keys))
    rows = ""
    for r in records:
        vals = [str(r.get(k, ""))[:25] for k in keys]
        rows += "| " + " | ".join(vals) + " |\n"
    return f"| {header} |\n|{sep}|\n{rows}"


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class Dynamics365ConnectorAgent(BasicAgent):
    """
    Dynamics 365 connector agent.

    Operations:
        entity_query    - query entity records with filters
        record_create   - create new records in an entity
        bulk_import     - bulk import records from templates
        schema_inspect  - inspect entity schema and metadata
    """

    def __init__(self):
        self.name = "Dynamics365ConnectorAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "entity_query", "record_create",
                            "bulk_import", "schema_inspect",
                        ],
                        "description": "The D365 operation to perform",
                    },
                    "entity_name": {
                        "type": "string",
                        "description": "D365 entity logical name (e.g. 'account', 'contact', 'opportunity')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "schema_inspect")
        entity = kwargs.get("entity_name", "account")
        dispatch = {
            "entity_query": self._entity_query,
            "record_create": self._record_create,
            "bulk_import": self._bulk_import,
            "schema_inspect": self._schema_inspect,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(entity)

    # ── entity_query ───────────────────────────────────────────
    def _entity_query(self, entity):
        live = _live_entity_records(entity)
        if live:
            preferred = ["name", "fullname", "title", "subject",
                         "accountnumber", "customeridname", "owneridname",
                         "estimatedvalue", "statecode"]
            keys = [k for k in preferred if k in live[0]][:6]
            if not keys:
                keys = [k for k in live[0] if "@" not in k][:6]
            header = " | ".join(keys)
            sep = " | ".join(["---"] * len(keys))
            rows = ""
            for r in live[:5]:
                vals = [str(r.get(k, ""))[:32] for k in keys]
                rows += "| " + " | ".join(vals) + " |\n"
            return (
                f"**D365 Entity Query: {entity.title()} (live tenant)**\n\n"
                f"Total Records: {len(live):,}\n\n"
                f"**Sample Records (first 5):**\n\n"
                f"| {header} |\n|{sep}|\n{rows}\n"
                f"**Query Info:**\n"
                f"- Entity: {entity}\n"
                f"- Endpoint: {DATA_SOURCE_URL}/{_ENTITY_COLLECTIONS[entity]}.json\n"
                f"- Records returned: {min(5, len(live))} of {len(live):,}\n\n"
                f"Source: [live Static Dynamics 365 tenant]\nAgents: Dynamics365ConnectorAgent"
            )

        schema = _ENTITY_SCHEMAS.get(entity)
        if not schema:
            return f"Entity '{entity}' not found. Available: {', '.join(_ENTITY_SCHEMAS.keys())}"
        record_table = _format_records(entity)
        count = schema["record_count"]
        return (
            f"**D365 Entity Query: {schema['display_name']}**\n\n"
            f"Total Records: {count:,} (simulated)\n\n"
            f"**Sample Records:**\n\n{record_table}\n"
            f"**Query Info:**\n"
            f"- Entity: {schema['logical_name']}\n"
            f"- Primary Key: {schema['primary_key']}\n"
            f"- Primary Name: {schema['primary_name']}\n"
            f"- Records returned: {len(_SAMPLE_RECORDS.get(entity, []))} of {count:,}\n\n"
            f"Source: [embedded demo layer (offline fallback)]\nAgents: Dynamics365ConnectorAgent"
        )

    # ── record_create ──────────────────────────────────────────
    def _record_create(self, entity):
        schema = _ENTITY_SCHEMAS.get(entity)
        if not schema:
            return f"Entity '{entity}' not found. Available: {', '.join(_ENTITY_SCHEMAS.keys())}"
        required_attrs = [a for a in schema["attributes"] if a.get("required")]
        req_rows = ""
        for a in required_attrs:
            req_rows += f"| {a['name']} | {a['type']} | Required |\n"
        sample = _SAMPLE_RECORDS.get(entity, [{}])[0]
        sample_lines = "\n".join(f"  \"{k}\": \"{v}\"" for k, v in list(sample.items())[:5])
        return (
            f"**D365 Record Create: {schema['display_name']}**\n\n"
            f"**Required Fields:**\n\n"
            f"| Attribute | Type | Status |\n|---|---|---|\n"
            f"{req_rows}\n"
            f"**Sample Payload:**\n```json\n{{\n{sample_lines}\n}}\n```\n\n"
            f"**Result:** Simulated — record creation receipt only; no live system was modified\n"
            f"- Entity: {schema['logical_name']}\n"
            f"- Simulated New Record Count: {schema['record_count'] + 1:,}\n\n"
            f"Source: [simulated write — wire a real Web API client at the LIVE DATA SEAM]\nAgents: Dynamics365ConnectorAgent"
        )

    # ── bulk_import ────────────────────────────────────────────
    def _bulk_import(self, entity):
        template_key = f"{entity}_import"
        template = _IMPORT_TEMPLATES.get(template_key)
        if not template:
            return f"No import template for '{entity}'. Available: {', '.join(k.replace('_import','') for k in _IMPORT_TEMPLATES.keys())}"
        req_cols = ", ".join(template["required_columns"])
        opt_cols = ", ".join(template["optional_columns"][:5])
        dup_fields = ", ".join(template["duplicate_detection_fields"])
        return (
            f"**D365 Bulk Import: {entity.title()}**\n\n"
            f"| Setting | Value |\n|---|---|\n"
            f"| Format | {template['format']} |\n"
            f"| Max Batch Size | {template['max_batch_size']:,} records |\n"
            f"| Est. Time per 1000 | {template['estimated_time_per_1000']} |\n"
            f"| Duplicate Detection | {dup_fields} |\n\n"
            f"**Required Columns:** {req_cols}\n\n"
            f"**Optional Columns:** {opt_cols}, ...\n\n"
            f"**Import Preview:**\n"
            f"- Records to import: 500 (simulated)\n"
            f"- Duplicates detected: 12\n"
            f"- Records to create: 488\n"
            f"- Estimated time: 23 seconds\n\n"
            f"Source: [Dynamics 365 Import Service]\nAgents: Dynamics365ConnectorAgent"
        )

    # ── schema_inspect ─────────────────────────────────────────
    def _schema_inspect(self, entity):
        schema = _ENTITY_SCHEMAS.get(entity)
        if not schema:
            overview_rows = ""
            for name, s in _ENTITY_SCHEMAS.items():
                overview_rows += f"| {name} | {s['display_name']} | {len(s['attributes'])} | {s['record_count']:,} |\n"
            return (
                f"**D365 Schema Overview**\n\n"
                f"| Entity | Display Name | Attributes | Records |\n|---|---|---|---|\n"
                f"{overview_rows}\n"
                f"Specify `entity_name` to inspect a specific entity.\n\n"
                f"Source: [Dynamics 365 Metadata API]\nAgents: Dynamics365ConnectorAgent"
            )
        attr_rows = _format_schema_attributes(entity)
        return (
            f"**D365 Schema: {schema['display_name']}**\n\n"
            f"| Property | Value |\n|---|---|\n"
            f"| Logical Name | {schema['logical_name']} |\n"
            f"| Primary Key | {schema['primary_key']} |\n"
            f"| Primary Name | {schema['primary_name']} |\n"
            f"| Record Count | {schema['record_count']:,} |\n"
            f"| Attributes | {len(schema['attributes'])} |\n\n"
            f"**Attributes:**\n\n"
            f"| Name | Type | Required | Details |\n|---|---|---|---|\n"
            f"{attr_rows}\n\n"
            f"Source: [Dynamics 365 Metadata API]\nAgents: Dynamics365ConnectorAgent"
        )


if __name__ == "__main__":
    agent = Dynamics365ConnectorAgent()
    print("=" * 60)
    print("LIVE TENANT ENTITY QUERY (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="entity_query", entity_name="account"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO OPERATIONS (work offline; writes are simulated)")
    for op in ["record_create", "bulk_import", "schema_inspect"]:
        print("=" * 60)
        print(agent.perform(operation=op, entity_name="account"))
        print()
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
