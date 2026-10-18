---
name: "rar-rapp-learn-new"
description: "Creates new RAPP agents or swarms from natural-language descriptions. By default it ADAPTS a real published agent from the public microsoft/aibast-agents-library (sha256-verified) instead of generating code from scratch. Actions: 'create' adapts a template into a single agent, 'templates' searches the published templates, 'swarm' creates a multi-agent pipeline, 'list' shows generated agents, 'delete' removes one, 'preview' dry-runs generation, 'submit' prepares a RAR registry submission. Call when the user wants to teach the brainstem something new, create a custom agent, or build an agent swarm."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/learn_new", "rar_sha256": "f9a108cd377b5b91d9288f56ee9f91c57717595c9cfb1e98b4952200c6806dfc", "source_kind": "rar-agent", "source_commit": "797681a7ca943fafc935d533fedd008ce2305420", "version": "3.1.0", "author": "RAPP", "tags": ["meta", "generator", "scaffolding", "learn", "swarm", "templates", "aibast"]}
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
  RAPP_LEARN_REGISTRY_URL      — another template library in the same registry.json shape
  RAPP_LEARN_TEMPLATE_BASE     — the base its "_file" paths resolve against (file:// works)
  RAPP_LEARN_TEMPLATE_REPO / _REPO_URL / _BRANCH / _LICENSE — how adapted files name that source

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `learn_new_agent.py` and embedded as the fenced Python below (sha256 f9a108cd377b5b91…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `learn_new_agent.py` first:

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
  RAPP_LEARN_REGISTRY_URL      — another template library in the same registry.json shape
  RAPP_LEARN_TEMPLATE_BASE     — the base its "_file" paths resolve against (file:// works)
  RAPP_LEARN_TEMPLATE_REPO / _REPO_URL / _BRANCH / _LICENSE — how adapted files name that source
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
    "version": "3.1.0",
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
# Another library in the same registry.json shape can be the template source instead
# (RAPP_LEARN_REGISTRY_URL; file:// works for a local library). Unset, nothing changes.
TEMPLATE_REPO = os.environ.get("RAPP_LEARN_TEMPLATE_REPO") or "microsoft/aibast-agents-library"
TEMPLATE_BRANCH = os.environ.get("RAPP_LEARN_TEMPLATE_BRANCH") or "main"
TEMPLATE_RAW_BASE = os.environ.get("RAPP_LEARN_TEMPLATE_BASE") or \
    "https://raw.githubusercontent.com/%s/%s/" % (TEMPLATE_REPO, TEMPLATE_BRANCH)
TEMPLATE_REGISTRY_URL = os.environ.get("RAPP_LEARN_REGISTRY_URL") or TEMPLATE_RAW_BASE + "registry.json"
TEMPLATE_REPO_URL = os.environ.get("RAPP_LEARN_TEMPLATE_REPO_URL") or "https://github.com/%s" % TEMPLATE_REPO
TEMPLATE_LICENSE = os.environ.get("RAPP_LEARN_TEMPLATE_LICENSE") or \
    "MIT License, Copyright (c) Microsoft (see %s/blob/%s/LICENSE)" % (TEMPLATE_REPO_URL, TEMPLATE_BRANCH)
DEFAULT_REGISTRY_URL = "https://raw.githubusercontent.com/microsoft/aibast-agents-library/main/registry.json"

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
        # One cache per source, so switching libraries never serves another library's index.
        stem = "aibast-registry" if TEMPLATE_REGISTRY_URL == DEFAULT_REGISTRY_URL else \
            "registry-" + hashlib.sha256(TEMPLATE_REGISTRY_URL.encode()).hexdigest()[:16]
        cache_f = cdir / (stem + ".json")
        meta_f = cdir / (stem + ".meta.json")

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
