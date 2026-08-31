from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import sys
import types
import uuid
from copy import deepcopy
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
AGENT_PATH = ROOT / "agents" / "@kody-w" / "rapp_projects_agent.py"
FRAME_KEYS = {
    "spec",
    "kind",
    "stream_id",
    "seq",
    "utc",
    "payload",
    "payload_hash",
    "frame_hash",
    "prev",
    "prev_wave",
    "sig",
}
UTC0 = "2026-08-31T00:00:00.000Z"
UTC1 = "2026-08-31T00:00:01.000Z"


class BasicAgent:
    def __init__(self, name=None, metadata=None):
        self.name = name
        self.metadata = metadata or {}


def _load_agent(monkeypatch: pytest.MonkeyPatch, root: Path):
    agents = types.ModuleType("agents")
    basic = types.ModuleType("agents.basic_agent")
    basic.BasicAgent = BasicAgent
    agents.basic_agent = basic
    monkeypatch.setitem(sys.modules, "agents", agents)
    monkeypatch.setitem(sys.modules, "agents.basic_agent", basic)
    monkeypatch.setenv("RAPP_PROJECTS_ROOT", str(root))
    spec = importlib.util.spec_from_file_location(
        f"rapp_projects_rapp1_test_{uuid.uuid4().hex}",
        AGENT_PATH,
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def module(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    return _load_agent(monkeypatch, tmp_path / "project-control")


def _canonical_bytes(module, value) -> bytes:
    return module.canonical(value).encode("utf-8")


def _independent_hash(module, space: str, value) -> str:
    return hashlib.sha256(
        space.encode("ascii") + b"\n" + _canonical_bytes(module, value)
    ).hexdigest()


def _stream(module, slug: str = "alpha") -> str:
    return module.project_stream_id(
        module.mint_rappid(slug, owner="example")
    )


def _genesis_payload(project: str = "alpha") -> dict:
    return {
        "project": project,
        "title": "Alpha",
        "goal": "Prove a generic RAPP project chain",
        "owner": "example",
        "origin": "test",
        "visibility": "local-private",
    }


def _status_payload(project: str = "alpha") -> dict:
    return {
        "project": project,
        "agent": "agent-a",
        "location": "workspace/project",
        "status": "working",
        "artifacts": [],
        "blockers": [],
        "next_action": "continue",
        "pct": 50,
    }


def _frame(
    module,
    *,
    stream_id: str,
    kind: str = "project.genesis",
    seq: int = 0,
    utc: str = UTC0,
    payload: dict | None = None,
    prev: str | None = None,
):
    if payload is None:
        payload = (
            _genesis_payload()
            if kind == "project.genesis"
            else _status_payload()
        )
    return module.build_frame(
        kind,
        stream_id,
        seq,
        payload,
        prev,
        utc_value=utc,
    )


def _rehash(module, frame: dict) -> dict:
    changed = deepcopy(frame)
    preimage = {
        key: value
        for key, value in changed.items()
        if key not in {"frame_hash", "sig"}
    }
    changed["frame_hash"] = module.H("rapp/1:wave", preimage)
    return changed


def _perform(adapter, operation: str, **values) -> dict:
    result = json.loads(adapter.perform(operation=operation, **values))
    assert isinstance(result, dict)
    assert result["operation"] == operation
    return result


def test_rappid_is_uuid_based_and_minted_once(
    module,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    values = iter(
        (
            uuid.UUID("11111111-1111-4111-8111-111111111111"),
            uuid.UUID("22222222-2222-4222-8222-222222222222"),
            uuid.UUID("33333333-3333-4333-8333-333333333333"),
            uuid.UUID("44444444-4444-4444-8444-444444444444"),
        )
    )
    monkeypatch.setattr(module.uuid, "uuid4", lambda: next(values))
    first = module.mint_rappid("alpha", owner="example")
    second = module.mint_rappid("alpha", owner="example")

    first_tail = first.rsplit(":", 1)[1]
    assert first == (
        "rappid:@example/alpha:"
        + hashlib.sha256(
            b"rapp/1:rappid\n"
            + uuid.UUID("11111111-1111-4111-8111-111111111111").bytes
        ).hexdigest()
    )
    assert first_tail != second.rsplit(":", 1)[1]
    assert first_tail != hashlib.sha256(b"example/alpha").hexdigest()

    agent = module.RappProjectsAgent()
    opened = _perform(
        agent,
        "open",
        project="mint-once",
        title="Mint Once",
        goal="Keep one project identity",
        owner="example",
        origin="test",
    )
    assert opened["status"] == "ok"
    assert opened["created"] is True
    identity_path = (
        Path(os.environ["RAPP_PROJECTS_ROOT"])
        / "mint-once"
        / "rappid.json"
    )
    stored = json.loads(identity_path.read_text(encoding="utf-8"))["rappid"]
    repeated = _perform(
        agent,
        "open",
        project="mint-once",
        title="Mint Once",
        goal="Keep one project identity",
        owner="example",
        origin="test",
    )
    assert repeated["status"] == "ok"
    assert repeated["created"] is False
    assert repeated["rappid"] == stored
    assert json.loads(identity_path.read_text(encoding="utf-8"))["rappid"] == stored


def test_frame_has_exact_keys_and_normative_domain_separated_hashes(module) -> None:
    stream_id = _stream(module)
    payload = _genesis_payload()
    frame = _frame(module, stream_id=stream_id, payload=payload)

    assert set(frame) == FRAME_KEYS
    assert frame["payload_hash"] == _independent_hash(
        module, "rapp/1:particle", payload
    )
    wave_preimage = {
        key: value
        for key, value in frame.items()
        if key not in {"frame_hash", "sig"}
    }
    assert frame["frame_hash"] == _independent_hash(
        module, "rapp/1:wave", wave_preimage
    )
    assert frame["payload_hash"] != frame["frame_hash"]

    signed = {**frame, "sig": "header.payload.signature"}
    signed_preimage = {
        key: value
        for key, value in signed.items()
        if key not in {"frame_hash", "sig"}
    }
    assert _independent_hash(
        module, "rapp/1:wave", signed_preimage
    ) == frame["frame_hash"]


def test_jcs_numbers_round_trip_or_are_refused(module) -> None:
    assert module.canonical(
        {"n": [0.1, -0.0, 9007199254740992]}
    ) == '{"n":[0.1,0,9007199254740992]}'
    assert module._strict_loads(b'{"n":0.1}')["n"] == 0.1
    with pytest.raises(Exception, match="binary64 round-trip"):
        module._strict_loads(b'{"n":9007199254740993}')
    with pytest.raises(Exception, match="binary64|I-JSON"):
        module._strict_loads(b'{"n":1e999}')


def test_jcs_strings_use_utf16_order_without_normalization(module) -> None:
    assert module.canonical({"\ue000": 2, "😀": 1}) == '{"😀":1,"\ue000":2}'
    composed = {"text": "é"}
    decomposed = {"text": "e\u0301"}
    assert module.canonical(composed) != module.canonical(decomposed)
    assert module.H("rapp/1:particle", composed) != module.H(
        "rapp/1:particle", decomposed
    )
    with pytest.raises(Exception, match="surrogate"):
        module.canonical({"text": "\ud800"})
    with pytest.raises(Exception, match="duplicate JSON member: a"):
        module._strict_loads(b'{"a":1,"a":2}')


def test_jcs_enforces_depth_and_one_mib_size(module) -> None:
    depth_64: object = 0
    for _ in range(64):
        depth_64 = [depth_64]
    module.canonical(depth_64)

    with pytest.raises(Exception, match="nesting exceeds the depth limit"):
        module.canonical([depth_64])

    exactly_one_mib = "x" * ((1 << 20) - 2)
    assert len(_canonical_bytes(module, exactly_one_mib)) == 1 << 20
    with pytest.raises(Exception, match="canonical JSON exceeds 1 MiB"):
        module.canonical(exactly_one_mib + "x")


def test_chain_is_contiguous_and_utc_is_monotonic(module) -> None:
    stream_id = _stream(module)
    first = _frame(module, stream_id=stream_id)
    second = _frame(
        module,
        stream_id=stream_id,
        kind="work.status",
        seq=1,
        utc=UTC1,
        prev=first["payload_hash"],
    )
    assert module.verify_frame(first, stream_id=stream_id) == (True, None)
    assert module.verify_frame(
        second, head=first, stream_id=stream_id
    ) == (True, None)

    wrong_seq = _rehash(module, {**second, "seq": 2})
    assert module.verify_frame(
        wrong_seq, head=first, stream_id=stream_id
    ) == (False, "RAPP/1 step 4: sequence is not contiguous")

    wrong_prev = _rehash(module, {**second, "prev": "0" * 64})
    assert module.verify_frame(
        wrong_prev, head=first, stream_id=stream_id
    ) == (False, "RAPP/1 step 4: previous particle does not match")

    utc_regression = _rehash(
        module, {**second, "utc": "2025-01-01T00:00:00.000Z"}
    )
    assert module.verify_frame(
        utc_regression, head=first, stream_id=stream_id
    ) == (False, "RAPP/1 step 4: utc moved backwards")


def test_stream_binding_kind_wire_and_tampering_reasons_are_exact(module) -> None:
    stream_id = _stream(module)
    frame = _frame(module, stream_id=stream_id)

    assert module.verify_frame(
        frame, stream_id=_stream(module, "beta")
    ) == (False, "RAPP/1 step 1a: frame belongs to another stream")

    invalid_kind = {**frame, "kind": "not_a_kind"}
    assert module.verify_frame(
        invalid_kind, stream_id=stream_id
    ) == (False, "RAPP/1 step 1: kind is unregistered")

    off_swarm_wave = _rehash(module, {**frame, "prev_wave": "1" * 64})
    assert module.verify_frame(
        off_swarm_wave, stream_id=stream_id
    ) == (False, "RAPP/1 step 5: prev_wave must be null off swarm")

    payload_tamper = deepcopy(frame)
    payload_tamper["payload"]["goal"] = "Changed"
    assert module.verify_frame(
        payload_tamper, stream_id=stream_id
    ) == (False, "RAPP/1 step 2: payload hash mismatch")

    frame_tamper = {**frame, "frame_hash": "f" * 64}
    assert module.verify_frame(
        frame_tamper, stream_id=stream_id
    ) == (False, "RAPP/1 step 3: frame hash mismatch")


def test_shape_mutations_report_the_exact_reason(module) -> None:
    stream_id = _stream(module)
    frame = _frame(module, stream_id=stream_id)
    mutations = (
        {key: value for key, value in frame.items() if key != "sig"},
        {**frame, "extra": None},
    )
    for changed in mutations:
        assert module.verify_frame(
            changed, stream_id=stream_id
        ) == (False, "RAPP/1 step 1: frame must have exactly eleven keys")


def test_corrupt_history_refuses_append(module) -> None:
    agent = module.RappProjectsAgent()
    assert _perform(
        agent,
        "open",
        project="closed-chain",
        title="Closed Chain",
        goal="Refuse append after corruption",
        owner="example",
        origin="test",
    )["status"] == "ok"
    assert _perform(
        agent,
        "punchin",
        project="closed-chain",
        agent="agent-a",
        runtime="runtime-a",
        session_id="session-a",
        capabilities=["files", "tests"],
        location="workspace/project",
        intent="test corruption",
        role="builder",
    )["status"] == "ok"

    chain_path = (
        Path(os.environ["RAPP_PROJECTS_ROOT"])
        / "closed-chain"
        / "chain.jsonl"
    )
    records = chain_path.read_text(encoding="utf-8").splitlines()
    corrupted = json.loads(records[-1])
    corrupted["payload"]["intent"] = "tampered"
    records[-1] = module.canonical(corrupted)
    chain_path.write_text("\n".join(records) + "\n", encoding="utf-8")
    count_before = len(records)

    refused = _perform(
        agent,
        "status",
        project="closed-chain",
        agent="agent-a",
        location="workspace/project",
        status="working",
        artifacts=[],
        blockers=[],
        next_action="continue",
        pct=50,
    )
    assert refused == {
        "status": "error",
        "operation": "status",
        "error": {
            "code": "chain-verification",
            "message": (
                "chain line 2 failed: "
                "RAPP/1 step 2: payload hash mismatch"
            ),
        },
    }
    assert len(chain_path.read_text(encoding="utf-8").splitlines()) == count_before


def test_complete_open_punchin_status_handoff_punchout_verify_chain(
    module,
    tmp_path: Path,
) -> None:
    agent = module.RappProjectsAgent()
    handoff = tmp_path / "handoff.md"
    handoff.write_text("# Handoff\n\nContinue the generic test.\n", encoding="utf-8")

    assert _perform(
        agent,
        "open",
        project="portable",
        title="Portable",
        goal="Move work between generic runtimes",
        owner="example",
        origin="test",
    )["status"] == "ok"
    assert _perform(
        agent,
        "punchin",
        project="portable",
        agent="agent-a",
        runtime="runtime-a",
        session_id="session-a",
        capabilities=["files", "tests"],
        location="workspace/project",
        intent="build",
        role="builder",
    )["status"] == "ok"
    assert _perform(
        agent,
        "status",
        project="portable",
        agent="agent-a",
        location="workspace/project",
        status="working",
        artifacts=[],
        blockers=[],
        next_action="handoff",
        pct=60,
    )["status"] == "ok"
    assert _perform(
        agent,
        "handoff",
        project="portable",
        from_agent="agent-a",
        to_agent="agent-b",
        doc=str(handoff),
        open_questions=[],
    )["status"] == "ok"
    assert _perform(
        agent,
        "punchout",
        project="portable",
        agent="agent-b",
        outcome="done",
        receipts=[],
        summary="Complete",
        blockers=[],
    )["status"] == "ok"
    verified = _perform(agent, "verify", project="portable")
    assert verified["status"] == "ok"
    assert verified["verdict"] == "pass"
    assert verified["verification_frame_hash"]

    chain_path = (
        Path(os.environ["RAPP_PROJECTS_ROOT"])
        / "portable"
        / "chain.jsonl"
    )
    frames = [
        json.loads(line)
        for line in chain_path.read_text(encoding="utf-8").splitlines()
    ]
    assert [frame["seq"] for frame in frames] == list(range(len(frames)))
    assert [frame["kind"] for frame in frames] == [
        "project.genesis",
        "work.punchin",
        "work.status",
        "work.handoff",
        "work.punchout",
        "project.verify",
    ]
    assert all(set(frame) == FRAME_KEYS for frame in frames)
    assert all(frame["prev_wave"] is None for frame in frames)
    for previous, current in zip(frames, frames[1:]):
        assert current["prev"] == previous["payload_hash"]
        assert current["utc"] >= previous["utc"]
