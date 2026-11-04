---
name: "rar-kody-w-project-tracker"
description: "Local-first tracker for a portfolio of AI-agent projects and their MVP statements. Speaks the aibast-agents-library project-tracker web tool's native JSON (projectTrackerData) so data round-trips via its JSON import/export. Add/update projects, set the MVP use case/description/timeline, register agents, and export a file ready to merge-import into the web tool. Data stays on this device \u2014 never in a repo or egg."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/project_tracker_agent", "rar_sha256": "0a9452444854c420edbf73b617d392c1a63510890a663455f69d56a4e4ea0fc6", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "kody-w", "tags": ["project", "tracker", "portfolio", "mvp", "local-first", "aibast", "rapplication"]}
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
