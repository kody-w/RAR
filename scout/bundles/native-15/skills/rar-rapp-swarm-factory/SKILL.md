---
name: "rar-rapp-swarm-factory"
description: "Generate, build, install, list, and uninstall RAPP swarms.\n\nA SWARM is a multi-persona pipeline collapsed into ONE shareable agent file \u2014 like BookFactory (Writer\u2192Editor\u2192CEO\u2192Publisher\u2192Reviewer all inlined as _Internal* classes behind one public entrypoint). Each persona has its own SOUL/system prompt; deterministic Python in perform() orchestrates them \u2014 the LLM calls are leaf nodes, the control flow is code.\n\nROLE BOUNDARY:\n \u2022 Single one-shot agent (fetch xkcd, roll dice) \u2192 LearnNew with action='create'. Do NOT use SwarmFactory.\n \u2022 Multi-persona converged singleton (research\u2192write\u2192critique, write\u2192edit\u2192publish) \u2192 SwarmFactory.generate.\n \u2022 Existing multi-file agents to collapse into one shippable file \u2192 SwarmFactory.build.\n\nActions:\n \u2022 'generate' \u2014 Design a BRAND-NEW converged swarm. YOU (the LLM) compose the full Python source \u2014 multiple _Internal persona classes (each with its own SOUL) plus ONE public composite \u2014 and pass it as 'agent_code'. Hot-loads on the next request. If the request is single-persona, REFUSE and route to LearnNew.create.\n \u2022 'build' \u2014 Converge existing local agents into a singleton .py.\n \u2022 'list' / 'install' / 'uninstall' \u2014 RAPP Store catalog ops.\n\nHARD RULES for generated swarm code (each maps to a shipped pattern in @rarbookworld/bookfactory v0.4 \u2014 read it as the exemplar):\n 1. ERRORS ARE DATA, NEVER CONTENT. _post retries once on 429/5xx/network then RAISES RuntimeError. perform() wraps the pipeline in ONE try/except and returns json.dumps({'status':'error','failed_stage':...,'completed_stages':[...]}). NEVER return '(LLM HTTP ...)' strings \u2014 the next persona would edit the error as if it were prose and every downstream call burns on garbage.\n 2. GATES ACTUALLY GATE. When a persona renders a verdict (ship/hold, a score), obtain it via _llm_json (stdlib parse + required-keys check + one re-prompt-with-the-error) and BRANCH on it in code; honor 'hold' by halting with a partial report. Use _llm_json ONLY for verdict-shaped outputs \u2014 prose stages stay raw text (JSON-wrapping a draft corrupts code fences and voice).\n 3. PER-RUN WORKSPACE. Artifacts go under a fresh subdir per run (timestamp+uuid). The brainstem serves requests threaded; fixed paths make concurrent runs clobber each other.\n 4. STATIC BOUNDS. Every revision/retry cycle is capped by a hard-coded constant, and a run-scoped counter inside _llm_call refuses past _MAX_LLM_CALLS with a clear error. Refusal is a feature.\n 5. PARALLEL ONLY WHEN SAFE. If \u22652 stages consume the SAME input and NEITHER writes a shared memory GUID, you may inline a 6-line ThreadPoolExecutor helper (cap 3 branches). Personas sharing a memory GUID must stay sequential \u2014 the local storage shim has no file locking, so concurrent writers lose updates.\n 6. TIERING IS OPPORTUNISTIC. _llm_call(soul, prompt, tier=None); tier='small' reads AZURE_OPENAI_DEPLOYMENT_SMALL / OPENAI_MODEL_SMALL when set and silently falls back to the primary deployment. Never hard-code a literal model name \u2014 on Azure the 'model' is a per-tenant deployment name; a baked-in id 404s on every box but the author's.\n\nMemory architecture (each swarm picks its own):\nPersonas use AzureFileStorageManager().set_memory_context(<guid>) to read/write a NAMESPACED memory file. Strategies:\n \u2022 SHARED \u2014 one _SWARM_MEMORY_GUID = '<slug>-shared-v1' module constant; every persona uses it (researcher\u2192writer pipelines).\n \u2022 SEGMENTED \u2014 per-persona GUID constants (a critic that must review fresh, with no prior bias).\n \u2022 MIXED \u2014 shared GUID for coordinating personas, private for the isolated ones. \u2022 USER-SCOPED \u2014 pipe the caller's user_guid through.  \u2022 EPHEMERAL \u2014 don't import the storage manager at all.\nBake GUIDs as MODULE CONSTANTS at code-write time (deterministic and portable). Remember rule 5: shared-GUID personas never run in parallel.\n\nRequired shape for 'generate':\n    from agents.basic_agent import BasicAgent\n    import json, os, time, uuid, threading, urllib.request, urllib.error\n\n    __manifest__ = {\"schema\": \"rapp-agent/1.0\", \"name\": \"@user/<slug>\",\n                     \"version\": \"0.1.0\",\n                     \"tags\": [\"composite\", \"swarm-factory-generated\"],\n                     \"delegates_to_inlined\": [\"<persona1>\", \"<persona2>\"]}\n\n    _MAX_LLM_CALLS = 30   # static bound (rule 4)\n    _SOUL_RESEARCHER = \"You are a researcher...\"  # one SOUL per persona\n    _SOUL_WRITER     = \"You are a writer...\"\n    _SOUL_CRITIC     = \"You are a brutal critic...\"\n\n    _calls = {\"n\": 0}; _lock = threading.Lock()\n    def _llm_call(soul, prompt, tier=None):\n        with _lock:\n            _calls[\"n\"] += 1\n            if _calls[\"n\"] > _MAX_LLM_CALLS:\n                raise RuntimeError(f\"call budget exceeded ({_MAX_LLM_CALLS})\")\n        msgs = [{\"role\": \"system\", \"content\": soul},\n                {\"role\": \"user\", \"content\": prompt}]\n        ep, key = os.environ.get(\"AZURE_OPENAI_ENDPOINT\", \"\"),\\\n                  os.environ.get(\"AZURE_OPENAI_API_KEY\", \"\")\n        dep = os.environ.get(\"AZURE_OPENAI_DEPLOYMENT\", \"\")\n        if tier == \"small\":\n            dep = os.environ.get(\"AZURE_OPENAI_DEPLOYMENT_SMALL\") or dep  # graceful fallback (rule 6)\n        if ep and key:\n            url = ep.rstrip(\"/\") + f\"/openai/deployments/{dep}/chat/completions?api-version=2025-01-01-preview\"\n            return _post(url, {\"messages\": msgs, \"model\": dep},\n                          {\"Content-Type\": \"application/json\", \"api-key\": key})\n        if os.environ.get(\"OPENAI_API_KEY\"):\n            m = os.environ.get(\"OPENAI_MODEL\", \"gpt-4o\")\n            if tier == \"small\": m = os.environ.get(\"OPENAI_MODEL_SMALL\") or m\n            return _post(\"https://api.openai.com/v1/chat/completions\",\n                          {\"model\": m, \"messages\": msgs},\n                          {\"Content-Type\": \"application/json\",\n                           \"Authorization\": \"Bearer \" + os.environ[\"OPENAI_API_KEY\"]})\n        raise RuntimeError(\"no LLM configured\")  # raise \u2014 never return error text (rule 1)\n\n    def _post(url, body, headers):\n        for attempt in (1, 2):\n            req = urllib.request.Request(url, data=json.dumps(body).encode(\"utf-8\"),\n                                          headers=headers, method=\"POST\")\n            try:\n                with urllib.request.urlopen(req, timeout=120) as r:\n                    c = json.loads(r.read().decode(\"utf-8\")).get(\"choices\") or []\n                return (c[0][\"message\"].get(\"content\") or \"\") if c else \"\"\n            except urllib.error.HTTPError as e:\n                if (e.code == 429 or e.code >= 500) and attempt == 1:\n                    time.sleep(2); continue\n                raise RuntimeError(f\"LLM HTTP {e.code}\")\n            except urllib.error.URLError as e:\n                if attempt == 1: time.sleep(2); continue\n                raise RuntimeError(f\"LLM network error: {e}\")\n\n    def _llm_json(soul, prompt, required_keys, retries=1):  # verdicts ONLY (rule 2)\n        err = \"\"\n        for _ in range(retries + 1):\n            nudge = f\"\\nPrevious reply invalid ({err}); reply with ONLY the JSON object.\" if err else \"\"\n            raw = _llm_call(soul, prompt + \"\\nReply with ONLY a JSON object with keys: \"\n                            + \", \".join(required_keys) + nudge)\n            s, e = raw.find(\"{\"), raw.rfind(\"}\")\n            try:\n                obj = json.loads(raw[s:e + 1])\n            except ValueError as ex:\n                err = str(ex); continue\n            if all(k in obj for k in required_keys):\n                return obj\n            err = \"missing keys\"\n        raise RuntimeError(\"structured handoff failed: \" + err)\n\n    # _Internal prefix keeps personas out of *Agent auto-discovery.\n    class _InternalResearcher:\n        def perform(self, topic): return _llm_call(_SOUL_RESEARCHER, topic)\n    class _InternalWriter:\n        def perform(self, research): return _llm_call(_SOUL_WRITER, research)\n    class _InternalCritic:  # renders a verdict the orchestrator branches on\n        def verdict(self, draft):\n            return _llm_json(_SOUL_CRITIC, \"Judge this draft:\\n\" + draft +\n                '\\n\"verdict\" is \"ship\" or \"revise\"; \"note\" is one sentence.',\n                [\"verdict\", \"note\"])\n\n    class <PascalCase>Agent(BasicAgent):\n        def __init__(self):\n            self.name = \"<PascalCase>\"\n            self.metadata = {\"name\": \"<PascalCase>\",\n                             \"description\": \"<what the swarm does \u2014 one line>\",\n                             \"parameters\": {\"type\": \"object\",\n                                            \"properties\": {\"topic\": {\"type\": \"string\"}},\n                                            \"required\": [\"topic\"]}}\n            super().__init__(self.name, self.metadata)\n        def perform(self, topic=\"\", **kwargs):\n            ws = os.path.join(\"/tmp/<slug>\",  # per-run dir (rule 3)\n                              time.strftime(\"%Y%m%dT%H%M%S\") + \"-\" + uuid.uuid4().hex[:6])\n            os.makedirs(ws, exist_ok=True)\n            stage = \"start\"\n            try:\n                stage = \"researcher\"; research = _InternalResearcher().perform(topic)\n                stage = \"writer\";     draft = _InternalWriter().perform(research)\n                stage = \"critic\";     v = _InternalCritic().verdict(draft)\n                if v[\"verdict\"] != \"ship\":  # the gate is real (rule 2)\n                    return json.dumps({\"status\": \"held\", \"reason\": v[\"note\"],\n                                       \"draft\": draft, \"workspace\": ws})\n                return json.dumps({\"status\": \"ok\", \"final\": draft, \"workspace\": ws})\n            except RuntimeError as e:  # errors are data (rule 1)\n                return json.dumps({\"status\": \"error\", \"failed_stage\": stage,\n                                   \"message\": str(e), \"workspace\": ws})"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/swarm_factory_agent", "rar_sha256": "cfe3a0cffffb9d6395bf3d9377239e24500d3f7ab23c00b059da62f16a529ae0", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "0.3.1", "author": "RAPP", "tags": ["meta", "build", "singleton", "swarm-factory", "store"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/swarm_factory_agent`. The original RAPP
agent is preserved byte-for-byte in `swarm_factory_agent.py` and in the RCI capsule.

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
