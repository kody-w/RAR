#!/usr/bin/env node
/**
 * Test harness: runs every agent .py through the unrapp transpiler + JS eval.
 * Reports: transpile errors, data extraction gaps, compile failures, eval failures.
 *
 * Usage: node tests/test_unrapp_all_agents.mjs
 */

import { readFileSync, readdirSync, statSync } from 'fs';
import { join, relative } from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT = join(__dirname, '..');

// ─── Extract JS from virtual-brainstem.html ─────────────────────────
const html = readFileSync(join(ROOT, 'virtual-brainstem.html'), 'utf-8');

// Extract everything between <script> and </script>
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) { console.error('Could not find <script> block'); process.exit(1); }
const fullScript = scriptMatch[1];

// We need sections 1 (lispy) + 2 (unrapp transpiler) + beginning of 3 (runtime helpers)
// We'll eval the whole script with DOM stubs

// ─── DOM & browser stubs ────────────────────────────────────────────
const _stubEl = () => ({ value: '', textContent: '', innerHTML: '', style: {}, classList: { add(){}, remove(){}, toggle(){}, contains(){ return false; } }, addEventListener(){}, removeEventListener(){}, querySelector(){ return null; }, querySelectorAll(){ return []; }, appendChild(c){ return c; }, removeChild(){}, closest(){ return null; }, focus(){}, blur(){}, click(){}, scrollTo(){}, getBoundingClientRect(){ return {}; }, dataset: {}, checked: false, disabled: false, options: [], selectedIndex: -1, files: [], offsetWidth: 0, offsetHeight: 0, parentNode: null, parentElement: null, children: [], firstChild: null, nextSibling: null, setAttribute(){}, getAttribute(){ return null; }, hasAttribute(){ return false; }, remove(){}, cloneNode(){ return _stubEl(); }, dispatchEvent(){ return true; }, replaceWith(){}, insertBefore(c){ return c; }, contains(){ return false; } });
globalThis.document = {
  getElementById: () => _stubEl(),
  querySelector: () => null,
  querySelectorAll: () => [],
  createElement: () => _stubEl(),
  createTextNode: (t) => ({ textContent: t }),
  createElementNS: () => _stubEl(),
  body: { ..._stubEl(), style: {} },
  head: { appendChild(){} },
  title: '',
  addEventListener(){},
  removeEventListener(){},
  createDocumentFragment(){ return _stubEl(); },
  cookie: '',
};
globalThis.window = {
  addEventListener(){},
  removeEventListener(){},
  location: { hash: '', hostname: 'localhost', pathname: '/', search: '', href: '' },
  history: { pushState(){}, replaceState(){} },
  localStorage: { getItem(){ return null; }, setItem(){}, removeItem(){} },
  sessionStorage: { getItem(){ return null; }, setItem(){}, removeItem(){} },
  getComputedStyle(){ return {}; },
  requestAnimationFrame(cb){ cb(); },
  setTimeout: globalThis.setTimeout,
  clearTimeout: globalThis.clearTimeout,
  setInterval: globalThis.setInterval,
  clearInterval: globalThis.clearInterval,
  matchMedia(){ return { matches: false, addEventListener(){} }; },
  innerWidth: 1024,
  innerHeight: 768,
  scrollTo(){},
  open(){ return null; },
  crypto: { randomUUID(){ return 'test-uuid'; } },
  navigator: { clipboard: { writeText(){ return Promise.resolve(); } } },
};
try { globalThis.navigator = { userAgent: 'node-test', clipboard: { writeText(){ return Promise.resolve(); } } }; } catch(e) {}
globalThis.localStorage = { _d: {}, getItem(k){ return this._d[k] ?? null; }, setItem(k,v){ this._d[k] = String(v); }, removeItem(k){ delete this._d[k]; }, get length(){ return Object.keys(this._d).length; }, key(i){ return Object.keys(this._d)[i] ?? null; }, clear(){ this._d = {}; } };
globalThis.sessionStorage = { ...globalThis.localStorage, _d: {} };
globalThis.fetch = async () => ({ ok: false, status: 404, text: async () => '', json: async () => ({}) });
globalThis.performance = { now: () => Date.now() };
globalThis.MutationObserver = class { observe(){} disconnect(){} };
globalThis.IntersectionObserver = class { observe(){} disconnect(){} };
globalThis.ResizeObserver = class { observe(){} disconnect(){} };
globalThis.URL = globalThis.URL || class { constructor(u){ this.href = u; } };
globalThis.Blob = class { constructor(){} };
globalThis.FileReader = class { readAsText(){} addEventListener(){} };
globalThis.DragEvent = class {};
globalThis.ClipboardEvent = class {};
globalThis.KeyboardEvent = class {};
globalThis.Event = globalThis.Event || class { constructor(t){ this.type = t; } };
globalThis.CustomEvent = globalThis.CustomEvent || class { constructor(t,d){ this.type = t; this.detail = d?.detail; } };
globalThis.HTMLElement = globalThis.HTMLElement || class {};
globalThis.alert = () => {};
globalThis.confirm = () => true;
globalThis.prompt = () => '';
globalThis.getComputedStyle = () => ({});
globalThis.requestAnimationFrame = (cb) => cb();

// ─── Eval the script to get all functions ───────────────────────────
// Wrap in a function to capture all the declarations
const wrappedScript = `
${fullScript}

// Export what we need
return {
  unrappTranspile,
  transpileAndLoad,
  runOperation,
  createGlobalEnv,
  lispParse,
  lispEval,
  LispEnv,
  NIL,
  displayValue,
};
`;

let mod;
try {
  const factory = new Function(wrappedScript);
  mod = factory();
} catch(e) {
  console.error('Failed to eval brainstem script:', e.message);
  // Try to find the line
  const lines = wrappedScript.split('\n');
  console.error('Near:', e.stack?.match(/anonymous>:(\d+)/)?.[1]);
  process.exit(1);
}

const { unrappTranspile, createGlobalEnv, lispParse, lispEval, NIL, displayValue } = mod;

// ─── Discover all agent .py files ───────────────────────────────────
function findAgents(dir) {
  const results = [];
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    try {
      const st = statSync(full);
      if (st.isDirectory()) results.push(...findAgents(full));
      else if (entry.endsWith('_agent.py')) results.push(full);
    } catch(e) {}
  }
  return results;
}

const agentsDir = join(ROOT, 'agents');
const agentFiles = findAgents(agentsDir).sort();
console.log(`\nFound ${agentFiles.length} agent files\n`);

// ─── Test each agent ────────────────────────────────────────────────

const results = {
  total: agentFiles.length,
  transpileOk: 0,
  transpileErrors: [],
  dataExtractFail: [],   // has _UPPER dicts in source but 0 extracted
  compileFail: [],
  evalFail: [],          // LisPy eval fails
  operationFail: [],     // running an operation fails
  fullPass: 0,
};

for (const file of agentFiles) {
  const rel = relative(ROOT, file);
  const src = readFileSync(file, 'utf-8');

  // Step 1: Transpile
  let result;
  try {
    result = unrappTranspile(src);
  } catch(e) {
    results.transpileErrors.push({ file: rel, error: e.message });
    continue;
  }

  if (result.errors.length > 0) {
    results.transpileErrors.push({ file: rel, error: result.errors.join('; ') });
    // Still continue to test what we can
  }

  results.transpileOk++;

  // Step 2: Check data extraction
  // Count _UPPER_CASE = { or UPPER_CASE = { dicts in source
  const srcDicts = [...src.matchAll(/^_?[A-Z][A-Z_0-9]+\s*=\s*[\{\[]/gm)].length;
  const manifestCount = (src.match(/__manifest__/g) || []).length > 0 ? 1 : 0;
  const expectedDicts = srcDicts - manifestCount;
  const extractedDicts = Object.keys(result.dataObjects || {}).length;
  if (expectedDicts > 0 && extractedDicts === 0) {
    results.dataExtractFail.push({ file: rel, expected: expectedDicts, got: extractedDicts });
  }

  // Step 3: Compile JS functions
  const PY = {
    len: x => { if (x == null) return 0; if (typeof x === 'object') return Array.isArray(x) ? x.length : Object.keys(x).length; return String(x).length; },
    int: x => Math.trunc(Number(x)) || 0,
    float: x => Number(x) || 0,
    str: x => String(x),
    list: x => { if (x == null) return []; if (Array.isArray(x)) return [...x]; if (typeof x === 'object') return Object.keys(x); return [x]; },
    sorted: (x, opts) => { const arr = Array.isArray(x) ? [...x] : Object.keys(x); if (opts?.key) arr.sort((a,b) => { const ka=opts.key(a), kb=opts.key(b); return ka<kb?-1:ka>kb?1:0; }); else arr.sort((a,b)=>a<b?-1:a>b?1:0); if (opts?.reverse) arr.reverse(); return arr; },
    sum: x => Array.isArray(x) ? x.reduce((a,b) => a+b, 0) : 0,
    max: (...args) => args.length===1 && Array.isArray(args[0]) ? Math.max(...args[0]) : Math.max(...args),
    min: (...args) => args.length===1 && Array.isArray(args[0]) ? Math.min(...args[0]) : Math.min(...args),
    abs: Math.abs,
    round: (n, d) => { if (d===undefined) return Math.round(n); const f = Math.pow(10, d); return Math.round(n * f) / f; },
    range: (...args) => { let s=0,e=0,step=1; if(args.length===1)e=args[0]; else if(args.length>=2){s=args[0];e=args[1];} if(args.length>=3)step=args[2]; const r=[]; if(step>0)for(let i=s;i<e;i+=step)r.push(i); else for(let i=s;i>e;i+=step)r.push(i); return r; },
    all: x => Array.isArray(x) ? x.every(Boolean) : Boolean(x),
    any: x => Array.isArray(x) ? x.some(Boolean) : Boolean(x),
    dict: x => x == null ? {} : Object.fromEntries(x),
    enumerate: x => Array.isArray(x) ? x.map((v,i) => [i,v]) : [],
    zip: (...arrs) => { const len = Math.min(...arrs.map(a=>a.length)); return Array.from({length:len}, (_,i) => arrs.map(a=>a[i])); },
    isinstance: () => true,
    get: (obj, key, dflt) => { if (obj == null) return dflt !== undefined ? dflt : null; const v = obj[key]; return v !== undefined ? v : (dflt !== undefined ? dflt : null); },
  };

  const DATA = result.dataObjects || {};
  const HELPERS = {};
  const jsFns = result.jsFunctions || {};
  let compileErrors = [];

  // Synthetic self for class method references
  const self = {
    name: (result.manifest || {}).display_name || (result.manifest || {}).name || 'Agent',
    metadata: result.manifest || {},
  };

  function compileAgentFn(fnDef) {
    const paramList = fnDef.params.join(', ');
    let body = fnDef.body;
    body = body.replace(/^\s*let\s+/gm, 'var ');
    // .get() -> PY.get()
    for (let pass = 0; pass < 3; pass++) {
      let newBody = '', idx = 0;
      while (idx < body.length) {
        const rest = body.slice(idx);
        const gm = rest.match(/^([a-zA-Z_]\w*(?:\[[^\]]*\])*)\.get\(/);
        if (gm) {
          const obj = gm[1];
          if (['Math','Number','String','Array','Object','JSON','Map','Set','PY'].includes(obj)) {
            newBody += body[idx]; idx++; continue;
          }
          const argsStart = idx + gm[0].length;
          let d = 1, j = argsStart, inS = false, sCh = '';
          while (j < body.length && d > 0) {
            const c = body[j];
            if (inS) { if (c === '\\') j++; else if (c === sCh) inS = false; }
            else { if (c==='"'||c==="'") { inS=true; sCh=c; } else if ('([{'.includes(c)) d++; else if (')]}'.includes(c)) d--; }
            j++;
          }
          const args = body.slice(argsStart, j - 1);
          newBody += `PY.get(${obj}, ${args})`;
          idx = j;
        } else { newBody += body[idx]; idx++; }
      }
      body = newBody;
    }
    body = body.replace(/(\w+)\.values\(\)/g, 'Object.values($1)');
    body = body.replace(/(\w+)\.keys\(\)/g, 'Object.keys($1)');
    body = body.replace(/(\w+)\.items\(\)/g, 'Object.entries($1)');
    const pyBuiltinReplacements = ['len','int','sorted','list','sum','round','abs','all','any','range','str','float'];
    for (const b of pyBuiltinReplacements) {
      body = body.replace(new RegExp('(?<!\\.)\\b' + b + '\\(', 'g'), 'PY.' + b + '(');
    }
    const fnCode = `(function(${paramList}) {\n${body}\n})`;
    return (new Function('DATA', 'HELPERS', 'PY', 'self', `return ${fnCode}`))(DATA, HELPERS, PY, self);
  }

  // Compile helpers first
  for (const [name, fnDef] of Object.entries(jsFns)) {
    if (!fnDef.isHelper) continue;
    try {
      HELPERS[name] = compileAgentFn(fnDef);
    } catch(e) {
      compileErrors.push(`helper ${name}: ${e.message}`);
    }
  }

  // Compile methods
  const ops = {};
  for (const [name, fnDef] of Object.entries(jsFns)) {
    if (!fnDef.isMethod) continue;
    try {
      const compiled = compileAgentFn(fnDef);
      const opName = name.replace(/^method_/, '');
      HELPERS['method_' + opName] = compiled;
      ops[opName] = compiled;
    } catch(e) {
      compileErrors.push(`method ${name}: ${e.message}`);
    }
  }

  if (compileErrors.length > 0) {
    results.compileFail.push({ file: rel, errors: compileErrors });
  }

  // Step 4: Eval LisPy dispatcher
  let env;
  try {
    env = createGlobalEnv();
    for (const [name, obj] of Object.entries(DATA)) {
      env.define(name, obj);
    }
    // Register helpers
    for (const [name, fn] of Object.entries(HELPERS)) {
      if (name.startsWith('method_')) {
        const opName = name.replace(/^method_/, '');
        env.define(`op-${opName}`, (kwargs) => {
          try { return fn(kwargs || {}); }
          catch(e) { return `Error in ${opName}: ${e.message}`; }
        });
      } else {
        env.define(name.replace(/_/g, '-'), (...args) => fn(...args));
      }
    }

    if (result.lispy) {
      const exprs = lispParse(result.lispy);
      for (const expr of exprs) lispEval(expr, env);
    }
  } catch(e) {
    results.evalFail.push({ file: rel, error: e.message });
    continue; // Can't run operations if eval failed
  }

  // Step 5: Run each operation
  const operations = result.operations || [];
  let opErrors = [];
  for (const opName of operations) {
    try {
      const kwargsExpr = `(make-dict "operation" "${opName}")`;
      const callExpr = `(perform ${kwargsExpr})`;
      const exprs = lispParse(callExpr);
      let opResult = NIL;
      for (const expr of exprs) opResult = lispEval(expr, env);
      const output = displayValue(opResult);
      // Check if the output contains an error
      if (output && (output.includes('is not defined') || output.includes('Cannot read prop') || output.includes('is not a function'))) {
        opErrors.push({ op: opName, error: output.slice(0, 200) });
      }
    } catch(e) {
      opErrors.push({ op: opName, error: e.message.slice(0, 200) });
    }
  }

  if (opErrors.length > 0) {
    results.operationFail.push({ file: rel, operations: opErrors });
  }

  if (compileErrors.length === 0 && opErrors.length === 0 && result.errors.length === 0) {
    results.fullPass++;
  }
}

// ─── Report ─────────────────────────────────────────────────────────
console.log('\n' + '═'.repeat(70));
console.log('UNRAPP TRANSPILER — FULL AGENT TEST REPORT');
console.log('═'.repeat(70));
console.log(`Total agents:        ${results.total}`);
console.log(`Transpile OK:        ${results.transpileOk}`);
console.log(`Full pass (no errs): ${results.fullPass}`);
console.log('');

if (results.transpileErrors.length > 0) {
  console.log(`\n── TRANSPILE ERRORS (${results.transpileErrors.length}) ──`);
  for (const { file, error } of results.transpileErrors) {
    console.log(`  ${file}`);
    console.log(`    ${error.slice(0, 200)}`);
  }
}

if (results.dataExtractFail.length > 0) {
  console.log(`\n── DATA EXTRACTION FAILURES (${results.dataExtractFail.length}) ──`);
  for (const { file, expected, got } of results.dataExtractFail) {
    console.log(`  ${file}  (expected ~${expected} dicts, got ${got})`);
  }
}

if (results.compileFail.length > 0) {
  console.log(`\n── COMPILE FAILURES (${results.compileFail.length}) ──`);
  for (const { file, errors } of results.compileFail) {
    console.log(`  ${file}`);
    for (const e of errors) console.log(`    ${e.slice(0, 200)}`);
  }
}

if (results.evalFail.length > 0) {
  console.log(`\n── LISPY EVAL FAILURES (${results.evalFail.length}) ──`);
  for (const { file, error } of results.evalFail) {
    console.log(`  ${file}`);
    console.log(`    ${error.slice(0, 200)}`);
  }
}

if (results.operationFail.length > 0) {
  console.log(`\n── OPERATION FAILURES (${results.operationFail.length}) ──`);
  for (const { file, operations } of results.operationFail) {
    console.log(`  ${file}`);
    for (const { op, error } of operations) {
      console.log(`    ${op}: ${error.slice(0, 150)}`);
    }
  }
}

const failCount = results.transpileErrors.length + results.compileFail.length + results.evalFail.length + results.operationFail.length;
console.log('\n' + '═'.repeat(70));
if (failCount === 0) {
  console.log('ALL AGENTS PASSED');
} else {
  console.log(`${failCount} agents have issues (${results.fullPass}/${results.total} clean)`);
}
console.log('═'.repeat(70));

process.exit(failCount > 0 ? 1 : 0);
