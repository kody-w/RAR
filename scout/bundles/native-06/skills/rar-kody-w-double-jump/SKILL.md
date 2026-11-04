---
name: "rar-kody-w-double-jump"
description: "A general improvement engine: make two loops compete on the SAME task and ratchet it upward, round over round. Jump 1 is the CALLER's loop (the main agent's current draft/attempt); Jump 2 is the BRAINSTEM \u2014 this agent POSTs the task to /chat, opus produces a competing attempt, and it reports back. Each round it judges the two, keeps the winner, and feeds what made the winner better into the next attempt \u2014 pulling the trailing loop up toward the leader (dynamic learning) without losing ground already won. Use to IMPROVE anything: sharpen an agent.py, refine a rapp-commons feature, strengthen a plan/strategy/draft, or solve a hard task better than one pass. ACTION 'improve' takes a 'task' (what to do/improve) and optionally a 'draft' (Jump 1, the caller's current best) and 'rounds'; it returns the ratcheted-up result + the round trace (which jump led, what improved). ACTION 'compete' runs two brainstem jumps against each other when there is no caller draft. ACTION 'demo' self-tests the convergence with no network. It round-trips http://localhost:7071/chat (override with env BRAINSTEM_CHAT); if a jump times out it degrades gracefully and keeps the best so far."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/double_jump_agent", "rar_sha256": "eb3e678ca3ca0a1ddb347dbf65218b716a6a78044d03d02f74b9a31a8336948b", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["improvement", "competition", "brainstem", "double-jump", "self-improvement"]}
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
