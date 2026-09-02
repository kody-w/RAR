#!/usr/bin/env python3
"""Checksum-pinned runner copied into every generated RAR Scout skill."""

from __future__ import annotations

import asyncio
import base64
import hashlib
import importlib.abc
import importlib.util
import inspect
import json
import linecache
import os
import re
import sys
import tempfile
import types
import zlib
from pathlib import Path


sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LOCK_PATH = ROOT / "rapp" / "agent.lock.json"
SKILL_PATH = ROOT / "SKILL.md"
CAPSULE = re.compile(
    r"<!--\s*rci-capsule:v1:([A-Za-z0-9+/=]+)\s*-->"
)
RAPPID = re.compile(
    r"^rappid:@[a-z0-9]+(?:-[a-z0-9]+)*/"
    r"[a-z0-9]+(?:-[a-z0-9]+)*:[0-9a-f]{64}$"
)
MAX_SKILL_BYTES = 16 * 1024 * 1024
MAX_CAPSULE_B64 = 16 * 1024 * 1024
MAX_CAPSULE_JSON_BYTES = 64 * 1024 * 1024
MAX_AGENT_BYTES = 32 * 1024 * 1024


def fail(code, message):
    print(message, file=sys.stderr)
    raise SystemExit(code)


def load_lock():
    try:
        lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        fail(6, f"RAPP_UNAVAILABLE:bundle-unreadable ({error})")
    required = {
        "agent",
        "agent_file",
        "agent_sha256",
        "entry_class",
        "tool_schema",
    }
    missing = sorted(required - set(lock))
    if missing:
        fail(6, "RAPP_UNAVAILABLE:lock-missing-" + ",".join(missing))
    schema = lock.get("schema")
    if schema not in {"rapp-agent-lock/1.0", "rapp-grail-lock/2.0"}:
        fail(6, f"RAPP_UNAVAILABLE:lock-schema-unsupported ({schema})")
    if schema == "rapp-grail-lock/2.0":
        grail_required = {
            "primary_artifact",
            "grail_file",
            "rappid",
            "backup_agent",
            "rollback_agent_retained",
            "materializes",
            "skill_sha256",
            "agent_bytes",
            "skill_bytes",
        }
        missing = sorted(grail_required - set(lock))
        if missing:
            fail(6, "RAPP_UNAVAILABLE:grail-lock-missing-" + ",".join(missing))
        if (
            lock["primary_artifact"] != "skill"
            or lock["grail_file"] != "SKILL.md"
            or lock["backup_agent"] != lock["agent_file"]
            or lock["materializes"] != ["agent"]
            or RAPPID.fullmatch(str(lock["rappid"])) is None
            or not isinstance(lock["agent_bytes"], int)
            or not isinstance(lock["skill_bytes"], int)
            or lock["agent_bytes"] < 0
            or lock["skill_bytes"] < 0
        ):
            fail(6, "RAPP_UNAVAILABLE:grail-lock-contract-invalid")
    return lock


def agent_path(lock):
    relative = Path(str(lock.get("backup_agent") or lock["agent_file"]))
    candidate = (ROOT / relative).resolve()
    if (
        relative.is_absolute()
        or ".." in relative.parts
        or ROOT != candidate
        and ROOT not in candidate.parents
    ):
        fail(6, "RAPP_UNAVAILABLE:agent-path-escapes-bundle")
    return candidate


def verify_bytes(lock, source):
    actual = hashlib.sha256(
        source.replace(b"\r\n", b"\n")
    ).hexdigest()
    expected = str(lock["agent_sha256"])
    if actual != expected:
        fail(
            3,
            "RAPP_UNAVAILABLE:integrity-mismatch "
            f"expected={expected[:12]} actual={actual[:12]}",
        )


def _bounded_gzip(data, limit, label):
    decompressor = zlib.decompressobj(16 + zlib.MAX_WBITS)
    output = decompressor.decompress(data, limit + 1)
    if len(output) > limit or decompressor.unconsumed_tail:
        fail(6, f"RAPP_UNAVAILABLE:{label}-too-large")
    output += decompressor.flush()
    if len(output) > limit:
        fail(6, f"RAPP_UNAVAILABLE:{label}-too-large")
    if not decompressor.eof or decompressor.unused_data:
        fail(6, f"RAPP_UNAVAILABLE:{label}-invalid-gzip")
    return output


def _active_capsule_payload(text):
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
        for match in CAPSULE.finditer(line):
            matches.append((match.group(1), offset + match.end()))
        offset += len(line)
    if len(matches) != 1:
        fail(6, "RAPP_UNAVAILABLE:skill-capsule-ambiguous")
    payload, end = matches[0]
    if text[end:].strip():
        fail(6, "RAPP_UNAVAILABLE:skill-capsule-not-terminal")
    return payload


def _verified_skill(lock):
    try:
        if SKILL_PATH.stat().st_size > MAX_SKILL_BYTES:
            fail(6, "RAPP_UNAVAILABLE:skill-too-large")
        skill = SKILL_PATH.read_bytes()
    except OSError as error:
        fail(6, f"RAPP_UNAVAILABLE:skill-missing ({error})")
    expected_skill = lock.get("skill_sha256")
    expected_size = lock.get("skill_bytes")
    if expected_size is not None and len(skill) != expected_size:
        fail(3, "RAPP_UNAVAILABLE:skill-size-mismatch")
    if expected_skill:
        actual_skill = hashlib.sha256(skill).hexdigest()
        if actual_skill != expected_skill:
            fail(
                3,
                "RAPP_UNAVAILABLE:skill-integrity-mismatch "
                f"expected={expected_skill[:12]} actual={actual_skill[:12]}",
            )
    return skill


def _capsule_agent(lock, skill):
    try:
        text = skill.decode("utf-8")
    except UnicodeDecodeError as error:
        fail(6, f"RAPP_UNAVAILABLE:skill-not-utf8 ({error})")
    payload = _active_capsule_payload(text)
    if len(payload) > MAX_CAPSULE_B64:
        fail(6, "RAPP_UNAVAILABLE:skill-capsule-too-large")
    try:
        packed = base64.b64decode(payload, validate=True)
        capsule = json.loads(
            _bounded_gzip(
                packed,
                MAX_CAPSULE_JSON_BYTES,
                "skill-capsule",
            )
        )
        if lock.get("rappid") is not None:
            capsule_rappid = (
                capsule.get("platform", {})
                .get("metadata", {})
                .get("rapp", {})
                .get("rappid")
            )
            if capsule_rappid != lock["rappid"]:
                raise ValueError("capsule RAPPID does not match Grail lock")
        preserved = capsule["preserved"]["agent"]
        if not isinstance(preserved, dict):
            raise TypeError("preserved agent is not an object")
        encoded_agent = preserved["b64"]
        if (
            not isinstance(encoded_agent, str)
            or len(encoded_agent) > MAX_CAPSULE_B64
        ):
            raise ValueError("preserved agent payload is oversized")
        source = _bounded_gzip(
            base64.b64decode(encoded_agent, validate=True),
            MAX_AGENT_BYTES,
            "agent",
        )
    except (KeyError, TypeError, ValueError, OSError) as error:
        fail(6, f"RAPP_UNAVAILABLE:skill-capsule-invalid ({error})")
    if preserved.get("filename") != lock["agent_file"]:
        fail(6, "RAPP_UNAVAILABLE:capsule-agent-name-mismatch")
    exact = hashlib.sha256(source).hexdigest()
    expected_agent_size = lock.get("agent_bytes")
    if expected_agent_size is not None and len(source) != expected_agent_size:
        fail(3, "RAPP_UNAVAILABLE:capsule-agent-size-mismatch")
    if preserved.get("bytes") is not None and preserved["bytes"] != len(source):
        fail(3, "RAPP_UNAVAILABLE:capsule-agent-size-ledger-mismatch")
    if exact != preserved.get("sha256"):
        fail(3, "RAPP_UNAVAILABLE:capsule-agent-integrity-mismatch")
    return source


def _cache_root():
    configured = os.environ.get("RAPP_CACHE_HOME")
    if configured:
        return Path(configured).expanduser()
    xdg = os.environ.get("XDG_CACHE_HOME")
    return (
        Path(xdg).expanduser() / "rapp"
        if xdg
        else Path.home() / ".cache" / "rapp"
    )


def _source_path(lock, source):
    path = agent_path(lock)
    if path.is_file():
        return path
    cache = (
        _cache_root()
        / "capsule-agents"
        / hashlib.sha256(source).hexdigest()
    )
    cache.mkdir(parents=True, exist_ok=True, mode=0o700)
    materialized = cache / str(lock["agent_file"])
    if materialized.exists():
        if materialized.read_bytes() != source:
            fail(3, "RAPP_UNAVAILABLE:materialized-agent-integrity-mismatch")
        return materialized
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{materialized.name}.",
        suffix=".tmp",
        dir=cache,
    )
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(source)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, 0o444)
        os.replace(temporary, materialized)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return materialized


def agent_source(lock, use_backup=False):
    skill = _verified_skill(lock)
    grail_source = _capsule_agent(lock, skill)
    verify_bytes(lock, grail_source)
    backup = agent_path(lock)
    if backup.is_file():
        backup_source = backup.read_bytes()
        verify_bytes(lock, backup_source)
        if backup_source != grail_source:
            fail(3, "RAPP_UNAVAILABLE:rollback-agent-differs-from-grail")
    source = backup_source if use_backup and backup.is_file() else grail_source
    return source, _source_path(lock, source)


def install_shims():
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

    package = types.ModuleType("agents")
    package.__path__ = []
    module = types.ModuleType("agents.basic_agent")
    module.BasicAgent = BasicAgent
    flat = types.ModuleType("basic_agent")
    flat.BasicAgent = BasicAgent
    sys.modules.setdefault("agents", package)
    sys.modules.setdefault("agents.basic_agent", module)
    sys.modules.setdefault("basic_agent", flat)


class VerifiedSourceLoader(importlib.abc.SourceLoader):
    def __init__(self, fullname, path, source):
        self.fullname = fullname
        self.path = str(path)
        self.source = source

    def get_filename(self, fullname):
        return self.path

    def get_data(self, path):
        if os.path.realpath(path) != os.path.realpath(self.path):
            raise OSError(path)
        return self.source

    def path_stats(self, path):
        return {"mtime": 0, "size": len(self.source)}

    def set_data(self, path, data):
        return None


def load_agent(lock, source, path):
    install_shims()
    module_name = (
        "rar_scout_carried_agent_"
        + hashlib.sha256(source).hexdigest()[:16]
    )
    loader = VerifiedSourceLoader(module_name, path, source)
    spec = importlib.util.spec_from_loader(module_name, loader)
    if spec is None:
        fail(6, "RAPP_UNAVAILABLE:agent-loader-missing")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    linecache.cache[str(path)] = (
        len(source),
        None,
        source.decode("utf-8", "replace").splitlines(keepends=True),
        str(path),
    )
    try:
        loader.exec_module(module)
    except UnicodeDecodeError as error:
        sys.modules.pop(module_name, None)
        fail(6, f"RAPP_UNAVAILABLE:agent-not-utf8 ({error})")
    except ModuleNotFoundError as error:
        sys.modules.pop(module_name, None)
        fail(
            4,
            f"RAPP_UNAVAILABLE:host-dependency-missing ({error.name})",
        )
    except Exception as error:
        sys.modules.pop(module_name, None)
        fail(5, f"RAPP_UNAVAILABLE:agent-import-failed ({error})")

    class_name = str(lock["entry_class"])
    agent_class = getattr(module, class_name, None)
    if (
        not isinstance(agent_class, type)
        or agent_class.__module__ != module.__name__
        or not hasattr(agent_class, "perform")
    ):
        fail(
            6,
            f"RAPP_UNAVAILABLE:entry-class-missing ({class_name})",
        )
    try:
        agent = agent_class()
    except Exception as error:
        fail(5, f"RAPP_UNAVAILABLE:agent-init-failed ({error})")

    expected_runtime_name = lock.get("runtime_name")
    if (
        expected_runtime_name
        and getattr(agent, "name", None) != expected_runtime_name
    ):
        fail(
            6,
            "RAPP_UNAVAILABLE:runtime-name-mismatch "
            f"expected={expected_runtime_name!r} "
            f"actual={getattr(agent, 'name', None)!r}",
        )
    return agent


def execute_agent_main():
    lock = load_lock()
    source, path = agent_source(lock)
    install_shims()
    namespace = {
        "__name__": "__main__",
        "__file__": str(path),
        "__package__": None,
    }
    exec(
        compile(source.decode("utf-8"), str(path), "exec"),
        namespace,
    )


def validate(arguments, schema):
    if not isinstance(arguments, dict):
        fail(2, "arguments must be one JSON object")
    properties = schema.get("properties") or {}
    if properties:
        unknown = sorted(set(arguments) - set(properties))
        if unknown:
            fail(2, "unknown argument(s): " + ", ".join(unknown))
    missing = [
        name
        for name in schema.get("required") or []
        if name not in arguments
    ]
    if missing:
        fail(2, "missing required argument(s): " + ", ".join(missing))


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    lock = load_lock()
    use_backup = "--rollback-agent" in argv or (
        os.environ.get("RAPP_USE_AGENT_BACKUP") == "1"
    )
    argv = [item for item in argv if item != "--rollback-agent"]
    source, path = agent_source(lock, use_backup=use_backup)

    if "--preflight" in argv:
        dependencies = lock.get("host_dependencies") or []
        print(
            "RAPP_DEGRADED:host-dependencies=" + ",".join(dependencies)
            if dependencies
            else (
                "RAPP_READY:source=rollback-agent"
                if use_backup
                else "RAPP_READY:source=grail"
            )
        )
        return 0
    if "--tool" in argv:
        print(json.dumps({
            "type": "function",
            "function": {
                "name": lock.get("runtime_name") or lock["entry_class"],
                "description": (
                    lock.get("manifest", {}).get("description") or ""
                ),
                "parameters": lock.get("tool_schema") or {},
            },
        }, indent=2))
        return 0

    raw = argv[0] if argv else (sys.stdin.read().strip() or "{}")
    try:
        arguments = json.loads(raw)
    except ValueError as error:
        fail(2, f"arguments are not valid JSON ({error})")
    validate(arguments, lock.get("tool_schema") or {})
    agent = load_agent(lock, source, path)
    try:
        result = agent.perform(**arguments)
        if inspect.isawaitable(result):
            result = asyncio.run(result)
    except Exception as error:
        fail(5, f"agent raised ({error})")
    print(result if isinstance(result, str) else json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
