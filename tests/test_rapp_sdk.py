"""
RAPP SDK Test Suite — validates all SDK operations:
manifest extraction, validation, contract tests, card generation,
Binder operations, CLI interface, and scaffold round-trip.
"""

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SDK_PATH = REPO_ROOT / "rapp_sdk.py"
BASIC_AGENT = REPO_ROOT / "agents" / "@rapp" / "basic_agent.py"
REGISTRY_JSON = REPO_ROOT / "registry.json"

# Insert repo root so we can import rapp_sdk
sys.path.insert(0, str(REPO_ROOT))
import rapp_sdk


# ═══════════════════════════════════════════════════════
# SECTION 1: Constants
# ═══════════════════════════════════════════════════════

def test_version_exists():
    assert hasattr(rapp_sdk, "__version__")
    assert rapp_sdk.__version__

def test_required_manifest_fields():
    assert "schema" in rapp_sdk.REQUIRED_MANIFEST_FIELDS
    assert "name" in rapp_sdk.REQUIRED_MANIFEST_FIELDS
    assert "version" in rapp_sdk.REQUIRED_MANIFEST_FIELDS
    assert "display_name" in rapp_sdk.REQUIRED_MANIFEST_FIELDS
    assert "description" in rapp_sdk.REQUIRED_MANIFEST_FIELDS
    assert "author" in rapp_sdk.REQUIRED_MANIFEST_FIELDS
    assert "tags" in rapp_sdk.REQUIRED_MANIFEST_FIELDS
    assert "category" in rapp_sdk.REQUIRED_MANIFEST_FIELDS

def test_tier_rarity_mapping_complete():
    for tier in rapp_sdk.VALID_TIERS:
        assert tier in rapp_sdk.TIER_TO_RARITY, f"Tier '{tier}' missing from TIER_TO_RARITY"

def test_rarity_labels_complete():
    for rarity in rapp_sdk.TIER_TO_RARITY.values():
        assert rarity in rapp_sdk.RARITY_LABELS, f"Rarity '{rarity}' missing from RARITY_LABELS"

def test_rarity_floor_complete():
    for rarity in rapp_sdk.TIER_TO_RARITY.values():
        assert rarity in rapp_sdk.RARITY_FLOOR, f"Rarity '{rarity}' missing from RARITY_FLOOR"

def test_agent_template_has_placeholders():
    for token in ["__NAME__", "__DISPLAY_NAME__", "__CLASS_NAME__", "__DESCRIPTION__", "__AUTHOR__"]:
        assert token in rapp_sdk.AGENT_TEMPLATE, f"Template missing {token}"


# ═══════════════════════════════════════════════════════
# SECTION 2: Manifest Operations
# ═══════════════════════════════════════════════════════

def test_extract_manifest_basic_agent():
    manifest = rapp_sdk.extract_manifest(str(BASIC_AGENT))
    assert manifest is not None
    assert manifest["name"] == "@rapp/basic_agent"
    assert manifest["schema"] == "rapp-agent/1.0"

def test_extract_manifest_nonexistent_file():
    result = rapp_sdk.extract_manifest("/nonexistent/path.py")
    assert result is None

def test_extract_manifest_no_manifest():
    with tempfile.NamedTemporaryFile(suffix=".py", mode="w", delete=False) as f:
        f.write("x = 42\n")
        f.flush()
        result = rapp_sdk.extract_manifest(f.name)
    os.unlink(f.name)
    assert result is None

def test_validate_manifest_valid():
    errors = rapp_sdk.validate_manifest(str(BASIC_AGENT))
    assert errors == [], f"Unexpected errors: {errors}"

def test_validate_manifest_missing_fields():
    with tempfile.NamedTemporaryFile(suffix=".py", mode="w", delete=False) as f:
        f.write('__manifest__ = {"schema": "rapp-agent/1.0"}\n')
        f.flush()
        errors = rapp_sdk.validate_manifest(f.name)
    os.unlink(f.name)
    assert len(errors) > 0
    assert any("Missing required field" in e for e in errors)

def test_validate_manifest_bad_name_format():
    with tempfile.NamedTemporaryFile(suffix=".py", mode="w", delete=False) as f:
        f.write('''__manifest__ = {
    "schema": "rapp-agent/1.0", "name": "bad-name", "version": "1.0.0",
    "display_name": "X", "description": "X", "author": "X",
    "tags": [], "category": "general"
}\n''')
        f.flush()
        errors = rapp_sdk.validate_manifest(f.name)
    os.unlink(f.name)
    assert any("@publisher/slug" in e for e in errors)

def test_validate_manifest_bad_version():
    with tempfile.NamedTemporaryFile(suffix=".py", mode="w", delete=False) as f:
        f.write('''__manifest__ = {
    "schema": "rapp-agent/1.0", "name": "@test/x", "version": "abc",
    "display_name": "X", "description": "X", "author": "X",
    "tags": [], "category": "general"
}\n''')
        f.flush()
        errors = rapp_sdk.validate_manifest(f.name)
    os.unlink(f.name)
    assert any("semver" in e.lower() or "version" in e.lower() for e in errors)


# ═══════════════════════════════════════════════════════
# SECTION 3: Deterministic Card Generation
# ═══════════════════════════════════════════════════════

def test_seed_hash_deterministic():
    h1 = rapp_sdk.seed_hash("@kody/deal-desk")
    h2 = rapp_sdk.seed_hash("@kody/deal-desk")
    assert h1 == h2

def test_seed_hash_different_inputs():
    h1 = rapp_sdk.seed_hash("@kody/deal-desk")
    h2 = rapp_sdk.seed_hash("@rapp/basic_agent")
    assert h1 != h2

def test_mulberry32_deterministic():
    rng1 = rapp_sdk.mulberry32(12345)
    rng2 = rapp_sdk.mulberry32(12345)
    assert [rng1() for _ in range(10)] == [rng2() for _ in range(10)]

def test_mulberry32_range():
    rng = rapp_sdk.mulberry32(42)
    for _ in range(100):
        val = rng()
        assert 0 <= val < 1, f"mulberry32 out of range: {val}"

def test_mint_card_basic_agent():
    card = rapp_sdk.mint_card(str(BASIC_AGENT))
    assert card["name"] == "@rapp/basic_agent"
    assert card["rarity"] == "mythic"
    assert card["rarity_label"] == "Legendary"
    assert card["floor_pts"] == 200
    assert isinstance(card["power"], int)
    assert isinstance(card["toughness"], int)
    assert isinstance(card["flavor"], str)
    assert len(card["flavor"]) > 0

def test_mint_card_deterministic():
    card1 = rapp_sdk.mint_card(str(BASIC_AGENT))
    card2 = rapp_sdk.mint_card(str(BASIC_AGENT))
    assert card1 == card2, "Same agent must produce identical card"

def test_resolve_card_basic_agent():
    card = rapp_sdk.resolve_card("@rapp/basic_agent")
    assert card["name"] == "@rapp/basic_agent"
    assert card["rarity"] == "mythic"
    assert "seed" in card
    assert isinstance(card["seed"], int) and card["seed"] > 0

def test_resolve_card_not_found():
    result = rapp_sdk.resolve_card("@nonexistent/agent")
    assert "error" in result

def test_resolve_matches_mint():
    """Resolve from name must produce same attributes as mint from file."""
    minted = rapp_sdk.mint_card(str(BASIC_AGENT))
    resolved = rapp_sdk.resolve_card("@rapp/basic_agent")
    assert minted["power"] == resolved["power"]
    assert minted["toughness"] == resolved["toughness"]
    assert minted["rarity"] == resolved["rarity"]
    assert minted["flavor"] == resolved["flavor"]
    assert minted["type_line"] == resolved["type_line"]


# ═══════════════════════════════════════════════════════
# SECTION 4: Card Value
# ═══════════════════════════════════════════════════════

def test_card_value_basic_agent():
    val = rapp_sdk.card_value("@rapp/basic_agent")
    assert "error" not in val
    assert val["tier"] == "official"
    assert val["rarity"] == "mythic"
    assert val["rarity_label"] == "Legendary"
    assert val["floor_pts"] == 200

def test_card_value_not_found():
    val = rapp_sdk.card_value("@nonexistent/nope")
    assert "error" in val


# ═══════════════════════════════════════════════════════
# SECTION 5: Binder Operations
# ═══════════════════════════════════════════════════════

def test_binder_status():
    status = rapp_sdk.binder_status()
    assert "error" not in status
    assert status["total_agents"] >= 131  # 131 founding + new agents
    assert "by_tier" in status
    assert status["total_pts"] > 0

def test_binder_transfer():
    result = rapp_sdk.binder_transfer("TEST-MINT-001", "0xdeadbeef1234567890")
    assert result["action"] == "transfer"
    assert result["mintId"] == "TEST-MINT-001"
    assert result["to"] == "0xdeadbeef1234567890"
    assert "timestamp" in result
    assert "hash" in result


# ═══════════════════════════════════════════════════════
# SECTION 6: Registry Client
# ═══════════════════════════════════════════════════════

def test_fetch_registry_local():
    reg = rapp_sdk.fetch_registry()
    assert "agents" in reg
    assert len(reg["agents"]) >= 131  # 131 founding + new agents

def test_search_agents():
    results = rapp_sdk.search_agents("memory")
    assert len(results) > 0
    assert any("memory" in r.get("name", "").lower() or "memory" in r.get("description", "").lower() for r in results)

def test_get_agent_info():
    info = rapp_sdk.get_agent_info("@rapp/basic_agent")
    assert info is not None
    assert info["name"] == "@rapp/basic_agent"

def test_get_agent_info_not_found():
    info = rapp_sdk.get_agent_info("@nonexistent/nope")
    assert info is None


# ═══════════════════════════════════════════════════════
# SECTION 7: Scaffold Round-Trip
# ═══════════════════════════════════════════════════════

def test_scaffold_creates_valid_agent():
    """Scaffold an agent, extract its manifest, validate it — full round-trip."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = rapp_sdk.scaffold_agent("@test/round_trip", output_dir=tmpdir)
        assert result is not None
        agent_path = Path(result)
        assert agent_path.exists()
        assert "-" not in agent_path.name, "Scaffolded filename must be snake_case"

        # Extract and validate manifest
        manifest = rapp_sdk.extract_manifest(str(agent_path))
        assert manifest is not None
        assert manifest["name"] == "@test/round_trip"
        assert manifest["display_name"] == "Round Trip"

        errors = rapp_sdk.validate_manifest(str(agent_path), manifest)
        assert errors == [], f"Scaffold produced invalid agent: {errors}"


def test_scaffold_rejects_kebab():
    """Scaffold must reject kebab-case slugs."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(ValueError, match="snake_case"):
            rapp_sdk.scaffold_agent("@test/bad-name", output_dir=tmpdir)


# ═══════════════════════════════════════════════════════
# SECTION 8: CLI
# ═══════════════════════════════════════════════════════

def test_cli_help():
    result = subprocess.run(
        [sys.executable, str(SDK_PATH), "--help"],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0
    assert "RAPP Foundation SDK" in result.stdout

def test_cli_version():
    result = subprocess.run(
        [sys.executable, str(SDK_PATH), "--version"],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0

def test_cli_validate():
    result = subprocess.run(
        [sys.executable, str(SDK_PATH), "validate", str(BASIC_AGENT)],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0
    assert "Valid" in result.stdout or "valid" in result.stdout.lower()

def test_cli_validate_json():
    result = subprocess.run(
        [sys.executable, str(SDK_PATH), "validate", str(BASIC_AGENT), "--json"],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data["valid"] is True

def test_cli_search():
    result = subprocess.run(
        [sys.executable, str(SDK_PATH), "search", "memory"],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0

def test_cli_card_resolve():
    result = subprocess.run(
        [sys.executable, str(SDK_PATH), "card", "resolve", "@rapp/basic_agent"],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0
    assert "Legendary" in result.stdout

def test_cli_card_resolve_json():
    result = subprocess.run(
        [sys.executable, str(SDK_PATH), "card", "resolve", "@rapp/basic_agent", "--json"],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data["name"] == "@rapp/basic_agent"
    assert isinstance(data["seed"], int) and data["seed"] > 0

def test_cli_card_value():
    result = subprocess.run(
        [sys.executable, str(SDK_PATH), "card", "value", "@rapp/basic_agent"],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0
    assert "Legendary" in result.stdout

def test_cli_binder_status():
    result = subprocess.run(
        [sys.executable, str(SDK_PATH), "binder", "status"],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0
    assert "agents" in result.stdout.lower()  # verify it shows agent count

def test_cli_card_mint():
    result = subprocess.run(
        [sys.executable, str(SDK_PATH), "card", "mint", str(BASIC_AGENT)],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0
    assert "BasicAgent" in result.stdout or "basic" in result.stdout.lower()
