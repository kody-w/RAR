---
name: "rar-kody-w-copilot-studio-forge"
description: "Authors Copilot Studio, M365, and Foundry artifacts from RAPP agents through four embedded engines \u2014 bundles, topics, solutions, and exports."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_forge_agent", "rar_sha256": "80f80484f489a3023354e4528bc52657032f686db909fe3ffdcf99d7ae454abe", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["copilot-studio", "forge", "transpiler", "mcs", "m365", "foundry", "authoring", "assimilated"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_forge_agent.py` and embedded as the fenced Python below (sha256 80f80484f489a302…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_forge_agent.py` first:

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
    "version": "1.0.1",
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
        prefix = schema_prefix or "rapp"
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
