---
name: "rar-kody-w-education-shorts"
description: "Turns a topic into an animated 9:16 educational YouTube Short: linted script, HyperFrames composition, check, MP4 \u2014 every stage a file on a chained ledger."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/education_shorts_agent", "rar_sha256": "36711e8da4ce32d9b11fc02c18e925f955ca0588dcc65a5ea08099d1f4233f1f", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "Kody Wildfeuer", "tags": ["video", "youtube-shorts", "hyperframes", "animation", "education", "creative"]}
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
