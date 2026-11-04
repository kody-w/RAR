---
name: "rar-kody-w-education-shorts"
description: "Turns a topic into an animated 9:16 educational YouTube Short: linted script, HyperFrames composition, check, MP4 \u2014 every stage a file on a chained ledger."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/education_shorts_agent", "rar_sha256": "36711e8da4ce32d9b11fc02c18e925f955ca0588dcc65a5ea08099d1f4233f1f", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "Kody Wildfeuer", "tags": ["video", "youtube-shorts", "hyperframes", "animation", "education", "creative"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `education_shorts_agent.py` and embedded as the fenced Python below (sha256 36711e8da4ce32d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `education_shorts_agent.py` first:

```bash
python3 education_shorts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 education_shorts_agent.py   # or on stdin
python3 education_shorts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/education_shorts_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/education_shorts_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/education_shorts_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
