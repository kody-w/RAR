"""The static API drift gate compares exact bytes without repairing outputs."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
OWNED = (
    "manifest.json",
    "api/v1/status.json",
    "api/v1/badge.json",
    "api/v1/catalog.json",
    "api/v1/taxonomy.json",
    "api/v1/match.json",
    "api/v1/marketplaces.json",
    "api/v1/audience/business.json",
    "api/v1/audience/consumer.json",
    "api/v1/audience/map.json",
)


@pytest.fixture
def checkout(tmp_path):
    for relative in (
        "scripts/build_static_api.py", "scripts/static_api.py",
        "registry.json", "marketplaces.json", "api/v1/skills.json",
        *OWNED,
    ):
        destination = tmp_path / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, destination)
    return tmp_path


def run_builder(checkout, *args):
    return subprocess.run(
        [sys.executable, "scripts/build_static_api.py", *args],
        cwd=checkout, capture_output=True, text=True,
        env={**os.environ, "SOURCE_DATE_EPOCH": "0"},
    )


def snapshot(checkout):
    return {
        path.relative_to(checkout): (path.read_bytes(), path.stat().st_mtime_ns)
        for path in checkout.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }


def test_clean_committed_outputs_match_without_writes(checkout):
    before = snapshot(checkout)
    result = run_builder(checkout, "--check")
    assert result.returncode == 0, result.stdout + result.stderr
    assert snapshot(checkout) == before
    assert not (checkout / "versions").exists()


@pytest.mark.parametrize("relative", OWNED)
def test_one_byte_changed_is_named_and_not_repaired(checkout, relative):
    path = checkout / relative
    original = path.read_bytes()
    assert original.endswith(b"\n")
    path.write_bytes(original[:-1] + b" ")
    before = snapshot(checkout)
    result = run_builder(checkout, "--check")
    assert result.returncode == 1, result.stdout + result.stderr
    assert f"different: {relative}" in result.stderr
    assert snapshot(checkout) == before


@pytest.mark.parametrize("relative", OWNED)
def test_missing_output_is_named_and_not_recreated(checkout, relative):
    (checkout / relative).unlink()
    before = snapshot(checkout)
    result = run_builder(checkout, "--check")
    assert result.returncode == 1, result.stdout + result.stderr
    assert f"missing: {relative}" in result.stderr
    assert snapshot(checkout) == before


def test_all_drift_is_listed_even_for_corrupt_json(checkout):
    (checkout / "api/v1/catalog.json").write_bytes(b"not json\n")
    (checkout / "manifest.json").write_bytes(b"\xff")
    (checkout / "api/v1/badge.json").unlink()
    before = snapshot(checkout)
    result = run_builder(checkout, "--check")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "different: api/v1/catalog.json" in result.stderr
    assert "different: manifest.json" in result.stderr
    assert "missing: api/v1/badge.json" in result.stderr
    assert snapshot(checkout) == before


@pytest.mark.parametrize("corruption", ["[]", "null", "invalid_time", "null_time"])
def test_invalid_output_shape_or_timestamp_is_named(checkout, corruption):
    path = checkout / "api/v1/catalog.json"
    if corruption in ("[]", "null"):
        path.write_text(corruption)
    else:
        payload = json.loads(path.read_text())
        payload["generated"] = "invalid" if corruption == "invalid_time" else None
        path.write_text(json.dumps(payload))
    before = snapshot(checkout)
    result = run_builder(checkout, "--check")
    assert result.returncode == 1, result.stdout + result.stderr
    assert "different: api/v1/catalog.json" in result.stderr
    assert snapshot(checkout) == before


def test_foreign_outputs_and_existing_frames_are_untouched(checkout):
    for relative in (
        "api/v1/index.json", "api/v1/agent/retired.json",
        "api/v1/sprite/retired.svg", "versions/retired.json",
    ):
        path = checkout / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"foreign bytes\n")
    before = snapshot(checkout)
    result = run_builder(checkout, "--check")
    assert result.returncode == 0, result.stdout + result.stderr
    assert snapshot(checkout) == before


def test_normal_build_then_check_uses_the_same_inputs(checkout):
    (checkout / "api/v1/catalog.json").unlink()
    built = run_builder(checkout)
    assert built.returncode == 0, built.stdout + built.stderr
    before = snapshot(checkout)
    checked = run_builder(checkout, "--check")
    assert checked.returncode == 0, checked.stdout + checked.stderr
    assert snapshot(checkout) == before


def test_workflow_checks_after_rebuild_before_commit():
    workflow = yaml.safe_load(
        (ROOT / ".github/workflows/build-registry.yml").read_text()
    )
    steps = workflow["jobs"]["build-registry"]["steps"]
    rebuild = next(i for i, step in enumerate(steps)
                   if "python scripts/build_static_api.py\n" in step.get("run", ""))
    check = next(i for i, step in enumerate(steps)
                 if step.get("run") == "python scripts/build_static_api.py --check")
    commit = next(i for i, step in enumerate(steps)
                  if step.get("name") == "Commit registry.json")
    assert rebuild < check < commit
    assert "if" not in steps[check]
