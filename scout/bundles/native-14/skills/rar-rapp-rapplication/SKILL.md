---
name: "rar-rapp-rapplication"
description: "Bundle, inspect, or validate a single-file agent against the RAPP rapplication contract. Use this when a teammate has a working *_agent.py and wants to publish it.\n\nActions:\n \u2022 'bundle'   \u2014 Produce a publish-ready directory with the agent file, optional service file, manifest.json, an index.json catalog snippet, and a README.\n \u2022 'inspect'  \u2014 Read the agent source and report what would be bundled. No files written.\n \u2022 'validate' \u2014 Check contract conformance only (errors + warnings). No files written.\n\nPaths can be absolute, relative to the cwd, or relative to the brainstem root (so 'agents/kanban_agent.py' works)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapplication_agent", "rar_sha256": "a40d2ce08abde9774ebb4d34f02577a31e15a2ef66d2064953ab08a3f39baa0b", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapplication_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/rapplication:a688baf6fa232496c28cee39e3621b98163ef432fb7e7ab5a623704c533c2cd3", "kind": "skill"}, "version": "1.0.2", "author": "RAPP", "tags": ["meta", "build", "rapplication", "bundler", "publish"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/rapplication_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapplication_agent.py` is
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
