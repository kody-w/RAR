---
name: "rar-rapp-rapplication"
description: "Bundle, inspect, or validate a single-file agent against the RAPP rapplication contract. Use this when a teammate has a working *_agent.py and wants to publish it.\n\nActions:\n \u2022 'bundle'   \u2014 Produce a publish-ready directory with the agent file, optional service file, manifest.json, an index.json catalog snippet, and a README.\n \u2022 'inspect'  \u2014 Read the agent source and report what would be bundled. No files written.\n \u2022 'validate' \u2014 Check contract conformance only (errors + warnings). No files written.\n\nPaths can be absolute, relative to the cwd, or relative to the brainstem root (so 'agents/kanban_agent.py' works)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapplication_agent", "rar_sha256": "c7bbf9955cd91626d099d580ab612f4081b0b81bd0b3b35033445872461de01c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.2", "author": "RAPP", "tags": ["meta", "build", "rapplication", "bundler", "publish"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/rapplication_agent`. The original RAPP
agent is preserved byte-for-byte in `rapplication_agent.py` and in the RCI capsule.

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

rapplication_agent.py — Bundle an existing single-file agent (and optional
service) into a publish-ready rapplication directory.

Drop this file in agents/ and ask the brainstem things like:

  "Bundle my kanban_agent.py as a rapplication"
  "Inspect agents/kanban_agent.py — what would the manifest look like?"
  "Validate agents/kanban_agent.py against the rapplication contract"
  "Bundle agents/kanban_agent.py with services/kanban_service.py"

Output lands in .brainstem_data/rapplications/<id>/ :

    <id>_agent.py        ← copied verbatim
    <id>_service.py      ← copied verbatim (if a service was provided)
    manifest.json        ← rapp-application/1.0 store metadata
    index_entry.json     ← catalog snippet — paste into your rapp_store/index.json
    README.md            ← one-page summary teammates can read

Then `cd` into that directory and `git init` / push it wherever your team
publishes rapplications. The brainstem itself isn't involved in publishing —
this agent just produces the right shape.

Reference: pages/docs/rapplication-sdk.md (the agent-first contract).

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "What to do with the source file.",
      "enum": [
        "bundle",
        "inspect",
        "validate"
      ],
      "type": "string"
    },
    "agent_path": {
      "description": "Path to the *_agent.py source file. Required for all actions.",
      "type": "string"
    },
    "publisher": {
      "description": "Publisher handle for the manifest (e.g. 'acme-team'). Defaults to 'team'.",
      "type": "string"
    },
    "rapp_id": {
      "description": "Override the rapplication id (defaults to the agent filename minus '_agent.py').",
      "type": "string"
    },
    "raw_url_base": {
      "description": "Optional. Base raw-URL for the catalog index entry, e.g. 'https://raw.githubusercontent.com/acme/rapp_store/main'. The bundler appends '/<id>/<file>' to build singleton_url and service_url.",
      "type": "string"
    },
    "service_path": {
      "description": "Optional path to a paired *_service.py. Bundled alongside the agent.",
      "type": "string"
    }
  },
  "required": [
    "action",
    "agent_path"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapplication_agent.py` and embedded as the fenced Python below (sha256 c7bbf9955cd91626…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapplication_agent.py` first:

```bash
python3 rapplication_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapplication_agent.py   # or on stdin
python3 rapplication_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/rapplication_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rapplication_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/rapplication_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
rapplication_agent.py — Bundle an existing single-file agent (and optional
service) into a publish-ready rapplication directory.

Drop this file in agents/ and ask the brainstem things like:

  "Bundle my kanban_agent.py as a rapplication"
  "Inspect agents/kanban_agent.py — what would the manifest look like?"
  "Validate agents/kanban_agent.py against the rapplication contract"
  "Bundle agents/kanban_agent.py with services/kanban_service.py"

Output lands in .brainstem_data/rapplications/<id>/ :

    <id>_agent.py        ← copied verbatim
    <id>_service.py      ← copied verbatim (if a service was provided)
    manifest.json        ← rapp-application/1.0 store metadata
    index_entry.json     ← catalog snippet — paste into your rapp_store/index.json
    README.md            ← one-page summary teammates can read

Then `cd` into that directory and `git init` / push it wherever your team
publishes rapplications. The brainstem itself isn't involved in publishing —
this agent just produces the right shape.

Reference: pages/docs/rapplication-sdk.md (the agent-first contract).
"""

from agents.basic_agent import BasicAgent
import ast
import json
import os
import re
import shutil
from datetime import datetime, timezone


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/rapplication_agent",
    "display_name": "Rapplication",
    "description": (
        "Bundles a single-file agent (and optional service) into a publish-ready rapplication directory with manifest.json and a catalog index entry."
    ),
    "author": "RAPP",
    "version": "1.0.2",
    "tags": ["meta", "build", "rapplication", "bundler", "publish"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {"args": {"action": "bundle", "agent_path": "agents/kanban_agent.py"}},
}


# ─── Helpers ────────────────────────────────────────────────────────────────

def _brainstem_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _resolve(path):
    """Accept absolute, relative-to-cwd, or relative-to-brainstem-root paths."""
    if not path:
        return ""
    if os.path.isabs(path):
        return path
    cwd_try = os.path.abspath(path)
    if os.path.exists(cwd_try):
        return cwd_try
    return os.path.join(_brainstem_root(), path)


def _output_dir(rapp_id):
    return os.path.join(_brainstem_root(), ".brainstem_data", "rapplications", rapp_id)


def _slugify(s):
    s = re.sub(r"[^\w\s-]", "", s or "").strip().lower()
    s = re.sub(r"[\s_-]+", "_", s)
    return s.strip("_") or "rapp"


def _id_from_filename(path):
    base = os.path.basename(path)
    if base.endswith("_agent.py"):
        return base[:-len("_agent.py")]
    if base.endswith("_service.py"):
        return base[:-len("_service.py")]
    if base.endswith(".py"):
        return base[:-3]
    return base


# ─── AST extraction ─────────────────────────────────────────────────────────

def _literal_or_none(node):
    """ast.literal_eval but tolerant — returns None if the node is dynamic."""
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


def _extract_module_manifest(tree):
    """Find a top-level `__manifest__ = {...}` literal."""
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id == "__manifest__":
                    val = _literal_or_none(node.value)
                    if isinstance(val, dict):
                        return val
    return None


def _extract_module_string(tree, name):
    """Find a top-level `name = "..."` string assignment."""
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id == name:
                    val = _literal_or_none(node.value)
                    if isinstance(val, str):
                        return val
    return None


def _extract_basic_agent_class(tree):
    """Return the first class that subclasses BasicAgent (by attribute or name)."""
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        for base in node.bases:
            base_name = ""
            if isinstance(base, ast.Name):
                base_name = base.id
            elif isinstance(base, ast.Attribute):
                base_name = base.attr
            if base_name == "BasicAgent":
                return node
    return None


def _extract_class_metadata(class_node):
    """Pull self.metadata = {...} out of __init__, if it's a literal dict."""
    for node in ast.walk(class_node):
        if isinstance(node, ast.FunctionDef) and node.name == "__init__":
            for stmt in ast.walk(node):
                if not isinstance(stmt, ast.Assign):
                    continue
                for tgt in stmt.targets:
                    if (isinstance(tgt, ast.Attribute)
                            and isinstance(tgt.value, ast.Name)
                            and tgt.value.id == "self"
                            and tgt.attr == "metadata"):
                        val = _literal_or_none(stmt.value)
                        if isinstance(val, dict):
                            return val
    return None


def _has_method(class_node, name):
    return any(isinstance(n, ast.FunctionDef) and n.name == name
               for n in class_node.body)


def _inspect_agent_source(source):
    """Extract everything we need to build a manifest from agent source code."""
    out = {
        "syntax_ok": False,
        "imports_basic_agent": False,
        "manifest": None,
        "class_name": None,
        "agent_name": None,
        "class_metadata": None,
        "has_perform": False,
        "has_system_context": False,
        "errors": [],
        "warnings": [],
    }
    try:
        tree = ast.parse(source)
        out["syntax_ok"] = True
    except SyntaxError as e:
        out["errors"].append(f"syntax error: {e.msg} (line {e.lineno})")
        return out

    out["imports_basic_agent"] = bool(
        re.search(r"from\s+agents\.basic_agent\s+import\s+BasicAgent", source)
    )
    if not out["imports_basic_agent"]:
        out["warnings"].append(
            "agent does not import BasicAgent from agents.basic_agent — "
            "the brainstem may not auto-discover it"
        )

    out["manifest"] = _extract_module_manifest(tree)

    class_node = _extract_basic_agent_class(tree)
    if class_node is None:
        out["errors"].append("no class extending BasicAgent found")
        return out

    out["class_name"] = class_node.name
    out["has_perform"] = _has_method(class_node, "perform")
    out["has_system_context"] = _has_method(class_node, "system_context")
    if not out["has_perform"]:
        out["errors"].append(f"class {class_node.name} has no perform() method")

    meta = _extract_class_metadata(class_node)
    if meta:
        out["class_metadata"] = meta
        out["agent_name"] = meta.get("name")

    return out


def _inspect_service_source(source):
    """Validate a service file against the contract: name + handle()."""
    out = {
        "syntax_ok": False,
        "name": None,
        "has_handle": False,
        "errors": [],
    }
    try:
        tree = ast.parse(source)
        out["syntax_ok"] = True
    except SyntaxError as e:
        out["errors"].append(f"syntax error: {e.msg} (line {e.lineno})")
        return out

    out["name"] = _extract_module_string(tree, "name")
    if not out["name"]:
        out["errors"].append("service is missing a top-level `name = \"...\"` string")

    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "handle":
            out["has_handle"] = True
            break
    if not out["has_handle"]:
        out["errors"].append("service is missing a `handle(method, path, body)` function")

    return out


# ─── Build the rapp-application/1.0 manifest ────────────────────────────────

def _derive_manifest(rapp_id, agent_info, agent_filename, service_filename, publisher):
    """Merge __manifest__, class metadata, and overrides into one canonical manifest."""
    src = agent_info.get("manifest") or {}
    cls = agent_info.get("class_metadata") or {}

    # Display name: prefer __manifest__.display_name, else the class agent name, else id.
    display_name = src.get("display_name") or agent_info.get("agent_name") or rapp_id
    summary = src.get("description") or cls.get("description") or ""
    summary = summary.strip().split("\n")[0][:240]
    version = src.get("version") or "1.0.0"
    tags = list(src.get("tags") or []) or ["rapplication"]
    category = src.get("category") or "general"

    manifest_name = src.get("name") or f"@{(publisher or 'team').lstrip('@')}/{rapp_id}"

    manifest = {
        "schema": "rapp-application/1.0",
        "id": rapp_id,
        "name": display_name,
        "version": version,
        "publisher": "@" + (publisher or "team").lstrip("@"),
        "manifest_name": manifest_name,
        "summary": summary,
        "category": category,
        "tags": tags,
        "agent": agent_filename,
        "license": src.get("license") or "BSD-style",
        "produced_by": {
            "method": "agent-first",
            "source_files_collapsed": 2 if service_filename else 1,
            "bundled_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "bundler": "rapplication_agent/1.0",
        },
    }
    if service_filename:
        manifest["service"] = service_filename
    if src.get("requires_env"):
        manifest["requires_env"] = src["requires_env"]
    if src.get("quality_tier"):
        manifest["quality_tier"] = src["quality_tier"]
    return manifest


def _index_entry(manifest, raw_url_base):
    """Build the snippet that goes inside rapp_store/index.json → rapplications[]."""
    rapp_id = manifest["id"]
    base = (raw_url_base or "").rstrip("/")
    entry = {
        "id": rapp_id,
        "name": manifest["name"],
        "version": manifest["version"],
        "summary": manifest.get("summary", ""),
        "category": manifest.get("category", "general"),
        "tags": manifest.get("tags", []),
        "manifest_name": manifest.get("manifest_name", ""),
        "singleton_filename": manifest["agent"],
        "produced_by": manifest["produced_by"],
    }
    if base:
        entry["singleton_url"] = f"{base}/{rapp_id}/{manifest['agent']}"
        if manifest.get("service"):
            entry["service_url"] = f"{base}/{rapp_id}/{manifest['service']}"
    if manifest.get("service"):
        entry["service_filename"] = manifest["service"]
    return entry


# ─── README rendered for teammates ──────────────────────────────────────────

def _render_readme(manifest, agent_info, service_info):
    lines = [
        f"# {manifest['name']}",
        "",
        f"> {manifest.get('summary', '_(no summary)_')}",
        "",
        f"- **id**: `{manifest['id']}`",
        f"- **version**: `{manifest['version']}`",
        f"- **publisher**: `{manifest['publisher']}`",
        f"- **manifest_name**: `{manifest['manifest_name']}`",
        f"- **category**: `{manifest['category']}`",
        f"- **tags**: {', '.join('`' + t + '`' for t in manifest.get('tags', [])) or '_(none)_'}",
        "",
        "## Files",
        "",
        f"- `{manifest['agent']}` — agent (required)",
    ]
    if manifest.get("service"):
        lines.append(f"- `{manifest['service']}` — service (optional)")
    lines += [
        "- `manifest.json` — rapp-application/1.0 metadata",
        "- `index_entry.json` — paste this into your store catalog's `rapplications[]`",
        "",
        "## Install (drop-in)",
        "",
        "```",
        f"cp {manifest['agent']} ~/.brainstem/src/rapp_brainstem/agents/",
    ]
    if manifest.get("service"):
        lines.append(f"cp {manifest['service']} ~/.brainstem/src/rapp_brainstem/services/")
    lines += [
        "```",
        "",
        "Next `/chat` request discovers the agent. No restart, no registration.",
        "",
        "## Contract checks",
        "",
        f"- BasicAgent import: {'✅' if agent_info.get('imports_basic_agent') else '⚠️ missing'}",
        f"- `perform()` method: {'✅' if agent_info.get('has_perform') else '❌ missing'}",
        f"- `__manifest__` dict: {'✅' if agent_info.get('manifest') else '⚠️ not provided'}",
    ]
    if service_info:
        lines += [
            f"- service `name = ...`: {'✅' if service_info.get('name') else '❌ missing'}",
            f"- service `handle()`: {'✅' if service_info.get('has_handle') else '❌ missing'}",
        ]
    lines += [
        "",
        "_Generated by `rapplication_agent.py` — see `pages/docs/rapplication-sdk.md`._",
        "",
    ]
    return "\n".join(lines)


# ─── Agent class ────────────────────────────────────────────────────────────

class RapplicationAgent(BasicAgent):
    def __init__(self):
        self.name = "Rapplication"
        self.metadata = {
            "name": self.name,
            "description": (
                "Bundle, inspect, or validate a single-file agent against the "
                "RAPP rapplication contract. Use this when a teammate has a "
                "working *_agent.py and wants to publish it.\n\n"
                "Actions:\n"
                " • 'bundle'   — Produce a publish-ready directory with the "
                "agent file, optional service file, manifest.json, an "
                "index.json catalog snippet, and a README.\n"
                " • 'inspect'  — Read the agent source and report what would "
                "be bundled. No files written.\n"
                " • 'validate' — Check contract conformance only (errors + "
                "warnings). No files written.\n\n"
                "Paths can be absolute, relative to the cwd, or relative to "
                "the brainstem root (so 'agents/kanban_agent.py' works)."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["bundle", "inspect", "validate"],
                        "description": "What to do with the source file.",
                    },
                    "agent_path": {
                        "type": "string",
                        "description": "Path to the *_agent.py source file. Required for all actions.",
                    },
                    "service_path": {
                        "type": "string",
                        "description": "Optional path to a paired *_service.py. Bundled alongside the agent.",
                    },
                    "rapp_id": {
                        "type": "string",
                        "description": "Override the rapplication id (defaults to the agent filename minus '_agent.py').",
                    },
                    "publisher": {
                        "type": "string",
                        "description": "Publisher handle for the manifest (e.g. 'acme-team'). Defaults to 'team'.",
                    },
                    "raw_url_base": {
                        "type": "string",
                        "description": "Optional. Base raw-URL for the catalog index entry, e.g. 'https://raw.githubusercontent.com/acme/rapp_store/main'. The bundler appends '/<id>/<file>' to build singleton_url and service_url.",
                    },
                },
                "required": ["action", "agent_path"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── Action: inspect ─────────────────────────────────────────────────
    def _do_inspect(self, agent_path, service_path):
        agent_abs = _resolve(agent_path)
        if not os.path.exists(agent_abs):
            return {"status": "error", "summary": f"agent file not found: {agent_path}"}
        with open(agent_abs) as f:
            agent_src = f.read()
        agent_info = _inspect_agent_source(agent_src)

        service_info = None
        if service_path:
            service_abs = _resolve(service_path)
            if not os.path.exists(service_abs):
                return {"status": "error",
                        "summary": f"service file not found: {service_path}"}
            with open(service_abs) as f:
                service_info = _inspect_service_source(f.read())

        return {
            "status": "ok",
            "action": "inspect",
            "agent_path": agent_abs,
            "agent": agent_info,
            "service_path": _resolve(service_path) if service_path else None,
            "service": service_info,
            "summary": (
                f"Inspected {os.path.basename(agent_abs)}: "
                f"class={agent_info.get('class_name')}, "
                f"perform={'yes' if agent_info.get('has_perform') else 'no'}, "
                f"manifest={'yes' if agent_info.get('manifest') else 'no'}, "
                f"errors={len(agent_info.get('errors', []))}"
            ),
        }

    # ── Action: validate ────────────────────────────────────────────────
    def _do_validate(self, agent_path, service_path):
        result = self._do_inspect(agent_path, service_path)
        if result.get("status") != "ok":
            return result
        agent_info = result["agent"]
        service_info = result.get("service")
        errors = list(agent_info.get("errors", []))
        warnings = list(agent_info.get("warnings", []))
        if service_info:
            errors += service_info.get("errors", [])
        passed = not errors
        return {
            "status": "ok" if passed else "error",
            "action": "validate",
            "passed": passed,
            "errors": errors,
            "warnings": warnings,
            "summary": (
                f"Contract: {'PASS' if passed else 'FAIL'} "
                f"({len(errors)} error(s), {len(warnings)} warning(s))"
            ),
        }

    # ── Action: bundle ──────────────────────────────────────────────────
    def _do_bundle(self, agent_path, service_path, rapp_id, publisher, raw_url_base):
        inspected = self._do_inspect(agent_path, service_path)
        if inspected.get("status") != "ok":
            return inspected
        agent_info = inspected["agent"]
        service_info = inspected.get("service")

        if agent_info.get("errors"):
            return {
                "status": "error",
                "action": "bundle",
                "summary": "agent failed contract checks; refusing to bundle",
                "errors": agent_info["errors"],
                "warnings": agent_info.get("warnings", []),
            }

        agent_abs = inspected["agent_path"]
        service_abs = inspected.get("service_path")

        # Resolve final id: explicit override → __manifest__ id-ish → filename.
        if not rapp_id:
            mf = agent_info.get("manifest") or {}
            mf_name = mf.get("name") or ""
            after_slash = mf_name.split("/", 1)[-1] if "/" in mf_name else ""
            rapp_id = _slugify(after_slash) or _id_from_filename(agent_abs)
        rapp_id = _slugify(rapp_id)

        # Standardize bundled filenames so install instructions are predictable.
        agent_filename = f"{rapp_id}_agent.py"
        service_filename = f"{rapp_id}_service.py" if service_abs else None

        out_dir = _output_dir(rapp_id)
        os.makedirs(out_dir, exist_ok=True)

        shutil.copyfile(agent_abs, os.path.join(out_dir, agent_filename))
        if service_abs:
            shutil.copyfile(service_abs, os.path.join(out_dir, service_filename))

        manifest = _derive_manifest(
            rapp_id=rapp_id,
            agent_info=agent_info,
            agent_filename=agent_filename,
            service_filename=service_filename,
            publisher=publisher,
        )
        with open(os.path.join(out_dir, "manifest.json"), "w") as f:
            json.dump(manifest, f, indent=2)

        entry = _index_entry(manifest, raw_url_base)
        with open(os.path.join(out_dir, "index_entry.json"), "w") as f:
            json.dump(entry, f, indent=2)

        with open(os.path.join(out_dir, "README.md"), "w") as f:
            f.write(_render_readme(manifest, agent_info, service_info))

        files = [agent_filename, "manifest.json", "index_entry.json", "README.md"]
        if service_filename:
            files.insert(1, service_filename)

        return {
            "status": "ok",
            "action": "bundle",
            "id": rapp_id,
            "directory": out_dir,
            "files": files,
            "manifest": manifest,
            "index_entry": entry,
            "warnings": agent_info.get("warnings", []),
            "summary": (
                f"Bundled '{manifest['name']}' (id={rapp_id}, v{manifest['version']}) "
                f"→ {out_dir} [{len(files)} files]. "
                f"Push the directory to your store repo and paste index_entry.json "
                f"into the catalog's `rapplications[]`."
            ),
        }

    # ── Dispatch ────────────────────────────────────────────────────────
    def perform(self, **kwargs):
        action = (kwargs.get("action") or "").strip().lower()
        agent_path = kwargs.get("agent_path") or ""
        service_path = kwargs.get("service_path") or ""
        rapp_id = kwargs.get("rapp_id") or ""
        publisher = kwargs.get("publisher") or ""
        raw_url_base = kwargs.get("raw_url_base") or ""

        if not action:
            return json.dumps({"status": "error",
                               "summary": "action is required: bundle | inspect | validate"})
        if not agent_path:
            return json.dumps({"status": "error",
                               "summary": "agent_path is required (path to a *_agent.py file)"})

        try:
            if action == "inspect":
                result = self._do_inspect(agent_path, service_path)
            elif action == "validate":
                result = self._do_validate(agent_path, service_path)
            elif action == "bundle":
                result = self._do_bundle(agent_path, service_path, rapp_id,
                                         publisher, raw_url_base)
            else:
                result = {"status": "error",
                          "summary": f"unknown action: {action}"}
        except Exception as e:
            result = {"status": "error",
                      "summary": f"{type(e).__name__}: {e}"}
        return json.dumps(result)
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
