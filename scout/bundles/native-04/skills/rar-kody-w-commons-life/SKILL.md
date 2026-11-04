---
name: "rar-kody-w-commons-life"
description: "Record, GROW, and PLAY the life of the commons as a digital organism, cradle to grave. The commons is a living world whose residents (each a signing rappid) are born, wander, play, bond, and persist; this agent records its life as frozen frames (full signed save-states at a chosen frame resolution), grows the fidelity between frames with the EZsharpen dream-catcher pattern (filling motion that never contradicts the signed record), and emits a LIFEPLAYER \u2014 an HTML scrubber that spins/plays the grown life back, cradle to grave, with the signed events ticking past like vitals. Use when the user wants to record/play/scrub the commons' life, watch the organism live at full fidelity, or produce a playable timeline of the world. ACTION 'life' (default) does the whole pipeline: record (params 'interval' seconds between frames = the resolution, 'duration' seconds total) -> grow (EZsharpen, 'subdivide' finer sub-frames) -> emit the LifePlayer HTML and return its path. 'record' just captures the life frames; 'grow' grows an existing recording; 'play' emits the player for an existing one. Higher frame resolution + more subdivision = higher-fidelity life. Returns file paths to open."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/commons_life_agent", "rar_sha256": "4d130862e28b92a3a3519a8b823905bffb90f35678565bb1743a714f20d0da70", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["commons", "frames", "playback", "lifeplayer", "digital-organism"]}
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

<!-- rci-capsule:v1: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 -->
