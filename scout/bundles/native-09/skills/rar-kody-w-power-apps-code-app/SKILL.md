---
name: "rar-kody-w-power-apps-code-app"
description: "Generates a complete Power Apps code app (vite + React + @microsoft/power-apps) from a structured spec, deploys it via the PAC CLI (pac code init / npm build / pac code push), and packages it for team sharing - a portable source zip with one-command deploy scripts, plus an ALM solution zip where the environment supports code-app solution components."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/power_apps_code_app_agent", "rar_sha256": "b080f45c3105b46c5b049ae7678e0b2844ec67ee52da6ed6a025f6ce1c45f074", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.1", "author": "kody-w", "tags": ["power-apps", "code-apps", "pac", "power-platform", "codegen", "deploy", "package", "alm", "vite", "react"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_apps_code_app_agent.py` and embedded as the fenced Python below (sha256 b080f45c3105b46c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_apps_code_app_agent.py` first:

```bash
python3 power_apps_code_app_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 power_apps_code_app_agent.py   # or on stdin
python3 power_apps_code_app_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/power_apps_code_app_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/power_apps_code_app_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/power_apps_code_app_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
