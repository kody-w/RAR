"""Exact RAPP/1 receipt for the RAPP Projects build and reconciliation."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from datetime import datetime
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
AGENT = ROOT / "agents" / "@kody-w" / "rapp_projects_agent.py"
RECEIPT = ROOT / "docs" / "rapp-projects-skill-build.rapp.json"
CATALOG = ROOT / "scout" / "catalog" / "catalog.json"
API_RECORD = ROOT / "api" / "v1" / "agent" / "kody-w__rapp_projects.json"
FRONT = ROOT / "api" / "v1" / "front.json"
REGISTRY = ROOT / "registry.json"
CARDS = ROOT / "cards" / "holo_cards.json"
LIFECYCLE = ROOT / "state" / "agent_lifecycle.json"
RECEIPTS = ROOT / "state" / "receipts"
IDENTITY = "@kody-w/rapp_projects"
PREFIX_FRAME_HASHES = [
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
]
PREFIX_SHA256 = (
    "acce90276506ec61640ffc8f66be1f11285f44c2ca38343640dab54a8b2cc1b1"
)
PRIOR_PAYLOAD_HASH = (
    "c8f4aa2f60b2998a81f828ba0079ac3ac827afe3ef8f929b0ece815d7d9282f0"
)
PRIOR_API_SHA256 = (
    "4df52c49bccbdaa5118ff0ee7e86e40396bb9382b0557584ea26f2dc2d5c8cb4"
)
POST_HOLO_API_SHA256 = (
    "29d3bef143ebf160237b67532a756a6eb9a29680dd2df8830df3a9bfd918e237"
)
POST_HOLO_CARD_SHA256 = (
    "0ea3e4454abc3d21fb1fb042d1cad6aab89e5f40f8910b20694f4153b1987a7b"
)
RECONCILIATION_PAYLOAD_HASH = (
    "b5e9438fd28e45904c1f5a5c9064ac3df0ebc3189d70938a14330ae53ba92e91"
)
RECONCILIATION_FRAME_HASH = (
    "efe2d654184b3c7345866120fef7606b947d6ee71bc7efb52821069281b49069"
)
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
SOURCE_COMMITS = [
    "3f0a4dacbf782b21798e00695c03689dd776272d",
    "5c5f0322218bc68045a3338d15befabd4e33578b",
    "c72e7521be9a7143a28934650963d9b9c480dd11",
    "bb78f67a928eebb8526746429b9c06affad5fcb5",
    "c128767574c7e5d290764e6c6e5d7157b3ecfe46",
    "00dd8de13c549252fa60722058de7cc6e957ed74",
    "90ba975aa831f2e50acd72e41bd0b205d79ed6eb",
    "7d63bcfc271070cff83d5f773ff3f04c1eb4d637",
    "fa28d1f78812d8fcec697fdeb5a2067b0f2efd58",
    "a3391b199669c48572aabdab2087b8c6733f0964",
    "a3391b199669c48572aabdab2087b8c6733f0964",
]


def git_history_contains_sha256(path, expected_sha256):
    relative = path.relative_to(ROOT).as_posix()
    history = subprocess.run(
        ["git", "log", "--format=%H", "--all", "--", relative],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
        timeout=30,
    ).stdout.splitlines()
    for commit in history:
        blob = subprocess.run(
            ["git", "show", f"{commit}:{relative}"],
            cwd=ROOT,
            capture_output=True,
            check=False,
            timeout=30,
        )
        if (
            blob.returncode == 0
            and hashlib.sha256(blob.stdout).hexdigest() == expected_sha256
        ):
            return True
    return False


def load_agent_module():
    spec = importlib.util.spec_from_file_location(
        "_rapp_projects_build_receipt",
        AGENT,
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_ten_frame_build_receipt_is_exact_and_linked():
    module = load_agent_module()
    frames = json.loads(RECEIPT.read_text(encoding="utf-8"))

    assert isinstance(frames, list)
    assert len(frames) == 11
    assert [frame["frame_hash"] for frame in frames[:10]] == (
        PREFIX_FRAME_HASHES
    )
    prefix = json.dumps(
        frames[:10],
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    assert hashlib.sha256(prefix).hexdigest() == PREFIX_SHA256
    assert [frame["seq"] for frame in frames] == list(range(11))
    assert [frame["payload"]["frame"] for frame in frames] == list(range(1, 12))
    assert [frame["payload"]["source_commit"] for frame in frames] == (
        SOURCE_COMMITS
    )
    assert len({frame["stream_id"] for frame in frames}) == 1
    assert re.fullmatch(
        r"rappid:@rapp/rapp-projects-skill-build:[0-9a-f]{64}:build",
        frames[0]["stream_id"],
    )

    previous = None
    for frame in frames:
        assert set(frame) == FRAME_KEYS
        assert frame["spec"] == "rapp/1"
        assert frame["kind"] == "build.frame"
        assert frame["prev_wave"] is None
        assert frame["sig"] is None
        assert frame["prev"] == (
            None if previous is None else previous["payload_hash"]
        )
        assert frame["payload_hash"] == module.H(
            "rapp/1:particle",
            frame["payload"],
        )
        preimage = {
            key: value
            for key, value in frame.items()
            if key not in {"frame_hash", "sig"}
        }
        assert frame["frame_hash"] == module.H("rapp/1:wave", preimage)
        commit = frame["payload"]["source_commit"]
        exists = subprocess.run(
            ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
            cwd=ROOT,
            capture_output=True,
            timeout=30,
        )
        assert exists.returncode == 0, commit
        committed_at = subprocess.run(
            ["git", "show", "-s", "--format=%cI", commit],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        ).stdout.strip()
        frame_utc = datetime.fromisoformat(
            frame["utc"].replace("Z", "+00:00")
        )
        assert frame_utc >= datetime.fromisoformat(committed_at)
        previous = frame

    reconciliation = frames[-1]["payload"]["reconciliation"]
    assert frames[-2]["payload_hash"] == PRIOR_PAYLOAD_HASH
    assert frames[-2]["payload"]["evidence"]["api_sha256"] == PRIOR_API_SHA256
    assert frames[-1]["prev"] == PRIOR_PAYLOAD_HASH
    assert frames[-1]["utc"] == "2026-09-01T00:25:56.072Z"
    assert frames[-1]["payload_hash"] == RECONCILIATION_PAYLOAD_HASH
    assert frames[-1]["frame_hash"] == RECONCILIATION_FRAME_HASH
    assert frames[-1]["payload"]["evidence"]["api_sha256"] == (
        POST_HOLO_API_SHA256
    )
    assert reconciliation == {
        "reason": (
            "Admission generates HOLO cards before the API projection; bind "
            "the receipt to that final publication shape."
        ),
        "prior_api_sha256": PRIOR_API_SHA256,
        "prior_frame_hash": PREFIX_FRAME_HASHES[-1],
        "post_holo_card_sha256": POST_HOLO_CARD_SHA256,
    }


def test_build_receipt_binds_the_generated_publication():
    frames = json.loads(RECEIPT.read_text(encoding="utf-8"))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    [record] = [
        item for item in catalog["skills"] if item["identity"] == IDENTITY
    ]
    [rapp_skill_record] = [
        item
        for item in catalog["skills"]
        if item["identity"] == "@kody-w/rapp_skill_agent"
    ]
    skill = (
        ROOT
        / "scout"
        / "bundles"
        / record["bundle"]
        / "skills"
        / record["skill_name"]
        / "SKILL.md"
    )

    source_sha256 = hashlib.sha256(
        AGENT.read_bytes().replace(b"\r\n", b"\n")
    ).hexdigest()
    skill_sha256 = hashlib.sha256(skill.read_bytes()).hexdigest()
    api_sha256 = hashlib.sha256(API_RECORD.read_bytes()).hexdigest()
    api = json.loads(API_RECORD.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    [registry_record] = [
        item for item in registry["agents"] if item["name"] == IDENTITY
    ]
    cards = json.loads(CARDS.read_text(encoding="utf-8"))
    card = cards.get(IDENTITY)
    has_card = isinstance(card, dict)
    assert api["has_card"] is has_card
    assert registry_record["_has_card"] is has_card
    if has_card:
        evidence = frames[-1]["payload"]["evidence"]
        card_bytes = json.dumps(
            card,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        assert hashlib.sha256(card_bytes).hexdigest() == (
            POST_HOLO_CARD_SHA256
        )
        assert registry_record["_card_sha256"] == POST_HOLO_CARD_SHA256
        assert api_sha256 == POST_HOLO_API_SHA256
    else:
        evidence = frames[-2]["payload"]["evidence"]
        assert "_card_sha256" not in registry_record
        assert api_sha256 == PRIOR_API_SHA256
    front = json.loads(FRONT.read_text(encoding="utf-8"))
    [front_record] = [
        item for item in front["items"] if item["ref"] == IDENTITY
    ]
    assert evidence["agent_version"] == "1.0.3"
    assert evidence["source_sha256"] == source_sha256
    assert evidence["skill_sha256"] == skill_sha256
    assert git_history_contains_sha256(
        API_RECORD,
        evidence["api_sha256"],
    )
    assert api["sha256"] == source_sha256
    assert api["version"] == "1.0.3"
    assert front_record["audience"] == evidence["front_audience"] == "both"
    assert record["source_sha256"] == source_sha256
    assert record["skill_sha256"] == skill_sha256
    assert record["source_commit"] == evidence["agent_source_commit"]
    assert evidence["source_tests"] >= 97
    assert evidence["targeted_tests"] >= 98
    assert evidence["publication_release_tests"] >= 179
    assert evidence["integration_tests"] >= 8102
    assert evidence["build_receipt_tests"] == 2
    assert evidence["privacy_mutations"] == 17
    assert evidence["runner_preflight"] == "RAPP_READY"
    assert evidence["transfer_byte_identical"] is True
    assert evidence["artifact_body_in_egg"] is False
    assert evidence["source_verdict"] == "pass"
    assert evidence["import_verdict"] == "pass"
    assert evidence["rapp1_commit"] == (
        "caf6ef276cafa92aa744499af90dc1a28559941a"
    )
    assert evidence["rapp_sdk_sha256"] == (
        "aba04a57390d98276eadd9c7decd821bb53549730daec3491cffee45ada48eb2"
    )
    assert evidence["rapp_skill_version"] == "1.3.1"
    assert evidence["rapp_skill_source_sha256"] == (
        rapp_skill_record["source_sha256"]
    )
    assert evidence["rapp_skill_skill_sha256"] == (
        rapp_skill_record["skill_sha256"]
    )
    assert evidence["rapp_proof"] == "pass"
    lifecycle = json.loads(LIFECYCLE.read_text(encoding="utf-8"))
    lifecycle_record = lifecycle["agents"][IDENTITY]
    assert lifecycle_record["latest_receipt"] == evidence["rar_receipt"]
    receipt_path = RECEIPTS / (
        evidence["rar_receipt"].removeprefix("rar_") + ".json"
    )
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    assert evidence["notary_policy"] == "rar-maintainer-migration/1.0"
    assert evidence["notary_check"] == "pass"
    assert receipt["acceptance"]["policy"] == evidence["notary_policy"]
    assert receipt["artifact"]["digest"] == source_sha256
    assert receipt["agent"] == IDENTITY
