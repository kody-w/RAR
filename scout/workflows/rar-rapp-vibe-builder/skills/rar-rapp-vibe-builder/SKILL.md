---
name: "rar-rapp-vibe-builder"
description: "Builds a complete rapplication (agent + service) from a natural language description. Use this when the user wants to create a new app, tool, or tracker \u2014 e.g. 'build me a bookmark manager' or 'I need a time tracker'. Generates both the conversational agent and the HTTP API, sharing the same data store. The generated agent is immediately usable in the next message."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/vibe_builder_agent", "rar_sha256": "c5e273a8c24b444d326c42dc45bba66e933b3a759893bc4ed1b20776ccb0539b", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "RAPP", "tags": ["meta", "builder", "rapplication"]}
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
