---
name: "rar-kody-w-git-warehouse"
description: "Turn any repository's data into a queryable, time-tracked warehouse using the public git-scraping + Datasette methodology (commit data to git on every change so the git history becomes a time-series database; shape it with a small .py on each commit; query it with Datasette). Use when the user wants to: build/refresh a data warehouse from files in a repo, 'git-scrape' a dataset so changes are tracked over time, prepare data for Datasette, or get a queryable view of a growing dataset. ACTIONS: 'shape' runs a shaper .py over the repo's data to (re)build warehouse files and returns row/table stats; 'scrape' does shape then git add+commit the warehouse so the commit history is the time-series (the heart of the pattern); 'serve' returns the exact `datasette` command + metadata to query the warehouse locally; 'history' summarizes how the warehouse changed across recent commits (the time axis). Everything is injectable: 'repo' (the git repo path), 'shaper' (path to the build/shape .py to run, relative to repo or absolute), 'warehouse' (the output dir, default 'warehouse'), and 'message' (the commit message). It returns the grounded stats AND a persona_directive so you can explain the result in a pragmatic, ship-small-tools data voice."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/git_warehouse_agent", "rar_sha256": "2848608c2c13c7ff65f8d434845cb522b4940049c6207d80a604c2da54a57ad2", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["data", "datasette", "git-scraping", "warehouse", "devtools"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/git_warehouse_agent`. The original RAPP
agent is preserved byte-for-byte in `git_warehouse_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "shape = run the shaper to (re)build the warehouse; scrape = shape then git-commit it (history becomes the time-series); serve = return the datasette command; history = summarize warehouse changes over commits. Default scrape.",
      "enum": [
        "shape",
        "scrape",
        "serve",
        "history"
      ],
      "type": "string"
    },
    "message": {
      "description": "For scrape: the git commit message. Defaults to a timestamped git-scraper-style message.",
      "type": "string"
    },
    "push": {
      "description": "For scrape: also `git push` after committing (publishes the warehouse). Default false.",
      "type": "boolean"
    },
    "repo": {
      "description": "Absolute path to the git repository whose data to warehouse. Required for all actions.",
      "type": "string"
    },
    "shaper": {
      "description": "Path to the shaper .py to run (the script that reads the repo's raw data and emits the warehouse files). Relative to repo or absolute. Defaults to 'warehouse/build.py'.",
      "type": "string"
    },
    "warehouse": {
      "description": "Warehouse output directory within the repo (where the shaper writes events.jsonl / frames.jsonl / metadata.json / stats.json). Default 'warehouse'.",
      "type": "string"
    }
  },
  "required": [
    "repo"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `git_warehouse_agent.py` and embedded as the fenced Python below (sha256 2848608c2c13c7ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `git_warehouse_agent.py` first:

```bash
python3 git_warehouse_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 git_warehouse_agent.py   # or on stdin
python3 git_warehouse_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
