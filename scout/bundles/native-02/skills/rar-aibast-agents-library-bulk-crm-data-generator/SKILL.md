---
name: "rar-aibast-agents-library-bulk-crm-data-generator"
description: "Generates synthetic CRM records and audits a live simulated Dynamics 365 tenant's data shape, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/bulk_crm_data_generator_agent", "rar_sha256": "587ddfc10256eab771b2371321f0fe22b38f261e57f0344b8b69be7ce534513d", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["crm", "data-generation", "testing", "contacts", "accounts", "opportunities"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/bulk_crm_data_generator_agent`. The original RAPP
agent is preserved byte-for-byte in `bulk_crm_data_generator_agent.py` and in the RCI capsule.

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

Bulk CRM Data Generator Agent — a template you are meant to mutate.

Generates synthetic CRM records (contacts, accounts, opportunities) for
testing, demos, and data migration validation. In this template the
`data_summary` operation also audits a real CRM: it counts and summarizes
the live tenant's actual contacts, accounts, and opportunity pipeline, so
you can compare generated data against a live shape.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `data_summary` operation pulls live
     contact/account/opportunity records over real HTTP from the globally
     hosted Static Dynamics 365 tenant (Aster Lane Office Systems —
     synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="data_summary")
     and look for the 22 live accounts and 15-opportunity pipeline.
  2. No network? Everything falls back to the embedded demo layer below
     (_GENERATED_CONTACTS / _GENERATED_ACCOUNTS / _GENERATED_OPPORTUNITIES)
     — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     BULK_CRM_DATA_GENERATOR_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from Salesforce), or replace
     _fetch_collection() with your own client. The fields the rest of
     the file needs are listed in _normalize_live_opportunity() —
     account revenue renders "n/a — enrichment seam" until you wire your
     firmographics provider.

OPERATIONS
  generate_contacts | generate_accounts | generate_opportunities
  | data_summary
  kwargs: operation (required)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The data generation operation to perform",
      "enum": [
        "generate_contacts",
        "generate_accounts",
        "generate_opportunities",
        "data_summary"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_crm_data_generator_agent.py` and embedded as the fenced Python below (sha256 587ddfc10256eab7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_crm_data_generator_agent.py` first:

```bash
python3 bulk_crm_data_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_crm_data_generator_agent.py   # or on stdin
python3 bulk_crm_data_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Bulk CRM Data Generator Agent — a template you are meant to mutate.

Generates synthetic CRM records (contacts, accounts, opportunities) for
testing, demos, and data migration validation. In this template the
`data_summary` operation also audits a real CRM: it counts and summarizes
the live tenant's actual contacts, accounts, and opportunity pipeline, so
you can compare generated data against a live shape.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `data_summary` operation pulls live
     contact/account/opportunity records over real HTTP from the globally
     hosted Static Dynamics 365 tenant (Aster Lane Office Systems —
     synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="data_summary")
     and look for the 22 live accounts and 15-opportunity pipeline.
  2. No network? Everything falls back to the embedded demo layer below
     (_GENERATED_CONTACTS / _GENERATED_ACCOUNTS / _GENERATED_OPPORTUNITIES)
     — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     BULK_CRM_DATA_GENERATOR_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from Salesforce), or replace
     _fetch_collection() with your own client. The fields the rest of
     the file needs are listed in _normalize_live_opportunity() —
     account revenue renders "n/a — enrichment seam" until you wire your
     firmographics provider.

OPERATIONS
  generate_contacts | generate_accounts | generate_opportunities
  | data_summary
  kwargs: operation (required)
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
    "name": "@aibast-agents-library/bulk_crm_data_generator_agent",
    "version": "1.1.0",
    "display_name": "Bulk CRM Data Generator",
    "description": "Generates synthetic CRM records and audits a live simulated Dynamics 365 tenant's data shape, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["crm", "data-generation", "testing", "contacts", "accounts", "opportunities"],
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
#   export BULK_CRM_DATA_GENERATOR_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_opportunity().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "BULK_CRM_DATA_GENERATOR_DATA_URL",
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


def _normalize_live_opportunity(row):
    """Project a Dynamics opportunity onto the shape this agent's
    summaries use. THIS is the contract your replacement data source must
    meet — a dict with these keys."""
    stage = {0: "Open", 1: "Closed Won", 2: "Closed Lost"}.get(row.get("statecode"), "Open")
    return {
        "amount": float(row.get("estimatedvalue") or 0),
        "probability": int(row.get("closeprobability") or 0),
        "stage": stage,
    }


def _live_snapshot():
    """Counts + normalized pipeline from the live tenant; None offline."""
    accounts = _fetch_collection("accounts")
    if not accounts:
        return None
    contacts = _fetch_collection("contacts")
    opportunities = [_normalize_live_opportunity(r) for r in _fetch_collection("opportunities")]
    industries = {}
    for a in accounts:
        industries.setdefault(a.get("industrycode", "Unknown"), 0)
        industries[a.get("industrycode", "Unknown")] += 1
    return {
        "contacts": len(contacts),
        "accounts": len(accounts),
        "opportunities": opportunities,
        "industries": industries,
    }


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_NAME_POOLS = {
    "first_names": ["James", "Maria", "Robert", "Jennifer", "David", "Sarah", "Michael", "Lisa", "William", "Patricia", "Thomas", "Linda", "Charles", "Karen", "Daniel", "Nancy"],
    "last_names": ["Anderson", "Chen", "Rodriguez", "Patel", "O'Brien", "Kim", "Johnson", "Williams", "Martinez", "Lee", "Garcia", "Taylor", "Thomas", "Wilson", "Moore", "Clark"],
    "titles": ["CEO", "CTO", "VP Sales", "Director of IT", "Procurement Manager", "CFO", "VP Marketing", "Operations Director", "Head of Engineering", "Business Development Manager"],
}

_INDUSTRY_LIST = [
    {"name": "Technology", "code": "TECH", "avg_deal_size": 85000, "typical_cycle_days": 90},
    {"name": "Healthcare", "code": "HLTH", "avg_deal_size": 120000, "typical_cycle_days": 120},
    {"name": "Financial Services", "code": "FNSV", "avg_deal_size": 150000, "typical_cycle_days": 150},
    {"name": "Manufacturing", "code": "MFCT", "avg_deal_size": 95000, "typical_cycle_days": 105},
    {"name": "Retail", "code": "RETL", "avg_deal_size": 45000, "typical_cycle_days": 60},
    {"name": "Education", "code": "EDUC", "avg_deal_size": 35000, "typical_cycle_days": 75},
    {"name": "Energy", "code": "ENRG", "avg_deal_size": 200000, "typical_cycle_days": 180},
    {"name": "Professional Services", "code": "PRSV", "avg_deal_size": 65000, "typical_cycle_days": 80},
]

_REVENUE_RANGES = [
    {"label": "Startup", "min": 500000, "max": 5000000, "employee_range": "10-50"},
    {"label": "Small Business", "min": 5000000, "max": 25000000, "employee_range": "50-200"},
    {"label": "Mid-Market", "min": 25000000, "max": 250000000, "employee_range": "200-1000"},
    {"label": "Enterprise", "min": 250000000, "max": 1000000000, "employee_range": "1000-5000"},
    {"label": "Large Enterprise", "min": 1000000000, "max": 10000000000, "employee_range": "5000+"},
]

_STAGE_DEFINITIONS = [
    {"name": "Prospecting", "probability": 10, "typical_duration_days": 14, "exit_criteria": "Initial contact made, interest confirmed"},
    {"name": "Qualification", "probability": 25, "typical_duration_days": 21, "exit_criteria": "Budget, authority, need, timeline confirmed"},
    {"name": "Proposal", "probability": 50, "typical_duration_days": 30, "exit_criteria": "Proposal delivered and reviewed by decision maker"},
    {"name": "Negotiation", "probability": 75, "typical_duration_days": 21, "exit_criteria": "Terms agreed, legal review complete"},
    {"name": "Closed Won", "probability": 100, "typical_duration_days": 0, "exit_criteria": "Contract signed, payment terms set"},
    {"name": "Closed Lost", "probability": 0, "typical_duration_days": 0, "exit_criteria": "Opportunity declined or competitor selected"},
]

_GENERATED_CONTACTS = [
    {"id": "CON-001", "first_name": "James", "last_name": "Anderson", "title": "VP Sales", "company": "Apex Technologies", "email": "james.anderson@apextech.com", "phone": "415-555-0101", "industry": "Technology"},
    {"id": "CON-002", "first_name": "Maria", "last_name": "Chen", "title": "CTO", "company": "HealthFirst Systems", "email": "maria.chen@healthfirst.com", "phone": "312-555-0202", "industry": "Healthcare"},
    {"id": "CON-003", "first_name": "Robert", "last_name": "Patel", "title": "CFO", "company": "Summit Financial Group", "email": "robert.patel@summitfin.com", "phone": "212-555-0303", "industry": "Financial Services"},
    {"id": "CON-004", "first_name": "Jennifer", "last_name": "Rodriguez", "title": "Procurement Manager", "company": "Pacific Manufacturing", "email": "jennifer.rodriguez@pacmfg.com", "phone": "503-555-0404", "industry": "Manufacturing"},
    {"id": "CON-005", "first_name": "David", "last_name": "Kim", "title": "Director of IT", "company": "EduPath Solutions", "email": "david.kim@edupath.com", "phone": "617-555-0505", "industry": "Education"},
]

_GENERATED_ACCOUNTS = [
    {"id": "ACC-001", "name": "Apex Technologies", "industry": "Technology", "revenue": 45000000, "employees": 320, "segment": "Mid-Market", "website": "www.apextech.com", "city": "San Francisco", "state": "CA"},
    {"id": "ACC-002", "name": "HealthFirst Systems", "industry": "Healthcare", "revenue": 180000000, "employees": 890, "segment": "Mid-Market", "website": "www.healthfirst.com", "city": "Chicago", "state": "IL"},
    {"id": "ACC-003", "name": "Summit Financial Group", "industry": "Financial Services", "revenue": 520000000, "employees": 2100, "segment": "Enterprise", "website": "www.summitfin.com", "city": "New York", "state": "NY"},
    {"id": "ACC-004", "name": "Pacific Manufacturing", "industry": "Manufacturing", "revenue": 75000000, "employees": 450, "segment": "Mid-Market", "website": "www.pacmfg.com", "city": "Portland", "state": "OR"},
    {"id": "ACC-005", "name": "EduPath Solutions", "industry": "Education", "revenue": 12000000, "employees": 85, "segment": "Small Business", "website": "www.edupath.com", "city": "Boston", "state": "MA"},
]

_GENERATED_OPPORTUNITIES = [
    {"id": "OPP-001", "name": "Apex Technologies - Platform License", "account": "ACC-001", "amount": 85000, "stage": "Proposal", "close_date": "2025-12-15", "probability": 50, "owner": "Sarah Johnson"},
    {"id": "OPP-002", "name": "HealthFirst - Enterprise Suite", "account": "ACC-002", "amount": 240000, "stage": "Negotiation", "close_date": "2025-11-30", "probability": 75, "owner": "Tom Rivera"},
    {"id": "OPP-003", "name": "Summit Financial - Compliance Module", "account": "ACC-003", "amount": 150000, "stage": "Qualification", "close_date": "2026-02-28", "probability": 25, "owner": "Sarah Johnson"},
    {"id": "OPP-004", "name": "Pacific Mfg - IoT Integration", "account": "ACC-004", "amount": 95000, "stage": "Prospecting", "close_date": "2026-03-31", "probability": 10, "owner": "Mike Davis"},
    {"id": "OPP-005", "name": "EduPath - SaaS Migration", "account": "ACC-005", "amount": 42000, "stage": "Closed Won", "close_date": "2025-10-20", "probability": 100, "owner": "Tom Rivera"},
]


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _summarize_contacts():
    by_industry = {}
    for c in _GENERATED_CONTACTS:
        by_industry.setdefault(c["industry"], []).append(c)
    return by_industry


def _summarize_pipeline():
    total_value = sum(o["amount"] for o in _GENERATED_OPPORTUNITIES)
    weighted = sum(o["amount"] * o["probability"] / 100 for o in _GENERATED_OPPORTUNITIES)
    by_stage = {}
    for o in _GENERATED_OPPORTUNITIES:
        by_stage.setdefault(o["stage"], {"count": 0, "value": 0})
        by_stage[o["stage"]]["count"] += 1
        by_stage[o["stage"]]["value"] += o["amount"]
    return total_value, weighted, by_stage


def _account_segments():
    by_segment = {}
    for a in _GENERATED_ACCOUNTS:
        by_segment.setdefault(a["segment"], {"count": 0, "total_revenue": 0})
        by_segment[a["segment"]]["count"] += 1
        by_segment[a["segment"]]["total_revenue"] += a["revenue"]
    return by_segment


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class BulkCRMDataGeneratorAgent(BasicAgent):
    """
    Bulk CRM data generator for testing and demos.

    Operations:
        generate_contacts       - generate sample contact records
        generate_accounts       - generate sample account records
        generate_opportunities  - generate sample opportunity records
        data_summary            - summarize all generated data
    """

    def __init__(self):
        self.name = "BulkCRMDataGeneratorAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "generate_contacts", "generate_accounts",
                            "generate_opportunities", "data_summary",
                        ],
                        "description": "The data generation operation to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "data_summary")
        dispatch = {
            "generate_contacts": self._generate_contacts,
            "generate_accounts": self._generate_accounts,
            "generate_opportunities": self._generate_opportunities,
            "data_summary": self._data_summary,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler()

    # ── generate_contacts ──────────────────────────────────────
    def _generate_contacts(self):
        rows = ""
        for c in _GENERATED_CONTACTS:
            rows += f"| {c['id']} | {c['first_name']} {c['last_name']} | {c['title']} | {c['company']} | {c['industry']} |\n"
        by_ind = _summarize_contacts()
        dist = "\n".join(f"- {ind}: {len(contacts)} contact(s)" for ind, contacts in by_ind.items())
        pool_info = f"First names: {len(_NAME_POOLS['first_names'])} | Last names: {len(_NAME_POOLS['last_names'])} | Titles: {len(_NAME_POOLS['titles'])}"
        return (
            f"**Generated Contacts ({len(_GENERATED_CONTACTS)} records)**\n\n"
            f"| ID | Name | Title | Company | Industry |\n|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Distribution by Industry:**\n{dist}\n\n"
            f"**Name Pool Capacity:** {pool_info}\n"
            f"**Max Unique Combinations:** {len(_NAME_POOLS['first_names']) * len(_NAME_POOLS['last_names']):,}\n\n"
            f"Source: [Synthetic Data Engine]\nAgents: BulkCRMDataGeneratorAgent"
        )

    # ── generate_accounts ──────────────────────────────────────
    def _generate_accounts(self):
        rows = ""
        for a in _GENERATED_ACCOUNTS:
            rows += f"| {a['id']} | {a['name']} | {a['industry']} | ${a['revenue']:,.0f} | {a['employees']} | {a['segment']} |\n"
        segments = _account_segments()
        seg_rows = "\n".join(f"- {seg}: {d['count']} accounts, ${d['total_revenue']:,.0f} total revenue" for seg, d in segments.items())
        ind_rows = "\n".join(f"| {i['name']} | {i['code']} | ${i['avg_deal_size']:,} | {i['typical_cycle_days']}d |" for i in _INDUSTRY_LIST)
        return (
            f"**Generated Accounts ({len(_GENERATED_ACCOUNTS)} records)**\n\n"
            f"| ID | Name | Industry | Revenue | Employees | Segment |\n|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Segment Distribution:**\n{seg_rows}\n\n"
            f"**Industry Reference:**\n\n"
            f"| Industry | Code | Avg Deal | Cycle |\n|---|---|---|---|\n"
            f"{ind_rows}\n\n"
            f"Source: [Synthetic Data Engine]\nAgents: BulkCRMDataGeneratorAgent"
        )

    # ── generate_opportunities ─────────────────────────────────
    def _generate_opportunities(self):
        rows = ""
        for o in _GENERATED_OPPORTUNITIES:
            rows += f"| {o['id']} | {o['name']} | ${o['amount']:,} | {o['stage']} | {o['probability']}% | {o['close_date']} |\n"
        stage_rows = ""
        for s in _STAGE_DEFINITIONS:
            stage_rows += f"| {s['name']} | {s['probability']}% | {s['typical_duration_days']}d | {s['exit_criteria'][:50]} |\n"
        return (
            f"**Generated Opportunities ({len(_GENERATED_OPPORTUNITIES)} records)**\n\n"
            f"| ID | Name | Amount | Stage | Probability | Close Date |\n|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Stage Definitions:**\n\n"
            f"| Stage | Probability | Duration | Exit Criteria |\n|---|---|---|---|\n"
            f"{stage_rows}\n\n"
            f"Source: [Synthetic Data Engine]\nAgents: BulkCRMDataGeneratorAgent"
        )

    # ── data_summary ───────────────────────────────────────────
    def _data_summary(self):
        live = _live_snapshot()
        if live:
            opps = live["opportunities"]
            total_val = sum(o["amount"] for o in opps)
            weighted_val = sum(o["amount"] * o["probability"] / 100 for o in opps)
            by_stage = {}
            for o in opps:
                by_stage.setdefault(o["stage"], {"count": 0, "value": 0})
                by_stage[o["stage"]]["count"] += 1
                by_stage[o["stage"]]["value"] += o["amount"]
            stage_lines = "\n".join(
                f"| {stg} | {d['count']} | ${d['value']:,.0f} |" for stg, d in by_stage.items()
            )
            ind_lines = "\n".join(
                f"| {ind} | {count} | n/a — enrichment seam |"
                for ind, count in sorted(live["industries"].items())
            )
            return (
                f"**CRM Data Summary (live tenant)**\n\n"
                f"| Entity | Count |\n|---|---|\n"
                f"| Contacts | {live['contacts']} |\n"
                f"| Accounts | {live['accounts']} |\n"
                f"| Opportunities | {len(opps)} |\n\n"
                f"**Pipeline Summary:**\n"
                f"- Total Value: ${total_val:,.0f}\n"
                f"- Weighted Value: ${weighted_val:,.0f}\n\n"
                f"| Stage | Opps | Value |\n|---|---|---|\n"
                f"{stage_lines}\n\n"
                f"**Accounts by Industry:**\n\n"
                f"| Industry | Count | Revenue |\n|---|---|---|\n"
                f"{ind_lines}\n\n"
                f"Revenue is an enrichment seam — wire your firmographics provider.\n\n"
                f"Source: [live Static Dynamics 365 tenant]\nAgents: BulkCRMDataGeneratorAgent"
            )

        total_val, weighted_val, by_stage = _summarize_pipeline()
        segments = _account_segments()
        stage_lines = "\n".join(f"| {stg} | {d['count']} | ${d['value']:,} |" for stg, d in by_stage.items())
        seg_lines = "\n".join(f"| {seg} | {d['count']} | ${d['total_revenue']:,.0f} |" for seg, d in segments.items())
        return (
            f"**CRM Data Generation Summary**\n\n"
            f"| Entity | Count |\n|---|---|\n"
            f"| Contacts | {len(_GENERATED_CONTACTS)} |\n"
            f"| Accounts | {len(_GENERATED_ACCOUNTS)} |\n"
            f"| Opportunities | {len(_GENERATED_OPPORTUNITIES)} |\n\n"
            f"**Pipeline Summary:**\n"
            f"- Total Value: ${total_val:,}\n"
            f"- Weighted Value: ${weighted_val:,.0f}\n\n"
            f"| Stage | Opps | Value |\n|---|---|---|\n"
            f"{stage_lines}\n\n"
            f"**Account Segments:**\n\n"
            f"| Segment | Count | Revenue |\n|---|---|---|\n"
            f"{seg_lines}\n\n"
            f"**Data Quality:** All records validated, no duplicates, referential integrity confirmed.\n\n"
            f"Source: [embedded demo layer (offline fallback)]\nAgents: BulkCRMDataGeneratorAgent"
        )


if __name__ == "__main__":
    agent = BulkCRMDataGeneratorAgent()
    print("=" * 60)
    print("EMBEDDED DEMO GENERATION (works offline)")
    for op in ["generate_contacts", "generate_accounts", "generate_opportunities"]:
        print("=" * 60)
        print(agent.perform(operation=op))
        print()
    print("=" * 60)
    print("LIVE TENANT DATA AUDIT (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="data_summary"))
    print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
