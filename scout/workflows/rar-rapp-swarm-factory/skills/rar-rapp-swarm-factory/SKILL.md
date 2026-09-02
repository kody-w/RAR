---
name: "rar-rapp-swarm-factory"
description: "Generate, build, install, list, and uninstall RAPP swarms.\n\nA SWARM is a multi-persona pipeline collapsed into ONE shareable agent file \u2014 like BookFactory (Writer\u2192Editor\u2192CEO\u2192Publisher\u2192Reviewer all inlined as _Internal* classes behind one public entrypoint). Each persona has its own SOUL/system prompt; deterministic Python in perform() orchestrates them \u2014 the LLM calls are leaf nodes, the control flow is code.\n\nROLE BOUNDARY:\n \u2022 Single one-shot agent (fetch xkcd, roll dice) \u2192 LearnNew with action='create'. Do NOT use SwarmFactory.\n \u2022 Multi-persona converged singleton (research\u2192write\u2192critique, write\u2192edit\u2192publish) \u2192 SwarmFactory.generate.\n \u2022 Existing multi-file agents to collapse into one shippable file \u2192 SwarmFactory.build.\n\nActions:\n \u2022 'generate' \u2014 Design a BRAND-NEW converged swarm. YOU (the LLM) compose the full Python source \u2014 multiple _Internal persona classes (each with its own SOUL) plus ONE public composite \u2014 and pass it as 'agent_code'. Hot-loads on the next request. If the request is single-persona, REFUSE and route to LearnNew.create.\n \u2022 'build' \u2014 Converge existing local agents into a singleton .py.\n \u2022 'list' / 'install' / 'uninstall' \u2014 RAPP Store catalog ops.\n\nHARD RULES for generated swarm code (each maps to a shipped pattern in @rarbookworld/bookfactory v0.4 \u2014 read it as the exemplar):\n 1. ERRORS ARE DATA, NEVER CONTENT. _post retries once on 429/5xx/network then RAISES RuntimeError. perform() wraps the pipeline in ONE try/except and returns json.dumps({'status':'error','failed_stage':...,'completed_stages':[...]}). NEVER return '(LLM HTTP ...)' strings \u2014 the next persona would edit the error as if it were prose and every downstream call burns on garbage.\n 2. GATES ACTUALLY GATE. When a persona renders a verdict (ship/hold, a score), obtain it via _llm_json (stdlib parse + required-keys check + one re-prompt-with-the-error) and BRANCH on it in code; honor 'hold' by halting with a partial report. Use _llm_json ONLY for verdict-shaped outputs \u2014 prose stages stay raw text (JSON-wrapping a draft corrupts code fences and voice).\n 3. PER-RUN WORKSPACE. Artifacts go under a fresh subdir per run (timestamp+uuid). The brainstem serves requests threaded; fixed paths make concurrent runs clobber each other.\n 4. STATIC BOUNDS. Every revision/retry cycle is capped by a hard-coded constant, and a run-scoped counter inside _llm_call refuses past _MAX_LLM_CALLS with a clear error. Refusal is a feature.\n 5. PARALLEL ONLY WHEN SAFE. If \u22652 stages consume the SAME input and NEITHER writes a shared memory GUID, you may inline a 6-line ThreadPoolExecutor helper (cap 3 branches). Personas sharing a memory GUID must stay sequential \u2014 the local storage shim has no file locking, so concurrent writers lose updates.\n 6. TIERING IS OPPORTUNISTIC. _llm_call(soul, prompt, tier=None); tier='small' reads AZURE_OPENAI_DEPLOYMENT_SMALL / OPENAI_MODEL_SMALL when set and silently falls back to the primary deployment. Never hard-code a literal model name \u2014 on Azure the 'model' is a per-tenant deployment name; a baked-in id 404s on every box but the author's.\n\nMemory architecture (each swarm picks its own):\nPersonas use AzureFileStorageManager().set_memory_context(<guid>) to read/write a NAMESPACED memory file. Strategies:\n \u2022 SHARED \u2014 one _SWARM_MEMORY_GUID = '<slug>-shared-v1' module constant; every persona uses it (researcher\u2192writer pipelines).\n \u2022 SEGMENTED \u2014 per-persona GUID constants (a critic that must review fresh, with no prior bias).\n \u2022 MIXED \u2014 shared GUID for coordinating personas, private for the isolated ones. \u2022 USER-SCOPED \u2014 pipe the caller's user_guid through.  \u2022 EPHEMERAL \u2014 don't import the storage manager at all.\nBake GUIDs as MODULE CONSTANTS at code-write time (deterministic and portable). Remember rule 5: shared-GUID personas never run in parallel.\n\nRequired shape for 'generate':\n    from agents.basic_agent import BasicAgent\n    import json, os, time, uuid, threading, urllib.request, urllib.error\n\n    __manifest__ = {\"schema\": \"rapp-agent/1.0\", \"name\": \"@user/<slug>\",\n                     \"version\": \"0.1.0\",\n                     \"tags\": [\"composite\", \"swarm-factory-generated\"],\n                     \"delegates_to_inlined\": [\"<persona1>\", \"<persona2>\"]}\n\n    _MAX_LLM_CALLS = 30   # static bound (rule 4)\n    _SOUL_RESEARCHER = \"You are a researcher...\"  # one SOUL per persona\n    _SOUL_WRITER     = \"You are a writer...\"\n    _SOUL_CRITIC     = \"You are a brutal critic...\"\n\n    _calls = {\"n\": 0}; _lock = threading.Lock()\n    def _llm_call(soul, prompt, tier=None):\n        with _lock:\n            _calls[\"n\"] += 1\n            if _calls[\"n\"] > _MAX_LLM_CALLS:\n                raise RuntimeError(f\"call budget exceeded ({_MAX_LLM_CALLS})\")\n        msgs = [{\"role\": \"system\", \"content\": soul},\n                {\"role\": \"user\", \"content\": prompt}]\n        ep, key = os.environ.get(\"AZURE_OPENAI_ENDPOINT\", \"\"),\\\n                  os.environ.get(\"AZURE_OPENAI_API_KEY\", \"\")\n        dep = os.environ.get(\"AZURE_OPENAI_DEPLOYMENT\", \"\")\n        if tier == \"small\":\n            dep = os.environ.get(\"AZURE_OPENAI_DEPLOYMENT_SMALL\") or dep  # graceful fallback (rule 6)\n        if ep and key:\n            url = ep.rstrip(\"/\") + f\"/openai/deployments/{dep}/chat/completions?api-version=2025-01-01-preview\"\n            return _post(url, {\"messages\": msgs, \"model\": dep},\n                          {\"Content-Type\": \"application/json\", \"api-key\": key})\n        if os.environ.get(\"OPENAI_API_KEY\"):\n            m = os.environ.get(\"OPENAI_MODEL\", \"gpt-4o\")\n            if tier == \"small\": m = os.environ.get(\"OPENAI_MODEL_SMALL\") or m\n            return _post(\"https://api.openai.com/v1/chat/completions\",\n                          {\"model\": m, \"messages\": msgs},\n                          {\"Content-Type\": \"application/json\",\n                           \"Authorization\": \"Bearer \" + os.environ[\"OPENAI_API_KEY\"]})\n        raise RuntimeError(\"no LLM configured\")  # raise \u2014 never return error text (rule 1)\n\n    def _post(url, body, headers):\n        for attempt in (1, 2):\n            req = urllib.request.Request(url, data=json.dumps(body).encode(\"utf-8\"),\n                                          headers=headers, method=\"POST\")\n            try:\n                with urllib.request.urlopen(req, timeout=120) as r:\n                    c = json.loads(r.read().decode(\"utf-8\")).get(\"choices\") or []\n                return (c[0][\"message\"].get(\"content\") or \"\") if c else \"\"\n            except urllib.error.HTTPError as e:\n                if (e.code == 429 or e.code >= 500) and attempt == 1:\n                    time.sleep(2); continue\n                raise RuntimeError(f\"LLM HTTP {e.code}\")\n            except urllib.error.URLError as e:\n                if attempt == 1: time.sleep(2); continue\n                raise RuntimeError(f\"LLM network error: {e}\")\n\n    def _llm_json(soul, prompt, required_keys, retries=1):  # verdicts ONLY (rule 2)\n        err = \"\"\n        for _ in range(retries + 1):\n            nudge = f\"\\nPrevious reply invalid ({err}); reply with ONLY the JSON object.\" if err else \"\"\n            raw = _llm_call(soul, prompt + \"\\nReply with ONLY a JSON object with keys: \"\n                            + \", \".join(required_keys) + nudge)\n            s, e = raw.find(\"{\"), raw.rfind(\"}\")\n            try:\n                obj = json.loads(raw[s:e + 1])\n            except ValueError as ex:\n                err = str(ex); continue\n            if all(k in obj for k in required_keys):\n                return obj\n            err = \"missing keys\"\n        raise RuntimeError(\"structured handoff failed: \" + err)\n\n    # _Internal prefix keeps personas out of *Agent auto-discovery.\n    class _InternalResearcher:\n        def perform(self, topic): return _llm_call(_SOUL_RESEARCHER, topic)\n    class _InternalWriter:\n        def perform(self, research): return _llm_call(_SOUL_WRITER, research)\n    class _InternalCritic:  # renders a verdict the orchestrator branches on\n        def verdict(self, draft):\n            return _llm_json(_SOUL_CRITIC, \"Judge this draft:\\n\" + draft +\n                '\\n\"verdict\" is \"ship\" or \"revise\"; \"note\" is one sentence.',\n                [\"verdict\", \"note\"])\n\n    class <PascalCase>Agent(BasicAgent):\n        def __init__(self):\n            self.name = \"<PascalCase>\"\n            self.metadata = {\"name\": \"<PascalCase>\",\n                             \"description\": \"<what the swarm does \u2014 one line>\",\n                             \"parameters\": {\"type\": \"object\",\n                                            \"properties\": {\"topic\": {\"type\": \"string\"}},\n                                            \"required\": [\"topic\"]}}\n            super().__init__(self.name, self.metadata)\n        def perform(self, topic=\"\", **kwargs):\n            ws = os.path.join(\"/tmp/<slug>\",  # per-run dir (rule 3)\n                              time.strftime(\"%Y%m%dT%H%M%S\") + \"-\" + uuid.uuid4().hex[:6])\n            os.makedirs(ws, exist_ok=True)\n            stage = \"start\"\n            try:\n                stage = \"researcher\"; research = _InternalResearcher().perform(topic)\n                stage = \"writer\";     draft = _InternalWriter().perform(research)\n                stage = \"critic\";     v = _InternalCritic().verdict(draft)\n                if v[\"verdict\"] != \"ship\":  # the gate is real (rule 2)\n                    return json.dumps({\"status\": \"held\", \"reason\": v[\"note\"],\n                                       \"draft\": draft, \"workspace\": ws})\n                return json.dumps({\"status\": \"ok\", \"final\": draft, \"workspace\": ws})\n            except RuntimeError as e:  # errors are data (rule 1)\n                return json.dumps({\"status\": \"error\", \"failed_stage\": stage,\n                                   \"message\": str(e), \"workspace\": ws})"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/swarm_factory_agent", "rar_sha256": "cfe3a0cffffb9d6395bf3d9377239e24500d3f7ab23c00b059da62f16a529ae0", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "swarm_factory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/swarm-factory:b9b1fe9d690d0df5eb2b9e1f2a7c4eeaacd48d196d2be33605a882ab7c05c1bc", "kind": "skill"}, "version": "0.3.1", "author": "RAPP", "tags": ["meta", "build", "singleton", "swarm-factory", "store"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/swarm_factory_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `swarm_factory_agent.py` is
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

swarm_factory_agent.py — Build, install, generate, and manage RAPP swarms.

Actions:
  generate  — Design a brand-new single-file agent from scratch and persist it
  build     — Converge existing local agents into a single shareable .py singleton
  list      — Show available swarms in the RAPP Store
  install   — Pull a swarm from the RAPP Store into your agents/ dir
  uninstall — Remove an installed swarm

Usage:
  "Build me an agent that fetches today's NYT front page and summarizes it" → generate
  "Package my agents as a swarm called SalesBot"                            → build
  "What swarms are available in the RAPP Store?"                            → list
  "Install the BookFactory swarm"                                           → install
  "Uninstall BookFactory"                                                   → uninstall

v0.3.0: the generate contract teaches the orchestration-harness hard rules —
errors raise (never flow downstream as prose), verdicts are structured and
actually gate, per-run workspaces, statically bounded cycles with a run
budget, parallel only for stateless same-input stages, opportunistic small-
model tiering with graceful fallback. Also fixes the build-mode manifest
name bug (built singletons previously claimed to BE the factory).

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "generate (design+persist a new agent), build (package locals into a singleton), list (browse store), install (pull from store), uninstall (remove)",
      "enum": [
        "generate",
        "build",
        "list",
        "install",
        "uninstall"
      ],
      "type": "string"
    },
    "agent_code": {
      "description": "REQUIRED for 'generate'. Full Python source for the new agent, top to bottom \u2014 imports, __manifest__ dict, the BasicAgent subclass with __init__/metadata/perform. Will be syntax-checked and contract-checked before persistence.",
      "type": "string"
    },
    "description": {
      "description": "One-line description of what this agent/swarm does. Used in the agent's manifest and in the LLM-facing description so the LLM knows when to call it.",
      "type": "string"
    },
    "exclude": {
      "description": "For 'build' only: comma-separated agent names to exclude. Built-in memory/factory agents are excluded automatically.",
      "type": "string"
    },
    "swarm_name": {
      "description": "PascalCase name for the new agent/swarm (generate, build) OR the swarm id/name (install, uninstall). Example: 'NytSummarizer'",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `swarm_factory_agent.py` and embedded as the fenced Python below (sha256 cfe3a0cffffb9d63…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `swarm_factory_agent.py` first:

```bash
python3 swarm_factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 swarm_factory_agent.py   # or on stdin
python3 swarm_factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
swarm_factory_agent.py — Build, install, generate, and manage RAPP swarms.

Actions:
  generate  — Design a brand-new single-file agent from scratch and persist it
  build     — Converge existing local agents into a single shareable .py singleton
  list      — Show available swarms in the RAPP Store
  install   — Pull a swarm from the RAPP Store into your agents/ dir
  uninstall — Remove an installed swarm

Usage:
  "Build me an agent that fetches today's NYT front page and summarizes it" → generate
  "Package my agents as a swarm called SalesBot"                            → build
  "What swarms are available in the RAPP Store?"                            → list
  "Install the BookFactory swarm"                                           → install
  "Uninstall BookFactory"                                                   → uninstall

v0.3.0: the generate contract teaches the orchestration-harness hard rules —
errors raise (never flow downstream as prose), verdicts are structured and
actually gate, per-run workspaces, statically bounded cycles with a run
budget, parallel only for stateless same-input stages, opportunistic small-
model tiering with graceful fallback. Also fixes the build-mode manifest
name bug (built singletons previously claimed to BE the factory).
"""

from agents.basic_agent import BasicAgent
import ast
import os
import re
import json
import hashlib
import glob
import urllib.request
import urllib.error


RAPP_STORE_CATALOG_URL = "https://raw.githubusercontent.com/kody-w/RAPP/main/rapp_store/index.json"

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/swarm_factory_agent",
    "display_name": "SwarmFactory",
    "description": "Generates, builds, installs, and uninstalls RAPP swarms \u2014 converging local agents into single shareable .py files via the RAPP Store catalog.",
    "author": "RAPP",
    "version": "0.3.1",
    "tags": ["meta", "build", "singleton", "swarm-factory", "store"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {"args": {"action": "list"}},
}


class SwarmFactoryAgent(BasicAgent):
    def __init__(self):
        self.name = "SwarmFactory"
        self.metadata = {
            "name": "SwarmFactory",
            "description": (
                "Generate, build, install, list, and uninstall RAPP swarms.\n\n"
                "A SWARM is a multi-persona pipeline collapsed into ONE shareable "
                "agent file — like BookFactory (Writer→Editor→CEO→Publisher→Reviewer "
                "all inlined as _Internal* classes behind one public entrypoint). "
                "Each persona has its own SOUL/system prompt; deterministic Python "
                "in perform() orchestrates them — the LLM calls are leaf nodes, the "
                "control flow is code.\n\n"
                "ROLE BOUNDARY:\n"
                " • Single one-shot agent (fetch xkcd, roll dice) → LearnNew with "
                "action='create'. Do NOT use SwarmFactory.\n"
                " • Multi-persona converged singleton (research→write→critique, "
                "write→edit→publish) → SwarmFactory.generate.\n"
                " • Existing multi-file agents to collapse into one shippable file "
                "→ SwarmFactory.build.\n\n"
                "Actions:\n"
                " • 'generate' — Design a BRAND-NEW converged swarm. YOU (the LLM) "
                "compose the full Python source — multiple _Internal persona classes "
                "(each with its own SOUL) plus ONE public composite — and pass it as "
                "'agent_code'. Hot-loads on the next request. If the request is "
                "single-persona, REFUSE and route to LearnNew.create.\n"
                " • 'build' — Converge existing local agents into a singleton .py.\n"
                " • 'list' / 'install' / 'uninstall' — RAPP Store catalog ops.\n\n"
                "HARD RULES for generated swarm code (each maps to a shipped pattern "
                "in @rarbookworld/bookfactory v0.4 — read it as the exemplar):\n"
                " 1. ERRORS ARE DATA, NEVER CONTENT. _post retries once on 429/5xx/"
                "network then RAISES RuntimeError. perform() wraps the pipeline in "
                "ONE try/except and returns json.dumps({'status':'error',"
                "'failed_stage':...,'completed_stages':[...]}). NEVER return "
                "'(LLM HTTP ...)' strings — the next persona would edit the error "
                "as if it were prose and every downstream call burns on garbage.\n"
                " 2. GATES ACTUALLY GATE. When a persona renders a verdict (ship/"
                "hold, a score), obtain it via _llm_json (stdlib parse + required-"
                "keys check + one re-prompt-with-the-error) and BRANCH on it in "
                "code; honor 'hold' by halting with a partial report. Use _llm_json "
                "ONLY for verdict-shaped outputs — prose stages stay raw text "
                "(JSON-wrapping a draft corrupts code fences and voice).\n"
                " 3. PER-RUN WORKSPACE. Artifacts go under a fresh subdir per run "
                "(timestamp+uuid). The brainstem serves requests threaded; fixed "
                "paths make concurrent runs clobber each other.\n"
                " 4. STATIC BOUNDS. Every revision/retry cycle is capped by a hard-"
                "coded constant, and a run-scoped counter inside _llm_call refuses "
                "past _MAX_LLM_CALLS with a clear error. Refusal is a feature.\n"
                " 5. PARALLEL ONLY WHEN SAFE. If ≥2 stages consume the SAME input "
                "and NEITHER writes a shared memory GUID, you may inline a 6-line "
                "ThreadPoolExecutor helper (cap 3 branches). Personas sharing a "
                "memory GUID must stay sequential — the local storage shim has no "
                "file locking, so concurrent writers lose updates.\n"
                " 6. TIERING IS OPPORTUNISTIC. _llm_call(soul, prompt, tier=None); "
                "tier='small' reads AZURE_OPENAI_DEPLOYMENT_SMALL / "
                "OPENAI_MODEL_SMALL when set and silently falls back to the primary "
                "deployment. Never hard-code a literal model name — on Azure the "
                "'model' is a per-tenant deployment name; a baked-in id 404s on "
                "every box but the author's.\n\n"
                "Memory architecture (each swarm picks its own):\n"
                "Personas use AzureFileStorageManager().set_memory_context(<guid>) "
                "to read/write a NAMESPACED memory file. Strategies:\n"
                " • SHARED — one _SWARM_MEMORY_GUID = '<slug>-shared-v1' module "
                "constant; every persona uses it (researcher→writer pipelines).\n"
                " • SEGMENTED — per-persona GUID constants (a critic that must "
                "review fresh, with no prior bias).\n"
                " • MIXED — shared GUID for coordinating personas, private for the "
                "isolated ones. • USER-SCOPED — pipe the caller's user_guid through. "
                " • EPHEMERAL — don't import the storage manager at all.\n"
                "Bake GUIDs as MODULE CONSTANTS at code-write time (deterministic "
                "and portable). Remember rule 5: shared-GUID personas never run in "
                "parallel.\n\n"
                "Required shape for 'generate':\n"
                "    from agents.basic_agent import BasicAgent\n"
                "    import json, os, time, uuid, threading, urllib.request, urllib.error\n\n"
                "    __manifest__ = {\"schema\": \"rapp-agent/1.0\", \"name\": \"@user/<slug>\",\n"
                "                     \"version\": \"0.1.0\",\n"
                "                     \"tags\": [\"composite\", \"swarm-factory-generated\"],\n"
                "                     \"delegates_to_inlined\": [\"<persona1>\", \"<persona2>\"]}\n\n"
                "    _MAX_LLM_CALLS = 30   # static bound (rule 4)\n"
                "    _SOUL_RESEARCHER = \"You are a researcher...\"  # one SOUL per persona\n"
                "    _SOUL_WRITER     = \"You are a writer...\"\n"
                "    _SOUL_CRITIC     = \"You are a brutal critic...\"\n\n"
                "    _calls = {\"n\": 0}; _lock = threading.Lock()\n"
                "    def _llm_call(soul, prompt, tier=None):\n"
                "        with _lock:\n"
                "            _calls[\"n\"] += 1\n"
                "            if _calls[\"n\"] > _MAX_LLM_CALLS:\n"
                "                raise RuntimeError(f\"call budget exceeded ({_MAX_LLM_CALLS})\")\n"
                "        msgs = [{\"role\": \"system\", \"content\": soul},\n"
                "                {\"role\": \"user\", \"content\": prompt}]\n"
                "        ep, key = os.environ.get(\"AZURE_OPENAI_ENDPOINT\", \"\"),\\\n"
                "                  os.environ.get(\"AZURE_OPENAI_API_KEY\", \"\")\n"
                "        dep = os.environ.get(\"AZURE_OPENAI_DEPLOYMENT\", \"\")\n"
                "        if tier == \"small\":\n"
                "            dep = os.environ.get(\"AZURE_OPENAI_DEPLOYMENT_SMALL\") or dep  # graceful fallback (rule 6)\n"
                "        if ep and key:\n"
                "            url = ep.rstrip(\"/\") + f\"/openai/deployments/{dep}/chat/completions?api-version=2025-01-01-preview\"\n"
                "            return _post(url, {\"messages\": msgs, \"model\": dep},\n"
                "                          {\"Content-Type\": \"application/json\", \"api-key\": key})\n"
                "        if os.environ.get(\"OPENAI_API_KEY\"):\n"
                "            m = os.environ.get(\"OPENAI_MODEL\", \"gpt-4o\")\n"
                "            if tier == \"small\": m = os.environ.get(\"OPENAI_MODEL_SMALL\") or m\n"
                "            return _post(\"https://api.openai.com/v1/chat/completions\",\n"
                "                          {\"model\": m, \"messages\": msgs},\n"
                "                          {\"Content-Type\": \"application/json\",\n"
                "                           \"Authorization\": \"Bearer \" + os.environ[\"OPENAI_API_KEY\"]})\n"
                "        raise RuntimeError(\"no LLM configured\")  # raise — never return error text (rule 1)\n\n"
                "    def _post(url, body, headers):\n"
                "        for attempt in (1, 2):\n"
                "            req = urllib.request.Request(url, data=json.dumps(body).encode(\"utf-8\"),\n"
                "                                          headers=headers, method=\"POST\")\n"
                "            try:\n"
                "                with urllib.request.urlopen(req, timeout=120) as r:\n"
                "                    c = json.loads(r.read().decode(\"utf-8\")).get(\"choices\") or []\n"
                "                return (c[0][\"message\"].get(\"content\") or \"\") if c else \"\"\n"
                "            except urllib.error.HTTPError as e:\n"
                "                if (e.code == 429 or e.code >= 500) and attempt == 1:\n"
                "                    time.sleep(2); continue\n"
                "                raise RuntimeError(f\"LLM HTTP {e.code}\")\n"
                "            except urllib.error.URLError as e:\n"
                "                if attempt == 1: time.sleep(2); continue\n"
                "                raise RuntimeError(f\"LLM network error: {e}\")\n\n"
                "    def _llm_json(soul, prompt, required_keys, retries=1):  # verdicts ONLY (rule 2)\n"
                "        err = \"\"\n"
                "        for _ in range(retries + 1):\n"
                "            nudge = f\"\\nPrevious reply invalid ({err}); reply with ONLY the JSON object.\" if err else \"\"\n"
                "            raw = _llm_call(soul, prompt + \"\\nReply with ONLY a JSON object with keys: \"\n"
                "                            + \", \".join(required_keys) + nudge)\n"
                "            s, e = raw.find(\"{\"), raw.rfind(\"}\")\n"
                "            try:\n"
                "                obj = json.loads(raw[s:e + 1])\n"
                "            except ValueError as ex:\n"
                "                err = str(ex); continue\n"
                "            if all(k in obj for k in required_keys):\n"
                "                return obj\n"
                "            err = \"missing keys\"\n"
                "        raise RuntimeError(\"structured handoff failed: \" + err)\n\n"
                "    # _Internal prefix keeps personas out of *Agent auto-discovery.\n"
                "    class _InternalResearcher:\n"
                "        def perform(self, topic): return _llm_call(_SOUL_RESEARCHER, topic)\n"
                "    class _InternalWriter:\n"
                "        def perform(self, research): return _llm_call(_SOUL_WRITER, research)\n"
                "    class _InternalCritic:  # renders a verdict the orchestrator branches on\n"
                "        def verdict(self, draft):\n"
                "            return _llm_json(_SOUL_CRITIC, \"Judge this draft:\\n\" + draft +\n"
                "                '\\n\"verdict\" is \"ship\" or \"revise\"; \"note\" is one sentence.',\n"
                "                [\"verdict\", \"note\"])\n\n"
                "    class <PascalCase>Agent(BasicAgent):\n"
                "        def __init__(self):\n"
                "            self.name = \"<PascalCase>\"\n"
                "            self.metadata = {\"name\": \"<PascalCase>\",\n"
                "                             \"description\": \"<what the swarm does — one line>\",\n"
                "                             \"parameters\": {\"type\": \"object\",\n"
                "                                            \"properties\": {\"topic\": {\"type\": \"string\"}},\n"
                "                                            \"required\": [\"topic\"]}}\n"
                "            super().__init__(self.name, self.metadata)\n"
                "        def perform(self, topic=\"\", **kwargs):\n"
                "            ws = os.path.join(\"/tmp/<slug>\",  # per-run dir (rule 3)\n"
                "                              time.strftime(\"%Y%m%dT%H%M%S\") + \"-\" + uuid.uuid4().hex[:6])\n"
                "            os.makedirs(ws, exist_ok=True)\n"
                "            stage = \"start\"\n"
                "            try:\n"
                "                stage = \"researcher\"; research = _InternalResearcher().perform(topic)\n"
                "                stage = \"writer\";     draft = _InternalWriter().perform(research)\n"
                "                stage = \"critic\";     v = _InternalCritic().verdict(draft)\n"
                "                if v[\"verdict\"] != \"ship\":  # the gate is real (rule 2)\n"
                "                    return json.dumps({\"status\": \"held\", \"reason\": v[\"note\"],\n"
                "                                       \"draft\": draft, \"workspace\": ws})\n"
                "                return json.dumps({\"status\": \"ok\", \"final\": draft, \"workspace\": ws})\n"
                "            except RuntimeError as e:  # errors are data (rule 1)\n"
                "                return json.dumps({\"status\": \"error\", \"failed_stage\": stage,\n"
                "                                   \"message\": str(e), \"workspace\": ws})"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["generate", "build", "list", "install", "uninstall"],
                        "description": "generate (design+persist a new agent), build (package locals into a singleton), list (browse store), install (pull from store), uninstall (remove)"
                    },
                    "swarm_name": {
                        "type": "string",
                        "description": "PascalCase name for the new agent/swarm (generate, build) OR the swarm id/name (install, uninstall). Example: 'NytSummarizer'"
                    },
                    "description": {
                        "type": "string",
                        "description": "One-line description of what this agent/swarm does. Used in the agent's manifest and in the LLM-facing description so the LLM knows when to call it."
                    },
                    "agent_code": {
                        "type": "string",
                        "description": "REQUIRED for 'generate'. Full Python source for the new agent, top to bottom — imports, __manifest__ dict, the BasicAgent subclass with __init__/metadata/perform. Will be syntax-checked and contract-checked before persistence."
                    },
                    "exclude": {
                        "type": "string",
                        "description": "For 'build' only: comma-separated agent names to exclude. Built-in memory/factory agents are excluded automatically."
                    }
                },
                "required": ["action"]
            }
        }
        super().__init__(self.name, self.metadata)

    def _fetch_catalog(self):
        req = urllib.request.Request(RAPP_STORE_CATALOG_URL,
                                     headers={"User-Agent": "RAPP-SwarmFactory/0.3"})
        resp = urllib.request.urlopen(req, timeout=10)
        return json.loads(resp.read().decode())

    def _list_swarms(self):
        cat = self._fetch_catalog()
        rapps = cat.get("rapplications", [])
        swarms = [r for r in rapps
                  if (r.get("produced_by", {}).get("source_files_collapsed", 0) > 1
                      and not r.get("egg_url"))]
        results = []
        for s in swarms:
            results.append({
                "id": s.get("id"),
                "name": s.get("display_name") or s.get("name") or s.get("id"),
                "description": s.get("description", ""),
                "version": s.get("version", ""),
                "agents_collapsed": s.get("produced_by", {}).get("source_files_collapsed", 0),
                "singleton_filename": s.get("singleton_filename", ""),
            })
        return json.dumps({
            "status": "ok",
            "action": "list",
            "swarms": results,
            "count": len(results),
            "message": f"Found {len(results)} swarm(s) in the RAPP Store.",
        })

    def _install_swarm(self, swarm_name):
        if not swarm_name:
            return json.dumps({"status": "error",
                               "message": "Provide swarm_name to install (e.g. 'bookfactory')."})
        agents_dir = os.environ.get("AGENTS_PATH",
                        os.path.join(os.path.dirname(os.path.abspath(__file__))))
        cat = self._fetch_catalog()
        rapps = cat.get("rapplications", [])
        lookup = swarm_name.lower().replace(" ", "").replace("-", "").replace("_", "")
        entry = None
        for r in rapps:
            rid = (r.get("id") or "").lower().replace("-", "").replace("_", "")
            rname = (r.get("display_name") or r.get("name") or "").lower().replace(" ", "").replace("-", "").replace("_", "")
            if lookup in (rid, rname):
                entry = r
                break
        if not entry:
            return json.dumps({"status": "error",
                               "message": f"Swarm '{swarm_name}' not found in the RAPP Store."})
        url = entry.get("singleton_url")
        fname = entry.get("singleton_filename")
        if not url or not fname:
            return json.dumps({"status": "error",
                               "message": f"Catalog entry for '{swarm_name}' is missing singleton_url or filename."})
        req = urllib.request.Request(url, headers={"User-Agent": "RAPP-SwarmFactory/0.3"})
        body = urllib.request.urlopen(req, timeout=15).read()
        dest = os.path.join(agents_dir, fname)
        os.makedirs(agents_dir, exist_ok=True)
        with open(dest, "wb") as f:
            f.write(body)
        return json.dumps({
            "status": "ok",
            "action": "install",
            "id": entry.get("id"),
            "filename": fname,
            "bytes": len(body),
            "destination": dest,
            "message": f"Installed '{entry.get('display_name') or entry.get('name') or entry.get('id')}' → agents/{fname} ({len(body)} bytes). It will load on the next request.",
        })

    def _generate_swarm(self, swarm_name, description, agent_code):
        # Validation gauntlet — refuse to write a file that won't load
        # cleanly. Every failure here returns a structured error the LLM
        # can read and retry with corrections, instead of "your agent
        # silently doesn't show up after restart" (the worst UX).
        if not swarm_name or not isinstance(swarm_name, str):
            return json.dumps({"status": "error",
                "message": "Provide swarm_name (PascalCase, e.g. 'NytSummarizer')."})
        if not agent_code or not isinstance(agent_code, str):
            return json.dumps({"status": "error",
                "message": "Provide agent_code — the full Python source for the new agent."})

        # Syntax check first — cheapest fail.
        try:
            tree = ast.parse(agent_code)
        except SyntaxError as e:
            return json.dumps({"status": "error",
                "message": f"agent_code has a SyntaxError on line {e.lineno}: {e.msg}",
                "lineno": e.lineno, "offset": e.offset})

        # Contract check: must define at least one class and a perform()
        # method on it. We don't enforce the BasicAgent base class via AST
        # because the import path could be aliased; the brainstem's loader
        # is the final word on whether it's a valid agent.
        classes = [n for n in tree.body if isinstance(n, ast.ClassDef)]
        if not classes:
            return json.dumps({"status": "error",
                "message": "agent_code defines no classes. The agent must be a class extending BasicAgent."})

        # Role boundary: SwarmFactory.generate is for CONVERGED SWARMS
        # (multi-persona composites — BookFactory pattern). Single-class
        # one-shot agents (fetch xkcd, roll dice) belong to LearnNew.create.
        # Refuse here so the LLM gets a clear pointer to the right tool
        # instead of silently producing a non-swarm via the swarm-shaped
        # path. The "swarm" name actually means something this way.
        if len(classes) < 2:
            return json.dumps({"status": "error",
                "message": (
                    "agent_code has only one class — that's a single-persona "
                    "agent, not a swarm. SwarmFactory.generate is for converged "
                    "multi-persona pipelines (BookFactory pattern: Writer→Editor"
                    "→CEO→Publisher→Reviewer all inlined). For a single one-shot "
                    "agent, call the LearnNew tool with action='create' instead."
                ),
                "hint": "If this really IS a multi-persona swarm, split the work "
                        "into _Internal<Role> classes (one per persona) plus one "
                        "public BasicAgent composite that orchestrates them.",
                "class_count": len(classes)})
        has_perform = any(
            isinstance(m, ast.FunctionDef) and m.name == "perform"
            for c in classes for m in c.body
        )
        if not has_perform:
            return json.dumps({"status": "error",
                "message": "No class defines perform(**kwargs). The brainstem won't know how to call this agent."})
        has_manifest = any(
            isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == "__manifest__" for t in n.targets)
            for n in tree.body
        )

        # Non-blocking lint against the hard rules — surfaced so the LLM
        # can self-correct on the next generate, but legacy-shaped code
        # still persists (graceful, not punitive).
        warnings = []
        if '"(LLM HTTP' in agent_code or "'(LLM HTTP" in agent_code:
            warnings.append(
                "legacy error-as-prose pattern detected ('(LLM HTTP ...' string). "
                "Hard rule 1: _post should RAISE after one retry; perform() catches "
                "once and returns a structured {'status':'error', 'failed_stage':...} report.")
        if "(no LLM configured" in agent_code and "raise" not in agent_code:
            warnings.append(
                "'(no LLM configured)' returned as a string. Hard rule 1: raise "
                "RuntimeError instead so the failure can't flow downstream as prose.")
        if "/tmp/" in agent_code and "uuid" not in agent_code and "strftime" not in agent_code:
            warnings.append(
                "fixed /tmp path with no per-run id — concurrent runs will clobber "
                "each other's artifacts. Hard rule 3: per-run subdir (timestamp+uuid).")

        # Auto-inject the BasicAgent import if the LLM forgot it. The agent
        # contract says the class must extend BasicAgent, and the brainstem
        # loader expects this exact import path, so it's a safe fix-up.
        if "from agents.basic_agent import BasicAgent" not in agent_code:
            agent_code = "from agents.basic_agent import BasicAgent\n" + agent_code

        # Filename derives from the swarm_name slug — same convention as
        # the rest of the agents/ directory so it shows up in /agents/full and the UI
        # agents grid without special-casing. Refuse to overwrite an
        # existing file: the LLM should pick a fresh name on collision,
        # not silently clobber the user's work.
        slug = re.sub(r'[^a-z0-9]', '', swarm_name.lower())
        if not slug:
            return json.dumps({"status": "error",
                "message": "swarm_name produced an empty slug after stripping non-alphanumerics. Use letters/digits."})
        agents_dir = os.environ.get("AGENTS_PATH",
                        os.path.join(os.path.dirname(os.path.abspath(__file__))))
        os.makedirs(agents_dir, exist_ok=True)
        fname = f"{slug}_agent.py"
        dest = os.path.join(agents_dir, fname)
        if os.path.exists(dest):
            return json.dumps({"status": "error",
                "message": f"agents/{fname} already exists. Pick a different swarm_name or call uninstall first."})

        with open(dest, "w") as f:
            f.write(agent_code)

        return json.dumps({
            "status": "ok",
            "action": "generate",
            "swarm_name": swarm_name,
            "filename": fname,
            "destination": dest,
            "bytes": len(agent_code),
            "lines": agent_code.count("\n") + 1,
            "has_manifest": has_manifest,
            "warnings": warnings,
            "message": (
                f"Generated agents/{fname} ({len(agent_code)} bytes). "
                f"It loads automatically on the next request — no restart needed. "
                f"Try calling it from chat to confirm."
                + (f" NOTE: {len(warnings)} hard-rule warning(s) — see 'warnings'." if warnings else "")
            ),
        })

    def _uninstall_swarm(self, swarm_name):
        if not swarm_name:
            return json.dumps({"status": "error",
                               "message": "Provide swarm_name to uninstall."})
        agents_dir = os.environ.get("AGENTS_PATH",
                        os.path.join(os.path.dirname(os.path.abspath(__file__))))
        lookup = swarm_name.lower().replace(" ", "").replace("-", "").replace("_", "")
        for fname in sorted(os.listdir(agents_dir)):
            if not fname.endswith("_agent.py") or fname == "basic_agent.py":
                continue
            stem = fname.replace("_agent.py", "").replace("-", "").replace("_", "")
            if stem == lookup:
                path = os.path.join(agents_dir, fname)
                os.remove(path)
                return json.dumps({
                    "status": "ok",
                    "action": "uninstall",
                    "removed": fname,
                    "message": f"Removed agents/{fname}. It will no longer load.",
                })
        return json.dumps({"status": "error",
                           "message": f"No installed agent matching '{swarm_name}' found."})

    def perform(self, action="build", swarm_name="MySwarm", description="", exclude="",
                agent_code="", **kwargs):
        if action == "generate":
            return self._generate_swarm(swarm_name, description, agent_code)
        if action == "list":
            return self._list_swarms()
        if action == "install":
            return self._install_swarm(swarm_name)
        if action == "uninstall":
            return self._uninstall_swarm(swarm_name)

        agents_dir = os.environ.get("AGENTS_PATH",
                        os.path.join(os.path.dirname(os.path.abspath(__file__))))

        auto_exclude = {"SwarmFactory", "BasicAgent", "SaveMemory", "RecallMemory"}
        user_exclude = set(x.strip() for x in exclude.split(",") if x.strip())
        skip = auto_exclude | user_exclude

        agent_files = sorted(glob.glob(os.path.join(agents_dir, "*_agent.py")))

        sources = {}
        for path in agent_files:
            fname = os.path.basename(path)
            if fname == "basic_agent.py":
                continue
            try:
                src = open(path).read()
                tree = ast.parse(src, filename=fname)
                classes = [n for n in tree.body if isinstance(n, ast.ClassDef)
                           and n.name != "BasicAgent"]
                if not classes:
                    continue
                cls_name = classes[0].name
                if cls_name in skip or cls_name.replace("Agent", "") in skip:
                    continue
                sources[fname] = {
                    "src": src,
                    "tree": tree,
                    "class_name": cls_name,
                    "path": path,
                }
            except Exception:
                continue

        if not sources:
            return json.dumps({"status": "error",
                               "message": "No eligible agents found to converge."})

        slug = re.sub(r'[^a-z0-9]', '', swarm_name.lower())
        public_name = re.sub(r'[^A-Za-z0-9]', '', swarm_name)
        if not public_name:
            public_name = "MySwarm"

        # Detect which agents import other agents (composites vs leaves)
        import_map = {}
        for fname, info in sources.items():
            imports = set()
            for node in info["tree"].body:
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    s = ast.get_source_segment(info["src"], node) or ""
                    for other_fname, other_info in sources.items():
                        if other_info["class_name"] in s:
                            imports.add(other_info["class_name"])
            import_map[fname] = imports

        leaves = [f for f in sources if not import_map[f]]
        composites = [f for f in sources if import_map[f]]

        # Build rename table
        renames = {}
        for fname, info in sources.items():
            cn = info["class_name"]
            base = cn.replace("Agent", "") if cn.endswith("Agent") else cn
            renames[cn] = f"_Internal{base}"

        # Extract SOUL constants and helper functions from each file
        all_souls = []
        has_llm_helper = False
        llm_helper_src = ""
        post_helper_src = ""

        for fname in leaves + composites:
            info = sources[fname]
            src = info["src"]
            tree = info["tree"]
            stem = os.path.splitext(fname)[0].replace("_agent", "").upper().replace("-", "_")

            for node in tree.body:
                if isinstance(node, ast.Assign):
                    for t in node.targets:
                        if isinstance(t, ast.Name) and t.id == "SOUL":
                            seg = ast.get_source_segment(src, node)
                            if seg:
                                renamed = re.sub(r'^SOUL\s*=', f'_SOUL_{stem} =', seg)
                                all_souls.append((stem, renamed))

            if not has_llm_helper:
                m_llm = re.search(
                    r'(def _llm_call\b.*?)(?=\n(?:def |class |__manifest__|\Z))',
                    src, re.DOTALL)
                m_post = re.search(
                    r'(def _post\b.*?)(?=\n(?:def |class |__manifest__|\Z))',
                    src, re.DOTALL)
                if m_llm:
                    llm_helper_src = m_llm.group(1).rstrip()
                    has_llm_helper = True
                if m_post:
                    post_helper_src = m_post.group(1).rstrip()

        # Extract standalone module-level constants (not SOUL, not __manifest__)
        extra_constants = []
        for fname in leaves + composites:
            info = sources[fname]
            for node in info["tree"].body:
                if isinstance(node, ast.Assign):
                    for t in node.targets:
                        if isinstance(t, ast.Name) and t.id not in (
                                "SOUL", "__manifest__", "metadata"):
                            seg = ast.get_source_segment(info["src"], node)
                            if seg and len(seg) < 5000:
                                extra_constants.append(seg)
                if isinstance(node, ast.Assert):
                    seg = ast.get_source_segment(info["src"], node)
                    if seg:
                        extra_constants.append(seg)

        # Extract standalone helper functions (not _llm_call, _post)
        extra_helpers = []
        for fname in leaves + composites:
            info = sources[fname]
            for node in info["tree"].body:
                if isinstance(node, ast.FunctionDef) and node.name not in (
                        "_llm_call", "_post", "perform"):
                    seg = ast.get_source_segment(info["src"], node)
                    if seg:
                        extra_helpers.append(seg)

        # Now build the singleton
        out = f'"""\n{slug}_agent.py — {public_name} singleton.\n\n'
        out += f'{description or "A converged RAPP swarm."}\n\n'
        out += 'Drop this file into any RAPP brainstem\'s agents/ directory and it works.\n'
        out += f'Generated by SwarmFactory from {len(sources)} source agents.\n\n'
        out += 'Inlined agents:\n'
        for fname, info in sources.items():
            out += f'  - {info["class_name"]}\n'
        out += '"""\n\n'
        out += 'from agents.basic_agent import BasicAgent\n'
        out += 'import json\nimport os\nimport re\nimport hashlib\n'
        out += 'import urllib.request\nimport urllib.error\n\n\n'

        delegates = [f'@rapp/{info["class_name"].replace("Agent","").lower()}'
                      for info in sources.values()]
        # The singleton's manifest carries the SWARM's own name — a built
        # artifact must never claim to be the factory that produced it.
        out += f'__manifest__ = {{\n'
        out += f'    "schema": "rapp-agent/1.0",\n'
        out += f'    "name": "@rapp/{slug}",\n'
        out += f'    "version": "0.1.0",\n'
        out += f'    "tags": ["composite", "singleton", "swarm-factory-generated"],\n'
        out += f'    "delegates_to_inlined": {json.dumps(delegates, indent=8)},\n'
        out += f'    "example_call": {{"args": {{}}}},\n'
        out += f'}}\n\n\n'

        # Constants
        if extra_constants:
            out += '# ─── Constants ─────────────────────────────────────────────────────────\n\n'
            for c in extra_constants:
                out += c + '\n\n'

        # SOULs
        if all_souls:
            out += '# ─── SOUL constants (verbatim from each agent) ─────────────────────────\n\n'
            for stem, soul_src in all_souls:
                out += soul_src + '\n\n'

        # Helper functions
        if extra_helpers:
            out += '# ─── Helper functions ──────────────────────────────────────────────────\n\n'
            for h in extra_helpers:
                out += h + '\n\n'

        # Internal classes — leaves first
        out += '# ─── Internal classes (prefixed _Internal to hide from discovery) ──────\n\n'
        for fname in leaves:
            info = sources[fname]
            cls_src = None
            for node in info["tree"].body:
                if isinstance(node, ast.ClassDef) and node.name == info["class_name"]:
                    cls_src = ast.get_source_segment(info["src"], node)
                    break
            if not cls_src:
                continue
            new = cls_src
            cn = info["class_name"]
            new = re.sub(rf'\bclass {re.escape(cn)}\b', f'class {renames[cn]}', new)
            stem = os.path.splitext(fname)[0].replace("_agent", "").upper().replace("-", "_")
            new = re.sub(r'\bSOUL\b', f'_SOUL_{stem}', new)
            out += new + '\n\n\n'

        # Internal classes — composites
        for fname in composites:
            info = sources[fname]
            cls_src = None
            for node in info["tree"].body:
                if isinstance(node, ast.ClassDef) and node.name == info["class_name"]:
                    cls_src = ast.get_source_segment(info["src"], node)
                    break
            if not cls_src:
                continue
            new = cls_src
            cn = info["class_name"]
            new = re.sub(rf'\bclass {re.escape(cn)}\b', f'class {renames[cn]}', new)
            for old_cn, new_cn in renames.items():
                if old_cn != cn:
                    new = re.sub(rf'\b{re.escape(old_cn)}\b', new_cn, new)
            out += new + '\n\n\n'

        # Public entrypoint — pick the top composite or first agent
        if composites:
            top_fname = composites[-1]
        else:
            top_fname = leaves[-1] if leaves else list(sources.keys())[-1]
        top_info = sources[top_fname]
        top_cls = top_info["class_name"]
        top_internal = renames[top_cls]

        out += '# ─── PUBLIC ENTRYPOINT ──────────────────────────────────────────────────\n\n'
        out += f'class {public_name}({top_internal}):\n'
        out += f'    def __init__(self):\n'
        out += f'        self.name = "{public_name}"\n'
        out += f'        self.metadata = {{\n'
        out += f'            "name": "{public_name}",\n'
        out += f'            "description": "{description or public_name + " swarm"}",\n'
        out += f'            "parameters": {json.dumps(top_info.get("metadata", {}).get("parameters", {"type": "object", "properties": {}, "required": []}))}\n'
        out += f'        }}\n'
        out += f'        super().__init__(self.name, self.metadata)\n\n\n'

        out += f'class {public_name}Agent({public_name}):\n'
        out += f'    pass\n\n\n'

        # LLM helpers
        if llm_helper_src:
            out += '# ─── Inlined LLM dispatch ──────────────────────────────────────────────\n\n'
            out += llm_helper_src + '\n\n\n'
        if post_helper_src:
            out += post_helper_src + '\n'

        # Write output
        output_fname = f"{slug}_agent.py"
        brainstem_dir = os.path.dirname(agents_dir)
        output_path = os.path.join(brainstem_dir, output_fname)
        with open(output_path, 'w') as f:
            f.write(out)

        n_lines = len(out.split('\n'))
        sha = hashlib.sha256(out.encode()).hexdigest()

        return json.dumps({
            "status": "ok",
            "swarm_name": public_name,
            "output_file": output_path,
            "filename": output_fname,
            "lines": n_lines,
            "bytes": len(out),
            "sha256": sha,
            "agents_collapsed": len(sources),
            "leaves": len(leaves),
            "composites": len(composites),
            "souls_inlined": len(all_souls),
            "message": (
                f"Converged {len(sources)} agents into {output_fname} "
                f"({n_lines} lines). The file is at {output_path} — "
                f"share it with anyone. They drop it in their brainstem's "
                f"agents/ dir and it works."
            ),
        })
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
