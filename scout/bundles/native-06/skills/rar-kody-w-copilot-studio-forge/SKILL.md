---
name: "rar-kody-w-copilot-studio-forge"
description: "Authors Copilot Studio, M365, and Foundry artifacts from RAPP agents through four embedded engines \u2014 bundles, topics, solutions, and exports."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_forge_agent", "rar_sha256": "b74dc71864503e47340899674b0e8b9c17f4e8fc617298ed83e5f148bf87e709", "source_kind": "rar-agent", "source_commit": "b4ba983328bbb00340c62a83332318dc0ffc22aa", "version": "1.0.2", "author": "kody-w", "tags": ["copilot-studio", "forge", "transpiler", "mcs", "m365", "foundry", "authoring", "assimilated"]}
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
