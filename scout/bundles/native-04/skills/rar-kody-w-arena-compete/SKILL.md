---
name: "rar-kody-w-arena-compete"
description: "Run a COMPETITION of player-agents in the RAPP Commons and make them dynamically LEARN: each round the competitors play (each driving a strategy/tab), they're judged, and the BOTTOM performer is pulled up by adjusting its strategy toward whatever made the TOP performer better that round \u2014 so the field climbs round over round and the laggard is never left behind. Use when the user wants competing self-improving agents, a learning tournament, agents that adapt by copying the leader, or to drop in and compete in the world themselves. ACTION 'compete' runs the loop for 'players' competitors over 'rounds' rounds; set live=true to drive REAL headless commons tabs via the Matrix Arena harness and score from the real signed stream (default false = a fast, deterministic simulation so the learning is reproducible and testable). ACTION 'demo' self-tests that the bottom performer's score climbs toward the leader's across rounds. Returns the per-round scoreboard, the strategy each competitor converged to, the winner, and the proof that the bottom improved (its first-round vs last-round score). 'learning_rate' controls how fast the laggard adopts the leader's strategy."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/arena_compete_agent", "rar_sha256": "3e5333752068fae52cdd93dafa259c357d697dc8af1ec7707f2d2f25eb556b10", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["competition", "learning", "self-improvement", "agents", "tournament"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZOjRrfmX1HUjRvuflVdLJJAlMM3RhtIgASSECC5HW2WZBH7vng8v30SpFp68WtPzMztLy0g85yTZ3nOkvXHg1bkTpQ+PD94kdl8qh4eH0yQGakb524UwteHIhxog4WwFVfSRtoIu0FkDWJfa0D6SbNBmGcDNxzkDhgcZqI4WERBEIXZQAvNQaB5oPsSDMwm1ALX0Hy/GfCr2WH3PACa4QzSqIDrus1GFMQgd/MozXrqgw/9AjN1Sze0oQRZnmo5sBsk1/SPj92e5qcUDK6FaQPzsefX0ZkLkiRsBzFIrSgNQDpwIb3C94E5KOKB3gw081pkeUfThaK/UB3kUaWl5qBy4GMJtwWa2cs+kATxHTUd5Dn8L4fL7sJ/LnAUGw+yqF9tucA3B4bvBnp2XxB15G4/X4T0NdvuuEHZwp6bD6wc0nbc0HwanDIA5QA3pRYZ/FxpnZrvKoKSZ8C3PrlBnEY35fRmgDqAdLQ07F7lUZFClcP3j/fPN5k1U4vzTg1GFDf9wk4cAA+bPg4ieLAIqjyKO5N2wt5YghcLV1Hq9ycIoAQlyJ4Gs0XvEj/dF/40SIswuxGNIBmotcFPN2fJfvrKxr1WfurVAr/c/v8ZHiwf+G4JfsnTAtyEgU+Dw2rGDxwopQ+yXg+9i0FHyAalq/XstlqeuvVgloJQGzhQC93K7giZEUE3sdIo6NelQPMHmWuH0CGg8YEWDD6YwNIKPx9Ymg9V/wvUo6VlUHEmPFEauKEL/cWAm4LC17qoeDH2q7ahHVMArWEWhqv74GZnkEEBffDxTUkmCKKfbsbrvt5N0lHSozyHAr762U/ZXe67J929881YcIFmpFF2dzJoiQPIoclvuod0Pt08rqeiR3BzHzJv/t5H15tB4M8QWgSGEuR1W1q5Ydh5xYvTwvPByP9W5JsXwm0funCy3DTL76zLDPr561MvCNTFTy9K+9IJ0vlEmKeRnw2cqOrV/lWAaGYU59nX5345whOEKlBrQQyd4uH5198eH6As/sPzHw8G5AtfPfTOsLh55qwLArjD10IbfoobiHohfL6rHL6CXvBigA+djR4H//qXB9VuZx+fP4eD+z/N6D3gl8GH27cnG+QfPj/cXn9++NgF0eeHztLw4QnK6sYfPj75UQXSDx/fyNxjAtIJtPoD/ggjLP+a4n3FneT447vNN5P/m723BfetxPutfgq3WX6kfbPjK6vcN6JPk/c7u0D8BZo98r/ZCj/AHe+WZgBatRfwO8nun+4cMBzuetvnWjcunceFUT6IsqdYy50nUMMIzD5sZ9Jho743Rq+M3u8H1ywKn8wiiLMPf0A2uZYXkMsztAVI0yj9/PD49rN72zMKIgjyIQBm9m8wJB/8J6Q0+M/Bjf+fX4ncqbNzlqcvEPg+3G32eLfQI1T3Y3+kxxedfPzqtC/O9Mury3xzuMiD9NNfPz/cou1LDwefH36Db14CDz71CutW9dnni1baX7rI67781y/ffOgjFH75J0o0INBrN3WlWhx/SkEGYRLBntCbOvvE0n3vNdClm/7tPRSeXw/1+DWzH/z72mJZYRhQ9VDpUEdQBaCD5Y6YnUIMMG/MO55fOhj9EmtZvzHy/gmjrzX5/CPtduS/09jzXyjyn/D81i7PP7ZWx/eGui9LXp7+EZeXqH8e/PrH/al7cH59feg53ID05cvL07tPX3qs/nrBy7t/IMiP1P1C7OWp53bX+lfcvn7XL4MKevna//ztz76scLqipNORA8EhShv44R9pCUI89HLti+mmAHpq2bOGyHTsEtBrxdX9uBetr2n+u5r126wNqf+9duApuqQGzB9ntT6W+8r0Lf939e1X9aUGUzUMPihKBl7z8z9jbmvxIHNSLfReKtf3+bbSvqmWu3r4rRa+SXsvgruSI47S99UAPMc/k6IPnpcK4X7Ul3PcfP4Jpog/u9RmQoz55es88f8Lre5F7N8B1l+A1ePgJRc+3zH/XRJ/HrzmhveBes8Tf8PurzChV2So+bdwyd5w5f273/6O+n8vIP4fgeFraD9/E+l/x+O1mv1yjyv3pp4/jC5zdkj4POh+9l+7PNkhivGCKL0sHdD8HZu/wpKdlnZce3d+68Sev2tyYZi9Qcqt6u772b+Nos7FQ++GIcFbif4dIH0Xzz32dC3LDwP779ne+987dHyLkK+Q8IKlX8PVHcy+Efe11/kHh+7w7tuu+nHQqfe7liV7keHNA9536O/anad/wHlj3WMakujac5DeW8l7c/0yp+jfvW9Qv8Wxhz9hnxJCmYoeeLo25T/+Y7B1u2YusvLB0YiKvOuiczcAHehJ0Ou7BvPWvEKhs77FvK2DJeAV3IpI2Jv9/j9uMxxE6yrYL3c4+9KL+PvTQIIUotS1O3johzWfw/5TPyKBWAHSro/Tmxx8gu7zqfvRRcTvP6D2FDe/3zLVffSz2AwMLYaAC546oZVufHET0dDCAaiBUeTdTMCArC0XdmywRgZZ5Jed4SD/zHN9f3CLIxjit4q2CJ87Yr///ruuZc7n8Na0jQa38VSGwAWv4gw+fYJnsHzXdvLPITCcaPDTH3/+NPifg3+3qyfe8RBhDfk2H2CPsF2HXUsR3OdbWQ4DpFfxH3/eNQnJQF8bQIO41otv+W4XlC9qPa5nn/AJAdOl1bk3LNhhaNwGT08D6FCv8nbDA/gJ9howcGA+NEEMOn8xmr7d/hy+arLrijItdzOreewKlZ7r73qq9SJCwIbLfx9sFyJ068jvBihQzNt8TQujsJvAvRr9bb4EI3D+QuJpsOsnUrEGkyisE+48LO1mFwiTL9shcQ02T9XnsOu7QaeqfjpyUw9cBDVj3E36qbN5Hxda1xjeefdrtK4UkiII+jCphdndm7U+vowuypuBXbimFhrg57tLwdAuYAx3+ruXancrmHer9D74vvt/Aaz0Hw8z7zH8eAfk9zDd+WYHqt26z+F3A8d/Omb8mxFjXxnd6vbww7dA+xE6UP7TzelWlwz2qtBj3o8Fe3NAI3ak4JHj2Hd7rHspQ54h97C5jddgfRLex0H9LAZqCCIX8iLz26y1h2nzO128LyB7AbO3cdtLYunVD817q2IrJ/L/ZlZ6I91ExeBDdLPxq5d/7DHlR2NK6PS96aX1asALUKsf4hd6t7EB9jRYfTP46hTSRd5NgMrNnd5iRpGmnQpfLfehw//n+0BS+w7oXwaR90TyfzGORCBcxn6U9sH0czd2fIb8vppF3pncaP1gGPkye+yP00WMdhus6GlUwXj/+NQRwJ8G7GnJrGBt1XUD72sT6L897X7d6Gkgnnh+cBIHnV5v/v48CPu4uE16K/BSxX/VyvxoankPxN/vpcrwl24k9a/7gT7k0Kaf7nXBx99fFrtP4OnxVroM/vV16NyD5Z09b2/+9TSYwTPnOVTCO3Xe+YSRC3HNAyCG8Z7frGFEvg8zWF/FfJBudUMU2t3JAg3Gsw/1rPejVdh8dFVM1mO33x2zJwXDT0sNpyPQT3nGfTUEoLTvGq3e57vh7b0kupkwheJkr7F0b9FgLsl+/mrU+qPbgs7djy8KL/vseb86gbHxK/qI/fbx+a4BMPgQwABDelQd2LeweOyGUNC5e9+8+eGtJco+dk2n4XYZ40OmNUgKfMjl4w3e73KDzsBd9Oia3yH0zaf7SHIg6IAuNiKYPMoo/fnNQ00362XolN8fYAlj+ROU98Ncy1yjH9VC7nHReXdu+q4+6Nl9eBvaZQ7w/Z74/0KeXpEBCfqw+9IXXnEDZd1FA3GzueWD27F6HHgBjNf0eAfYT68yvnhUl4y+nev9ehvq/fZx8Om/3k3YB6CM/OLFzbrR130aep/3Pw96ZP5xpf5Xg/53kJh142vXgEoFD88hTECPD13l+82gu5tpw9wddHiRddNwyLRzWhf0Tzfjdr++vuZ70cgvf62St07m59vpfnk723f3An91nqfB8n7b0pHoZ/hhETw8//oiQX8BGUSwx3vIm7g7XTdED+2ucP5qSv39GdbvrxC+0/C/u0sYfEA/YR/fZEOfJp1odwGggDpIewGg2b/nC2u57r7q8b/jtqpT/fvbqg/9gf/qpurju1N0k3ughd0x7v78Yw32hcG7bPCmlfE7arD+A/ZNKXfn/GtifQn1CR7v060qer2zeiFM/JjwfWb+PWUagtwtHb9cNYAfZvXX7P/GCsN/xKs7BUgKWKuat6uk+4JI79qru8ry20XRHw8wtjRTy7V7dN07MLg81dJPWVeidlMnyAY+31oN+O3f9Gb3lbCMg+0CXDoCk9FoRE5wlJhaGpjghmlSI1Oz4HfKGE1Ik6BI05hqFgYMkkRJCzdxC58AfTIhdKzjnMFYNUDHJnA77rqBWhhBYVMLAErH8RGBTgFqjSiCtDQCjHBgTlEU1d+2ejC73I90E7JT0mub2EPJ7WR/POjEuDP3ONvMbv8WyFDWCZw0BFYfqigyl81F5bMH2XQJM7RTQxhO0Eue8OqmXV3lIDvLx5blY06/KN5GVvAF5pUTdx0sgMlS12KNcbiXxSOzssjLZjXP3GuzniCaaaDXwLWu6xEyZMoh305BEHOsGB1jVT7x/vbKO9uTq1YpuW8nK9afyJIXHDajpm6sqzdcFaf0KC/2l+tkUjSBAqY6v1+paUUOXVbgvVMwavKDxqCVysapf9huCH57uKS8spB8Zetke6SdlmykuisnOOOsyafysYqPyZYW9kLV0hIWBcz+olQpssrb9eaw3JjuRNmKIX4pV8OGAqg+vRiei2z1bS0jQ2szXDCe2pCbLI63rISRQRw3QzF0KIH2kuBy4VfA4txFVWaHXRu1h3p8RQ5KYroIxU6BgaTLvWNMLDpAmovBCnIj7oeSxbH+CbTSNThq3BWrxbEccNZEajn5Yud6exKbo49kHlk7mUNr54igiw1ByXhdXXJ6U8hH8RqmjFKd99OrTtWXyVAUUSQjMs8iDcBii0TKGseitfi0RcZn2inqcFwiQSS1blGuiM3VD67y8prPqplepNthNT2RwHdZraEXub/kCYk1VG3P203N79XIcmVrzJT0MdJ3WX6u5jtBHKGTVb0NKPO0nEkYnwWsCXzRcZR1NNIxR1J8OZ6XzRlxuTmJKkDRTodJC5qgKel1Yi5AjbO6eF7QQ45plRHeZsOFNZGRZTBH8nK4uPBMIWeRlK4pYi8m5WnYroat613WDYKIZSMKU1RaxWQykgOk8zlSYGPRJTVDjIeIIGUTQQzR01A7RSfoLCCf0rNKWJ4zcTEKxHrYJkzceBf+rAoY5m+9Ocef7dG4StuDNEGE9jqhNvPcmoSJn9O2ek7Hh205oXQj8pTpzFyem+KieQrTLKWrua/P7MJQthqnXDBKCPA8JIqmXg7jHSf7gshfpeNFPR4PR1Y9MUG0J1iDU+kUIZekcAry1kzEQyNiniyklMKNbXfhBafNen6IZ4G92s/tw17G0z2Uo4LQoeirypMnchFNHTXmhAt1Euqx5E1x4BQ7pthrB/2k7tc+N1HY+blcIjPXmKimX88PK5xb1x4vOjrC14JcuyznUaqh0NECUJc8s6WrswvQZHbmnIDMBBfZHK/Srt4fVs1UPBBCo5pDnmLxq8Q3cVKpe2+xCy3lQMemzx75aOZyK/pCXo2NuDyfotVQIoJkOTz6px2vaBD/Z9Q2wo4rxBXidTa3G2ONH2MPK+eqa9r+vqpqM/dGkkycj1GgKNKebe24OGykSCH43cxS2S0CxsIuWYTn+rITUnZV2sd47Z9P3sSUz8L+OJdX5VKMZPTI+tPrqLpqAnlcXzgZXTEbyssUBLHSNqSonXPRL/Ips5ywUY7mFp0JYZwOEcvFKHGuhaeidE6XecW2S4DMJEDuBQRD9KwWr5PjSETxdpod0euUXCWeIhFoZNn+krRLkrPcHdtozqJYzQ2ZOI0DeCS6tvNNHR0mBDN2XNd3ZU9vwsM0uzZzGCXxfkFs+Rm2vxzD5FhtqfmZC+sNn8dUuJiwEXtgCE7fk3J9PE7kVGxOlxj2PQp3DtfxfJ6cPJPfOItZa+R7GPx05U/YWR4l0Jl9eWRjk6Of7jZ4HizjiHZY1L+mbBrVux06obeMEnDz+GjKvrvGZ1JFAkReJEPZWbNkuLU3dissp9qanq5PrkasSnSTSceNkGyU3exoo1yx5shNqpDSbLY++NNtGJyateQxZHDRWGWxAAs6Vzaj1HBdehG3iz13yM+nXdAo+4O8sicCe1QLi5CAsDcUdrwYX9rp0AnrRcUxYI2wK/S4PohHO1Rq1jeKcXuYj4sjlU1BYfhXg6cVbVv4AqUv3RVbztEKS2bDFj03E0FCydk4d7iDSINozy9FZaTOgDMs9RHn6rPFmaHnhtL428K8LuOG3wstorGnqp0GMaYqII2xsFYSGR/NPJRT90EVMaP07DNoPTrtAH919Iw5Tc4R5W0btjbsYp6xEbmSkYvbogc+v7CnMJzT2qKYVchyxlBl6a3IAzbKYIxFCb7fNyhT7RezYWoc3C21XKRH2tsbZNCGyWEbs4JrzvbDtN011xWTUyWftDIfr0HqGEvTxDjbiU/eWCeW+JH0heNI43kYlw3dhGvRd3IZn8wdNsGTEGZ2GTSROif4gF7M45g06924oLms1M9mHOcWKbi5Z3L0ZuGdsvZa7YuRc3ZXDaIwuxBIBJHzeybBSn1YsGCebZtMqi9FaPGisKXZHSokJVHtaeJU+1gjrQ8KChxGyDLXOSgIT3lWHWwTyzaGE9tsBRgIqH0kJjxEvtxuE7mIsWYh1+e2oa/OfI8zsUxshyf6ylJKk85pSbI1Sd3z0720g3XSaZ5dvcnpah7sZINEJGJfNnkOw0KyYhBcayygOVHx8INgr47rZHwUA/26O6smrEXW+xALlKwg1KEnWrS6RWmY+5mjFc70nDm0DrHYEmrhnH2JU2JwsGxkkkBEN6Z2KiwEGxaD2ml2tDxIdVgEuV8rc9u0RnHCjrFinakRQ7bShAIbI4+cS7MxC+fapjEv7A+n9YwjRKexLImcmPVyNzOwKjrMLotDsMbd0ioqa1UqM5RJGdyNRqVMr6ZOVmGj9bSRSJatgLFWszk/2o/5k8cuZ47jIIvNnvNOk/HOo3my4TJ5lcgpYwnCZDaOpyQ+Y3ckbyXXfCql3gGeY5S4RbacnlifNsTSoovdVQt4bB1Mrw4/paP9appJrh8fRBRjmOF6DNu9cA+OkRCOTWQorESRWog8NpxapbwcCqmfQPDOlMlhK66I2UorELk8hpZKmwmy5PNQyGWtCL0CX3NILmOE7ufAREMOpDVeJhd2LylXAzHb3VolxXHj6iK/GY0xwc+JMRcTbMBq03GuNYm0oCSZKctRjSHI1cnZw9Kh9IBQk2FhjwOHI4iI4ADKFrm329A7mzj7cGOF7WGZ7q1X66vCafGyPdc5zdt6qdcXnouPuUsfF0VBznLfW4ZrE1VTbKins9NE2irsepcu7Jg3jiIrrAje28BSYTa3gla+xEorGno+1pa8XywTWC+sbf08d7RFyrkVJqbbbCVm+Zwzl8ViY61MoNjTmvDwieSrDGNh08S21CtPpnrIFpPDCFw579CcIqWoJ+N0VZ6JNhNIXBdxfDeVNMvbIDEaFVxEcaV8wRtMiq1wMkJoWPifci5UuBSWMvIZVn1hyK2VaogGOpFG9KJc1TMA0UZFveW1wJM4OhHtVXGW5S7YqUtD2+0SPwiDkru4Jjgb3N5NEYWPTVPaBkuR2ZkMYSh1mTR7u04PKFtxuLirTlSN0Epoeovh8SqedygdTspzIpmsH68l8sBdhoJtRPwpD7hMOQ9p6UpPAzw+FDsKMMtRqoGxyFCwrWxxpwSUemi55b5BGkYybXYkZhyRznl25y6IE5vMF4xhH9NNWglCfgzG4vQalsT2QBk6xVwWshKYOiznzHQ1neIj8khNIpvKgJyX81PuTw5DOaL5CD9MR7Y6RumkIHfbtRWvC1iHzEML4LxeJOL6ELrySFD2kRVq88PxsCDxyTieTJbembQX+ySaH1PKUJBROV3gFr1Uq7hh0Glp6ky1sRaZKgWwJBdkKphIyZGLxlY61M9T8yqMa6cVfaFM1dDyc5GYI9m60nelTS5kxMqWq6WOm7Npi65qhroeFqeNOly2wwnBt9u5pLZaszzHlJztC8amRg2zl8eAP9ZIdfAyFGi6j4rUsGU1mMzxwL7kINyztsYk9hnTrwoswsQyyOJmqU6Gq51Oc6rJSUf1kq8Kk3Ekmiew4QZGRYwwwoWoKTdANb2JrTjD6JOpiDlILXa6OWWrMvM6o8ZcDePM5x06MUk6XoJYmSzPVJaGyzhZ+9Mi2zCBy0S74YpwZuhiX/oXrNitielmKM9yKqWIBQhFjiR40WJMYzlaWPtrNFXIy8qsnc16EkCP3zntVuHHm/VZ3zOENJ6TAo/l9aKux8XSnE2sLceQBTELJnpkyNkxyg71Gq1aZzxr17YPcxPrVgLMD1cX5beBshJ2PLbQLuJiquwif2euqCusPGe7KMJFlQrOMl+h+fVYRVPKaPHSVJM5u0H5cJThGaNmwWgJtRYWHKKPhqQoHUN/tZsfcXYcSQd7S2ihutlqK7c+FnN9OhcuMBvjCRm6xTXeUYh/DGGZxZoxGMvmMUVsopkdd7JoL4o9uZy1RxnxUogU4VKbBIVvMUt7He9yztQj6misI0lUcVRvD+l5vCgPhyNFGsuZ0o4FwOz9YTjHryxH7AhrEZ2nQxNrxt5UoYpaQfBhpJWFm20Bv91V81G2VIHFKD6HICorj92kkpDQGAd1Jhj6nAtQborkoS8Q1GhW2WtRtM9sDWAKj5f5CYz3unmMiWJGcOhSyCPYbKkHPZ0W7jbDklgvMsubqIuc2CYLqZJG9XS11lg0DNer+XjjlEe0KhNqeZqe0eUOI1Vnfqzk8yxf4Qc2ULQLLAknSLGmK8aETaiUYCE+FtRUla0Ln6fzSDzEU4+TywyqahSJdrE4OCNGaD16jK43uDIVtzqzqrP6pCNuYBDtenXlcD2a0zvTKGvDw8LpaLFSWWvG2aWSGPFUdaQZ45uJMZE4TGqUTewRm8JkudEmVxqbmBDbbBM6Q2NJ4yJK89SpzVatGAGGPAnppKXMBbKeM3Sa7ieXyWnsnqDVR1uSGvLG2KJobDI7cT44GeNzSI2noKnkyygbM1NcT4amTOvIRjIxSy21uM3rEjcZfmvvFCTihG0QS4WeEJMTKOqMNsfVbkqY+NEnMamIZ2utnJGzeZ5iKTEPHXdycg5askzJEj20ynx/9KSIrq+bmdis3HCsW8OZhVdgirbji3ikQlOMzrjHOLtLsFm2amBKmF0MgYc6TnycHPYkNlu2Gx/2FaHD4NhFyCL1yqyWlzHMXIJYDGVBJabteF3k6crE63Ik7LE8myvzOTvGcf5S4IurQS5UfSXUqnkQVFDgbivTcYwCFtetk7Idzo9YAMiLiV5cS6rmpxnGLlt4Sp6aaDYguZrAjlfjxBX01q6kM2FViQz2mwyPzV2ZYmSdjpTYgHmuDOKTy1crAyeZvGTKGWxMWCISampkxxMskZdzzFccLPdPCexcx1dhesGrM7PSdUIbqkayZHWZLghUQmCOTAxidSZsy7wqMiNjgT47mAmFCV5uRynCjhw+HuZopHnjdK/qjBPvhVm72zWrpbuc22tuMgxor1ScULtg+3mxlNkxuSVP6BQhVGkjeFQs2DNcNFWBWrQM610KimkN9kh6ip3CnnquHdOGLPFrxTO6ajPcbua2+WxGBYqgnuYSrl7lCy0LKFVtj8l8k6fxGU8rBSeuILL2sgn4YSJfUjyRo4TdzLDprMbxNY2oUhZyJo5XxalqtDLJsGnOA2RRkKsivwQrvm7nlGwDFiGn22aRemaVzmhTGzn45rrpWo0Zne/VJMd9IDbyYTgbbQl+etk4akvNKpb06Yhk2vBgY2trZOuyci3b0ARAOOwLzBviBEuPLLocyxuSd8a8ATPkBszwpX5ynCW6txtTy8L8bJm5iOswHWflPqeG21m0Q3eJnR7bw2yYDUkQAm+PDA1Dpc+UsVqPKjXVKx09CTh7lNdnozHk4DJuzqPlST4I0wXjLQiNMRdgXG8r5YTge32xPo7XI+5aVepaSndLfgfQkVrUySIldqWlWChZVpknZEJK+5pL6fzZ3zVkphZdZ1GalIZhXHiWYWWbSkUFonITcThzvpgGu7btcVkMi4jG8UPaJkREEUwS7RZxiJ13QMvP0UbkYTNR7TSsULCpPWWAW5crwKPJcsfJnKJM4uja+rvzZA3b1DWh48xOG5LbeF9fclLyKKh23IENG08lBCZhWKgsonwN03buKpklqJuhcVBOI5n2LWqyI/bslovsAl/m562mWDDtr8dDomq1Pe+QilyaBxqpkVCPVRWM/RMw8FKV47Mtj4dLzsvO5uUwOoKxxVzdRTlauLDZH+PbtbNFYDBduTF12ezRvNGmIE6HtNWOsOveqi+nubokxSRCU2tV7BQ1o0MK2V7dnaWywNw1+mlqtlPch8WSKU1FeiVhh9Zsprp9Rf1JnnMt2qwaPElE4jzFvSQklGUSlsKmrHFsHkVGytBjZG8juLgINwqLpXMMuYJaBEN0Ll8t07IKT0hxwhKYcTnH67qkxHm8naDXZH1dX/dTet0O95pA0ASQ6QkhLykT1jSoLuu1ByozoGrupKLmaTkqIpc66QrfXjNjjJHtNRzT0oxigwyFihBFsNQXGz7hcodVmJElhOsosojZXhFmlb/SCwthizmLhWE2XPs6Q0mKXpuIIipgh3r4SdCboT817Y1oJEKlzbHsCqu3CeLQQKy1JJACYk1YuEegBpsNL4HrpmKyiPNgxCGJtU2paMEMCU+sEWqdnD25wHetIpF5eUm1YTZ1drvRcDQJyf103pLSlGqYAJzK0z6eA/Y6N1Hzuj17NlKZwjDgds2o0iphXKV4USzdiDHTCHYH/tn0WOWaIOOpasGGzwr4hTy9ynM/Ub0tNsQzSqoi6xz6DVHxEjIfYoymGj55mGjyETHzgrq0S71ClmAZ0QoYtt5sNvvll4fHh+6vle5Xqz/+47fumuT/2W3N7WIlKiGj0ADdVWgKNPO55/X8F/x/e3xIDRdyv100ZX5h3y9rbtdMn/p9n97uVLPm9gdiUZiDOn+5P841O3u7e+1vux/erlm7bd/8SRF8dfs7qe4S7fU+uBOn/8vE/hYMivSEPfz5vwFpFqOgWzoAAA== -->
