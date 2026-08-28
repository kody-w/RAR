---
name: "rar-kody-w-factory"
description: "Turns any caller-selected group of local RAPP agent.py files into one provisioned, functionally parity-tested Copilot Studio Draft."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/factory", "rar_sha256": "e81878cc359660ac98047c607bea3245cda5967f4725091ded356597309c2b77", "source_kind": "rar-agent", "source_commit": "e0afa71b1efa282946b862adee22d21922173fdd", "version": "1.0.3", "author": "kody-w", "tags": ["copilot_studio", "factory", "pipeline", "deployment", "parity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/factory`. The original RAPP
agent is preserved byte-for-byte in `factory_agent.py` and in the RCI capsule.

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
