---
name: "rar-kody-w-estate-factory"
description: "Generate a full functioning digital estate from intent.\n\nEstate types (classical 1-5):\n  1 - Sanctum (identity, memory, twins)\n  2 - Polity  (governance, decisions, scenarios)\n  3 - Works   (production, content, code, ops)\n  4 - Press   (judgment, publication, analytics)\n  5 - Commons (federation, peer exchange)\n\nActions:\n  design    - preview the estate tree (no writes)\n  generate  - write the estate to ~/.rapp/estates/<name>/\n  provision - prepare the dashboard + register rappids\n  tour      - describe an existing estate\n  list      - all estates on this box"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/estate_factory", "rar_sha256": "46b070177e96da94f21bacbd45bfb0fa19f01d9aa79af7727bf1ff8aadd8e7b3", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "0.1.2", "author": "kody-w", "tags": ["meta", "factory", "estate", "scaffolding", "rapplication", "singleton"]}
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
