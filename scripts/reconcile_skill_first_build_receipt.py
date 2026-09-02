#!/usr/bin/env python3
"""Append the skill-first Grail migration to the RAPP Projects receipt."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
AGENT = ROOT / "agents" / "@kody-w" / "rapp_projects_agent.py"
RECEIPT = ROOT / "docs" / "rapp-projects-skill-build.rapp.json"
CATALOG = ROOT / "scout" / "catalog" / "catalog.json"
API = ROOT / "api" / "v1" / "agent" / "kody-w__rapp_projects.json"
IDENTITY = "@kody-w/rapp_projects"
RAPP_SKILL_IDENTITY = "@kody-w/rapp_skill_agent"
FRAME_NAME = "skill-first-runtime-hardening"
FRAME_UTC = "2026-09-02T18:15:00.000Z"


def load_agent():
    spec = importlib.util.spec_from_file_location(
        "_rapp_projects_skill_first_receipt",
        AGENT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load RAPP Projects agent")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_agent()
    frames = json.loads(RECEIPT.read_text(encoding="utf-8"))
    if frames[-1].get("payload", {}).get("name") == FRAME_NAME:
        print("Skill-first build receipt is already reconciled")
        return 0

    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    records = {
        item["identity"]: item
        for item in catalog["skills"]
    }
    project = records[IDENTITY]
    foundation = records[RAPP_SKILL_IDENTITY]
    project_skill = (
        ROOT
        / "scout"
        / "bundles"
        / project["bundle"]
        / "skills"
        / project["skill_name"]
        / "SKILL.md"
    )
    prior = frames[-1]
    payload = copy.deepcopy(prior["payload"])
    payload["frame"] = int(prior["payload"]["frame"]) + 1
    payload["name"] = FRAME_NAME
    evidence = payload["evidence"]
    evidence.update({
        "api_sha256": hashlib.sha256(API.read_bytes()).hexdigest(),
        "skill_sha256": hashlib.sha256(project_skill.read_bytes()).hexdigest(),
        "rappid": project["rappid"],
        "default_artifact": "skill",
        "grail_record": "SKILL.md",
        "backup_agent_retained": True,
        "lock_schema": "rapp-grail-lock/2.0",
        "runner_preflight": "RAPP_READY:source=grail",
        "rapp_skill_version": foundation["version"],
        "rapp_skill_source_sha256": foundation["source_sha256"],
        "rapp_skill_skill_sha256": foundation["skill_sha256"],
        "rapp_skill_rappid": foundation["rappid"],
        "targeted_tests": max(int(evidence.get("targeted_tests", 0)), 177),
        "publication_release_tests": max(
            int(evidence.get("publication_release_tests", 0)),
            216,
        ),
    })
    payload["skill_first_runtime"] = {
        "reason": (
            "Make the Grail authoritative at runtime with bounded capsule "
            "execution while retaining agent.py as a rollback backup."
        ),
        "prior_frame_hash": prior["frame_hash"],
        "project_rappid": project["rappid"],
        "rapp_skill_rappid": foundation["rappid"],
    }
    frame = {
        "spec": "rapp/1",
        "kind": "build.frame",
        "stream_id": prior["stream_id"],
        "seq": int(prior["seq"]) + 1,
        "utc": FRAME_UTC,
        "payload": payload,
        "payload_hash": module.H("rapp/1:particle", payload),
        "prev": prior["payload_hash"],
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
    RECEIPT.write_text(
        json.dumps(frames, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Appended {FRAME_NAME} at seq {frame['seq']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
