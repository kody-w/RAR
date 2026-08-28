---
name: "rar-howardh-vaultmind"
description: "Obsidian vault manager for multi-person 30-60-90 day plans, LLM knowledge bases, and scheduled automation. People: add_person, roster, check_in, retire, assign, priorities, metrics, plan. Reporting: report (HTML dashboard), dashboard (text summary), review (weekly). Wiki: compile, ingest, health, query. Productivity: paste (quick raw-text ingest), log (activity log), okr (objectives & key results), kanban (generate Kanban board). Automation: brief (morning digest), watch (URL monitor), job_status (show scheduled jobs), run_job (trigger a job), setup (configure jobs), pause (toggle job)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/vaultmind_agent", "rar_sha256": "e669b4fb17fde143672f311dd544159d611928b298587a90f03f5f9f068eaafe", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Howard Hoy", "tags": ["obsidian", "30-60-90", "onboarding", "wiki", "knowledge-base", "vault", "automation", "scheduling", "monitoring"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@howardh/vaultmind_agent`. The original RAPP
agent is preserved byte-for-byte in `vaultmind_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "add_person=create a new person's 30-60-90 folder, roster=list all people, check_in=status for one person, retire=archive a person, assign=add a priority task, priorities=show priority board, metrics=person metrics, report=generate HTML dashboard, dashboard=quick text summary, compile=rebuild wiki from raw sources, ingest=add content to vault, health=wiki lint check, query=search wiki, review=weekly review, plan=personal 30-60-90 status, brief=generate morning digest, watch=add/list monitored URLs, job_status=show all scheduled jobs, run_job=manually trigger a job, setup=configure scheduled jobs, pause=pause or resume a job, bootstrap=create vault structure + install Obsidian plugins automatically, training=read a person's learning objectives and design a training quest, build_quest=render training quest HTML from checkpoint JSON, paste=quick-ingest raw text into 01-raw, log=show or add to activity log, okr=track objectives and key results per person, kanban=generate Kanban board from priorities",
      "enum": [
        "add_person",
        "roster",
        "check_in",
        "retire",
        "assign",
        "priorities",
        "metrics",
        "report",
        "dashboard",
        "compile",
        "ingest",
        "health",
        "query",
        "review",
        "plan",
        "brief",
        "watch",
        "job_status",
        "run_job",
        "setup",
        "pause",
        "bootstrap",
        "training",
        "build_quest",
        "paste",
        "log",
        "okr",
        "kanban"
      ],
      "type": "string"
    },
    "checkpoints": {
      "description": "JSON array of checkpoint objects for build_quest action",
      "type": "string"
    },
    "content": {
      "description": "Raw text content for paste action",
      "type": "string"
    },
    "context": {
      "description": "Additional context for add_person",
      "type": "string"
    },
    "enabled": {
      "description": "Enable (true) or disable (false) a job in setup",
      "type": "boolean"
    },
    "job": {
      "description": "Job name for run_job/pause/setup actions: morning_brief, content_watch, auto_review, wiki_health, phase_alert, digest",
      "enum": [
        "morning_brief",
        "content_watch",
        "auto_review",
        "wiki_health",
        "phase_alert",
        "digest"
      ],
      "type": "string"
    },
    "key_result": {
      "description": "Key result text for okr action",
      "type": "string"
    },
    "manager": {
      "description": "Manager name for add_person",
      "type": "string"
    },
    "name": {
      "description": "Person name for people actions",
      "type": "string"
    },
    "note": {
      "description": "Manual note for log action",
      "type": "string"
    },
    "objective": {
      "description": "Objective text for okr action",
      "type": "string"
    },
    "priority": {
      "description": "now/next/later for assign action",
      "type": "string"
    },
    "role": {
      "description": "Role/title for add_person",
      "type": "string"
    },
    "start_date": {
      "description": "Start date YYYY-MM-DD for add_person",
      "type": "string"
    },
    "task": {
      "description": "Task description for assign action",
      "type": "string"
    },
    "title": {
      "description": "Title for paste action",
      "type": "string"
    },
    "topic": {
      "description": "Topic for query action",
      "type": "string"
    },
    "url": {
      "description": "URL for ingest or watch actions",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vaultmind_agent.py` and embedded as the fenced Python below (sha256 e669b4fb17fde143…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vaultmind_agent.py` first:

```bash
python3 vaultmind_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vaultmind_agent.py   # or on stdin
python3 vaultmind_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
    "name": "@howardh/vaultmind_agent",
    "version": "1.0.1",
    "display_name": "VaultMind",
    "description": (
        "Manages an Obsidian vault through 28 actions \u2014 30-60-90 plans, OKRs, Kanban boards, dashboards, briefs, wiki ingestion, and health checks."
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
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
