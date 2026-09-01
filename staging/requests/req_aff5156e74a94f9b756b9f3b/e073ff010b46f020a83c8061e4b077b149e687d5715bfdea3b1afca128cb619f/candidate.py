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
    The agent supports semantic queries and direct Work IQ entity reads.
    Examples:
    - "What emails did I receive from my manager this week?"
    - "What meetings do I have tomorrow?"
    - "Find documents about project planning"
    - operation="teams_live", query="What changed in Teams?"
    - operation="fetch", entity_urls=["/me/chats"]
"""

import html
import logging
import os
import re
import subprocess
import shutil
import json
import time
from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/workiq",
    "version": "1.1.2",
    "display_name": "WorkIQ",
    "description": "Queries Microsoft 365 through the official Work IQ CLI, including direct entity reads for live Teams data when semantic ask results are insufficient.",
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
                "Access Microsoft 365 through the official Work IQ CLI. For "
                "current Teams status, use operation='teams_live' or "
                "operation='fetch' instead of trusting a semantic 'no update' "
                "answer. Also supports ask, search_paths, and get_schema."
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
                    "operation": {
                        "type": "string",
                        "enum": [
                            "auto",
                            "ask",
                            "teams_live",
                            "fetch",
                            "search_paths",
                            "get_schema"
                        ],
                        "description": (
                            "Operation to run. 'auto' uses direct Teams entity "
                            "reads for Teams queries and semantic ask otherwise."
                        ),
                        "default": "auto"
                    },
                    "entity_urls": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": (
                            "Relative Work IQ entity paths for operation='fetch', "
                            "for example '/me/chats' or "
                            "'/me/chats/{id}/messages'."
                        )
                    },
                    "schema_path": {
                        "type": "string",
                        "description": (
                            "Relative Work IQ path for operation='get_schema'."
                        )
                    },
                    "schema_method": {
                        "type": "string",
                        "enum": ["get", "post", "patch", "delete"],
                        "description": "Optional schema method filter.",
                        "default": "get"
                    },
                    "account": {
                        "type": "string",
                        "description": (
                            "Optional cached Work IQ account email. Leave empty "
                            "to use the CLI default account."
                        )
                    },
                    "tenant_id": {
                        "type": "string",
                        "description": (
                            "Legacy compatibility field. Current Work IQ builds "
                            "select cached identities with the account parameter."
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
                "required": []
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        """Execute a WorkIQ query against Microsoft 365 data."""
        query = kwargs.get('query', '')
        operation = kwargs.get('operation', 'auto')
        account = kwargs.get('account', '')
        tenant_id = kwargs.get('tenant_id', '')
        data_type = kwargs.get('data_type', 'all')

        if not self._check_workiq_installed():
            return self._get_installation_instructions()

        if tenant_id:
            return (
                "Error: tenant_id is not supported by the current Work IQ CLI. "
                "Use the account parameter to select an explicitly cached "
                "Microsoft 365 identity; the agent will not silently fall back "
                "to a different tenant."
            )

        if operation == 'fetch':
            urls = kwargs.get('entity_urls') or []
            if not urls:
                return "Error: operation='fetch' requires entity_urls."
            return self._execute_entity_fetch(urls, account)

        if operation == 'search_paths':
            if not query:
                return "Error: operation='search_paths' requires query."
            return self._execute_search_paths(query, account)

        if operation == 'get_schema':
            path = kwargs.get('schema_path', '')
            if not path:
                return "Error: operation='get_schema' requires schema_path."
            return self._execute_get_schema(
                path,
                kwargs.get('schema_method', 'get'),
                account,
            )

        if not query:
            return "Error: No query provided. Please specify what information you want to find in Microsoft 365."

        if operation == 'teams_live' or (
            operation == 'auto'
            and data_type == 'teams'
            and re.search(
                r'\b(live|latest|current|recent|update|status|changed)\b',
                query,
                re.I,
            )
        ):
            return self._execute_live_teams_query(query, account)

        enhanced_query = self._build_enhanced_query(query, data_type)
        return self._execute_workiq_query(enhanced_query, account)

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
            "\n\nOfficial source: https://github.com/microsoft/work-iq"
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

    def _command_prefix(self):
        """Resolve the official Work IQ CLI or its npx fallback."""
        import sys as _sys
        workiq_path = shutil.which('workiq')
        if not workiq_path and _sys.platform == 'win32':
            candidate = os.path.join(
                os.path.expanduser("~"),
                "AppData",
                "Roaming",
                "npm",
                "workiq.CMD",
            )
            if os.path.isfile(candidate):
                workiq_path = candidate
        return [workiq_path] if workiq_path else [
            'npx',
            '-y',
            '@microsoft/workiq',
        ]

    def _run_cli(self, args, account='', timeout=180, retries=1):
        """Run an official Work IQ command with bounded transient retries."""
        command = self._command_prefix() + list(args)
        if account:
            command.extend(['--account', account])
        last_output = ''
        for attempt in range(max(1, retries)):
            try:
                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    shell=False,
                )
            except subprocess.TimeoutExpired as exc:
                if attempt + 1 == retries:
                    raise RuntimeError(
                        f"Work IQ command timed out after {timeout} seconds"
                    ) from exc
                time.sleep(2 ** attempt)
                continue
            output = _strip_ansi(result.stdout or result.stderr).strip()
            last_output = output
            if result.returncode == 0 and output:
                return output
            retryable = any(
                token in output.lower()
                for token in ('internal error', 'internalservererror', 'temporar')
            )
            if not retryable or attempt + 1 == retries:
                raise RuntimeError(output or 'Work IQ returned no content')
            time.sleep(2 ** attempt)
        raise RuntimeError(last_output or 'Work IQ command failed')

    def _fetch_json(self, entity_url, account=''):
        """Fetch one Work IQ entity and reject success-shaped error envelopes."""
        last_error = None
        for attempt in range(3):
            output = self._run_cli(
                ['fetch', '-u', entity_url],
                account,
                timeout=180,
            )
            try:
                value = json.loads(output)
            except json.JSONDecodeError as exc:
                raise RuntimeError(
                    f"Work IQ returned invalid JSON for {entity_url}"
                ) from exc
            if isinstance(value, dict) and 'results' in value:
                rows = value.get('results') or []
                first = rows[0] if rows else {}
                status = int(first.get('statusCode') or 500)
                if status < 400:
                    value = first.get('data') or {}
                else:
                    error = first.get('error')
                    last_error = (
                        f"Work IQ fetch failed for {entity_url}: "
                        f"{json.dumps(error)}"
                    )
                    retryable = (
                        status in (408, 429)
                        or status >= 500
                        or 'internal' in str(error).lower()
                        or 'temporar' in str(error).lower()
                    )
                    if not retryable:
                        raise RuntimeError(last_error)
                    value = None
            if isinstance(value, dict):
                return value
            if attempt < 2:
                time.sleep(2 ** attempt)
        raise RuntimeError(last_error or f"Work IQ fetch failed for {entity_url}")

    def _execute_workiq_query(self, query, account=''):
        """Execute a semantic Work IQ query."""
        try:
            logging.info("WorkIQ Agent executing semantic ask: %s...", query[:100])
            output = self._run_cli(
                ['ask', '--json', '-q', query],
                account,
                timeout=420,
            )
            try:
                value = json.loads(output)
            except json.JSONDecodeError:
                return self._format_output(output)
            if value.get('isError'):
                return f"Error querying Microsoft 365: {value.get('response')}"
            response = str(value.get('response') or '').strip()
            if not response:
                return (
                    "No source-backed semantic result was returned. For live "
                    "Teams status, use operation='teams_live' or 'fetch'."
                )
            return self._format_output(response)
        except FileNotFoundError:
            return self._get_installation_instructions()
        except Exception as exc:
            logging.error("WorkIQ Agent error: %s", exc)
            return f"Error executing Work IQ query: {exc}"

    def _execute_entity_fetch(self, entity_urls, account=''):
        """Fetch exact Microsoft 365 entities through Work IQ."""
        try:
            results = []
            for entity_url in entity_urls:
                if not isinstance(entity_url, str) or not entity_url.startswith('/'):
                    return "Error: Work IQ entity URLs must be relative paths beginning with '/'."
                results.append({
                    'entityUrl': entity_url,
                    'data': self._fetch_json(entity_url, account),
                })
            return (
                "**Microsoft 365 Direct Entity Results:**\n\n```json\n"
                + json.dumps({'results': results}, indent=2)
                + "\n```"
            )
        except Exception as exc:
            return f"Error fetching Microsoft 365 entities: {exc}"

    def _execute_search_paths(self, query, account=''):
        """Discover supported Work IQ entity paths."""
        try:
            output = self._run_cli(
                ['search-paths', '-f', query],
                account,
                timeout=120,
            )
            return f"**Work IQ Paths:**\n\n```text\n{output}\n```"
        except Exception as exc:
            return f"Error searching Work IQ paths: {exc}"

    def _execute_get_schema(self, path, method='get', account=''):
        """Read a Work IQ entity schema."""
        try:
            output = self._run_cli(
                ['get-schema', '-p', path, '-m', method],
                account,
                timeout=120,
            )
            return f"**Work IQ Schema:**\n\n```text\n{output}\n```"
        except Exception as exc:
            return f"Error reading Work IQ schema: {exc}"

    @staticmethod
    def _plain_text(value):
        text = html.unescape(re.sub(r'<[^>]+>', ' ', value or ''))
        return re.sub(r'\s+', ' ', text).strip()

    def _execute_live_teams_query(self, query, account=''):
        """Read live Teams chat previews through the Work IQ entity API."""
        try:
            entity_url = (
                "/me/chats?$top=50"
                "&$expand=lastMessagePreview"
            )
            value = self._fetch_json(entity_url, account)
            chats = [
                item
                for item in value.get('value', [])
                if isinstance(item, dict)
            ]
            count = value.get('@odata.count')
            if isinstance(count, int) and len(chats) < count:
                raise RuntimeError(
                    f"Work IQ returned only {len(chats)} of {count} chats"
                )
            stop = {
                'about', 'after', 'before', 'change', 'changed', 'current',
                'find', 'from', 'has', 'have', 'happened', 'latest',
                'message', 'messages', 'new', 'project', 'recent',
                'recently', 'said', 'show', 'status', 'team', 'teams', 'the',
                'this', 'update', 'updates', 'what', 'which', 'with',
            }
            terms = [
                token
                for token in re.findall(r'[a-z0-9][a-z0-9_-]+', query.lower())
                if len(token) >= 3 and token not in stop
            ]
            rows = []
            for chat in chats:
                preview = chat.get('lastMessagePreview') or {}
                sender = (
                    ((preview.get('from') or {}).get('user') or {}).get(
                        'displayName'
                    )
                    or ''
                )
                body = self._plain_text(
                    ((preview.get('body') or {}).get('content') or '')
                )
                haystack = ' '.join([
                    str(chat.get('topic') or ''),
                    sender,
                    body,
                ]).lower()
                if terms and not any(term in haystack for term in terms):
                    continue
                rows.append({
                    'chatId': chat.get('id'),
                    'topic': chat.get('topic'),
                    'chatType': chat.get('chatType'),
                    'previewCreatedDateTime': preview.get('createdDateTime'),
                    'sender': sender,
                    'preview': body,
                    'webUrl': chat.get('webUrl'),
                })
            rows.sort(
                key=lambda item: str(item.get('previewCreatedDateTime') or ''),
                reverse=True,
            )
            return (
                "**Microsoft 365 Live Teams Entity Results:**\n\n"
                "This result comes from `/me/chats` and `lastMessagePreview`, "
                "not semantic `ask`. Use operation='fetch' with the returned "
                "chat ID to inspect `/me/chats/{id}/messages`. A messages "
                "response with `@odata.nextLink` is page-capped and must not "
                "be treated as complete.\n\n```json\n"
                + json.dumps({
                    'queryTerms': terms,
                    'returnedChatCount': len(chats),
                    'partial': bool(value.get('@odata.nextLink')),
                    'partialWarning': (
                        "Work IQ returned @odata.nextLink; do not interpret "
                        "zero matches as proof that no update exists."
                        if value.get('@odata.nextLink')
                        else None
                    ),
                    'matchedCount': len(rows),
                    'chats': rows[:25],
                }, indent=2)
                + "\n```"
            )
        except Exception as exc:
            return f"Error reading live Teams entities: {exc}"

    def _format_output(self, output):
        """Format the workiq output for better readability."""
        if output.startswith('{') or output.startswith('['):
            try:
                data = json.loads(output)
                return f"**Microsoft 365 Query Results:**\n\n```json\n{json.dumps(data, indent=2)}\n```"
            except json.JSONDecodeError:
                pass

        return f"**Microsoft 365 Query Results:**\n\n{output}"
