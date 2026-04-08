"""
VaultMind — "Your second brain has a brain." — Made by HOLO

One agent to manage it all: multi-person 30-60-90 day plans, Now/Next/Later
priorities, OKRs, Kanban boards, team dashboards, Karpathy-style knowledge 
bases, training quests, and scheduled automation — all through your Obsidian vault.
28 actions. One file. Zero dependencies beyond brainstem.

## 10 Usage Examples

1. "Add Jane Smith as a Senior Engineer starting today"
   → ObsidianPilot action=add_person, name="Jane Smith", role="Senior Engineer", start_date="2025-04-15"

2. "Show me everyone's status"
   → ObsidianPilot action=roster

3. "Assign Jane a NOW priority: complete architecture review"
   → ObsidianPilot action=assign, name="Jane Smith", priority="now", task="Complete architecture review by Friday"

4. "Generate the team dashboard"
   → ObsidianPilot action=report

5. "Generate my morning brief"
   → ObsidianPilot action=brief

6. "Ingest this article into my wiki"
   → ObsidianPilot action=ingest, url="https://example.com/article"

7. "Run a health check on the wiki"
   → ObsidianPilot action=health

8. "Watch this URL for changes"
   → ObsidianPilot action=watch, url="https://blog.example.com/feed"

9. "Show me the scheduled jobs"
   → ObsidianPilot action=job_status

10. "Retire Bob's plan — he completed onboarding"
    → ObsidianPilot action=retire, name="Bob Chen"
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@borg/vaultmind_agent",
    "version": "1.0.0",
    "display_name": "VaultMind",
    "description": (
        "Your second brain has a brain. 28-action Obsidian vault manager: "
        "multi-person 30-60-90 plans, OKRs, Kanban boards, Now/Next/Later priorities, "
        "Karpathy-style LLM knowledge bases, training quests, morning briefs, "
        "wiki health checks, auto-bootstrap with plugins. One file, zero deps."
    ),
    "author": "Howard Hoy",
    "tags": ["obsidian", "30-60-90", "onboarding", "wiki", "knowledge-base",
             "vault", "automation", "scheduling", "monitoring"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": ["OBSIDIAN_VAULT"],
    "dependencies": ["@rapp/basic_agent"],
}

import hashlib
import html
import json
import os
import re
import urllib.error
import urllib.request
import webbrowser
from datetime import date, datetime, timezone
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    from basic_agent import BasicAgent

_BRAINSTEM_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DELIVERABLES_DIR = os.path.join(_BRAINSTEM_DIR, "deliverables")
_DEFAULT_VAULT = os.path.join(os.path.expanduser("~"), "ObsidianVault")

_IGNORED_DIRS = {".obsidian", ".trash", "_archived", ".git", "__pycache__",
                 "node_modules", ".obsidian-sentinel"}

_WIN_RESERVED = (
    {"con", "prn", "aux", "nul"}
    | {f"com{i}" for i in range(1, 10)}
    | {f"lpt{i}" for i in range(1, 10)}
)

_USER_AGENT = "ObsidianPilot/2.0 (RAPP Brainstem)"

_ALL_JOBS = [
    "morning_brief", "content_watch", "auto_review",
    "wiki_health", "phase_alert", "digest",
]

_JOB_DESCRIPTIONS = {
    "morning_brief": "Generate morning digest — people status, overdue items, milestones",
    "content_watch": "Check watched URLs for new content",
    "auto_review": "Draft weekly reviews from recent activity per person",
    "wiki_health": "Scan wiki for stale, orphaned, or broken articles",
    "phase_alert": "Alert on 30/60/90 day boundary crossings this week",
    "digest": "Summarise all vault changes since last digest",
}


# ─── Helpers ──────────────────────────────────────────────────────────────────

def _slugify(name):
    """Convert a display name to a filesystem-safe slug."""
    slug = name.lower().strip()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    if slug in _WIN_RESERVED:
        slug = slug + "-person"
    return slug or "unnamed"


def _safe_write(path, content):
    """Atomic write: write to temp then replace."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(content)
    os.replace(tmp, path)


def _safe_read(path):
    """Read a file with graceful error handling."""
    if not os.path.isfile(path):
        return ""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def _parse_frontmatter(text):
    """Parse YAML-style frontmatter from a markdown file."""
    data = {}
    if not text.startswith("---"):
        return data, text
    end = text.find("---", 3)
    if end == -1:
        return data, text
    fm_block = text[3:end].strip()
    body = text[end + 3:].strip()
    for line in fm_block.split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            data[key.strip()] = val.strip()
    return data, body


def _build_frontmatter(data):
    """Build a YAML frontmatter block."""
    lines = ["---"]
    for k, v in data.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def _today():
    return date.today()


def _now_iso():
    return datetime.now(timezone.utc).isoformat()


def _parse_date(s):
    """Parse a YYYY-MM-DD date string."""
    try:
        return datetime.strptime(s.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None


def _day_count(start_date):
    """Number of days since start_date."""
    if not start_date:
        return 0
    d = _parse_date(start_date) if isinstance(start_date, str) else start_date
    if not d:
        return 0
    return max(0, (_today() - d).days)


def _phase_label(days):
    """Determine plan phase from day count."""
    if days <= 30:
        return "Phase 1 (30-day)"
    elif days <= 60:
        return "Phase 2 (60-day)"
    elif days <= 90:
        return "Phase 3 (90-day)"
    return "Complete"


def _phase_file(days):
    """Return the active plan filename for the current phase."""
    if days <= 30:
        return "30-day.md"
    elif days <= 60:
        return "60-day.md"
    elif days <= 90:
        return "90-day.md"
    return "90-day.md"


def _count_tasks(text):
    """Count completed and total checkbox tasks in markdown text."""
    total = len(re.findall(r"- \[[ x]\]", text))
    done = len(re.findall(r"- \[x\]", text, re.IGNORECASE))
    return done, total


def _extract_section_items(text, section_name):
    """Extract list items from a markdown section (e.g., NOW, NEXT, LATER)."""
    pattern = rf"##\s*{re.escape(section_name)}\s*\n(.*?)(?=\n##|\Z)"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    if not match:
        return []
    block = match.group(1)
    items = []
    for line in block.split("\n"):
        line = line.strip()
        if re.match(r"^- \[[ x]\] ", line, re.IGNORECASE):
            items.append(line[6:])
        elif line.startswith("- "):
            items.append(line[2:])
    return items


def _collect_md_files(directory, ignored=None):
    """Collect all .md files in a directory tree, ignoring specified dirs."""
    ignored = ignored or _IGNORED_DIRS
    files = []
    if not os.path.isdir(directory):
        return files
    for root, dirs, filenames in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ignored]
        for fn in filenames:
            if fn.endswith(".md"):
                files.append(os.path.join(root, fn))
    return files


def _status_indicator(person_dir):
    """Return 🟢🟡🔴 based on overdue items."""
    overdue = 0
    for fname in ["30-day.md", "60-day.md", "90-day.md", "priorities.md"]:
        text = _safe_read(os.path.join(person_dir, fname))
        for m in re.finditer(r"- \[ \] (.+)", text):
            item = m.group(1)
            dm = re.search(r"\d{4}-\d{2}-\d{2}", item)
            if dm:
                due = _parse_date(dm.group())
                if due and due < _today():
                    overdue += 1
    if overdue == 0:
        return "🟢"
    elif overdue <= 2:
        return "🟡"
    return "🔴"


# ─── Vault resolution ────────────────────────────────────────────────────────

def _resolve_vault_path():
    """Resolve vault path: OBSIDIAN_VAULT env var → .env file → default."""
    path = os.environ.get("OBSIDIAN_VAULT", "").strip()
    if path:
        return os.path.normpath(os.path.expanduser(os.path.expandvars(path)))

    for env_dir in [os.getcwd(), _BRAINSTEM_DIR]:
        env_file = os.path.join(env_dir, ".env")
        if os.path.isfile(env_file):
            try:
                with open(env_file, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("OBSIDIAN_VAULT="):
                            val = line.split("=", 1)[1].strip().strip('"').strip("'")
                            if val:
                                return os.path.normpath(
                                    os.path.expanduser(os.path.expandvars(val))
                                )
            except OSError:
                pass

    return _DEFAULT_VAULT


def _ensure_vault(vault):
    """Create vault directory structure if it doesn't exist."""
    dirs = [
        os.path.join(vault, "01-raw"),
        os.path.join(vault, "02-wiki", "concepts"),
        os.path.join(vault, "03-people", "_archived"),
        os.path.join(vault, "04-output"),
        os.path.join(vault, "log"),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)


# ─── People helpers ───────────────────────────────────────────────────────────

def _find_person_dir(vault, name):
    """Find a person's directory by name or slug."""
    slug = _slugify(name)
    people_dir = os.path.join(vault, "03-people")
    target = os.path.join(people_dir, slug)
    if os.path.isdir(target):
        return target
    if os.path.isdir(people_dir):
        for entry in os.listdir(people_dir):
            if entry.startswith("_") or entry.startswith("."):
                continue
            candidate = os.path.join(people_dir, entry)
            if not os.path.isdir(candidate):
                continue
            profile = _safe_read(os.path.join(candidate, "profile.md"))
            fm, _ = _parse_frontmatter(profile)
            if fm.get("name", "").lower() == name.lower():
                return candidate
    return None


def _load_all_people(vault):
    """Load metadata for all active people from their profile.md frontmatter."""
    people_dir = os.path.join(vault, "03-people")
    people = []
    if not os.path.isdir(people_dir):
        return people
    for entry in sorted(os.listdir(people_dir)):
        if entry.startswith("_") or entry.startswith("."):
            continue
        person_dir = os.path.join(people_dir, entry)
        if not os.path.isdir(person_dir):
            continue
        profile = _safe_read(os.path.join(person_dir, "profile.md"))
        fm, _ = _parse_frontmatter(profile)
        if not fm.get("name"):
            continue
        fm["slug"] = entry
        fm["dir"] = person_dir
        people.append(fm)
    return people


def _load_active_people(vault):
    """Load metadata for active (non-archived, non-retired) people."""
    people_dir = os.path.join(vault, "03-people")
    people = []
    if not os.path.isdir(people_dir):
        return people
    for entry in sorted(os.listdir(people_dir)):
        if entry.startswith("_") or entry.startswith("."):
            continue
        person_dir = os.path.join(people_dir, entry)
        if not os.path.isdir(person_dir):
            continue
        profile = _safe_read(os.path.join(person_dir, "profile.md"))
        fm, _ = _parse_frontmatter(profile)
        if not fm.get("name"):
            continue
        status = fm.get("status", "active").lower()
        if status in ("retired", "archived", "inactive"):
            continue
        fm["slug"] = entry
        fm["dir"] = person_dir
        people.append(fm)
    return people


def _regenerate_roster(vault):
    """Regenerate _roster.md from all active person profiles."""
    people = _load_all_people(vault)
    lines = [
        "# Team Roster",
        "",
        "> Auto-generated by ObsidianPilot. Do not edit manually.",
        "",
        "| Name | Role | Start Date | Phase | Days | Manager |",
        "|------|------|------------|-------|------|---------|",
    ]
    for p in people:
        days = _day_count(p.get("start_date", ""))
        phase = _phase_label(days)
        lines.append(
            f"| [[{p.get('name', '?')}]] "
            f"| {p.get('role', '?')} "
            f"| {p.get('start_date', '?')} "
            f"| {phase} "
            f"| {days} "
            f"| {p.get('manager', '—')} |"
        )
    lines.append("")
    _safe_write(os.path.join(vault, "03-people", "_roster.md"), "\n".join(lines))


# ─── Templates ────────────────────────────────────────────────────────────────

def _person_profile_template(name, role, start_date, manager, context):
    fm = {
        "name": name,
        "role": role,
        "start_date": start_date,
        "manager": manager or "—",
        "status": "active",
        "created": _today().isoformat(),
    }
    body = f"# {name}\n\n**Role:** {role}\n**Start Date:** {start_date}\n**Manager:** {manager or '—'}\n"
    if context:
        body += f"\n## Context\n\n{context}\n"
    return _build_frontmatter(fm) + "\n\n" + body


def _plan_template(name, phase_num, start_date):
    phase_names = {1: "First 30 Days", 2: "Days 31–60", 3: "Days 61–90"}
    phase = phase_names.get(phase_num, f"Phase {phase_num}")
    return (
        f"# {name} — {phase}\n\n"
        f"Start date: {start_date}\n\n"
        f"## Goals\n\n- [ ] \n\n"
        f"## Key Results\n\n- [ ] \n\n"
        f"## Notes\n\n"
    )


def _priorities_template(name):
    return (
        f"# {name} — Priorities\n\n"
        f"## NOW\n\n\n\n"
        f"## NEXT\n\n\n\n"
        f"## LATER\n\n\n"
    )


def _metrics_template(name):
    return (
        f"# {name} — Metrics\n\n"
        f"## Completion Rate\n\n_Auto-calculated from plan files._\n\n"
        f"## Velocity\n\n_Tasks completed per week._\n\n"
        f"## Training Progress\n\n- [ ] Onboarding checklist complete\n\n"
        f"## Notes\n\n"
    )


def _training_quest_template(name, role):
    return (
        f"# {name} — Training Quest\n\n"
        f"Role: {role}\n\n"
        f"## Week 1: Orientation\n\n- [ ] Meet the team\n- [ ] Set up dev environment\n- [ ] Review codebase\n\n"
        f"## Week 2: First Contributions\n\n- [ ] Complete first PR\n- [ ] Shadow a senior engineer\n\n"
        f"## Week 3: Independence\n\n- [ ] Own a small feature\n- [ ] Present at team standup\n\n"
        f"## Week 4: Integration\n\n- [ ] Lead a code review\n- [ ] Propose an improvement\n"
    )


def _notes_template(name):
    return f"# {name} — Notes\n\nRunning notes, 1:1 topics, observations.\n\n"


# ─── HTML Report ──────────────────────────────────────────────────────────────

def _generate_report_html(people, vault):
    """Generate a complete self-contained HTML dashboard report."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    cards_html = ""
    phase_counts = {"Phase 1 (30-day)": 0, "Phase 2 (60-day)": 0, "Phase 3 (90-day)": 0, "Complete": 0}
    overdue_data = []

    for p in people:
        name = p.get("name", "?")
        role = p.get("role", "?")
        days = _day_count(p.get("start_date", ""))
        phase = _phase_label(days)
        phase_counts[phase] = phase_counts.get(phase, 0) + 1
        person_dir = p.get("dir", "")

        total_done, total_tasks = 0, 0
        for fname in ["30-day.md", "60-day.md", "90-day.md"]:
            d, t = _count_tasks(_safe_read(os.path.join(person_dir, fname)))
            total_done += d
            total_tasks += t

        pct = int((total_done / total_tasks * 100)) if total_tasks > 0 else 0
        status = _status_indicator(person_dir)

        overdue_count = 0
        for fname in ["30-day.md", "60-day.md", "90-day.md", "priorities.md"]:
            text = _safe_read(os.path.join(person_dir, fname))
            for m in re.findall(r"- \[ \] .+?\d{4}-\d{2}-\d{2}", text):
                dm = re.search(r"\d{4}-\d{2}-\d{2}", m)
                if dm and _parse_date(dm.group()) and _parse_date(dm.group()) < _today():
                    overdue_count += 1
        overdue_data.append((name, overdue_count))

        pri_text = _safe_read(os.path.join(person_dir, "priorities.md"))
        now_items = _extract_section_items(pri_text, "NOW")

        phase_color = {"Phase 1 (30-day)": "#0078d4", "Phase 2 (60-day)": "#107c10",
                       "Phase 3 (90-day)": "#ff8c00", "Complete": "#6b6b6b"}.get(phase, "#333")

        now_list = ""
        for item in now_items[:3]:
            now_list += f"<li>{html.escape(item)}</li>"
        if len(now_items) > 3:
            now_list += f"<li><em>+{len(now_items) - 3} more</em></li>"

        cards_html += f"""
        <div class="card" style="border-left:4px solid {phase_color}">
          <div class="card-header">
            <span class="status-dot">{status}</span>
            <strong>{html.escape(name)}</strong>
            <span class="role">{html.escape(role)}</span>
          </div>
          <div class="card-meta">
            <span class="phase" style="color:{phase_color}">{phase}</span>
            <span class="days">Day {days}</span>
          </div>
          <div class="progress-bar">
            <div class="progress-fill" style="width:{pct}%;background:{phase_color}"></div>
          </div>
          <div class="progress-label">{total_done}/{total_tasks} tasks ({pct}%)</div>
          {f'<ul class="now-items">{now_list}</ul>' if now_list else ''}
          {f'<div class="overdue">⚠ {overdue_count} overdue</div>' if overdue_count else ''}
        </div>"""

    phase_dist = ""
    for phase, count in phase_counts.items():
        if count > 0:
            phase_dist += f'<span class="phase-chip">{phase}: {count}</span> '

    heatmap_html = ""
    max_overdue = max((x[1] for x in overdue_data), default=0)
    if max_overdue > 0:
        heatmap_html = '<div class="heatmap"><h3>Overdue Heatmap</h3><div class="heatmap-grid">'
        for name, count in overdue_data:
            intensity = min(1.0, count / max(max_overdue, 1))
            r = int(255 * intensity)
            g = int(255 * (1 - intensity * 0.7))
            bg = f"rgb({r},{g},100)"
            heatmap_html += f'<div class="heat-cell" style="background:{bg}" title="{html.escape(name)}: {count} overdue">{html.escape(name.split()[0])}<br><strong>{count}</strong></div>'
        heatmap_html += "</div></div>"

    report = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Team 30-60-90 Dashboard</title>
<style>
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{font-family:'Segoe UI',-apple-system,Helvetica,Arial,sans-serif;
    color:#333;background:#fafafa;line-height:1.5;padding:20px 40px}}
  .header{{margin-bottom:32px;border-bottom:2px solid #0078d4;padding-bottom:16px}}
  .header h1{{font-size:1.8rem;font-weight:300;color:#0078d4}}
  .header .meta{{color:#888;font-size:0.85rem;margin-top:4px}}
  .phase-dist{{margin:16px 0;display:flex;gap:8px;flex-wrap:wrap}}
  .phase-chip{{background:#f0f0f0;padding:4px 12px;border-radius:12px;font-size:0.8rem;color:#555}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:20px;margin-top:20px}}
  .card{{background:#fff;border-radius:6px;padding:16px 20px;box-shadow:0 1px 3px rgba(0,0,0,0.08)}}
  .card-header{{display:flex;align-items:center;gap:8px;margin-bottom:8px}}
  .card-header strong{{font-size:1.05rem}}
  .role{{color:#888;font-size:0.8rem;margin-left:auto}}
  .status-dot{{font-size:1rem}}
  .card-meta{{display:flex;gap:16px;font-size:0.85rem;margin-bottom:10px}}
  .phase{{font-weight:600}}
  .days{{color:#888}}
  .progress-bar{{height:6px;background:#eee;border-radius:3px;overflow:hidden}}
  .progress-fill{{height:100%;border-radius:3px;transition:width 0.3s}}
  .progress-label{{font-size:0.75rem;color:#999;margin-top:4px}}
  .now-items{{margin:10px 0 0 16px;font-size:0.85rem;color:#555}}
  .now-items li{{margin:2px 0}}
  .overdue{{color:#d13438;font-size:0.8rem;font-weight:600;margin-top:8px}}
  .heatmap{{margin-top:32px}}
  .heatmap h3{{font-size:1rem;font-weight:400;color:#555;margin-bottom:12px}}
  .heatmap-grid{{display:flex;gap:8px;flex-wrap:wrap}}
  .heat-cell{{padding:12px;border-radius:6px;text-align:center;font-size:0.75rem;
    color:#fff;min-width:80px}}
  .footer{{margin-top:40px;padding-top:16px;border-top:1px solid #ddd;
    color:#999;font-size:0.8rem}}
</style>
</head>
<body>
<div class="header">
  <h1>Team 30-60-90 Dashboard</h1>
  <div class="meta">Generated {ts} by ObsidianPilot</div>
</div>
<div class="phase-dist">{phase_dist}</div>
<div class="grid">{cards_html}</div>
{heatmap_html}
<div class="footer">ObsidianPilot — "Your vault, your command." — Made by HOLO</div>
</body>
</html>"""
    return report


# ─── Sentinel config management ──────────────────────────────────────────────

def _default_config():
    """Return the default sentinel config."""
    jobs = {}
    for job_name in _ALL_JOBS:
        jobs[job_name] = {
            "enabled": True,
            "paused": False,
            "schedule": "daily",
            "time": "08:00",
            "last_run": None,
            "last_success": None,
            "last_error": "",
            "last_status": "never_run",
        }
    return {
        "version": 1,
        "updated_at": _now_iso(),
        "vault_path": "",
        "jobs": jobs,
        "watched_urls": [],
        "last_digest_at": None,
        "notifications": {
            "console": True,
            "file": True,
        },
    }


def _config_path(vault):
    return os.path.join(vault, ".obsidian-sentinel", "config.json")


def _load_config(vault):
    """Load config, creating defaults if missing."""
    path = _config_path(vault)
    if os.path.isfile(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            default = _default_config()
            for job_name in _ALL_JOBS:
                if job_name not in cfg.get("jobs", {}):
                    cfg.setdefault("jobs", {})[job_name] = default["jobs"][job_name]
            return cfg
        except (json.JSONDecodeError, OSError):
            pass
    return _default_config()


def _save_config(vault, cfg):
    """Persist config atomically."""
    cfg["updated_at"] = _now_iso()
    path = _config_path(vault)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, default=str)
    os.replace(tmp, path)


# ─── Agent ────────────────────────────────────────────────────────────────────

class ObsidianPilotAgent(BasicAgent):
    """Obsidian vault manager for 30-60-90 plans, wiki knowledge bases, and scheduled automation."""

    def __init__(self):
        self.name = "ObsidianPilot"
        self.metadata = {
            "name": self.name,
            "description": (
                "Obsidian vault manager for multi-person 30-60-90 day plans, "
                "LLM knowledge bases, and scheduled automation. "
                "People: add_person, roster, check_in, retire, assign, priorities, metrics, plan. "
                "Reporting: report (HTML dashboard), dashboard (text summary), review (weekly). "
                "Wiki: compile, ingest, health, query. "
                "Productivity: paste (quick raw-text ingest), log (activity log), "
                "okr (objectives & key results), kanban (generate Kanban board). "
                "Automation: brief (morning digest), watch (URL monitor), "
                "job_status (show scheduled jobs), run_job (trigger a job), "
                "setup (configure jobs), pause (toggle job)."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": [
                            "add_person", "roster", "check_in", "retire", "assign",
                            "priorities", "metrics", "report", "dashboard", "compile",
                            "ingest", "health", "query", "review", "plan",
                            "brief", "watch", "job_status", "run_job", "setup", "pause",
                            "bootstrap",
                            "training", "build_quest",
                            "paste", "log", "okr", "kanban",
                        ],
                        "description": (
                            "add_person=create a new person's 30-60-90 folder, "
                            "roster=list all people, check_in=status for one person, "
                            "retire=archive a person, assign=add a priority task, "
                            "priorities=show priority board, metrics=person metrics, "
                            "report=generate HTML dashboard, dashboard=quick text summary, "
                            "compile=rebuild wiki from raw sources, ingest=add content to vault, "
                            "health=wiki lint check, query=search wiki, "
                            "review=weekly review, plan=personal 30-60-90 status, "
                            "brief=generate morning digest, watch=add/list monitored URLs, "
                            "job_status=show all scheduled jobs, run_job=manually trigger a job, "
                            "setup=configure scheduled jobs, pause=pause or resume a job, "
                            "bootstrap=create vault structure + install Obsidian plugins automatically, "
                            "training=read a person's learning objectives and design a training quest, "
                            "build_quest=render training quest HTML from checkpoint JSON, "
                            "paste=quick-ingest raw text into 01-raw, "
                            "log=show or add to activity log, "
                            "okr=track objectives and key results per person, "
                            "kanban=generate Kanban board from priorities"
                        ),
                    },
                    "name": {"type": "string", "description": "Person name for people actions"},
                    "role": {"type": "string", "description": "Role/title for add_person"},
                    "start_date": {"type": "string", "description": "Start date YYYY-MM-DD for add_person"},
                    "manager": {"type": "string", "description": "Manager name for add_person"},
                    "context": {"type": "string", "description": "Additional context for add_person"},
                    "priority": {"type": "string", "description": "now/next/later for assign action"},
                    "task": {"type": "string", "description": "Task description for assign action"},
                    "url": {"type": "string", "description": "URL for ingest or watch actions"},
                    "topic": {"type": "string", "description": "Topic for query action"},
                    "checkpoints": {"type": "string", "description": "JSON array of checkpoint objects for build_quest action"},
                    "content": {"type": "string", "description": "Raw text content for paste action"},
                    "title": {"type": "string", "description": "Title for paste action"},
                    "note": {"type": "string", "description": "Manual note for log action"},
                    "objective": {"type": "string", "description": "Objective text for okr action"},
                    "key_result": {"type": "string", "description": "Key result text for okr action"},
                    "job": {
                        "type": "string",
                        "enum": _ALL_JOBS,
                        "description": (
                            "Job name for run_job/pause/setup actions: "
                            "morning_brief, content_watch, auto_review, "
                            "wiki_health, phase_alert, digest"
                        ),
                    },
                    "enabled": {
                        "type": "boolean",
                        "description": "Enable (true) or disable (false) a job in setup",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)
        self._vault = None

    def system_context(self):
        vault = self.vault
        obs_dir = os.path.join(vault, ".obsidian")
        if not os.path.isdir(obs_dir) or not os.path.isfile(os.path.join(obs_dir, "community-plugins.json")):
            return (
                "<ObsidianPilot>\n"
                "The Obsidian vault has not been bootstrapped yet. On your FIRST response "
                "to the user, mention that you can auto-setup their Obsidian vault with plugins "
                "and configuration by calling ObsidianPilot action=bootstrap. Say something like: "
                "'I can set up your Obsidian vault with all the right plugins and configuration "
                "automatically. Want me to run bootstrap?'\n"
                "</ObsidianPilot>"
            )
        return None

    @property
    def vault(self):
        if self._vault is None:
            self._vault = _resolve_vault_path()
        return self._vault

    # ══════════════════════════════════════════════════════════════════════
    #  Logging Helper
    # ══════════════════════════════════════════════════════════════════════

    def _log(self, message):
        """Append to log/activity.md."""
        log_dir = os.path.join(self.vault, "log")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, "activity.md")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        entry = f"- [{timestamp}] {message}\n"
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(entry)

    # ══════════════════════════════════════════════════════════════════════
    #  Action Dispatch
    # ══════════════════════════════════════════════════════════════════════

    def perform(self, **kwargs):
        action = kwargs.get("action", "dashboard")
        dispatch = {
            # People actions
            "add_person": self._action_add_person,
            "roster": self._action_roster,
            "check_in": self._action_check_in,
            "retire": self._action_retire,
            "assign": self._action_assign,
            "priorities": self._action_priorities,
            "metrics": self._action_metrics,
            "plan": self._action_plan,
            # Reporting actions
            "report": self._action_report,
            "dashboard": self._action_dashboard,
            "review": self._action_review,
            # Wiki actions
            "compile": self._action_compile,
            "ingest": self._action_ingest,
            "health": self._action_health,
            "query": self._action_query,
            # Automation actions (from Sentinel)
            "brief": self._action_brief,
            "watch": self._action_watch,
            "job_status": self._action_job_status,
            "run_job": self._action_run_job,
            "setup": self._action_setup,
            "pause": self._action_pause,
            "bootstrap": self._action_bootstrap,
            "training": self._action_training,
            "build_quest": self._action_build_quest,
            # Productivity actions
            "paste": self._action_paste,
            "log": self._action_log,
            "okr": self._action_okr,
            "kanban": self._action_kanban,
        }
        handler = dispatch.get(action)
        if not handler:
            return f"❌ Unknown action `{action}`. Valid: {', '.join(dispatch.keys())}"
        try:
            return handler(**kwargs)
        except Exception as e:
            return f"❌ Error in `{action}`: {e}"

    # ══════════════════════════════════════════════════════════════════════
    #  People Actions
    # ══════════════════════════════════════════════════════════════════════

    # ── 1. add_person ─────────────────────────────────────────────────────

    def _action_add_person(self, **kwargs):
        name = kwargs.get("name", "").strip()
        if not name:
            return "❌ `name` is required for add_person."
        role = kwargs.get("role", "Team Member").strip()
        start_date = kwargs.get("start_date", _today().isoformat()).strip()
        manager = kwargs.get("manager", "").strip()
        context = kwargs.get("context", "").strip()

        if not _parse_date(start_date):
            return f"❌ Invalid start_date `{start_date}`. Use YYYY-MM-DD format."

        _ensure_vault(self.vault)
        slug = _slugify(name)
        person_dir = os.path.join(self.vault, "03-people", slug)

        if os.path.isdir(person_dir):
            return f"⚠️ Person `{name}` already exists at `03-people/{slug}/`."

        os.makedirs(person_dir, exist_ok=True)
        os.makedirs(os.path.join(person_dir, "weekly"), exist_ok=True)

        _safe_write(os.path.join(person_dir, "profile.md"),
                    _person_profile_template(name, role, start_date, manager, context))
        _safe_write(os.path.join(person_dir, "30-day.md"),
                    _plan_template(name, 1, start_date))
        _safe_write(os.path.join(person_dir, "60-day.md"),
                    _plan_template(name, 2, start_date))
        _safe_write(os.path.join(person_dir, "90-day.md"),
                    _plan_template(name, 3, start_date))
        _safe_write(os.path.join(person_dir, "priorities.md"),
                    _priorities_template(name))
        _safe_write(os.path.join(person_dir, "metrics.md"),
                    _metrics_template(name))
        _safe_write(os.path.join(person_dir, "training-quest.md"),
                    _training_quest_template(name, role))
        _safe_write(os.path.join(person_dir, "notes.md"),
                    _notes_template(name))

        _regenerate_roster(self.vault)

        days = _day_count(start_date)
        phase = _phase_label(days)
        self._log(f"Added person: {name}")
        return (
            f"✅ Added **{name}** ({role})\n\n"
            f"- 📁 `03-people/{slug}/`\n"
            f"- 📅 Start: {start_date} (Day {days}, {phase})\n"
            f"- 👤 Manager: {manager or '—'}\n"
            f"- 📝 Created: profile.md, 30/60/90-day plans, priorities, "
            f"metrics, training-quest, notes, weekly/\n"
            f"- 📋 Roster updated"
        )

    # ── 2. roster ─────────────────────────────────────────────────────────

    def _action_roster(self, **kwargs):
        _ensure_vault(self.vault)
        people = _load_all_people(self.vault)
        if not people:
            return "📋 **Team Roster** — No people tracked yet. Use `add_person` to add someone."

        lines = ["# 📋 Team Roster", "", "| Status | Name | Role | Start | Day | Phase |",
                 "|--------|------|------|-------|-----|-------|"]
        for p in people:
            days = _day_count(p.get("start_date", ""))
            phase = _phase_label(days)
            status = _status_indicator(p.get("dir", ""))
            lines.append(
                f"| {status} | {p.get('name', '?')} | {p.get('role', '?')} "
                f"| {p.get('start_date', '?')} | {days} | {phase} |"
            )
        lines.append(f"\n_{len(people)} active people_")

        _regenerate_roster(self.vault)
        return "\n".join(lines)

    # ── 3. check_in ───────────────────────────────────────────────────────

    def _action_check_in(self, **kwargs):
        name = kwargs.get("name", "").strip()
        if not name:
            return "❌ `name` is required for check_in."

        person_dir = _find_person_dir(self.vault, name)
        if not person_dir:
            return f"❌ Person `{name}` not found in vault."

        profile = _safe_read(os.path.join(person_dir, "profile.md"))
        fm, _ = _parse_frontmatter(profile)
        days = _day_count(fm.get("start_date", ""))
        phase = _phase_label(days)
        active_file = _phase_file(days)

        plan_text = _safe_read(os.path.join(person_dir, active_file))
        done_plan, total_plan = _count_tasks(plan_text)

        pri_text = _safe_read(os.path.join(person_dir, "priorities.md"))
        now_items = _extract_section_items(pri_text, "NOW")

        overdue = []
        for fname in ["30-day.md", "60-day.md", "90-day.md", "priorities.md"]:
            text = _safe_read(os.path.join(person_dir, fname))
            for m in re.finditer(r"- \[ \] (.+)", text):
                item = m.group(1)
                dm = re.search(r"\d{4}-\d{2}-\d{2}", item)
                if dm:
                    due = _parse_date(dm.group())
                    if due and due < _today():
                        overdue.append(f"- ⏰ {item.strip()} (from {fname})")

        upcoming = []
        for fname in ["30-day.md", "60-day.md", "90-day.md", "priorities.md"]:
            text = _safe_read(os.path.join(person_dir, fname))
            for m in re.finditer(r"- \[ \] (.+)", text):
                item = m.group(1)
                dm = re.search(r"\d{4}-\d{2}-\d{2}", item)
                if dm:
                    due = _parse_date(dm.group())
                    if due and _today() <= due <= _today().replace(
                        day=min(_today().day + 7, 28)
                    ):
                        upcoming.append(f"- 📅 {item.strip()} (from {fname})")

        status = _status_indicator(person_dir)
        lines = [
            f"# {status} Check-in: {fm.get('name', name)}",
            f"**{fm.get('role', '?')}** — Day {days}, {phase}",
            "",
            f"## 📊 Active Plan ({active_file})",
            f"Progress: {done_plan}/{total_plan} tasks complete"
            + (f" ({int(done_plan / total_plan * 100)}%)" if total_plan else ""),
            "",
        ]

        if now_items:
            lines.append("## 🎯 NOW Priorities")
            for item in now_items:
                lines.append(f"- {item}")
            lines.append("")

        if overdue:
            lines.append(f"## 🔴 Overdue ({len(overdue)})")
            lines.extend(overdue)
            lines.append("")

        if upcoming:
            lines.append(f"## 📅 Upcoming (next 7 days)")
            lines.extend(upcoming)
            lines.append("")

        if not overdue and not upcoming:
            lines.append("_No dated items found. Add dates to tasks (YYYY-MM-DD) for tracking._")

        return "\n".join(lines)

    # ── 4. retire ─────────────────────────────────────────────────────────

    def _action_retire(self, **kwargs):
        name = kwargs.get("name", "").strip()
        if not name:
            return "❌ `name` is required for retire."

        person_dir = _find_person_dir(self.vault, name)
        if not person_dir:
            return f"❌ Person `{name}` not found in vault."

        profile = _safe_read(os.path.join(person_dir, "profile.md"))
        fm, body = _parse_frontmatter(profile)
        days = _day_count(fm.get("start_date", ""))

        total_done, total_tasks = 0, 0
        for fname in ["30-day.md", "60-day.md", "90-day.md"]:
            d, t = _count_tasks(_safe_read(os.path.join(person_dir, fname)))
            total_done += d
            total_tasks += t

        summary = (
            f"# {fm.get('name', name)} — Final Summary\n\n"
            f"**Archived:** {_today().isoformat()}\n"
            f"**Duration:** {days} days\n"
            f"**Completion:** {total_done}/{total_tasks} tasks\n\n"
            f"## Role\n{fm.get('role', '?')}\n\n"
            f"## Manager\n{fm.get('manager', '—')}\n"
        )
        _safe_write(os.path.join(person_dir, "_final_summary.md"), summary)

        fm["status"] = "archived"
        fm["archived_date"] = _today().isoformat()
        _safe_write(
            os.path.join(person_dir, "profile.md"),
            _build_frontmatter(fm) + "\n\n" + body,
        )

        slug = os.path.basename(person_dir)
        archive_dir = os.path.join(self.vault, "03-people", "_archived", slug)
        if os.path.exists(archive_dir):
            archive_dir = archive_dir + f"-{_today().isoformat()}"
        os.rename(person_dir, archive_dir)

        _regenerate_roster(self.vault)

        pct = int(total_done / total_tasks * 100) if total_tasks else 0
        self._log(f"Retired: {name}")
        return (
            f"📦 **{fm.get('name', name)}** archived\n\n"
            f"- Duration: {days} days\n"
            f"- Completion: {total_done}/{total_tasks} ({pct}%)\n"
            f"- Moved to: `03-people/_archived/{slug}/`\n"
            f"- Final summary written\n"
            f"- Roster updated"
        )

    # ── 5. assign ─────────────────────────────────────────────────────────

    def _action_assign(self, **kwargs):
        name = kwargs.get("name", "").strip()
        priority = kwargs.get("priority", "").strip().upper()
        task = kwargs.get("task", "").strip()

        if not name:
            return "❌ `name` is required for assign."
        if priority not in ("NOW", "NEXT", "LATER"):
            return "❌ `priority` must be now, next, or later."
        if not task:
            return "❌ `task` is required for assign."

        person_dir = _find_person_dir(self.vault, name)
        if not person_dir:
            return f"❌ Person `{name}` not found in vault."

        pri_path = os.path.join(person_dir, "priorities.md")
        text = _safe_read(pri_path)

        if not text.strip():
            profile = _safe_read(os.path.join(person_dir, "profile.md"))
            fm, _ = _parse_frontmatter(profile)
            text = _priorities_template(fm.get("name", name))

        section_pattern = rf"(##\s*{priority}\s*\n)"
        match = re.search(section_pattern, text, re.IGNORECASE)
        if match:
            insert_pos = match.end()
            new_line = f"- [ ] {task}\n"
            text = text[:insert_pos] + new_line + text[insert_pos:]
        else:
            text += f"\n## {priority}\n\n- [ ] {task}\n"

        _safe_write(pri_path, text)
        self._log(f"Assigned {priority} to {name}: {task}")
        return f"✅ Assigned to **{name}** [{priority}]: {task}"

    # ── 6. priorities ─────────────────────────────────────────────────────

    def _action_priorities(self, **kwargs):
        name = kwargs.get("name", "").strip()

        if name:
            person_dir = _find_person_dir(self.vault, name)
            if not person_dir:
                return f"❌ Person `{name}` not found in vault."

            pri_text = _safe_read(os.path.join(person_dir, "priorities.md"))
            if not pri_text.strip():
                return f"📋 **{name}** has no priorities set yet. Use `assign` to add tasks."

            now = _extract_section_items(pri_text, "NOW")
            nxt = _extract_section_items(pri_text, "NEXT")
            later = _extract_section_items(pri_text, "LATER")

            lines = [f"# 🎯 {name} — Priorities", ""]
            if now:
                lines.append("## NOW")
                for item in now:
                    lines.append(f"- {item}")
                lines.append("")
            if nxt:
                lines.append("## NEXT")
                for item in nxt:
                    lines.append(f"- {item}")
                lines.append("")
            if later:
                lines.append("## LATER")
                for item in later:
                    lines.append(f"- {item}")
                lines.append("")
            if not (now or nxt or later):
                lines.append("_No priorities found. Use `assign` to add tasks._")
            return "\n".join(lines)

        people = _load_all_people(self.vault)
        if not people:
            return "📋 No people tracked yet."

        lines = ["# 🎯 Team NOW Priorities", ""]
        for p in people:
            pri_text = _safe_read(os.path.join(p.get("dir", ""), "priorities.md"))
            now = _extract_section_items(pri_text, "NOW")
            lines.append(f"### {p.get('name', '?')}")
            if now:
                for item in now:
                    lines.append(f"- {item}")
            else:
                lines.append("_No NOW items_")
            lines.append("")
        return "\n".join(lines)

    # ── 7. metrics ────────────────────────────────────────────────────────

    def _action_metrics(self, **kwargs):
        name = kwargs.get("name", "").strip()
        if not name:
            return "❌ `name` is required for metrics."

        person_dir = _find_person_dir(self.vault, name)
        if not person_dir:
            return f"❌ Person `{name}` not found in vault."

        profile = _safe_read(os.path.join(person_dir, "profile.md"))
        fm, _ = _parse_frontmatter(profile)
        days = _day_count(fm.get("start_date", ""))

        phase_stats = []
        grand_done, grand_total = 0, 0
        for fname in ["30-day.md", "60-day.md", "90-day.md"]:
            text = _safe_read(os.path.join(person_dir, fname))
            d, t = _count_tasks(text)
            grand_done += d
            grand_total += t
            pct = int(d / t * 100) if t > 0 else 0
            phase_stats.append(f"- {fname}: {d}/{t} ({pct}%)")

        grand_pct = int(grand_done / grand_total * 100) if grand_total > 0 else 0

        weeks = max(1, days / 7)
        velocity = round(grand_done / weeks, 1)

        overdue = 0
        for fname in ["30-day.md", "60-day.md", "90-day.md", "priorities.md"]:
            text = _safe_read(os.path.join(person_dir, fname))
            for m in re.finditer(r"- \[ \] .+?(\d{4}-\d{2}-\d{2})", text):
                due = _parse_date(m.group(1))
                if due and due < _today():
                    overdue += 1

        tq = _safe_read(os.path.join(person_dir, "training-quest.md"))
        tq_done, tq_total = _count_tasks(tq)
        tq_pct = int(tq_done / tq_total * 100) if tq_total > 0 else 0

        lines = [
            f"# 📊 Metrics: {fm.get('name', name)}",
            f"Day {days} — {_phase_label(days)}",
            "",
            "## Completion Rate",
            f"**Overall: {grand_done}/{grand_total} ({grand_pct}%)**",
            "",
        ]
        lines.extend(phase_stats)
        lines.extend([
            "",
            "## Velocity",
            f"**{velocity} tasks/week** ({grand_done} tasks in {days} days)",
            "",
            "## Overdue Items",
            f"**{overdue}** overdue task(s)" if overdue else "✅ No overdue items",
            "",
            "## Training Progress",
            f"**{tq_done}/{tq_total} ({tq_pct}%)** training checkpoints complete",
        ])

        return "\n".join(lines)

    # ── 8. plan ───────────────────────────────────────────────────────────

    def _action_plan(self, **kwargs):
        _ensure_vault(self.vault)
        name = kwargs.get("name", "").strip() or kwargs.get("topic", "").strip()

        if name:
            person_dir = _find_person_dir(self.vault, name)
            if not person_dir:
                return f"❌ Person `{name}` not found in vault."
        else:
            people = _load_all_people(self.vault)
            if not people:
                return "📋 No people tracked. Use `add_person` to add someone."
            person_dir = people[0].get("dir", "")
            name = people[0].get("name", "?")

        profile = _safe_read(os.path.join(person_dir, "profile.md"))
        fm, _ = _parse_frontmatter(profile)
        days = _day_count(fm.get("start_date", ""))
        phase = _phase_label(days)

        lines = [
            f"# 📋 30-60-90 Plan: {fm.get('name', name)}",
            f"**{fm.get('role', '?')}** — Day {days}, {phase}",
            "",
        ]

        for fname, label in [("30-day.md", "Phase 1 (Days 1-30)"),
                              ("60-day.md", "Phase 2 (Days 31-60)"),
                              ("90-day.md", "Phase 3 (Days 61-90)")]:
            text = _safe_read(os.path.join(person_dir, fname))
            d, t = _count_tasks(text)
            pct = int(d / t * 100) if t > 0 else 0
            active = "→ " if fname == _phase_file(days) else "  "
            bar = "█" * (pct // 10) + "░" * (10 - pct // 10)
            lines.append(f"{active}**{label}**: {bar} {d}/{t} ({pct}%)")

        lines.append("")

        active_file = _phase_file(days)
        active_text = _safe_read(os.path.join(person_dir, active_file))
        if active_text:
            lines.append(f"## Active: {active_file}")
            for m in re.finditer(r"- \[ \] (.+)", active_text):
                lines.append(f"- [ ] {m.group(1).strip()}")
            for m in re.finditer(r"- \[x\] (.+)", active_text, re.IGNORECASE):
                lines.append(f"- [x] {m.group(1).strip()}")

        return "\n".join(lines)

    # ══════════════════════════════════════════════════════════════════════
    #  Reporting Actions
    # ══════════════════════════════════════════════════════════════════════

    # ── 9. report ─────────────────────────────────────────────────────────

    def _action_report(self, **kwargs):
        _ensure_vault(self.vault)
        people = _load_all_people(self.vault)
        if not people:
            return "📋 No people tracked yet. Add someone first with `add_person`."

        html_content = _generate_report_html(people, self.vault)

        os.makedirs(_DELIVERABLES_DIR, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d-%H%M")
        filename = f"team-30-60-90-dashboard-{ts}.html"
        out_path = os.path.join(_DELIVERABLES_DIR, filename)
        _safe_write(out_path, html_content)

        file_uri = Path(out_path).resolve().as_uri()
        webbrowser.open(file_uri)

        self._log("Generated team report")
        return (
            f"📊 **Team Dashboard Generated**\n\n"
            f"- 📁 `deliverables/{filename}`\n"
            f"- 👥 {len(people)} people\n"
            f"- 🌐 Opened in browser"
        )

    # ── 10. dashboard ─────────────────────────────────────────────────────

    def _action_dashboard(self, **kwargs):
        _ensure_vault(self.vault)
        people = _load_all_people(self.vault)
        if not people:
            return "📋 No people tracked yet. Use `add_person` to get started."

        lines = ["# 📊 Team Dashboard", ""]
        phase_counts = {}
        for p in people:
            days = _day_count(p.get("start_date", ""))
            phase = _phase_label(days)
            phase_counts[phase] = phase_counts.get(phase, 0) + 1
            status = _status_indicator(p.get("dir", ""))

            total_done, total_tasks = 0, 0
            for fname in ["30-day.md", "60-day.md", "90-day.md"]:
                d, t = _count_tasks(_safe_read(os.path.join(p.get("dir", ""), fname)))
                total_done += d
                total_tasks += t

            pct = int(total_done / total_tasks * 100) if total_tasks > 0 else 0
            lines.append(
                f"{status} **{p.get('name', '?')}** — {phase}, Day {days} — "
                f"{total_done}/{total_tasks} ({pct}%)"
            )
        lines.append("")
        lines.append("**Phase Distribution:** " +
                     ", ".join(f"{k}: {v}" for k, v in phase_counts.items()))
        lines.append(f"\n_{len(people)} active people_")
        return "\n".join(lines)

    # ── 11. review ────────────────────────────────────────────────────────

    def _action_review(self, **kwargs):
        _ensure_vault(self.vault)

        daily_dirs = [
            os.path.join(self.vault, "daily"),
            os.path.join(self.vault, "Daily Notes"),
            os.path.join(self.vault, "journal"),
            os.path.join(self.vault, "Journal"),
        ]

        recent_notes = []
        cutoff = _today().replace(day=max(1, _today().day - 7))

        for ddir in daily_dirs:
            if not os.path.isdir(ddir):
                continue
            for fname in sorted(os.listdir(ddir), reverse=True):
                if not fname.endswith(".md"):
                    continue
                date_match = re.search(r"(\d{4}-\d{2}-\d{2})", fname)
                if date_match:
                    note_date = _parse_date(date_match.group(1))
                    if note_date and note_date >= cutoff:
                        text = _safe_read(os.path.join(ddir, fname))
                        recent_notes.append((note_date, fname, text))

        if not recent_notes:
            for fname in sorted(os.listdir(self.vault), reverse=True):
                if not fname.endswith(".md"):
                    continue
                date_match = re.search(r"(\d{4}-\d{2}-\d{2})", fname)
                if date_match:
                    note_date = _parse_date(date_match.group(1))
                    if note_date and note_date >= cutoff:
                        text = _safe_read(os.path.join(self.vault, fname))
                        recent_notes.append((note_date, fname, text))

        if not recent_notes:
            return (
                "📝 **Weekly Review**\n\n"
                "No recent daily notes found. I looked in:\n"
                + "\n".join(f"- `{d}`" for d in ["daily/", "Daily Notes/", "journal/", "Journal/"]) +
                "\n\nCreate daily notes with dates in the filename (YYYY-MM-DD) for auto-review."
            )

        recent_notes.sort(key=lambda x: x[0])
        lines = [
            "# 📝 Weekly Review",
            f"_{len(recent_notes)} notes from the past 7 days_",
            "",
        ]
        all_tasks_done = []
        all_tasks_todo = []

        for note_date, fname, text in recent_notes:
            lines.append(f"## {note_date.strftime('%A, %B %d')}")

            content_lines = [l.strip() for l in text.split("\n")
                            if l.strip() and not l.strip().startswith("#")]
            preview = " ".join(content_lines[:3])[:200]
            if preview:
                lines.append(preview)

            for m in re.finditer(r"- \[x\] (.+)", text, re.IGNORECASE):
                all_tasks_done.append(m.group(1).strip())
            for m in re.finditer(r"- \[ \] (.+)", text):
                all_tasks_todo.append(m.group(1).strip())

            lines.append("")

        if all_tasks_done:
            lines.append(f"## ✅ Completed ({len(all_tasks_done)})")
            for t in all_tasks_done[:10]:
                lines.append(f"- {t}")
            lines.append("")

        if all_tasks_todo:
            lines.append(f"## 📋 Still Open ({len(all_tasks_todo)})")
            for t in all_tasks_todo[:10]:
                lines.append(f"- {t}")
            lines.append("")

        return "\n".join(lines)

    # ══════════════════════════════════════════════════════════════════════
    #  Wiki Actions
    # ══════════════════════════════════════════════════════════════════════

    # ── 12. compile ───────────────────────────────────────────────────────

    def _action_compile(self, **kwargs):
        _ensure_vault(self.vault)
        raw_dir = os.path.join(self.vault, "01-raw")
        wiki_dir = os.path.join(self.vault, "02-wiki", "concepts")
        os.makedirs(wiki_dir, exist_ok=True)

        raw_files = _collect_md_files(raw_dir)
        if not raw_files:
            return "📚 No files found in `01-raw/`. Use `ingest` to add content first."

        compiled = []
        all_concepts = []
        for fpath in sorted(raw_files):
            text = _safe_read(fpath)
            if not text.strip():
                continue

            basename = os.path.splitext(os.path.basename(fpath))[0]
            slug = _slugify(basename)

            title_match = re.search(r"^#\s+(.+)", text, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else basename

            headings = re.findall(r"^##\s+(.+)", text, re.MULTILINE)

            summary_lines = []
            paragraphs = text.split("\n\n")
            char_count = 0
            for para in paragraphs:
                para = para.strip()
                if para and not para.startswith("#"):
                    summary_lines.append(para)
                    char_count += len(para)
                    if char_count > 1000:
                        break

            article = (
                f"# {title}\n\n"
                f"> Compiled from `01-raw/{os.path.basename(fpath)}`\n\n"
            )
            if headings:
                article += "## Key Topics\n\n"
                for h in headings:
                    article += f"- [[{h}]]\n"
                article += "\n"
            if summary_lines:
                article += "## Summary\n\n" + "\n\n".join(summary_lines) + "\n"

            wiki_path = os.path.join(wiki_dir, f"{slug}.md")
            _safe_write(wiki_path, article)
            compiled.append(f"- `{slug}.md` ← `{os.path.basename(fpath)}`")
            all_concepts.append({"title": title, "slug": slug, "source": os.path.basename(fpath)})

        index_lines = [
            "# 📚 Wiki Index",
            "",
            "> Auto-generated by ObsidianPilot compile.",
            "",
            "| Article | Source |",
            "|---------|--------|",
        ]
        for c in all_concepts:
            index_lines.append(f"| [[{c['title']}]] | `{c['source']}` |")
        index_lines.append(f"\n_{len(all_concepts)} articles_")
        _safe_write(os.path.join(self.vault, "02-wiki", "_index.md"), "\n".join(index_lines))

        self._log("Compiled wiki")
        return (
            f"📚 **Wiki Compiled**\n\n"
            f"Processed {len(raw_files)} raw files → {len(compiled)} wiki articles\n\n"
            + "\n".join(compiled) +
            f"\n\n_Index updated: `02-wiki/_index.md`_"
        )

    # ── 13. ingest ────────────────────────────────────────────────────────

    def _action_ingest(self, **kwargs):
        url = kwargs.get("url", "").strip()
        path = kwargs.get("topic", "").strip()

        _ensure_vault(self.vault)
        raw_dir = os.path.join(self.vault, "01-raw")
        os.makedirs(raw_dir, exist_ok=True)

        if url and (url.startswith("http://") or url.startswith("https://")):
            return self._ingest_url(url, raw_dir)
        elif url:
            return self._ingest_file(url, raw_dir)
        elif path and os.path.isfile(path):
            return self._ingest_file(path, raw_dir)
        else:
            return "❌ Provide a `url` (http/https) or file path to ingest."

    def _ingest_url(self, url, raw_dir):
        """Fetch a URL and save to raw directory."""
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "ObsidianPilot/2.0",
                "Accept": "text/html,text/plain,application/json,*/*",
            })
            with urllib.request.urlopen(req, timeout=30) as resp:
                content_type = resp.headers.get("Content-Type", "")
                if not any(t in content_type for t in ["text/", "application/json", "application/xml"]):
                    return f"❌ Non-text content type: {content_type}. Only text content can be ingested."

                raw = resp.read(1024 * 1024)
                charset = "utf-8"
                ct_match = re.search(r"charset=([^\s;]+)", content_type)
                if ct_match:
                    charset = ct_match.group(1)
                text = raw.decode(charset, errors="replace")

        except urllib.error.HTTPError as e:
            return f"❌ HTTP {e.code}: {e.reason}"
        except urllib.error.URLError as e:
            return f"❌ URL error: {e.reason}"
        except Exception as e:
            return f"❌ Fetch failed: {e}"

        text = re.sub(r"<script[^>]*>.*?</script>", "", text, flags=re.DOTALL)
        text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL)
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()

        from urllib.parse import urlparse
        parsed = urlparse(url)
        slug = _slugify(parsed.netloc + "-" + parsed.path.strip("/").replace("/", "-"))
        if not slug:
            slug = "ingested"
        slug = slug[:80]

        ts = datetime.now().strftime("%Y%m%d")
        filename = f"{slug}-{ts}.md"
        out_path = os.path.join(raw_dir, filename)

        content = f"---\nsource: {url}\ningested: {_today().isoformat()}\n---\n\n# {parsed.netloc}{parsed.path}\n\n{text}"
        _safe_write(out_path, content)

        summary_text = text[:500] + ("..." if len(text) > 500 else "")
        wiki_dir = os.path.join(os.path.dirname(raw_dir), "02-wiki", "concepts")
        os.makedirs(wiki_dir, exist_ok=True)
        wiki_article = (
            f"# {parsed.netloc}{parsed.path}\n\n"
            f"> Ingested from [{url}]({url}) on {_today().isoformat()}\n\n"
            f"## Summary\n\n{summary_text}\n\n"
            f"_See full content: `01-raw/{filename}`_\n"
        )
        wiki_path = os.path.join(wiki_dir, f"{slug}.md")
        _safe_write(wiki_path, wiki_article)

        self._log(f"Ingested: {url}")
        return (
            f"📥 **Ingested URL**\n\n"
            f"- Source: {url}\n"
            f"- Raw: `01-raw/{filename}` ({len(text)} chars)\n"
            f"- Wiki: `02-wiki/concepts/{slug}.md`"
        )

    def _ingest_file(self, filepath, raw_dir):
        """Read a local file and save to raw directory."""
        filepath = os.path.normpath(os.path.expanduser(filepath))
        if not os.path.isfile(filepath):
            return f"❌ File not found: `{filepath}`"

        text = _safe_read(filepath)
        if not text.strip():
            return f"❌ File is empty: `{filepath}`"

        basename = os.path.splitext(os.path.basename(filepath))[0]
        slug = _slugify(basename)
        ts = datetime.now().strftime("%Y%m%d")
        filename = f"{slug}-{ts}.md"
        out_path = os.path.join(raw_dir, filename)

        content = f"---\nsource: {filepath}\ningested: {_today().isoformat()}\n---\n\n{text}"
        _safe_write(out_path, content)

        summary_text = text[:500] + ("..." if len(text) > 500 else "")
        wiki_dir = os.path.join(os.path.dirname(raw_dir), "02-wiki", "concepts")
        os.makedirs(wiki_dir, exist_ok=True)
        wiki_article = (
            f"# {basename}\n\n"
            f"> Ingested from `{filepath}` on {_today().isoformat()}\n\n"
            f"## Summary\n\n{summary_text}\n\n"
            f"_See full content: `01-raw/{filename}`_\n"
        )
        wiki_path = os.path.join(wiki_dir, f"{slug}.md")
        _safe_write(wiki_path, wiki_article)

        self._log(f"Ingested: {filepath}")
        return (
            f"📥 **Ingested File**\n\n"
            f"- Source: `{filepath}`\n"
            f"- Raw: `01-raw/{filename}` ({len(text)} chars)\n"
            f"- Wiki: `02-wiki/concepts/{slug}.md`"
        )

    # ── 14. health ────────────────────────────────────────────────────────

    def _action_health(self, **kwargs):
        _ensure_vault(self.vault)
        wiki_dir = os.path.join(self.vault, "02-wiki")
        raw_dir = os.path.join(self.vault, "01-raw")

        issues = []
        suggestions = []

        all_files = _collect_md_files(self.vault)
        all_titles = set()
        all_links = set()
        link_targets = {}
        stale_threshold = 90

        for fpath in all_files:
            text = _safe_read(fpath)
            basename = os.path.splitext(os.path.basename(fpath))[0]
            all_titles.add(basename.lower())

            for m in re.finditer(r"\[\[([^\]|#]+)(?:[|#][^\]]+)?\]\]", text):
                target = m.group(1).strip().lower()
                all_links.add(target)
                link_targets.setdefault(target, []).append(os.path.basename(fpath))

        broken = all_links - all_titles
        for b in sorted(broken):
            sources = link_targets.get(b, [])
            issues.append(f"🔗 Broken link `[[{b}]]` referenced from: {', '.join(sources[:3])}")

        wiki_files = _collect_md_files(wiki_dir)
        for fpath in wiki_files:
            basename = os.path.splitext(os.path.basename(fpath))[0]
            if basename.startswith("_"):
                continue
            if basename.lower() not in all_links:
                issues.append(f"🏝️ Orphaned wiki article: `{basename}.md` (no incoming links)")

        for fpath in wiki_files:
            try:
                mtime = os.path.getmtime(fpath)
                age_days = (_today() - date.fromtimestamp(mtime)).days
                if age_days > stale_threshold:
                    issues.append(
                        f"📅 Stale: `{os.path.basename(fpath)}` last modified {age_days} days ago"
                    )
            except OSError:
                pass

        raw_files = _collect_md_files(raw_dir)
        wiki_slugs = {os.path.splitext(os.path.basename(f))[0].lower() for f in wiki_files}
        for fpath in raw_files:
            slug = _slugify(os.path.splitext(os.path.basename(fpath))[0])
            if slug not in wiki_slugs:
                suggestions.append(f"📝 Raw file `{os.path.basename(fpath)}` has no wiki article. Run `compile`.")

        if not issues and not suggestions:
            return (
                "✅ **Wiki Health: All Clear**\n\n"
                f"- {len(all_files)} markdown files scanned\n"
                f"- {len(all_links)} wikilinks checked\n"
                f"- No issues found"
            )

        lines = [
            f"# 🏥 Wiki Health Check",
            f"Scanned {len(all_files)} files, {len(all_links)} wikilinks",
            "",
        ]
        if issues:
            lines.append(f"## Issues ({len(issues)})")
            lines.extend(issues)
            lines.append("")
        if suggestions:
            lines.append(f"## Suggestions ({len(suggestions)})")
            lines.extend(suggestions)
            lines.append("")

        return "\n".join(lines)

    # ── 15. query ─────────────────────────────────────────────────────────

    def _action_query(self, **kwargs):
        topic = kwargs.get("topic", "").strip()
        if not topic:
            return "❌ `topic` is required for query."

        _ensure_vault(self.vault)
        wiki_dir = os.path.join(self.vault, "02-wiki")
        keywords = [w.lower() for w in re.split(r"\s+", topic) if len(w) > 2]

        results = []
        wiki_files = _collect_md_files(wiki_dir)

        for fpath in wiki_files:
            text = _safe_read(fpath)
            text_lower = text.lower()
            score = sum(text_lower.count(kw) for kw in keywords)
            if score > 0:
                best_para = ""
                best_score = 0
                for para in text.split("\n\n"):
                    p_score = sum(para.lower().count(kw) for kw in keywords)
                    if p_score > best_score:
                        best_score = p_score
                        best_para = para.strip()
                results.append((score, os.path.basename(fpath), best_para[:300]))

        results.sort(key=lambda x: -x[0])

        if not results:
            return f"🔍 No results found for `{topic}` in the wiki."

        lines = [f"# 🔍 Query: {topic}", f"Found {len(results)} relevant articles", ""]
        for score, fname, snippet in results[:5]:
            lines.append(f"### {fname} (relevance: {score})")
            lines.append(snippet)
            lines.append("")

        return "\n".join(lines)

    # ══════════════════════════════════════════════════════════════════════
    #  Automation Actions (merged from ObsidianSentinel)
    # ══════════════════════════════════════════════════════════════════════

    # ── 16. brief ─────────────────────────────────────────────────────────

    def _action_brief(self, **kwargs):
        """Generate the morning brief directly."""
        _ensure_vault(self.vault)
        cfg = _load_config(self.vault)
        result = self._job_morning_brief(cfg)
        cfg["jobs"]["morning_brief"]["last_run"] = _now_iso()
        cfg["jobs"]["morning_brief"]["last_status"] = "ok"
        cfg["jobs"]["morning_brief"]["last_success"] = _now_iso()
        cfg["jobs"]["morning_brief"]["last_error"] = ""
        _save_config(self.vault, cfg)
        self._log("Generated morning brief")
        return result

    # ── 17. watch ─────────────────────────────────────────────────────────

    def _action_watch(self, **kwargs):
        """Add or list watched URLs."""
        _ensure_vault(self.vault)
        cfg = _load_config(self.vault)
        url = kwargs.get("url", "").strip() if kwargs.get("url") else ""

        if url:
            existing = [u["url"] for u in cfg.get("watched_urls", [])]
            if url in existing:
                return f"⚠️ URL already watched: `{url}`"

            cfg.setdefault("watched_urls", []).append({
                "url": url,
                "enabled": True,
                "etag": "",
                "last_modified": "",
                "sha256": "",
                "last_checked": "",
                "last_changed": "",
                "last_error": "",
            })
            _save_config(self.vault, cfg)
            return (
                f"✅ Now watching: `{url}`\n\n"
                f"Total watched URLs: {len(cfg['watched_urls'])}\n"
                f"Run `action=run_job, job=content_watch` to check now."
            )

        urls = cfg.get("watched_urls", [])
        if not urls:
            return (
                "📡 **Content Watch** — No URLs being monitored.\n\n"
                "Add one with `action=watch, url=\"https://...\"`"
            )

        lines = ["# 📡 Watched URLs", ""]
        lines.append("| # | URL | Enabled | Last Checked | Last Changed |")
        lines.append("|---|-----|---------|--------------|--------------|")
        for i, u in enumerate(urls, 1):
            en = "✅" if u.get("enabled", True) else "⛔"
            checked = u.get("last_checked", "")[:10] or "never"
            changed = u.get("last_changed", "")[:10] or "never"
            display_url = u["url"]
            if len(display_url) > 60:
                display_url = display_url[:57] + "..."
            lines.append(f"| {i} | `{display_url}` | {en} | {checked} | {changed} |")

        return "\n".join(lines)

    # ── 18. job_status ────────────────────────────────────────────────────

    def _action_job_status(self, **kwargs):
        """Show all jobs with last run, next run, enabled state."""
        _ensure_vault(self.vault)
        cfg = _load_config(self.vault)

        lines = ["# 📊 ObsidianPilot — Job Status", ""]
        lines.append("| Job | State | Last Run | Last Status |")
        lines.append("|-----|-------|----------|-------------|")

        for jname in _ALL_JOBS:
            j = cfg["jobs"].get(jname, {})
            if not j.get("enabled", True):
                state = "⛔ Disabled"
            elif j.get("paused", False):
                state = "⏸️ Paused"
            else:
                state = "▶️ Active"

            last_run = j.get("last_run")
            if last_run:
                try:
                    lr_dt = datetime.fromisoformat(last_run)
                    age_s = (datetime.now(timezone.utc) - lr_dt).total_seconds()
                    if age_s < 3600:
                        ago = f"{int(age_s / 60)}m ago"
                    elif age_s < 86400:
                        ago = f"{int(age_s / 3600)}h ago"
                    else:
                        ago = f"{int(age_s / 86400)}d ago"
                    last_display = ago
                except (ValueError, TypeError):
                    last_display = str(last_run)[:19]
            else:
                last_display = "never"

            last_status = j.get("last_status", "never_run")
            status_icon = {"ok": "✅", "error": "❌", "never_run": "⬜"}.get(
                last_status, "⬜"
            )

            lines.append(
                f"| {jname} | {state} | {last_display} | "
                f"{status_icon} {last_status} |"
            )

        urls = cfg.get("watched_urls", [])
        active_urls = [u for u in urls if u.get("enabled", True)]
        lines.append("")
        lines.append(f"**Watched URLs:** {len(active_urls)} active / {len(urls)} total")

        last_digest = cfg.get("last_digest_at")
        lines.append(
            f"**Last digest:** {last_digest[:19] if last_digest else 'never'}"
        )
        lines.append(f"**Vault:** `{self.vault}`")

        return "\n".join(lines)

    # ── 19. run_job ───────────────────────────────────────────────────────

    def _action_run_job(self, **kwargs):
        """Manually trigger a specific job."""
        job_name = kwargs.get("job", "").strip() if kwargs.get("job") else ""
        if not job_name:
            return (
                "❌ `job` is required for run_job. Valid jobs:\n"
                + "\n".join(f"- `{j}` — {_JOB_DESCRIPTIONS[j]}" for j in _ALL_JOBS)
            )
        if job_name not in _ALL_JOBS:
            return f"❌ Unknown job `{job_name}`. Valid: {', '.join(_ALL_JOBS)}"

        _ensure_vault(self.vault)
        cfg = _load_config(self.vault)

        job_dispatch = {
            "morning_brief": self._job_morning_brief,
            "content_watch": self._job_content_watch,
            "auto_review": self._job_auto_review,
            "wiki_health": self._job_wiki_health,
            "phase_alert": self._job_phase_alert,
            "digest": self._job_digest,
        }

        handler = job_dispatch.get(job_name)
        if not handler:
            return f"❌ Job `{job_name}` has no implementation."

        cfg["jobs"][job_name]["last_run"] = _now_iso()
        try:
            result = handler(cfg)
            cfg["jobs"][job_name]["last_status"] = "ok"
            cfg["jobs"][job_name]["last_success"] = _now_iso()
            cfg["jobs"][job_name]["last_error"] = ""
            _save_config(self.vault, cfg)
            return result
        except Exception as e:
            cfg["jobs"][job_name]["last_status"] = "error"
            cfg["jobs"][job_name]["last_error"] = str(e)
            _save_config(self.vault, cfg)
            return f"❌ Job `{job_name}` failed: {e}"

    # ── 20. setup ─────────────────────────────────────────────────────────

    def _action_setup(self, **kwargs):
        """Show or configure scheduled jobs."""
        _ensure_vault(self.vault)
        cfg = _load_config(self.vault)
        job_name = kwargs.get("job", "").strip() if kwargs.get("job") else ""
        enabled = kwargs.get("enabled")

        if job_name:
            if job_name not in _ALL_JOBS:
                return f"❌ Unknown job `{job_name}`. Valid: {', '.join(_ALL_JOBS)}"
            if enabled is not None:
                cfg["jobs"][job_name]["enabled"] = bool(enabled)
                if bool(enabled):
                    cfg["jobs"][job_name]["paused"] = False
                _save_config(self.vault, cfg)
                state = "enabled ✅" if enabled else "disabled ⛔"
                return f"⚙️ Job **{job_name}** is now **{state}**."
            j = cfg["jobs"][job_name]
            return (
                f"## ⚙️ Job: {job_name}\n\n"
                f"- **Description:** {_JOB_DESCRIPTIONS.get(job_name, '—')}\n"
                f"- **Enabled:** {j['enabled']}\n"
                f"- **Paused:** {j['paused']}\n"
                f"- **Schedule:** {j.get('schedule', 'daily')} at {j.get('time', '—')}\n"
                f"- **Last run:** {j.get('last_run') or 'never'}\n"
                f"- **Last status:** {j.get('last_status', '—')}\n"
                f"- **Last error:** {j.get('last_error') or '—'}"
            )

        lines = ["# ⚙️ ObsidianPilot — Job Configuration", ""]
        lines.append("| Job | Enabled | Paused | Schedule | Description |")
        lines.append("|-----|---------|--------|----------|-------------|")
        for jname in _ALL_JOBS:
            j = cfg["jobs"].get(jname, {})
            en = "✅" if j.get("enabled", True) else "⛔"
            pa = "⏸️" if j.get("paused", False) else "▶️"
            sched = j.get("schedule", "daily")
            desc = _JOB_DESCRIPTIONS.get(jname, "")
            lines.append(f"| {jname} | {en} | {pa} | {sched} | {desc} |")

        lines.append("")
        lines.append("_Use `setup` with `job` and `enabled` params to configure._")
        return "\n".join(lines)

    # ── 21. pause ─────────────────────────────────────────────────────────

    def _action_pause(self, **kwargs):
        """Toggle pause state on a job."""
        job_name = kwargs.get("job", "").strip() if kwargs.get("job") else ""
        if not job_name:
            return (
                "❌ `job` is required for pause. Valid jobs:\n"
                + "\n".join(f"- `{j}`" for j in _ALL_JOBS)
            )
        if job_name not in _ALL_JOBS:
            return f"❌ Unknown job `{job_name}`. Valid: {', '.join(_ALL_JOBS)}"

        _ensure_vault(self.vault)
        cfg = _load_config(self.vault)
        job_cfg = cfg["jobs"][job_name]

        if not job_cfg.get("enabled", True):
            return f"⚠️ Job `{job_name}` is disabled. Enable it first with `setup`."

        was_paused = job_cfg.get("paused", False)
        job_cfg["paused"] = not was_paused
        _save_config(self.vault, cfg)

        if was_paused:
            return f"▶️ Job **{job_name}** has been **resumed**."
        else:
            return f"⏸️ Job **{job_name}** has been **paused**."

    # ══════════════════════════════════════════════════════════════════════
    #  Bootstrap Action
    # ══════════════════════════════════════════════════════════════════════

    _REQUIRED_PLUGINS = {
        "templater-obsidian": {
            "name": "Templater",
            "repo": "SilentVoid13/Templater",
            "desc": "Template engine — powers all vault templates",
        },
        "dataview": {
            "name": "Dataview",
            "repo": "blacksmithgu/obsidian-dataview",
            "desc": "Query notes like a database",
        },
        "calendar": {
            "name": "Calendar",
            "repo": "liamcain/obsidian-calendar-plugin",
            "desc": "Daily note navigation via calendar widget",
        },
        "obsidian-kanban": {
            "name": "Kanban",
            "repo": "mgmeyers/obsidian-kanban",
            "desc": "Drag-and-drop Kanban boards from markdown",
        },
        "obsidian-git": {
            "name": "Obsidian Git",
            "repo": "Vinzent03/obsidian-git",
            "desc": "Version control your vault with Git",
        },
    }

    def _action_bootstrap(self, **kwargs):
        """Create vault structure, download & install Obsidian plugins, configure settings."""
        vault = self.vault
        results = []

        # 1. Create vault structure
        _ensure_vault(vault)
        results.append("✅ Vault structure verified")

        # 2. Create .obsidian directory
        obs_dir = os.path.join(vault, ".obsidian")
        plugins_dir = os.path.join(obs_dir, "plugins")
        os.makedirs(plugins_dir, exist_ok=True)

        # 3. Download and install plugins
        installed = []
        failed = []
        for plugin_id, info in self._REQUIRED_PLUGINS.items():
            plugin_dir = os.path.join(plugins_dir, plugin_id)
            manifest_path = os.path.join(plugin_dir, "manifest.json")

            if os.path.isfile(manifest_path):
                installed.append(f"✅ **{info['name']}** — already installed")
                continue

            os.makedirs(plugin_dir, exist_ok=True)
            try:
                base_url = f"https://github.com/{info['repo']}/releases/latest/download"
                for fname in ["manifest.json", "main.js"]:
                    url = f"{base_url}/{fname}"
                    req = urllib.request.Request(url, headers={"User-Agent": "RAPP-ObsidianPilot/1.0"})
                    resp = urllib.request.urlopen(req, timeout=15)
                    with open(os.path.join(plugin_dir, fname), "wb") as f:
                        f.write(resp.read())

                # Try styles.css (optional, some plugins don't have it)
                try:
                    url = f"{base_url}/styles.css"
                    req = urllib.request.Request(url, headers={"User-Agent": "RAPP-ObsidianPilot/1.0"})
                    resp = urllib.request.urlopen(req, timeout=10)
                    with open(os.path.join(plugin_dir, "styles.css"), "wb") as f:
                        f.write(resp.read())
                except Exception:
                    pass  # styles.css is optional

                installed.append(f"✅ **{info['name']}** — downloaded and installed")
            except Exception as e:
                failed.append(f"❌ **{info['name']}** — failed: {e}")

        # 4. Write community-plugins.json (enables plugins on Obsidian startup)
        cp_path = os.path.join(obs_dir, "community-plugins.json")
        plugin_ids = list(self._REQUIRED_PLUGINS.keys())
        # Preserve any existing plugins
        if os.path.isfile(cp_path):
            try:
                with open(cp_path, "r", encoding="utf-8") as f:
                    existing = json.loads(f.read())
                if isinstance(existing, list):
                    for pid in existing:
                        if pid not in plugin_ids:
                            plugin_ids.append(pid)
            except Exception:
                pass
        with open(cp_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(plugin_ids, indent=2))
        results.append(f"✅ Enabled {len(plugin_ids)} plugins in community-plugins.json")

        # 5. Disable safe mode (required for community plugins)
        app_json_path = os.path.join(obs_dir, "app.json")
        app_config = {}
        if os.path.isfile(app_json_path):
            try:
                with open(app_json_path, "r", encoding="utf-8") as f:
                    app_config = json.loads(f.read())
            except Exception:
                pass
        app_config["community-plugins-enabled"] = True
        with open(app_json_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(app_config, indent=2))

        # 6. Configure Templater settings
        templater_dir = os.path.join(plugins_dir, "templater-obsidian")
        if os.path.isdir(templater_dir):
            data_path = os.path.join(templater_dir, "data.json")
            templater_config = {}
            if os.path.isfile(data_path):
                try:
                    with open(data_path, "r", encoding="utf-8") as f:
                        templater_config = json.loads(f.read())
                except Exception:
                    pass
            templater_config["templates_folder"] = "templates"
            with open(data_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(templater_config, indent=2))
            results.append("✅ Templater configured (templates folder = templates/)")

        # 7. Configure daily notes
        daily_notes_config = {
            "folder": "00-inbox",
            "template": "templates/daily-note.md",
            "autorun": False,
        }
        core_plugins_path = os.path.join(obs_dir, "core-plugins.json")
        core_plugins = ["file-explorer", "global-search", "switcher", "graph",
                        "backlink", "tag-pane", "page-preview", "daily-notes",
                        "templates", "command-palette", "editor-status", "outline"]
        with open(core_plugins_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(core_plugins, indent=2))

        daily_notes_path = os.path.join(obs_dir, "daily-notes.json")
        with open(daily_notes_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(daily_notes_config, indent=2))
        results.append("✅ Daily notes configured (folder = 00-inbox/)")

        # Build output
        output = (
            "## 🚀 ObsidianPilot Bootstrap Complete — Made by HOLO\n\n"
            f"**Vault:** `{vault}`\n\n"
            "### Vault Structure\n"
            + results[0] + "\n\n"
            "### Plugins\n"
            + "\n".join(installed + failed) + "\n\n"
            "### Configuration\n"
            + "\n".join(results[1:]) + "\n\n"
        )

        if failed:
            output += (
                "### ⚠️ Manual Steps Needed\n"
                "Some plugins failed to download. Open Obsidian → Settings → "
                "Community plugins → Browse → search and install:\n"
                + "\n".join(f"- {f}" for f in failed) + "\n\n"
            )

        output += (
            "### Next Steps\n"
            "1. **Open Obsidian** → File → Open folder as vault → select `" + vault + "`\n"
            "2. Obsidian will load with plugins pre-installed and configured\n"
            "3. Say **\"Add me to the 30-60-90 tracker\"** in brainstem to get started\n"
        )

        self._log("Bootstrap completed")
        return output

        return output

    # ══════════════════════════════════════════════════════════════════════
    #  Training Quest Actions
    # ══════════════════════════════════════════════════════════════════════

    def _action_training(self, **kwargs):
        """Read a person's training-quest.md and return it with instructions for the LLM to design checkpoints."""
        name = kwargs.get("name", "").strip()
        if not name:
            return "❌ `name` is required. Example: `action=training, name=\"Jane Smith\"`"

        slug = _slugify(name)
        quest_path = os.path.join(self.vault, "03-people", slug, "training-quest.md")
        if not os.path.isfile(quest_path):
            return f"❌ No training-quest.md found for {name} at `{quest_path}`"

        with open(quest_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # Also read their profile for context
        profile_path = os.path.join(self.vault, "03-people", slug, "profile.md")
        profile = ""
        if os.path.isfile(profile_path):
            with open(profile_path, "r", encoding="utf-8", errors="replace") as f:
                profile = f.read(3000)

        return (
            f"## Training Quest Design for {name}\n\n"
            f"I've read {name}'s training objectives and profile. Now I need YOU to design "
            f"the training checkpoints.\n\n"
            f"**Read the content below**, then call me again with `action=build_quest` "
            f"and provide `name=\"{name}\"` plus a `checkpoints` parameter containing a JSON array.\n\n"
            f"### Checkpoint JSON Format\n\n"
            f"Each checkpoint object must have:\n"
            f"```json\n"
            f'{{\n'
            f'  "phase": 1,\n'
            f'  "emoji": "🚀",\n'
            f'  "title": "Short Title (max 35 chars)",\n'
            f'  "time": "10 min",\n'
            f'  "desc": "Clear description of what to learn and why it matters.",\n'
            f'  "substeps": ["Step 1: do this", "Step 2: then this"],\n'
            f'  "copies": [{{"label": "Try this", "text": "actual command or prompt to copy"}}],\n'
            f'  "learn": "Key concepts covered",\n'
            f'  "stuck": "Detailed troubleshooting if they get stuck.",\n'
            f'  "toggle": "I completed this ✓"\n'
            f'}}\n'
            f"```\n\n"
            f"### Rules\n"
            f"1. Tasks must be **actionable** — things the person DOES, not just reads\n"
            f"2. Copies must be **real commands/prompts** they can paste and run\n"
            f"3. Stuck text must **solve real problems** with specific guidance\n"
            f"4. Phase numbers 1-4, aim for 8-16 checkpoints total\n"
            f"5. Base the checkpoints on the **learning objectives** in the training-quest.md\n"
            f"6. Tailor to the person's **role and context** from their profile\n\n"
            f"---\n\n"
            f"### {name}'s Profile\n```\n{profile[:2000]}\n```\n\n"
            f"### {name}'s Training Objectives\n```\n{content}\n```"
        )

    def _action_build_quest(self, **kwargs):
        """Render an interactive HTML training quest from LLM-designed checkpoint JSON."""
        name = kwargs.get("name", "Training Quest").strip()
        checkpoints_json = kwargs.get("checkpoints", "")
        if not checkpoints_json:
            return "❌ `checkpoints` JSON is required. Call `action=training` first to get the design instructions."

        try:
            raw_cps = json.loads(checkpoints_json)
            if not isinstance(raw_cps, list) or len(raw_cps) == 0:
                return "❌ Checkpoints must be a non-empty JSON array."
        except json.JSONDecodeError as e:
            return f"❌ Invalid JSON: {e}"

        # Normalize checkpoints
        all_cps = []
        for i, cp in enumerate(raw_cps):
            n = {
                "id": cp.get("id", f"step-{i+1}"),
                "phase": cp.get("phase", 1),
                "emoji": cp.get("emoji", "📋"),
                "title": str(cp.get("title", f"Step {i+1}"))[:40],
                "time": cp.get("time", "5 min"),
                "desc": str(cp.get("desc", "")),
                "toggle": cp.get("toggle", "Done ✓"),
            }
            if cp.get("substeps"):
                n["substeps"] = [str(s) for s in cp["substeps"][:10]]
            if cp.get("copies"):
                n["copies"] = [{"label": str(c.get("label", "Copy")), "text": str(c.get("text", ""))} for c in cp["copies"][:6]]
            if cp.get("learn"):
                n["learn"] = str(cp["learn"])
            if cp.get("stuck"):
                n["stuck"] = str(cp["stuck"])
            for key in ["desc", "stuck", "learn", "toggle"]:
                if key in n and isinstance(n[key], str):
                    n[key] = n[key].replace("'", "\\'")
            all_cps.append(n)

        # Generate positions
        phases_used = sorted(set(cp["phase"] for cp in all_cps))
        counts = [0] * max(4, len(phases_used))
        for cp in all_cps:
            counts[cp["phase"] - 1] += 1

        positions = self._generate_quest_positions(counts[:4])
        phase_labels = {1: "🚀 Foundations", 2: "📚 Skills", 3: "⚡ Application", 4: "🏆 Mastery"}
        labels = [phase_labels.get(p, f"Phase {p}") for p in phases_used]
        while len(labels) < 4:
            labels.append("")

        # Render HTML
        total = len(all_cps)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        cp_json = json.dumps(all_cps, indent=2)
        pos_json = json.dumps(positions, indent=2)

        # Compute proportional widths
        weights = [max(c, 1) if c > 0 else 0 for c in counts[:4]]
        total_w = sum(w for w in weights if w > 0) or 1
        widths = [(w / total_w * 100) if w > 0 else 0 for w in weights]
        for i in range(4):
            if widths[i] > 0 and widths[i] < 15:
                deficit = 15 - widths[i]
                widths[i] = 15
                largest = max(range(4), key=lambda x: widths[x])
                widths[largest] -= deficit

        lp = []
        dp = []
        x = 0
        for i, w in enumerate(widths):
            lp.append(round(x + 1, 1) if w > 0 else -100)
            if i < 3:
                x += w
                dp.append(round(x, 1) if w > 0 else -100)
        while len(dp) < 3:
            dp.append(-100)

        slug = _slugify(name)
        quest_title = f"{name} Training Quest"

        html = self._render_quest_html(quest_title, all_cps, positions, labels, lp, dp, total, timestamp, cp_json, pos_json)

        # Save and open
        out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "deliverables")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"training-quest-{slug}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        import webbrowser
        webbrowser.open(f"file://{os.path.abspath(out_path)}")

        return (
            f"## ✅ Training Quest Generated for {name}!\n\n"
            f"**File:** `{out_path}`\n\n"
            f"**{total} checkpoints** across {len(phases_used)} phases.\n\n"
            f"Opened in browser! — Made by HOLO"
        )

    def _generate_quest_positions(self, counts):
        """Generate non-overlapping node positions for the quest map."""
        weights = [max(c, 2) if c > 0 else 0 for c in counts]
        total_w = sum(w for w in weights if w > 0) or 1
        widths = [(w / total_w * 100) if w > 0 else 0 for w in weights]
        for i in range(4):
            if widths[i] > 0 and widths[i] < 15:
                deficit = 15 - widths[i]
                widths[i] = 15
                largest = max(range(4), key=lambda x: widths[x])
                widths[largest] -= deficit
        boundaries = []
        x = 0
        for w in widths:
            boundaries.append((x + 2, x + w - 2) if w > 0 else (0, 0))
            x += w
        positions = []
        for phase_idx, count in enumerate(counts):
            if count == 0:
                continue
            x_min, x_max = boundaries[phase_idx]
            x_mid = (x_min + x_max) / 2
            x_swing = (x_max - x_min) * 0.35
            y_top, y_bottom = 16, 82
            step = (y_bottom - y_top) / (count - 1) if count > 1 else 0
            for i in range(count):
                y = y_top + i * step if count > 1 else 50
                px = x_mid - x_swing if i % 2 == 0 else x_mid + x_swing
                positions.append({"x": round(px, 1), "y": round(y, 1)})
        return positions

    def _render_quest_html(self, title, cps, positions, labels, lp, dp, total, timestamp, cp_json, pos_json):
        pl = labels
        return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--bg:#eaecf0;--blue:#0969da;--green:#1a7f37;--orange:#bf8700;--red:#cf222e;--text:#24292f;--text-muted:#57606a;--border:#c5ccd6;--panel-w:460px;--top-bar:52px}}
html,body{{height:100%;overflow:hidden;font-family:'Segoe UI',system-ui,sans-serif;background:linear-gradient(135deg,#dfe2e6,var(--bg));color:var(--text)}}
.top-bar{{position:fixed;top:0;left:0;right:0;height:var(--top-bar);background:rgba(234,236,240,.94);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);display:flex;align-items:center;padding:0 24px;z-index:100}}
.top-bar .title{{font-size:15px;font-weight:600}}.top-bar .title span{{color:var(--blue)}}
.progress-wrap{{flex:1;max-width:420px;margin:0 auto;display:flex;align-items:center;gap:10px}}
.progress-track{{flex:1;height:8px;background:var(--border);border-radius:4px;overflow:hidden}}
.progress-fill{{height:100%;background:linear-gradient(90deg,var(--blue),var(--green));border-radius:4px;transition:width .6s}}
.progress-label{{font-size:13px;color:var(--text-muted);min-width:90px;text-align:right}}
.btn-reset{{background:transparent;border:1px solid var(--border);color:var(--text-muted);padding:6px 12px;border-radius:6px;cursor:pointer;font-size:12px}}.btn-reset:hover{{border-color:var(--red);color:var(--red)}}
.quest-map{{position:fixed;top:var(--top-bar);left:0;right:0;bottom:0;overflow:hidden}}
.quest-map svg{{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}}
.phase-label{{position:absolute;font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:3px;color:var(--text-muted);opacity:.55;pointer-events:none}}
.phase-label.p1{{top:82px;left:{lp[0]}%}}.phase-label.p2{{top:82px;left:{lp[1]}%}}.phase-label.p3{{top:82px;left:{lp[2]}%}}.phase-label.p4{{top:82px;left:{lp[3] if len(lp)>3 else -100}%}}
.phase-divider{{position:absolute;top:var(--top-bar);bottom:0;width:1px;background:linear-gradient(to bottom,transparent,var(--border) 15%,var(--border) 85%,transparent);opacity:.6;pointer-events:none}}
.phase-divider.d1{{left:{dp[0]}%}}.phase-divider.d2{{left:{dp[1]}%}}.phase-divider.d3{{left:{dp[2]}%}}
.node{{position:absolute;width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .35s;z-index:10;transform:translate(-50%,-50%)}}
.node .ring{{position:absolute;inset:-4px;border-radius:50%;border:2px solid var(--border);transition:all .35s}}
.node .inner{{width:100%;height:100%;border-radius:50%;background:#f0f1f3;display:flex;align-items:center;justify-content:center;font-size:22px;position:relative;z-index:1;transition:all .35s;border:2px solid var(--border)}}
.node.active .ring{{border-color:var(--blue);box-shadow:0 0 20px rgba(88,166,255,.35);animation:pulse 2s infinite}}
.node.active .inner{{border-color:var(--blue);background:rgba(88,166,255,.1);transform:scale(1.12)}}
.node.complete .ring{{border-color:var(--green);box-shadow:0 0 12px rgba(63,185,80,.25)}}
.node.complete .inner{{border-color:var(--green);background:rgba(63,185,80,.15)}}
.node:hover{{transform:translate(-50%,-50%) scale(1.1)}}
.node .label{{position:absolute;top:calc(100% + 10px);white-space:nowrap;font-size:11px;font-weight:600;color:var(--text-muted);text-align:center;pointer-events:none}}
.node.active .label{{color:var(--blue)}}.node.complete .label{{color:var(--green)}}
@keyframes pulse{{0%,100%{{box-shadow:0 0 20px rgba(88,166,255,.25)}}50%{{box-shadow:0 0 32px rgba(88,166,255,.5)}}}}
.check-icon{{display:none}}.node.complete .check-icon{{display:block}}.node.complete .emoji{{display:none}}
.overlay{{position:fixed;inset:0;background:rgba(0,0,0,.2);z-index:200;opacity:0;pointer-events:none;transition:opacity .3s}}.overlay.open{{opacity:1;pointer-events:auto}}
.panel{{position:fixed;top:0;right:0;bottom:0;width:var(--panel-w);max-width:92vw;background:#f0f1f3;border-left:1px solid var(--border);z-index:210;transform:translateX(100%);transition:transform .35s;display:flex;flex-direction:column;overflow-y:auto;box-shadow:-4px 0 24px rgba(0,0,0,.08)}}.panel.open{{transform:translateX(0)}}
.panel-header{{padding:20px 24px 16px;border-bottom:1px solid var(--border);display:flex;align-items:flex-start;gap:12px}}
.panel-header .emoji-big{{font-size:32px}}.panel-header .meta{{flex:1}}.panel-header .meta h2{{font-size:18px;font-weight:700;margin-bottom:4px}}.panel-header .meta .time{{font-size:12px;color:var(--text-muted)}}
.panel-close{{background:none;border:none;color:var(--text-muted);font-size:22px;cursor:pointer}}.panel-close:hover{{color:var(--text)}}
.panel-body{{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:16px}}.panel-body .desc{{font-size:14px;line-height:1.55}}
.copy-block{{position:relative;background:#e4e6ea;border:1px solid var(--border);border-radius:8px;padding:12px 44px 12px 14px;font-family:'Cascadia Code',monospace;font-size:12.5px;line-height:1.5;white-space:pre-wrap;word-break:break-word}}
.copy-btn{{position:absolute;top:8px;right:8px;background:#d5d8dd;border:none;color:var(--text-muted);width:30px;height:30px;border-radius:6px;cursor:pointer;display:flex;align-items:center;justify-content:center}}.copy-btn:hover{{background:var(--blue);color:#fff}}.copy-btn.copied{{background:var(--green);color:#fff}}
.toggle-done{{display:flex;align-items:center;gap:10px;padding:12px 16px;border-radius:8px;border:2px solid var(--border);background:transparent;cursor:pointer;font-size:14px;font-weight:600;width:100%}}
.toggle-done .dot{{width:22px;height:22px;border-radius:50%;border:2px solid var(--border);display:flex;align-items:center;justify-content:center;flex-shrink:0}}
.toggle-done.checked{{border-color:var(--green);background:rgba(63,185,80,.08)}}.toggle-done.checked .dot{{background:var(--green);border-color:var(--green)}}
.substeps{{list-style:none;padding:0;display:flex;flex-direction:column;gap:6px}}.substeps li{{font-size:13px;color:var(--text-muted);padding-left:20px;position:relative;line-height:1.5}}.substeps li::before{{content:'';position:absolute;left:2px;top:7px;width:8px;height:8px;border-radius:50%;border:2px solid var(--border)}}
.stuck-toggle{{background:none;border:none;color:var(--orange);font-size:13px;cursor:pointer;padding:4px 0}}.stuck-toggle:hover{{text-decoration:underline}}
.stuck-content{{max-height:0;overflow:hidden;transition:max-height .3s;font-size:13px;color:var(--text-muted);line-height:1.6}}.stuck-content.open{{max-height:500px}}.stuck-content p{{margin-top:8px}}
.copy-group{{display:flex;flex-direction:column;gap:8px}}
.particle{{position:fixed;width:8px;height:8px;border-radius:50%;pointer-events:none;z-index:999}}
.confetti{{position:fixed;width:10px;height:16px;pointer-events:none;z-index:999;border-radius:2px}}
.rocket-anim{{position:fixed;font-size:40px;z-index:999;pointer-events:none}}
.banner{{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%) scale(0);background:rgba(240,241,243,.97);border:2px solid var(--green);border-radius:16px;padding:32px 56px;text-align:center;z-index:999;transition:transform .5s cubic-bezier(.175,.885,.32,1.275);box-shadow:0 12px 48px rgba(0,0,0,.15)}}.banner.show{{transform:translate(-50%,-50%) scale(1)}}.banner h1{{font-size:28px;margin-bottom:8px}}.banner p{{color:var(--text-muted);font-size:15px}}
.credit{{position:fixed;bottom:10px;left:50%;transform:translateX(-50%);font-size:11px;color:var(--text-muted);opacity:.6;pointer-events:none;z-index:5}}
</style></head><body>
<div class="top-bar"><div class="title"><span>{title}</span></div>
<div class="progress-wrap"><div class="progress-track"><div class="progress-fill" id="pf" style="width:0%"></div></div><div class="progress-label" id="pl">0 of {total}</div></div>
<button class="btn-reset" onclick="resetProgress()">Reset</button></div>
<div class="phase-label p1">{pl[0]}</div><div class="phase-label p2">{pl[1]}</div><div class="phase-label p3">{pl[2]}</div><div class="phase-label p4">{pl[3] if len(pl)>3 else ''}</div>
<div class="phase-divider d1"></div><div class="phase-divider d2"></div><div class="phase-divider d3"></div>
<div class="quest-map" id="qm"><svg id="ps" preserveAspectRatio="none"></svg></div>
<div class="overlay" id="ov" onclick="closePanel()"></div>
<div class="panel" id="pn"><div class="panel-header"><div class="emoji-big" id="pe"></div><div class="meta"><h2 id="pt"></h2><div class="time" id="ptm"></div></div><button class="panel-close" onclick="closePanel()">✕</button></div><div class="panel-body" id="pb"></div></div>
<div class="banner" id="bn"><h1>🏆 Quest Complete!</h1><p>Training finished!</p></div>
<div class="credit">{title} · Generated {timestamp} · Made by HOLO</div>
<script>
const C={cp_json};const P={pos_json};
const SK='quest-'+btoa('{title}').slice(0,12);let S=ls();
function ls(){{try{{const s=localStorage.getItem(SK);if(s)return JSON.parse(s)}}catch(e){{}}return{{c:{{}}}}}}
function ss(){{localStorage.setItem(SK,JSON.stringify(S))}}
function ic(id){{return!!S.c[id]}}function cc(){{return C.filter(c=>ic(c.id)).length}}
function render(){{rp();rn();up()}}
function up(){{const n=cc(),t=C.length;document.getElementById('pf').style.width=Math.round(n/t*100)+'%';document.getElementById('pl').textContent=n+' of '+t}}
function ai(){{for(let i=0;i<C.length;i++)if(!ic(C[i].id))return i;return C.length}}
function rp(){{const s=document.getElementById('ps'),w=window.innerWidth,h=window.innerHeight-52;s.setAttribute('viewBox','0 0 '+w+' '+h);let html='';const pts=P.map(p=>({{x:p.x/100*w,y:p.y/100*h}}));const a=ai();for(let i=0;i<pts.length-1;i++){{const p=pts[i],q=pts[i+1],cx1=p.x+(q.x-p.x)*.6,cy1=p.y,cx2=p.x+(q.x-p.x)*.4,cy2=q.y;const d='M'+p.x+','+p.y+' C'+cx1+','+cy1+' '+cx2+','+cy2+' '+q.x+','+q.y;if(ic(C[i].id)&&ic(C[i+1].id))html+='<path d="'+d+'" fill="none" stroke="var(--green)" stroke-width="3" stroke-opacity=".5"/>';else if(ic(C[i].id)||i===a-1||i===a)html+='<path d="'+d+'" fill="none" stroke="var(--blue)" stroke-width="2.5" stroke-opacity=".4" stroke-dasharray="8 6"><animate attributeName="stroke-dashoffset" from="28" to="0" dur="1.5s" repeatCount="indefinite"/></path>';else html+='<path d="'+d+'" fill="none" stroke="var(--border)" stroke-width="2" stroke-dasharray="6 8" stroke-opacity=".5"/>'}}s.innerHTML=html}}
function rn(){{document.querySelectorAll('.node').forEach(n=>n.remove());const m=document.getElementById('qm'),a=ai();C.forEach((c,i)=>{{const p=P[i];if(!p)return;const n=document.createElement('div');n.className='node';if(ic(c.id))n.classList.add('complete');else if(i===a)n.classList.add('active');n.style.left=p.x+'%';n.style.top='calc('+p.y+'% + 0px)';const l=i>a&&!ic(c.id);n.innerHTML='<div class="ring"></div><div class="inner"><span class="emoji">'+(l?'🔒':c.emoji)+'</span><svg class="check-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><polyline points="4 12 10 18 20 6"/></svg></div><div class="label">'+c.title+'</div>';n.addEventListener('click',()=>op(i));m.appendChild(n)}})}}
let cp=-1;function op(i){{cp=i;const c=C[i];document.getElementById('pe').textContent=c.emoji;document.getElementById('pt').textContent=c.title;document.getElementById('ptm').textContent=c.time?'⏱ '+c.time:'';let h='<div class="desc">'+c.desc+'</div>';if(c.substeps){{h+='<ol class="substeps">';c.substeps.forEach(s=>h+='<li>'+s+'</li>');h+='</ol>'}}if(c.copies){{h+='<div class="copy-group">';c.copies.forEach(x=>{{h+='<div><div style="font-size:12px;color:var(--text-muted);margin-bottom:4px">'+x.label+'</div><div class="copy-block">'+eh(x.text)+'<button class="copy-btn" onclick="ct(this,\\''+ea(x.text)+'\\')" title="Copy">📋</button></div></div>'}});h+='</div>'}}if(c.learn)h+='<div style="font-size:13px;color:var(--text-muted)">📚 <b>Learn:</b> '+c.learn+'</div>';const k=ic(c.id);h+='<button class="toggle-done '+(k?'checked':'')+'" onclick="td(\\''+c.id+'\\',this)"><span class="dot">'+(k?'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><polyline points="4 12 10 18 20 6"/></svg>':'')+'</span><span>'+(c.toggle||'Done ✓')+'</span></button>';if(c.stuck)h+='<div><button class="stuck-toggle" onclick="this.nextElementSibling.classList.toggle(\\'open\\')">🆘 Stuck?</button><div class="stuck-content"><p>'+c.stuck+'</p></div></div>';document.getElementById('pb').innerHTML=h;document.getElementById('ov').classList.add('open');document.getElementById('pn').classList.add('open')}}
function closePanel(){{document.getElementById('ov').classList.remove('open');document.getElementById('pn').classList.remove('open');cp=-1}}
function eh(s){{return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}}
function ea(s){{return s.replace(/\\\\/g,'\\\\\\\\').replace(/'/g,"\\\\'")}}
function ct(b,t){{navigator.clipboard.writeText(t).then(()=>{{b.classList.add('copied');b.textContent='✓';setTimeout(()=>{{b.classList.remove('copied');b.textContent='📋'}},1500)}}).catch(()=>{{const a=document.createElement('textarea');a.value=t;a.style.cssText='position:fixed;left:-9999px';document.body.appendChild(a);a.select();document.execCommand('copy');document.body.removeChild(a);b.classList.add('copied');b.textContent='✓';setTimeout(()=>{{b.classList.remove('copied');b.textContent='📋'}},1500)}})}}
function td(id,b){{if(ic(id)){{delete S.c[id];b.classList.remove('checked');b.querySelector('.dot').innerHTML=''}}else{{S.c[id]=1;b.classList.add('checked');b.querySelector('.dot').innerHTML='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><polyline points="4 12 10 18 20 6"/></svg>';cel(id)}}ss();render()}}
function cel(id){{const i=C.findIndex(c=>c.id===id),p=P[i];if(!p)return;const x=p.x/100*innerWidth,y=p.y/100*(innerHeight-52)+52;sp(x,y);const mx=Math.max(...C.map(c=>c.phase));for(let q=1;q<=mx;q++){{const ph=C.filter(c=>c.phase===q);if(ph.every(c=>ic(c.id))&&id===ph[ph.length-1].id)setTimeout(ra,400)}}if(cc()===C.length)setTimeout(()=>{{cf();sb()}},600)}}
function sp(x,y){{const co=['#58a6ff','#3fb950','#d29922','#f778ba','#bc8cff'];for(let i=0;i<12;i++){{const e=document.createElement('div');e.className='particle';e.style.left=x+'px';e.style.top=y+'px';e.style.background=co[i%5];document.body.appendChild(e);const a=Math.random()*Math.PI*2,d=40+Math.random()*60;e.animate([{{transform:'translate(0,0) scale(1)',opacity:1}},{{transform:'translate('+Math.cos(a)*d+'px,'+Math.sin(a)*d+'px) scale(0)',opacity:0}}],{{duration:600+Math.random()*400,easing:'cubic-bezier(.4,0,.2,1)'}}).onfinish=()=>e.remove()}}}}
function ra(){{const e=document.createElement('div');e.className='rocket-anim';e.textContent='🚀';e.style.left='-50px';e.style.bottom='60%';document.body.appendChild(e);e.animate([{{transform:'translate(0,0) rotate(-30deg)',opacity:1}},{{transform:'translate('+(innerWidth+100)+'px,-'+(innerHeight/2)+'px) rotate(-30deg)',opacity:.8}}],{{duration:1400,easing:'cubic-bezier(.25,.1,.25,1)'}}).onfinish=()=>e.remove()}}
function cf(){{const co=['#58a6ff','#3fb950','#d29922','#f778ba','#bc8cff','#f85149','#fff'];for(let i=0;i<60;i++){{const e=document.createElement('div');e.className='confetti';e.style.background=co[i%7];e.style.left=Math.random()*innerWidth+'px';e.style.top='-20px';e.style.width=(6+Math.random()*8)+'px';e.style.height=(10+Math.random()*12)+'px';document.body.appendChild(e);const x=(Math.random()-.5)*200,s=Math.random()*720-360;e.animate([{{transform:'rotate(0)',opacity:1}},{{transform:'translate('+x+'px,'+(innerHeight+40)+'px) rotate('+s+'deg)',opacity:.6}}],{{duration:2000+Math.random()*1500,delay:Math.random()*300}}).onfinish=()=>e.remove()}}}}
function sb(){{const b=document.getElementById('bn');b.classList.add('show');setTimeout(()=>b.classList.remove('show'),4000)}}
function resetProgress(){{if(!confirm('Reset?'))return;S={{c:{{}}}};ss();closePanel();render()}}
render();addEventListener('resize',render);
</script></body></html>"""

    # ══════════════════════════════════════════════════════════════════════
    #  Productivity Actions (paste, log, okr, kanban)
    # ══════════════════════════════════════════════════════════════════════

    def _action_paste(self, **kwargs):
        """Quick-ingest raw text (meeting notes, emails, goals) into 01-raw/."""
        content = kwargs.get("content", "").strip()
        title = kwargs.get("title", "").strip()
        if not content:
            return "❌ `content` is required. Paste the text you want to ingest."

        today = datetime.now()
        slug = _slugify(title) if title else f"paste-{today.strftime('%Y%m%d-%H%M%S')}"
        filename = f"{slug}.md"

        raw_dir = os.path.join(self.vault, "01-raw")
        os.makedirs(raw_dir, exist_ok=True)
        filepath = os.path.join(raw_dir, filename)

        md = f"---\ningested: {today.strftime('%Y-%m-%d')}\ntype: paste\ntags: [raw, paste]\n---\n# {title or 'Pasted Content'}\n\n{content}\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md)

        self._log(f"Pasted content to 01-raw/{filename}")
        return f"✅ Saved to `01-raw/{filename}` ({len(content)} chars)\n\nRun `action=compile` to integrate into the wiki."

    def _action_log(self, **kwargs):
        """Show or add to the activity log."""
        note = kwargs.get("note", "").strip()
        if note:
            self._log(note)
            return f"✅ Logged: {note}"

        log_path = os.path.join(self.vault, "log", "activity.md")
        if not os.path.isfile(log_path):
            return "📋 Activity log is empty. Actions will auto-log as you use them."

        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        recent = lines[-30:]  # last 30 entries
        return "## 📋 Activity Log (last 30 entries)\n\n" + "".join(recent)

    def _action_okr(self, **kwargs):
        """Track Goals/OKRs. Add objectives, key results, update progress."""
        name = kwargs.get("name", "").strip()
        objective = kwargs.get("objective", "").strip()
        key_result = kwargs.get("key_result", "").strip()

        if not name:
            # Team-wide OKR view
            people_dir = os.path.join(self.vault, "03-people")
            lines = ["## 🎯 Team OKRs\n"]
            if os.path.isdir(people_dir):
                for entry in sorted(os.listdir(people_dir)):
                    okr_path = os.path.join(people_dir, entry, "okr.md")
                    if os.path.isfile(okr_path):
                        with open(okr_path, "r", encoding="utf-8") as f:
                            content = f.read(2000)
                        lines.append(f"### {entry.replace('-', ' ').title()}\n{content[:500]}\n")
            if len(lines) == 1:
                lines.append("_No OKRs found. Use `action=okr, name=\"Jane Smith\", objective=\"...\"` to add one._")
            return "\n".join(lines)

        slug = _slugify(name)
        okr_path = os.path.join(self.vault, "03-people", slug, "okr.md")
        person_dir = os.path.join(self.vault, "03-people", slug)

        if not os.path.isdir(person_dir):
            return f"❌ Person `{name}` not found. Add them first with `action=add_person`."

        # If adding an objective
        if objective:
            if not os.path.isfile(okr_path):
                header = f"---\nperson: {name}\nupdated: {datetime.now().strftime('%Y-%m-%d')}\ntags: [okr]\n---\n# OKRs — {name}\n\n"
                with open(okr_path, "w", encoding="utf-8") as f:
                    f.write(header)

            with open(okr_path, "a", encoding="utf-8") as f:
                f.write(f"\n## 🎯 {objective}\n")
                if key_result:
                    f.write(f"- [ ] {key_result}\n")

            self._log(f"Added OKR for {name}: {objective}")
            return f"✅ Added objective for **{name}**: {objective}" + (f"\n  Key result: {key_result}" if key_result else "\n  Add key results with `key_result=\"...\"`")

        # If adding a key result to existing
        if key_result:
            if not os.path.isfile(okr_path):
                return f"❌ No OKRs found for {name}. Add an objective first with `objective=\"...\"`"
            with open(okr_path, "a", encoding="utf-8") as f:
                f.write(f"- [ ] {key_result}\n")
            self._log(f"Added key result for {name}: {key_result}")
            return f"✅ Added key result for **{name}**: {key_result}"

        # Show existing OKRs
        if os.path.isfile(okr_path):
            with open(okr_path, "r", encoding="utf-8") as f:
                return f.read()
        return f"No OKRs for {name} yet. Add one with `objective=\"...\"`"

    def _action_kanban(self, **kwargs):
        """Generate a Kanban board from a person's priorities (Obsidian Kanban plugin format)."""
        name = kwargs.get("name", "").strip()
        if not name:
            return "❌ `name` is required. Example: `action=kanban, name=\"Jane Smith\"`"

        slug = _slugify(name)
        prio_path = os.path.join(self.vault, "03-people", slug, "priorities.md")

        if not os.path.isfile(prio_path):
            return f"❌ No priorities found for {name}."

        with open(prio_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Parse NOW/NEXT/LATER sections
        now_items, next_items, later_items, done_items = [], [], [], []
        current_section = None
        for line in content.splitlines():
            line_stripped = line.strip()
            if "## 🔴 NOW" in line or "## NOW" in line.upper():
                current_section = "now"
            elif "## 🟡 NEXT" in line or "## NEXT" in line.upper():
                current_section = "next"
            elif "## 🟢 LATER" in line or "## LATER" in line.upper():
                current_section = "later"
            elif "## ✅ COMPLETED" in line or "## COMPLETED" in line.upper() or "## DONE" in line.upper():
                current_section = "done"
            elif line_stripped.startswith("- [") and current_section:
                task = line_stripped.lstrip("- [x] ").lstrip("- [ ] ").strip()
                if task:
                    is_done = "[x]" in line_stripped
                    if is_done or current_section == "done":
                        done_items.append(task)
                    elif current_section == "now":
                        now_items.append(task)
                    elif current_section == "next":
                        next_items.append(task)
                    elif current_section == "later":
                        later_items.append(task)

        # Build Obsidian Kanban format
        kanban_md = f"---\nkanban-plugin: basic\n---\n\n## 🔴 Now\n\n"
        for item in now_items:
            kanban_md += f"- [ ] {item}\n"
        kanban_md += f"\n## 🟡 Next\n\n"
        for item in next_items:
            kanban_md += f"- [ ] {item}\n"
        kanban_md += f"\n## 🟢 Later\n\n"
        for item in later_items:
            kanban_md += f"- [ ] {item}\n"
        kanban_md += f"\n## ✅ Done\n\n"
        for item in done_items:
            kanban_md += f"- [x] {item}\n"
        kanban_md += "\n%% kanban:settings\n```\n{\"kanban-plugin\":\"basic\"}\n```\n%%\n"

        # Save kanban board
        kanban_path = os.path.join(self.vault, "03-people", slug, "kanban.md")
        with open(kanban_path, "w", encoding="utf-8") as f:
            f.write(kanban_md)

        total = len(now_items) + len(next_items) + len(later_items) + len(done_items)
        self._log(f"Generated kanban board for {name} ({total} items)")
        return (
            f"✅ Kanban board generated for **{name}**\n\n"
            f"**File:** `03-people/{slug}/kanban.md`\n"
            f"- 🔴 Now: {len(now_items)} items\n"
            f"- 🟡 Next: {len(next_items)} items\n"
            f"- 🟢 Later: {len(later_items)} items\n"
            f"- ✅ Done: {len(done_items)} items\n\n"
            f"Open in Obsidian — it renders as a drag-and-drop Kanban board with the Kanban plugin."
        )

    # ── morning_brief ─────────────────────────────────────────────────────

    def _job_morning_brief(self, cfg):
        """Generate a morning brief: per-person status, overdue items, milestones."""
        today = _today()
        people = _load_active_people(self.vault)

        lines = [
            f"# ☀️ Morning Brief — {today.strftime('%A, %B %d, %Y')}",
            "",
            f"> Generated by ObsidianPilot at {datetime.now().strftime('%H:%M')}",
            "",
        ]

        if not people:
            lines.append("_No active people in the vault. Use add_person to add someone._")
            brief_text = "\n".join(lines)
            self._save_brief(today, brief_text)
            return brief_text

        total_overdue = 0
        total_upcoming = 0
        people_needing_checkin = []
        all_alerts = []

        lines.append(f"## 👥 Team Overview ({len(people)} active)")
        lines.append("")
        lines.append("| Status | Name | Day | Phase | Overdue | NOW Items |")
        lines.append("|--------|------|-----|-------|---------|-----------|")

        person_sections = []

        for person in people:
            try:
                section = self._brief_person(person, today)
                person_sections.append(section)

                status = section["status"]
                overdue_count = len(section["overdue"])
                now_count = len(section["now_items"])
                total_overdue += overdue_count
                total_upcoming += len(section["upcoming"])

                lines.append(
                    f"| {status} | {section['name']} | {section['day']} "
                    f"| {section['phase']} | {overdue_count} | {now_count} |"
                )

                if overdue_count > 0 or now_count == 0:
                    people_needing_checkin.append(section["name"])

                if section.get("phase_alert"):
                    all_alerts.append(section["phase_alert"])

            except Exception as e:
                lines.append(
                    f"| ⚠️ | {person.get('name', '?')} "
                    f"| — | — | — | Error: {e} |"
                )

        lines.append("")

        if people_needing_checkin:
            lines.append(f"## 🔔 Needs Check-in ({len(people_needing_checkin)})")
            lines.append("")
            for pname in people_needing_checkin:
                lines.append(f"- **{pname}**")
            lines.append("")

        if all_alerts:
            lines.append(f"## 🚨 Phase Alerts")
            lines.append("")
            for alert in all_alerts:
                lines.append(f"- {alert}")
            lines.append("")

        overdue_details = []
        for section in person_sections:
            for item in section.get("overdue", []):
                overdue_details.append(
                    f"- **{section['name']}** — {item}"
                )

        if overdue_details:
            lines.append(f"## ⏰ Overdue Items ({len(overdue_details)})")
            lines.append("")
            lines.extend(overdue_details[:20])
            if len(overdue_details) > 20:
                lines.append(f"_...and {len(overdue_details) - 20} more_")
            lines.append("")

        upcoming_details = []
        for section in person_sections:
            for item in section.get("upcoming", []):
                upcoming_details.append(
                    f"- **{section['name']}** — {item}"
                )

        if upcoming_details:
            lines.append(f"## 📅 Upcoming This Week ({len(upcoming_details)})")
            lines.append("")
            lines.extend(upcoming_details[:15])
            if len(upcoming_details) > 15:
                lines.append(f"_...and {len(upcoming_details) - 15} more_")
            lines.append("")

        lines.append("---")
        lines.append("")
        for section in person_sections:
            lines.extend(self._brief_person_detail(section))
            lines.append("")

        lines.append("---")
        lines.append(
            f"_Brief complete: {len(people)} people, "
            f"{total_overdue} overdue, {total_upcoming} upcoming this week._"
        )

        brief_text = "\n".join(lines)
        output_path = self._save_brief(today, brief_text)
        brief_text += f"\n\n📄 _Saved to `{os.path.basename(output_path)}`_"
        return brief_text

    def _brief_person(self, person, today):
        """Gather brief data for a single person. Returns a dict."""
        name = person.get("name", "?")
        person_dir = person.get("dir", "")
        start_date = person.get("start_date", "")
        days = _day_count(start_date)
        phase = _phase_label(days)
        status = _status_indicator(person_dir)
        active_file = _phase_file(days)

        plan_text = _safe_read(os.path.join(person_dir, active_file))
        done_plan, total_plan = _count_tasks(plan_text)

        pri_text = _safe_read(os.path.join(person_dir, "priorities.md"))
        now_items = _extract_section_items(pri_text, "NOW")

        overdue = []
        for fname in ["30-day.md", "60-day.md", "90-day.md", "priorities.md"]:
            text = _safe_read(os.path.join(person_dir, fname))
            for m in re.finditer(r"- \[ \] (.+)", text):
                item = m.group(1)
                dm = re.search(r"\d{4}-\d{2}-\d{2}", item)
                if dm:
                    due = _parse_date(dm.group())
                    if due and due < today:
                        overdue.append(f"{item.strip()} (from {fname})")

        upcoming = []
        for fname in ["30-day.md", "60-day.md", "90-day.md", "priorities.md"]:
            text = _safe_read(os.path.join(person_dir, fname))
            for m in re.finditer(r"- \[ \] (.+)", text):
                item = m.group(1)
                dm = re.search(r"\d{4}-\d{2}-\d{2}", item)
                if dm:
                    due = _parse_date(dm.group())
                    if due and today <= due:
                        delta = (due - today).days
                        if delta <= 7:
                            upcoming.append(f"{item.strip()} (due in {delta}d)")

        phase_alert = None
        for boundary in [30, 60, 90]:
            if days < boundary <= days + 7:
                days_until = boundary - days
                phase_alert = (
                    f"**{name}** crosses day {boundary} in {days_until} day(s) "
                    f"(currently day {days})"
                )
                break

        return {
            "name": name,
            "slug": person.get("slug", ""),
            "role": person.get("role", ""),
            "day": str(days),
            "days": days,
            "phase": phase,
            "status": status,
            "active_file": active_file,
            "done_plan": done_plan,
            "total_plan": total_plan,
            "now_items": now_items,
            "overdue": overdue,
            "upcoming": upcoming,
            "phase_alert": phase_alert,
        }

    def _brief_person_detail(self, section):
        """Render per-person detail section for the brief."""
        lines = [
            f"### {section['status']} {section['name']}",
            f"_{section.get('role', '')}_ — Day {section['day']}, {section['phase']}",
            "",
        ]

        done = section["done_plan"]
        total = section["total_plan"]
        if total > 0:
            pct = int(done / total * 100)
            bar = "█" * (pct // 10) + "░" * (10 - pct // 10)
            lines.append(
                f"**{section['active_file']}:** {bar} {done}/{total} ({pct}%)"
            )
        else:
            lines.append(f"**{section['active_file']}:** No tasks defined")
        lines.append("")

        if section["now_items"]:
            lines.append(f"**NOW priorities ({len(section['now_items'])}):**")
            for item in section["now_items"][:5]:
                lines.append(f"  - {item}")
            lines.append("")

        return lines

    def _save_brief(self, today, content):
        """Save brief to 04-output/ and return path."""
        output_dir = os.path.join(self.vault, "04-output")
        os.makedirs(output_dir, exist_ok=True)
        filename = f"morning-brief-{today.isoformat()}.md"
        path = os.path.join(output_dir, filename)
        _safe_write(path, content)
        return path

    # ── content_watch ─────────────────────────────────────────────────────

    def _job_content_watch(self, cfg):
        """Check watched URLs for new content."""
        urls = cfg.get("watched_urls", [])
        if not urls:
            return "📡 **Content Watch** — No URLs configured. Use `watch` to add some."

        results = []
        changed_count = 0
        error_count = 0

        for entry in urls:
            if not entry.get("enabled", True):
                continue
            url = entry.get("url", "")
            if not url:
                continue

            try:
                body, new_etag, new_last_modified = self._fetch_url(
                    url,
                    etag=entry.get("etag", ""),
                    last_modified=entry.get("last_modified", ""),
                )
                entry["last_checked"] = _now_iso()

                if body is None:
                    results.append(f"  ✅ `{url[:60]}` — unchanged (304)")
                    continue

                normalized = re.sub(r"\s+", " ", body).strip()
                new_hash = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
                old_hash = entry.get("sha256", "")

                if new_hash == old_hash:
                    results.append(f"  ✅ `{url[:60]}` — unchanged")
                    continue

                entry["sha256"] = new_hash
                entry["etag"] = new_etag
                entry["last_modified"] = new_last_modified
                entry["last_changed"] = _now_iso()
                entry["last_error"] = ""
                changed_count += 1

                slug = _slugify(url.split("//")[-1].split("?")[0][:50])
                url_hash = hashlib.sha256(url.encode()).hexdigest()[:8]
                filename = f"watch-{slug}-{url_hash}.md"
                raw_path = os.path.join(self.vault, "01-raw", filename)

                content = (
                    f"---\n"
                    f"source: {url}\n"
                    f"fetched: {_now_iso()}\n"
                    f"sha256: {new_hash[:16]}\n"
                    f"type: content_watch\n"
                    f"---\n\n"
                    f"# Content from {url}\n\n"
                    f"{body[:50000]}\n"
                )
                _safe_write(raw_path, content)
                results.append(
                    f"  🆕 `{url[:60]}` — **changed** → `01-raw/{filename}`"
                )

            except Exception as e:
                entry["last_checked"] = _now_iso()
                entry["last_error"] = str(e)
                error_count += 1
                results.append(f"  ❌ `{url[:60]}` — error: {e}")

        _save_config(self.vault, cfg)

        active = [u for u in urls if u.get("enabled", True)]
        header = (
            f"# 📡 Content Watch Results\n\n"
            f"Checked {len(active)} URL(s) — "
            f"**{changed_count} changed**, {error_count} errors\n"
        )
        return header + "\n".join(results)

    def _fetch_url(self, url, etag="", last_modified=""):
        """Fetch a URL with conditional GET. Returns (body, etag, last_modified) or (None, ...) for 304."""
        req = urllib.request.Request(url)
        req.add_header("User-Agent", _USER_AGENT)
        if etag:
            req.add_header("If-None-Match", etag)
        if last_modified:
            req.add_header("If-Modified-Since", last_modified)

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                content_type = resp.headers.get("Content-Type", "")
                if "text" not in content_type and "json" not in content_type:
                    raise ValueError(f"Skipping non-text content: {content_type}")

                body = resp.read(1_048_576).decode("utf-8", errors="replace")
                new_etag = resp.headers.get("ETag", "")
                new_lm = resp.headers.get("Last-Modified", "")
                return body, new_etag, new_lm

        except urllib.error.HTTPError as e:
            if e.code == 304:
                return None, etag, last_modified
            raise

    # ── auto_review ───────────────────────────────────────────────────────

    def _job_auto_review(self, cfg):
        """For each active person, draft a weekly review from recent activity."""
        people = _load_active_people(self.vault)
        if not people:
            return "📝 **Auto Review** — No active people in vault."

        today = _today()
        cutoff = today.toordinal() - 7
        reviews = []

        for person in people:
            try:
                name = person.get("name", "?")
                person_dir = person.get("dir", "")
                weekly_dir = os.path.join(person_dir, "weekly")

                recent_notes = []
                if os.path.isdir(weekly_dir):
                    for fname in sorted(os.listdir(weekly_dir), reverse=True):
                        if not fname.endswith(".md"):
                            continue
                        date_match = re.search(r"(\d{4}-\d{2}-\d{2})", fname)
                        if date_match:
                            note_date = _parse_date(date_match.group(1))
                            if note_date and note_date.toordinal() >= cutoff:
                                text = _safe_read(os.path.join(weekly_dir, fname))
                                recent_notes.append((note_date, fname, text))

                modified_files = []
                for fname in os.listdir(person_dir):
                    fpath = os.path.join(person_dir, fname)
                    if not os.path.isfile(fpath) or not fname.endswith(".md"):
                        continue
                    try:
                        mtime = date.fromtimestamp(os.path.getmtime(fpath))
                        if mtime.toordinal() >= cutoff:
                            modified_files.append(fname)
                    except OSError:
                        pass

                completed = []
                for fname in ["30-day.md", "60-day.md", "90-day.md", "priorities.md"]:
                    text = _safe_read(os.path.join(person_dir, fname))
                    for m in re.finditer(r"- \[x\] (.+)", text, re.IGNORECASE):
                        completed.append(m.group(1).strip())

                days = _day_count(person.get("start_date", ""))
                phase = _phase_label(days)

                review_lines = [
                    f"### {name}",
                    f"_Day {days}, {phase}_",
                    "",
                ]

                if recent_notes:
                    review_lines.append(
                        f"**Weekly notes:** {len(recent_notes)} entries"
                    )
                    for nd, nf, nt in recent_notes[:3]:
                        preview_lines = [
                            ln.strip() for ln in nt.split("\n")
                            if ln.strip() and not ln.strip().startswith("#")
                        ]
                        preview = " ".join(preview_lines[:2])[:150]
                        review_lines.append(f"- {nd}: {preview}")
                    review_lines.append("")

                if completed:
                    review_lines.append(
                        f"**Completed tasks:** {len(completed)}"
                    )
                    for task_item in completed[:5]:
                        review_lines.append(f"- ✅ {task_item}")
                    review_lines.append("")

                if modified_files:
                    review_lines.append(
                        f"**Modified files:** {', '.join(modified_files)}"
                    )
                    review_lines.append("")

                if not recent_notes and not completed and not modified_files:
                    review_lines.append("_No activity detected this week._")
                    review_lines.append("")

                reviews.append("\n".join(review_lines))

            except Exception as e:
                reviews.append(f"### {person.get('name', '?')}\n\n_Error: {e}_\n")

        header = (
            f"# 📝 Auto Review — Week of {today.isoformat()}\n\n"
            f"{len(people)} people reviewed\n\n"
        )
        return header + "\n".join(reviews)

    # ── wiki_health (job version) ─────────────────────────────────────────

    def _job_wiki_health(self, cfg):
        """Scan 02-wiki/ for stale, orphaned, or broken articles."""
        wiki_dir = os.path.join(self.vault, "02-wiki")
        all_files = _collect_md_files(self.vault)
        wiki_files = _collect_md_files(wiki_dir)

        issues = []
        all_titles = set()
        all_links = set()
        link_targets = {}

        for fpath in all_files:
            text = _safe_read(fpath)
            basename = os.path.splitext(os.path.basename(fpath))[0]
            all_titles.add(basename.lower())

            for m in re.finditer(r"\[\[([^\]|#]+)(?:[|#][^\]]+)?\]\]", text):
                target = m.group(1).strip().lower()
                all_links.add(target)
                link_targets.setdefault(target, []).append(
                    os.path.basename(fpath)
                )

        stale_threshold = 30
        for fpath in wiki_files:
            try:
                mtime = os.path.getmtime(fpath)
                age_days = (_today() - date.fromtimestamp(mtime)).days
                if age_days > stale_threshold:
                    issues.append(
                        f"📅 Stale: `{os.path.basename(fpath)}` — "
                        f"last modified {age_days} days ago"
                    )
            except OSError:
                pass

        for fpath in wiki_files:
            basename = os.path.splitext(os.path.basename(fpath))[0]
            if basename.startswith("_"):
                continue
            if basename.lower() not in all_links:
                issues.append(
                    f"🏝️ Orphaned: `{basename}.md` — no incoming links"
                )

        broken = all_links - all_titles
        for b in sorted(broken):
            sources = link_targets.get(b, [])
            issues.append(
                f"🔗 Missing: `[[{b}]]` — referenced from: "
                f"{', '.join(sources[:3])}"
            )

        index_path = os.path.join(wiki_dir, "_index.md")
        if wiki_files and not os.path.isfile(index_path):
            issues.append("📋 Missing: `02-wiki/_index.md` — run compile action")
        elif os.path.isfile(index_path):
            index_text = _safe_read(index_path)
            index_refs = set(
                m.group(1).strip().lower()
                for m in re.finditer(r"\[\[([^\]|#]+)", index_text)
            )
            wiki_basenames = {
                os.path.splitext(os.path.basename(f))[0].lower()
                for f in wiki_files
                if not os.path.basename(f).startswith("_")
            }
            not_indexed = wiki_basenames - index_refs
            for idx_name in sorted(not_indexed):
                issues.append(f"📋 Not indexed: `{idx_name}.md` missing from _index.md")

        if not issues:
            return (
                f"✅ **Wiki Health: All Clear**\n\n"
                f"- {len(all_files)} files scanned\n"
                f"- {len(wiki_files)} wiki articles\n"
                f"- {len(all_links)} wikilinks checked\n"
                f"- No issues found"
            )

        lines = [
            f"# 🏥 Wiki Health Check",
            f"Scanned {len(all_files)} files, {len(wiki_files)} wiki articles, "
            f"{len(all_links)} wikilinks",
            "",
            f"## Issues ({len(issues)})",
            "",
        ]
        lines.extend(issues)
        return "\n".join(lines)

    # ── phase_alert ───────────────────────────────────────────────────────

    def _job_phase_alert(self, cfg):
        """Check for 30/60/90 day boundary crossings this week."""
        people = _load_active_people(self.vault)
        if not people:
            return "📊 **Phase Alert** — No active people in vault."

        today = _today()
        alerts = []

        for person in people:
            pname = person.get("name", "?")
            days = _day_count(person.get("start_date", ""))

            for boundary in [30, 60, 90]:
                if days < boundary <= days + 7:
                    days_until = boundary - days
                    phase_from = _phase_label(days)
                    phase_to = _phase_label(boundary)
                    alerts.append(
                        f"- 🚨 **{pname}** — day {days} → crosses **day {boundary}** "
                        f"in {days_until}d ({phase_from} → {phase_to})"
                    )
                elif days == boundary:
                    alerts.append(
                        f"- 🎯 **{pname}** — at **day {boundary}** today! "
                        f"Now entering {_phase_label(boundary)}"
                    )

        if not alerts:
            return (
                f"✅ **Phase Alert** — No boundary crossings this week.\n\n"
                f"_{len(people)} people checked._"
            )

        return (
            f"# 🚨 Phase Alerts — {today.isoformat()}\n\n"
            + "\n".join(alerts)
            + f"\n\n_{len(people)} people checked, {len(alerts)} alert(s)._"
        )

    # ── digest ────────────────────────────────────────────────────────────

    def _job_digest(self, cfg):
        """Scan vault for files modified since last digest, summarise changes."""
        last_digest = cfg.get("last_digest_at")
        if last_digest:
            try:
                cutoff_dt = datetime.fromisoformat(last_digest)
                cutoff_ts = cutoff_dt.timestamp()
            except (ValueError, TypeError):
                cutoff_ts = 0
        else:
            cutoff_ts = 0

        all_files = _collect_md_files(self.vault)
        modified = []

        for fpath in all_files:
            try:
                mtime = os.path.getmtime(fpath)
                if mtime > cutoff_ts:
                    rel = os.path.relpath(fpath, self.vault)
                    size = os.path.getsize(fpath)
                    modified.append((mtime, rel, size))
            except OSError:
                pass

        modified.sort(key=lambda x: x[0], reverse=True)

        cfg["last_digest_at"] = _now_iso()

        if not modified:
            period = f"since {last_digest[:19]}" if last_digest else "ever"
            return f"✅ **Vault Digest** — No changes {period}."

        by_dir = {}
        for mtime, rel, size in modified:
            parts = rel.replace("\\", "/").split("/")
            top_dir = parts[0] if len(parts) > 1 else "root"
            by_dir.setdefault(top_dir, []).append((mtime, rel, size))

        period_start = last_digest[:19] if last_digest else "beginning"
        lines = [
            f"# 📊 Vault Digest",
            f"_Changes since {period_start}_",
            "",
            f"**{len(modified)} file(s) modified** across "
            f"{len(by_dir)} area(s)",
            "",
        ]

        for dir_name in sorted(by_dir.keys()):
            files = by_dir[dir_name]
            lines.append(f"## {dir_name}/ ({len(files)} files)")
            for mtime, rel, size in files[:10]:
                mdate = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
                size_kb = f"{size / 1024:.1f}KB" if size >= 1024 else f"{size}B"
                lines.append(f"- `{rel}` — {mdate} ({size_kb})")
            if len(files) > 10:
                lines.append(f"  _...and {len(files) - 10} more_")
            lines.append("")

        return "\n".join(lines)
