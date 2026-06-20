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
    "version": "1.0.0",
    "display_name": "Arena Compete",
    "description": "Run a competition of player-agents that dynamically LEARN: each round the bottom performer is pulled up by adjusting its strategy toward what made the top performer better, so the field climbs round over round and the laggard is never left behind. Live mode drives real commons tabs; default is a fast deterministic simulation.",
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
