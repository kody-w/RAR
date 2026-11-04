---
name: "rar-kody-w-git-warehouse"
description: "Turn any repository's data into a queryable, time-tracked warehouse using the public git-scraping + Datasette methodology (commit data to git on every change so the git history becomes a time-series database; shape it with a small .py on each commit; query it with Datasette). Use when the user wants to: build/refresh a data warehouse from files in a repo, 'git-scrape' a dataset so changes are tracked over time, prepare data for Datasette, or get a queryable view of a growing dataset. ACTIONS: 'shape' runs a shaper .py over the repo's data to (re)build warehouse files and returns row/table stats; 'scrape' does shape then git add+commit the warehouse so the commit history is the time-series (the heart of the pattern); 'serve' returns the exact `datasette` command + metadata to query the warehouse locally; 'history' summarizes how the warehouse changed across recent commits (the time axis). Everything is injectable: 'repo' (the git repo path), 'shaper' (path to the build/shape .py to run, relative to repo or absolute), 'warehouse' (the output dir, default 'warehouse'), and 'message' (the commit message). It returns the grounded stats AND a persona_directive so you can explain the result in a pragmatic, ship-small-tools data voice."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/git_warehouse_agent", "rar_sha256": "eb7b05da0183c37da67b7c1a480731cce05da42753401aa4df86581373c307c3", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["data", "datasette", "git-scraping", "warehouse", "devtools"]}
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
