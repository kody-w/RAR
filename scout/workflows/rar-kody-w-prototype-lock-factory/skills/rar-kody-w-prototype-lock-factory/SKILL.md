---
name: "rar-kody-w-prototype-lock-factory"
description: "Locks an accepted prototype into a canonical project, enforces local-before-cloud causal evidence, prevents post-acceptance scope drift, and exports a hash-verified no-PII handoff."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/prototype_lock_factory_agent", "rar_sha256": "916f1fb4e63074c6302593d80a28f31779ef070b6e4352ec4c45cda14cab431b", "source_kind": "rar-agent", "source_commit": "234384a80e84ebb7c5097959c2c9d2223fc0fabb", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "prototype_lock_factory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/prototype-lock-factory:f1e10603170d0e6ea17ac83f03e30f4e1b04f644451c0f9bfa2d0a57d97c4b44", "kind": "skill"}, "version": "1.0.1", "author": "RAPP Community", "tags": ["prototype", "factory", "local_first", "acceptance", "handoff", "no_pii"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/prototype_lock_factory_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `prototype_lock_factory_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
