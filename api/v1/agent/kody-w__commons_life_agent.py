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
