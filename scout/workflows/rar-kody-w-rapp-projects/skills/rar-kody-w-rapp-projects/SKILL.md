---
name: "rar-kody-w-rapp-projects"
description: "Coordinates local-first projects through strict RAPP/1 work chains, verified derived boards, artifact receipts, and deterministic eggs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_projects", "rar_sha256": "e994af96f664097a291b4a1446ba8b8e36e911d7ccacd5aa58d984f64fb3afca", "source_kind": "rar-agent", "source_commit": "a3391b199669c48572aabdab2087b8c6733f0964", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_projects_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/rapp-projects:901718bc9aaf54d5f849173968dde177d46dd088d22dee04b4ba716322332f9e", "kind": "skill"}, "version": "1.0.3", "author": "kody-w", "tags": ["rapp-1", "project-management", "local-first", "rapplication", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/rapp_projects`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_projects_agent.py` is
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
