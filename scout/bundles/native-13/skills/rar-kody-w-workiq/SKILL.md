---
name: "rar-kody-w-workiq"
description: "Access Microsoft 365 through the official Work IQ CLI. For current Teams status, use operation='teams_live' or operation='fetch' instead of trusting a semantic 'no update' answer. Also supports ask, search_paths, and get_schema."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/workiq", "rar_sha256": "7f6de288bc1e6756834a22d68cf832b987c9d5a28ef3338e658a6948a5b18fab", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.2", "author": "Kody", "tags": ["m365", "microsoft", "email", "calendar", "teams", "sharepoint", "workiq"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `workiq_agent.py` and embedded as the fenced Python below (sha256 7f6de288bc1e6756…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `workiq_agent.py` first:

```bash
python3 workiq_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 workiq_agent.py   # or on stdin
python3 workiq_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/workiq_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/workiq_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/workiq/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
