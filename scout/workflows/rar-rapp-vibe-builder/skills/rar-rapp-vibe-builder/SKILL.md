---
name: "rar-rapp-vibe-builder"
description: "Builds a complete rapplication (agent + service) from a natural language description. Use this when the user wants to create a new app, tool, or tracker \u2014 e.g. 'build me a bookmark manager' or 'I need a time tracker'. Generates both the conversational agent and the HTTP API, sharing the same data store. The generated agent is immediately usable in the next message."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/vibe_builder_agent", "rar_sha256": "c5e273a8c24b444d326c42dc45bba66e933b3a759893bc4ed1b20776ccb0539b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "RAPP", "tags": ["meta", "builder", "rapplication"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vibe_builder_agent.py` and embedded as the fenced Python below (sha256 c5e273a8c24b444d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vibe_builder_agent.py` first:

```bash
python3 vibe_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vibe_builder_agent.py   # or on stdin
python3 vibe_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/vibe_builder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/vibe_builder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/vibe_builder_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
