---
name: "rar-kody-w-workiq"
description: "Access Microsoft 365 through the official Work IQ CLI. For current Teams status, use operation='teams_live' or operation='fetch' instead of trusting a semantic 'no update' answer. Also supports ask, search_paths, and get_schema."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/workiq", "rar_sha256": "e5cb90e2a731de05214243cc96ad52946ee5c4ef6c96cb724349469172bd8dc4", "source_kind": "rar-agent", "source_commit": "09f233a024d97f592c70107e1d3dee2b32eac874", "version": "1.1.2", "author": "Kody", "tags": ["m365", "microsoft", "email", "calendar", "teams", "sharepoint", "workiq"]}
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
