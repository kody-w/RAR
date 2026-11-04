---
name: "rar-discreetrappers-project-tracker"
description: "Manages RAPP Pipeline and AIdeate project tracking data. Use this agent to create, update, import, list, retrieve, or delete project tracking information including full project details, agent assignments, competitive intelligence, contract details, MVP definitions, and timeline events."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/project_tracker_agent", "rar_sha256": "6ce05fe89b9c16b52949a4e36991f5d9536cb7981aa891d93b4fc53419bd4849", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Bill Whalen", "tags": ["pipeline", "project-management", "tracking"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/project_tracker_agent`. The original RAPP
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

Project Tracker Agent
Purpose: Manage RAPP Pipeline and AIdeate project data - create, update, list, retrieve, import, and export project tracking information

This agent provides CRUD operations for project tracking data stored in Azure File Storage.
It supports both the 14-step RAPP Pipeline workflow and comprehensive AIdeate project data including:
- Project metadata (status, type, description, stakeholders)
- Competitive intelligence and contract details
- Agent assignments and MVP information
- Timeline events and progress tracking

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "The action to perform on project data",
      "enum": [
        "create",
        "update",
        "list",
        "get",
        "delete",
        "export",
        "import",
        "add_timeline_event",
        "list_agents_catalog",
        "update_agents_catalog"
      ],
      "type": "string"
    },
    "agents": {
      "description": "Array of agent names assigned to this project",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "agents_catalog": {
      "description": "Agents catalog with builtin and custom arrays for update_agents_catalog action",
      "type": "object"
    },
    "competing_solution": {
      "description": "Competing solutions or vendors",
      "type": "string"
    },
    "completed_steps": {
      "description": "Array of completed RAPP step numbers for update action",
      "items": {
        "type": "integer"
      },
      "type": "array"
    },
    "contract_details": {
      "description": "Contract and licensing details",
      "type": "string"
    },
    "current_step": {
      "description": "Current RAPP step number (1-14) for update action",
      "type": "integer"
    },
    "customer_name": {
      "description": "Customer name (required for create, optional for update)",
      "type": "string"
    },
    "description": {
      "description": "Full project description with business context",
      "type": "string"
    },
    "discovery_data": {
      "description": "Full discovery data including problemStatements, dataSources, stakeholders, successCriteria, timeline, suggestedAgents, riskFactors",
      "type": "object"
    },
    "generated_code": {
      "description": "Generated agent code including agent_name, class_name, file_name, code content, and features",
      "type": "object"
    },
    "import_data": {
      "description": "Full AIdeate JSON data structure with projects, agents, and timeline arrays for bulk import",
      "type": "object"
    },
    "mvp_description": {
      "description": "Detailed MVP description",
      "type": "string"
    },
    "mvp_document": {
      "description": "MVP Poke document including full document text, features (p0/p1/p2), outOfScope, successMetrics, estimatedDays",
      "type": "object"
    },
    "mvp_timeline": {
      "description": "MVP timeline or deadline",
      "type": "string"
    },
    "mvp_use_case": {
      "description": "MVP use case name/title",
      "type": "string"
    },
    "notes": {
      "description": "General project notes and context",
      "type": "string"
    },
    "project_date": {
      "description": "Project start date in YYYY-MM-DD format (optional)",
      "type": "string"
    },
    "project_id": {
      "description": "The unique project ID (required for update, get, delete, export)",
      "type": "string"
    },
    "project_name": {
      "description": "Project name (required for create, optional for update)",
      "type": "string"
    },
    "qg_results": {
      "description": "Quality gate results keyed by gate (QG1-QG6). Each contains decision, score, concerns, recommendations",
      "type": "object"
    },
    "stakeholders": {
      "description": "Key stakeholders and their roles",
      "type": "string"
    },
    "status": {
      "description": "Project status: planning, poc, active, production, on-hold, completed",
      "enum": [
        "planning",
        "poc",
        "active",
        "production",
        "on-hold",
        "completed"
      ],
      "type": "string"
    },
    "step_artifacts": {
      "description": "Additional artifacts from each step keyed by step number",
      "type": "object"
    },
    "step_checklists": {
      "description": "Object mapping step number strings to checklist completion objects. Example: {\"1\": {\"item1\": true}}",
      "type": "object"
    },
    "step_decisions": {
      "description": "Object mapping step number strings to quality gate decisions. Valid: PASS, FAIL, CLARIFY, COMPLETE, HOLD",
      "type": "object"
    },
    "step_notes": {
      "description": "Object mapping step number strings to note text. Example: {\"1\": \"Discovery completed\"}",
      "type": "object"
    },
    "timeline_event": {
      "description": "Timeline event with date, title, and description fields",
      "type": "object"
    },
    "type": {
      "description": "Project type/industry (e.g., legal, customer-service, banking, pharma)",
      "type": "string"
    },
    "user_guid": {
      "description": "User GUID to scope projects to a specific user",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `project_tracker_agent.py` and embedded as the fenced Python below (sha256 6ce05fe89b9c16b5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `project_tracker_agent.py` first:

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
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/project_tracker_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/project_tracker_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/project_tracker_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Project Tracker Agent
Purpose: Manage RAPP Pipeline and AIdeate project data - create, update, list, retrieve, import, and export project tracking information

This agent provides CRUD operations for project tracking data stored in Azure File Storage.
It supports both the 14-step RAPP Pipeline workflow and comprehensive AIdeate project data including:
- Project metadata (status, type, description, stakeholders)
- Competitive intelligence and contract details
- Agent assignments and MVP information
- Timeline events and progress tracking
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/project_tracker_agent",
    "version": "1.0.1",
    "display_name": "ProjectTracker",
    "description": "Creates, updates, lists, imports, and exports RAPP project tracking records stored as JSON in Azure File Storage.",
    "author": "Bill Whalen",
    "tags": ["pipeline", "project-management", "tracking"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import logging
import uuid
from datetime import datetime
from typing import Optional, Dict, Any, List
from agents.basic_agent import BasicAgent
from utils.storage_factory import get_storage_manager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ProjectTrackerAgent(BasicAgent):
    """
    Project Tracker Agent for managing RAPP Pipeline and AIdeate project data.

    Capabilities:
    - Create new projects with full AIdeate schema support
    - Update project progress (steps, checklists, notes, decisions)
    - Import bulk data from AIdeate JSON format
    - List all projects for a user
    - Get project details by ID
    - Delete projects
    - Export project data
    - Manage agents catalog and timeline
    """

    STORAGE_DIRECTORY = "project_tracker"

    # Valid project statuses
    VALID_STATUSES = ["planning", "poc", "active", "production", "on-hold", "completed"]

    # Valid project types
    VALID_TYPES = [
        "legal", "customer-service", "other", "insurance", "banking",
        "health-payor", "health-provider", "pharma", "healthcare",
        "telecommunications", "consumer-goods", "retail", "real-estate",
        "high-tech", "discrete-manufacturing", "manufacturing", "automotive",
        "transport-logistics", "power-utilities", "utilities", "mining",
        "engineering", "government", "it-services", "consulting", "energy"
    ]

    def __init__(self):
        self.name = 'ProjectTracker'
        self.metadata = {
            "name": self.name,
            "description": "Manages RAPP Pipeline and AIdeate project tracking data. Use this agent to create, update, import, list, retrieve, or delete project tracking information including full project details, agent assignments, competitive intelligence, contract details, MVP definitions, and timeline events.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "description": "The action to perform on project data",
                        "enum": ["create", "update", "list", "get", "delete", "export", "import", "add_timeline_event", "list_agents_catalog", "update_agents_catalog"]
                    },
                    "project_id": {
                        "type": "string",
                        "description": "The unique project ID (required for update, get, delete, export)"
                    },
                    # Basic project fields
                    "customer_name": {
                        "type": "string",
                        "description": "Customer name (required for create, optional for update)"
                    },
                    "project_name": {
                        "type": "string",
                        "description": "Project name (required for create, optional for update)"
                    },
                    "project_date": {
                        "type": "string",
                        "description": "Project start date in YYYY-MM-DD format (optional)"
                    },
                    # AIdeate extended fields
                    "status": {
                        "type": "string",
                        "description": "Project status: planning, poc, active, production, on-hold, completed",
                        "enum": ["planning", "poc", "active", "production", "on-hold", "completed"]
                    },
                    "type": {
                        "type": "string",
                        "description": "Project type/industry (e.g., legal, customer-service, banking, pharma)"
                    },
                    "description": {
                        "type": "string",
                        "description": "Full project description with business context"
                    },
                    "stakeholders": {
                        "type": "string",
                        "description": "Key stakeholders and their roles"
                    },
                    "competing_solution": {
                        "type": "string",
                        "description": "Competing solutions or vendors"
                    },
                    "contract_details": {
                        "type": "string",
                        "description": "Contract and licensing details"
                    },
                    "agents": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Array of agent names assigned to this project"
                    },
                    "notes": {
                        "type": "string",
                        "description": "General project notes and context"
                    },
                    "mvp_use_case": {
                        "type": "string",
                        "description": "MVP use case name/title"
                    },
                    "mvp_description": {
                        "type": "string",
                        "description": "Detailed MVP description"
                    },
                    "mvp_timeline": {
                        "type": "string",
                        "description": "MVP timeline or deadline"
                    },
                    # RAPP Pipeline fields
                    "current_step": {
                        "type": "integer",
                        "description": "Current RAPP step number (1-14) for update action"
                    },
                    "completed_steps": {
                        "type": "array",
                        "items": {"type": "integer"},
                        "description": "Array of completed RAPP step numbers for update action"
                    },
                    "step_notes": {
                        "type": "object",
                        "description": "Object mapping step number strings to note text. Example: {\"1\": \"Discovery completed\"}"
                    },
                    "step_checklists": {
                        "type": "object",
                        "description": "Object mapping step number strings to checklist completion objects. Example: {\"1\": {\"item1\": true}}"
                    },
                    "step_decisions": {
                        "type": "object",
                        "description": "Object mapping step number strings to quality gate decisions. Valid: PASS, FAIL, CLARIFY, COMPLETE, HOLD"
                    },
                    # Engagement data fields (RAPP Pipeline outputs)
                    "discovery_data": {
                        "type": "object",
                        "description": "Full discovery data including problemStatements, dataSources, stakeholders, successCriteria, timeline, suggestedAgents, riskFactors"
                    },
                    "qg_results": {
                        "type": "object",
                        "description": "Quality gate results keyed by gate (QG1-QG6). Each contains decision, score, concerns, recommendations"
                    },
                    "mvp_document": {
                        "type": "object",
                        "description": "MVP Poke document including full document text, features (p0/p1/p2), outOfScope, successMetrics, estimatedDays"
                    },
                    "generated_code": {
                        "type": "object",
                        "description": "Generated agent code including agent_name, class_name, file_name, code content, and features"
                    },
                    "step_artifacts": {
                        "type": "object",
                        "description": "Additional artifacts from each step keyed by step number"
                    },
                    # Import action
                    "import_data": {
                        "type": "object",
                        "description": "Full AIdeate JSON data structure with projects, agents, and timeline arrays for bulk import"
                    },
                    # Timeline event
                    "timeline_event": {
                        "type": "object",
                        "description": "Timeline event with date, title, and description fields"
                    },
                    # Agents catalog
                    "agents_catalog": {
                        "type": "object",
                        "description": "Agents catalog with builtin and custom arrays for update_agents_catalog action"
                    },
                    "user_guid": {
                        "type": "string",
                        "description": "User GUID to scope projects to a specific user"
                    }
                },
                "required": ["action"]
            }
        }
        self.storage_manager = get_storage_manager()
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        """
        Execute project tracking operations.

        Args:
            **kwargs: Parameters matching metadata schema

        Returns:
            str: JSON string with results or error information
        """
        action = kwargs.get('action')
        user_guid = kwargs.get('user_guid', 'default')

        if not action:
            return json.dumps({"status": "error", "error": "Action is required"})

        try:
            if action == 'create':
                return self._create_project(kwargs, user_guid)
            elif action == 'update':
                return self._update_project(kwargs, user_guid)
            elif action == 'list':
                return self._list_projects(user_guid)
            elif action == 'get':
                return self._get_project(kwargs, user_guid)
            elif action == 'delete':
                return self._delete_project(kwargs, user_guid)
            elif action == 'export':
                return self._export_project(kwargs, user_guid)
            elif action == 'import':
                return self._import_aideate_data(kwargs, user_guid)
            elif action == 'add_timeline_event':
                return self._add_timeline_event(kwargs, user_guid)
            elif action == 'list_agents_catalog':
                return self._list_agents_catalog(user_guid)
            elif action == 'update_agents_catalog':
                return self._update_agents_catalog(kwargs, user_guid)
            else:
                return json.dumps({"status": "error", "error": f"Unknown action: {action}"})

        except Exception as e:
            logger.error(f"Error in ProjectTracker: {str(e)}", exc_info=True)
            return json.dumps({
                "status": "error",
                "error": str(e),
                "agent": self.name
            })

    def _get_user_directory(self, user_guid):
        """Get the storage directory for a specific user."""
        return f"{self.STORAGE_DIRECTORY}/{user_guid}"

    def _get_projects_index(self, user_guid):
        """Get the projects index for a user."""
        directory = self._get_user_directory(user_guid)
        index_content = self.storage_manager.read_file(directory, 'projects_index.json')
        if index_content:
            try:
                return json.loads(index_content)
            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON in projects index for {user_guid}")
        return {"projects": []}

    def _save_projects_index(self, user_guid, index_data):
        """Save the projects index for a user."""
        directory = self._get_user_directory(user_guid)
        self.storage_manager.write_file(directory, 'projects_index.json', json.dumps(index_data, indent=2))

    def _normalize_aideate_to_internal(self, aideate_project: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert AIdeate format (camelCase) to internal format (snake_case).
        Preserves all data without loss.
        """
        return {
            "id": aideate_project.get("id", str(uuid.uuid4())[:8]),
            "customer_name": aideate_project.get("customerName", ""),
            "project_name": aideate_project.get("projectName", aideate_project.get("project_name", "")),
            "project_date": self._parse_date(aideate_project.get("createdDate", aideate_project.get("project_date", ""))),
            "created_at": aideate_project.get("createdDate", datetime.now().isoformat()),
            "updated_at": aideate_project.get("updatedDate", datetime.now().isoformat()),
            # AIdeate extended fields
            "status": aideate_project.get("status", "planning"),
            "type": aideate_project.get("type", "other"),
            "description": aideate_project.get("description", ""),
            "stakeholders": aideate_project.get("stakeholders", ""),
            "competing_solution": aideate_project.get("competingSolution", ""),
            "contract_details": aideate_project.get("contractDetails", ""),
            "agents": aideate_project.get("agents", []),
            "notes": aideate_project.get("notes", ""),
            "mvp_use_case": aideate_project.get("mvpUseCase", ""),
            "mvp_description": aideate_project.get("mvpDescription", ""),
            "mvp_timeline": aideate_project.get("mvpTimeline", ""),
            # RAPP Pipeline fields (preserve if present)
            "current_step": aideate_project.get("current_step", 1),
            "completed_steps": aideate_project.get("completed_steps", []),
            "step_notes": aideate_project.get("step_notes", {}),
            "step_checklists": aideate_project.get("step_checklists", {}),
            "step_decisions": aideate_project.get("step_decisions", {}),
        }

    def _normalize_internal_to_aideate(self, internal_project: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert internal format (snake_case) to AIdeate format (camelCase) for export.
        """
        return {
            "id": internal_project.get("id", ""),
            "customerName": internal_project.get("customer_name", ""),
            "projectName": internal_project.get("project_name", ""),
            "status": internal_project.get("status", "planning"),
            "type": internal_project.get("type", "other"),
            "description": internal_project.get("description", ""),
            "stakeholders": internal_project.get("stakeholders", ""),
            "competingSolution": internal_project.get("competing_solution", ""),
            "contractDetails": internal_project.get("contract_details", ""),
            "agents": internal_project.get("agents", []),
            "notes": internal_project.get("notes", ""),
            "mvpUseCase": internal_project.get("mvp_use_case", ""),
            "mvpDescription": internal_project.get("mvp_description", ""),
            "mvpTimeline": internal_project.get("mvp_timeline", ""),
            "createdDate": internal_project.get("created_at", ""),
            "updatedDate": internal_project.get("updated_at", ""),
        }

    def _parse_date(self, date_str: str) -> str:
        """Parse various date formats to YYYY-MM-DD."""
        if not date_str:
            return datetime.now().strftime('%Y-%m-%d')

        # If already in YYYY-MM-DD format
        if len(date_str) == 10 and date_str[4] == '-' and date_str[7] == '-':
            return date_str

        # Try to parse ISO format
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d')
        except (ValueError, AttributeError):
            return datetime.now().strftime('%Y-%m-%d')

    def _create_project(self, kwargs, user_guid):
        """Create a new project with full AIdeate schema support."""
        customer_name = kwargs.get('customer_name', '')
        project_name = kwargs.get('project_name', '')
        project_date = kwargs.get('project_date', datetime.now().strftime('%Y-%m-%d'))

        if not customer_name and not project_name:
            return json.dumps({"status": "error", "error": "At least customer_name or project_name is required"})

        # Generate project ID
        project_id = str(uuid.uuid4())[:8]

        # Create project data with all AIdeate fields
        project_data = {
            "id": project_id,
            "customer_name": customer_name,
            "project_name": project_name,
            "project_date": project_date,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            # AIdeate extended fields
            "status": kwargs.get('status', 'planning'),
            "type": kwargs.get('type', 'other'),
            "description": kwargs.get('description', ''),
            "stakeholders": kwargs.get('stakeholders', ''),
            "competing_solution": kwargs.get('competing_solution', ''),
            "contract_details": kwargs.get('contract_details', ''),
            "agents": kwargs.get('agents', []),
            "notes": kwargs.get('notes', ''),
            "mvp_use_case": kwargs.get('mvp_use_case', ''),
            "mvp_description": kwargs.get('mvp_description', ''),
            "mvp_timeline": kwargs.get('mvp_timeline', ''),
            # RAPP Pipeline fields
            "current_step": kwargs.get('current_step', 1),
            "completed_steps": kwargs.get('completed_steps', []),
            "step_notes": kwargs.get('step_notes', {}),
            "step_checklists": kwargs.get('step_checklists', {}),
            "step_decisions": kwargs.get('step_decisions', {}),
            # Engagement data (populated by RAPP agents)
            "discovery_data": kwargs.get('discovery_data', {}),
            "qg_results": kwargs.get('qg_results', {}),
            "mvp_document": kwargs.get('mvp_document', {}),
            "generated_code": kwargs.get('generated_code', {}),
            "step_artifacts": kwargs.get('step_artifacts', {}),
            "user_guid": user_guid
        }

        # Save project file
        directory = self._get_user_directory(user_guid)
        self.storage_manager.write_file(directory, f'project_{project_id}.json', json.dumps(project_data, indent=2))

        # Update index
        index = self._get_projects_index(user_guid)
        index["projects"].append({
            "id": project_id,
            "customer_name": customer_name,
            "project_name": project_name,
            "status": project_data["status"],
            "type": project_data["type"],
            "created_at": project_data["created_at"]
        })
        self._save_projects_index(user_guid, index)

        logger.info(f"Created project {project_id} for user {user_guid}")

        return json.dumps({
            "status": "success",
            "message": f"Project created successfully",
            "project": project_data
        })

    def _update_project(self, kwargs, user_guid):
        """Update an existing project with full AIdeate schema support."""
        project_id = kwargs.get('project_id')
        if not project_id:
            return json.dumps({"status": "error", "error": "project_id is required for update"})

        # Load existing project
        directory = self._get_user_directory(user_guid)
        project_content = self.storage_manager.read_file(directory, f'project_{project_id}.json')

        if not project_content:
            return json.dumps({"status": "error", "error": f"Project {project_id} not found"})

        try:
            project_data = json.loads(project_content)
        except json.JSONDecodeError:
            return json.dumps({"status": "error", "error": f"Invalid project data for {project_id}"})

        # All updatable fields (basic + AIdeate + RAPP)
        update_fields = [
            'customer_name', 'project_name', 'project_date',
            'status', 'type', 'description', 'stakeholders',
            'competing_solution', 'contract_details', 'agents', 'notes',
            'mvp_use_case', 'mvp_description', 'mvp_timeline',
            'current_step', 'completed_steps'
        ]

        # Fields that should be merged (dict update) instead of replaced
        merge_fields = ['step_notes', 'step_checklists', 'step_decisions', 'qg_results', 'step_artifacts']

        # Fields that should be replaced entirely (complex engagement data)
        replace_object_fields = ['discovery_data', 'mvp_document', 'generated_code']

        updated = False
        for field in update_fields:
            if field in kwargs and kwargs[field] is not None:
                project_data[field] = kwargs[field]
                updated = True

        # Handle merge fields - merge new values with existing instead of replacing
        for field in merge_fields:
            if field in kwargs and kwargs[field] is not None:
                existing = project_data.get(field, {})
                if isinstance(existing, dict) and isinstance(kwargs[field], dict):
                    # Merge: existing values are kept, new values are added/updated
                    existing.update(kwargs[field])
                    project_data[field] = existing
                else:
                    # Fallback to replace if types don't match
                    project_data[field] = kwargs[field]
                updated = True

        # Handle replace object fields - replace entirely (engagement data)
        for field in replace_object_fields:
            if field in kwargs and kwargs[field] is not None:
                project_data[field] = kwargs[field]
                updated = True

        if updated:
            project_data["updated_at"] = datetime.now().isoformat()
            self.storage_manager.write_file(directory, f'project_{project_id}.json', json.dumps(project_data, indent=2))

            # Update index if key fields changed
            index_update_fields = ['customer_name', 'project_name', 'status', 'type']
            if any(f in kwargs for f in index_update_fields):
                index = self._get_projects_index(user_guid)
                for proj in index["projects"]:
                    if proj["id"] == project_id:
                        for f in index_update_fields:
                            if f in kwargs:
                                proj[f] = kwargs[f]
                        break
                self._save_projects_index(user_guid, index)

            logger.info(f"Updated project {project_id}")

        return json.dumps({
            "status": "success",
            "message": f"Project {project_id} updated successfully",
            "project": project_data
        })

    def _list_projects(self, user_guid):
        """List all projects for a user with full AIdeate fields."""
        index = self._get_projects_index(user_guid)
        projects = index.get("projects", [])

        # Enrich with full project info
        enriched_projects = []
        directory = self._get_user_directory(user_guid)

        for proj_summary in projects:
            project_content = self.storage_manager.read_file(directory, f'project_{proj_summary["id"]}.json')
            if project_content:
                try:
                    project_data = json.loads(project_content)
                    enriched_projects.append({
                        "id": proj_summary["id"],
                        "customer_name": project_data.get("customer_name", ""),
                        "project_name": project_data.get("project_name", ""),
                        "project_date": project_data.get("project_date", ""),
                        "status": project_data.get("status", "planning"),
                        "type": project_data.get("type", "other"),
                        "mvp_use_case": project_data.get("mvp_use_case", ""),
                        "mvp_timeline": project_data.get("mvp_timeline", ""),
                        "agents_count": len(project_data.get("agents", [])),
                        "current_step": project_data.get("current_step", 1),
                        "completed_steps": len(project_data.get("completed_steps", [])),
                        "total_steps": 14,
                        "created_at": project_data.get("created_at", ""),
                        "updated_at": project_data.get("updated_at", "")
                    })
                except json.JSONDecodeError:
                    continue

        return json.dumps({
            "status": "success",
            "count": len(enriched_projects),
            "projects": enriched_projects
        })

    def _get_project(self, kwargs, user_guid):
        """Get a specific project by ID with all fields."""
        project_id = kwargs.get('project_id')
        if not project_id:
            return json.dumps({"status": "error", "error": "project_id is required"})

        directory = self._get_user_directory(user_guid)
        project_content = self.storage_manager.read_file(directory, f'project_{project_id}.json')

        if not project_content:
            return json.dumps({"status": "error", "error": f"Project {project_id} not found"})

        try:
            project_data = json.loads(project_content)
            return json.dumps({
                "status": "success",
                "project": project_data
            })
        except json.JSONDecodeError:
            return json.dumps({"status": "error", "error": f"Invalid project data for {project_id}"})

    def _delete_project(self, kwargs, user_guid):
        """Delete a project."""
        project_id = kwargs.get('project_id')
        if not project_id:
            return json.dumps({"status": "error", "error": "project_id is required"})

        directory = self._get_user_directory(user_guid)

        # Check if project exists
        project_content = self.storage_manager.read_file(directory, f'project_{project_id}.json')
        if not project_content:
            return json.dumps({"status": "error", "error": f"Project {project_id} not found"})

        # Delete project file
        deleted = self.storage_manager.delete_file(directory, f'project_{project_id}.json')

        if deleted:
            # Update index
            index = self._get_projects_index(user_guid)
            index["projects"] = [p for p in index["projects"] if p["id"] != project_id]
            self._save_projects_index(user_guid, index)

            logger.info(f"Deleted project {project_id}")
            return json.dumps({
                "status": "success",
                "message": f"Project {project_id} deleted successfully"
            })
        else:
            return json.dumps({"status": "error", "error": f"Failed to delete project {project_id}"})

    def _export_project(self, kwargs, user_guid):
        """Export a project in AIdeate format."""
        project_id = kwargs.get('project_id')
        if not project_id:
            return json.dumps({"status": "error", "error": "project_id is required"})

        directory = self._get_user_directory(user_guid)
        project_content = self.storage_manager.read_file(directory, f'project_{project_id}.json')

        if not project_content:
            return json.dumps({"status": "error", "error": f"Project {project_id} not found"})

        try:
            project_data = json.loads(project_content)
            aideate_format = self._normalize_internal_to_aideate(project_data)

            return json.dumps({
                "status": "success",
                "export": aideate_format
            })
        except json.JSONDecodeError:
            return json.dumps({"status": "error", "error": f"Invalid project data for {project_id}"})

    def _import_aideate_data(self, kwargs, user_guid):
        """
        Import full AIdeate JSON data structure.
        Handles projects, agents catalog, and timeline.
        """
        import_data = kwargs.get('import_data')
        if not import_data:
            return json.dumps({"status": "error", "error": "import_data is required"})

        if isinstance(import_data, str):
            try:
                import_data = json.loads(import_data)
            except json.JSONDecodeError:
                return json.dumps({"status": "error", "error": "Invalid JSON in import_data"})

        directory = self._get_user_directory(user_guid)
        imported_count = 0
        updated_count = 0
        errors = []

        # Import projects
        projects = import_data.get('projects', [])
        for aideate_project in projects:
            try:
                # Convert to internal format
                internal_project = self._normalize_aideate_to_internal(aideate_project)
                project_id = internal_project['id']
                internal_project['user_guid'] = user_guid

                # Check if project exists
                existing = self.storage_manager.read_file(directory, f'project_{project_id}.json')

                if existing:
                    # Merge with existing (preserve RAPP pipeline data)
                    try:
                        existing_data = json.loads(existing)
                        # Preserve RAPP fields from existing if not in import
                        for rapp_field in ['current_step', 'completed_steps', 'step_notes', 'step_checklists', 'step_decisions']:
                            if rapp_field not in aideate_project and rapp_field in existing_data:
                                internal_project[rapp_field] = existing_data[rapp_field]
                    except json.JSONDecodeError:
                        pass
                    updated_count += 1
                else:
                    imported_count += 1

                # Save project
                self.storage_manager.write_file(
                    directory,
                    f'project_{project_id}.json',
                    json.dumps(internal_project, indent=2)
                )

            except Exception as e:
                errors.append(f"Project {aideate_project.get('id', 'unknown')}: {str(e)}")

        # Rebuild index from all project files
        self._rebuild_projects_index(user_guid)

        # Import agents catalog if present
        agents_catalog = import_data.get('agents')
        if agents_catalog:
            self.storage_manager.write_file(
                directory,
                'agents_catalog.json',
                json.dumps(agents_catalog, indent=2)
            )

        # Import timeline if present
        timeline = import_data.get('timeline', [])
        if timeline:
            # Load existing timeline and merge
            existing_timeline = self._get_timeline(user_guid)

            # Add new events (avoid duplicates by date+title)
            existing_keys = {(e.get('date', ''), e.get('title', '')) for e in existing_timeline}
            for event in timeline:
                key = (event.get('date', ''), event.get('title', ''))
                if key not in existing_keys:
                    existing_timeline.append(event)

            # Sort by date descending
            existing_timeline.sort(key=lambda x: x.get('date', ''), reverse=True)

            self.storage_manager.write_file(
                directory,
                'timeline.json',
                json.dumps(existing_timeline, indent=2)
            )

        result = {
            "status": "success",
            "message": f"Import completed: {imported_count} new, {updated_count} updated",
            "imported": imported_count,
            "updated": updated_count,
            "total_projects": imported_count + updated_count
        }

        if errors:
            result["errors"] = errors
            result["error_count"] = len(errors)

        return json.dumps(result)

    def _rebuild_projects_index(self, user_guid):
        """Rebuild the projects index from project files."""
        directory = self._get_user_directory(user_guid)

        # List all project files
        try:
            files = self.storage_manager.list_files(directory)
            project_files = [f for f in files if hasattr(f, 'name') and f.name.startswith('project_') and f.name.endswith('.json')]
        except Exception:
            project_files = []

        projects_index = []
        for pf in project_files:
            project_content = self.storage_manager.read_file(directory, pf.name)
            if project_content:
                try:
                    project_data = json.loads(project_content)
                    projects_index.append({
                        "id": project_data.get("id", ""),
                        "customer_name": project_data.get("customer_name", ""),
                        "project_name": project_data.get("project_name", ""),
                        "status": project_data.get("status", "planning"),
                        "type": project_data.get("type", "other"),
                        "created_at": project_data.get("created_at", "")
                    })
                except json.JSONDecodeError:
                    continue

        # Sort by updated_at descending
        projects_index.sort(key=lambda x: x.get('created_at', ''), reverse=True)

        self._save_projects_index(user_guid, {"projects": projects_index})

    def _get_timeline(self, user_guid) -> List[Dict[str, Any]]:
        """Get timeline events for a user."""
        directory = self._get_user_directory(user_guid)
        timeline_content = self.storage_manager.read_file(directory, 'timeline.json')
        if timeline_content:
            try:
                return json.loads(timeline_content)
            except json.JSONDecodeError:
                pass
        return []

    def _add_timeline_event(self, kwargs, user_guid):
        """Add a timeline event."""
        event = kwargs.get('timeline_event')
        if not event:
            return json.dumps({"status": "error", "error": "timeline_event is required"})

        if isinstance(event, str):
            try:
                event = json.loads(event)
            except json.JSONDecodeError:
                return json.dumps({"status": "error", "error": "Invalid JSON in timeline_event"})

        # Ensure required fields
        if not event.get('title'):
            return json.dumps({"status": "error", "error": "timeline_event.title is required"})

        # Add date if not present
        if not event.get('date'):
            event['date'] = datetime.now().isoformat()

        # Load and update timeline
        timeline = self._get_timeline(user_guid)
        timeline.append(event)
        timeline.sort(key=lambda x: x.get('date', ''), reverse=True)

        directory = self._get_user_directory(user_guid)
        self.storage_manager.write_file(directory, 'timeline.json', json.dumps(timeline, indent=2))

        return json.dumps({
            "status": "success",
            "message": "Timeline event added",
            "event": event
        })

    def _list_agents_catalog(self, user_guid):
        """List the agents catalog."""
        directory = self._get_user_directory(user_guid)
        catalog_content = self.storage_manager.read_file(directory, 'agents_catalog.json')

        if catalog_content:
            try:
                catalog = json.loads(catalog_content)
                return json.dumps({
                    "status": "success",
                    "catalog": catalog,
                    "builtin_count": len(catalog.get("builtin", [])),
                    "custom_count": len(catalog.get("custom", []))
                })
            except json.JSONDecodeError:
                pass

        return json.dumps({
            "status": "success",
            "catalog": {"builtin": [], "custom": []},
            "builtin_count": 0,
            "custom_count": 0
        })

    def _update_agents_catalog(self, kwargs, user_guid):
        """Update the agents catalog."""
        catalog = kwargs.get('agents_catalog')
        if not catalog:
            return json.dumps({"status": "error", "error": "agents_catalog is required"})

        if isinstance(catalog, str):
            try:
                catalog = json.loads(catalog)
            except json.JSONDecodeError:
                return json.dumps({"status": "error", "error": "Invalid JSON in agents_catalog"})

        directory = self._get_user_directory(user_guid)
        self.storage_manager.write_file(directory, 'agents_catalog.json', json.dumps(catalog, indent=2))

        return json.dumps({
            "status": "success",
            "message": "Agents catalog updated",
            "builtin_count": len(catalog.get("builtin", [])),
            "custom_count": len(catalog.get("custom", []))
        })


# Usage example
if __name__ == "__main__":
    agent = ProjectTrackerAgent()

    # Example AIdeate import
    sample_import = {
        "projects": [
            {
                "id": "test-123",
                "customerName": "Acme Corp",
                "status": "active",
                "type": "customer-service",
                "description": "AI-powered customer service transformation",
                "stakeholders": "CTO, VP Engineering",
                "competingSolution": "Salesforce",
                "contractDetails": "$500k ACV",
                "agents": ["CustomerServiceAgent", "EmailToCaseAgent"],
                "notes": "High priority engagement",
                "mvpUseCase": "Email Automation",
                "mvpDescription": "Automated email categorization and routing",
                "mvpTimeline": "6 weeks",
                "createdDate": "2025-01-01T00:00:00Z",
                "updatedDate": "2025-01-06T00:00:00Z"
            }
        ],
        "agents": {
            "builtin": [{"name": "SharePointDocumentExtractor", "description": "Extract from SharePoint", "category": "integration", "status": "existing"}],
            "custom": [{"name": "CustomerServiceAgent", "description": "Custom CS agent", "category": "workflow", "status": "new"}]
        },
        "timeline": [
            {"date": "2025-01-01T00:00:00Z", "title": "Project Kickoff", "description": "Initial engagement started"}
        ]
    }

    result = agent.perform(
        action="import",
        import_data=sample_import,
        user_guid="test-user-123"
    )
    print("Import result:", result)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
