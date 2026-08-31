---
name: "rar-kody-w-workiq"
description: "Access Microsoft 365 through the official Work IQ CLI. For current Teams status, use operation='teams_live' or operation='fetch' instead of trusting a semantic 'no update' answer. Also supports ask, search_paths, and get_schema."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/workiq", "rar_sha256": "e5cb90e2a731de05214243cc96ad52946ee5c4ef6c96cb724349469172bd8dc4", "source_kind": "rar-agent", "source_commit": "c1e5a4e591cee3007b204676a8a236fa341939b4", "version": "1.1.2", "author": "Kody", "tags": ["m365", "microsoft", "email", "calendar", "teams", "sharepoint", "workiq"]}
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
