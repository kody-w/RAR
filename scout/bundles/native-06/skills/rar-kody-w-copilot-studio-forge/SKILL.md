---
name: "rar-kody-w-copilot-studio-forge"
description: "Authors Copilot Studio, M365, and Foundry artifacts from RAPP agents through four embedded engines \u2014 bundles, topics, solutions, and exports."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_forge_agent", "rar_sha256": "f30e91e542090161fd2b559f4565c5c63b0fd93cb51f9a208256eb6c2d689667", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.2", "author": "kody-w", "tags": ["copilot-studio", "forge", "transpiler", "mcs", "m365", "foundry", "authoring", "assimilated"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_forge_agent.py` and embedded as the fenced Python below (sha256 f30e91e542090161…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_forge_agent.py` first:

```bash
python3 copilot_studio_forge_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_forge_agent.py   # or on stdin
python3 copilot_studio_forge_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/copilot_studio_forge_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_studio_forge_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/copilot_studio_forge_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
