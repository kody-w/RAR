---
name: "rar-rapp-learn-new"
description: "Creates new RAPP agents or swarms from natural-language descriptions. Actions: 'create' generates a single agent, 'swarm' creates a multi-agent pipeline, 'list' shows generated agents, 'delete' removes one, 'preview' dry-runs generation, 'submit' prepares a RAR registry submission. Call when the user wants to teach the brainstem something new, create a custom agent, or build an agent swarm."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/learn_new", "rar_sha256": "ee12a37ef550c9ffb1097334da29ebcb4dcaeeac5b3f8b5dbab366e5178eab71", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "2.1.1", "author": "RAPP", "tags": ["meta", "generator", "scaffolding", "learn", "swarm"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/learn_new`. The original RAPP
agent is preserved byte-for-byte in `learn_new_agent.py` and in the RCI capsule.

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

LearnNewAgent - Meta-agent that creates new agents and swarms from natural language.

Describe what you want the agent to do and LearnNewAgent generates,
saves, and hot-loads it — agents building agents in real-time.
Generated agents follow the Single File Agent pattern: one file
containing documentation, metadata contract, and deterministic code.

v2: adds swarm generation, RAR registry compatibility, and submit workflow.
Output is dual-compatible — works in local brainstem AND ready for the
RAR registry (https://github.com/kody-w/RAR).

Actions:
  create  — Generate and save a single agent (default)
  swarm   — Generate a multi-agent pipeline + orchestrator
  list    — List generated agents in agents/
  delete  — Remove a generated agent
  preview — Show what would be generated without writing
  submit  — Prepare a RAR-compatible submission

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Action to perform.",
      "enum": [
        "create",
        "swarm",
        "list",
        "delete",
        "preview",
        "submit"
      ],
      "type": "string"
    },
    "agents_in_swarm": {
      "description": "For swarm: comma-separated sub-agent roles (e.g. 'researcher,writer,editor').",
      "type": "string"
    },
    "category": {
      "description": "Agent category for the registry.",
      "enum": [
        "general",
        "productivity",
        "sales",
        "support",
        "data",
        "automation",
        "integrations",
        "devtools",
        "pipeline"
      ],
      "type": "string"
    },
    "description": {
      "description": "Natural language description of what the new agent should do.",
      "type": "string"
    },
    "name": {
      "description": "Name for the new agent (optional, will be generated from description).",
      "type": "string"
    },
    "namespace": {
      "description": "RAR namespace for submission (e.g. @myname). Defaults to @rapp.",
      "type": "string"
    },
    "query": {
      "description": "Natural language query that may contain the agent description.",
      "type": "string"
    },
    "requires_env": {
      "description": "Comma-separated env vars the agent needs (e.g. 'API_KEY,WEBHOOK_URL').",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `learn_new_agent.py` and embedded as the fenced Python below (sha256 ee12a37ef550c9ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `learn_new_agent.py` first:

```bash
python3 learn_new_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 learn_new_agent.py   # or on stdin
python3 learn_new_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
LearnNewAgent - Meta-agent that creates new agents and swarms from natural language.

Describe what you want the agent to do and LearnNewAgent generates,
saves, and hot-loads it — agents building agents in real-time.
Generated agents follow the Single File Agent pattern: one file
containing documentation, metadata contract, and deterministic code.

v2: adds swarm generation, RAR registry compatibility, and submit workflow.
Output is dual-compatible — works in local brainstem AND ready for the
RAR registry (https://github.com/kody-w/RAR).

Actions:
  create  — Generate and save a single agent (default)
  swarm   — Generate a multi-agent pipeline + orchestrator
  list    — List generated agents in agents/
  delete  — Remove a generated agent
  preview — Show what would be generated without writing
  submit  — Prepare a RAR-compatible submission
"""

import json
import re
import subprocess
from pathlib import Path
from datetime import datetime

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/learn_new",
    "version": "2.1.1",
    "display_name": "LearnNew",
    "description": "Generates, saves, and hot-loads new single-file RAPP agents or swarms from natural-language descriptions using built-in code templates.",
    "author": "RAPP",
    "tags": ["meta", "generator", "scaffolding", "learn", "swarm"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {"args": {"action": "create", "description": "An agent that summarizes web pages by URL"}},
}


class LearnNewAgent(BasicAgent):

    AGENT_TEMPLATE = '''""\"
{description}

Auto-generated by LearnNewAgent on {date}.
Drop this file into any RAPP brainstem's agents/ directory and it works.
Compatible with the RAR registry at https://github.com/kody-w/RAR
""\"

import json
{extra_imports}
try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


__manifest__ = {{
    "schema": "rapp-agent/1.0",
    "name": "@{namespace}/{snake_name}",
    "version": "1.0.0",
    "display_name": "{agent_name}",
    "description": "{agent_description}",
    "author": "{author}",
    "tags": {tags_json},
    "category": "{category}",
    "quality_tier": "community",
    "requires_env": {env_json},
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {{"args": {example_args_json}}},
    "estimated_rpp": {estimated_rpp},
    "rpp_basis": "{rpp_basis}",
}}


class {class_name}(BasicAgent):
    def __init__(self):
        self.name = '{agent_name}'
        self.metadata = {{
            "name": self.name,
            "description": __manifest__["description"],
            "estimated_rpp": __manifest__.get("estimated_rpp"),
            "parameters": {{
                "type": "object",
                "properties": {{
                    "query": {{
                        "type": "string",
                        "description": "The user\'s request or input."
                    }}{extra_params}
                }},
                "required": []
            }}
        }}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        """Execute the agent\'s task."""
        query = kwargs.get('query', '')

{perform_body}


if __name__ == "__main__":
    a = {class_name}()
    print(a.perform(query="test"))
'''

    SWARM_SUB_TEMPLATE = '''""\"
{description}

Part of the {swarm_name} swarm pipeline. Handles the {role} stage.
Auto-generated by LearnNewAgent on {date}.
""\"

import json
{extra_imports}
try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


__manifest__ = {{
    "schema": "rapp-agent/1.0",
    "name": "@{namespace}/{snake_name}",
    "version": "1.0.0",
    "display_name": "{agent_name}",
    "description": "{agent_description}",
    "author": "{author}",
    "tags": {tags_json},
    "category": "{category}",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {{"args": {{"task": "example {role} task"}}}},
}}


class {class_name}(BasicAgent):
    def __init__(self):
        self.name = '{agent_name}'
        self.metadata = {{
            "name": self.name,
            "description": __manifest__["description"],
            "estimated_rpp": __manifest__.get("estimated_rpp"),
            "parameters": {{
                "type": "object",
                "properties": {{
                    "task": {{
                        "type": "string",
                        "description": "What to {role}"
                    }}
                }},
                "required": ["task"]
            }}
        }}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        task = kwargs.get('task', '')

{perform_body}


if __name__ == "__main__":
    a = {class_name}()
    print(a.perform(task="test"))
'''

    SWARM_ORCH_TEMPLATE = '''""\"
{description}

Orchestrates the {swarm_name} swarm by coordinating sub-agents:
{sub_agent_list}

Auto-generated by LearnNewAgent on {date}.
Drop this file into any RAPP brainstem's agents/ directory and it works.
Use SwarmFactory to converge the sub-agents into a single shareable singleton.
""\"

import json
import os

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent

{sub_agent_imports}


__manifest__ = {{
    "schema": "rapp-agent/1.0",
    "name": "@{namespace}/{snake_name}",
    "version": "1.0.0",
    "display_name": "{swarm_name}",
    "description": "{agent_description}",
    "author": "{author}",
    "tags": {tags_json},
    "category": "{category}",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {{"args": {{"task": "Run the {swarm_name} pipeline"}}}},
}}


class {class_name}(BasicAgent):
    def __init__(self):
        self.name = '{swarm_name}'
        self.metadata = {{
            "name": self.name,
            "description": __manifest__["description"],
            "estimated_rpp": __manifest__.get("estimated_rpp"),
            "parameters": {{
                "type": "object",
                "properties": {{
                    "task": {{
                        "type": "string",
                        "description": "What you want the swarm to do"
                    }},
                    "sub_agent": {{
                        "type": "string",
                        "description": "Optional: run a specific sub-agent by name instead of the full pipeline"
                    }}
                }},
                "required": ["task"]
            }}
        }}
        super().__init__(name=self.name, metadata=self.metadata)
        self._agents = {{}}

    def _get_agent(self, name):
        if name not in self._agents:
            agents = {{{agent_map}}}
            cls = agents.get(name)
            if cls:
                self._agents[name] = cls()
        return self._agents.get(name)

    def perform(self, **kwargs):
        task = kwargs.get('task', '')
        sub_agent = kwargs.get('sub_agent', '')

        if sub_agent:
            agent = self._get_agent(sub_agent)
            if not agent:
                available = {agent_names_json}
                return json.dumps({{"status": "error",
                    "message": f"Unknown sub-agent '{{sub_agent}}'. Available: {{available}}"}})
            return agent.perform(task=task, **kwargs)

        results = {{}}
        pipeline = {pipeline_json}
        slush = {{}}
        for step_name in pipeline:
            agent = self._get_agent(step_name)
            if agent:
                agent_kwargs = {{"task": task}}
                if hasattr(agent, 'context'):
                    agent.context = type('Ctx', (), {{'slush': slush}})()
                r = agent.perform(**agent_kwargs)
                results[step_name] = r
                try:
                    parsed = json.loads(r)
                    if 'data_slush' in parsed:
                        slush.update(parsed['data_slush'])
                except (json.JSONDecodeError, TypeError):
                    pass

        return json.dumps({{
            "status": "ok",
            "swarm": "{swarm_name}",
            "pipeline_steps": len(pipeline),
            "results": results,
        }})


if __name__ == "__main__":
    a = {class_name}()
    print(a.perform(task="test"))
'''

    def __init__(self):
        self.name = 'LearnNew'
        self.metadata = {
            "name": self.name,
            "description": (
                "Creates new RAPP agents or swarms from natural-language descriptions. "
                "Actions: 'create' generates a single agent, 'swarm' creates a multi-agent "
                "pipeline, 'list' shows generated agents, 'delete' removes one, "
                "'preview' dry-runs generation, 'submit' prepares a RAR registry submission. "
                "Call when the user wants to teach the brainstem something new, create a "
                "custom agent, or build an agent swarm."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string",
                        "description": "Natural language description of what the new agent should do."
                    },
                    "name": {
                        "type": "string",
                        "description": "Name for the new agent (optional, will be generated from description)."
                    },
                    "action": {
                        "type": "string",
                        "description": "Action to perform.",
                        "enum": ["create", "swarm", "list", "delete", "preview", "submit"]
                    },
                    "query": {
                        "type": "string",
                        "description": "Natural language query that may contain the agent description."
                    },
                    "category": {
                        "type": "string",
                        "enum": ["general", "productivity", "sales", "support", "data",
                                 "automation", "integrations", "devtools", "pipeline"],
                        "description": "Agent category for the registry."
                    },
                    "namespace": {
                        "type": "string",
                        "description": "RAR namespace for submission (e.g. @myname). Defaults to @rapp."
                    },
                    "agents_in_swarm": {
                        "type": "string",
                        "description": "For swarm: comma-separated sub-agent roles (e.g. 'researcher,writer,editor')."
                    },
                    "requires_env": {
                        "type": "string",
                        "description": "Comma-separated env vars the agent needs (e.g. 'API_KEY,WEBHOOK_URL')."
                    }
                },
                "required": []
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)
        self.agents_dir = Path(__file__).parent

    def perform(self, **kwargs):
        action = kwargs.pop('action', 'create')
        description = kwargs.pop('description', '')
        name = kwargs.pop('name', '')
        query = kwargs.pop('query', '')

        if not description and query:
            description = query

        if action == 'list':
            return self._list_generated_agents()
        elif action == 'delete':
            return self._delete_agent(name or description)
        elif action == 'preview':
            if kwargs.get('agents_in_swarm'):
                return self._create_swarm(description, name, write=False, **kwargs)
            return self._create_agent(description, name, write=False, **kwargs)
        elif action == 'submit':
            return self._prepare_submit(description, name, **kwargs)
        elif action == 'swarm':
            return self._create_swarm(description, name, write=True, **kwargs)
        else:
            return self._create_agent(description, name, write=True, **kwargs)

    # ── Single agent creation ─────────────────────────────────────────────

    def _create_agent(self, description, name='', write=True, **kwargs):
        if not description:
            return json.dumps({
                "status": "error",
                "message": "Please provide a description of what the agent should do."
            })

        if not name:
            name = self._generate_name(description)

        name = self._sanitize_name(name)
        class_name = f"{name}Agent"
        snake = self._to_snake_case(name)
        file_name = f"{snake}_agent.py"
        file_path = self.agents_dir / file_name

        if write and file_path.exists():
            return json.dumps({
                "status": "error",
                "message": f"Agent '{name}' already exists at {file_path}. "
                           f"Delete it first or choose a different name."
            })

        agent_code = self._generate_agent_code(description, name, class_name, **kwargs)

        if not write:
            return json.dumps({
                "status": "ok",
                "action": "preview",
                "filename": file_name,
                "class_name": class_name,
                "display_name": name,
                "lines": len(agent_code.split('\n')),
                "code": agent_code,
                "message": f"Preview of {file_name} — use action='create' to write it."
            })

        try:
            file_path.write_text(agent_code)
        except Exception as e:
            return json.dumps({"status": "error", "message": f"Failed to write agent file: {e}"})

        hot_load_result = self._hot_load_agent(file_path, class_name)

        result = {
            "status": "success",
            "action": "create",
            "message": f"Created and loaded agent '{name}'",
            "agent_name": name,
            "filename": file_name,
            "file_path": str(file_path),
            "lines": len(agent_code.split('\n')),
            "hot_loaded": hot_load_result.get("success", False),
            "description": description[:200],
            "hint": (
                f"Agent saved to agents/{file_name} — it will auto-load on next request. "
                f"Edit the perform() method to customize the logic. "
                f"To submit to RAR, re-run with action='submit'."
            ),
        }

        if hot_load_result.get("installed_deps"):
            result["installed_dependencies"] = hot_load_result["installed_deps"]
        if not hot_load_result.get("success"):
            result["hot_load_error"] = hot_load_result.get("error")
            if hot_load_result.get("hint"):
                result["hot_load_hint"] = hot_load_result["hint"]

        return json.dumps(result)

    # ── Swarm creation ────────────────────────────────────────────────────

    def _create_swarm(self, description, swarm_name='', write=True, **kwargs):
        if not description:
            return json.dumps({
                "status": "error",
                "message": "Please provide a description of what the swarm should do."
            })

        if not swarm_name:
            swarm_name = self._generate_name(description)
        swarm_name = self._sanitize_name(swarm_name)

        agents_in_swarm = kwargs.get('agents_in_swarm', '')
        if agents_in_swarm:
            sub_roles = [s.strip() for s in agents_in_swarm.split(",") if s.strip()]
        else:
            sub_roles = ["researcher", "processor", "formatter"]

        category = kwargs.get('category', 'pipeline')
        namespace = (kwargs.get('namespace', '') or 'rapp').lstrip('@')
        env_list = [e.strip() for e in (kwargs.get('requires_env', '') or '').split(",") if e.strip()]
        tags = self._generate_tags(description) + ["swarm"]

        generated_files = []

        for role in sub_roles:
            sub_name = self._sanitize_name(role)
            sub_snake = self._to_snake_case(swarm_name) + "_" + self._to_snake_case(sub_name)
            sub_class = f"{sub_name}Agent"
            sub_filename = f"{sub_snake}_agent.py"
            sub_desc = f"{sub_name} sub-agent for the {swarm_name} swarm."

            perform_body = self._generate_perform_body(
                f"{role} step for a {description}")

            sub_code = self.SWARM_SUB_TEMPLATE.format(
                description=sub_desc,
                swarm_name=swarm_name,
                role=role.lower(),
                date=datetime.now().strftime("%Y-%m-%d %H:%M"),
                namespace=namespace,
                snake_name=sub_snake,
                agent_name=sub_name,
                agent_description=sub_desc.replace('"', '\\"'),
                author=namespace,
                class_name=sub_class,
                category=category,
                tags_json=json.dumps([category, "swarm-member", self._to_snake_case(role)]),
                env_json=json.dumps(env_list),
                perform_body=perform_body,
                extra_imports=self._generate_extra_imports(sub_desc),
            )

            if write:
                dest = self.agents_dir / sub_filename
                try:
                    dest.write_text(sub_code)
                except Exception as e:
                    return json.dumps({"status": "error",
                                       "message": f"Failed to write {sub_filename}: {e}"})

            generated_files.append({
                "filename": sub_filename,
                "class": sub_class,
                "role": role,
                "snake": sub_snake,
            })

        orch_snake = self._to_snake_case(swarm_name)
        orch_filename = f"{orch_snake}_agent.py"
        orch_class = f"{swarm_name}Agent"
        safe_desc = description.replace('"', '\\"').replace('\n', ' ')[:200]

        sub_imports = "\n".join(
            f"from agents.{f['snake']}_agent import {f['class']}"
            for f in generated_files
        )
        agent_map = ", ".join(
            f'"{self._to_snake_case(f["role"])}": {f["class"]}'
            for f in generated_files
        )
        agent_names = [self._to_snake_case(f["role"]) for f in generated_files]
        sub_list_str = "\n".join(f"  - {f['class']} ({f['role']})" for f in generated_files)

        orch_code = self.SWARM_ORCH_TEMPLATE.format(
            description=description,
            swarm_name=swarm_name,
            sub_agent_list=sub_list_str,
            date=datetime.now().strftime("%Y-%m-%d %H:%M"),
            namespace=namespace,
            snake_name=orch_snake,
            agent_description=safe_desc,
            author=namespace,
            class_name=orch_class,
            category=category,
            tags_json=json.dumps(tags),
            sub_agent_imports=sub_imports,
            agent_map=agent_map,
            agent_names_json=json.dumps(agent_names),
            pipeline_json=json.dumps(agent_names),
        )

        if write:
            dest = self.agents_dir / orch_filename
            try:
                dest.write_text(orch_code)
            except Exception as e:
                return json.dumps({"status": "error",
                                   "message": f"Failed to write {orch_filename}: {e}"})

        generated_files.append({
            "filename": orch_filename,
            "class": orch_class,
            "role": "orchestrator",
            "is_orchestrator": True,
        })

        all_filenames = [f["filename"] for f in generated_files]

        result = {
            "status": "success",
            "action": "swarm" if write else "preview",
            "swarm_name": swarm_name,
            "files_generated": len(generated_files),
            "filenames": all_filenames,
            "sub_agents": sub_roles,
            "orchestrator": orch_filename,
            "message": (
                f"Created {swarm_name} swarm: {len(sub_roles)} sub-agents + 1 orchestrator "
                f"({len(generated_files)} files total). "
            ),
        }

        if write:
            result["message"] += (
                "All written to agents/ — they auto-load on next request. "
                "Use SwarmFactory (action=build) to converge them into a "
                "single shareable singleton file."
            )

            for f in generated_files:
                if not f.get("is_orchestrator"):
                    fpath = self.agents_dir / f["filename"]
                    self._hot_load_agent(fpath, f["class"])
            orch_path = self.agents_dir / orch_filename
            self._hot_load_agent(orch_path, orch_class)
        else:
            result["orchestrator_code"] = orch_code

        return json.dumps(result)

    # ── RAR submission ────────────────────────────────────────────────────

    def _prepare_submit(self, description, name='', **kwargs):
        preview = json.loads(self._create_agent(description, name, write=False, **kwargs))
        if preview.get("status") != "ok":
            return json.dumps(preview)

        code = preview.get("code", "")
        namespace = (kwargs.get('namespace', '') or 'rapp').lstrip('@')
        filename = preview["filename"]
        rar_path = f"agents/@{namespace}/{filename}"

        issue_title = f"[AGENT] @{namespace}/{filename.replace('.py', '')}"

        return json.dumps({
            "status": "ok",
            "action": "submit",
            "filename": filename,
            "namespace": f"@{namespace}",
            "rar_path": rar_path,
            "issue_title": issue_title,
            "code": code,
            "message": (
                f"Agent ready for RAR submission.\n\n"
                f"Option 1 — GitHub Issue:\n"
                f"  Open https://github.com/kody-w/RAR/issues/new\n"
                f"  Title: {issue_title}\n"
                f"  Body: paste the agent code as a Python code block.\n\n"
                f"Option 2 — Pull Request:\n"
                f"  Add the file to {rar_path} and open a PR.\n\n"
                f"The registry CI validates the manifest and runs security checks."
            ),
        })

    # ── Name generation ───────────────────────────────────────────────────

    def _generate_name(self, description):
        try:
            result = subprocess.run(
                ['copilot', '--message',
                 f'Generate a short 1-2 word CamelCase name for an agent that: '
                 f'{description[:200]}. Reply with ONLY the name, nothing else.'],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0 and result.stdout.strip():
                name = result.stdout.strip().split('\n')[0]
                name = re.sub(r'[^a-zA-Z]', '', name)
                if name and len(name) <= 30:
                    return name
        except Exception:
            pass

        words = description.lower().split()
        keywords = [w for w in words if len(w) > 3 and w not in
                    {'that', 'this', 'with', 'from', 'agent', 'create', 'make',
                     'want', 'should', 'would', 'could', 'learn', 'teach',
                     'build', 'about', 'which', 'their', 'your', 'they'}]

        if keywords:
            return ''.join(w.capitalize() for w in keywords[:2])
        return 'Custom'

    def _sanitize_name(self, name):
        name = re.sub(r'[^a-zA-Z0-9]', '', name)
        if name and not name[0].isalpha():
            name = 'Agent' + name
        if name:
            name = name[0].upper() + name[1:]
        return name or 'Custom'

    def _to_snake_case(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    # ── Code generation ───────────────────────────────────────────────────

    def _generate_agent_code(self, description, name, class_name, **kwargs):
        perform_body = self._generate_perform_body(description)
        extra_params = self._generate_extra_params(description)
        extra_imports = self._generate_extra_imports(description)
        safe_desc = description.replace('"', '\\"').replace('\n', ' ')[:200]
        tags = self._generate_tags(description)
        snake = self._to_snake_case(name)

        category = kwargs.get('category', 'general')
        namespace = (kwargs.get('namespace', '') or 'rapp').lstrip('@')
        env_list = [e.strip() for e in (kwargs.get('requires_env', '') or '').split(",") if e.strip()]

        extra_params_inferred = self._infer_example_params(description)
        example_args = {}
        if extra_params_inferred:
            for p in extra_params_inferred[:2]:
                example_args[p] = f"example {p}"
        else:
            example_args["query"] = "example query"

        # rpp trace (github.com/kody-w/rapp-personpower): conservative run-rating.
        # Manual baseline = 180s to do the task by hand + 120s per input the
        # agent gathers/uses; engine = ~30s per run. Rounded down, floor 1.
        _manual_s = 180 + 120 * len(extra_params_inferred)
        estimated_rpp = max(1, _manual_s // 30)
        rpp_basis = ("~%ds manual baseline (180s task + 120s/input x %d) vs ~30s per run; "
                     "preview stat, rounded down") % (_manual_s, len(extra_params_inferred))

        return self.AGENT_TEMPLATE.format(
            description=description,
            date=datetime.now().strftime("%Y-%m-%d %H:%M"),
            class_name=class_name,
            agent_name=name,
            agent_description=safe_desc,
            extra_imports=extra_imports,
            extra_params=extra_params,
            perform_body=perform_body,
            tags_json=json.dumps(tags),
            estimated_rpp=estimated_rpp,
            rpp_basis=rpp_basis,
            category=category,
            namespace=namespace,
            snake_name=snake,
            author=namespace,
            env_json=json.dumps(env_list),
            example_args_json=json.dumps(example_args),
        )

    def _infer_example_params(self, description):
        params = []
        desc_lower = description.lower()
        if any(w in desc_lower for w in ['url', 'link', 'website', 'page']):
            params.append('url')
        if any(w in desc_lower for w in ['file', 'read', 'write', 'path']):
            params.append('path')
        if any(w in desc_lower for w in ['search', 'find', 'look']):
            params.append('query')
        return params

    def _generate_tags(self, description):
        tags = []
        desc_lower = description.lower()
        tag_map = {
            'weather': 'weather', 'api': 'api', 'web': 'web',
            'file': 'filesystem', 'data': 'data', 'search': 'search',
            'email': 'email', 'database': 'database', 'sql': 'database',
            'news': 'news', 'schedule': 'scheduling', 'voice': 'voice',
            'stock': 'finance', 'price': 'finance', 'video': 'media',
            'image': 'media', 'summarize': 'nlp', 'translate': 'nlp',
            'monitor': 'monitoring', 'track': 'tracking', 'slack': 'messaging',
        }
        for keyword, tag in tag_map.items():
            if keyword in desc_lower and tag not in tags:
                tags.append(tag)
        return tags or ['custom']

    def _generate_extra_params(self, description):
        extra = ""
        desc_lower = description.lower()

        if any(w in desc_lower for w in ['file', 'read', 'write', 'path']):
            extra += """,
                    "path": {
                        "type": "string",
                        "description": "File or directory path."
                    }"""

        if any(w in desc_lower for w in ['url', 'http', 'web', 'fetch']):
            extra += """,
                    "url": {
                        "type": "string",
                        "description": "URL to access."
                    }"""

        if any(w in desc_lower for w in ['number', 'count', 'amount', 'limit']):
            extra += """,
                    "count": {
                        "type": "integer",
                        "description": "Number or count value."
                    }"""

        return extra

    def _generate_perform_body(self, description):
        try:
            prompt = (
                f"Generate ONLY the Python code for the body of a perform() method "
                f"for an agent that: {description}\n\n"
                f"Rules:\n"
                f"- Return a JSON string with status and result\n"
                f"- Use kwargs.get() to access parameters\n"
                f"- Keep it simple and functional\n"
                f"- Do NOT include the method signature, just the body\n"
                f"- Indent with 8 spaces\n\n"
                f"Example format:\n"
                f"        # Process the query\n"
                f"        result = \"processed: \" + query\n"
                f'        return json.dumps({{"status": "success", "result": result}})'
            )

            result = subprocess.run(
                ['copilot', '--message', prompt],
                capture_output=True, text=True, timeout=30
            )

            if result.returncode == 0 and result.stdout.strip():
                body = result.stdout.strip()
                if '```python' in body:
                    body = body.split('```python')[1].split('```')[0]
                elif '```' in body:
                    body = body.split('```')[1].split('```')[0]

                lines = body.strip().split('\n')
                indented = '\n'.join(
                    '        ' + line.lstrip() if line.strip() else ''
                    for line in lines
                )
                if indented.strip():
                    return indented
        except Exception:
            pass

        return '''        # Default implementation - customize this
        if not query:
            return json.dumps({
                "status": "error",
                "message": "No query provided"
            })

        return json.dumps({
            "status": "success",
            "query": query,
            "result": f"Processed by {self.name}: {query}"
        })'''

    def _generate_extra_imports(self, description):
        imports = []
        desc_lower = description.lower()

        import_map = {
            ('http', 'api', 'fetch', 'url', 'web', 'request'): 'import urllib.request',
            ('html', 'scrape', 'parse html', 'beautifulsoup'): 'from bs4 import BeautifulSoup',
            ('csv', 'spreadsheet'): 'import csv',
            ('xml',): 'import xml.etree.ElementTree as ET',
            ('datetime', 'date', 'time', 'timestamp'): 'from datetime import datetime',
            ('regex', 'pattern', 'match'): 'import re',
            ('file', 'read', 'write', 'path'): 'from pathlib import Path',
            ('base64', 'encode', 'decode'): 'import base64',
            ('hash', 'md5', 'sha'): 'import hashlib',
            ('random', 'shuffle', 'choice'): 'import random',
            ('sleep', 'wait', 'delay'): 'import time',
            ('environment', 'env var'): 'import os',
        }

        for keywords, import_stmt in import_map.items():
            if any(kw in desc_lower for kw in keywords):
                if import_stmt not in imports:
                    imports.append(import_stmt)

        if imports:
            return '\n'.join(imports) + '\n'
        return ''

    # ── Hot-loading ───────────────────────────────────────────────────────

    def _hot_load_agent(self, file_path, class_name):
        try:
            import importlib.util

            code = file_path.read_text()
            missing_deps = self._detect_missing_imports(code)

            if missing_deps:
                install_result = self._install_dependencies(missing_deps)
                if not install_result['success']:
                    return {
                        "success": False,
                        "error": f"Failed to install dependencies: {install_result['error']}",
                        "missing_deps": missing_deps
                    }

            spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            agent_class = getattr(module, class_name, None)
            if agent_class is None:
                return {"success": False, "error": "Class not found in module"}

            import sys
            module_name = f"agents.{file_path.stem}"
            sys.modules[module_name] = module

            result = {"success": True, "class": class_name}
            if missing_deps:
                result["installed_deps"] = missing_deps
            return result

        except ModuleNotFoundError as e:
            missing = str(e).split("'")[1] if "'" in str(e) else str(e)
            return {
                "success": False,
                "error": f"Missing module: {missing}",
                "hint": f"Try: pip install {missing}"
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def _detect_missing_imports(self, code):
        import importlib

        missing = []
        import_pattern = r'^(?:from\s+(\w+)|import\s+(\w+))'
        for line in code.split('\n'):
            line = line.strip()
            match = re.match(import_pattern, line)
            if match:
                module_name = match.group(1) or match.group(2)
                if module_name in self._stdlib_modules():
                    continue
                if module_name in ('agents', 'basic_agent'):
                    continue
                try:
                    importlib.import_module(module_name)
                except ImportError:
                    pkg_name = self._module_to_package(module_name)
                    if pkg_name not in missing:
                        missing.append(pkg_name)
        return missing

    def _module_to_package(self, module_name):
        mappings = {
            'cv2': 'opencv-python',
            'PIL': 'Pillow',
            'sklearn': 'scikit-learn',
            'yaml': 'pyyaml',
            'bs4': 'beautifulsoup4',
            'dotenv': 'python-dotenv',
            'jwt': 'pyjwt',
            'serial': 'pyserial',
            'usb': 'pyusb',
            'Crypto': 'pycryptodome',
        }
        return mappings.get(module_name, module_name)

    def _stdlib_modules(self):
        return {
            'abc', 'argparse', 'ast', 'asyncio', 'base64', 'collections',
            'contextlib', 'copy', 'csv', 'datetime', 'decimal', 'difflib',
            'email', 'enum', 'functools', 'glob', 'gzip', 'hashlib', 'heapq',
            'html', 'http', 'importlib', 'inspect', 'io', 'itertools', 'json',
            'logging', 'math', 'mimetypes', 'multiprocessing', 'operator', 'os',
            'pathlib', 'pickle', 'platform', 'pprint', 'queue', 'random', 're',
            'shutil', 'signal', 'socket', 'sqlite3', 'ssl', 'statistics',
            'string', 'struct', 'subprocess', 'sys', 'tempfile', 'textwrap',
            'threading', 'time', 'traceback', 'types', 'typing', 'unittest',
            'urllib', 'uuid', 'warnings', 'weakref', 'xml', 'zipfile', 'zlib'
        }

    def _install_dependencies(self, packages):
        if not packages:
            return {"success": True}
        try:
            import sys
            for pkg in packages:
                result = subprocess.run(
                    [sys.executable, '-m', 'pip', 'install', '--quiet', pkg],
                    capture_output=True, text=True, timeout=60
                )
                if result.returncode != 0:
                    return {"success": False,
                            "error": f"pip install {pkg} failed: {result.stderr}"}
            return {"success": True, "installed": packages}
        except subprocess.TimeoutExpired:
            return {"success": False, "error": "pip install timed out"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    # ── List / Delete ─────────────────────────────────────────────────────

    def _list_generated_agents(self):
        agents = []
        core = {'basic_agent.py', 'save_memory_agent.py', 'recall_memory_agent.py',
                'learn_new_agent.py', 'swarm_factory_agent.py'}
        for f in sorted(self.agents_dir.glob('*_agent.py')):
            if f.name in core:
                continue
            content = f.read_text()
            is_generated = 'Auto-generated by LearnNewAgent' in content
            agents.append({
                "name": f.stem.replace('_agent', ''),
                "file": f.name,
                "auto_generated": is_generated
            })
        return json.dumps({
            "status": "success",
            "agents": agents,
            "count": len(agents)
        })

    def _delete_agent(self, name):
        if not name:
            return json.dumps({
                "status": "error",
                "message": "Please provide the agent name to delete."
            })

        snake_name = self._to_snake_case(self._sanitize_name(name))
        file_path = self.agents_dir / f"{snake_name}_agent.py"

        if not file_path.exists():
            for f in self.agents_dir.glob('*_agent.py'):
                if name.lower() in f.name.lower():
                    file_path = f
                    break

        if not file_path.exists():
            return json.dumps({
                "status": "error",
                "message": f"Agent '{name}' not found."
            })

        core = {'basic_agent.py', 'save_memory_agent.py', 'recall_memory_agent.py',
                'learn_new_agent.py', 'swarm_factory_agent.py'}
        if file_path.name in core:
            return json.dumps({
                "status": "error",
                "message": "Cannot delete core agents."
            })

        try:
            file_path.unlink()
            return json.dumps({
                "status": "success",
                "message": f"Deleted agent '{name}'",
                "file": str(file_path)
            })
        except Exception as e:
            return json.dumps({"status": "error", "message": str(e)})


if __name__ == "__main__":
    a = LearnNewAgent()
    print(a.perform(action="preview",
                    description="An agent that tracks daily habits and streaks"))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
