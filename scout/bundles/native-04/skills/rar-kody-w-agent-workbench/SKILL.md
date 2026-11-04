---
name: "rar-kody-w-agent-workbench"
description: "Build, validate, test, and publish single-file RAPP agents. The development companion for the agent.py pattern."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/agent_workbench", "rar_sha256": "c0a0329cdb06728062ac11043d8989c1c1262c33f69f0afdf9d65e87f0d0575c", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.2", "author": "RAPP Core Team", "tags": ["devtools", "workbench", "scaffolding", "validation", "testing", "publishing"]}
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
