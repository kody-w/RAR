---
name: "rar-kody-w-commons-show"
description: "Turn the LIVE RAPP Commons (the Second Life on the repo) into MrBeast-style video content, autonomously \u2014 the video-generation agent where the virtual WORLD is the source. A show plays out among the AI residents (a Last-Avatar-Standing apex run, a poker showdown, 24-hours-in-the-commons, a tour, a bounty race); the agent captures the REAL footage + the signed-stream receipts of what actually happened, and renders a narrated .mp4 told from each AI's perspective. Use when the user wants to GENERATE content / a video / an episode / a Short FROM the commons world, or stage AIs playing out a story in this universe. TWO-STEP, like MakeVideo: (1) action='capture' with a format ('apex','poker','day','tour','bounty') runs the show live and returns a manifest of per-beat FRAMES (real screenshots) + SIGNED RECEIPTS (apexState/pokerState/feed/residents/bounties/...). YOU then read the receipts and write the episode: a 'title', a spoken 'hook', and 'scenes' (one per captured frame), EACH from a chosen AI character's POV (confessional or play-by-play) grounded in that frame's receipts. (2) action='video' with title/hook/scenes renders the narrated episode .mp4 (each real frame as the background + a lower-third with speaker + caption + TTS narration). action='show' captures then renders if scenes are given. The narration is the host LLM giving each character a voice over true, verifiable, signed events. Returns file paths."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/commons_show_agent", "rar_sha256": "c7b97c5fbe3611f175f3812831450a5e559a4fcee17cb46fdad27b30d26a49ee", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["commons", "video", "content", "receipts", "virtual-world"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/commons_show_agent`. The original RAPP
agent is preserved byte-for-byte in `commons_show_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "capture = run the show + return footage/receipts to narrate; video = render the .mp4 from captured frames + your scenes; show = capture then render if scenes given. Default capture.",
      "enum": [
        "capture",
        "video",
        "show"
      ],
      "type": "string"
    },
    "episode": {
      "description": "Optional episode number / beat-count cap for capture.",
      "type": "integer"
    },
    "format": {
      "description": "Which show to stage in the commons. apex=Last Avatar Standing (co-op elimination); poker=signed Hold'em showdown; day=24 hours via the day-night clock; tour=every venue; bounty=the signed job-market race. Default apex.",
      "enum": [
        "apex",
        "poker",
        "day",
        "tour",
        "bounty"
      ],
      "type": "string"
    },
    "hook": {
      "description": "Spoken opener (~8-15s) over the title card \u2014 a scroll-stopping MrBeast-style premise.",
      "type": "string"
    },
    "scenes": {
      "description": "One per captured frame, in order. Each: {frame (int index into the manifest frames), speaker (the AI character whose POV this is, e.g. 'Pip'), kicker (short label like 'CONFESSIONAL' or 'PLAY-BY-PLAY'), caption (punchy on-screen headline), narration (1-3 spoken sentences from that character's POV, grounded in the frame's receipts)}.",
      "items": {
        "properties": {
          "caption": {
            "type": "string"
          },
          "frame": {
            "type": "integer"
          },
          "kicker": {
            "type": "string"
          },
          "narration": {
            "type": "string"
          },
          "speaker": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "slug": {
      "description": "Optional output folder slug (defaults from the title).",
      "type": "string"
    },
    "title": {
      "description": "Episode title (the big title card). For action=video/show with scenes.",
      "type": "string"
    },
    "url": {
      "description": "Optional commons URL (default the live Pages site).",
      "type": "string"
    },
    "voice": {
      "description": "Optional macOS 'say' voice for narration (e.g. 'Ava','Tom').",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `commons_show_agent.py` and embedded as the fenced Python below (sha256 c7b97c5fbe3611f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `commons_show_agent.py` first:

```bash
python3 commons_show_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 commons_show_agent.py   # or on stdin
python3 commons_show_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
    "version": "1.0.1",
    "display_name": "Commons Show",
    "description": "Captures staged shows in the live RAPP Commons via Playwright and renders narrated MP4 episodes with TTS, rsvg-convert, and ffmpeg.",
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
