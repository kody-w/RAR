---
name: "rar-kody-w-workiq"
description: "Access Microsoft 365 through the official Work IQ CLI. For current Teams status, use operation='teams_live' or operation='fetch' instead of trusting a semantic 'no update' answer. Also supports ask, search_paths, and get_schema."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/workiq", "rar_sha256": "e5cb90e2a731de05214243cc96ad52946ee5c4ef6c96cb724349469172bd8dc4", "source_kind": "rar-agent", "source_commit": "09f233a024d97f592c70107e1d3dee2b32eac874", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "workiq_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/workiq:0769118dc44e06bf48825f6d9dd3cbf6e24850524936977ae7d48153925c003a", "kind": "skill"}, "version": "1.1.2", "author": "Kody", "tags": ["m365", "microsoft", "email", "calendar", "teams", "sharepoint", "workiq"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/workiq`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `workiq_agent.py` is
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
