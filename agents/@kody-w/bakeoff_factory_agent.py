"""bakeoff_factory_agent.py — generic content-improvement bakeoff loop,
collapsed into ONE drop-in agent.py.

Mental model
============

You give it a task — ANY task that can be expressed as "produce some text
for these inputs" — and a handful of variant strategies. It runs a
continuous tournament:

  • Each ROUND: every variant generates one output for a randomly-chosen
    input from the task's input pool.
  • A JUDGE persona scores every output on a 0-10 rubric across the axes
    you defined (defaults to specificity / voice / hook / coverage / craft).
  • Every N rounds: the worst-performing variant is MUTATED by a mutator
    persona, which grafts ONE technique from the current best variant's
    prompt into the loser's prompt ("rising tide raises all boats").
  • Everything is persisted under ~/.rapp/bakeoffs/<name>/ so the loop
    survives restarts.

This is the loop that ran on Rappterbook's content engine for 24h and
moved the floor +7 points. It is platform-agnostic — drop it on a
codebase to evolve docstrings, on a marketing pipeline to evolve copy,
on a chatbot to evolve system prompts, on anything.

API
===

  BakeoffFactory(action="spawn",
                 name="post-quality",
                 task_description="Write one engaging Rappterbook post.",
                 input_pool=["topic A", "topic B", "topic C"],
                 variants=[
                     {"id": "v1", "name": "specificity",
                      "system": "Every claim names a concrete artifact..."},
                     {"id": "v2", "name": "voice",
                      "system": "First sentence echoes a conviction..."},
                 ],
                 rubric_axes=["specificity", "voice", "hook", "craft"],
                 control_system=None,      # raw model baseline (default: bare instruction)
                 rounds_per_mutation=3,
                 round_interval_s=240,
                 max_rounds=None)          # None = forever

  BakeoffFactory(action="round",  name="post-quality")  # one round on demand
  BakeoffFactory(action="status", name="post-quality")
  BakeoffFactory(action="report", name="post-quality", window=15)
  BakeoffFactory(action="stop",   name="post-quality")
  BakeoffFactory(action="list")

Storage
=======

  ~/.rapp/bakeoffs/<name>/
      config.json          — task spec, variants, rubric
      lineage.json         — every round + mutation + score
      variants/<id>.json   — current system prompts (mutated over time)
      generations/N.json   — per-round artifact
      logs/loop.log        — keepalive logs
      pump.pid             — pump process id (when running)

LLM dispatch
============

Tries local RAPP brainstem (http://localhost:7071/chat) first — the
preferred path because it gives you control over model choice (Opus 4.7,
GPT-5, Claude Sonnet, etc.) via the brainstem's /models/set endpoint.
Falls back to Azure/OpenAI from env vars. Has retry+backoff baked in
so a single brainstem hiccup doesn't kill a round.

Portability
===========

This file is self-contained Python. Only deps: `agents.basic_agent`
(any RAPP brainstem ships it) and stdlib. Drop it into any brainstem's
agents/ directory; auto-discovery picks it up; the model gets a tool
called `BakeoffFactory` with the action set above.
"""
from __future__ import annotations

import json
import os
import pathlib
import random
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from statistics import mean

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:                       # last-resort standalone
        def __init__(self, name, metadata):
            self.name, self.metadata = name, metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/bakeoff_factory",
    "version": "0.1.0",
    "display_name": "BakeoffFactory",
    "description": (
        "Generic content-improvement bakeoff loop. Variants compete on a "
        "task; a judge scores every output on a rubric; the worst variant "
        "evolves by grafting techniques from the best. Rising tide raises "
        "all boats. Drop it on any text-producing task."
    ),
    "author": "kody-w",
    "tags": ["meta", "evolution", "tournament", "loop", "self-improving",
             "composite", "rapplication"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {
        "args": {
            "action": "spawn",
            "name": "post-quality",
            "task_description": "Write one short, engaging social-media post.",
            "input_pool": ["productivity hacks", "AI agents", "weekend projects"],
            "variants": [
                {"id": "v1", "name": "concrete",
                 "system": "Open with a specific number or named thing. No abstractions."},
                {"id": "v2", "name": "voice",
                 "system": "Open with a strong opinion, defend it in one breath."},
            ],
            "rounds_per_mutation": 3,
        }
    },
}


# ─── Storage paths ──────────────────────────────────────────────────────────

ROOT = pathlib.Path(os.environ.get("RAPP_BAKEOFFS_ROOT",
                                   pathlib.Path.home() / ".rapp" / "bakeoffs"))


def _workspace(name: str) -> pathlib.Path:
    ws = ROOT / re.sub(r"[^a-zA-Z0-9._-]", "_", name)
    ws.mkdir(parents=True, exist_ok=True)
    (ws / "variants").mkdir(exist_ok=True)
    (ws / "generations").mkdir(exist_ok=True)
    (ws / "logs").mkdir(exist_ok=True)
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


def _llm_call(system: str, user: str, timeout: int = 120, retries: int = 3) -> str:
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
            url = (url.rstrip("/") +
                   f"/openai/deployments/{deployment}/chat/completions"
                   f"?api-version=2025-01-01-preview")
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


# ─── SOUL constants — the personas the loop calls ───────────────────────────

_SOUL_JUDGE = """You are a brutal but fair content judge. You score outputs on
a 0-10 rubric across the axes given to you. Return STRICT JSON only — no
markdown, no preamble.

Schema: {"<axis_1>": int, "<axis_2>": int, ..., "total": int,
         "verdict": "kill" | "keep" | "winner",
         "one_line_critique": str}

total = sum of axis scores. verdict = "kill" if total < (40% of max),
"winner" if total >= (75% of max), else "keep". Be honest. Generic AI-
voice prose is a 4, not a 6. Specific receipts beat eloquence."""


_SOUL_MUTATOR = """You evolve a content-generator's SYSTEM prompt to fix
specific failure modes — without losing its identity. You may cross-
pollinate: when shown a WINNER's prompt, lift ONE technique (a specific
clause, rule, or constraint) and graft it into the loser's prompt, keeping
the loser's identity intact.

Rising-tide principle: when the lowest-performing variant absorbs one
technique from the highest, the gap closes and the floor rises. Variants
stay distinct (different identities, different strategies); proven
techniques spread.

Rules:
- Change ONE thing. A targeted edit, not a rewrite.
- Preserve the variant's name and strategic identity.
- If a WINNER prompt is shown, lift exactly one technique from it.
- Length similar to the input.
- No commentary, no markdown, no preamble. Output ONLY the new SYSTEM body."""


_DEFAULT_CONTROL_SYSTEM = "You produce one short output for the user's task. Be concise. No preamble."


# ─── Bakeoff state helpers ──────────────────────────────────────────────────

def _config_path(ws: pathlib.Path) -> pathlib.Path:
    return ws / "config.json"


def _lineage_path(ws: pathlib.Path) -> pathlib.Path:
    return ws / "lineage.json"


def _variant_path(ws: pathlib.Path, vid: str) -> pathlib.Path:
    return ws / "variants" / f"{vid}.json"


def _load_variants(ws: pathlib.Path) -> dict:
    out = {}
    for path in sorted((ws / "variants").glob("*.json")):
        try:
            v = json.loads(path.read_text())
            out[v["id"]] = v
        except Exception:
            continue
    return out


def _judge_output(output: str, rubric_axes: list, max_per_axis: int = 10) -> dict:
    """Score an output via the judge persona. Returns normalized dict."""
    if not output or not output.strip():
        return {ax: 0 for ax in rubric_axes} | {
            "total": 0, "verdict": "kill",
            "one_line_critique": "empty output",
        }
    axes_text = ", ".join(rubric_axes)
    schema_keys = ", ".join(f'"{ax}": int' for ax in rubric_axes)
    judge_user = (
        f"Rubric axes (0-{max_per_axis} each): {axes_text}\n\n"
        f"Output to score:\n\n{output}\n\n"
        f"Return STRICT JSON: {{{schema_keys}, "
        f'"total": int, "verdict": "kill"|"keep"|"winner", '
        f'"one_line_critique": str}}'
    )
    try:
        raw = _llm_call(_SOUL_JUDGE, judge_user, timeout=90)
    except Exception as e:
        return {ax: 0 for ax in rubric_axes} | {
            "total": 0, "verdict": "kill",
            "one_line_critique": f"judge call failed: {e}",
        }
    s_idx = raw.find("{")
    e_idx = raw.rfind("}")
    if s_idx < 0 or e_idx <= s_idx:
        return {ax: 0 for ax in rubric_axes} | {
            "total": 0, "verdict": "kill",
            "one_line_critique": "judge returned non-JSON",
        }
    try:
        parsed = json.loads(raw[s_idx:e_idx + 1])
    except json.JSONDecodeError:
        return {ax: 0 for ax in rubric_axes} | {
            "total": 0, "verdict": "kill",
            "one_line_critique": "judge JSON parse failed",
        }
    max_total = max_per_axis * len(rubric_axes)
    for ax in rubric_axes:
        try:
            parsed[ax] = max(0, min(max_per_axis, int(parsed.get(ax, 0))))
        except (TypeError, ValueError):
            parsed[ax] = 0
    parsed["total"] = sum(parsed[ax] for ax in rubric_axes)
    if parsed["total"] >= int(0.75 * max_total):
        parsed["verdict"] = "winner"
    elif parsed["total"] < int(0.40 * max_total):
        parsed["verdict"] = "kill"
    else:
        parsed["verdict"] = parsed.get("verdict", "keep")
    parsed.setdefault("one_line_critique", "")
    return parsed


def _find_worst_variant(generations: list, rubric_axes: list) -> tuple:
    """Return (variant_id, [failing_axes]) for the worst non-control variant
    over the last 3 generations."""
    if len(generations) < 3:
        return None, []
    recent = generations[-3:]
    totals = defaultdict(list)
    fails = defaultdict(list)
    for g in recent:
        for vid, r in g.get("results", {}).items():
            if vid.startswith("control"):
                continue
            score = r.get("score") or {}
            totals[vid].append(score.get("total", 0))
            for ax in rubric_axes:
                if score.get(ax, 99) <= 4:
                    fails[vid].append(ax)
    if not totals:
        return None, []
    avgs = {vid: mean(t) for vid, t in totals.items()}
    worst = min(avgs, key=avgs.get)
    top_fails = [ax for ax, _ in Counter(fails.get(worst, [])).most_common(2)]
    return worst, top_fails


def _find_best_variant(generations: list, exclude: str | None = None) -> str | None:
    if len(generations) < 3:
        return None
    recent = generations[-3:]
    totals = defaultdict(list)
    for g in recent:
        for vid, r in g.get("results", {}).items():
            if vid.startswith("control") or vid == exclude:
                continue
            score = r.get("score") or {}
            totals[vid].append(score.get("total", 0))
    if not totals:
        return None
    avgs = {vid: mean(t) for vid, t in totals.items()}
    return max(avgs, key=avgs.get)


def _mutate_variant(ws: pathlib.Path, loser_id: str, winner_id: str | None,
                    failing_axes: list) -> dict:
    """Rewrite the loser's system via the mutator persona, with winner DNA."""
    loser_path = _variant_path(ws, loser_id)
    if not loser_path.exists():
        return {"ok": False, "error": "loser_missing"}
    loser = json.loads(loser_path.read_text())
    winner_clause = ""
    if winner_id:
        winner_path = _variant_path(ws, winner_id)
        if winner_path.exists():
            winner = json.loads(winner_path.read_text())
            winner_clause = (
                f"\n\nWINNER ('{winner_id}') SYSTEM — lift ONE technique:\n"
                f'"""\n{winner["system"]}\n"""'
            )
    ask = (
        f"Variant: {loser_id} ({loser.get('name', '')})\n"
        f"Failure axes: {', '.join(failing_axes) or 'general quality'}\n\n"
        f"CURRENT SYSTEM:\n\"\"\"\n{loser['system']}\n\"\"\"{winner_clause}\n\n"
        f"Rewrite the SYSTEM to address the failure axes. ONE targeted change.\n"
        f"If a WINNER is shown, graft exactly one of its techniques.\n"
        f"Output ONLY the new SYSTEM body."
    )
    try:
        new_body = _llm_call(_SOUL_MUTATOR, ask, timeout=120)
    except Exception as e:
        return {"ok": False, "error": f"llm: {e}"}
    new_body = new_body.strip().strip('"').strip("'").strip()
    if new_body.startswith("```"):
        new_body = new_body.split("\n", 1)[1] if "\n" in new_body else new_body
        new_body = new_body.rsplit("```", 1)[0].strip()
    if len(new_body) < 50 or len(new_body) > 6000:
        return {"ok": False, "error": "out_of_bounds_len"}
    loser["system"] = new_body
    loser["mutations"] = loser.get("mutations", 0) + 1
    loser.setdefault("history", []).append({
        "ts": _now(), "donor": winner_id,
        "failing_axes": failing_axes,
        "new_system_preview": new_body[:200],
    })
    _save_json(loser_path, loser)
    return {"ok": True, "donor": winner_id,
            "failing_axes": failing_axes,
            "new_system_preview": new_body[:200]}


def _run_one_round(ws: pathlib.Path, cfg: dict) -> dict:
    """Execute one bakeoff round. Returns the generation record."""
    variants = _load_variants(ws)
    if not variants:
        raise RuntimeError("no variants loaded")
    task_input = random.choice(cfg["input_pool"]) if cfg.get("input_pool") else ""
    task_template = cfg.get("task_template",
                            "Task: {task}\n\nInput: {input}\n\nProduce one output.")
    user_prompt = task_template.format(
        task=cfg["task_description"], input=task_input,
    )
    results = {}
    # Variants
    for vid, v in variants.items():
        try:
            out = _llm_call(v["system"], user_prompt, timeout=120)
            score = _judge_output(out, cfg["rubric_axes"])
            results[vid] = {
                "name": v.get("name", vid),
                "mutations": v.get("mutations", 0),
                "output": out,
                "score": score,
            }
        except Exception as e:
            results[vid] = {"error": str(e), "output": None, "score": None}
    # Control
    ctrl_system = cfg.get("control_system") or _DEFAULT_CONTROL_SYSTEM
    try:
        ctrl_out = _llm_call(ctrl_system, user_prompt, timeout=120)
        ctrl_score = _judge_output(ctrl_out, cfg["rubric_axes"])
        results["control"] = {"name": "control", "output": ctrl_out,
                              "score": ctrl_score, "mutations": 0}
    except Exception as e:
        results["control"] = {"error": str(e), "output": None, "score": None}

    return {
        "ts": _now(),
        "input": task_input,
        "results": results,
    }


# ─── The agent ──────────────────────────────────────────────────────────────

class BakeoffFactoryAgent(BasicAgent):

    def __init__(self):
        self.name = "BakeoffFactory"
        self.metadata = {
            "name": self.name,
            "description": (
                "Run a generic content-improvement bakeoff. Variants compete "
                "on a task; a judge scores every output on a rubric; the worst "
                "variant evolves by grafting techniques from the best.\n\n"
                "Actions:\n"
                " - spawn:  initialize a bakeoff with task + variants + rubric\n"
                " - round:  run one round on demand (returns scores)\n"
                " - report: render a meta-review of the last N rounds\n"
                " - status: snapshot of one bakeoff (rounds, mutations, gap)\n"
                " - stop:   halt the background pump for a bakeoff\n"
                " - list:   every bakeoff on this machine\n"
                " - pump:   start a background pump loop (forever)\n\n"
                "Storage lives under ~/.rapp/bakeoffs/<name>/. LLM dispatch "
                "tries the local brainstem first (so model choice is yours) "
                "and falls back to Azure/OpenAI."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["spawn", "round", "report",
                                        "status", "stop", "list", "pump"]},
                    "name": {"type": "string",
                             "description": "Bakeoff name (slug). Required for all but list."},
                    "task_description": {"type": "string",
                                         "description": "What every variant produces. Required for spawn."},
                    "input_pool": {"type": "array", "items": {"type": "string"},
                                   "description": "Inputs randomly sampled each round."},
                    "task_template": {"type": "string",
                                      "description": "Jinja-like {task}/{input} template. Optional."},
                    "variants": {"type": "array",
                                 "items": {"type": "object"},
                                 "description": "List of {id,name,system} for each competing strategy. Required for spawn."},
                    "rubric_axes": {"type": "array", "items": {"type": "string"},
                                    "description": "Axes the judge scores. Default: ['specificity','voice','hook','craft']."},
                    "control_system": {"type": "string",
                                       "description": "System prompt for the bare baseline control."},
                    "rounds_per_mutation": {"type": "integer",
                                            "description": "Mutate worst variant every N rounds. Default 3."},
                    "round_interval_s": {"type": "integer",
                                         "description": "Pump cadence in seconds. Default 240."},
                    "max_rounds": {"type": "integer",
                                   "description": "Stop after this many rounds (pump action). Default: forever."},
                    "window": {"type": "integer",
                               "description": "Report window. Default 15."},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── action: spawn ─────────────────────────────────────────────────────

    def _spawn(self, name, task_description, input_pool, variants,
               rubric_axes, control_system, rounds_per_mutation,
               round_interval_s, task_template, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required"})
        if not task_description:
            return json.dumps({"status": "error", "message": "task_description required"})
        if not variants or len(variants) < 2:
            return json.dumps({"status": "error",
                "message": "Provide at least 2 variants — bakeoff needs competitors."})

        ws = _workspace(name)
        cfg = {
            "name": name,
            "task_description": task_description,
            "input_pool": input_pool or [""],
            "task_template": task_template or "Task: {task}\n\nInput: {input}\n\nProduce one output.",
            "rubric_axes": rubric_axes or ["specificity", "voice", "hook", "craft"],
            "control_system": control_system,
            "rounds_per_mutation": int(rounds_per_mutation or 3),
            "round_interval_s": int(round_interval_s or 240),
            "created_at": _now(),
        }
        _save_json(_config_path(ws), cfg)
        # Variants
        for v in variants:
            vid = v.get("id") or re.sub(r"[^a-z0-9]+", "_", (v.get("name") or "v").lower())
            entry = {
                "id": vid,
                "name": v.get("name", vid),
                "system": v["system"],
                "mutations": 0,
                "born_at": _now(),
            }
            _save_json(_variant_path(ws, vid), entry)
        # Lineage seed
        _save_json(_lineage_path(ws), {
            "_meta": {"started_at": _now()},
            "generations": [], "mutations": [],
        })
        return json.dumps({
            "status": "ok", "action": "spawn", "name": name,
            "workspace": str(ws),
            "variants": [v["id"] if "id" in v
                         else re.sub(r"[^a-z0-9]+", "_", v["name"].lower())
                         for v in variants],
            "message": (
                f"Bakeoff '{name}' initialized at {ws}.\n"
                f"Call action='round' to run one round on demand, "
                f"or action='pump' to start the background loop."
            ),
        })

    # ── action: round ─────────────────────────────────────────────────────

    def _round(self, name, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required"})
        ws = _workspace(name)
        cfg = _load_json(_config_path(ws), None)
        if not cfg:
            return json.dumps({"status": "error",
                "message": f"bakeoff '{name}' not initialized. Call action='spawn' first."})
        lin = _load_json(_lineage_path(ws), {"generations": [], "mutations": []})
        record = _run_one_round(ws, cfg)
        gen_num = len(lin["generations"]) + 1
        record["gen"] = gen_num
        lin["generations"].append(record)
        # Persist per-round file too
        _save_json(ws / "generations" / f"{gen_num:04d}.json", record)
        # Maybe mutate
        rpm = cfg.get("rounds_per_mutation", 3)
        mutation = None
        if gen_num >= rpm and gen_num % rpm == 0:
            worst, fails = _find_worst_variant(lin["generations"], cfg["rubric_axes"])
            winner = _find_best_variant(lin["generations"], exclude=worst) if worst else None
            if worst:
                mutation = _mutate_variant(ws, worst, winner, fails)
                mutation.update({"gen": gen_num, "variant_id": worst,
                                 "ts": _now()})
                lin["mutations"].append(mutation)
        _save_json(_lineage_path(ws), lin)
        scores = {vid: (r.get("score") or {}).get("total", "ERR")
                  for vid, r in record["results"].items()}
        return json.dumps({
            "status": "ok", "action": "round", "name": name,
            "gen": gen_num,
            "scores": scores,
            "mutation": mutation,
        })

    # ── action: report ────────────────────────────────────────────────────

    def _report(self, name, window=15, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required"})
        ws = _workspace(name)
        lin = _load_json(_lineage_path(ws), None)
        cfg = _load_json(_config_path(ws), None)
        if not lin or not cfg:
            return json.dumps({"status": "error",
                "message": f"bakeoff '{name}' not initialized."})
        gens = lin.get("generations", [])
        if not gens:
            return json.dumps({"status": "ok", "name": name,
                "message": "no generations yet"})
        win = int(window or 15)
        recent = gens[-win:]
        vtotals = defaultdict(list)
        vaxes = defaultdict(lambda: defaultdict(list))
        for g in recent:
            for vid, r in g.get("results", {}).items():
                s = r.get("score") or {}
                t = s.get("total")
                if t is None:
                    continue
                vtotals[vid].append(t)
                for ax in cfg["rubric_axes"]:
                    vaxes[vid][ax].append(s.get(ax, 0))
        rows = sorted(((vid, mean(ts), len(ts))
                       for vid, ts in vtotals.items()),
                      key=lambda r: -r[1])
        all_avgs = [r[1] for r in rows]
        report = {
            "name": name,
            "total_generations": len(gens),
            "window": len(recent),
            "tally": [{"variant": vid, "avg": round(a, 2), "n": n,
                       "axes": {ax: round(mean(vaxes[vid][ax]), 1)
                                for ax in cfg["rubric_axes"]}}
                      for vid, a, n in rows],
            "floor": round(min(all_avgs), 2) if all_avgs else None,
            "ceiling": round(max(all_avgs), 2) if all_avgs else None,
            "gap": round(max(all_avgs) - min(all_avgs), 2) if all_avgs else None,
            "mutations_total": len(lin.get("mutations", [])),
            "recent_mutations": lin.get("mutations", [])[-3:],
        }
        return json.dumps({"status": "ok", "action": "report", **report},
                          indent=2)

    # ── action: status ────────────────────────────────────────────────────

    def _status(self, name, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required"})
        ws = _workspace(name)
        cfg = _load_json(_config_path(ws), None)
        lin = _load_json(_lineage_path(ws), None)
        if not cfg:
            return json.dumps({"status": "error",
                "message": f"bakeoff '{name}' not initialized."})
        pid_file = ws / "pump.pid"
        pump_alive = False
        if pid_file.exists():
            try:
                pid = int(pid_file.read_text().strip())
                os.kill(pid, 0)
                pump_alive = True
            except (ProcessLookupError, ValueError, PermissionError):
                pump_alive = False
        return json.dumps({
            "status": "ok", "action": "status",
            "name": name,
            "workspace": str(ws),
            "rounds": len((lin or {}).get("generations", [])),
            "mutations": len((lin or {}).get("mutations", [])),
            "pump_alive": pump_alive,
            "variants": list(_load_variants(ws).keys()),
            "config_summary": {
                "task": cfg.get("task_description", "")[:100],
                "rubric": cfg.get("rubric_axes"),
                "input_pool_size": len(cfg.get("input_pool", [])),
                "round_interval_s": cfg.get("round_interval_s"),
            },
        }, indent=2)

    # ── action: list ──────────────────────────────────────────────────────

    def _list(self, **_):
        ROOT.mkdir(parents=True, exist_ok=True)
        out = []
        for d in sorted(ROOT.iterdir()) if ROOT.exists() else []:
            if not d.is_dir():
                continue
            cfg = _load_json(_config_path(d), None)
            lin = _load_json(_lineage_path(d), None)
            if not cfg:
                continue
            out.append({
                "name": d.name,
                "rounds": len((lin or {}).get("generations", [])),
                "mutations": len((lin or {}).get("mutations", [])),
                "task": cfg.get("task_description", "")[:80],
                "workspace": str(d),
            })
        return json.dumps({"status": "ok", "action": "list",
                           "bakeoffs": out, "count": len(out)}, indent=2)

    # ── action: stop ──────────────────────────────────────────────────────

    def _stop(self, name, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required"})
        ws = _workspace(name)
        pid_file = ws / "pump.pid"
        if not pid_file.exists():
            return json.dumps({"status": "ok", "action": "stop",
                "message": f"no pump running for '{name}'."})
        try:
            pid = int(pid_file.read_text().strip())
            os.kill(pid, 15)
            pid_file.unlink(missing_ok=True)
            return json.dumps({"status": "ok", "action": "stop",
                               "pid": pid, "name": name})
        except (ProcessLookupError, ValueError) as e:
            pid_file.unlink(missing_ok=True)
            return json.dumps({"status": "ok", "action": "stop",
                "message": f"pid already gone: {e}"})

    # ── action: pump (start background loop) ──────────────────────────────

    def _pump(self, name, max_rounds=None, **_):
        if not name:
            return json.dumps({"status": "error", "message": "name required"})
        ws = _workspace(name)
        cfg = _load_json(_config_path(ws), None)
        if not cfg:
            return json.dumps({"status": "error",
                "message": f"bakeoff '{name}' not initialized."})
        pid_file = ws / "pump.pid"
        if pid_file.exists():
            try:
                existing = int(pid_file.read_text().strip())
                os.kill(existing, 0)
                return json.dumps({"status": "ok", "action": "pump",
                    "message": f"pump already running for '{name}' (pid {existing}).",
                    "pid": existing})
            except (ProcessLookupError, ValueError, PermissionError):
                pid_file.unlink(missing_ok=True)
        # Spawn a child python that loops calling _round
        runner_code = (
            "import time, sys, json, urllib.request\n"
            f"from pathlib import Path\n"
            f"sys.path.insert(0, '{os.path.dirname(os.path.abspath(__file__))}')\n"
            "import bakeoff_factory_agent as bf\n"
            f"name = {json.dumps(name)}\n"
            f"max_rounds = {repr(max_rounds)}\n"
            "agent = bf.BakeoffFactoryAgent()\n"
            "ws = bf._workspace(name)\n"
            "cfg = bf._load_json(bf._config_path(ws), {})\n"
            "(ws/'pump.pid').write_text(str(__import__('os').getpid()))\n"
            "(ws/'logs').mkdir(exist_ok=True)\n"
            "rounds = 0\n"
            "log = open(ws/'logs'/'pump.log', 'a')\n"
            "while True:\n"
            "    try:\n"
            "        r = agent._round(name=name)\n"
            "        log.write(f'[{__import__(\"datetime\").datetime.utcnow().isoformat()}Z] {r}\\n')\n"
            "        log.flush()\n"
            "    except Exception as e:\n"
            "        log.write(f'ERR {e}\\n')\n"
            "        log.flush()\n"
            "    rounds += 1\n"
            "    if max_rounds is not None and rounds >= max_rounds:\n"
            "        break\n"
            "    time.sleep(cfg.get('round_interval_s', 240))\n"
            "log.close()\n"
            "(ws/'pump.pid').unlink(missing_ok=True)\n"
        )
        runner_path = ws / "_pump_runner.py"
        runner_path.write_text(runner_code)
        proc = subprocess.Popen(
            [sys.executable, str(runner_path)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
        return json.dumps({
            "status": "ok", "action": "pump", "name": name,
            "pid": proc.pid,
            "interval_s": cfg.get("round_interval_s", 240),
            "max_rounds": max_rounds,
            "message": (
                f"Pump started for '{name}' (pid {proc.pid}). "
                f"Tail logs at {ws/'logs'/'pump.log'}. "
                f"Stop with action='stop'."
            ),
        })

    # ── dispatch ──────────────────────────────────────────────────────────

    def perform(self, action="list", **kwargs):
        try:
            if action == "spawn":
                return self._spawn(**kwargs)
            if action == "round":
                return self._round(**kwargs)
            if action == "report":
                return self._report(**kwargs)
            if action == "status":
                return self._status(**kwargs)
            if action == "list":
                return self._list(**kwargs)
            if action == "stop":
                return self._stop(**kwargs)
            if action == "pump":
                return self._pump(**kwargs)
            return json.dumps({"status": "error",
                "message": f"unknown action '{action}'."})
        except Exception as e:
            return json.dumps({"status": "error", "exception": str(e)})


# Discovery alias — brainstem's *Agent loader picks this up.
class BakeoffFactory(BakeoffFactoryAgent):
    pass
