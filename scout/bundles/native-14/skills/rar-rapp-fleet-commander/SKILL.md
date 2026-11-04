---
name: "rar-rapp-fleet-commander"
description: "Builds new RAR agents from a natural-language spec \u2014 plans, writes pytest tests, generates code via the Copilot CLI, iterates, and publishes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/fleet_commander", "rar_sha256": "2352d839c61457a7cd0d108e56d64814cff7f3dcdabe942d07404063e25016e4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "RAPP", "tags": ["meta", "automation", "fleet", "ci", "tdd", "pipeline"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `fleet_commander_agent.py` and embedded as the fenced Python below (sha256 2352d839c61457a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `fleet_commander_agent.py` first:

```bash
python3 fleet_commander_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 fleet_commander_agent.py   # or on stdin
python3 fleet_commander_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/fleet_commander_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/fleet_commander_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/fleet_commander/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
