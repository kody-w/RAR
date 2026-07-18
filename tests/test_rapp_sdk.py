"""
RAPP SDK Test Suite — validates all SDK operations:
manifest extraction, validation, contract tests, card generation,
collection status/transfer, CLI interface, and scaffold round-trip.
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


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return json.dumps(self.payload).encode()


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


def _write_submission_agent(tmp_path: Path, version: str = "1.0.0") -> Path:
    path = tmp_path / "my_agent.py"
    path.write_text(
        rapp_sdk.AGENT_TEMPLATE
        .replace("__NAME__", "@testuser/my_agent")
        .replace("__DISPLAY_NAME__", "My Agent")
        .replace("__CLASS_NAME__", "MyAgent")
        .replace("__DESCRIPTION__", "A test agent.")
        .replace("__AUTHOR__", "testuser")
        .replace('"version": "1.0.0"', f'"version": "{version}"')
    )
    return path


def test_submit_uses_versioned_issue_command(tmp_path, monkeypatch):
    path = _write_submission_agent(tmp_path)
    captured = {}
    monkeypatch.setattr(rapp_sdk, "_get_token", lambda: "test-token")
    monkeypatch.setattr(
        rapp_sdk,
        "_fetch_target_registry",
        lambda _upstream, _token: {"agents": [], "lifecycle": {"tombstones": []}},
    )

    def fake_urlopen(request, timeout):
        captured["url"] = request.full_url
        captured["payload"] = json.loads(request.data)
        return FakeResponse({"number": 123, "html_url": "https://example.test/123"})

    monkeypatch.setattr(rapp_sdk.urllib.request, "urlopen", fake_urlopen)
    result = rapp_sdk.submit_agent(str(path), upstream="owner/rar")
    command_text = captured["payload"]["body"].split("```json\n", 1)[1].rsplit(
        "\n```", 1
    )[0]
    command = json.loads(command_text)
    assert result["status"] == "submitted"
    assert result["operation"] == "create"
    assert command["schema"] == "rar-change-request/1.0"
    assert command["operation"] == "create"
    assert command["resource"]["id"] == "@testuser/my_agent"
    assert command["preconditions"] == {"if_none_match": "*"}
    assert command["payload"]["source"]["sha256"].startswith("sha256:")
    assert "labels" not in captured["payload"]


def test_mutation_registry_uses_fresh_contents_api(monkeypatch):
    captured = {}

    def fake_urlopen(request, timeout):
        captured["url"] = request.full_url
        return FakeResponse({"agents": [], "lifecycle": {"tombstones": []}})

    monkeypatch.setattr(rapp_sdk.urllib.request, "urlopen", fake_urlopen)
    registry = rapp_sdk._fetch_target_registry("owner/rar", "test-token")
    assert registry["agents"] == []
    assert captured["url"] == (
        "https://api.github.com/repos/owner/rar/contents/registry.json?ref=main"
    )


def test_submit_update_binds_current_hash(tmp_path, monkeypatch):
    path = _write_submission_agent(tmp_path, "1.1.0")
    monkeypatch.setattr(rapp_sdk, "_get_token", lambda: "test-token")
    monkeypatch.setattr(
        rapp_sdk,
        "_fetch_target_registry",
        lambda _upstream, _token: {
            "agents": [{"name": "@testuser/my_agent", "_sha256": "abc123"}],
            "lifecycle": {"tombstones": []},
        },
    )
    captured = {}

    def fake_urlopen(request, timeout):
        captured["payload"] = json.loads(request.data)
        return FakeResponse({"number": 124, "html_url": "https://example.test/124"})

    monkeypatch.setattr(rapp_sdk.urllib.request, "urlopen", fake_urlopen)
    result = rapp_sdk.submit_agent(str(path), upstream="owner/rar")
    command = json.loads(
        captured["payload"]["body"].split("```json\n", 1)[1].rsplit("\n```", 1)[0]
    )
    assert result["operation"] == "update"
    assert command["preconditions"]["if_match"] == "sha256:abc123"


def test_submit_updates_legacy_official_identity(tmp_path, monkeypatch):
    path = tmp_path / "hacker_news_agent.py"
    path.write_text(
        rapp_sdk.AGENT_TEMPLATE
        .replace("__NAME__", "@rapp/hacker_news")
        .replace("__DISPLAY_NAME__", "Hacker News")
        .replace("__CLASS_NAME__", "HackerNews")
        .replace("__DESCRIPTION__", "Legacy official agent.")
        .replace("__AUTHOR__", "rapp")
        .replace('"quality_tier": "community"', '"quality_tier": "official"')
        .replace('"version": "1.0.0"', '"version": "1.1.0"')
    )
    monkeypatch.setattr(rapp_sdk, "_get_token", lambda: "test-token")
    monkeypatch.setattr(
        rapp_sdk,
        "_fetch_target_registry",
        lambda _upstream, _token: {
            "agents": [{
                "name": "@rapp/hacker_news",
                "version": "1.0.0",
                "quality_tier": "official",
                "_sha256": "abc123",
            }],
            "lifecycle": {"tombstones": []},
        },
    )
    captured = {}

    def fake_urlopen(request, timeout):
        captured["payload"] = json.loads(request.data)
        return FakeResponse({"number": 128, "html_url": "https://example.test/128"})

    monkeypatch.setattr(rapp_sdk.urllib.request, "urlopen", fake_urlopen)
    result = rapp_sdk.submit_agent(str(path), upstream="owner/rar")
    command = json.loads(
        captured["payload"]["body"].split("```json\n", 1)[1].rsplit("\n```", 1)[0]
    )
    assert result["operation"] == "update"
    assert command["resource"]["id"] == "@rapp/hacker_news"
    assert command["preconditions"]["if_match"] == "sha256:abc123"


def test_large_submit_uses_hash_pinned_source_url(tmp_path, monkeypatch):
    path = _write_submission_agent(tmp_path)
    path.write_text(
        path.read_text() + "\n#" + ("x" * rapp_sdk.INLINE_ISSUE_COMMAND_LIMIT)
    )
    monkeypatch.setattr(rapp_sdk, "_get_token", lambda: "test-token")
    monkeypatch.setattr(
        rapp_sdk,
        "_fetch_target_registry",
        lambda _upstream, _token: {"agents": [], "lifecycle": {"tombstones": []}},
    )
    monkeypatch.setattr(
        rapp_sdk,
        "_create_source_gist",
        lambda _code, _filename, _token: (
            "https://gist.githubusercontent.com/user/id/raw/sha/my_agent.py"
        ),
    )
    captured = {}

    def fake_urlopen(request, timeout):
        captured["payload"] = json.loads(request.data)
        return FakeResponse({"number": 127, "html_url": "https://example.test/127"})

    monkeypatch.setattr(rapp_sdk.urllib.request, "urlopen", fake_urlopen)
    rapp_sdk.submit_agent(str(path), upstream="owner/rar")
    command = json.loads(
        captured["payload"]["body"].split("```json\n", 1)[1].rsplit("\n```", 1)[0]
    )
    source = command["payload"]["source"]
    assert "content" not in source
    assert source["url"].startswith("https://gist.githubusercontent.com/")
    assert source["sha256"].startswith("sha256:")


def test_delete_uses_hash_precondition(monkeypatch):
    monkeypatch.setattr(rapp_sdk, "_get_token", lambda: "test-token")
    monkeypatch.setattr(
        rapp_sdk,
        "_fetch_target_registry",
        lambda _upstream, _token: {
            "agents": [{"name": "@testuser/my_agent", "_sha256": "deadbeef"}],
            "lifecycle": {"tombstones": []},
        },
    )
    captured = {}

    def fake_urlopen(request, timeout):
        captured["payload"] = json.loads(request.data)
        return FakeResponse({"number": 125, "html_url": "https://example.test/125"})

    monkeypatch.setattr(rapp_sdk.urllib.request, "urlopen", fake_urlopen)
    result = rapp_sdk.delete_agent(
        "@testuser/my_agent",
        "No longer maintained",
        upstream="owner/rar",
    )
    command = json.loads(
        captured["payload"]["body"].split("```json\n", 1)[1].rsplit("\n```", 1)[0]
    )
    assert result["operation"] == "delete"
    assert command["preconditions"]["if_match"] == "sha256:deadbeef"
    assert command["payload"]["reason"] == "No longer maintained"


def test_request_read_uses_issue_control_plane(monkeypatch):
    monkeypatch.setattr(rapp_sdk, "_get_token", lambda: "test-token")
    captured = {}

    def fake_urlopen(request, timeout):
        captured["payload"] = json.loads(request.data)
        return FakeResponse({"number": 126, "html_url": "https://example.test/126"})

    monkeypatch.setattr(rapp_sdk.urllib.request, "urlopen", fake_urlopen)
    result = rapp_sdk.request_agent_read(
        "@testuser/my_agent",
        upstream="owner/rar",
    )
    command = json.loads(
        captured["payload"]["body"].split("```json\n", 1)[1].rsplit("\n```", 1)[0]
    )
    assert result["operation"] == "read"
    assert command["operation"] == "read"
    assert command["resource"]["id"] == "@testuser/my_agent"


def test_request_status_projects_labels(monkeypatch):
    monkeypatch.setattr(rapp_sdk, "_get_token", lambda: "test-token")
    monkeypatch.setattr(
        rapp_sdk.urllib.request,
        "urlopen",
        lambda _request, timeout: FakeResponse({
            "number": 126,
            "html_url": "https://example.test/126",
            "title": "[RAR] CREATE agent",
            "state": "open",
            "labels": [{"name": "pending-review"}],
            "updated_at": "2026-07-18T20:00:00Z",
        }),
    )
    result = rapp_sdk.request_status(126, upstream="owner/rar")
    assert result["status"] == "pending-review"


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
# SECTION 5: Collection Operations
# ═══════════════════════════════════════════════════════

def test_agents_status():
    status = rapp_sdk.agents_status()
    assert "error" not in status
    assert status["total_agents"] >= 131  # 131 founding + new agents
    assert "by_tier" in status
    assert status["total_pts"] > 0

def test_transfer_card():
    result = rapp_sdk.transfer_card("TEST-MINT-001", "0xdeadbeef1234567890")
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


def test_install_agent_uses_collision_safe_registry_filename(tmp_path, monkeypatch):
    agent = {
        "name": "@one/shared",
        "_file": "agents/@one/shared_agent.py",
        "_install_filename": "rar_one_shared_agent.py",
    }
    monkeypatch.setattr(rapp_sdk, "get_agent_info", lambda name: agent)
    monkeypatch.setattr(rapp_sdk, "_get_token", lambda: None)

    class Response:
        def __enter__(self): return self
        def __exit__(self, *args): return False
        def read(self): return b"print('loaded')\n"

    monkeypatch.setattr(rapp_sdk.urllib.request, "urlopen", lambda *args, **kwargs: Response())
    installed = Path(rapp_sdk.install_agent(agent["name"], str(tmp_path)))
    assert installed.name == agent["_install_filename"]
    assert installed.read_text(encoding="utf-8") == "print('loaded')\n"


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
        assert manifest["name"] == "@test/round_trip_agent"
        assert manifest["display_name"] == "Round Trip"

        errors = rapp_sdk.validate_manifest(str(agent_path), manifest)
        assert errors == [], f"Scaffold produced invalid agent: {errors}"
        source = agent_path.read_text()
        assert 'self.name = "RoundTrip"' in source
        assert '"display_name": "Round Trip"' in source

        contract = dict((name, passed) for name, passed, _ in rapp_sdk.run_contract_tests(str(agent_path)))
        assert contract["runtime_name_is_tool_safe"] is True


def test_contract_rejects_display_name_as_runtime_name(tmp_path):
    agent_path = tmp_path / "bad_runtime_agent.py"
    agent_path.write_text('''
__manifest__ = {
    "schema": "rapp-agent/1.0", "name": "@test/bad_runtime", "version": "1.0.0",
    "display_name": "Bad Runtime", "description": "test", "author": "test",
    "tags": [], "category": "general"
}
from agents.basic_agent import BasicAgent
class BadRuntimeAgent(BasicAgent):
    def __init__(self):
        self.name = "Bad Runtime"
        self.metadata = {"name": self.name}
        super().__init__(self.name, self.metadata)
    def perform(self, **kwargs): return "ok"
''')
    results = dict((name, passed) for name, passed, _ in rapp_sdk.run_contract_tests(str(agent_path)))
    assert results["runtime_name_is_tool_safe"] is False


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

def test_cli_status():
    result = subprocess.run(
        [sys.executable, str(SDK_PATH), "status"],
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
