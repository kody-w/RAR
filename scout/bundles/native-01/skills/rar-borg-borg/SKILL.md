---
name: "rar-borg-borg"
description: "Assimilates knowledge from GitHub repos and web URLs. When the user says 'Borg this <url>', call this tool to inspect the codebase or page. Returns a structured analysis AND an assimilation plan. Every assimilation is automatically saved as a .md report in the docs/ folder and logged to history. IMPORTANT: After receiving the Borg's analysis, you MUST enter planning mode. Present the assimilation plan to the user as follows:\n1. BASE ASSIMILATION \u2014 what core patterns/capabilities should be absorbed into the brainstem as foundational functionality\n2. Present 5 creative, mind-blowing, out-of-the-box extensions the user could build on top of the base\n3. Ask the user which extensions they want before building anything\nThe saved_report field in the response contains the .md file path. Always tell the user where the report was saved. Never skip the planning step. Never just dump raw data. Always analyze, plan, and present options."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@borg/borg_agent", "rar_sha256": "7710557fc30ce2098c1b4d136004bc7e979ed8441b91dba95c38de830905166f", "source_kind": "rar-agent", "source_commit": "93b35d7eba4c70b67b78d4b56bac8f7ca977dc8b", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "borg_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@borg/borg:aa5b44b17bfc6db2b2c91664a79678d8cb545f9b2b90448489bfa672b26ec490", "kind": "skill"}, "version": "1.1.0", "author": "Howard", "tags": ["core", "analysis", "github", "web", "assimilation"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@borg/borg_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `borg_agent.py` is
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
