#!/usr/bin/env python3
"""Append an exact reconciliation frame for the RAPP Projects publication."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
AGENT = ROOT / "agents" / "@kody-w" / "rapp_projects_agent.py"
API = ROOT / "api" / "v1" / "agent" / "kody-w__rapp_projects.json"
RECEIPT = ROOT / "docs" / "rapp-projects-skill-build.rapp.json"


def load_agent_module():
    spec = importlib.util.spec_from_file_location(
        "_rapp_projects_receipt_reconcile",
        AGENT,
    )
    if not spec or not spec.loader:
        raise RuntimeError("Unable to load the RAPP Projects agent")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def utc() -> str:
    now = datetime.now(timezone.utc)
    return now.strftime("%Y-%m-%dT%H:%M:%S.") + f"{now.microsecond // 1000:03d}Z"


def main() -> int:
    module = load_agent_module()
    frames = json.loads(RECEIPT.read_text(encoding="utf-8"))
    latest = frames[-1]
    current_api = hashlib.sha256(API.read_bytes()).hexdigest()
    recorded_api = latest["payload"]["evidence"]["api_sha256"]
    if current_api == recorded_api:
        print("RAPP Projects build receipt already matches the publication")
        return 0

    payload = copy.deepcopy(latest["payload"])
    payload["frame"] = int(latest["payload"]["frame"]) + 1
    payload["name"] = "publication-reconciliation"
    payload["evidence"]["api_sha256"] = current_api
    payload["reconciliation"] = {
        "reason": (
            "Admission generates HOLO cards before the API projection; bind "
            "the receipt to that final publication shape."
        ),
        "prior_api_sha256": recorded_api,
        "prior_frame_hash": latest["frame_hash"],
    }
    frame = {
        "spec": "rapp/1",
        "kind": "build.frame",
        "stream_id": latest["stream_id"],
        "seq": int(latest["seq"]) + 1,
        "utc": utc(),
        "payload": payload,
        "payload_hash": module.H("rapp/1:particle", payload),
        "prev": latest["payload_hash"],
        "prev_wave": None,
        "sig": None,
    }
    preimage = {
        key: value
        for key, value in frame.items()
        if key not in {"frame_hash", "sig"}
    }
    frame["frame_hash"] = module.H("rapp/1:wave", preimage)
    frames.append(frame)

    temporary = RECEIPT.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(frames, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(RECEIPT)
    print(
        "Appended RAPP Projects publication reconciliation: "
        f"{recorded_api} -> {current_api}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
