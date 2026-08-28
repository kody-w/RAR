"""Education Shorts — turn a topic into an animated 9:16 educational YouTube Short.

Drives kody-w/rapp-education-shorts (public, MIT): brief → SCRIPT.json → HyperFrames
composition → `hyperframes check` → MP4, every stage a file and a ledger entry.

The brainstem's own model can be the writer: call with action="brief" to get the
script contract for a topic, then call action="once" with the script JSON you wrote
(no Copilot CLI needed). If the GitHub Copilot CLI is on PATH, action="once" with
only a topic lets the pack's confined model (no tools) write it instead.

Prereqs on the machine: git, python3 (3.9+), Node/npx (the HyperFrames renderer is
fetched by npx and pinned per project). No secrets, no environment variables.
The pack is cloned on first use into ~/.rapp/education-shorts/pack; shorts land in
~/.rapp/education-shorts/shorts/<slug>/ (override with EDUCATION_SHORTS_HOME).
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/education_shorts_agent",
    "version": "1.0.0",
    "display_name": "Education Shorts",
    "description": (
        "Turns a topic into an animated 9:16 educational YouTube Short: linted script, "
        "HyperFrames composition, check, MP4 — every stage a file on a chained ledger."
    ),
    "author": "Kody Wildfeuer",
    "tags": ["video", "youtube-shorts", "hyperframes", "animation", "education", "creative"],
    "category": "creative",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "external_prereqs": [
        "git",
        "Node.js with npx (HyperFrames renderer, pinned per project)",
        "optional: GitHub Copilot CLI on PATH, if you want the pack's model to write scripts",
    ],
    "example_call": {
        "args": {"action": "once", "slug": "sky", "topic": "Why is the sky blue?", "theme": "midnight"}
    },
}

PACK_REPO = "https://github.com/kody-w/rapp-education-shorts"
ACTIONS = ("setup", "brief", "once", "script", "compose", "check", "render", "status", "list", "verify")
THEMES = ("midnight", "ember", "forest", "paper", "ocean")


def _home():
    raw = os.environ.get("EDUCATION_SHORTS_HOME", "").strip()
    return Path(raw).expanduser() if raw else Path.home() / ".rapp" / "education-shorts"


class EducationShorts(BasicAgent):
    def __init__(self):
        self.name = "EducationShorts"
        self.metadata = {
            "name": self.name,
            "description": (
                "Make an animated educational YouTube Short (9:16, text-forward, sound-off friendly) "
                "from a topic. Flow: action='brief' with a topic returns the script contract and a word "
                "budget — write the script JSON yourself and call action='once' with slug, topic and "
                "script (renders an MP4). Or, with the Copilot CLI installed, action='once' with just a "
                "topic. Also: status/list/verify, and compose/check/render one stage at a time. Use for "
                "anything about making a Short, an explainer video, an animated lesson or a TikTok-style "
                "educational clip."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": list(ACTIONS), "description": "What to do. Default: status."},
                    "slug": {"type": "string", "description": "Short id, e.g. 'why-sky-blue' (lowercase, hyphens)."},
                    "topic": {"type": "string", "description": "What the Short teaches (one sentence)."},
                    "audience": {"type": "string", "description": "Who it is for, e.g. 'curious teens'."},
                    "tone": {"type": "string", "description": "e.g. 'clear, warm, a little playful'."},
                    "notes": {"type": "string", "description": "Anything the writer must include or avoid."},
                    "theme": {"type": "string", "enum": list(THEMES), "description": "Palette. Default: hashed from slug."},
                    "script": {"type": "object", "description": (
                        "A rapp-education-short/1.0 script object (from action='brief'): title, topic, chip, "
                        "scenes[] with kind/heading/lines/visual/emphasis. If given, YOU are the writer.")},
                    "quality": {"type": "string", "enum": ["draft", "high"], "description": "Render quality. Default high."},
                    "skip_render": {"type": "boolean", "description": "Stop after compose + check (no MP4)."},
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── plumbing ─────────────────────────────────────────────────────────
    def _pack(self):
        pack = _home() / "pack"
        if (pack / "shorts.py").exists():
            return pack, None
        if not shutil.which("git"):
            return None, "git is required to fetch %s" % PACK_REPO
        pack.parent.mkdir(parents=True, exist_ok=True)
        try:
            r = subprocess.run(["git", "clone", "--depth", "1", PACK_REPO, str(pack)], capture_output=True,
                               text=True, timeout=300, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            return None, "git clone timed out"
        if r.returncode != 0 or not (pack / "shorts.py").exists():
            return None, "could not clone %s: %s" % (PACK_REPO, (r.stderr or "")[-300:].strip())
        return pack, None

    def _cli(self, pack, args, timeout=1800):
        root = _home() / "shorts"
        root.mkdir(parents=True, exist_ok=True)
        try:
            r = subprocess.run([sys.executable, str(pack / "shorts.py"), "--root", str(root)] + args,
                               capture_output=True, text=True, timeout=timeout, cwd=str(pack),
                               stdin=subprocess.DEVNULL, env=dict(os.environ, NO_COLOR="1"))
        except subprocess.TimeoutExpired:
            return {"status": "error", "message": "timed out after %ss" % timeout}
        out = (r.stdout or "").strip()
        try:
            data = json.loads(out) if out else {}
        except Exception:
            data = {"raw": out[-2000:]}
        if r.returncode not in (0, 2) and not out:
            return {"status": "error", "message": (r.stderr or "")[-600:].strip() or "shorts.py failed"}
        return {"status": "success" if r.returncode == 0 else "error", "result": data}

    @staticmethod
    def _contract(pack):
        try:
            sys.path.insert(0, str(pack))
            from eshorts import script as S  # noqa: WPS433
            return {"schema": S.SCHEMA_SCRIPT, "kinds": ("hook", "point", "steps", "compare", "number", "quote", "recap", "cta"),
                    "limits": {"scenes": "%d-%d" % (S.MIN_SCENES, S.MAX_SCENES), "heading_chars": S.MAX_HEADING_CHARS,
                               "line_words": S.MAX_LINE_WORDS, "lines_per_scene": S.MAX_LINES,
                               "total_words": S.MAX_TOTAL_WORDS, "seconds": S.MAX_TOTAL_S},
                    "shape": {"schema": S.SCHEMA_SCRIPT, "title": "...", "topic": "...", "chip": "1-3 word series label",
                              "hashtags": ["#..."], "scenes": [
                                  {"kind": "hook", "heading": "punchy question <= 9 words", "lines": ["subtitle <= 10 words"], "emphasis": ["word"]},
                                  {"kind": "point", "heading": "...", "lines": ["...", "..."], "emphasis": ["word"]},
                                  {"kind": "steps", "heading": "...", "lines": [], "visual": {"type": "steps", "items": ["...", "...", "..."]}},
                                  {"kind": "compare", "heading": "...", "lines": ["one line"], "visual": {"type": "compare", "left": "...", "right": "..."}},
                                  {"kind": "number", "heading": "...", "lines": [], "visual": {"type": "number", "value": "70%", "caption": "..."}},
                                  {"kind": "quote", "heading": "...", "lines": ["the quote", "— who"]},
                                  {"kind": "recap", "heading": "...", "lines": ["...", "...", "..."]},
                                  {"kind": "cta", "heading": "...", "lines": ["..."], "visual": {"type": "pill", "text": "Follow for more"}}]},
                    "rules": ["scene 1 is a hook; last scene is recap or cta", "no URLs/handles in text",
                              "timing is derived from words — respect the total word budget", "use 5-8 scenes"]}
        except Exception as e:  # pragma: no cover
            return {"error": "%s: %s" % (type(e).__name__, e)}
        finally:
            try:
                sys.path.remove(str(pack))
            except ValueError:
                pass

    # ── perform ──────────────────────────────────────────────────────────
    def perform(self, **kwargs) -> str:
        action = (kwargs.get("action") or "status").strip().lower()
        if action not in ACTIONS:
            return json.dumps({"status": "error", "message": "unknown action %r; one of %s" % (action, ", ".join(ACTIONS))})
        pack, err = self._pack()
        if err:
            return json.dumps({"status": "error", "message": err})
        try:
            if action == "setup":
                node = shutil.which("npx") or shutil.which("hyperframes")
                return json.dumps({"status": "success", "pack": str(pack), "shorts_root": str(_home() / "shorts"),
                                   "renderer": node or "MISSING — install Node.js (npx) for check/render",
                                   "copilot_cli": bool(shutil.which("copilot"))})
            if action == "brief":
                topic = (kwargs.get("topic") or "").strip()
                if not topic:
                    return json.dumps({"status": "error", "message": "brief needs a topic"})
                return json.dumps({"status": "success", "topic": topic, "audience": kwargs.get("audience") or "curious general viewers",
                                   "tone": kwargs.get("tone") or "clear, warm, a little playful", "notes": kwargs.get("notes") or "",
                                   "next": "Write the script JSON to this contract, then call action='once' with slug, topic and script.",
                                   "contract": self._contract(pack)}, ensure_ascii=False)
            slug = (kwargs.get("slug") or "").strip()
            if action == "list":
                return json.dumps(self._cli(pack, ["list"], timeout=60))
            if not slug:
                return json.dumps({"status": "error", "message": "%s needs a slug" % action})
            if action in ("status", "verify"):
                return json.dumps(self._cli(pack, [action, slug], timeout=60))
            script_obj = kwargs.get("script")
            script_file = None
            if script_obj:
                if isinstance(script_obj, str):
                    try:
                        script_obj = json.loads(script_obj)
                    except Exception:
                        return json.dumps({"status": "error", "message": "script must be a JSON object"})
                fd, script_file = tempfile.mkstemp(suffix=".json", prefix="short-script-")
                with os.fdopen(fd, "w", encoding="utf-8") as fh:
                    json.dump(script_obj, fh, ensure_ascii=False)
            try:
                if action == "once":
                    args = ["once", slug]
                    if kwargs.get("topic"):
                        args += ["--topic", str(kwargs["topic"])]
                    for k in ("audience", "tone", "notes", "theme", "quality"):
                        if kwargs.get(k):
                            args += ["--" + k, str(kwargs[k])]
                    if script_file:
                        args += ["--script", script_file]
                    elif not shutil.which("copilot"):
                        return json.dumps({"status": "error", "message": (
                            "no script given and the Copilot CLI is not installed — call action='brief' with the "
                            "topic, write the script JSON yourself, then call action='once' with it")})
                    if kwargs.get("skip_render"):
                        args += ["--skip-render"]
                    out = self._cli(pack, args, timeout=2400)
                    res = out.get("result") or {}
                    if isinstance(res, dict) and res.get("mp4"):
                        out["message"] = "Rendered %s (%s). Preview/edit in Studio: cd %s && npx hyperframes preview" % (
                            res["mp4"], (res.get("probe") or {}).get("duration", "?") + "s", _home() / "shorts" / slug / "project")
                    return json.dumps(out, ensure_ascii=False)
                if action == "script":
                    args = ["script", slug] + (["--script", script_file] if script_file else [])
                    if not script_file and not shutil.which("copilot"):
                        return json.dumps({"status": "error", "message": "script needs a script object here (no Copilot CLI); use action='brief' first"})
                    return json.dumps(self._cli(pack, args, timeout=900), ensure_ascii=False)
                if action == "compose":
                    args = ["compose", slug] + (["--theme", str(kwargs["theme"])] if kwargs.get("theme") else [])
                    return json.dumps(self._cli(pack, args, timeout=120))
                if action == "check":
                    return json.dumps(self._cli(pack, ["check", slug], timeout=900))
                if action == "render":
                    args = ["render", slug] + (["--quality", str(kwargs["quality"])] if kwargs.get("quality") else [])
                    return json.dumps(self._cli(pack, args, timeout=2400))
            finally:
                if script_file and os.path.exists(script_file):
                    os.unlink(script_file)
        except Exception as e:  # never break the turn
            return json.dumps({"status": "error", "message": "%s: %s" % (type(e).__name__, e)})
        return json.dumps({"status": "error", "message": "unhandled action"})


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Education Shorts cartridge")
    p.add_argument("action", nargs="?", default="setup", choices=ACTIONS)
    p.add_argument("--slug"); p.add_argument("--topic"); p.add_argument("--theme"); p.add_argument("--script")
    a = p.parse_args()
    sc = json.load(open(a.script)) if a.script else None
    print(EducationShorts().perform(action=a.action, slug=a.slug, topic=a.topic, theme=a.theme, script=sc))
