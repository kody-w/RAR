---
name: "rar-aibast-agents-library-software-customer-onboarding"
description: "Tracks onboarding pipelines and blockers from a live simulated Dynamics 365 tenant's accounts and cases, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/software_customer_onboarding", "rar_sha256": "66ae08bf5fe89d05a0f1cc1a8b365adadb72a72e127d4487111e71baf83effea", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["onboarding", "customer-success", "saas", "adoption", "milestones"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/software_customer_onboarding`. The original RAPP
agent is preserved byte-for-byte in `customer_onboarding_agent.py` and in the RCI capsule.

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

Customer Onboarding Agent — a template you are meant to mutate.

Tracks customer onboarding progress, milestone completion, feature adoption
metrics, and risk flags for SaaS customer success teams managing enterprise
onboarding pipelines.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live accounts and service cases over real
     HTTP from the globally hosted Static Dynamics 365 tenant (Aster
     Lane Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="onboarding_status")
     — with network up, the pipeline is built from the tenant's 22 live
     accounts with open-case friction signals, and spotlights onboarding
     cases such as CAS-260135 "Contractor onboarding blocked on
     background check". In this template an onboarding engagement is
     represented as a CRM account and its blockers as Dynamics cases.
  2. No network? Everything falls back to the embedded demo layer below
     (CUSTOMERS / RISK_THRESHOLDS) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SOFTWARE_CUSTOMER_ONBOARDING_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from Gainsight/Totango),
     or replace _fetch_collection() with your own CS platform API. The
     fields the rest of the file needs are listed in
     _normalize_live_engagement() — ARR, health score, and go-live dates
     stay "n/a — enrichment seam" until you wire your CS platform.

OPERATIONS
  onboarding_status | milestone_tracking | adoption_metrics | risk_flags
  kwargs: operation (required), customer_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "customer_id": {
      "description": "Optional customer ID to filter results.",
      "type": "string"
    },
    "operation": {
      "description": "The onboarding operation to perform.",
      "enum": [
        "onboarding_status",
        "milestone_tracking",
        "adoption_metrics",
        "risk_flags"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_onboarding_agent.py` and embedded as the fenced Python below (sha256 66ae08bf5fe89d05…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_onboarding_agent.py` first:

```bash
python3 customer_onboarding_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_onboarding_agent.py   # or on stdin
python3 customer_onboarding_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer Onboarding Agent — a template you are meant to mutate.

Tracks customer onboarding progress, milestone completion, feature adoption
metrics, and risk flags for SaaS customer success teams managing enterprise
onboarding pipelines.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live accounts and service cases over real
     HTTP from the globally hosted Static Dynamics 365 tenant (Aster
     Lane Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="onboarding_status")
     — with network up, the pipeline is built from the tenant's 22 live
     accounts with open-case friction signals, and spotlights onboarding
     cases such as CAS-260135 "Contractor onboarding blocked on
     background check". In this template an onboarding engagement is
     represented as a CRM account and its blockers as Dynamics cases.
  2. No network? Everything falls back to the embedded demo layer below
     (CUSTOMERS / RISK_THRESHOLDS) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SOFTWARE_CUSTOMER_ONBOARDING_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from Gainsight/Totango),
     or replace _fetch_collection() with your own CS platform API. The
     fields the rest of the file needs are listed in
     _normalize_live_engagement() — ARR, health score, and go-live dates
     stay "n/a — enrichment seam" until you wire your CS platform.

OPERATIONS
  onboarding_status | milestone_tracking | adoption_metrics | risk_flags
  kwargs: operation (required), customer_id
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/software_customer_onboarding",
    "version": "1.1.0",
    "display_name": "Customer Onboarding Agent",
    "description": "Tracks onboarding pipelines and blockers from a live simulated Dynamics 365 tenant's accounts and cases, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["onboarding", "customer-success", "saas", "adoption", "milestones"],
    "category": "software_digital_products",
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
#   export SOFTWARE_CUSTOMER_ONBOARDING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CS-platform client.
# Downstream code only needs the fields from
# _normalize_live_engagement().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "SOFTWARE_CUSTOMER_ONBOARDING_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}

# Case-title keywords that mark a tenant case as an onboarding blocker.
_ONBOARDING_KEYWORDS = ("onboarding", "kickoff", "training", "migration", "intake")


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


def _normalize_live_engagement(row, incidents):
    """Project a Dynamics account record onto the shape this agent uses —
    in this template an onboarding engagement IS a CRM account and its
    blockers are Dynamics cases. THIS is the contract your replacement
    data source must meet — a dict with these keys. None means 'not
    available from CRM alone' and the renderers label it as an
    enrichment seam."""
    name = row.get("name", "Unknown")
    open_cases = [
        i for i in incidents
        if i.get("customeridname") == name and i.get("statecode") == 0
    ]
    return {
        "name": name,
        "csm": row.get("owneridname", "Unassigned"),
        "primary_contact": row.get("primarycontactidname", ""),
        "since": str(row.get("createdon") or "")[:10],
        "open_cases": len(open_cases),
        "open_case_titles": [c.get("title", "untitled") for c in open_cases[:2]],
        "arr": None,             # enrichment seam — wire your billing system
        "health_score": None,    # enrichment seam — wire your CS platform
        "target_go_live": None,  # enrichment seam
        "_live": True,
    }


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Synthetic domain data
# ---------------------------------------------------------------------------

CUSTOMERS = {
    "CUST-1001": {
        "name": "Meridian Healthcare Systems",
        "plan": "Enterprise",
        "arr": 186000,
        "onboarding_start": "2026-01-15",
        "target_go_live": "2026-03-31",
        "csm": "Priya Sharma",
        "health_score": 72,
        "milestones": {
            "kickoff_complete": {"status": "complete", "date": "2026-01-18"},
            "sso_configured": {"status": "complete", "date": "2026-01-25"},
            "data_migration": {"status": "complete", "date": "2026-02-10"},
            "integration_setup": {"status": "in_progress", "date": None},
            "user_training": {"status": "not_started", "date": None},
            "go_live": {"status": "not_started", "date": None},
        },
        "feature_adoption": {
            "dashboard": 88,
            "reporting": 62,
            "api_access": 45,
            "automation_rules": 12,
            "custom_fields": 33,
        },
        "training_completion_pct": 41,
        "active_users": 28,
        "licensed_users": 75,
    },
    "CUST-1002": {
        "name": "Apex Financial Group",
        "plan": "Enterprise",
        "arr": 240000,
        "onboarding_start": "2026-02-01",
        "target_go_live": "2026-04-15",
        "csm": "Marcus Chen",
        "health_score": 89,
        "milestones": {
            "kickoff_complete": {"status": "complete", "date": "2026-02-03"},
            "sso_configured": {"status": "complete", "date": "2026-02-08"},
            "data_migration": {"status": "complete", "date": "2026-02-20"},
            "integration_setup": {"status": "complete", "date": "2026-03-05"},
            "user_training": {"status": "in_progress", "date": None},
            "go_live": {"status": "not_started", "date": None},
        },
        "feature_adoption": {
            "dashboard": 95,
            "reporting": 81,
            "api_access": 72,
            "automation_rules": 55,
            "custom_fields": 68,
        },
        "training_completion_pct": 73,
        "active_users": 92,
        "licensed_users": 120,
    },
    "CUST-1003": {
        "name": "Vanguard Logistics",
        "plan": "Professional",
        "arr": 84000,
        "onboarding_start": "2025-12-10",
        "target_go_live": "2026-02-28",
        "csm": "Priya Sharma",
        "health_score": 38,
        "milestones": {
            "kickoff_complete": {"status": "complete", "date": "2025-12-13"},
            "sso_configured": {"status": "complete", "date": "2025-12-20"},
            "data_migration": {"status": "blocked", "date": None},
            "integration_setup": {"status": "not_started", "date": None},
            "user_training": {"status": "not_started", "date": None},
            "go_live": {"status": "not_started", "date": None},
        },
        "feature_adoption": {
            "dashboard": 55,
            "reporting": 20,
            "api_access": 0,
            "automation_rules": 0,
            "custom_fields": 10,
        },
        "training_completion_pct": 15,
        "active_users": 8,
        "licensed_users": 40,
    },
    "CUST-1004": {
        "name": "BrightPath Education",
        "plan": "Professional",
        "arr": 96000,
        "onboarding_start": "2026-02-20",
        "target_go_live": "2026-04-30",
        "csm": "Marcus Chen",
        "health_score": 81,
        "milestones": {
            "kickoff_complete": {"status": "complete", "date": "2026-02-22"},
            "sso_configured": {"status": "complete", "date": "2026-03-01"},
            "data_migration": {"status": "in_progress", "date": None},
            "integration_setup": {"status": "not_started", "date": None},
            "user_training": {"status": "not_started", "date": None},
            "go_live": {"status": "not_started", "date": None},
        },
        "feature_adoption": {
            "dashboard": 78,
            "reporting": 45,
            "api_access": 22,
            "automation_rules": 5,
            "custom_fields": 30,
        },
        "training_completion_pct": 28,
        "active_users": 15,
        "licensed_users": 35,
    },
    "CUST-1005": {
        "name": "Orion Manufacturing",
        "plan": "Enterprise",
        "arr": 312000,
        "onboarding_start": "2026-03-01",
        "target_go_live": "2026-05-15",
        "csm": "Priya Sharma",
        "health_score": 91,
        "milestones": {
            "kickoff_complete": {"status": "complete", "date": "2026-03-03"},
            "sso_configured": {"status": "in_progress", "date": None},
            "data_migration": {"status": "not_started", "date": None},
            "integration_setup": {"status": "not_started", "date": None},
            "user_training": {"status": "not_started", "date": None},
            "go_live": {"status": "not_started", "date": None},
        },
        "feature_adoption": {
            "dashboard": 40,
            "reporting": 15,
            "api_access": 10,
            "automation_rules": 0,
            "custom_fields": 5,
        },
        "training_completion_pct": 8,
        "active_users": 12,
        "licensed_users": 200,
    },
}

RISK_THRESHOLDS = {
    "health_score_critical": 40,
    "health_score_warning": 60,
    "training_min_pct": 50,
    "adoption_min_pct": 30,
    "user_activation_min_pct": 40,
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _onboarding_status_summary():
    total = len(CUSTOMERS)
    on_track = sum(1 for c in CUSTOMERS.values() if c["health_score"] >= 70)
    at_risk = sum(1 for c in CUSTOMERS.values() if 40 <= c["health_score"] < 70)
    critical = sum(1 for c in CUSTOMERS.values() if c["health_score"] < 40)
    total_arr = sum(c["arr"] for c in CUSTOMERS.values())
    return {
        "total_customers": total,
        "on_track": on_track,
        "at_risk": at_risk,
        "critical": critical,
        "total_arr": total_arr,
        "customers": {cid: {"name": c["name"], "health_score": c["health_score"],
                            "plan": c["plan"], "target_go_live": c["target_go_live"]}
                      for cid, c in CUSTOMERS.items()},
    }


def _milestone_tracking():
    results = {}
    for cid, c in CUSTOMERS.items():
        ms = c["milestones"]
        done = sum(1 for m in ms.values() if m["status"] == "complete")
        total = len(ms)
        blocked = [k for k, v in ms.items() if v["status"] == "blocked"]
        next_ms = next((k for k, v in ms.items() if v["status"] in ("in_progress", "not_started")), None)
        results[cid] = {
            "name": c["name"], "completed": done, "total": total,
            "pct": round(done / total * 100, 1), "blocked": blocked,
            "next_milestone": next_ms,
        }
    return results


def _adoption_metrics():
    results = {}
    for cid, c in CUSTOMERS.items():
        fa = c["feature_adoption"]
        avg = round(sum(fa.values()) / len(fa), 1)
        act_pct = round(c["active_users"] / c["licensed_users"] * 100, 1) if c["licensed_users"] else 0
        results[cid] = {
            "name": c["name"], "avg_adoption_pct": avg,
            "feature_adoption": fa, "training_pct": c["training_completion_pct"],
            "activation_pct": act_pct, "active_users": c["active_users"],
            "licensed_users": c["licensed_users"],
        }
    return results


def _risk_flags():
    flags = []
    for cid, c in CUSTOMERS.items():
        cflags = []
        if c["health_score"] < RISK_THRESHOLDS["health_score_critical"]:
            cflags.append("CRITICAL: Health score below threshold")
        elif c["health_score"] < RISK_THRESHOLDS["health_score_warning"]:
            cflags.append("WARNING: Health score declining")
        if c["training_completion_pct"] < RISK_THRESHOLDS["training_min_pct"]:
            cflags.append("Low training completion")
        act = round(c["active_users"] / c["licensed_users"] * 100, 1) if c["licensed_users"] else 0
        if act < RISK_THRESHOLDS["user_activation_min_pct"]:
            cflags.append("Low user activation")
        blocked = [k for k, v in c["milestones"].items() if v["status"] == "blocked"]
        if blocked:
            cflags.append(f"Blocked milestones: {', '.join(blocked)}")
        if cflags:
            flags.append({"id": cid, "name": c["name"], "arr": c["arr"],
                          "health_score": c["health_score"], "flags": cflags})
    flags.sort(key=lambda x: x["health_score"])
    return flags


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class CustomerOnboardingAgent(BasicAgent):
    """Customer onboarding tracking and risk assessment agent."""

    def __init__(self):
        self.name = "CustomerOnboardingAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "onboarding_status",
                            "milestone_tracking",
                            "adoption_metrics",
                            "risk_flags",
                        ],
                        "description": "The onboarding operation to perform.",
                    },
                    "customer_id": {
                        "type": "string",
                        "description": "Optional customer ID to filter results.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "onboarding_status")
        if op == "onboarding_status":
            return self._onboarding_status(kwargs.get("customer_id"))
        elif op == "milestone_tracking":
            return self._milestone_tracking()
        elif op == "adoption_metrics":
            return self._adoption_metrics()
        elif op == "risk_flags":
            return self._risk_flags()
        return f"**Error:** Unknown operation `{op}`."

    def _live_onboarding_status(self, engagements, incidents):
        """Pipeline built from live tenant accounts (preferred online)."""
        with_friction = [e for e in engagements if e["open_cases"] > 0]
        blockers = [
            i for i in incidents
            if i.get("statecode") == 0 and any(
                kw in str(i.get("title", "")).lower()
                for kw in _ONBOARDING_KEYWORDS
            )
        ]
        lines = [
            "# Customer Onboarding Pipeline — Live Tenant Accounts",
            "",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "In this template an engagement is a CRM account and blockers are",
            "Dynamics cases. Pass `customer_id` (e.g. CUST-1001) for the",
            "embedded demo view.",
            "",
            f"**Accounts:** {len(engagements)} | "
            f"**With open-case friction:** {len(with_friction)}",
            "",
            "| Customer | CSM | Since | Open Cases | ARR | Health | Go-Live |",
            "|----------|-----|-------|------------|-----|--------|---------|",
        ]
        for e in sorted(
            engagements, key=lambda x: x["open_cases"], reverse=True
        )[:10]:
            lines.append(
                f"| {e['name']} | {e['csm']} | {e['since']} | {e['open_cases']} "
                f"| n/a — enrichment seam | n/a — enrichment seam "
                f"| n/a — enrichment seam |"
            )
        if blockers:
            lines.append("")
            lines.append("## Onboarding Blockers (live cases)")
            lines.append("")
            for b in blockers:
                lines.append(
                    f"- {b.get('ticketnumber', '?')}: {b.get('title', 'untitled')} "
                    f"({b.get('customeridname', 'Unknown')})"
                )
        lines.append("")
        lines.append(
            "ARR, health scores, and go-live dates need your CS platform — "
            "wire it at the LIVE DATA SEAM."
        )
        return "\n".join(lines)

    def _onboarding_status(self, customer_id=None) -> str:
        if not customer_id:
            rows = _fetch_collection("accounts")
            if rows:
                incidents = _fetch_collection("incidents")
                engagements = [
                    _normalize_live_engagement(r, incidents)
                    for r in rows if r.get("name")
                ]
                if engagements:
                    return self._live_onboarding_status(engagements, incidents)
        data = _onboarding_status_summary()
        lines = [
            "# Customer Onboarding Pipeline",
            "",
            f"**Total Customers:** {data['total_customers']} | "
            f"**Pipeline ARR:** ${data['total_arr']:,}",
            "",
            f"- On Track: {data['on_track']}",
            f"- At Risk: {data['at_risk']}",
            f"- Critical: {data['critical']}",
            "",
            "| Customer | Plan | Health | Target Go-Live |",
            "|----------|------|--------|----------------|",
        ]
        for cid, info in data["customers"].items():
            lines.append(
                f"| {info['name']} | {info['plan']} | {info['health_score']} | {info['target_go_live']} |"
            )
        return "\n".join(lines)

    def _milestone_tracking(self) -> str:
        data = _milestone_tracking()
        lines = [
            "# Milestone Tracking",
            "",
            "| Customer | Completed | Progress | Blocked | Next Milestone |",
            "|----------|-----------|----------|---------|----------------|",
        ]
        for cid, m in data.items():
            blocked_str = ", ".join(m["blocked"]) if m["blocked"] else "None"
            lines.append(
                f"| {m['name']} | {m['completed']}/{m['total']} | {m['pct']}% "
                f"| {blocked_str} | {m['next_milestone'] or 'N/A'} |"
            )
        return "\n".join(lines)

    def _adoption_metrics(self) -> str:
        data = _adoption_metrics()
        lines = ["# Feature Adoption Metrics", ""]
        for cid, m in data.items():
            lines.append(f"## {m['name']}")
            lines.append(f"- Avg Adoption: {m['avg_adoption_pct']}%")
            lines.append(f"- Training: {m['training_pct']}%")
            lines.append(f"- User Activation: {m['activation_pct']}% ({m['active_users']}/{m['licensed_users']})")
            lines.append("")
            lines.append("| Feature | Adoption % |")
            lines.append("|---------|-----------|")
            for feat, pct in m["feature_adoption"].items():
                lines.append(f"| {feat.replace('_', ' ').title()} | {pct}% |")
            lines.append("")
        return "\n".join(lines)

    def _risk_flags(self) -> str:
        data = _risk_flags()
        if not data:
            return "# Risk Flags\n\nNo customers currently flagged."
        lines = ["# Customer Risk Flags", ""]
        for entry in data:
            lines.append(f"## {entry['name']} (ARR: ${entry['arr']:,})")
            lines.append(f"Health Score: {entry['health_score']}")
            for flag in entry["flags"]:
                lines.append(f"- {flag}")
            lines.append("")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = CustomerOnboardingAgent()
    print("=" * 60)
    print("EMBEDDED DEMO PIPELINE (works offline)")
    print(agent.perform(operation="onboarding_status", customer_id="CUST-1001"))
    print("\n" + "=" * 60)
    print("LIVE TENANT PIPELINE (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="onboarding_status"))
    for op in ["milestone_tracking", "adoption_metrics", "risk_flags"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
