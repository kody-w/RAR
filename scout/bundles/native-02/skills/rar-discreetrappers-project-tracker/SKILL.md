---
name: "rar-discreetrappers-project-tracker"
description: "Manages RAPP Pipeline and AIdeate project tracking data. Use this agent to create, update, import, list, retrieve, or delete project tracking information including full project details, agent assignments, competitive intelligence, contract details, MVP definitions, and timeline events."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/project_tracker_agent", "rar_sha256": "b9df9cb9d4f0743092aae62cabc5a156bd6b7f73fd773fce14584278f1c56fa4", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "project_tracker_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/project-tracker:d3ed069ac4f071cef934ce499956823ecb0371dad7a84b53cdeadad7f3ca8918", "kind": "skill"}, "version": "1.0.1", "author": "Bill Whalen", "tags": ["pipeline", "project-management", "tracking"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/project_tracker_agent`. The
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
