---
name: "rar-aibast-agents-library-find-accurate-models"
description: "Compares models by accuracy, readiness, and cost, merging live catalog entries from a simulated Dynamics 365 tenant with offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/find_accurate_models", "rar_sha256": "d7f5c04d4c9662d15626ed4658095f16d645842700479c66143fb1e49e9a0e1e", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["ai", "ml", "model-selection", "benchmarks", "accuracy", "deployment"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/find_accurate_models`. The original RAPP
agent is preserved byte-for-byte in `find_accurate_models_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "model_id": {
      "description": "Model ID for detailed inspection (e.g. 'MDL-001')",
      "type": "string"
    },
    "operation": {
      "description": "The model search operation to perform",
      "enum": [
        "model_search",
        "accuracy_benchmark",
        "deployment_readiness",
        "cost_comparison"
      ],
      "type": "string"
    },
    "task_filter": {
      "description": "Filter models by task type",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `find_accurate_models_agent.py` and embedded as the fenced Python below (sha256 d7f5c04d4c9662d1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `find_accurate_models_agent.py` first:

```bash
python3 find_accurate_models_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 find_accurate_models_agent.py   # or on stdin
python3 find_accurate_models_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
