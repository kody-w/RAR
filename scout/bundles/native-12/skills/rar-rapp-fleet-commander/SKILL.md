---
name: "rar-rapp-fleet-commander"
description: "Builds new RAR agents from a natural-language spec \u2014 plans, writes pytest tests, generates code via the Copilot CLI, iterates, and publishes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/fleet_commander", "rar_sha256": "2ba26bb68c2fdaf8f75f5068fe244d227330e8ab96c7ee6516c6d2530b386487", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "RAPP", "tags": ["meta", "automation", "fleet", "ci", "tdd", "pipeline"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/fleet_commander`. The original RAPP
agent is preserved byte-for-byte in `fleet_commander_agent.py` and in the RCI capsule.

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

FleetCommander — Autonomous agent development pipeline.

Takes a natural-language description and runs the full lifecycle:
plan → write tests → generate code → run tests → iterate → publish.

Uses GitHub Copilot CLI as the LLM backend for code generation.
Designed for batch/fleet operation: queue multiple agent builds
and let them converge independently.

Drop this file into any RAPP brainstem's agents/ directory.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Pipeline stage. 'plan' produces a spec. 'test' writes pytest cases. 'build' generates the agent. 'run' executes tests and iterates. 'publish' pushes to RAR. 'full' runs the entire pipeline end-to-end.",
      "enum": [
        "plan",
        "test",
        "build",
        "run",
        "publish",
        "full"
      ],
      "type": "string"
    },
    "agent_name": {
      "description": "PascalCase name for the agent (auto-generated if omitted).",
      "type": "string"
    },
    "category": {
      "description": "Agent category for the registry.",
      "enum": [
        "general",
        "productivity",
        "sales",
        "support",
        "data",
        "automation",
        "integrations",
        "devtools"
      ],
      "type": "string"
    },
    "namespace": {
      "description": "RAR namespace (default @rapp).",
      "type": "string"
    },
    "plan_json": {
      "description": "JSON plan from a prior 'plan' step (used by build/test).",
      "type": "string"
    },
    "spec": {
      "description": "Natural-language description of the agent to build.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `fleet_commander_agent.py` and embedded as the fenced Python below (sha256 2ba26bb68c2fdaf8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `fleet_commander_agent.py` first:

```bash
python3 fleet_commander_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 fleet_commander_agent.py   # or on stdin
python3 fleet_commander_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
    "version": "1.0.1",
    "display_name": "FleetCommander",
    "description": (
        "Builds new RAR agents from a natural-language spec \u2014 plans, writes pytest tests, generates code via the Copilot CLI, iterates, and publishes."
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
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
