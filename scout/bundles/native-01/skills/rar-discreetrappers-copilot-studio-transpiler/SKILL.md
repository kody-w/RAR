---
name: "rar-discreetrappers-copilot-studio-transpiler"
description: "Converts RAPP Python agents to fully native Copilot Studio solutions without Function App dependency."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/copilot_studio_transpiler_agent", "rar_sha256": "acccbacba2be5acb4aa7583abb1c85aee291c5205f4d7915d6eeafc579c86934", "source_kind": "rar-agent", "source_commit": "4a5ea1bb2d453217e8cf5ad16c44542a06d6066d", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "copilot_studio_transpiler_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/copilot-studio-transpiler:4e3cd89201ddb2eef403ce09eff5dae26d49e34075d94c9ee0b4f76fe873867f", "kind": "skill"}, "author": "Bill Whalen", "tags": ["pipeline", "transpiler", "copilot-studio", "native", "no-code"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/copilot_studio_transpiler_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `copilot_studio_transpiler_agent.py` is
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

Copilot Studio Transpiler Agent
Converts RAPP Python agents to fully native Copilot Studio solutions.

This transpiler generates STANDALONE Copilot Studio agents that do NOT require
the RAPP Function App backend. Instead, it maps RAPP capabilities to:
- Native Copilot Studio Topics
- Power Automate Flows (for complex logic)
- Native Connectors (Salesforce, SharePoint, Dataverse, etc.)
- Generative AI capabilities (replaces Azure OpenAI direct calls)

Usage:
    transpiler = CopilotStudioTranspilerAgent()
    result = transpiler.perform(
        action="transpile",
        agent_name="FabrikamCaseTriageOrchestrator",
        output_format="solution"  # or "yaml" for individual files
    )

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Transpilation action to perform",
      "enum": [
        "transpile",
        "analyze",
        "preview",
        "validate",
        "list_connectors",
        "batch_transpile",
        "package",
        "deploy",
        "deploy_status",
        "configure_deployment"
      ],
      "type": "string"
    },
    "agent_file": {
      "description": "Path to the agent Python file (optional, will search if not provided)",
      "type": "string"
    },
    "agent_list": {
      "description": "List of agent names for batch_transpile",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "agent_name": {
      "description": "Name of the RAPP agent to transpile (e.g., 'FabrikamCaseTriageOrchestrator')",
      "type": "string"
    },
    "client_id": {
      "description": "Azure AD app registration client ID",
      "type": "string"
    },
    "dataverse_alternative": {
      "default": true,
      "description": "Use Dataverse instead of Cosmos DB where possible",
      "type": "boolean"
    },
    "environment_url": {
      "description": "Dataverse environment URL for deployment (e.g., https://org.crm.dynamics.com)",
      "type": "string"
    },
    "include_flows": {
      "default": true,
      "description": "Generate Power Automate flows for complex actions",
      "type": "boolean"
    },
    "output_format": {
      "default": "solution",
      "description": "Output format - 'solution' for importable package",
      "enum": [
        "solution",
        "yaml",
        "json"
      ],
      "type": "string"
    },
    "pattern": {
      "description": "Pattern to match agent names for batch_transpile (e.g., 'contoso')",
      "type": "string"
    },
    "tenant_id": {
      "description": "Azure AD tenant ID for deployment authentication",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_transpiler_agent.py` and embedded as the fenced Python below (sha256 acccbacba2be5acb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_transpiler_agent.py` first:

```bash
python3 copilot_studio_transpiler_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_transpiler_agent.py   # or on stdin
python3 copilot_studio_transpiler_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot Studio Transpiler Agent
Converts RAPP Python agents to fully native Copilot Studio solutions.

This transpiler generates STANDALONE Copilot Studio agents that do NOT require
the RAPP Function App backend. Instead, it maps RAPP capabilities to:
- Native Copilot Studio Topics
- Power Automate Flows (for complex logic)
- Native Connectors (Salesforce, SharePoint, Dataverse, etc.)
- Generative AI capabilities (replaces Azure OpenAI direct calls)

Usage:
    transpiler = CopilotStudioTranspilerAgent()
    result = transpiler.perform(
        action="transpile",
        agent_name="FabrikamCaseTriageOrchestrator",
        output_format="solution"  # or "yaml" for individual files
    )
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/copilot_studio_transpiler_agent",
    "version": "1.0.0",
    "display_name": "CopilotStudioTranspiler",
    "description": "Transpiles RAPP Python agents to fully native Copilot Studio solutions without Azure Function dependency.",
    "author": "Bill Whalen",
    "tags": ["pipeline", "transpiler", "copilot-studio", "native", "no-code"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": ["AZURE_TENANT_ID", "COPILOT_STUDIO_CLIENT_ID", "DATAVERSE_ENVIRONMENT_URL"],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import os
import re
import ast
import logging
from datetime import datetime
from typing import Optional, List, Dict, Any
from agents.basic_agent import BasicAgent

logger = logging.getLogger(__name__)

# =============================================================================
# COPILOT STUDIO MAPPING CONFIGURATION
# =============================================================================

# Maps RAPP external dependencies to Copilot Studio connectors
CONNECTOR_MAPPINGS = {
    "salesforce": {
        "connector_id": "shared_salesforce",
        "display_name": "Salesforce",
        "operations": {
            "query": "GetItems",
            "create": "PostItem",
            "update": "PatchItem",
            "get_by_id": "GetItem"
        }
    },
    "cosmos_db": {
        "connector_id": "shared_documentdb",
        "display_name": "Azure Cosmos DB",
        "alternative": "dataverse",  # Can use Dataverse as simpler alternative
        "operations": {
            "query": "QueryDocuments",
            "create": "CreateDocument",
            "update": "ReplaceDocument"
        }
    },
    "sharepoint": {
        "connector_id": "shared_sharepointonline",
        "display_name": "SharePoint",
        "operations": {
            "get_files": "GetFileContent",
            "create_file": "CreateFile",
            "list_items": "GetItems"
        }
    },
    "azure_openai": {
        "connector_id": None,  # Use native Generative AI
        "display_name": "Generative AI (Native)",
        "note": "Handled by Copilot Studio's built-in AI capabilities"
    },
    "outlook": {
        "connector_id": "shared_office365",
        "display_name": "Office 365 Outlook",
        "operations": {
            "send_email": "SendEmail",
            "get_emails": "GetEmails"
        }
    }
}

# Topic templates for common patterns
TOPIC_TEMPLATES = {
    "greeting": {
        "trigger_phrases": ["hello", "hi", "hey", "start", "help"],
        "type": "system"
    },
    "fallback": {
        "trigger_phrases": [],
        "type": "system",
        "use_generative_answers": True
    },
    "action": {
        "type": "custom",
        "requires_flow": True
    }
}


class CopilotStudioTranspilerAgent(BasicAgent):
    """
    Transpiles RAPP Python agents to native Copilot Studio solutions.
    
    Generates:
    - Solution manifest (for import into Copilot Studio)
    - Agent configuration with instructions
    - Topics for each action
    - Power Automate flows for complex operations
    - Connector configurations for external systems
    
    Capabilities:
    - transpile: Convert RAPP agent to Copilot Studio format
    - analyze: Analyze agent and recommend mapping strategy
    - preview: Preview what would be generated
    - validate: Check if agent can be fully transpiled
    - list_connectors: Show available connector mappings
    """
    
    def __init__(self):
        self.name = "CopilotStudioTranspiler"
        self.metadata = {
            "name": self.name,
            "description": "Converts RAPP Python agents to fully native Copilot Studio solutions without Function App dependency.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["transpile", "analyze", "preview", "validate", "list_connectors", "batch_transpile", "package", "deploy", "deploy_status", "configure_deployment"],
                        "description": "Transpilation action to perform"
                    },
                    "agent_name": {
                        "type": "string",
                        "description": "Name of the RAPP agent to transpile (e.g., 'FabrikamCaseTriageOrchestrator')"
                    },
                    "agent_file": {
                        "type": "string",
                        "description": "Path to the agent Python file (optional, will search if not provided)"
                    },
                    "pattern": {
                        "type": "string",
                        "description": "Pattern to match agent names for batch_transpile (e.g., 'contoso')"
                    },
                    "agent_list": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of agent names for batch_transpile"
                    },
                    "output_format": {
                        "type": "string",
                        "enum": ["solution", "yaml", "json"],
                        "default": "solution",
                        "description": "Output format - 'solution' for importable package"
                    },
                    "include_flows": {
                        "type": "boolean",
                        "default": True,
                        "description": "Generate Power Automate flows for complex actions"
                    },
                    "dataverse_alternative": {
                        "type": "boolean",
                        "default": True,
                        "description": "Use Dataverse instead of Cosmos DB where possible"
                    },
                    "environment_url": {
                        "type": "string",
                        "description": "Dataverse environment URL for deployment (e.g., https://org.crm.dynamics.com)"
                    },
                    "tenant_id": {
                        "type": "string",
                        "description": "Azure AD tenant ID for deployment authentication"
                    },
                    "client_id": {
                        "type": "string",
                        "description": "Azure AD app registration client ID"
                    }
                },
                "required": ["action"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.output_path = os.path.join(self.base_path, "transpiled", "copilot_studio_native")
    
    def perform(self, **kwargs) -> str:
        """Execute transpilation action."""
        action = kwargs.get("action", "analyze")
        
        try:
            if action == "transpile":
                return self._transpile(**kwargs)
            elif action == "analyze":
                return self._analyze(**kwargs)
            elif action == "preview":
                return self._preview(**kwargs)
            elif action == "validate":
                return self._validate(**kwargs)
            elif action == "list_connectors":
                return self._list_connectors()
            elif action == "batch_transpile":
                return self._batch_transpile(
                    pattern=kwargs.get("pattern"),
                    agent_list=kwargs.get("agent_list")
                )
            elif action == "package":
                return self._create_solution_package(kwargs.get("agent_name"))
            elif action == "deploy":
                return self._deploy_to_copilot_studio(**kwargs)
            elif action == "deploy_status":
                return self._check_deployment_status(**kwargs)
            elif action == "configure_deployment":
                return self._configure_deployment(**kwargs)
            elif action == "deploy_solution":
                return self._deploy_solution(**kwargs)
            elif action == "list_solutions":
                return self._list_solutions(**kwargs)
            elif action == "create_solution":
                return self._create_solution_definition(**kwargs)
            else:
                return json.dumps({
                    "status": "error",
                    "error": f"Unknown action: {action}"
                })
        except Exception as e:
            logger.error(f"Transpiler error: {e}")
            import traceback
            return json.dumps({
                "status": "error",
                "error": str(e),
                "traceback": traceback.format_exc()
            })
    
    def _transpile(self, **kwargs) -> str:
        """Transpile RAPP agent to Copilot Studio native format."""
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            return json.dumps({"status": "error", "error": "agent_name is required"})
        
        # Find and parse the agent
        agent_def = self._parse_agent(agent_name, kwargs.get("agent_file"))
        if not agent_def:
            return json.dumps({"status": "error", "error": f"Could not find agent: {agent_name}"})
        
        # Analyze dependencies
        analysis = self._analyze_dependencies(agent_def)
        
        # Generate Copilot Studio components
        output_format = kwargs.get("output_format", "solution")
        include_flows = kwargs.get("include_flows", True)
        use_dataverse = kwargs.get("dataverse_alternative", True)
        
        solution = self._generate_solution(
            agent_def, 
            analysis, 
            include_flows=include_flows,
            use_dataverse=use_dataverse
        )
        
        # Save outputs
        output_dir = self._save_solution(agent_name, solution, output_format)
        
        return json.dumps({
            "status": "success",
            "agent_name": agent_name,
            "output_directory": output_dir,
            "files_generated": list(solution.keys()),
            "connectors_required": analysis.get("connectors", []),
            "flows_generated": len([f for f in solution.keys() if "flow" in f.lower()]),
            "topics_generated": len([f for f in solution.keys() if "topic" in f.lower()]),
            "deployment_notes": self._get_deployment_notes(analysis)
        }, indent=2)
    
    def _analyze(self, **kwargs) -> str:
        """Analyze agent and recommend transpilation strategy."""
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            return json.dumps({"status": "error", "error": "agent_name is required"})
        
        agent_def = self._parse_agent(agent_name, kwargs.get("agent_file"))
        if not agent_def:
            return json.dumps({"status": "error", "error": f"Could not find agent: {agent_name}"})
        
        analysis = self._analyze_dependencies(agent_def)
        
        # Determine transpilation feasibility
        feasibility = self._assess_feasibility(analysis)
        
        return json.dumps({
            "status": "success",
            "agent_name": agent_name,
            "analysis": analysis,
            "feasibility": feasibility,
            "recommendations": self._get_recommendations(analysis, feasibility)
        }, indent=2)
    
    def _preview(self, **kwargs) -> str:
        """Preview what would be generated without saving."""
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            return json.dumps({"status": "error", "error": "agent_name is required"})
        
        agent_def = self._parse_agent(agent_name, kwargs.get("agent_file"))
        if not agent_def:
            return json.dumps({"status": "error", "error": f"Could not find agent: {agent_name}"})
        
        analysis = self._analyze_dependencies(agent_def)
        solution = self._generate_solution(agent_def, analysis)
        
        # Return preview without saving
        preview = {}
        for filename, content in solution.items():
            if isinstance(content, dict):
                preview[filename] = content
            else:
                preview[filename] = f"[{len(content)} characters]"
        
        return json.dumps({
            "status": "success",
            "agent_name": agent_name,
            "preview": preview
        }, indent=2)
    
    def _validate(self, **kwargs) -> str:
        """Validate if agent can be fully transpiled."""
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            return json.dumps({"status": "error", "error": "agent_name is required"})
        
        agent_def = self._parse_agent(agent_name, kwargs.get("agent_file"))
        if not agent_def:
            return json.dumps({"status": "error", "error": f"Could not find agent: {agent_name}"})
        
        analysis = self._analyze_dependencies(agent_def)
        feasibility = self._assess_feasibility(analysis)
        
        issues = []
        warnings = []
        
        # Check for unsupported features
        for dep in analysis.get("unsupported_dependencies", []):
            issues.append(f"Unsupported dependency: {dep}")
        
        # Check for features that need manual config
        for feature in analysis.get("manual_config_required", []):
            warnings.append(f"Manual configuration needed: {feature}")
        
        return json.dumps({
            "status": "success",
            "agent_name": agent_name,
            "can_transpile": feasibility["can_transpile"],
            "transpile_completeness": feasibility["completeness_percent"],
            "issues": issues,
            "warnings": warnings
        }, indent=2)
    
    def _list_connectors(self) -> str:
        """List available connector mappings."""
        connectors = []
        for key, config in CONNECTOR_MAPPINGS.items():
            connectors.append({
                "rapp_dependency": key,
                "copilot_studio_connector": config["display_name"],
                "connector_id": config.get("connector_id"),
                "alternative": config.get("alternative"),
                "note": config.get("note")
            })
        
        return json.dumps({
            "status": "success",
            "connectors": connectors
        }, indent=2)
    
    # =========================================================================
    # PARSING METHODS
    # =========================================================================
    
    def _parse_agent(self, agent_name: str, agent_file: str = None) -> Optional[Dict]:
        """
        Parse a RAPP agent into a definition dictionary.
        
        Supports both:
        - Python agent files (.py) in agents/ directory
        - JSON agent definitions (.json) in demos/ directory
        """
        # Find the agent file (JSON or Python)
        if agent_file and os.path.exists(agent_file):
            file_path = agent_file
        else:
            file_path = self._find_agent_file(agent_name)
        
        if not file_path:
            logger.error(f"Could not find agent file for: {agent_name}")
            return None
        
        try:
            # Determine file type and parse accordingly
            if file_path.endswith('.json'):
                return self._parse_json_agent(agent_name, file_path)
            else:
                return self._parse_python_agent(agent_name, file_path)
            
        except Exception as e:
            logger.error(f"Error parsing agent file: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def _parse_json_agent(self, agent_name: str, file_path: str) -> Optional[Dict]:
        """Parse a RAPP JSON agent definition file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        agent_info = data.get("agent", {})
        metadata = data.get("metadata", {})
        
        # Extract systemPrompt - this is CRITICAL for Copilot Studio
        system_prompt = data.get("systemPrompt", "")
        if not system_prompt:
            # Try to build from description and other fields
            system_prompt = self._build_system_prompt_from_json(data)
        
        # Extract actions from metadata or actions array
        actions = []
        if "actions" in data:
            for action in data["actions"]:
                actions.append({
                    "name": action.get("name", ""),
                    "description": action.get("description", ""),
                    "parameters": action.get("parameters", []),
                    "needs_flow": True  # JSON-defined actions typically need flows
                })
        elif "parameters" in metadata and "properties" in metadata["parameters"]:
            action_prop = metadata["parameters"]["properties"].get("action", {})
            if "enum" in action_prop:
                for action_name in action_prop["enum"]:
                    actions.append({
                        "name": action_name,
                        "description": self._action_to_description(action_name),
                        "needs_flow": True
                    })
        
        # Build agent definition
        agent_def = {
            "name": agent_name,
            "file_path": file_path,
            "file_type": "json",
            "class_name": metadata.get("name", agent_info.get("name", agent_name)),
            "description": agent_info.get("description", metadata.get("description", "")),
            "system_prompt": system_prompt,
            "actions": actions,
            "imports": [],
            "external_calls": self._detect_external_calls_from_json(data),
            "sub_agents": [],
            "metadata": metadata,
            "raw_json": data  # Keep the full JSON for reference
        }
        
        return agent_def
    
    def _build_system_prompt_from_json(self, data: Dict) -> str:
        """Build a system prompt from JSON agent data if systemPrompt is missing."""
        agent_info = data.get("agent", {})
        metadata = data.get("metadata", {})
        
        parts = []
        
        # Start with the description
        desc = agent_info.get("description", metadata.get("description", ""))
        if desc:
            parts.append(f"You are {agent_info.get('name', 'an AI agent')}. {desc}")
        
        # Add scope information if present
        scope = data.get("scope", {})
        if scope:
            parts.append("\n**SCOPE:**")
            for key, value in scope.items():
                if isinstance(value, dict) and "description" in value:
                    parts.append(f"- {key.replace('_', ' ').title()}: {value['description']}")
        
        # Add signal priorities if present
        signals = data.get("signal_priorities", [])
        if signals:
            parts.append("\n**PRIORITY SIGNALS:**")
            for sig in signals[:5]:  # Limit to top 5
                parts.append(f"- Priority {sig.get('priority', '?')}: {sig.get('signal', '')}")
        
        # Add confidence calibration if present
        conf = data.get("confidence_calibration", {})
        if conf:
            parts.append("\n**CONFIDENCE LEVELS:**")
            for level, info in conf.items():
                if isinstance(info, dict) and "criteria" in info:
                    parts.append(f"- {level.upper()}: {info['criteria']}")
        
        return "\n".join(parts) if parts else "You are a helpful AI assistant."
    
    def _detect_external_calls_from_json(self, data: Dict) -> List[str]:
        """Detect external service calls from JSON agent data."""
        external_calls = []
        json_str = json.dumps(data).lower()
        
        if "salesforce" in json_str or "sobject" in json_str:
            external_calls.append("salesforce")
        if "cosmos" in json_str or "documentdb" in json_str:
            external_calls.append("cosmos_db")
        if "openai" in json_str or "gpt" in json_str:
            external_calls.append("azure_openai")
        if "sharepoint" in json_str or "onedrive" in json_str:
            external_calls.append("sharepoint")
        if "outlook" in json_str or "email" in json_str:
            external_calls.append("outlook")
        
        return external_calls
    
    def _parse_python_agent(self, agent_name: str, file_path: str) -> Optional[Dict]:
        """Parse a RAPP Python agent file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Parse the AST
        tree = ast.parse(source_code)
        
        # Extract agent definition
        agent_def = {
            "name": agent_name,
            "file_path": file_path,
            "file_type": "python",
            "source_code": source_code,
            "class_name": None,
            "description": "",
            "system_prompt": "",
            "actions": [],
            "imports": [],
            "external_calls": [],
            "sub_agents": []
        }
        
        # Extract imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    agent_def["imports"].append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    agent_def["imports"].append(f"{module}.{alias.name}")
        
        # Find the main agent class
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                if "Agent" in node.name:
                    agent_def["class_name"] = node.name
                    agent_def["description"] = ast.get_docstring(node) or ""
                    
                    # Extract metadata from __init__
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef) and item.name == "__init__":
                            agent_def["metadata"] = self._extract_metadata(item)
                        
                        # Extract actions from perform method
                        if isinstance(item, ast.FunctionDef) and item.name == "perform":
                            agent_def["actions"] = self._extract_actions(item)
                    
                    # If AST extraction found no actions, try source-based extraction
                    if not agent_def["actions"]:
                        agent_def["actions"] = self._extract_actions_from_source(source_code)
        
        # Try to extract system_prompt from source
        agent_def["system_prompt"] = self._extract_system_prompt_from_source(source_code)
        
        # Detect external dependencies
        agent_def["external_calls"] = self._detect_external_calls(source_code)
        
        # Detect sub-agents (for orchestrators)
        agent_def["sub_agents"] = self._detect_sub_agents(source_code)
        
        return agent_def
    
    def _extract_system_prompt_from_source(self, source_code: str) -> str:
        """Extract system prompt from Python source code."""
        # Try multiple patterns
        patterns = [
            r'system_prompt\s*=\s*["\'\"](.+?)["\'\"]',
            r'systemPrompt\s*=\s*["\'\"](.+?)["\'\"]',
            r'SYSTEM_PROMPT\s*=\s*["\'\"](.+?)["\'\"]',
            r'instructions\s*=\s*["\'\"](.+?)["\'\"]',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, source_code, re.DOTALL)
            if match:
                return match.group(1).strip()
        
        # Try to find multi-line string assignments
        multiline_patterns = [
            r'system_prompt\s*=\s*"""(.+?)"""',
            r"system_prompt\s*=\s*'''(.+?)'''",
        ]
        
        for pattern in multiline_patterns:
            match = re.search(pattern, source_code, re.DOTALL)
            if match:
                return match.group(1).strip()
        
        return ""
    
    def _find_agent_file(self, agent_name: str) -> Optional[str]:
        """
        Find the Python or JSON file for an agent.
        
        PRIORITY: JSON files are preferred because they contain the full
        systemPrompt and structured agent configuration. Python files are
        used as fallback.
        """
        # Convert agent name to possible file names
        snake_name = self._to_snake_case(agent_name)
        possible_json_names = [
            f"{snake_name}.json",
            f"{snake_name}_agent.json",
            f"{agent_name}.json",
            f"{agent_name.lower()}.json"
        ]
        possible_py_names = [
            f"{snake_name}.py",
            f"{snake_name}_agent.py",
            f"{agent_name}.py",
            f"{agent_name.lower()}.py",
        ]
        
        # FIRST: Search in demos directory for JSON files (preferred - has systemPrompt)
        demos_dir = os.path.join(self.base_path, "demos")
        if os.path.exists(demos_dir):
            for filename in os.listdir(demos_dir):
                if filename.endswith('.json'):
                    if filename in possible_json_names or agent_name.lower() in filename.lower().replace('.json', ''):
                        json_path = os.path.join(demos_dir, filename)
                        logger.info(f"Found JSON agent file: {json_path}")
                        return json_path
        
        # SECOND: Search in agents directory for Python files (fallback)
        agents_dir = os.path.join(self.base_path, "agents")
        for root, dirs, files in os.walk(agents_dir):
            for filename in files:
                if filename.endswith('.py'):
                    if filename in possible_py_names or agent_name.lower() in filename.lower().replace('.py', ''):
                        py_path = os.path.join(root, filename)
                        logger.info(f"Found Python agent file: {py_path}")
                        return py_path
        
        return None
    
    def _extract_metadata(self, init_node: ast.FunctionDef) -> Dict:
        """Extract metadata from __init__ method."""
        metadata = {}
        for node in ast.walk(init_node):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Attribute) and target.attr == "metadata":
                        # Try to extract the dict
                        if isinstance(node.value, ast.Dict):
                            metadata = self._ast_dict_to_python(node.value)
        return metadata
    
    def _extract_actions_from_source(self, source_code: str) -> List[Dict]:
        """Extract actions from source code using regex patterns."""
        actions = []
        
        # Pattern 1: Look for action enum in metadata
        # "enum": ["action1", "action2", ...]
        enum_pattern = r'"enum"\s*:\s*\[([\s\S]*?)\]'
        enum_match = re.search(enum_pattern, source_code)
        if enum_match:
            enum_content = enum_match.group(1)
            # Extract quoted strings
            action_pattern = r'"([^"]+)"'
            action_matches = re.findall(action_pattern, enum_content)
            for action_name in action_matches:
                if action_name not in ['string', 'object', 'array', 'boolean', 'integer']:
                    actions.append({
                        "name": action_name,
                        "description": self._action_to_description(action_name)
                    })
        
        # Pattern 2: Look for if/elif action == "xyz" patterns
        action_compare_pattern = r'action\s*==\s*["\']([^"\']+)["\']'
        compare_matches = re.findall(action_compare_pattern, source_code)
        existing_names = {a["name"] for a in actions}
        for action_name in compare_matches:
            if action_name not in existing_names:
                actions.append({
                    "name": action_name,
                    "description": self._action_to_description(action_name)
                })
                existing_names.add(action_name)
        
        return actions
    
    def _action_to_description(self, action_name: str) -> str:
        """Convert action name to human-readable description."""
        # Replace underscores with spaces and title case
        desc = action_name.replace("_", " ").title()
        return desc
    
    def _extract_actions(self, perform_node: ast.FunctionDef) -> List[Dict]:
        """Extract actions from perform method."""
        actions = []
        
        # Look for if/elif chains checking action
        for node in ast.walk(perform_node):
            if isinstance(node, ast.Compare):
                # Check if comparing action variable
                if isinstance(node.left, ast.Name) and node.left.id == "action":
                    for comparator in node.comparators:
                        if isinstance(comparator, ast.Constant):
                            actions.append({
                                "name": comparator.value,
                                "description": f"Action: {comparator.value}"
                            })
        
        return actions
    
    def _detect_external_calls(self, source_code: str) -> List[str]:
        """Detect external service calls in source code."""
        external_calls = []
        
        # Salesforce patterns
        if re.search(r'salesforce|sf_client|simple_salesforce|sobjects', source_code, re.I):
            external_calls.append("salesforce")
        
        # Cosmos DB patterns
        if re.search(r'cosmos|CosmosClient|documentdb', source_code, re.I):
            external_calls.append("cosmos_db")
        
        # Azure OpenAI patterns
        if re.search(r'openai|AzureOpenAI|ChatCompletion|gpt-4', source_code, re.I):
            external_calls.append("azure_openai")
        
        # SharePoint patterns
        if re.search(r'sharepoint|graph.*sites|OneDrive', source_code, re.I):
            external_calls.append("sharepoint")
        
        # Email/Outlook patterns
        if re.search(r'outlook|send.*email|smtp', source_code, re.I):
            external_calls.append("outlook")
        
        return external_calls
    
    def _detect_sub_agents(self, source_code: str) -> List[str]:
        """Detect sub-agents used by orchestrators."""
        sub_agents = []
        
        # Find agent imports
        pattern = r'from agents\.(\w+) import (\w+Agent)'
        matches = re.findall(pattern, source_code)
        for module, class_name in matches:
            sub_agents.append({
                "module": module,
                "class_name": class_name
            })
        
        return sub_agents
    
    def _ast_dict_to_python(self, node: ast.Dict) -> Dict:
        """Convert AST Dict to Python dict (simplified)."""
        result = {}
        for key, value in zip(node.keys, node.values):
            if isinstance(key, ast.Constant):
                key_str = key.value
                if isinstance(value, ast.Constant):
                    result[key_str] = value.value
                elif isinstance(value, ast.Dict):
                    result[key_str] = self._ast_dict_to_python(value)
                else:
                    result[key_str] = str(ast.dump(value))
        return result
    
    # =========================================================================
    # ANALYSIS METHODS
    # =========================================================================
    
    def _analyze_dependencies(self, agent_def: Dict) -> Dict:
        """Analyze agent dependencies and map to Copilot Studio capabilities."""
        analysis = {
            "agent_type": "simple",
            "connectors": [],
            "native_capabilities": [],
            "flows_needed": [],
            "unsupported_dependencies": [],
            "manual_config_required": []
        }
        
        # Determine agent type
        if agent_def.get("sub_agents"):
            analysis["agent_type"] = "orchestrator"
        elif "analyzer" in agent_def.get("name", "").lower():
            analysis["agent_type"] = "analyzer"
        elif "generator" in agent_def.get("name", "").lower():
            analysis["agent_type"] = "generator"
        
        # Map external calls to connectors
        for call in agent_def.get("external_calls", []):
            mapping = CONNECTOR_MAPPINGS.get(call, {})
            
            if mapping.get("connector_id"):
                analysis["connectors"].append({
                    "type": call,
                    "connector_id": mapping["connector_id"],
                    "display_name": mapping["display_name"]
                })
            elif call == "azure_openai":
                analysis["native_capabilities"].append("generative_ai")
            else:
                analysis["unsupported_dependencies"].append(call)
        
        # Determine which actions need flows
        for action in agent_def.get("actions", []):
            action_name = action.get("name", "")
            
            # Simple queries can be topics, complex operations need flows
            if any(x in action_name.lower() for x in ["get", "list", "query", "status"]):
                action["needs_flow"] = False
            else:
                action["needs_flow"] = True
                analysis["flows_needed"].append(action_name)
        
        # Check for manual config requirements
        if agent_def.get("sub_agents"):
            analysis["manual_config_required"].append(
                "Sub-agent coordination - may need multiple topics or a master flow"
            )
        
        return analysis
    
    def _assess_feasibility(self, analysis: Dict) -> Dict:
        """Assess feasibility of transpilation."""
        issues = len(analysis.get("unsupported_dependencies", []))
        total_features = (
            len(analysis.get("connectors", [])) +
            len(analysis.get("native_capabilities", [])) +
            len(analysis.get("flows_needed", [])) +
            issues
        )
        
        if total_features == 0:
            total_features = 1
        
        completeness = ((total_features - issues) / total_features) * 100
        
        return {
            "can_transpile": issues == 0,
            "completeness_percent": round(completeness, 1),
            "blocking_issues": analysis.get("unsupported_dependencies", []),
            "agent_type": analysis.get("agent_type", "simple")
        }
    
    def _get_recommendations(self, analysis: Dict, feasibility: Dict) -> List[str]:
        """Get recommendations for transpilation."""
        recommendations = []
        
        if feasibility["completeness_percent"] == 100:
            recommendations.append("✅ Agent can be fully transpiled to native Copilot Studio")
        elif feasibility["completeness_percent"] >= 80:
            recommendations.append("⚠️ Agent can be mostly transpiled with some manual configuration")
        else:
            recommendations.append("❌ Agent requires significant manual work or hybrid approach")
        
        if "generative_ai" in analysis.get("native_capabilities", []):
            recommendations.append("💡 Azure OpenAI calls will use Copilot Studio's native Generative AI")
        
        if analysis.get("connectors"):
            connectors = [c["display_name"] for c in analysis["connectors"]]
            recommendations.append(f"🔌 Required connectors: {', '.join(connectors)}")
        
        if analysis.get("flows_needed"):
            recommendations.append(f"⚡ {len(analysis['flows_needed'])} Power Automate flows will be generated")
        
        if analysis.get("agent_type") == "orchestrator":
            recommendations.append("🎭 Orchestrator pattern - consider using topic routing or a master flow")
        
        return recommendations
    
    # =========================================================================
    # GENERATION METHODS
    # =========================================================================
    
    def _generate_solution(self, agent_def: Dict, analysis: Dict, 
                          include_flows: bool = True, use_dataverse: bool = True) -> Dict:
        """Generate complete Copilot Studio solution."""
        solution = {}
        
        agent_name = agent_def.get("name", "RAPPAgent")
        description = agent_def.get("description", "")[:500]
        
        # 1. Generate agent manifest
        solution["agent_manifest.json"] = self._generate_agent_manifest(
            agent_name, description, agent_def, analysis
        )
        
        # 2. Generate system instructions
        solution["instructions.md"] = self._generate_instructions(agent_def)
        
        # 3. Generate topics
        topics = self._generate_topics(agent_def, analysis)
        solution.update(topics)
        
        # 4. Generate flows (if needed)
        if include_flows and analysis.get("flows_needed"):
            flows = self._generate_flows(agent_def, analysis, use_dataverse)
            solution.update(flows)
        
        # 5. Generate connector configs
        if analysis.get("connectors"):
            solution["connectors.json"] = self._generate_connector_configs(analysis)
        
        # 6. Generate deployment guide
        solution["DEPLOYMENT_GUIDE.md"] = self._generate_deployment_guide(
            agent_name, analysis
        )
        
        return solution
    
    def _generate_agent_manifest(self, name: str, description: str, 
                                  agent_def: Dict, analysis: Dict) -> Dict:
        """
        Generate Copilot Studio agent manifest.
        
        CRITICAL: This manifest MUST include the systemPrompt/instructions
        for the agent to function properly in Copilot Studio.
        """
        # Get the system prompt - this is CRITICAL for the agent to work!
        system_prompt = agent_def.get("system_prompt", "")
        if not system_prompt:
            # Try to get from raw_json if available (JSON agent files)
            raw_json = agent_def.get("raw_json", {})
            system_prompt = raw_json.get("systemPrompt", "")
        
        if not system_prompt:
            # Fall back to description-based instructions
            system_prompt = f"You are {name}. {description}"
        
        return {
            "schemaVersion": "1.2",
            "name": name,
            "displayName": self._to_title_case(name),
            "description": description,
            "icon": "robot",
            "primaryLanguage": "en-US",
            "isGenerativeActionsEnabled": True,
            "isOrchestrationEnabled": analysis.get("agent_type") == "orchestrator",
            "knowledgeSources": [],
            # CRITICAL: Include the full system prompt for GPT component creation
            "instructions": system_prompt,
            "systemPrompt": system_prompt,  # Alias for compatibility
            "capabilities": {
                "generativeAnswers": "azure_openai" in agent_def.get("external_calls", []),
                "powerAutomateFlows": len(analysis.get("flows_needed", [])) > 0,
                "customConnectors": len(analysis.get("connectors", [])) > 0
            },
            "topics": [f"topic_{a['name']}" for a in agent_def.get("actions", [])],
            "metadata": {
                "source": "RAPP Transpiler",
                "transpiled_at": datetime.now().isoformat(),
                "original_agent": agent_def.get("class_name", name)
            }
        }
    
    def _generate_instructions(self, agent_def: Dict) -> str:
        """
        Generate agent instructions markdown file.
        
        This extracts the system prompt from multiple sources and formats it
        for documentation purposes. The actual GPT component instructions
        are set in the agent manifest.
        """
        description = agent_def.get("description", "")
        
        # Get system prompt from agent_def (already extracted during parsing)
        system_prompt = agent_def.get("system_prompt", "")
        
        # If not found, try raw_json for JSON agents
        if not system_prompt:
            raw_json = agent_def.get("raw_json", {})
            system_prompt = raw_json.get("systemPrompt", "")
        
        # If still not found, try to extract from Python source
        if not system_prompt:
            source = agent_def.get("source_code", "")
            if source:
                match = re.search(r'system_prompt\s*=\s*["\'](.+?)["\']', source, re.S)
                if match:
                    system_prompt = match.group(1)
        
        # Default if nothing found
        if not system_prompt:
            system_prompt = f"You are {agent_def.get('name', 'an AI agent')}. {description}"
        
        instructions = f"""# {agent_def.get('name', 'Agent')} Instructions

## Overview
{description}

## System Prompt
{system_prompt}

## Available Actions
"""
        for action in agent_def.get("actions", []):
            instructions += f"- **{action['name']}**: {action.get('description', 'No description')}\n"
        
        instructions += """
## Guidelines
1. Be helpful and professional
2. Ask for clarification if the request is unclear
3. Confirm actions before executing them
4. Report results clearly and concisely

## Copilot Studio Notes
This agent was transpiled from a RAPP Python/JSON agent. The system prompt above
has been automatically configured as the GPT component instructions in Copilot Studio.
"""
        return instructions
    
    def _generate_topics(self, agent_def: Dict, analysis: Dict) -> Dict:
        """Generate Copilot Studio topics."""
        topics = {}
        
        # Greeting topic
        topics["topic_greeting.yaml"] = {
            "kind": "AdaptiveDialog",
            "id": "topic_greeting",
            "displayName": "Greeting",
            "triggers": [
                {"kind": "OnRecognizedIntent", "intent": "Greeting"}
            ],
            "actions": [
                {
                    "kind": "SendMessage",
                    "message": f"Hello! I'm the {agent_def.get('name', 'Agent')}. {agent_def.get('description', '')[:200]} How can I help you today?"
                }
            ]
        }
        
        # Generate topic for each action
        for action in agent_def.get("actions", []):
            action_name = action.get("name", "unknown")
            topic_id = f"topic_{action_name}"
            
            # Build trigger phrases
            trigger_phrases = [
                action_name.replace("_", " "),
                f"run {action_name.replace('_', ' ')}",
                f"execute {action_name.replace('_', ' ')}"
            ]
            
            # Build topic actions
            topic_actions = []
            
            if action.get("needs_flow", True):
                # Call Power Automate flow
                topic_actions.append({
                    "kind": "InvokeFlowAction",
                    "flowId": f"flow_{action_name}",
                    "inputs": self._get_action_inputs(action),
                    "outputs": {"result": "flowResult"}
                })
                topic_actions.append({
                    "kind": "SendMessage",
                    "message": "${flowResult}"
                })
            else:
                # Simple generative response
                topic_actions.append({
                    "kind": "GenerativeAnswer",
                    "prompt": f"Help the user with: {action_name.replace('_', ' ')}"
                })
            
            topics[f"{topic_id}.yaml"] = {
                "kind": "AdaptiveDialog",
                "id": topic_id,
                "displayName": self._to_title_case(action_name),
                "triggers": [
                    {
                        "kind": "OnRecognizedIntent",
                        "intent": action_name,
                        "triggerQueries": trigger_phrases
                    }
                ],
                "actions": topic_actions
            }
        
        return topics
    
    def _generate_flows(self, agent_def: Dict, analysis: Dict, 
                        use_dataverse: bool = True) -> Dict:
        """Generate Power Automate flows for complex actions."""
        flows = {}
        
        for action_name in analysis.get("flows_needed", []):
            flow_id = f"flow_{action_name}"
            
            # Build flow definition
            flow = {
                "name": flow_id,
                "displayName": f"{self._to_title_case(action_name)} Flow",
                "description": f"Power Automate flow for {action_name}",
                "trigger": {
                    "kind": "PowerVirtualAgents",
                    "inputs": self._get_action_inputs_schema(action_name, agent_def)
                },
                "actions": self._build_flow_actions(action_name, agent_def, analysis, use_dataverse),
                "outputs": {
                    "result": {
                        "type": "string",
                        "description": "Result of the action"
                    }
                }
            }
            
            flows[f"{flow_id}.json"] = flow
        
        return flows
    
    def _build_flow_actions(self, action_name: str, agent_def: Dict, 
                           analysis: Dict, use_dataverse: bool) -> List[Dict]:
        """Build Power Automate actions for a flow."""
        actions = []
        
        # Check what connectors are needed
        connectors = {c["type"]: c for c in analysis.get("connectors", [])}
        
        if "salesforce" in connectors:
            actions.append({
                "kind": "Salesforce_GetRecords",
                "connection": "salesforce_connection",
                "inputs": {
                    "object": "Case",
                    "query": "SELECT Id, Subject, Description FROM Case"
                },
                "outputs": {"records": "sfRecords"}
            })
        
        if "cosmos_db" in connectors and not use_dataverse:
            actions.append({
                "kind": "CosmosDB_QueryDocuments",
                "connection": "cosmosdb_connection",
                "inputs": {
                    "database": "rapp_db",
                    "collection": "agents"
                },
                "outputs": {"documents": "cosmosData"}
            })
        elif use_dataverse:
            actions.append({
                "kind": "Dataverse_ListRows",
                "connection": "dataverse_connection",
                "inputs": {
                    "entityName": "rapp_data"
                },
                "outputs": {"rows": "dataverseRows"}
            })
        
        # Add AI processing if needed
        if "generative_ai" in analysis.get("native_capabilities", []):
            actions.append({
                "kind": "AzureOpenAI_ChatCompletion",
                "connection": "azure_openai_connection",
                "inputs": {
                    "prompt": f"Process the data for {action_name}",
                    "systemMessage": agent_def.get("description", "")
                },
                "outputs": {"response": "aiResponse"}
            })
        
        # Return result
        actions.append({
            "kind": "Response",
            "inputs": {
                "result": "@{variables('aiResponse') ?? 'Action completed successfully'}"
            }
        })
        
        return actions
    
    def _generate_connector_configs(self, analysis: Dict) -> Dict:
        """Generate connector configuration."""
        connectors = {}
        
        for conn in analysis.get("connectors", []):
            connectors[conn["type"]] = {
                "connectorId": conn["connector_id"],
                "displayName": conn["display_name"],
                "connectionRequired": True,
                "authType": "OAuth2" if conn["type"] in ["salesforce", "sharepoint"] else "ApiKey"
            }
        
        return {
            "connectors": connectors,
            "instructions": "Configure each connector in Power Platform admin center before importing the solution."
        }
    
    def _generate_deployment_guide(self, agent_name: str, analysis: Dict) -> str:
        """Generate deployment guide markdown."""
        guide = f"""# Deployment Guide: {agent_name}

## Overview
This guide covers deploying the transpiled Copilot Studio agent.

## Prerequisites
1. Copilot Studio license
2. Power Platform environment
"""
        
        if analysis.get("connectors"):
            guide += "\n### Required Connectors\n"
            for conn in analysis["connectors"]:
                guide += f"- **{conn['display_name']}** ({conn['connector_id']})\n"
        
        guide += """
## Deployment Steps

### 1. Import the Solution
1. Go to [Power Platform Admin Center](https://admin.powerplatform.microsoft.com)
2. Select your environment
3. Go to Solutions > Import
4. Upload the solution package

### 2. Configure Connectors
"""
        
        if analysis.get("connectors"):
            for conn in analysis["connectors"]:
                guide += f"""
#### {conn['display_name']}
1. Go to Connections in Power Platform
2. Create new connection for {conn['display_name']}
3. Authenticate with your credentials
4. Link to the flows in this solution
"""
        
        guide += """
### 3. Configure the Agent
1. Open Copilot Studio
2. Find the imported agent
3. Review and customize instructions
4. Test the agent in the test canvas

### 4. Publish
1. Click "Publish" in Copilot Studio
2. Configure channels (Teams, Web, etc.)
3. Deploy to users

## Testing
Run through each topic to verify:
- Greeting works
- Each action topic triggers correctly
- Flows execute and return results
- Connectors are authenticated

## Troubleshooting
- **Flow not triggering**: Check Power Automate run history
- **Connector errors**: Verify connection credentials
- **Topic not matching**: Review trigger phrases
"""
        
        return guide
    
    def _get_action_inputs(self, action: Dict) -> Dict:
        """Get input parameters for an action."""
        return {"action": action.get("name", "unknown")}
    
    def _get_action_inputs_schema(self, action_name: str, agent_def: Dict) -> Dict:
        """Get input schema for a flow."""
        return {
            "type": "object",
            "properties": {
                "action": {"type": "string"},
                "parameters": {"type": "object"}
            }
        }
    
    # =========================================================================
    # SAVE METHODS
    # =========================================================================
    
    def _save_solution(self, agent_name: str, solution: Dict, output_format: str) -> str:
        """Save the generated solution files."""
        # Create output directory
        snake_name = self._to_snake_case(agent_name)
        output_dir = os.path.join(self.output_path, snake_name)
        os.makedirs(output_dir, exist_ok=True)
        
        # Create subdirectories
        os.makedirs(os.path.join(output_dir, "topics"), exist_ok=True)
        os.makedirs(os.path.join(output_dir, "flows"), exist_ok=True)
        
        for filename, content in solution.items():
            # Determine subdirectory
            if "topic" in filename.lower():
                filepath = os.path.join(output_dir, "topics", filename)
            elif "flow" in filename.lower():
                filepath = os.path.join(output_dir, "flows", filename)
            else:
                filepath = os.path.join(output_dir, filename)
            
            # Write content
            with open(filepath, 'w', encoding='utf-8') as f:
                if isinstance(content, dict):
                    if filename.endswith('.yaml'):
                        import yaml
                        yaml.dump(content, f, default_flow_style=False, sort_keys=False)
                    else:
                        json.dump(content, f, indent=2)
                else:
                    f.write(content)
        
        return output_dir
    
    def _get_deployment_notes(self, analysis: Dict) -> List[str]:
        """Get deployment notes based on analysis."""
        notes = []
        
        if analysis.get("connectors"):
            notes.append("Configure connectors before importing solution")
        
        if analysis.get("flows_needed"):
            notes.append("Test flows individually before testing full agent")
        
        if analysis.get("agent_type") == "orchestrator":
            notes.append("Orchestrator agents may need topic routing configuration")
        
        return notes
    
    # =========================================================================
    # UTILITY METHODS
    # =========================================================================
    
    def _to_snake_case(self, name: str) -> str:
        """Convert name to snake_case."""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    def _to_title_case(self, name: str) -> str:
        """Convert name to Title Case."""
        return name.replace("_", " ").title()
    
    # =========================================================================
    # BATCH AND PACKAGING METHODS
    # =========================================================================
    
    def _batch_transpile(self, pattern: str = None, agent_list: List[str] = None) -> str:
        """Batch transpile multiple agents matching a pattern."""
        import glob
        
        agents_to_transpile = []
        
        if agent_list:
            agents_to_transpile = agent_list
        elif pattern:
            # Find agents matching pattern
            agents_dir = os.path.join(self.base_path, "agents")
            for f in os.listdir(agents_dir):
                if f.endswith('.py') and pattern.lower() in f.lower():
                    agents_to_transpile.append(f.replace('.py', ''))
        else:
            return json.dumps({"status": "error", "error": "Must provide pattern or agent_list"})
        
        results = []
        for agent_name in agents_to_transpile:
            try:
                agent_def = self._parse_agent(agent_name)
                if agent_def:
                    analysis = self._analyze_dependencies(agent_def)
                    solution = self._generate_solution(agent_def, analysis)
                    output_dir = self._save_solution(agent_name, solution, "solution")
                    results.append({
                        "agent": agent_name,
                        "status": "success",
                        "output_dir": output_dir,
                        "topics": len([k for k in solution.keys() if k.startswith("topic_")]),
                        "flows": len([k for k in solution.keys() if k.startswith("flow_")])
                    })
                else:
                    results.append({"agent": agent_name, "status": "error", "error": "Could not parse"})
            except Exception as e:
                results.append({"agent": agent_name, "status": "error", "error": str(e)})
        
        # Generate combined summary
        successful = [r for r in results if r["status"] == "success"]
        total_topics = sum(r.get("topics", 0) for r in successful)
        total_flows = sum(r.get("flows", 0) for r in successful)
        
        return json.dumps({
            "status": "success",
            "agents_transpiled": len(successful),
            "agents_failed": len(results) - len(successful),
            "total_topics": total_topics,
            "total_flows": total_flows,
            "results": results
        }, indent=2)
    
    def _create_solution_package(self, agent_name: str) -> str:
        """Create a downloadable ZIP package for the solution."""
        import zipfile
        from datetime import datetime
        
        snake_name = self._to_snake_case(agent_name)
        source_dir = os.path.join(self.output_path, snake_name)
        
        if not os.path.exists(source_dir):
            return json.dumps({
                "status": "error",
                "error": f"Solution not found: {source_dir}. Run transpile first."
            })
        
        # Create ZIP file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_filename = f"{snake_name}_copilot_studio_{timestamp}.zip"
        zip_path = os.path.join(self.output_path, zip_filename)
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_dir)
                    zipf.write(file_path, arcname)
        
        return json.dumps({
            "status": "success",
            "package_path": zip_path,
            "package_name": zip_filename,
            "agent_name": agent_name
        }, indent=2)
    # =========================================================================
    # DEPLOYMENT METHODS - Deploy to Copilot Studio via Dataverse API
    # =========================================================================
    
    def _get_deployment_config_file(self) -> str:
        """Get path to deployment configuration file."""
        return os.path.join(self.base_path, "copilot_studio_deployment_config.json")
    
    def _load_deployment_config(self) -> Dict:
        """Load deployment configuration."""
        config_file = self._get_deployment_config_file()
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_deployment_config(self, config: Dict) -> None:
        """Save deployment configuration."""
        config_file = self._get_deployment_config_file()
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
    
    def _configure_deployment(self, **kwargs) -> str:
        """
        Configure deployment settings for Copilot Studio.
        
        Sets up the environment URL, tenant ID, and client ID for API access.
        """
        config = self._load_deployment_config()
        
        # Update with provided values
        if kwargs.get("environment_url"):
            config["environment_url"] = kwargs["environment_url"]
        if kwargs.get("tenant_id"):
            config["tenant_id"] = kwargs["tenant_id"]
        if kwargs.get("client_id"):
            config["client_id"] = kwargs["client_id"]
        
        # Check if any config provided
        if not any([kwargs.get("environment_url"), kwargs.get("tenant_id"), kwargs.get("client_id")]):
            # Return current config and instructions
            return json.dumps({
                "status": "info",
                "current_config": config,
                "instructions": {
                    "setup_steps": [
                        "1. Create an Azure AD app registration in Azure Portal",
                        "2. Add Dataverse/Dynamics CRM API permissions (user_impersonation)",
                        "3. Create a client secret (or use interactive auth)",
                        "4. Get your Dataverse environment URL from Power Platform admin center",
                        "5. Run configure_deployment with environment_url, tenant_id, client_id"
                    ],
                    "example": {
                        "action": "configure_deployment",
                        "environment_url": "https://yourorg.crm.dynamics.com",
                        "tenant_id": "your-tenant-guid",
                        "client_id": "your-app-client-id"
                    },
                    "environment_variables": {
                        "DATAVERSE_ENVIRONMENT_URL": "Alternative to environment_url parameter",
                        "AZURE_TENANT_ID": "Alternative to tenant_id parameter",
                        "COPILOT_STUDIO_CLIENT_ID": "Alternative to client_id parameter",
                        "COPILOT_STUDIO_CLIENT_SECRET": "For service principal auth (optional)"
                    }
                }
            }, indent=2)
        
        self._save_deployment_config(config)
        
        return json.dumps({
            "status": "success",
            "message": "Deployment configuration saved",
            "config": config,
            "next_steps": [
                "Run deploy action with agent_name to deploy a transpiled agent",
                "Example: action='deploy', agent_name='contoso_drains_ci_agent'"
            ]
        }, indent=2)
    
    def _deploy_to_copilot_studio(self, **kwargs) -> str:
        """
        Deploy a transpiled agent to Copilot Studio via Dataverse API.
        
        This creates a new agent in Copilot Studio with all topics and configurations.
        
        Prerequisites:
        - Agent must be transpiled first (action='transpile')
        - Deployment must be configured (action='configure_deployment')
        - User must have Copilot Studio access in the target environment
        """
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            return json.dumps({"status": "error", "error": "agent_name is required"})
        
        # Check for transpiled output
        snake_name = self._to_snake_case(agent_name)
        agent_dir = os.path.join(self.output_path, snake_name)
        
        if not os.path.exists(agent_dir):
            return json.dumps({
                "status": "error",
                "error": f"Transpiled agent not found at {agent_dir}",
                "suggestion": f"Run transpile first: action='transpile', agent_name='{agent_name}'"
            })
        
        # Load agent manifest
        manifest_path = os.path.join(agent_dir, "agent_manifest.json")
        if not os.path.exists(manifest_path):
            return json.dumps({
                "status": "error",
                "error": f"Agent manifest not found: {manifest_path}"
            })
        
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        # Load topics
        topics = []
        topics_dir = os.path.join(agent_dir, "topics")
        if os.path.exists(topics_dir):
            for topic_file in os.listdir(topics_dir):
                if topic_file.endswith('.yaml'):
                    import yaml
                    with open(os.path.join(topics_dir, topic_file), 'r') as f:
                        topics.append(yaml.safe_load(f))
                elif topic_file.endswith('.json'):
                    with open(os.path.join(topics_dir, topic_file), 'r') as f:
                        topics.append(json.load(f))
        
        # Get deployment config
        config = self._load_deployment_config()
        
        # Override with kwargs
        environment_url = kwargs.get("environment_url") or config.get("environment_url") or os.environ.get("DATAVERSE_ENVIRONMENT_URL")
        tenant_id = kwargs.get("tenant_id") or config.get("tenant_id") or os.environ.get("AZURE_TENANT_ID")
        client_id = kwargs.get("client_id") or config.get("client_id") or os.environ.get("COPILOT_STUDIO_CLIENT_ID")
        
        if not environment_url:
            return json.dumps({
                "status": "error",
                "error": "environment_url is required",
                "suggestion": "Run configure_deployment first or set DATAVERSE_ENVIRONMENT_URL"
            })
        
        try:
            # Import and use CopilotStudioClient
            from utils.copilot_studio_api import CopilotStudioClient, CopilotStudioAPIError
            
            client = CopilotStudioClient(
                environment_url=environment_url,
                tenant_id=tenant_id,
                client_id=client_id,
                use_interactive_auth=True  # Will prompt for login if no secret
            )
            
            # Authenticate
            client.authenticate()
            
            # Deploy using the client's deploy method
            result = client.deploy_transpiled_agent(
                agent_manifest=manifest,
                topics=topics,
                flows=[]  # Power Automate flows handled separately
            )
            
            # Save deployment result
            deployment_record = {
                "agent_name": agent_name,
                "deployed_at": datetime.now().isoformat(),
                "environment_url": environment_url,
                "bot_id": result.get("bot_id"),
                "topic_ids": result.get("topic_ids", []),
                "status": result.get("status")
            }
            
            deployments_file = os.path.join(agent_dir, "deployment_history.json")
            history = []
            if os.path.exists(deployments_file):
                with open(deployments_file, 'r') as f:
                    history = json.load(f)
            history.append(deployment_record)
            with open(deployments_file, 'w') as f:
                json.dump(history, f, indent=2)
            
            return json.dumps({
                "status": "success",
                "message": f"Agent '{agent_name}' deployed to Copilot Studio",
                "deployment": deployment_record,
                "next_steps": [
                    f"Open Copilot Studio: {environment_url.replace('.crm.dynamics.com', '.powerva.microsoft.com')}",
                    f"Find your agent by name: {manifest.get('displayName', agent_name)}",
                    "Test the agent using the Test pane",
                    "Publish the agent when ready"
                ]
            }, indent=2)
            
        except ImportError as e:
            return json.dumps({
                "status": "error",
                "error": "CopilotStudioClient not available",
                "details": str(e),
                "suggestion": "Ensure utils/copilot_studio_api.py exists and dependencies are installed (requests, azure-identity or msal)"
            })
        except Exception as e:
            import traceback
            return json.dumps({
                "status": "error",
                "error": str(e),
                "traceback": traceback.format_exc(),
                "suggestion": "Check deployment configuration and ensure you have access to the Copilot Studio environment"
            })
    
    def _check_deployment_status(self, **kwargs) -> str:
        """
        Check the deployment status and history for an agent.
        """
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            # List all deployments
            all_deployments = []
            if os.path.exists(self.output_path):
                for agent_dir in os.listdir(self.output_path):
                    history_file = os.path.join(self.output_path, agent_dir, "deployment_history.json")
                    if os.path.exists(history_file):
                        with open(history_file, 'r') as f:
                            history = json.load(f)
                            if history:
                                all_deployments.append({
                                    "agent": agent_dir,
                                    "last_deployment": history[-1],
                                    "total_deployments": len(history)
                                })
            
            return json.dumps({
                "status": "success",
                "deployments": all_deployments,
                "total_agents_deployed": len(all_deployments)
            }, indent=2)
        
        # Get specific agent deployment history
        snake_name = self._to_snake_case(agent_name)
        history_file = os.path.join(self.output_path, snake_name, "deployment_history.json")
        
        if not os.path.exists(history_file):
            return json.dumps({
                "status": "info",
                "agent_name": agent_name,
                "message": "No deployments found for this agent",
                "suggestion": f"Run deploy action: action='deploy', agent_name='{agent_name}'"
            })
        
        with open(history_file, 'r') as f:
            history = json.load(f)
        
        return json.dumps({
            "status": "success",
            "agent_name": agent_name,
            "deployment_history": history,
            "last_deployment": history[-1] if history else None,
            "total_deployments": len(history)
        }, indent=2)
    
    # =========================================================================
    # SOLUTION-BASED DEPLOYMENT - Deploy multiple agents as a unified solution
    # =========================================================================
    
    def _get_solutions_file(self) -> str:
        """Get path to solutions definition file."""
        return os.path.join(self.base_path, "copilot_studio_solutions.json")
    
    def _load_solutions(self) -> Dict:
        """Load solution definitions."""
        solutions_file = self._get_solutions_file()
        if os.path.exists(solutions_file):
            with open(solutions_file, 'r') as f:
                return json.load(f)
        return {"solutions": {}}
    
    def _save_solutions(self, data: Dict) -> None:
        """Save solution definitions."""
        solutions_file = self._get_solutions_file()
        with open(solutions_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _create_solution_definition(self, **kwargs) -> str:
        """
        Create or update a solution definition that groups multiple agents.
        
        A solution is a logical grouping of agents that work together.
        This is similar to Power Platform solutions that contain multiple components.
        """
        solution_name = kwargs.get("solution_name")
        if not solution_name:
            return json.dumps({
                "status": "error",
                "error": "solution_name is required"
            })
        
        data = self._load_solutions()
        
        # Get existing or create new solution
        solution = data["solutions"].get(solution_name, {
            "name": solution_name,
            "display_name": kwargs.get("display_name", solution_name.replace("_", " ").title()),
            "description": kwargs.get("description", ""),
            "publisher": kwargs.get("publisher", "RAPP"),
            "version": kwargs.get("version", "1.0.0"),
            "agents": [],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        })
        
        # Update properties if provided
        if kwargs.get("display_name"):
            solution["display_name"] = kwargs["display_name"]
        if kwargs.get("description"):
            solution["description"] = kwargs["description"]
        if kwargs.get("publisher"):
            solution["publisher"] = kwargs["publisher"]
        if kwargs.get("version"):
            solution["version"] = kwargs["version"]
        
        # Add agents
        agents_to_add = kwargs.get("agents", [])
        if isinstance(agents_to_add, str):
            agents_to_add = [agents_to_add]
        
        for agent in agents_to_add:
            agent_snake = self._to_snake_case(agent)
            if agent_snake not in solution["agents"]:
                # Verify agent exists
                agent_dir = os.path.join(self.output_path, agent_snake)
                if os.path.exists(agent_dir):
                    solution["agents"].append(agent_snake)
                else:
                    logger.warning(f"Agent not found (not transpiled yet?): {agent_snake}")
        
        # Remove agents
        agents_to_remove = kwargs.get("remove_agents", [])
        if isinstance(agents_to_remove, str):
            agents_to_remove = [agents_to_remove]
        
        for agent in agents_to_remove:
            agent_snake = self._to_snake_case(agent)
            if agent_snake in solution["agents"]:
                solution["agents"].remove(agent_snake)
        
        solution["updated_at"] = datetime.now().isoformat()
        data["solutions"][solution_name] = solution
        self._save_solutions(data)
        
        return json.dumps({
            "status": "success",
            "message": f"Solution '{solution_name}' updated",
            "solution": solution,
            "next_steps": [
                f"Add more agents: action='create_solution', solution_name='{solution_name}', agents=['agent_name']",
                f"Deploy solution: action='deploy_solution', solution_name='{solution_name}'",
                f"View all solutions: action='list_solutions'"
            ]
        }, indent=2)
    
    def _list_solutions(self, **kwargs) -> str:
        """List all defined solutions and their agents."""
        data = self._load_solutions()
        
        solution_name = kwargs.get("solution_name")
        if solution_name:
            # Return specific solution details
            solution = data["solutions"].get(solution_name)
            if not solution:
                return json.dumps({
                    "status": "error",
                    "error": f"Solution not found: {solution_name}"
                })
            
            # Enrich with agent details
            agent_details = []
            for agent_name in solution["agents"]:
                agent_dir = os.path.join(self.output_path, agent_name)
                manifest_path = os.path.join(agent_dir, "agent_manifest.json")
                if os.path.exists(manifest_path):
                    with open(manifest_path, 'r') as f:
                        manifest = json.load(f)
                    agent_details.append({
                        "name": agent_name,
                        "display_name": manifest.get("displayName", agent_name),
                        "description": manifest.get("description", "")[:100] + "..."
                    })
                else:
                    agent_details.append({
                        "name": agent_name,
                        "status": "not transpiled"
                    })
            
            return json.dumps({
                "status": "success",
                "solution": solution,
                "agent_details": agent_details
            }, indent=2)
        
        # List all solutions
        solutions_summary = []
        for name, sol in data["solutions"].items():
            solutions_summary.append({
                "name": name,
                "display_name": sol.get("display_name", name),
                "agent_count": len(sol.get("agents", [])),
                "version": sol.get("version", "1.0.0"),
                "updated_at": sol.get("updated_at")
            })
        
        return json.dumps({
            "status": "success",
            "solutions": solutions_summary,
            "total_solutions": len(solutions_summary)
        }, indent=2)
    
    def _deploy_solution(self, **kwargs) -> str:
        """
        Deploy a complete solution with all its agents to Copilot Studio.
        
        This creates all agents in the solution as a cohesive set in Copilot Studio.
        Each agent is created with proper metadata linking it to the solution.
        
        Prerequisites:
        - Solution must be defined (action='create_solution')
        - All agents in the solution must be transpiled
        - Deployment must be configured (action='configure_deployment')
        """
        solution_name = kwargs.get("solution_name")
        if not solution_name:
            # Check for predefined solution patterns
            if kwargs.get("predefined") == "contoso":
                return self._deploy_contoso_solution(**kwargs)
            
            return json.dumps({
                "status": "error",
                "error": "solution_name is required",
                "alternatives": {
                    "predefined_solutions": [
                        "Use predefined='contoso' for Contoso CI solution"
                    ],
                    "create_custom": "Use action='create_solution' first"
                }
            })
        
        data = self._load_solutions()
        solution = data["solutions"].get(solution_name)
        
        if not solution:
            return json.dumps({
                "status": "error",
                "error": f"Solution not found: {solution_name}",
                "suggestion": "Use action='create_solution' to define a solution first"
            })
        
        if not solution.get("agents"):
            return json.dumps({
                "status": "error",
                "error": f"Solution '{solution_name}' has no agents",
                "suggestion": "Add agents: action='create_solution', solution_name='...', agents=[...]"
            })
        
        # Get deployment config
        config = self._load_deployment_config()
        environment_url = kwargs.get("environment_url") or config.get("environment_url")
        tenant_id = kwargs.get("tenant_id") or config.get("tenant_id")
        client_id = kwargs.get("client_id") or config.get("client_id")
        
        if not environment_url:
            return json.dumps({
                "status": "error",
                "error": "Deployment not configured",
                "suggestion": "Run action='configure_deployment' first"
            })
        
        # Deploy all agents in the solution
        deployment_results = {
            "status": "success",
            "solution_name": solution_name,
            "environment_url": environment_url,
            "deployed_at": datetime.now().isoformat(),
            "agents_deployed": [],
            "agents_failed": [],
            "errors": []
        }
        
        try:
            from utils.copilot_studio_api import CopilotStudioClient, CopilotStudioAPIError
            
            client = CopilotStudioClient(
                environment_url=environment_url,
                tenant_id=tenant_id,
                client_id=client_id,
                use_interactive_auth=True
            )
            
            # Authenticate once for all deployments
            logger.info("Authenticating to Copilot Studio...")
            client.authenticate()
            logger.info("Authentication successful")
            
            # Deploy each agent
            for agent_name in solution["agents"]:
                try:
                    agent_dir = os.path.join(self.output_path, agent_name)
                    manifest_path = os.path.join(agent_dir, "agent_manifest.json")
                    
                    if not os.path.exists(manifest_path):
                        deployment_results["agents_failed"].append({
                            "agent": agent_name,
                            "error": "Not transpiled"
                        })
                        continue
                    
                    with open(manifest_path, 'r') as f:
                        manifest = json.load(f)
                    
                    # Create short display name (max 42 chars for Copilot Studio)
                    # Use abbreviations for solution prefix
                    solution_prefix = kwargs.get("name_prefix", "ZE")  # ZE = Contoso
                    base_name = manifest.get('displayName', agent_name)
                    # Shorten common words
                    base_name = base_name.replace("Competitive Intelligence", "CI")
                    base_name = base_name.replace("Orchestrator", "Orch")
                    base_name = base_name.replace("Synthesizer", "Synth")
                    base_name = base_name.replace("Agent", "")
                    base_name = base_name.replace("Contoso ", "")
                    base_name = base_name.strip()
                    
                    display_name = f"{solution_prefix} {base_name}"[:42]
                    description = f"Part of {solution['display_name']} solution (v{solution['version']}). {manifest.get('description', '')}"
                    
                    # CRITICAL: Get instructions from manifest for GPT component
                    # This is what makes the agent actually work in Copilot Studio!
                    instructions = manifest.get("instructions") or manifest.get("systemPrompt", "")
                    if not instructions:
                        # Try to load from instructions.md file
                        instructions_path = os.path.join(agent_dir, "instructions.md")
                        if os.path.exists(instructions_path):
                            with open(instructions_path, 'r', encoding='utf-8') as f:
                                instructions = f.read()
                    
                    if not instructions:
                        # Fallback to description
                        instructions = f"You are {display_name}. {description}"
                    
                    logger.info(f"Agent instructions length: {len(instructions)} chars")
                    
                    # Load topics
                    topics = []
                    topics_dir = os.path.join(agent_dir, "topics")
                    if os.path.exists(topics_dir):
                        for topic_file in os.listdir(topics_dir):
                            topic_path = os.path.join(topics_dir, topic_file)
                            if topic_file.endswith('.yaml'):
                                import yaml
                                with open(topic_path, 'r') as f:
                                    topics.append(yaml.safe_load(f))
                            elif topic_file.endswith('.json'):
                                with open(topic_path, 'r') as f:
                                    topics.append(json.load(f))
                    
                    # Create the agent WITH instructions (GPT component created automatically!)
                    logger.info(f"Creating agent: {display_name}")
                    bot_id = client.create_agent(
                        name=display_name,
                        description=description[:500],  # Truncate if too long
                        instructions=instructions,  # CRITICAL: Pass instructions for GPT component
                        language=manifest.get("primaryLanguage", "en-us")
                    )
                    
                    # Create topics for the agent
                    topic_ids = []
                    for topic in topics:
                        try:
                            trigger_phrases = []
                            if "triggers" in topic:
                                for trigger in topic.get("triggers", []):
                                    trigger_phrases.extend(trigger.get("triggerQueries", []))
                            
                            topic_id = client.create_topic(
                                bot_id=bot_id,
                                name=topic.get("displayName", topic.get("name", "Unknown")),
                                trigger_phrases=trigger_phrases,
                                description=topic.get("description", "")
                            )
                            topic_ids.append(topic_id)
                        except Exception as topic_error:
                            logger.warning(f"Failed to create topic: {topic_error}")
                    
                    deployment_results["agents_deployed"].append({
                        "agent": agent_name,
                        "bot_id": bot_id,
                        "display_name": display_name,
                        "topics_created": len(topic_ids),
                        "has_instructions": bool(instructions)
                    })
                    logger.info(f"Successfully deployed: {agent_name} ({bot_id}) with GPT instructions")
                    
                except Exception as agent_error:
                    deployment_results["agents_failed"].append({
                        "agent": agent_name,
                        "error": str(agent_error)
                    })
                    deployment_results["errors"].append(f"{agent_name}: {str(agent_error)}")
                    logger.error(f"Failed to deploy {agent_name}: {agent_error}")
            
            # Update solution with deployment info
            if "deployments" not in solution:
                solution["deployments"] = []
            solution["deployments"].append({
                "environment_url": environment_url,
                "deployed_at": deployment_results["deployed_at"],
                "agents_deployed": len(deployment_results["agents_deployed"]),
                "agents_failed": len(deployment_results["agents_failed"])
            })
            data["solutions"][solution_name] = solution
            self._save_solutions(data)
            
            # Set overall status
            if deployment_results["agents_failed"]:
                if deployment_results["agents_deployed"]:
                    deployment_results["status"] = "partial"
                else:
                    deployment_results["status"] = "failed"
            
            # Add next steps
            copilot_studio_url = environment_url.replace('.crm.dynamics.com', '.powervirtualagents.com')
            deployment_results["next_steps"] = [
                f"Open Copilot Studio: {copilot_studio_url}",
                f"Find agents by searching for: [{solution['display_name']}]",
                "Configure connectors and test each agent",
                "Publish agents when ready"
            ]
            
        except ImportError as e:
            deployment_results["status"] = "error"
            deployment_results["errors"].append(f"Missing dependency: {str(e)}")
        except Exception as e:
            deployment_results["status"] = "error"
            deployment_results["errors"].append(str(e))
            import traceback
            deployment_results["traceback"] = traceback.format_exc()
        
        return json.dumps(deployment_results, indent=2)
    
    def _deploy_contoso_solution(self, **kwargs) -> str:
        """
        Deploy the predefined Contoso Competitive Intelligence solution.
        
        This is a convenience method for the complete Contoso CI system:
        - 1 Orchestrator agent (coordinates all BU agents)
        - 5 Business Unit agents (Drains, Drinking Water, Sinks, Commercial Brass, Wilkins)
        - 1 Cross-BU Synthesizer agent (aggregates insights)
        """
        # Define the Contoso solution
        contoso_agents = [
            "contoso_ci_orchestrator_agent",
            "contoso_drains_ci_agent",
            "contoso_drinking_water_ci_agent",
            "contoso_sinks_ci_agent",
            "contoso_commercial_brass_ci_agent",
            "contoso_wilkins_ci_agent",
            "contoso_crossbu_synthesizer_agent"
        ]
        
        # First, create/update the solution definition
        solution_result = json.loads(self._create_solution_definition(
            solution_name="contoso_competitive_intelligence",
            display_name="Contoso Competitive Intelligence",
            description="Multi-agent competitive intelligence system for Contoso with orchestrated BU-specific agents and cross-BU synthesis capabilities.",
            publisher="RAPP",
            version=kwargs.get("version", "1.0.0"),
            agents=contoso_agents
        ))
        
        if solution_result.get("status") != "success":
            return json.dumps(solution_result)
        
        # Check which agents are transpiled
        missing_agents = []
        for agent in contoso_agents:
            agent_dir = os.path.join(self.output_path, agent)
            if not os.path.exists(agent_dir):
                missing_agents.append(agent)
        
        if missing_agents:
            return json.dumps({
                "status": "info",
                "message": "Some agents need to be transpiled first",
                "missing_agents": missing_agents,
                "transpiled_agents": [a for a in contoso_agents if a not in missing_agents],
                "next_steps": [
                    "Run batch_transpile for missing agents:",
                    f"action='batch_transpile', agent_list={missing_agents}",
                    "Then run: action='deploy_solution', predefined='contoso'"
                ]
            }, indent=2)
        
        # Deploy the solution
        return self._deploy_solution(solution_name="contoso_competitive_intelligence", **kwargs)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
