---
name: "rar-rapp-learn-new"
description: "Creates new single-file RAPP agents by adapting a real published agent from the public microsoft/aibast-agents-library (sha256-verified, MIT-attributed, mutated not regenerated); or, with source='chat', saves an agent the chat model wrote only after its own test call passes; built-in scratch templates remain as an explicit fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/learn_new", "rar_sha256": "0d3df4dbd6ee8f7d9786cc7cbd2c35616fb61bd0813cd85150b6c339fe6618e2", "source_kind": "rar-agent", "source_commit": "37b2f58ea887a90b996f47e63f3bba1918d4fa8a", "version": "3.4.1", "author": "RAPP", "tags": ["meta", "generator", "scaffolding", "learn", "swarm", "templates", "aibast"]}
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

v3.4.1 — 3.4.0 briefly added action='workflow'; it now lives in its own agent,
@kody-w/workflow_builder (stacks/claude-workflows). This version behaves exactly
like 3.3.0.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `learn_new_agent.py` and embedded as the fenced Python below (sha256 0d3df4dbd6ee8f7d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `learn_new_agent.py` first:

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

v3.4.1 — 3.4.0 briefly added action='workflow'; it now lives in its own agent,
@kody-w/workflow_builder (stacks/claude-workflows). This version behaves exactly
like 3.3.0.

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
    "version": "3.4.1",
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
