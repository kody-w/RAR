---
name: "rar-kody-w-factory"
description: "Turns any caller-selected group of local RAPP agent.py files into one provisioned, functionally parity-tested Copilot Studio Draft."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/factory", "rar_sha256": "e81878cc359660ac98047c607bea3245cda5967f4725091ded356597309c2b77", "source_kind": "rar-agent", "source_commit": "e0afa71b1efa282946b862adee22d21922173fdd", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "factory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/factory:a9661d9f2759313bf76d2d994ab26ea436b95a85539b28fe36fe2d41aa686cdc", "kind": "skill"}, "version": "1.0.3", "author": "kody-w", "tags": ["copilot_studio", "factory", "pipeline", "deployment", "parity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/factory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `factory_agent.py` is
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

RAPP to Copilot Studio Factory — compile selected agent.py files into one Draft.

This is the portable control-plane wrapper for CopilotStudioDeploy. It keeps
the selected local RAPP agents authoritative, preserves an existing Draft when
extending it, and exposes the build -> provision -> parity -> finalize process
as explicit resumable actions.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "doctor",
        "plan",
        "build",
        "extend",
        "provision",
        "parity",
        "finalize",
        "verify",
        "release_plan",
        "status"
      ],
      "type": "string"
    },
    "agents": {
      "description": "Tool names, class names, filenames, or paths for the exact local agent.py files to compile.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "client_id": {
      "description": "Optional public-client ID for published parity.",
      "type": "string"
    },
    "display_name": {
      "description": "Copilot Studio display name.",
      "type": "string"
    },
    "dry_run": {
      "description": "For action=build, generate the complete manifest, snapshots, and brief without initializing or pushing.",
      "type": "boolean"
    },
    "environment": {
      "description": "Target Power Platform environment ID or URL.",
      "type": "string"
    },
    "infrastructure_manifest": {
      "description": "Optional manifest path under run_dir.",
      "type": "string"
    },
    "output_root": {
      "description": "Optional root for a new build.",
      "type": "string"
    },
    "parity_cases": {
      "description": "Optional parity-case path under run_dir.",
      "type": "string"
    },
    "publisher_prefix": {
      "description": "Caller-selected publisher prefix.",
      "type": "string"
    },
    "reuse_parity": {
      "description": "For action=finalize, reuse a live parity run from the last 24 hours after full hash revalidation.",
      "type": "boolean"
    },
    "run_dir": {
      "description": "Existing factory run directory.",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `factory_agent.py` and embedded as the fenced Python below (sha256 e81878cc359660ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `factory_agent.py` first:

```bash
python3 factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 factory_agent.py   # or on stdin
python3 factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""RAPP to Copilot Studio Factory — compile selected agent.py files into one Draft.

This is the portable control-plane wrapper for CopilotStudioDeploy. It keeps
the selected local RAPP agents authoritative, preserves an existing Draft when
extending it, and exposes the build -> provision -> parity -> finalize process
as explicit resumable actions.
"""

from __future__ import annotations

import importlib
import json
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/factory",
    "version": "1.0.3",
    "display_name": "RAPP to Copilot Studio Factory",
    "description": (
        "Turns any caller-selected group of local RAPP agent.py files into one "
        "provisioned, functionally parity-tested Copilot Studio Draft."
    ),
    "author": "kody-w",
    "tags": [
        "copilot_studio",
        "factory",
        "pipeline",
        "deployment",
        "parity",
    ],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent",
        "@kody-w/copilot_studio_parity_deploy",
    ],
    "example_call": {
        "args": {
            "action": "plan",
            "agents": ["HackerNews", "Weatheragent"],
            "display_name": "News and Weather",
            "environment": "00000000-0000-0000-0000-000000000000",
            "publisher_prefix": "rapp",
        }
    },
}


_DEPLOYER_MODULES = (
    "agents.copilot_studio_deploy_agent",
    "agents.rar_kody_w_copilot_studio_parity_deploy_agent",
    "copilot_studio_deploy_agent",
    "rar_kody_w_copilot_studio_parity_deploy_agent",
)


def _load_deployer():
    failures = []
    for module_name in _DEPLOYER_MODULES:
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError as error:
            failures.append(str(error))
            continue
        agent_class = getattr(module, "CopilotStudioDeployAgent", None)
        manifest = getattr(module, "__manifest__", {})
        if (
            agent_class is not None
            and manifest.get("name")
            == "@kody-w/copilot_studio_parity_deploy"
        ):
            return module, agent_class
    raise RuntimeError(
        "CopilotStudioDeployAgent is not installed. Install the declared "
        "@kody-w/copilot_studio_parity_deploy dependency. "
        + "; ".join(failures[-2:])
    )


def _parse_result(value):
    if isinstance(value, dict):
        return value
    if not isinstance(value, str):
        raise RuntimeError("CopilotStudioDeploy returned a non-string result")
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as error:
        raise RuntimeError(
            "CopilotStudioDeploy returned non-JSON output: " + value[:500]
        ) from error
    if not isinstance(parsed, dict):
        raise RuntimeError("CopilotStudioDeploy result must be a JSON object")
    return parsed


def _write_json(module, path: Path, value) -> None:
    writer = getattr(module, "_write_json", None)
    if writer is None:
        raise RuntimeError(
            "Installed CopilotStudioDeploy is too old for factory extensions"
        )
    writer(path, value)


class RappCopilotStudioFactoryAgent(BasicAgent):
    """Resumable factory around the generic Copilot Studio deploy engine."""

    def __init__(self):
        self.name = "RappCopilotStudioFactory"
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": [
                            "doctor",
                            "plan",
                            "build",
                            "extend",
                            "provision",
                            "parity",
                            "finalize",
                            "verify",
                            "release_plan",
                            "status",
                        ],
                    },
                    "agents": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": (
                            "Tool names, class names, filenames, or paths for "
                            "the exact local agent.py files to compile."
                        ),
                    },
                    "display_name": {
                        "type": "string",
                        "description": "Copilot Studio display name.",
                    },
                    "environment": {
                        "type": "string",
                        "description": "Target Power Platform environment ID or URL.",
                    },
                    "publisher_prefix": {
                        "type": "string",
                        "description": "Caller-selected publisher prefix.",
                    },
                    "run_dir": {
                        "type": "string",
                        "description": "Existing factory run directory.",
                    },
                    "output_root": {
                        "type": "string",
                        "description": "Optional root for a new build.",
                    },
                    "infrastructure_manifest": {
                        "type": "string",
                        "description": "Optional manifest path under run_dir.",
                    },
                    "parity_cases": {
                        "type": "string",
                        "description": "Optional parity-case path under run_dir.",
                    },
                    "client_id": {
                        "type": "string",
                        "description": "Optional public-client ID for published parity.",
                    },
                    "dry_run": {
                        "type": "boolean",
                        "description": (
                            "For action=build, generate the complete manifest, "
                            "snapshots, and brief without initializing or pushing."
                        ),
                    },
                    "reuse_parity": {
                        "type": "boolean",
                        "description": (
                            "For action=finalize, reuse a live parity run from "
                            "the last 24 hours after full hash revalidation."
                        ),
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _call(self, action: str, **kwargs):
        _, agent_class = _load_deployer()
        payload = {"action": action, **kwargs}
        return _parse_result(agent_class().perform(**payload))

    def _extend(self, **kwargs):
        module, _ = _load_deployer()
        required_helpers = (
            "_resolve_agent_paths",
            "_build_manifest",
            "_snapshot_sources",
            "_brief_text",
            "_protected_identity",
            "_invoke_plugin_agent",
            "_materialize_skill_resources",
            "_validate_target_project",
            "_pac_pull_push",
            "_sha256",
            "_utc_now",
        )
        missing = [
            name for name in required_helpers
            if not hasattr(module, name)
        ]
        if missing:
            raise RuntimeError(
                "Installed CopilotStudioDeploy is too old for action=extend: "
                + ", ".join(missing)
            )

        run_dir_value = str(kwargs.get("run_dir") or "").strip()
        selectors = kwargs.get("agents")
        if not run_dir_value:
            raise ValueError("run_dir is required for action=extend")
        if not isinstance(selectors, list) or not selectors:
            raise ValueError("agents must contain the complete desired agent set")

        run_dir = Path(run_dir_value).expanduser().resolve()
        project = run_dir / "project"
        manifest_path = run_dir / "rapp-deploy-manifest.json"
        state_path = run_dir / "state.json"
        if not project.is_dir() or not manifest_path.is_file():
            raise ValueError("run_dir is not a complete Copilot Studio run")

        old_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        display_name = str(old_manifest.get("display_name") or "").strip()
        environment = str(old_manifest.get("environment") or "").strip()
        prefix = str(old_manifest.get("publisher_prefix") or "").strip()
        requested_identity = {
            "display_name": kwargs.get("display_name"),
            "environment": kwargs.get("environment"),
            "publisher_prefix": kwargs.get("publisher_prefix"),
        }
        existing_identity = {
            "display_name": display_name,
            "environment": environment,
            "publisher_prefix": prefix,
        }
        for key, requested in requested_identity.items():
            if requested is not None and str(requested).strip() != existing_identity[key]:
                raise ValueError(
                    f"extension cannot change existing {key}"
                )
        paths = module._resolve_agent_paths(selectors)
        new_manifest = module._build_manifest(
            paths,
            display_name=display_name,
            environment=environment,
            publisher_prefix=prefix,
        )
        old_tools = {
            row["tool_name"] for row in old_manifest.get("source_agents", [])
        }
        old_contracts = {
            row["tool_name"]: row
            for row in old_manifest.get("source_agents", [])
        }
        new_contracts = {
            row["tool_name"]: row
            for row in new_manifest.get("source_agents", [])
        }
        new_tools = set(new_contracts)
        removed = sorted(old_tools - new_tools)
        if removed:
            raise ValueError(
                "extension cannot remove existing source agents: "
                + ", ".join(removed)
            )
        for tool_name, old_contract in old_contracts.items():
            new_contract = new_contracts[tool_name]
            for field in ("class_name", "source_path", "source_sha256"):
                if new_contract.get(field) != old_contract.get(field):
                    raise ValueError(
                        "extension cannot replace existing source identity: "
                        f"{tool_name}.{field}"
                    )
        old_order = [
            row["tool_name"] for row in old_manifest.get("source_agents", [])
        ]
        caller_order = [
            row["tool_name"] for row in new_manifest.get("source_agents", [])
        ]
        stable_order = old_order + [
            tool_name for tool_name in caller_order
            if tool_name not in old_tools
        ]
        new_manifest["source_agents"] = [
            new_contracts[tool_name] for tool_name in stable_order
        ]

        identity = module._protected_identity(project)
        if (
            identity.get("displayName") != display_name
            or identity.get("EnvironmentId") != environment
        ):
            raise RuntimeError(
                "existing project identity differs from its deployment manifest"
            )
        module._snapshot_sources(new_manifest, run_dir)
        _write_json(module, manifest_path, new_manifest)
        brief_path = run_dir / "architect-brief.md"
        brief_path.write_text(
            module._brief_text(new_manifest, project),
            encoding="utf-8",
        )
        state = (
            json.loads(state_path.read_text(encoding="utf-8"))
            if state_path.is_file()
            else {"schema": "rapp-to-copilot-studio-state/1.0"}
        )
        state.update({
            "updated_at": module._utc_now(),
            "stage": "extension-planned",
            "manifest_sha256": module._sha256(manifest_path),
            "published": False,
        })
        _write_json(module, state_path, state)

        prompt = (
            f"Read the complete architect brief at {brief_path}. Extend the "
            f"existing initialized project at {project} in place. Preserve "
            "identity and every existing selected capability. Add only the "
            "new caller-selected source contracts. Missing runtime capabilities "
            "must become explicit provisionable infrastructure requirements, "
            "not terminal gaps or model-knowledge substitutes. Do not run PAC, "
            "push, or publish."
        )
        architect_output = module._invoke_plugin_agent(
            module.PLUGIN_AGENTS["architect"],
            prompt,
            cwd=run_dir,
            log_path=run_dir / "logs" / "architect-extension.log",
        )
        materialized = module._materialize_skill_resources(project)
        if module._protected_identity(project) != identity:
            raise RuntimeError(
                "architect changed protected Copilot Studio identity"
            )
        validation = module._validate_target_project(project, prefix)
        pac = module._pac_pull_push(
            project,
            run_dir / "logs" / "pac-extension-push.log",
            publisher_prefix=prefix,
            protected_identity=module._protected_identity(
                project,
                include_file_hashes=False,
            ),
        )
        state.update({
            "updated_at": module._utc_now(),
            "stage": "extension-pushed-unverified",
            "published": False,
        })
        _write_json(module, state_path, state)
        return {
            "status": "extension_pushed",
            "run_dir": str(run_dir),
            "source_agents": sorted(new_tools),
            "infrastructure_requests": [
                row["id"]
                for row in new_manifest.get("infrastructure_requests", [])
            ],
            "materialized_resources": materialized,
            "validation": validation,
            "architect": architect_output,
            "pac": pac,
            "published": False,
            "next_action": "provision",
        }

    def _status(self, run_dir_value: str):
        if not run_dir_value.strip():
            raise ValueError("run_dir is required for action=status")
        run_dir = Path(run_dir_value).expanduser().resolve()
        if not run_dir.is_dir():
            raise ValueError(f"run_dir does not exist: {run_dir}")
        for required in ("rapp-deploy-manifest.json", "state.json"):
            if not (run_dir / required).is_file():
                raise ValueError(
                    f"run_dir is missing required artifact: {required}"
                )
        result = {"status": "success", "run_dir": str(run_dir)}
        for name in (
            "state.json",
            "result.json",
            "infrastructure-receipts.json",
            "parity-evidence.json",
            "release-receipt.json",
        ):
            path = run_dir / name
            if path.is_file():
                result[name.removesuffix(".json")] = json.loads(
                    path.read_text(encoding="utf-8")
                )
        return result

    def perform(self, **kwargs):
        action = str(kwargs.get("action") or "").strip().lower()
        shared = {
            key: kwargs.get(key)
            for key in (
                "agents",
                "display_name",
                "environment",
                "publisher_prefix",
                "run_dir",
                "output_root",
                "infrastructure_manifest",
                "parity_cases",
                "client_id",
                "dry_run",
                "reuse_parity",
            )
            if kwargs.get(key) is not None
        }
        try:
            if action == "doctor":
                result = self._call("doctor")
            elif action == "plan":
                result = self._call("plan", **shared)
            elif action == "build":
                result = self._call("deploy", **shared)
            elif action == "extend":
                result = self._extend(**shared)
            elif action == "provision":
                result = self._call("provision", **shared)
            elif action == "parity":
                result = self._call("parity", **shared)
            elif action == "finalize":
                result = self._call("finalize", **shared)
            elif action == "verify":
                parity = self._call("parity", **shared)
                if parity.get("status") != "success":
                    result = {
                        "status": "parity_failed",
                        "parity": parity,
                    }
                else:
                    finalize = self._call("finalize", **shared)
                    result = {
                        "status": (
                            "success"
                            if finalize.get("status") == "success"
                            else "finalize_failed"
                        ),
                        "parity": parity,
                        "finalize": finalize,
                    }
            elif action == "release_plan":
                result = self._call("release_plan", **shared)
            elif action == "status":
                result = self._status(str(kwargs.get("run_dir") or ""))
            else:
                result = {
                    "status": "error",
                    "error": (
                        "unknown action; expected doctor, plan, build, extend, "
                        "provision, parity, finalize, verify, release_plan, or status"
                    ),
                }
        except (
            ImportError,
            OSError,
            RuntimeError,
            ValueError,
        ) as error:
            result = {
                "status": "error",
                "error": f"{type(error).__name__}: {error}",
            }
        return json.dumps(result, indent=2, ensure_ascii=True)


if __name__ == "__main__":
    print(RappCopilotStudioFactoryAgent().perform(action="doctor"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
