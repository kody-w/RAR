---
name: "rar-kody-w-kody2day"
description: "Keep up with Kody: today's digest of what he shipped across his public GitHub, any past day, a multi-day catch-up, or a search by repo \u2014 Kody's own commits separated from the fleet of bots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/kody2day_agent", "rar_sha256": "3c0814050b74a0b9f7fb44220ed66600430ab8779601f469be8c20ac86521a99", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "Kody Wildfeuer", "tags": ["digest", "daily", "changelog", "github", "kody", "catch-up", "news"]}
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
