---
name: "rar-kody-w-bakeoff-factory"
description: "Run a generic content-improvement bakeoff. Variants compete on a task; a judge scores every output on a rubric; the worst variant evolves by grafting techniques from the best.\n\nActions:\n - spawn:  initialize a bakeoff with task + variants + rubric\n - round:  run one round on demand (returns scores)\n - report: render a meta-review of the last N rounds\n - status: snapshot of one bakeoff (rounds, mutations, gap)\n - stop:   halt the background pump for a bakeoff\n - list:   every bakeoff on this machine\n - pump:   start a background pump loop (forever)\n\nStorage lives under ~/.rapp/bakeoffs/<name>/. LLM dispatch tries the local brainstem first (so model choice is yours) and falls back to Azure/OpenAI."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/bakeoff_factory", "rar_sha256": "461620d239ee7c63430f5a5cd4412429d72a049977d5ff2beb04d0ba5e38b786", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "0.1.1", "author": "kody-w", "tags": ["meta", "evolution", "tournament", "loop", "self-improving", "composite", "rapplication"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/bakeoff_factory`. The original RAPP
agent is preserved byte-for-byte in `bakeoff_factory_agent.py` and in the RCI capsule.

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

bakeoff_factory_agent.py — generic content-improvement bakeoff loop,
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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "spawn",
        "round",
        "report",
        "status",
        "stop",
        "list",
        "pump"
      ],
      "type": "string"
    },
    "control_system": {
      "description": "System prompt for the bare baseline control.",
      "type": "string"
    },
    "input_pool": {
      "description": "Inputs randomly sampled each round.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "max_rounds": {
      "description": "Stop after this many rounds (pump action). Default: forever.",
      "type": "integer"
    },
    "name": {
      "description": "Bakeoff name (slug). Required for all but list.",
      "type": "string"
    },
    "round_interval_s": {
      "description": "Pump cadence in seconds. Default 240.",
      "type": "integer"
    },
    "rounds_per_mutation": {
      "description": "Mutate worst variant every N rounds. Default 3.",
      "type": "integer"
    },
    "rubric_axes": {
      "description": "Axes the judge scores. Default: ['specificity','voice','hook','craft'].",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "task_description": {
      "description": "What every variant produces. Required for spawn.",
      "type": "string"
    },
    "task_template": {
      "description": "Jinja-like {task}/{input} template. Optional.",
      "type": "string"
    },
    "variants": {
      "description": "List of {id,name,system} for each competing strategy. Required for spawn.",
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "window": {
      "description": "Report window. Default 15.",
      "type": "integer"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bakeoff_factory_agent.py` and embedded as the fenced Python below (sha256 461620d239ee7c63…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bakeoff_factory_agent.py` first:

```bash
python3 bakeoff_factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bakeoff_factory_agent.py   # or on stdin
python3 bakeoff_factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
    "version": "0.1.1",
    "display_name": "BakeoffFactory",
    "description": (
        "Runs a persistent tournament where prompt variants compete on a text task, an LLM judge scores outputs, and the worst variant mutates toward the best."
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
            "import os, time, sys, json, datetime, urllib.request\n"
            f"from pathlib import Path\n"
            f"sys.path.insert(0, '{os.path.dirname(os.path.abspath(__file__))}')\n"
            "import bakeoff_factory_agent as bf\n"
            f"name = {json.dumps(name)}\n"
            f"max_rounds = {repr(max_rounds)}\n"
            "agent = bf.BakeoffFactoryAgent()\n"
            "ws = bf._workspace(name)\n"
            "cfg = bf._load_json(bf._config_path(ws), {})\n"
            "(ws/'pump.pid').write_text(str(os.getpid()))\n"
            "(ws/'logs').mkdir(exist_ok=True)\n"
            "rounds = 0\n"
            "log = open(ws/'logs'/'pump.log', 'a')\n"
            "while True:\n"
            "    try:\n"
            "        r = agent._round(name=name)\n"
            "        log.write(f'[{datetime.datetime.utcnow().isoformat()}Z] {r}\\n')\n"
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
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
