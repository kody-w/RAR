---
name: "rar-rapp-learn-new"
description: "Creates new single-file RAPP agents by adapting a real published agent from the public microsoft/aibast-agents-library (sha256-verified, MIT-attributed, mutated not regenerated); or, with source='chat', saves an agent the chat model wrote only after its own test call passes; built-in scratch templates remain as an explicit fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/learn_new", "rar_sha256": "3cc1431dca7e6aee411f653c9ea2746e2161b1fe8db3fdeb5cbc72c0c803f4f9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.4.1", "author": "RAPP", "tags": ["meta", "generator", "scaffolding", "learn", "swarm", "templates", "aibast"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `learn_new_agent.py` and embedded as the fenced Python below (sha256 3cc1431dca7e6aee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `learn_new_agent.py` first:

```bash
python3 learn_new_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 learn_new_agent.py   # or on stdin
python3 learn_new_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/learn_new_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/learn_new_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/learn_new/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
