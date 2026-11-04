---
name: "rar-rapp-swarm-factory"
description: "Generate, build, install, list, and uninstall RAPP swarms.\n\nA SWARM is a multi-persona pipeline collapsed into ONE shareable agent file \u2014 like BookFactory (Writer\u2192Editor\u2192CEO\u2192Publisher\u2192Reviewer all inlined as _Internal* classes behind one public entrypoint). Each persona has its own SOUL/system prompt; deterministic Python in perform() orchestrates them \u2014 the LLM calls are leaf nodes, the control flow is code.\n\nROLE BOUNDARY:\n \u2022 Single one-shot agent (fetch xkcd, roll dice) \u2192 LearnNew with action='create'. Do NOT use SwarmFactory.\n \u2022 Multi-persona converged singleton (research\u2192write\u2192critique, write\u2192edit\u2192publish) \u2192 SwarmFactory.generate.\n \u2022 Existing multi-file agents to collapse into one shippable file \u2192 SwarmFactory.build.\n\nActions:\n \u2022 'generate' \u2014 Design a BRAND-NEW converged swarm. YOU (the LLM) compose the full Python source \u2014 multiple _Internal persona classes (each with its own SOUL) plus ONE public composite \u2014 and pass it as 'agent_code'. Hot-loads on the next request. If the request is single-persona, REFUSE and route to LearnNew.create.\n \u2022 'build' \u2014 Converge existing local agents into a singleton .py.\n \u2022 'list' / 'install' / 'uninstall' \u2014 RAPP Store catalog ops.\n\nHARD RULES for generated swarm code (each maps to a shipped pattern in @rarbookworld/bookfactory v0.4 \u2014 read it as the exemplar):\n 1. ERRORS ARE DATA, NEVER CONTENT. _post retries once on 429/5xx/network then RAISES RuntimeError. perform() wraps the pipeline in ONE try/except and returns json.dumps({'status':'error','failed_stage':...,'completed_stages':[...]}). NEVER return '(LLM HTTP ...)' strings \u2014 the next persona would edit the error as if it were prose and every downstream call burns on garbage.\n 2. GATES ACTUALLY GATE. When a persona renders a verdict (ship/hold, a score), obtain it via _llm_json (stdlib parse + required-keys check + one re-prompt-with-the-error) and BRANCH on it in code; honor 'hold' by halting with a partial report. Use _llm_json ONLY for verdict-shaped outputs \u2014 prose stages stay raw text (JSON-wrapping a draft corrupts code fences and voice).\n 3. PER-RUN WORKSPACE. Artifacts go under a fresh subdir per run (timestamp+uuid). The brainstem serves requests threaded; fixed paths make concurrent runs clobber each other.\n 4. STATIC BOUNDS. Every revision/retry cycle is capped by a hard-coded constant, and a run-scoped counter inside _llm_call refuses past _MAX_LLM_CALLS with a clear error. Refusal is a feature.\n 5. PARALLEL ONLY WHEN SAFE. If \u22652 stages consume the SAME input and NEITHER writes a shared memory GUID, you may inline a 6-line ThreadPoolExecutor helper (cap 3 branches). Personas sharing a memory GUID must stay sequential \u2014 the local storage shim has no file locking, so concurrent writers lose updates.\n 6. TIERING IS OPPORTUNISTIC. _llm_call(soul, prompt, tier=None); tier='small' reads AZURE_OPENAI_DEPLOYMENT_SMALL / OPENAI_MODEL_SMALL when set and silently falls back to the primary deployment. Never hard-code a literal model name \u2014 on Azure the 'model' is a per-tenant deployment name; a baked-in id 404s on every box but the author's.\n\nMemory architecture (each swarm picks its own):\nPersonas use AzureFileStorageManager().set_memory_context(<guid>) to read/write a NAMESPACED memory file. Strategies:\n \u2022 SHARED \u2014 one _SWARM_MEMORY_GUID = '<slug>-shared-v1' module constant; every persona uses it (researcher\u2192writer pipelines).\n \u2022 SEGMENTED \u2014 per-persona GUID constants (a critic that must review fresh, with no prior bias).\n \u2022 MIXED \u2014 shared GUID for coordinating personas, private for the isolated ones. \u2022 USER-SCOPED \u2014 pipe the caller's user_guid through.  \u2022 EPHEMERAL \u2014 don't import the storage manager at all.\nBake GUIDs as MODULE CONSTANTS at code-write time (deterministic and portable). Remember rule 5: shared-GUID personas never run in parallel.\n\nRequired shape for 'generate':\n    from agents.basic_agent import BasicAgent\n    import json, os, time, uuid, threading, urllib.request, urllib.error\n\n    __manifest__ = {\"schema\": \"rapp-agent/1.0\", \"name\": \"@user/<slug>\",\n                     \"version\": \"0.1.0\",\n                     \"tags\": [\"composite\", \"swarm-factory-generated\"],\n                     \"delegates_to_inlined\": [\"<persona1>\", \"<persona2>\"]}\n\n    _MAX_LLM_CALLS = 30   # static bound (rule 4)\n    _SOUL_RESEARCHER = \"You are a researcher...\"  # one SOUL per persona\n    _SOUL_WRITER     = \"You are a writer...\"\n    _SOUL_CRITIC     = \"You are a brutal critic...\"\n\n    _calls = {\"n\": 0}; _lock = threading.Lock()\n    def _llm_call(soul, prompt, tier=None):\n        with _lock:\n            _calls[\"n\"] += 1\n            if _calls[\"n\"] > _MAX_LLM_CALLS:\n                raise RuntimeError(f\"call budget exceeded ({_MAX_LLM_CALLS})\")\n        msgs = [{\"role\": \"system\", \"content\": soul},\n                {\"role\": \"user\", \"content\": prompt}]\n        ep, key = os.environ.get(\"AZURE_OPENAI_ENDPOINT\", \"\"),\\\n                  os.environ.get(\"AZURE_OPENAI_API_KEY\", \"\")\n        dep = os.environ.get(\"AZURE_OPENAI_DEPLOYMENT\", \"\")\n        if tier == \"small\":\n            dep = os.environ.get(\"AZURE_OPENAI_DEPLOYMENT_SMALL\") or dep  # graceful fallback (rule 6)\n        if ep and key:\n            url = ep.rstrip(\"/\") + f\"/openai/deployments/{dep}/chat/completions?api-version=2025-01-01-preview\"\n            return _post(url, {\"messages\": msgs, \"model\": dep},\n                          {\"Content-Type\": \"application/json\", \"api-key\": key})\n        if os.environ.get(\"OPENAI_API_KEY\"):\n            m = os.environ.get(\"OPENAI_MODEL\", \"gpt-4o\")\n            if tier == \"small\": m = os.environ.get(\"OPENAI_MODEL_SMALL\") or m\n            return _post(\"https://api.openai.com/v1/chat/completions\",\n                          {\"model\": m, \"messages\": msgs},\n                          {\"Content-Type\": \"application/json\",\n                           \"Authorization\": \"Bearer \" + os.environ[\"OPENAI_API_KEY\"]})\n        raise RuntimeError(\"no LLM configured\")  # raise \u2014 never return error text (rule 1)\n\n    def _post(url, body, headers):\n        for attempt in (1, 2):\n            req = urllib.request.Request(url, data=json.dumps(body).encode(\"utf-8\"),\n                                          headers=headers, method=\"POST\")\n            try:\n                with urllib.request.urlopen(req, timeout=120) as r:\n                    c = json.loads(r.read().decode(\"utf-8\")).get(\"choices\") or []\n                return (c[0][\"message\"].get(\"content\") or \"\") if c else \"\"\n            except urllib.error.HTTPError as e:\n                if (e.code == 429 or e.code >= 500) and attempt == 1:\n                    time.sleep(2); continue\n                raise RuntimeError(f\"LLM HTTP {e.code}\")\n            except urllib.error.URLError as e:\n                if attempt == 1: time.sleep(2); continue\n                raise RuntimeError(f\"LLM network error: {e}\")\n\n    def _llm_json(soul, prompt, required_keys, retries=1):  # verdicts ONLY (rule 2)\n        err = \"\"\n        for _ in range(retries + 1):\n            nudge = f\"\\nPrevious reply invalid ({err}); reply with ONLY the JSON object.\" if err else \"\"\n            raw = _llm_call(soul, prompt + \"\\nReply with ONLY a JSON object with keys: \"\n                            + \", \".join(required_keys) + nudge)\n            s, e = raw.find(\"{\"), raw.rfind(\"}\")\n            try:\n                obj = json.loads(raw[s:e + 1])\n            except ValueError as ex:\n                err = str(ex); continue\n            if all(k in obj for k in required_keys):\n                return obj\n            err = \"missing keys\"\n        raise RuntimeError(\"structured handoff failed: \" + err)\n\n    # _Internal prefix keeps personas out of *Agent auto-discovery.\n    class _InternalResearcher:\n        def perform(self, topic): return _llm_call(_SOUL_RESEARCHER, topic)\n    class _InternalWriter:\n        def perform(self, research): return _llm_call(_SOUL_WRITER, research)\n    class _InternalCritic:  # renders a verdict the orchestrator branches on\n        def verdict(self, draft):\n            return _llm_json(_SOUL_CRITIC, \"Judge this draft:\\n\" + draft +\n                '\\n\"verdict\" is \"ship\" or \"revise\"; \"note\" is one sentence.',\n                [\"verdict\", \"note\"])\n\n    class <PascalCase>Agent(BasicAgent):\n        def __init__(self):\n            self.name = \"<PascalCase>\"\n            self.metadata = {\"name\": \"<PascalCase>\",\n                             \"description\": \"<what the swarm does \u2014 one line>\",\n                             \"parameters\": {\"type\": \"object\",\n                                            \"properties\": {\"topic\": {\"type\": \"string\"}},\n                                            \"required\": [\"topic\"]}}\n            super().__init__(self.name, self.metadata)\n        def perform(self, topic=\"\", **kwargs):\n            ws = os.path.join(\"/tmp/<slug>\",  # per-run dir (rule 3)\n                              time.strftime(\"%Y%m%dT%H%M%S\") + \"-\" + uuid.uuid4().hex[:6])\n            os.makedirs(ws, exist_ok=True)\n            stage = \"start\"\n            try:\n                stage = \"researcher\"; research = _InternalResearcher().perform(topic)\n                stage = \"writer\";     draft = _InternalWriter().perform(research)\n                stage = \"critic\";     v = _InternalCritic().verdict(draft)\n                if v[\"verdict\"] != \"ship\":  # the gate is real (rule 2)\n                    return json.dumps({\"status\": \"held\", \"reason\": v[\"note\"],\n                                       \"draft\": draft, \"workspace\": ws})\n                return json.dumps({\"status\": \"ok\", \"final\": draft, \"workspace\": ws})\n            except RuntimeError as e:  # errors are data (rule 1)\n                return json.dumps({\"status\": \"error\", \"failed_stage\": stage,\n                                   \"message\": str(e), \"workspace\": ws})"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/swarm_factory_agent", "rar_sha256": "54ef914e46c15b4127235a1e17dd3a1d0257fbae0f9cede71a33173d52da4d93", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "0.3.1", "author": "RAPP", "tags": ["meta", "build", "singleton", "swarm-factory", "store"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `swarm_factory_agent.py` and embedded as the fenced Python below (sha256 54ef914e46c15b41…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `swarm_factory_agent.py` first:

```bash
python3 swarm_factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 swarm_factory_agent.py   # or on stdin
python3 swarm_factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/swarm_factory_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/swarm_factory_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/swarm_factory_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
