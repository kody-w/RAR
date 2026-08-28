---
name: "rar-kody-w-estate-factory"
description: "Generate a full functioning digital estate from intent.\n\nEstate types (classical 1-5):\n  1 - Sanctum (identity, memory, twins)\n  2 - Polity  (governance, decisions, scenarios)\n  3 - Works   (production, content, code, ops)\n  4 - Press   (judgment, publication, analytics)\n  5 - Commons (federation, peer exchange)\n\nActions:\n  design    - preview the estate tree (no writes)\n  generate  - write the estate to ~/.rapp/estates/<name>/\n  provision - prepare the dashboard + register rappids\n  tour      - describe an existing estate\n  list      - all estates on this box"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/estate_factory", "rar_sha256": "7558023b529e952b58084d09cf0c93c1a8cdea34684302e62e6dba5b0ccbc238", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "0.1.2", "author": "kody-w", "tags": ["meta", "factory", "estate", "scaffolding", "rapplication", "singleton"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `estate_factory_agent.py` and embedded as the fenced Python below (sha256 7558023b529e952b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `estate_factory_agent.py` first:

```bash
python3 estate_factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 estate_factory_agent.py   # or on stdin
python3 estate_factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
