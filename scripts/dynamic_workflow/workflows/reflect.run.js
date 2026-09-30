async (ctx) => {
  const A = ctx.args || {};
  for (const k of ["tool", "about", "contract", "template", "check_cmd", "out_dir", "scratch_root"]) {
    if (typeof A[k] !== "string" || !A[k]) throw new Error("reflect: missing string arg '" + k + "'");
  }
  if (!/^[a-z][a-z0-9-]{1,30}$/.test(A.tool)) throw new Error("reflect: tool must be a lowercase name (letters, digits, '-')");
  const needs = Array.isArray(A.needs) && A.needs.length ? A.needs : [
    "every session: its own id, title, working folder, when it started and last acted",
    "every message: who said it (the person or the AI), what, and when (the tool's own timestamp)",
    "its state now: working, waiting on the person, idle, stopped, or interrupted by a crash or restart",
    "whether a person started it (interactive) or a script did",
    "the exact command that brings a session back as it was",
  ];
  const roots = A.roots && typeof A.roots === "object" ? A.roots : {};
  if (!Object.values(roots).some((v) => Array.isArray(v) && v.length)) throw new Error("reflect: give roots: {name: [paths where the tool's code, data or docs live]}");

  // Static bounds (RAR @rapp/swarm_factory hard rule 4).
  const MAX_HOOKS = 12;
  const MAX_REVISIONS = 1;
  const PRODUCT = A.product || "RAPP Buzz";
  const USER = A.user || "the user";
  const OPUS = { model: "claude-opus-5.5", reasoningEffort: "max", contextTier: "long_context" };
  const SOL = { model: "gpt-5.6-sol", reasoningEffort: "max", contextTier: "long_context" };
  const M = Object.assign({ recon: OPUS, map: OPUS, refute: SOL, build: OPUS, prove: SOL, fallback: OPUS }, A.models || {});
  const ledger = { preflight: null, recon: [], map: null, hooks: [], build: null, proof: null, errors: [] };
  const oneLine = (s, n) => String(s == null ? "" : s).replace(/\s+/g, " ").trim().slice(0, n || 140);
  const failed = (stage, label) => {
    ledger.errors.push({ failed_stage: stage, label: label });
    ctx.log("ERROR at " + stage + " (" + label + "): the agent returned nothing");
    return null;
  };
  const tiered = async (prompt, label, tier, schema) => {
    const first = await ctx.agent(prompt, Object.assign({ label: label, schema: schema }, M[tier]));
    if (first !== null) return { value: first, model: M[tier].model };
    ctx.log("fallback: " + label + " got nothing from " + M[tier].model + "; asking " + M.fallback.model);
    const second = await ctx.agent(prompt, Object.assign({ label: label + ":fallback", schema: schema }, M.fallback));
    return { value: second, model: second === null ? null : M.fallback.model };
  };
  const agentFile = A.out_dir + "/" + A.tool.replace(/-/g, "_") + "_beside_agent.py";
  const testFile = A.out_dir + "/test_" + A.tool.replace(/-/g, "_") + "_beside.py";

  const RULES = [
    "Rules (they bind every subagent in this workflow):",
    "- You are one of several subagents reverse-engineering '" + A.tool + "' on " + USER + "'s Mac, at the same time. You cannot ask questions: do the job, then return the JSON.",
    "- READ-ONLY on the tool: never start a model session of it or of any AI CLI (--version / --help only), never write inside its folders, never send anything anywhere.",
    "- Its data is " + USER + "'s work: report file layouts, field NAMES, counts, value TYPES and 8-character id prefixes - never message text, titles, prompts or file contents. Fixtures you write are synthetic: made-up text in the real shape.",
    "- Write only under your scratch folder (and, for the builder, the output folder). Never under /tmp.",
    "- Errors are data: if something fails, say exactly what in your JSON.",
  ].join("\n");

  const HOOK = {
    type: "object",
    required: ["need", "hook", "kind", "where", "shape", "evidence"],
    properties: {
      need: { type: "string" },
      hook: { type: "string" },
      kind: { type: "string", enum: ["file", "field", "event", "process", "socket", "api", "flag", "other"] },
      where: { type: "string" },
      shape: { type: "string" },
      lifecycle: { type: "string" },
      evidence: { type: "string" },
      confidence: { type: "string", enum: ["high", "medium", "low"] },
    },
  };
  const RECON_SCHEMA = { type: "object", required: ["lens", "hooks"], properties: { lens: { type: "string" }, hooks: { type: "array", items: HOOK }, unknowns: { type: "array", items: { type: "string" } }, notes: { type: "string" } } };
  const MAP_SCHEMA = {
    type: "object",
    required: ["hooks", "gaps"],
    properties: {
      hooks: { type: "array", items: Object.assign({}, HOOK, { required: HOOK.required.concat(["id"]), properties: Object.assign({ id: { type: "string" } }, HOOK.properties) }) },
      gaps: { type: "array", items: { type: "string" } },
      resume: { type: "string" },
      alive: { type: "string" },
    },
  };
  const VERDICT_SCHEMA = { type: "object", required: ["holds", "demonstrated", "reason"], properties: { holds: { type: "boolean" }, demonstrated: { type: "boolean" }, reason: { type: "string" }, corrected: { type: "string" }, counts: { type: "string" } } };
  const BUILD_SCHEMA = {
    type: "object",
    required: ["status", "summary"],
    properties: {
      status: { type: "string", enum: ["built", "declined", "error"] },
      agent_file: { type: "string" },
      test_file: { type: "string" },
      tests_pass: { type: "boolean" },
      check_pass: { type: "boolean" },
      live_dry_run: { type: "string" },
      idempotent: { type: "boolean" },
      covers: { type: "array", items: { type: "string" } },
      gaps: { type: "array", items: { type: "string" } },
      summary: { type: "string" },
    },
  };
  const PROVE_SCHEMA = { type: "object", required: ["verdict", "reason"], properties: { verdict: { type: "string", enum: ["proven", "held"] }, tests_real: { type: "boolean" }, check_pass: { type: "boolean" }, read_only: { type: "boolean" }, idempotent: { type: "boolean" }, live_counts: { type: "string" }, reason: { type: "string" } } };
  const PRE_SCHEMA = { type: "object", required: ["ok", "notes"], properties: { ok: { type: "boolean" }, notes: { type: "string" } } };

  const LENSES = [
    { key: "docs", ask: "its OWN documentation shipped with the installed tool (READMEs, docs/, .d.ts or type files, changelogs, --help of every subcommand) and its public docs: documented session storage, event formats, resume/continue flags, hooks or extension points." },
    { key: "disk", ask: "its data on disk: which folders and files it writes, their formats, the field names in each record type, how a session's files are named and found, when files are created, appended, rewritten or deleted (watch mtimes), and counts per type. Field names and counts only." },
    { key: "code", ask: "its installed code or binary: fixed-string searches (Python mmap find - a regex grep over a large binary hangs) for file names, record/event type names, schema keys, and flags such as resume/continue/session. Confirm what the docs claim and find what they do not say." },
    { key: "process", ask: "how it runs: its processes and their arguments shapes, open files and sockets (lsof -w -n -P), how to tell a session is alive, busy, or waiting on the person, and how a session is brought back exactly (flags, folder, model)." },
  ];
  const reconPrompt = (lens) => [
    "You are the '" + lens.key + "' lens reverse-engineering a locally run AI tool so that " + PRODUCT + " can record it: '" + A.tool + "' - " + A.about,
    "Look at: " + lens.ask,
    "Where to start (not exhaustive): " + JSON.stringify(roots),
    "What " + PRODUCT + " needs to latch onto:",
    needs.map((n) => " - " + n).join("\n"),
    "The contract the result must feed (read it): " + A.contract,
    "Your scratch folder: " + A.scratch_root + "/recon-" + lens.key + "/",
    "",
    "Return hooks: each names the need it serves, the hook (what to read), its kind, where it lives, its shape (fields/types), its lifecycle, the EVIDENCE (the command you ran and what it showed, counts only) and your confidence. List unknowns plainly. At most " + MAX_HOOKS + " hooks.",
    "",
    RULES,
    "",
    "Return ONLY the JSON object.",
  ].join("\n");
  const mapPrompt = (recon) => [
    "You are the MAP step: merge four reverse-engineering lenses on '" + A.tool + "' (" + A.about + ") into ONE hook map for " + PRODUCT + ".",
    "For every need, keep the most reliable hooks (prefer the tool's own records over inference; prefer documented over undocumented when both hold), give each a short id, and say how to read it. Name what no lens could satisfy in gaps. State how to tell a session is alive (alive) and the exact bring-back command (resume, with placeholders), if found.",
    "Needs:",
    needs.map((n) => " - " + n).join("\n"),
    "Contract (read it; the hooks must be enough to write a beside agent that follows it): " + A.contract,
    "",
    "The lenses' reports (JSON):",
    JSON.stringify(recon, null, 1),
    "",
    RULES,
    "",
    "At most " + MAX_HOOKS + " hooks. Return ONLY the JSON object.",
  ].join("\n");
  const refutePrompt = (h) => [
    "You are the REFUTER for one hook in a reverse-engineering map of '" + A.tool + "'. DISPROVE it: holds=false if you can.",
    "It holds only if you DEMONSTRATE it on this Mac's real data by running something (demonstrated=true only then): the file or record exists with this shape, the field means what is claimed, the lifecycle is as described. Counts and field names only.",
    "Your scratch folder: " + A.scratch_root + "/refute-" + h.id + "/",
    "If the mechanism holds with a different shape or meaning, say so in corrected.",
    "",
    "The hook (JSON):",
    JSON.stringify(h, null, 1),
    "",
    RULES,
    "",
    "Return ONLY the JSON object.",
  ].join("\n");
  const buildPrompt = (map, hooks) => [
    "You are the BUILDER: write the beside agent that lets " + PRODUCT + " record '" + A.tool + "' (" + A.about + ").",
    "Follow the contract exactly (read it first): " + A.contract,
    "Start from the template (copy it, then fill it in): " + A.template,
    "Write: " + agentFile + " and its tests " + testFile + " (stdlib unittest, Python 3.9). Create the folder if needed.",
    "",
    "Work test-first:",
    " 1. Build SYNTHETIC fixtures in the real shapes the hooks below describe (made-up text, never copied content) inside the test file or a fixtures folder next to it.",
    " 2. Write tests that fail first: look() on the fixtures yields the right lines (agent ids, roles, who said it, created_at from the tool's own timestamps, state), a second look() with the returned state yields nothing new, a new record appended yields exactly its line.",
    " 3. Implement look(). Stdlib only, read-only, fast (seconds), deterministic created_at.",
    " 4. Run the tests: they must pass. Run the contract check: " + A.check_cmd.replace("{file}", agentFile) + " - it must pass.",
    " 5. Dry-run look() on the REAL data (read-only) and report only counts of lines per kind and state, plus 8-character id prefixes.",
    "A hook whose status is 'corrected' was demonstrated on real data but overstated: its verdict.corrected SUPERSEDES the hook's own claims - build from the correction, and handle the cases the refuter's reason names.",
    "Declare in covers which needs it serves and in gaps which it cannot. If the hooks cannot support a correct agent, return status 'declined' with the reason.",
    "",
    "The hook map after refutation (hooks that held, and hooks corrected by their refuter) (JSON):",
    JSON.stringify({ map: map, hooks: hooks }, null, 1),
    "",
    RULES,
    "",
    "Return ONLY the JSON object.",
  ].join("\n");
  const provePrompt = (b, attempt) => [
    "You are the PROVER for a generated beside agent for '" + A.tool + "'. Assume it is wrong until shown otherwise: verdict 'held' if you can.",
    "Agent: " + (b.agent_file || agentFile) + "  Tests: " + (b.test_file || testFile) + "  Contract: " + A.contract,
    "Your scratch folder: " + A.scratch_root + "/prove-" + attempt + "/ - copy the agent and tests there; never edit the originals.",
    "Prove by running:",
    " 1. The tests pass - and are real: break one fixture field the agent depends on (in your copy) and a test must fail.",
    " 2. The contract check passes: " + A.check_cmd.replace("{file}", b.agent_file || agentFile),
    " 3. Read-only: run look() on the real data while watching that nothing is written anywhere but its returned state (compare mtimes of the tool's folders before and after).",
    " 4. Idempotent: look() twice on the real data - the second, given the first's state, yields no new lines; and lines are identical (same created_at, content) when replayed from an empty state.",
    " 5. The live counts are sane against what the tool's own files hold (counts only).",
    "",
    "The builder's report (JSON):",
    JSON.stringify(b, null, 1),
    "",
    RULES,
    "",
    "Return ONLY the JSON object.",
  ].join("\n");

  ctx.phase("Preflight");
  const pre = await ctx.agent([
    "Preflight for a reverse-engineering workflow. Run exactly these and nothing else, and report:",
    " 1. ls -d " + Object.values(roots).flat().map((p) => JSON.stringify(p)).join(" ") + " (which of these exist)",
    " 2. test -f " + JSON.stringify(A.contract) + " && test -f " + JSON.stringify(A.template) + " && echo contract-and-template-ok",
    " 3. mkdir -p " + JSON.stringify(A.out_dir) + " " + JSON.stringify(A.scratch_root) + " && touch " + JSON.stringify(A.out_dir + "/.preflight") + " && rm " + JSON.stringify(A.out_dir + "/.preflight"),
    "ok=true only if at least one root exists and steps 2 and 3 worked. notes: one line with what exists and anything that failed.",
    "Return ONLY the JSON object.",
  ].join("\n"), Object.assign({ label: "preflight", schema: PRE_SCHEMA }, M.recon));
  ledger.preflight = pre;
  if (!pre || pre.ok !== true) {
    ctx.log("Preflight failed - halting: " + oneLine(pre && pre.notes, 300));
    return JSON.parse(JSON.stringify(Object.assign({ status: "halted", reason: "preflight failed" }, ledger)));
  }
  ctx.log("Preflight ok: " + oneLine(pre.notes));

  ctx.phase("Recon");
  const recon = await ctx.parallel(LENSES.map((lens) => async () => {
    const r = await ctx.agent(reconPrompt(lens), Object.assign({ label: "recon:" + lens.key, schema: RECON_SCHEMA }, M.recon));
    if (r === null) return failed("recon", "recon:" + lens.key);
    const hooks = (Array.isArray(r.hooks) ? r.hooks : []).slice(0, MAX_HOOKS);
    ctx.log("recon:" + lens.key + ": " + hooks.length + " hook(s), " + (r.unknowns || []).length + " unknown(s)");
    return { lens: lens.key, hooks: hooks, unknowns: r.unknowns || [], notes: r.notes || "" };
  }));
  ledger.recon = recon.filter((x) => x !== null);
  if (!ledger.recon.some((r) => r.hooks.length)) {
    ctx.log("No lens found a hook - nothing to build on");
    return JSON.parse(JSON.stringify(Object.assign({ status: "halted", reason: "no hooks found" }, ledger)));
  }

  ctx.phase("Hook map");
  const map = await ctx.agent(mapPrompt(ledger.recon), Object.assign({ label: "map", schema: MAP_SCHEMA }, M.map));
  if (map === null || !Array.isArray(map.hooks) || !map.hooks.length) {
    failed("map", "map");
    return JSON.parse(JSON.stringify(Object.assign({ status: "halted", reason: "no hook map" }, ledger)));
  }
  ledger.map = { gaps: map.gaps || [], resume: map.resume || "", alive: map.alive || "" };
  const ids = new Set();
  const hooks = map.hooks.slice(0, MAX_HOOKS).map((h, i) => {
    let id = String(h.id || "h" + (i + 1)).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || "h" + (i + 1);
    while (ids.has(id)) id = id + "-" + (i + 1);
    ids.add(id);
    return Object.assign({}, h, { id: id });
  });
  ctx.log("Hook map: " + hooks.length + " hook(s); gaps: " + (map.gaps || []).length);

  ctx.phase("Refute");
  const judged = await ctx.parallel(hooks.map((h) => async () => {
    const r = await tiered(refutePrompt(h), "refute:" + h.id, "refute", VERDICT_SCHEMA);
    const v = r.value;
    if (v === null) failed("refute", "refute:" + h.id);
    // Real but overstated is not refuted: a hook demonstrated on real data with a correction is built from the correction.
    const corrected = v !== null && v.holds !== true && v.demonstrated === true && typeof v.corrected === "string" && v.corrected.trim().length >= 20;
    const status = v === null ? "error" : v.holds === true && v.demonstrated === true ? "holds" : corrected ? "corrected" : v.holds === true ? "undemonstrated" : "refuted";
    ctx.log("refute:" + h.id + " -> " + status + (v ? " - " + oneLine(v.reason, 100) : ""));
    return Object.assign({}, h, { status: status, verdict: v, refuted_by: r.model });
  }));
  ledger.hooks = judged.filter((x) => x !== null);
  const held = ledger.hooks.filter((h) => h.status === "holds" || h.status === "corrected");
  if (!held.length) {
    ctx.log("No hook survived refutation - nothing to build on");
    return JSON.parse(JSON.stringify(Object.assign({ status: "halted", reason: "no hook survived" }, ledger)));
  }

  if (A.gate === true) {
    ctx.phase("Governor gate");
    ctx.log("Paused for the governor: " + held.length + " hook(s) to build on (" + ledger.hooks.filter((h) => h.status === "corrected").length + " corrected). Review the ledger, then resume the run to build.");
    await ctx.pause("hook-map-reviewed");
  }

  ctx.phase("Build + prove");
  let b = await ctx.agent(buildPrompt(ledger.map, held), Object.assign({ label: "build", schema: BUILD_SCHEMA }, M.build));
  if (b === null) {
    failed("build", "build");
    return JSON.parse(JSON.stringify(Object.assign({ status: "completed", outcome: "error" }, ledger)));
  }
  ledger.build = b;
  ctx.log("build -> " + b.status + " - " + oneLine(b.summary, 120));
  let outcome = b.status;
  for (let attempt = 0; b.status === "built" && attempt <= MAX_REVISIONS; attempt += 1) {
    const selfOk = b.tests_pass === true && b.check_pass === true;
    let p;
    if (!selfOk) {
      p = { verdict: "held", reason: "The builder's own tests or the contract check did not pass." };
    } else {
      const r = await tiered(provePrompt(b, attempt), "prove:" + attempt, "prove", PROVE_SCHEMA);
      if (r.value === null) { failed("prove", "prove:" + attempt); outcome = "unproven"; break; }
      p = Object.assign({ proved_by: r.model }, r.value);
    }
    ledger.proof = p;
    if (p.verdict === "proven") { outcome = "proven"; ctx.log("prove -> PROVEN (" + p.proved_by + "): " + oneLine(p.live_counts, 120)); break; }
    ctx.log("prove -> held (" + attempt + "): " + oneLine(p.reason, 120));
    outcome = "held";
    if (attempt === MAX_REVISIONS) break;
    const rb = await ctx.agent([
      "You are the BUILDER again: the independent prover HELD your beside agent for '" + A.tool + "'. Its report (JSON):",
      JSON.stringify(p, null, 1),
      "Fix " + (b.agent_file || agentFile) + " and its tests (or show by running something that the prover is wrong, and say so in summary). Tests and the contract check must pass: " + A.check_cmd.replace("{file}", b.agent_file || agentFile),
      "Your previous report (JSON):",
      JSON.stringify(b, null, 1),
      "",
      RULES,
      "",
      "Return ONLY the JSON object (the same shape as before).",
    ].join("\n"), Object.assign({ label: "revise:" + (attempt + 1), schema: BUILD_SCHEMA }, M.build));
    if (rb === null) { failed("revise", "revise:" + (attempt + 1)); break; }
    ctx.log("revise -> " + rb.status);
    b = rb;
    ledger.build = b;
    outcome = b.status;
  }

  ctx.phase("Ledger");
  const summary = {
    tool: A.tool,
    lenses_ok: ledger.recon.length,
    hooks: hooks.length,
    held: held.length,
    corrected: ledger.hooks.filter((h) => h.status === "corrected").length,
    refuted: ledger.hooks.filter((h) => h.status === "refuted").length,
    outcome: outcome,
    agent_file: b && b.agent_file ? b.agent_file : agentFile,
    covers: (b && b.covers) || [],
    gaps: ((b && b.gaps) || []).concat(ledger.map.gaps || []),
    errors: ledger.errors.length,
  };
  ctx.log("Ledger: " + JSON.stringify({ tool: summary.tool, held: summary.held, outcome: summary.outcome }));
  return JSON.parse(JSON.stringify(Object.assign({ status: "completed", summary: summary }, ledger)));
}
