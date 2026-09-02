---
name: "rar-rapp-fleet-commander"
description: "Builds new RAR agents from a natural-language spec \u2014 plans, writes pytest tests, generates code via the Copilot CLI, iterates, and publishes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/fleet_commander", "rar_sha256": "2ba26bb68c2fdaf8f75f5068fe244d227330e8ab96c7ee6516c6d2530b386487", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "fleet_commander_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/fleet-commander:019697f8d61791dacd7c19df86d6e1e6075c80289b8f8d969fc1930cf5d5eef7", "kind": "skill"}, "version": "1.0.1", "author": "RAPP", "tags": ["meta", "automation", "fleet", "ci", "tdd", "pipeline"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/fleet_commander`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `fleet_commander_agent.py` is
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
