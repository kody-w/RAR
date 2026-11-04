---
name: "rar-kody-w-github-agent-library"
description: "Comprehensive manager for the GitHub Agent Template Library at kody-w/AI-Agent-Templates. Discovers, searches, installs, and manages 65+ pre-built agents from the public repository. Also creates GUID-based agent groups for custom deployments. All agents are downloaded from GitHub raw URLs and automatically integrated into your system."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/github_agent_library_agent", "rar_sha256": "b9bd6d0f87082877c37cca17be3a1d5ba873dcf736ce9805538eb8affcfadbab", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["core", "package-manager", "install", "discovery"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `github_agent_library_agent.py` and embedded as the fenced Python below (sha256 b9bd6d0f87082877…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `github_agent_library_agent.py` first:

```bash
python3 github_agent_library_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 github_agent_library_agent.py   # or on stdin
python3 github_agent_library_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/github_agent_library_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/github_agent_library_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/github_agent_library_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
