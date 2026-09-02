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
