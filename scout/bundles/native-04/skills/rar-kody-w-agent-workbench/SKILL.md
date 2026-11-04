---
name: "rar-kody-w-agent-workbench"
description: "Build, validate, test, and publish single-file RAPP agents. The development companion for the agent.py pattern."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/agent_workbench", "rar_sha256": "c0a0329cdb06728062ac11043d8989c1c1262c33f69f0afdf9d65e87f0d0575c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.2", "author": "RAPP Core Team", "tags": ["devtools", "workbench", "scaffolding", "validation", "testing", "publishing"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_workbench_agent.py` and embedded as the fenced Python below (sha256 c0a0329cdb067280…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_workbench_agent.py` first:

```bash
python3 agent_workbench_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_workbench_agent.py   # or on stdin
python3 agent_workbench_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/agent_workbench_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/agent_workbench_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/agent_workbench/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
