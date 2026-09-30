async (ctx) => {
  const A = ctx.args || {};
  for (const k of ["repo", "base", "frozen", "brief", "scratch_root", "build_root"]) {
    if (typeof A[k] !== "string" || !A[k]) throw new Error("adversarial-fleet: missing string arg '" + k + "'");
  }
  const dims = Array.isArray(A.dimensions) ? A.dimensions : [];
  const seedsIn = Array.isArray(A.seeds) ? A.seeds : [];
  const elsewhere = Array.isArray(A.elsewhere) ? A.elsewhere : [];
  if (dims.length === 0 && seedsIn.length === 0) throw new Error("adversarial-fleet: give dimensions to review, seeds to build, or both");
  for (const d of dims) {
    if (!d || typeof d.key !== "string" || !d.key || typeof d.focus !== "string" || !d.focus) throw new Error("adversarial-fleet: every dimension needs a key and a focus");
  }
  for (const s of seedsIn) {
    if (!s || typeof s.unit_id !== "string" || !s.unit_id || typeof s.title !== "string" || typeof s.plan !== "string") throw new Error("adversarial-fleet: every seed needs unit_id, title and plan");
  }

  // Static bounds (RAR @rapp/swarm_factory hard rule 4).
  const MAX_FINDINGS = 4;
  const MAX_REVISIONS = 1;
  const PRODUCT = A.product || "the project";
  const USER = A.user || "the user";
  const PREFIX = A.branch_prefix || "fleet/";
  const TESTS = A.test_prefix || "tests/test_fleet_";
  const TRAILERS = A.trailers || "(no trailers)";
  const OPUS = { model: "claude-opus-5.5", reasoningEffort: "max", contextTier: "long_context" };
  const SOL = { model: "gpt-5.6-sol", reasoningEffort: "max", contextTier: "long_context" };
  const M = Object.assign({ review: OPUS, refute: SOL, triage: OPUS, build: OPUS, prove: SOL, fallback: OPUS }, A.models || {});

  const ledger = { preflight: null, reviewers: [], findings: [], dropped: [], units: [], errors: [] };
  const oneLine = (s, n) => String(s == null ? "" : s).replace(/\s+/g, " ").trim().slice(0, n || 140);
  const slugify = (s) => String(s || "unit").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 40) || "unit";
  // Errors are data, never content (hard rule 1): a failed agent is recorded and never flows downstream.
  const failed = (stage, label) => {
    ledger.errors.push({ failed_stage: stage, label: label });
    ctx.log("ERROR at " + stage + " (" + label + "): the agent returned nothing");
    return { status: "error", failed_stage: stage, label: label };
  };
  // Opportunistic tiering with graceful fallback (hard rule 6).
  const tiered = async (prompt, label, tier, schema) => {
    const first = await ctx.agent(prompt, Object.assign({ label: label, schema: schema }, M[tier]));
    if (first !== null) return { value: first, model: M[tier].model };
    ctx.log("fallback: " + label + " got nothing from " + M[tier].model + "; asking " + M.fallback.model);
    const second = await ctx.agent(prompt, Object.assign({ label: label + ":fallback", schema: schema }, M.fallback));
    return { value: second, model: second === null ? null : M.fallback.model };
  };

  const RULES = [
    "Fleet rules (they bind every subagent in this workflow):",
    "- You are one of many subagents running at once on " + USER + "'s Mac under a governed workflow; the machine is loaded. You cannot ask questions: do the job, then return the JSON.",
    "- The brief is the contract and its safety rules bind you. In particular: never start a model session of any AI CLI (--version / --help only); never push; never write under /tmp (your runtime cannot); read real logs only to confirm shapes, and report counts, field names, states and 8-character id prefixes - never content.",
    "- Run TARGETED tests only (the modules you need), never the whole suite; never two installer test modules at once in one tree.",
    "- Errors are data: if something you need fails, say exactly what failed in your JSON. Never dress an error up as a result.",
  ].join("\n");

  const FINDINGS_SCHEMA = {
    type: "object",
    required: ["dimension", "findings"],
    properties: {
      dimension: { type: "string" },
      findings: {
        type: "array",
        items: {
          type: "object",
          required: ["title", "file", "line", "severity", "scenario", "kody_impact", "repro"],
          properties: {
            title: { type: "string" },
            file: { type: "string" },
            line: { type: ["integer", "string"] },
            severity: { type: "string", enum: ["high", "medium", "low"] },
            scenario: { type: "string" },
            kody_impact: { type: "string" },
            repro: { type: "string" },
            repro_command: { type: "string" },
            observed: { type: "string" },
          },
        },
      },
      controls: { type: "array", items: { type: "object", required: ["path", "proves"], properties: { path: { type: "string" }, proves: { type: "string" } } } },
      notes: { type: "string" },
    },
  };
  const VERDICT_SCHEMA = {
    type: "object",
    required: ["isReal", "reproduced", "reason"],
    properties: {
      isReal: { type: "boolean" },
      reproduced: { type: "boolean" },
      reason: { type: "string" },
      path: { type: "string" },
      corrected_scenario: { type: "string" },
      real_data: { type: "string" },
      fix_hint: { type: "string" },
    },
  };
  const TRIAGE_SCHEMA = {
    type: "object",
    required: ["units", "dropped"],
    properties: {
      units: {
        type: "array",
        items: {
          type: "object",
          required: ["unit_id", "title", "finding_ids", "files", "plan"],
          properties: {
            unit_id: { type: "string" },
            title: { type: "string" },
            finding_ids: { type: "array", items: { type: "string" } },
            seed: { type: "boolean" },
            files: { type: "array", items: { type: "string" } },
            plan: { type: "string" },
            risk: { type: "string" },
          },
        },
      },
      dropped: { type: "array", items: { type: "object", required: ["finding_id", "reason"], properties: { finding_id: { type: "string" }, reason: { type: "string" } } } },
    },
  };
  const BUILD_SCHEMA = {
    type: "object",
    required: ["status", "summary"],
    properties: {
      status: { type: "string", enum: ["built", "declined", "error"] },
      branch: { type: "string" },
      commit: { type: "string" },
      worktree: { type: "string" },
      files_changed: { type: "array", items: { type: "string" } },
      tests_added: { type: "array", items: { type: "string" } },
      ab: { type: "object", required: ["fails_on_base", "passes_on_fix"], properties: { fails_on_base: { type: "boolean" }, passes_on_fix: { type: "boolean" }, evidence: { type: "string" } } },
      targeted_runs: { type: "string" },
      mutations: {
        type: "array",
        items: {
          type: "object",
          required: ["name", "file", "old", "new", "tests"],
          properties: { name: { type: "string" }, file: { type: "string" }, old: { type: "string" }, new: { type: "string" }, tests: { type: "array", items: { type: "string" } } },
        },
      },
      summary: { type: "string" },
      risks: { type: "string" },
    },
  };
  const PROVE_SCHEMA = {
    type: "object",
    required: ["verdict", "reason"],
    properties: {
      verdict: { type: "string", enum: ["proven", "held"] },
      ab: { type: "object", properties: { fails_on_base: { type: "boolean" }, passes_on_fix: { type: "boolean" } } },
      targeted_ok: { type: "boolean" },
      one_layer_over: { type: "string" },
      vacuous: { type: "boolean" },
      reason: { type: "string" },
    },
  };
  const PRE_SCHEMA = { type: "object", required: ["ok", "notes"], properties: { ok: { type: "boolean" }, notes: { type: "string" } } };

  const reviewPrompt = (d) => [
    "You are reviewer '" + d.key + "' in an adversarial review round of " + PRODUCT + ".",
    "Read the brief first; it is the contract for this job: " + A.brief,
    "Frozen tree to review (read-only; commit " + A.base + "): " + A.frozen,
    "Your scratch folder (the only place you write): " + A.scratch_root + "/" + d.key + "/ - copy the tree there to run probes and tests.",
    "",
    "YOUR DIMENSION - " + d.key + ": " + d.focus,
    "",
    "Follow the brief's instruction: assume this round's fixes reintroduced, one layer over, the bugs they were written to prevent. Find where.",
    "At most " + MAX_FINDINGS + " findings. Each needs file and line, the concrete failure scenario (inputs -> the wrong behaviour -> what " + USER + " would see or lose, in kody_impact), and a runnable reproduction saved in your scratch folder: its path (repro), the command (repro_command) and the output you observed (observed). No style notes, no speculation without a path, nothing the brief lists as fixed or as known-and-left.",
    "An EMPTY findings list is a legitimate answer and is plausible after many rounds. Do not invent work to justify yourself.",
    "Also list up to 4 controls: probes you ran that PASS and would make good regression tests (path + what each proves).",
    "",
    RULES,
    "",
    "Return ONLY the JSON object.",
  ].join("\n");

  const refutePrompt = (f) => [
    "You are the REFUTER for one finding from an adversarial review of " + PRODUCT + ". Your job is to DISPROVE it: return isReal=false if you can.",
    "It survives only if you restate, in your own words, the concrete path to the wrong behaviour (in 'path') AND you reproduced it by RUNNING something - a probe or a test - on a fresh copy of the frozen tree, not by reading source alone (reproduced=true only then).",
    "Brief (the contract; read its rules and the history of what was fixed or left on purpose): " + A.brief,
    "Frozen tree (read-only; commit " + A.base + "): " + A.frozen,
    "Your scratch folder: " + A.scratch_root + "/refute-" + f.id + "/ (the reviewer's own probes are under " + A.scratch_root + "/" + f.dimension + "/).",
    "",
    "Check, in order: (1) run the reviewer's reproduction on a fresh copy of the frozen tree; (2) is the trigger real on this Mac - confirm the data shape exists in real logs or the record (counts and field names only; the live record only through a keyless backup copy, as the brief says); (3) is it already fixed, or listed as known-and-left in the brief - then isReal=false; (4) if the mechanism is real but the scenario is wrong, say so in corrected_scenario (that correction is valuable); (5) a one-line fix_hint.",
    "",
    "The finding (JSON):",
    JSON.stringify(f, null, 1),
    "",
    RULES,
    "",
    "Return ONLY the JSON object.",
  ].join("\n");

  const triagePrompt = (confirmed, seeds) => [
    "You are the TRIAGE step of a governed fleet fixing " + PRODUCT + " (repo " + A.repo + ", base commit " + A.base + ").",
    "Below are the findings that survived refutation, and seed units already planned. Group them into BUILD UNITS: one builder per unit, all working at once in separate git worktrees from " + A.base + ", merged afterwards.",
    "- Put findings that share a root cause, or that would edit the same function, into ONE unit: two builders must never fix the same code two ways.",
    "- Otherwise keep units small and independent. Name the files each unit will touch.",
    "- Keep every seed unit (same unit_id, seed=true); you may fold a finding into a seed by listing its id there.",
    "- Every finding id appears in exactly one unit, or in dropped with a reason (for example: the same defect as another finding).",
    "- Never create a unit that duplicates one being built elsewhere (listed below); a finding that is the same defect goes to dropped with the reason 'covered by <unit_id> elsewhere'.",
    "- unit_id: a short kebab-case slug. plan: the fix in 2-4 sentences, using the refuter's corrected scenario where it gave one.",
    "Read the code at " + A.frozen + " (read-only) as needed. Do not edit anything.",
    "",
    "Findings (JSON):",
    JSON.stringify(confirmed.map((f) => ({ id: f.id, dimension: f.dimension, title: f.title, file: f.file, line: f.line, severity: f.severity, scenario: f.scenario, verdict: f.verdict })), null, 1),
    "",
    "Seed units (JSON):",
    JSON.stringify(seeds, null, 1),
    "",
    "Units being built elsewhere (JSON):",
    JSON.stringify(elsewhere, null, 1),
    "",
    "Return ONLY the JSON object.",
  ].join("\n");

  const buildPrompt = (u) => {
    const wt = A.build_root + "/" + u.slug;
    const br = PREFIX + u.slug;
    return [
      "You are the BUILDER for one unit of work on " + PRODUCT + ". Work test-first and prove your test is real.",
      "Contract: read the brief first: " + A.brief + " - its rules bind you. Match the repo's own conventions (read its README and the newest tests before writing).",
      "",
      "Your workspace (yours alone):",
      "  git -C " + A.repo + " worktree add " + wt + " -b " + br + " " + A.base,
      "If that path already exists as a worktree on " + br + ", it is your own earlier attempt: continue from its state. If git reports a lock, wait 5 s and retry (up to 5 times).",
      "",
      "Steps:",
      " 1. Write the failing test(s) FIRST, in a new module " + TESTS + u.slug.replace(/-/g, "_") + ".py.",
      " 2. Run it on the unchanged base code: it MUST fail. Keep that output. If it passes on base, the test is vacuous: fix the test, not the code.",
      " 3. Make the smallest correct fix. Update directly related docs when behaviour " + USER + " reads about changes.",
      " 4. Run your test: it MUST pass. Run the existing test modules of every file you touched (targeted only).",
      " 5. Assume your fix reintroduced the bug one layer over: check the neighbours (other callers, the sibling code paths and modes, append-only guarantees, lock waits, what " + USER + " sees) and cover what you find.",
      " 6. Commit on " + br + " only - one commit. Message: first line = what " + USER + " gets, in plain words; body = the failure, the cause, the fix, and the A/B evidence; end with these trailers exactly:",
      TRAILERS,
      " 7. Propose mutation-catalog entries (do NOT edit any catalog): each re-introduces the old behaviour by replacing an exact 'old' snippet of a source file with 'new'; 'tests' are the test ids that must then fail.",
      "Never push. Never touch the main branch, another branch, another worktree, or anything the brief forbids.",
      "If the unit turns out not to be a real defect, or has no clean fix, return status 'declined' with the reason - a gate that says no is working.",
      "",
      "The unit (JSON):",
      JSON.stringify(u, null, 1),
      "",
      RULES,
      "",
      "Return ONLY the JSON object (branch " + br + ", worktree " + wt + ").",
    ].join("\n");
  };

  const provePrompt = (u, b, attempt) => {
    const dir = A.build_root + "/prove-" + u.slug + "-" + attempt;
    return [
      "You are the PROVER for one fix to " + PRODUCT + ". Assume the fix is wrong until you have shown otherwise; return verdict 'held' if you can.",
      "Brief (the contract): " + A.brief + ". Repo: " + A.repo + "; base commit " + A.base + ".",
      "The builder's branch " + (b.branch || "?") + " at commit " + (b.commit || "?") + " - never modify it or its worktree.",
      "Make your own copy: git -C " + A.repo + " worktree add --detach " + dir + " " + (b.commit || b.branch) + " (retry on a git lock); remove it when done: git -C " + A.repo + " worktree remove --force " + dir,
      "Prove it by running things, not by reading:",
      " 1. A/B: with the new tests but the BASE source (git checkout " + A.base + " -- <every changed file that is not a test>), the new tests must FAIL; with the branch's source they must PASS. Report both.",
      " 2. The existing test modules of the touched files pass on the branch (targeted only).",
      " 3. One layer over: does the fix move the bug somewhere else - other callers, the sibling code paths and modes, append-only guarantees, lock waits, what " + USER + " sees? Probe it.",
      " 4. Vacuous tests: do they pass for the wrong reason, or mock past the code under test?",
      "verdict 'proven' only if 1 and 2 hold and 3 and 4 found nothing real; otherwise 'held', with a reason the builder can act on.",
      "",
      "The unit and the builder's report (JSON):",
      JSON.stringify({ unit: u, build: b }, null, 1),
      "",
      RULES,
      "",
      "Return ONLY the JSON object.",
    ].join("\n");
  };

  const revisePrompt = (u, b, p) => [
    "You are the BUILDER again, revising your fix to " + PRODUCT + ": the independent prover HELD it.",
    "The prover's report (JSON):",
    JSON.stringify(p, null, 1),
    "",
    "Continue in your own worktree " + (b.worktree || A.build_root + "/" + u.slug) + " on branch " + (b.branch || PREFIX + u.slug) + ". Address the prover's reason - or, if the prover is wrong, show why by running something and say so in summary. Keep the test-first A/B discipline: the new tests must still FAIL on the base source and PASS on yours. Add one commit (same message rules), ending with these trailers exactly:",
    TRAILERS,
    "Never push; never touch anything but your branch and worktree. Brief: " + A.brief,
    "",
    "Your previous report (JSON):",
    JSON.stringify(b, null, 1),
    "",
    "The unit (JSON):",
    JSON.stringify(u, null, 1),
    "",
    RULES,
    "",
    "Return ONLY the JSON object (the same shape as before).",
  ].join("\n");

  // Preflight: gates actually gate (hard rule 2) - fail before the fleet spends anything.
  ctx.phase("Preflight");
  const pre = await ctx.agent([
    "Preflight for a governed subagent fleet. Run exactly these and nothing else:",
    " 1. ls " + A.frozen + " && git -C " + A.repo + " rev-parse --short " + A.base,
    " 2. mkdir -p " + A.build_root + " && touch " + A.build_root + "/.preflight && rm " + A.build_root + "/.preflight",
    " 3. git -C " + A.repo + " worktree list | head -3",
    "ok=true only if all three worked. notes: one line; name anything that failed with its exact error.",
    "Return ONLY the JSON object.",
  ].join("\n"), Object.assign({ label: "preflight", schema: PRE_SCHEMA }, M.review));
  ledger.preflight = pre;
  if (!pre || pre.ok !== true) {
    ctx.log("Preflight failed - halting before the fleet spends anything: " + oneLine(pre && pre.notes, 300));
    return JSON.parse(JSON.stringify(Object.assign({ status: "halted", reason: "preflight failed" }, ledger)));
  }
  ctx.log("Preflight ok: " + oneLine(pre.notes));

  // Review + refute: no barrier - a finding is refuted as soon as its reviewer returns.
  const recs = [];
  if (dims.length) {
    ctx.phase("Review + refute");
    const reviewed = await ctx.pipeline(dims,
      async (_prev, d) => {
        const label = "review:" + d.key;
        const out = await ctx.agent(reviewPrompt(d), Object.assign({ label: label, schema: FINDINGS_SCHEMA }, M.review));
        if (out === null) {
          ledger.reviewers.push({ key: d.key, status: "error" });
          failed("review", label);
          return [];
        }
        const all = Array.isArray(out.findings) ? out.findings : [];
        const kept = all.slice(0, MAX_FINDINGS);
        if (all.length > kept.length) ctx.log(label + ": dropped " + (all.length - kept.length) + " finding(s) beyond the cap of " + MAX_FINDINGS);
        ledger.reviewers.push({ key: d.key, status: "ok", findings: kept.length, controls: Array.isArray(out.controls) ? out.controls : [], notes: out.notes || "" });
        ctx.log(label + ": " + kept.length + " finding(s)" + (kept.length ? " - " + kept.map((f) => oneLine(f.title, 70)).join(" | ") : ""));
        return kept.map((f, i) => Object.assign({ id: d.key + "-" + (i + 1), dimension: d.key }, f));
      },
      async (fs) => {
        if (!Array.isArray(fs) || fs.length === 0) return [];
        const out = await ctx.parallel(fs.map((f) => async () => {
          const r = await tiered(refutePrompt(f), "refute:" + f.id, "refute", VERDICT_SCHEMA);
          const v = r.value;
          if (v === null) failed("refute", "refute:" + f.id);
          const status = v === null ? "error" : v.isReal === true && v.reproduced === true ? "confirmed" : v.isReal === true ? "unreproduced" : "refuted";
          const rec = Object.assign({}, f, { status: status, verdict: v, refuted_by: r.model });
          ledger.findings.push(rec);
          ctx.log("refute:" + f.id + " -> " + status + (v ? " - " + oneLine(v.reason, 110) : ""));
          return rec;
        }));
        return out.filter((x) => x !== null);
      });
    for (const arr of reviewed) if (Array.isArray(arr)) for (const r of arr) if (r) recs.push(r);
    const n = (s) => recs.filter((r) => r.status === s).length;
    ctx.log("Review + refute done: " + recs.length + " finding(s) - " + n("confirmed") + " confirmed, " + n("refuted") + " refuted, " + n("unreproduced") + " unreproduced (held for the governor), " + n("error") + " error(s)");
  }
  const confirmed = recs.filter((r) => r.status === "confirmed");

  // Triage: the one barrier - dedupe needs every confirmed finding at once.
  const seeds = seedsIn.map((s) => Object.assign({ seed: true, finding_ids: [], files: [] }, s));
  let units = seeds.slice();
  let triageFailed = false;
  if (confirmed.length) {
    ctx.phase("Triage");
    const t = await ctx.agent(triagePrompt(confirmed, seeds), Object.assign({ label: "triage", schema: TRIAGE_SCHEMA }, M.triage));
    if (t && Array.isArray(t.units)) {
      units = t.units.slice();
      ledger.dropped = Array.isArray(t.dropped) ? t.dropped : [];
    } else {
      triageFailed = true;
      failed("triage", "triage");
      ctx.log("Triage failed: one unit per confirmed finding, plus the seeds");
    }
  }
  // Coverage gate: every confirmed finding and every seed is built or explicitly dropped.
  const covered = new Set();
  for (const u of units) for (const id of Array.isArray(u.finding_ids) ? u.finding_ids : []) covered.add(id);
  for (const d of ledger.dropped) covered.add(d.finding_id);
  for (const f of confirmed) {
    if (covered.has(f.id)) continue;
    units.push({ unit_id: f.id, title: f.title, finding_ids: [f.id], files: [f.file], plan: (f.verdict && (f.verdict.corrected_scenario || f.verdict.fix_hint)) || f.scenario });
    if (!triageFailed) ctx.log("Triage left " + f.id + " out - it gets its own unit");
  }
  const have = new Set(units.map((u) => u.unit_id));
  for (const s of seeds) {
    if (have.has(s.unit_id)) continue;
    units.push(s);
    ctx.log("Triage left seed " + s.unit_id + " out - kept");
  }
  const byId = {};
  for (const f of confirmed) byId[f.id] = f;
  const used = new Set();
  units = units.map((u) => {
    const base = slugify(u.unit_id || u.title);
    let slug = base;
    let k = 2;
    while (used.has(slug)) { slug = base.slice(0, 36) + "-" + k; k += 1; }
    used.add(slug);
    return Object.assign({}, u, { slug: slug, findings: (Array.isArray(u.finding_ids) ? u.finding_ids : []).map((id) => byId[id]).filter((x) => x) });
  });
  if (units.length) ctx.log("Build units (" + units.length + "): " + units.map((u) => u.slug).join(", "));

  // Build + prove: one builder per unit in its own worktree (hard rule 3); a prover gates each; one bounded revision (rule 4).
  let results = [];
  if (units.length) {
    ctx.phase("Build + prove");
    results = await ctx.pipeline(units,
      async (_prev, u) => {
        const b = await ctx.agent(buildPrompt(u), Object.assign({ label: "build:" + u.slug, schema: BUILD_SCHEMA }, M.build));
        if (b === null) return Object.assign(failed("build", "build:" + u.slug), { unit: u.slug, title: u.title });
        ctx.log("build:" + u.slug + " -> " + b.status + (b.commit ? " " + String(b.commit).slice(0, 8) : "") + " - " + oneLine(b.summary, 110));
        return { unit: u.slug, title: u.title, status: b.status, build: b };
      },
      async (prev, u) => {
        if (!prev || prev.status !== "built") return prev;
        let b = prev.build;
        for (let attempt = 0; attempt <= MAX_REVISIONS; attempt += 1) {
          const selfOk = !!(b.ab && b.ab.fails_on_base === true && b.ab.passes_on_fix === true && b.commit);
          let p;
          if (!selfOk) {
            p = { verdict: "held", reason: "The builder's own A/B did not hold: the new tests must FAIL on the base source and PASS on the fix, with the fix committed." };
          } else {
            const r = await tiered(provePrompt(u, b, attempt), "prove:" + u.slug + ":" + attempt, "prove", PROVE_SCHEMA);
            if (r.value === null) {
              failed("prove", "prove:" + u.slug + ":" + attempt);
              return { unit: u.slug, title: u.title, status: "unproven", build: b };
            }
            p = Object.assign({ proved_by: r.model }, r.value);
          }
          if (p.verdict === "proven") {
            ctx.log("prove:" + u.slug + " -> PROVEN (" + p.proved_by + ")");
            return { unit: u.slug, title: u.title, status: "proven", build: b, proof: p };
          }
          ctx.log("prove:" + u.slug + " -> held (" + attempt + "): " + oneLine(p.reason, 120));
          if (attempt === MAX_REVISIONS) return { unit: u.slug, title: u.title, status: "held", build: b, proof: p };
          const rb = await ctx.agent(revisePrompt(u, b, p), Object.assign({ label: "revise:" + u.slug + ":" + (attempt + 1), schema: BUILD_SCHEMA }, M.build));
          if (rb === null) {
            failed("revise", "revise:" + u.slug + ":" + (attempt + 1));
            return { unit: u.slug, title: u.title, status: "held", build: b, proof: p };
          }
          ctx.log("revise:" + u.slug + " -> " + rb.status + (rb.commit ? " " + String(rb.commit).slice(0, 8) : ""));
          if (rb.status !== "built") return { unit: u.slug, title: u.title, status: rb.status, build: rb, proof: p };
          b = rb;
        }
        return { unit: u.slug, title: u.title, status: "held", build: b };
      });
  }

  ctx.phase("Ledger");
  ledger.units = results.filter((x) => x !== null);
  const count = (arr, s) => arr.filter((x) => x && x.status === s).length;
  const summary = {
    reviewers: dims.length,
    reviewers_ok: count(ledger.reviewers, "ok"),
    findings: recs.length,
    confirmed: confirmed.length,
    refuted: count(recs, "refuted"),
    unreproduced: count(recs, "unreproduced"),
    units: units.length,
    proven: count(ledger.units, "proven"),
    held: count(ledger.units, "held"),
    declined: count(ledger.units, "declined"),
    unproven: count(ledger.units, "unproven"),
    errors: ledger.errors.length,
  };
  ctx.log("Ledger: " + JSON.stringify(summary));
  return JSON.parse(JSON.stringify(Object.assign({ status: "completed", summary: summary }, ledger)));
}
