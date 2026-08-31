"""Storage acceptance tests for the generic RAPP Projects agent.

Every fixture is synthetic. The tests always select a temporary authority and
never inspect or mutate the user's real project store.
"""

from __future__ import annotations

import builtins
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
import hashlib
import importlib.util
import inspect
import json
import multiprocessing
import os
from pathlib import Path
import re
import stat
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


def process_status(root: str, index: int) -> dict:
    os.environ["RAPP_PROJECTS_OWNER"] = "example"
    module = load_agent(f"rapp_projects_process_writer_{os.getpid()}_{index}")
    return json.loads(
        module.RappProjectsAgent().perform(
            operation="status",
            root=root,
            project="alpha-project",
            agent=f"process-{index}",
            location=f"project://process/{index}",
            status=f"process-update-{index}",
            artifacts=[],
            blockers=[],
            next_action=f"Continue after process {index}",
            pct=index,
        )
    )


def process_reads(root: str, iterations: int) -> list[str]:
    os.environ["RAPP_PROJECTS_OWNER"] = "example"
    module = load_agent(f"rapp_projects_process_reader_{os.getpid()}")
    failures = []
    for _ in range(iterations):
        try:
            module.load_chain("alpha-project", root)
        except Exception as exc:
            failures.append(str(exc))
    return failures


def crash_after_project_rename(root: str) -> None:
    os.environ["RAPP_PROJECTS_OWNER"] = "example"
    module = load_agent(f"rapp_projects_crash_{os.getpid()}")

    def terminate_before_manifest(*_args, **_kwargs):
        os._exit(77)

    module._write_root_children = terminate_before_manifest
    module.RappProjectsAgent().perform(
        operation="open",
        root=root,
        project="crash-project",
        title="Crash project",
        goal="Prove journal recovery",
        owner="example",
        origin="process-death fixture",
    )
    os._exit(78)


def crash_after_chain_replace(root: str) -> None:
    os.environ["RAPP_PROJECTS_OWNER"] = "example"
    module = load_agent(f"rapp_projects_append_crash_{os.getpid()}")
    original = module._atomic_json

    def terminate_before_head(path, value, **kwargs):
        if Path(path).name == "head.json":
            os._exit(79)
        return original(path, value, **kwargs)

    module._atomic_json = terminate_before_head
    module.RappProjectsAgent().perform(
        operation="status",
        root=root,
        project="alpha-project",
        agent="crash-runtime",
        location="project://work",
        status="committed before process death",
        artifacts=[],
        blockers=[],
        next_action="Recover the head",
        pct=50,
    )
    os._exit(80)


def crash_during_root_initialization(root: str) -> None:
    os.environ["RAPP_PROJECTS_OWNER"] = "example"
    module = load_agent(f"rapp_projects_root_crash_{os.getpid()}")
    original = module._atomic_json

    def terminate_before_identity(path, value, **kwargs):
        if Path(path).name == "rappid.json":
            os._exit(81)
        return original(path, value, **kwargs)

    module._atomic_json = terminate_before_identity
    module.ensure_root(root, identity_owner="example")
    os._exit(82)


def crash_after_import_rename(root: str, egg: str) -> None:
    os.environ["RAPP_PROJECTS_OWNER"] = "example"
    module = load_agent(f"rapp_projects_import_crash_{os.getpid()}")

    def terminate_before_manifest(*_args, **_kwargs):
        os._exit(83)

    module._write_root_children = terminate_before_manifest
    module.RappProjectsAgent().perform(
        operation="import",
        root=root,
        egg=egg,
    )
    os._exit(84)


def crash_before_fast_forward_chain(root: str, egg: str) -> None:
    os.environ["RAPP_PROJECTS_OWNER"] = "example"
    module = load_agent(f"rapp_projects_fast_forward_crash_{os.getpid()}")
    original = module._atomic_bytes

    def terminate_before_chain(path, data):
        if Path(path).name == "chain.jsonl":
            os._exit(85)
        return original(path, data)

    module._atomic_bytes = terminate_before_chain
    module.RappProjectsAgent().perform(
        operation="import",
        root=root,
        egg=egg,
    )
    os._exit(86)


@pytest.fixture
def projects(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    monkeypatch.setenv("RAPP_PROJECTS_ROOT", str(tmp_path / "configured-root"))
    monkeypatch.setenv("RAPP_PROJECTS_OWNER", "example")
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


def test_multiprocess_readers_never_mix_chain_and_head_snapshots(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root)["status"] == "ok"

    with ProcessPoolExecutor(max_workers=5) as executor:
        reader = executor.submit(process_reads, str(root), 80)
        writers = [
            executor.submit(process_status, str(root), index)
            for index in range(1, 9)
        ]
        results = [future.result(timeout=60) for future in writers]
        failures = reader.result(timeout=60)

    assert all(result["status"] == "ok" for result in results)
    assert failures == []
    project_frames = frames(root, "alpha-project")
    assert [frame["seq"] for frame in project_frames] == list(
        range(len(project_frames))
    )


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


def test_rejected_root_keeps_permissions_and_symlink_target_untouched(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "unowned"
    root.mkdir(mode=0o755)
    marker = root / "foreign.txt"
    marker.write_text("foreign data\n", encoding="utf-8")
    root.chmod(0o755)
    before_mode = stat.S_IMODE(root.stat().st_mode)

    refused = perform(projects.RappProjectsAgent(), "board", root=root)
    assert refused["status"] == "error"
    assert stat.S_IMODE(root.stat().st_mode) == before_mode
    assert marker.read_text(encoding="utf-8") == "foreign data\n"

    target = tmp_path / "target"
    target.mkdir(mode=0o755)
    target.chmod(0o755)
    symlink = tmp_path / "root-link"
    try:
        symlink.symlink_to(target, target_is_directory=True)
    except OSError:
        return
    linked = perform(projects.RappProjectsAgent(), "board", root=symlink)
    assert linked["status"] == "error"
    assert stat.S_IMODE(target.stat().st_mode) == 0o755


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


def test_trusted_chain_digest_detects_interior_history_rewrite(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root)["status"] == "ok"
    for index in (1, 2):
        assert perform(
            agent,
            "status",
            root=root,
            project="alpha-project",
            **actor(),
            location="project://work",
            status=f"status-{index}",
            artifacts=[],
            blockers=[],
            next_action=f"Continue {index}",
            pct=index * 20,
        )["status"] == "ok"
    assert perform(
        agent,
        "verify",
        root=root,
        project="alpha-project",
    )["verdict"] == "pass"

    chain_path = root / "alpha-project" / "chain.jsonl"
    project_frames = frames(root, "alpha-project")
    trusted_head = json.loads(
        (root / "alpha-project" / "head.json").read_text(encoding="utf-8")
    )
    project_frames[0]["payload"]["title"] = "rewritten history"
    project_frames[0]["payload_hash"] = projects.H(
        "rapp/1:particle",
        project_frames[0]["payload"],
    )
    project_frames[0]["frame_hash"] = projects.H(
        "rapp/1:wave",
        {
            key: value
            for key, value in project_frames[0].items()
            if key not in {"frame_hash", "sig"}
        },
    )
    project_frames[1]["prev"] = project_frames[0]["payload_hash"]
    project_frames[1]["frame_hash"] = projects.H(
        "rapp/1:wave",
        {
            key: value
            for key, value in project_frames[1].items()
            if key not in {"frame_hash", "sig"}
        },
    )
    assert project_frames[-1]["frame_hash"] == trusted_head["frame_hash"]
    chain_path.write_text(
        "".join(
            projects.canonical(frame) + "\n"
            for frame in project_frames
        ),
        encoding="utf-8",
    )

    with pytest.raises(
        projects.ChainVerificationError,
        match="history differs beneath the trusted head",
    ):
        projects.load_chain("alpha-project", root)


def test_legacy_v1_head_migrates_under_lock_without_rewriting_history(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root)["status"] == "ok"
    assert perform(
        agent,
        "status",
        root=root,
        project="alpha-project",
        **actor(),
        location="project://work",
        status="ready for head migration",
        artifacts=[],
        blockers=[],
        next_action="Upgrade trusted metadata",
        pct=40,
    )["status"] == "ok"
    chain_path = root / "alpha-project" / "chain.jsonl"
    identity_path = root / "alpha-project" / "rappid.json"
    chain_before = chain_path.read_bytes()
    identity_before = identity_path.read_bytes()
    project_frames = frames(root, "alpha-project")
    head_path = root / "alpha-project" / "head.json"
    projects._atomic_json(
        head_path,
        {
            "schema": projects.LEGACY_HEAD_SCHEMA,
            "stream_id": project_frames[-1]["stream_id"],
            "seq": project_frames[-1]["seq"],
            "frame_hash": project_frames[-1]["frame_hash"],
        },
    )

    loaded = projects.load_chain("alpha-project", root)
    upgraded = json.loads(head_path.read_text(encoding="utf-8"))
    assert loaded == project_frames
    assert upgraded["schema"] == projects.HEAD_SCHEMA
    assert upgraded["chain_hash"] == projects._chain_hash(project_frames)
    assert chain_path.read_bytes() == chain_before
    assert identity_path.read_bytes() == identity_before


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


def test_chain_commit_is_atomic_and_head_failure_is_recoverable(
    projects,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root)["status"] == "ok"
    chain_path = root / "alpha-project" / "chain.jsonl"
    transaction = root / "alpha-project" / ".append-transaction.json"
    original_chain = chain_path.read_bytes()
    original_atomic_bytes = projects._atomic_bytes

    def fail_chain(path, data):
        if Path(path).name == "chain.jsonl":
            raise OSError("injected chain replacement failure")
        return original_atomic_bytes(path, data)

    with monkeypatch.context() as context:
        context.setattr(projects, "_atomic_bytes", fail_chain)
        refused = perform(
            agent,
            "status",
            root=root,
            project="alpha-project",
            **actor(),
            location="project://work",
            status="must not partially append",
            artifacts=[],
            blockers=[],
            next_action="Retry only after a true refusal",
            pct=10,
        )
    assert refused["status"] == "error"
    assert chain_path.read_bytes() == original_chain
    projects.load_chain("alpha-project", root)
    assert not transaction.exists()

    original_atomic_json = projects._atomic_json
    failed = False

    def fail_head_once(path, value, **kwargs):
        nonlocal failed
        if Path(path).name == "head.json" and not failed:
            failed = True
            raise OSError("injected head refresh failure")
        return original_atomic_json(path, value, **kwargs)

    with monkeypatch.context() as context:
        context.setattr(projects, "_atomic_json", fail_head_once)
        committed = perform(
            agent,
            "status",
            root=root,
            project="alpha-project",
            **actor(),
            location="project://work",
            status="committed despite stale head cache",
            artifacts=[],
            blockers=[],
            next_action="Recover the trusted head",
            pct=20,
        )
    assert committed["status"] == "ok"
    assert committed["storage_warnings"][0]["code"] == "head-refresh-failed"
    recovered = projects.load_chain("alpha-project", root)
    assert recovered[-1]["payload"]["status"] == (
        "committed despite stale head cache"
    )
    assert not transaction.exists()
    trusted = json.loads(
        (root / "alpha-project" / "head.json").read_text(encoding="utf-8")
    )
    assert trusted["frame_hash"] == recovered[-1]["frame_hash"]


def test_root_and_project_transactions_recover_after_interrupted_publish(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "control"
    projects.ensure_root(root, identity_owner="example")
    assert open_project(
        projects.RappProjectsAgent(),
        root,
        "beta-project",
    )["status"] == "ok"

    manifest_path = root / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["children"].remove("beta-project")
    projects._atomic_json(manifest_path, manifest)
    projects._atomic_json(
        root / ".project-transaction.json",
        {
            "schema": projects.PROJECT_TRANSACTION_SCHEMA,
            "operation": "create",
            "project": "beta-project",
            "staging": ".staging-beta-project-" + "1" * 32,
        },
    )
    projects.ensure_root(root)
    recovered = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert "beta-project" in recovered["children"]
    assert not (root / ".project-transaction.json").exists()

    staging = root / (".staging-gamma-project-" + "2" * 32)
    staging.mkdir()
    (staging / "partial").write_text("partial\n", encoding="utf-8")
    projects._atomic_json(
        root / ".project-transaction.json",
        {
            "schema": projects.PROJECT_TRANSACTION_SCHEMA,
            "operation": "import",
            "project": "gamma-project",
            "staging": staging.name,
        },
    )
    projects.ensure_root(root)
    assert not staging.exists()
    assert "gamma-project" not in json.loads(
        manifest_path.read_text(encoding="utf-8")
    )["children"]

    new_root = tmp_path / "root-init"
    new_root.mkdir()
    root_rappid = projects.mint_rappid(
        "projects-control",
        owner="example",
    )
    journal = {
        "schema": projects.ROOT_INIT_SCHEMA,
        "identity": projects._identity_record(
            root_rappid,
            "projects-root",
            "projects-control",
        ),
        "lineage": {
            "schema": projects.ROOT_LINEAGE_SCHEMA,
            "parent_rappid": None,
        },
        "manifest": projects._cell_manifest(
            "leviathan",
            "projects",
            [],
        ),
    }
    projects._atomic_json(new_root / ".root-init.json", journal)
    projects._atomic_json(new_root / "rappid.json", journal["identity"])
    projects.ensure_root(new_root)
    assert not (new_root / ".root-init.json").exists()
    assert (new_root / "lineage.json").is_file()
    assert (new_root / "manifest.json").is_file()


def test_process_death_after_project_rename_recovers_on_next_open(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "control"
    projects.ensure_root(root, identity_owner="example")
    process = multiprocessing.get_context("spawn").Process(
        target=crash_after_project_rename,
        args=(str(root),),
    )
    process.start()
    process.join(30)
    assert process.exitcode == 77
    assert (root / ".project-transaction.json").is_file()
    assert (root / "crash-project").is_dir()

    projects.ensure_root(root)
    assert not (root / ".project-transaction.json").exists()
    assert "crash-project" in json.loads(
        (root / "manifest.json").read_text(encoding="utf-8")
    )["children"]
    assert projects.load_chain("crash-project", root)[0]["seq"] == 0


def test_process_death_after_chain_replace_recovers_committed_frame(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "control"
    assert open_project(
        projects.RappProjectsAgent(),
        root,
        "alpha-project",
    )["status"] == "ok"
    chain_path = root / "alpha-project" / "chain.jsonl"
    genesis_chain = chain_path.read_bytes()
    process = multiprocessing.get_context("spawn").Process(
        target=crash_after_chain_replace,
        args=(str(root),),
    )
    process.start()
    process.join(30)
    assert process.exitcode == 79
    transaction = root / "alpha-project" / ".append-transaction.json"
    assert transaction.is_file()
    stale_head = json.loads(
        (root / "alpha-project" / "head.json").read_text(encoding="utf-8")
    )
    assert stale_head["seq"] == 0
    committed_chain = chain_path.read_bytes()
    chain_path.write_bytes(genesis_chain)
    with pytest.raises(
        projects.ChainVerificationError,
        match="rolls back a committed append transaction",
    ):
        projects.load_chain("alpha-project", root)
    chain_path.write_bytes(committed_chain)

    recovered = projects.load_chain("alpha-project", root)
    assert len(recovered) == 2
    assert recovered[-1]["payload"]["status"] == (
        "committed before process death"
    )
    assert not transaction.exists()
    trusted = json.loads(
        (root / "alpha-project" / "head.json").read_text(encoding="utf-8")
    )
    assert trusted["seq"] == 1
    assert trusted["frame_hash"] == recovered[-1]["frame_hash"]


def test_process_death_during_root_initialization_recovers_same_identity(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "control"
    process = multiprocessing.get_context("spawn").Process(
        target=crash_during_root_initialization,
        args=(str(root),),
    )
    process.start()
    process.join(30)
    assert process.exitcode == 81
    journal = json.loads(
        (root / ".root-init.json").read_text(encoding="utf-8")
    )
    expected_rappid = journal["identity"]["rappid"]

    projects.ensure_root(root, identity_owner="different-owner")
    actual_rappid = json.loads(
        (root / "rappid.json").read_text(encoding="utf-8")
    )["rappid"]
    assert actual_rappid == expected_rappid
    assert actual_rappid.startswith("rappid:@example/projects-control:")
    assert not (root / ".root-init.json").exists()


def test_process_death_after_import_rename_recovers_imported_project(
    projects,
    tmp_path: Path,
) -> None:
    source = tmp_path / "source"
    target = tmp_path / "target"
    assert open_project(
        projects.RappProjectsAgent(),
        source,
        "portable-project",
    )["status"] == "ok"
    exported = json.loads(
        projects.RappProjectsAgent().perform(
            operation="export",
            root=str(source),
            project="portable-project",
            owner_approved=True,
        )
    )
    assert exported["status"] == "ok"
    projects.ensure_root(target, identity_owner="example")

    process = multiprocessing.get_context("spawn").Process(
        target=crash_after_import_rename,
        args=(str(target), exported["egg"]),
    )
    process.start()
    process.join(30)
    assert process.exitcode == 83
    assert (target / ".project-transaction.json").is_file()
    assert (target / "portable-project").is_dir()

    projects.ensure_root(target)
    assert not (target / ".project-transaction.json").exists()
    assert projects.load_chain("portable-project", target) == (
        projects.load_chain("portable-project", source)
    )


def test_process_death_before_multiframe_fast_forward_discards_journal(
    projects,
    tmp_path: Path,
) -> None:
    source = tmp_path / "source"
    target = tmp_path / "target"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, source, "portable-project")["status"] == "ok"
    seed = json.loads(
        agent.perform(
            operation="export",
            root=str(source),
            project="portable-project",
            owner_approved=True,
        )
    )
    assert seed["status"] == "ok"
    imported = json.loads(
        agent.perform(
            operation="import",
            root=str(target),
            egg=seed["egg"],
        )
    )
    assert imported["status"] == "ok"
    assert perform(
        agent,
        "punchin",
        root=source,
        project="portable-project",
        **actor(),
        location="project://work",
        intent="Create a multiframe extension",
        role="builder",
    )["status"] == "ok"
    assert perform(
        agent,
        "status",
        root=source,
        project="portable-project",
        **actor(),
        location="project://work",
        status="extension ready",
        artifacts=[],
        blockers=[],
        next_action="Import the extension",
        pct=50,
    )["status"] == "ok"
    updated = json.loads(
        agent.perform(
            operation="export",
            root=str(source),
            project="portable-project",
            owner_approved=True,
        )
    )
    assert updated["status"] == "ok"

    process = multiprocessing.get_context("spawn").Process(
        target=crash_before_fast_forward_chain,
        args=(str(target), updated["egg"]),
    )
    process.start()
    process.join(30)
    assert process.exitcode == 85
    transaction = target / "portable-project" / ".append-transaction.json"
    assert transaction.is_file()

    local = projects.load_chain("portable-project", target)
    assert len(local) == 1
    assert not transaction.exists()
    retried = json.loads(
        agent.perform(
            operation="import",
            root=str(target),
            egg=updated["egg"],
        )
    )
    assert retried["status"] == "ok"
    assert retried["imported_frames"] == 2


def test_public_mutation_helpers_do_not_refresh_after_commit_by_default(
    projects,
) -> None:
    for name in (
        "append_frame",
        "open_project",
        "verify_project",
        "import_project_egg",
    ):
        parameter = inspect.signature(getattr(projects, name)).parameters[
            "refresh"
        ]
        assert parameter.default is False


def test_new_work_invalidates_prior_board_verification(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root)["status"] == "ok"
    assert perform(
        agent,
        "verify",
        root=root,
        project="alpha-project",
    )["verdict"] == "pass"
    verified_board = perform(agent, "board", root=root)
    assert verified_board["projects"][0]["verified"] is True

    updated = perform(
        agent,
        "status",
        root=root,
        project="alpha-project",
        **actor(),
        location="project://work",
        status="new work after verification",
        artifacts=[],
        blockers=[],
        next_action="Verify the new head",
        pct=70,
    )
    assert updated["status"] == "ok"
    unverified_board = perform(agent, "board", root=root)
    assert unverified_board["projects"][0]["verified"] is False

    assert perform(
        agent,
        "verify",
        root=root,
        project="alpha-project",
    )["verdict"] == "pass"
    reverified_board = perform(agent, "board", root=root)
    assert reverified_board["projects"][0]["verified"] is True


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


def test_derived_views_and_api_sanitize_agent_identifier_keys(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root)["status"] == "ok"
    private_agent = "/Users/example/private/runtime"
    result = perform(
        agent,
        "punchin",
        root=root,
        project="alpha-project",
        agent=private_agent,
        runtime="fixture-runtime",
        session_id="fixture-session",
        location="project://work",
        intent="Sanitize agent keys",
        role="builder",
        capabilities=[],
    )
    assert result["status"] == "ok"
    literal_placeholder = "[local-private-path]"
    second = perform(
        agent,
        "punchin",
        root=root,
        project="alpha-project",
        agent=literal_placeholder,
        runtime="fixture-runtime",
        session_id="fixture-session-2",
        location="project://work",
        intent="Exercise redaction collisions",
        role="reviewer",
        capabilities=[],
    )
    assert second["status"] == "ok"

    board = perform(agent, "board", root=root)
    inspected = perform(
        agent,
        "inspect",
        root=root,
        project="alpha-project",
    )
    published = "\n".join(
        path.read_text(encoding="utf-8")
        for path in derived_paths(root)
    ) + json.dumps([board, inspected], sort_keys=True)
    assert private_agent not in published
    assert "[local-private-path]" in published
    assert "[local-private-path]#2" in published
    assert sorted(board["projects"][0]["agents"]) == [
        "[local-private-path]",
        "[local-private-path]#2",
    ]


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


def test_artifact_receipts_refuse_project_managed_files(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "control"
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root)["status"] == "ok"
    assert not projects._valid_receipt_path("project://chain.jsonl")
    assert not projects._valid_receipt_path("project://CHAIN.JSONL")
    assert not projects._valid_receipt_path(
        "projects://alpha-project/head.json"
    )
    assert not projects._valid_receipt_path(
        "projects://alpha-project/Head.Json"
    )
    assert projects._managed_storage_path(
        root / "alpha-project" / "CHAIN.JSONL",
        "alpha-project",
        root,
    )
    chain = root / "alpha-project" / "chain.jsonl"
    before = chain.read_bytes()

    refused = perform(
        agent,
        "status",
        root=root,
        project="alpha-project",
        **actor(),
        location="project://work",
        status="must not receipt authority files",
        artifacts=[str(chain)],
        blockers=[],
        next_action="Use an immutable artifact path",
        pct=30,
    )
    assert refused["status"] == "error"
    assert "managed storage" in refused["error"]["message"]
    assert chain.read_bytes() == before

    target = tmp_path / "external.txt"
    target.write_text("external\n", encoding="utf-8")
    link = tmp_path / "external-link.txt"
    try:
        link.symlink_to(target)
    except OSError:
        return
    symlinked = perform(
        agent,
        "status",
        root=root,
        project="alpha-project",
        **actor(),
        location="project://work",
        status="must not follow a symlink",
        artifacts=[str(link)],
        blockers=[],
        next_action="Use the regular file explicitly",
        pct=35,
    )
    assert symlinked["status"] == "error"
    assert "symbolic link" in symlinked["error"]["message"]
    assert chain.read_bytes() == before


def test_failed_status_does_not_persist_private_receipt_locator(
    projects,
    tmp_path: Path,
) -> None:
    root = tmp_path / "control"
    artifact = tmp_path / "external.txt"
    artifact.write_text("external evidence\n", encoding="utf-8")
    agent = projects.RappProjectsAgent()
    assert open_project(agent, root)["status"] == "ok"
    chain = root / "alpha-project" / "chain.jsonl"
    before = chain.read_bytes()

    refused = perform(
        agent,
        "status",
        root=root,
        project="alpha-project",
        **actor(),
        location="project://work",
        status="invalid progress",
        artifacts=[str(artifact)],
        blockers=[],
        next_action="Fix the request",
        pct=101,
    )
    assert refused["status"] == "error"
    assert chain.read_bytes() == before
    assert not (
        root / "alpha-project" / ".receipt-locators.json"
    ).exists()
    assert not (
        root / "alpha-project" / ".append-transaction.json"
    ).exists()


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
