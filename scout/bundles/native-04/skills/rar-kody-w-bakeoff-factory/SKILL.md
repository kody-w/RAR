---
name: "rar-kody-w-bakeoff-factory"
description: "Run a generic content-improvement bakeoff. Variants compete on a task; a judge scores every output on a rubric; the worst variant evolves by grafting techniques from the best.\n\nActions:\n - spawn:  initialize a bakeoff with task + variants + rubric\n - round:  run one round on demand (returns scores)\n - report: render a meta-review of the last N rounds\n - status: snapshot of one bakeoff (rounds, mutations, gap)\n - stop:   halt the background pump for a bakeoff\n - list:   every bakeoff on this machine\n - pump:   start a background pump loop (forever)\n\nStorage lives under ~/.rapp/bakeoffs/<name>/. LLM dispatch tries the local brainstem first (so model choice is yours) and falls back to Azure/OpenAI."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/bakeoff_factory", "rar_sha256": "61263e01de638d1c43e7ef6af8352ba219cf101d7b109118c36aaca34b2f502b", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "0.1.1", "author": "kody-w", "tags": ["meta", "evolution", "tournament", "loop", "self-improving", "composite", "rapplication"]}
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
