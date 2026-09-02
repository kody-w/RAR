---
name: "rar-kody-w-project-tracker"
description: "Local-first tracker for a portfolio of AI-agent projects and their MVP statements. Speaks the aibast-agents-library project-tracker web tool's native JSON (projectTrackerData) so data round-trips via its JSON import/export. Add/update projects, set the MVP use case/description/timeline, register agents, and export a file ready to merge-import into the web tool. Data stays on this device \u2014 never in a repo or egg."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/project_tracker_agent", "rar_sha256": "b6270faf10379411b7a0065a91b571299bbb3f9a8c6072d041f24580c70d7e7c", "source_kind": "rar-agent", "source_commit": "0553d9160832ffb46ee5f0bb2d03c596d9039fa1", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "project_tracker_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/project-tracker:30f317cb9abab0c44c3b9d1adb9cabe1ee6e05f786b17af5e5644796a6705c67", "kind": "skill"}, "author": "kody-w", "tags": ["project", "tracker", "portfolio", "mvp", "local-first", "aibast", "rapplication"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/project_tracker_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `project_tracker_agent.py` is
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
