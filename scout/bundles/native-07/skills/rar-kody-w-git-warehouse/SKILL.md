---
name: "rar-kody-w-git-warehouse"
description: "Turn any repository's data into a queryable, time-tracked warehouse using the public git-scraping + Datasette methodology (commit data to git on every change so the git history becomes a time-series database; shape it with a small .py on each commit; query it with Datasette). Use when the user wants to: build/refresh a data warehouse from files in a repo, 'git-scrape' a dataset so changes are tracked over time, prepare data for Datasette, or get a queryable view of a growing dataset. ACTIONS: 'shape' runs a shaper .py over the repo's data to (re)build warehouse files and returns row/table stats; 'scrape' does shape then git add+commit the warehouse so the commit history is the time-series (the heart of the pattern); 'serve' returns the exact `datasette` command + metadata to query the warehouse locally; 'history' summarizes how the warehouse changed across recent commits (the time axis). Everything is injectable: 'repo' (the git repo path), 'shaper' (path to the build/shape .py to run, relative to repo or absolute), 'warehouse' (the output dir, default 'warehouse'), and 'message' (the commit message). It returns the grounded stats AND a persona_directive so you can explain the result in a pragmatic, ship-small-tools data voice."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/git_warehouse_agent", "rar_sha256": "eb7b05da0183c37da67b7c1a480731cce05da42753401aa4df86581373c307c3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["data", "datasette", "git-scraping", "warehouse", "devtools"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `git_warehouse_agent.py` and embedded as the fenced Python below (sha256 eb7b05da0183c37d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `git_warehouse_agent.py` first:

```bash
python3 git_warehouse_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 git_warehouse_agent.py   # or on stdin
python3 git_warehouse_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/git_warehouse_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/git_warehouse_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/git_warehouse_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
