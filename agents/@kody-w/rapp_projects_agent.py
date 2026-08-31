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
    Verify the complete chain and receipts, then append ``project.verify``.
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
paths stay in private locator metadata under that root and never enter eggs.

Standalone use accepts one JSON object as a Python argv value or on stdin.
Run the file with ``--tool`` to print its callable operation schema. Supply
``operation``; ``action`` is a compatibility alias, and omission is refused.
"""

from __future__ import annotations

import hashlib
import io
import json
import math
import os
import re
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
    "version": "1.0.1",
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
HEAD_SCHEMA = "rapp-project-head/1"
RECEIPT_SCHEMA = "rapp-artifact-receipt/1"
RECEIPT_LOCATORS_SCHEMA = "rapp-receipt-locators/1"
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
        "summary": {"type": "string"},
        "egg": {"type": "string"},
        "output": {"type": "string"},
        "owner_approved": {"type": "boolean"},
    },
    "anyOf": [
        {"required": ["operation"]},
        {"required": ["action"]},
    ],
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
HEAD_KEYS = frozenset({"schema", "stream_id", "seq", "frame_hash"})
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

SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
KIND = re.compile(
    r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?"
    r"\.[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$"
)
HEX64 = re.compile(r"^[0-9a-f]{64}$")
LOCATOR_TOKEN = re.compile(r"^[0-9a-f]{32}$")
UTC = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$")
RAPPID = re.compile(
    r"^rappid:@"
    r"([a-z0-9](?:[a-z0-9-]{0,37}[a-z0-9])?)"
    r"/"
    r"([a-z0-9](?:[a-z0-9-]{0,98}[a-z0-9])?)"
    r":([0-9a-f]{64})$"
)
INSTANCE = re.compile(
    r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$"
)
WINDOWS_RESERVED = frozenset(
    {"con", "prn", "aux", "nul"}
    | {f"com{number}" for number in range(1, 10)}
    | {f"lpt{number}" for number in range(1, 10)}
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


def mint_rappid(slug: Any, owner: str = "local") -> str:
    """Mint a keyless UUIDv4 RAPPID; no name participates in its hash tail."""
    slug = require_slug(slug)
    if (
        not isinstance(owner, str)
        or len(owner) > 39
        or not SLUG.fullmatch(owner)
    ):
        raise RappProjectsError("RAPPID owner must be a lowercase label")
    tail = Hb("rapp/1:rappid", uuid.uuid4().bytes)
    return f"rappid:@{owner}/{slug}:{tail}"


def _valid_rappid(value: Any, *, slug: str | None = None) -> bool:
    if not isinstance(value, str):
        return False
    match = RAPPID.fullmatch(value)
    return bool(match and (slug is None or match.group(2) == slug))


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
    return bool(_valid_rappid(rappid) and INSTANCE.fullmatch(instance))


def _mkdir(path: Path) -> Path:
    if path.is_symlink():
        raise RappProjectsError("storage directories cannot be symbolic links")
    if path.exists() and not path.is_dir():
        raise RappProjectsError("storage path is not a directory")
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
    for project in directories:
        _validate_project_metadata(root / project, project)
    return {
        "identity": identity,
        "cell": manifest,
        "lineage": lineage,
        "projects": directories,
    }


def ensure_root(root: Any = None) -> Path:
    root_path = projects_root(root)
    _mkdir(root_path)
    with _PROCESS_LOCK:
        with file_lock(root_path / ".projects.lock"):
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
                other_files = [
                    entry.name
                    for entry in root_path.iterdir()
                    if entry.is_file()
                    and entry.name
                    not in {".projects.lock", ".views.lock"}
                ]
                if directories or other_files:
                    raise RappProjectsError(
                        "refusing to mint identity into non-empty unowned root"
                    )
                rappid = mint_rappid("projects-control")
                created: list[Path] = []
                try:
                    for path, value in (
                        (
                            root_path / "rappid.json",
                            _identity_record(
                                rappid, "projects-root", "projects-control"
                            ),
                        ),
                        (
                            root_path / "lineage.json",
                            {
                                "schema": ROOT_LINEAGE_SCHEMA,
                                "parent_rappid": None,
                            },
                        ),
                        (
                            root_path / "manifest.json",
                            _cell_manifest("leviathan", "projects", []),
                        ),
                    ):
                        _atomic_json(path, value)
                        created.append(path)
                except BaseException:
                    for path in created:
                        path.unlink(missing_ok=True)
                    raise
            _validate_root_locked(root_path)
    return root_path


def _validate_receipt(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != RECEIPT_KEYS:
        raise RappProjectsError("artifact receipt has an invalid key set")
    if value["schema"] != RECEIPT_SCHEMA:
        raise RappProjectsError("artifact receipt schema is invalid")
    if not isinstance(value["path"], str) or not value["path"]:
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
    path = project_dir(project, root) / ".receipt-locators.json"
    if not path.exists():
        return {"schema": RECEIPT_LOCATORS_SCHEMA, "paths": {}}
    return _validate_receipt_locators(_read_json(path))


def _register_receipt_locator(path: Path, project: str, root: Path) -> str:
    directory = project_dir(project, root)
    if not directory.is_dir() or directory.is_symlink():
        raise RappProjectsError("receipt project directory is unavailable")
    location = str(path.resolve())
    with _PROCESS_LOCK:
        with file_lock(directory / ".chain.lock"):
            locators = _load_receipt_locators(project, root)
            token = next(
                (
                    candidate
                    for candidate, existing in locators["paths"].items()
                    if existing == location
                ),
                None,
            )
            if token is None:
                token = uuid.uuid4().hex
                locators["paths"][token] = location
                _atomic_json(directory / ".receipt-locators.json", locators)
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
    raw = Path(value).expanduser()
    if raw.is_absolute():
        return raw.resolve()
    return safe_join(project_dir(project, root), raw)


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


def artifact_receipt(value: Any, project: Any, root: Any = None) -> dict[str, Any]:
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
            str(resolved), project=project, root=root_path
        )
        if existing["sha256"] != current["sha256"]:
            raise RappProjectsError("supplied artifact receipt no longer matches")
        return current
    raw = value.get("path") if isinstance(value, dict) else value
    if not isinstance(raw, (str, os.PathLike)) or not str(raw):
        raise RappProjectsError("artifact receipt requires a file path")
    text = str(raw)
    resolved = _resolve_receipt_path(text, project=project, root=root_path)
    if resolved is None:
        raise RappProjectsError(
            "local-private receipt URIs can only be reused as complete receipts"
        )
    if resolved.is_symlink():
        raise RappProjectsError("artifact receipts refuse symbolic links")
    logical = (
        _view_path(resolved, project, root_path)
        if _is_within(resolved, root_path)
        else _register_receipt_locator(resolved, project, root_path)
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


def _receipt_list(value: Any, project: str, root: Path) -> list[dict[str, Any]]:
    if value is None:
        values: list[Any] = []
    elif isinstance(value, list):
        values = value
    else:
        values = [value]
    if len(values) > MAX_LIST_ITEMS:
        raise RappProjectsError("artifact list has too many items")
    return [artifact_receipt(item, project, root) for item in values]


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
    if kind not in FRAME_KINDS or not KIND.fullmatch(kind):
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
    _validate_payload(kind, payload)
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
) -> None:
    # Step 1 — shape and types.
    if not isinstance(frame, dict) or set(frame) != FRAME_KEYS:
        raise FrameVerificationError("1", "frame must have exactly eleven keys")
    if frame.get("spec") != SPEC:
        raise FrameVerificationError("1", "spec must be rapp/1")
    if (
        not isinstance(frame.get("kind"), str)
        or not KIND.fullmatch(frame["kind"])
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
    if frame.get("sig") is not None and not isinstance(frame["sig"], str):
        raise FrameVerificationError("1", "sig must be null or a JWS string")
    try:
        canonical(frame)
    except RappProjectsError as exc:
        raise FrameVerificationError("1", str(exc)) from exc

    # Step 1a — stream binding.
    if stream_id is not None and frame["stream_id"] != stream_id:
        raise FrameVerificationError("1a", "frame belongs to another stream")

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
        if frame["seq"] != head["seq"] + 1:
            raise FrameVerificationError("4", "sequence is not contiguous")
        if frame["prev"] != head["payload_hash"]:
            raise FrameVerificationError("4", "previous particle does not match")
        if frame["utc"] < head["utc"]:
            raise FrameVerificationError("4", "utc moved backwards")

    # Step 5 — wire chain. Project streams are never swarm streams.
    if frame["prev_wave"] is not None:
        raise FrameVerificationError("5", "prev_wave must be null off swarm")

    # Step 6 — local project streams are intentionally unsigned.
    if frame["sig"] is not None:
        raise FrameVerificationError("6", "sig must be null on this local stream")


def verify_frame(
    frame: Any,
    head: dict[str, Any] | None = None,
    stream_id: str | None = None,
    project: str | None = None,
) -> tuple[bool, str | None]:
    """Return ``(ok, reason)`` after the ordered RAPP/1 checklist."""
    try:
        _verify_frame_or_raise(
            frame,
            head=head,
            stream_id=stream_id,
            project=project,
        )
        return True, None
    except FrameVerificationError as exc:
        return False, str(exc)


def _head_record(frame: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": HEAD_SCHEMA,
        "stream_id": frame["stream_id"],
        "seq": frame["seq"],
        "frame_hash": frame["frame_hash"],
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
    ):
        raise ChainVerificationError("trusted head metadata is invalid")
    return dict(value)


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
    trusted = _validate_head(_read_json(head_path), stream_id)
    actual = frames[-1]
    if trusted["seq"] > actual["seq"]:
        raise ChainVerificationError("presented chain rolls back the trusted head")
    if trusted["seq"] >= len(frames):
        raise ChainVerificationError("trusted head sequence is outside the chain")
    trusted_frame = frames[trusted["seq"]]
    if trusted_frame["frame_hash"] != trusted["frame_hash"]:
        raise ChainVerificationError("chain forks from the trusted head")
    if trusted["seq"] < actual["seq"]:
        _atomic_json(head_path, _head_record(actual))


def load_chain(project: Any, root: Any = None) -> list[dict[str, Any]]:
    """Load a complete verified chain and enforce its persisted monotonic head."""
    project = require_slug(project)
    root_path = projects_root(root)
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
    _check_trusted_head(directory, frames, stream_id)
    return frames


def _append_octets(path: Path, record: bytes) -> None:
    if len(record) > MAX_CANONICAL_BYTES + 1 or not record.endswith(b"\n"):
        raise RappProjectsError("append record exceeds the frame limit")
    flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT
    if hasattr(os, "O_BINARY"):
        flags |= os.O_BINARY
    descriptor = os.open(path, flags, 0o600)
    try:
        written = os.write(descriptor, record)
        if written != len(record):
            raise OSError("atomic append wrote a partial record")
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass
    _fsync_directory(path.parent)


def _append_locked(
    project: str,
    kind: str,
    payload: dict[str, Any],
    root: Path,
) -> dict[str, Any]:
    directory = project_dir(project, root)
    frames = load_chain(project, root)
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
    _append_octets(
        directory / "chain.jsonl",
        canonical(frame).encode("utf-8") + b"\n",
    )
    _atomic_json(directory / "head.json", _head_record(frame))
    return frame


def append_frame(
    project: Any,
    kind: str,
    payload: dict[str, Any],
    root: Any = None,
    *,
    refresh: bool = True,
) -> dict[str, Any]:
    """Append after locking, reloading, and verifying the authoritative chain."""
    project = require_slug(project)
    root_path = ensure_root(root)
    _validate_payload(kind, payload, project=project)
    directory = project_dir(project, root_path)
    with _PROCESS_LOCK:
        with file_lock(directory / ".chain.lock"):
            frame = _append_locked(project, kind, payload, root_path)
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
    refresh: bool = True,
) -> dict[str, Any] | None:
    project = require_slug(project)
    root_path = ensure_root(root)
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
                    load_chain(project, root_path)
                return None
            old_manifest = root_metadata["cell"]
            created = False
            try:
                _mkdir(directory)
                created = True
                project_rappid = mint_rappid(project)
                _atomic_json(
                    directory / "rappid.json",
                    _identity_record(project_rappid, "project", project),
                )
                _atomic_json(
                    directory / "lineage.json",
                    {
                        "schema": PROJECT_LINEAGE_SCHEMA,
                        "parent_rappid": root_metadata["identity"]["rappid"],
                        "origin": payload["origin"],
                    },
                )
                _atomic_json(
                    directory / "manifest.json",
                    _cell_manifest("factory", f"projects/{project}", []),
                )
                frame = build_frame(
                    "project.genesis",
                    project_stream_id(project_rappid),
                    0,
                    payload,
                    None,
                )
                with file_lock(directory / ".chain.lock"):
                    _append_octets(
                        directory / "chain.jsonl",
                        canonical(frame).encode("utf-8") + b"\n",
                    )
                    _atomic_json(directory / "head.json", _head_record(frame))
                updated = dict(old_manifest)
                updated["children"] = sorted(old_manifest["children"] + [project])
                _validate_cell(updated)
                _atomic_json(root_path / "manifest.json", updated)
                _validate_root_locked(root_path)
            except BaseException:
                if created and directory.exists():
                    import shutil

                    shutil.rmtree(directory)
                _atomic_json(root_path / "manifest.json", old_manifest)
                raise
    if refresh:
        refresh_views(root_path)
    return frame


def _verify_receipts(
    frames: list[dict[str, Any]],
    project: str,
    root: Path,
) -> list[dict[str, Any]]:
    broken: list[dict[str, Any]] = []
    for frame in frames:
        if frame["kind"] == "work.status":
            receipts = frame["payload"]["artifacts"]
        elif frame["kind"] == "work.handoff":
            receipts = [frame["payload"]["doc"]]
        elif frame["kind"] == "work.punchout":
            receipts = frame["payload"]["receipts"]
        else:
            receipts = []
        for value in receipts:
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
    root_path = projects_root(root)
    frames = load_chain(project, root_path) if frames is None else list(frames)
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
        "verified": True,
        "frame_count": len(frames),
    }
    for frame in frames:
        kind = frame["kind"]
        payload = frame["payload"]
        state["last_frame_utc"] = frame["utc"]
        state["last_frame_hash"] = frame["frame_hash"]
        if kind != "project.verify":
            state["last_work_utc"] = frame["utc"]
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
        return {
            key: _public_value(child, root, portable=portable)
            for key, child in value.items()
        }
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
                        frames = load_chain(project, root_path)
                        state = fold_project(project, frames, root_path)
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
    refresh: bool = True,
) -> dict[str, Any]:
    project = require_slug(project)
    root_path = ensure_root(root)
    directory = project_dir(project, root_path)
    with _PROCESS_LOCK:
        with file_lock(directory / ".chain.lock"):
            frames = load_chain(project, root_path)
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
            frames = load_chain(project, root_path)
            state = fold_project(project, frames, root_path)
            broken = _verify_receipts(frames, project, root_path)
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
            frames = load_chain(project, root_path)
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
            destination = (directory / "PROJECT.egg").resolve()
            if output not in (None, ""):
                requested = Path(str(output)).expanduser()
                requested = (
                    requested.resolve()
                    if requested.is_absolute()
                    else safe_join(directory, requested)
                )
                if requested != destination:
                    raise RappProjectsError(
                        "egg output must be the selected project's PROJECT.egg"
                    )
            if destination.exists() and destination.is_symlink():
                raise RappProjectsError("egg output cannot be a symbolic link")
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
    frames = _load_chain_bytes(
        files["chain.jsonl"],
        project=project,
        stream_id=payload["stream_id"],
    )
    if (
        len(frames) != payload["frame_count"]
        or frames[-1]["frame_hash"] != payload["head_frame_hash"]
        or frames[-1]["utc"] != manifest["created_utc"]
    ):
        raise EggVerificationError("egg chain head metadata does not match")
    state = fold_project(project, frames, root=Path.cwd())
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
    refresh: bool = True,
) -> dict[str, Any]:
    """Verify the full egg first, then create or fast-forward without reparenting."""
    verified = verify_project_egg(path)
    manifest = verified["manifest"]
    project = manifest["payload"]["project"]
    incoming_frames = verified["frames"]
    root_path = ensure_root(root)
    directory = project_dir(project, root_path)
    imported_frames = 0
    created = False
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
                    local_frames = load_chain(project, root_path)
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
                    for frame in incoming_frames[len(local_frames) :]:
                        _append_octets(
                            directory / "chain.jsonl",
                            canonical(frame).encode("utf-8") + b"\n",
                        )
                        _atomic_json(directory / "head.json", _head_record(frame))
                        imported_frames += 1
                    load_chain(project, root_path)
            else:
                old_manifest = root_metadata["cell"]
                try:
                    _mkdir(directory)
                    _atomic_json(directory / "rappid.json", verified["identity"])
                    _atomic_json(directory / "manifest.json", verified["cell"])
                    _atomic_json(directory / "lineage.json", verified["lineage"])
                    _atomic_bytes(
                        directory / "chain.jsonl", verified["files"]["chain.jsonl"]
                    )
                    _atomic_json(
                        directory / "head.json",
                        _head_record(incoming_frames[-1]),
                    )
                    _atomic_bytes(
                        directory / "STATUS.md", verified["files"]["STATUS.md"]
                    )
                    updated = dict(old_manifest)
                    updated["children"] = sorted(
                        old_manifest["children"] + [project]
                    )
                    _validate_cell(updated)
                    _atomic_json(root_path / "manifest.json", updated)
                    _validate_root_locked(root_path)
                    load_chain(project, root_path)
                    imported_frames = len(incoming_frames)
                    created = True
                except BaseException:
                    if directory.exists():
                        import shutil

                        shutil.rmtree(directory)
                    _atomic_json(root_path / "manifest.json", old_manifest)
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
    }


PROTOCOL = {
    "schema": "rapp-projects-protocol/1",
    "agent": __manifest__["name"],
    "version": "1.0.1",
    "operations": list(OPERATIONS),
    "root_precedence": [
        "explicit root",
        "RAPP_PROJECTS_ROOT",
        "~/.rapp/projects-control",
    ],
    "identity": {
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
        "sig": None,
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
            "private locators excluded from eggs; unresolved locators fail"
        ),
        "egg_output": "<root>/<project>/PROJECT.egg only",
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
            if operation_value is None:
                raise RappProjectsError(
                    "operation is required; action is a compatibility alias"
                )
            if operation not in OPERATIONS:
                raise RappProjectsError("unknown operation")
            if operation == "protocol":
                return self._result(operation, protocol=PROTOCOL)

            root_path = projects_root(kwargs.get("root"))
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
                            "agents": sorted(state["agents"]),
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

            if operation == "import":
                egg = kwargs.get("egg", kwargs.get("path"))
                if not isinstance(egg, (str, os.PathLike)) or not str(egg):
                    raise RappProjectsError("import requires egg")
                result = import_project_egg(egg, root_path, refresh=False)
                return self._result_after_refresh(
                    operation,
                    root_path,
                    **result,
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
                )

            if operation == "status":
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
                        kwargs.get("artifacts"), project, root_path
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
                )
                return self._result_after_refresh(
                    operation,
                    root_path,
                    project=project,
                    seq=frame["seq"],
                    frame_hash=frame["frame_hash"],
                )

            if operation == "handoff":
                document = artifact_receipt(
                    kwargs.get("doc"), project, root_path
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
                )
                return self._result_after_refresh(
                    operation,
                    root_path,
                    project=project,
                    seq=frame["seq"],
                    frame_hash=frame["frame_hash"],
                    doc=document,
                )

            if operation == "punchout":
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
                            kwargs.get("receipts"), project, root_path
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
                )
                return self._result_after_refresh(
                    operation,
                    root_path,
                    project=project,
                    seq=frame["seq"],
                    frame_hash=frame["frame_hash"],
                )

            if operation == "verify":
                result = verify_project(
                    project,
                    root_path,
                    append_verdict=True,
                    refresh=False,
                )
                frame = result.pop("frame")
                return self._result_after_refresh(
                    operation,
                    root_path,
                    **result,
                    seq=frame["seq"],
                    verification_frame_hash=frame["frame_hash"],
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
    "require_slug",
    "safe_join",
    "slugify",
    "verify_frame",
    "verify_project",
    "verify_project_egg",
]


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv[1:]))
