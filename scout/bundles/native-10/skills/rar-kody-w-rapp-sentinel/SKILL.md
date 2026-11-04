---
name: "rar-kody-w-rapp-sentinel"
description: "Run the RAPP Sentinel from the brainstem: free health verdicts over your declared GitHub targets, a roll-call of N mutually-verifying AI watchers, published heads peers can check, overnight standup reports \u2014 a watchdog that can't quietly lie."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_sentinel_agent", "rar_sha256": "21c1590863a76733ea61aad02ff93d6ef2f89b5f386d76a2417c4794e5bc944d", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "Kody Wildfeuer", "tags": ["sentinel", "watchdog", "health", "monitoring", "rapp1", "neighborhood", "trifecta", "devtools"]}
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
