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
        "Bundle a teammate's single-file agent (and optional service) into "
        "a publish-ready rapplication directory with manifest.json and a "
        "catalog index entry."
    ),
    "author": "RAPP",
    "version": "1.0.0",
    "tags": ["meta", "build", "rapplication", "bundler", "publish"],
    "category": "core",
    "quality_tier": "community",
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
