import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build_scout_exports", ROOT / "scripts" / "build_scout_exports.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_entry_without_singleton_url_is_skipped_not_fetched():
    assert mod._federated_unfetchable_reason({"id": "dock_scotty", "access": "public", "singleton_url": ""})
    assert mod._federated_unfetchable_reason({"id": "x", "access": "public"})


def test_entry_with_singleton_url_is_fetched():
    assert mod._federated_unfetchable_reason({"id": "x", "singleton_url": "https://example.com/a.py"}) is None
