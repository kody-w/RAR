---
name: "rar-kody-w-kody2day"
description: "Keep up with Kody: today's digest of what he shipped across his public GitHub, any past day, a multi-day catch-up, or a search by repo \u2014 Kody's own commits separated from the fleet of bots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/kody2day_agent", "rar_sha256": "e4dd13bc20c0f1d3c4333cdbefe6f1e09359a7fc7da5309822248d41ba3b0638", "source_kind": "rar-agent", "source_commit": "12b72173806aa97877273642ec6173ce9d4cb154", "author": "Kody Wildfeuer", "tags": ["digest", "daily", "changelog", "github", "kody", "catch-up", "news"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `kody2day_agent.py` and embedded as the fenced Python below (sha256 e4dd13bc20c0f1d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `kody2day_agent.py` first:

```bash
python3 kody2day_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 kody2day_agent.py   # or on stdin
python3 kody2day_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
