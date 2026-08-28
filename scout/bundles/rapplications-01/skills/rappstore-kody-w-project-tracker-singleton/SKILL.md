---
name: "rappstore-kody-w-project-tracker-singleton"
description: "Local-first tracker for a portfolio of AI-agent projects and their MVP statements. Speaks the aibast-agents-library project-tracker web tool's native JSON (projectTrackerData) so data round-trips via its JSON import/export. Add/update projects, set the MVP use case/description/timeline, register agents, and export a file ready to merge-import into the web tool. Data stays on this device \u2014 never in a repo or egg."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/project-tracker-singleton", "rar_sha256": "b6270faf10379411b7a0065a91b571299bbb3f9a8c6072d041f24580c70d7e7c", "source_kind": "federated-rapplication", "source_commit": null, "author": "kody-w", "tags": ["project", "tracker", "portfolio", "mvp", "local-first", "aibast", "rapplication"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/project-tracker-singleton`. The original RAPP
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

<!-- rci-capsule:v1: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 -->
