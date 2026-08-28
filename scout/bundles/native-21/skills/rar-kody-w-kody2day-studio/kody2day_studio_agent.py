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
