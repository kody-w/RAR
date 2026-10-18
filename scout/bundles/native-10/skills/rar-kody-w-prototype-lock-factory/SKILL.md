---
name: "rar-kody-w-prototype-lock-factory"
description: "Locks an accepted prototype into a canonical project, enforces local-before-cloud causal evidence, prevents post-acceptance scope drift, and exports a hash-verified no-PII handoff."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/prototype_lock_factory_agent", "rar_sha256": "916f1fb4e63074c6302593d80a28f31779ef070b6e4352ec4c45cda14cab431b", "source_kind": "rar-agent", "source_commit": "234384a80e84ebb7c5097959c2c9d2223fc0fabb", "version": "1.0.1", "author": "RAPP Community", "tags": ["prototype", "factory", "local_first", "acceptance", "handoff", "no_pii"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/prototype_lock_factory_agent`. The original RAPP
agent is preserved byte-for-byte in `prototype_lock_factory_agent.py` and in the RCI capsule.

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

Prototype Lock Factory — freeze an accepted prototype into a public handoff.

Use this after a prototype finally behaves correctly and before anyone adds
"one more impressive feature." The accepted transcript becomes authority.

Process:
1. Capture the business workflow, adapter boundary, specialist roster, human
   decisions, immutable transport, and exact approved transcript.
2. Create one canonical `rapp_projects/<slug>/` source with `agents/`,
   `inputs/`, `outputs/`, `exports/`, `PROCESS_CONTRACT.json`, and
   `APPROVED_TRANSCRIPT.md`.
3. Keep transport dumb. The function/agents own routing and business logic.
   `user_guid` may partition memory and workflow state; it never selects agents.
4. Test T1 local/direct first. Require the real natural prompts, truthful
   specialist trace, editable artifacts, downloaded hashes, visual inspection,
   reset, and a causal input -> calculation -> output delta.
5. Only after T1 passes, run the identical T2 cloud gate. Test an immutable T3
   harness last and never debug business logic through it.
6. Once the transcript is accepted, treat later scope as a new version. Do not
   silently replace the approved ending, prompts, artifacts, or human boundary.
7. Export only canonical agents, contracts, evidence receipts, and hashes.
   Public export refuses obvious secrets and requires no customer, employee,
   tenant, subscription, endpoint, phone, or email identifiers.
8. Promote the sanitized public derivative only after export:
   - validate/test the single-file agent against the public registry SDK;
   - project agent.py -> SKILL.md with the shared converter and prove a
     byte-identical round trip;
   - run the complete public skill validation suite;
   - submit the exact bytes through the registry mutation/receipt path;
   - verify the notarized registry hash and the public skills-repo hash.
9. Commit the canonical private/project source and public derivative with
   provenance. A public receipt is not proof of the private project, and a
   private green suite is not permission to publish customer context.

The agent is offline and standard-library only. It scaffolds and gates files;
the host executes the commands named by the contract and supplies measured
evidence back to operation=gate or operation=run.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "contract_json": {
      "type": "string"
    },
    "evidence_json": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "describe",
        "plan",
        "scaffold",
        "gate",
        "export",
        "run"
      ],
      "type": "string"
    },
    "output_dir": {
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prototype_lock_factory_agent.py` and embedded as the fenced Python below (sha256 916f1fb4e63074c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prototype_lock_factory_agent.py` first:

```bash
python3 prototype_lock_factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prototype_lock_factory_agent.py   # or on stdin
python3 prototype_lock_factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""Prototype Lock Factory — freeze an accepted prototype into a public handoff.

Use this after a prototype finally behaves correctly and before anyone adds
"one more impressive feature." The accepted transcript becomes authority.

Process:
1. Capture the business workflow, adapter boundary, specialist roster, human
   decisions, immutable transport, and exact approved transcript.
2. Create one canonical `rapp_projects/<slug>/` source with `agents/`,
   `inputs/`, `outputs/`, `exports/`, `PROCESS_CONTRACT.json`, and
   `APPROVED_TRANSCRIPT.md`.
3. Keep transport dumb. The function/agents own routing and business logic.
   `user_guid` may partition memory and workflow state; it never selects agents.
4. Test T1 local/direct first. Require the real natural prompts, truthful
   specialist trace, editable artifacts, downloaded hashes, visual inspection,
   reset, and a causal input -> calculation -> output delta.
5. Only after T1 passes, run the identical T2 cloud gate. Test an immutable T3
   harness last and never debug business logic through it.
6. Once the transcript is accepted, treat later scope as a new version. Do not
   silently replace the approved ending, prompts, artifacts, or human boundary.
7. Export only canonical agents, contracts, evidence receipts, and hashes.
   Public export refuses obvious secrets and requires no customer, employee,
   tenant, subscription, endpoint, phone, or email identifiers.
8. Promote the sanitized public derivative only after export:
   - validate/test the single-file agent against the public registry SDK;
   - project agent.py -> SKILL.md with the shared converter and prove a
     byte-identical round trip;
   - run the complete public skill validation suite;
   - submit the exact bytes through the registry mutation/receipt path;
   - verify the notarized registry hash and the public skills-repo hash.
9. Commit the canonical private/project source and public derivative with
   provenance. A public receipt is not proof of the private project, and a
   private green suite is not permission to publish customer context.

The agent is offline and standard-library only. It scaffolds and gates files;
the host executes the commands named by the contract and supplies measured
evidence back to operation=gate or operation=run.
"""

from __future__ import annotations

import ast
import hashlib
import json
import re
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name = name
            self.metadata = metadata or {}

        def to_tool(self):
            return {
                "type": "function",
                "function": {
                    "name": self.name,
                    "description": self.metadata.get("description", ""),
                    "parameters": self.metadata.get("parameters", {}),
                },
            }


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/prototype_lock_factory_agent",
    "version": "1.0.1",
    "display_name": "Prototype Lock Factory",
    "description": (
        "Locks an accepted prototype into a canonical project, enforces "
        "local-before-cloud causal evidence, prevents post-acceptance scope "
        "drift, and exports a hash-verified no-PII handoff."
    ),
    "author": "RAPP Community",
    "tags": [
        "prototype",
        "factory",
        "local_first",
        "acceptance",
        "handoff",
        "no_pii",
    ],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {
        "args": {
            "operation": "plan",
            "contract_json": (
                "{\"schema\":\"rapp-prototype-process/1.0\","
                "\"project_slug\":\"sample_project\"}"
            ),
        }
    },
}


SCHEMA = "rapp-prototype-process/1.0"
INVARIANTS = (
    "immutable_transport",
    "local_first",
    "one_specialist_per_turn",
    "user_guid_partition_only",
    "human_approval",
    "artifact_delta",
    "reset_supported",
    "canonical_project_source",
)
SLUG = re.compile(r"^[a-z0-9][a-z0-9_-]{1,79}$")
PUBLIC_DENY = re.compile(
    r"(?i)(client[_-]?secret|api[_-]?key|access[_-]?token|"
    r"refresh[_-]?token|x-functions-key|tenant[_-]?id|"
    r"subscription[_-]?id)\s*[:=]\s*[\"']?[^\"'\s]+"
)


def _now():
    return datetime.now(timezone.utc).isoformat()


def _load(value, field):
    if isinstance(value, dict):
        return value
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a JSON object, string, or path")
    path = Path(value).expanduser()
    text = path.read_text(encoding="utf-8") if path.is_file() else value
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{field} must be valid JSON") from exc
    if not isinstance(parsed, dict):
        raise ValueError(f"{field} must decode to an object")
    return parsed


def _errors(contract):
    errors = []
    if contract.get("schema") != SCHEMA:
        errors.append(f"schema must be {SCHEMA}")
    slug = str(contract.get("project_slug") or "")
    if not SLUG.fullmatch(slug):
        errors.append("project_slug must be lowercase snake/kebab case")
    for field in ("display_name", "business_workflow", "adapter_boundary"):
        if not contract.get(field):
            errors.append(f"{field} is required")
    invariants = contract.get("invariants")
    if not isinstance(invariants, dict):
        errors.append("invariants must be an object")
    else:
        for name in INVARIANTS:
            if invariants.get(name) is not True:
                errors.append(f"invariants.{name} must be true")
    specialists = contract.get("specialists")
    if not isinstance(specialists, list) or not specialists:
        errors.append("specialists must be a non-empty array")
    else:
        for index, specialist in enumerate(specialists):
            if not isinstance(specialist, dict):
                errors.append(f"specialists[{index}] must be an object")
            elif not str(specialist.get("file") or "").endswith("_agent.py"):
                errors.append(
                    f"specialists[{index}].file must end with _agent.py"
                )
    turns = contract.get("approved_transcript")
    if not isinstance(turns, list) or not turns:
        errors.append("approved_transcript must be non-empty")
    else:
        for index, turn in enumerate(turns):
            if not isinstance(turn, dict):
                errors.append(f"approved_transcript[{index}] must be an object")
                continue
            for field in ("prompt", "expected_agent", "assertions"):
                if not turn.get(field):
                    errors.append(
                        f"approved_transcript[{index}].{field} is required"
                    )
    transport = contract.get("transport_contract")
    if not isinstance(transport, dict) or transport.get("immutable") is not True:
        errors.append("transport_contract.immutable must be true")
    return errors


def _write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        delete=False,
    ) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    temporary.replace(path)


def _write_json(path, value):
    _write(path, json.dumps(value, indent=2, sort_keys=True) + "\n")


def _transcript(contract):
    lines = [
        f"# Approved workflow: {contract['display_name']}",
        "",
        "| Turn | Prompt | Expected agent | Assertions |",
        "|---:|---|---|---|",
    ]
    for index, turn in enumerate(contract["approved_transcript"], 1):
        prompt = str(turn["prompt"]).replace("|", "\\|")
        assertions = "; ".join(
            str(item).replace("|", "\\|") for item in turn["assertions"]
        )
        lines.append(
            f"| {index} | {prompt} | `{turn['expected_agent']}` | "
            f"{assertions} |"
        )
    return "\n".join(lines) + "\n"


def _evidence_errors(evidence, contract):
    errors = []
    local = evidence.get("local")
    if not isinstance(local, dict) or local.get("passed") is not True:
        errors.append("T1 local evidence must pass first")
    for field in ("artifact_hashes", "visible_agent_trace", "causal_delta"):
        if not evidence.get(field):
            errors.append(f"{field} proof is required")
    gates = contract.get("gates") or {}
    if gates.get("require_cloud"):
        cloud = evidence.get("cloud")
        if not isinstance(cloud, dict) or cloud.get("passed") is not True:
            errors.append("T2 cloud evidence is required")
    if gates.get("require_transport"):
        transport = evidence.get("transport")
        if (
            not isinstance(transport, dict)
            or transport.get("passed") is not True
            or transport.get("wire_changed") is not False
        ):
            errors.append(
                "T3 transport must pass with wire_changed=false"
            )
    return errors


def _scan(project):
    findings = []
    for path in project.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {
            ".py",
            ".json",
            ".md",
            ".yml",
            ".yaml",
        }:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if PUBLIC_DENY.search(text):
            findings.append(str(path.relative_to(project)))
        if path.suffix == ".py":
            try:
                ast.parse(text, filename=str(path))
            except SyntaxError as exc:
                findings.append(f"{path.name}: {exc}")
    return findings


def _sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _export(project):
    archive = project / "exports" / (
        project.name.replace("-", "_") + "_approved_agents.zip"
    )
    archive.parent.mkdir(parents=True, exist_ok=True)
    manifest = {}
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as target:
        for path in sorted(project.rglob("*")):
            if not path.is_file() or "exports" in path.parts:
                continue
            if "__pycache__" in path.parts:
                continue
            name = str(path.relative_to(project.parent))
            target.write(path, name)
            manifest[name] = _sha(path)
    _write_json(project / "exports" / "SHA256SUMS.json", manifest)
    return {
        "archive": str(archive),
        "sha256": _sha(archive),
        "members": len(manifest),
    }


class PrototypeLockFactoryAgent(BasicAgent):
    def __init__(self):
        self.name = "PrototypeLockFactory"
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "describe",
                            "plan",
                            "scaffold",
                            "gate",
                            "export",
                            "run",
                        ],
                    },
                    "contract_json": {"type": "string"},
                    "evidence_json": {"type": "string"},
                    "output_dir": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        operation = str(kwargs.get("operation") or "describe").lower()
        if operation == "describe":
            return json.dumps(
                {
                    "status": "ok",
                    "package": __manifest__["name"],
                    "version": __manifest__["version"],
                    "instructions": __doc__,
                },
                indent=2,
            )
        try:
            contract = _load(kwargs.get("contract_json"), "contract_json")
            errors = _errors(contract)
            if errors:
                return json.dumps(
                    {"status": "refused", "stage": "contract", "errors": errors},
                    indent=2,
                )
            if operation == "plan":
                return json.dumps(
                    {
                        "status": "ok",
                        "stages": [
                            "contract",
                            "scaffold",
                            "T1 local evidence",
                            "T2 cloud evidence",
                            "T3 immutable transport evidence",
                            "no-PII export",
                        ],
                        "project_slug": contract["project_slug"],
                    },
                    indent=2,
                )
            output = Path(kwargs.get("output_dir") or ".").expanduser().resolve()
            project = output / contract["project_slug"]
            if operation in {"scaffold", "run"}:
                for name in (
                    "inputs",
                    "agents",
                    "outputs",
                    "exports",
                    "tests",
                ):
                    (project / name).mkdir(parents=True, exist_ok=True)
                _write_json(project / "PROCESS_CONTRACT.json", contract)
                _write(
                    project / "APPROVED_TRANSCRIPT.md",
                    _transcript(contract),
                )
                _write_json(
                    project / "project_config.json",
                    {
                        "guid": contract["project_slug"],
                        "name": contract["display_name"],
                        "enabled_agents": [
                            item["file"] for item in contract["specialists"]
                        ],
                        "behavior_contract": "APPROVED_TRANSCRIPT.md",
                    },
                )
                if operation == "scaffold":
                    return json.dumps(
                        {"status": "success", "project_dir": str(project)},
                        indent=2,
                    )
            if operation in {"gate", "run"}:
                evidence = _load(
                    kwargs.get("evidence_json"),
                    "evidence_json",
                )
                findings = _scan(project)
                gate_errors = _evidence_errors(evidence, contract) + findings
                receipt = {
                    "schema": "rapp-prototype-acceptance/1.0",
                    "status": "success" if not gate_errors else "refused",
                    "errors": gate_errors,
                    "evidence": evidence,
                    "checked_at": _now(),
                }
                _write_json(
                    project / "outputs" / "acceptance_receipt.json",
                    receipt,
                )
                if gate_errors:
                    return json.dumps(receipt, indent=2)
                if operation == "gate":
                    return json.dumps(receipt, indent=2)
            if operation in {"export", "run"}:
                receipt_path = (
                    project / "outputs" / "acceptance_receipt.json"
                )
                if not receipt_path.is_file():
                    return json.dumps(
                        {
                            "status": "refused",
                            "stage": "export",
                            "message": "Passing acceptance receipt required.",
                        },
                        indent=2,
                    )
                receipt = json.loads(
                    receipt_path.read_text(encoding="utf-8")
                )
                if receipt.get("status") != "success":
                    return json.dumps(
                        {
                            "status": "refused",
                            "stage": "export",
                            "message": "Acceptance receipt did not pass.",
                        },
                        indent=2,
                    )
                return json.dumps(
                    {"status": "success", "export": _export(project)},
                    indent=2,
                )
            raise ValueError(f"Unknown operation: {operation}")
        except (OSError, ValueError, KeyError) as exc:
            return json.dumps(
                {"status": "error", "message": str(exc)},
                indent=2,
            )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tool":
        print(json.dumps(PrototypeLockFactoryAgent().to_tool(), indent=2))
    else:
        raw = sys.argv[1] if len(sys.argv) > 1 else (
            sys.stdin.read().strip() or "{}"
        )
        print(PrototypeLockFactoryAgent().perform(**json.loads(raw)))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
