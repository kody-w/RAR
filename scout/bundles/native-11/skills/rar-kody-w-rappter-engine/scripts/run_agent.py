#!/usr/bin/env python3
"""Checksum-pinned runner copied into every generated RAR Scout skill."""

from __future__ import annotations

import asyncio
import hashlib
import importlib.util
import inspect
import json
import sys
import types
from pathlib import Path


sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LOCK_PATH = ROOT / "rapp" / "agent.lock.json"


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
    return lock


def agent_path(lock):
    relative = Path(str(lock["agent_file"]))
    candidate = (ROOT / relative).resolve()
    if (
        relative.is_absolute()
        or ".." in relative.parts
        or ROOT != candidate
        and ROOT not in candidate.parents
    ):
        fail(6, "RAPP_UNAVAILABLE:agent-path-escapes-bundle")
    if not candidate.is_file():
        fail(6, "RAPP_UNAVAILABLE:agent-missing")
    return candidate


def verify(lock, path):
    actual = hashlib.sha256(
        path.read_bytes().replace(b"\r\n", b"\n")
    ).hexdigest()
    expected = str(lock["agent_sha256"])
    if actual != expected:
        fail(
            3,
            "RAPP_UNAVAILABLE:integrity-mismatch "
            f"expected={expected[:12]} actual={actual[:12]}",
        )


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


def load_agent(lock, path):
    install_shims()
    spec = importlib.util.spec_from_file_location(
        "rar_scout_carried_agent",
        path,
    )
    if spec is None or spec.loader is None:
        fail(6, "RAPP_UNAVAILABLE:agent-loader-missing")
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except ModuleNotFoundError as error:
        fail(
            4,
            f"RAPP_UNAVAILABLE:host-dependency-missing ({error.name})",
        )
    except Exception as error:
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
    path = agent_path(lock)
    verify(lock, path)

    if "--preflight" in argv:
        dependencies = lock.get("host_dependencies") or []
        print(
            "RAPP_DEGRADED:host-dependencies=" + ",".join(dependencies)
            if dependencies
            else "RAPP_READY"
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
    agent = load_agent(lock, path)
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
