"""Public contract for the single-file, product-neutral RAPP Projects agent."""

from __future__ import annotations

import ast
import importlib.util
import inspect
import json
import os
import re
import socket
import subprocess
import sys
import urllib.request
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
AGENT_PATH = ROOT / "agents" / "@kody-w" / "rapp_projects_agent.py"

EXPECTED_OPERATIONS = [
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

EXPECTED_PARAMETER_TYPES = {
    "operation": "string",
    "action": "string",
    "root": "string",
    "identity_owner": "string",
    "project": "string",
    "title": "string",
    "goal": "string",
    "owner": "string",
    "origin": "string",
    "agent": "string",
    "runtime": "string",
    "session_id": "string",
    "location": "string",
    "intent": "string",
    "role": "string",
    "capabilities": "array",
    "status": "string",
    "artifacts": "array",
    "blockers": "array",
    "next_action": "string",
    "pct": "integer",
    "project_state": "string",
    "from_agent": "string",
    "to_agent": "string",
    "doc": "string",
    "open_questions": "array",
    "outcome": "string",
    "receipts": "array",
    "receipt_bindings": "object",
    "summary": "string",
    "egg": "string",
    "output": "string",
    "owner_approved": "boolean",
}

STRING_ARRAY_PARAMETERS = {
    name
    for name, kind in EXPECTED_PARAMETER_TYPES.items()
    if kind == "array"
}


def load_agent_module():
    assert AGENT_PATH.is_file(), "agents/@kody-w/rapp_projects_agent.py is missing"
    basic_dir = str(ROOT / "agents" / "@rapp")
    sys.path.insert(0, basic_dir)
    try:
        spec = importlib.util.spec_from_file_location(
            "_rapp_projects_contract",
            AGENT_PATH,
        )
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(basic_dir)


@pytest.fixture(scope="module")
def module():
    return load_agent_module()


@pytest.fixture(autouse=True)
def configured_identity_owner(monkeypatch):
    monkeypatch.setenv("RAPP_PROJECTS_OWNER", "example")


@pytest.fixture
def agent(module, monkeypatch, tmp_path):
    monkeypatch.setenv("RAPP_PROJECTS_ROOT", str(tmp_path / "env-root"))
    return module.RappProjectsAgent()


def parse_result(value: object) -> dict:
    assert isinstance(value, str), f"perform returned {type(value).__name__}"
    decoded = json.loads(value)
    assert isinstance(decoded, dict), "perform must return a JSON object string"
    return decoded


def source_tree() -> ast.Module:
    return ast.parse(AGENT_PATH.read_text(encoding="utf-8"), filename=str(AGENT_PATH))


def test_manifest_identity_version_category_tags_and_dependency(module):
    manifest = module.__manifest__
    assert manifest["schema"] == "rapp-agent/1.0"
    assert manifest["name"] == "@kody-w/rapp_projects"
    assert manifest["version"] == "1.0.3"
    assert manifest["display_name"] == "RappProjects"
    assert manifest["category"] == "productivity"
    assert manifest["tags"] == [
        "rapp-1",
        "project-management",
        "local-first",
        "rapplication",
        "productivity",
    ]
    assert manifest["dependencies"] == ["@rapp/basic_agent"]


def test_class_runtime_name_and_metadata_match(module):
    instance = module.RappProjectsAgent()
    assert module.RappProjectsAgent.__name__ == "RappProjectsAgent"
    assert instance.name == "RappProjects"
    assert instance.metadata["name"] == instance.name
    assert instance.metadata["display_name"] == instance.name
    assert instance.metadata["description"] == module.__manifest__["description"]
    assert instance.metadata["parameters"]["type"] == "object"
    assert instance.metadata["parameters"]["anyOf"] == [
        {"required": ["operation"]},
        {"required": ["action"]},
    ]
    assert instance.metadata["parameters"]["additionalProperties"] is False


def test_operation_enum_and_parameter_types_are_complete(agent):
    properties = agent.metadata["parameters"]["properties"]
    assert set(properties) == set(EXPECTED_PARAMETER_TYPES)
    assert {
        name: schema.get("type")
        for name, schema in properties.items()
    } == EXPECTED_PARAMETER_TYPES
    assert properties["operation"]["enum"] == EXPECTED_OPERATIONS
    assert properties["action"]["enum"] == EXPECTED_OPERATIONS
    assert properties["outcome"]["enum"] == ["done", "blocked", "abandoned"]
    assert properties["receipt_bindings"]["additionalProperties"] == {
        "type": "string"
    }
    for name in STRING_ARRAY_PARAMETERS & {
        "capabilities",
        "blockers",
        "open_questions",
    }:
        assert properties[name]["items"] == {"type": "string"}, name


def test_every_operation_returns_a_json_string(agent, tmp_path):
    root = tmp_path / "all-operations"
    for operation in EXPECTED_OPERATIONS:
        result = agent.perform(
            operation=operation,
            root=str(root),
            project="contract-fixture",
        )
        parse_result(result)


def test_operation_is_canonical_and_action_is_a_compatibility_alias(
    agent,
    tmp_path,
):
    action_only = parse_result(
        agent.perform(action="board", root=str(tmp_path / "action-root"))
    )
    assert action_only["status"] == "ok"
    assert action_only["operation"] == "board"

    operation_wins = parse_result(
        agent.perform(
            operation="protocol",
            action="board",
            root=str(tmp_path / "precedence-root"),
        )
    )
    assert operation_wins["status"] == "ok"
    assert operation_wins["operation"] == "protocol"
    assert not (tmp_path / "precedence-root").exists()

    missing = parse_result(agent.perform())
    assert missing["status"] == "error"
    assert missing["operation"] == "missing"
    assert "required" in missing["error"]["message"]

    unknown = parse_result(
        agent.perform(operation="protocol", host_context="not-declared")
    )
    assert unknown["status"] == "error"
    assert "unknown argument" in unknown["error"]["message"]


def test_explicit_root_overrides_environment(module, monkeypatch, tmp_path):
    explicit = tmp_path / "explicit"
    environment = tmp_path / "environment"
    monkeypatch.setenv("RAPP_PROJECTS_ROOT", str(environment))
    result = parse_result(
        module.RappProjectsAgent().perform(
            operation="board",
            root=str(explicit),
        )
    )
    assert result["root"] == "projects://"
    assert explicit.exists()
    assert not environment.exists()


def test_environment_root_is_used_when_argument_is_absent(module, monkeypatch, tmp_path):
    environment = tmp_path / "environment"
    monkeypatch.setenv("RAPP_PROJECTS_ROOT", str(environment))
    result = parse_result(module.RappProjectsAgent().perform(operation="board"))
    assert result["root"] == "projects://"
    assert environment.exists()


def test_home_root_is_the_product_neutral_fallback(module, monkeypatch, tmp_path):
    home = tmp_path / "home"
    home.mkdir()
    monkeypatch.delenv("RAPP_PROJECTS_ROOT", raising=False)
    monkeypatch.setenv("HOME", str(home))
    monkeypatch.setattr(Path, "home", classmethod(lambda cls: home))
    result = parse_result(module.RappProjectsAgent().perform(operation="board"))
    expected = home / ".rapp" / "projects-control"
    assert result["root"] == "projects://"
    assert expected.exists()


def test_new_root_requires_and_reuses_explicit_identity_owner(
    module,
    monkeypatch,
    tmp_path,
):
    root = tmp_path / "identity-root"
    monkeypatch.delenv("RAPP_PROJECTS_OWNER", raising=False)
    refused = parse_result(
        module.RappProjectsAgent().perform(
            operation="board",
            root=str(root),
        )
    )
    assert refused["status"] == "error"
    assert "identity_owner" in refused["error"]["message"]
    assert not (root / "rappid.json").exists()

    opened = parse_result(
        module.RappProjectsAgent().perform(
            operation="open",
            root=str(root),
            identity_owner="Example-Owner",
            project="identity-project",
            title="Identity project",
            goal="Bind one owner authority",
            owner="display owner",
            origin="generic fixture",
        )
    )
    assert opened["status"] == "ok"
    root_identity = json.loads(
        (root / "rappid.json").read_text(encoding="utf-8")
    )["rappid"]
    project_identity = json.loads(
        (root / "identity-project" / "rappid.json").read_text(
            encoding="utf-8"
        )
    )["rappid"]
    assert root_identity.startswith("rappid:@example-owner/projects-control:")
    assert project_identity.startswith(
        "rappid:@example-owner/identity-project:"
    )


def test_constructor_and_operations_never_open_network_connections(
    module,
    monkeypatch,
    tmp_path,
):
    def blocked(*_args, **_kwargs):
        raise AssertionError("RAPP Projects attempted a network connection")

    monkeypatch.setattr(socket, "socket", blocked)
    monkeypatch.setattr(socket, "create_connection", blocked)
    monkeypatch.setattr(urllib.request, "urlopen", blocked)
    monkeypatch.setattr(subprocess, "run", blocked)
    monkeypatch.setattr(subprocess, "Popen", blocked)
    monkeypatch.setattr(os, "system", blocked)
    instance = module.RappProjectsAgent()
    root = tmp_path / "offline"
    parse_result(instance.perform(root=str(root)))
    for operation in EXPECTED_OPERATIONS:
        parse_result(
            instance.perform(
                operation=operation,
                root=str(root),
                project="offline-fixture",
            )
        )


def test_source_has_no_network_clients_model_ids_or_secrets():
    source = AGENT_PATH.read_text(encoding="utf-8")
    tree = source_tree()
    imported_roots = {
        alias.name.split(".", 1)[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imported_roots.update(
        node.module.split(".", 1)[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    )
    assert imported_roots.isdisjoint(
        {"requests", "httpx", "aiohttp", "urllib3", "boto3"}
    )
    assert not re.search(
        r"\b(?:gpt-\d|o[134]-|claude-\d|gemini-\d|grok-\d|llama-\d|mistral-\d)",
        source,
        re.IGNORECASE,
    )
    assert not re.search(
        r"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret)"
        r"\s*[:=]\s*['\"][^'\"]+['\"]",
        source,
    )
    assert not re.search(
        r"(?:sk|ghp|github_pat|AIza)[_-]?[A-Za-z0-9_-]{16,}",
        source,
    )


def test_source_has_no_private_company_defaults():
    source = AGENT_PATH.read_text(encoding="utf-8")
    forbidden = (
        "RapterBox",
        "RBox",
        "RapterBox LLC",
        "BOX/projects",
    )
    assert not any(value.casefold() in source.casefold() for value in forbidden)


def test_errors_use_stable_json_envelopes(agent, tmp_path):
    unknown = parse_result(
        agent.perform(
            operation="not-a-real-operation",
            root=str(tmp_path / "unknown"),
        )
    )
    assert unknown["status"] == "error"
    assert unknown["operation"] == "not-a-real-operation"
    assert set(unknown) == {"status", "operation", "error"}
    assert set(unknown["error"]) == {"code", "message"}
    assert unknown["error"]["code"] == "project-error"
    assert isinstance(unknown["error"]["message"], str)
    assert unknown["error"]["message"]

    invalid = parse_result(
        agent.perform(
            operation="verify",
            root=str(tmp_path / "invalid"),
            project="missing-project",
        )
    )
    assert invalid["status"] == "error"
    assert invalid["operation"] == "verify"
    assert set(invalid) == {"status", "operation", "error"}
    assert set(invalid["error"]) == {"code", "message"}
    assert isinstance(invalid["error"]["code"], str)
    assert isinstance(invalid["error"]["message"], str)
    assert invalid["error"]["message"]


def test_standalone_supports_argv_stdin_and_tool_contract(tmp_path):
    root = tmp_path / "standalone"
    payload = json.dumps({"operation": "board", "root": str(root)})
    env = {**os.environ, "PYTHONPATH": str(ROOT / "agents" / "@rapp")}

    argv = subprocess.run(
        [sys.executable, str(AGENT_PATH), payload],
        capture_output=True,
        text=True,
        env=env,
        timeout=30,
    )
    assert argv.returncode == 0, argv.stderr
    assert json.loads(argv.stdout)["status"] == "ok"

    stdin = subprocess.run(
        [sys.executable, str(AGENT_PATH)],
        input=payload,
        capture_output=True,
        text=True,
        env=env,
        timeout=30,
    )
    assert stdin.returncode == 0, stdin.stderr
    assert json.loads(stdin.stdout)["status"] == "ok"

    tool = subprocess.run(
        [sys.executable, str(AGENT_PATH), "--tool"],
        capture_output=True,
        text=True,
        env=env,
        timeout=30,
    )
    assert tool.returncode == 0, tool.stderr
    contract = json.loads(tool.stdout)
    assert contract["type"] == "function"
    function = contract["function"]
    assert function["name"] == "RappProjects"
    assert function["parameters"]["properties"]["operation"]["enum"] == (
        EXPECTED_OPERATIONS
    )


def test_agent_is_one_source_file_with_actionable_runtime_docstring(module):
    package_files = list(AGENT_PATH.parent.glob("rapp_projects*.py"))
    assert package_files == [AGENT_PATH]
    assert not (AGENT_PATH.parent / "rapp_projects").exists()
    assert inspect.getsourcefile(module.RappProjectsAgent) == str(AGENT_PATH)

    doc = inspect.getdoc(module)
    assert doc and len(doc.splitlines()) >= 8
    lowered = doc.casefold()
    for instruction in (
        "python",
        "stdin",
        "--tool",
        "operation",
        "rapp_projects_root",
        "~/.rapp/projects-control",
        "json",
    ):
        assert instruction in lowered, f"docstring must explain {instruction}"
