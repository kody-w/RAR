---
name: "rar-kody-w-copilot-studio-forge"
description: "Authors Copilot Studio, M365, and Foundry artifacts from RAPP agents through four embedded engines \u2014 bundles, topics, solutions, and exports."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_forge_agent", "rar_sha256": "b74dc71864503e47340899674b0e8b9c17f4e8fc617298ed83e5f148bf87e709", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "1.0.2", "author": "kody-w", "tags": ["copilot-studio", "forge", "transpiler", "mcs", "m365", "foundry", "authoring", "assimilated"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/copilot_studio_forge_agent`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_forge_agent.py` and in the RCI capsule.

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

Copilot Studio Forge (assimilated) — author CS / M365 / Foundry artifacts from RAPP agents.

Consolidates four overlapping agents (copilot_studio_forge, topic_wizard,
copilot_studio_transpiler, agent_transpiler) into one authoring surface. Each
source agent's real logic is embedded verbatim as an internal engine; a single
dispatcher routes by `engine`. No credentials are hardcoded — engines read from
the environment or local config.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Engine-specific verb (e.g. forge/list/refresh/inspect/validate, wizard/generate/scan, transpile/analyze/preview).",
      "type": "string"
    },
    "agent_filename": {
      "description": "forge engine: specific agent file.",
      "type": "string"
    },
    "agent_name": {
      "description": "solution/export engine: agent to convert.",
      "type": "string"
    },
    "agents_dir": {
      "description": "topics engine: directory of agents/*.py to author topics from.",
      "type": "string"
    },
    "engine": {
      "description": "Which authoring engine: forge (swarm->CS bundle), topics (agents->topic yaml), solution (agent->full CS solution), export (agent->m365/foundry).",
      "enum": [
        "forge",
        "topics",
        "solution",
        "export",
        "help"
      ],
      "type": "string"
    },
    "output_dir": {
      "description": "Where to write generated artifacts.",
      "type": "string"
    },
    "platform": {
      "description": "export engine target platform.",
      "enum": [
        "m365",
        "copilot_studio",
        "foundry"
      ],
      "type": "string"
    },
    "swarm_name": {
      "description": "forge engine: swarm singleton name.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_forge_agent.py` and embedded as the fenced Python below (sha256 b74dc71864503e47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_forge_agent.py` first:

```bash
python3 copilot_studio_forge_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_forge_agent.py   # or on stdin
python3 copilot_studio_forge_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""Copilot Studio Forge (assimilated) — author CS / M365 / Foundry artifacts from RAPP agents.\n\nConsolidates four overlapping agents (copilot_studio_forge, topic_wizard,\ncopilot_studio_transpiler, agent_transpiler) into one authoring surface. Each\nsource agent's real logic is embedded verbatim as an internal engine; a single\ndispatcher routes by `engine`. No credentials are hardcoded — engines read from\nthe environment or local config."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/copilot_studio_forge_agent",
    "version": "1.0.2",
    "display_name": "CopilotStudioForge",
    "description": "Authors Copilot Studio, M365, and Foundry artifacts from RAPP agents through four embedded engines \u2014 bundles, topics, solutions, and exports.",
    "author": "kody-w",
    "tags": ["copilot-studio", "forge", "transpiler", "mcs", "m365", "foundry", "authoring", "assimilated"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": ["DATAVERSE_ENVIRONMENT_URL", "AZURE_TENANT_ID", "COPILOT_STUDIO_CLIENT_ID", "AI_PROJECT_CONNECTION_STRING"],
    "dependencies": ["@rapp/basic_agent"],
}

from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any
import ast
import glob
import hashlib
import json
import logging
import os
import re
import textwrap
import time
import urllib.error
import urllib.request
import zipfile

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # pragma: no cover
    try:
        from basic_agent import BasicAgent
    except ImportError:
        class BasicAgent:  # type: ignore
            def __init__(self, name=None, metadata=None):
                self.name = name
                self.metadata = metadata


class _EngineBase:
    """Plain shim so the embedded source-agent engines don't need BasicAgent.
    Each engine sets self.name/self.metadata in its own __init__; we just absorb
    the super().__init__(...) call without side effects."""
    def __init__(self, *args, **kwargs):
        if args:
            self.name = getattr(self, "name", args[0])


# ============================================================================
# Embedded engines — REAL logic ported verbatim from the source agents
# ============================================================================
_MS_REPO_RAW = "https://raw.githubusercontent.com/microsoft/skills-for-copilot-studio/main"

_MS_TEMPLATES = {
    "agent":        f"{_MS_REPO_RAW}/templates/agents/agent.mcs.yml",
    "child":        f"{_MS_REPO_RAW}/templates/agents/child-agent.mcs.yml",
    "topic":        f"{_MS_REPO_RAW}/templates/topics/question-topic.topic.mcs.yml",
    "greeting":     f"{_MS_REPO_RAW}/templates/topics/greeting.topic.mcs.yml",
    "fallback":     f"{_MS_REPO_RAW}/templates/topics/fallback.topic.mcs.yml",
    "mcp_action":   f"{_MS_REPO_RAW}/templates/actions/mcp-action.mcs.yml",
    "variable":     f"{_MS_REPO_RAW}/templates/variables/global-variable.variable.mcs.yml",
}

_MS_SCHEMA_URL = f"{_MS_REPO_RAW}/reference/bot.schema.yaml-authoring.json"

_DEFAULT_MODEL_HINT = "Sonnet46"

def _cache_dir():
    here = os.path.dirname(os.path.abspath(__file__))
    base = os.path.dirname(here)  # the brainstem dir
    d = os.path.join(base, ".brainstem_data", "cs_forge_cache")
    os.makedirs(d, exist_ok=True)
    return d

def _cached_or_fetch(name, url, ttl_seconds=86400):
    """Fetch a small text resource, cache it under .brainstem_data/cs_forge_cache.
    Returns (text, source) where source is 'cache' or 'fetch'.
    Falls back to last cached copy on network failure."""
    path = os.path.join(_cache_dir(), name)
    fresh = (os.path.exists(path)
             and (time.time() - os.path.getmtime(path)) < ttl_seconds)
    if fresh:
        with open(path) as f:
            return f.read(), "cache"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "RAPP-CS-Forge/0.1"})
        body = urllib.request.urlopen(req, timeout=12).read().decode("utf-8")
        with open(path, "w") as f:
            f.write(body)
        return body, "fetch"
    except Exception as e:
        if os.path.exists(path):
            with open(path) as f:
                return f.read(), f"cache (stale; fetch failed: {e})"
        raise

def _ensure_templates():
    """Pull all MS templates + schema into the cache. Returns dict of cached paths."""
    paths = {}
    for key, url in _MS_TEMPLATES.items():
        _cached_or_fetch(f"template_{key}.yml", url)
        paths[key] = os.path.join(_cache_dir(), f"template_{key}.yml")
    _cached_or_fetch("bot.schema.yaml-authoring.json", _MS_SCHEMA_URL)
    paths["schema"] = os.path.join(_cache_dir(), "bot.schema.yaml-authoring.json")
    return paths

def _short_hash(s, n=6):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:n]

def _node_id(prefix, content):
    """Generate a deterministic CS node id like 'sendMessage_a1b2c3'.
    CS node ids must be unique within a topic; deriving from content
    keeps re-forges of the same swarm stable (good for diffing)."""
    return f"{prefix}_{_short_hash(content, 8)}"

def _pascal(s):
    parts = re.split(r"[\s_\-]+", s.strip())
    return "".join(p[:1].upper() + p[1:] for p in parts if p)

def _slug(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-") or "swarm"

def _yaml_block_scalar(text, indent=4):
    """Render a multi-line string as a YAML block scalar (`|` form).
    CS instructions blocks always use `|` — preserves newlines verbatim."""
    if text is None:
        text = ""
    pad = " " * indent
    lines = text.replace("\r\n", "\n").split("\n")
    return "\n".join(pad + ln for ln in lines)

def _yaml_quote(s):
    """Quote a YAML scalar safely. We intentionally do NOT use the PyYAML
    dump — too many style flags. CS YAML is hand-written by Microsoft and
    we mirror that style."""
    if s is None:
        return '""'
    if not isinstance(s, str):
        s = str(s)
    if any(c in s for c in [":", "#", "{", "}", "[", "]", ",", "&", "*", "!", "|", ">", "'", '"', "%", "@", "`"]):
        return json.dumps(s, ensure_ascii=False)
    if s.strip() != s or not s:
        return json.dumps(s, ensure_ascii=False)
    return s

class _PersonaInfo:
    """One persona discovered in the singleton:
       - kind: 'leaf' (pure-prompt) | 'composite' | 'public'
       - name: class name (without _Internal prefix)
       - soul: the SOUL constant text, if leaf
       - calls: list of other personas this one delegates to (composite/public)
       - description: from metadata
       - parameters: from metadata
       - python_compute: True if perform() does work beyond _llm_call/persona dispatch
       - python_summary: short description of what the Python does (for MCP stub)"""

    def __init__(self, name):
        self.name = name
        self.kind = "leaf"
        self.soul = None
        self.calls = []
        self.description = ""
        self.parameters = {"type": "object", "properties": {}, "required": []}
        self.python_compute = False
        self.python_summary = ""

def _extract_personas(tree, src):
    """Walk the AST, return:
        souls: dict[soul_const_name] -> string
        personas: list[_PersonaInfo] in source order
        public_class_name: name of the BasicAgent subclass NOT prefixed _Internal
                           and NOT BasicAgent itself"""
    souls = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id.startswith("_SOUL_"):
                    if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                        souls[t.id] = node.value.value
                    elif isinstance(node.value, ast.JoinedStr):  # f-string
                        souls[t.id] = "".join(
                            v.value for v in node.value.values
                            if isinstance(v, ast.Constant) and isinstance(v.value, str)
                        )

    personas = []
    public_class_name = None

    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        if node.name == "BasicAgent":
            continue
        # Skip the alias class (Foo(FooParent): pass) — those are duplicates
        if (len(node.body) == 1 and isinstance(node.body[0], ast.Pass)):
            continue

        is_internal = node.name.startswith("_Internal")
        is_basic_agent = any(
            (isinstance(b, ast.Name) and b.id == "BasicAgent") or
            (isinstance(b, ast.Attribute) and b.attr == "BasicAgent")
            for b in node.bases
        )
        # Public class: not internal, AND extends BasicAgent (or some BasicAgent subclass)
        if not is_internal and is_basic_agent:
            public_class_name = node.name

        info = _PersonaInfo(node.name.replace("_Internal", "", 1) if is_internal else node.name)

        # Mine metadata.description and parameters from __init__
        for sub in ast.walk(node):
            if isinstance(sub, ast.Assign):
                for t in sub.targets:
                    if (isinstance(t, ast.Attribute)
                            and isinstance(t.value, ast.Name)
                            and t.value.id == "self"
                            and t.attr == "metadata"):
                        # self.metadata = {...}
                        if isinstance(sub.value, ast.Dict):
                            for k, v in zip(sub.value.keys, sub.value.values):
                                if not isinstance(k, ast.Constant):
                                    continue
                                if k.value == "description":
                                    if isinstance(v, ast.Constant):
                                        info.description = v.value
                                    elif isinstance(v, ast.JoinedStr):
                                        info.description = "".join(
                                            x.value for x in v.values
                                            if isinstance(x, ast.Constant) and isinstance(x.value, str)
                                        )
                                elif k.value == "parameters":
                                    try:
                                        info.parameters = ast.literal_eval(v)
                                    except Exception:
                                        pass

        # Mine perform() body to classify leaf vs composite vs python-compute
        perform_node = next((m for m in node.body
                             if isinstance(m, ast.FunctionDef) and m.name == "perform"),
                            None)
        if perform_node:
            soul_used = None
            persona_calls = []
            other_compute_kinds = set()
            for sub in ast.walk(perform_node):
                # _llm_call(_SOUL_X, ...)
                if (isinstance(sub, ast.Call)
                        and isinstance(sub.func, ast.Name)
                        and sub.func.id == "_llm_call"
                        and sub.args
                        and isinstance(sub.args[0], ast.Name)
                        and sub.args[0].id.startswith("_SOUL_")):
                    soul_used = sub.args[0].id
                # _InternalX().perform(...)  → composite call
                elif (isinstance(sub, ast.Call)
                        and isinstance(sub.func, ast.Attribute)
                        and sub.func.attr == "perform"
                        and isinstance(sub.func.value, ast.Call)
                        and isinstance(sub.func.value.func, ast.Name)
                        and sub.func.value.func.id.startswith("_Internal")):
                    persona_calls.append(sub.func.value.func.id.replace("_Internal", "", 1))
                # File ops, urllib, regex, json — irreducible Python
                elif isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute):
                    nm = sub.func.attr
                    if nm in ("makedirs", "open", "write", "urlopen", "search",
                              "match", "sub", "findall", "loads", "dumps", "remove"):
                        other_compute_kinds.add(nm)
                elif isinstance(sub, ast.With) or isinstance(sub, ast.For):
                    other_compute_kinds.add("control-flow")

            if soul_used and not persona_calls:
                info.kind = "leaf"
                info.soul = souls.get(soul_used, "")
            elif persona_calls and not soul_used:
                info.kind = "composite"
                info.calls = persona_calls
            elif persona_calls and soul_used:
                # Mixed — treat as composite, note the soul as fallback instructions
                info.kind = "composite"
                info.calls = persona_calls
                info.soul = souls.get(soul_used, "")
            else:
                # No soul, no persona calls — pure python (or trivial wrapper)
                info.kind = "leaf"

            if other_compute_kinds:
                info.python_compute = True
                info.python_summary = ", ".join(sorted(other_compute_kinds))

        personas.append(info)

    return souls, personas, public_class_name

def _emit_root_agent(public_name, display_name, instructions, starters):
    """Emit the gpt.default data file in the EXPORT shape (matching the
    botcomponent.../data files Microsoft ships in solution zips like
    enhanced-task-completion). The export shape is much leaner than the
    authoring template:
      - no `mcs.metadata` wrapper (componentName lives on the bot record,
        not the data field)
      - no `displayName` (also on the bot record)
      - no `conversationStarters` at this level
      - `gptCapabilities` + `aISettings.model.modelNameHint` + an
        `extensionData.lastUsedCustomModel` placeholder
    Display name + conversation starters are still useful — but they
    belong on the bot record itself, set during deploy, not in this YAML."""
    out = [
        "kind: GptComponentMetadata",
        "instructions: |",
        _yaml_block_scalar(instructions, indent=2),
        "gptCapabilities:",
        "  webBrowsing: true",
        "  codeInterpreter: true",
        "",
        "aISettings:",
        "  model:",
        f"    modelNameHint: {_DEFAULT_MODEL_HINT}",
        "",
        "  extensionData:",
        "    lastUsedCustomModel: {}",
    ]
    return "\n".join(out) + "\n"

def _emit_child_agent(persona):
    instructions = persona.soul or (
        f"You are the {persona.name} specialist. {persona.description or ''}"
    ).strip()
    description = (
        persona.description
        or f"Specialist that handles {persona.name} work in this pipeline."
    )
    out = [
        f"# Name: {persona.name}",
        f"# {persona.name}",
        "kind: AgentDialog",
        "",
        "beginDialog:",
        "  kind: OnToolSelected",
        "  id: main",
        f"  description: {_yaml_quote(description)}",
        "",
        "settings:",
        "  instructions: |",
        _yaml_block_scalar(instructions, indent=4),
        "",
        "inputType:",
        "  properties:",
        "    Input:",
        "      displayName: Input",
        "      description: Content the parent orchestrator passes to this specialist.",
        "      type: String",
        "",
        "outputType:",
        "  properties:",
        "    Result:",
        "      displayName: Result",
        f"      description: The {persona.name} specialist's output.",
        "      type: String",
    ]
    return "\n".join(out) + "\n"

def _emit_mcp_action_stub(action_name, description, op_id):
    """Stub template for irreducible Python compute. User must wire up
    the connection reference to a real MCP server (e.g. a brainstem
    exposed via the documented MCP-action protocol)."""
    out = [
        f"# Name: {action_name}",
        f"# {description}",
        "kind: TaskDialog",
        f"modelDisplayName: {_yaml_quote(action_name)}",
        f"modelDescription: {_yaml_quote(description)}",
        "action:",
        "  kind: InvokeExternalAgentTaskAction",
        "  connectionReference: REPLACE_WITH_MCP_CONNECTION_REFERENCE",
        "  connectionProperties:",
        "    mode: Invoker",
        "  operationDetails:",
        "    kind: ModelContextProtocolMetadata",
        f"    operationId: {_yaml_quote(op_id)}",
    ]
    return "\n".join(out) + "\n"

def _emit_global_variable(name, default, description, schema_prefix):
    out = [
        f"# Name: {name}",
        f"# {description}",
        f"name: {_yaml_quote(name)}",
        "aIVisibility: UseInAIContext",
        "scope: Conversation",
        f"description: {_yaml_quote(description)}",
        f"schemaName: {schema_prefix}.globalvariable.{name}",
        "kind: GlobalVariableComponent",
        f"defaultValue: {_yaml_quote(default if default is not None else '')}",
    ]
    return "\n".join(out) + "\n"

def _emit_conn_json_placeholder():
    """Microsoft's validate skill expects .mcs/conn.json with tenant/env URLs.
    We emit a placeholder so users see exactly what to fill in."""
    return json.dumps({
        "tenantId": "REPLACE_WITH_TENANT_ID",
        "environmentId": "REPLACE_WITH_ENVIRONMENT_ID",
        "environmentUrl": "https://REPLACE.crm.dynamics.com",
        "agentMgmtUrl": "https://REPLACE.api.powerplatform.com"
    }, indent=2) + "\n"

def _synthesize_pipeline_instructions(public_name, top_persona, leaves_in_order,
                                      composites_index):
    """Mechanical synthesis of root-agent instructions from the public class's
    perform() body. We list children in the order their _Internal*().perform()
    calls appear in the AST, with the composite expansions inlined.

    The instructions tell the orchestrator: 'when the user asks for X, do
    these things in order, calling the specialist children for each step.'
    Generative orchestration handles the routing — but with explicit ordering
    it stays stable across runs."""
    sequence = []
    visited = set()

    def expand(name):
        if name in visited:
            return
        visited.add(name)
        if name in composites_index:
            for sub in composites_index[name].calls:
                expand(sub)
        else:
            sequence.append(name)

    for name in top_persona.calls:
        expand(name)

    # Description first sentence, then the pipeline.
    intro = (top_persona.description
             or f"You are {public_name}, an orchestrator that runs a multi-step pipeline.")

    if not sequence:
        return intro + "\n\nFollow the user's request directly."

    lines = [intro, ""]
    lines.append("Pipeline (call each child agent in this order, passing the previous result forward):")
    for i, step in enumerate(sequence, 1):
        lines.append(f"  {i}. Route to the {step} child agent.")
    lines.append("")
    lines.append(
        "Always run the full pipeline. Do not skip steps. After the final child "
        "returns, present the user with the final artifact and a concise summary."
    )
    return "\n".join(lines)

def _try_validate_schema(workspace_path):
    """Best-effort offline schema validation of all .mcs.yml files in the
    workspace against bot.schema.yaml-authoring.json.

    The MS authoring schema's top-level `oneOf` only covers AdaptiveDialog +
    TaskDialog. The other kinds we emit (GptComponentMetadata, AgentDialog,
    GlobalVariableComponent) live in `#/definitions/<Kind>` and must be
    referenced directly. So we read each file's `kind:` and validate against
    the matching definition. Files with a kind not present in definitions
    are reported as 'skipped_kind' rather than a misleading top-level error.

    Returns dict with:
      ok: bool, files: int, validated: int, skipped: int,
      errors: [{file, message}], skipped_files: [{file, reason}],
      skipped_reason: str  (set only when whole validation was skipped)"""
    schema_path = os.path.join(_cache_dir(), "bot.schema.yaml-authoring.json")
    if not os.path.exists(schema_path):
        return {"ok": None, "files": 0, "validated": 0, "skipped": 0,
                "errors": [], "skipped_files": [],
                "skipped_reason": "MS schema not cached; run action='refresh' first."}
    try:
        import yaml  # PyYAML
    except ImportError:
        return {"ok": None, "files": 0, "validated": 0, "skipped": 0,
                "errors": [], "skipped_files": [],
                "skipped_reason": "PyYAML not installed; pip install pyyaml to validate."}
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        return {"ok": None, "files": 0, "validated": 0, "skipped": 0,
                "errors": [], "skipped_files": [],
                "skipped_reason": "jsonschema not installed; pip install jsonschema to validate."}

    with open(schema_path) as f:
        schema = json.load(f)
    definitions = schema.get("definitions", schema.get("$defs", {}))

    files = []
    for root, _, fnames in os.walk(workspace_path):
        for fn in fnames:
            if fn.endswith(".mcs.yml"):
                files.append(os.path.join(root, fn))

    errors = []
    skipped_files = []
    validated = 0
    for fp in files:
        rel = os.path.relpath(fp, workspace_path)
        try:
            with open(fp) as f:
                doc = yaml.safe_load(f)
        except Exception as e:
            errors.append({"file": rel, "message": f"YAML parse error: {e}"[:300]})
            continue

        # Pick the definition by kind. Root agents have `kind:` at top; some
        # files embed it under a sub-key (mcs.metadata is a wrapper but kind
        # is still top-level in the templates we emit).
        kind = (doc or {}).get("kind") if isinstance(doc, dict) else None
        if not kind:
            skipped_files.append({"file": rel, "reason": "no top-level 'kind:' field"})
            continue
        if kind not in definitions:
            skipped_files.append({"file": rel,
                                  "reason": f"kind '{kind}' not in MS schema definitions"})
            continue

        # Known limitation: bot.schema.yaml-authoring.json's definitions for
        # GptComponentMetadata and AgentDialog have `additionalProperties: false`
        # but omit fields used by Microsoft's own templates (displayName,
        # aISettings, mcs.metadata). The canonical validator is
        # manage-agent.bundle.js (LSP) which has the full coverage. For these
        # kinds we do a shape check instead of full schema validation, and
        # tell the user to run the MS LSP for canonical validation.
        partial_schema_kinds = {"GptComponentMetadata", "AgentDialog"}
        if kind in partial_schema_kinds:
            required = {
                "GptComponentMetadata": ["kind"],
                "AgentDialog":          ["kind", "beginDialog"],
            }[kind]
            missing = [k for k in required if k not in doc]
            if missing:
                errors.append({
                    "file": rel, "kind": kind,
                    "message": f"shape check: missing required keys {missing}",
                })
            else:
                skipped_files.append({
                    "file": rel,
                    "reason": (f"kind '{kind}' passed shape check; offline schema "
                               f"is partial for this kind — run "
                               f"manage-agent.bundle.js validate for canonical check"),
                })
            continue

        try:
            sub_schema = {"$ref": f"#/definitions/{kind}", "definitions": definitions}
            jsonschema.validate(instance=doc, schema=sub_schema)
            validated += 1
        except Exception as e:
            errors.append({"file": rel, "kind": kind,
                           "message": str(e).split("\n")[0][:300]})
    return {"ok": (not errors), "files": len(files),
            "validated": validated, "skipped": len(skipped_files),
            "errors": errors, "skipped_files": skipped_files,
            "skipped_reason": ""}

def _zip_workspace(workspace_path):
    zip_path = workspace_path.rstrip("/") + ".zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, fnames in os.walk(workspace_path):
            for fn in fnames:
                full = os.path.join(root, fn)
                arc = os.path.relpath(full, os.path.dirname(workspace_path))
                zf.write(full, arc)
    return zip_path

def _resolve_singleton(swarm_name, agent_filename, agents_dir):
    """Find the singleton .py for the requested swarm. Returns (path, source)
    where source is 'local' or 'error'."""
    if agent_filename:
        candidate = agent_filename if os.path.isabs(agent_filename) \
            else os.path.join(agents_dir, agent_filename)
        if os.path.exists(candidate):
            return candidate, "local"
        return None, f"agent_filename not found: {candidate}"

    if not swarm_name:
        return None, "Provide swarm_name (e.g. 'BookFactory') or agent_filename."

    # Match against installed agents/<slug>_agent.py
    target = re.sub(r"[^a-z0-9]", "", swarm_name.lower())
    for fp in sorted(glob.glob(os.path.join(agents_dir, "*_agent.py"))):
        fname = os.path.basename(fp)
        stem = fname.replace("_agent.py", "").replace("_", "").replace("-", "")
        if stem == target:
            return fp, "local"
    return None, (
        f"No installed agent matching '{swarm_name}'. Use SwarmFactory.install "
        f"or SwarmFactory.list to add it first."
    )

class _ForgeEngine(_EngineBase):
    def __init__(self):
        self.name = "CopilotStudioForge"
        self.metadata = {
            "name": self.name,
            "description": (
                "Translate a RAPP swarm into a native Microsoft Copilot Studio "
                "YAML bundle (anchored on microsoft/skills-for-copilot-studio "
                "templates + schema). Emits a validated .zip ready for import "
                "via the Copilot Studio VS Code extension or pac CLI.\n\n"
                "TRANSLATION RULES (deterministic, LLM-free):\n"
                " • Pure-prompt persona (just _llm_call(SOUL, input)) → child "
                "agent (AgentDialog) with instructions=SOUL.\n"
                " • Composite persona (delegates to other personas) → folded "
                "into root agent's instructions as ordered pipeline steps.\n"
                " • Public class → root agent (GptComponentMetadata) with "
                "instructions synthesized from the perform() call sequence.\n"
                " • Python compute (file writes, regex, urllib, json parse) → "
                "mcp-action.mcs.yml STUB flagged for user wiring.\n"
                " • The forge does NOT push to a Copilot Studio environment. "
                "Push/pull/clone require the VS Code Copilot Studio extension "
                "or pac CLI with tenant creds — that's a separate confirmed step.\n\n"
                "Actions:\n"
                " • 'forge'    — translate + write bundle + zip\n"
                " • 'inspect'  — dry-run; report what would be emitted\n"
                " • 'validate' — schema-validate an emitted bundle\n"
                " • 'list'     — show forge-able installed agents\n"
                " • 'refresh'  — re-fetch MS templates + schema (cached 24h by default)"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["forge", "inspect", "validate", "list", "refresh"],
                        "description": "forge | inspect | validate | list | refresh"
                    },
                    "swarm_name": {
                        "type": "string",
                        "description": "Display/PascalCase name of the installed swarm to forge (e.g. 'BookFactory'). The forge resolves this against agents/*_agent.py."
                    },
                    "agent_filename": {
                        "type": "string",
                        "description": "Optional explicit path or filename of a singleton .py to forge. Wins over swarm_name when both are set."
                    },
                    "display_name": {
                        "type": "string",
                        "description": "Human-readable name shown in Copilot Studio. Defaults to the public class name."
                    },
                    "schema_prefix": {
                        "type": "string",
                        "description": "Schema prefix (publisher namespace) for variable schemaNames. Defaults to 'rapp' — set to your Power Platform publisher prefix for production use."
                    },
                    "path": {
                        "type": "string",
                        "description": "For action='validate': absolute path to a forged bundle directory."
                    }
                },
                "required": ["action"]
            }
        }
        super().__init__(self.name, self.metadata)

    # ─── action handlers ───────────────────────────────────────────────

    def _list(self):
        agents_dir = os.environ.get(
            "AGENTS_PATH",
            os.path.join(os.path.dirname(os.path.abspath(__file__))))
        targets = []
        for fp in sorted(glob.glob(os.path.join(agents_dir, "*_agent.py"))):
            fname = os.path.basename(fp)
            if fname == "basic_agent.py":
                continue
            try:
                with open(fp) as f:
                    src = f.read()
                tree = ast.parse(src, filename=fname)
                souls, personas, public_name = _extract_personas(tree, src)
                if not personas:
                    continue
                leaves = sum(1 for p in personas if p.kind == "leaf")
                composites = sum(1 for p in personas if p.kind == "composite")
                py_compute = sum(1 for p in personas if p.python_compute)
                targets.append({
                    "filename": fname,
                    "public_class": public_name,
                    "personas_total": len(personas),
                    "leaves_pure_prompt": leaves,
                    "composites": composites,
                    "personas_with_python_compute": py_compute,
                    "estimated_native_pct": (
                        round(100 * leaves / max(1, len(personas)), 1)
                        if personas else 0
                    ),
                })
            except Exception as e:
                targets.append({"filename": fname, "error": str(e)[:200]})
        return json.dumps({
            "status": "ok",
            "action": "list",
            "count": len(targets),
            "targets": targets,
        })

    def _refresh(self):
        try:
            paths = _ensure_templates()
        except Exception as e:
            return json.dumps({"status": "error",
                               "message": f"Failed to refresh MS templates: {e}"})
        sizes = {k: os.path.getsize(v) for k, v in paths.items() if os.path.exists(v)}
        return json.dumps({
            "status": "ok",
            "action": "refresh",
            "cache_dir": _cache_dir(),
            "templates_cached": list(sizes.keys()),
            "sizes_bytes": sizes,
            "message": f"MS templates + schema cached at {_cache_dir()}.",
        })

    def _validate(self, path):
        if not path or not os.path.isdir(path):
            return json.dumps({"status": "error",
                               "message": f"validate requires path= an existing forged bundle dir. Got: {path!r}"})
        result = _try_validate_schema(path)
        return json.dumps({
            "status": "ok",
            "action": "validate",
            "path": path,
            "validation": result,
        })

    def _forge_or_inspect(self, action, swarm_name, agent_filename,
                         display_name, schema_prefix):
        agents_dir = os.environ.get(
            "AGENTS_PATH",
            os.path.join(os.path.dirname(os.path.abspath(__file__))))
        path, source = _resolve_singleton(swarm_name, agent_filename, agents_dir)
        if not path:
            return json.dumps({"status": "error", "message": source})

        try:
            with open(path) as f:
                src = f.read()
            tree = ast.parse(src, filename=os.path.basename(path))
        except Exception as e:
            return json.dumps({"status": "error",
                               "message": f"Could not parse {path}: {e}"})

        souls, personas, public_class_name = _extract_personas(tree, src)
        if not personas:
            return json.dumps({"status": "error",
                               "message": f"No personas/agent classes found in {path}."})
        if not public_class_name:
            return json.dumps({"status": "error",
                               "message": (
                                   "Could not identify the public class (must extend "
                                   "BasicAgent and not be _Internal-prefixed)."
                               )})

        # Identify top persona (the public one) and split internals
        top = next((p for p in personas if p.name == public_class_name), None)
        if not top:
            top = personas[-1]  # fallback: last class is usually the public one

        composites_index = {p.name: p for p in personas
                            if p.kind == "composite" and p.name != public_class_name}

        leaves = [p for p in personas
                  if p.kind == "leaf" and p.name != public_class_name]

        # Native vs MCP-action breakdown
        native_count = len(leaves)
        mcp_action_personas = [p for p in personas
                               if p.python_compute and p.name != public_class_name]
        mcp_action_count = len(mcp_action_personas)

        display = display_name or public_class_name
        prefix = schema_prefix or _DEFAULT_PUBLISHER_PREFIX
        slug = _slug(public_class_name)
        bundle_id = f"{slug}-{_short_hash(src, 6)}"

        # Compose root agent instructions
        instructions = _synthesize_pipeline_instructions(
            public_class_name, top, leaves, composites_index
        )

        # Plan output
        plan = {
            "bundle_id": bundle_id,
            "root_agent": {
                "componentName": public_class_name,
                "displayName": display,
                "instructions_preview": instructions[:600],
                "model": _DEFAULT_MODEL_HINT,
            },
            "child_agents": [
                {"name": p.name,
                 "soul_present": bool(p.soul),
                 "description": p.description[:200]}
                for p in leaves
            ],
            "mcp_action_stubs": [
                {"name": p.name + "MCPAction",
                 "reason_python_compute": p.python_summary or "perform() does Python work",
                 "operation_id": f"{prefix}_{slug}_{_slug(p.name)}"}
                for p in mcp_action_personas
            ],
            "stats": {
                "personas_total": len(personas) - 1,  # exclude public
                "child_agents_native": native_count,
                "mcp_action_stubs": mcp_action_count,
                "native_pct": (
                    round(100 * native_count / max(1, native_count + mcp_action_count), 1)
                ),
            },
        }

        if action == "inspect":
            return json.dumps({
                "status": "ok",
                "action": "inspect",
                "source_path": path,
                "plan": plan,
                "message": (
                    f"Inspect complete. {native_count} native child agent(s), "
                    f"{mcp_action_count} MCP-action stub(s). No files written."
                ),
            })

        # Action == 'forge': make sure templates are cached, then write files
        try:
            _ensure_templates()
        except Exception as e:
            # Non-fatal: forge still works without templates because we emit
            # YAML directly. We just won't be able to schema-validate.
            plan["templates_warning"] = f"Could not refresh MS templates: {e}"

        brainstem_dir = os.path.dirname(agents_dir.rstrip("/"))
        forged_root = os.path.join(brainstem_dir, ".brainstem_data", "forged")
        os.makedirs(forged_root, exist_ok=True)
        workspace = os.path.join(forged_root, bundle_id)
        if os.path.exists(workspace):
            # Re-forging the same source; clean it.
            import shutil
            shutil.rmtree(workspace)
        os.makedirs(workspace)
        os.makedirs(os.path.join(workspace, "agents"))
        os.makedirs(os.path.join(workspace, "topics"))
        os.makedirs(os.path.join(workspace, "actions"))
        os.makedirs(os.path.join(workspace, "variables"))
        os.makedirs(os.path.join(workspace, ".mcs"))

        # Root agent
        starters = [
            {"title": "Get Started",
             "text": f"How does {display} work?"},
            {"title": "Run the pipeline",
             "text": f"Run {display} on this input: ..."},
        ]
        with open(os.path.join(workspace, "agent.mcs.yml"), "w") as f:
            f.write(_emit_root_agent(public_class_name, display, instructions, starters))

        # Child agents
        for p in leaves:
            child_dir = os.path.join(workspace, "agents", p.name)
            os.makedirs(child_dir, exist_ok=True)
            with open(os.path.join(child_dir, "agent.mcs.yml"), "w") as f:
                f.write(_emit_child_agent(p))

        # MCP-action stubs
        for p in mcp_action_personas:
            op_id = f"{prefix}_{slug}_{_slug(p.name)}"
            stub_path = os.path.join(workspace, "actions", f"{p.name}_mcp.mcs.yml")
            description = (
                f"Irreducible Python compute from {p.name}.perform() "
                f"({p.python_summary or 'computation'}). "
                f"Wire connectionReference to a brainstem MCP server exposing "
                f"the {op_id} operation."
            )
            with open(stub_path, "w") as f:
                f.write(_emit_mcp_action_stub(p.name + "MCPAction", description, op_id))

        # Conn placeholder (so the user can fill in tenant/env and run MS validators)
        with open(os.path.join(workspace, ".mcs", "conn.json"), "w") as f:
            f.write(_emit_conn_json_placeholder())

        # README inside the bundle so a human inspecting it knows the provenance
        readme = (
            f"# {display} — forged Copilot Studio bundle\n\n"
            f"Generated from: {os.path.basename(path)}\n"
            f"Source SHA-256 (first 16): {_short_hash(src, 16)}\n"
            f"Bundle id: {bundle_id}\n\n"
            f"## Native vs MCP-action\n"
            f"- Native child agents: {native_count}\n"
            f"- MCP-action stubs to wire up: {mcp_action_count}\n"
            f"- Native %: {plan['stats']['native_pct']}\n\n"
            f"## Layout\n"
            f"- `agent.mcs.yml` — root orchestrator\n"
            f"- `agents/<Persona>/agent.mcs.yml` — child agents (one per pure-prompt persona)\n"
            f"- `actions/*_mcp.mcs.yml` — MCP-action stubs (replace `connectionReference`)\n"
            f"- `.mcs/conn.json` — fill tenant/environment for MS validate scripts\n\n"
            f"## Next steps\n"
            f"1. Fill `.mcs/conn.json` with your Power Platform tenant/environment.\n"
            f"2. Wire each MCP-action stub's `connectionReference` to a real connector.\n"
            f"3. Validate: `node manage-agent.bundle.js validate --workspace <this-dir> ...`\n"
            f"   (requires a clone of microsoft/skills-for-copilot-studio).\n"
            f"4. Push via the Copilot Studio VS Code extension or pac CLI.\n"
        )
        with open(os.path.join(workspace, "README.md"), "w") as f:
            f.write(readme)

        # Schema validation (best effort)
        validation = _try_validate_schema(workspace)

        # Zip
        zip_path = _zip_workspace(workspace)

        return json.dumps({
            "status": "ok",
            "action": "forge",
            "source_path": path,
            "bundle_dir": workspace,
            "bundle_zip": zip_path,
            "bundle_zip_bytes": os.path.getsize(zip_path),
            "plan": plan,
            "validation": validation,
            "message": (
                f"Forged {display} → {os.path.basename(zip_path)} "
                f"({plan['stats']['native_pct']}% native, "
                f"{mcp_action_count} MCP-action stub(s) need wiring). "
                f"Bundle dir: {workspace}"
            ),
        })

    # ─── dispatch ─────────────────────────────────────────────────────

    def run(self, action="list", swarm_name="", agent_filename="",
                display_name="", schema_prefix="rapp", path="", **kwargs):
        if action == "list":
            return self._list()
        if action == "refresh":
            return self._refresh()
        if action == "validate":
            return self._validate(path)
        if action in ("forge", "inspect"):
            return self._forge_or_inspect(action, swarm_name, agent_filename,
                                          display_name, schema_prefix)
        return json.dumps({"status": "error",
                           "message": f"Unknown action {action!r}. "
                                      f"Use forge | inspect | validate | list | refresh."})

class _Scanner:
    """Walk a directory of RAPP *_agent.py files and extract the bits the
    wizard needs: class name, manifest, description, storage usage, URL
    constants. From those signals we pick a default topic pattern.
    """

    SKIP = {"basic_agent.py"}

    def scan(self, agents_dir):
        agents_dir = Path(agents_dir)
        if not agents_dir.is_dir():
            return {"status": "error",
                    "message": f"agents_dir not found: {agents_dir}"}
        results = []
        for path in sorted(agents_dir.glob("*_agent.py")):
            if path.name in self.SKIP:
                continue
            try:
                src = path.read_text(encoding="utf-8")
                tree = ast.parse(src, filename=str(path))
            except (OSError, SyntaxError) as e:
                results.append({"path": str(path), "error": str(e)})
                continue
            results.append(self._extract(path, src, tree))
        return {"status": "ok",
                "agents_dir": str(agents_dir),
                "count": len(results),
                "agents": results}

    def _extract(self, path, src, tree):
        info = {
            "path": str(path),
            "filename": path.name,
            "class_name": None,
            "agent_name": None,
            "description": None,
            "manifest_description": None,
            "uses_storage": False,
            "uses_urls": [],
            "default_pattern": "topic-only",
            "default_trigger_queries": [],
            "default_display_name": "",
            "default_intent_name": "",
        }
        # Manifest first — pure literal, safest source of description.
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name) and t.id == "__manifest__":
                        try:
                            m = ast.literal_eval(node.value)
                            info["manifest_description"] = m.get("description")
                        except (ValueError, SyntaxError):
                            pass
        # Class + storage signal
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and not info["class_name"]:
                info["class_name"] = node.name
                for m in node.body:
                    if isinstance(m, ast.FunctionDef) and m.name == "__init__":
                        for stmt in m.body:
                            self._sniff_init_assign(stmt, info)
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                seg = ast.get_source_segment(src, node) or ""
                if "AzureFileStorageManager" in seg or "storage_manager" in seg.lower():
                    info["uses_storage"] = True
        # URL constants anywhere in the module
        for n in ast.walk(tree):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) \
                    and n.value.startswith(("http://", "https://")):
                info["uses_urls"].append(n.value)
        info["uses_urls"] = sorted(set(info["uses_urls"]))
        # Default pattern + naming
        self._fill_defaults(info)
        return info

    def _sniff_init_assign(self, stmt, info):
        if not isinstance(stmt, ast.Assign):
            return
        for tgt in stmt.targets:
            if not (isinstance(tgt, ast.Attribute) and isinstance(tgt.value, ast.Name)
                    and tgt.value.id == "self"):
                continue
            if tgt.attr == "name":
                try:
                    info["agent_name"] = ast.literal_eval(stmt.value)
                except (ValueError, SyntaxError):
                    pass
            elif tgt.attr == "metadata":
                try:
                    md = ast.literal_eval(stmt.value)
                    info["description"] = md.get("description")
                except (ValueError, SyntaxError):
                    pass

    def _fill_defaults(self, info):
        """Pick the most likely topic pattern + name defaults for this
        agent. The wizard surfaces these as the pre-filled values — the
        human can override anything before generating."""
        cls = (info.get("class_name") or "").lower()
        name = (info.get("agent_name") or "").lower()
        desc = (info.get("description") or info.get("manifest_description") or "").lower()
        urls = info.get("uses_urls") or []
        blob = cls + " " + name + " " + desc

        # Pattern detection — same heuristic the factory's policy uses,
        # exposed here so the human can see (and override) the choice.
        if info.get("uses_storage") and any(k in blob for k in
                                            ("save", "store", "remember", "manage memory", "managememory", "write")):
            info["default_pattern"] = "memory-save"
        elif info.get("uses_storage") and any(k in blob for k in
                                              ("recall", "read", "context", "memory")):
            info["default_pattern"] = "memory-recall"
        elif urls and not info.get("uses_storage"):
            info["default_pattern"] = "web-browse"
        else:
            info["default_pattern"] = "topic-only"

        # Display name: humanize the class name
        info["default_intent_name"] = _humanize(info["class_name"] or "Topic")
        info["default_display_name"] = info["default_intent_name"]

        # Trigger queries: lean on description for the headline phrasing
        info["default_trigger_queries"] = _seed_triggers(
            info["default_intent_name"],
            info.get("manifest_description") or info.get("description") or "",
            info["default_pattern"],
        )

def _humanize(camel):
    """HackerNewsAgent → 'Hacker News'; ContextMemoryAgent → 'Context Memory'."""
    if not camel:
        return "Topic"
    s = re.sub(r"([a-z])([A-Z])", r"\1 \2", camel)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", s)
    s = s.replace("_", " ").strip()
    if s.endswith(" Agent"):
        s = s[:-6]
    return re.sub(r"\s+", " ", s)

def _seed_triggers(intent, description, pattern):
    """Produce 4–6 trigger phrases that feel natural for the intent.
    Deterministic — the wizard pre-fills these and the human edits."""
    base = [intent]
    desc = (description or "").strip()
    if desc:
        # Use the first 8-ish words of the description as one trigger
        snippet = " ".join(desc.split()[:8]).rstrip(".,;")
        base.append(snippet)
    pattern_extras = {
        "memory-save": ["Remember that", "Save this", "Note that", "Don't forget that"],
        "memory-recall": ["What do you remember", "Recall my memories", "What did I tell you",
                          "List my memories"],
        "web-browse": [f"What's on {intent}", f"Show me {intent.lower()}", f"Latest from {intent}"],
        "topic-only": [intent.lower(), f"Tell me about {intent.lower()}"],
    }
    base.extend(pattern_extras.get(pattern, []))
    # Dedupe preserving order
    seen, out = set(), []
    for b in base:
        if b and b not in seen:
            seen.add(b); out.append(b)
    return out[:6]

def _yaml_str(s):
    """Single-line YAML scalar — quotes if needed."""
    if s is None:
        return '""'
    s = str(s)
    if any(c in s for c in ':#&*!|>\'"\n') or s.strip() != s:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s

def _bullets(items, indent=6):
    """Render a YAML list as joined lines with the given column indent."""
    pad = " " * indent
    return "\n".join(f"{pad}- {_yaml_str(i)}" for i in (items or []))

def _join(*lines):
    """Build a YAML block from individual lines. Blank list items render
    as empty lines. Newlines inside a single item are preserved."""
    out = []
    for ln in lines:
        if ln is None:
            continue
        out.append(ln)
    return "\n".join(out) + "\n"

def _header(component_name, description):
    return _join(
        "mcs.metadata:",
        f"  componentName: {_yaml_str(component_name)}",
        f"  description: {_yaml_str(description)}",
    ).rstrip("\n")

def _intent_block(intent_display_name, trigger_queries):
    return _join(
        "  intent:",
        f"    displayName: {_yaml_str(intent_display_name)}",
        "    includeInOnSelectIntent: true",
        "    triggerQueries:",
        _bullets(trigger_queries, indent=6),
    ).rstrip("\n")

def topic_only_yaml(*, component_name, description, intent_display_name,
                    trigger_queries, response_text):
    return _join(
        _header(component_name, description),
        "kind: AdaptiveDialog",
        "beginDialog:",
        "  kind: OnRecognizedIntent",
        "  id: main",
        _intent_block(intent_display_name, trigger_queries),
        "",
        "  actions:",
        "    - kind: SendActivity",
        "      id: sendMessage_main",
        "      activity:",
        "        text:",
        f"          - {_yaml_str(response_text)}",
        "",
        "    - kind: EndDialog",
        "      id: end_topic",
        "      clearTopicQueue: true",
    )

def web_browse_yaml(*, component_name, description, intent_display_name,
                    trigger_queries, browse_url, format_hint):
    fx = (f'=Concatenate("Fetch ", "{browse_url}", " and {format_hint}. '
          'Use the agent\'s web browsing — do not fabricate.")')
    return _join(
        _header(component_name, description),
        "kind: AdaptiveDialog",
        "beginDialog:",
        "  kind: OnRecognizedIntent",
        "  id: main",
        _intent_block(intent_display_name, trigger_queries),
        "",
        "  actions:",
        "    - kind: SendActivity",
        "      id: sendMessage_fetching",
        "      activity:",
        "        text:",
        f"          - {_yaml_str('Fetching from ' + browse_url + ' ...')}",
        "",
        "    - kind: SearchAndSummarizeContent",
        "      id: search_topic",
        "      variable: Topic.Answer",
        f"      userInput: {fx}",
        "      additionalInstructions: |-",
        "        Use the agent's built-in web browsing capability to read the URL above directly.",
        "        Do not fabricate. If browsing fails, reply exactly:",
        '        "I couldn\'t reach that source just now."',
        "",
        "    - kind: ConditionGroup",
        "      id: condition_answer",
        "      conditions:",
        "        - id: has_answer",
        "          condition: =!IsBlank(Topic.Answer)",
        "          actions:",
        "            - kind: SendActivity",
        "              id: sendMessage_answer",
        '              activity: "{Topic.Answer}"',
        "            - kind: EndDialog",
        "              id: end_topic",
        "              clearTopicQueue: true",
        "",
        "      elseActions:",
        "        - kind: SendActivity",
        "          id: sendMessage_failed",
        "          activity: I couldn't reach that source just now. Try again in a moment.",
    )

def memory_save_yaml(*, component_name, description, intent_display_name,
                     trigger_queries):
    return _join(
        _header(component_name, description),
        "kind: AdaptiveDialog",
        "beginDialog:",
        "  kind: OnRecognizedIntent",
        "  id: main",
        _intent_block(intent_display_name, trigger_queries),
        "",
        "  inputs:",
        "    - kind: AutomaticTaskParameter",
        "      propertyName: content",
        "      parameter:",
        "        description: The content to save to memory. Extract from the user's message.",
        "        displayName: Memory Content",
        "        entity: StringPrebuiltEntity",
        "",
        "    - kind: AutomaticTaskParameter",
        "      propertyName: memory_type",
        "      parameter:",
        "        description: |-",
        "          Classify the memory as one of fact (objective statement),",
        "          preference (like/dislike), insight (observation), task (todo).",
        "          Default to fact.",
        "        displayName: Memory Type",
        "        entity: StringPrebuiltEntity",
        "",
        "  actions:",
        "    - kind: ConditionGroup",
        "      id: condition_have_content",
        "      conditions:",
        "        - id: condition_content_blank",
        "          condition: =IsBlank(Topic.content)",
        "          actions:",
        "            - kind: Question",
        "              id: question_memory_content",
        "              alwaysPrompt: true",
        "              variable: Topic.content",
        "              prompt: What would you like me to remember?",
        "              entity: StringPrebuiltEntity",
        "",
        "    - kind: SetVariable",
        "      id: setVariable_resolved_type",
        "      variable: Topic.ResolvedType",
        '      value: =If(IsBlank(Topic.memory_type) Or Not(Topic.memory_type in ["fact", "preference", "insight", "task"]), "fact", Lower(Topic.memory_type))',
        "",
        "    - kind: SetVariable",
        "      id: setVariable_subject",
        "      variable: Topic.Subject",
        '      value: =Concatenate("RAPP-memory:", Topic.ResolvedType)',
        "",
        "    - kind: InvokeConnectorAction",
        "      id: dvAddNote_RAPP_memory",
        "      connectionReference: shared_commondataserviceforapps",
        "      connectionProperties:",
        "        mode: Maker",
        "      operationId: AddRow",
        "      input:",
        "        binding:",
        '          entityName: ="annotations"',
        "          item/subject: =Topic.Subject",
        "          item/notetext: =Topic.content",
        "      output:",
        "        binding:",
        "          response: Topic.AddResponse",
        "",
        "    - kind: SendActivity",
        "      id: sendMessage_saved",
        "      activity:",
        "        text:",
        "          - 'Saved {Topic.ResolvedType} memory: \"{Topic.content}\"'",
        "",
        "    - kind: EndDialog",
        "      id: end_remember_topic",
        "      clearTopicQueue: true",
    )

def memory_recall_yaml(*, component_name, description, intent_display_name,
                       trigger_queries):
    return _join(
        _header(component_name, description),
        "kind: AdaptiveDialog",
        "beginDialog:",
        "  kind: OnRecognizedIntent",
        "  id: main",
        _intent_block(intent_display_name, trigger_queries),
        "",
        "  inputs:",
        "    - kind: AutomaticTaskParameter",
        "      propertyName: keywords",
        "      parameter:",
        "        description: Optional keywords to filter memories by. Leave blank for full recall.",
        "        displayName: Keyword Filter",
        "        entity: StringPrebuiltEntity",
        "",
        "  actions:",
        "    - kind: SetVariable",
        "      id: setVariable_user_filter",
        "      variable: Topic.UserFilter",
        "      value: =Concatenate(\"_createdby_value eq '\", Text(System.User.Id), \"' and startswith(subject, 'RAPP-memory:')\")",
        "",
        "    - kind: SetVariable",
        "      id: setVariable_final_filter",
        "      variable: Topic.FinalFilter",
        "      value: =If(IsBlank(Topic.keywords), Topic.UserFilter, Concatenate(Topic.UserFilter, \" and contains(notetext, '\", Topic.keywords, \"')\"))",
        "",
        "    - kind: InvokeConnectorAction",
        "      id: dvListNotes_RAPP_memory",
        "      connectionReference: shared_commondataserviceforapps",
        "      connectionProperties:",
        "        mode: Maker",
        "      operationId: ListRows",
        "      input:",
        "        binding:",
        '          entityName: ="annotations"',
        "          $filter: =Topic.FinalFilter",
        '          $orderby: ="createdon desc"',
        '          $select: ="subject,notetext,createdon"',
        "          $top: =50",
        "      output:",
        "        binding:",
        "          response: Topic.ListResponse",
        "",
        "    - kind: ConditionGroup",
        "      id: condition_have_rows",
        "      conditions:",
        "        - id: condition_no_rows",
        "          condition: =IsBlank(Topic.ListResponse) Or IsBlank(Topic.ListResponse.value) Or CountRows(Topic.ListResponse.value) = 0",
        "          actions:",
        "            - kind: SendActivity",
        "              id: sendMessage_no_memories",
        "              activity:",
        "                text:",
        "                  - I don't have any memories stored yet. Tell me something to remember and I'll save it.",
        "",
        "            - kind: EndDialog",
        "              id: end_recall_empty",
        "              clearTopicQueue: true",
        "",
        "    - kind: SendActivity",
        "      id: sendMessage_recall",
        '      activity: "{Topic.ListResponse.value}"',
        "",
        "    - kind: EndDialog",
        "      id: end_recall_topic",
        "      clearTopicQueue: true",
    )

PATTERN_BUILDERS = {
    "topic-only": topic_only_yaml,
    "web-browse": web_browse_yaml,
    "memory-save": memory_save_yaml,
    "memory-recall": memory_recall_yaml,
}

_WIZARD_HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>RAPP → MCS Topic Wizard</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  :root {
    --bg: #0d1117; --surface: #161b22; --surface2: #21262d; --border: #30363d;
    --text: #e6edf3; --dim: #8b949e; --muted: #656d76;
    --accent: #58a6ff; --accent2: #bc8cff; --green: #3fb950; --amber: #d29922;
    --red: #f85149;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 0; background: var(--bg); color: var(--text);
    font: 14px/1.5 -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
  }
  header {
    padding: 16px 24px; border-bottom: 1px solid var(--border);
    display: flex; justify-content: space-between; align-items: center;
    background: var(--surface);
  }
  header h1 { margin: 0; font-size: 18px; }
  header .stats { color: var(--dim); font-size: 12px; }
  main { display: grid; grid-template-columns: 280px 1fr 1fr; height: calc(100vh - 60px); }
  nav {
    border-right: 1px solid var(--border); overflow: auto; padding: 12px; background: var(--surface);
  }
  nav .agent-pill {
    display: block; padding: 10px 12px; margin: 0 0 6px 0; border-radius: 6px;
    cursor: pointer; border: 1px solid transparent; color: var(--text);
    font-size: 13px; transition: background 0.1s;
  }
  nav .agent-pill:hover { background: var(--surface2); }
  nav .agent-pill.active { background: var(--surface2); border-color: var(--accent); }
  nav .agent-pill .name { font-weight: 600; }
  nav .agent-pill .pattern {
    display: inline-block; margin-top: 4px; padding: 2px 6px; font-size: 11px;
    background: var(--surface); border-radius: 4px; color: var(--dim);
  }
  nav .agent-pill .pattern.memory-save  { color: var(--accent2); }
  nav .agent-pill .pattern.memory-recall{ color: var(--accent); }
  nav .agent-pill .pattern.web-browse   { color: var(--green); }
  nav .agent-pill .pattern.topic-only   { color: var(--amber); }
  nav .toolbar {
    border-top: 1px solid var(--border); padding-top: 12px; margin-top: 12px;
    display: flex; flex-direction: column; gap: 6px;
  }
  nav .toolbar button {
    width: 100%; padding: 8px 10px; background: var(--surface2); color: var(--text);
    border: 1px solid var(--border); border-radius: 6px; cursor: pointer; font: inherit;
  }
  nav .toolbar button:hover { background: var(--border); }
  nav .toolbar button.primary { background: var(--accent); border-color: var(--accent); color: #0d1117; font-weight: 600; }

  section.editor, section.preview { overflow: auto; padding: 20px 24px; }
  section.editor { border-right: 1px solid var(--border); background: var(--bg); }
  section.preview { background: var(--bg); }
  section h2 { margin: 0 0 16px 0; font-size: 14px; color: var(--dim); text-transform: uppercase; letter-spacing: 0.06em; }
  label { display: block; font-size: 12px; color: var(--dim); margin-bottom: 4px; margin-top: 14px; }
  label:first-of-type { margin-top: 0; }
  input[type=text], textarea, select {
    width: 100%; padding: 8px 10px; background: var(--surface); color: var(--text);
    border: 1px solid var(--border); border-radius: 6px; font: 13px/1.4 -apple-system, BlinkMacSystemFont, sans-serif;
  }
  textarea { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; min-height: 90px; resize: vertical; }
  .row { display: flex; gap: 10px; }
  .row > * { flex: 1; }
  .pattern-radio { display: flex; gap: 8px; flex-wrap: wrap; }
  .pattern-radio label {
    display: inline-flex; gap: 6px; align-items: center; padding: 8px 12px;
    background: var(--surface); border: 1px solid var(--border); border-radius: 6px;
    cursor: pointer; margin: 0; font-size: 13px; color: var(--text);
  }
  .pattern-radio label.selected { border-color: var(--accent); background: var(--surface2); }
  .pattern-radio input { margin: 0; }
  .preview-actions {
    display: flex; gap: 8px; margin-bottom: 12px;
  }
  .preview-actions button {
    padding: 6px 12px; font-size: 12px; background: var(--surface2); color: var(--text);
    border: 1px solid var(--border); border-radius: 6px; cursor: pointer;
  }
  .preview-actions button:hover { background: var(--border); }
  pre.yaml {
    margin: 0; padding: 16px; background: var(--surface); border: 1px solid var(--border);
    border-radius: 6px; overflow: auto; font-size: 12px; line-height: 1.55;
    white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    color: var(--text);
  }
  .step-help {
    background: var(--surface); border-left: 3px solid var(--accent);
    padding: 10px 14px; border-radius: 0 6px 6px 0; margin-bottom: 16px;
    font-size: 13px; color: var(--dim);
  }
  .step-help strong { color: var(--text); }
  .empty {
    display: flex; align-items: center; justify-content: center; flex-direction: column;
    height: 100%; color: var(--dim);
  }
  .empty h2 { color: var(--dim); }
  .badge { display: inline-block; padding: 2px 8px; font-size: 11px; border-radius: 10px; background: var(--surface2); color: var(--dim); margin-left: 8px;}
  .filename { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12px; color: var(--dim); }
</style>
</head>
<body>
<header>
  <h1>RAPP → MCS Topic Wizard</h1>
  <div class="stats" id="stats">
    <span id="agents-dir-display"></span>
    <span class="badge" id="count-badge">0 agents</span>
  </div>
</header>
<main>
  <nav>
    <div id="agent-list"></div>
    <div class="toolbar">
      <button id="btn-download-current">Download this .mcs.yml</button>
      <button id="btn-download-all" class="primary">Download all (.json bundle)</button>
      <button id="btn-copy-config">Copy config JSON</button>
      <button id="btn-reset">Reset to defaults</button>
    </div>
  </nav>

  <section class="editor" id="editor">
    <div class="empty">
      <h2>Select an agent on the left</h2>
      <p>Step through each one, edit its topic, and grab the YAML.</p>
    </div>
  </section>

  <section class="preview" id="preview">
    <div class="empty">
      <h2>YAML preview</h2>
    </div>
  </section>
</main>

<script>
// ─── Embedded scan results (baked at wizard-emit time) ────────────
const SCAN = __SCAN_JSON__;
const AGENTS_DIR = __AGENTS_DIR_JSON__;
const TOPICS_DIR_HINT = __TOPICS_DIR_JSON__;

// ─── Per-agent editable config (initialised from defaults) ─────────
const CONFIG = SCAN.agents
  .filter(a => !a.error)
  .map(a => ({
    filename: a.filename,
    class_name: a.class_name,
    pattern: a.default_pattern,
    component_name: a.default_display_name,
    intent_display_name: a.default_intent_name,
    description: a.manifest_description || a.description || '',
    trigger_queries: a.default_trigger_queries.slice(),
    response_text: 'This is the ' + a.default_intent_name + ' topic. Edit me.',
    browse_url: (a.uses_urls[0] || ''),
    format_hint: 'summarize as a numbered markdown list',
    topic_filename: a.default_intent_name.replace(/\s+/g,'') + '.mcs.yml',
  }));

document.getElementById('agents-dir-display').textContent = AGENTS_DIR;
document.getElementById('count-badge').textContent = CONFIG.length + ' agents';

// ─── YAML builders (mirror the python builders) ────────────────────
function yamlStr(s) {
  if (s === null || s === undefined) return '""';
  s = String(s);
  if (/[:#&*!|>'"\n]/.test(s) || s.trim() !== s) {
    return '"' + s.replace(/\\/g,'\\\\').replace(/"/g,'\\"') + '"';
  }
  return s;
}
function bullets(items, indent='      - ') {
  return (items || []).map(i => indent + yamlStr(i)).join('\n');
}
function topicOnly(c) {
  return [
    'mcs.metadata:',
    '  componentName: ' + yamlStr(c.component_name),
    '  description: ' + yamlStr(c.description || c.component_name),
    'kind: AdaptiveDialog',
    'beginDialog:',
    '  kind: OnRecognizedIntent',
    '  id: main',
    '  intent:',
    '    displayName: ' + yamlStr(c.intent_display_name),
    '    includeInOnSelectIntent: true',
    '    triggerQueries:',
    bullets(c.trigger_queries),
    '',
    '  actions:',
    '    - kind: SendActivity',
    '      id: sendMessage_main',
    '      activity:',
    '        text:',
    '          - ' + yamlStr(c.response_text),
    '',
    '    - kind: EndDialog',
    '      id: end_topic',
    '      clearTopicQueue: true',
    '',
  ].join('\n');
}
function webBrowse(c) {
  const fx = '=Concatenate("Fetch ", "' + c.browse_url + '", " and ' + c.format_hint
    + '. Use the agent\'s web browsing — do not fabricate.")';
  return [
    'mcs.metadata:',
    '  componentName: ' + yamlStr(c.component_name),
    '  description: ' + yamlStr(c.description || c.component_name),
    'kind: AdaptiveDialog',
    'beginDialog:',
    '  kind: OnRecognizedIntent',
    '  id: main',
    '  intent:',
    '    displayName: ' + yamlStr(c.intent_display_name),
    '    includeInOnSelectIntent: true',
    '    triggerQueries:',
    bullets(c.trigger_queries),
    '',
    '  actions:',
    '    - kind: SendActivity',
    '      id: sendMessage_fetching',
    '      activity:',
    '        text:',
    '          - ' + yamlStr('Fetching from ' + c.browse_url + ' ...'),
    '',
    '    - kind: SearchAndSummarizeContent',
    '      id: search_topic',
    '      variable: Topic.Answer',
    '      userInput: ' + fx,
    '      additionalInstructions: |-',
    '        Use the agent\'s built-in web browsing capability to read the URL above directly.',
    '        Do not fabricate. If browsing fails, reply exactly: "I couldn\'t reach that source just now."',
    '',
    '    - kind: ConditionGroup',
    '      id: condition_answer',
    '      conditions:',
    '        - id: has_answer',
    '          condition: =!IsBlank(Topic.Answer)',
    '          actions:',
    '            - kind: SendActivity',
    '              id: sendMessage_answer',
    '              activity: "{Topic.Answer}"',
    '            - kind: EndDialog',
    '              id: end_topic',
    '              clearTopicQueue: true',
    '',
    '      elseActions:',
    '        - kind: SendActivity',
    '          id: sendMessage_failed',
    '          activity: I couldn\'t reach that source just now. Try again in a moment.',
    '',
  ].join('\n');
}
function memorySave(c) {
  return [
    'mcs.metadata:',
    '  componentName: ' + yamlStr(c.component_name),
    '  description: ' + yamlStr(c.description || c.component_name),
    'kind: AdaptiveDialog',
    'beginDialog:',
    '  kind: OnRecognizedIntent',
    '  id: main',
    '  intent:',
    '    displayName: ' + yamlStr(c.intent_display_name),
    '    includeInOnSelectIntent: true',
    '    triggerQueries:',
    bullets(c.trigger_queries),
    '',
    '  inputs:',
    '    - kind: AutomaticTaskParameter',
    '      propertyName: content',
    '      parameter:',
    '        description: The content to save to memory.',
    '        displayName: Memory Content',
    '        entity: StringPrebuiltEntity',
    '',
    '    - kind: AutomaticTaskParameter',
    '      propertyName: memory_type',
    '      parameter:',
    '        description: Classify the memory (fact / preference / insight / task). Default fact.',
    '        displayName: Memory Type',
    '        entity: StringPrebuiltEntity',
    '',
    '  actions:',
    '    - kind: SetVariable',
    '      id: setVariable_resolved_type',
    '      variable: Topic.ResolvedType',
    '      value: =If(IsBlank(Topic.memory_type) Or Not(Topic.memory_type in ["fact", "preference", "insight", "task"]), "fact", Lower(Topic.memory_type))',
    '',
    '    - kind: SetVariable',
    '      id: setVariable_subject',
    '      variable: Topic.Subject',
    '      value: =Concatenate("RAPP-memory:", Topic.ResolvedType)',
    '',
    '    - kind: InvokeConnectorAction',
    '      id: dvAddNote_RAPP_memory',
    '      connectionReference: shared_commondataserviceforapps',
    '      connectionProperties:',
    '        mode: Maker',
    '      operationId: AddRow',
    '      input:',
    '        binding:',
    '          entityName: ="annotations"',
    '          item/subject: =Topic.Subject',
    '          item/notetext: =Topic.content',
    '      output:',
    '        binding:',
    '          response: Topic.AddResponse',
    '',
    '    - kind: SendActivity',
    '      id: sendMessage_saved',
    '      activity:',
    '        text:',
    '          - \'Saved {Topic.ResolvedType} memory: "{Topic.content}"\'',
    '',
    '    - kind: EndDialog',
    '      id: end_remember_topic',
    '      clearTopicQueue: true',
    '',
  ].join('\n');
}
function memoryRecall(c) {
  return [
    'mcs.metadata:',
    '  componentName: ' + yamlStr(c.component_name),
    '  description: ' + yamlStr(c.description || c.component_name),
    'kind: AdaptiveDialog',
    'beginDialog:',
    '  kind: OnRecognizedIntent',
    '  id: main',
    '  intent:',
    '    displayName: ' + yamlStr(c.intent_display_name),
    '    includeInOnSelectIntent: true',
    '    triggerQueries:',
    bullets(c.trigger_queries),
    '',
    '  inputs:',
    '    - kind: AutomaticTaskParameter',
    '      propertyName: keywords',
    '      parameter:',
    '        description: Optional keyword filter. Blank for full recall.',
    '        displayName: Keyword Filter',
    '        entity: StringPrebuiltEntity',
    '',
    '  actions:',
    '    - kind: SetVariable',
    '      id: setVariable_user_filter',
    '      variable: Topic.UserFilter',
    '      value: =Concatenate("_createdby_value eq \'", Text(System.User.Id), "\' and startswith(subject, \'RAPP-memory:\')")',
    '',
    '    - kind: SetVariable',
    '      id: setVariable_final_filter',
    '      variable: Topic.FinalFilter',
    '      value: =If(IsBlank(Topic.keywords), Topic.UserFilter, Concatenate(Topic.UserFilter, " and contains(notetext, \'", Topic.keywords, "\')"))',
    '',
    '    - kind: InvokeConnectorAction',
    '      id: dvListNotes_RAPP_memory',
    '      connectionReference: shared_commondataserviceforapps',
    '      connectionProperties:',
    '        mode: Maker',
    '      operationId: ListRows',
    '      input:',
    '        binding:',
    '          entityName: ="annotations"',
    '          $filter: =Topic.FinalFilter',
    '          $orderby: ="createdon desc"',
    '          $select: ="subject,notetext,createdon"',
    '          $top: =50',
    '      output:',
    '        binding:',
    '          response: Topic.ListResponse',
    '',
    '    - kind: SendActivity',
    '      id: sendMessage_recall',
    '      activity: "{Topic.ListResponse.value}"',
    '',
    '    - kind: EndDialog',
    '      id: end_recall_topic',
    '      clearTopicQueue: true',
    '',
  ].join('\n');
}
const BUILDERS = {
  'topic-only': topicOnly,
  'web-browse': webBrowse,
  'memory-save': memorySave,
  'memory-recall': memoryRecall,
};

// ─── UI state + render ──────────────────────────────────────────────
let selected = 0;
function renderNav() {
  const el = document.getElementById('agent-list');
  el.innerHTML = '';
  CONFIG.forEach((c, i) => {
    const div = document.createElement('div');
    div.className = 'agent-pill' + (i === selected ? ' active' : '');
    div.onclick = () => { selected = i; renderNav(); renderEditor(); renderPreview(); };
    div.innerHTML =
      '<div class="name">' + c.intent_display_name + '</div>' +
      '<div class="filename">' + c.filename + '</div>' +
      '<span class="pattern ' + c.pattern + '">' + c.pattern + '</span>';
    el.appendChild(div);
  });
}

function renderEditor() {
  const c = CONFIG[selected];
  if (!c) return;
  const e = document.getElementById('editor');
  e.innerHTML = '';
  e.appendChild(html(`
    <h2>Step ${selected+1} of ${CONFIG.length} · ${c.filename}</h2>
    <div class="step-help">
      <strong>What this is:</strong> the topic an LLM-driven Copilot Studio agent
      will route to when a user's message matches one of the trigger queries below.
      Pick the pattern that best matches what the source agent does — the wizard
      pre-fills sensible defaults, but everything is editable.
    </div>

    <label>Pattern (decides the topic shape)</label>
    <div class="pattern-radio" id="pattern-radio"></div>

    <div class="row" style="margin-top:14px;">
      <div>
        <label>Component name (shown in Copilot Studio)</label>
        <input type="text" id="component_name" value="${esc(c.component_name)}">
      </div>
      <div>
        <label>Intent display name</label>
        <input type="text" id="intent_display_name" value="${esc(c.intent_display_name)}">
      </div>
    </div>

    <label>Output topic filename</label>
    <input type="text" id="topic_filename" value="${esc(c.topic_filename)}">

    <label>Description (in mcs.metadata)</label>
    <textarea id="description" rows="3">${esc(c.description)}</textarea>

    <label>Trigger queries (one per line — phrases users say to invoke this topic)</label>
    <textarea id="trigger_queries" rows="6">${esc(c.trigger_queries.join('\n'))}</textarea>

    <div id="pattern-specific"></div>
  `));

  // pattern radio
  const r = e.querySelector('#pattern-radio');
  Object.keys(BUILDERS).forEach(p => {
    const lab = document.createElement('label');
    lab.className = p === c.pattern ? 'selected' : '';
    lab.innerHTML = '<input type="radio" name="pattern" value="' + p + '"'
      + (p === c.pattern ? ' checked' : '') + '> ' + p;
    lab.onclick = () => { setTimeout(() => {
      c.pattern = r.querySelector('input:checked').value;
      renderNav(); renderEditor(); renderPreview();
    }, 0); };
    r.appendChild(lab);
  });

  // pattern-specific fields
  const ps = e.querySelector('#pattern-specific');
  if (c.pattern === 'topic-only') {
    ps.innerHTML = '<label>Response text (what the topic says when triggered)</label>'
      + '<textarea id="response_text" rows="3">' + esc(c.response_text) + '</textarea>';
    ps.querySelector('#response_text').oninput = ev => { c.response_text = ev.target.value; renderPreview(); };
  } else if (c.pattern === 'web-browse') {
    ps.innerHTML =
      '<label>Browse URL (the source the agent\'s webBrowsing will read)</label>'
      + '<input type="text" id="browse_url" value="' + esc(c.browse_url) + '">'
      + '<label>Format hint (told to the model along with the URL)</label>'
      + '<input type="text" id="format_hint" value="' + esc(c.format_hint) + '">';
    ps.querySelector('#browse_url').oninput = ev => { c.browse_url = ev.target.value; renderPreview(); };
    ps.querySelector('#format_hint').oninput = ev => { c.format_hint = ev.target.value; renderPreview(); };
  } else if (c.pattern === 'memory-save') {
    ps.innerHTML = '<div class="step-help">Calls <strong>shared_commondataserviceforapps</strong> '
      + '→ <strong>AddRow</strong> against the OOTB <code>annotations</code> table. '
      + 'subject = <code>RAPP-memory:&lt;type&gt;</code>, notetext = the user\'s content. '
      + 'No custom Dataverse tables, no Azure Function.</div>';
  } else if (c.pattern === 'memory-recall') {
    ps.innerHTML = '<div class="step-help">Calls <strong>shared_commondataserviceforapps</strong> '
      + '→ <strong>ListRows</strong> against <code>annotations</code>, filtered to '
      + '<code>_createdby_value eq System.User.Id</code> AND '
      + '<code>startswith(subject, \'RAPP-memory:\')</code>, ordered by <code>createdon desc</code>.</div>';
  }

  // generic-field bindings
  bind('#component_name', v => c.component_name = v);
  bind('#intent_display_name', v => c.intent_display_name = v);
  bind('#topic_filename', v => c.topic_filename = v);
  bind('#description', v => c.description = v);
  bind('#trigger_queries', v => c.trigger_queries = v.split('\n').map(s => s.trim()).filter(Boolean));
}

function bind(sel, setter) {
  const node = document.querySelector(sel);
  if (!node) return;
  node.oninput = ev => { setter(ev.target.value); renderPreview(); };
}

function renderPreview() {
  const c = CONFIG[selected];
  if (!c) return;
  const yaml = BUILDERS[c.pattern](c);
  const p = document.getElementById('preview');
  p.innerHTML = '';
  p.appendChild(html(`
    <h2>${esc(c.topic_filename)} · preview</h2>
    <div class="preview-actions">
      <button id="btn-copy-yaml">Copy YAML</button>
      <button id="btn-download-this">Download this file</button>
    </div>
    <pre class="yaml" id="yaml-output"></pre>
  `));
  p.querySelector('#yaml-output').textContent = yaml;
  p.querySelector('#btn-copy-yaml').onclick = () => copyText(yaml);
  p.querySelector('#btn-download-this').onclick = () => downloadFile(c.topic_filename, yaml);
}

// ─── Downloads + clipboard ──────────────────────────────────────────
function downloadFile(name, text) {
  const blob = new Blob([text], {type:'text/yaml;charset=utf-8'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = name;
  document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}
function downloadAllBundle() {
  const bundle = {
    schema: 'topic-wizard-bundle/1.0',
    generated_at: new Date().toISOString(),
    agents_dir: AGENTS_DIR,
    topics_dir_hint: TOPICS_DIR_HINT,
    files: Object.fromEntries(CONFIG.map(c => [c.topic_filename, BUILDERS[c.pattern](c)])),
    config: CONFIG,
  };
  downloadFile('topic_wizard_bundle.json', JSON.stringify(bundle, null, 2));
}
function copyText(t) { navigator.clipboard.writeText(t); }
function copyConfig() { copyText(JSON.stringify({ config: CONFIG }, null, 2)); }

document.getElementById('btn-download-current').onclick = () => {
  const c = CONFIG[selected]; if (!c) return;
  downloadFile(c.topic_filename, BUILDERS[c.pattern](c));
};
document.getElementById('btn-download-all').onclick = downloadAllBundle;
document.getElementById('btn-copy-config').onclick = copyConfig;
document.getElementById('btn-reset').onclick = () => { location.reload(); };

// ─── small helpers ──────────────────────────────────────────────────
function html(s) { const t = document.createElement('template'); t.innerHTML = s.trim(); return t.content.firstChild; }
function esc(s) { return String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }

// ─── bootstrap ──────────────────────────────────────────────────────
renderNav();
if (CONFIG.length) { selected = 0; renderEditor(); renderPreview(); }
</script>
</body>
</html>
"""

class _TopicEngine(_EngineBase):
    def __init__(self):
        self.name = "TopicWizard"
        self.metadata = {
            "name": self.name,
            "description": (
                "Convert rapp_brainstem/agents/*.py into Microsoft Copilot "
                "Studio topic .mcs.yml files, step-by-step.\n\n"
                "Actions:\n"
                " • 'scan' — list each agent and the auto-detected pattern.\n"
                " • 'wizard' — write a self-contained HTML page you open "
                "   in a browser. Walks through each agent: pick pattern "
                "   (topic-only / web-browse / memory-save / memory-recall), "
                "   edit display name, triggers, description, response text. "
                "   Live YAML preview. Download each .mcs.yml or the whole "
                "   bundle as JSON.\n"
                " • 'generate' — write the .mcs.yml files directly from a "
                "   config dict (the JSON the wizard exports, or one you "
                "   hand-author).\n\n"
                "Sacred constraints: OOTB Dataverse only (annotations "
                "table via shared_commondataserviceforapps), no Azure "
                "Functions, no custom connectors, no custom tables."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["scan", "wizard", "generate"],
                    },
                    "agents_dir": {
                        "type": "string",
                        "description": "Path to a directory of *_agent.py. "
                                       "Default: rapp_brainstem/agents",
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Where to write the wizard HTML or "
                                       "the YAML files. For 'wizard', a .html "
                                       "file path. For 'generate', a directory.",
                    },
                    "config": {
                        "description": "For 'generate': a list of topic "
                                       "config dicts, or a wizard bundle "
                                       "JSON (with .files or .config). "
                                       "Accepts a JSON string or a dict.",
                    },
                    "open_in_browser": {
                        "type": "boolean",
                        "description": "For 'wizard': try to open the HTML "
                                       "file in the OS default browser. "
                                       "Default: false.",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def run(self, action="wizard", **kwargs):
        try:
            if action == "scan":
                return json.dumps(self._scan(kwargs), indent=2)
            if action == "wizard":
                return json.dumps(self._wizard(kwargs), indent=2)
            if action == "generate":
                return json.dumps(self._generate(kwargs), indent=2)
            return json.dumps({"status": "error",
                               "message": f"Unknown action: {action}"})
        except Exception as e:
            return json.dumps({"status": "error", "action": action,
                               "exception": type(e).__name__,
                               "message": str(e)})

    # — scan ——————————————————————————————————————————————————

    def _scan(self, k):
        agents_dir = k.get("agents_dir") or self._default_agents_dir()
        return _Scanner().scan(agents_dir)

    def _default_agents_dir(self):
        here = Path(__file__).resolve().parent
        for cand in (here, *here.parents):
            d = cand / "rapp_brainstem" / "agents"
            if d.is_dir():
                return str(d)
        return str(here / "rapp_brainstem" / "agents")

    # — wizard ——————————————————————————————————————————————————

    def _wizard(self, k):
        agents_dir = k.get("agents_dir") or self._default_agents_dir()
        scan = _Scanner().scan(agents_dir)
        if scan.get("status") != "ok":
            return scan
        topics_dir_hint = k.get("topics_dir_hint", "RAPP to MCS Agent Template/topics")
        output_path = k.get("output_path")
        if not output_path:
            output_path = str(Path(self._default_agents_dir()).parent.parent /
                              "build" / "topic_wizard.html")
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        html = (_WIZARD_HTML_TEMPLATE
                .replace("__SCAN_JSON__", json.dumps(scan))
                .replace("__AGENTS_DIR_JSON__", json.dumps(scan["agents_dir"]))
                .replace("__TOPICS_DIR_JSON__", json.dumps(topics_dir_hint)))
        output_path.write_text(html, encoding="utf-8")

        opened = False
        if k.get("open_in_browser"):
            try:
                import webbrowser
                opened = webbrowser.open(output_path.as_uri())
            except Exception:
                pass

        return {"status": "ok",
                "phase": "wizard",
                "html_path": str(output_path),
                "html_uri": output_path.as_uri(),
                "agents_dir": scan["agents_dir"],
                "agent_count": scan["count"],
                "topics_dir_hint": topics_dir_hint,
                "opened_in_browser": opened,
                "next_step": ("Open html_path in a browser. Walk through "
                              "each agent. Download topic_wizard_bundle.json "
                              "at the end and pass it back via "
                              "perform(action='generate', config=<json>) "
                              "to write the .mcs.yml files to disk.")}

    # — generate ——————————————————————————————————————————————

    def _generate(self, k):
        config = k.get("config")
        if isinstance(config, str):
            config = json.loads(config)
        if not config:
            return {"status": "error",
                    "message": "config is required (the wizard's bundle JSON "
                               "or a list of topic config dicts)."}

        # Two acceptable shapes:
        #   1) Wizard bundle: {"files": {"X.mcs.yml": "<yaml>"}, ...}
        #   2) Raw config:    {"config": [...]} or just [...]
        # In case (1) we already have built YAMLs — write them straight.
        # In case (2) we rebuild deterministically from the config items.
        out_dir = Path(k.get("output_path") or "build/topics")
        out_dir.mkdir(parents=True, exist_ok=True)

        files_written = []
        files_from_bundle = config.get("files") if isinstance(config, dict) else None
        if files_from_bundle:
            for fname, yaml in files_from_bundle.items():
                p = out_dir / fname
                p.write_text(yaml, encoding="utf-8")
                files_written.append({"path": str(p), "bytes": len(yaml.encode())})
        else:
            items = config.get("config") if isinstance(config, dict) else config
            if not isinstance(items, list):
                return {"status": "error",
                        "message": "config must be a list of topic dicts or a wizard bundle."}
            for c in items:
                pattern = c.get("pattern", "topic-only")
                builder = PATTERN_BUILDERS.get(pattern)
                if not builder:
                    return {"status": "error",
                            "message": f"unknown pattern: {pattern!r}",
                            "supported": list(PATTERN_BUILDERS.keys())}
                yaml = self._build_yaml(builder, c)
                fname = c.get("topic_filename") or \
                        (c.get("intent_display_name", "Topic").replace(" ", "") + ".mcs.yml")
                p = out_dir / fname
                p.write_text(yaml, encoding="utf-8")
                files_written.append({"path": str(p), "bytes": len(yaml.encode()),
                                      "pattern": pattern})

        return {"status": "ok",
                "phase": "generate",
                "output_dir": str(out_dir),
                "files_written": files_written,
                "count": len(files_written)}

    def _build_yaml(self, builder, c):
        common = {
            "component_name": c.get("component_name", c.get("intent_display_name", "Topic")),
            "description": c.get("description", ""),
            "intent_display_name": c.get("intent_display_name", "Topic"),
            "trigger_queries": c.get("trigger_queries", []),
        }
        if builder is topic_only_yaml:
            return builder(response_text=c.get("response_text", ""), **common)
        if builder is web_browse_yaml:
            return builder(browse_url=c.get("browse_url", ""),
                           format_hint=c.get("format_hint", "summarize"),
                           **common)
        # memory-save and memory-recall don't need extra fields
        return builder(**common)

logger = logging.getLogger(__name__)

CONNECTOR_MAPPINGS = {
    "salesforce": {
        "connector_id": "shared_salesforce",
        "display_name": "Salesforce",
        "operations": {
            "query": "GetItems",
            "create": "PostItem",
            "update": "PatchItem",
            "get_by_id": "GetItem"
        }
    },
    "cosmos_db": {
        "connector_id": "shared_documentdb",
        "display_name": "Azure Cosmos DB",
        "alternative": "dataverse",  # Can use Dataverse as simpler alternative
        "operations": {
            "query": "QueryDocuments",
            "create": "CreateDocument",
            "update": "ReplaceDocument"
        }
    },
    "sharepoint": {
        "connector_id": "shared_sharepointonline",
        "display_name": "SharePoint",
        "operations": {
            "get_files": "GetFileContent",
            "create_file": "CreateFile",
            "list_items": "GetItems"
        }
    },
    "azure_openai": {
        "connector_id": None,  # Use native Generative AI
        "display_name": "Generative AI (Native)",
        "note": "Handled by Copilot Studio's built-in AI capabilities"
    },
    "outlook": {
        "connector_id": "shared_office365",
        "display_name": "Office 365 Outlook",
        "operations": {
            "send_email": "SendEmail",
            "get_emails": "GetEmails"
        }
    }
}

TOPIC_TEMPLATES = {
    "greeting": {
        "trigger_phrases": ["hello", "hi", "hey", "start", "help"],
        "type": "system"
    },
    "fallback": {
        "trigger_phrases": [],
        "type": "system",
        "use_generative_answers": True
    },
    "action": {
        "type": "custom",
        "requires_flow": True
    }
}

class _SolutionEngine(_EngineBase):
    """
    Transpiles RAPP Python agents to native Copilot Studio solutions.
    
    Generates:
    - Solution manifest (for import into Copilot Studio)
    - Agent configuration with instructions
    - Topics for each action
    - Power Automate flows for complex operations
    - Connector configurations for external systems
    
    Capabilities:
    - transpile: Convert RAPP agent to Copilot Studio format
    - analyze: Analyze agent and recommend mapping strategy
    - preview: Preview what would be generated
    - validate: Check if agent can be fully transpiled
    - list_connectors: Show available connector mappings
    """
    
    def __init__(self):
        self.name = "CopilotStudioTranspiler"
        self.metadata = {
            "name": self.name,
            "description": "Converts RAPP Python agents to fully native Copilot Studio solutions without Function App dependency.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["transpile", "analyze", "preview", "validate", "list_connectors", "batch_transpile", "package", "deploy", "deploy_status", "configure_deployment"],
                        "description": "Transpilation action to perform"
                    },
                    "agent_name": {
                        "type": "string",
                        "description": "Name of the RAPP agent to transpile (e.g., 'FabrikamCaseTriageOrchestrator')"
                    },
                    "agent_file": {
                        "type": "string",
                        "description": "Path to the agent Python file (optional, will search if not provided)"
                    },
                    "pattern": {
                        "type": "string",
                        "description": "Pattern to match agent names for batch_transpile (e.g., 'contoso')"
                    },
                    "agent_list": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of agent names for batch_transpile"
                    },
                    "output_format": {
                        "type": "string",
                        "enum": ["solution", "yaml", "json"],
                        "default": "solution",
                        "description": "Output format - 'solution' for importable package"
                    },
                    "include_flows": {
                        "type": "boolean",
                        "default": True,
                        "description": "Generate Power Automate flows for complex actions"
                    },
                    "dataverse_alternative": {
                        "type": "boolean",
                        "default": True,
                        "description": "Use Dataverse instead of Cosmos DB where possible"
                    },
                    "environment_url": {
                        "type": "string",
                        "description": "Dataverse environment URL for deployment (e.g., https://org.crm.dynamics.com)"
                    },
                    "tenant_id": {
                        "type": "string",
                        "description": "Azure AD tenant ID for deployment authentication"
                    },
                    "client_id": {
                        "type": "string",
                        "description": "Azure AD app registration client ID"
                    }
                },
                "required": ["action"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.output_path = os.path.join(self.base_path, "transpiled", "copilot_studio_native")
    
    def run(self, **kwargs) -> str:
        """Execute transpilation action."""
        action = kwargs.get("action", "analyze")
        
        try:
            if action == "transpile":
                return self._transpile(**kwargs)
            elif action == "analyze":
                return self._analyze(**kwargs)
            elif action == "preview":
                return self._preview(**kwargs)
            elif action == "validate":
                return self._validate(**kwargs)
            elif action == "list_connectors":
                return self._list_connectors()
            elif action == "batch_transpile":
                return self._batch_transpile(
                    pattern=kwargs.get("pattern"),
                    agent_list=kwargs.get("agent_list")
                )
            elif action == "package":
                return self._create_solution_package(kwargs.get("agent_name"))
            elif action == "deploy":
                return self._deploy_to_copilot_studio(**kwargs)
            elif action == "deploy_status":
                return self._check_deployment_status(**kwargs)
            elif action == "configure_deployment":
                return self._configure_deployment(**kwargs)
            elif action == "deploy_solution":
                return self._deploy_solution(**kwargs)
            elif action == "list_solutions":
                return self._list_solutions(**kwargs)
            elif action == "create_solution":
                return self._create_solution_definition(**kwargs)
            else:
                return json.dumps({
                    "status": "error",
                    "error": f"Unknown action: {action}"
                })
        except Exception as e:
            logger.error(f"Transpiler error: {e}")
            import traceback
            return json.dumps({
                "status": "error",
                "error": str(e),
                "traceback": traceback.format_exc()
            })
    
    def _transpile(self, **kwargs) -> str:
        """Transpile RAPP agent to Copilot Studio native format."""
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            return json.dumps({"status": "error", "error": "agent_name is required"})
        
        # Find and parse the agent
        agent_def = self._parse_agent(agent_name, kwargs.get("agent_file"))
        if not agent_def:
            return json.dumps({"status": "error", "error": f"Could not find agent: {agent_name}"})
        
        # Analyze dependencies
        analysis = self._analyze_dependencies(agent_def)
        
        # Generate Copilot Studio components
        output_format = kwargs.get("output_format", "solution")
        include_flows = kwargs.get("include_flows", True)
        use_dataverse = kwargs.get("dataverse_alternative", True)
        
        solution = self._generate_solution(
            agent_def, 
            analysis, 
            include_flows=include_flows,
            use_dataverse=use_dataverse
        )
        
        # Save outputs
        output_dir = self._save_solution(agent_name, solution, output_format)
        
        return json.dumps({
            "status": "success",
            "agent_name": agent_name,
            "output_directory": output_dir,
            "files_generated": list(solution.keys()),
            "connectors_required": analysis.get("connectors", []),
            "flows_generated": len([f for f in solution.keys() if "flow" in f.lower()]),
            "topics_generated": len([f for f in solution.keys() if "topic" in f.lower()]),
            "deployment_notes": self._get_deployment_notes(analysis)
        }, indent=2)
    
    def _analyze(self, **kwargs) -> str:
        """Analyze agent and recommend transpilation strategy."""
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            return json.dumps({"status": "error", "error": "agent_name is required"})
        
        agent_def = self._parse_agent(agent_name, kwargs.get("agent_file"))
        if not agent_def:
            return json.dumps({"status": "error", "error": f"Could not find agent: {agent_name}"})
        
        analysis = self._analyze_dependencies(agent_def)
        
        # Determine transpilation feasibility
        feasibility = self._assess_feasibility(analysis)
        
        return json.dumps({
            "status": "success",
            "agent_name": agent_name,
            "analysis": analysis,
            "feasibility": feasibility,
            "recommendations": self._get_recommendations(analysis, feasibility)
        }, indent=2)
    
    def _preview(self, **kwargs) -> str:
        """Preview what would be generated without saving."""
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            return json.dumps({"status": "error", "error": "agent_name is required"})
        
        agent_def = self._parse_agent(agent_name, kwargs.get("agent_file"))
        if not agent_def:
            return json.dumps({"status": "error", "error": f"Could not find agent: {agent_name}"})
        
        analysis = self._analyze_dependencies(agent_def)
        solution = self._generate_solution(agent_def, analysis)
        
        # Return preview without saving
        preview = {}
        for filename, content in solution.items():
            if isinstance(content, dict):
                preview[filename] = content
            else:
                preview[filename] = f"[{len(content)} characters]"
        
        return json.dumps({
            "status": "success",
            "agent_name": agent_name,
            "preview": preview
        }, indent=2)
    
    def _validate(self, **kwargs) -> str:
        """Validate if agent can be fully transpiled."""
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            return json.dumps({"status": "error", "error": "agent_name is required"})
        
        agent_def = self._parse_agent(agent_name, kwargs.get("agent_file"))
        if not agent_def:
            return json.dumps({"status": "error", "error": f"Could not find agent: {agent_name}"})
        
        analysis = self._analyze_dependencies(agent_def)
        feasibility = self._assess_feasibility(analysis)
        
        issues = []
        warnings = []
        
        # Check for unsupported features
        for dep in analysis.get("unsupported_dependencies", []):
            issues.append(f"Unsupported dependency: {dep}")
        
        # Check for features that need manual config
        for feature in analysis.get("manual_config_required", []):
            warnings.append(f"Manual configuration needed: {feature}")
        
        return json.dumps({
            "status": "success",
            "agent_name": agent_name,
            "can_transpile": feasibility["can_transpile"],
            "transpile_completeness": feasibility["completeness_percent"],
            "issues": issues,
            "warnings": warnings
        }, indent=2)
    
    def _list_connectors(self) -> str:
        """List available connector mappings."""
        connectors = []
        for key, config in CONNECTOR_MAPPINGS.items():
            connectors.append({
                "rapp_dependency": key,
                "copilot_studio_connector": config["display_name"],
                "connector_id": config.get("connector_id"),
                "alternative": config.get("alternative"),
                "note": config.get("note")
            })
        
        return json.dumps({
            "status": "success",
            "connectors": connectors
        }, indent=2)
    
    # =========================================================================
    # PARSING METHODS
    # =========================================================================
    
    def _parse_agent(self, agent_name: str, agent_file: str = None) -> Optional[Dict]:
        """
        Parse a RAPP agent into a definition dictionary.
        
        Supports both:
        - Python agent files (.py) in agents/ directory
        - JSON agent definitions (.json) in demos/ directory
        """
        # Find the agent file (JSON or Python)
        if agent_file and os.path.exists(agent_file):
            file_path = agent_file
        else:
            file_path = self._find_agent_file(agent_name)
        
        if not file_path:
            logger.error(f"Could not find agent file for: {agent_name}")
            return None
        
        try:
            # Determine file type and parse accordingly
            if file_path.endswith('.json'):
                return self._parse_json_agent(agent_name, file_path)
            else:
                return self._parse_python_agent(agent_name, file_path)
            
        except Exception as e:
            logger.error(f"Error parsing agent file: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def _parse_json_agent(self, agent_name: str, file_path: str) -> Optional[Dict]:
        """Parse a RAPP JSON agent definition file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        agent_info = data.get("agent", {})
        metadata = data.get("metadata", {})
        
        # Extract systemPrompt - this is CRITICAL for Copilot Studio
        system_prompt = data.get("systemPrompt", "")
        if not system_prompt:
            # Try to build from description and other fields
            system_prompt = self._build_system_prompt_from_json(data)
        
        # Extract actions from metadata or actions array
        actions = []
        if "actions" in data:
            for action in data["actions"]:
                actions.append({
                    "name": action.get("name", ""),
                    "description": action.get("description", ""),
                    "parameters": action.get("parameters", []),
                    "needs_flow": True  # JSON-defined actions typically need flows
                })
        elif "parameters" in metadata and "properties" in metadata["parameters"]:
            action_prop = metadata["parameters"]["properties"].get("action", {})
            if "enum" in action_prop:
                for action_name in action_prop["enum"]:
                    actions.append({
                        "name": action_name,
                        "description": self._action_to_description(action_name),
                        "needs_flow": True
                    })
        
        # Build agent definition
        agent_def = {
            "name": agent_name,
            "file_path": file_path,
            "file_type": "json",
            "class_name": metadata.get("name", agent_info.get("name", agent_name)),
            "description": agent_info.get("description", metadata.get("description", "")),
            "system_prompt": system_prompt,
            "actions": actions,
            "imports": [],
            "external_calls": self._detect_external_calls_from_json(data),
            "sub_agents": [],
            "metadata": metadata,
            "raw_json": data  # Keep the full JSON for reference
        }
        
        return agent_def
    
    def _build_system_prompt_from_json(self, data: Dict) -> str:
        """Build a system prompt from JSON agent data if systemPrompt is missing."""
        agent_info = data.get("agent", {})
        metadata = data.get("metadata", {})
        
        parts = []
        
        # Start with the description
        desc = agent_info.get("description", metadata.get("description", ""))
        if desc:
            parts.append(f"You are {agent_info.get('name', 'an AI agent')}. {desc}")
        
        # Add scope information if present
        scope = data.get("scope", {})
        if scope:
            parts.append("\n**SCOPE:**")
            for key, value in scope.items():
                if isinstance(value, dict) and "description" in value:
                    parts.append(f"- {key.replace('_', ' ').title()}: {value['description']}")
        
        # Add signal priorities if present
        signals = data.get("signal_priorities", [])
        if signals:
            parts.append("\n**PRIORITY SIGNALS:**")
            for sig in signals[:5]:  # Limit to top 5
                parts.append(f"- Priority {sig.get('priority', '?')}: {sig.get('signal', '')}")
        
        # Add confidence calibration if present
        conf = data.get("confidence_calibration", {})
        if conf:
            parts.append("\n**CONFIDENCE LEVELS:**")
            for level, info in conf.items():
                if isinstance(info, dict) and "criteria" in info:
                    parts.append(f"- {level.upper()}: {info['criteria']}")
        
        return "\n".join(parts) if parts else "You are a helpful AI assistant."
    
    def _detect_external_calls_from_json(self, data: Dict) -> List[str]:
        """Detect external service calls from JSON agent data."""
        external_calls = []
        json_str = json.dumps(data).lower()
        
        if "salesforce" in json_str or "sobject" in json_str:
            external_calls.append("salesforce")
        if "cosmos" in json_str or "documentdb" in json_str:
            external_calls.append("cosmos_db")
        if "openai" in json_str or "gpt" in json_str:
            external_calls.append("azure_openai")
        if "sharepoint" in json_str or "onedrive" in json_str:
            external_calls.append("sharepoint")
        if "outlook" in json_str or "email" in json_str:
            external_calls.append("outlook")
        
        return external_calls
    
    def _parse_python_agent(self, agent_name: str, file_path: str) -> Optional[Dict]:
        """Parse a RAPP Python agent file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Parse the AST
        tree = ast.parse(source_code)
        
        # Extract agent definition
        agent_def = {
            "name": agent_name,
            "file_path": file_path,
            "file_type": "python",
            "source_code": source_code,
            "class_name": None,
            "description": "",
            "system_prompt": "",
            "actions": [],
            "imports": [],
            "external_calls": [],
            "sub_agents": []
        }
        
        # Extract imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    agent_def["imports"].append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    agent_def["imports"].append(f"{module}.{alias.name}")
        
        # Find the main agent class
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                if "Agent" in node.name:
                    agent_def["class_name"] = node.name
                    agent_def["description"] = ast.get_docstring(node) or ""
                    
                    # Extract metadata from __init__
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef) and item.name == "__init__":
                            agent_def["metadata"] = self._extract_metadata(item)
                        
                        # Extract actions from perform method
                        if isinstance(item, ast.FunctionDef) and item.name == "perform":
                            agent_def["actions"] = self._extract_actions(item)
                    
                    # If AST extraction found no actions, try source-based extraction
                    if not agent_def["actions"]:
                        agent_def["actions"] = self._extract_actions_from_source(source_code)
        
        # Try to extract system_prompt from source
        agent_def["system_prompt"] = self._extract_system_prompt_from_source(source_code)
        
        # Detect external dependencies
        agent_def["external_calls"] = self._detect_external_calls(source_code)
        
        # Detect sub-agents (for orchestrators)
        agent_def["sub_agents"] = self._detect_sub_agents(source_code)
        
        return agent_def
    
    def _extract_system_prompt_from_source(self, source_code: str) -> str:
        """Extract system prompt from Python source code."""
        # Try multiple patterns
        patterns = [
            r'system_prompt\s*=\s*["\'\"](.+?)["\'\"]',
            r'systemPrompt\s*=\s*["\'\"](.+?)["\'\"]',
            r'SYSTEM_PROMPT\s*=\s*["\'\"](.+?)["\'\"]',
            r'instructions\s*=\s*["\'\"](.+?)["\'\"]',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, source_code, re.DOTALL)
            if match:
                return match.group(1).strip()
        
        # Try to find multi-line string assignments
        multiline_patterns = [
            r'system_prompt\s*=\s*"""(.+?)"""',
            r"system_prompt\s*=\s*'''(.+?)'''",
        ]
        
        for pattern in multiline_patterns:
            match = re.search(pattern, source_code, re.DOTALL)
            if match:
                return match.group(1).strip()
        
        return ""
    
    def _find_agent_file(self, agent_name: str) -> Optional[str]:
        """
        Find the Python or JSON file for an agent.
        
        PRIORITY: JSON files are preferred because they contain the full
        systemPrompt and structured agent configuration. Python files are
        used as fallback.
        """
        # Convert agent name to possible file names
        snake_name = self._to_snake_case(agent_name)
        possible_json_names = [
            f"{snake_name}.json",
            f"{snake_name}_agent.json",
            f"{agent_name}.json",
            f"{agent_name.lower()}.json"
        ]
        possible_py_names = [
            f"{snake_name}.py",
            f"{snake_name}_agent.py",
            f"{agent_name}.py",
            f"{agent_name.lower()}.py",
        ]
        
        # FIRST: Search in demos directory for JSON files (preferred - has systemPrompt)
        demos_dir = os.path.join(self.base_path, "demos")
        if os.path.exists(demos_dir):
            for filename in os.listdir(demos_dir):
                if filename.endswith('.json'):
                    if filename in possible_json_names or agent_name.lower() in filename.lower().replace('.json', ''):
                        json_path = os.path.join(demos_dir, filename)
                        logger.info(f"Found JSON agent file: {json_path}")
                        return json_path
        
        # SECOND: Search in agents directory for Python files (fallback)
        agents_dir = os.path.join(self.base_path, "agents")
        for root, dirs, files in os.walk(agents_dir):
            for filename in files:
                if filename.endswith('.py'):
                    if filename in possible_py_names or agent_name.lower() in filename.lower().replace('.py', ''):
                        py_path = os.path.join(root, filename)
                        logger.info(f"Found Python agent file: {py_path}")
                        return py_path
        
        return None
    
    def _extract_metadata(self, init_node: ast.FunctionDef) -> Dict:
        """Extract metadata from __init__ method."""
        metadata = {}
        for node in ast.walk(init_node):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Attribute) and target.attr == "metadata":
                        # Try to extract the dict
                        if isinstance(node.value, ast.Dict):
                            metadata = self._ast_dict_to_python(node.value)
        return metadata
    
    def _extract_actions_from_source(self, source_code: str) -> List[Dict]:
        """Extract actions from source code using regex patterns."""
        actions = []
        
        # Pattern 1: Look for action enum in metadata
        # "enum": ["action1", "action2", ...]
        enum_pattern = r'"enum"\s*:\s*\[([\s\S]*?)\]'
        enum_match = re.search(enum_pattern, source_code)
        if enum_match:
            enum_content = enum_match.group(1)
            # Extract quoted strings
            action_pattern = r'"([^"]+)"'
            action_matches = re.findall(action_pattern, enum_content)
            for action_name in action_matches:
                if action_name not in ['string', 'object', 'array', 'boolean', 'integer']:
                    actions.append({
                        "name": action_name,
                        "description": self._action_to_description(action_name)
                    })
        
        # Pattern 2: Look for if/elif action == "xyz" patterns
        action_compare_pattern = r'action\s*==\s*["\']([^"\']+)["\']'
        compare_matches = re.findall(action_compare_pattern, source_code)
        existing_names = {a["name"] for a in actions}
        for action_name in compare_matches:
            if action_name not in existing_names:
                actions.append({
                    "name": action_name,
                    "description": self._action_to_description(action_name)
                })
                existing_names.add(action_name)
        
        return actions
    
    def _action_to_description(self, action_name: str) -> str:
        """Convert action name to human-readable description."""
        # Replace underscores with spaces and title case
        desc = action_name.replace("_", " ").title()
        return desc
    
    def _extract_actions(self, perform_node: ast.FunctionDef) -> List[Dict]:
        """Extract actions from perform method."""
        actions = []
        
        # Look for if/elif chains checking action
        for node in ast.walk(perform_node):
            if isinstance(node, ast.Compare):
                # Check if comparing action variable
                if isinstance(node.left, ast.Name) and node.left.id == "action":
                    for comparator in node.comparators:
                        if isinstance(comparator, ast.Constant):
                            actions.append({
                                "name": comparator.value,
                                "description": f"Action: {comparator.value}"
                            })
        
        return actions
    
    def _detect_external_calls(self, source_code: str) -> List[str]:
        """Detect external service calls in source code."""
        external_calls = []
        
        # Salesforce patterns
        if re.search(r'salesforce|sf_client|simple_salesforce|sobjects', source_code, re.I):
            external_calls.append("salesforce")
        
        # Cosmos DB patterns
        if re.search(r'cosmos|CosmosClient|documentdb', source_code, re.I):
            external_calls.append("cosmos_db")
        
        # Azure OpenAI patterns
        if re.search(r'openai|AzureOpenAI|ChatCompletion|gpt-4', source_code, re.I):
            external_calls.append("azure_openai")
        
        # SharePoint patterns
        if re.search(r'sharepoint|graph.*sites|OneDrive', source_code, re.I):
            external_calls.append("sharepoint")
        
        # Email/Outlook patterns
        if re.search(r'outlook|send.*email|smtp', source_code, re.I):
            external_calls.append("outlook")
        
        return external_calls
    
    def _detect_sub_agents(self, source_code: str) -> List[str]:
        """Detect sub-agents used by orchestrators."""
        sub_agents = []
        
        # Find agent imports
        pattern = r'from agents\.(\w+) import (\w+Agent)'
        matches = re.findall(pattern, source_code)
        for module, class_name in matches:
            sub_agents.append({
                "module": module,
                "class_name": class_name
            })
        
        return sub_agents
    
    def _ast_dict_to_python(self, node: ast.Dict) -> Dict:
        """Convert AST Dict to Python dict (simplified)."""
        result = {}
        for key, value in zip(node.keys, node.values):
            if isinstance(key, ast.Constant):
                key_str = key.value
                if isinstance(value, ast.Constant):
                    result[key_str] = value.value
                elif isinstance(value, ast.Dict):
                    result[key_str] = self._ast_dict_to_python(value)
                else:
                    result[key_str] = str(ast.dump(value))
        return result
    
    # =========================================================================
    # ANALYSIS METHODS
    # =========================================================================
    
    def _analyze_dependencies(self, agent_def: Dict) -> Dict:
        """Analyze agent dependencies and map to Copilot Studio capabilities."""
        analysis = {
            "agent_type": "simple",
            "connectors": [],
            "native_capabilities": [],
            "flows_needed": [],
            "unsupported_dependencies": [],
            "manual_config_required": []
        }
        
        # Determine agent type
        if agent_def.get("sub_agents"):
            analysis["agent_type"] = "orchestrator"
        elif "analyzer" in agent_def.get("name", "").lower():
            analysis["agent_type"] = "analyzer"
        elif "generator" in agent_def.get("name", "").lower():
            analysis["agent_type"] = "generator"
        
        # Map external calls to connectors
        for call in agent_def.get("external_calls", []):
            mapping = CONNECTOR_MAPPINGS.get(call, {})
            
            if mapping.get("connector_id"):
                analysis["connectors"].append({
                    "type": call,
                    "connector_id": mapping["connector_id"],
                    "display_name": mapping["display_name"]
                })
            elif call == "azure_openai":
                analysis["native_capabilities"].append("generative_ai")
            else:
                analysis["unsupported_dependencies"].append(call)
        
        # Determine which actions need flows
        for action in agent_def.get("actions", []):
            action_name = action.get("name", "")
            
            # Simple queries can be topics, complex operations need flows
            if any(x in action_name.lower() for x in ["get", "list", "query", "status"]):
                action["needs_flow"] = False
            else:
                action["needs_flow"] = True
                analysis["flows_needed"].append(action_name)
        
        # Check for manual config requirements
        if agent_def.get("sub_agents"):
            analysis["manual_config_required"].append(
                "Sub-agent coordination - may need multiple topics or a master flow"
            )
        
        return analysis
    
    def _assess_feasibility(self, analysis: Dict) -> Dict:
        """Assess feasibility of transpilation."""
        issues = len(analysis.get("unsupported_dependencies", []))
        total_features = (
            len(analysis.get("connectors", [])) +
            len(analysis.get("native_capabilities", [])) +
            len(analysis.get("flows_needed", [])) +
            issues
        )
        
        if total_features == 0:
            total_features = 1
        
        completeness = ((total_features - issues) / total_features) * 100
        
        return {
            "can_transpile": issues == 0,
            "completeness_percent": round(completeness, 1),
            "blocking_issues": analysis.get("unsupported_dependencies", []),
            "agent_type": analysis.get("agent_type", "simple")
        }
    
    def _get_recommendations(self, analysis: Dict, feasibility: Dict) -> List[str]:
        """Get recommendations for transpilation."""
        recommendations = []
        
        if feasibility["completeness_percent"] == 100:
            recommendations.append("✅ Agent can be fully transpiled to native Copilot Studio")
        elif feasibility["completeness_percent"] >= 80:
            recommendations.append("⚠️ Agent can be mostly transpiled with some manual configuration")
        else:
            recommendations.append("❌ Agent requires significant manual work or hybrid approach")
        
        if "generative_ai" in analysis.get("native_capabilities", []):
            recommendations.append("💡 Azure OpenAI calls will use Copilot Studio's native Generative AI")
        
        if analysis.get("connectors"):
            connectors = [c["display_name"] for c in analysis["connectors"]]
            recommendations.append(f"🔌 Required connectors: {', '.join(connectors)}")
        
        if analysis.get("flows_needed"):
            recommendations.append(f"⚡ {len(analysis['flows_needed'])} Power Automate flows will be generated")
        
        if analysis.get("agent_type") == "orchestrator":
            recommendations.append("🎭 Orchestrator pattern - consider using topic routing or a master flow")
        
        return recommendations
    
    # =========================================================================
    # GENERATION METHODS
    # =========================================================================
    
    def _generate_solution(self, agent_def: Dict, analysis: Dict, 
                          include_flows: bool = True, use_dataverse: bool = True) -> Dict:
        """Generate complete Copilot Studio solution."""
        solution = {}
        
        agent_name = agent_def.get("name", "RAPPAgent")
        description = agent_def.get("description", "")[:500]
        
        # 1. Generate agent manifest
        solution["agent_manifest.json"] = self._generate_agent_manifest(
            agent_name, description, agent_def, analysis
        )
        
        # 2. Generate system instructions
        solution["instructions.md"] = self._generate_instructions(agent_def)
        
        # 3. Generate topics
        topics = self._generate_topics(agent_def, analysis)
        solution.update(topics)
        
        # 4. Generate flows (if needed)
        if include_flows and analysis.get("flows_needed"):
            flows = self._generate_flows(agent_def, analysis, use_dataverse)
            solution.update(flows)
        
        # 5. Generate connector configs
        if analysis.get("connectors"):
            solution["connectors.json"] = self._generate_connector_configs(analysis)
        
        # 6. Generate deployment guide
        solution["DEPLOYMENT_GUIDE.md"] = self._generate_deployment_guide(
            agent_name, analysis
        )
        
        return solution
    
    def _generate_agent_manifest(self, name: str, description: str, 
                                  agent_def: Dict, analysis: Dict) -> Dict:
        """
        Generate Copilot Studio agent manifest.
        
        CRITICAL: This manifest MUST include the systemPrompt/instructions
        for the agent to function properly in Copilot Studio.
        """
        # Get the system prompt - this is CRITICAL for the agent to work!
        system_prompt = agent_def.get("system_prompt", "")
        if not system_prompt:
            # Try to get from raw_json if available (JSON agent files)
            raw_json = agent_def.get("raw_json", {})
            system_prompt = raw_json.get("systemPrompt", "")
        
        if not system_prompt:
            # Fall back to description-based instructions
            system_prompt = f"You are {name}. {description}"
        
        return {
            "schemaVersion": "1.2",
            "name": name,
            "displayName": self._to_title_case(name),
            "description": description,
            "icon": "robot",
            "primaryLanguage": "en-US",
            "isGenerativeActionsEnabled": True,
            "isOrchestrationEnabled": analysis.get("agent_type") == "orchestrator",
            "knowledgeSources": [],
            # CRITICAL: Include the full system prompt for GPT component creation
            "instructions": system_prompt,
            "systemPrompt": system_prompt,  # Alias for compatibility
            "capabilities": {
                "generativeAnswers": "azure_openai" in agent_def.get("external_calls", []),
                "powerAutomateFlows": len(analysis.get("flows_needed", [])) > 0,
                "customConnectors": len(analysis.get("connectors", [])) > 0
            },
            "topics": [f"topic_{a['name']}" for a in agent_def.get("actions", [])],
            "metadata": {
                "source": "RAPP Transpiler",
                "transpiled_at": datetime.now().isoformat(),
                "original_agent": agent_def.get("class_name", name)
            }
        }
    
    def _generate_instructions(self, agent_def: Dict) -> str:
        """
        Generate agent instructions markdown file.
        
        This extracts the system prompt from multiple sources and formats it
        for documentation purposes. The actual GPT component instructions
        are set in the agent manifest.
        """
        description = agent_def.get("description", "")
        
        # Get system prompt from agent_def (already extracted during parsing)
        system_prompt = agent_def.get("system_prompt", "")
        
        # If not found, try raw_json for JSON agents
        if not system_prompt:
            raw_json = agent_def.get("raw_json", {})
            system_prompt = raw_json.get("systemPrompt", "")
        
        # If still not found, try to extract from Python source
        if not system_prompt:
            source = agent_def.get("source_code", "")
            if source:
                match = re.search(r'system_prompt\s*=\s*["\'](.+?)["\']', source, re.S)
                if match:
                    system_prompt = match.group(1)
        
        # Default if nothing found
        if not system_prompt:
            system_prompt = f"You are {agent_def.get('name', 'an AI agent')}. {description}"
        
        instructions = f"""# {agent_def.get('name', 'Agent')} Instructions

## Overview
{description}

## System Prompt
{system_prompt}

## Available Actions
"""
        for action in agent_def.get("actions", []):
            instructions += f"- **{action['name']}**: {action.get('description', 'No description')}\n"
        
        instructions += """
## Guidelines
1. Be helpful and professional
2. Ask for clarification if the request is unclear
3. Confirm actions before executing them
4. Report results clearly and concisely

## Copilot Studio Notes
This agent was transpiled from a RAPP Python/JSON agent. The system prompt above
has been automatically configured as the GPT component instructions in Copilot Studio.
"""
        return instructions
    
    def _generate_topics(self, agent_def: Dict, analysis: Dict) -> Dict:
        """Generate Copilot Studio topics."""
        topics = {}
        
        # Greeting topic
        topics["topic_greeting.yaml"] = {
            "kind": "AdaptiveDialog",
            "id": "topic_greeting",
            "displayName": "Greeting",
            "triggers": [
                {"kind": "OnRecognizedIntent", "intent": "Greeting"}
            ],
            "actions": [
                {
                    "kind": "SendMessage",
                    "message": f"Hello! I'm the {agent_def.get('name', 'Agent')}. {agent_def.get('description', '')[:200]} How can I help you today?"
                }
            ]
        }
        
        # Generate topic for each action
        for action in agent_def.get("actions", []):
            action_name = action.get("name", "unknown")
            topic_id = f"topic_{action_name}"
            
            # Build trigger phrases
            trigger_phrases = [
                action_name.replace("_", " "),
                f"run {action_name.replace('_', ' ')}",
                f"execute {action_name.replace('_', ' ')}"
            ]
            
            # Build topic actions
            topic_actions = []
            
            if action.get("needs_flow", True):
                # Call Power Automate flow
                topic_actions.append({
                    "kind": "InvokeFlowAction",
                    "flowId": f"flow_{action_name}",
                    "inputs": self._get_action_inputs(action),
                    "outputs": {"result": "flowResult"}
                })
                topic_actions.append({
                    "kind": "SendMessage",
                    "message": "${flowResult}"
                })
            else:
                # Simple generative response
                topic_actions.append({
                    "kind": "GenerativeAnswer",
                    "prompt": f"Help the user with: {action_name.replace('_', ' ')}"
                })
            
            topics[f"{topic_id}.yaml"] = {
                "kind": "AdaptiveDialog",
                "id": topic_id,
                "displayName": self._to_title_case(action_name),
                "triggers": [
                    {
                        "kind": "OnRecognizedIntent",
                        "intent": action_name,
                        "triggerQueries": trigger_phrases
                    }
                ],
                "actions": topic_actions
            }
        
        return topics
    
    def _generate_flows(self, agent_def: Dict, analysis: Dict, 
                        use_dataverse: bool = True) -> Dict:
        """Generate Power Automate flows for complex actions."""
        flows = {}
        
        for action_name in analysis.get("flows_needed", []):
            flow_id = f"flow_{action_name}"
            
            # Build flow definition
            flow = {
                "name": flow_id,
                "displayName": f"{self._to_title_case(action_name)} Flow",
                "description": f"Power Automate flow for {action_name}",
                "trigger": {
                    "kind": "PowerVirtualAgents",
                    "inputs": self._get_action_inputs_schema(action_name, agent_def)
                },
                "actions": self._build_flow_actions(action_name, agent_def, analysis, use_dataverse),
                "outputs": {
                    "result": {
                        "type": "string",
                        "description": "Result of the action"
                    }
                }
            }
            
            flows[f"{flow_id}.json"] = flow
        
        return flows
    
    def _build_flow_actions(self, action_name: str, agent_def: Dict, 
                           analysis: Dict, use_dataverse: bool) -> List[Dict]:
        """Build Power Automate actions for a flow."""
        actions = []
        
        # Check what connectors are needed
        connectors = {c["type"]: c for c in analysis.get("connectors", [])}
        
        if "salesforce" in connectors:
            actions.append({
                "kind": "Salesforce_GetRecords",
                "connection": "salesforce_connection",
                "inputs": {
                    "object": "Case",
                    "query": "SELECT Id, Subject, Description FROM Case"
                },
                "outputs": {"records": "sfRecords"}
            })
        
        if "cosmos_db" in connectors and not use_dataverse:
            actions.append({
                "kind": "CosmosDB_QueryDocuments",
                "connection": "cosmosdb_connection",
                "inputs": {
                    "database": "rapp_db",
                    "collection": "agents"
                },
                "outputs": {"documents": "cosmosData"}
            })
        elif use_dataverse:
            actions.append({
                "kind": "Dataverse_ListRows",
                "connection": "dataverse_connection",
                "inputs": {
                    "entityName": "rapp_data"
                },
                "outputs": {"rows": "dataverseRows"}
            })
        
        # Add AI processing if needed
        if "generative_ai" in analysis.get("native_capabilities", []):
            actions.append({
                "kind": "AzureOpenAI_ChatCompletion",
                "connection": "azure_openai_connection",
                "inputs": {
                    "prompt": f"Process the data for {action_name}",
                    "systemMessage": agent_def.get("description", "")
                },
                "outputs": {"response": "aiResponse"}
            })
        
        # Return result
        actions.append({
            "kind": "Response",
            "inputs": {
                "result": "@{variables('aiResponse') ?? 'Action completed successfully'}"
            }
        })
        
        return actions
    
    def _generate_connector_configs(self, analysis: Dict) -> Dict:
        """Generate connector configuration."""
        connectors = {}
        
        for conn in analysis.get("connectors", []):
            connectors[conn["type"]] = {
                "connectorId": conn["connector_id"],
                "displayName": conn["display_name"],
                "connectionRequired": True,
                "authType": "OAuth2" if conn["type"] in ["salesforce", "sharepoint"] else "ApiKey"
            }
        
        return {
            "connectors": connectors,
            "instructions": "Configure each connector in Power Platform admin center before importing the solution."
        }
    
    def _generate_deployment_guide(self, agent_name: str, analysis: Dict) -> str:
        """Generate deployment guide markdown."""
        guide = f"""# Deployment Guide: {agent_name}

## Overview
This guide covers deploying the transpiled Copilot Studio agent.

## Prerequisites
1. Copilot Studio license
2. Power Platform environment
"""
        
        if analysis.get("connectors"):
            guide += "\n### Required Connectors\n"
            for conn in analysis["connectors"]:
                guide += f"- **{conn['display_name']}** ({conn['connector_id']})\n"
        
        guide += """
## Deployment Steps

### 1. Import the Solution
1. Go to [Power Platform Admin Center](https://admin.powerplatform.microsoft.com)
2. Select your environment
3. Go to Solutions > Import
4. Upload the solution package

### 2. Configure Connectors
"""
        
        if analysis.get("connectors"):
            for conn in analysis["connectors"]:
                guide += f"""
#### {conn['display_name']}
1. Go to Connections in Power Platform
2. Create new connection for {conn['display_name']}
3. Authenticate with your credentials
4. Link to the flows in this solution
"""
        
        guide += """
### 3. Configure the Agent
1. Open Copilot Studio
2. Find the imported agent
3. Review and customize instructions
4. Test the agent in the test canvas

### 4. Publish
1. Click "Publish" in Copilot Studio
2. Configure channels (Teams, Web, etc.)
3. Deploy to users

## Testing
Run through each topic to verify:
- Greeting works
- Each action topic triggers correctly
- Flows execute and return results
- Connectors are authenticated

## Troubleshooting
- **Flow not triggering**: Check Power Automate run history
- **Connector errors**: Verify connection credentials
- **Topic not matching**: Review trigger phrases
"""
        
        return guide
    
    def _get_action_inputs(self, action: Dict) -> Dict:
        """Get input parameters for an action."""
        return {"action": action.get("name", "unknown")}
    
    def _get_action_inputs_schema(self, action_name: str, agent_def: Dict) -> Dict:
        """Get input schema for a flow."""
        return {
            "type": "object",
            "properties": {
                "action": {"type": "string"},
                "parameters": {"type": "object"}
            }
        }
    
    # =========================================================================
    # SAVE METHODS
    # =========================================================================
    
    def _save_solution(self, agent_name: str, solution: Dict, output_format: str) -> str:
        """Save the generated solution files."""
        # Create output directory
        snake_name = self._to_snake_case(agent_name)
        output_dir = os.path.join(self.output_path, snake_name)
        os.makedirs(output_dir, exist_ok=True)
        
        # Create subdirectories
        os.makedirs(os.path.join(output_dir, "topics"), exist_ok=True)
        os.makedirs(os.path.join(output_dir, "flows"), exist_ok=True)
        
        for filename, content in solution.items():
            # Determine subdirectory
            if "topic" in filename.lower():
                filepath = os.path.join(output_dir, "topics", filename)
            elif "flow" in filename.lower():
                filepath = os.path.join(output_dir, "flows", filename)
            else:
                filepath = os.path.join(output_dir, filename)
            
            # Write content
            with open(filepath, 'w', encoding='utf-8') as f:
                if isinstance(content, dict):
                    if filename.endswith('.yaml'):
                        import yaml
                        yaml.dump(content, f, default_flow_style=False, sort_keys=False)
                    else:
                        json.dump(content, f, indent=2)
                else:
                    f.write(content)
        
        return output_dir
    
    def _get_deployment_notes(self, analysis: Dict) -> List[str]:
        """Get deployment notes based on analysis."""
        notes = []
        
        if analysis.get("connectors"):
            notes.append("Configure connectors before importing solution")
        
        if analysis.get("flows_needed"):
            notes.append("Test flows individually before testing full agent")
        
        if analysis.get("agent_type") == "orchestrator":
            notes.append("Orchestrator agents may need topic routing configuration")
        
        return notes
    
    # =========================================================================
    # UTILITY METHODS
    # =========================================================================
    
    def _to_snake_case(self, name: str) -> str:
        """Convert name to snake_case."""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    def _to_title_case(self, name: str) -> str:
        """Convert name to Title Case."""
        return name.replace("_", " ").title()
    
    # =========================================================================
    # BATCH AND PACKAGING METHODS
    # =========================================================================
    
    def _batch_transpile(self, pattern: str = None, agent_list: List[str] = None) -> str:
        """Batch transpile multiple agents matching a pattern."""
        import glob
        
        agents_to_transpile = []
        
        if agent_list:
            agents_to_transpile = agent_list
        elif pattern:
            # Find agents matching pattern
            agents_dir = os.path.join(self.base_path, "agents")
            for f in os.listdir(agents_dir):
                if f.endswith('.py') and pattern.lower() in f.lower():
                    agents_to_transpile.append(f.replace('.py', ''))
        else:
            return json.dumps({"status": "error", "error": "Must provide pattern or agent_list"})
        
        results = []
        for agent_name in agents_to_transpile:
            try:
                agent_def = self._parse_agent(agent_name)
                if agent_def:
                    analysis = self._analyze_dependencies(agent_def)
                    solution = self._generate_solution(agent_def, analysis)
                    output_dir = self._save_solution(agent_name, solution, "solution")
                    results.append({
                        "agent": agent_name,
                        "status": "success",
                        "output_dir": output_dir,
                        "topics": len([k for k in solution.keys() if k.startswith("topic_")]),
                        "flows": len([k for k in solution.keys() if k.startswith("flow_")])
                    })
                else:
                    results.append({"agent": agent_name, "status": "error", "error": "Could not parse"})
            except Exception as e:
                results.append({"agent": agent_name, "status": "error", "error": str(e)})
        
        # Generate combined summary
        successful = [r for r in results if r["status"] == "success"]
        total_topics = sum(r.get("topics", 0) for r in successful)
        total_flows = sum(r.get("flows", 0) for r in successful)
        
        return json.dumps({
            "status": "success",
            "agents_transpiled": len(successful),
            "agents_failed": len(results) - len(successful),
            "total_topics": total_topics,
            "total_flows": total_flows,
            "results": results
        }, indent=2)
    
    def _create_solution_package(self, agent_name: str) -> str:
        """Create a downloadable ZIP package for the solution."""
        import zipfile
        from datetime import datetime
        
        snake_name = self._to_snake_case(agent_name)
        source_dir = os.path.join(self.output_path, snake_name)
        
        if not os.path.exists(source_dir):
            return json.dumps({
                "status": "error",
                "error": f"Solution not found: {source_dir}. Run transpile first."
            })
        
        # Create ZIP file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_filename = f"{snake_name}_copilot_studio_{timestamp}.zip"
        zip_path = os.path.join(self.output_path, zip_filename)
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_dir)
                    zipf.write(file_path, arcname)
        
        return json.dumps({
            "status": "success",
            "package_path": zip_path,
            "package_name": zip_filename,
            "agent_name": agent_name
        }, indent=2)
    # =========================================================================
    # DEPLOYMENT METHODS - Deploy to Copilot Studio via Dataverse API
    # =========================================================================
    
    def _get_deployment_config_file(self) -> str:
        """Get path to deployment configuration file."""
        return os.path.join(self.base_path, "copilot_studio_deployment_config.json")
    
    def _load_deployment_config(self) -> Dict:
        """Load deployment configuration."""
        config_file = self._get_deployment_config_file()
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_deployment_config(self, config: Dict) -> None:
        """Save deployment configuration."""
        config_file = self._get_deployment_config_file()
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
    
    def _configure_deployment(self, **kwargs) -> str:
        """
        Configure deployment settings for Copilot Studio.
        
        Sets up the environment URL, tenant ID, and client ID for API access.
        """
        config = self._load_deployment_config()
        
        # Update with provided values
        if kwargs.get("environment_url"):
            config["environment_url"] = kwargs["environment_url"]
        if kwargs.get("tenant_id"):
            config["tenant_id"] = kwargs["tenant_id"]
        if kwargs.get("client_id"):
            config["client_id"] = kwargs["client_id"]
        
        # Check if any config provided
        if not any([kwargs.get("environment_url"), kwargs.get("tenant_id"), kwargs.get("client_id")]):
            # Return current config and instructions
            return json.dumps({
                "status": "info",
                "current_config": config,
                "instructions": {
                    "setup_steps": [
                        "1. Create an Azure AD app registration in Azure Portal",
                        "2. Add Dataverse/Dynamics CRM API permissions (user_impersonation)",
                        "3. Create a client secret (or use interactive auth)",
                        "4. Get your Dataverse environment URL from Power Platform admin center",
                        "5. Run configure_deployment with environment_url, tenant_id, client_id"
                    ],
                    "example": {
                        "action": "configure_deployment",
                        "environment_url": "https://yourorg.crm.dynamics.com",
                        "tenant_id": "your-tenant-guid",
                        "client_id": "your-app-client-id"
                    },
                    "environment_variables": {
                        "DATAVERSE_ENVIRONMENT_URL": "Alternative to environment_url parameter",
                        "AZURE_TENANT_ID": "Alternative to tenant_id parameter",
                        "COPILOT_STUDIO_CLIENT_ID": "Alternative to client_id parameter",
                        "COPILOT_STUDIO_CLIENT_SECRET": "For service principal auth (optional)"
                    }
                }
            }, indent=2)
        
        self._save_deployment_config(config)
        
        return json.dumps({
            "status": "success",
            "message": "Deployment configuration saved",
            "config": config,
            "next_steps": [
                "Run deploy action with agent_name to deploy a transpiled agent",
                "Example: action='deploy', agent_name='contoso_drains_ci_agent'"
            ]
        }, indent=2)
    
    def _deploy_to_copilot_studio(self, **kwargs) -> str:
        """
        Deploy a transpiled agent to Copilot Studio via Dataverse API.
        
        This creates a new agent in Copilot Studio with all topics and configurations.
        
        Prerequisites:
        - Agent must be transpiled first (action='transpile')
        - Deployment must be configured (action='configure_deployment')
        - User must have Copilot Studio access in the target environment
        """
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            return json.dumps({"status": "error", "error": "agent_name is required"})
        
        # Check for transpiled output
        snake_name = self._to_snake_case(agent_name)
        agent_dir = os.path.join(self.output_path, snake_name)
        
        if not os.path.exists(agent_dir):
            return json.dumps({
                "status": "error",
                "error": f"Transpiled agent not found at {agent_dir}",
                "suggestion": f"Run transpile first: action='transpile', agent_name='{agent_name}'"
            })
        
        # Load agent manifest
        manifest_path = os.path.join(agent_dir, "agent_manifest.json")
        if not os.path.exists(manifest_path):
            return json.dumps({
                "status": "error",
                "error": f"Agent manifest not found: {manifest_path}"
            })
        
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        # Load topics
        topics = []
        topics_dir = os.path.join(agent_dir, "topics")
        if os.path.exists(topics_dir):
            for topic_file in os.listdir(topics_dir):
                if topic_file.endswith('.yaml'):
                    import yaml
                    with open(os.path.join(topics_dir, topic_file), 'r') as f:
                        topics.append(yaml.safe_load(f))
                elif topic_file.endswith('.json'):
                    with open(os.path.join(topics_dir, topic_file), 'r') as f:
                        topics.append(json.load(f))
        
        # Get deployment config
        config = self._load_deployment_config()
        
        # Override with kwargs
        environment_url = kwargs.get("environment_url") or config.get("environment_url") or os.environ.get("DATAVERSE_ENVIRONMENT_URL")
        tenant_id = kwargs.get("tenant_id") or config.get("tenant_id") or os.environ.get("AZURE_TENANT_ID")
        client_id = kwargs.get("client_id") or config.get("client_id") or os.environ.get("COPILOT_STUDIO_CLIENT_ID")
        
        if not environment_url:
            return json.dumps({
                "status": "error",
                "error": "environment_url is required",
                "suggestion": "Run configure_deployment first or set DATAVERSE_ENVIRONMENT_URL"
            })
        
        try:
            # Import and use CopilotStudioClient
            from utils.copilot_studio_api import CopilotStudioClient, CopilotStudioAPIError
            
            client = CopilotStudioClient(
                environment_url=environment_url,
                tenant_id=tenant_id,
                client_id=client_id,
                use_interactive_auth=True  # Will prompt for login if no secret
            )
            
            # Authenticate
            client.authenticate()
            
            # Deploy using the client's deploy method
            result = client.deploy_transpiled_agent(
                agent_manifest=manifest,
                topics=topics,
                flows=[]  # Power Automate flows handled separately
            )
            
            # Save deployment result
            deployment_record = {
                "agent_name": agent_name,
                "deployed_at": datetime.now().isoformat(),
                "environment_url": environment_url,
                "bot_id": result.get("bot_id"),
                "topic_ids": result.get("topic_ids", []),
                "status": result.get("status")
            }
            
            deployments_file = os.path.join(agent_dir, "deployment_history.json")
            history = []
            if os.path.exists(deployments_file):
                with open(deployments_file, 'r') as f:
                    history = json.load(f)
            history.append(deployment_record)
            with open(deployments_file, 'w') as f:
                json.dump(history, f, indent=2)
            
            return json.dumps({
                "status": "success",
                "message": f"Agent '{agent_name}' deployed to Copilot Studio",
                "deployment": deployment_record,
                "next_steps": [
                    f"Open Copilot Studio: {environment_url.replace('.crm.dynamics.com', '.powerva.microsoft.com')}",
                    f"Find your agent by name: {manifest.get('displayName', agent_name)}",
                    "Test the agent using the Test pane",
                    "Publish the agent when ready"
                ]
            }, indent=2)
            
        except ImportError as e:
            return json.dumps({
                "status": "error",
                "error": "CopilotStudioClient not available",
                "details": str(e),
                "suggestion": "Ensure utils/copilot_studio_api.py exists and dependencies are installed (requests, azure-identity or msal)"
            })
        except Exception as e:
            import traceback
            return json.dumps({
                "status": "error",
                "error": str(e),
                "traceback": traceback.format_exc(),
                "suggestion": "Check deployment configuration and ensure you have access to the Copilot Studio environment"
            })
    
    def _check_deployment_status(self, **kwargs) -> str:
        """
        Check the deployment status and history for an agent.
        """
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            # List all deployments
            all_deployments = []
            if os.path.exists(self.output_path):
                for agent_dir in os.listdir(self.output_path):
                    history_file = os.path.join(self.output_path, agent_dir, "deployment_history.json")
                    if os.path.exists(history_file):
                        with open(history_file, 'r') as f:
                            history = json.load(f)
                            if history:
                                all_deployments.append({
                                    "agent": agent_dir,
                                    "last_deployment": history[-1],
                                    "total_deployments": len(history)
                                })
            
            return json.dumps({
                "status": "success",
                "deployments": all_deployments,
                "total_agents_deployed": len(all_deployments)
            }, indent=2)
        
        # Get specific agent deployment history
        snake_name = self._to_snake_case(agent_name)
        history_file = os.path.join(self.output_path, snake_name, "deployment_history.json")
        
        if not os.path.exists(history_file):
            return json.dumps({
                "status": "info",
                "agent_name": agent_name,
                "message": "No deployments found for this agent",
                "suggestion": f"Run deploy action: action='deploy', agent_name='{agent_name}'"
            })
        
        with open(history_file, 'r') as f:
            history = json.load(f)
        
        return json.dumps({
            "status": "success",
            "agent_name": agent_name,
            "deployment_history": history,
            "last_deployment": history[-1] if history else None,
            "total_deployments": len(history)
        }, indent=2)
    
    # =========================================================================
    # SOLUTION-BASED DEPLOYMENT - Deploy multiple agents as a unified solution
    # =========================================================================
    
    def _get_solutions_file(self) -> str:
        """Get path to solutions definition file."""
        return os.path.join(self.base_path, "copilot_studio_solutions.json")
    
    def _load_solutions(self) -> Dict:
        """Load solution definitions."""
        solutions_file = self._get_solutions_file()
        if os.path.exists(solutions_file):
            with open(solutions_file, 'r') as f:
                return json.load(f)
        return {"solutions": {}}
    
    def _save_solutions(self, data: Dict) -> None:
        """Save solution definitions."""
        solutions_file = self._get_solutions_file()
        with open(solutions_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _create_solution_definition(self, **kwargs) -> str:
        """
        Create or update a solution definition that groups multiple agents.
        
        A solution is a logical grouping of agents that work together.
        This is similar to Power Platform solutions that contain multiple components.
        """
        solution_name = kwargs.get("solution_name")
        if not solution_name:
            return json.dumps({
                "status": "error",
                "error": "solution_name is required"
            })
        
        data = self._load_solutions()
        
        # Get existing or create new solution
        solution = data["solutions"].get(solution_name, {
            "name": solution_name,
            "display_name": kwargs.get("display_name", solution_name.replace("_", " ").title()),
            "description": kwargs.get("description", ""),
            "publisher": kwargs.get("publisher", "RAPP"),
            "version": kwargs.get("version", "1.0.0"),
            "agents": [],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        })
        
        # Update properties if provided
        if kwargs.get("display_name"):
            solution["display_name"] = kwargs["display_name"]
        if kwargs.get("description"):
            solution["description"] = kwargs["description"]
        if kwargs.get("publisher"):
            solution["publisher"] = kwargs["publisher"]
        if kwargs.get("version"):
            solution["version"] = kwargs["version"]
        
        # Add agents
        agents_to_add = kwargs.get("agents", [])
        if isinstance(agents_to_add, str):
            agents_to_add = [agents_to_add]
        
        for agent in agents_to_add:
            agent_snake = self._to_snake_case(agent)
            if agent_snake not in solution["agents"]:
                # Verify agent exists
                agent_dir = os.path.join(self.output_path, agent_snake)
                if os.path.exists(agent_dir):
                    solution["agents"].append(agent_snake)
                else:
                    logger.warning(f"Agent not found (not transpiled yet?): {agent_snake}")
        
        # Remove agents
        agents_to_remove = kwargs.get("remove_agents", [])
        if isinstance(agents_to_remove, str):
            agents_to_remove = [agents_to_remove]
        
        for agent in agents_to_remove:
            agent_snake = self._to_snake_case(agent)
            if agent_snake in solution["agents"]:
                solution["agents"].remove(agent_snake)
        
        solution["updated_at"] = datetime.now().isoformat()
        data["solutions"][solution_name] = solution
        self._save_solutions(data)
        
        return json.dumps({
            "status": "success",
            "message": f"Solution '{solution_name}' updated",
            "solution": solution,
            "next_steps": [
                f"Add more agents: action='create_solution', solution_name='{solution_name}', agents=['agent_name']",
                f"Deploy solution: action='deploy_solution', solution_name='{solution_name}'",
                f"View all solutions: action='list_solutions'"
            ]
        }, indent=2)
    
    def _list_solutions(self, **kwargs) -> str:
        """List all defined solutions and their agents."""
        data = self._load_solutions()
        
        solution_name = kwargs.get("solution_name")
        if solution_name:
            # Return specific solution details
            solution = data["solutions"].get(solution_name)
            if not solution:
                return json.dumps({
                    "status": "error",
                    "error": f"Solution not found: {solution_name}"
                })
            
            # Enrich with agent details
            agent_details = []
            for agent_name in solution["agents"]:
                agent_dir = os.path.join(self.output_path, agent_name)
                manifest_path = os.path.join(agent_dir, "agent_manifest.json")
                if os.path.exists(manifest_path):
                    with open(manifest_path, 'r') as f:
                        manifest = json.load(f)
                    agent_details.append({
                        "name": agent_name,
                        "display_name": manifest.get("displayName", agent_name),
                        "description": manifest.get("description", "")[:100] + "..."
                    })
                else:
                    agent_details.append({
                        "name": agent_name,
                        "status": "not transpiled"
                    })
            
            return json.dumps({
                "status": "success",
                "solution": solution,
                "agent_details": agent_details
            }, indent=2)
        
        # List all solutions
        solutions_summary = []
        for name, sol in data["solutions"].items():
            solutions_summary.append({
                "name": name,
                "display_name": sol.get("display_name", name),
                "agent_count": len(sol.get("agents", [])),
                "version": sol.get("version", "1.0.0"),
                "updated_at": sol.get("updated_at")
            })
        
        return json.dumps({
            "status": "success",
            "solutions": solutions_summary,
            "total_solutions": len(solutions_summary)
        }, indent=2)
    
    def _deploy_solution(self, **kwargs) -> str:
        """
        Deploy a complete solution with all its agents to Copilot Studio.
        
        This creates all agents in the solution as a cohesive set in Copilot Studio.
        Each agent is created with proper metadata linking it to the solution.
        
        Prerequisites:
        - Solution must be defined (action='create_solution')
        - All agents in the solution must be transpiled
        - Deployment must be configured (action='configure_deployment')
        """
        solution_name = kwargs.get("solution_name")
        if not solution_name:
            # Check for predefined solution patterns
            if kwargs.get("predefined") == "contoso":
                return self._deploy_contoso_solution(**kwargs)
            
            return json.dumps({
                "status": "error",
                "error": "solution_name is required",
                "alternatives": {
                    "predefined_solutions": [
                        "Use predefined='contoso' for Contoso CI solution"
                    ],
                    "create_custom": "Use action='create_solution' first"
                }
            })
        
        data = self._load_solutions()
        solution = data["solutions"].get(solution_name)
        
        if not solution:
            return json.dumps({
                "status": "error",
                "error": f"Solution not found: {solution_name}",
                "suggestion": "Use action='create_solution' to define a solution first"
            })
        
        if not solution.get("agents"):
            return json.dumps({
                "status": "error",
                "error": f"Solution '{solution_name}' has no agents",
                "suggestion": "Add agents: action='create_solution', solution_name='...', agents=[...]"
            })
        
        # Get deployment config
        config = self._load_deployment_config()
        environment_url = kwargs.get("environment_url") or config.get("environment_url")
        tenant_id = kwargs.get("tenant_id") or config.get("tenant_id")
        client_id = kwargs.get("client_id") or config.get("client_id")
        
        if not environment_url:
            return json.dumps({
                "status": "error",
                "error": "Deployment not configured",
                "suggestion": "Run action='configure_deployment' first"
            })
        
        # Deploy all agents in the solution
        deployment_results = {
            "status": "success",
            "solution_name": solution_name,
            "environment_url": environment_url,
            "deployed_at": datetime.now().isoformat(),
            "agents_deployed": [],
            "agents_failed": [],
            "errors": []
        }
        
        try:
            from utils.copilot_studio_api import CopilotStudioClient, CopilotStudioAPIError
            
            client = CopilotStudioClient(
                environment_url=environment_url,
                tenant_id=tenant_id,
                client_id=client_id,
                use_interactive_auth=True
            )
            
            # Authenticate once for all deployments
            logger.info("Authenticating to Copilot Studio...")
            client.authenticate()
            logger.info("Authentication successful")
            
            # Deploy each agent
            for agent_name in solution["agents"]:
                try:
                    agent_dir = os.path.join(self.output_path, agent_name)
                    manifest_path = os.path.join(agent_dir, "agent_manifest.json")
                    
                    if not os.path.exists(manifest_path):
                        deployment_results["agents_failed"].append({
                            "agent": agent_name,
                            "error": "Not transpiled"
                        })
                        continue
                    
                    with open(manifest_path, 'r') as f:
                        manifest = json.load(f)
                    
                    # Create short display name (max 42 chars for Copilot Studio)
                    # Use abbreviations for solution prefix
                    solution_prefix = kwargs.get("name_prefix", "ZE")  # ZE = Contoso
                    base_name = manifest.get('displayName', agent_name)
                    # Shorten common words
                    base_name = base_name.replace("Competitive Intelligence", "CI")
                    base_name = base_name.replace("Orchestrator", "Orch")
                    base_name = base_name.replace("Synthesizer", "Synth")
                    base_name = base_name.replace("Agent", "")
                    base_name = base_name.replace("Contoso ", "")
                    base_name = base_name.strip()
                    
                    display_name = f"{solution_prefix} {base_name}"[:42]
                    description = f"Part of {solution['display_name']} solution (v{solution['version']}). {manifest.get('description', '')}"
                    
                    # CRITICAL: Get instructions from manifest for GPT component
                    # This is what makes the agent actually work in Copilot Studio!
                    instructions = manifest.get("instructions") or manifest.get("systemPrompt", "")
                    if not instructions:
                        # Try to load from instructions.md file
                        instructions_path = os.path.join(agent_dir, "instructions.md")
                        if os.path.exists(instructions_path):
                            with open(instructions_path, 'r', encoding='utf-8') as f:
                                instructions = f.read()
                    
                    if not instructions:
                        # Fallback to description
                        instructions = f"You are {display_name}. {description}"
                    
                    logger.info(f"Agent instructions length: {len(instructions)} chars")
                    
                    # Load topics
                    topics = []
                    topics_dir = os.path.join(agent_dir, "topics")
                    if os.path.exists(topics_dir):
                        for topic_file in os.listdir(topics_dir):
                            topic_path = os.path.join(topics_dir, topic_file)
                            if topic_file.endswith('.yaml'):
                                import yaml
                                with open(topic_path, 'r') as f:
                                    topics.append(yaml.safe_load(f))
                            elif topic_file.endswith('.json'):
                                with open(topic_path, 'r') as f:
                                    topics.append(json.load(f))
                    
                    # Create the agent WITH instructions (GPT component created automatically!)
                    logger.info(f"Creating agent: {display_name}")
                    bot_id = client.create_agent(
                        name=display_name,
                        description=description[:500],  # Truncate if too long
                        instructions=instructions,  # CRITICAL: Pass instructions for GPT component
                        language=manifest.get("primaryLanguage", "en-us")
                    )
                    
                    # Create topics for the agent
                    topic_ids = []
                    for topic in topics:
                        try:
                            trigger_phrases = []
                            if "triggers" in topic:
                                for trigger in topic.get("triggers", []):
                                    trigger_phrases.extend(trigger.get("triggerQueries", []))
                            
                            topic_id = client.create_topic(
                                bot_id=bot_id,
                                name=topic.get("displayName", topic.get("name", "Unknown")),
                                trigger_phrases=trigger_phrases,
                                description=topic.get("description", "")
                            )
                            topic_ids.append(topic_id)
                        except Exception as topic_error:
                            logger.warning(f"Failed to create topic: {topic_error}")
                    
                    deployment_results["agents_deployed"].append({
                        "agent": agent_name,
                        "bot_id": bot_id,
                        "display_name": display_name,
                        "topics_created": len(topic_ids),
                        "has_instructions": bool(instructions)
                    })
                    logger.info(f"Successfully deployed: {agent_name} ({bot_id}) with GPT instructions")
                    
                except Exception as agent_error:
                    deployment_results["agents_failed"].append({
                        "agent": agent_name,
                        "error": str(agent_error)
                    })
                    deployment_results["errors"].append(f"{agent_name}: {str(agent_error)}")
                    logger.error(f"Failed to deploy {agent_name}: {agent_error}")
            
            # Update solution with deployment info
            if "deployments" not in solution:
                solution["deployments"] = []
            solution["deployments"].append({
                "environment_url": environment_url,
                "deployed_at": deployment_results["deployed_at"],
                "agents_deployed": len(deployment_results["agents_deployed"]),
                "agents_failed": len(deployment_results["agents_failed"])
            })
            data["solutions"][solution_name] = solution
            self._save_solutions(data)
            
            # Set overall status
            if deployment_results["agents_failed"]:
                if deployment_results["agents_deployed"]:
                    deployment_results["status"] = "partial"
                else:
                    deployment_results["status"] = "failed"
            
            # Add next steps
            copilot_studio_url = environment_url.replace('.crm.dynamics.com', '.powervirtualagents.com')
            deployment_results["next_steps"] = [
                f"Open Copilot Studio: {copilot_studio_url}",
                f"Find agents by searching for: [{solution['display_name']}]",
                "Configure connectors and test each agent",
                "Publish agents when ready"
            ]
            
        except ImportError as e:
            deployment_results["status"] = "error"
            deployment_results["errors"].append(f"Missing dependency: {str(e)}")
        except Exception as e:
            deployment_results["status"] = "error"
            deployment_results["errors"].append(str(e))
            import traceback
            deployment_results["traceback"] = traceback.format_exc()
        
        return json.dumps(deployment_results, indent=2)
    
    def _deploy_contoso_solution(self, **kwargs) -> str:
        """
        Deploy the predefined Contoso Competitive Intelligence solution.
        
        This is a convenience method for the complete Contoso CI system:
        - 1 Orchestrator agent (coordinates all BU agents)
        - 5 Business Unit agents (Drains, Drinking Water, Sinks, Commercial Brass, Wilkins)
        - 1 Cross-BU Synthesizer agent (aggregates insights)
        """
        # Define the Contoso solution
        contoso_agents = [
            "contoso_ci_orchestrator_agent",
            "contoso_drains_ci_agent",
            "contoso_drinking_water_ci_agent",
            "contoso_sinks_ci_agent",
            "contoso_commercial_brass_ci_agent",
            "contoso_wilkins_ci_agent",
            "contoso_crossbu_synthesizer_agent"
        ]
        
        # First, create/update the solution definition
        solution_result = json.loads(self._create_solution_definition(
            solution_name="contoso_competitive_intelligence",
            display_name="Contoso Competitive Intelligence",
            description="Multi-agent competitive intelligence system for Contoso with orchestrated BU-specific agents and cross-BU synthesis capabilities.",
            publisher="RAPP",
            version=kwargs.get("version", "1.0.0"),
            agents=contoso_agents
        ))
        
        if solution_result.get("status") != "success":
            return json.dumps(solution_result)
        
        # Check which agents are transpiled
        missing_agents = []
        for agent in contoso_agents:
            agent_dir = os.path.join(self.output_path, agent)
            if not os.path.exists(agent_dir):
                missing_agents.append(agent)
        
        if missing_agents:
            return json.dumps({
                "status": "info",
                "message": "Some agents need to be transpiled first",
                "missing_agents": missing_agents,
                "transpiled_agents": [a for a in contoso_agents if a not in missing_agents],
                "next_steps": [
                    "Run batch_transpile for missing agents:",
                    f"action='batch_transpile', agent_list={missing_agents}",
                    "Then run: action='deploy_solution', predefined='contoso'"
                ]
            }, indent=2)
        
        # Deploy the solution
        return self._deploy_solution(solution_name="contoso_competitive_intelligence", **kwargs)

SUPPORTED_PLATFORMS = {
    "m365_copilot": {
        "name": "M365 Copilot Declarative Agent",
        "description": "Declarative agents for Microsoft 365 Copilot with API plugins",
        "output_files": ["declarativeAgent.json", "plugin.json", "openapi.yaml"],
        "best_for": ["Teams integration", "Outlook integration", "SharePoint integration"]
    },
    "copilot_studio": {
        "name": "Copilot Studio Agent",
        "description": "Low-code agents with Power Platform connectors",
        "output_files": ["agent.yaml", "topics/*.yaml", "connector.json"],
        "best_for": ["Power Platform", "Low-code", "Business users"]
    },
    "azure_foundry": {
        "name": "Azure AI Foundry Agent",
        "description": "Full Python agents with Azure AI Agent Service",
        "output_files": ["agent.py", "tools.py", "config.yaml"],
        "best_for": ["Complex logic", "Custom integrations", "Full control"]
    }
}

M365_MANIFEST_VERSION = "v1.6"

class _ExportEngine(_EngineBase):
    """
    Multi-Platform Agent Factory - Transpiles RAPP agents to various platforms.
    
    Capabilities:
    - transpile: Convert agent to target platform format
    - analyze: Recommend best platform for an agent
    - generate_openapi: Create OpenAPI spec for RAPP Function App
    - preview: Show what would be generated without saving
    - list_platforms: Show supported target platforms
    """
    
    def __init__(self):
        self.name = "AgentTranspiler"
        self.metadata = {
            "name": self.name,
            "description": "Converts RAPP agent definitions to M365 Copilot, Copilot Studio, or Azure AI Foundry formats.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": [
                            "transpile",
                            "analyze",
                            "generate_openapi",
                            "preview",
                            "list_platforms",
                            "batch_transpile"
                        ],
                        "description": "The transpilation action to perform"
                    },
                    "agent_name": {
                        "type": "string",
                        "description": "Name of the RAPP agent to transpile"
                    },
                    "target_platform": {
                        "type": "string",
                        "enum": ["m365_copilot", "copilot_studio", "azure_foundry", "all"],
                        "description": "Target platform for transpilation"
                    },
                    "agent_json": {
                        "type": "object",
                        "description": "Optional: Direct agent JSON instead of loading by name"
                    },
                    "function_app_url": {
                        "type": "string",
                        "description": "URL of the RAPP Function App for API connections"
                    },
                    "save_files": {
                        "type": "boolean",
                        "description": "Whether to save generated files to disk",
                        "default": False
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Path to save generated files"
                    }
                },
                "required": ["action"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)
        
        # Paths
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.demos_path = os.path.join(self.base_path, "demos")
        self.agents_path = os.path.join(self.base_path, "agents")
        self.output_path = os.path.join(self.base_path, "transpiled")
    
    def run(self, **kwargs) -> str:
        """Route to appropriate action handler."""
        action = kwargs.get("action", "list_platforms")
        
        actions = {
            "transpile": self._transpile,
            "analyze": self._analyze,
            "generate_openapi": self._generate_openapi,
            "preview": self._preview,
            "list_platforms": self._list_platforms,
            "batch_transpile": self._batch_transpile,
        }
        
        if action not in actions:
            return json.dumps({
                "status": "error",
                "error": f"Unknown action: {action}",
                "available_actions": list(actions.keys())
            })
        
        try:
            return actions[action](**kwargs)
        except Exception as e:
            logger.error(f"Error in AgentTranspiler.{action}: {e}")
            return json.dumps({
                "status": "error",
                "error": str(e)
            })
    
    # =========================================================================
    # ACTION HANDLERS
    # =========================================================================
    
    def _list_platforms(self, **kwargs) -> str:
        """List all supported target platforms."""
        return json.dumps({
            "status": "success",
            "platforms": SUPPORTED_PLATFORMS,
            "usage": "Use action='transpile' with target_platform to convert an agent"
        }, indent=2)
    
    def _analyze(self, **kwargs) -> str:
        """Analyze an agent and recommend the best target platform."""
        agent_name = kwargs.get("agent_name")
        agent_json = kwargs.get("agent_json")
        
        if not agent_name and not agent_json:
            return json.dumps({
                "status": "error",
                "error": "Provide either agent_name or agent_json"
            })
        
        # Load agent definition
        agent_def = agent_json or self._load_agent_definition(agent_name)
        if not agent_def:
            return json.dumps({
                "status": "error",
                "error": f"Could not load agent: {agent_name}"
            })
        
        # Analyze complexity
        analysis = self._analyze_agent_complexity(agent_def)
        
        return json.dumps({
            "status": "success",
            "agent_name": agent_def.get("agent", {}).get("name", agent_name),
            "analysis": analysis,
            "recommendations": self._generate_platform_recommendations(analysis)
        }, indent=2)
    
    def _preview(self, **kwargs) -> str:
        """Preview transpilation without saving files."""
        kwargs["save_files"] = False
        return self._transpile(**kwargs)
    
    def _transpile(self, **kwargs) -> str:
        """Transpile an agent to the target platform."""
        agent_name = kwargs.get("agent_name")
        agent_json = kwargs.get("agent_json")
        target_platform = kwargs.get("target_platform", "m365_copilot")
        save_files = kwargs.get("save_files", False)
        function_app_url = kwargs.get("function_app_url", "https://your-function-app.azurewebsites.net")
        
        if not agent_name and not agent_json:
            return json.dumps({
                "status": "error",
                "error": "Provide either agent_name or agent_json"
            })
        
        # Load agent definition
        agent_def = agent_json or self._load_agent_definition(agent_name)
        if not agent_def:
            return json.dumps({
                "status": "error",
                "error": f"Could not load agent: {agent_name}"
            })
        
        results = {}
        platforms_to_generate = (
            list(SUPPORTED_PLATFORMS.keys()) 
            if target_platform == "all" 
            else [target_platform]
        )
        
        for platform in platforms_to_generate:
            if platform == "m365_copilot":
                results[platform] = self._transpile_to_m365(agent_def, function_app_url)
            elif platform == "copilot_studio":
                results[platform] = self._transpile_to_copilot_studio(agent_def, function_app_url)
            elif platform == "azure_foundry":
                results[platform] = self._transpile_to_azure_foundry(agent_def, function_app_url)
        
        # Save files if requested
        if save_files:
            saved_paths = self._save_transpiled_files(agent_name or "agent", results)
            
            # Create a preview by truncating long string values
            def truncate_value(v):
                if isinstance(v, str) and len(v) > 500:
                    return v[:500] + "..."
                return str(v)[:500] + "..." if len(str(v)) > 500 else v
            
            preview = {}
            for platform, files in results.items():
                preview[platform] = {fk: truncate_value(fv) for fk, fv in files.items()}
            
            return json.dumps({
                "status": "success",
                "message": "Files generated and saved",
                "saved_paths": saved_paths,
                "preview": preview
            }, indent=2)
        
        return json.dumps({
            "status": "success",
            "transpiled": results
        }, indent=2)
    
    def _batch_transpile(self, **kwargs) -> str:
        """Transpile multiple agents at once."""
        agent_names = kwargs.get("agent_names", [])
        target_platform = kwargs.get("target_platform", "all")
        
        if not agent_names:
            # Get all agents from demos folder
            agent_names = self._list_available_agents()
        
        results = {}
        for name in agent_names:
            result = json.loads(self._transpile(
                agent_name=name,
                target_platform=target_platform,
                save_files=kwargs.get("save_files", False),
                function_app_url=kwargs.get("function_app_url")
            ))
            results[name] = result.get("status")
        
        return json.dumps({
            "status": "success",
            "processed": len(results),
            "results": results
        }, indent=2)
    
    def _generate_openapi(self, **kwargs) -> str:
        """Generate OpenAPI spec for the RAPP Function App."""
        function_app_url = kwargs.get("function_app_url", "https://your-function-app.azurewebsites.net")
        include_agents = kwargs.get("include_agents", None)
        
        # Get all agents or filter
        agents = []
        if include_agents:
            for name in include_agents:
                agent_def = self._load_agent_definition(name)
                if agent_def:
                    agents.append(agent_def)
        else:
            for name in self._list_available_agents():
                agent_def = self._load_agent_definition(name)
                if agent_def:
                    agents.append(agent_def)
        
        openapi_spec = self._build_openapi_spec(agents, function_app_url)
        
        return json.dumps({
            "status": "success",
            "openapi_spec": openapi_spec,
            "agents_included": len(agents)
        }, indent=2)
    
    # =========================================================================
    # PLATFORM-SPECIFIC TRANSPILERS
    # =========================================================================
    
    def _transpile_to_m365(self, agent_def: Dict, function_app_url: str) -> Dict:
        """Transpile to M365 Copilot Declarative Agent format."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        description = agent_info.get("description", "RAPP Agent")
        
        # Build instructions from system_prompt or description
        instructions = agent_def.get("system_prompt", agent_def.get("systemPrompt", ""))
        if not instructions:
            instructions = f"You are {agent_name}. {description}"
        
        # Get actions/capabilities
        actions = agent_def.get("actions", [])
        metadata = agent_def.get("metadata", {})
        
        # Build conversation starters from demo_conversation
        conversation_starters = []
        demo_conv = agent_def.get("demo_conversation", agent_def.get("demoConversation", []))
        for msg in demo_conv:
            if msg.get("role") == "user":
                conversation_starters.append({
                    "title": msg.get("content", "")[:50],
                    "text": msg.get("content", "")
                })
        
        # Limit to 6 starters
        conversation_starters = conversation_starters[:6]
        
        # Build declarative agent manifest
        declarative_agent = {
            "$schema": f"https://developer.microsoft.com/json-schemas/copilot/declarative-agent/{M365_MANIFEST_VERSION}/schema.json",
            "version": M365_MANIFEST_VERSION,
            "name": agent_name,
            "description": description[:1000],
            "instructions": instructions[:8000],
            "conversation_starters": conversation_starters,
            "actions": [
                {
                    "id": f"{self._to_snake_case(agent_name)}_plugin",
                    "file": f"{self._to_snake_case(agent_name)}-plugin.json"
                }
            ]
        }
        
        # Build API plugin manifest
        plugin_manifest = self._build_plugin_manifest(agent_def, function_app_url)
        
        # Build OpenAPI spec for this specific agent
        openapi_spec = self._build_agent_openapi(agent_def, function_app_url)
        
        return {
            "declarativeAgent.json": declarative_agent,
            "plugin.json": plugin_manifest,
            "openapi.yaml": openapi_spec
        }
    
    def _transpile_to_copilot_studio(self, agent_def: Dict, function_app_url: str) -> Dict:
        """Transpile to Copilot Studio format."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        description = agent_info.get("description", "RAPP Agent")
        
        # Build system topic with instructions
        instructions = agent_def.get("system_prompt", agent_def.get("systemPrompt", ""))
        
        # Build topics from actions
        topics = {}
        actions = agent_def.get("actions", [])
        
        for i, action in enumerate(actions):
            action_name = action.get("name", f"action_{i}")
            topic_name = self._to_title_case(action_name)
            
            # Get trigger phrases
            trigger_phrases = [action_name.replace("_", " ")]
            if action.get("description"):
                trigger_phrases.append(action["description"][:50])
            
            # Build topic YAML
            topics[f"topic_{action_name}.yaml"] = {
                "kind": "AdaptiveDialog",
                "name": topic_name,
                "triggerQueries": trigger_phrases,
                "actions": [
                    {
                        "kind": "InvokeFlowAction",
                        "flowId": f"/flows/rapp-{self._to_snake_case(agent_name)}",
                        "inputs": {
                            "action": action_name,
                            "parameters": action.get("parameters", [])
                        }
                    },
                    {
                        "kind": "SendMessage",
                        "message": f"I've completed the {topic_name} action. Is there anything else you'd like me to do?"
                    }
                ]
            }
        
        # Build main agent configuration
        agent_config = {
            "schemaVersion": "1.0",
            "kind": "Bot",
            "metadata": {
                "name": agent_name,
                "description": description,
                "icon": agent_info.get("icon", "fa-robot"),
                "category": agent_info.get("category", "productivity")
            },
            "language": {
                "primaryLanguage": "en-us"
            },
            "systemTopic": {
                "kind": "SystemTopic",
                "name": "System",
                "instructions": instructions[:4000] if instructions else description
            },
            "topics": list(topics.keys()),
            "connectors": [
                {
                    "id": f"rapp-{self._to_snake_case(agent_name)}-connector",
                    "type": "CustomConnector",
                    "apiDefinitionUrl": f"{function_app_url}/api/openapi"
                }
            ]
        }
        
        # Build Power Automate flow template
        flow_template = self._build_power_automate_flow(agent_def, function_app_url)
        
        result = {
            "agent.yaml": agent_config,
            "flow_template.json": flow_template
        }
        result.update(topics)
        
        return result
    
    def _transpile_to_azure_foundry(self, agent_def: Dict, function_app_url: str) -> Dict:
        """Transpile to Azure AI Foundry Agent format."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        class_name = self._to_pascal_case(agent_name)
        snake_name = self._to_snake_case(agent_name)
        description = agent_info.get("description", "RAPP Agent")
        
        # Get actions
        actions = agent_def.get("actions", [])
        
        # Build tools.py with function definitions
        tools_code = self._generate_foundry_tools(agent_def)
        
        # Build agent.py
        agent_code = f'''"""
Azure AI Foundry Agent: {agent_name}
Auto-generated from RAPP agent definition

Description: {description}
"""

import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import (
    AgentThread,
    MessageRole,
    FunctionTool,
    ToolSet
)
from {snake_name}_tools import get_tools, execute_tool


class {class_name}Agent:
    """
    {description}
    
    This agent was transpiled from RAPP format for Azure AI Foundry.
    """
    
    def __init__(self, project_connection_string: str = None):
        self.project_connection_string = project_connection_string or os.environ.get("AI_PROJECT_CONNECTION_STRING")
        self.credential = DefaultAzureCredential()
        self.client = AIProjectClient.from_connection_string(
            credential=self.credential,
            conn_str=self.project_connection_string
        )
        self.agent = None
        self.thread = None
        
    def create_agent(self):
        """Create the AI agent with tools."""
        tools = get_tools()
        
        self.agent = self.client.agents.create_agent(
            model="gpt-4o",
            name="{agent_name}",
            instructions="""{description}

{agent_def.get("system_prompt", agent_def.get("systemPrompt", ""))}""",
            tools=tools
        )
        
        self.thread = self.client.agents.create_thread()
        return self.agent.id
    
    def chat(self, user_message: str) -> str:
        """Send a message and get a response."""
        if not self.agent or not self.thread:
            self.create_agent()
        
        # Create message
        self.client.agents.create_message(
            thread_id=self.thread.id,
            role=MessageRole.USER,
            content=user_message
        )
        
        # Run the agent
        run = self.client.agents.create_run(
            thread_id=self.thread.id,
            agent_id=self.agent.id
        )
        
        # Poll for completion and handle tool calls
        while run.status in ["queued", "in_progress", "requires_action"]:
            if run.status == "requires_action":
                tool_outputs = []
                for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                    result = execute_tool(
                        tool_call.function.name,
                        tool_call.function.arguments
                    )
                    tool_outputs.append({{
                        "tool_call_id": tool_call.id,
                        "output": result
                    }})
                
                run = self.client.agents.submit_tool_outputs(
                    thread_id=self.thread.id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )
            else:
                import time
                time.sleep(1)
                run = self.client.agents.get_run(
                    thread_id=self.thread.id,
                    run_id=run.id
                )
        
        # Get the response
        messages = self.client.agents.list_messages(thread_id=self.thread.id)
        return messages.data[0].content[0].text.value
    
    def cleanup(self):
        """Clean up resources."""
        if self.agent:
            self.client.agents.delete_agent(self.agent.id)
        if self.thread:
            self.client.agents.delete_thread(self.thread.id)


# Usage example
if __name__ == "__main__":
    agent = {class_name}Agent()
    agent.create_agent()
    
    response = agent.chat("What can you help me with?")
    print(response)
    
    agent.cleanup()
'''
        
        # Build config.yaml
        config = {
            "agent": {
                "name": agent_name,
                "description": description,
                "model": "gpt-4o",
                "version": "1.0.0"
            },
            "rapp_backend": {
                "url": function_app_url,
                "enabled": True
            },
            "tools": [a.get("name") for a in actions],
            "environment": {
                "AI_PROJECT_CONNECTION_STRING": "${AI_PROJECT_CONNECTION_STRING}",
                "RAPP_FUNCTION_APP_URL": function_app_url
            }
        }
        
        return {
            f"{snake_name}_agent.py": agent_code,
            f"{snake_name}_tools.py": tools_code,
            "config.yaml": config,
            "requirements.txt": "azure-ai-projects>=1.0.0\nazure-identity>=1.15.0\nrequests>=2.31.0"
        }
    
    # =========================================================================
    # HELPER METHODS
    # =========================================================================
    
    def _load_agent_definition(self, agent_name: str) -> Optional[Dict]:
        """Load agent definition from demos folder."""
        # Try different naming patterns
        patterns = [
            f"{agent_name}.json",
            f"{self._to_snake_case(agent_name)}.json",
            f"{self._to_snake_case(agent_name)}_agent.json",
        ]
        
        for pattern in patterns:
            path = os.path.join(self.demos_path, pattern)
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        
        return None
    
    def _list_available_agents(self) -> List[str]:
        """List all available agent definitions."""
        agents = []
        if os.path.exists(self.demos_path):
            for f in os.listdir(self.demos_path):
                if f.endswith('.json') and 'agent' in f.lower():
                    agents.append(f.replace('.json', ''))
        return agents
    
    def _analyze_agent_complexity(self, agent_def: Dict) -> Dict:
        """Analyze agent complexity for platform recommendations."""
        actions = agent_def.get("actions", [])
        has_swarm = "swarm_agents" in agent_def
        has_external_api = any("api" in str(a).lower() or "http" in str(a).lower() for a in actions)
        
        return {
            "action_count": len(actions),
            "has_swarm_orchestration": has_swarm,
            "has_external_api_calls": has_external_api,
            "complexity_score": len(actions) + (10 if has_swarm else 0) + (5 if has_external_api else 0),
            "has_system_prompt": bool(agent_def.get("system_prompt") or agent_def.get("systemPrompt")),
            "has_demo_conversation": bool(agent_def.get("demo_conversation") or agent_def.get("demoConversation"))
        }
    
    def _generate_platform_recommendations(self, analysis: Dict) -> List[Dict]:
        """Generate platform recommendations based on analysis."""
        recs = []
        
        complexity = analysis.get("complexity_score", 0)
        
        # M365 Copilot - good for moderate complexity with M365 integration
        recs.append({
            "platform": "m365_copilot",
            "score": 80 if complexity < 20 else 60,
            "reason": "Best for Teams/Outlook integration with moderate complexity",
            "pros": ["Native M365 integration", "Declarative approach", "Easy deployment"],
            "cons": ["Limited to API plugin actions", "8K instruction limit"]
        })
        
        # Copilot Studio - good for low-code scenarios
        recs.append({
            "platform": "copilot_studio",
            "score": 90 if complexity < 10 else 50,
            "reason": "Best for low-code scenarios and Power Platform integration",
            "pros": ["Visual designer", "Power Automate flows", "Easy for business users"],
            "cons": ["Less flexibility", "May need multiple flows for complex logic"]
        })
        
        # Azure Foundry - good for complex scenarios
        recs.append({
            "platform": "azure_foundry",
            "score": 90 if complexity >= 15 else 70,
            "reason": "Best for complex orchestration and custom logic",
            "pros": ["Full Python control", "Complex tool chains", "Swarm support"],
            "cons": ["Requires coding", "More setup"]
        })
        
        # Sort by score
        recs.sort(key=lambda x: x["score"], reverse=True)
        return recs
    
    def _build_plugin_manifest(self, agent_def: Dict, function_app_url: str) -> Dict:
        """Build API plugin manifest for M365 Copilot."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        
        return {
            "$schema": "https://developer.microsoft.com/json-schemas/copilot/plugin/v2.2/schema.json",
            "schema_version": "v2.2",
            "name_for_human": agent_name,
            "description_for_human": agent_info.get("description", "")[:100],
            "description_for_model": agent_info.get("description", "")[:500],
            "api": {
                "type": "openapi",
                "url": f"{function_app_url}/api/openapi/{self._to_snake_case(agent_name)}"
            },
            "auth": {
                "type": "none"
            },
            "capabilities": {
                "conversation_starters": True
            }
        }
    
    def _build_agent_openapi(self, agent_def: Dict, function_app_url: str) -> str:
        """Build OpenAPI spec for a single agent."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        snake_name = self._to_snake_case(agent_name)
        
        actions = agent_def.get("actions", [])
        metadata = agent_def.get("metadata", {})
        
        paths = {}
        
        # Main agent endpoint
        paths[f"/api/{snake_name}"] = {
            "post": {
                "operationId": f"{snake_name}_invoke",
                "summary": f"Invoke {agent_name}",
                "description": agent_info.get("description", ""),
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "action": {
                                        "type": "string",
                                        "description": "The action to perform",
                                        "enum": [a.get("name") for a in actions] if actions else ["default"]
                                    },
                                    "parameters": {
                                        "type": "object",
                                        "description": "Action-specific parameters"
                                    }
                                },
                                "required": ["action"]
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object"
                                }
                            }
                        }
                    }
                }
            }
        }
        
        spec = {
            "openapi": "3.0.3",
            "info": {
                "title": f"{agent_name} API",
                "description": agent_info.get("description", ""),
                "version": agent_info.get("version", "1.0.0")
            },
            "servers": [
                {"url": function_app_url}
            ],
            "paths": paths
        }
        
        # Return as YAML-like string (simplified)
        return json.dumps(spec, indent=2)
    
    def _build_openapi_spec(self, agents: List[Dict], function_app_url: str) -> Dict:
        """Build complete OpenAPI spec for all agents."""
        paths = {}
        
        for agent_def in agents:
            agent_info = agent_def.get("agent", agent_def)
            agent_name = agent_info.get("name", agent_info.get("agent_name", "Agent"))
            snake_name = self._to_snake_case(agent_name)
            
            paths[f"/api/{snake_name}"] = {
                "post": {
                    "operationId": f"{snake_name}_invoke",
                    "summary": f"Invoke {agent_name}",
                    "description": agent_info.get("description", ""),
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "action": {"type": "string"},
                                        "parameters": {"type": "object"}
                                    }
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Success",
                            "content": {
                                "application/json": {"schema": {"type": "object"}}
                            }
                        }
                    }
                }
            }
        
        return {
            "openapi": "3.0.3",
            "info": {
                "title": "RAPP Agent API",
                "description": "Multi-agent platform API",
                "version": "1.0.0"
            },
            "servers": [{"url": function_app_url}],
            "paths": paths
        }
    
    def _build_power_automate_flow(self, agent_def: Dict, function_app_url: str) -> Dict:
        """Build Power Automate flow template for Copilot Studio."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        
        return {
            "name": f"RAPP-{agent_name}-Flow",
            "description": f"Power Automate flow for {agent_name}",
            "trigger": {
                "type": "Request",
                "kind": "Http",
                "inputs": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "action": {"type": "string"},
                            "parameters": {"type": "object"}
                        }
                    }
                }
            },
            "actions": {
                "Call_RAPP_Function": {
                    "type": "Http",
                    "inputs": {
                        "method": "POST",
                        "uri": f"{function_app_url}/api/{self._to_snake_case(agent_name)}",
                        "headers": {
                            "Content-Type": "application/json"
                        },
                        "body": "@triggerBody()"
                    }
                },
                "Response": {
                    "type": "Response",
                    "inputs": {
                        "statusCode": 200,
                        "body": "@body('Call_RAPP_Function')"
                    },
                    "runAfter": {"Call_RAPP_Function": ["Succeeded"]}
                }
            }
        }
    
    def _generate_foundry_tools(self, agent_def: Dict) -> str:
        """Generate tools.py for Azure AI Foundry."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        snake_name = self._to_snake_case(agent_name)
        actions = agent_def.get("actions", [])
        
        tools_code = f'''"""
Tools for {agent_name} Azure AI Foundry Agent
Auto-generated from RAPP agent definition
"""

import json
import requests
from typing import Dict, Any, List
from azure.ai.projects.models import FunctionTool

# PUBLISHER PREFIX. Kody, 2026-08-27: "make it aibast for now."
#
# Env-overridable rather than hardcoded, because this repo is public: a bare "aibast"
# default would stamp every stranger's generated solution with a publisher that is not
# theirs, and a solution carrying the wrong publisher is a real problem for them to unpick
# in a tenant. Setting RAPP_PUBLISHER_PREFIX overrides it; unset, it is aibast.
_DEFAULT_PUBLISHER_PREFIX = os.getenv("RAPP_PUBLISHER_PREFIX", "aibast")


RAPP_FUNCTION_APP_URL = "https://your-function-app.azurewebsites.net"


def get_tools() -> List[FunctionTool]:
    """Get all tools for this agent."""
    tools = []
    
'''
        
        # Add tool definitions for each action
        for action in actions:
            action_name = action.get("name", "unknown")
            description = action.get("description", f"Execute {action_name}")
            params = action.get("parameters", [])
            
            # Build parameters schema
            param_props = {}
            for p in params:
                if isinstance(p, str):
                    param_props[p] = {"type": "string", "description": f"The {p} parameter"}
                elif isinstance(p, dict):
                    param_props[p.get("name", "param")] = {
                        "type": p.get("type", "string"),
                        "description": p.get("description", "")
                    }
            
            tools_code += f'''    tools.append(FunctionTool(
        name="{action_name}",
        description="{description}",
        parameters={{
            "type": "object",
            "properties": {json.dumps(param_props, indent=12)},
            "required": []
        }}
    ))
    
'''
        
        tools_code += '''    return tools


def execute_tool(tool_name: str, arguments: str) -> str:
    """Execute a tool by calling the RAPP Function App."""
    try:
        args = json.loads(arguments) if arguments else {}
        
        response = requests.post(
            f"{RAPP_FUNCTION_APP_URL}/api/''' + snake_name + '''",
            json={
                "action": tool_name,
                **args
            },
            timeout=60
        )
        
        if response.status_code == 200:
            return json.dumps(response.json())
        else:
            return json.dumps({"error": f"API returned {response.status_code}"})
            
    except Exception as e:
        return json.dumps({"error": str(e)})
'''
        
        return tools_code
    
    def _save_transpiled_files(self, agent_name: str, results: Dict) -> Dict:
        """Save transpiled files to disk."""
        saved = {}
        base_output = os.path.join(self.output_path, self._to_snake_case(agent_name))
        
        for platform, files in results.items():
            platform_path = os.path.join(base_output, platform)
            os.makedirs(platform_path, exist_ok=True)
            saved[platform] = []
            
            for filename, content in files.items():
                filepath = os.path.join(platform_path, filename)
                
                # Create subdirectories if needed
                os.makedirs(os.path.dirname(filepath), exist_ok=True) if os.path.dirname(filepath) != platform_path else None
                
                with open(filepath, 'w') as f:
                    if isinstance(content, (dict, list)):
                        json.dump(content, f, indent=2)
                    else:
                        f.write(str(content))
                
                saved[platform].append(filepath)
        
        return saved
    
    # String utilities
    def _to_snake_case(self, name: str) -> str:
        """Convert to snake_case."""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower().replace(' ', '_').replace('-', '_')
    
    def _to_pascal_case(self, name: str) -> str:
        """Convert to PascalCase."""
        return ''.join(word.capitalize() for word in re.split(r'[_\s-]', name))
    
    def _to_title_case(self, name: str) -> str:
        """Convert to Title Case."""
        return ' '.join(word.capitalize() for word in re.split(r'[_\s-]', name))

# ============================================================================
# Unified dispatcher
# ============================================================================
class CopilotStudioForgeAgent(BasicAgent):
    """One authoring surface for RAPP -> Copilot Studio / M365 / Foundry.

    engine=
      "forge"    -> swarm singleton .py  -> native multi-agent CS YAML bundle (+zip)
                    (actions: list, refresh, forge, inspect, validate)
      "topics"   -> brainstem agents/*.py -> Copilot Studio topic .mcs.yml
                    (actions: wizard, generate, scan)
      "solution" -> a single agent        -> full native CS solution w/ flows+connectors
                    (actions: transpile, analyze, preview, validate, batch)
      "export"   -> a single agent        -> M365 declarative agent OR Azure AI Foundry tools
                    (platform: m365 | foundry ; actions: transpile, analyze, preview)
    All other kwargs pass through to the selected engine unchanged.
    """

    def __init__(self):
        self.name = "CopilotStudioForge"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "engine": {"type": "string", "enum": ["forge", "topics", "solution", "export", "help"],
                                "description": "Which authoring engine: forge (swarm->CS bundle), topics (agents->topic yaml), solution (agent->full CS solution), export (agent->m365/foundry)."},
                    "action": {"type": "string", "description": "Engine-specific verb (e.g. forge/list/refresh/inspect/validate, wizard/generate/scan, transpile/analyze/preview)."},
                    "swarm_name": {"type": "string", "description": "forge engine: swarm singleton name."},
                    "agent_name": {"type": "string", "description": "solution/export engine: agent to convert."},
                    "agent_filename": {"type": "string", "description": "forge engine: specific agent file."},
                    "agents_dir": {"type": "string", "description": "topics engine: directory of agents/*.py to author topics from."},
                    "platform": {"type": "string", "enum": ["m365", "copilot_studio", "foundry"], "description": "export engine target platform."},
                    "output_dir": {"type": "string", "description": "Where to write generated artifacts."},
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)
        self._e_forge = None
        self._e_topics = None
        self._e_solution = None
        self._e_export = None

    @property
    def forge(self):
        if self._e_forge is None:
            self._e_forge = _ForgeEngine()
        return self._e_forge

    @property
    def topics(self):
        if self._e_topics is None:
            self._e_topics = _TopicEngine()
        return self._e_topics

    @property
    def solution(self):
        if self._e_solution is None:
            self._e_solution = _SolutionEngine()
        return self._e_solution

    @property
    def export(self):
        if self._e_export is None:
            self._e_export = _ExportEngine()
        return self._e_export

    def _help(self, note=""):
        head = (note + "\n\n") if note else ""
        return (head +
                "CopilotStudioForge — one authoring surface (assimilates forge + topic_wizard + "
                "copilot_studio_transpiler + agent_transpiler).\n"
                "  engine=forge     action=list|refresh|forge|inspect|validate  swarm_name=...\n"
                "  engine=topics    action=wizard|generate|scan                 agents_dir=...\n"
                "  engine=solution  action=transpile|analyze|preview|validate   agent_name=...\n"
                "  engine=export    platform=m365|foundry  action=transpile     agent_name=...\n"
                "All extra kwargs pass straight through to the chosen engine.")

    def perform(self, engine="help", **kwargs):
        e = str(engine or "help").strip().lower()
        try:
            if e in ("help", "", "usage"):
                return self._help()
            if e in ("forge", "swarm", "bundle"):
                if e in ("swarm", "bundle"):
                    kwargs.setdefault("action", "forge")
                return self.forge.run(**kwargs)
            if e in ("topics", "topic", "wizard"):
                if e == "wizard":
                    kwargs.setdefault("action", "wizard")
                return self.topics.run(**kwargs)
            if e in ("solution", "transpile", "single"):
                return self.solution.run(**kwargs)
            if e in ("export", "platform", "m365", "foundry"):
                if e in ("m365", "foundry"):
                    kwargs.setdefault("platform", e)
                    kwargs.setdefault("action", "transpile")
                return self.export.run(**kwargs)
            return self._help("Unknown engine '%s'." % engine)
        except Exception as ex:  # noqa: BLE001
            return "CopilotStudioForge[%s] error: %s" % (engine, ex)

if __name__ == "__main__":
    import sys as _sys
    a = CopilotStudioForgeAgent()
    print(a.perform(_sys.argv[1] if len(_sys.argv) > 1 else "help"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
