---
name: "rar-discreetrappers-copilot-studio-transpiler"
description: "Converts RAPP Python agents to fully native Copilot Studio solutions without Function App dependency."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/copilot_studio_transpiler_agent", "rar_sha256": "ee87bb1000f7f33a408097d912f3cd41946d0feb5ce40e7abe37f1938c8acefb", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "Bill Whalen", "tags": ["pipeline", "transpiler", "copilot-studio", "native", "no-code"]}
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
