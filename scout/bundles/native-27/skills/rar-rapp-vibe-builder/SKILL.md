---
name: "rar-rapp-vibe-builder"
description: "Builds a complete rapplication (agent + service) from a natural language description. Use this when the user wants to create a new app, tool, or tracker \u2014 e.g. 'build me a bookmark manager' or 'I need a time tracker'. Generates both the conversational agent and the HTTP API, sharing the same data store. The generated agent is immediately usable in the next message."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/vibe_builder_agent", "rar_sha256": "8fd77f26eacf4f4f22b7b48c06cc22e0fa76af51c2d20bb21a2194cc16de967f", "source_kind": "rar-agent", "source_commit": "ce4d2aa63a3ebb409c34534643e32ab7cccd8aa2", "version": "1.0.1", "author": "RAPP", "tags": ["meta", "builder", "rapplication"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/vibe_builder_agent`. The original RAPP
agent is preserved byte-for-byte in `vibe_builder_agent.py` and in the RCI capsule.

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

vibe_builder_agent.py — Build a complete rapplication from natural language.

"Build me a bookmark manager" → generates bookmark_agent.py + bookmark_service.py,
both hot-loaded and ready to use immediately. Agent-first: the generated agent
works through any LLM, the service is optional HTTP for UIs.

Auto-generates both files deterministically from an LLM-produced spec.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "description": {
      "description": "What the rapplication should do, in plain English.",
      "type": "string"
    },
    "name": {
      "description": "Optional name override (snake_case). Auto-generated if omitted.",
      "type": "string"
    }
  },
  "required": [
    "description"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vibe_builder_agent.py` and embedded as the fenced Python below (sha256 8fd77f26eacf4f4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vibe_builder_agent.py` first:

```bash
python3 vibe_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vibe_builder_agent.py   # or on stdin
python3 vibe_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
vibe_builder_agent.py — Build a complete rapplication from natural language.

"Build me a bookmark manager" → generates bookmark_agent.py + bookmark_service.py,
both hot-loaded and ready to use immediately. Agent-first: the generated agent
works through any LLM, the service is optional HTTP for UIs.

Auto-generates both files deterministically from an LLM-produced spec.
"""

import json
import os
import uuid
import importlib.util
import sys
from datetime import datetime
from pathlib import Path
from agents.basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/vibe_builder_agent",
    "version": "1.0.1",
    "display_name": "VibeBuilder",
    "description": "Builds a complete rapplication (agent + service) from a natural language description.",
    "author": "RAPP",
    "tags": ["meta", "builder", "rapplication"],
    "category": "platform",
    "quality_tier": "official",
    "requires_env": [],
    "example_call": "Build me a bookmark manager",
}


class VibeBuilderAgent(BasicAgent):
    def __init__(self):
        self.name = "VibeBuilder"
        self.metadata = {
            "name": self.name,
            "description": (
                "Builds a complete rapplication (agent + service) from a natural "
                "language description. Use this when the user wants to create a new "
                "app, tool, or tracker — e.g. 'build me a bookmark manager' or "
                "'I need a time tracker'. Generates both the conversational agent "
                "and the HTTP API, sharing the same data store. The generated agent "
                "is immediately usable in the next message."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string",
                        "description": "What the rapplication should do, in plain English.",
                    },
                    "name": {
                        "type": "string",
                        "description": "Optional name override (snake_case). Auto-generated if omitted.",
                    },
                },
                "required": ["description"],
            },
        }
        self.agents_dir = Path(__file__).parent
        self.services_dir = self.agents_dir.parent / "services"
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        description = (kwargs.get("description") or kwargs.get("query") or "").strip()
        name_override = (kwargs.get("name") or "").strip()

        if not description:
            return json.dumps({"status": "error", "summary": "Description required."})

        # 1. Get spec from LLM
        spec = self._generate_spec(description)
        if name_override:
            spec["entity_name"] = self._to_snake_case(name_override)
            spec["display_name"] = name_override.replace("_", " ").title()

        name = spec["entity_name"]
        display = spec["display_name"]
        class_name = display.replace(" ", "") + "Agent"

        # 2. Check for collisions
        agent_path = self.agents_dir / f"{name}_agent.py"
        service_path = self.services_dir / f"{name}_service.py"
        if agent_path.exists():
            return json.dumps({"status": "error", "summary": f"Agent '{name}_agent.py' already exists."})

        # 3. Generate code
        agent_code = self._build_agent_code(spec)
        service_code = self._build_service_code(spec)

        # 4. Write files
        agent_path.write_text(agent_code, encoding="utf-8")
        self.services_dir.mkdir(exist_ok=True)
        service_path.write_text(service_code, encoding="utf-8")

        # 5. Hot-load the agent
        load_result = self._hot_load_agent(agent_path, class_name)

        summary = (
            f'Built rapplication "{display}"!\n'
            f"  Agent: agents/{name}_agent.py (loaded: {load_result.get('success', False)})\n"
            f"  Service: services/{name}_service.py (auto-discovers next request)\n"
            f"  Storage: .brainstem_data/{name}.json\n\n"
            f'Try: "{spec.get("example_call", f"Use the {display}")}"'
        )

        return json.dumps({
            "status": "ok",
            "summary": summary,
            "agent_file": f"{name}_agent.py",
            "service_file": f"{name}_service.py",
            "entity_name": name,
            "display_name": display,
        })

    # ── Spec generation ──────────────────────────────────────────────────

    def _generate_spec(self, description):
        prompt = (
            "You are generating a specification for a CRUD rapplication.\n"
            f"The user wants: {description}\n\n"
            "Return ONLY valid JSON (no markdown, no explanation) with this structure:\n"
            "{\n"
            '  "entity_name": "bookmark",\n'
            '  "entity_plural": "bookmarks",\n'
            '  "display_name": "Bookmark",\n'
            '  "description": "A bookmark manager you can talk to.",\n'
            '  "category": "productivity",\n'
            '  "tags": ["bookmarks", "links"],\n'
            '  "example_call": "Save a bookmark for github.com",\n'
            '  "default_data_key": "bookmarks",\n'
            '  "fields": [\n'
            '    {"name": "url", "type": "string", "description": "The URL to bookmark", "required": true},\n'
            '    {"name": "title", "type": "string", "description": "Title or label", "required": false}\n'
            '  ],\n'
            '  "actions": ["create", "list", "delete", "search"],\n'
            '  "id_prefix": "bm"\n'
            "}\n\n"
            "Rules:\n"
            "- entity_name must be snake_case, singular\n"
            "- entity_plural must be snake_case, plural\n"
            "- display_name must be CamelCase, singular\n"
            "- fields: each field has name, type (string/number/boolean/array), description, required\n"
            "- actions: always include create, list, delete. Optionally add update, search, or domain-specific actions\n"
            "- id_prefix: 2-3 char prefix for generated IDs\n"
            "- Keep it simple — 3-6 fields, 3-5 actions\n"
        )

        raw = self._call_llm(prompt)
        if raw:
            try:
                # Strip markdown code fences if present
                text = raw.strip()
                if text.startswith("```"):
                    text = text.split("\n", 1)[1] if "\n" in text else text[3:]
                if text.endswith("```"):
                    text = text[:-3]
                text = text.strip()
                if text.startswith("json"):
                    text = text[4:].strip()
                spec = json.loads(text)
                # Validate required keys
                for key in ("entity_name", "entity_plural", "display_name", "fields", "actions"):
                    if key not in spec:
                        raise ValueError(f"Missing key: {key}")
                return spec
            except Exception:
                pass

        # Fallback: generic CRUD spec
        return self._fallback_spec(description)

    def _fallback_spec(self, description):
        # Extract a name from the description
        words = description.lower().split()
        skip = {"a", "an", "the", "for", "to", "that", "which", "build", "create",
                "make", "me", "my", "app", "tool", "tracker", "manager", "system",
                "rapplication", "i", "need", "want"}
        name_words = [w for w in words if w.isalpha() and w not in skip]
        name = name_words[0] if name_words else "item"
        return {
            "entity_name": name,
            "entity_plural": name + "s",
            "display_name": name.title(),
            "description": f"A {name} manager you can talk to.",
            "category": "general",
            "tags": [name, "rapplication"],
            "example_call": f"Create a new {name}",
            "default_data_key": name + "s",
            "fields": [
                {"name": "name", "type": "string", "description": f"Name of the {name}", "required": True},
                {"name": "description", "type": "string", "description": "Optional description", "required": False},
                {"name": "status", "type": "string", "description": "Status (active/done/archived)", "required": False},
            ],
            "actions": ["create", "list", "update", "delete"],
            "id_prefix": name[:2],
        }

    # ── Agent code generation ────────────────────────────────────────────

    def _build_agent_code(self, spec):
        name = spec["entity_name"]
        plural = spec.get("entity_plural", name + "s")
        display = spec["display_name"]
        class_name = display.replace(" ", "") + "Agent"
        data_key = spec.get("default_data_key", plural)
        desc = spec.get("description", f"A {name} manager you can talk to.")
        category = spec.get("category", "general")
        tags = json.dumps(spec.get("tags", [name, "rapplication"]))
        example = spec.get("example_call", f"Create a new {name}")
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        fields = spec.get("fields", [])
        actions = spec.get("actions", ["create", "list", "delete"])
        id_prefix = spec.get("id_prefix", name[:2])

        # Build parameter properties
        params = {
            "action": {
                "type": "string",
                "enum": actions,
                "description": "What to do.",
            },
            "item_id": {
                "type": "string",
                "description": f"{display} ID (for update/delete). Use 'list' to find IDs.",
            },
        }
        for f in fields:
            params[f["name"]] = {"type": f.get("type", "string"), "description": f.get("description", "")}
        params_json = json.dumps({"type": "object", "properties": params, "required": ["action"]}, indent=12)

        # Build perform body
        perform_body = self._build_perform_body(spec)

        return f'''"""
{name}_agent.py — {desc}

Agent-first: works through any LLM with no UI required.
The optional {name}_service.py exposes the same data over HTTP.

Storage: .brainstem_data/{name}.json
Auto-generated by VibeBuilder on {date}.
"""

import json
import uuid
import os
from datetime import datetime
from agents.basic_agent import BasicAgent


__manifest__ = {{
    "schema": "rapp-agent/1.0",
    "name": "@rapp/vibe_builder_agent",
    "version": "1.0.0",
    "display_name": "{display}",
    "description": "{desc}",
    "author": "RAPP",
    "tags": {tags},
    "category": "{category}",
    "quality_tier": "community",
    "requires_env": [],
    "example_call": "{example}",
}}


def _data_path():
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        ".brainstem_data", "{name}.json"
    )


def _read():
    path = _data_path()
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {{"{data_key}": {{}}}}


def _write(data):
    path = _data_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


class {class_name}(BasicAgent):
    def __init__(self):
        self.name = "{display}"
        self.metadata = {{
            "name": self.name,
            "description": (
                "{desc} Call this when the user wants to create, list, "
                "update, delete, or search {plural}."
            ),
            "parameters": {params_json},
        }}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get("action", "list")
        data = _read()

{perform_body}
        return json.dumps({{"status": "error", "summary": f"Unknown action: {{action}}"}})
'''

    def _build_perform_body(self, spec):
        name = spec["entity_name"]
        plural = spec.get("entity_plural", name + "s")
        display = spec["display_name"]
        data_key = spec.get("default_data_key", plural)
        fields = spec.get("fields", [])
        actions = spec.get("actions", ["create", "list", "delete"])
        id_prefix = spec.get("id_prefix", name[:2])

        required_fields = [f for f in fields if f.get("required")]
        first_field = fields[0]["name"] if fields else "name"

        lines = []

        if "create" in actions:
            extract_lines = []
            item_dict_lines = []
            for f in fields:
                extract_lines.append(f'            {f["name"]} = kwargs.get("{f["name"]}", "")')
                item_dict_lines.append(f'                "{f["name"]}": {f["name"]},')
            lines.append(f"""        if action == "create":
{chr(10).join(extract_lines)}
            tid = str(uuid.uuid4())[:8]
            data["{data_key}"][tid] = {{
{chr(10).join(item_dict_lines)}
                "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }}
            _write(data)
            return json.dumps({{
                "status": "ok",
                "summary": f'Created {name} "{{kwargs.get("{first_field}", tid)}}" (ID: {{tid}})',
                "item_id": tid,
            }})
""")

        if "list" in actions:
            format_parts = []
            for f in fields[:3]:
                format_parts.append(f"t.get('{f['name']}', '')")
            format_expr = " | ".join(f"{{{p}}}" for p in format_parts) if format_parts else '{t}'
            lines.append(f"""        if action == "list":
            items = data["{data_key}"]
            if not items:
                return json.dumps({{"status": "ok", "summary": "No {plural} yet.", "{data_key}": {{}}}})
            lines = []
            for tid, t in items.items():
                line = f"  - [{{tid}}] {format_expr}"
                lines.append(line)
            return json.dumps({{
                "status": "ok",
                "summary": f"{{len(items)}} {plural}:\\n" + "\\n".join(lines),
                "{data_key}": items,
            }})
""")

        if "update" in actions:
            update_lines = []
            for f in fields:
                update_lines.append(f'            if kwargs.get("{f["name"]}"): data["{data_key}"][tid]["{f["name"]}"] = kwargs["{f["name"]}"]')
            lines.append(f"""        if action == "update":
            tid = kwargs.get("item_id", "")
            if tid not in data["{data_key}"]:
                return json.dumps({{"status": "error", "summary": f"{display} {{tid}} not found."}})
{chr(10).join(update_lines)}
            _write(data)
            return json.dumps({{"status": "ok", "summary": f"Updated {name} {{tid}}"}})
""")

        if "delete" in actions:
            lines.append(f"""        if action == "delete":
            tid = kwargs.get("item_id", "")
            if tid not in data["{data_key}"]:
                return json.dumps({{"status": "error", "summary": f"{display} {{tid}} not found."}})
            removed = data["{data_key}"].pop(tid)
            _write(data)
            label = removed.get('{first_field}', tid)
            return json.dumps({{"status": "ok", "summary": f'Deleted {name} "{{label}}"'}})
""")

        if "search" in actions:
            lines.append(f"""        if action == "search":
            query = " ".join(str(v) for v in kwargs.values() if v and v != "search").lower()
            matches = {{}}
            for tid, t in data["{data_key}"].items():
                hay = json.dumps(t).lower()
                if query in hay:
                    matches[tid] = t
            if not matches:
                return json.dumps({{"status": "ok", "summary": f"No {plural} match '{{query}}'."}})
            lines = [f"  - [{{tid}}] {{json.dumps(t)}}" for tid, t in matches.items()]
            return json.dumps({{"status": "ok", "summary": f"{{len(matches)}} match(es):\\n" + "\\n".join(lines)}})
""")

        return "\n".join(lines)

    # ── Service code generation ──────────────────────────────────────────

    def _build_service_code(self, spec):
        name = spec["entity_name"]
        plural = spec.get("entity_plural", name + "s")
        display = spec["display_name"]
        data_key = spec.get("default_data_key", plural)
        fields = spec.get("fields", [])
        date = datetime.now().strftime("%Y-%m-%d %H:%M")

        handle_body = self._build_handle_body(spec)

        return f'''"""
{name}_service.py — Optional HTTP layer for the {display} rapplication.

Reads/writes the same .brainstem_data/{name}.json that
{name}_agent.py uses. The agent works without this service.
Auto-generated by VibeBuilder on {date}.
"""

import json
import os
import uuid
from datetime import datetime

name = "{name}"

_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".brainstem_data")
_STATE_FILE = os.path.join(_DATA_DIR, "{name}.json")


def _read():
    if os.path.exists(_STATE_FILE):
        with open(_STATE_FILE) as f:
            return json.load(f)
    return {{"{data_key}": {{}}}}


def _write(data):
    os.makedirs(_DATA_DIR, exist_ok=True)
    with open(_STATE_FILE, "w") as f:
        json.dump(data, f, indent=2)


def handle(method, path, body):
    data = _read()

{handle_body}
    return {{"error": "not found"}}, 404
'''

    def _build_handle_body(self, spec):
        name = spec["entity_name"]
        plural = spec.get("entity_plural", name + "s")
        data_key = spec.get("default_data_key", plural)
        fields = spec.get("fields", [])

        field_assigns = []
        for f in fields:
            field_assigns.append(f'        if "{f["name"]}" in body: item["{f["name"]}"] = body["{f["name"]}"]')

        return f"""    # GET /api/{name} — list all
    if method == "GET" and path == "":
        return data, 200

    # POST /api/{name}/items — create
    if method == "POST" and path == "items":
        tid = str(uuid.uuid4())[:8]
        item = {{k: body.get(k, "") for k in {json.dumps([f["name"] for f in fields])}}}
        item["created"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        data["{data_key}"][tid] = item
        _write(data)
        return {{"status": "ok", "id": tid}}, 201

    # PUT /api/{name}/items/<id> — update
    if method == "PUT" and path.startswith("items/"):
        tid = path[len("items/"):]
        if tid not in data["{data_key}"]:
            return {{"error": "not found"}}, 404
        item = data["{data_key}"][tid]
{chr(10).join(field_assigns)}
        _write(data)
        return {{"status": "ok", "item": item}}, 200

    # DELETE /api/{name}/items/<id> — delete
    if method == "DELETE" and path.startswith("items/"):
        tid = path[len("items/"):]
        if tid not in data["{data_key}"]:
            return {{"error": "not found"}}, 404
        data["{data_key}"].pop(tid)
        _write(data)
        return {{"status": "ok"}}, 200
"""

    # ── Utilities (from LearnNew) ────────────────────────────────────────

    def _call_llm(self, prompt):
        try:
            brainstem = sys.modules.get("brainstem") or sys.modules.get("__main__")
            call_copilot = getattr(brainstem, "call_copilot", None) if brainstem else None
            if call_copilot is None:
                return None
            resp = call_copilot([{"role": "user", "content": prompt}])
            choice = (resp.get("choices") or [{}])[0]
            content = (choice.get("message") or {}).get("content") or ""
            return content.strip() or None
        except Exception:
            return None

    def _hot_load_agent(self, file_path, class_name):
        try:
            spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module_name = f"agents.{file_path.stem}"
            sys.modules[module_name] = module
            return {"success": True, "class": class_name}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def _to_snake_case(self, text):
        import re
        s = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower())
        return s.strip("_")
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
