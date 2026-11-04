---
name: "rar-kody-w-github-agent-library"
description: "Comprehensive manager for the GitHub Agent Template Library at kody-w/AI-Agent-Templates. Discovers, searches, installs, and manages 65+ pre-built agents from the public repository. Also creates GUID-based agent groups for custom deployments. All agents are downloaded from GitHub raw URLs and automatically integrated into your system."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/github_agent_library_agent", "rar_sha256": "b9bd6d0f87082877c37cca17be3a1d5ba873dcf736ce9805538eb8affcfadbab", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["core", "package-manager", "install", "discovery"]}
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
