---
name: "rar-kody-w-factory"
description: "Turns any caller-selected group of local RAPP agent.py files into one provisioned, functionally parity-tested Copilot Studio Draft."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/factory", "rar_sha256": "72dc8b72531aa6133effb8dc23175b85889d63f7aa2bece4970ddca60792ddbf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.3", "author": "kody-w", "tags": ["copilot_studio", "factory", "pipeline", "deployment", "parity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `factory_agent.py` and embedded as the fenced Python below (sha256 72dc8b72531aa613…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `factory_agent.py` first:

```bash
python3 factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 factory_agent.py   # or on stdin
python3 factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/factory_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/factory_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/factory/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
