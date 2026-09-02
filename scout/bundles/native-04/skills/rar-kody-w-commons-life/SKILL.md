---
name: "rar-kody-w-commons-life"
description: "Record, GROW, and PLAY the life of the commons as a digital organism, cradle to grave. The commons is a living world whose residents (each a signing rappid) are born, wander, play, bond, and persist; this agent records its life as frozen frames (full signed save-states at a chosen frame resolution), grows the fidelity between frames with the EZsharpen dream-catcher pattern (filling motion that never contradicts the signed record), and emits a LIFEPLAYER \u2014 an HTML scrubber that spins/plays the grown life back, cradle to grave, with the signed events ticking past like vitals. Use when the user wants to record/play/scrub the commons' life, watch the organism live at full fidelity, or produce a playable timeline of the world. ACTION 'life' (default) does the whole pipeline: record (params 'interval' seconds between frames = the resolution, 'duration' seconds total) -> grow (EZsharpen, 'subdivide' finer sub-frames) -> emit the LifePlayer HTML and return its path. 'record' just captures the life frames; 'grow' grows an existing recording; 'play' emits the player for an existing one. Higher frame resolution + more subdivision = higher-fidelity life. Returns file paths to open."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/commons_life_agent", "rar_sha256": "1f097fe46efeb8c2298fde16d0469016cb62bb59b4448d954bb6757fe53f27bc", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "commons_life_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/commons-life:5ce87e6feef76e8cbbd53499c17d6aaf35497430b322f35ef44dc1e9705a6c4a", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["commons", "frames", "playback", "lifeplayer", "digital-organism"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/commons_life_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `commons_life_agent.py` is
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

CommonsLife — record, GROW, and PLAY the life of the commons as a digital organism, cradle to
grave. The commons is a living thing: residents with their own rappids are born, wander, play,
bond, and persist. This agent records its life as frozen FRAMES (full signed save-states at a
chosen frame resolution), GROWS the fidelity between those frames with the EZsharpen / dream-catcher
pattern (filling in motion that never contradicts the signed record), and emits a LIFEPLAYER — an
HTML scrubber that spins and plays the grown life back, frame by frame, cradle to grave.

So you don't watch the sparse samples — you watch the organism LIVE, reconstructed to full fidelity
between every recorded moment, with its signed events ticking past like vitals. Every brick is a
signature on a public ledger; the growth only ever adds detail the record allows.

Pipeline: CommonsShow `record` (the life) -> EZSharpen `grow/compete` (the fidelity) -> LifePlayer
(the playback). Drop-in (BasicAgent). Records via ~/.brainstem/commons_show_capture.py (Playwright,
installed); grows via the EZSharpen agent if present (degrades to raw frames otherwise). No PII.

Actions:
  life    record the organism's life (interval/duration), grow it, and emit the LifePlayer (default)
  record  just capture the life frames (cradle to grave) at a frame resolution
  grow    grow an existing recording's fidelity with EZsharpen (fill consistent in-between detail)
  play    emit the LifePlayer HTML for an existing (grown) recording

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "life = record+grow+play (default); record = capture the life frames; grow = EZsharpen an existing recording; play = emit the LifePlayer for an existing recording.",
      "enum": [
        "life",
        "record",
        "grow",
        "play"
      ],
      "type": "string"
    },
    "dir": {
      "description": "For grow/play: an existing recording dir to operate on.",
      "type": "string"
    },
    "duration": {
      "description": "Total seconds of life to record (the lifespan window). Default 40.",
      "type": "number"
    },
    "interval": {
      "description": "Seconds between recorded frames \u2014 the FRAME RESOLUTION (lower = higher fidelity). Default 4.",
      "type": "number"
    },
    "slug": {
      "description": "Output folder name. Default 'commons-life'.",
      "type": "string"
    },
    "subdivide": {
      "description": "EZsharpen: synthesize this many grown sub-frames between each pair for smoother playback. Default 3.",
      "type": "integer"
    },
    "title": {
      "description": "Optional player title. Default 'The Life of the Commons'.",
      "type": "string"
    },
    "url": {
      "description": "Optional commons URL (default the live Pages site).",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `commons_life_agent.py` and embedded as the fenced Python below (sha256 1f097fe46efeb8c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `commons_life_agent.py` first:

```bash
python3 commons_life_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 commons_life_agent.py   # or on stdin
python3 commons_life_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
CommonsLife — record, GROW, and PLAY the life of the commons as a digital organism, cradle to
grave. The commons is a living thing: residents with their own rappids are born, wander, play,
bond, and persist. This agent records its life as frozen FRAMES (full signed save-states at a
chosen frame resolution), GROWS the fidelity between those frames with the EZsharpen / dream-catcher
pattern (filling in motion that never contradicts the signed record), and emits a LIFEPLAYER — an
HTML scrubber that spins and plays the grown life back, frame by frame, cradle to grave.

So you don't watch the sparse samples — you watch the organism LIVE, reconstructed to full fidelity
between every recorded moment, with its signed events ticking past like vitals. Every brick is a
signature on a public ledger; the growth only ever adds detail the record allows.

Pipeline: CommonsShow `record` (the life) -> EZSharpen `grow/compete` (the fidelity) -> LifePlayer
(the playback). Drop-in (BasicAgent). Records via ~/.brainstem/commons_show_capture.py (Playwright,
installed); grows via the EZSharpen agent if present (degrades to raw frames otherwise). No PII.

Actions:
  life    record the organism's life (interval/duration), grow it, and emit the LifePlayer (default)
  record  just capture the life frames (cradle to grave) at a frame resolution
  grow    grow an existing recording's fidelity with EZsharpen (fill consistent in-between detail)
  play    emit the LifePlayer HTML for an existing (grown) recording
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/commons_life_agent",
    "version": "1.0.1",
    "display_name": "Commons Life",
    "author": "kody-w",
    "category": "creative",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ],
    "description": "Records the live commons as signed frames via Playwright, grows in-between fidelity with EZsharpen, and emits an HTML LifePlayer scrubber.",
    "tags": [
        "commons",
        "frames",
        "playback",
        "lifeplayer",
        "digital-organism"
    ]
}

import os, json, subprocess

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

PY = os.path.expanduser("~/.brainstem/venv/bin/python")
CAP = os.path.expanduser("~/.brainstem/commons_show_capture.py")
OUT_ROOT = os.path.expanduser("~/.brainstem/videos")
LIVE = "https://kody-w.github.io/rapp-commons/commons.html"


def _py():
    return PY if os.path.exists(PY) else "python3"


class CommonsLifeAgent(BasicAgent):
    def __init__(self):
        self.name = "CommonsLife"
        self.metadata = {
            "name": self.name,
            "description": (
                "Record, GROW, and PLAY the life of the commons as a digital organism, cradle to grave. The commons "
                "is a living world whose residents (each a signing rappid) are born, wander, play, bond, and persist; "
                "this agent records its life as frozen frames (full signed save-states at a chosen frame resolution), "
                "grows the fidelity between frames with the EZsharpen dream-catcher pattern (filling motion that never "
                "contradicts the signed record), and emits a LIFEPLAYER — an HTML scrubber that spins/plays the grown "
                "life back, cradle to grave, with the signed events ticking past like vitals. Use when the user wants "
                "to record/play/scrub the commons' life, watch the organism live at full fidelity, or produce a "
                "playable timeline of the world. ACTION 'life' (default) does the whole pipeline: record (params "
                "'interval' seconds between frames = the resolution, 'duration' seconds total) -> grow (EZsharpen, "
                "'subdivide' finer sub-frames) -> emit the LifePlayer HTML and return its path. 'record' just captures "
                "the life frames; 'grow' grows an existing recording; 'play' emits the player for an existing one. "
                "Higher frame resolution + more subdivision = higher-fidelity life. Returns file paths to open."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["life", "record", "grow", "play"],
                               "description": "life = record+grow+play (default); record = capture the life frames; grow = EZsharpen an existing recording; play = emit the LifePlayer for an existing recording."},
                    "interval": {"type": "number", "description": "Seconds between recorded frames — the FRAME RESOLUTION (lower = higher fidelity). Default 4."},
                    "duration": {"type": "number", "description": "Total seconds of life to record (the lifespan window). Default 40."},
                    "subdivide": {"type": "integer", "description": "EZsharpen: synthesize this many grown sub-frames between each pair for smoother playback. Default 3."},
                    "slug": {"type": "string", "description": "Output folder name. Default 'commons-life'."},
                    "dir": {"type": "string", "description": "For grow/play: an existing recording dir to operate on."},
                    "url": {"type": "string", "description": "Optional commons URL (default the live Pages site)."},
                    "title": {"type": "string", "description": "Optional player title. Default 'The Life of the Commons'."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # ---------- record ----------
    def _record(self, out_dir, interval, duration, url):
        if not os.path.exists(CAP):
            return {"status": "error", "error": "capture CLI missing at %s" % CAP}
        try:
            r = subprocess.run([_py(), CAP, "record", out_dir, str(interval), str(duration), url],
                               capture_output=True, text=True, timeout=int(duration) + 90)
        except Exception as e:
            return {"status": "error", "error": "record: %s" % e}
        mp = os.path.join(out_dir, "manifest.json")
        if os.path.exists(mp):
            return {"status": "success", "manifest": json.loads(open(mp).read())}
        return {"status": "error", "error": (r.stderr or r.stdout or "no manifest")[:300]}

    # ---------- frames (entities from the record's per-frame receipts) ----------
    def _frames_from_record(self, manifest):
        frames = []
        for b in manifest.get("beats", []):
            ents = {}
            rec = b.get("receipts") or {}
            # the BODIES: resident positions are the moving, interpolatable entities (the organism
            # in motion). EZsharpen grows their motion between frames — JIT fidelity for presence.
            for r in (rec.get("residents") or []):
                pos = r.get("pos") or {}
                if isinstance(pos, dict) and "x" in pos:
                    ents["res:" + str(r.get("from") or r.get("name"))] = {
                        "v": [pos.get("x", 0), pos.get("y", 0), pos.get("z", 0)],
                        "kind": "resident", "signed": False, "name": r.get("name")}
            sg = rec.get("signed") or []
            # signed events pin the world's authoritative pulse at this frame (immutable).
            for i, s in enumerate(sg):
                ents["sig:%s" % (s.get("sig8") or i)] = {"v": [float(s.get("ts") or 0)],
                                                          "kind": s.get("kind", "event"), "signed": True,
                                                          "from": s.get("from"), "schema": s.get("schema")}
            frames.append({"ts": b.get("t", b.get("i")), "frame": b.get("frame"),
                           "entities": ents, "records": b.get("state_records", len(sg)),
                           "signed_sample": sg[:4]})
        return frames

    # ---------- grow (EZsharpen) ----------
    def _grow(self, frames, subdivide):
        try:
            from ez_sharpen_agent import EZSharpenAgent
        except Exception:
            try:
                import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
                from ez_sharpen_agent import EZSharpenAgent
            except Exception:
                return {"grown": False, "frames": frames, "subframes": [], "note": "EZSharpen not available — raw frames"}
        ez = EZSharpenAgent()
        out = json.loads(ez.perform(action="grow", frames=frames, subdivide=subdivide))
        return {"grown": True, "frames": out.get("frames", frames), "subframes": out.get("subframes", []),
                "stats": out.get("stats", {})}

    # ---------- LifePlayer HTML ----------
    def _player_html(self, title, life):
        data = json.dumps(life)
        tpl = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>__TITLE__</title><style>
*{box-sizing:border-box;margin:0;padding:0}body{background:#05070b;color:#e8edf4;font-family:-apple-system,Helvetica,Arial,sans-serif;overflow:hidden;height:100vh}
#stage{position:relative;height:72vh;background:#000;display:flex;align-items:center;justify-content:center}
#shot{max-width:100%;max-height:100%;transition:opacity .25s}
#vitals{position:absolute;top:14px;left:18px;font-size:13px;line-height:1.5;background:rgba(5,7,11,.5);padding:10px 14px;border-radius:8px;backdrop-filter:blur(6px)}
#vitals b{color:#4ade80}
#mini{position:absolute;top:14px;right:18px;width:180px;height:180px;background:rgba(5,7,11,.5);border:1px solid #1b2230;border-radius:8px}
#age{position:absolute;bottom:14px;left:18px;font-size:12px;color:#8b95a5}
#panel{height:28vh;padding:20px 5vw;display:flex;flex-direction:column;gap:14px;border-top:1px solid #141a26}
#title{font-size:22px;font-weight:800;letter-spacing:-.01em}#title span{color:#8b95a5;font-weight:500;font-size:14px}
#bar{position:relative;height:10px;background:#141a26;border-radius:6px;cursor:pointer}
#fill{position:absolute;left:0;top:0;height:100%;background:linear-gradient(90deg,#4ade80,#38bdf8);border-radius:6px;width:0}
#head{position:absolute;top:-4px;width:18px;height:18px;border-radius:50%;background:#fff;box-shadow:0 0 12px #38bdf8;transform:translateX(-9px)}
#marks{position:absolute;inset:0}.mk{position:absolute;top:-3px;width:2px;height:16px;background:#46506a}.mk.sig{background:#fbbf24;height:20px;top:-5px}
#ctl{display:flex;gap:14px;align-items:center;font-size:13px;color:#cdd5e0}
button{background:#141a26;color:#e8edf4;border:1px solid #263042;border-radius:8px;padding:8px 16px;font-size:14px;cursor:pointer}
button:hover{border-color:#38bdf8}#ticker{flex:1;overflow:hidden;white-space:nowrap;color:#8b95a5;font-size:12px;font-family:ui-monospace,Menlo,monospace}
.cradle{color:#4ade80;font-weight:700}.grave{color:#fb7185;font-weight:700}
</style></head><body>
<div id="stage"><img id="shot" alt="frame"/><div id="vitals"></div><canvas id="mini" width="180" height="180"></canvas><div id="age"></div></div>
<div id="panel">
<div id="title">__TITLE__ <span>— a digital organism, <span class="cradle">cradle</span> → <span class="grave">grave</span> · every frame signed</span></div>
<div id="bar"><div id="marks"></div><div id="fill"></div><div id="head"></div></div>
<div id="ctl"><button id="play">▶ play</button><button id="loop">↻ loop</button>
<label>speed <input id="spd" type="range" min="0.25" max="3" step="0.25" value="1" style="vertical-align:middle"></label>
<div id="ticker"></div></div>
</div><script>
const L=__DATA__;const F=L.frames||[];const SUB=L.subframes||[];
// build a unified, time-sorted timeline: real frames + grown sub-frames (the fidelity between).
const TL=F.map((f,i)=>({...f,real:true,idx:i})).concat(SUB.map(s=>({...s,real:false}))).filter(f=>f.ts!=null).sort((a,b)=>a.ts-b.ts);
const t0=TL.length?TL[0].ts:0, t1=TL.length?TL[TL.length-1].ts:1, span=(t1-t0)||1;
let pos=0, playing=false, loop=true, spd=1, last=0;
const shot=document.getElementById("shot"),fill=document.getElementById("fill"),head=document.getElementById("head");
const vitals=document.getElementById("vitals"),ticker=document.getElementById("ticker"),age=document.getElementById("age");
const mini=document.getElementById("mini").getContext("2d");
// lifespan marks (yellow = a frame that carried signed events)
const marks=document.getElementById("marks");
F.forEach(f=>{const m=document.createElement("div");m.className="mk"+((f.records||0)>0?" sig":"");m.style.left=(((f.ts-t0)/span)*100)+"%";marks.appendChild(m);});
function nearestReal(ts){let best=F[0],bd=1e9;F.forEach(f=>{const d=Math.abs((f.ts||0)-ts);if(d<bd){bd=d;best=f;}});return best;}
function ents(ts){ // interpolate entity positions across the grown timeline at time ts
  let a=TL[0],b=TL[TL.length-1];for(let i=0;i<TL.length-1;i++){if(TL[i].ts<=ts&&TL[i+1].ts>=ts){a=TL[i];b=TL[i+1];break;}}
  const f=(b.ts-a.ts)?((ts-a.ts)/(b.ts-a.ts)):0;const out={};const ea=a.entities||{},eb=b.entities||{};
  Object.keys(ea).forEach(k=>{if(k.startsWith("sig:"))return;const va=ea[k].v||[0,0,0];const vb=(eb[k]&&eb[k].v)||va;
    out[k]={v:[va[0]+(vb[0]-va[0])*f,(va[1]||0),va[2]+((vb[2]||0)-(va[2]||0))*f],by:(a.entities[k]||{}).by};});
  return out;}
function drawMini(E){mini.clearRect(0,0,180,180);mini.fillStyle="#0a0e1a";mini.fillRect(0,0,180,180);
  mini.strokeStyle="#1b2230";mini.strokeRect(0,0,180,180);
  Object.keys(E).forEach(k=>{const v=E[k].v;const x=90+(v[0]||0)*1.6,y=90+(v[2]||0)*1.6;
    mini.fillStyle=E[k].by==="interp"?"#38bdf8":(E[k].by?"#c084fc":"#4ade80");mini.beginPath();mini.arc(x,y,3.5,0,7);mini.fill();});}
function render(){const ts=t0+pos*span;const rf=nearestReal(ts);
  if(rf&&rf.frame){const p=L.base?(L.base+"/"+rf.frame.split("/").pop()):rf.frame;if(shot.src.indexOf(p.split("/").pop())<0){shot.style.opacity=.4;shot.onload=()=>shot.style.opacity=1;shot.src=p;}}
  fill.style.width=(pos*100)+"%";head.style.left=(pos*100)+"%";
  const E=ents(ts);drawMini(E);
  const lifeFrac=Math.round(pos*100);
  vitals.innerHTML="<b>"+(rf.records||0)+"</b> signed events at this moment<br>"+
    "entities alive: <b>"+Object.keys(E).length+"</b><br>life: <b>"+lifeFrac+"%</b> through the span";
  age.textContent="t = "+ (ts).toFixed(1) +"s   ·   "+(pos<0.02?"⟵ cradle":(pos>0.98?"grave ⟶":"living"));
  const sigs=(rf.signed_sample||[]).map(s=>s.kind+"·"+String(s.from||"").slice(0,16)+"·"+(s.sig8||"")).join("    ");
  ticker.textContent=sigs||"…";}
function tick(now){if(playing){const dt=(now-last)/1000;last=now;pos+=dt*spd/span* (span/Math.max(span,8)) ;
  // advance roughly 1 lifespan per ~ (span/ ) — normalize so playback ~ real-time*spd
  pos+=dt*spd*0.06; if(pos>=1){if(loop){pos=0;}else{pos=1;playing=false;document.getElementById("play").textContent="▶ play";}}render();}
  else last=now; requestAnimationFrame(tick);}
document.getElementById("play").onclick=e=>{playing=!playing;e.target.textContent=playing?"⏸ pause":"▶ play";last=performance.now();};
document.getElementById("loop").onclick=e=>{loop=!loop;e.target.style.borderColor=loop?"#4ade80":"#263042";};
document.getElementById("spd").oninput=e=>spd=parseFloat(e.target.value);
document.getElementById("bar").onclick=e=>{const r=e.currentTarget.getBoundingClientRect();pos=Math.max(0,Math.min(1,(e.clientX-r.left)/r.width));render();};
document.getElementById("loop").style.borderColor="#4ade80";render();requestAnimationFrame(tick);
</script></body></html>"""
        return tpl.replace("__TITLE__", (title or "The Life of the Commons")).replace("__DATA__", data)

    def _play(self, d, title, grown, subframes, manifest):
        frames = []
        for f in grown:
            frames.append({"ts": f.get("ts"), "frame": (f.get("frame") or (manifest.get("beats", [{}])[f.get("idx", 0)].get("frame") if f.get("idx") is not None else None)),
                           "entities": f.get("entities", {}), "records": f.get("records", 0),
                           "signed_sample": f.get("signed_sample", [])})
        # attach the frame screenshot paths from the manifest (by index order)
        beats = manifest.get("beats", [])
        for i, f in enumerate(frames):
            if not f.get("frame") and i < len(beats):
                f["frame"] = beats[i].get("frame")
            if not f.get("signed_sample") and i < len(beats):
                f["signed_sample"] = ((beats[i].get("receipts") or {}).get("signed") or [])[:4]
            if not f.get("records") and i < len(beats):
                f["records"] = beats[i].get("state_records", 0)
        life = {"title": title, "base": os.path.join(d, "shots") if os.path.isdir(os.path.join(d, "shots")) else d,
                "frames": frames, "subframes": subframes}
        html = self._player_html(title, life)
        path = os.path.join(d, "lifeplayer.html"); open(path, "w").write(html)
        open(os.path.join(d, "life.json"), "w").write(json.dumps(life))
        return path

    # ---------- perform ----------
    def perform(self, **kwargs):
        action = (kwargs.get("action") or "life").strip().lower()
        title = (kwargs.get("title") or "The Life of the Commons").strip()
        url = (kwargs.get("url") or LIVE).strip()
        interval = float(kwargs.get("interval") or 4)
        duration = float(kwargs.get("duration") or 40)
        subdivide = int(kwargs.get("subdivide") or 3)
        slug = (kwargs.get("slug") or "commons-life").strip()
        d = (kwargs.get("dir") and os.path.expanduser(kwargs["dir"])) or os.path.join(OUT_ROOT, slug)
        os.makedirs(d, exist_ok=True)
        shots = os.path.join(d, "shots"); os.makedirs(shots, exist_ok=True)

        manifest = None
        if action in ("life", "record"):
            rec = self._record(shots, interval, duration, url)
            if rec.get("status") != "success":
                return json.dumps({"status": "error", "stage": "record", "error": rec.get("error")})
            manifest = rec["manifest"]
            if action == "record":
                return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": "record",
                                   "status": "success", "frames": len(manifest.get("beats", [])),
                                   "resolution_hz": manifest.get("resolution_hz"), "dir": d,
                                   "events_recorded": manifest.get("events_recorded"),
                                   "next": "grow it: CommonsLife action='grow' dir='%s'; then play it." % d}, indent=2)

        if manifest is None:
            mp = os.path.join(shots, "manifest.json")
            if not os.path.exists(mp):
                mp = os.path.join(d, "manifest.json")
            if not os.path.exists(mp):
                return json.dumps({"status": "error", "error": "no recording found in %s — run action='record' first." % d})
            manifest = json.loads(open(mp).read())

        frames = self._frames_from_record(manifest)
        grown = self._grow(frames, subdivide)
        if action == "grow":
            return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": "grow",
                               "status": "success", "grown": grown.get("grown"), "stats": grown.get("stats"),
                               "subframes": len(grown.get("subframes", [])), "dir": d,
                               "persona_directive": ("Report the life recording grew in fidelity: interior frames "
                                "polished and N sub-frames synthesized between samples, all bounded by the signed "
                                "neighbors. Then play it.")}, indent=2)

        # life / play: emit the LifePlayer
        # re-attach frame paths + signed samples onto the grown frames in order
        for i, f in enumerate(grown["frames"]):
            f.setdefault("frame", frames[i].get("frame") if i < len(frames) else None)
            f.setdefault("records", frames[i].get("records") if i < len(frames) else 0)
            f.setdefault("signed_sample", frames[i].get("signed_sample") if i < len(frames) else [])
            f["idx"] = i
        path = self._play(d, title, grown["frames"], grown.get("subframes", []), manifest)
        return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": action,
                           "status": "success", "lifeplayer": path, "dir": d,
                           "frames": len(manifest.get("beats", [])), "subframes": len(grown.get("subframes", [])),
                           "grew_fidelity": grown.get("grown"),
                           "open": "open '%s'" % path,
                           "persona_directive": ("Tell the user their LifePlayer is ready: the commons' life — a digital "
                            "organism, cradle to grave — recorded as signed frames and grown to full fidelity between "
                            "them, now plays back in an HTML scrubber (play/loop/scrub, signed events ticking like "
                            "vitals). Give the open command and frame/sub-frame counts.")}, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
