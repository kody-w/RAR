"""Storage acceptance tests for the generic RAPP Projects agent.

Every fixture is synthetic. The tests always select a temporary authority and
never inspect or mutate the user's real project store.
"""

from __future__ import annotations

import builtins
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import re
import sys
from types import SimpleNamespace
import uuid
from unittest import mock

import pytest


REPOSITORY = Path(__file__).resolve().parents[1]
AGENT_PATH = REPOSITORY / "agents" / "@kody-w" / "rapp_projects_agent.py"
CELL_KEYS = {"schema", "layer", "path", "context", "children", "souls"}
ABSOLUTE_USER_PATH = re.compile(
    r"(?<![A-Za-z0-9+.-])/(?:Users|home|root|private|Volumes|mnt)/"
    r"[^\s`\"'<>]*|\b[A-Za-z]:[\\/](?:Users|Documents and Settings)[\\/]",
    re.IGNORECASE,
)


def load_agent(name: str):
    if not AGENT_PATH.is_file():
        raise ModuleNotFoundError(
            "required generic project agent is missing: "
            "agents/@kody-w/rapp_projects_agent.py"
        )
    basic_agent_dir = REPOSITORY / "agents" / "@rapp"
    for import_root in (REPOSITORY, basic_agent_dir):
        if str(import_root) not in sys.path:
            sys.path.insert(0, str(import_root))
    spec = importlib.util.spec_from_file_location(name, AGENT_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {AGENT_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def projects(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    monkeypatch.setenv("RAPP_PROJECTS_ROOT", str(tmp_path / "configured-root"))
    return load_agent(f"rapp_projects_storage_{uuid.uuid4().hex}")


def perform(instance, action: str, *, root: Path | None = None, **values) -> dict:
    if root is not None:
        values["root"] = str(root)
    result = json.loads(instance.perform(operation=action, **values))
    assert isinstance(result, dict)
    return result


def actor(name: str = "fixture-agent") -> dict[str, object]:
    return {
        "agent": name,
        "runtime": "fixture-runtime",
        "session_id": f"{name}-session",
        "model": "fixture-model",
        "host": "fixture-host",
        "capabilities": ["files", "shell"],
    }


def open_project(agent, root: Path, project: str = "alpha-project") -> dict:
    return perform(
        agent,
        "open",
        root=root,
        project=project,
        title=f"{project} title",
        goal="Exercise the generic storage contract",
        owner="example-owner",
        origin="generic-fixture",
        visibility="local",
    )


def punch_in(agent, root: Path, project: str, current_actor: dict) -> dict:
    return perform(
        agent,
        "punchin",
        root=root,
        project=project,
        **current_actor,
        location="project://work",
        intent="Exercise generic project storage",
        role="builder",
    )


def project_directory(root: Path, project: str) -> Path:
    return root / project


def frames(root: Path, project: str) -> list[dict]:
    chain = project_directory(root, project) / "chain.jsonl"
    if not chain.is_file():
        return []
    return [
        json.loads(line)
        for line in chain.read_text(encoding="utf-8").splitlines()
    ]


def frame_event(frame: dict) -> str:
    return str(frame["kind"])


def authoritative_frame_count(root: Path, project: str) -> int:
    return len(frames(root, project))


def derived_paths(root: Path) -> list[Path]:
    names = {
        "BOARD.md",
        "CATCHUP.md",
        "index.json",
        "STATUS.md",
        "RESUME.md",
        "HANDOFF.md",
    }
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and path.name in names
    )


def corrupt_genesis_title(root: Path, project: str, marker: str) -> None:
    chain = project_directory(root, project) / "chain.jsonl"
    values = [
        json.loads(line)
        for line in chain.read_text(encoding="utf-8").splitlines()
    ]
    values[0]["payload"]["title"] = marker
    chain.write_text(
        "".join(
            json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n"
            for value in values
        ),
        encoding="utf-8",
    )


def parse_utc(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ").replace(
        tzinfo=timezone.utc
    )


def fold_at(projects, root: Path, project: str, now: datetime) -> dict:
    project_frames = frames(root, project)
    fold = getattr(projects, "fold_project", None)
    if fold is not None:
        parameters = inspect.signature(fold).parameters
        values = {"frames": project_frames}
        if "root" in parameters:
            values["root"] = root
        if "now" in parameters:
            values["now"] = now
        return fold(project, **values)

    store_type = getattr(projects, "ProjectStore", None)
    if store_type is not None:
        store = store_type(root, clock=lambda: now.timestamp())
        fold_frames = getattr(store, "_fold_frames", None)
        if fold_frames is not None:
            return fold_frames(project, project_frames)
        return store._fold(project)

    fold = getattr(projects, "_fold", None)
    assert fold is not None, "the project store must expose deterministic folding"
    parameters = inspect.signature(fold).parameters
    values = {}
    if "frames" in parameters:
        values["frames"] = project_frames
    if "root" in parameters:
        values["root"] = root
    if "now" in parameters:
        values["now"] = now
    return fold(project, **values)


def test_parallel_appends_are_atomic_and_never_lose_an_update(
    projects, tmp_path: Path
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root)["status"] == "ok"
    current_actor = actor()
    assert punch_in(agent, root, "alpha-project", current_actor)["status"] == "ok"

    def publish(index: int) -> dict:
        return perform(
            projects.RappProjectsAgent(),
            "status",
            root=root,
            project="alpha-project",
            **current_actor,
            location=f"project://work/{index}",
            status=f"parallel-update-{index}",
            artifacts=[],
            blockers=[],
            next_action=f"Continue after update {index}",
            pct=index,
        )

    with ThreadPoolExecutor(max_workers=6) as executor:
        results = list(executor.map(publish, range(1, 17)))

    assert all(result["status"] == "ok" for result in results)
    project_frames = frames(root, "alpha-project")
    assert [frame["seq"] for frame in project_frames] == list(range(18))
    assert all(
        current["prev"] == previous["payload_hash"]
        for previous, current in zip(project_frames, project_frames[1:])
    )
    updates = {
        frame["payload"]["status"]
        for frame in project_frames
        if frame_event(frame) == "work.status"
    }
    assert updates == {f"parallel-update-{index}" for index in range(1, 17)}


def test_root_override_precedence_is_explicit_then_environment_then_default(
    projects,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    explicit_root = tmp_path / "explicit-control"
    environment_root = tmp_path / "environment-control"
    monkeypatch.setenv("RAPP_PROJECTS_ROOT", str(environment_root))
    agent = projects.RappProjectsAgent()

    explicit = perform(agent, "board", root=explicit_root)
    assert explicit["status"] == "ok"
    assert explicit_root.is_dir()
    assert not environment_root.exists()

    inherited = perform(agent, "board")
    assert inherited["status"] == "ok"
    assert environment_root.is_dir()

    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.delenv("RAPP_PROJECTS_ROOT")
    monkeypatch.setenv("HOME", str(fake_home))
    monkeypatch.setattr(Path, "home", classmethod(lambda cls: fake_home))
    reloaded = load_agent(f"rapp_projects_default_{uuid.uuid4().hex}")
    default = perform(reloaded.RappProjectsAgent(), "board")
    expected = fake_home / ".rapp" / "projects-control"
    assert default["status"] == "ok"
    assert expected.is_dir()


@pytest.mark.parametrize(
    "unsafe",
    (
        "../escape",
        "alpha/../../escape",
        "/absolute-project",
        r"C:\Users\Example\escape",
        r"..\escape",
        ".hidden",
        "UPPER",
    ),
)
def test_unsafe_project_slugs_and_path_escapes_are_refused(
    projects, tmp_path: Path, unsafe: str
) -> None:
    root = tmp_path / "control"
    with pytest.raises(projects.RappProjectsError):
        projects.safe_join(root, "..", "escape")
    result = open_project(projects.RappProjectsAgent(), root, unsafe)
    assert result["status"] == "error"
    assert not (tmp_path / "escape").exists()
    assert not project_directory(root, "escape").exists()


def test_corruption_is_never_returned_as_a_success_shaped_result(
    projects, tmp_path: Path
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root)["status"] == "ok"
    corrupt_genesis_title(root, "alpha-project", "unverified mutation")
    count_before = authoritative_frame_count(root, "alpha-project")

    verified = perform(
        agent,
        "verify",
        root=root,
        project="alpha-project",
    )
    assert verified["status"] == "error"
    assert verified.get("verdict") != "pass"
    assert re.search(
        r"hash|corrupt|verif",
        json.dumps(verified),
        re.IGNORECASE,
    )

    appended = perform(
        agent,
        "status",
        root=root,
        project="alpha-project",
        **actor(),
        location="project://work",
        status="must not append",
        artifacts=[],
        blockers=[],
        next_action="Preserve evidence",
        pct=50,
    )
    assert appended["status"] == "error"
    assert re.search(
        r"hash|corrupt|verif",
        json.dumps(appended),
        re.IGNORECASE,
    )
    assert authoritative_frame_count(root, "alpha-project") == count_before


def test_committed_append_reports_view_refresh_failure_without_retry_signal(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root, "alpha-project")["status"] == "ok"
    assert open_project(agent, root, "beta-project")["status"] == "ok"
    corrupt_genesis_title(root, "beta-project", "unverified sibling mutation")
    count_before = authoritative_frame_count(root, "alpha-project")

    result = perform(
        agent,
        "status",
        root=root,
        project="alpha-project",
        **actor(),
        location="project://work",
        status="authoritative append committed",
        artifacts=[],
        blockers=[],
        next_action="Repair the sibling before rebuilding views",
        pct=60,
    )

    assert result["status"] == "ok"
    assert result["operation"] == "status"
    assert result["view_refresh"]["status"] == "error"
    assert result["view_refresh"]["error"]["code"] == "chain-verification"
    assert authoritative_frame_count(root, "alpha-project") == count_before + 1
    assert frames(root, "alpha-project")[-1]["payload"]["status"] == (
        "authoritative append committed"
    )


def test_root_and_project_cells_have_exact_manifests_and_separate_lineage(
    projects, tmp_path: Path
) -> None:
    root = tmp_path / "control"
    assert open_project(projects.RappProjectsAgent(), root)["status"] == "ok"

    manifests = []
    for path in root.rglob("manifest.json"):
        value = json.loads(path.read_text(encoding="utf-8"))
        if value.get("schema") == "rapp-cell/1.0":
            manifests.append((path, value))

    assert len(manifests) == 2
    root_cells = [item for item in manifests if item[1]["layer"] == "leviathan"]
    project_cells = [item for item in manifests if item[1]["layer"] == "factory"]
    assert len(root_cells) == len(project_cells) == 1

    root_manifest_path, root_manifest = root_cells[0]
    project_manifest_path, project_manifest = project_cells[0]
    assert set(root_manifest) == CELL_KEYS
    assert set(project_manifest) == CELL_KEYS
    assert root_manifest["children"] == ["alpha-project"]
    assert project_manifest["children"] == []
    assert project_manifest["path"].split("/")[-1] == "alpha-project"
    assert project_manifest_path.parent.resolve() == project_directory(
        root, "alpha-project"
    ).resolve()

    project_root = root_manifest_path.parent
    project_directories = sorted(
        path.name
        for path in project_root.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )
    assert root_manifest["children"] == project_directories
    for manifest_path, manifest in manifests:
        lineage_path = manifest_path.with_name("lineage.json")
        assert lineage_path.is_file()
        assert "lineage" not in manifest
        lineage = json.loads(lineage_path.read_text(encoding="utf-8"))
        assert isinstance(lineage, dict)
    assert root_manifest_path.parent == root


def test_rebuild_uses_only_verified_chains_and_marks_corruption(
    projects, tmp_path: Path
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root, "alpha-project")["status"] == "ok"
    assert open_project(agent, root, "beta-project")["status"] == "ok"
    marker = "UNVERIFIED-PAYLOAD-MUST-NOT-BECOME-A-VIEW"
    before = {path: path.read_bytes() for path in derived_paths(root)}
    corrupt_genesis_title(root, "beta-project", marker)

    result = perform(agent, "board", root=root)

    rendered = "\n".join(
        path.read_text(encoding="utf-8") for path in derived_paths(root)
    )
    assert marker not in rendered
    assert str(root.resolve()) not in rendered
    if result["status"] == "error":
        after = {
            path: path.read_bytes() for path in derived_paths(root)
        }
        if after == before:
            return
        assert re.search(
            r"corrupt|could not verify|verification failed|hash mismatch",
            rendered,
            re.IGNORECASE,
        )

    index = json.loads((root / "index.json").read_text(encoding="utf-8"))
    alpha = next(row for row in index["projects"] if row["project"] == "alpha-project")
    assert alpha["state"] != "corrupt"
    beta = next(
        (row for row in index["projects"] if row["project"] == "beta-project"),
        None,
    )
    assert (
        beta is None
        or beta["state"] == "corrupt"
        or beta.get("verified") is False
    )


def test_derived_views_sanitize_absolute_user_paths(
    projects, tmp_path: Path
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root)["status"] == "ok"
    current_actor = actor()
    user_path = "/Users/example/private/work/review.md"
    windows_path = r"C:\Users\Example\private\review.md"
    assert perform(
        agent,
        "punchin",
        root=root,
        project="alpha-project",
        **current_actor,
        location=user_path,
        intent=f"Review {windows_path}",
        role="reviewer",
    )["status"] == "ok"
    assert perform(
        agent,
        "status",
        root=root,
        project="alpha-project",
        **current_actor,
        location=user_path,
        status="reviewing local evidence",
        artifacts=[],
        blockers=[f"Compare {user_path} with {windows_path}"],
        next_action=f"Continue in {user_path}",
        pct=50,
    )["status"] == "ok"
    perform(agent, "board", root=root)

    views = "\n".join(
        path.read_text(encoding="utf-8") for path in derived_paths(root)
    )
    assert user_path not in views
    assert windows_path not in views
    assert str(tmp_path.resolve()) not in views
    assert ABSOLUTE_USER_PATH.search(views) is None
    assert "local-private://" in views or "[local-private-path]" in views


def test_stale_thresholds_distinguish_active_idle_and_finished_projects(
    projects, tmp_path: Path
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()

    assert open_project(agent, root, "idle-project")["status"] == "ok"
    idle_head = frames(root, "idle-project")[-1]
    idle_time = parse_utc(idle_head["utc"])
    assert fold_at(
        projects,
        root,
        "idle-project",
        idle_time + timedelta(hours=24) - timedelta(milliseconds=1),
    )["stale"] is False
    assert fold_at(
        projects,
        root,
        "idle-project",
        idle_time + timedelta(hours=24),
    )["stale"] is True

    assert open_project(agent, root, "active-project")["status"] == "ok"
    current_actor = actor("active-agent")
    assert punch_in(agent, root, "active-project", current_actor)["status"] == "ok"
    active_time = parse_utc(frames(root, "active-project")[-1]["utc"])
    assert fold_at(
        projects,
        root,
        "active-project",
        active_time + timedelta(hours=4) - timedelta(milliseconds=1),
    )["stale"] is False
    assert fold_at(
        projects,
        root,
        "active-project",
        active_time + timedelta(hours=4),
    )["stale"] is True

    assert perform(
        agent,
        "punchout",
        root=root,
        project="active-project",
        **current_actor,
        outcome="done",
        receipts=[],
        summary="Generic fixture completed.",
    )["status"] == "ok"
    done_time = parse_utc(frames(root, "active-project")[-1]["utc"])
    assert fold_at(
        projects,
        root,
        "active-project",
        done_time + timedelta(days=7),
    )["stale"] is False


def test_artifact_receipts_hash_content_without_copying_artifact_bodies(
    projects, tmp_path: Path
) -> None:
    root = tmp_path / "control"
    artifact = tmp_path / "outside" / "generic-artifact.bin"
    artifact.parent.mkdir()
    body = (
        b"generic-project-artifact-"
        + hashlib.sha256(b"generic-fixture-body").digest()
    ) * 257
    artifact.write_bytes(body)

    agent = projects.RappProjectsAgent()
    assert open_project(agent, root)["status"] == "ok"
    current_actor = actor()
    assert punch_in(agent, root, "alpha-project", current_actor)["status"] == "ok"
    assert perform(
        agent,
        "status",
        root=root,
        project="alpha-project",
        **current_actor,
        location="project://work",
        status="artifact ready",
        artifacts=[str(artifact)],
        blockers=[],
        next_action="Verify the receipt",
        pct=75,
    )["status"] == "ok"

    status_frame = next(
        frame
        for frame in reversed(frames(root, "alpha-project"))
        if frame_event(frame) == "work.status"
    )
    receipt = status_frame["payload"]["artifacts"][0]
    assert receipt["exists"] is True
    assert receipt["sha256"] == hashlib.sha256(body).hexdigest()
    assert receipt.get("bytes", receipt.get("size")) == len(body)
    assert re.fullmatch(r"local-private://[0-9a-f]{32}", receipt["path"])
    locators = json.loads(
        (
            project_directory(root, "alpha-project")
            / ".receipt-locators.json"
        ).read_text(encoding="utf-8")
    )
    assert locators["paths"][receipt["path"].removeprefix(
        "local-private://"
    )] == str(artifact.resolve())
    project = project_directory(root, "alpha-project")
    assert not any(
        path.is_file() and path.name == artifact.name
        for path in project.rglob("*")
    )
    assert all(
        path.read_bytes() != body
        for path in project.rglob("*")
        if path.is_file()
    )

    verified = perform(
        agent,
        "verify",
        root=root,
        project="alpha-project",
    )
    assert verified["verdict"] == "pass"

    artifact.write_bytes(body + b"-mutated")
    broken = perform(
        agent,
        "verify",
        root=root,
        project="alpha-project",
    )
    assert broken["status"] == "ok"
    assert broken["verdict"] == "fail"
    assert broken["broken_receipts"] == [receipt]


def test_windows_file_lock_backend_locks_and_unlocks_one_byte(
    projects, tmp_path: Path
) -> None:
    calls: list[tuple[int, int, int]] = []
    fake_msvcrt = SimpleNamespace(
        LK_LOCK=1,
        LK_UNLCK=2,
        locking=lambda descriptor, mode, count: calls.append(
            (descriptor, mode, count)
        ),
    )
    real_import = builtins.__import__

    def windows_import(name, *args, **kwargs):
        if name == "fcntl":
            raise ImportError("fixture selects Windows")
        if name == "msvcrt":
            return fake_msvcrt
        return real_import(name, *args, **kwargs)

    lock_path = tmp_path / "locks" / "append.lock"
    with mock.patch.object(builtins, "__import__", side_effect=windows_import):
        with projects.file_lock(lock_path):
            assert lock_path.read_bytes() == b"\0"

    assert [mode for _, mode, _ in calls] == [
        fake_msvcrt.LK_LOCK,
        fake_msvcrt.LK_UNLCK,
    ]
    assert all(count == 1 for _, _, count in calls)
