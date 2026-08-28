"""Cowork Cookbook aggregation preserves attribution without mirroring recipes."""

from __future__ import annotations

import ast
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def manifest_of(path: Path) -> dict:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "__manifest__"
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise AssertionError(f"{path} has no literal __manifest__")


def cowork_source() -> dict:
    sources = json.loads((ROOT / "sources.json").read_text())["sources"]
    return next(source for source in sources if source["id"] == "cowork-cookbook")


def test_source_carries_repository_and_cc_by_attribution():
    source = cowork_source()
    assert source["format"] == "cowork-cookbook/1"
    assert source["repository_url"] == (
        "https://github.com/seangalliher/Coworkcookbook"
    )
    assert source["license"] == "CC-BY-4.0"
    assert source["license_verified"] is True
    assert source["license_url"].endswith("/Coworkcookbook/blob/main/LICENSE")


def test_adapter_keeps_hierarchy_and_drops_recipe_body():
    crawler = load_module("cowork_crawler", ROOT / "scripts" / "crawl_sources.py")
    source = cowork_source()
    recipe = {
        "id": "source-to-pay/example-recipe",
        "slug": "source-to-pay/example-recipe",
        "title": "Example Recipe",
        "summary": "A metadata-only fixture.",
        "version": "1.2.3",
        "process_tags": [
            "source-to-pay/manage-suppliers/onboard-supplier",
        ],
        "recipe_type": "prompt+skill",
        "category": "bulk-update",
        "difficulty": "advanced",
        "plugin": "dynamics-365-finance",
        "mutates_data": True,
        "deprecated": False,
        "status": "verified",
        "last_verified_on": "2026-08-01",
        "uses_skills": {
            "ootb": ["Word"],
            "custom": ["supplier-review"],
            "plugin": [{"plugin": "dynamics-365-finance", "action": "update"}],
        },
        "prompt": "This upstream recipe body must never enter RAR.",
        "instructions": ["Also must not enter RAR."],
    }
    [record] = crawler.parse_cowork_cookbook([recipe], source)

    assert record["ref"] == "@cowork-cookbook/source_to_pay_example_recipe"
    assert record["process_roots"] == ["source-to-pay"]
    assert record["process_tags"] == recipe["process_tags"]
    assert record["recipe_type"] == "prompt+skill"
    assert record["upstream_path"] == "source-to-pay/example-recipe"
    assert record["mutates_data"] is True
    assert record["source_signal"] == {"verified": True}
    assert "workflow" in record["tags"]
    assert "integration" in record["tags"]
    assert record["url"].endswith("/recipes/source-to-pay/example-recipe")
    assert "prompt" not in record
    assert "instructions" not in record


def test_snapshot_and_generated_agent_cover_every_recipe():
    items = json.loads((ROOT / "state" / "aggregated.json").read_text())["items"]
    recipes = [
        item
        for item in items
        if item.get("source_id") == "cowork-cookbook"
    ]
    assert len(recipes) == 1481
    assert len({item["ref"] for item in recipes}) == 1481
    assert all("prompt" not in item and "instructions" not in item for item in recipes)

    agents = sorted((ROOT / "agents" / "@cowork-cookbook").glob("*_agent.py"))
    assert len(agents) == 1481
    manifest = manifest_of(
        ROOT / "agents" / "@cowork-cookbook" / "account_360_briefing_agent.py"
    )
    assert manifest["source"]["source_id"] == "cowork-cookbook"
    assert manifest["source"]["license"] == "CC-BY-4.0"
    assert manifest["source"]["license_verified"] is True
    assert manifest["source"]["upstream_url"] == (
        "https://coworkcookbook.com/recipes/account-360-briefing"
    )
    assert manifest["quality_tier"] == "community"
    assert manifest["source"]["details"]["repository_url"] == (
        "https://github.com/seangalliher/Coworkcookbook"
    )
    assert manifest["source"]["details"]["license_url"].endswith(
        "/Coworkcookbook/blob/main/LICENSE"
    )
    context = manifest["industry_context"]
    assert context["process_roots"] == ["prospect-to-quote"]
    assert context["recipe_type"] == "prompt"
    assert context["plugin"] == "dynamics-365-sales"
    assert context["upstream_path"] == "prospect-to-quote/account-360-briefing"

    verified = manifest_of(
        ROOT
        / "agents"
        / "@cowork-cookbook"
        / "blueprint_credit_and_collections_review_agent.py"
    )
    assert verified["industry_context"]["verification_status"] == "verified"
    assert verified["quality_tier"] == "verified"
