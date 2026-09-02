---
name: "rar-kody-w-github-agent-library"
description: "Comprehensive manager for the GitHub Agent Template Library at kody-w/AI-Agent-Templates. Discovers, searches, installs, and manages 65+ pre-built agents from the public repository. Also creates GUID-based agent groups for custom deployments. All agents are downloaded from GitHub raw URLs and automatically integrated into your system."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/github_agent_library_agent", "rar_sha256": "7d25b2d553356cfcb2f74921552b984d8e348ab56f20984fcda831eb65336923", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "github_agent_library_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/github-agent-library:2eec5bacd5b2840381e96ab956bc7c3da6736342241846e7b2944e018af6b0c3", "kind": "skill"}, "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["core", "package-manager", "install", "discovery"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/github_agent_library_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `github_agent_library_agent.py` is
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
