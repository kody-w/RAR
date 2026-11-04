---
name: "rar-kody-w-copilot-studio-forge"
description: "Authors Copilot Studio, M365, and Foundry artifacts from RAPP agents through four embedded engines \u2014 bundles, topics, solutions, and exports."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_forge_agent", "rar_sha256": "f30e91e542090161fd2b559f4565c5c63b0fd93cb51f9a208256eb6c2d689667", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.2", "author": "kody-w", "tags": ["copilot-studio", "forge", "transpiler", "mcs", "m365", "foundry", "authoring", "assimilated"]}
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
