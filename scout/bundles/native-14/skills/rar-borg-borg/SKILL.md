---
name: "rar-borg-borg"
description: "Assimilates knowledge from GitHub repos and web URLs. When the user says 'Borg this <url>', call this tool to inspect the codebase or page. Returns a structured analysis AND an assimilation plan. Every assimilation is automatically saved as a .md report in the docs/ folder and logged to history. IMPORTANT: After receiving the Borg's analysis, you MUST enter planning mode. Present the assimilation plan to the user as follows:\n1. BASE ASSIMILATION \u2014 what core patterns/capabilities should be absorbed into the brainstem as foundational functionality\n2. Present 5 creative, mind-blowing, out-of-the-box extensions the user could build on top of the base\n3. Ask the user which extensions they want before building anything\nThe saved_report field in the response contains the .md file path. Always tell the user where the report was saved. Never skip the planning step. Never just dump raw data. Always analyze, plan, and present options."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@borg/borg_agent", "rar_sha256": "7710557fc30ce2098c1b4d136004bc7e979ed8441b91dba95c38de830905166f", "source_kind": "rar-agent", "source_commit": "93b35d7eba4c70b67b78d4b56bac8f7ca977dc8b", "version": "1.1.0", "author": "Howard", "tags": ["core", "analysis", "github", "web", "assimilation"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `borg_agent.py` and embedded as the fenced Python below (sha256 7710557fc30ce209…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `borg_agent.py` first:

```bash
python3 borg_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 borg_agent.py   # or on stdin
python3 borg_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
