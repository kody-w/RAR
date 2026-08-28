---
name: "rar-rapp-rapplication"
description: "Bundle, inspect, or validate a single-file agent against the RAPP rapplication contract. Use this when a teammate has a working *_agent.py and wants to publish it.\n\nActions:\n \u2022 'bundle'   \u2014 Produce a publish-ready directory with the agent file, optional service file, manifest.json, an index.json catalog snippet, and a README.\n \u2022 'inspect'  \u2014 Read the agent source and report what would be bundled. No files written.\n \u2022 'validate' \u2014 Check contract conformance only (errors + warnings). No files written.\n\nPaths can be absolute, relative to the cwd, or relative to the brainstem root (so 'agents/kanban_agent.py' works)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapplication_agent", "rar_sha256": "a40d2ce08abde9774ebb4d34f02577a31e15a2ef66d2064953ab08a3f39baa0b", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "RAPP", "tags": ["meta", "build", "rapplication", "bundler", "publish"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapplication_agent.py` and embedded as the fenced Python below (sha256 a40d2ce08abde977…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapplication_agent.py` first:

```bash
python3 rapplication_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapplication_agent.py   # or on stdin
python3 rapplication_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
