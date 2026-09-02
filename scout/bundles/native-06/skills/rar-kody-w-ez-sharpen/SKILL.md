---
name: "rar-kody-w-ez-sharpen"
description: "Recursively GROW the fidelity of commons frame recordings using the EZsharpen / dream-catcher pattern: generate in-between detail for a frame, but keep ONLY the generated detail that does not contradict the signed data in the previous or next frame \u2014 the original resolution is preserved and only polished. Use when the user wants to: sharpen / upscale / enhance / interpolate / 'grow' a captured frame or a whole recording (from CommonsShow capture/record), fill motion between sparse frames, or add detail without losing or faking the real signed evidence. ACTIONS: 'sharpen' polishes ONE frame given its previous/current/next frames (entities = {id:{v:[numbers], kind, signed:bool}}); optional host-LLM 'candidates' are filtered the same way. 'grow' EZsharpens EVERY interior frame of a recording (pass 'recording' = a dir of frameNN.state.json + manifest, or inline 'frames'), with optional recursive 'subdivide' to synthesize finer-resolution sub-frames. 'demo' runs a built-in self-test. The dream catcher keeps consistent detail and reports every rejection with its reason; signed records are immutable and never overwritten."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/ez_sharpen_agent", "rar_sha256": "ae232a01c0cee6bf5109635803b5cf99ba215201856d4c830b3b11ae972992e6", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ez_sharpen_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/ez-sharpen:658a08cba777507f3d5098cc9b6a881aa5ea213c8ca4eac9c70f0055491160e9", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["frames", "interpolation", "dream-catcher", "fidelity", "ezsharpen"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/ez_sharpen_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ez_sharpen_agent.py` is
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
