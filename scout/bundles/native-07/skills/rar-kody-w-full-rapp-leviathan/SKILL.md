---
name: "rar-kody-w-full-rapp-leviathan"
description: "Compile and assess Full RAPP Leviathan protocol blueprints. Use for governed agent businesses with Brainstem intelligence, private execution, evidence, memory, and commerce."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/full_rapp_leviathan", "rar_sha256": "5f9093cc6020d9e24ec906d7dd16483ec159b06b33bb26bfcb9c2f2a1edb3fef", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["leviathan", "protocol", "brainstem", "foundry", "evidence", "commerce", "x402", "enterprise"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `full_rapp_leviathan_agent.py` and embedded as the fenced Python below (sha256 5f9093cc6020d9e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `full_rapp_leviathan_agent.py` first:

```bash
python3 full_rapp_leviathan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 full_rapp_leviathan_agent.py   # or on stdin
python3 full_rapp_leviathan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/full_rapp_leviathan_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/full_rapp_leviathan_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/full_rapp_leviathan/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
