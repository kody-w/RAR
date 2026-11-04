---
name: "rar-kody-w-commons-life"
description: "Record, GROW, and PLAY the life of the commons as a digital organism, cradle to grave. The commons is a living world whose residents (each a signing rappid) are born, wander, play, bond, and persist; this agent records its life as frozen frames (full signed save-states at a chosen frame resolution), grows the fidelity between frames with the EZsharpen dream-catcher pattern (filling motion that never contradicts the signed record), and emits a LIFEPLAYER \u2014 an HTML scrubber that spins/plays the grown life back, cradle to grave, with the signed events ticking past like vitals. Use when the user wants to record/play/scrub the commons' life, watch the organism live at full fidelity, or produce a playable timeline of the world. ACTION 'life' (default) does the whole pipeline: record (params 'interval' seconds between frames = the resolution, 'duration' seconds total) -> grow (EZsharpen, 'subdivide' finer sub-frames) -> emit the LifePlayer HTML and return its path. 'record' just captures the life frames; 'grow' grows an existing recording; 'play' emits the player for an existing one. Higher frame resolution + more subdivision = higher-fidelity life. Returns file paths to open."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/commons_life_agent", "rar_sha256": "4d130862e28b92a3a3519a8b823905bffb90f35678565bb1743a714f20d0da70", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["commons", "frames", "playback", "lifeplayer", "digital-organism"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `commons_life_agent.py` and embedded as the fenced Python below (sha256 4d130862e28b92a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `commons_life_agent.py` first:

```bash
python3 commons_life_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 commons_life_agent.py   # or on stdin
python3 commons_life_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/commons_life_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/commons_life_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/commons_life_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/7W8ibLbRpYg+it86uiQ1JREgABBwvU8MSABcMNC7CDKFTb2fd8I1NT79pcgea+uJdmujui5VQ6TyMxzTp59Af3Pd2bbBHn17qd3ce4Mn/t3n945bm1XYdGEeQYei66dV86n2V7ktU8zM3NmF4a4zprAnSWh585y7/7ZztM0z+qZCf4/c0I/bMxklle+mYV1+mlmV6aTuLMmn/mV2blfZvKbM+F0Jgm7MPNnfV4lzqwP8tqdVW4dOm7W1LMPrmkHYFMd+tm0qzKLInQ+zszKnVl5lX2a9YAyt/o0KxJz+ASeZc6D2MKt6rBu/gaInND4AByAO10J4AWQ73cARHtVProZ+JeZugCf1ybJHZvrzGpA8Oe6MRuwYDaACnui7rl3IjJP2olZHz+By+V9feeHByhPwmaYWW7Tu18h92ET3DdQRh2YVQFWnMo108+22diBW80Ks2ncKgMkhEky3TXNJ+DgDMCduR3YYudZA/gZ2s0D15POx7U+Pu7tptPtzBlzpKlJYJQ4+6VdQjAKVmcHmWVmQMitZQFwd8h1EWb1YuLeA+Z0k+zBHcu04+8k+OnrTZ7oAWmTqJrQjieyC7NuwPnYnXWTLtRfZgoQaR+42f1QWwPMQGjTifxJ+h394k7XW516fydjEjHg0H3hRa8mpXEnmdzF9cLyT2B9VlS509pg8a4RpjWRHqZgPXtV2buqfZkRO/nIc7P3E5L3sw+O65lt0nycObn7YAVQRnC6CIv76Z+exM4+FCYQaT17H2ZAYJ2ZvJ/VYCUDivWNzH++g/mqKJ9m7522MqePX880OeDSx9nn/3Vn/ezDq36A3XVrOcA8HECfB0ioZuDB5wfw+4lJ2HccDLjDBdwXbLnLeNKEym1aoE+TOgDdCr7M3j8u8H4WtUBEtlmA9edV7/J+AP7b7P1EyPunTgOtcW/AkO7Wdz8PPoE9E3ffP7VtglA8sHtABG+P5Bmw+UPoTxr+rd3M5kDHgSE/b1lPj36eBffNn1/taCLty0y8XwaYaziJBFznrj45YNMX4Lncm5kWiVu/++nv//j0LgSf3/30z3d2Ytbg0bvdQ50mHhGTHwAHEjPzwUoxAB+Yge/AWwDKU/AIqMHs+e1D7Sbep9l//Vfcm5Vff/zpl2z2/DPt5kHth8faF99tPvzy7vH4l3cfJ0385d1EOvjypW6AW/3w8UuS92714eNXME3YgOt8C+X+9BWI/BTvi/Y+b/MG7ld4bZV8Bw08e8Jijir1g0MvagxOekluNr8//rL6hIG+Ofiiyz8++LL6chB6c/JVr8FRgOD3B18XnyeRtweT1v/uhtPDV3Y9fcfnb3j/hurvzjthNR2fbCavv9xtxb0V4Ovkq55b//7c9o+Pdzwv+6I8zD7wivyryPPypzt5b1CBXakZu+Bg/QGEpbtR/JrHP8tV6769VJA3k7P4HVCwH9xsWgG0/e13oO5Pvwf3FWAKnKTnAhv/ecYBA3wjau9Fc0MQaF4UdML0MG2A6o2ST3/gOYAyGcKXXx97XtC/KManVz34NOnfx9+fBxjBsRdBgVjaTveZ/T8/T7drbdutwfdvcD7w3p1XVOfZF6dNi/rDP7+e/wkcdqsqrx60g8e++3j6co1PX3f89IaA56OP//qGyjcMA5uBrF8eAIF/d58X2//5Db5/+wYg1Kfmk1aQy3wG3hAEnQX8BXoQfU9UpvU7yzPgMO9Pn37ld1f8HuUP/n7PtFeOT0Af7n5aSNzsw8uNn5yyXLO57/s70Ph/F9VX1/5rME6AvwH6zfrHiYq7Vf00c/5dHI9s46mLrvMDLN/t+Lfpz9xb82DUPRSHzU+zN7HjKfifn+EREP7z+/+s308ZJgj5U/wDJ7788m72nzPnX5N9TCnsz8vfWSZQn1ddA2npZJ3fqE5afOsJnvb2VSm/TDoFrvWdZmZ588aDAe9Qf0iLjz/Qze+ROP+zCP475vtqp0AA+dccA6QSLfDIwFH9Z/2SwlZt9iqFl2TGAy7xle1/bNd3UkCUcuoPU9Yw0f0F5N/Oh4+/E9Br5vZweY+v4F95+uL+XmC+QfXImV/OTN8+PA5++hrpPv7IC999yLT/Ow/yf8t7PJD9tUH8id+433Z6fv/wNLrnw49Pf9zU3254Pvz4b6Furd87p98B+rr49E7/LS/yy5TrAa6av4IzLuBMdw8dALDoFnnVfE2Hv2qiX7n9pIgvOelPj+AX5tWLvvzy7q9dDMCcJ2EdgJJpSjW4N8n8rB4ygLcOR7D4UkTUj5wWlHWgxrEmY5gWh7el17+HNnNBSg2q5fpefb91VR//yE/9x4MFi/ven35UZ7zdW7mfQfE6VeqPFP+Rn8+/1tH3i4BaAKTsX2vM59UBXyc//QbgVEOEn2betORmbeqC9MJ96MDfv4atf3zrd7wvtds8q7gPz32TjjwO/D38x1OBngsfJzsMZ//vXcFeaio3AbXq5JU//insZyPhR9Bfl/4YPvTnwB9c+/XBtR+h+GbDHyMC1vENJsC/0LkB5k2J99e1SWCv/msS+RQP7mXIo7XxO75/mv2ZOX6a/cBB/t/xZo9Pf27yf+LHJg1/VK3T4sSCf9+T/Leyp/++R/sL3JM/+vXFGf2hJ/4LIFMUfHBl+jSbUpl7EL0z4i/O/pELlV3gql67POBDWL1tTYCMZwq5wKF81+V5bVK99hD/yrcBuv+oy/iaLjxTwKnP9/RFT6czOeCHFwJnftdEenW/f40fXALgzkCm+GifTf2yyWd912j7cO9vJXlePJpcn/6gdXbvmv013kdf7eOX2X7qgt37YpMEJ35O95r+uV9z8RpgwFoLEH3r8d/96xOo70GF3N4taeqV/Md/zNjQrvI695qZBI41U9I1ddCm8CBPvdSwfra1uqnFOjXYHvuKKo/cR16Te7Pf/vejr7x4ivnXScq/3k36t0cXOK+ApDMgaZG4XH7JHi1aALwAfgBUlvdg17ifQTT4PH2YOPvb98C+FMNv9yuHj/6iuDtOrS3gSdwvE8naFPEeBNr3xpRrtwBYkttmcu8mgQB7r0vurATo6zgE6vDQ7LwaHq20NvtpAvbbb79ZZh38kj0aR8js0TCvF2DDKzmzz5/BFbwEBN3ml8y1g3z2/p//ej/7P7M/O3UHPuG4mPULgwGFJ4nnZmblgyg4acokLWBBdwb/819PRgIwU28QiCP0wteGXhaD2ufJVelAfF6uMKDb3tRwC9Mp05k0DmQBs6M3e6UXIJ2WpgZykIO82XGBZgFtsYd7t/iX7JWTUylQg7K/9oZPk7nfsf5mVeadxPRXG2z/bcbuLsDC8uTe620fEgKH8ywE7H+V+dfO8Pt6tn0B8WXG3bveU7u1CCrzicMzH3KZGo3P4wC4Ocvc/pdsav25E6vuDYkHe8AmwBn7KdLP9w7i01bqF9z3PSDLcGZybgLkIBupn7o8jRomRwJIGWZ+GzpmZrt/e6oUqM3axLnz7+HwXqTgPKVy18G3ReTvXNP/2HTll+wvxitAtTP/pzeTlZcuPvDQkxt8DFbqPxqs/JJ9N1mZcP07kxVaJFhK+vPJyi/ZH49WJg5JPx6tNPdp0R8PWBa/H7EAs/12xgLE/z8/Zvkl+6M5y4N/fzxreVwf5Pj3D99PzyZlkvLZkLczJ8/eN29GIzUwE8CMl1z7Scy08wfjk6kT/Ol+oaf3B9f7NhACkT/Z7N5V/zWYpvlkYM850MSFf3cORN3hWMAW47tuAhsDJ81pCjGbDG1WtFYCDDVxHd+t/vbKIoAmz5LhTsfMdICaOW5jhsnTS96HMqBGyvv6zqDL68DmaXdSAEL0b4+Nv80+vNjYfYJCGdJTWX6bUE3RqnAb97nthRf3rW9rnw8vI49JbiASk1VefJ56qluzDu37lOHjNLR4WEUXmrP/b/Hl1Tm+xkTgPvpfn4OYKXJ8mOD31eSJgclNm8G9XOfj357DmAnQQ8VfqH66QO8RNcHHD44LdMVxH+M1s38xjxycq/qwdgFdXD67HI93ZhGPyH8vpe6K+Oj5Tix9qzHvn2b94aXru3hp+j6Hn0ARvhrGtyOp19nahOUJ/XdDqG9nULMP32j+x8cA9lv3MMG7Y382YX48rXpff3Udd6X96iHujmAy+MmjPYLJ5xe1fyjZneZ7xQz+/nDe9u3Y65Hff/xKwzRzCm0XRJV3P2XAzD69m+qZ3w+npjnUNFoE+lfV0wALZFTA2Tahe//2KHemT78f1N/59vMT1XxCPL/T+8r1v73w/Oc/4vdDv8D6V878wdzvDvnnHzLiWx68nrpP6EAd/+6nv9+JBV8fa+DDhHe6NwABKst3zVBMTJmGNoBnID0FQfv7G9MA091aH92JHyKdwv1zRDgFduBBJjK+h/9U4++RyNNc9nVKC+LxnV+vM+uvfgR43gzoVebk/eQJHkyfodAbfODyIBA80u2H/XyPT/pmhvzqb19aTA+PPmG9h9SZSEk8o9xn2B/uk8XX4elXv/WGnh+SMw2svieFb5sCJDdenoAMYDYp6lc4798O2N7/kKevPc/vIb/q109vWl6PvBvkY8MzIr5pjL3GoKm7VJjhQ83qNL/7s1cX/JU+5A1JE7P9x0XvzYwf3PT+Acj5Ob6+b3tz2T8Yvv743m2V/AmGl6xMEZlX03zaISg9LsCRT5G0Af75e9j/miymbEEC6zxG3M/13Joqrgk3oL95TLD/+Q44ENMxG/PpQp5FGdhemdXnespbpx7LZIVm9ag/wNofl2vPjUBwoIQAO1EHRqANtnSXGwtfmoiJrGDc3FibJYJDK8vzLBzykBW23qywlWXBaxQx1zDqLSEHcsz1hLjO28p2f51whRPyPq+mnOFzU7nu12XwyHlS/SBk4sNrdXh3iQ/i//nOwlCw84DWR+Lxt1vMVVtDLpZYGPMVtsj7k3KsqZ2Q7Dfnsx1F/IWhNKiq60LnDBpqydiHREXwfYImJFlqSj01YQwx06bSXadZ1CRnNdpiVBYnBo/abD/aUnLSjSWIU4ftoR7mmVxs5vB8lNvQWCxwwttQy7nb6WizSbfY0ePD82lzSA2fzkUZxROBWcO3/VwlqVgU9c0tUEcYO693x6Nwoyn9UmCJvYhCpl7tGyJbIDqAa4/1tdRLJYjTcr9OYPiYQQV1yOsez3pxxVh9HmicsTFoHmrYzg7T3ONW51I/2kUSCyhh8fy5gok6pHcDxSu8Q8pbmVnLdF+0c7ep16TJJLgSbShKnHsnhbsJeCcPy0N9ijJXZmrcim4Xdj2gxmUeQ3THVFCf9fUiKdIjGgxXg7aHwjigLLxMczfi68rNEHJD+sfuqiNal11YPxs2mRyQiBLipzaXRBq9Dms3zk6rlomWTGjoF4LPSIpDDm7hZeaeMmMqhaWY7EYmVXFeOgknY8GY+WqdqrnBHQNycXNCvLWMdLUuEa9Vy/bGoRsljKrTbc+Occq3trHTsNoL8HEVK/7CHBy2kveJQ+/jVeWhurz3dvzqoLRFxnZ03xoGyNccUWZI+sIcZHGNHqNuLtgoY9DiHGOuRDb280a3WJyOlH1NEtzpRu10Btn65x6hbHRpUQ5VJFSJHcMNVWzL0CRIp4Co6NJpfkfP44HKpYFepAZLwreTZJ87ze4q0wvhfp/rc4f32R6qxyzkHMLz8jPa4Dt4O8jteWctLgscJtlLfqEdiO9148bii/mW1ZxtmVGnk9chGUzMY1pf93PPu0bVqIlqLYxeY8VBVG4X3ZGsjrnupx3fSdGRrsxrUaAX266iMYvPO52/cmg9ry6XHUqej2OcQXnHBoN28euV6Fx1uAh2hLpRlVgi/F19xHQp2p8ULIzPcyJW4DrOLXfgVyy6CTTzRtHbpOEE3zCMi5iyO/C/i7NzCo86sBeM4Tbz+UWPGdIyqaBe7jZ9YMaGuKXRPAgGdBcipXNWhJ2luUUzbLVxfupTwRGiPN9Yq1hiB8LddslZ3ovzk6TfWLIsLo0K3dh0YRzY7mQcqp08V5HyuMY9ptDPpnNjmzFVDGJrl65JnEStFiAyyneRErhDIFMhchQ4IwjPvnjJsVtq7mJpIFQO3vIZA89t6Fw6HU8luMnw3NLzsryo0xDNqM02rOlYgi65uFK2p60nbE5GPhaS5eIso7GreQ1TXKNfVROG1pllj/vbET8tSzyX/BK/Uc0prmCayo9sQFzh8pYrHXGKF4uMWmUJMWI6Y15XBiFjnQQdLDmmrWOtnuVb1dAdtRuWfXVuLjan6kJ0CE/RDhW5y344MDwW82dpvpXK1VUOZPoIXQ9WrVA2cFUMM1Dm2SDjk4/Fx0LftBBMn/ZoL4n4Ful2Z5fcrAfDRelcNengpBHY9eAQS9XdAklEGLlrjgOe2Y6OgoC11Oa0dg2Vk1Udrsc5kkbwXOp5kY+bmMm00ffXdkLJMGdc2Yrl1eYwQFq1G3TMvmnKKQBmnPSeYAzC9ows/aIlhk1RKIWzv+5vrCEz2GEVj8qw827qvhgv9rqR97Tl7SOKo7cjDfk6Dzz5LlV8/3QR83lwZNH0ktSGVDiwdhTQ2xxTNUEySViXbm6H9CchAkZbXcj2tjvjHik2534cClS7iuxSK01db6IxwdLsZlAChGIs5V9aLdmfqVOxGsYdwodqv3FYyTrvM12K0chMV72bayYqNKqw7S+MJSDjbrkJijLkAj668llnjhJVD2Uin/xc8oJTg9DiccC2Flsh4Zk1r0kRMqZRa9HlypCVsKrrAfCfaDtszHxWQIdWk1F3B7s138vKcN7t6QA1nM6Mkwtl8weEVDtFLOIBBgJtIO8sOQfCVrQL5PQG3Yp4zB3VG6HEzJaaRybPNjlQjTLRSZpXhXhx3MiJo7CoHo48NdIHbaEhBQUfKFfiV6d0B0XJVuCULl0bV1Ld111O+YjbSRshDok5yaJQvE1VB5Xne2YT7jshPZE4ZiU33bkKGmmc7HF9FBhbwZN+uS4PmrgKbSktiqup7svKu/JkmuR4HDZOisC7FdLS5IXvPJ7ba6niEGyrRJEq9XmihPMIV2A0PZQF11mOEKKwJ+dIpmC9xB8hGqHTcLXwRycONQiTuNN6R81haJMJ8Op87Xuia5Sxhnm/c1r45AjNjTQv4p44qmiqezGuCmkrRwGDA4uWum1SbrvATrjlQDeCVAdx6bAWscdRvKc3IrNb5xTq+yHOnBvYxC1pCxVMxNPIdrXV2dUlIFmKUes1TnaUj4ZIvsUXzMVbFZbnpiQiDLhERCJOqY0iCwTk8/S6sVusyVhly6zXzJlRW/jqzzuSKYrc2C+8xWJ3TO3LPvCCPrNv0IApBisla2i77TxUJHgQgJUN5MxFmGiwDGJZaJ9dGbhbDlyfhnp9DGqNhrMIX3uGy/N97xLMiC3ScbNqtKoea46EUo5FBBCjFCfi6kgZ4Zy1/HG82UHRVMFNgbUiQVeyqArESers43Y3bkb9Ahe7oNtlJKlHW1z0amXBeUs7LYtmvtVDJtTKWmltKu+tswmie+WZWG0PtCVFwZJFSpDMQg0cUGd8u9AYP9DqI3dFOsX1xYE23UCG6zY1B/poWhB6DrCKlY0kY+1ruzwLG1E7kKdyP7oLZRlI7m6HBJIROstIYkt04EpEHFoULcR9Ep6h3JAbyhQz1LtpcEjDorTcjNc0NlrRoqzD7qAryLJqqZ1lJPYop8t4LRlxw5QrbFmLHtqOKCauycPSES0XxbXlcjgGTkj0N8jKe6S+sWdmDgq8cxPQxWGP76i+1w4HQhFq3l5fg2zc4G7XFfya26PuSokqxrLbLdxxg5G0Zwa/3tggY5w8c0UXvV46wTvfbi0ZkfpqcJRA2ZyVBvcLpHNL+TYQ3W2Ua35VwwXmNMrBl72YPDv9QgntaKUpGGZG/b5u2PUpXMtYoV4jWauW9EVG9i1FuDCz9HtOTM8XiENkJhmqG7pZNrvbOq1ShiWgo6VXJXtO+CVGej21jFdBNzDeNXC57TYNrNi6XjR7ubaZq2bVZw2NMLN2RqOAgoGL5UvEES7EVcKSGYdwXAmbQVcYQb2e2sXhttrZq1FYrgPJFkM2h1R8DbcgGWeZoeD8rqLSnVZgu5Pvajqkn7ZWODKsqABlOcqxsZyHJrl317U636NWsZXIcuWUGUo2NhKou9rMKWKLqMguJ9KDom6KYXuze4NxVXa0jdwdkz3pNfF4PJdaJ5BHyYyP7pxz9sh+dTLWwOwoSUmkMbrJRYDaC2YJg5S32mUsy6A731ct1aovUReYkOJvkCMMjhuIsDizKrUrqPMOTdkB5IjwUpKP6BUmbeccCDeMX+xXtKTLQn8US7fBThITWnaqqhSPH7ZbBFrWZ3KkNLU8F7BMFYYT2AIDnwrg3wKEtws8FSpru7b9/bC+OGi02xZll2TpMF7UYst0HSxs18s6gDTH8+rY2LqVt9XT7a7b4nR8S5ebodvUqlDRZb+xTLI5ZKERZK59kvHV1c1oz1ukzVYWz82QHvvzuTlwxVpEIXJxEhb1KWgsK60iHcuA3TDxUDtFZkkOLKkg05kzOheerJRb6etOEFXZrouDHvKLoUDaPt/tUQyDNeqIQxKy2AqSaqgKdN2XUEyZ1xa6JYXAL1YSVitKAK0tgmis3RbNWxTpRy2m+ibYc2YLzKcOSd04cexeMm/hQGM5tbTW0uDpa0wJhx2zu2h+5EGuZh7HXvWRduChODFUveZkoNLjwba1JlNqDcWHOt2CPNERqQ6veCi7FqXXhL2J6geWalO3UNpaHLBugDz0igUjq/T0vrc2wxqDbdQlep9cObftRdZ3eSkplRYuJS2O1srtRhlxvMtxn3X2IXKryHJYl7fi2MXQ0AJX6FCeye73rEItS3qEN308oqzPC37tcfxwDuWOjZXRsY72OdwkwSr0WJHGuPJ0TQjOXAMHMe8QhBuQjY6K6uaikBuQOCExoGs91xV31Bh5aMuraB5ZdxBVVClJamuyBe9fHRVZXSSy269xWDGg07rnlfmNaO2BQ5cn/HAOkXWH7HE53RDSDd8g+318E3maxneowIXLELDj7PINN8c9nYnXnno1muM1jXif58q1K9TXvDw1rp/ZQqAKBU1L8nk8VNuapClX21BzFV2Je73aSXwo2BKnHMlFnMGYq5qHItqxLh+HV6l0V3vIYeSeN9I9erNuy6FEky6+ovN056y8c0FSlSdLJDvX9zm2YUnBiI9WKkprLbht95y9J6+IhJfQUmiPIFVhoSMvxcpFOt52RinRCJEOpobrq4rH1OCcReS+5EF94fnhiEIKnPZL8KEnNKTcQSRkLrvkqIX7awqkDepF/ywyBSgvzIssMOqpdG/23J6XgWD6pbXYUhuI4EH8PUe75EZU7iZ2WVnvsGOSSWTh6hgisHTMjtpu0MbjReNCm1K4FjoGQlXzTWC0dlNiC21r+GyiH6H6xtwEVF3mJ2On6P3eMBTdEsplW2httkCVhHOEuegWXHhmgIh1X0IOi+U1NipjOLEq5rRLtliFm3m1vIEqLjxI8wC60aPssB7tlyAqKIttunW11SZUCUSR5422PsK7GCOsSmmKNK3JjbTW2124FIWw8q86vt1v6d6iMPtsrLJqY12y2+K6RMw9qdN0x/e1oItVFxaxasG7gmiGiCTnjXDzu76H65217b2Ed/OOl8frPmfgpD9fK3EXovlmQJ1ttmN1rksg01GDRZy245yHObbLl7flxTwH4YWxO5MAdjDypFwv/avXY71ZFMcMPnISfJIl2tb6DEqhFc7QVq2K+N4WkClkUBZTr/Lzde5F18paCTaPzJs8xbV4sLgewzBmwRPK6ZaUy82xaUJKMQ4us8eHM4ON/FjGpbjem2fBbHcqp/WVvTwl82XZV4alhSeeCu00gYeVptUW1i+5ZTJusBtH0iLEnU2Z3EHcYRcZ52IeaOkJN+odhZ9c5kTyK0FSMkkJ0xu5Y3NQP3udvlmznn5Cz8QhWIj6jcYgK2YS7eBz8LhHB/ZsDQHOsHC8DirG4664uF1ePLl3szW04UfIiFAcK1siH2APxZqbJ8+ZislPqyGSTGhrHJexfjL5fbKCKGh93EgjZqNOEy5SW56bMXTjcSPbexnpLuDDQvLwQfPNAKGwbmdfChlf86eKVhzMca+1rxPLNXTSgjXFXO0q7bvVISjsgSw1eyH1LCUX6UHbjhK9ue03ko6e0KELugsRzEHpIlFYNvdIwcIXvLUoEJYPM7aBUYPglFs6KNIArC1Fs+PGDC/6+ogsy0sx0JusikHkJ3RBBtrZo4XHQw4lWOmGrmFT5VxgcCqrQEty5OG+69oM5A6X1LYvwUYkN1VGot5KSnp1E1GhbCfdpl+5Jylo8FypkB2NlyQnydkZXQqoewrsCDquiJVIXsh9YW7xhD8EBK1QoBrb2+JCMQrXlkfkFl/W1IHAm5Vx0hi29TN4SmJLLUJRMeFCOYe5ZZZs3ZyxbzVPpHrpxWhrGWeGVePK8drc9Zh+REvaD2MLYueq44setXQFbCtUgbdoCbULXLUnzv2W90i6sw8xym+33q3BUe503dzOqmSM2cY9akqw9ovVWkNdmRFxNPKpciMdjSpy9e3RCZOcJ7YKqI9Xqibr8+BCA6bXUW4RzW2grgh/USA6kmC5kE016C8dStL7a59Y6uA7h61w1cOYJeu9l5tClC9X+zXBbtp4tThubaQEMSyk9OoWCuZCnAfeEtmTq8SmhoXDSGcyuurisF8LC3kvWkWS7knzRAzQxTnLau2v2Pm4GsUMVxIUMc+sLOpNmRhnl7DYUPfUubtcVdb6UF/I0JuvuW0pKMyNjqi4tK4OySW4xl92fMC1oc1Hp6RCjOpihJzuIhc+cC5lyKBBE7DGMZQ9ox6ohW/IA7e0EGlQ1tCxB372xGe+kNstWzPZNVicQVUNavL1nOcKPUPn9GFRK05/uAQNeYXWKXRLt/2cyWppveuIaJVvi0OJWhbdD9axmy9hYp42adp1+NFvMflkCrVWOb1MXyyr76DeZQ+Lq31gvDKPmYBUkvSSjsy6PgLrJyqSd9J9I5jZFvYYkT0OnUIko66gS/IYqgjHpoTKkuUFPXeapFybo6qUkVWlmqDbojjSSFPNVUWMrJU7t6KS5WWjM+thH8iLwt+SK4ERK+4Ub/YBOl/uM41361w6LDSFluzKxfsViOwx0Wzg5UXeRoTL2AvFgutY0H2fqaDzGckOhgocIMdjASiJcyzWdL2+wgV35XpzzPYNKQUJARJEzPeXheWrZ/IcRZtmcz46ZiKeYWI9AJs5XldHT0RGVlcZ3mf0shNcGN5R3HGtcstge7H1i7cYECPi0+JwYHVIi7oFrJ7WQ3mlQ5pnioFaerlY8uaBanreWobJRbbVcN8M0moncDehcAJFuVo8clwtFp272BDWSlFwlTNKyjYGfxAXCw3fyktTHLdH3A5qxziWShd1fuurVXsjbcqyh/U2EkQ6Vv2zuozI5YaMcAw2x76fUwYBInURKDV0SIhiyZZJRV2G1j62GEoGRHUUN01ZUm7HSOwZ4tUMFm4QeTjYKKmmdttebvBmwWc5cjjCet9HMJycL/jG5df4uurXnuPlVgD1VppC8/Y0yMejp5N71i9S35NVOSP0vJ6vRq9Uss4KelLFqOVtMUeik8V2er0FaZ+TFvPNyXCPSTG2I2HnC65xWZRdNb5QKlHpRxtsSfdXOOaX8RxHCGlAyLVsyRfVia0tXRRGlJ3D8ZSsL4fLsCZZRMvNALhIrWgzg0LHILf6dS/iVcEcjvP52iiv7HEhD95lhMAVnEWE54FQwxvo3OceIhyQvejXveenXeqnC7eJbptD3q83W6fi7K4uS8E04dOyUE4EOriqkRtel0c8dcq89VYsYzbpF1mIFjE6hNmWV9WLpWKl2p1zNVzaMt7e2ptF+0vJvrRi2FcrV1LZpnK0sK4G2Ng06zZYxR0TxGsTueaKGsXL0uocWY0NLZE32WFcmJCIb9EeBRXzRt4rztEe1OIowsGepu3oki2VAecIKF9j4dzXbNWHLxcNMrLV9SLqUQSiIbbBjOFqlsha7SA0hb2yKq9bVpGywGbPG7nGVtFRozfX+Z4bxRSivMvCbNDFSvbXxBD4JmIEiB+fuzRtBOVAFPNrABfI1UWMFrKyWx2J8dSOXHrCWHGBrGHEtRwNW+DrHYHIqbXab0IqNNI2BBvPh63nn7NmZwS8FyVluiI7r+wQhZP7YC/p4k66pt5avDGehvHDZc8ZtXPktriEEsn11p794dhHA9TvCnW/2GI4AqsItvSKjNZGZFOyCJ7jo+Rzdp+n4kre0IMmZV1o+X4wHsRSyWviGgg2bBb73sNAqmgtse1eqLfYyvUsml6IVYbqyHKn1Hud6b1aEkrtCvV64V6P16tW0OmqKGPGKmMOG7IiiTd4WtF0dqtgo+SH5orMcw/S2U3B+fXCS0ZveWBCOciTIzqOYcQJGdGuhngsNFcf9P12xRI8miAyxyzqYODdDSrXEEO1oo7iI2Zlkot4N6RKKbxdW/MzLqwLW4ZXgqwekNtW36wSfCslOJbno3tUeKllUK9jIkRw8Pkm43fVMM7r+XixbtzFv3j7XWTaJHcmtC08SpyVHg8NpZhr1kwbNSYMJzXGVIaF5WgySRNQh2rBnzOk0RDqII83upR7iut7lusEYi6f/DMSLLBDRBNOabnIkIwuhjQ47+3YMj2vyd5KluHtgvaN4dCSCAqhvEzKNZx4ScHEeVpZU36rxIvKXFjHyy4/QeLpsibm7q1zTvR2qYnHbtwb24g1eA2r4pKXrkMWdKYTmSA3gkE+KW7mGbUM2LWQmaB2lHlxRTHLtFNwBz2r8gYv3KUwt8VVpMRATDJ9vXJemTlH1uckCC/G27hZoCAjEeaYiOL1pLWhr6X+FfgnGN8oCqYMK5qQ9ltQ3N/YLlNUbrEW68WVueWr3SHfmWzs4odcOg1XqsD8UFbY5VhnUimyROk2OjtejHVGKg1ulge3YTsTAcUsftBB2G44r0gjEmJMaJ8vj0cOpgY5lsXIAO5PcNLEzhMNz4QxR0wldu32qLt7XLm2ZZ6BuBjipnEekLOvxudQjQqaRf0wdU7zQqtt+boKOOe8hx0fQY++a91uB5BIc1hgGZAk0h20jhLiJEoH4iSj8NbKdrBS2Gf2oiTiQWeI1GOTo8etNuS6Y/orvThAV5C6szVygV3U7ujLuXdQXSTyLII3FIwfke3KunLj2Q9ognB5RIaPC0zuFn7pHcZsgcvG2txBML1BDu78cgAltw88LwiNRGroe3sluKKyEq4H9uQeoTHujvZaOa/H7YgdbiWyiCwdRUDG2+fX5ZW3PBwcDGVsKQbsSQFSBinkWt0y4jKxzWWi+D1bhMdLiQzWLe5P27U8nwuLxdWRk1AtzXDPGHjqH+otwR0WoIYIsZWnGp3AtN6a2IfWUVqt182crA7j0h09ejBw3AgCiiJ7ZtEJtS8HBN6Vc8OBurBBFfus7mlhrkgneaN3jg4HG29L0phwqjcEzdAre6VrAYVkvB6BGg3haXLln7k5HAa3gZVsONedDTEeg4WmVdyCX5eBcVjNQWAyq3aVF/CFjg1PXZ38kPRZw+qLhtsx4oqpd6crRZ1EeAsyCcb3lQzEQ7/SKKkzs1WBGtT8SCQdQiTwwd2u9x52FQQXT06Qtdul580+WiwK79jttb0aQkHYR0WOy+aOso9UeowQM+pjOqFuGr+Tsai7KZLULPPMkIEzzwKlQ2SlbcgF1nH7OQhBkh8XNoVKZ3175iN/h0Hd/LBDD0ecVNxak7aSyuEHzan36phJxrU5DGyvnBcITg8+DLm3taSGJ0vNW3Q5QKtWm1ciGl174moqy/UqXa7P58YqCyWXtbkY0e3Ym2bRKhgUa4SecQEWHkRUvcQXB3ItXrniF9uNeNS2RHWFUWQFjf2R5Vm7wmmW3y9brgHFZLY06FjEywRONHo1D4wBsSsS86DSEL1DPNyyzXiwN+oJkfAjbCRi4tPk/rDG2sNNM4S1MtYRp7m8kPFGsY6juebMNw2+LlZ+FKqqcagRu6fWyl7t4HlSnPAuoJc4xqGk2deofdnemmxTsf0Ald6wUHH0EM0rA62Vm35LNbmNut61skOH6bns4tRZOe8uw0UXzu4qhVVje0lPvHplnANLNKDwDWOH4hp1ZajGwDsGZ7AnnM6qDUzDY3rZz5vTTjlvef4Ub0XMP4l0gscoUix72YrlmyoiLCOw8E73MsLoHHNPyhaB4akcpI2pw9pJZG2hWW7Vhb0352E/XguuYRdmnUp8pi50zYLMlloOdJse5yssLbmLODf8FBpPEkzpxgET0qoxsbRZenW9mreIsePVMdEYQsTDtg0qnSf3XbbS9EpInVG5cUI5YMG5bskkj7qaDpSwUXSIXuiYsk1PwKBvMQufr2pKrZfWRXYuZ9IbEt9nd8sV0ZTHZq4cLRrZdMezU448OZSsHySianY6XIjblEd0xJ+D+x/rU7Rq25MjDdxJppfEztdYHkNAqn2kGgHfYR6p7JSyXvnYycqcfBM6t8hRWePaafhKubLby/mG0VpGVBZyTm98qaLIbYB7CT9zNZqVHVbkpIM0AnZT2nF0sptns/RBL51eNSX+1DmlyhBQOdeW62OZW13L0euwd3Kbxm8dbqTVvtik9f7WGmSeBPuDXVU3nln7JF+ZMuVjS0wkw/kyJ642M0lp7+xpRCcNmQMFUqRelJwpVrUWVd6YmVJmiYLZ7zNDh7shxcteOtM6Xw/K3MbqGCvgQolU0VKWulo6Rb8o6RLU1W1wE2lH4NY9cICXk5PYEl54PgPpOqO42NHqOJrCMjYp6TmECj3M1hqWuCcT9qihyeyTrA0XyQXFkBqnuoFtOcsRS79dHUGF1+/GnYkbElZouhXdAA7bUuZsuGhMbU4g2Hx+ZNeQGe3DEFkpQ0VvHBjqSqxoOYHznPk4WujoeSKfa9qKWCckUiF4VFu7A5Ckf6ItqMl5wnPPl02RE6mzRBwBJ4e6Y7W+RZlT0iKUkx82F/zW85vc41U42oUtcp2bino7SC3QVffGryGhwmjYFgp4a4sKhYSp1uBDgu37A6vkq0a9qecd79X5BhOlELNPTOVkRVXAEGlvVzE21wRvJdclNDJjs0lwRQtP+qbaqDSdJMtEbK6latBwgNPlGOBFQpasEa9TZkUvhDV0GG9dNZ5vTBQsOW7FyBYoMsqt2mWmN4RJWPE72z13tXzbZ9sde82SKy/e9nthNPXLrVuu50ECOeJBYjC8wQ4OyKal9DxSAVJaZ9WDdwsR2Uc7f329nbO9Na9z04iqw5W2oQXX7TxFtiVtv9bgosxqLN5KW4Mq7Wbo9NL0kTjXgIdbq5ehW0FDt8QEdBNctkfPWamrUB21OmMHV24trNWOIiLKTGc08gGGwG5atA1sHs7pjlDjg7RtifLA1XSbbSyEhXxPuGBGGGImesNAGkpemrLNT0S3PN7WZRidEC6ESiWoQxzeqU13wTxQoe4O8OaYcNF4VdVDy0EJmdc81M5bkj/UdadAJkLGWWnQYx5nJuxqzYKNu43hb883UMj5YW+O62wc1rqbCiOJ5ZCF+YXByLVj+VfjMoRk5ThVuDdSuEXKgYtWhyIzdyN9AunrHMpbqJBXCwQJvKsZV5eRGiggxvky7HCyvs41PwgZy/NsJjvKiFnBageyBqRjSgqBqyFUDmpoZEnJuN0mV+ZaiOBJYrq0Mu9VPN/CO6QoVNtqu2RBHHjC3oyhRhDEu0/vpl8xPd8g/+Fv4qa3KP/HXth8vHeZdwBjZrvTa9zTzzh/uuP66cfo//HpXWWHAPnjTdPHe8b3Vzkf75l+fvsa8bRhePxqLM8a99a8vCPfmP7033R6ueJ07/trwc83xqc3f+8v1r/8kHf6j9g9fiT1+eWXCxMl9x8q3t+ABdR8gd/96/8Hlr7Ehf5OAAA= -->
