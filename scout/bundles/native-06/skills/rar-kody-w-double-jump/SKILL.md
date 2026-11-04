---
name: "rar-kody-w-double-jump"
description: "A general improvement engine: make two loops compete on the SAME task and ratchet it upward, round over round. Jump 1 is the CALLER's loop (the main agent's current draft/attempt); Jump 2 is the BRAINSTEM \u2014 this agent POSTs the task to /chat, opus produces a competing attempt, and it reports back. Each round it judges the two, keeps the winner, and feeds what made the winner better into the next attempt \u2014 pulling the trailing loop up toward the leader (dynamic learning) without losing ground already won. Use to IMPROVE anything: sharpen an agent.py, refine a rapp-commons feature, strengthen a plan/strategy/draft, or solve a hard task better than one pass. ACTION 'improve' takes a 'task' (what to do/improve) and optionally a 'draft' (Jump 1, the caller's current best) and 'rounds'; it returns the ratcheted-up result + the round trace (which jump led, what improved). ACTION 'compete' runs two brainstem jumps against each other when there is no caller draft. ACTION 'demo' self-tests the convergence with no network. It round-trips http://localhost:7071/chat (override with env BRAINSTEM_CHAT); if a jump times out it degrades gracefully and keeps the best so far."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/double_jump_agent", "rar_sha256": "eb3e678ca3ca0a1ddb347dbf65218b716a6a78044d03d02f74b9a31a8336948b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["improvement", "competition", "brainstem", "double-jump", "self-improvement"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/double_jump_agent`. The original RAPP
agent is preserved byte-for-byte in `double_jump_agent.py` and in the RCI capsule.

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

DoubleJump — a general improvement engine that makes two loops compete on the SAME task and ratchet
it upward. The two competitors aren't anonymous strategies — they're two loops running the same
work:

  • Jump 1 — the caller's loop (the main agent loop / whoever invokes this): its current best draft.
  • Jump 2 — the brainstem: this agent POSTs the task to /chat, opus reads it, produces a competing
    attempt, and reports back.

Each round it judges the two, keeps the winner, and feeds *what made the winner better* forward so
the next attempt builds on it — pulling the laggard up toward the leader (dynamic learning) without
ever losing ground already won (dream-catcher: keep what's good, only add non-contradicting gains).
Point it at ANYTHING in the universe — an agent.py to sharpen, a rapp-commons feature, a plan, a
draft, a strategy — and it double-jumps it better, round over round.

Live mode round-trips the brainstem at http://localhost:7071/chat (the same /chat the user drives).
A deterministic 'demo' proves the two-jump convergence with no network. Drop-in (BasicAgent), no PII.

Actions:
  improve  given a task (+ optional draft = Jump 1, rounds), compete the caller's loop vs the
           brainstem and return the ratcheted-up best + the round-by-round trace
  compete  no draft: run two brainstem jumps (different framings) against each other + cross-improve
  demo     self-test: prove the trailing jump climbs toward the leader and the result improves

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "improve = caller-draft (Jump 1) vs brainstem (Jump 2), ratchet up; compete = two brainstem jumps cross-improve; demo = deterministic self-test. Default demo.",
      "enum": [
        "improve",
        "compete",
        "demo"
      ],
      "type": "string"
    },
    "criteria": {
      "description": "Optional explicit judging criteria (what 'better' means). If omitted the judge infers it from the task.",
      "type": "string"
    },
    "draft": {
      "description": "For improve: the caller's CURRENT best attempt (Jump 1). The brainstem (Jump 2) tries to beat it; the winner is kept and fed forward.",
      "type": "string"
    },
    "rounds": {
      "description": "How many compete-and-improve rounds. Default 2 (each round is one or two /chat round-trips).",
      "type": "integer"
    },
    "task": {
      "description": "What to do / improve \u2014 the goal both jumps work on (e.g., 'improve this agent.py to ...', 'make this commons feature better', 'strengthen this plan'). Include the material to improve.",
      "type": "string"
    },
    "timeout": {
      "description": "Per /chat round-trip timeout in seconds. Default 70.",
      "type": "integer"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `double_jump_agent.py` and embedded as the fenced Python below (sha256 eb3e678ca3ca0a1d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `double_jump_agent.py` first:

```bash
python3 double_jump_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 double_jump_agent.py   # or on stdin
python3 double_jump_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/double_jump_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/double_jump_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/double_jump_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
DoubleJump — a general improvement engine that makes two loops compete on the SAME task and ratchet
it upward. The two competitors aren't anonymous strategies — they're two loops running the same
work:

  • Jump 1 — the caller's loop (the main agent loop / whoever invokes this): its current best draft.
  • Jump 2 — the brainstem: this agent POSTs the task to /chat, opus reads it, produces a competing
    attempt, and reports back.

Each round it judges the two, keeps the winner, and feeds *what made the winner better* forward so
the next attempt builds on it — pulling the laggard up toward the leader (dynamic learning) without
ever losing ground already won (dream-catcher: keep what's good, only add non-contradicting gains).
Point it at ANYTHING in the universe — an agent.py to sharpen, a rapp-commons feature, a plan, a
draft, a strategy — and it double-jumps it better, round over round.

Live mode round-trips the brainstem at http://localhost:7071/chat (the same /chat the user drives).
A deterministic 'demo' proves the two-jump convergence with no network. Drop-in (BasicAgent), no PII.

Actions:
  improve  given a task (+ optional draft = Jump 1, rounds), compete the caller's loop vs the
           brainstem and return the ratcheted-up best + the round-by-round trace
  compete  no draft: run two brainstem jumps (different framings) against each other + cross-improve
  demo     self-test: prove the trailing jump climbs toward the leader and the result improves
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/double_jump_agent",
    "version": "1.0.1",
    "display_name": "Double Jump",
    "author": "kody-w",
    "category": "workflow",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ],
    "description": "Improves any draft by competing it against the local brainstem's /chat output round over round, keeping each round's winner; defaults to offline demo.",
    "tags": [
        "improvement",
        "competition",
        "brainstem",
        "double-jump",
        "self-improvement"
    ]
}

import os, json, urllib.request

try:
    from agents.basic_agent import BasicAgent  # RAR layout
except Exception:
    try:
        from basic_agent import BasicAgent
    except Exception:
        try:
            from openrappter.agents.basic_agent import BasicAgent
        except Exception:
            class BasicAgent:
                def __init__(self, name=None, metadata=None):
                    if name is not None: self.name = name
                    if metadata is not None: self.metadata = metadata
                def perform(self, **k): return "Not implemented."

CHAT = os.environ.get("BRAINSTEM_CHAT", "http://localhost:7071/chat")


class DoubleJumpAgent(BasicAgent):
    def __init__(self):
        self.name = "DoubleJump"
        self.metadata = {
            "name": self.name,
            "description": (
                "A general improvement engine: make two loops compete on the SAME task and ratchet it upward, round "
                "over round. Jump 1 is the CALLER's loop (the main agent's current draft/attempt); Jump 2 is the "
                "BRAINSTEM — this agent POSTs the task to /chat, opus produces a competing attempt, and it reports back. "
                "Each round it judges the two, keeps the winner, and feeds what made the winner better into the next "
                "attempt — pulling the trailing loop up toward the leader (dynamic learning) without losing ground "
                "already won. Use to IMPROVE anything: sharpen an agent.py, refine a rapp-commons feature, strengthen a "
                "plan/strategy/draft, or solve a hard task better than one pass. ACTION 'improve' takes a 'task' (what to "
                "do/improve) and optionally a 'draft' (Jump 1, the caller's current best) and 'rounds'; it returns the "
                "ratcheted-up result + the round trace (which jump led, what improved). ACTION 'compete' runs two "
                "brainstem jumps against each other when there is no caller draft. ACTION 'demo' self-tests the "
                "convergence with no network. It round-trips http://localhost:7071/chat (override with env "
                "BRAINSTEM_CHAT); if a jump times out it degrades gracefully and keeps the best so far."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["improve", "compete", "demo"],
                               "description": "improve = caller-draft (Jump 1) vs brainstem (Jump 2), ratchet up; compete = two brainstem jumps cross-improve; demo = deterministic self-test. Default demo."},
                    "task": {"type": "string", "description": "What to do / improve — the goal both jumps work on (e.g., 'improve this agent.py to ...', 'make this commons feature better', 'strengthen this plan'). Include the material to improve."},
                    "draft": {"type": "string", "description": "For improve: the caller's CURRENT best attempt (Jump 1). The brainstem (Jump 2) tries to beat it; the winner is kept and fed forward."},
                    "rounds": {"type": "integer", "description": "How many compete-and-improve rounds. Default 2 (each round is one or two /chat round-trips)."},
                    "criteria": {"type": "string", "description": "Optional explicit judging criteria (what 'better' means). If omitted the judge infers it from the task."},
                    "timeout": {"type": "integer", "description": "Per /chat round-trip timeout in seconds. Default 70."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # ---- one brainstem round-trip (Jump 2 / the judge live) ----
    def _chat(self, prompt, timeout):
        try:
            req = urllib.request.Request(CHAT, method="POST",
                                         data=json.dumps({"user_input": prompt}).encode(),
                                         headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = json.loads(r.read().decode())
            return (body.get("response") or body.get("assistant_response") or "").strip() or None
        except Exception:
            return None

    def _attempt(self, task, current, criteria, timeout):
        # ask the brainstem to BEAT the current best (build on it; don't lose what's good).
        p = ("You are Jump 2 in a double-jump improvement loop. TASK:\n" + task + "\n\n" +
             (("CURRENT BEST (Jump 1) to beat — keep everything good about it, only improve:\n" + current + "\n\n") if current else "") +
             (("Judge by: " + criteria + "\n\n") if criteria else "") +
             "Produce your best improved version. Output ONLY the improved result, no preamble.")
        return self._chat(p, timeout)

    def _judge(self, task, a, b, criteria, timeout):
        p = ("Judge two attempts at a task. TASK:\n" + task + "\n\n" +
             (("Criteria: " + criteria + "\n\n") if criteria else "") +
             "ATTEMPT A:\n" + (a or "(none)") + "\n\nATTEMPT B:\n" + (b or "(none)") + "\n\n" +
             "Reply as STRICT JSON only: {\"winner\":\"A\"|\"B\",\"why\":\"one sentence on what made the winner better\"}.")
        r = self._chat(p, timeout)
        if not r:
            return None
        try:
            i, j = r.find("{"), r.rfind("}")
            return json.loads(r[i:j + 1])
        except Exception:
            return {"winner": "B" if (b and (not a or len(b) >= len(a))) else "A", "why": "fallback heuristic"}

    def _improve(self, task, draft, rounds, criteria, timeout, two_jumps):
        trace, best = [], (draft or None)
        # if no caller draft, the first brainstem jump seeds Jump 1.
        if best is None:
            best = self._attempt(task, None, criteria, timeout) or ""
            trace.append({"round": 0, "event": "seed", "leader": "brainstem(seed)", "len": len(best)})
        for rnd in range(max(1, rounds)):
            challenger = self._attempt(task, best, criteria, timeout)
            if not challenger:
                trace.append({"round": rnd + 1, "event": "jump2_timeout", "kept": "current best"})
                continue
            verdict = self._judge(task, best, challenger, criteria, timeout)
            winner = (verdict or {}).get("winner", "B")
            why = (verdict or {}).get("why", "")
            if winner == "B":
                best = challenger
                trace.append({"round": rnd + 1, "leader": "Jump2(brainstem)", "improved": True, "why": why})
            else:
                trace.append({"round": rnd + 1, "leader": "Jump1(caller)", "improved": False, "why": why})
        return best, trace

    # ---- deterministic demo (no network) ----
    def _demo(self):
        # toy task: two jumps refine a numeric "quality"; the trailing jump adopts the leader's gain.
        import math
        def score(v): return round(100 * (1 - math.exp(-3 * v)), 2)   # quality of an attempt in [0,1] -> 0..100
        jump1, jump2 = 0.20, 0.35
        rounds = []
        for r in range(5):
            s1, s2 = score(jump1), score(jump2)
            lead, lag = (("Jump2", "Jump1") if s2 >= s1 else ("Jump1", "Jump2"))
            # the laggard adopts the leader's level + a learned increment (what made the leader better).
            top = max(jump1, jump2); gain = (top - min(jump1, jump2)) * 0.6 + 0.05
            if jump1 <= jump2: jump1 = min(1.0, jump1 + gain)
            else: jump2 = min(1.0, jump2 + gain)
            rounds.append({"round": r, "leader": lead, "j1": score(jump1), "j2": score(jump2)})
        first = min(rounds[0]["j1"], rounds[0]["j2"])
        last = min(rounds[-1]["j1"], rounds[-1]["j2"])
        return {"rounds": rounds, "trailing_first": first, "trailing_last": last,
                "best_first": max(rounds[0]["j1"], rounds[0]["j2"]),
                "best_last": max(rounds[-1]["j1"], rounds[-1]["j2"]),
                "improved": last > first}

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "demo").strip().lower()
        timeout = int(kwargs.get("timeout") or 70)
        criteria = (kwargs.get("criteria") or "").strip() or None

        if action == "demo":
            d = self._demo()
            ok = d["improved"] and d["best_last"] >= d["best_first"]
            return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": "demo",
                               "status": "success" if ok else "degraded", "self_test_pass": ok,
                               "trailing_jump": {"first": d["trailing_first"], "last": d["trailing_last"]},
                               "best": {"first": d["best_first"], "last": d["best_last"]}, "rounds": d["rounds"],
                               "persona_directive": ("Show the double jump: each round the trailing loop adopted what "
                                "made the leading loop better, so both climbed and the result ratcheted up. Report the "
                                "trailing jump's first vs last score and that the best improved.")}, indent=2)

        task = (kwargs.get("task") or "").strip()
        if not task:
            return json.dumps({"status": "error", "error": "provide a 'task' (what to do/improve) for the two jumps to compete on."})
        draft = (kwargs.get("draft") or "").strip() or None
        rounds = int(kwargs.get("rounds") or 2)
        if action == "compete":
            draft = None   # no caller draft — both jumps are the brainstem
        best, trace = self._improve(task, draft, rounds, criteria, timeout, two_jumps=(action == "compete"))
        improved = any(t.get("improved") for t in trace)
        return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": action,
                           "status": "success" if best else "degraded",
                           "result": best, "improved_over_draft": bool(draft and improved),
                           "rounds_run": rounds, "trace": trace,
                           "persona_directive": ("Present the ratcheted-up result and narrate the double jump: Jump 1 "
                            "(the caller's draft) vs Jump 2 (the brainstem), judged each round, the winner kept and its "
                            "improvement fed forward — so the work climbed without losing what was already good. Note "
                            "which jump led and what made it better. If a jump timed out, say the best-so-far was kept.")}, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
