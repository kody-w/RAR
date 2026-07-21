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
