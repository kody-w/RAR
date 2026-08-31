"""Acceptance tests for portable, local-private RAPP project eggs."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import warnings
import zipfile

import pytest


ROOT = Path(__file__).resolve().parent.parent
AGENT_CANDIDATES = (
    ROOT / "agents" / "@kody-w" / "rapp_projects_agent.py",
    ROOT / "agents" / "@rapp" / "rapp_projects_agent.py",
)
AGENT_PATH = next(
    (candidate for candidate in AGENT_CANDIDATES if candidate.is_file()),
    AGENT_CANDIDATES[0],
)
if os.environ.get("RAPP_PROJECTS_AGENT_PATH"):
    AGENT_PATH = Path(os.environ["RAPP_PROJECTS_AGENT_PATH"]).resolve()
BASIC_AGENT_PATH = ROOT / "agents" / "@rapp" / "basic_agent.py"
PROJECT = "example-project"
ZIP_EPOCH = (1980, 1, 1, 0, 0, 0)
MEMBERS = {
    "manifest.json",
    "chain.jsonl",
    "rappid.json",
    "STATUS.md",
    "agent.py",
    "cell/manifest.json",
    "cell/lineage.json",
}
CONTENT_MEMBERS = MEMBERS - {"manifest.json"}
RAPPID = re.compile(
    r"^rappid:@[a-z0-9]+(?:-[a-z0-9]+)*/"
    r"[a-z0-9]+(?:-[a-z0-9]+)*:[0-9a-f]{64}$"
)


def canonical(value: object) -> str:
    if value is None or isinstance(value, bool):
        return json.dumps(value)
    if isinstance(value, int) and not isinstance(value, bool):
        if abs(value) > 2**53 - 1:
            raise ValueError("integer is outside the RAPP/1 interoperable range")
        return json.dumps(value)
    if isinstance(value, float):
        raise ValueError("RAPP/1 fixture values do not use floats")
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, list):
        return "[" + ",".join(canonical(item) for item in value) + "]"
    if isinstance(value, dict):
        if not all(isinstance(key, str) for key in value):
            raise ValueError("canonical object keys must be strings")
        keys = sorted(value, key=lambda key: key.encode("utf-16-be"))
        return "{" + ",".join(
            json.dumps(key, ensure_ascii=False) + ":" + canonical(value[key])
            for key in keys
        ) + "}"
    raise ValueError(f"non-JSON fixture value: {type(value).__name__}")


def rapp_hash(space: str, value: object) -> str:
    return hashlib.sha256(
        space.encode("utf-8") + b"\n" + canonical(value).encode("utf-8")
    ).hexdigest()


def rapp_bytes_hash(space: str, value: bytes) -> str:
    return hashlib.sha256(space.encode("utf-8") + b"\n" + value).hexdigest()


def load_projects_module():
    if not AGENT_PATH.is_file():
        raise ModuleNotFoundError(
            "required generic project agent is missing from both "
            "agents/@kody-w and agents/@rapp"
        )
    if "agents.basic_agent" not in sys.modules:
        basic_spec = importlib.util.spec_from_file_location(
            "agents.basic_agent", BASIC_AGENT_PATH
        )
        assert basic_spec is not None and basic_spec.loader is not None
        basic = importlib.util.module_from_spec(basic_spec)
        sys.modules["agents.basic_agent"] = basic
        basic_spec.loader.exec_module(basic)
    spec = importlib.util.spec_from_file_location(
        "rapp_projects_egg_acceptance", AGENT_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    sys.path.insert(0, str(AGENT_PATH.parent))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(str(AGENT_PATH.parent))
    return module


@pytest.fixture(scope="module")
def projects():
    return load_projects_module()


def perform(instance, action: str, **request) -> dict[str, object]:
    properties = instance.metadata["parameters"]["properties"]
    action_key = "action" if "action" in properties else "operation"
    choices = properties[action_key].get("enum", [])
    aliases = {
        "export": ("export", "export-project"),
        "import": ("import", "import-project"),
    }
    selected = next(
        (candidate for candidate in aliases.get(action, (action,)) if candidate in choices),
        action,
    )
    result = json.loads(instance.perform(**{action_key: selected}, **request))
    assert isinstance(result, dict)
    return result


def open_project(projects, root: Path, project: str = PROJECT) -> None:
    result = perform(
        projects.RappProjectsAgent(),
        "open",
        root=str(root),
        project=project,
        title="Example project",
        goal="Verify portable project records",
        owner="Example Owner",
        origin="generic-test-fixture",
        visibility="local",
    )
    assert result["status"] == "ok", result


def append_status(
    projects,
    root: Path,
    *,
    project: str = PROJECT,
    status: str = "working",
    pct: int = 25,
    artifacts: list[str] | None = None,
) -> None:
    name = f"generic-test-agent-{status}"
    punched_in = perform(
        projects.RappProjectsAgent(),
        "punchin",
        root=str(root),
        project=project,
        agent=name,
        runtime="generic-test-runtime",
        session_id=f"{name}-session",
        capabilities=["files", "tests"],
        model="generic-test-model",
        host="generic-test-host",
        location="project://work/example",
        intent="Exercise portable project eggs",
        role="builder",
        lease_seconds=86_400,
    )
    assert punched_in["status"] == "ok", punched_in
    updated = perform(
        projects.RappProjectsAgent(),
        "status",
        root=str(root),
        project=project,
        agent=name,
        runtime="generic-test-runtime",
        session_id=f"{name}-session",
        location="project://work/example",
        status=status,
        artifacts=artifacts or [],
        blockers=[],
        next_action="Continue the generic fixture",
        pct=pct,
    )
    assert updated["status"] == "ok", updated


def export_egg(
    projects,
    root: Path,
    *,
    project: str = PROJECT,
) -> tuple[Path, dict[str, object]]:
    destination = root / project / "PROJECT.egg"
    result = perform(
        projects.RappProjectsAgent(),
        "export",
        project=project,
        root=str(root),
        owner_approved=True,
    )
    assert result["status"] == "ok", result
    assert result["owner_approved"] is True
    assert result["egg"]
    assert destination.is_file()
    return destination, result


def snapshot(root: Path) -> dict[str, bytes]:
    if not root.exists():
        return {}
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def write_zip(path: Path, entries: list[tuple[str, bytes]]) -> None:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_STORED) as archive:
            for name, data in entries:
                info = zipfile.ZipInfo(name, date_time=ZIP_EPOCH)
                info.compress_type = zipfile.ZIP_STORED
                archive.writestr(info, data)


def mutate_egg(source: Path, destination: Path, mutation: str) -> Path:
    with zipfile.ZipFile(source) as archive:
        entries = [(name, archive.read(name)) for name in archive.namelist()]
    manifest = json.loads(entries[0][1])

    if mutation == "traversal":
        body = b"must-not-escape"
        manifest["contents"].append(
            {
                "path": "../outside.txt",
                "hash": rapp_bytes_hash("rapp/1:egg", body),
            }
        )
        manifest["contents"].sort(key=lambda item: item["path"].encode("utf-8"))
        entries[0] = (
            "manifest.json",
            canonical(manifest).encode("utf-8"),
        )
        entries.append(("../outside.txt", body))
    elif mutation == "duplicate":
        chain = next(data for name, data in entries if name == "chain.jsonl")
        entries.append(("chain.jsonl", chain))
    elif mutation == "undeclared":
        entries.append(("extra.txt", b"not declared by the manifest"))
    elif mutation == "missing":
        entries = [
            (name, data) for name, data in entries if name != "STATUS.md"
        ]
    elif mutation == "hash":
        entries = [
            (name, data + b"\ntampered\n")
            if name == "STATUS.md"
            else (name, data)
            for name, data in entries
        ]
    else:
        raise AssertionError(f"unknown mutation: {mutation}")

    write_zip(destination, entries)
    return destination


def test_export_requires_approval_and_refuses_unbounded_output(
    projects, tmp_path: Path
) -> None:
    root = tmp_path / "projects"
    outside = tmp_path / "must-not-overwrite.txt"
    open_project(projects, root)

    refused = perform(
        projects.RappProjectsAgent(),
        "export",
        project=PROJECT,
        root=str(root),
    )

    assert refused["status"] == "error"
    message = str(refused["error"]["message"]).lower()
    assert "owner" in message
    assert "approv" in message
    assert not (root / PROJECT / "PROJECT.egg").exists()

    outside.write_bytes(b"must remain unchanged")
    unbounded = perform(
        projects.RappProjectsAgent(),
        "export",
        project=PROJECT,
        root=str(root),
        output=str(outside),
        owner_approved=True,
    )
    assert unbounded["status"] == "error"
    assert "project.egg" in str(unbounded["error"]["message"]).lower()
    assert outside.read_bytes() == b"must remain unchanged"

    egg, _ = export_egg(projects, root)
    assert egg == root / PROJECT / "PROJECT.egg"


def test_export_is_a_canonical_deterministic_rapp_egg(
    projects, tmp_path: Path
) -> None:
    root = tmp_path / "projects"
    artifact = tmp_path / "external-artifact.txt"
    artifact_marker = b"ARTIFACT-BODY-MUST-NOT-BE-IN-THE-EGG"
    artifact.write_bytes(artifact_marker)
    open_project(projects, root)
    append_status(projects, root, artifacts=[str(artifact)])

    egg, _ = export_egg(projects, root)
    first_bytes = egg.read_bytes()
    _, exported = export_egg(projects, root)
    assert egg.read_bytes() == first_bytes
    assert artifact_marker not in first_bytes

    with zipfile.ZipFile(egg) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        assert names[0] == "manifest.json"
        assert names[1:] == sorted(CONTENT_MEMBERS, key=lambda p: p.encode())
        assert set(names) == MEMBERS
        assert len(names) == len(set(names))
        assert archive.comment == b""
        assert all(info.compress_type == zipfile.ZIP_STORED for info in infos)
        assert all(info.date_time == ZIP_EPOCH for info in infos)
        manifest_bytes = archive.read("manifest.json")
        manifest = json.loads(manifest_bytes)
        files = {
            name: archive.read(name)
            for name in names
            if name != "manifest.json"
        }

    assert ".receipt-locators.json" not in names
    assert manifest_bytes == canonical(manifest).encode("utf-8")
    assert set(manifest) == {
        "schema",
        "variant",
        "rappid",
        "created_utc",
        "contents",
        "payload",
        "sig",
    }
    assert manifest["schema"] == "rapp/1-egg"
    assert manifest["variant"] == "rapplication"
    assert RAPPID.fullmatch(manifest["rappid"])
    assert re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z",
        manifest["created_utc"],
    )
    assert manifest["sig"] is None
    paths = [item["path"] for item in manifest["contents"]]
    assert paths == sorted(CONTENT_MEMBERS, key=lambda p: p.encode())
    assert all(
        path
        and not path.startswith("/")
        and "\\" not in path
        and all(part not in {"", ".", ".."} for part in path.split("/"))
        for path in paths
    )
    assert all(set(item) == {"path", "hash"} for item in manifest["contents"])
    assert {
        item["path"]: item["hash"] for item in manifest["contents"]
    } == {
        path: rapp_bytes_hash("rapp/1:egg", data)
        for path, data in files.items()
    }

    payload = manifest["payload"]
    assert payload["visibility"] == "local-private"
    warning = payload["warning"].lower()
    assert "local-private" in warning
    assert "owner approval" in warning
    expected_address = rapp_hash(
        "rapp/1:egg-manifest",
        {key: value for key, value in manifest.items() if key != "sig"},
    )
    reported_address = exported.get("egg_hash") or exported.get(
        "manifest_address"
    )
    if reported_address is None:
        assert hasattr(projects, "egg_address")
        reported_address = projects.egg_address(manifest)
    assert reported_address == expected_address


def test_egg_status_is_portable_across_working_directories(
    projects,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root = tmp_path / "projects"
    open_project(projects, root)
    punched_in = perform(
        projects.RappProjectsAgent(),
        "punchin",
        root=str(root),
        project=PROJECT,
        agent="portable-runtime",
        runtime="generic-runtime",
        session_id="portable-session",
        capabilities=["files"],
        location=str(root / "private-worktree"),
        intent="Prove CWD-independent egg verification",
        role="builder",
    )
    assert punched_in["status"] == "ok"
    egg, _ = export_egg(projects, root)

    unrelated = tmp_path / "unrelated-working-directory"
    unrelated.mkdir()
    monkeypatch.chdir(unrelated)
    verified = projects.verify_project_egg(egg)

    assert verified["manifest"]["payload"]["project"] == PROJECT
    assert b"[local-private-path]" in verified["files"]["STATUS.md"]


def test_imported_external_receipts_are_unverifiable_until_rebound(
    projects,
    tmp_path: Path,
) -> None:
    source_root = tmp_path / "source-projects"
    destination = tmp_path / "imported-projects"
    artifact = tmp_path / "external-artifact.txt"
    artifact.write_text("generic external evidence\n", encoding="utf-8")
    open_project(projects, source_root)
    append_status(projects, source_root, artifacts=[str(artifact)])
    egg, _ = export_egg(projects, source_root)

    imported = perform(
        projects.RappProjectsAgent(),
        "import",
        root=str(destination),
        egg=str(egg),
    )
    assert imported["status"] == "ok"
    assert not (
        destination / PROJECT / ".receipt-locators.json"
    ).exists()

    verified = perform(
        projects.RappProjectsAgent(),
        "verify",
        root=str(destination),
        project=PROJECT,
    )
    assert verified["status"] == "ok"
    assert verified["verdict"] == "fail"
    assert len(verified["broken_receipts"]) == 1
    assert verified["broken_receipts"][0]["path"].startswith(
        "local-private://"
    )


@pytest.mark.parametrize(
    "mutation",
    ["traversal", "duplicate", "undeclared", "missing", "hash"],
)
def test_import_rejects_malformed_egg_before_creating_destination(
    projects, tmp_path: Path, mutation: str
) -> None:
    source_root = tmp_path / "source-projects"
    open_project(projects, source_root)
    source, _ = export_egg(projects, source_root)
    malformed = mutate_egg(
        source, tmp_path / f"{mutation}-project.egg", mutation
    )
    destination = tmp_path / f"{mutation}-destination"

    refused = perform(
        projects.RappProjectsAgent(),
        "import",
        root=str(destination),
        path=str(malformed),
    )

    assert refused["status"] == "error"
    assert not destination.exists()
    assert not (tmp_path / "outside.txt").exists()


def test_import_is_idempotent(projects, tmp_path: Path) -> None:
    source_root = tmp_path / "source-projects"
    destination = tmp_path / "imported-projects"
    open_project(projects, source_root)
    append_status(projects, source_root, status="ready", pct=80)
    egg, _ = export_egg(projects, source_root)

    first = perform(
        projects.RappProjectsAgent(),
        "import",
        root=str(destination),
        path=str(egg),
    )
    after_first = snapshot(destination)
    second = perform(
        projects.RappProjectsAgent(),
        "import",
        root=str(destination),
        path=str(egg),
    )

    assert first["status"] == "ok"
    assert snapshot(destination) == after_first
    assert second["created"] is False
    assert second["imported_frames"] == 0
    assert list(destination.rglob("chain.jsonl"))


def test_divergent_import_is_refused_without_mutation(
    projects, tmp_path: Path
) -> None:
    left = tmp_path / "left-projects"
    right = tmp_path / "right-projects"
    open_project(projects, left)
    seed, _ = export_egg(projects, left)
    imported = perform(
        projects.RappProjectsAgent(),
        "import",
        root=str(right),
        path=str(seed),
    )
    assert imported["status"] == "ok"
    append_status(projects, left, status="left-branch", pct=40)
    append_status(projects, right, status="right-branch", pct=45)
    left_egg, _ = export_egg(projects, left)
    before = snapshot(right)

    refused = perform(
        projects.RappProjectsAgent(),
        "import",
        root=str(right),
        path=str(left_egg),
    )

    assert refused["status"] == "error"
    message = str(refused["error"]["message"]).lower()
    assert "diverg" in message or "fork" in message
    assert snapshot(right) == before
