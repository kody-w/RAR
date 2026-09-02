---
name: "rar-kody-w-estate-factory"
description: "Generate a full functioning digital estate from intent.\n\nEstate types (classical 1-5):\n  1 - Sanctum (identity, memory, twins)\n  2 - Polity  (governance, decisions, scenarios)\n  3 - Works   (production, content, code, ops)\n  4 - Press   (judgment, publication, analytics)\n  5 - Commons (federation, peer exchange)\n\nActions:\n  design    - preview the estate tree (no writes)\n  generate  - write the estate to ~/.rapp/estates/<name>/\n  provision - prepare the dashboard + register rappids\n  tour      - describe an existing estate\n  list      - all estates on this box"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/estate_factory", "rar_sha256": "7558023b529e952b58084d09cf0c93c1a8cdea34684302e62e6dba5b0ccbc238", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "estate_factory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/estate-factory:df50e1b2b94aa28e31a9f228f89cba64f28fee66929ff01b88192a10ca9981ad", "kind": "skill"}, "version": "0.1.2", "author": "kody-w", "tags": ["meta", "factory", "estate", "scaffolding", "rapplication", "singleton"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/estate_factory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `estate_factory_agent.py` is
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
