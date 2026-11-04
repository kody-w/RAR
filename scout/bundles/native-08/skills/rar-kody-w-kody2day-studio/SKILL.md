---
name: "rar-kody-w-kody2day-studio"
description: "Make the daily Kody2day episode: the day's digest \u2192 Claude writes the RAPP lesson, Copilot refutes it, the education-shorts pack renders a narrated 16:9 explainer plus byte-sized Shorts \u2192 queue with YouTube metadata."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/kody2day_studio_agent", "rar_sha256": "d20355f26593583aedbfb7d091a6d6a36b9e1798294baec17cfdc05cfa90b1bb", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "Kody Wildfeuer", "tags": ["video", "youtube", "shorts", "education", "kody2day", "hyperframes", "creative", "autonomous"]}
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
