---
name: "rar-howardh-vaultmind"
description: "Obsidian vault manager for multi-person 30-60-90 day plans, LLM knowledge bases, and scheduled automation. People: add_person, roster, check_in, retire, assign, priorities, metrics, plan. Reporting: report (HTML dashboard), dashboard (text summary), review (weekly). Wiki: compile, ingest, health, query. Productivity: paste (quick raw-text ingest), log (activity log), okr (objectives & key results), kanban (generate Kanban board). Automation: brief (morning digest), watch (URL monitor), job_status (show scheduled jobs), run_job (trigger a job), setup (configure jobs), pause (toggle job)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/vaultmind_agent", "rar_sha256": "6e2af2a79f6dcb1ba6fbf2ea9331d5f8a571b9842efa39727f4605333a3a846a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Howard Hoy", "tags": ["obsidian", "30-60-90", "onboarding", "wiki", "knowledge-base", "vault", "automation", "scheduling", "monitoring"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vaultmind_agent.py` and embedded as the fenced Python below (sha256 6e2af2a79f6dcb1b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vaultmind_agent.py` first:

```bash
python3 vaultmind_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vaultmind_agent.py   # or on stdin
python3 vaultmind_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@howardh/vaultmind_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/vaultmind_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@howardh/vaultmind_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
