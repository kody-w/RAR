---
name: "rar-kody-w-full-rapp-leviathan"
description: "Compile and assess Full RAPP Leviathan protocol blueprints. Use for governed agent businesses with Brainstem intelligence, private execution, evidence, memory, and commerce."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/full_rapp_leviathan", "rar_sha256": "78dac24c84eeca02f8e40144562d9ace2dd4da28b8fd7ca8f78b8b075feaad5a", "source_kind": "rar-agent", "source_commit": "0c4e7b86c53a71299a2fe1b65aaae320d3f68cfa", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "full_rapp_leviathan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/full-rapp-leviathan:2fc9be8794302bc94fb268508047a4bb6b0c84f5505d6c9b74af7213a62923cf", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["leviathan", "protocol", "brainstem", "foundry", "evidence", "commerce", "x402", "enterprise"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/full_rapp_leviathan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `full_rapp_leviathan_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
