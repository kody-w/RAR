---
name: "rar-aibast-agents-library-product-reference"
description: "Looks up products and pricing from a live simulated Dynamics 365 tenant catalog, with feature comparison and an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/product_reference", "rar_sha256": "1039e00d13b1925f90e6ae453729973bf6f7ca4b317a8c0dcac94f02330797d3", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["product", "catalog", "pricing", "features", "compatibility"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/product_reference`. The original RAPP
agent is preserved byte-for-byte in `product_reference_agent.py` and in the RCI capsule.

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

Product Reference Agent — a template you are meant to mutate.

Product catalog lookup with feature comparison, pricing information,
and compatibility checking across the product portfolio.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls the live product catalog over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="product_lookup", product_id="AST-SCN-012")
     — the tenant's real seeded "ScanDock S12" desktop document
     scanner with its live list price and unit cost.
  2. No network? Everything falls back to the embedded demo layer below
     (_PRODUCTS / _PRICING_TIERS) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PRODUCT_REFERENCE_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your PIM), or replace
     _fetch_collection() with your catalog client. The fields the rest
     of the file needs are listed in _normalize_live_product() —
     feature lists and compatibility rules for live entries are labeled
     "n/a — enrichment seam"; wire your PIM there.

OPERATIONS
  product_lookup | feature_comparison | pricing_info
  | compatibility_check
  kwargs: operation (required), product_id (embedded 'CORE'/'ENT' or a
  live tenant product number like 'AST-SCN-012' or name)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The product reference operation to perform",
      "enum": [
        "product_lookup",
        "feature_comparison",
        "pricing_info",
        "compatibility_check"
      ],
      "type": "string"
    },
    "product_id": {
      "description": "Product ID (e.g. 'CORE', 'ENT')",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `product_reference_agent.py` and embedded as the fenced Python below (sha256 1039e00d13b1925f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `product_reference_agent.py` first:

```bash
python3 product_reference_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 product_reference_agent.py   # or on stdin
python3 product_reference_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Product Reference Agent — a template you are meant to mutate.

Product catalog lookup with feature comparison, pricing information,
and compatibility checking across the product portfolio.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls the live product catalog over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="product_lookup", product_id="AST-SCN-012")
     — the tenant's real seeded "ScanDock S12" desktop document
     scanner with its live list price and unit cost.
  2. No network? Everything falls back to the embedded demo layer below
     (_PRODUCTS / _PRICING_TIERS) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PRODUCT_REFERENCE_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your PIM), or replace
     _fetch_collection() with your catalog client. The fields the rest
     of the file needs are listed in _normalize_live_product() —
     feature lists and compatibility rules for live entries are labeled
     "n/a — enrichment seam"; wire your PIM there.

OPERATIONS
  product_lookup | feature_comparison | pricing_info
  | compatibility_check
  kwargs: operation (required), product_id (embedded 'CORE'/'ENT' or a
  live tenant product number like 'AST-SCN-012' or name)
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
    "name": "@aibast-agents-library/product_reference",
    "version": "1.1.0",
    "display_name": "Product Reference",
    "description": "Looks up products and pricing from a live simulated Dynamics 365 tenant catalog, with feature comparison and an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["product", "catalog", "pricing", "features", "compatibility"],
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
#   export PRODUCT_REFERENCE_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your PIM/catalog client.
# Downstream code only needs the fields produced by
# _normalize_live_product().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "PRODUCT_REFERENCE_DATA_URL",
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


def _normalize_live_product(row):
    """Project a Dynamics product record onto the catalog shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not available from the
    catalog alone' and renderers label it as an enrichment seam."""
    return {
        "id": row.get("productnumber", row.get("productid", "")),
        "name": row.get("name", "Unknown"),
        "category": row.get("producttypecode@OData.Community.Display.V1.FormattedValue", "Catalog Item"),
        "description": row.get("description", ""),
        "features": [],            # enrichment seam — wire your PIM feature data
        "max_users": None,         # enrichment seam
        "storage_gb": None,        # enrichment seam
        "api_calls_monthly": None, # enrichment seam
        "support_level": None,     # enrichment seam
        "list_price": float(row.get("price") or 0),
        "unit_cost": float(row.get("currentcost") or 0),
        "uom": row.get("defaultuomidname", ""),
        "_live": True,
    }


def _live_catalog():
    """id-keyed dict of live tenant products; {} when offline."""
    rows = _fetch_collection("products")
    return {
        p["id"]: p
        for p in (_normalize_live_product(r) for r in rows)
        if p["id"]
    }


def _na(value, suffix=""):
    return "n/a — enrichment seam" if value is None else f"{value}{suffix}"


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_PRODUCTS = {
    "CORE": {"id": "CORE", "name": "Core Platform", "category": "Platform", "description": "Essential CRM and workflow automation for growing teams", "features": ["Contact Management", "Deal Pipeline", "Task Automation", "Basic Reporting", "Email Integration", "Mobile App"], "max_users": 100, "storage_gb": 50, "api_calls_monthly": 10000, "support_level": "Standard"},
    "ENT": {"id": "ENT", "name": "Enterprise Platform", "category": "Platform", "description": "Full-featured platform with advanced analytics and enterprise controls", "features": ["Everything in Core", "Advanced Analytics", "Custom Dashboards", "Role-Based Access", "Audit Logging", "SSO/SAML", "API Unlimited", "Custom Objects", "Workflow Builder"], "max_users": 10000, "storage_gb": 500, "api_calls_monthly": -1, "support_level": "Premium"},
    "ANLYT-STD": {"id": "ANLYT-STD", "name": "Analytics Standard", "category": "Analytics", "description": "Business intelligence and reporting for data-driven decisions", "features": ["Pre-built Reports", "Dashboard Builder", "Data Export (CSV/PDF)", "Scheduled Reports", "Basic Visualizations"], "max_users": 50, "storage_gb": 25, "api_calls_monthly": 5000, "support_level": "Standard"},
    "ANLYT-PRO": {"id": "ANLYT-PRO", "name": "Analytics Pro", "category": "Analytics", "description": "Advanced analytics with predictive insights and custom models", "features": ["Everything in Standard", "Predictive Analytics", "Custom Models", "Data Warehouse Connect", "Real-time Dashboards", "Embedded Analytics", "AI-Powered Insights"], "max_users": 500, "storage_gb": 200, "api_calls_monthly": 50000, "support_level": "Premium"},
    "INTGR": {"id": "INTGR", "name": "Integration Hub", "category": "Integration", "description": "Connect your tech stack with pre-built and custom integrations", "features": ["200+ Pre-built Connectors", "Custom API Builder", "Webhook Support", "Data Sync Engine", "Transformation Rules", "Error Handling & Retry"], "max_users": -1, "storage_gb": 100, "api_calls_monthly": 100000, "support_level": "Standard"},
    "SECUR": {"id": "SECUR", "name": "Security Suite", "category": "Security", "description": "Enterprise-grade security, compliance, and data protection", "features": ["Data Encryption (AES-256)", "IP Allowlisting", "MFA Enforcement", "DLP Policies", "Compliance Reports (SOC2, HIPAA)", "Threat Detection", "Backup & Recovery"], "max_users": -1, "storage_gb": 50, "api_calls_monthly": -1, "support_level": "Premium"},
}

_PRICING_TIERS = {
    "CORE": {"monthly_per_user": 29, "annual_per_user": 24, "annual_savings_pct": 17},
    "ENT": {"monthly_per_user": 79, "annual_per_user": 65, "annual_savings_pct": 18},
    "ANLYT-STD": {"monthly_per_user": 19, "annual_per_user": 15, "annual_savings_pct": 21},
    "ANLYT-PRO": {"monthly_per_user": 49, "annual_per_user": 40, "annual_savings_pct": 18},
    "INTGR": {"monthly_flat": 1500, "annual_flat": 15000, "annual_savings_pct": 17},
    "SECUR": {"monthly_flat": 1250, "annual_flat": 12500, "annual_savings_pct": 17},
}

_COMPATIBILITY_MATRIX = {
    "CORE": {"requires": [], "recommended": ["ANLYT-STD", "INTGR"], "incompatible": []},
    "ENT": {"requires": [], "recommended": ["ANLYT-PRO", "INTGR", "SECUR"], "incompatible": []},
    "ANLYT-STD": {"requires": ["CORE"], "recommended": ["INTGR"], "incompatible": ["ANLYT-PRO"]},
    "ANLYT-PRO": {"requires": ["ENT"], "recommended": ["INTGR", "SECUR"], "incompatible": ["ANLYT-STD"]},
    "INTGR": {"requires": ["CORE"], "recommended": ["SECUR"], "incompatible": []},
    "SECUR": {"requires": ["ENT"], "recommended": ["INTGR"], "incompatible": []},
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_product(query):
    """Embedded demo products first, then the live tenant catalog.
    Returns (product, is_live)."""
    if not query:
        return _PRODUCTS["CORE"], False
    q = query.upper().strip()
    if q in _PRODUCTS:
        return _PRODUCTS[q], False
    for pid, prod in _PRODUCTS.items():
        if q in prod["name"].upper():
            return prod, False
    live = _live_catalog()
    if q in live:
        return live[q], True
    for pid, prod in live.items():
        if q in prod["name"].upper():
            return prod, True
    return _PRODUCTS["CORE"], False


def _calculate_bundle_price(product_ids, num_users=100, billing="annual"):
    total = 0
    for pid in product_ids:
        pricing = _PRICING_TIERS.get(pid, {})
        if billing == "annual":
            if "annual_per_user" in pricing:
                total += pricing["annual_per_user"] * num_users * 12
            elif "annual_flat" in pricing:
                total += pricing["annual_flat"]
        else:
            if "monthly_per_user" in pricing:
                total += pricing["monthly_per_user"] * num_users * 12
            elif "monthly_flat" in pricing:
                total += pricing["monthly_flat"] * 12
    return total


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class ProductReferenceAgent(BasicAgent):
    """
    Product reference and catalog agent.

    Operations:
        product_lookup       - look up product details
        feature_comparison   - compare features across products
        pricing_info         - view pricing tiers and calculate costs
        compatibility_check  - check product compatibility and dependencies
    """

    def __init__(self):
        self.name = "ProductReferenceAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "product_lookup", "feature_comparison",
                            "pricing_info", "compatibility_check",
                        ],
                        "description": "The product reference operation to perform",
                    },
                    "product_id": {
                        "type": "string",
                        "description": "Product ID (e.g. 'CORE', 'ENT')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "product_lookup")
        dispatch = {
            "product_lookup": self._product_lookup,
            "feature_comparison": self._feature_comparison,
            "pricing_info": self._pricing_info,
            "compatibility_check": self._compatibility_check,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(kwargs)

    # ── product_lookup ─────────────────────────────────────────
    def _product_lookup(self, params):
        prod, is_live = _resolve_product(params.get("product_id", ""))
        if is_live:
            source = "Record source: LIVE product from the Aster Lane Dynamics 365 tenant"
            price_line = f"${prod['list_price']:,.2f} list / ${prod['unit_cost']:,.2f} unit cost ({prod['uom'] or 'per unit'})"
            features = "- n/a — enrichment seam (wire your PIM feature data)"
            support = _na(prod["support_level"])
            users = _na(prod["max_users"])
            storage = _na(prod["storage_gb"], " GB")
            api = _na(prod["api_calls_monthly"])
        else:
            source = "Record source: embedded demo layer (simulated)"
            pricing = _PRICING_TIERS.get(prod["id"], {})
            if "monthly_per_user" in pricing:
                price_line = f"${pricing['monthly_per_user']}/user/month (${pricing['annual_per_user']}/user/month annual)"
            else:
                price_line = f"${pricing.get('monthly_flat', 0):,}/month (${pricing.get('annual_flat', 0):,}/year)"
            features = "\n".join(f"- {f}" for f in prod["features"])
            support = prod["support_level"]
            users = f"{prod['max_users']:,}" if prod["max_users"] > 0 else "Unlimited"
            storage = f"{prod['storage_gb']} GB"
            api = f"{prod['api_calls_monthly']:,}" if prod["api_calls_monthly"] > 0 else "Unlimited"
        return (
            f"**Product: {prod['name']}** ({prod['id']})\n\n"
            f"**Category:** {prod['category']} | **Support:** {support}\n\n"
            f"**Description:** {prod['description']}\n\n"
            f"| Spec | Value |\n|---|---|\n"
            f"| Max Users | {users} |\n"
            f"| Storage | {storage} |\n"
            f"| API Calls | {api}/month |\n"
            f"| Pricing | {price_line} |\n\n"
            f"**Features:**\n{features}\n\n"
            f"{source}\n"
            f"Source: [Product Catalog]\nAgents: ProductReferenceAgent"
        )

    # ── feature_comparison ─────────────────────────────────────
    def _feature_comparison(self, params):
        categories = {}
        for pid, prod in _PRODUCTS.items():
            categories.setdefault(prod["category"], []).append(prod)
        comparison = ""
        for cat, products in categories.items():
            if len(products) < 2:
                continue
            comparison += f"**{cat}:**\n\n"
            all_features = set()
            for p in products:
                all_features.update(f for f in p["features"] if not f.startswith("Everything"))
            header = "| Feature | " + " | ".join(p["name"] for p in products) + " |\n"
            sep = "|---|" + "|".join(["---"] * len(products)) + "|\n"
            rows = ""
            for feat in sorted(all_features):
                cells = []
                for p in products:
                    cells.append("Yes" if feat in p["features"] else "No")
                rows += f"| {feat} | " + " | ".join(cells) + " |\n"
            comparison += header + sep + rows + "\n"
        live = _live_catalog()
        live_note = (
            f"**Live tenant catalog:** {len(live)} products available for lookup "
            "(feature matrices for live entries are an enrichment seam — wire your PIM).\n\n"
            if live else
            "**Live tenant catalog:** live tenant unreachable — embedded demo data only.\n\n"
        )
        return (
            f"**Feature Comparison** (embedded demo catalog — simulated)\n\n"
            f"{comparison}"
            f"{live_note}"
            f"Source: [Product Catalog]\nAgents: ProductReferenceAgent"
        )

    # ── pricing_info ───────────────────────────────────────────
    def _pricing_info(self, params):
        rows = ""
        for pid, pricing in _PRICING_TIERS.items():
            name = _PRODUCTS[pid]["name"]
            if "monthly_per_user" in pricing:
                monthly = f"${pricing['monthly_per_user']}/user"
                annual = f"${pricing['annual_per_user']}/user"
            else:
                monthly = f"${pricing.get('monthly_flat', 0):,} flat"
                annual = f"${pricing.get('annual_flat', 0):,} flat"
            rows += f"| {name} | {monthly} | {annual} | {pricing.get('annual_savings_pct', 0)}% |\n"
        example_100 = _calculate_bundle_price(["ENT", "ANLYT-PRO", "INTGR", "SECUR"], 100, "annual")
        example_500 = _calculate_bundle_price(["ENT", "ANLYT-PRO", "INTGR", "SECUR"], 500, "annual")
        live = _live_catalog()
        live_rows = "".join(
            f"| {p['id']} | {p['name']} | ${p['list_price']:,.2f} | ${p['unit_cost']:,.2f} |\n"
            for p in sorted(live.values(), key=lambda x: x["id"])
        )
        live_section = (
            f"**Live Tenant Price List (LIVE Dynamics 365 tenant):**\n\n"
            f"| ID | Product | List Price | Unit Cost |\n|---|---|---|---|\n{live_rows}\n"
            if live_rows else
            "**Live Tenant Price List:** live tenant unreachable — embedded demo data only.\n\n"
        )
        return (
            f"**Pricing Information** (tiers below are embedded demo data — simulated)\n\n"
            f"| Product | Monthly | Annual | Savings |\n|---|---|---|---|\n"
            f"{rows}\n"
            f"**Bundle Examples (Annual Billing):**\n"
            f"- Enterprise Full Suite (100 users): ${example_100:,}/year\n"
            f"- Enterprise Full Suite (500 users): ${example_500:,}/year\n\n"
            f"{live_section}"
            f"**Notes:**\n"
            f"- Volume discounts available for 50+ users\n"
            f"- Multi-year commitments receive additional 10-20% discount\n"
            f"- Non-profit and education pricing available\n\n"
            f"Source: [Pricing Engine + Live Dynamics 365 Tenant]\nAgents: ProductReferenceAgent"
        )

    # ── compatibility_check ────────────────────────────────────
    def _compatibility_check(self, params):
        prod, is_live = _resolve_product(params.get("product_id", ""))
        if is_live:
            header = (
                f"**Compatibility Check: {prod['name']}** ({prod['id']})\n\n"
                "This is a LIVE tenant product — compatibility rules are an "
                "enrichment seam (wire your PIM/dependency data). The embedded "
                "matrix below shows the shape your rules should take.\n\n"
            )
        else:
            compat = _COMPATIBILITY_MATRIX.get(prod["id"], {})
            requires = ", ".join(_PRODUCTS[r]["name"] for r in compat.get("requires", [])) or "None (standalone)"
            recommended = ", ".join(_PRODUCTS[r]["name"] for r in compat.get("recommended", [])) or "None"
            incompatible = ", ".join(_PRODUCTS[r]["name"] for r in compat.get("incompatible", [])) or "None"
            header = (
                f"**Compatibility Check: {prod['name']}**\n\n"
                f"| Relationship | Products |\n|---|---|\n"
                f"| Requires | {requires} |\n"
                f"| Recommended With | {recommended} |\n"
                f"| Incompatible With | {incompatible} |\n\n"
            )
        matrix_rows = ""
        for p_id, c in _COMPATIBILITY_MATRIX.items():
            reqs = ", ".join(c["requires"]) or "-"
            recs = ", ".join(c["recommended"]) or "-"
            incompat = ", ".join(c["incompatible"]) or "-"
            matrix_rows += f"| {_PRODUCTS[p_id]['name']} | {reqs} | {recs} | {incompat} |\n"
        return (
            f"{header}"
            f"**Full Compatibility Matrix (embedded demo data — simulated):**\n\n"
            f"| Product | Requires | Recommended | Incompatible |\n|---|---|---|---|\n"
            f"{matrix_rows}\n\n"
            f"Source: [Product Catalog + Compatibility Engine]\nAgents: ProductReferenceAgent"
        )


if __name__ == "__main__":
    agent = ProductReferenceAgent()
    print("=" * 60)
    print("EMBEDDED DEMO PRODUCT (works offline)")
    print(agent.perform(operation="product_lookup", product_id="ENT"))
    print()
    print("=" * 60)
    print("LIVE TENANT PRODUCT (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="product_lookup", product_id="AST-SCN-012"))
    print()
    print("=" * 60)
    print(agent.perform(operation="pricing_info"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
