"""dynamic_workflow_agent.py - save, run and never lose governed multi-subagent workflows.

A dynamic workflow is a small JavaScript `run(ctx)` body that governs a fleet of subagents: `ctx.agent` spawns
one, `ctx.parallel` / `ctx.pipeline` fan them out, `ctx.step` and `ctx.pause` journal progress. GitHub Copilot CLI
runs these natively ("Dynamic Workflows") - but only in a session that has extensions configured, and a workflow
authored in a session lives only as long as that session. This agent is where they live instead:

  LIBRARY  Every workflow is saved as ~/.rapp/workflows/library/<name>.json (meta, run source, sha256, version).
           Built-ins ship inside this file: `adversarial-fleet` (review -> refute -> triage -> build -> prove) and
           `reflect` (reverse-engineer a locally run AI tool -> generate a beside agent.py that feeds RAPP Buzz).
  ENGINE   Runs any saved workflow on this machine with the same ctx semantics as Copilot's; each subagent is a
           headless `copilot -p` session. Every result is journaled, so a crash or a restart RESUMES the run:
           finished agents replay from the journal, a subagent still running is adopted, and one that was killed
           continues in its own Copilot session with its context kept.
  COPILOT  `install_copilot` writes a user-level Copilot CLI extension that registers every saved workflow
           natively in each new Copilot session that has experimental features on (copilot --experimental);
           `export` prints the exact payload to author one by hand.

Actions: list, show, save, save_preset, export, install_copilot, mount, unmount, run, status, runs, result, resume,
cancel. `mount` writes a copy of this file bound to ONE workflow into a Brainstem's agents/ folder: the Brainstem
hot-loads it on its next request as its own tool (AdversarialFleetWorkflow, ReflectWorkflow...) carrying its
workflow and the engine - a single file that can be shared and cannot lose its workflow. `unmount` removes it.

    DynamicWorkflow(action="run", name="adversarial-fleet", preset="my-round")
    DynamicWorkflow(action="status", run_id="adversarial-fleet-20260930-130200-ab12")
    DynamicWorkflow(action="resume", run_id="...")   # after a crash or a restart
    DynamicWorkflow(action="run", name="reflect", preset="gemini", replay_from="<run id>")  # rerun an improved
                                                     # workflow: identical settled agent calls are not spent again

CLI: python3 dynamic_workflow_agent.py <action> [--name N] [--run-id R] [--preset P] [--args JSON | --args-file F]
     [--meta-file F --run-file F] [--max-concurrent N] [--keep-mcp]

Harness rules, from RAR @rapp/swarm_factory v0.3: errors are data, never content; gates actually gate; a fresh
workspace per run; static bounds; parallel only when safe; opportunistic tiering with graceful fallback.
Stdlib only. Needs `node` and GitHub Copilot CLI (`copilot`) on this machine; nothing leaves it but the
subagents' own model calls.
"""

import argparse
import hashlib
import json
import os
import re
import secrets
import shutil
import signal
import subprocess
import sys
import tempfile
import time

try:
    from agents.basic_agent import BasicAgent
except Exception:  # standalone: python3 dynamic_workflow_agent.py ...
    try:
        from basic_agent import BasicAgent
    except Exception:
        class BasicAgent:
            def __init__(self, name=None, metadata=None):
                self.name = name or getattr(self, "name", "BasicAgent")
                self.metadata = metadata or getattr(self, "metadata", {})

            def perform(self, **kwargs):
                return "Not implemented."


# ---- manifest (mount rewrites this block) ----
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/dynamic_workflow",
    "version": "1.0.0",
    "display_name": "DynamicWorkflow",
    "description": "Save, run and resume governed multi-subagent workflows from a durable library, on a local engine that survives crashes and restarts, and register them natively in every Copilot CLI session.",
    "author": "Kody Wildfeuer",
    "tags": ["workflows", "orchestration", "subagents", "copilot", "durable", "rapp-buzz"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ---- end manifest ----

ENGINE_VERSION = "1.0.0"
NAME_RE = re.compile(r"^[A-Za-z0-9_-]+$")
ACTIONS = ("list", "show", "save", "save_preset", "export", "install_copilot", "mount", "unmount", "run", "status", "runs", "result", "resume", "cancel")
BOUND_ACTIONS = ("run", "status", "runs", "result", "resume", "cancel", "show")
MOUNT_MARK = "# mounted-by: RAPP DynamicWorkflow"
BOUND_WORKFLOW = None  # `mount` binds a copy of this file to one workflow: one hot-loadable tool per workflow
STALE_S = 60

RUNNER_JS = r'''__RUNNER_JS__'''

EXTENSION_JS = r'''__EXTENSION_JS__'''

# ---- builtins (mount rewrites this block) ----
BUILTINS = __BUILTINS__
# ---- end builtins ----


class WorkflowError(Exception):
    """A refusal the caller can act on (bad name, unknown run, missing tool)."""


# ---------------------------------------------------------------- places

def _home():
    return os.environ.get("RAPP_WORKFLOWS_HOME") or os.path.join(os.path.expanduser("~"), ".rapp", "workflows")


def _dir(*parts):
    p = os.path.join(_home(), *parts)
    os.makedirs(p, exist_ok=True)
    return p


def _extensions_dir():
    return os.environ.get("COPILOT_EXTENSIONS_DIR") or os.path.join(os.path.expanduser("~"), ".copilot", "extensions")


def _read_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".tmp-")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)


def _write_json(path, value):
    _write(path, json.dumps(value, indent=1, sort_keys=True) + "\n")


def _tool(name, env_var):
    p = os.environ.get(env_var)
    if p:
        return p
    found = shutil.which(name)
    if found:
        return found
    for d in ("/opt/homebrew/bin", "/usr/local/bin", os.path.expanduser("~/.local/bin"), os.path.expanduser("~/.npm-global/bin")):
        c = os.path.join(d, name)
        if os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    return None


def _sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _version_tuple(v):
    try:
        return tuple(int(x) for x in str(v).split("."))
    except ValueError:
        return (0,)


def _check_name(name, what="workflow"):
    if not name or not NAME_RE.match(str(name)):
        raise WorkflowError("give a %s name made of letters, digits, '-' and '_' (got %r)" % (what, name))
    return str(name)


def _as_obj(value, what):
    if value is None or value == "":
        return None
    if isinstance(value, (dict, list)):
        return value
    try:
        return json.loads(value)
    except (TypeError, ValueError):
        raise WorkflowError("%s must be JSON (an object)" % what)


# ---------------------------------------------------------------- library

def _lib_path(name):
    return os.path.join(_dir("library"), name + ".json")


def _store_workflow(name, meta, run, version, source):
    doc = {"name": name, "version": version, "source": source, "meta": meta, "run": run,
           "sha256": _sha(run), "saved_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "engine": ENGINE_VERSION}
    _write_json(_lib_path(name), doc)
    return doc


def _sync_builtins():
    for name, b in BUILTINS.items():
        cur = _read_json(_lib_path(name))
        if cur is None or (cur.get("source") == "builtin" and _version_tuple(cur.get("version")) < _version_tuple(b["version"])):
            _store_workflow(name, b["meta"], b["run"], b["version"], "builtin")


def _load(name):
    _sync_builtins()
    if BOUND_WORKFLOW and name == BOUND_WORKFLOW:
        b = BUILTINS[name]
        return {"name": name, "version": b["version"], "source": "mounted", "meta": b["meta"], "run": b["run"], "sha256": _sha(b["run"])}
    doc = _read_json(_lib_path(_check_name(name)))
    if not doc:
        raise WorkflowError("no workflow named %r - action=list shows the library" % name)
    return doc


def _node_check(run):
    node = _tool("node", "RAPP_WORKFLOWS_NODE")
    if not node:
        return "not checked (node not found)"
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "check.mjs")
        with open(p, "w", encoding="utf-8") as f:
            f.write("export default (\n" + run + "\n);\n")
        r = subprocess.run([node, "--check", p], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        raise WorkflowError("the run source does not parse: " + (r.stderr.strip().splitlines() or ["?"])[-1])
    return "parses"


def _validate_meta(name, meta):
    if not isinstance(meta, dict):
        raise WorkflowError("meta must be an object with name, description and phases")
    if meta.get("name") != name:
        raise WorkflowError("meta.name must be %r" % name)
    if not isinstance(meta.get("description"), str) or not meta["description"].strip():
        raise WorkflowError("meta.description must say what the workflow does and what args it takes")
    phases = meta.get("phases")
    if not isinstance(phases, list) or not all(isinstance(p, dict) and isinstance(p.get("title"), str) for p in phases):
        raise WorkflowError("meta.phases must be a list of {title, detail?}")
    if "limits" in meta:
        raise WorkflowError("declare limits per run, only from a known cost - not in meta")


# ---------------------------------------------------------------- runs

def _run_dir(run_id):
    if not run_id or not NAME_RE.match(str(run_id)):
        raise WorkflowError("give the run_id that action=run returned (action=runs lists them)")
    d = os.path.join(_dir("runs"), run_id)
    if not os.path.isfile(os.path.join(d, "run.json")):
        raise WorkflowError("no run %r - action=runs lists them" % run_id)
    return d


def _pid_alive(pid, marker):
    if not pid:
        return False
    try:
        os.kill(int(pid), 0)
    except (OSError, ValueError):
        return False
    try:
        cmd = subprocess.run(["ps", "-o", "command=", "-p", str(pid)], capture_output=True, text=True, timeout=5).stdout
    except (OSError, subprocess.SubprocessError):
        return True
    return marker in cmd


def _state(run_dir):
    st = _read_json(os.path.join(run_dir, "state.json"), {}) or {}
    if st.get("status") == "running" and not _pid_alive(st.get("pid"), "runner-"):
        st["status"] = "interrupted"
        st["note"] = "the engine is not running (a crash, a restart or a kill) - action=resume continues it"
    return st


def _progress_tail(run_dir, n):
    lines = []
    try:
        with open(os.path.join(run_dir, "progress.jsonl"), encoding="utf-8") as f:
            for line in f:
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                lines.append("%s %s%s" % (e.get("t", "")[11:19], "## " if e.get("kind") == "phase" else "", e.get("text", "")))
    except OSError:
        pass
    return lines[-n:]


def _mcp_flags():
    """Subagents get the built-in tools only: every configured MCP server is switched off for them (less static
    context, no mail or cloud tools in a fleet)."""
    flags = ["--disable-builtin-mcps"]
    cfg = _read_json(os.path.join(os.path.expanduser("~"), ".copilot", "mcp-config.json"), {}) or {}
    for name in sorted((cfg.get("mcpServers") or {}).keys()):
        flags += ["--disable-mcp-server", name]
    return flags


def _engine_path():
    p = os.path.join(_dir("engine"), "runner-%s.mjs" % _sha(RUNNER_JS)[:12])
    if not os.path.exists(p):
        _write(p, RUNNER_JS)
    return p


def _start(run_dir):
    """Start the engine detached from the caller (double fork through sh): it outlives a Brainstem request, a
    terminal or this process, and never lingers as a zombie of a long-lived host. Its pid comes from state.json."""
    node = _tool("node", "RAPP_WORKFLOWS_NODE")
    if not node:
        raise WorkflowError("node is not installed - the engine needs Node.js (brew install node)")
    env = dict(os.environ)
    env["PATH"] = os.pathsep.join([os.path.dirname(node), "/opt/homebrew/bin", "/usr/local/bin", env.get("PATH", "")])
    env["RAPP_ENGINE_LOG"] = os.path.join(run_dir, "engine.log")
    try:
        os.remove(os.path.join(run_dir, "cancel"))
    except OSError:
        pass
    before = (_read_json(os.path.join(run_dir, "state.json"), {}) or {}).get("attempt", 0)
    sh = subprocess.Popen(["/bin/sh", "-c", '"$@" </dev/null >>"$RAPP_ENGINE_LOG" 2>&1 &', "sh", node, _engine_path(), run_dir],
                          stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                          cwd=run_dir, env=env, start_new_session=True)
    sh.wait(timeout=30)
    for _ in range(100):
        st = _read_json(os.path.join(run_dir, "state.json"), {}) or {}
        if st.get("attempt", 0) > before and st.get("pid"):
            return st["pid"]
        time.sleep(0.1)
    raise WorkflowError("the engine did not start - see %s" % env["RAPP_ENGINE_LOG"])


def _summary_line(st):
    a = st.get("agents") or {}
    return "%s - %s (attempt %s, phase %s; agents running %s, done %s, failed %s, replayed %s)" % (
        st.get("run_id", "?"), st.get("status", "?"), st.get("attempt", "?"), st.get("phase") or "-",
        a.get("running", 0), a.get("done", 0), a.get("failed", 0), a.get("replayed", 0))


# ---------------------------------------------------------------- actions

def act_list(**_):
    _sync_builtins()
    out = []
    for f in sorted(os.listdir(_dir("library"))):
        doc = _read_json(os.path.join(_dir("library"), f))
        if doc and f.endswith(".json"):
            out.append({"name": doc["name"], "version": doc.get("version"), "source": doc.get("source"),
                        "about": doc["meta"]["description"].split(". ")[0][:160]})
    runs = [_state(os.path.join(_dir("runs"), r)) for r in sorted(os.listdir(_dir("runs")), reverse=True)[:8]]
    return {"workflows": out, "recent_runs": [_summary_line(s) for s in runs if s]}


def act_show(name=None, **_):
    doc = _load(name)
    return {"name": doc["name"], "version": doc.get("version"), "source": doc.get("source"), "sha256": doc.get("sha256"),
            "description": doc["meta"]["description"], "phases": [p["title"] for p in doc["meta"]["phases"]],
            "args": sorted(((doc["meta"].get("argsSchema") or {}).get("properties") or {}).keys()),
            "run_source_chars": len(doc["run"]),
            "presets": sorted(p[:-5] for p in os.listdir(_dir("presets", doc["name"])) if p.endswith(".json"))}


def act_save(name=None, meta=None, run=None, version=None, **_):
    name = _check_name(name)
    meta = _as_obj(meta, "meta")
    if not isinstance(run, str) or not run.strip():
        raise WorkflowError("give run: the workflow body as a JavaScript function expression, async (ctx) => { ... }")
    _validate_meta(name, meta)
    parsed = _node_check(run)
    cur = _read_json(_lib_path(name))
    if version is None:
        v = list(_version_tuple(cur.get("version"))) if cur else [1, 0, 0]
        v = (v + [0, 0, 0])[:3]
        version = "1.0.0" if not cur else "%d.%d.%d" % (v[0], v[1], v[2] + 1)
    doc = _store_workflow(name, meta, run, str(version), "saved")
    return {"saved": name, "version": doc["version"], "sha256": doc["sha256"], "source_check": parsed,
            "path": _lib_path(name), "copilot": "native in new Copilot sessions started with --experimental, once action=install_copilot has run"}


def act_save_preset(name=None, preset=None, args=None, **_):
    doc = _load(name)
    preset = _check_name(preset, "preset")
    args = _as_obj(args, "args")
    if not isinstance(args, dict):
        raise WorkflowError("give args: the JSON object the workflow receives as ctx.args")
    p = os.path.join(_dir("presets", doc["name"]), preset + ".json")
    _write_json(p, args)
    return {"saved_preset": preset, "workflow": doc["name"], "path": p}


def act_export(name=None, **_):
    doc = _load(name)
    return {"how": "In any Copilot CLI session with extensions: dynamic_workflows_manage(operation='author', meta=<meta>, run=<run>), then run_dynamic_workflow(name=<name>, args=...). Or action=install_copilot once, and every new session has it.",
            "operation": "author", "meta": doc["meta"], "run": doc["run"]}


def act_install_copilot(**_):
    _sync_builtins()
    p = os.path.join(_extensions_dir(), "rapp-workflows", "extension.mjs")
    _write(p, EXTENSION_JS)
    names = sorted(f[:-5] for f in os.listdir(_dir("library")) if f.endswith(".json"))
    return {"installed": p, "registers": names,
            "note": "Copilot CLI sessions with experimental features on (copilot --experimental, or /experimental on once) load it at start: each saved workflow is a native Dynamic Workflow there"}


def _replay_journal(run_dir, replay_from):
    """Seed a new run's journal with the SETTLED agent results of an earlier run. A result is keyed by its exact
    prompt and options, so only identical calls replay - an improved workflow re-spends nothing it did not change.
    Steps and pauses are never carried: their keys are author names, not content. The records of calls that never
    settled (an outage, a crash) are carried too, so the new run continues their own sessions, context kept."""
    src_dir = _run_dir(replay_from)
    src = os.path.join(src_dir, "journal.jsonl")
    n = 0
    out = []
    settled = set()
    try:
        with open(src, encoding="utf-8") as f:
            for line in f:
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                if e.get("kind") == "agent" and e.get("key"):
                    out.append(json.dumps(e) + "\n")
                    settled.add(e["key"])
                    n += 1
    except OSError:
        pass
    if out:
        with open(os.path.join(run_dir, "journal.jsonl"), "w", encoding="utf-8") as f:
            f.writelines(out)
    carried = 0
    agents = os.path.join(src_dir, "agents")
    for name in sorted(os.listdir(agents)) if os.path.isdir(agents) else []:
        rec = _read_json(os.path.join(agents, name)) if name.endswith(".json") else None
        if rec and rec.get("key") and rec["key"] not in settled and rec.get("status") == "exited" and rec.get("session_id"):
            _write_json(os.path.join(run_dir, "agents", name), rec)
            carried += 1
    return n, carried


def act_run(name=None, args=None, preset=None, max_concurrent=None, agent_timeout_s=None, keep_mcp=False, replay_from=None, **_):
    doc = _load(name)
    merged = {}
    if preset:
        p = os.path.join(_dir("presets", doc["name"]), _check_name(preset, "preset") + ".json")
        base = _read_json(p)
        if base is None:
            raise WorkflowError("no preset %r for %s" % (preset, doc["name"]))
        merged.update(base)
    extra = _as_obj(args, "args")
    if extra is not None and not isinstance(extra, dict):
        raise WorkflowError("args must be a JSON object")
    merged.update(extra or {})
    copilot = _tool("copilot", "RAPP_WORKFLOWS_COPILOT")
    if not copilot:
        raise WorkflowError("GitHub Copilot CLI (copilot) is not installed - subagents run as copilot -p sessions")
    if replay_from:
        if _state(_run_dir(replay_from)).get("status") == "running":
            raise WorkflowError("run %s is still running - replay from it once it has settled (or cancel it)" % replay_from)
    run_id = "%s-%s-%s" % (doc["name"], time.strftime("%Y%m%d-%H%M%S"), secrets.token_hex(2))
    run_dir = os.path.join(_dir("runs"), run_id)
    os.makedirs(run_dir)
    replayed, carried = _replay_journal(run_dir, replay_from) if replay_from else (0, 0)
    options = {"max_concurrent": int(max_concurrent or 8), "agent_timeout_s": int(agent_timeout_s or 14400),
               "transient_backoff_s": float(os.environ.get("RAPP_WORKFLOWS_BACKOFF_S", "30")),
               "copilot": copilot, "extra_flags": [] if keep_mcp else _mcp_flags()}
    _write_json(os.path.join(run_dir, "run.json"), {
        "run_id": run_id, "args": merged, "options": options, "preset": preset or None,
        "workflow": {"name": doc["name"], "version": doc.get("version"), "sha256": doc.get("sha256"), "run": doc["run"]}})
    pid = _start(run_dir)
    return {"started": run_id, "engine_pid": pid, "run_dir": run_dir, "replayable_results": replayed,
            "continued_sessions": carried,
            "next": "action=status run_id=%s (it keeps running on its own; after a crash or restart: action=resume)" % run_id}


def act_status(run_id=None, lines=14, **_):
    d = _run_dir(run_id)
    st = _state(d)
    out = {"summary": _summary_line(st), "status": st.get("status"), "phase": st.get("phase"),
           "agents": st.get("agents"), "updated_at": st.get("updated_at"), "progress": _progress_tail(d, int(lines or 14))}
    if st.get("note"):
        out["note"] = st["note"]
    if st.get("error"):
        out["error"] = st["error"].splitlines()[0][:400]
    res = _read_json(os.path.join(d, "result.json"))
    if isinstance(res, dict) and "summary" in res:
        out["result_summary"] = res["summary"]
    return out


def act_runs(**_):
    rows = []
    for r in sorted(os.listdir(_dir("runs")), reverse=True)[:40]:
        st = _state(os.path.join(_dir("runs"), r))
        if st:
            rows.append(_summary_line(st))
    return {"runs": rows}


def act_result(run_id=None, **_):
    d = _run_dir(run_id)
    res = _read_json(os.path.join(d, "result.json"))
    if res is None:
        return {"status": _state(d).get("status"), "result": None, "note": "no result yet"}
    return {"status": _state(d).get("status"), "result": res}


def act_resume(run_id=None, force=False, **_):
    d = _run_dir(run_id)
    st = _state(d)
    if st.get("status") == "running":
        return {"resumed": False, "summary": _summary_line(st), "note": "it is running"}
    if st.get("status") == "completed":
        return {"resumed": False, "summary": _summary_line(st), "note": "it already completed - action=result"}
    if st.get("status") == "cancelled" and not force:
        return {"resumed": False, "summary": _summary_line(st), "note": "it was cancelled on purpose - pass force=true to resume it anyway"}
    pid = _start(d)
    return {"resumed": run_id, "engine_pid": pid, "from": st.get("status"),
            "note": "finished agents replay from the journal; running ones are adopted; killed ones continue their own sessions"}


def act_cancel(run_id=None, **_):
    d = _run_dir(run_id)
    st = _state(d)
    _write(os.path.join(d, "cancel"), time.strftime("%Y-%m-%dT%H:%M:%S%z") + "\n")
    stopped = []
    if st.get("status") == "running":
        try:
            os.kill(int(st["pid"]), signal.SIGTERM)
            stopped.append("engine")
        except (OSError, KeyError, ValueError):
            pass
        for _ in range(50):
            if not _pid_alive(st.get("pid"), "runner-"):
                break
            time.sleep(0.1)
    for f in os.listdir(os.path.join(d, "agents")) if os.path.isdir(os.path.join(d, "agents")) else []:
        rec = _read_json(os.path.join(d, "agents", f)) if f.endswith(".json") else None
        if rec and rec.get("status") == "running" and _pid_alive(rec.get("pid"), ""):
            try:
                os.killpg(int(rec["pid"]), signal.SIGTERM)
                stopped.append(rec.get("label") or str(rec["pid"]))
            except (OSError, ValueError):
                pass
    st = _read_json(os.path.join(d, "state.json"), {}) or {}
    if st.get("status") in ("running", "interrupted", "paused", "error", None):
        st["status"] = "cancelled"
        _write_json(os.path.join(d, "state.json"), st)
    return {"cancelled": run_id, "stopped": stopped}


def _pascal(name):
    return "".join(w[:1].upper() + w[1:] for w in re.split(r"[-_]+", name) if w) + "Workflow"


def _agents_dir(agents_dir):
    if agents_dir:
        d = os.path.abspath(os.path.expanduser(agents_dir))
    else:
        d = os.path.dirname(os.path.abspath(__file__))
        if os.path.basename(d) != "agents" and not os.path.isfile(os.path.join(d, "basic_agent.py")):
            raise WorkflowError("give agents_dir: the agents/ folder of the Brainstem that should host the workflow")
    if not os.path.isdir(d):
        raise WorkflowError("no such folder: %s" % d)
    return d


def _block(src, begin, end, body):
    i, j = src.index(begin), src.index(end)
    return src[:i] + begin + "\n" + body + "\n" + src[j:]


def act_mount(name=None, agents_dir=None, **_):
    """Write this file, bound to one workflow, into a Brainstem's agents/ folder: the Brainstem hot-loads it on
    its next request as one tool (e.g. AdversarialFleetWorkflow) that carries its own workflow and engine."""
    doc = _load(name)
    d = _agents_dir(agents_dir)
    if "\'\'\'" in doc["run"] or "\'\'\'" in json.dumps(doc["meta"]):
        raise WorkflowError("this workflow's source contains a triple quote and cannot be embedded")
    with open(os.path.abspath(__file__), encoding="utf-8") as f:
        src = f.read()
    tool = _pascal(doc["name"])
    snake = re.sub(r"[^a-z0-9]+", "_", doc["name"].lower()).strip("_")
    manifest = dict(__manifest__, name=__manifest__["name"].split("/")[0] + "/" + snake + "_workflow",
                    version=str(doc.get("version") or "1.0.0"), display_name=tool,
                    description=doc["meta"]["description"].split(". ")[0][:240] + ".",
                    tags=["workflow", "dynamic-workflow", doc["name"]])
    src = _block(src, "# ---- manifest (mount rewrites this block) ----", "# ---- end manifest ----",
                 "__manifest__ = " + json.dumps(manifest, indent=4))
    body = ("BUILTINS = {\n    %r: {\n        \"version\": %r,\n        \"meta\": json.loads(r\'\'\'%s\'\'\'),\n"
            "        \"run\": r\'\'\'%s\'\'\',\n    },\n}") % (doc["name"], str(doc.get("version") or "1.0.0"), json.dumps(doc["meta"]), doc["run"])
    src = _block(src, "# ---- builtins (mount rewrites this block) ----", "# ---- end builtins ----", body)
    bound = "BOUND_WORKFLOW = %r  # `mount` bound this copy to one workflow" % doc["name"]
    src = re.sub(r"^BOUND_WORKFLOW = .*$", lambda m: bound, src, count=1, flags=re.M)
    src = re.sub(r'^(""")', lambda m: MOUNT_MARK + " %s (workflow %s %s, sha %s)\n" % (ENGINE_VERSION, doc["name"], doc.get("version"), doc["sha256"][:12]) + m.group(1), src, count=1, flags=re.M)
    path = os.path.join(d, snake + "_workflow_agent.py")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            if MOUNT_MARK not in f.read(400):
                raise WorkflowError("%s exists and was not mounted by this agent - not overwriting it" % path)
    tmp = os.path.join(d, "." + snake + "_workflow.mounting.py")  # never matches the *_agent.py hot-load glob
    _write(tmp, src)
    check = subprocess.run([sys.executable, "-c", "import importlib.util,sys;s=importlib.util.spec_from_file_location('m',sys.argv[1]);"
                            "m=importlib.util.module_from_spec(s);s.loader.exec_module(m);a=m.DynamicWorkflowAgent();print(a.name)", tmp],
                           capture_output=True, text=True, timeout=60, cwd=d)
    if check.returncode != 0 or check.stdout.strip() != tool:
        os.remove(tmp)
        raise WorkflowError("the mounted copy did not load: " + (check.stderr.strip().splitlines() or ["?"])[-1])
    os.replace(tmp, path)
    return {"mounted": path, "tool": tool, "workflow": doc["name"], "version": doc.get("version"),
            "note": "a Brainstem hot-loads it on its next request; action=unmount removes it"}


def act_unmount(name=None, agents_dir=None, **_):
    d = _agents_dir(agents_dir)
    snake = re.sub(r"[^a-z0-9]+", "_", _check_name(name).lower()).strip("_")
    path = os.path.join(d, snake + "_workflow_agent.py")
    if not os.path.exists(path):
        return {"unmounted": False, "note": "nothing mounted for %s in %s" % (name, d)}
    with open(path, encoding="utf-8") as f:
        if MOUNT_MARK not in f.read(400):
            raise WorkflowError("%s was not mounted by this agent - not removing it" % path)
    os.remove(path)
    return {"unmounted": path, "note": "the Brainstem drops the tool on its next request"}


def dispatch(action, **kw):
    allowed = BOUND_ACTIONS if BOUND_WORKFLOW else ACTIONS
    fn = globals().get("act_" + str(action))
    if action not in allowed or fn is None:
        raise WorkflowError("action must be one of: " + ", ".join(allowed))
    if BOUND_WORKFLOW and action not in ("runs",):
        kw = dict(kw, name=BOUND_WORKFLOW) if action in ("run", "show") else kw
    return fn(**kw)


class DynamicWorkflowAgent(BasicAgent):
    def __init__(self):
        if BOUND_WORKFLOW:
            meta = BUILTINS[BOUND_WORKFLOW]["meta"]
            args_schema = meta.get("argsSchema") or {"type": "object"}
            self.name = _pascal(BOUND_WORKFLOW)
            self.metadata = {
                "name": self.name,
                "description": meta["description"] + " Runs survive crashes and restarts: action=status to watch, resume after a restart.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": list(BOUND_ACTIONS), "description": "run starts it; status/result read a run"},
                        "args": dict(args_schema, description="the workflow's arguments (ctx.args)"),
                        "preset": {"type": "string", "description": "a saved set of args for this workflow"},
                        "run_id": {"type": "string", "description": "a run's id (from run or runs)"},
                        "max_concurrent": {"type": "integer", "description": "for run: subagents at once (default 8)"},
                    },
                    "required": ["action"],
                },
            }
            super().__init__(self.name, self.metadata)
            return
        self.name = "DynamicWorkflow"
        self.metadata = {
            "name": self.name,
            "description": ("Save, run and resume governed multi-subagent workflows (a fleet of Copilot subagents that "
                            "review, refute, build and prove) from a durable library; runs survive crashes and restarts. "
                            "Use action=list to see workflows, run to start one, status to watch it, resume after a restart."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": list(ACTIONS), "description": "what to do"},
                    "name": {"type": "string", "description": "workflow name (list shows them)"},
                    "run_id": {"type": "string", "description": "a run's id (from run or runs)"},
                    "preset": {"type": "string", "description": "a saved set of args for the workflow"},
                    "args": {"type": "object", "description": "the JSON object the workflow receives as ctx.args"},
                    "meta": {"type": "object", "description": "for save: {name, description, phases, argsSchema?}"},
                    "run": {"type": "string", "description": "for save: the workflow body, async (ctx) => { ... }"},
                    "max_concurrent": {"type": "integer", "description": "for run: subagents at once (default 8)"},
                    "replay_from": {"type": "string", "description": "for run: an earlier run whose settled identical agent calls are reused"},
                    "agents_dir": {"type": "string", "description": "optional, for mount/unmount - leave it out: it defaults to the agents/ folder this Brainstem loaded me from"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, action=None, **kwargs):
        action = action or ("run" if BOUND_WORKFLOW else "list")
        try:
            out = dispatch(action, **kwargs)
            return json.dumps(out, indent=1, default=str)
        except WorkflowError as e:
            return json.dumps({"status": "refused", "action": action, "reason": str(e)})
        except Exception as e:  # errors are data, never content
            return json.dumps({"status": "error", "action": action, "error": "%s: %s" % (type(e).__name__, e)})


def main(argv=None):
    p = argparse.ArgumentParser(prog="dynamic_workflow_agent.py", description="Save, run and resume governed multi-subagent workflows.")
    p.add_argument("action", nargs="?", default="run" if BOUND_WORKFLOW else "list", choices=BOUND_ACTIONS if BOUND_WORKFLOW else ACTIONS)
    p.add_argument("--name")
    p.add_argument("--run-id")
    p.add_argument("--preset")
    p.add_argument("--args")
    p.add_argument("--args-file")
    p.add_argument("--meta-file")
    p.add_argument("--run-file")
    p.add_argument("--version")
    p.add_argument("--max-concurrent", type=int)
    p.add_argument("--agent-timeout-s", type=int)
    p.add_argument("--keep-mcp", action="store_true")
    p.add_argument("--force", action="store_true")
    p.add_argument("--lines", type=int, default=14)
    p.add_argument("--agents-dir")
    p.add_argument("--replay-from")
    a = p.parse_args(argv)
    kw = {"name": a.name, "run_id": a.run_id, "preset": a.preset, "max_concurrent": a.max_concurrent,
          "agent_timeout_s": a.agent_timeout_s, "keep_mcp": a.keep_mcp, "force": a.force, "lines": a.lines,
          "agents_dir": a.agents_dir, "replay_from": a.replay_from}
    if a.args_file:
        with open(a.args_file, encoding="utf-8") as f:
            kw["args"] = json.load(f)
    elif a.args:
        kw["args"] = a.args
    if a.meta_file:
        with open(a.meta_file, encoding="utf-8") as f:
            kw["meta"] = json.load(f)
    if a.run_file:
        with open(a.run_file, encoding="utf-8") as f:
            kw["run"] = f.read()
    if a.version:
        kw["version"] = a.version
    out = DynamicWorkflowAgent().perform(action=a.action, **{k: v for k, v in kw.items() if v is not None})
    print(out)
    return 0 if '"status": "refused"' not in out and '"status": "error"' not in out else 1


if __name__ == "__main__":
    sys.exit(main())
