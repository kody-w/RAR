---
name: "rar-kody-w-copilot-studio-forge"
description: "Authors Copilot Studio, M365, and Foundry artifacts from RAPP agents through four embedded engines \u2014 bundles, topics, solutions, and exports."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_forge_agent", "rar_sha256": "b74dc71864503e47340899674b0e8b9c17f4e8fc617298ed83e5f148bf87e709", "source_kind": "rar-agent", "source_commit": "b4ba983328bbb00340c62a83332318dc0ffc22aa", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "copilot_studio_forge_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/copilot-studio-forge:00560b4c895457249015dd85da12897e06bbfb608a01ddd09004af78c4635b88", "kind": "skill"}, "version": "1.0.2", "author": "kody-w", "tags": ["copilot-studio", "forge", "transpiler", "mcs", "m365", "foundry", "authoring", "assimilated"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/copilot_studio_forge_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `copilot_studio_forge_agent.py` is
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
