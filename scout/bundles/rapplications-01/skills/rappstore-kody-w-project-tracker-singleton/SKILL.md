---
name: "rappstore-kody-w-project-tracker-singleton"
description: "Local-first tracker for a portfolio of AI-agent projects and their MVP statements. Speaks the aibast-agents-library project-tracker web tool's native JSON (projectTrackerData) so data round-trips via its JSON import/export. Add/update projects, set the MVP use case/description/timeline, register agents, and export a file ready to merge-import into the web tool. Data stays on this device \u2014 never in a repo or egg."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/project-tracker-singleton", "rar_sha256": "b6270faf10379411b7a0065a91b571299bbb3f9a8c6072d041f24580c70d7e7c", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "project_tracker_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/project-tracker-singleton:810a8573b9015c9e37359fafaac80e9c5776de64f2d06fb57d362fd35e043de3", "kind": "skill"}, "author": "kody-w", "tags": ["project", "tracker", "portfolio", "mvp", "local-first", "aibast", "rapplication"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/project-tracker-singleton`. The
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
