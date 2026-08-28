---
name: "rar-rapp-learn-new"
description: "Creates new RAPP agents or swarms from natural-language descriptions. By default it ADAPTS a real published agent from the public microsoft/aibast-agents-library (sha256-verified) instead of generating code from scratch. Actions: 'create' adapts a template into a single agent, 'templates' searches the published templates, 'swarm' creates a multi-agent pipeline, 'list' shows generated agents, 'delete' removes one, 'preview' dry-runs generation, 'submit' prepares a RAR registry submission. Call when the user wants to teach the brainstem something new, create a custom agent, or build an agent swarm."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/learn_new", "rar_sha256": "9104535d15333d9a30543d94483df7bad958a61c4b4c00e492fc627fe3b21741", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "3.0.1", "author": "RAPP", "tags": ["meta", "generator", "scaffolding", "learn", "swarm", "templates", "aibast"]}
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
