---
name: "rar-kody-w-full-rapp-leviathan"
description: "Compile and assess Full RAPP Leviathan protocol blueprints. Use for governed agent businesses with Brainstem intelligence, private execution, evidence, memory, and commerce."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/full_rapp_leviathan", "rar_sha256": "78dac24c84eeca02f8e40144562d9ace2dd4da28b8fd7ca8f78b8b075feaad5a", "source_kind": "rar-agent", "source_commit": "0c4e7b86c53a71299a2fe1b65aaae320d3f68cfa", "version": "1.0.1", "author": "kody-w", "tags": ["leviathan", "protocol", "brainstem", "foundry", "evidence", "commerce", "x402", "enterprise"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/full_rapp_leviathan`. The original RAPP
agent is preserved byte-for-byte in `full_rapp_leviathan_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Full RAPP Leviathan

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "additionalProperties": false,
  "properties": {
    "architecture_json": {
      "type": "string"
    },
    "blueprint_json": {
      "type": "string"
    },
    "customer": {
      "type": "string"
    },
    "intent": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "protocol",
        "assess",
        "blueprint",
        "materialize",
        "inspect",
        "list"
      ],
      "type": "string"
    },
    "revenue_model": {
      "type": "string"
    },
    "trust_anchors_json": {
      "description": "JSON array of RSA-SHA256 public trust-anchor objects for this assessment.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `full_rapp_leviathan_agent.py` and embedded as the fenced Python below (sha256 78dac24c84eeca02…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `full_rapp_leviathan_agent.py` first:

```bash
python3 full_rapp_leviathan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 full_rapp_leviathan_agent.py   # or on stdin
python3 full_rapp_leviathan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
    "version": "1.0.1",
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
    "category": "core",
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


def _parse_ipv6(candidate: str):
    normalized = candidate.split("%", 1)[0]
    try:
        address = ipaddress.ip_address(normalized)
    except ValueError:
        return None
    return address if address.version == 6 else None


def _parse_legacy_ipv4_candidates(candidate: str):
    parts = candidate.lower().split(".")
    if not 1 <= len(parts) <= 4:
        return set()
    options = []
    for part in parts:
        try:
            if part.startswith("0x"):
                values = {int(part[2:], 16)}
            elif len(part) > 1 and part.startswith("0"):
                if not re.fullmatch(r"[0-9]+", part):
                    return set()
                values = {int(part, 10)}
                if re.fullmatch(r"0[0-7]+", part):
                    values.add(int(part, 8))
            elif re.fullmatch(r"[0-9]+", part):
                values = {int(part, 10)}
            else:
                return set()
        except ValueError:
            return set()
        options.append(values)

    limits = {
        1: (0xFFFFFFFF,),
        2: (0xFF, 0xFFFFFF),
        3: (0xFF, 0xFF, 0xFFFF),
        4: (0xFF, 0xFF, 0xFF, 0xFF),
    }[len(options)]
    combinations = [()]
    for values in options:
        combinations = [
            previous + (value,)
            for previous in combinations
            for value in values
        ]
    addresses = set()
    for values in combinations:
        if any(
            value > limit
            for value, limit in zip(values, limits)
        ):
            continue
        if len(values) == 1:
            packed = values[0]
        elif len(values) == 2:
            packed = (values[0] << 24) | values[1]
        elif len(values) == 3:
            packed = (
                (values[0] << 24)
                | (values[1] << 16)
                | values[2]
            )
        else:
            packed = (
                (values[0] << 24)
                | (values[1] << 16)
                | (values[2] << 8)
                | values[3]
            )
        addresses.add(ipaddress.ip_address(packed))
    return addresses


def _parse_legacy_ipv4(candidate: str):
    return next(
        iter(_parse_legacy_ipv4_candidates(candidate)),
        None,
    )


def _legacy_ipv4_addresses(value: str):
    pattern = re.compile(
        r"(?i)(?<![0-9a-z])"
        r"(?:0x[0-9a-f]+|[0-9]+)"
        r"(?:\.(?:0x[0-9a-f]+|[0-9]+)){0,3}"
        r"(?![0-9a-z])"
    )
    for match in pattern.finditer(value):
        candidate = match.group()
        addresses = _parse_legacy_ipv4_candidates(candidate)
        if (
            "." not in candidate
            and not candidate.lower().startswith("0x")
            and not any(
                int(address) >= (1 << 24)
                for address in addresses
            )
        ):
            continue
        for address in addresses:
            yield candidate, address


def _is_public_ip(address) -> bool:
    return bool(
        address.is_global
        and not address.is_private
        and not address.is_loopback
        and not address.is_link_local
        and not address.is_multicast
        and not address.is_reserved
        and not address.is_unspecified
        and not getattr(address, "is_site_local", False)
    )


def _validate_public_dns_hostname(hostname: str, label: str) -> None:
    if (
        len(hostname) > 253
        or hostname.endswith(".")
        or "." not in hostname
        or hostname == "localhost"
        or hostname.endswith((".local", ".internal", ".lan", ".home"))
        or hostname == "home.arpa"
        or hostname.endswith(".home.arpa")
        or _parse_legacy_ipv4(hostname) is not None
    ):
        raise LeviathanError(f"{label} contains an internal hostname")
    for part in hostname.split("."):
        if not re.fullmatch(
            r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?",
            part,
        ):
            raise LeviathanError(
                f"{label} contains an invalid public hostname"
            )


def _ipv6_addresses(value: str):
    seen = set()
    pattern = re.compile(
        r"(?i)[0-9a-f:.]+(?:%[0-9a-z_.-]+)?"
    )
    for match in pattern.finditer(value):
        raw = match.group()
        bracketed = (
            match.start() > 0
            and match.end() < len(value)
            and value[match.start() - 1] == "["
            and value[match.end()] == "]"
        )
        standalone_unspecified = (
            raw == "::"
            and (
                match.start() == 0
                or not (
                    value[match.start() - 1].isalnum()
                    or value[match.start() - 1] == "_"
                )
            )
            and (
                match.end() == len(value)
                or not (
                    value[match.end()].isalnum()
                    or value[match.end()] == "_"
                )
            )
        )
        if (
            raw.count(":") < 2
            or (
                not re.search(r"[0-9a-f]", raw, re.I)
                and not bracketed
                and not standalone_unspecified
            )
        ):
            continue
        trimmed = raw.rstrip(".,!?")
        full = _parse_ipv6(trimmed)
        embedded = (
            match.start() > 0
            and (
                value[match.start() - 1].isalnum()
                or value[match.start() - 1] == "_"
            )
        )
        if full is not None and not embedded:
            key = str(full)
            if key not in seen:
                seen.add(key)
                yield full
            continue

        boundaries = {0, len(trimmed)}
        for index, character in enumerate(trimmed):
            if character == ":":
                boundaries.update({index, index + 1})
        forms = set()
        ordered = sorted(boundaries)
        for position, start in enumerate(ordered):
            for end in ordered[position + 1:position + 22]:
                if end - start > 80:
                    break
                fragment = trimmed[start:end]
                forms.update({
                    fragment,
                    fragment.lstrip(":"),
                    fragment.rstrip(":"),
                    fragment.strip(":"),
                })
        for candidate in forms:
            if candidate.count(":") < 2:
                continue
            lowered = candidate.lower()
            if (
                not any(character.isdigit() for character in candidate)
                and not lowered.startswith(("fc", "fd", "fe"))
            ):
                continue
            address = _parse_ipv6(candidate)
            if address is None:
                continue
            key = str(address)
            if key not in seen:
                seen.add(key)
                yield address


def _public_text(
    value: Any,
    label: str,
    maximum: int,
    *,
    scan_ip_literals: bool = True,
) -> str:
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
    if scan_ip_literals:
        for candidate in re.findall(
            r"(?<![0-9])(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![0-9])",
            result,
        ):
            try:
                address = ipaddress.ip_address(candidate)
            except ValueError:
                continue
            if not _is_public_ip(address):
                raise LeviathanError(f"{label} contains private topology")
        for candidate, address in _legacy_ipv4_addresses(result):
            if candidate == str(address):
                continue
            if not _is_public_ip(address):
                raise LeviathanError(f"{label} contains private topology")
        for address in _ipv6_addresses(result):
            if not _is_public_ip(address):
                raise LeviathanError(f"{label} contains private topology")
    return result


def _public_surface(value: Any, label: str) -> str:
    result = _public_text(
        value,
        label,
        2000,
        scan_ip_literals=False,
    )
    if result.startswith("urn:rapp:surface:") and re.fullmatch(
        r"urn:rapp:surface:[a-z0-9][a-z0-9._-]{2,127}",
        result,
    ):
        return result
    if not result.lower().startswith(("http://", "https://")):
        raise LeviathanError(
            f"{label} must be a public HTTPS URL or RAPP surface URN"
        )
    if "\\" in result or any(
        ord(character) < 32 or ord(character) == 127
        for character in result
    ):
        raise LeviathanError(
            f"{label} URL cannot contain controls or backslashes"
        )
    parsed = urlsplit(result)
    if parsed.scheme != "https" or not parsed.hostname:
        raise LeviathanError(f"{label} must use a public HTTPS URL")
    if (
        "@" in parsed.netloc
        or "?" in result
        or "#" in result
        or parsed.netloc.endswith(":")
    ):
        raise LeviathanError(
            f"{label} URL contains an empty or forbidden component"
        )
    authority = parsed.netloc
    if authority.startswith("[") and not re.fullmatch(
        r"\[[0-9a-fA-F:.]+\](?::[0-9]+)?",
        authority,
    ):
        raise LeviathanError(
            f"{label} URL contains an unsupported bracketed host"
        )
    if "%" in parsed.netloc:
        raise LeviathanError(
            f"{label} URL hostname cannot contain percent escapes"
        )
    try:
        parsed.netloc.encode("ascii")
    except UnicodeEncodeError as error:
        raise LeviathanError(
            f"{label} URL authority must use ASCII or punycode"
        ) from error
    try:
        parsed.port
    except ValueError as error:
        raise LeviathanError(
            f"{label} URL contains an invalid port"
        ) from error
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
        if not _is_public_ip(address):
            raise LeviathanError(
                f"{label} contains a non-public IP address"
            )
        return result
    if _parse_legacy_ipv4(hostname) is not None:
        raise LeviathanError(f"{label} contains a numeric private host")
    if re.fullmatch(r"(?:0x[0-9a-f]+|[0-9.]+)", hostname):
        raise LeviathanError(f"{label} contains a numeric private host")
    _validate_public_dns_hostname(hostname, label)
    return result


def _public_reference(value: Any, label: str) -> str:
    result = _public_text(
        value,
        label,
        2000,
        scan_ip_literals=False,
    )
    if re.fullmatch(r"urn:sha256:[0-9a-f]{64}", result):
        return result
    return _public_surface(result, label)


def _public_verifier(value: Any) -> str:
    result = _public_text(
        value,
        "verifier",
        1000,
        scan_ip_literals=False,
    )
    if re.fullmatch(r"did:key:[A-Za-z0-9._-]+", result):
        return result
    if re.fullmatch(r"did:web:[A-Za-z0-9.-]+", result):
        hostname = result.removeprefix("did:web:")
        _validate_public_dns_hostname(hostname.lower(), "verifier")
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
        and value["reference"] == value["reference"].strip()
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
