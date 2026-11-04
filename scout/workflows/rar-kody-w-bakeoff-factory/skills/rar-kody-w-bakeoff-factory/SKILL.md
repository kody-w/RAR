---
name: "rar-kody-w-bakeoff-factory"
description: "Run a generic content-improvement bakeoff. Variants compete on a task; a judge scores every output on a rubric; the worst variant evolves by grafting techniques from the best.\n\nActions:\n - spawn:  initialize a bakeoff with task + variants + rubric\n - round:  run one round on demand (returns scores)\n - report: render a meta-review of the last N rounds\n - status: snapshot of one bakeoff (rounds, mutations, gap)\n - stop:   halt the background pump for a bakeoff\n - list:   every bakeoff on this machine\n - pump:   start a background pump loop (forever)\n\nStorage lives under ~/.rapp/bakeoffs/<name>/. LLM dispatch tries the local brainstem first (so model choice is yours) and falls back to Azure/OpenAI."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/bakeoff_factory", "rar_sha256": "61263e01de638d1c43e7ef6af8352ba219cf101d7b109118c36aaca34b2f502b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "0.1.1", "author": "kody-w", "tags": ["meta", "evolution", "tournament", "loop", "self-improving", "composite", "rapplication"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bakeoff_factory_agent.py` and embedded as the fenced Python below (sha256 61263e01de638d1c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bakeoff_factory_agent.py` first:

```bash
python3 bakeoff_factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bakeoff_factory_agent.py   # or on stdin
python3 bakeoff_factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/bakeoff_factory_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/bakeoff_factory_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/bakeoff_factory/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
