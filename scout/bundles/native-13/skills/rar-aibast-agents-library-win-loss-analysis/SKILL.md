---
name: "rar-aibast-agents-library-win-loss-analysis"
description: "Computes win/loss stats from live closed deals in a simulated Dynamics 365 tenant, with recovery models and an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/win_loss_analysis", "rar_sha256": "9506127641a61d589a0b1966fc7570b0b425bdc90968bc886e1eec84be143c6c", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["b2b", "sales", "win-loss", "competitive-intel", "revenue-recovery"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/win_loss_analysis`. The original RAPP
agent is preserved byte-for-byte in `win_loss_analysis_agent.py` and in the RCI capsule.

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

Win/Loss Analysis Agent — a template you are meant to mutate.

Analyzes closed opportunities for win-rate trends, loss patterns,
competitor insights, counter-strategies, revenue recovery projections,
and board-ready presentation frameworks.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live closed opportunities over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="win_loss_overview") — win rate and deal
     values are computed from real closed records such as the won
     "Foxglove Learning — Secure print rollout" ($13,500 actual).
  2. No network? Everything falls back to the embedded demo layer below
     (_Q3_OPPORTUNITIES / _Q2_OPPORTUNITIES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     WIN_LOSS_ANALYSIS_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_closed_deal().
     Loss reasons and competitor attribution are enrichment seams — wire
     your win/loss survey platform there; the pattern/recovery ops stay
     simulated until you do.

OPERATIONS
  win_loss_overview | root_cause_analysis | counter_strategies
  | revenue_impact | board_presentation | action_summary | publish_findings
  kwargs: operation (required), quarter, analysis_id (publish_findings)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "analysis_id": {
      "description": "Exact analysis ID for publish_findings (e.g. 'Q3-COMPETITORX')",
      "type": "string"
    },
    "operation": {
      "description": "The analysis to perform",
      "enum": [
        "win_loss_overview",
        "root_cause_analysis",
        "counter_strategies",
        "revenue_impact",
        "board_presentation",
        "action_summary",
        "publish_findings"
      ],
      "type": "string"
    },
    "quarter": {
      "description": "Quarter to analyze (default: Q3 current)",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `win_loss_analysis_agent.py` and embedded as the fenced Python below (sha256 9506127641a61d58…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `win_loss_analysis_agent.py` first:

```bash
python3 win_loss_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 win_loss_analysis_agent.py   # or on stdin
python3 win_loss_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
Win/Loss Analysis Agent — a template you are meant to mutate.

Analyzes closed opportunities for win-rate trends, loss patterns,
competitor insights, counter-strategies, revenue recovery projections,
and board-ready presentation frameworks.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live closed opportunities over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="win_loss_overview") — win rate and deal
     values are computed from real closed records such as the won
     "Foxglove Learning — Secure print rollout" ($13,500 actual).
  2. No network? Everything falls back to the embedded demo layer below
     (_Q3_OPPORTUNITIES / _Q2_OPPORTUNITIES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     WIN_LOSS_ANALYSIS_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_closed_deal().
     Loss reasons and competitor attribution are enrichment seams — wire
     your win/loss survey platform there; the pattern/recovery ops stay
     simulated until you do.

OPERATIONS
  win_loss_overview | root_cause_analysis | counter_strategies
  | revenue_impact | board_presentation | action_summary | publish_findings
  kwargs: operation (required), quarter, analysis_id (publish_findings)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/win_loss_analysis",
    "version": "1.2.0",
    "display_name": "Win/Loss Analysis",
    "description": "Computes win/loss stats from live closed deals in a simulated Dynamics 365 tenant, with recovery models and an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "win-loss", "competitive-intel", "revenue-recovery"],
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
#   export WIN_LOSS_ANALYSIS_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_closed_deal().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "WIN_LOSS_ANALYSIS_DATA_URL",
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


def _normalize_live_closed_deal(row):
    """Project a closed Dynamics opportunity onto the shape this agent
    uses. THIS is the contract your replacement data source must meet — a
    dict with these keys. None means 'not knowable from the CRM alone'
    and the renderers label it an enrichment seam (loss reasons and
    competitor attribution come from your win/loss survey platform)."""
    won = row.get("statecode") == 1
    value = float((row.get("actualvalue") if won else row.get("estimatedvalue")) or 0)
    return {
        "name": row.get("name", "Unknown"),
        "account": row.get("parentaccountidname", "Unknown"),
        "value": int(value),
        "outcome": "won" if won else "lost",
        "competitor_lost_to": None,  # enrichment seam — wire win/loss surveys
        "loss_reason": None,         # enrichment seam
        "owner": row.get("owneridname", ""),
        "closed_on": str(row.get("actualclosedate") or "")[:10],
        "_live": True,
    }


def _live_closed_deals():
    """Live closed opportunities (won or lost); [] when offline."""
    return [_normalize_live_closed_deal(o)
            for o in _fetch_collection("opportunities")
            if o.get("statecode") in (1, 2)]


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# Stands in for CRM, Gong, Win/Loss Survey System, etc.
# ═══════════════════════════════════════════════════════════════

_LOSS_REASONS = [
    "security_certs", "enterprise_references", "pricing",
    "feature_gaps", "no_decision", "relationship",
]

_COMPETITORS = {
    "CompetitorX": {"strength": "Enterprise security certs (FedRAMP, ISO 27001)", "weakness": "Poor UX, slow implementation"},
    "CompetitorY": {"strength": "Low price point, bundled analytics",            "weakness": "Limited API, weak support"},
    "CompetitorZ": {"strength": "Industry-specific templates",                    "weakness": "No multi-cloud, small team"},
}

# Q3: 127 closed opportunities
_Q3_OPPORTUNITIES = [
    # ── Enterprise Won ──
    {"name": "Apex Financial Platform",   "account": "Apex Financial",      "value": 620000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Pinnacle Data Migration",   "account": "Pinnacle Corp",       "value": 540000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Orion Cloud Expansion",     "account": "Orion Industries",    "value": 480000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Atlas Infra Modernization", "account": "Atlas Group",         "value": 710000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Summit ERP Integration",    "account": "Summit Enterprises",  "value": 390000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Crestview Analytics",       "account": "Crestview Inc",       "value": 310000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    # ── Enterprise Lost to CompetitorX ──
    {"name": "TechCorp Secure Platform",  "account": "TechCorp Industries", "value": 890000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "GlobalBank Core Upgrade",   "account": "Global Banking Corp", "value": 780000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "SecureHealth Compliance",   "account": "SecureHealth Inc",    "value": 650000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "FedFirst Platform",         "account": "FedFirst Solutions",  "value": 720000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Metro Gov Modernization",   "account": "Metro Government",    "value": 580000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "NexGen Data Suite",         "account": "NexGen Corp",         "value": 510000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "PrimeCo Digital Transform", "account": "PrimeCo",             "value": 440000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "enterprise_references", "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Vantage Cloud Migration",   "account": "Vantage Ltd",         "value": 520000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "enterprise_references", "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Beacon ERP Overhaul",       "account": "Beacon Systems",      "value": 390000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "enterprise_references", "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "IronClad Security Suite",   "account": "IronClad Defense",    "value": 670000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Fortress Data Vault",       "account": "Fortress Financial",  "value": 600000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Titanium Platform Deal",    "account": "Titanium Holdings",   "value": 430000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "enterprise_references", "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "QuantumEdge Infra",         "account": "QuantumEdge",         "value": 350000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "pricing",            "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Sterling Cloud Services",   "account": "Sterling Group",      "value": 480000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "pricing",            "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Nexus Analytics Platform",  "account": "Nexus Corp",          "value": 290000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "feature_gaps",       "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "OmniTech Suite",            "account": "OmniTech Inc",        "value": 380000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "pricing",            "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "CipherOne Security",        "account": "CipherOne",           "value": 550000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "AlphaWave Data",            "account": "AlphaWave",           "value": 420000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "enterprise_references", "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "SentinelOps Platform",      "account": "SentinelOps",         "value": 310000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "feature_gaps",       "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    # ── Lost to CompetitorY ──
    {"name": "BrightPath Analytics",      "account": "BrightPath Co",       "value": 185000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Cascade Data Services",     "account": "Cascade Inc",         "value": 210000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Evergreen SaaS Upgrade",    "account": "Evergreen LLC",       "value": 175000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Clearwater Cloud",          "account": "Clearwater Inc",      "value": 230000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "StreamLine Ops",            "account": "StreamLine Co",       "value": 195000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "PeakView Integration",      "account": "PeakView Inc",       "value": 260000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "250K-500K"},
    {"name": "Horizon Data Platform",     "account": "Horizon Ltd",         "value": 150000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Ridgeline Cloud Suite",     "account": "Ridgeline Corp",      "value": 280000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "enterprise_references", "segment": "mid-market", "deal_size_bucket": "250K-500K"},
    {"name": "Trailhead Analytics",       "account": "Trailhead Inc",       "value": 140000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Summit Edge Platform",      "account": "Summit Edge",         "value": 165000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "relationship",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "NorthStar CRM Deal",        "account": "NorthStar Co",        "value": 220000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "WildPine Integration",      "account": "WildPine Ltd",        "value": 190000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "CoralReef Data Migration",  "account": "CoralReef Inc",       "value": 155000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "StoneArch Platform",        "account": "StoneArch Corp",      "value": 245000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "BlueSky SaaS Renewal",      "account": "BlueSky Solutions",   "value": 130000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "relationship",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "GreenField Ops",            "account": "GreenField Inc",      "value": 170000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "IronBridge Analytics",      "account": "IronBridge LLC",      "value": 200000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "SilverLake Cloud",          "account": "SilverLake Co",       "value": 225000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "enterprise_references", "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    # ── No Decision ──
    {"name": "Redwood Budget Freeze",     "account": "Redwood Corp",        "value": 320000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Pinecrest Reorg",           "account": "Pinecrest Inc",       "value": 180000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Willow Delayed Decision",   "account": "Willow LLC",          "value": 250000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Birchwood Stall",           "account": "Birchwood Co",        "value": 145000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "OakHill Budget Hold",       "account": "OakHill Partners",    "value": 410000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Cedarpoint Priority Shift", "account": "Cedarpoint Inc",      "value": 270000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "250K-500K"},
    {"name": "Aspen Internal Conflict",   "account": "Aspen Group",         "value": 190000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Maple Reorg Delay",         "account": "Maple Industries",    "value": 360000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "ElmGrove Postponed",        "account": "ElmGrove Ltd",        "value": 135000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Spruce Budget Cut",         "account": "Spruce Systems",      "value": 160000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Juniper Priority Shift",    "account": "Juniper Corp",        "value": 200000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "CypressWood Stall",         "account": "CypressWood Inc",     "value": 95000,  "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "smb",        "deal_size_bucket": "<100K"},
    # ── Other Losses (CompetitorZ / relationship) ──
    {"name": "PolarStar Niche Fit",       "account": "PolarStar Inc",       "value": 175000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "CoastalTech Templates",     "account": "CoastalTech",         "value": 210000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "TideLine Industry Pack",    "account": "TideLine Corp",       "value": 165000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "HarborView Vertical",       "account": "HarborView LLC",      "value": 140000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Anchor Relationship Play",  "account": "Anchor Corp",         "value": 195000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "relationship",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "LightHouse Legacy",         "account": "LightHouse Inc",      "value": 150000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "relationship",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Portside Deal",             "account": "Portside LLC",        "value": 120000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "pricing",            "segment": "smb",        "deal_size_bucket": "100K-250K"},
    {"name": "BreakWater Eval",           "account": "BreakWater Co",       "value": 88000,  "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "pricing",            "segment": "smb",        "deal_size_bucket": "<100K"},
    # ── Mid-Market & SMB Won ──
    {"name": "Velocity SaaS Upgrade",     "account": "Velocity Co",         "value": 185000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Spark Analytics Deal",      "account": "Spark Corp",          "value": 210000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Pulse Data Services",       "account": "Pulse Inc",           "value": 165000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Drift Cloud Platform",      "account": "Drift Technologies",  "value": 140000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Zenith Integration",        "account": "Zenith LLC",          "value": 120000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Nimbus Cloud Deal",         "account": "Nimbus Corp",         "value": 195000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Helix SaaS Expansion",      "account": "Helix Inc",           "value": 230000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Prism Data Migration",      "account": "Prism Ltd",           "value": 175000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Aether Platform",           "account": "Aether Solutions",    "value": 155000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Cirrus Ops Tooling",        "account": "Cirrus Co",           "value": 92000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Ember Starter Pack",        "account": "Ember LLC",           "value": 78000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Flint Quick Deploy",        "account": "Flint Corp",          "value": 85000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Nova Small Biz",            "account": "Nova Inc",            "value": 65000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Quasar Rapid Start",        "account": "Quasar Ltd",          "value": 72000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Photon Pilot",              "account": "Photon Co",           "value": 55000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Echo SMB Cloud",            "account": "Echo Systems",        "value": 48000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Stratos Integration",       "account": "Stratos Inc",         "value": 260000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "250K-500K"},
    {"name": "Vortex Platform",           "account": "Vortex Corp",         "value": 240000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Matrix Data Suite",         "account": "Matrix LLC",          "value": 190000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Dynamo Cloud Ops",          "account": "Dynamo Co",           "value": 275000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "250K-500K"},
    {"name": "Warp Speed Deploy",         "account": "Warp Inc",            "value": 145000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Comet Expansion",           "account": "Comet Solutions",     "value": 110000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Orbit Analytics",           "account": "Orbit Ltd",           "value": 98000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Luna Starter",              "account": "Luna Corp",           "value": 42000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Astro Mini Deploy",         "account": "Astro LLC",           "value": 58000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Cosmic Quick Start",        "account": "Cosmic Inc",          "value": 35000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Nebula Cloud",              "account": "Nebula Co",           "value": 68000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Pulsar SMB",               "account": "Pulsar Ltd",          "value": 46000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    # ── Additional Enterprise Lost (relationship / misc) ──
    {"name": "Horizon Ent Relationship",  "account": "Horizon Ent",         "value": 410000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "relationship",       "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Meridian Legacy Vendor",    "account": "Meridian Corp",       "value": 340000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "relationship",       "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Zenon Pricing Squeeze",     "account": "Zenon Inc",           "value": 280000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "pricing",            "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    # ── Additional Mid-Market Lost ──
    {"name": "RapidScale Eval",           "account": "RapidScale Co",       "value": 160000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    # ── Additional SMB Won ──
    {"name": "Pixel Quick Deploy",        "account": "Pixel Corp",          "value": 52000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Byte Starter Pack",         "account": "Byte LLC",            "value": 38000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Atom SMB Platform",         "account": "Atom Inc",            "value": 44000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Quark Cloud Lite",          "account": "Quark Co",            "value": 62000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    # ── Additional Q3 deals to reach ~127 total ──
    {"name": "Radiant Enterprise Suite",  "account": "Radiant Corp",        "value": 560000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Cobalt Security Platform",  "account": "Cobalt Inc",          "value": 490000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Sapphire Data Vault",       "account": "Sapphire Ltd",        "value": 620000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "enterprise_references", "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Topaz Cloud Migration",     "account": "Topaz Group",         "value": 340000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "pricing",            "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Jade Analytics Platform",   "account": "Jade Corp",           "value": 275000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "feature_gaps",       "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Onyx Infra Deal",           "account": "Onyx Industries",     "value": 385000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "enterprise_references", "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Garnet Platform Upgrade",   "account": "Garnet Solutions",    "value": 450000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Pearl Managed Services",    "account": "Pearl Inc",           "value": 310000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Opal Cloud Expansion",      "account": "Opal Ltd",            "value": 420000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Ruby Analytics Suite",      "account": "Ruby Corp",           "value": 180000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Amber Data Connect",        "account": "Amber Inc",           "value": 155000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Citrine SaaS Deploy",       "account": "Citrine LLC",         "value": 125000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Agate Cloud Ops",           "account": "Agate Co",            "value": 88000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Beryl Quick Start",         "account": "Beryl Ltd",           "value": 72000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Coral SMB Platform",        "account": "Coral Corp",          "value": 55000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Diamond Micro Deploy",      "account": "Diamond Inc",         "value": 42000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "FlintEdge Analytics",       "account": "FlintEdge Co",        "value": 195000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Granite Cloud Services",    "account": "Granite Inc",         "value": 170000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Basalt Data Migration",     "account": "Basalt Corp",         "value": 215000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Slate Integration Pack",    "account": "Slate LLC",           "value": 145000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "enterprise_references", "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Shale Ops Platform",        "account": "Shale Inc",           "value": 190000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Pumice Cloud Suite",        "account": "Pumice Co",           "value": 135000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Sandstone Budget Freeze",   "account": "Sandstone Ltd",       "value": 285000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "250K-500K"},
    {"name": "Quartzite Delay",           "account": "Quartzite Corp",      "value": 110000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "smb",        "deal_size_bucket": "100K-250K"},
    {"name": "Feldspar Reorg",            "account": "Feldspar Inc",        "value": 78000,  "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Mica Postponement",         "account": "Mica LLC",            "value": 92000,  "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Calcite Quick Win",         "account": "Calcite Co",          "value": 47000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Dolomite Starter",          "account": "Dolomite Inc",        "value": 56000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
]

# Q2: 118 closed opportunities (prior quarter baseline)
_Q2_OPPORTUNITIES = [
    # ── Enterprise Won (higher win rate in Q2) ──
    {"name": "Q2-Apex Expansion",        "account": "Apex Financial",     "value": 580000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Q2-Pinnacle Phase2",       "account": "Pinnacle Corp",      "value": 490000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Orion Initial",         "account": "Orion Industries",   "value": 520000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Q2-Atlas Core",            "account": "Atlas Group",        "value": 640000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Q2-Summit Begin",          "account": "Summit Enterprises", "value": 410000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Crestview Start",       "account": "Crestview Inc",      "value": 350000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Vertex Platform",       "account": "Vertex Corp",        "value": 470000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Keystone Migration",    "account": "Keystone Inc",       "value": 380000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Paradigm Cloud",        "account": "Paradigm LLC",       "value": 550000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Q2-Milestone ERP",         "account": "Milestone Corp",     "value": 620000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "500K+"},
    # ── Enterprise Lost Q2 (fewer losses) ──
    {"name": "Q2-TechCorp Eval",         "account": "TechCorp Industries","value": 680000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Q2-GlobalBank RFP",        "account": "Global Banking Corp","value": 590000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Q2-SecureHealth Phase1",   "account": "SecureHealth Inc",   "value": 420000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "enterprise_references", "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Vantage Initial",       "account": "Vantage Ltd",        "value": 380000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "pricing",            "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-PrimeCo Start",         "account": "PrimeCo",            "value": 310000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "feature_gaps",       "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-NexGen Eval",           "account": "NexGen Corp",        "value": 290000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "pricing",            "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Beacon Proposal",       "account": "Beacon Systems",     "value": 350000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "enterprise_references", "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    # ── Q2 Mid-Market Won ──
    {"name": "Q2-Velocity Start",        "account": "Velocity Co",        "value": 175000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Spark Initial",         "account": "Spark Corp",         "value": 190000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Pulse Phase1",          "account": "Pulse Inc",          "value": 155000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Drift Deploy",          "account": "Drift Technologies", "value": 130000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Zenith Pilot",          "account": "Zenith LLC",         "value": 110000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Nimbus Start",          "account": "Nimbus Corp",        "value": 180000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Helix Core",            "account": "Helix Inc",          "value": 210000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Prism Start",           "account": "Prism Ltd",          "value": 165000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Aether Pilot",          "account": "Aether Solutions",   "value": 140000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Stratos Begin",         "account": "Stratos Inc",        "value": 250000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Vortex Initial",        "account": "Vortex Corp",        "value": 220000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Matrix Deploy",         "account": "Matrix LLC",         "value": 185000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Dynamo Ops",            "account": "Dynamo Co",          "value": 260000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "250K-500K"},
    # ── Q2 Mid-Market Lost ──
    {"name": "Q2-BrightPath Eval",       "account": "BrightPath Co",      "value": 170000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Cascade RFP",           "account": "Cascade Inc",        "value": 200000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Evergreen Bid",         "account": "Evergreen LLC",      "value": 160000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Clearwater Eval",       "account": "Clearwater Inc",     "value": 210000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-StreamLine RFP",        "account": "StreamLine Co",      "value": 180000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-PeakView Proposal",     "account": "PeakView Inc",       "value": 240000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Horizon Eval",          "account": "Horizon Ltd",        "value": 145000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Ridgeline RFP",         "account": "Ridgeline Corp",     "value": 255000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "enterprise_references", "segment": "mid-market", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Trailhead Bid",         "account": "Trailhead Inc",      "value": 130000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Summit Edge Eval",      "account": "Summit Edge",        "value": 150000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "relationship",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-NorthStar RFP",         "account": "NorthStar Co",       "value": 195000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    # ── Q2 No Decision ──
    {"name": "Q2-Redwood Stall",         "account": "Redwood Corp",       "value": 310000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Pinecrest Delay",       "account": "Pinecrest Inc",      "value": 170000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Willow Hold",           "account": "Willow LLC",         "value": 240000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Birchwood Pause",       "account": "Birchwood Co",       "value": 135000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-OakHill Delay",         "account": "OakHill Partners",   "value": 390000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Cedarpoint Freeze",     "account": "Cedarpoint Inc",     "value": 260000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Aspen Stall",           "account": "Aspen Group",        "value": 185000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Maple Pause",           "account": "Maple Industries",   "value": 340000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-ElmGrove Freeze",       "account": "ElmGrove Ltd",       "value": 125000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "smb",        "deal_size_bucket": "100K-250K"},
    # ── Q2 CompetitorZ / Other ──
    {"name": "Q2-PolarStar Eval",        "account": "PolarStar Inc",      "value": 160000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-CoastalTech RFP",       "account": "CoastalTech",        "value": 190000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-TideLine Eval",         "account": "TideLine Corp",      "value": 155000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-HarborView Bid",        "account": "HarborView LLC",     "value": 130000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Anchor Deal",           "account": "Anchor Corp",        "value": 180000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "relationship",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    # ── Q2 SMB Won ──
    {"name": "Q2-Cirrus Pilot",          "account": "Cirrus Co",          "value": 85000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Ember Quick",           "account": "Ember LLC",          "value": 72000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Flint Deploy",          "account": "Flint Corp",         "value": 80000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Nova Start",            "account": "Nova Inc",           "value": 60000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Quasar Pilot",          "account": "Quasar Ltd",         "value": 68000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Photon Trial",          "account": "Photon Co",          "value": 50000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Echo Quick",            "account": "Echo Systems",       "value": 45000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Orbit Start",           "account": "Orbit Ltd",          "value": 90000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Luna Trial",            "account": "Luna Corp",          "value": 40000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Astro Pilot",           "account": "Astro LLC",          "value": 55000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Cosmic Trial",          "account": "Cosmic Inc",         "value": 32000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Nebula Start",          "account": "Nebula Co",          "value": 62000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Pulsar Quick",          "account": "Pulsar Ltd",         "value": 42000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    # ── Additional Q2 deals to reach ~118 total ──
    {"name": "Q2-Warp Initial",          "account": "Warp Inc",           "value": 135000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Comet Start",           "account": "Comet Solutions",    "value": 105000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Ruby Start",            "account": "Ruby Corp",          "value": 170000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Amber Deploy",          "account": "Amber Inc",          "value": 145000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Citrine Pilot",         "account": "Citrine LLC",        "value": 118000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Agate Quick",           "account": "Agate Co",           "value": 82000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Beryl Trial",           "account": "Beryl Ltd",          "value": 68000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Coral Deploy",          "account": "Coral Corp",         "value": 52000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Diamond Start",         "account": "Diamond Inc",        "value": 39000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Pearl Initial",         "account": "Pearl Inc",          "value": 290000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Opal Expansion",        "account": "Opal Ltd",           "value": 400000, "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Calcite Trial",         "account": "Calcite Co",         "value": 44000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Dolomite Quick",        "account": "Dolomite Inc",       "value": 52000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Pixel Pilot",           "account": "Pixel Corp",         "value": 48000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Byte Quick",            "account": "Byte LLC",           "value": 35000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Atom Deploy",           "account": "Atom Inc",           "value": 41000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Quark Trial",           "account": "Quark Co",           "value": 58000,  "outcome": "won",  "competitor_lost_to": None,          "loss_reason": None,                 "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Radiant Eval",          "account": "Radiant Corp",       "value": 520000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Q2-Cobalt RFP",            "account": "Cobalt Inc",         "value": 450000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "enterprise_references", "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Sapphire Bid",          "account": "Sapphire Ltd",       "value": 580000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "security_certs",     "segment": "enterprise", "deal_size_bucket": "500K+"},
    {"name": "Q2-FlintEdge Eval",        "account": "FlintEdge Co",       "value": 180000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Granite RFP",           "account": "Granite Inc",        "value": 160000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Basalt Proposal",       "account": "Basalt Corp",        "value": 200000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Shale Eval",            "account": "Shale Inc",          "value": 175000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-LightHouse Bid",        "account": "LightHouse Inc",     "value": 140000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "relationship",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Pumice Stall",          "account": "Pumice Co",          "value": 125000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Sandstone Pause",       "account": "Sandstone Ltd",      "value": 270000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Quartzite Hold",        "account": "Quartzite Corp",     "value": 100000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "smb",        "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Feldspar Delay",        "account": "Feldspar Inc",       "value": 72000,  "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Mica Freeze",           "account": "Mica LLC",           "value": 85000,  "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Portside RFP",          "account": "Portside LLC",       "value": 110000, "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "pricing",            "segment": "smb",        "deal_size_bucket": "100K-250K"},
    {"name": "Q2-BreakWater Bid",        "account": "BreakWater Co",      "value": 80000,  "outcome": "lost", "competitor_lost_to": "CompetitorZ", "loss_reason": "pricing",            "segment": "smb",        "deal_size_bucket": "<100K"},
    {"name": "Q2-Slate Eval",            "account": "Slate LLC",          "value": 135000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "enterprise_references", "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-RapidScale RFP",        "account": "RapidScale Co",      "value": 150000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-WildPine Eval",         "account": "WildPine Ltd",       "value": 175000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-CoralReef Bid",         "account": "CoralReef Inc",      "value": 145000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-StoneArch Eval",        "account": "StoneArch Corp",     "value": 230000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-BlueSky RFP",           "account": "BlueSky Solutions",  "value": 120000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "relationship",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-GreenField Bid",        "account": "GreenField Inc",     "value": 160000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "feature_gaps",       "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-IronBridge RFP",        "account": "IronBridge LLC",     "value": 190000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-SilverLake Eval",       "account": "SilverLake Co",      "value": 210000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "enterprise_references", "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-NorthStar Bid",         "account": "NorthStar Co",       "value": 185000, "outcome": "lost", "competitor_lost_to": "CompetitorY", "loss_reason": "pricing",            "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Topaz Eval",            "account": "Topaz Group",        "value": 320000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "pricing",            "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Jade RFP",              "account": "Jade Corp",          "value": 260000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "feature_gaps",       "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Onyx Proposal",         "account": "Onyx Industries",    "value": 360000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "enterprise_references", "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Garnet Eval",           "account": "Garnet Solutions",   "value": 410000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "pricing",            "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Meridian Eval",         "account": "Meridian Corp",      "value": 310000, "outcome": "lost", "competitor_lost_to": "CompetitorX", "loss_reason": "relationship",       "segment": "enterprise", "deal_size_bucket": "250K-500K"},
    {"name": "Q2-Spruce Freeze",         "account": "Spruce Systems",     "value": 150000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-Juniper Stall",         "account": "Juniper Corp",       "value": 190000, "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "mid-market", "deal_size_bucket": "100K-250K"},
    {"name": "Q2-CypressWood Hold",      "account": "CypressWood Inc",    "value": 88000,  "outcome": "lost", "competitor_lost_to": None,          "loss_reason": "no_decision",        "segment": "smb",        "deal_size_bucket": "<100K"},
]

# Intervention costs and expected recovery rates
_INTERVENTIONS = {
    "security_positioning": {
        "label": "Security Positioning Refresh",
        "cost": 25000,
        "recovery_rate": 0.35,
        "timeline": "Immediate",
        "actions": [
            "Lead with SOC 2 Type II (currently underutilized in sales materials)",
            "Create Security Architecture one-pager for enterprise buyers",
            "Offer security team direct access during evaluation period",
            "Bridge messaging: FedRAMP in progress, SOC 2 + ISO active now",
        ],
    },
    "fedramp_certification": {
        "label": "FedRAMP Certification",
        "cost": 85000,
        "recovery_rate": 0.55,
        "timeline": "6 months",
        "actions": [
            "Engage FedRAMP 3PAO for readiness assessment",
            "Assign dedicated compliance engineering team",
            "Target FedRAMP Moderate authorization",
        ],
    },
    "reference_program": {
        "label": "Enterprise Reference Program",
        "cost": 30000,
        "recovery_rate": 0.40,
        "timeline": "30 days",
        "actions": [
            "Activate 3 enterprise customers for reference calls",
            "Produce 2 video testimonials from Fortune 1000 logos",
            "Offer reference incentives (extended support, discounts)",
            "Build enterprise customer advisory board",
        ],
    },
    "pricing_flexibility": {
        "label": "Pricing & Packaging Adjustment",
        "cost": 15000,
        "recovery_rate": 0.30,
        "timeline": "Immediate",
        "actions": [
            "Enterprise tier: bundle security features at no extra cost",
            "Offer 90-day pilot with success-based conversion",
            "Match competitor payment terms flexibility",
            "Introduce volume discount for multi-year commits",
        ],
    },
    "iso_certification": {
        "label": "ISO 27001 Certification",
        "cost": 25000,
        "recovery_rate": 0.20,
        "timeline": "4 months",
        "actions": [
            "Engage certification body for gap assessment",
            "Implement required ISMS controls",
            "Complete Stage 1 and Stage 2 audits",
        ],
    },
}

_ANALYSIS_RECORDS = {
    "Q3-COMPETITORX": {
        "quarter": "Q3",
        "competitor": "CompetitorX",
        "segment": "enterprise",
        "crm_topic": "Enterprise win-rate recovery",
    },
}


# ═══════════════════════════════════════════════════════════════
# HELPERS -- real computation, synthetic inputs
# ═══════════════════════════════════════════════════════════════

def _quarter_stats(opps):
    """Compute aggregate stats for a list of opportunities."""
    total = len(opps)
    won = [o for o in opps if o["outcome"] == "won"]
    lost = [o for o in opps if o["outcome"] == "lost"]
    win_rate = round(len(won) / max(total, 1) * 100, 1)
    avg_won_value = int(sum(o["value"] for o in won) / max(len(won), 1))
    total_won_value = sum(o["value"] for o in won)
    total_lost_value = sum(o["value"] for o in lost)

    # Segment breakdown
    segments = {}
    for seg in ("enterprise", "mid-market", "smb"):
        seg_opps = [o for o in opps if o["segment"] == seg]
        seg_won = [o for o in seg_opps if o["outcome"] == "won"]
        segments[seg] = {
            "total": len(seg_opps),
            "won": len(seg_won),
            "lost": len(seg_opps) - len(seg_won),
            "win_rate": round(len(seg_won) / max(len(seg_opps), 1) * 100, 1),
        }

    return {
        "total": total, "won": len(won), "lost": len(lost),
        "win_rate": win_rate, "avg_won_value": avg_won_value,
        "total_won_value": total_won_value,
        "total_lost_value": total_lost_value,
        "segments": segments,
    }


def _competitor_breakdown(opps):
    """Break down losses by competitor with counts and values."""
    lost = [o for o in opps if o["outcome"] == "lost"]
    competitors = {}
    no_decision_count = 0
    no_decision_value = 0
    for o in lost:
        comp = o["competitor_lost_to"]
        if comp is None:
            no_decision_count += 1
            no_decision_value += o["value"]
        else:
            if comp not in competitors:
                competitors[comp] = {"count": 0, "value": 0, "reasons": {}}
            competitors[comp]["count"] += 1
            competitors[comp]["value"] += o["value"]
            reason = o["loss_reason"] or "unknown"
            competitors[comp]["reasons"][reason] = competitors[comp]["reasons"].get(reason, 0) + 1

    competitors["No Decision"] = {"count": no_decision_count, "value": no_decision_value, "reasons": {"no_decision": no_decision_count}}
    total_lost = len(lost)
    for comp in competitors:
        competitors[comp]["pct_of_losses"] = round(competitors[comp]["count"] / max(total_lost, 1) * 100, 1)
    return competitors


def _loss_reason_analysis(opps, competitor=None):
    """Analyze loss reasons, optionally filtered to a specific competitor."""
    lost = [o for o in opps if o["outcome"] == "lost"]
    if competitor:
        lost = [o for o in lost if o["competitor_lost_to"] == competitor]

    reasons = {}
    for o in lost:
        r = o["loss_reason"] or "unknown"
        if r not in reasons:
            reasons[r] = {"count": 0, "value": 0}
        reasons[r]["count"] += 1
        reasons[r]["value"] += o["value"]

    total_lost = len(lost)
    for r in reasons:
        reasons[r]["frequency_pct"] = round(reasons[r]["count"] / max(total_lost, 1) * 100, 1)

    # Impact scoring: high if frequency > 25%, medium 10-25%, low < 10%
    for r in reasons:
        pct = reasons[r]["frequency_pct"]
        if pct >= 25:
            reasons[r]["impact"] = "High"
        elif pct >= 10:
            reasons[r]["impact"] = "Medium"
        else:
            reasons[r]["impact"] = "Low"

        # Addressable assessment
        addressable_map = {
            "security_certs": "Yes (6 months)",
            "enterprise_references": "Yes (3 months)",
            "pricing": "Yes (immediate)",
            "feature_gaps": "Roadmap item",
            "no_decision": "Partially (nurture)",
            "relationship": "Yes (engagement plan)",
        }
        reasons[r]["addressable"] = addressable_map.get(r, "Unknown")

    return reasons


def _revenue_recovery_model(opps):
    """Model recoverable revenue per intervention based on loss data."""
    lost = [o for o in opps if o["outcome"] == "lost"]
    projections = {}
    total_recoverable = 0

    reason_to_intervention = {
        "security_certs": ["security_positioning", "fedramp_certification"],
        "enterprise_references": ["reference_program"],
        "pricing": ["pricing_flexibility"],
        "feature_gaps": [],
        "no_decision": [],
        "relationship": ["reference_program"],
    }

    for intv_key, intv in _INTERVENTIONS.items():
        # Find deals that map to this intervention
        applicable_reasons = [r for r, ivs in reason_to_intervention.items() if intv_key in ivs]
        applicable_deals = [o for o in lost if o.get("loss_reason") in applicable_reasons]

        total_pipeline = sum(o["value"] for o in applicable_deals)
        recoverable_value = int(total_pipeline * intv["recovery_rate"])
        deal_count_low = max(1, int(len(applicable_deals) * intv["recovery_rate"] * 0.7))
        deal_count_high = max(deal_count_low, int(len(applicable_deals) * intv["recovery_rate"] * 1.1))

        projections[intv_key] = {
            "label": intv["label"],
            "applicable_deals": len(applicable_deals),
            "total_pipeline": total_pipeline,
            "recoverable_value": recoverable_value,
            "deals_recoverable": f"{deal_count_low}-{deal_count_high}",
            "cost": intv["cost"],
            "timeline": intv["timeline"],
            "roi": round(recoverable_value / max(intv["cost"], 1), 1),
        }
        total_recoverable += recoverable_value

    total_cost = sum(intv["cost"] for intv in _INTERVENTIONS.values())
    return projections, total_recoverable, total_cost


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class WinLossAnalysisAgent(BasicAgent):
    """
    Analyzes closed opportunities to surface win-rate trends, loss patterns,
    and revenue recovery opportunities.

    Operations:
        win_loss_overview   - Quarter comparison, win rates, competitor breakdown
        root_cause_analysis - Loss pattern identification with frequency/impact scoring
        counter_strategies  - Specific strategies per loss driver (immediate + long-term)
        revenue_impact      - Financial modeling of interventions with ROI
        board_presentation  - Slide-by-slide board presentation framework
        action_summary      - Complete findings and next steps
        publish_findings    - update CRM and share exact analysis via Teams
    """

    def __init__(self):
        self.name = "WinLossAnalysisAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "win_loss_overview", "root_cause_analysis",
                            "counter_strategies", "revenue_impact",
                            "board_presentation", "action_summary",
                            "publish_findings",
                        ],
                        "description": "The analysis to perform",
                    },
                    "quarter": {
                        "type": "string",
                        "description": "Quarter to analyze (default: Q3 current)",
                    },
                    "analysis_id": {
                        "type": "string",
                        "description": "Exact analysis ID for publish_findings (e.g. 'Q3-COMPETITORX')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "win_loss_overview")
        if op == "publish_findings":
            return self._publish_findings(kwargs.get("analysis_id"))
        dispatch = {
            "win_loss_overview": self._win_loss_overview,
            "root_cause_analysis": self._root_cause_analysis,
            "counter_strategies": self._counter_strategies,
            "revenue_impact": self._revenue_impact,
            "board_presentation": self._board_presentation,
            "action_summary": self._action_summary,
        }
        handler = dispatch.get(op)
        if not handler:
            return json.dumps({"status": "error", "message": f"Unknown operation: {op}"})
        return handler()

    def _publish_findings(self, analysis_id):
        analysis = _ANALYSIS_RECORDS.get(analysis_id)
        if analysis is None:
            return json.dumps({
                "status": "error",
                "message": f"Unknown analysis_id: {analysis_id!r}",
                "valid_analysis_ids": ", ".join(sorted(_ANALYSIS_RECORDS)),
            })
        stats = _quarter_stats(_Q3_OPPORTUNITIES)
        competitor = analysis["competitor"]
        reasons = _loss_reason_analysis(_Q3_OPPORTUNITIES, competitor=competitor)
        top_reason, top_data = max(reasons.items(), key=lambda item: item[1]["count"])
        _, recoverable, investment = _revenue_recovery_model(_Q3_OPPORTUNITIES)
        receipt = {
            "status": "simulated",
            "analysis_id": analysis_id,
            "quarter": analysis["quarter"],
            "segment": analysis["segment"],
            "competitor": competitor,
            "opportunities_analyzed": stats["total"],
            "win_rate_pct": stats["win_rate"],
            "top_loss_driver": top_reason,
            "top_loss_driver_frequency_pct": top_data["frequency_pct"],
            "recoverable_pipeline": recoverable,
            "recommended_investment": investment,
            "crm_insight_id": f"sim-d365-insight-{analysis_id.lower()}",
            "teams_message_id": f"sim-teams-board-{analysis_id.lower()}",
        }
        return "**Win/Loss Findings Publication Receipt**\n\n```json\n" + json.dumps(receipt, indent=2) + "\n```"

    # ── win_loss_overview (flagship: prefers LIVE, falls back) ──
    def _win_loss_overview(self):
        live = _live_closed_deals()
        if live:
            won = [d for d in live if d["outcome"] == "won"]
            lost = [d for d in live if d["outcome"] == "lost"]
            win_rate = round(len(won) / max(len(live), 1) * 100, 1)
            avg_won = int(sum(d["value"] for d in won) / max(len(won), 1))
            rows = ""
            for d in sorted(live, key=lambda x: -x["value"]):
                rows += (f"| {d['name']} | ${d['value']:,} | {d['outcome'].upper()} | "
                         f"{d['closed_on'] or 'n/a'} | {d['owner']} | "
                         f"n/a — enrichment seam |\n")
            return (
                f"**Win/Loss Overview — {len(live)} LIVE Closed Deals** "
                f"(Static Dynamics 365 tenant)\n\n"
                f"| Metric | Value |\n|---|---|\n"
                f"| Closed opportunities | {len(live)} |\n"
                f"| Won / Lost | {len(won)} / {len(lost)} |\n"
                f"| Win rate | {win_rate}% |\n"
                f"| Avg deal size (won) | ${avg_won:,} |\n"
                f"| Won value | ${sum(d['value'] for d in won):,} |\n"
                f"| Lost value | ${sum(d['value'] for d in lost):,} |\n\n"
                f"**Closed Deals:**\n\n"
                f"| Deal | Value | Outcome | Closed | Owner | Loss Reason |\n"
                f"|------|-------|---------|--------|-------|-------------|\n"
                f"{rows}\n"
                f"Loss reasons and competitor attribution stay n/a until you "
                f"wire your win/loss survey platform at the LIVE DATA SEAM. "
                f"Prior-quarter comparison needs your historical snapshots "
                f"(the offline demo shows the full Q3-vs-Q2 renderer).\n\n"
                f"Source: [Live Dynamics 365 opportunities]\n"
                f"Agents: WinLossDataAgent"
            )
        q3 = _quarter_stats(_Q3_OPPORTUNITIES)
        q2 = _quarter_stats(_Q2_OPPORTUNITIES)
        wr_delta = round(q3["win_rate"] - q2["win_rate"], 1)
        ent_delta = round(q3["segments"]["enterprise"]["win_rate"] - q2["segments"]["enterprise"]["win_rate"], 1)
        opp_delta = round((q3["total"] - q2["total"]) / max(q2["total"], 1) * 100)
        avg_delta = round((q3["avg_won_value"] - q2["avg_won_value"]) / max(q2["avg_won_value"], 1) * 100)

        comp_q3 = _competitor_breakdown(_Q3_OPPORTUNITIES)
        comp_q2 = _competitor_breakdown(_Q2_OPPORTUNITIES)

        # Build competitor table sorted by loss count descending
        comp_rows = ""
        for comp in sorted(comp_q3, key=lambda c: comp_q3[c]["count"], reverse=True):
            c3 = comp_q3[comp]
            c2 = comp_q2.get(comp, {"pct_of_losses": 0})
            trend_val = round(c3["pct_of_losses"] - c2["pct_of_losses"], 1)
            trend = f"Up {trend_val}%" if trend_val > 1 else ("Down {:.0f}%".format(abs(trend_val)) if trend_val < -1 else "Flat")
            comp_rows += f"| {comp} | {c3['count']} | {c3['pct_of_losses']}% | {trend} |\n"

        # Identify top competitor
        top_comp = max((c for c in comp_q3 if c != "No Decision"), key=lambda c: comp_q3[c]["count"], default="CompetitorX")

        seg_table = ""
        for seg in ("enterprise", "mid-market", "smb"):
            s3 = q3["segments"][seg]
            s2 = q2["segments"][seg]
            delta = round(s3["win_rate"] - s2["win_rate"], 1)
            seg_table += f"| {seg.title()} | {s3['win_rate']}% | {s2['win_rate']}% | {delta:+.1f} pts |\n"

        return (
            f"**Q3 Win/Loss Overview** ({q3['total']} closed opportunities analyzed)\n\n"
            f"| Metric | Q3 | Q2 | Change |\n|---|---|---|---|\n"
            f"| Total opportunities | {q3['total']} | {q2['total']} | {opp_delta:+d}% |\n"
            f"| Win rate | {q3['win_rate']}% | {q2['win_rate']}% | {wr_delta:+.1f} pts |\n"
            f"| Enterprise win rate | {q3['segments']['enterprise']['win_rate']}% | {q2['segments']['enterprise']['win_rate']}% | {ent_delta:+.1f} pts |\n"
            f"| Avg deal size (won) | ${q3['avg_won_value']:,} | ${q2['avg_won_value']:,} | {avg_delta:+d}% |\n\n"
            f"**Win Rate by Segment:**\n\n"
            f"| Segment | Q3 | Q2 | Change |\n|---|---|---|---|\n{seg_table}\n"
            f"**Loss Analysis by Competitor:**\n\n"
            f"| Competitor | Losses | % of Total | Trend |\n|---|---|---|---|\n{comp_rows}\n"
            f"**Initial Pattern:** {top_comp} wins are concentrated in enterprise ($500K+) deals with security-conscious buyers.\n\n"
            f"Source: [CRM + Win/Loss Interviews + Competitive Intel]\n"
            f"Agents: WinLossDataAgent, PatternRecognitionAgent"
        )

    # ── root_cause_analysis ────────────────────────────────────
    def _root_cause_analysis(self):
        # Focus on top competitor
        comp = _competitor_breakdown(_Q3_OPPORTUNITIES)
        top_comp = max((c for c in comp if c != "No Decision"), key=lambda c: comp[c]["count"], default="CompetitorX")
        reasons = _loss_reason_analysis(_Q3_OPPORTUNITIES, competitor=top_comp)

        # Sort by frequency
        sorted_reasons = sorted(reasons.items(), key=lambda kv: kv[1]["count"], reverse=True)

        reason_labels = {
            "security_certs": "Security certifications",
            "enterprise_references": "Enterprise references",
            "pricing": "Pricing/packaging",
            "feature_gaps": "Feature gaps",
            "no_decision": "No decision",
            "relationship": "Relationship/trust",
        }

        table = ""
        for r, data in sorted_reasons:
            label = reason_labels.get(r, r)
            table += f"| {label} | {data['frequency_pct']}% | {data['impact']} | {data['addressable']} |\n"

        # Deep dives for top 2 reasons
        top_two = sorted_reasons[:2]
        deep_dives = ""
        buyer_quotes = {
            "security_certs": "We loved the product but couldn't get past security review",
            "enterprise_references": "We need peer validation from companies our size before we commit",
            "pricing": "The total cost was above our budget threshold for this category",
            "feature_gaps": "Missing capabilities we consider table-stakes for our use case",
            "relationship": "We had stronger rapport and trust with the competing vendor team",
        }

        sec_deals = [o for o in _Q3_OPPORTUNITIES if o["outcome"] == "lost" and o["competitor_lost_to"] == top_comp and o["loss_reason"] == "security_certs"]
        ref_deals = [o for o in _Q3_OPPORTUNITIES if o["outcome"] == "lost" and o["competitor_lost_to"] == top_comp and o["loss_reason"] == "enterprise_references"]

        if sec_deals:
            deep_dives += (
                f"\n**Deep Dive - Security ({len(sec_deals)} deals, ${sum(d['value'] for d in sec_deals):,} pipeline):**\n"
                f"- {top_comp} has FedRAMP certification (we do not)\n"
                f"- They lead with SOC 2 Type II + ISO 27001 in every proposal\n"
                f"- Enterprise buyers require these for procurement approval\n"
                f'- Quote: "{buyer_quotes["security_certs"]}"\n'
            )
        if ref_deals:
            deep_dives += (
                f"\n**Deep Dive - References ({len(ref_deals)} deals, ${sum(d['value'] for d in ref_deals):,} pipeline):**\n"
                f"- {top_comp} has 12 Fortune 500 logos available for reference\n"
                f"- We have 3 enterprise references currently available\n"
                f"- Buyers want peer validation at their scale before committing\n"
                f'- Quote: "{buyer_quotes["enterprise_references"]}"\n'
            )

        # Win/loss interview insight
        preferred_ux_count = len(sec_deals) + len(ref_deals)
        interview_note = ""
        if preferred_ux_count > 0:
            surveyed = min(preferred_ux_count, 10)
            preferred = int(surveyed * 0.8)
            interview_note = f"\n**Win/Loss Interview Insight:** {preferred} of {surveyed} lost buyers said they preferred our UX but couldn't justify the security/reference risk.\n"

        return (
            f"**Root Cause Analysis - Losses to {top_comp}:**\n\n"
            f"| Reason | Frequency | Impact | Addressable? |\n|---|---|---|---|\n{table}"
            f"{deep_dives}{interview_note}\n"
            f"Source: [Win/Loss Surveys + Gong Calls + Competitive Intel]\n"
            f"Agents: RootCauseAnalysisAgent, PatternRecognitionAgent"
        )

    # ── counter_strategies ─────────────────────────────────────
    def _counter_strategies(self):
        reasons = _loss_reason_analysis(_Q3_OPPORTUNITIES)
        sorted_reasons = sorted(reasons.items(), key=lambda kv: kv[1]["count"], reverse=True)

        immediate = []
        long_term = []
        for intv_key, intv in _INTERVENTIONS.items():
            if intv["timeline"] in ("Immediate", "30 days"):
                immediate.append((intv_key, intv))
            else:
                long_term.append((intv_key, intv))

        imm_section = "**Immediate Actions (This Quarter):**\n\n"
        for i, (key, intv) in enumerate(immediate, 1):
            imm_section += f"**{i}. {intv['label']}**\n"
            for action in intv["actions"]:
                imm_section += f"- {action}\n"
            imm_section += "\n"

        lt_section = "**Longer-Term (Next 2 Quarters):**\n\n"
        for key, intv in long_term:
            lt_section += f"- {intv['label']} ({intv['timeline']} timeline, ${intv['cost']:,} investment)\n"
            for action in intv["actions"]:
                lt_section += f"  - {action}\n"
        lt_section += "\n"

        talk_track = (
            "**Updated Talk Track:**\n"
            '"We\'re the secure choice for enterprises who want modern UX. '
            "Here's our SOC 2 Type II, and our FedRAMP is in progress. "
            'Let us connect you with 3 enterprise references in your industry."\n'
        )

        return (
            f"**Counter-Strategies for Win Rate Recovery:**\n\n"
            f"{imm_section}{lt_section}{talk_track}\n"
            f"Source: [Competitive Playbook + Product Roadmap]\n"
            f"Agents: CompetitiveStrategyAgent"
        )

    # ── revenue_impact ─────────────────────────────────────────
    def _revenue_impact(self):
        q3 = _quarter_stats(_Q3_OPPORTUNITIES)
        projections, total_recoverable, total_cost = _revenue_recovery_model(_Q3_OPPORTUNITIES)

        # Revenue recovery table
        table = ""
        for key in sorted(projections, key=lambda k: projections[k]["recoverable_value"], reverse=True):
            p = projections[key]
            table += f"| {p['label']} | {p['deals_recoverable']} deals | ${p['recoverable_value']:,} | {p['timeline']} |\n"

        overall_roi = round(total_recoverable / max(total_cost, 1), 1)

        # Forecast impact modeling
        current_won = q3["total_won_value"]
        # Project Q4 based on current trajectory vs intervention
        q4_current_trajectory = int(current_won * 1.0)  # Flat from Q3
        intervention_lift = int(total_recoverable * 0.62)  # 62% realizable in Q4
        q4_with_intervention = q4_current_trajectory + intervention_lift

        current_wr = q3["win_rate"]
        q4_wr = round(current_wr + (total_recoverable / max(q3["total_lost_value"], 1)) * 100 * 0.15, 1)
        q1_wr = round(q4_wr + 4.0, 1)
        q2_wr = round(q1_wr + 4.0, 1)

        return (
            f"**Revenue Impact Model:**\n\n"
            f"| Intervention | Deals Recoverable | Pipeline Value | Timeline |\n|---|---|---|---|\n{table}\n"
            f"**Q4 Forecast Impact:**\n"
            f"- Current trajectory: ${q4_current_trajectory:,} ({current_wr}% win rate)\n"
            f"- With interventions: ${q4_with_intervention:,} ({q4_wr}% win rate)\n"
            f"- **Incremental revenue: ${intervention_lift:,}**\n\n"
            f"**Win Rate Recovery Path:**\n\n"
            f"| Quarter | Projected Win Rate | Key Driver |\n|---|---|---|\n"
            f"| Q4 | {q4_wr}% | Positioning + pricing |\n"
            f"| Q1 | {q1_wr}% | References + certifications |\n"
            f"| Q2 | {q2_wr}% | Full program maturity |\n\n"
            f"**ROI Calculation:**\n"
            f"- Investment: ${total_cost:,} (certifications, content, incentives)\n"
            f"- Return: ${total_recoverable:,} recovered pipeline\n"
            f"- ROI: {overall_roi}:1\n\n"
            f"Source: [Revenue Analytics + Forecast Models]\n"
            f"Agents: RevenueImpactAgent"
        )

    # ── board_presentation ─────────────────────────────────────
    def _board_presentation(self):
        q3 = _quarter_stats(_Q3_OPPORTUNITIES)
        q2 = _quarter_stats(_Q2_OPPORTUNITIES)
        wr_delta = round(q3["win_rate"] - q2["win_rate"], 1)
        ent_delta = round(q3["segments"]["enterprise"]["win_rate"] - q2["segments"]["enterprise"]["win_rate"], 1)

        comp = _competitor_breakdown(_Q3_OPPORTUNITIES)
        top_comp = max((c for c in comp if c != "No Decision"), key=lambda c: comp[c]["count"], default="CompetitorX")
        top_comp_pct = comp[top_comp]["pct_of_losses"]

        reasons = _loss_reason_analysis(_Q3_OPPORTUNITIES, competitor=top_comp)
        sorted_reasons = sorted(reasons.items(), key=lambda kv: kv[1]["count"], reverse=True)

        reason_labels = {
            "security_certs": "Security certs",
            "enterprise_references": "Enterprise refs",
            "pricing": "Pricing",
            "feature_gaps": "Feature gaps",
            "relationship": "Relationship",
        }

        projections, total_recoverable, total_cost = _revenue_recovery_model(_Q3_OPPORTUNITIES)
        overall_roi = round(total_recoverable / max(total_cost, 1), 1)

        current_wr = q3["win_rate"]
        q4_wr = round(current_wr + (total_recoverable / max(q3["total_lost_value"], 1)) * 100 * 0.15, 1)

        evidence_table = ""
        for r, data in sorted_reasons[:3]:
            label = reason_labels.get(r, r)
            evidence_table += f"| {label} | {data['frequency_pct']}% of losses | Buyer feedback, lost deal analysis |\n"

        return (
            f"**Board Presentation: Q3 Win/Loss Analysis**\n\n"
            f"**Slide 1: The Challenge**\n"
            f"- Win rate declined to {q3['win_rate']}% (from {q2['win_rate']}%)\n"
            f"- Enterprise segment hit hardest ({ent_delta:+.1f} pts)\n"
            f"- {top_comp} captured {top_comp_pct}% of our losses\n"
            f"- Root cause: Security positioning and references gap\n\n"
            f"**Slide 2: Why We're Losing**\n\n"
            f"| Factor | Impact | Evidence |\n|---|---|---|\n{evidence_table}\n"
            f"**Slide 3: The Plan**\n"
            f"- Immediate: Security messaging refresh, pricing flexibility\n"
            f"- 30 days: Enterprise reference program launch\n"
            f"- 6 months: FedRAMP + ISO 27001 certification\n\n"
            f"**Slide 4: Expected Outcomes**\n"
            f"- Q4 win rate target: {q4_wr}% ({q4_wr - current_wr:+.1f} pts)\n"
            f"- Pipeline recovery: ${total_recoverable:,}\n"
            f"- Investment required: ${total_cost:,}\n"
            f"- ROI: {overall_roi}:1\n\n"
            f"**Ask:** Approve ${total_cost:,} for certification and reference program.\n\n"
            f"Source: [All Analysis Systems]\n"
            f"Agents: ExecutivePresentationAgent"
        )

    # ── action_summary ─────────────────────────────────────────
    def _action_summary(self):
        q3 = _quarter_stats(_Q3_OPPORTUNITIES)
        q2 = _quarter_stats(_Q2_OPPORTUNITIES)
        wr_delta = round(q3["win_rate"] - q2["win_rate"], 1)

        comp = _competitor_breakdown(_Q3_OPPORTUNITIES)
        top_comp = max((c for c in comp if c != "No Decision"), key=lambda c: comp[c]["count"], default="CompetitorX")
        top_comp_pct = comp[top_comp]["pct_of_losses"]

        reasons = _loss_reason_analysis(_Q3_OPPORTUNITIES, competitor=top_comp)
        sorted_reasons = sorted(reasons.items(), key=lambda kv: kv[1]["count"], reverse=True)
        top_reason = sorted_reasons[0] if sorted_reasons else ("unknown", {"frequency_pct": 0})
        second_reason = sorted_reasons[1] if len(sorted_reasons) > 1 else ("unknown", {"frequency_pct": 0})

        reason_labels = {
            "security_certs": "Security certifications",
            "enterprise_references": "Enterprise references",
            "pricing": "Pricing/packaging",
            "feature_gaps": "Feature gaps",
            "no_decision": "No decision",
            "relationship": "Relationship/trust",
        }

        projections, total_recoverable, total_cost = _revenue_recovery_model(_Q3_OPPORTUNITIES)
        overall_roi = round(total_recoverable / max(total_cost, 1), 1)
        num_root_causes = len([r for r in reasons if reasons[r]["frequency_pct"] >= 10])

        current_wr = q3["win_rate"]
        q4_wr = round(current_wr + (total_recoverable / max(q3["total_lost_value"], 1)) * 100 * 0.15, 1)
        recovery_quarters = 2

        return (
            f"**Win/Loss Analysis - Complete Summary**\n\n"
            f"| Insight | Finding |\n|---|---|\n"
            f"| Q3 win rate | {q3['win_rate']}% ({wr_delta:+.1f} pts from Q2) |\n"
            f"| Primary competitor | {top_comp} ({top_comp_pct}% of losses) |\n"
            f"| Biggest gap | {reason_labels.get(top_reason[0], top_reason[0])} ({top_reason[1]['frequency_pct']}%) |\n"
            f"| Second gap | {reason_labels.get(second_reason[0], second_reason[0])} ({second_reason[1]['frequency_pct']}%) |\n"
            f"| Recoverable pipeline | ${total_recoverable:,} |\n\n"
            f"**Session Accomplishments:**\n"
            f"- Analyzed {q3['total']} Q3 opportunities\n"
            f"- Identified {num_root_causes} root causes for losses\n"
            f"- Developed counter-strategies for each driver\n"
            f"- Modeled ${total_recoverable:,} revenue recovery\n"
            f"- Created board presentation framework\n\n"
            f"**Immediate Actions (This Week):**\n"
            f"1. Update security positioning materials\n"
            f"2. Launch pricing flexibility program\n"
            f"3. Activate enterprise reference calls\n"
            f"4. Train sales team on updated talk tracks\n\n"
            f"**30-Day Milestones:**\n"
            f"- Reference video testimonials live\n"
            f"- FedRAMP readiness assessment initiated\n"
            f"- Win rate tracking dashboard active\n\n"
            f"**Expected Outcome:** Win rate recovery from {current_wr}% to {q4_wr}% within {recovery_quarters} quarters, "
            f"${total_recoverable:,} pipeline recovery, {overall_roi}:1 ROI on ${total_cost:,} investment.\n\n"
            f"Source: [All Win/Loss Systems]\n"
            f"Agents: ExecutivePresentationAgent (orchestrating all agents)"
        )


if __name__ == "__main__":
    agent = WinLossAnalysisAgent()
    print("=" * 60)
    print("LIVE TENANT CLOSED DEALS (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="win_loss_overview"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="root_cause_analysis"))
    print()
    print("=" * 60)
    print(agent.perform(operation="action_summary"))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
