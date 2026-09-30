// Simulates a dynamic-workflow run function against a mock ctx that follows the documented semantics
// (copilot-sdk/docs/workflows.md): agent() resolves null on ordinary failure, parallel/pipeline turn a
// throwing thunk/stage into null, labels make calls distinct. Usage: node sim.js <run.js>
const fs = require("fs");
const assert = require("assert");
const run = (0, eval)("(" + fs.readFileSync(process.argv[2], "utf8") + ")");

function harness(args, respond) {
  const calls = [];
  const logs = [];
  const ctx = {
    runId: "sim",
    args,
    signal: new AbortController().signal,
    phase: (t) => logs.push("PHASE " + t),
    log: (m) => logs.push(m),
    step: async (_k, p) => p(),
    pause: async () => {},
    workflow: async () => { throw new Error("nested workflows are not supported"); },
    parallel: async (thunks) => Promise.all(thunks.map(async (t) => { try { return await t(); } catch (e) { logs.push("THUNK THREW " + e.message); return null; } })),
    pipeline: async (items, ...stages) => Promise.all(items.map(async (item, i) => {
      let prev = item;
      for (const s of stages) {
        try { prev = await s(prev, item, i); } catch (e) { logs.push("STAGE THREW " + e.stack); return null; }
      }
      return prev;
    })),
    agent: async (prompt, opts) => {
      for (const k of Object.keys(opts)) assert.ok(["label", "schema", "model", "agent", "reasoningEffort", "contextTier"].includes(k), "bad option " + k);
      calls.push(opts.label);
      return respond(opts.label, prompt, opts);
    },
  };
  return { ctx, calls, logs };
}

const BASE = {
  repo: "/r", base: "abc1234", frozen: "/f", brief: "/b.md", scratch_root: "/s", build_root: "/w",
  product: "RAPP Buzz", user: "Kody", branch_prefix: "r12/", test_prefix: "tests/test_round12_", trailers: "T: 1",
};
const built = (slug, ok) => ({ status: "built", branch: "r12/" + slug, commit: "c0ffee" + slug.length, worktree: "/w/" + slug, ab: { fails_on_base: ok, passes_on_fix: true, evidence: "x" }, summary: "fixed " + slug });

async function scenario(name, args, respond, check) {
  const h = harness(Object.assign({}, BASE, args), respond);
  const out = await run(h.ctx);
  assert.deepStrictEqual(JSON.parse(JSON.stringify(out)), out, name + ": result is not plain JSON");
  const dup = h.calls.filter((c, i) => h.calls.indexOf(c) !== i);
  assert.deepStrictEqual(dup, [], name + ": duplicate labels would be memoized into one agent: " + dup);
  assert.ok(!h.logs.some((l) => l.startsWith("STAGE THREW") || l.startsWith("THUNK THREW")), name + ": a stage threw\n" + h.logs.join("\n"));
  check(out, h.calls, h.logs);
  console.log("ok  " + name + "  (" + h.calls.length + " agents)");
}

(async () => {
  await assert.rejects(run(harness(Object.assign({}, BASE, { dimensions: [] }), () => null).ctx), /dimensions to review, seeds to build/);
  await assert.rejects(run(harness(Object.assign({}, BASE, { brief: "" }), () => null).ctx), /missing string arg 'brief'/);
  console.log("ok  argument validation");

  await scenario("preflight gate halts before any spend", { dimensions: [{ key: "a", focus: "x" }] },
    (label) => (label === "preflight" ? { ok: false, notes: "git: bad revision" } : assert.fail("spent after a failed preflight: " + label)),
    (out, calls) => { assert.strictEqual(out.status, "halted"); assert.deepStrictEqual(calls, ["preflight"]); });

  await scenario("preflight null halts", { dimensions: [{ key: "a", focus: "x" }] }, () => null,
    (out, calls) => { assert.strictEqual(out.status, "halted"); assert.deepStrictEqual(calls, ["preflight"]); });

  const full = { dimensions: [{ key: "a", focus: "x" }, { key: "b", focus: "y" }, { key: "c", focus: "z" }], seeds: [{ unit_id: "seed-one", title: "S1", plan: "p" }], elsewhere: [{ unit_id: "far", title: "F" }] };
  await scenario("full governed run", full, (label, prompt, opts) => {
    if (label === "preflight") return { ok: true, notes: "fine" };
    if (label === "review:a") return { dimension: "a", findings: [1, 2, 3, 4, 5].map((i) => ({ title: "A" + i, file: "f.py", line: i, severity: "high", scenario: "s", kody_impact: "k", repro: "r" })) };
    if (label === "review:b") return { dimension: "b", findings: [] };
    if (label === "review:c") return null;
    if (label === "refute:a-1") { assert.strictEqual(opts.model, "gpt-5.6-sol"); return { isReal: true, reproduced: true, reason: "ran it" }; }
    if (label === "refute:a-2") return null;
    if (label === "refute:a-2:fallback") { assert.strictEqual(opts.model, "claude-opus-5.5"); return { isReal: false, reproduced: false, reason: "already fixed" }; }
    if (label === "refute:a-3") return { isReal: true, reproduced: false, reason: "could not trigger" };
    if (label === "refute:a-4") return { isReal: true, reproduced: true, reason: "ran it too" };
    if (label === "triage") {
      assert.ok(prompt.includes('"far"'), "triage must see the units built elsewhere");
      return { units: [{ unit_id: "Fix A1!!", title: "fix a1", finding_ids: ["a-1"], files: ["f.py"], plan: "p" }, { unit_id: "fix-a1", title: "dup slug", finding_ids: [], files: [], plan: "p" }], dropped: [] };
    }
    if (label === "build:fix-a1") { assert.ok(prompt.includes("worktree add /w/fix-a1 -b r12/fix-a1 abc1234") && prompt.includes("T: 1") && prompt.includes("tests/test_round12_fix_a1.py")); return built("fix-a1", true); }
    if (label === "prove:fix-a1:0") return { verdict: "held", reason: "vacuous" };
    if (label === "revise:fix-a1:1") return built("fix-a1", true);
    if (label === "prove:fix-a1:1") return { verdict: "proven", reason: "A/B holds" };
    if (label === "build:fix-a1-2") return { status: "declined", summary: "not real" };
    if (label === "build:a-4") return built("a-4", false);
    if (label === "revise:a-4:1") return built("a-4", true);
    if (label === "prove:a-4:1") return null;
    if (label === "prove:a-4:1:fallback") return { verdict: "proven", reason: "ok" };
    if (label === "build:seed-one") return built("seed-one", true);
    if (label === "prove:seed-one:0") return null;
    if (label === "prove:seed-one:0:fallback") return null;
    return assert.fail("unexpected agent " + label);
  }, (out, calls, logs) => {
    const s = out.summary;
    assert.deepStrictEqual([s.reviewers, s.reviewers_ok, s.findings, s.confirmed, s.refuted, s.unreproduced], [3, 2, 4, 2, 1, 1]);
    assert.deepStrictEqual([s.units, s.proven, s.held, s.declined, s.unproven], [4, 2, 0, 1, 1]);
    assert.ok(logs.some((l) => l.includes("dropped 1 finding(s) beyond the cap")), "the cap drop must be logged");
    assert.ok(logs.some((l) => l.includes("Triage left a-4 out")), "a finding triage forgot gets its own unit");
    assert.ok(logs.some((l) => l.includes("Triage left seed seed-one out")), "a seed triage forgot is kept");
    assert.ok(!calls.includes("prove:a-4:0"), "a builder whose own A/B failed is not sent to the prover");
    const byUnit = Object.fromEntries(out.units.map((u) => [u.unit, u.status]));
    assert.deepStrictEqual(byUnit, { "fix-a1": "proven", "fix-a1-2": "declined", "a-4": "proven", "seed-one": "unproven" });
    assert.strictEqual(out.errors.filter((e) => e.failed_stage === "review").length, 1);
  });

  await scenario("seeds only: no review, no triage", { dimensions: [], seeds: [{ unit_id: "s1", title: "S", plan: "p" }, { unit_id: "s2", title: "T", plan: "q" }] }, (label) => {
    if (label === "preflight") return { ok: true, notes: "" };
    if (label.startsWith("build:")) return built(label.slice(6), true);
    if (label.startsWith("prove:")) return { verdict: "proven", reason: "ok" };
    return assert.fail("unexpected agent " + label);
  }, (out, calls) => {
    assert.ok(!calls.some((c) => c.startsWith("review:") || c === "triage"));
    assert.deepStrictEqual([out.summary.units, out.summary.proven], [2, 2]);
  });

  await scenario("triage fails: one unit per confirmed finding plus seeds", { dimensions: [{ key: "a", focus: "x" }], seeds: [{ unit_id: "s1", title: "S", plan: "p" }] }, (label) => {
    if (label === "preflight") return { ok: true, notes: "" };
    if (label === "review:a") return { dimension: "a", findings: [{ title: "A", file: "f.py", line: 1, severity: "low", scenario: "s", kody_impact: "k", repro: "r" }] };
    if (label.startsWith("refute:")) return { isReal: true, reproduced: true, reason: "r" };
    if (label === "triage") return null;
    if (label.startsWith("build:")) return { status: "error", summary: "git lock" };
    return assert.fail("unexpected agent " + label);
  }, (out) => {
    assert.deepStrictEqual(out.units.map((u) => u.unit).sort(), ["a-1", "s1"]);
    assert.ok(out.errors.some((e) => e.failed_stage === "triage"));
    assert.deepStrictEqual(out.units.map((u) => u.status), ["error", "error"]);
  });

  await scenario("prover holds twice: held after one bounded revision", { dimensions: [], seeds: [{ unit_id: "s1", title: "S", plan: "p" }] }, (label) => {
    if (label === "preflight") return { ok: true, notes: "" };
    if (label === "build:s1" || label === "revise:s1:1") return built("s1", true);
    if (label.startsWith("prove:")) return { verdict: "held", reason: "moves the bug one layer over" };
    return assert.fail("unexpected agent " + label);
  }, (out, calls) => {
    assert.deepStrictEqual(calls, ["preflight", "build:s1", "prove:s1:0", "revise:s1:1", "prove:s1:1"]);
    assert.strictEqual(out.units[0].status, "held");
  });
  console.log("ALL SCENARIOS PASS");
})().catch((e) => { console.error(e); process.exit(1); });
