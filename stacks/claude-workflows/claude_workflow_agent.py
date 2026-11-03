"""Claude Workflows — run a Claude Managed Agent with dynamic workflows from Brainstem chat.

A "template" is a JSON file holding the agent's config (name, model, system, tools,
multiagent ...), exactly the arguments of client.beta.agents.create. Say "run the
explainer-video template on <topic>" and this agent:
  1. creates that Claude agent once (reused while the template is unchanged, like an image digest),
  2. uploads your files to /mnt/session/uploads/,
  3. starts a session with a hard spending cap,
  4. hands the job to a detached worker that follows the session's events and downloads
     /mnt/session/outputs/ when it is done — so chat never blocks and a Brainstem restart
     doesn't lose the job.
Ask "status" to see phases and runs as they happen, "results" for the files.

Credentials: ANTHROPIC_API_KEY, else the macOS Keychain item named in CLAUDE_WORKFLOW_KEYCHAIN
(default "anthropic-api-backup"). The key is read at run time and never written anywhere.
The Brainstem kernel is never edited.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/claude_workflow_agent",
    "version": "1.0.0",
    "display_name": "ClaudeWorkflows",
    "description": "Runs a Claude Managed Agent with dynamic multi-agent workflows from chat: start a job from a template, watch its phases, collect its output files.",
    "author": "kody-w",
    "tags": ["claude", "managed-agents", "workflows", "multi-agent", "jobs"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import hashlib
import json
import os
import re
import subprocess
import sys
import time
import uuid
from pathlib import Path

import anthropic  # top-level on purpose: the Brainstem kernel pip-installs a missing import

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # worker mode runs this file directly
    BasicAgent = object

NAME = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")
DEFAULT_BUDGET_USD = 5.0
MAX_BUDGET_USD = 50.0


def _home():
    d = Path(os.getenv("CLAUDE_WORKFLOW_HOME") or Path(__file__).resolve().parent.parent / "claude-workflows")
    for sub in ("templates", "jobs"):
        (d / sub).mkdir(parents=True, exist_ok=True)
    return d


def _key():
    if os.getenv("ANTHROPIC_API_KEY"):
        return os.environ["ANTHROPIC_API_KEY"]
    item = os.getenv("CLAUDE_WORKFLOW_KEYCHAIN", "anthropic-api-backup")
    r = subprocess.run(["security", "find-generic-password", "-s", item, "-w"], capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        return r.stdout.strip()
    raise RuntimeError("No Anthropic API key found: set ANTHROPIC_API_KEY or add one to the Keychain "
                       f"as '{item}'.")


def _client():
    return anthropic.Anthropic(api_key=_key())


def _jread(p, default=None):
    return json.loads(p.read_text()) if p.exists() else default


def _jwrite(p, obj):
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(obj, indent=1, default=str))
    os.replace(tmp, p)


def _ensure_agent(client, template_name):
    """Create the Claude agent for a template once; reuse it while the template is unchanged."""
    tp = _home() / "templates" / f"{template_name}.json"
    if not tp.exists():
        raise ValueError(f"There is no template called {template_name}.")
    cfg = json.loads(tp.read_text())
    digest = hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:16]
    reg_p = _home() / "agents.json"
    reg = _jread(reg_p, {})
    hit = reg.get(template_name)
    if hit and hit.get("digest") == digest:
        return hit
    agent = client.beta.agents.create(**cfg)
    reg[template_name] = {"id": agent.id, "version": agent.version, "digest": digest}
    _jwrite(reg_p, reg)
    return reg[template_name]


def _ensure_environment(client):
    reg_p = _home() / "agents.json"
    reg = _jread(reg_p, {})
    if reg.get("_environment"):
        return reg["_environment"]
    env = client.beta.environments.create(
        name="brainstem-claude-workflows",
        config={"type": "cloud", "networking": {"type": "limited"}},  # no outside traffic from the sandbox
    )
    reg["_environment"] = env.id
    _jwrite(reg_p, reg)
    return env.id


# ── the detached worker ─────────────────────────────────────────────────────────────────
def follow(job_id):
    """Follow one session to the end, log its events, then download its outputs."""
    jd = _home() / "jobs" / job_id
    job = _jread(jd / "job.json")
    client = _client()
    log = open(jd / "events.jsonl", "a")
    open_runs, phases, seen = set(job.get("open_runs", [])), {}, set()

    def note(**kw):
        kw["at"] = time.strftime("%H:%M:%S")
        log.write(json.dumps(kw, default=str) + "\n")
        log.flush()

    def save(**kw):
        job.update(kw, open_runs=sorted(open_runs))
        _jwrite(jd / "job.json", job)

    for attempt in range(20):  # reconnect a dropped stream; send the task only once
        try:
            with client.beta.sessions.events.stream(session_id=job["session_id"]) as stream:
                if not job.get("sent"):
                    client.beta.sessions.events.send(session_id=job["session_id"], events=[{
                        "type": "user.message", "content": [{"type": "text", "text": job["task"]}]}])
                    save(sent=True, state="running")
                for ev in stream:
                    if getattr(ev, "id", None) in seen:
                        continue
                    seen.add(getattr(ev, "id", None))
                    t = ev.type
                    if t == "agent.message":
                        text = "".join(b.text for b in ev.content if getattr(b, "type", "") == "text")
                        note(type="message", text=text[:2000])
                        save(last_message=text[:2000])
                    elif t == "workflow_run.created":
                        open_runs.add(ev.workflow_run_id)
                        for ph in ev.phases or []:
                            phases[ph.id] = ph.name
                        note(type="run_started", run=ev.workflow_run_id, name=ev.name,
                             phases=[p.name for p in ev.phases or []])
                        save()
                    elif t == "workflow_run.phase_started":
                        note(type="phase_started", run=ev.workflow_run_id,
                             phase=phases.get(ev.workflow_run_phase_id, ev.workflow_run_phase_id))
                    elif t == "workflow_run.phase_ended":
                        note(type="phase_ended", run=ev.workflow_run_id,
                             phase=phases.get(ev.workflow_run_phase_id, ev.workflow_run_phase_id))
                    elif t == "workflow_run.error":
                        note(type="run_error", run=ev.workflow_run_id, error=getattr(ev.error, "message", str(ev.error)))
                    elif t == "workflow_run.status_ended":
                        open_runs.discard(ev.workflow_run_id)
                        note(type="run_ended", run=ev.workflow_run_id, result=ev.result.type)
                        save()
                    elif t == "session.thread_created":
                        ag = getattr(ev, "agent", None) or getattr(getattr(ev, "session_thread", None), "agent", None)
                        note(type="agent_started", name=getattr(ag, "name", None) or "helper")
                    elif t in ("agent.tool_use", "agent.mcp_tool_use") and getattr(ev, "evaluated_permission", None) == "ask":
                        # Nobody is watching: never approve blindly.
                        client.beta.sessions.events.send(session_id=job["session_id"], events=[{
                            "type": "user.tool_confirmation", "tool_use_id": ev.id, "result": "deny"}])
                        note(type="denied", tool=getattr(ev, "name", "?"))
                    elif t == "session.error":
                        note(type="error", error=str(getattr(ev, "error", ""))[:300])
                    elif t == "session.status_idle":
                        why = ev.stop_reason.type
                        if why == "end_turn" and not open_runs:
                            return _finish(client, job, jd, note, save, "done")
                        if why == "budget_reached":
                            return _finish(client, job, jd, note, save, "paused_at_budget")
                        if why == "retries_exhausted":
                            note(type="warning", text="the agent gave up on an error; waiting to see if it continues")
                    elif t == "session.status_terminated":
                        return _finish(client, job, jd, note, save, "terminated")
        except Exception as e:  # dropped stream: reconnect
            note(type="reconnect", error=str(e)[:200])
            time.sleep(min(30, 2 ** attempt))
    save(state="lost_track")


def _finish(client, job, jd, note, save, state):
    out = jd / "outputs"
    out.mkdir(exist_ok=True)
    got = []
    for _ in range(4):  # outputs are indexed a few seconds after idle
        files = list(client.beta.files.list(scope_id=job["session_id"], betas=["managed-agents-2026-04-01"]))
        if files:
            for f in files:
                name = Path(f.filename).name
                client.beta.files.download(f.id).write_to_file(out / name)
                got.append(name)
            break
        time.sleep(3)
    try:
        s = client.beta.sessions.retrieve(session_id=job["session_id"])
        cost = getattr(getattr(s, "usage", None), "list_cost", None) or getattr(s, "list_cost", None)
    except Exception:
        cost = None
    if cost is not None and getattr(cost, "amount", None) is not None:  # list cost comes in cents
        cost = f"${int(cost.amount) / 100:.2f} {getattr(cost, 'currency', 'USD')}"
    note(type="finished", state=state, files=got, cost=str(cost) if cost is not None else None)
    save(state=state, files=got, cost=str(cost) if cost is not None else None, ended=time.strftime("%Y-%m-%d %H:%M"))


# ── the chat-facing agent ───────────────────────────────────────────────────────────────
class ClaudeWorkflowAgent(BasicAgent):
    def __init__(self):
        self.name = "ClaudeWorkflows"
        self.metadata = {
            "name": self.name,
            "description": (
                "Runs a Claude Managed Agent (it can split work across many agents in phases) as a "
                "background job. 'templates' lists what it can run; 'run' starts a job (template, task, "
                "optional files = local paths, optional budget_usd, default 5); 'status' shows progress "
                "(job, or the latest); 'results' lists the files it made; 'stop' asks it to stop. "
                "Always confirm the budget with the user before 'run': it spends real money."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["templates", "run", "status", "results", "stop"]},
                    "template": {"type": "string"},
                    "task": {"type": "string", "description": "what the Claude agent should do"},
                    "files": {"type": "array", "items": {"type": "string"},
                              "description": "local file paths to upload to /mnt/session/uploads/"},
                    "budget_usd": {"type": "number", "description": "hard spending cap for the job, in dollars"},
                    "job": {"type": "string", "description": "job id; latest job if left out"},
                },
                "required": ["action"],
            },
        }
        if BasicAgent is not object:
            super().__init__(self.name, self.metadata)

    def perform(self, **kw) -> str:
        try:
            return getattr(self, "_" + kw.get("action", "status"))(**kw)
        except (AttributeError, TypeError) as e:
            return f"Unknown action or bad arguments ({e}). Use templates, run, status, results or stop."
        except Exception as e:
            return f"Claude Workflows hit a problem: {str(e)[:300]}"

    def _templates(self, **_):
        names = sorted(p.stem for p in (_home() / "templates").glob("*.json"))
        if not names:
            return f"No templates yet. Put an agent config JSON in {_home() / 'templates'}."
        out = []
        for n in names:
            cfg = json.loads((_home() / "templates" / f"{n}.json").read_text())
            wf = ((cfg.get("multiagent") or {}).get("workflows") or {}).get("type") == "enabled"
            out.append(f"- {n}: {cfg.get('description', '')} ({'workflows on' if wf else 'single agent'})")
        return "\n".join(out)

    def _run(self, template="", task="", files=None, budget_usd=None, **_):
        if not NAME.match(template or ""):
            return "Which template? Ask me to list templates."
        if not (task or "").strip():
            return "What should it do? Give me the task."
        budget = float(budget_usd or DEFAULT_BUDGET_USD)
        if not 0 < budget <= MAX_BUDGET_USD:
            return f"The budget must be between $0 and ${MAX_BUDGET_USD:.0f}."
        paths = [Path(f).expanduser() for f in (files or [])]
        missing = [str(p) for p in paths if not p.is_file()]
        if missing:
            return f"I can't find these files: {', '.join(missing)}"
        client = _client()
        ag = _ensure_agent(client, template)
        env_id = _ensure_environment(client)
        resources = []
        for p in paths:
            with open(p, "rb") as fh:
                up = client.files.upload(file=(p.name, fh))
            resources.append({"type": "file", "file_id": up.id, "mount_path": f"/mnt/session/uploads/{p.name}"})
        session = client.beta.sessions.create(
            agent={"type": "agent", "id": ag["id"], "version": ag["version"]},
            environment_id=env_id,
            title=f"{template}: {task[:60]}",
            resources=resources,
            budget={"type": "limit", "max_list_cost": {"amount": str(int(round(budget * 100))), "currency": "USD"}},
        )
        job_id = time.strftime("%Y%m%d-%H%M%S-") + uuid.uuid4().hex[:4]
        jd = _home() / "jobs" / job_id
        jd.mkdir()
        _jwrite(jd / "job.json", {"job": job_id, "template": template, "task": task, "budget_usd": budget,
                                  "session_id": session.id, "state": "starting", "sent": False,
                                  "started": time.strftime("%Y-%m-%d %H:%M"), "uploads": [p.name for p in paths]})
        subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "--follow", job_id],
                         stdout=open(jd / "worker.log", "w"), stderr=subprocess.STDOUT,
                         env={**os.environ, "CLAUDE_WORKFLOW_HOME": str(_home())}, start_new_session=True)
        return (f"Started job {job_id} on the {template} template with a ${budget:.2f} cap. "
                f"It runs in the background; ask me for its status any time. "
                f"Live trace: https://platform.claude.com/workspaces/default/sessions/{session.id}")

    def _job(self, job):
        jobs = sorted(p.name for p in (_home() / "jobs").iterdir() if p.is_dir())
        if not jobs:
            raise ValueError("There are no jobs yet.")
        jid = job or jobs[-1]
        if jid not in jobs:
            raise ValueError(f"There is no job {jid}.")
        return jid, _home() / "jobs" / jid

    def _status(self, job="", **_):
        jid, jd = self._job(job)
        j = _jread(jd / "job.json")
        evs = [json.loads(l) for l in (jd / "events.jsonl").read_text().splitlines()] if (jd / "events.jsonl").exists() else []
        words = {"starting": "starting", "running": "working", "done": "finished",
                 "paused_at_budget": "paused: it reached its spending cap", "terminated": "stopped by the server",
                 "lost_track": "the worker lost the connection; the session may still be running"}
        lines = [f"Job {jid} ({j['template']}): {words.get(j['state'], j['state'])}."]
        for e in evs:
            if e["type"] == "run_started":
                lines.append(f"- {e['at']} started a team run \"{e.get('name')}\" with phases: {', '.join(e.get('phases') or [])}")
            elif e["type"] in ("phase_started", "phase_ended"):
                lines.append(f"- {e['at']} {e['phase']}: {'started' if e['type'] == 'phase_started' else 'done'}")
            elif e["type"] == "run_ended":
                lines.append(f"- {e['at']} team run ended: {e['result']}")
            elif e["type"] in ("run_error", "error", "denied"):
                lines.append(f"- {e['at']} {e['type'].replace('_', ' ')}: {e.get('error') or e.get('tool')}")
        helpers = sum(e["type"] == "agent_started" for e in evs)
        if helpers:
            lines.append(f"{helpers} helper agent(s) have worked on it so far.")
        if j.get("last_message"):
            lines.append(f"Latest from Claude: {j['last_message'][:600]}")
        if j.get("files"):
            lines.append(f"Files: {', '.join(j['files'])} in {jd / 'outputs'}")
        if j.get("cost"):
            lines.append(f"Cost: {j['cost']}")
        return "\n".join(lines[-25:])

    def _results(self, job="", **_):
        jid, jd = self._job(job)
        j = _jread(jd / "job.json")
        if j["state"] in ("starting", "running"):
            return f"Job {jid} is still working. Ask for its status."
        files = sorted((jd / "outputs").glob("*")) if (jd / "outputs").exists() else []
        if not files:
            return f"Job {jid} ended ({j['state']}) without output files."
        return f"Job {jid} made {len(files)} file(s):\n" + "\n".join(f"- {f}" for f in files)

    def _stop(self, job="", **_):
        jid, jd = self._job(job)
        j = _jread(jd / "job.json")
        if j["state"] not in ("starting", "running"):
            return f"Job {jid} isn't running ({j['state']})."
        _client().beta.sessions.events.send(session_id=j["session_id"], events=[{
            "type": "user.message",
            "content": [{"type": "text", "text": "Please stop your workflow runs now and tell me what finished."}]}])
        return f"Asked job {jid} to stop. Its team runs will end and it will report what finished."


if __name__ == "__main__" and len(sys.argv) == 3 and sys.argv[1] == "--follow":
    follow(sys.argv[2])
