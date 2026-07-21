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
