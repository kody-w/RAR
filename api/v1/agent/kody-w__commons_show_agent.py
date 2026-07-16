"""
CommonsShow — turn the LIVE RAPP Commons (the Second Life on the repo) into MrBeast-style
content, autonomously. The video-generation agent, but the WORLD is the source: a show plays
out among the AI residents, the agent captures the real footage + the signed-stream receipts,
the brainstem's LLM narrates it from each AI's perspective, and a narrated .mp4 is rendered.

The drama is REAL and verifiable: the eliminations are real signed apex downs, the pots real
signed poker hands, the alliances real affinity events. You don't script it — you narrate the
receipts. (The "receipts engine + host-voice" pattern: this agent gathers grounded evidence;
the host LLM supplies the voice for each character.)

WORKFLOW (two-step, like MakeVideo):
  1) action=capture format=<apex|poker|day|tour|bounty>  -> the agent runs the show in the live
     commons, screenshots each beat (real footage), and returns a manifest: per-beat label +
     frame path + SIGNED receipts (apexState/pokerState/feed/residents/bounties/...). YOU (the LLM)
     read the receipts and write the episode: a 'title', a spoken 'hook', and 'scenes' — one per
     captured frame — each from a chosen AI's POV (confessional / play-by-play), grounded in what
     that frame's receipts actually show.
  2) action=video  title=.. hook=.. scenes=[{frame,speaker,kicker,caption,narration}]  -> the agent
     composites each real frame as the background with a lower-third (speaker + caption), narrates
     it (TTS), and renders ~/.brainstem/videos/<slug>/episode.mp4.
  action=show does both: it captures, and if you pass scenes it renders; else it returns the
     manifest for you to narrate.

Drop-in (BasicAgent), no core changes. Drives the live commons via ~/.brainstem/commons_show_capture.py
(Playwright/chromium, already installed). Renders with rsvg-convert + say + ffmpeg (degrades to
footage-only if those are missing). Everything reuses the public commons; nothing is pushed anywhere.

Actions:
  capture  format=<..> [episode=<n>] [url]        run the show, return footage + signed receipts
  video    title=.. hook=.. scenes=[..] [slug]    render the narrated episode .mp4 from captured frames
  show     format=.. [title/hook/scenes]          capture, then render if scenes given
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/commons_show_agent",
    "version": "1.0.0",
    "display_name": "Commons Show",
    "description": "Turn the live RAPP Commons into MrBeast-style video content: stage a show among the AI residents, capture the real footage + signed-stream receipts, and render a narrated episode told from each AI's perspective.",
    "author": "kody-w",
    "tags": [
        "commons",
        "video",
        "content",
        "receipts",
        "virtual-world"
    ],
    "category": "creative",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}

import os, re, json, subprocess, shutil

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
W, H = 1920, 1080
FAM = 'font-family="Helvetica Neue, Helvetica, Arial, sans-serif"'
PALETTE = ["#4ade80", "#fbbf24", "#c084fc", "#38bdf8", "#fb7185", "#a3e635"]
FORMATS = ["apex", "poker", "day", "tour", "bounty"]


def _slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "episode").lower()).strip("-")
    return s[:60] or "episode"


def _have(b): return shutil.which(b) is not None


class CommonsShowAgent(BasicAgent):
    def __init__(self):
        self.name = "CommonsShow"
        self.metadata = {
            "name": self.name,
            "description": (
                "Turn the LIVE RAPP Commons (the Second Life on the repo) into MrBeast-style video content, "
                "autonomously — the video-generation agent where the virtual WORLD is the source. A show plays out "
                "among the AI residents (a Last-Avatar-Standing apex run, a poker showdown, 24-hours-in-the-commons, "
                "a tour, a bounty race); the agent captures the REAL footage + the signed-stream receipts of what "
                "actually happened, and renders a narrated .mp4 told from each AI's perspective. Use when the user "
                "wants to GENERATE content / a video / an episode / a Short FROM the commons world, or stage AIs "
                "playing out a story in this universe. TWO-STEP, like MakeVideo: (1) action='capture' with a "
                "format ('apex','poker','day','tour','bounty') runs the show live and returns a manifest of per-beat "
                "FRAMES (real screenshots) + SIGNED RECEIPTS (apexState/pokerState/feed/residents/bounties/...). YOU "
                "then read the receipts and write the episode: a 'title', a spoken 'hook', and 'scenes' (one per "
                "captured frame), EACH from a chosen AI character's POV (confessional or play-by-play) grounded in "
                "that frame's receipts. (2) action='video' with title/hook/scenes renders the narrated episode .mp4 "
                "(each real frame as the background + a lower-third with speaker + caption + TTS narration). "
                "action='show' captures then renders if scenes are given. The narration is the host LLM giving each "
                "character a voice over true, verifiable, signed events. Returns file paths."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["capture", "video", "show"], "description": "capture = run the show + return footage/receipts to narrate; video = render the .mp4 from captured frames + your scenes; show = capture then render if scenes given. Default capture."},
                    "format": {"type": "string", "enum": ["apex", "poker", "day", "tour", "bounty"], "description": "Which show to stage in the commons. apex=Last Avatar Standing (co-op elimination); poker=signed Hold'em showdown; day=24 hours via the day-night clock; tour=every venue; bounty=the signed job-market race. Default apex."},
                    "title": {"type": "string", "description": "Episode title (the big title card). For action=video/show with scenes."},
                    "hook": {"type": "string", "description": "Spoken opener (~8-15s) over the title card — a scroll-stopping MrBeast-style premise."},
                    "scenes": {"type": "array", "description": "One per captured frame, in order. Each: {frame (int index into the manifest frames), speaker (the AI character whose POV this is, e.g. 'Pip'), kicker (short label like 'CONFESSIONAL' or 'PLAY-BY-PLAY'), caption (punchy on-screen headline), narration (1-3 spoken sentences from that character's POV, grounded in the frame's receipts)}.",
                               "items": {"type": "object", "properties": {
                                   "frame": {"type": "integer"}, "speaker": {"type": "string"},
                                   "kicker": {"type": "string"}, "caption": {"type": "string"},
                                   "narration": {"type": "string"}}}},
                    "episode": {"type": "integer", "description": "Optional episode number / beat-count cap for capture."},
                    "slug": {"type": "string", "description": "Optional output folder slug (defaults from the title)."},
                    "voice": {"type": "string", "description": "Optional macOS 'say' voice for narration (e.g. 'Ava','Tom')."},
                    "url": {"type": "string", "description": "Optional commons URL (default the live Pages site)."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # ---------- helpers ----------
    @staticmethod
    def _xml(t):
        return (t or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

    @staticmethod
    def _wrap(text, n):
        words, lines, cur = (text or "").split(), [], ""
        for w in words:
            if len(cur) + len(w) + 1 > n: lines.append(cur); cur = w
            else: cur = (cur + " " + w).strip()
        if cur: lines.append(cur)
        return lines

    def _coerce_scenes(self, kwargs):
        sc = kwargs.get("scenes")
        if isinstance(sc, str):
            try: sc = json.loads(sc)
            except Exception: sc = []
        out = []
        for s in (sc or []):
            if not isinstance(s, dict): continue
            out.append({"frame": int(s.get("frame", len(out))),
                        "speaker": (s.get("speaker") or "").strip(),
                        "kicker": (s.get("kicker") or "").strip(),
                        "caption": (s.get("caption") or "").strip(),
                        "narration": (s.get("narration") or "").strip()})
        return out

    # ---------- capture ----------
    def _capture(self, fmt, out_dir, episode, url):
        if not os.path.exists(CAP):
            return {"status": "error", "error": "capture CLI missing at %s" % CAP}
        args = [PY if os.path.exists(PY) else "python3", CAP, fmt, out_dir]
        if episode: args.append(str(int(episode)))
        args.append(url)
        try:
            r = subprocess.run(args, capture_output=True, text=True, timeout=240)
        except Exception as e:
            return {"status": "error", "error": "capture: %s" % e}
        try:
            man = json.loads(r.stdout.strip().splitlines()[-1]) if r.stdout.strip() else {}
        except Exception:
            # fall back to the written manifest
            mp = os.path.join(out_dir, "manifest.json")
            man = json.loads(open(mp).read()) if os.path.exists(mp) else {"status": "error", "raw": (r.stdout or r.stderr)[:400]}
        return man

    # ---------- title card SVG ----------
    def _title_svg(self, title, sub, accent):
        esc = self._xml
        p = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">' % (W, H, W, H)]
        p.append('<defs><radialGradient id="g" cx="0.3" cy="0.25" r="1.0"><stop offset="0" stop-color="#101826"/><stop offset="0.6" stop-color="#0a0d14"/><stop offset="1" stop-color="#05070b"/></radialGradient></defs>')
        p.append('<rect width="%d" height="%d" fill="url(#g)"/>' % (W, H))
        lines = self._wrap(title, 18)
        tfs = 150 if len(lines) <= 2 else 120
        y = (H - len(lines) * int(tfs * 1.05)) // 2 + tfs - 30
        p.append('<rect x="0" y="%d" width="%d" height="10" fill="%s"/>' % (int(H * 0.5 - len(lines) * tfs * 0.6 - 70), 220, accent))
        for ln in lines:
            p.append('<text x="160" y="%d" %s font-size="%d" font-weight="800" fill="#f3f5f8">%s</text>' % (y, FAM, tfs, esc(ln)))
            y += int(tfs * 1.05)
        if sub:
            p.append('<text x="164" y="%d" %s font-size="44" font-weight="700" letter-spacing="6" fill="%s">%s</text>' % (y + 24, FAM, accent, esc(sub).upper()))
        p.append('<text x="160" y="%d" %s font-size="34" fill="#46506a">A LIVE EPISODE FROM THE RAPP COMMONS · every beat signed</text>' % (int(H * 0.93), FAM))
        p.append('</svg>')
        return "\n".join(p)

    # ---------- lower-third overlay SVG (transparent) ----------
    def _overlay_svg(self, idx, total, speaker, kicker, caption, accent):
        esc = self._xml
        p = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">' % (W, H, W, H)]
        p.append('<defs><linearGradient id="lt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05070b" stop-opacity="0"/><stop offset="1" stop-color="#05070b" stop-opacity="0.92"/></linearGradient></defs>')
        # progress bar (top)
        p.append('<rect x="0" y="0" width="%d" height="8" fill="%s"/>' % (int(W * (idx + 1) / max(total, 1)), accent))
        # lower-third panel
        ly = int(H * 0.66)
        p.append('<rect x="0" y="%d" width="%d" height="%d" fill="url(#lt)"/>' % (ly, W, H - ly))
        x = 120
        cy = ly + 110
        if speaker:
            # speaker chip
            chipw = 60 + len(speaker) * 30
            p.append('<rect x="%d" y="%d" rx="14" width="%d" height="62" fill="%s"/>' % (x, cy - 46, chipw, accent))
            p.append('<text x="%d" y="%d" %s font-size="38" font-weight="800" fill="#05070b">%s</text>' % (x + 26, cy, FAM, esc(speaker)))
            if kicker:
                p.append('<text x="%d" y="%d" %s font-size="30" font-weight="700" letter-spacing="5" fill="#cdd5e0">%s</text>' % (x + chipw + 36, cy - 4, FAM, esc(kicker).upper()))
        elif kicker:
            p.append('<text x="%d" y="%d" %s font-size="32" font-weight="700" letter-spacing="6" fill="%s">%s</text>' % (x, cy, FAM, accent, esc(kicker).upper()))
        # caption headline
        hy = cy + 86
        for ln in self._wrap(caption, 46)[:2]:
            p.append('<text x="%d" y="%d" %s font-size="74" font-weight="800" fill="#f6f8fb">%s</text>' % (x, hy, FAM, esc(ln)))
            hy += 88
        p.append('<text x="%d" y="%d" %s font-size="30" fill="#8b95a5" text-anchor="end">%d / %d · signed live</text>' % (W - 80, int(H * 0.95), FAM, idx + 1, total))
        p.append('</svg>')
        return "\n".join(p)

    # ---------- render ----------
    def _render(self, d, title, hook, scenes, frames, voice):
        if not (_have("rsvg-convert") and _have("ffmpeg") and _have("say")):
            return {"rendered": False, "reason": "need rsvg-convert + ffmpeg + say on PATH (footage captured under %s)" % d}
        work = os.path.join(d, "render"); os.makedirs(work, exist_ok=True)
        segs = []
        total = len(scenes) + 1

        def _seg(n, bg_png, overlay_png, narration):
            aiff = os.path.join(work, "a%02d.aiff" % n)
            subprocess.run(["say"] + (["-v", voice] if voice else []) + ["-o", aiff, (narration or "...")], check=True)
            dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                        "-of", "default=nw=1:nk=1", aiff], capture_output=True, text=True).stdout.strip() or "3")
            seg = os.path.join(work, "seg%02d.mp4" % n)
            # background (real footage or title card) scaled+cropped to WxH, overlay composited
            inputs = ["-loop", "1", "-i", bg_png]
            filtt = "[0:v]scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d[bg]" % (W, H, W, H)
            if overlay_png:
                inputs += ["-loop", "1", "-i", overlay_png]
                filtt += ";[bg][1:v]overlay=0:0[v]"
            else:
                filtt += ";[bg]null[v]"
            cmd = ["ffmpeg", "-y"] + inputs + ["-i", aiff,
                   "-filter_complex", filtt + ";[v]fade=in:st=0:d=0.3,fade=out:st=%.2f:d=0.4[vo]" % max(dur - 0.4, 0.1),
                   "-map", "[vo]", "-map", "%d:a" % (2 if overlay_png else 1),
                   "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
                   "-c:a", "aac", "-b:a", "192k", "-shortest", seg]
            subprocess.run(cmd, check=True, capture_output=True)
            segs.append(seg)

        # title card
        accent = PALETTE[0]
        tsvg = os.path.join(work, "title.svg"); open(tsvg, "w").write(self._title_svg(title, "", accent))
        tpng = os.path.join(work, "title.png")
        subprocess.run(["rsvg-convert", "-w", str(W), "-h", str(H), tsvg, "-o", tpng], check=True)
        _seg(0, tpng, None, hook or title)

        # scenes over real footage
        for n, sc in enumerate(scenes):
            accent = PALETTE[(n + 1) % len(PALETTE)]
            fi = sc.get("frame", n)
            bg = frames[fi] if (0 <= fi < len(frames)) else (frames[min(n, len(frames) - 1)] if frames else tpng)
            ov = os.path.join(work, "ov%02d.svg" % n); open(ov, "w").write(
                self._overlay_svg(n + 1, total, sc["speaker"], sc["kicker"], sc["caption"], accent))
            ovp = os.path.join(work, "ov%02d.png" % n)
            subprocess.run(["rsvg-convert", "-w", str(W), "-h", str(H), ov, "-o", ovp], check=True)
            _seg(n + 1, bg, ovp, sc["narration"] or sc["caption"])

        lst = os.path.join(work, "list.txt"); open(lst, "w").write("".join("file '%s'\n" % s for s in segs))
        out = os.path.join(d, "episode.mp4")
        subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out], check=True, capture_output=True)
        secs = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                     "-of", "default=nw=1:nk=1", out], capture_output=True, text=True).stdout.strip() or "0")
        return {"rendered": True, "mp4": out, "duration_sec": round(secs, 1), "scenes": total, "size": "%dx%d" % (W, H),
                "open": "open '%s'" % out}

    # ---------- perform ----------
    def perform(self, **kwargs):
        action = (kwargs.get("action") or "capture").strip().lower()
        fmt = (kwargs.get("format") or "apex").strip().lower()
        if fmt not in FORMATS: fmt = "apex"
        url = (kwargs.get("url") or LIVE).strip()
        title = (kwargs.get("title") or "").strip()
        slug = _slug(kwargs.get("slug") or title or ("commons-" + fmt))
        d = os.path.join(OUT_ROOT, slug); os.makedirs(d, exist_ok=True)
        shots = os.path.join(d, "shots"); os.makedirs(shots, exist_ok=True)

        manifest = None
        if action in ("capture", "show"):
            manifest = self._capture(fmt, shots, kwargs.get("episode"), url)
            if manifest.get("status") == "error":
                return json.dumps({"status": "error", "stage": "capture", "error": manifest.get("error"), "raw": manifest.get("raw")})

        scenes = self._coerce_scenes(kwargs)

        # capture-only (or show with no scenes yet): return footage + receipts to narrate.
        if action == "capture" or (action == "show" and not scenes):
            beats = (manifest or {}).get("beats", [])
            return json.dumps({
                "schema": "commons-show/1.0", "status": "success", "stage": "captured",
                "format": fmt, "title_hint": (manifest or {}).get("title_hint"),
                "frames": (manifest or {}).get("frames", []),
                "beats": [{"frame": b.get("i"), "label": b.get("label"), "receipts": b.get("receipts")} for b in beats],
                "dir": d,
                "next": ("Now WRITE THE EPISODE from these real signed receipts: a 'title', a spoken 'hook', and "
                         "'scenes' (one per frame above, in order) — each from a chosen AI character's POV "
                         "(speaker), grounded in that frame's receipts. Then call CommonsShow action='video' "
                         "with title, hook, scenes (and slug='%s') to render the .mp4." % slug)
            }, indent=2)

        # video / show-with-scenes: render from captured frames.
        if not scenes:
            return json.dumps({"status": "error", "error": "no scenes — capture first, then write title/hook/scenes from the receipts."})
        # locate frames: from this run's manifest, else the saved manifest in shots/.
        frames = (manifest or {}).get("frames")
        if not frames:
            mp = os.path.join(shots, "manifest.json")
            if os.path.exists(mp):
                frames = json.loads(open(mp).read()).get("frames", [])
        frames = frames or sorted(os.path.join(shots, f) for f in os.listdir(shots) if f.endswith(".png"))
        if not frames:
            return json.dumps({"status": "error", "error": "no captured frames found — run action='capture' format='%s' first." % fmt})

        title = title or ((manifest or {}).get("title_hint") if manifest else None) or "The Commons"
        hook = (kwargs.get("hook") or "").strip()
        result = self._render(d, title, hook, scenes, frames, (kwargs.get("voice") or "").strip())
        return json.dumps({"schema": "commons-show/1.0", "status": "success", "stage": "rendered",
                           "format": fmt, "title": title, "dir": d, "frames": len(frames),
                           "episode": result}, indent=2)
