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

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/power_apps_code_app_agent",
    "version": "1.1.0",
    "display_name": "PowerAppsCodeApp",
    "description": "Generates a complete Power Apps code app (vite + React + @microsoft/power-apps) from a structured spec, deploys it via the PAC CLI (pac code init / npm build / pac code push), and packages it for team sharing - a portable source zip with one-command deploy scripts, plus an ALM solution zip where the environment supports code-app solution components.",
    "author": "kody-w",
    "tags": ["power-apps", "code-apps", "pac", "power-platform", "codegen", "deploy", "package", "alm", "vite", "react"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


from __future__ import annotations

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
