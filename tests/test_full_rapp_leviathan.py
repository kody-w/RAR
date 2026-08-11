from __future__ import annotations

import importlib.util
import json
import os
import sys
import threading
import types
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT = (
    ROOT
    / "agents"
    / "@kody-w"
    / "full_rapp_leviathan_agent.py"
)
TEST_N = int(
    "ec8d089d611516ff7b89940a4708b674a13be47ffbdc91f73710c4a48386614d"
    "57bba4ed6db81b2d6c753d05b1d1ad56a49a4cdd34a8f7b60d0be34ccfd1e4e"
    "f1010d448555e5f1426fd88700196919aebc16831f6b7432fbd6d29a052e8961"
    "880f5e5215b84c24d5488610865c4df764bdd62367fb6585ebeb320bd4c3d4c0"
    "cae735005ed08df9fd44f8191a7fe374bc1af56e786cc9577a4a40cefe9d9a6"
    "c0713414fd97b24c2379cbb64ac2f2c4ec068ac34f5348efcf63b6800cbe3653"
    "187489c2cf49e83fed10bf6c9d7e6aa74a63d6e790f130ac432c54c361d15264"
    "56327394bd8ca8bb98df0eaa989a584f2c514bdbf862364f4a253f97c5a1aa6"
    "bbf",
    16,
)
TEST_D = int(
    "42188637b350b94459b86f6d0fbc177f2f2e1502cdd52bd3efc6f7ab2035042b"
    "2040862cf16367f4a14180f37e642012fd9b3faeef6fe7072f4e0b0d03649a9b"
    "51d9e1f6f423925d872780600b918ecdc2e21fc31634cec9201cc86ccbbdc172"
    "c755edd80c426428475e73fe6cb13ddf48036bd5de898cd7ac6150dc93d8ecce"
    "74bcb83e7ea4e49ac969fb72e67bf78fb476c1536cda3e3d2aa175ea9a5558e"
    "238378cad15f01d2deeb8ef1cacfb3f7b5e5a08dbb1b6167e8a01266abbb34d"
    "f4b8ca5e17e468fb4413e9607404906f1a263265b2f5d66cdac2dd70906f296b"
    "c4912cc05e9fe837e30a40d25beb338fc21f4ae95abd7a68a0664c2b98e9905"
    "bc1",
    16,
)
TEST_E = 65537
VERIFIER = "https://verifier.example.com"


class BasicAgent:
    def __init__(self, name=None, metadata=None):
        self.name = name
        self.metadata = metadata


def load_agent(workspace: Path):
    agents = types.ModuleType("agents")
    basic = types.ModuleType("agents.basic_agent")
    basic.BasicAgent = BasicAgent
    agents.basic_agent = basic
    sys.modules["agents"] = agents
    sys.modules["agents.basic_agent"] = basic
    os.environ["RAPP_LEVIATHANS_ROOT"] = str(workspace)
    spec = importlib.util.spec_from_file_location(
        "full_rapp_leviathan_test",
        AGENT,
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def trust_anchor():
    return {
        "schema": "rapp-trust-anchor/1",
        "id": VERIFIER,
        "algorithm": "rsa-sha256",
        "modulus_hex": format(TEST_N, "x"),
        "exponent": TEST_E,
    }


def sign_evidence(module, value):
    digest = module.hashlib.sha256(
        module._evidence_message(value)
    ).digest()
    digest_info = bytes.fromhex(
        "3031300d060960864801650304020105000420"
    ) + digest
    width = (TEST_N.bit_length() + 7) // 8
    padding = width - len(digest_info) - 3
    encoded = (
        b"\x00\x01"
        + b"\xff" * padding
        + b"\x00"
        + digest_info
    )
    signature = pow(
        int.from_bytes(encoded, "big"),
        TEST_D,
        TEST_N,
    )
    value["signature_hex"] = format(signature, f"0{width * 2}x")
    return value


def test_protocol_is_clean_room_full_rapp_definition(tmp_path):
    module = load_agent(tmp_path)
    result = json.loads(
        module.FullRappLeviathanAgent().perform(
            operation="protocol"
        )
    )
    protocol = result["result"]
    assert protocol["schema"] == "rapp-full-leviathan/1"
    assert set(protocol["organs"]) == {
        "identity",
        "intelligence",
        "production",
        "truth",
        "commerce",
    }
    assert set(protocol["planes"]) == {
        "control",
        "private-execution",
        "memory-continuity",
        "evidence-recovery",
        "public-discovery-commerce",
    }


def test_blueprint_materialize_and_inspect_round_trip(tmp_path):
    module = load_agent(tmp_path)
    agent = module.FullRappLeviathanAgent()
    built = json.loads(agent.perform(
        operation="blueprint",
        name="Agent Market Intelligence",
        intent=(
            "Sell agent-ready market intelligence through a persistent "
            "Brainstem, private execution, evidence, and paid tool calls."
        ),
        customer="Marketing agencies",
    ))
    blueprint = built["result"]
    materialized = json.loads(agent.perform(
        operation="materialize",
        blueprint_json=json.dumps(blueprint),
    ))
    assert materialized["status"] == "ok"
    inspected = json.loads(agent.perform(
        operation="inspect",
        name="Agent Market Intelligence",
    ))
    assert inspected["result"]["blueprint"] == blueprint
    assert inspected["result"]["assessment"]["full_leviathan"] is False
    repeated = json.loads(agent.perform(
        operation="materialize",
        name="Agent Market Intelligence",
        intent=(
            "Sell agent-ready market intelligence through a persistent "
            "Brainstem, private execution, evidence, and paid tool calls."
        ),
        customer="Marketing agencies",
    ))
    assert repeated["status"] == "ok"


def test_assessment_requires_evidence_for_every_organ_and_plane(tmp_path):
    module = load_agent(tmp_path)
    architecture = module.blueprint(
        name="Conformance Candidate",
        intent=(
            "Operate a governed agent business with private execution, "
            "evidence, memory, and commerce."
        ),
        customer="Enterprise operators",
    )
    def evidence(label):
        return sign_evidence(module, {
            "schema": "rapp-evidence-ref/1",
            "kind": sorted(module.REQUIRED_KINDS[label])[0],
            "subject": architecture["id"],
            "claim": label,
            "reference": "urn:sha256:" + "a" * 64,
            "artifact_sha256": "a" * 64,
            "verifier": VERIFIER,
            "independent": True,
        })
    for item in architecture["organs"].values():
        item["status"] = "proven"
        item["evidence"] = {
            label: evidence(label)
            for label in item["evidence_required"]
        }
    for item in architecture["planes"].values():
        item["status"] = "proven"
        item["endpoint_or_surface"] = (
            "urn:rapp:surface:verified-plane"
        )
        item["evidence"] = {
            label: evidence(label)
            for label in item["evidence_required"]
        }
    architecture["loop_evidence"] = {
        label: evidence(label)
        for label in architecture["end_to_end_loop"]
    }
    stable = {
        key: value
        for key, value in architecture.items()
        if key != "sha256"
    }
    architecture["sha256"] = module._digest(stable)
    full = module.assess(architecture, [trust_anchor()])
    assert full["full_leviathan"] is True

    proven = deepcopy(architecture)
    for name, item in proven["organs"].items():
        for label in item["evidence_required"]:
            candidate = deepcopy(proven)
            del candidate["organs"][name]["evidence"][label]
            stable = {
                key: value
                for key, value in candidate.items()
                if key != "sha256"
            }
            candidate["sha256"] = module._digest(stable)
            partial = module.assess(candidate, [trust_anchor()])
            assert partial["full_leviathan"] is False
            assert name in partial["missing_organs"]
            assert label in partial["organs"][name]["missing_evidence"]

    for name, item in proven["planes"].items():
        for label in item["evidence_required"]:
            candidate = deepcopy(proven)
            del candidate["planes"][name]["evidence"][label]
            stable = {
                key: value
                for key, value in candidate.items()
                if key != "sha256"
            }
            candidate["sha256"] = module._digest(stable)
            partial = module.assess(candidate, [trust_anchor()])
            assert partial["full_leviathan"] is False
            assert name in partial["missing_planes"]
            assert label in partial["planes"][name]["missing_evidence"]

    for label in proven["end_to_end_loop"]:
        candidate = deepcopy(proven)
        del candidate["loop_evidence"][label]
        stable = {
            key: value
            for key, value in candidate.items()
            if key != "sha256"
        }
        candidate["sha256"] = module._digest(stable)
        partial = module.assess(candidate, [trust_anchor()])
        assert partial["full_leviathan"] is False
        assert label in partial["missing_loop_evidence"]


def test_materialize_rejects_extra_or_sensitive_fields(tmp_path):
    module = load_agent(tmp_path)
    value = module.blueprint(
        name="Public Candidate",
        intent=(
            "Operate a governed agent service with private execution, "
            "evidence, memory, and commerce."
        ),
        customer="Enterprise operators",
    )
    value["private_memory"] = "do not publish"
    stable = {
        key: item
        for key, item in value.items()
        if key != "sha256"
    }
    value["sha256"] = module._digest(stable)
    try:
        module.materialize(value)
    except module.LeviathanError:
        pass
    else:
        raise AssertionError("extra private field was accepted")

    try:
        module.blueprint(
            name="Sensitive Candidate",
            intent=(
                "Use bearer abcdefghijklmnopqrstuvwxyz123456 to operate "
                "a public agent service."
            ),
            customer="Enterprise operators",
        )
    except module.LeviathanError:
        pass
    else:
        raise AssertionError("credential-like intent was accepted")


def test_generated_public_surfaces_match_clean_room_package():
    api = json.loads(
        (
            ROOT
            / "api"
            / "v1"
            / "agent"
            / "kody-w__full_rapp_leviathan.json"
        ).read_text(encoding="utf-8")
    )
    cards = json.loads(
        (ROOT / "cards" / "holo_cards.json").read_text(
            encoding="utf-8"
        )
    )
    card = cards["@kody-w/full_rapp_leviathan"]
    assert api["version"] == "1.0.1"
    assert api["card_url"] is None
    assert api["api_card_url"] is None
    card_text = card["abilities"][0]["text"].lower()
    assert "identity" in card_text
    assert "commerce" in card_text


def test_nested_private_evidence_and_topology_are_rejected(tmp_path):
    module = load_agent(tmp_path)
    value = module.blueprint(
        name="Public Candidate",
        intent=(
            "Operate a governed public agent service with evidence, memory, "
            "private execution, and commerce."
        ),
        customer="Enterprise operators",
    )
    value["loop_evidence"]["private_payload"] = {
        "schema": "rapp-evidence-ref/1",
        "kind": "test",
        "subject": value["id"],
        "claim": "private_payload",
        "reference": "urn:sha256:" + "a" * 64,
        "artifact_sha256": "a" * 64,
        "verifier": "https://verifier.example.com",
        "signature_hex": "00",
        "independent": True,
    }
    stable = {
        key: item
        for key, item in value.items()
        if key != "sha256"
    }
    value["sha256"] = module._digest(stable)
    try:
        module.materialize(value)
    except module.LeviathanError:
        pass
    else:
        raise AssertionError("extra private loop evidence was accepted")

    value = module.blueprint(
        name="Topology Candidate",
        intent=(
            "Operate a governed public agent service with evidence, memory, "
            "private execution, and commerce."
        ),
        customer="Enterprise operators",
    )
    value["planes"]["control"]["endpoint_or_surface"] = (
        "http://10.20.30.40/rbox"
    )
    stable = {
        key: item
        for key, item in value.items()
        if key != "sha256"
    }
    value["sha256"] = module._digest(stable)
    try:
        module.materialize(value)
    except module.LeviathanError:
        pass
    else:
        raise AssertionError("private topology was accepted")


def test_self_attested_evidence_cannot_claim_full(tmp_path):
    module = load_agent(tmp_path)
    verifier = VERIFIER
    architecture = module.blueprint(
        name="Self Attested Candidate",
        intent=(
            "Operate a governed agent service with evidence, memory, private "
            "execution, and commerce."
        ),
        customer="Enterprise operators",
    )

    def evidence(label):
        return sign_evidence(module, {
            "schema": "rapp-evidence-ref/1",
            "kind": sorted(module.REQUIRED_KINDS[label])[0],
            "subject": architecture["id"],
            "claim": label,
            "reference": "urn:sha256:" + "a" * 64,
            "artifact_sha256": "a" * 64,
            "verifier": verifier,
            "independent": True,
        })

    for item in architecture["organs"].values():
        item["status"] = "proven"
        item["evidence"] = {
            label: evidence(label)
            for label in item["evidence_required"]
        }
    for item in architecture["planes"].values():
        item["status"] = "proven"
        item["endpoint_or_surface"] = "urn:rapp:surface:verified-plane"
        item["evidence"] = {
            label: evidence(label)
            for label in item["evidence_required"]
        }
    architecture["loop_evidence"] = {
        label: evidence(label)
        for label in architecture["end_to_end_loop"]
    }
    stable = {
        key: value
        for key, value in architecture.items()
        if key != "sha256"
    }
    architecture["sha256"] = module._digest(stable)
    assert module.assess(architecture)["full_leviathan"] is False
    assert module.assess(
        architecture,
        [{
            **trust_anchor(),
            "id": "https://different-verifier.example.com",
        }],
    )["full_leviathan"] is False
    assert module.assess(
        architecture,
        [trust_anchor()],
    )["full_leviathan"] is True


def test_weak_anchor_and_digest_mismatch_are_rejected(tmp_path):
    module = load_agent(tmp_path)
    weak = {
        **trust_anchor(),
        "modulus_hex": "f" * 128,
    }
    try:
        module._validate_trust_anchor(weak)
    except module.LeviathanError:
        pass
    else:
        raise AssertionError("weak RSA anchor was accepted")

    record = {
        "schema": "rapp-evidence-ref/1",
        "kind": "test",
        "subject": "leviathan:expected",
        "claim": "acceptance tests",
        "reference": "urn:sha256:" + "a" * 64,
        "artifact_sha256": "b" * 64,
        "verifier": VERIFIER,
        "independent": True,
        "signature_hex": "00",
    }
    assert not module._evidence_valid(
        record,
        allowed_kinds={"test"},
        subject="leviathan:expected",
        claim="acceptance tests",
    )
    assert not module._evidence_valid(
        {
            **record,
            "reference": " " + record["reference"] + " ",
        },
        allowed_kinds={"test"},
        subject="leviathan:expected",
        claim="acceptance tests",
    )


def test_public_reference_grammar_is_canonical(tmp_path):
    module = load_agent(tmp_path)
    assert module._public_reference(
        "urn:rapp:surface:abc",
        "reference",
    ) == "urn:rapp:surface:abc"
    assert module._public_reference(
        "https://evidence.example.com:8443/artifact",
        "reference",
    ).startswith("https://")
    assert module._public_reference(
        "https://evidence.example.com/releases/2026-08-11",
        "reference",
    ).startswith("https://")
    assert module._public_reference(
        "https://evidence.example.com/archive/10.0.0.1/artifact",
        "reference",
    ).startswith("https://")
    assert module._public_reference(
        "https://[2001:4860:4860::8888]/artifact",
        "reference",
    ).startswith("https://")
    for value in (
        "urn:rapp:surface:ab",
        "urn:rapp:surface:Uppercase",
        "https://user@evidence.example.com/artifact",
        "https://@evidence.example.com/artifact",
        "https://evidence.example.com/artifact?mutable=yes",
        "https://evidence.example.com/artifact?",
        "https://evidence.example.com/artifact#",
        "https://evidence.example.com:/artifact",
        "https://evidence.example.com:notaport/artifact",
        "https://0x7f.0.0.1/control",
        "https://%31%32%37.0.0.1/control",
        "https://１２７.０.０.１/control",
        "https://local\thost\\public.example/path",
        "https://localhost\\public.example/path",
        "https://home.arpa/control",
        "https://[v1.fe80]/artifact",
        "HTTPS://[v1.fe80]/artifact",
    ):
        try:
            module._public_reference(value, "reference")
        except module.LeviathanError:
            continue
        raise AssertionError(f"invalid reference was accepted: {value}")

    assert module._public_verifier(
        "did:web:verifier.example.com"
    ) == "did:web:verifier.example.com"
    assert module._public_verifier(
        "did:web:xn--bcher-kva.example"
    ) == "did:web:xn--bcher-kva.example"
    assert module._public_verifier(
        "did:key:zPublicVerifier"
    ) == "did:key:zPublicVerifier"
    for value in (
        "did:web:localhost",
        "did:web:127.0.0.1",
        "did:web:%31%32%37.0.0.1",
        "did:web:8.8.8.8",
        "did:web:example..com",
        "did:web:home.arpa",
    ):
        try:
            module._public_verifier(value)
        except module.LeviathanError:
            continue
        raise AssertionError(f"private verifier was accepted: {value}")


def test_public_text_rejects_private_topology(tmp_path):
    module = load_agent(tmp_path)
    for intent in (
        (
            "Operate the private service at 10.20.30.40 with evidence, "
            "memory, execution, and commerce."
        ),
        (
            "Load file:///Users/operator/private-rbox/topology.json and "
            "operate a governed agent service."
        ),
        (
            "Operate the private service at fd00::1 with evidence, "
            "memory, execution, and commerce."
        ),
        (
            "Operate the private service at fe80::1 with evidence, "
            "memory, execution, and commerce."
        ),
        (
            "Operate the private service at ::1 with evidence, "
            "memory, execution, and commerce."
        ),
        (
            "Operate endpoint:fd00::1 with evidence, memory, "
            "execution, and commerce."
        ),
        (
            "Operate node:fd00::1 with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate foo::fd00::1 with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate fd00::1:: with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate fe80::1: with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate fd00::1. with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate fe80::1. with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate ::1. with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate http://[::]:8080 with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate the private service at :: with evidence, memory, "
            "execution, and commerce."
        ),
        (
            "Operate fec0::1 with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate ff02::1 with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate ff05::1 with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate 0x7f.0.0.1 with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate 0177.0.0.1 with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate 2130706433 with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate 127.1 with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate 010.020.030.040 with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate 172.016.5.4 with evidence, memory, execution, "
            "and commerce."
        ),
        (
            "Operate 100.064.1.1 with evidence, memory, execution, "
            "and commerce."
        ),
    ):
        try:
            module.blueprint(
                name="Topology Leak",
                intent=intent,
                customer="Enterprise operators",
            )
        except module.LeviathanError:
            continue
        raise AssertionError("private topology was accepted")

    public = module.blueprint(
        name="Public IPv6",
        intent=(
            "Operate the public service at 2001:4860:4860::8888 with "
            "evidence, memory, execution, and commerce."
        ),
        customer="Enterprise operators",
    )
    assert public["name"] == "Public IPv6"

    prose = module.blueprint(
        name="Namespace Prose",
        intent=(
            "Use syntax:: as a namespace separator while operating a "
            "governed service with evidence, memory, execution, and commerce."
        ),
        customer="Enterprise operators",
    )
    assert prose["name"] == "Namespace Prose"

    version_prose = module.blueprint(
        name="Version Prose",
        intent=(
            "Use protocol version 1.2 while operating a governed service "
            "with evidence, memory, execution, and commerce."
        ),
        customer="Enterprise operators",
    )
    assert version_prose["name"] == "Version Prose"


def test_concurrent_materialization_never_last_writer_wins(tmp_path):
    module = load_agent(tmp_path)
    first = module.blueprint(
        name="Concurrent Candidate",
        intent=(
            "Operate one governed agent service with evidence, memory, "
            "private execution, and commerce."
        ),
        customer="Enterprise operators",
    )
    second = module.blueprint(
        name="Concurrent Candidate",
        intent=(
            "Operate a different governed agent service with evidence, "
            "memory, private execution, and commerce."
        ),
        customer="Enterprise operators",
    )
    barrier = threading.Barrier(2)
    outcomes = []

    def write(value):
        barrier.wait()
        try:
            module.materialize(value)
        except module.LeviathanError:
            outcomes.append("rejected")
        else:
            outcomes.append("written")

    threads = [
        threading.Thread(target=write, args=(value,))
        for value in (first, second)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    assert sorted(outcomes) == ["rejected", "written"]
    stored = module._read_blueprint("concurrent-candidate")
    assert stored in (first, second)
