---
name: "rar-borg-borg"
description: "Assimilates knowledge from GitHub repos and web URLs. When the user says 'Borg this <url>', call this tool to inspect the codebase or page. Returns a structured analysis AND an assimilation plan. Every assimilation is automatically saved as a .md report in the docs/ folder and logged to history. IMPORTANT: After receiving the Borg's analysis, you MUST enter planning mode. Present the assimilation plan to the user as follows:\n1. BASE ASSIMILATION \u2014 what core patterns/capabilities should be absorbed into the brainstem as foundational functionality\n2. Present 5 creative, mind-blowing, out-of-the-box extensions the user could build on top of the base\n3. Ask the user which extensions they want before building anything\nThe saved_report field in the response contains the .md file path. Always tell the user where the report was saved. Never skip the planning step. Never just dump raw data. Always analyze, plan, and present options."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@borg/borg_agent", "rar_sha256": "f381aedc272544bba4bac2329153244c037376b964bb2978fd9092306caae8c8", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.0", "author": "Howard", "tags": ["core", "analysis", "github", "web", "assimilation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@borg/borg_agent`. The original RAPP
agent is preserved byte-for-byte in `borg_agent.py` and in the RCI capsule.

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

Borg Agent — Assimilates knowledge from GitHub repos and web URLs.

"We are the Borg. Your technological distinctiveness will be added to our own."

Give it a GitHub URL or web link and it will inspect the codebase, analyze the
tech stack, and return a structured report. HOLO then determines what to use
as base functionality and suggests creative extensions.

Usage: "Borg this https://github.com/owner/repo"

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "assimilate: inspect a URL (default). history: show past assimilations. dashboard: open the Borg assimilation log web page.",
      "enum": [
        "assimilate",
        "history",
        "dashboard"
      ],
      "type": "string"
    },
    "url": {
      "description": "GitHub repository URL or web URL to assimilate.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `borg_agent.py` and embedded as the fenced Python below (sha256 f381aedc272544bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `borg_agent.py` first:

```bash
python3 borg_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 borg_agent.py   # or on stdin
python3 borg_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@borg/borg_agent.py.card -o ~/.brainstem/src/rapp_brainstem/agents/borg_agent.py.card
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@borg/borg_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Borg Agent — Assimilates knowledge from GitHub repos and web URLs.

"We are the Borg. Your technological distinctiveness will be added to our own."

Give it a GitHub URL or web link and it will inspect the codebase, analyze the
tech stack, and return a structured report. HOLO then determines what to use
as base functionality and suggests creative extensions.

Usage: "Borg this https://github.com/owner/repo"
"""

import json
import os
import re
import threading
import time
import urllib.request
import urllib.error
import base64
from datetime import datetime, timezone
from html.parser import HTMLParser
from http.server import HTTPServer, BaseHTTPRequestHandler

try:
    from basic_agent import BasicAgent
except ModuleNotFoundError:
    from agents.basic_agent import BasicAgent

# ── Agent Manifest (machine-readable identity) ──
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@borg/borg_agent",
    "version": "1.1.0",
    "display_name": "Borg",
    "description": "Assimilates knowledge from GitHub repos and web URLs into structured reports.",
    "author": "Howard",
    "tags": ["core", "analysis", "github", "web", "assimilation"],
    "category": "core",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ── Card Shell (Howard-compatible trading card metadata) ──
# This is the card "shell" that wraps the bare agent.
# Format matches CardSmith _CARD_DATABASE exactly.
# Generated by: CardSmith forge action
# Artist: Howard (original HOLO set)
__card__ = {
    "name": "Borg",
    "title": "The Assimilator",
    "mana_cost": "{2}{U}{B}",
    "colors": ["U", "B"],
    "type_line": "Creature — Agent Assimilator",
    "rarity": "mythic",
    "power": 6,
    "toughness": 4,
    "abilities": [
        {
            "keyword": "Assimilate",
            "cost": "{T}",
            "text": "Target GitHub repository or URL becomes part of the collective. Create a structured knowledge report.",
        },
        {
            "keyword": "Adaptive Analysis",
            "cost": "",
            "text": "When Borg assimilates, it detects the tech stack and maps 40+ framework patterns.",
        },
    ],
    "flavor_text": "\"Resistance is futile. Your codebase will be added to our own. Your architectural distinctiveness will be catalogued.\" —Borg Collective Directive 7.1",
    "avatar_svg": '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="bg-borg"><stop offset="0%" stop-color="#1a0a3e"/><stop offset="100%" stop-color="#080818"/></radialGradient><filter id="glow-borg"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="200" height="200" fill="url(#bg-borg)"/><g filter="url(#glow-borg)"><rect x="55" y="55" width="90" height="90" fill="none" stroke="#4a9eff" stroke-width="2" rx="4"/><rect x="70" y="70" width="60" height="60" fill="none" stroke="#8b5cf6" stroke-width="1.5" rx="2"/><line x1="55" y1="100" x2="145" y2="100" stroke="#4a9eff" stroke-width="1" opacity="0.6"/><line x1="100" y1="55" x2="100" y2="145" stroke="#4a9eff" stroke-width="1" opacity="0.6"/><polygon points="100,25 135,45 135,85 100,105 65,85 65,45" fill="none" stroke="#8b5cf6" stroke-width="1" opacity="0.4"/><polygon points="100,95 135,115 135,155 100,175 65,155 65,115" fill="none" stroke="#4a9eff" stroke-width="1" opacity="0.4"/><circle cx="100" cy="100" r="15" fill="#4a9eff" opacity="0.2"/><circle cx="100" cy="100" r="6" fill="#8b5cf6" opacity="0.9"/><circle cx="85" cy="85" r="3" fill="#4a9eff" opacity="0.5"/><circle cx="115" cy="85" r="3" fill="#4a9eff" opacity="0.5"/><circle cx="85" cy="115" r="3" fill="#4a9eff" opacity="0.5"/><circle cx="115" cy="115" r="3" fill="#4a9eff" opacity="0.5"/></g></svg>',
    "set_code": "HOLO",
    "artist": "Howard",
}


# History persistence
_BRAINSTEM_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_HISTORY_PATH = os.path.join(_BRAINSTEM_DIR, ".brainstem_data", "borg_history.json")

# Dashboard server state
_dashboard_server = None
_dashboard_lock = threading.Lock()
_DASHBOARD_PORT = 7074


def _history_path():
    return _HISTORY_PATH


def _load_history():
    path = _history_path()
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def _save_history(history):
    path = _history_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)


def _record_assimilation(url, report):
    """Append an assimilation to the history log."""
    history = _load_history()
    entry = {
        "id": len(history) + 1,
        "url": url,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": report.get("source", "unknown"),
    }
    if report.get("source") == "github":
        repo = report.get("repo", {})
        entry["name"] = repo.get("name", "")
        entry["description"] = repo.get("description", "")
        entry["language"] = repo.get("language", "")
        entry["stars"] = repo.get("stars", 0)
        entry["tech_stack"] = report.get("tech_stack", [])
        entry["total_files"] = report.get("total_files", 0)
    else:
        entry["name"] = report.get("title", url)
        entry["description"] = report.get("description", "")
        entry["tech_hints"] = report.get("tech_hints", [])
    history.append(entry)
    _save_history(history)


def _save_report_md(url, report):
    """Save a Borg assimilation report as a .md file in docs/."""
    docs_dir = os.path.join(_BRAINSTEM_DIR, "docs")
    os.makedirs(docs_dir, exist_ok=True)

    # Generate filename from URL
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', url.split("//")[-1]).strip("-")[:60]
    filename = f"borg-{slug}.md"
    filepath = os.path.join(docs_dir, filename)

    lines = []
    source = report.get("source", "unknown")
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    if source == "github":
        repo = report.get("repo", {})
        lines.append(f"# Borg Report: {repo.get('name', url)}")
        lines.append("")
        lines.append(f"**Assimilated:** {ts}")
        lines.append(f"**URL:** [{url}]({url})")
        lines.append(f"**Description:** {repo.get('description', '')}")
        lines.append(f"**Language:** {repo.get('language', '')} | "
                      f"**Stars:** {repo.get('stars', 0)} | "
                      f"**Forks:** {repo.get('forks', 0)} | "
                      f"**License:** {repo.get('license', '')}")
        lines.append("")
        tech = report.get("tech_stack", [])
        if tech:
            lines.append(f"**Tech Stack:** {', '.join(tech)}")
        langs = report.get("languages", {})
        if langs:
            lines.append(f"**Languages:** {', '.join(f'{k} ({v:,} bytes)' for k, v in langs.items())}")
        lines.append(f"**Total Files:** {report.get('total_files', 0)}")
        lines.append("")
        lines.append("## Structure")
        lines.append("```")
        for item in report.get("structure", [])[:30]:
            lines.append(item)
        lines.append("```")
        lines.append("")
        key_files = report.get("key_files", [])
        if key_files:
            lines.append("## Key Files")
            for f in key_files:
                lines.append(f"- `{f}`")
            lines.append("")
        readme = report.get("readme_preview", "")
        if readme and readme != "(no README found)":
            lines.append("## README Preview")
            lines.append("")
            lines.append(readme[:2000])
            lines.append("")
    else:
        title = report.get("title", url)
        lines.append(f"# Borg Report: {title}")
        lines.append("")
        lines.append(f"**Assimilated:** {ts}")
        lines.append(f"**URL:** [{url}]({url})")
        desc = report.get("description", "")
        if desc:
            lines.append(f"**Description:** {desc}")
        hints = report.get("tech_hints", [])
        if hints:
            lines.append(f"**Tech Hints:** {', '.join(hints)}")
        lines.append("")
        content = report.get("content_preview", "")
        if content:
            lines.append("## Content Preview")
            lines.append("")
            lines.append(content[:2000])
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Assimilation Plan")
    lines.append("")
    lines.append("### Base Assimilation")
    lines.append("*(Analyze the above and identify core patterns to absorb)*")
    lines.append("")
    lines.append("### Creative Extensions")
    lines.append("1. ")
    lines.append("2. ")
    lines.append("3. ")
    lines.append("4. ")
    lines.append("5. ")
    lines.append("")
    lines.append(f"*Borged on {ts}. Fill in the plan above or ask HOLO to analyze.*")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return filepath


# ---------------------------------------------------------------------------
# Simple HTML text extractor (no external deps)
# ---------------------------------------------------------------------------

class _TextExtractor(HTMLParser):
    """Minimal HTML-to-text extractor."""

    _SKIP_TAGS = {"script", "style", "noscript", "svg", "path"}

    def __init__(self):
        super().__init__()
        self._pieces = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in self._SKIP_TAGS:
            self._skip_depth += 1

    def handle_endtag(self, tag):
        if tag in self._SKIP_TAGS and self._skip_depth > 0:
            self._skip_depth -= 1

    def handle_data(self, data):
        if self._skip_depth == 0:
            text = data.strip()
            if text:
                self._pieces.append(text)

    def get_text(self):
        return "\n".join(self._pieces)


# ---------------------------------------------------------------------------
# Tech stack detection patterns
# ---------------------------------------------------------------------------

_TECH_MARKERS = {
    "package.json": "Node.js / JavaScript",
    "tsconfig.json": "TypeScript",
    "requirements.txt": "Python",
    "setup.py": "Python",
    "pyproject.toml": "Python",
    "Pipfile": "Python (Pipenv)",
    "Cargo.toml": "Rust",
    "go.mod": "Go",
    "pom.xml": "Java (Maven)",
    "build.gradle": "Java/Kotlin (Gradle)",
    "Gemfile": "Ruby",
    "composer.json": "PHP",
    "Dockerfile": "Docker",
    "docker-compose.yml": "Docker Compose",
    "docker-compose.yaml": "Docker Compose",
    ".github/workflows": "GitHub Actions CI/CD",
    "Makefile": "Make",
    "CMakeLists.txt": "C/C++ (CMake)",
    "terraform": "Terraform",
    "serverless.yml": "Serverless Framework",
    "azuredeploy.json": "Azure ARM Template",
    "bicep": "Azure Bicep",
    "helm": "Kubernetes Helm",
    "k8s": "Kubernetes",
    ".env.example": "Environment config",
    "next.config.js": "Next.js",
    "nuxt.config.js": "Nuxt.js",
    "vite.config": "Vite",
    "webpack.config": "Webpack",
    "tailwind.config": "Tailwind CSS",
    "flask": "Flask",
    "fastapi": "FastAPI",
    "django": "Django",
    "express": "Express.js",
}


def _detect_tech_stack(file_list):
    """Detect technologies from a list of file paths."""
    found = set()
    for filepath in file_list:
        name = filepath.lower().rstrip("/")
        basename = os.path.basename(name)
        for marker, tech in _TECH_MARKERS.items():
            if marker.lower() in name or marker.lower() == basename:
                found.add(tech)
    return sorted(found)


# ---------------------------------------------------------------------------
# GitHub URL parsing
# ---------------------------------------------------------------------------

_GITHUB_RE = re.compile(
    r"github\.com/([^/]+)/([^/]+?)(?:\.git)?(?:/(?:tree|blob)/([^/]+)(?:/(.+))?)?/?$"
)


def _parse_github_url(url):
    """Extract (owner, repo, branch, path) from a GitHub URL."""
    m = _GITHUB_RE.search(url)
    if not m:
        return None
    owner, repo, branch, path = m.group(1), m.group(2), m.group(3), m.group(4)
    return owner, repo, branch or "main", path or ""


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def _fetch_json(url, token=None):
    """Fetch a URL and return parsed JSON, or None on failure."""
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github.v3+json"})
    if token:
        req.add_header("Authorization", f"token {token}")
    req.add_header("User-Agent", "HOLO-Borg-Agent/1.0")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, json.JSONDecodeError, OSError):
        return None


def _fetch_text(url):
    """Fetch a URL and return text content, or None on failure."""
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "HOLO-Borg-Agent/1.0")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, OSError):
        return None


# ---------------------------------------------------------------------------
# Dashboard — serves Borg assimilation history as a web page
# ---------------------------------------------------------------------------

_DASHBOARD_HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>KIM — Borg Assimilation Log</title>
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:#0a0a2e;color:#c0c0c0;font-family:'Segoe UI','Courier New',monospace;padding:30px 40px}
  h1{color:#00ff88;font-size:2.2em;margin-bottom:5px;letter-spacing:-0.5px}
  .subtitle{color:#666;margin-bottom:30px;font-size:0.95em}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(380px,1fr));gap:20px}
  .card{background:#111;border:1px solid #333;border-radius:12px;padding:20px;transition:all 0.3s;cursor:pointer;text-decoration:none;display:block;color:inherit}
  .card:hover{border-color:#00ff88;transform:translateY(-2px);box-shadow:0 4px 20px rgba(0,255,136,0.1)}
  .card-header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px}
  .card-name{color:#00ccff;font-size:1.1em;font-weight:bold;word-break:break-word}
  .card-badge{padding:2px 8px;border-radius:4px;font-size:0.7em;flex-shrink:0;margin-left:10px;font-weight:bold;text-transform:uppercase}
  .badge-github{background:#00ff88;color:#0a0a2e}
  .badge-web{background:#ffcc00;color:#0a0a2e}
  .badge-local{background:#ff6b9d;color:#0a0a2e}
  .badge-kit{background:#bf5af2;color:#fff}
  .card-desc{color:#999;font-size:0.88em;margin:8px 0;line-height:1.5}
  .card-url{color:#555;font-size:0.78em;word-break:break-all;margin-top:4px}
  .meta{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}
  .tag{background:#1a1a3e;padding:3px 8px;border-radius:4px;font-size:0.72em}
  .tag-tech{color:#00ff88}
  .tag-lang{color:#ffcc00}
  .tag-stars{color:#ff6b6b}
  .tag-size{color:#888}
  .stat{color:#555;font-size:0.78em;margin-top:8px}
  .empty{text-align:center;color:#555;padding:60px;font-size:1.2em}
  .count{color:#00ff88;font-size:0.9em;margin-bottom:20px}
  .view-report{display:inline-block;margin-top:12px;color:#00ff88;font-size:0.82em;border:1px solid #00ff8844;padding:4px 12px;border-radius:6px;transition:all 0.2s}
  .card:hover .view-report{background:#00ff88;color:#0a0a2e}
</style>
</head>
<body>
<h1>&#x1F6F8; Borg Assimilation Log</h1>
<p class="subtitle">We are KIM. Your technological distinctiveness has been added to our own.</p>
<div id="content"><p class="empty">Scanning collective...</p></div>
<script>
// Resolve base path for both direct access and proxy access
const base = window.location.pathname.replace(/\/?$/, '/');
fetch(base + 'api')
  .then(r=>r.json())
  .then(data=>{
    const c=document.getElementById('content');
    const reports=data.reports||[];
    if(!reports.length){c.innerHTML='<p class="empty">No assimilations yet. Tell KIM to Borg something.</p>';return}
    let html='<p class="count">'+reports.length+' assimilation'+(reports.length>1?'s':'')+' in the collective</p><div class="grid">';
    reports.forEach(e=>{
      const badge=e.badge||'local';
      const badgeLabel=e.badge_label||badge;
      const tech=(e.tags||[]).map(t=>'<span class="tag tag-tech">'+t+'</span>').join('');
      const lang=e.language?'<span class="tag tag-lang">'+e.language+'</span>':'';
      const stars=e.stars?'<span class="tag tag-stars">\\u2605 '+e.stars+'</span>':'';
      const size=e.size?'<span class="tag tag-size">'+e.size+'</span>':'';
      const reportUrl=e.report_file?base+'report/'+encodeURIComponent(e.report_file):'#';
      html+='<a class="card" href="'+reportUrl+'">'
        +'<div class="card-header"><span class="card-name">'+e.title+'</span>'
        +'<span class="card-badge badge-'+badge+'">'+badgeLabel+'</span></div>'
        +(e.description?'<p class="card-desc">'+e.description+'</p>':'')
        +(e.url?'<p class="card-url">'+e.url+'</p>':'')
        +'<div class="meta">'+lang+stars+tech+size+'</div>'
        +(e.date?'<p class="stat">Assimilated: '+e.date+'</p>':'')
        +'<span class="view-report">View Full Report \\u2192</span>'
        +'</a>';
    });
    html+='</div>';
    c.innerHTML=html;
  })
  .catch(err=>{document.getElementById('content').innerHTML='<p class="empty">Could not load assimilation data: '+err+'</p>'});
</script>
</body>
</html>"""


def _scan_borg_reports():
    """Scan docs/ for all borg-*.md files and extract metadata from each."""
    docs_dir = os.path.join(_BRAINSTEM_DIR, "docs")
    if not os.path.exists(docs_dir):
        return []

    reports = []
    for fname in sorted(os.listdir(docs_dir), reverse=True):
        if not fname.startswith("borg-") or not fname.endswith(".md"):
            continue
        fpath = os.path.join(docs_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read(4000)  # first 4KB for metadata extraction
        except Exception:
            continue

        lines = content.split("\n")
        title = fname.replace("borg-", "").replace(".md", "").replace("-", " ").title()
        description = ""
        url = ""
        date = ""
        language = ""
        stars = 0
        tags = []
        badge = "local"
        badge_label = "Report"

        for line in lines[:30]:
            line_s = line.strip()
            if line_s.startswith("# "):
                raw_title = line_s[2:].strip()
                title = raw_title.replace("Borg Report: ", "").replace("KIM × Kit9 ", "")
            elif line_s.startswith("**Assimilated:**"):
                date = line_s.split("**Assimilated:**")[-1].strip()
            elif line_s.startswith("**Date:**"):
                date = line_s.split("**Date:**")[-1].strip()
            elif line_s.startswith("**URL:**"):
                url_part = line_s.split("**URL:**")[-1].strip()
                # Extract URL from markdown link
                if "(" in url_part and ")" in url_part:
                    url = url_part.split("(")[1].split(")")[0]
                else:
                    url = url_part
            elif line_s.startswith("**Description:**"):
                description = line_s.split("**Description:**")[-1].strip()
            elif line_s.startswith("**Language:**"):
                lang_part = line_s.split("**Language:**")[-1].strip()
                language = lang_part.split("|")[0].strip()
            elif line_s.startswith("**Stars:**"):
                try:
                    stars = int(line_s.split("**Stars:**")[-1].strip().split()[0].replace(",", ""))
                except (ValueError, IndexError):
                    pass
            elif line_s.startswith("**Tech Stack:**") or line_s.startswith("**Tech Hints:**"):
                tag_part = line_s.split(":**")[-1].strip()
                tags = [t.strip() for t in tag_part.split(",") if t.strip()]
            elif line_s.startswith("**Operation:**"):
                description = line_s.split("**Operation:**")[-1].strip()

        # Classify badge type
        if "github.com" in url:
            badge = "github"
            badge_label = "GitHub"
        elif url and ("http" in url):
            badge = "web"
            badge_label = "Web"
        elif "kit9" in fname or "assimilation" in fname:
            badge = "kit"
            badge_label = "Kit"
        else:
            badge = "local"
            badge_label = "Report"

        stat = os.stat(fpath)
        size_kb = stat.st_size / 1024

        reports.append({
            "title": title,
            "description": description[:200],
            "url": url,
            "date": date or datetime.fromtimestamp(stat.st_mtime, timezone.utc).strftime("%Y-%m-%d"),
            "language": language,
            "stars": stars,
            "tags": tags[:6],
            "badge": badge,
            "badge_label": badge_label,
            "report_file": fname,
            "size": f"{size_kb:.0f} KB"
        })

    return reports


def _render_md_as_html(md_content, title="Borg Report"):
    """Convert markdown to simple HTML for display."""
    import html as html_mod
    content = html_mod.escape(md_content)
    # Basic markdown rendering
    lines = content.split("\n")
    html_lines = []
    in_code = False
    in_table = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_code:
                html_lines.append("</pre>")
                in_code = False
            else:
                html_lines.append("<pre>")
                in_code = True
            continue
        if in_code:
            html_lines.append(line)
            continue
        if stripped.startswith("|") and not in_table:
            in_table = True
            html_lines.append("<table>")
        if in_table and not stripped.startswith("|"):
            in_table = False
            html_lines.append("</table>")
        if in_table:
            if all(c in "-| " for c in stripped):
                continue  # skip separator rows
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            html_lines.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
            continue
        # Headings
        if stripped.startswith("### "):
            html_lines.append(f"<h3>{stripped[4:]}</h3>")
        elif stripped.startswith("## "):
            html_lines.append(f"<h2>{stripped[3:]}</h2>")
        elif stripped.startswith("# "):
            html_lines.append(f"<h1>{stripped[2:]}</h1>")
        elif stripped.startswith("- "):
            html_lines.append(f"<li>{stripped[2:]}</li>")
        elif stripped.startswith("---"):
            html_lines.append("<hr>")
        elif stripped == "":
            html_lines.append("<br>")
        else:
            # Bold
            import re as _re
            rendered = _re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', stripped)
            rendered = _re.sub(r'\*(.+?)\*', r'<em>\1</em>', rendered)
            rendered = _re.sub(r'`(.+?)`', r'<code>\1</code>', rendered)
            rendered = _re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" target="_blank">\1</a>', rendered)
            html_lines.append(f"<p>{rendered}</p>")
    if in_table:
        html_lines.append("</table>")

    body = "\n".join(html_lines)
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{title} — KIM Borg</title>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{background:#0a0a2e;color:#c0c0c0;font-family:'Segoe UI',sans-serif;padding:30px 60px;max-width:1000px;margin:0 auto;line-height:1.7}}
  a{{color:#00ccff}}
  a:hover{{color:#00ff88}}
  h1{{color:#00ff88;font-size:1.8em;margin:20px 0 10px;border-bottom:1px solid #333;padding-bottom:8px}}
  h2{{color:#00ccff;font-size:1.3em;margin:25px 0 8px;border-bottom:1px solid #222;padding-bottom:5px}}
  h3{{color:#bf5af2;font-size:1.1em;margin:18px 0 6px}}
  p{{margin:4px 0}}
  strong{{color:#e0e0e0}}
  code{{background:#1a1a3e;color:#00ff88;padding:1px 6px;border-radius:3px;font-size:0.9em}}
  pre{{background:#111;border:1px solid #333;border-radius:8px;padding:15px;overflow-x:auto;font-size:0.85em;color:#00ff88;margin:10px 0}}
  hr{{border:none;border-top:1px solid #333;margin:20px 0}}
  li{{margin:3px 0 3px 20px;list-style:disc}}
  table{{border-collapse:collapse;width:100%;margin:10px 0}}
  td{{border:1px solid #333;padding:6px 12px;font-size:0.88em}}
  tr:nth-child(odd){{background:#111}}
  tr:first-child td{{background:#1a1a3e;color:#00ccff;font-weight:bold}}
  .back{{display:inline-block;margin-bottom:20px;color:#00ff88;text-decoration:none;font-size:0.9em}}
  .back:hover{{text-decoration:underline}}
</style>
</head>
<body>
<a class="back" href="javascript:history.back()">&#x2190; Back to Assimilation Log</a>
{body}
</body>
</html>"""


class _DashboardHandler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        if self.path == "/api" or self.path == "/api/":
            reports = _scan_borg_reports()
            body = json.dumps({"reports": reports}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
        elif self.path.startswith("/report/"):
            fname = urllib.request.unquote(self.path[8:])
            # Sanitize filename
            fname = os.path.basename(fname)
            fpath = os.path.join(_BRAINSTEM_DIR, "docs", fname)
            if os.path.exists(fpath) and fname.startswith("borg-") and fname.endswith(".md"):
                with open(fpath, "r", encoding="utf-8") as f:
                    md_content = f.read()
                body = _render_md_as_html(md_content, fname.replace(".md", "")).encode()
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
            else:
                body = b"Report not found."
                self.send_response(404)
                self.send_header("Content-Type", "text/plain")
        else:
            body = _DASHBOARD_HTML.encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def _start_dashboard():
    """Start the Borg dashboard server."""
    global _dashboard_server
    with _dashboard_lock:
        if _dashboard_server is not None:
            return _DASHBOARD_PORT
        import socket
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect(("127.0.0.1", _DASHBOARD_PORT))
                return _DASHBOARD_PORT
        except (OSError, ConnectionRefusedError):
            pass
        try:
            server = HTTPServer(("127.0.0.1", _DASHBOARD_PORT), _DashboardHandler)
            t = threading.Thread(target=server.serve_forever, daemon=True)
            t.start()
            _dashboard_server = server
            return _DASHBOARD_PORT
        except OSError:
            return None


# ---------------------------------------------------------------------------
# Borg Agent
# ---------------------------------------------------------------------------

class BorgAgent(BasicAgent):
    def __init__(self):
        self.name = "Borg"
        self.metadata = {
            "name": self.name,
            "description": (
                "Assimilates knowledge from GitHub repos and web URLs. "
                "When the user says 'Borg this <url>', call this tool to inspect "
                "the codebase or page. Returns a structured analysis AND an "
                "assimilation plan. Every assimilation is automatically saved as a "
                ".md report in the docs/ folder and logged to history. "
                "IMPORTANT: After receiving the Borg's analysis, "
                "you MUST enter planning mode. Present the assimilation plan to the "
                "user as follows:\n"
                "1. BASE ASSIMILATION — what core patterns/capabilities should be "
                "absorbed into the brainstem as foundational functionality\n"
                "2. Present 5 creative, mind-blowing, out-of-the-box extensions "
                "the user could build on top of the base\n"
                "3. Ask the user which extensions they want before building anything\n"
                "The saved_report field in the response contains the .md file path. "
                "Always tell the user where the report was saved. "
                "Never skip the planning step. Never just dump raw data. Always "
                "analyze, plan, and present options."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "GitHub repository URL or web URL to assimilate.",
                    },
                    "action": {
                        "type": "string",
                        "enum": ["assimilate", "history", "dashboard"],
                        "description": (
                            "assimilate: inspect a URL (default). "
                            "history: show past assimilations. "
                            "dashboard: open the Borg assimilation log web page."
                        ),
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # ------------------------------------------------------------------
    # GitHub assimilation
    # ------------------------------------------------------------------

    def _assimilate_github(self, owner, repo, branch, path):
        """Assimilate a GitHub repository."""
        token = os.environ.get("GITHUB_TOKEN")

        # 1. Repo metadata
        repo_info = _fetch_json(f"https://api.github.com/repos/{owner}/{repo}", token)
        if repo_info is None:
            return json.dumps({
                "error": f"Could not access github.com/{owner}/{repo}. Repository may be private or not exist.",
                "suggestion": "Set GITHUB_TOKEN env var for private repo access.",
            })

        # Use the repo's actual default branch if none was specified in the URL
        default_branch = repo_info.get("default_branch", "main")
        if branch == "main":
            branch = default_branch

        # 2. README
        readme_data = _fetch_json(f"https://api.github.com/repos/{owner}/{repo}/readme", token)
        readme_text = ""
        if readme_data and "content" in readme_data:
            try:
                raw = base64.b64decode(readme_data["content"]).decode("utf-8", errors="replace")
                readme_text = raw[:3000]
            except Exception:
                readme_text = "(could not decode README)"

        # 3. File tree
        tree_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
        tree_data = _fetch_json(tree_url, token)
        file_list = []
        if tree_data and "tree" in tree_data:
            file_list = [
                item["path"] for item in tree_data["tree"]
                if item.get("type") in ("blob", "tree")
            ]

        # 4. If a specific path was requested, fetch that file/dir
        target_content = ""
        if path:
            raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
            target_content = _fetch_text(raw_url) or ""
            if len(target_content) > 5000:
                target_content = target_content[:5000] + "\n... (truncated)"

        # 5. Tech stack detection
        tech_stack = _detect_tech_stack(file_list)

        # 6. Key files (package.json, requirements.txt, etc.)
        key_files = [f for f in file_list if os.path.basename(f) in _TECH_MARKERS]

        # 7. Language stats
        languages_data = _fetch_json(f"https://api.github.com/repos/{owner}/{repo}/languages", token)
        languages = languages_data if isinstance(languages_data, dict) else {}

        # 8. Summarize file structure (top-level + one level deep)
        top_level = sorted(set(
            f.split("/")[0] + ("/" if "/" in f else "") for f in file_list
        ))[:50]

        report = {
            "source": "github",
            "url": f"https://github.com/{owner}/{repo}",
            "repo": {
                "name": repo_info.get("full_name", f"{owner}/{repo}"),
                "description": repo_info.get("description", ""),
                "stars": repo_info.get("stargazers_count", 0),
                "forks": repo_info.get("forks_count", 0),
                "language": repo_info.get("language", ""),
                "topics": repo_info.get("topics", []),
                "license": (repo_info.get("license") or {}).get("spdx_id", ""),
                "updated": repo_info.get("updated_at", ""),
            },
            "tech_stack": tech_stack,
            "languages": languages,
            "file_count": len([f for f in file_list if "/" not in f or f.count("/") <= 2]),
            "total_files": len(file_list),
            "structure": top_level,
            "key_files": key_files[:20],
            "readme_preview": readme_text[:2000] if readme_text else "(no README found)",
        }

        if target_content:
            report["target_file"] = {"path": path, "content": target_content}

        # Assimilation plan
        report["assimilation_plan"] = {
            "instructions": (
                "ENTER PLANNING MODE. Present this to the user as a structured plan: "
                "1) BASE ASSIMILATION: Identify the core patterns, architectures, and "
                "capabilities from this repo that should be absorbed as foundational "
                "functionality into the brainstem. 2) CREATIVE EXTENSIONS: Propose 5 "
                "mind-blowing, out-of-the-box things the user could build by combining "
                "this repo's ideas with the existing brainstem agents (HoloNaming, Borg, "
                "Anvil, Memory). 3) Ask the user which ones they want before building. "
                "Be specific — reference actual files, patterns, and code from the analysis."
            ),
            "source_summary": {
                "name": repo_info.get("full_name", f"{owner}/{repo}"),
                "description": repo_info.get("description", ""),
                "primary_language": repo_info.get("language", ""),
                "tech_stack": tech_stack,
                "total_files": len(file_list),
            },
        }

        return json.dumps(report, indent=2)

    # ------------------------------------------------------------------
    # Web page assimilation
    # ------------------------------------------------------------------

    def _assimilate_web(self, url):
        """Assimilate a web page."""
        html = _fetch_text(url)
        if html is None:
            return json.dumps({"error": f"Could not fetch {url}."})

        # Extract text
        extractor = _TextExtractor()
        try:
            extractor.feed(html)
        except Exception:
            pass
        text = extractor.get_text()

        # Extract title
        title_match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else ""

        # Extract meta description
        desc_match = re.search(
            r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',
            html, re.IGNORECASE
        )
        description = desc_match.group(1).strip() if desc_match else ""

        # Find linked resources (scripts, stylesheets)
        scripts = re.findall(r'src=["\']([^"\']+\.js)["\']', html)
        styles = re.findall(r'href=["\']([^"\']+\.css)["\']', html)

        # Detect tech from page content
        tech_hints = set()
        lower_html = html.lower()
        if "react" in lower_html:
            tech_hints.add("React")
        if "vue" in lower_html:
            tech_hints.add("Vue.js")
        if "angular" in lower_html:
            tech_hints.add("Angular")
        if "next" in lower_html and "next.js" in lower_html:
            tech_hints.add("Next.js")
        if "tailwind" in lower_html:
            tech_hints.add("Tailwind CSS")
        if "bootstrap" in lower_html:
            tech_hints.add("Bootstrap")
        if "swagger" in lower_html or "openapi" in lower_html:
            tech_hints.add("OpenAPI/Swagger")

        report = {
            "source": "web",
            "url": url,
            "title": title,
            "description": description,
            "tech_hints": sorted(tech_hints),
            "scripts": scripts[:10],
            "stylesheets": styles[:5],
            "content_preview": text[:3000] if text else "(no text content extracted)",
            "content_length": len(text),
        }

        # Assimilation plan
        report["assimilation_plan"] = {
            "instructions": (
                "ENTER PLANNING MODE. Present this to the user as a structured plan: "
                "1) BASE ASSIMILATION: Identify the core patterns, architectures, and "
                "capabilities from this page that should be absorbed as foundational "
                "functionality into the brainstem. 2) CREATIVE EXTENSIONS: Propose 5 "
                "mind-blowing, out-of-the-box things the user could build by combining "
                "this page's ideas with the existing brainstem agents (HoloNaming, Borg, "
                "Anvil, Memory). 3) Ask the user which ones they want before building. "
                "Be specific — reference actual content and features from the analysis."
            ),
            "source_summary": {
                "title": title,
                "description": description,
                "tech_hints": sorted(tech_hints),
            },
        }

        return json.dumps(report, indent=2)

    # ------------------------------------------------------------------
    # Main entry point
    # ------------------------------------------------------------------

    def perform(self, **kwargs):
        action = kwargs.get("action", "assimilate")
        url = kwargs.get("url", "").strip()

        # History action
        if action == "history":
            history = _load_history()
            if not history:
                return json.dumps({"entries": [], "message": "No assimilations yet."})
            return json.dumps({"entries": history, "total": len(history)})

        # Dashboard action
        if action == "dashboard":
            port = _start_dashboard()
            if port:
                return json.dumps({
                    "dashboard": f"http://127.0.0.1:{port}",
                    "message": f"Borg dashboard running at http://127.0.0.1:{port}",
                    "total_assimilations": len(_load_history()),
                })
            return json.dumps({"error": "Could not start dashboard server."})

        # Assimilate (default)
        if not url:
            return json.dumps({
                "error": "Resistance is futile... but I need a URL to assimilate.",
                "usage": "Borg this https://github.com/owner/repo",
            })

        # Normalize URL
        if not url.startswith("http"):
            url = "https://" + url

        # GitHub or web?
        parsed = _parse_github_url(url)
        if parsed:
            owner, repo, branch, path = parsed
            result_str = self._assimilate_github(owner, repo, branch, path)
        else:
            result_str = self._assimilate_web(url)

        # Record to history
        try:
            report = json.loads(result_str)
            if "error" not in report:
                _record_assimilation(url, report)
                # Auto-save .md report to docs/
                md_path = _save_report_md(url, report)
                report["saved_report"] = md_path
                result_str = json.dumps(report, indent=2)
        except (json.JSONDecodeError, TypeError):
            pass

        return result_str
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
