"""rapp_leviathan_factory_agent.py — generate a complete Rapp Leviathan
from intent. One drop-in agent.py.

A **Rapp Leviathan** is one operator's full digital being — composed of
up to five estates (the five classical estates applied to digital
labor). This factory composes EstateFactory five times under one top-
level rappid and a single five-organ dashboard.

Mapping
=======

  Estate (organ)         Body part   Question it answers
  ─────────────────      ─────────   ────────────────────
  1st  — Sanctum         soul        Who am I?
  2nd  — Polity          will        What shall I do?
  3rd  — Works           hands       What shall I make?
  4th  — Press           eyes        What is true?
  5th  — Commons         mouth       Who shall I speak to?

A partial Leviathan (1-2 estates) is a fragment. A full Leviathan has all
five and can think, decide, do, see, and speak as one being.

Pair concept
============

  EstateFactory.generate(type=N)        → one estate (one organ)
  RappLeviathanFactory.generate(...)    → the whole body, composed

API
===

  RappLeviathanFactory(action="design",   intent="...")
  RappLeviathanFactory(action="generate", intent="...", name="kody",
                       estates=[1,2,3,4,5])  # subset OK
  RappLeviathanFactory(action="tour",     name="kody")
  RappLeviathanFactory(action="list")
  RappLeviathanFactory(action="anatomy",  name="kody")   # ascii body

Workspace
=========

  ~/.rapp/leviathans/<slug>/
    leviathan.json    — composite: which estates, links to each
    rappid.json       — top-level UUIDv4 (the Leviathan's permanent identity)
    leviathan.html    — five-organ anatomy dashboard
    README.md         — generated walkthrough

  Each sub-estate keeps its canonical workspace at ~/.rapp/estates/<estate-slug>/
  — the Leviathan is the registry that says "I own these organs."
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
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name, self.metadata = name, metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rapp_leviathan_factory",
    "version": "0.1.0",
    "display_name": "RappLeviathanFactory",
    "description": (
        "Generate a full Rapp Leviathan — an operator's complete digital "
        "being — by composing 1-5 estates (Sanctum/Polity/Works/Press/"
        "Commons) under a single top-level rappid and a five-organ "
        "anatomy dashboard."
    ),
    "author": "kody-w",
    "industry": "meta",
    "tags": ["meta", "factory", "leviathan", "estate", "composite",
             "anatomy", "rapplication", "singleton"],
    "category": "meta",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent", "@kody-w/estate_factory"],
    "example_call": {
        "args": {
            "action": "design",
            "intent": "I want a complete digital twin of me — remembers, decides, produces, judges, and speaks.",
        }
    },
}


# ─── Storage paths ──────────────────────────────────────────────────────────

LEVIATHANS_ROOT = pathlib.Path(os.environ.get(
    "RAPP_LEVIATHANS_ROOT",
    pathlib.Path.home() / ".rapp" / "leviathans",
))
ESTATES_ROOT = pathlib.Path(os.environ.get(
    "RAPP_ESTATES_ROOT",
    pathlib.Path.home() / ".rapp" / "estates",
))
PIDS_DIR = pathlib.Path(os.environ.get(
    "RAPP_PIDS_DIR",
    pathlib.Path.home() / ".rapp" / "pids",
))


# ─── Estate type table (mirrors estate_factory_agent.py) ────────────────────

ESTATE_TYPES = {
    1: {"slug": "sanctum",  "name": "1st Estate — Sanctum",
        "organ": "soul",  "question": "Who am I?",
        "domain": "identity, memory, twins, soul-keeping"},
    2: {"slug": "polity",   "name": "2nd Estate — Polity",
        "organ": "will",  "question": "What shall I do?",
        "domain": "governance, decisions, constitution, scenarios"},
    3: {"slug": "works",    "name": "3rd Estate — Works",
        "organ": "hands", "question": "What shall I make?",
        "domain": "production, labor, content/code/ops"},
    4: {"slug": "press",    "name": "4th Estate — Press",
        "organ": "eyes",  "question": "What is true?",
        "domain": "observation, judgment, publication, critique"},
    5: {"slug": "commons",  "name": "5th Estate — Commons",
        "organ": "mouth", "question": "Who shall I speak to?",
        "domain": "federation, cross-estate exchange, public square"},
}


# ─── Helpers ────────────────────────────────────────────────────────────────

def _slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9_]+", "_", (s or "").lower()).strip("_") or "leviathan"


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


def _workspace(name: str) -> pathlib.Path:
    ws = LEVIATHANS_ROOT / _slugify(name)
    ws.mkdir(parents=True, exist_ok=True)
    return ws


# ─── LLM dispatch (brainstem-first, retrying) ───────────────────────────────

BRAIN_URL = os.environ.get("RAPP_BRAINSTEM_URL", "http://localhost:7071/chat")


def _llm_call(system: str, user: str, timeout: int = 180, retries: int = 3) -> str:
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
    return "(no LLM available)"


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
If the intent is broad ("a complete digital twin of me"), pick all 5."""


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


# ─── Anatomy ASCII (visible everywhere — including the dashboard) ───────────

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
    """Render the anatomy frame with present organs filled, absent ones dimmed."""
    out = _ANATOMY_FRAME
    for n in range(1, 6):
        marker = f"({['1st','2nd','3rd','4th','5th'][n-1]})"
        if n not in estates_present:
            out = out.replace(marker, f"({['1st','2nd','3rd','4th','5th'][n-1]} ✕)")
    return out


# ─── EstateFactory invocation (best-effort import) ──────────────────────────

def _call_estate_factory(action: str, **kwargs) -> dict:
    """Invoke EstateFactory if it's loadable as a sibling agent, else
    return a stub. The contract: it accepts the same action verbs as the
    standalone agent (design/generate/provision/tour/list)."""
    try:
        # Same-directory import — works when both files live in @kody-w/
        import importlib.util
        here = pathlib.Path(__file__).resolve().parent
        spec = importlib.util.spec_from_file_location(
            "estate_factory_agent",
            here / "estate_factory_agent.py",
        )
        if not spec or not spec.loader:
            return {"status": "error", "message": "estate_factory_agent not found locally"}
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        agent = mod.EstateFactoryAgent()
        result = agent.perform(action=action, **kwargs)
        return json.loads(result) if isinstance(result, str) else result
    except Exception as e:
        return {"status": "error", "exception": str(e)}


# ─── The agent ──────────────────────────────────────────────────────────────

class RappLeviathanFactoryAgent(BasicAgent):

    def __init__(self):
        self.name = "RappLeviathanFactory"
        self.metadata = {
            "name": self.name,
            "description": (
                "Generate a Rapp Leviathan — an operator's complete digital "
                "being — by composing 1-5 estates under one top-level "
                "rappid.\n\n"
                "Body parts (estates):\n"
                "  1 Sanctum = soul   (identity, memory)\n"
                "  2 Polity  = will   (governance, decisions)\n"
                "  3 Works   = hands  (production, content/code/ops)\n"
                "  4 Press   = eyes   (judgment, publication)\n"
                "  5 Commons = mouth  (federation, peers)\n\n"
                "Actions: design, generate, provision, tour, anatomy, list."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["design", "generate", "provision",
                                        "tour", "anatomy", "list"]},
                    "intent": {"type": "string",
                               "description": "What the Leviathan should be able to do. Required for design + generate."},
                    "name": {"type": "string",
                             "description": "Slug for the Leviathan. Required for generate/provision/tour/anatomy."},
                    "estates": {"type": "array", "items": {"type": "integer", "minimum": 1, "maximum": 5},
                                "description": "Subset of [1..5] to compose. Optional; Incarnator infers from intent if omitted."},
                    "write_souls": {"type": "boolean",
                                    "description": "Whether to call SoulWriter for each persona soul. Default true (slower); false uses placeholders."},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── action: design ────────────────────────────────────────────────────

    def _design(self, intent="", **_):
        if not intent:
            return json.dumps({"status": "error",
                "message": "intent required for design."})
        raw = _llm_call(_SOUL_INCARNATOR, f"Intent:\n{intent}\n\nDecide.")
        s = raw.find("{"); e = raw.rfind("}")
        if s < 0 or e <= s:
            return json.dumps({"status": "error",
                "message": "incarnator returned non-JSON",
                "raw_preview": raw[:300]})
        try:
            plan = json.loads(raw[s:e+1])
        except json.JSONDecodeError as ex:
            return json.dumps({"status": "error",
                "message": f"incarnator JSON parse failed: {ex}"})
        estates = [int(n) for n in plan.get("estates", []) if 1 <= int(n) <= 5]
        plan["estates"] = sorted(set(estates))
        # Decorate with body-part labels for the dashboard
        plan["organs"] = [
            {"type": n, **ESTATE_TYPES[n]} for n in plan["estates"]
        ]
        plan["anatomy_ascii"] = _render_anatomy(plan["estates"])
        # Anatomy paragraph
        present_names = ", ".join(ESTATE_TYPES[n]["name"] for n in plan["estates"])
        anatomy_ask = (
            f"Leviathan name: {plan.get('name', 'unnamed')}\n"
            f"Tagline: {plan.get('tagline', '')}\n"
            f"Estates present: {present_names}\n"
            f"Estates missing: {', '.join(ESTATE_TYPES[n]['name'] for n in [1,2,3,4,5] if n not in plan['estates']) or 'none — this is a full Leviathan'}\n\n"
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

        # Phase 1: design
        designed = json.loads(self._design(intent=intent))
        if designed.get("status") != "ok":
            return json.dumps(designed)
        plan = designed["plan"]
        chosen = estates if estates else plan["estates"]
        chosen = sorted(set(int(n) for n in chosen if 1 <= int(n) <= 5))
        if not chosen:
            return json.dumps({"status": "error",
                "message": "no estates selected"})

        # Phase 2: top-level rappid + workspace
        ws = _workspace(name)
        leviathan_rappid = str(uuid.uuid4())
        _save_json(ws / "rappid.json", {
            "rappid": leviathan_rappid,
            "scale": "leviathan",
            "name": plan.get("name", name),
            "created_at": _now(),
            "intent": intent,
        })

        # Phase 3: generate each estate via EstateFactory
        organ_results = []
        for n in chosen:
            estate_slug = f"{_slugify(name)}_{ESTATE_TYPES[n]['slug']}"
            r = _call_estate_factory(
                "generate",
                intent=f"{intent}\n\n(Generating the {ESTATE_TYPES[n]['organ']} "
                       f"organ — {ESTATE_TYPES[n]['name']}: "
                       f"{ESTATE_TYPES[n]['domain']}.)",
                name=estate_slug,
                type=n,
                write_souls=write_souls,
            )
            r["estate_type"] = n
            r["organ"] = ESTATE_TYPES[n]["organ"]
            r["estate_type_name"] = ESTATE_TYPES[n]["name"]
            organ_results.append(r)

        # Phase 4: leviathan.json — the composite manifest
        leviathan = {
            "rappid": leviathan_rappid,
            "name": plan.get("name", name),
            "tagline": plan.get("tagline", ""),
            "intent": intent,
            "created_at": _now(),
            "rationale": plan.get("rationale", ""),
            "anatomy_paragraph": plan.get("anatomy_paragraph", ""),
            "anatomy_ascii": _render_anatomy(chosen),
            "organs": [
                {
                    "estate_type": r["estate_type"],
                    "estate_type_name": r["estate_type_name"],
                    "organ": r["organ"],
                    "estate_slug": r.get("name"),
                    "rappid": r.get("rappid"),
                    "workspace": r.get("workspace"),
                    "dashboard": r.get("dashboard"),
                    "factories_written": r.get("factories_written"),
                    "status": r.get("status"),
                }
                for r in organ_results
            ],
            "estates_present": chosen,
            "estates_missing": [n for n in [1,2,3,4,5] if n not in chosen],
            "is_full_leviathan": chosen == [1, 2, 3, 4, 5],
        }
        _save_json(ws / "leviathan.json", leviathan)

        # Phase 5: dashboard + readme
        (ws / "leviathan.html").write_text(_render_leviathan_html(leviathan))
        (ws / "README.md").write_text(_render_readme(leviathan, ws))

        return json.dumps({
            "status": "ok", "action": "generate",
            "name": leviathan["name"],
            "rappid": leviathan_rappid,
            "workspace": str(ws),
            "is_full_leviathan": leviathan["is_full_leviathan"],
            "organs_built": len(organ_results),
            "estates_present": chosen,
            "dashboard": f"file://{ws}/leviathan.html",
            "anatomy_ascii": leviathan["anatomy_ascii"],
            "anatomy_paragraph": leviathan["anatomy_paragraph"],
            "organ_summaries": organ_results,
        }, indent=2)

    # ── action: tour ──────────────────────────────────────────────────────

    def _tour(self, name=None, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required."})
        ws = _workspace(name)
        lev = _load_json(ws / "leviathan.json", None)
        if not lev:
            return json.dumps({"status": "error",
                "message": f"Leviathan '{name}' not found at {ws}"})
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
            lines.append(f"    dashboard: {o.get('dashboard', '?')}")
        lines.append("")
        lines.append(lev.get("anatomy_ascii", ""))
        return json.dumps({"status": "ok", "action": "tour",
                           "rendering": "\n".join(lines),
                           "leviathan": lev}, indent=2)

    # ── action: anatomy ───────────────────────────────────────────────────

    def _anatomy(self, name=None, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required."})
        lev = _load_json(_workspace(name) / "leviathan.json", None)
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

    # ── action: provision ─────────────────────────────────────────────────

    def _provision(self, name=None, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required."})
        ws = _workspace(name)
        lev = _load_json(ws / "leviathan.json", None)
        if not lev:
            return json.dumps({"status": "error",
                "message": f"Leviathan '{name}' not generated."})
        PIDS_DIR.mkdir(parents=True, exist_ok=True)
        # Register the Leviathan's own session rappid marker (no live process
        # yet — this is the placeholder for the orchestrator that pumps the
        # whole body when it's ready).
        marker = PIDS_DIR / f"{_slugify(name)}_leviathan_0_rap.pid"
        marker.write_text("0")
        provisioned_organs = []
        for o in lev.get("organs", []):
            # Each organ runs EstateFactory provision under the hood
            r = _call_estate_factory("provision", name=o.get("estate_slug", ""))
            provisioned_organs.append({
                "organ": o["organ"],
                "estate_type_name": o["estate_type_name"],
                "result_status": r.get("status"),
            })
        return json.dumps({
            "status": "ok", "action": "provision",
            "name": lev["name"],
            "leviathan_pid_marker": str(marker),
            "organs": provisioned_organs,
            "next_step": (
                "For each factory inside each organ, run provision-twin.sh "
                "to spin up a real brainstem. Each will register as "
                "<estate>_<factory>_<pid>_rap.pid in ~/.rapp/pids/."
            ),
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
                    "slug": d.name,
                    "name": lev.get("name"),
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
            if action == "design":
                return self._design(**kwargs)
            if action == "generate":
                return self._generate(**kwargs)
            if action == "provision":
                return self._provision(**kwargs)
            if action == "tour":
                return self._tour(**kwargs)
            if action == "anatomy":
                return self._anatomy(**kwargs)
            if action == "list":
                return self._list(**kwargs)
            return json.dumps({"status": "error",
                "message": f"unknown action '{action}'."})
        except Exception as e:
            return json.dumps({"status": "error", "exception": str(e)})


class RappLeviathanFactory(RappLeviathanFactoryAgent):
    pass


# ─── HTML dashboard renderer ────────────────────────────────────────────────

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
.organ .stat{{color:#888;font-size:10px;margin-top:4px}}
.summary-stats{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:16px}}
.stat{{background:#111118;border:1px solid #222;border-radius:8px;padding:8px 14px;text-align:center;min-width:90px}}
.stat .num{{font-size:1.6em;font-weight:bold;color:#00ff88}}
.stat .label{{font-size:9px;color:#555;text-transform:uppercase;letter-spacing:1px;margin-top:2px}}
.full-banner{{background:linear-gradient(90deg, #0d1a14, #1a0d1a, #0d1a14);border:1px solid #2a4a3a;border-radius:8px;padding:10px 14px;margin-bottom:16px;color:#00ff88;font-size:12px;letter-spacing:1px}}
</style></head><body>

<h1>{name}</h1>
<div class="sub">{tagline} · rappid <span class="rappid">{rappid}</span></div>

{full_banner}

<div class="summary-stats">
  <div class="stat"><div class="num">{n_present}/5</div><div class="label">Organs Present</div></div>
  <div class="stat"><div class="num">{n_factories}</div><div class="label">Factories</div></div>
</div>

<div class="banner">
  <div class="tag">Anatomy</div>
  <div class="para">{anatomy_paragraph}</div>
</div>

<div class="anatomy"><pre>{anatomy_ascii}</pre></div>

<div class="organs">
{organ_cards}
</div>

<div class="banner">
  <div class="tag">Rationale</div>
  <div class="para">{rationale}</div>
</div>

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
          <div class="stat">{o.get('factories_written', 0)} factories</div>
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
                   f'<div class="full-banner" style="opacity:.6">PARTIAL LEVIATHAN — {len(lev.get("estates_present", []))}/5 organs. Capabilities limited to present organs.</div>')
    n_factories = sum(o.get("factories_written", 0) or 0
                      for o in lev.get("organs", []))
    return _LEVIATHAN_HTML.format(
        name=lev["name"],
        tagline=lev.get("tagline", ""),
        rappid=lev["rappid"],
        full_banner=full_banner,
        n_present=len(lev.get("estates_present", [])),
        n_factories=n_factories,
        anatomy_paragraph=lev.get("anatomy_paragraph", ""),
        anatomy_ascii=lev.get("anatomy_ascii", "").replace("<", "&lt;"),
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

## Rationale (why these estates, not others)

{lev.get('rationale', '')}

## Next steps

1. Open `leviathan.html` for the full anatomy dashboard.
2. For each organ, open its `estate.html` for that organ's industries.
3. To bring the Leviathan to life: `RappLeviathanFactory(action="provision", name="{_slugify(lev['name'])}")` then `provision-twin.sh` for each factory.

The Leviathan's permanent rappid (`{lev['rappid']}`) is the lineage
anchor — every organ, factory, and rapp underneath traces back to it.
This is what peer Leviathans see when they federate.
"""
