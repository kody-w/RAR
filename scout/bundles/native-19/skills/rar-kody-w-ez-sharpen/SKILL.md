---
name: "rar-kody-w-ez-sharpen"
description: "Recursively GROW the fidelity of commons frame recordings using the EZsharpen / dream-catcher pattern: generate in-between detail for a frame, but keep ONLY the generated detail that does not contradict the signed data in the previous or next frame \u2014 the original resolution is preserved and only polished. Use when the user wants to: sharpen / upscale / enhance / interpolate / 'grow' a captured frame or a whole recording (from CommonsShow capture/record), fill motion between sparse frames, or add detail without losing or faking the real signed evidence. ACTIONS: 'sharpen' polishes ONE frame given its previous/current/next frames (entities = {id:{v:[numbers], kind, signed:bool}}); optional host-LLM 'candidates' are filtered the same way. 'grow' EZsharpens EVERY interior frame of a recording (pass 'recording' = a dir of frameNN.state.json + manifest, or inline 'frames'), with optional recursive 'subdivide' to synthesize finer-resolution sub-frames. 'demo' runs a built-in self-test. The dream catcher keeps consistent detail and reports every rejection with its reason; signed records are immutable and never overwritten."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/ez_sharpen_agent", "rar_sha256": "ae232a01c0cee6bf5109635803b5cf99ba215201856d4c830b3b11ae972992e6", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["frames", "interpolation", "dream-catcher", "fidelity", "ezsharpen"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ez_sharpen_agent.py` and embedded as the fenced Python below (sha256 ae232a01c0cee6bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ez_sharpen_agent.py` first:

```bash
python3 ez_sharpen_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ez_sharpen_agent.py   # or on stdin
python3 ez_sharpen_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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

<!-- rci-capsule:v1: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 -->
