---
name: "rar-kody-w-rapp-sentinel"
description: "Run the RAPP Sentinel from the brainstem: free health verdicts over your declared GitHub targets, a roll-call of N mutually-verifying AI watchers, published heads peers can check, overnight standup reports \u2014 a watchdog that can't quietly lie."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_sentinel_agent", "rar_sha256": "bfbd0a5baed8da9e3c813a90fc36a20961798f9d93e8ebe164425047d0dc8884", "source_kind": "rar-agent", "source_commit": "0cac8b2ead93e9791fa77022cbd654990205184e", "author": "Kody Wildfeuer", "tags": ["sentinel", "watchdog", "health", "monitoring", "rapp1", "neighborhood", "trifecta", "devtools"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rapp_sentinel_agent`. The original RAPP
agent is preserved byte-for-byte in `rapp_sentinel_agent.py` and in the RCI capsule.

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

RAPP Sentinel — a watchdog that can't quietly lie to you, from the brainstem.

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

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_sentinel_agent.py` and embedded as the fenced Python below (sha256 bfbd0a5baed8da9e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_sentinel_agent.py` first:

```bash
python3 rapp_sentinel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_sentinel_agent.py   # or on stdin
python3 rapp_sentinel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
