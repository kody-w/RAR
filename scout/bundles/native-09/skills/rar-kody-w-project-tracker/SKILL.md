---
name: "rar-kody-w-project-tracker"
description: "Local-first tracker for a portfolio of AI-agent projects and their MVP statements. Speaks the aibast-agents-library project-tracker web tool's native JSON (projectTrackerData) so data round-trips via its JSON import/export. Add/update projects, set the MVP use case/description/timeline, register agents, and export a file ready to merge-import into the web tool. Data stays on this device \u2014 never in a repo or egg."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/project_tracker_agent", "rar_sha256": "b6270faf10379411b7a0065a91b571299bbb3f9a8c6072d041f24580c70d7e7c", "source_kind": "rar-agent", "source_commit": "0553d9160832ffb46ee5f0bb2d03c596d9039fa1", "author": "kody-w", "tags": ["project", "tracker", "portfolio", "mvp", "local-first", "aibast", "rapplication"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `project_tracker_agent.py` and embedded as the fenced Python below (sha256 b6270faf10379411…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `project_tracker_agent.py` first:

```bash
python3 project_tracker_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 project_tracker_agent.py   # or on stdin
python3 project_tracker_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/6172bLjRpLlr3Cy2qakYmYCBIhNbW02WIiFWAmCBMHKMgn7vm8ENJpvnyDvTSlVknpehi8XCIR7eHi4+zluFvfnD+44JHX34YcPeR0sn+YPHz8EYe93aTOkdQWGldp3i09R2vXDZuhcPw+7TVR3G3fT1N0Q1UVab+poQ0uf3Dishk3T1VnoD/3GrYLNkIRpt1GvxqYf3CEswYT+8+bchG7ePz9u3NRz++FNtP9UpF7ndstXHZ++rjeH3mao6+Lv/aZyh3QKN8ezrm2+e59nvU3j3MH9ftPXmwA8bLp6rAKgIW36zZS6mxSY9JJKy6fhUPh4/vm8oYMAGhsgEv5q+sdNHw4v856Wj3248d0+hL7xCzSkZVikVfhx04Vx2g/AyLc9fHzt+0058FGUFiGY4gYL2MCmDLs4/PRmwCatwMhzka+7+7x57uDpqaXf1BX4lvabIJxSP9x8GRF4t99U4QRWSiuguQsb4PhuE8bxZ3Bo4cMtmyLsP/zwz399/ACWKD788PMHv3B7MPTB+J2j6KelQKZwqxh8bBYQARV4b8IOnGwJhoIw2ry/fdeHRfRx849/5LPbxf33P3ypNu8/13/6YvNfm+/evn2Ow+G7Lx/ehr98+P5p3pcP4OFz/zyH777/TXTolm8UPX8J8FsBNvdfm59//+H5A0qD4Mf38/ny4YfN06jPP34z+PHPhN7O9Y9yvx//U1EQAT+WU/ObzPvAn052h8H1kx/fIuAb874d/vhXu3p9/v2eXkN/KlCAWPtq9zcr/W74TwXB0fzRD98M/rkTQNJ+s8rr9U8nvsX7j+/5+pvE78f/VPQtG/4o+vvxfxP95RVqb4H2/e8/pdGvoQTSR6ur8Ic/LtuFw9hVm6yvq8/BWDb9dz+/7XZ8bRdsqOtqYMyfWPwnPyA6liUoXE/ZCIRdlVf1XH3Nj5/f/v6P7hdQ+sLwlfPPfN98U1BeJXVyizR4l+o/f/nwy79t7Y9Wv+/0u1+z8xuJ8OGHzbA5vP48l3D7TfjDZvO39yrid26fvIwBRTetQA0rN0VdN/+vNf/CU3/wws/D0oTfhd9//vHHyi3DH3/85YfNz+Evz219+AWUKLBiN77tFVScv/1to6Z+V/d1NGzOfj0Om26snmX2S/Wlsp6lMH2DjO5pfZ96oLC+zXuP4OcWARD99L/egAx6H/4aQW9J9dPnjQV01F0ap5VbbEzaML5Ub8gF9Ddd2IfdFAYbbxnCT+BQPj0fnhX3pz/V97lZfnpV/LR6GWeyEgCLph+L8PPTcDsJq3czfbcCZxL6I9BXPEH1BQ79E0H6upjCt3rf52kBIiPtwFI1gMKnbuCIH57KfvrpJ4CWyZfqrWKjm7fw6SEw4VdzNp8+gV1ERRonw5cq9JN68/eff/n75n9v/jupl/LnGgYAjHc3AwtfgAkCa3wh9+YVJW7wcvPPv7z7EqipQDiBQ0mjNHwTBtCYh8FXx55F+hOC4RsvBA4N3wE4rWKAyZ83UrT51d4XqHVP7rBJasA3grAJqyCsfICeiQu286snq3rY9IAK9NHy8YXQz1V/+jWQf/TB9J82Kmu8ZRpAWmDmaxIQrqsUuP/XY38bB0o6wC+Yryo+b7RXmjRu5zYJyJW3NSL37Vzqd8B/g3EX5NT8pXrC7ovkuM9ofHMPmAQ8478f6acXIfBrkChV0H9d+zUHIFKwsWr3SSa+VP17RLvd8yj8GpiybOIxDdzKD//zPaT6pB6L4OU/YOlT0/spBO+n8orBvwrcr6TiW4b3PnfzP9939xvHe5d+aaQ3CQgDELwgeoOubj6BfTwz6V3oeVYbsEHw1v8VT/xS1c3zw1ilwzNq3j1xuNGs9Ubg+sRtwqfIX/JEYMqH4k+M/xVLfqVWr/R5lrPya435HKdDMnqf0xr6U93QU6yHXupf2n/8dze+KFsylMVbnoPjm16HAJL4zQ1zlw5gZ28Y+MaH30IfZDlQ8gr4dxII/PXGb59bUp8scSO9scQXJfzumYffg/1891TyJISfnjUQsF0v9N1n+KcgGH5j1b/jyiC1/8iTfwJVIAlL91fHuE3zWuob+vXlw7dE45+bnzdp8HHjj/1QAyKrgZr+cfOGBB83z1r/8VtAe33Kw6QuAmDpX+IoyIQmfNaCc12Mb3J+XT1dPHDh4KbFk1C/DuaHfz5RpP/Xxw3I/fCvNQKOdulDFuTrx+cz961J4N36Stz/0iJQ+EAmAmcABW9E8fWy+WXzr4+/ueY3rrcBjvnywRvTAuzj3VPVyzm/c4cPdMSgcnz12bfq/p1OvPn4pfyfm8+fP2/+tfnlm7W/Nh9fjyV42TqkQ/H7RZ8mv0n98jzmb/L8h1eY/JaYBYiTV89hidL5a8/xLLhP4f8wTP14YK0fLZNm5YP5IyeZm2cB3PzHM+l/FHX1AP17y/b6/n+gz6B4Nv/+EVTefvPHmPz8Ihkb6YXEAdih9yqKxbLJn0RGv1hniTuAPAJoMIN6Mddd3jeu/zxL0PWBp/wJKq8MfE14K83V5jPokYD/u+4rPP0jrAD8h//4+E6FXmO/euMfX6rv5iT1E1DDls0zgn8N+ldl+h5AQw1WAWslISjP73n+uzlfYeEJaK+SyYEy+dWg5TfG9ff3YtFDT4D4z5clVfgYNtATwYB4O4agsj1rSP8spiCZf9/L/fTeOp6HADhss90wbp/6rw4PnGfxa5GvaqB3eLrsmUBAITiLJ772z+axAMcNEOfDD9VYFB8/PKP3D03jsz8EUFiGAJ76Z28JDhC0iM/iDd4AoXvaCjAueOtAnwUB6Ki9p4on32sKd3jrLn/+AJS4Ty+9q3lnb2A6qLyf+ie0QbvPMFgRvL/BFfj23/K697kAMwDRAJM9HCHgyI12MEpQ+93OI1wYxjGX2nkYsUMoyvM8NKJc0sdhAgng/S5C9hgJ+wQcECHhA319PXZ++OMTq9Pn+jCGoQG1w2ESRaLI2+NhiEWw5wFp1McoPKBglIrc3W+iIByD9029GfnL0w9fKeZz8+97+xnYuwczxX0v0W8/FtrCFHFTMrNSoK15snSmZ91949+WuinWu1zZOMCnYJyQjh9CtVaYmk2So3pQaaZWzmpaRNviFEioaeTHSIKyrVSdb5GhrZjkTn4beK3stoPKCXc8rDochFi2QrqsTtujCdmk0mv14g9YqCJrWDx6hCUhaF9SS6vOxrXO79fLitxFSnTVsVMzJWwEQM+IHDb42FebMWTSapIbQWGJdZ9mR8SYrGAL5blRl52Wt6vONk574KXrdoaxQNwJ5Ymn0u3aSHh83dO1QiSE8YisglJtc7UlUDTnWslYYTZyfJzb/ibhaaJ1fTuj9EIOtDal7k0kpvjaQippmHtVMJYhbzO1RR9mhm+tbXmntAuxnM+Rw57w9hifvZO69QZV1ffYgBenvYCS2nl7hifaH/O8HyEZU92iP0H7WE5UZ7j3iQzJM2veNOjSa3ucR03WUbV2r6AlZl0rBc8zHVblrbIlQqMvyWNqHATcShmIMfmL07N9mISj3ONmefVF7n65wIeacfjBOyomRMpHIWSb2dxL2z4tib3cnA6sM7JNViQUZKmlIJ+XDNCO7RIeI0Eyw7Fdi5CMGH3c0tnMbfudJ7aUHNINVlwvx9wOMKak7En2DAlmHtjhgBiLQhY3Bl/OxNRn1mDGNmaW58EisuCe5jTf9I+JL5hEs/uHqPgpU4okd/UiIdmnEMt2LIMiPnKaaNK6OqRlKWEKQ0cnGlKJ1tXbAzQ6JeNphZYZ0uGUSyfm7C1dcFdYNj7zairLp70jJQVUYRfPXGolh6qS7eMMzWtUdNZ7Zq+7SjGFm/A4WHF1PTdbDE5ZX0PAGRXxHB1W0ukvIyOdawF1o2jqFpr0E0WRHw2mbbchBCHB1p+ayWi2lHqbVgoyVorY3vHHJJ1QWRNXj9pujYaSpiw90ykXQuhhUWpBLFNSdPybO3HRtvXbVb31x4onGSZl2kky+cYcEexw09AKd27dTOpzcEc8Ducai7ld92O7yKqjj20FIvB4Y7UDd8QtSLLu5ap2+JbBSvt4js0bdDerHczuG5LeX1I8se5GivssNMJlKlCMLuw9tZ1Krzjs5ztIvZI+l+N4KK6Y0lNH3uox6aa7GavuGIhteo2e7fOdv2lXWG84uT6mmLHormCSDrkr4VNNsTdoxloOzqXg4gpn0Vj3ayves8XSHfRuPmC6o9IbYV3jAj5XoM48lCTodL9m7hLIDoumHY8+nAY8E2gSWplYTwIzPd8mVJchu8P0+qYOQ9yz2Vr4JhZJtsWaanK9+zsIoedSpZhx8RVb5clussUjcVJ6eREjVoDx8dyRlmb0ii3C9XGKCFTdk6iJupZ1lCu91Vt6Jg5QzDH0vj21cEWvV5LOERCv5RYrE9rEt9eaNYLpIt/uIc1NaMlW/JLL2rzsy+NtolBrKgUnrjH0wQeCejOTHYoknl2wZtFITKQcGTZZjQtEPiZ2Z9An1pV4ciAr/0IrbN72DEeXoDRlnkynJ8RnRRW+t8HDYITWakktYOyJtQtfKFqb5az2ISvJQ5KrQFMlW49x2namYzCq6eGeii1XSXmOBXSRHfTS7wKWFC9FKVXl4+QrlzQ5Zk600G0yne2ztV5K34QxzYnn+iTVacuKFm0faAUzXBGH6lLBDhAjk83QZpy7HsdlOGISklgVbSAWcaCNmqNmg3KM2NmmJcrfyCx3TwouVoUqV4XR3ra+MLrS7iH2d/448fQRsiW/MVSCwc8iPLPyCNPRWbzS65G1JyxbCPPyqMr2oFT9hUxhzoRPzdbyu1tenDUaIp2ubi/rLE680oUhwh/bvRPl5klSYES97TTMJmjSOUjCjWAiaDqtkKBODX8tDX6c5NGdTrTOru2D8amGYK4rYa35Y+G2K7IyQU753EwdNYkVdtAMCyiGbMMqRyYsDa2M8mPDmw2TqxVaL2TCiaVMylAr3p3ZmkVTPeWXWVuV041W3GlLCW0oNa3kFIbB7ta9YoIiwy/aFaJiWbrQaXZnnXuqIezAMfCdT3FpAqFDXcR7WJUMH6+ntlsrQr9ciHt72/H7uRhHD5q4seLdGzn2sxk8plQNz3ZLZqynS7s2Vlde5M+ICXs0cDI7n89CWqHYApU+FlUHwpjQioDikG3XuZIK326avm0jGkVqjS8HyLwz5VzD7Mrh7o6D5syXbn6yny1aLfWzsI/h4ZSqY6yKDUgeFH1od22be1JMiNdzkZV39GGbOq/LJ69jaXYnh05arnwUtjiz7ByO7zJHHaxdUxA9KVBOf4un4x7mAFs1oqrC9todhbDeUK6UfvPIc+tzyO0IFkLGh49KpyLCfA5wgsWVYHkL7DtYbBXdDoA7R1F+28pBzan1LDJOXHJnAVMix8jneDrwWIvDPbyWx92w5/3z9QZBGQTN+wkR+xnr+2N+z0oNPajSrDkrM3Ikx4/Qou+I8z6rT1vpXmEK/YDn4cB0zrbFLyeNoU+d6MU7kCPXatWua7o3vGIvnQ2ZD2GhZ7yeU69ctW4puLpbXC4dT6I73OAiOFppWuSay2rZ2b0xdBu2ATSczvvegym9i9ZwcZXroVxaE7AUF9V8mSEJyNjBHS5QRiYgUYNz9LXmjlNig+wkvOu6P1gTSTD0eC8oal2aa4GzNVYNtFiQZ/YMghyg4MjUYqE48hCG0OVG2eScGiW7BiK8IhDtTBmjBgKMGTa+qiwhgh3lx9PJLdAVmQKY0X0eZyOA83LvkQ4URxmOx+JFzWhTF5GCgAB52TMIr7nJnIRW7apYsjDlupsD37bEjvNaaevsUIHv4LbHuLIzXOewpEwhrXfOOqnrMqLFGTshEq4ueks0/p6GohBSOPhuXOG7tt+OlrdfwinDKD87klQIuROaZ/C4w8yO5GiMBnU8ZaFeWkLCGWKzPKgwNDGjup/c0VwNhN7qMumk7L1JmzyzjuaVorG+rC/xYJSxJ+7Y02E1qk6eaBbhmDGOfbZk+kNqPmJlyu7BcEfDvpHMo6+tHuLA+9Suo1MMm6J02BGZC/eYcF281Pcu0XBSBdfDh5M1aSd4RlBeX3bITWst03W2pSBYF54ApWhb9HpvWk5z0qHOL1U87w8HGqtNRjR7hzeYksSy2kiPA76/mTuSG0kJUSQ8CA5wfynPlyllc36WcOiRJPtervhHslS3A/3otyZ98XridKN0hrMUKvUm/sE4NO3e2hMVXxyyJWnOyoKsfDTHJMz5gBkokaPS8dCLay1BjwdX0+Fjrhzl4FZ7Z45wyRgPu065XS+WIi2CfcL6vWg4qbBbYNgFIDbTDgKdySuTqQ5fYIrFwBf+nBDyZS+ywUJ6+O7c41NDzhdixZvdcinT4uq3zJ6ji2LFTgydXKLGHts6U/mj0nX6cmmP06nOGidAkssxyZkzirEtOVHWsTwfQi9p5EOcYoSpKScBbJC007QMUjtTmNkOFgDiD5UmBEMhL1AvAiqbz0efvsYpHRVD7+Tztc4ugM0RaeP7ZVpDTHbgLtd9lVJGM9ru+VEEvEPk/QIx0IHNUt3V4INkmZkjLux6dIhHyF+PNJ9qjqZaGuWXk8ZLBYORWntoTmtogm690XOWc8NruLuPR221QjeY/LApQjp3UHO2Zi6ueYF1iQTbJQZCcsjV23OTyVo52QO6YD3UXo4yUjOk2xmzHiLKgl7F4IUTmWpNKI3mEb3SN1Lgtkw5OLSAqP1VmlHfIRkH2yYuVgr0oyru/nzVPR53m0UKTmnHLuH95DocfgrjAmiWu3v5YCBF2Vltey7PWiX6R3nt8oyQCf9gdZkqYZTiWro7gn6g8eTB393Op6t1c/rdtTny3emmnK3ZiGM38LBTdXmYQv3YSxdMcOxZ5kAG4hedwRR+NvsLKIf8CYtl4XAZbT3BtfV4KYds4g/V1F4XsdRVM9Ri1cyP685rjJDLecuctlly4buKnsy25gzGK6axK1HrMtR4UQgM61YzNQzlhT4hQuOEtF/QhOMv5WNeq2vTn7apdNHGwNLTNF+oUUGKZmeSQxXEEhncZY/mWwu57Y/HsE7E/lwR61F1hI7MscPdbi2U1nKtgTX7xhMsQEekFpzxbomwowz5I75QanE8Eqyw7uQ6NZHcMnzJ9gNsh+eNWLulAgmwtRb8TpOT9AZi3rtXdCQxrlsgpxTZ2i1lSzS1hcMxoYlS94Ljfe3OXB0S+T6D3eFYSEFjGUESyMm21inhDGl52DWNceWrE39QZI9KIgYcGm6fQN1qoUA4xvHp3kP+eR27JV3apk34WxHs8yyHqPMMe8t2SdMkfYiFvF+DxkglQxQu/GMwwz0XwBeDLSpRDZ0DRIkZM15970BDMLfAgi44R/+mLod40fBbJp/mAlIJ946gkq5uu17G54OhIdaWGZHHYLfdoIeAtFQ3c43ve24ux0mIC05XjuZQG7F9kIXr6HAuzlPnDu4dNVdRCCIamNpR5rg2F5JdMOQMETjEJOqdUR8HUU9uRK5dQE912J+NXKh7WsB1i9n7+uDHNnzJa9GWESaWF2rt+Son7Z3mKFuq8rKEgb0gOl1t/rG30PEex1E0u1CfinDxYG+ctKw1zsn9lVXhR7Szkx2z8k62S3bHto8xqEt4ZmsfR/py3+HJ+RQ/QD9HJudQ9NZLHLRpW7DF1kEU/TAgmS5PvaTPGkZ6gLtdUj4Z5qYZ4YxR0u5o1UGdR/R8dI5JmwOOpsl9KwgwOAWaWPAdtq7eCbF3gzrm9RW0PIBnsSfKZCNguK3evPs6DJZX1Ii6Dsc1jibO4wZ7PFEMp9W3SOycjjSbjFxpTl+uZerYAn3eSuhaD4G+TKp6iHfbPC+Bmw8uKhaFb53jSGNONAJ6nxPXQVhnakLq4Ii1F8WS55248m8G5h0AV6sO7TW5WgLq1XGqUOQFxxOVseqBXEwFnyq/Q1O855xIJP3LGUNrP2muVqgh9nTAMw05n6xghlvGnynNy1yVSGmNvnB33QzDig9NmNdd9SrQbZsFyDUUncYKrmhsIwPElhc7W5W6tEN9P6QprkML2sXqdbuNSkjQE5g/ayd552KsrOvXS7Uk4fZg5Auf5AfIFsQzZ58O9o4dHqySuJeV10yPbPfwtXEPrn/2fPUC8fiaAz5YXzGSx6Uy9bql7094vi8pNrt5dW03Fky0jH5zIhMAC2oDAG4Rk5vaM27Ij/7kOA/BoVptW/DmXidauz0fj2wsK+sW7vcs1Wu7pewvcGJtnTucOk1Ylo1BzA639URRcJpduqQ3eXnEzOm+NLSOOlLDHpayLq4Dd2bsY3AcDrpGm+KK3nbHGa/gPI4Pp0qeCmnSka6rYFf1Zd90o8vJfFBmnxd27mdnnZu1Q6Gf9i1LT6jKtmllBR6DWGZhX1ZCRI+XWpH0oOnaKBulhQqCuSXgVJEOq8+kYe3dqqIWkGIH7TDnGtPzEO5aGcYJnLjxwD0DiurTFT9Wwgk3bAJ6YHh8NQXQfkcGF6DFyQ0aeno0aZ3ZjzNF7yXFIvvbNZAwzY5OjiKgeqdCnLwqAAdqzGB1jRof1MFxCXQwExVKI21eKcKtYm2sz2tNeKYMaYEKM/weEZeWLqYLP56jk3Hk4SpLDlzvhUEZYSNvGckizqfh8rhArjrdfcQ0MiyJt2GPXq63mj9cFme/RmoRSkdlSg/olt4rNTQ+4KqslOqUw8sh2oqO6WiMcL3fdmyVZEHqniFhqd3YFiErk9ITxNHqBAf9YkjyepftknCQ+rbEvFeP7qOsQK+CUqlvZnuU1EfE1Z1pibH7eoNsnUqVyL4/uuWMIrm/8FQr8qA3UB3dge5aVWyrSFRwyL/p9uWGcVV8pNhKqm+6fDH1vlFvnOqdWDrnoKthaostztE8wXosMbaTG4B7JchI6I7LRfdpliJzW+FVhzI0VHaAneKDu1WZTlO7eZy3x7JA3UfkGdy9P953dJL2IhFfe+FIJ6N992IT83hy5+U7ZI+3um6keUiJZaMdI1glhnbP6d5hd/No8TFH3XUa/TWIBG9LwhyF2ffV81qUoBvtnuwEoYXbHcNN97jxaUJmkPF8snVuPVVBfluNaT7gDNGrFY7SawDrM3QRx9i5oLCFWY1vUJ2xQ+1HFxvx4ngdvvj3acwOtWwcReZ8Nh/R/baYMMdpWGc3wV4VbVv2BZxZT6bBq2Y0V9Y0R5xonmnfzfz27NOppxVVtAdEPcBzw9mzAhSyV2ucFRHLS08cbxevznOXcavTsbSUOPKoki8O5XEcbpdTp4tlm/OjT0X3TjwLuxOHoZpoUffL7lp5natw3I3wbqczHExXRLTr3Wxng4BccVQo9R11f0gClME7Tej293NHlNj6IFIBxwlh9GHtnjrjIZ8vmkrBvDvQqRRWvYJWg9ecW0OZCOv4MIQM5rIaI8PzUYkfXqgP6o4LpKQjQbeMeH42lDwFICyrXKGx2VY4mVMgUL4WWY/iMq5UuNxjTyp7c93GEMvMYSgi6r3cJ0O9yv3j6C/bbOADfavMjt7sF4ISJzted4JRa62zEmEsGrm9WxQFF6x052Ow4R37lsRTu+xnu6fOodFkl6uJEWlFGXrfKkhSjsVt2uPYgHjqjSjOaS/7xGIY/iHv++Vx2I2Wg98ul9zrESmMa/1xc+crxqhWcjTFAe9k787dPCdPayHKKcM/i5oecPhZ4Ba1c64yD7GHm+PZSOAuUdDs9dPkmig+38LuYG1xX7+peMMtndqeeNM5HHZ42GNZEnStfHVk3z+RW9P3VFD1YSQcy+EiXLEFvjesomV+Ctp0DCq0MLS8nOSydo6dsztqxdYnAG/OdWMwU8C3zZtDuhCDEibCIWugI4wQkGc8slg/nZuelZD9cBtJKj7jmbLVz+xVJYNYW9hKtcOOFRkNfNsT+HIkVHztRQve7V16t+N2uMcbmnKtJOLRTQCoQeAhK9M9gsgVUp3VhczvgiQK2JUmBVLFTBl2u0Cu814oF2p7OW1v9R7BZaMqJElxmkdrZZhYU2NzM6fyKiVMArozC3Vqs1ubqMuvl5OW3Ze+ZVoT5xnTvIfGvaxO8BojgZOOzGRbW/XUK06ROGFbsu0QaBpLdMlF2GP7fJhODfK4Tn6rzielY7muK8MBJD3TudBRxJiUQKoQA3xXKNQp1l1iABZH5ZWxpHFA5CLVzOgoifUlNQ7Mfb/0FemusxmcSBG/DeHFAzDNpjDBIoFKYjcnEJD7oxa9GyUo9O52RUXJq3fFaKPuUQld2OPNk7O95vW9OaJJ0ukP+SzoeDygwkJcPSpd0NkmQMfC+Po+QO6lRXHdiDBw3c1bUNW0RmfVRpVP465H1UzatpdsCybK5jKj6yDaZKGgqBhOtqYJs3dy4mLJLtMdxjTVMT1p61jXvTYsbqKfI2NfcvItGthWNb0zW6ocpQZmp3QcPMpnR+AZmFXW1U0QzHkcLseCEca7FFF6QQCGDi9aaA+UZ/ixAsWmYbOrD3l7JZoxpNOCDrmWtMP15x4hqnGEg4hhuataDbDo5gnCjdt8wuCLvZfYHdwdAqV9lPTuvrBcdpgWSZWGBpoExTTu+ysAmv56VpvkwjJbIjr4VCIepsdWR3iGjJY+yQcSXcXj/WopvjHMhCvmjFybRCNf71lOxjtIgdaaOdfqqeLFHN03jolDFV3r+iR6oWqnoi6ZbJ+t+0B+iKQdWXsykfF1xTzris5lTDxkkWuK/qHz4RWNFCfJ4e3tsYMofKj6/mGfr+aymA/jbteOfhRLyl2R2GBvyGlvUBc9dSWbg4C37gBSrpnYL1s6sXLL20bLRcZS8nHzIutkFaeWIx+HLWPfuJ205FijMN2aJXRokQUBKIkVceFypUb9oez31wr1H0U71TvdvR8FeN7LIhZZgfXIQVdIlVmP5VMWdwZ7vnYE3qLRlaJUbbZB7N2HC/EQHhKFCwg8mVoa4oMIzlPXiVN0g3Q4bWZXPrfCfDnpZTVcswwG/SChjoW+XiSuVfF2j+4Op9vW9klfPF7Pea9q2kHIoRHxMNATmSx2Pxs8iTNHlLJN+Uq1SDB5XT1FJYnKJWCka4bO/SFBGivpQP1Sbk0gWKcOGy9u2bTHzj9vIb450hHEUMV+sN25eiDbi0GJMABC/8B2Teaz0h73YusuDqeAGHUjxN2V8zpS3h2i3Qgr8lJaYgvBx3s35lDHu7LdaxG6C9GZV3d47GkrBsGXOocl38jWUIMPdbkX6xC0m9dJ445FxVa6NI1Hpe4zDqel0GEZBDSuho14yE2TSGpp5WHHG0KrJ48zgSMjU7rBDjngO/hA43UW2rtuBvx45KbaW2KfHyw0kq6xT7BjcXfLLp1QI4IH4Jn0MGUA8mn2QR4RtMfv0qk5XxKVl04HpEjPjrnaimUCNr7H8UMC+xT6KDTZE+3rdkZueXXRH4GRsqiNez15GeDrkKoY7Oby4TEfBFi5y5JG3lmldiYytk0LRdlil8J27t1guXMx+RqRXnrXguEByVaNTJ6OEgNyNtZi3HPa3itlrzr3FnJ0Eh3Ox3698KZFFDU6afsjvw9QX1dt9Go4M1njKCZvh0cHKxd8Z+YhzHMNBrGtlIW0GbtUikABVyXoXkfoECE9fccVA0fVeXYTEpXSd2RYG+HQJjdUxrG1vBA5I2TYZd6HaxKPQnk60s46hS0phnRcBSPOb7cOBPFGiE2re6MQxet1CgpWOd9BfZmWxDLpSqqvBL49sluafmT+yb+6qlyuZX6xOXKpQi1F8WI1cgQT9XaSbhw+dt6qw3OnIgfMryOZvBxuoEzkyuWg1ldUcciS4kt3wKejMSW7C1pg7HXlYdQ84tsDktSFh+aUo0hX34X30oO4HD0AMpPmxR2X7+8EwRy3pZOGrm3iQjwCepZfr/Y6xiyvjCyBro7FnpQ2Xs24nhuymo+EEtElFd78xBYviBxnCrUcoeXSTiLsglp0cFWv2mXRxdaEY2Eu19OhCK1RrHeqQfUkTgAaenPPChf1ZkfT9H99+PjheUf0/Q7OX93dfF4y+f921+XtWko9gUUrH6z6zw/P/1j54bXWD39pwb8+fuj8FKz/dlWnL8b4/bLL20WdT/926+s5Z3m7nFtXQ/gYvl43Gtz4+W8rX/cK5v0m8eulLPBcTs3zrtJvt9jA29vdzdftn6YpUv918fZp2uuO+OtOETAPGPjL/wUMzxjl6jQAAA== -->
