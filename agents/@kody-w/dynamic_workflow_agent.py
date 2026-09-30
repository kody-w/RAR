"""dynamic_workflow_agent.py - save, run and never lose governed multi-subagent workflows.

A dynamic workflow is a small JavaScript `run(ctx)` body that governs a fleet of subagents: `ctx.agent` spawns
one, `ctx.parallel` / `ctx.pipeline` fan them out, `ctx.step` and `ctx.pause` journal progress. GitHub Copilot CLI
runs these natively ("Dynamic Workflows") - but only in a session that has extensions configured, and a workflow
authored in a session lives only as long as that session. This agent is where they live instead:

  LIBRARY  Every workflow is saved as ~/.rapp/workflows/library/<name>.json (meta, run source, sha256, version).
           Built-ins ship inside this file: `adversarial-fleet` (review -> refute -> triage -> build -> prove) and
           `reflect` (reverse-engineer a locally run AI tool -> generate a beside agent.py that feeds RAPP Buzz).
  ENGINE   Runs any saved workflow on this machine with the same ctx semantics as Copilot's; each subagent is a
           headless `copilot -p` session. Every result is journaled, so a crash or a restart RESUMES the run:
           finished agents replay from the journal, a subagent still running is adopted, and one that was killed
           continues in its own Copilot session with its context kept.
  COPILOT  `install_copilot` writes a user-level Copilot CLI extension that registers every saved workflow
           natively in each new Copilot session that has experimental features on (copilot --experimental);
           `export` prints the exact payload to author one by hand.

Actions: list, show, save, save_preset, export, install_copilot, mount, unmount, run, status, runs, result, resume,
cancel. `mount` writes a copy of this file bound to ONE workflow into a Brainstem's agents/ folder: the Brainstem
hot-loads it on its next request as its own tool (AdversarialFleetWorkflow, ReflectWorkflow...) carrying its
workflow and the engine - a single file that can be shared and cannot lose its workflow. `unmount` removes it.

    DynamicWorkflow(action="run", name="adversarial-fleet", preset="my-round")
    DynamicWorkflow(action="status", run_id="adversarial-fleet-20260930-130200-ab12")
    DynamicWorkflow(action="resume", run_id="...")   # after a crash or a restart
    DynamicWorkflow(action="run", name="reflect", preset="gemini", replay_from="<run id>")  # rerun an improved
                                                     # workflow: identical settled agent calls are not spent again

CLI: python3 dynamic_workflow_agent.py <action> [--name N] [--run-id R] [--preset P] [--args JSON | --args-file F]
     [--meta-file F --run-file F] [--max-concurrent N] [--keep-mcp]

Harness rules, from RAR @rapp/swarm_factory v0.3: errors are data, never content; gates actually gate; a fresh
workspace per run; static bounds; parallel only when safe; opportunistic tiering with graceful fallback.
Stdlib only. Needs `node` and GitHub Copilot CLI (`copilot`) on this machine; nothing leaves it but the
subagents' own model calls.
"""

import argparse
import hashlib
import json
import os
import re
import secrets
import shutil
import signal
import subprocess
import sys
import tempfile
import time

try:
    from agents.basic_agent import BasicAgent
except Exception:  # standalone: python3 dynamic_workflow_agent.py ...
    try:
        from basic_agent import BasicAgent
    except Exception:
        class BasicAgent:
            def __init__(self, name=None, metadata=None):
                self.name = name or getattr(self, "name", "BasicAgent")
                self.metadata = metadata or getattr(self, "metadata", {})

            def perform(self, **kwargs):
                return "Not implemented."


# ---- manifest (mount rewrites this block) ----
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/dynamic_workflow",
    "version": "1.0.0",
    "display_name": "DynamicWorkflow",
    "description": "Save, run and resume governed multi-subagent workflows from a durable library, on a local engine that survives crashes and restarts, and register them natively in every Copilot CLI session.",
    "author": "Kody Wildfeuer",
    "tags": ["workflows", "orchestration", "subagents", "copilot", "durable", "rapp-buzz"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ---- end manifest ----

ENGINE_VERSION = "1.0.0"
NAME_RE = re.compile(r"^[A-Za-z0-9_-]+$")
ACTIONS = ("list", "show", "save", "save_preset", "export", "install_copilot", "mount", "unmount", "run", "status", "runs", "result", "resume", "cancel")
BOUND_ACTIONS = ("run", "status", "runs", "result", "resume", "cancel", "show")
MOUNT_MARK = "# mounted-by: RAPP DynamicWorkflow"
BOUND_WORKFLOW = None  # `mount` binds a copy of this file to one workflow: one hot-loadable tool per workflow
STALE_S = 60

RUNNER_JS = r'''// RAPP dynamic-workflow engine.
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
const OPT = Object.assign({ max_concurrent: 8, agent_timeout_s: 14400, transient_backoff_s: 30, copilot: "copilot", cwd: F("cwd"), extra_flags: [], env: {} }, spec.options || {});
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
    // The CLI failing (a model or network outage, a limit - a non-zero exit, not a signal) is not the subagent's
    // answer: continue its own session, context kept, with backoff, before the call counts as failed.
    while (text == null && !controller.signal.aborted && rec.status === "exited" && typeof rec.exit === "number" && rec.exit !== 0 && !rec.signal && rec.session_id && rec.tries < MAX_TRIES) {
      const wait = OPT.transient_backoff_s * rec.tries;
      progress("log", (rec.label || "agent") + ": the CLI failed (exit " + rec.exit + ") - continuing its own session " + rec.session_id.slice(0, 8) + " in " + wait + " s");
      await sleep(wait * 1000);
      if (controller.signal.aborted) break;
      state.agents.resumed += 1;
      text = await spawnCopilot(rec, CONTINUE + (opts.schema ? schemaTail(opts.schema) : ""), opts, rec.session_id);
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
'''

EXTENSION_JS = r'''// RAPP workflows - a GitHub Copilot CLI extension that registers every workflow saved by the RAPP
// DynamicWorkflow agent (~/.rapp/workflows/library/*.json) as a native Copilot Dynamic Workflow in every new
// Copilot session, so a workflow is never lost with the session that authored it.
// Written by dynamic_workflow_agent.py (action install_copilot). Safe to delete; the library stays.
import { defineWorkflow, joinSession } from "@github/copilot-sdk/extension";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const home = process.env.RAPP_WORKFLOWS_HOME || path.join(os.homedir(), ".rapp", "workflows");
const library = path.join(home, "library");
const workflows = [];
let files = [];
try {
  files = fs.readdirSync(library).filter((f) => f.endsWith(".json")).sort();
} catch {
  files = [];
}
for (const f of files) {
  try {
    const w = JSON.parse(fs.readFileSync(path.join(library, f), "utf8"));
    const run = (0, eval)("(" + w.run + "\n)");
    if (typeof run !== "function") throw new TypeError("its run source is not a function expression");
    workflows.push(defineWorkflow({ meta: w.meta, run }));
  } catch (e) {
    process.stderr.write("rapp-workflows: skipped " + f + ": " + ((e && e.message) || e) + "\n");
  }
}
await joinSession({ workflows });
'''

# ---- builtins (mount rewrites this block) ----
BUILTINS = {
    'adversarial-fleet': {
        "version": '1.0.0',
        "meta": json.loads(r'''{"name": "adversarial-fleet", "description": "Governed subagent fleet built on RAR @rapp/swarm_factory's harness rules. Steps: a preflight gate; one reviewer per dimension; one refuter per finding (Sol, with Opus fallback); a triage barrier that dedupes findings into build units, plus seeds; one builder per unit in its own git worktree, test-first; an A/B prover gate with one bounded revision. Returns a ledger. args: {repo, base, frozen, brief, scratch_root, build_root, product?, user?, dimensions?:[{key,focus}], seeds?:[{unit_id,title,plan,files?}], elsewhere?:[{unit_id,title}], branch_prefix?, test_prefix?, trailers?, models?}. Saved in the RAPP DynamicWorkflow library (RAR @kody-w/dynamic_workflow_agent).", "phases": [{"title": "Preflight"}, {"title": "Review + refute"}, {"title": "Triage"}, {"title": "Build + prove"}, {"title": "Ledger"}], "argsSchema": {"type": "object", "required": ["repo", "base", "frozen", "brief", "scratch_root", "build_root"], "properties": {"repo": {"type": "string"}, "base": {"type": "string"}, "frozen": {"type": "string"}, "brief": {"type": "string"}, "scratch_root": {"type": "string"}, "build_root": {"type": "string"}, "product": {"type": "string"}, "user": {"type": "string"}, "branch_prefix": {"type": "string"}, "test_prefix": {"type": "string"}, "trailers": {"type": "string"}, "dimensions": {"type": "array", "items": {"type": "object", "required": ["key", "focus"], "properties": {"key": {"type": "string"}, "focus": {"type": "string"}}}}, "seeds": {"type": "array", "items": {"type": "object", "required": ["unit_id", "title", "plan"], "properties": {"unit_id": {"type": "string"}, "title": {"type": "string"}, "plan": {"type": "string"}, "files": {"type": "array", "items": {"type": "string"}}}}}, "elsewhere": {"type": "array", "items": {"type": "object"}}, "models": {"type": "object"}}}}'''),
        "run": r'''async (ctx) => {
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
}''',
    },
    'reflect': {
        "version": '1.0.1',
        "meta": json.loads(r'''{"name": "reflect", "description": "Reverse-engineer a locally run AI tool so RAPP Buzz can record it, with the tool itself as the only source of truth. Steps: a preflight gate; four recon lenses at once (docs, disk, code, process); a hook map; a Sol refuter demonstrates every hook on real data, or it is dropped; an optional governor gate (pause); one builder writes <tool>_beside_agent.py test-first per the RAPP Buzz beside contract (docs/BESIDE.md); a prover gate with one bounded revision. args: {tool, about, roots:{name:[paths]}, contract, template, check_cmd ('{file}' = the agent), out_dir, scratch_root, needs?, gate?, product?, user?, models?}. Saved in the RAPP DynamicWorkflow library (RAR @kody-w/dynamic_workflow_agent).", "phases": [{"title": "Preflight"}, {"title": "Recon"}, {"title": "Hook map"}, {"title": "Refute"}, {"title": "Governor gate"}, {"title": "Build + prove"}, {"title": "Ledger"}], "argsSchema": {"type": "object", "required": ["tool", "about", "roots", "contract", "template", "check_cmd", "out_dir", "scratch_root"], "properties": {"tool": {"type": "string"}, "about": {"type": "string"}, "roots": {"type": "object"}, "contract": {"type": "string"}, "template": {"type": "string"}, "check_cmd": {"type": "string"}, "out_dir": {"type": "string"}, "scratch_root": {"type": "string"}, "needs": {"type": "array", "items": {"type": "string"}}, "gate": {"type": "boolean"}, "product": {"type": "string"}, "user": {"type": "string"}, "models": {"type": "object"}}}}'''),
        "run": r'''async (ctx) => {
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
}''',
    },
}
# ---- end builtins ----


class WorkflowError(Exception):
    """A refusal the caller can act on (bad name, unknown run, missing tool)."""


# ---------------------------------------------------------------- places

def _home():
    return os.environ.get("RAPP_WORKFLOWS_HOME") or os.path.join(os.path.expanduser("~"), ".rapp", "workflows")


def _dir(*parts):
    p = os.path.join(_home(), *parts)
    os.makedirs(p, exist_ok=True)
    return p


def _extensions_dir():
    return os.environ.get("COPILOT_EXTENSIONS_DIR") or os.path.join(os.path.expanduser("~"), ".copilot", "extensions")


def _read_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".tmp-")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)


def _write_json(path, value):
    _write(path, json.dumps(value, indent=1, sort_keys=True) + "\n")


def _tool(name, env_var):
    p = os.environ.get(env_var)
    if p:
        return p
    found = shutil.which(name)
    if found:
        return found
    for d in ("/opt/homebrew/bin", "/usr/local/bin", os.path.expanduser("~/.local/bin"), os.path.expanduser("~/.npm-global/bin")):
        c = os.path.join(d, name)
        if os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    return None


def _sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _version_tuple(v):
    try:
        return tuple(int(x) for x in str(v).split("."))
    except ValueError:
        return (0,)


def _check_name(name, what="workflow"):
    if not name or not NAME_RE.match(str(name)):
        raise WorkflowError("give a %s name made of letters, digits, '-' and '_' (got %r)" % (what, name))
    return str(name)


def _as_obj(value, what):
    if value is None or value == "":
        return None
    if isinstance(value, (dict, list)):
        return value
    try:
        return json.loads(value)
    except (TypeError, ValueError):
        raise WorkflowError("%s must be JSON (an object)" % what)


# ---------------------------------------------------------------- library

def _lib_path(name):
    return os.path.join(_dir("library"), name + ".json")


def _store_workflow(name, meta, run, version, source):
    doc = {"name": name, "version": version, "source": source, "meta": meta, "run": run,
           "sha256": _sha(run), "saved_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "engine": ENGINE_VERSION}
    _write_json(_lib_path(name), doc)
    return doc


def _sync_builtins():
    for name, b in BUILTINS.items():
        cur = _read_json(_lib_path(name))
        if cur is None or (cur.get("source") == "builtin" and _version_tuple(cur.get("version")) < _version_tuple(b["version"])):
            _store_workflow(name, b["meta"], b["run"], b["version"], "builtin")


def _load(name):
    _sync_builtins()
    if BOUND_WORKFLOW and name == BOUND_WORKFLOW:
        b = BUILTINS[name]
        return {"name": name, "version": b["version"], "source": "mounted", "meta": b["meta"], "run": b["run"], "sha256": _sha(b["run"])}
    doc = _read_json(_lib_path(_check_name(name)))
    if not doc:
        raise WorkflowError("no workflow named %r - action=list shows the library" % name)
    return doc


def _node_check(run):
    node = _tool("node", "RAPP_WORKFLOWS_NODE")
    if not node:
        return "not checked (node not found)"
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "check.mjs")
        with open(p, "w", encoding="utf-8") as f:
            f.write("export default (\n" + run + "\n);\n")
        r = subprocess.run([node, "--check", p], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        raise WorkflowError("the run source does not parse: " + (r.stderr.strip().splitlines() or ["?"])[-1])
    return "parses"


def _validate_meta(name, meta):
    if not isinstance(meta, dict):
        raise WorkflowError("meta must be an object with name, description and phases")
    if meta.get("name") != name:
        raise WorkflowError("meta.name must be %r" % name)
    if not isinstance(meta.get("description"), str) or not meta["description"].strip():
        raise WorkflowError("meta.description must say what the workflow does and what args it takes")
    phases = meta.get("phases")
    if not isinstance(phases, list) or not all(isinstance(p, dict) and isinstance(p.get("title"), str) for p in phases):
        raise WorkflowError("meta.phases must be a list of {title, detail?}")
    if "limits" in meta:
        raise WorkflowError("declare limits per run, only from a known cost - not in meta")


# ---------------------------------------------------------------- runs

def _run_dir(run_id):
    if not run_id or not NAME_RE.match(str(run_id)):
        raise WorkflowError("give the run_id that action=run returned (action=runs lists them)")
    d = os.path.join(_dir("runs"), run_id)
    if not os.path.isfile(os.path.join(d, "run.json")):
        raise WorkflowError("no run %r - action=runs lists them" % run_id)
    return d


def _pid_alive(pid, marker):
    if not pid:
        return False
    try:
        os.kill(int(pid), 0)
    except (OSError, ValueError):
        return False
    try:
        cmd = subprocess.run(["ps", "-o", "command=", "-p", str(pid)], capture_output=True, text=True, timeout=5).stdout
    except (OSError, subprocess.SubprocessError):
        return True
    return marker in cmd


def _state(run_dir):
    st = _read_json(os.path.join(run_dir, "state.json"), {}) or {}
    if st.get("status") == "running" and not _pid_alive(st.get("pid"), "runner-"):
        st["status"] = "interrupted"
        st["note"] = "the engine is not running (a crash, a restart or a kill) - action=resume continues it"
    return st


def _progress_tail(run_dir, n):
    lines = []
    try:
        with open(os.path.join(run_dir, "progress.jsonl"), encoding="utf-8") as f:
            for line in f:
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                lines.append("%s %s%s" % (e.get("t", "")[11:19], "## " if e.get("kind") == "phase" else "", e.get("text", "")))
    except OSError:
        pass
    return lines[-n:]


def _mcp_flags():
    """Subagents get the built-in tools only: every configured MCP server is switched off for them (less static
    context, no mail or cloud tools in a fleet)."""
    flags = ["--disable-builtin-mcps"]
    cfg = _read_json(os.path.join(os.path.expanduser("~"), ".copilot", "mcp-config.json"), {}) or {}
    for name in sorted((cfg.get("mcpServers") or {}).keys()):
        flags += ["--disable-mcp-server", name]
    return flags


def _engine_path():
    p = os.path.join(_dir("engine"), "runner-%s.mjs" % _sha(RUNNER_JS)[:12])
    if not os.path.exists(p):
        _write(p, RUNNER_JS)
    return p


def _start(run_dir):
    """Start the engine detached from the caller (double fork through sh): it outlives a Brainstem request, a
    terminal or this process, and never lingers as a zombie of a long-lived host. Its pid comes from state.json."""
    node = _tool("node", "RAPP_WORKFLOWS_NODE")
    if not node:
        raise WorkflowError("node is not installed - the engine needs Node.js (brew install node)")
    env = dict(os.environ)
    env["PATH"] = os.pathsep.join([os.path.dirname(node), "/opt/homebrew/bin", "/usr/local/bin", env.get("PATH", "")])
    env["RAPP_ENGINE_LOG"] = os.path.join(run_dir, "engine.log")
    try:
        os.remove(os.path.join(run_dir, "cancel"))
    except OSError:
        pass
    before = (_read_json(os.path.join(run_dir, "state.json"), {}) or {}).get("attempt", 0)
    sh = subprocess.Popen(["/bin/sh", "-c", '"$@" </dev/null >>"$RAPP_ENGINE_LOG" 2>&1 &', "sh", node, _engine_path(), run_dir],
                          stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                          cwd=run_dir, env=env, start_new_session=True)
    sh.wait(timeout=30)
    for _ in range(100):
        st = _read_json(os.path.join(run_dir, "state.json"), {}) or {}
        if st.get("attempt", 0) > before and st.get("pid"):
            return st["pid"]
        time.sleep(0.1)
    raise WorkflowError("the engine did not start - see %s" % env["RAPP_ENGINE_LOG"])


def _summary_line(st):
    a = st.get("agents") or {}
    return "%s - %s (attempt %s, phase %s; agents running %s, done %s, failed %s, replayed %s)" % (
        st.get("run_id", "?"), st.get("status", "?"), st.get("attempt", "?"), st.get("phase") or "-",
        a.get("running", 0), a.get("done", 0), a.get("failed", 0), a.get("replayed", 0))


# ---------------------------------------------------------------- actions

def act_list(**_):
    _sync_builtins()
    out = []
    for f in sorted(os.listdir(_dir("library"))):
        doc = _read_json(os.path.join(_dir("library"), f))
        if doc and f.endswith(".json"):
            out.append({"name": doc["name"], "version": doc.get("version"), "source": doc.get("source"),
                        "about": doc["meta"]["description"].split(". ")[0][:160]})
    runs = [_state(os.path.join(_dir("runs"), r)) for r in sorted(os.listdir(_dir("runs")), reverse=True)[:8]]
    return {"workflows": out, "recent_runs": [_summary_line(s) for s in runs if s]}


def act_show(name=None, **_):
    doc = _load(name)
    return {"name": doc["name"], "version": doc.get("version"), "source": doc.get("source"), "sha256": doc.get("sha256"),
            "description": doc["meta"]["description"], "phases": [p["title"] for p in doc["meta"]["phases"]],
            "args": sorted(((doc["meta"].get("argsSchema") or {}).get("properties") or {}).keys()),
            "run_source_chars": len(doc["run"]),
            "presets": sorted(p[:-5] for p in os.listdir(_dir("presets", doc["name"])) if p.endswith(".json"))}


def act_save(name=None, meta=None, run=None, version=None, **_):
    name = _check_name(name)
    meta = _as_obj(meta, "meta")
    if not isinstance(run, str) or not run.strip():
        raise WorkflowError("give run: the workflow body as a JavaScript function expression, async (ctx) => { ... }")
    _validate_meta(name, meta)
    parsed = _node_check(run)
    cur = _read_json(_lib_path(name))
    if version is None:
        v = list(_version_tuple(cur.get("version"))) if cur else [1, 0, 0]
        v = (v + [0, 0, 0])[:3]
        version = "1.0.0" if not cur else "%d.%d.%d" % (v[0], v[1], v[2] + 1)
    doc = _store_workflow(name, meta, run, str(version), "saved")
    return {"saved": name, "version": doc["version"], "sha256": doc["sha256"], "source_check": parsed,
            "path": _lib_path(name), "copilot": "native in new Copilot sessions started with --experimental, once action=install_copilot has run"}


def act_save_preset(name=None, preset=None, args=None, **_):
    doc = _load(name)
    preset = _check_name(preset, "preset")
    args = _as_obj(args, "args")
    if not isinstance(args, dict):
        raise WorkflowError("give args: the JSON object the workflow receives as ctx.args")
    p = os.path.join(_dir("presets", doc["name"]), preset + ".json")
    _write_json(p, args)
    return {"saved_preset": preset, "workflow": doc["name"], "path": p}


def act_export(name=None, **_):
    doc = _load(name)
    return {"how": "In any Copilot CLI session with extensions: dynamic_workflows_manage(operation='author', meta=<meta>, run=<run>), then run_dynamic_workflow(name=<name>, args=...). Or action=install_copilot once, and every new session has it.",
            "operation": "author", "meta": doc["meta"], "run": doc["run"]}


def act_install_copilot(**_):
    _sync_builtins()
    p = os.path.join(_extensions_dir(), "rapp-workflows", "extension.mjs")
    _write(p, EXTENSION_JS)
    names = sorted(f[:-5] for f in os.listdir(_dir("library")) if f.endswith(".json"))
    return {"installed": p, "registers": names,
            "note": "Copilot CLI sessions with experimental features on (copilot --experimental, or /experimental on once) load it at start: each saved workflow is a native Dynamic Workflow there"}


def _replay_journal(run_dir, replay_from):
    """Seed a new run's journal with the SETTLED agent results of an earlier run. A result is keyed by its exact
    prompt and options, so only identical calls replay - an improved workflow re-spends nothing it did not change.
    Steps and pauses are never carried: their keys are author names, not content. The records of calls that never
    settled (an outage, a crash) are carried too, so the new run continues their own sessions, context kept."""
    src_dir = _run_dir(replay_from)
    src = os.path.join(src_dir, "journal.jsonl")
    n = 0
    out = []
    settled = set()
    try:
        with open(src, encoding="utf-8") as f:
            for line in f:
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                if e.get("kind") == "agent" and e.get("key"):
                    out.append(json.dumps(e) + "\n")
                    settled.add(e["key"])
                    n += 1
    except OSError:
        pass
    if out:
        with open(os.path.join(run_dir, "journal.jsonl"), "w", encoding="utf-8") as f:
            f.writelines(out)
    carried = 0
    agents = os.path.join(src_dir, "agents")
    for name in sorted(os.listdir(agents)) if os.path.isdir(agents) else []:
        rec = _read_json(os.path.join(agents, name)) if name.endswith(".json") else None
        if rec and rec.get("key") and rec["key"] not in settled and rec.get("status") == "exited" and rec.get("session_id"):
            _write_json(os.path.join(run_dir, "agents", name), rec)
            carried += 1
    return n, carried


def act_run(name=None, args=None, preset=None, max_concurrent=None, agent_timeout_s=None, keep_mcp=False, replay_from=None, **_):
    doc = _load(name)
    merged = {}
    if preset:
        p = os.path.join(_dir("presets", doc["name"]), _check_name(preset, "preset") + ".json")
        base = _read_json(p)
        if base is None:
            raise WorkflowError("no preset %r for %s" % (preset, doc["name"]))
        merged.update(base)
    extra = _as_obj(args, "args")
    if extra is not None and not isinstance(extra, dict):
        raise WorkflowError("args must be a JSON object")
    merged.update(extra or {})
    copilot = _tool("copilot", "RAPP_WORKFLOWS_COPILOT")
    if not copilot:
        raise WorkflowError("GitHub Copilot CLI (copilot) is not installed - subagents run as copilot -p sessions")
    if replay_from:
        if _state(_run_dir(replay_from)).get("status") == "running":
            raise WorkflowError("run %s is still running - replay from it once it has settled (or cancel it)" % replay_from)
    run_id = "%s-%s-%s" % (doc["name"], time.strftime("%Y%m%d-%H%M%S"), secrets.token_hex(2))
    run_dir = os.path.join(_dir("runs"), run_id)
    os.makedirs(run_dir)
    replayed, carried = _replay_journal(run_dir, replay_from) if replay_from else (0, 0)
    options = {"max_concurrent": int(max_concurrent or 8), "agent_timeout_s": int(agent_timeout_s or 14400),
               "transient_backoff_s": float(os.environ.get("RAPP_WORKFLOWS_BACKOFF_S", "30")),
               "copilot": copilot, "extra_flags": [] if keep_mcp else _mcp_flags()}
    _write_json(os.path.join(run_dir, "run.json"), {
        "run_id": run_id, "args": merged, "options": options, "preset": preset or None,
        "workflow": {"name": doc["name"], "version": doc.get("version"), "sha256": doc.get("sha256"), "run": doc["run"]}})
    pid = _start(run_dir)
    return {"started": run_id, "engine_pid": pid, "run_dir": run_dir, "replayable_results": replayed,
            "continued_sessions": carried,
            "next": "action=status run_id=%s (it keeps running on its own; after a crash or restart: action=resume)" % run_id}


def act_status(run_id=None, lines=14, **_):
    d = _run_dir(run_id)
    st = _state(d)
    out = {"summary": _summary_line(st), "status": st.get("status"), "phase": st.get("phase"),
           "agents": st.get("agents"), "updated_at": st.get("updated_at"), "progress": _progress_tail(d, int(lines or 14))}
    if st.get("note"):
        out["note"] = st["note"]
    if st.get("error"):
        out["error"] = st["error"].splitlines()[0][:400]
    res = _read_json(os.path.join(d, "result.json"))
    if isinstance(res, dict) and "summary" in res:
        out["result_summary"] = res["summary"]
    return out


def act_runs(**_):
    rows = []
    for r in sorted(os.listdir(_dir("runs")), reverse=True)[:40]:
        st = _state(os.path.join(_dir("runs"), r))
        if st:
            rows.append(_summary_line(st))
    return {"runs": rows}


def act_result(run_id=None, **_):
    d = _run_dir(run_id)
    res = _read_json(os.path.join(d, "result.json"))
    if res is None:
        return {"status": _state(d).get("status"), "result": None, "note": "no result yet"}
    return {"status": _state(d).get("status"), "result": res}


def act_resume(run_id=None, force=False, **_):
    d = _run_dir(run_id)
    st = _state(d)
    if st.get("status") == "running":
        return {"resumed": False, "summary": _summary_line(st), "note": "it is running"}
    if st.get("status") == "completed":
        return {"resumed": False, "summary": _summary_line(st), "note": "it already completed - action=result"}
    if st.get("status") == "cancelled" and not force:
        return {"resumed": False, "summary": _summary_line(st), "note": "it was cancelled on purpose - pass force=true to resume it anyway"}
    pid = _start(d)
    return {"resumed": run_id, "engine_pid": pid, "from": st.get("status"),
            "note": "finished agents replay from the journal; running ones are adopted; killed ones continue their own sessions"}


def act_cancel(run_id=None, **_):
    d = _run_dir(run_id)
    st = _state(d)
    _write(os.path.join(d, "cancel"), time.strftime("%Y-%m-%dT%H:%M:%S%z") + "\n")
    stopped = []
    if st.get("status") == "running":
        try:
            os.kill(int(st["pid"]), signal.SIGTERM)
            stopped.append("engine")
        except (OSError, KeyError, ValueError):
            pass
        for _ in range(50):
            if not _pid_alive(st.get("pid"), "runner-"):
                break
            time.sleep(0.1)
    for f in os.listdir(os.path.join(d, "agents")) if os.path.isdir(os.path.join(d, "agents")) else []:
        rec = _read_json(os.path.join(d, "agents", f)) if f.endswith(".json") else None
        if rec and rec.get("status") == "running" and _pid_alive(rec.get("pid"), ""):
            try:
                os.killpg(int(rec["pid"]), signal.SIGTERM)
                stopped.append(rec.get("label") or str(rec["pid"]))
            except (OSError, ValueError):
                pass
    st = _read_json(os.path.join(d, "state.json"), {}) or {}
    if st.get("status") in ("running", "interrupted", "paused", "error", None):
        st["status"] = "cancelled"
        _write_json(os.path.join(d, "state.json"), st)
    return {"cancelled": run_id, "stopped": stopped}


def _pascal(name):
    return "".join(w[:1].upper() + w[1:] for w in re.split(r"[-_]+", name) if w) + "Workflow"


def _agents_dir(agents_dir):
    if agents_dir:
        d = os.path.abspath(os.path.expanduser(agents_dir))
    else:
        d = os.path.dirname(os.path.abspath(__file__))
        if os.path.basename(d) != "agents" and not os.path.isfile(os.path.join(d, "basic_agent.py")):
            raise WorkflowError("give agents_dir: the agents/ folder of the Brainstem that should host the workflow")
    if not os.path.isdir(d):
        raise WorkflowError("no such folder: %s" % d)
    return d


def _block(src, begin, end, body):
    i, j = src.index(begin), src.index(end)
    return src[:i] + begin + "\n" + body + "\n" + src[j:]


def act_mount(name=None, agents_dir=None, **_):
    """Write this file, bound to one workflow, into a Brainstem's agents/ folder: the Brainstem hot-loads it on
    its next request as one tool (e.g. AdversarialFleetWorkflow) that carries its own workflow and engine."""
    doc = _load(name)
    d = _agents_dir(agents_dir)
    if "\'\'\'" in doc["run"] or "\'\'\'" in json.dumps(doc["meta"]):
        raise WorkflowError("this workflow's source contains a triple quote and cannot be embedded")
    with open(os.path.abspath(__file__), encoding="utf-8") as f:
        src = f.read()
    tool = _pascal(doc["name"])
    snake = re.sub(r"[^a-z0-9]+", "_", doc["name"].lower()).strip("_")
    manifest = dict(__manifest__, name=__manifest__["name"].split("/")[0] + "/" + snake + "_workflow",
                    version=str(doc.get("version") or "1.0.0"), display_name=tool,
                    description=doc["meta"]["description"].split(". ")[0][:240] + ".",
                    tags=["workflow", "dynamic-workflow", doc["name"]])
    src = _block(src, "# ---- manifest (mount rewrites this block) ----", "# ---- end manifest ----",
                 "__manifest__ = " + json.dumps(manifest, indent=4))
    body = ("BUILTINS = {\n    %r: {\n        \"version\": %r,\n        \"meta\": json.loads(r\'\'\'%s\'\'\'),\n"
            "        \"run\": r\'\'\'%s\'\'\',\n    },\n}") % (doc["name"], str(doc.get("version") or "1.0.0"), json.dumps(doc["meta"]), doc["run"])
    src = _block(src, "# ---- builtins (mount rewrites this block) ----", "# ---- end builtins ----", body)
    bound = "BOUND_WORKFLOW = %r  # `mount` bound this copy to one workflow" % doc["name"]
    src = re.sub(r"^BOUND_WORKFLOW = .*$", lambda m: bound, src, count=1, flags=re.M)
    src = re.sub(r'^(""")', lambda m: MOUNT_MARK + " %s (workflow %s %s, sha %s)\n" % (ENGINE_VERSION, doc["name"], doc.get("version"), doc["sha256"][:12]) + m.group(1), src, count=1, flags=re.M)
    path = os.path.join(d, snake + "_workflow_agent.py")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            if MOUNT_MARK not in f.read(400):
                raise WorkflowError("%s exists and was not mounted by this agent - not overwriting it" % path)
    tmp = os.path.join(d, "." + snake + "_workflow.mounting.py")  # never matches the *_agent.py hot-load glob
    _write(tmp, src)
    check = subprocess.run([sys.executable, "-c", "import importlib.util,sys;s=importlib.util.spec_from_file_location('m',sys.argv[1]);"
                            "m=importlib.util.module_from_spec(s);s.loader.exec_module(m);a=m.DynamicWorkflowAgent();print(a.name)", tmp],
                           capture_output=True, text=True, timeout=60, cwd=d)
    if check.returncode != 0 or check.stdout.strip() != tool:
        os.remove(tmp)
        raise WorkflowError("the mounted copy did not load: " + (check.stderr.strip().splitlines() or ["?"])[-1])
    os.replace(tmp, path)
    return {"mounted": path, "tool": tool, "workflow": doc["name"], "version": doc.get("version"),
            "note": "a Brainstem hot-loads it on its next request; action=unmount removes it"}


def act_unmount(name=None, agents_dir=None, **_):
    d = _agents_dir(agents_dir)
    snake = re.sub(r"[^a-z0-9]+", "_", _check_name(name).lower()).strip("_")
    path = os.path.join(d, snake + "_workflow_agent.py")
    if not os.path.exists(path):
        return {"unmounted": False, "note": "nothing mounted for %s in %s" % (name, d)}
    with open(path, encoding="utf-8") as f:
        if MOUNT_MARK not in f.read(400):
            raise WorkflowError("%s was not mounted by this agent - not removing it" % path)
    os.remove(path)
    return {"unmounted": path, "note": "the Brainstem drops the tool on its next request"}


def dispatch(action, **kw):
    allowed = BOUND_ACTIONS if BOUND_WORKFLOW else ACTIONS
    fn = globals().get("act_" + str(action))
    if action not in allowed or fn is None:
        raise WorkflowError("action must be one of: " + ", ".join(allowed))
    if BOUND_WORKFLOW and action not in ("runs",):
        kw = dict(kw, name=BOUND_WORKFLOW) if action in ("run", "show") else kw
    return fn(**kw)


class DynamicWorkflowAgent(BasicAgent):
    def __init__(self):
        if BOUND_WORKFLOW:
            meta = BUILTINS[BOUND_WORKFLOW]["meta"]
            args_schema = meta.get("argsSchema") or {"type": "object"}
            self.name = _pascal(BOUND_WORKFLOW)
            self.metadata = {
                "name": self.name,
                "description": meta["description"] + " Runs survive crashes and restarts: action=status to watch, resume after a restart.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": list(BOUND_ACTIONS), "description": "run starts it; status/result read a run"},
                        "args": dict(args_schema, description="the workflow's arguments (ctx.args)"),
                        "preset": {"type": "string", "description": "a saved set of args for this workflow"},
                        "run_id": {"type": "string", "description": "a run's id (from run or runs)"},
                        "max_concurrent": {"type": "integer", "description": "for run: subagents at once (default 8)"},
                    },
                    "required": ["action"],
                },
            }
            super().__init__(self.name, self.metadata)
            return
        self.name = "DynamicWorkflow"
        self.metadata = {
            "name": self.name,
            "description": ("Save, run and resume governed multi-subagent workflows (a fleet of Copilot subagents that "
                            "review, refute, build and prove) from a durable library; runs survive crashes and restarts. "
                            "Use action=list to see workflows, run to start one, status to watch it, resume after a restart."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": list(ACTIONS), "description": "what to do"},
                    "name": {"type": "string", "description": "workflow name (list shows them)"},
                    "run_id": {"type": "string", "description": "a run's id (from run or runs)"},
                    "preset": {"type": "string", "description": "a saved set of args for the workflow"},
                    "args": {"type": "object", "description": "the JSON object the workflow receives as ctx.args"},
                    "meta": {"type": "object", "description": "for save: {name, description, phases, argsSchema?}"},
                    "run": {"type": "string", "description": "for save: the workflow body, async (ctx) => { ... }"},
                    "max_concurrent": {"type": "integer", "description": "for run: subagents at once (default 8)"},
                    "replay_from": {"type": "string", "description": "for run: an earlier run whose settled identical agent calls are reused"},
                    "agents_dir": {"type": "string", "description": "optional, for mount/unmount - leave it out: it defaults to the agents/ folder this Brainstem loaded me from"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, action=None, **kwargs):
        action = action or ("run" if BOUND_WORKFLOW else "list")
        try:
            out = dispatch(action, **kwargs)
            return json.dumps(out, indent=1, default=str)
        except WorkflowError as e:
            return json.dumps({"status": "refused", "action": action, "reason": str(e)})
        except Exception as e:  # errors are data, never content
            return json.dumps({"status": "error", "action": action, "error": "%s: %s" % (type(e).__name__, e)})


def main(argv=None):
    p = argparse.ArgumentParser(prog="dynamic_workflow_agent.py", description="Save, run and resume governed multi-subagent workflows.")
    p.add_argument("action", nargs="?", default="run" if BOUND_WORKFLOW else "list", choices=BOUND_ACTIONS if BOUND_WORKFLOW else ACTIONS)
    p.add_argument("--name")
    p.add_argument("--run-id")
    p.add_argument("--preset")
    p.add_argument("--args")
    p.add_argument("--args-file")
    p.add_argument("--meta-file")
    p.add_argument("--run-file")
    p.add_argument("--version")
    p.add_argument("--max-concurrent", type=int)
    p.add_argument("--agent-timeout-s", type=int)
    p.add_argument("--keep-mcp", action="store_true")
    p.add_argument("--force", action="store_true")
    p.add_argument("--lines", type=int, default=14)
    p.add_argument("--agents-dir")
    p.add_argument("--replay-from")
    a = p.parse_args(argv)
    kw = {"name": a.name, "run_id": a.run_id, "preset": a.preset, "max_concurrent": a.max_concurrent,
          "agent_timeout_s": a.agent_timeout_s, "keep_mcp": a.keep_mcp, "force": a.force, "lines": a.lines,
          "agents_dir": a.agents_dir, "replay_from": a.replay_from}
    if a.args_file:
        with open(a.args_file, encoding="utf-8") as f:
            kw["args"] = json.load(f)
    elif a.args:
        kw["args"] = a.args
    if a.meta_file:
        with open(a.meta_file, encoding="utf-8") as f:
            kw["meta"] = json.load(f)
    if a.run_file:
        with open(a.run_file, encoding="utf-8") as f:
            kw["run"] = f.read()
    if a.version:
        kw["version"] = a.version
    out = DynamicWorkflowAgent().perform(action=a.action, **{k: v for k, v in kw.items() if v is not None})
    print(out)
    return 0 if '"status": "refused"' not in out and '"status": "error"' not in out else 1


if __name__ == "__main__":
    sys.exit(main())
