#!/usr/bin/env python3
"""Build the additive Microsoft Scout projection of public RAR capabilities.

Canonical RAR agent bytes remain untouched. This script projects them into:

  scout/skills/<namespaced-skill>/SKILL.md  (Toasted, reversible)
  scout/skills/<namespaced-skill>/<agent>.py (byte-exact source)
  scout/skills/<namespaced-skill>/scripts/run_agent.py
  scout/skills/<namespaced-skill>/rapp/agent.lock.json
  scout/*.json                               (factory/rapplication workflows)

Scout's GitHub importer treats every root JSON file as an automation and scans
only the skills/ subdirectory for skills. Metadata therefore lives under
scout/meta/, never at the import root.
"""

from __future__ import annotations

import argparse
import ast
import base64
import gzip
import hashlib
import importlib.util
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "scout"
CONFIG_PATH = ROOT / "scout.config.json"
REGISTRY_PATH = ROOT / "registry.json"
FEDERATION_PATH = ROOT / "state" / "federation.json"
AGGREGATED_PATH = ROOT / "state" / "aggregated.json"
LIFECYCLE_PATH = ROOT / "state" / "agent_lifecycle.json"
SKILL_IDENTITIES_PATH = ROOT / "state" / "scout_skill_identities.json"
RUNNER_SOURCE = ROOT / "scripts" / "scout_run_agent.py"
FOUNDATION_AGENT = ROOT / "rapp_skill_agent.py"
FOUNDATION_SKILL = ROOT / "rapp_skills.md"
LEGACY_FOUNDATION_SKILL = ROOT / "rapp_skill.md"
CONVERTER_AGENT = ROOT / "scripts" / "rapp_agent_converter_agent.py"
CONVERTER_SKILL_NAME = "rapp-agent-converter"
CONVERTER_RAPPID = (
    "rappid:@rapp/rapp-agent-converter:"
    "11ce7bf2e7b301b3a35c919f34a60f9a25742552c9871ee33421d2de313e65fa"
)
CONVERTER_EMBED_MARKER = "__RAPP_TOASTER_EMBEDDED_GZIP_BASE64__"
CONVERTER_CLI = """#!/usr/bin/env python3
from run_agent import execute_agent_main

execute_agent_main()
"""

TOASTER_COMMIT = "d54ba8484b5c5dae6406d2090c03115d12985446"
TOASTER_URL = (
    "https://raw.githubusercontent.com/kody-w/rapp-toaster/"
    f"{TOASTER_COMMIT}/scripts/toast.py"
)
TOASTER_SHA256 = (
    "d340043178aa4160f76a179b8b1086971e09207b212aff2ab2c0752b69173e17"
)
INSTALLER_COMMIT = "5fbde1776a72715935c3d597a9ddfce28a04032b"
INSTALLER_BASE = (
    "https://raw.githubusercontent.com/kody-w/rapp-installer/"
    f"{INSTALLER_COMMIT}"
)
INSTALLERS = {
    "install.sh": (
        f"{INSTALLER_BASE}/install.sh",
        "cc586dd1752520d05fbff99a637eef308bb7051ffae457b7d037aa0574341794",
    ),
    "install.ps1": (
        f"{INSTALLER_BASE}/install.ps1",
        "747a5a8b2e6a41292a4b8b1a719fea588bdd21c523e3a3edb474dd651a8a2fda",
    ),
    "install.cmd": (
        f"{INSTALLER_BASE}/install.cmd",
        "9d4695f8ef7401d8098f2f0ed3bafddd916098d73892f0310f19c7729b514940",
    ),
}

WORKFLOW_SCHEMA = "rar-scout-workflow/1.0"
LOCK_SCHEMA = "rapp-grail-lock/2.0"
SKILL_IDENTITIES_SCHEMA = "rapp-scout-skill-identities/1.0"
DEFAULT_TIMESTAMP = "2000-01-01T00:00:00.000Z"
MAX_BUNDLE_SKILLS = 8
MAX_BUNDLE_BYTES = 2_000_000
RAW_BASE = "https://raw.githubusercontent.com/kody-w/RAR/main/scout"
TREE_BASE = "https://github.com/kody-w/RAR/tree/main/scout"
DEFAULT_SCHEDULE = {
    "kind": "single",
    "naturalLanguage": "every weekday at 9am",
    "days": [1, 2, 3, 4, 5],
    "time": {"hour": 9, "minute": 0},
    "hour": 9,
    "minute": 0,
}
RAPPID_RE = re.compile(
    r"^rappid:@[a-z0-9]+(?:-[a-z0-9]+)*/"
    r"[a-z0-9]+(?:-[a-z0-9]+)*:[0-9a-f]{64}$"
)


def _json(value):
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def _sha256(data):
    return hashlib.sha256(data).hexdigest()


def _stable_gzip(data):
    compressed = bytearray(gzip.compress(data, 9, mtime=0))
    if len(compressed) >= 10:
        compressed[9] = 255
    return bytes(compressed)


def _mint_skill_rappid(identity):
    owner, slug = identity.lstrip("@").split("/", 1)
    owner = _kebab(owner)
    slug = _kebab(slug.removesuffix("_agent"))
    tail = hashlib.sha256(
        b"rapp/1:rappid\n" + uuid.uuid4().bytes
    ).hexdigest()
    return f"rappid:@{owner}/{slug}:{tail}"


def _load_skill_identities():
    if not SKILL_IDENTITIES_PATH.exists():
        return {
            "schema": SKILL_IDENTITIES_SCHEMA,
            "entries": {},
        }
    value = _load_json(SKILL_IDENTITIES_PATH)
    if (
        value.get("schema") != SKILL_IDENTITIES_SCHEMA
        or not isinstance(value.get("entries"), dict)
    ):
        raise RuntimeError(
            f"{SKILL_IDENTITIES_PATH}: invalid skill identity ledger"
        )
    return value


def _manifest_rappid(raw):
    manifest = _source_manifest(raw)
    rapp = manifest.get("rapp")
    if rapp is None:
        return None
    if not isinstance(rapp, dict):
        raise RuntimeError(
            f"{manifest.get('name')}: invalid agent RAPP identity envelope"
        )
    if "schema" not in rapp and "rappid" not in rapp:
        return None
    if rapp.get("schema") != "rapp/1":
        raise RuntimeError(
            f"{manifest.get('name')}: unsupported agent RAPP identity envelope"
        )
    rappid = rapp.get("rappid")
    if not isinstance(rappid, str) or RAPPID_RE.fullmatch(rappid) is None:
        raise RuntimeError(f"{manifest.get('name')}: invalid agent RAPPID")
    return rappid


def _skill_rappid(ledger, identity, raw, mint_missing):
    entries = ledger["entries"]
    existing = entries.get(identity)
    existing_id = (
        existing.get("rappid")
        if isinstance(existing, dict)
        else None
    )
    authoritative = _manifest_rappid(raw)
    if (
        existing_id is not None
        and (
            not isinstance(existing_id, str)
            or RAPPID_RE.fullmatch(existing_id) is None
        )
    ):
        raise RuntimeError(f"{identity}: invalid committed skill RAPPID")
    if (
        authoritative is not None
        and existing_id is not None
        and authoritative != existing_id
    ):
        raise RuntimeError(
            f"{identity}: committed skill RAPPID conflicts with agent identity"
        )
    if existing_id is not None:
        return existing_id, False
    if not mint_missing and authoritative is None:
        raise RuntimeError(
            f"{identity}: missing committed skill RAPPID; "
            "run build_scout_exports.py --mint-skill-identities"
        )
    rappid = authoritative or _mint_skill_rappid(identity)
    entries[identity] = {
        "rappid": rappid,
        "source": (
            "agent-manifest"
            if authoritative is not None
            else "projection-genesis"
        ),
        "minted_at": datetime.now(timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
    }
    return rappid, True


def _lf(data):
    return data.replace(b"\r\n", b"\n")


def _kebab(value):
    return re.sub(r"[^a-z0-9]+", "-", str(value).lower()).strip("-")


def _safe_virtual_filename(path):
    name = path.name.removesuffix(".card").removesuffix(".stub")
    if not name.endswith(".py"):
        name += ".py"
    stem = name[:-3]
    if not stem.endswith("_agent"):
        stem += "_agent"
    return stem + ".py"


def _scout_skill_name(identity, prefix="rar"):
    owner, slug = identity.lstrip("@").split("/", 1)
    slug = slug.removesuffix("_agent")
    return f"{prefix}-{_kebab(owner)}-{_kebab(slug)}"


def _stable_workflow_id(identity):
    return _sha256(("rar-scout-workflow/1\n" + identity).encode("utf-8"))[:16]


def _iso_utc(value):
    if not value:
        return DEFAULT_TIMESTAMP
    text = str(value).strip()
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return DEFAULT_TIMESTAMP
    parsed = parsed.astimezone(timezone.utc)
    return parsed.strftime("%Y-%m-%dT%H:%M:%S.") + f"{parsed.microsecond // 1000:03d}Z"


def _load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def _load_literal(path, name):
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == name
        ):
            return ast.literal_eval(node.value)
    raise RuntimeError(f"{path}: missing literal {name}")


def _load_toaster():
    configured = os.environ.get("RAPP_TOASTER_PATH")
    if configured:
        source = Path(configured).expanduser().resolve()
        data = source.read_bytes()
    else:
        request = urllib.request.Request(
            TOASTER_URL,
            headers={"User-Agent": "rar-scout-export/1.0"},
        )
        try:
            data = urllib.request.urlopen(request, timeout=30).read()
        except urllib.error.URLError as error:
            raise RuntimeError(f"could not fetch pinned RAPP Toaster: {error}") from error
        temporary = tempfile.NamedTemporaryFile(
            "wb",
            prefix="rapp-toaster-",
            suffix=".py",
            delete=False,
        )
        with temporary:
            temporary.write(data)
        source = Path(temporary.name)

    actual = _sha256(data)
    if actual != TOASTER_SHA256:
        raise RuntimeError(
            "pinned RAPP Toaster failed SHA-256 verification "
            f"(expected {TOASTER_SHA256}, got {actual})"
        )

    spec = importlib.util.spec_from_file_location("_rar_scout_toaster", source)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load RAPP Toaster from {source}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module._rar_pinned_source_bytes = data
    return module


def _installer_bytes(filename):
    url, expected = INSTALLERS[filename]
    configured = os.environ.get("RAPP_INSTALLER_DIR")
    if configured:
        data = (Path(configured).expanduser().resolve() / filename).read_bytes()
    else:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "rar-scout-export/1.0"},
        )
        try:
            data = urllib.request.urlopen(request, timeout=30).read()
        except urllib.error.URLError as error:
            raise RuntimeError(
                f"could not fetch pinned {filename}: {error}"
            ) from error
    actual = _sha256(data)
    if actual != expected:
        raise RuntimeError(
            f"{filename}: installer hash mismatch {actual} != {expected}"
        )
    return data


def _source_manifest(data):
    tree = ast.parse(data.decode("utf-8"), filename="<agent>")
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "__manifest__"
                for target in node.targets
            )
        ):
            value = ast.literal_eval(node.value)
            return value if isinstance(value, dict) else {}
    return {}


def _resolve_registry_source(entry, source_path):
    """Return bytes matching the registry's notarized hash, never drifted bytes."""
    expected = entry.get("_sha256")
    if not expected:
        raise RuntimeError(f"{entry.get('name')}: registry has no _sha256")
    current = source_path.read_bytes()
    current_matches = _sha256(_lf(current)) == expected
    relative = source_path.relative_to(ROOT).as_posix()
    history = subprocess.run(
        ["git", "log", "--format=%H", "--", relative],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )
    if history.returncode != 0:
        raise RuntimeError(
            f"{entry.get('name')}: could not inspect git history for {relative}"
        )
    for commit in history.stdout.splitlines():
        shown = subprocess.run(
            ["git", "show", f"{commit}:{relative}"],
            cwd=ROOT,
            capture_output=True,
            timeout=60,
            check=False,
        )
        if shown.returncode == 0 and _sha256(_lf(shown.stdout)) == expected:
            return shown.stdout, commit
    if current_matches:
        return current, "working-tree"
    raise RuntimeError(
        f"{entry.get('name')}: no git blob matches notarized hash {expected}"
    )


def _normalized_identifier(value):
    return re.sub(r"[^a-z0-9]+", "", str(value).lower())


def _public_agent_contract(toaster, raw, manifest):
    """Select the public entrypoint in converged agents with inlined personas."""
    text = raw.decode("utf-8")
    tree = ast.parse(text, filename="<agent>")
    env = {}
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
        ):
            try:
                env[node.targets[0].id] = toaster._eval_node(node.value, env)
            except toaster._Unevaluable:
                pass

    candidates = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        if node.name == "BasicAgent" or node.name.startswith("_"):
            continue
        perform = next(
            (
                member
                for member in node.body
                if isinstance(member, ast.FunctionDef)
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
                    self_env[member.targets[0].id] = toaster._eval_node(
                        member.value,
                        self_env,
                    )
                except toaster._Unevaluable:
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
                            self_env[statement.targets[0].attr] = toaster._eval_node(
                                statement.value,
                                self_env,
                            )
                        except toaster._Unevaluable:
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


def _host_dependencies(source, manifest):
    dependencies = []
    try:
        tree = ast.parse(source, filename="<agent>")
    except SyntaxError:
        tree = None
    if tree is not None:
        stdlib = set(getattr(sys, "stdlib_module_names", ()))
        for statement in tree.body:
            modules = []
            if isinstance(statement, ast.Import):
                modules = [alias.name for alias in statement.names]
            elif (
                isinstance(statement, ast.ImportFrom)
                and statement.level == 0
                and statement.module
            ):
                modules = [statement.module]
            for module in modules:
                root = module.split(".", 1)[0]
                if module in {
                    "__future__",
                    "agents.basic_agent",
                    "basic_agent",
                }:
                    continue
                if module.startswith("agents."):
                    dependencies.append(f"agent:{module}")
                elif module.startswith("utils."):
                    dependencies.append(f"brainstem:{module}")
                elif root not in stdlib:
                    dependencies.append(f"python:{module}")
    for module in (
        "utils.azure_file_storage",
        "utils.storage_factory",
        "azure.functions",
    ):
        if re.search(rf"\b{re.escape(module)}\b", source):
            dependencies.append(f"brainstem:{module}")
    dependencies.extend(
        f"env:{name}" for name in manifest.get("requires_env", []) if name
    )
    return sorted(set(dependencies))


def _scout_instructions(identity, linked_name, original):
    preface = f"""## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `{identity}`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `{linked_name}` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{{}}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{{}}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

"""
    return preface + original.strip()


def _write_skill_bundle(
    destination,
    toaster,
    runner_template,
    *,
    identity,
    raw,
    virtual_filename,
    expected_sha256,
    scout_name,
    source_kind,
    rappid,
    source_commit=None,
    channel="native",
    platform_metadata=None,
):
    normalized = _lf(raw)
    actual = _sha256(normalized)
    if expected_sha256 and actual != expected_sha256:
        raise RuntimeError(
            f"{identity}: source hash mismatch {actual} != {expected_sha256}"
        )

    rci = toaster.read_agent(raw, virtual_filename)
    restored = toaster.restore(rci, "agent")
    if restored != raw:
        raise RuntimeError(f"{identity}: Toaster did not preserve source bytes")
    preserved_agent = rci["preserved"]["agent"]
    preserved_agent["bytes"] = len(raw)
    preserved_agent["gzip_bytes"] = len(
        base64.b64decode(preserved_agent["b64"])
    )
    manifest = _source_manifest(raw)
    public_contract = _public_agent_contract(toaster, raw, manifest)
    if public_contract:
        rci["name"] = public_contract["name"]
        rci["description"] = public_contract["description"]
        rci["parameters"] = public_contract["parameters"]
        rci["impl"] = {
            **(rci.get("impl") or {}),
            "class": public_contract["class_name"],
            "perform": public_contract["perform"],
        }

    rci["slug"] = scout_name
    platform = dict(rci.get("platform") or {})
    metadata = dict(platform.get("metadata") or {})
    metadata.update({
        "projection": "rar-scout/1.0",
        "rar_agent": identity,
        "rar_sha256": actual,
        "source_kind": source_kind,
        "source_commit": source_commit,
        "default_artifact": "skill",
        "canonical_format": "skill",
        "grail_record": True,
        "materializes": ["agent"],
        "backup_agent": virtual_filename,
        "rollback_agent_retained": True,
        "rapp": {
            "schema": "rapp/1",
            "rappid": rappid,
            "kind": "skill",
        },
    })
    metadata.update(platform_metadata or {})
    platform["metadata"] = metadata
    rci["platform"] = platform
    rci["instructions"] = _scout_instructions(
        identity,
        virtual_filename,
        rci.get("instructions") or rci.get("description") or "",
    )

    skill_bytes = toaster.write_skill(rci)
    skill_dir = destination / "skills" / scout_name
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_bytes(skill_bytes)
    (skill_dir / virtual_filename).write_bytes(raw)

    source_text = raw.decode("utf-8")
    lock = {
        "schema": LOCK_SCHEMA,
        "primary_artifact": "skill",
        "grail_file": "SKILL.md",
        "rappid": rappid,
        "backup_agent": virtual_filename,
        "rollback_agent_retained": True,
        "materializes": ["agent"],
        "agent": identity,
        "version": str(manifest.get("version") or rci.get("version") or "0.0.0"),
        "agent_file": virtual_filename,
        "agent_sha256": actual,
        "skill_sha256": _sha256(skill_bytes),
        "agent_bytes": len(raw),
        "skill_bytes": len(skill_bytes),
        "digest_algorithm": "sha256-lf-v1",
        "manifest": manifest,
        "tool_schema": rci.get("parameters") or {
            "type": "object",
            "properties": {},
        },
        "host_dependencies": _host_dependencies(source_text, manifest),
        "runtime_name": rci.get("name"),
        "entry_class": (
            public_contract["class_name"]
            if public_contract
            else (rci.get("impl") or {}).get("class")
        ),
    }
    lock_dir = skill_dir / "rapp"
    lock_dir.mkdir()
    (lock_dir / "agent.lock.json").write_text(
        _json(lock),
        encoding="utf-8",
        newline="\n",
    )
    scripts_dir = skill_dir / "scripts"
    scripts_dir.mkdir()
    runner = scripts_dir / "run_agent.py"
    runner.write_text(runner_template, encoding="utf-8", newline="\n")
    runner.chmod(runner.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    example_call = manifest.get("example_call")
    example_args = (
        example_call.get("args") or {}
        if isinstance(example_call, dict)
        else {}
    )
    return {
        "identity": identity,
        "skill_name": scout_name,
        "source_kind": source_kind,
        "source_commit": source_commit,
        "source_sha256": actual,
        "skill_sha256": _sha256(skill_bytes),
        "linked_agent": virtual_filename,
        "default_artifact": "skill",
        "grail_record": "SKILL.md",
        "backup_agent": virtual_filename,
        "rollback_agent_retained": True,
        "materializes": ["agent"],
        "rappid": rappid,
        "requires_env": manifest.get("requires_env", []),
        "description": rci.get("description") or "",
        "parameters": rci.get("parameters") or {},
        "example_args": example_args,
        "version": str(manifest.get("version") or rci.get("version") or "0.0.0"),
        "channel": channel,
        "_skill_dir": str(skill_dir),
    }


def _install_converter_runtime(record):
    skill_dir = Path(record["_skill_dir"])
    scripts_dir = skill_dir / "scripts"
    cli = scripts_dir / "toast.py"
    cli.write_text(CONVERTER_CLI, encoding="utf-8", newline="\n")
    cli.chmod(cli.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def _bundled_converter_agent(toaster):
    source = CONVERTER_AGENT.read_text(encoding="utf-8")
    if source.count(CONVERTER_EMBED_MARKER) != 1:
        raise RuntimeError("converter source has the wrong embed marker count")
    core = getattr(toaster, "_rar_pinned_source_bytes", None)
    if not isinstance(core, bytes) or _sha256(core) != TOASTER_SHA256:
        raise RuntimeError("pinned RAPP Toaster source bytes are unavailable")
    payload = base64.b64encode(_stable_gzip(core)).decode("ascii")
    bundled = source.replace(CONVERTER_EMBED_MARKER, payload)
    compile(bundled, "rapp_agent_converter_agent.py", "exec")
    return bundled.encode("utf-8")


def _is_workflow_capability(entry):
    tags = {_kebab(tag) for tag in entry.get("tags", [])}
    stem = Path(entry.get("_file") or "").name.lower()
    name = str(entry.get("name") or "").lower()
    return (
        "rapplication" in tags
        or "factory" in stem
        or "factory" in name
        or any("factory" in tag for tag in tags)
    )


def _skill_channel(identity):
    if identity.startswith("@cat-agent-skills/"):
        return "powercat"
    if identity.startswith("@cowork-cookbook/"):
        return "cowork-cookbook"
    return "native"


def _workflow_prompt(record, example_args):
    args_text = json.dumps(example_args or {}, indent=2, sort_keys=True)
    return (
        f"Use the imported Scout skill `{record['skill_name']}`. "
        f"It is the reversible Toasted projection of `{record['identity']}`.\n\n"
        "Run its checksum-verified `scripts/run_agent.py`; do not recreate or "
        "paraphrase the Python behavior. Use these starting arguments:\n\n"
        f"```json\n{args_text}\n```\n\n"
        "If a value is still a placeholder or a required input is missing, "
        "stop and report the exact missing field instead of inventing data. "
        "Return only the canonical agent result."
    )


def _workflow_json(record, source_entry, lifecycle, override=None):
    override = override or {}
    identity = record["identity"]
    lifecycle_entry = lifecycle.get(identity) or {}
    created_at = _iso_utc(
        source_entry.get("_added_at")
        or source_entry.get("added_at")
        or lifecycle_entry.get("created_at")
    )
    updated_at = _iso_utc(
        lifecycle_entry.get("updated_at")
        or source_entry.get("_added_at")
        or source_entry.get("added_at")
    )
    example_args = override.get("example_args", record.get("example_args") or {})
    display = (
        override.get("name")
        or source_entry.get("display_name")
        or source_entry.get("name")
        or identity
    )
    return {
        "schedule": DEFAULT_SCHEDULE,
        "id": _stable_workflow_id(identity),
        "name": str(display),
        "description": (
            f"Disabled Scout workflow projected from {identity} "
            f"({record['version']}). Edit inputs or schedule before enabling."
        ),
        "steps": [{
            "id": "1",
            "label": f"Run {record['skill_name']}",
            "prompt": _workflow_prompt(record, example_args),
        }],
        "enabled": False,
        "createdAt": created_at,
        "updatedAt": updated_at,
        "triggerType": "schedule",
        "lastExecutedAt": None,
        "skillNames": [record["skill_name"]],
        "teamsNotify": "auto",
        "rapp": {
            "schema": "rapp/1",
            "skill_name": record["skill_name"],
            "default_artifact": "skill",
            "grail_record": "SKILL.md",
            "backup_agent": record["backup_agent"],
        },
    }


def _render_root_foundation(toaster):
    raw = FOUNDATION_AGENT.read_bytes()
    legacy_rci = toaster.read_agent(raw, FOUNDATION_AGENT.name)
    legacy_skill = toaster.write_skill(legacy_rci)
    if toaster.restore(legacy_rci, "agent") != raw:
        raise RuntimeError("rapp_skill.md did not preserve rapp_skill_agent.py")

    plural_rci = toaster.read_agent(raw, FOUNDATION_AGENT.name)
    plural_rci["slug"] = "rapp-skills"
    platform = dict(plural_rci.get("platform") or {})
    metadata = dict(platform.get("metadata") or {})
    metadata.update({
        "projection": "rapp-capability-interchange/1.0",
        "canonical_agent": FOUNDATION_AGENT.name,
    })
    platform["metadata"] = metadata
    plural_rci["platform"] = platform
    plural_skill = toaster.write_skill(plural_rci)
    if toaster.restore(plural_rci, "agent") != raw:
        raise RuntimeError("rapp_skills.md did not preserve rapp_skill_agent.py")
    return legacy_skill, plural_skill


def _fetch_federated(entry):
    request = urllib.request.Request(
        entry["singleton_url"],
        headers={"User-Agent": "rar-scout-export/1.0"},
    )
    try:
        raw = urllib.request.urlopen(request, timeout=30).read()
    except urllib.error.URLError as error:
        raise RuntimeError(f"{entry['id']}: fetch failed: {error}") from error
    actual = _sha256(_lf(raw))
    expected = entry.get("singleton_sha256")
    if actual != expected:
        raise RuntimeError(
            f"{entry['id']}: singleton hash mismatch {actual} != {expected}"
        )
    return raw


def _compare_trees(expected, actual):
    def comparable(path):
        return "__pycache__" not in path.parts and path.suffix != ".pyc"

    expected_files = {
        path.relative_to(expected): path
        for path in expected.rglob("*")
        if path.is_file() and comparable(path)
    }
    actual_files = {
        path.relative_to(actual): path
        for path in actual.rglob("*")
        if path.is_file() and comparable(path)
    } if actual.exists() else {}
    differences = []
    for relative in sorted(set(expected_files) | set(actual_files)):
        if relative not in expected_files:
            differences.append(f"extra: {relative}")
        elif relative not in actual_files:
            differences.append(f"missing: {relative}")
        elif expected_files[relative].read_bytes() != actual_files[relative].read_bytes():
            differences.append(f"changed: {relative}")
    return differences


def _directory_size(path):
    return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())


def _copy_skill(record, destination):
    source = Path(record["_skill_dir"])
    target = destination / "skills" / record["skill_name"]
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)
    return target


def _catalog_files(skill_dir, scout_relative):
    files = []
    for path in sorted(item for item in skill_dir.rglob("*") if item.is_file()):
        relative = path.relative_to(skill_dir).as_posix()
        published = f"{scout_relative}/{relative}"
        files.append({
            "path": relative,
            "sha256": _sha256(path.read_bytes()),
            "url": f"{RAW_BASE}/{published}",
        })
    return files


def _publish_skill_bundles(staging, records):
    bundles = []
    starters = [
        record for record in records if record["channel"] == "starter"
    ]
    foundation = next(
        record for record in starters if record["skill_name"] == "rapp-skills"
    )
    starter = staging / "starter"
    starter_dirs = {
        record["skill_name"]: _copy_skill(record, starter)
        for record in starters
    }
    foundation_dir = starter_dirs[foundation["skill_name"]]
    installer_dir = foundation_dir / "installer"
    installer_dir.mkdir()
    for filename in sorted(INSTALLERS):
        path = installer_dir / filename
        path.write_bytes(_installer_bytes(filename))
        if filename.endswith(".sh"):
            path.chmod(0o755)
    for record in starters:
        skill_dir = starter_dirs[record["skill_name"]]
        relative = f"starter/skills/{record['skill_name']}"
        record["bundle"] = "starter"
        record["import_url"] = f"{TREE_BASE}/starter"
        record["files"] = _catalog_files(skill_dir, relative)
    bundles.append({
        "id": "starter",
        "channel": "starter",
        "import_url": f"{TREE_BASE}/starter",
        "skills": [record["skill_name"] for record in starters],
        "files": sum(len(record["files"]) for record in starters),
        "bytes": _directory_size(starter / "skills"),
    })
    (starter / "README.md").write_text(
        "# RAPP Scout starter\n\n"
        "Import this directory in Microsoft Scout to install the Toasted "
        "`rapp-skills` manager, Brainstem bridge, and the RAPP/1 "
        "`rapp-agent-converter`. Toasted `SKILL.md` is the persistent Grail "
        "record; `agent.py` is generated only when selected or hotloaded. "
        "Use `scripts/toast.py config --default-format agent` to flip the "
        "global materialization without changing the canonical record.\n",
        encoding="utf-8",
        newline="\n",
    )
    plugin_dir = starter / ".claude-plugin"
    plugin_dir.mkdir()
    (plugin_dir / "plugin.json").write_text(
        _json({
            "name": "rapp",
            "version": foundation["version"],
            "description": (
                "RAR catalog, RAPP/1 Toasted Grail records, global skill or "
                "agent materialization, format-agnostic Brainstem hotload, "
                "manual exports, and a pinned local RAPP Brainstem bootstrap."
            ),
            "author": {
                "name": "RAPP Agent Registry",
                "url": "https://github.com/kody-w/RAR",
            },
            "homepage": "https://kody-w.github.io/RAR/",
            "repository": "https://github.com/kody-w/RAR",
            "license": "MIT",
            "keywords": [
                "rapp",
                "rar",
                "brainstem",
                "scout",
                "copilot-cli",
                "agent-skills",
            ],
        }),
        encoding="utf-8",
        newline="\n",
    )

    by_channel = {}
    for record in records:
        if record["channel"] == "starter":
            continue
        by_channel.setdefault(record["channel"], []).append(record)

    for channel in sorted(by_channel):
        groups = []
        current = []
        current_bytes = 0
        for record in sorted(
            by_channel[channel],
            key=lambda item: item["skill_name"],
        ):
            size = _directory_size(Path(record["_skill_dir"]))
            if current and (
                len(current) >= MAX_BUNDLE_SKILLS
                or current_bytes + size > MAX_BUNDLE_BYTES
            ):
                groups.append(current)
                current = []
                current_bytes = 0
            current.append(record)
            current_bytes += size
        if current:
            groups.append(current)

        for index, group in enumerate(groups, 1):
            bundle_id = f"{channel}-{index:02d}"
            root = staging / "bundles" / bundle_id
            total_bytes = 0
            total_files = 0
            for record in group:
                copied = _copy_skill(record, root)
                relative = (
                    f"bundles/{bundle_id}/skills/"
                    f"{record['skill_name']}"
                )
                record["bundle"] = bundle_id
                record["import_url"] = (
                    f"{TREE_BASE}/bundles/{bundle_id}"
                )
                record["files"] = _catalog_files(copied, relative)
                total_bytes += _directory_size(copied)
                total_files += len(record["files"])
            (root / "README.md").write_text(
                f"# RAR Scout bundle: {bundle_id}\n\n"
                f"Channel: `{channel}`. Skills: {len(group)}. "
                "Import this directory in Microsoft Scout.\n",
                encoding="utf-8",
                newline="\n",
            )
            bundles.append({
                "id": bundle_id,
                "channel": channel,
                "import_url": f"{TREE_BASE}/bundles/{bundle_id}",
                "skills": [
                    record["skill_name"] for record in group
                ],
                "files": total_files,
                "bytes": total_bytes,
            })
    return bundles


def _publish_workflow_bundles(staging, pending_workflows):
    published = []
    for record, workflow in sorted(
        pending_workflows,
        key=lambda item: item[0]["skill_name"],
    ):
        bundle_id = record["skill_name"]
        root = staging / "workflows" / bundle_id
        root.mkdir(parents=True)
        filename = f"workflow--{bundle_id}.json"
        (root / filename).write_text(
            _json(workflow),
            encoding="utf-8",
            newline="\n",
        )
        _copy_skill(record, root)
        (root / "README.md").write_text(
            f"# Scout workflow: {workflow['name']}\n\n"
            "This import directory contains exactly one disabled workflow "
            "and its one reversible Toasted companion skill.\n",
            encoding="utf-8",
            newline="\n",
        )
        grail_url = next(
            (
                item["url"]
                for item in record.get("files", [])
                if item.get("path") == "SKILL.md"
            ),
            None,
        )
        published.append({
            "identity": record["identity"],
            "file": filename,
            "id": workflow["id"],
            "skill_name": record["skill_name"],
            "import_url": f"{TREE_BASE}/workflows/{bundle_id}",
            "rappid": record["rappid"],
            "default_artifact": "skill",
            "grail_record": "SKILL.md",
            "grail_url": grail_url,
            "backup_agent": record["backup_agent"],
        })
    return published


def build(check=False, mint_skill_identities=False):
    config = _load_json(CONFIG_PATH)
    registry = _load_json(REGISTRY_PATH).get("agents", [])
    federation = _load_json(FEDERATION_PATH).get("rapplications", [])
    aggregated = _load_json(AGGREGATED_PATH).get("items", [])
    lifecycle = _load_json(LIFECYCLE_PATH)
    toaster = _load_toaster()
    runner_template = RUNNER_SOURCE.read_text(encoding="utf-8")
    overrides = config.get("workflow_overrides") or {}
    skill_identities = _load_skill_identities()
    identities_changed = False

    def skill_rappid(identity, raw):
        nonlocal identities_changed
        value, changed = _skill_rappid(
            skill_identities,
            identity,
            raw,
            mint_skill_identities,
        )
        identities_changed = identities_changed or changed
        return value

    with tempfile.TemporaryDirectory(prefix=".scout-build-", dir=ROOT) as temp:
        staging = Path(temp) / "scout"
        pool = Path(temp) / "pool"
        (pool / "skills").mkdir(parents=True)
        records = []
        pending_workflows = []
        skipped = []

        legacy_foundation_skill, foundation_skill = _render_root_foundation(
            toaster
        )
        foundation_raw = FOUNDATION_AGENT.read_bytes()
        foundation = _write_skill_bundle(
            pool,
            toaster,
            runner_template,
            identity="@kody-w/rapp_skill_agent",
            raw=foundation_raw,
            virtual_filename=FOUNDATION_AGENT.name,
            expected_sha256=_sha256(_lf(foundation_raw)),
            scout_name="rapp-skills",
            source_kind="foundation",
            rappid=skill_rappid("@kody-w/rapp_skill_agent", foundation_raw),
            source_commit=None,
            channel="starter",
        )
        records.append(foundation)
        converter_agent = _bundled_converter_agent(toaster)
        converter = _write_skill_bundle(
            pool,
            toaster,
            runner_template,
            identity="@rapp/rapp_agent_converter",
            raw=converter_agent,
            virtual_filename="rapp_agent_converter_agent.py",
            expected_sha256=_sha256(_lf(converter_agent)),
            scout_name=CONVERTER_SKILL_NAME,
            source_kind="foundation",
            rappid=skill_rappid(
                "@rapp/rapp_agent_converter",
                converter_agent,
            ),
            source_commit=None,
            channel="starter",
            platform_metadata={
                "default_format": "skill",
                "canonical_format": "skill",
                "grail_record": True,
                "materializes": ["agent"],
                "toasted": True,
                "canonical_agent": "rapp_agent_converter_agent.py",
                "normalization_path": (
                    "raw-skill->rar-agent->toasted-skill"
                ),
                "rapp": {
                    "schema": "rapp/1",
                    "rappid": CONVERTER_RAPPID,
                    "kind": "skill",
                },
                "reader_versions": ["raw-skill", "rci/1", "rapp/1"],
                "writer_version": "rapp/1",
            },
        )
        _install_converter_runtime(converter)
        records.append(converter)

        if config.get("include_registry_agents", True):
            for entry in sorted(registry, key=lambda item: item.get("name", "")):
                identity = entry.get("name")
                source_path = ROOT / str(entry.get("_file") or "")
                if identity == "@rapp/basic_agent":
                    skipped.append({
                        "identity": identity,
                        "reason": "infrastructure base class, not a callable agent",
                    })
                    continue
                if source_path.name.endswith(".stub"):
                    skipped.append({
                        "identity": identity,
                        "reason": "gated stub has no public executable bytes",
                    })
                    continue
                if not identity or not source_path.is_file():
                    raise RuntimeError(f"registry source missing: {identity} {source_path}")
                raw, source_commit = _resolve_registry_source(entry, source_path)
                record = _write_skill_bundle(
                    pool,
                    toaster,
                    runner_template,
                    identity=identity,
                    raw=raw,
                    virtual_filename=_safe_virtual_filename(source_path),
                    expected_sha256=entry.get("_sha256"),
                    scout_name=_scout_skill_name(identity),
                    source_kind="rar-agent",
                    rappid=skill_rappid(identity, raw),
                    source_commit=source_commit,
                    channel=_skill_channel(identity),
                )
                records.append(record)
                if _is_workflow_capability(entry):
                    workflow = _workflow_json(
                        record,
                        entry,
                        lifecycle,
                        overrides.get(identity),
                    )
                    pending_workflows.append((record, workflow))

            registry_names = {
                entry.get("name") for entry in registry
            }
            for item in aggregated:
                reference = str(item.get("ref") or "").strip()
                if (
                    reference.startswith("@cat-agent-skills/")
                    and reference not in registry_names
                ):
                    skipped.append({
                        "identity": reference,
                        "aggregate_id": item.get("source_slug"),
                        "reason": (
                            "aggregated PowerCAT entry has no notarized RAR "
                            "container agent to Toast reversibly"
                        ),
                    })

        if config.get("include_federated_rapplications", True):
            excluded_federation = config.get("exclude_federation") or {}
            for entry in sorted(federation, key=lambda item: item.get("id", "")):
                identity = str(entry.get("manifest_name") or "").strip()
                if entry.get("id") in excluded_federation:
                    skipped.append({
                        "identity": identity or entry.get("id"),
                        "federation_id": entry.get("id"),
                        "reason": excluded_federation[entry["id"]],
                    })
                    continue
                if entry.get("access") != "public":
                    skipped.append({
                        "identity": identity or entry.get("id"),
                        "federation_id": entry.get("id"),
                        "reason": "federated rapplication is not public",
                    })
                    continue
                raw = _fetch_federated(entry)
                source_manifest = _source_manifest(raw)
                identity = identity or str(
                    source_manifest.get("name") or ""
                ).strip()
                if not identity.startswith("@") or "/" not in identity:
                    identity = f"@rapp-store/{_kebab(entry.get('id') or 'rapplication')}"
                record = _write_skill_bundle(
                    pool,
                    toaster,
                    runner_template,
                    identity=identity,
                    raw=raw,
                    virtual_filename=_safe_virtual_filename(
                        Path(urllib.parse.urlsplit(entry["singleton_url"]).path)
                    ),
                    expected_sha256=entry.get("singleton_sha256"),
                    scout_name=_scout_skill_name(identity, prefix="rappstore"),
                    source_kind="federated-rapplication",
                    rappid=skill_rappid(identity, raw),
                    source_commit=None,
                    channel="rapplications",
                )
                record["federation_id"] = entry.get("id")
                records.append(record)
                source_entry = {
                    "name": entry.get("name"),
                    "display_name": entry.get("name"),
                    "version": entry.get("version"),
                    "tags": entry.get("tags") or ["rapplication"],
                }
                workflow = _workflow_json(
                    record,
                    source_entry,
                    lifecycle,
                    overrides.get(identity),
                )
                pending_workflows.append((record, workflow))

        if identities_changed:
            if check:
                raise RuntimeError(
                    "skill identity ledger would change during --check"
                )
            SKILL_IDENTITIES_PATH.write_text(
                _json(skill_identities),
                encoding="utf-8",
                newline="\n",
            )

        skill_names = [record["skill_name"] for record in records]
        if len(skill_names) != len(set(skill_names)):
            raise RuntimeError("generated Scout skill names are not unique")
        bundles = _publish_skill_bundles(staging, records)
        workflows = _publish_workflow_bundles(
            staging,
            pending_workflows,
        )
        workflow_ids = [workflow["id"] for workflow in workflows]
        if len(workflow_ids) != len(set(workflow_ids)):
            raise RuntimeError("generated Scout workflow IDs are not unique")

        public_records = []
        for record in records:
            public_records.append({
                key: value
                for key, value in record.items()
                if not key.startswith("_")
            })

        catalog = staging / "catalog"
        catalog.mkdir()
        (catalog / "catalog.json").write_text(
            _json({
                "schema": "rar-scout-catalog/1.0",
                "toaster": {
                    "commit": TOASTER_COMMIT,
                    "sha256": TOASTER_SHA256,
                },
                "skills": sorted(
                    public_records,
                    key=lambda item: item["skill_name"],
                ),
                "bundles": sorted(
                    bundles,
                    key=lambda item: item["id"],
                ),
                "workflows": sorted(workflows, key=lambda item: item["file"]),
                "skipped": sorted(
                    skipped,
                    key=lambda item: str(item.get("identity") or ""),
                ),
            }),
            encoding="utf-8",
            newline="\n",
        )
        (catalog / "README.md").write_text(
            "# RAR Scout catalog\n\n"
            "The machine catalog is `catalog.json`. Each `import_url` points "
            "to a bounded Scout-compatible directory.\n",
            encoding="utf-8",
            newline="\n",
        )
        (staging / "README.md").write_text(
            "# RAR skills and workflows for Microsoft Scout\n\n"
            "Copilot plugin install:\n\n"
            "```text\n"
            "copilot plugin marketplace add kody-w/RAR\n"
            "copilot plugin install rapp@rar\n"
            "```\n\n"
            "Start with the Toasted RAPP skill manager and Grail converter:\n\n"
            "```text\n"
            "https://github.com/kody-w/RAR/tree/main/scout/starter\n"
            "```\n\n"
            "The starter keeps Toasted `SKILL.md` as the persistent Grail "
            "record, materializes `agent.py` deterministically when selected, "
            "and lets Brainstem hotload raw skills, Toasted skills, or agents "
            "through one converter. The manager hotloads verified skills into "
            "`~/.copilot/skills`, which Microsoft Scout can read in place. "
            "Bounded GitHub-import "
            "shards live under `bundles/`; each factory or rapplication "
            "workflow has an isolated directory under `workflows/` containing "
            "only that workflow and its companion skill. See "
            "`catalog/catalog.json` for every import URL.\n\n"
            f"Generated: {len(records)} reversible Toasted skill(s), "
            f"{len(bundles)} bounded skill bundle(s), and {len(workflows)} "
            "disabled workflow template(s). Canonical RAR agent bytes remain "
            "under `agents/`; `scout/` is removable compatibility output.\n",
            encoding="utf-8",
            newline="\n",
        )

        if check:
            differences = _compare_trees(staging, OUTPUT)
            root_expected = foundation_skill
            if not FOUNDATION_SKILL.exists():
                differences.append("missing: rapp_skills.md")
            elif FOUNDATION_SKILL.read_bytes() != root_expected:
                differences.append("changed: rapp_skills.md")
            if not LEGACY_FOUNDATION_SKILL.exists():
                differences.append("missing: rapp_skill.md")
            elif LEGACY_FOUNDATION_SKILL.read_bytes() != legacy_foundation_skill:
                differences.append("changed: rapp_skill.md")
            if differences:
                print("Scout export drift:")
                for difference in differences[:100]:
                    print("  " + difference)
                if len(differences) > 100:
                    print(f"  ... {len(differences) - 100} more")
                return 1
            print(
                f"Scout export is current: {len(records)} skills, "
                f"{len(workflows)} workflows, {len(skipped)} skipped"
            )
            return 0

        if OUTPUT.exists():
            shutil.rmtree(OUTPUT)
        shutil.copytree(staging, OUTPUT)
        FOUNDATION_SKILL.write_bytes(foundation_skill)
        LEGACY_FOUNDATION_SKILL.write_bytes(legacy_foundation_skill)
        print(
            f"Built Scout export: {len(records)} skills, "
            f"{len(workflows)} workflows, {len(skipped)} skipped"
        )
        return 0


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="compare generated output without modifying scout/",
    )
    parser.add_argument(
        "--mint-skill-identities",
        action="store_true",
        help="mint and persist missing RAPP/1 identities for Toasted skills",
    )
    args = parser.parse_args(argv)
    return build(
        check=args.check,
        mint_skill_identities=args.mint_skill_identities,
    )


if __name__ == "__main__":
    raise SystemExit(main())
