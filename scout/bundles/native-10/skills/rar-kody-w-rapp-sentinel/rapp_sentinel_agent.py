"""RAPP Sentinel — a watchdog that can't quietly lie to you, from the brainstem.

Drives kody-w/rapp-sentinel (public, MIT): N AIs each keeping a tamper-evident
rapp/1 chain the others can verify; health checks are free and only failure may
invoke a model. This agent installs the sentinel code once (a shallow clone into
~/.rapp/sentinel/pack, or point `code_dir` at an existing checkout such as a live
~/rapp-sentinel install) and runs its own scripts as subprocesses, so the agent
never re-implements a check — every verdict here is the sentinel's own verdict.

Doctrine it enforces (TRIFECTA-PATTERN.md §6d), quoted because it decides how
you should read the output:
  R1 receipts aren't evidence — read the artifact, not the log line about it.
  R2 ran isn't worked — a green cron with no output is a stall.
  R3 require known-good, never enumerate known-bad.

Actions: setup, health, status, tick, roll_call, publish, peers, anchors,
verify, standup, diagnose, checks, config, explain, install_launchd. Level 0
(the default config) spends no model tokens; a tick at level 0 observes and
notifies only. Prereqs: git, python3 (3.9+); `gh` (authenticated) for the
GitHub checks; the Copilot CLI only for levels 1+. No secrets, no env vars.
"""

import json
import os
import platform
import shutil
import subprocess
import sys
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
    "name": "@kody-w/rapp_sentinel_agent",
    "version": "1.0.0",
    "display_name": "RAPP Sentinel",
    "description": (
        "Run the RAPP Sentinel from the brainstem: free health verdicts over your declared "
        "GitHub targets, a roll-call of N mutually-verifying AI watchers, published heads "
        "peers can check, overnight standup reports — a watchdog that can't quietly lie."
    ),
    "author": "Kody Wildfeuer",
    "tags": ["sentinel", "watchdog", "health", "monitoring", "rapp1", "neighborhood", "trifecta", "devtools"],
    "category": "devtools",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "external_prereqs": [
        "git",
        "gh (GitHub CLI, authenticated) for the GitHub health checks",
        "optional: GitHub Copilot CLI for levels 1+ (repair/evolve arms)",
        "optional: macOS launchd for install_launchd (every-15-minutes tick)",
    ],
    "example_call": {"args": {"action": "health"}},
}

PACK_REPO = "https://github.com/kody-w/rapp-sentinel"
ACTIONS = ("setup", "health", "status", "tick", "roll_call", "publish", "peers", "anchors",
           "verify", "standup", "diagnose", "checks", "config", "explain", "install_launchd")

EXPLAIN = {
    "pattern": "N AIs walk into a bar: a declarable roster of watchers (any vendor) each keeping a "
               "hash-chained rapp/1 frame log the others can verify. Health checks are stdlib and free; "
               "only failure may spend a model. Freedom to change things is a dial (level 0-3), not a switch.",
    "levels": {
        "0": "observe + notify only (default; costs nothing)",
        "1": "diagnose with a model on failure, no writes",
        "2": "repair: model may open PRs against declared targets; outsider smoke tests allowed",
        "3": "evolve: proactive art/contribution arm, only while healthy",
    },
    "rules": {
        "R1": "receipts aren't evidence — read the artifact, not the log line about it",
        "R2": "ran isn't worked — a green run with no output is a stall",
        "R3": "require known-good, never enumerate known-bad",
    },
    "trust_model": "An outside neighbor is trusted exactly as far as its published head can be checked "
                   "against what it published before: you can catch a peer that stalled, never one that lied.",
    "docs": ["README.md", "TRIFECTA-PATTERN.md", "N-AIS-WALK-INTO-A-BAR.md", "JOINING.md", "SPEC-rapp1.md"],
    "repo": PACK_REPO,
}


def _root():
    raw = os.environ.get("RAPP_SENTINEL_AGENT_HOME", "").strip()
    return Path(raw).expanduser() if raw else Path.home() / ".rapp" / "sentinel"


class RappSentinel(BasicAgent):
    def __init__(self):
        self.name = "RappSentinel"
        self.metadata = {
            "name": self.name,
            "description": (
                "Operate the RAPP Sentinel — the tamper-evident watchdog for GitHub-native platforms. "
                "action='health' runs every check (free, stdlib) and returns the verdict: status "
                "healthy/degraded/critical, which check ids failed and why. action='status' reads the "
                "last tick's heartbeat plus the neighbors' roll-call. action='tick' runs one sentinel "
                "tick (level 0 spends nothing). roll_call/verify/publish/peers/anchors drive the rapp/1 "
                "neighborhood chains. standup renders the overnight shift report; diagnose prints the "
                "dependency page; checks lists the required check ids; config reads or edits the "
                "instance config (level, watch_repos, notify); explain returns the doctrine (R1/R2/R3, "
                "levels). Use for anything about watchdogs, health checks, chains that can't lie, "
                "sentinel neighborhoods, or 'is my platform actually moving'."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": list(ACTIONS), "description": "What to do. Default: status."},
                    "code_dir": {"type": "string", "description": (
                        "Existing rapp-sentinel checkout to drive (e.g. a live ~/rapp-sentinel install). "
                        "Default: a shallow clone at ~/.rapp/sentinel/pack, fetched on first use.")},
                    "home_dir": {"type": "string", "description": (
                        "SENTINEL_HOME — where this instance's config/state/chains live. Default: "
                        "~/.rapp/sentinel/instance. Pass the same value as code_dir to drive a live install "
                        "in place (its state sits beside the code).")},
                    "hours": {"type": "integer", "description": "standup: report window in hours (default 14)."},
                    "watch_repos": {"type": "array", "items": {"type": "string"},
                                    "description": "config: replace the owner/name list of repos to watch."},
                    "level": {"type": "integer", "description": "config: set the autonomy dial 0-3."},
                    "notify_handle": {"type": "string", "description": "config: iMessage/SMS handle for alerts."},
                    "instance_name": {"type": "string", "description": "config: display name for this instance."},
                    "check_id": {"type": "string", "description": "checks: return just this check's manifest row."},
                    "confirm": {"type": "boolean", "description": "install_launchd: must be true (loads launchd jobs)."},
                    "update": {"type": "boolean", "description": "setup: git pull an existing pack clone (molt)."},
                    "timeout": {"type": "integer", "description": "Subprocess ceiling in seconds (default 900)."},
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
            if not (code / "health.py").exists() or not (code / "sentinel.py").exists():
                return None, "%s is not a rapp-sentinel checkout (no health.py/sentinel.py)" % code
            return code, None
        pack = _root() / "pack"
        if (pack / "health.py").exists():
            if params.get("update"):
                subprocess.run(["git", "-C", str(pack), "pull", "--ff-only", "-q"], capture_output=True,
                               text=True, timeout=300, stdin=subprocess.DEVNULL)
            return pack, None
        if not shutil.which("git"):
            return None, "git is required to fetch %s" % PACK_REPO
        pack.parent.mkdir(parents=True, exist_ok=True)
        try:
            r = subprocess.run(["git", "clone", "--depth", "1", PACK_REPO, str(pack)], capture_output=True,
                               text=True, timeout=300, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            return None, "git clone timed out"
        if r.returncode != 0 or not (pack / "health.py").exists():
            return None, "could not clone %s: %s" % (PACK_REPO, (r.stderr or "")[-300:].strip())
        return pack, None

    def _home(self, params, code):
        raw = (params.get("home_dir") or "").strip()
        home = Path(raw).expanduser() if raw else _root() / "instance"
        home.mkdir(parents=True, exist_ok=True)
        # A fresh instance is seeded from the pack's examples: config at level 0
        # (nothing spent, nothing loaded) and the repo's direction.json (the
        # declared situation + targets the ecosystem sweep reads at runtime).
        # Existing files are never touched — a live install's state is its own.
        for name, src in (("config.json", "config.example.json"), ("direction.json", "direction.json")):
            dst = home / name
            if not dst.exists() and (code / src).exists() and dst.resolve() != (code / src).resolve():
                shutil.copy2(code / src, dst)
        return home

    def _env(self, code, home):
        env = dict(os.environ, NO_COLOR="1")
        if home.resolve() != code.resolve():
            env["SENTINEL_HOME"] = str(home)
        else:
            env.pop("SENTINEL_HOME", None)
        return env

    def _run(self, code, home, argv, timeout=900):
        try:
            r = subprocess.run([sys.executable] + argv, capture_output=True, text=True, timeout=timeout,
                               cwd=str(code), stdin=subprocess.DEVNULL, env=self._env(code, home))
        except subprocess.TimeoutExpired:
            return None, {"status": "error", "message": "%s timed out after %ss" % (argv[0], timeout)}
        return r, None

    @staticmethod
    def _json(text):
        text = (text or "").strip()
        if not text:
            return None
        try:
            return json.loads(text)
        except Exception:
            # some scripts print log lines before the JSON; take the last balanced object
            i = text.find("{")
            if i >= 0:
                try:
                    return json.loads(text[i:])
                except Exception:
                    pass
        return None

    @staticmethod
    def _read(path):
        try:
            return json.loads(Path(path).read_text())
        except Exception:
            return None

    # ── actions ──────────────────────────────────────────────────────────
    def _setup(self, code, home):
        head = subprocess.run(["git", "-C", str(code), "rev-parse", "--short", "HEAD"], capture_output=True,
                              text=True, stdin=subprocess.DEVNULL)
        cfg = self._read(home / "config.json") or {}
        return {"status": "success", "code_dir": str(code), "home_dir": str(home),
                "code_head": (head.stdout or "").strip() or "unknown",
                "level": cfg.get("level"), "instance_name": cfg.get("instance_name"),
                "watch_repos": cfg.get("watch_repos", []),
                "gh": bool(shutil.which("gh")), "copilot": bool(shutil.which("copilot")),
                "next": "action='health' for a free verdict; action='config' to set watch_repos/level"}

    def _health(self, code, home, timeout):
        r, err = self._run(code, home, ["health.py"], timeout)
        if err:
            return err
        doc = self._json(r.stdout)
        if not doc:
            return {"status": "error", "message": (r.stderr or r.stdout or "health.py produced no verdict")[-800:]}
        failed = [{"id": c["id"], "severity": c.get("severity"), "detail": c.get("detail")}
                  for c in doc.get("checks", []) if not c.get("ok")]
        return {"status": "success", "verdict": doc.get("status"), "generated": doc.get("generated"),
                "checks_run": len(doc.get("checks", [])), "failed": failed,
                "critical": doc.get("critical", []), "summary": doc.get("summary")}

    def _status(self, code, home, timeout):
        last = self._read(home / "state" / "last_run.json")
        r, err = self._run(code, home, ["neighborhood.py", "roll-call"], min(timeout, 120))
        roll = self._json(r.stdout) if r else None
        cfg = self._read(home / "config.json") or {}
        stop = (home / "STOP").exists()
        return {"status": "success", "instance": cfg.get("instance_name"), "level": cfg.get("level"),
                "stopped": stop, "last_run": last or "no tick has run yet (action='tick' or 'health')",
                "roll_call": roll if roll is not None else (err or {"note": "no chains yet"}),
                "home_dir": str(home), "code_dir": str(code)}

    def _tick(self, code, home, timeout):
        r, err = self._run(code, home, ["sentinel.py"], timeout)
        if err:
            return err
        last = self._read(home / "state" / "last_run.json")
        return {"status": "success" if r.returncode == 0 else "error", "exit": r.returncode,
                "log": (r.stdout or "").strip()[-2000:], "stderr": (r.stderr or "").strip()[-600:],
                "last_run": last}

    def _nbhd(self, code, home, sub, timeout):
        r, err = self._run(code, home, ["neighborhood.py", sub], min(timeout, 300))
        if err:
            return err
        doc = self._json(r.stdout)
        if doc is None:
            return {"status": "error", "message": (r.stderr or r.stdout or "no output")[-800:]}
        out = {"status": "success", "result": doc}
        if sub == "publish":
            out["head_path"] = str(home / "public" / "sentinel-head.json")
        return out

    def _verify(self, code, home, timeout):
        r, err = self._run(code, home, ["neighborhood.py", "roll-call"], min(timeout, 120))
        if err:
            return err
        roll = self._json(r.stdout) or {}
        broken = {k: v.get("chain_detail") for k, v in roll.items() if v.get("frames") and not v.get("chain_ok")}
        return {"status": "success", "chains_ok": not broken, "broken": broken,
                "neighbors": {k: {"frames": v.get("frames"), "alive": v.get("alive"),
                                  "age_minutes": v.get("age_minutes")} for k, v in roll.items()}}

    def _standup(self, code, home, hours, timeout):
        r, err = self._run(code, home, ["standup.py", "--hours=%d" % hours], timeout)
        if err:
            return err
        return {"status": "success" if r.returncode == 0 else "error", "line": (r.stdout or "").strip()[-600:],
                "report": str(home / "dashboard" / "index.html"), "stderr": (r.stderr or "").strip()[-400:]}

    def _diagnose(self, code, home, timeout):
        r, err = self._run(code, home, ["sentinel.py", "diagnose"], timeout)
        if err:
            return err
        return {"status": "success" if r.returncode == 0 else "error", "exit": r.returncode,
                "page": (r.stdout or "").strip()[-4000:], "stderr": (r.stderr or "").strip()[-400:]}

    def _checks(self, code, check_id):
        doc = self._read(code / "required_checks.json")
        if not isinstance(doc, dict) or not isinstance(doc.get("required"), list):
            return {"status": "error", "message": "required_checks.json unreadable or unexpected shape"}
        ids = [str(x) for x in doc["required"]]
        kinds = doc.get("kinds") if isinstance(doc.get("kinds"), dict) else {}
        if check_id:
            if check_id not in ids:
                return {"status": "error", "message": "unknown id %s (ids never rename; see action='checks')" % check_id}
            return {"status": "success", "check": {"id": check_id, "required": True, **(kinds.get(check_id) or {})}}
        return {"status": "success", "count": len(ids), "ids": ids,
                "kinds": {k: v for k, v in kinds.items() if k in ids},
                "outsider_platforms": doc.get("outsider_platforms"),
                "unpaired_accepted": doc.get("unpaired_accepted")}

    def _config(self, home, params):
        cfg_path = home / "config.json"
        cfg = self._read(cfg_path)
        if cfg is None:
            return {"status": "error", "message": "%s missing or unreadable" % cfg_path}
        changed = {}
        if isinstance(params.get("watch_repos"), list):
            cfg["watch_repos"] = [str(x) for x in params["watch_repos"]]
            changed["watch_repos"] = cfg["watch_repos"]
        if params.get("level") is not None:
            lvl = int(params["level"])
            if lvl not in (0, 1, 2, 3):
                return {"status": "error", "message": "level must be 0-3"}
            cfg["level"] = lvl
            changed["level"] = lvl
        if params.get("notify_handle"):
            cfg["notify_handle"] = str(params["notify_handle"])
            cfg["notify"] = True
            changed["notify_handle"] = cfg["notify_handle"]
        if params.get("instance_name"):
            cfg["instance_name"] = str(params["instance_name"])
            changed["instance_name"] = cfg["instance_name"]
        if changed:
            cfg_path.write_text(json.dumps(cfg, indent=2) + "\n")
        view = {k: cfg.get(k) for k in ("instance_name", "instance_slug", "level", "notify", "notify_handle",
                                       "watch_repos", "repair_enabled", "daily_escalation_budget")}
        return {"status": "success", "changed": changed, "config": view, "path": str(cfg_path)}

    def _install_launchd(self, code, home, params, timeout):
        if platform.system() != "Darwin":
            return {"status": "error", "message": "install_launchd needs macOS launchd; run health/tick from your own scheduler"}
        if not params.get("confirm"):
            return {"status": "error", "message": "loads launchd jobs (a tick every 15 minutes) — pass confirm=true"}
        argv = ["./install-launchd.sh"] + (["--home", str(home)] if home.resolve() != code.resolve() else [])
        try:
            r = subprocess.run(argv, capture_output=True, text=True, timeout=timeout, cwd=str(code),
                               stdin=subprocess.DEVNULL, env=self._env(code, home))
        except subprocess.TimeoutExpired:
            return {"status": "error", "message": "installer timed out"}
        return {"status": "success" if r.returncode == 0 else "error", "exit": r.returncode,
                "log": (r.stdout or "").strip()[-1500:], "stderr": (r.stderr or "").strip()[-600:]}

    # ── entry ────────────────────────────────────────────────────────────
    def perform(self, **kwargs):
        params = dict(kwargs)
        action = (params.get("action") or "status").strip().lower()
        if action not in ACTIONS:
            return json.dumps({"status": "error", "message": "unknown action %r; one of %s" % (action, list(ACTIONS))})
        if action == "explain":
            return json.dumps({"status": "success", "explain": EXPLAIN}, indent=2)
        try:
            timeout = max(30, int(params.get("timeout") or 900))
        except (TypeError, ValueError):
            timeout = 900
        code, err = self._code(params)
        if err:
            return json.dumps({"status": "error", "message": err})
        home = self._home(params, code)
        try:
            if action == "setup":
                out = self._setup(code, home)
            elif action == "health":
                out = self._health(code, home, timeout)
            elif action == "status":
                out = self._status(code, home, timeout)
            elif action == "tick":
                out = self._tick(code, home, timeout)
            elif action in ("roll_call", "publish", "peers", "anchors"):
                out = self._nbhd(code, home, action.replace("_", "-"), timeout)
            elif action == "verify":
                out = self._verify(code, home, timeout)
            elif action == "standup":
                out = self._standup(code, home, int(params.get("hours") or 14), timeout)
            elif action == "diagnose":
                out = self._diagnose(code, home, timeout)
            elif action == "checks":
                out = self._checks(code, params.get("check_id"))
            elif action == "config":
                out = self._config(home, params)
            else:
                out = self._install_launchd(code, home, params, timeout)
        except Exception as e:  # a broken agent, not a broken platform — say so
            out = {"status": "error", "message": "%s: %s" % (type(e).__name__, e)}
        return json.dumps(out, indent=2, default=str)


if __name__ == "__main__":
    a = RappSentinel()
    args = {}
    for tok in sys.argv[1:]:
        if "=" in tok:
            k, v = tok.split("=", 1)
            args[k] = v
        else:
            args["action"] = tok
    print(a.perform(**args))
