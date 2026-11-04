---
name: "rar-rapp-learn-new"
description: "Creates new single-file RAPP agents by adapting a real published agent from the public microsoft/aibast-agents-library (sha256-verified, MIT-attributed, mutated not regenerated); or, with source='chat', saves an agent the chat model wrote only after its own test call passes; built-in scratch templates remain as an explicit fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/learn_new", "rar_sha256": "3cc1431dca7e6aee411f653c9ea2746e2161b1fe8db3fdeb5cbc72c0c803f4f9", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.4.1", "author": "RAPP", "tags": ["meta", "generator", "scaffolding", "learn", "swarm", "templates", "aibast"]}
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
