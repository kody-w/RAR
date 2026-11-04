---
name: "rar-kody-w-factory"
description: "Turns any caller-selected group of local RAPP agent.py files into one provisioned, functionally parity-tested Copilot Studio Draft."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/factory", "rar_sha256": "72dc8b72531aa6133effb8dc23175b85889d63f7aa2bece4970ddca60792ddbf", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.3", "author": "kody-w", "tags": ["copilot_studio", "factory", "pipeline", "deployment", "parity"]}
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
