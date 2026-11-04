---
name: "rar-kody-w-kody2day-studio"
description: "Make the daily Kody2day episode: the day's digest \u2192 Claude writes the RAPP lesson, Copilot refutes it, the education-shorts pack renders a narrated 16:9 explainer plus byte-sized Shorts \u2192 queue with YouTube metadata."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/kody2day_studio_agent", "rar_sha256": "d20355f26593583aedbfb7d091a6d6a36b9e1798294baec17cfdc05cfa90b1bb", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "Kody Wildfeuer", "tags": ["video", "youtube", "shorts", "education", "kody2day", "hyperframes", "creative", "autonomous"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/kody2day_studio_agent`. The original RAPP
agent is preserved byte-for-byte in `kody2day_studio_agent.py` and in the RCI capsule.

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

Kody2day Studio — make the daily Kody2day episode (long-form + byte-sized Shorts) from the brainstem.

Drives kody-w/kody2day's studio (studio/kody2day_studio.py): the day's public digest →
Claude Code writes the lesson scripts (rapp-education-shorts contracts, pack lints gate them)
→ GitHub Copilot REFUTES (facts must trace to the digest; up to two revision rounds) →
rapp-education-shorts renders a 16:9 narrated explainer + N 9:16 Shorts → every MP4 is
probed → the episode lands in ~/.rapp/kody2day-studio/queue/<date>/ with YOUTUBE.json,
and one rapp/1 frame goes on the live sentinel's `kody2day` chain.

An episode takes 20-40 minutes, so action='run' starts it DETACHED and returns at once;
poll with action='status' / 'log' / 'episode'. The code is cloned on first use into
~/.rapp/kody2day-studio/code (or point code_dir at a checkout). Prereqs on the machine:
git, python3, the claude CLI (signed in), the copilot CLI (signed in), Node/npx for the
HyperFrames renderer, ffprobe; VibeVoice optional (tts='none' renders silent).

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `kody2day_studio_agent.py` and embedded as the fenced Python below (sha256 d20355f26593583a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `kody2day_studio_agent.py` first:

```bash
python3 kody2day_studio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 kody2day_studio_agent.py   # or on stdin
python3 kody2day_studio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/kody2day_studio_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/kody2day_studio_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/kody2day_studio_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Kody2day Studio — make the daily Kody2day episode (long-form + byte-sized Shorts) from the brainstem.

Drives kody-w/kody2day's studio (studio/kody2day_studio.py): the day's public digest →
Claude Code writes the lesson scripts (rapp-education-shorts contracts, pack lints gate them)
→ GitHub Copilot REFUTES (facts must trace to the digest; up to two revision rounds) →
rapp-education-shorts renders a 16:9 narrated explainer + N 9:16 Shorts → every MP4 is
probed → the episode lands in ~/.rapp/kody2day-studio/queue/<date>/ with YOUTUBE.json,
and one rapp/1 frame goes on the live sentinel's `kody2day` chain.

An episode takes 20-40 minutes, so action='run' starts it DETACHED and returns at once;
poll with action='status' / 'log' / 'episode'. The code is cloned on first use into
~/.rapp/kody2day-studio/code (or point code_dir at a checkout). Prereqs on the machine:
git, python3, the claude CLI (signed in), the copilot CLI (signed in), Node/npx for the
HyperFrames renderer, ffprobe; VibeVoice optional (tts='none' renders silent).
"""

import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
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
    "name": "@kody-w/kody2day_studio_agent",
    "version": "1.0.0",
    "display_name": "Kody2day Studio",
    "description": (
        "Make the daily Kody2day episode: the day's digest → Claude writes the RAPP lesson, Copilot refutes it, "
        "the education-shorts pack renders a narrated 16:9 explainer plus byte-sized Shorts → queue with YouTube metadata."
    ),
    "author": "Kody Wildfeuer",
    "tags": ["video", "youtube", "shorts", "education", "kody2day", "hyperframes", "creative", "autonomous"],
    "category": "creative",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "external_prereqs": [
        "git", "claude CLI (signed in) — the writer", "GitHub Copilot CLI (signed in) — the refute reviewer",
        "Node.js with npx (HyperFrames renderer)", "ffprobe",
        "optional: VibeVoice venv for narration (else tts='none')",
    ],
    "example_call": {"args": {"action": "run", "date": "2026-08-18"}},
}

CODE_REPO = "https://github.com/kody-w/kody2day"
STUDIO = Path(os.environ.get("KODY2DAY_STUDIO", "") or (Path.home() / ".rapp" / "kody2day-studio")).expanduser()
ACTIONS = ("run", "status", "episode", "log", "queue", "episodes", "curriculum", "setup")
# A brainstem or launchd process rarely has these on PATH; the studio needs claude + copilot + npx.
EXTRA_BIN = [str(Path.home() / ".local" / "bin"), "/opt/homebrew/bin", "/usr/local/bin",
             str(Path.home() / "Library" / "Application Support" / "Code" / "User" / "globalStorage" / "github.copilot-chat" / "copilotCli"),
             str(Path.home() / ".copilot" / "bin"), str(Path.home() / ".npm-global" / "bin")]


def _path():
    return os.pathsep.join([d for d in EXTRA_BIN if Path(d).is_dir()] + [os.environ.get("PATH", "")])


def _which(tool):
    return shutil.which(tool, path=_path())
DATE_FMT = "%Y-%m-%d"


class Kody2dayStudio(BasicAgent):
    def __init__(self):
        self.name = "Kody2dayStudio"
        self.metadata = {
            "name": self.name,
            "description": (
                "Produce or inspect Kody2day episodes — the daily educational YouTube show about RAPP built from what "
                "Kody shipped. action='run' (date=YYYY-MM-DD, default yesterday) starts an episode in the background: "
                "digest → Claude writes → Copilot refutes → render long-form + Shorts → queue; returns immediately with "
                "the log path. action='status' says whether a run is in progress and shows the last ledger entry; "
                "action='episode' (date) returns that episode's result (concept, refute verdict, MP4 durations, queue "
                "path, YouTube title/description); action='log' tails a run's log; action='queue' lists rendered "
                "episodes ready to upload; action='episodes' lists the ledger; action='curriculum' shows the concept "
                "syllabus. Use for 'make today's Kody2day', 'is the episode done', 'what's in the upload queue', "
                "'render the shorts for <date>'."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": list(ACTIONS), "description": "Default: status."},
                    "date": {"type": "string", "description": "Digest day YYYY-MM-DD (UTC). Default: yesterday for run; latest otherwise."},
                    "shorts": {"type": "integer", "description": "run: how many byte-sized Shorts (default 3)."},
                    "tts": {"type": "string", "enum": ["vibevoice", "none"], "description": "run: narration engine (default vibevoice)."},
                    "quality": {"type": "string", "enum": ["draft", "high"], "description": "run: render quality (default high)."},
                    "skip_render": {"type": "boolean", "description": "run: stop after the scripts pass refute (no MP4)."},
                    "code_dir": {"type": "string", "description": "A kody2day checkout to use (default ~/.rapp/kody2day-studio/code, cloned on first use)."},
                    "lines": {"type": "integer", "description": "log: how many tail lines (default 40)."},
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── plumbing ─────────────────────────────────────────────────────────
    def _code(self, params):
        raw = (params.get("code_dir") or "").strip()
        if raw:
            code = Path(raw).expanduser()
            return (code, None) if (code / "studio" / "kody2day_studio.py").exists() else (None, "%s has no studio/kody2day_studio.py" % code)
        code = STUDIO / "code"
        if (code / "studio" / "kody2day_studio.py").exists():
            subprocess.run(["git", "-C", str(code), "pull", "-q", "--ff-only"], capture_output=True, timeout=120, stdin=subprocess.DEVNULL)
            return code, None
        if not shutil.which("git"):
            return None, "git is required to fetch %s" % CODE_REPO
        code.parent.mkdir(parents=True, exist_ok=True)
        r = subprocess.run(["git", "clone", "--depth", "1", CODE_REPO, str(code)], capture_output=True, text=True, timeout=300,
                           stdin=subprocess.DEVNULL)
        if r.returncode != 0 or not (code / "studio" / "kody2day_studio.py").exists():
            return None, "could not clone %s: %s" % (CODE_REPO, (r.stderr or "")[-300:])
        return code, None

    @staticmethod
    def _valid_date(s):
        try:
            datetime.strptime(s, DATE_FMT)
            return True
        except Exception:
            return False

    @staticmethod
    def _read(p):
        try:
            return json.loads(Path(p).read_text())
        except Exception:
            return None

    @staticmethod
    def _running():
        """Detached runs leave a pidfile per date; a live pid means in progress."""
        live = {}
        for pf in (STUDIO / "runs").glob("*.pid"):
            try:
                pid = int(pf.read_text().strip())
                os.kill(pid, 0)
                # a detached child of a long-lived server can linger as a zombie; that is finished, not running
                st = subprocess.run(["ps", "-o", "stat=", "-p", str(pid)], capture_output=True, text=True, timeout=5).stdout.strip()
                if not st or st.startswith("Z"):
                    continue
                live[pf.stem] = pid
            except Exception:
                continue
        return live

    def _ledger(self):
        led = STUDIO / "ledger.jsonl"
        if not led.exists():
            return []
        rows = []
        for line in led.read_text().splitlines():
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
        return rows

    # ── actions ──────────────────────────────────────────────────────────
    def _run(self, params):
        code, err = self._code(params)
        if err:
            return {"status": "error", "message": err}
        date = str(params.get("date") or (datetime.now(timezone.utc) - timedelta(days=1)).strftime(DATE_FMT))
        if not self._valid_date(date):
            return {"status": "error", "message": "date must be YYYY-MM-DD"}
        live = self._running()
        if date in live:
            return {"status": "success", "already_running": True, "date": date, "pid": live[date],
                    "log": str(STUDIO / "runs" / ("%s.log" % date)), "next": "action='status' or action='log'"}
        for tool in ("claude", "copilot"):
            if not _which(tool):
                return {"status": "error", "message": "%s CLI not on PATH — the studio needs both claude (writer) and copilot (refuter)" % tool}
        runs = STUDIO / "runs"
        runs.mkdir(parents=True, exist_ok=True)
        argv = [sys.executable, str(code / "studio" / "kody2day_studio.py"), "run", "--date", date,
                "--shorts", str(int(params.get("shorts") or 3)), "--tts", str(params.get("tts") or "vibevoice"),
                "--quality", str(params.get("quality") or "high")]
        if params.get("skip_render"):
            argv.append("--skip-render")
        log = runs / ("%s.log" % date)
        env = dict(os.environ, NO_COLOR="1", PATH=_path())
        env.pop("CLAUDECODE", None)
        with open(log, "ab") as fh:
            fh.write(("\n=== %s run started %s ===\n" % (date, datetime.now(timezone.utc).isoformat(timespec="seconds"))).encode())
            p = subprocess.Popen(argv, stdout=fh, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, cwd=str(code),
                                 env=env, start_new_session=True)
        (runs / ("%s.pid" % date)).write_text(str(p.pid))
        return {"status": "success", "started": True, "date": date, "pid": p.pid, "log": str(log),
                "episode_dir": str(STUDIO / "episodes" / date),
                "expect": "20-40 minutes (write ~3 min, refute ~2 min per round, long-form narration + render, then Shorts)",
                "next": "action='status' to poll; action='episode' with date once done; files land in action='queue'"}

    def _status(self):
        rows = self._ledger()
        live = self._running()
        eps = sorted((STUDIO / "episodes").glob("*/"), reverse=True) if (STUDIO / "episodes").exists() else []
        latest_dir = str(eps[0]) if eps else None
        return {"status": "success", "running": live, "episodes_on_ledger": len(rows), "last": rows[-1] if rows else None,
                "latest_episode_dir": latest_dir, "studio": str(STUDIO),
                "queue": sorted(p.name for p in (STUDIO / "queue").glob("*/")) if (STUDIO / "queue").exists() else []}

    def _episode(self, date):
        eps = sorted((STUDIO / "episodes").glob("*/"), reverse=True) if (STUDIO / "episodes").exists() else []
        if not date:
            if not eps:
                return {"status": "error", "message": "no episodes yet — action='run'"}
            date = eps[0].name
        ep = STUDIO / "episodes" / date
        if not ep.exists():
            return {"status": "error", "message": "no episode dir for %s" % date}
        e = self._read(ep / "episode.json")
        draft = self._read(ep / "draft.json") or {}
        refute = self._read(ep / "refute.json") or {}
        yt = self._read(STUDIO / "queue" / date / "YOUTUBE.json") or draft.get("youtube") or {}
        return {"status": "success", "date": date, "running": date in self._running(),
                "episode": e or "in progress / not finished (see action='log')",
                "concept": (e or {}).get("concept") or draft.get("concept"),
                "long_title": (draft.get("long") or {}).get("title"),
                "shorts": [s.get("title") for s in draft.get("shorts", [])],
                "refute": {"verdict": refute.get("verdict"), "issues": (refute.get("issues") or [])[:6]},
                "youtube": {k: yt.get(k) for k in ("title", "description", "tags", "chapters", "files") if k in yt},
                "dir": str(ep)}

    def _log(self, date, lines):
        if not date:
            live = self._running()
            date = sorted(live)[-1] if live else None
            if not date:
                logs = sorted((STUDIO / "runs").glob("*.log")) if (STUDIO / "runs").exists() else []
                date = logs[-1].stem if logs else None
        if not date:
            return {"status": "error", "message": "no runs yet"}
        cand = [STUDIO / "runs" / ("%s.log" % date), STUDIO / "episodes" / date / "studio.log"]
        for p in cand:
            if p.exists():
                tail = p.read_text().splitlines()[-max(5, lines):]
                return {"status": "success", "date": date, "running": date in self._running(), "log": str(p), "tail": tail}
        return {"status": "error", "message": "no log for %s" % date}

    def _queue(self):
        q = STUDIO / "queue"
        out = []
        for d in sorted(q.glob("*/"), reverse=True) if q.exists() else []:
            yt = self._read(d / "YOUTUBE.json") or {}
            files = sorted(str(f) for f in d.glob("*.mp4"))
            out.append({"date": d.name, "title": yt.get("title"), "files": files, "shorts_titles": yt.get("shorts_titles"),
                        "youtube_json": str(d / "YOUTUBE.json")})
        return {"status": "success", "count": len(out), "queue": out,
                "note": "uploading to YouTube is the human step — each folder has the MP4s and YOUTUBE.json (title, description, tags, chapters)"}

    def _curriculum(self, params):
        code, err = self._code(params)
        if err:
            return {"status": "error", "message": err}
        try:
            sys.path.insert(0, str(code / "studio"))
            import importlib
            m = importlib.import_module("kody2day_studio")
            taught = {r.get("concept") for r in self._ledger() if r.get("ok")}
            return {"status": "success", "curriculum": [{"id": k, "concept": v, "taught": k in taught} for k, v in m.CURRICULUM]}
        except Exception as e:
            return {"status": "error", "message": "could not read curriculum: %s" % e}

    def _setup(self, params):
        code, err = self._code(params)
        if err:
            return {"status": "error", "message": err}
        head = subprocess.run(["git", "-C", str(code), "rev-parse", "--short", "HEAD"], capture_output=True, text=True, stdin=subprocess.DEVNULL)
        tools = {t: bool(_which(t)) for t in ("claude", "copilot", "npx", "hyperframes", "ffprobe", "git")}
        return {"status": "success", "code_dir": str(code), "code_head": (head.stdout or "").strip(), "studio": str(STUDIO), "tools": tools,
                "vibevoice": (Path.home() / ".rapp-mirror" / "venv").exists() or (Path.home() / "VibeVoice").exists(),
                "next": "action='run' (date=YYYY-MM-DD) — then action='status'"}

    # ── entry ────────────────────────────────────────────────────────────
    def perform(self, **kwargs):
        params = dict(kwargs)
        action = (params.get("action") or "status").strip().lower()
        date = str(params.get("date") or "").strip()
        if date and not self._valid_date(date):
            return json.dumps({"status": "error", "message": "date must be YYYY-MM-DD"})
        try:
            if action == "run":
                out = self._run(params)
            elif action == "status":
                out = self._status()
            elif action == "episode":
                out = self._episode(date)
            elif action == "log":
                out = self._log(date, int(params.get("lines") or 40))
            elif action == "queue":
                out = self._queue()
            elif action == "episodes":
                out = {"status": "success", "episodes": self._ledger()[-30:]}
            elif action == "curriculum":
                out = self._curriculum(params)
            elif action == "setup":
                out = self._setup(params)
            else:
                out = {"status": "error", "message": "unknown action %r; one of %s" % (action, list(ACTIONS))}
        except Exception as e:
            out = {"status": "error", "message": "%s: %s" % (type(e).__name__, e)}
        return json.dumps(out, indent=2, default=str)


if __name__ == "__main__":
    a = Kody2dayStudio()
    args = {}
    for tok in sys.argv[1:]:
        if "=" in tok:
            k, v = tok.split("=", 1)
            args[k] = v
        else:
            args["action"] = tok
    print(a.perform(**args))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
