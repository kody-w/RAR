---
name: "rar-kody-w-power-apps-code-app"
description: "Generates a complete Power Apps code app (vite + React + @microsoft/power-apps) from a structured spec, deploys it via the PAC CLI (pac code init / npm build / pac code push), and packages it for team sharing - a portable source zip with one-command deploy scripts, plus an ALM solution zip where the environment supports code-app solution components."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/power_apps_code_app_agent", "rar_sha256": "fbcd47231e85c44efedbdc661b1e20da4f8cc77f45bbc20d53d7355c25269a10", "source_kind": "rar-agent", "source_commit": "13ba36d938ea0d393c9d863b411b4ed0096648de", "version": "1.1.1", "author": "kody-w", "tags": ["power-apps", "code-apps", "pac", "power-platform", "codegen", "deploy", "package", "alm", "vite", "react"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/power_apps_code_app_agent`. The original RAPP
agent is preserved byte-for-byte in `power_apps_code_app_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

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
