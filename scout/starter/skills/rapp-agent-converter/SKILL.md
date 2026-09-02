---
name: "rapp-agent-converter"
description: "Converts RAR agent.py files and SKILL.md files in both directions, automatically normalizing every raw skill through a valid RAR agent and emitting a RAPP/1 Toasted SKILL.md by default."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp_agent_converter", "rar_sha256": "c5f83f431afd25221a7227dbac5dd05f7f1afe1463e5f665c94062137d9a8f8c", "source_kind": "foundation", "source_commit": null, "default_format": "skill", "toasted": true, "canonical_agent": "rapp_agent_converter_agent.py", "normalization_path": "raw-skill->rar-agent->toasted-skill", "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/rapp-agent-converter:11ce7bf2e7b301b3a35c919f34a60f9a25742552c9871ee33421d2de313e65fa", "kind": "skill"}, "author": "RAPP Agent Registry", "tags": ["rapp", "rapp-1", "rar", "skills", "toasted", "conversion", "fidelity", "local-first"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/rapp_agent_converter`. The original RAPP
agent is preserved byte-for-byte in `rapp_agent_converter_agent.py` and in the RCI capsule.

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

RAPP Agent Converter - make agent.py and SKILL.md interchangeable.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "additionalProperties": false,
  "properties": {
    "force": {
      "description": "Replace a conflicting output file.",
      "type": "boolean"
    },
    "operation": {
      "description": "auto and convert emit a Toasted skill by default.",
      "enum": [
        "auto",
        "convert",
        "inspect",
        "verify",
        "restore_raw"
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
      "description": "Target format. Defaults to skill.",
      "enum": [
        "skill",
        "agent"
      ],
      "type": "string"
    }
  },
  "required": [
    "path"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_agent_converter_agent.py` and embedded as the fenced Python below (sha256 c5f83f431afd2522…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_agent_converter_agent.py` first:

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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
