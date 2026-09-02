---
name: "rar-kody-w-double-jump"
description: "A general improvement engine: make two loops compete on the SAME task and ratchet it upward, round over round. Jump 1 is the CALLER's loop (the main agent's current draft/attempt); Jump 2 is the BRAINSTEM \u2014 this agent POSTs the task to /chat, opus produces a competing attempt, and it reports back. Each round it judges the two, keeps the winner, and feeds what made the winner better into the next attempt \u2014 pulling the trailing loop up toward the leader (dynamic learning) without losing ground already won. Use to IMPROVE anything: sharpen an agent.py, refine a rapp-commons feature, strengthen a plan/strategy/draft, or solve a hard task better than one pass. ACTION 'improve' takes a 'task' (what to do/improve) and optionally a 'draft' (Jump 1, the caller's current best) and 'rounds'; it returns the ratcheted-up result + the round trace (which jump led, what improved). ACTION 'compete' runs two brainstem jumps against each other when there is no caller draft. ACTION 'demo' self-tests the convergence with no network. It round-trips http://localhost:7071/chat (override with env BRAINSTEM_CHAT); if a jump times out it degrades gracefully and keeps the best so far."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/double_jump_agent", "rar_sha256": "a85073b79ec0d416a94d596ac455aa393ed33049aa615b267a5f7ff20a004ab3", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "double_jump_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/double-jump:8cf4215de61021cf43331e7566fa6260168d7fbecb428c4b3a58fd070b444719", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["improvement", "competition", "brainstem", "double-jump", "self-improvement"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/double_jump_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `double_jump_agent.py` is
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
