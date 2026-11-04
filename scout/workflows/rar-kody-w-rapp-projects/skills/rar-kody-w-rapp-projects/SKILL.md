---
name: "rar-kody-w-rapp-projects"
description: "Coordinates local-first projects through strict RAPP/1 work chains, verified derived boards, artifact receipts, and deterministic eggs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_projects", "rar_sha256": "f4102700cea9eefca33d876a04ba7b077e4111bf045492af678d2854058d97f1", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.3", "author": "kody-w", "tags": ["rapp-1", "project-management", "local-first", "rapplication", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_projects_agent.py` and embedded as the fenced Python below (sha256 f4102700cea9eefc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_projects_agent.py` first:

```bash
python3 rapp_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_projects_agent.py   # or on stdin
python3 rapp_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/rapp_projects_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rapp_projects_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/rapp_projects/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
