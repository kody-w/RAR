from __future__ import annotations

from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import apply_agent_batch as batch


def event(number: int, labels=None) -> dict:
    return {
        "issue": {
            "number": number,
            "state": "open",
            "labels": labels
            if labels is not None
            else [{"name": "approved"}, {"name": "agent-submission"}],
        },
        "repository": {"id": 1234},
    }


def test_batch_rejects_unapproved_issue():
    with pytest.raises(batch.BatchMutationError, match="not an approved"):
        batch.apply_batch(
            [event(10, labels=[{"name": "agent-submission"}])],
            approver_id=1,
            approver_login="maintainer",
        )


def test_batch_preflights_every_issue_before_applying(monkeypatch):
    requests = {
        10: {"repository_id": 1234, "agent": "@test/alpha"},
        20: {"repository_id": 1234, "agent": "@test/bravo"},
    }
    applied = []

    def find_staged(current):
        return Path(f"/tmp/{current['issue']['number']}.json")

    def load_request(path):
        return requests[int(path.stem)]

    def apply_request(path, **_kwargs):
        number = int(path.stem)
        applied.append(number)
        return {
            "ok": True,
            "already_applied": False,
            "revision_id": f"revision-{number}",
            "receipt": f"state/receipts/{number}.json",
            "agent": requests[number]["agent"],
            "status": "notarized",
        }

    monkeypatch.setattr(batch.mutation, "find_staged_request", find_staged)
    monkeypatch.setattr(batch.mutation, "_load_json", load_request)
    monkeypatch.setattr(batch.mutation, "apply_request", apply_request)

    result = batch.apply_batch(
        [event(20), event(10)],
        approver_id=1,
        approver_login="maintainer",
    )

    assert applied == [10, 20]
    assert result["issues"] == [10, 20]
    assert result["count"] == 2


def test_batch_rejects_duplicate_agent_mutations(monkeypatch):
    monkeypatch.setattr(
        batch.mutation,
        "find_staged_request",
        lambda current: Path(f"/tmp/{current['issue']['number']}.json"),
    )
    monkeypatch.setattr(
        batch.mutation,
        "_load_json",
        lambda _path: {
            "repository_id": 1234,
            "agent": "@test/same",
        },
    )

    with pytest.raises(batch.BatchMutationError, match="multiple mutations"):
        batch.apply_batch(
            [event(10), event(20)],
            approver_id=1,
            approver_login="maintainer",
        )
