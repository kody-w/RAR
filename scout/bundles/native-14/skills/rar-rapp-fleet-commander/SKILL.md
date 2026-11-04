---
name: "rar-rapp-fleet-commander"
description: "Builds new RAR agents from a natural-language spec \u2014 plans, writes pytest tests, generates code via the Copilot CLI, iterates, and publishes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/fleet_commander", "rar_sha256": "2352d839c61457a7cd0d108e56d64814cff7f3dcdabe942d07404063e25016e4", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "RAPP", "tags": ["meta", "automation", "fleet", "ci", "tdd", "pipeline"]}
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
