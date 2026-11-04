---
name: "rar-kody-w-workiq"
description: "Access Microsoft 365 through the official Work IQ CLI. For current Teams status, use operation='teams_live' or operation='fetch' instead of trusting a semantic 'no update' answer. Also supports ask, search_paths, and get_schema."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/workiq", "rar_sha256": "7f6de288bc1e6756834a22d68cf832b987c9d5a28ef3338e658a6948a5b18fab", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.2", "author": "Kody", "tags": ["m365", "microsoft", "email", "calendar", "teams", "sharepoint", "workiq"]}
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
