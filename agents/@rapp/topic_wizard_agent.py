"""
topic_wizard_agent.py — Step-by-step UI + generator for converting a
rapp_brainstem agents/ directory into Microsoft Copilot Studio (MCS)
topic .mcs.yml files.

Scope is intentionally narrower than @rapp/rapp2mcs_factory: this agent
ONLY does the agents/*.py → topics/*.mcs.yml hop. No analyzer, no
normalizer, no solution.zip, no pac deploy. Just topic authoring —
either through a self-contained HTML wizard the human drives in a
browser, or through a deterministic `generate` action that takes a
config dict and writes the YAMLs straight to disk.

Why a separate agent: the factory is the autonomous one-button path. This
one is the inspectable, click-through path for when you want to see and
shape each topic before any solution.zip is built.

Actions:
  scan        — list agents in agents_dir + the auto-detected pattern
                for each (memory-save / memory-recall / web-browse /
                topic-only). Read-only, no LLM.
  wizard      — write a single self-contained HTML wizard to a file you
                open in a browser. Embeds the scan results so the page
                works offline (no CDN, no network). The page lets you
                edit display names, trigger queries, descriptions, and
                topic shape per agent, previews the .mcs.yml live, and
                downloads each topic file individually or the whole set
                as a JSON bundle.
  generate    — write the fully-built .mcs.yml files straight to disk
                from a config dict. Skips the UI entirely. Useful when
                you've already settled the config (e.g. by pasting the
                wizard's exported JSON back into chat).

Topic patterns the wizard knows how to build:
  • topic-only        — pure SendActivity + EndDialog, no connector
  • web-browse        — SearchAndSummarizeContent against the agent's
                        own webBrowsing capability (no Azure Function)
  • memory-save       — InvokeConnectorAction → AddRow on the OOTB
                        Dataverse `annotation` (Notes) table via
                        shared_commondataserviceforapps
  • memory-recall     — InvokeConnectorAction → ListRows on the same
                        OOTB `annotation` table, filtered to the
                        current user's RAPP-memory:* subjects

Public class: TopicWizardAgent
"""

try:
    from agents.basic_agent import BasicAgent  # RAPP brainstem layout
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent  # flat layout
    except ModuleNotFoundError:
        class BasicAgent:  # last-resort standalone
            def __init__(self, name, metadata):
                self.name, self.metadata = name, metadata

import ast
import json
import os
import re
import textwrap
from pathlib import Path


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/topic_wizard",
    "version": "0.1.0",
    "display_name": "Topic Wizard",
    "description": (
        "Step-by-step UI for converting rapp_brainstem/agents/*.py into "
        "Microsoft Copilot Studio topic .mcs.yml files. Writes a "
        "self-contained HTML wizard you drive in a browser, OR generates "
        "the YAMLs deterministically from a config dict. OOTB Dataverse "
        "only (annotation table), no Azure Functions."
    ),
    "author": "RAPP",
    "tags": ["mcs", "copilot-studio", "topic", "wizard", "ui", "singleton"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {"args": {"action": "wizard"}},
}


# ══════════════════════════════════════════════════════════════════════════
# Scan — discover agents/*.py and detect each one's intended topic shape.
# Pure AST. No LLM. No imports of the agent module itself.
# ══════════════════════════════════════════════════════════════════════════

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


# ══════════════════════════════════════════════════════════════════════════
# Topic YAML builders — one per pattern, all return ready-to-drop YAML
# (mcs.metadata header + kind: AdaptiveDialog + dialog).
# ══════════════════════════════════════════════════════════════════════════

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


# ══════════════════════════════════════════════════════════════════════════
# Wizard HTML — single self-contained page. The scan data is injected as a
# JSON blob, the page does the rest in-browser. No CDN, no network.
# ══════════════════════════════════════════════════════════════════════════

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


# ══════════════════════════════════════════════════════════════════════════
# PUBLIC ENTRYPOINT
# ══════════════════════════════════════════════════════════════════════════

class TopicWizardAgent(BasicAgent):
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

    def perform(self, action="wizard", **kwargs):
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


# Discovery alias — RAPP brainstem auto-loads classes whose names end in Agent.
class TopicWizard(TopicWizardAgent):
    pass
