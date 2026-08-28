---
name: "rar-discreetrappers-project-tracker"
description: "Manages RAPP Pipeline and AIdeate project tracking data. Use this agent to create, update, import, list, retrieve, or delete project tracking information including full project details, agent assignments, competitive intelligence, contract details, MVP definitions, and timeline events."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/project_tracker_agent", "rar_sha256": "b9df9cb9d4f0743092aae62cabc5a156bd6b7f73fd773fce14584278f1c56fa4", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Bill Whalen", "tags": ["pipeline", "project-management", "tracking"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `project_tracker_agent.py` and embedded as the fenced Python below (sha256 b9df9cb9d4f07430…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `project_tracker_agent.py` first:

```bash
python3 project_tracker_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 project_tracker_agent.py   # or on stdin
python3 project_tracker_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
