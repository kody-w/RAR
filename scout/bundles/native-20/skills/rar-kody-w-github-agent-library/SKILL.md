---
name: "rar-kody-w-github-agent-library"
description: "Comprehensive manager for the GitHub Agent Template Library at kody-w/AI-Agent-Templates. Discovers, searches, installs, and manages 65+ pre-built agents from the public repository. Also creates GUID-based agent groups for custom deployments. All agents are downloaded from GitHub raw URLs and automatically integrated into your system."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/github_agent_library_agent", "rar_sha256": "7d25b2d553356cfcb2f74921552b984d8e348ab56f20984fcda831eb65336923", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["core", "package-manager", "install", "discovery"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/github_agent_library_agent`. The original RAPP
agent is preserved byte-for-byte in `github_agent_library_agent.py` and in the RCI capsule.

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

Comprehensive manager for the GitHub Agent Template Library at kody-w/AI-Agent-Templates. Discovers, searches, installs, and manages 65+ pre-built agents from the public repository. Also creates GUID-based agent groups for custom deployments. All agents are downloaded from GitHub raw URLs and automatically integrated into your system.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Action to perform: 'discover' (browse ALL 65+ available agents with no parameters needed), 'search' (find specific agents - REQUIRES search_query parameter with keyword like 'email' or 'sales'), 'install' (download and install an agent - REQUIRES agent_id from search/discover results, NEVER guess the agent_id), 'list_installed' (show installed GitHub agents - no parameters), 'update' (update an agent - REQUIRES agent_id), 'remove' (uninstall agent - REQUIRES agent_id), 'get_info' (detailed agent info - REQUIRES agent_id), 'sync_manifest' (refresh catalogue from GitHub - no parameters), 'create_group' (create a GUID-based agent group - REQUIRES agent_ids list), 'list_groups' (show all GUID-based agent groups - no parameters), 'get_group_info' (get details about a specific GUID group - REQUIRES guid parameter). CRITICAL: Before calling 'install', you MUST call 'search' or 'discover' first to get the exact agent_id.",
      "enum": [
        "discover",
        "search",
        "install",
        "list_installed",
        "update",
        "remove",
        "get_info",
        "sync_manifest",
        "create_group",
        "list_groups",
        "get_group_info"
      ],
      "type": "string"
    },
    "agent_id": {
      "description": "REQUIRED for install/update/remove/get_info actions. The unique identifier of the agent (e.g., 'deal_progression_agent', 'email_agent'). CRITICAL: Get this EXACT value from discover or search results first. Do NOT guess or make up agent IDs - they must come from the GitHub library. If you don't have the exact agent_id from a prior search/discover, you MUST search first before attempting to install.",
      "type": "string"
    },
    "agent_ids": {
      "description": "REQUIRED for create_group action: List of agent IDs to fetch from GitHub and group together. Example: ['deal_progression_agent', 'email_agent', 'sales_forecast_agent']. These must be valid agent IDs from the kody-w/AI-Agent-Templates repository.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "category": {
      "description": "OPTIONAL: Additional filter to narrow results by industry vertical. Only use if user specifically mentions an industry. Available industries: b2b_sales, b2c_sales, energy, federal_government, financial_services, general, healthcare, manufacturing, professional_services, retail_cpg, slg_government, software_dp",
      "enum": [
        "b2b_sales",
        "b2c_sales",
        "energy",
        "federal_government",
        "financial_services",
        "general",
        "healthcare",
        "manufacturing",
        "professional_services",
        "retail_cpg",
        "slg_government",
        "software_dp"
      ],
      "type": "string"
    },
    "force": {
      "description": "OPTIONAL: Set to true to reinstall an agent even if it already exists. Default is false. Use when updating/fixing an installed agent.",
      "type": "boolean"
    },
    "group_name": {
      "description": "OPTIONAL for create_group action: A friendly name for the agent group (e.g., 'Sales Team Agents'). This is stored with the GUID for reference.",
      "type": "string"
    },
    "guid": {
      "description": "REQUIRED for get_group_info action: The GUID of the agent group to retrieve information about.",
      "type": "string"
    },
    "search_query": {
      "description": "REQUIRED for search action: Keyword to search for in agent names, descriptions, and features. Examples: 'email', 'sales', 'manufacturing', 'automation'. Use broad terms for better results.",
      "type": "string"
    },
    "stack_path": {
      "description": "OPTIONAL: Only needed when installing a stack agent. Path format: 'industry_stacks/stack_name' (e.g., 'b2b_sales_stacks/deal_progression_stack'). This is provided in search results for stack agents. Leave empty for singular agents.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `github_agent_library_agent.py` and embedded as the fenced Python below (sha256 7d25b2d553356cfc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `github_agent_library_agent.py` first:

```bash
python3 github_agent_library_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 github_agent_library_agent.py   # or on stdin
python3 github_agent_library_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
from agents.basic_agent import BasicAgent

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/github_agent_library_agent",
    "version": "1.0.1",
    "display_name": "GitHubAgentLibrary",
    "description": "Browses, searches, and installs agents from the kody-w/AI-Agent-Templates GitHub repo into local agent storage.",
    "author": "Kody Wildfeuer",
    "tags": ["core", "package-manager", "install", "discovery"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

from utils.storage_factory import get_storage_manager
import logging
import requests
import json
import re
import uuid
from datetime import datetime

class GitHubAgentLibraryManager(BasicAgent):
    """
    Comprehensive GitHub Agent Library Manager.
    Manages integration with the GitHub Agent Template Library at kody-w/AI-Agent-Templates.
    Handles both individual agent operations (discover, search, install) and GUID-based agent groups.
    """
    
    # GitHub repository configuration
    GITHUB_REPO = "kody-w/AI-Agent-Templates"
    GITHUB_BRANCH = "main"
    GITHUB_RAW_BASE = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{GITHUB_BRANCH}"
    GITHUB_API_BASE = f"https://api.github.com/repos/{GITHUB_REPO}"
    
    def __init__(self):
        self.name = 'GitHubAgentLibrary'
        self.metadata = {
            "name": self.name,
            "description": "Comprehensive manager for the GitHub Agent Template Library at kody-w/AI-Agent-Templates. Discovers, searches, installs, and manages 65+ pre-built agents from the public repository. Also creates GUID-based agent groups for custom deployments. All agents are downloaded from GitHub raw URLs and automatically integrated into your system.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "description": "Action to perform: 'discover' (browse ALL 65+ available agents with no parameters needed), 'search' (find specific agents - REQUIRES search_query parameter with keyword like 'email' or 'sales'), 'install' (download and install an agent - REQUIRES agent_id from search/discover results, NEVER guess the agent_id), 'list_installed' (show installed GitHub agents - no parameters), 'update' (update an agent - REQUIRES agent_id), 'remove' (uninstall agent - REQUIRES agent_id), 'get_info' (detailed agent info - REQUIRES agent_id), 'sync_manifest' (refresh catalogue from GitHub - no parameters), 'create_group' (create a GUID-based agent group - REQUIRES agent_ids list), 'list_groups' (show all GUID-based agent groups - no parameters), 'get_group_info' (get details about a specific GUID group - REQUIRES guid parameter). CRITICAL: Before calling 'install', you MUST call 'search' or 'discover' first to get the exact agent_id.",
                        "enum": ["discover", "search", "install", "list_installed", "update", "remove", "get_info", "sync_manifest", "create_group", "list_groups", "get_group_info"]
                    },
                    "agent_id": {
                        "type": "string",
                        "description": "REQUIRED for install/update/remove/get_info actions. The unique identifier of the agent (e.g., 'deal_progression_agent', 'email_agent'). CRITICAL: Get this EXACT value from discover or search results first. Do NOT guess or make up agent IDs - they must come from the GitHub library. If you don't have the exact agent_id from a prior search/discover, you MUST search first before attempting to install."
                    },
                    "agent_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "REQUIRED for create_group action: List of agent IDs to fetch from GitHub and group together. Example: ['deal_progression_agent', 'email_agent', 'sales_forecast_agent']. These must be valid agent IDs from the kody-w/AI-Agent-Templates repository."
                    },
                    "group_name": {
                        "type": "string",
                        "description": "OPTIONAL for create_group action: A friendly name for the agent group (e.g., 'Sales Team Agents'). This is stored with the GUID for reference."
                    },
                    "guid": {
                        "type": "string",
                        "description": "REQUIRED for get_group_info action: The GUID of the agent group to retrieve information about."
                    },
                    "stack_path": {
                        "type": "string",
                        "description": "OPTIONAL: Only needed when installing a stack agent. Path format: 'industry_stacks/stack_name' (e.g., 'b2b_sales_stacks/deal_progression_stack'). This is provided in search results for stack agents. Leave empty for singular agents."
                    },
                    "search_query": {
                        "type": "string",
                        "description": "REQUIRED for search action: Keyword to search for in agent names, descriptions, and features. Examples: 'email', 'sales', 'manufacturing', 'automation'. Use broad terms for better results."
                    },
                    "category": {
                        "type": "string",
                        "description": "OPTIONAL: Additional filter to narrow results by industry vertical. Only use if user specifically mentions an industry. Available industries: b2b_sales, b2c_sales, energy, federal_government, financial_services, general, healthcare, manufacturing, professional_services, retail_cpg, slg_government, software_dp",
                        "enum": ["b2b_sales", "b2c_sales", "energy", "federal_government", 
                                "financial_services", "general", "healthcare", "manufacturing",
                                "professional_services", "retail_cpg", "slg_government", "software_dp"]
                    },
                    "force": {
                        "type": "boolean",
                        "description": "OPTIONAL: Set to true to reinstall an agent even if it already exists. Default is false. Use when updating/fixing an installed agent."
                    }
                },
                "required": ["action"]
            },
            "examples": {
                "discover_all": {
                    "description": "Browse all available agents in the library",
                    "parameters": {"action": "discover"}
                },
                "search_by_keyword": {
                    "description": "Find agents related to email",
                    "parameters": {"action": "search", "search_query": "email"}
                },
                "search_by_industry": {
                    "description": "Find manufacturing agents",
                    "parameters": {"action": "search", "search_query": "manufacturing", "category": "manufacturing"}
                },
                "search_before_install_workflow": {
                    "description": "CORRECT WORKFLOW: First search for 'maintenance' agents, then use the agent_id from results to install",
                    "steps": [
                        {"step": 1, "action": "search", "parameters": {"action": "search", "search_query": "maintenance"}},
                        {"step": 2, "action": "install", "parameters": {"action": "install", "agent_id": "asset_maintenance_forecast_agent"}, "note": "Use exact agent_id from step 1 results"}
                    ]
                },
                "install_agent": {
                    "description": "Install agent AFTER getting exact agent_id from search",
                    "parameters": {"action": "install", "agent_id": "deal_progression_agent"}
                },
                "get_agent_details": {
                    "description": "Get detailed information about an agent",
                    "parameters": {"action": "get_info", "agent_id": "email_agent"}
                },
                "list_installed": {
                    "description": "Show all installed GitHub agents",
                    "parameters": {"action": "list_installed"}
                },
                "create_agent_group": {
                    "description": "Create a GUID-based group of agents for custom deployment",
                    "parameters": {
                        "action": "create_group",
                        "agent_ids": ["deal_progression_agent", "email_agent", "sales_forecast_agent"],
                        "group_name": "Sales Team Agents"
                    }
                },
                "list_groups": {
                    "description": "Show all created GUID-based agent groups",
                    "parameters": {"action": "list_groups"}
                },
                "get_group_details": {
                    "description": "Get detailed information about a specific agent group",
                    "parameters": {"action": "get_group_info", "guid": "550e8400-e29b-41d4-a716-446655440000"}
                }
            }
        }
        self.storage_manager = get_storage_manager()
        super().__init__(name=self.name, metadata=self.metadata)
        
        # Cache for manifest
        self._manifest_cache = None
        self._manifest_last_fetch = None
    
    def perform(self, **kwargs):
        action = kwargs.get('action')
        
        try:
            if action == 'discover':
                return self._discover_agents(kwargs)
            elif action == 'search':
                return self._search_agents(kwargs)
            elif action == 'install':
                return self._install_agent(kwargs)
            elif action == 'list_installed':
                return self._list_installed_agents()
            elif action == 'update':
                return self._update_agent(kwargs)
            elif action == 'remove':
                return self._remove_agent(kwargs)
            elif action == 'get_info':
                return self._get_agent_info(kwargs)
            elif action == 'sync_manifest':
                return self._sync_manifest()
            elif action == 'create_group':
                return self._create_agent_group(kwargs)
            elif action == 'list_groups':
                return self._list_agent_groups()
            elif action == 'get_group_info':
                return self._get_group_info(kwargs)
            else:
                return f"Error: Unknown action '{action}'"
        except Exception as e:
            logging.error(f"Error in GitHubAgentLibrary: {str(e)}")
            return f"Error: {str(e)}"
    
    def _fetch_manifest(self, force_refresh=False):
        """Fetch the manifest.json from GitHub"""
        # Check cache (refresh every 5 minutes)
        if not force_refresh and self._manifest_cache and self._manifest_last_fetch:
            if (datetime.now() - self._manifest_last_fetch).seconds < 300:
                return self._manifest_cache
        
        try:
            manifest_url = f"{self.GITHUB_RAW_BASE}/manifest.json"
            response = requests.get(manifest_url, timeout=10)
            response.raise_for_status()
            
            manifest = response.json()
            self._manifest_cache = manifest
            self._manifest_last_fetch = datetime.now()
            
            return manifest
        except Exception as e:
            logging.error(f"Error fetching manifest: {str(e)}")
            return None
    
    def _discover_agents(self, params):
        """Discover all available agents in the GitHub library"""
        manifest = self._fetch_manifest()
        
        if not manifest:
            return "Error: Unable to fetch agent library manifest"
        
        category = params.get('category')
        
        # Get singular agents
        singular_agents = manifest.get('agents', [])
        
        # Get stack agents
        stacks = manifest.get('stacks', [])
        
        # Filter by category if provided
        if category:
            category_key = f"{category}_stacks"
            stacks = [s for s in stacks if s.get('path', '').startswith(category_key)]
        
        # Count total agents
        total_singular = len(singular_agents)
        total_stack_agents = sum(len(stack.get('agents', [])) for stack in stacks)
        
        response = f"🔍 GitHub Agent Library Discovery\n\n"
        response += f"**Repository:** {self.GITHUB_REPO}\n"
        response += f"**Total Agents Available:** {total_singular + total_stack_agents}\n"
        response += f"  • Singular Agents: {total_singular}\n"
        response += f"  • Stack Agents: {total_stack_agents}\n\n"
        
        # Show singular agents
        if singular_agents:
            response += f"## 📦 Singular Agents ({len(singular_agents)})\n\n"
            for i, agent in enumerate(singular_agents[:10], 1):  # Show first 10
                response += f"{i}. **{agent['name']}** ({agent['id']})\n"
                response += f"   {agent.get('icon', '🤖')} {agent.get('description', 'No description')[:100]}\n"
                response += f"   Install: `agent_id='{agent['id']}'`\n\n"
            
            if len(singular_agents) > 10:
                response += f"   ... and {len(singular_agents) - 10} more singular agents\n\n"
        
        # Show stack agents by industry
        if stacks:
            response += f"## 🏢 Agent Stacks ({len(stacks)} stacks)\n\n"
            for stack in stacks[:5]:  # Show first 5 stacks
                response += f"### {stack['name']}\n"
                response += f"**Industry:** {stack.get('industry', 'General')}\n"
                response += f"**Path:** {stack.get('path', 'N/A')}\n"
                response += f"**Agents in Stack:** {len(stack.get('agents', []))}\n\n"
                
                for agent in stack.get('agents', [])[:3]:  # Show first 3 agents per stack
                    response += f"  • **{agent['name']}** ({agent['id']})\n"
                    response += f"    {agent.get('description', 'No description')[:80]}\n"
                    response += f"    Install: `agent_id='{agent['id']}', stack_path='{stack.get('path', '')}'`\n\n"
                
                if len(stack.get('agents', [])) > 3:
                    response += f"    ... and {len(stack.get('agents', [])) - 3} more agents in this stack\n\n"
            
            if len(stacks) > 5:
                response += f"... and {len(stacks) - 5} more stacks\n\n"
        
        response += f"\n💡 **Tips:**\n"
        response += f"• Use `action='search', search_query='keyword'` to find specific agents\n"
        response += f"• Use `action='install', agent_id='exact_id'` to install an agent\n"
        response += f"• Use `action='create_group', agent_ids=['id1', 'id2']` to create a GUID-based group\n"
        
        return response
    
    def _search_agents(self, params):
        """Search for agents by keyword"""
        search_query = params.get('search_query', '').lower()
        category = params.get('category')
        
        if not search_query:
            return "Error: search_query is required for search action"
        
        manifest = self._fetch_manifest()
        if not manifest:
            return "Error: Unable to fetch agent library manifest"
        
        results = []
        
        # Search singular agents
        for agent in manifest.get('agents', []):
            if self._matches_search(agent, search_query):
                results.append({
                    'agent': agent,
                    'type': 'singular',
                    'relevance': self._calculate_relevance(agent, search_query)
                })
        
        # Search stack agents
        for stack in manifest.get('stacks', []):
            # Filter by category if provided
            if category:
                category_key = f"{category}_stacks"
                if not stack.get('path', '').startswith(category_key):
                    continue
            
            for agent in stack.get('agents', []):
                if self._matches_search(agent, search_query):
                    results.append({
                        'agent': agent,
                        'type': 'stack',
                        'stack_name': stack['name'],
                        'stack_path': stack.get('path', ''),
                        'stack_industry': stack.get('industry', 'General'),
                        'relevance': self._calculate_relevance(agent, search_query)
                    })
        
        # Sort by relevance
        results.sort(key=lambda x: x['relevance'], reverse=True)
        
        if not results:
            response = f"❌ No agents found matching '{search_query}'\n\n"
            response += f"💡 Try:\n"
            response += f"• Using broader search terms\n"
            response += f"• Using `action='discover'` to browse all agents\n"
            response += f"• Checking the repository directly: {self.GITHUB_REPO}\n"
            return response
        
        response = f"🔍 Search Results for '{search_query}' ({len(results)} found)\n\n"
        
        for i, result in enumerate(results[:15], 1):  # Show top 15 results
            agent = result['agent']
            response += f"{i}. **{agent['name']}**\n"
            response += f"   • ID: `{agent['id']}`\n"
            response += f"   • Type: {result['type']}\n"
            
            if result['type'] == 'stack':
                response += f"   • Stack: {result['stack_name']} ({result['stack_industry']})\n"
                response += f"   • Stack Path: `{result['stack_path']}`\n"
            
            response += f"   • Description: {agent.get('description', 'No description')[:120]}\n"
            response += f"   • Size: {agent.get('size_formatted', 'Unknown')}\n"
            
            if agent.get('features'):
                response += f"   • Features: {', '.join(agent['features'][:3])}\n"
            
            response += f"\n   **Install Command:**\n"
            response += f"   `action='install', agent_id='{agent['id']}'"
            if result['type'] == 'stack':
                response += f", stack_path='{result['stack_path']}'"
            response += f"`\n\n"
        
        if len(results) > 15:
            response += f"... and {len(results) - 15} more results. Refine your search for more specific results.\n"
        
        return response
    
    def _matches_search(self, agent, search_query):
        """Check if agent matches search query"""
        searchable_text = f"{agent.get('name', '')} {agent.get('id', '')} {agent.get('description', '')} {' '.join(agent.get('features', []))}"
        return search_query in searchable_text.lower()
    
    def _calculate_relevance(self, agent, search_query):
        """Calculate relevance score for search results"""
        score = 0
        
        # Name match (highest priority)
        if search_query in agent.get('name', '').lower():
            score += 10
        
        # ID match
        if search_query in agent.get('id', '').lower():
            score += 8
        
        # Description match
        if search_query in agent.get('description', '').lower():
            score += 5
        
        # Features match
        for feature in agent.get('features', []):
            if search_query in feature.lower():
                score += 3
        
        return score
    
    def _install_agent(self, params):
        """Install an agent from GitHub"""
        agent_id = params.get('agent_id')
        stack_path = params.get('stack_path')
        force = params.get('force', False)
        
        if not agent_id:
            return "Error: agent_id is required"
        
        # Fetch manifest
        manifest = self._fetch_manifest()
        if not manifest:
            return "Error: Unable to fetch agent library manifest"
        
        # Find agent in manifest
        agent_info = None
        source_type = 'singular'
        
        # Check singular agents
        for agent in manifest.get('agents', []):
            if agent['id'] == agent_id:
                agent_info = agent
                break
        
        # Check stack agents
        if not agent_info:
            for stack in manifest.get('stacks', []):
                for agent in stack.get('agents', []):
                    if agent['id'] == agent_id:
                        agent_info = agent
                        source_type = 'stack'
                        agent_info['stack_info'] = {
                            'name': stack['name'],
                            'path': stack.get('path', ''),
                            'industry': stack.get('industry', 'General')
                        }
                        break
                if agent_info:
                    break
        
        if not agent_info:
            # Provide helpful error with search suggestion
            search_term = agent_id.replace('_agent', '').replace('_', ' ')
            return f"""Error: Agent '{agent_id}' not found in GitHub library.

❌ The agent_id you provided doesn't exist in the repository.

💡 **What to do:**
1. Use `action='search', search_query='{search_term}'` to find the correct agent_id
2. Use `action='discover'` to browse all available agents
3. Make sure you're using the exact agent_id from search results

⚠️ **Important:** Never guess or make up agent IDs. Always get them from search/discover results first."""
        
        # Check if already installed (unless force=True)
        if not force:
            log_data = self.storage_manager.read_file('agent_catalogue', 'installation_log.json')
            if log_data:
                installations = json.loads(log_data)
                if any(a['agent_id'] == agent_id for a in installations.get('installations', [])):
                    return f"""⚠️ Agent '{agent_info['name']}' is already installed.

**Options:**
1. Use `action='update', agent_id='{agent_id}'` to reinstall/update
2. Use `force=True` to force reinstall
3. Use `action='list_installed'` to see all installed agents"""
        
        # Download agent code
        try:
            response = requests.get(agent_info['url'], timeout=10)
            response.raise_for_status()
            agent_code = response.text
        except Exception as e:
            logging.error(f"Error fetching agent {agent_id}: {str(e)}")
            return f"Error: Failed to download agent from GitHub: {str(e)}"
        
        # Store in Azure File Storage
        try:
            success = self.storage_manager.write_file('agents', agent_info['filename'], agent_code)
            if not success:
                return "Error: Failed to write agent to Azure storage"
        except Exception as e:
            logging.error(f"Error storing agent {agent_id}: {str(e)}")
            return f"Error: Failed to save agent to storage: {str(e)}"
        
        # Update installation log
        try:
            log_data = self.storage_manager.read_file('agent_catalogue', 'installation_log.json')
            
            if log_data:
                installations = json.loads(log_data)
            else:
                installations = {'installations': []}
            
            # Remove old entry if exists (for updates)
            installations['installations'] = [
                a for a in installations['installations'] if a['agent_id'] != agent_id
            ]
            
            # Add new entry
            installation_record = {
                'agent_id': agent_id,
                'agent_name': agent_info['name'],
                'filename': agent_info['filename'],
                'installed_at': datetime.now().isoformat(),
                'source': 'github_library',
                'type': source_type,
                'size': agent_info.get('size_formatted', 'Unknown'),
                'github_url': agent_info['url']
            }
            
            if source_type == 'stack' and agent_info.get('stack_info'):
                installation_record['stack'] = agent_info['stack_info']
            
            installations['installations'].append(installation_record)
            
            self.storage_manager.write_file(
                'agent_catalogue',
                'installation_log.json',
                json.dumps(installations, indent=2)
            )
        except Exception as e:
            logging.error(f"Error updating installation log: {str(e)}")
            # Don't fail the installation if logging fails
        
        # Format success response
        response = f"✅ Successfully installed: **{agent_info['name']}**\n\n"
        response += f"**Details:**\n"
        response += f"• ID: {agent_id}\n"
        response += f"• Filename: {agent_info['filename']}\n"
        response += f"• Type: {source_type}\n"
        response += f"• Size: {agent_info.get('size_formatted', 'Unknown')}\n"
        
        if source_type == 'stack' and agent_info.get('stack_info'):
            response += f"• Stack: {agent_info['stack_info']['name']}\n"
            response += f"• Industry: {agent_info['stack_info']['industry']}\n"
        
        response += f"\n**Features:**\n"
        for feature in agent_info.get('features', [])[:5]:
            response += f"• {feature}\n"
        
        response += f"\n**Status:**\n"
        response += f"• Downloaded from GitHub: ✅\n"
        response += f"• Saved to Azure storage: ✅\n"
        response += f"• Installation logged: ✅\n"
        response += f"• Ready to use: ✅\n"
        
        return response
    
    def _list_installed_agents(self):
        """List all installed GitHub agents"""
        try:
            log_data = self.storage_manager.read_file('agent_catalogue', 'installation_log.json')
            
            if not log_data:
                return "No agents have been installed from the GitHub library yet."
            
            installations = json.loads(log_data)
            installed_agents = installations.get('installations', [])
            
            if not installed_agents:
                return "No agents have been installed from the GitHub library yet."
            
            # Format response
            response = f"📦 Installed GitHub Library Agents ({len(installed_agents)}):\n\n"
            
            for i, agent in enumerate(installed_agents, 1):
                response += f"{i}. **{agent['agent_name']}**\n"
                response += f"   • ID: {agent['agent_id']}\n"
                response += f"   • Filename: {agent['filename']}\n"
                response += f"   • Type: {agent.get('type', 'singular')}\n"
                response += f"   • Installed: {agent['installed_at']}\n"
                response += f"   • Size: {agent.get('size', 'Unknown')}\n"
                
                if agent.get('stack'):
                    response += f"   • Stack: {agent['stack']['name']}\n"
                
                response += "\n"
            
            response += f"\n**Management Commands:**\n"
            response += f"• Update: `action='update', agent_id='agent_id'`\n"
            response += f"• Remove: `action='remove', agent_id='agent_id'`\n"
            response += f"• Details: `action='get_info', agent_id='agent_id'`\n"
            
            return response
        except Exception as e:
            logging.error(f"Error listing installed agents: {str(e)}")
            return f"Error: {str(e)}"
    
    def _update_agent(self, params):
        """Update an installed agent to the latest version"""
        agent_id = params.get('agent_id')
        
        if not agent_id:
            return "Error: agent_id is required"
        
        # Force reinstall
        params['force'] = True
        return self._install_agent(params)
    
    def _remove_agent(self, params):
        """Remove an installed agent"""
        agent_id = params.get('agent_id')
        
        if not agent_id:
            return "Error: agent_id is required"
        
        # Find agent in installation log
        try:
            log_data = self.storage_manager.read_file('agent_catalogue', 'installation_log.json')
            if not log_data:
                return f"Error: Agent '{agent_id}' not found in installation log"
            
            installations = json.loads(log_data)
            agent_entry = next((a for a in installations['installations'] if a['agent_id'] == agent_id), None)
            
            if not agent_entry:
                return f"Error: Agent '{agent_id}' not found in installation log"
            
            filename = agent_entry['filename']
            
            # Remove from storage (note: Azure File Storage doesn't have a delete method in the provided code)
            # We'll mark it as removed in the log instead
            
            # Remove from installation log
            installations['installations'] = [a for a in installations['installations'] if a['agent_id'] != agent_id]
            
            self.storage_manager.write_file(
                'agent_catalogue',
                'installation_log.json',
                json.dumps(installations, indent=2)
            )
            
            return f"✅ Agent '{agent_entry['agent_name']}' has been removed from the installation log.\n\nNote: The file may still exist in storage until manually deleted."
            
        except Exception as e:
            logging.error(f"Error removing agent: {str(e)}")
            return f"Error: {str(e)}"
    
    def _get_agent_info(self, params):
        """Get detailed information about an agent"""
        agent_id = params.get('agent_id')
        
        if not agent_id:
            return "Error: agent_id is required"
        
        manifest = self._fetch_manifest()
        if not manifest:
            return "Error: Unable to fetch agent library manifest"
        
        # Find agent in manifest
        agent_info = None
        
        # Check singular agents
        for agent in manifest.get('agents', []):
            if agent['id'] == agent_id:
                agent_info = agent
                break
        
        # Check stack agents
        if not agent_info:
            for stack in manifest.get('stacks', []):
                for agent in stack.get('agents', []):
                    if agent['id'] == agent_id:
                        agent_info = agent
                        agent_info['stack_info'] = {
                            'name': stack['name'],
                            'industry': stack.get('industry', 'General'),
                            'path': stack.get('path', '')
                        }
                        break
                if agent_info:
                    break
        
        if not agent_info:
            # Try to suggest a search
            search_term = agent_id.replace('_agent', '').replace('_', ' ')
            return f"""Error: Agent '{agent_id}' not found in library.

💡 Try searching to find the correct agent_id:
   action='search', search_query='{search_term}'

The search will show available agents and their exact IDs."""
        
        # Format detailed info
        response = f"📋 Agent Information: {agent_info['name']}\n\n"
        response += f"**Basic Info:**\n"
        response += f"• ID: {agent_info['id']}\n"
        response += f"• Filename: {agent_info['filename']}\n"
        response += f"• Type: {agent_info.get('type', 'singular')}\n"
        response += f"• Size: {agent_info.get('size_formatted', 'Unknown')}\n"
        response += f"• Icon: {agent_info.get('icon', '🤖')}\n\n"
        
        response += f"**Description:**\n{agent_info.get('description', 'No description available')}\n\n"
        
        if agent_info.get('features'):
            response += f"**Features:**\n"
            for feature in agent_info['features']:
                response += f"• {feature}\n"
            response += "\n"
        
        if agent_info.get('stack_info'):
            response += f"**Stack Information:**\n"
            response += f"• Stack: {agent_info['stack_info']['name']}\n"
            response += f"• Industry: {agent_info['stack_info']['industry']}\n"
            response += f"• Path: {agent_info['stack_info']['path']}\n\n"
        
        response += f"**Installation:**\n"
        response += f"To install: `action='install', agent_id='{agent_id}'"
        if agent_info.get('stack_info'):
            response += f", stack_path='{agent_info['stack_info']['path']}'"
        response += "`\n"
        
        return response
    
    def _sync_manifest(self):
        """Force sync/refresh the manifest from GitHub"""
        manifest = self._fetch_manifest(force_refresh=True)
        
        if not manifest:
            return "Error: Unable to sync manifest from GitHub"
        
        return f"""✅ Manifest synced successfully

**Library Stats:**
• Singular Agents: {len(manifest.get('agents', []))}
• Agent Stacks: {len(manifest.get('stacks', []))}
• Last Generated: {manifest.get('generated', 'Unknown')}
• Repository: {self.GITHUB_REPO}

The local cache has been refreshed with the latest agent library data."""
    
    # ===========================
    # GUID-BASED AGENT GROUP METHODS
    # ===========================
    
    def _create_agent_group(self, params):
        """
        Create a GUID-based agent group by downloading specific agents from GitHub.
        This allows creating custom agent deployments with a unique GUID.
        """
        agent_ids = params.get('agent_ids', [])
        group_name = params.get('group_name', 'Unnamed Agent Group')
        
        if not agent_ids or not isinstance(agent_ids, list):
            return "Error: agent_ids is required and must be a list of agent IDs"
        
        if len(agent_ids) == 0:
            return "Error: agent_ids list cannot be empty"
        
        try:
            # Fetch manifest from GitHub
            manifest = self._fetch_manifest()
            if not manifest:
                return "Error: Unable to fetch agent library manifest from GitHub"
            
            # Validate and download each agent
            downloaded_agents = []
            errors = []
            
            for agent_id in agent_ids:
                result = self._download_agent_for_group(agent_id, manifest)
                if result['success']:
                    downloaded_agents.append(result['filename'])
                else:
                    errors.append(f"❌ {agent_id}: {result['error']}")
            
            if not downloaded_agents:
                error_msg = "Error: No agents were successfully downloaded\n\n"
                error_msg += "\n".join(errors)
                error_msg += "\n\n💡 Use `action='search', search_query='keyword'` to find valid agent IDs"
                return error_msg
            
            # Generate new GUID for this agent group
            new_guid = str(uuid.uuid4())
            
            # Create agent config for this GUID
            config_result = self._create_agent_config(new_guid, downloaded_agents, group_name, agent_ids)
            
            if not config_result:
                return "Error: Failed to create agent configuration"
            
            # Format response
            response = f"✅ Successfully created agent group!\n\n"
            response += f"**Group Details:**\n"
            response += f"• Name: {group_name}\n"
            response += f"• GUID: `{new_guid}`\n"
            response += f"• Agents Downloaded: {len(downloaded_agents)}\n"
            response += f"• Total Requested: {len(agent_ids)}\n\n"
            
            response += f"**Downloaded Agents:**\n"
            for filename in downloaded_agents:
                response += f"• {filename}\n"
            
            if errors:
                response += f"\n**Warnings:**\n"
                response += "\n".join(errors)
            
            response += f"\n\n**How to Use This Group:**\n"
            response += f"1. Include this GUID in your API requests: `user_guid: '{new_guid}'`\n"
            response += f"2. Only the agents in this group will be loaded from Azure storage\n"
            response += f"3. All local agents will still be available\n"
            response += f"4. Use `action='get_group_info', guid='{new_guid}'` to view group details later\n\n"
            response += f"💡 This GUID is now stored in Azure storage at: `agent_config/{new_guid}/`\n"
            
            return response
            
        except Exception as e:
            logging.error(f"Error in create_agent_group: {str(e)}")
            return f"Error: {str(e)}"
    
    def _download_agent_for_group(self, agent_id, manifest):
        """Download a single agent from GitHub for a group"""
        # Find agent in manifest
        agent_info = None
        
        # Check singular agents
        for agent in manifest.get('agents', []):
            if agent['id'] == agent_id:
                agent_info = agent
                break
        
        # Check stack agents
        if not agent_info:
            for stack in manifest.get('stacks', []):
                for agent in stack.get('agents', []):
                    if agent['id'] == agent_id:
                        agent_info = agent
                        break
                if agent_info:
                    break
        
        if not agent_info:
            return {
                'success': False,
                'error': f"Agent ID '{agent_id}' not found in GitHub library"
            }
        
        # Download agent code
        try:
            response = requests.get(agent_info['url'], timeout=10)
            response.raise_for_status()
            agent_code = response.text
        except Exception as e:
            logging.error(f"Error fetching agent {agent_id}: {str(e)}")
            return {
                'success': False,
                'error': f"Failed to download from GitHub: {str(e)}"
            }
        
        # Store in Azure File Storage
        try:
            success = self.storage_manager.write_file('agents', agent_info['filename'], agent_code)
            if not success:
                return {
                    'success': False,
                    'error': 'Failed to write to Azure storage'
                }
            
            return {
                'success': True,
                'filename': agent_info['filename'],
                'agent_info': agent_info
            }
        except Exception as e:
            logging.error(f"Error storing agent {agent_id}: {str(e)}")
            return {
                'success': False,
                'error': f"Failed to save to storage: {str(e)}"
            }
    
    def _create_agent_config(self, guid, agent_filenames, group_name, agent_ids):
        """Create the agent configuration file for the GUID"""
        try:
            # Create the config directory path
            config_path = f"agent_config/{guid}"
            
            # Create the enabled agents list (just the filenames)
            enabled_agents_json = json.dumps(agent_filenames, indent=2)
            
            # Create metadata file
            metadata = {
                "guid": guid,
                "group_name": group_name,
                "created_at": datetime.now().isoformat(),
                "agent_ids": agent_ids,
                "agent_filenames": agent_filenames,
                "agent_count": len(agent_filenames),
                "source": "github_library"
            }
            metadata_json = json.dumps(metadata, indent=2)
            
            # Write both files to Azure storage
            success1 = self.storage_manager.write_file(config_path, 'enabled_agents.json', enabled_agents_json)
            success2 = self.storage_manager.write_file(config_path, 'metadata.json', metadata_json)
            
            return success1 and success2
        except Exception as e:
            logging.error(f"Error creating agent config: {str(e)}")
            return False
    
    def _list_agent_groups(self):
        """List all GUID-based agent groups"""
        try:
            # This would need to list all subdirectories under agent_config
            # Since we don't have a list_directories method, we'll need to track groups differently
            # For now, return a message about the limitation
            
            response = f"📦 GUID-Based Agent Groups\n\n"
            response += f"**Note:** To view a specific group's details, use:\n"
            response += f"`action='get_group_info', guid='your-guid-here'`\n\n"
            response += f"**How Groups Work:**\n"
            response += f"• Each group has a unique GUID that loads specific agents\n"
            response += f"• Groups are stored in Azure at: `agent_config/<guid>/`\n"
            response += f"• Include the GUID in API requests to use that group\n\n"
            response += f"**Available Actions:**\n"
            response += f"• Create: `action='create_group', agent_ids=['id1', 'id2'], group_name='Name'`\n"
            response += f"• View: `action='get_group_info', guid='guid-value'`\n"
            
            return response
            
        except Exception as e:
            logging.error(f"Error listing agent groups: {str(e)}")
            return f"Error: {str(e)}"
    
    def _get_group_info(self, params):
        """Get detailed information about a GUID-based agent group"""
        guid = params.get('guid')
        
        if not guid:
            return "Error: guid parameter is required"
        
        try:
            # Read the metadata file for this GUID
            config_path = f"agent_config/{guid}"
            metadata_json = self.storage_manager.read_file(config_path, 'metadata.json')
            
            if not metadata_json:
                return f"Error: Agent group with GUID '{guid}' not found"
            
            metadata = json.loads(metadata_json)
            
            # Read the enabled agents list
            enabled_agents_json = self.storage_manager.read_file(config_path, 'enabled_agents.json')
            enabled_agents = json.loads(enabled_agents_json) if enabled_agents_json else []
            
            # Format response
            response = f"📋 Agent Group Details\n\n"
            response += f"**Group Information:**\n"
            response += f"• Name: {metadata.get('group_name', 'Unnamed')}\n"
            response += f"• GUID: `{metadata.get('guid', guid)}`\n"
            response += f"• Created: {metadata.get('created_at', 'Unknown')}\n"
            response += f"• Agent Count: {metadata.get('agent_count', len(enabled_agents))}\n"
            response += f"• Source: {metadata.get('source', 'Unknown')}\n\n"
            
            response += f"**Agent IDs:**\n"
            for agent_id in metadata.get('agent_ids', []):
                response += f"• {agent_id}\n"
            response += "\n"
            
            response += f"**Agent Files:**\n"
            for filename in metadata.get('agent_filenames', enabled_agents):
                response += f"• {filename}\n"
            response += "\n"
            
            response += f"**Usage:**\n"
            response += f"Include this GUID in your API requests:\n"
            response += f"`user_guid: '{guid}'`\n\n"
            response += f"**Storage Location:**\n"
            response += f"`agent_config/{guid}/`\n"
            
            return response
            
        except Exception as e:
            logging.error(f"Error getting group info: {str(e)}")
            return f"Error: {str(e)}"
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
