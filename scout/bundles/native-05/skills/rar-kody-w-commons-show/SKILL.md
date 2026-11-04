---
name: "rar-kody-w-commons-show"
description: "Turn the LIVE RAPP Commons (the Second Life on the repo) into MrBeast-style video content, autonomously \u2014 the video-generation agent where the virtual WORLD is the source. A show plays out among the AI residents (a Last-Avatar-Standing apex run, a poker showdown, 24-hours-in-the-commons, a tour, a bounty race); the agent captures the REAL footage + the signed-stream receipts of what actually happened, and renders a narrated .mp4 told from each AI's perspective. Use when the user wants to GENERATE content / a video / an episode / a Short FROM the commons world, or stage AIs playing out a story in this universe. TWO-STEP, like MakeVideo: (1) action='capture' with a format ('apex','poker','day','tour','bounty') runs the show live and returns a manifest of per-beat FRAMES (real screenshots) + SIGNED RECEIPTS (apexState/pokerState/feed/residents/bounties/...). YOU then read the receipts and write the episode: a 'title', a spoken 'hook', and 'scenes' (one per captured frame), EACH from a chosen AI character's POV (confessional or play-by-play) grounded in that frame's receipts. (2) action='video' with title/hook/scenes renders the narrated episode .mp4 (each real frame as the background + a lower-third with speaker + caption + TTS narration). action='show' captures then renders if scenes are given. The narration is the host LLM giving each character a voice over true, verifiable, signed events. Returns file paths."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/commons_show_agent", "rar_sha256": "9287c090fce8d7a702aaddcb1223ea739ee2ac8988048239b7f78d16e8d94a0f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["commons", "video", "content", "receipts", "virtual-world"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `commons_show_agent.py` and embedded as the fenced Python below (sha256 9287c090fce8d7a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `commons_show_agent.py` first:

```bash
python3 commons_show_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 commons_show_agent.py   # or on stdin
python3 commons_show_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/commons_show_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/commons_show_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/commons_show_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
