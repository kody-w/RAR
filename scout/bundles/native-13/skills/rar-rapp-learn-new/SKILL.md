---
name: "rar-rapp-learn-new"
description: "Creates new RAPP agents or swarms from natural-language descriptions. By default it ADAPTS a real published agent from the public microsoft/aibast-agents-library (sha256-verified) instead of generating code from scratch. Actions: 'create' adapts a template into a single agent, 'templates' searches the published templates, 'swarm' creates a multi-agent pipeline, 'list' shows generated agents, 'delete' removes one, 'preview' dry-runs generation, 'submit' prepares a RAR registry submission. Call when the user wants to teach the brainstem something new, create a custom agent, or build an agent swarm."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/learn_new", "rar_sha256": "9104535d15333d9a30543d94483df7bad958a61c4b4c00e492fc627fe3b21741", "source_kind": "rar-agent", "source_commit": "b4ba983328bbb00340c62a83332318dc0ffc22aa", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "learn_new_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/learn-new:b34f04ce326a6f9a34bc4368ea5dca3cdbe3da10a791aea4e3b08d48d30cfe93", "kind": "skill"}, "version": "3.0.1", "author": "RAPP", "tags": ["meta", "generator", "scaffolding", "learn", "swarm", "templates", "aibast"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/learn_new`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `learn_new_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
