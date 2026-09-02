#!/usr/bin/env python3
"""Append an exact reconciliation frame for the RAPP Projects publication."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
AGENT = ROOT / "agents" / "@kody-w" / "rapp_projects_agent.py"
API = ROOT / "api" / "v1" / "agent" / "kody-w__rapp_projects.json"
CARDS = ROOT / "cards" / "holo_cards.json"
REGISTRY = ROOT / "registry.json"
RECEIPT = ROOT / "docs" / "rapp-projects-skill-build.rapp.json"
IDENTITY = "@kody-w/rapp_projects"
RECONCILIATION_UTC = "2026-09-01T00:25:56.072Z"
EXPECTED_PREFIX_FRAME_HASHES = (
    "e5a4162dbe46f4dbd681ebc1a5d250146bf3a10e47e15a630e7fa2eb19596a7f",
    "2dbc557f3c2bafddf9dbc5d8b2c785b82018638953417aa04614fd72e4c845a6",
    "6618bedca806ba05c6e6aefcf672e0d5a3b77b5b1002e010150eabea7ecfd725",
    "900358c185a0d7d16bea4bf3ea519f64ea213a55e6760ad7710194d625703945",
    "e73d8f73be31cf1c4511b260f8f3aa7c7423055b6ab77261ab341ae0365b70b8",
    "1ed8ac9fcaca0a5fa6aee6f8773515dda373b001cca0269e9b1521d89babd6d7",
    "9c01bb67aa45f71c540b69e70943aa3aeea2761bb033044fb42fcb3f6ce734af",
    "9d5a175f2195978c20541300907a3f8dafe446c54997c0327b615046e4d150df",
    "c96248f3dbca9f0bccad19f904bbfd7acc3da876215797228bc9b21778377a76",
    "60ac594fcd9322961b051b2056546e5ce0198071d45bc124d3c4093a8dc8d44d",
)
EXPECTED_PRIOR_PAYLOAD_HASH = (
    "c8f4aa2f60b2998a81f828ba0079ac3ac827afe3ef8f929b0ece815d7d9282f0"
)
EXPECTED_PRIOR_API_SHA256 = (
    "4df52c49bccbdaa5118ff0ee7e86e40396bb9382b0557584ea26f2dc2d5c8cb4"
)
EXPECTED_POST_HOLO_API_SHA256 = (
    "29d3bef143ebf160237b67532a756a6eb9a29680dd2df8830df3a9bfd918e237"
)
EXPECTED_CARD_SHA256 = (
    "0ea3e4454abc3d21fb1fb042d1cad6aab89e5f40f8910b20694f4153b1987a7b"
)
EXPECTED_RECONCILIATION_PAYLOAD_HASH = (
    "b5e9438fd28e45904c1f5a5c9064ac3df0ebc3189d70938a14330ae53ba92e91"
)
EXPECTED_RECONCILIATION_FRAME_HASH = (
    "efe2d654184b3c7345866120fef7606b947d6ee71bc7efb52821069281b49069"
)


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


def canonical_card_sha256(card: dict) -> str:
    encoded = json.dumps(
        card,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def validate_prefix(frames: list[dict]) -> dict:
    if len(frames) not in {10, 11, 12, 13}:
        raise RuntimeError(
            "Expected the immutable ten-frame receipt, optionally followed by "
            "its one reconciliation frame"
        )
    actual_hashes = tuple(frame.get("frame_hash") for frame in frames[:10])
    if actual_hashes != EXPECTED_PREFIX_FRAME_HASHES:
        raise RuntimeError("Refusing to reconcile rewritten receipt history")
    prior = frames[9]
    if prior.get("payload_hash") != EXPECTED_PRIOR_PAYLOAD_HASH:
        raise RuntimeError("The immutable receipt tip payload has changed")
    recorded_api = (
        prior.get("payload", {})
        .get("evidence", {})
        .get("api_sha256")
    )
    if recorded_api != EXPECTED_PRIOR_API_SHA256:
        raise RuntimeError("The immutable receipt tip no longer binds the prior API")
    return prior


def validate_post_holo_artifacts() -> tuple[str, str]:
    current_api = hashlib.sha256(API.read_bytes()).hexdigest()
    if current_api != EXPECTED_POST_HOLO_API_SHA256:
        raise RuntimeError(
            "Refusing to reconcile an unexpected API projection: "
            f"{current_api}"
        )
    api = json.loads(API.read_text(encoding="utf-8"))
    if api.get("has_card") is not True:
        raise RuntimeError("The reconciled API must expose has_card=true")

    cards = json.loads(CARDS.read_text(encoding="utf-8"))
    card = cards.get(IDENTITY)
    if not isinstance(card, dict):
        raise RuntimeError(f"The HOLO card for {IDENTITY} is missing")
    card_sha256 = canonical_card_sha256(card)
    if card_sha256 != EXPECTED_CARD_SHA256:
        raise RuntimeError(
            "Refusing to reconcile an unexpected HOLO card: "
            f"{card_sha256}"
        )

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    matches = [
        item
        for item in registry.get("agents", [])
        if item.get("name") == IDENTITY
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one registry record for {IDENTITY}")
    record = matches[0]
    if record.get("_has_card") is not True:
        raise RuntimeError("The post-HOLO registry must expose _has_card=true")
    if record.get("_card_sha256") != EXPECTED_CARD_SHA256:
        raise RuntimeError("The post-HOLO registry card digest is inconsistent")
    return current_api, card_sha256


def validate_reconciliation(module, prior: dict, frame: dict) -> None:
    if frame.get("seq") != 10 or frame.get("utc") != RECONCILIATION_UTC:
        raise RuntimeError("The reconciliation frame identity has changed")
    if frame.get("prev") != EXPECTED_PRIOR_PAYLOAD_HASH:
        raise RuntimeError("The reconciliation no longer extends the immutable tip")
    payload = frame.get("payload", {})
    expected_payload = copy.deepcopy(prior["payload"])
    expected_payload["frame"] = 11
    expected_payload["name"] = "publication-reconciliation"
    expected_payload["evidence"]["api_sha256"] = (
        EXPECTED_POST_HOLO_API_SHA256
    )
    expected_payload["reconciliation"] = {
        "reason": (
            "Admission generates HOLO cards before the API projection; bind "
            "the receipt to that final publication shape."
        ),
        "prior_api_sha256": EXPECTED_PRIOR_API_SHA256,
        "prior_frame_hash": EXPECTED_PREFIX_FRAME_HASHES[-1],
        "post_holo_card_sha256": EXPECTED_CARD_SHA256,
    }
    if payload != expected_payload:
        raise RuntimeError("The reconciliation payload has changed")
    if frame.get("payload_hash") != module.H("rapp/1:particle", payload):
        raise RuntimeError("The reconciliation payload hash is invalid")
    if frame.get("payload_hash") != EXPECTED_RECONCILIATION_PAYLOAD_HASH:
        raise RuntimeError("The reconciliation payload is not the exact repair")
    preimage = {
        key: value
        for key, value in frame.items()
        if key not in {"frame_hash", "sig"}
    }
    if frame.get("frame_hash") != module.H("rapp/1:wave", preimage):
        raise RuntimeError("The reconciliation frame hash is invalid")
    if frame.get("frame_hash") != EXPECTED_RECONCILIATION_FRAME_HASH:
        raise RuntimeError("The reconciliation frame is not the exact repair")


def main() -> int:
    module = load_agent_module()
    frames = json.loads(RECEIPT.read_text(encoding="utf-8"))
    prior = validate_prefix(frames)
    if len(frames) >= 11:
        validate_reconciliation(module, prior, frames[10])
    if len(frames) >= 12:
        if frames[11].get("payload", {}).get("name") != (
            "skill-first-grail-migration"
        ):
            raise RuntimeError("Unexpected frame after publication reconciliation")
    if len(frames) == 13:
        if frames[12].get("payload", {}).get("name") != (
            "skill-first-runtime-hardening"
        ):
            raise RuntimeError("Unexpected skill-first runtime frame")
        print("RAPP Projects skill-first runtime receipt is already exact")
        return 0
    if len(frames) == 12:
        print("RAPP Projects skill-first reconciliation is already exact")
        return 0
    if len(frames) == 11:
        print("RAPP Projects publication reconciliation is already exact")
        return 0

    current_api, card_sha256 = validate_post_holo_artifacts()
    payload = copy.deepcopy(prior["payload"])
    payload["frame"] = int(prior["payload"]["frame"]) + 1
    payload["name"] = "publication-reconciliation"
    payload["evidence"]["api_sha256"] = current_api
    payload["reconciliation"] = {
        "reason": (
            "Admission generates HOLO cards before the API projection; bind "
            "the receipt to that final publication shape."
        ),
        "prior_api_sha256": EXPECTED_PRIOR_API_SHA256,
        "prior_frame_hash": EXPECTED_PREFIX_FRAME_HASHES[-1],
        "post_holo_card_sha256": card_sha256,
    }
    frame = {
        "spec": "rapp/1",
        "kind": "build.frame",
        "stream_id": prior["stream_id"],
        "seq": int(prior["seq"]) + 1,
        "utc": RECONCILIATION_UTC,
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

    temporary = RECEIPT.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(frames, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(RECEIPT)
    print(
        "Appended RAPP Projects publication reconciliation: "
        f"{EXPECTED_PRIOR_API_SHA256} -> {current_api}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
