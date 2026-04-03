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
    "name": "@discreetRappers/project_tracker",
    "version": "1.0.0",
    "display_name": "ProjectTracker",
    "description": "RAPP project management — create, update, list, retrieve, import, and export project tracking data.",
    "author": "Bill Whalen",
    "tags": ["pipeline", "project-management", "tracking"],
    "category": "pipeline",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
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
