---
name: "rar-kody-w-rapp-sentinel"
description: "Run the RAPP Sentinel from the brainstem: free health verdicts over your declared GitHub targets, a roll-call of N mutually-verifying AI watchers, published heads peers can check, overnight standup reports \u2014 a watchdog that can't quietly lie."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_sentinel_agent", "rar_sha256": "21c1590863a76733ea61aad02ff93d6ef2f89b5f386d76a2417c4794e5bc944d", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "Kody Wildfeuer", "tags": ["sentinel", "watchdog", "health", "monitoring", "rapp1", "neighborhood", "trifecta", "devtools"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_sentinel_agent.py` and embedded as the fenced Python below (sha256 21c1590863a76733…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_sentinel_agent.py` first:

```bash
python3 rapp_sentinel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_sentinel_agent.py   # or on stdin
python3 rapp_sentinel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/rapp_sentinel_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rapp_sentinel_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/rapp_sentinel_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
