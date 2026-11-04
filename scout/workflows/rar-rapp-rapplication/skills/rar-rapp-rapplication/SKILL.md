---
name: "rar-rapp-rapplication"
description: "Bundle, inspect, or validate a single-file agent against the RAPP rapplication contract. Use this when a teammate has a working *_agent.py and wants to publish it.\n\nActions:\n \u2022 'bundle'   \u2014 Produce a publish-ready directory with the agent file, optional service file, manifest.json, an index.json catalog snippet, and a README.\n \u2022 'inspect'  \u2014 Read the agent source and report what would be bundled. No files written.\n \u2022 'validate' \u2014 Check contract conformance only (errors + warnings). No files written.\n\nPaths can be absolute, relative to the cwd, or relative to the brainstem root (so 'agents/kanban_agent.py' works)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapplication_agent", "rar_sha256": "c7bbf9955cd91626d099d580ab612f4081b0b81bd0b3b35033445872461de01c", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.2", "author": "RAPP", "tags": ["meta", "build", "rapplication", "bundler", "publish"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/71757Lb1pbmq7BO/7B8KQuJSJ7ungEJgiCITAQCrS4bOQciEvTcd59NnnMUbN07XV1Tw1JRCHuvHL5Fbf3x4o1D2nQvv77ojKq+fHwJoz7osnbImho83I51WEYfV1ndt1EwfFw13Wryyiz0hmjlrfqsTsrolzgrwV0S1QP49sDaYTWk0epBcdV5bVtmgfcguAqaeui8YPi0MvsIrMn61ZxGNaA0RF5VPYimXg9u56YrAO3V3357kv3ULiuvDlezVw/9amhW7eiXWZ+usuHT5/pzzQQP8v2vn+vV5xGFUXT1k/+U/KfV6vkE2azUrgnH4CH12+ZfusgLl1WYdUCzpltWczakT8FfVXloBRR+msIrV33UTRnY//q48uosjvrhU9439UcgHDBRGN2etyugrVc2yaqvs7aNho9P2b2VvmdYaf/pGyHfzPrTFyF1INI3IvTN2D1EBtu7qG26AZjLA1/NWIYrP1q9Khl+WsnNUy5gzi4bhqj+lsm7v356Z7JLo6D44ovHRdx0QCHAqanLZfUh6rqm61drYO+uBm7of/4hh8+16g1pD9StH8J4ft+U4wCM00Ul8PcUPTz1UCaYw2fk/Pm53z2DJapWXdMMqw99s/rpqXgPFV7te/UX7//0jAggB4jQ6OZVLZDk5df/+M+PLxm4fvn1j5eg9Pr+EcbfxBvz2A12lF6dgFftAkK9Bvdt1D00Bo/CKF693X3oozL+uPrb3wqgNVD5EUxvH+8ZXqt/W314ffcpiYYPn19eH39++fmh2+cXcPGpH0DufPj5U9nMUffh529IPET5rQX2AmS+p/LlzTeUvm58C7sfbv323Q83P5Lvtyz88763xz/c8pYcUffnTV9e/ANO829jV/7meyCx/8Lu67vvNn/dnsWrGkTAq0W/sfyTdDSMXb16ZNancKza/sMfQPXBG8b+88uvgNQzXD+/fPx+2w8+YNsIqky3vO57cysoQl10HUEZCH99y6jV/36veODqPX8+v/z9579K/MV7/9+k/hpJ30i++vB8AhLL+7ZoPlL251fBv/IZuuVPwgJl3mP83wCLN90Bv78K10X9WA7AxY90+fRb2Pz2tvrDV8E+fhe1P39PJCr/xO2rff9L7N6X/7f5vbr4v8jtdfE/5PXxPcX+7278+vmSSR+/S5u/yN1H/0zE/0Y4fRdJ8eeXsS7qZq7f0271x+vF30HAfCUT3YKoHVb7518PI4IGHf0l2P97Qv1ZoD+GpY0+RD9/+u232qui3377OxAq+l6evybWK/efX/7+8RG5Qze+ogFQ3v/lX1ZSFnRN38TD6hw047DqxnrIquiRD8YDf4A/j1bURVPU9ZkPcv91Xds1efQaNU28+v1/PfwMfQtmXpPs908rA2xvuizJHijhgXk+16/dG5BugWwgXEB++ssAgFLT/fK4ANVl9ftfiYGM/f3Z7MHrJ4DaHUFzbYF20bPd2g+s9Creo+dGtygA/XZVNgHg/OzOj94LuvD0Bq76IivLbxDOE0iMjwL7uf79999B1KWf69e2iK1ecV8PgQVfC8gvvwAV4jJL0uFzHQUp6NB//P0nUBX/2a4n8Vd80L+bF0gonBV5BfrCWD1a/OrZ+gHceZj3j7+/GRKQqUHvAc7I4ix63VxmdRGF71Y988wvKE4AxAGsCSxZPXDRAysCLLg6xqsv8r5BpgecTBsAScOojQBGq4MFUPWAOl8s+SjkPfBDHy8fV+MTmUar37+gk98CsPz3lbRTQX1tykeRBWK+Ihuvbmrgw/KLz1+fAyLdT/1q+04C4KdHgK1aD3g97bw3HrH36hfQEd+3Pyt4Hc2f6weyiR6mekbIq3nAImCZ4M2lr8A7aEAK1WH/zvu5BhTIcGU0HmDefa77t0j2uocrggaIsqySEdRRAPr+x1tI9ekTVj7sByR9UHrzQvjmlWcM/jBq35Hl67iwesZm1j+98tcR4cMjCt9h9UO2Zzn9+V3379H5d+PDl0B+SsJ2Tfsa5k/iQPs37PgKt/viTxgTLAVQFkRTEf362g4/v803q2pZ/Qlwrp5jyLfcX9HO55fjGzD4MVB9t8Q3OP0hxfu4AHK1KZ4i/M93etaXcerHBL+dqH44TL0Tejf+j8k8h5s3W395+3b/SNknHFPGoQWRUL6H06evOQBE9L6rfz30r1n479Dq13do8bj9yu+9wo8oQsNA1vYRRyCgfLC5+mbDVxH+2YbVh0cT/zKDzd6jtDZTFkbhW9v8biD7E/eH2L98IzqEfIJX/fAoH1U0eA/VXok8Z7jfgAYgxL7QeZfo+6Hu3dHtI8VeY3cB09orHnjShr5OhK/U3+a/KvyuBb5Sb+rolxYYb/XWEL8MxK/j1SMZXlsW6AC/B+HvrxwfdexP5f33JHuUkQwULAjk0nNGfgzZzwb3KuKDNCj7byik/y6q+tc68zVrsuGBhUAvq3960J0ezeXZoN72P3L81RSf62cyviZ5PvbPHvoYud9awLMm96nXvjYz/VFmQDWOfl09FO+hsAn67yLslz4sHtb68GUgBmWk64cvkf8cB8HqCBSRl1/rsSw/vjxww5/GwMfEB+oucDVo8Y9ZEcgFhr4hi553r6DncfX9bx/2w7jAyGHz9ZeBt4H8UXCeo2g9ginyP94g5cvHd+QMrt5h6guYUR+oBhB8DIdgEAUw5Suc/Ctb9Q3HP9h9g+S/5bzS31F//OgcoMW/6tA/ZPoLsy9w8we8vgx7qfcsHg9639WrD9Gn5BOYyoMq+uURNz/9/GnFRrEHANfzh5ifng9/yPcNGf+VqwIisQOp+9eSBkbVD+E31L//Mebh2lWV1WO/+unrLwM//wPmX4H1DyR46z6fVttHKwaLfzF18Yv276n+TODVsxx8XL0aIh2Gtv8VAnE6fwKZlo7+o9U/AvIhDmjF0MNU0DdVoAKZ9NNbVj3DBHisfSARoMVrCf3Xh3L//tNDYX/MQMd47ZkDaLBAhWdWv88c4P6H6n47k/xjdVdfZ8TWe8bP376pv5/e2jfonWUDOuW7h14t/VeuDyu/xeEjB97S6Lvg/hr7jf9A089wLL3h9deXP17eq+9bUr4BbrC887pf+gcqeZTql4c7u1ePg3f/CIq/LQMVBsBDsC4gfT+maRwPQhohUCKEaTrEKdjzCQSNNzCF+LAPvkLYx3wMhzFss8EpEt0QSBjBSADovSbdbw+ElT1Y+wEcIwSNUHEU0T6KYgRMRXCM0QQZe0SEoVFIwTDsf91agBh60+dVyIfZvkwFz/LzqtYfLz6xASv5TX9kXj87aG1SpEPmei1CtK6FYupkyK07EfMwz2p+CFFlii2S4TdDeNncijATbjfZO/JNZ/ZerROVxtFLjJ3g3W7Db7idzhan+EitZwFPLd2KyR2JhIbkK3fGSNzujAqYhcQXCwktC5L0CJpqlTpC9CRSN22yuU7ysbHlSe+o+Rxh1hJXC/VQIOTtaiBlGPiui8hbGGoXoSKOvW3xOnyL/bDkLvLuZiUKSclYvgfYwR3KDeZLps8E0j0I5HssiV7VWkjZKRnvH3p0FKjAw0jBXmzrrARjCcM1q+pUa262l61qQu6tuJmWymVLxODDcWbuC9XoNurdO2QtT0t2pd1eRf2Qe0gWBNd1HFtckR3tjHTD2iF5hC/1DPLhcg1B1FhuZl9ZLv6OwhvBCrXRyRhkCnY+URGoX7SYdPP6yRNnhmFDZMoxt5VDbkTSuDVN2u9Ei0i029JfzzKqIqJuinSOkkuv7Rwe1XrQ2+jEuCgbobUlJTVmteCGYhjoUmesi7eNIFvZns8SvUvFSeKdyV8gxXLylIS23b6wpCErO4u7mCiQDhlQs5ahigguY9HeiJNrBrRAw+l25xCXAw+zNhdTRjBUGXErz8tmP+ykC2p1zDw05jjBmeuvc37Z1ieE4GxDyI6MOU01ibB6b1w5eM8IrWB6mO1fjFOT63IDobx+sg8d1QxLzh7PmgZfQtvabHmF3pc2a012t+vRKx6LndRw2V1BN1ZwnmK1XjzI9ecxmc6oz3DHxjQndwezEM2QZ7oUEHaXByZ8WcfQxte5PbzbTzl6h9bVBaW6WtC2NyaCro7mW1wozTx0ggrhqtXI1nFtJUj0vCdPTJAffYPPs/Cc5ifMtlAz5TIQWNBx6IkQgEl+tq0eQzFtjmTfPMHBtvSv8sE88h5s79xU246If0naC8caVMhuM5E7daLoT8L1Okl2kR2GwY4USVzfl/GWDDUiq5vkosIH/aIbHTUGQhLfxMhNJIlVECOAKYIS4JIuXZerxYhiSws24FIwSPWiElcwNZeFb8c5NssZM7MyZw/KNS5kUt6m1GTjW8kqBSXxC2J9P24FVuQVU9sglLU2w1xv9ZzladgkKmjAIEKAt7MVMGMQjP7plmEkCwIWClG33t+25LWrq5m9cAlC26hO3edUE64BcYkaivZ6VwoGXwpVGIq3h0GT++MOO3jEgQF6zAMtMYdeOzIKKx33kauhmZ3aHRcR6CwN1vZ61qSiqtJxvjI6bPBHgXE4eh1NZL/AkOEGRK/OmlitIWHXoK19lFqP9HpcLynP5nltUk5MvnEStRpQ/mwbkBkxmVDgwq2ItO6wu13FsO8OzRad1YCf7s4R4/dJXZgqwxDmhpGR9GI29lQq+ya1qfqo3nRT9i0xRCJtCBiGAzbj6kRjWDhD215eD5p+3R7iwkv31cm9HGhPKB131yvjlJ3v88H3Ehfl6KC71QUdQFGwx/n4eLQyfn9j5jMDM5wthsLp7Oq1VGHX1mWvnOpnztko89tFsOQFIw/bdbjBlW2UCD0oMMJx3ZJifMbScZicjhszBLg2bnitDxBHBRVUZaF4Zm1W89jFNETsYOzuQ6agW1RAneMk0Xe9VVh9SvYZt0GKCDcHxfdR0jgQF4Q4Wm45CGQHnekpI1g8uAvXnbGz4EwLvUkw0IY4EDNJLCF5mOB62eyKsEK85ERoO2NMNd1uyp1ijexI11rSMzSi9VtTt5a9ftBOE8Ko6PruzXtVXEQTOeT75jogZuRvbgbPIEem86ddZxcCfHW2jIBtZG8HEsPOmu1EkrKVe2E+tDt4c0RiGZfO42J2AQapYWeLR6bCduKZm71roxjFRmY4ZM4EpGwXT3GrDhLK63g2KEY/XflO7BvPTrdUda7GUzDrgd6Qtn0ZmHbNG5cIxjbUIcKZ9XKT0xqSzrGLxpNNLQcFhH3eQaEsmqHe1y1sSGkXd9vqaBfnE2e224N1RDckFqJCzNzr4qbRWWQI++Kwy8mZkxAvV+CTwmUXiq6kjtpmlz2fj4ll+VgibOqLaNAd4Yq+sDgHpL4VsHHbyumw3WeVdwpbCb/pQDrZaFqr3SGwmdtz5iC9zxMNohJ6nYBE45hSzTt8f1jnrHDTT7dDbR6tu733VNDjLePG6MPBkIj8ymVGeme2AH7C65uFVxxHzztRbeMdYvcMy1q5ego60N75+FYIsuAwDmtC3Dprx6YZodhHcNHcjHudpQR8G5vuuWgS0z+cw9Y2peNhF20TD+JwxVhUfcZm5yBM2pLeCtnQUkZv4SS3FM3A2O3xVuSUuCV2WsTYPbStEdi67/B15ew3e7Q8Ozclx4+BMhPUpd2Z94IWp55BL3iABUyPTWhi9Cc8jS7Mep26BK8cI4I9iSfdbSAaOsxncnumlqAVMHO+oiqZX3scd+8TczdThMU2IrpurLWED6w+nK2i4k1XOPQnasZn0dRNinfsnVOh9FZsrm6vo0mpRXu6irQdx0xQ40gIEcNMqNEHdbRoLmx4pxGKxd54KGPTZycaZhRDJtnVwgG3CZrRKhxfPG/dz2q6rskTt3cO1L1oMm62UhlmJB/dMeLEtjDLF+mx3TDYeVd4cM9LaTZOpyLbyFcSOQi4zrQZ1tf+bPnXkL2y2z0zwadwB6fTrEWteVHuPc5MBFLqxyihGMgNb24VMe3gwRdkg+SBMzpXkdreWZPOAg0YbiR5kdX3iGEDuGJo5faWH0SfVbJskiprOYH02vnIHoa4u6NX44YKQeiw9XZ9MHBNUNzM1FBE6Urs2BAdcfLJnZErLSgUQrwRLczRFrFb2JO34XCHYzZ+Du3pJJhZHAU9QoJmMP5QfoUFx2WTVZ28vbuqd44NQzJjvphusKmJFxbkwN1FBy6lz7zk7yuE0SMS3thmPPOy3MYDo7si4XHX0NmaITsLldYUTDFKY3HeRUZ9zo6uA2EBlt/8bq+cQHSQV1/uGCne3WyG1ITtlBmLkx9RW1xsYYikXNhG5i7zRXHBa1ZxsI5G/Wsm6k2Z3M96dCCPTX4Q2NSKB2myqzDye4tqggh0C/rYVcnhnhAscXcIT01Ity7wdZTAWyjjBEzhz0iZnuMo3EhwPp37nCI4kjX5bZttPYs45imRHzT9JOXbSQzDTiXtoOX0/jpfeVkUBUw21B5gcbcyabOuTQemLpK2P86nm3fys2UpsnNwqnzLEsrJJGafK4wNAcU385qLbCpf7X1v9ckmyFQpZsW+PSYs4YWgNTTo8bxPkvF+GiyOszxhMxRzlfpDWPnnC8xqMV3bWo12h9EgzmHqL8v2UrdXby949oJcMePE4eJFkJ3Yv5wGBD3i/UXdHwixlzZHZXCKcctHTV9JAiPQGzg8K/3ENDRm63LqlkDIeg3v4kOnEcdse7otaZvaB4dghP0kSkKkjeF0qEy8FCcqKxtIP89za0P4gdWd5gLgRqfxmsUA0MM4srssvLm+bOpO3XRHJr3h640dWiQuNRSA5AkbOAeJSctMWFuYFd4GX7PUXV+d4UTd29sow6ICqhIE86M9jp8CleXQbnu4n1zeGYN8XfIzUlGOc86TkxCZ9YhT9JnZLlB7HvREGn2wqqGzcihtfqhGFGoKkTr3t0JH4YvH7psx0CdPT/soP9yrqzRf0GRLqoarKofSOB6UjRI41dXOS0xiJEo7yemeCCMLKsOiOrbiQip9xR+Qcg/Zt0rY5chBHk7hvo76lmh57ZLSLHoRtchVavdYoHUponeFSca43ZW7QDqWYstnx7Svq0u3NtqYZ+WE8u+Un/bTgUepYim6lt11OCcC8LpLUT9aE+smPXaxMYghrdds55pNtyE3g8wfTxE8kzyWsJ4jbggjpAd9npxoPPsp1odn6Aag8NEj9bU83C9cvFEuzUgtWzejnRzg7610yRI7p2XH7zoYYPnk0vO2CivYDb9fWP6w7UvrCisNPFNIzPbCNSeiQSNhW7nqXH8d4RkkeIL7nIRam144tSgAM4vDswKt1PhMVRM1qOvyduCVai3aaNOa57ovaNibOVX2YjoUcOGAbgfHiC93P5T9/DzjKdtJdztTEBzNcjk7jRuIdDm2uFDNrO7x3Z3dHbfNvnPrSGi95eQdztdFMwlPIVXZTHBqQEL/qqUwHS1XvmByvuNqqkyNtr441/5wd+xAvl6wWXFOzAXbtlu0LOEmmqumoYQgR0975mRlh1vg4PpOD+ILNe1NcsiK3fmgtFeMsdq6G7T4KoNCmdUe4/Lx/VjsG85nZjnWoLVIL5vJYCFyid3yaK2jlO7uRMbpu1upnmnERhVxOMjNFh5EvjW0qEbUS2bWxEYg3OVQw4vX07lRTKW+ZwJ2S+SJJReByVZ5fb8TbESi+6RTQSZBwX4+myNOKtyU9uV64uQCq0dtcjFJgW9YaFTLkTCDqKpDZchHXqivdjfkLnSRvVwWG0kldqwbhYipd1mzXDfH8XxmChg6WBQ9XdtF20XXdApT1q6tqesQr1PSjmfv6yahokiLCoJR4Y01KKBu3o18MVgVIxFyf4ZRXPQR7mLxcV3sOt4dI4KkegwufLPH/O1h2dhnFWac3YWJl7vgg9mYVQG2vYkhZj7+mStni/OlWC+XHQDkWt5FrdydwNhSm2QzK5BiEAIoLFAcC5soPm6gtX/DiUid7jcaUtrJ3+Gutu0HByG39TKUET1BO48NycvVw24h0RKKjCj0tDmktrIz+bOWBfBaPl+vj9l315vrQtsqEywd2LCFPPQKhyh7pdq6aZHDjYz9zO/a3miWSSDGGfEsRNeZaSHaFDnN+40lXsPMhyD4jpI3uLdL1PdM4qqofupw8sif1aaS/csdJi67nOajPmYHL0FHLh9G28/Jdpf4wxnkiEr2kg36G6+rMc1LFLwnd2W/B723PdSRpbANCkpXEuX1Lh+PwTag4S0aXXMBHRW7ZDIxSpStO58rZ4sTl867LxSNmVIUtoJ0EcfZTRy0uN3V5oahA+sFVIBL0k430zYmF9UrVX3TQLF1rrF214Y8VsEkIqdq5N6F6Vio+hmOzdy1b6V7PkQDcRP30Z6/bm02oEtymE1+2hT50JR+qvQaQF9YWRgoytu4tI2zMnHI6z4P5X14MW212lu0sB3BIHakCKin1te8M+TZOU2mnw/pzFQHC7uejJ2RzJO1VVBBqvWYLJZz5du1dFGCmVKjrMmPfGzfYYXNOSVjoaPMnHlF7zoWM72EUhAn5nhijLeanTqBxCinc94lR984XtKzGC88Bucb6ZQihEPmaXXWlp2ZbsogWGScp6NcP0KOG6UuP7JH+aqiZt8eriInDs2lyrYlGdmwJVDdFU7Z4dJC8iKnGH7rmr25DupWXdbu3M9JLZ7EnX0MuKVjCEKX6GXyWtzDg8Gc6cmSpNHzuMtO0fWeGFEEXlQzXvDpRgJch14p2VVh2kWUi1G5nZUBcBXRo3qEXNckIyq6KusAG2KZr5RgRDx+Z2FZ7hbNxfEcaatROY9jXZlfzL7fibFtjZxX+PoQaKD474tJO6p3XAezxoEJjR5v08jmyrYKdD6+YGSHUZDOt0QfH+eAP87G6XxX6zspQtD6AkF4fr+Gm3VyJRxdwAvckqfY0TnHG90pwSAi5clrqLX52Y7MGyVep/y+WP6p7ba2p5xpKNTvWXQWqx5B0vYSxu1k6DLApJ5c7ITDtk7Gm0sxHFGnCsVg2aUh23vWl9HVtw4eJLjUfetToHUM3kJLiXdCo4atqKiDPKMRslOdw4ddpSubPOXqjLtVZ04a9nCwvkPg3m9jAsa7zCgqSzzL/Dm0shuXrB252Jyyi44YyTQ5w8lKQR3uz3LmXkQ/2eLHixoPmjqtEz6iCD3fn67B1F0UJSFHQU54vom4Pa9bR/5+OYcbqj0ifYKEpTSqEpyWZ645oWAC8g02gfoINy2j9l0+Cfd3l8XNPMUD/4JE/ZVRDoE08JksJ0dq2sT+Ljd2hUIRs5pB8PEgJTF2IueOMzCxvOu7oIEVsSKa24a4JIc63m/nrlT9UT5iJqQhiB3VxzHVxRQTQhHdW5hNlMQN1qxebTU5I6ibw0SB7S5jrelFLBx9t806v0SMfTHsZnnnlGpw7O+gAcaBPDH9bWtba9u+xSLMXO5Kwe6aYL0psv1eS2+hQ+xpbGBYaF73O0PGENqjpI0qMbIazxW6Od9OQjVDLJIvHEsAKS5mujar0ZK9HSp6YT4iSAKP6ElML5ZFU1uJRAfdiYteXaNU04limSMwjaRobNlbt3KRI2+DIazuaFccC9K4OKk+N24sB9MwSfvtTg5mPVxnFMNbFNkaYCLJQhkMpPhEXw8RTk92wKOGwHebxuZaQlTkoplnTyAkM2sxbYO70p6hw1x1lLg3yviEyIh5HXbELdY74Et7E7RKa0tCFveJy91UPcYhah1w5pWIhVw0k7DdItF0RpaMv29UbrwEydQaJ1HwdmvRy+CkzG2vZm9wEHvC7Uhl8ehutPtVkPIF85eOV0VEmQ1DLqfbno+us0t7C27W6ozXtmtbkMtxkhTetliFKPEULztSZWbxwu1duUNs6pTs+Kus8Rs0OV3jeY/eq+aoO3vPWYZ00nRfLY2LN15cplVvQr2NL62x5rSO0ylljIatYNMi6kWmxcOsMu9kWhZ2hmeZNkoiHcGV5o7K1sEtv4C4JEujWbtEo14XpAZpx09hU7cAGA3naWNChqhsAqLDLiV7RdT2dit5RxikMzLZmLOVZ0Y8q6AjVHiwSeM8ouP7nWemiZizOsWO0eABkK/Yum4cxzWxcQ4knibncNcPTHpv9nTJ83rYcJRuhkinOwADYTjiWz2nHaU9pJsb2PBJ2LGU0y6Zbdjt5vM2LW+gPzXs6ew5x36Ray50+bOoowf+sJGZ2C95dx4kuJw0ntii06a6jdHW9OmS6uUDrETcMsPOOB8pBoqb6509k6LUdcOlrnvbS2kHgaxhCg3DUdATG+/vp4xT2gIFk4x6z6uk0V1iHvk7N25wu0dlpvUVRMRr7a6yV9UeLwS/JZNs3MhihWM7ck+xfjdfXePur92q6pr0Xik3fnb31ztmoweUwEc+QLvTlVdjFg5reL/Z8+vrbe2xAqmEV/t2SGEH9dwzHU9RcTDifomcUtqqURFrtoxD53m73Tbr430aUpfUsTIkt0OGmjNinmyibeeJzHJWQ8Z9fWTsvSiGk9TYY6xe/Ao5gEaR3M7bYXddpGRqOJGLreNp7JDDNnTpBl62oxGNMkVfj7EYoTaHwjDPslyX5sa13xW7XOR76sYymZw0e8IsZ4tk+9Ypz+wapIc3hPg2mhDdcJaMjq6YWWo1TRfchbxtNY3cONO9XNOH6SoeahyFpkXcGEQDGXw7BVoHuvnewQ8A9sHY4iq0nmBekcQ+ExUVBOvG0IAhXcgjR6slbx77a48konOjCJyNApq0LtvkyJKM4xZ3xxPySlmjB5UsbrzhHVTNy29riWYP/Bj2za5DJJfneWeQo4BzU6wSy9rVqZ0wSUh51o1Edvh7lQ4DuYwwX5s1WsJ6o/eNHimsc0rTnsq4oHnkw73aI0su2Z2+Xkpa4pkiuOwNbT+K/BpMiEQm25e9dfTLiSGSZU/Nlw2phn6T04EUtfpxXPD4vsYdL1xkmIjKhSyjKMojtcdqsdoUDIQOW8yuErErQoaoYiENamOhdC1OBUtLTiNrIGJ3Hqd+oVLp7CWKA8Xb8ojfNSXv2fZSi2cq4qwKsXBkNDgeXk6YvLUlbn+njfa0ru426F3HvnHzs2FHceVe2sDcD7ebiWR1y1wvo3U+8iDV7jPfhpmIhA2RuCR2Sy4zy5SUkWSJMuVKRWSXs4tp7Jg7uVUIHGVEu2LKa/Y0p6i8ryeiaGsadAWF9/Z8V021cWAuzGmPabBDNnaEZTf7RuJ4LHVu4qbWpr7Np4UpPDTgBTBiNwbZZcQ9uLkkgmgnXuERNFBVhrABJCDl0SWVEdeRw1Dtr3qA3yxHmxi63TdBcqlomZqsm+va7H0fXdrr5PfMZtyM1f2utnZDU7HR4QTOEc01vuUHitq097jf5dSMGNDhmPWBKuL2XRK4+mLH/dzR1Kbe1zoDYoUaNSlFbV3ocZPcutOhztuZQ9Y2f+Z6MHYQkWSRSG/gGKslkLzrAt5xCJyf7jB6vZPIxuEAPjYsuGRCVRY0xoFSPpzT9XrKEe8ASGvazWMzgzvEgT6CGnk8G0w/n5B1O2eIewNT6hY4fXtK7lQPK8qGm1rqLK3JcPZDP3Z8/tZqDLJADi2TwkETrtgVp1peG6ZLqCVpZPa1h67l0iyEhNH10FmivAB56LM+PsB73FrwcKp9zpGvNWncVfJWipvQrsOuOOIjq1aMklMGTanBXcBAFbpsocshtIizap5jcqroEetxf4LGWZm1qTb1WYD2SoOdN9htsoZjfxDXTmyyexYu6nRzNBcP30k8enBgsSQpBF+moMpu/sBSG0/pSQo9pWhfHdJlLY64HBB32AGD6w5FRiwlvSqe6XgXDW7ZmDK+xmJ1EOrLziruB6uL3OVqHPgFG0OtCt21a8ldSjYGezFmMeIFemq5vR0z+ZpFJE+Y2QKzEJO2/XPWn1GqmOj0IEBIQ5IwuVFQMXNEnmXWtrMh9xXZXI1FJ6YiHI784XqqWRX313cqxtZHR2OYl48v7+d2nmcgfnBy9HFS4v/ZgY3XsxXNBDjWQfQ4lPI4N/frk9evP2b/nx9fuiADzF/PmfTlmLwd13geGuy+P0bWL6/ngR/HfW7D+5EzMFQ//jPS8zQLWPQ8w/Py8eVPe98O/7x8OZD14P08dP488QL4f0Jf/v5/AK2wtKKRNwAA -->
