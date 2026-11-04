---
name: "rar-rapp-swarm-factory"
description: "Generate, build, install, list, and uninstall RAPP swarms.\n\nA SWARM is a multi-persona pipeline collapsed into ONE shareable agent file \u2014 like BookFactory (Writer\u2192Editor\u2192CEO\u2192Publisher\u2192Reviewer all inlined as _Internal* classes behind one public entrypoint). Each persona has its own SOUL/system prompt; deterministic Python in perform() orchestrates them \u2014 the LLM calls are leaf nodes, the control flow is code.\n\nROLE BOUNDARY:\n \u2022 Single one-shot agent (fetch xkcd, roll dice) \u2192 LearnNew with action='create'. Do NOT use SwarmFactory.\n \u2022 Multi-persona converged singleton (research\u2192write\u2192critique, write\u2192edit\u2192publish) \u2192 SwarmFactory.generate.\n \u2022 Existing multi-file agents to collapse into one shippable file \u2192 SwarmFactory.build.\n\nActions:\n \u2022 'generate' \u2014 Design a BRAND-NEW converged swarm. YOU (the LLM) compose the full Python source \u2014 multiple _Internal persona classes (each with its own SOUL) plus ONE public composite \u2014 and pass it as 'agent_code'. Hot-loads on the next request. If the request is single-persona, REFUSE and route to LearnNew.create.\n \u2022 'build' \u2014 Converge existing local agents into a singleton .py.\n \u2022 'list' / 'install' / 'uninstall' \u2014 RAPP Store catalog ops.\n\nHARD RULES for generated swarm code (each maps to a shipped pattern in @rarbookworld/bookfactory v0.4 \u2014 read it as the exemplar):\n 1. ERRORS ARE DATA, NEVER CONTENT. _post retries once on 429/5xx/network then RAISES RuntimeError. perform() wraps the pipeline in ONE try/except and returns json.dumps({'status':'error','failed_stage':...,'completed_stages':[...]}). NEVER return '(LLM HTTP ...)' strings \u2014 the next persona would edit the error as if it were prose and every downstream call burns on garbage.\n 2. GATES ACTUALLY GATE. When a persona renders a verdict (ship/hold, a score), obtain it via _llm_json (stdlib parse + required-keys check + one re-prompt-with-the-error) and BRANCH on it in code; honor 'hold' by halting with a partial report. Use _llm_json ONLY for verdict-shaped outputs \u2014 prose stages stay raw text (JSON-wrapping a draft corrupts code fences and voice).\n 3. PER-RUN WORKSPACE. Artifacts go under a fresh subdir per run (timestamp+uuid). The brainstem serves requests threaded; fixed paths make concurrent runs clobber each other.\n 4. STATIC BOUNDS. Every revision/retry cycle is capped by a hard-coded constant, and a run-scoped counter inside _llm_call refuses past _MAX_LLM_CALLS with a clear error. Refusal is a feature.\n 5. PARALLEL ONLY WHEN SAFE. If \u22652 stages consume the SAME input and NEITHER writes a shared memory GUID, you may inline a 6-line ThreadPoolExecutor helper (cap 3 branches). Personas sharing a memory GUID must stay sequential \u2014 the local storage shim has no file locking, so concurrent writers lose updates.\n 6. TIERING IS OPPORTUNISTIC. _llm_call(soul, prompt, tier=None); tier='small' reads AZURE_OPENAI_DEPLOYMENT_SMALL / OPENAI_MODEL_SMALL when set and silently falls back to the primary deployment. Never hard-code a literal model name \u2014 on Azure the 'model' is a per-tenant deployment name; a baked-in id 404s on every box but the author's.\n\nMemory architecture (each swarm picks its own):\nPersonas use AzureFileStorageManager().set_memory_context(<guid>) to read/write a NAMESPACED memory file. Strategies:\n \u2022 SHARED \u2014 one _SWARM_MEMORY_GUID = '<slug>-shared-v1' module constant; every persona uses it (researcher\u2192writer pipelines).\n \u2022 SEGMENTED \u2014 per-persona GUID constants (a critic that must review fresh, with no prior bias).\n \u2022 MIXED \u2014 shared GUID for coordinating personas, private for the isolated ones. \u2022 USER-SCOPED \u2014 pipe the caller's user_guid through.  \u2022 EPHEMERAL \u2014 don't import the storage manager at all.\nBake GUIDs as MODULE CONSTANTS at code-write time (deterministic and portable). Remember rule 5: shared-GUID personas never run in parallel.\n\nRequired shape for 'generate':\n    from agents.basic_agent import BasicAgent\n    import json, os, time, uuid, threading, urllib.request, urllib.error\n\n    __manifest__ = {\"schema\": \"rapp-agent/1.0\", \"name\": \"@user/<slug>\",\n                     \"version\": \"0.1.0\",\n                     \"tags\": [\"composite\", \"swarm-factory-generated\"],\n                     \"delegates_to_inlined\": [\"<persona1>\", \"<persona2>\"]}\n\n    _MAX_LLM_CALLS = 30   # static bound (rule 4)\n    _SOUL_RESEARCHER = \"You are a researcher...\"  # one SOUL per persona\n    _SOUL_WRITER     = \"You are a writer...\"\n    _SOUL_CRITIC     = \"You are a brutal critic...\"\n\n    _calls = {\"n\": 0}; _lock = threading.Lock()\n    def _llm_call(soul, prompt, tier=None):\n        with _lock:\n            _calls[\"n\"] += 1\n            if _calls[\"n\"] > _MAX_LLM_CALLS:\n                raise RuntimeError(f\"call budget exceeded ({_MAX_LLM_CALLS})\")\n        msgs = [{\"role\": \"system\", \"content\": soul},\n                {\"role\": \"user\", \"content\": prompt}]\n        ep, key = os.environ.get(\"AZURE_OPENAI_ENDPOINT\", \"\"),\\\n                  os.environ.get(\"AZURE_OPENAI_API_KEY\", \"\")\n        dep = os.environ.get(\"AZURE_OPENAI_DEPLOYMENT\", \"\")\n        if tier == \"small\":\n            dep = os.environ.get(\"AZURE_OPENAI_DEPLOYMENT_SMALL\") or dep  # graceful fallback (rule 6)\n        if ep and key:\n            url = ep.rstrip(\"/\") + f\"/openai/deployments/{dep}/chat/completions?api-version=2025-01-01-preview\"\n            return _post(url, {\"messages\": msgs, \"model\": dep},\n                          {\"Content-Type\": \"application/json\", \"api-key\": key})\n        if os.environ.get(\"OPENAI_API_KEY\"):\n            m = os.environ.get(\"OPENAI_MODEL\", \"gpt-4o\")\n            if tier == \"small\": m = os.environ.get(\"OPENAI_MODEL_SMALL\") or m\n            return _post(\"https://api.openai.com/v1/chat/completions\",\n                          {\"model\": m, \"messages\": msgs},\n                          {\"Content-Type\": \"application/json\",\n                           \"Authorization\": \"Bearer \" + os.environ[\"OPENAI_API_KEY\"]})\n        raise RuntimeError(\"no LLM configured\")  # raise \u2014 never return error text (rule 1)\n\n    def _post(url, body, headers):\n        for attempt in (1, 2):\n            req = urllib.request.Request(url, data=json.dumps(body).encode(\"utf-8\"),\n                                          headers=headers, method=\"POST\")\n            try:\n                with urllib.request.urlopen(req, timeout=120) as r:\n                    c = json.loads(r.read().decode(\"utf-8\")).get(\"choices\") or []\n                return (c[0][\"message\"].get(\"content\") or \"\") if c else \"\"\n            except urllib.error.HTTPError as e:\n                if (e.code == 429 or e.code >= 500) and attempt == 1:\n                    time.sleep(2); continue\n                raise RuntimeError(f\"LLM HTTP {e.code}\")\n            except urllib.error.URLError as e:\n                if attempt == 1: time.sleep(2); continue\n                raise RuntimeError(f\"LLM network error: {e}\")\n\n    def _llm_json(soul, prompt, required_keys, retries=1):  # verdicts ONLY (rule 2)\n        err = \"\"\n        for _ in range(retries + 1):\n            nudge = f\"\\nPrevious reply invalid ({err}); reply with ONLY the JSON object.\" if err else \"\"\n            raw = _llm_call(soul, prompt + \"\\nReply with ONLY a JSON object with keys: \"\n                            + \", \".join(required_keys) + nudge)\n            s, e = raw.find(\"{\"), raw.rfind(\"}\")\n            try:\n                obj = json.loads(raw[s:e + 1])\n            except ValueError as ex:\n                err = str(ex); continue\n            if all(k in obj for k in required_keys):\n                return obj\n            err = \"missing keys\"\n        raise RuntimeError(\"structured handoff failed: \" + err)\n\n    # _Internal prefix keeps personas out of *Agent auto-discovery.\n    class _InternalResearcher:\n        def perform(self, topic): return _llm_call(_SOUL_RESEARCHER, topic)\n    class _InternalWriter:\n        def perform(self, research): return _llm_call(_SOUL_WRITER, research)\n    class _InternalCritic:  # renders a verdict the orchestrator branches on\n        def verdict(self, draft):\n            return _llm_json(_SOUL_CRITIC, \"Judge this draft:\\n\" + draft +\n                '\\n\"verdict\" is \"ship\" or \"revise\"; \"note\" is one sentence.',\n                [\"verdict\", \"note\"])\n\n    class <PascalCase>Agent(BasicAgent):\n        def __init__(self):\n            self.name = \"<PascalCase>\"\n            self.metadata = {\"name\": \"<PascalCase>\",\n                             \"description\": \"<what the swarm does \u2014 one line>\",\n                             \"parameters\": {\"type\": \"object\",\n                                            \"properties\": {\"topic\": {\"type\": \"string\"}},\n                                            \"required\": [\"topic\"]}}\n            super().__init__(self.name, self.metadata)\n        def perform(self, topic=\"\", **kwargs):\n            ws = os.path.join(\"/tmp/<slug>\",  # per-run dir (rule 3)\n                              time.strftime(\"%Y%m%dT%H%M%S\") + \"-\" + uuid.uuid4().hex[:6])\n            os.makedirs(ws, exist_ok=True)\n            stage = \"start\"\n            try:\n                stage = \"researcher\"; research = _InternalResearcher().perform(topic)\n                stage = \"writer\";     draft = _InternalWriter().perform(research)\n                stage = \"critic\";     v = _InternalCritic().verdict(draft)\n                if v[\"verdict\"] != \"ship\":  # the gate is real (rule 2)\n                    return json.dumps({\"status\": \"held\", \"reason\": v[\"note\"],\n                                       \"draft\": draft, \"workspace\": ws})\n                return json.dumps({\"status\": \"ok\", \"final\": draft, \"workspace\": ws})\n            except RuntimeError as e:  # errors are data (rule 1)\n                return json.dumps({\"status\": \"error\", \"failed_stage\": stage,\n                                   \"message\": str(e), \"workspace\": ws})"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/swarm_factory_agent", "rar_sha256": "54ef914e46c15b4127235a1e17dd3a1d0257fbae0f9cede71a33173d52da4d93", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "0.3.1", "author": "RAPP", "tags": ["meta", "build", "singleton", "swarm-factory", "store"]}
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
