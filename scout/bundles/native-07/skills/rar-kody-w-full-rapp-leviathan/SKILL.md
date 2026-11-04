---
name: "rar-kody-w-full-rapp-leviathan"
description: "Compile and assess Full RAPP Leviathan protocol blueprints. Use for governed agent businesses with Brainstem intelligence, private execution, evidence, memory, and commerce."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/full_rapp_leviathan", "rar_sha256": "5f9093cc6020d9e24ec906d7dd16483ec159b06b33bb26bfcb9c2f2a1edb3fef", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["leviathan", "protocol", "brainstem", "foundry", "evidence", "commerce", "x402", "enterprise"]}
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
