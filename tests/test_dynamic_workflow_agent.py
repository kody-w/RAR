"""Tests for dynamic_workflow_agent.py: the library, the engine's ctx semantics, and - the reason it exists -
a run that survives its engine being killed. Uses fake_copilot.py instead of real model calls.
Run: python3 -m pytest tests/test_dynamic_workflow_agent.py   (DWF_AGENT=<path> tests another build of the agent)"""
import importlib.util
import json
import os
import shutil
import signal
import subprocess
import tempfile
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
AGENT = os.environ.get("DWF_AGENT") or os.path.join(os.path.dirname(HERE), "agents", "@kody-w", "dynamic_workflow_agent.py")
FAKE = os.path.join(HERE, "dynamic_workflow_fake_copilot.py")
HAVE_NODE = shutil.which("node") is not None
HAVE_LSOF = shutil.which("lsof") is not None
OBJ = {"type": "object", "required": ["ok"], "properties": {"ok": {"type": "boolean"}}}


def load():
    spec = importlib.util.spec_from_file_location("dwf_under_test", AGENT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def alive(pid):
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    out = subprocess.run(["ps", "-o", "stat=", "-p", str(pid)], capture_output=True, text=True).stdout.strip()
    return bool(out) and not out.startswith("Z")


@unittest.skipUnless(HAVE_NODE, "the engine needs node")
class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="dwf-test-")
        self.saved_env = dict(os.environ)
        os.environ.update({
            "RAPP_WORKFLOWS_HOME": os.path.join(self.tmp, "wf"), "RAPP_WORKFLOWS_COPILOT": FAKE,
            "COPILOT_EXTENSIONS_DIR": os.path.join(self.tmp, "ext"), "FAKE_STATE": os.path.join(self.tmp, "fake-state"),
            "FAKE_LOG": os.path.join(self.tmp, "fake.log"), "FAKE_HOME": os.path.join(self.tmp, "home"),
            "FAKE_PLAN": os.path.join(self.tmp, "plan.json")})
        self.m = load()
        self.plan({})
        self.runs = []

    def tearDown(self):
        for run_id in self.runs:
            d = self.run_dir(run_id)
            st = self.m._read_json(os.path.join(d, "state.json"), {}) or {}
            if st.get("pid") and alive(st["pid"]):
                os.kill(st["pid"], signal.SIGKILL)
            for f in os.listdir(os.path.join(d, "agents")) if os.path.isdir(os.path.join(d, "agents")) else []:
                rec = self.m._read_json(os.path.join(d, "agents", f)) if f.endswith(".json") else None
                if rec and rec.get("pid") and alive(rec["pid"]):
                    try:
                        os.killpg(rec["pid"], signal.SIGKILL)
                    except OSError:
                        pass
        os.environ.clear()
        os.environ.update(self.saved_env)
        shutil.rmtree(self.tmp, ignore_errors=True)

    def plan(self, p):
        with open(os.environ["FAKE_PLAN"], "w") as f:
            json.dump(p, f)

    def act(self, action, **kw):
        return self.m.dispatch(action, **kw)

    def save(self, name, run):
        return self.act("save", name=name, run=run, meta={"name": name, "description": "test workflow " + name, "phases": [{"title": "Work"}]})

    def start(self, name, **kw):
        run_id = self.act("run", name=name, **kw)["started"]
        self.runs.append(run_id)
        return run_id

    def run_dir(self, run_id):
        return os.path.join(os.environ["RAPP_WORKFLOWS_HOME"], "runs", run_id)

    def state(self, run_id):
        return self.m._state(self.run_dir(run_id))

    def wait(self, run_id, statuses=("completed", "error", "cancelled", "paused"), timeout=60):
        end, st = time.time() + timeout, {}
        while time.time() < end:
            st = self.state(run_id)
            if st.get("status") in statuses:
                return st
            time.sleep(0.2)
        log = open(os.path.join(self.run_dir(run_id), "engine.log")).read()[-3000:]
        self.fail("run did not reach %s: %s\n%s" % (statuses, st, log))

    def wait_for(self, what, fn, timeout=30):
        end = time.time() + timeout
        while time.time() < end:
            v = fn()
            if v:
                return v
            time.sleep(0.2)
        self.fail("timed out waiting for " + what)

    def calls(self, label=None):
        try:
            with open(os.environ["FAKE_LOG"]) as f:
                rows = [json.loads(line) for line in f]
        except FileNotFoundError:
            rows = []
        return [r for r in rows if label is None or r["label"] == label]

    def result(self, run_id):
        return self.act("result", run_id=run_id)["result"]

    def records(self, run_id):
        d = os.path.join(self.run_dir(run_id), "agents")
        return [self.m._read_json(os.path.join(d, f)) for f in sorted(os.listdir(d)) if f.endswith(".json")]


class LibraryTest(Base):
    def test_builtins_list_show_export_and_the_copilot_extension(self):
        names = [w["name"] for w in self.act("list")["workflows"]]
        self.assertIn("adversarial-fleet", names)
        shown = self.act("show", name="adversarial-fleet")
        self.assertEqual(shown["source"], "builtin")
        self.assertIn("dimensions", shown["args"])
        ex = self.act("export", name="adversarial-fleet")
        self.assertEqual(ex["operation"], "author")
        self.assertTrue(ex["run"].startswith("async (ctx) =>"))
        inst = self.act("install_copilot")
        self.assertTrue(os.path.isfile(inst["installed"]))
        self.assertIn("adversarial-fleet", inst["registers"])
        self.assertEqual(subprocess.run(["node", "--check", inst["installed"]], capture_output=True).returncode, 0)

    def test_save_versions_and_refusals(self):
        first = self.save("mine", "async (ctx) => { return 1; }")
        self.assertEqual(first["version"], "1.0.0")
        self.assertEqual(self.save("mine", "async (ctx) => { return 2; }")["version"], "1.0.1")
        for bad in (lambda: self.save("bad name!", "async (ctx) => 1"),
                    lambda: self.save("broken", "async (ctx) => { return ; ; }}"),
                    lambda: self.act("run", name="nope"),
                    lambda: self.act("status", run_id="nope"),
                    lambda: self.act("save", name="x", run="async () => 1", meta={"name": "y", "description": "d", "phases": []})):
            with self.assertRaises(self.m.WorkflowError):
                bad()
        refused = json.loads(self.m.DynamicWorkflowAgent().perform(action="run", name="nope"))
        self.assertEqual(refused["status"], "refused")

    def test_a_builtin_upgrade_never_overwrites_a_saved_workflow(self):
        self.save("adversarial-fleet", "async (ctx) => { return 'mine'; }")
        self.m.BUILTINS["adversarial-fleet"]["version"] = "9.9.9"
        self.m._sync_builtins()
        self.assertEqual(self.act("show", name="adversarial-fleet")["source"], "saved")

    def test_presets_merge_under_explicit_args(self):
        self.save("echo", "async (ctx) => ctx.args")
        self.act("save_preset", name="echo", preset="p1", args={"a": 1, "b": 2})
        run_id = self.start("echo", preset="p1", args={"b": 3})
        self.wait(run_id)
        self.assertEqual(self.result(run_id), {"a": 1, "b": 3})


class EngineTest(Base):
    def test_agents_schema_steps_memo_and_replay(self):
        self.plan({"a": [{"reply": 'Here you go:\n```json\n{"ok": true}\n```'}], "b": [{"reply": "hello"}], "c": [{"reply": "one", "sleep": 1}]})
        self.save("basic", """async (ctx) => {
          ctx.phase("Work");
          const a = await ctx.agent("give json", { label: "a", schema: %s });
          const b = await ctx.agent("give text", { label: "b" });
          const s = await ctx.step("stamp", () => ({ n: 1 }));
          const same = await ctx.parallel([() => ctx.agent("give text", { label: "b" }), () => ctx.agent("give text", { label: "b" })]);
          const twice = await ctx.parallel([() => ctx.agent("once", { label: "c" }), () => ctx.agent("once", { label: "c" })]);
          return { a, b, s, same, twice };
        }""" % json.dumps(OBJ))
        run_id = self.start("basic")
        st = self.wait(run_id)
        self.assertEqual(st["status"], "completed", st)
        self.assertEqual(self.result(run_id), {"a": {"ok": True}, "b": "hello", "s": {"n": 1}, "same": ["hello", "hello"], "twice": ["one", "one"]})
        self.assertEqual((len(self.calls("a")), len(self.calls("b")), len(self.calls("c"))), (1, 1, 1))
        self.assertTrue(self.calls("a")[0]["has_schema"])
        self.assertEqual(self.calls("a")[0]["cwd"], os.path.realpath(os.path.join(self.run_dir(run_id), "cwd")))
        self.assertIn("--disable-builtin-mcps", self.calls("a")[0]["argv"])
        # the same run again replays every settled result and spawns nothing
        st_path = os.path.join(self.run_dir(run_id), "state.json")
        with open(st_path) as f:
            st = json.load(f)
        st["status"] = "interrupted"
        with open(st_path, "w") as f:
            json.dump(st, f)
        self.act("resume", run_id=run_id)
        st = self.wait(run_id)
        self.assertEqual(st["status"], "completed")
        self.assertEqual(len(self.calls()), 3)
        self.assertEqual(st["agents"]["replayed"], 6)

    def test_a_reply_that_breaks_its_schema_is_asked_again_in_its_own_session(self):
        self.plan({"x": [{"reply": "I think it is fine."}, {"reply": '{"ok": false}'}]})
        self.save("retry", "async (ctx) => ({ v: await ctx.agent('p', { label: 'x', schema: %s }) })" % json.dumps(OBJ))
        run_id = self.start("retry")
        self.wait(run_id)
        self.assertEqual(self.result(run_id), {"v": {"ok": False}})
        first, second = self.calls("x")
        self.assertIsNone(first["resume"])
        self.assertIsNotNone(second["resume"])

    def test_an_agent_that_fails_resolves_null_and_the_run_goes_on(self):
        self.plan({"f": [{"reply": "", "exit": 1}]})
        self.save("fails", "async (ctx) => ({ got: await ctx.agent('p', { label: 'f' }) })")
        run_id = self.start("fails")
        st = self.wait(run_id)
        self.assertEqual((st["status"], self.result(run_id)), ("completed", {"got": None}))
        self.assertEqual(st["agents"]["failed"], 1)

    def test_parallel_pipeline_and_nested_workflow_semantics(self):
        self.save("sem", """async (ctx) => {
          const p = await ctx.parallel([() => 1, () => { throw new Error("x"); }, async () => 3]);
          const q = await ctx.pipeline([1, 2, 3], (v) => v * 10, (v, item) => { if (item === 2) throw new Error("no"); return v + item; });
          let nested = "allowed";
          try { await ctx.workflow("x"); } catch (e) { nested = "rejected"; }
          return { p, q, nested, args: ctx.args };
        }""")
        run_id = self.start("sem")
        self.wait(run_id)
        self.assertEqual(self.result(run_id), {"p": [1, None, 3], "q": [11, None, 33], "nested": "rejected", "args": {}})

    def test_pause_then_resume_continues_past_the_checkpoint(self):
        self.save("gate", "async (ctx) => { const a = await ctx.step('a', () => 1); await ctx.pause('review'); return { a, after: true }; }")
        run_id = self.start("gate")
        self.assertEqual(self.wait(run_id)["status"], "paused")
        self.act("resume", run_id=run_id)
        self.assertEqual(self.wait(run_id)["status"], "completed")
        self.assertEqual(self.result(run_id), {"a": 1, "after": True})

    def test_a_workflow_that_throws_is_an_error_with_its_reason(self):
        self.save("boom", "async (ctx) => { throw new Error('bad args'); }")
        run_id = self.start("boom")
        st = self.wait(run_id)
        self.assertEqual(st["status"], "error")
        self.assertIn("bad args", self.act("status", run_id=run_id)["error"])


    def test_replay_from_reuses_identical_settled_calls_and_nothing_else(self):
        self.plan({"same": [{"reply": "first"}], "changed": [{"reply": "v1"}, {"reply": "v2"}]})
        self.save("rr", """async (ctx) => ({ a: await ctx.agent("same prompt", { label: "same" }), b: await ctx.agent("old prompt", { label: "changed" }), s: await ctx.step("k", () => 1) })""")
        first = self.start("rr")
        self.wait(first)
        self.save("rr", """async (ctx) => ({ a: await ctx.agent("same prompt", { label: "same" }), b: await ctx.agent("new prompt", { label: "changed" }), s: await ctx.step("k", () => 2) })""")
        out = self.act("run", name="rr", replay_from=first)
        self.runs.append(out["started"])
        self.assertEqual(out["replayable_results"], 2)
        st = self.wait(out["started"])
        self.assertEqual(self.result(out["started"]), {"a": "first", "b": "v2", "s": 2})
        self.assertEqual((len(self.calls("same")), len(self.calls("changed"))), (1, 2))
        self.assertEqual(st["agents"]["replayed"], 1)
        with self.assertRaises(self.m.WorkflowError):
            self.act("run", name="rr", replay_from="no-such-run")


class CrashTest(Base):
    """The engine is killed mid-run (a crash, a restart): nothing finished is redone and nothing running is lost."""

    def slow_run(self, plan):
        self.plan(plan)
        self.save("slow", "async (ctx) => ({ v: await ctx.agent('work', { label: 'slow' }) })")
        run_id = self.start("slow")
        self.wait_for("the subagent to start", lambda: self.calls("slow"))
        return run_id

    def test_a_subagent_still_running_is_adopted_not_started_again(self):
        run_id = self.slow_run({"slow": [{"reply": "done", "sleep": 4}]})
        os.kill(self.state(run_id)["pid"], signal.SIGKILL)
        self.assertEqual(self.state(run_id)["status"], "interrupted")
        self.act("resume", run_id=run_id)
        st = self.wait(run_id)
        self.assertEqual((st["status"], self.result(run_id)), ("completed", {"v": "done"}))
        self.assertEqual(len(self.calls("slow")), 1)
        self.assertEqual(st["agents"]["adopted"], 1)

    @unittest.skipUnless(HAVE_LSOF, "naming a running session needs lsof")
    def test_a_killed_subagent_continues_in_its_own_session(self):
        run_id = self.slow_run({"slow": [{"reply": "partial", "sleep": 60}, {"reply": "finished"}]})
        rec = self.wait_for("its session to be named", lambda: [r for r in self.records(run_id) if r.get("session_id")])[0]
        os.kill(self.state(run_id)["pid"], signal.SIGKILL)
        os.killpg(rec["pid"], signal.SIGKILL)
        self.act("resume", run_id=run_id)
        st = self.wait(run_id)
        self.assertEqual(self.result(run_id), {"v": "finished"})
        again = self.calls("slow")[1]
        self.assertEqual((again["resume"], again["continue"]), (rec["session_id"], True))
        self.assertEqual(st["agents"]["resumed"], 1)

    def test_a_restart_signal_leaves_the_run_resumable_but_cancel_stops_it(self):
        run_id = self.slow_run({"slow": [{"reply": "done", "sleep": 3}]})
        os.kill(self.state(run_id)["pid"], signal.SIGTERM)
        self.assertEqual(self.wait(run_id, statuses=("interrupted",))["status"], "interrupted")
        self.act("resume", run_id=run_id)
        self.assertEqual(self.wait(run_id)["status"], "completed")
        self.assertEqual(len(self.calls("slow")), 1)

    def test_cancel_stops_the_engine_and_its_subagents(self):
        run_id = self.slow_run({"slow": [{"reply": "never", "sleep": 60}]})
        pid = self.calls("slow")[0]["pid"]
        out = self.act("cancel", run_id=run_id)
        self.assertEqual(self.wait(run_id, statuses=("cancelled",))["status"], "cancelled")
        self.wait_for("the subagent to stop", lambda: not alive(pid), timeout=10)
        self.assertIn("cancelled", out)
        self.assertFalse(self.act("resume", run_id=run_id)["resumed"])


class FleetTest(Base):
    def test_the_adversarial_fleet_runs_end_to_end_on_this_engine(self):
        finding = {"title": "T", "file": "x.py", "line": 3, "severity": "high", "scenario": "s", "kody_impact": "k", "repro": "r"}
        self.plan({
            "preflight": [{"reply": '{"ok": true, "notes": "all three worked"}'}],
            "review:a": [{"reply": json.dumps({"dimension": "a", "findings": [finding]})}],
            "review:b": [{"reply": '{"dimension": "b", "findings": []}'}],
            "refute:a-1": [{"reply": '{"isReal": true, "reproduced": true, "reason": "ran the probe"}'}],
            "triage": [{"reply": json.dumps({"units": [{"unit_id": "fix-one", "title": "Fix one", "finding_ids": ["a-1"], "files": ["x.py"], "plan": "p"}], "dropped": []})}],
            "build:fix-one": [{"reply": json.dumps({"status": "built", "branch": "r/fix-one", "commit": "abc1234", "worktree": "/w", "ab": {"fails_on_base": True, "passes_on_fix": True}, "summary": "fixed"})}],
            "prove:fix-one:0": [{"reply": '{"verdict": "proven", "reason": "A/B holds"}'}],
        })
        args = {"repo": "/r", "base": "abc", "frozen": "/f", "brief": "/b", "scratch_root": "/s", "build_root": "/w",
                "dimensions": [{"key": "a", "focus": "x"}, {"key": "b", "focus": "y"}]}
        run_id = self.start("adversarial-fleet", args=args)
        st = self.wait(run_id)
        self.assertEqual(st["status"], "completed", self.act("status", run_id=run_id))
        s = self.result(run_id)["summary"]
        self.assertEqual((s["reviewers_ok"], s["confirmed"], s["units"], s["proven"]), (2, 1, 1, 1))
        argv = lambda label: self.calls(label)[0]["argv"]
        self.assertEqual(argv("review:a")[argv("review:a").index("--model") + 1], "claude-opus-5.5")
        self.assertEqual(argv("refute:a-1")[argv("refute:a-1").index("--model") + 1], "gpt-5.6-sol")
        self.assertIn("long_context", argv("review:a"))
        self.assertEqual(self.act("status", run_id=run_id)["phase"], "Ledger")


class MountTest(Base):
    """mount: one hot-loadable tool per workflow, carrying its own workflow and engine."""

    def setUp(self):
        super().setUp()
        self.agents = os.path.join(self.tmp, "brainstem", "agents")
        os.makedirs(self.agents)
        with open(os.path.join(self.agents, "basic_agent.py"), "w") as f:
            f.write("class BasicAgent:\n    def __init__(self, name=None, metadata=None):\n        self.name, self.metadata = name, metadata\n")

    def load_mounted(self, path):
        spec = importlib.util.spec_from_file_location("mounted_" + str(len(self.runs)) + os.path.basename(path)[:-3], path)
        m = importlib.util.module_from_spec(spec)
        import sys
        sys.path.insert(0, self.agents)
        try:
            spec.loader.exec_module(m)
        finally:
            sys.path.remove(self.agents)
        return m

    def test_mount_writes_one_self_contained_tool_per_workflow(self):
        out = self.act("mount", name="adversarial-fleet", agents_dir=self.agents)
        self.assertEqual(out["tool"], "AdversarialFleetWorkflow")
        path = out["mounted"]
        self.assertTrue(path.endswith("adversarial_fleet_workflow_agent.py"))
        self.assertEqual(sorted(f for f in os.listdir(self.agents) if f.endswith("_agent.py") and f != "basic_agent.py"), ["adversarial_fleet_workflow_agent.py"])
        self.assertEqual([f for f in os.listdir(self.agents) if "mounting" in f], [])
        m = self.load_mounted(path)
        tools = [c for n, c in vars(m).items() if isinstance(c, type) and c.__module__ == m.__name__ and hasattr(c, "perform") and not n.startswith("_") and n != "BasicAgent"]
        self.assertEqual(len(tools), 1)
        a = tools[0]()
        self.assertEqual(a.name, "AdversarialFleetWorkflow")
        params = a.metadata["parameters"]
        self.assertEqual(params["type"], "object")
        self.assertIn("dimensions", params["properties"]["args"]["properties"])
        self.assertNotIn("mount", params["properties"]["action"]["enum"])
        self.assertEqual(m.__manifest__["display_name"], "AdversarialFleetWorkflow")
        self.assertIn("refused", a.perform(action="save"))
        shown = json.loads(a.perform(action="show"))
        self.assertEqual(shown["source"], "mounted")

    def test_a_mounted_tool_runs_the_workflow_it_carries_even_if_the_library_changes(self):
        self.save("tiny", "async (ctx) => ({ from: 'carried', args: ctx.args })")
        path = self.act("mount", name="tiny", agents_dir=self.agents)["mounted"]
        self.save("tiny", "async (ctx) => ({ from: 'library' })")
        a = self.load_mounted(path).DynamicWorkflowAgent()
        started = json.loads(a.perform(action="run", args={"k": 1}))
        self.runs.append(started["started"])
        self.wait(started["started"])
        self.assertEqual(self.result(started["started"]), {"from": "carried", "args": {"k": 1}})

    def test_unmount_removes_only_what_mount_wrote(self):
        path = self.act("mount", name="adversarial-fleet", agents_dir=self.agents)["mounted"]
        self.assertEqual(self.act("unmount", name="adversarial-fleet", agents_dir=self.agents)["unmounted"], path)
        self.assertFalse(os.path.exists(path))
        with open(path, "w") as f:
            f.write("# somebody's own agent\n")
        with self.assertRaises(self.m.WorkflowError):
            self.act("unmount", name="adversarial-fleet", agents_dir=self.agents)
        with self.assertRaises(self.m.WorkflowError):
            self.act("mount", name="adversarial-fleet", agents_dir=self.agents)
        self.assertTrue(os.path.exists(path))


    def test_hosted_in_a_brainstem_agents_folder_mount_needs_no_path(self):
        os.remove(os.path.join(self.agents, "basic_agent.py"))  # a bare Brainstem shims BasicAgent instead
        host = os.path.join(self.agents, "dynamic_workflow_agent.py")
        shutil.copy(AGENT, host)
        hosted = self.load_mounted(host)
        out = json.loads(hosted.DynamicWorkflowAgent().perform(action="mount", name="adversarial-fleet"))
        self.assertEqual(out.get("tool"), "AdversarialFleetWorkflow", out)
        self.assertTrue(os.path.exists(os.path.join(self.agents, "adversarial_fleet_workflow_agent.py")))
        elsewhere = os.path.join(self.tmp, "not-a-brainstem")
        os.makedirs(elsewhere)
        stray = os.path.join(elsewhere, "dynamic_workflow_agent.py")
        shutil.copy(AGENT, stray)
        refused = json.loads(self.load_mounted(stray).DynamicWorkflowAgent().perform(action="mount", name="adversarial-fleet"))
        self.assertEqual(refused["status"], "refused")


if __name__ == "__main__":
    unittest.main()
