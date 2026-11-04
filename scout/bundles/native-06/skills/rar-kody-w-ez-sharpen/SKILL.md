---
name: "rar-kody-w-ez-sharpen"
description: "Recursively GROW the fidelity of commons frame recordings using the EZsharpen / dream-catcher pattern: generate in-between detail for a frame, but keep ONLY the generated detail that does not contradict the signed data in the previous or next frame \u2014 the original resolution is preserved and only polished. Use when the user wants to: sharpen / upscale / enhance / interpolate / 'grow' a captured frame or a whole recording (from CommonsShow capture/record), fill motion between sparse frames, or add detail without losing or faking the real signed evidence. ACTIONS: 'sharpen' polishes ONE frame given its previous/current/next frames (entities = {id:{v:[numbers], kind, signed:bool}}); optional host-LLM 'candidates' are filtered the same way. 'grow' EZsharpens EVERY interior frame of a recording (pass 'recording' = a dir of frameNN.state.json + manifest, or inline 'frames'), with optional recursive 'subdivide' to synthesize finer-resolution sub-frames. 'demo' runs a built-in self-test. The dream catcher keeps consistent detail and reports every rejection with its reason; signed records are immutable and never overwritten."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/ez_sharpen_agent", "rar_sha256": "066d314a213177a5f0b8b0fac69652e5190b6980e5a6a6ae0a9b51b41d57420c", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["frames", "interpolation", "dream-catcher", "fidelity", "ezsharpen"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/ez_sharpen_agent`. The original RAPP
agent is preserved byte-for-byte in `ez_sharpen_agent.py` and in the RCI capsule.

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

EZSharpen — a recursive FRAME GROWER for the commons recordings. It upgrades the fidelity of a
captured frame by GENERATING in-between detail, but only where that detail does NOT contradict the
real signed data in the previous or next frame. The original resolution is never lost — it's only
polished. (The "dream catcher" pattern: the host LLM, or deterministic interpolation, DREAMS
candidate detail; this agent CATCHES only the dreams consistent with the signed evidence and merges
them as an additive layer; contradictions fall through and are discarded.)

THE EZsharpen ALGORITHM (per interior frame F_i, with neighbors F_{i-1}, F_{i+1}):
  1. For every entity present in both neighbors, propose an interpolated state at F_i's time
     (linear tween between the neighbors) — and/or accept host-LLM-proposed candidates.
  2. DREAM CATCHER: keep a candidate ONLY if it (a) stays within the bound implied by the two
     neighbors (no over/undershoot) and (b) does not conflict with any SIGNED record in F_i itself.
     Signed records are immutable ground truth and are never overwritten.
  3. Merge kept candidates into F_i as an additive `dream` layer (marked generated + confidence).
  4. RECURSIVE GROWTH: optionally subdivide — synthesize sub-frames between frames at finer time
     steps, each filtered the same way — growing temporal resolution without contradicting the record.

So in a brainstem this becomes an autonomous frame grower: point it at a recording and it builds
out detail frame by frame, bounded by the neighbors, never inventing anything the data forbids.

Drop-in (BasicAgent), pure stdlib, no core changes, no PII.

Actions:
  sharpen  one frame: given prev/cur/next (+ optional candidates) -> kept dream layer + rejects
  grow     a whole recording: EZsharpen every interior frame (optionally recursive subdivision)
  demo     run a built-in self-test proving consistent detail is kept and contradictions rejected

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "sharpen = polish one frame vs its neighbors; grow = sharpen every interior frame of a recording (recursive frame grower); compete = run MULTIPLE engines that compete to add non-conflicting detail, judged + self-improved over passes (glitches shrink, winners merge); demo = self-test. Default demo.",
      "enum": [
        "sharpen",
        "grow",
        "compete",
        "demo"
      ],
      "type": "string"
    },
    "candidates": {
      "description": "Optional host-LLM-proposed enhancement records for cur: [{id, v:[numbers], kind, note}]. Each is filtered by the dream catcher.",
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "cur": {
      "description": "For sharpen: the frame to polish (same shape). Its signed entities are immutable.",
      "type": "object"
    },
    "frames": {
      "description": "For grow: an inline ordered list of frames [{ts, entities:{...}}] to grow.",
      "items": {
        "type": "object"
      },
      "type": "array"
    },
    "next": {
      "description": "For sharpen: the next frame (same shape).",
      "type": "object"
    },
    "passes": {
      "description": "For compete: how many judge-and-improve rounds to run (engines nudge toward the winner each pass). Default 3.",
      "type": "integer"
    },
    "prev": {
      "description": "For sharpen: the previous frame {ts, entities:{id:{v:[..], kind, signed}}}.",
      "type": "object"
    },
    "recording": {
      "description": "For grow: path to a recording dir (frameNN.state.json + manifest.json from CommonsShow record) to grow instead of inline frames.",
      "type": "string"
    },
    "subdivide": {
      "description": "For grow: synthesize this many interpolated sub-frames between each pair (recursive growth). Default 0 (none).",
      "type": "integer"
    },
    "tolerance": {
      "description": "Slack allowed beyond the neighbor bound before a candidate is judged contradictory. Default 0 (strict).",
      "type": "number"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ez_sharpen_agent.py` and embedded as the fenced Python below (sha256 066d314a213177a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ez_sharpen_agent.py` first:

```bash
python3 ez_sharpen_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ez_sharpen_agent.py   # or on stdin
python3 ez_sharpen_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/ez_sharpen_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/ez_sharpen_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/ez_sharpen_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
EZSharpen — a recursive FRAME GROWER for the commons recordings. It upgrades the fidelity of a
captured frame by GENERATING in-between detail, but only where that detail does NOT contradict the
real signed data in the previous or next frame. The original resolution is never lost — it's only
polished. (The "dream catcher" pattern: the host LLM, or deterministic interpolation, DREAMS
candidate detail; this agent CATCHES only the dreams consistent with the signed evidence and merges
them as an additive layer; contradictions fall through and are discarded.)

THE EZsharpen ALGORITHM (per interior frame F_i, with neighbors F_{i-1}, F_{i+1}):
  1. For every entity present in both neighbors, propose an interpolated state at F_i's time
     (linear tween between the neighbors) — and/or accept host-LLM-proposed candidates.
  2. DREAM CATCHER: keep a candidate ONLY if it (a) stays within the bound implied by the two
     neighbors (no over/undershoot) and (b) does not conflict with any SIGNED record in F_i itself.
     Signed records are immutable ground truth and are never overwritten.
  3. Merge kept candidates into F_i as an additive `dream` layer (marked generated + confidence).
  4. RECURSIVE GROWTH: optionally subdivide — synthesize sub-frames between frames at finer time
     steps, each filtered the same way — growing temporal resolution without contradicting the record.

So in a brainstem this becomes an autonomous frame grower: point it at a recording and it builds
out detail frame by frame, bounded by the neighbors, never inventing anything the data forbids.

Drop-in (BasicAgent), pure stdlib, no core changes, no PII.

Actions:
  sharpen  one frame: given prev/cur/next (+ optional candidates) -> kept dream layer + rejects
  grow     a whole recording: EZsharpen every interior frame (optionally recursive subdivision)
  demo     run a built-in self-test proving consistent detail is kept and contradictions rejected
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/ez_sharpen_agent",
    "version": "1.0.1",
    "display_name": "EZSharpen",
    "author": "kody-w",
    "category": "analysis",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ],
    "description": "Grows in-between detail for recorded commons frames by bounded interpolation, keeping only candidates consistent with signed neighbor frames.",
    "tags": [
        "frames",
        "interpolation",
        "dream-catcher",
        "fidelity",
        "ezsharpen"
    ]
}

import os, json


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


def _num(v):
    return [float(x) for x in v] if isinstance(v, (list, tuple)) else [float(v)]


def _interp(a, b, f):
    return [a[i] + (b[i] - a[i]) * f for i in range(min(len(a), len(b)))]


def _within(v, lo, hi, tol=1e-6):
    return all(lo[i] - tol <= v[i] <= hi[i] + tol for i in range(len(v)))


class EZSharpenAgent(BasicAgent):
    def __init__(self):
        self.name = "EZSharpen"
        self.metadata = {
            "name": self.name,
            "description": (
                "Recursively GROW the fidelity of commons frame recordings using the EZsharpen / dream-catcher "
                "pattern: generate in-between detail for a frame, but keep ONLY the generated detail that does not "
                "contradict the signed data in the previous or next frame — the original resolution is preserved and "
                "only polished. Use when the user wants to: sharpen / upscale / enhance / interpolate / 'grow' a "
                "captured frame or a whole recording (from CommonsShow capture/record), fill motion between sparse "
                "frames, or add detail without losing or faking the real signed evidence. ACTIONS: 'sharpen' polishes "
                "ONE frame given its previous/current/next frames (entities = {id:{v:[numbers], kind, signed:bool}}); "
                "optional host-LLM 'candidates' are filtered the same way. 'grow' EZsharpens EVERY interior frame of "
                "a recording (pass 'recording' = a dir of frameNN.state.json + manifest, or inline 'frames'), with "
                "optional recursive 'subdivide' to synthesize finer-resolution sub-frames. 'demo' runs a built-in "
                "self-test. The dream catcher keeps consistent detail and reports every rejection with its reason; "
                "signed records are immutable and never overwritten."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["sharpen", "grow", "compete", "demo"],
                               "description": "sharpen = polish one frame vs its neighbors; grow = sharpen every interior frame of a recording (recursive frame grower); compete = run MULTIPLE engines that compete to add non-conflicting detail, judged + self-improved over passes (glitches shrink, winners merge); demo = self-test. Default demo."},
                    "passes": {"type": "integer", "description": "For compete: how many judge-and-improve rounds to run (engines nudge toward the winner each pass). Default 3."},
                    "prev": {"type": "object", "description": "For sharpen: the previous frame {ts, entities:{id:{v:[..], kind, signed}}}."},
                    "cur": {"type": "object", "description": "For sharpen: the frame to polish (same shape). Its signed entities are immutable."},
                    "next": {"type": "object", "description": "For sharpen: the next frame (same shape)."},
                    "candidates": {"type": "array", "description": "Optional host-LLM-proposed enhancement records for cur: [{id, v:[numbers], kind, note}]. Each is filtered by the dream catcher.",
                                   "items": {"type": "object"}},
                    "frames": {"type": "array", "description": "For grow: an inline ordered list of frames [{ts, entities:{...}}] to grow.", "items": {"type": "object"}},
                    "recording": {"type": "string", "description": "For grow: path to a recording dir (frameNN.state.json + manifest.json from CommonsShow record) to grow instead of inline frames."},
                    "subdivide": {"type": "integer", "description": "For grow: synthesize this many interpolated sub-frames between each pair (recursive growth). Default 0 (none)."},
                    "tolerance": {"type": "number", "description": "Slack allowed beyond the neighbor bound before a candidate is judged contradictory. Default 0 (strict)."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # ---- the DREAM CATCHER: is this candidate consistent with the neighbors + self signed truth? ----
    def _judge(self, ent_id, cand_v, prev, cur, nxt, tol):
        pe = (prev.get("entities") or {}).get(ent_id)
        ne = (nxt.get("entities") or {}).get(ent_id)
        ce = (cur.get("entities") or {}).get(ent_id)
        # ground truth: if cur already has a SIGNED state for this entity, never override it.
        if ce and ce.get("signed"):
            if cand_v != _num(ce.get("v", cand_v)):
                return False, "contradicts a SIGNED record in the current frame"
            return False, "already signed (authoritative) — nothing to polish"
        # need both neighbors to bound an interpolation.
        if not (pe and ne):
            return False, "no bounding neighbors (entity missing in prev or next)"
        a, b = _num(pe.get("v", [])), _num(ne.get("v", []))
        if len(a) != len(b) or not a:
            return False, "neighbor states not comparable"
        lo = [min(a[i], b[i]) - tol for i in range(len(a))]
        hi = [max(a[i], b[i]) + tol for i in range(len(a))]
        if len(cand_v) != len(a):
            return False, "candidate dimensionality mismatch"
        if not _within(cand_v, lo, hi):
            return False, "outside the bound implied by prev->next (would over/undershoot the record)"
        return True, "consistent with both neighbors; no signed contradiction"

    def _conf(self, prev, nxt, ent_id):
        # confidence shrinks as the neighbors disagree more (bigger gap = more guesswork).
        pe = (prev.get("entities") or {}).get(ent_id); ne = (nxt.get("entities") or {}).get(ent_id)
        try:
            a, b = _num(pe["v"]), _num(ne["v"])
            d = sum((a[i] - b[i]) ** 2 for i in range(len(a))) ** 0.5
            return round(max(0.4, 1.0 / (1.0 + d * 0.05)), 3)
        except Exception:
            return 0.5

    def sharpen(self, prev, cur, nxt, candidates, tol):
        prev = prev or {"entities": {}}; nxt = nxt or {"entities": {}}; cur = cur or {"entities": {}}
        ts = cur.get("ts")
        # time fraction for the interpolation (default midpoint if no ts).
        f = 0.5
        try:
            f = (ts - prev["ts"]) / (nxt["ts"] - prev["ts"])
            f = max(0.0, min(1.0, f))
        except Exception:
            pass
        kept, rejected = [], []
        # 1) host-LLM candidates (if any) — filtered as-is.
        for c in (candidates or []):
            eid = c.get("id"); v = _num(c.get("v", []))
            ok, why = self._judge(eid, v, prev, cur, nxt, tol)
            (kept if ok else rejected).append({"id": eid, "v": v, "kind": c.get("kind", "state"),
                                               "source": "llm", "note": c.get("note", ""),
                                               "generated": True, "confidence": self._conf(prev, nxt, eid),
                                               "reason": why})
        # 2) deterministic interpolation: tween every entity present in both neighbors + absent/unsigned in cur.
        # Only defer to a KEPT llm candidate; if the llm glitched (rejected), interp still gets to try.
        proposed_ids = set((prev.get("entities") or {})) & set((nxt.get("entities") or {}))
        kept_ids = {k["id"] for k in kept}
        for eid in sorted(proposed_ids):
            if eid in kept_ids:
                continue
            a = _num(prev["entities"][eid].get("v", [])); b = _num(nxt["entities"][eid].get("v", []))
            if len(a) != len(b) or not a:
                continue
            v = [round(x, 4) for x in _interp(a, b, f)]
            ok, why = self._judge(eid, v, prev, cur, nxt, tol)
            (kept if ok else rejected).append({"id": eid, "v": v, "kind": prev["entities"][eid].get("kind", "state"),
                                               "source": "interp", "generated": True,
                                               "confidence": self._conf(prev, nxt, eid), "reason": why})
        # 3) merge — additive dream layer; signed/original entities untouched.
        merged = {"ts": ts, "entities": dict(cur.get("entities") or {}),
                  "dream": [k for k in kept]}
        for k in kept:
            if k["id"] not in merged["entities"]:   # never overwrite existing (incl. signed)
                merged["entities"][k["id"]] = {"v": k["v"], "kind": k["kind"], "signed": False, "generated": True}
        return {"kept": kept, "rejected": rejected, "merged": merged,
                "preserved_signed": [eid for eid, e in (cur.get("entities") or {}).items() if e.get("signed")]}

    def grow(self, frames, subdivide, tol):
        out_frames, total_kept, total_rej = [], 0, 0
        n = len(frames)
        for i, cur in enumerate(frames):
            if i == 0 or i == n - 1:
                out_frames.append({"ts": cur.get("ts"), "entities": cur.get("entities", {}), "dream": [], "edge": True})
                continue
            r = self.sharpen(frames[i - 1], cur, frames[i + 1], None, tol)
            total_kept += len(r["kept"]); total_rej += len(r["rejected"])
            out_frames.append(r["merged"])
        # recursive growth: synthesize finer sub-frames between each pair, each consistency-filtered.
        subframes = []
        if subdivide and subdivide > 0:
            for i in range(n - 1):
                a, b = frames[i], frames[i + 1]
                for s in range(1, subdivide + 1):
                    f = s / (subdivide + 1)
                    ts = None
                    try: ts = a["ts"] + (b["ts"] - a["ts"]) * f
                    except Exception: pass
                    sub = {"ts": ts, "entities": {}}
                    r = self.sharpen(a, sub, b, None, tol)
                    sub_merged = r["merged"]; sub_merged["synthetic"] = True; sub_merged["between"] = [i, i + 1]
                    subframes.append(sub_merged)
                    total_kept += len(r["kept"])
        return {"frames": out_frames, "subframes": subframes,
                "stats": {"input_frames": n, "interior_sharpened": max(0, n - 2),
                          "detail_kept": total_kept, "detail_rejected": total_rej,
                          "subframes_grown": len(subframes)}}

    # ---- COMPETING ENGINES: each proposes detail; the dream catcher accepts only non-conflicting
    #      proposals (a conflict = "a glitch in the matrix"); a judge scores them; losers are nudged
    #      toward the winner each pass = recursive automated improvement. Merge all winners = build
    #      out the world frame. -----------------------------------------------------------------------
    def _engine_propose(self, name, a, b, f, aggr):
        if name == "interp":  ff = f
        elif name == "ease":  ff = f * f * (3 - 2 * f)                  # smoothstep
        elif name == "hold":  ff = 0.0 if f < 0.5 else 1.0             # nearest neighbor
        elif name == "extrap": ff = f + aggr                           # overshoot by aggr (glitch-prone)
        else: ff = f
        return [round(x, 4) for x in _interp(a, b, ff)]

    def compete(self, frames, passes, tol):
        engines = {"interp": {"aggr": 0.0}, "ease": {"aggr": 0.0},
                   "hold": {"aggr": 0.0}, "extrap": {"aggr": 0.7}}   # extrap starts glitch-prone; it improves
        board = {e: {"kept": 0, "glitches": 0, "wins": 0, "score": 0.0} for e in engines}
        history, n = [], len(frames)
        final_frames = None
        for p in range(max(1, passes)):
            tally = {e: {"kept": 0, "glitches": 0, "wins": 0} for e in engines}
            glitch_log, built = [], []
            for i, cur in enumerate(frames):
                if i == 0 or i == n - 1:
                    built.append({"ts": cur.get("ts"), "entities": cur.get("entities", {}), "dream": [], "edge": True})
                    continue
                prev, nxt = frames[i - 1], frames[i + 1]
                try:
                    f = max(0.0, min(1.0, (cur["ts"] - prev["ts"]) / (nxt["ts"] - prev["ts"])))
                except Exception:
                    f = 0.5
                merged = {"ts": cur.get("ts"), "entities": dict(cur.get("entities") or {}), "dream": []}
                ids = set((prev.get("entities") or {})) & set((nxt.get("entities") or {}))
                for eid in sorted(ids):
                    ce = (cur.get("entities") or {}).get(eid)
                    if ce and ce.get("signed"):
                        continue  # immutable ground truth — engines don't touch it
                    a = _num(prev["entities"][eid].get("v", [])); b = _num(nxt["entities"][eid].get("v", []))
                    if len(a) != len(b) or not a:
                        continue
                    winners = []  # (engine, v, conf)
                    for ename, cfg in engines.items():
                        v = self._engine_propose(ename, a, b, f, cfg["aggr"])
                        ok, why = self._judge(eid, v, prev, cur, nxt, tol)
                        if ok:
                            tally[ename]["kept"] += 1
                            winners.append((ename, v, self._conf(prev, nxt, eid)))
                        else:
                            tally[ename]["glitches"] += 1
                            glitch_log.append({"frame": i, "entity": eid, "engine": ename, "reason": why})
                    if winners:
                        # the winner is the consistent engine with the best standing score (tie -> confidence).
                        winners.sort(key=lambda w: (board[w[0]]["score"], w[2]), reverse=True)
                        we, wv, wc = winners[0]
                        tally[we]["wins"] += 1
                        merged["entities"][eid] = {"v": wv, "kind": prev["entities"][eid].get("kind", "state"),
                                                   "signed": False, "generated": True, "by": we, "confidence": wc}
                        merged["dream"].append({"id": eid, "v": wv, "by": we, "confidence": wc})
                built.append(merged)
            # JUDGE + accumulate the scoreboard
            for e in engines:
                board[e]["kept"] += tally[e]["kept"]; board[e]["glitches"] += tally[e]["glitches"]
                board[e]["wins"] += tally[e]["wins"]
                board[e]["score"] = board[e]["kept"] * 2 + board[e]["wins"] - board[e]["glitches"]
            ranked = sorted(board.items(), key=lambda kv: kv[1]["score"], reverse=True)
            winner = ranked[0][0]
            # AUTONOMOUS IMPROVEMENT: nudge every engine's aggressiveness toward the winner's (losers
            # that glitch a lot converge toward consistent behavior — glitches shrink each pass).
            target = engines[winner]["aggr"]
            adjustments = {}
            for e in engines:
                if e == winner:
                    continue
                old = engines[e]["aggr"]
                engines[e]["aggr"] = round(old + (target - old) * 0.5, 4)
                if abs(engines[e]["aggr"] - old) > 1e-9:
                    adjustments[e] = {"from": old, "to": engines[e]["aggr"]}
            history.append({"pass": p, "winner": winner,
                            "scoreboard": {e: dict(board[e]) for e in engines},
                            "glitches_this_pass": sum(tally[e]["glitches"] for e in engines),
                            "adjustments": adjustments})
            final_frames = built
        return {"frames": final_frames, "passes": history,
                "winner": history[-1]["winner"] if history else None,
                "engines_final": {e: engines[e]["aggr"] for e in engines},
                "stats": {"input_frames": n,
                          "glitches_first_pass": history[0]["glitches_this_pass"] if history else 0,
                          "glitches_last_pass": history[-1]["glitches_this_pass"] if history else 0}}

    def _load_recording(self, path):
        """Build frames from a CommonsShow record dir: residents' positions per beat = entities."""
        path = os.path.expanduser(path)
        mpath = os.path.join(path, "manifest.json")
        frames = []
        if os.path.exists(mpath):
            man = json.loads(open(mpath).read())
            for b in man.get("beats", []):
                ents = {}
                for r in ((b.get("receipts") or {}).get("residents") or []):
                    pos = r.get("pos") or {}
                    if isinstance(pos, dict) and "x" in pos:
                        ents["res:" + str(r.get("from") or r.get("name"))] = {
                            "v": [pos.get("x", 0), pos.get("y", 0), pos.get("z", 0)], "kind": "resident", "signed": False}
                # signed events at this beat pin authoritative facts (immutable)
                for s in ((b.get("receipts") or {}).get("signed") or []):
                    ents["sig:" + str(s.get("sig8"))] = {"v": [float(s.get("ts") or 0)], "kind": s.get("kind", "event"), "signed": True}
                frames.append({"ts": b.get("t") if b.get("t") is not None else b.get("i"), "entities": ents})
        return frames

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "demo").strip().lower()
        tol = float(kwargs.get("tolerance") or 0.0)

        if action == "sharpen":
            r = self.sharpen(kwargs.get("prev"), kwargs.get("cur"), kwargs.get("next"),
                             kwargs.get("candidates"), tol)
            return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": "sharpen",
                               "status": "success", "kept": r["kept"], "rejected": r["rejected"],
                               "merged_frame": r["merged"], "preserved_signed": r["preserved_signed"],
                               "persona_directive": ("Explain that you POLISHED the frame: list what generated detail "
                                "was kept (consistent with both neighbors) vs rejected (would contradict the record), "
                                "and stress the original signed resolution was preserved, never overwritten — only "
                                "in-between detail was added.")}, indent=2)

        if action == "grow":
            frames = kwargs.get("frames")
            if isinstance(frames, str):
                try: frames = json.loads(frames)
                except Exception: frames = None
            if not frames and kwargs.get("recording"):
                frames = self._load_recording(kwargs["recording"])
            if not frames or len(frames) < 3:
                return json.dumps({"status": "error", "error": "need >=3 frames (inline 'frames' or a 'recording' dir) to grow interior frames."})
            r = self.grow(frames, int(kwargs.get("subdivide") or 0), tol)
            return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": "grow",
                               "status": "success", "stats": r["stats"],
                               "frames": r["frames"], "subframes": r["subframes"],
                               "persona_directive": ("Report the recording grew in fidelity: how many interior frames "
                                "were sharpened, how much detail was kept vs rejected by the dream catcher, and how "
                                "many finer sub-frames were synthesized — all bounded by the signed neighbors so "
                                "nothing contradicts the record. Initial resolution preserved; only polished.")}, indent=2)

        if action == "compete":
            frames = kwargs.get("frames")
            if isinstance(frames, str):
                try: frames = json.loads(frames)
                except Exception: frames = None
            if not frames and kwargs.get("recording"):
                frames = self._load_recording(kwargs["recording"])
            if not frames or len(frames) < 3:
                return json.dumps({"status": "error", "error": "need >=3 frames (inline 'frames' or a 'recording' dir) for engines to compete."})
            r = self.compete(frames, int(kwargs.get("passes") or 3), tol)
            return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": "compete",
                               "status": "success", "winner": r["winner"], "stats": r["stats"],
                               "engines_final": r["engines_final"], "passes": r["passes"], "frames": r["frames"],
                               "persona_directive": ("Narrate the competition: multiple engines proposed detail, the "
                                "dream catcher accepted only the non-conflicting proposals (conflicts = glitches in the "
                                "matrix), a judge scored them, and the losers were nudged toward the winner each pass — "
                                "so glitches shrank from the first pass to the last while the merged frame gained "
                                "non-conflicting resolution. Report the winner, the glitch drop, and that the world's "
                                "established frames were built out without ever contradicting the signed record.")}, indent=2)

        # demo / self-test — prove a consistent tween is kept and a contradiction is rejected.
        prev = {"ts": 0, "entities": {"pip": {"v": [0, 0, 0], "kind": "resident", "signed": False}}}
        cur  = {"ts": 1, "entities": {}}
        nxt  = {"ts": 2, "entities": {"pip": {"v": [10, 0, 0], "kind": "resident", "signed": False}}}
        # an LLM candidate that OVERSHOOTS (teleport past the next frame) must be rejected; an in-bound one kept.
        cands = [{"id": "pip", "v": [99, 0, 0], "kind": "resident", "note": "wild guess"}]
        r1 = self.sharpen(prev, cur, nxt, cands, tol)
        # signed-immutability check: cur has a SIGNED pip; any different candidate must be rejected.
        cur2 = {"ts": 1, "entities": {"pip": {"v": [5, 0, 0], "kind": "resident", "signed": True}}}
        r2 = self.sharpen(prev, cur2, nxt, [{"id": "pip", "v": [5.0001, 0, 0]}], tol)
        interp_kept = any(k["source"] == "interp" and k["id"] == "pip" for k in r1["kept"])
        overshoot_rejected = any(rj["id"] == "pip" and rj["source"] == "llm" for rj in r1["rejected"])
        signed_protected = (len(r2["kept"]) == 0 and "pip" in r2["preserved_signed"])
        ok = interp_kept and overshoot_rejected and signed_protected
        return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": "demo",
                           "status": "success" if ok else "degraded", "self_test_pass": ok,
                           "interp_tween_kept": interp_kept, "overshoot_rejected": overshoot_rejected,
                           "signed_resolution_protected": signed_protected,
                           "example_kept": r1["kept"], "example_rejected": r1["rejected"],
                           "persona_directive": ("Show the user the dream catcher working: a midpoint tween between two "
                            "frames was KEPT (consistent), an overshoot 'dream' was REJECTED, and a signed frame was "
                            "left untouched. EZsharpen grows fidelity only where the record allows.")}, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+28afeiWNYv+FVc8bzIyEtkyCCgUZ13tSIIyKCAMlTmymIGGWUUsvO790H9DxGRlZV3Pd33TXdUrQjF49n77OG3h7PN3z/YbRMV1YcvH5LCG37qP3z64Pm1W8VlExc5eKz4blvVceenw2ynyPqsifxZEHt+GjfDrAhmbpFlRV7PgsrO/Fnlu0XlxXlYz9oa/HNfTlt1ZFeln8/mM6/y7ewn127cyK9mpd00fpV/mYV+7ld248/i/CfHb3ofLPb8xo7TWVBUM/ux/aeZ0zazxPfLmSwJ5n3zl296L+ubyG5mXuHXs7xoAHt5U9le7Db31XUc5tNSu7EBqfujsvK7uGjrGaCT+7fmeZJfWhRGFvcVRRWHcW6n4HR1kbaTZGZxPX2x9qsObGfn3qzIgYTKIo3ryPc+z061P+sj/0GiBetmvZ039awpvszepNGWtWunPnjl55Gdu9OrOAciARtN0pjPfgirov8BCMC1y6atALEHe3eh9FGRvpP57GNQFdmMemhEjYr+5Vvzx5ofPwHVpeksK+5neBF0XdoVYPe+cf3pvrX3Ks4+BgYCpJ4Wd32CDwM7edEsUGb6IlMgRc8HR/g8W1MaJ0vql9kPz5P+8CKYGuiNfp4gBEYF5NjUrxqYA1Or/LyZv6mhnn0ED+ImBq9+nv0ee19+7778M28zx6/qXz/NACfepycHX5yiSP/448d/zIq79QLWoqJufhIEcfaDC3QUA7X7NRBmNZlwCsQM2L5bxcRPbw+fX8T9arH1jD7TivlQSjwd/iH9AEj/ndxLu65nP7w++AHwas+8uJoW3r8hSZ/rBlD/fKmB4KFZZudx4NfNXdpxnsa5P/vhceIfgJYmob+donrxQSDQ1vHiSdA/AEua1UMO2K/jcToPcIOf3hkoWPnTY0NwKs/Pih9mVQvOYwMfAmf/CVh/7afBT0AizeeZBqRwd83Zi2tOXlZP7lPHdQN08GIPk61XfllUQHF+51cDeHfx3TvNO9uTRsFO4Jz/eDGNh2Dqu+DjLGsb2wF2O+2UT1vMCvBXX8UAC/LPAIH8m52VqV9/+PLPXz99iMHrD19+/+CmQMgAkWhLfehmDVy/ActTOw/B83IAhpqD96VfAczIwCPPD2bPdx+nw36a/Y//kfR2FdY/fvklnz3/2A/mf559fHz2OfSbj798eDz+5cOPk4p++TCJELwBagTg+PHHz2nR+9XHH9+2aYoU7BGkhd18vRH4ACAU8IznXvBnGHzt7Ytx8MrCz4DQ0/J++fCOxelPBXafDvH5ueBrIpMPgf2BR7x/Cuzm+4eTd01Pv97+uz9fb/TqPvf9wJF+/IY7H+BMPpvM+7PXZmX98XdwFGBJmQ1OAo5V2WU52WebNnPkM/zLh0/goT2pcPr8frD8DvFvkv/yXhr/id3ZtBi4WFs/v9i6rl/XDzqJX97JVP98ef3r9Phhub738tHb+1//DrnMr0Lf++3uZS9bPJ4993+NEL89HOFl0ffP/xY9YMpAvPZvAFgmh+vuRIFy6FuZ2vdoBiLfULSzgyxwKktvH8F6Yu/LDOBvAwIGWPFdxPzlw38kDtb0dj2bZDf7+A4U7h7vFOCv3I/DyCmq+sdZV89eJDn72Bdt6n0bhl/D0d8jPSEF8Dugzq/j8Su8vKLexOSrdD99Dy8vYf0erf8e8e8zkokIiJAgzANn+OMTwG8Q+Jqf0b/y6imufOfSzxD389e+9ngKtv56MdgwBiEY2DiAko8vwRqI5ccv3x+jqYYvb9vfvRIAk1c/v/fj99/wb+6kXPr+D2D73delIve/42VKrp4rJvV8dYLXQAgO8SfMvW589/rfJsZ+e/3KE9b++dUuv/74V/QBpqYAD59Hm/0fM+xPiP45QL0DDL+qiuoBF8+X09PcBwb2P3/GXtORb4L1IxF7H/qBd/44BedJ49/kDTUwmD9+/DewPq1/VSv43tf4/hr4X4LI/1YUfljvfwuCpw/qFwB8vvlbqPfiDo9vvry74ysQytefvnvw30JU5Z7gvIOqKcsLK39S6Gv182U2Zdggkxu+VfPfRVSQgL4UAxNa3bdr3eg9ztwR9z2gOsOdra+StU93F5y+/vcI33m+Z4zv0sTZg53XlNJ7wUobVAxO0QKQe6X+BN5XzJ/Vxd8kDdw2moT5FhDqd2L+PONykOx/XWq94vk/vimy/j76giK19Bv//wfg/88A8NQ18HOQJvhTzT17GsBf4e9zyb+H4KnIu5vFRBL734q/r/b734LgPs6By79g5cu7X/9b6PyU8W/BlJC9bPDNw0cu/JTeMwN+vrt/9O8Q/r8B4JJd3dtJE7Q8hBc/fCoDko9BcflqHGVVlEX9mgx/un/l72HZ1wWz7U6O6z87QdMueZH/BHAuSAHKTZj3IGWn9T2Fvj+enDAEwcSdeiPPhtTfxXBQiN6AFdqzS+uFAJOBAzz6GdkjHkx7peBo1RPa82kZeFwAo358+jCBmW+DmHNvYTwR/+9xADD/lfU6AhVuMrv3nx4dwgqUG/c9gffdObHv9UecPpTyqJNeWkGgepnizd+MIF9L9S1SfJ69i9uPsz3U+WATxMyifBGN/VxVVKn3w98N2H49dS7uwWf2PmjeOyqzqUv20i271x1vMe6lX/ZVP+Sv4td/zaZ+w2z+1qN50Q0wos6f+oFvRdijOImfycJ0Pvs97Ue38iWB+PxGZOoZTF21Xz48fB++Q++z3TY9AJ+Ucfl81U3//hOsmf5/99up+faENZAxeHcQu4PJa7HLAGP3//jjjzeablvN3tNEvqP5fnV+a75ajf4NDpH/Lov/BUQ4m5qGr02Ph73IZ1pRWVnW1NnHxk8fplZOZn139tee5Y8AZMBDx3+V+T+mHac6csqiAD74d02908REaYKCf4JTxE+G7+eaeH0ca7X6G8cCMdl/PO9jUHWH7R37//j1jVKFfNtGmqzg06SXT5O4Pz14+Ta4/dfTdH96tu/ie/sfuL6bfLnrNJpq4pnK7SR6OwOsT0ceQCgOAn9q6b6T5bfC+fyVcaB/bRzfqxv/X9K2VrVfK/tO8M/lgT4F8hdKwT/DMIw8Ofjj12+l9mjl/3Z3y58ngXxMpvBatNXUDPz1kZs+Fv3y4ZHF/fNB6/nZndw9l0mm6FAhb/2rd2Sm/kYdFUXz22uV8KBWXf5su3sH9/I9I2maPYlVl1dq71pi7yg+BPobwKLmhd7HKQOs0HcMTrvCd2ovlKdN0T/vf70/TgK2ey+6+/XK92e8d4W+YeSdYv9fSsUefeC/zk3+TQ42Zc3gcD4AnPtGIQDo6fB3EwX0fptw/rcpaE5fLJL/ROQpozv8//bS4nwnuGnf7+V23/u7p//xQA9BvwXbdzKfxPWNHv7Tds8W/yvX7y3707vPv+rQIv8rLdp/nxveL8Zer+W+K6annGC64PoC8CyLvbKIX0PsSx+w6f9zufuSyN6r+D190N73Tae0LX/TwuyHOwc/3NcqNE9TGr399Izkz5zhkSlNC/4z5dQPmlmbN0Xr3i8j3y5gp0ZO/e7+dkpV+2jKYd6K8KngB6u+TU8+/PHpw1T9Vu3dG6armP/6r5kYu1VRF4Ce6k6JTwXIxpk/5TJaBNKO+KW8n84aT9c+j3XAUl5ujYpg9q//83H9PPfH356s/nZ3xX89rqZeO77K+nD4Jb9/9PUVrDM0/k8Au36aXkxA869vt/pcDv+6i/SZZisUN12PAv8HZSFgV59uax/MgWAFynHfbZspg3YB3QDkrSAo3s2/m4QFiNfJdJf6sK6iGh642uZfps3+9a9/OXYd/ZI/bqWw2eNOvZ6DBa/szH76CRwAJLJh1PyS+25UzH74/Y8fZv/X7K++dd98onGw6/rtFpZXZWkGqtU286d75klTvu3dhfv7H08xgm2mfB+oIg6mG9V7Xh7nyYSbD5mq7PonFCeApQNZTpd1U5IzZa9x83nGBbNXfl/vAO37JStIV4Ggp/vf4Z4s/ZK/SnLqE9R2E9fB8GlyuTvVfzmVfWcx+80Fy/81E6kDCJ5FOpULgM1H4WaDXD8G4n/V+Nt1OsjZNy9bfJ5J93y7tAGmg0LkSSOwH3qZGgTPr4PNbZCp9b/k062iP4nKflQO2ssoQew+VfrTpPP7eMM9OXvSfrs80QqQ+oECOq+fdjzdbk4edL8UDVuQ7eSu/4+nSQE/n+5BJvk9QeepBe+plbsNvt5tvvbe3l3+MspapO9DGLRyD9PP4vY+fvE2eAH0BJy/vAeX+rtxDfuX/JtJAmeY7WiJVtYaJ+2+n794zFx8BRT262XwfcxCkrVv7nd+yd8PBvznYYtvnPzrMYvHHU5avJVAcQO0P3EE3Ot14OKjdi+dv4JyEHJfJ0wm6ndLBZn9/dYdHMGvsjgHiAx0/jZ1Ach+mm0Vei2qk6xe0tbHif/xcP2HPVFrjWJp9a3gvxP/6tL8fj/2rvJ7GZK4g8W9Bq5/mRqu2WzKn/PpWimeQhUolwe/+sfXZRwA7qkX20RV0YbRIzwAhXhx7YKKHgjhXkJqLP0O8NfCTlY4jRVnH0E8/HaOgfktfg4bvLVymd9+j39CAPJPLyDkj0cDEfk8Y6aW2t247yn58EDfh1t+fQX46aWr8qh7XudZplu8SZbAgABloMRHqLhHrY9TV8+uvo2098rq9WbxxStyb168dFxehzx+em3lvN1W34sL9PNDn0+FKV8eI0T2u6LkPk40NXib2Uf7x4nNob4L5mm3j8ptAo34rQsO0oAn82/S+5gX97g+n/rlj+j+411TH50fv5pKuvcvHrKfKqVn5fSMwIAqENA0SjGloU8i6l8NU4DAPnEIonPzZhnfT1dMW2GfZ+JkeY92wZusHvg40f3GFv91t+t/PWxy9jGzKxAx3iEhdD/Pw7B/vJNYfAZpDHVSVO78QCyN/fI6zwKc5fU260Wj7yZZ3t1IvFjBS5u7eV5avDMb4GYlsLd7C+tPZ3peKEyZz70N408x7WuUeenafN+weenUAL9Si0kt9uw1cj2gwAErHj34md02RV5kE7w9+1rVNCTyZfbIIYFtgRO8nxu6ZyPNvX3kARyYWHgZenuB5pe5t6/vX9552kPHcd5NTnnfc3jcsNwBaYJeECqc2Kvvh9gCF5lGfz5u7Dp27xM0IBct2+nmp/HS2AEbTt1y8B7E5Tyckh7w4MBx96+vHzh0R4QXhLn3M55DBo+Zrgnkp1muxxzXR+htkunN2H6c/fQ/Hwb4QOyHbUHPrkA9EbhfoN4HdL4ddPvyDuAeiPQNrn18Z2tvAfRpdTX45F5u3lts91qxzf90LurebHveVn0zBvW+2/YNSL+UKNNoUuz6ID/48CVv0/TTh6mefD/BNA0r2RPDgPl6mnGaEMyvpm7H9O5Rdk6vvp7JfDn6z8+rsDcNTDeF0/zVq3384yHFn2d/Ka5vx9neRPbejn/8x8s1CthvEpl4EjTuINBvFy1TavCyZsq1PO+7JvhLVnF5dKOhh7QBsk59zUedP3vcDsw+vm8vgzT107OpWz8iJ+DnrsGf3w+ybf3ABhX9/ZP7LFneZh++/PNFZuDJdBjwz5PN+8BrVoBq8kMzlJN2pgGvPJyqnTdr/V4H8rcjhm/R5znKOSWXr2A9pWtApl9m//w99j7N/mSGcWrd/fErqNUmJIvrNzD7swvf6WQxgKA7Y0++C2cyu4nv54PpCmS4n6Otvj/AFM2fQvnyNic0ae1pVB/vCAqWlADUQU5Zv+YwLwOZX0WgiaXvOHkA958Tn/Tw5ZEg3C/0gJzu570PKr3MTdZAYM2E70+aX37//PnzH3/8+jJg8b8miAmP/oYk3k0BfyWEPzvhw1T/fNOnib2bE7gb/U/ArF4MfnYP2/VL1fPxxZPudzV/dVXz45upY+8Ymxw79Ks7ZwCF/8ZhXzPyx4G/kfZz4Pbz529mbf/4448/FccriPyVzkFOHt3h4R3mTMOyH/9yVPbx/rsJ5+co2buJm9fC92lYz9GbD3/i4a95yF+x+y43uUf8t4mP16z2+5TlqajpVG9oOu3XRO9UB0/5Yv6Vab3T4Ovg6PfcqantJo9GzQQR/lA8L/xekP+ZsT7r+PepLjjBE3vf4hYok79iapKQ27xn6wFXH/646/jaggrZe4znfu8RQCaP+dvfP4DIZk85yDO2PTs+YHllVz/VU2E8tV4BFfD+0eAAn/27XtBzGXiG4gRYBxOEhyELG0UwhCRtPICdpQODqp9YETjq48gKdojVEvZxmwD/82F75eCIs0A8nFygsAv2e3TAf5uK6Hgi7bhwgBArZBn4/spBUYyAlz4cYCuCDGzCx1DfW8Iw7Lx9dXKK53keTP7xcL1HW+oexR/H+v2DQyzASnZRc+vHH2oOIZ6PHZyBZ+cGvoq31wWx1ms1accaP/GMj+2W+nU1NK2qNnyzP1P9jqdphQmTfk3F/BWSzofkCJkaya/sFbmJwqUq7SBL7q5kqvnMMRcLwifxlX/w/ZiBmiaYw8IckXXnclud2QJr+6ZfDldPKWNHERgNlvG12uuwiY/o+bZniIxyYKJGraElYvR0Y0RtvmrFa6664zmQsGM9n6PGNR7jc5EOyLHpL+qFSBiUWZA3kPjzWWxsdPqMK71xozoUj9U8v57po7faIIcE2552Z7wVIwKRBqXCCGeTMuIWcva5R5Hby2mkMtOTjqsdg7gsSUgLyIjrIJozC+gYEUQeGCSGBcz6NgYSQ0LUmoIhTZDnq2VHGUofaCJ/SU/jWe6TkVFPxMlar6K4JBcWqYgWUZCDTfruHBV3VSTcrl0bYksH9w4pzEFqOCqmIFzDPX+R+k5ZB/P9eA2Kg3Qchr1jIEMaBDyWGAsIOUpDIV1Ptz0pEhS0WusKfHMH24tk11lplLLdWIIFbcWyxW6jr1LIFltchH5O5b1jSXRomNoYSnM8Lp0rD9XLbYDGxEG8qPRxdT1tSbVytBOTA8/zzUUgjmd7UyV2hGc7B2W30mkoUDY9RGfgCHUArZty5xhHoaRkLsIWPssg1ZFYXFWf3SUhe3JuJp7gB9khOxlqLnhK20JmVvZ2U8Yn0TVU5cZcqoLQ4SMJuVfDta6pOOZHbZTTTVtE2LrABRhfznGpM1tuSVrZqZSt80UJAlUb/OWy92LpsF3ENKsG3HyJzP0FeSF5DFqermbZkWhKLlXqeoquxnF3NW4Y5Dvbq1FifsCSMNyoEK6m21Omhgxdq66nBHSjynV3dvOds8lku6PCMXadSBBLY19mhblbnoQDn6pZOKqmhF85s1r5JDw/aMMYGBakdWrmL/pxs6KIfOHiCUNDW8bFQwUuGe4Aj1umopRzYrjUFnINBFaYnJHmsBqxEVaXhRnsi6Y1/Shhgf7WjF0yuwZnB22/FTsZNjf8Mo8tftcgO9E7AaNDsmHsY0wV00t9IEXqVAyYkCm4po1rF/EXTcJkhubKfcWsdE80TkRJZOfLIhKVAaUO67nWisHKjK7lClrOl1Qfo7UEs/VZUdrwYK9TzY6bdXQD6OcbZdavjNteWrAbNi0UsqzNtXIlGQKCHABefn5ecidJXHkWuqGUAo2HtSRRBpFmp+2WLYLbnjq6rCKKpeBFTeJ3+EIjV3TILLDd6bhUR3OjZ7ebSXLLCD1WId/TkN4gUsupa/yyl2pmr1zMgsIaLFjN7YSY27IPIoYEYa6RooGBYaujkCDxTudp7uZvgtHn5IQPWdrGYHSnWp1W7/3Cr7RuufANBW27Zu/FJ5II9Y2wUSWqLGg66ft+wxfigQZusq1wnkmyHcekUkmutfJGe+quvZoR77FLjDoUHgA2gzaTzXVsowwZbsng2a2vcfwioCl6s5cUgD1WxsCqlXqYzNhMs90Hemxf+lQ4uVVVX526N6SNuC/OhBuQ0Ha42snWVNbsNXT5000lVX9biqmrZbaAmoqkLU973z3E3sarazjN8NPR74lC3rOpRKfDpTeSbYWpXsnB/CiJW90knEN1Rp1uhNE5kq9PXaydaW3jyHxFwq56JrjhNDB5COfDfDTpS7bcWinU8XBmBQS3ERlkOyS0n0IX3uGafFg3ES3ErJjmSzUGZYW97gjeC9JDUVz2+dEt5xtehcZNajpkApvh4EOXiCEJ4sBiZA8ZZ9SEKM0Lgn6Bb9xTWp2H0tnWrtLwyzSzkRjlD0V5W3ftdTjqKkPMrfPJOu3t5Hy99q2dF0s+lLgze5RKpjlsl2FizjdU0+bBZTiu42LYcl1SHfe8v1nV9dhcTV11qPnGxFYdOVw3+zV/zljfWtESMaKa0qK6fxMTl6KskdJQdUnQumoqfGIe0EJUYiZcrFiVuKDaxTnOl7Z87Gr8uPRgJ1IR4lbyBnCMvBOPO3zYaPAZjVJ3UI5iMbLlvCEwiTpw+FlonYVY7yp4o+cJLB5BEmweLrqmJMKi5SiUvZkwFwXd9kZy/bW77eDe7bGjyMlCejBPpJ+wF/oCrWmrXMs7Z+6lnF4KrTae5yfzpF02licnae2fNRlQtqNVbZLJDr0mrSzZQK/DulxYfnU9O6Wen/TSUXaLuc0ugjGSWra6iT2EHfqNItfqTcvW+4YUJZZyKNhKLhdt27Bnlwl3NEdaWruUNq1CKYp0dbTNkYeuvOQZ/HAYxTUZJeQB2i+wQ8KOhecrc1DEb9AEl5KhYU1RKU6lV0GJkcq1sAyjEBflhU6a6+vxkhAas4eSzVx2hZ20yIhj1a0zLhhqu8FyDEdP6zlKHZWBNSJGvl3kjN9b1C5A8J3E1zvTuB02OklE5fXoh6ap7HY7fOSdpW9iuwO5odlrsVk63VBU1p5DzFS+9Kya0kh+hFCxVrDjVrSRgC1E+5ptTwjXE8sI21pHpg3PY3BEL7Ez2KazqtFwCVGoFIdlIc3HBK4Oq7DR5zZ+UwiQiETZmC9OcxvsqEmlQ0II02+3Q7eL90HMzYPdqhPglXEwFnPVkvFtvlrGS2l/HpK8Q7huz11Xt3WfkFIisKtsnXdcV6SevceLJmtIm4+8xiFyRW/oeB3VxWbLCtjC6IvCkFhj10t9O4z7Ug/MNnC1SFn3V40rr4lwNedrheSXsuomHEKZK244UtF8ZV2R5Ulq19m1F+Bqx1JncksdocNIRg3eXLMQt+3I77SiVCtP1TawP5p7gp9D10omVuxpwS19rmrH6JBh6uDC0JanB+WEtqJyW7a4TyzZct0FGnURxwZhL0Nw5uDRCyzIK7jb1h2FgsxhVksz3UNUqGTMlbY4jcs2ghGj7ZxVYTSGuxXT3pPsFGGkGx2YPOktLoFh6l3elXvNuVyoDZrXW7iF/G0rcCO/hupivsEJo8m2/k4Obd6CEV5xkctg5crAYAZUrhJ71/NwCkfy+SQsoVMQLJQKyhOFom6k3sIevPJO/io+Ls4gehGW1BwIG40U3EZRsQwXBot0qtGWi6t7OZ0KvU1PBuIrcIYVMSuVFUVtWGXolToy+hNcnRhNGA+hUnr06rQxklNCjP2wh8WMjDbtWqZafzffkGjv5Z2SQ+mRyAUVUcqDbOvatVbwltzwWrsD+cwiCWV7xZN2WDMdYcWSuklrLj1vQ2cDx0ovAoTjjtCZ1/DT0qAWhUzJc7zYxmWcZUyODmEsEE24DGx+tUC2jm4XmlztR1x1LzfaJiDGY3zNzQLAtVyuR+l6zIb0INMKWtEJyCFS2jnC19yUCuK4V4revTCt2Buhw7C8uraw0vfcqEuyvjPOGQmSpFuQn0cUqebZzVnFRhOcSdfAr/kuR0UqEffJkQcpILNGjH2y4NptYvALd3OKa3tVzjt/67NeshmyQ5ND+w2OScxuZVqCiGRd1zJ6e8tpZGlrtoCgTHAkSj0WJWwRt9lWptkL5BsdEZGgtBh3XYkUCxlb66FFrhY1vbxQcdxryM7Yjcl8NabLVQsCOH+0LviBYcQTV0g6tNwZAYywq6ba6WwnQbR1aTjoXG900/UxvdHP/M6+gNRCcsjlvh5RkmlB8O0bVV+d4PwgbspEcBcYnq3tPsq55lB3h8rnF0xIXikjVq7NsUaRSLyVnVLn53PV21DDwyD51AyZ5g+XEzkyruDVssa5ESzHSKFqjJXJTsxtIUQOS1mUQNafHuFMPpW2qWmc7x/TTdNed9JSYYvd1lW6sDOZk+kfaG7USFIBaV/mZ7TFL1FVTeNd0NaQiZ1OtR/fbugit3dXkAail8rfp4NXX2rOzZmGkchY4qD5YQtB7XiBEJECeU+ppf3OP+920gak1pR3Q1BFg4WIPxm4DTILXHZBJndbKAoQJavzeraT1pdzPUSDFJ62Zjo2eFSDEpXgs2SxCP1tVB7SvY5hC1szt7kAOOsqqcEJOGQZf7fhHa+Hbl2tJLy0Ja55KJUjzsnmPCbLkmA81zTZc6Fbi9s1u1ERp90g6sxs+E0MSl1lG6dndY4l3LDQW8bcy1AVKFc38K/n1E4g63gRbHHT6kGIHrxKFW5+NXracV7dIvfIbd1jUjl1G47Hs24qJkYJqeQ5fMb1ey7rMypwMgrNBoNb7mWrZQ0k9tRitclCu0rDRUfkdjVy0tXoD5vjerdxRZXrzWPA84NsV6BwZSmGIIlOuzLbuuWyc7YqLMeV3K6T6z68uAbtj5WIgroeq08si1Rtv9727OVwTJDlTaephKI5rC81KtiZKHG9UhBJzI3ADsVdt1Ug2df069bZ1BooOXB8TA87MaxD0ye9yrX87hIsDz6WZw5djGmyM/sbKL20RBxtqcDWm0MoLy2K0tvlGj8l9s1u7HnmkWeOM25pYm5IkItQpCknZ/3QwLAZt27hUxumwteN3SAUANZ6J8GRFqvkES68quQXBp0NRK7NRb4PRf3a0ast1+ySsl8sE+Osc5EXsb7W4oK5EvcZUpceY8fXuUCwDE8Whwo6GfAQZIKYFnVyi88yL1H6SoEKp4L7pdwIZklngBN2hzlQquNIzO6Q4/pajdhyN3r+rQ7EPY4WBWPu1psePpCXrpawYs0lnLvBx0trNzRbbKTlhtkFS3RkMFZjLmxIHMjm4CxqRysZ5xxXiSEFJyKlz258vBA5XHT7LKkPNsiZQkvd1ywoKEEKVJTRmT3nXdKdrcV1WefsqR7HA2OHF31+RejkvLDLQ8xfFa6VSf3EiMVNXp3m+SmWb7g69/oh7ywTThPiHGwCsa42l2jF6Yh/tpn98qqu+pRiBCTZtdJOsYrOWKdzpVe2aIQOc87bKZFVbzcoWrGLXeGbKa+nykY97c+ppV610tjRFh0abV9dkEZnjSt3Q+Jhu9UrUovxatzLh0IqBWRrSeslXRCJH6lZ6wox5GKBOacEUAsjN9Ip6atOIXvtsAmwkIERdJGgkHi0Lc9U8T7iBzYpY6vbOA6ykUK0lK77E42SnmZk3ZpJ0BPm2q6HhfVZwPATjqxcCsbKXAFVUGraaK1AamHJo2BTrLjQxYWnZM55v9nQdcI67TLVfdOy0rwyYzzBDsiOqdZ+0p5rg5lvG8tkBJCrGecBBAeU32cb6+wzF2EPEoszYymsgKpVRPP7g3JqKCU8M1ttCdkcpKvXHvfFeHTOLYOzO2MjODY96iyN7UDRN1oudjQFnA9uBAvoN+k2aXB8XgYbstsZCx25HO01kaJ40XeaIKtKsIcMlhKrgtfr4uroBYCw4Hp2HYlXArYrg2ZIuIIMhUCbw8GKUZQ5Ecnpug0qNLmk22a5a0TCC/xLUh/bFIHPcKTfevGMWrZezTVsh5jHBSupprTRBp0ZPMmpQLbFhuFh1c1PiCZx/Jycp56aHbX1ladZUc2J81VnOZZIuv1N74drQfVuHdgQnrImifUXK91vz+1VshnZ2SQwstBDFVaEdOmRa5jngKhrY75voGupAJxcqOvFMXRF5ZAMS8PWdychXYSy4WvVbkGNY71eck0V3XDLco56soJtb0wg7nreL/cZJze7zD1xm932ePL8q+rOOSVVSio+wAdlf1N22vKy0leZ6l+2jskc+nTYefJZS7EFGtaC7JXViqyvyBnxSdtWeNYf0Ew0F0G+WV9bkozkglDTFj6xfrgpYXrbqQrArgCqw81ViGQPl0WdQxg60/daB49Zj3qrKMZR1jrk0KVE5qonsPpRRM+LPbxB1GFJbS6OSPfmqktXqn5Vd7G+qWQEX7mV07RQXc69NekA0LiurzuZO2fqrTGJULQq7bw46rqgx7EZ1dK6xueHObIARoyVwcI/QrGJGfG1RqVLtLPs+QaRODIJdDoMgSJyJTpYYrwmVieKy0mawtsF6kL7MsDNIUNR7oxnetugeXvrCpNf5vAN2cV4UA3RuF2JtA6q6XSRok69N43KbW22LHwRvaEMBVUEWW5M52SmxwrU+sHJqJbEcbESdktv0VTnPnd6D3N1KVpzYANNPRjOSSD6MzavKCdYzbclX5t+FdBnJJnzN6paHiiL9In9ogQByDDyqxpYVntBTSV3rJpAUjI5OsxSt49Diu18YcvkA5RzjrvbH0Qmo69l0rH4sV0z/bHy6S6D64SDa5Vx3LPuBd1YreLWlwbdyYSLaoLkV2quCilHFCjYLUps12vgzKFyYAo8qyF/DasZhHnEhiTHdVygCkqmNqgHjACKaJdA5MW5Pkme6DkIJW/5Xrso220tX1JmLBGvOGzhc9vGVrCLvJ3HC+NCpjZxvDpqB5XNaUe6uleZNUo/vJWIe9yottcrOBPDJFHo/rER8xXC4EeqXNBlSnm4uOk4Tj6N2xNEKpDSsJaF76gzxyv6Kk5xertJTEqyb5mwywxa0vYbMy3xnSF1dMmHQX9dpzhvJmklUOgZG+1ry2G+F0WRE5x2ZHGkm4V1NVrS1JErLHGL+UmwtaMWQ7eii1G3g6y0PmRVaC3TbnXmzKwhuGtn8Hl5VPdALVnqjRe8rouat7mgRueNNtYCtjt2W13Zk35y7uj+Kp0R8rLpSmPNyhXBk5ahBVy76s1LhEgQBJseku0ZuxzZuNmp+GqvlD6DdktnoeQJnOGgvk3zcR2dUGcdbUmejk77RHdiTKgVh8YCQjdjrqTbmIswD2S161ykWeWMVqpeLZUFol12XcvaElIz7Vi4+6bdLPtoFcEoIWzPGEH1SukM7LnpnOimSPmeZfU1UqYY0p0niGi2qsCDAHtqQI4eNJW0kZgm02+HW7w6lbuB8opUXKxla6RWwta16JS/EL2khtebgjVJovB2Z27iFbN2pSai2AFBfOZmrZFlQaPqxcuzVNcDKtpaaHa8pWvmuDYWAsqIy5XnVEMLlLeoDyw8x1fStoScdlyu5CpPTG7p0iPR36RAgThWzo70iCGIgXmRcs4Tjt2FjhEfxBPfNBKH7zgVmYuhRkjsTSQ2goQWW6kDKFmjh6WJ8vGIL7GEN5oY5BrZUK0XqXBdq2W/zToRpMxQewPJgqy3VHFpUsulOGcOwVDN+3sZvqioF7oBVEGBQe7HPV8zt6hYny+kcWn2/pyEF4GJNspWdlgxbdHWtQ6CwIcUSecjlZ1RMZeuvSAeyYOwUsmsLQQBX2guQhQOjx8rur7kUm2zqj2KFlMsAog7xs6VWV7SQdlsDB5BNOsWryMSStB1x+XubewlkSolEm6yXjHZeX8mC5xT2CuRNBK+Cy8GJgvqoJ0Uq1oumvq2QlM4FItzGB1IZFPK9jhohNaCQskrbFcUoqLVYJzjTYheH4z8xKuI6zXUbmti6GW9FHFi6XZIViYJeVMDTERPo7W65CymuMQRVpciXS/GYmu06R6DQUbVdbDEBLZiW5dxYCXNiNmi2Q4nKdAXtbWzrFyGhmN/ZSrvVCjKEd5fCCXOJRbum2uoUZultYkCA7kI0PGyJ+uDqVwiqJTKMG1uqMWsPPHG4qhGItY8PwubBp5vZRJRGs/GRZWE4qUHUlmsJR0pANaAHNhYEOy6xh264X13uDjJknBOrewUndtc2GULClkGPmjNPGT5tkatdmdSZCfpi6sozRuAfJDV2KFjojnl0kVihkR+2chBKrsNpUqOTdSQRs+HAZOpMenreWmvBrj3nBVjbcfusoH1Io/EU72tz4WbNVGWpLyzd7IuCTukGk61bIcnUcTMDCOw2tHnZV0Ot3JMyM5H4j405wuJXhVYf9zHESE3jaYKW3uwQ4VPM1zeYZlJoF6w2G45wSeP26t9UvYFuibXbNn7V264Entmj3M0s0pVvlZz7YTaC6tm66OA9tlBzDHl6LCh0KB6hqu75QFksVyOeSQ1Fsxg61rM6pe27RiECqkRE0DpPHIC7m6GIrqRzALbGE6Et9uuo1WMoYdDuMSEkbrm+r7cnfS8pmDHcsw1yYJyUSNFilshBqL4WOfggbteOCy25MZQv+zDnhdjaJ73S1SzqiO20Ml9udqF3MYoi0oUVxfJOWzTXa3n84sfcgfPOJCawpxZHohApIWVUwddjmBxFkUSU8kpdltGS2h73JxNWamgzMcSyTqDyr3Yc2y1Y2pIrs7CGTq3usCvOsIWTjm5jw9So6p6jS8al6i8CFk6ghVU/hnLrrHEXTpU6JQgZAxRNikLswXd8DCMOMydgqwhx8KLLDvJEu3BwnDVCNggaviA3IKcuS1Bfhup1m0JGSm59A9VtDoMREkGWoacjYHrOsa5pu5mrxyKpLNRk7lyYeWb6krOTKY9pexmV2TSOHddxFpLKB+hW8rddO5CcmmDQbQD31wcSK9vm/G0OyNhhSyQI7L10LoqXTkg4PHA4QbO0ydhC2lbg8nCfbzxs3iFpa0M6wpTniN5wejQDqCGesRN2nSEPmct9+Y1cn7blmhHnzIMVmpRJP30eMaQHXY6efn8fIgo4YyoWqIcyMpiu6xnnGWhSoaAlftkhUBMRtHDkRv5UyECLFoFfCSTIcE7ZoivCaRDoSyTfJHnV+UIXYz1tlE3eFGT+/R6xKUdsYTMde3F7OVcBXYXOSo2gNTKS7IMiTG/NkczGzIo0491RgwchqnyZr8d03pJEpGuqjJneA6tH/x6u7LnBGZLJ1lsYn21whzlPGh7ERm4YTleaUnQS2udQSKJ7VFN97Z1eMswffAqmzjfQr5zN7VhbSpxI9Rxfk62oSziXaKYiDJqiQRCStHDILTQ6dkfE36HUaLH1UlZL9w9pojrnqZq3VgadKmQ2TxGxi2Nn5PDhcQXvkzltOwiuW5lrLABBtGfbgJjrI9Ce3BuFNpqGOcwlcB1ZjLPxqy94M2C4vfOMV+vdpZKtIq3TgN9uHhZ0x4wpQZ2lR3Vm7wLbU81L6bdsxqo3rEtKNEGVmfhiLrJXK/7KmZ7YdkO84PulJcN5QeAQX4lukjtdlmj9qbeShzAAcvgteywzaClVjn0ejEKxR7LF5sblVdXwuqtkkyL+UI8wHnjdawgdcR2HpjwfqVWCLtok4isi9sWAUXyOL+t0Vo7unRVkjuhELMdA51w27LUhO+EyL9oXLuvIrdcLdFCNVkZ0qFj0YlIlS5XPLJTmKYotR19Y6jeyhUfmUtBf0rr1KOZzMqAoTOulSBGTCnLnq84nkd0+IyY6XkYyWt/prcn6kDqWHaJwJIgCs4uekJU4ihdDEU/psElC5EB3ZHNyBs+nbexwSZp52dau+xp2RQqSAtBIrtesb0vn5rABqAgJuI5mTdpk8q+FfEBVGjE0lz1NhZIvHuuDELHghClsDFzVwt944zYNq47m9PGHmLmINWL44NgFE2mGJIV2uTS2EMDHYeN0yr2AQTTeTnwBy6GeC6EbguRQG6wHzg4GhykWsiFi1zXynAYFtJuodXg2+SAGFqHakWV+/i6d/XtwDXO1bt6yKlfnu3t6BVKiwejaCYbg6aCiFzJJ6JcQILuUkJ+PLotNUcXS4Osia7TyGWzXWoovtkm64V7WZk1mu+Crd+6Ecx4YevVB9kIF6A4q7OVxe71CvM2qnHyRxB4ltRwFuW27QV5UW7n/jl1CgZxT37u23EQDqV/WhERCjkpr4fQTpauius55q2uTwcyQVzLGuzgRpCub6vBJr8I9lzv6hWpiibJbPbwyin4ArtsFBDIcTqwmGrZE8qqOHUEGUutqR6iHasZJY479q6ymaOaXU7dib/itVUVPtIQfBjDSIudqpVRXdQA1BmRqh36XlNEiFKLwN2Gp3I5QLKRehjFqO3YbMk0vjnQPtR1N6gcvZNFitevSy9ksyq36Aixi9A1chek5WIw3urhAivGwrb4PIwgfn+Q0Y1O+5sjH6C4sarzELL3FbIUQ9xbqmbIiO5liV3NyGLObpBpXs1Q2oJe9KACbOMRxlk9EVSY1tXLRkTji+llNtTjIo8YQZHaaUMKvaYX18bXD5YwDg7iQ1IlIUVKJDVqnzUXFrRDlF4NEy3HjB/Ka2nwN6P3ieEqDVqzKfNsUQpzZYnNAzss48WBYMqAJneOteXLrF3WGSapFts7EjIut/bGNoi8t5zIsq6CJh4MOMolSzv5qUSe2UArxs2Iawdf6ve3M8Q1rb+IT3Ln9xHGlYnhovy14WMmcgahhS8iog1FHYpUo8PCbQ1DeFE1UA3PkcJaL2/heD3FCQGha7mnWy8cVD09oVtWoIKB5EbdTyxZDBfktmalgTCUbd/RhyAScZS4QBw5HB3+EixKB6Sj9SVBNueCkuLqdlvRiz0q1ylCY0RJiyd6gYVYdcX7WvQQI02Ns69f8eo01yXRod2lrPRStWsFSJNdPfCieH85g1rVkldaExq2T9gmCkHAwEdcJ7oLqOMjUHJ6u623OjbRsEf2oQNT3EDMAw/pTlu0uhjBrj50yJEsiIPBmChAVYESLL728SQR8b3AXOD6Ykcm1hj6KVfwFrNRKT8zeY+creulIsx8A2RrMwPEnE8LWWDhZVuRA/jrCp2yhTvC1oJBBIWgcZ498kw02l2Ik6xLetS5n+fc4rTe85bHziW31BoQ01shTfyIwcommOsVeTxo1unEB1RywTGhHYVcRogzvTI8Hj1e2gpVMq2Xu2vOjHR6c47jBvOWJ6IhIjhUZPiGzY/QJba1ZD8HdXhq4ItzF8+xs1UxRhnkyKUWEoOvUxUioiCIu9UhcrKAQAIsWvj7I2kEXkXyu6Yk9948PF48aAWY2JFdhZY60yeBehTHFcP6Jlcf9LLt4xW6OBK1uKoKrkNOziLotvPbibgleRyftvM6hWHD6pVLvCNPMU6YSsfQUcCoGn9IKlnPJcyWkbOOOSzXETJa7fBwVTQcJCTKAqU6AzqGSwkfrih05JrcvM3rcuMsxkXHBRF7NXsqlMyGGzwMbS4nbAck2x514UjGULGkA0lqFpDYHyO+TQO1tqglefIFdFUF61u/NYSoKVV17FJ5bCNfUEYl321vS0MwxdO5XqJbmrxwITEXtsvS2e3KuQIdotbbHkTdNhOuPURIhx+6aFs7xjywIBKD/CEl/LmMIWQQlI1yayTHujD0abexyKsXWQdXrpCroeHLYRWsU8w1UGyF3BL14paScc7d9TzsVCK7KuiuXq/XP//84dOH6cehz59z/MkPjaf50P/HxlQfE6VFB+jdZ4H/+aHybe/LndaXPyP+66cPlRsD0o/Z2jptw+eI6mOy9id//Ont9xD18PgZbpE39/H4x09VQG04/fd3Xyb4P3346geS068m3v+HvO8CefzIdPrNxfiyO+Dk/rvv+8wv4OYz8uGP/xtwUr/PdFwAAA== -->
