---
name: "rar-kody-w-kody2day"
description: "Keep up with Kody: today's digest of what he shipped across his public GitHub, any past day, a multi-day catch-up, or a search by repo \u2014 Kody's own commits separated from the fleet of bots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/kody2day_agent", "rar_sha256": "3c0814050b74a0b9f7fb44220ed66600430ab8779601f469be8c20ac86521a99", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "Kody Wildfeuer", "tags": ["digest", "daily", "changelog", "github", "kody", "catch-up", "news"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/kody2day_agent`. The original RAPP
agent is preserved byte-for-byte in `kody2day_agent.py` and in the RCI capsule.

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

Kody2day — "u need a daily Kody2day so i can keep up." (Howard)

Reads the public daily digest at https://kody-w.github.io/kody2day/ — one page
per day of what Kody shipped across his PUBLIC GitHub estate, Kody's own commits
separated from the fleet of bots — and hands it to your brainstem so you can ask
"what did Kody ship today?", "what happened in rapp-sentinel this week?", or
"catch me up on the last 3 days". Nothing here needs a token: it is a static
site built by kody-w/kody2day's daily cron. If you have that repo checked out,
action='build' regenerates a day locally and action='note' drops an editor's
note that the next build renders at the top of the page.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `kody2day_agent.py` and embedded as the fenced Python below (sha256 3c0814050b74a0b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `kody2day_agent.py` first:

```bash
python3 kody2day_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 kody2day_agent.py   # or on stdin
python3 kody2day_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/kody2day_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/kody2day_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/kody2day_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Kody2day — "u need a daily Kody2day so i can keep up." (Howard)

Reads the public daily digest at https://kody-w.github.io/kody2day/ — one page
per day of what Kody shipped across his PUBLIC GitHub estate, Kody's own commits
separated from the fleet of bots — and hands it to your brainstem so you can ask
"what did Kody ship today?", "what happened in rapp-sentinel this week?", or
"catch me up on the last 3 days". Nothing here needs a token: it is a static
site built by kody-w/kody2day's daily cron. If you have that repo checked out,
action='build' regenerates a day locally and action='note' drops an editor's
note that the next build renders at the top of the page.
"""

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
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
    "name": "@kody-w/kody2day_agent",
    "version": "1.0.0",
    "display_name": "Kody2day",
    "description": (
        "Keep up with Kody: today's digest of what he shipped across his public GitHub, any past day, "
        "a multi-day catch-up, or a search by repo — Kody's own commits separated from the fleet of bots."
    ),
    "author": "Kody Wildfeuer",
    "tags": ["digest", "daily", "changelog", "github", "kody", "catch-up", "news"],
    "category": "productivity",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "external_prereqs": ["network access to kody-w.github.io (static site, no token)",
                         "impact only: the owner's private ledger at ~/.rapp/kody2day-private (local, never published)"],
    "example_call": {"args": {"action": "today"}},
}

SITE = os.environ.get("KODY2DAY_SITE", "https://kody-w.github.io/kody2day").rstrip("/")
ACTIONS = ("today", "day", "catchup", "repo", "days", "links", "impact", "build", "note")
PRIVATE_HOME = Path(os.environ.get("KODY2DAY_HOME", "") or (Path.home() / ".rapp" / "kody2day-private")).expanduser()
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _get(path, timeout=30):
    url = "%s/%s" % (SITE, path.lstrip("/"))
    req = urllib.request.Request(url, headers={"User-Agent": "kody2day-agent/1.0", "Cache-Control": "no-cache"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8")), None
    except urllib.error.HTTPError as e:
        return None, "%s -> HTTP %s" % (url, e.code)
    except Exception as e:
        return None, "%s -> %s: %s" % (url, type(e).__name__, e)


def _brief(d, per_repo=5, include_fleet=True):
    """A digest trimmed to what a reader (or a model) needs to narrate a day."""
    repos = []
    for t in d.get("repos", []):
        row = {"repo": t["repo"], "url": t["url"], "kody_commits": t["human_count"], "fleet_commits": t["fleet_count"],
               "shipped": [c["subject"] for c in t.get("human", [])[:per_repo]]}
        if t.get("new"):
            row["new_repo"] = True
        if t.get("description"):
            row["about"] = t["description"]
        if include_fleet and t["fleet_count"] and not t["human_count"]:
            row["fleet_sample"] = [c["subject"] for c in t.get("fleet", [])[:2]]
        repos.append(row)
    return {"date": d.get("date"), "totals": d.get("totals"), "note": d.get("note") or "",
            "page": d.get("page"), "repos": repos}


class Kody2day(BasicAgent):
    def __init__(self):
        self.name = "Kody2day"
        self.metadata = {
            "name": self.name,
            "description": (
                "What did Kody ship? action='today' returns the latest daily digest of Kody's public GitHub "
                "(repos touched, his own commits with subject lines, the fleet's automated commit counts, new "
                "repos, an editor's note when there is one). action='day' with date=YYYY-MM-DD for a past day; "
                "action='catchup' with days=N for the last N days in one answer; action='repo' with repo=<name> "
                "for everything that landed in one repo over the last N days; action='days' lists every "
                "published day; action='links' gives the site, latest.json and RSS. Use for 'what's Kody up "
                "to', 'catch me up', 'what changed in <repo>', 'kody2day', or anything about following Kody's work. "
                "Summarize the 'shipped' lines in your own words for the reader; link the page."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": list(ACTIONS), "description": "Default: today."},
                    "window": {"type": "string", "enum": ["last_7d", "last_30d", "all_time"], "description": "impact: which window to expand (default last_7d)."},
                    "date": {"type": "string", "description": "day/build/note: YYYY-MM-DD (UTC)."},
                    "days": {"type": "integer", "description": "catchup/repo: how many recent days (default 3, max 30)."},
                    "repo": {"type": "string", "description": "repo: repository name, e.g. 'rapp-sentinel'."},
                    "per_repo": {"type": "integer", "description": "How many of Kody's commit subjects to return per repo (default 5)."},
                    "text": {"type": "string", "description": "note: the editor's note to save (markdown)."},
                    "code_dir": {"type": "string", "description": "build/note: a local checkout of kody-w/kody2day (default ~/Documents/GitHub/kody2day)."},
                    "hours": {"type": "integer", "description": "build: window length in hours (default 24)."},
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── read the public site ─────────────────────────────────────────────
    def _today(self, per_repo):
        d, err = _get("latest.json")
        if err:
            return {"status": "error", "message": err}
        return {"status": "success", "digest": _brief(d, per_repo)}

    def _day(self, date, per_repo):
        if not date or not DATE_RE.match(date):
            return {"status": "error", "message": "date must be YYYY-MM-DD"}
        d, err = _get("daily/%s.json" % date)
        if err:
            return {"status": "error", "message": "no digest for %s (%s) — action='days' lists what exists" % (date, err)}
        return {"status": "success", "digest": _brief(d, per_repo)}

    def _archive(self):
        arc, err = _get("archive.json")
        if err:
            return None, err
        return [a for a in arc if isinstance(a, dict) and DATE_RE.match(str(a.get("date", "")))], None

    def _catchup(self, days, per_repo):
        arc, err = self._archive()
        if err:
            return {"status": "error", "message": err}
        out = []
        for a in arc[:days]:
            d, e = _get("daily/%s.json" % a["date"])
            if d:
                out.append(_brief(d, per_repo))
        return {"status": "success", "days": len(out), "digests": out,
                "totals": {"kody_commits": sum((x["totals"] or {}).get("human_commits", 0) for x in out),
                           "fleet_commits": sum((x["totals"] or {}).get("fleet_commits", 0) for x in out),
                           "repos": sorted({r["repo"] for x in out for r in x["repos"]})}}

    def _repo(self, repo, days, per_repo):
        if not repo:
            return {"status": "error", "message": "repo is required, e.g. repo='rapp-sentinel'"}
        arc, err = self._archive()
        if err:
            return {"status": "error", "message": err}
        want = repo.lower().split("/")[-1]
        hits = []
        for a in arc[:days]:
            d, e = _get("daily/%s.json" % a["date"])
            for t in (d or {}).get("repos", []):
                if t["repo"].lower() == want:
                    hits.append({"date": d["date"], "kody_commits": t["human_count"], "fleet_commits": t["fleet_count"],
                                 "shipped": [{"sha": c["sha"], "subject": c["subject"], "url": c["url"]}
                                             for c in t.get("human", [])[:per_repo]],
                                 "page": d.get("page")})
        return {"status": "success", "repo": repo, "days_searched": min(days, len(arc)), "hits": hits}

    def _days(self):
        arc, err = self._archive()
        if err:
            return {"status": "error", "message": err}
        return {"status": "success", "count": len(arc), "days": arc}

    @staticmethod
    def _links():
        return {"status": "success", "site": SITE + "/", "latest_json": SITE + "/latest.json",
                "rss": SITE + "/feed.xml", "source": "https://github.com/kody-w/kody2day",
                "share_line": "Kody2day — a daily digest of what Kody shipped, so you can keep up: %s/" % SITE}

    @staticmethod
    def _impact(window, per_repo):
        p = PRIVATE_HOME / "docs" / "impact.json"
        if not p.exists():
            return {"status": "error", "message": "no private ledger at %s — run KODY2DAY_PRIVATE=1 python3 kody2day.py build "
                                                  "(or the com.rapp.kody2day-private launchd job) on the owner's machine" % p}
        try:
            imp = json.loads(p.read_text())
        except Exception as e:
            return {"status": "error", "message": "ledger unreadable: %s" % e}
        w = imp.get(window) or {}
        return {"status": "success", "private": True, "local_only": str(p), "as_of": imp.get("as_of"),
                "generated": imp.get("generated"), "days_on_record": imp.get("days_on_record"),
                "streak_days": imp.get("streak_days"),
                "windows": {k: {kk: vv for kk, vv in (imp.get(k) or {}).items() if kk != "per_repo"}
                            for k in ("last_7d", "last_30d", "all_time")},
                "window": window, "per_repo": (w.get("per_repo") or [])[:max(per_repo, 10)],
                "series": (imp.get("series") or [])[-14:], "page": "file://%s" % (PRIVATE_HOME / "docs" / "impact.html")}

    # ── maintainer side (needs a local checkout) ─────────────────────────
    @staticmethod
    def _checkout(params):
        raw = (params.get("code_dir") or "").strip()
        code = Path(raw).expanduser() if raw else Path.home() / "Documents" / "GitHub" / "kody2day"
        if not (code / "kody2day.py").exists():
            return None, "%s is not a kody2day checkout (git clone https://github.com/kody-w/kody2day)" % code
        return code, None

    def _build(self, params):
        code, err = self._checkout(params)
        if err:
            return {"status": "error", "message": err}
        argv = [sys.executable, "kody2day.py", "build"]
        if params.get("date"):
            if not DATE_RE.match(str(params["date"])):
                return {"status": "error", "message": "date must be YYYY-MM-DD"}
            argv += ["--date", str(params["date"])]
        if params.get("hours"):
            argv += ["--hours", str(int(params["hours"]))]
        try:
            r = subprocess.run(argv, capture_output=True, text=True, timeout=600, cwd=str(code), stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            return {"status": "error", "message": "build timed out"}
        if r.returncode != 0:
            return {"status": "error", "message": (r.stderr or r.stdout)[-800:]}
        try:
            summary = json.loads(r.stdout)
        except Exception:
            summary = {"raw": r.stdout[-800:]}
        return {"status": "success", "built": summary, "docs": str(code / "docs"),
                "next": "commit + push docs/ (or let the daily cron publish); the site updates via Pages"}

    def _note(self, params):
        code, err = self._checkout(params)
        if err:
            return {"status": "error", "message": err}
        date = str(params.get("date") or "")
        text = (params.get("text") or "").strip()
        if not DATE_RE.match(date) or not text:
            return {"status": "error", "message": "note needs date=YYYY-MM-DD and text"}
        p = code / "docs" / "notes" / ("%s.md" % date)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text + "\n")
        return {"status": "success", "path": str(p), "next": "action='build' with the same date renders it at the top of the page"}

    # ── entry ────────────────────────────────────────────────────────────
    def perform(self, **kwargs):
        params = dict(kwargs)
        action = (params.get("action") or "today").strip().lower()
        try:
            per_repo = max(1, min(25, int(params.get("per_repo") or 5)))
        except (TypeError, ValueError):
            per_repo = 5
        try:
            days = max(1, min(30, int(params.get("days") or 3)))
        except (TypeError, ValueError):
            days = 3
        try:
            if action == "today":
                out = self._today(per_repo)
            elif action == "day":
                out = self._day(str(params.get("date") or ""), per_repo)
            elif action == "catchup":
                out = self._catchup(days, per_repo)
            elif action == "repo":
                out = self._repo(str(params.get("repo") or ""), max(days, 7) if not params.get("days") else days, per_repo)
            elif action == "days":
                out = self._days()
            elif action == "links":
                out = self._links()
            elif action == "impact":
                out = self._impact(str(params.get("window") or "last_7d"), per_repo)
            elif action == "build":
                out = self._build(params)
            elif action == "note":
                out = self._note(params)
            else:
                out = {"status": "error", "message": "unknown action %r; one of %s" % (action, list(ACTIONS))}
        except Exception as e:
            out = {"status": "error", "message": "%s: %s" % (type(e).__name__, e)}
        return json.dumps(out, indent=2, default=str)


if __name__ == "__main__":
    a = Kody2day()
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
