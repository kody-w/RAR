---
name: "rar-rapp-learn-new"
description: "Creates new RAPP agents or swarms from natural-language descriptions. By default it ADAPTS a real published agent from the public microsoft/aibast-agents-library (sha256-verified) instead of generating code from scratch. Actions: 'create' adapts a template into a single agent, 'templates' searches the published templates, 'swarm' creates a multi-agent pipeline, 'list' shows generated agents, 'delete' removes one, 'preview' dry-runs generation, 'submit' prepares a RAR registry submission. Call when the user wants to teach the brainstem something new, create a custom agent, or build an agent swarm."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/learn_new", "rar_sha256": "9104535d15333d9a30543d94483df7bad958a61c4b4c00e492fc627fe3b21741", "source_kind": "rar-agent", "source_commit": "b4ba983328bbb00340c62a83332318dc0ffc22aa", "version": "3.0.1", "author": "RAPP", "tags": ["meta", "generator", "scaffolding", "learn", "swarm", "templates", "aibast"]}
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

Describe what you want the agent to do and LearnNewAgent adapts a real,
published agent into it — agents building agents from proven parts rather
than from a blank page. Generated agents follow the Single File Agent
pattern: one file containing documentation, metadata contract, and
deterministic code.

v3 — TEMPLATE-FIRST. The default path no longer invents an agent from
built-in strings. It:

  1. discovers published agents from the PUBLIC, MIT-licensed
     microsoft/aibast-agents-library registry (cached outside this repo),
  2. selects the best match for your description (and tells you why),
  3. fetches the chosen file and VERIFIES its sha256 against the registry —
     on mismatch it REFUSES; it never repairs and never falls back to the
     unverified bytes,
  4. mutates the verified template in memory (rename, remanifest, retarget)
     while preserving its structure, its MIT attribution, and a machine-
     readable provenance record.

Scratch generation from the built-in string templates is still available,
but it is now an explicit choice (source='scratch') and the honest fallback
when the network is unavailable or nothing matches well. Every response
says which path produced the output via the "generator" field.

No template source is ever written into this repository: templates are
fetched at runtime, mutated in memory, and written to the caller's output
directory. The registry cache lives outside the repo (see
RAPP_LEARN_CACHE_DIR, default ~/.rapp-learn-new).

Actions:
  create    — Adapt a published template into a new agent (default)
  templates — Search/list the published templates available to adapt
  swarm     — Generate a multi-agent pipeline + orchestrator
  list      — List generated agents in agents/
  delete    — Remove a generated agent
  preview   — Show what would be generated without writing
  submit    — Prepare a RAR-compatible submission

Env:
  RAPP_LEARN_CACHE_DIR  — where the registry cache lives (default ~/.rapp-learn-new)
  RAPP_LEARN_OFFLINE=1  — never touch the network (cache-only / scratch)
  RAPP_LEARN_NO_LLM=1   — never shell out to `copilot` for naming/body generation

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
        "templates",
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
    "output_dir": {
      "description": "Directory to write the generated agent into. Defaults to this brainstem's agents/ directory.",
      "type": "string"
    },
    "query": {
      "description": "Natural language query that may contain the agent description.",
      "type": "string"
    },
    "refresh": {
      "description": "Force a refetch of the published template registry, ignoring the cache TTL.",
      "type": "boolean"
    },
    "requires_env": {
      "description": "Comma-separated env vars the agent needs (e.g. 'API_KEY,WEBHOOK_URL').",
      "type": "string"
    },
    "source": {
      "description": "Where the new agent comes from. 'template' (default) adapts a verified published agent; 'scratch' uses the built-in string templates. Scratch is also the automatic fallback when offline or when nothing matches well.",
      "enum": [
        "template",
        "scratch"
      ],
      "type": "string"
    },
    "template": {
      "description": "Explicit published template to adapt (e.g. 'account-intelligence' or '@aibast-agents-library/account-intelligence'). Overrides automatic selection. Use action='templates' to see what exists.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `learn_new_agent.py` and embedded as the fenced Python below (sha256 9104535d15333d9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `learn_new_agent.py` first:

```bash
python3 learn_new_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 learn_new_agent.py   # or on stdin
python3 learn_new_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
LearnNewAgent - Meta-agent that creates new agents and swarms from natural language.

Describe what you want the agent to do and LearnNewAgent adapts a real,
published agent into it — agents building agents from proven parts rather
than from a blank page. Generated agents follow the Single File Agent
pattern: one file containing documentation, metadata contract, and
deterministic code.

v3 — TEMPLATE-FIRST. The default path no longer invents an agent from
built-in strings. It:

  1. discovers published agents from the PUBLIC, MIT-licensed
     microsoft/aibast-agents-library registry (cached outside this repo),
  2. selects the best match for your description (and tells you why),
  3. fetches the chosen file and VERIFIES its sha256 against the registry —
     on mismatch it REFUSES; it never repairs and never falls back to the
     unverified bytes,
  4. mutates the verified template in memory (rename, remanifest, retarget)
     while preserving its structure, its MIT attribution, and a machine-
     readable provenance record.

Scratch generation from the built-in string templates is still available,
but it is now an explicit choice (source='scratch') and the honest fallback
when the network is unavailable or nothing matches well. Every response
says which path produced the output via the "generator" field.

No template source is ever written into this repository: templates are
fetched at runtime, mutated in memory, and written to the caller's output
directory. The registry cache lives outside the repo (see
RAPP_LEARN_CACHE_DIR, default ~/.rapp-learn-new).

Actions:
  create    — Adapt a published template into a new agent (default)
  templates — Search/list the published templates available to adapt
  swarm     — Generate a multi-agent pipeline + orchestrator
  list      — List generated agents in agents/
  delete    — Remove a generated agent
  preview   — Show what would be generated without writing
  submit    — Prepare a RAR-compatible submission

Env:
  RAPP_LEARN_CACHE_DIR  — where the registry cache lives (default ~/.rapp-learn-new)
  RAPP_LEARN_OFFLINE=1  — never touch the network (cache-only / scratch)
  RAPP_LEARN_NO_LLM=1   — never shell out to `copilot` for naming/body generation
"""

import ast
import hashlib
import json
import os
import re
import subprocess
import tempfile
import urllib.error
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/learn_new",
    "version": "3.0.1",
    "display_name": "LearnNew",
    "description": "Creates new single-file RAPP agents by adapting a real published agent from the public microsoft/aibast-agents-library (sha256-verified, MIT-attributed, mutated not regenerated); built-in scratch templates remain as an explicit fallback.",
    "author": "RAPP",
    "tags": ["meta", "generator", "scaffolding", "learn", "swarm", "templates", "aibast"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {"args": {"action": "create", "description": "An agent that researches an enterprise account before a sales call"}},
}


# ── Published template source ────────────────────────────────────────────
# PUBLIC + MIT licensed. Fetched at runtime; never vendored into this repo.
TEMPLATE_REPO = "microsoft/aibast-agents-library"
TEMPLATE_BRANCH = "main"
TEMPLATE_RAW_BASE = "https://raw.githubusercontent.com/%s/%s/" % (TEMPLATE_REPO, TEMPLATE_BRANCH)
TEMPLATE_REGISTRY_URL = TEMPLATE_RAW_BASE + "registry.json"
TEMPLATE_REPO_URL = "https://github.com/%s" % TEMPLATE_REPO
TEMPLATE_LICENSE = "MIT License, Copyright (c) Microsoft (see %s/blob/%s/LICENSE)" % (
    TEMPLATE_REPO_URL, TEMPLATE_BRANCH)

# A cached registry older than this is refetched; if the refetch fails the
# cache is still usable but is reported as STALE, never as current.
REGISTRY_TTL_SECONDS = 24 * 60 * 60
NETWORK_TIMEOUT = 20

# Minimum weighted match score before a template is considered a real match.
# Below this we say "no confident match" instead of forcing a bad one.
MIN_MATCH_SCORE = 6.0

_STOPWORDS = {
    'a', 'an', 'the', 'and', 'or', 'of', 'for', 'to', 'in', 'on', 'with', 'that',
    'this', 'from', 'agent', 'agents', 'create', 'creates', 'make', 'makes', 'want',
    'wants', 'should', 'would', 'could', 'learn', 'teach', 'build', 'builds', 'about',
    'which', 'their', 'your', 'they', 'it', 'is', 'are', 'be', 'can', 'need', 'needs',
    'me', 'my', 'i', 'new', 'thing', 'something', 'help', 'helps', 'using', 'use',
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
                "By default it ADAPTS a real published agent from the public "
                "microsoft/aibast-agents-library (sha256-verified) instead of generating "
                "code from scratch. Actions: 'create' adapts a template into a single agent, "
                "'templates' searches the published templates, 'swarm' creates a multi-agent "
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
                        "enum": ["create", "templates", "swarm", "list", "delete",
                                 "preview", "submit"]
                    },
                    "template": {
                        "type": "string",
                        "description": (
                            "Explicit published template to adapt (e.g. 'account-intelligence' "
                            "or '@aibast-agents-library/account-intelligence'). Overrides "
                            "automatic selection. Use action='templates' to see what exists."
                        )
                    },
                    "source": {
                        "type": "string",
                        "enum": ["template", "scratch"],
                        "description": (
                            "Where the new agent comes from. 'template' (default) adapts a "
                            "verified published agent; 'scratch' uses the built-in string "
                            "templates. Scratch is also the automatic fallback when offline "
                            "or when nothing matches well."
                        )
                    },
                    "refresh": {
                        "type": "boolean",
                        "description": "Force a refetch of the published template registry, ignoring the cache TTL."
                    },
                    "output_dir": {
                        "type": "string",
                        "description": "Directory to write the generated agent into. Defaults to this brainstem's agents/ directory."
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
            return self._list_generated_agents(kwargs.get('output_dir'))
        elif action in ('templates', 'list_templates'):
            return self._list_templates(description, **kwargs)
        elif action == 'delete':
            return self._delete_agent(name or description, kwargs.get('output_dir'))
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

        source_mode = (kwargs.get('source') or 'template').strip().lower()
        template_pick = (kwargs.get('template') or '').strip()
        if template_pick:
            source_mode = 'template'

        provenance = None
        template_report = None
        generator = "builtin-scratch"
        fallback_reason = None
        agent_code = None

        if source_mode != 'scratch':
            tpl = self._build_from_template(description, template_pick, **kwargs)
            template_report = tpl.get("report")

            if tpl.get("ok"):
                entry = tpl["entry"]
                fetched = tpl["fetched"]
                if not name:
                    name = self._name_from_template(entry, description)
                name = self._sanitize_name(name)
                class_name = f"{name}Agent"
                agent_code, provenance = self._mutate_template(
                    fetched["code"], entry, fetched, description, name, class_name, **kwargs)
                generator = "aibast-template-mutation"

            elif tpl.get("reason") == "integrity_mismatch":
                # Refuse-never-repair. Do NOT fall back to the unverified bytes.
                return json.dumps({
                    "status": "refused",
                    "action": "create",
                    "generator": "none",
                    "reason": "integrity_mismatch",
                    "message": (
                        "REFUSED: the fetched template did not match its published sha256. "
                        "Nothing was generated, nothing was written, and the bytes were "
                        "discarded. This estate refuses; it does not repair. Re-run with "
                        "refresh=true to pull a fresh registry, or source='scratch' to "
                        "generate without a template."
                    ),
                    "template": tpl.get("integrity"),
                }, indent=2)

            elif tpl.get("reason") == "unknown_template":
                return json.dumps({
                    "status": "error",
                    "action": "create",
                    "generator": "none",
                    "reason": "unknown_template",
                    "message": (
                        f"No published template matches template='{template_pick}'. "
                        f"Nothing was generated. Use action='templates' to list what exists, "
                        f"or drop the 'template' argument to let selection choose."
                    ),
                    "did_you_mean": tpl.get("candidates", []),
                    "registry": tpl.get("report", {}).get("registry"),
                }, indent=2)

            else:
                fallback_reason = tpl.get("reason")

        if agent_code is None:
            # Scratch path: explicit choice, or the honest fallback.
            if not name:
                name = self._generate_name(description)
            name = self._sanitize_name(name)
            class_name = f"{name}Agent"
            agent_code = self._generate_agent_code(description, name, class_name, **kwargs)
            generator = "builtin-scratch"

        snake = self._to_snake_case(name)
        file_name = f"{snake}_agent.py"
        out_dir = self._resolve_output_dir(kwargs.get('output_dir'))
        file_path = out_dir / file_name

        base = {
            "generator": generator,
            "generator_description": (
                "Mutated a sha256-verified published agent from %s" % TEMPLATE_REPO
                if generator == "aibast-template-mutation"
                else "Generated from LearnNewAgent's built-in string templates (no published template used)"
            ),
        }
        if provenance:
            base["provenance"] = provenance
        if template_report:
            base["template_selection"] = template_report
        if fallback_reason:
            base["fallback_reason"] = fallback_reason
            base["fallback_message"] = self._fallback_message(fallback_reason, template_report)

        if write and file_path.exists():
            out = dict(base)
            out.update({
                "status": "error",
                "message": f"Agent '{name}' already exists at {file_path}. "
                           f"Delete it first or choose a different name.",
            })
            return json.dumps(out, indent=2)

        if not write:
            out = dict(base)
            out.update({
                "status": "ok",
                "action": "preview",
                "filename": file_name,
                "class_name": class_name,
                "display_name": name,
                "lines": len(agent_code.split('\n')),
                "code": agent_code,
                "message": f"Preview of {file_name} via {generator} — use action='create' to write it.",
            })
            return json.dumps(out, indent=2)

        try:
            out_dir.mkdir(parents=True, exist_ok=True)
            file_path.write_text(agent_code)
        except Exception as e:
            out = dict(base)
            out.update({"status": "error", "message": f"Failed to write agent file: {e}"})
            return json.dumps(out, indent=2)

        hot_load_result = self._hot_load_agent(file_path, class_name)

        result = dict(base)
        result.update({
            "status": "success",
            "action": "create",
            "message": f"Created agent '{name}' via {generator}",
            "agent_name": name,
            "filename": file_name,
            "file_path": str(file_path),
            "lines": len(agent_code.split('\n')),
            "hot_loaded": hot_load_result.get("success", False),
            "description": description[:200],
            "hint": (
                f"Agent saved to {file_path} — it will auto-load on next request. "
                + ("Its behaviour is inherited from the verified template; edit the "
                   "operations listed in the class docstring to retarget the logic. "
                   if generator == "aibast-template-mutation"
                   else "Edit the perform() method to customize the logic. ")
                + "To submit to RAR, re-run with action='submit'."
            ),
        })

        if hot_load_result.get("installed_deps"):
            result["installed_dependencies"] = hot_load_result["installed_deps"]
        if not hot_load_result.get("success"):
            result["hot_load_error"] = hot_load_result.get("error")
            if hot_load_result.get("hint"):
                result["hot_load_hint"] = hot_load_result["hint"]

        return json.dumps(result, indent=2)

    def _resolve_output_dir(self, output_dir):
        if output_dir:
            return Path(output_dir).expanduser()
        return self.agents_dir

    def _fallback_message(self, reason, report):
        reg = (report or {}).get("registry", {})
        if reason == "offline":
            return (
                "Could not reach the published template registry and no cached copy is "
                "available, so nothing could be adapted. Fell back to built-in scratch "
                "generation. Network error: %s" % reg.get("network_error", "unknown")
            )
        if reason == "no_match":
            return (
                "No published template matched the description with enough confidence "
                "(best score %s < threshold %s), so no template was forced. Fell back to "
                "built-in scratch generation. Pass template='<name>' to override, or "
                "action='templates' to browse." % (
                    (report or {}).get("best_score"), MIN_MATCH_SCORE)
            )
        if reason == "fetch_failed":
            return (
                "The template was selected but could not be downloaded (%s). Nothing "
                "unverified was used. Fell back to built-in scratch generation."
                % (report or {}).get("fetch_error", "unknown error")
            )
        if reason == "no_expected_hash":
            return ("The selected registry entry carries no published sha256, so it could "
                    "not be verified and was not used. Fell back to built-in scratch generation.")
        return "Fell back to built-in scratch generation (%s)." % reason

    # ── Published-template discovery ──────────────────────────────────────

    def _cache_dir(self):
        """Registry cache location. Always OUTSIDE any agent repo."""
        env_dir = os.environ.get("RAPP_LEARN_CACHE_DIR")
        candidate = Path(env_dir).expanduser() if env_dir else (Path.home() / ".rapp-learn-new")
        try:
            # Never let the cache land inside the agents tree of a checkout.
            if str(candidate.resolve()).startswith(str(self.agents_dir.resolve())):
                candidate = Path(tempfile.gettempdir()) / "rapp-learn-new"
        except Exception:
            pass
        try:
            candidate.mkdir(parents=True, exist_ok=True)
        except Exception:
            candidate = Path(tempfile.gettempdir()) / "rapp-learn-new"
            candidate.mkdir(parents=True, exist_ok=True)
        return candidate

    def _http_get(self, url, extra_headers=None):
        headers = {"User-Agent": "rapp-learn-new/3.0 (+%s)" % TEMPLATE_REPO_URL}
        if extra_headers:
            headers.update({k: v for k, v in extra_headers.items() if v})
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=NETWORK_TIMEOUT) as resp:
            return resp.read(), dict(resp.headers)

    def _load_registry(self, refresh=False):
        """
        Returns (registry_or_None, meta).

        meta["source"] is one of:
          network            — freshly downloaded
          network-unchanged  — server said 304; cache re-validated as CURRENT
          cache              — cache still within TTL, network not contacted
          cache-STALE        — network unreachable; cache served but flagged STALE
          none               — no network and no cache

        "I couldn't reach it" (cache-STALE / none, with network_error) and
        "nothing changed" (network-unchanged) are deliberately distinct.
        """
        cdir = self._cache_dir()
        cache_f = cdir / "aibast-registry.json"
        meta_f = cdir / "aibast-registry.meta.json"

        cached_meta = {}
        if meta_f.exists():
            try:
                cached_meta = json.loads(meta_f.read_text())
            except Exception:
                cached_meta = {}

        def _age():
            ts = cached_meta.get("fetched_at_epoch")
            if not ts:
                return None
            return max(0, int(self._now_epoch() - ts))

        def _read_cache():
            try:
                return json.loads(cache_f.read_text())
            except Exception:
                return None

        age = _age()
        offline = os.environ.get("RAPP_LEARN_OFFLINE") == "1"

        if cache_f.exists() and not refresh and age is not None and age < REGISTRY_TTL_SECONDS:
            reg = _read_cache()
            if reg is not None:
                return reg, {
                    "source": "cache",
                    "stale": False,
                    "cache_path": str(cache_f),
                    "fetched_at": cached_meta.get("fetched_at"),
                    "age_seconds": age,
                    "url": TEMPLATE_REGISTRY_URL,
                }

        if offline:
            reg = _read_cache() if cache_f.exists() else None
            if reg is not None:
                return reg, {
                    "source": "cache-STALE",
                    "stale": True,
                    "cache_path": str(cache_f),
                    "fetched_at": cached_meta.get("fetched_at"),
                    "age_seconds": age,
                    "network_error": "RAPP_LEARN_OFFLINE=1 — network deliberately not contacted",
                    "warning": "Served from cache without contacting the network. Content may be out of date.",
                    "url": TEMPLATE_REGISTRY_URL,
                }
            return None, {
                "source": "none",
                "stale": True,
                "network_error": "RAPP_LEARN_OFFLINE=1 — network deliberately not contacted",
                "cache_path": str(cache_f),
                "url": TEMPLATE_REGISTRY_URL,
            }

        etag = cached_meta.get("etag") if cache_f.exists() else None
        try:
            body, headers = self._http_get(
                TEMPLATE_REGISTRY_URL,
                {"If-None-Match": etag} if etag else None)
            reg = json.loads(body.decode("utf-8"))
            now_iso = self._now_iso()
            cache_f.write_text(json.dumps(reg))
            meta_f.write_text(json.dumps({
                "url": TEMPLATE_REGISTRY_URL,
                "fetched_at": now_iso,
                "fetched_at_epoch": self._now_epoch(),
                "etag": headers.get("ETag"),
                "bytes": len(body),
            }, indent=2))
            return reg, {
                "source": "network",
                "stale": False,
                "cache_path": str(cache_f),
                "fetched_at": now_iso,
                "age_seconds": 0,
                "bytes": len(body),
                "url": TEMPLATE_REGISTRY_URL,
                "registry_generated_at": reg.get("generated_at"),
            }
        except urllib.error.HTTPError as e:
            if e.code == 304 and cache_f.exists():
                reg = _read_cache()
                if reg is not None:
                    now_iso = self._now_iso()
                    cached_meta["fetched_at"] = now_iso
                    cached_meta["fetched_at_epoch"] = self._now_epoch()
                    try:
                        meta_f.write_text(json.dumps(cached_meta, indent=2))
                    except Exception:
                        pass
                    return reg, {
                        "source": "network-unchanged",
                        "stale": False,
                        "cache_path": str(cache_f),
                        "fetched_at": now_iso,
                        "age_seconds": 0,
                        "note": "Registry re-validated against the server: 304 Not Modified — nothing changed upstream.",
                        "url": TEMPLATE_REGISTRY_URL,
                    }
            net_err = "HTTP %s %s" % (e.code, e.reason)
        except Exception as e:
            net_err = "%s: %s" % (type(e).__name__, e)

        reg = _read_cache() if cache_f.exists() else None
        if reg is not None:
            return reg, {
                "source": "cache-STALE",
                "stale": True,
                "cache_path": str(cache_f),
                "fetched_at": cached_meta.get("fetched_at"),
                "age_seconds": age,
                "network_error": net_err,
                "warning": (
                    "Could NOT reach the published registry. Serving a STALE cache "
                    "last fetched %s (%s seconds old). This is not a statement that "
                    "nothing changed upstream." % (cached_meta.get("fetched_at"), age)
                ),
                "url": TEMPLATE_REGISTRY_URL,
            }
        return None, {
            "source": "none",
            "stale": True,
            "network_error": net_err,
            "cache_path": str(cache_f),
            "url": TEMPLATE_REGISTRY_URL,
        }

    def _now_epoch(self):
        return int(datetime.now(timezone.utc).timestamp())

    def _now_iso(self):
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # ── Template selection ────────────────────────────────────────────────

    def _tokens(self, text):
        raw = re.split(r'[^a-z0-9]+', (text or '').lower())
        out = []
        for t in raw:
            if len(t) < 3 or t in _STOPWORDS:
                continue
            if t not in out:
                out.append(t)
        return out

    def _variants(self, token):
        """Progressively shorter forms, longest first (substring matching)."""
        v = [token]
        if token.endswith('ies') and len(token) > 4:
            v.append(token[:-3] + 'y')
        if token.endswith('s') and len(token) > 3:
            v.append(token[:-1])
        if token.endswith('es') and len(token) > 4:
            v.append(token[:-2])
        return v

    def _entry_fields(self, entry):
        sol = entry.get("_solution") or {}
        strong = " ".join([
            str(entry.get("display_name", "")),
            str(entry.get("name", "")),
            str(entry.get("_stack", "")),
            " ".join(entry.get("tags") or []),
        ])
        mid = " ".join([
            str(entry.get("description", "")),
            str(entry.get("category", "")),
            str(entry.get("_stack_vertical", "")),
        ])
        weak = " ".join([
            str(sol.get("executive_summary", "")),
            " ".join(sol.get("capabilities") or []),
            " ".join(sol.get("personas") or []),
            " ".join(sol.get("industries") or []),
            " ".join(sol.get("featured_tools") or []),
            " ".join(str(o) for o in (sol.get("outcomes") or [])),
        ])
        return strong.lower(), mid.lower(), weak.lower()

    def _score_entry(self, entry, tokens):
        strong, mid, weak = self._entry_fields(entry)
        score = 0.0
        hits = []
        for t in tokens:
            # Best tier across all morphological variants — a token scores once,
            # at the strongest field any of its forms appears in.
            best = 0.0
            for v in self._variants(t):
                if v in strong:
                    best = max(best, 3.0)
                elif v in mid:
                    best = max(best, 2.0)
                elif v in weak:
                    best = max(best, 1.0)
            if best:
                score += best
                hits.append(t)
        return score, hits

    def _rank_templates(self, agents, description, limit=5):
        tokens = self._tokens(description)
        scored = []
        for e in agents:
            if not e.get("_file") or not e.get("_sha256"):
                continue
            s, hits = self._score_entry(e, tokens)
            if s > 0:
                scored.append((s, hits, e))
        scored.sort(key=lambda x: (-x[0], x[2].get("name", "")))
        return tokens, scored[:limit]

    def _find_template(self, agents, wanted):
        w = wanted.strip().lower().lstrip('@')
        w_norm = w.replace('_', '-')
        exact, partial = None, []
        for e in agents:
            if not e.get("_file") or not e.get("_sha256"):
                continue
            name = str(e.get("name", "")).lower().lstrip('@')
            slug = name.split('/')[-1]
            stack = str(e.get("_stack", "")).lower().replace('_', '-')
            disp = str(e.get("display_name", "")).lower()
            keys = {name, name.replace('_', '-'), slug, slug.replace('_', '-'), stack, disp}
            if w in keys or w_norm in keys:
                exact = e
                break
            if w_norm and (w_norm in slug or w_norm in stack or w in disp):
                partial.append(e)
        if exact:
            return exact, []
        if len(partial) == 1:
            return partial[0], []
        return None, [self._entry_summary(e) for e in partial[:8]]

    def _entry_summary(self, entry, score=None, hits=None):
        out = {
            "template": entry.get("name"),
            "display_name": entry.get("display_name"),
            "vertical": entry.get("_stack_vertical"),
            "stack": entry.get("_stack"),
            "lines": entry.get("_lines"),
            "kind": entry.get("_catalog_kind"),
            "description": (entry.get("description") or "")[:160],
            "file": entry.get("_file"),
            "sha256": entry.get("_sha256"),
        }
        if score is not None:
            out["match_score"] = round(score, 1)
        if hits:
            out["matched_on"] = hits
        return out

    def _list_templates(self, description='', **kwargs):
        reg, meta = self._load_registry(refresh=bool(kwargs.get('refresh')))
        if reg is None:
            return json.dumps({
                "status": "error",
                "action": "templates",
                "message": "Could not load the published template registry.",
                "registry": meta,
            }, indent=2)

        agents = reg.get("agents") or []
        query = description or kwargs.get('template') or ''
        if query:
            tokens, ranked = self._rank_templates(agents, query, limit=10)
            items = [self._entry_summary(e, s, h) for s, h, e in ranked]
            msg = "%d of %d published templates ranked against your query." % (
                len(items), len(agents))
        else:
            items = [self._entry_summary(e) for e in agents]
            tokens = []
            msg = "%d published templates available to adapt." % len(agents)

        return json.dumps({
            "status": "ok",
            "action": "templates",
            "source_repo": TEMPLATE_REPO_URL,
            "license": TEMPLATE_LICENSE,
            "registry": meta,
            "query_tokens": tokens,
            "count": len(items),
            "templates": items,
            "message": msg + (
                "  WARNING: this listing came from a STALE cache — it may not reflect "
                "the current published set." if meta.get("stale") else ""),
        }, indent=2)

    # ── Template fetch + integrity verification ───────────────────────────

    def _fetch_and_verify(self, entry):
        expected = entry.get("_sha256")
        rel = entry.get("_file")
        if not expected:
            return {"ok": False, "reason": "no_expected_hash", "file": rel}
        url = TEMPLATE_RAW_BASE + rel
        if os.environ.get("RAPP_LEARN_OFFLINE") == "1":
            return {"ok": False, "reason": "fetch_failed", "url": url,
                    "error": "RAPP_LEARN_OFFLINE=1 — template bytes cannot be fetched or "
                             "verified offline; nothing unverified will be used"}
        try:
            body, _ = self._http_get(url)
        except Exception as e:
            return {"ok": False, "reason": "fetch_failed",
                    "error": "%s: %s" % (type(e).__name__, e), "url": url}

        actual = hashlib.sha256(body).hexdigest()
        if actual != expected:
            return {
                "ok": False,
                "reason": "integrity_mismatch",
                "url": url,
                "expected_sha256": expected,
                "actual_sha256": actual,
                "bytes": len(body),
                "action_taken": "bytes discarded, not written, not repaired",
            }
        return {
            "ok": True,
            "code": body.decode("utf-8"),
            "sha256": actual,
            "url": url,
            "bytes": len(body),
            "fetched_at": self._now_iso(),
            "verified": "sha256 matched the published registry entry",
        }

    def _build_from_template(self, description, template_pick='', **kwargs):
        if os.environ.get("RAPP_LEARN_OFFLINE") == "1" and not template_pick:
            pass  # still allowed: a cached registry may serve, fetch will then fail honestly

        reg, meta = self._load_registry(refresh=bool(kwargs.get('refresh')))
        report = {"registry": meta, "source_repo": TEMPLATE_REPO_URL, "license": TEMPLATE_LICENSE}

        if reg is None:
            report["outcome"] = "registry unavailable"
            return {"ok": False, "reason": "offline", "report": report}

        agents = reg.get("agents") or []
        report["templates_available"] = len(agents)

        if template_pick:
            entry, candidates = self._find_template(agents, template_pick)
            if entry is None:
                report["outcome"] = "explicit template not found"
                return {"ok": False, "reason": "unknown_template",
                        "candidates": candidates, "report": report}
            report["mode"] = "explicit override"
            report["chosen"] = self._entry_summary(entry)
            report["why"] = ("You named it: template=%r resolved to %s. Automatic "
                             "selection was bypassed." % (template_pick, entry.get("name")))
        else:
            tokens, ranked = self._rank_templates(agents, description)
            report["mode"] = "automatic selection"
            report["query_tokens"] = tokens
            report["considered"] = [self._entry_summary(e, s, h) for s, h, e in ranked]
            report["best_score"] = round(ranked[0][0], 1) if ranked else 0.0
            report["threshold"] = MIN_MATCH_SCORE
            if not ranked or ranked[0][0] < MIN_MATCH_SCORE:
                report["outcome"] = "no confident match — refusing to force one"
                return {"ok": False, "reason": "no_match", "report": report}
            score, hits, entry = ranked[0]
            runner_up = ranked[1][0] if len(ranked) > 1 else 0.0
            report["chosen"] = self._entry_summary(entry, score, hits)
            report["why"] = (
                "Best weighted match: scored %.1f (threshold %.1f, runner-up %.1f) on "
                "%s. Name/stack/tag hits weigh 3, description/vertical 2, solution "
                "metadata 1." % (score, MIN_MATCH_SCORE, runner_up,
                                 ", ".join(hits) or "no direct token hits"))

        fetched = self._fetch_and_verify(entry)
        if not fetched.get("ok"):
            reason = fetched.get("reason")
            report["outcome"] = "template rejected: %s" % reason
            if reason == "fetch_failed":
                report["fetch_error"] = fetched.get("error")
            if reason == "integrity_mismatch":
                report["integrity"] = fetched
                return {"ok": False, "reason": "integrity_mismatch",
                        "integrity": fetched, "report": report}
            return {"ok": False, "reason": reason, "report": report}

        report["outcome"] = "verified and adapted"
        report["integrity"] = {
            "url": fetched["url"],
            "expected_sha256": entry.get("_sha256"),
            "actual_sha256": fetched["sha256"],
            "match": True,
            "bytes": fetched["bytes"],
            "fetched_at": fetched["fetched_at"],
        }
        return {"ok": True, "entry": entry, "fetched": fetched, "report": report}

    def _name_from_template(self, entry, description):
        """Prefer a name derived from the user's ask; fall back to the template's."""
        derived = self._generate_name(description)
        if derived and derived != 'Custom':
            return derived
        disp = re.sub(r'[^a-zA-Z0-9 ]', '', str(entry.get("display_name") or ""))
        disp = disp.replace(" Agent", "")
        words = [w for w in disp.split() if w]
        if words:
            return ''.join(w[0].upper() + w[1:] for w in words[:3])
        return 'Custom'

    # ── Template mutation (structural, never regeneration) ────────────────

    def _py_block(self, var_name, data):
        lines = ["%s = {" % var_name]
        for k, v in data.items():
            lines.append("    %s: %s," % (repr(str(k)), repr(v)))
        lines.append("}")
        return lines

    def _mutate_template(self, code, entry, fetched, description, name, class_name, **kwargs):
        """
        Adapt a VERIFIED published template into the user's agent.

        Structure-preserving: the template's operations, data layer, and
        method bodies survive intact. What changes is identity (class name,
        agent name), the manifest, the documentation, the import shim, and
        the provenance record. Nothing is regenerated from scratch.
        """
        tree = ast.parse(code)
        lines = code.split("\n")
        edits = []  # (start0, end0_exclusive, replacement_lines)

        # 1. Locate the pieces we are allowed to touch.
        mod_doc = None
        manifest_node = None
        class_node = None
        import_node = None
        syspath_nodes = []

        if (tree.body and isinstance(tree.body[0], ast.Expr)
                and isinstance(tree.body[0].value, ast.Constant)
                and isinstance(tree.body[0].value.value, str)):
            mod_doc = tree.body[0]

        for node in tree.body:
            if (isinstance(node, ast.Assign) and manifest_node is None
                    and any(isinstance(t, ast.Name) and t.id == "__manifest__"
                            for t in node.targets)):
                manifest_node = node
            elif isinstance(node, ast.ClassDef) and class_node is None:
                for b in node.bases:
                    bn = b.id if isinstance(b, ast.Name) else getattr(b, "attr", None)
                    if bn == "BasicAgent":
                        class_node = node
                        break
            elif isinstance(node, ast.ImportFrom) and node.module == "basic_agent":
                import_node = node
            elif isinstance(node, ast.Expr):
                seg = ast.get_source_segment(code, node) or ""
                if "sys.path.insert" in seg:
                    syspath_nodes.append(node)

        if class_node is None:
            raise ValueError("template has no BasicAgent subclass to adapt")

        old_class = class_node.name
        old_manifest = {}
        if manifest_node is not None:
            try:
                old_manifest = ast.literal_eval(manifest_node.value)
            except Exception:
                old_manifest = {}

        namespace = (kwargs.get('namespace', '') or 'rapp').lstrip('@')
        snake = self._to_snake_case(name)
        safe_desc = description.replace('"', "'").replace('\n', ' ').strip()[:300]
        user_tags = self._generate_tags(description)
        tags = []
        for t in user_tags + list(old_manifest.get("tags") or []):
            t = str(t)
            if t not in tags:
                tags.append(t)
        env_list = [e.strip() for e in (kwargs.get('requires_env', '') or '').split(",") if e.strip()]
        category = kwargs.get('category') or old_manifest.get("category") or "general"
        adapted_at = self._now_iso()

        provenance = {
            "adapted_from_repo": TEMPLATE_REPO_URL,
            "adapted_from_agent": entry.get("name"),
            "adapted_from_file": entry.get("_file"),
            "source_url": fetched["url"],
            "source_sha256": fetched["sha256"],
            "sha256_verified": True,
            "verification": "sha256 of the fetched bytes matched registry.json's published _sha256",
            "fetched_at": fetched["fetched_at"],
            "adapted_at": adapted_at,
            "adapted_by": "%s v%s" % (__manifest__["name"], __manifest__["version"]),
            "method": "structural mutation (rename + remanifest + retarget); NOT regenerated",
            "license": TEMPLATE_LICENSE,
            "upstream_display_name": entry.get("display_name"),
            "upstream_description": entry.get("description"),
        }

        # 2. Module docstring -> new purpose + provenance + MIT attribution.
        ops = [n.name[1:] for n in class_node.body
               if isinstance(n, ast.FunctionDef) and n.name.startswith("_")
               and not n.name.startswith("__")]
        new_doc = ['"""', "%s" % name, "", safe_desc or "Adapted RAPP agent.", "",
                   "ADAPTED, NOT GENERATED.", ""]
        new_doc += [
            "This agent was produced by mutating a real published agent rather than",
            "writing one from scratch. The upstream structure, operations and data",
            "layer are preserved; identity, manifest and documentation were retargeted.",
            "",
            "  Upstream agent : %s" % entry.get("name"),
            "  Upstream repo  : %s (branch %s)" % (TEMPLATE_REPO_URL, TEMPLATE_BRANCH),
            "  Upstream file  : %s" % entry.get("_file"),
            "  sha256         : %s (verified at fetch time)" % fetched["sha256"],
            "  Fetched        : %s" % fetched["fetched_at"],
            "  Adapted        : %s by %s" % (adapted_at, __manifest__["name"]),
            "",
            "  License: %s" % TEMPLATE_LICENSE,
            "  The upstream MIT terms travel with this file. Attribution preserved.",
            "",
            "Drop this file into any RAPP brainstem's agents/ directory and it works.",
            "Compatible with the RAR registry at https://github.com/kody-w/RAR",
            '"""',
        ]
        if mod_doc is not None:
            edits.append((mod_doc.lineno - 1, mod_doc.end_lineno, new_doc))
        else:
            edits.append((0, 0, new_doc + [""]))

        # 3. Import shim -> the portable RAPP form.
        rapp_import = [
            "try:",
            "    from agents.basic_agent import BasicAgent",
            "except ImportError:",
            "    from basic_agent import BasicAgent",
        ]
        if import_node is not None:
            edits.append((import_node.lineno - 1, import_node.end_lineno, rapp_import))
        for n in syspath_nodes:
            edits.append((n.lineno - 1, n.end_lineno,
                          ["# (upstream sys.path shim removed — RAPP resolves BasicAgent directly)"]))

        # 4. Manifest -> this agent's identity + provenance block.
        new_manifest = {
            "schema": "rapp-agent/1.0",
            "name": "@%s/%s" % (namespace, snake),
            "version": "1.0.0",
            "display_name": name,
            "description": safe_desc or old_manifest.get("description", ""),
            "author": namespace,
            "tags": tags,
            "category": category,
            "quality_tier": "community",
            "requires_env": env_list,
            "dependencies": ["@rapp/basic_agent"],
            "example_call": {"args": {"operation": (ops[0] if ops else "run")}},
            "derived_from": entry.get("name"),
            "derived_from_sha256": fetched["sha256"],
            "license": "MIT (inherited from %s)" % TEMPLATE_REPO,
        }
        manifest_lines = (
            ["# " + "=" * 63,
             "# RAPP AGENT MANIFEST",
             "# " + "=" * 63]
            + self._py_block("__manifest__", new_manifest)
            + ["",
               "# " + "=" * 63,
               "# PROVENANCE — this file is an adaptation of a published agent.",
               "# Do not strip: it is the audit trail and the license attribution.",
               "# " + "=" * 63]
            + self._py_block("__provenance__", provenance)
        )
        if manifest_node is not None:
            # Swallow the upstream banner comment directly above the manifest so
            # the adapted file carries one banner, not two.
            start = manifest_node.lineno - 1
            while start > 0 and lines[start - 1].strip().startswith("#"):
                start -= 1
            edits.append((start, manifest_node.end_lineno, manifest_lines))
        else:
            edits.append((class_node.lineno - 1, class_node.lineno - 1, manifest_lines + ["", ""]))

        # 5. Class docstring -> adaptation note, upstream doc preserved below.
        cls_doc_node = None
        if (class_node.body and isinstance(class_node.body[0], ast.Expr)
                and isinstance(class_node.body[0].value, ast.Constant)
                and isinstance(class_node.body[0].value.value, str)):
            cls_doc_node = class_node.body[0]
        original_doc = (cls_doc_node.value.value if cls_doc_node else "").strip("\n")
        note = ['    """',
                "    %s" % name,
                "",
                "    ADAPTATION TARGET: %s" % (safe_desc or "(no description given)"),
                "",
                "    Behaviour below is inherited from %s and is intentionally left" % entry.get("name"),
                "    intact. To retarget it, edit the operations listed here rather than",
                "    rewriting the file — the structure is the part that was proven.",
                ""]
        if original_doc:
            note += ["    --- upstream documentation (preserved) ---"]
            note += ["    " + ln if ln.strip() else "" for ln in original_doc.split("\n")]
        note += ['    """']
        if cls_doc_node is not None:
            edits.append((cls_doc_node.lineno - 1, cls_doc_node.end_lineno, note))
        else:
            edits.append((class_node.body[0].lineno - 1, class_node.body[0].lineno - 1, note))

        # 6. Apply edits bottom-up so line numbers stay valid.
        for start, end, repl in sorted(edits, key=lambda x: -x[0]):
            lines[start:end] = repl
        mutated = "\n".join(lines)

        # 7. Rename the class (and every reference, including self.name).
        mutated = re.sub(r'\b%s\b' % re.escape(old_class), class_name, mutated)
        mutated = re.sub(r"(self\.name\s*=\s*)(['\"])[^'\"]*\2",
                         lambda m: '%s"%s"' % (m.group(1), class_name), mutated, count=1)

        if not mutated.endswith("\n"):
            mutated += "\n"

        # 8. Fail loudly rather than emit a broken file.
        ast.parse(mutated)
        return mutated, provenance

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
        out_dir = self._resolve_output_dir(kwargs.get('output_dir'))
        if write:
            out_dir.mkdir(parents=True, exist_ok=True)

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
                dest = out_dir / sub_filename
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
            dest = out_dir / orch_filename
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
            "generator": "builtin-scratch",
            "generator_description": (
                "Swarm scaffolding comes from LearnNewAgent's built-in string templates; "
                "published-template adaptation applies to single agents (action='create')."
            ),
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
                    fpath = out_dir / f["filename"]
                    self._hot_load_agent(fpath, f["class"])
            orch_path = out_dir / orch_filename
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

        submission = {
            "status": "ok",
            "action": "submit",
            "generator": preview.get("generator"),
            "generator_description": preview.get("generator_description"),
            "filename": filename,
            "namespace": f"@{namespace}",
            "rar_path": rar_path,
            "issue_title": issue_title,
            "code": code,
        }
        if preview.get("provenance"):
            submission["provenance"] = preview["provenance"]
            submission["attribution_notice"] = (
                "This agent is an adaptation of %s under %s. The provenance block in the "
                "generated file must survive submission." % (
                    preview["provenance"].get("adapted_from_agent"), TEMPLATE_LICENSE)
            )
        if preview.get("template_selection"):
            submission["template_selection"] = preview["template_selection"]
        submission.update({
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
        return json.dumps(submission, indent=2)

    # ── Name generation ───────────────────────────────────────────────────

    def _generate_name(self, description):
        try:
            if os.environ.get("RAPP_LEARN_NO_LLM") == "1":
                raise RuntimeError("LLM naming disabled by RAPP_LEARN_NO_LLM=1")
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
            if os.environ.get("RAPP_LEARN_NO_LLM") == "1":
                raise RuntimeError("LLM body generation disabled by RAPP_LEARN_NO_LLM=1")
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

    def _list_generated_agents(self, output_dir=None):
        agents = []
        scan_dir = self._resolve_output_dir(output_dir)
        core = {'basic_agent.py', 'save_memory_agent.py', 'recall_memory_agent.py',
                'learn_new_agent.py', 'swarm_factory_agent.py'}
        for f in sorted(scan_dir.glob('*_agent.py')):
            if f.name in core:
                continue
            content = f.read_text()
            from_scratch = 'Auto-generated by LearnNewAgent' in content
            adapted = '__provenance__' in content and 'ADAPTED, NOT GENERATED' in content
            entry = {
                "name": f.stem.replace('_agent', ''),
                "file": f.name,
                "auto_generated": from_scratch or adapted,
                "origin": ("aibast-template-mutation" if adapted
                           else "builtin-scratch" if from_scratch else "unknown"),
            }
            if adapted:
                m = re.search(r"'adapted_from_agent':\s*'([^']+)'", content)
                if m:
                    entry["adapted_from"] = m.group(1)
            agents.append(entry)
        return json.dumps({
            "status": "success",
            "directory": str(scan_dir),
            "agents": agents,
            "count": len(agents)
        })

    def _delete_agent(self, name, output_dir=None):
        scan_dir = self._resolve_output_dir(output_dir)
        if not name:
            return json.dumps({
                "status": "error",
                "message": "Please provide the agent name to delete."
            })

        snake_name = self._to_snake_case(self._sanitize_name(name))
        file_path = scan_dir / f"{snake_name}_agent.py"

        if not file_path.exists():
            for f in scan_dir.glob('*_agent.py'):
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
    # Preview only — writes nothing. Shows which path produced the output.
    print(a.perform(
        action="preview",
        description="An agent that researches an enterprise account and maps its buying committee before a sales call"))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
