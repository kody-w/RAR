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
    "version": "0.1.0",
    "display_name": "EstateFactory",
    "description": (
        "Generate a full functioning digital estate from intent. Picks "
        "estate type (1st-5th, classical estates framing), designs the "
        "industries→neighborhoods→factories tree, writes every file the "
        "estate needs, and optionally provisions live rapps."
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
        estate["rappid"] = str(uuid.uuid4())
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
