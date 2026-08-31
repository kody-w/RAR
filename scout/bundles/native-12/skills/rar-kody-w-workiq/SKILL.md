---
name: "rar-kody-w-workiq"
description: "Access Microsoft 365 through the official Work IQ CLI. For current Teams status, use operation='teams_live' or operation='fetch' instead of trusting a semantic 'no update' answer. Also supports ask, search_paths, and get_schema."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/workiq", "rar_sha256": "e5cb90e2a731de05214243cc96ad52946ee5c4ef6c96cb724349469172bd8dc4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.2", "author": "Kody", "tags": ["m365", "microsoft", "email", "calendar", "teams", "sharepoint", "workiq"]}
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
    The agent supports semantic queries and direct Work IQ entity reads.
    Examples:
    - "What emails did I receive from my manager this week?"
    - "What meetings do I have tomorrow?"
    - "Find documents about project planning"
    - operation="teams_live", query="What changed in Teams?"
    - operation="fetch", entity_urls=["/me/chats"]

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "account": {
      "description": "Optional cached Work IQ account email. Leave empty to use the CLI default account.",
      "type": "string"
    },
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
    "entity_urls": {
      "description": "Relative Work IQ entity paths for operation='fetch', for example '/me/chats' or '/me/chats/{id}/messages'.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "operation": {
      "default": "auto",
      "description": "Operation to run. 'auto' uses direct Teams entity reads for Teams queries and semantic ask otherwise.",
      "enum": [
        "auto",
        "ask",
        "teams_live",
        "fetch",
        "search_paths",
        "get_schema"
      ],
      "type": "string"
    },
    "query": {
      "description": "The natural language query to search Microsoft 365 data. Examples: 'What emails did I receive from John this week?', 'What meetings do I have tomorrow?', 'Find documents about the Q4 budget', 'What did the team say about the deadline in Teams?'",
      "type": "string"
    },
    "schema_method": {
      "default": "get",
      "description": "Optional schema method filter.",
      "enum": [
        "get",
        "post",
        "patch",
        "delete"
      ],
      "type": "string"
    },
    "schema_path": {
      "description": "Relative Work IQ path for operation='get_schema'.",
      "type": "string"
    },
    "tenant_id": {
      "description": "Legacy compatibility field. Current Work IQ builds select cached identities with the account parameter.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `workiq_agent.py` and embedded as the fenced Python below (sha256 e5cb90e2a731de05…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `workiq_agent.py` first:

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
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
