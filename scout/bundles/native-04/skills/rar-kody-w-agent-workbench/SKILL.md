---
name: "rar-kody-w-agent-workbench"
description: "Build, validate, test, and publish single-file RAPP agents. The development companion for the agent.py pattern."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/agent_workbench", "rar_sha256": "00b19b2e98b854333dbf7d89d74980f3e54c4f5753f31ac9039cf8f8ed30e2b4", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "agent_workbench_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/agent-workbench:a14d527025538954d7fde085060c3a05ec1ab3cebbac89abb3090dc8fa76f23a", "kind": "skill"}, "version": "1.1.2", "author": "RAPP Core Team", "tags": ["devtools", "workbench", "scaffolding", "validation", "testing", "publishing"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/agent_workbench`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `agent_workbench_agent.py` is
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

<!-- rci-capsule:v1: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 -->
