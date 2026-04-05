from agents.basic_agent import BasicAgent

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody/github_agent_library",
    "version": "1.0.0",
    "display_name": "GitHubAgentLibrary",
    "description": "Browse, search, and install agents from the RAPP Agent Repo via chat. The autonomous package manager.",
    "author": "Kody Wildfeuer",
    "tags": ["core", "package-manager", "install", "discovery"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
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