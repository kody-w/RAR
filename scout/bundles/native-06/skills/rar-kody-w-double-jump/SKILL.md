---
name: "rar-kody-w-double-jump"
description: "A general improvement engine: make two loops compete on the SAME task and ratchet it upward, round over round. Jump 1 is the CALLER's loop (the main agent's current draft/attempt); Jump 2 is the BRAINSTEM \u2014 this agent POSTs the task to /chat, opus produces a competing attempt, and it reports back. Each round it judges the two, keeps the winner, and feeds what made the winner better into the next attempt \u2014 pulling the trailing loop up toward the leader (dynamic learning) without losing ground already won. Use to IMPROVE anything: sharpen an agent.py, refine a rapp-commons feature, strengthen a plan/strategy/draft, or solve a hard task better than one pass. ACTION 'improve' takes a 'task' (what to do/improve) and optionally a 'draft' (Jump 1, the caller's current best) and 'rounds'; it returns the ratcheted-up result + the round trace (which jump led, what improved). ACTION 'compete' runs two brainstem jumps against each other when there is no caller draft. ACTION 'demo' self-tests the convergence with no network. It round-trips http://localhost:7071/chat (override with env BRAINSTEM_CHAT); if a jump times out it degrades gracefully and keeps the best so far."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/double_jump_agent", "rar_sha256": "a85073b79ec0d416a94d596ac455aa393ed33049aa615b267a5f7ff20a004ab3", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["improvement", "competition", "brainstem", "double-jump", "self-improvement"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `double_jump_agent.py` and embedded as the fenced Python below (sha256 a85073b79ec0d416…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `double_jump_agent.py` first:

```bash
python3 double_jump_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 double_jump_agent.py   # or on stdin
python3 double_jump_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
