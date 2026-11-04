---
name: "rar-kody-w-project-tracker"
description: "Local-first tracker for a portfolio of AI-agent projects and their MVP statements. Speaks the aibast-agents-library project-tracker web tool's native JSON (projectTrackerData) so data round-trips via its JSON import/export. Add/update projects, set the MVP use case/description/timeline, register agents, and export a file ready to merge-import into the web tool. Data stays on this device \u2014 never in a repo or egg."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/project_tracker_agent", "rar_sha256": "0a9452444854c420edbf73b617d392c1a63510890a663455f69d56a4e4ea0fc6", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "kody-w", "tags": ["project", "tracker", "portfolio", "mvp", "local-first", "aibast", "rapplication"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/project_tracker_agent`. The original RAPP
agent is preserved byte-for-byte in `project_tracker_agent.py` and in the RCI capsule.

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

project_tracker_agent.py — Local-first project & agent portfolio tracker.

A headless, drop-in RAPP agent that manages a portfolio of AI-agent
opportunities in the EXACT data shape of the aibast-agents-library
"local-first project tracker" web tool:

    microsoft.github.io/aibast-agents-library/tools/localfirst_project_tracker_tool.html

Whatever this agent writes exports and imports straight into that tool's
"Merge Import Data (JSON)" (and vice-versa) because it speaks the tool's native
`projectTrackerData` schema:

    appData = {
      "projects": [ { id, customerName, status, type, description, stakeholders,
                      competingSolution, contractDetails, agents:[names], notes,
                      mvpUseCase, mvpDescription, mvpTimeline,
                      createdDate, updatedDate } ],
      "agents":   { "builtin": [ {name, description, category, status} ],
                    "custom":  [ ... ] },
      "timeline": [ { date, title, description } ]
    }

Local-first: the portfolio lives on THIS device at
    $PROJECT_TRACKER_DIR  or  $RAPP_HOME/project-tracker  or  ~/.rapp/project-tracker
as projectTrackerData.json. It is deliberately kept OUTSIDE any twin workspace,
so packing this twin into an .egg carries the *engine*, never the *portfolio*
(which may hold customer data). Nothing here writes customer data into a repo.

Drop into any brainstem's agents/ dir; the next /chat request exposes a
`ProjectTracker` tool. Stdlib + BasicAgent only — no network, no extra deps.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `project_tracker_agent.py` and embedded as the fenced Python below (sha256 0a9452444854c420…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `project_tracker_agent.py` first:

```bash
python3 project_tracker_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 project_tracker_agent.py   # or on stdin
python3 project_tracker_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/project_tracker_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/project_tracker_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/project_tracker_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""project_tracker_agent.py — Local-first project & agent portfolio tracker.

A headless, drop-in RAPP agent that manages a portfolio of AI-agent
opportunities in the EXACT data shape of the aibast-agents-library
"local-first project tracker" web tool:

    microsoft.github.io/aibast-agents-library/tools/localfirst_project_tracker_tool.html

Whatever this agent writes exports and imports straight into that tool's
"Merge Import Data (JSON)" (and vice-versa) because it speaks the tool's native
`projectTrackerData` schema:

    appData = {
      "projects": [ { id, customerName, status, type, description, stakeholders,
                      competingSolution, contractDetails, agents:[names], notes,
                      mvpUseCase, mvpDescription, mvpTimeline,
                      createdDate, updatedDate } ],
      "agents":   { "builtin": [ {name, description, category, status} ],
                    "custom":  [ ... ] },
      "timeline": [ { date, title, description } ]
    }

Local-first: the portfolio lives on THIS device at
    $PROJECT_TRACKER_DIR  or  $RAPP_HOME/project-tracker  or  ~/.rapp/project-tracker
as projectTrackerData.json. It is deliberately kept OUTSIDE any twin workspace,
so packing this twin into an .egg carries the *engine*, never the *portfolio*
(which may hold customer data). Nothing here writes customer data into a repo.

Drop into any brainstem's agents/ dir; the next /chat request exposes a
`ProjectTracker` tool. Stdlib + BasicAgent only — no network, no extra deps.
"""

import json
import os
import re
import time

from agents.basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/project_tracker_agent",
    "version": "1.0.0",
    "display_name": "Project Tracker",
    "description": (
        "Local-first tracker for a portfolio of AI-agent projects and their MVP "
        "statements. Speaks the aibast-agents-library project-tracker web tool's "
        "native JSON (projectTrackerData) so data round-trips via its JSON "
        "import/export. Add/update projects, set the MVP use case/description/"
        "timeline, register agents, and export a file ready to merge-import into "
        "the web tool. Data stays on this device — never in a repo or egg."
    ),
    "author": "kody-w",
    "tags": ["project", "tracker", "portfolio", "mvp", "local-first", "aibast", "rapplication"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {"args": {"action": "list_projects"}},
}


# ── Contract enums (must match the web tool's <option> values exactly) ────────

VALID_STATUS = ("planning", "poc", "active", "production", "completed")
# Must match the web tool's <select id="project-type"> values EXACTLY so a
# project's type renders after a merge-import (no "operations"; IT is "it").
VALID_TYPE = ("legal", "hr", "it", "compliance", "customer-service", "other")
VALID_AGENT_CATEGORY = ("contract", "analysis", "workflow", "integration", "other")
VALID_AGENT_STATUS = ("existing", "new", "required")

# The web tool seeds these 8 builtin agents. Mirror them so an export imports
# cleanly (the tool merges builtin agents by name and won't duplicate).
DEFAULT_BUILTIN_AGENTS = [
    {"name": "SharePointDocumentExtractor", "description": "Extract content from SharePoint documents", "category": "integration", "status": "existing"},
    {"name": "Dynamics365CRUD", "description": "CRUD operations with Dynamics 365", "category": "integration", "status": "existing"},
    {"name": "PowerPoint", "description": "Generate PowerPoint presentations", "category": "other", "status": "existing"},
    {"name": "ManageMemory", "description": "Memory management for conversations", "category": "other", "status": "existing"},
    {"name": "ContractTemplate", "description": "Generate contracts from templates", "category": "contract", "status": "new"},
    {"name": "ContractAnalysis", "description": "Analyze contract content and risks", "category": "analysis", "status": "new"},
    {"name": "ContractRouting", "description": "Route contracts for approval", "category": "workflow", "status": "new"},
    {"name": "ContractMonitoring", "description": "Monitor contract lifecycle", "category": "contract", "status": "new"},
]


# ── Local-first storage ───────────────────────────────────────────────────────

def _rapp_home():
    return os.environ.get("RAPP_HOME") or os.path.join(os.path.expanduser("~"), ".rapp")


def _data_dir():
    return os.environ.get("PROJECT_TRACKER_DIR") or os.path.join(_rapp_home(), "project-tracker")


def _db_path():
    return os.path.join(_data_dir(), "projectTrackerData.json")


def _now_iso():
    return time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime())


def _new_id():
    # Mirror the web tool's Date.now().toString() (epoch millis as a string).
    return str(int(time.time() * 1000))


def _empty_appdata():
    return {
        "projects": [],
        "agents": {"builtin": [dict(a) for a in DEFAULT_BUILTIN_AGENTS], "custom": []},
        "timeline": [],
    }


def _load():
    path = _db_path()
    if not os.path.exists(path):
        return _empty_appdata()
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return _empty_appdata()
    # Normalize shape defensively.
    if not isinstance(data, dict):
        return _empty_appdata()
    data.setdefault("projects", [])
    ag = data.setdefault("agents", {"builtin": [], "custom": []})
    if not isinstance(ag, dict):
        ag = {"builtin": [], "custom": []}
        data["agents"] = ag
    ag.setdefault("builtin", [])
    ag.setdefault("custom", [])
    data.setdefault("timeline", [])
    # Ensure the builtin defaults are present (merge by name, like the tool).
    have = {a.get("name") for a in ag["builtin"] if isinstance(a, dict)}
    for a in DEFAULT_BUILTIN_AGENTS:
        if a["name"] not in have:
            ag["builtin"].append(dict(a))
    return data


def _save(data):
    d = _data_dir()
    os.makedirs(d, exist_ok=True)
    tmp = _db_path() + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, _db_path())


def _timeline(data, title, description):
    data["timeline"].append({"date": _now_iso(), "title": title, "description": description})


# ── Validation / coercion ─────────────────────────────────────────────────────

def _coerce(value, valid, default):
    v = (value or "").strip().lower()
    return v if v in valid else default


def _all_agent_names(data):
    names = set()
    for a in data["agents"]["builtin"] + data["agents"]["custom"]:
        if isinstance(a, dict) and a.get("name"):
            names.add(a["name"])
    return names


def _register_missing_agents(data, agent_names):
    """Any project agent name not already known is registered as a custom
    'required' agent so the web tool renders it in the Agent Library."""
    known = _all_agent_names(data)
    for name in agent_names:
        if name and name not in known:
            data["agents"]["custom"].append({
                "name": name,
                "description": "Referenced by a tracked project",
                "category": "other",
                "status": "required",
            })
            known.add(name)


def _find_project(data, project_id=None, customer_name=None):
    if project_id:
        for p in data["projects"]:
            if p.get("id") == project_id:
                return p
    if customer_name:
        cn = customer_name.strip().lower()
        for p in data["projects"]:
            if (p.get("customerName") or "").strip().lower() == cn:
                return p
    return None


def _project_summary(p):
    return {
        "id": p.get("id"),
        "customerName": p.get("customerName"),
        "status": p.get("status"),
        "type": p.get("type"),
        "mvpUseCase": p.get("mvpUseCase"),
        "agents": p.get("agents", []),
        "updatedDate": p.get("updatedDate"),
    }


# ── Merge (mirrors the web tool's mergeData) ──────────────────────────────────

def _merge(existing, incoming):
    import copy
    merged = copy.deepcopy(existing)
    by_id = {p.get("id"): i for i, p in enumerate(merged["projects"])}
    for np in (incoming.get("projects") or []):
        if not isinstance(np, dict):
            continue
        pid = np.get("id")
        if pid in by_id:
            merged["projects"][by_id[pid]] = {**merged["projects"][by_id[pid]], **np,
                                              "updatedDate": _now_iso()}
        else:
            merged["projects"].append({**np,
                                       "id": pid or _new_id(),
                                       "createdDate": np.get("createdDate") or _now_iso(),
                                       "updatedDate": _now_iso()})
            by_id[np.get("id") or merged["projects"][-1]["id"]] = len(merged["projects"]) - 1
    inc_ag = incoming.get("agents") or {}
    have_builtin = {a.get("name") for a in merged["agents"]["builtin"]}
    for a in (inc_ag.get("builtin") or []):
        if isinstance(a, dict) and a.get("name") not in have_builtin:
            merged["agents"]["builtin"].append(a)
            have_builtin.add(a.get("name"))
    custom_idx = {a.get("name"): i for i, a in enumerate(merged["agents"]["custom"])}
    for a in (inc_ag.get("custom") or []):
        if not isinstance(a, dict):
            continue
        if a.get("name") in custom_idx:
            i = custom_idx[a["name"]]
            merged["agents"]["custom"][i] = {**merged["agents"]["custom"][i], **a}
        else:
            merged["agents"]["custom"].append(a)
            custom_idx[a.get("name")] = len(merged["agents"]["custom"]) - 1
    for ev in (incoming.get("timeline") or []):
        if not isinstance(ev, dict):
            continue
        dup = any(e.get("date") == ev.get("date") and e.get("title") == ev.get("title")
                  for e in merged["timeline"])
        if not dup:
            merged["timeline"].append(ev)
    return merged


# ── The cartridge ─────────────────────────────────────────────────────────────

class ProjectTrackerAgent(BasicAgent):
    def __init__(self):
        self.name = "ProjectTracker"
        self.metadata = {
            "name": self.name,
            "description": (
                "Manage a local-first portfolio of AI-agent projects and their MVP "
                "statements, in the aibast project-tracker web tool's native JSON so "
                "data round-trips via its import/export. Pick an action:\n"
                " • add_project     — create a project (customer_name required)\n"
                " • update_project  — patch fields on a project (by project_id or customer_name)\n"
                " • set_mvp         — set mvp_use_case / mvp_description / mvp_timeline\n"
                " • attach_agents   — set a project's agents to a list of agent names\n"
                " • add_agent       — register a custom agent (name+description)\n"
                " • list_projects   — summaries of all projects\n"
                " • get_project     — full record of one project\n"
                " • stats           — portfolio metrics\n"
                " • export_tracker  — write a JSON file ready to merge-import into the web tool\n"
                " • import_tracker  — merge a web-tool export JSON (path) into local data\n"
                "Data lives on this device only; it never enters a repo or egg."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["add_project", "update_project", "set_mvp", "attach_agents",
                                 "add_agent", "list_projects", "get_project", "stats",
                                 "export_tracker", "import_tracker"],
                        "description": "What to do.",
                    },
                    "project_id": {"type": "string", "description": "Target project id (update/get/set_mvp/attach_agents)."},
                    "customer_name": {"type": "string", "description": "Customer name. Required for add_project; usable as a lookup key elsewhere."},
                    "status": {"type": "string", "enum": list(VALID_STATUS), "description": "Project status. Default 'planning'."},
                    "type": {"type": "string", "enum": list(VALID_TYPE), "description": "Project type. Default 'other'."},
                    "description": {"type": "string", "description": "Project description."},
                    "stakeholders": {"type": "string", "description": "Key stakeholders (free text)."},
                    "competing_solution": {"type": "string", "description": "Competing solution (e.g. Google/AWS)."},
                    "contract_details": {"type": "string", "description": "Contract/commercial details."},
                    "notes": {"type": "string", "description": "Free-form notes."},
                    "mvp_use_case": {"type": "string", "description": "One-line MVP use case."},
                    "mvp_description": {"type": "string", "description": "The MVP statement (paragraphs)."},
                    "mvp_timeline": {"type": "string", "description": "MVP timeline text."},
                    "agents": {"type": "array", "items": {"type": "string"}, "description": "Agent names to attach to the project (attach_agents / add_project)."},
                    "agent_name": {"type": "string", "description": "Custom agent name (add_agent)."},
                    "agent_description": {"type": "string", "description": "Custom agent description (add_agent)."},
                    "agent_category": {"type": "string", "enum": list(VALID_AGENT_CATEGORY), "description": "Custom agent category (add_agent). Default 'other'."},
                    "agent_status": {"type": "string", "enum": list(VALID_AGENT_STATUS), "description": "Custom agent status (add_agent). Default 'new'."},
                    "path": {"type": "string", "description": "File path for export_tracker (output) / import_tracker (input)."},
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "").strip()
        try:
            handler = {
                "add_project": self._add_project,
                "update_project": self._update_project,
                "set_mvp": self._set_mvp,
                "attach_agents": self._attach_agents,
                "add_agent": self._add_agent,
                "list_projects": self._list_projects,
                "get_project": self._get_project,
                "stats": self._stats,
                "export_tracker": self._export_tracker,
                "import_tracker": self._import_tracker,
            }.get(action)
            if handler is None:
                return json.dumps({"status": "error",
                                   "summary": f"unknown action {action!r}. See the tool description for valid actions."})
            return json.dumps(handler(**kwargs))
        except Exception as e:  # never crash the brainstem loop
            return json.dumps({"status": "error", "summary": f"{type(e).__name__}: {e}"})

    # ── add_project ──────────────────────────────────────────────────────────
    def _add_project(self, **k):
        customer = (k.get("customer_name") or "").strip()
        if not customer:
            return {"status": "error", "summary": "customer_name is required for add_project"}
        data = _load()
        if _find_project(data, customer_name=customer):
            return {"status": "error",
                    "summary": f"a project for '{customer}' already exists; use update_project / set_mvp instead"}
        agents = [a for a in (k.get("agents") or []) if isinstance(a, str) and a.strip()]
        _register_missing_agents(data, agents)
        now = _now_iso()
        project = {
            "id": _new_id(),
            "customerName": customer,
            "status": _coerce(k.get("status"), VALID_STATUS, "planning"),
            "type": _coerce(k.get("type"), VALID_TYPE, "other"),
            "description": k.get("description") or "",
            "stakeholders": k.get("stakeholders") or "",
            "competingSolution": k.get("competing_solution") or "",
            "contractDetails": k.get("contract_details") or "",
            "agents": agents,
            "notes": k.get("notes") or "",
            "mvpUseCase": k.get("mvp_use_case") or "",
            "mvpDescription": k.get("mvp_description") or "",
            "mvpTimeline": k.get("mvp_timeline") or "",
            "createdDate": now,
            "updatedDate": now,
        }
        data["projects"].append(project)
        _timeline(data, f"Created new project for {customer}",
                  f"{project['type']} implementation with {len(agents)} agents")
        _save(data)
        return {"status": "ok", "action": "add_project", "id": project["id"],
                "summary": f"Added project '{customer}' (id={project['id']}, status={project['status']}, {len(agents)} agents).",
                "project": _project_summary(project), "db": _db_path()}

    # ── update_project ───────────────────────────────────────────────────────
    def _update_project(self, **k):
        data = _load()
        p = _find_project(data, k.get("project_id"), k.get("customer_name"))
        if not p:
            return {"status": "error", "summary": "project not found (give project_id or an existing customer_name)"}
        field_map = {
            "status": ("status", lambda v: _coerce(v, VALID_STATUS, p.get("status", "planning"))),
            "type": ("type", lambda v: _coerce(v, VALID_TYPE, p.get("type", "other"))),
            "description": ("description", lambda v: v),
            "stakeholders": ("stakeholders", lambda v: v),
            "competing_solution": ("competingSolution", lambda v: v),
            "contract_details": ("contractDetails", lambda v: v),
            "notes": ("notes", lambda v: v),
            "mvp_use_case": ("mvpUseCase", lambda v: v),
            "mvp_description": ("mvpDescription", lambda v: v),
            "mvp_timeline": ("mvpTimeline", lambda v: v),
        }
        changed = []
        for arg, (field, fn) in field_map.items():
            if k.get(arg) is not None:
                p[field] = fn(k.get(arg))
                changed.append(field)
        if k.get("agents") is not None:
            agents = [a for a in k["agents"] if isinstance(a, str) and a.strip()]
            _register_missing_agents(data, agents)
            p["agents"] = agents
            changed.append("agents")
        p["updatedDate"] = _now_iso()
        _timeline(data, f"Updated {p.get('customerName')} project",
                  f"Status: {p.get('status')}, Type: {p.get('type')}")
        _save(data)
        return {"status": "ok", "action": "update_project", "id": p["id"],
                "changed": changed,
                "summary": f"Updated {p.get('customerName')} ({', '.join(changed) or 'no fields'}).",
                "project": _project_summary(p)}

    # ── set_mvp ──────────────────────────────────────────────────────────────
    def _set_mvp(self, **k):
        data = _load()
        p = _find_project(data, k.get("project_id"), k.get("customer_name"))
        if not p:
            return {"status": "error", "summary": "project not found (give project_id or an existing customer_name)"}
        for arg, field in (("mvp_use_case", "mvpUseCase"),
                           ("mvp_description", "mvpDescription"),
                           ("mvp_timeline", "mvpTimeline")):
            if k.get(arg) is not None:
                p[field] = k[arg]
        p["updatedDate"] = _now_iso()
        _timeline(data, f"Set MVP for {p.get('customerName')}",
                  (p.get("mvpUseCase") or "")[:120])
        _save(data)
        return {"status": "ok", "action": "set_mvp", "id": p["id"],
                "summary": f"MVP set for {p.get('customerName')}: {(p.get('mvpUseCase') or '')[:80]}",
                "project": _project_summary(p)}

    # ── attach_agents ────────────────────────────────────────────────────────
    def _attach_agents(self, **k):
        data = _load()
        p = _find_project(data, k.get("project_id"), k.get("customer_name"))
        if not p:
            return {"status": "error", "summary": "project not found"}
        agents = [a for a in (k.get("agents") or []) if isinstance(a, str) and a.strip()]
        _register_missing_agents(data, agents)
        p["agents"] = agents
        p["updatedDate"] = _now_iso()
        _save(data)
        return {"status": "ok", "action": "attach_agents", "id": p["id"],
                "summary": f"Attached {len(agents)} agents to {p.get('customerName')}.",
                "agents": agents}

    # ── add_agent ────────────────────────────────────────────────────────────
    def _add_agent(self, **k):
        name = (k.get("agent_name") or "").strip()
        if not name:
            return {"status": "error", "summary": "agent_name is required for add_agent"}
        data = _load()
        if name in _all_agent_names(data):
            return {"status": "error", "summary": f"an agent named '{name}' already exists"}
        agent = {
            "name": name,
            "description": k.get("agent_description") or "",
            "category": _coerce(k.get("agent_category"), VALID_AGENT_CATEGORY, "other"),
            "status": _coerce(k.get("agent_status"), VALID_AGENT_STATUS, "new"),
        }
        data["agents"]["custom"].append(agent)
        _timeline(data, f"Added custom agent: {name}", agent["description"])
        _save(data)
        return {"status": "ok", "action": "add_agent",
                "summary": f"Registered custom agent '{name}' ({agent['category']}/{agent['status']}).",
                "agent": agent}

    # ── list_projects ────────────────────────────────────────────────────────
    def _list_projects(self, **k):
        data = _load()
        projects = [_project_summary(p) for p in data["projects"]]
        return {"status": "ok", "action": "list_projects", "count": len(projects),
                "summary": f"{len(projects)} project(s) tracked.",
                "projects": projects, "db": _db_path()}

    # ── get_project ──────────────────────────────────────────────────────────
    def _get_project(self, **k):
        data = _load()
        p = _find_project(data, k.get("project_id"), k.get("customer_name"))
        if not p:
            return {"status": "error", "summary": "project not found"}
        return {"status": "ok", "action": "get_project", "project": p}

    # ── stats ────────────────────────────────────────────────────────────────
    def _stats(self, **k):
        data = _load()
        ps = data["projects"]
        active = [p for p in ps if p.get("status") in ("active", "poc")]
        success = [p for p in ps if p.get("status") in ("production", "completed")]
        total_agents = len(data["agents"]["builtin"]) + len(data["agents"]["custom"])
        return {"status": "ok", "action": "stats",
                "summary": (f"{len(ps)} projects · {len(active)} active/poc · "
                            f"{len(success)} in production/completed · {total_agents} agents."),
                "totalProjects": len(ps), "activeProjects": len(active),
                "successfulPocs": len(success), "totalAgents": total_agents}

    # ── export_tracker ───────────────────────────────────────────────────────
    def _export_tracker(self, **k):
        data = _load()
        path = k.get("path")
        if not path:
            exports = os.path.join(_data_dir(), "exports")
            os.makedirs(exports, exist_ok=True)
            day = time.strftime("%Y-%m-%d", time.gmtime())
            path = os.path.join(exports, f"project-tracker-export-{day}.json")
        path = os.path.expanduser(path)
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return {"status": "ok", "action": "export_tracker", "path": path,
                "projects": len(data["projects"]),
                "summary": (f"Exported {len(data['projects'])} project(s) to {path}. "
                            f"Open the web tool → Data Management → 'Merge Import Data (JSON)' → "
                            f"choose this file to load it in.")}

    # ── import_tracker ───────────────────────────────────────────────────────
    def _import_tracker(self, **k):
        path = k.get("path")
        if not path:
            return {"status": "error", "summary": "path to a web-tool export JSON is required"}
        path = os.path.expanduser(path)
        if not os.path.exists(path):
            return {"status": "error", "summary": f"file not found: {path}"}
        try:
            with open(path, "r", encoding="utf-8") as f:
                incoming = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            return {"status": "error", "summary": f"could not read JSON: {e}"}
        before = _load()
        merged = _merge(before, incoming if isinstance(incoming, dict) else {})
        _save(merged)
        return {"status": "ok", "action": "import_tracker",
                "summary": (f"Merged {len(incoming.get('projects', []) if isinstance(incoming, dict) else [])} "
                            f"incoming project(s); portfolio now holds {len(merged['projects'])}."),
                "totalProjects": len(merged["projects"])}
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
