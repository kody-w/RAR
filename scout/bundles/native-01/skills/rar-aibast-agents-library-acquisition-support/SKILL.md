---
name: "rar-aibast-agents-library-acquisition-support"
description: "Tracks acquisitions from a live simulated Dynamics 365 tenant with FAR/DFAR checklists and vendor scoring, plus an offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/acquisition_support", "rar_sha256": "b470bfbe595b3f5c1b01f2d7454c359a20be6ac3714db588a97743a9969fdf13", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["acquisition", "FAR", "DFAR", "procurement", "vendor-evaluation", "federal"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/acquisition_support`. The original RAPP
agent is preserved byte-for-byte in `acquisition_support_agent.py` and in the RCI capsule.

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

Acquisition Support Agent — a template you are meant to mutate.

Provides acquisition lifecycle support including FAR/DFAR compliance,
vendor evaluation, procurement timelines, and compliance checklists
for federal acquisition professionals.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live procurement records over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a Dynamics opportunity is reinterpreted as an
     acquisition action: its estimated value drives real FAR-threshold
     math — e.g. "Prairie Wind Energy Cooperative — Mobile workstation
     expansion" at $9,450 estimated value.
     Try: perform(operation="acquisition_overview")
  2. No network? Everything falls back to the embedded demo layer below
     (FAR_REQUIREMENTS / VENDOR_PROPOSALS / PROCUREMENT_TIMELINES) —
     the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ACQUISITION_SUPPORT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your contract-writing
     system), or replace _fetch_collection() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_acquisition() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output (CAGE
     codes, NAICS, milestone dates) are where you wire SAM.gov and your
     acquisition system.

OPERATIONS
  acquisition_overview | vendor_evaluation | compliance_checklist
  | timeline_tracker
  kwargs: operation (required), project_id, vendor_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "enum": [
        "acquisition_overview",
        "vendor_evaluation",
        "compliance_checklist",
        "timeline_tracker"
      ],
      "type": "string"
    },
    "project_id": {
      "type": "string"
    },
    "vendor_id": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `acquisition_support_agent.py` and embedded as the fenced Python below (sha256 b470bfbe595b3f5c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `acquisition_support_agent.py` first:

```bash
python3 acquisition_support_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 acquisition_support_agent.py   # or on stdin
python3 acquisition_support_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Acquisition Support Agent — a template you are meant to mutate.

Provides acquisition lifecycle support including FAR/DFAR compliance,
vendor evaluation, procurement timelines, and compliance checklists
for federal acquisition professionals.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live procurement records over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a Dynamics opportunity is reinterpreted as an
     acquisition action: its estimated value drives real FAR-threshold
     math — e.g. "Prairie Wind Energy Cooperative — Mobile workstation
     expansion" at $9,450 estimated value.
     Try: perform(operation="acquisition_overview")
  2. No network? Everything falls back to the embedded demo layer below
     (FAR_REQUIREMENTS / VENDOR_PROPOSALS / PROCUREMENT_TIMELINES) —
     the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ACQUISITION_SUPPORT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your contract-writing
     system), or replace _fetch_collection() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_acquisition() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output (CAGE
     codes, NAICS, milestone dates) are where you wire SAM.gov and your
     acquisition system.

OPERATIONS
  acquisition_overview | vendor_evaluation | compliance_checklist
  | timeline_tracker
  kwargs: operation (required), project_id, vendor_id
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/acquisition_support",
    "version": "1.1.0",
    "display_name": "Acquisition Support Agent",
    "description": "Tracks acquisitions from a live simulated Dynamics 365 tenant with FAR/DFAR checklists and vendor scoring, plus an offline fallback.",
    "author": "AIBAST",
    "tags": ["acquisition", "FAR", "DFAR", "procurement", "vendor-evaluation", "federal"],
    "category": "federal_government",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export ACQUISITION_SUPPORT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your acquisition-system client.
# Downstream code only needs the fields produced by
# _normalize_live_acquisition().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "ACQUISITION_SUPPORT_DATA_URL",
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


def _normalize_live_acquisition(row):
    """Project a Dynamics opportunity onto the acquisition shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not available from CRM
    alone' and the renderers label it as an enrichment seam. In this
    template a Dynamics opportunity is reinterpreted as an acquisition
    action; its estimated value drives real FAR-threshold math."""
    close = row.get("estimatedclosedate")
    return {
        "title": row.get("name", "untitled"),
        "office": row.get("parentaccountidname", "Unknown"),
        "estimated_value": float(row.get("estimatedvalue") or 0),
        "stage": row.get("stepname", "n/a"),
        "status": {0: "open", 1: "won", 2: "lost"}.get(row.get("statecode"), "unknown"),
        "target_award": str(close)[:10] if close else None,
        "acquisition_type": None,  # enrichment seam — wire your contract-writing system
        "cage_code": None,          # enrichment seam — wire SAM.gov
        "_live": True,
    }


def _live_acquisitions():
    """Live tenant acquisition actions; [] when offline."""
    return [_normalize_live_acquisition(o) for o in _fetch_collection("opportunities")]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

FAR_REQUIREMENTS = {
    "FAR 15.3": {
        "title": "Source Selection",
        "description": "Policies and procedures for negotiated competitive acquisitions",
        "key_provisions": [
            "Evaluation factors must be stated in solicitation",
            "Cost/price evaluation required for all competitive acquisitions",
            "Past performance must be evaluated for acquisitions over $1M",
        ],
        "threshold": 1000000,
    },
    "FAR 19.5": {
        "title": "Small Business Set-Asides",
        "description": "Requirements for setting aside acquisitions for small businesses",
        "key_provisions": [
            "Acquisitions between $10K-$250K reserved for small business",
            "Market research required to identify small business capability",
            "SBA size standards apply by NAICS code",
        ],
        "threshold": 250000,
    },
    "FAR 12.6": {
        "title": "Commercial Item Streamlining",
        "description": "Streamlined procedures for acquiring commercial items",
        "key_provisions": [
            "Use of simplified evaluation procedures permitted",
            "Standard commercial warranties acceptable",
            "Reduced documentation requirements for commercial items",
        ],
        "threshold": 7500000,
    },
    "FAR 8.4": {
        "title": "Federal Supply Schedules",
        "description": "Ordering procedures under GSA Federal Supply Schedules",
        "key_provisions": [
            "Three or more quotes required for orders over micro-purchase",
            "Best value determination required",
            "Statement of work required for services",
        ],
        "threshold": 0,
    },
}

DFAR_SUPPLEMENTS = {
    "DFARS 252.204-7012": {
        "title": "Safeguarding Covered Defense Information",
        "applicability": "All DoD contracts with CDI",
        "compliance_standard": "NIST SP 800-171",
        "assessment_required": True,
    },
    "DFARS 252.204-7021": {
        "title": "CMMC Requirements",
        "applicability": "DoD contracts requiring CMMC certification",
        "compliance_standard": "CMMC Level 2",
        "assessment_required": True,
    },
    "DFARS 215.403-1": {
        "title": "Certified Cost or Pricing Data",
        "applicability": "Acquisitions exceeding $2M threshold",
        "compliance_standard": "TINA",
        "assessment_required": False,
    },
}

VENDOR_PROPOSALS = {
    "VP-2025-001": {
        "vendor": "Meridian Defense Systems",
        "cage_code": "3AB47",
        "naics": "541512",
        "proposal_amount": 4750000,
        "technical_score": 88.5,
        "past_performance_rating": "Satisfactory",
        "small_business": False,
        "cmmc_level": 2,
        "delivery_days": 180,
    },
    "VP-2025-002": {
        "vendor": "Patriot Tech Solutions",
        "cage_code": "7KF92",
        "naics": "541512",
        "proposal_amount": 3980000,
        "technical_score": 91.2,
        "past_performance_rating": "Highly Satisfactory",
        "small_business": True,
        "cmmc_level": 2,
        "delivery_days": 210,
    },
    "VP-2025-003": {
        "vendor": "Centurion Analytics Group",
        "cage_code": "5DL83",
        "naics": "541519",
        "proposal_amount": 5120000,
        "technical_score": 85.0,
        "past_performance_rating": "Satisfactory",
        "small_business": False,
        "cmmc_level": 3,
        "delivery_days": 150,
    },
    "VP-2025-004": {
        "vendor": "Osprey Federal Services",
        "cage_code": "1RM56",
        "naics": "541512",
        "proposal_amount": 4200000,
        "technical_score": 79.8,
        "past_performance_rating": "Neutral",
        "small_business": True,
        "cmmc_level": 1,
        "delivery_days": 240,
    },
}

EVALUATION_CRITERIA = {
    "technical_approach": {"weight": 35, "max_score": 100},
    "past_performance": {"weight": 25, "max_score": 100},
    "cost_price": {"weight": 20, "max_score": 100},
    "management_approach": {"weight": 10, "max_score": 100},
    "small_business_plan": {"weight": 10, "max_score": 100},
}

PROCUREMENT_TIMELINES = {
    "PRJ-FY25-101": {
        "title": "Enterprise Cloud Migration Services",
        "acquisition_type": "Full & Open Competition",
        "estimated_value": 12500000,
        "milestones": {
            "acquisition_plan_approval": {"target": "2025-02-15", "actual": "2025-02-18", "status": "complete"},
            "market_research": {"target": "2025-03-01", "actual": "2025-03-01", "status": "complete"},
            "solicitation_release": {"target": "2025-04-15", "actual": None, "status": "in_progress"},
            "proposal_due": {"target": "2025-05-30", "actual": None, "status": "pending"},
            "evaluation_complete": {"target": "2025-07-15", "actual": None, "status": "pending"},
            "award_decision": {"target": "2025-08-01", "actual": None, "status": "pending"},
        },
    },
    "PRJ-FY25-102": {
        "title": "Cybersecurity Operations Center Staffing",
        "acquisition_type": "8(a) Sole Source",
        "estimated_value": 3200000,
        "milestones": {
            "acquisition_plan_approval": {"target": "2025-01-10", "actual": "2025-01-10", "status": "complete"},
            "market_research": {"target": "2025-01-25", "actual": "2025-01-28", "status": "complete"},
            "solicitation_release": {"target": "2025-02-20", "actual": "2025-02-22", "status": "complete"},
            "proposal_due": {"target": "2025-03-15", "actual": "2025-03-14", "status": "complete"},
            "evaluation_complete": {"target": "2025-04-01", "actual": None, "status": "in_progress"},
            "award_decision": {"target": "2025-04-15", "actual": None, "status": "pending"},
        },
    },
    "PRJ-FY25-103": {
        "title": "Data Analytics Platform Modernization",
        "acquisition_type": "GSA Schedule",
        "estimated_value": 850000,
        "milestones": {
            "acquisition_plan_approval": {"target": "2025-03-01", "actual": None, "status": "in_progress"},
            "market_research": {"target": "2025-03-20", "actual": None, "status": "pending"},
            "solicitation_release": {"target": "2025-04-10", "actual": None, "status": "pending"},
            "proposal_due": {"target": "2025-04-25", "actual": None, "status": "pending"},
            "evaluation_complete": {"target": "2025-05-10", "actual": None, "status": "pending"},
            "award_decision": {"target": "2025-05-20", "actual": None, "status": "pending"},
        },
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _compute_weighted_score(proposal):
    """Compute weighted evaluation score for a vendor proposal."""
    pp_scores = {"Highly Satisfactory": 95, "Satisfactory": 80, "Neutral": 60, "Unsatisfactory": 30}
    tech = proposal["technical_score"]
    pp = pp_scores.get(proposal["past_performance_rating"], 50)
    cost_efficiency = max(0, 100 - (proposal["proposal_amount"] / 100000))
    sb_bonus = 90 if proposal["small_business"] else 60
    mgmt = min(100, tech * 0.9)
    weighted = (
        tech * EVALUATION_CRITERIA["technical_approach"]["weight"]
        + pp * EVALUATION_CRITERIA["past_performance"]["weight"]
        + cost_efficiency * EVALUATION_CRITERIA["cost_price"]["weight"]
        + mgmt * EVALUATION_CRITERIA["management_approach"]["weight"]
        + sb_bonus * EVALUATION_CRITERIA["small_business_plan"]["weight"]
    ) / 100.0
    return round(weighted, 2)


def _get_applicable_far(value):
    """Return applicable FAR clauses based on acquisition value."""
    applicable = []
    for ref, data in FAR_REQUIREMENTS.items():
        if value >= data["threshold"]:
            applicable.append((ref, data["title"]))
    return applicable


def _timeline_progress(project):
    """Calculate milestone completion percentage."""
    milestones = project["milestones"]
    total = len(milestones)
    complete = sum(1 for m in milestones.values() if m["status"] == "complete")
    return round((complete / total) * 100, 1) if total else 0.0


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class AcquisitionSupportAgent(BasicAgent):
    """Federal acquisition support agent for procurement lifecycle management."""

    def __init__(self):
        self.name = "AcquisitionSupportAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Acquisition Support Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "acquisition_overview",
                            "vendor_evaluation",
                            "compliance_checklist",
                            "timeline_tracker",
                        ],
                    },
                    "project_id": {"type": "string"},
                    "vendor_id": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "acquisition_overview")
        dispatch = {
            "acquisition_overview": self._acquisition_overview,
            "vendor_evaluation": self._vendor_evaluation,
            "compliance_checklist": self._compliance_checklist,
            "timeline_tracker": self._timeline_tracker,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    # -- Operations ----------------------------------------------------------

    def _acquisition_overview(self, **kwargs) -> str:
        live = _live_acquisitions()
        if live:
            open_actions = [a for a in live if a["status"] == "open"]
            total_value = sum(a["estimated_value"] for a in live if a["status"] == "open")
            lines = ["# Federal Acquisition Overview (live tenant data)\n"]
            lines.append("## Acquisition Actions\n")
            lines.append("| Action | Office | Est. Value | Stage | Status | Target Award | FAR Basis |")
            lines.append("|---|---|---|---|---|---|---|")
            for a in sorted(live, key=lambda x: (x["status"] != "open", -x["estimated_value"])):
                far = _get_applicable_far(a["estimated_value"])
                far_str = far[-1][0] if far else "Micro-purchase"
                lines.append(
                    f"| {a['title']} | {a['office']} | ${a['estimated_value']:,.0f} "
                    f"| {a['stage']} | {a['status'].upper()} | {a['target_award'] or 'n/a'} "
                    f"| {far_str} |"
                )
            lines.append(f"\n**Open Actions:** {len(open_actions)} | "
                         f"**Open Pipeline Value:** ${total_value:,.0f}")
            lines.append("**Acquisition type / CAGE data:** n/a — enrichment seam "
                         "(wire your contract-writing system and SAM.gov)")
            lines.append("\n## Applicable Regulatory Framework\n")
            for ref, data in FAR_REQUIREMENTS.items():
                lines.append(f"- **{ref}** — {data['title']}")
            for ref, data in DFAR_SUPPLEMENTS.items():
                lines.append(f"- **{ref}** — {data['title']}")
            lines.append("\n_Source: live Static Dynamics 365 tenant (opportunities). An "
                         "opportunity is reinterpreted as an acquisition action; the FAR "
                         "basis is computed from its real estimated value._")
            return "\n".join(lines)

        lines = ["# Federal Acquisition Overview (embedded demo data — offline)\n"]
        lines.append("## Active Procurements\n")
        lines.append("| Project ID | Title | Type | Est. Value | Progress |")
        lines.append("|---|---|---|---|---|")
        for pid, proj in PROCUREMENT_TIMELINES.items():
            pct = _timeline_progress(proj)
            lines.append(
                f"| {pid} | {proj['title']} | {proj['acquisition_type']} "
                f"| ${proj['estimated_value']:,.0f} | {pct}% |"
            )
        total_value = sum(p["estimated_value"] for p in PROCUREMENT_TIMELINES.values())
        lines.append(f"\n**Total Pipeline Value:** ${total_value:,.0f}")
        lines.append(f"\n**Active Vendor Proposals:** {len(VENDOR_PROPOSALS)}")
        lines.append("\n## Applicable Regulatory Framework\n")
        for ref, data in FAR_REQUIREMENTS.items():
            lines.append(f"- **{ref}** — {data['title']}")
        for ref, data in DFAR_SUPPLEMENTS.items():
            lines.append(f"- **{ref}** — {data['title']}")
        return "\n".join(lines)

    def _vendor_evaluation(self, **kwargs) -> str:
        vendor_id = kwargs.get("vendor_id")
        if vendor_id and vendor_id in VENDOR_PROPOSALS:
            vp = VENDOR_PROPOSALS[vendor_id]
            score = _compute_weighted_score(vp)
            lines = [f"# Vendor Evaluation: {vp['vendor']}\n"]
            lines.append(f"- **Proposal ID:** {vendor_id}")
            lines.append(f"- **CAGE Code:** {vp['cage_code']}")
            lines.append(f"- **NAICS:** {vp['naics']}")
            lines.append(f"- **Proposal Amount:** ${vp['proposal_amount']:,.0f}")
            lines.append(f"- **Technical Score:** {vp['technical_score']}/100")
            lines.append(f"- **Past Performance:** {vp['past_performance_rating']}")
            lines.append(f"- **Small Business:** {'Yes' if vp['small_business'] else 'No'}")
            lines.append(f"- **CMMC Level:** {vp['cmmc_level']}")
            lines.append(f"- **Delivery:** {vp['delivery_days']} days")
            lines.append(f"\n**Weighted Composite Score:** {score}")
            return "\n".join(lines)

        lines = ["# Vendor Evaluation Summary\n"]
        lines.append("| Proposal | Vendor | Amount | Technical | PP Rating | Weighted Score |")
        lines.append("|---|---|---|---|---|---|")
        ranked = []
        for vid, vp in VENDOR_PROPOSALS.items():
            score = _compute_weighted_score(vp)
            ranked.append((vid, vp, score))
        ranked.sort(key=lambda x: x[2], reverse=True)
        for vid, vp, score in ranked:
            lines.append(
                f"| {vid} | {vp['vendor']} | ${vp['proposal_amount']:,.0f} "
                f"| {vp['technical_score']} | {vp['past_performance_rating']} | {score} |"
            )
        lines.append(f"\n**Recommendation:** {ranked[0][1]['vendor']} (highest weighted score: {ranked[0][2]})")
        return "\n".join(lines)

    def _compliance_checklist(self, **kwargs) -> str:
        project_id = kwargs.get("project_id", "PRJ-FY25-101")
        proj = PROCUREMENT_TIMELINES.get(project_id, list(PROCUREMENT_TIMELINES.values())[0])
        value = proj["estimated_value"]
        applicable_far = _get_applicable_far(value)
        lines = [f"# Compliance Checklist: {proj['title']}\n"]
        lines.append(f"**Estimated Value:** ${value:,.0f}\n")
        lines.append("## FAR Requirements\n")
        for ref, title in applicable_far:
            provisions = FAR_REQUIREMENTS[ref]["key_provisions"]
            lines.append(f"### {ref} — {title}\n")
            for p in provisions:
                lines.append(f"- [ ] {p}")
            lines.append("")
        lines.append("## DFARS Supplements\n")
        for ref, data in DFAR_SUPPLEMENTS.items():
            lines.append(f"### {ref} — {data['title']}\n")
            lines.append(f"- **Applicability:** {data['applicability']}")
            lines.append(f"- **Standard:** {data['compliance_standard']}")
            status = "Required" if data["assessment_required"] else "Not Required"
            lines.append(f"- **Assessment:** {status}")
            lines.append("")
        return "\n".join(lines)

    def _timeline_tracker(self, **kwargs) -> str:
        lines = ["# Procurement Timeline Tracker\n"]
        for pid, proj in PROCUREMENT_TIMELINES.items():
            pct = _timeline_progress(proj)
            lines.append(f"## {pid}: {proj['title']}\n")
            lines.append(f"- **Type:** {proj['acquisition_type']}")
            lines.append(f"- **Value:** ${proj['estimated_value']:,.0f}")
            lines.append(f"- **Completion:** {pct}%\n")
            lines.append("| Milestone | Target | Actual | Status |")
            lines.append("|---|---|---|---|")
            for mname, mdata in proj["milestones"].items():
                display = mname.replace("_", " ").title()
                actual = mdata["actual"] or "—"
                status_icon = {"complete": "Done", "in_progress": "In Progress", "pending": "Pending"}
                lines.append(
                    f"| {display} | {mdata['target']} | {actual} "
                    f"| {status_icon.get(mdata['status'], mdata['status'])} |"
                )
            lines.append("")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = AcquisitionSupportAgent()
    print("=" * 60)
    print("LIVE TENANT ACQUISITIONS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="acquisition_overview"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO EVALUATIONS (works offline)")
    print(agent.perform(operation="vendor_evaluation"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="vendor_evaluation", vendor_id="VP-2025-002"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="compliance_checklist", project_id="PRJ-FY25-101"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="timeline_tracker"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
