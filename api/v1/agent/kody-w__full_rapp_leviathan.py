"""Full RAPP Leviathan

Clean-room public protocol implementation for compiling a governed agent
business from intent.

A Full RAPP Leviathan is a governed operating system that closes the complete
loop:

    intent -> intelligence -> production -> evidence -> commerce -> memory

Every Full RAPP Leviathan has five required organs:

1. Identity
   Constitutional purpose, authority, ownership, policy, succession, and the
   public/private boundary.
2. Intelligence
   Brainstem runtimes, persistent state, memory, sessions, and trusted tools.
3. Production
   A repeatable foundry that turns use cases and trusted sources into isolated
   deployable capabilities.
4. Truth
   Twins, evaluations, receipts, limitations, recovery, and release gates.
5. Commerce
   Machine-readable discovery, access control, payment, distribution, and
   measured outcomes.

The protocol also requires five operating planes:

- control;
- private execution;
- memory continuity;
- evidence and recovery;
- public discovery and commerce.

RBox is the first declared private implementation. This public agent exposes
only the protocol, deterministic assessment, synthetic blueprints, and public
conformance bundles. It contains no customer data, PII, credentials, private
memory, proprietary orchestration, economics, deployment topology, or private
RBox implementation.

Actions
=======

protocol
    Return the complete public protocol.
assess
    Assess a supplied architecture JSON against the protocol.
blueprint
    Compile intent into a deterministic public-safe Leviathan blueprint.
materialize
    Write a public conformance bundle under ~/.rapp/leviathans/<slug>/.
inspect
    Read and reassess one materialized bundle.
list
    List materialized Leviathan protocol bundles.
"""

from __future__ import annotations

import hashlib
import ipaddress
import json
import os
import re
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name = name
            self.metadata = metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/full_rapp_leviathan",
    "version": "1.0.0",
    "display_name": "FullRappLeviathan",
    "description": (
        "Compiles and assesses public-safe Full RAPP Leviathan blueprints "
        "across identity, intelligence, production, truth, and commerce."
    ),
    "author": "kody-w",
    "industry": "meta",
    "tags": [
        "leviathan",
        "protocol",
        "brainstem",
        "foundry",
        "evidence",
        "commerce",
        "x402",
        "enterprise",
    ],
    "category": "meta",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {
        "args": {
            "operation": "blueprint",
            "name": "agent-market-intelligence",
            "intent": (
                "Sell agent-ready market intelligence through a persistent "
                "Brainstem, private execution, evidence, and paid tool calls."
            ),
            "customer": "Marketing agencies",
        }
    },
}


PROTOCOL_SCHEMA = "rapp-full-leviathan/1"
BLUEPRINT_SCHEMA = "rapp-leviathan-blueprint/1"
ASSESSMENT_SCHEMA = "rapp-leviathan-assessment/1"
WORKSPACE = Path(
    os.environ.get(
        "RAPP_LEVIATHANS_ROOT",
        str(Path.home() / ".rapp" / "leviathans"),
    )
).expanduser()
SLUG = re.compile(r"[a-z0-9][a-z0-9-]{2,63}\Z")
SENSITIVE = re.compile(
    r"(?i)(gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
    r"bearer\s+[A-Za-z0-9._-]{24,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|"
    r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b|"
    r"\b\d{3}-\d{2}-\d{4}\b)"
)


ORGANS = {
    "identity": {
        "purpose": (
            "Bind purpose, authority, ownership, policy, succession, and the "
            "public/private boundary."
        ),
        "required_evidence": [
            "constitutional purpose",
            "named authority",
            "ownership and custody boundary",
            "data classification policy",
            "succession or shutdown path",
        ],
    },
    "intelligence": {
        "purpose": (
            "Operate persistent Brainstem intelligence with state, memory, "
            "sessions, trusted tools, and bounded model access."
        ),
        "required_evidence": [
            "durable runtime identity",
            "memory and session contract",
            "tool allowlist",
            "quota and model-cost boundary",
            "pause and recovery controls",
        ],
    },
    "production": {
        "purpose": (
            "Compile use cases and trusted sources into reproducible, isolated, "
            "deployable capabilities."
        ),
        "required_evidence": [
            "use-case contract",
            "source provenance",
            "repeatable build",
            "isolated deployment target",
            "rollback and retirement path",
        ],
    },
    "truth": {
        "purpose": (
            "Separate claims from evidence through twins, evaluations, "
            "receipts, limitations, recovery, and release gates."
        ),
        "required_evidence": [
            "acceptance tests",
            "independent evaluation boundary",
            "append-only or versioned receipts",
            "documented limitations",
            "release and recovery gate",
        ],
    },
    "commerce": {
        "purpose": (
            "Make capabilities discoverable, accessible, payable, distributable, "
            "and measurable by humans and agents."
        ),
        "required_evidence": [
            "machine-readable discovery",
            "access-control contract",
            "payment or subscription contract",
            "distribution channel",
            "measured customer outcome",
        ],
    },
}


PLANES = {
    "control": (
        "One authenticated plane for users and agents to inspect and operate "
        "the system without bypassing policy."
    ),
    "private-execution": (
        "A bounded runtime for private state, tools, credentials, and external "
        "actions."
    ),
    "memory-continuity": (
        "Durable organizational and session memory with explicit capture and "
        "recovery."
    ),
    "evidence-recovery": (
        "Independent evidence, receipts, rollback, restore, export, and "
        "transition."
    ),
    "public-discovery-commerce": (
        "Public-safe discovery, interfaces, access terms, payment, and "
        "distribution."
    ),
}

PLANE_EVIDENCE = {
    "control": [
        "authenticated control interface",
        "policy enforcement result",
    ],
    "private-execution": [
        "bounded runtime evidence",
        "secret and network boundary evidence",
    ],
    "memory-continuity": [
        "durable memory evidence",
        "restore or replay evidence",
    ],
    "evidence-recovery": [
        "independent evaluation evidence",
        "rollback or recovery evidence",
    ],
    "public-discovery-commerce": [
        "machine-readable discovery evidence",
        "access or payment evidence",
    ],
}

LOOP_STEPS = [
    "capture intent",
    "invoke Brainstem intelligence",
    "compile or select capability",
    "execute inside private policy",
    "evaluate and preserve evidence",
    "publish discovery and access terms",
    "settle payment or subscription",
    "measure outcome and update memory",
]

REQUIRED_KINDS = {
    "constitutional purpose": {"policy"},
    "named authority": {"policy"},
    "ownership and custody boundary": {"policy"},
    "data classification policy": {"policy"},
    "succession or shutdown path": {"runbook", "test"},
    "durable runtime identity": {"receipt", "measurement"},
    "memory and session contract": {"policy", "test"},
    "tool allowlist": {"policy", "test"},
    "quota and model-cost boundary": {"policy", "measurement"},
    "pause and recovery controls": {"runbook", "test"},
    "use-case contract": {"policy"},
    "source provenance": {"receipt"},
    "repeatable build": {"test", "receipt"},
    "isolated deployment target": {"test", "measurement"},
    "rollback and retirement path": {"runbook", "test"},
    "acceptance tests": {"test"},
    "independent evaluation boundary": {"policy", "receipt"},
    "append-only or versioned receipts": {"receipt", "test"},
    "documented limitations": {"policy"},
    "release and recovery gate": {"test", "runbook"},
    "machine-readable discovery": {"test", "measurement"},
    "access-control contract": {"policy", "test"},
    "payment or subscription contract": {"receipt", "policy"},
    "distribution channel": {"measurement", "receipt"},
    "measured customer outcome": {"measurement", "receipt"},
    "authenticated control interface": {"test", "measurement"},
    "policy enforcement result": {"test", "receipt"},
    "bounded runtime evidence": {"test", "measurement"},
    "secret and network boundary evidence": {"test", "measurement"},
    "durable memory evidence": {"test", "measurement"},
    "restore or replay evidence": {"test", "receipt"},
    "independent evaluation evidence": {"test", "receipt"},
    "rollback or recovery evidence": {"test", "receipt"},
    "machine-readable discovery evidence": {"test", "measurement"},
    "access or payment evidence": {"test", "receipt"},
    "capture intent": {"receipt"},
    "invoke Brainstem intelligence": {"receipt", "measurement"},
    "compile or select capability": {"receipt", "test"},
    "execute inside private policy": {"receipt", "test"},
    "evaluate and preserve evidence": {"receipt", "test"},
    "publish discovery and access terms": {"receipt", "test"},
    "settle payment or subscription": {"receipt"},
    "measure outcome and update memory": {"measurement", "receipt"},
}


PUBLIC_PRIVATE_BOUNDARY = {
    "public": [
        "protocol definitions and schemas",
        "machine-readable discovery contracts",
        "synthetic examples and conformance vectors",
        "public-safe agent and payment interfaces",
        "implementation-independent conformance tests",
    ],
    "private": [
        "customer data, PII, PHI, and production records",
        "credentials, wallet secrets, and provider account identifiers",
        "private prompts, memory, reasoning, and operator context",
        "proprietary orchestration, scoring, pricing, and economics",
        "deployment topology, customer connectors, and acceptance evidence",
    ],
}


PROTOCOL = {
    "schema": PROTOCOL_SCHEMA,
    "version": "1.0.0",
    "name": "Full RAPP Leviathan Protocol",
    "definition": (
        "A governed operating system that turns human intent into repeatable, "
        "evidence-bound, commercially accessible agent capability."
    ),
    "organs": ORGANS,
    "planes": PLANES,
    "boundary": PUBLIC_PRIVATE_BOUNDARY,
    "conformance": {
        "full": (
            "All five organs and all five planes are present with evidence and "
            "one governed end-to-end operating loop."
        ),
        "partial": (
            "At least one required organ or plane is missing, unproven, or "
            "disconnected."
        ),
        "not_implied": [
            "legal personhood",
            "certified isolation",
            "hardware attestation",
            "unsupervised consequential authority",
            "guaranteed outcomes",
        ],
    },
    "first_declared_private_implementation": "RBox",
}


class LeviathanError(ValueError):
    pass


def _exclusive_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(value, indent=2, sort_keys=True).encode() + b"\n"
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=path.parent,
    )
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.link(temporary, path)
        os.unlink(temporary)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


def _canonical(value: Any) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def _text(
    value: Any,
    label: str,
    *,
    minimum: int = 1,
    maximum: int = 4000,
) -> str:
    if not isinstance(value, str):
        raise LeviathanError(f"{label} must be text")
    result = value.strip()
    if not minimum <= len(result) <= maximum:
        raise LeviathanError(
            f"{label} must be {minimum}-{maximum} characters"
        )
    return result


def _public_text(value: Any, label: str, maximum: int) -> str:
    result = _text(value, label, maximum=maximum)
    if SENSITIVE.search(result):
        raise LeviathanError(
            f"{label} contains credential or personal-data patterns"
        )
    if (
        re.search(
            r"(?i)(?:file://|/Users/|/home/|[A-Z]:\\Users\\|"
            r"\b(?:localhost|[a-z0-9-]+\.(?:local|internal|lan|home))\b)",
            result,
        )
    ):
        raise LeviathanError(f"{label} contains private topology")
    for candidate in re.findall(
        r"(?<![0-9])(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![0-9])",
        result,
    ):
        try:
            address = ipaddress.ip_address(candidate)
        except ValueError:
            continue
        if not address.is_global:
            raise LeviathanError(f"{label} contains private topology")
    return result


def _public_surface(value: Any, label: str) -> str:
    result = _public_text(value, label, 2000)
    if result.startswith("urn:rapp:surface:") and re.fullmatch(
        r"urn:rapp:surface:[a-z0-9][a-z0-9._-]{2,127}",
        result,
    ):
        return result
    if not result.lower().startswith(("http://", "https://")):
        raise LeviathanError(
            f"{label} must be a public HTTPS URL or RAPP surface URN"
        )
    parsed = urlsplit(result)
    if parsed.scheme != "https" or not parsed.hostname:
        raise LeviathanError(f"{label} must use a public HTTPS URL")
    if (
        parsed.username
        or parsed.password
        or parsed.query
        or parsed.fragment
    ):
        raise LeviathanError(
            f"{label} URL cannot contain userinfo, query, or fragment"
        )
    hostname = parsed.hostname.lower()
    try:
        address = ipaddress.ip_address(hostname)
    except ValueError:
        address = None
    if address is not None:
        if not address.is_global:
            raise LeviathanError(
                f"{label} contains a non-public IP address"
            )
        return result
    if re.fullmatch(r"(?:0x[0-9a-f]+|[0-9.]+)", hostname):
        raise LeviathanError(f"{label} contains a numeric private host")
    if (
        hostname == "localhost"
        or hostname.endswith((".local", ".internal", ".lan", ".home"))
        or "." not in hostname
    ):
        raise LeviathanError(f"{label} contains an internal hostname")
    return result


def _public_reference(value: Any, label: str) -> str:
    result = _public_text(value, label, 2000)
    if re.fullmatch(r"urn:sha256:[0-9a-f]{64}", result):
        return result
    return _public_surface(result, label)


def _public_verifier(value: Any) -> str:
    result = _public_text(value, "verifier", 1000)
    if re.fullmatch(r"did:(?:web|key):[A-Za-z0-9._:%-]+", result):
        return result
    return _public_surface(result, "verifier")


def _slug(value: str) -> str:
    result = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    result = result[:64].rstrip("-")
    if not SLUG.fullmatch(result):
        raise LeviathanError("name cannot produce a valid Leviathan slug")
    return result


def _object(value: Any, label: str) -> dict[str, Any]:
    if isinstance(value, dict):
        return deepcopy(value)
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except ValueError as error:
            raise LeviathanError(f"{label} is malformed JSON") from error
        if isinstance(parsed, dict):
            return parsed
    raise LeviathanError(f"{label} must be an object")


def _atomic_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=path.parent,
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


def _workspace(slug: str) -> Path:
    return WORKSPACE / slug


def _default_organ(
    organ: str,
) -> dict[str, Any]:
    patterns = {
        "identity": [
            "Define the operator, customer, owner, and authority boundaries.",
            "Classify public protocol separately from private implementation.",
            "Document shutdown, succession, and customer exit.",
        ],
        "intelligence": [
            "Provide one durable Brainstem identity per governed instance.",
            "Persist session and organizational memory.",
            "Expose typed, allowlisted tools with quotas and pause controls.",
        ],
        "production": [
            "Accept a use case or trusted library source.",
            "Generate a reproducible capability bundle.",
            "Deploy to a bounded private runtime with rollback.",
        ],
        "truth": [
            "Test the promised workflow against synthetic fixtures.",
            "Keep evaluation authority outside the builder's control.",
            "Bind claims to receipts, limitations, and recovery evidence.",
        ],
        "commerce": [
            "Publish agent cards, OpenAPI, and machine-readable pricing.",
            "Gate valuable calls with subscription or agent-native payment.",
            "Measure accepted outcomes and direct provider cost.",
        ],
    }
    return {
        "status": "planned",
        "purpose": ORGANS[organ]["purpose"],
        "design": patterns[organ],
        "evidence_required": ORGANS[organ]["required_evidence"],
        "evidence": {},
    }


def _default_plane(plane: str) -> dict[str, Any]:
    return {
        "status": "planned",
        "purpose": PLANES[plane],
        "endpoint_or_surface": None,
        "evidence_required": PLANE_EVIDENCE[plane],
        "evidence": {},
    }


def blueprint(
    *,
    name: str,
    intent: str,
    customer: str,
    revenue_model: str = "subscription plus paid agent calls",
) -> dict[str, Any]:
    name = _public_text(name, "name", 120)
    intent = _public_text(intent, "intent", 4000)
    if len(intent) < 20:
        raise LeviathanError("intent must be 20-4000 characters")
    customer = _public_text(customer, "customer", 1000)
    revenue_model = _public_text(
        revenue_model,
        "revenue model",
        1000,
    )
    slug = _slug(name)
    value = {
        "schema": BLUEPRINT_SCHEMA,
        "protocol": {
            "schema": PROTOCOL_SCHEMA,
            "version": PROTOCOL["version"],
        },
        "id": f"leviathan:{slug}",
        "name": name,
        "slug": slug,
        "intent": intent,
        "customer": customer,
        "revenue_model": revenue_model,
        "classification": "public-safe-blueprint",
        "organs": {
            organ: _default_organ(organ)
            for organ in ORGANS
        },
        "planes": {
            plane: _default_plane(plane)
            for plane in PLANES
        },
        "end_to_end_loop": LOOP_STEPS,
        "loop_evidence": {},
        "boundary": deepcopy(PUBLIC_PRIVATE_BOUNDARY),
    }
    value["sha256"] = _digest(value)
    return value


def _evidence_valid(
    value: Any,
    *,
    allowed_kinds: set[str],
    subject: str,
    claim: str,
) -> bool:
    return (
        isinstance(value, dict)
        and set(value) == {
            "schema",
            "kind",
            "subject",
            "claim",
            "reference",
            "artifact_sha256",
            "verifier",
            "signature_hex",
            "independent",
        }
        and value.get("schema") == "rapp-evidence-ref/1"
        and value.get("kind") in allowed_kinds
        and value.get("subject") == subject
        and value.get("claim") == claim
        and isinstance(value.get("reference"), str)
        and bool(value["reference"].strip())
        and _is_public_reference(value["reference"])
        and isinstance(value.get("artifact_sha256"), str)
        and bool(re.fullmatch(r"[0-9a-f]{64}", value["artifact_sha256"]))
        and (
            not value["reference"].startswith("urn:sha256:")
            or value["reference"].removeprefix("urn:sha256:")
            == value["artifact_sha256"]
        )
        and isinstance(value.get("verifier"), str)
        and _is_public_verifier(value["verifier"])
        and isinstance(value.get("signature_hex"), str)
        and bool(
            re.fullmatch(r"[0-9a-f]+", value["signature_hex"])
        )
        and value.get("independent") is True
    )


def _is_public_reference(value: str) -> bool:
    try:
        _public_reference(value, "evidence reference")
    except LeviathanError:
        return False
    return True


def _is_public_verifier(value: str) -> bool:
    try:
        _public_verifier(value)
    except LeviathanError:
        return False
    return True


def _evidence_proven(
    value: Any,
    *,
    allowed_kinds: set[str],
    trust_anchors: dict[str, dict[str, Any]],
    subject: str,
    claim: str,
) -> bool:
    if not _evidence_valid(
        value,
        allowed_kinds=allowed_kinds,
        subject=subject,
        claim=claim,
    ):
        return False
    anchor = trust_anchors.get(value["verifier"])
    return bool(anchor and _verify_evidence_signature(value, anchor))


def _evidence_message(value: dict[str, Any]) -> bytes:
    return _canonical({
        "schema": value["schema"],
        "kind": value["kind"],
        "subject": value["subject"],
        "claim": value["claim"],
        "reference": value["reference"],
        "artifact_sha256": value["artifact_sha256"],
        "verifier": value["verifier"],
        "independent": value["independent"],
    })


def _validate_trust_anchor(value: Any) -> dict[str, Any]:
    if (
        not isinstance(value, dict)
        or set(value)
        != {
            "schema",
            "id",
            "algorithm",
            "modulus_hex",
            "exponent",
        }
        or value.get("schema") != "rapp-trust-anchor/1"
        or value.get("algorithm") != "rsa-sha256"
        or not isinstance(value.get("id"), str)
        or _public_verifier(value["id"]) != value["id"]
        or not isinstance(value.get("modulus_hex"), str)
        or not re.fullmatch(r"[0-9a-f]{512,}", value["modulus_hex"])
        or not isinstance(value.get("exponent"), int)
        or value["exponent"] != 65537
    ):
        raise LeviathanError("trust anchor is invalid")
    if int(value["modulus_hex"], 16).bit_length() < 2048:
        raise LeviathanError("trust anchor modulus is too small")
    return value


def _verify_evidence_signature(
    evidence: dict[str, Any],
    anchor: dict[str, Any],
) -> bool:
    try:
        modulus = int(anchor["modulus_hex"], 16)
        exponent = int(anchor["exponent"])
        signature = int(evidence["signature_hex"], 16)
    except (KeyError, TypeError, ValueError):
        return False
    width = (modulus.bit_length() + 7) // 8
    if signature >= modulus or width < 62:
        return False
    encoded = pow(signature, exponent, modulus).to_bytes(width, "big")
    digest = hashlib.sha256(_evidence_message(evidence)).digest()
    digest_info = bytes.fromhex(
        "3031300d060960864801650304020105000420"
    ) + digest
    padding_length = width - len(digest_info) - 3
    if padding_length < 8:
        return False
    expected = (
        b"\x00\x01"
        + b"\xff" * padding_length
        + b"\x00"
        + digest_info
    )
    return encoded == expected


def _required_evidence(
    value: Any,
    required: list[str],
    trust_anchors: dict[str, dict[str, Any]],
    subject: str,
) -> tuple[bool, list[str]]:
    if not isinstance(value, dict):
        return False, list(required)
    missing = [
        item
        for item in required
        if not _evidence_proven(
            value.get(item),
            allowed_kinds=REQUIRED_KINDS[item],
            trust_anchors=trust_anchors,
            subject=subject,
            claim=item,
        )
    ]
    return not missing, missing


def _validate_blueprint(value: dict[str, Any]) -> dict[str, Any]:
    required_root = {
        "schema",
        "protocol",
        "id",
        "name",
        "slug",
        "intent",
        "customer",
        "revenue_model",
        "classification",
        "organs",
        "planes",
        "end_to_end_loop",
        "loop_evidence",
        "boundary",
        "sha256",
    }
    if set(value) != required_root:
        raise LeviathanError("blueprint fields are invalid")
    if value.get("schema") != BLUEPRINT_SCHEMA:
        raise LeviathanError("blueprint identity is invalid")
    protocol = value.get("protocol")
    if protocol != {
        "schema": PROTOCOL_SCHEMA,
        "version": PROTOCOL["version"],
    }:
        raise LeviathanError("blueprint protocol identity is invalid")
    slug = value.get("slug")
    if not isinstance(slug, str) or not SLUG.fullmatch(slug):
        raise LeviathanError("blueprint slug is invalid")
    if value.get("id") != f"leviathan:{slug}":
        raise LeviathanError("blueprint id is invalid")
    _public_text(value.get("name"), "name", 120)
    _public_text(value.get("intent"), "intent", 4000)
    _public_text(value.get("customer"), "customer", 1000)
    _public_text(
        value.get("revenue_model"),
        "revenue model",
        1000,
    )
    if value.get("classification") != "public-safe-blueprint":
        raise LeviathanError("blueprint classification is invalid")
    organs = value.get("organs")
    if not isinstance(organs, dict) or set(organs) != set(ORGANS):
        raise LeviathanError("blueprint organs are invalid")
    for name, item in organs.items():
        if (
            not isinstance(item, dict)
            or set(item)
            != {
                "status",
                "purpose",
                "design",
                "evidence_required",
                "evidence",
            }
            or item.get("status")
            not in {"planned", "implemented", "proven"}
            or item.get("purpose") != ORGANS[name]["purpose"]
            or item.get("evidence_required")
            != ORGANS[name]["required_evidence"]
            or not isinstance(item.get("design"), list)
            or not all(
                isinstance(line, str)
                and bool(_public_text(line, f"{name} design", 1000))
                for line in item["design"]
            )
            or not isinstance(item.get("evidence"), dict)
            or not set(item["evidence"]) <= set(
                ORGANS[name]["required_evidence"]
            )
            or not all(
                _evidence_valid(
                    record,
                    allowed_kinds=REQUIRED_KINDS[label],
                    subject=value["id"],
                    claim=label,
                )
                for label, record in item["evidence"].items()
            )
        ):
            raise LeviathanError(f"{name} organ is invalid")
    planes = value.get("planes")
    if not isinstance(planes, dict) or set(planes) != set(PLANES):
        raise LeviathanError("blueprint planes are invalid")
    for name, item in planes.items():
        if (
            not isinstance(item, dict)
            or set(item)
            != {
                "status",
                "purpose",
                "endpoint_or_surface",
                "evidence_required",
                "evidence",
            }
            or item.get("status")
            not in {"planned", "implemented", "proven"}
            or item.get("purpose") != PLANES[name]
            or (
                item.get("endpoint_or_surface") is not None
                and (
                    not isinstance(item["endpoint_or_surface"], str)
                    or not _public_surface(
                        item["endpoint_or_surface"],
                        f"{name} endpoint",
                    )
                )
            )
            or item.get("evidence_required") != PLANE_EVIDENCE[name]
            or not isinstance(item.get("evidence"), dict)
            or not set(item["evidence"]) <= set(PLANE_EVIDENCE[name])
            or not all(
                _evidence_valid(
                    record,
                    allowed_kinds=REQUIRED_KINDS[label],
                    subject=value["id"],
                    claim=label,
                )
                for label, record in item["evidence"].items()
            )
        ):
            raise LeviathanError(f"{name} plane is invalid")
    if value.get("end_to_end_loop") != LOOP_STEPS:
        raise LeviathanError("blueprint end-to-end loop is invalid")
    if (
        not isinstance(value.get("loop_evidence"), dict)
        or not set(value["loop_evidence"]) <= set(LOOP_STEPS)
        or not all(
            _evidence_valid(
                record,
                allowed_kinds=REQUIRED_KINDS[label],
                subject=value["id"],
                claim=label,
            )
            for label, record in value["loop_evidence"].items()
        )
    ):
        raise LeviathanError("blueprint loop evidence is invalid")
    if value.get("boundary") != PUBLIC_PRIVATE_BOUNDARY:
        raise LeviathanError("blueprint public/private boundary is invalid")
    stable = {key: item for key, item in value.items() if key != "sha256"}
    if value.get("sha256") != _digest(stable):
        raise LeviathanError("blueprint digest is invalid")
    return value


def assess(
    value: dict[str, Any],
    trust_anchors: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    _validate_blueprint(value)
    anchors = {
        anchor["id"]: anchor
        for anchor in (
            _validate_trust_anchor(item)
            for item in (trust_anchors or [])
        )
    }
    organs = value.get("organs")
    planes = value.get("planes")
    if not isinstance(organs, dict) or not isinstance(planes, dict):
        raise LeviathanError(
            "architecture must contain organs and planes objects"
        )
    organ_results = {}
    for name in ORGANS:
        item = organs.get(name)
        present = isinstance(item, dict) and item.get("status") in {
            "implemented",
            "proven",
        }
        proven_evidence, missing_evidence = _required_evidence(
            item.get("evidence"),
            ORGANS[name]["required_evidence"],
            anchors,
            value["id"],
        )
        proven = present and proven_evidence
        organ_results[name] = {
            "present": present,
            "proven": proven,
            "missing_evidence": (
                []
                if proven
                else missing_evidence
                or ORGANS[name]["required_evidence"]
            ),
        }
    plane_results = {}
    for name in PLANES:
        item = planes.get(name)
        present = (
            isinstance(item, dict)
            and item.get("status") in {"implemented", "proven"}
            and isinstance(item.get("endpoint_or_surface"), str)
            and bool(item["endpoint_or_surface"])
        )
        proven_evidence, missing_evidence = _required_evidence(
            item.get("evidence"),
            PLANE_EVIDENCE[name],
            anchors,
            value["id"],
        )
        plane_results[name] = {
            "present": present,
            "proven": present and proven_evidence,
            "missing_evidence": (
                []
                if present and proven_evidence
                else missing_evidence or PLANE_EVIDENCE[name]
            ),
        }
    missing_organs = [
        name
        for name, result in organ_results.items()
        if not result["proven"]
    ]
    missing_planes = [
        name
        for name, result in plane_results.items()
        if not result["proven"]
    ]
    loop_proven, missing_loop = _required_evidence(
        value.get("loop_evidence"),
        LOOP_STEPS,
        anchors,
        value["id"],
    )
    full = not missing_organs and not missing_planes and loop_proven
    return {
        "schema": ASSESSMENT_SCHEMA,
        "protocol_version": PROTOCOL["version"],
        "classification": "full" if full else "partial",
        "full_leviathan": full,
        "organs": organ_results,
        "planes": plane_results,
        "missing_organs": missing_organs,
        "missing_planes": missing_planes,
        "loop_proven": loop_proven,
        "missing_loop_evidence": missing_loop,
        "trust_anchors": sorted(anchors),
        "conformance_basis": (
            "trusted-independent-evidence"
            if anchors
            else "no-trust-anchors"
        ),
        "limitations": PROTOCOL["conformance"]["not_implied"],
    }


def _read_blueprint(slug: str) -> dict[str, Any]:
    path = _workspace(slug) / "leviathan.json"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise LeviathanError("materialized Leviathan was not found") from error
    except (OSError, UnicodeError, ValueError) as error:
        raise LeviathanError(
            f"cannot read materialized Leviathan: {error}"
        ) from error
    return _validate_blueprint(value)


def materialize(value: dict[str, Any]) -> dict[str, Any]:
    _validate_blueprint(value)
    slug = value["slug"]
    workspace = _workspace(slug)
    workspace.mkdir(parents=True, exist_ok=True)
    path = workspace / "leviathan.json"
    try:
        _exclusive_json(path, value)
    except FileExistsError:
        current = _read_blueprint(slug)
        if current != value:
            raise LeviathanError(
                "materialized Leviathan already exists with drift"
            )
    protocol_path = workspace / "protocol.json"
    _atomic_json(protocol_path, PROTOCOL)
    readme = (
        f"# {value['name']}\n\n"
        f"Protocol: `{PROTOCOL_SCHEMA}` version `{PROTOCOL['version']}`\n\n"
        f"Intent: {value['intent']}\n\n"
        f"Customer: {value['customer']}\n\n"
        "This is a public-safe protocol blueprint. It is not a production "
        "deployment and contains no private implementation or customer data.\n"
    )
    (workspace / "README.md").write_text(readme, encoding="utf-8")
    return {
        "workspace": str(workspace),
        "blueprint": str(path),
        "protocol": str(protocol_path),
        "sha256": value["sha256"],
    }


class FullRappLeviathanAgent(BasicAgent):
    def __init__(self):
        self.name = "FullRappLeviathan"
        self.metadata = {
            "name": self.name,
            "description": (
                "Compile and assess Full RAPP Leviathan protocol blueprints. "
                "Use for governed agent businesses with Brainstem intelligence, "
                "private execution, evidence, memory, and commerce."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "protocol",
                            "assess",
                            "blueprint",
                            "materialize",
                            "inspect",
                            "list",
                        ],
                    },
                    "name": {"type": "string"},
                    "intent": {"type": "string"},
                    "customer": {"type": "string"},
                    "revenue_model": {"type": "string"},
                    "architecture_json": {"type": "string"},
                    "blueprint_json": {"type": "string"},
                    "trust_anchors_json": {
                        "type": "string",
                        "description": (
                            "JSON array of RSA-SHA256 public trust-anchor "
                            "objects for this assessment."
                        ),
                    },
                },
                "required": ["operation"],
                "additionalProperties": False,
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(
        self,
        operation="protocol",
        name="",
        intent="",
        customer="",
        revenue_model="subscription plus paid agent calls",
        architecture_json="",
        blueprint_json="",
        trust_anchors_json="",
        **kwargs,
    ):
        try:
            trust_anchors = []
            if trust_anchors_json:
                trust_anchors = json.loads(trust_anchors_json)
                if (
                    not isinstance(trust_anchors, list)
                    or not all(
                        isinstance(item, dict)
                        for item in trust_anchors
                    )
                ):
                    raise LeviathanError(
                        "trust_anchors_json must contain an object array"
                    )
            if operation == "protocol":
                result: Any = PROTOCOL
            elif operation == "assess":
                result = assess(
                    _object(architecture_json, "architecture_json"),
                    trust_anchors,
                )
            elif operation == "blueprint":
                result = blueprint(
                    name=name,
                    intent=intent,
                    customer=customer,
                    revenue_model=revenue_model,
                )
            elif operation == "materialize":
                value = (
                    _object(blueprint_json, "blueprint_json")
                    if blueprint_json
                    else blueprint(
                        name=name,
                        intent=intent,
                        customer=customer,
                        revenue_model=revenue_model,
                    )
                )
                result = materialize(value)
            elif operation == "inspect":
                value = _read_blueprint(_slug(name))
                result = {
                    "blueprint": value,
                    "assessment": assess(value, trust_anchors),
                }
            elif operation == "list":
                result = []
                if WORKSPACE.exists():
                    for path in sorted(WORKSPACE.iterdir()):
                        if not path.is_dir():
                            continue
                        try:
                            value = _read_blueprint(path.name)
                        except LeviathanError:
                            continue
                        result.append({
                            "slug": value["slug"],
                            "name": value["name"],
                            "sha256": value["sha256"],
                            "workspace": str(path),
                        })
            else:
                raise LeviathanError("unsupported operation")
            return json.dumps({
                "status": "ok",
                "operation": operation,
                "result": result,
            }, indent=2)
        except (LeviathanError, OSError, UnicodeError, ValueError) as error:
            return json.dumps({
                "status": "error",
                "operation": operation,
                "error": str(error),
            })


if __name__ == "__main__":
    agent = FullRappLeviathanAgent()
    print(agent.perform(operation="protocol"))
