---
name: "rar-kody-w-workiq"
description: "Access Microsoft 365 through the official Work IQ CLI. For current Teams status, use operation='teams_live' or operation='fetch' instead of trusting a semantic 'no update' answer. Also supports ask, search_paths, and get_schema."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/workiq", "rar_sha256": "e5cb90e2a731de05214243cc96ad52946ee5c4ef6c96cb724349469172bd8dc4", "source_kind": "rar-agent", "source_commit": "18db1bbd65dfdc2f1cd6756f698f4a1d59a7aa71", "version": "1.1.2", "author": "Kody", "tags": ["m365", "microsoft", "email", "calendar", "teams", "sharepoint", "workiq"]}
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
