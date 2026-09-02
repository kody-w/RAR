#!/usr/bin/env python3
"""RAPP Agent Converter - make agent.py and SKILL.md interchangeable.

The default artifact is a RAPP/1 Toasted SKILL.md. RAR agents project to that
format without changing their source bytes. Raw or legacy skills first cross
the RAR agent membrane:

    raw SKILL.md -> valid RAR single-file agent -> RAPP/1 Toasted SKILL.md

That intermediate agent is not an implementation guess. It carries the exact
authored Markdown in its RCI ledger, exposes the skill's typed contract when
one exists, and remains executable outside a Brainstem. The final Toasted
skill vaults both the normalized agent and the byte-exact source Markdown.

The converter is local-only, stdlib-only, and delegates the low-level RCI
codec to a checksum-pinned RAPP Toaster shipped in the same skill package.

Usage:
    python3 scripts/toast.py path/to/example_agent.py
    python3 scripts/toast.py path/to/SKILL.md
    python3 scripts/toast.py path/to/SKILL.md --to agent
    python3 scripts/toast.py verify path/to/SKILL.md
    python3 scripts/toast.py restore-raw path/to/SKILL.md
"""

from __future__ import annotations

import argparse
import ast
import base64
import copy
import gzip
import hashlib
import importlib.util
import json
import os
import pprint
import re
import sys
import tempfile
import uuid
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

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/rapp_agent_converter",
    "version": "1.0.0",
    "display_name": "RappAgentConverter",
    "description": (
        "Converts RAR agent.py files and SKILL.md files in both directions, "
        "automatically normalizing every raw skill through a valid RAR agent "
        "and emitting a RAPP/1 Toasted SKILL.md by default."
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
    if core_path is None:
        raise RuntimeError(
            "pinned RAPP Toaster is missing; keep the rapp-agent-converter "
            "skill directory intact"
        )

    data = core_path.read_bytes()
    actual = _sha256(data)
    if actual != PINNED_TOASTER_SHA256:
        raise RuntimeError(
            "pinned RAPP Toaster failed SHA-256 verification "
            f"(expected {PINNED_TOASTER_SHA256}, got {actual})"
        )
    spec = importlib.util.spec_from_file_location(
        "_rapp_agent_converter_toaster",
        core_path,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load pinned RAPP Toaster from {core_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
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


def _canonical_agent_filename(manifest: dict, filename: str) -> str:
    basename = Path(filename).name
    if re.fullmatch(r"[A-Za-z0-9_]+_agent\.py", basename):
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


def _rappid_from_metadata(rci: dict) -> str | None:
    metadata = _metadata_for(rci)
    rapp_meta = metadata.get("rapp")
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
    manifest_rapp = manifest.get("rapp")
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
        "toasted": True,
        "canonical_agent": canonical_agent,
        "source_format": source_format,
        "source_sha256": source_sha256,
        "normalization_path": normalization_path,
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
        raw = gzip.decompress(base64.b64decode(entry["gzip_base64"]))
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


def _validate_rar_agent(data: bytes, filename: str) -> dict:
    if not re.fullmatch(r"[A-Za-z0-9_]+_agent\.py", Path(filename).name):
        raise ValueError("RAR agent filename must be snake_case and end _agent.py")
    text = data.decode("utf-8")
    compile(text, filename, "exec")
    manifest = _manifest_from_bytes(data)
    if not _manifest_is_valid(manifest):
        raise ValueError("generated agent does not satisfy the RAR manifest contract")
    if not _has_rar_agent_class(data):
        raise ValueError(
            "generated agent has no BasicAgent-derived class defining perform()"
        )
    return manifest


def _is_rapp1_toast(core, raw: bytes) -> tuple[bool, dict | None]:
    try:
        capsule = core.unpack_capsule(raw.decode("utf-8"))
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
    rci = core.read_skill(raw, str(source_path))
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
    if not re.fullmatch(r"[A-Za-z0-9_]+_agent\.py", filename):
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
    if explicit_rappid is not None:
        if not _valid_rappid(explicit_rappid):
            raise ValueError(f"invalid RAPP/1 identity: {explicit_rappid!r}")
        if agent_rappid is not None and agent_rappid != explicit_rappid:
            raise ValueError(
                "explicit RAPPID conflicts with the vaulted agent identity; "
                "preserve the agent identity or perform an explicit re-genesis"
            )
        rappid = explicit_rappid
    else:
        rappid = (
            agent_rappid
            or skill_rappid
            or _mint_rappid(
                owner,
                rci.get("slug") or rci.get("name") or "skill",
            )
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
    agent_rci = core.read_agent(agent_bytes, filename)
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
    projected = core.read_skill(skill_bytes, "SKILL.md")
    if core.restore(projected, "agent") != agent_bytes:
        raise RuntimeError("Toasted skill did not restore its normalized agent exactly")
    return agent_rci, agent_bytes, skill_bytes


def _project_agent(
    core,
    source_path: Path,
    raw: bytes,
    *,
    explicit_rappid: str | None,
) -> tuple[dict, bytes]:
    manifest = _manifest_from_bytes(raw)
    canonical_agent = _canonical_agent_filename(manifest, source_path.name)
    try:
        _validate_rar_agent(raw, canonical_agent)
    except ValueError:
        raise ValueError(f"{source_path}: not a valid RAR single-file agent")
    rci = core.read_agent(raw, str(source_path))
    rci["preserved"]["agent"]["filename"] = canonical_agent
    publisher = manifest["name"].split("/", 1)[0]
    manifest_rappid = _rappid_from_manifest(manifest)
    ledger_rappid = _rappid_from_metadata(rci)
    if explicit_rappid is not None:
        if not _valid_rappid(explicit_rappid):
            raise ValueError(f"invalid RAPP/1 identity: {explicit_rappid!r}")
        if manifest_rappid is not None and manifest_rappid != explicit_rappid:
            raise ValueError(
                "explicit RAPPID conflicts with the source agent identity; "
                "preserve the agent identity or perform an explicit re-genesis"
            )
        rappid = explicit_rappid
    else:
        rappid = (
            manifest_rappid
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
    projected = core.read_skill(skill_bytes, "SKILL.md")
    if core.restore(projected, "agent") != raw:
        raise RuntimeError("Toasted skill did not restore the RAR agent byte-exact")
    return rci, skill_bytes


def _atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
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
        os.replace(temporary, path)
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
) -> list[dict]:
    normalized_source = replace_source.resolve() if replace_source else None
    for path, data in artifacts:
        if not path.exists() or path.read_bytes() == data:
            continue
        if normalized_source is not None and path.resolve() == normalized_source:
            continue
        if not force:
            raise FileExistsError(
                f"{path} exists with different content; pass force=true or --force"
            )

    written = []
    seen = set()
    for path, data in artifacts:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        status = "unchanged" if path.exists() and path.read_bytes() == data else "written"
        if status == "written":
            _atomic_write(path, data)
        written.append({
            "path": str(path),
            "sha256": _sha256(data),
            "status": status,
        })
    return written


def convert_path(
    path: str,
    *,
    to: str = "skill",
    out: str | None = None,
    publisher: str | None = None,
    rappid: str | None = None,
    force: bool = False,
) -> dict:
    if to not in {"agent", "skill"}:
        raise ValueError("to must be 'agent' or 'skill'")
    source = Path(path).expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(f"not found: {source}")
    core = _load_core()
    source_format = core.detect(str(source))
    raw = source.read_bytes()

    if source_format == "agent":
        if to == "agent":
            manifest = _manifest_from_bytes(raw)
            canonical_agent = _canonical_agent_filename(manifest, source.name)
            manifest = _validate_rar_agent(raw, canonical_agent)
            artifacts = []
            if out or canonical_agent != source.name:
                agent_path = (
                    Path(out).expanduser().resolve()
                    if out
                    else source.with_name(canonical_agent)
                )
                if not agent_path.name.endswith("_agent.py"):
                    raise ValueError("agent output must end in _agent.py")
                artifacts = _write_artifacts(
                    [(agent_path, raw)],
                    force=force,
                )
            return {
                "status": "ok",
                "source_format": "agent",
                "target_format": "agent",
                "default_format": "skill",
                "already_valid": True,
                "manifest": manifest["name"],
                "artifacts": artifacts,
            }
        preview = core.read_agent(raw, str(source))
        preview_manifest = _manifest_from_bytes(raw)
        canonical_agent = _canonical_agent_filename(
            preview_manifest,
            source.name,
        )
        skill_path = (
            Path(out).expanduser().resolve()
            if out
            else source.parent / _kebab(preview.get("slug")) / "SKILL.md"
        )
        if skill_path.name.lower() != "skill.md":
            raise ValueError("skill output must be named SKILL.md")
        effective_rappid = rappid
        if effective_rappid is None and skill_path.is_file():
            existing = skill_path.read_bytes()
            existing_compliant, existing_capsule = _is_rapp1_toast(
                core,
                existing,
            )
            if existing_compliant and existing_capsule:
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
        linked = skill_path.parent / core.linked_agent_name(rci)
        artifacts = _write_artifacts(
            [(linked, raw), (skill_path, skill_bytes)],
            force=force,
        )
        rapp = _metadata_for(rci)["rapp"]
        return {
            "status": "ok",
            "source_format": "agent",
            "target_format": "skill",
            "default_format": "skill",
            "normalized_through_agent": False,
            "transport_fidelity": "byte-exact agent restore",
            "rapp": rapp,
            "artifacts": artifacts,
        }

    compliant, capsule = _is_rapp1_toast(core, raw)
    if compliant:
        rci = core.read_skill(raw, str(source))
        if to == "skill" and not out:
            return {
                "status": "ok",
                "source_format": "skill",
                "target_format": "skill",
                "default_format": "skill",
                "already_toasted": True,
                "rapp": _metadata_for(rci)["rapp"],
                "artifacts": [],
            }
        if to == "skill":
            skill_path = Path(out).expanduser().resolve()
            if skill_path.name.lower() != "skill.md":
                raise ValueError("skill output must be named SKILL.md")
            artifacts_to_write = []
            agent_bytes = core.restore(rci, "agent")
            if agent_bytes is not None:
                agent_name = core.linked_agent_name(rci)
                artifacts_to_write.append((skill_path.parent / agent_name, agent_bytes))
            artifacts_to_write.append((skill_path, raw))
            artifacts = _write_artifacts(artifacts_to_write, force=force)
            return {
                "status": "ok",
                "source_format": "skill",
                "target_format": "skill",
                "default_format": "skill",
                "already_toasted": True,
                "rapp": _metadata_for(rci)["rapp"],
                "artifacts": artifacts,
            }

        agent_bytes = core.write_agent(rci)
        agent_name = core.linked_agent_name(rci)
        manifest = _validate_rar_agent(agent_bytes, agent_name)
        agent_path = (
            Path(out).expanduser().resolve()
            if out
            else source.parent / agent_name
        )
        if not agent_path.name.endswith("_agent.py"):
            raise ValueError("agent output must end in _agent.py")
        artifacts = _write_artifacts([(agent_path, agent_bytes)], force=force)
        return {
            "status": "ok",
            "source_format": "skill",
            "target_format": "agent",
            "default_format": "skill",
            "restored_byte_exact": True,
            "manifest": manifest["name"],
            "rapp": _metadata_for(rci)["rapp"],
            "artifacts": artifacts,
        }

    initial_rci = core.read_skill(raw, str(source))
    default_agent_name = (
        core.linked_agent_name(initial_rci)
        if core.restore(initial_rci, "agent") is not None
        else core.agent_filename(initial_rci)
    )
    if to == "agent" and out:
        agent_path = Path(out).expanduser().resolve()
        if not agent_path.name.endswith("_agent.py"):
            raise ValueError("agent output must end in _agent.py")
        agent_name = agent_path.name
        skill_path = source
    else:
        skill_path = (
            Path(out).expanduser().resolve()
            if out
            else source
        )
        if skill_path.name.lower() != "skill.md":
            raise ValueError("skill output must be named SKILL.md")
        agent_name = default_agent_name
        agent_path = skill_path.parent / agent_name

    effective_rappid = rappid
    if (
        effective_rappid is None
        and skill_path.is_file()
        and skill_path.resolve() != source.resolve()
    ):
        existing_compliant, existing_capsule = _is_rapp1_toast(
            core,
            skill_path.read_bytes(),
        )
        if existing_compliant and existing_capsule:
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
    if to == "agent" and not out:
        agent_path = skill_path.parent / agent_name
    artifacts = _write_artifacts(
        [(agent_path, agent_bytes), (skill_path, skill_bytes)],
        force=force,
        replace_source=source if skill_path == source else None,
    )
    return {
        "status": "ok",
        "source_format": "skill",
        "target_format": to,
        "default_format": "skill",
        "normalized_through_agent": True,
        "source_skill_vaulted": True,
        "rapp": _metadata_for(rci)["rapp"],
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
        rci = core.read_agent(raw, str(source))
        return {
            "status": "ok",
            "format": "agent",
            "rar_valid": _manifest_is_valid(manifest),
            "manifest": manifest.get("name"),
            "rappid": _rappid_from(rci, manifest, None),
            "sha256": _sha256(raw),
        }

    compliant, capsule = _is_rapp1_toast(core, raw)
    rci = core.read_skill(raw, str(source))
    metadata = _metadata_for(rci)
    return {
        "status": "ok",
        "format": "skill",
        "state": (
            "rapp1-toasted"
            if compliant
            else "legacy-toasted"
            if capsule
            else "raw"
        ),
        "default_format": "skill",
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
        )
        restored = core.write_agent(core.read_skill(skill_bytes, "SKILL.md"))
        return {
            "status": "ok",
            "format": "agent",
            "rar_valid": True,
            "manifest": manifest["name"],
            "agent_skill_agent_identical": restored == raw,
            "rapp": _metadata_for(rci)["rapp"],
        }

    compliant, _ = _is_rapp1_toast(core, raw)
    if not compliant:
        return {
            "status": "error",
            "format": "skill",
            "rapp1_toasted": False,
            "fix": (
                "run rapp-agent-converter/scripts/toast.py "
                f"{source}"
            ),
        }
    rci = core.read_skill(raw, str(source))
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
        "default_format": "skill",
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
    rci = core.read_skill(source.read_bytes(), str(source))
    raw, filename = _restore_source_skill(rci)
    target = (
        Path(out).expanduser().resolve()
        if out
        else source.with_name(filename)
    )
    artifacts = _write_artifacts([(target, raw)], force=force)
    return {
        "status": "ok",
        "restored": str(target),
        "sha256": _sha256(raw),
        "artifacts": artifacts,
    }


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
                            "inspect",
                            "verify",
                            "restore_raw",
                        ],
                        "description": (
                            "auto and convert emit a Toasted skill by default."
                        ),
                    },
                    "path": {
                        "type": "string",
                        "description": "RAR *_agent.py or SKILL.md input.",
                    },
                    "to": {
                        "type": "string",
                        "enum": ["skill", "agent"],
                        "description": "Target format. Defaults to skill.",
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
                },
                "required": ["path"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        operation = kwargs.get("operation") or "auto"
        path = kwargs.get("path")
        if not path:
            return _json({
                "status": "error",
                "message": "path is required",
                "default_format": "skill",
            })
        try:
            if operation in {"auto", "convert"}:
                result = convert_path(
                    str(path),
                    to=str(kwargs.get("to") or "skill"),
                    out=kwargs.get("out"),
                    publisher=kwargs.get("publisher"),
                    rappid=kwargs.get("rappid"),
                    force=bool(kwargs.get("force", False)),
                )
            elif operation == "inspect":
                result = inspect_path(str(path))
            elif operation == "verify":
                result = verify_path(str(path))
            elif operation == "restore_raw":
                result = restore_raw_skill(
                    str(path),
                    out=kwargs.get("out"),
                    force=bool(kwargs.get("force", False)),
                )
            else:
                result = {
                    "status": "error",
                    "message": f"unknown operation: {operation}",
                }
        except (OSError, RuntimeError, ValueError) as error:
            result = {
                "status": "error",
                "message": f"{type(error).__name__}: {error}",
                "default_format": "skill",
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

    convert = subparsers.add_parser("convert")
    convert.add_argument("path")
    convert.add_argument("--to", choices=("skill", "agent"), default="skill")
    convert.add_argument("-o", "--out")
    convert.add_argument("--publisher")
    convert.add_argument("--rappid")
    convert.add_argument("--force", action="store_true")

    inspect = subparsers.add_parser("inspect")
    inspect.add_argument("path")

    verify = subparsers.add_parser("verify")
    verify.add_argument("path")

    restore = subparsers.add_parser("restore-raw")
    restore.add_argument("path")
    restore.add_argument("-o", "--out")
    restore.add_argument("--force", action="store_true")
    return parser


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv == ["--tool"]:
        print(_json(RappAgentConverterAgent().to_tool()))
        return 0
    if not argv:
        print(RappAgentConverterAgent().perform())
        return 0
    if argv[0] not in {"convert", "inspect", "verify", "restore-raw"}:
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
            )
        elif args.command == "inspect":
            result = inspect_path(args.path)
        elif args.command == "verify":
            result = verify_path(args.path)
        else:
            result = restore_raw_skill(
                args.path,
                out=args.out,
                force=args.force,
            )
    except (OSError, RuntimeError, ValueError) as error:
        print(_json({
            "status": "error",
            "message": f"{type(error).__name__}: {error}",
            "default_format": "skill",
        }), file=sys.stderr)
        return 1
    print(_json(result))
    return 0 if result.get("status") == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
