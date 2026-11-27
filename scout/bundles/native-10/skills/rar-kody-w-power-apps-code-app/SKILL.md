---
name: "rar-kody-w-power-apps-code-app"
description: "Generates a complete Power Apps code app (vite + React + @microsoft/power-apps) from a structured spec, deploys it via the PAC CLI (pac code init / npm build / pac code push), and packages it for team sharing - a portable source zip with one-command deploy scripts, plus an ALM solution zip where the environment supports code-app solution components."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/power_apps_code_app_agent", "rar_sha256": "b080f45c3105b46c5b049ae7678e0b2844ec67ee52da6ed6a025f6ce1c45f074", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.1", "author": "kody-w", "tags": ["power-apps", "code-apps", "pac", "power-platform", "codegen", "deploy", "package", "alm", "vite", "react"]}
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
