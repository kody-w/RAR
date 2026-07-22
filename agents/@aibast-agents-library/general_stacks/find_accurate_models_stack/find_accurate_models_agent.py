"""
Find Accurate Models Agent — a template you are meant to mutate.

Searches and compares AI/ML models by accuracy benchmarks, deployment
readiness, and cost metrics to help teams select the best model for
their needs.

The live tenant has no native "model registry" entity, so in this
template a Dynamics PRODUCT record stands in for a model-registry entry
(a deployable, versioned catalog item with an owner and a cost) — that
keeps the registry seam demonstrable end-to-end until you point it at a
real MLflow/Azure ML/HuggingFace registry.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live catalog records over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="model_search", task_filter="scanner")
     — surfaces the tenant's real seeded "ScanDock S12" catalog entry.
  2. No network? Everything falls back to the embedded demo layer below
     (_MODEL_CATALOG) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FIND_ACCURATE_MODELS_DATA_URL to any OData-shaped endpoint, or
     replace _fetch_collection() with your model-registry client. The
     fields the rest of the file needs are listed in
     _normalize_live_model(). Accuracy, F1, and latency are labeled
     "n/a — enrichment seam" for live entries — wire your benchmark
     suite there.

OPERATIONS
  model_search | accuracy_benchmark | deployment_readiness
  | cost_comparison
  kwargs: operation (required), task_filter, model_id
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
    "name": "@aibast-agents-library/find_accurate_models",
    "version": "1.1.0",
    "display_name": "Find Accurate Models",
    "description": "Compares models by accuracy, readiness, and cost, merging live catalog entries from a simulated Dynamics 365 tenant with offline fallback.",
    "author": "AIBAST",
    "tags": ["ai", "ml", "model-selection", "benchmarks", "accuracy", "deployment"],
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
#   export FIND_ACCURATE_MODELS_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your model-registry client.
# Downstream code only needs the fields produced by
# _normalize_live_model().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "FIND_ACCURATE_MODELS_DATA_URL",
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


def _normalize_live_model(row):
    """Project a Dynamics product record onto the registry-entry shape
    this agent uses. THIS is the contract your replacement data source
    must meet — a dict with these keys. None means 'not available from
    the catalog alone' and the renderers label it as an enrichment seam
    (wire your benchmark suite / profiler)."""
    return {
        "id": row.get("productnumber", row.get("productid", "")),
        "name": row.get("name", "Unknown"),
        "task": row.get("description", "Uncategorized"),
        "framework": None,          # enrichment seam — wire your registry metadata
        "parameters": None,         # enrichment seam
        "size_mb": None,            # enrichment seam
        "accuracy": None,           # enrichment seam — wire your benchmark suite
        "f1_score": None,           # enrichment seam
        "latency_ms": None,         # enrichment seam — wire your profiler
        "training_data": None,      # enrichment seam
        "last_updated": str(row.get("modifiedon", ""))[:10],
        "license": None,            # enrichment seam
        "provider": row.get("owneridname", "Live tenant"),
        "unit_cost": float(row.get("currentcost") or 0),
        "list_price": float(row.get("price") or 0),
        "_live": True,
    }


def _live_model_catalog():
    """id-keyed dict of live tenant catalog entries; {} when offline."""
    rows = _fetch_collection("products")
    return {
        m["id"]: m
        for m in (_normalize_live_model(r) for r in rows)
        if m["id"]
    }


def _fmt(value, suffix=""):
    """None = unknowable from the catalog alone (enrichment seam)."""
    if value is None:
        return "n/a — enrichment seam"
    if isinstance(value, float) and suffix == "%":
        return f"{value:.1%}"
    return f"{value}{suffix}"


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_MODEL_CATALOG = {
    "MDL-001": {
        "id": "MDL-001", "name": "SentimentBERT-v3", "task": "Sentiment Analysis",
        "framework": "PyTorch", "parameters": "110M", "size_mb": 438,
        "accuracy": 0.943, "f1_score": 0.938, "latency_ms": 45,
        "training_data": "200K labeled reviews", "last_updated": "2025-09-15",
        "license": "Apache 2.0", "provider": "Internal ML Team",
    },
    "MDL-002": {
        "id": "MDL-002", "name": "DocClassifier-XL", "task": "Document Classification",
        "framework": "TensorFlow", "parameters": "340M", "size_mb": 1350,
        "accuracy": 0.967, "f1_score": 0.961, "latency_ms": 120,
        "training_data": "500K documents, 45 categories", "last_updated": "2025-10-01",
        "license": "MIT", "provider": "AI Research Lab",
    },
    "MDL-003": {
        "id": "MDL-003", "name": "ChurnPredictor-v2", "task": "Churn Prediction",
        "framework": "scikit-learn", "parameters": "2.5M", "size_mb": 12,
        "accuracy": 0.891, "f1_score": 0.874, "latency_ms": 8,
        "training_data": "150K customer records, 24-month history", "last_updated": "2025-08-20",
        "license": "Proprietary", "provider": "Data Science Team",
    },
    "MDL-004": {
        "id": "MDL-004", "name": "NER-Finance-v4", "task": "Named Entity Recognition",
        "framework": "spaCy", "parameters": "85M", "size_mb": 320,
        "accuracy": 0.952, "f1_score": 0.947, "latency_ms": 32,
        "training_data": "80K financial documents", "last_updated": "2025-10-15",
        "license": "Apache 2.0", "provider": "NLP Team",
    },
    "MDL-005": {
        "id": "MDL-005", "name": "ImageQuality-ResNet", "task": "Image Quality Assessment",
        "framework": "PyTorch", "parameters": "25M", "size_mb": 98,
        "accuracy": 0.928, "f1_score": 0.921, "latency_ms": 15,
        "training_data": "100K images with quality labels", "last_updated": "2025-07-10",
        "license": "MIT", "provider": "Computer Vision Team",
    },
    "MDL-006": {
        "id": "MDL-006", "name": "FraudDetector-Ensemble", "task": "Fraud Detection",
        "framework": "XGBoost + PyTorch", "parameters": "50M", "size_mb": 215,
        "accuracy": 0.978, "f1_score": 0.965, "latency_ms": 25,
        "training_data": "2M transactions, 18 months", "last_updated": "2025-11-01",
        "license": "Proprietary", "provider": "Security ML Team",
    },
}

_DEPLOYMENT_REQUIREMENTS = {
    "cpu_inference": {"min_ram_gb": 4, "min_cores": 2, "max_latency_ms": 200, "cost_per_1k_inferences": 0.02},
    "gpu_inference": {"min_ram_gb": 8, "gpu_vram_gb": 8, "max_latency_ms": 50, "cost_per_1k_inferences": 0.15},
    "edge_deployment": {"min_ram_gb": 2, "max_model_size_mb": 200, "max_latency_ms": 30, "cost_per_1k_inferences": 0.005},
    "serverless": {"max_cold_start_ms": 3000, "max_model_size_mb": 500, "cost_per_1k_inferences": 0.05},
}

_PRICING_TIERS = {
    "development": {"monthly_cost": 0, "inference_limit": 10000, "support": "Community", "sla": "None"},
    "standard": {"monthly_cost": 499, "inference_limit": 500000, "support": "Email (48h)", "sla": "99.5%"},
    "professional": {"monthly_cost": 1999, "inference_limit": 5000000, "support": "Priority (4h)", "sla": "99.9%"},
    "enterprise": {"monthly_cost": 7999, "inference_limit": -1, "support": "Dedicated (1h)", "sla": "99.99%"},
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _combined_catalog():
    """Embedded demo models plus live tenant catalog entries."""
    combined = dict(_MODEL_CATALOG)
    combined.update(_live_model_catalog())
    return combined


def _search_models(task_filter=None, min_accuracy=0.0):
    results = []
    for mid, model in _combined_catalog().items():
        if task_filter and task_filter.lower() not in model["task"].lower():
            continue
        acc = model.get("accuracy")
        if acc is None and min_accuracy > 0:
            continue
        if acc is None or acc >= min_accuracy:
            results.append(model)
    return sorted(results, key=lambda m: m["accuracy"] if m["accuracy"] is not None else -1, reverse=True)


def _check_deployment_readiness(model_id, target="cpu_inference"):
    model = _combined_catalog().get(model_id)
    if not model:
        return None
    reqs = _DEPLOYMENT_REQUIREMENTS.get(target, {})
    checks = []
    if "max_model_size_mb" in reqs:
        if model["size_mb"] is None:
            checks.append({"check": "Model Size", "status": "Unknown", "detail": "n/a — enrichment seam (wire your registry metadata)"})
        else:
            ok = model["size_mb"] <= reqs["max_model_size_mb"]
            checks.append({"check": "Model Size", "status": "Pass" if ok else "Fail", "detail": f"{model['size_mb']}MB vs {reqs['max_model_size_mb']}MB max"})
    if "max_latency_ms" in reqs:
        if model["latency_ms"] is None:
            checks.append({"check": "Latency", "status": "Unknown", "detail": "n/a — enrichment seam (wire your profiler)"})
        else:
            ok = model["latency_ms"] <= reqs["max_latency_ms"]
            checks.append({"check": "Latency", "status": "Pass" if ok else "Fail", "detail": f"{model['latency_ms']}ms vs {reqs['max_latency_ms']}ms max"})
    passed = sum(1 for c in checks if c["status"] == "Pass")
    return {"model": model["name"], "target": target, "checks": checks, "passed": passed, "total": len(checks), "ready": passed == len(checks)}


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class FindAccurateModelsAgent(BasicAgent):
    """
    AI/ML model search and comparison agent.

    Operations:
        model_search         - search models by task and accuracy threshold
        accuracy_benchmark   - detailed accuracy comparison across models
        deployment_readiness - check if a model meets deployment requirements
        cost_comparison      - compare hosting and inference costs
    """

    def __init__(self):
        self.name = "FindAccurateModelsAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "model_search", "accuracy_benchmark",
                            "deployment_readiness", "cost_comparison",
                        ],
                        "description": "The model search operation to perform",
                    },
                    "task_filter": {
                        "type": "string",
                        "description": "Filter models by task type",
                    },
                    "model_id": {
                        "type": "string",
                        "description": "Model ID for detailed inspection (e.g. 'MDL-001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "model_search")
        dispatch = {
            "model_search": self._model_search,
            "accuracy_benchmark": self._accuracy_benchmark,
            "deployment_readiness": self._deployment_readiness,
            "cost_comparison": self._cost_comparison,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(kwargs)

    # ── model_search ───────────────────────────────────────────
    def _model_search(self, params):
        task = params.get("task_filter", "")
        models = _search_models(task_filter=task if task else None)
        if not models:
            return f"No models match task filter '{task}'. Try an empty filter to list everything."
        rows = ""
        for m in models:
            origin = "live tenant" if m.get("_live") else "embedded"
            rows += f"| {m['id']} | {m['name']} | {m['task'][:35]} | {_fmt(m['accuracy'], '%')} | {_fmt(m['latency_ms'], 'ms')} | {origin} |\n"
        filter_note = f" (filtered by: '{task}')" if task else ""
        benchmarked = [m for m in models if m["accuracy"] is not None]
        live_count = sum(1 for m in models if m.get("_live"))
        top_line = (
            f"**Highest Accuracy:** {benchmarked[0]['name']} ({benchmarked[0]['accuracy']:.1%})\n"
            if benchmarked else
            "**Highest Accuracy:** n/a — no benchmarked entries in this result set (enrichment seam)\n"
        )
        timed = [m for m in models if m["latency_ms"] is not None]
        latency_line = (
            f"**Lowest Latency:** {min(timed, key=lambda m: m['latency_ms'])['name']} ({min(m['latency_ms'] for m in timed)}ms)\n"
            if timed else
            "**Lowest Latency:** n/a — enrichment seam\n"
        )
        return (
            f"**AI/ML Model Search Results{filter_note}**\n\n"
            f"| ID | Name | Task | Accuracy | Latency | Origin |\n|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Total Models:** {len(models)} ({live_count} from the live Dynamics tenant, where a product record stands in for a registry entry)\n"
            f"{top_line}"
            f"{latency_line}\n"
            f"Source: [Model Registry + Live Dynamics 365 Tenant]\nAgents: FindAccurateModelsAgent"
        )

    # ── accuracy_benchmark ─────────────────────────────────────
    def _accuracy_benchmark(self, params):
        models = sorted(_MODEL_CATALOG.values(), key=lambda m: m["accuracy"], reverse=True)
        rows = ""
        for m in models:
            rows += f"| {m['name']} | {m['task']} | {m['accuracy']:.1%} | {m['f1_score']:.1%} | {m['parameters']} | {m['training_data'][:30]} |\n"
        top = models[0]
        unbenchmarked = list(_live_model_catalog().values())
        live_note = (
            f"\n**Awaiting benchmarks (live tenant entries):** "
            + ", ".join(m["name"] for m in unbenchmarked[:6])
            + f"{'...' if len(unbenchmarked) > 6 else ''} — accuracy/F1 are enrichment seams; wire your benchmark suite.\n"
            if unbenchmarked else ""
        )
        return (
            f"**Accuracy Benchmark Comparison** (embedded demo benchmarks — simulated)\n\n"
            f"| Model | Task | Accuracy | F1 Score | Parameters | Training Data |\n|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Top Performer:** {top['name']} ({top['accuracy']:.1%} accuracy, {top['f1_score']:.1%} F1)\n\n"
            f"**Accuracy Distribution:**\n"
            f"- 95%+: {sum(1 for m in models if m['accuracy'] >= 0.95)} models\n"
            f"- 90-95%: {sum(1 for m in models if 0.90 <= m['accuracy'] < 0.95)} models\n"
            f"- Below 90%: {sum(1 for m in models if m['accuracy'] < 0.90)} models\n"
            f"{live_note}\n"
            f"Source: [Benchmark Suite + Model Registry]\nAgents: FindAccurateModelsAgent"
        )

    # ── deployment_readiness ───────────────────────────────────
    def _deployment_readiness(self, params):
        model_id = params.get("model_id", "MDL-001")
        catalog = _combined_catalog()
        model = catalog.get(model_id)
        if not model:
            return f"Model '{model_id}' not found. Available: {', '.join(sorted(catalog.keys()))}"
        target_rows = ""
        for target in _DEPLOYMENT_REQUIREMENTS:
            result = _check_deployment_readiness(model_id, target)
            unknown = sum(1 for c in result["checks"] if c["status"] == "Unknown")
            status = "Ready" if result["ready"] and not unknown else ("Needs benchmarks" if unknown else "Not Ready")
            target_rows += f"| {target} | {result['passed']}/{result['total']} checks | {status} |\n"
        detail_rows = ""
        for target in _DEPLOYMENT_REQUIREMENTS:
            result = _check_deployment_readiness(model_id, target)
            for check in result["checks"]:
                detail_rows += f"| {target} | {check['check']} | {check['status']} | {check['detail']} |\n"
        origin = "LIVE Dynamics 365 tenant entry" if model.get("_live") else "embedded demo entry (simulated)"
        return (
            f"**Deployment Readiness: {model['name']}** ({origin})\n\n"
            f"| Property | Value |\n|---|---|\n"
            f"| Model Size | {_fmt(model['size_mb'], ' MB')} |\n"
            f"| Latency | {_fmt(model['latency_ms'], ' ms')} |\n"
            f"| Framework | {_fmt(model['framework'])} |\n"
            f"| Parameters | {_fmt(model['parameters'])} |\n\n"
            f"**Target Compatibility:**\n\n"
            f"| Target | Checks Passed | Status |\n|---|---|---|\n"
            f"{target_rows}\n"
            f"**Detailed Checks:**\n\n"
            f"| Target | Check | Result | Detail |\n|---|---|---|---|\n"
            f"{detail_rows}\n\n"
            f"Source: [MLOps Platform + Infrastructure]\nAgents: FindAccurateModelsAgent"
        )

    # ── cost_comparison ────────────────────────────────────────
    def _cost_comparison(self, params):
        tier_rows = ""
        for tier, info in _PRICING_TIERS.items():
            limit = f"{info['inference_limit']:,}" if info['inference_limit'] > 0 else "Unlimited"
            tier_rows += f"| {tier.title()} | ${info['monthly_cost']:,}/mo | {limit} | {info['support']} | {info['sla']} |\n"
        infra_rows = ""
        for target, reqs in _DEPLOYMENT_REQUIREMENTS.items():
            infra_rows += f"| {target} | ${reqs['cost_per_1k_inferences']:.3f} | {reqs.get('min_ram_gb', 'N/A')} GB | {reqs.get('max_latency_ms', 'N/A')} ms |\n"
        monthly_100k = {t: reqs["cost_per_1k_inferences"] * 100 for t, reqs in _DEPLOYMENT_REQUIREMENTS.items()}
        cost_lines = "\n".join(f"- {t}: ${c:.2f}/month" for t, c in monthly_100k.items())
        live = list(_live_model_catalog().values())
        live_rows = "".join(
            f"| {m['id']} | {m['name']} | ${m['unit_cost']:,.2f} | ${m['list_price']:,.2f} |\n"
            for m in live[:12]
        )
        live_section = (
            f"**Live Tenant Catalog Costs (unit cost / list price, from the live Dynamics tenant):**\n\n"
            f"| ID | Entry | Unit Cost | List Price |\n|---|---|---|---|\n{live_rows}\n"
            if live_rows else
            "**Live Tenant Catalog Costs:** live tenant unreachable — embedded demo data only.\n\n"
        )
        return (
            f"**Cost Comparison** (pricing tiers are simulated demo data)\n\n"
            f"**Pricing Tiers:**\n\n"
            f"| Tier | Monthly Cost | Inference Limit | Support | SLA |\n|---|---|---|---|---|\n"
            f"{tier_rows}\n"
            f"**Infrastructure Cost per 1K Inferences:**\n\n"
            f"| Target | Cost/1K | Min RAM | Max Latency |\n|---|---|---|---|\n"
            f"{infra_rows}\n"
            f"**Estimated Monthly Cost (100K inferences):**\n{cost_lines}\n\n"
            f"{live_section}"
            f"Source: [Pricing Engine + Live Dynamics 365 Tenant]\nAgents: FindAccurateModelsAgent"
        )


if __name__ == "__main__":
    agent = FindAccurateModelsAgent()
    print("=" * 60)
    print("EMBEDDED DEMO ENTRY (works offline)")
    print(agent.perform(operation="deployment_readiness", model_id="MDL-001"))
    print()
    print("=" * 60)
    print("LIVE TENANT CATALOG (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="model_search", task_filter="scanner"))
    print()
    print("=" * 60)
    print(agent.perform(operation="cost_comparison"))
