---
name: "rar-kody-w-rapp-sentinel"
description: "Run the RAPP Sentinel from the brainstem: free health verdicts over your declared GitHub targets, a roll-call of N mutually-verifying AI watchers, published heads peers can check, overnight standup reports \u2014 a watchdog that can't quietly lie."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_sentinel_agent", "rar_sha256": "bfbd0a5baed8da9e3c813a90fc36a20961798f9d93e8ebe164425047d0dc8884", "source_kind": "rar-agent", "source_commit": "0cac8b2ead93e9791fa77022cbd654990205184e", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_sentinel_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/rapp-sentinel:4d8eb0e062e92dee97bf36fe7b39cba2c3557db44ecce2c40b9368a238add9a6", "kind": "skill"}, "author": "Kody Wildfeuer", "tags": ["sentinel", "watchdog", "health", "monitoring", "rapp1", "neighborhood", "trifecta", "devtools"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/rapp_sentinel_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_sentinel_agent.py` is
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
