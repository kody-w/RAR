---
name: "rar-discreetrappers-project-tracker"
description: "Manages RAPP Pipeline and AIdeate project tracking data. Use this agent to create, update, import, list, retrieve, or delete project tracking information including full project details, agent assignments, competitive intelligence, contract details, MVP definitions, and timeline events."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/project_tracker_agent", "rar_sha256": "6ce05fe89b9c16b52949a4e36991f5d9536cb7981aa891d93b4fc53419bd4849", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Bill Whalen", "tags": ["pipeline", "project-management", "tracking"]}
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
