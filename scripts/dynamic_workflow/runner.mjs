// RAPP dynamic-workflow engine.
// Runs a Copilot-style workflow body - the same run(ctx) source GitHub Copilot's Dynamic Workflows run - outside the
// Copilot CLI, with the same ctx semantics (copilot-sdk/docs/workflows.md). Each ctx.agent is a headless
// `copilot -p` session. Every result is journaled, so a crash or a restart RESUMES the run instead of losing it:
// finished agents replay from the journal, a subagent still running is adopted, and one that was killed continues
// in its own Copilot session with its context kept.
// Usage: node runner.mjs <run_dir>   (run_dir/run.json = {run_id, workflow: {name, version, run}, args, options})
import { spawn, execFileSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const ENGINE_VERSION = "1.0.0";
const RUN_DIR = path.resolve(process.argv[2] || ".");
const F = (n) => path.join(RUN_DIR, n);
const spec = JSON.parse(fs.readFileSync(F("run.json"), "utf8"));
const OPT = Object.assign({ max_concurrent: 8, agent_timeout_s: 14400, copilot: "copilot", cwd: F("cwd"), extra_flags: [], env: {} }, spec.options || {});
const OPTION_KEYS = ["label", "schema", "model", "agent", "reasoningEffort", "contextTier"];
const MAX_TRIES = 4;
const SESSION_RE = /\/\.copilot\/session-state\/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})\//;

fs.mkdirSync(F("agents"), { recursive: true });
fs.mkdirSync(OPT.cwd, { recursive: true });
const now = () => new Date().toISOString();
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const sha = (s) => crypto.createHash("sha256").update(s).digest("hex");
const canon = (v) => (Array.isArray(v) ? v.map(canon) : v && typeof v === "object" ? Object.fromEntries(Object.keys(v).sort().map((k) => [k, canon(v[k])])) : v);
const slug = (s) => String(s || "agent").replace(/[^A-Za-z0-9._-]+/g, "-").slice(0, 60);
const readJson = (p, dflt) => { try { return JSON.parse(fs.readFileSync(p, "utf8")); } catch { return dflt; } };
const writeJson = (p, v) => { const t = p + ".tmp-" + process.pid; fs.writeFileSync(t, JSON.stringify(v, null, 1)); fs.renameSync(t, p); };
const message = (e) => (e && e.message) || String(e);

// ---- journal: one JSON line per settled result; a line torn by a crash is not a result ----
const journal = new Map();
if (fs.existsSync(F("journal.jsonl"))) {
  const raw = fs.readFileSync(F("journal.jsonl"), "utf8");
  for (const line of raw.split("\n")) {
    if (!line.trim()) continue;
    try { const e = JSON.parse(line); journal.set(e.key, e); } catch { /* torn */ }
  }
  if (raw && !raw.endsWith("\n")) fs.appendFileSync(F("journal.jsonl"), "\n");
}
const journalAdd = (key, kind, value, label) => {
  const e = { key, kind, value, label: label || "", t: now() };
  fs.appendFileSync(F("journal.jsonl"), JSON.stringify(e) + "\n");
  journal.set(key, e);
};

// ---- state + progress ----
const prev = readJson(F("state.json"), {});
const state = Object.assign({}, prev, {
  run_id: spec.run_id, workflow: spec.workflow.name, version: spec.workflow.version || "", engine: ENGINE_VERSION,
  status: "running", pid: process.pid, attempt: (prev.attempt || 0) + 1, started_at: prev.started_at || now(),
  attempt_started_at: now(), updated_at: now(), phase: prev.phase || "", error: null,
  agents: { running: 0, done: 0, failed: 0, replayed: 0, adopted: 0, resumed: 0 },
});
const save = () => { state.updated_at = now(); writeJson(F("state.json"), state); };
save();
const heartbeat = setInterval(save, 10000);
heartbeat.unref();
const progress = (kind, text) => fs.appendFileSync(F("progress.jsonl"), JSON.stringify({ t: now(), kind, text: String(text) }) + "\n");

// ---- stopping: an explicit cancel (the 'cancel' file) stops everything; any other signal - a restart, a logout,
// a kill - leaves the run INTERRUPTED and its subagents running, to be adopted by the next attempt ----
const controller = new AbortController();
let cancelled = false;
let pausedAt = null;
const children = new Set();
const hardError = (msg) => { const e = new Error(msg); e.name = "AbortError"; return e; };
const isHard = (e) => !!e && (e.name === "AbortError" || e.hard === true);
const throwIfAborted = () => { if (controller.signal.aborted) throw hardError("the run was stopped"); };
const stopChildren = () => { for (const pid of children) { try { process.kill(-pid, "SIGTERM"); } catch { /* gone */ } } };
for (const sig of ["SIGTERM", "SIGINT", "SIGHUP"]) {
  process.on(sig, () => {
    if (fs.existsSync(F("cancel"))) {
      cancelled = true;
      controller.abort(hardError("cancelled"));
      stopChildren();
      return;
    }
    state.status = "interrupted";
    state.interrupted_by = sig;
    save();
    progress("log", "interrupted by " + sig + " - resume to continue; running subagents are adopted");
    process.exit(0);
  });
}

// ---- one slot per running subagent (backpressure, never failure) ----
let active = 0;
const queue = [];
const acquire = () => new Promise((res) => { if (active < OPT.max_concurrent) { active += 1; res(); } else queue.push(res); });
const release = () => { const next = queue.shift(); if (next) next(); else active -= 1; };

// ---- structural JSON Schema subset (type, required, enum, const, properties, items, anyOf/oneOf/allOf) ----
const typeOk = (v, t) => ({ null: v === null, boolean: typeof v === "boolean", integer: Number.isInteger(v), number: typeof v === "number" && Number.isFinite(v), string: typeof v === "string", array: Array.isArray(v), object: v !== null && typeof v === "object" && !Array.isArray(v) })[t] === true;
function check(v, s, p) {
  if (!s || typeof s !== "object") return null;
  for (const sub of s.allOf || []) { const e = check(v, sub, p); if (e) return e; }
  const alts = s.anyOf || s.oneOf;
  if (alts && !alts.some((sub) => !check(v, sub, p))) return p + " matches none of its alternatives";
  if (s.const !== undefined && JSON.stringify(v) !== JSON.stringify(s.const)) return p + " must be " + JSON.stringify(s.const);
  if (s.enum && !s.enum.some((x) => JSON.stringify(x) === JSON.stringify(v))) return p + " must be one of " + JSON.stringify(s.enum);
  if (s.type) { const ts = Array.isArray(s.type) ? s.type : [s.type]; if (!ts.some((t) => typeOk(v, t))) return p + " must be " + ts.join(" or "); }
  if (typeOk(v, "object")) {
    for (const r of s.required || []) if (!(r in v)) return p + " is missing '" + r + "'";
    for (const [k, sub] of Object.entries(s.properties || {})) if (k in v) { const e = check(v[k], sub, p + "." + k); if (e) return e; }
  }
  if (Array.isArray(v) && s.items) for (let i = 0; i < v.length; i += 1) { const e = check(v[i], s.items, p + "[" + i + "]"); if (e) return e; }
  return null;
}
function extractJson(text) {
  const t = String(text == null ? "" : text).trim();
  const tries = [t];
  const fences = [...t.matchAll(/```(?:json)?[ \t]*\n([\s\S]*?)```/g)].map((m) => m[1]);
  tries.push(...fences.reverse());
  const last = t.lastIndexOf("}");
  if (last !== -1) {
    let seen = 0;
    for (let i = last; i >= 0 && seen < 400; i -= 1) if (t[i] === "{") { seen += 1; tries.push(t.slice(i, last + 1)); }
  }
  for (const c of tries) { try { return { ok: true, value: JSON.parse(c) }; } catch { /* next */ } }
  return { ok: false, error: "no JSON value found in the reply" };
}
function parseChecked(text, schema) {
  const r = extractJson(text);
  if (!r.ok) return r;
  const e = check(r.value, schema, "$");
  return e ? { ok: false, error: e } : r;
}
const schemaTail = (schema) => "\n\nReturn ONLY a JSON value that matches this JSON Schema - no prose, no code fences:\n" + JSON.stringify(schema);
const CONTINUE = "You were interrupted (the machine restarted or the run was stopped) before you gave your final answer. Continue the same task from where you left off - check what you already did before redoing anything - then give the final answer exactly as it was originally asked for.";

// ---- one headless Copilot session ----
function readEvents(file) {
  const out = { text: null, sessionId: null, exitCode: null, error: null };
  let raw = "";
  try { raw = fs.readFileSync(file, "utf8"); } catch { return out; }
  for (const line of raw.split("\n")) {
    if (!line.trim()) continue;
    let e;
    try { e = JSON.parse(line); } catch { continue; }
    const d = e.data || {};
    if (e.type === "assistant.message" && typeof d.content === "string" && d.content.trim()) out.text = d.content;
    else if (e.type === "session.error") out.error = d.message || d.errorType || "session error";
    else if (e.type === "result") { out.sessionId = e.sessionId || null; out.exitCode = e.exitCode; }
  }
  return out;
}
const recPath = (key) => F("agents/" + key.slice(0, 24) + ".json");
let seq = 0;
for (const f of fs.readdirSync(F("agents"))) if (f.endsWith(".json")) { const r = readJson(F("agents/" + f), null); if (r && r.seq > seq) seq = r.seq; }

function watchSession(rec) {
  let n = 0;
  const t = setInterval(() => {
    n += 1;
    if (rec.session_id || n > 60 || !rec.pid) { clearInterval(t); return; }
    try {
      const listing = execFileSync("lsof", ["-w", "-n", "-P", "-g", String(rec.pid), "-Fn"], { encoding: "utf8", timeout: 5000, stdio: ["ignore", "pipe", "ignore"] });
      const m = listing.match(SESSION_RE);
      if (m) { rec.session_id = m[1]; writeJson(recPath(rec.key), rec); clearInterval(t); }
    } catch { /* lsof exits 1 when nothing matches */ }
  }, 3000);
  t.unref();
  return t;
}
function alive(rec) {
  if (!rec.pid) return false;
  try { process.kill(rec.pid, 0); } catch { return false; }
  try {
    const cmd = execFileSync("ps", ["-o", "command=", "-p", String(rec.pid)], { encoding: "utf8", timeout: 5000 });
    return cmd.includes("copilot") || cmd.includes(path.basename(OPT.copilot));
  } catch { return false; }
}
function spawnCopilot(rec, promptText, opts, resumeSid) {
  return new Promise((resolve) => {
    rec.tries = (rec.tries || 0) + 1;
    const base = F("agents/" + String(rec.seq).padStart(4, "0") + "-" + slug(rec.label) + "." + rec.tries);
    fs.writeFileSync(base + ".prompt", promptText);
    const args = ["-p", promptText, "--output-format", "json", "--no-color", "--no-ask-user", "--allow-all"];
    if (resumeSid) args.push("--resume", resumeSid);
    if (opts.model) args.push("--model", opts.model);
    if (opts.reasoningEffort) args.push("--reasoning-effort", opts.reasoningEffort);
    if (opts.contextTier) args.push("--context", opts.contextTier);
    if (opts.agent) args.push("--agent", opts.agent);
    args.push(...OPT.extra_flags);
    const out = fs.openSync(base + ".out", "w");
    const err = fs.openSync(base + ".err", "w");
    let child;
    try {
      child = spawn(OPT.copilot, args, { cwd: OPT.cwd, detached: true, stdio: ["ignore", out, err], env: Object.assign({}, process.env, OPT.env, { RAPP_WORKFLOW_RUN: spec.run_id, RAPP_WORKFLOW_AGENT: rec.label || "" }) });
    } catch (e) {
      progress("log", (rec.label || "agent") + ": could not start copilot - " + message(e));
      fs.closeSync(out); fs.closeSync(err);
      return resolve(null);
    }
    fs.closeSync(out); fs.closeSync(err);
    let settled = false;
    const finish = (code, signal) => {
      if (settled) return;
      settled = true;
      clearTimeout(timer);
      clearInterval(finder);
      children.delete(child.pid);
      state.agents.running -= 1;
      const got = readEvents(base + ".out");
      if (got.sessionId) rec.session_id = got.sessionId;
      Object.assign(rec, { status: "exited", exit: code, signal: signal || null, ended_at: now() });
      writeJson(recPath(rec.key), rec);
      if (code !== 0 || got.text == null) {
        progress("log", (rec.label || "agent") + ": no answer (exit " + code + (signal ? ", " + signal : "") + ")" + (got.error ? " - " + got.error : ""));
        return resolve(null);
      }
      resolve(got.text);
    };
    child.on("error", (e) => { progress("log", (rec.label || "agent") + ": " + message(e)); finish(-1, null); });
    child.on("close", finish);
    Object.assign(rec, { status: "running", pid: child.pid, out: base + ".out", err: base + ".err", started_at: now() });
    writeJson(recPath(rec.key), rec);
    children.add(child.pid);
    state.agents.running += 1;
    const finder = watchSession(rec);
    const timer = setTimeout(() => {
      progress("log", (rec.label || "agent") + ": timed out after " + OPT.agent_timeout_s + " s");
      try { process.kill(-child.pid, "SIGTERM"); } catch { /* gone */ }
    }, OPT.agent_timeout_s * 1000);
  });
}
async function adopt(rec) {
  state.agents.running += 1;
  state.agents.adopted += 1;
  progress("log", (rec.label || "agent") + ": still running from the last attempt - adopted");
  while (!controller.signal.aborted) {
    await sleep(5000);
    try { process.kill(rec.pid, 0); } catch { break; }
  }
  state.agents.running -= 1;
  const got = readEvents(rec.out);
  if (got.sessionId) rec.session_id = got.sessionId;
  Object.assign(rec, { status: "exited", exit: got.exitCode, ended_at: now() });
  writeJson(recPath(rec.key), rec);
  return got.exitCode === 0 ? got.text : null;
}

// ---- ctx ----
const inflight = new Map();
async function runAgent(key, prompt, opts) {
  await acquire();
  try {
    throwIfAborted();
    let rec = readJson(recPath(key), null);
    const fromBefore = !!rec;
    if (!rec) { seq += 1; rec = { key, label: opts.label || "", seq, tries: 0 }; }
    const first = prompt + (opts.schema ? schemaTail(opts.schema) : "");
    let text = null;
    if (fromBefore) {
      if (rec.status === "running" && alive(rec)) text = await adopt(rec);
      else if (rec.status === "exited" && rec.exit === 0 && rec.out) text = readEvents(rec.out).text;
      if (text == null && rec.session_id && rec.tries < MAX_TRIES) {
        state.agents.resumed += 1;
        progress("log", (rec.label || "agent") + ": interrupted - continuing its own session " + rec.session_id.slice(0, 8));
        text = await spawnCopilot(rec, CONTINUE + (opts.schema ? schemaTail(opts.schema) : ""), opts, rec.session_id);
      }
      if (text == null && !rec.session_id && rec.tries < MAX_TRIES) text = await spawnCopilot(rec, first, opts, null);
    } else {
      text = await spawnCopilot(rec, first, opts, null);
    }
    if (text == null) {
      if (controller.signal.aborted) throw hardError("the run was stopped");
      state.agents.failed += 1;
      return null;
    }
    if (!opts.schema) {
      journalAdd(key, "agent", text, opts.label);
      state.agents.done += 1;
      return text;
    }
    let r = parseChecked(text, opts.schema);
    if (!r.ok && rec.session_id) {
      progress("log", (rec.label || "agent") + ": reply did not match its schema (" + r.error + ") - asking once more");
      const fix = await spawnCopilot(rec, "Your final answer did not match the required JSON Schema: " + r.error + ". Reply with ONLY the corrected JSON value - no prose, no code fences." + schemaTail(opts.schema), opts, rec.session_id);
      if (fix != null) r = parseChecked(fix, opts.schema);
    }
    if (controller.signal.aborted) throw hardError("the run was stopped");
    if (!r.ok) { state.agents.failed += 1; progress("log", (rec.label || "agent") + ": no valid answer - " + r.error); return null; }
    journalAdd(key, "agent", r.value, opts.label);
    state.agents.done += 1;
    return r.value;
  } finally {
    release();
  }
}
function agent(prompt, options) {
  if (typeof prompt !== "string") return Promise.reject(new TypeError("ctx.agent: the prompt must be a string"));
  const opts = {};
  for (const k of OPTION_KEYS) if (options && options[k] !== undefined) opts[k] = options[k];
  const key = sha(JSON.stringify(canon({ prompt, opts })));
  const hit = journal.get(key);
  if (hit && hit.kind === "agent") { state.agents.replayed += 1; return Promise.resolve(hit.value); }
  if (inflight.has(key)) return inflight.get(key);
  const p = runAgent(key, prompt, opts).finally(() => inflight.delete(key));
  inflight.set(key, p);
  return p;
}
async function parallel(thunks) {
  throwIfAborted();
  if (!Array.isArray(thunks)) throw new TypeError("ctx.parallel: expects an array of thunks");
  if (thunks.length > 4096) throw new RangeError("ctx.parallel: more than 4096 items");
  return Promise.all(thunks.map(async (t, i) => {
    try { return await t(); } catch (e) { if (isHard(e)) throw e; progress("log", "parallel item " + i + " failed: " + message(e)); return null; }
  }));
}
async function pipeline(items, ...stages) {
  throwIfAborted();
  if (!Array.isArray(items)) throw new TypeError("ctx.pipeline: expects an array of items");
  if (items.length > 4096) throw new RangeError("ctx.pipeline: more than 4096 items");
  return Promise.all(items.map(async (item, i) => {
    let value = item;
    for (const stage of stages) {
      try { value = await stage(value, item, i); } catch (e) { if (isHard(e)) throw e; progress("log", "pipeline item " + i + " dropped: " + message(e)); return null; }
    }
    return value;
  }));
}
async function step(key, producer, options) {
  throwIfAborted();
  if (options && options.volatile) return producer();
  const k = "step:" + key;
  if (journal.has(k)) return journal.get(k).value;
  const v = await producer();
  if (v === undefined) throw new TypeError("ctx.step('" + key + "'): a journaled producer must return a JSON value");
  const j = JSON.parse(JSON.stringify(v));
  journalAdd(k, "step", j, key);
  return j;
}
async function pause(key) {
  const k = "pause:" + key;
  if (journal.has(k)) return;
  journalAdd(k, "pause", true, key);
  pausedAt = key;
  const e = hardError("paused at checkpoint '" + key + "'");
  controller.abort(e);
  throw e;
}
const ctx = {
  runId: spec.run_id,
  args: spec.args == null ? {} : spec.args,
  agent,
  parallel,
  pipeline,
  step,
  pause,
  phase: (title) => { throwIfAborted(); state.phase = String(title); progress("phase", title); save(); },
  log: (msg) => { throwIfAborted(); progress("log", msg); },
  workflow: async () => { throw new Error("nested workflows are not supported"); },
  signal: controller.signal,
  session: undefined,
};

progress("log", "attempt " + state.attempt + " started (engine " + ENGINE_VERSION + ", journal " + journal.size + " entries, up to " + OPT.max_concurrent + " subagents at once)");
try {
  const run = (0, eval)("(" + spec.workflow.run + "\n)");
  if (typeof run !== "function") throw new TypeError("the workflow's run source is not a function expression");
  const result = await run(ctx);
  if (result !== undefined) {
    const text = JSON.stringify(result);
    if (text === undefined) throw new TypeError("the workflow returned a value that is not JSON");
    writeJson(F("result.json"), JSON.parse(text));
  }
  state.status = "completed";
  state.completed_at = now();
  progress("log", "completed");
} catch (e) {
  if (pausedAt) { state.status = "paused"; state.paused_at = pausedAt; }
  else if (cancelled) state.status = "cancelled";
  else { state.status = "error"; state.error = String((e && e.stack) || e).slice(0, 4000); }
  progress("log", state.status + ": " + message(e));
  if (state.status !== "paused") stopChildren();
} finally {
  clearInterval(heartbeat);
  save();
}
process.exit(0);
