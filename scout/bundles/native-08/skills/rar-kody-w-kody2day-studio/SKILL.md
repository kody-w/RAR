---
name: "rar-kody-w-kody2day-studio"
description: "Make the daily Kody2day episode: the day's digest \u2192 Claude writes the RAPP lesson, Copilot refutes it, the education-shorts pack renders a narrated 16:9 explainer plus byte-sized Shorts \u2192 queue with YouTube metadata."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/kody2day_studio_agent", "rar_sha256": "520f26e2500bd6ec02288d510735b6ed1c3997ca824735865695c47ae17645d9", "source_kind": "rar-agent", "source_commit": "6df086ae702e7b5f1dbfec69470a242317e780be", "author": "Kody Wildfeuer", "tags": ["video", "youtube", "shorts", "education", "kody2day", "hyperframes", "creative", "autonomous"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `kody2day_studio_agent.py` and embedded as the fenced Python below (sha256 520f26e2500bd6ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `kody2day_studio_agent.py` first:

```bash
python3 kody2day_studio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 kody2day_studio_agent.py   # or on stdin
python3 kody2day_studio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
