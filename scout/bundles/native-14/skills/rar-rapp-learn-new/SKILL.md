---
name: "rar-rapp-learn-new"
description: "Creates new single-file RAPP agents by adapting a real published agent from the public microsoft/aibast-agents-library (sha256-verified, MIT-attributed, mutated not regenerated); or, with source='chat', saves an agent the chat model wrote only after its own test call passes; built-in scratch templates remain as an explicit fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/learn_new", "rar_sha256": "c610a51c8958901dd8bf40f74de2ee4a6fd3f0d36bd52df6252da6c523ae8418", "source_kind": "rar-agent", "source_commit": "100291a4fa04c3446c132a053d8af64bde3cc6d6", "version": "3.3.0", "author": "RAPP", "tags": ["meta", "generator", "scaffolding", "learn", "swarm", "templates", "aibast"]}
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

v3.3 — NO SILENT SKELETONS. When no published template can be used (no
confident match, offline, fetch failed, no hash), create/preview no longer
write a placeholder agent that only echoes its query. They write nothing and
answer status "needs_code" with the reason and how to write the agent with
source='chat'. An explicit source='scratch' and swarms are unchanged;
RAPP_LEARN_SCRATCH_FALLBACK=1 restores the old fallback.

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
  RAPP_LEARN_SCRATCH_FALLBACK=1 — when no template can be used, write a scratch agent (the pre-3.3 fallback)
  RAPP_LEARN_REGISTRY_URL      — another template library in the same registry.json shape
  RAPP_LEARN_TEMPLATE_BASE     — the base its "_file" paths resolve against (file:// works)
  RAPP_LEARN_TEMPLATE_REPO / _REPO_URL / _BRANCH / _LICENSE — how adapted files name that source

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `learn_new_agent.py` and embedded as the fenced Python below (sha256 c610a51c8958901d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `learn_new_agent.py` first:

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

v3.3 — NO SILENT SKELETONS. When no published template can be used (no
confident match, offline, fetch failed, no hash), create/preview no longer
write a placeholder agent that only echoes its query. They write nothing and
answer status "needs_code" with the reason and how to write the agent with
source='chat'. An explicit source='scratch' and swarms are unchanged;
RAPP_LEARN_SCRATCH_FALLBACK=1 restores the old fallback.

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
  RAPP_LEARN_SCRATCH_FALLBACK=1 — when no template can be used, write a scratch agent (the pre-3.3 fallback)
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
    "version": "3.3.0",
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

        if agent_code is None and source_mode != 'scratch' \
                and os.environ.get("RAPP_LEARN_SCRATCH_FALLBACK") != "1":
            # No template could be used. A scratch file here would only echo its query
            # and look like success, so write nothing and ask for the real code.
            return self._needs_code(description, name, fallback_reason, template_report, write)

        if agent_code is None:
            # Scratch path: explicit choice, or the pre-3.3 fallback (RAPP_LEARN_SCRATCH_FALLBACK=1).
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

    def _needs_code(self, description, name, reason, report, write):
        why = {
            "offline": "the published template registry could not be reached and no cached copy is available",
            "no_match": "no published template matched this request with enough confidence (best score %s < %s)"
                        % ((report or {}).get("best_score"), MIN_MATCH_SCORE),
            "fetch_failed": "the chosen template could not be downloaded",
            "no_expected_hash": "the chosen template has no published sha256, so it could not be verified",
        }.get(reason, "no published template could be used (%s)" % reason)
        suggested = self._sanitize_name(name) if name else self._generate_name(description)
        return json.dumps({
            "status": "needs_code",
            "action": "create" if write else "preview",
            "generator": "none",
            "reason": reason,
            "message": (
                "Nothing was written: %s, and a placeholder agent would not do the job. "
                "Write the agent yourself: call LearnNew again with action='create', source='chat', "
                "name (CamelCase, e.g. %s), code (the complete file, in the shape the 'code' parameter "
                "describes), test_args (one realistic call) and expect (text its correct answer contains). "
                "It is saved only if that test passes. To browse templates instead use action='templates'; "
                "for a placeholder file anyway use source='scratch'." % (why, suggested)
            ),
            "suggested_name": suggested,
            "description": (description or "")[:200],
            "template_selection": report,
        }, indent=2)

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
