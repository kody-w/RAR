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
EMBEDDED_TOASTER_GZIP_BASE64 = "__RAPP_TOASTER_EMBEDDED_GZIP_BASE64__"
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
