---
name: "rar-kody-w-rapp-projects"
description: "Coordinates local-first projects through strict RAPP/1 work chains, verified derived boards, artifact receipts, and deterministic eggs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_projects", "rar_sha256": "e994af96f664097a291b4a1446ba8b8e36e911d7ccacd5aa58d984f64fb3afca", "source_kind": "rar-agent", "source_commit": "a3391b199669c48572aabdab2087b8c6733f0964", "version": "1.0.3", "author": "kody-w", "tags": ["rapp-1", "project-management", "local-first", "rapplication", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rapp_projects`. The original RAPP
agent is preserved byte-for-byte in `rapp_projects_agent.py` and in the RCI capsule.

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

RappProjects — local-first, interoperable project control in one agent.

RappProjects gives humans and AI runtimes one shared, append-only project
record without a server, account, database, or project-specific integration.
Each project is a strict unsigned off-swarm RAPP/1 stream.  Project chains are
authoritative; ``BOARD.md``, ``CATCHUP.md``, ``index.json``, and per-project
``STATUS.md`` files are disposable views rebuilt only from verified chains.

Operations
==========

``protocol``
    Return the embedded public protocol and parameter contract.
``open``
    Create a project and its ``project.genesis`` frame.
``punchin``
    Record an AI or human runtime beginning work.
``status``
    Record progress, blockers, next action, and file artifact receipts.
``handoff``
    Record a handoff whose document is hashed, never copied.
``punchout``
    Record a done, blocked, or abandoned outcome and file receipts.
``verify``
    Verify the complete chain and receipts, optionally bind owner-approved
    imported receipt tokens, then append ``project.verify``.
``board``
    Rebuild and return the cross-project board.
``inspect``
    Return one project's verified identity, cell, state, and receipt status.
``export``
    With ``owner_approved=true``, create a deterministic local-private
    ``rapp/1-egg`` rapplication ZIP containing project metadata only.
``import``
    Verify an entire project egg before creating or fast-forwarding a project;
    stale or divergent histories are refused without mutation.

The storage root is selected in this order: explicit ``root`` argument,
``RAPP_PROJECTS_ROOT``, then ``~/.rapp/projects-control``.  State is never
written beside this agent.  The implementation uses only Python's standard
library plus the required ``BasicAgent`` base dependency. External receipt
paths stay in private locator metadata under that root and never enter eggs;
an imported token can be rebound only to owner-approved matching bytes.
Minting a root requires ``identity_owner`` or ``RAPP_PROJECTS_OWNER`` so every
RAPPID names the operator's lowercase GitHub owner rather than a synthetic
namespace. Fsynced journals recover interrupted root, project, import, and head
updates without rewriting historical frames.

Standalone use accepts one JSON object as a Python argv value or on stdin.
Run the file with ``--tool`` to print its callable operation schema. Supply
``operation``; ``action`` is a compatibility alias, and omission is refused.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "additionalProperties": false,
  "anyOf": [
    {
      "required": [
        "operation"
      ]
    },
    {
      "required": [
        "action"
      ]
    }
  ],
  "properties": {
    "action": {
      "description": "Compatibility alias for operation; operation takes precedence.",
      "enum": [
        "protocol",
        "open",
        "punchin",
        "status",
        "handoff",
        "punchout",
        "verify",
        "board",
        "inspect",
        "export",
        "import"
      ],
      "type": "string"
    },
    "agent": {
      "type": "string"
    },
    "artifacts": {
      "type": "array"
    },
    "blockers": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "capabilities": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "doc": {
      "type": "string"
    },
    "egg": {
      "type": "string"
    },
    "from_agent": {
      "type": "string"
    },
    "goal": {
      "type": "string"
    },
    "identity_owner": {
      "description": "Lowercase GitHub login used only when minting a new root.",
      "type": "string"
    },
    "intent": {
      "type": "string"
    },
    "location": {
      "type": "string"
    },
    "next_action": {
      "type": "string"
    },
    "open_questions": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "operation": {
      "enum": [
        "protocol",
        "open",
        "punchin",
        "status",
        "handoff",
        "punchout",
        "verify",
        "board",
        "inspect",
        "export",
        "import"
      ],
      "type": "string"
    },
    "origin": {
      "type": "string"
    },
    "outcome": {
      "enum": [
        "done",
        "blocked",
        "abandoned"
      ],
      "type": "string"
    },
    "output": {
      "type": "string"
    },
    "owner": {
      "type": "string"
    },
    "owner_approved": {
      "type": "boolean"
    },
    "pct": {
      "maximum": 100,
      "minimum": 0,
      "type": "integer"
    },
    "project": {
      "type": "string"
    },
    "project_state": {
      "enum": [
        "active",
        "blocked",
        "done",
        "parked"
      ],
      "type": "string"
    },
    "receipt_bindings": {
      "additionalProperties": {
        "type": "string"
      },
      "type": "object"
    },
    "receipts": {
      "type": "array"
    },
    "role": {
      "type": "string"
    },
    "root": {
      "type": "string"
    },
    "runtime": {
      "type": "string"
    },
    "session_id": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "summary": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "to_agent": {
      "type": "string"
    }
  },
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_projects_agent.py` and embedded as the fenced Python below (sha256 e994af96f664097a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_projects_agent.py` first:

```bash
python3 rapp_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_projects_agent.py   # or on stdin
python3 rapp_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""RappProjects — local-first, interoperable project control in one agent.

RappProjects gives humans and AI runtimes one shared, append-only project
record without a server, account, database, or project-specific integration.
Each project is a strict unsigned off-swarm RAPP/1 stream.  Project chains are
authoritative; ``BOARD.md``, ``CATCHUP.md``, ``index.json``, and per-project
``STATUS.md`` files are disposable views rebuilt only from verified chains.

Operations
==========

``protocol``
    Return the embedded public protocol and parameter contract.
``open``
    Create a project and its ``project.genesis`` frame.
``punchin``
    Record an AI or human runtime beginning work.
``status``
    Record progress, blockers, next action, and file artifact receipts.
``handoff``
    Record a handoff whose document is hashed, never copied.
``punchout``
    Record a done, blocked, or abandoned outcome and file receipts.
``verify``
    Verify the complete chain and receipts, optionally bind owner-approved
    imported receipt tokens, then append ``project.verify``.
``board``
    Rebuild and return the cross-project board.
``inspect``
    Return one project's verified identity, cell, state, and receipt status.
``export``
    With ``owner_approved=true``, create a deterministic local-private
    ``rapp/1-egg`` rapplication ZIP containing project metadata only.
``import``
    Verify an entire project egg before creating or fast-forwarding a project;
    stale or divergent histories are refused without mutation.

The storage root is selected in this order: explicit ``root`` argument,
``RAPP_PROJECTS_ROOT``, then ``~/.rapp/projects-control``.  State is never
written beside this agent.  The implementation uses only Python's standard
library plus the required ``BasicAgent`` base dependency. External receipt
paths stay in private locator metadata under that root and never enter eggs;
an imported token can be rebound only to owner-approved matching bytes.
Minting a root requires ``identity_owner`` or ``RAPP_PROJECTS_OWNER`` so every
RAPPID names the operator's lowercase GitHub owner rather than a synthetic
namespace. Fsynced journals recover interrupted root, project, import, and head
updates without rewriting historical frames.

Standalone use accepts one JSON object as a Python argv value or on stdin.
Run the file with ``--tool`` to print its callable operation schema. Supply
``operation``; ``action`` is a compatibility alias, and omission is refused.
"""

from __future__ import annotations

import base64
import hashlib
import io
import json
import math
import os
import re
import secrets
import shutil
import struct
import sys
import threading
import time
import unicodedata
import uuid
import zipfile
import zlib
from datetime import datetime, timezone
from contextlib import contextmanager
from decimal import Decimal, InvalidOperation
from pathlib import Path, PureWindowsPath
from typing import Any

try:
    from agents.basic_agent import BasicAgent
except (ImportError, ModuleNotFoundError):
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name = name
            self.metadata = metadata or {}


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rapp_projects",
    "version": "1.0.3",
    "display_name": "RappProjects",
    "description": (
        "Coordinates local-first projects through strict RAPP/1 work chains, "
        "verified derived boards, artifact receipts, and deterministic eggs."
    ),
    "author": "kody-w",
    "tags": [
        "rapp-1",
        "project-management",
        "local-first",
        "rapplication",
        "productivity",
    ],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


SPEC = "rapp/1"
VISIBILITY = "local-private"
CELL_SCHEMA = "rapp-cell/1.0"
EGG_SCHEMA = "rapp/1-egg"
EGG_VARIANT = "rapplication"
EXPORT_SCHEMA = "rapp-project-export/1"
INDEX_SCHEMA = "rapp-projects/index/1"
IDENTITY_SCHEMA = "rapp/1"
HEAD_SCHEMA = "rapp-project-head/2"
LEGACY_HEAD_SCHEMA = "rapp-project-head/1"
RECEIPT_SCHEMA = "rapp-artifact-receipt/1"
RECEIPT_LOCATORS_SCHEMA = "rapp-receipt-locators/1"
ROOT_INIT_SCHEMA = "rapp-project-root-init/1"
PROJECT_TRANSACTION_SCHEMA = "rapp-project-transaction/1"
APPEND_TRANSACTION_SCHEMA = "rapp-append-transaction/1"
ROOT_LINEAGE_SCHEMA = "rapp-project-lineage/1"
PROJECT_LINEAGE_SCHEMA = "rapp-project-lineage/1"
SESSION_ID_FIELD = "session_id"
EGG_WARNING = (
    "Local-private project metadata export created only with explicit owner "
    "approval; it contains no artifact bodies."
)

OPERATION_SCHEMA_VALUES = [
    "protocol",
    "open",
    "punchin",
    "status",
    "handoff",
    "punchout",
    "verify",
    "board",
    "inspect",
    "export",
    "import",
]
OPERATIONS = tuple(OPERATION_SCHEMA_VALUES)
AGENT_PARAMETERS = {
    "type": "object",
    "properties": {
        "operation": {"type": "string", "enum": OPERATION_SCHEMA_VALUES},
        "action": {
            "type": "string",
            "enum": OPERATION_SCHEMA_VALUES,
            "description": (
                "Compatibility alias for operation; operation takes precedence."
            ),
        },
        "root": {"type": "string"},
        "identity_owner": {
            "type": "string",
            "description": (
                "Lowercase GitHub login used only when minting a new root."
            ),
        },
        "project": {"type": "string"},
        "title": {"type": "string"},
        "goal": {"type": "string"},
        "owner": {"type": "string"},
        "origin": {"type": "string"},
        "agent": {"type": "string"},
        "runtime": {"type": "string"},
        "session_id": {"type": "string"},
        "location": {"type": "string"},
        "intent": {"type": "string"},
        "role": {"type": "string"},
        "capabilities": {
            "type": "array",
            "items": {"type": "string"},
        },
        "status": {"type": "string"},
        "artifacts": {"type": "array"},
        "blockers": {
            "type": "array",
            "items": {"type": "string"},
        },
        "next_action": {"type": "string"},
        "pct": {"type": "integer", "minimum": 0, "maximum": 100},
        "project_state": {
            "type": "string",
            "enum": ["active", "blocked", "done", "parked"],
        },
        "from_agent": {"type": "string"},
        "to_agent": {"type": "string"},
        "doc": {"type": "string"},
        "open_questions": {
            "type": "array",
            "items": {"type": "string"},
        },
        "outcome": {
            "type": "string",
            "enum": ["done", "blocked", "abandoned"],
        },
        "receipts": {"type": "array"},
        "receipt_bindings": {
            "type": "object",
            "additionalProperties": {"type": "string"},
        },
        "summary": {"type": "string"},
        "egg": {"type": "string"},
        "output": {"type": "string"},
        "owner_approved": {"type": "boolean"},
    },
    "anyOf": [
        {"required": ["operation"]},
        {"required": ["action"]},
    ],
    "additionalProperties": False,
}
AGENT_METADATA = {
    "name": "RappProjects",
    "display_name": "RappProjects",
    "description": (
        "Coordinates local-first projects through strict RAPP/1 work chains, "
        "verified derived boards, artifact receipts, and deterministic eggs."
    ),
    "parameters": AGENT_PARAMETERS,
}
FRAME_KEYS = frozenset(
    {
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
)
FRAME_KINDS = frozenset(
    {
        "project.genesis",
        "work.punchin",
        "work.status",
        "work.handoff",
        "work.punchout",
        "project.verify",
    }
)
CELL_KEYS = frozenset(
    {"schema", "layer", "path", "context", "children", "souls"}
)
IDENTITY_KEYS = frozenset(
    {"schema", "rappid", "kind", "name", "visibility"}
)
HEAD_KEYS = frozenset(
    {"schema", "stream_id", "seq", "frame_hash", "chain_hash"}
)
LEGACY_HEAD_KEYS = frozenset({"schema", "stream_id", "seq", "frame_hash"})
RECEIPT_KEYS = frozenset(
    {"schema", "path", "exists", "type", "size", "sha256"}
)
EGG_KEYS = frozenset(
    {"schema", "variant", "rappid", "created_utc", "contents", "payload", "sig"}
)
EXPORT_PAYLOAD_KEYS = frozenset(
    {
        "schema",
        "project",
        "stream_id",
        "visibility",
        "frame_count",
        "head_frame_hash",
        "content",
        "warning",
    }
)

MAX_CANONICAL_BYTES = 1024 * 1024
MAX_DEPTH = 64
MAX_CHAIN_BYTES = 64 * 1024 * 1024
MAX_EGG_BYTES = 64 * 1024 * 1024
MAX_EGG_ENTRIES = 16
MAX_LIST_ITEMS = 256
MAX_ERROR_CHARS = 500
MAX_SAFE_INTEGER = 2**53 - 1
ACTIVE_STALE_HOURS = 4
IDLE_STALE_HOURS = 24

LCLABEL = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SLUG = LCLABEL
KIND = re.compile(
    r"^[a-z0-9]+(?:-[a-z0-9]+)*"
    r"\.[a-z0-9]+(?:-[a-z0-9]+)*$"
)
HEX64 = re.compile(r"^[0-9a-f]{64}$")
LOCATOR_TOKEN = re.compile(r"^[0-9a-f]{32}$")
STAGING_NAME = re.compile(
    r"^\.staging-([a-z0-9]+(?:-[a-z0-9]+)*)-([0-9a-f]{32})$"
)
UTC = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$")
RAPPID = re.compile(
    r"^rappid:@"
    r"([a-z0-9]+(?:-[a-z0-9]+)*)"
    r"/"
    r"([a-z0-9]+(?:-[a-z0-9]+)*)"
    r":([0-9a-f]{64})$"
)
INSTANCE = LCLABEL
WINDOWS_RESERVED = frozenset(
    {"con", "prn", "aux", "nul"}
    | {f"com{number}" for number in range(1, 10)}
    | {f"lpt{number}" for number in range(1, 10)}
)
PROJECT_MANAGED_FILES = frozenset(
    {
        ".chain.lock",
        ".append-transaction.json",
        ".receipt-locators.json",
        "PROJECT.egg",
        "STATUS.md",
        "chain.jsonl",
        "head.json",
        "lineage.json",
        "manifest.json",
        "rappid.json",
    }
)
ROOT_MANAGED_FILES = frozenset(
    {
        ".project-transaction.json",
        ".projects.lock",
        ".root-init.json",
        ".views.lock",
        "BOARD.md",
        "CATCHUP.md",
        "index.json",
        "lineage.json",
        "manifest.json",
        "rappid.json",
    }
)
PROJECT_MANAGED_CASEFOLD = frozenset(
    name.casefold() for name in PROJECT_MANAGED_FILES
)
ROOT_MANAGED_CASEFOLD = frozenset(
    name.casefold() for name in ROOT_MANAGED_FILES
)
ABSOLUTE_PATH = re.compile(
    r"(?<![A-Za-z0-9+.\-:/])/(?!/)[^\s`\"'<>|]*"
    r"|\b[A-Za-z]:[\\/][^\s`\"'<>|]*",
    re.IGNORECASE,
)

_PROCESS_LOCK = threading.RLock()
_AGENT_DIRECTORY = Path(__file__).resolve().parent

_PAYLOAD_SCHEMAS = {
    "project.genesis": {
        "required": {"project", "title", "goal", "owner", "origin", "visibility"},
        "optional": set(),
    },
    "work.punchin": {
        "required": {
            "project",
            "agent",
            "runtime",
            "session_id",
            "location",
            "intent",
            "role",
            "capabilities",
        },
        "optional": set(),
    },
    "work.status": {
        "required": {
            "project",
            "agent",
            "location",
            "status",
            "artifacts",
            "blockers",
            "next_action",
            "pct",
        },
        "optional": {"project_state"},
    },
    "work.handoff": {
        "required": {
            "project",
            "from_agent",
            "to_agent",
            "doc",
            "open_questions",
        },
        "optional": set(),
    },
    "work.punchout": {
        "required": {
            "project",
            "agent",
            "outcome",
            "receipts",
            "summary",
            "blockers",
        },
        "optional": set(),
    },
    "project.verify": {
        "required": {
            "project",
            "verdict",
            "broken_receipts",
            "verified_frames",
            "head_frame_hash",
        },
        "optional": set(),
    },
}


class RappProjectsError(ValueError):
    """Base refusal for invalid or unsafe project operations."""

    code = "project-error"


class ChainVerificationError(RappProjectsError):
    """Raised when a project chain cannot be trusted."""

    code = "chain-verification"


class DivergentChainError(RappProjectsError):
    """Raised instead of guessing how two histories should merge."""

    code = "divergent-chain"


class EggVerificationError(RappProjectsError):
    """Raised when any integrity or viability egg check fails."""

    code = "egg-verification"


class FrameVerificationError(ChainVerificationError):
    """A RAPP/1 verification refusal annotated with its normative step."""

    def __init__(self, step: str, reason: str):
        self.step = step
        self.reason = reason
        super().__init__(f"RAPP/1 step {step}: {reason}")


class CommittedFrame(dict):
    """Exact frame mapping plus out-of-band storage warnings."""

    def __init__(
        self,
        frame: dict[str, Any],
        storage_warnings: list[dict[str, str]] | None = None,
    ):
        super().__init__(frame)
        self.storage_warnings = list(storage_warnings or [])


def _has_surrogate(value: str) -> bool:
    return any(0xD800 <= ord(character) <= 0xDFFF for character in value)


def _string(value: Any, field: str, limit: int, default: str | None = None) -> str:
    if value is None:
        if default is None:
            raise RappProjectsError(f"{field} is required")
        value = default
    if not isinstance(value, str):
        raise RappProjectsError(f"{field} must be a string")
    if _has_surrogate(value):
        raise RappProjectsError(f"{field} contains an unpaired surrogate")
    value = unicodedata.normalize("NFC", value)
    if len(value) > limit:
        raise RappProjectsError(f"{field} exceeds {limit} characters")
    return value


def _string_list(
    value: Any,
    field: str,
    *,
    item_limit: int = 500,
    default: tuple[str, ...] = (),
) -> list[str]:
    if value is None:
        value = list(default)
    elif not isinstance(value, list):
        value = [value]
    if len(value) > MAX_LIST_ITEMS:
        raise RappProjectsError(f"{field} has too many items")
    return [
        _string(item, f"{field}[{index}]", item_limit, "")
        for index, item in enumerate(value)
    ]


def _serialize_binary64(value: float) -> str:
    """Serialize one finite binary64 value as ECMAScript Number::toString."""
    if not math.isfinite(value):
        raise RappProjectsError("non-finite numbers are outside I-JSON")
    if value == 0:
        return "0"
    negative = value < 0
    text = repr(abs(value)).lower()
    if "e" in text:
        mantissa, exponent_text = text.split("e", 1)
        exponent = int(exponent_text)
    else:
        mantissa, exponent = text, 0
    if "." in mantissa:
        integer, fraction = mantissa.split(".", 1)
        digits = integer + fraction
        decimal_position = len(integer) + exponent
    else:
        digits = mantissa
        decimal_position = len(mantissa) + exponent
    leading_zeroes = len(digits) - len(digits.lstrip("0"))
    digits = digits.lstrip("0") or "0"
    decimal_position -= leading_zeroes
    digits = digits.rstrip("0") or "0"
    magnitude = abs(value)
    if 1e-6 <= magnitude < 1e21:
        if decimal_position <= 0:
            rendered = "0." + ("0" * -decimal_position) + digits
        elif decimal_position >= len(digits):
            rendered = digits + ("0" * (decimal_position - len(digits)))
        else:
            rendered = digits[:decimal_position] + "." + digits[decimal_position:]
    else:
        exponent = decimal_position - 1
        rendered = digits[0]
        if len(digits) > 1:
            rendered += "." + digits[1:]
        rendered += "e" + ("+" if exponent >= 0 else "") + str(exponent)
    return ("-" if negative else "") + rendered


def _number_roundtrips(token: str) -> float:
    try:
        original = Decimal(token)
        value = float(token)
        rendered = _serialize_binary64(value)
        roundtrip = Decimal(rendered)
    except (InvalidOperation, OverflowError, ValueError) as exc:
        raise RappProjectsError("number is outside the I-JSON binary64 domain") from exc
    if not math.isfinite(value) or original != roundtrip:
        raise RappProjectsError("number does not survive the binary64 round-trip")
    return value


def _parse_int(token: str) -> int:
    _number_roundtrips(token)
    return int(token)


def _parse_float(token: str) -> float:
    return _number_roundtrips(token)


def _object_from_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, child in pairs:
        if key in value:
            raise RappProjectsError(f"duplicate JSON member: {key}")
        value[key] = child
    return value


def _strict_loads(data: str | bytes, *, limit: int = MAX_CANONICAL_BYTES) -> Any:
    if isinstance(data, bytes):
        if len(data) > limit:
            raise RappProjectsError("JSON input exceeds the byte limit")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise RappProjectsError("JSON input is not UTF-8") from exc
    elif isinstance(data, str):
        try:
            encoded = data.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise RappProjectsError("JSON input contains an unpaired surrogate") from exc
        if len(encoded) > limit:
            raise RappProjectsError("JSON input exceeds the byte limit")
        text = data
    else:
        raise RappProjectsError("JSON input must be text or bytes")
    try:
        value = json.loads(
            text,
            object_pairs_hook=_object_from_pairs,
            parse_int=_parse_int,
            parse_float=_parse_float,
            parse_constant=lambda token: (_ for _ in ()).throw(
                RappProjectsError(f"non-I-JSON number: {token}")
            ),
        )
    except RecursionError as exc:
        raise RappProjectsError("JSON nesting exceeds the depth limit") from exc
    except json.JSONDecodeError as exc:
        raise RappProjectsError("invalid JSON") from exc
    canonical(value)
    return value


def _quoted(value: str) -> str:
    if _has_surrogate(value):
        raise RappProjectsError("I-JSON strings cannot contain unpaired surrogates")
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def _emit_canonical(value: Any, depth: int) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, str):
        return _quoted(value)
    if isinstance(value, int) and not isinstance(value, bool):
        number = _number_roundtrips(str(value))
        return _serialize_binary64(number)
    if isinstance(value, float):
        return _serialize_binary64(value)
    if isinstance(value, list):
        if depth > MAX_DEPTH:
            raise RappProjectsError("JSON nesting exceeds the depth limit")
        return "[" + ",".join(
            _emit_canonical(item, depth + 1) for item in value
        ) + "]"
    if isinstance(value, dict):
        if depth > MAX_DEPTH:
            raise RappProjectsError("JSON nesting exceeds the depth limit")
        if not all(isinstance(key, str) for key in value):
            raise RappProjectsError("I-JSON object keys must be strings")
        for key in value:
            if _has_surrogate(key):
                raise RappProjectsError(
                    "I-JSON object keys cannot contain unpaired surrogates"
                )
        keys = sorted(value, key=lambda key: key.encode("utf-16-be"))
        return "{" + ",".join(
            _quoted(key) + ":" + _emit_canonical(value[key], depth + 1)
            for key in keys
        ) + "}"
    raise RappProjectsError(
        f"value contains non-JSON data: {type(value).__name__}"
    )


def canonical(value: Any) -> str:
    """Return RFC 8785/JCS-compatible canonical I-JSON text."""
    rendered = _emit_canonical(value, 1)
    if len(rendered.encode("utf-8")) > MAX_CANONICAL_BYTES:
        raise RappProjectsError("canonical JSON exceeds 1 MiB")
    return rendered


def H(space: str, value: Any) -> str:
    """Hash a canonical JSON value in one domain-separated address space."""
    if not isinstance(space, str) or "\n" in space or not space.isascii():
        raise RappProjectsError("hash space must be a one-line ASCII string")
    return hashlib.sha256(
        space.encode("ascii") + b"\n" + canonical(value).encode("utf-8")
    ).hexdigest()


def Hb(space: str, value: bytes) -> str:
    """Hash raw octets in one domain-separated address space."""
    if not isinstance(space, str) or "\n" in space or not space.isascii():
        raise RappProjectsError("hash space must be a one-line ASCII string")
    if not isinstance(value, (bytes, bytearray, memoryview)):
        raise RappProjectsError("byte hash input must be bytes-like")
    return hashlib.sha256(
        space.encode("ascii") + b"\n" + bytes(value)
    ).hexdigest()


def utc_now() -> str:
    now = datetime.now(timezone.utc)
    return now.strftime("%Y-%m-%dT%H:%M:%S.") + f"{now.microsecond // 1000:03d}Z"


def _valid_utc(value: Any) -> bool:
    if not isinstance(value, str) or not UTC.fullmatch(value):
        return False
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return False
    return value[17:19] != "60"


def slugify(value: Any) -> str:
    """Create one safe canonical project directory component."""
    text = unicodedata.normalize("NFC", str(value or "")).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    slug = slug[:80].rstrip("-")
    if not slug or not SLUG.fullmatch(slug) or slug in WINDOWS_RESERVED:
        raise RappProjectsError("project must produce a safe lowercase slug")
    return slug


def require_slug(value: Any) -> str:
    value = str(value or "")
    if (
        len(value) > 80
        or not SLUG.fullmatch(value)
        or value in WINDOWS_RESERVED
    ):
        raise RappProjectsError(
            "project must be a canonical lowercase hyphenated slug"
        )
    return value


def _is_within(path: Path, base: Path) -> bool:
    try:
        path.relative_to(base)
        return True
    except ValueError:
        return False


def projects_root(root: Any = None) -> Path:
    selected = (
        root
        if root not in (None, "")
        else os.environ.get("RAPP_PROJECTS_ROOT")
        or str(Path.home() / ".rapp" / "projects-control")
    )
    path = Path(str(selected)).expanduser()
    if not path.is_absolute():
        path = Path.cwd() / path
    if path.is_symlink():
        raise RappProjectsError("project root cannot be a symbolic link")
    path = path.resolve()
    if _is_within(path, _AGENT_DIRECTORY):
        raise RappProjectsError("project state cannot live beside the agent")
    return path


def safe_join(base: Path | str, *parts: Any) -> Path:
    base_path = Path(base).expanduser().resolve()
    candidate = base_path.joinpath(*(str(part) for part in parts)).resolve()
    if not _is_within(candidate, base_path):
        raise RappProjectsError("path escapes the selected project root")
    return candidate


def project_dir(project: Any, root: Any = None) -> Path:
    return safe_join(projects_root(root), require_slug(project))


def require_identity_owner(value: Any = None) -> str:
    selected = (
        value
        if value not in (None, "")
        else os.environ.get("RAPP_PROJECTS_OWNER")
    )
    if not isinstance(selected, str) or not selected.strip():
        raise RappProjectsError(
            "identity_owner or RAPP_PROJECTS_OWNER is required for a new root"
        )
    owner = unicodedata.normalize("NFC", selected.strip().lower())
    if len(owner) > 39 or not LCLABEL.fullmatch(owner):
        raise RappProjectsError(
            "identity_owner must be a lowercase GitHub login"
        )
    return owner


def mint_rappid(slug: Any, owner: Any = None) -> str:
    """Mint a keyless UUIDv4 RAPPID; no name participates in its hash tail."""
    slug = require_slug(slug)
    owner = require_identity_owner(owner)
    tail = Hb("rapp/1:rappid", uuid.uuid4().bytes)
    return f"rappid:@{owner}/{slug}:{tail}"


def _valid_rappid(value: Any, *, slug: str | None = None) -> bool:
    if not isinstance(value, str):
        return False
    match = RAPPID.fullmatch(value)
    return bool(
        match
        and len(match.group(1)) <= 39
        and len(match.group(2)) <= 100
        and (slug is None or match.group(2) == slug)
    )


def _rappid_owner(value: str) -> str:
    match = RAPPID.fullmatch(value)
    if not match or not _valid_rappid(value):
        raise RappProjectsError("invalid RAPPID")
    return match.group(1)


def _valid_kind(value: Any) -> bool:
    if not isinstance(value, str) or not KIND.fullmatch(value):
        return False
    left, right = value.split(".", 1)
    return len(left) <= 64 and len(right) <= 64


def _base64url_decode(value: str) -> bytes:
    if not value or "=" in value or not re.fullmatch(r"[A-Za-z0-9_-]+", value):
        raise RappProjectsError("JWS segment is not unpadded base64url")
    padding = "=" * ((4 - len(value) % 4) % 4)
    try:
        decoded = base64.urlsafe_b64decode(value + padding)
    except (ValueError, TypeError) as exc:
        raise RappProjectsError("JWS segment is invalid") from exc
    encoded = base64.urlsafe_b64encode(decoded).rstrip(b"=").decode("ascii")
    if encoded != value:
        raise RappProjectsError("JWS segment is not canonical base64url")
    return decoded


def _validate_jws_syntax(value: str) -> None:
    parts = value.split(".")
    if len(parts) != 3 or parts[1] != "":
        raise RappProjectsError("sig must use detached compact JWS")
    protected_bytes = _base64url_decode(parts[0])
    signature = _base64url_decode(parts[2])
    protected = _strict_loads(protected_bytes)
    if (
        not isinstance(protected, dict)
        or set(protected) != {"alg", "b64", "crit", "kid"}
        or protected["alg"] not in {"EdDSA", "ES256"}
        or protected["b64"] is not False
        or protected["crit"] != ["b64"]
        or not _valid_rappid(protected["kid"])
        or protected_bytes != canonical(protected).encode("utf-8")
        or len(signature) != 64
    ):
        raise RappProjectsError("sig protected header or signature is invalid")


def project_stream_id(rappid: str) -> str:
    if not _valid_rappid(rappid):
        raise RappProjectsError("invalid project RAPPID")
    return rappid + ":project"


def _valid_stream_id(value: Any) -> bool:
    if not isinstance(value, str) or value.startswith("net:"):
        return False
    if ":" not in value:
        return False
    rappid, instance = value.rsplit(":", 1)
    return bool(
        _valid_rappid(rappid)
        and INSTANCE.fullmatch(instance)
        and len(instance) <= 64
    )


def _stream_project(value: str) -> str:
    if not _valid_stream_id(value) or not value.endswith(":project"):
        raise RappProjectsError("project stream_id is invalid")
    rappid = value.rsplit(":", 1)[0]
    match = RAPPID.fullmatch(rappid)
    if match is None:
        raise RappProjectsError("project stream RAPPID is invalid")
    return match.group(2)


def _mkdir(path: Path) -> Path:
    if path.is_symlink():
        raise RappProjectsError("storage directories cannot be symbolic links")
    if path.exists():
        if not path.is_dir():
            raise RappProjectsError("storage path is not a directory")
        return path
    path.mkdir(parents=True, exist_ok=True, mode=0o700)
    try:
        os.chmod(path, 0o700)
    except OSError:
        pass
    return path


def _fsync_directory(path: Path) -> None:
    try:
        descriptor = os.open(path, os.O_RDONLY)
    except OSError:
        return
    try:
        os.fsync(descriptor)
    except OSError:
        pass
    finally:
        os.close(descriptor)


def _atomic_bytes(path: Path, data: bytes) -> None:
    path = Path(path)
    _mkdir(path.parent)
    temporary = path.with_name(
        f".{path.name}.{os.getpid()}.{threading.get_ident()}.{time.time_ns()}.tmp"
    )
    try:
        with temporary.open("xb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.chmod(temporary, 0o600)
        except OSError:
            pass
        os.replace(temporary, path)
        _fsync_directory(path.parent)
    finally:
        temporary.unlink(missing_ok=True)


def _atomic_json(path: Path, value: Any, *, pretty: bool = False) -> None:
    canonical(value)
    if pretty:
        data = (
            json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        ).encode("utf-8")
    else:
        data = canonical(value).encode("utf-8") + b"\n"
    _atomic_bytes(path, data)


def _read_bounded(path: Path, limit: int, label: str) -> bytes:
    try:
        size = path.stat().st_size
    except OSError as exc:
        raise RappProjectsError(f"cannot inspect {label}") from exc
    if size > limit:
        raise RappProjectsError(f"{label} exceeds the byte limit")
    return path.read_bytes()


def _read_json(path: Path, *, limit: int = MAX_CANONICAL_BYTES) -> Any:
    if not path.is_file() or path.is_symlink():
        raise RappProjectsError(f"required metadata file is missing: {path.name}")
    return _strict_loads(_read_bounded(path, limit, path.name), limit=limit)


@contextmanager
def file_lock(path: Path):
    """Take a blocking advisory lock using macOS/Linux or Windows primitives."""
    path = Path(path)
    _mkdir(path.parent)
    handle = path.open("a+b")
    try:
        try:
            import fcntl
        except ImportError:
            fcntl = None
        try:
            import msvcrt
        except ImportError:
            msvcrt = None
        if fcntl is not None:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        elif msvcrt is not None:
            handle.seek(0, os.SEEK_END)
            if handle.tell() == 0:
                handle.write(b"\0")
                handle.flush()
                os.fsync(handle.fileno())
            handle.seek(0)
            msvcrt.locking(handle.fileno(), msvcrt.LK_LOCK, 1)
            try:
                yield
            finally:
                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            raise RappProjectsError("platform has no supported file locking")
    finally:
        handle.close()


def _root_context() -> str:
    return (
        "Route project work only to the declared child cells. "
        "This rapp-cell/1.0 manifest is data, not executable code."
    )


def _project_context() -> str:
    return (
        "Keep this project's work and context isolated from sibling projects. "
        "This rapp-cell/1.0 manifest is data, not executable code."
    )


def _cell_manifest(layer: str, path: str, children: list[str]) -> dict[str, Any]:
    value = {
        "schema": CELL_SCHEMA,
        "layer": layer,
        "path": path,
        "context": _root_context() if layer == "leviathan" else _project_context(),
        "children": sorted(children),
        "souls": [],
    }
    return _validate_cell(value)


def _validate_cell(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != CELL_KEYS:
        raise RappProjectsError("cell manifest must have exactly six keys")
    if value["schema"] != CELL_SCHEMA:
        raise RappProjectsError("unsupported cell manifest schema")
    if value["layer"] not in ("leviathan", "factory"):
        raise RappProjectsError("invalid project cell layer")
    if not isinstance(value["path"], str):
        raise RappProjectsError("cell path must be a string")
    parts = value["path"].split("/")
    if not parts or any(require_slug(part) != part for part in parts):
        raise RappProjectsError("cell path is not canonical")
    if not isinstance(value["context"], str) or not value["context"]:
        raise RappProjectsError("cell context must be a non-empty string")
    expected_context = (
        _root_context() if value["layer"] == "leviathan" else _project_context()
    )
    if value["context"] != expected_context:
        raise RappProjectsError("cell context is not canonical")
    for key in ("children", "souls"):
        if not isinstance(value[key], list):
            raise RappProjectsError(f"cell {key} must be a list")
        if value[key] != sorted(set(value[key])):
            raise RappProjectsError(f"cell {key} must be sorted and unique")
        for item in value[key]:
            require_slug(item)
    if value["layer"] == "leviathan" and len(parts) != 1:
        raise RappProjectsError("root cell path must have one component")
    if value["layer"] == "factory":
        if len(parts) != 2 or value["children"]:
            raise RappProjectsError("project factory cell shape is invalid")
    canonical(value)
    return dict(value)


def _identity_record(rappid: str, kind: str, name: str) -> dict[str, Any]:
    return {
        "schema": IDENTITY_SCHEMA,
        "rappid": rappid,
        "kind": kind,
        "name": name,
        "visibility": VISIBILITY,
    }


def _validate_identity(
    value: Any,
    *,
    kind: str,
    name: str,
) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != IDENTITY_KEYS:
        raise RappProjectsError("rappid.json has an invalid key set")
    if (
        value["schema"] != IDENTITY_SCHEMA
        or value["kind"] != kind
        or value["name"] != name
        or value["visibility"] != VISIBILITY
        or not _valid_rappid(value["rappid"], slug=name)
    ):
        raise RappProjectsError("rappid.json does not match its storage cell")
    return dict(value)


def _validate_lineage(value: Any, *, schema: str) -> dict[str, Any]:
    if not isinstance(value, dict) or value.get("schema") != schema:
        raise RappProjectsError("lineage metadata is invalid")
    canonical(value)
    return dict(value)


def _root_project_directories(root: Path) -> list[str]:
    names: list[str] = []
    for entry in root.iterdir():
        if entry.is_symlink():
            raise RappProjectsError(f"project root contains a symlink: {entry.name}")
        if not entry.is_dir():
            continue
        if entry.name.startswith("."):
            continue
        names.append(require_slug(entry.name))
    return sorted(names)


def _validate_project_metadata(directory: Path, project: str) -> dict[str, Any]:
    if directory.is_symlink() or not directory.is_dir():
        raise RappProjectsError("project cell must be a regular directory")
    identity = _validate_identity(
        _read_json(directory / "rappid.json"),
        kind="project",
        name=project,
    )
    manifest = _validate_cell(_read_json(directory / "manifest.json"))
    if manifest["layer"] != "factory" or manifest["path"] != f"projects/{project}":
        raise RappProjectsError("project cell manifest is bound to another project")
    lineage = _validate_lineage(
        _read_json(directory / "lineage.json"),
        schema=PROJECT_LINEAGE_SCHEMA,
    )
    return {"identity": identity, "cell": manifest, "lineage": lineage}


def _validate_root_locked(root: Path) -> dict[str, Any]:
    identity = _validate_identity(
        _read_json(root / "rappid.json"),
        kind="projects-root",
        name="projects-control",
    )
    manifest = _validate_cell(_read_json(root / "manifest.json"))
    if manifest["layer"] != "leviathan" or manifest["path"] != "projects":
        raise RappProjectsError("root cell manifest is invalid")
    lineage = _validate_lineage(
        _read_json(root / "lineage.json"),
        schema=ROOT_LINEAGE_SCHEMA,
    )
    directories = _root_project_directories(root)
    if manifest["children"] != directories:
        raise RappProjectsError(
            "root cell children do not match project directories"
        )
    root_owner = _rappid_owner(identity["rappid"])
    for project in directories:
        metadata = _validate_project_metadata(root / project, project)
        if _rappid_owner(metadata["identity"]["rappid"]) != root_owner:
            raise RappProjectsError(
                "project RAPPID owner does not match the root authority"
            )
    return {
        "identity": identity,
        "cell": manifest,
        "lineage": lineage,
        "projects": directories,
    }


def _validate_root_init(value: Any) -> dict[str, Any]:
    if (
        not isinstance(value, dict)
        or set(value) != {"schema", "identity", "lineage", "manifest"}
        or value["schema"] != ROOT_INIT_SCHEMA
    ):
        raise RappProjectsError("root initialization journal is invalid")
    identity = _validate_identity(
        value["identity"],
        kind="projects-root",
        name="projects-control",
    )
    lineage = _validate_lineage(
        value["lineage"],
        schema=ROOT_LINEAGE_SCHEMA,
    )
    manifest = _validate_cell(value["manifest"])
    if manifest["layer"] != "leviathan" or manifest["path"] != "projects":
        raise RappProjectsError("root initialization manifest is invalid")
    return {
        "schema": ROOT_INIT_SCHEMA,
        "identity": identity,
        "lineage": lineage,
        "manifest": manifest,
    }


def _recover_root_init_locked(root: Path) -> None:
    journal_path = root / ".root-init.json"
    if not journal_path.exists():
        return
    journal = _validate_root_init(_read_json(journal_path))
    for filename, value in (
        ("rappid.json", journal["identity"]),
        ("lineage.json", journal["lineage"]),
        ("manifest.json", journal["manifest"]),
    ):
        destination = root / filename
        if destination.exists():
            if _read_json(destination) != value:
                raise RappProjectsError(
                    "root initialization conflicts with existing metadata"
                )
        else:
            _atomic_json(destination, value)
    journal_path.unlink(missing_ok=True)
    _fsync_directory(root)


def _validate_project_transaction(value: Any) -> dict[str, str]:
    if (
        not isinstance(value, dict)
        or set(value) != {"schema", "operation", "project", "staging"}
        or value["schema"] != PROJECT_TRANSACTION_SCHEMA
        or value["operation"] not in {"create", "import"}
    ):
        raise RappProjectsError("project transaction journal is invalid")
    project = require_slug(value["project"])
    staging = value["staging"]
    if (
        not isinstance(staging, str)
        or not STAGING_NAME.fullmatch(staging)
        or STAGING_NAME.fullmatch(staging).group(1) != project
    ):
        raise RappProjectsError("project transaction staging name is invalid")
    return {
        "schema": PROJECT_TRANSACTION_SCHEMA,
        "operation": value["operation"],
        "project": project,
        "staging": staging,
    }


def _write_root_children(
    root: Path,
    manifest: dict[str, Any],
    children: set[str],
) -> None:
    updated = dict(manifest)
    updated["children"] = sorted(children)
    _validate_cell(updated)
    _atomic_json(root / "manifest.json", updated)


def _recover_project_transaction_locked(root: Path) -> None:
    transaction_path = root / ".project-transaction.json"
    if not transaction_path.exists():
        return
    transaction = _validate_project_transaction(_read_json(transaction_path))
    project = transaction["project"]
    staging = root / transaction["staging"]
    destination = root / project
    manifest = _validate_cell(_read_json(root / "manifest.json"))
    children = set(manifest["children"])

    if destination.exists():
        if destination.is_symlink() or not destination.is_dir():
            raise RappProjectsError(
                "committed project transaction target is unsafe"
            )
        try:
            with file_lock(destination / ".chain.lock"):
                _validate_project_metadata(destination, project)
                _load_chain_locked(project, root)
        except RappProjectsError as exc:
            quarantine = root / (
                f".quarantine-{project}-{secrets.token_hex(16)}"
            )
            os.replace(destination, quarantine)
            children.discard(project)
            _write_root_children(root, manifest, children)
            transaction_path.unlink(missing_ok=True)
            _fsync_directory(root)
            raise RappProjectsError(
                "incomplete project transaction was quarantined"
            ) from exc
        children.add(project)
        if staging.exists():
            if staging.is_symlink() or not staging.is_dir():
                raise RappProjectsError(
                    "project transaction staging path is unsafe"
                )
            shutil.rmtree(staging)
    else:
        if staging.exists():
            if staging.is_symlink() or not staging.is_dir():
                raise RappProjectsError(
                    "project transaction staging path is unsafe"
                )
            shutil.rmtree(staging)
        children.discard(project)

    if sorted(children) != manifest["children"]:
        _write_root_children(root, manifest, children)
    transaction_path.unlink(missing_ok=True)
    _fsync_directory(root)


def _cleanup_staging_locked(root: Path) -> None:
    for entry in root.iterdir():
        if not STAGING_NAME.fullmatch(entry.name):
            continue
        if entry.is_symlink() or not entry.is_dir():
            raise RappProjectsError("project staging path is unsafe")
        shutil.rmtree(entry)
    _fsync_directory(root)


def _publish_staged_project_locked(
    root: Path,
    project: str,
    staging: Path,
    manifest: dict[str, Any],
    operation: str,
) -> list[dict[str, str]]:
    transaction_path = root / ".project-transaction.json"
    _atomic_json(
        transaction_path,
        {
            "schema": PROJECT_TRANSACTION_SCHEMA,
            "operation": operation,
            "project": project,
            "staging": staging.name,
        },
    )
    destination = root / project
    os.replace(staging, destination)
    _fsync_directory(root)
    try:
        _write_root_children(
            root,
            manifest,
            set(manifest["children"]) | {project},
        )
    except (OSError, RappProjectsError):
        _recover_project_transaction_locked(root)
        return [
            {
                "code": "root-manifest-recovered",
                "message": (
                    "project committed; root manifest recovered from journal"
                ),
            }
        ]
    transaction_path.unlink(missing_ok=True)
    _fsync_directory(root)
    return []


def ensure_root(
    root: Any = None,
    *,
    identity_owner: Any = None,
) -> Path:
    root_path = projects_root(root)
    _mkdir(root_path)
    with _PROCESS_LOCK:
        with file_lock(root_path / ".projects.lock"):
            _recover_root_init_locked(root_path)
            required = (
                root_path / "rappid.json",
                root_path / "manifest.json",
                root_path / "lineage.json",
            )
            present = [path.exists() for path in required]
            if any(present) and not all(present):
                raise RappProjectsError("project root has partial identity metadata")
            if not any(present):
                directories = _root_project_directories(root_path)
                other_entries = [
                    entry.name
                    for entry in root_path.iterdir()
                    if entry.name
                    not in {".projects.lock", ".views.lock"}
                ]
                if directories or other_entries:
                    raise RappProjectsError(
                        "refusing to mint identity into non-empty unowned root"
                    )
                rappid = mint_rappid(
                    "projects-control",
                    owner=require_identity_owner(identity_owner),
                )
                _atomic_json(
                    root_path / ".root-init.json",
                    {
                        "schema": ROOT_INIT_SCHEMA,
                        "identity": _identity_record(
                            rappid,
                            "projects-root",
                            "projects-control",
                        ),
                        "lineage": {
                            "schema": ROOT_LINEAGE_SCHEMA,
                            "parent_rappid": None,
                        },
                        "manifest": _cell_manifest(
                            "leviathan",
                            "projects",
                            [],
                        ),
                    },
                )
                _recover_root_init_locked(root_path)
            _recover_project_transaction_locked(root_path)
            _cleanup_staging_locked(root_path)
            _validate_root_locked(root_path)
    return root_path


def _validate_receipt(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != RECEIPT_KEYS:
        raise RappProjectsError("artifact receipt has an invalid key set")
    if value["schema"] != RECEIPT_SCHEMA:
        raise RappProjectsError("artifact receipt schema is invalid")
    if (
        not isinstance(value["path"], str)
        or not _valid_receipt_path(value["path"])
    ):
        raise RappProjectsError("artifact receipt path is invalid")
    if value["type"] not in ("file", "missing"):
        raise RappProjectsError("artifact receipts can describe files only")
    if not isinstance(value["exists"], bool):
        raise RappProjectsError("artifact receipt exists must be boolean")
    if value["exists"] != (value["type"] == "file"):
        raise RappProjectsError("artifact receipt type and existence disagree")
    if value["type"] == "file":
        if (
            not isinstance(value["size"], int)
            or isinstance(value["size"], bool)
            or value["size"] < 0
            or not isinstance(value["sha256"], str)
            or not HEX64.fullmatch(value["sha256"])
        ):
            raise RappProjectsError("file artifact receipt is incomplete")
    elif value["size"] is not None or value["sha256"] is not None:
        raise RappProjectsError("missing artifact receipt must use null metadata")
    canonical(value)
    return dict(value)


def _valid_receipt_path(value: str) -> bool:
    if value.startswith("local-private://"):
        return bool(
            LOCATOR_TOKEN.fullmatch(value[len("local-private://") :])
        )
    for prefix in ("project://", "projects://"):
        if value.startswith(prefix):
            relative = value[len(prefix) :]
            if (
                not relative
                or relative.startswith("/")
                or "\\" in relative
            ):
                return False
            parts = relative.split("/")
            if not all(
                part not in ("", ".", "..")
                for part in parts
            ):
                return False
            if prefix == "project://":
                return relative.casefold() not in PROJECT_MANAGED_CASEFOLD
            if len(parts) == 1:
                return parts[0].casefold() not in ROOT_MANAGED_CASEFOLD
            return parts[1].casefold() not in PROJECT_MANAGED_CASEFOLD
    return False


def _managed_storage_path(path: Path, project: str, root: Path) -> bool:
    path = path.resolve()
    directory = project_dir(project, root)
    if _is_within(path, directory):
        relative = path.relative_to(directory)
        return (
            not relative.parts
            or relative.parts[0].startswith(".staging-")
            or relative.as_posix().casefold() in PROJECT_MANAGED_CASEFOLD
        )
    if _is_within(path, root):
        relative = path.relative_to(root)
        if not relative.parts:
            return True
        if len(relative.parts) == 1:
            return relative.parts[0].casefold() in ROOT_MANAGED_CASEFOLD
        if relative.parts[0].startswith("."):
            return True
        return relative.parts[1].casefold() in PROJECT_MANAGED_CASEFOLD
    return False


def _view_path(path: Path, project: str, root: Path) -> str:
    path = path.resolve()
    directory = project_dir(project, root)
    if _is_within(path, directory):
        relative = path.relative_to(directory).as_posix()
        return unicodedata.normalize("NFC", "project://" + (relative or "."))
    if _is_within(path, root):
        relative = path.relative_to(root).as_posix()
        return unicodedata.normalize("NFC", "projects://" + (relative or "."))
    return unicodedata.normalize("NFC", "local-private://" + path.name)


def _validate_receipt_locators(value: Any) -> dict[str, Any]:
    if (
        not isinstance(value, dict)
        or set(value) != {"schema", "paths"}
        or value["schema"] != RECEIPT_LOCATORS_SCHEMA
        or not isinstance(value["paths"], dict)
    ):
        raise RappProjectsError("receipt locator metadata is invalid")
    paths: dict[str, str] = {}
    for token, location in value["paths"].items():
        if (
            not isinstance(token, str)
            or not LOCATOR_TOKEN.fullmatch(token)
            or not isinstance(location, str)
            or not location
        ):
            raise RappProjectsError("receipt locator entry is invalid")
        path = Path(location).expanduser()
        if not path.is_absolute():
            raise RappProjectsError("receipt locator path must be absolute")
        paths[token] = str(path)
    normalized = {"schema": RECEIPT_LOCATORS_SCHEMA, "paths": paths}
    canonical(normalized)
    return normalized


def _load_receipt_locators(project: str, root: Path) -> dict[str, Any]:
    return _load_receipt_locators_from_directory(project_dir(project, root))


def _load_receipt_locators_from_directory(
    directory: Path,
) -> dict[str, Any]:
    path = directory / ".receipt-locators.json"
    if not path.exists():
        return {"schema": RECEIPT_LOCATORS_SCHEMA, "paths": {}}
    return _validate_receipt_locators(_read_json(path))


def _merge_receipt_locators(
    directory: Path,
    additions: dict[str, str],
) -> None:
    if not additions:
        return
    locators = _load_receipt_locators_from_directory(directory)
    locators["paths"].update(additions)
    _atomic_json(directory / ".receipt-locators.json", locators)


def _register_receipt_locator(
    path: Path,
    project: str,
    root: Path,
    pending_locators: dict[str, str] | None = None,
) -> str:
    directory = project_dir(project, root)
    if not directory.is_dir() or directory.is_symlink():
        raise RappProjectsError("receipt project directory is unavailable")
    location = str(path.resolve())
    token = secrets.token_hex(16)
    if pending_locators is not None:
        pending_locators[token] = location
        return "local-private://" + token
    with _PROCESS_LOCK:
        with file_lock(directory / ".chain.lock"):
            _merge_receipt_locators(directory, {token: location})
    return "local-private://" + token


def _resolve_receipt_path(
    value: str,
    *,
    project: str,
    root: Path,
) -> Path | None:
    if value.startswith("project://"):
        relative = value[len("project://") :]
        if not relative or relative == ".":
            return None
        return safe_join(project_dir(project, root), relative)
    if value.startswith("projects://"):
        relative = value[len("projects://") :]
        if not relative or relative == ".":
            return None
        return safe_join(root, relative)
    if value.startswith("local-private://"):
        token = value[len("local-private://") :]
        if not LOCATOR_TOKEN.fullmatch(token):
            return None
        location = _load_receipt_locators(project, root)["paths"].get(token)
        if location is None:
            return None
        path = Path(location).expanduser()
        return path.resolve() if path.is_absolute() else None
    return None


def _hash_file(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as handle:
        while True:
            block = handle.read(1024 * 1024)
            if not block:
                break
            digest.update(block)
            size += len(block)
    return digest.hexdigest(), size


def artifact_receipt(
    value: Any,
    project: Any,
    root: Any = None,
    *,
    pending_locators: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Hash one file without copying its body into project storage."""
    project = require_slug(project)
    root_path = projects_root(root)
    if isinstance(value, dict) and set(value) == RECEIPT_KEYS:
        existing = _validate_receipt(value)
        resolved = _resolve_receipt_path(
            existing["path"], project=project, root=root_path
        )
        if resolved is None:
            raise RappProjectsError(
                "supplied artifact receipt cannot be verified on this device"
            )
        current = artifact_receipt(
            str(resolved),
            project=project,
            root=root_path,
            pending_locators=pending_locators,
        )
        if existing["sha256"] != current["sha256"]:
            raise RappProjectsError("supplied artifact receipt no longer matches")
        return current
    raw = value.get("path") if isinstance(value, dict) else value
    if not isinstance(raw, (str, os.PathLike)) or not str(raw):
        raise RappProjectsError("artifact receipt requires a file path")
    text = str(raw)
    if any(
        text.startswith(prefix)
        for prefix in ("project://", "projects://", "local-private://")
    ):
        if not _valid_receipt_path(text):
            raise RappProjectsError("artifact receipt path is invalid")
        resolved = _resolve_receipt_path(
            text,
            project=project,
            root=root_path,
        )
        if resolved is None:
            raise RappProjectsError(
                "opaque receipt path is not bound on this device"
            )
    else:
        input_path = Path(text).expanduser()
        candidate = (
            input_path
            if input_path.is_absolute()
            else project_dir(project, root_path) / input_path
        )
        if candidate.is_symlink():
            raise RappProjectsError("artifact receipts refuse symbolic links")
        resolved = (
            candidate.resolve()
            if input_path.is_absolute()
            else safe_join(project_dir(project, root_path), input_path)
        )
    if resolved.is_symlink():
        raise RappProjectsError("artifact receipts refuse symbolic links")
    if _managed_storage_path(resolved, project, root_path):
        raise RappProjectsError(
            "artifact receipts cannot target project-managed storage"
        )
    logical = (
        _view_path(resolved, project, root_path)
        if _is_within(resolved, root_path)
        else _register_receipt_locator(
            resolved,
            project,
            root_path,
            pending_locators,
        )
    )
    if not resolved.exists():
        return {
            "schema": RECEIPT_SCHEMA,
            "path": logical,
            "exists": False,
            "type": "missing",
            "size": None,
            "sha256": None,
        }
    if not resolved.is_file():
        raise RappProjectsError("artifact receipts hash regular files only")
    digest, size = _hash_file(resolved)
    return {
        "schema": RECEIPT_SCHEMA,
        "path": logical,
        "exists": True,
        "type": "file",
        "size": size,
        "sha256": digest,
    }


def _receipt_list(
    value: Any,
    project: str,
    root: Path,
    pending_locators: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    if value is None:
        values: list[Any] = []
    elif isinstance(value, list):
        values = value
    else:
        values = [value]
    if len(values) > MAX_LIST_ITEMS:
        raise RappProjectsError("artifact list has too many items")
    return [
        artifact_receipt(
            item,
            project,
            root,
            pending_locators=pending_locators,
        )
        for item in values
    ]


def _frame_receipts(frame: dict[str, Any]) -> list[dict[str, Any]]:
    if frame["kind"] == "work.status":
        return frame["payload"]["artifacts"]
    if frame["kind"] == "work.handoff":
        return [frame["payload"]["doc"]]
    if frame["kind"] == "work.punchout":
        return frame["payload"]["receipts"]
    return []


def bind_receipt_locators(
    project: Any,
    bindings: Any,
    root: Any = None,
    *,
    owner_approved: bool = False,
) -> dict[str, Any]:
    """Bind imported opaque receipt tokens to matching local files."""
    if owner_approved is not True:
        raise PermissionError("receipt binding requires owner_approved=true")
    project = require_slug(project)
    root_path = ensure_root(root)
    if (
        not isinstance(bindings, dict)
        or not bindings
        or len(bindings) > MAX_LIST_ITEMS
    ):
        raise RappProjectsError("receipt_bindings must be a non-empty object")

    requested: dict[str, Path] = {}
    for logical, location in bindings.items():
        if (
            not isinstance(logical, str)
            or not logical.startswith("local-private://")
            or not LOCATOR_TOKEN.fullmatch(
                logical[len("local-private://") :]
            )
            or not isinstance(location, (str, os.PathLike))
            or not str(location)
        ):
            raise RappProjectsError("receipt binding entry is invalid")
        path = Path(str(location)).expanduser()
        if not path.is_absolute() or path.is_symlink():
            raise RappProjectsError(
                "receipt binding must name an absolute regular file"
            )
        requested[logical] = path.resolve()

    directory = project_dir(project, root_path)
    with _PROCESS_LOCK:
        with file_lock(directory / ".chain.lock"):
            frames = _load_chain_locked(project, root_path)
            historical: dict[str, list[dict[str, Any]]] = {
                logical: [] for logical in requested
            }
            for frame in frames:
                for receipt in _frame_receipts(frame):
                    receipt = _validate_receipt(receipt)
                    if receipt["path"] in historical:
                        historical[receipt["path"]].append(receipt)
            missing = sorted(
                logical for logical, values in historical.items() if not values
            )
            if missing:
                raise RappProjectsError(
                    "receipt binding token is absent from the project chain"
                )

            resolved_bindings: dict[str, str] = {}
            for logical, path in requested.items():
                if path.is_symlink() or not path.is_file():
                    raise RappProjectsError(
                        "receipt binding must name an existing regular file"
                    )
                digest, size = _hash_file(path)
                if any(
                    receipt["sha256"] != digest or receipt["size"] != size
                    for receipt in historical[logical]
                ):
                    raise RappProjectsError(
                        "receipt binding does not match the historical hash"
                    )
                resolved_bindings[
                    logical[len("local-private://") :]
                ] = str(path)

            locators = _load_receipt_locators(project, root_path)
            locators["paths"].update(resolved_bindings)
            _atomic_json(directory / ".receipt-locators.json", locators)
    return {
        "bound": sorted(requested),
        "count": len(requested),
    }


def _validate_payload(kind: str, payload: Any, project: str | None = None) -> None:
    if kind not in FRAME_KINDS:
        raise RappProjectsError("unsupported project frame kind")
    if not isinstance(payload, dict):
        raise RappProjectsError("frame payload must be an object")
    schema = _PAYLOAD_SCHEMAS[kind]
    keys = set(payload)
    missing = schema["required"] - keys
    extra = keys - schema["required"] - schema["optional"]
    if missing or extra:
        raise RappProjectsError(
            f"{kind} payload key set is invalid"
            + (f"; missing={sorted(missing)}" if missing else "")
            + (f"; extra={sorted(extra)}" if extra else "")
        )
    if not isinstance(payload.get("project"), str):
        raise RappProjectsError("payload project must be a string")
    require_slug(payload["project"])
    if project is not None and payload["project"] != project:
        raise RappProjectsError("payload is bound to another project")
    string_fields = {
        "title",
        "goal",
        "owner",
        "origin",
        "visibility",
        "agent",
        "runtime",
        "session_id",
        "location",
        "intent",
        "role",
        "status",
        "next_action",
        "project_state",
        "from_agent",
        "to_agent",
        "outcome",
        "summary",
        "verdict",
        "head_frame_hash",
    }
    for key in keys & string_fields:
        if not isinstance(payload[key], str):
            raise RappProjectsError(f"{kind}.{key} must be a string")
    list_fields = {
        "capabilities",
        "artifacts",
        "blockers",
        "open_questions",
        "receipts",
        "broken_receipts",
    }
    for key in keys & list_fields:
        if not isinstance(payload[key], list):
            raise RappProjectsError(f"{kind}.{key} must be a list")
        if len(payload[key]) > MAX_LIST_ITEMS:
            raise RappProjectsError(f"{kind}.{key} has too many items")
    if kind == "project.genesis" and payload["visibility"] != VISIBILITY:
        raise RappProjectsError("project visibility must be local-private")
    if kind == "work.punchin":
        if not all(isinstance(item, str) for item in payload["capabilities"]):
            raise RappProjectsError("capabilities must contain strings")
    if kind == "work.status":
        pct = payload["pct"]
        if (
            not isinstance(pct, int)
            or isinstance(pct, bool)
            or not 0 <= pct <= 100
        ):
            raise RappProjectsError("status pct must be an integer from 0 to 100")
        if payload.get("project_state") not in (
            None,
            "active",
            "blocked",
            "done",
            "parked",
        ):
            raise RappProjectsError("invalid project_state")
        for receipt in payload["artifacts"]:
            _validate_receipt(receipt)
    if kind == "work.handoff":
        _validate_receipt(payload["doc"])
    if kind == "work.punchout":
        if payload["outcome"] not in ("done", "blocked", "abandoned"):
            raise RappProjectsError("invalid punchout outcome")
        for receipt in payload["receipts"]:
            _validate_receipt(receipt)
    if kind == "project.verify":
        if payload["verdict"] not in ("pass", "fail"):
            raise RappProjectsError("invalid project verification verdict")
        count = payload["verified_frames"]
        if (
            not isinstance(count, int)
            or isinstance(count, bool)
            or count < 1
            or count > MAX_SAFE_INTEGER
        ):
            raise RappProjectsError("verified_frames must be a positive uint53")
        if not HEX64.fullmatch(payload["head_frame_hash"]):
            raise RappProjectsError("head_frame_hash must be lowercase sha256")
        for receipt in payload["broken_receipts"]:
            _validate_receipt(receipt)
        if (payload["verdict"] == "pass") != (
            len(payload["broken_receipts"]) == 0
        ):
            raise RappProjectsError(
                "verification verdict contradicts broken_receipts"
            )
    for key in ("blockers", "open_questions"):
        if key in payload and not all(isinstance(item, str) for item in payload[key]):
            raise RappProjectsError(f"{key} must contain strings")
    canonical(payload)


def build_frame(
    kind: str,
    stream_id: str,
    seq: int,
    payload: dict[str, Any],
    prev: str | None = None,
    utc_value: str | None = None,
) -> dict[str, Any]:
    """Build one exact unsigned, off-swarm, eleven-key RAPP/1 frame."""
    if kind not in FRAME_KINDS or not _valid_kind(kind):
        raise RappProjectsError("unsupported project frame kind")
    if not _valid_stream_id(stream_id) or not stream_id.endswith(":project"):
        raise RappProjectsError("project stream_id is invalid")
    if (
        not isinstance(seq, int)
        or isinstance(seq, bool)
        or not 0 <= seq <= MAX_SAFE_INTEGER
    ):
        raise RappProjectsError("frame seq must be uint53")
    if seq == 0 and prev is not None:
        raise RappProjectsError("genesis prev must be null")
    if seq > 0 and (not isinstance(prev, str) or not HEX64.fullmatch(prev)):
        raise RappProjectsError("non-genesis prev must be lowercase sha256")
    _validate_payload(
        kind,
        payload,
        project=_stream_project(stream_id),
    )
    stamp = utc_value or utc_now()
    if not _valid_utc(stamp):
        raise RappProjectsError("utc must be a valid millisecond UTC timestamp")
    frame: dict[str, Any] = {
        "spec": SPEC,
        "kind": kind,
        "stream_id": stream_id,
        "seq": seq,
        "utc": stamp,
        "payload": payload,
        "payload_hash": H("rapp/1:particle", payload),
        "prev": prev,
        "prev_wave": None,
        "sig": None,
    }
    preimage = {
        key: value
        for key, value in frame.items()
        if key not in {"frame_hash", "sig"}
    }
    frame["frame_hash"] = H("rapp/1:wave", preimage)
    if set(frame) != FRAME_KEYS:
        raise AssertionError("internal frame key set drift")
    canonical(frame)
    return frame


def _verify_frame_or_raise(
    frame: Any,
    *,
    head: dict[str, Any] | None = None,
    stream_id: str | None = None,
    project: str | None = None,
    signature_verifier: Any = None,
) -> None:
    # Step 1 — shape and types.
    if not isinstance(frame, dict) or set(frame) != FRAME_KEYS:
        raise FrameVerificationError("1", "frame must have exactly eleven keys")
    if frame.get("spec") != SPEC:
        raise FrameVerificationError("1", "spec must be rapp/1")
    if (
        not isinstance(frame.get("kind"), str)
        or not _valid_kind(frame["kind"])
        or frame["kind"] not in FRAME_KINDS
    ):
        raise FrameVerificationError("1", "kind is unregistered")
    if (
        not isinstance(frame.get("stream_id"), str)
        or not _valid_stream_id(frame["stream_id"])
        or not frame["stream_id"].endswith(":project")
    ):
        raise FrameVerificationError("1", "stream_id is invalid")
    seq = frame.get("seq")
    if (
        not isinstance(seq, int)
        or isinstance(seq, bool)
        or not 0 <= seq <= MAX_SAFE_INTEGER
    ):
        raise FrameVerificationError("1", "seq must be uint53")
    if not _valid_utc(frame.get("utc")):
        raise FrameVerificationError("1", "utc is invalid")
    if not isinstance(frame.get("payload"), dict):
        raise FrameVerificationError("1", "payload must be an object")
    try:
        _validate_payload(frame["kind"], frame["payload"], project=project)
    except RappProjectsError as exc:
        raise FrameVerificationError("1", str(exc)) from exc
    for key in ("payload_hash", "frame_hash"):
        if not isinstance(frame.get(key), str) or not HEX64.fullmatch(frame[key]):
            raise FrameVerificationError("1", f"{key} is invalid")
    for key in ("prev", "prev_wave"):
        if frame.get(key) is not None and (
            not isinstance(frame[key], str) or not HEX64.fullmatch(frame[key])
        ):
            raise FrameVerificationError("1", f"{key} is invalid")
    if frame.get("sig") is not None:
        if not isinstance(frame["sig"], str):
            raise FrameVerificationError("1", "sig must be null or a JWS string")
        try:
            _validate_jws_syntax(frame["sig"])
        except RappProjectsError as exc:
            raise FrameVerificationError("1", str(exc)) from exc
    try:
        canonical(frame)
    except RappProjectsError as exc:
        raise FrameVerificationError("1", str(exc)) from exc

    # Step 1a — stream binding.
    if stream_id is None:
        raise FrameVerificationError("1a", "stream of record is required")
    if frame["stream_id"] != stream_id:
        raise FrameVerificationError("1a", "frame belongs to another stream")
    stream_project = _stream_project(frame["stream_id"])
    if frame["payload"].get("project") != stream_project:
        raise FrameVerificationError(
            "1a",
            "payload project does not match the stream identity",
        )
    if project is not None and project != stream_project:
        raise FrameVerificationError(
            "1a",
            "project of record does not match the stream identity",
        )

    # Step 2 — particle.
    if frame["payload_hash"] != H("rapp/1:particle", frame["payload"]):
        raise FrameVerificationError("2", "payload hash mismatch")

    # Step 3 — wave.
    preimage = {
        key: value
        for key, value in frame.items()
        if key not in {"frame_hash", "sig"}
    }
    if frame["frame_hash"] != H("rapp/1:wave", preimage):
        raise FrameVerificationError("3", "frame hash mismatch")

    # Step 4 — worldline chain and time.
    if head is None:
        if (
            frame["seq"] != 0
            or frame["prev"] is not None
            or frame["kind"] != "project.genesis"
        ):
            raise FrameVerificationError("4", "invalid project genesis")
    else:
        if frame["kind"] == "project.genesis":
            raise FrameVerificationError(
                "4",
                "project genesis is allowed only at sequence zero",
            )
        if frame["seq"] != head["seq"] + 1:
            raise FrameVerificationError("4", "sequence is not contiguous")
        if frame["prev"] != head["payload_hash"]:
            raise FrameVerificationError("4", "previous particle does not match")
        if frame["utc"] < head["utc"]:
            raise FrameVerificationError("4", "utc moved backwards")
        if frame["kind"] == "project.verify" and (
            frame["payload"]["verified_frames"] != frame["seq"]
            or frame["payload"]["head_frame_hash"] != head["frame_hash"]
        ):
            raise FrameVerificationError(
                "4",
                "verification verdict does not cover its predecessor",
            )

    # Step 5 — wire chain. Project streams are never swarm streams.
    if frame["prev_wave"] is not None:
        raise FrameVerificationError("5", "prev_wave must be null off swarm")

    # Step 6 — local project streams are intentionally unsigned.
    if frame["sig"] is not None:
        if signature_verifier is None:
            raise FrameVerificationError(
                "6",
                "signed frame requires a RAPP registry trust verifier",
            )
        try:
            verified = signature_verifier(frame)
        except Exception as exc:
            raise FrameVerificationError(
                "6",
                "signature trust verification failed",
            ) from exc
        if verified is not True:
            raise FrameVerificationError("6", "signature is not trusted")


def verify_frame(
    frame: Any,
    head: dict[str, Any] | None = None,
    stream_id: str | None = None,
    project: str | None = None,
    signature_verifier: Any = None,
) -> tuple[bool, str | None]:
    """Return ``(ok, reason)`` after the ordered RAPP/1 checklist."""
    try:
        _verify_frame_or_raise(
            frame,
            head=head,
            stream_id=stream_id,
            project=project,
            signature_verifier=signature_verifier,
        )
        return True, None
    except FrameVerificationError as exc:
        return False, str(exc)


def _chain_hash(frames: list[dict[str, Any]]) -> str:
    digest = hashlib.sha256(b"rapp-project-chain/1\n")
    for frame in frames:
        digest.update(frame["frame_hash"].encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def _head_record(frames: list[dict[str, Any]]) -> dict[str, Any]:
    if not frames:
        raise RappProjectsError("trusted head requires at least one frame")
    frame = frames[-1]
    return {
        "schema": HEAD_SCHEMA,
        "stream_id": frame["stream_id"],
        "seq": frame["seq"],
        "frame_hash": frame["frame_hash"],
        "chain_hash": _chain_hash(frames),
    }


def _validate_head(value: Any, stream_id: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != HEAD_KEYS:
        raise ChainVerificationError("trusted head metadata has an invalid key set")
    if (
        value["schema"] != HEAD_SCHEMA
        or value["stream_id"] != stream_id
        or not isinstance(value["seq"], int)
        or isinstance(value["seq"], bool)
        or not 0 <= value["seq"] <= MAX_SAFE_INTEGER
        or not isinstance(value["frame_hash"], str)
        or not HEX64.fullmatch(value["frame_hash"])
        or not isinstance(value["chain_hash"], str)
        or not HEX64.fullmatch(value["chain_hash"])
    ):
        raise ChainVerificationError("trusted head metadata is invalid")
    return dict(value)


def _load_trusted_head(
    head_path: Path,
    frames: list[dict[str, Any]],
    stream_id: str,
) -> dict[str, Any]:
    value = _read_json(head_path)
    if (
        isinstance(value, dict)
        and set(value) == LEGACY_HEAD_KEYS
        and value.get("schema") == LEGACY_HEAD_SCHEMA
    ):
        seq = value.get("seq")
        frame_hash = value.get("frame_hash")
        if (
            value.get("stream_id") != stream_id
            or not isinstance(seq, int)
            or isinstance(seq, bool)
            or seq < 0
            or seq >= len(frames)
            or not isinstance(frame_hash, str)
            or not HEX64.fullmatch(frame_hash)
            or frames[seq]["frame_hash"] != frame_hash
        ):
            raise ChainVerificationError(
                "legacy trusted head does not match the chain"
            )
        upgraded = _head_record(frames[: seq + 1])
        _atomic_json(head_path, upgraded)
        return upgraded
    return _validate_head(value, stream_id)


def _load_chain_bytes(
    data: bytes,
    *,
    project: str,
    stream_id: str,
) -> list[dict[str, Any]]:
    if len(data) > MAX_CHAIN_BYTES:
        raise ChainVerificationError("chain exceeds the storage byte limit")
    if not data:
        return []
    if not data.endswith(b"\n"):
        raise ChainVerificationError("chain is missing its final record terminator")
    frames: list[dict[str, Any]] = []
    head = None
    for line_number, line in enumerate(data.splitlines(keepends=True), 1):
        if not line.endswith(b"\n") or line == b"\n":
            raise ChainVerificationError(
                f"chain line {line_number} is blank or unterminated"
            )
        record = line[:-1]
        if len(record) > MAX_CANONICAL_BYTES:
            raise ChainVerificationError(
                f"chain line {line_number} exceeds 1 MiB"
            )
        try:
            frame = _strict_loads(record)
            _verify_frame_or_raise(
                frame,
                head=head,
                stream_id=stream_id,
                project=project,
            )
        except RappProjectsError as exc:
            raise ChainVerificationError(
                f"chain line {line_number} failed: {exc}"
            ) from exc
        frames.append(frame)
        head = frame
    return frames


def _check_trusted_head(
    directory: Path,
    frames: list[dict[str, Any]],
    stream_id: str,
) -> None:
    head_path = directory / "head.json"
    if not frames:
        if head_path.exists():
            raise ChainVerificationError("trusted head exists for an empty chain")
        return
    if not head_path.is_file() or head_path.is_symlink():
        raise ChainVerificationError("trusted project head is missing")
    trusted = _load_trusted_head(head_path, frames, stream_id)
    actual = frames[-1]
    if trusted["seq"] > actual["seq"]:
        raise ChainVerificationError("presented chain rolls back the trusted head")
    if trusted["seq"] >= len(frames):
        raise ChainVerificationError("trusted head sequence is outside the chain")
    trusted_frame = frames[trusted["seq"]]
    if trusted_frame["frame_hash"] != trusted["frame_hash"]:
        raise ChainVerificationError("chain forks from the trusted head")
    trusted_chain_hash = _chain_hash(frames[: trusted["seq"] + 1])
    if trusted_chain_hash != trusted["chain_hash"]:
        raise ChainVerificationError(
            "chain history differs beneath the trusted head"
        )
    if trusted["seq"] < actual["seq"]:
        try:
            _atomic_json(head_path, _head_record(frames))
        except OSError:
            pass


def _validate_append_transaction(
    value: Any,
    stream_id: str,
) -> dict[str, Any]:
    keys = {
        "schema",
        "phase",
        "stream_id",
        "base_seq",
        "base_frame_hash",
        "base_chain_hash",
        "final_seq",
        "final_payload_hash",
        "final_frame_hash",
        "final_chain_hash",
        "locators",
    }
    if not isinstance(value, dict) or set(value) != keys:
        raise ChainVerificationError("append transaction has an invalid key set")
    if (
        value["schema"] != APPEND_TRANSACTION_SCHEMA
        or not isinstance(value["phase"], str)
        or value["phase"] not in {"prepared", "committed"}
        or value["stream_id"] != stream_id
        or not isinstance(value["base_seq"], int)
        or isinstance(value["base_seq"], bool)
        or not isinstance(value["final_seq"], int)
        or isinstance(value["final_seq"], bool)
        or value["base_seq"] < 0
        or value["final_seq"] <= value["base_seq"]
        or value["final_seq"] > MAX_SAFE_INTEGER
        or any(
            not isinstance(value[key], str)
            or not HEX64.fullmatch(value[key])
            for key in (
                "base_frame_hash",
                "base_chain_hash",
                "final_payload_hash",
                "final_frame_hash",
                "final_chain_hash",
            )
        )
        or not isinstance(value["locators"], dict)
    ):
        raise ChainVerificationError("append transaction is invalid")
    for token, location in value["locators"].items():
        if (
            not isinstance(token, str)
            or not LOCATOR_TOKEN.fullmatch(token)
            or not isinstance(location, str)
            or not Path(location).is_absolute()
        ):
            raise ChainVerificationError(
                "append transaction locator is invalid"
            )
    return dict(value)


def _append_transaction_record(
    frames: list[dict[str, Any]],
    extension: list[dict[str, Any]],
    phase: str,
    locators: dict[str, str] | None = None,
) -> dict[str, Any]:
    base = frames[-1]
    final_frames = frames + extension
    final = final_frames[-1]
    return {
        "schema": APPEND_TRANSACTION_SCHEMA,
        "phase": phase,
        "stream_id": base["stream_id"],
        "base_seq": base["seq"],
        "base_frame_hash": base["frame_hash"],
        "base_chain_hash": _chain_hash(frames),
        "final_seq": final["seq"],
        "final_payload_hash": final["payload_hash"],
        "final_frame_hash": final["frame_hash"],
        "final_chain_hash": _chain_hash(final_frames),
        "locators": dict(locators or {}),
    }


def _recover_append_transaction_locked(
    directory: Path,
    frames: list[dict[str, Any]],
    stream_id: str,
) -> None:
    transaction_path = directory / ".append-transaction.json"
    if not transaction_path.exists():
        return
    transaction = _validate_append_transaction(
        _read_json(transaction_path),
        stream_id,
    )
    current = frames[-1]
    current_chain_hash = _chain_hash(frames)
    final_matches = (
        current["seq"] == transaction["final_seq"]
        and current["frame_hash"] == transaction["final_frame_hash"]
        and current["payload_hash"] == transaction["final_payload_hash"]
        and current_chain_hash == transaction["final_chain_hash"]
    )
    base_matches = (
        current["seq"] == transaction["base_seq"]
        and current["frame_hash"] == transaction["base_frame_hash"]
        and current_chain_hash == transaction["base_chain_hash"]
    )
    if final_matches:
        _merge_receipt_locators(
            directory,
            transaction["locators"],
        )
        try:
            _atomic_json(
                directory / "head.json",
                _head_record(frames),
            )
        except OSError:
            return
        transaction_path.unlink(missing_ok=True)
        _fsync_directory(directory)
        return

    if base_matches and transaction["phase"] == "prepared":
        transaction_path.unlink(missing_ok=True)
        _fsync_directory(directory)
        return
    if transaction["phase"] == "committed":
        raise ChainVerificationError(
            "presented chain rolls back a committed append transaction"
        )
    raise ChainVerificationError(
        "chain does not match append transaction boundaries"
    )


def _load_chain_locked(project: str, root_path: Path) -> list[dict[str, Any]]:
    directory = project_dir(project, root_path)
    metadata = _validate_project_metadata(directory, project)
    stream_id = project_stream_id(metadata["identity"]["rappid"])
    chain_path = directory / "chain.jsonl"
    if not chain_path.is_file() or chain_path.is_symlink():
        raise ChainVerificationError("chain.jsonl must be a regular file")
    frames = _load_chain_bytes(
        _read_bounded(chain_path, MAX_CHAIN_BYTES, "chain.jsonl"),
        project=project,
        stream_id=stream_id,
    )
    if not frames:
        raise ChainVerificationError("opened project has an empty chain")
    _recover_append_transaction_locked(directory, frames, stream_id)
    _check_trusted_head(directory, frames, stream_id)
    return frames


def load_chain(project: Any, root: Any = None) -> list[dict[str, Any]]:
    """Read chain and head under one cross-process project lock."""
    project = require_slug(project)
    root_path = projects_root(root)
    directory = project_dir(project, root_path)
    if directory.is_symlink() or not directory.is_dir():
        raise ChainVerificationError("project cell must be a regular directory")
    with _PROCESS_LOCK:
        with file_lock(directory / ".chain.lock"):
            return _load_chain_locked(project, root_path)


def _append_octets(path: Path, record: bytes) -> None:
    if len(record) > MAX_CANONICAL_BYTES + 1 or not record.endswith(b"\n"):
        raise RappProjectsError("append record exceeds the frame limit")
    if path.exists():
        if path.is_symlink() or not path.is_file():
            raise RappProjectsError("append target must be a regular file")
        existing = _read_bounded(path, MAX_CHAIN_BYTES, path.name)
    else:
        existing = b""
    if len(existing) + len(record) > MAX_CHAIN_BYTES:
        raise RappProjectsError("chain exceeds the storage byte limit")
    _atomic_bytes(path, existing + record)


def _commit_chain_extension_locked(
    directory: Path,
    project: str,
    frames: list[dict[str, Any]],
    extension: list[dict[str, Any]],
    pending_locators: dict[str, str] | None = None,
) -> list[dict[str, str]]:
    if not extension:
        return []
    stream_id = frames[0]["stream_id"]
    chain_path = directory / "chain.jsonl"
    existing = _read_bounded(chain_path, MAX_CHAIN_BYTES, "chain.jsonl")
    suffix = b"".join(
        canonical(frame).encode("utf-8") + b"\n"
        for frame in extension
    )
    updated = existing + suffix
    _load_chain_bytes(updated, project=project, stream_id=stream_id)
    transaction_path = directory / ".append-transaction.json"
    _atomic_json(
        transaction_path,
        _append_transaction_record(
            frames,
            extension,
            "prepared",
            pending_locators,
        ),
    )
    warnings: list[dict[str, str]] = []
    try:
        _atomic_bytes(chain_path, updated)
    except (OSError, RappProjectsError):
        transaction_path.unlink(missing_ok=True)
        _fsync_directory(directory)
        raise
    try:
        _atomic_json(
            transaction_path,
            _append_transaction_record(
                frames,
                extension,
                "committed",
                pending_locators,
            ),
        )
    except OSError:
        warnings.append(
            {
                "code": "commit-marker-refresh-failed",
                "message": (
                    "frame committed; append marker recovery remains pending"
                ),
            }
        )
    locators_written = True
    try:
        _merge_receipt_locators(
            directory,
            dict(pending_locators or {}),
        )
    except (OSError, RappProjectsError):
        locators_written = False
        warnings.append(
            {
                "code": "receipt-locator-refresh-failed",
                "message": (
                    "frame committed; receipt locator recovery remains pending"
                ),
            }
        )
    head_written = True
    try:
        _atomic_json(
            directory / "head.json",
            _head_record(frames + extension),
        )
    except OSError:
        head_written = False
        warnings.append(
            {
                "code": "head-refresh-failed",
                "message": (
                    "frame committed; trusted head recovery remains pending"
                ),
            }
        )
    if locators_written and head_written:
        transaction_path.unlink(missing_ok=True)
        _fsync_directory(directory)
    return warnings


def _append_locked(
    project: str,
    kind: str,
    payload: dict[str, Any],
    root: Path,
    pending_locators: dict[str, str] | None = None,
) -> dict[str, Any]:
    directory = project_dir(project, root)
    frames = _load_chain_locked(project, root)
    head = frames[-1]
    frame = build_frame(
        kind,
        head["stream_id"],
        head["seq"] + 1,
        payload,
        head["payload_hash"],
    )
    _verify_frame_or_raise(
        frame,
        head=head,
        stream_id=head["stream_id"],
        project=project,
    )
    warnings = _commit_chain_extension_locked(
        directory,
        project,
        frames,
        [frame],
        pending_locators,
    )
    return CommittedFrame(frame, warnings)


def append_frame(
    project: Any,
    kind: str,
    payload: dict[str, Any],
    root: Any = None,
    *,
    refresh: bool = False,
    pending_locators: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Append after locking, reloading, and verifying the authoritative chain."""
    project = require_slug(project)
    root_path = ensure_root(root)
    _validate_payload(kind, payload, project=project)
    directory = project_dir(project, root_path)
    with _PROCESS_LOCK:
        with file_lock(directory / ".chain.lock"):
            frame = _append_locked(
                project,
                kind,
                payload,
                root_path,
                pending_locators,
            )
    if refresh:
        refresh_views(root_path)
    return frame


def open_project(
    project: Any,
    title: str,
    goal: str,
    owner: str,
    origin: str,
    root: Any = None,
    *,
    refresh: bool = False,
    identity_owner: Any = None,
) -> dict[str, Any] | None:
    project = require_slug(project)
    root_path = ensure_root(root, identity_owner=identity_owner)
    directory = project_dir(project, root_path)
    payload = {
        "project": project,
        "title": _string(title, "title", 200, project),
        "goal": _string(goal, "goal", 2000, ""),
        "owner": _string(owner, "owner", 200, "local-owner"),
        "origin": _string(origin, "origin", 1000, "local"),
        "visibility": VISIBILITY,
    }
    _validate_payload("project.genesis", payload, project=project)
    with _PROCESS_LOCK:
        with file_lock(root_path / ".projects.lock"):
            root_metadata = _validate_root_locked(root_path)
            if directory.exists():
                with file_lock(directory / ".chain.lock"):
                    _load_chain_locked(project, root_path)
                return None
            old_manifest = root_metadata["cell"]
            staging = root_path / (
                f".staging-{project}-{secrets.token_hex(16)}"
            )
            try:
                _mkdir(staging)
                project_rappid = mint_rappid(
                    project,
                    owner=_rappid_owner(
                        root_metadata["identity"]["rappid"]
                    ),
                )
                _atomic_json(
                    staging / "rappid.json",
                    _identity_record(project_rappid, "project", project),
                )
                _atomic_json(
                    staging / "lineage.json",
                    {
                        "schema": PROJECT_LINEAGE_SCHEMA,
                        "parent_rappid": root_metadata["identity"]["rappid"],
                        "origin": payload["origin"],
                    },
                )
                _atomic_json(
                    staging / "manifest.json",
                    _cell_manifest("factory", f"projects/{project}", []),
                )
                frame = build_frame(
                    "project.genesis",
                    project_stream_id(project_rappid),
                    0,
                    payload,
                    None,
                )
                with file_lock(staging / ".chain.lock"):
                    _append_octets(
                        staging / "chain.jsonl",
                        canonical(frame).encode("utf-8") + b"\n",
                    )
                    _atomic_json(staging / "head.json", _head_record([frame]))
                metadata = _validate_project_metadata(staging, project)
                stream_id = project_stream_id(
                    metadata["identity"]["rappid"]
                )
                staged_frames = _load_chain_bytes(
                    _read_bounded(
                        staging / "chain.jsonl",
                        MAX_CHAIN_BYTES,
                        "chain.jsonl",
                    ),
                    project=project,
                    stream_id=stream_id,
                )
                _check_trusted_head(staging, staged_frames, stream_id)
                warnings = _publish_staged_project_locked(
                    root_path,
                    project,
                    staging,
                    old_manifest,
                    "create",
                )
                _validate_root_locked(root_path)
            except (OSError, RappProjectsError):
                if (root_path / ".project-transaction.json").exists():
                    _recover_project_transaction_locked(root_path)
                elif staging.exists():
                    shutil.rmtree(staging)
                raise
    if refresh:
        refresh_views(root_path)
    return CommittedFrame(frame, warnings)


def _verify_receipts(
    frames: list[dict[str, Any]],
    project: str,
    root: Path,
) -> list[dict[str, Any]]:
    broken: list[dict[str, Any]] = []
    for frame in frames:
        for value in _frame_receipts(frame):
            receipt = _validate_receipt(value)
            problem = not receipt["exists"]
            resolved = _resolve_receipt_path(
                receipt["path"], project=project, root=root
            )
            if resolved is None and receipt["exists"]:
                problem = True
            elif resolved is not None and receipt["exists"]:
                if resolved.is_symlink() or not resolved.is_file():
                    problem = True
                else:
                    digest, size = _hash_file(resolved)
                    problem = (
                        digest != receipt["sha256"] or size != receipt["size"]
                    )
            if problem:
                broken.append(receipt)
    return broken


def fold_project(
    project: Any,
    frames: list[dict[str, Any]] | None = None,
    root: Any = None,
    now: datetime | None = None,
) -> dict[str, Any]:
    project = require_slug(project)
    frames = load_chain(project, root) if frames is None else list(frames)
    if not frames:
        raise ChainVerificationError("cannot fold an empty project chain")
    stream_id = frames[0]["stream_id"]
    head = None
    for frame in frames:
        _verify_frame_or_raise(
            frame,
            head=head,
            stream_id=stream_id,
            project=project,
        )
        head = frame
    state: dict[str, Any] = {
        "project": project,
        "rappid": stream_id.rsplit(":", 1)[0],
        "stream_id": stream_id,
        "visibility": VISIBILITY,
        "title": project,
        "goal": "",
        "owner": "",
        "origin": "",
        "state": "active",
        "status": "opened",
        "pct": 0,
        "agents": {},
        "location": "",
        "artifacts": [],
        "receipts": [],
        "blockers": [],
        "next_action": "Assign work",
        "last_handoff": None,
        "last_work_utc": None,
        "last_frame_utc": None,
        "last_frame_hash": None,
        "verified": False,
        "frame_count": len(frames),
    }
    for frame in frames:
        kind = frame["kind"]
        payload = frame["payload"]
        state["last_frame_utc"] = frame["utc"]
        state["last_frame_hash"] = frame["frame_hash"]
        if kind != "project.verify":
            state["last_work_utc"] = frame["utc"]
            state["verified"] = False
        if kind == "project.genesis":
            state.update(
                {
                    "title": payload["title"],
                    "goal": payload["goal"],
                    "owner": payload["owner"],
                    "origin": payload["origin"],
                }
            )
        elif kind == "work.punchin":
            state["agents"][payload["agent"]] = {
                "runtime": payload["runtime"],
                SESSION_ID_FIELD: payload[SESSION_ID_FIELD],
                "role": payload["role"],
                "location": payload["location"],
                "intent": payload["intent"],
                "capabilities": payload["capabilities"],
                "punched_in_utc": frame["utc"],
            }
            state.update(
                {
                    "state": "active",
                    "status": "working",
                    "location": payload["location"],
                    "next_action": payload["intent"],
                }
            )
        elif kind == "work.status":
            state.update(
                {
                    "status": payload["status"],
                    "location": payload["location"],
                    "artifacts": payload["artifacts"],
                    "blockers": payload["blockers"],
                    "next_action": payload["next_action"],
                    "pct": payload["pct"],
                }
            )
            if payload.get("project_state"):
                state["state"] = payload["project_state"]
            elif payload["blockers"]:
                state["state"] = "blocked"
            elif state["state"] != "done":
                state["state"] = "active"
        elif kind == "work.handoff":
            state["agents"].pop(payload["from_agent"], None)
            state["agents"][payload["to_agent"]] = {
                "runtime": "",
                SESSION_ID_FIELD: "",
                "role": "handoff-recipient",
                "location": payload["doc"]["path"],
                "intent": "Review handoff",
                "capabilities": [],
                "punched_in_utc": frame["utc"],
            }
            state["last_handoff"] = payload
            state["location"] = payload["doc"]["path"]
            state["next_action"] = (
                payload["open_questions"][0]
                if payload["open_questions"]
                else "Review handoff"
            )
        elif kind == "work.punchout":
            state["agents"].pop(payload["agent"], None)
            state["receipts"] = payload["receipts"]
            if payload["outcome"] == "done":
                state.update(
                    {
                        "state": "done",
                        "status": "done",
                        "pct": 100,
                        "next_action": "",
                    }
                )
            elif payload["outcome"] == "blocked":
                state.update(
                    {
                        "state": "blocked",
                        "status": "blocked",
                        "blockers": payload["blockers"] or [payload["summary"]],
                    }
                )
            else:
                state.update({"state": "parked", "status": "abandoned"})
        elif kind == "project.verify":
            state["verified"] = payload["verdict"] == "pass"
    current = now or datetime.now(timezone.utc)
    age_hours = None
    if state["last_work_utc"]:
        last_work = datetime.strptime(
            state["last_work_utc"], "%Y-%m-%dT%H:%M:%S.%fZ"
        ).replace(tzinfo=timezone.utc)
        age_hours = max(
            0,
            int((current - last_work).total_seconds() // 3600),
        )
    stale_limit = (
        ACTIVE_STALE_HOURS if state["agents"] else IDLE_STALE_HOURS
    )
    state["age_hours"] = age_hours
    state["stale"] = bool(
        state["state"] not in ("done", "parked")
        and age_hours is not None
        and age_hours >= stale_limit
    )
    return state


def _sanitize_text(
    value: Any,
    root: Path | None = None,
    *,
    portable: bool = False,
) -> str:
    text = str(value or "")
    if portable:
        return ABSOLUTE_PATH.sub("[local-private-path]", text)
    replacements = [
        (str(_AGENT_DIRECTORY), "[agent-directory]"),
        (str(Path.home().resolve()), "[home]"),
    ]
    if root is not None:
        replacements.insert(0, (str(root.resolve()), "[projects-root]"))
    for source, replacement in replacements:
        text = text.replace(source, replacement)
        text = text.replace(source.replace("/", "\\"), replacement)
    return ABSOLUTE_PATH.sub("[local-private-path]", text)


def _public_value(
    value: Any,
    root: Path | None,
    *,
    portable: bool = False,
) -> Any:
    if isinstance(value, str):
        return _sanitize_text(value, root, portable=portable)
    if isinstance(value, list):
        return [
            _public_value(item, root, portable=portable)
            for item in value
        ]
    if isinstance(value, dict):
        public: dict[str, Any] = {}
        for key, child in value.items():
            base_key = _sanitize_text(key, root, portable=portable)
            public_key = base_key
            ordinal = 2
            while public_key in public:
                public_key = f"{base_key}#{ordinal}"
                ordinal += 1
            public[public_key] = _public_value(
                child,
                root,
                portable=portable,
            )
        return public
    return value


def _status_markdown(
    state: dict[str, Any],
    root: Path | None,
    *,
    portable: bool = False,
) -> str:
    public = _public_value(state, root, portable=portable)
    agents = ", ".join(sorted(public["agents"])) or "none"
    blockers = "; ".join(public["blockers"]) or "none"
    artifacts = "\n".join(
        f"- `{item['path']}` — {item['type']} "
        f"({item['sha256'] or 'unavailable'})"
        for item in public["artifacts"]
    ) or "- none"
    return (
        f"# {public['title']}\n\n"
        f"- Project: `{public['project']}`\n"
        f"- RAPPID: `{public['rappid']}`\n"
        f"- Stream: `{public['stream_id']}`\n"
        f"- State: **{public['state']}**\n"
        f"- Status: {public['status']}\n"
        f"- Progress: {public['pct']}%\n"
        f"- Active agents: {agents}\n"
        f"- Location: {public['location'] or 'not declared'}\n"
        f"- Blockers: {blockers}\n"
        f"- Next action: {public['next_action'] or 'none'}\n"
        f"- Frames: {public['frame_count']}\n"
        f"- Verified: {'yes' if public['verified'] else 'no'}\n\n"
        "## Goal\n\n"
        f"{public['goal'] or 'Not declared.'}\n\n"
        "## Artifacts\n\n"
        f"{artifacts}\n"
    )


def _index_value(
    root_metadata: dict[str, Any],
    states: list[dict[str, Any]],
    root: Path,
) -> dict[str, Any]:
    projects = []
    for state in states:
        public = _public_value(state, root)
        projects.append(
            {
                "project": public["project"],
                "rappid": public["rappid"],
                "stream_id": public["stream_id"],
                "title": public["title"],
                "state": public["state"],
                "status": public["status"],
                "pct": public["pct"],
                "agents": sorted(public["agents"]),
                "blockers": public["blockers"],
                "next_action": public["next_action"],
                "last_frame_utc": public["last_frame_utc"],
                "last_frame_hash": public["last_frame_hash"],
                "frame_count": public["frame_count"],
                "verified": public["verified"],
                "stale": public["stale"],
                "visibility": VISIBILITY,
            }
        )
    updated = max(
        (item["last_frame_utc"] for item in projects if item["last_frame_utc"]),
        default=None,
    )
    return {
        "schema": INDEX_SCHEMA,
        "rappid": root_metadata["identity"]["rappid"],
        "visibility": VISIBILITY,
        "updated_utc": updated,
        "projects": projects,
    }


def _board_markdown(index: dict[str, Any]) -> str:
    rows = [
        "# RAPP Projects Board",
        "",
        "| Project | State | Progress | Agents | Next action | Verified |",
        "|---|---:|---:|---|---|---:|",
    ]
    for item in index["projects"]:
        rows.append(
            "| {project} | {state} | {pct}% | {agents} | {next_action} | {verified} |".format(
                project=item["project"],
                state=item["state"],
                pct=item["pct"],
                agents=", ".join(item["agents"]) or "none",
                next_action=item["next_action"] or "none",
                verified="yes" if item["verified"] else "no",
            )
        )
    if not index["projects"]:
        rows.append("| none | — | — | — | Open a project | — |")
    return "\n".join(rows) + "\n"


def _catchup_markdown(index: dict[str, Any]) -> str:
    rows = ["# RAPP Projects Catchup", ""]
    for item in index["projects"]:
        rows.extend(
            [
                f"## {item['project']}",
                "",
                f"- State: {item['state']} ({item['pct']}%)",
                f"- Status: {item['status']}",
                f"- Agents: {', '.join(item['agents']) or 'none'}",
                f"- Blockers: {'; '.join(item['blockers']) or 'none'}",
                f"- Next: {item['next_action'] or 'none'}",
                f"- Head: `{item['last_frame_hash']}`",
                "",
            ]
        )
    if not index["projects"]:
        rows.extend(["No projects are open.", ""])
    return "\n".join(rows)


def refresh_views(root: Any = None) -> list[dict[str, Any]]:
    """Rebuild every derived view only after all project chains verify."""
    root_path = ensure_root(root)
    with _PROCESS_LOCK:
        with file_lock(root_path / ".projects.lock"):
            with file_lock(root_path / ".views.lock"):
                root_metadata = _validate_root_locked(root_path)
                states: list[dict[str, Any]] = []
                status_documents: list[tuple[Path, str]] = []
                for project in root_metadata["projects"]:
                    directory = project_dir(project, root_path)
                    with file_lock(directory / ".chain.lock"):
                        frames = _load_chain_locked(project, root_path)
                        state = fold_project(project, frames, root_path)
                        state["verified"] = bool(
                            state["verified"]
                            and not _verify_receipts(
                                frames,
                                project,
                                root_path,
                            )
                        )
                    states.append(state)
                    status_documents.append(
                        (directory / "STATUS.md", _status_markdown(state, root_path))
                    )
                index = _index_value(root_metadata, states, root_path)
                board = _board_markdown(index)
                catchup = _catchup_markdown(index)
                for path, text in status_documents:
                    _atomic_bytes(path, text.encode("utf-8"))
                _atomic_json(root_path / "index.json", index, pretty=True)
                _atomic_bytes(root_path / "BOARD.md", board.encode("utf-8"))
                _atomic_bytes(root_path / "CATCHUP.md", catchup.encode("utf-8"))
    return states


def verify_project(
    project: Any,
    root: Any = None,
    *,
    append_verdict: bool = True,
    refresh: bool = False,
) -> dict[str, Any]:
    project = require_slug(project)
    root_path = ensure_root(root)
    directory = project_dir(project, root_path)
    with _PROCESS_LOCK:
        with file_lock(directory / ".chain.lock"):
            frames = _load_chain_locked(project, root_path)
            broken = _verify_receipts(frames, project, root_path)
            verdict = "fail" if broken else "pass"
            frame = None
            if append_verdict:
                head = frames[-1]
                frame = _append_locked(
                    project,
                    "project.verify",
                    {
                        "project": project,
                        "verdict": verdict,
                        "broken_receipts": broken,
                        "verified_frames": len(frames),
                        "head_frame_hash": head["frame_hash"],
                    },
                    root_path,
                )
    if append_verdict and refresh:
        refresh_views(root_path)
    return {
        "project": project,
        "verdict": verdict,
        "verified_frames": len(frames),
        "head_frame_hash": frames[-1]["frame_hash"],
        "broken_receipts": broken,
        "frame": frame,
    }


def inspect_project(project: Any, root: Any = None) -> dict[str, Any]:
    project = require_slug(project)
    root_path = ensure_root(root)
    directory = project_dir(project, root_path)
    with _PROCESS_LOCK:
        with file_lock(directory / ".chain.lock"):
            metadata = _validate_project_metadata(directory, project)
            frames = _load_chain_locked(project, root_path)
            state = fold_project(project, frames, root_path)
            broken = _verify_receipts(frames, project, root_path)
            state["verified"] = bool(state["verified"] and not broken)
    return {
        "project": project,
        "identity": metadata["identity"],
        "cell": metadata["cell"],
        "lineage": _public_value(metadata["lineage"], root_path),
        "state": _public_value(state, root_path),
        "verification": {
            "verdict": "fail" if broken else "pass",
            "verified_frames": len(frames),
            "head_frame_hash": frames[-1]["frame_hash"],
            "broken_receipts": broken,
        },
    }


def _egg_agent_bytes(project: str, rappid: str) -> bytes:
    return (
        '"""Metadata-only shell for a RAPP Projects rapplication egg."""\n'
        f"PROJECT = {project!r}\n"
        f"RAPPID = {rappid!r}\n"
    ).encode("utf-8")


def _zip_bytes(entries: list[tuple[str, bytes]]) -> bytes:
    """Write the deterministic stored-only ZIP profile required by RAPP/1."""
    local_parts: list[bytes] = []
    central_parts: list[bytes] = []
    offset = 0
    dos_time = 0
    dos_date = (1 << 5) | 1
    flags = 0x0800
    for name, data in entries:
        name_bytes = name.encode("utf-8")
        crc = zlib.crc32(data) & 0xFFFFFFFF
        local = struct.pack(
            "<IHHHHHIIIHH",
            0x04034B50,
            20,
            flags,
            0,
            dos_time,
            dos_date,
            crc,
            len(data),
            len(data),
            len(name_bytes),
            0,
        ) + name_bytes + data
        central = struct.pack(
            "<IHHHHHHIIIHHHHHII",
            0x02014B50,
            20,
            20,
            flags,
            0,
            dos_time,
            dos_date,
            crc,
            len(data),
            len(data),
            len(name_bytes),
            0,
            0,
            0,
            0,
            0,
            offset,
        ) + name_bytes
        local_parts.append(local)
        central_parts.append(central)
        offset += len(local)
    central_directory = b"".join(central_parts)
    if len(entries) > 0xFFFF or offset > 0xFFFFFFFF:
        raise RappProjectsError("project egg exceeds classic ZIP limits")
    end = struct.pack(
        "<IHHHHIIH",
        0x06054B50,
        0,
        0,
        len(entries),
        len(entries),
        len(central_directory),
        offset,
        0,
    )
    value = b"".join(local_parts) + central_directory + end
    if len(value) > MAX_EGG_BYTES:
        raise RappProjectsError("project egg exceeds the byte limit")
    return value


def _egg_path_valid(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    if value != unicodedata.normalize("NFC", value):
        return False
    if value.startswith("/") or "\\" in value:
        return False
    parts = value.split("/")
    return all(part not in ("", ".", "..") for part in parts)


def _export_files(
    project: str,
    root: Path,
    frames: list[dict[str, Any]],
) -> dict[str, bytes]:
    directory = project_dir(project, root)
    metadata = _validate_project_metadata(directory, project)
    state = fold_project(project, frames, root)
    status = _status_markdown(state, None, portable=True).encode("utf-8")
    rappid = metadata["identity"]["rappid"]
    return {
        "STATUS.md": status,
        "agent.py": _egg_agent_bytes(project, rappid),
        "cell/lineage.json": canonical(metadata["lineage"]).encode("utf-8"),
        "cell/manifest.json": canonical(metadata["cell"]).encode("utf-8"),
        "chain.jsonl": (directory / "chain.jsonl").read_bytes(),
        "rappid.json": canonical(metadata["identity"]).encode("utf-8"),
    }


def export_project_egg(
    project: Any,
    output: Any = None,
    root: Any = None,
    *,
    owner_approved: bool = False,
) -> dict[str, Any]:
    if owner_approved is not True:
        raise PermissionError("export requires owner_approved=true")
    project = require_slug(project)
    root_path = ensure_root(root)
    directory = project_dir(project, root_path)
    with _PROCESS_LOCK:
        with file_lock(directory / ".chain.lock"):
            frames = _load_chain_locked(project, root_path)
            broken = _verify_receipts(frames, project, root_path)
            if broken:
                raise RappProjectsError(
                    "project has broken artifact receipts; export refused"
                )
            files = _export_files(project, root_path, frames)
            identity = _validate_identity(
                _strict_loads(files["rappid.json"]),
                kind="project",
                name=project,
            )
            contents = [
                {"path": path, "hash": Hb("rapp/1:egg", files[path])}
                for path in sorted(files, key=lambda item: item.encode("utf-8"))
            ]
            head = frames[-1]
            manifest = {
                "schema": EGG_SCHEMA,
                "variant": EGG_VARIANT,
                "rappid": identity["rappid"],
                "created_utc": head["utc"],
                "contents": contents,
                "payload": {
                    "schema": EXPORT_SCHEMA,
                    "project": project,
                    "stream_id": head["stream_id"],
                    "visibility": VISIBILITY,
                    "frame_count": len(frames),
                    "head_frame_hash": head["frame_hash"],
                    "content": "chain-rappid-status-cell-metadata-only",
                    "warning": EGG_WARNING,
                },
                "sig": None,
            }
            manifest_bytes = canonical(manifest).encode("utf-8")
            archive = _zip_bytes(
                [("manifest.json", manifest_bytes)]
                + [(item["path"], files[item["path"]]) for item in contents]
            )
            destination = directory / "PROJECT.egg"
            if destination.is_symlink():
                raise RappProjectsError("egg output cannot be a symbolic link")
            if output not in (None, ""):
                requested = Path(str(output)).expanduser()
                if not requested.is_absolute():
                    requested = directory / requested
                if requested.is_symlink():
                    raise RappProjectsError(
                        "egg output cannot be a symbolic link"
                    )
                if (
                    requested.name != destination.name
                    or requested.parent.resolve() != directory
                ):
                    raise RappProjectsError(
                        "egg output must be the selected project's PROJECT.egg"
                    )
            if destination.exists() and not destination.is_file():
                raise RappProjectsError("egg output must be a regular file")
            _atomic_bytes(destination, archive)
    egg_hash = H(
        "rapp/1:egg-manifest",
        {key: value for key, value in manifest.items() if key != "sig"},
    )
    return {
        "project": project,
        "egg": str(destination),
        "egg_hash": egg_hash,
        "sha256": hashlib.sha256(archive).hexdigest(),
        "bytes": len(archive),
        "visibility": VISIBILITY,
        "owner_approved": True,
    }


def _verify_egg_manifest(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != EGG_KEYS:
        raise EggVerificationError("egg manifest must have exactly seven keys")
    if value["schema"] != EGG_SCHEMA or value["variant"] != EGG_VARIANT:
        raise EggVerificationError("egg is not a rapp/1 rapplication")
    if not _valid_rappid(value["rappid"]):
        raise EggVerificationError("egg rappid is invalid")
    if not _valid_utc(value["created_utc"]):
        raise EggVerificationError("egg created_utc is invalid")
    if value["sig"] is not None:
        raise EggVerificationError("local project eggs must be unsigned")
    if not isinstance(value["contents"], list) or not value["contents"]:
        raise EggVerificationError("egg contents must be a non-empty list")
    if len(value["contents"]) > MAX_EGG_ENTRIES:
        raise EggVerificationError("egg has too many entries")
    paths = []
    for item in value["contents"]:
        if (
            not isinstance(item, dict)
            or set(item) != {"path", "hash"}
            or not _egg_path_valid(item["path"])
            or not isinstance(item["hash"], str)
            or not HEX64.fullmatch(item["hash"])
        ):
            raise EggVerificationError("egg content record is invalid")
        paths.append(item["path"])
    expected_order = sorted(paths, key=lambda path: path.encode("utf-8"))
    if paths != expected_order or len(set(paths)) != len(paths):
        raise EggVerificationError("egg content paths are unsorted or duplicated")
    payload = value["payload"]
    if not isinstance(payload, dict) or set(payload) != EXPORT_PAYLOAD_KEYS:
        raise EggVerificationError("project export payload key set is invalid")
    if (
        payload["schema"] != EXPORT_SCHEMA
        or payload["visibility"] != VISIBILITY
        or payload["content"] != "chain-rappid-status-cell-metadata-only"
        or payload["warning"] != EGG_WARNING
    ):
        raise EggVerificationError("project export payload is invalid")
    project = require_slug(payload["project"])
    if not _valid_rappid(value["rappid"], slug=project):
        raise EggVerificationError("egg identity is bound to another project")
    if payload["stream_id"] != project_stream_id(value["rappid"]):
        raise EggVerificationError("egg stream binding is invalid")
    if (
        not isinstance(payload["frame_count"], int)
        or isinstance(payload["frame_count"], bool)
        or payload["frame_count"] < 1
        or payload["frame_count"] > MAX_SAFE_INTEGER
        or not isinstance(payload["head_frame_hash"], str)
        or not HEX64.fullmatch(payload["head_frame_hash"])
    ):
        raise EggVerificationError("egg head metadata is invalid")
    canonical(value)
    return dict(value)


def verify_project_egg(path: Any) -> dict[str, Any]:
    source = Path(str(path)).expanduser().resolve()
    if not source.is_file() or source.is_symlink():
        raise EggVerificationError("egg must be a regular file")
    try:
        raw = _read_bounded(source, MAX_EGG_BYTES, "egg")
    except RappProjectsError as exc:
        raise EggVerificationError(str(exc)) from exc
    try:
        archive = zipfile.ZipFile(io.BytesIO(raw), "r")
    except zipfile.BadZipFile as exc:
        raise EggVerificationError("egg is not a valid ZIP") from exc
    with archive:
        infos = archive.infolist()
        if not infos or len(infos) > MAX_EGG_ENTRIES + 1:
            raise EggVerificationError("egg entry count is invalid")
        if infos[0].filename != "manifest.json":
            raise EggVerificationError("manifest.json must be the first entry")
        if any(
            info.compress_type != zipfile.ZIP_STORED
            or info.file_size != info.compress_size
            or info.file_size > MAX_EGG_BYTES
            for info in infos
        ) or sum(info.file_size for info in infos) > MAX_EGG_BYTES:
            raise EggVerificationError("egg entries exceed the stored-only limits")
        try:
            manifest_bytes = archive.read(infos[0])
        except (OSError, RuntimeError, zipfile.BadZipFile) as exc:
            raise EggVerificationError("cannot read egg manifest") from exc
        manifest = _verify_egg_manifest(_strict_loads(manifest_bytes))
        if manifest_bytes != canonical(manifest).encode("utf-8"):
            raise EggVerificationError("egg manifest bytes are not canonical")
        expected_names = ["manifest.json"] + [
            item["path"] for item in manifest["contents"]
        ]
        if [info.filename for info in infos] != expected_names:
            raise EggVerificationError("egg archive entry set or order is invalid")
        files: dict[str, bytes] = {}
        for info, item in zip(infos[1:], manifest["contents"]):
            if (
                info.compress_type != zipfile.ZIP_STORED
                or info.flag_bits != 0x0800
                or info.date_time != (1980, 1, 1, 0, 0, 0)
                or info.extra
                or info.comment
                or info.external_attr != 0
            ):
                raise EggVerificationError("egg ZIP metadata is not deterministic")
            try:
                body = archive.read(info)
            except (OSError, RuntimeError, zipfile.BadZipFile) as exc:
                raise EggVerificationError("cannot read egg content") from exc
            if Hb("rapp/1:egg", body) != item["hash"]:
                raise EggVerificationError(f"egg hash mismatch: {item['path']}")
            files[item["path"]] = body
        if len([path for path in files if path == "agent.py"]) != 1:
            raise EggVerificationError("rapplication must contain exactly agent.py")
        required = {
            "STATUS.md",
            "agent.py",
            "cell/lineage.json",
            "cell/manifest.json",
            "chain.jsonl",
            "rappid.json",
        }
        if set(files) != required:
            raise EggVerificationError("project egg contains non-metadata files")
        deterministic = _zip_bytes(
            [("manifest.json", manifest_bytes)]
            + [(item["path"], files[item["path"]]) for item in manifest["contents"]]
        )
        if deterministic != raw:
            raise EggVerificationError("egg container bytes are non-deterministic")

    payload = manifest["payload"]
    project = payload["project"]
    identity = _validate_identity(
        _strict_loads(files["rappid.json"]),
        kind="project",
        name=project,
    )
    if identity["rappid"] != manifest["rappid"]:
        raise EggVerificationError("rappid.json does not match the egg manifest")
    cell = _validate_cell(_strict_loads(files["cell/manifest.json"]))
    if cell["layer"] != "factory" or cell["path"] != f"projects/{project}":
        raise EggVerificationError("egg project cell is invalid")
    lineage = _validate_lineage(
        _strict_loads(files["cell/lineage.json"]),
        schema=PROJECT_LINEAGE_SCHEMA,
    )
    if files["agent.py"] != _egg_agent_bytes(project, identity["rappid"]):
        raise EggVerificationError("metadata-only agent.py marker is invalid")
    try:
        frames = _load_chain_bytes(
            files["chain.jsonl"],
            project=project,
            stream_id=payload["stream_id"],
        )
    except ChainVerificationError as exc:
        raise EggVerificationError(str(exc)) from exc
    if (
        len(frames) != payload["frame_count"]
        or frames[-1]["frame_hash"] != payload["head_frame_hash"]
        or frames[-1]["utc"] != manifest["created_utc"]
    ):
        raise EggVerificationError("egg chain head metadata does not match")
    state = fold_project(project, frames)
    expected_status = _status_markdown(
        state,
        None,
        portable=True,
    ).encode("utf-8")
    if files["STATUS.md"] != expected_status:
        raise EggVerificationError("egg STATUS.md is not derived from its chain")
    egg_hash = H(
        "rapp/1:egg-manifest",
        {key: value for key, value in manifest.items() if key != "sig"},
    )
    return {
        "source": source,
        "raw": raw,
        "manifest": manifest,
        "files": files,
        "frames": frames,
        "identity": identity,
        "cell": cell,
        "lineage": lineage,
        "egg_hash": egg_hash,
    }


def _frame_hashes(frames: list[dict[str, Any]]) -> list[str]:
    return [frame["frame_hash"] for frame in frames]


def import_project_egg(
    path: Any,
    root: Any = None,
    *,
    refresh: bool = False,
    identity_owner: Any = None,
) -> dict[str, Any]:
    """Verify the full egg first, then create or fast-forward without reparenting."""
    verified = verify_project_egg(path)
    manifest = verified["manifest"]
    project = manifest["payload"]["project"]
    incoming_frames = verified["frames"]
    root_path = ensure_root(root, identity_owner=identity_owner)
    directory = project_dir(project, root_path)
    imported_frames = 0
    created = False
    storage_warnings: list[dict[str, str]] = []
    with _PROCESS_LOCK:
        with file_lock(root_path / ".projects.lock"):
            root_metadata = _validate_root_locked(root_path)
            if directory.exists():
                with file_lock(directory / ".chain.lock"):
                    metadata = _validate_project_metadata(directory, project)
                    if metadata["identity"] != verified["identity"]:
                        raise DivergentChainError(
                            "local project uses a different RAPPID"
                        )
                    local_frames = _load_chain_locked(project, root_path)
                    local_hashes = _frame_hashes(local_frames)
                    incoming_hashes = _frame_hashes(incoming_frames)
                    common = 0
                    for local_hash, incoming_hash in zip(
                        local_hashes, incoming_hashes
                    ):
                        if local_hash != incoming_hash:
                            break
                        common += 1
                    if common < min(len(local_hashes), len(incoming_hashes)):
                        raise DivergentChainError(
                            "divergent project histories fork"
                        )
                    if len(incoming_frames) < len(local_frames):
                        raise DivergentChainError(
                            "egg is stale and would roll back the local head"
                        )
                    extension = incoming_frames[len(local_frames) :]
                    storage_warnings.extend(
                        _commit_chain_extension_locked(
                            directory,
                            project,
                            local_frames,
                            extension,
                        )
                    )
                    imported_frames = len(extension)
            else:
                old_manifest = root_metadata["cell"]
                staging = (
                    root_path
                    / f".staging-{project}-{secrets.token_hex(16)}"
                )
                try:
                    if _rappid_owner(
                        verified["identity"]["rappid"]
                    ) != _rappid_owner(root_metadata["identity"]["rappid"]):
                        raise RappProjectsError(
                            "imported project owner does not match root authority"
                        )
                    _mkdir(staging)
                    _atomic_json(staging / "rappid.json", verified["identity"])
                    _atomic_json(staging / "manifest.json", verified["cell"])
                    _atomic_json(staging / "lineage.json", verified["lineage"])
                    _atomic_bytes(
                        staging / "chain.jsonl",
                        verified["files"]["chain.jsonl"],
                    )
                    _atomic_json(
                        staging / "head.json",
                        _head_record(incoming_frames),
                    )
                    metadata = _validate_project_metadata(staging, project)
                    stream_id = project_stream_id(
                        metadata["identity"]["rappid"]
                    )
                    staged_frames = _load_chain_bytes(
                        _read_bounded(
                            staging / "chain.jsonl",
                            MAX_CHAIN_BYTES,
                            "chain.jsonl",
                        ),
                        project=project,
                        stream_id=stream_id,
                    )
                    _check_trusted_head(staging, staged_frames, stream_id)
                    storage_warnings.extend(
                        _publish_staged_project_locked(
                            root_path,
                            project,
                            staging,
                            old_manifest,
                            "import",
                        )
                    )
                    _validate_root_locked(root_path)
                    imported_frames = len(incoming_frames)
                    created = True
                except (OSError, RappProjectsError):
                    if (root_path / ".project-transaction.json").exists():
                        _recover_project_transaction_locked(root_path)
                    elif staging.exists():
                        shutil.rmtree(staging)
                    raise
    if refresh:
        refresh_views(root_path)
    return {
        "project": project,
        "created": created,
        "imported_frames": imported_frames,
        "head_frame_hash": incoming_frames[-1]["frame_hash"],
        "egg_hash": verified["egg_hash"],
        "visibility": VISIBILITY,
        "storage_warnings": storage_warnings,
    }


PROTOCOL = {
    "schema": "rapp-projects-protocol/1",
    "agent": __manifest__["name"],
    "version": "1.0.3",
    "operations": list(OPERATIONS),
    "root_precedence": [
        "explicit root",
        "RAPP_PROJECTS_ROOT",
        "~/.rapp/projects-control",
    ],
    "identity": {
        "owner": (
            "explicit identity_owner or RAPP_PROJECTS_OWNER when minting root"
        ),
        "mint": "UUIDv4 keyless RAPPID once per root and project",
        "project_stream": "<project-rappid>:project",
        "name_hash_identity": False,
    },
    "frame": {
        "spec": SPEC,
        "keys": sorted(FRAME_KEYS),
        "kinds": sorted(FRAME_KINDS),
        "payload_hash": 'H("rapp/1:particle", payload)',
        "frame_hash": 'H("rapp/1:wave", frame without frame_hash and sig)',
        "prev": "previous payload_hash",
        "prev_wave": None,
        "sig": (
            "producer emits null; signed input requires exact detached JWS "
            "plus a caller-supplied RAPP registry trust verifier"
        ),
        "verification_order": ["1", "1a", "2", "3", "4", "5", "6"],
        "limits": {
            "canonical_bytes": MAX_CANONICAL_BYTES,
            "depth": MAX_DEPTH,
            "numbers": "finite exact binary64 round-trip",
            "surrogates": "unpaired refused",
        },
    },
    "cells": {
        "schema": CELL_SCHEMA,
        "manifest_keys": sorted(CELL_KEYS),
        "root_layer": "leviathan",
        "project_layer": "factory",
        "lineage": "separate lineage.json data",
    },
    "eggs": {
        "schema": EGG_SCHEMA,
        "variant": EGG_VARIANT,
        "visibility": VISIBILITY,
        "owner_approval_required": True,
        "compression": "stored",
        "timestamp": "1980-01-01T00:00:00Z",
        "contents": (
            "verified chain, rappid, derived status, cell metadata, and the "
            "standard metadata-only agent.py marker; never artifact bodies"
        ),
    },
    "boundaries": {
        "network": False,
        "artifact_bodies_copied": False,
        "external_receipts": (
            "private locators excluded from eggs; unresolved locators fail "
            "until owner-approved matching bytes are rebound"
        ),
        "egg_output": "<root>/<project>/PROJECT.egg only",
        "persistence": (
            "atomic chain replacement, rolling trusted chain digest, and "
            "fsynced append/root/project journals"
        ),
        "corruption_policy": "fail closed",
        "fork_policy": "refuse divergence",
    },
}


class RappProjectsAgent(BasicAgent):
    """Single-file BasicAgent wrapper for the public RAPP Projects protocol."""

    def __init__(self):
        self.name = "RappProjects"
        self.metadata = AGENT_METADATA
        super().__init__(name=self.name, metadata=self.metadata)

    def to_tool(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.metadata["description"],
                "parameters": self.metadata["parameters"],
            },
        }

    def system_context(self) -> str:
        return (
            "<rapp_projects protocol=\"rapp-projects-protocol/1\">"
            "Use punchin before substantial work, append status or handoff "
            "frames, then punchout and verify. Chains are authoritative; "
            "derived views are rebuilt only from verified histories."
            "</rapp_projects>"
        )

    def _result(self, operation: str, **values: Any) -> str:
        return json.dumps(
            {"status": "ok", "operation": operation, **values},
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )

    def _result_after_refresh(
        self,
        operation: str,
        root: Path,
        **values: Any,
    ) -> str:
        storage_warnings = values.pop("_storage_warnings", [])
        if storage_warnings:
            values["storage_warnings"] = storage_warnings
        try:
            refresh_views(root)
        except (RappProjectsError, OSError) as exc:
            values["view_refresh"] = {
                "status": "error",
                "error": {
                    "code": getattr(exc, "code", "view-refresh-failed"),
                    "message": _sanitize_text(str(exc), root)[:MAX_ERROR_CHARS],
                },
            }
        return self._result(operation, **values)

    def _error(
        self,
        operation: str,
        exc: Exception,
        root: Path | None = None,
    ) -> str:
        message = _sanitize_text(str(exc), root)[:MAX_ERROR_CHARS]
        code = getattr(exc, "code", None)
        if not code:
            if isinstance(exc, PermissionError):
                code = "owner-approval-required"
            elif isinstance(exc, OSError):
                code = "io-error"
            else:
                code = "invalid-request"
        error: dict[str, Any] = {"code": code, "message": message}
        step = getattr(exc, "step", None)
        if step is not None:
            error["step"] = step
        return json.dumps(
            {"status": "error", "operation": operation, "error": error},
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )

    def perform(self, **kwargs: Any) -> str:
        if "operation" in kwargs:
            operation_value = kwargs["operation"]
        elif "action" in kwargs:
            operation_value = kwargs["action"]
        else:
            operation_value = None
        operation = (
            operation_value.strip().lower()[:64]
            if isinstance(operation_value, str)
            else ("missing" if operation_value is None else "invalid")
        )
        root_path: Path | None = None
        try:
            canonical(dict(kwargs))
            unknown = sorted(
                set(kwargs) - set(AGENT_PARAMETERS["properties"])
            )
            if unknown:
                raise RappProjectsError(
                    "unknown argument(s): " + ", ".join(unknown)
                )
            if operation_value is None:
                raise RappProjectsError(
                    "operation is required; action is a compatibility alias"
                )
            if operation not in OPERATIONS:
                raise RappProjectsError("unknown operation")
            if operation == "protocol":
                return self._result(operation, protocol=PROTOCOL)

            if operation == "import":
                egg = kwargs.get("egg")
                if not isinstance(egg, (str, os.PathLike)) or not str(egg):
                    raise RappProjectsError("import requires egg")
                root_path = projects_root(kwargs.get("root"))
                result = import_project_egg(
                    egg,
                    root_path,
                    refresh=False,
                    identity_owner=kwargs.get("identity_owner"),
                )
                return self._result_after_refresh(
                    operation,
                    root_path,
                    **result,
                )

            root_path = ensure_root(
                kwargs.get("root"),
                identity_owner=kwargs.get("identity_owner"),
            )
            if operation == "open":
                raw_project = kwargs.get("project")
                project = (
                    require_slug(raw_project)
                    if raw_project not in (None, "")
                    else slugify(kwargs.get("title"))
                )
                frame = open_project(
                    project,
                    _string(kwargs.get("title"), "title", 200, project),
                    _string(kwargs.get("goal"), "goal", 2000, ""),
                    _string(kwargs.get("owner"), "owner", 200, "local-owner"),
                    _string(kwargs.get("origin"), "origin", 1000, "local"),
                    root_path,
                    refresh=False,
                    identity_owner=kwargs.get("identity_owner"),
                )
                frames = load_chain(project, root_path)
                return self._result_after_refresh(
                    operation,
                    root_path,
                    project=project,
                    created=frame is not None,
                    rappid=frames[0]["stream_id"].rsplit(":", 1)[0],
                    stream_id=frames[0]["stream_id"],
                    seq=frame["seq"] if frame else frames[-1]["seq"],
                    frame_hash=(
                        frame["frame_hash"] if frame else frames[-1]["frame_hash"]
                    ),
                    _storage_warnings=getattr(
                        frame,
                        "storage_warnings",
                        [],
                    ),
                )

            if operation == "board":
                states = refresh_views(root_path)
                return self._result(
                    operation,
                    root="projects://",
                    board="projects://BOARD.md",
                    catchup="projects://CATCHUP.md",
                    index="projects://index.json",
                    projects=[
                        {
                            "project": state["project"],
                            "state": state["state"],
                            "status": state["status"],
                            "pct": state["pct"],
                            "agents": sorted(
                                _public_value(
                                    state["agents"],
                                    root_path,
                                )
                            ),
                            "blockers": _public_value(
                                state["blockers"], root_path
                            ),
                            "next_action": _sanitize_text(
                                state["next_action"], root_path
                            ),
                            "verified": state["verified"],
                            "stale": state["stale"],
                        }
                        for state in states
                    ],
                )

            project = require_slug(kwargs.get("project"))

            if operation == "punchin":
                frame = append_frame(
                    project,
                    "work.punchin",
                    {
                        "project": project,
                        "agent": _string(
                            kwargs.get("agent"), "agent", 200, "unknown-agent"
                        ),
                        "runtime": _string(
                            kwargs.get("runtime"),
                            "runtime",
                            200,
                            str(kwargs.get("agent") or "unknown-runtime"),
                        ),
                        SESSION_ID_FIELD: _string(
                            kwargs.get("session_id"), "session_id", 500, ""
                        ),
                        "location": _string(
                            kwargs.get("location"),
                            "location",
                            1000,
                            "not-declared",
                        ),
                        "intent": _string(
                            kwargs.get("intent"),
                            "intent",
                            2000,
                            "Work the project",
                        ),
                        "role": _string(
                            kwargs.get("role"), "role", 200, "worker"
                        ),
                        "capabilities": _string_list(
                            kwargs.get("capabilities"),
                            "capabilities",
                            item_limit=200,
                        ),
                    },
                    root_path,
                    refresh=False,
                )
                return self._result_after_refresh(
                    operation,
                    root_path,
                    project=project,
                    seq=frame["seq"],
                    frame_hash=frame["frame_hash"],
                    _storage_warnings=frame.storage_warnings,
                )

            if operation == "status":
                pending_locators: dict[str, str] = {}
                pct = kwargs.get("pct", 0)
                if not isinstance(pct, int) or isinstance(pct, bool):
                    raise RappProjectsError("pct must be an integer")
                next_action = _string(
                    kwargs.get("next_action"), "next_action", 2000, None
                )
                payload: dict[str, Any] = {
                    "project": project,
                    "agent": _string(
                        kwargs.get("agent"), "agent", 200, "unknown-agent"
                    ),
                    "location": _string(
                        kwargs.get("location"),
                        "location",
                        1000,
                        "not-declared",
                    ),
                    "status": _string(
                        kwargs.get("status"), "status", 500, "working"
                    ),
                    "artifacts": _receipt_list(
                        kwargs.get("artifacts"),
                        project,
                        root_path,
                        pending_locators,
                    ),
                    "blockers": _string_list(
                        kwargs.get("blockers"), "blockers", item_limit=1000
                    ),
                    "next_action": next_action,
                    "pct": pct,
                }
                if kwargs.get("project_state") is not None:
                    payload["project_state"] = _string(
                        kwargs["project_state"], "project_state", 20
                    )
                frame = append_frame(
                    project,
                    "work.status",
                    payload,
                    root_path,
                    refresh=False,
                    pending_locators=pending_locators,
                )
                return self._result_after_refresh(
                    operation,
                    root_path,
                    project=project,
                    seq=frame["seq"],
                    frame_hash=frame["frame_hash"],
                    _storage_warnings=frame.storage_warnings,
                )

            if operation == "handoff":
                pending_locators = {}
                document = artifact_receipt(
                    kwargs.get("doc"),
                    project,
                    root_path,
                    pending_locators=pending_locators,
                )
                if not document["exists"]:
                    raise RappProjectsError(
                        "handoff document must exist when its receipt is recorded"
                    )
                frame = append_frame(
                    project,
                    "work.handoff",
                    {
                        "project": project,
                        "from_agent": _string(
                            kwargs.get("from_agent"),
                            "from_agent",
                            200,
                            "unknown-agent",
                        ),
                        "to_agent": _string(
                            kwargs.get("to_agent"),
                            "to_agent",
                            200,
                            "unassigned",
                        ),
                        "doc": document,
                        "open_questions": _string_list(
                            kwargs.get("open_questions"),
                            "open_questions",
                            item_limit=1000,
                        ),
                    },
                    root_path,
                    refresh=False,
                    pending_locators=pending_locators,
                )
                return self._result_after_refresh(
                    operation,
                    root_path,
                    project=project,
                    seq=frame["seq"],
                    frame_hash=frame["frame_hash"],
                    doc=document,
                    _storage_warnings=frame.storage_warnings,
                )

            if operation == "punchout":
                pending_locators = {}
                frame = append_frame(
                    project,
                    "work.punchout",
                    {
                        "project": project,
                        "agent": _string(
                            kwargs.get("agent"), "agent", 200, "unknown-agent"
                        ),
                        "outcome": _string(
                            kwargs.get("outcome"), "outcome", 20, "done"
                        ),
                        "receipts": _receipt_list(
                            kwargs.get("receipts"),
                            project,
                            root_path,
                            pending_locators,
                        ),
                        "summary": _string(
                            kwargs.get("summary"), "summary", 4000, ""
                        ),
                        "blockers": _string_list(
                            kwargs.get("blockers"),
                            "blockers",
                            item_limit=1000,
                        ),
                    },
                    root_path,
                    refresh=False,
                    pending_locators=pending_locators,
                )
                return self._result_after_refresh(
                    operation,
                    root_path,
                    project=project,
                    seq=frame["seq"],
                    frame_hash=frame["frame_hash"],
                    _storage_warnings=frame.storage_warnings,
                )

            if operation == "verify":
                binding_result = None
                if kwargs.get("receipt_bindings") is not None:
                    binding_result = bind_receipt_locators(
                        project,
                        kwargs["receipt_bindings"],
                        root_path,
                        owner_approved=kwargs.get("owner_approved") is True,
                    )
                result = verify_project(
                    project,
                    root_path,
                    append_verdict=True,
                    refresh=False,
                )
                frame = result.pop("frame")
                if binding_result is not None:
                    result["receipt_bindings"] = binding_result
                return self._result_after_refresh(
                    operation,
                    root_path,
                    **result,
                    seq=frame["seq"],
                    verification_frame_hash=frame["frame_hash"],
                    _storage_warnings=frame.storage_warnings,
                )

            if operation == "inspect":
                return self._result(
                    operation, **inspect_project(project, root_path)
                )

            if operation == "export":
                result = export_project_egg(
                    project,
                    kwargs.get("output"),
                    root_path,
                    owner_approved=kwargs.get("owner_approved") is True,
                )
                return self._result(operation, **result)

            raise AssertionError("unreachable operation")
        except Exception as exc:
            return self._error(operation, exc, root_path)


def _main(argv: list[str]) -> int:
    agent = RappProjectsAgent()
    if "--tool" in argv:
        if argv != ["--tool"]:
            print(
                agent._error(
                    "tool",
                    RappProjectsError("--tool does not accept additional arguments"),
                )
            )
            return 1
        print(
            json.dumps(
                agent.to_tool(),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 0
    if len(argv) > 1:
        print(
            agent._error(
                "input",
                RappProjectsError("accepts exactly one JSON object argument"),
            )
        )
        return 1
    try:
        if argv:
            raw: str | bytes = argv[0]
        else:
            raw = sys.stdin.buffer.read(MAX_CANONICAL_BYTES + 1)
        if not raw or (isinstance(raw, bytes) and not raw.strip()) or (
            isinstance(raw, str) and not raw.strip()
        ):
            raw = "{}"
        request = _strict_loads(raw)
        if not isinstance(request, dict):
            raise RappProjectsError("standalone input must be one JSON object")
        print(agent.perform(**request))
        return 0
    except Exception as exc:
        print(agent._error("input", exc))
        return 1


__all__ = [
    "ChainVerificationError",
    "CommittedFrame",
    "DivergentChainError",
    "EggVerificationError",
    "FRAME_KEYS",
    "FRAME_KINDS",
    "H",
    "Hb",
    "OPERATIONS",
    "PROTOCOL",
    "RappProjectsAgent",
    "RappProjectsError",
    "append_frame",
    "artifact_receipt",
    "bind_receipt_locators",
    "build_frame",
    "canonical",
    "ensure_root",
    "export_project_egg",
    "fold_project",
    "import_project_egg",
    "inspect_project",
    "load_chain",
    "mint_rappid",
    "open_project",
    "project_dir",
    "project_stream_id",
    "projects_root",
    "refresh_views",
    "require_identity_owner",
    "require_slug",
    "safe_join",
    "slugify",
    "verify_frame",
    "verify_project",
    "verify_project_egg",
]


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv[1:]))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
