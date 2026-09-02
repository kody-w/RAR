---
name: "rar-kody-w-education-shorts"
description: "Turns a topic into an animated 9:16 educational YouTube Short: linted script, HyperFrames composition, check, MP4 \u2014 every stage a file on a chained ledger."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/education_shorts_agent", "rar_sha256": "e8dae3c739c30dd6ea7a3c690a4aa6aaa25cbbfd26ab906d274ec9b520f28715", "source_kind": "rar-agent", "source_commit": "17828d807f840c6d6338a3284b737735b1267142", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "education_shorts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/education-shorts:49f47ae00ce963ebb49a16a550dd95638c7bcb073c899ab93331bd0f237f5ac8", "kind": "skill"}, "author": "Kody Wildfeuer", "tags": ["video", "youtube-shorts", "hyperframes", "animation", "education", "creative"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/education_shorts_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `education_shorts_agent.py` is
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
