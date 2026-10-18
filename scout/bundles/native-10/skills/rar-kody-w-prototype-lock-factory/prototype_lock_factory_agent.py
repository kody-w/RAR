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
