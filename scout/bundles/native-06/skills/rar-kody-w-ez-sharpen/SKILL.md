---
name: "rar-kody-w-ez-sharpen"
description: "Recursively GROW the fidelity of commons frame recordings using the EZsharpen / dream-catcher pattern: generate in-between detail for a frame, but keep ONLY the generated detail that does not contradict the signed data in the previous or next frame \u2014 the original resolution is preserved and only polished. Use when the user wants to: sharpen / upscale / enhance / interpolate / 'grow' a captured frame or a whole recording (from CommonsShow capture/record), fill motion between sparse frames, or add detail without losing or faking the real signed evidence. ACTIONS: 'sharpen' polishes ONE frame given its previous/current/next frames (entities = {id:{v:[numbers], kind, signed:bool}}); optional host-LLM 'candidates' are filtered the same way. 'grow' EZsharpens EVERY interior frame of a recording (pass 'recording' = a dir of frameNN.state.json + manifest, or inline 'frames'), with optional recursive 'subdivide' to synthesize finer-resolution sub-frames. 'demo' runs a built-in self-test. The dream catcher keeps consistent detail and reports every rejection with its reason; signed records are immutable and never overwritten."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/ez_sharpen_agent", "rar_sha256": "066d314a213177a5f0b8b0fac69652e5190b6980e5a6a6ae0a9b51b41d57420c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["frames", "interpolation", "dream-catcher", "fidelity", "ezsharpen"]}
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

<!-- rci-capsule:v1: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 -->
