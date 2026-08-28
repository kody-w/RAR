---
name: "rar-aibast-agents-library-store-associate-copilot"
description: "Gives associates product lookups, scripts, dashboards, and a live refrigeration alert joining simulated telemetry to CRM, with offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/store_associate_copilot", "rar_sha256": "9c75b3deb9ab3750efe6e8dd200630a35dcb42458dc799fc57ae729309ae9a26", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["store-operations", "associate", "copilot", "product-lookup", "retail"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/store_associate_copilot`. The original RAPP
agent is preserved byte-for-byte in `store_associate_copilot_agent.py` and in the RCI capsule.

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

Store Associate Copilot Agent — a template you are meant to mutate.

Empowers store associates with product lookup, customer assistance
scripts, daily task management, and performance dashboards.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
            — the product catalog and store cases
       TEL  https://kody-w.github.io/static-telemetry/api/v1/
            — sensors, alerts, and 672-point reading series
     Try: perform(operation="product_lookup", query="Mobile Cart")
     — with network up, that finds the tenant's live "Mobile Cart M8"
     (AST-CRT-008) even though it is not in the embedded catalog.
     Try: perform(operation="task_checklist")
     — the checklist now ends with the LIVE store alert: the
     temperature_excursion on Harbor Lights Grocery's refrigeration
     case R-4 (aisle four), joined by ticket number to CRM case
     CAS-260138 — the case that was created via the CRM Write API.
  2. No network? Everything falls back to the embedded demo layer below
     (PRODUCT_CATALOG / DAILY_TASK_LIST) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     STORE_ASSOCIATE_COPILOT_DATA_URL (CRM) and/or
     STORE_ASSOCIATE_COPILOT_TEL_URL (telemetry) to your own endpoints
     (your real Dynamics org, your store IoT platform), or replace
     _fetch_collection() / _fetch_telemetry() with your own catalog
     API. The fields the rest of the file needs are listed in
     _normalize_live_product() — aisle location, on-hand, sizes, and
     care instructions stay "n/a — enrichment seam" until you wire your
     store systems.

OPERATIONS
  product_lookup | customer_assist | task_checklist |
  performance_dashboard | product_intelligence | add_on_commission |
  product_comparison | transaction_preparation
  kwargs: operation (required), query, sku_id, scenario, shift, key,
  user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "key": {
      "description": "Exact record key for a v1.1.0 evidence operation.",
      "type": "string"
    },
    "operation": {
      "enum": [
        "product_lookup",
        "customer_assist",
        "task_checklist",
        "performance_dashboard",
        "product_intelligence",
        "add_on_commission",
        "product_comparison",
        "transaction_preparation"
      ],
      "type": "string"
    },
    "query": {
      "type": "string"
    },
    "scenario": {
      "type": "string"
    },
    "shift": {
      "type": "string"
    },
    "sku_id": {
      "type": "string"
    },
    "user_input": {
      "description": "Optional request containing an exact v1.1.0 record key.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `store_associate_copilot_agent.py` and embedded as the fenced Python below (sha256 9c75b3deb9ab3750…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `store_associate_copilot_agent.py` first:

```bash
python3 store_associate_copilot_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 store_associate_copilot_agent.py   # or on stdin
python3 store_associate_copilot_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Store Associate Copilot Agent — a template you are meant to mutate.

Empowers store associates with product lookup, customer assistance
scripts, daily task management, and performance dashboards.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
            — the product catalog and store cases
       TEL  https://kody-w.github.io/static-telemetry/api/v1/
            — sensors, alerts, and 672-point reading series
     Try: perform(operation="product_lookup", query="Mobile Cart")
     — with network up, that finds the tenant's live "Mobile Cart M8"
     (AST-CRT-008) even though it is not in the embedded catalog.
     Try: perform(operation="task_checklist")
     — the checklist now ends with the LIVE store alert: the
     temperature_excursion on Harbor Lights Grocery's refrigeration
     case R-4 (aisle four), joined by ticket number to CRM case
     CAS-260138 — the case that was created via the CRM Write API.
  2. No network? Everything falls back to the embedded demo layer below
     (PRODUCT_CATALOG / DAILY_TASK_LIST) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     STORE_ASSOCIATE_COPILOT_DATA_URL (CRM) and/or
     STORE_ASSOCIATE_COPILOT_TEL_URL (telemetry) to your own endpoints
     (your real Dynamics org, your store IoT platform), or replace
     _fetch_collection() / _fetch_telemetry() with your own catalog
     API. The fields the rest of the file needs are listed in
     _normalize_live_product() — aisle location, on-hand, sizes, and
     care instructions stay "n/a — enrichment seam" until you wire your
     store systems.

OPERATIONS
  product_lookup | customer_assist | task_checklist |
  performance_dashboard | product_intelligence | add_on_commission |
  product_comparison | transaction_preparation
  kwargs: operation (required), query, sku_id, scenario, shift, key,
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

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/store_associate_copilot",
    "version": "1.3.0",
    "display_name": "Store Associate Copilot Agent",
    "description": (
        "Gives associates product lookups, scripts, dashboards, and a live refrigeration alert joining simulated telemetry to CRM, with offline fallback."
    ),
    "author": "AIBAST",
    "tags": [
        "store-operations",
        "associate",
        "copilot",
        "product-lookup",
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
#   export STORE_ASSOCIATE_COPILOT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your commerce client. Downstream
# code only needs the fields produced by _normalize_live_product().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "STORE_ASSOCIATE_COPILOT_DATA_URL",
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


# Sibling live source: the static-telemetry API. Its refrigeration
# temperature_excursion alert on Harbor Lights Grocery joins CRM case
# CAS-260138 (created via the CRM Write API) and surfaces on the task
# checklist. Override with STORE_ASSOCIATE_COPILOT_TEL_URL.
TELEMETRY_SOURCE_URL = os.environ.get(
    "STORE_ASSOCIATE_COPILOT_TEL_URL",
    "https://kody-w.github.io/static-telemetry/api/v1",
)


def _fetch_telemetry(path, key="value", timeout=6):
    """Bounded GET against the telemetry API, cached in _LIVE_CACHE by
    full URL. Returns [] on ANY failure — offline-safe. Reading series
    are large (672 points each) — fetch them lazily, at most a couple
    per run."""
    url = f"{TELEMETRY_SOURCE_URL}/{path}.json"
    if url in _LIVE_CACHE:
        return _LIVE_CACHE[url]
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "rapp-agent-template/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8")).get(key, [])
    except Exception:
        data = []
    _LIVE_CACHE[url] = data
    return data


def _store_refrigeration_alert():
    """The live Harbor Lights Grocery temperature_excursion alert
    joined to its real CRM case (CAS-260138 — created via the CRM
    Write API), with stats over the case-temperature reading series
    (ONE lazy 672-point fetch); None when offline."""
    alert = next(
        (a for a in _fetch_telemetry("alerts")
         if a.get("alert_type") == "temperature_excursion"),
        None,
    )
    if not alert:
        return None
    case = next(
        (c for c in _fetch_collection("incidents")
         if c.get("ticketnumber") == alert.get("crm_case")),
        None,
    )
    points = _fetch_telemetry(
        f"readings/{alert.get('sensor_id')}", key="points"
    )
    values = [
        p.get("v") for p in points if isinstance(p.get("v"), (int, float))
    ]
    return {
        "alert": alert,
        "case": case,
        "latest": values[-1] if values else None,
        "max": max(values) if values else None,
        "n": len(values),
    }


def _normalize_live_product(row):
    """Project a Dynamics product record onto the catalog shape this agent
    uses. THIS is the contract your replacement data source must meet — a
    dict with these keys. None means 'not available from the catalog
    alone' and the renderer labels it as an enrichment seam."""
    def _f(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return None
    features = [row["description"]] if row.get("description") else []
    return {
        "sku_id": row.get("productnumber") or row.get("productid", ""),
        "name": row.get("name", "Unknown"),
        "category": row.get(
            "producttypecode@OData.Community.Display.V1.FormattedValue", "General"
        ),
        "brand": "Aster Lane Office Systems (live tenant)",
        "retail_price": _f(row.get("price")),
        "sizes": None,            # enrichment seam — wire your PIM
        "colors": None,           # enrichment seam
        "materials": None,        # enrichment seam
        "care": None,             # enrichment seam
        "location_aisle": None,   # enrichment seam — wire store planogram
        "location_shelf": None,   # enrichment seam
        "on_hand": None,          # enrichment seam — wire your POS/WMS
        "upc": None,              # enrichment seam
        "features": features,
        "_live": True,
    }


def _na(value, fmt="{}"):
    """None = the source system alone can't know this (enrichment seam)."""
    if value is None:
        return "n/a — enrichment seam"
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    return fmt.format(value)


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Product Catalog
# ---------------------------------------------------------------------------

PRODUCT_CATALOG = {
    "SKU-1001": {
        "name": "Classic Denim Jacket",
        "category": "Apparel",
        "brand": "Heritage Line",
        "retail_price": 89.99,
        "sizes": ["XS", "S", "M", "L", "XL", "XXL"],
        "colors": ["Indigo Wash", "Light Blue", "Black"],
        "materials": "100% cotton denim, brass buttons",
        "care": "Machine wash cold, tumble dry low",
        "location_aisle": "A3",
        "location_shelf": "Top rack",
        "on_hand": 74,
        "upc": "0-12345-67890-1",
        "features": ["Adjustable waist tabs", "Two chest pockets", "Vintage fade finish"],
    },
    "SKU-1002": {
        "name": "Wireless Earbuds Pro",
        "category": "Electronics",
        "brand": "SoundWave",
        "retail_price": 59.99,
        "sizes": ["One Size"],
        "colors": ["Matte Black", "Pearl White", "Navy"],
        "materials": "ABS plastic, silicone ear tips",
        "care": "Wipe with dry cloth. Do not submerge.",
        "location_aisle": "E1",
        "location_shelf": "Locked case",
        "on_hand": 132,
        "upc": "0-12345-67890-2",
        "features": ["Active noise cancellation", "8-hour battery", "IPX4 water resistant", "Bluetooth 5.3"],
    },
    "SKU-1003": {
        "name": "Organic Cotton T-Shirt",
        "category": "Apparel",
        "brand": "EcoBasics",
        "retail_price": 29.99,
        "sizes": ["XS", "S", "M", "L", "XL"],
        "colors": ["White", "Heather Grey", "Black", "Sage Green", "Dusty Rose"],
        "materials": "100% GOTS-certified organic cotton",
        "care": "Machine wash cold with like colors",
        "location_aisle": "A1",
        "location_shelf": "Mid rack",
        "on_hand": 210,
        "upc": "0-12345-67890-3",
        "features": ["Pre-shrunk", "Tagless comfort label", "Reinforced shoulder seams"],
    },
    "SKU-1004": {
        "name": "Smart Fitness Tracker",
        "category": "Electronics",
        "brand": "FitPulse",
        "retail_price": 129.99,
        "sizes": ["S/M Band", "L/XL Band"],
        "colors": ["Midnight Black", "Arctic White", "Forest Green"],
        "materials": "Aluminum case, fluoroelastomer band",
        "care": "Rinse with fresh water after swimming",
        "location_aisle": "E2",
        "location_shelf": "Display stand",
        "on_hand": 45,
        "upc": "0-12345-67890-4",
        "features": ["Heart rate monitor", "GPS tracking", "Sleep analysis", "7-day battery", "5ATM water resistant"],
    },
    "SKU-1005": {
        "name": "Premium Running Shoes",
        "category": "Footwear",
        "brand": "StrideMax",
        "retail_price": 149.99,
        "sizes": ["7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "12", "13"],
        "colors": ["Cloud White/Grey", "Black/Volt", "Navy/Orange"],
        "materials": "Engineered mesh upper, EVA foam midsole, rubber outsole",
        "care": "Spot clean with damp cloth. Air dry only.",
        "location_aisle": "F1",
        "location_shelf": "Wall display",
        "on_hand": 38,
        "upc": "0-12345-67890-5",
        "features": ["Responsive cushioning", "Breathable knit upper", "Reflective accents", "Carbon fiber plate"],
    },
    "SKU-1006": {
        "name": "Stainless Water Bottle",
        "category": "Accessories",
        "brand": "HydroKeep",
        "retail_price": 24.99,
        "sizes": ["20oz", "32oz"],
        "colors": ["Brushed Steel", "Matte Black", "Ocean Blue", "Coral"],
        "materials": "18/8 stainless steel, BPA-free lid",
        "care": "Hand wash recommended. Dishwasher safe (top rack).",
        "location_aisle": "C2",
        "location_shelf": "End cap",
        "on_hand": 195,
        "upc": "0-12345-67890-6",
        "features": ["Double-wall vacuum insulation", "24h cold / 12h hot", "Leak-proof lid", "Wide mouth"],
    },
    "SKU-1007": {
        "name": "Leather Crossbody Bag",
        "category": "Accessories",
        "brand": "UrbanCraft",
        "retail_price": 79.99,
        "sizes": ["One Size"],
        "colors": ["Cognac", "Black", "Olive"],
        "materials": "Full-grain leather, brass hardware",
        "care": "Condition with leather balm quarterly",
        "location_aisle": "B2",
        "location_shelf": "Display hooks",
        "on_hand": 61,
        "upc": "0-12345-67890-7",
        "features": ["Adjustable strap", "RFID-blocking pocket", "Three compartments", "YKK zippers"],
    },
    "SKU-1008": {
        "name": "UV Protection Sunglasses",
        "category": "Accessories",
        "brand": "ClearView",
        "retail_price": 44.99,
        "sizes": ["Standard", "Wide"],
        "colors": ["Tortoise", "Matte Black", "Crystal Clear"],
        "materials": "Acetate frame, polarized CR-39 lenses",
        "care": "Clean with included microfiber cloth. Store in case.",
        "location_aisle": "B1",
        "location_shelf": "Rotating display",
        "on_hand": 88,
        "upc": "0-12345-67890-8",
        "features": ["100% UV400 protection", "Polarized lenses", "Spring hinges", "Scratch-resistant coating"],
    },
    "SKU-1009": {
        "name": "Performance Yoga Mat",
        "category": "Fitness",
        "brand": "ZenGrip",
        "retail_price": 54.99,
        "sizes": ["68x24 in", "72x26 in"],
        "colors": ["Midnight Purple", "Sage", "Charcoal"],
        "materials": "Natural rubber base, polyurethane top layer",
        "care": "Wipe with damp cloth after use. Air dry flat.",
        "location_aisle": "F2",
        "location_shelf": "Standing rack",
        "on_hand": 42,
        "upc": "0-12345-67890-9",
        "features": ["Non-slip grip", "6mm thickness", "Alignment lines", "Carrying strap included"],
    },
    "SKU-1010": {
        "name": "Aromatherapy Candle Set",
        "category": "Home",
        "brand": "Luminary",
        "retail_price": 34.99,
        "sizes": ["3-pack (4oz each)"],
        "colors": ["Lavender/Eucalyptus/Vanilla"],
        "materials": "Soy wax, cotton wicks, essential oils",
        "care": "Trim wick to 1/4 inch before lighting. Burn max 4 hours.",
        "location_aisle": "D1",
        "location_shelf": "Feature table",
        "on_hand": 67,
        "upc": "0-12345-67891-0",
        "features": ["Clean-burning soy wax", "40-hour burn time per candle", "Reusable glass jars", "No synthetic fragrances"],
    },
}

CUSTOMER_INTERACTION_SCRIPTS = {
    "greeting": {
        "scenario": "Customer enters the store",
        "script": "Welcome to our store! Is there anything specific I can help you find today?",
        "follow_up": "If they mention a product category, guide them to the correct aisle.",
        "tips": ["Make eye contact", "Smile genuinely", "Keep a comfortable distance"],
    },
    "upsell": {
        "scenario": "Customer is ready to purchase a single item",
        "script": "Great choice! Did you know that pairs perfectly with our {complementary_product}? Many customers love the combination.",
        "follow_up": "If interested, walk them to the complementary item. If not, respect their decision.",
        "tips": ["Suggest only relevant items", "Limit to one upsell attempt", "Focus on value not price"],
    },
    "complaint_handling": {
        "scenario": "Customer has a complaint or issue",
        "script": "I am sorry to hear about that. Let me make sure I understand the issue so I can help resolve it right away.",
        "follow_up": "Listen fully, repeat back the issue, offer a concrete solution within your authority.",
        "tips": ["Never argue", "Acknowledge their frustration", "Offer alternatives if first solution is declined"],
    },
    "size_help": {
        "scenario": "Customer needs sizing assistance",
        "script": "I would be happy to help you find the right fit. What size do you typically wear in this type of item?",
        "follow_up": "Check fitting room availability. Bring two sizes if customer is between sizes.",
        "tips": ["Be sensitive about sizing", "Suggest trying multiple sizes", "Check stock for requested size first"],
    },
    "return_at_counter": {
        "scenario": "Customer wants to make a return at the register",
        "script": "Of course, I can help with that. Do you have your receipt or order confirmation?",
        "follow_up": "Verify return eligibility per policy. Process efficiently and offer exchange if applicable.",
        "tips": ["Stay positive and empathetic", "Explain policy clearly", "Thank them regardless of outcome"],
    },
}

DAILY_TASK_LIST = {
    "opening": [
        {"task": "Unlock entrance doors and disable alarm", "priority": "critical", "est_minutes": 2},
        {"task": "Power on POS terminals and verify connectivity", "priority": "critical", "est_minutes": 5},
        {"task": "Walk floor to check overnight display condition", "priority": "high", "est_minutes": 10},
        {"task": "Restock fitting rooms with hangers", "priority": "medium", "est_minutes": 5},
        {"task": "Review daily promotions and update signage", "priority": "high", "est_minutes": 15},
        {"task": "Check inventory alerts and pull items for floor replenishment", "priority": "high", "est_minutes": 20},
    ],
    "midday": [
        {"task": "Restock high-traffic areas and end caps", "priority": "high", "est_minutes": 20},
        {"task": "Process online pickup orders (BOPIS)", "priority": "critical", "est_minutes": 15},
        {"task": "Clean fitting rooms and return abandoned items", "priority": "medium", "est_minutes": 10},
        {"task": "Rotate break schedule for floor coverage", "priority": "high", "est_minutes": 5},
        {"task": "Check and respond to customer service queue", "priority": "high", "est_minutes": 10},
    ],
    "closing": [
        {"task": "Process remaining BOPIS orders for next-day pickup", "priority": "critical", "est_minutes": 15},
        {"task": "Reconcile POS drawers and prepare deposit", "priority": "critical", "est_minutes": 20},
        {"task": "Tidy all displays and return misplaced merchandise", "priority": "high", "est_minutes": 25},
        {"task": "Vacuum high-traffic aisles", "priority": "medium", "est_minutes": 15},
        {"task": "Set alarm and lock all entrances", "priority": "critical", "est_minutes": 3},
    ],
}

ASSOCIATE_PERFORMANCE = {
    "ASC-101": {
        "name": "Taylor Brooks",
        "role": "Senior Associate",
        "shift": "opening",
        "units_sold_today": 23,
        "revenue_today": 1847.50,
        "transactions_today": 14,
        "avg_basket": 131.96,
        "upsell_rate": 0.35,
        "csat_score": 4.8,
        "tasks_completed": 11,
        "tasks_total": 12,
        "hours_this_week": 32.5,
    },
    "ASC-102": {
        "name": "Jordan Kim",
        "role": "Associate",
        "shift": "midday",
        "units_sold_today": 17,
        "revenue_today": 1295.80,
        "transactions_today": 11,
        "avg_basket": 117.80,
        "upsell_rate": 0.22,
        "csat_score": 4.5,
        "tasks_completed": 8,
        "tasks_total": 10,
        "hours_this_week": 28.0,
    },
    "ASC-103": {
        "name": "Morgan Lee",
        "role": "Associate",
        "shift": "closing",
        "units_sold_today": 12,
        "revenue_today": 985.40,
        "transactions_today": 9,
        "avg_basket": 109.49,
        "upsell_rate": 0.18,
        "csat_score": 4.3,
        "tasks_completed": 7,
        "tasks_total": 9,
        "hours_this_week": 24.0,
    },
    "ASC-104": {
        "name": "Casey Rivera",
        "role": "Lead Associate",
        "shift": "opening",
        "units_sold_today": 29,
        "revenue_today": 2410.30,
        "transactions_today": 18,
        "avg_basket": 133.91,
        "upsell_rate": 0.40,
        "csat_score": 4.9,
        "tasks_completed": 12,
        "tasks_total": 12,
        "hours_this_week": 36.0,
    },
}

COMPLEMENTARY_PRODUCTS = {
    "SKU-1001": ["SKU-1003", "SKU-1008"],
    "SKU-1002": ["SKU-1004", "SKU-1006"],
    "SKU-1003": ["SKU-1001", "SKU-1008"],
    "SKU-1004": ["SKU-1005", "SKU-1009"],
    "SKU-1005": ["SKU-1006", "SKU-1009"],
    "SKU-1006": ["SKU-1009", "SKU-1005"],
    "SKU-1007": ["SKU-1008", "SKU-1001"],
    "SKU-1008": ["SKU-1007", "SKU-1001"],
    "SKU-1009": ["SKU-1006", "SKU-1004"],
    "SKU-1010": ["SKU-1009", "SKU-1006"],
}


# ---------------------------------------------------------------------------
# Demonstrated Retail Store Associate Copilot capabilities
# ---------------------------------------------------------------------------

EVIDENCE_CAPABILITIES = {
    "product_intelligence": {
        "title": "Real-Time Product Intelligence",
        "response": (
            "Here is the current product availability, feature, promotion, "
            "and sales guidance from the simulated commerce view."
        ),
        "source_system": "Dynamics 365 Commerce",
        "write": False,
        "key_field": "product_id",
        "knowledge": [
            "Store associates can surface product specifications, availability, and current promotions without searching multiple systems.",
            "Unified commerce context supports faster, more confident customer conversations during peak traffic.",
            "Sales guidance highlights a useful customer-facing talking point alongside the product facts.",
        ],
        "records": [
            {
                "product_id": "TECHPRO-X",
                "product": "TechPro X-Series wireless headphones",
                "availability": "14 units in the Bellevue store",
                "features": "38-hour battery, active ANC at -42 dB, three-device pairing, foldable design with premium case",
                "price_and_warranty": "$199.99 sale price; 2-year standard warranty",
                "promotion": "Save $50 from $249.99; promotion ends Sunday",
                "reviews": "4.7/5.0 from 847 reviews",
                "sales_guidance": "Lead with comfort, battery life, and the included premium case",
            },
            {
                "product_id": "PRD-7314",
                "product": "Premium Noise-Canceling Headphones",
                "availability": "12 in store",
                "features": "Adaptive ANC, 30-hour battery, spatial audio",
                "promotion": "$40 off when bundled with a laptop",
                "sales_guidance": "Demonstrate ambient mode for frequent travelers",
            },
            {
                "product_id": "PRD-9056",
                "product": "Ultra-Light 14-inch Laptop",
                "availability": "Out of stock; pickup tomorrow at North store",
                "features": "16 GB RAM, 1 TB SSD, 18-hour battery",
                "promotion": "12 months interest-free financing",
                "sales_guidance": "Offer PRD-9138 when same-day availability is the priority",
            },
        ],
    },
    "add_on_commission": {
        "title": "Add-On, Warranty, and Commission Guidance",
        "response": (
            "Here are high-value add-ons, warranty guidance, conversion tips, "
            "and deterministic commission calculations for the selected bundle."
        ),
        "source_system": "Dynamics 365 Commerce",
        "write": False,
        "key_field": "bundle_id",
        "knowledge": [
            "Relevant accessories and warranties can be suggested in real time instead of relying on associate guesswork.",
            "Conversion tips keep recommendations tied to customer value and increase accessory attach rates.",
            "Item-level commission visibility helps associates explain and prioritize complete solutions.",
        ],
        "records": [
            {
                "bundle_id": "BND-TECHPRO",
                "anchor_product": "TechPro X-Series wireless headphones",
                "add_ons": "Premium cleaning kit, travel adapter, replacement cushions",
                "warranty": "Extended warranty with 3-year coverage",
                "conversion_tip": "Mention that the cleaning kit extends cushion life; observed conversion is 65%",
                "bundle_value": "$319.95",
                "commission_breakdown": "Headphones $16.00; warranty $7.20; accessories $9.60",
                "commission": "$32.80",
            },
            {
                "bundle_id": "BND-2402",
                "anchor_product": "Premium Noise-Canceling Headphones",
                "add_on": "Travel case and airline adapter",
                "warranty": "2-year accidental damage plan",
                "conversion_tip": "Position the case as protection for frequent travel",
                "bundle_value": "$429.97",
                "commission": "$12.90 at 3%",
            },
            {
                "bundle_id": "BND-2403",
                "anchor_product": "Ultra-Light 14-inch Laptop",
                "add_on": "USB-C dock and wireless mouse",
                "warranty": "3-year premium support",
                "conversion_tip": "Show the one-cable desk setup",
                "bundle_value": "$1,829.96",
                "commission": "$54.90 at 3%",
            },
        ],
    },
    "product_comparison": {
        "title": "Alternative Product Comparison",
        "response": (
            "Here is a side-by-side alternative comparison with the key "
            "differences and a recommendation based on the stated customer priority."
        ),
        "source_system": "Dynamics 365 Commerce",
        "write": False,
        "key_field": "comparison_id",
        "knowledge": [
            "The agent compares relevant alternatives and highlights meaningful differences for the associate.",
            "Recommendations are tied to an explicit customer priority rather than a generic ranking.",
            "Out-of-stock alternatives can preserve trust and keep the customer interaction moving.",
        ],
        "records": [
            {
                "comparison_id": "CMP-TECHPRO-SOUNDMAX",
                "products": "TechPro X-Series vs SoundMax Pro",
                "key_differences": "$199.99 vs $229.99; 38 vs 30 hours; premium vs audiophile sound; -42 vs -48 dB ANC; 14 vs 3 units",
                "customer_priority": "Travel and commute vs pure audio quality",
                "recommendation": "TechPro for travel, all-day use, or budget; SoundMax when pure audio quality matters most",
            },
            {
                "comparison_id": "CMP-3102",
                "products": "OLED 65 vs Mini-LED 65",
                "key_differences": "Perfect black levels vs higher peak brightness",
                "customer_priority": "Bright-room sports viewing",
                "recommendation": "Mini-LED 65 for higher sustained brightness",
            },
            {
                "comparison_id": "CMP-3103",
                "products": "Headphones Pro vs Headphones Lite",
                "key_differences": "Adaptive ANC and 30 hours vs standard ANC and 24 hours",
                "customer_priority": "Lowest price",
                "recommendation": "Headphones Lite, saving $120 while retaining ANC",
            },
        ],
    },
    "transaction_preparation": {
        "title": "Transaction Preparation",
        "response": (
            "The selected transaction has been prepared with the applicable "
            "loyalty discount, warranty, financing option, and next steps."
        ),
        "source_system": "Dynamics 365 Commerce",
        "write": True,
        "key_field": "transaction_id",
        "knowledge": [
            "Transaction preparation can apply loyalty discounts and include selected warranties without manual price calculations.",
            "Eligible financing options are surfaced before checkout to reduce friction and pricing errors.",
            "The associate receives explicit next steps while the demo remains offline and non-mutating.",
        ],
        "records": [
            {
                "transaction_id": "TXN-TECHPRO",
                "items": "TechPro headphones $199.99; 3-year warranty $39.99; premium cleaning kit $24.99",
                "subtotal": "$264.97",
                "loyalty_discount": "-$13.25 (Gold member, 5% off)",
                "sales_tax": "$21.40 at 8.5%",
                "financing": "0% APR for 6 months at $45.52 per month",
                "prepared_total": "$273.12",
                "commission": "$32.80",
                "customer_savings": "$63.25 from sale and loyalty discount",
                "next_step": "Confirm loyalty discount and customer consent, then proceed to checkout",
            },
            {
                "transaction_id": "TXN-81025",
                "items": "Headphones, travel kit, 2-year protection",
                "subtotal": "$429.97",
                "loyalty_discount": "-$25.00",
                "financing": "Pay in full",
                "prepared_total": "$404.97 before tax",
                "next_step": "Confirm protection plan and complete payment at POS",
            },
            {
                "transaction_id": "TXN-81026",
                "items": "Laptop, USB-C dock, mouse, 3-year support",
                "subtotal": "$1,829.96",
                "loyalty_discount": "-$100.00",
                "financing": "$144.16/month for 12 months, 0% APR",
                "prepared_total": "$1,729.96 before tax",
                "next_step": "Verify financing eligibility and complete payment at POS",
            },
        ],
    },
}

_EVIDENCE_KEY_PUNCTUATION = "-_.,:;()?!/#@+$%^&*=[]{}<>~`'\""


def _normalize_evidence_tokens(text):
    """Normalize text into tokens used only for exact capability-key matching."""
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
    """Resolve an explicit key or an exact key token embedded in user input."""
    key_field = capability["key_field"]
    records = capability["records"]
    if key:
        wanted = _normalize_evidence_tokens(key)
        for record in records:
            if wanted and _normalize_evidence_tokens(record[key_field]) == wanted:
                return "match", record
        return "not_found", None

    explicit_input = str(user_input or "").strip()
    if not explicit_input:
        return "summary", None

    query_tokens = _normalize_evidence_tokens(explicit_input)
    for record in records:
        key_tokens = _normalize_evidence_tokens(record[key_field])
        width = len(key_tokens)
        if width and any(
            query_tokens[index:index + width] == key_tokens
            for index in range(len(query_tokens) - width + 1)
        ):
            return "match", record
    return "not_found", None


def _format_evidence_record(record):
    return ", ".join(
        f"{field.replace('_', ' ').title()}: {value}"
        for field, value in record.items()
    )


# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

def _search_products(query):
    """Search products by name, category, or SKU."""
    query_lower = query.lower()
    results = []
    for sku_id, prod in PRODUCT_CATALOG.items():
        if (query_lower in prod["name"].lower()
                or query_lower in prod["category"].lower()
                or query_lower in sku_id.lower()):
            results.append((sku_id, prod))
    return results


def _store_total_revenue():
    return sum(a["revenue_today"] for a in ASSOCIATE_PERFORMANCE.values())


def _store_total_transactions():
    return sum(a["transactions_today"] for a in ASSOCIATE_PERFORMANCE.values())


def _task_completion_rate(shift):
    tasks = DAILY_TASK_LIST.get(shift, [])
    total = len(tasks)
    # Simulate that critical and high tasks are done
    done = sum(1 for t in tasks if t["priority"] in ("critical", "high"))
    return round(done / total * 100, 1) if total > 0 else 0


# ---------------------------------------------------------------------------
# Agent Class
# ---------------------------------------------------------------------------

class StoreAssociateCopilotAgent(BasicAgent):
    """Copilot agent assisting store associates with daily operations."""

    def __init__(self):
        self.name = "store-associate-copilot-agent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "product_lookup",
                            "customer_assist",
                            "task_checklist",
                            "performance_dashboard",
                            "product_intelligence",
                            "add_on_commission",
                            "product_comparison",
                            "transaction_preparation",
                        ],
                    },
                    "query": {"type": "string"},
                    "sku_id": {"type": "string"},
                    "scenario": {"type": "string"},
                    "shift": {"type": "string"},
                    "key": {
                        "type": "string",
                        "description": "Exact record key for a v1.1.0 evidence operation.",
                    },
                    "user_input": {
                        "type": "string",
                        "description": "Optional request containing an exact v1.1.0 record key.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _search_live_products(self, query):
        """Search the live tenant catalog; [] when offline or no match."""
        q = query.lower()
        results = []
        for row in _fetch_collection("products"):
            prod = _normalize_live_product(row)
            if not prod["sku_id"]:
                continue
            if (q in prod["name"].lower()
                    or q in prod["sku_id"].lower()
                    or q in prod["category"].lower()):
                results.append((prod["sku_id"], prod))
        return results

    def _product_lookup(self, **kwargs):
        query = kwargs.get("query", "")
        sku_id = kwargs.get("sku_id", "")
        if sku_id and sku_id in PRODUCT_CATALOG:
            results = [(sku_id, PRODUCT_CATALOG[sku_id])]
        elif query:
            # Embedded demo catalog first, then the live tenant catalog.
            results = _search_products(query) or self._search_live_products(query)
        else:
            results = list(PRODUCT_CATALOG.items())
        lines = ["# Product Lookup", ""]
        if not results:
            lines.append(f"No products found for query: \"{query}\"")
            return "\n".join(lines)
        for sid, prod in results:
            live = prod.get("_live", False)
            lines.append(f"## {prod['name']} (`{sid}`)")
            lines.append("")
            if live:
                lines.append(
                    f"_Live record from {DATA_SOURCE_URL} "
                    "(Aster Lane Office Systems)_"
                )
            lines.append(f"- **Brand:** {prod['brand']}")
            lines.append(f"- **Category:** {prod['category']}")
            lines.append(f"- **Price:** {_na(prod['retail_price'], '${:.2f}')}")
            lines.append(f"- **Sizes:** {_na(prod['sizes'])}")
            lines.append(f"- **Colors:** {_na(prod['colors'])}")
            lines.append(f"- **Materials:** {_na(prod['materials'])}")
            lines.append(f"- **Care:** {_na(prod['care'])}")
            if prod["location_aisle"] is None:
                lines.append("- **Location:** n/a — enrichment seam")
            else:
                lines.append(f"- **Location:** Aisle {prod['location_aisle']}, {prod['location_shelf']}")
            lines.append(f"- **In Stock:** {_na(prod['on_hand'], '{} units')}")
            lines.append(f"- **UPC:** {_na(prod['upc'])}")
            lines.append("")
            if prod["features"]:
                lines.append("**Key Features:**")
                for feat in prod["features"]:
                    lines.append(f"  - {feat}")
                lines.append("")
            comp_skus = COMPLEMENTARY_PRODUCTS.get(sid, [])
            if comp_skus:
                comp_names = [PRODUCT_CATALOG[c]["name"] for c in comp_skus if c in PRODUCT_CATALOG]
                lines.append(f"**Pairs Well With:** {', '.join(comp_names)}")
            lines.append("")
        return "\n".join(lines)

    def _customer_assist(self, **kwargs):
        scenario = kwargs.get("scenario", "")
        if scenario and scenario in CUSTOMER_INTERACTION_SCRIPTS:
            scripts = {scenario: CUSTOMER_INTERACTION_SCRIPTS[scenario]}
        else:
            scripts = CUSTOMER_INTERACTION_SCRIPTS
        lines = ["# Customer Assistance Guide", ""]
        for scen_id, scr in scripts.items():
            lines.append(f"## {scen_id.replace('_', ' ').title()}")
            lines.append("")
            lines.append(f"**Scenario:** {scr['scenario']}")
            lines.append("")
            lines.append("**Suggested Script:**")
            lines.append(f"> {scr['script']}")
            lines.append("")
            lines.append(f"**Follow-Up:** {scr['follow_up']}")
            lines.append("")
            lines.append("**Tips:**")
            for tip in scr["tips"]:
                lines.append(f"- {tip}")
            lines.append("")
        return "\n".join(lines)

    def _task_checklist(self, **kwargs):
        shift = kwargs.get("shift", "")
        if shift and shift in DAILY_TASK_LIST:
            shifts = {shift: DAILY_TASK_LIST[shift]}
        else:
            shifts = DAILY_TASK_LIST
        lines = ["# Daily Task Checklist", ""]
        for shift_name, tasks in shifts.items():
            total_minutes = sum(t["est_minutes"] for t in tasks)
            comp_rate = _task_completion_rate(shift_name)
            lines.append(f"## {shift_name.title()} Shift")
            lines.append(f"**Estimated Time:** {total_minutes} min | **Completion:** {comp_rate}%")
            lines.append("")
            lines.append("| # | Task | Priority | Est. Time |")
            lines.append("|---|------|----------|-----------|")
            for i, task in enumerate(tasks, 1):
                lines.append(f"| {i} | {task['task']} | {task['priority'].upper()} | {task['est_minutes']} min |")
            lines.append("")
        # Live telemetry overlay — purely additive: everything above is
        # unchanged, and offline this section simply does not appear.
        live = _store_refrigeration_alert()
        if live:
            alert, case = live["alert"], live["case"]
            unit = alert.get("unit", "")
            lines.append("## Live Store Alerts (telemetry overlay)")
            lines.append("")
            lines.append(
                f"- **{alert.get('alert_code', '?')} "
                f"{alert.get('alert_type', '?')} "
                f"({str(alert.get('severity', '?')).upper()}):** "
                f"{alert.get('asset_name', '?')} at "
                f"{alert.get('account_name', '?')} — "
                f"{alert.get('title', '')}"
            )
            lines.append(
                f"- **Reading:** peak {alert.get('peak_value')} {unit} vs "
                f"threshold {alert.get('threshold')} {unit}"
                + (
                    f"; latest {live['latest']} {unit}, series max "
                    f"{live['max']} {unit} ({live['n']} samples @ 15 min)"
                    if live["latest"] is not None else ""
                )
            )
            if case:
                case_status = "Open" if case.get("statecode") == 0 else "Resolved"
                lines.append(
                    f"- **CRM case:** {case.get('ticketnumber', '?')} — "
                    f"{case.get('title', '?')} ({case_status}) — the case "
                    "created via the CRM Write API, joined by ticket number"
                )
            else:
                lines.append(
                    f"- **CRM case:** {alert.get('crm_case', 'n/a')} "
                    "(case detail unavailable — CRM offline)"
                )
            lines.append(
                "- **Suggested task:** Check the aisle-four refrigeration "
                "case, move perishables per SOP, and confirm the case is "
                "acknowledged."
            )
            lines.append("")
            lines.append(
                "_Source: live static-telemetry alert + reading series "
                "joined to the Static Dynamics 365 case by its real ticket "
                "number._"
            )
        return "\n".join(lines)

    def _performance_dashboard(self, **kwargs):
        total_rev = _store_total_revenue()
        total_txn = _store_total_transactions()
        lines = [
            "# Associate Performance Dashboard",
            "",
            f"**Store Total Revenue Today:** ${total_rev:,.2f}",
            f"**Store Total Transactions:** {total_txn}",
            f"**Store Avg Basket:** ${total_rev / total_txn:.2f}" if total_txn > 0 else "",
            "",
            "| Associate | Role | Shift | Revenue | Units | Txns | Basket | Upsell | CSAT | Tasks |",
            "|-----------|------|-------|---------|-------|------|--------|--------|------|-------|",
        ]
        for asc_id, asc in ASSOCIATE_PERFORMANCE.items():
            task_pct = round(asc["tasks_completed"] / asc["tasks_total"] * 100) if asc["tasks_total"] > 0 else 0
            lines.append(
                f"| {asc['name']} | {asc['role']} | {asc['shift']} "
                f"| ${asc['revenue_today']:,.2f} | {asc['units_sold_today']} "
                f"| {asc['transactions_today']} | ${asc['avg_basket']:.2f} "
                f"| {asc['upsell_rate']*100:.0f}% | {asc['csat_score']}/5.0 "
                f"| {asc['tasks_completed']}/{asc['tasks_total']} ({task_pct}%) |"
            )
        lines.append("")
        lines.append("## Top Performer Highlights")
        lines.append("")
        best_rev = max(ASSOCIATE_PERFORMANCE.values(), key=lambda a: a["revenue_today"])
        best_csat = max(ASSOCIATE_PERFORMANCE.values(), key=lambda a: a["csat_score"])
        best_upsell = max(ASSOCIATE_PERFORMANCE.values(), key=lambda a: a["upsell_rate"])
        lines.append(f"- **Highest Revenue:** {best_rev['name']} — ${best_rev['revenue_today']:,.2f}")
        lines.append(f"- **Best CSAT:** {best_csat['name']} — {best_csat['csat_score']}/5.0")
        lines.append(f"- **Top Upsell Rate:** {best_upsell['name']} — {best_upsell['upsell_rate']*100:.0f}%")
        return "\n".join(lines)

    def _evidence_capability(self, capability_name, **kwargs):
        capability = EVIDENCE_CAPABILITIES[capability_name]
        key = kwargs.get("key", "")
        user_input = str(kwargs.get("user_input") or "").strip()
        lookup_status, record = _record_for_evidence_request(
            capability, key, user_input
        )

        lines = [
            f"# {capability['title']}",
            "",
            capability["response"],
            "",
            "## Grounded Capability",
        ]
        lines.extend(f"- {fact}" for fact in capability["knowledge"])
        lines.extend([
            "",
            f"## Records — {capability['source_system']} (synthetic demo data)",
            "",
        ])

        receipt_key = "BATCH"
        if lookup_status == "match":
            receipt_key = record[capability["key_field"]]
            lines.append(
                f"Exact match on `{capability['key_field']}`:"
            )
            lines.append(f"- {_format_evidence_record(record)}")
        elif lookup_status == "not_found":
            lines.append(
                f"No record matched the requested {capability['key_field']}. "
                "Not substituting another record."
            )
        else:
            lines.append(
                "Worked examples (synthetic demo data; no customer data required):"
            )
            lines.extend(
                f"- {_format_evidence_record(item)}"
                for item in capability["records"]
            )

        if capability["write"] and lookup_status == "match":
            lines.extend([
                "",
                "## Simulated Write Receipt",
                "",
                "- Action Status: simulated",
                f"- Receipt: SIM-{capability_name.upper()}-{receipt_key}",
                f"- Target System: {capability['source_system']}",
                "- No external system changed (no live mutation).",
            ])
        elif capability["write"]:
            lines.extend([
                "",
                "_Write-capable operation; provide an exact key to prepare a "
                "simulated receipt. No external system is modified._",
            ])
        else:
            lines.extend([
                "",
                "_Read-only capability; no external system is modified._",
            ])
        return "\n".join(lines)

    def _product_intelligence(self, **kwargs):
        return self._evidence_capability("product_intelligence", **kwargs)

    def _add_on_commission(self, **kwargs):
        return self._evidence_capability("add_on_commission", **kwargs)

    def _product_comparison(self, **kwargs):
        return self._evidence_capability("product_comparison", **kwargs)

    def _transaction_preparation(self, **kwargs):
        return self._evidence_capability("transaction_preparation", **kwargs)

    def perform(self, **kwargs):
        operation = kwargs.get("operation", "product_lookup")
        dispatch = {
            "product_lookup": self._product_lookup,
            "customer_assist": self._customer_assist,
            "task_checklist": self._task_checklist,
            "performance_dashboard": self._performance_dashboard,
            "product_intelligence": self._product_intelligence,
            "add_on_commission": self._add_on_commission,
            "product_comparison": self._product_comparison,
            "transaction_preparation": self._transaction_preparation,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        return handler(**kwargs)


# ---------------------------------------------------------------------------
# Main — exercise all operations
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = StoreAssociateCopilotAgent()
    print("=" * 80)
    print("EMBEDDED DEMO PRODUCT (works offline)")
    print(agent.perform(operation="product_lookup", sku_id="SKU-1005"))
    print("\n" + "=" * 80)
    print("LIVE TENANT PRODUCT (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="product_lookup", query="Mobile Cart"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="customer_assist", scenario="upsell"))
    print("\n" + "=" * 80)
    print("TASK CHECKLIST + LIVE REFRIGERATION ALERT (telemetry joined to CRM")
    print("case CAS-260138; overlay disappears offline)")
    print(agent.perform(operation="task_checklist", shift="opening"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="performance_dashboard"))
    print("=" * 80)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
