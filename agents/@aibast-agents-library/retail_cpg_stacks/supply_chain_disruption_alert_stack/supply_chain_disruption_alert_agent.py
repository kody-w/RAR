"""
Supply Chain Disruption Alert Agent — a template you are meant to mutate.

Monitors supply chain routes for disruptions, assesses risk levels,
generates mitigation plans, and identifies alternative suppliers.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live disruption signals over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="disruption_dashboard")
     — with network up, the feed surfaces the tenant's live supply-chain
     cases such as CAS-260133 "Cold chain temperature excursion in
     produce section" (Harbor Lights Grocery). In this template a
     disruption signal is represented as a Dynamics case (incident).
  2. No network? Everything falls back to the embedded demo layer below
     (SUPPLY_ROUTES / DISRUPTION_EVENTS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SUPPLY_CHAIN_DISRUPTION_ALERT_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON from your TMS/visibility platform),
     or replace _fetch_collection() with your own logistics API. The
     fields the rest of the file needs are listed in
     _normalize_live_disruption() — revenue impact and affected routes
     stay "n/a — enrichment seam" until you wire your planning system.

OPERATIONS
  disruption_dashboard | risk_assessment | mitigation_plan |
  supplier_alternatives | disruption_impact | response_scenarios |
  response_execution | recovery_tracking | incident_report
  kwargs: operation (required), route_id, disruption_id, category, key,
  user_input
"""

import sys
import os

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"),
)
from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/supply_chain_disruption_alert",
    "version": "1.2.0",
    "display_name": "Supply Chain Disruption Alert Agent",
    "description": (
        "Flags disruptions and builds mitigation plans from a live simulated Dynamics 365 tenant's service cases, with an offline demo fallback."
    ),
    "author": "AIBAST",
    "tags": [
        "supply-chain",
        "disruption",
        "risk-management",
        "logistics",
        "retail",
    ],
    "category": "retail_cpg",
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
#   export SUPPLY_CHAIN_DISRUPTION_ALERT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your TMS/visibility client.
# Downstream code only needs the fields from _normalize_live_disruption().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "SUPPLY_CHAIN_DISRUPTION_ALERT_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}

# Case-title keywords that mark a tenant case as a supply-chain signal.
_DISRUPTION_KEYWORDS = (
    "shipment", "freight", "cold chain", "backorder", "delivery",
    "delayed", "downtime", "tracking",
)


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


def _normalize_live_disruption(row):
    """Project a Dynamics case (incident) record onto the shape this agent
    uses — in this template a supply-chain disruption signal IS a Dynamics
    case. THIS is the contract your replacement data source must meet — a
    dict with these keys. None means 'not available from the service desk
    alone' and the renderers label it as an enrichment seam."""
    return {
        "event_id": row.get("ticketnumber", row.get("incidentid", "")),
        "title": row.get("title", "untitled"),
        "customer": row.get("customeridname", "Unknown"),
        "severity": row.get(
            "prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"
        ),
        "status": row.get(
            "statecode@OData.Community.Display.V1.FormattedValue", "Active"
        ),
        "open": row.get("statecode") == 0,
        "age_days": _age_days(row.get("createdon")),
        "revenue_impact": None,   # enrichment seam — wire your planning system
        "affected_routes": None,  # enrichment seam — wire your TMS
        "_live": True,
    }


def _age_days(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


def _live_disruption_signals():
    """Live tenant cases whose titles look supply-chain-shaped; [] offline."""
    signals = []
    for row in _fetch_collection("incidents"):
        title = str(row.get("title", "")).lower()
        if any(kw in title for kw in _DISRUPTION_KEYWORDS):
            signal = _normalize_live_disruption(row)
            if signal["event_id"]:
                signals.append(signal)
    return signals


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Supply Chain Network
# ---------------------------------------------------------------------------

SUPPLY_ROUTES = {
    "RT-APAC-01": {
        "name": "Asia-Pacific Primary",
        "origin": "Shenzhen, China",
        "destination": "Los Angeles, CA",
        "transport_mode": "ocean_freight",
        "transit_days": 18,
        "carriers": ["COSCO Shipping", "Evergreen Marine"],
        "annual_volume_teu": 4800,
        "annual_value_usd": 28500000.00,
        "categories": ["Electronics", "Accessories"],
        "current_status": "disrupted",
        "reliability_score": 0.82,
    },
    "RT-EURO-01": {
        "name": "European Apparel Route",
        "origin": "Porto, Portugal",
        "destination": "Newark, NJ",
        "transport_mode": "ocean_freight",
        "transit_days": 12,
        "carriers": ["Maersk Line", "MSC"],
        "annual_volume_teu": 2200,
        "annual_value_usd": 15800000.00,
        "categories": ["Apparel"],
        "current_status": "at_risk",
        "reliability_score": 0.91,
    },
    "RT-DOMESTIC-01": {
        "name": "West Coast to Midwest",
        "origin": "Los Angeles, CA",
        "destination": "Chicago, IL",
        "transport_mode": "intermodal_rail",
        "transit_days": 4,
        "carriers": ["Union Pacific", "BNSF Railway"],
        "annual_volume_teu": 6500,
        "annual_value_usd": 42000000.00,
        "categories": ["Electronics", "Accessories", "Apparel", "Footwear"],
        "current_status": "normal",
        "reliability_score": 0.95,
    },
    "RT-LATAM-01": {
        "name": "Central America Footwear",
        "origin": "Leon, Mexico",
        "destination": "Dallas, TX",
        "transport_mode": "trucking",
        "transit_days": 3,
        "carriers": ["J.B. Hunt", "Werner Enterprises"],
        "annual_volume_teu": 1800,
        "annual_value_usd": 12400000.00,
        "categories": ["Footwear"],
        "current_status": "normal",
        "reliability_score": 0.93,
    },
    "RT-SEASIA-01": {
        "name": "Southeast Asia Textiles",
        "origin": "Ho Chi Minh City, Vietnam",
        "destination": "Savannah, GA",
        "transport_mode": "ocean_freight",
        "transit_days": 22,
        "carriers": ["Yang Ming", "ONE Line"],
        "annual_volume_teu": 3100,
        "annual_value_usd": 19200000.00,
        "categories": ["Apparel", "Home"],
        "current_status": "disrupted",
        "reliability_score": 0.78,
    },
}

DISRUPTION_EVENTS = {
    "DISR-001": {
        "title": "Port Congestion — Los Angeles/Long Beach",
        "type": "port_congestion",
        "severity": "high",
        "affected_routes": ["RT-APAC-01"],
        "start_date": "2026-03-05",
        "estimated_resolution": "2026-03-28",
        "delay_days": 8,
        "affected_skus": ["SKU-1002", "SKU-1004", "SKU-1006", "SKU-1008"],
        "estimated_revenue_impact": 2150000.00,
        "description": (
            "Severe vessel queue at LA/LB ports due to labor slowdown and "
            "equipment shortages. Average vessel wait time is 6 days."
        ),
        "status": "active",
    },
    "DISR-002": {
        "title": "Typhoon Disruption — South China Sea",
        "type": "weather_event",
        "severity": "critical",
        "affected_routes": ["RT-APAC-01", "RT-SEASIA-01"],
        "start_date": "2026-03-10",
        "estimated_resolution": "2026-03-20",
        "delay_days": 12,
        "affected_skus": ["SKU-1002", "SKU-1003", "SKU-1004", "SKU-1006", "SKU-1008", "SKU-1010"],
        "estimated_revenue_impact": 3800000.00,
        "description": (
            "Typhoon Mirinae forcing rerouting of vessels through northern "
            "Pacific corridor. Multiple sailings cancelled or delayed."
        ),
        "status": "active",
    },
    "DISR-003": {
        "title": "EU Customs Regulation Change",
        "type": "regulatory",
        "severity": "medium",
        "affected_routes": ["RT-EURO-01"],
        "start_date": "2026-03-01",
        "estimated_resolution": "2026-04-15",
        "delay_days": 5,
        "affected_skus": ["SKU-1001", "SKU-1003"],
        "estimated_revenue_impact": 720000.00,
        "description": (
            "New EU sustainability documentation requirements adding processing "
            "time at origin. Additional compliance certificates needed for textiles."
        ),
        "status": "active",
    },
}

RISK_SCORES = {
    "RT-APAC-01": {
        "overall_risk": 0.78,
        "geopolitical": 0.65,
        "weather": 0.82,
        "infrastructure": 0.70,
        "labor": 0.75,
        "regulatory": 0.40,
        "financial": 0.35,
    },
    "RT-EURO-01": {
        "overall_risk": 0.45,
        "geopolitical": 0.30,
        "weather": 0.20,
        "infrastructure": 0.25,
        "labor": 0.35,
        "regulatory": 0.72,
        "financial": 0.28,
    },
    "RT-DOMESTIC-01": {
        "overall_risk": 0.22,
        "geopolitical": 0.05,
        "weather": 0.30,
        "infrastructure": 0.20,
        "labor": 0.25,
        "regulatory": 0.10,
        "financial": 0.15,
    },
    "RT-LATAM-01": {
        "overall_risk": 0.35,
        "geopolitical": 0.25,
        "weather": 0.15,
        "infrastructure": 0.40,
        "labor": 0.30,
        "regulatory": 0.45,
        "financial": 0.32,
    },
    "RT-SEASIA-01": {
        "overall_risk": 0.72,
        "geopolitical": 0.50,
        "weather": 0.85,
        "infrastructure": 0.55,
        "labor": 0.40,
        "regulatory": 0.48,
        "financial": 0.30,
    },
}

MITIGATION_PLAYBOOKS = {
    "port_congestion": {
        "label": "Port Congestion Mitigation",
        "immediate_actions": [
            "Divert eligible shipments to alternate ports (Oakland, Seattle-Tacoma)",
            "Activate premium drayage contracts for priority container retrieval",
            "Convert ocean shipments under 2 TEU to air freight for critical SKUs",
        ],
        "short_term_actions": [
            "Increase safety stock at distribution centers by 20%",
            "Negotiate priority berthing with carrier partners",
            "Activate cross-dock bypass for pre-cleared containers",
        ],
        "long_term_actions": [
            "Diversify port-of-entry strategy across West and East Coast",
            "Invest in inland port relationships for rail-direct receiving",
            "Develop dual-source contracts for top-volume categories",
        ],
        "estimated_mitigation_cost": 340000.00,
        "risk_reduction_pct": 45,
    },
    "weather_event": {
        "label": "Weather Event Mitigation",
        "immediate_actions": [
            "Activate emergency inventory reserves at regional warehouses",
            "Reroute in-transit vessels through safe corridors",
            "Expedite air freight for high-priority SKUs with less than 7 days supply",
        ],
        "short_term_actions": [
            "Shift demand to in-stock alternative products via merchandising",
            "Enable backorder with guaranteed delivery dates for affected items",
            "Communicate proactively with B2B customers on revised timelines",
        ],
        "long_term_actions": [
            "Integrate real-time weather monitoring into planning systems",
            "Build seasonal safety stock buffers for typhoon/hurricane seasons",
            "Qualify backup suppliers in geographically diverse regions",
        ],
        "estimated_mitigation_cost": 520000.00,
        "risk_reduction_pct": 55,
    },
    "regulatory": {
        "label": "Regulatory Change Mitigation",
        "immediate_actions": [
            "Engage customs broker to prepare updated documentation templates",
            "Pre-certify next 3 shipments with new compliance requirements",
            "Brief all origin-side partners on updated export procedures",
        ],
        "short_term_actions": [
            "Conduct compliance audit of all active POs on affected routes",
            "Update vendor manual with new regulatory requirements",
            "Schedule training session for procurement team",
        ],
        "long_term_actions": [
            "Subscribe to regulatory change monitoring service",
            "Build compliance buffer time into standard lead times",
            "Develop relationships with in-country compliance consultants",
        ],
        "estimated_mitigation_cost": 85000.00,
        "risk_reduction_pct": 70,
    },
}

ALTERNATIVE_SUPPLIERS = {
    "Electronics": [
        {
            "name": "TechSource Taiwan",
            "location": "Taipei, Taiwan",
            "lead_time_days": 21,
            "quality_rating": 4.5,
            "capacity_units_monthly": 15000,
            "price_premium_pct": 8.0,
            "certifications": ["ISO 9001", "ISO 14001"],
            "min_order_qty": 500,
        },
        {
            "name": "KoreanTech Partners",
            "location": "Incheon, South Korea",
            "lead_time_days": 19,
            "quality_rating": 4.7,
            "capacity_units_monthly": 10000,
            "price_premium_pct": 12.0,
            "certifications": ["ISO 9001", "IATF 16949"],
            "min_order_qty": 300,
        },
    ],
    "Apparel": [
        {
            "name": "TurkTex Industries",
            "location": "Istanbul, Turkey",
            "lead_time_days": 16,
            "quality_rating": 4.3,
            "capacity_units_monthly": 25000,
            "price_premium_pct": 5.0,
            "certifications": ["GOTS", "OEKO-TEX"],
            "min_order_qty": 1000,
        },
        {
            "name": "BanglaStitch Ltd",
            "location": "Dhaka, Bangladesh",
            "lead_time_days": 25,
            "quality_rating": 4.0,
            "capacity_units_monthly": 40000,
            "price_premium_pct": -3.0,
            "certifications": ["WRAP", "BSCI"],
            "min_order_qty": 2000,
        },
    ],
    "Footwear": [
        {
            "name": "IndoSole Manufacturing",
            "location": "Tangerang, Indonesia",
            "lead_time_days": 28,
            "quality_rating": 4.2,
            "capacity_units_monthly": 18000,
            "price_premium_pct": 2.0,
            "certifications": ["ISO 9001", "SA8000"],
            "min_order_qty": 800,
        },
    ],
    "Accessories": [
        {
            "name": "IndiaGlobal Accessories",
            "location": "Mumbai, India",
            "lead_time_days": 24,
            "quality_rating": 4.1,
            "capacity_units_monthly": 30000,
            "price_premium_pct": -5.0,
            "certifications": ["ISO 9001"],
            "min_order_qty": 1500,
        },
        {
            "name": "MediterraneanCraft Co",
            "location": "Florence, Italy",
            "lead_time_days": 14,
            "quality_rating": 4.8,
            "capacity_units_monthly": 5000,
            "price_premium_pct": 25.0,
            "certifications": ["ISO 9001", "Made in Italy"],
            "min_order_qty": 200,
        },
    ],
    "Home": [
        {
            "name": "ThaiHome Products",
            "location": "Bangkok, Thailand",
            "lead_time_days": 20,
            "quality_rating": 4.3,
            "capacity_units_monthly": 12000,
            "price_premium_pct": 4.0,
            "certifications": ["ISO 9001", "FSC"],
            "min_order_qty": 600,
        },
    ],
}

EVIDENCE_CAPABILITIES = {
    "disruption_impact": {
        "title": "Disruption Root Cause and Impact",
        "source_system": "Dynamics 365 Supply Chain Management",
        "write": False,
        "key_field": "incident_id",
        "summary": (
            "Connects a detected disruption to root cause, severity, affected "
            "stores, SKUs, revenue, and customer impact."
        ),
        "record": {
            "incident_id": "INC-PORTLAND-DC",
            "root_cause": "Portland distribution-center conveyor failure causing a 3-day backlog",
            "scope": "12 Northwest stores; 143 products; Seattle Flagship at 47% stockout",
            "category_impact": "Electronics 42 SKUs; apparel 38; home goods 31; sporting 32",
            "revenue_exposure": "$84,300 per week and escalating",
            "customer_impact": "37 complaints, 280% above baseline, with social mentions rising",
            "severity": "Critical; immediate management decision required",
        },
    },
    "response_scenarios": {
        "title": "Emergency Response Scenarios",
        "source_system": "Dynamics 365 Supply Chain Management",
        "write": False,
        "key_field": "scenario_id",
        "summary": (
            "Compares response timelines, fulfillment coverage, cost, revenue "
            "recovery, and ROI before making a recommendation."
        ),
        "record": {
            "scenario_id": "SCENARIO-DENVER-TRANSFER",
            "option_a": "Denver DC transfer; 36 hours; 80 priority SKUs; $15,600 cost; $47,000 recovery; 3:1 ROI",
            "option_b": "Wait for Portland; 2 days; 40% restored; $0 response cost; $127,000 additional loss",
            "expansion": "Add five high-impact stores for $8,900, bringing total response investment to $24,500",
            "recommendation": "Execute Denver transfer and five-store expansion to protect $78,000 revenue",
        },
    },
    "response_execution": {
        "title": "Emergency Response Execution",
        "source_system": "Dynamics 365 Supply Chain Management and Microsoft Teams",
        "write": True,
        "key_field": "execution_id",
        "summary": (
            "Prepares transfer, receiving, restocking, and notification actions "
            "without triggering connected operations systems."
        ),
        "record": {
            "execution_id": "EXEC-DENVER-NORTHWEST",
            "seattle": "80 priority electronics SKUs; simulated departure 18:00; simulated arrival Friday 10:00",
            "additional_stores": "Portland South, Tacoma Mall, Bellevue Square, Olympia Center, Spokane Valley; 60 SKUs each",
            "coordination": "Store notifications, receiving staff, tablet restocking plans, and customer SMS prepared",
            "economics": "$24,500 response investment; $78,000 projected recovery",
            "execution_note": "Simulation only; no freight, workflow, staffing, or notification action occurs",
        },
    },
    "recovery_tracking": {
        "title": "Shipment Tracking and Recovery Plan",
        "source_system": "Dynamics 365 Supply Chain Management",
        "write": False,
        "key_field": "tracking_id",
        "summary": (
            "Provides deterministic shipment status, recovery milestones, "
            "backlog clearance, and prevention recommendations."
        ),
        "record": {
            "tracking_id": "TRACK-DENVER-PORTLAND",
            "shipment": "Denver truck departed 18:04; Seattle ETA Friday 09:47; on schedule",
            "repair": "Conveyor repair Thursday 20:00; backlog processing Friday 06:00; normal operations Friday noon",
            "backlog": "340 pending orders; Seattle and affected stores first; full clearance Saturday end of day",
            "prevention": "$145,000 backup conveyor; 48-hour installation; $340,000 three-year avoided-loss value",
        },
    },
    "incident_report": {
        "title": "Incident Report and Leadership Distribution",
        "source_system": "Microsoft Teams",
        "write": True,
        "key_field": "report_id",
        "summary": (
            "Builds a financial and operational incident report with a "
            "simulated leadership distribution receipt."
        ),
        "record": {
            "report_id": "REPORT-PORTLAND-DC",
            "financial_impact": "$84,300 at risk; $24,500 response cost; $78,000 recovered; $53,500 net value protected",
            "performance": "47 minutes detection-to-action; 36-hour alternate DC activation; 95% inventory in 3 days",
            "lessons": "Backup conveyor, multi-DC sourcing rules, and monitoring tuned to reduce response by 18 minutes",
            "prevention_value": "$340,000 avoided losses over three years versus $145,000 investment",
            "distribution": "Prepared for executive team review in Microsoft Teams",
        },
    },
}

_EVIDENCE_KEY_PUNCTUATION = "-_.,:;()?!/#@+$%^&*=[]{}<>~`'\""


def _normalize_evidence_tokens(text):
    tokens = []
    for raw in str(text).split():
        cleaned = "".join(
            character.lower()
            for character in raw
            if character not in _EVIDENCE_KEY_PUNCTUATION
        )
        if cleaned:
            tokens.append(cleaned)
    return tokens


def _record_for_evidence_request(capability, key, user_input):
    record = capability["record"]
    key_field = capability["key_field"]
    if key:
        if str(record[key_field]).lower() == str(key).strip().lower():
            return "match", record
        return "not_found", None
    query_tokens = _normalize_evidence_tokens(user_input)
    key_tokens = _normalize_evidence_tokens(record[key_field])
    width = len(key_tokens)
    if width and any(
        query_tokens[index:index + width] == key_tokens
        for index in range(len(query_tokens) - width + 1)
    ):
        return "match", record
    return "summary", None


def _format_evidence_record(record):
    return "\n".join(
        f"- **{field.replace('_', ' ').title()}:** {value}"
        for field, value in record.items()
    )


# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

def _total_revenue_at_risk():
    return sum(d["estimated_revenue_impact"] for d in DISRUPTION_EVENTS.values() if d["status"] == "active")


def _affected_route_count():
    affected = set()
    for d in DISRUPTION_EVENTS.values():
        if d["status"] == "active":
            affected.update(d["affected_routes"])
    return len(affected)


def _risk_level_label(score):
    if score >= 0.70:
        return "HIGH"
    if score >= 0.40:
        return "MEDIUM"
    return "LOW"


def _total_mitigation_cost():
    seen_types = set()
    total = 0.0
    for d in DISRUPTION_EVENTS.values():
        if d["status"] == "active" and d["type"] not in seen_types:
            pb = MITIGATION_PLAYBOOKS.get(d["type"], {})
            total += pb.get("estimated_mitigation_cost", 0)
            seen_types.add(d["type"])
    return total


def _best_alternative(category):
    alts = ALTERNATIVE_SUPPLIERS.get(category, [])
    if not alts:
        return None
    return min(alts, key=lambda a: a["lead_time_days"])


# ---------------------------------------------------------------------------
# Agent Class
# ---------------------------------------------------------------------------

class SupplyChainDisruptionAlertAgent(BasicAgent):
    """Agent for supply chain disruption monitoring and mitigation."""

    def __init__(self):
        self.name = "supply-chain-disruption-alert-agent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "disruption_dashboard",
                            "risk_assessment",
                            "mitigation_plan",
                            "supplier_alternatives",
                            "disruption_impact",
                            "response_scenarios",
                            "response_execution",
                            "recovery_tracking",
                            "incident_report",
                        ],
                    },
                    "route_id": {"type": "string"},
                    "disruption_id": {"type": "string"},
                    "category": {"type": "string"},
                    "key": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _live_disruption_dashboard(self, signals):
        """Disruption feed built from live tenant cases (preferred online)."""
        open_signals = [s for s in signals if s["open"]]
        lines = [
            "# Supply Chain Disruption Dashboard — Live Tenant Signals",
            "",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "In this template a disruption signal is a Dynamics case. Pass",
            "`route_id` or `disruption_id` for the embedded demo network view.",
            "",
            "| Case | Event | Customer | Severity | Status | Age | Revenue Impact |",
            "|------|-------|----------|----------|--------|-----|----------------|",
        ]
        for s in sorted(signals, key=lambda x: x["event_id"]):
            impact = (
                "n/a — enrichment seam"
                if s["revenue_impact"] is None
                else f"${s['revenue_impact']:,.2f}"
            )
            lines.append(
                f"| {s['event_id']} | {s['title']} | {s['customer']} "
                f"| {s['severity']} | {s['status']} | {s['age_days']}d | {impact} |"
            )
        high = sum(1 for s in open_signals if s["severity"] == "High")
        lines.append("")
        lines.append(
            f"**Active signals:** {len(open_signals)} open of {len(signals)} matched "
            f"| **High severity:** {high}"
        )
        lines.append(
            "Affected routes and revenue impact need your TMS/planning system — "
            "wire it at the LIVE DATA SEAM."
        )
        return "\n".join(lines)

    def _disruption_dashboard(self, **kwargs):
        if not kwargs.get("route_id") and not kwargs.get("disruption_id"):
            signals = _live_disruption_signals()
            if signals:
                return self._live_disruption_dashboard(signals)
        rev_at_risk = _total_revenue_at_risk()
        routes_affected = _affected_route_count()
        lines = [
            "# Supply Chain Disruption Dashboard",
            "",
            f"**Active Disruptions:** {len([d for d in DISRUPTION_EVENTS.values() if d['status'] == 'active'])}",
            f"**Routes Affected:** {routes_affected} of {len(SUPPLY_ROUTES)}",
            f"**Total Revenue at Risk:** ${rev_at_risk:,.2f}",
            "",
            "## Active Disruption Events",
            "",
            "| ID | Title | Type | Severity | Delay | Revenue Impact | Resolution ETA |",
            "|----|-------|------|----------|-------|----------------|----------------|",
        ]
        for did, d in DISRUPTION_EVENTS.items():
            if d["status"] == "active":
                lines.append(
                    f"| {did} | {d['title']} | {d['type'].replace('_', ' ')} "
                    f"| {d['severity'].upper()} | +{d['delay_days']}d "
                    f"| ${d['estimated_revenue_impact']:,.2f} | {d['estimated_resolution']} |"
                )
        lines.append("")
        lines.append("## Route Status Overview")
        lines.append("")
        lines.append("| Route | Origin | Destination | Mode | Status | Reliability |")
        lines.append("|-------|--------|-------------|------|--------|-------------|")
        for rid, route in SUPPLY_ROUTES.items():
            status_display = route["current_status"].upper().replace("_", " ")
            lines.append(
                f"| {route['name']} | {route['origin']} | {route['destination']} "
                f"| {route['transport_mode'].replace('_', ' ')} "
                f"| {status_display} | {route['reliability_score']*100:.0f}% |"
            )
        lines.append("")
        for did, d in DISRUPTION_EVENTS.items():
            if d["status"] == "active":
                lines.append(f"### {did}: {d['title']}")
                lines.append("")
                lines.append(f"{d['description']}")
                lines.append("")
                lines.append(f"**Affected SKUs:** {', '.join(d['affected_skus'])}")
                lines.append(f"**Affected Routes:** {', '.join(d['affected_routes'])}")
                lines.append("")
        return "\n".join(lines)

    def _risk_assessment(self, **kwargs):
        route_id = kwargs.get("route_id")
        if route_id and route_id in RISK_SCORES:
            routes = {route_id: RISK_SCORES[route_id]}
        else:
            routes = RISK_SCORES
        lines = [
            "# Supply Chain Risk Assessment",
            "",
            "## Risk Score Matrix",
            "",
            "| Route | Overall | Geopolitical | Weather | Infrastructure | Labor | Regulatory | Financial |",
            "|-------|---------|--------------|---------|----------------|-------|------------|-----------|",
        ]
        for rid, scores in routes.items():
            route_name = SUPPLY_ROUTES.get(rid, {}).get("name", rid)
            level = _risk_level_label(scores["overall_risk"])
            lines.append(
                f"| {route_name} | **{scores['overall_risk']:.2f}** ({level}) "
                f"| {scores['geopolitical']:.2f} | {scores['weather']:.2f} "
                f"| {scores['infrastructure']:.2f} | {scores['labor']:.2f} "
                f"| {scores['regulatory']:.2f} | {scores['financial']:.2f} |"
            )
        lines.append("")
        lines.append("## Risk Level Distribution")
        lines.append("")
        high = sum(1 for s in RISK_SCORES.values() if s["overall_risk"] >= 0.70)
        med = sum(1 for s in RISK_SCORES.values() if 0.40 <= s["overall_risk"] < 0.70)
        low = sum(1 for s in RISK_SCORES.values() if s["overall_risk"] < 0.40)
        lines.append(f"- **HIGH risk routes:** {high}")
        lines.append(f"- **MEDIUM risk routes:** {med}")
        lines.append(f"- **LOW risk routes:** {low}")
        lines.append("")
        lines.append("## Highest Risk Factors")
        lines.append("")
        all_factors = {}
        for scores in RISK_SCORES.values():
            for factor in ["geopolitical", "weather", "infrastructure", "labor", "regulatory", "financial"]:
                all_factors.setdefault(factor, []).append(scores[factor])
        for factor, values in sorted(all_factors.items(), key=lambda x: -max(x[1])):
            avg_score = sum(values) / len(values)
            peak = max(values)
            lines.append(f"- **{factor.title()}:** avg {avg_score:.2f}, peak {peak:.2f}")
        return "\n".join(lines)

    def _mitigation_plan(self, **kwargs):
        disruption_id = kwargs.get("disruption_id")
        if disruption_id and disruption_id in DISRUPTION_EVENTS:
            events = {disruption_id: DISRUPTION_EVENTS[disruption_id]}
        else:
            events = {k: v for k, v in DISRUPTION_EVENTS.items() if v["status"] == "active"}
        total_cost = _total_mitigation_cost()
        lines = [
            "# Disruption Mitigation Plan",
            "",
            f"**Estimated Total Mitigation Investment:** ${total_cost:,.2f}",
            "",
        ]
        for did, event in events.items():
            playbook = MITIGATION_PLAYBOOKS.get(event["type"], {})
            if not playbook:
                continue
            lines.append(f"## {did}: {event['title']}")
            lines.append(f"**Playbook:** {playbook['label']}")
            lines.append(f"**Expected Risk Reduction:** {playbook['risk_reduction_pct']}%")
            lines.append(f"**Mitigation Cost:** ${playbook['estimated_mitigation_cost']:,.2f}")
            lines.append("")
            lines.append("### Immediate Actions (0-48 hours)")
            for action in playbook["immediate_actions"]:
                lines.append(f"1. {action}")
            lines.append("")
            lines.append("### Short-Term Actions (1-2 weeks)")
            for action in playbook["short_term_actions"]:
                lines.append(f"1. {action}")
            lines.append("")
            lines.append("### Long-Term Actions (1-3 months)")
            for action in playbook["long_term_actions"]:
                lines.append(f"1. {action}")
            lines.append("")
        return "\n".join(lines)

    def _supplier_alternatives(self, **kwargs):
        category = kwargs.get("category")
        if category and category in ALTERNATIVE_SUPPLIERS:
            cats = {category: ALTERNATIVE_SUPPLIERS[category]}
        else:
            cats = ALTERNATIVE_SUPPLIERS
        lines = ["# Alternative Supplier Directory", ""]
        for cat_name, suppliers in cats.items():
            best = _best_alternative(cat_name)
            lines.append(f"## {cat_name}")
            if best:
                lines.append(f"**Recommended (fastest lead time):** {best['name']} — {best['lead_time_days']}d")
            lines.append("")
            lines.append("| Supplier | Location | Lead Time | Quality | Capacity/Mo | Price Premium | MOQ |")
            lines.append("|----------|----------|-----------|---------|-------------|---------------|-----|")
            for sup in suppliers:
                premium_str = f"+{sup['price_premium_pct']:.1f}%" if sup["price_premium_pct"] >= 0 else f"{sup['price_premium_pct']:.1f}%"
                lines.append(
                    f"| {sup['name']} | {sup['location']} | {sup['lead_time_days']}d "
                    f"| {sup['quality_rating']}/5.0 | {sup['capacity_units_monthly']:,} "
                    f"| {premium_str} | {sup['min_order_qty']:,} |"
                )
            lines.append("")
            lines.append("**Certifications:**")
            for sup in suppliers:
                lines.append(f"- {sup['name']}: {', '.join(sup['certifications'])}")
            lines.append("")
        total_suppliers = sum(len(s) for s in ALTERNATIVE_SUPPLIERS.values())
        lines.append(f"**Total Qualified Alternatives:** {total_suppliers} suppliers across {len(ALTERNATIVE_SUPPLIERS)} categories")
        return "\n".join(lines)

    def _evidence_capability(self, capability_name, **kwargs):
        capability = EVIDENCE_CAPABILITIES[capability_name]
        lookup_status, record = _record_for_evidence_request(
            capability,
            kwargs.get("key", ""),
            kwargs.get("user_input", ""),
        )
        lines = [
            f"# {capability['title']}",
            "",
            capability["summary"],
            "",
            f"## {capability['source_system']} (synthetic demo data)",
            "",
        ]
        if lookup_status == "not_found":
            lines.append(
                f"No record matched the requested {capability['key_field']}. "
                "Not substituting another record."
            )
        else:
            selected = record or capability["record"]
            label = "Exact keyed record" if lookup_status == "match" else "Worked example"
            lines.extend([f"**{label}:**", _format_evidence_record(selected)])

        if capability["write"] and lookup_status == "match":
            receipt_key = record[capability["key_field"]]
            lines.extend([
                "",
                "## Simulated Write Receipt",
                "",
                "- **Action Status:** simulated",
                f"- **Receipt:** SIM-{capability_name.upper()}-{receipt_key}",
                f"- **Target System:** {capability['source_system']}",
                "- **External Changes:** none; no live freight, workflow, message, or report distribution occurred",
            ])
        elif capability["write"]:
            lines.extend([
                "",
                "_Write-capable workflow; provide an exact key to generate a "
                "simulated receipt. No external system is modified._",
            ])
        else:
            lines.extend(["", "_Read-only; no external system is modified._"])
        return "\n".join(lines)

    def perform(self, **kwargs):
        operation = kwargs.get("operation", "disruption_dashboard")
        dispatch = {
            "disruption_dashboard": self._disruption_dashboard,
            "risk_assessment": self._risk_assessment,
            "mitigation_plan": self._mitigation_plan,
            "supplier_alternatives": self._supplier_alternatives,
            "disruption_impact": self._evidence_capability,
            "response_scenarios": self._evidence_capability,
            "response_execution": self._evidence_capability,
            "recovery_tracking": self._evidence_capability,
            "incident_report": self._evidence_capability,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        if operation in EVIDENCE_CAPABILITIES:
            return handler(operation, **kwargs)
        return handler(**kwargs)


# ---------------------------------------------------------------------------
# Main — exercise all operations
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = SupplyChainDisruptionAlertAgent()
    print("=" * 80)
    print("EMBEDDED DEMO NETWORK (works offline)")
    print(agent.perform(operation="disruption_dashboard", disruption_id="DISR-002"))
    print("\n" + "=" * 80)
    print("LIVE TENANT DISRUPTION SIGNALS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="disruption_dashboard"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="risk_assessment", route_id="RT-APAC-01"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="mitigation_plan", disruption_id="DISR-002"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="supplier_alternatives", category="Electronics"))
    print("=" * 80)
