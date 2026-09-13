"""Pinned, additive repository workspace bootstrap overlay."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BOOTSTRAP_DIR = ROOT / ".rapp"
CONFIG_PATH = BOOTSTRAP_DIR / "bootstrap.json"
WRAPPER_PATH = BOOTSTRAP_DIR / "bootstrap.py"
MANAGED_PATH = BOOTSTRAP_DIR / "bootstrap-managed.json"
SKILL_PATH = (
    ROOT
    / ".github"
    / "skills"
    / "rapp-workspace-bootstrap"
    / "SKILL.md"
)
ROOT_SKILL = ROOT / "skill.md"
SOURCE_COMMIT = "b0e37eb3c67e309f342629e0ec96dea2688a5951"
AUTHORITY_COMMIT = "dda32d741c7218f41443a5bd17eebfe0eae82cb7"
BEGIN = b"<!-- rapp-workspace-bootstrap:begin -->"
END = b"<!-- rapp-workspace-bootstrap:end -->"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def test_public_bootstrap_overlay_is_exactly_pinned():
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    assert config["schema"] == "rapp-repository-bootstrap/1"
    assert config["operator"]["source_commit"] == SOURCE_COMMIT
    assert config["operator"]["url"].endswith(
        f"/{SOURCE_COMMIT}/rapp_workspace.py"
    )
    assert len(config["operator"]["sha256"]) == 64
    assert config["authority"]["commit"] == AUTHORITY_COMMIT
    assert config["authority"]["revision"] == "rev-15"
    assert config["local_only"] is True


def test_wrapper_embeds_the_reviewed_config_without_importing_it():
    tree = ast.parse(WRAPPER_PATH.read_text(encoding="utf-8"))
    expected = None
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "EXPECTED"
        ):
            expected = ast.literal_eval(node.value)
            break
    assert expected == json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def test_managed_hashes_bind_public_files_and_root_block():
    managed = json.loads(MANAGED_PATH.read_text(encoding="utf-8"))
    assert managed["schema"] == "rapp-bootstrap-managed/1"
    assert managed["root_skill"] == "skill.md"
    for relative, digest in managed["files"].items():
        assert sha256((ROOT / relative).read_bytes()) == digest

    root_skill = ROOT_SKILL.read_bytes()
    assert root_skill.count(BEGIN) == 1
    assert root_skill.count(END) == 1
    start = root_skill.index(BEGIN)
    end = root_skill.index(END) + len(END)
    assert sha256(root_skill[start:end]) == managed["root_block_sha256"]


def test_root_skill_keeps_existing_api_and_adds_managed_bootstrap():
    text = ROOT_SKILL.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    assert "## API — How to Use This Repo Programmatically" in text
    assert "## Workspace Bootstrap (Reserved, Additive)" in text
    assert text.index("## Workspace Bootstrap (Reserved, Additive)") < text.index(
        "<!-- rapp-workspace-bootstrap:begin -->"
    )
    assert "Neither a clone nor this bootstrap certifies RAPP/1" in normalized
    assert AUTHORITY_COMMIT in text


def test_bootstrap_skill_is_discoverable_and_non_claiming():
    text = SKILL_PATH.read_text(encoding="utf-8")
    assert "name: rapp-workspace-bootstrap" in text
    assert "python3 .rapp/bootstrap.py audit" in text
    assert "python3 .rapp/bootstrap.py bootstrap --apply" in text
    assert "authenticated/production conformance are separate" in text


def test_private_workspace_paths_are_root_ignored():
    ignored = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    for relative in (
        ".rapp/cache/",
        ".rapp/workspace/",
        ".rapp/reports/",
    ):
        assert relative in ignored
