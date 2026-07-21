"""
GitWarehouse — a "data-journalist twin" that turns any repo's data into a queryable, time-tracked
warehouse using the public git-scraping + Datasette methodology (the pattern popularized by Simon
Willison): commit data to git on every change so the GIT HISTORY itself becomes a time-series
database, shape it with a small .py on each commit, and serve/query it with Datasette.

It does the real work deterministically (run the shaper, scrape into git, compute the Datasette
command + stats) and returns a persona_directive so the host brainstem LLM can explain the result
in a pragmatic, build-small-tools data voice. (Receipts engine + host-voice pattern — the agent
gathers the grounded facts; the host supplies the voice.)

Everything is injectable: point it at any repo, any shaper script, any data glob. Nothing is
hardcoded; no PII. Drop-in (BasicAgent), no core changes. Needs git on PATH; Datasette is optional
(it returns the exact command to run rather than requiring it installed).

Actions:
  shape    run the shaper .py over the repo's data -> (re)build the warehouse files; return stats
  scrape   shape, then git add+commit the warehouse (the git-scraper step: history = time-series)
  serve    return the Datasette command + metadata to query the warehouse locally
  history  summarize how the warehouse has changed over git commits (the time axis)
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/git_warehouse_agent",
    "version": "1.0.1",
    "display_name": "Git Warehouse",
    "description": "Builds a queryable git-tracked warehouse from any repo's data by running a shaper script, committing on change, and emitting the Datasette command.",
    "author": "kody-w",
    "tags": [
        "data",
        "datasette",
        "git-scraping",
        "warehouse",
        "devtools"
    ],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}

import os, json, subprocess, shutil


try:
    from agents.basic_agent import BasicAgent  # RAR layout
except Exception:
    try:
        from basic_agent import BasicAgent
    except Exception:
        try:
            from openrappter.agents.basic_agent import BasicAgent
        except Exception:
            class BasicAgent:
                def __init__(self, name=None, metadata=None):
                    if name is not None: self.name = name
                    if metadata is not None: self.metadata = metadata
                def perform(self, **k): return "Not implemented."


def _have(b): return shutil.which(b) is not None


def _git(repo, *args, timeout=60):
    try:
        r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, timeout=timeout)
        return r.returncode, (r.stdout or "").strip(), (r.stderr or "").strip()
    except Exception as e:
        return 1, "", str(e)


class GitWarehouseAgent(BasicAgent):
    def __init__(self):
        self.name = "GitWarehouse"
        self.metadata = {
            "name": self.name,
            "description": (
                "Turn any repository's data into a queryable, time-tracked warehouse using the public "
                "git-scraping + Datasette methodology (commit data to git on every change so the git history "
                "becomes a time-series database; shape it with a small .py on each commit; query it with Datasette). "
                "Use when the user wants to: build/refresh a data warehouse from files in a repo, 'git-scrape' a "
                "dataset so changes are tracked over time, prepare data for Datasette, or get a queryable view of a "
                "growing dataset. ACTIONS: 'shape' runs a shaper .py over the repo's data to (re)build warehouse "
                "files and returns row/table stats; 'scrape' does shape then git add+commit the warehouse so the "
                "commit history is the time-series (the heart of the pattern); 'serve' returns the exact `datasette` "
                "command + metadata to query the warehouse locally; 'history' summarizes how the warehouse changed "
                "across recent commits (the time axis). Everything is injectable: 'repo' (the git repo path), "
                "'shaper' (path to the build/shape .py to run, relative to repo or absolute), 'warehouse' (the output "
                "dir, default 'warehouse'), and 'message' (the commit message). It returns the grounded stats AND a "
                "persona_directive so you can explain the result in a pragmatic, ship-small-tools data voice."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["shape", "scrape", "serve", "history"],
                               "description": "shape = run the shaper to (re)build the warehouse; scrape = shape then git-commit it (history becomes the time-series); serve = return the datasette command; history = summarize warehouse changes over commits. Default scrape."},
                    "repo": {"type": "string", "description": "Absolute path to the git repository whose data to warehouse. Required for all actions."},
                    "shaper": {"type": "string", "description": "Path to the shaper .py to run (the script that reads the repo's raw data and emits the warehouse files). Relative to repo or absolute. Defaults to 'warehouse/build.py'."},
                    "warehouse": {"type": "string", "description": "Warehouse output directory within the repo (where the shaper writes events.jsonl / frames.jsonl / metadata.json / stats.json). Default 'warehouse'."},
                    "message": {"type": "string", "description": "For scrape: the git commit message. Defaults to a timestamped git-scraper-style message."},
                    "push": {"type": "boolean", "description": "For scrape: also `git push` after committing (publishes the warehouse). Default false."},
                },
                "required": ["repo"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _run_shaper(self, repo, shaper, warehouse):
        sp = shaper if os.path.isabs(shaper) else os.path.join(repo, shaper)
        if not os.path.exists(sp):
            return {"status": "error", "error": "shaper not found: %s" % sp}
        py = os.path.expanduser("~/.brainstem/venv/bin/python")
        py = py if os.path.exists(py) else "python3"
        try:
            r = subprocess.run([py, sp, repo], capture_output=True, text=True, timeout=180)
        except Exception as e:
            return {"status": "error", "error": "shaper: %s" % e}
        out = (r.stdout or "").strip()
        try:
            stats = json.loads(out.splitlines()[-1]) if out else {}
        except Exception:
            stats = {"raw": out[:400]}
        whd = os.path.join(repo, warehouse)
        files = sorted(os.path.basename(f) for f in (
            [os.path.join(whd, x) for x in os.listdir(whd)] if os.path.isdir(whd) else []))
        return {"status": "success" if r.returncode == 0 else "degraded", "stats": stats,
                "warehouse_files": files, "stderr": (r.stderr or "")[:200] if r.returncode else ""}

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "scrape").strip().lower()
        repo = os.path.expanduser((kwargs.get("repo") or "").strip())
        if not repo or not os.path.isdir(repo):
            return json.dumps({"status": "error", "error": "repo path required (an existing git repo dir)."})
        shaper = (kwargs.get("shaper") or "warehouse/build.py").strip()
        warehouse = (kwargs.get("warehouse") or "warehouse").strip()

        if action == "serve":
            whd = os.path.join(repo, warehouse)
            meta = os.path.join(warehouse, "metadata.json")
            cmd = "datasette %s --metadata %s" % (whd, os.path.join(repo, meta))
            tip = ("If the warehouse is JSONL, first load it: "
                   "`sqlite-utils insert warehouse.db events %s --nl && datasette warehouse.db -m %s`"
                   % (os.path.join(whd, "events.jsonl"), os.path.join(repo, meta)))
            return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": "serve",
                               "status": "success", "datasette_cmd": cmd, "sqlite_utils_tip": tip,
                               "has_datasette": _have("datasette"),
                               "persona_directive": ("Speak as a pragmatic data-tools builder. Tell the user the one "
                                "command to explore their data locally with Datasette, and note that because it's "
                                "git-scraped, they can also diff any two commits to see exactly what changed and when. "
                                "Keep it concrete and short.")}, indent=2)

        if action == "history":
            rc, out, _ = _git(repo, "log", "--oneline", "-15", "--", warehouse)
            rc2, stat, _ = _git(repo, "log", "--format=%h %ci", "-5", "--", os.path.join(warehouse, "stats.json"))
            return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": "history",
                               "status": "success", "recent_warehouse_commits": out.splitlines()[:15],
                               "stats_snapshots": stat.splitlines()[:5],
                               "persona_directive": ("Explain that the git history of the warehouse IS the time-series: "
                                "each commit is a snapshot, and diffing stats.json across commits shows how the dataset "
                                "grew over time. Point at the recent commits as the timeline.")}, indent=2)

        # shape / scrape
        res = self._run_shaper(repo, shaper, warehouse)
        if res.get("status") == "error":
            return json.dumps({"schema": "rapp-result/1.0", "agent": self.name, "action": action, **res})

        result = {"schema": "rapp-result/1.0", "agent": self.name, "action": action, "status": res["status"],
                  "repo": repo, "warehouse": warehouse, "stats": res.get("stats"),
                  "warehouse_files": res.get("warehouse_files")}

        if action == "scrape":
            _git(repo, "add", warehouse)
            rc, _, _ = _git(repo, "diff", "--cached", "--quiet")
            if rc == 0:
                result["committed"] = False
                result["note"] = "no warehouse changes to commit (data unchanged since last scrape)"
            else:
                msg = (kwargs.get("message") or "").strip() or ("warehouse: git-scrape refresh — %s events"
                       % (res.get("stats", {}).get("events", "?")))
                crc, cout, cerr = _git(repo, "commit", "-m", msg)
                result["committed"] = crc == 0
                result["commit_message"] = msg
                rc3, sha, _ = _git(repo, "rev-parse", "--short", "HEAD")
                result["sha"] = sha if rc3 == 0 else None
                if cerr and crc != 0:
                    result["commit_error"] = cerr[:200]
                if kwargs.get("push"):
                    prc, pout, perr = _git(repo, "push", timeout=120)
                    result["pushed"] = prc == 0
                    if perr and prc != 0:
                        result["push_error"] = perr[:200]
            result["persona_directive"] = ("Speak as a pragmatic data-tools builder in the git-scraping tradition. "
                "Report what the warehouse now holds (events/frames/episodes from the stats), and emphasize the key "
                "idea: the data is committed to git, so the commit history is a free, queryable time-series — they can "
                "diff commits to see exactly what changed and when, and point Datasette at it to explore. Be concrete, "
                "no hype.")
        else:
            result["persona_directive"] = ("Explain plainly what the shaper produced (the warehouse tables + row "
                "counts from the stats), and suggest the next step: 'scrape' to commit it so the history becomes a "
                "time-series, or 'serve' to query it with Datasette.")
        return json.dumps(result, indent=2)
