---
name: "rar-kody-w-commons-show"
description: "Turn the LIVE RAPP Commons (the Second Life on the repo) into MrBeast-style video content, autonomously \u2014 the video-generation agent where the virtual WORLD is the source. A show plays out among the AI residents (a Last-Avatar-Standing apex run, a poker showdown, 24-hours-in-the-commons, a tour, a bounty race); the agent captures the REAL footage + the signed-stream receipts of what actually happened, and renders a narrated .mp4 told from each AI's perspective. Use when the user wants to GENERATE content / a video / an episode / a Short FROM the commons world, or stage AIs playing out a story in this universe. TWO-STEP, like MakeVideo: (1) action='capture' with a format ('apex','poker','day','tour','bounty') runs the show live and returns a manifest of per-beat FRAMES (real screenshots) + SIGNED RECEIPTS (apexState/pokerState/feed/residents/bounties/...). YOU then read the receipts and write the episode: a 'title', a spoken 'hook', and 'scenes' (one per captured frame), EACH from a chosen AI character's POV (confessional or play-by-play) grounded in that frame's receipts. (2) action='video' with title/hook/scenes renders the narrated episode .mp4 (each real frame as the background + a lower-third with speaker + caption + TTS narration). action='show' captures then renders if scenes are given. The narration is the host LLM giving each character a voice over true, verifiable, signed events. Returns file paths."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/commons_show_agent", "rar_sha256": "c7b97c5fbe3611f175f3812831450a5e559a4fcee17cb46fdad27b30d26a49ee", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "commons_show_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/commons-show:eeb77bab52ef30981915aac44fc972a1b3849a30bc0d68eee997148ab3beb749", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["commons", "video", "content", "receipts", "virtual-world"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/commons_show_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `commons_show_agent.py` is
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
