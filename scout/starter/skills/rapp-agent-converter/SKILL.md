---
name: "rapp-agent-converter"
description: "Makes a RAPP/1 Toasted SKILL.md the persistent Grail record for raw skills and RAR agents, deterministically materializes agent.py on demand, and hotloads any supported form into a Brainstem."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp_agent_converter", "rar_sha256": "81bae056a1736e2499333d7aae869d29a19245d1488e13b9f28dbb2038ad2c4a", "source_kind": "foundation", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_agent_converter_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/rapp-agent-converter:11ce7bf2e7b301b3a35c919f34a60f9a25742552c9871ee33421d2de313e65fa", "kind": "skill"}, "default_format": "skill", "toasted": true, "canonical_agent": "rapp_agent_converter_agent.py", "normalization_path": "raw-skill->rar-agent->toasted-skill", "reader_versions": ["raw-skill", "rci/1", "rapp/1"], "writer_version": "rapp/1", "version": "1.1.0", "author": "RAPP Agent Registry", "tags": ["rapp", "rapp-1", "rar", "skills", "toasted", "conversion", "fidelity", "local-first", "grail", "hotload"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/rapp_agent_converter`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_agent_converter_agent.py` is
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

RAPP Agent Converter - make agent.py and SKILL.md interchangeable.

The default artifact is a RAPP/1 Toasted SKILL.md. RAR agents project to that
format without changing their source bytes. Raw or legacy skills first cross
the RAR agent membrane:

    raw SKILL.md -> valid RAR single-file agent -> RAPP/1 Toasted SKILL.md

That intermediate agent is not an implementation guess. It carries the exact
authored Markdown in its RCI ledger and exposes the skill's typed contract when
one exists. The final Toasted skill vaults the normalized agent and byte-exact
source Markdown as the persistent Grail record. Agent files are materialized
from that record only when selected or hotloaded, so the default path stores no
adjacent duplicate.

The converter is local-only, stdlib-only, and delegates the low-level RCI
codec to a checksum-pinned RAPP Toaster embedded in the generated single-file
converter agent.

Drop `rapp_agent_converter_agent.py` by itself into a Brainstem `agents/`
directory to make raw SKILL.md, Toasted SKILL.md, and agent.py inputs share one
restart-free `hotload` path.

Usage:
    python3 scripts/toast.py path/to/example_agent.py
    python3 scripts/toast.py path/to/SKILL.md
    python3 scripts/toast.py materialize path/to/SKILL.md
    python3 scripts/toast.py hotload path/to/SKILL.md --brainstem-dir ./brainstem
    python3 scripts/toast.py config --default-format agent
    python3 scripts/toast.py verify path/to/SKILL.md
    python3 scripts/toast.py restore-raw path/to/SKILL.md

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "additionalProperties": false,
  "properties": {
    "agents_dir": {
      "description": "Exact Brainstem agents directory.",
      "type": "string"
    },
    "brainstem_dir": {
      "description": "Brainstem root for operation=hotload.",
      "type": "string"
    },
    "default_format": {
      "description": "Global selected output for config.",
      "enum": [
        "skill",
        "agent"
      ],
      "type": "string"
    },
    "force": {
      "description": "Replace a conflicting output file.",
      "type": "boolean"
    },
    "in_place": {
      "description": "Explicitly replace a raw/legacy source SKILL.md after preserving an exact backup.",
      "type": "boolean"
    },
    "mode": {
      "description": "rapp1 writes a Grail record without duplicates; legacy preserves adjacent pair behavior.",
      "enum": [
        "rapp1",
        "legacy"
      ],
      "type": "string"
    },
    "operation": {
      "description": "Convert, materialize, hotload, verify, or configure the agent/skill compatibility membrane.",
      "enum": [
        "auto",
        "convert",
        "toast",
        "materialize",
        "hotload",
        "inspect",
        "verify",
        "roundtrip",
        "soak",
        "restore_raw",
        "config"
      ],
      "type": "string"
    },
    "out": {
      "description": "Optional output path.",
      "type": "string"
    },
    "path": {
      "description": "RAR *_agent.py or SKILL.md input.",
      "type": "string"
    },
    "publisher": {
      "description": "Publisher for agents synthesized from raw skills. Defaults to RAPP_PUBLISHER or @local.",
      "type": "string"
    },
    "rappid": {
      "description": "Optional existing mint-once RAPP/1 identity.",
      "type": "string"
    },
    "to": {
      "description": "Selected materialization. Defaults to the global converter setting; the Grail remains SKILL.md.",
      "enum": [
        "skill",
        "agent"
      ],
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_agent_converter_agent.py` and embedded as the fenced Python below (sha256 81bae056a1736e24…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_agent_converter_agent.py` first:

```bash
python3 rapp_agent_converter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_agent_converter_agent.py   # or on stdin
python3 rapp_agent_converter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
#!/usr/bin/env python3
"""RAPP Agent Converter - make agent.py and SKILL.md interchangeable.

The default artifact is a RAPP/1 Toasted SKILL.md. RAR agents project to that
format without changing their source bytes. Raw or legacy skills first cross
the RAR agent membrane:

    raw SKILL.md -> valid RAR single-file agent -> RAPP/1 Toasted SKILL.md

That intermediate agent is not an implementation guess. It carries the exact
authored Markdown in its RCI ledger and exposes the skill's typed contract when
one exists. The final Toasted skill vaults the normalized agent and byte-exact
source Markdown as the persistent Grail record. Agent files are materialized
from that record only when selected or hotloaded, so the default path stores no
adjacent duplicate.

The converter is local-only, stdlib-only, and delegates the low-level RCI
codec to a checksum-pinned RAPP Toaster embedded in the generated single-file
converter agent.

Drop `rapp_agent_converter_agent.py` by itself into a Brainstem `agents/`
directory to make raw SKILL.md, Toasted SKILL.md, and agent.py inputs share one
restart-free `hotload` path.

Usage:
    python3 scripts/toast.py path/to/example_agent.py
    python3 scripts/toast.py path/to/SKILL.md
    python3 scripts/toast.py materialize path/to/SKILL.md
    python3 scripts/toast.py hotload path/to/SKILL.md --brainstem-dir ./brainstem
    python3 scripts/toast.py config --default-format agent
    python3 scripts/toast.py verify path/to/SKILL.md
    python3 scripts/toast.py restore-raw path/to/SKILL.md
"""

from __future__ import annotations

import argparse
import ast
import base64
import copy
from contextlib import ExitStack, contextmanager
from datetime import datetime, timezone
import gzip
import hashlib
import importlib.util
import json
import os
import pprint
import re
import stat
import sys
import tempfile
import types
import uuid
import zlib
from pathlib import Path

sys.dont_write_bytecode = True

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            if name is not None:
                self.name = name
            if metadata is not None:
                self.metadata = metadata

        def perform(self, **kwargs):
            return "Not implemented."

        def system_context(self):
            return None

        def to_tool(self):
            return {
                "type": "function",
                "function": {
                    "name": self.name,
                    "description": self.metadata.get("description", ""),
                    "parameters": self.metadata.get("parameters", {}),
                },
            }


CONVERTER_RAPPID = (
    "rappid:@rapp/rapp-agent-converter:"
    "11ce7bf2e7b301b3a35c919f34a60f9a25742552c9871ee33421d2de313e65fa"
)
PINNED_TOASTER_SHA256 = (
    "d340043178aa4160f76a179b8b1086971e09207b212aff2ab2c0752b69173e17"
)
EMBEDDED_TOASTER_GZIP_BASE64 = "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"
RAPPID_RE = re.compile(
    r"^rappid:@[a-z0-9]+(?:-[a-z0-9]+)*/"
    r"[a-z0-9]+(?:-[a-z0-9]+)*:[0-9a-f]{64}$"
)
OWNER_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
REQUIRED_MANIFEST_FIELDS = (
    "schema",
    "name",
    "version",
    "display_name",
    "description",
    "author",
    "tags",
    "category",
)
CONFIG_SCHEMA = "rapp-agent-converter-config/1.0"
IDENTITY_SCHEMA = "rapp-identity-ledger/1.0"
FORMATS = {"skill", "agent"}
MODES = {"rapp1", "legacy"}
SKILL_CAPSULE_RE = re.compile(
    r"<!--\s*rci-capsule:v1:([A-Za-z0-9+/=]+)\s*-->"
)
MAX_SKILL_BYTES = 16 * 1024 * 1024
MAX_CAPSULE_B64 = 16 * 1024 * 1024
MAX_CAPSULE_JSON_BYTES = 64 * 1024 * 1024
MAX_AGENT_BYTES = 32 * 1024 * 1024
MAX_SOURCE_SKILL_BYTES = 16 * 1024 * 1024

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/rapp_agent_converter",
    "version": "1.1.0",
    "display_name": "RappAgentConverter",
    "description": (
        "Makes a RAPP/1 Toasted SKILL.md the persistent Grail record for raw "
        "skills and RAR agents, deterministically materializes agent.py on "
        "demand, and hotloads any supported form into a Brainstem."
    ),
    "author": "RAPP Agent Registry",
    "tags": [
        "rapp",
        "rapp-1",
        "rar",
        "skills",
        "toasted",
        "conversion",
        "fidelity",
        "local-first",
        "grail",
        "hotload",
    ],
    "category": "devtools",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "rapp": {
        "schema": "rapp/1",
        "rappid": (
            "rappid:@rapp/rapp-agent-converter:"
            "11ce7bf2e7b301b3a35c919f34a60f9a25742552c9871ee33421d2de313e65fa"
        ),
        "kind": "skill",
        "default_format": "skill",
        "canonical_format": "skill",
    },
}

BASE_DIR = Path(__file__).resolve().parent
_CORE = None


def _json(value) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _stable_gzip(data: bytes) -> bytes:
    compressed = bytearray(gzip.compress(data, 9, mtime=0))
    if len(compressed) >= 10:
        compressed[9] = 255
    return bytes(compressed)


def _bounded_gzip(data: bytes, limit: int, label: str) -> bytes:
    decompressor = zlib.decompressobj(16 + zlib.MAX_WBITS)
    output = decompressor.decompress(data, limit + 1)
    if len(output) > limit or decompressor.unconsumed_tail:
        raise ValueError(f"{label} exceeds {limit} bytes")
    output += decompressor.flush()
    if len(output) > limit:
        raise ValueError(f"{label} exceeds {limit} bytes")
    if not decompressor.eof or decompressor.unused_data:
        raise ValueError(f"{label} is not one canonical gzip member")
    return output


def _active_skill_capsule(text: str) -> str | None:
    in_fence = None
    fence_length = 0
    matches = []
    offset = 0
    for line in text.splitlines(keepends=True):
        if in_fence:
            close = re.match(r"^ {0,3}([`~]{3,})[ \t]*(?:\r?\n)?$", line)
            if (
                close
                and close.group(1)[0] == in_fence
                and len(close.group(1)) >= fence_length
            ):
                in_fence = None
                fence_length = 0
            offset += len(line)
            continue
        fence = re.match(r"^ {0,3}([`~]{3,})", line)
        if fence:
            in_fence = fence.group(1)[0]
            fence_length = len(fence.group(1))
            offset += len(line)
            continue
        for match in SKILL_CAPSULE_RE.finditer(line):
            matches.append((match.group(1), offset + match.end()))
        offset += len(line)
    if not matches:
        return None
    if len(matches) != 1:
        raise ValueError("SKILL.md has multiple active RCI capsules")
    payload, end = matches[0]
    if text[end:].strip():
        raise ValueError("SKILL.md active RCI capsule must be terminal")
    return payload


def _absolute(path: str | Path) -> Path:
    return Path(path).expanduser().absolute()


def _data_home() -> Path:
    configured = os.environ.get("RAPP_DATA_HOME")
    if configured:
        return _absolute(configured)
    xdg = os.environ.get("XDG_DATA_HOME")
    return (
        _absolute(xdg) / "rapp"
        if xdg
        else Path.home() / ".local" / "share" / "rapp"
    )


def _cache_home() -> Path:
    configured = os.environ.get("RAPP_CACHE_HOME")
    if configured:
        return _absolute(configured)
    xdg = os.environ.get("XDG_CACHE_HOME")
    return (
        _absolute(xdg) / "rapp"
        if xdg
        else Path.home() / ".cache" / "rapp"
    )


def _config_home() -> Path:
    configured = os.environ.get("RAPP_CONFIG_HOME")
    if configured:
        return _absolute(configured)
    xdg = os.environ.get("XDG_CONFIG_HOME")
    return (
        _absolute(xdg) / "rapp"
        if xdg
        else Path.home() / ".config" / "rapp"
    )


def _config_path() -> Path:
    configured = os.environ.get("RAPP_CONVERTER_CONFIG")
    return (
        _absolute(configured)
        if configured
        else _config_home() / "converter.json"
    )


def _identity_path() -> Path:
    configured = os.environ.get("RAPP_IDENTITY_STORE")
    return (
        _absolute(configured)
        if configured
        else _data_home() / "identities.json"
    )


def _lock_root() -> Path:
    configured = os.environ.get("RAPP_LOCK_HOME")
    return (
        _absolute(configured)
        if configured
        else _cache_home() / "locks"
    )


@contextmanager
def _exclusive_lock(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = open(path, "a+b")
    try:
        if os.name == "nt":
            import msvcrt

            handle.seek(0, os.SEEK_END)
            if handle.tell() == 0:
                handle.write(b"\0")
                handle.flush()
            handle.seek(0)
            msvcrt.locking(handle.fileno(), msvcrt.LK_LOCK, 1)
        else:
            import fcntl

            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        yield
    finally:
        if os.name == "nt":
            import msvcrt

            handle.seek(0)
            try:
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            except OSError:
                pass
        else:
            import fcntl

            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()


def _load_core():
    global _CORE
    if _CORE is not None:
        return _CORE

    configured = os.environ.get("RAPP_TOASTER_CORE")
    candidates = []
    if configured:
        candidates.append(Path(configured).expanduser())
    candidates.extend([
        BASE_DIR / "_toaster.py",
        BASE_DIR / "scripts" / "_toaster.py",
    ])
    core_path = next((path.resolve() for path in candidates if path.is_file()), None)
    if core_path is not None:
        data = core_path.read_bytes()
    elif not EMBEDDED_TOASTER_GZIP_BASE64.startswith("__RAPP_TOASTER_"):
        try:
            data = gzip.decompress(
                base64.b64decode(EMBEDDED_TOASTER_GZIP_BASE64)
            )
        except (KeyError, TypeError, ValueError, OSError) as error:
            raise RuntimeError("embedded RAPP Toaster is unreadable") from error
    else:
        raise RuntimeError(
            "pinned RAPP Toaster is missing; use the generated self-contained "
            "converter agent or keep its compatibility runtime intact"
        )

    actual = _sha256(data)
    if actual != PINNED_TOASTER_SHA256:
        raise RuntimeError(
            "pinned RAPP Toaster failed SHA-256 verification "
            f"(expected {PINNED_TOASTER_SHA256}, got {actual})"
        )
    if core_path is not None:
        spec = importlib.util.spec_from_file_location(
            "_rapp_agent_converter_toaster",
            core_path,
        )
        if spec is None or spec.loader is None:
            raise RuntimeError(
                f"could not load pinned RAPP Toaster from {core_path}"
            )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    else:
        module = types.ModuleType("_rapp_agent_converter_toaster")
        module.__file__ = "<embedded-rapp-toaster>"
        exec(
            compile(data, module.__file__, "exec"),
            module.__dict__,
        )

    def bounded_unpack_capsule(text):
        matches = module.CAPSULE_COMMENT_RE.findall(text)
        if not matches:
            return None
        payload = next(
            part for part in matches[-1] if part
        ).strip()
        if len(payload) > MAX_CAPSULE_B64:
            raise ValueError("RCI capsule exceeds encoded size limit")
        try:
            packed = base64.b64decode(payload, validate=True)
            decoded = json.loads(
                _bounded_gzip(
                    packed,
                    MAX_CAPSULE_JSON_BYTES,
                    "RCI capsule",
                )
            )
        except (TypeError, ValueError, OSError) as error:
            raise ValueError("malformed rci-capsule:v1 payload") from error
        return module._validate_capsule(decoded)

    def bounded_restore(rci, fmt):
        entry = (rci.get("preserved") or {}).get(fmt)
        if not entry:
            return None
        encoded = entry.get("b64")
        if not isinstance(encoded, str) or len(encoded) > MAX_CAPSULE_B64:
            raise ValueError(f"preserved {fmt} payload exceeds size limit")
        limit = (
            MAX_AGENT_BYTES
            if fmt == "agent"
            else MAX_SOURCE_SKILL_BYTES
        )
        try:
            raw = _bounded_gzip(
                base64.b64decode(encoded, validate=True),
                limit,
                f"preserved {fmt}",
            )
        except (TypeError, ValueError, OSError) as error:
            raise ValueError(f"preserved {fmt} payload is invalid") from error
        if _sha256(raw) != entry.get("sha256"):
            raise ValueError(f"preserved {fmt} payload failed its checksum")
        return raw

    module.unpack_capsule = bounded_unpack_capsule
    module.restore = bounded_restore
    _CORE = module
    return module


def _kebab(value: str) -> str:
    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", str(value or ""))
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "capability"


def _snake(value: str) -> str:
    return _kebab(value).replace("-", "_")


def _publisher(value: str | None) -> str:
    owner = str(value or os.environ.get("RAPP_PUBLISHER") or "@local").strip()
    owner = owner[1:] if owner.startswith("@") else owner
    owner = owner.lower()
    if not OWNER_RE.fullmatch(owner):
        raise ValueError(
            "publisher must be a GitHub-style owner such as @octocat"
        )
    return "@" + owner


def _mint_rappid(publisher: str, slug: str) -> str:
    owner = _publisher(publisher)[1:]
    kind = _kebab(slug)
    tail = hashlib.sha256(
        b"rapp/1:rappid\n" + uuid.uuid4().bytes
    ).hexdigest()
    return f"rappid:@{owner}/{kind}:{tail}"


def _valid_rappid(value) -> bool:
    return isinstance(value, str) and RAPPID_RE.fullmatch(value) is not None


def _manifest_from_bytes(data: bytes) -> dict:
    try:
        tree = ast.parse(data.decode("utf-8"))
    except (UnicodeDecodeError, SyntaxError):
        return {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == "__manifest__"
            for target in node.targets
        ):
            continue
        try:
            value = ast.literal_eval(node.value)
        except (ValueError, TypeError):
            return {}
        return value if isinstance(value, dict) else {}
    return {}


def _manifest_is_valid(manifest: dict) -> bool:
    return (
        isinstance(manifest, dict)
        and all(field in manifest for field in REQUIRED_MANIFEST_FIELDS)
        and manifest.get("schema") == "rapp-agent/1.0"
        and isinstance(manifest.get("name"), str)
        and re.fullmatch(
            r"@[A-Za-z0-9][A-Za-z0-9_-]*/[A-Za-z0-9][A-Za-z0-9_]*",
            manifest["name"],
        ) is not None
        and isinstance(manifest.get("version"), str)
        and SEMVER_RE.fullmatch(manifest["version"]) is not None
        and isinstance(manifest.get("display_name"), str)
        and bool(manifest["display_name"])
        and isinstance(manifest.get("description"), str)
        and bool(manifest["description"])
        and isinstance(manifest.get("author"), str)
        and bool(manifest["author"])
        and isinstance(manifest.get("tags"), list)
        and all(isinstance(tag, str) for tag in manifest["tags"])
        and isinstance(manifest.get("category"), str)
        and bool(manifest["category"])
    )


def _valid_agent_filename(filename: str) -> bool:
    return re.fullmatch(r"[a-z0-9_]+_agent\.py", filename) is not None


def _canonical_agent_filename(manifest: dict, filename: str) -> str:
    basename = Path(filename).name
    if _valid_agent_filename(basename):
        return basename
    package = str(manifest.get("name") or "").split("/", 1)
    slug = _snake(package[1] if len(package) == 2 else Path(basename).stem)
    if not slug.endswith("_agent"):
        slug += "_agent"
    return slug + ".py"


def _metadata_for(rci: dict) -> dict:
    platform = rci.get("platform") or {}
    metadata = platform.get("metadata") or {}
    return metadata if isinstance(metadata, dict) else {}


def _validate_rapp_envelope(value, label: str) -> dict | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError(f"{label} RAPP envelope must be an object")
    schema = value.get("schema")
    if schema is not None and schema != "rapp/1":
        raise ValueError(
            f"unsupported {label} RAPP schema {schema!r}; "
            "install a reader for that major version"
        )
    return value


def _rappid_from_metadata(rci: dict) -> str | None:
    metadata = _metadata_for(rci)
    rapp_meta = _validate_rapp_envelope(
        metadata.get("rapp"),
        "skill metadata",
    )
    candidates = []
    if isinstance(rapp_meta, dict):
        candidates.append(rapp_meta.get("rappid"))
    candidates.append(metadata.get("rappid"))
    for candidate in candidates:
        if candidate is None:
            continue
        if not _valid_rappid(candidate):
            raise ValueError(f"invalid RAPP/1 identity: {candidate!r}")
        return candidate
    return None


def _rappid_from_manifest(manifest: dict) -> str | None:
    candidates = []
    manifest_rapp = _validate_rapp_envelope(
        manifest.get("rapp"),
        "agent manifest",
    )
    if isinstance(manifest_rapp, dict):
        candidates.append(manifest_rapp.get("rappid"))
    candidates.append(manifest.get("rappid"))
    for candidate in candidates:
        if candidate is None:
            continue
        if not _valid_rappid(candidate):
            raise ValueError(f"invalid RAPP/1 identity: {candidate!r}")
        return candidate
    return None


def _rappid_from(rci: dict, manifest: dict, explicit: str | None) -> str | None:
    if explicit is not None:
        if not _valid_rappid(explicit):
            raise ValueError(f"invalid RAPP/1 identity: {explicit!r}")
        return explicit
    return _rappid_from_metadata(rci) or _rappid_from_manifest(manifest)


def _set_rapp_skill_metadata(
    rci: dict,
    *,
    rappid: str,
    canonical_agent: str,
    source_format: str,
    source_sha256: str,
    normalization_path: str,
) -> None:
    platform = dict(rci.get("platform") or {})
    metadata = dict(platform.get("metadata") or {})
    metadata.update({
        "projection": "rapp-capability-interchange/1.0",
        "default_format": "skill",
        "canonical_format": "skill",
        "grail_record": True,
        "materializes": ["agent"],
        "toasted": True,
        "canonical_agent": canonical_agent,
        "source_format": source_format,
        "source_sha256": source_sha256,
        "normalization_path": normalization_path,
        "reader_versions": ["raw-skill", "rci/1", "rapp/1"],
        "writer_version": "rapp/1",
    })
    metadata["rapp"] = {
        "schema": "rapp/1",
        "rappid": rappid,
        "kind": "skill",
    }
    platform["metadata"] = metadata
    rci["platform"] = platform


def _vault_source_skill(rci: dict, raw: bytes, filename: str) -> None:
    platform = dict(rci.get("platform") or {})
    platform["source_skill"] = {
        "filename": Path(filename).name,
        "sha256": _sha256(raw),
        "gzip_base64": base64.b64encode(_stable_gzip(raw)).decode("ascii"),
    }
    rci["platform"] = platform


def _restore_source_skill(rci: dict) -> tuple[bytes, str]:
    entry = (rci.get("platform") or {}).get("source_skill")
    if not isinstance(entry, dict):
        raise ValueError("this Toasted skill does not vault an original SKILL.md")
    try:
        encoded = entry["gzip_base64"]
        if not isinstance(encoded, str) or len(encoded) > MAX_CAPSULE_B64:
            raise ValueError("vaulted source SKILL.md exceeds size limit")
        raw = _bounded_gzip(
            base64.b64decode(encoded, validate=True),
            MAX_SOURCE_SKILL_BYTES,
            "vaulted source SKILL.md",
        )
    except Exception as error:
        raise ValueError("vaulted source SKILL.md is unreadable") from error
    if _sha256(raw) != entry.get("sha256"):
        raise ValueError("vaulted source SKILL.md failed its checksum")
    return raw, str(entry.get("filename") or "SKILL.raw.md")


def _manifest_for(
    rci: dict,
    *,
    publisher: str,
    rappid: str,
    source_skill_sha256: str,
    existing: dict | None = None,
) -> dict:
    existing = dict(existing or {})
    slug = _snake(rci.get("slug") or rci.get("name") or "capability")
    runtime_name = str(rci.get("name") or "Capability")
    version = str(rci.get("version") or "1.0.0")
    if SEMVER_RE.fullmatch(version) is None:
        version = "1.0.0"
    tags = [
        str(tag)
        for tag in (rci.get("tags") or [])
        if isinstance(tag, str) and tag.strip()
    ]
    for tag in ("rapp-1", "toasted", "converted-skill"):
        if tag not in tags:
            tags.append(tag)
    metadata = _metadata_for(rci)
    category = metadata.get("category")
    if not isinstance(category, str) or not category:
        category = "productivity"
    author = rci.get("author") or metadata.get("author") or publisher
    existing_name = existing.get("name")
    package_name = (
        existing_name
        if (
            isinstance(existing_name, str)
            and re.fullmatch(
                r"@[A-Za-z0-9][A-Za-z0-9_-]*/[A-Za-z0-9][A-Za-z0-9_]*",
                existing_name,
            ) is not None
            and existing_name.split("/", 1)[0].lower() == publisher.lower()
        )
        else f"{publisher}/{slug}"
    )
    manifest = {
        **existing,
        "schema": "rapp-agent/1.0",
        "name": package_name,
        "version": version,
        "display_name": runtime_name,
        "description": (
            str(rci.get("description") or "").strip()
            or f"Normalized agent for the {runtime_name} skill."
        ),
        "author": str(author),
        "tags": tags,
        "category": category,
        "quality_tier": existing.get("quality_tier", "community"),
        "requires_env": (
            existing.get("requires_env")
            if isinstance(existing.get("requires_env"), list)
            else []
        ),
        "dependencies": ["@rapp/basic_agent"],
        "rapp": {
            "schema": "rapp/1",
            "rappid": rappid,
            "kind": "agent",
            "source_skill_sha256": source_skill_sha256,
            "default_projection": "SKILL.md",
        },
    }
    return manifest


def _manifest_assignment(manifest: dict) -> str:
    rendered = pprint.pformat(
        manifest,
        width=88,
        sort_dicts=False,
    )
    return f"__manifest__ = {rendered}\n"


def _upsert_manifest(data: bytes, manifest: dict) -> bytes:
    text = data.decode("utf-8")
    tree = ast.parse(text)
    lines = text.splitlines(keepends=True)
    manifest_node = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "__manifest__"
            for target in node.targets
        ):
            manifest_node = node
            break

    block = _manifest_assignment(manifest)
    if manifest_node is not None:
        lines[manifest_node.lineno - 1:manifest_node.end_lineno] = [block]
    else:
        body_index = 0
        if (
            tree.body
            and isinstance(tree.body[0], ast.Expr)
            and isinstance(tree.body[0].value, ast.Constant)
            and isinstance(tree.body[0].value.value, str)
        ):
            body_index = 1
        while (
            body_index < len(tree.body)
            and isinstance(tree.body[body_index], ast.ImportFrom)
            and tree.body[body_index].module == "__future__"
        ):
            body_index += 1
        insert_line = (
            tree.body[body_index - 1].end_lineno
            if body_index
            else 0
        )
        lines[insert_line:insert_line] = ["\n", block, "\n"]
    result = "".join(lines)
    compile(result, "<rapp-agent-converter>", "exec")
    return result.encode("utf-8")


def _append_current_capsule(core, data: bytes, rci: dict) -> bytes:
    clean = core.strip_capsules(data).rstrip()
    ledger = copy.deepcopy(rci)
    ledger.setdefault("preserved", {}).pop("agent", None)
    capsule = core.pack_capsule(ledger)
    return clean + b"\n\n# " + capsule.encode("ascii") + b"\n"


def _has_rar_agent_class(data: bytes) -> bool:
    try:
        tree = ast.parse(data.decode("utf-8"))
    except (UnicodeDecodeError, SyntaxError):
        return False
    class_defs = {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.ClassDef)
    }

    def base_name(node) -> str | None:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            return node.attr
        return None

    def inherits_rar_base(node, seen=None) -> bool:
        seen = set(seen or ())
        if node.name in seen:
            return False
        seen.add(node.name)
        for base in node.bases:
            name = base_name(base)
            if name in {"BasicAgent", "RappterEngine"}:
                return True
            if name in class_defs and inherits_rar_base(class_defs[name], seen):
                return True
        return False

    return any(
        node.name != "BasicAgent"
        and inherits_rar_base(node)
        and any(
            isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef))
            and member.name == "perform"
            for member in node.body
        )
        for node in class_defs.values()
    )


def _normalized_identifier(value) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value or "").lower())


def _public_agent_contract(core, data: bytes, manifest: dict) -> dict | None:
    text = data.decode("utf-8")
    tree = ast.parse(text, filename="<agent>")
    env = {}
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
        ):
            try:
                env[node.targets[0].id] = core._eval_node(node.value, env)
            except core._Unevaluable:
                pass

    class_defs = {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.ClassDef)
    }

    def base_name(node) -> str | None:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            return node.attr
        return None

    def inherits_rar_base(node, seen=None) -> bool:
        seen = set(seen or ())
        if node.name in seen:
            return False
        seen.add(node.name)
        for base in node.bases:
            name = base_name(base)
            if name in {"BasicAgent", "RappterEngine"}:
                return True
            if name in class_defs and inherits_rar_base(class_defs[name], seen):
                return True
        return False

    candidates = []
    for node in tree.body:
        if (
            not isinstance(node, ast.ClassDef)
            or node.name == "BasicAgent"
            or node.name.startswith("_")
            or not inherits_rar_base(node)
        ):
            continue
        perform = next(
            (
                member
                for member in node.body
                if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef))
                and member.name == "perform"
            ),
            None,
        )
        if perform is not None:
            candidates.append((node, perform))
    if not candidates:
        return None

    manifest_slug = str(manifest.get("name") or "").split("/", 1)[-1]
    manifest_slug = manifest_slug.removesuffix("_agent")
    display = str(manifest.get("display_name") or "").split("(", 1)[0]
    desired = {
        _normalized_identifier(manifest_slug),
        _normalized_identifier(display),
    }
    scored = []
    for index, (node, perform) in enumerate(candidates):
        self_env = dict(env)
        for member in node.body:
            if (
                isinstance(member, ast.Assign)
                and len(member.targets) == 1
                and isinstance(member.targets[0], ast.Name)
            ):
                try:
                    self_env[member.targets[0].id] = core._eval_node(
                        member.value,
                        self_env,
                    )
                except core._Unevaluable:
                    pass
            if isinstance(member, ast.FunctionDef) and member.name == "__init__":
                for statement in ast.walk(member):
                    if (
                        isinstance(statement, ast.Assign)
                        and len(statement.targets) == 1
                        and isinstance(statement.targets[0], ast.Attribute)
                        and isinstance(statement.targets[0].value, ast.Name)
                        and statement.targets[0].value.id == "self"
                    ):
                        try:
                            self_env[statement.targets[0].attr] = core._eval_node(
                                statement.value,
                                self_env,
                            )
                        except core._Unevaluable:
                            pass
        runtime_name = self_env.get("name")
        metadata = self_env.get("metadata")
        metadata = metadata if isinstance(metadata, dict) else {}
        names = {
            _normalized_identifier(node.name.removesuffix("Agent")),
            _normalized_identifier(runtime_name),
            _normalized_identifier(metadata.get("name")),
        }
        score = 100 if desired & names else 0
        score += index
        scored.append((score, node, perform, runtime_name, metadata))

    _, node, perform, runtime_name, metadata = max(
        scored,
        key=lambda item: item[0],
    )
    parameters = metadata.get("parameters")
    if not isinstance(parameters, dict):
        parameters = {"type": "object", "properties": {}, "required": []}
    return {
        "name": (
            runtime_name
            if isinstance(runtime_name, str) and runtime_name
            else node.name.removesuffix("Agent")
        ),
        "description": (
            metadata.get("description")
            or manifest.get("description")
            or ""
        ),
        "parameters": parameters,
        "class_name": node.name,
        "perform": ast.get_source_segment(text, perform),
    }


def _read_public_agent(core, data: bytes, filename: str) -> dict:
    manifest = _manifest_from_bytes(data)
    rci = core.read_agent(data, filename)
    public = _public_agent_contract(core, data, manifest)
    if public is None:
        raise ValueError(f"{filename}: no public RAR agent entrypoint")
    rci["name"] = public["name"]
    rci["description"] = public["description"]
    rci["parameters"] = public["parameters"]
    rci["impl"] = {
        **(rci.get("impl") or {}),
        "class": public["class_name"],
        "perform": public["perform"],
    }
    return rci


def _validate_rar_agent(data: bytes, filename: str) -> dict:
    if not _valid_agent_filename(Path(filename).name):
        raise ValueError("RAR agent filename must be snake_case and end _agent.py")
    text = data.decode("utf-8")
    compile(text, filename, "exec")
    manifest = _manifest_from_bytes(data)
    _validate_rapp_envelope(manifest.get("rapp"), "agent manifest")
    if not _manifest_is_valid(manifest):
        raise ValueError("generated agent does not satisfy the RAR manifest contract")
    if not _has_rar_agent_class(data):
        raise ValueError(
            "generated agent has no BasicAgent-derived class defining perform()"
        )
    return manifest


def _read_skill(core, raw: bytes, filename: str) -> dict:
    if len(raw) > MAX_SKILL_BYTES:
        raise ValueError(f"{filename}: SKILL.md exceeds size limit")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError(f"{filename}: SKILL.md must be UTF-8") from error
    active = _active_skill_capsule(text)
    if active is not None:
        if len(active) > MAX_CAPSULE_B64:
            raise ValueError(f"{filename}: active RCI capsule is too large")
        return core.read_skill(raw, filename)

    frontmatter, body = core.split_frontmatter(text)
    rci = core.blank_rci()
    rci["slug"] = frontmatter.get("name") or "imported-skill"
    rci["name"] = core._pascal(rci["slug"])
    rci["description"] = frontmatter.get("description", "")
    for key in ("version", "author", "license"):
        if frontmatter.get(key):
            rci[key] = frontmatter[key]
    if isinstance(frontmatter.get("tags"), list):
        rci["tags"] = frontmatter["tags"]
    platform = {}
    for key in ("compatibility", "disable-model-invocation"):
        if key in frontmatter:
            platform[key] = frontmatter[key]
    if "allowed-tools" in frontmatter:
        platform.setdefault("claude", {})["allowed-tools"] = frontmatter[
            "allowed-tools"
        ]
    if isinstance(frontmatter.get("metadata"), dict):
        metadata = dict(frontmatter["metadata"])
        for key in ("version", "author", "tags"):
            if key in metadata:
                rci[key] = metadata.pop(key)
        if metadata:
            platform["metadata"] = metadata
    rci["platform"] = platform
    rci["instructions"] = body.replace(
        "<!-- toaster:generated:begin -->",
        "<!-- nested-toaster-generated-begin -->",
    ).replace(
        "<!-- toaster:generated:end -->",
        "<!-- nested-toaster-generated-end -->",
    ).strip()
    rci["impl"] = None
    parameters = {
        "type": "object",
        "properties": {},
        "required": [],
    }
    parameter_match = core.PARAM_FENCE.search(body)
    if parameter_match:
        try:
            parameters = json.loads(parameter_match.group(1))
            core._validate_parameters(parameters)
        except (TypeError, ValueError) as error:
            raise ValueError("Parameters fence is not valid JSON Schema") from error
    rci["parameters"] = parameters
    rci.setdefault("preserved", {}).pop("skill", None)
    core.preserve(rci, "skill", raw, filename)
    rci.setdefault("provenance", []).append(
        f"read:raw-skill:{Path(filename).name}"
    )
    rci["_read_fmt"] = "skill"
    return rci


def _is_rapp1_toast(core, raw: bytes) -> tuple[bool, dict | None]:
    try:
        if _active_skill_capsule(raw.decode("utf-8")) is None:
            return False, None
        capsule = _read_skill(core, raw, "SKILL.md")
    except (UnicodeDecodeError, ValueError):
        return False, None
    if not capsule:
        return False, None
    metadata = _metadata_for(capsule)
    rapp = metadata.get("rapp")
    compliant = (
        isinstance(rapp, dict)
        and rapp.get("schema") == "rapp/1"
        and rapp.get("kind") == "skill"
        and _valid_rappid(rapp.get("rappid"))
        and metadata.get("default_format") == "skill"
        and metadata.get("toasted") is True
    )
    if not compliant:
        return False, capsule
    try:
        agent = core.restore(capsule, "agent")
        canonical_agent = metadata.get("canonical_agent")
        if agent is None or not isinstance(canonical_agent, str):
            return False, capsule
        manifest = _validate_rar_agent(agent, canonical_agent)
        agent_rappid = _rappid_from_manifest(manifest)
        if agent_rappid is not None and agent_rappid != rapp["rappid"]:
            return False, capsule
        if metadata.get("source_format") == "skill":
            _restore_source_skill(capsule)
    except (OSError, RuntimeError, ValueError):
        return False, capsule
    return compliant, capsule


def _normalize_skill(
    core,
    source_path: Path,
    raw: bytes,
    *,
    publisher: str | None,
    explicit_rappid: str | None,
    agent_filename: str | None = None,
) -> tuple[dict, bytes, bytes]:
    rci = _read_skill(core, raw, str(source_path))
    frontmatter, _ = core.split_frontmatter(raw.decode("utf-8"))
    if (
        not frontmatter.get("name")
        and _active_skill_capsule(raw.decode("utf-8")) is None
    ):
        rci["slug"] = "imported-skill"
        rci["name"] = "ImportedSkill"
    existing_agent = core.restore(rci, "agent")
    existing_manifest = (
        _manifest_from_bytes(existing_agent)
        if existing_agent is not None
        else {}
    )
    filename = agent_filename or (
        core.linked_agent_name(rci)
        if existing_agent is not None
        else core.agent_filename(rci)
    )
    if not _valid_agent_filename(filename):
        raise ValueError("normalized agent filename must end in _agent.py")
    existing_has_rar_class = (
        existing_agent is not None
        and _has_rar_agent_class(existing_agent)
    )
    owner = _publisher(
        publisher
        or _metadata_for(rci).get("publisher")
    )
    skill_rappid = _rappid_from_metadata(rci)
    agent_rappid = (
        _rappid_from_manifest(existing_manifest)
        if existing_has_rar_class
        else None
    )
    rappid = _persisted_rappid(
        source_format="skill",
        source_path=source_path,
        raw=raw,
        publisher=owner,
        slug=rci.get("slug") or rci.get("name") or "skill",
        manifest_name=(
            existing_manifest.get("name")
            if existing_has_rar_class
            else None
        ),
        explicit=explicit_rappid,
        authoritative=agent_rappid,
        carried=skill_rappid,
    )

    _vault_source_skill(rci, raw, source_path.name)
    _set_rapp_skill_metadata(
        rci,
        rappid=rappid,
        canonical_agent=filename,
        source_format="skill",
        source_sha256=_sha256(raw),
        normalization_path="skill->rar-agent->toasted-skill",
    )

    if existing_agent is None or not existing_has_rar_class:
        synthesis_rci = copy.deepcopy(rci)
        synthesis_rci.setdefault("preserved", {}).pop("agent", None)
        generated = core.write_agent(synthesis_rci)
        generated = core.strip_capsules(generated)
        manifest = _manifest_for(
            synthesis_rci,
            publisher=owner,
            rappid=rappid,
            source_skill_sha256=_sha256(raw),
            existing=existing_manifest,
        )
        generated = _upsert_manifest(generated, manifest)
        agent_bytes = _append_current_capsule(core, generated, synthesis_rci)
    elif _manifest_is_valid(existing_manifest):
        agent_bytes = existing_agent
    else:
        manifest = _manifest_for(
            rci,
            publisher=owner,
            rappid=rappid,
            source_skill_sha256=_sha256(raw),
            existing=existing_manifest,
        )
        repaired = _upsert_manifest(core.strip_capsules(existing_agent), manifest)
        agent_bytes = _append_current_capsule(core, repaired, rci)

    _validate_rar_agent(agent_bytes, filename)
    agent_rci = _read_public_agent(core, agent_bytes, filename)
    _vault_source_skill(agent_rci, raw, source_path.name)
    _set_rapp_skill_metadata(
        agent_rci,
        rappid=rappid,
        canonical_agent=filename,
        source_format="skill",
        source_sha256=_sha256(raw),
        normalization_path="skill->rar-agent->toasted-skill",
    )
    skill_bytes = core.write_skill(agent_rci)
    projected = _read_skill(core, skill_bytes, "SKILL.md")
    if core.restore(projected, "agent") != agent_bytes:
        raise RuntimeError("Toasted skill did not restore its normalized agent exactly")
    return agent_rci, agent_bytes, skill_bytes


def _project_agent(
    core,
    source_path: Path,
    raw: bytes,
    *,
    explicit_rappid: str | None,
    persist_identity: bool = True,
) -> tuple[dict, bytes]:
    manifest = _manifest_from_bytes(raw)
    canonical_agent = _canonical_agent_filename(manifest, source_path.name)
    try:
        _validate_rar_agent(raw, canonical_agent)
    except ValueError as error:
        raise ValueError(f"{source_path}: {error}") from error
    rci = _read_public_agent(core, raw, str(source_path))
    rci["preserved"]["agent"]["filename"] = canonical_agent
    publisher = manifest["name"].split("/", 1)[0]
    manifest_rappid = _rappid_from_manifest(manifest)
    ledger_rappid = _rappid_from_metadata(rci)
    if persist_identity:
        rappid = _persisted_rappid(
            source_format="agent",
            source_path=source_path,
            raw=raw,
            publisher=publisher,
            slug=rci.get("slug") or source_path.stem,
            manifest_name=manifest["name"],
            explicit=explicit_rappid,
            authoritative=manifest_rappid,
            carried=ledger_rappid,
        )
    else:
        rappid = (
            explicit_rappid
            or manifest_rappid
            or ledger_rappid
            or _mint_rappid(publisher, rci.get("slug") or source_path.stem)
        )
    _set_rapp_skill_metadata(
        rci,
        rappid=rappid,
        canonical_agent=canonical_agent,
        source_format="agent",
        source_sha256=_sha256(raw),
        normalization_path="rar-agent->toasted-skill",
    )
    skill_bytes = core.write_skill(rci)
    projected = _read_skill(core, skill_bytes, "SKILL.md")
    if core.restore(projected, "agent") != raw:
        raise RuntimeError("Toasted skill did not restore the RAR agent byte-exact")
    return rci, skill_bytes


def _atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = (
        stat.S_IMODE(path.stat().st_mode)
        if path.exists()
        else 0o644
    )
    fd, temporary = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=path.parent,
    )
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, mode)
        os.replace(temporary, path)
        if os.name != "nt":
            directory_fd = os.open(path.parent, os.O_RDONLY)
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
    except Exception:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def _write_artifacts(
    artifacts: list[tuple[Path, bytes]],
    *,
    force: bool,
    replace_source: Path | None = None,
    replace_paths: set[Path] | None = None,
) -> list[dict]:
    allowed_replacements = {
        path.resolve()
        for path in (replace_paths or set())
    }
    if replace_source is not None:
        allowed_replacements.add(replace_source.resolve())
    targets = sorted({
        str(path.resolve())
        for path, _ in artifacts
    })
    with ExitStack() as locks:
        for target in targets:
            lock_name = hashlib.sha256(
                b"rapp-agent-converter/path-lock/1\n"
                + target.encode("utf-8")
            ).hexdigest()
            locks.enter_context(
                _exclusive_lock(_lock_root() / f"{lock_name}.lock")
            )

        expanded = []
        core = None
        for path, data in artifacts:
            if (
                path.name.lower() == "skill.md"
                and path.is_file()
                and path.read_bytes() != data
            ):
                core = core or _load_core()
                new_state, new_rci = _skill_state(core, data)
                if new_state == "rapp1" and new_rci:
                    new_rapp = _metadata_for(new_rci).get("rapp")
                    if isinstance(new_rapp, dict):
                        history, replacements = _grail_history(
                            core,
                            path,
                            data,
                            new_rapp["rappid"],
                        )
                        expanded.extend(history)
                        allowed_replacements.update(
                            item.resolve() for item in replacements
                        )
            expanded.append((path, data))

        for path, data in expanded:
            if not path.exists() or path.read_bytes() == data:
                continue
            if path.resolve() in allowed_replacements:
                continue
            if not force:
                raise FileExistsError(
                    f"{path} exists with different content; "
                    "pass force=true or --force"
                )

        written = []
        seen = set()
        for path, data in expanded:
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            status = (
                "unchanged"
                if path.exists() and path.read_bytes() == data
                else "written"
            )
            if status == "written":
                _atomic_write(path, data)
            written.append({
                "path": str(path),
                "sha256": _sha256(data),
                "status": status,
            })
        return written


def _read_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return copy.deepcopy(default)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ValueError(f"{path}: invalid JSON ({error})") from error
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def _stored_config() -> dict:
    value = _read_json(
        _config_path(),
        {
            "schema": CONFIG_SCHEMA,
            "default_format": "skill",
            "mode": "rapp1",
        },
    )
    if value.get("schema") != CONFIG_SCHEMA:
        raise ValueError(
            f"{_config_path()}: unsupported config schema "
            f"{value.get('schema')!r}"
        )
    if value.get("default_format") not in FORMATS:
        raise ValueError("converter default_format must be skill or agent")
    if value.get("mode") not in MODES:
        raise ValueError("converter mode must be rapp1 or legacy")
    return value


def _effective_settings(
    target_format: str | None,
    mode: str | None,
) -> tuple[str, str]:
    config = _stored_config()
    selected_format = (
        target_format
        or os.environ.get("RAPP_DEFAULT_FORMAT")
        or config["default_format"]
    )
    selected_mode = (
        mode
        or os.environ.get("RAPP_TOAST_MODE")
        or config["mode"]
    )
    if selected_format not in FORMATS:
        raise ValueError("default format must be skill or agent")
    if selected_mode not in MODES:
        raise ValueError("toast mode must be rapp1 or legacy")
    return selected_format, selected_mode


def configure_converter(
    *,
    default_format: str | None = None,
    mode: str | None = None,
) -> dict:
    path = _config_path()
    lock = path.with_suffix(path.suffix + ".lock")
    with _exclusive_lock(lock):
        config = _stored_config()
        if default_format is not None:
            if default_format not in FORMATS:
                raise ValueError("default format must be skill or agent")
            config["default_format"] = default_format
        if mode is not None:
            if mode not in MODES:
                raise ValueError("toast mode must be rapp1 or legacy")
            config["mode"] = mode
        config["schema"] = CONFIG_SCHEMA
        if default_format is not None or mode is not None:
            _atomic_write(
                path,
                (_json(config) + "\n").encode("utf-8"),
            )
    effective_format, effective_mode = _effective_settings(None, None)
    return {
        "status": "ok",
        "operation": "config",
        "path": str(path),
        "stored": config,
        "effective": {
            "default_format": effective_format,
            "mode": effective_mode,
        },
        "environment_overrides": {
            "RAPP_DEFAULT_FORMAT": os.environ.get("RAPP_DEFAULT_FORMAT"),
            "RAPP_TOAST_MODE": os.environ.get("RAPP_TOAST_MODE"),
        },
    }


def _identity_aliases(
    *,
    source_format: str,
    source_path: Path,
    raw: bytes,
    publisher: str,
    manifest_name: str | None,
) -> list[str]:
    labels = [
        f"{source_format}:path:{source_path}",
        f"{source_format}:sha256:{_sha256(raw)}:{publisher}",
    ]
    if manifest_name:
        labels.insert(0, f"agent:manifest:{manifest_name}")
    return [
        hashlib.sha256(
            b"rapp-agent-converter/identity-key/1\n"
            + label.encode("utf-8")
        ).hexdigest()
        for label in labels
    ]


def _persisted_rappid(
    *,
    source_format: str,
    source_path: Path,
    raw: bytes,
    publisher: str,
    slug: str,
    manifest_name: str | None = None,
    explicit: str | None = None,
    authoritative: str | None = None,
    carried: str | None = None,
) -> str:
    for label, value in (
        ("explicit", explicit),
        ("authoritative", authoritative),
        ("carried", carried),
    ):
        if value is not None and not _valid_rappid(value):
            raise ValueError(f"invalid {label} RAPP/1 identity: {value!r}")
    if (
        explicit is not None
        and authoritative is not None
        and explicit != authoritative
    ):
        raise ValueError(
            "explicit RAPPID conflicts with the authoritative agent identity; "
            "preserve it or perform an explicit re-genesis"
        )

    aliases = _identity_aliases(
        source_format=source_format,
        source_path=source_path,
        raw=raw,
        publisher=publisher,
        manifest_name=manifest_name,
    )
    path = _identity_path()
    lock = path.with_suffix(path.suffix + ".lock")
    with _exclusive_lock(lock):
        ledger = _read_json(
            path,
            {"schema": IDENTITY_SCHEMA, "entries": {}},
        )
        if ledger.get("schema") != IDENTITY_SCHEMA:
            raise ValueError(
                f"{path}: unsupported identity schema "
                f"{ledger.get('schema')!r}"
            )
        entries = ledger.get("entries")
        if not isinstance(entries, dict):
            raise ValueError(f"{path}: identity entries must be an object")
        found = {
            entries[key]["rappid"]
            for key in aliases
            if (
                isinstance(entries.get(key), dict)
                and _valid_rappid(entries[key].get("rappid"))
            )
        }
        preferred = explicit or authoritative or carried
        if len(found) > 1:
            raise ValueError(
                "identity ledger aliases disagree; refusing to remint or "
                "guess which capability identity is authoritative"
            )
        existing = next(iter(found), None)
        if preferred is not None and existing is not None and preferred != existing:
            raise ValueError(
                "identity ledger already binds this capability to a different "
                "mint-once RAPPID; use an explicit re-genesis workflow"
            )
        if preferred is None:
            preferred = existing
        chosen = preferred or _mint_rappid(publisher, slug)
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        changed = False
        for key in aliases:
            current = entries.get(key)
            if not isinstance(current, dict) or current.get("rappid") != chosen:
                entries[key] = {
                    "rappid": chosen,
                    "created_at": (
                        current.get("created_at")
                        if isinstance(current, dict)
                        else now
                    ),
                }
                changed = True
        if changed or not path.exists():
            ledger["schema"] = IDENTITY_SCHEMA
            ledger["entries"] = entries
            _atomic_write(
                path,
                (_json(ledger) + "\n").encode("utf-8"),
            )
    return chosen


def _grail_skill_path(rappid: str) -> Path:
    return _data_home() / "grail" / rappid.rsplit(":", 1)[-1] / "SKILL.md"


def _materialized_agent_path(rappid: str, filename: str) -> Path:
    return (
        _cache_home()
        / "materialized"
        / rappid.rsplit(":", 1)[-1]
        / filename
    )


def _skill_state(core, raw: bytes) -> tuple[str, dict | None]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError("SKILL.md must be UTF-8") from error
    active = _active_skill_capsule(text)
    record = _read_skill(core, raw, "SKILL.md")
    if active is None:
        raw_rapp = _metadata_for(record).get("rapp")
        if (
            isinstance(raw_rapp, dict)
            and isinstance(raw_rapp.get("schema"), str)
            and raw_rapp["schema"] != "rapp/1"
        ):
            raise ValueError(
                f"unsupported RAPP skill schema {raw_rapp['schema']!r}; "
                "install a reader for that major version"
            )
        return "raw", None
    metadata = _metadata_for(record)
    rapp = metadata.get("rapp")
    if isinstance(rapp, dict):
        schema = rapp.get("schema")
        if isinstance(schema, str) and schema != "rapp/1":
            raise ValueError(
                f"unsupported RAPP skill schema {schema!r}; "
                "install a reader for that major version"
            )
    compliant, _ = _is_rapp1_toast(core, raw)
    return ("rapp1" if compliant else "legacy"), record


def _grail_history(
    core,
    path: Path,
    new_bytes: bytes,
    rappid: str,
) -> tuple[list[tuple[Path, bytes]], set[Path]]:
    if not path.is_file():
        return [], set()
    current = path.read_bytes()
    if current == new_bytes:
        return [], set()
    state, rci = _skill_state(core, current)
    existing_rapp = _metadata_for(rci or {}).get("rapp")
    if (
        state != "rapp1"
        or not isinstance(existing_rapp, dict)
        or existing_rapp.get("rappid") != rappid
    ):
        return [], set()
    history = (
        path.parent
        / "history"
        / f"{_sha256(current)}.SKILL.md"
    )
    return [(history, current)], {path}


def _is_materialized_cache(path: Path) -> bool:
    try:
        path.resolve().relative_to(
            (_cache_home() / "materialized").resolve()
        )
        return True
    except ValueError:
        return False


def convert_path(
    path: str,
    *,
    to: str | None = None,
    out: str | None = None,
    publisher: str | None = None,
    rappid: str | None = None,
    force: bool = False,
    in_place: bool = False,
    mode: str | None = None,
) -> dict:
    target_format, selected_mode = _effective_settings(to, mode)
    requested_source = _absolute(path)
    source_is_symlink = requested_source.is_symlink()
    source = requested_source.resolve()
    if not source.is_file():
        raise FileNotFoundError(f"not found: {source}")
    if in_place and source_is_symlink:
        raise ValueError(
            "refusing in-place conversion through a symlink; use the default "
            "Grail record or address the real file explicitly"
        )
    if in_place and out:
        raise ValueError("--in-place and --out are mutually exclusive")
    core = _load_core()
    source_format = core.detect(str(source))
    raw = source.read_bytes()
    if selected_mode == "legacy" and out:
        raise ValueError(
            "--legacy cannot be combined with --out; legacy mode owns the "
            "adjacent source layout"
        )
    if (
        source_format == "skill"
        and target_format == "skill"
        and out
        and _absolute(out).resolve() == source
        and not in_place
    ):
        raise ValueError(
            "refusing to replace the source SKILL.md without --in-place"
        )

    if source_format == "agent":
        preview = _read_public_agent(core, raw, str(source))
        preview_manifest = _manifest_from_bytes(raw)
        canonical_agent = _canonical_agent_filename(
            preview_manifest,
            source.name,
        )
        effective_rappid = rappid
        legacy_skill_path = (
            source.parent / _kebab(preview.get("slug")) / "SKILL.md"
        )
        explicit_skill_path = (
            _absolute(out)
            if target_format == "skill" and out
            else legacy_skill_path
            if selected_mode == "legacy"
            else None
        )
        if (
            effective_rappid is None
            and explicit_skill_path is not None
            and explicit_skill_path.is_file()
        ):
            state, existing_capsule = _skill_state(
                core,
                explicit_skill_path.read_bytes(),
            )
            if state == "rapp1" and existing_capsule:
                existing_metadata = _metadata_for(existing_capsule)
                if (
                    existing_metadata.get("source_sha256") == _sha256(raw)
                    and existing_metadata.get("canonical_agent") == canonical_agent
                ):
                    effective_rappid = existing_metadata["rapp"]["rappid"]
        rci, skill_bytes = _project_agent(
            core,
            source,
            raw,
            explicit_rappid=effective_rappid,
        )
        rapp = _metadata_for(rci)["rapp"]
        skill_path = (
            _absolute(out)
            if target_format == "skill" and out
            else legacy_skill_path
            if selected_mode == "legacy"
            else _grail_skill_path(rapp["rappid"])
        )
        if skill_path.name.lower() != "skill.md":
            raise ValueError("skill output must be named SKILL.md")

        replacements = set()
        artifacts_to_write = [(skill_path, skill_bytes)]
        selected_artifact = skill_path
        if selected_mode == "legacy":
            artifacts_to_write.append(
                (skill_path.parent / canonical_agent, raw)
            )
        if target_format == "agent":
            if out:
                agent_path = _absolute(out)
            elif canonical_agent == source.name:
                agent_path = source
            elif selected_mode == "legacy":
                agent_path = source.with_name(canonical_agent)
            else:
                agent_path = _materialized_agent_path(
                    rapp["rappid"],
                    canonical_agent,
                )
            if not _valid_agent_filename(agent_path.name):
                raise ValueError("agent output must end in _agent.py")
            selected_artifact = agent_path
            if agent_path != source:
                artifacts_to_write.append((agent_path, raw))
                if _is_materialized_cache(agent_path):
                    replacements.add(agent_path)

        artifacts = _write_artifacts(
            artifacts_to_write,
            force=force,
            replace_paths=replacements,
        )
        return {
            "status": "ok",
            "source_format": "agent",
            "target_format": target_format,
            "configured_default": _stored_config()["default_format"],
            "mode": selected_mode,
            "canonical_grail": str(skill_path),
            "selected_artifact": str(selected_artifact),
            "normalized_through_agent": False,
            "transport_fidelity": "byte-exact agent restore",
            "source_unchanged": True,
            "rapp": rapp,
            "artifacts": artifacts,
        }

    state, capsule = _skill_state(core, raw)
    if state == "rapp1":
        rci = _read_skill(core, raw, str(source))
        rapp = _metadata_for(rci)["rapp"]
        if target_format == "skill" and not out and selected_mode != "legacy":
            return {
                "status": "ok",
                "source_format": "skill",
                "target_format": "skill",
                "configured_default": _stored_config()["default_format"],
                "mode": selected_mode,
                "canonical_grail": str(source),
                "selected_artifact": str(source),
                "already_toasted": True,
                "source_unchanged": True,
                "rapp": rapp,
                "artifacts": [],
            }
        if target_format == "skill":
            skill_path = _absolute(out) if out else source
            if skill_path.name.lower() != "skill.md":
                raise ValueError("skill output must be named SKILL.md")
            artifacts_to_write = [(skill_path, raw)]
            if selected_mode == "legacy":
                artifacts_to_write.append(
                    (
                        skill_path.parent / core.linked_agent_name(rci),
                        core.restore(rci, "agent"),
                    ),
                )
            artifacts = _write_artifacts(
                artifacts_to_write,
                force=force,
            )
            return {
                "status": "ok",
                "source_format": "skill",
                "target_format": "skill",
                "configured_default": _stored_config()["default_format"],
                "mode": selected_mode,
                "canonical_grail": str(skill_path),
                "selected_artifact": str(skill_path),
                "already_toasted": True,
                "source_unchanged": skill_path != source or raw == skill_path.read_bytes(),
                "rapp": rapp,
                "artifacts": artifacts,
            }

        agent_bytes = core.write_agent(rci)
        agent_name = core.linked_agent_name(rci)
        manifest = _validate_rar_agent(agent_bytes, agent_name)
        agent_path = (
            _absolute(out)
            if out
            else source.parent / agent_name
            if selected_mode == "legacy"
            else _materialized_agent_path(rapp["rappid"], agent_name)
        )
        if not _valid_agent_filename(agent_path.name):
            raise ValueError("agent output must end in _agent.py")
        replacements = {agent_path} if _is_materialized_cache(agent_path) else set()
        artifacts = _write_artifacts(
            [(agent_path, agent_bytes)],
            force=force,
            replace_paths=replacements,
        )
        return {
            "status": "ok",
            "source_format": "skill",
            "target_format": "agent",
            "configured_default": _stored_config()["default_format"],
            "mode": selected_mode,
            "canonical_grail": str(source),
            "selected_artifact": str(agent_path),
            "restored_byte_exact": True,
            "manifest": manifest["name"],
            "source_unchanged": True,
            "rapp": rapp,
            "artifacts": artifacts,
        }

    initial_rci = _read_skill(core, raw, str(source))
    default_agent_name = (
        core.linked_agent_name(initial_rci)
        if core.restore(initial_rci, "agent") is not None
        else core.agent_filename(initial_rci)
    )
    agent_name = default_agent_name
    legacy_or_in_place = selected_mode == "legacy" or in_place
    candidate_skill_path = (
        source
        if legacy_or_in_place
        else _absolute(out)
        if target_format == "skill" and out
        else None
    )

    effective_rappid = rappid
    if (
        effective_rappid is None
        and candidate_skill_path is not None
        and candidate_skill_path.is_file()
        and candidate_skill_path.resolve() != source
    ):
        existing_state, existing_capsule = _skill_state(
            core,
            candidate_skill_path.read_bytes(),
        )
        if existing_state == "rapp1" and existing_capsule:
            existing_metadata = _metadata_for(existing_capsule)
            if (
                existing_metadata.get("source_format") == "skill"
                and existing_metadata.get("source_sha256") == _sha256(raw)
                and existing_metadata.get("canonical_agent") == agent_name
            ):
                effective_rappid = existing_metadata["rapp"]["rappid"]

    rci, agent_bytes, skill_bytes = _normalize_skill(
        core,
        source,
        raw,
        publisher=publisher,
        explicit_rappid=effective_rappid,
        agent_filename=agent_name,
    )
    rapp = _metadata_for(rci)["rapp"]
    skill_path = (
        source
        if legacy_or_in_place
        else _absolute(out)
        if target_format == "skill" and out
        else _grail_skill_path(rapp["rappid"])
    )
    if skill_path.name.lower() != "skill.md":
        raise ValueError("skill output must be named SKILL.md")
    if skill_path.resolve() == source and not legacy_or_in_place:
        raise ValueError(
            "automatic Grail path resolves to the source SKILL.md; "
            "use --in-place or move the legacy source outside the Grail store"
        )

    replacements = set()
    artifacts_to_write = []
    replace_source = None
    if skill_path.resolve() == source:
        backup = source.parent / "rapp" / "source" / source.name
        artifacts_to_write.append((backup, raw))
        replace_source = source
    if selected_mode == "legacy":
        artifacts_to_write.append((skill_path.parent / agent_name, agent_bytes))
    artifacts_to_write.append((skill_path, skill_bytes))

    selected_artifact = skill_path
    if target_format == "agent":
        agent_path = (
            _absolute(out)
            if out
            else skill_path.parent / agent_name
            if selected_mode == "legacy" or in_place
            else _materialized_agent_path(rapp["rappid"], agent_name)
        )
        if not _valid_agent_filename(agent_path.name):
            raise ValueError("agent output must end in _agent.py")
        selected_artifact = agent_path
        if not any(path == agent_path for path, _ in artifacts_to_write):
            artifacts_to_write.append((agent_path, agent_bytes))
        if _is_materialized_cache(agent_path):
            replacements.add(agent_path)

    artifacts = _write_artifacts(
        artifacts_to_write,
        force=force,
        replace_source=replace_source,
        replace_paths=replacements,
    )
    return {
        "status": "ok",
        "source_format": "skill",
        "source_state": state,
        "target_format": target_format,
        "configured_default": _stored_config()["default_format"],
        "mode": selected_mode,
        "canonical_grail": str(skill_path),
        "selected_artifact": str(selected_artifact),
        "normalized_through_agent": True,
        "source_skill_vaulted": True,
        "source_unchanged": skill_path.resolve() != source,
        "rapp": rapp,
        "artifacts": artifacts,
    }


def inspect_path(path: str) -> dict:
    source = Path(path).expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(f"not found: {source}")
    core = _load_core()
    source_format = core.detect(str(source))
    raw = source.read_bytes()
    if source_format == "agent":
        manifest = _manifest_from_bytes(raw)
        rci = _read_public_agent(core, raw, str(source))
        return {
            "status": "ok",
            "format": "agent",
            "rar_valid": _manifest_is_valid(manifest),
            "manifest": manifest.get("name"),
            "rappid": _rappid_from(rci, manifest, None),
            "sha256": _sha256(raw),
        }

    state, capsule = _skill_state(core, raw)
    rci = _read_skill(core, raw, str(source))
    metadata = _metadata_for(rci)
    return {
        "status": "ok",
        "format": "skill",
        "state": {
            "rapp1": "rapp1-toasted",
            "legacy": "legacy-toasted",
            "raw": "raw",
        }[state],
        "canonical_format": "skill",
        "configured_default": _effective_settings(None, None)[0],
        "rapp": metadata.get("rapp"),
        "vaulted_agent": core.restore(rci, "agent") is not None,
        "vaulted_source_skill": (
            isinstance((rci.get("platform") or {}).get("source_skill"), dict)
        ),
        "sha256": _sha256(raw),
    }


def verify_path(path: str) -> dict:
    source = Path(path).expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(f"not found: {source}")
    core = _load_core()
    source_format = core.detect(str(source))
    raw = source.read_bytes()
    if source_format == "agent":
        parsed_manifest = _manifest_from_bytes(raw)
        canonical_agent = _canonical_agent_filename(
            parsed_manifest,
            source.name,
        )
        manifest = _validate_rar_agent(raw, canonical_agent)
        rci, skill_bytes = _project_agent(
            core,
            source,
            raw,
            explicit_rappid=None,
            persist_identity=False,
        )
        restored = core.write_agent(_read_skill(core, skill_bytes, "SKILL.md"))
        return {
            "status": "ok",
            "format": "agent",
            "rar_valid": True,
            "manifest": manifest["name"],
            "agent_skill_agent_identical": restored == raw,
            "rapp": _metadata_for(rci)["rapp"],
        }

    state, _ = _skill_state(core, raw)
    if state != "rapp1":
        return {
            "status": "error",
            "format": "skill",
            "rapp1_toasted": False,
            "state": state,
            "fix": (
                "run rapp-agent-converter/scripts/toast.py "
                f"{source}"
            ),
        }
    rci = _read_skill(core, raw, str(source))
    agent_bytes = core.restore(rci, "agent")
    if agent_bytes is None:
        raise ValueError("RAPP/1 Toasted skill does not vault an agent")
    agent_name = core.linked_agent_name(rci)
    manifest = _validate_rar_agent(agent_bytes, agent_name)
    source_vault_ok = None
    if isinstance((rci.get("platform") or {}).get("source_skill"), dict):
        restored_source, _ = _restore_source_skill(rci)
        source_vault_ok = _sha256(restored_source) == (
            (rci.get("platform") or {})["source_skill"]["sha256"]
        )
    return {
        "status": "ok",
        "format": "skill",
        "rapp1_toasted": True,
        "canonical_format": "skill",
        "vaulted_agent_valid_rar": True,
        "vaulted_agent_manifest": manifest["name"],
        "vaulted_source_skill_valid": source_vault_ok,
        "rapp": _metadata_for(rci)["rapp"],
    }


def restore_raw_skill(path: str, *, out: str | None, force: bool = False) -> dict:
    source = Path(path).expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(f"not found: {source}")
    core = _load_core()
    if core.detect(str(source)) != "skill":
        raise ValueError("restore-raw requires a SKILL.md input")
    rci = _read_skill(core, source.read_bytes(), str(source))
    raw, filename = _restore_source_skill(rci)
    target = (
        _absolute(out)
        if out
        else source.with_name(filename)
    )
    if target.resolve() == source:
        target = source.with_name(
            source.stem + ".raw" + source.suffix
        )
    artifacts = _write_artifacts([(target, raw)], force=force)
    return {
        "status": "ok",
        "restored": str(target),
        "sha256": _sha256(raw),
        "artifacts": artifacts,
    }


KERNEL_AGENT_FILES = {
    "basic_agent.py",
    "context_memory_agent.py",
    "manage_memory_agent.py",
    "learn_new_agent.py",
    "swarm_factory_agent.py",
    "hacker_news_agent.py",
}
KERNEL_AGENT_NAMES = {
    "BasicAgent",
    "ContextMemory",
    "ManageMemory",
    "LearnNew",
    "SwarmFactory",
    "HackerNews",
}


def _brainstem_agents_dir(
    *,
    brainstem_dir: str | None,
    agents_dir: str | None,
) -> Path:
    if agents_dir:
        target = _absolute(agents_dir)
    elif brainstem_dir:
        target = _absolute(brainstem_dir) / "agents"
    elif os.environ.get("RAPP_BRAINSTEM_AGENTS_DIR"):
        target = _absolute(os.environ["RAPP_BRAINSTEM_AGENTS_DIR"])
    elif os.environ.get("AGENTS_PATH"):
        target = _absolute(os.environ["AGENTS_PATH"])
    elif BASE_DIR.name == "agents":
        target = BASE_DIR
    else:
        raise ValueError(
            "hotload needs brainstem_dir or agents_dir when the converter is "
            "not already running from a Brainstem agents directory"
        )
    target.mkdir(parents=True, exist_ok=True)
    return target.resolve()


def _plan_hotload(
    source: Path,
    *,
    publisher: str | None,
    rappid: str | None,
) -> dict:
    core = _load_core()
    raw = source.read_bytes()
    source_format = core.detect(str(source))
    if source_format == "agent":
        rci, skill_bytes = _project_agent(
            core,
            source,
            raw,
            explicit_rappid=rappid,
        )
        agent_bytes = raw
        filename = core.linked_agent_name(rci)
        skill_path = _grail_skill_path(
            _metadata_for(rci)["rapp"]["rappid"]
        )
        grail_artifact = (skill_path, skill_bytes)
    else:
        state, _ = _skill_state(core, raw)
        if state == "rapp1":
            rci = _read_skill(core, raw, str(source))
            agent_bytes = core.restore(rci, "agent")
            if agent_bytes is None:
                raise ValueError("RAPP/1 Grail does not vault an agent")
            filename = core.linked_agent_name(rci)
            skill_path = source
            grail_artifact = None
        else:
            initial_rci = _read_skill(core, raw, str(source))
            filename = (
                core.linked_agent_name(initial_rci)
                if core.restore(initial_rci, "agent") is not None
                else core.agent_filename(initial_rci)
            )
            rci, agent_bytes, skill_bytes = _normalize_skill(
                core,
                source,
                raw,
                publisher=publisher,
                explicit_rappid=rappid,
                agent_filename=filename,
            )
            skill_path = _grail_skill_path(
                _metadata_for(rci)["rapp"]["rappid"]
            )
            grail_artifact = (skill_path, skill_bytes)
    manifest = _validate_rar_agent(agent_bytes, filename)
    public = _read_public_agent(core, agent_bytes, filename)
    return {
        "core": core,
        "source_format": source_format,
        "source_sha256": _sha256(raw),
        "filename": filename,
        "agent_bytes": agent_bytes,
        "manifest": manifest,
        "runtime_name": public.get("name"),
        "rapp": _metadata_for(rci)["rapp"],
        "canonical_grail": str(skill_path),
        "grail_artifact": grail_artifact,
    }


def _commit_hotload(
    *,
    core,
    target_dir: Path,
    destination: Path,
    filename: str,
    agent_bytes: bytes,
    manifest: dict,
    runtime_name: str,
    source: Path,
    plan: dict,
    force: bool,
) -> dict:
    directory_lock = hashlib.sha256(
        b"rapp-agent-converter/brainstem-dir-lock/1\n"
        + str(target_dir).encode("utf-8")
    ).hexdigest()
    with _exclusive_lock(
        _lock_root() / f"brainstem-{directory_lock}.lock"
    ):
        collisions = []
        for candidate in sorted(target_dir.glob("*_agent.py")):
            if candidate == destination:
                continue
            try:
                candidate_name = _read_public_agent(
                    core,
                    candidate.read_bytes(),
                    candidate.name,
                ).get("name")
            except (OSError, SystemExit, ValueError):
                continue
            if candidate_name == runtime_name:
                collisions.append(candidate.name)
        if collisions:
            raise ValueError(
                f"runtime name {runtime_name!r} already belongs to "
                + ", ".join(collisions)
            )

        artifacts = []
        result = "installed"
        origin_path = destination.with_suffix(
            destination.suffix + ".origin.json"
        )
        origin_exists = False
        if destination.exists():
            existing = destination.read_bytes()
            if existing == agent_bytes:
                result = "already-installed"
                if origin_path.is_file():
                    existing_origin = _read_json(origin_path, {})
                    if (
                        existing_origin.get("sha256") == _sha256(agent_bytes)
                        and existing_origin.get("rappid")
                        == plan["rapp"]["rappid"]
                    ):
                        origin_exists = True
                        plan = {
                            **plan,
                            "canonical_grail": existing_origin.get(
                                "grail",
                                plan["canonical_grail"],
                            ),
                            "grail_artifact": None,
                        }
                    elif not force:
                        raise ValueError(
                            "installed agent matches but its provenance binds "
                            "a different identity; pass force only after review"
                        )
            elif not force:
                raise FileExistsError(
                    f"{destination} differs; pass force=true to back it up "
                    "and replace it"
                )
            else:
                backup = (
                    target_dir
                    / ".rapp-backups"
                    / f"{filename}.{_sha256(existing)[:16]}.bak"
                )
                artifacts.append((backup, existing))

        if plan.get("grail_artifact") is not None:
            artifacts.append(plan["grail_artifact"])
        if result == "installed":
            artifacts.append((destination, agent_bytes))
        if not origin_exists:
            origin = {
                "schema": "rapp-agent-origin/1.0",
                "agent": filename,
                "manifest": manifest["name"],
                "runtime_name": runtime_name,
                "sha256": _sha256(agent_bytes),
                "source_format": plan["source_format"],
                "source_sha256": plan["source_sha256"],
                "grail": plan["canonical_grail"],
                "rappid": plan["rapp"]["rappid"],
                "installed_at": datetime.now(timezone.utc).strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                ),
                "installer": "@rapp/rapp_agent_converter",
            }
            artifacts.append(
                (
                    origin_path,
                    (_json(origin) + "\n").encode("utf-8"),
                )
            )
        written = _write_artifacts(
            artifacts,
            force=force,
        )
        return {
            "status": "ok",
            "operation": "hotload",
            "result": result,
            "agent": filename,
            "runtime_name": runtime_name,
            "path": str(destination),
            "sha256": _sha256(agent_bytes),
            "canonical_grail": plan["canonical_grail"],
            "rapp": plan["rapp"],
            "hotload": (
                "No restart required; Brainstem discovery reloads agents "
                "from disk."
            ),
            "artifacts": written,
        }


def hotload_path(
    path: str,
    *,
    brainstem_dir: str | None = None,
    agents_dir: str | None = None,
    publisher: str | None = None,
    rappid: str | None = None,
    force: bool = False,
) -> dict:
    source = _absolute(path).resolve()
    if not source.is_file():
        raise FileNotFoundError(f"not found: {source}")
    plan = _plan_hotload(
        source,
        publisher=publisher,
        rappid=rappid,
    )
    core = plan["core"]
    filename = plan["filename"]
    protected_files = {name.casefold() for name in KERNEL_AGENT_FILES}
    if filename.casefold() in protected_files:
        raise ValueError(f"refusing to replace sacred kernel agent {filename}")
    target_dir = _brainstem_agents_dir(
        brainstem_dir=brainstem_dir,
        agents_dir=agents_dir,
    )
    destination = target_dir / filename
    for protected in KERNEL_AGENT_FILES:
        protected_path = target_dir / protected
        if not protected_path.exists() or not destination.exists():
            continue
        try:
            if os.path.samefile(destination, protected_path):
                raise ValueError(
                    f"refusing destination that aliases sacred kernel agent "
                    f"{protected}"
                )
        except OSError:
            continue

    agent_bytes = plan["agent_bytes"]
    manifest = plan["manifest"]
    runtime_name = plan["runtime_name"]
    protected_names = {name.casefold() for name in KERNEL_AGENT_NAMES}
    if (
        isinstance(runtime_name, str)
        and runtime_name.casefold() in protected_names
    ):
        raise ValueError(
            f"refusing agent that declares sacred kernel name {runtime_name}"
        )
    return _commit_hotload(
        core=core,
        target_dir=target_dir,
        destination=destination,
        filename=filename,
        agent_bytes=agent_bytes,
        manifest=manifest,
        runtime_name=runtime_name,
        source=source,
        plan=plan,
        force=force,
    )


class RappAgentConverterAgent(BasicAgent):
    def __init__(self):
        self.name = "RappAgentConverter"
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "auto",
                            "convert",
                            "toast",
                            "materialize",
                            "hotload",
                            "inspect",
                            "verify",
                            "roundtrip",
                            "soak",
                            "restore_raw",
                            "config",
                        ],
                        "description": (
                            "Convert, materialize, hotload, verify, or configure "
                            "the agent/skill compatibility membrane."
                        ),
                    },
                    "path": {
                        "type": "string",
                        "description": "RAR *_agent.py or SKILL.md input.",
                    },
                    "to": {
                        "type": "string",
                        "enum": ["skill", "agent"],
                        "description": (
                            "Selected materialization. Defaults to the global "
                            "converter setting; the Grail remains SKILL.md."
                        ),
                    },
                    "out": {
                        "type": "string",
                        "description": "Optional output path.",
                    },
                    "publisher": {
                        "type": "string",
                        "description": (
                            "Publisher for agents synthesized from raw skills. "
                            "Defaults to RAPP_PUBLISHER or @local."
                        ),
                    },
                    "rappid": {
                        "type": "string",
                        "description": "Optional existing mint-once RAPP/1 identity.",
                    },
                    "force": {
                        "type": "boolean",
                        "description": "Replace a conflicting output file.",
                    },
                    "in_place": {
                        "type": "boolean",
                        "description": (
                            "Explicitly replace a raw/legacy source SKILL.md "
                            "after preserving an exact backup."
                        ),
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["rapp1", "legacy"],
                        "description": (
                            "rapp1 writes a Grail record without duplicates; "
                            "legacy preserves adjacent pair behavior."
                        ),
                    },
                    "default_format": {
                        "type": "string",
                        "enum": ["skill", "agent"],
                        "description": "Global selected output for config.",
                    },
                    "brainstem_dir": {
                        "type": "string",
                        "description": "Brainstem root for operation=hotload.",
                    },
                    "agents_dir": {
                        "type": "string",
                        "description": "Exact Brainstem agents directory.",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        operation = kwargs.get("operation") or "auto"
        path = kwargs.get("path")
        if operation != "config" and not path:
            return _json({
                "status": "error",
                "message": "path is required",
                "canonical_format": "skill",
            })
        try:
            if operation in {"auto", "convert", "toast", "materialize"}:
                selected = kwargs.get("to")
                if operation == "toast":
                    selected = "skill"
                elif operation == "materialize":
                    selected = "agent"
                result = convert_path(
                    str(path),
                    to=str(selected) if selected else None,
                    out=kwargs.get("out"),
                    publisher=kwargs.get("publisher"),
                    rappid=kwargs.get("rappid"),
                    force=bool(kwargs.get("force", False)),
                    in_place=bool(kwargs.get("in_place", False)),
                    mode=kwargs.get("mode"),
                )
            elif operation == "inspect":
                result = inspect_path(str(path))
            elif operation in {"verify", "roundtrip", "soak"}:
                result = verify_path(str(path))
            elif operation == "hotload":
                result = hotload_path(
                    str(path),
                    brainstem_dir=kwargs.get("brainstem_dir"),
                    agents_dir=kwargs.get("agents_dir"),
                    publisher=kwargs.get("publisher"),
                    rappid=kwargs.get("rappid"),
                    force=bool(kwargs.get("force", False)),
                )
            elif operation == "restore_raw":
                result = restore_raw_skill(
                    str(path),
                    out=kwargs.get("out"),
                    force=bool(kwargs.get("force", False)),
                )
            elif operation == "config":
                result = configure_converter(
                    default_format=kwargs.get("default_format"),
                    mode=kwargs.get("mode"),
                )
            else:
                result = {
                    "status": "error",
                    "message": f"unknown operation: {operation}",
                }
        except (OSError, RuntimeError, SyntaxError, SystemExit, ValueError) as error:
            result = {
                "status": "error",
                "message": f"{type(error).__name__}: {error}",
                "canonical_format": "skill",
            }
        return _json(result)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="toast.py",
        description=(
            "Auto-convert agent.py and SKILL.md; RAPP/1 Toasted SKILL.md is "
            "the default output."
        ),
    )
    subparsers = parser.add_subparsers(dest="command")

    def conversion_flags(command, *, target=True):
        if target:
            command.add_argument("--to", choices=("skill", "agent"))
        command.add_argument("-o", "--out")
        command.add_argument("--publisher")
        command.add_argument("--rappid")
        command.add_argument("--force", action="store_true")
        command.add_argument("--in-place", action="store_true")
        command.add_argument("--mode", choices=("rapp1", "legacy"))
        command.add_argument(
            "--legacy",
            action="store_const",
            const="legacy",
            dest="mode",
        )

    convert = subparsers.add_parser("convert")
    convert.add_argument("path")
    conversion_flags(convert)

    toast = subparsers.add_parser("toast")
    toast.add_argument("paths", nargs="+")
    conversion_flags(toast, target=False)

    materialize = subparsers.add_parser("materialize")
    materialize.add_argument("path")
    conversion_flags(materialize, target=False)

    hotload = subparsers.add_parser("hotload")
    hotload.add_argument("path")
    hotload.add_argument("--brainstem-dir")
    hotload.add_argument("--agents-dir")
    hotload.add_argument("--publisher")
    hotload.add_argument("--rappid")
    hotload.add_argument("--force", action="store_true")

    inspect = subparsers.add_parser("inspect")
    inspect.add_argument("path")

    verify = subparsers.add_parser("verify")
    verify.add_argument("path")

    roundtrip = subparsers.add_parser("roundtrip")
    roundtrip.add_argument("path")

    soak = subparsers.add_parser("soak")
    soak.add_argument("paths", nargs="+")

    restore = subparsers.add_parser("restore-raw")
    restore.add_argument("path")
    restore.add_argument("-o", "--out")
    restore.add_argument("--force", action="store_true")

    config = subparsers.add_parser("config")
    config.add_argument("--default-format", choices=("skill", "agent"))
    config.add_argument("--mode", choices=("rapp1", "legacy"))
    return parser


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv == ["--tool"]:
        print(_json(RappAgentConverterAgent().to_tool()))
        return 0
    if not argv:
        print(RappAgentConverterAgent().perform())
        return 0
    commands = {
        "convert",
        "toast",
        "materialize",
        "hotload",
        "inspect",
        "verify",
        "roundtrip",
        "soak",
        "restore-raw",
        "config",
    }
    if argv[0] not in commands:
        argv.insert(0, "convert")
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "convert":
            result = convert_path(
                args.path,
                to=args.to,
                out=args.out,
                publisher=args.publisher,
                rappid=args.rappid,
                force=args.force,
                in_place=args.in_place,
                mode=args.mode,
            )
        elif args.command == "toast":
            if args.out and len(args.paths) != 1:
                raise ValueError("--out is valid only when toasting one path")
            results = [
                convert_path(
                    path,
                    to="skill",
                    out=args.out,
                    publisher=args.publisher,
                    rappid=args.rappid,
                    force=args.force,
                    in_place=args.in_place,
                    mode=args.mode,
                )
                for path in args.paths
            ]
            result = results[0] if len(results) == 1 else {
                "status": "ok",
                "operation": "toast",
                "results": results,
            }
        elif args.command == "materialize":
            result = convert_path(
                args.path,
                to="agent",
                out=args.out,
                publisher=args.publisher,
                rappid=args.rappid,
                force=args.force,
                in_place=args.in_place,
                mode=args.mode,
            )
        elif args.command == "hotload":
            result = hotload_path(
                args.path,
                brainstem_dir=args.brainstem_dir,
                agents_dir=args.agents_dir,
                publisher=args.publisher,
                rappid=args.rappid,
                force=args.force,
            )
        elif args.command == "inspect":
            result = inspect_path(args.path)
        elif args.command in {"verify", "roundtrip"}:
            result = verify_path(args.path)
        elif args.command == "soak":
            checks = [verify_path(path) for path in args.paths]
            result = {
                "status": (
                    "ok"
                    if all(item.get("status") == "ok" for item in checks)
                    else "error"
                ),
                "operation": "soak",
                "checks": checks,
            }
        elif args.command == "config":
            result = configure_converter(
                default_format=args.default_format,
                mode=args.mode,
            )
        else:
            result = restore_raw_skill(
                args.path,
                out=args.out,
                force=args.force,
            )
    except (OSError, RuntimeError, SyntaxError, SystemExit, ValueError) as error:
        print(_json({
            "status": "error",
            "message": f"{type(error).__name__}: {error}",
            "canonical_format": "skill",
        }), file=sys.stderr)
        return 1
    print(_json(result))
    return 0 if result.get("status") == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
