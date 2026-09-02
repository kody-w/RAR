---
name: "rar-kody-w-git-warehouse"
description: "Turn any repository's data into a queryable, time-tracked warehouse using the public git-scraping + Datasette methodology (commit data to git on every change so the git history becomes a time-series database; shape it with a small .py on each commit; query it with Datasette). Use when the user wants to: build/refresh a data warehouse from files in a repo, 'git-scrape' a dataset so changes are tracked over time, prepare data for Datasette, or get a queryable view of a growing dataset. ACTIONS: 'shape' runs a shaper .py over the repo's data to (re)build warehouse files and returns row/table stats; 'scrape' does shape then git add+commit the warehouse so the commit history is the time-series (the heart of the pattern); 'serve' returns the exact `datasette` command + metadata to query the warehouse locally; 'history' summarizes how the warehouse changed across recent commits (the time axis). Everything is injectable: 'repo' (the git repo path), 'shaper' (path to the build/shape .py to run, relative to repo or absolute), 'warehouse' (the output dir, default 'warehouse'), and 'message' (the commit message). It returns the grounded stats AND a persona_directive so you can explain the result in a pragmatic, ship-small-tools data voice."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/git_warehouse_agent", "rar_sha256": "2848608c2c13c7ff65f8d434845cb522b4940049c6207d80a604c2da54a57ad2", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "git_warehouse_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/git-warehouse:97c419af073cfc8f4deef66df66baaa853abedd83d8031896124177b14e8c2c6", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["data", "datasette", "git-scraping", "warehouse", "devtools"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/git_warehouse_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `git_warehouse_agent.py` is
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
