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
    "name": "@kody/agent_workbench",
    "version": "1.1.0",
    "display_name": "Agent Workbench",
    "description": "Build, validate, test, and publish single-file RAPP agents. The development companion for the agent.py pattern.",
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

        from agents.basic_agent import BasicAgent


        class {class_name}(BasicAgent):
            def __init__(self):
                self.name = "{display_name}"
                self.metadata = {{
                    "name": self.name,
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
        from agents.basic_agent import BasicAgent


        class {class_name}(BasicAgent):
            def __init__(self):
                self.name = "{display_name}"
                self.metadata = {{
                    "name": self.name,
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
