---
name: "rar-kody-w-kody2day"
description: "Keep up with Kody: today's digest of what he shipped across his public GitHub, any past day, a multi-day catch-up, or a search by repo \u2014 Kody's own commits separated from the fleet of bots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/kody2day_agent", "rar_sha256": "e4dd13bc20c0f1d3c4333cdbefe6f1e09359a7fc7da5309822248d41ba3b0638", "source_kind": "rar-agent", "source_commit": "12b72173806aa97877273642ec6173ce9d4cb154", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "kody2day_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/kody2day:5079e9d41f7940357f0047bef606547363c94c6dc8f3af2385a2e6200f8f96a7", "kind": "skill"}, "author": "Kody Wildfeuer", "tags": ["digest", "daily", "changelog", "github", "kody", "catch-up", "news"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/kody2day_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `kody2day_agent.py` is
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
