---
name: "rar-kody-w-workiq"
description: "Access Microsoft 365 data using natural language queries. Can search emails, calendar meetings, documents, Teams messages, and people information. Use this agent when the user wants to find or retrieve information from their Microsoft 365 tenant."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/workiq", "rar_sha256": "52075126c877c38ed9d5f135b74f6a490c1593957f6b8fa2367ff2b7eb5c3949", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "Kody", "tags": ["m365", "microsoft", "email", "calendar", "teams", "sharepoint", "workiq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/workiq`. The original RAPP
agent is preserved byte-for-byte in `workiq_agent.py` and in the RCI capsule.

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

WorkIQ Agent - Microsoft 365 Data Access via work-iq-mcp

This agent provides natural language access to Microsoft 365 data including:
- Emails and conversations
- Calendar meetings and events
- Documents (SharePoint, OneDrive)
- Teams messages and channels
- People and organizational contacts

Prerequisites:
    1. Install workiq CLI: npm install -g @microsoft/workiq
    2. Accept EULA: workiq accept-eula
    3. Authenticate: Run workiq ask once to complete Entra ID login

Usage:
    The agent accepts natural language queries about M365 data.
    Examples:
    - "What emails did I receive from my manager this week?"
    - "What meetings do I have tomorrow?"
    - "Find documents about project planning"
    - "What did Sarah say in Teams about the deadline?"

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "data_type": {
      "description": "Optional filter to search only specific data types. Default is 'all' which searches across all Microsoft 365 data.",
      "enum": [
        "all",
        "email",
        "calendar",
        "documents",
        "teams",
        "people"
      ],
      "type": "string"
    },
    "query": {
      "description": "The natural language query to search Microsoft 365 data. Examples: 'What emails did I receive from John this week?', 'What meetings do I have tomorrow?', 'Find documents about the Q4 budget', 'What did the team say about the deadline in Teams?'",
      "type": "string"
    },
    "tenant_id": {
      "description": "Optional Entra tenant ID for multi-tenant scenarios. Leave empty to use the default 'common' tenant.",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `workiq_agent.py` and embedded as the fenced Python below (sha256 52075126c877c38e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `workiq_agent.py` first:

```bash
python3 workiq_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 workiq_agent.py   # or on stdin
python3 workiq_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
WorkIQ Agent - Microsoft 365 Data Access via work-iq-mcp

This agent provides natural language access to Microsoft 365 data including:
- Emails and conversations
- Calendar meetings and events
- Documents (SharePoint, OneDrive)
- Teams messages and channels
- People and organizational contacts

Prerequisites:
    1. Install workiq CLI: npm install -g @microsoft/workiq
    2. Accept EULA: workiq accept-eula
    3. Authenticate: Run workiq ask once to complete Entra ID login

Usage:
    The agent accepts natural language queries about M365 data.
    Examples:
    - "What emails did I receive from my manager this week?"
    - "What meetings do I have tomorrow?"
    - "Find documents about project planning"
    - "What did Sarah say in Teams about the deadline?"
"""

import logging
import os
import re
import subprocess
import shutil
import json
from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/workiq",
    "version": "1.0.2",
    "display_name": "WorkIQ",
    "description": "Queries Microsoft 365 data \u2014 email, calendar, SharePoint/OneDrive, Teams, people \u2014 by shelling out to the workiq CLI with Entra ID auth.",
    "author": "Kody",
    "tags": ["m365", "microsoft", "email", "calendar", "teams", "sharepoint", "workiq"],
    "category": "integrations",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "external_prereqs": [
        "npm install -g @microsoft/workiq",
        "workiq accept-eula",
        "Entra ID login (run `workiq ask` once)",
    ],
    "example_call": "What emails did I receive from my manager this week?",
}



_ANSI_RE = re.compile(r'\x1b(?:\[[0-9;?]*[a-zA-Z]|\][^\x07\x1b]*(?:\x07|\x1b\\))')


def _strip_ansi(text):
    return _ANSI_RE.sub('', text or '')


class WorkIQAgent(BasicAgent):
    def __init__(self):
        self.name = 'WorkIQ'
        self.metadata = {
            "name": self.name,
            "description": (
                "Access Microsoft 365 data using natural language queries. "
                "Can search emails, calendar meetings, documents, Teams messages, and people information. "
                "Use this agent when the user wants to find or retrieve information from their Microsoft 365 tenant."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": (
                            "The natural language query to search Microsoft 365 data. "
                            "Examples: 'What emails did I receive from John this week?', "
                            "'What meetings do I have tomorrow?', "
                            "'Find documents about the Q4 budget', "
                            "'What did the team say about the deadline in Teams?'"
                        )
                    },
                    "tenant_id": {
                        "type": "string",
                        "description": (
                            "Optional Entra tenant ID for multi-tenant scenarios. "
                            "Leave empty to use the default 'common' tenant."
                        )
                    },
                    "data_type": {
                        "type": "string",
                        "enum": ["all", "email", "calendar", "documents", "teams", "people"],
                        "description": (
                            "Optional filter to search only specific data types. "
                            "Default is 'all' which searches across all Microsoft 365 data."
                        )
                    }
                },
                "required": ["query"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        """Execute a WorkIQ query against Microsoft 365 data."""
        query = kwargs.get('query', '')
        tenant_id = kwargs.get('tenant_id', '')
        data_type = kwargs.get('data_type', 'all')

        if not query:
            return "Error: No query provided. Please specify what information you want to find in Microsoft 365."

        if not self._check_workiq_installed():
            return self._get_installation_instructions()

        enhanced_query = self._build_enhanced_query(query, data_type)
        return self._execute_workiq_query(enhanced_query, tenant_id)

    def _check_workiq_installed(self):
        """Check if the workiq CLI is installed and available."""
        import sys as _sys
        if shutil.which('workiq'):
            return True
        if _sys.platform == 'win32':
            appdata_cmd = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "npm", "workiq.CMD")
            if os.path.isfile(appdata_cmd):
                return True
        if shutil.which('npx'):
            return True
        return False

    def _get_installation_instructions(self):
        """Return instructions for installing workiq."""
        return (
            "**WorkIQ CLI not found.** To use this agent, please install the WorkIQ CLI:\n\n"
            "**Option 1 - Global installation:**\n"
            "```bash\n"
            "npm install -g @microsoft/workiq\n"
            "workiq accept-eula\n"
            "```\n\n"
            "**Option 2 - Use without installation (via npx):**\n"
            "```bash\n"
            "npx -y @microsoft/workiq accept-eula\n"
            "```\n\n"
            "After installation, run `workiq ask 'test query'` once to complete Entra ID authentication."
        )

    def _build_enhanced_query(self, query, data_type):
        """Build an enhanced query with data type context."""
        if data_type == 'all':
            return query

        context_hints = {
            'email': f"In my emails: {query}",
            'calendar': f"In my calendar/meetings: {query}",
            'documents': f"In my documents (SharePoint/OneDrive): {query}",
            'teams': f"In Teams messages: {query}",
            'people': f"About people/contacts: {query}"
        }

        return context_hints.get(data_type, query)

    def _execute_workiq_query(self, query, tenant_id=''):
        """Execute a query using the workiq CLI."""
        import sys as _sys
        try:
            workiq_path = shutil.which('workiq')
            if not workiq_path and _sys.platform == 'win32':
                appdata_cmd = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "npm", "workiq.CMD")
                if os.path.isfile(appdata_cmd):
                    workiq_path = appdata_cmd

            if workiq_path:
                cmd = [workiq_path, 'ask', '-q', query]
            else:
                cmd = ['npx', '-y', '@microsoft/workiq', 'ask', '-q', query]

            if tenant_id:
                cmd.extend(['--tenant-id', tenant_id])

            logging.info(f"WorkIQ Agent executing query: {query[:100]}...")

            use_shell = _sys.platform == 'win32'

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120,
                shell=use_shell
            )

            if result.returncode != 0:
                error_msg = result.stderr.strip() if result.stderr else "Unknown error"

                if 'EULA' in error_msg or 'accept-eula' in error_msg.lower():
                    return (
                        "**EULA not accepted.** Please run the following command first:\n"
                        "```bash\n"
                        "workiq accept-eula\n"
                        "```"
                    )
                elif 'login' in error_msg.lower() or 'auth' in error_msg.lower():
                    return (
                        "**Authentication required.** Please authenticate with Microsoft Entra ID:\n"
                        "```bash\n"
                        "workiq ask 'test'\n"
                        "```\n"
                        "This will open a browser window for authentication."
                    )
                else:
                    logging.error(f"WorkIQ error: {error_msg}")
                    return f"Error querying Microsoft 365: {error_msg}"

            output = _strip_ansi(result.stdout).strip()

            if not output:
                return "No results found for your query. Try rephrasing or broadening your search."

            return self._format_output(output)

        except subprocess.TimeoutExpired:
            logging.error("WorkIQ query timed out after 120 seconds")
            return (
                "The query timed out. This might happen if:\n"
                "- The query is too broad (try being more specific)\n"
                "- Network connectivity issues\n"
                "- Microsoft 365 services are slow to respond\n\n"
                "Please try a more specific query."
            )
        except FileNotFoundError:
            return self._get_installation_instructions()
        except Exception as e:
            logging.error(f"WorkIQ Agent error: {str(e)}")
            return f"Error executing WorkIQ query: {str(e)}"

    def _format_output(self, output):
        """Format the workiq output for better readability."""
        if output.startswith('{') or output.startswith('['):
            try:
                data = json.loads(output)
                return f"**Microsoft 365 Query Results:**\n\n```json\n{json.dumps(data, indent=2)}\n```"
            except json.JSONDecodeError:
                pass

        return f"**Microsoft 365 Query Results:**\n\n{output}"
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
