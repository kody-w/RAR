"""Multi-runtime interoperability contract for the generic RAPP Projects agent."""

from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "agents" / "@kody-w" / "rapp_projects_agent.py"
IDENTITY = "@kody-w/rapp_projects"
PROJECT = "shared-runtime-project"


def load_agent():
    basic_dir = ROOT / "agents" / "@rapp"
    sys.path.insert(0, str(basic_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "rapp_projects_interop_agent",
            SOURCE,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(str(basic_dir))

    classes = [
        value
        for value in vars(module).values()
        if (
            isinstance(value, type)
            and value.__module__ == module.__name__
            and value.__name__.lower().endswith("projectsagent")
            and hasattr(value, "perform")
        )
    ]
    assert len(classes) == 1
    return classes[0]()


def decode_result(raw: str, action: str) -> dict:
    result = json.loads(raw)
    assert result["status"] == "ok", result
    if "action" in result:
        assert result["action"] == action
    if "operation" in result:
        assert result["operation"] == action
    return result


def run_source(
    arguments: dict[str, object],
    *,
    stdin: bool = False,
) -> dict:
    command = [sys.executable, str(SOURCE)]
    input_text = None
    if stdin:
        input_text = json.dumps(arguments)
    else:
        command.append(json.dumps(arguments))
    environment = dict(os.environ)
    basic_dir = str(ROOT / "agents" / "@rapp")
    environment["PYTHONPATH"] = os.pathsep.join(
        part for part in (basic_dir, environment.get("PYTHONPATH", "")) if part
    )
    process = subprocess.run(
        command,
        cwd=ROOT,
        env=environment,
        input=input_text,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert process.returncode == 0, process.stderr
    expected = arguments.get("action", arguments.get("operation"))
    return decode_result(process.stdout, str(expected))


def scout_runner() -> tuple[Path, Path] | None:
    catalog_path = ROOT / "scout" / "catalog" / "catalog.json"
    if not catalog_path.is_file():
        return None
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    records = [
        item
        for item in catalog.get("skills", [])
        if item.get("identity") == IDENTITY
    ]
    if not records:
        return None
    [record] = records
    if record["bundle"] == "starter":
        skill_dir = (
            ROOT / "scout" / "starter" / "skills" / record["skill_name"]
        )
    else:
        skill_dir = (
            ROOT
            / "scout"
            / "bundles"
            / record["bundle"]
            / "skills"
            / record["skill_name"]
        )
    runner = skill_dir / "scripts" / "run_agent.py"
    assert runner.is_file()
    return skill_dir, runner


def run_scout_or_source(arguments: dict[str, object]) -> dict:
    projected = scout_runner()
    if projected is None:
        return run_source(arguments)
    skill_dir, runner = projected
    process = subprocess.run(
        [sys.executable, str(runner), json.dumps(arguments)],
        cwd=skill_dir,
        env=dict(os.environ),
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert process.returncode == 0, process.stderr
    expected = arguments.get("action", arguments.get("operation"))
    return decode_result(process.stdout, str(expected))


def read_chain(root: Path) -> list[dict]:
    path = root / PROJECT / "chain.jsonl"
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
    ]


def project_identity(root: Path) -> dict:
    return json.loads(
        (root / PROJECT / "rappid.json").read_text(encoding="utf-8")
    )


def assert_linear_chain(frames: list[dict]) -> None:
    assert [frame["spec"].casefold() for frame in frames] == (
        ["rapp/1"] * len(frames)
    )
    assert [frame["seq"] for frame in frames] == list(range(len(frames)))
    assert len({frame["stream_id"] for frame in frames}) == 1
    assert frames[0]["prev"] is None
    for previous, current in zip(frames, frames[1:]):
        assert current["prev"] == previous["payload_hash"]


def index_record(root: Path) -> dict:
    index = json.loads((root / "index.json").read_text(encoding="utf-8"))
    [record] = [
        item for item in index["projects"] if item["project"] == PROJECT
    ]
    return record


def result_frame_hash(result: dict) -> str:
    if isinstance(result.get("frame_hash"), str):
        return result["frame_hash"]
    if isinstance(result.get("verification_frame_hash"), str):
        return result["verification_frame_hash"]
    frame = result.get("frame")
    assert isinstance(frame, dict) and isinstance(frame.get("frame_hash"), str)
    return frame["frame_hash"]


def authoritative_snapshot(root: Path) -> bytes:
    return (root / PROJECT / "chain.jsonl").read_bytes()


def public_operation_key(agent) -> str:
    properties = agent.metadata["parameters"]["properties"]
    keys = [name for name in ("action", "operation") if name in properties]
    assert len(keys) == 1
    return keys[0]


def test_independent_callers_share_one_append_only_project_chain(tmp_path):
    project_root = tmp_path / "projects"
    alternate_root = tmp_path / "alternate-projects"
    handoff = tmp_path / "handoff.md"
    handoff.write_text(
        "# Runtime handoff\n\nContinue the append-only project chain.\n",
        encoding="utf-8",
    )
    agent = load_agent()
    operation_key = public_operation_key(agent)
    results = []
    identities = []

    results.append(
        decode_result(
            agent.perform(
                **{operation_key: "open"},
                root=str(project_root),
                project=PROJECT,
                title="Shared runtime project",
                goal="Prove interoperable project continuity",
                owner="runtime-a",
                origin="runtime-a",
            ),
            "open",
        )
    )
    identities.append(project_identity(project_root))

    results.append(
        run_source(
            {
                operation_key: "punchin",
                "root": str(project_root),
                "project": PROJECT,
                "agent": "runtime-b",
                "runtime": "runtime-b",
                "session_id": "session-b",
                "location": "workspace-b",
                "intent": "Open the shared work",
                "role": "builder",
                "capabilities": ["append"],
            }
        )
    )
    identities.append(project_identity(project_root))

    results.append(
        run_source(
            {
                operation_key: "status",
                "root": str(project_root),
                "project": PROJECT,
                "agent": "runtime-b",
                "runtime": "runtime-b",
                "session_id": "session-b",
                "capabilities": ["append"],
                "location": "workspace-b",
                "status": "ready for handoff",
                "artifacts": [],
                "blockers": [],
                "next_action": "Transfer control to runtime-c",
                "pct": 60,
                "project_state": "active",
            },
            stdin=True,
        )
    )
    identities.append(project_identity(project_root))

    results.append(
        decode_result(
            agent.perform(
                **{operation_key: "handoff"},
                root=str(project_root),
                project=PROJECT,
                from_agent="runtime-b",
                to_agent="runtime-c",
                doc=str(handoff),
                open_questions=[],
            ),
            "handoff",
        )
    )
    identities.append(project_identity(project_root))
    prefix_snapshot = authoritative_snapshot(project_root)
    prefix_frames = read_chain(project_root)

    results.append(
        run_scout_or_source(
            {
                operation_key: "punchout",
                "root": str(project_root),
                "project": PROJECT,
                "agent": "runtime-c",
                "runtime": "runtime-c",
                "session_id": "session-c",
                "capabilities": ["verify"],
                "outcome": "done",
                "receipts": [],
                "summary": "Runtime-c completed the shared work.",
                "blockers": [],
            }
        )
    )
    identities.append(project_identity(project_root))

    results.append(
        run_source(
            {
                operation_key: "verify",
                "root": str(project_root),
                "project": PROJECT,
            },
            stdin=True,
        )
    )
    identities.append(project_identity(project_root))

    frames = read_chain(project_root)
    assert [frame["kind"] for frame in frames] == [
        "project.genesis",
        "work.punchin",
        "work.status",
        "work.handoff",
        "work.punchout",
        "project.verify",
    ]
    assert_linear_chain(frames)
    assert [result_frame_hash(result) for result in results] == [
        frame["frame_hash"] for frame in frames
    ]
    assert len({identity["rappid"] for identity in identities}) == 1
    assert frames[-1]["stream_id"] in {
        identities[-1]["rappid"],
        identities[-1]["rappid"] + ":project",
    }
    assert results[-1]["verdict"] == "pass"

    final_snapshot = authoritative_snapshot(project_root)
    assert final_snapshot.startswith(prefix_snapshot)
    assert frames[: len(prefix_frames)] == prefix_frames
    assert "runtime-a" in json.dumps(frames[0]["payload"], sort_keys=True)
    assert "runtime-b" in json.dumps(frames[1]["payload"], sort_keys=True)
    assert "runtime-b" in json.dumps(frames[2]["payload"], sort_keys=True)
    assert "runtime-b" in json.dumps(frames[3]["payload"], sort_keys=True)
    assert "runtime-c" in json.dumps(frames[3]["payload"], sort_keys=True)
    assert "runtime-c" in json.dumps(frames[4]["payload"], sort_keys=True)

    board = (project_root / "BOARD.md").read_text(encoding="utf-8")
    catchup = (project_root / "CATCHUP.md").read_text(encoding="utf-8")
    assert PROJECT in board
    assert PROJECT in catchup
    assert frames[-1]["frame_hash"] in catchup
    assert index_record(project_root)["last_frame_hash"] == frames[-1]["frame_hash"]

    main_snapshot = final_snapshot
    isolated = decode_result(
        agent.perform(
            **{operation_key: "open"},
            root=str(alternate_root),
            project=PROJECT,
            title="Alternate root project",
            goal="Remain isolated from the shared runtime root",
            owner="Example team",
            origin="runtime-a",
        ),
        "open",
    )
    alternate_frames = read_chain(alternate_root)
    assert result_frame_hash(isolated) == alternate_frames[0]["frame_hash"]
    assert [frame["kind"] for frame in alternate_frames] == ["project.genesis"]
    assert_linear_chain(alternate_frames)
    assert project_identity(alternate_root)["rappid"] != identities[-1]["rappid"]
    assert alternate_frames[-1]["frame_hash"] != frames[-1]["frame_hash"]
    assert authoritative_snapshot(project_root) == main_snapshot
    assert index_record(alternate_root)["last_frame_hash"] == (
        alternate_frames[-1]["frame_hash"]
    )
