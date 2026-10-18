---
name: "rar-rapp-learn-new"
description: "Creates new single-file RAPP agents by adapting a real published agent from the public microsoft/aibast-agents-library (sha256-verified, MIT-attributed, mutated not regenerated); or, with source='chat', saves an agent the chat model wrote only after its own test call passes; built-in scratch templates remain as an explicit fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/learn_new", "rar_sha256": "7f2540f9c39bd60b93a8cc3059768c839cf4555acd8779ed3c167c61e33eaafe", "source_kind": "rar-agent", "source_commit": "d14ad46c566f809379da94f3ff9f4ee6413008e1", "version": "3.2.0", "author": "RAPP", "tags": ["meta", "generator", "scaffolding", "learn", "swarm", "templates", "aibast"]}
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

v3.2 — CHAT-WRITTEN (source='chat'). The model already in the conversation
writes the whole agent file (`code`) plus one test call (`test_args`) and the
text its correct answer contains (`expect`). The file is written only if it
parses, defines exactly one BasicAgent class whose name matches, takes a free
file name, and the test call, run in a separate process, returns that text.
Otherwise nothing is written and the reason goes back to the model to fix.
Without source='chat', nothing about the other paths changes.

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

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `learn_new_agent.py` and embedded as the fenced Python below (sha256 7f2540f9c39bd60b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `learn_new_agent.py` first:

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

v3.2 — CHAT-WRITTEN (source='chat'). The model already in the conversation
writes the whole agent file (`code`) plus one test call (`test_args`) and the
text its correct answer contains (`expect`). The file is written only if it
parses, defines exactly one BasicAgent class whose name matches, takes a free
file name, and the test call, run in a separate process, returns that text.
Otherwise nothing is written and the reason goes back to the model to fix.
Without source='chat', nothing about the other paths changes.

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
import sys
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
    "version": "3.2.0",
    "display_name": "LearnNew",
    "description": "Creates new single-file RAPP agents by adapting a real published agent from the public microsoft/aibast-agents-library (sha256-verified, MIT-attributed, mutated not regenerated); or, with source='chat', saves an agent the chat model wrote only after its own test call passes; built-in scratch templates remain as an explicit fallback.",
    "author": "RAPP",
    "tags": ["meta", "generator", "scaffolding", "learn", "swarm", "templates", "aibast"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {"args": {"action": "create", "description": "An agent that researches an enterprise account before a sales call"}},
}


# ── source='chat': the shape the chat model writes, and the test runner ──
CHAT_TEMPLATE = '''try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent
import json  # and any other standard-library modules the logic needs

class {Name}Agent(BasicAgent):
    def __init__(self):
        self.name = "{Name}"
        self.metadata = {
            "name": self.name,
            "description": "{when to use it and what it returns}",
            "parameters": {
                "type": "object",
                "properties": {
                    "{param}": {"type": "{number|string|integer|boolean|array}", "description": "{what it is}"}
                },
                "required": ["{param}"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        {param} = kwargs.get("{param}")
        # the real logic, every step written out; no placeholders, no TODO
        return "{a plain sentence with the result}"   # a STRING, not a dict'''

CHAT_RUNNER = r'''
import importlib.util, json, sys
sys.path[:0] = [sys.argv[1], sys.argv[2]]
spec = importlib.util.spec_from_file_location("candidate", sys.argv[3])
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent
classes = [c for c in vars(mod).values()
           if isinstance(c, type) and issubclass(c, BasicAgent) and c is not BasicAgent]
if len(classes) != 1:
    raise SystemExit("the file must define exactly one BasicAgent class, it defines %d" % len(classes))
agent = classes[0]()
out = agent.perform(**json.loads(sys.argv[4]))
print(json.dumps({"name": agent.name, "result": out if isinstance(out, str) else json.dumps(out)}))
'''


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
                "To create an agent whose logic YOU write (calculations, text handling, "
                "anything no template covers), use action='create', source='chat' with "
                "name, code (the complete file), test_args and expect: it is saved only "
                "if your test call returns expect. "
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
                        "enum": ["template", "scratch", "chat"],
                        "description": (
                            "Where the new agent comes from. 'template' (default) adapts a "
                            "verified published agent; 'scratch' uses the built-in string "
                            "templates. Scratch is also the automatic fallback when offline "
                            "or when nothing matches well. 'chat': you write the whole file "
                            "in 'code' and give 'test_args' and 'expect'; it is saved only "
                            "if the test passes."
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
                    },
                    "code": {
                        "type": "string",
                        "description": "For source='chat': the complete Python file. Follow this shape exactly:\n" + CHAT_TEMPLATE
                    },
                    "test_args": {
                        "type": "object",
                        "description": "For source='chat': one realistic call to the new agent, the arguments perform() gets (e.g. {\"total\": 120, \"tip_percent\": 20, \"people\": 4})."
                    },
                    "expect": {
                        "type": "string",
                        "description": "For source='chat': text the correct answer to test_args must contain, worked out by you beforehand (e.g. \"36\")."
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
        if source_mode == 'chat':
            return self._create_from_chat(description, name, write=write, **kwargs)
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

    # ── Chat-written agents (source='chat') ───────────────────────────────

    def _create_from_chat(self, description, name='', write=True, code='', test_args=None, expect='', **kwargs):
        def refuse(why):
            return json.dumps({
                "status": "error",
                "action": "create" if write else "preview",
                "generator": "chat-written",
                "message": "NOT SAVED: %s. Fix it and call LearnNew again with source='chat'." % why,
            }, indent=2)

        name = (name or '').strip()
        if not re.fullmatch(r"[A-Z][A-Za-z0-9]*", name):
            return refuse("name must be CamelCase letters and digits, e.g. TipSplitter")
        if not (code or '').strip():
            return refuse("code is empty; send the complete agent file")
        try:
            ast.parse(code)
        except SyntaxError as e:
            return refuse("line %s does not parse: %s" % (e.lineno, e.msg))
        if not str(expect or '').strip():
            return refuse("expect is empty; say what the correct answer to test_args contains")
        if isinstance(test_args, str):
            try:
                test_args = json.loads(test_args)
            except ValueError:
                return refuse("test_args must be an object of arguments")
        if not isinstance(test_args, dict):
            return refuse("test_args must be an object of arguments")

        snake = self._to_snake_case(name)
        file_name = f"{snake}_agent.py"
        out_dir = self._resolve_output_dir(kwargs.get('output_dir'))
        file_path = out_dir / file_name
        if write and file_path.exists():
            return refuse("%s already exists; pick another name" % file_name)

        with tempfile.TemporaryDirectory() as tmp:
            cand = Path(tmp) / file_name
            cand.write_text(code)
            try:
                p = subprocess.run(
                    [sys.executable, "-c", CHAT_RUNNER, str(self.agents_dir.parent), str(self.agents_dir),
                     str(cand), json.dumps(test_args)],
                    capture_output=True, text=True, timeout=30, cwd=tmp, stdin=subprocess.DEVNULL)
            except subprocess.TimeoutExpired:
                return refuse("the test call took longer than 30 seconds")
        if p.returncode != 0:
            return refuse("the test call failed:\n" + (p.stderr or p.stdout).strip()[-1200:])
        try:
            ran = json.loads(p.stdout.strip().splitlines()[-1])
        except (ValueError, IndexError):
            return refuse("the test call printed nothing readable")
        if ran["name"] != name:
            return refuse("self.name is %r but name is %r; make them the same" % (ran["name"], name))
        if str(expect).strip().lower() not in ran["result"].lower():
            return refuse("test_args %s returned %r, which does not contain %r"
                          % (json.dumps(test_args), ran["result"][:400], expect))

        test = {"args": test_args, "expect": expect, "returned": ran["result"][:400]}
        base = {
            "generator": "chat-written",
            "generator_description": "Written by the chat model; saved only after its own test call returned the expected text",
            "agent_name": name,
            "filename": file_name,
            "lines": len(code.split('\n')),
            "test": test,
        }
        if not write:
            out = dict(base)
            out.update({"status": "ok", "action": "preview", "code": code,
                        "message": f"Test passed. Preview of {file_name} — use action='create' to write it."})
            return json.dumps(out, indent=2)
        try:
            out_dir.mkdir(parents=True, exist_ok=True)
            file_path.write_text(code)
        except Exception as e:
            return refuse(f"the file could not be written: {e}")
        hot = self._hot_load_agent(file_path, f"{name}Agent")
        out = dict(base)
        out.update({
            "status": "success",
            "action": "create",
            "message": f"Created agent '{name}' (chat-written, test passed)",
            "file_path": str(file_path),
            "hot_loaded": hot.get("success", False),
            "description": (description or '')[:200],
            "hint": f"Agent saved to {file_path} — it will auto-load on next request.",
        })
        if not hot.get("success"):
            out["hot_load_error"] = hot.get("error")
        return json.dumps(out, indent=2)

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
