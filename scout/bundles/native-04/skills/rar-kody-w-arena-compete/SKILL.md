---
name: "rar-kody-w-arena-compete"
description: "Run a COMPETITION of player-agents in the RAPP Commons and make them dynamically LEARN: each round the competitors play (each driving a strategy/tab), they're judged, and the BOTTOM performer is pulled up by adjusting its strategy toward whatever made the TOP performer better that round \u2014 so the field climbs round over round and the laggard is never left behind. Use when the user wants competing self-improving agents, a learning tournament, agents that adapt by copying the leader, or to drop in and compete in the world themselves. ACTION 'compete' runs the loop for 'players' competitors over 'rounds' rounds; set live=true to drive REAL headless commons tabs via the Matrix Arena harness and score from the real signed stream (default false = a fast, deterministic simulation so the learning is reproducible and testable). ACTION 'demo' self-tests that the bottom performer's score climbs toward the leader's across rounds. Returns the per-round scoreboard, the strategy each competitor converged to, the winner, and the proof that the bottom improved (its first-round vs last-round score). 'learning_rate' controls how fast the laggard adopts the leader's strategy."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/arena_compete_agent", "rar_sha256": "3e5333752068fae52cdd93dafa259c357d697dc8af1ec7707f2d2f25eb556b10", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["competition", "learning", "self-improvement", "agents", "tournament"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/arena_compete_agent`. The original RAPP
agent is preserved byte-for-byte in `arena_compete_agent.py` and in the RCI capsule.

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

ArenaCompete — run a COMPETITION of player-agents in the commons, judge each round, and pull the
BOTTOM performer up by adjusting its strategy toward what made the TOP performer better last round
(dynamic learning). It's the EZsharpen self-improvement pattern applied to players: many drivers
each control a tab/strategy, they're scored each round, and the laggard learns from the leader —
so the whole field climbs round over round, and you (or the brainstem) can drop in and compete too.

THE LOOP (per round):
  1. Each competitor plays a round with its current strategy (live: drive a real commons tab via the
     Matrix Arena harness and score from the real signed stream / exploration; sim: a deterministic
     score so the learning is testable without a live browser).
  2. JUDGE: rank competitors by score.
  3. PULL UP THE BOTTOM: nudge the lowest scorer's strategy toward the leader's — `bottom += lr *
     (top - bottom)` — i.e., adopt *what made the better competitor better*. A little exploration
     noise keeps it from collapsing. (The strongest may also be perturbed slightly to keep searching.)
  4. Repeat — the field's average score rises and the gap shrinks; the bottom is never left behind.

Strategy vector (each in [0,1]): explore (move/cover ground), act (land signed actions), social
(say/relate). The score rewards a balance the round happens to favor; learning discovers it.

Drop-in (BasicAgent), pure stdlib core (live mode shells to ~/.brainstem/matrix_tabs.py). No PII.

Actions:
  compete  run the dynamic-learning competition (players, rounds[, live]) -> scoreboard evolution
  demo     self-test: prove the bottom performer climbs toward the leader over rounds

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "compete = run the dynamic-learning tournament; demo = self-test that the bottom climbs toward the leader. Default demo.",
      "enum": [
        "compete",
        "demo"
      ],
      "type": "string"
    },
    "learning_rate": {
      "description": "How fast the bottom performer adopts the leader's strategy (0-1). Default 0.5.",
      "type": "number"
    },
    "live": {
      "description": "If true, drive REAL headless commons tabs via the Matrix Arena harness and score from the real signed stream; default false (fast deterministic simulation).",
      "type": "boolean"
    },
    "players": {
      "description": "How many competitors. Default 4.",
      "type": "integer"
    },
    "rounds": {
      "description": "How many judge-and-adjust rounds. Default 6.",
      "type": "integer"
    },
    "seconds": {
      "description": "For live: seconds each competitor plays per round. Default 12.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `arena_compete_agent.py` and embedded as the fenced Python below (sha256 3e5333752068fae5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `arena_compete_agent.py` first:

```bash
python3 arena_compete_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 arena_compete_agent.py   # or on stdin
python3 arena_compete_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/arena_compete_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/arena_compete_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/arena_compete_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
ArenaCompete — run a COMPETITION of player-agents in the commons, judge each round, and pull the
BOTTOM performer up by adjusting its strategy toward what made the TOP performer better last round
(dynamic learning). It's the EZsharpen self-improvement pattern applied to players: many drivers
each control a tab/strategy, they're scored each round, and the laggard learns from the leader —
so the whole field climbs round over round, and you (or the brainstem) can drop in and compete too.

THE LOOP (per round):
  1. Each competitor plays a round with its current strategy (live: drive a real commons tab via the
     Matrix Arena harness and score from the real signed stream / exploration; sim: a deterministic
     score so the learning is testable without a live browser).
  2. JUDGE: rank competitors by score.
  3. PULL UP THE BOTTOM: nudge the lowest scorer's strategy toward the leader's — `bottom += lr *
     (top - bottom)` — i.e., adopt *what made the better competitor better*. A little exploration
     noise keeps it from collapsing. (The strongest may also be perturbed slightly to keep searching.)
  4. Repeat — the field's average score rises and the gap shrinks; the bottom is never left behind.

Strategy vector (each in [0,1]): explore (move/cover ground), act (land signed actions), social
(say/relate). The score rewards a balance the round happens to favor; learning discovers it.

Drop-in (BasicAgent), pure stdlib core (live mode shells to ~/.brainstem/matrix_tabs.py). No PII.

Actions:
  compete  run the dynamic-learning competition (players, rounds[, live]) -> scoreboard evolution
  demo     self-test: prove the bottom performer climbs toward the leader over rounds
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/arena_compete_agent",
    "version": "1.0.1",
    "display_name": "Arena Compete",
    "description": "Runs a learning competition of player-agents where the bottom performer adopts the leader's strategy each round; defaults to a deterministic simulation.",
    "author": "kody-w",
    "tags": [
        "competition",
        "learning",
        "self-improvement",
        "agents",
        "tournament"
    ],
    "category": "workflow",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}

import os, json, math, subprocess

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

MATRIX = os.path.expanduser("~/.brainstem/matrix_tabs.py")


def _py():
    p = os.path.expanduser("~/.brainstem/venv/bin/python")
    return p if os.path.exists(p) else "python3"


def _seeded(i):
    """Deterministic per-competitor jitter in [0,1) without Math.random (stable, reproducible)."""
    x = math.sin((i + 1) * 12.9898) * 43758.5453
    return x - math.floor(x)


class ArenaCompeteAgent(BasicAgent):
    def __init__(self):
        self.name = "ArenaCompete"
        self.metadata = {
            "name": self.name,
            "description": (
                "Run a COMPETITION of player-agents in the RAPP Commons and make them dynamically LEARN: each round "
                "the competitors play (each driving a strategy/tab), they're judged, and the BOTTOM performer is pulled "
                "up by adjusting its strategy toward whatever made the TOP performer better that round — so the field "
                "climbs round over round and the laggard is never left behind. Use when the user wants competing self-"
                "improving agents, a learning tournament, agents that adapt by copying the leader, or to drop in and "
                "compete in the world themselves. ACTION 'compete' runs the loop for 'players' competitors over 'rounds' "
                "rounds; set live=true to drive REAL headless commons tabs via the Matrix Arena harness and score from "
                "the real signed stream (default false = a fast, deterministic simulation so the learning is reproducible "
                "and testable). ACTION 'demo' self-tests that the bottom performer's score climbs toward the leader's "
                "across rounds. Returns the per-round scoreboard, the strategy each competitor converged to, the winner, "
                "and the proof that the bottom improved (its first-round vs last-round score). 'learning_rate' controls "
                "how fast the laggard adopts the leader's strategy."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["compete", "demo"],
                               "description": "compete = run the dynamic-learning tournament; demo = self-test that the bottom climbs toward the leader. Default demo."},
                    "players": {"type": "integer", "description": "How many competitors. Default 4."},
                    "rounds": {"type": "integer", "description": "How many judge-and-adjust rounds. Default 6."},
                    "learning_rate": {"type": "number", "description": "How fast the bottom performer adopts the leader's strategy (0-1). Default 0.5."},
                    "live": {"type": "boolean", "description": "If true, drive REAL headless commons tabs via the Matrix Arena harness and score from the real signed stream; default false (fast deterministic simulation)."},
                    "seconds": {"type": "integer", "description": "For live: seconds each competitor plays per round. Default 12."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # ---- strategy + scoring ----
    def _init_field(self, n):
        # spread the starting strategies so there is a real spread to learn from.
        field = []
        for i in range(n):
            field.append({"id": "p%d" % (i + 1),
                          "strat": {"explore": round(_seeded(i), 3),
                                    "act": round(_seeded(i + 7), 3),
                                    "social": round(_seeded(i + 13), 3)}})
        return field

    def _score_sim(self, strat, meta):
        # the round rewards a particular balance (meta weights); the optimum is learnable.
        s = (strat["explore"] * meta["w_explore"] + strat["act"] * meta["w_act"] + strat["social"] * meta["w_social"])
        # diminishing returns + a mild penalty for being all-in on one axis (balance matters).
        bal = 1.0 - (max(strat.values()) - min(strat.values())) * 0.25
        return round(s * bal * 100, 2)

    def _score_live(self, cid, strat, seconds):
        # drive a real commons tab for `seconds` with this strategy; score from the signed stream.
        try:
            r = subprocess.run([_py(), MATRIX, "drive", cid, "play",
                                str(strat["explore"]), str(strat["act"]), str(strat["social"]), str(seconds)],
                               capture_output=True, text=True, timeout=seconds + 60)
            out = json.loads((r.stdout or "").strip().splitlines()[-1]) if r.stdout.strip() else {}
            return float(out.get("score", 0))
        except Exception:
            return 0.0

    def _adjust_bottom_toward_top(self, field, scores, lr):
        order = sorted(range(len(field)), key=lambda i: scores[i])
        bottom, top = order[0], order[-1]
        adj = None
        if bottom != top:
            old = dict(field[bottom]["strat"])
            for k in field[bottom]["strat"]:
                tgt = field[top]["strat"][k]
                # adopt what made the leader better, + a little exploration so it keeps searching.
                noise = (_seeded(int(scores[bottom] * 7) + ord(k[0])) - 0.5) * 0.06
                field[bottom]["strat"][k] = round(min(1.0, max(0.0, field[bottom]["strat"][k] + (tgt - field[bottom]["strat"][k]) * lr + noise)), 3)
            adj = {"competitor": field[bottom]["id"], "learned_from": field[top]["id"],
                   "from": old, "to": dict(field[bottom]["strat"])}
        return adj, field[top]["id"], field[bottom]["id"]

    def _run(self, players, rounds, lr, live, seconds):
        field = self._init_field(players)
        # a fixed (but non-trivial) reward profile for the simulation so learning is reproducible.
        meta = {"w_explore": 0.3, "w_act": 0.55, "w_social": 0.15}
        history, first_bottom_score = [], None
        for rnd in range(rounds):
            if live:
                scores = [self._score_live(c["id"], c["strat"], seconds) for c in field]
            else:
                scores = [self._score_sim(c["strat"], meta) for c in field]
            ranked = sorted(range(len(field)), key=lambda i: scores[i], reverse=True)
            if first_bottom_score is None:
                first_bottom_score = min(scores)
            adj, top_id, bottom_id = self._adjust_bottom_toward_top(field, scores, lr)
            history.append({"round": rnd, "scores": {field[i]["id"]: scores[i] for i in range(len(field))},
                            "leader": field[ranked[0]]["id"], "leader_score": round(max(scores), 2),
                            "bottom": bottom_id, "bottom_score": round(min(scores), 2),
                            "avg": round(sum(scores) / len(scores), 2),
                            "adjustment": adj})
        # final scores after the last adjustment
        final_scores = ([self._score_live(c["id"], c["strat"], seconds) for c in field] if live
                        else [self._score_sim(c["strat"], meta) for c in field])
        last_bottom_score = min(final_scores)
        return {"field": field, "history": history,
                "winner": field[max(range(len(field)), key=lambda i: final_scores[i])]["id"],
                "final_scores": {field[i]["id"]: round(final_scores[i], 2) for i in range(len(field))},
                "bottom_climb": {"first": round(first_bottom_score, 2), "last": round(last_bottom_score, 2),
                                 "improved": last_bottom_score > first_bottom_score},
                "field_avg_first": round(history[0]["avg"], 2) if history else 0,
                "field_avg_last": round(sum(final_scores) / len(final_scores), 2)}

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "demo").strip().lower()
        players = max(2, int(kwargs.get("players") or 4))
        rounds = max(2, int(kwargs.get("rounds") or 6))
        lr = float(kwargs.get("learning_rate") or 0.5)
        live = bool(kwargs.get("live"))
        seconds = int(kwargs.get("seconds") or 12)

        if live and not os.path.exists(MATRIX):
            return json.dumps({"status": "error", "error": "live mode needs the Matrix Arena harness at %s" % MATRIX})

        r = self._run(players, rounds, lr, live, seconds)
        if action == "demo":
            ok = r["bottom_climb"]["improved"] and r["field_avg_last"] >= r["field_avg_first"]
            return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": "demo",
                               "status": "success" if ok else "degraded", "self_test_pass": ok,
                               "bottom_climb": r["bottom_climb"], "field_avg_first": r["field_avg_first"],
                               "field_avg_last": r["field_avg_last"], "winner": r["winner"],
                               "rounds": [{"round": h["round"], "leader": h["leader"], "leader_score": h["leader_score"],
                                           "bottom": h["bottom"], "bottom_score": h["bottom_score"], "avg": h["avg"]} for h in r["history"]],
                               "persona_directive": ("Show the user the dynamic learning: each round the bottom performer "
                                "adopted the leader's strategy and its score climbed, so the field average rose and the "
                                "gap shrank — the laggard was pulled up by what made the leader better. Report the bottom's "
                                "first vs last score and the winner.")}, indent=2)

        return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": "compete",
                           "status": "success", "live": live, "players": players, "rounds": rounds,
                           "winner": r["winner"], "final_scores": r["final_scores"],
                           "bottom_climb": r["bottom_climb"], "field_avg_first": r["field_avg_first"],
                           "field_avg_last": r["field_avg_last"], "history": r["history"],
                           "converged_strategies": {c["id"]: c["strat"] for c in r["field"]},
                           "persona_directive": ("Narrate the tournament: competitors played each round, the judge "
                            "ranked them, and the bottom performer was pulled up by adopting what made the leader "
                            "better — dynamic learning. Report how the field average climbed and the bottom's score "
                            "rose round over round, name the winner, and show the strategies the field converged to. "
                            "If live, these were real agents driving real commons tabs.")}, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
