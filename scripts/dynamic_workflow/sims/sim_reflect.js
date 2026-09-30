const fs = require("fs");
const assert = require("assert");
const run = (0, eval)("(" + fs.readFileSync(process.argv[2], "utf8") + ")");
function harness(args, respond) {
  const calls = [], logs = [], pauses = [];
  const ctx = {
    runId: "sim", args, signal: new AbortController().signal,
    phase: (t) => logs.push("PHASE " + t), log: (m) => logs.push(m),
    step: async (_k, p) => p(), pause: async (k) => { pauses.push(k); calls.push("PAUSE:" + k); },
    workflow: async () => { throw new Error("nested"); },
    parallel: async (th) => Promise.all(th.map(async (t) => { try { return await t(); } catch (e) { logs.push("THREW " + e.stack); return null; } })),
    pipeline: async () => { throw new Error("unused"); },
    agent: async (prompt, opts) => { calls.push(opts.label); return respond(opts.label, prompt, opts); },
  };
  return { ctx, calls, logs, pauses };
}
const BASE = { tool: "gemini", about: "Gemini CLI", contract: "/c.md", template: "/t.py", check_cmd: "check {file}", out_dir: "/o", scratch_root: "/s", roots: { data: ["~/.gemini"] } };
const hook = (id, need) => ({ id, need, hook: "h", kind: "file", where: "w", shape: "s", evidence: "e", confidence: "high" });
const buildSaw = [];
const good = (label, prompt) => {
  if (label === "preflight") return { ok: true, notes: "ok" };
  if (label.startsWith("recon:")) return label === "recon:code" ? null : { lens: label.slice(6), hooks: [hook("x", "n")], unknowns: [] };
  if (label === "map") return { hooks: [hook("Sessions!", "a"), hook("sessions", "b"), hook("state", "c"), hook("times", "d"), hook("proc", "e")], gaps: ["resume"], resume: "gemini --resume {id}" };
  if (label === "refute:sessions") return { holds: true, demonstrated: true, reason: "ran it" };
  if (label === "refute:sessions-2") return { holds: false, demonstrated: false, reason: "no", corrected: "a long correction that nobody demonstrated on real data" };
  if (label === "refute:times") return { holds: false, demonstrated: true, reason: "overstated", corrected: "started = startTime; last acted = newest message timestamp" };
  if (label === "refute:proc") return { holds: false, demonstrated: true, reason: "no such thing", corrected: "none" };
  if (label === "refute:state") return null;
  if (label === "refute:state:fallback") return { holds: true, demonstrated: false, reason: "read only" };
  if (label === "build") return (buildSaw.push(prompt), { status: "built", agent_file: "/o/gemini_beside_agent.py", tests_pass: true, check_pass: true, summary: "ok", covers: ["a"], gaps: [] });
  if (label === "prove:0") return { verdict: "proven", reason: "ok", live_counts: "12 lines" };
  return assert.fail("unexpected " + label);
};
async function sc(name, args, respond, check) {
  const h = harness(Object.assign({}, BASE, args), respond);
  const out = await run(h.ctx);
  assert.deepStrictEqual(JSON.parse(JSON.stringify(out)), out);
  const dup = h.calls.filter((c, i) => h.calls.indexOf(c) !== i);
  assert.deepStrictEqual(dup, [], name + ": duplicate labels " + dup);
  assert.ok(!h.logs.some((l) => l.startsWith("THREW")), name + "\n" + h.logs.join("\n"));
  check(out, h.calls, h.logs, h.pauses);
  console.log("ok  " + name + " (" + h.calls.length + " calls)");
}
(async () => {
  await assert.rejects(run(harness(Object.assign({}, BASE, { tool: "Bad Name" }), () => null).ctx), /lowercase/);
  await assert.rejects(run(harness(Object.assign({}, BASE, { roots: {} }), () => null).ctx), /give roots/);
  await sc("preflight gate", {}, (l) => (l === "preflight" ? { ok: false, notes: "no" } : assert.fail(l)), (o, c) => { assert.strictEqual(o.status, "halted"); assert.deepStrictEqual(c, ["preflight"]); });
  await sc("happy path", {}, good, (o, c) => {
    assert.strictEqual(o.summary.outcome, "proven");
    assert.deepStrictEqual([o.summary.lenses_ok, o.summary.hooks, o.summary.held, o.summary.corrected, o.summary.refuted], [3, 5, 2, 1, 2]);
    assert.deepStrictEqual(o.hooks.map((h) => h.id + ":" + h.status), ["sessions:holds", "sessions-2:refuted", "state:undemonstrated", "times:corrected", "proc:refuted"]);
    const saw = buildSaw[buildSaw.length - 1];
    assert.ok(saw.includes("newest message timestamp") && saw.includes("SUPERSEDES"), "the builder must get the correction");
    assert.ok(!saw.includes('"id": "proc"'), "a refuted hook never reaches the builder");
    assert.ok(o.summary.gaps.includes("resume"));
    assert.ok(!c.some((x) => x.startsWith("PAUSE")));
  });
  await sc("governor gate pauses before building", { gate: true }, good, (o, c, logs, pauses) => {
    assert.deepStrictEqual(pauses, ["hook-map-reviewed"]);
    assert.ok(c.indexOf("PAUSE:hook-map-reviewed") < c.indexOf("build"));
    assert.ok(c.indexOf("PAUSE:hook-map-reviewed") > c.indexOf("refute:sessions"));
  });
  await sc("nothing held: no build", {}, (l, p) => (l.startsWith("refute:") ? { holds: false, demonstrated: false, reason: "no" } : good(l, p)), (o, c) => {
    assert.strictEqual(o.reason, "no hook survived"); assert.ok(!c.includes("build"));
  });
  await sc("self-check fails -> revise -> proven", {}, (l, p) => {
    if (l === "build") return { status: "built", tests_pass: false, check_pass: true, summary: "x" };
    if (l === "revise:1") return { status: "built", tests_pass: true, check_pass: true, summary: "y" };
    if (l === "prove:1") return { verdict: "proven", reason: "ok" };
    return good(l, p);
  }, (o, c) => { assert.strictEqual(o.summary.outcome, "proven"); assert.ok(!c.includes("prove:0")); });
  await sc("held twice stays held", {}, (l, p) => {
    if (l.startsWith("prove:")) return { verdict: "held", reason: "writes outside its state" };
    if (l === "revise:1") return { status: "built", tests_pass: true, check_pass: true, summary: "y" };
    return good(l, p);
  }, (o, c) => { assert.strictEqual(o.summary.outcome, "held"); assert.deepStrictEqual(c.filter((x) => /^(prove|revise)/.test(x)), ["prove:0", "revise:1", "prove:1"]); });
  console.log("ALL REFLECT SCENARIOS PASS");
})().catch((e) => { console.error(e); process.exit(1); });
