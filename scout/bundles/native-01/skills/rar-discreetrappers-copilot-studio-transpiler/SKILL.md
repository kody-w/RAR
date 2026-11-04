---
name: "rar-discreetrappers-copilot-studio-transpiler"
description: "Converts RAPP Python agents to fully native Copilot Studio solutions without Function App dependency."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/copilot_studio_transpiler_agent", "rar_sha256": "ee87bb1000f7f33a408097d912f3cd41946d0feb5ce40e7abe37f1938c8acefb", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "Bill Whalen", "tags": ["pipeline", "transpiler", "copilot-studio", "native", "no-code"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/copilot_studio_transpiler_agent`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_transpiler_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_transpiler_agent.py` and embedded as the fenced Python below (sha256 ee87bb1000f7f33a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_transpiler_agent.py` first:

```bash
python3 copilot_studio_transpiler_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_transpiler_agent.py   # or on stdin
python3 copilot_studio_transpiler_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/copilot_studio_transpiler_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_studio_transpiler_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/copilot_studio_transpiler_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
