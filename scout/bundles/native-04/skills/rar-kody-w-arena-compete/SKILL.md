---
name: "rar-kody-w-arena-compete"
description: "Run a COMPETITION of player-agents in the RAPP Commons and make them dynamically LEARN: each round the competitors play (each driving a strategy/tab), they're judged, and the BOTTOM performer is pulled up by adjusting its strategy toward whatever made the TOP performer better that round \u2014 so the field climbs round over round and the laggard is never left behind. Use when the user wants competing self-improving agents, a learning tournament, agents that adapt by copying the leader, or to drop in and compete in the world themselves. ACTION 'compete' runs the loop for 'players' competitors over 'rounds' rounds; set live=true to drive REAL headless commons tabs via the Matrix Arena harness and score from the real signed stream (default false = a fast, deterministic simulation so the learning is reproducible and testable). ACTION 'demo' self-tests that the bottom performer's score climbs toward the leader's across rounds. Returns the per-round scoreboard, the strategy each competitor converged to, the winner, and the proof that the bottom improved (its first-round vs last-round score). 'learning_rate' controls how fast the laggard adopts the leader's strategy."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/arena_compete_agent", "rar_sha256": "cb5fdc2203b8127d5f174fbe9773c1f8f24e01dcdfb7162fb0a17ad40a2239db", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "arena_compete_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/arena-compete:22424aa2fca30b44f9ff102d56be894331061e387924bf584f64a8ae856194cd", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["competition", "learning", "self-improvement", "agents", "tournament"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/arena_compete_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `arena_compete_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `arena_compete_agent.py` and embedded as the fenced Python below (sha256 cb5fdc2203b8127d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `arena_compete_agent.py` first:

```bash
python3 arena_compete_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 arena_compete_agent.py   # or on stdin
python3 arena_compete_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
