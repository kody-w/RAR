#!/usr/bin/env python3
"""Append a dependency-reconciliation frame to the RAPP Projects publication receipt.

The receipt binds the rapp_skill foundation (version, source sha256, SKILL.md sha256) that the
RAPP Projects publication was proven against. When that foundation moves (a new rapp_skill
version), the chain is advanced by one frame that records the new binding and names the old
one. History is never rewritten: the ten build frames and the publication-reconciliation frame
stay byte-identical, and every later frame links to the one before it.

Re-runnable: when the tip already binds the catalog's rapp_skill record, nothing is written.
"""

from __future__ import annotations

import copy
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from reconcile_rapp_projects_build_receipt import (  # noqa: E402
    RECEIPT,
    load_agent_module,
    validate_prefix,
    validate_reconciliation,
)

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "scout" / "catalog" / "catalog.json"
FOUNDATION = "@kody-w/rapp_skill_agent"
DEPENDENCY_FRAME = "dependency-reconciliation"
DEPENDENCY_REASON = (
    "The rapp_skill foundation this publication was proven against moved; "
    "bind the receipt to the version the catalog publishes now."
)


def catalog_binding() -> dict:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    matches = [
        item for item in catalog.get("skills", []) if item.get("identity") == FOUNDATION
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one catalog record for {FOUNDATION}")
    record = matches[0]
    return {
        "rapp_skill_version": record["version"],
        "rapp_skill_source_sha256": record["source_sha256"],
        "rapp_skill_skill_sha256": record["skill_sha256"],
    }


def tip_binding(frame: dict) -> dict:
    evidence = frame["payload"]["evidence"]
    return {key: evidence[key] for key in (
        "rapp_skill_version",
        "rapp_skill_source_sha256",
        "rapp_skill_skill_sha256",
    )}


def validate_dependency_frame(module, previous: dict, frame: dict) -> None:
    payload = frame.get("payload", {})
    if payload.get("name") != DEPENDENCY_FRAME:
        raise RuntimeError("A frame after the publication reconciliation must be a dependency reconciliation")
    if frame.get("seq") != int(previous["seq"]) + 1 or payload.get("frame") != int(previous["payload"]["frame"]) + 1:
        raise RuntimeError("The dependency frame does not continue the sequence")
    if frame.get("prev") != previous["payload_hash"]:
        raise RuntimeError("The dependency frame does not extend the prior tip")
    expected = copy.deepcopy(previous["payload"])
    expected["frame"] = payload.get("frame")
    expected["name"] = DEPENDENCY_FRAME
    expected["evidence"].update(tip_binding(frame))
    expected["reconciliation"] = {
        "reason": DEPENDENCY_REASON,
        "prior_frame_hash": previous["frame_hash"],
        "prior_rapp_skill_version": previous["payload"]["evidence"]["rapp_skill_version"],
        "prior_rapp_skill_source_sha256": previous["payload"]["evidence"]["rapp_skill_source_sha256"],
        "prior_rapp_skill_skill_sha256": previous["payload"]["evidence"]["rapp_skill_skill_sha256"],
    }
    if payload != expected:
        raise RuntimeError("The dependency frame changes more than the rapp_skill binding")
    if frame.get("payload_hash") != module.H("rapp/1:particle", payload):
        raise RuntimeError("The dependency frame payload hash is invalid")
    preimage = {k: v for k, v in frame.items() if k not in {"frame_hash", "sig"}}
    if frame.get("frame_hash") != module.H("rapp/1:wave", preimage):
        raise RuntimeError("The dependency frame hash is invalid")


def validate_chain(module, frames: list[dict]) -> dict:
    """Validate the whole receipt and return its tip frame."""
    prior = validate_prefix(frames)
    if len(frames) < 11:
        raise RuntimeError("The publication reconciliation frame is missing; run reconcile_rapp_projects_build_receipt.py first")
    validate_reconciliation(module, prior, frames[10])
    for index in range(11, len(frames)):
        validate_dependency_frame(module, frames[index - 1], frames[index])
    return frames[-1]


def main() -> int:
    module = load_agent_module()
    frames = json.loads(RECEIPT.read_text(encoding="utf-8"))
    tip = validate_chain(module, frames)
    binding = catalog_binding()
    if tip_binding(tip) == binding:
        print(f"RAPP Projects receipt already binds rapp_skill {binding['rapp_skill_version']}")
        return 0

    payload = copy.deepcopy(tip["payload"])
    payload["frame"] = int(tip["payload"]["frame"]) + 1
    payload["name"] = DEPENDENCY_FRAME
    payload["evidence"].update(binding)
    payload["reconciliation"] = {
        "reason": DEPENDENCY_REASON,
        "prior_frame_hash": tip["frame_hash"],
        "prior_rapp_skill_version": tip["payload"]["evidence"]["rapp_skill_version"],
        "prior_rapp_skill_source_sha256": tip["payload"]["evidence"]["rapp_skill_source_sha256"],
        "prior_rapp_skill_skill_sha256": tip["payload"]["evidence"]["rapp_skill_skill_sha256"],
    }
    now = datetime.now(timezone.utc)
    frame = {
        "spec": "rapp/1",
        "kind": "build.frame",
        "stream_id": tip["stream_id"],
        "seq": int(tip["seq"]) + 1,
        "utc": now.strftime("%Y-%m-%dT%H:%M:%S.") + f"{now.microsecond // 1000:03d}Z",
        "payload": payload,
        "payload_hash": module.H("rapp/1:particle", payload),
        "prev": tip["payload_hash"],
        "prev_wave": None,
        "sig": None,
    }
    preimage = {k: v for k, v in frame.items() if k not in {"frame_hash", "sig"}}
    frame["frame_hash"] = module.H("rapp/1:wave", preimage)
    validate_dependency_frame(module, tip, frame)
    frames.append(frame)

    temporary = RECEIPT.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(frames, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(RECEIPT)
    print(
        "Appended RAPP Projects dependency reconciliation: rapp_skill "
        f"{tip['payload']['evidence']['rapp_skill_version']} -> {binding['rapp_skill_version']} "
        f"(frame {frame['seq']}, {frame['frame_hash'][:12]})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
