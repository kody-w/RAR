---
name: "rar-kody-w-prototype-lock-factory"
description: "Locks an accepted prototype into a canonical project, enforces local-before-cloud causal evidence, prevents post-acceptance scope drift, and exports a hash-verified no-PII handoff."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/prototype_lock_factory_agent", "rar_sha256": "eb9308df4af313ea90fd0ef432c2b69d04635135c0c1d368e1886f775eedb2b0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "RAPP Community", "tags": ["prototype", "factory", "local_first", "acceptance", "handoff", "no_pii"]}
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
