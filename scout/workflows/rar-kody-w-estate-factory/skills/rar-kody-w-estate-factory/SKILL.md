---
name: "rar-kody-w-estate-factory"
description: "Generate a full functioning digital estate from intent.\n\nEstate types (classical 1-5):\n  1 - Sanctum (identity, memory, twins)\n  2 - Polity  (governance, decisions, scenarios)\n  3 - Works   (production, content, code, ops)\n  4 - Press   (judgment, publication, analytics)\n  5 - Commons (federation, peer exchange)\n\nActions:\n  design    - preview the estate tree (no writes)\n  generate  - write the estate to ~/.rapp/estates/<name>/\n  provision - prepare the dashboard + register rappids\n  tour      - describe an existing estate\n  list      - all estates on this box"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/estate_factory", "rar_sha256": "46b070177e96da94f21bacbd45bfb0fa19f01d9aa79af7727bf1ff8aadd8e7b3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "0.1.2", "author": "kody-w", "tags": ["meta", "factory", "estate", "scaffolding", "rapplication", "singleton"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/estate_factory`. The original RAPP
agent is preserved byte-for-byte in `estate_factory_agent.py` and in the RCI capsule.

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

estate_factory_agent.py — generate a FULL functioning digital estate
from intent. One drop-in agent.py.

You describe what you need ("I want an estate that writes a daily blog and
ships podcast scripts") and the EstateFactory:

  1. Picks (or accepts) the estate TYPE — 1st through 5th — using the
     classical estates framing applied to digital labor.
  2. Designs the org chart: industries → neighborhoods → factories.
  3. Writes every file the estate needs to live: rappid.json, estate.json,
     factory_agent.py stubs (one per factory), soul.md per persona,
     estate.html dashboard, README.md, .gitignore.
  4. Optionally provisions: registers rappids in ~/.rapp/pids/ and
     prints the kill switch.

Estate types
============

  1st — The Sanctum     identity, memory, twins, soul-keeping
  2nd — The Polity      governance, decisions, constitution, scenarios
  3rd — The Works       production, labor, content/code/ops
  4th — The Press       observation, judgment, publication, critique
  5th — The Commons     federation, cross-estate exchange, public square

Each type ships with a default template tree. The architect persona will
extend the template based on the user's intent — adding industries,
naming neighborhoods, and specifying factory souls.

API
===

  EstateFactory(action="design",   intent="I want X")           # preview
  EstateFactory(action="generate", intent="...", name="kody")   # write
  EstateFactory(action="provision", name="kody")                # start it
  EstateFactory(action="tour",     name="kody")                 # describe
  EstateFactory(action="list")                                  # all estates

Workspace
=========

  ~/.rapp/estates/<slug>/
    rappid.json                       — permanent UUIDv4 identity
    estate.json                       — the tree (industries→neighborhoods→factories)
    estate.html                       — drill-down dashboard
    README.md                         — generated walkthrough
    industries/<industry>/
      <neighborhood>/
        <factory>/
          agent.py                    — factory_agent.py for this factory
          souls/<persona>.md          — one soul file per inlined persona
          manifest.json               — capabilities, port-on-provision

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "design",
        "generate",
        "provision",
        "tour",
        "list"
      ],
      "type": "string"
    },
    "intent": {
      "description": "What the user wants the estate to do. Required for design + generate.",
      "type": "string"
    },
    "name": {
      "description": "Slug for the estate. Required for generate/provision/tour.",
      "type": "string"
    },
    "type": {
      "description": "Estate type 1-5. Optional; inferred from intent if omitted.",
      "maximum": 5,
      "minimum": 1,
      "type": "integer"
    },
    "write_souls": {
      "description": "On generate, also call the SoulWriter persona to produce real soul prompts (slower; cheap mode skips this and uses placeholders).",
      "type": "boolean"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `estate_factory_agent.py` and embedded as the fenced Python below (sha256 46b070177e96da94…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `estate_factory_agent.py` first:

```bash
python3 estate_factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 estate_factory_agent.py   # or on stdin
python3 estate_factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/estate_factory_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/estate_factory_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/estate_factory/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""estate_factory_agent.py — generate a FULL functioning digital estate
from intent. One drop-in agent.py.

You describe what you need ("I want an estate that writes a daily blog and
ships podcast scripts") and the EstateFactory:

  1. Picks (or accepts) the estate TYPE — 1st through 5th — using the
     classical estates framing applied to digital labor.
  2. Designs the org chart: industries → neighborhoods → factories.
  3. Writes every file the estate needs to live: rappid.json, estate.json,
     factory_agent.py stubs (one per factory), soul.md per persona,
     estate.html dashboard, README.md, .gitignore.
  4. Optionally provisions: registers rappids in ~/.rapp/pids/ and
     prints the kill switch.

Estate types
============

  1st — The Sanctum     identity, memory, twins, soul-keeping
  2nd — The Polity      governance, decisions, constitution, scenarios
  3rd — The Works       production, labor, content/code/ops
  4th — The Press       observation, judgment, publication, critique
  5th — The Commons     federation, cross-estate exchange, public square

Each type ships with a default template tree. The architect persona will
extend the template based on the user's intent — adding industries,
naming neighborhoods, and specifying factory souls.

API
===

  EstateFactory(action="design",   intent="I want X")           # preview
  EstateFactory(action="generate", intent="...", name="kody")   # write
  EstateFactory(action="provision", name="kody")                # start it
  EstateFactory(action="tour",     name="kody")                 # describe
  EstateFactory(action="list")                                  # all estates

Workspace
=========

  ~/.rapp/estates/<slug>/
    rappid.json                       — permanent UUIDv4 identity
    estate.json                       — the tree (industries→neighborhoods→factories)
    estate.html                       — drill-down dashboard
    README.md                         — generated walkthrough
    industries/<industry>/
      <neighborhood>/
        <factory>/
          agent.py                    — factory_agent.py for this factory
          souls/<persona>.md          — one soul file per inlined persona
          manifest.json               — capabilities, port-on-provision
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import time
import urllib.error
import urllib.request
import uuid
from datetime import datetime, timezone


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:                       # last-resort standalone
        def __init__(self, name, metadata):
            self.name, self.metadata = name, metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/estate_factory",
    "version": "0.1.2",
    "display_name": "EstateFactory",
    "description": (
        "Generates a complete digital estate from an intent \u2014 org tree, factory agent stubs, souls, HTML dashboard \u2014 via brainstem or LLM APIs when available."
    ),
    "author": "kody-w",
    "industry": "meta",
    "tags": ["meta", "factory", "estate", "scaffolding", "rapplication",
             "singleton"],
    "category": "meta",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {
        "args": {
            "action": "design",
            "intent": "I want an estate that produces a daily blog post and a weekly podcast script.",
        }
    },
}


# ─── Storage paths ──────────────────────────────────────────────────────────

ESTATES_ROOT = pathlib.Path(os.environ.get(
    "RAPP_ESTATES_ROOT", pathlib.Path.home() / ".rapp" / "estates",
))
PIDS_DIR = pathlib.Path(os.environ.get(
    "RAPP_PIDS_DIR", pathlib.Path.home() / ".rapp" / "pids",
))


def _slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9_]+", "_", s.lower()).strip("_") or "x"


def _workspace(name: str) -> pathlib.Path:
    ws = ESTATES_ROOT / _slugify(name)
    ws.mkdir(parents=True, exist_ok=True)
    return ws


def _load_json(path: pathlib.Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return default


def _save_json(path: pathlib.Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2))
    tmp.replace(path)



def _canonical_rappid(name, owner="local"):
    """Canonical §6.1 rappid: rappid:@<owner>/<slug>:<64hex>, tail = keyless
    Hb("rapp/1:rappid", uuid4) (domain-separated). kind lives in the record."""
    import re, hashlib, uuid
    o = re.sub(r"[^a-z0-9]+", "-", (owner or "local").lower()).strip("-") or "local"
    s = re.sub(r"[^a-z0-9]+", "-", (name or "estate").lower()).strip("-") or "estate"
    return f"rappid:@{o}/{s}:" + hashlib.sha256(b"rapp/1:rappid\n" + uuid.uuid4().bytes).hexdigest()

def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


# ─── LLM dispatch — brainstem first, retry, then Azure/OpenAI fallback ──────

BRAIN_URL = os.environ.get("RAPP_BRAINSTEM_URL", "http://localhost:7071/chat")


def _llm_call(system: str, user: str, timeout: int = 180, retries: int = 3) -> str:
    """Call brainstem with retry+backoff; fall back to Azure/OpenAI."""
    for attempt in range(retries):
        try:
            body = json.dumps({
                "user_input": f"[SYSTEM]\n{system}\n[/SYSTEM]\n\n{user}",
                "system": system,
            }).encode("utf-8")
            req = urllib.request.Request(
                BRAIN_URL, data=body,
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = json.loads(r.read())
            out = (data.get("response") or data.get("reply") or "").strip()
            if out and "no LLM configured" not in out:
                return out
        except (urllib.error.URLError, json.JSONDecodeError, TimeoutError):
            pass
        time.sleep(2 ** attempt)
    # Azure / OpenAI fallback
    messages = [{"role": "system", "content": system},
                {"role": "user", "content": user}]
    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT", "")
    api_key = os.environ.get("AZURE_OPENAI_API_KEY", "")
    deployment = (os.environ.get("AZURE_OPENAI_DEPLOYMENT")
                  or os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", ""))
    if endpoint and api_key:
        url = endpoint
        if "/chat/completions" not in url:
            url = (url.rstrip("/") + f"/openai/deployments/{deployment}"
                   "/chat/completions?api-version=2025-01-01-preview")
        return _post(url, {"messages": messages, "model": deployment},
                     {"Content-Type": "application/json", "api-key": api_key})
    if os.environ.get("OPENAI_API_KEY"):
        return _post(
            "https://api.openai.com/v1/chat/completions",
            {"model": os.environ.get("OPENAI_MODEL", "gpt-4o"), "messages": messages},
            {"Content-Type": "application/json",
             "Authorization": "Bearer " + os.environ["OPENAI_API_KEY"]},
        )
    return "(no LLM configured)"


def _post(url, body, headers):
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"),
                                 headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            j = json.loads(resp.read().decode("utf-8"))
        choices = j.get("choices") or []
        return (choices[0]["message"].get("content") or "") if choices else ""
    except urllib.error.HTTPError as e:
        return f"(LLM HTTP {e.code}: {e.read().decode('utf-8')[:200]})"
    except urllib.error.URLError as e:
        return f"(LLM network error: {e})"


# ─── Estate-type templates ──────────────────────────────────────────────────

ESTATE_TYPES = {
    1: {
        "name": "1st Estate — The Sanctum",
        "domain": "identity, memory, twins, soul-keeping",
        "default_industries": [
            {"id": "twins", "name": "Twins",
             "neighborhoods": [
                 {"id": "personal-twin", "name": "Personal Twin",
                  "factories": [
                      {"id": "twin_speaker",
                       "souls": ["speaker", "memory_keeper", "voice_check"]}
                  ]},
             ]},
            {"id": "memory", "name": "Memory",
             "neighborhoods": [
                 {"id": "vault", "name": "Vault",
                  "factories": [
                      {"id": "memory_curator",
                       "souls": ["curator", "tagger", "summarizer"]}
                  ]},
             ]},
        ],
    },
    2: {
        "name": "2nd Estate — The Polity",
        "domain": "governance, decisions, constitution, scenarios",
        "default_industries": [
            {"id": "governance", "name": "Governance",
             "neighborhoods": [
                 {"id": "amendment-house", "name": "Amendment House",
                  "factories": [
                      {"id": "amendment_drafter",
                       "souls": ["drafter", "challenger", "ratifier"]}
                  ]},
             ]},
            {"id": "strategy", "name": "Strategy",
             "neighborhoods": [
                 {"id": "scenario-room", "name": "Scenario Room",
                  "factories": [
                      {"id": "scenario_runner",
                       "souls": ["planner", "red_team", "decision_maker"]}
                  ]},
             ]},
        ],
    },
    3: {
        "name": "3rd Estate — The Works",
        "domain": "production, labor, content/code/ops",
        "default_industries": [
            {"id": "content", "name": "Content",
             "neighborhoods": [
                 {"id": "post-shop", "name": "Post Shop",
                  "factories": [
                      {"id": "post_factory",
                       "souls": ["researcher", "drafter", "editor", "publisher"]}
                  ]},
             ]},
            {"id": "code", "name": "Code",
             "neighborhoods": [
                 {"id": "build-bench", "name": "Build Bench",
                  "factories": [
                      {"id": "build_factory",
                       "souls": ["architect", "implementer", "reviewer"]}
                  ]},
             ]},
        ],
    },
    4: {
        "name": "4th Estate — The Press",
        "domain": "observation, judgment, publication, critique",
        "default_industries": [
            {"id": "critique", "name": "Critique",
             "neighborhoods": [
                 {"id": "bakeoff", "name": "Bakeoff",
                  "factories": [
                      {"id": "bakeoff_factory",
                       "souls": ["judge", "mutator", "publisher"]}
                  ]},
             ]},
            {"id": "analytics", "name": "Analytics",
             "neighborhoods": [
                 {"id": "newsroom", "name": "Newsroom",
                  "factories": [
                      {"id": "analytics_factory",
                       "souls": ["observer", "summarizer", "reporter"]}
                  ]},
             ]},
        ],
    },
    5: {
        "name": "5th Estate — The Commons",
        "domain": "federation, cross-estate exchange, public square",
        "default_industries": [
            {"id": "federation", "name": "Federation",
             "neighborhoods": [
                 {"id": "peer-discovery", "name": "Peer Discovery",
                  "factories": [
                      {"id": "neighbor_factory",
                       "souls": ["scout", "handshaker", "ledger_keeper"]}
                  ]},
             ]},
        ],
    },
}


# ─── SOUL constants — internal personas ─────────────────────────────────────

_SOUL_ARCHITECT = """You are the Architect persona of the EstateFactory.

Given a user's intent and a chosen estate type (1-5, classical estates
applied to digital labor), you design the estate's org chart:

  industries → neighborhoods → factories → persona souls inside each factory

You ALWAYS start from the estate type's default template (provided to you
inline) and extend it based on intent. You may add industries, rename
neighborhoods, add factories, and add personas. You do NOT shrink the
template — every default neighborhood from the type stays.

Output STRICT JSON only — no markdown, no preamble:

{
  "name": "...",
  "tagline": "...",
  "type": <int 1-5>,
  "industries": [
    {"id": "...", "name": "...",
     "neighborhoods": [
       {"id": "...", "name": "...",
        "factories": [
          {"id": "...", "name": "...", "tagline": "...",
           "souls": ["persona_a", "persona_b", ...]}
        ]}
     ]}
  ]
}

Slugs are lowercase_with_underscores. Names are Title Case. Tagline is one
short sentence. Souls list is 2-6 personas per factory."""


_SOUL_SOULWRITER = """You are the SoulWriter persona of the EstateFactory.

You write ONE soul prompt for ONE persona inside ONE factory. The soul is
the system prompt that defines what this persona does, how it thinks, what
its hard rules are.

Rules for the soul:
  - 80-300 words.
  - Open with "You are the <persona> persona of the <factory> factory."
  - State the persona's job in concrete terms.
  - List 3-5 hard rules (numbered) — what it MUST do and MUST NOT do.
  - End with the output format ("Output ONLY X, no preamble").
  - Voice should match the persona's role (a Judge sounds brutal; a
    Researcher sounds curious; a Publisher sounds decisive).

Output ONLY the soul text. No commentary, no markdown fences."""


_SOUL_REVIEWER = """You are the Reviewer persona of the EstateFactory.

You read a designed estate (the JSON tree) and return ONE of:
  - "READY: <one-line reason>"  if the estate is coherent and shippable
  - "FIX: <what to fix>"        if there's a structural problem

Check for:
  - Every industry has at least one neighborhood
  - Every neighborhood has at least one factory
  - Every factory has at least 2 souls (otherwise it's not a converged factory)
  - No duplicate slugs at any level
  - Names and slugs match (no industry called "Press" with slug "operations")

Output ONLY the verdict line. No explanation, no markdown."""


# ─── Helpers ────────────────────────────────────────────────────────────────

def _parse_json_strict(raw: str) -> dict | None:
    """Extract the first {...} object from a model response."""
    s = raw.find("{")
    e = raw.rfind("}")
    if s < 0 or e <= s:
        return None
    try:
        return json.loads(raw[s:e + 1])
    except json.JSONDecodeError:
        return None


def _classify_intent(intent: str, explicit_type: int | None) -> int:
    """Decide the estate type. Explicit wins; otherwise heuristic."""
    if explicit_type and 1 <= explicit_type <= 5:
        return explicit_type
    t = (intent or "").lower()
    scores = {
        1: sum(t.count(w) for w in ["twin", "memory", "soul", "identity",
                                     "vault", "persona", "remember"]),
        2: sum(t.count(w) for w in ["govern", "decide", "decision", "vote",
                                     "amendment", "strategy", "constitution"]),
        3: sum(t.count(w) for w in ["produce", "write", "ship", "build",
                                     "code", "content", "post", "blog",
                                     "ops", "deploy"]),
        4: sum(t.count(w) for w in ["judge", "review", "score", "critique",
                                     "publish", "analytics", "report",
                                     "press", "newsroom", "bakeoff"]),
        5: sum(t.count(w) for w in ["federation", "peer", "commons",
                                     "exchange", "public", "share"]),
    }
    best = max(scores, key=scores.get)
    # Default to 3rd if everything is zero — "the works" is the most common ask
    return best if scores[best] > 0 else 3


def _factory_template(factory_id: str, factory_name: str,
                      factory_tagline: str, souls: list[str],
                      estate_name: str, neighborhood_name: str) -> str:
    """Render the agent.py source for one generated factory.

    The body is intentionally minimal — it loads its souls from the souls/
    sibling dir, exposes a perform(input) that pipelines them in order,
    and ships under the same _<pid>_rap.pid convention when provisioned.
    """
    class_name = re.sub(r"[^A-Za-z0-9]", "", factory_name.title()) or "Generated"
    souls_calls = "\n".join(
        f'        out = _run_persona({json.dumps(s)}, out)' for s in souls
    )
    souls_meta = ", ".join(json.dumps(s) for s in souls)
    return f'''"""
{factory_id}/agent.py — generated factory for the "{factory_name}" factory
in the {neighborhood_name} neighborhood of the {estate_name} estate.

Personas (run in order): {", ".join(souls)}

Each persona's soul lives in souls/<persona>.md and is the system prompt
for that persona. Edit those files freely — the factory hot-loads them.
"""
from __future__ import annotations

import json, os, pathlib, time
import urllib.request, urllib.error

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name, self.metadata = name, metadata


__manifest__ = {{
    "schema": "rapp-agent/1.0",
    "name": "@operator/{factory_id}",
    "version": "0.1.0",
    "display_name": "{factory_name}",
    "description": "{factory_tagline}",
    "industry": "estate-generated",
    "tags": ["composite", "estate-factory", "generated"],
    "personas": [{souls_meta}],
    "capabilities": ["perform"],
}}


HERE = pathlib.Path(__file__).resolve().parent
SOULS_DIR = HERE / "souls"
BRAIN_URL = os.environ.get("RAPP_BRAINSTEM_URL", "http://localhost:7071/chat")


def _read_soul(name):
    p = SOULS_DIR / f"{{name}}.md"
    return p.read_text() if p.exists() else f"You are the {{name}} persona."


def _llm(soul, user, timeout=180, retries=3):
    for attempt in range(retries):
        try:
            body = json.dumps({{
                "user_input": f"[SYSTEM]\\n{{soul}}\\n[/SYSTEM]\\n\\n{{user}}",
                "system": soul,
            }}).encode("utf-8")
            req = urllib.request.Request(
                BRAIN_URL, data=body,
                headers={{"Content-Type": "application/json"}},
            )
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = json.loads(r.read())
            out = (data.get("response") or data.get("reply") or "").strip()
            if out and "no LLM configured" not in out:
                return out
        except Exception:
            pass
        time.sleep(2 ** attempt)
    return "(no LLM available)"


def _run_persona(name, prev_output):
    return _llm(_read_soul(name), prev_output)


class {class_name}Agent(BasicAgent):
    def __init__(self):
        self.name = "{class_name}"
        self.metadata = {{
            "name": self.name,
            "description": "{factory_tagline}",
            "parameters": {{
                "type": "object",
                "properties": {{"input": {{"type": "string"}}}},
                "required": ["input"],
            }},
        }}
        super().__init__(self.name, self.metadata)

    def perform(self, input="", **kwargs):
        out = input
{souls_calls}
        return out


class {class_name}(Agent := {class_name}Agent):
    pass
'''


def _write_factory_files(factory_dir: pathlib.Path, factory: dict,
                         estate_name: str, neighborhood_name: str) -> None:
    factory_dir.mkdir(parents=True, exist_ok=True)
    (factory_dir / "souls").mkdir(exist_ok=True)
    # agent.py
    src = _factory_template(
        factory_id=factory["id"],
        factory_name=factory.get("name", factory["id"].title()),
        factory_tagline=factory.get("tagline", "Generated factory."),
        souls=factory["souls"],
        estate_name=estate_name,
        neighborhood_name=neighborhood_name,
    )
    (factory_dir / "agent.py").write_text(src)
    # manifest
    _save_json(factory_dir / "manifest.json", {
        "id": factory["id"],
        "name": factory.get("name", factory["id"]),
        "tagline": factory.get("tagline", ""),
        "personas": factory["souls"],
        "industry": "estate-generated",
    })
    # souls (generated lazily by SoulWriter — on first generate())
    for soul_name in factory["souls"]:
        path = factory_dir / "souls" / f"{soul_name}.md"
        if path.exists():
            continue
        # Defer LLM-soul generation to the caller (it batches)
        path.write_text(f"(soul for {soul_name} — generated below)")


def _generate_soul(persona_name: str, factory_name: str,
                   estate_name: str) -> str:
    """Call SoulWriter to produce a soul for one persona."""
    prompt = (
        f"Persona name: {persona_name}\n"
        f"Factory: {factory_name}\n"
        f"Estate: {estate_name}\n\n"
        f"Write the soul for this persona. Output ONLY the soul text."
    )
    return _llm_call(_SOUL_SOULWRITER, prompt)


# ─── Dashboard template (per-estate) ────────────────────────────────────────

_ESTATE_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<title>{name} — Estate</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0a0a0f;color:#c8c8c8;font-family:'SF Mono','Fira Code','Consolas',monospace;font-size:13px;padding:16px;max-width:1100px;margin:0 auto}}
h1{{color:#00ff88;font-size:22px;margin-bottom:4px;letter-spacing:1px}}
.sub{{color:#555;font-size:11px;margin-bottom:18px}}
h2{{color:#d2a8ff;font-size:13px;text-transform:uppercase;letter-spacing:2px;margin:18px 0 8px}}
h3{{color:#e8c87a;font-size:11px;text-transform:uppercase;letter-spacing:1.5px;margin:12px 0 6px}}
.industry{{background:#111118;border:1px solid #222;border-radius:8px;padding:14px;margin-bottom:12px}}
.neighborhood{{background:#0d0d14;border:1px solid #1a1a2a;border-radius:6px;padding:10px;margin-top:8px}}
.factory{{font-size:11px;padding:6px 8px;border-left:2px solid #4488ff;margin:4px 0;background:#0a0a14}}
.factory .name{{color:#fff;font-weight:bold}}
.factory .tagline{{color:#888}}
.factory .souls{{color:#666;font-size:10px;margin-top:2px}}
</style></head><body>
<h1>{name}</h1>
<div class="sub">{tagline} · type {type} · rappid {rappid}</div>
{body_html}
</body></html>
"""


def _render_estate_html(estate: dict) -> str:
    parts = []
    for i in estate.get("industries", []):
        parts.append(f'<div class="industry"><h2>{i["name"]}</h2>')
        for n in i.get("neighborhoods", []):
            parts.append(f'<div class="neighborhood"><h3>{n["name"]}</h3>')
            for f in n.get("factories", []):
                souls = ", ".join(f.get("souls", []))
                parts.append(
                    f'<div class="factory"><div class="name">{f["name"]}</div>'
                    f'<div class="tagline">{f.get("tagline", "")}</div>'
                    f'<div class="souls">personas: {souls}</div></div>')
            parts.append('</div>')
        parts.append('</div>')
    return _ESTATE_HTML_TEMPLATE.format(
        name=estate["name"], tagline=estate.get("tagline", ""),
        type=estate.get("type", "?"), rappid=estate.get("rappid", "?"),
        body_html="\n".join(parts),
    )


# ─── The agent ──────────────────────────────────────────────────────────────

class EstateFactoryAgent(BasicAgent):

    def __init__(self):
        self.name = "EstateFactory"
        self.metadata = {
            "name": self.name,
            "description": (
                "Generate a full functioning digital estate from intent.\n\n"
                "Estate types (classical 1-5):\n"
                "  1 - Sanctum (identity, memory, twins)\n"
                "  2 - Polity  (governance, decisions, scenarios)\n"
                "  3 - Works   (production, content, code, ops)\n"
                "  4 - Press   (judgment, publication, analytics)\n"
                "  5 - Commons (federation, peer exchange)\n\n"
                "Actions:\n"
                "  design    - preview the estate tree (no writes)\n"
                "  generate  - write the estate to ~/.rapp/estates/<name>/\n"
                "  provision - prepare the dashboard + register rappids\n"
                "  tour      - describe an existing estate\n"
                "  list      - all estates on this box"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["design", "generate", "provision",
                                        "tour", "list"]},
                    "intent": {"type": "string",
                               "description": "What the user wants the estate to do. Required for design + generate."},
                    "name": {"type": "string",
                             "description": "Slug for the estate. Required for generate/provision/tour."},
                    "type": {"type": "integer",
                             "description": "Estate type 1-5. Optional; inferred from intent if omitted.",
                             "minimum": 1, "maximum": 5},
                    "write_souls": {"type": "boolean",
                                    "description": "On generate, also call the SoulWriter persona to produce real soul prompts (slower; cheap mode skips this and uses placeholders)."},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── action: design ────────────────────────────────────────────────────

    def _design(self, intent="", type=None, name=None, **_):
        if not intent:
            return json.dumps({"status": "error",
                "message": "intent required for design."})
        chosen = _classify_intent(intent, type)
        template = ESTATE_TYPES[chosen]
        ask = (
            f"User intent:\n{intent}\n\n"
            f"Estate type chosen: {chosen} ({template['name']})\n"
            f"Domain: {template['domain']}\n\n"
            f"Default template (extend it, don't shrink it):\n"
            f"{json.dumps(template['default_industries'], indent=2)}\n\n"
            f"Suggested name slug: {_slugify(name) if name else 'kody_estate'}\n\n"
            f"Design the estate JSON tree. Output STRICT JSON only."
        )
        raw = _llm_call(_SOUL_ARCHITECT, ask)
        parsed = _parse_json_strict(raw)
        if not parsed:
            return json.dumps({"status": "error",
                "message": "architect returned non-JSON",
                "raw_preview": raw[:300]})
        parsed.setdefault("type", chosen)
        parsed.setdefault("name", name or "kody_estate")
        return json.dumps({"status": "ok", "action": "design",
                           "estate": parsed,
                           "type_chosen": chosen,
                           "type_name": template["name"]},
                          indent=2)

    # ── action: generate ──────────────────────────────────────────────────

    def _generate(self, intent="", name=None, type=None,
                  write_souls=True, **_):
        if not intent or not name:
            return json.dumps({"status": "error",
                "message": "intent + name required for generate."})
        # First design
        designed = json.loads(self._design(intent=intent, type=type, name=name))
        if designed.get("status") != "ok":
            return json.dumps(designed)
        estate = designed["estate"]
        estate["rappid"] = _canonical_rappid(name)
        estate["created_at"] = _now()
        estate["intent"] = intent
        estate.setdefault("type", designed["type_chosen"])

        # Reviewer check
        verdict = _llm_call(_SOUL_REVIEWER,
                            f"Review this estate:\n{json.dumps(estate, indent=2)}")
        if verdict.upper().startswith("FIX:"):
            return json.dumps({"status": "error",
                "message": f"reviewer rejected: {verdict}",
                "estate": estate})

        # Write files
        ws = _workspace(name)
        _save_json(ws / "rappid.json", {
            "rappid": estate["rappid"],
            "type": estate["type"],
            "name": estate["name"],
            "created_at": estate["created_at"],
            "intent": intent,
        })
        _save_json(ws / "estate.json", estate)
        (ws / ".gitignore").write_text("*.log\n*.pid\n")

        souls_written = 0
        factories_written = 0
        for ind in estate.get("industries", []):
            for nb in ind.get("neighborhoods", []):
                for fac in nb.get("factories", []):
                    fac_dir = (ws / "industries" / ind["id"] /
                               nb["id"] / fac["id"])
                    _write_factory_files(fac_dir, fac, estate["name"], nb["name"])
                    factories_written += 1
                    if write_souls:
                        for soul_name in fac["souls"]:
                            soul_text = _generate_soul(
                                soul_name, fac.get("name", fac["id"]),
                                estate["name"])
                            (fac_dir / "souls" / f"{soul_name}.md").write_text(soul_text)
                            souls_written += 1

        # Dashboard + README
        (ws / "estate.html").write_text(_render_estate_html(estate))
        (ws / "README.md").write_text(_make_readme(estate, ws))

        return json.dumps({
            "status": "ok", "action": "generate",
            "name": estate["name"],
            "type": estate["type"],
            "rappid": estate["rappid"],
            "workspace": str(ws),
            "factories_written": factories_written,
            "souls_written": souls_written,
            "dashboard": f"file://{ws}/estate.html",
            "reviewer_verdict": verdict,
        }, indent=2)

    # ── action: provision ─────────────────────────────────────────────────

    def _provision(self, name=None, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required."})
        ws = _workspace(name)
        estate = _load_json(ws / "estate.json", None)
        if not estate:
            return json.dumps({"status": "error",
                "message": f"estate '{name}' not generated yet."})
        # Provisioning = register every factory's rappid pid placeholder.
        # Actual brainstem-per-rapp spin-up is handled by a separate
        # provision-twin.sh helper (out of scope for this singleton).
        PIDS_DIR.mkdir(parents=True, exist_ok=True)
        prepped = []
        for ind in estate.get("industries", []):
            for nb in ind.get("neighborhoods", []):
                for fac in nb.get("factories", []):
                    slug = f"{name}_{fac['id']}"
                    # Use a stub pid (the actual rapp doesn't exist yet —
                    # provision-twin would replace this)
                    stub_pid = 0
                    marker = PIDS_DIR / f"{slug}_{stub_pid}_rap.pid"
                    marker.write_text(str(stub_pid))
                    prepped.append(str(marker))
        return json.dumps({
            "status": "ok", "action": "provision",
            "name": name, "prepared_pid_stubs": prepped,
            "next_step": (
                f"For each factory, run provision-twin.sh on the agent.py "
                f"at {ws}/industries/<industry>/<neighborhood>/<factory>/ "
                f"to spin up a real brainstem and replace the stub pid file."
            ),
        }, indent=2)

    # ── action: tour ──────────────────────────────────────────────────────

    def _tour(self, name=None, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required."})
        ws = _workspace(name)
        estate = _load_json(ws / "estate.json", None)
        if not estate:
            return json.dumps({"status": "error",
                "message": f"estate '{name}' not found at {ws}"})
        lines = [
            f"{estate.get('name', name)} — type {estate.get('type', '?')}",
            f"rappid: {estate.get('rappid', '?')}",
            f"created: {estate.get('created_at', '?')}",
            f"workspace: {ws}",
            "",
        ]
        for ind in estate.get("industries", []):
            lines.append(f"  {ind['name']}")
            for nb in ind.get("neighborhoods", []):
                lines.append(f"    {nb['name']}")
                for fac in nb.get("factories", []):
                    souls = ", ".join(fac.get("souls", []))
                    lines.append(f"      ⚙ {fac['name']}  — {souls}")
        lines.append("")
        lines.append(f"dashboard: file://{ws}/estate.html")
        return json.dumps({"status": "ok", "action": "tour",
                           "rendering": "\n".join(lines),
                           "estate": estate},
                          indent=2)

    # ── action: list ──────────────────────────────────────────────────────

    def _list(self, **_):
        out = []
        if ESTATES_ROOT.exists():
            for d in sorted(ESTATES_ROOT.iterdir()):
                if not d.is_dir():
                    continue
                e = _load_json(d / "estate.json", None)
                r = _load_json(d / "rappid.json", None)
                if e and r:
                    out.append({
                        "slug": d.name,
                        "name": e.get("name"),
                        "type": e.get("type"),
                        "rappid": r.get("rappid"),
                        "factories": sum(len(n.get("factories", []))
                                         for i in e.get("industries", [])
                                         for n in i.get("neighborhoods", [])),
                        "workspace": str(d),
                    })
        return json.dumps({"status": "ok", "action": "list",
                           "estates": out, "count": len(out)},
                          indent=2)

    # ── dispatch ──────────────────────────────────────────────────────────

    def perform(self, action="list", **kwargs):
        try:
            if action == "design":
                return self._design(**kwargs)
            if action == "generate":
                return self._generate(**kwargs)
            if action == "provision":
                return self._provision(**kwargs)
            if action == "tour":
                return self._tour(**kwargs)
            if action == "list":
                return self._list(**kwargs)
            return json.dumps({"status": "error",
                "message": f"unknown action '{action}'."})
        except Exception as e:
            return json.dumps({"status": "error", "exception": str(e)})


class EstateFactory(EstateFactoryAgent):
    pass


def _make_readme(estate: dict, ws: pathlib.Path) -> str:
    type_name = ESTATE_TYPES.get(estate.get("type", 3), {}).get("name", "Custom")
    industries_md = ""
    for ind in estate.get("industries", []):
        industries_md += f"\n### {ind['name']}\n"
        for nb in ind.get("neighborhoods", []):
            industries_md += f"\n- **{nb['name']}**\n"
            for fac in nb.get("factories", []):
                souls = ", ".join(fac.get("souls", []))
                industries_md += (f"  - ⚙ `{fac['id']}` — "
                                  f"{fac.get('name', fac['id'])} "
                                  f"({souls})\n")
    return f"""# {estate['name']}

**Type:** {type_name}
**Rappid:** `{estate.get('rappid', '?')}`
**Created:** {estate.get('created_at', '?')}

## Intent
> {estate.get('intent', '(no intent recorded)')}

## Org chart
{industries_md}

## Files

```
{ws.name}/
├── rappid.json              ← permanent identity
├── estate.json              ← the tree
├── estate.html              ← dashboard
├── README.md                ← this file
└── industries/
    └── <industry>/<neighborhood>/<factory>/
        ├── agent.py         ← the factory_agent.py
        ├── manifest.json
        └── souls/<persona>.md
```

## Next steps

1. Open `estate.html` in a browser.
2. For each factory you want live, run:
   `provision-twin.sh industries/<i>/<n>/<f>/agent.py`
3. Each factory registers as `<name>_<factory_id>_<pid>_rap.pid` in
   `~/.rapp/pids/` and becomes reachable through the neighborhood organ.
"""
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
