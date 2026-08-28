---
name: "rar-kody-w-commons-life"
description: "Record, GROW, and PLAY the life of the commons as a digital organism, cradle to grave. The commons is a living world whose residents (each a signing rappid) are born, wander, play, bond, and persist; this agent records its life as frozen frames (full signed save-states at a chosen frame resolution), grows the fidelity between frames with the EZsharpen dream-catcher pattern (filling motion that never contradicts the signed record), and emits a LIFEPLAYER \u2014 an HTML scrubber that spins/plays the grown life back, cradle to grave, with the signed events ticking past like vitals. Use when the user wants to record/play/scrub the commons' life, watch the organism live at full fidelity, or produce a playable timeline of the world. ACTION 'life' (default) does the whole pipeline: record (params 'interval' seconds between frames = the resolution, 'duration' seconds total) -> grow (EZsharpen, 'subdivide' finer sub-frames) -> emit the LifePlayer HTML and return its path. 'record' just captures the life frames; 'grow' grows an existing recording; 'play' emits the player for an existing one. Higher frame resolution + more subdivision = higher-fidelity life. Returns file paths to open."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/commons_life_agent", "rar_sha256": "1f097fe46efeb8c2298fde16d0469016cb62bb59b4448d954bb6757fe53f27bc", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["commons", "frames", "playback", "lifeplayer", "digital-organism"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/commons_life_agent`. The original RAPP
agent is preserved byte-for-byte in `commons_life_agent.py` and in the RCI capsule.

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
