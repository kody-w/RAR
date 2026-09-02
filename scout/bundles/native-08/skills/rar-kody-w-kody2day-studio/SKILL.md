---
name: "rar-kody-w-kody2day-studio"
description: "Make the daily Kody2day episode: the day's digest \u2192 Claude writes the RAPP lesson, Copilot refutes it, the education-shorts pack renders a narrated 16:9 explainer plus byte-sized Shorts \u2192 queue with YouTube metadata."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/kody2day_studio_agent", "rar_sha256": "520f26e2500bd6ec02288d510735b6ed1c3997ca824735865695c47ae17645d9", "source_kind": "rar-agent", "source_commit": "6df086ae702e7b5f1dbfec69470a242317e780be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "kody2day_studio_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/kody2day-studio:8480595cf98f9334aee0fdb2103bfb0eabb0a5324ceba8bcb8ee84dfe4e0cdd7", "kind": "skill"}, "author": "Kody Wildfeuer", "tags": ["video", "youtube", "shorts", "education", "kody2day", "hyperframes", "creative", "autonomous"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/kody2day_studio_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `kody2day_studio_agent.py` is
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
