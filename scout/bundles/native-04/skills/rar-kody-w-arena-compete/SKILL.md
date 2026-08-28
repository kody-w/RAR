---
name: "rar-kody-w-arena-compete"
description: "Run a COMPETITION of player-agents in the RAPP Commons and make them dynamically LEARN: each round the competitors play (each driving a strategy/tab), they're judged, and the BOTTOM performer is pulled up by adjusting its strategy toward whatever made the TOP performer better that round \u2014 so the field climbs round over round and the laggard is never left behind. Use when the user wants competing self-improving agents, a learning tournament, agents that adapt by copying the leader, or to drop in and compete in the world themselves. ACTION 'compete' runs the loop for 'players' competitors over 'rounds' rounds; set live=true to drive REAL headless commons tabs via the Matrix Arena harness and score from the real signed stream (default false = a fast, deterministic simulation so the learning is reproducible and testable). ACTION 'demo' self-tests that the bottom performer's score climbs toward the leader's across rounds. Returns the per-round scoreboard, the strategy each competitor converged to, the winner, and the proof that the bottom improved (its first-round vs last-round score). 'learning_rate' controls how fast the laggard adopts the leader's strategy."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/arena_compete_agent", "rar_sha256": "cb5fdc2203b8127d5f174fbe9773c1f8f24e01dcdfb7162fb0a17ad40a2239db", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["competition", "learning", "self-improvement", "agents", "tournament"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOiWNfnVzHyjTcq6zEr2RQ0O/qNYVEBFQFFkK6OanZQ9kXAnp7PPhfUzKyln66JmXnrnxK495xzz/I7y80/H4yq9JP84eXhlNjtp/rh6cF2CisP0jJIYvBaruKBMaA3a3G243bcRhgk7iANjdbJPxmeE5fFIIgHpe8MZFIUB3QSRUlcDIzYHkTGyem+RAO7jY0osIwwbAerGSkLLwPHsPxBnlRgXbfZSqLUKYMyyYue+uCxX2DnwTmIPSBBUeZG6XgtVBrmx6duT/shdwbHyvYc+6nn19GhNrvdZj1IndxN8sjJBwGgV4WhYw+qdGC2A8M+VkXZ0QyA6HeqgzKpjdwe1D54PINtkWH3sg92G/EdNdMpS/BfCZbdhP9coTAyGhRJv9oNnNAeWGEQmcVtQdKRu/68CxkantdxA7LFPbfQcUtA2w9i+3mgFA6Qw7kqtSrA59ro1HxTEZC8cEL3UxCleXJVTm8GoANAx8jj7lWZVDlQOXj/dPt8ldmwjbTs1GAladsv7MRxwGHzp0ECDpYAlSdpZ9JO2CtL527hOsnD/gQRkODsFM8Dku5d4sNt4YdBXsXFlWgCyACtDT5cnaX48JWNe6186NUCvlz//wUcrByEwdn5tcwr5yoMeBrIM3I18IGUoVP0euhdDDhCMTgHRs9ubZR50AzI3ImNgQ+00K3sjlBYCXATN0+ifl3uGOGgCLwYOAQwvmNEg0fbcY0qLAeuEQLV/wr06BoFUJwNTpRHQRwAf7HApqgKjS4q7sZ+1TawY+4Aa9iVFZihc7WzUwABQ+fjm5JsJ0o+XI3Xfb2ZpKNkJmUJBHz1sw/FTe6bJ928881YYIFh5UlxczJgCdkpgcmvugd0Pl09rqdiJmBzHzJv/t5H15tBwM8YWASEEuB1XVoHcdx5xd1pwflA5H8r8tULwbbHLpzcIC/KG+tzAfz89akXBOjiw11pXzpBOp+IyzwJi4Gf1L3avwoQw07Ssvj63PcjPAOochojSoFTPLz89vvTA5AlfHj588ECfMGrh94Z6Ktnkl0QgB2hEXvgU9oC1IvB803l4BXwgrsBHjsbPQ3+9a8TULtXfHz5HA9u/wyr94BfB4/Xb8+eUz5+fri+/vzwsQuizw+dpcHDM5A1SB8/PodJ7eSPH9/I3GIC0ImM5hF9AhFWfk3xtuJGcvTx3earyf/N3uuC21b8/dYwB9vcMDG+2fGVVW4b4efx+51dIP4KzJ6E32wFH8COd0sLB1i1F/A7yW6fbhwQFOx62xe4Vy6dx8VJOUiK59Qo/WenARFYPK7Jncxp743RK6P3+8GxSOJnu4rS4vFPwKY0ygpweQG2cPI8yT8/PL397N72jKIEgHzsOHbxbzCkHPwnoDT4z8GV/19fidyps3OW5y8A+B5vNnu6WegJqPupP9LTXScfvzrt3Zl+fXWZbw6XnAD9/LfPD9do+9LDweeH38Gbe+CBp15h3ao++3wxzt6XLvK6L//16zcf+ggFX35GiRYAeuOqrtxI00+5UwCYhJBn+KrOPrF033sNdOmmf3sLhZfXQz19zewH/762WFFZFlA9UDrQEVCB08FyR8zLAQbYV+Ydzy8djH5JjaLfmJx+htHXmnz5kXY78t9p7OVvFPkzPL+1y8uPrdXxvaLufcn96ae43KP+ZfDbn7en7sH/7fWh53AF0vuX+9O7T196rP56wf3dTwjyI3Xfid2fem43rX/F7et3/TKgoPvX/ufvf/Vlhd8VJZ2OfAAOSd6CDz+lJQDxwMuNL3aQO8BTzz1rgEzbLgG9Vlzdj1vR+prmv6tZv83agPo/awecoktqjv3jrNbHcl+ZvuX/rr79qr40QKoGwQdEKZzX/PxzzD0jHRR+bsSne+X6Pt/WxjfVclcPv9XCV2lvRXBXcqRJ/r4aAOf4OSn64LlXCLej3s9x9flnkCL+6lKbDTDm16/zxP8vtLoVsf8EWH8DVk+Dey58uWH+uyT+MnjNDe8D9ZYn/oHd32FCr8jYCK/hUrzhyvt3v/8T9f9eQPw/AsPX0H75JtL/icdrNfvlFlfBVT1/Wl3m7JDwZdD97L92ebJDFOuOKL0sHdD8E5u/wxLByDuuvTu/dWIv3zW5IMzeIOVadff97D9GUefi8emKIdFbif4dIH0Xzz32dC3LDwP7n9ne+t8bdHyLkK+QcMfSr+HqBmbfiPva6/zEoTu8+7arfhp06v2uZSnuMrx5wPsO/V278/wTnDn3FtOARNeeO/mtlbw11/c5Rf/ufYP6LY49/AX6lBjIVPXA07Up//Efg3XQNXOJWw62VlKVXRddBpHTgd4OeH3XYF6bVyB00beY13WgBDw61yIS9GZ//I/rDAcyugr2yw3OvvQi/vE82AEKSR54HTz0w5rPcf+pH5EArHDyro8z29L5BNznU/eji4g/fkDtOW3/uGaq2+iH5gaWkQLAdZ47odVufHEV0TLigdM4VlV2MwELsHYD0LGBGtkpkvDcGQ7wL05BGA6ucQRC/FrRVvFLR+yPP/4wjcL/HF+bNmxwHU8VEFjwKs7g0ydwBjcMPL/8HDuWnww+/PnXh8H/HPy7XT3xjocIasi3+QC/Be066Fqq6DbfKkoQIL2K//zrpklABvjaABgkcO++FQZdUN7VumXJT+gYB+nS7dwbFOwgNK6Dp+cBcKhXebvhAfgEeg0QOCAf2k7qdP5itX27/Tl+1WTXFRVGGRRu+9QVKj3XP8zc6EUEgA2W/zFY0yJw6yTsBihAzOt8zYiTuJvAvRr9bb4EIpC6k3geCP1EKjVAEgV1wo2Ha1ztAmDyvh0QN0DzVH+Ou77b6VTVT0eu6gGLgGasm0k/dTbv48LoGsMb736N0ZVCuwSAPkhqcXHzZqOPL6uL8nbgVYFtxJbzy82lQGhXIIY7/d1KtZsV7JtVeh983/3fASv/6WHmLYafboD8HqY73+xAtVv3Of5u4PizY8Z/GDH2ldG1bo8fvwXaj8CByg9Xp5vpBehVgce8Hwv25gBG7EiBI6dpGPRYdy9DXgD3uL2O10B9Et/GQf0sBmgIIBd0l/lt1trDtP2dLt4XkL2Axdu47Z5YevUD816r2NpPwn+YlV5Jt0k1eEyuNn718o89pvxoTAmcvjf9jp0NVhug1cf0Tu86NkCeB7NvBl+dQrrIuwpQB6XfW8yq8rxT4avlHjv8f7kNJI3vgP4+iLwlkv+LcSQE4DINk7wPpl+6seML4PfVLPLG5ErrB8PI++yxP04XMcZ1sGLmSQ3i/eNzRwB9HvAKs5iB2qrrBt7XJsB/e9r9Oux5ICqr1UARB51er/7+Moj7uLhOemvnXsV/1cr8aGp5C8Q/bqXK8NduJPWv24EeS2DTT7e64OMf98XBs/P8dC1dBv/6OnRuwfLOntc3/3oekODMZQmU8E6dNz5xEgBcOzlOCuK9vFrDSsIQZLC+inncXeuGJPa6k0UGiOcQ6NnsR6ug+eiqmKLH7rA7Zk8KhJ+RW35HoJ/yjPpqyAHSvmu0ep/vhre3kuhqwhyIU7zG0q1FA7mk+OWrUeuPbgs6d9/eFX7us+ft6gTExm/wE/L7x5ebBpzBYwQCDOpRdeBdw+KpG0IB5+598+qH15ao+Ng1nVbQZYzHwmih3AkBl49XeL/J7XQG7qLHNMIOoa8+3UeSD0DH6WIjAcnjnOS/vHmoHRS9DJ3y+wMwIJY/AXkfKaMIrH5UC7inVefdpR0G5qBn9/g2tCt8Jwx74v8Len5FBijqw+5LX3ilLZBVSAYix13zwfVYPQ7cAeM1Pd4A9tOrjHeP6pLRt3O9365Dvd8/Dj7917sJ+8A5J2F1d7Nu9HWbht7m/S+DHpl/XKn/3aD/HSQW3fg6sIBSnYeXGCSgp4eu8v1m0N3NtEHujjq8KLppOGDaOW3g9E9X43a/vr7mu2vk179XyVsn88v1dL++ne27e4G/O8/zgLndtnQk+hl+XEUPL7/dJegvIKME9HgPZZt2p+uG6LHXFc5fTam/PwP7/grhOw3/u7uEwSP8Cfn4Jhv8PO5EuwkABDSdvBcAmP17vqCW6+6rnv47bqs61b+/rXrsD/x3N1Uf352im9w7Rtwd4+bPP9ZgXxi8ywZvWhm9owbqP8e7KuXmnH9PrC+hPoHjfbpWRa93VnfC+I8J32bm31OeA5C7puP7VYPzw6z+mv3fWCHoj3h1p3CyCtSq9vUq6bYgMbv26qay8npR9OcDiC3DNkrjFl23Dgwsz438U9GVqN3UCbABz9dWA3z7N73ZbSUo40C70MWiOXZtC0VhzJwgKGGPXYQYuaYzJQjMQtyJi44cGLEt2zUJBEddEzYQwrBHsIGi2NQ2Ab0CxKrldGyioOMOo7iLTMwRPMUczLFgwkJdbDy17SmOTEbYxIFR2IBN523rCWSX25GuQnZKem0Teyi5nuzPBxMfdeYeFRx5/UdDBGI6KHQU/BWEjYd0ii+5clMklyOBT9b8HJzsXCX29KAXtF8XdDjWE7Up9f3slAUmy412xMy1VgTPWJeU3i1PKVZoGjvWm80y3iwm7lFgrGTtLXg4VVzSHRsHRc4pCIIEdzdX5qPhhbVRyDlfGsh2iQzbF1GIX9bDvZEciNHWt2fFcuzr9NjkLspBdYp6uK/C5Xq92An7TbssuWYEa8s2yEXLJhIfc+PxEHKK+TJJ95KZ7P19UajqxJWPqYKo+dxbCKu9jHHHfeiH4xrRlmZpWgWJiJQ5w13IdVRiIjUFCW1sd7H22zluml7UNn7l0BnJp/JljuscjK40aGznxCmTrQXc8i6LGroyCdNComTVyqQZmdphnJyUiCnlqbw9zJFKzaragHywhTsVR54bZ2u3bpRoOrrMWlQepbUmBXOZ0ffSruIcJ58f0vlwKhSZs1scvUJSDDaQkXzbrhFjnHDleryIV+voclF4U/UuaM62rYpEjUKDlmJOTpaEJEcjLzxzlN02y9IX1lsdKY76rjZiF5qccmRITZN1O04NgYIb288uIaLPYh7WE65awjSdjzV8F+0UfZlFilQqCOWVF0VgFcPLYnpMaHkyxw+lpfMX2xuKm8VirNnrM4dT4SH1BQPe2bydNU6Q5MKedJPZLuHPKHnalahSeWoRBY1bW7v13A5iLj3q+ukwy3ndYHlHU9RdARRDYlKxWUirIjku6/Vq7Uw9yDwd5UMWROz0ND5OpwBsoTPftr50zo/N1BBlnUuwXVyYBWQMzxohuNhFUDJNa5bbIpklwflMzis7meH4ucQM7DIKWBZDYc4gpxwU53OrUGw1FGiSOwx1SN5NZX9zUdc7jzROBaOdFUZeawt+JBNWcIx4lMrWBknwo+3qMKX1MKuX7XwZLJrjTmc4ceOEVI7NV0zNtjk1VY1GSjyUhdcIVdUVxamnrFRIc2yHmalxyhH2qYxd7HN+TlKL1mmcllmSWjHfamSuLxlv6FlnKvUaORTqvQ7PLlLOxDt1GVTVlCzyGFHkaMVJCxIdq1R+oAiKr00byvb7yUpeKqIhkz5DjyKuEVf4Jp0haG2Rm8bmeUlaIgXDUfSs3lS75TjBpNFCmlmGGEW6ztSur6fn3XjHeVJM0mg8N8PMk7tg9muOFw6qEF1Uj65pEl60vDlU8ZOWnxZRZEgASezjdNfQl4Zg9AnpVMVQWp9k/RA2Kl6c4ou5XnALRTFROKirOb4SaXcLXQJ+UUsjdE9zF4vd2fumOhj2mdfOEO6r9Wa13h7Mi5bNqPo4LRGSzS1zOUW50KMOizllqW0I+/aRTi+rgEIgfazWp81RGYV5FLqbYr9oT4xizTSpnS63ojfdYvohz5gqHMPOio7lenbKhfmEASXv6sB67nocEZQwtgx6V9rH+rBOaGqbYaB2OQn8aHaACjulxNHULfJIxUUTHo24krEydb6Bh1VqUBuJVC3GcwOY9RwmkYlI2J5Wh2CMCelmtgtldXFyPQlRvUPdZKVua+ZUp4n9TPQ7OD4dmKWK0Y40zzSIy4ShpG6GAXeax+FcDJvzHnFImcuwZbzfXpBqOMsZnFPnNHVp7GoUwRpZRrshGqHm1ER0xZ3suG02Xx7kkQCCueTpwNrPzxbGIcoerkiETYkzYlmjRU0I48i7AG6ZlByyrZVMtGq/NNg4yf3FZjsyJzA5SjOeW+ezIwa5idBaK4YhYiY+YAlxlunFVm6PNF8ecLWRfRJe1tQcT+Yt75O0XwlHoABDYv10rLTTDLg3vhHMwhgeKGgjnqiU5GPruJZLzmNkDcRpspBX+ZY1T8yYO+GHjTJMZaP1lwp5WjL4aCuiuyNz0KZHkYw9N107kwrXoBnr8poA0p09W5/8TYEekq24xoqU9jh8PtqesFjE18Ps3PDIeUsXCQcfaWsDYi9Qw5EcQlhu1DqzbCqxQA31sCHsms2EM5TA8v602Coe3xwKhy55+xLNvZl/9JYjTB9arnaGhWCWkXpM+wuG2+p8vQySSb0hmUDaScZR8c3xToezwHMl4OWYOD2dZCUey2ZwJr1ArVJUXXJb1V+SAEgLrtXbJWnR1ZBKFUZUpUwKmJ3IsjoDkgmOerSxOZv58QAb+2BWDZW90JyVuaPMo3DEOn5uHbxM8riEkJfrs5cHPns6WUq59Iex1Jy2vh8SF47ZcJiJ8yIBfGYI1fuhK7oYPty5zQR1xRhKA0xZUfKmINdLaWkicwzx3amW2BZcDJF9hjtbLNuMoXI/EtbLKlxPxlCsTPQEp3fqrCkxEbNreXqsN8XkxDjEWtSHkHtAs2Dpt6vIQ6Gk3LbZbj294HPDgbAWLDEz3SZVgYnxOJum3njhZ/iozjgXbtLzqZzxKCNnastnjAkPM8FaSVXjJ6232OyGsGLIwYSlL8aKksqAD2gnw8lpGTEa48BYjAzzmFLS3TTLF+JselAWvFn4mdDElE6B0kcmsaZEgu3+dMRY98xKepE1Q/QyJ6MJsyB1gTdX4OzbaEd5F4KiwrRdW7PS2XuTMcEJWMRvrMU0PpXCShLF8ZJgzYiXEQ+rYn5GRpok7MpWdni5QULOhh3UPRbGIYIhaTeJGUrdr/F1djCddejgbIg6Z1ROT605303FdKntHJUZJumUOCISX+iVlyzxWJnV/ulwWJ8Qg23c1U5TDDfjhGJrYmsfSZBFrhmtfpxmNKqHWEYzs0kyPKGIhdUjyT8n0RbNI6RJR+uZLRozibWGsW/C87VFTLc6W3hx4TF5Xh2tZoZP20NCxyrutmuf3Up0qVlzq9SDdrYQJtE2LLEFXgkyBg/ZgjnK2B5NiSMAiCwZh1Riu61/uhxou2EoTbN4eVXW7I6fS5K/IQX1xE8W7KI0lXjizZuhP5OwBSSfvCVhbkrPnArzwKVW5rTZTATJ9ty9nRSzmYrU7hJhwtqShha/KhwGEfU42pqwDpVmLeuYVgYoqAVxYz3cDpsaKGM4rmfc1tJI7CyIZKL47ISslxm1V4aV6BDxZIFOeSo+WOOVYcfDaXwACG2t0t3mWCz2RxTZGsEyHZ+PezcZ2cchXFPRupqe+VIU3YtT8LUV16BdqYxmPREJsiXLfOP7ukwWMgjZbcFpFhNP5OHqUggSxmwvTJIySqEMFxyBtrg1r9cb5ugiscToRLqJ1anGiHFSoxQelGE2Q1k7n9Vzxk6WumNdEtDV4OWKPntzWG+UcbNNp7J6ilACWQK9u8c5sh/WB8hPz866MUBEggrebFM7UZC5MkUFB3KLOdxqB17b8962NNt9YHgLpZpt06yZNpS1Qmj0LHPjhDD91FzmTZgkFExDqn7wYXpXULxf2OIIPmQHptS2k/lGSlycnhQFfJhPWgTEiVTQpH2qNiNyxIw0qz2UPrpZiKiwSjTZryQCeIGmXaYbZVdMHM6L7U0sb47VKkq5aouzc2aerRRXFji7trjDUTIQzZ5dDuwJRZvxIYyOS2ozXwm0anD0NBLquWCzdrzbw6QZMAfcDfbHw5ndouGSYRUxcEo2mfpLQ6BleGZf1ijBspcZwhBuuCMESNBxS3Phw3TOnrapHPmkPkI2w32SrFmd90SXPEJ+ZUdbtYVniL0fHwvQm4ljlV4bPqHu/ZWrLvJEgJFZMtdguoIxD8CiOhqZtlqfA2M81qSDLPt5HZe4NUoE0AwM1/FFMwSdRM+jIN6CTgZZNxVIV8z6WCfDy2G8DI+7mc3GWlG5rkFtteHFwEaXPeFGrKbqiadVNWPV9ngEjSO5Pu/cmL3MFUadzTGpWqsm6pJrf65Z+0pAdlsPqpja9DB24xmbWjyNBNhvMtFaChvZdTVJiuEdpSVqaET5+lLEq6UxM10hn4aLemXrsSQ5BT6JlIOVxJG7xmdkfQn2oi0HmcoXig+zmCQzc3VF70khwy/MZqfXCt5MtAZX1RnfQsiYzVRRO45twd6XSYkeFhQdr+ot7104K2OcrSxNJwyzgfV4NptAuknCl3KkzbG5XkxmUKpxE0+PLjZF5bLGRhu+UZ3LYX3cLhQya5vDGOc4Yz+bIbm3RZF4I4wqpUAvWTBvTlolG2VGJVvF1rciFVjHEGh+oUZpVO/GAdVg6yMBHTeIIkBRsJjn+XZbnDKDt8xqPFmBHNzUQxbShe120fpaFG9YHjIEtoBXK3Qak2ceAV6k6RHUziv8nGulOkZrhNgcZ1G9SV14MV9cDi0RoeUZYZOCoBRntBjuNnWy26QKYUhUeU5wklE97Exy0xkmU3s18I0zvz8OjXp1okiCkrimYUYkFTeCWKPxhjwPp9ZEBwUJoR2hudBweUQGtAyQuSqLNs6pFCfLhqZCIqUZxyMnoKA3uBQ+lkd1ly/nSeOTKLXAW5mfiEdOdplLLGFbHK0hc+EqY2YBScFsze6AdBtGrhYRgZwWo9W0ivBAKSZn1K/34gVpIxZdHV2FtpaR1Jgstb5UjoyPyJrTJ5Gz2JGQoyZs1RbOVEmwPZ35O2m9QDfxiF+JklKi6XbjXhBoF0/Q1BqdxBhzMp9pZ6l/2RCG4NYIJxynvr07VtQRqoCZ5zCy5feRRaRbnqR4rRFV0axnDL2Pp87lhGRFqwrp/jydTYen+hBWKS2MxLG030enIdnmWyZcsWXtBZAK1fMTpE0UfqcA6LGPCpywZC0IKKDG0B67SIbBPDqrXmjw0yPlMKq+xETiBE8hY7fjnGKSOjDZivJhM9xcFnxxyOzFxdKd8UlcK0VZ+s4sm2yQGqYo47KA6Ub2ZgUhkeJlxSwNKcWXflUGOWNUI4ffS6fCTCU092wMN43MrSnbzZFsX6WZgk9PfF0jEyqEW5aHtV05X06h8WElrunogueCe0l3yGgOGeE+P0v1ZXEQoyHNi7VLEtxmaMK0wmnI0GAP2yQAVYJKruDgvHcLZcbHhjmhQZop/XRmDCFvQYlKWsYkauMCnkwJhypt03Epd7QeuXTj5jxzxOBjMVnF07TB97SERiP6ZFBhQRbpmJtJW6E1EVvEIZXIwGEkTjm7VjkRSCEHOS0lq2M0uxAtYaMWHoiTFR3gORtT1HQyx9Gh5DUH/LDgFVvGlg0qhwwf2yVlLwiPPHiaG+kwNToeMEbfEQZlce5qtlMym2UsITiPrBM6z2WHiBK+OqAQw4Ms1Bh7EXRTDa/m4pk3Z2mlTekprK+WGNGGlXZAbV9txpBztshwr/ukXVQ1PB41Z6Yu8mLjIAvRFTD5oiVm5k2WgaunmO4TjSTZ2oY3PR3Jrel5JCfr6fyicoappIIh5aYZpOsNRyf69jSCXaKdSk49zTRN2isTNydxI/Q1NJlMTL4giGaaBSZziOKxt1xtQ4JBQz2+BDoa4V6SQ6Oy2tKCh8zm6NbOqMXuPHStaBhhKmtuKRvLhiWRrauJOMlsfIhjsyq4RChuo2FAmUdonW0Rv+ut1hPQLbGzUCvmp0O295LW4Y7QaT2x8iMW88IWl/eQu8MmCyg+5wsP8tpkeSZUdy+n6hBUprY2WokEJLGzaFhtA8I8qeFwpE3Py2aE41htLZPKOC6IcIJS8zS/6AaCJSf+eN4r7qY57HlNRCsWYR2lcfxyuQj8S2FozJRkRjQ8WvLDOJJXnoHJ55lnQCNqf7Sm7hkzZgixF+OjpXmmMqqr8xBeWBMZdJJxA/rxYzPmStGlh+IymEyXvhuheUqZgjo6sBZ7OFvufG6LKFkSY+7ssAJdE4S2EcmN5EzJwmT1JbygqmFKYSBhZvSQjg9bpKywnV+zCjskpf2a9PVIxNhJnQdbezweif5431gTJJrYDjFGG6lK4NafWqwj1QsrG7Zcw9SyRxBDccLnDb7cq6hNcG56sFdCMpLHzmUzD1Ub2FovKxtSh7s94XEmg3DuEWoRreVyqzDhIoZ0Z+dgk3FDW+YZOl82M4meX4hjPW3RzFZEaZfK25VP6YTNcOZJ3F3sqj2tpwhcG5PlyM/hqmKOCWqHyQRdhWJ4kqMzcKmR5mBuKO423rKycdKuY50obCgG1U0DmXvYU0Bd4GoqvBwv0RiDl+kQN3XigvOY51iQVxG5HyoISZK/Pjw9dH+Fcrsy+/EfNXXj7/9nU/jrwDw5A0ax5XRXXLlj2C89r5e/4f/700NuBYD79QKhCCvvNoS/Xh986vd9ersrK9rrH/4kcek05f1esDS84u1Orb/FfHi7Puu2ffOnIuDV9e9fusuR13u+Tpz+L8762w0g0jPy8Nf/Box+SogzOAAA -->
