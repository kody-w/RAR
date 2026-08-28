---
name: "rar-kody-w-education-shorts"
description: "Turns a topic into an animated 9:16 educational YouTube Short: linted script, HyperFrames composition, check, MP4 \u2014 every stage a file on a chained ledger."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/education_shorts_agent", "rar_sha256": "e8dae3c739c30dd6ea7a3c690a4aa6aaa25cbbfd26ab906d274ec9b520f28715", "source_kind": "rar-agent", "source_commit": "17828d807f840c6d6338a3284b737735b1267142", "author": "Kody Wildfeuer", "tags": ["video", "youtube-shorts", "hyperframes", "animation", "education", "creative"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/education_shorts_agent`. The original RAPP
agent is preserved byte-for-byte in `education_shorts_agent.py` and in the RCI capsule.

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

Education Shorts — turn a topic into an animated 9:16 educational YouTube Short.

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

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `education_shorts_agent.py` and embedded as the fenced Python below (sha256 e8dae3c739c30dd6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `education_shorts_agent.py` first:

```bash
python3 education_shorts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 education_shorts_agent.py   # or on stdin
python3 education_shorts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
