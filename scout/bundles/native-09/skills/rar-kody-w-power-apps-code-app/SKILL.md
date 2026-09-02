---
name: "rar-kody-w-power-apps-code-app"
description: "Generates a complete Power Apps code app (vite + React + @microsoft/power-apps) from a structured spec, deploys it via the PAC CLI (pac code init / npm build / pac code push), and packages it for team sharing - a portable source zip with one-command deploy scripts, plus an ALM solution zip where the environment supports code-app solution components."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/power_apps_code_app_agent", "rar_sha256": "fbcd47231e85c44efedbdc661b1e20da4f8cc77f45bbc20d53d7355c25269a10", "source_kind": "rar-agent", "source_commit": "13ba36d938ea0d393c9d863b411b4ed0096648de", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "power_apps_code_app_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/power-apps-code-app:0f812757911fed5ff8eadd05cb7ced043933dba8d351b236f7512e2aa30f9163", "kind": "skill"}, "version": "1.1.1", "author": "kody-w", "tags": ["power-apps", "code-apps", "pac", "power-platform", "codegen", "deploy", "package", "alm", "vite", "react"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/power_apps_code_app_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `power_apps_code_app_agent.py` is
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

Power Apps Code App generator + deployer (RAPP brainstem).

Generates a complete Power Apps *code app* (the `pac code` path: vite +
React + @microsoft/power-apps SDK) from a structured spec supplied by the
host LLM, then deploys it to a Power Platform environment via the PAC CLI.

Operations:
  - status    readiness report: pac CLI, npm/node, pac auth profile, env
  - generate  scaffold a full buildable code app from the spec (offline-safe)
  - deploy    build an already-generated app and `pac code push` it
  - full      generate + deploy in one call (default)
  - list      list previously generated code apps and their state
  - package   emit shareable artifacts for other Power Platform environments:
              ALWAYS a portable source zip (project + deploy.sh/deploy.ps1 that
              re-init against the teammate's env), and — when solution_name is
              given — a native solution .zip via `pac code push --solutionName`
              + `pac solution export` for standard ALM import

Prototype doctrine: generated apps ship with real end-to-end UI logic and
mocked seed rows derived from the data entities (localStorage-persisted),
so the app is demoable the second it lands — swapping mock for live data
(Dataverse/connector) is a data-plane change, not a rewrite.

Apps live under .brainstem_data/code_apps/<slug>/ next to the brainstem.

Deployment prerequisites (reported by `status`, never assumed):
  - PAC CLI on PATH (`pac`) with the `pac code` command group
  - an authenticated profile: `pac auth create --environment <env-url>`
  - the target environment must have Code Apps enabled (admin setting)

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_apps_code_app_agent.py` and embedded as the fenced Python below (sha256 fbcd47231e85c44e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_apps_code_app_agent.py` first:

```bash
python3 power_apps_code_app_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 power_apps_code_app_agent.py   # or on stdin
python3 power_apps_code_app_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""Power Apps Code App generator + deployer (RAPP brainstem).

Generates a complete Power Apps *code app* (the `pac code` path: vite +
React + @microsoft/power-apps SDK) from a structured spec supplied by the
host LLM, then deploys it to a Power Platform environment via the PAC CLI.

Operations:
  - status    readiness report: pac CLI, npm/node, pac auth profile, env
  - generate  scaffold a full buildable code app from the spec (offline-safe)
  - deploy    build an already-generated app and `pac code push` it
  - full      generate + deploy in one call (default)
  - list      list previously generated code apps and their state
  - package   emit shareable artifacts for other Power Platform environments:
              ALWAYS a portable source zip (project + deploy.sh/deploy.ps1 that
              re-init against the teammate's env), and — when solution_name is
              given — a native solution .zip via `pac code push --solutionName`
              + `pac solution export` for standard ALM import

Prototype doctrine: generated apps ship with real end-to-end UI logic and
mocked seed rows derived from the data entities (localStorage-persisted),
so the app is demoable the second it lands — swapping mock for live data
(Dataverse/connector) is a data-plane change, not a rewrite.

Apps live under .brainstem_data/code_apps/<slug>/ next to the brainstem.

Deployment prerequisites (reported by `status`, never assumed):
  - PAC CLI on PATH (`pac`) with the `pac code` command group
  - an authenticated profile: `pac auth create --environment <env-url>`
  - the target environment must have Code Apps enabled (admin setting)
"""

from __future__ import annotations


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/power_apps_code_app_agent",
    "version": "1.1.1",
    "display_name": "PowerAppsCodeApp",
    "description": "Generates a complete Power Apps code app (vite + React + @microsoft/power-apps) from a structured spec, deploys it via the PAC CLI (pac code init / npm build / pac code push), and packages it for team sharing - a portable source zip with one-command deploy scripts, plus an ALM solution zip where the environment supports code-app solution components.",
    "author": "kody-w",
    "tags": ["power-apps", "code-apps", "pac", "power-platform", "codegen", "deploy", "package", "alm", "vite", "react"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


import json
import os
import re
import shutil
import subprocess
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except Exception:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata

APPS_ROOT = Path(__file__).resolve().parent.parent / ".brainstem_data" / "code_apps"

NPM_INSTALL_TIMEOUT = 600
BUILD_TIMEOUT = 300
PUSH_TIMEOUT = 600

FIELD_TYPES = ("text", "number", "date", "boolean", "choice", "email", "currency")


# ---------------------------------------------------------------- helpers

def _slug(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")
    return s or "code-app"


def _run(cmd, cwd=None, timeout=120):
    """Run a command, return (ok, combined_output). Never raises."""
    try:
        p = subprocess.run(
            cmd, cwd=str(cwd) if cwd else None, timeout=timeout,
            capture_output=True, text=True, shell=isinstance(cmd, str))
        out = ((p.stdout or "") + "\n" + (p.stderr or "")).strip()
        return p.returncode == 0, out
    except subprocess.TimeoutExpired:
        return False, f"TIMEOUT after {timeout}s: {cmd}"
    except FileNotFoundError:
        return False, f"NOT FOUND: {cmd[0] if isinstance(cmd, list) else cmd}"
    except Exception as e:
        return False, f"ERROR: {e}"


def _pac() -> str | None:
    return shutil.which("pac")


def _npm() -> str | None:
    return shutil.which("npm")


def _mock_value(field: dict, i: int):
    """Deterministic seed value for a field, by declared type."""
    name = field.get("name", "field")
    ftype = (field.get("type") or "text").lower()
    if ftype == "number":
        return (i + 1) * 7
    if ftype == "currency":
        return round(1250.0 * (i + 1), 2)
    if ftype == "date":
        return f"2026-0{(i % 9) + 1}-1{i % 3}"
    if ftype == "boolean":
        return i % 2 == 0
    if ftype == "choice":
        opts = field.get("options") or ["New", "Active", "Closed"]
        return opts[i % len(opts)]
    if ftype == "email":
        return f"contact{i + 1}@example.com"
    return f"Sample {name} {i + 1}"


def _normalize_entities(data_entities, description: str):
    """Accept list/JSON-string/None; always return a usable entity list."""
    if isinstance(data_entities, str):
        try:
            data_entities = json.loads(data_entities)
        except Exception:
            data_entities = None
    entities = []
    for e in data_entities or []:
        if not isinstance(e, dict) or not e.get("name"):
            continue
        fields = []
        for f in e.get("fields") or []:
            if isinstance(f, str):
                f = {"name": f, "type": "text"}
            if isinstance(f, dict) and f.get("name"):
                f.setdefault("type", "text")
                fields.append(f)
        if not fields:
            fields = [{"name": "title", "type": "text"},
                      {"name": "status", "type": "choice",
                       "options": ["New", "Active", "Closed"]},
                      {"name": "updated", "type": "date"}]
        entities.append({"name": e["name"], "fields": fields})
    if not entities:
        entities = [{"name": "Items", "fields": [
            {"name": "title", "type": "text"},
            {"name": "status", "type": "choice",
             "options": ["New", "In Progress", "Done"]},
            {"name": "due", "type": "date"},
        ]}]
    return entities


# ------------------------------------------------------------- templates

def _package_json(slug: str) -> str:
    return json.dumps({
        "name": slug,
        "private": True,
        "version": "0.1.0",
        "type": "module",
        "scripts": {
            # Code apps dev loop: vite on :3000 alongside `pac code run`
            "dev": "concurrently \"vite\" \"pac code run\"",
            "build": "vite build",
            "preview": "vite preview",
        },
        "dependencies": {
            "@microsoft/power-apps": "^0.3.1",
            "react": "^18.3.1",
            "react-dom": "^18.3.1",
        },
        "devDependencies": {
            "@types/react": "^18.3.3",
            "@types/react-dom": "^18.3.0",
            "@vitejs/plugin-react": "^4.3.1",
            "concurrently": "^9.0.0",
            "typescript": "^5.5.3",
            "vite": "^5.4.0",
        },
    }, indent=2)


VITE_CONFIG = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Power Apps code apps require the dev server on port 3000 and relative asset paths.
export default defineConfig({
  plugins: [react()],
  base: './',
  server: { host: '::', port: 3000 },
})
"""

TSCONFIG = json.dumps({
    "compilerOptions": {
        "target": "ES2020", "useDefineForClassFields": True,
        "lib": ["ES2020", "DOM", "DOM.Iterable"], "module": "ESNext",
        "skipLibCheck": True, "moduleResolution": "bundler",
        "allowImportingTsExtensions": True, "resolveJsonModule": True,
        "isolatedModules": True, "noEmit": True, "jsx": "react-jsx",
        "strict": True,
    },
    "include": ["src"],
}, indent=2)


def _index_html(title: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
"""


POWER_PROVIDER = """import { initialize } from '@microsoft/power-apps/app';
import { useEffect, type ReactNode } from 'react';

interface PowerProviderProps { children: ReactNode }

export default function PowerProvider({ children }: PowerProviderProps) {
  useEffect(() => {
    const initApp = async () => {
      try {
        await initialize();
        console.log('Power Platform SDK initialized');
      } catch (error) {
        // Outside Power Apps (plain vite dev) initialize() rejects; the app
        // still runs on mock data so local dev is never blocked.
        console.warn('Power Platform SDK not initialized (running standalone):', error);
      }
    };
    initApp();
  }, []);

  return <>{children}</>;
}
"""

MAIN_TSX = """import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import PowerProvider from './PowerProvider.tsx'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <PowerProvider>
      <App />
    </PowerProvider>
  </StrictMode>,
)
"""


def _mock_data_ts(entities, slug: str) -> str:
    seeds = {}
    for e in entities:
        rows = []
        for i in range(4):
            row = {"id": f"{_slug(e['name'])}-{i + 1}"}
            for f in e["fields"]:
                row[f["name"]] = _mock_value(f, i)
            rows.append(row)
        seeds[e["name"]] = rows
    return (
        "// Seed data — real UI logic runs against these rows; swapping to a live\n"
        "// data source (Dataverse / connector) replaces only this module.\n"
        f"export const ENTITIES = {json.dumps(entities, indent=2)} as const;\n\n"
        f"export const SEED_DATA: Record<string, Record<string, unknown>[]> = "
        f"{json.dumps(seeds, indent=2)};\n\n"
        f"export const STORAGE_KEY = 'codeapp:{slug}:data';\n"
    )


def _app_tsx(title: str, description: str, accent: str) -> str:
    return """import { useEffect, useMemo, useState } from 'react'
import { ENTITIES, SEED_DATA, STORAGE_KEY } from './mockData'

type Row = Record<string, unknown>
type Store = Record<string, Row[]>

const ACCENT = '__ACCENT__'

function loadStore(): Store {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (raw) return JSON.parse(raw) as Store
  } catch { /* fall through to seed */ }
  return JSON.parse(JSON.stringify(SEED_DATA)) as Store
}

export default function App() {
  const [store, setStore] = useState<Store>(loadStore)
  const [active, setActive] = useState<string>(ENTITIES[0].name)
  const [query, setQuery] = useState('')
  const [draft, setDraft] = useState<Row>({})
  const [showForm, setShowForm] = useState(false)

  useEffect(() => {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(store)) } catch { /* quota */ }
  }, [store])

  const entity = ENTITIES.find(e => e.name === active) ?? ENTITIES[0]
  const rows = store[entity.name] ?? []
  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase()
    if (!q) return rows
    return rows.filter(r => JSON.stringify(r).toLowerCase().includes(q))
  }, [rows, query])

  const addRow = () => {
    const row: Row = { id: `${entity.name.toLowerCase()}-${Date.now()}` }
    for (const f of entity.fields) row[f.name] = draft[f.name] ?? ''
    setStore(s => ({ ...s, [entity.name]: [row, ...(s[entity.name] ?? [])] }))
    setDraft({}); setShowForm(false)
  }

  const removeRow = (id: unknown) =>
    setStore(s => ({ ...s, [entity.name]: (s[entity.name] ?? []).filter(r => r.id !== id) }))

  const cell = (v: unknown) =>
    typeof v === 'boolean' ? (v ? 'Yes' : 'No') : String(v ?? '')

  return (
    <div style={{ fontFamily: 'Segoe UI, system-ui, sans-serif', minHeight: '100vh', background: '#f5f5f7', color: '#1a1a2e' }}>
      <header style={{ background: ACCENT, color: '#fff', padding: '20px 28px' }}>
        <h1 style={{ margin: 0, fontSize: 22, fontWeight: 600 }}>__TITLE__</h1>
        <p style={{ margin: '4px 0 0', opacity: 0.85, fontSize: 13 }}>__DESCRIPTION__</p>
      </header>

      <div style={{ display: 'flex', gap: 8, padding: '14px 28px', flexWrap: 'wrap', alignItems: 'center' }}>
        {ENTITIES.map(e => (
          <button key={e.name} onClick={() => { setActive(e.name); setShowForm(false) }}
            style={{ padding: '7px 16px', borderRadius: 18, border: 'none', cursor: 'pointer', fontSize: 13,
              background: e.name === active ? ACCENT : '#fff', color: e.name === active ? '#fff' : '#444',
              boxShadow: '0 1px 3px rgba(0,0,0,.12)' }}>
            {e.name} ({(store[e.name] ?? []).length})
          </button>
        ))}
        <span style={{ flex: 1 }} />
        <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Search…"
          style={{ padding: '7px 12px', borderRadius: 8, border: '1px solid #ddd', fontSize: 13, minWidth: 180 }} />
        <button onClick={() => setShowForm(v => !v)}
          style={{ padding: '7px 16px', borderRadius: 8, border: 'none', cursor: 'pointer', fontSize: 13,
            background: ACCENT, color: '#fff' }}>
          {showForm ? 'Cancel' : `+ New ${entity.name.replace(/s$/, '')}`}
        </button>
      </div>

      {showForm && (
        <div style={{ margin: '0 28px 14px', padding: 16, background: '#fff', borderRadius: 10,
          boxShadow: '0 1px 4px rgba(0,0,0,.1)', display: 'flex', gap: 10, flexWrap: 'wrap', alignItems: 'flex-end' }}>
          {entity.fields.map(f => (
            <label key={f.name} style={{ fontSize: 12, color: '#555', display: 'flex', flexDirection: 'column', gap: 4 }}>
              {f.name}
              <input value={String(draft[f.name] ?? '')}
                onChange={e => setDraft(d => ({ ...d, [f.name]: e.target.value }))}
                style={{ padding: '6px 10px', borderRadius: 6, border: '1px solid #ddd', fontSize: 13 }} />
            </label>
          ))}
          <button onClick={addRow} style={{ padding: '8px 18px', borderRadius: 8, border: 'none',
            cursor: 'pointer', background: ACCENT, color: '#fff', fontSize: 13 }}>Save</button>
        </div>
      )}

      <main style={{ padding: '0 28px 40px' }}>
        <div style={{ background: '#fff', borderRadius: 10, boxShadow: '0 1px 4px rgba(0,0,0,.1)', overflowX: 'auto' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
            <thead>
              <tr>
                {entity.fields.map(f => (
                  <th key={f.name} style={{ textAlign: 'left', padding: '10px 14px', borderBottom: '2px solid #eee',
                    color: '#666', fontWeight: 600, textTransform: 'capitalize' }}>{f.name}</th>
                ))}
                <th style={{ width: 40 }} />
              </tr>
            </thead>
            <tbody>
              {filtered.map(r => (
                <tr key={String(r.id)}>
                  {entity.fields.map(f => (
                    <td key={f.name} style={{ padding: '9px 14px', borderBottom: '1px solid #f0f0f0' }}>{cell(r[f.name])}</td>
                  ))}
                  <td style={{ padding: '9px 8px', borderBottom: '1px solid #f0f0f0' }}>
                    <button onClick={() => removeRow(r.id)} title="Delete"
                      style={{ border: 'none', background: 'none', cursor: 'pointer', color: '#bbb' }}>✕</button>
                  </td>
                </tr>
              ))}
              {filtered.length === 0 && (
                <tr><td colSpan={entity.fields.length + 1}
                  style={{ padding: 24, textAlign: 'center', color: '#999' }}>No records</td></tr>
              )}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  )
}
""".replace("__ACCENT__", accent).replace("__TITLE__", title).replace("__DESCRIPTION__", description)


# ------------------------------------------------------------------ agent

class PowerAppsCodeApp(BasicAgent):
    def __init__(self):
        self.name = "PowerAppsCodeApp"
        self.metadata = {
            "name": self.name,
            "description": (
                "Generate and deploy a Power Apps CODE APP (pac code path: "
                "vite + React + @microsoft/power-apps SDK) from what the user "
                "wants. Give it an app_name, a one-line description, and "
                "data_entities describing the records the app manages; it "
                "scaffolds a complete buildable app with a working UI and "
                "mocked seed data, then deploys via PAC CLI (pac code init / "
                "npm build / pac code push) and returns the live app URL. "
                "Call operation=status first to check deploy readiness; use "
                "operation=generate for scaffold-only (no cloud touch)."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["status", "generate", "deploy", "full", "list", "package"],
                        "description": ("status=readiness report; generate=scaffold only; "
                                        "deploy=build+push an existing app; full=generate "
                                        "then deploy (default); list=show generated apps; "
                                        "package=produce shareable zips for other Power "
                                        "Platform environments (portable source zip always; "
                                        "plus an ALM solution .zip when solution_name is set)."),
                    },
                    "app_name": {
                        "type": "string",
                        "description": "Display name of the app, e.g. 'Field Service Tracker'. Required for generate/deploy/full.",
                    },
                    "description": {
                        "type": "string",
                        "description": "One-line description of what the app does, shown in the app header.",
                    },
                    "data_entities": {
                        "type": "array",
                        "description": ("The record types the app manages, derived from the user's "
                                        "needs. Each: {name, fields:[{name, type, options?}]}. "
                                        f"Field types: {', '.join(FIELD_TYPES)}. 'choice' fields "
                                        "may include an options array."),
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "fields": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "name": {"type": "string"},
                                            "type": {"type": "string", "enum": list(FIELD_TYPES)},
                                            "options": {"type": "array", "items": {"type": "string"}},
                                        },
                                        "required": ["name"],
                                    },
                                },
                            },
                            "required": ["name"],
                        },
                    },
                    "app_tsx": {
                        "type": "string",
                        "description": ("OPTIONAL full custom src/App.tsx source (React+TS, default "
                                        "export). Overrides the generated UI when the user needs a "
                                        "bespoke experience beyond the standard record-management UI."),
                    },
                    "accent_color": {
                        "type": "string",
                        "description": "Hex accent color for the app theme, e.g. '#4F46E5'.",
                    },
                    "environment": {
                        "type": "string",
                        "description": ("Power Platform environment URL or GUID to deploy into. "
                                        "Omit to use the PAC auth profile's currently selected environment."),
                    },
                    "solution_name": {
                        "type": "string",
                        "description": ("Dataverse solution unique name (no spaces, e.g. "
                                        "'UnderwriterReferralWorkbench'). With operation=package, "
                                        "associates the code app via `pac code push --solutionName` "
                                        "and exports that solution as an importable .zip. Also "
                                        "honored by deploy/full to push into the solution."),
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # ------------------------------------------------------------- perform

    def perform(self, **kwargs):
        op = (kwargs.get("operation") or "full").lower()
        try:
            if op == "status":
                return self._status(kwargs.get("environment"))
            if op == "list":
                return self._list()
            app_name = (kwargs.get("app_name") or "").strip()
            if not app_name:
                return "ERROR: app_name is required for generate/deploy/full."
            if op == "generate":
                return self._generate(kwargs)[0]
            if op == "deploy":
                return self._deploy(_slug(app_name), app_name, kwargs.get("environment"),
                                    kwargs.get("solution_name"))
            if op == "full":
                gen_report, app_dir = self._generate(kwargs)
                dep_report = self._deploy(app_dir.name, app_name, kwargs.get("environment"),
                                          kwargs.get("solution_name"))
                return gen_report + "\n\n" + dep_report
            if op == "package":
                return self._package(_slug(app_name), app_name,
                                     kwargs.get("solution_name"), kwargs.get("environment"))
            return f"ERROR: unknown operation '{op}'. Use status|generate|deploy|full|list|package."
        except Exception as e:
            return f"ERROR: {type(e).__name__}: {e}"

    # -------------------------------------------------------------- status

    def _status(self, environment=None):
        lines = ["Power Apps Code App readiness:"]
        pac, npm = _pac(), _npm()
        lines.append(f"- pac CLI: {'OK (' + pac + ')' if pac else 'MISSING — install: dotnet tool install --global Microsoft.PowerApps.CLI.Tool'}")
        lines.append(f"- npm:     {'OK (' + npm + ')' if npm else 'MISSING — install Node.js (https://nodejs.org)'}")
        if pac:
            ok, out = _run([pac, "auth", "who"], timeout=60)
            if ok:
                lines.append("- pac auth: OK")
                for ln in out.splitlines():
                    if any(k in ln for k in ("User", "Environment", "Url", "Type")):
                        lines.append(f"    {ln.strip()}")
            else:
                lines.append("- pac auth: NOT AUTHENTICATED — run: pac auth create"
                             + (f" --environment {environment}" if environment else " --environment <env-url>"))
            # `pac code` rejects --help; probe by running the bare group and
            # checking its usage banner (exit code is unreliable here).
            _, out = _run([pac, "code"], timeout=60)
            has_code = "Usage: pac code" in out or "init" in out
            lines.append(f"- pac code command group: {'OK' if has_code else 'MISSING (update PAC CLI: pac install latest)'}")
        lines.append("- NOTE: the target environment must have Code Apps enabled "
                     "(Power Platform admin center > environment > settings > features).")
        return "\n".join(lines)

    # ---------------------------------------------------------------- list

    def _list(self):
        if not APPS_ROOT.exists():
            return "No code apps generated yet."
        rows = []
        for d in sorted(APPS_ROOT.iterdir()):
            if not d.is_dir():
                continue
            state = []
            if (d / "power.config.json").exists():
                state.append("pac-initialized")
            if (d / "dist").exists():
                state.append("built")
            if (d / "node_modules").exists():
                state.append("deps-installed")
            rows.append(f"- {d.name}  [{', '.join(state) or 'scaffold only'}]  {d}")
        return "Generated code apps:\n" + "\n".join(rows) if rows else "No code apps generated yet."

    # ------------------------------------------------------------ generate

    def _generate(self, kwargs):
        app_name = kwargs["app_name"].strip()
        slug = _slug(app_name)
        description = (kwargs.get("description") or f"{app_name} — built with RAPP brainstem").strip()
        accent = kwargs.get("accent_color") or "#4F46E5"
        if not re.fullmatch(r"#[0-9a-fA-F]{6}", accent):
            accent = "#4F46E5"
        entities = _normalize_entities(kwargs.get("data_entities"), description)

        app_dir = APPS_ROOT / slug
        src = app_dir / "src"
        src.mkdir(parents=True, exist_ok=True)

        (app_dir / "package.json").write_text(_package_json(slug))
        (app_dir / "vite.config.ts").write_text(VITE_CONFIG)
        (app_dir / "tsconfig.json").write_text(TSCONFIG)
        (app_dir / "index.html").write_text(_index_html(app_name))
        (app_dir / ".gitignore").write_text("node_modules/\ndist/\n")
        (src / "PowerProvider.tsx").write_text(POWER_PROVIDER)
        (src / "main.tsx").write_text(MAIN_TSX)
        (src / "mockData.ts").write_text(_mock_data_ts(entities, slug))

        custom = kwargs.get("app_tsx")
        if custom and "export default" in custom:
            (src / "App.tsx").write_text(custom)
            ui_note = "custom App.tsx supplied by caller"
        else:
            (src / "App.tsx").write_text(_app_tsx(app_name, description, accent))
            ui_note = f"generated record-management UI ({len(entities)} entit{'y' if len(entities) == 1 else 'ies'}: " \
                      + ", ".join(e["name"] for e in entities) + ")"

        report = (
            f"GENERATED code app '{app_name}' at {app_dir}\n"
            f"- UI: {ui_note}\n"
            f"- Seed data: 4 mocked rows per entity (localStorage-persisted; swap src/mockData.ts for live data later)\n"
            f"- Stack: vite + React 18 + @microsoft/power-apps (PowerProvider initializes the Power SDK)\n"
            f"- Local dev: cd {app_dir} && npm install && npm run dev  (vite on :3000 + pac code run)"
        )
        return report, app_dir

    # -------------------------------------------------------------- deploy

    def _deploy(self, slug, app_name, environment=None, solution_name=None):
        app_dir = APPS_ROOT / slug
        if not (app_dir / "package.json").exists():
            return (f"ERROR: no generated app at {app_dir}. "
                    "Run operation=generate (or full) first.")
        pac, npm = _pac(), _npm()
        if not pac:
            return "ERROR: pac CLI not found. Install: dotnet tool install --global Microsoft.PowerApps.CLI.Tool"
        if not npm:
            return "ERROR: npm not found. Install Node.js from https://nodejs.org"

        log = [f"DEPLOYING '{app_name}' from {app_dir}"]

        ok, out = _run([pac, "auth", "who"], timeout=60)
        if not ok:
            return (f"{log[0]}\nBLOCKED: no PAC auth profile. The user must run "
                    f"(interactive browser sign-in):\n  pac auth create"
                    + (f" --environment {environment}" if environment else " --environment <env-url>")
                    + "\nthen retry operation=deploy.")
        log.append("1. pac auth: OK")

        if environment:
            ok, out = _run([pac, "env", "select", "--environment", environment], timeout=90)
            log.append(f"2. pac env select {environment}: {'OK' if ok else 'FAILED — ' + out[-400:]}")
            if not ok:
                return "\n".join(log)

        if not (app_dir / "power.config.json").exists():
            ok, out = _run([pac, "code", "init", "--displayName", app_name],
                           cwd=app_dir, timeout=180)
            # PAC CLI exits 0 even on errors — the real success signal is the
            # power.config.json it writes.
            ok = ok and (app_dir / "power.config.json").exists()
            log.append(f"3. pac code init: {'OK' if ok else 'FAILED'}\n   {out[-600:]}")
            if not ok:
                log.append("   (Common causes: Code Apps not enabled on the environment, "
                           "or PAC CLI too old — try `pac install latest`.)")
                return "\n".join(log)
        else:
            log.append("3. pac code init: already initialized (power.config.json present)")

        if not (app_dir / "node_modules").exists():
            ok, out = _run([npm, "install", "--no-audit", "--no-fund"],
                           cwd=app_dir, timeout=NPM_INSTALL_TIMEOUT)
            log.append(f"4. npm install: {'OK' if ok else 'FAILED — ' + out[-600:]}")
            if not ok:
                return "\n".join(log)
        else:
            log.append("4. npm install: already installed")

        ok, out = _run([npm, "run", "build"], cwd=app_dir, timeout=BUILD_TIMEOUT)
        log.append(f"5. npm run build: {'OK' if ok else 'FAILED — ' + out[-800:]}")
        if not ok:
            return "\n".join(log)

        push_cmd = [pac, "code", "push"] + (["--solutionName", solution_name] if solution_name else [])
        ok, out = _run(push_cmd, cwd=app_dir, timeout=PUSH_TIMEOUT)
        # Exit code is unreliable; only a returned app URL proves the push landed.
        m = re.search(r"https://\S*powerapps\.com\S*", out)
        ok = ok and m is not None and not re.search(r"(?i)\berror\b|is required|not found", out)
        log.append(f"6. pac code push{' --solutionName ' + solution_name if solution_name else ''}: "
                   f"{'OK' if ok else 'FAILED'}\n   {out[-1000:]}")
        if ok and m:
            log.append(f"\nLIVE APP URL: {m.group(0).rstrip('.,)')}")
        return "\n".join(log)

    # -------------------------------------------------------------- package

    DEPLOY_SH = """#!/usr/bin/env bash
# Deploy this Power Apps code app into YOUR environment.
# Usage: ./deploy.sh [environment-url]   e.g. ./deploy.sh https://yourorg.crm.dynamics.com/
set -euo pipefail
ENV_URL="${1:-}"
command -v pac >/dev/null || { echo "Install PAC CLI: dotnet tool install --global Microsoft.PowerApps.CLI.Tool"; exit 1; }
command -v npm >/dev/null || { echo "Install Node.js: https://nodejs.org"; exit 1; }
pac auth who >/dev/null 2>&1 || pac auth create ${ENV_URL:+--environment "$ENV_URL"}
[ -n "$ENV_URL" ] && pac env select --environment "$ENV_URL"
rm -f power.config.json   # env-bound; re-init against YOUR environment
pac code init --displayName "__APP_NAME__"
npm install --no-audit --no-fund
npm run build
pac code push
"""

    DEPLOY_PS1 = """# Deploy this Power Apps code app into YOUR environment.
# Usage: ./deploy.ps1 [-EnvironmentUrl https://yourorg.crm.dynamics.com/]
param([string]$EnvironmentUrl = "")
$ErrorActionPreference = "Stop"
if (-not (Get-Command pac -ErrorAction SilentlyContinue)) { throw "Install PAC CLI: dotnet tool install --global Microsoft.PowerApps.CLI.Tool" }
if (-not (Get-Command npm -ErrorAction SilentlyContinue)) { throw "Install Node.js: https://nodejs.org" }
try { pac auth who | Out-Null } catch { if ($EnvironmentUrl) { pac auth create --environment $EnvironmentUrl } else { pac auth create } }
if ($EnvironmentUrl) { pac env select --environment $EnvironmentUrl }
Remove-Item power.config.json -ErrorAction SilentlyContinue   # env-bound; re-init against YOUR environment
pac code init --displayName "__APP_NAME__"
npm install --no-audit --no-fund
npm run build
pac code push
"""

    def _ensure_solution(self, pac, solution_name, app_name):
        """Create the unmanaged solution in Dataverse if missing (pac has no server-side
        create verb, so we import a minimal empty solution stub)."""
        import tempfile
        import zipfile
        ok, out = _run([pac, "solution", "list"], timeout=180)
        if ok and re.search(rf"^\s*{re.escape(solution_name)}\s", out, re.M):
            return True, "already exists"
        solution_xml = f"""<ImportExportXml version="9.2.0.0" SolutionPackageVersion="9.2" languagecode="1033" generatedBy="CrmLive" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
 <SolutionManifest>
  <UniqueName>{solution_name}</UniqueName>
  <LocalizedNames><LocalizedName description="{app_name}" languagecode="1033" /></LocalizedNames>
  <Descriptions/>
  <Version>1.0.0.0</Version>
  <Managed>0</Managed>
  <Publisher>
   <UniqueName>rappbrainstem</UniqueName>
   <LocalizedNames><LocalizedName description="RAPP Brainstem" languagecode="1033" /></LocalizedNames>
   <Descriptions/>
   <EMailAddress xsi:nil="true"></EMailAddress>
   <SupportingWebsiteUrl xsi:nil="true"></SupportingWebsiteUrl>
   <CustomizationPrefix>rapp</CustomizationPrefix>
   <CustomizationOptionValuePrefix>10000</CustomizationOptionValuePrefix>
   <Addresses/>
  </Publisher>
  <RootComponents/>
  <MissingDependencies/>
 </SolutionManifest>
</ImportExportXml>"""
        customizations_xml = ('<?xml version="1.0" encoding="utf-8"?><ImportExportXml '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><Entities/><Roles/><Workflows/>'
            '<FieldSecurityProfiles/><Templates/><EntityMaps/><EntityRelationships/>'
            '<OrganizationSettings/><optionsets/><CustomControls/><SolutionPluginAssemblies/>'
            '<EntityDataProviders/><Languages><Language>1033</Language></Languages></ImportExportXml>')
        content_types = ('<?xml version="1.0" encoding="utf-8"?><Types '
            'xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="xml" ContentType="text/xml" /></Types>')
        with tempfile.TemporaryDirectory() as td:
            stub = Path(td) / "stub_solution.zip"
            with zipfile.ZipFile(stub, "w", zipfile.ZIP_DEFLATED) as z:
                z.writestr("solution.xml", solution_xml)
                z.writestr("customizations.xml", customizations_xml)
                z.writestr("[Content_Types].xml", content_types)
            ok, out = _run([pac, "solution", "import", "--path", str(stub)], timeout=300)
        if not ok or re.search(r"(?i)\berror\b", out):
            return False, out[-500:]
        return True, "created via empty-solution import"

    def _package(self, slug, app_name, solution_name=None, environment=None):
        import zipfile
        app_dir = APPS_ROOT / slug
        if not (app_dir / "package.json").exists():
            return f"ERROR: no generated app at {app_dir}. Run operation=generate (or full) first."
        log = [f"PACKAGING '{app_name}' from {app_dir}"]
        desktop = Path.home() / "Desktop"
        out_dir = desktop if desktop.is_dir() else app_dir.parent

        # Portable source zip — teammates re-init against their own environment.
        (app_dir / "deploy.sh").write_text(self.DEPLOY_SH.replace("__APP_NAME__", app_name))
        (app_dir / "deploy.sh").chmod(0o755)
        (app_dir / "deploy.ps1").write_text(self.DEPLOY_PS1.replace("__APP_NAME__", app_name))
        (app_dir / "DEPLOY.md").write_text(
            f"# {app_name} — Power Apps code app (portable)\n\n"
            "Prereqs: PAC CLI, Node.js, a Power Platform environment with the **Code Apps** "
            "feature enabled (admin center > environment > Settings > Product > Features), "
            "Power Apps license.\n\n"
            "```bash\n./deploy.sh https://yourorg.crm.dynamics.com/   # macOS/Linux\n"
            "./deploy.ps1 -EnvironmentUrl https://yourorg.crm.dynamics.com/   # Windows\n```\n\n"
            "The script signs in, re-inits `power.config.json` against YOUR environment, "
            "builds, and pushes — then prints your live app URL.\n")
        src_zip = out_dir / f"{slug}-source.zip"
        EXCLUDE_DIRS = {"node_modules", "dist", ".git"}
        EXCLUDE_FILES = {"power.config.json"}  # env-bound; deploy script re-creates it
        with zipfile.ZipFile(src_zip, "w", zipfile.ZIP_DEFLATED) as z:
            for p in sorted(app_dir.rglob("*")):
                rel = p.relative_to(app_dir)
                if p.is_dir() or set(rel.parts) & EXCLUDE_DIRS or rel.name in EXCLUDE_FILES:
                    continue
                z.write(p, Path(slug) / rel)
        n_files = len(zipfile.ZipFile(src_zip).namelist())
        log.append(f"1. Portable source zip: {src_zip} ({n_files} files, "
                   f"{src_zip.stat().st_size // 1024} KB) — unzip, then ./deploy.sh <env-url>")

        # Native solution zip — standard ALM import path.
        if solution_name:
            pac = _pac()
            if not pac:
                log.append("2. Solution export SKIPPED: pac CLI not found.")
                return "\n".join(log)
            if environment:
                _run([pac, "env", "select", "--environment", environment], timeout=90)
            if not (app_dir / "dist").exists():
                ok, out = _run([_npm(), "run", "build"], cwd=app_dir, timeout=BUILD_TIMEOUT)
                if not ok:
                    log.append(f"2. Build FAILED before solution push — {out[-400:]}")
                    return "\n".join(log)
            ok, why = self._ensure_solution(pac, solution_name, app_name)
            log.append(f"2. Solution '{solution_name}': {'OK — ' + why if ok else 'FAILED — ' + why}")
            if not ok:
                return "\n".join(log)
            ok, out = _run([pac, "code", "push", "--solutionName", solution_name],
                           cwd=app_dir, timeout=PUSH_TIMEOUT)
            url = re.search(r"https://\S*powerapps\.com\S*", out)
            if not (ok and url):
                log.append(f"2b. pac code push --solutionName: FAILED — {out[-500:]}")
                return "\n".join(log)
            sol_zip = out_dir / f"{slug}-solution.zip"
            ok, out = _run([pac, "solution", "export", "--name", solution_name,
                            "--path", str(sol_zip), "--overwrite"], timeout=300)
            if not (ok and sol_zip.exists()):
                log.append(f"3. pac solution export FAILED — {out[-500:]}")
                return "\n".join(log)
            with zipfile.ZipFile(sol_zip) as z:
                n_components = z.read("solution.xml").decode("utf-8", "ignore").count("<RootComponent ")
            if n_components == 0:
                # Some environments/CLI versions don't yet register code apps as solution
                # components (no solutioncomponent row) — an empty solution zip would be
                # a lie, so remove it and say exactly what happened.
                sol_zip.unlink()
                log.append("3. Solution zip SKIPPED: this environment did not register the code "
                           "app as a solution component (pac code push --solutionName produced no "
                           "solutioncomponent row), so the export would be an empty shell. "
                           "Share the portable source zip instead — teammates deploy with one "
                           "command into their own environment.")
            else:
                log.append(f"3. Solution zip: {sol_zip} ({max(1, sol_zip.stat().st_size // 1024)} KB, "
                           f"{n_components} component{'s' if n_components != 1 else ''}) — import via "
                           "make.powerapps.com > Solutions > Import, or "
                           "`pac solution import --path <zip>` in the target environment.")
        else:
            log.append("2. No solution_name given — skipped the ALM solution zip "
                       "(pass solution_name to also export an importable solution).")
        return "\n".join(log)
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
