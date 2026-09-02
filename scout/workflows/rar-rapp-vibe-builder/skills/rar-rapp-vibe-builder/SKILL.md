---
name: "rar-rapp-vibe-builder"
description: "Builds a complete rapplication (agent + service) from a natural language description. Use this when the user wants to create a new app, tool, or tracker \u2014 e.g. 'build me a bookmark manager' or 'I need a time tracker'. Generates both the conversational agent and the HTTP API, sharing the same data store. The generated agent is immediately usable in the next message."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/vibe_builder_agent", "rar_sha256": "8fd77f26eacf4f4f22b7b48c06cc22e0fa76af51c2d20bb21a2194cc16de967f", "source_kind": "rar-agent", "source_commit": "ce4d2aa63a3ebb409c34534643e32ab7cccd8aa2", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "vibe_builder_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/vibe-builder:577377816bfe14958ec97d367d8c265b658235afbc4bf80f2b2d66b9de234f8f", "kind": "skill"}, "version": "1.0.1", "author": "RAPP", "tags": ["meta", "builder", "rapplication"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/vibe_builder_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `vibe_builder_agent.py` is
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
