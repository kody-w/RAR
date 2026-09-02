---
name: "rar-kody-w-bakeoff-factory"
description: "Run a generic content-improvement bakeoff. Variants compete on a task; a judge scores every output on a rubric; the worst variant evolves by grafting techniques from the best.\n\nActions:\n - spawn:  initialize a bakeoff with task + variants + rubric\n - round:  run one round on demand (returns scores)\n - report: render a meta-review of the last N rounds\n - status: snapshot of one bakeoff (rounds, mutations, gap)\n - stop:   halt the background pump for a bakeoff\n - list:   every bakeoff on this machine\n - pump:   start a background pump loop (forever)\n\nStorage lives under ~/.rapp/bakeoffs/<name>/. LLM dispatch tries the local brainstem first (so model choice is yours) and falls back to Azure/OpenAI."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/bakeoff_factory", "rar_sha256": "461620d239ee7c63430f5a5cd4412429d72a049977d5ff2beb04d0ba5e38b786", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bakeoff_factory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/bakeoff-factory:7b22406672acd622052f2dd226ad0e337f41076a2b5d849c9ad406d019eaed67", "kind": "skill"}, "version": "0.1.1", "author": "kody-w", "tags": ["meta", "evolution", "tournament", "loop", "self-improving", "composite", "rapplication"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/bakeoff_factory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bakeoff_factory_agent.py` is
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
