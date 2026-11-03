---
name: "rar-rapp-learn-new"
description: "Creates new single-file RAPP agents by adapting a real published agent from the public microsoft/aibast-agents-library (sha256-verified, MIT-attributed, mutated not regenerated); or, with source='chat', saves an agent the chat model wrote only after its own test call passes; built-in scratch templates remain as an explicit fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/learn_new", "rar_sha256": "0d3df4dbd6ee8f7d9786cc7cbd2c35616fb61bd0813cd85150b6c339fe6618e2", "source_kind": "rar-agent", "source_commit": "513c341d154ec859f7124d096c56ae650a6420e1", "version": "3.4.1", "author": "RAPP", "tags": ["meta", "generator", "scaffolding", "learn", "swarm", "templates", "aibast"]}
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
