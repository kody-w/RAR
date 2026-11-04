---
name: "rar-kody-w-commons-show"
description: "Turn the LIVE RAPP Commons (the Second Life on the repo) into MrBeast-style video content, autonomously \u2014 the video-generation agent where the virtual WORLD is the source. A show plays out among the AI residents (a Last-Avatar-Standing apex run, a poker showdown, 24-hours-in-the-commons, a tour, a bounty race); the agent captures the REAL footage + the signed-stream receipts of what actually happened, and renders a narrated .mp4 told from each AI's perspective. Use when the user wants to GENERATE content / a video / an episode / a Short FROM the commons world, or stage AIs playing out a story in this universe. TWO-STEP, like MakeVideo: (1) action='capture' with a format ('apex','poker','day','tour','bounty') runs the show live and returns a manifest of per-beat FRAMES (real screenshots) + SIGNED RECEIPTS (apexState/pokerState/feed/residents/bounties/...). YOU then read the receipts and write the episode: a 'title', a spoken 'hook', and 'scenes' (one per captured frame), EACH from a chosen AI character's POV (confessional or play-by-play) grounded in that frame's receipts. (2) action='video' with title/hook/scenes renders the narrated episode .mp4 (each real frame as the background + a lower-third with speaker + caption + TTS narration). action='show' captures then renders if scenes are given. The narration is the host LLM giving each character a voice over true, verifiable, signed events. Returns file paths."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/commons_show_agent", "rar_sha256": "9287c090fce8d7a702aaddcb1223ea739ee2ac8988048239b7f78d16e8d94a0f", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["commons", "video", "content", "receipts", "virtual-world"]}
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
