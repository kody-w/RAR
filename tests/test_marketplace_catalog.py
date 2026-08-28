"""The constitutional rapp@x marketplace catalog stays installable."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def test_ratified_marketplaces_use_rapp_at_x_identity():
    catalog = json.loads((ROOT / "marketplaces.json").read_text())
    entries = catalog["marketplaces"]
    assert catalog["schema"] == "rapp-marketplaces/1.0"
    assert [entry["identity"] for entry in entries] == [
        "rapp@brainstem",
        "rapp@rar",
    ]
    for entry in entries:
        assert entry["plugin"] == "rapp"
        assert entry["identity"] == f"rapp@{entry['marketplace']}"
        assert entry["commands"]["copilot_install"] == (
            f"copilot plugin install {entry['identity']}"
        )
        assert entry["commands"]["claude_install"] == (
            f"claude plugin install {entry['identity']}"
        )
        assert {
            "Microsoft Scout",
            "GitHub Copilot CLI",
            "Claude Code",
        }.issubset(entry["clients"])


def test_static_api_publishes_the_marketplace_catalog():
    source = json.loads((ROOT / "marketplaces.json").read_text())
    published = json.loads(
        (ROOT / "api" / "v1" / "marketplaces.json").read_text()
    )
    manifest = json.loads((ROOT / "manifest.json").read_text())
    assert published["marketplaces"] == source["marketplaces"]
    assert published["count"] == 2
    assert manifest["endpoints"]["marketplaces"]["url"].endswith(
        "/api/v1/marketplaces.json"
    )
