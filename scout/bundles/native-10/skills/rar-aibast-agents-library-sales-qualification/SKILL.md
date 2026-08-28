---
name: "rar-aibast-agents-library-sales-qualification"
description: "Tiers live leads from a simulated Dynamics 365 tenant by CRM rating and value, with ICP/BANT tooling and an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/sales_qualification", "rar_sha256": "52d90ddf45bfd90e4e1e1218f74bfabfb9a9c8150af1a2dfb13084609f556ca7", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["b2b", "sales", "lead-qualification", "bant", "icp-scoring", "lead-routing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/sales_qualification`. The original RAPP
agent is preserved byte-for-byte in `sales_qualification_agent.py` and in the RCI capsule.

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

Sales Qualification Agent — a template you are meant to mutate.

Scores inbound leads against an Ideal Customer Profile, runs BANT
analysis, generates personalized outreach, routes leads to AEs, and
enforces SLA-based follow-up tracking.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM leads over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="score_leads") — the summary tiers live
     leads such as Priya Natarajan at "City of Alder Creek" (rated Hot
     in the CRM, $9,825 estimated).
  2. No network? Everything falls back to the embedded demo layer below
     (_LEADS / _ICP / _AE_TEAM) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SALES_QUALIFICATION_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_lead(). Firmographics
     (employees, industry, tech stack) and engagement signals are
     enrichment seams — wire ZoomInfo / 6sense there; ICP and BANT ops
     stay simulated until you do.

OPERATIONS
  score_leads | bant_analysis | create_outreach | assign_leads
  | setup_tracking | qualification_report | handoff_lead
  kwargs: operation (required), tier_filter, lead_id (handoff_lead)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "lead_id": {
      "description": "Exact lead ID for handoff_lead (e.g. 'L001')",
      "type": "string"
    },
    "operation": {
      "description": "The qualification operation to perform",
      "enum": [
        "score_leads",
        "bant_analysis",
        "create_outreach",
        "assign_leads",
        "setup_tracking",
        "qualification_report",
        "handoff_lead"
      ],
      "type": "string"
    },
    "tier_filter": {
      "description": "Optional tier filter: Hot, Warm, Nurture, Disqualified",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_qualification_agent.py` and embedded as the fenced Python below (sha256 52d90ddf45bfd90e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_qualification_agent.py` first:

```bash
python3 sales_qualification_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sales_qualification_agent.py   # or on stdin
python3 sales_qualification_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
Sales Qualification Agent — a template you are meant to mutate.

Scores inbound leads against an Ideal Customer Profile, runs BANT
analysis, generates personalized outreach, routes leads to AEs, and
enforces SLA-based follow-up tracking.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM leads over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="score_leads") — the summary tiers live
     leads such as Priya Natarajan at "City of Alder Creek" (rated Hot
     in the CRM, $9,825 estimated).
  2. No network? Everything falls back to the embedded demo layer below
     (_LEADS / _ICP / _AE_TEAM) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SALES_QUALIFICATION_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_lead(). Firmographics
     (employees, industry, tech stack) and engagement signals are
     enrichment seams — wire ZoomInfo / 6sense there; ICP and BANT ops
     stay simulated until you do.

OPERATIONS
  score_leads | bant_analysis | create_outreach | assign_leads
  | setup_tracking | qualification_report | handoff_lead
  kwargs: operation (required), tier_filter, lead_id (handoff_lead)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timedelta

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/sales_qualification",
    "version": "1.2.0",
    "display_name": "Sales Qualification",
    "description": "Tiers live leads from a simulated Dynamics 365 tenant by CRM rating and value, with ICP/BANT tooling and an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "lead-qualification", "bant", "icp-scoring", "lead-routing"],
    "category": "b2b_sales",
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
#   export SALES_QUALIFICATION_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_lead().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "SALES_QUALIFICATION_DATA_URL",
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


def _normalize_live_lead(row):
    """Project a Dynamics lead onto the shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not knowable from the CRM alone' and the
    renderers label it an enrichment seam (wire ZoomInfo / 6sense for
    firmographics and intent signals)."""
    quality = row.get("leadqualitycode@OData.Community.Display.V1.FormattedValue", "")
    state = row.get("statecode")
    if state == 2:
        tier = "Disqualified"
    else:
        tier = {"Hot": "Hot", "Warm": "Warm", "Cold": "Nurture"}.get(quality, "Nurture")
    return {
        "id": str(row.get("leadid", ""))[:8],
        "company": row.get("companyname", "Unknown"),
        "contact_name": row.get("fullname", "Unknown"),
        "subject": row.get("subject", ""),
        "estimated_amount": int(float(row.get("estimatedamount") or 0)),
        "crm_quality": quality or "n/a",
        "tier": tier,
        "owner": row.get("owneridname", ""),
        "employees": None,           # enrichment seam — wire ZoomInfo
        "industry": None,            # enrichment seam
        "tech_stack": None,          # enrichment seam
        "engagement_signals": None,  # enrichment seam — wire 6sense
        "_live": True,
    }


def _live_leads():
    """Live tenant leads normalized for this agent; [] when offline."""
    return [_normalize_live_lead(l) for l in _fetch_collection("leads")]


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# Stands in for CRM, ZoomInfo, 6sense, Clearbit, etc.
# ═══════════════════════════════════════════════════════════════

_ICP = {
    "size_weight": 0.20,
    "industry_weight": 0.25,
    "tech_fit_weight": 0.20,
    "budget_weight": 0.20,
    "authority_weight": 0.15,
    "ideal_employees_min": 200,
    "ideal_employees_max": 10000,
    "ideal_industries": ["Technology", "Financial Services", "Healthcare", "Manufacturing", "SaaS"],
    "ideal_tech": ["Salesforce", "AWS", "Snowflake", "Kubernetes", "Databricks", "Azure"],
    "budget_tiers": {"confirmed": 1.0, "planned": 0.7, "exploring": 0.4, "tbd": 0.2},
    "authority_tiers": {"C-Level": 1.0, "VP": 0.85, "Director": 0.7, "Manager": 0.5, "Individual": 0.3},
}

_AE_TEAM = [
    {"name": "Mike Rodriguez", "territory": "West", "specialty": "Enterprise Tech", "current_capacity_pct": 62, "max_leads": 12},
    {"name": "Sarah Kim", "territory": "East", "specialty": "Healthcare / FinServ", "current_capacity_pct": 55, "max_leads": 14},
    {"name": "James Chen", "territory": "Central", "specialty": "Manufacturing / Industrial", "current_capacity_pct": 70, "max_leads": 10},
    {"name": "Lisa Park", "territory": "West", "specialty": "Mid-Market SaaS", "current_capacity_pct": 48, "max_leads": 15},
    {"name": "David Okafor", "territory": "East", "specialty": "Enterprise FinServ", "current_capacity_pct": 58, "max_leads": 12},
]

_SLA_RULES = {
    "Hot":          {"response_hours": 4,  "escalation": "Manager alert + Slack DM",     "sequence": "Immediate call + personalized email"},
    "Warm":         {"response_hours": 24, "escalation": "Team channel alert",            "sequence": "Personalized email day 0, call day 1"},
    "Nurture":      {"response_hours": 48, "escalation": "Weekly digest flag",            "sequence": "3-email drip over 10 days"},
    "Disqualified": {"response_hours": 0,  "escalation": "None — routed to marketing",   "sequence": "Marketing nurture list"},
}

_LEADS = [
    {"id": "L001", "company": "TechFlow Industries",    "contact_name": "Sarah Nguyen",    "title": "VP Engineering",        "employees": 520,  "industry": "Technology",          "revenue": 85_000_000,   "source": "Trade Show",     "budget": "confirmed", "authority_level": "VP",        "need": "Consolidate 12 data sources into unified pipeline",              "timeline": "Q1",    "engagement_signals": ["Visited pricing page", "Attended booth demo twice", "Downloaded whitepaper"],                  "tech_stack": ["AWS", "Snowflake", "Kubernetes"]},
    {"id": "L002", "company": "Meridian Corp",          "contact_name": "James Walker",    "title": "CTO",                   "employees": 1200, "industry": "Healthcare",          "revenue": 340_000_000,  "source": "Trade Show",     "budget": "confirmed", "authority_level": "C-Level",   "need": "Replace legacy EHR integration layer",                          "timeline": "60 days", "engagement_signals": ["Asked technical questions at session", "Requested architecture doc"],                          "tech_stack": ["Azure", "Salesforce", "Databricks"]},
    {"id": "L003", "company": "Apex Solutions",         "contact_name": "Diana Reyes",     "title": "Director of IT",        "employees": 780,  "industry": "SaaS",                "revenue": 120_000_000,  "source": "Trade Show",     "budget": "planned",   "authority_level": "Director",  "need": "Displace incumbent vendor, contract ending Q1",                  "timeline": "Q1",    "engagement_signals": ["Competitor displacement signal", "Visited comparison page", "Booth conversation 15 min"],       "tech_stack": ["AWS", "Kubernetes", "Salesforce"]},
    {"id": "L004", "company": "Summit Technologies",    "contact_name": "Robert Kim",      "title": "VP Operations",         "employees": 450,  "industry": "Manufacturing",       "revenue": 95_000_000,   "source": "Trade Show",     "budget": "tbd",       "authority_level": "VP",        "need": "Scale production monitoring across 8 plants",                    "timeline": "90 days", "engagement_signals": ["Attended keynote", "Visited booth"],                                                           "tech_stack": ["Azure", "Salesforce"]},
    {"id": "L005", "company": "DataCorp Analytics",     "contact_name": "Emily Tran",      "title": "IT Manager",            "employees": 310,  "industry": "Technology",          "revenue": 52_000_000,   "source": "Trade Show",     "budget": "confirmed", "authority_level": "Manager",   "need": "Improve data pipeline efficiency by 40%",                        "timeline": "Q2",    "engagement_signals": ["Downloaded ROI calculator", "Signed up for trial"],                                            "tech_stack": ["Snowflake", "AWS"]},
    {"id": "L006", "company": "Greenfield Health",      "contact_name": "Maria Santos",    "title": "Chief Digital Officer",  "employees": 2800, "industry": "Healthcare",          "revenue": 620_000_000,  "source": "Webinar",        "budget": "confirmed", "authority_level": "C-Level",   "need": "Unified patient data platform across 14 facilities",             "timeline": "Q1",    "engagement_signals": ["Watched full webinar", "Booked follow-up meeting", "Downloaded case study"],                   "tech_stack": ["Azure", "Salesforce", "Snowflake"]},
    {"id": "L007", "company": "Pinnacle Financial",     "contact_name": "Kevin Okafor",    "title": "VP Technology",         "employees": 1800, "industry": "Financial Services",  "revenue": 450_000_000,  "source": "Referral",       "budget": "planned",   "authority_level": "VP",        "need": "Real-time fraud detection pipeline",                             "timeline": "60 days", "engagement_signals": ["Referral from existing customer", "Requested demo"],                                           "tech_stack": ["AWS", "Databricks", "Kubernetes"]},
    {"id": "L008", "company": "Orion Manufacturing",    "contact_name": "Thomas Park",     "title": "CTO",                   "employees": 3200, "industry": "Manufacturing",       "revenue": 780_000_000,  "source": "Trade Show",     "budget": "confirmed", "authority_level": "C-Level",   "need": "IoT data ingestion for predictive maintenance",                  "timeline": "Q1",    "engagement_signals": ["Booth demo", "Technical deep-dive session", "Exchanged business cards with CEO"],              "tech_stack": ["AWS", "Kubernetes", "Snowflake"]},
    {"id": "L009", "company": "Velocity SaaS",          "contact_name": "Rachel Green",    "title": "Director of Engineering","employees": 180,  "industry": "SaaS",                "revenue": 28_000_000,   "source": "Trade Show",     "budget": "exploring", "authority_level": "Director",  "need": "Microservices observability platform",                           "timeline": "Q2",    "engagement_signals": ["Visited booth briefly"],                                                                       "tech_stack": ["Kubernetes", "AWS"]},
    {"id": "L010", "company": "Atlas Logistics",        "contact_name": "Brian Murphy",    "title": "IT Director",           "employees": 950,  "industry": "Logistics",           "revenue": 210_000_000,  "source": "Trade Show",     "budget": "planned",   "authority_level": "Director",  "need": "Supply chain visibility dashboard",                              "timeline": "90 days", "engagement_signals": ["Attended breakout session", "Asked about integrations"],                                        "tech_stack": ["Salesforce", "Azure"]},
    {"id": "L011", "company": "Quantum Health Systems", "contact_name": "Jennifer Lee",    "title": "VP IT",                 "employees": 4100, "industry": "Healthcare",          "revenue": 1_200_000_000,"source": "Inbound Form",   "budget": "confirmed", "authority_level": "VP",        "need": "HIPAA-compliant analytics for 200+ providers",                   "timeline": "Q1",    "engagement_signals": ["Filled detailed form", "Requested pricing", "Downloaded compliance guide"],                    "tech_stack": ["Azure", "Snowflake", "Salesforce"]},
    {"id": "L012", "company": "Sterling Partners",      "contact_name": "Michael Chen",    "title": "Managing Director",     "employees": 85,   "industry": "Financial Services",  "revenue": 15_000_000,   "source": "Trade Show",     "budget": "tbd",       "authority_level": "C-Level",   "need": "Portfolio analytics automation",                                 "timeline": "Q3",    "engagement_signals": ["Brief booth visit"],                                                                           "tech_stack": ["Salesforce"]},
    {"id": "L013", "company": "NovaTech Solutions",     "contact_name": "Amanda Torres",   "title": "CTO",                   "employees": 650,  "industry": "Technology",          "revenue": 110_000_000,  "source": "Referral",       "budget": "confirmed", "authority_level": "C-Level",   "need": "Replace custom ETL with managed platform",                       "timeline": "60 days", "engagement_signals": ["Referral from board member", "Requested architecture review", "Downloaded migration guide"],     "tech_stack": ["AWS", "Snowflake", "Databricks", "Kubernetes"]},
    {"id": "L014", "company": "Cascade Energy",         "contact_name": "Daniel Wright",   "title": "VP Operations",         "employees": 1500, "industry": "Energy",              "revenue": 380_000_000,  "source": "Trade Show",     "budget": "planned",   "authority_level": "VP",        "need": "SCADA data integration for grid monitoring",                     "timeline": "Q2",    "engagement_signals": ["Attended demo", "Exchanged cards"],                                                            "tech_stack": ["Azure", "Salesforce"]},
    {"id": "L015", "company": "BlueWave Analytics",     "contact_name": "Samantha Hall",   "title": "Director Data Science",  "employees": 240,  "industry": "SaaS",                "revenue": 42_000_000,   "source": "Trade Show",     "budget": "exploring", "authority_level": "Director",  "need": "ML pipeline orchestration",                                      "timeline": "Q2",    "engagement_signals": ["Technical questions at booth", "Signed up for newsletter"],                                     "tech_stack": ["AWS", "Databricks", "Kubernetes"]},
    {"id": "L016", "company": "Pacific Mutual Insurance","contact_name": "Gregory Adams",  "title": "CIO",                   "employees": 5200, "industry": "Financial Services",  "revenue": 2_100_000_000,"source": "Executive Event","budget": "confirmed", "authority_level": "C-Level",   "need": "Claims processing automation with AI/ML",                        "timeline": "Q1",    "engagement_signals": ["1-on-1 executive meeting", "Requested proposal", "Site visit scheduled"],                       "tech_stack": ["AWS", "Salesforce", "Snowflake", "Databricks"]},
    {"id": "L017", "company": "Redstone Manufacturing", "contact_name": "Laura Martinez",  "title": "Plant Manager",         "employees": 2200, "industry": "Manufacturing",       "revenue": 540_000_000,  "source": "Trade Show",     "budget": "tbd",       "authority_level": "Manager",   "need": "Quality control data capture across lines",                      "timeline": "Q3",    "engagement_signals": ["Booth visit"],                                                                                 "tech_stack": ["Azure"]},
    {"id": "L018", "company": "Horizon Biotech",        "contact_name": "Andrew Liu",      "title": "VP Technology",         "employees": 380,  "industry": "Healthcare",          "revenue": 68_000_000,   "source": "Trade Show",     "budget": "planned",   "authority_level": "VP",        "need": "Lab data integration for clinical trials",                       "timeline": "90 days", "engagement_signals": ["Detailed booth conversation", "Downloaded case study", "Requested references"],                 "tech_stack": ["AWS", "Snowflake"]},
    {"id": "L019", "company": "Vertex Cloud",           "contact_name": "Nicole Brown",    "title": "CEO",                   "employees": 130,  "industry": "SaaS",                "revenue": 18_000_000,   "source": "Inbound Form",   "budget": "exploring", "authority_level": "C-Level",   "need": "Data infrastructure for new product line",                       "timeline": "Q3",    "engagement_signals": ["Form fill"],                                                                                   "tech_stack": ["AWS", "Kubernetes"]},
    {"id": "L020", "company": "Continental Logistics",  "contact_name": "Paul Wilson",     "title": "IT Manager",            "employees": 6800, "industry": "Logistics",           "revenue": 1_800_000_000,"source": "Trade Show",     "budget": "tbd",       "authority_level": "Manager",   "need": "Fleet telematics data warehousing",                              "timeline": "Q3",    "engagement_signals": ["Booth scan only"],                                                                             "tech_stack": ["Azure", "Salesforce"]},
    {"id": "L021", "company": "Nexus Health Network",   "contact_name": "Christina Park",  "title": "CMIO",                  "employees": 7500, "industry": "Healthcare",          "revenue": 3_200_000_000,"source": "Referral",       "budget": "confirmed", "authority_level": "C-Level",   "need": "Population health analytics across 30 hospitals",                "timeline": "Q1",    "engagement_signals": ["Executive referral", "Requested ROI model", "Reviewed case studies"],                           "tech_stack": ["Azure", "Snowflake", "Salesforce", "Databricks"]},
    {"id": "L022", "company": "Ironclad Security",      "contact_name": "Mark Stevens",    "title": "VP Engineering",        "employees": 420,  "industry": "Technology",          "revenue": 75_000_000,   "source": "Trade Show",     "budget": "planned",   "authority_level": "VP",        "need": "Security event log aggregation at scale",                        "timeline": "60 days", "engagement_signals": ["Attended technical session", "Downloaded architecture doc", "Booth demo"],                      "tech_stack": ["AWS", "Kubernetes", "Snowflake"]},
    {"id": "L023", "company": "Maple Financial Group",  "contact_name": "Karen Zhao",      "title": "SVP Operations",        "employees": 3400, "industry": "Financial Services",  "revenue": 920_000_000,  "source": "Executive Event","budget": "confirmed", "authority_level": "VP",        "need": "Regulatory reporting data pipeline",                             "timeline": "Q1",    "engagement_signals": ["Executive dinner attendee", "Scheduled follow-up call", "Compliance use case discussed"],       "tech_stack": ["Salesforce", "Snowflake", "Databricks"]},
    {"id": "L024", "company": "Bright Horizons Edu",    "contact_name": "Steven Miller",   "title": "CTO",                   "employees": 900,  "industry": "Education",           "revenue": 145_000_000,  "source": "Trade Show",     "budget": "exploring", "authority_level": "C-Level",   "need": "Student analytics platform consolidation",                       "timeline": "Q2",    "engagement_signals": ["Booth conversation", "Requested demo video"],                                                  "tech_stack": ["Azure", "Salesforce"]},
    {"id": "L025", "company": "Titan Aerospace",        "contact_name": "Angela White",    "title": "Director of IT",        "employees": 2600, "industry": "Manufacturing",       "revenue": 680_000_000,  "source": "Trade Show",     "budget": "planned",   "authority_level": "Director",  "need": "Supply chain data unification across 6 plants",                  "timeline": "90 days", "engagement_signals": ["Attended breakout", "Asked about security compliance"],                                         "tech_stack": ["AWS", "Salesforce", "Snowflake"]},
    {"id": "L026", "company": "CoreBridge Insurance",   "contact_name": "Jason Taylor",    "title": "VP Data & Analytics",   "employees": 4800, "industry": "Financial Services",  "revenue": 1_500_000_000,"source": "Inbound Form",   "budget": "confirmed", "authority_level": "VP",        "need": "Actuarial data lake modernization",                              "timeline": "60 days", "engagement_signals": ["Detailed form fill", "Requested customer references", "Downloaded ROI calculator"],             "tech_stack": ["AWS", "Snowflake", "Databricks", "Salesforce"]},
    {"id": "L027", "company": "Silverline Consulting",  "contact_name": "Tara Robinson",   "title": "Partner",               "employees": 60,   "industry": "Professional Services","revenue": 8_000_000,  "source": "Trade Show",     "budget": "tbd",       "authority_level": "C-Level",   "need": "Client reporting dashboard",                                     "timeline": "Q3",    "engagement_signals": ["Booth scan"],                                                                                  "tech_stack": ["Salesforce"]},
    {"id": "L028", "company": "Westfield Medical",      "contact_name": "Priya Sharma",    "title": "VP Clinical Informatics","employees": 1900, "industry": "Healthcare",          "revenue": 420_000_000,  "source": "Trade Show",     "budget": "planned",   "authority_level": "VP",        "need": "Clinical data warehouse for research analytics",                 "timeline": "Q1",    "engagement_signals": ["Booth demo", "Requested HIPAA compliance docs", "Technical Q&A"],                               "tech_stack": ["Azure", "Snowflake", "Salesforce"]},
    {"id": "L029", "company": "FusionTech Labs",        "contact_name": "Derek Johnson",   "title": "CTO",                   "employees": 290,  "industry": "SaaS",                "revenue": 48_000_000,   "source": "Referral",       "budget": "confirmed", "authority_level": "C-Level",   "need": "Migrate from on-prem Hadoop to cloud-native",                    "timeline": "60 days", "engagement_signals": ["Customer referral", "Requested migration assessment", "Downloaded migration guide"],             "tech_stack": ["AWS", "Kubernetes", "Databricks"]},
    {"id": "L030", "company": "National Grid Services", "contact_name": "Barbara Collins", "title": "IT Director",           "employees": 8200, "industry": "Energy",              "revenue": 4_500_000_000,"source": "Trade Show",     "budget": "tbd",       "authority_level": "Director",  "need": "Smart meter data aggregation platform",                          "timeline": "Q3",    "engagement_signals": ["Booth conversation", "Exchanged cards"],                                                       "tech_stack": ["Azure", "Salesforce"]},
    {"id": "L031", "company": "Elevate Commerce",       "contact_name": "Ryan Mitchell",   "title": "VP Engineering",        "employees": 350,  "industry": "Technology",          "revenue": 62_000_000,   "source": "Trade Show",     "budget": "planned",   "authority_level": "VP",        "need": "Real-time inventory sync across marketplace channels",           "timeline": "90 days", "engagement_signals": ["Attended session", "Downloaded integration guide"],                                             "tech_stack": ["AWS", "Snowflake", "Kubernetes"]},
    {"id": "L032", "company": "Summit Health Partners", "contact_name": "Lisa Nakamura",   "title": "Chief Analytics Officer","employees": 5600, "industry": "Healthcare",          "revenue": 1_600_000_000,"source": "Executive Event","budget": "confirmed", "authority_level": "C-Level",   "need": "Enterprise analytics platform for value-based care",             "timeline": "Q1",    "engagement_signals": ["1-on-1 exec meeting", "Requested business case template", "Reviewed 3 case studies"],           "tech_stack": ["Azure", "Snowflake", "Salesforce", "Databricks"]},
    {"id": "L033", "company": "Pioneer Robotics",       "contact_name": "Alex Petrov",     "title": "Director of Automation", "employees": 410,  "industry": "Manufacturing",       "revenue": 88_000_000,   "source": "Trade Show",     "budget": "exploring", "authority_level": "Director",  "need": "Robotics telemetry data pipeline",                               "timeline": "Q2",    "engagement_signals": ["Booth demo", "Technical questions"],                                                           "tech_stack": ["AWS", "Kubernetes"]},
    {"id": "L034", "company": "Heritage Bank",          "contact_name": "Sandra Lee",      "title": "SVP Technology",        "employees": 2100, "industry": "Financial Services",  "revenue": 580_000_000,  "source": "Trade Show",     "budget": "planned",   "authority_level": "VP",        "need": "Anti-money laundering data pipeline modernization",              "timeline": "60 days", "engagement_signals": ["Detailed booth conversation", "Requested compliance references"],                               "tech_stack": ["AWS", "Salesforce", "Snowflake"]},
    {"id": "L035", "company": "ClearView Optics",       "contact_name": "Nathan Ford",     "title": "IT Manager",            "employees": 160,  "industry": "Manufacturing",       "revenue": 22_000_000,   "source": "Trade Show",     "budget": "tbd",       "authority_level": "Manager",   "need": "Quality inspection image data storage",                          "timeline": "Q3",    "engagement_signals": ["Booth scan only"],                                                                             "tech_stack": ["Azure"]},
    {"id": "L036", "company": "Axiom Data Systems",     "contact_name": "Michelle Yang",   "title": "CEO",                   "employees": 95,   "industry": "SaaS",                "revenue": 12_000_000,   "source": "Trade Show",     "budget": "exploring", "authority_level": "C-Level",   "need": "Data pipeline as a service offering",                            "timeline": "Q3",    "engagement_signals": ["Brief booth stop"],                                                                            "tech_stack": ["AWS"]},
    {"id": "L037", "company": "Metro Health Alliance",  "contact_name": "David Nguyen",    "title": "VP Data Engineering",   "employees": 3800, "industry": "Healthcare",          "revenue": 890_000_000,  "source": "Webinar",        "budget": "planned",   "authority_level": "VP",        "need": "Real-time patient flow analytics for 18 facilities",             "timeline": "90 days", "engagement_signals": ["Webinar attendee", "Downloaded guide", "Requested pricing"],                                    "tech_stack": ["Azure", "Snowflake", "Salesforce"]},
    {"id": "L038", "company": "Vanguard Logistics",     "contact_name": "Carlos Mendez",   "title": "CTO",                   "employees": 1400, "industry": "Logistics",           "revenue": 320_000_000,  "source": "Trade Show",     "budget": "planned",   "authority_level": "C-Level",   "need": "Cross-border shipment tracking data platform",                   "timeline": "Q2",    "engagement_signals": ["Attended demo", "Booth conversation"],                                                         "tech_stack": ["AWS", "Salesforce"]},
    {"id": "L039", "company": "TrueNorth Energy",       "contact_name": "Helen Foster",    "title": "VP Technology",         "employees": 2900, "industry": "Energy",              "revenue": 750_000_000,  "source": "Trade Show",     "budget": "tbd",       "authority_level": "VP",        "need": "Renewable energy asset performance analytics",                   "timeline": "Q3",    "engagement_signals": ["Keynote attendee", "Brief booth visit"],                                                       "tech_stack": ["Azure", "Salesforce"]},
    {"id": "L040", "company": "Paragon Pharma",         "contact_name": "William Chang",   "title": "Director of R&D IT",    "employees": 1100, "industry": "Healthcare",          "revenue": 290_000_000,  "source": "Trade Show",     "budget": "exploring", "authority_level": "Director",  "need": "Genomics data pipeline for drug discovery",                      "timeline": "Q2",    "engagement_signals": ["Technical session attendee", "Downloaded whitepaper"],                                          "tech_stack": ["AWS", "Databricks"]},
    {"id": "L041", "company": "Crestline Financial",    "contact_name": "Patricia Adams",  "title": "Chief Data Officer",    "employees": 6200, "industry": "Financial Services",  "revenue": 2_800_000_000,"source": "Referral",       "budget": "confirmed", "authority_level": "C-Level",   "need": "Enterprise data mesh architecture implementation",               "timeline": "Q1",    "engagement_signals": ["Board-level referral", "Requested executive briefing", "Scheduled site visit"],                 "tech_stack": ["AWS", "Snowflake", "Databricks", "Kubernetes", "Salesforce"]},
    {"id": "L042", "company": "Bridgepoint Retail",     "contact_name": "Scott Thompson",  "title": "IT Manager",            "employees": 720,  "industry": "Retail",              "revenue": 165_000_000,  "source": "Trade Show",     "budget": "tbd",       "authority_level": "Manager",   "need": "POS data aggregation for analytics",                             "timeline": "Q3",    "engagement_signals": ["Booth scan"],                                                                                  "tech_stack": ["Salesforce"]},
    {"id": "L043", "company": "Sapphire Biomedical",    "contact_name": "Rebecca Foster",  "title": "VP Informatics",        "employees": 480,  "industry": "Healthcare",          "revenue": 76_000_000,   "source": "Trade Show",     "budget": "planned",   "authority_level": "VP",        "need": "Clinical trial data harmonization",                              "timeline": "90 days", "engagement_signals": ["Booth demo", "Requested case study", "Technical Q&A"],                                          "tech_stack": ["AWS", "Snowflake"]},
    {"id": "L044", "company": "Forge Industrial",       "contact_name": "Christopher Hall","title": "Plant Director",         "employees": 3500, "industry": "Manufacturing",       "revenue": 920_000_000,  "source": "Trade Show",     "budget": "exploring", "authority_level": "Director",  "need": "Predictive maintenance data platform",                           "timeline": "Q2",    "engagement_signals": ["Attended session", "Brief booth visit"],                                                       "tech_stack": ["Azure", "Salesforce"]},
    {"id": "L045", "company": "Luminary Wealth",        "contact_name": "Jessica Wang",    "title": "VP Technology",         "employees": 250,  "industry": "Financial Services",  "revenue": 38_000_000,   "source": "Trade Show",     "budget": "exploring", "authority_level": "VP",        "need": "Client portfolio reporting automation",                          "timeline": "Q3",    "engagement_signals": ["Booth conversation"],                                                                          "tech_stack": ["Salesforce", "AWS"]},
]

_LEADS_BY_ID = {lead["id"]: lead for lead in _LEADS}


# ═══════════════════════════════════════════════════════════════
# HELPERS — real computation, synthetic inputs
# ═══════════════════════════════════════════════════════════════

def _icp_score(lead):
    """Compute ICP fit score (0-100) from weighted criteria."""
    # Size score
    emp = lead["employees"]
    if _ICP["ideal_employees_min"] <= emp <= _ICP["ideal_employees_max"]:
        size_score = 100
    elif emp < _ICP["ideal_employees_min"]:
        size_score = max(10, int((emp / _ICP["ideal_employees_min"]) * 100))
    else:
        size_score = max(40, 100 - int((emp - _ICP["ideal_employees_max"]) / 200))

    # Industry score
    industry_score = 100 if lead["industry"] in _ICP["ideal_industries"] else 30

    # Tech fit score
    overlap = len(set(lead["tech_stack"]) & set(_ICP["ideal_tech"]))
    tech_score = min(100, int((overlap / max(len(_ICP["ideal_tech"]), 1)) * 150))

    # Budget score
    budget_score = int(_ICP["budget_tiers"].get(lead["budget"], 0.2) * 100)

    # Authority score
    authority_score = int(_ICP["authority_tiers"].get(lead["authority_level"], 0.3) * 100)

    total = (
        size_score * _ICP["size_weight"]
        + industry_score * _ICP["industry_weight"]
        + tech_score * _ICP["tech_fit_weight"]
        + budget_score * _ICP["budget_weight"]
        + authority_score * _ICP["authority_weight"]
    )
    return min(100, max(0, int(total)))


def _bant_scores(lead):
    """Score each BANT dimension independently (0-100)."""
    budget_map = {"confirmed": 95, "planned": 70, "exploring": 40, "tbd": 15}
    b = budget_map.get(lead["budget"], 15)

    authority_map = {"C-Level": 95, "VP": 80, "Director": 60, "Manager": 40, "Individual": 20}
    a = authority_map.get(lead["authority_level"], 20)

    n = min(100, 50 + len(lead["need"]) // 3 + len(lead["engagement_signals"]) * 8)

    timeline_val = lead["timeline"].upper()
    if "60" in timeline_val or "Q1" in timeline_val:
        t = 90
    elif "90" in timeline_val:
        t = 70
    elif "Q2" in timeline_val:
        t = 55
    else:
        t = 25

    composite = int(b * 0.30 + a * 0.25 + n * 0.25 + t * 0.20)
    return {"budget": b, "authority": a, "need": n, "timeline": t, "composite": composite}


def _tier_lead(icp_score, bant_composite):
    """Assign tier from combined ICP and BANT scores."""
    combined = int(icp_score * 0.55 + bant_composite * 0.45)
    if combined >= 88:
        return "Hot", combined
    elif combined >= 73:
        return "Warm", combined
    elif combined >= 55:
        return "Nurture", combined
    else:
        return "Disqualified", combined


def _match_ae(lead, team):
    """Route lead to best AE by specialty keyword match and capacity."""
    industry = lead["industry"].lower()
    best_ae = None
    best_score = -1
    for ae in team:
        spec = ae["specialty"].lower()
        score = 0
        if industry in spec:
            score += 50
        if "enterprise" in spec and lead["employees"] >= 1000:
            score += 20
        elif "mid-market" in spec and lead["employees"] < 1000:
            score += 20
        if "finserv" in spec and "financial" in industry:
            score += 30
        if "tech" in spec and industry in ("technology", "saas"):
            score += 25
        if "health" in spec and "healthcare" in industry:
            score += 30
        if "manufactur" in spec and "manufacturing" in industry:
            score += 30
        capacity_bonus = max(0, (100 - ae["current_capacity_pct"]) // 5)
        score += capacity_bonus
        if score > best_score:
            best_score = score
            best_ae = ae
    return best_ae


def _generate_outreach(lead, tier, icp_score):
    """Build personalized outreach elements from lead context."""
    company = lead["company"]
    first_name = lead["contact_name"].split()[0]
    need_short = lead["need"][:60]

    if tier == "Hot":
        subject = f"Following up on our {lead['source'].lower()} conversation, {first_name}"
        hook = f'You mentioned "{need_short}" — we have a proven path to solve this in {lead["timeline"]}.'
        cta = "15-minute deep dive this week?"
    elif tier == "Warm":
        subject = f"{company} + DataSync: {need_short[:40]}"
        hook = f"Teams like yours at {company} are solving {need_short.lower()} with our platform."
        cta = "Quick call to explore fit?"
    else:
        subject = f"Resource: solving {need_short[:35].lower()} at scale"
        hook = f"Thought you would find our latest guide on {lead['industry'].lower()} data challenges useful."
        cta = "Reply if you would like a walkthrough."

    return {"subject": subject, "hook": hook, "cta": cta}


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class SalesQualificationAgent(BasicAgent):
    """
    Scores, qualifies, and routes inbound leads.

    Operations:
        score_leads          - ICP scoring + tiering for all leads
        bant_analysis        - BANT breakdown for top-tier leads
        create_outreach      - Personalized email outreach per lead
        assign_leads         - Route to AEs by territory/expertise/capacity
        setup_tracking       - SLA rules and escalation configuration
        qualification_report - Full pipeline summary with conversion targets
        handoff_lead         - route one exact lead with CRM/Teams receipts
    """

    def __init__(self):
        self.name = "SalesQualificationAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "score_leads", "bant_analysis",
                            "create_outreach", "assign_leads",
                            "setup_tracking", "qualification_report",
                            "handoff_lead",
                        ],
                        "description": "The qualification operation to perform",
                    },
                    "tier_filter": {
                        "type": "string",
                        "description": "Optional tier filter: Hot, Warm, Nurture, Disqualified",
                    },
                    "lead_id": {
                        "type": "string",
                        "description": "Exact lead ID for handoff_lead (e.g. 'L001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)
        self._scored = None

    def _ensure_scored(self):
        """Lazily compute and cache scored leads."""
        if self._scored is not None:
            return self._scored
        results = []
        for lead in _LEADS:
            icp = _icp_score(lead)
            bant = _bant_scores(lead)
            tier, combined = _tier_lead(icp, bant["composite"])
            results.append({**lead, "icp_score": icp, "bant": bant, "tier": tier, "combined_score": combined})
        results.sort(key=lambda x: x["combined_score"], reverse=True)
        self._scored = results
        return results

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "score_leads")
        if op == "handoff_lead":
            return self._handoff_lead(kwargs.get("lead_id"))
        dispatch = {
            "score_leads": self._score_leads,
            "bant_analysis": self._bant_analysis,
            "create_outreach": self._create_outreach,
            "assign_leads": self._assign_leads,
            "setup_tracking": self._setup_tracking,
            "qualification_report": self._qualification_report,
        }
        handler = dispatch.get(op)
        if not handler:
            return json.dumps({"status": "error", "message": f"Unknown operation: {op}"})
        return handler(kwargs.get("tier_filter"))

    def _handoff_lead(self, lead_id):
        lead = _LEADS_BY_ID.get(lead_id)
        if lead is None:
            return json.dumps({
                "status": "error",
                "message": f"Unknown lead_id: {lead_id!r}",
                "valid_lead_ids": ", ".join(sorted(_LEADS_BY_ID)),
            })
        scored = next(item for item in self._ensure_scored() if item["id"] == lead_id)
        ae = _match_ae(scored, _AE_TEAM)
        outreach = _generate_outreach(scored, scored["tier"], scored["icp_score"])
        sla = _SLA_RULES[scored["tier"]]
        receipt = {
            "status": "simulated",
            "lead_id": lead_id,
            "company": scored["company"],
            "tier": scored["tier"],
            "combined_score": scored["combined_score"],
            "bant_score": scored["bant"]["composite"],
            "assigned_ae": ae["name"] if ae else "Marketing nurture",
            "outreach_subject": outreach["subject"],
            "response_sla_hours": sla["response_hours"],
            "crm_assignment_id": f"sim-d365-lead-{lead_id.lower()}",
            "teams_message_id": f"sim-teams-sla-{lead_id.lower()}",
        }
        return "**Qualified Lead Handoff Receipt**\n\n```json\n" + json.dumps(receipt, indent=2) + "\n```"

    # ── score_leads (flagship: prefers LIVE tenant, falls back) ──
    def _score_leads(self, tier_filter):
        live = _live_leads()
        if live:
            tiers = {"Hot": [], "Warm": [], "Nurture": [], "Disqualified": []}
            for l in live:
                tiers[l["tier"]].append(l)
            actions = {"Hot": "Immediate AE handoff", "Warm": "SDR qualification call",
                       "Nurture": "Automated email sequence", "Disqualified": "Marketing nurture list"}
            summary = (
                "| Tier | Leads | Est. Value | Recommended Action |\n"
                "|---|---|---|---|\n"
            )
            for tier_name in ["Hot", "Warm", "Nurture", "Disqualified"]:
                group = tiers[tier_name]
                total = sum(l["estimated_amount"] for l in group)
                summary += f"| {tier_name} | {len(group)} | ${total:,} | {actions[tier_name]} |\n"

            top_hot = sorted(tiers["Hot"], key=lambda l: -l["estimated_amount"])[:5]
            top_lines = ""
            for i, lead in enumerate(top_hot, 1):
                top_lines += (f"{i}. **{lead['company']}** — ${lead['estimated_amount']:,} — "
                              f"{lead['contact_name']}, {lead['subject']}\n")

            filtered = ""
            if tier_filter and tier_filter in tiers:
                filtered = f"\n**{tier_filter} Leads Detail:**\n\n"
                filtered += "| Company | Contact | Est. Value | CRM Rating | Signals |\n|---|---|---|---|---|\n"
                for l in tiers[tier_filter]:
                    filtered += (f"| {l['company']} | {l['contact_name']} | "
                                 f"${l['estimated_amount']:,} | {l['crm_quality']} | "
                                 f"n/a — enrichment seam |\n")

            return (
                f"**Lead Qualification Summary — {len(live)} LIVE Leads** "
                f"(Static Dynamics 365 tenant)\n\n"
                f"Tiers come from the CRM lead rating (Hot/Warm/Cold) and lead "
                f"state; ICP fit and BANT scoring activate when you wire "
                f"ZoomInfo / 6sense at the LIVE DATA SEAM.\n\n"
                f"{summary}\n"
                f"**Top Hot Leads:**\n{top_lines}"
                f"{filtered}\n"
                "Source: [Live Dynamics 365 leads]\n"
                "Agents: LeadEnrichmentAgent, ICPMatchingAgent"
            )
        scored = self._ensure_scored()
        tiers = {"Hot": [], "Warm": [], "Nurture": [], "Disqualified": []}
        for s in scored:
            tiers[s["tier"]].append(s)

        summary = (
            "| Tier | Leads | Avg Score | Recommended Action |\n"
            "|---|---|---|---|\n"
        )
        actions = {"Hot": "Immediate AE handoff", "Warm": "SDR qualification call",
                   "Nurture": "Automated email sequence", "Disqualified": "Marketing nurture list"}
        for tier_name in ["Hot", "Warm", "Nurture", "Disqualified"]:
            group = tiers[tier_name]
            avg = int(sum(l["combined_score"] for l in group) / max(len(group), 1))
            summary += f"| {tier_name} | {len(group)} | {avg}/100 | {actions[tier_name]} |\n"

        top_hot = tiers["Hot"][:5]
        top_lines = ""
        for i, lead in enumerate(top_hot, 1):
            top_lines += f"{i}. **{lead['company']}** — Score: {lead['combined_score']} — {lead['contact_name']}, {lead['title']}, {lead['need'][:50]}\n"

        filtered = ""
        if tier_filter and tier_filter in tiers:
            filtered = f"\n**{tier_filter} Leads Detail:**\n\n"
            filtered += "| Company | Contact | Score | Industry | Signals |\n|---|---|---|---|---|\n"
            for l in tiers[tier_filter]:
                sigs = ", ".join(l["engagement_signals"][:2])
                filtered += f"| {l['company']} | {l['contact_name']} | {l['combined_score']} | {l['industry']} | {sigs} |\n"

        return (
            f"**Lead Qualification Summary — {len(scored)} Leads Scored**\n\n"
            f"{summary}\n"
            f"**Top Hot Leads:**\n{top_lines}"
            f"{filtered}\n"
            "Source: [CRM + ZoomInfo + 6sense Intent Data]\n"
            "Agents: LeadEnrichmentAgent, ICPMatchingAgent"
        )

    # ── bant_analysis ─────────────────────────────────────────
    def _bant_analysis(self, tier_filter):
        scored = self._ensure_scored()
        hot = [s for s in scored if s["tier"] == "Hot"]
        targets = hot[:8]

        table = "| Lead | Budget | Authority | Need | Timeline | BANT Score |\n|---|---|---|---|---|---|\n"
        for lead in targets:
            b = lead["bant"]
            budget_label = f"{lead['budget'].capitalize()} ({b['budget']})"
            auth_label = f"{lead['authority_level']} ({b['authority']})"
            need_label = f"{b['need']}"
            time_label = f"{lead['timeline']} ({b['timeline']})"
            table += f"| {lead['company']} | {budget_label} | {auth_label} | {need_label} | {time_label} | {b['composite']} |\n"

        signals = "\n**Strongest Engagement Signals:**\n"
        for lead in targets[:3]:
            sigs = ", ".join(lead["engagement_signals"])
            signals += f"- **{lead['company']}**: {sigs}\n"

        risks = "\n**Risk Flags:**\n"
        for lead in targets:
            if lead["bant"]["budget"] < 50:
                risks += f"- {lead['company']}: Budget not confirmed ({lead['budget']})\n"
            if lead["bant"]["authority"] < 60:
                risks += f"- {lead['company']}: Decision maker not yet engaged ({lead['authority_level']})\n"

        return (
            f"**BANT Analysis — Top {len(targets)} Hot Leads**\n\n"
            f"{table}{signals}{risks}\n"
            "Source: [CRM + Booth Interactions + Intent Data]\n"
            "Agents: BANTScoringAgent"
        )

    # ── create_outreach ───────────────────────────────────────
    def _create_outreach(self, tier_filter):
        scored = self._ensure_scored()
        tier = tier_filter if tier_filter in ("Hot", "Warm") else "Hot"
        targets = [s for s in scored if s["tier"] == tier][:5]

        blocks = ""
        for lead in targets:
            o = _generate_outreach(lead, lead["tier"], lead["icp_score"])
            blocks += (
                f"**{lead['company']} Outreach:**\n\n"
                f"**Subject:** {o['subject']}\n\n"
                f"**Hook:** \"{o['hook']}\"\n\n"
                f"**CTA:** {o['cta']}\n\n---\n\n"
            )

        sequence = (
            "**Sequence Cadence (all leads):**\n"
            "- Day 0: Personalized email (above)\n"
            "- Day 1: LinkedIn connection + note\n"
            "- Day 2: Phone attempt #1\n"
            "- Day 3: Value content email\n"
            "- Day 5: Phone attempt #2\n"
        )

        return (
            f"**Personalized Outreach — {len(targets)} {tier} Leads**\n\n"
            f"{blocks}{sequence}\n"
            "Source: [Content Library + Booth Notes + LinkedIn]\n"
            "Agents: PersonalizedOutreachAgent"
        )

    # ── assign_leads ──────────────────────────────────────────
    def _assign_leads(self, tier_filter):
        scored = self._ensure_scored()
        actionable = [s for s in scored if s["tier"] in ("Hot", "Warm")]
        assignments = {ae["name"]: {"ae": ae, "leads": [], "value": 0} for ae in _AE_TEAM}

        for lead in actionable:
            ae = _match_ae(lead, _AE_TEAM)
            if ae:
                est_value = int(lead["revenue"] * 0.001)
                assignments[ae["name"]]["leads"].append(lead)
                assignments[ae["name"]]["value"] += est_value

        summary_table = "| AE | Leads | Est. Pipeline | Specialty Match | Capacity |\n|---|---|---|---|---|\n"
        for ae_name, data in assignments.items():
            if data["leads"]:
                summary_table += (
                    f"| {ae_name} | {len(data['leads'])} | ${data['value']:,} | "
                    f"{data['ae']['specialty']} | {data['ae']['current_capacity_pct']}% |\n"
                )

        detail = "\n**Assignment Detail:**\n"
        for ae_name, data in assignments.items():
            for lead in data["leads"][:3]:
                est_value = int(lead["revenue"] * 0.001)
                detail += f"- {lead['company']} (${est_value:,}) -> {ae_name} ({data['ae']['specialty']})\n"

        handoff = (
            "\n**Handoff Package per Lead:**\n"
            "- Lead score + BANT summary\n"
            "- Booth interaction / source notes\n"
            "- Personalized email draft\n"
            "- Recommended talk track\n"
        )

        return (
            f"**Lead Assignments — {len(actionable)} Leads Routed**\n\n"
            f"{summary_table}{detail}{handoff}\n"
            "Source: [Territory Rules + Capacity Dashboard]\n"
            "Agents: LeadRoutingAgent"
        )

    # ── setup_tracking ────────────────────────────────────────
    def _setup_tracking(self, tier_filter):
        scored = self._ensure_scored()
        tiers = {"Hot": 0, "Warm": 0, "Nurture": 0, "Disqualified": 0}
        for s in scored:
            tiers[s["tier"]] += 1

        sla_table = "| Lead Tier | Response SLA | Escalation | Sequence |\n|---|---|---|---|\n"
        for tier_name in ["Hot", "Warm", "Nurture", "Disqualified"]:
            rule = _SLA_RULES[tier_name]
            hrs = f"{rule['response_hours']}h" if rule["response_hours"] > 0 else "N/A"
            sla_table += f"| {tier_name} ({tiers[tier_name]} leads) | {hrs} | {rule['escalation']} | {rule['sequence']} |\n"

        monitoring = (
            "\n**Monitoring Activated:**\n"
            "- Real-time dashboard tracking all 45 leads\n"
            "- Slack alerts when SLA at risk (50% time elapsed)\n"
            "- Daily summary report at 9:00 AM\n"
            "- Weekly conversion tracking by tier\n"
        )

        escalation = (
            "\n**Escalation Rules:**\n"
            "- Hot lead no contact in 4h: Manager DM + email\n"
            "- Warm lead no contact in 24h: Team channel alert\n"
            "- Any lead no response after full sequence: Re-route to alternate AE\n"
            "- Meeting booked: Auto-update opportunity stage in CRM\n"
        )

        return (
            f"**SLA Tracking Configuration — {len(scored)} Leads**\n\n"
            f"{sla_table}{monitoring}{escalation}\n"
            "Source: [SLA Engine + Notification System]\n"
            "Agents: SLAMonitoringAgent"
        )

    # ── qualification_report ──────────────────────────────────
    def _qualification_report(self, tier_filter):
        scored = self._ensure_scored()
        tiers = {"Hot": [], "Warm": [], "Nurture": [], "Disqualified": []}
        for s in scored:
            tiers[s["tier"]].append(s)

        hot_value = sum(int(l["revenue"] * 0.001) for l in tiers["Hot"])
        warm_value = sum(int(l["revenue"] * 0.001) for l in tiers["Warm"])
        total_pipeline = hot_value + warm_value

        summary_table = (
            "| Metric | Value |\n|---|---|\n"
            f"| Total leads scored | {len(scored)} |\n"
            f"| Hot leads | {len(tiers['Hot'])} |\n"
            f"| Warm leads | {len(tiers['Warm'])} |\n"
            f"| Nurture leads | {len(tiers['Nurture'])} |\n"
            f"| Disqualified | {len(tiers['Disqualified'])} |\n"
            f"| Hot pipeline value | ${hot_value:,} |\n"
            f"| Warm pipeline value | ${warm_value:,} |\n"
            f"| **Total qualified pipeline** | **${total_pipeline:,}** |\n"
        )

        industry_counts = {}
        for s in scored:
            ind = s["industry"]
            industry_counts[ind] = industry_counts.get(ind, 0) + 1
        industry_table = "\n**Leads by Industry:**\n\n| Industry | Count | Hot | Warm |\n|---|---|---|---|\n"
        for ind in sorted(industry_counts, key=industry_counts.get, reverse=True):
            hot_ct = sum(1 for l in tiers["Hot"] if l["industry"] == ind)
            warm_ct = sum(1 for l in tiers["Warm"] if l["industry"] == ind)
            industry_table += f"| {ind} | {industry_counts[ind]} | {hot_ct} | {warm_ct} |\n"

        conversion = (
            "\n**Conversion Targets:**\n"
            f"- Hot to meeting: 40% ({int(len(tiers['Hot']) * 0.4)} meetings)\n"
            f"- Meeting to opportunity: 60% ({int(len(tiers['Hot']) * 0.4 * 0.6)} opportunities)\n"
            f"- Warm to meeting: 20% ({int(len(tiers['Warm']) * 0.2)} meetings)\n"
            f"- Expected pipeline from hot leads: ${int(hot_value * 0.4 * 0.6):,}\n"
        )

        actions = (
            "\n**Immediate Actions:**\n"
            f"1. {len(tiers['Hot'])} hot leads — AE outreach within 4 hours\n"
            f"2. {len(tiers['Warm'])} warm leads — SDR calls today/tomorrow\n"
            f"3. {len(tiers['Nurture'])} nurture leads — Email sequence starts automatically\n"
            f"4. {len(tiers['Disqualified'])} disqualified — Routed to marketing nurture\n"
        )

        return (
            f"**Qualification Report — Full Pipeline Summary**\n\n"
            f"{summary_table}{industry_table}{conversion}{actions}\n"
            "Source: [All Qualification Systems]\n"
            "Agents: QualificationReportAgent (orchestrating all agents)"
        )


if __name__ == "__main__":
    agent = SalesQualificationAgent()
    print("=" * 70)
    print("LIVE TENANT LEADS (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="score_leads"))
    print()
    print("=" * 70)
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="bant_analysis"))
    print()
    print("=" * 70)
    print(agent.perform(operation="qualification_report"))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
