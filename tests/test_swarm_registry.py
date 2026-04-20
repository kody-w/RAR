"""
Tests for swarm support in the registry builder.
Validates converged swarms (from swarms/) and stack-promoted swarms.
"""

import ast
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_JSON = REPO_ROOT / "registry.json"
SWARMS_DIR = REPO_ROOT / "swarms"

# Ensure build_registry module is importable
sys.path.insert(0, str(REPO_ROOT))


# ═══════════════════════════════════════════════════════════════
# Extraction and Validation Unit Tests
# ═══════════════════════════════════════════════════════════��═══

class TestSwarmExtraction:
    def test_extract_swarm_returns_dict(self, tmp_path):
        from build_registry import extract_swarm
        agent = tmp_path / "test_agent.py"
        agent.write_text('''
__swarm__ = {
    "schema": "rapp-swarm/1.0",
    "id": "test",
    "display_name": "Test",
    "summary": "A test swarm.",
    "category": "pipeline",
    "publisher": "@test",
    "type": "converged",
    "produced_by": {"method": "manual", "cycles": 1, "source_files_collapsed": 2, "specialists": []},
}
''')
        result = extract_swarm(agent)
        assert isinstance(result, dict)
        assert result["schema"] == "rapp-swarm/1.0"
        assert result["id"] == "test"

    def test_extract_swarm_returns_none_for_no_swarm(self, tmp_path):
        from build_registry import extract_swarm
        agent = tmp_path / "test_agent.py"
        agent.write_text('__manifest__ = {"schema": "rapp-agent/1.0"}\n')
        result = extract_swarm(agent)
        assert result is None

    def test_extract_swarm_rejects_non_literal(self, tmp_path):
        from build_registry import extract_swarm
        agent = tmp_path / "test_agent.py"
        agent.write_text('__swarm__ = dict(schema="rapp-swarm/1.0")\n')
        result = extract_swarm(agent)
        assert result is None


class TestSwarmValidation:
    def test_validate_swarm_all_required_fields(self, tmp_path):
        from build_registry import validate_swarm
        agent = tmp_path / "test.py"
        swarm = {
            "schema": "rapp-swarm/1.0",
            "id": "test",
            "display_name": "Test",
            "summary": "Summary.",
            "category": "pipeline",
            "publisher": "@test",
            "produced_by": {"method": "manual"},
        }
        errors = validate_swarm(agent, swarm)
        assert errors == []

    def test_validate_swarm_missing_fields(self, tmp_path):
        from build_registry import validate_swarm
        agent = tmp_path / "test.py"
        swarm = {"schema": "rapp-swarm/1.0"}
        errors = validate_swarm(agent, swarm)
        assert len(errors) >= 5  # missing id, display_name, summary, category, publisher, produced_by

    def test_validate_swarm_wrong_schema(self, tmp_path):
        from build_registry import validate_swarm
        agent = tmp_path / "test.py"
        swarm = {
            "schema": "rapp-swarm/2.0",
            "id": "test",
            "display_name": "Test",
            "summary": "Summary.",
            "category": "pipeline",
            "publisher": "@test",
            "produced_by": {"method": "manual"},
        }
        errors = validate_swarm(agent, swarm)
        assert any("Invalid swarm schema" in e for e in errors)

    def test_validate_swarm_produced_by_must_have_method(self, tmp_path):
        from build_registry import validate_swarm
        agent = tmp_path / "test.py"
        swarm = {
            "schema": "rapp-swarm/1.0",
            "id": "test",
            "display_name": "Test",
            "summary": "Summary.",
            "category": "pipeline",
            "publisher": "@test",
            "produced_by": {},
        }
        errors = validate_swarm(agent, swarm)
        assert any("produced_by" in e for e in errors)


# ═══════════════════════════════════════════════════════════════
# Registry Build Integration Tests
# ═══════════════════════════════════════════════════════════════

class TestSwarmRegistryBuild:
    @pytest.fixture(autouse=True)
    def _load_registry(self):
        """Ensure registry.json exists by running build if needed."""
        if not REGISTRY_JSON.exists():
            subprocess.run(
                [sys.executable, str(REPO_ROOT / "build_registry.py")],
                capture_output=True, text=True, timeout=120,
                cwd=str(REPO_ROOT),
            )
        self.reg = json.loads(REGISTRY_JSON.read_text())

    def test_build_includes_swarms_array(self):
        assert "swarms" in self.reg
        assert isinstance(self.reg["swarms"], list)

    def test_converged_swarms_have_swarm_metadata(self):
        converged = [s for s in self.reg["swarms"] if s.get("type") == "converged"]
        for s in converged:
            assert "_swarm" in s, f"Converged swarm {s['name']} missing _swarm metadata"
            assert s["_swarm"]["schema"] == "rapp-swarm/1.0"
            assert "produced_by" in s["_swarm"]

    def test_stack_swarms_generated(self):
        stack_swarms = [s for s in self.reg["swarms"] if s.get("type") == "stack"]
        assert len(stack_swarms) > 0, "No stack swarms generated from existing stacks"

    def test_stack_swarm_agent_count_matches(self):
        stack_swarms = [s for s in self.reg["swarms"] if s.get("type") == "stack"]
        for s in stack_swarms:
            assert s["agent_count"] == len(s["agents"]), (
                f"Stack {s['name']}: agent_count={s['agent_count']} != len(agents)={len(s['agents'])}"
            )

    def test_stack_swarm_agent_files_exist(self):
        stack_swarms = [s for s in self.reg["swarms"] if s.get("type") == "stack"]
        for s in stack_swarms:
            for f in s.get("agent_files", []):
                assert (REPO_ROOT / f).exists(), f"Agent file {f} in swarm {s['name']} does not exist"

    def test_seed_unique_across_agents_and_swarms(self):
        seen = {}
        for item in self.reg.get("agents", []) + self.reg.get("swarms", []):
            seed = item.get("_seed")
            if seed is None:
                continue
            assert seed not in seen, (
                f"Seed collision: {item.get('name')} and {seen[seed]} both have seed {seed}"
            )
            seen[seed] = item.get("name")

    def test_registry_backward_compat_stacks_present(self):
        assert "stacks" in self.reg
        assert isinstance(self.reg["stacks"], dict)
        assert len(self.reg["stacks"]) > 0

    def test_registry_backward_compat_agents_present(self):
        assert "agents" in self.reg
        assert len(self.reg["agents"]) >= 131

    def test_registry_schema_version_bumped(self):
        assert self.reg["schema"] == "rapp-registry/1.1"
        assert self.reg["version"] == "1.1.0"

    def test_stats_include_swarm_count(self):
        assert "total_swarms" in self.reg["stats"]
        assert self.reg["stats"]["total_swarms"] == len(self.reg["swarms"])

    def test_converged_swarm_files_exist(self):
        converged = [s for s in self.reg["swarms"] if s.get("type") == "converged"]
        for s in converged:
            assert (REPO_ROOT / s["_file"]).exists(), f"Swarm file {s['_file']} does not exist"


# ═══════════════════════════════════════════════════════════════
# Swarm File Contract Tests
# ═══════════════════════════════════════════════════════════════

class TestSwarmFileContract:
    @pytest.fixture(params=list(SWARMS_DIR.rglob("*.py")) if SWARMS_DIR.exists() else [],
                    ids=lambda p: str(p.relative_to(REPO_ROOT)))
    def swarm_path(self, request):
        return request.param

    def test_swarm_has_manifest(self, swarm_path):
        from build_registry import extract_manifest
        m = extract_manifest(swarm_path)
        assert m is not None, f"{swarm_path} has no __manifest__"

    def test_swarm_has_swarm_dict(self, swarm_path):
        from build_registry import extract_swarm
        s = extract_swarm(swarm_path)
        assert s is not None, f"{swarm_path} has no __swarm__"

    def test_swarm_manifest_valid(self, swarm_path):
        from build_registry import extract_manifest, validate_manifest
        m = extract_manifest(swarm_path)
        if m:
            errors = validate_manifest(swarm_path, m)
            assert errors == [], f"{swarm_path} manifest errors: {errors}"

    def test_swarm_swarm_valid(self, swarm_path):
        from build_registry import extract_swarm, validate_swarm
        s = extract_swarm(swarm_path)
        if s:
            errors = validate_swarm(swarm_path, s)
            assert errors == [], f"{swarm_path} swarm errors: {errors}"

    def test_swarm_parseable(self, swarm_path):
        source = swarm_path.read_text()
        tree = ast.parse(source)
        assert tree is not None
