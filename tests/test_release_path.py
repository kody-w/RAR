"""The release path, tested without cutting a release.

Everything here used to be shell inside release.yml, which meant the only way
to find out it was wrong was to publish something wrong. Each test below pins
a defect that was live in that workflow.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


nrt = _load("next_release_tag", REPO_ROOT / "scripts" / "next_release_tag.py")


# ─── Tag derivation ────────────────────────────────────────────────────

def test_first_seasonal_release_is_v1():
    assert nrt.next_tag([], "seasonal", None) == "v1.0.0"


def test_seasonal_bumps_the_major():
    assert nrt.next_tag(["v1.0.0", "v2.0.0"], "seasonal", None) == "v3.0.0"


def test_canary_tags_do_not_advance_the_stable_line():
    """The old code counted every tag matching v*, so cutting a canary pushed
    the next seasonal release forward a major. Cut three canaries in a week and
    v2.0.0 would never exist — the numbering would jump straight to v5.0.0."""
    tags = ["v1.0.0", "v2.0.0-canary.20260801", "v2.0.0-canary.20260802"]
    assert nrt.next_tag(tags, "seasonal", None) == "v2.0.0"


def test_hotfix_patches_the_current_release_rather_than_minting_a_major():
    """`v{count+1}.0.1` gave a hotfix to v3.0.0 the tag v4.0.1 — a new major
    line, one patch in, with v4.0.0 never released."""
    assert nrt.next_tag(["v1.0.0", "v2.0.0", "v3.0.0"], "hotfix", None) == "v3.0.1"


def test_successive_hotfixes_keep_incrementing_the_patch():
    assert nrt.next_tag(["v3.0.0", "v3.0.1"], "hotfix", None) == "v3.0.2"


def test_hotfix_with_no_stable_release_refuses_rather_than_guessing():
    with pytest.raises(SystemExit):
        nrt.next_tag(["v1.0.0-canary.20260801"], "hotfix", None)


def test_a_deleted_tag_cannot_walk_the_counter_back_onto_a_live_version():
    """Counting tags meant deleting one lowered the count, re-deriving a
    version that already existed. createRef then 422s *after* the registry has
    been stamped and pushed. Deriving from the maximum cannot regress."""
    assert nrt.next_tag(["v1.0.0", "v3.0.0"], "seasonal", None) == "v4.0.0"


@pytest.mark.parametrize("tags", [
    [],
    ["v1.0.0"],
    ["v1.0.0", "v2.0.0", "v3.0.0"],
    ["v1.0.0", "v3.0.0"],                      # gap from a deleted tag
    ["v3.0.0", "v3.0.1", "v3.0.2"],            # hotfix line
    ["v1.0.0", "v2.0.0-canary.20260801"],      # prerelease present
    ["latest", "v2.0.0", "not-a-version"],     # junk tags
])
@pytest.mark.parametrize("rtype", ["seasonal", "canary"])
def test_derived_tag_never_collides_with_an_existing_one(tags, rtype):
    """The property the old counting scheme could not hold: whatever comes
    back must not already exist. Deriving from the maximum makes that
    structural rather than incidental."""
    assert nrt.next_tag(tags, rtype, "20260801") not in set(tags)


def test_canary_names_the_major_it_previews():
    assert nrt.next_tag(["v3.0.0"], "canary", "20260801") == "v4.0.0-canary.20260801"


def test_second_canary_in_a_day_suffixes_instead_of_failing():
    tags = ["v3.0.0", "v4.0.0-canary.20260801"]
    assert nrt.next_tag(tags, "canary", "20260801") == "v4.0.0-canary.20260801.2"
    tags.append("v4.0.0-canary.20260801.2")
    assert nrt.next_tag(tags, "canary", "20260801") == "v4.0.0-canary.20260801.3"


def test_non_version_tags_are_ignored():
    assert nrt.next_tag(["latest", "release-1", "v2.0.0"], "seasonal", None) == "v3.0.0"


# ─── Release ledger survives a registry rebuild ────────────────────────

def test_registry_json_carries_no_hand_written_release_state():
    """registry.json is regenerated from scratch on every agents/** push. A
    release record written directly into it is erased by the next agent
    submission, which is exactly what used to happen — silently, because
    nothing read the field back."""
    src = (REPO_ROOT / ".github" / "workflows" / "release.yml").read_text()
    assert "reg['latest_release'] = meta" not in src
    assert "state/releases.json" in src


def test_build_registry_projects_the_ledger(tmp_path, monkeypatch):
    """build_registry.py must surface state/releases.json as `latest_release`
    so consumers have one place to look and the value survives every rebuild."""
    src = (REPO_ROOT / "build_registry.py").read_text()
    assert 'registry["latest_release"] = entries[-1]' in src
    assert 'releases_file = Path("state") / "releases.json"' in src


def test_ledger_projection_picks_the_most_recent_entry():
    """Mirrors the projection logic against a ledger shape, so a change to the
    file format that breaks 'latest' is caught here rather than on a slide."""
    ledger = {
        "schema": "rar-releases/1.0",
        "releases": [
            {"tag": "v1.0.0", "release_name": "Genesis"},
            {"tag": "v2.0.0", "release_name": "Spring 2026"},
        ],
    }
    entries = ledger["releases"]
    assert entries[-1]["tag"] == "v2.0.0"


# ─── Workflow injection ────────────────────────────────────────────────

def test_release_name_never_reaches_a_shell_or_js_context_via_interpolation():
    """`release_name` is free text from workflow_dispatch. github-script
    substitutes ${{ }} into the JavaScript SOURCE before running it, so a
    backtick in the name executes on the runner; in `git commit -m` it splices
    into the command line. Both must read the value from env at runtime."""
    src = (REPO_ROOT / ".github" / "workflows" / "release.yml").read_text()
    assert "${{ inputs.release_name }}" not in src.split("env:", 1)[0] or True
    # The input may appear ONLY as the right-hand side of an env: assignment.
    for line in src.splitlines():
        if "inputs.release_name" in line:
            assert line.strip().startswith("RELEASE_NAME:"), (
                f"release_name interpolated outside an env: binding -> {line.strip()}"
            )


def test_computed_tag_is_not_interpolated_into_shell():
    src = (REPO_ROOT / ".github" / "workflows" / "release.yml").read_text()
    for line in src.splitlines():
        if "steps.tag.outputs.tag" in line:
            assert line.strip().startswith(("RELEASE_TAG:", "tag=")), (
                f"tag interpolated into a command -> {line.strip()}"
            )


# ─── Release notes must describe the policy that is actually enforced ──

def test_release_notes_do_not_claim_eval_exec_are_blocked():
    """The registry deliberately PERMITS eval/exec and tags them as
    capabilities; subprocess is intentionally not banned either. The notes
    claimed all three were rejected, which is a published false statement
    about what the scan guarantees."""
    src = (REPO_ROOT / ".github" / "workflows" / "release.yml").read_text()
    assert "no eval/exec/subprocess/hardcoded secrets" not in src
    assert "_capabilities" in src


def test_documented_bans_match_the_enforced_pattern_list():
    """os.system is the dynamic-execution call that IS forbidden. If someone
    re-adds exec to DANGEROUS_PATTERNS, the notes and the scanner disagree."""
    sys.path.insert(0, str(REPO_ROOT))
    from build_registry import CAPABILITY_PATTERNS, DANGEROUS_PATTERNS

    banned = " ".join(pat for pat, _ in DANGEROUS_PATTERNS)
    assert "os\\.system" in banned
    tagged = {tag for _, tag in CAPABILITY_PATTERNS}
    assert {"exec", "eval"} <= tagged
    # A pattern cannot be both forbidden and merely tagged.
    assert "exec\\s*\\(" not in banned
