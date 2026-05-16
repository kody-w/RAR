"""rapp_leviathan_factory_agent.py — v0.2.0

SELF-CONTAINED Rapp Leviathan factory. ONE drop-in agent.py with NO
sibling dependencies. Pull just this file into any RAPP brainstem's
agents/ directory and the operator can generate a complete digital
being from intent.

A Rapp Leviathan is one operator's full digital AI entity — composed
of up to five estates (the five classical estates applied to digital
labor). This factory composes those estates under one top-level
rappid and a single five-organ anatomy dashboard.

  Estate (organ)         Body part   Question it answers
  ─────────────────      ─────────   ────────────────────
  1st  — Sanctum         soul        Who am I?
  2nd  — Polity          will        What shall I do?
  3rd  — Works           hands       What shall I make?
  4th  — Press           eyes        What is true?
  5th  — Commons         mouth       Who shall I speak to?

A full Leviathan has all five organs. Partial Leviathans (1-4) are
explicit and dashboard-rendered as such.

What changed vs v0.1.0
======================

  • Inlined the entire EstateFactory logic. No sibling-file dependency.
  • New `bootstrap_check` action — diagnoses LLM/brainstem reachability
    and prints copy-paste remedies before the user wastes a generate call.
  • Inlined the provision routine. No more references to an external
    `provision-twin.sh` that ships in a different repo.

API
===

  RappLeviathanFactory(action="bootstrap_check")
  RappLeviathanFactory(action="design",   intent="...")
  RappLeviathanFactory(action="generate", intent="...", name="kody",
                       estates=[1,2,3,4,5])           # subset OK
  RappLeviathanFactory(action="provision", name="kody")
  RappLeviathanFactory(action="tour",     name="kody")
  RappLeviathanFactory(action="anatomy",  name="kody")
  RappLeviathanFactory(action="list")

Workspaces
==========

  ~/.rapp/leviathans/<slug>/      composite leviathan + dashboard
  ~/.rapp/estates/<slug>/         one per organ (full factory tree)
  ~/.rapp/pids/<slug>_<pid>_rap.pid   provisioning markers
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
    class BasicAgent:                       # standalone fallback
        def __init__(self, name, metadata):
            self.name, self.metadata = name, metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rapp_leviathan_factory",
    "version": "0.2.0",
    "display_name": "RappLeviathanFactory",
    "description": (
        "Generate a complete Rapp Leviathan — one operator's full digital "
        "AI entity — from intent. Self-contained in one file: pulls no "
        "sibling agents, composes 1-5 estates (Sanctum/Polity/Works/Press/"
        "Commons) under a single top-level rappid, writes every file each "
        "estate needs, and renders a five-organ anatomy dashboard. "
        "bootstrap_check diagnoses LLM reachability before you generate."
    ),
    "author": "kody-w",
    "industry": "meta",
    "tags": ["meta", "factory", "leviathan", "estate", "composite",
             "anatomy", "rapplication", "singleton", "self-contained"],
    "category": "meta",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {
        "args": {
            "action": "generate",
            "intent": "I want a complete digital twin of me — remembers, decides, produces, judges, and speaks.",
            "name": "kody",
        }
    },
}


# ─── Storage roots ──────────────────────────────────────────────────────────

LEVIATHANS_ROOT = pathlib.Path(os.environ.get(
    "RAPP_LEVIATHANS_ROOT", pathlib.Path.home() / ".rapp" / "leviathans"))
ESTATES_ROOT = pathlib.Path(os.environ.get(
    "RAPP_ESTATES_ROOT", pathlib.Path.home() / ".rapp" / "estates"))
PIDS_DIR = pathlib.Path(os.environ.get(
    "RAPP_PIDS_DIR", pathlib.Path.home() / ".rapp" / "pids"))


# ─── Estate type table (full) ───────────────────────────────────────────────

ESTATE_TYPES: dict[int, dict] = {
    1: {
        "slug": "sanctum", "name": "1st Estate — Sanctum",
        "organ": "soul", "question": "Who am I?",
        "domain": "identity, memory, twins, soul-keeping",
        "default_industries": [
            {"id": "twins", "name": "Twins", "neighborhoods": [
                {"id": "personal_twin", "name": "Personal Twin", "factories": [
                    {"id": "twin_speaker", "name": "Twin Speaker",
                     "tagline": "Speaks for the operator in their voice.",
                     "souls": ["speaker", "memory_keeper", "voice_check"]},
                ]},
            ]},
            {"id": "memory", "name": "Memory", "neighborhoods": [
                {"id": "vault", "name": "Vault", "factories": [
                    {"id": "memory_curator", "name": "Memory Curator",
                     "tagline": "Tags, summarizes, and retrieves memories.",
                     "souls": ["curator", "tagger", "summarizer"]},
                ]},
            ]},
        ],
    },
    2: {
        "slug": "polity", "name": "2nd Estate — Polity",
        "organ": "will", "question": "What shall I do?",
        "domain": "governance, decisions, constitution, scenarios",
        "default_industries": [
            {"id": "governance", "name": "Governance", "neighborhoods": [
                {"id": "amendment_house", "name": "Amendment House", "factories": [
                    {"id": "amendment_drafter", "name": "Amendment Drafter",
                     "tagline": "Drafts, challenges, and ratifies amendments.",
                     "souls": ["drafter", "challenger", "ratifier"]},
                ]},
            ]},
            {"id": "strategy", "name": "Strategy", "neighborhoods": [
                {"id": "scenario_room", "name": "Scenario Room", "factories": [
                    {"id": "scenario_runner", "name": "Scenario Runner",
                     "tagline": "Plans, red-teams, and decides.",
                     "souls": ["planner", "red_team", "decision_maker"]},
                ]},
            ]},
        ],
    },
    3: {
        "slug": "works", "name": "3rd Estate — Works",
        "organ": "hands", "question": "What shall I make?",
        "domain": "production, labor, content/code/ops",
        "default_industries": [
            {"id": "content", "name": "Content", "neighborhoods": [
                {"id": "post_shop", "name": "Post Shop", "factories": [
                    {"id": "post_factory", "name": "Post Factory",
                     "tagline": "Research → draft → edit → publish.",
                     "souls": ["researcher", "drafter", "editor", "publisher"]},
                ]},
            ]},
            {"id": "code", "name": "Code", "neighborhoods": [
                {"id": "build_bench", "name": "Build Bench", "factories": [
                    {"id": "build_factory", "name": "Build Factory",
                     "tagline": "Architect → implement → review.",
                     "souls": ["architect", "implementer", "reviewer"]},
                ]},
            ]},
        ],
    },
    4: {
        "slug": "press", "name": "4th Estate — Press",
        "organ": "eyes", "question": "What is true?",
        "domain": "observation, judgment, publication, critique",
        "default_industries": [
            {"id": "critique", "name": "Critique", "neighborhoods": [
                {"id": "bakeoff", "name": "Bakeoff", "factories": [
                    {"id": "bakeoff_factory", "name": "Bakeoff Factory",
                     "tagline": "Judge, mutate, publish winners.",
                     "souls": ["judge", "mutator", "publisher"]},
                ]},
            ]},
            {"id": "analytics", "name": "Analytics", "neighborhoods": [
                {"id": "newsroom", "name": "Newsroom", "factories": [
                    {"id": "analytics_factory", "name": "Analytics Factory",
                     "tagline": "Observe, summarize, report.",
                     "souls": ["observer", "summarizer", "reporter"]},
                ]},
            ]},
        ],
    },
    5: {
        "slug": "commons", "name": "5th Estate — Commons",
        "organ": "mouth", "question": "Who shall I speak to?",
        "domain": "federation, cross-estate exchange, public square",
        "default_industries": [
            {"id": "federation", "name": "Federation", "neighborhoods": [
                {"id": "peer_discovery", "name": "Peer Discovery", "factories": [
                    {"id": "neighbor_factory", "name": "Neighbor Factory",
                     "tagline": "Scout peers, handshake, ledger.",
                     "souls": ["scout", "handshaker", "ledger_keeper"]},
                ]},
            ]},
        ],
    },
}


# ─── Generic helpers ────────────────────────────────────────────────────────

def _slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9_]+", "_", (s or "").lower()).strip("_") or "x"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


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


def _parse_json_strict(raw: str) -> dict | None:
    s = raw.find("{")
    e = raw.rfind("}")
    if s < 0 or e <= s:
        return None
    try:
        return json.loads(raw[s:e + 1])
    except json.JSONDecodeError:
        return None


def _leviathan_workspace(name: str) -> pathlib.Path:
    ws = LEVIATHANS_ROOT / _slugify(name)
    ws.mkdir(parents=True, exist_ok=True)
    return ws


def _estate_workspace(name: str) -> pathlib.Path:
    ws = ESTATES_ROOT / _slugify(name)
    ws.mkdir(parents=True, exist_ok=True)
    return ws


# ─── LLM dispatch + bootstrap check ─────────────────────────────────────────

BRAIN_URL = os.environ.get("RAPP_BRAINSTEM_URL", "http://localhost:7071/chat")
HEALTH_URL = BRAIN_URL.replace("/chat", "/health")


def _llm_call(system: str, user: str, timeout: int = 180, retries: int = 3) -> str:
    """Try brainstem with retry+backoff; fall back to Azure/OpenAI."""
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
    # Azure fallback
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


def _check_brainstem() -> dict:
    try:
        with urllib.request.urlopen(HEALTH_URL, timeout=5) as r:
            return {"ok": True, "data": json.loads(r.read())}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def bootstrap_check() -> dict:
    """Diagnose whether this agent can actually generate a Leviathan right now."""
    diagnostics = {"checks": [], "ok": True, "remedies": []}

    # 1. Brainstem reachable?
    brain = _check_brainstem()
    if brain["ok"]:
        model = brain["data"].get("model", "?")
        diagnostics["checks"].append({
            "name": "RAPP brainstem", "status": "ok",
            "detail": f"Reachable at {BRAIN_URL}, model={model}",
        })
    else:
        # Fallback creds?
        has_azure = bool(os.environ.get("AZURE_OPENAI_ENDPOINT") and
                         os.environ.get("AZURE_OPENAI_API_KEY"))
        has_openai = bool(os.environ.get("OPENAI_API_KEY"))
        if has_azure or has_openai:
            diagnostics["checks"].append({
                "name": "RAPP brainstem", "status": "warn",
                "detail": f"Not reachable at {BRAIN_URL}. "
                          f"Falling back to {'Azure' if has_azure else 'OpenAI'} env vars.",
            })
        else:
            diagnostics["ok"] = False
            diagnostics["checks"].append({
                "name": "RAPP brainstem", "status": "fail",
                "detail": f"Not reachable at {BRAIN_URL}, no Azure or OpenAI env vars.",
            })
            diagnostics["remedies"].append(
                "Install + run the RAPP brainstem: "
                "`curl -fsSL https://kody-w.github.io/RAPP/installer/install.sh | bash` "
                "then `rapp-brainstem start`."
            )
            diagnostics["remedies"].append(
                "OR set AZURE_OPENAI_ENDPOINT + AZURE_OPENAI_API_KEY + "
                "AZURE_OPENAI_DEPLOYMENT, OR OPENAI_API_KEY."
            )

    # 2. Writable workspaces?
    for path, label in [(LEVIATHANS_ROOT, "leviathans root"),
                        (ESTATES_ROOT, "estates root"),
                        (PIDS_DIR, "pids dir")]:
        try:
            path.mkdir(parents=True, exist_ok=True)
            diagnostics["checks"].append({
                "name": label, "status": "ok",
                "detail": f"writable at {path}",
            })
        except OSError as e:
            diagnostics["ok"] = False
            diagnostics["checks"].append({
                "name": label, "status": "fail",
                "detail": f"cannot create {path}: {e}",
            })

    # 3. Smoke test the LLM with a 1-token round-trip
    if diagnostics["ok"]:
        try:
            probe = _llm_call("You reply with exactly one word.",
                              "Reply: pong", timeout=30, retries=1)
            if "pong" in probe.lower():
                diagnostics["checks"].append({
                    "name": "LLM round-trip", "status": "ok",
                    "detail": f"smoke test passed: {probe.strip()[:40]!r}",
                })
            else:
                diagnostics["checks"].append({
                    "name": "LLM round-trip", "status": "warn",
                    "detail": f"unexpected response: {probe.strip()[:80]!r}",
                })
        except Exception as e:
            diagnostics["ok"] = False
            diagnostics["checks"].append({
                "name": "LLM round-trip", "status": "fail",
                "detail": f"smoke test failed: {e}",
            })

    diagnostics["verdict"] = (
        "READY — call action='generate' to build a Leviathan."
        if diagnostics["ok"] else
        "NOT READY — see remedies above."
    )
    return diagnostics


# ─── SOUL constants — internal personas ─────────────────────────────────────

_SOUL_INCARNATOR = """You are the Incarnator persona of the RappLeviathanFactory.

Given a user's intent, you decide WHICH estates the Leviathan needs.
A full Leviathan has all five estates (Sanctum/Polity/Works/Press/Commons).
A partial Leviathan has 1-4. You pick based on what the user actually
needs — never bloat.

Estate map:
  1 Sanctum — identity, memory, twins        (the soul)
  2 Polity  — governance, decisions          (the will)
  3 Works   — production, content/code/ops   (the hands)
  4 Press   — judgment, publication          (the eyes)
  5 Commons — federation, peer exchange      (the mouth)

Output STRICT JSON only — no markdown, no preamble:

{
  "name": "...",
  "tagline": "...",
  "estates": [1,3,4],
  "rationale": "<one short paragraph: why these estates and not the others>"
}

Pick 'estates' as a SUBSET of [1,2,3,4,5]. Always include rationale.
If the intent is broad ("a complete digital twin"), pick all 5."""


_SOUL_ARCHITECT = """You are the Architect persona of the RappLeviathanFactory.

Given a user's intent and a chosen estate type (1-5), you design the
estate's org chart: industries → neighborhoods → factories → persona souls.

You ALWAYS start from the estate type's default template (provided to
you inline) and extend it based on intent. You may add industries,
rename neighborhoods, add factories, and add personas. You do NOT
shrink the template — every default stays.

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

Slugs: lowercase_with_underscores. Names: Title Case. Tagline: one short
sentence. Souls list: 2-6 personas per factory."""


_SOUL_SOULWRITER = """You are the SoulWriter persona of the EstateFactory.

You write ONE soul prompt for ONE persona inside ONE factory.

Rules for the soul:
  - 80-300 words.
  - Open with "You are the <persona> persona of the <factory> factory."
  - State the persona's job in concrete terms.
  - List 3-5 hard rules (numbered).
  - End with the output format ("Output ONLY X, no preamble").
  - Voice should match the persona's role.

Output ONLY the soul text. No commentary, no markdown fences."""


_SOUL_REVIEWER = """You are the Reviewer persona of the EstateFactory.

You read a designed estate (the JSON tree) and return ONE of:
  - "READY: <one-line reason>"
  - "FIX: <what to fix>"

Check for:
  - Every industry has at least one neighborhood
  - Every neighborhood has at least one factory
  - Every factory has at least 2 souls
  - No duplicate slugs at any level
  - Names and slugs match in spirit

Output ONLY the verdict line."""


_SOUL_ANATOMIST = """You are the Anatomist persona of the RappLeviathanFactory.

You write a short anatomy plate — the one-paragraph description of THIS
specific Leviathan as a single being: which organs it has, which it
lacks, and what it can therefore do (and cannot do).

Rules:
  - One paragraph, 60-120 words.
  - Refer to it as "this Leviathan" or by its name.
  - Mention each present organ by body-part name (soul, will, hands,
    eyes, mouth) AND by estate name.
  - If an organ is missing, name what capability is missing.
  - End with: "This Leviathan can <X> but cannot <Y>."

Output ONLY the paragraph."""


# ─── EstateFactory (inlined, was separate file) ─────────────────────────────

def _classify_intent_for_estate(intent: str, explicit_type: int | None) -> int:
    """Pick estate type 1-5. Explicit wins; else heuristic by keywords."""
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
    return best if scores[best] > 0 else 3


def _factory_template(factory_id: str, factory_name: str,
                      factory_tagline: str, souls: list,
                      estate_name: str, neighborhood_name: str) -> str:
    """Render the agent.py source for one generated factory."""
    class_name = re.sub(r"[^A-Za-z0-9]", "", factory_name.title()) or "Generated"
    souls_calls = "\n".join(
        f'        out = _run_persona({json.dumps(s)}, out)' for s in souls
    )
    souls_meta = ", ".join(json.dumps(s) for s in souls)
    return f'''"""
{factory_id}/agent.py — generated factory for "{factory_name}"
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
    "industry": "leviathan-generated",
    "tags": ["composite", "leviathan-factory", "generated"],
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


class {class_name}({class_name}Agent):
    pass
'''


def _write_factory_files(factory_dir: pathlib.Path, factory: dict,
                         estate_name: str, neighborhood_name: str) -> None:
    factory_dir.mkdir(parents=True, exist_ok=True)
    (factory_dir / "souls").mkdir(exist_ok=True)
    src = _factory_template(
        factory_id=factory["id"],
        factory_name=factory.get("name", factory["id"].title()),
        factory_tagline=factory.get("tagline", "Generated factory."),
        souls=factory["souls"],
        estate_name=estate_name,
        neighborhood_name=neighborhood_name,
    )
    (factory_dir / "agent.py").write_text(src)
    _save_json(factory_dir / "manifest.json", {
        "id": factory["id"],
        "name": factory.get("name", factory["id"]),
        "tagline": factory.get("tagline", ""),
        "personas": factory["souls"],
        "industry": "leviathan-generated",
    })
    for soul_name in factory["souls"]:
        path = factory_dir / "souls" / f"{soul_name}.md"
        if not path.exists():
            path.write_text(f"(soul for {soul_name} — pending generation)")


def _generate_soul(persona_name: str, factory_name: str,
                   estate_name: str) -> str:
    prompt = (f"Persona: {persona_name}\n"
              f"Factory: {factory_name}\n"
              f"Estate: {estate_name}\n\n"
              f"Write the soul for this persona. Output ONLY the soul text.")
    return _llm_call(_SOUL_SOULWRITER, prompt)


def _design_estate(intent: str, type: int | None, name: str | None) -> dict:
    """Design one estate's tree via the Architect persona."""
    chosen = _classify_intent_for_estate(intent, type)
    template = ESTATE_TYPES[chosen]
    ask = (
        f"User intent:\n{intent}\n\n"
        f"Estate type chosen: {chosen} ({template['name']})\n"
        f"Domain: {template['domain']}\n\n"
        f"Default template (extend, don't shrink):\n"
        f"{json.dumps(template['default_industries'], indent=2)}\n\n"
        f"Suggested name slug: {_slugify(name) if name else 'estate'}\n\n"
        f"Design the estate JSON tree. Output STRICT JSON only."
    )
    raw = _llm_call(_SOUL_ARCHITECT, ask)
    parsed = _parse_json_strict(raw) or {}
    parsed.setdefault("type", chosen)
    parsed.setdefault("name", name or "estate")
    # If model failed, fall back to the raw default template
    if not parsed.get("industries"):
        parsed["industries"] = template["default_industries"]
    return parsed


def _generate_estate(intent: str, name: str, type: int | None = None,
                     write_souls: bool = True) -> dict:
    """End-to-end generation of one estate's filesystem footprint."""
    estate = _design_estate(intent, type, name)
    estate["rappid"] = str(uuid.uuid4())
    estate["created_at"] = _now()
    estate["intent"] = intent

    verdict = _llm_call(_SOUL_REVIEWER,
                        f"Review this estate:\n{json.dumps(estate, indent=2)}")
    if verdict.upper().startswith("FIX:"):
        return {"status": "error", "message": f"reviewer rejected: {verdict}",
                "estate": estate}

    ws = _estate_workspace(name)
    _save_json(ws / "rappid.json", {
        "rappid": estate["rappid"], "type": estate["type"],
        "name": estate["name"], "created_at": estate["created_at"],
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
                            soul_name,
                            fac.get("name", fac["id"]),
                            estate["name"],
                        )
                        (fac_dir / "souls" / f"{soul_name}.md").write_text(soul_text)
                        souls_written += 1

    (ws / "estate.html").write_text(_render_estate_html(estate))
    return {
        "status": "ok", "name": estate["name"], "type": estate["type"],
        "rappid": estate["rappid"], "workspace": str(ws),
        "factories_written": factories_written,
        "souls_written": souls_written,
        "dashboard": f"file://{ws}/estate.html",
        "reviewer_verdict": verdict,
    }


# ─── Anatomy frame ──────────────────────────────────────────────────────────

_ANATOMY_FRAME = """
            ╭───────────╮
            │   SOUL    │   ← 1st Estate · Sanctum
            │  (1st)    │     Who am I?
            ╰─────┬─────╯
                  │
            ╭─────┴─────╮
            │   WILL    │   ← 2nd Estate · Polity
            │  (2nd)    │     What shall I do?
            ╰─────┬─────╯
                  │
        ┌─────────┴─────────┐
   ╭────┴────╮         ╭────┴────╮
   │  HANDS  │         │  EYES   │
   │ (3rd)   │         │ (4th)   │
   ╰────┬────╯         ╰────┬────╯
        │                   │
        └─────────┬─────────┘
                  │
            ╭─────┴─────╮
            │  MOUTH    │   ← 5th Estate · Commons
            │  (5th)    │     Who shall I speak to?
            ╰───────────╯
"""


def _render_anatomy(estates_present: list[int]) -> str:
    out = _ANATOMY_FRAME
    for n in range(1, 6):
        marker = f"({['1st','2nd','3rd','4th','5th'][n-1]})"
        if n not in estates_present:
            out = out.replace(marker,
                              f"({['1st','2nd','3rd','4th','5th'][n-1]} ✕)")
    return out


# ─── HTML templates ─────────────────────────────────────────────────────────

_ESTATE_HTML = """<!DOCTYPE html>
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
    return _ESTATE_HTML.format(
        name=estate["name"], tagline=estate.get("tagline", ""),
        type=estate.get("type", "?"), rappid=estate.get("rappid", "?"),
        body_html="\n".join(parts),
    )


_LEVIATHAN_HTML = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<title>{name} — Rapp Leviathan</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0a0a0f;color:#c8c8c8;font-family:'SF Mono','Fira Code','Consolas',monospace;font-size:13px;padding:18px;max-width:1200px;margin:0 auto}}
h1{{color:#00ff88;font-size:24px;letter-spacing:2px;margin-bottom:4px}}
.sub{{color:#555;font-size:11px;margin-bottom:18px}}
.sub .rappid{{color:#888;font-family:monospace}}
.banner{{background:#0d0d14;border:1px solid #1a1a2a;border-radius:8px;padding:14px;margin-bottom:16px}}
.banner .tag{{color:#d2a8ff;font-size:11px;text-transform:uppercase;letter-spacing:2px;margin-bottom:4px}}
.banner .para{{color:#aaa;line-height:1.5;font-size:13px}}
.anatomy{{background:#0d0d14;border:1px solid #1a1a2a;border-radius:8px;padding:14px;margin-bottom:16px;overflow-x:auto}}
.anatomy pre{{color:#e8c87a;font-family:inherit;font-size:11px;line-height:1.3;white-space:pre}}
.organs{{display:grid;grid-template-columns:repeat(5, 1fr);gap:10px;margin-bottom:16px}}
@media (max-width:1000px){{.organs{{grid-template-columns:repeat(2,1fr)}}}}
.organ{{background:#111118;border:1px solid #222;border-radius:8px;padding:14px;min-height:180px}}
.organ.present{{border-color:#1a3a1a;background:#0d1a14}}
.organ.absent{{opacity:.35}}
.organ .num{{color:#888;font-size:10px;letter-spacing:2px;text-transform:uppercase}}
.organ .body{{color:#e8c87a;font-size:18px;margin:4px 0 8px;letter-spacing:1px;text-transform:uppercase}}
.organ.present .body{{color:#00ff88}}
.organ .name{{color:#fff;font-size:13px;font-weight:bold;margin-bottom:4px}}
.organ .q{{color:#888;font-size:11px;font-style:italic;margin-bottom:8px}}
.organ .domain{{color:#666;font-size:10px;line-height:1.4;margin-bottom:8px}}
.organ a{{color:#4488ff;font-size:11px}}
.full-banner{{background:linear-gradient(90deg,#0d1a14,#1a0d1a,#0d1a14);border:1px solid #2a4a3a;border-radius:8px;padding:10px 14px;margin-bottom:16px;color:#00ff88;font-size:12px;letter-spacing:1px}}
</style></head><body>
<h1>{name}</h1>
<div class="sub">{tagline} · rappid <span class="rappid">{rappid}</span></div>
{full_banner}
<div class="banner"><div class="tag">Anatomy</div><div class="para">{anatomy_paragraph}</div></div>
<div class="anatomy"><pre>{anatomy_ascii}</pre></div>
<div class="organs">
{organ_cards}
</div>
<div class="banner"><div class="tag">Rationale</div><div class="para">{rationale}</div></div>
</body></html>
"""


def _render_leviathan_html(lev: dict) -> str:
    organ_lookup = {o["estate_type"]: o for o in lev.get("organs", [])}
    cards = []
    for n in [1, 2, 3, 4, 5]:
        meta = ESTATE_TYPES[n]
        if n in organ_lookup:
            o = organ_lookup[n]
            cards.append(f"""
        <div class="organ present">
          <div class="num">{['1ST','2ND','3RD','4TH','5TH'][n-1]} ESTATE</div>
          <div class="body">{meta['organ']}</div>
          <div class="name">{meta['name'].split('—')[-1].strip()}</div>
          <div class="q">{meta['question']}</div>
          <div class="domain">{meta['domain']}</div>
          <a href="file://{o.get('workspace', '')}/estate.html">open dashboard ↗</a>
        </div>""")
        else:
            cards.append(f"""
        <div class="organ absent">
          <div class="num">{['1ST','2ND','3RD','4TH','5TH'][n-1]} ESTATE</div>
          <div class="body">{meta['organ']}</div>
          <div class="name">{meta['name'].split('—')[-1].strip()}</div>
          <div class="q">{meta['question']}</div>
          <div class="domain">(absent)</div>
        </div>""")
    full = lev.get("is_full_leviathan", False)
    full_banner = ('<div class="full-banner">★ FULL LEVIATHAN — all five organs present. This entity can think, decide, do, see, and speak.</div>'
                   if full else
                   f'<div class="full-banner" style="opacity:.6">PARTIAL LEVIATHAN — {len(lev.get("estates_present", []))}/5 organs.</div>')
    return _LEVIATHAN_HTML.format(
        name=lev["name"], tagline=lev.get("tagline", ""),
        rappid=lev["rappid"], full_banner=full_banner,
        anatomy_paragraph=lev.get("anatomy_paragraph", ""),
        anatomy_ascii=(lev.get("anatomy_ascii", "") or "").replace("<", "&lt;"),
        organ_cards="\n".join(cards),
        rationale=lev.get("rationale", ""),
    )


def _render_readme(lev: dict, ws: pathlib.Path) -> str:
    organs_md = "\n".join(
        f"- **{o['estate_type_name']}** — organ: {o['organ']} — "
        f"{o.get('factories_written', '?')} factories  \n"
        f"  workspace: `{o.get('workspace', '?')}`  \n"
        f"  dashboard: `{o.get('dashboard', '?')}`"
        for o in lev.get("organs", [])
    )
    return f"""# {lev['name']} — Rapp Leviathan

**Rappid:** `{lev['rappid']}`
**Status:** {'FULL Leviathan' if lev.get('is_full_leviathan') else 'PARTIAL Leviathan'}
**Created:** {lev.get('created_at', '?')}

## Intent
> {lev.get('intent', '(no intent recorded)')}

## Anatomy

{lev.get('anatomy_paragraph', '')}

```
{lev.get('anatomy_ascii', '')}
```

## Organs

{organs_md}

## Rationale

{lev.get('rationale', '')}

## Next steps

1. Open `leviathan.html` for the dashboard.
2. For each organ, open its `estate.html`.
3. Bring it to life: `RappLeviathanFactory(action="provision", name="{_slugify(lev['name'])}")`.
"""


# ─── The agent ──────────────────────────────────────────────────────────────

class RappLeviathanFactoryAgent(BasicAgent):

    def __init__(self):
        self.name = "RappLeviathanFactory"
        self.metadata = {
            "name": self.name,
            "description": (
                "Generate a Rapp Leviathan — an operator's complete digital "
                "being — by composing 1-5 estates under one top-level "
                "rappid. SELF-CONTAINED v0.2.0: no sibling-file deps.\n\n"
                "Body parts (estates):\n"
                "  1 Sanctum = soul   (identity, memory)\n"
                "  2 Polity  = will   (governance, decisions)\n"
                "  3 Works   = hands  (production, content/code/ops)\n"
                "  4 Press   = eyes   (judgment, publication)\n"
                "  5 Commons = mouth  (federation, peers)\n\n"
                "Actions:\n"
                "  bootstrap_check - verify env can generate (call FIRST)\n"
                "  design          - preview without writing\n"
                "  generate        - write the full Leviathan to disk\n"
                "  provision       - register pid markers (inline, no scripts)\n"
                "  tour            - drill an existing Leviathan\n"
                "  anatomy         - just the anatomy paragraph + ascii\n"
                "  list            - all Leviathans on this box"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["bootstrap_check", "design",
                                        "generate", "provision", "tour",
                                        "anatomy", "list"]},
                    "intent": {"type": "string",
                               "description": "What the Leviathan should do."},
                    "name": {"type": "string",
                             "description": "Slug for the Leviathan."},
                    "estates": {"type": "array",
                                "items": {"type": "integer", "minimum": 1,
                                          "maximum": 5},
                                "description": "Subset of [1..5]. Optional."},
                    "write_souls": {"type": "boolean",
                                    "description": "Generate real soul prompts. Default true."},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── action: bootstrap_check ───────────────────────────────────────────

    def _bootstrap_check(self, **_):
        d = bootstrap_check()
        return json.dumps({"status": "ok", "action": "bootstrap_check", **d},
                          indent=2)

    # ── action: design ────────────────────────────────────────────────────

    def _design(self, intent="", **_):
        if not intent:
            return json.dumps({"status": "error",
                "message": "intent required for design."})
        raw = _llm_call(_SOUL_INCARNATOR, f"Intent:\n{intent}\n\nDecide.")
        plan = _parse_json_strict(raw)
        if not plan:
            return json.dumps({"status": "error",
                "message": "incarnator returned non-JSON",
                "raw_preview": raw[:300]})
        estates = sorted({int(n) for n in plan.get("estates", [])
                          if 1 <= int(n) <= 5})
        plan["estates"] = estates
        plan["organs"] = [{"type": n, **ESTATE_TYPES[n]} for n in estates]
        plan["anatomy_ascii"] = _render_anatomy(estates)
        present_names = ", ".join(ESTATE_TYPES[n]["name"] for n in estates)
        absent = [n for n in [1,2,3,4,5] if n not in estates]
        anatomy_ask = (
            f"Leviathan name: {plan.get('name', 'unnamed')}\n"
            f"Tagline: {plan.get('tagline', '')}\n"
            f"Estates present: {present_names or '(none)'}\n"
            f"Estates missing: "
            f"{', '.join(ESTATE_TYPES[n]['name'] for n in absent) or 'none — full Leviathan'}\n\n"
            f"Write the anatomy paragraph."
        )
        plan["anatomy_paragraph"] = _llm_call(_SOUL_ANATOMIST, anatomy_ask)
        return json.dumps({"status": "ok", "action": "design",
                           "plan": plan}, indent=2)

    # ── action: generate ──────────────────────────────────────────────────

    def _generate(self, intent="", name=None, estates=None,
                  write_souls=True, **_):
        if not intent or not name:
            return json.dumps({"status": "error",
                "message": "intent + name required for generate."})

        # Pre-flight: bootstrap_check (fail fast if env can't deliver)
        diag = bootstrap_check()
        if not diag["ok"]:
            return json.dumps({"status": "error",
                "message": "bootstrap_check failed — cannot generate.",
                "diagnostics": diag})

        # Phase 1: design (Incarnator + Anatomist)
        designed = json.loads(self._design(intent=intent))
        if designed.get("status") != "ok":
            return json.dumps(designed)
        plan = designed["plan"]
        chosen = estates if estates else plan["estates"]
        chosen = sorted({int(n) for n in chosen if 1 <= int(n) <= 5})
        if not chosen:
            return json.dumps({"status": "error",
                "message": "no estates selected"})

        # Phase 2: top-level rappid + workspace
        ws = _leviathan_workspace(name)
        leviathan_rappid = str(uuid.uuid4())
        _save_json(ws / "rappid.json", {
            "rappid": leviathan_rappid, "scale": "leviathan",
            "name": plan.get("name", name),
            "created_at": _now(), "intent": intent,
        })

        # Phase 3: generate each estate INLINE (no sibling factory call)
        organ_results = []
        for n in chosen:
            estate_slug = f"{_slugify(name)}_{ESTATE_TYPES[n]['slug']}"
            r = _generate_estate(
                intent=f"{intent}\n\n(Generating the "
                       f"{ESTATE_TYPES[n]['organ']} organ — "
                       f"{ESTATE_TYPES[n]['name']}: "
                       f"{ESTATE_TYPES[n]['domain']}.)",
                name=estate_slug,
                type=n,
                write_souls=write_souls,
            )
            r["estate_type"] = n
            r["organ"] = ESTATE_TYPES[n]["organ"]
            r["estate_type_name"] = ESTATE_TYPES[n]["name"]
            organ_results.append(r)

        # Phase 4: leviathan.json (composite)
        leviathan = {
            "rappid": leviathan_rappid,
            "name": plan.get("name", name),
            "tagline": plan.get("tagline", ""),
            "intent": intent,
            "created_at": _now(),
            "rationale": plan.get("rationale", ""),
            "anatomy_paragraph": plan.get("anatomy_paragraph", ""),
            "anatomy_ascii": _render_anatomy(chosen),
            "organs": [{
                "estate_type": r["estate_type"],
                "estate_type_name": r["estate_type_name"],
                "organ": r["organ"],
                "estate_slug": r.get("name"),
                "rappid": r.get("rappid"),
                "workspace": r.get("workspace"),
                "dashboard": r.get("dashboard"),
                "factories_written": r.get("factories_written"),
                "status": r.get("status"),
            } for r in organ_results],
            "estates_present": chosen,
            "estates_missing": [n for n in [1,2,3,4,5] if n not in chosen],
            "is_full_leviathan": chosen == [1, 2, 3, 4, 5],
        }
        _save_json(ws / "leviathan.json", leviathan)
        (ws / "leviathan.html").write_text(_render_leviathan_html(leviathan))
        (ws / "README.md").write_text(_render_readme(leviathan, ws))

        return json.dumps({
            "status": "ok", "action": "generate",
            "name": leviathan["name"], "rappid": leviathan_rappid,
            "workspace": str(ws),
            "is_full_leviathan": leviathan["is_full_leviathan"],
            "organs_built": len(organ_results),
            "estates_present": chosen,
            "dashboard": f"file://{ws}/leviathan.html",
            "anatomy_ascii": leviathan["anatomy_ascii"],
            "anatomy_paragraph": leviathan["anatomy_paragraph"],
            "organ_summaries": organ_results,
        }, indent=2)

    # ── action: provision (inline — no external script) ───────────────────

    def _provision(self, name=None, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required."})
        ws = _leviathan_workspace(name)
        lev = _load_json(ws / "leviathan.json", None)
        if not lev:
            return json.dumps({"status": "error",
                "message": f"Leviathan '{name}' not generated yet."})
        PIDS_DIR.mkdir(parents=True, exist_ok=True)
        markers = []
        # Top-level Leviathan marker (stub pid 0 = not yet alive)
        slug = _slugify(name)
        lev_marker = PIDS_DIR / f"{slug}_leviathan_0_rap.pid"
        lev_marker.write_text("0")
        markers.append(str(lev_marker))
        # One marker per factory across all organs
        for o in lev.get("organs", []):
            estate_slug = o.get("estate_slug") or f"{slug}_{o['organ']}"
            estate_ws = _estate_workspace(estate_slug)
            estate_json = _load_json(estate_ws / "estate.json", {})
            for ind in estate_json.get("industries", []):
                for nb in ind.get("neighborhoods", []):
                    for fac in nb.get("factories", []):
                        fid = fac["id"]
                        marker = PIDS_DIR / f"{slug}_{fid}_0_rap.pid"
                        marker.write_text("0")
                        markers.append(str(marker))
        return json.dumps({
            "status": "ok", "action": "provision",
            "name": lev["name"],
            "markers_written": len(markers),
            "pids_dir": str(PIDS_DIR),
            "note": (
                "These are STUB markers (pid 0 = not yet alive). To bring "
                "each factory to life, run its agent.py inside a RAPP brainstem "
                "and replace the stub marker with the real <slug>_<pid>_rap.pid "
                "file containing the live process's pid."
            ),
        }, indent=2)

    # ── action: tour ──────────────────────────────────────────────────────

    def _tour(self, name=None, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required."})
        lev = _load_json(_leviathan_workspace(name) / "leviathan.json", None)
        if not lev:
            return json.dumps({"status": "error",
                "message": f"Leviathan '{name}' not found."})
        lines = [
            f"{lev['name']}  (rappid: {lev['rappid']})",
            f"  tagline: {lev.get('tagline', '')}",
            f"  full Leviathan: {lev['is_full_leviathan']}",
            f"  organs present: {lev['estates_present']}",
            f"  organs missing: {lev['estates_missing']}",
            "",
            "ANATOMY",
            lev.get("anatomy_paragraph", ""),
            "",
            "ORGANS",
        ]
        for o in lev.get("organs", []):
            lines.append(f"  {o['estate_type_name']} → {o['organ']} "
                         f"({o.get('factories_written', '?')} factories)")
            lines.append(f"    workspace: {o.get('workspace', '?')}")
        lines.append("")
        lines.append(lev.get("anatomy_ascii", ""))
        return json.dumps({"status": "ok", "action": "tour",
                           "rendering": "\n".join(lines),
                           "leviathan": lev}, indent=2)

    # ── action: anatomy ───────────────────────────────────────────────────

    def _anatomy(self, name=None, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required."})
        lev = _load_json(_leviathan_workspace(name) / "leviathan.json", None)
        if not lev:
            return json.dumps({"status": "error",
                "message": f"Leviathan '{name}' not found."})
        return json.dumps({
            "status": "ok", "action": "anatomy",
            "name": lev["name"],
            "anatomy_ascii": lev.get("anatomy_ascii", ""),
            "anatomy_paragraph": lev.get("anatomy_paragraph", ""),
            "estates_present": lev.get("estates_present", []),
            "estates_missing": lev.get("estates_missing", []),
            "is_full_leviathan": lev.get("is_full_leviathan", False),
        }, indent=2)

    # ── action: list ──────────────────────────────────────────────────────

    def _list(self, **_):
        out = []
        if LEVIATHANS_ROOT.exists():
            for d in sorted(LEVIATHANS_ROOT.iterdir()):
                if not d.is_dir():
                    continue
                lev = _load_json(d / "leviathan.json", None)
                if not lev:
                    continue
                out.append({
                    "slug": d.name, "name": lev.get("name"),
                    "rappid": lev.get("rappid"),
                    "organs_present": lev.get("estates_present", []),
                    "is_full": lev.get("is_full_leviathan", False),
                    "workspace": str(d),
                })
        return json.dumps({"status": "ok", "action": "list",
                           "leviathans": out, "count": len(out)},
                          indent=2)

    # ── dispatch ──────────────────────────────────────────────────────────

    def perform(self, action="list", **kwargs):
        try:
            if action == "bootstrap_check": return self._bootstrap_check(**kwargs)
            if action == "design":          return self._design(**kwargs)
            if action == "generate":        return self._generate(**kwargs)
            if action == "provision":       return self._provision(**kwargs)
            if action == "tour":            return self._tour(**kwargs)
            if action == "anatomy":         return self._anatomy(**kwargs)
            if action == "list":            return self._list(**kwargs)
            return json.dumps({"status": "error",
                "message": f"unknown action '{action}'."})
        except Exception as e:
            return json.dumps({"status": "error", "exception": str(e)})


class RappLeviathanFactory(RappLeviathanFactoryAgent):
    pass
