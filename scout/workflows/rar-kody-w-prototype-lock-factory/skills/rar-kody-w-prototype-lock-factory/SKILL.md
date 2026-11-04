---
name: "rar-kody-w-prototype-lock-factory"
description: "Locks an accepted prototype into a canonical project, enforces local-before-cloud causal evidence, prevents post-acceptance scope drift, and exports a hash-verified no-PII handoff."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/prototype_lock_factory_agent", "rar_sha256": "eb9308df4af313ea90fd0ef432c2b69d04635135c0c1d368e1886f775eedb2b0", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "RAPP Community", "tags": ["prototype", "factory", "local_first", "acceptance", "handoff", "no_pii"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prototype_lock_factory_agent.py` and embedded as the fenced Python below (sha256 eb9308df4af313ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prototype_lock_factory_agent.py` first:

```bash
python3 prototype_lock_factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prototype_lock_factory_agent.py   # or on stdin
python3 prototype_lock_factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/prototype_lock_factory_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/prototype_lock_factory_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/prototype_lock_factory_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
