---
name: "rar-kody-w-agent-workbench"
description: "Build, validate, test, and publish single-file RAPP agents. The development companion for the agent.py pattern."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/agent_workbench", "rar_sha256": "00b19b2e98b854333dbf7d89d74980f3e54c4f5753f31ac9039cf8f8ed30e2b4", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.1.2", "author": "RAPP Core Team", "tags": ["devtools", "workbench", "scaffolding", "validation", "testing", "publishing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/agent_workbench`. The original RAPP
agent is preserved byte-for-byte in `agent_workbench_agent.py` and in the RCI capsule.

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

Agent Workbench — Build, validate, test, and iterate on single-file RAPP agents.

The workbench is the development environment for the single-file agent pattern.
It understands the RAPP conventions — __manifest__, BasicAgent, perform() — and
helps you go from blank file to published agent without leaving the brainstem.

Workflow:
  1. scaffold  — Generate a new agent.py from a template
  2. validate  — Check manifest, syntax, required fields, naming conventions
  3. dry_run   — Execute perform() in a sandboxed context and show the result
  4. diff      — Compare local agent against the published registry version
  5. publish   — Submit the agent to RAPP via Issues-as-API

The workbench enforces the RAPP Constitution: single file, no secrets,
no network in __init__, readable code, declared env vars. It catches
problems before they reach the registry.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "scaffold: generate new agent from template, validate: check agent file against Constitution, dry_run: execute perform() in sandbox, diff: compare local vs published, publish: submit to RAPP",
      "enum": [
        "scaffold",
        "validate",
        "dry_run",
        "diff",
        "publish"
      ],
      "type": "string"
    },
    "agent_path": {
      "description": "Path to the agent .py file (for validate/dry_run/diff/publish)",
      "type": "string"
    },
    "author": {
      "description": "Author name",
      "type": "string"
    },
    "display_name": {
      "description": "Human-readable agent name",
      "type": "string"
    },
    "dry_run_kwargs": {
      "description": "kwargs to pass to perform() during dry_run",
      "type": "object"
    },
    "publisher": {
      "description": "Your @publisher namespace (e.g. 'kody')",
      "type": "string"
    },
    "slug": {
      "description": "Agent slug in snake_case (e.g. 'my_agent')",
      "type": "string"
    },
    "template": {
      "description": "Template to use for scaffold action",
      "enum": [
        "blank",
        "api"
      ],
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_workbench_agent.py` and embedded as the fenced Python below (sha256 00b19b2e98b85433…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_workbench_agent.py` first:

```bash
python3 agent_workbench_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_workbench_agent.py   # or on stdin
python3 agent_workbench_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
Agent Workbench — Build, validate, test, and iterate on single-file RAPP agents.

The workbench is the development environment for the single-file agent pattern.
It understands the RAPP conventions — __manifest__, BasicAgent, perform() — and
helps you go from blank file to published agent without leaving the brainstem.

Workflow:
  1. scaffold  — Generate a new agent.py from a template
  2. validate  — Check manifest, syntax, required fields, naming conventions
  3. dry_run   — Execute perform() in a sandboxed context and show the result
  4. diff      — Compare local agent against the published registry version
  5. publish   — Submit the agent to RAPP via Issues-as-API

The workbench enforces the RAPP Constitution: single file, no secrets,
no network in __init__, readable code, declared env vars. It catches
problems before they reach the registry.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/agent_workbench",
    "version": "1.1.2",
    "display_name": "Agent Workbench",
    "description": "Scaffolds, validates, dry-runs, diffs, and publishes single-file RAPP agents against the registry via GitHub Issues-as-API.",
    "author": "RAPP Core Team",
    "tags": ["devtools", "workbench", "scaffolding", "validation", "testing", "publishing"],
    "category": "devtools",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

from agents.basic_agent import BasicAgent
import ast
import json
import logging
import os
import re
import textwrap
import traceback
from pathlib import Path

logger = logging.getLogger(__name__)

# Optional brainstem integrations
try:
    from utils.storage_factory import get_storage_manager
    _HAS_STORAGE = True
except ImportError:
    _HAS_STORAGE = False


# ══════════════════════════════════════════════════════════════════
# Templates
# ══════════════════════════════════════════════════════════════════

TEMPLATES = {
    "blank": textwrap.dedent('''\
        """
        {display_name} — One-line description here.

        Longer explanation of what this agent does, how to use it,
        and any configuration it needs.
        """

        __manifest__ = {{
            "schema": "rapp-agent/1.0",
            "name": "@{publisher}/{slug}",
            "version": "0.1.0",
            "display_name": "{display_name}",
            "description": "One-line description here.",
            "author": "{author}",
            "tags": [],
            "category": "general",
            "quality_tier": "experimental",
            "requires_env": [],
            "dependencies": ["@rapp/basic_agent"],
        }}

        try:
            from agents.basic_agent import BasicAgent
        except ModuleNotFoundError:
            class BasicAgent:
                def __init__(self, name, metadata):
                    self.name = name
                    self.metadata = metadata


        class {class_name}(BasicAgent):
            def __init__(self):
                self.name = "{class_name}"
                self.metadata = {{
                    "name": self.name,
                    "display_name": "{display_name}",
                    "description": __manifest__["description"],
                    "parameters": {{
                        "type": "object",
                        "properties": {{
                            "task": {{
                                "type": "string",
                                "description": "What to do"
                            }}
                        }},
                        "required": ["task"]
                    }}
                }}
                super().__init__(self.name, self.metadata)

            async def perform(self, **kwargs):
                task = kwargs.get("task", "")
                return f"{{self.name}} received: {{task}}"
    '''),

    "api": textwrap.dedent('''\
        """
        {display_name} — Connects to an external API.

        Requires: {env_var} environment variable.
        """

        __manifest__ = {{
            "schema": "rapp-agent/1.0",
            "name": "@{publisher}/{slug}",
            "version": "0.1.0",
            "display_name": "{display_name}",
            "description": "Connects to an external API.",
            "author": "{author}",
            "tags": ["integrations"],
            "category": "integrations",
            "quality_tier": "experimental",
            "requires_env": ["{env_var}"],
            "dependencies": ["@rapp/basic_agent"],
        }}

        import os
        import urllib.request
        import json
        try:
            from agents.basic_agent import BasicAgent
        except ModuleNotFoundError:
            class BasicAgent:
                def __init__(self, name, metadata):
                    self.name = name
                    self.metadata = metadata


        class {class_name}(BasicAgent):
            def __init__(self):
                self.name = "{class_name}"
                self.metadata = {{
                    "name": self.name,
                    "display_name": "{display_name}",
                    "description": __manifest__["description"],
                    "parameters": {{
                        "type": "object",
                        "properties": {{
                            "query": {{
                                "type": "string",
                                "description": "Query to send to the API"
                            }}
                        }},
                        "required": ["query"]
                    }}
                }}
                super().__init__(self.name, self.metadata)

            async def perform(self, **kwargs):
                api_key = os.environ.get("{env_var}")
                if not api_key:
                    return "Error: {env_var} not set. Add it to your .env file."

                query = kwargs.get("query", "")
                # TODO: Replace with your actual API endpoint
                return f"{{self.name}} would query: {{query}}"
    '''),
}


# ══════════════════════════════════════════════════════════════════
# Validation rules (derived from CONSTITUTION.md)
# ══════════════════════════════════════════════════════════════════

REQUIRED_MANIFEST_FIELDS = [
    "schema", "name", "version", "display_name",
    "description", "author", "tags", "category",
]

VALID_CATEGORIES = {"core", "pipeline", "integrations", "productivity", "devtools", "general"}
VALID_TIERS = {"official", "verified", "community", "experimental"}
SUBMITTABLE_TIERS = {"community", "experimental"}


class AgentWorkbenchAgent(BasicAgent):
    """
    Agent Workbench — the development companion for building RAPP agents.

    Actions:
      scaffold  — Generate a new agent from a template
      validate  — Deep validation of an agent file against the Constitution
      dry_run   — Execute perform() in isolation and report the result
      diff      — Compare local vs. published version
      publish   — Submit to RAPP via Issues-as-API
    """

    def __init__(self):
        self.name = "AgentWorkbench"
        self.metadata = {
            "name": self.name,
            "description": (
                "Build, validate, test, and publish single-file RAPP agents. "
                "The development companion for the agent.py pattern."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["scaffold", "validate", "dry_run", "diff", "publish"],
                        "description": (
                            "scaffold: generate new agent from template, "
                            "validate: check agent file against Constitution, "
                            "dry_run: execute perform() in sandbox, "
                            "diff: compare local vs published, "
                            "publish: submit to RAPP"
                        )
                    },
                    "agent_path": {
                        "type": "string",
                        "description": "Path to the agent .py file (for validate/dry_run/diff/publish)"
                    },
                    "template": {
                        "type": "string",
                        "enum": ["blank", "api"],
                        "description": "Template to use for scaffold action"
                    },
                    "publisher": {
                        "type": "string",
                        "description": "Your @publisher namespace (e.g. 'kody')"
                    },
                    "slug": {
                        "type": "string",
                        "description": "Agent slug in snake_case (e.g. 'my_agent')"
                    },
                    "display_name": {
                        "type": "string",
                        "description": "Human-readable agent name"
                    },
                    "author": {
                        "type": "string",
                        "description": "Author name"
                    },
                    "dry_run_kwargs": {
                        "type": "object",
                        "description": "kwargs to pass to perform() during dry_run"
                    },
                },
                "required": ["action"]
            }
        }
        super().__init__(self.name, self.metadata)

    # ──────────────────────────────────────────────────────────
    # Dispatcher
    # ──────────────────────────────────────────────────────────

    async def perform(self, **kwargs):
        action = kwargs.get("action", "")
        dispatch = {
            "scaffold": self._scaffold,
            "validate": self._validate,
            "dry_run": self._dry_run,
            "diff": self._diff,
            "publish": self._publish,
        }
        handler = dispatch.get(action)
        if not handler:
            return (
                f"Unknown action '{action}'. "
                f"Valid: {', '.join(dispatch.keys())}"
            )
        return await handler(**kwargs)

    # ──────────────────────────────────────────────────────────
    # scaffold
    # ──────────────────────────────────────────────────────────

    async def _scaffold(self, **kwargs):
        template_key = kwargs.get("template", "blank")
        publisher = kwargs.get("publisher", "your-username")
        slug = kwargs.get("slug", "my_agent")
        display_name = kwargs.get("display_name", slug.replace("_", " ").title())
        author = kwargs.get("author", publisher)

        template = TEMPLATES.get(template_key)
        if not template:
            return f"Unknown template '{template_key}'. Available: {', '.join(TEMPLATES.keys())}"

        # Derive class name from slug
        class_name = "".join(w.capitalize() for w in slug.split("_")) + "Agent"

        code = template.format(
            publisher=publisher,
            slug=slug,
            display_name=display_name,
            class_name=class_name,
            author=author,
            env_var=f"{slug.upper()}_API_KEY",
        )

        # Write to the conventional path
        agents_dir = Path("agents") / f"@{publisher}"
        agents_dir.mkdir(parents=True, exist_ok=True)
        file_path = agents_dir / f"{slug}.py"

        if file_path.exists():
            return (
                f"File already exists: {file_path}\n"
                f"Use 'validate' to check the existing file, or choose a different slug."
            )

        file_path.write_text(code)

        return (
            f"Scaffolded new agent: {file_path}\n"
            f"  Name: @{publisher}/{slug}\n"
            f"  Class: {class_name}\n"
            f"  Template: {template_key}\n\n"
            f"Next steps:\n"
            f"  1. Edit the docstring and description\n"
            f"  2. Implement perform() with your logic\n"
            f"  3. Run: workbench validate agent_path={file_path}\n"
            f"  4. Run: workbench dry_run agent_path={file_path}\n"
            f"  5. Run: workbench publish agent_path={file_path}"
        )

    # ──────────────────────────────────────────────────────────
    # validate
    # ──────────────────────────────────────────────────────────

    async def _validate(self, **kwargs):
        path = self._resolve_path(kwargs.get("agent_path", ""))
        if not path:
            return "Error: agent_path is required for validate"
        if not path.exists():
            return f"File not found: {path}"

        code = path.read_text()
        errors = []
        warnings = []

        # 1. Syntax check
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            return f"SYNTAX ERROR at line {e.lineno}: {e.msg}\n\nFix this before anything else."

        # 2. Extract manifest
        manifest = self._extract_manifest(tree)
        if manifest is None:
            errors.append("No __manifest__ dict found. Every agent needs one.")
        else:
            # 3. Required fields
            for field in REQUIRED_MANIFEST_FIELDS:
                if field not in manifest:
                    errors.append(f"Missing required manifest field: {field}")

            # 4. Name format
            name = manifest.get("name", "")
            if not name.startswith("@") or "/" not in name:
                errors.append(f"Invalid name '{name}' — must be @publisher/slug")
            else:
                parts = name.split("/")
                slug_part = parts[1] if len(parts) > 1 else ""
                if slug_part != slug_part.lower() or "-" in slug_part:
                    warnings.append(
                        f"Slug '{slug_part}' should use snake_case "
                        f"(e.g. '{slug_part.lower().replace('-', '_')}')"
                    )
                # Check name matches file path
                expected_slug = path.stem
                if slug_part and slug_part != expected_slug:
                    warnings.append(
                        f"Manifest name slug '{slug_part}' doesn't match "
                        f"filename '{expected_slug}'"
                    )

            # 5. Version
            version = manifest.get("version", "")
            v_parts = version.split(".")
            if len(v_parts) != 3 or not all(p.isdigit() for p in v_parts):
                errors.append(f"Invalid version '{version}' — must be semver (e.g. 1.0.0)")

            # 6. Category
            cat = manifest.get("category", "")
            if cat and cat not in VALID_CATEGORIES:
                warnings.append(
                    f"Unknown category '{cat}'. "
                    f"Standard: {', '.join(sorted(VALID_CATEGORIES))}"
                )

            # 7. Tier
            tier = manifest.get("quality_tier", "community")
            if tier not in VALID_TIERS:
                errors.append(f"Invalid quality_tier '{tier}'")
            elif tier not in SUBMITTABLE_TIERS:
                warnings.append(
                    f"Tier '{tier}' can only be assigned by maintainers. "
                    f"Use 'community' or 'experimental' for submissions."
                )

            # 8. Tags
            tags = manifest.get("tags", [])
            if not isinstance(tags, list):
                errors.append("tags must be a list")
            elif not tags:
                warnings.append("Empty tags — add keywords so people can find your agent")

        # 5. Class check
        has_basic_agent = False
        has_perform = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for base in node.bases:
                    base_name = ""
                    if isinstance(base, ast.Name):
                        base_name = base.id
                    elif isinstance(base, ast.Attribute):
                        base_name = base.attr
                    if base_name == "BasicAgent":
                        has_basic_agent = True
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        if item.name == "perform":
                            has_perform = True

        if not has_basic_agent:
            errors.append("No class inheriting BasicAgent found")
        if not has_perform:
            errors.append("No perform() method found")

        # 6. Security checks
        if self._has_hardcoded_secrets(code):
            errors.append("Possible hardcoded secret detected — use requires_env + os.environ.get()")

        if self._has_network_in_init(tree):
            warnings.append("Network call in __init__ — the Constitution says keep constructors fast")

        # 7. Docstring
        docstring = ast.get_docstring(tree)
        if not docstring:
            warnings.append("No module docstring — this serves as the agent's README")

        # Format report
        lines = [f"Validation: {path.name}", "=" * 50]
        if errors:
            lines.append(f"\n{len(errors)} ERROR(S):")
            for e in errors:
                lines.append(f"  x {e}")
        if warnings:
            lines.append(f"\n{len(warnings)} WARNING(S):")
            for w in warnings:
                lines.append(f"  ! {w}")
        if not errors and not warnings:
            lines.append("\nAll clear. This agent is ready to publish.")
        elif not errors:
            lines.append("\nNo errors — warnings are suggestions, not blockers.")
        else:
            lines.append("\nFix errors before publishing.")

        return "\n".join(lines)

    # ──────────────────────────────────────────────────────────
    # dry_run
    # ──────────────────────────────────────────────────────────

    async def _dry_run(self, **kwargs):
        path = self._resolve_path(kwargs.get("agent_path", ""))
        if not path:
            return "Error: agent_path is required for dry_run"
        if not path.exists():
            return f"File not found: {path}"

        run_kwargs = kwargs.get("dry_run_kwargs", {"task": "hello world"})

        code = path.read_text()
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            return f"Syntax error: {e}"

        # Find the class name
        class_name = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for base in node.bases:
                    name = ""
                    if isinstance(base, ast.Name):
                        name = base.id
                    elif isinstance(base, ast.Attribute):
                        name = base.attr
                    if name == "BasicAgent":
                        class_name = node.name
                        break

        if not class_name:
            return "No BasicAgent subclass found — cannot dry_run"

        # Execute in isolated namespace
        namespace = {}
        try:
            # Provide a BasicAgent stub
            exec(
                "class BasicAgent:\n"
                "    def __init__(self, *a, **kw): pass\n",
                namespace
            )
            exec(compile(tree, str(path), "exec"), namespace)
        except Exception as e:
            return f"Import error: {type(e).__name__}: {e}\n{traceback.format_exc()}"

        agent_cls = namespace.get(class_name)
        if not agent_cls:
            return f"Class {class_name} not found after exec"

        try:
            instance = agent_cls()
            result = instance.perform(**run_kwargs)
            # Handle both sync and async perform
            if hasattr(result, "__await__"):
                import asyncio
                result = await result
        except Exception as e:
            return (
                f"Runtime error in perform():\n"
                f"  {type(e).__name__}: {e}\n\n"
                f"{traceback.format_exc()}"
            )

        return (
            f"Dry run: {path.name}\n"
            f"  kwargs: {json.dumps(run_kwargs)}\n"
            f"  result: {result}"
        )

    # ──────────────────────────────────────────────────────────
    # diff
    # ──────────────────────────────────────────────────────────

    async def _diff(self, **kwargs):
        path = self._resolve_path(kwargs.get("agent_path", ""))
        if not path:
            return "Error: agent_path is required for diff"
        if not path.exists():
            return f"File not found: {path}"

        code = path.read_text()
        manifest = self._extract_manifest(ast.parse(code))
        if not manifest:
            return "No __manifest__ found — cannot determine registry name"

        name = manifest.get("name", "")
        if not name.startswith("@"):
            return f"Invalid name: {name}"

        # Fetch published version from RAPP registry
        parts = name.split("/")
        publisher = parts[0]
        slug = parts[1] if len(parts) > 1 else ""
        raw_url = (
            f"https://raw.githubusercontent.com/kody-w/RAR/main/"
            f"agents/{publisher}/{slug}.py"
        )

        try:
            import urllib.request
            req = urllib.request.Request(raw_url)
            token = os.environ.get("GITHUB_TOKEN", "")
            if token:
                req.add_header("Authorization", f"token {token}")
            with urllib.request.urlopen(req, timeout=10) as resp:
                published = resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return f"Agent {name} not found in the registry — this is a new agent."
            return f"Failed to fetch published version: {e}"
        except Exception as e:
            return f"Network error: {e}"

        # Compare
        local_lines = code.splitlines()
        published_lines = published.splitlines()

        if local_lines == published_lines:
            return f"No differences — local matches published version of {name}"

        # Simple line diff
        local_manifest = manifest
        pub_manifest = self._extract_manifest(ast.parse(published))

        diffs = []
        if pub_manifest and local_manifest:
            old_v = pub_manifest.get("version", "?")
            new_v = local_manifest.get("version", "?")
            if old_v == new_v:
                diffs.append(f"WARNING: Version unchanged ({old_v}). Bump before publishing.")
            else:
                diffs.append(f"Version: {old_v} -> {new_v}")

        diffs.append(f"Published: {len(published_lines)} lines")
        diffs.append(f"Local:     {len(local_lines)} lines")
        diffs.append(f"Delta:     {len(local_lines) - len(published_lines):+d} lines")

        return f"Diff: {name}\n" + "\n".join(f"  {d}" for d in diffs)

    # ──────────────────────────────────────────────────────────
    # publish
    # ──────────────────────────────────────────────────────────

    async def _publish(self, **kwargs):
        path = self._resolve_path(kwargs.get("agent_path", ""))
        if not path:
            return "Error: agent_path is required for publish"
        if not path.exists():
            return f"File not found: {path}"

        # Validate first
        validation = await self._validate(**kwargs)
        if "ERROR" in validation:
            return f"Cannot publish — fix errors first:\n\n{validation}"

        code = path.read_text()
        manifest = self._extract_manifest(ast.parse(code))
        name = manifest.get("name", "unknown")

        # Build the Issues-as-API payload
        payload = {
            "action": "submit_agent",
            "payload": {
                "code": code
            }
        }

        token = os.environ.get("GITHUB_TOKEN", "")
        if not token:
            return (
                "No GITHUB_TOKEN found. To publish:\n"
                "  1. Set GITHUB_TOKEN in your environment, or\n"
                "  2. Copy this payload and create a GitHub Issue manually:\n\n"
                f"```json\n{json.dumps(payload, indent=2)}\n```"
            )

        # Create the issue via GitHub API
        try:
            import urllib.request
            issue_data = json.dumps({
                "title": f"[submit] {name} v{manifest.get('version', '?')}",
                "body": f"```json\n{json.dumps(payload, indent=2)}\n```",
                "labels": ["agent-submission"],
            }).encode()

            req = urllib.request.Request(
                "https://api.github.com/repos/kody-w/RAR/issues",
                data=issue_data,
                headers={
                    "Authorization": f"token {token}",
                    "Accept": "application/vnd.github.v3+json",
                    "Content-Type": "application/json",
                },
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                result = json.loads(resp.read())
                issue_url = result.get("html_url", "")
        except Exception as e:
            return f"Failed to create submission issue: {e}"

        return (
            f"Submitted: {name} v{manifest.get('version', '?')}\n"
            f"Issue: {issue_url}\n\n"
            f"The RAPP automation pipeline will validate and merge your agent. "
            f"Watch the issue for status updates."
        )

    # ──────────────────────────────────────────────────────────
    # Helpers
    # ──────────────────────────────────────────────────────────

    def _resolve_path(self, raw: str) -> Path | None:
        if not raw:
            return None
        p = Path(raw)
        if p.is_absolute():
            return p
        return Path.cwd() / p

    def _extract_manifest(self, tree: ast.AST) -> dict | None:
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "__manifest__":
                        try:
                            return ast.literal_eval(node.value)
                        except (ValueError, TypeError):
                            return None
        return None

    def _has_hardcoded_secrets(self, code: str) -> bool:
        patterns = [
            r'(?:api[_-]?key|token|secret|password)\s*=\s*["\'][^"\']{8,}["\']',
            r'Bearer\s+[A-Za-z0-9\-._~+/]+=*',
            r'sk-[A-Za-z0-9]{20,}',
        ]
        for pattern in patterns:
            if re.search(pattern, code, re.IGNORECASE):
                return True
        return False

    def _has_network_in_init(self, tree: ast.AST) -> bool:
        network_calls = {"urlopen", "request", "get", "post", "fetch", "connect"}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        if item.name == "__init__":
                            for child in ast.walk(item):
                                if isinstance(child, ast.Call):
                                    func = child.func
                                    name = ""
                                    if isinstance(func, ast.Name):
                                        name = func.id
                                    elif isinstance(func, ast.Attribute):
                                        name = func.attr
                                    if name in network_calls:
                                        return True
        return False
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/616147kWJLlrzhyHnoGrCpqVYsBli7opFO6U3NqUEWttWbv/PvSIyKzeqa792kDiQh38l4zu8eOqcT96zdvGtOm//brtxejqqdL00cnPfKqbz99C6Mh6LN2zJr6eH2esjL86TR7ZRZ6Y/TTaYyG8aeTV4endvLLbEhPQ1YnZfRznJXR6UOal0T1OPxy0tPoFEZzVDZtdTw5BU3VevUh9xQ3/Wk83n6s/KXdTq03jlFf/3Loj1avasto+Pbrf/znT9+y4/O3X//6LSi94Xj0jXnvsJq+8KM6SD++HXtKr06Ol+12HKo+vrdRf6iovv1aT2X5X4eUehj7KXif6S3kX/7lJGVB3wxNPJ60oJnGUz/VY1ZFv9W/1XqaDafj39vA/jC/HzL/ONrnurZv8uhD0KmJT3/876IJt58X8OMgvy/f7frj8/BNnyVZ7ZUfsPxWfyx6S277aIj6OQpP/jYeyDX9z+8Pp6w+/fE/JP3+HaI/PjA/VrzNel34U+C1w1RGv7xNttKo/jIw8OpTtEbBdMgrm+BQ/nbM8NNxlKEp5+jYf1gwFFlZnsKsP87S9NuH7AOCX9/C/vjjD98b0t/qTzjR0ycfBvBY8MOc088/H6eIyyxJx9/qKEib01/++l9/Of2f0/9r14fwtw718OYXwIeFD02RT16fTG+aHNgf3oq88APgv/7XF5aHmDrqT4c7sjiLPjeXWV1E4XdgNY75GcGJkx/FbzofzGn68eDmKRt/OfHx6Ye9h9L3q+HkndJmGA+OtlEdHmhvh1TvOM4PJOtmPA3emA3x9tNpGqIPrX/4vfdhYvV7cCz/4yRd1NPYNOXx623mx6Jjc1NnB/w/3P75/BDS/2U4nb+L+OUkvyl2BEDvtWnvfemIvU+/HHHyffsh3DvV0fJb/Y6J6A2V9+bhJzzHogOZ4Muln8F4xFt1OHb4rvtjzRHE4UlvvEN5/1s9fHHZ69+uCJrDlO2UTEes10H0v74oNaTNVIYf+EWfcfvlhfDLKx8c/IjF04/QPP02IRCMnf4fCSQbP8w5Hfr/WQ75jMfo9CMevgfm3+aVqJ6zvqk/Pn/PLH8r8BPB7ynmt5ofT9Ph734YP9D5CKi3zqCp52PlO0l8t/733w8Es/gw+ffffzqdvSELPs750+krxfzrv31fesj6rU6jsh1OWzOdkuYU90118o/cVHzE4JseXznzQO7TqCU7guWAuIy8+U3Vty0/6PUZ2sfJ47JZjtA8neBfjrDy4rg53PFd7/3Lq5/s+DOlfmj3DrgPthyv39uRX3744cf2SxoFxen7KX86DdvBq/WdLrrp4FJ4mB6V4ZE/aq96W/g3IL1For+cwn77/U37HyJvX+nnT4gOAnpHINWh36yHyEPGGK3jBwkOci1fmeBIZ+NbJnbIzOL49PHz3cx37ei/p7RP8LzkA6iP3X8C20dJdmT77fSRuZv6LRH/5Ue1+iFRm/wqG/8sQ2/3fNBgzrwTPwxTNPzsDT8zKv/3JIzq42BB9DfcuRx4jNk4vYH59Yt9H14/gGtOR5j10Tj89NuRUQ4vjW9Jb1B+/z2rsw9qHXkw9PyPoA2PPWF0FLw3+ge3D5/1RzXl3xlpDNLowP2oQsfaavie6w4ztreIw7RPKD8heJfTMguiI8w/S+FP3w4vRn9XRt8V88g/VXQEyPCutof8w3ljFn1884LPZuCv/6M3+E7FX39klj8Z+Em/7+T7M/5/PQUfhPta9Bmen278Wwh/+s6qX38Us//Gpi8u/fRBlF8/O4sf7JiHP+nw0/ePh1O+HP7p5nenUU9Hi/AfP85xPPpu5rsP+jTg/enQ8YboU9C3oysZt/aN4oHx4ehvR4PxWbWPFJP+PUzq8fSt9U+mfYTn++j/+k5X33WCXxrBtz7wS9u/fftH2r6at/+pifl4fvrw8T/YFmbD4Y3t908O/M/N3HQkgZ9/8PDT0n8q6tPU34vlKNvD3wv7fP6R8T4qffM37gunt5TTn/h+SW/8d2f1lv7de//giE4z9af//WPBh4FD6wUHltEvyS+nv7wbsr/8Q9SGckr+AWYf53y/++BV7RXR78G7DH/Jq7bP7uUfy/xO8L+Xq3+9eZ/93Tm8Pf0jd39F1J8U/KgSx3evzf4Bvw5F39Pxe/HX7v/8R8gdKj87379+O8L58OXofQX0V9t6LO+9/ufhXdlB+BfoUHp8/zzj8e6fNLRfq4bUOzqsYxkE+TDtIxFN+RSOoSga+jEZUnRIYjQFxWiEYwEW4ySOxijsBTSE0kFMxVQUolCE+Nghbzg8GRxYH01K9tYMIUQMUz4G0WiERgFEBkiM4nQY0gRMYSgVQQjkQX7059Yiq8Ov43ya/wbqR2/9kbk+T/XXbz6BvSmODTzz+XMBAYj27dmXWzGmtWkhmfCRGUvt2bMNgTJmbSFyywEfYUvf8wAbYDMvvesWKxRae4ZNWEfJG0Be0RQMbJTfGYy5ARdR9EK5P/JVPeIP3rkyzs7s1dXJc0VE6btBb3SJeLaJLg8xLUAw91G6zvmmv978GcG2HAp2PFNeMZ6p5WMThMAFL3z7LHRDF0QgwKAsL0jUBuFsLnitz2h00rQBHzQneznXhL7EA5qHV47D7HTjLLN9jkDtGf6s28wt01CKu7kiKuOvvWkK/FHzzNN45E9Hgqandy/clk/SecdnUtOfrHuF5/VMknzSNlGmINi5kqSVkroXzBAmukUXzpEy1BHvti4+kD2jU7VPM7kmwsEw91vh50VjiNVjaGZoe9RSHM2MKV+wTNwbSC9iBt9fSatg4KtC7+rQBOMNux32vpbtPjOuvulu/PCX+1K/bG0vpyvxDEmCx3QTiiPNch9hWMP7hvF9GzmIY108HETImzTj+s2yGDTXs0BL76LK1dkjPN+WKzoF88VXyvIV8MUkyah6SZiwsJ4Cc5POj2vB1xCHCWdwH8FylPNM6pE0s9yA5W4KJWJMJLPQNmUqdJvryw7m4g27qrBXUFV4Y6fWLXQuH6C8QA7jFoi/RMl11OAINOmrkjUHK66jYIjMc5RFuwgAJb1kGKJy7D4TfbN3OvXUqht6uSouxpxjvhFxxnAoMxzFluna54OrnhRLSFF8o7G8uTxvLWY/XuyqUz4NiQAjFjfv2UbPM3lXcca30pctpNLECIsEXjcCJy7Ixj565ezPScK43OPh8MzrouMPWQ/RQdHYXXVZBVlhh34ITs7IYhBSvrTFO+s0cTWD8zOOLhLOjY6N4fNMlsIC2MquYTB1awTi7gnTmG9NfKzztDjFbwxXjsS9WGVyGCubebmjlJjZVWXXTtTOByOse8NZTAcyusR3rxrSmmFarev6Cgx5EEW1mVc8sG7zIAwrlQzPmdleRjAI9ANeYoKMcRCXFnlAE7WF685bg5svSUF2KR+Wzoj60uINv6dnoLFaXaSfEiVHOJNg4n4PjwlVTwUw31CDYhmps+0UX58ZEOqdlFCVSttF1VD8ubxJ3F4MT/E6NsNF46dbTN1ZdEeZ0TJfhH7Bwoiux6didIXnwwVkEy/XnzK0rvssA8U+X/iDGogK0YX06EywLR7gRuZAmj1ABsmMeZdA7BwCwcV6MTeYuhuBHU0vmxJV+0kyFLO4FiVD7g6DzwFjOV9x8QUmZwl1Lyije42p2fy9ZOBhs62kw5zbZjQey9iVmmb5LjuiGMEMmCAwr14vMgakNn/j1gKWZXKuwao2YEWfo5h7Pi4FsSdqjE0YPwWcyanLtooDyvoIEQIil6hUvHMguKOH5WAlpTdfizMILw0fFTFqtEQwqFPLMxbPp+5MKFAE5gTtpYlpdabHHanA8poSE9UbSzR5gYQfLFG4i9nU7ovIYXTLJUXp+4nWzmoRgJgCZP5t2LZwaEeR2033Ib8U1vOau1VfdbZIFTYVmpW/EcdqKxIrpYGrNHpRHsP61wU8O7mwijZojFhpApbng95jMAHMFwgkHUB70gad9Vl49qYlvNKLZagGvV7cpiEturQ1fRqJFZqTHvCNszXNFEW3uwGj6qZ4AgGjvZVOVmkFL6sT5TGFPPSRp3LbBjIMzB1pjKFLAghM2sSKCzMJS8smVitSAzJj+Eh43oEEHNjsJjGq64PMjI/XF3VuRM7Y+WqJMpdaN6mRl1ie54TbXXjQzOWB4pBMC0wjcADSTTyvswHkhEVr3Fm/Qodzh43To8QUzXVaNPDD3Ei7ZXxd7NpAp1VhRj4VBN+ZSS6q7Rg6L1Kw8Eqf3nZHekqtPAxs45oRKGXXmZHCi/4Qn9p6eCHwn5e2ZdkIlUlpYWRFzQXSj2gN2rioCEv5OVLkfc7OA+pRiM5upKnpinx4Dm39xVqJB9Ml2F1srBVq7kNZzoioEsB0Lc+B3iMFoDt1PaOjJdcUfLvQUt4PV4bKEc9JlIc6ZvDeX1/3eov5YnZgthq1Vrc8NAko5ajRZOYg3DS+GA+BlXvTAvv6ip+9DKPLfhYTFeN64sjKm3wVz+Dw7GNCuHahADz5qeGO7kWsLXNcGK7Qm0ZFQeQKHS3LTtMQyMmSFur+1MIxg6KsEAb1PUQRHO1fR7PQSllG3eXgdTsy6k5YoOCCfXkFUYUDpxfi3c/obVJj15kBYSHuUdExgMLXaz0yOggpd9ILcCjaHEq+EyW6PuIzJJQbPFCVPNHCY3chsur5YrftOuxZeyKHPHSQNUYe6mIrNukEzjbErOW57FqfsaxBCL2jzoWTetIGHW3dOGYU6OCKnrjM4itMai2XchObeE3I7Rmt/oArtyx/rmXkjGXQStZRO19P3atE8uDcTEBJnsdlyQrlwCF8mCTpDYXviQpM5xut6AVQratsF4CiN2QY6TmV3ni6xUIwtmEoqvNkDhdQrVsiuvprnWLhnOfMJlG+AD8Bo2xBUy6jBu/uPlZ2OdRcPe8pNS6bEs1K4CQajeAw5wlBPcBJX5CgbqFgw6fnzTPcq+jx7Lon9/gYtPlSFJwXV0C65TwxTTxaHotyMpjJKVzJN7MQDkYbUFEVXrKnlza8YvMtsQWp663ZV+0cpiJd88njb3BvGYSOchi/4EqEOi5NhPEewIEFnkckOCpxBjIse7nkfNfOzCxxFp9tBfa49RfmIpgwPEHt0B6JUCXdi89f92OAz6Yy9xlMcmUzfqRKP/KKy7Licxwy9aUJ8sNmJPxuBumQy/M5OSMt40yrNxXPrpeqKwbj2IWAVspySeVRqaLUi4Nph0QduSa54JZpoTW3a8bkS2lBbDXqmne3gMnFLQdXhDbfyVrThaixu0neqixXXz1abmStUtTyZxJPPPHJtn7cW5694HKmj57CZkzeGaan2XfI5H29czmPyB/PET5MmqlhXYm9evlBNaZd80LW3XHjLO6cs6v3fsqGBrLOqRdV6uKDHWRZpueTYZYyk88W0k0RhO0OsM65uwSPXLNfaI/cSSTsU2PIIXHzqzibgK6t10rRdbgfg1vXOsvdcBtRb91wNGkZZ7MJ6awnECoQfKeodhYzfnvtmmZ481iF4EvQtXCXbo8SnMzbFJC7f5G4GknguInIaJy3kuORNRBlkeLQB4L3PG0yIESKyXSfdOw5j8KyMCwvnFUwq6ezCLUQDg2u3Rf9ltsgWCgJ2C8MjQJ1zwCvoeBy1ECY0NWnBL/YySHXLDpHjerBd+KQDO7CvXY0hTXdxrCEmrCEazIFXe8LY+EBuHsL7+X54h00FGYABGrfvjAMZtcgiEAxpGI2xDwTwdTokgOCIaojaRpyuMeMlWXVIyOsT8Nz26sb3EtS4NUYSeqkfq5tOpl0B866mwr41KIYQjFhurgvFTP8MC0tpK6IPG5WP5oTPX8Qnsfp8KNppOIJGWfWkrU+gpwC61VZQq9dLBGT0WsVdNTKHtBs2qflcgSI8nJj1pcUUzpBNnRbMqvQCiRmJNt9gRtsuj2efMTFAHt/4N05oHnaE3NTjF8PzXq2/AivHQQB7LNDqdZ3hBfZOy0gMNsorAD8QthavzSKpFR3yiUd2XR3niQ5vCAKxvbt2KD5GyJYHU2yib7Yxn6PnUA5kxeHIp/ngCrx4aqUGqFNqCyzQJWY14LlKe0YpjjW9xst6zsXvw/8wJGuMNzN+eEzwDbonNSPYG/Eq5VXFvc4ei/m4XWUAK74s2H5MnfSDj8zWRhtUpF57TG1YTKCMWHdKNHE1s05cFE9LLhjKEnCxysvn+F1LGnXYLwFEVyxuWo39LzK4Hm3IMQsZaif6YpgmdhbQNDJKbhEcxnMHy2uylUDVA1aOBP12MHB3Fp+3kNYENGBTabtSfsR2A05uQEcus4IHF4Kug7dhwoZoax1REUvJn3Dey5Tmqxb4u0aNxaFFpejm+LdgcXzs84xpOijAXC0oyF2jaTr7i6rKN7s3CmCjKb5FjCnjdMzAW/ziyFpmMLDao3dCk9b4sCa3eWi6Qsse+ReSgIrvZp8o8pnmWwG8whmCPXkFrSxe38M5X7wAsUHxkha4VySm9b1q3MTE2qA2Fd2pCvEdukW7p6RHRWQMF0jTD0TlrZsz5cDIb2teGVm26qwZEI61DJnOMriHvVVsfjGQtYCeCpBaClHnahi79x4VsmOWLWHPhfdXwzOLelaIQnX94PEaixo3TzteNM0l7tLXy3KvYtnf1lbJI1x7WUInoHVhnm2KFC1bU94etcuuzGu3OGXBzqhhWqJ55QJxRCL1qMlvF/7DXmS186Z8RfS8x73AO+NJ9UFgvKeCtW+fpY2UgPYbiKkq4cfTSlnF2GuQ75N2p3aonKvXZPN67v7g3kVteold9Lqb53qTFJbdhUDXcapV4DlzExwb746+PnEsCxYNDjAEf26n2+vUNVNRAwZ3kU1TYv6kOwFX1UkrMvojQWdaHENqw9tR2OPKm7lwpRt0QAA6gOcwT3BVR2ilcql9q4Io+AVgAWqyZ39QMXKK7AWP5L36+j1ex3bYpGTgLt0xkQBAoG71bULGmLuhZ+vSGf6oHUtcgvz2doqmHVJU8cvWTihFAnqDPhejDV8fA1l+6IY5GyIznIZHY2Br2ZFlhZzyWb5bpz3ayhZLfK4gthitCiC7KzbPu8skfOuaxItgrIewnNDmkKsmtssyTgSvRL1LqWC8+g6bNaeR8tojzedWO2OR+70NVkR7VzkZTOb+r1dnBI3pbq8j/DV6BRKgPogB8WzdUQ6EPjDg2D4Iw02W3TX3U7vCrARLqxb6jlkkk+O3mpQ3ujETOMgU+ypqOgMo+VAEaoLc2VNorNHPESsSwLdiDub36q4oQA/VQxsxYeKiRPQrenyem+euD6OnplegZGN6UBRoXMFW/xwjD0QfDRJEQCxDehJLZSm53M4si1B0EJyY+bAKE3+lSXyJvJ74iRC31HekXenCqW5+LXPKr6gL5PwuxErvADydLumii3ZHy/nUWflsDrUxtWNoAOGfOmijG4lT+9e3sHuZFZ6Ih61bNXlZ661uRYGRY1NDzJ7bXkKr2Fh5dMIsJDZG8mAQGRo5eVylGJrT0fGg18U7PcgMt62Ri6bARU8hgej/hiXCxKI+bV89WwQXdPX9JAe7dkEKltsL3gYzSNuomoj0hqKtJoIJoHdJcV2U9EkHhNEfrUgIGwPoo3W2AFBfz1XXbe0BlI7T7o4krYBdAdotBAgsEOZhmHLjLO4YO5xyWrcGpKbQFTKk0qQGRW5h/rLS56cBdbN0dYimandpv3Z8EnjIZa2aW02Hh3fffcy8KVt3ZG3ozO1rZLyvHAb44QxHB0N/osE1YjY+TXFbFMLmCZ7xHysMPKrl27hGIkPl6mZZhB24XEMX5SjhLeyi5tGRJGd6JKZIjwHXH2elMTQGRAgye3dJf1XcnRWuW7qoznOezmhRJEmuHOJk1vPpZmy0MYL6IinBrG8F0e9MeZPw3aUaiSAS7AfOe024AzZkjyzuJHMJVeHxx/5dS81cimv1bDsz4vhamyRNTfElw1+rkfZnnEojSLLQaYrqXkkbscol6CPGLq/cjhinmdjjrlcQCo5nwZD9jIX4krMv4EYp14QpgK6s6TK9wuUETxjUvAGkTCHdU1zG3NvlQJGuSUSROqtgALTk/IHP43Qyh0XeOGIyKVZtgjplj1TRGigV4/Z9j7qp/pOYrtmVRQFjw8eLDCrZalcH47JC3GxKXxVGwOhsPd4aFtimCYFBSrCJQR6Y7iUb49uX9sNdEMdq5Wv3fHrJb/YxJwoLCywayksnKcIPG4XZkm8BmLxnxq73tFnt+VGrUS2Z2YXki1I+lyolzQFhMg0K0YW1PXCzbweXmfYlQ674peuTTTCL91gHOXZ4lothC3DEpUnjphd4dJMIyegP6gzLNWqOPTXp5GGWXQMHkrMIHV4fgZU3N0aiOkv9v5okM2VtQGzxIu9tM8E3c43a3q5ixFRS+QjrwAenwEJ8DflzjpupQs3gZGu0QVmAG9vdUC6lAQ9V5Av4PUrWtf0tieXIAgOWpPXITZv5is2WEXiyPNGqb6vxUU/tVphi/iaVg174bWaJKgKO3ooDSMSRghAJwgbmgaia1DzYsG8RjQpj2EVAXTW7JZhMhfRkYKEVNNJdMHGxd7z4n1YjMkBQCfr6KOHZyFkcXL0OAlQkSCt5g3AFpzZ6r3nHHl1jGJEaSvUfZWsE16m1QX95tY5YqPa5/mGSiADdIlCmwpzjSUBdkzmGEJv91rcL9LZveRq0e78ko4W27S5TJ07jRVo42kndvBqgyaqYMl0dW655WbV8KyvdH7+WmvLrxi/a9bzeAb6I1i0ZgGR8lbRZgGO1zNeeCxcUa5H4AKkNG5IDsDR5VjAnOEBVefKMYxq60IQAIcE0aBynHB4n5hyRHS7WKg99aFjvSuVfVRv15sC3oIdvQL8HpPnPTZHMbbIe1RbTsqlygD6xUAxOZebw9Go8gp8uZgT7wTdxd4QPG00PkzthR9qB/IebfBoAITlIxdgU1PTAwkr8g3zUeTeh6ImxIMZulGKsMRF8QXFZlMLIZcuGVeI9x446RfzS1mpuo5I3MgCaS0d+gIj/uiicrUHyYg5Dgt2F0nj2ntypS1F0ezn3gDrU64VoWVkXWd4G30O3nkC3BjVcXvLd2tnMNJsY+EuSg3eB6wmVGBgtEbPJcs2MG3fXjDFSdH0Qbx4AXYpiL4urhco9AOD9Nq1o7bGIXyZ1ORx8cXsiM8pFWefgZ7+FanPmH7ka0L0JroTJ9SbIMC/3p0BaAeeDlvxSkIyzsNb/pJpi+4nlImM+4sb8tU53+gcaW5qQLfQMy/7o2uRjPYYiPmuvVtuY9sWsWEUxHpQUDZF9NSIZEwuri9CwhCPtNYNFWp7CvrczVsM9Z4U4NrZl/JWdtCk9S1DCZIqvYdEhvE+G19u93UUELq9FalObtsW6kBzNp8twPPPZgcs2W/MJABtWiPrM+n0dPW8+kcMYFf5qAgCycWoYq+owgfCmgvbrpeRA0a2rgb3o6u3/ckrfOqOdBWpQPu1nEKzNWUYZ00rGflVx2DIp+dhNOtNIFXr1WyFLphTHaAKeJ7m7S42JhviJVoBN0UNbStP94Z5rk/buskqO93qKRmspSPwRA0hEA3M22bh4RhU2UrDlfLCTLV3GhTwqmnmLve+sNSFm8JERU0OU2BFHzj9WILmWjCit4FQHxQdqXNQP+yFUBFQucGcGgyFCuBqmxIsconU89DcsPClg/0GW3WertvrBcLItjWZANxVcJVY8jxR3HwL+FDK0H3GHCklOyJxzs4oP6kyOwbMCy6aS8jIyrMPl0u9EQFu64OMGICqgdMA1NAahXq53bl1bzXScWCKAu5iEFsKO/KsHWqDENZxv47DVvNp+pgkwBPCqxFXSRclUWlVpH6pZqpGJGM9WqL4rMCvGhFq4tEiDM0dWDVFgrdadG077e6G85aF6Bm+MRYlQkQuYI/2bj7EkgRyQTNfqAmzhqszhK3LNQyz1d3ttIUXyHj2BuI+VLQRSbcnWkJIsgplY9yYqcjdvoWuVZklUNzBg39/FIOXhhvckgeXX+ga3qBHogJtwZAEfAcuVTpOOs/2Uy/xrhmxHhs3IUHxipnp59YFJedu3AVMgD9mqDCTyYATEWKKvUQGLKjjUglHwGQRczL1XEuA7Q6EsIIBkeI8yOk2uaFuKimeMXZ2Ts+7fl8eyaDaY/2ksVodwjosFA+Sm/gKDIvqeEz9YFY6tZFq54pVLuFHRGX1ddRukkC/tJRCOR9tGqDGfLzX/D0lfYaOuesVEW4lGCRYaNOVx0L5c4xHXp440oDyRPKya2WwniqsTHsxkfRWjRVhpSBaVpV5DEbQOqV0/563cRUc5PskInpYuojacqOzMdsqttKZfLgr0QR3leZmfORsKmn0F4zXjUE+ZA/Xm4gcQ6JOHo9lhTx7v3H+bNJZd8xbteeNyLkSn3HOpMQgtppbTwTWSs4METuAKgv7MmZLDYymq4+gS1ROPM9H79xqVUMYJBtJzBgygAYEVIbdeTtOl3mFoXO90gDAsFeRuqiv5HVfXtDZr1OZoLH8Kr2YjcKa2zmlgzovSie9yzPBnmsUhLiJEBldNfZjjjUzxPa3q7t5Z4vwlTtVLjjdLXOJu7FM22bSWleODDnSPSbfNHk89/OUTrKVXVkwMRwOfFyYl8bUXof1NkFfHsnuPLTsCvN9EM7NdLU4WCaaGcsMGWom4eFYF1l6PSJBYDvthdaDSbiD3KoHq/N2EkmBnmru2gETplk8+GSCm/z0HBm9GYYah97KzLIz9zsA5kKtw/Em0qSLPKbKvqSy+OoBQ7uwVT4AEaXklQ9zHdXvMYE/3XnkF/eGUqmFVWfMtRBbCXliE/ObKOwwp9iAvt/X3QjDNa77mg9Kw2sj1lAsNMamBCuKoxN3z4/54YiyoQCve0cEfjSkS1MDLTpTfAHWQX0QHEDPwKCtgfNUaUUL3F2e4NtsEbB+xonz0Yl0uqGbHTlFrCNZFzA7UjMsPRQdrKnnw8I0CYmoOhmN1fFiswIHyLmh8jVUro3RtbF3jGyw5KnXcCgWowtFUG9dJB2rJ+5gCoiz+5liAjefqDvR8YPwrIXrHT8PYzLOHVpA/rXAWWrZ8sqqgGq93Agxt2bjAYY9BeaYGRyBSaPSktVlhM9xqZOs3Hjp4FX6qj338uCNIJjllHYL2kqDvxYyZzAIl011XPMDfR0faoHqaYbWwcxVQNrqBcaOwyshpUy5Tc8S4CwM7ilnx3u2z+i5laeAxPq76GW7JotuIIubY+C2VeH6lV7CMEcUO46uc23D4IprADSDWMbHwKWzsOGeAgAbxwim0nMtxjS1x2AW02Gsmx5EgUDH+IsUB3vdQyZNgwMJbtwMqnuCw2BEznk003AMxhQ4EvSrltfRlGCVPapTfvbuCKqIMW5AxDVo3faV7MVOJj3Di8nRiTk57QHt4ky5SwV1i4UqPVBHyoNS05sVS4d1ECb08bnD0Xj0v75kP+f4kpXmGSaiDnyRqH03Lhs/+sRTlcS4KwRhoXjoYVP53KPEMOEYbaIe0ksV1pI4qdHP6qVeaO+WmGdUEx67VzzvN6O1RGkEUukiXQHJrOSaRekBtsbdD+VK5e7P3upCJfFZsERgnYzNZ2nmPiyJ47M672PX9GXT4rdVb0Unpkt3BWHw1d/Je2c/GYb593//9tO391W3r3uH/+x2+/tSz/+3u0Wf14Ca+VBaB9H7xtT7VtuvH7p+/acW/OdP3/ogO/R/Xor6vC32cbno80rU5x2jn//2StSwfd4C/7zO+v2K5ei9b8T9x7f3/0w0TTkcC//bpq9LYO+bXT8uHH7eBntfjf58/HXB7f3lsOvrJuuHbfAvyLf/+r/oeMiAwDEAAA== -->
