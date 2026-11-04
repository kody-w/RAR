---
name: "rar-borg-borg"
description: "Assimilates knowledge from GitHub repos and web URLs. When the user says 'Borg this <url>', call this tool to inspect the codebase or page. Returns a structured analysis AND an assimilation plan. Every assimilation is automatically saved as a .md report in the docs/ folder and logged to history. IMPORTANT: After receiving the Borg's analysis, you MUST enter planning mode. Present the assimilation plan to the user as follows:\n1. BASE ASSIMILATION \u2014 what core patterns/capabilities should be absorbed into the brainstem as foundational functionality\n2. Present 5 creative, mind-blowing, out-of-the-box extensions the user could build on top of the base\n3. Ask the user which extensions they want before building anything\nThe saved_report field in the response contains the .md file path. Always tell the user where the report was saved. Never skip the planning step. Never just dump raw data. Always analyze, plan, and present options."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@borg/borg_agent", "rar_sha256": "f381aedc272544bba4bac2329153244c037376b964bb2978fd9092306caae8c8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.0", "author": "Howard", "tags": ["core", "analysis", "github", "web", "assimilation"]}
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
