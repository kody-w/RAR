"""
Contract tests — parametrized over ALL agents.
Validates manifest, class structure, perform() return type, and standalone execution.
"""

import importlib.util
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_MANIFEST_FIELDS = [
    "schema", "name", "version", "display_name",
    "description", "author", "tags", "category",
]

CALLABLE_OPERATION_SCHEMA_PACKAGES = {
    "@aibast-agents-library/client_health_score": {
        "record_id", "client_id",
    },
    "@aibast-agents-library/contract_risk_review": {
        "record_id", "contract_id",
    },
    "@aibast-agents-library/inventory_rebalancing": {"sku"},
    "@aibast-agents-library/maintenance_scheduling": {"equipment_id"},
    "@aibast-agents-library/order_status_communication": {"order_id"},
    "@aibast-agents-library/production_line_optimization": {"line_id"},
    "@aibast-agents-library/resource_utilization": {
        "record_id", "consultant_id",
    },
    "@aibast-agents-library/supplier_risk_monitoring": {"supplier_id"},
    "@aibast-agents-library/time_entry_billing": {
        "record_id", "entry_id",
    },
}


def test_filename_is_snake_case(agent_info):
    mod, cls, path = agent_info
    stem = path.stem.replace('.py', '')  # handle .py.card
    assert '-' not in stem, (
        f"{path.name}: filename uses dashes — must be snake_case "
        f"(rename to {stem.replace('-', '_')}.py)"
    )


def test_has_manifest(agent_info):
    mod, cls, path = agent_info
    assert hasattr(mod, "__manifest__"), f"{path.name}: missing __manifest__"
    assert isinstance(mod.__manifest__, dict), f"{path.name}: __manifest__ is not a dict"


def test_manifest_required_fields(agent_info):
    mod, cls, path = agent_info
    manifest = getattr(mod, "__manifest__", {})
    for field in REQUIRED_MANIFEST_FIELDS:
        assert field in manifest, f"{path.name}: __manifest__ missing '{field}'"


def test_manifest_name_format(agent_info):
    mod, cls, path = agent_info
    manifest = getattr(mod, "__manifest__", {})
    name = manifest.get("name", "")
    assert name.startswith("@"), f"{path.name}: name must start with @, got '{name}'"
    assert "/" in name, f"{path.name}: name must contain /, got '{name}'"


def test_class_inherits_basic_agent(agent_info):
    mod, cls, path = agent_info
    assert cls is not None, f"{path.name}: no BasicAgent subclass found"
    from basic_agent import BasicAgent
    assert issubclass(cls, BasicAgent), f"{path.name}: {cls.__name__} does not inherit BasicAgent"


def test_instantiation(agent_info):
    mod, cls, path = agent_info
    assert cls is not None, f"{path.name}: no agent class found"
    instance = cls()
    assert instance is not None


def test_runtime_name_is_tool_safe(agent_info):
    mod, cls, path = agent_info
    assert cls is not None, f"{path.name}: no agent class found"
    instance = cls()
    name = getattr(instance, "name", "")
    assert re.fullmatch(r"[A-Za-z0-9_-]+", name), (
        f"{path.name}: runtime name {name!r} is not a valid function name"
    )
    assert instance.metadata.get("name", name) == name, (
        f"{path.name}: metadata name must match runtime name {name!r}"
    )


def test_perform_returns_str(agent_info):
    mod, cls, path = agent_info
    assert cls is not None, f"{path.name}: no agent class found"
    instance = cls()
    # Get the first operation from metadata enum if available
    ops = []
    meta = getattr(instance, "metadata", {})
    params = meta.get("parameters", {})
    props = params.get("properties", {})
    op_prop = props.get("operation", {})
    ops = op_prop.get("enum", [])

    if ops:
        result = instance.perform(operation=ops[0])
    else:
        result = instance.perform()

    assert isinstance(result, str), (
        f"{path.name}: perform() returned {type(result).__name__}, expected str"
    )


def test_all_operations_return_nonempty(agent_info):
    mod, cls, path = agent_info
    assert cls is not None, f"{path.name}: no agent class found"
    instance = cls()

    meta = getattr(instance, "metadata", {})
    params = meta.get("parameters", {})
    props = params.get("properties", {})
    op_prop = props.get("operation", {})
    ops = op_prop.get("enum", [])

    if not ops:
        # Agent doesn't use operation enum — just call perform()
        result = instance.perform()
        assert isinstance(result, str) and len(result) > 0, (
            f"{path.name}: perform() returned empty or non-str"
        )
        return

    for op in ops:
        result = instance.perform(operation=op)
        assert isinstance(result, str), (
            f"{path.name}: perform(operation='{op}') returned {type(result).__name__}"
        )
        assert len(result) > 0, (
            f"{path.name}: perform(operation='{op}') returned empty string"
        )


def test_standalone_execution(agent_info):
    mod, cls, path = agent_info
    result = subprocess.run(
        [sys.executable, str(path)],
        capture_output=True, text=True, timeout=30,
    )
    assert result.returncode == 0, (
        f"{path.name}: standalone execution failed (exit {result.returncode})\n"
        f"stderr: {result.stderr[:500]}"
    )


def test_v111_operations_are_exposed_as_tool_parameters(agent_info):
    mod, cls, path = agent_info
    manifest = getattr(mod, "__manifest__", {})
    package_id = manifest.get("name")
    if package_id not in CALLABLE_OPERATION_SCHEMA_PACKAGES:
        return

    instance = cls()
    metadata = instance.metadata
    operations = metadata.get("operations")
    parameters = metadata.get("parameters", {})
    properties = parameters.get("properties", {})

    assert manifest.get("version") == "1.1.1"
    assert isinstance(operations, list) and operations
    assert properties.get("operation", {}).get("type") == "string"
    assert properties["operation"].get("enum") == operations
    assert "operation" not in parameters.get("required", [])
    assert set(properties) == {
        "operation", *CALLABLE_OPERATION_SCHEMA_PACKAGES[package_id],
    }
    for selector in CALLABLE_OPERATION_SCHEMA_PACKAGES[package_id]:
        assert properties[selector].get("type") == "string"


def test_store_associate_evidence_id_matrix(agent_info):
    mod, cls, path = agent_info
    if getattr(mod, "__manifest__", {}).get("name") != (
        "@aibast-agents-library/store_associate_copilot"
    ):
        return

    instance = cls()
    for operation, capability in mod.EVIDENCE_CAPABILITIES.items():
        key_field = capability["key_field"]
        record_id = str(capability["records"][0][key_field])

        omitted = instance.perform(operation=operation)
        assert "Worked examples" in omitted
        assert "Simulated Write Receipt" not in omitted

        exact = instance.perform(operation=operation, key=record_id.lower())
        assert "Exact match" in exact
        assert record_id in exact
        assert ("Simulated Write Receipt" in exact) is capability["write"]

        normalized = instance.perform(
            operation=operation,
            key=f"({record_id.lower()})",
        )
        assert "Exact match" in normalized
        assert record_id in normalized
        assert ("Simulated Write Receipt" in normalized) is capability["write"]

        embedded = instance.perform(
            operation=operation,
            user_input=f"Use exact record {record_id}.",
        )
        assert "Exact match" in embedded
        assert record_id in embedded
        assert ("Simulated Write Receipt" in embedded) is capability["write"]

        for malformed in (f"x{record_id}y", f"{record_id}0"):
            for parameter in ("key", "user_input"):
                rejected = instance.perform(
                    operation=operation,
                    **{parameter: malformed},
                )
                assert "No record matched" in rejected
                assert record_id not in rejected
                assert "Simulated Write Receipt" not in rejected


def test_prior_authorization_evidence_id_matrix():
    path = (
        REPO_ROOT / "agents" / "@aibast-agents-library" / "healthcare_stacks"
        / "prior_authorization_stack" / "prior_authorization_agent.py"
    )
    templates = REPO_ROOT / "agents" / "@aibast-agents-library" / "templates"
    if str(templates) not in sys.path:
        sys.path.insert(0, str(templates))
    spec = importlib.util.spec_from_file_location("prior_authorization_matrix", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    instance = mod.PriorAuthorizationAgent()
    for operation, capability in mod.CAPABILITIES.items():
        key_field = capability["key_field"]
        record_id = str(capability["records"][0][key_field])

        omitted = instance.perform(operation=operation)
        assert "**Error:**" not in omitted
        assert "Simulated Write Receipt" not in omitted
        assert omitted == instance.perform(operation=operation)

        exact = instance.perform(operation=operation, key=record_id.swapcase())
        assert "**Error:**" not in exact
        assert record_id in exact
        assert ("Simulated Write Receipt" in exact) is capability["write"]
        assert exact == instance.perform(operation=operation, key=record_id.swapcase())

        normalized = instance.perform(
            operation=operation,
            key=f"({record_id.swapcase()})",
        )
        assert "**Error:**" not in normalized
        assert record_id in normalized
        assert ("Simulated Write Receipt" in normalized) is capability["write"]

        embedded = instance.perform(
            operation=operation,
            user_input=f"Use exact record [{record_id.swapcase()}], now.",
        )
        assert "**Error:**" not in embedded
        assert record_id in embedded
        assert ("Simulated Write Receipt" in embedded) is capability["write"]

        for malformed in (f"x{record_id}y", f"{record_id}0"):
            for parameter in ("key", "user_input"):
                rejected = instance.perform(
                    operation=operation,
                    **{parameter: malformed},
                )
                assert "**Error:** No record found" in rejected
                assert "Simulated Write Receipt" not in rejected
                assert "Receipt ID:" not in rejected
                assert rejected == instance.perform(
                    operation=operation,
                    **{parameter: malformed},
                )
