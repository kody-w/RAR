---
name: "rar-kody-w-rapp-projects"
description: "Coordinates local-first projects through strict RAPP/1 work chains, verified derived boards, artifact receipts, and deterministic eggs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_projects", "rar_sha256": "f4102700cea9eefca33d876a04ba7b077e4111bf045492af678d2854058d97f1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.3", "author": "kody-w", "tags": ["rapp-1", "project-management", "local-first", "rapplication", "productivity"]}
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
