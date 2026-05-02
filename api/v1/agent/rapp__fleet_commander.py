"""
FleetCommander — Autonomous agent development pipeline.

Takes a natural-language description and runs the full lifecycle:
plan → write tests → generate code → run tests → iterate → publish.

Uses GitHub Copilot CLI as the LLM backend for code generation.
Designed for batch/fleet operation: queue multiple agent builds
and let them converge independently.

Drop this file into any RAPP brainstem's agents/ directory.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
from datetime import datetime
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/fleet_commander",
    "version": "1.0.0",
    "display_name": "FleetCommander",
    "description": (
        "Autonomous agent development pipeline. Accepts a natural-language spec, "
        "generates a plan, writes tests, builds the agent, iterates until tests pass, "
        "and publishes to the RAR registry. Uses Copilot CLI for code generation."
    ),
    "author": "RAPP",
    "tags": ["meta", "automation", "fleet", "ci", "tdd", "pipeline"],
    "category": "devtools",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {
        "args": {
            "action": "full",
            "spec": "An agent that fetches the top stories from Hacker News and summarizes them",
        }
    },
}

_COPILOT_BIN = shutil.which("copilot") or shutil.which("github-copilot-cli")
_MAX_FIX_ITERATIONS = 5


class FleetCommanderAgent(BasicAgent):

    def __init__(self):
        self.name = "FleetCommander"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["plan", "test", "build", "run", "publish", "full"],
                        "description": (
                            "Pipeline stage. 'plan' produces a spec. "
                            "'test' writes pytest cases. 'build' generates the agent. "
                            "'run' executes tests and iterates. 'publish' pushes to RAR. "
                            "'full' runs the entire pipeline end-to-end."
                        ),
                    },
                    "spec": {
                        "type": "string",
                        "description": "Natural-language description of the agent to build.",
                    },
                    "agent_name": {
                        "type": "string",
                        "description": "PascalCase name for the agent (auto-generated if omitted).",
                    },
                    "namespace": {
                        "type": "string",
                        "description": "RAR namespace (default @rapp).",
                    },
                    "category": {
                        "type": "string",
                        "enum": [
                            "general", "productivity", "sales", "support",
                            "data", "automation", "integrations", "devtools",
                        ],
                        "description": "Agent category for the registry.",
                    },
                    "plan_json": {
                        "type": "string",
                        "description": "JSON plan from a prior 'plan' step (used by build/test).",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

        self._agents_dir = self._find_agents_dir()
        self._workspace = None

    # ── routing ──────────────────────────────────────────────────────────

    def perform(self, **kwargs):
        action = kwargs.get("action", "full")
        spec = kwargs.get("spec", "") or kwargs.get("query", "")
        agent_name = kwargs.get("agent_name", "")
        namespace = (kwargs.get("namespace", "") or "rapp").lstrip("@")
        category = kwargs.get("category", "general")
        plan_json = kwargs.get("plan_json", "")

        if not spec and action != "publish":
            return json.dumps({"status": "error", "message": "No spec provided."})

        plan = json.loads(plan_json) if plan_json else None

        if action == "plan":
            return self._plan(spec, agent_name, namespace, category)
        elif action == "test":
            if not plan:
                plan = json.loads(self._plan(spec, agent_name, namespace, category))
            return self._write_tests(plan)
        elif action == "build":
            if not plan:
                plan = json.loads(self._plan(spec, agent_name, namespace, category))
            return self._build_agent(plan)
        elif action == "run":
            if not plan:
                plan = json.loads(self._plan(spec, agent_name, namespace, category))
            return self._run_tests(plan)
        elif action == "publish":
            return self._publish(spec, agent_name, namespace)
        elif action == "full":
            return self._full_pipeline(spec, agent_name, namespace, category)
        else:
            return json.dumps({"status": "error", "message": f"Unknown action: {action}"})

    # ── 1. PLAN ──────────────────────────────────────────────────────────

    def _plan(self, spec, agent_name="", namespace="rapp", category="general"):
        if not agent_name:
            agent_name = self._generate_name(spec)
        agent_name = self._sanitize_name(agent_name)
        snake = self._to_snake(agent_name)
        class_name = f"{agent_name}Agent"
        filename = f"{snake}_agent.py"

        params = self._infer_parameters(spec)
        tags = self._infer_tags(spec)
        imports = self._infer_imports(spec)

        plan = {
            "status": "ok",
            "action": "plan",
            "agent_name": agent_name,
            "class_name": class_name,
            "filename": filename,
            "snake_name": snake,
            "namespace": namespace,
            "category": category,
            "spec": spec,
            "parameters": params,
            "tags": tags,
            "imports": imports,
            "test_filename": f"test_{snake}_agent.py",
        }
        plan["message"] = (
            f"Plan ready: {class_name} ({filename})\n"
            f"Parameters: {', '.join(p['name'] for p in params)}\n"
            f"Tags: {', '.join(tags)}\n"
            f"Next: write tests, then build."
        )
        return json.dumps(plan)

    # ── 2. WRITE TESTS ──────────────────────────────────────────────────

    def _write_tests(self, plan):
        agent_name = plan["agent_name"]
        class_name = plan["class_name"]
        filename = plan["filename"]
        snake = plan["snake_name"]
        params = plan["parameters"]
        spec = plan["spec"]

        param_test_blocks = []
        for p in params:
            pname = p["name"]
            param_test_blocks.append(textwrap.dedent(f"""\
                def test_perform_with_{pname}(agent):
                    result = agent.perform({pname}="test value")
                    data = json.loads(result)
                    assert data["status"] in ("success", "ok"), f"Failed with {pname}: {{data}}"
            """))

        test_code = textwrap.dedent(f'''\
            """Tests for {class_name} — auto-generated by FleetCommander."""

            import json
            import sys
            import os
            import pytest

            sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
            sys.path.insert(0, os.path.dirname(__file__))

            from {snake}_agent import {class_name}


            @pytest.fixture
            def agent():
                return {class_name}()


            def test_instantiation(agent):
                assert agent.name == "{agent_name}"
                assert "description" in agent.metadata
                assert "parameters" in agent.metadata


            def test_metadata_has_required_fields(agent):
                meta = agent.metadata
                assert meta["name"] == "{agent_name}"
                params = meta["parameters"]
                assert params["type"] == "object"
                assert "properties" in params


            def test_has_perform_method(agent):
                assert callable(getattr(agent, "perform", None))


            def test_perform_returns_string(agent):
                result = agent.perform(query="test")
                assert isinstance(result, str), f"perform() returned {{type(result)}}, expected str"


            def test_perform_returns_valid_json(agent):
                result = agent.perform(query="test")
                data = json.loads(result)
                assert "status" in data, "Response missing 'status' field"


            def test_perform_empty_input(agent):
                result = agent.perform()
                assert isinstance(result, str)


            def test_manifest_exists():
                from {snake}_agent import __manifest__
                assert __manifest__["schema"] == "rapp-agent/1.0"
                assert __manifest__["name"].startswith("@")
                assert "version" in __manifest__
                assert "display_name" in __manifest__
                assert "description" in __manifest__
                assert "author" in __manifest__
                assert "tags" in __manifest__
                assert isinstance(__manifest__["tags"], list)


            def test_to_tool(agent):
                tool = agent.to_tool()
                assert tool["type"] == "function"
                assert tool["function"]["name"] == "{agent_name}"
                assert "description" in tool["function"]

        ''')

        for block in param_test_blocks:
            test_code += "\n" + block

        copilot_tests = self._copilot_generate_tests(plan)
        if copilot_tests:
            test_code += "\n# ── Copilot-generated scenario tests ──\n\n" + copilot_tests

        test_path = self._agents_dir / plan["test_filename"]
        test_path.write_text(test_code)

        return json.dumps({
            "status": "ok",
            "action": "test",
            "test_file": str(test_path),
            "test_count": test_code.count("def test_"),
            "message": f"Wrote {test_code.count('def test_')} tests to {plan['test_filename']}",
        })

    def _copilot_generate_tests(self, plan):
        if not _COPILOT_BIN:
            return ""
        try:
            prompt = (
                f"Generate 3 additional pytest test functions for a RAPP agent named "
                f"{plan['class_name']} that: {plan['spec'][:300]}\n\n"
                f"The agent class has a perform(**kwargs) method that returns a JSON string "
                f"with at least a 'status' field.\n"
                f"Parameters: {json.dumps([p['name'] for p in plan['parameters']])}\n\n"
                f"Rules:\n"
                f"- Each test uses a fixture called 'agent' that returns {plan['class_name']}()\n"
                f"- Tests must be self-contained (no network calls, no file I/O)\n"
                f"- Output ONLY the test functions, no imports or fixtures\n"
                f"- Each test name starts with test_\n"
                f"- Parse result with json.loads() and assert on the 'status' field"
            )
            result = subprocess.run(
                [_COPILOT_BIN, "--message", prompt],
                capture_output=True, text=True, timeout=30,
            )
            if result.returncode == 0 and result.stdout.strip():
                body = result.stdout.strip()
                if "```python" in body:
                    body = body.split("```python")[1].split("```")[0]
                elif "```" in body:
                    body = body.split("```")[1].split("```")[0]
                return body.strip()
        except Exception:
            pass
        return ""

    # ── 3. BUILD AGENT ───────────────────────────────────────────────────

    def _build_agent(self, plan):
        perform_body = self._generate_perform_body(plan)
        extra_imports = "\n".join(plan.get("imports", []))
        if extra_imports:
            extra_imports += "\n"

        params_block = self._build_params_block(plan["parameters"])
        safe_desc = plan["spec"].replace('"', '\\"').replace("\n", " ")[:200]
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M")

        lines = [
            '"""',
            plan["spec"],
            "",
            f"Auto-generated by FleetCommander on {date_str}.",
            "Drop this file into any RAPP brainstem's agents/ directory.",
            '"""',
            "",
            "import json",
        ]
        if extra_imports:
            lines.append(extra_imports.rstrip())
        lines += [
            "try:",
            "    from agents.basic_agent import BasicAgent",
            "except ImportError:",
            "    from basic_agent import BasicAgent",
            "",
            "",
            "__manifest__ = {",
            '    "schema": "rapp-agent/1.0",',
            f'    "name": "@{plan["namespace"]}/{plan["snake_name"]}",',
            '    "version": "1.0.0",',
            f'    "display_name": "{plan["agent_name"]}",',
            f'    "description": "{safe_desc}",',
            f'    "author": "{plan["namespace"]}",',
            f'    "tags": {json.dumps(plan["tags"])},',
            f'    "category": "{plan["category"]}",',
            '    "quality_tier": "community",',
            '    "requires_env": [],',
            '    "dependencies": ["@rapp/basic_agent"],',
            '    "example_call": {"args": {"query": "test"}},',
            "}",
            "",
            "",
            f"class {plan['class_name']}(BasicAgent):",
            "    def __init__(self):",
            f'        self.name = "{plan["agent_name"]}"',
            "        self.metadata = {",
            '            "name": self.name,',
            '            "description": __manifest__["description"],',
            '            "parameters": {',
            '                "type": "object",',
            f'                "properties": {{{params_block}',
            "                },",
            '                "required": [],',
            "            },",
            "        }",
            "        super().__init__(name=self.name, metadata=self.metadata)",
            "",
            "    def perform(self, **kwargs):",
            '        query = kwargs.get("query", "")',
            perform_body,
            "",
            "",
            'if __name__ == "__main__":',
            f"    a = {plan['class_name']}()",
            '    print(a.perform(query="test"))',
            "",
        ]

        code = "\n".join(lines)

        agent_path = self._agents_dir / plan["filename"]
        agent_path.write_text(code)

        return json.dumps({
            "status": "ok",
            "action": "build",
            "agent_file": str(agent_path),
            "class_name": plan["class_name"],
            "message": f"Built {plan['class_name']} → {plan['filename']}",
        })

    def _generate_perform_body(self, plan):
        if _COPILOT_BIN:
            try:
                params_list = ", ".join(p["name"] for p in plan["parameters"])
                prompt = (
                    f"Generate ONLY the body of a perform() method for a Python agent that: "
                    f"{plan['spec'][:400]}\n\n"
                    f"The method signature is: def perform(self, **kwargs)\n"
                    f"Available params via kwargs.get(): {params_list}\n"
                    f"'query' is always available as a local variable.\n\n"
                    f"Rules:\n"
                    f"- Return json.dumps(dict) with at least 'status' field\n"
                    f"- Use kwargs.get('param', '') for each parameter\n"
                    f"- Keep it functional — no placeholders or TODOs\n"
                    f"- No network calls in the default path (mock-friendly)\n"
                    f"- Indent body with 8 spaces (2 levels)\n"
                    f"- Do NOT include the def line"
                )
                result = subprocess.run(
                    [_COPILOT_BIN, "--message", prompt],
                    capture_output=True, text=True, timeout=30,
                )
                if result.returncode == 0 and result.stdout.strip():
                    body = result.stdout.strip()
                    if "```python" in body:
                        body = body.split("```python")[1].split("```")[0]
                    elif "```" in body:
                        body = body.split("```")[1].split("```")[0]
                    lines = body.strip().split("\n")
                    indented = "\n".join(
                        "        " + line.lstrip() if line.strip() else ""
                        for line in lines
                    )
                    if indented.strip():
                        return indented
            except Exception:
                pass

        return textwrap.indent(textwrap.dedent("""\
            if not query:
                return json.dumps({"status": "error", "message": "No query provided."})

            return json.dumps({
                "status": "success",
                "query": query,
                "result": f"Processed by {self.name}: {query}",
            })"""), "        ")

    def _build_params_block(self, params):
        if not params:
            return ""
        lines = []
        for p in params:
            lines.append(
                f'\n                "{p["name"]}": {{'
                f'\n                    "type": "{p.get("type", "string")}",'
                f'\n                    "description": "{p.get("description", p["name"])}"'
                f"\n                }},"
            )
        return "".join(lines)

    # ── 4. RUN TESTS ─────────────────────────────────────────────────────

    def _run_tests(self, plan):
        test_path = self._agents_dir / plan["test_filename"]
        agent_path = self._agents_dir / plan["filename"]

        if not test_path.exists():
            self._write_tests(plan)
        if not agent_path.exists():
            self._build_agent(plan)

        for iteration in range(1, _MAX_FIX_ITERATIONS + 1):
            passed, output = self._execute_pytest(test_path)
            if passed:
                return json.dumps({
                    "status": "ok",
                    "action": "run",
                    "passed": True,
                    "iterations": iteration,
                    "message": f"All tests passed on iteration {iteration}.",
                    "output": output[-2000:],
                })

            fixed = self._attempt_fix(plan, output, iteration)
            if not fixed:
                return json.dumps({
                    "status": "error",
                    "action": "run",
                    "passed": False,
                    "iterations": iteration,
                    "message": f"Tests still failing after {iteration} fix attempts.",
                    "output": output[-2000:],
                })

        return json.dumps({
            "status": "error",
            "action": "run",
            "passed": False,
            "iterations": _MAX_FIX_ITERATIONS,
            "message": f"Exhausted {_MAX_FIX_ITERATIONS} fix iterations.",
        })

    def _execute_pytest(self, test_path):
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pytest", str(test_path), "-v", "--tb=short", "-x"],
                capture_output=True, text=True, timeout=60,
                cwd=str(self._agents_dir),
                env={**os.environ, "LLM_FAKE": "1"},
            )
            output = (result.stdout + "\n" + result.stderr).strip()
            return result.returncode == 0, output
        except subprocess.TimeoutExpired:
            return False, "pytest timed out after 60s"
        except Exception as e:
            return False, f"pytest error: {e}"

    def _attempt_fix(self, plan, test_output, iteration):
        if not _COPILOT_BIN:
            return False

        agent_path = self._agents_dir / plan["filename"]
        if not agent_path.exists():
            return False

        current_code = agent_path.read_text()
        failures = self._extract_failures(test_output)

        prompt = (
            f"Fix this Python RAPP agent so the failing tests pass.\n\n"
            f"CURRENT CODE:\n```python\n{current_code[-3000:]}\n```\n\n"
            f"FAILING TESTS:\n{failures[-1500:]}\n\n"
            f"Rules:\n"
            f"- Return the COMPLETE fixed agent file (not a diff)\n"
            f"- Keep the same class name, agent name, and __manifest__\n"
            f"- perform() must return a JSON string with 'status' field\n"
            f"- Do not add network calls or file I/O\n"
            f"- Fix iteration {iteration}/{_MAX_FIX_ITERATIONS}"
        )
        try:
            result = subprocess.run(
                [_COPILOT_BIN, "--message", prompt],
                capture_output=True, text=True, timeout=45,
            )
            if result.returncode != 0 or not result.stdout.strip():
                return False

            body = result.stdout.strip()
            if "```python" in body:
                body = body.split("```python")[1].split("```")[0]
            elif "```" in body:
                body = body.split("```")[1].split("```")[0]

            body = body.strip()
            if not body or "class " not in body:
                return False

            agent_path.write_text(body)
            return True
        except Exception:
            return False

    def _extract_failures(self, output):
        lines = output.split("\n")
        relevant = []
        capture = False
        for line in lines:
            if "FAILED" in line or "ERROR" in line or "assert" in line.lower():
                capture = True
            if capture:
                relevant.append(line)
            if line.strip() == "" and capture and len(relevant) > 3:
                capture = False
        return "\n".join(relevant) if relevant else output[-1000:]

    # ── 5. PUBLISH ───────────────────────────────────────────────────────

    def _publish(self, spec, agent_name, namespace="rapp"):
        if not agent_name:
            agent_name = self._generate_name(spec)
        snake = self._to_snake(self._sanitize_name(agent_name))
        filename = f"{snake}_agent.py"
        agent_path = self._agents_dir / filename

        if not agent_path.exists():
            return json.dumps({
                "status": "error",
                "message": f"Agent file not found: {filename}. Run 'full' or 'build' first.",
            })

        rar_path = f"agents/@{namespace}/{filename}"

        return json.dumps({
            "status": "ok",
            "action": "publish",
            "filename": filename,
            "namespace": f"@{namespace}",
            "rar_path": rar_path,
            "agent_source": agent_path.read_text(),
            "message": (
                f"Agent ready for RAR.\n"
                f"  Path: {rar_path}\n"
                f"  Submit via PR to https://github.com/kody-w/RAR\n"
                f"  Or open an issue with the code at "
                f"https://github.com/kody-w/RAR/issues/new"
            ),
        })

    # ── 6. FULL PIPELINE ─────────────────────────────────────────────────

    def _full_pipeline(self, spec, agent_name="", namespace="rapp", category="general"):
        steps = []

        # Plan
        plan_result = self._plan(spec, agent_name, namespace, category)
        plan = json.loads(plan_result)
        if plan.get("status") != "ok":
            return plan_result
        steps.append({"step": "plan", "status": "ok"})

        # Write tests
        test_result = json.loads(self._write_tests(plan))
        steps.append({"step": "test", "status": test_result.get("status", "error")})

        # Build agent
        build_result = json.loads(self._build_agent(plan))
        steps.append({"step": "build", "status": build_result.get("status", "error")})

        # Run tests and iterate
        run_result = json.loads(self._run_tests(plan))
        steps.append({
            "step": "run",
            "status": "ok" if run_result.get("passed") else "error",
            "iterations": run_result.get("iterations", 0),
        })

        passed = run_result.get("passed", False)

        # Clean up test file
        test_path = self._agents_dir / plan["test_filename"]
        if test_path.exists():
            test_path.unlink()

        result = {
            "status": "ok" if passed else "error",
            "action": "full",
            "agent_name": plan["agent_name"],
            "filename": plan["filename"],
            "class_name": plan["class_name"],
            "passed": passed,
            "steps": steps,
            "data_slush": {
                "agent_name": plan["agent_name"],
                "filename": plan["filename"],
                "passed": passed,
            },
        }

        if passed:
            result["message"] = (
                f"Pipeline complete. {plan['class_name']} built and all tests passed.\n"
                f"Agent saved to agents/{plan['filename']}.\n"
                f"Ready to use — it will auto-load on next request."
            )
        else:
            result["message"] = (
                f"Pipeline finished but tests did not pass after "
                f"{run_result.get('iterations', 0)} iterations.\n"
                f"Agent saved to agents/{plan['filename']} — may need manual fixes.\n"
                f"Last output: {run_result.get('output', '')[-500:]}"
            )

        return json.dumps(result)

    # ── helpers ──────────────────────────────────────────────────────────

    def _find_agents_dir(self):
        here = Path(__file__).resolve().parent
        if here.name == "agents":
            return here
        candidate = here / "agents"
        if candidate.is_dir():
            return candidate
        return here

    def _generate_name(self, spec):
        if _COPILOT_BIN:
            try:
                result = subprocess.run(
                    [
                        _COPILOT_BIN, "--message",
                        f"Generate a short 1-2 word PascalCase name for an agent that: "
                        f"{spec[:200]}. Reply with ONLY the name, nothing else.",
                    ],
                    capture_output=True, text=True, timeout=10,
                )
                if result.returncode == 0 and result.stdout.strip():
                    name = re.sub(r"[^a-zA-Z]", "", result.stdout.strip().split("\n")[0])
                    if name and len(name) <= 30:
                        return name
            except Exception:
                pass

        words = spec.lower().split()
        stop = {
            "that", "this", "with", "from", "agent", "create", "make",
            "want", "should", "would", "could", "learn", "build", "about",
            "which", "their", "your", "they", "will", "does", "have",
            "into", "also", "been", "each", "when", "what", "some",
        }
        keywords = [w for w in words if len(w) > 3 and w not in stop]
        if keywords:
            return "".join(w.capitalize() for w in keywords[:2])
        return "Custom"

    def _sanitize_name(self, name):
        name = re.sub(r"[^a-zA-Z0-9]", "", name)
        if name and not name[0].isalpha():
            name = "Agent" + name
        if name:
            name = name[0].upper() + name[1:]
        return name or "Custom"

    def _to_snake(self, name):
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

    def _infer_parameters(self, spec):
        params = [{"name": "query", "type": "string", "description": "The user's request or input."}]
        lower = spec.lower()
        if any(w in lower for w in ["url", "link", "website", "page", "fetch"]):
            params.append({"name": "url", "type": "string", "description": "URL to access."})
        if any(w in lower for w in ["file", "read", "write", "path"]):
            params.append({"name": "path", "type": "string", "description": "File or directory path."})
        if any(w in lower for w in ["number", "count", "limit", "top", "max"]):
            params.append({"name": "count", "type": "integer", "description": "Number of results."})
        if any(w in lower for w in ["format", "output", "style"]):
            params.append({"name": "format", "type": "string", "description": "Output format."})
        return params

    def _infer_tags(self, spec):
        tags = []
        lower = spec.lower()
        tag_map = {
            "weather": "weather", "api": "api", "web": "web", "fetch": "web",
            "file": "filesystem", "data": "data", "search": "search",
            "email": "email", "database": "database", "sql": "database",
            "news": "news", "schedule": "scheduling", "summarize": "nlp",
            "translate": "nlp", "monitor": "monitoring", "slack": "messaging",
            "stock": "finance", "price": "finance", "image": "media",
            "github": "devtools", "git": "devtools", "deploy": "devops",
        }
        for keyword, tag in tag_map.items():
            if keyword in lower and tag not in tags:
                tags.append(tag)
        return tags or ["custom"]

    def _infer_imports(self, spec):
        imports = []
        lower = spec.lower()
        import_map = {
            ("http", "api", "fetch", "url", "web", "request"): "import urllib.request",
            ("html", "scrape", "parse"): "from bs4 import BeautifulSoup",
            ("csv", "spreadsheet"): "import csv",
            ("datetime", "date", "time", "timestamp"): "from datetime import datetime",
            ("regex", "pattern", "match"): "import re",
            ("file", "read", "write", "path"): "from pathlib import Path",
            ("random", "shuffle", "choice"): "import random",
            ("environment", "env"): "import os",
            ("subprocess", "command", "shell", "cli"): "import subprocess",
        }
        for keywords, stmt in import_map.items():
            if any(kw in lower for kw in keywords):
                if stmt not in imports:
                    imports.append(stmt)
        return imports


if __name__ == "__main__":
    a = FleetCommanderAgent()
    print(a.perform(
        action="plan",
        spec="An agent that fetches top Hacker News stories and summarizes them",
    ))
