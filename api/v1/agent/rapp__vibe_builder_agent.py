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
    "version": "1.0.0",
    "display_name": "VibeBuilder",
    "description": "Builds a complete rapplication (agent + service) from a natural language description.",
    "author": "RAPP",
    "tags": ["meta", "builder", "rapplication"],
    "category": "platform",
    "quality_tier": "community",
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