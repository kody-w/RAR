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
