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
