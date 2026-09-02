---
name: "rar-howardh-vaultmind"
description: "Obsidian vault manager for multi-person 30-60-90 day plans, LLM knowledge bases, and scheduled automation. People: add_person, roster, check_in, retire, assign, priorities, metrics, plan. Reporting: report (HTML dashboard), dashboard (text summary), review (weekly). Wiki: compile, ingest, health, query. Productivity: paste (quick raw-text ingest), log (activity log), okr (objectives & key results), kanban (generate Kanban board). Automation: brief (morning digest), watch (URL monitor), job_status (show scheduled jobs), run_job (trigger a job), setup (configure jobs), pause (toggle job)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/vaultmind_agent", "rar_sha256": "e669b4fb17fde143672f311dd544159d611928b298587a90f03f5f9f068eaafe", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "vaultmind_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@howardh/vaultmind:8630f062c7661102f57aaec3045b281ae541bcd7c8a0516cce945963d5572aa7", "kind": "skill"}, "version": "1.0.1", "author": "Howard Hoy", "tags": ["obsidian", "30-60-90", "onboarding", "wiki", "knowledge-base", "vault", "automation", "scheduling", "monitoring"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@howardh/vaultmind_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `vaultmind_agent.py` is
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/4y8d9erVtIv+FW0zl1r2n2xTRQCz3hmyEKABCIoXN/lJoPISYSe/u6zkZ4T7ON+337+OEI71K5d8VeF1vnnJ3fok6r99MunfTW6bbDZV/OnHz8FYee3ad2nVQmmTl6XBqlbbp7ukPebwi3dOGw3UdVuCjCQ/lSHbVeVGxz5iUR+opFN4M6bOnfL7seNqmqbrKzGPAzicOO5XQgG3TLYdH4SBgMY3gAWqsJdz/p5o4dVnYe/bNwg+P1N9cdNW3V92P64ARv87Pd0HQn7tA0Bna5LY/C9btOqTft0pV2EfZv64GFl4OfNOayrtk/L+Bewa33c/LC3NBWw2CVeBW789x+/Pm9+6MOp33RDUbjt/Pf1oGcajpsfxjDM8vnvP28uaZb+svGrok5zwACgG3b9j5skdPM++XHTDGE7g1u0VTD4ffpM+/mXTe0C/jc/NEPqZ5vWHX96HfLeCs7Iq3jzg/uxev0Gxqqs3fxQeY9wHQ67zf+xycIZcNMBcXdgPnNLD+jjhzgsw9YF1JX3wPtGP2+YLyL9ZeO1aRhtfiiqtgRnboL049zR7f1k84N9VjdFVaZ91YLBR+X93vVuP3SbH7qkGr9RE5haj26H8nfwCETVpvFqBu46Aya6sB/qzQ9+VUZpPLTh5w21O3Tg+n0Vx/lr8O8/AwsLJ7cAmu4+/fK//vePn1Lw/OmXf37yc6DSbyxOT/OqZ8Ate7AF6DMGc/UMLLYE34F9ABMswFAALvjx7YcuzKMfN//zf2bAnOPu77/8Vm4+/lYZAyv9dfOe+jkO+x9++/Qe/e3Tj5vfPn0xhN8+/f3rviDt6pesft388+vo+vc/Puz1g3T3x1lA+4sV//bpl83K2c+/v5f+/o2B/3nX296/2/HhBn9e/dkrvlv/xV2+o//ynu/pv53quzu8fOx7/t+u9+fVXz3xux3fOOmfd3347HdbPvvyd6cAU/iePhj88c/6+eL+/05F76DwF8JYh787+BsD+dOGLzN/Ie41hvzFCevwdwyvAebf8foRdr7X9Ec4+vP6d4j5bvlH0Prz6ncM+271R2j78+pXpPtu8Wv0uzt9jUafb7b5IWqrYmMCx07LMP/7n6m/YtZ31F+j33HyimPfrX2Nfrf2a3j7bsPXqe81+A5536vwPf7d+lck/G71a/R7U16j4/e2vI5+t9arqr7rW/d72l9mvtsDBtM17n+35fPE96cMaR6smvwL0/lm7jstf5v0/p0Fv1LhX9wWjH7HB8iE360EY9+tA7nyu3Vg7Lt175z53dL38Der//X1MQFAJQcp7tcvOeCVNN47vzHaNNqUVf95+S9/PBnE1aEtN8CcfxuwHeFv7HIFRJ99YfOPf74f/vWPnzeOm6fBL5t//u3Hzd9+flRp+cOXgwEA6H74+9//Bch8Id+3818f9sHJD1/S4NdV4eSHdb8RXh8vl+w24X/HstC2AOyl3zILuAwBMyAPdzNQXwGiULkCm490/MfBV1b+Nhe/keSvb1W8vnydA7Dh9yBdpV51P4PLJ29JvFatWfrn6gMd/CFLf+jg85a0AyR++CD19w3g/o+zEQiYP/yB/sfaH9+BthgAJJp/qvMhTsvu58crh//9738tqB/+OPq2t//rDyDm//7tt/Jb1X1dZyXh5k8IOwE6Wdn1wnDFdB++XQMQNof9z5tTuZmrod2I8tm0VlRYA1cLN39Nvq82PTgBxJN2BcflS+d94vYrjY0Pzlzx909v9AZWAsH/iZsx7ZPNhyD+zSEroP8M/N6B3psB7TxfM+8f5PBh9b9+udXPGxNUC10Fcn2yrs7TDOD/vz7mb/KLYcDrBjD7ksFf8QrOfd0ZANSk/8L59zz+m7t8ZKuVfYDlL24JSp5wA+QI4v1Xbfw/f/u3Gv2/4D+p/k+rvrHaDwM6VmX46V8AB5eA9vCOncCR/sf/2GipD4BfFfUb06+GfuWhT4sQHF1aSdptrGoNnsHmH6Yiq+rPRfCPDRhdbw+88CUSCQT6HJRI1auaANeuos0//t/kVe4l8EtsRVoGv7srzAYxCNjjbyVAakBobr45M7q+eU2tdF+YEpRHP722gWPT8nXWmVs1U4PyJPw/N//4E82f63ll6rcSXBbkHLALRAYAr9w2zec1/LjAWvrwJ1AS+OCCVZ57LqiU1n+G+uf1ppcE+MH7/qv+wyn0B1D05BXQ0Wb15G4t1boqfwI9rVLpshTYAPBmcOWqnV+6B5L7ZSX2j3/8A5ShyW/lu5DAN+9St4PXdP6Z4c1PP9VtGOWrBf1Whn5Sbf72z3/9bfP/bf6rXS/i6xk6gMdvEwToaXMwT8cNCMPD6n7dZlVy6AYvPfzzX2+Jr9yBUm7zDNs0AhB53QyofVXqeoO3Gj7rYC1xAYughnif9Ee5bcYEyGWT9kBaadevoGYlUYGl7ZiCaPEhxPfmt+g/K/V9zqqT7kOGQE8vwLaufdnTqky/aoOfN3K0+SKpjxJ71WgCqhVggnVYBmHpz++I80WFa3DrgI910fzjGpp+K1fK//BWTPLOG2D5PzYapwO/q/LPzrcuArtBtboq/sMqyy/x7W/AxtjPJH7eHEMgTVB+AmdNWrcLX+si920RICF83g+Iu5sSlPlrFRquOno3I1ZFOqtINGDKG5AJEZQA3n1bw04Hbg8GXwy/wrX7fv75t0+fV2puEK5hcH9STyupUxl+HAkOfPdQVvWAKPPLf99GOVYjfASJFFbdtTYsv+14nJQz+PfbDgD4Ciys+NrYeM23a66bf+r6GRjG157Mb+VHV+YzIty88N1/0ab5fMN3nG2rIU7+KhgDAWLUZyS4Zq3w5as/b+5hW321jdXavXD+Is6X8laBgeiHIhu7WwUlfLQL1nH0Z6AFJgg2BxeQNItXyF81AMoJIJWNUILQFQLVAzj/rv36CojyIwoD3lEa++uk9G3XqXSL8NffPn09Y20RACdbB/900DrzOgtUgf06jyHY9ieE+AndrocCMawcm2s7BSSS1SrBbcO/dZvPpch/y9hHSwCQwl+XfxXf7/u7m+Pp8rkDNr97U3kIoqPb+knaA+ddezGfi9D/XgQfLbW/vP7nU8AEMJ91pHe7DHzj/otDVx8Q2/RDA7+VxHoD6XPjavXJP9rqfyKOd9EOiG3/QKyYN5/bXB8V5H9L6r0OUCJXSvKrNH7nkNV2/DWErgECUB5BZf4fEPzcEhzaHAgm6fu6+wWGP9pdPwPtwB+E39LYrceeQWxzP5qI7/i+qd5h7T889KN2B/Sold7l1a563WJt762NWhBQV8b+A1rvyvlP/Hug8vr520tEYRi8b0B/a9wrz39sGf4HJ35Tla/ujbxE8upGbdjKA36yBsHPQWdNAR/WBtJZ+TKZV337BlX/tdm828Yftg1obziALF5FTJ76IQDRn34phzz/8dO65M99yLXlCJIJAKogRKzdSoCpQLRYg/D67X3I+vTH7vnXoPKrD+DA6iSvbPMeA7f7Eu+jKg9WlP729l9zkLdfMbZ+NRm/NsB//ejQrnoFgWTzpVH+ut+vLx98rsd8nng79Rre1sEPJ3757re9819fDd8v0+9u1ud++q8fyelLe/3tg79+6UD/sav+TVP913fj+9vO+o+fO+hAJa+WwsvO3xCjdUdQDQytv6aktzO9GH9Vku/k+VEJvo3+19dWUGh8IKOPJvyvXbjK4UX4cx//13cb/+Pb+w3Bx70AnPiiho8u0DuEfL3gHxvoH/3zlTX4paiPHjowSuBy3bed9LdcV0X+0TO+9NJ/BWhgWKuNzR966h8t9V+/dtT/vP/VJvr13WAHtrC+HyjCz5u/VCqfze5dIb0LjJUa9EKiK19f8vaXWunbGugrMgDqcoMvdgVMNwdCfgnlm3cVK2oAHrAmKPdPmAIw9bWBBIiB/N/+acnbjl6W8FJnXa2aXRH0j+8XKW9z+ultGS9r+XidAgwDQX8CA69XKm+hrygP2M6K8L55wfJ6v/IrOHeNs39k/JvXLOstv3jQu0v061++b3lz+9WP1rcb5VB8+uV/feP7YPDt1uDhsx+vYy+XBQ9vF11DzLd0PrzttXB1t/XV3Ge/Wgm9vejTjx+tXvDwdgrw8PKC18bV2FfCwNrBx8uqwefLfMHnVztdF78Ncm3qrKb3injAuNZtn60JPH/W2Dr8VZ+vxeCGazCt1jkgZPDvW3Kf/jfYNtdrTAVU1r3/+pDDS8Hd92Hzo2hqAQYGhdI3tvDW2Dv6fXP8R5D/9FfnvEPH92ecP1vP5+Cy0ny/rvtvqE1/QQ1A0nR9BLHkY82L3h9s4DtqYel6wKG/pya8JtbXbEP46l8Fafceidy8A0MvN1/Ln8+q+qANNAXcslyJr6r8XrBg15reXsx9KBx+qRl+N4E+EPsvnyPeR9/9s5A+WuuvGPH5LcYrzH5+VbCpQUEU/u7mIDf++BEuv/GJP1D99EU7v382yG/ormb6lfBqYF8pr67wJv1XpgX8+Pe3H38vAOWLj2++KGl94frvVf7xxvt7UtrHq/Av8vyvlf1GFX8mor8z6xca9R/eKf4lnaoP/5IZkEXWxuGbzvpi+d/f6Uvg+57Q6fPUfyqfz5jhe1KgTIDLtW7N17r1LaJ38fLvqa1F1l/4KhiF+7TP/xNBf63GvidkrnObdW5zA38/adpPPP8f0Fzh0vfULDC6+WboP7vi6x5/QezL9f67INRXder/BYF1+EXgFf7/CwIA3n+//XOx8JFcwdP7RwL/1hRXbYUgIbdrBPtfnyHwV4d8G9nLRIABvN/W/3PNai6Qv7s+v7tV7w4a2PB963CNEJ9bPr+vFNx13avB9/qhyqvJ+ftaU62tnW+m4rVP9fu7TfXplzWMro4MrDB183R5/fLg0/vY/71a8Of2KKDQuu1P3dqqgtGfkTUrunW98poBvr45YB1Og9f69eGX73uqv1AkjkQIifk7kkRRBIu2O9cNfRwhth5GoW64JVDPD3Y+5SJblPT9kCa2NIkH2+0Oc93dmohB6ivcj1Ng9OUgbvtFYP+ukfvpvaxLXGxLgnUhSdIeEXnoLgpClMDJHRbhKBoEW4JAt3QA2KMxysNoakvtXBpwjUfbiAbMU6HrRuELv7w7jO8Dfv/czf0s2zdoX19GF+nKGYKREUp5BELjIR76yM4HJ4KTAppEKQKnQgRDXMRbKX9s/ZDvKv73Hf71ii1hF7bPd4r8uDUwG5JYf7NEdDLz/uNgaKa9q+aZd3mkawyu2ptziWWbYZRsUkQmvmqu6Z0eFw8LmkNBR2Ycogzj3hmI9bIRlw+yOl73kM+Gp2Gn49fnbYtBTw/jh/0ep+fkhMkHaNntDtQcQdy2hFiqcZuBbAjJ0PCuI/V76SEWEqDOxcnvF6e4r5/lEPTRqdTP/am8WYaBw4vYEhZO4ekl5a1qgrk0h5PkoO0oR39QAySeKzeCZJajFXh/B6fpx8UNz8R+tIhjpTTuJOndGWa9xNHTh+0MGnO938rxfJAygEDQMnJp73nsrsxzUqzsDOXHSOiefQKJ+XTqtzCBzPy94M5JKVuWJrP6gsOk8NzRzRlGYeGB3B7UfTxpCKUFhr6glorvmsN0hMPy7lhkcK0Qzj/De1FhY4ZLOlpH7NFGDOoh7ER0p8WlL6t7vLnQHcSNxqhwJYU9/Ag6MhbVSQPT39PwEO07Wph82SxCmj6MAiNL3lY8PW5YEIV7vLs+XOH4WG5WrEiDDLNC1rGdkKXMnUWZCDmbEIGkZ62mJKLzxIkg7tXRt6/KWa0Q14bLauYC6fRAz3wI+yITnQi+V47TiUess849ZObgpkJ0ds+xyNyWAypABSbTNa9by7F66cnRsQd1rcxHyNVnEk554x4ersnprI8EeY29oCGybN9J7ZXRxxKEEL5gMiDgkw8Fp+e12OFt+/AuS8fI2/0dlkSJ8dOQ7TJEdWKNus4IWpD7g51ZpRgfcXcqMICWM8+3UYoKYWKR/WjXpDipBYcHl0AmnGcEH7XW5azIh33ssYnfnrLeKM+oQ/Bd2DE2ZcE48jxp9OUo293zUpp2bONtfDzpVJbKsqAwB18ITcJDrvsYKXyL97FdnTBTHqR7LhIeLZLxsqcaDnd+3BA61hniFF8H1jxzBIPH8bIbw+SRJGpnipC4HdjJMFWnvdWudup394CvDxj99BjvGDNzCqu2yJULxE357iQnadRRTMRYOmediojbxqEp8451lfrHDQVnaUtEV/BtO8Ohngu8vPegwoeIVvan+HqZsb0nUZeSP+v57cwznLT4Rye2NH8q6DyYPMTe2Yqq6sxidXIW8OQt6TS59A2IkGbbng2TadpkYWQz7oxQEYYpJwhoFMWOM/V9rMopxRt0tstcnCPkea8pcaAOqQzdhDnT/Wm3u4r5LrXmOyo0rdfantXAIs7KTgSPFsktqe/dj5pU6d0uP9wdY1u4TFXdRKnCL2lNE9qY2NsgONu+GtVobPL9ARKzubZb+iBDOneZ+Ga8bg0zFWv3fmXN5315HtEB1XChP++2VlkDZBFUITxLJnex7gJ3u3EYZkm9JmUt0nTGzYwmI8dI/pSmcNw9c5kunk2pXMctXSiHYxazFiZJTwKfEi5KPTht861AtinwRH2nV+T2MVwWdOSiQzipl5O845RbHIV8c8b0M8vWizSfr+kpK1Pg2xWdeFlGqRi5zcBp/qDKvL3HuB1ljjOXWiy66HHTGt5ZguoLRcGna0tR+p6+08hzh8PT9uAMszgrzXGOZCHoDSzinoPhKGp7w5jHXlGc8WFRXmLh9InFdPQEPW+sc35CRxu2K442+kIJzh2ID+Zhl+Mph2hVWe+Aa5PmdT6PpTxakmzX4ukmL+xzew2odihwWcETHIUZszvl/t3eV0o7chOUL7y5dfOT3hgJqkrI7emYuU6JVxreH88lf+fnu0VZZ0kBMbUsCXchVVamrDBWDX8SPDzbRvh+oXbh8wrCeJQQW3+MwxMSRzHKFhKXkb1JDwtuPyePvN7PHpRgDX1tzs8oqeZQf+ILQj2J0pqIYBuytHgLztOF7JNG23GFdIIW1JD5kaO44qQ/j8yzvZMcR5TaQSwMHVNomiYcg3vcH8qBuXELcsWpDIv067IlUw3xK+cxS4OLuDemyUNlJkun3l5HlUmSqCRuiLhrg9m5RslcGrvwVvLC8AxZFpkQC8tPVY3ptp0yFTlrMZ8MC7TTpWXX9fszQYfRs6zkkGeMIj7ZhDgWnHFedr0Ks/qxY4hLyEWFsR0HCucTxFZ4ITOy4ZjYl8fVGMhaGgIxG5rRtwdZNRR2BwN5lKlA6/aT8SAKKRp1pp6kKkKyVYM8a7teFMFKBi25ZirJtByPRvt0guvQtydFeihXEzPnwRdSNmjCqzzcurnRnvOjrDR/0Suo0WLZrHSjNlVbvwmXyrrcdE7ftxMwVNUhoEh/tEo+SeTWc6vYftKxoVqMdZNvziOsl94ReHVEC0Uw98SS+MbsF9k22Tc3xdh1a1pgSeOBcEKXtbpdI9aNi2yQF63DvY06VTxTBZwwooEz0FDL7kWrFo0pyZOeU4opsBNijuYwpALBkGR3mo2s2x9jlJZuggxSX3ydDI1iw06Fxa3AlagZRdKB55nhRsHsIWsx/Hn0LsVAi6wCaYVDykeuGFXa7u+toDtd6F4Sw5kKYidFiZQz4HbPXFQXweG2eyI98zvrehtz6omLfKSf2ifEw8KWEmVoaunB5eEWOj5sYRSPKHLku2OC+o4oJ07eXmJuweRqF8i+SMu7m2EfHkYeeUqPpIN/ha/2flR4pjIkMqNv4gQx+E5EbtM5isW0PfZy7XKQ0zwzmju3dSsGB5DTYBoa4Fi8woFTweOtEOiYsBWzpE4PbJu416apU4E3Yf8YtksZtFyT7cUxla4sJz5Mz8XEmjEFHduygZ1n9BFHOLE0fSuKZYm+3Kzg7DnXLDErpEUYbg6rSp6fTVBcssiHSC5Irih3Pz5pFosPhwMZDzEUq/HpQRsHzcmrYYqmHTPW9sV5iBSAno+BmViPwPUTCZkXnw9KRiH4FD9jsi/pvIJwy7m80ayoPBmFNruYL+JcC2tvf6GwfeDhT7N1B+qkyZom0QiAMq6QaxdHTuRaTFJrZIk52T0nNeSu95QXtpbBMz5/M2sFY9BEO9ri0ypv0TkdlPr6gHlRGVxDRtnMuSBsccBzIuLNaaHb6751/dDSzdoYpSTHFBbSzlJGPlVqFtmrJ4+ZYd4hJpWPWylG2BAk2hOsHNUYGU6yGCU+/IRhJL2aniRcciV1mPiA6EQ1yPp5VoyGCyDvoajCRMoRI50M2qwZVssetZaNB+iiBhJII3h1vOPDiTA8lhuc82kXDgcjvpFVj95ZqSJ3N3bHcZ0VP8rIs/WrkMUuHe65XE91/4IpuHePGMc43RgfbXiPYYW08J12uWZBFhga2oZofJrpJx8kWx+1+fhBMj2sxEyviA9QXjnCsx95zXaENDBYs3ZPYhlMJlkx4e449ntGKpgOlArjAY4DNpH2GFv7u/rmWrYxna8X0d1DKXllTpHPQ3LASI0hAEul7WYES1lu1p5WsSUGrFDpwNTEKro4J00fuF6yxJxpm5M9hWrgKOgAxbIFVX7B3QJfQ4L6LPikwJbzU/GKh1Y/kcY6ybchtoIF40daY8jcMmDlxhaUCNNkoJMj4QvOwDESr3LFk99um33H7mnbfoCUzpwHuJ0gH53hU8Q1/KW1im52VBg/qwAgXs86XqNcfdw+Zx8XJN0+tub+xjVHtY/R29xezsNAjsuCeY99POG6YPVnMwsuvkRNGqhgjnVHteNebfcViAUHTZNt+sJE0kOCKkGbmlsd54f6WFDIycwbi8d0uOuVLr3VKZ8LV4a0Ese/Ya06H2GRGJue2Vs3ac9E/E7ifOR0VarqwGIHMplMvrC4DBQRE25AVT3TxtXxbqXitdpp69Y+d5vH9liHrmcHdpC17dXF+2MzNMcRbcjiOZdljZ3NOAGF6ygMQ2wTE9LIuewxWePEBBKJj2h7yxqpsqq9cxjrc/VgghYpDk/zml2FcOduz9jzHgW1rD4rTECXlB55WDoQu547HmWcVQvmaacQdNjTY1odTiruIvtTUVuNw2bdieOrKmxzJV7I03xAiWhPPNWMDivTUVpd8fcaD6tzDjfj42pLfWlHJQ+T4t7JnzZTdbe+mbecGLBe3SOIzARePgKoi6pPT7mSQuAzF2O6sIn9bE/NXDWx8AiOEn/HJ0qDHjoOkhgCD0+8RbqmOWiKJMrIIQigRzDoAonfKx7K9i49+yPm44UI833gnEGQQv32uvjhGQfr9gN9hYwd3xXOwrfzKJL8XJltJpkJRUexkR0PbX3c58dYOMRcPy3L3DggyLb2ScBTzDVSEcUKww6d4zEiD0ZHi46gDp7QmYTBWJdKYZ8PXSMIQ9NqgONgpa+3DKfkjlB10W7n6NoQIzpm7pK8yp8HJw4SgITPXZPZ2AUxEqkF9VGmsbJC8vcRP/nxUTbL7D4J8UgOmnvLiKTJWERFiO1RSw0PK4ZZTecDKBnYSvKT0rBon31wuaC1cq1VOMMYoEDkbI/1rceIobIcNtVB4R/M0su9ehCv13i7CFrEXKp8b8UVbLB4fIWHh88ZhbrfBef90oXCwWBJWx3zxkjB7Z53jj5pnSamMfFAEtqxd+VZ6lScjWdnL0D2bZex6PlsxFi7pdp4N1LxRQqm/G4MZ4H01QqUWBDNTVw/WFebgzveoiCMhqEdzMEw3II4jTkwdb/eSeR5kXbRouxsddfP3MU9Ec+W0y0cE2Pdbdyx3WZpQU+4W1LX63bKIttPYq6W7l193/sUaYfHS4Ne1J2kz0S7B5WcENzrrL3x9UVqw8bMquthhBQO7W2XI24XSG4oh9C3rX8NogQ/w4Rqs6JwtGApxsXJOuRIHd9Q+4ReGuJqcozREHIjRhCco6CAjbC680pHMBHE1R1ivGnXXLSj8CLnzs1JtWA7g+jnhAlIj8/DoqftItuccjwvemg9oREXTwIUDLFJk6QK/H4xcn5P2i2/QFji4SjTe80FTn1EvsfMBAPcwurMYZuyxOjQt5mmRaZjT6fOP7cMVuvenAnXPMTPcSWl+VPja+mmpIo2ESE6gnOejAbZOFgb7SuSWW7EiCWcgedMU1KTwTwlvGLGe4pfKmlX0MmYHfbWTCCu01/aouQ65SyTqGoOLSluz71d+ypH7tM0G/oD/lTbQ7O7BhpKHVzvRhcTOVyOxBUWHUTaX+X7Xg2RHFEhPDKw3jrOCNkNidHITMjnqkk/6oPt1Jd+4C8Eryutk0d8JxRXSH1eo0mALd7RRszqk0sJnZA8Sw+4K8KPKyKhSVsXdXifqiOyj6SbKVa4plxPQvpYzGKnP46lpFSC2+r7A+McmUo+8CAfoGcdHpvnxUksr3GfwRYn/JsfWejVwcjdhN8wWGndCRumnV7X+j2Qrgf7OjdzYbod6u6x4p7vLDsU+UWgM3WKy9BbHjtbN3YHx02agD/R58NeO3YGNHkxecW2vufepAS+Zuc4GhyrwI7hEgg5gaUSkVXW0GKCSG4jREj2KRQwt7JHxYSkE39wk5jCe7w0ZsS+QVcx4St7oKVqZyLd3qONMgfmc2cbrmfQKpTMnZXimXBbDLU1Jjqz7Xh4mrZdGTdFyfEze9wzaIHSWXeeG3Oy/IcDClKzPoqZfHx4vGYucmFua6hi89pQsXERW4m18BFvRJwXeTrgfcN8YucbSU4F9phYZJs+UVYkF0FNtEXFwmiU/IlvbpBnMrFJsmITTabK7uWzJdAcwbMdRHr40GvxrsWcA3tUeb8tz2MNUW10jCut9L3DUeHYQOfQ56UcvXtKjqJy36qZdARCOhV+nLfhNquc44nEhISE+ed0iFKcvspW5u/xrkIfI0IoJYymAfPwtlnBVtnZV+vHDZvuF0ulvJAovQSPbvfy3tCC75yv5nLpQE4RqpvCN50aP7AFOi/3KDGtXegyrGN30g07aoIluofBOgaFgUpHSTnQxalJHtNVkjJmP0b3vDLLNTSb5D4b/BLLeoD5YtPv7RuGdNreloxaoBd7XPazhzFYMGQXm+/4SFBulBjZ1VEaDn0JPwibxiJrUHajRPLmnbiYR9/iC/kWHqUA8TJ/MU5cYxves7ymkjJoO3fvChGxHZWq2GO6g8dteMS7/cMxavgkybgQUh2zv5ILvH3okwkpBneHHzRLF0Ij2VvLU+8PL+tPRxFWSou+6NYB23LY9lFo1rLDHVA2sYaMP4glA1LOrXurFccHHLbc9mRV56uiVArRC3vnyh46Y6nrm332IP+60+wZ2k/aIdvHr77zxFMDOY/uRAdz6S9E4R9TlNdZosWXE0ZtIWx2KJHQQBUfwUlyx+oyZy56qeugfh6jwjlTnHajqFyx7lvflOxLjvtXvjPI9qjoI2e3mNjt2QuhuE9QSj8xDMvvF+PhH0ro1nHPG1PrbKfNTxfLB1zql+1WY7zRtorDcmcAXozHG8ZJsroUqY6nQWSQWF8DEKyGWHJYJgCjvUXZGgO1PE9Fm3MLMvvcXWIzhTyhD9N3tLPI7/qJYXG2s3k43skP6Xq/OujWp+qpLZlbJST3/KHGE13YzDR4ULAvbEc9soMH3H3vlORDNYUbcXYNmtZG0w3SHslNUfEMvnOrqrA874ovIgwRyexLAQjW+nVC+znjs4M9agRvOsBdJa3pYS+H+h37uC3yISeQMxsmimmfgmPXjidxb58L0t6BKLk7wAKcPkQadyZVIIWKOuvx/Jy0LAGIY3zS8ygJd4leZnmij+5JN+5YJWxrEYUrsiGwEqY0fNdAut4sznyJXBb2YOVwZj2b4qLnM4ECqx36ykLuBXH09ubIKQevQeBnRNtXCpPjC2MtSqXJM4JcrwxkybcpQscws5lrLglG4gmxtDekvd61eq7srw6V+WZp3hmXgXPg+3pCMqHCi2zcLnuFfJzzHNlig2Q1RWnZg07UTFc/DP5wMEmDCx4Uz8XpraUgS9DPp1MJWUHk1IKwoK6Fo1T8CBfzngrq6Pj9Mef5VYEBRTdUxI+qz6ZoK7gGy42xfT2bVRKGQVd76OjLSX5tJ7sNoG0MpxwkqbkGYNtT1e5OzsuSFp7hSrMwRiPG6/BUggcqzXtZD0rTZSBgn2xNPLbKmbamPdeNl8lEu3PvSbJbcrct+cCTQsyyxFjkZWrkwyJKs+AQB8494ONdG5N5f9bi7UzeL49EQOod5p99w2AVRhrpzkTwmPNJpCBywj1INK2Xnqr7lbioNAnFoOA2dk2ks6SJAZ+QQzJka7VoOzTzjhCtCid96dlidB+3M8iahySReUU+Phu/vHDx5TZabYmqYxpZrqVkqXALpjQZot6FIOC3VNiwh8XXITyBHjQvjIsSdl5qHmyudRdJbgEKP9qhUeqly8nqA11akj8T13s+cc54K/ZbulPVwJpP2WneWb0QgZQtgMR4PzmyigwOdMBv0HAT+aFIplNvwbxnKVKVmm5jmBheIucUeDdRedI5cfL4KoLoye8fM19oZPM4jPIO508E0d0RkSE4HbeuPEUSZ1ySdh1/6uwr4p/U7aRC/ON4era1TN0SniFFQ2f63HmYO9NdzEbsDs2TRy7WiLre+QqrSJx67f4q5ogBisjrciJSH7p7Z40k5CKdKsE4VlLrQ0F1gU7MoUFj0pO8nr92N5tyZPOg6gi2rc5aKSPBYdKuFVP56NBoqNs3D4nQ2Efg0gx1xGOJNgv36t+KvDtvm/bG8MqD3RbnS1UI9gGzTbR9nr09iei7Rz+Ylz4gdQdWHpHbticXaRckleTn+ckTVxI2/bDkb/sODx4tEUFUYhblkx12w64r0D7JkccOtRvxlp2UKWY6FBQG3rDkErq9Hh7qiHMxXA6nufJFQ5nQ1scIDy+HEp1k1uc9W0EAvhGDZDdGjxEFabSdt5gIbENrU5y/07k2Pe90cwhZo9AQr9/FMNeTMkwdTyhx0UYrOM0FAV/TO8tktCOMpXp/WvNWlCqYiy3ZcC/GFW8k1k22BmyMNxVJO22FvjfOPFTDNCiVTjQ5fjr5+4rlLrMYunF+p9zkZBN4k5z2VOsRl4vpdYNknE71sO2NObwEcYNb9zua+unDtZPMHYLqkKJFgPhHW42FkAjiBRkiYD/n0k74ht4tHKHHSny/4Ej8iBLhVBchE+4hctiXBgU/S0UjQcVHtGfDuoxVYvMcK/TPW98PEXCM0EBCyjk3rBvzVeT1pPc4n/2CuaNFfGPsDLlWx3sXqI8DNAUz20vz4BXbmRFm7XA2UetJbfsIlgf38hCRKvOfssc27EM8ICLFLqbdNJlfCrHpRCYbZK5/ZsYuuTRjVZZasktMW19C/rDfz/720IvPZsEXSjncM2a8tXmZtXvhMGgHCr+RdOpv62vZXXF3McSOgnNlq0tkYDPUoFwX7qLMzfHs3DGpbCSGADWpQ7WZ2J5PBn5TLwvu62X3vJewrobHdlpEhYwOw5450TNy4ONnsW3lQ+tuBYaiADRIh8uuOjTzpbXvFhoMRZQ86ZFniAtKy7VI4j7kn9w94+Y5XqFcbbu3PbLkbSB0uHReiurpHOdH6pZPv6IugVXUROcqVYgJNJXK+JF5PDw0KnjNvx5dGiGuZZ1KNr48M1VxnZsZyjfH1B7pGPYjxQR71xxJFD3e/amjZ6bAbFCHTYyV7xyWCTAfooIe3yHgjjy6o2HNfpjxfR72ku5WW4pXZU2O6Wg8ynyEsjcCEjFEGwrluTWfoecfoUQwtDQ8ASbPDl2C3HSEEAmAh2o8NUwCuRpJs7cKFeT4rEw8BhIfdjFCJXti+OMO422y7wXv3FuX6AHj2VFe3OV2OugIi4vw0kz3CD3qo6h3D1Tsic6WzZjGY2g/Hi60K8B8Flx3PvYgeOM0saF+xHrUZu57447o1dGHOOT+HG1vgHbXHXdh7yaMVK0bsEJM6BjjFo6ROnvnZOPTg4RUisf3EttbFaXfB+xCIDupLYJDupA9JERGE7HNrmxA3tqCuuBBD7vTVj8wN4R8Bq05yKxNsY7guCf8rmnO3cRvtsIKDP/sDxpPxuIUamhBLqHJ7EYTxI0Y8ReAE8T+EeELLMe87UG4bxTdmZQy2sihfaOyh/N1aBIjOAsUwoQ0Rulnap+Pbga7Ic2rsJRE9Z4RAIaOM64+1bRXS3gKL0ZtX9FGup8VWBAIk34icyc79v1KD3ug6zZkx2KEnPmRIOMesoGhtnxtFzL2ANXbwkp34HbHGyIdQgYqRKqoruedepFSz1FKW9ojGLc7xdM5Rkp0u0802Uds4YGnVCIScqrPd/3mVdXlecREeAymrRO6x6iOql0eLeemVjByVk6YPvYn2YFl7N7HspChVAE9Metm5Kq2N6fQzQ4xsDjk4rTb6cCzRJKcw8Os2/M+AAk6FJvW4q+Sb/iko58eUkUeOUzKFVReero9PjPPrZgCakHCBaaxxWXzRuqFxNzZjO156TDy4sniQYV6vVjxjRWF0/6p6GycqIuN7FmVkX3f5vwde7wl6qUNEIQlfES/H8dO9QLNe1C7HtstbVE7Xt25jUy4nQqbFXDe5ebGSSpK8UM5ZLkx3Nm6iLfusAvwvTOfpRGxMBzlH4Og1JX9iDLr4O4R577rt3yrMDhFCvu9kS7zeevuHU9VZtvZt9uSgtEdhyoHzuil5xktqroByH2/oNPFFkymPkl512LP4ZrdJvT4GF0+8S4eF6M74yJUNsnn3gkMxoGt+VkN+QqTgBhUJYaTZ2xAX/lH8iBxUhF0BM+LNtIwyZsGbPLVC57RSKZNFNfeD3p+kC5p1DywciRZR1ICLCtTyj87eV5eQmlIK+RIA7jnXPZKOAbYo4S63Ky1J8f5lZMOjxssPdK5llrkEEqY6eamGitbzZXnc17tJMSfj5PXWJ0+OsLtQGikCh23/VVIllobKqee9sjFvmdBSyPP7lyo9mQuHHeOncJ1rMGu0YeyaGWnKZNSHtPkUhskIglhII96LOsynZ7UAk4XVCXpJtOT4jpUSJWnHtnHBuze/O1xO0gQt992uzb0wjPkJlMRDl2mCXOelqoF8GELDpcYdc7Z4qKMnBkhKjdmYzN3qFhfvGI/54kEZ8Vl77F5clC1wym399czZV0k536sRhPzJWIvyOE9qDsEiW8eZpPdiegkRziNif6QyL1OuhBxvnfMNTnr4yyRKL7f88uunJIzcRgcQqLCG9FtScLvOdZXq4zm5eC6aAs9mQC+CF2htHumbCGVOVEpVJiR2TjlPJaMO4wSD7HcDUAo2jg+3FAsLS5kJzNp91RoC/sleQ4aftkmwkXs8HNbm1lzQvTrngRFwhHtbxzVjvQ8XawCPiHOZB+T5cJLC3+BNDUt9WusmU8tEFvR531nn0JayN0OieJoy5x3s4ET8BZCSmy5XywQn4etTFbOLQ7LiaIj+DaOCroUPi2W+aIStrdHu7GqRyUJRLLtib14tpwOo5JbvJzuxCOp3Iip0SnYZ0J7iUN1v+0t6Vm4VjjhA/TES2bWTb7wHqbhkPZ05GnW0BB5GLOlZLTjXkMeU7KtD4ppTbCsliiq1ypWNb2WC7iCli5STU8/zQHwYSKryykk3yrNIc6du79F/d5s+BDZbz0CpKqhvJB4HAuHKVmYifD8ZBdYLl5j0hWlqpar5inReLPA2YOVa8FNzHM2vvs12Y6PYb6fSnTmTG6Uo7QYVQ3XdmcIvpyAublydj9badkL9dZrPDVHxB6APAszvP0EnLHKJ1q0Ogz4FggCrn0T3CzXyrnJawsKhLZU5oUsluROMX2pNcFSuG0PAGetniQpSi0Fj/DHxZK9s2mAiGc/a1KEr6czxAaoUV0SxnQfkHi2A+kAEnlFsrMNWYiR70rEsbWkU0pSm4NsNAxp6FA+L3mArmALYA4N7b0epmE77h+514OSjXQMVlUyuqpA2YjZkssH5CU6TLadTbFXBMN5rPVqICn2KMlxrmcWSsMnRWKLp+9xcqNq1oSrimAY1WDIiW4hEdL1zeiiviqVAkeNJdE2Cdb5293RlIJ8LFuMf0h78xETXF6WNbFzsItuE5dr1AYu8ZzarfO0m5OqT02SgIov3BWOxdEX7HzY+QzjnKyUJs3ppFmdZYji02yGuS0qzqbuQykzWvpY/GJ3vF7ZOzeb4vEhOkkRuLOxNaRi9k/xyenGnt/NDqZU9gi3uabdiUlA7o+DciUI6rznzgDIcWyn3ZLOjVquqYzsdta6YLGhpTJ7JRV0PpMiwwWwSVkE0gqEMs/mi9YVdaCcpCvfRbcRXviH5pGaGoR72ZtcmeOwvDtlYjEY9JBJGlcbz8pmcDc7aazDCScH5ZuRS5fJE3xQMijlEthNfA9ZQui3ouH1UEMKRSSiCWZabYb5LRt6j3ws6KBZhPzii2ek90M8n9CEPqXLbjGd6nBltv1SHwxxLHxEtNQii2qpo0y4Iayn6stNK+/MREuVvnuenCMlLZ1wOp/TY5n7p0c29l6ScUETjKhCcNZwORTPMCwuR93ZS1eono5LKOUaLZMkDQQgctFAW+exEufw3uLASYWp0QQ/ZuiuzXNyPA1VXOyYS1s7x0xf6rvQ30DFfQAZ4ukeHh6HerPvMYXHATApTsVkwiqFiyrAlSp5uF54M7zFqaj0YS3V/VXJa5MgZ8M3XVycjMctHj0BEbJqRI9MD6nEcB8Up/TrjLwaTmV52nID2iIQhkj0wyLNKtvUDeTDXA6Fyf4SgqBwqFkQ1gkQVZtZYHaKhxlXXR8pKT96nn2cLmgcJjglxYOuUYgxOUsWH5+THLYTEdRUVfJYkCk4AAdKvUudgrjO/ePu7AxXl1UhKRFZ2KJhtt2ecidsT4pzNHm9bPAzcyBbQkIXvVbCxj7nnYJYnjQg2QE9aIlet31+C5JkeNw9m3OCY2vZwHgigGufMVywzAmDIfOA5pedf++deUBH4vbouzNeSdKJQrtEV03VCKGezf25D1qmos5cqAfHc3M/uDqK5exVF/It48E3EWSN59WSbxQ6gC9NInq+4yalndIByH/KeRBK7vzYUQFjF+lEX3h72Z62CnuychF6Hi3TAYG55oSK1QjHoWL2SFpG2wwedbnzs9rB9y7hLxE/0GP6sEck9xl0PtDPsxs20IGzEBuhHB9h4l7Mp1ChAQptnO2t7W2tyF+/OG33oRrlFr6EwaLeFcdGvfuhoOtiR0h+c0KdlEzQnpghn5RbD0MWr0zuIKZ5zi6tql2N8Eh/vN7w+WriLGZ6sQTgxZCq639f0i38YumcOpJKemfvVnNnuQKWXBkiasfJ5foxApKnLt3hab6LGQ9RgUpTdDkPVPoce1ntr/eE2x6Qy/aedjv1qsTkBcH3fru9eHeqq2nB2t9Lyoxy8mQ3g0JHB5Crr6gpyPSBCZ5Qms+T6t/ZwGjtx1MeBIM+o3h4TK63cn8vyj17yZEGwuWohRrqoemJqW5LyKX0xTtdhm5uu5mF3WkXNrf6Rlcy09tAOMjCoGqmgFJ5UhjfjvSW2IK8JAq+VRxCdoagfbDLmFCbyZTRbkgoQ3p0KjmGW4JepFpdE7b05J6cc2Ui7v1UERf72F+OSRlldLMTilip7njybO8m7frJo2By63KMa0vrdKPVmW2AUNYtEsiq3tMHFFefykVX81YWZe1wKzWKUji1Jm9BPfKRsOzp+/VZ3OSDJGBMQj9PWTTi7Y1e+OzaPAeXLZfpQMt34DAlV4TJoiG6pU0PSyHGw5nBeLpZlm0xHCtob9+u58GUIOhGw/So73Q6myjTgHTbLojdsETtI1g872podnrulEMJKf0Y3/dE4OjB4Xa8nEfFS4dlWITwqM0PM+KPhyu1mC42x3y9RD6ApQ80Zi1UDbYzi8I2xczQg7/NHeMPVlBL/UiVObtVjlg9o/xJv5HQgWgLobe6s28XdWI9j52NNkmKp710VhKvGUzFTyDqqHd6TnkUKJnSedndcYqhxjnjLp6VOcfehZ7UmNEnGzsNlCfvYe0enXhWVArvwtbsFOez2e64JbJP+bS9KpDg3cXa8+HTdh5ccvJ2S4LtLVncBt489aI/ZfhYKiIdgYlCjyqDu/dksoBSrrgk2xLvrqFy7M/zZOPH9tkrReupThB6dpsRp1N4ORPzU3nmSSY+87bfG8PuKVqN7sE6y+1byicvy+NGHSd6ywiWe3f4DPH9KHi4e9ftRr3uZx/HWQCNPGV+4jve90NTJavjSe2qdsoLsz+osB7MvHehTdwUr+q+ebLXE/7QbDp0LzV/37e22qS90t4OXXMh7R0oB0wsiKhBy3pktzDU5UlRUnbXH3kKyDlI0sS2Pt3dbdzHklcTOpkx9NU5D9MQqU10JqHOCT1v3u9ylj5oW5Vf7inVOc/qxlf9WeMl1jlPC8Y8nsjJUEfz6VfXrC6lYa/SaOHXiHYxGbMWTJSz7MHZscLhkuORj4c9TG0LWBQnUWLnMhQLGMQbfapTCaKFKKk4vCiYxghMPdju8zF33Aa9Odd9l9WXrXBzdCvNZVqPhDPs7ptczlNO8e22arR0nCSDm7yQR6ElM57P6HYso12qPG7NXlQwqXOF5PkMpkffEkoY09uoufO8jfSW9hB27eOWQj4qPriTTVdFu7ALBhu2GIXDcblkrJgfIu1Q+FhbCwfEHO51LPro6cEf+n47oy6CGCTZPRDnpnTqmW0sDKNn2z70YZBgaHLxrgBvP7fKTj7c1dKPjMvZ3d/JJSjs7GTkDpRBNiqSEs6bmphc4csZ83gHlnD1MXROXoRePwAwT2UNTvLxc2ALN2jrVj/BcB3BVAHB4l590iNWnsvuAbOCJIjztLZrL62PDz3enyx3h+23j6AnkZnCO22+FIM5jMM23Sbx0X5Kih0g3tLVJlLbxYwHu6e3hYb+Wh9LVdVM0q5OlqL0zaRVfdD7EERj/bJ1CjyMXAoLdrRT7ArtjF37fLC152W7IP3dQ+vbjgwDVEIV0q8xGwfz7V2oqV1ztDFPuF8w0k8h195dbtYRszP7OWNT4fsHzA6aaai29JweBbtUKWQKkzovD+F4uQQWrNKLBa4fcu4F7f071qsOH0/u8Xry/MwhBzWK4EGHSVR1ateG7f5UYdsSYS+OyjmG5QI47lUJrONwXStAjX521kgUSp7sEYFYsoYO5zpBlhCjt4+7ftlfw5FZ5oXSTVBEYVf6bgsZcsHpLjf1+biI1HPLZIk2XrateR2Op3PN6iJb3tqDC8ptZOlA2XglDTinGXdn2kmpbEkG6e3MTRqkJ5Ybe9vzp5Ss3GpkiN66yKee8yyNpoxZRONx33fF3rQyLZmlLf6kpIfnoPdY8AnKblh5JMigp3rj6B/uB18deHd4XgN0S9ssXdkc1BXLDunR7ZBQyzR77tjkTpD5PpUtu1ubi5NaiTo1T9tW7p6Y108nuQ+J9HLSIKbEVWN/A6himCM7U11khvHmagfZhMfSNRhpC0VzaqZAPBswOT4gDiYt7eV6nWMhsxIYx8ZjYg/besbVw4PbXy+FeDl6OgC2jXdQVfVC1fYBRzHGFQ+L6sFFgxCgSMQQ8uznyfWwX+Ah324vqN6ktJ9JB3UQRyndXuveO/FSxRwfPJvsMVqbtRnJeRvKUfF6hC/0jGDu3RN2+rNgtB4aoquPLPcip5HwWRozHsohslRRq/dH6OkNmeixLc4FPS9xmHu0xOMOpp6U4XeOY3qcgLvhXcCyq3OX+XvNQrofPbvHtIx6qDHH6E5gu5CixedOOF7vkKNgsSQH1jGtXJJL/KynHFbbQRB5yWHuRiSSNftxetk+VbRblGvAyT7tGQ97akOCU90HKgioPUhITRPzDEzKIUhZDJq4cbkat4nk/6foLJYbhMIw+kAscFsGD+62wwnu9vSli850OmkD5f7fd07kBu5jjvCdU/pxvhqC+IR828/7uyJ7PF+0q/rKSgljP3gO0qOlpkjUqagbTXZCzphACCimceGRYfSeOEbCf0Y6UxboypC5Q3x1OgGv3UIVuF0tndAW1fT7vXRhQsdaBYI1SDlpiN1LlD4/lIXaxiHuACLJxdVJNT27fkF8naNVa1n56OnWA1xM6+dbS8waarAFvwBQN0/cIxH2kwHRYP2KG1vVphvwNIWsDNu8+KL7OpfgYArA8F6Y3wvRDJo06CkH7T03tcfGrGrMzL3FHS4JGa2n+kQ0P9MD+vZEreNlV0KF3Ogi3gYiukp5VukKzR+wZFCD18qW07y0DYOl3Fz0ZtDOrp+n4vza++37nV1iP5Why/Ng//90ZndvWALsL/2/kTVPTxpbe6h6xd3U97x6gHA8oe86JIWtykL9YLL9OjZnE6iAS+4P+U3fFNKv3WfrXOmPYN8p4ONdvtUB2m/BaK8PPghpbqURWAoFTV1H1Ymc2yk+6IpleBHLFqK/lmWM0NdRrlyC9uhGCvbyuszAERlFzbW/jnvYH+XL7kkOkLe8yA2Ht2h5b+Ln6WCkJ5O36oVwwFAIPXp5YB0SLnXG1IodKuPDXZdlQ2WUnN0DlSSEu4jbz/yFpA9GXEzwxjQ4Px3pYXyhlPIAqpPP7y5BNGyeBUTWrT/Irj6rsFKMWheJtNRN59AlfkMXuGKVQ5SzM4Z0uGTyNMfJxvXG4mMGv/JnDldoTJJRBmoIiQW1+LOOBPYPTXtdktnFyQqkw0rzEECIDwMyymFqxMXwZ2sLrtRcSSONie5CCfSBqwDExPECNkLRA3/ftZAgQvv/xoqjdnyK2gIC/Y1wreL558podT9YGv4JHI73weuyfhPKR2fJYfz5rvNTtR0kvcLJNAuwhTotoEyARzBdqpj7CWGeEYCfjOWiN1gEfWNUuuTivgfiyXAE1WDUrK/u2bbhYGU9F+lRGRP2bJagugLZJnHAe1KpglU816bXa0cwS8mooGzEVS0snIxDHI4nc2zfls0j/Dt8WZ4hom3+3o58NMMuI4w58n6gGdgVA88CoNpL3eqwGl3vI14qM1JIG/FYqN7A2K6TAZ1xsxxejz2qpyeUu72Ts4Fq22FQ9+7oTNwLIzf2/Lg8kRmcSeIjimzo4Go7vvpdAlMmSxLyDBiQJNj0ROs3bAVMKogbcX4vchFxTAjb904g6ZFwotOPVXkuPv0wqrhwU1RtzlPKfuMvi+TGud8a873/gm1/Zl1UfDCYnTMkRuQnv0eHtLpptHfuI6OL4ZCXhMR1du1M0uQ7VCQ9GIdPFnr5gNKcs0/vueHROrS0eU35mbHd0qltaZw2QdiFGaz4vaPz6M3fuT1ccmJTnqmdb2wQ7Ae5pQGbVgQtRsbUOfhP6tAwbJL7OKMvWQRd5Wvn7NSnsmR+5AHTlAoacTZqqLu2Mkk4uCrzyvvnefUDLn7d6wUVbvc/nkW/eXIbHzB4dmSUcHRMPzUF+wyuUoWYHMtXQrGS/jCBC2blOL1YLFIcY+/14hYw9ttMnrmWW68kUF5A92UunWKRRhVuklPjLjqK97rAFT0SCHefzAwj731ZUH/gAvxqtRHLSdv34yNTjHHwN4wjU+Hye5BoIrqtwVi3Bd6t3Hifkm2z2QSqxgMn+h7YaSm7No5A5+841jr5LhdwibM7FZ3RK6c4AbvBo80bTP452hq0stk4M5rfrU1zsHg91V40/3IJxvBNwosOrTG3IqPmJx5dQpY+uBjBZXYEsJ1j8uLvsUUHQJxSSbwnNd2rXism2SrWcW6OXq9dFWoN2F8Bp/gpf8xMPKhDeLW9XUe5pn/u6yNYDrU27aelgyhq6o12HOFOdxh3ENUdBNFiKnbcxz1L71uFQcUpVkXsvm6wY3q6a960aJs95y360TUO0cpxGUXe97S7N4g1H+x9t7vtBZ0A0dMudrmCtsjmDYf6pMZwnzriw83Wrvh3m6zVpGc/vtntQCJzN8Ye4wNlXedEt5HHVyrG36fZPP1D16u3sCtwmlvBdthEaAVq5MXddfO3m0W49cQ4eOhxghOcCnkaQQ0BTIeE6dAh5qlJtgcvK7U2hsJE/mlmlhCruAfmUYymjMTgYYd7Sn414KobINxlgLPZL+nffm16Aq3aypI41/7i9WBRmh1sQE88wRBFurkf0b4hnKhL51ZvH2sIPoOCsqIdfrZu+dg8cxsgl0iVifpUkQPL5z7iELyZ8QyMbTc0DHmpz5J5cszDhz/V0wWBvH6z83ulKUJ/IDvOKQqiQRehU9fnQyTJu7KuYvTcMl0p7foCP63OKdHcTl5N2HsxU85MZttDnJ/WgiwFUhwgjN7BrsU8XY/X445NGPMIjUJ6pG7sZKXAAcptD58lfQKcW0ZJjn/rkvxeF9frzewGcHvnpn5oRNwndPtgtHo1OAVieNJd93JM1BT030ieB80Qnzki0pRX6IOcRwqMmFqoawlNYnJij7n85UMn33E5hySli+4FU0AxDGB7F2azjKZEUqubTyy4UB3rC0fTUwbRZOBKKm8i//x9A63+TIFdIb1hWQxLaCSHzNKf6tni80uNXc8k/TfL7ci6TlD1rYdo+Md7Ee//5YtJMYpyI3iC+aX5ICLqDiUU2XpCmg8t4g4v2x5bLlvyeWSir5PNyCqpS51L7FrFWxdFmA8sEDgQ/GDU1StYqrcxmlWL33Sci1mr0BhbxB+s8J1EgSHl0LOwgju/g2oOyjjOTadxx44V36tJBCsiZqnUMHeu6MZYNpx99aFcqSjDSikH35MGgWpwFg6CPlmdSOzAXz90OoC8ZX+xc4HOx8vJPkBmLdwsPsl+G02BoiepVWS016+gew5wk+v2lIJ8/1eXsXAttprPcy2OsjvA3fheu9OiIGtClAVU6fByKqYQ2oKasrtMvlw8cXT5CwDSEElkgiCiTYuKkqDxPmnvUOxGgJSSpBXMW8KhmfHhTFLfn/r0x0/NIKildBynoQxB1gFNfwVFqn4yV2Th0q1q8yTF4TcafvI60Radv9VyIu/2qt8DBiGFBQH+u3OrDP743IYVFPLPuyFG0FtKgVgzUU6qAaHiKHMMuk9PE411BjPqQot0/P/JU1ggKAYJ3wh0OrklKoHgR3HSUAUJM1w3yKEepaqyncDgFD32WByEria0bCcsmKJj2gB1NcMRUy5B0HRDZD4VAKF6REIJhkX4UkBT0Kbxs463LJvlKpvfJemH8SFUru/hOqmY3ZU+vK/HpgI1ALkU7Q9VFl1z6uaKFZwyDFSF7hOMF5RbOX7JUzJ12kcs+b71Gy/WAQfuxDWhxD4M0g6QlOiUQagMAAU0xDk+gQG6HHPQHdzmU+RYYvTmyHZLHOFBRMYTzRhNI3MQiVLwTkNutGhpMlLpkJlMNuzuRA05dNBksApZPpUeyNUwbn1xCPpWbFVjkRTok7gxW0BffbE+E3SGbY/TKpkP0BgN8UVQS6BIDnpJ4P/dgAvaoept6YNk+BTAzhqoSkfEH+p2/Kilxtff1DH1uhwXH9DWmsrJc/YGwiA/XW6ull45IwIEqJeN3755vdnV+1TPTx/8tpqu4GDHf2CQ7Fl/m/EDH2L1giPt39wdv9jylAdMubr7fp1Jup15EHcfkZD3+JsSgxNGLbTWLm7WvRBxCtUszwwdUMRxZvAVnJspkd4Kklz4ftDDmGS1nv0tiwxCJZz5Rqlm20mZDhu6ffM/qqIO9kPg5YvZPnX4MMYFyJUN7T6bv0FTCEhziK9wtwS4OcZvueyL8SUaTbFOl6/m50f+Pkjdiw7/9nPVAQh7AXBAIU5us4ObIL68Bj1k94lzXIIEXeyBfhO0trG6eU2u/vig8KBERcPk6G3dm9C7ldcTK7XoUxVpj6s2+MQFtDpg8AJzpeCAjkQ2WijEusWGlG14/iJwrRb2xPro/etO3BkG3tu8qlOR6wuLVggmkgVioRciY8FpcOorYNqD9kDtHzphrB7Advq4gZFHS7ZwuJW08ydshkmaYDzgNKeaFWUhm/XCNh1xAu+bYMA879+xHm4GQXhT5Wh74u8qRHB2lhwNHhUnwjRkryMrQiUXNpT3QFk68Yzw4bqbauhpSkAUb/JyWtIroExHlQmqMNGBIgURZj+hiYmpxVbrA7iEDq/NMafs3boj165fbMJOe67GMx1dh52ulR2Yom6f6Sa6utyVUj7IVpUDqX7MbiE4gM5AqmYQ3W9+KH2snCLJ32TihDaJbqmcXMPw62SoI5ftvXVhO4ecNyfZj6ACeKLHYHhvzCXCqgWpJyRkRqGheRNNHlRxtzO0MJT6dY7ci2XwNd/TSzdp+P3GMM3qi3jrHIJ8qx8hT66lQXY1jj7cuz3Xy5OM1NLuALGY3GuPD5EtC2z+UIbDktLmI/xiLu/XnPgwUZvb4tlHQxGKBq++m55RyH/pHQ9Q16G4IVef6TsV4VfK+rbODPjzlhNPtn5V1hZ5ezLwgUdu/rV8Rusqt7CTopJ2pQPfFCRnEmDxXL0eNV7vsBWzgrLbcNoEnr1ZloEO+auBAOOabYMDan/wvuo0VsjFYfDyLD7Cu5ZHmRBk9E/KDz8D4fJojuTIloxwjBH2W52QgTcjUaxtiJaqo/AOFJIo4ghGg6P3UHiegGhOAOc0+oqMTxXm0B0r00uJdQj43JaY6uBPdKz7QCsmgSOk83S7aPJXY7b6BImbqwkv3rIZGm4CVmR9jtNEqLzSlzKlumyGCX45hOXlKEG64QlhTlnj0S5VObFdX/0YsMkjQpirx4m87/cOpxUfV8oMWHUCPJvtWP2A+71LDerx2j7/dH4X4j/34/Kbvrx4v7hhLheavlskk9CVdNQSL91DiAauqlxFyfWkotnO+cAn6YMXGr/K6ain6BGgE0G1Q/xeuWJCPErW8n+/m+kFRzL/cAztit0CYK39/6p29crn72MlhFzJH6u5+g/Mfec6tBR+/oL0/Ur2/BllqgkZClG7SqZ2I8pUCqw34/PjVRr7FD3NM17/uKVV3x0/aiIvXdWOTr8zwFqHs9db9H/FtlMeyPmsQK9eqOK05cMmmEaM5fn4J0o5CdtdZe/LLAu9TppuTm7jesF4qb7EvAPv8I7W2Y3ZdggH2z+JPhAUkMPWIGzROSgO/83fhkh/w6Uepf2IxuVLMbrG1sYs9GtxlKbMDMnQ9fMZtKtADopZuqVAqTEVBD0pig/rP4CmNUxiMhkG7VpEDxCF7+2NGS4mQ9iSfiDTI4545GMRaFssXQ0NzBj4rsBqVAweh0UlKSQYfpvH78/cMlbEfHFe/ebPOxXDl6JaXPEldGk05DGU2dWTZY3E16mKqGfGXSwYQl9G2192Wur5Xgsywvi9/4nm9/0i6W/DV3z79Wa8+1D7icdvb34FmieAmYSjaB8hDQkFdw+xBwaGlx9bZBreouq3SPXVxT5EO/aW56QONxzGBNEs2tAZTxZhy1d/fnJNF26kQBIP3kbOytSbbBMBBRjOTA4W+668gnaOeMtzAWWcXcXJLHRV09eHzqiYjjrGhE/nRffLCg7Qxl770IKAayLw06NWOp9hOf2mcMD9XFvEBMHnjI33+zK8jgAGMqc+DERxS7e5XVozfGnBQD2kZQiYHYrRFyhhWAsp0SuLzqXr/B92AM+ckHR6RtUH6V9twJZJp+cqk/WRFnYx+q5lLblQKrai0/5opfR4OUCxRa7zw9YESDBzuyH2BnDScm2Ab2YKFZyHjFwTcrdMoRo2BS8+KW6jN2w+KDU31QCYSLmZ0QGvA720Kyn3uhHht1TRwfXUS+4EaqqTXyd4DBYujgMjo/9dMxh53MO2mF0AdTpN9wg04H9+rlk/8L32/4/aS1LlZn3z7PNe19YSXYvyhPkQRG5Gy/7BJ40VFIUnr8NTK9KnIWfbxBYpPeaPS9hN8qqeAYpPsMPhnlDfrNTZfenI+OLWb40nUtNLuvEZ/Lf0kPrrFf3HiLVTpAh997ozBofdsxiVCk7Im03/qS85CGwMxhEYSKH86/gGLxu3270WyaFGz/zeTEtwIAY/6cZ7dR9UbxEAt4wdzeDA4Bi4pqSorVQjZ7avGuHtyHKLfNJGmfv+DdvRHF9jpD5JFbNx4dXb9LLqCDaoGMtEAUcPFjp369qPoudsMDWSpZC05pgaPuIdRCs+B+k5BqHW1z8CS/l3jk0/TljODXU/Odh+X4qoqE4FeP3BiVatXsy0uUtn3nR0IV14PKcm5QA/5S7Q8GZ5yjAUxr/AcuWqby0SE/T7y5AwGDKd4lexPu7rwd2V5s+Qidc15eKJ/Bg5tmMS8LMFC1xN2Hg782gR6lQDBNxAd4irF3Na4gaAdlp0F2d/mq/1AkBIx9Fc31P34t+vYcs3Lj6/GLtKDGJn88HqnEJwiMUilfolF0TsGkz3udzKpPB9HIBsIhQ1D1rcShQxSlBt0mXFMRTUhI+K/3QvvJm7eMIfYJNl+RCiCo0yQO+Dfs9+g+8SpZnlNxkaGCgPDps4Am+ArkWJoovssee0mzXr0bbiqjFQJScKZjyzlQMu7aHmKso8OEzNPuS1wXFlDjM1ScevCocrNA0QM9Fe39k7YEVVMPxqV2IQprnwPonEdXmVS8zRBQCCeQgqHF6XKgsUkk6Zxj+XkMWpVFp1W58gi1UxqydTrrr4qlDnJxb+ZM1u4d5EovZFHr41Omz0UBo9wRCJhEFgiecpjbjyHfG3h85GZdHtl3yYT6CA4BcFgbAsf30h49pj4mqaiQvKXi8p+aD1km5n1QB5SIneL9ydz5dwjKopmVQ64vLMM1ZUdwQef0y9hTXNT9JnAJfA7pn01+EiuLKEpZfXxH/BGbVZRfJx0w3ak7zWDNyY1JqDur+t7GDDwuAxiBSgAUY0TYgp6QOyUfRLO2ss3XEVCS0ogDNWDApajZstJZxHocsbWyI9pGASv9gwfwhISMAPRaVH7+xfpb+1IJ2iiQ1StX/I8NVD4ct4rPzLFXjhf1d0woh87iBYpbDORaqAIXMjo/vT5+KudiojH7iSXj2WNlMrTpxSW7JlSLkFWBF3wygDgg3j1NtSmcHx47ziM8RWLitfO7KtZHRD9XVDSqI8r82pxT1qWihU0/rt4ypI1dvcmesMTBgeerxIkz4Nx/SJ6M5JaACIAR4KDIBM/586Nb4FzK1KiWxqMbDBL8Oij4NLxPq7GPpJ4T7H73EhN9Gr81hlIbR2WX/1ILe/9Q8kOkZDVTP0yGrplSyu8+aua2643iwOLKx7+Z/w3iGL7fDoS3xqEi/Z77rvX009rvTx6++Nf8uW1DDTqIhdNZjBClXkFEZenX38cdjmhdR2g2XMxpLpvrq7kpFUMn5iZrUr/kG67SqIZF5bYqragOgU1P/+FgfvTAAVWbaFCBEubrFCDQ8VgNOycBkbx6oOQmWUL4W57dGFoRfgR5+inxKORl1Gr86Zqa3+tQQdk3KHPM5l8wq40Y1HxFra5XD6IoDj2auYSLEednWeyVycUFNEI/xWJ0Fa/9T/3UnayM2/21x5cG6f4FKayVlwt5dMLtatvAfslCCVTEvvpVUm7uvQgy7qnwvXOhkX44Gq/UL6SMYAqO1EHtTKfgvy8AA5bG6F1eAqEq7TqTECyl2pJPtXDFmorQqdvxterIbnGp3eMJEhNpF7WWODFfFZq4Lb3bSW3wNJ6FL9KKX1pa6nmWra2KOxI73fq8GilVc/aJPW77gZ1WKt1dNOR1ueozgeUTrKjrhCNQAlrZArQraZ/MtCP03WIsy9m1A3izLfcZEu0jyRisp00eA3h1jGZbqbw5/uZ0m3osgkmOxv94W6Q5xMU4UQ8tXuOcxvUhg66hMk1wa3wsELOyxQkIW6u6RsyB77xyHiOYHM64O/JAyo16/7/fQd0ReuYFpPgUdbEMUi0JE1+9Gr65ojdaGgxzOZ9z1iJnsuOHIGKSJlzpSiIpomTtVQki6Go17R8Cc8Yu3ipfVGCF1+r3NHMuPMicrR9Bls1l6cC8gYyRFqvpjTcZ2O8pgQZ/NIm+8FP77AV/Zt9xPng1CC0EF8+hbTM1tZ6PA3PuNBKWPdFHjBp/wJfgCD5mwZCpSmWlYP39ksOt6qOuYm+jKlVm6eUDBzBA4ud4UO++im4ZvKvXvD0ZI5mATVxAC/y+9Ao4Zsuw0+q+f8KNUempA/O3V4YK5IQo75YCW3eMn+mNLzm0lbU3I1uIjvx+iRxCJf7hyucOhFy8e2YY5yXo9Gql9ZcO/Hn6CxFparvyTGJj/GvxW9spiu3WhLLVDTdMjR+mAXVu7rF1jDPheLPcYp3k2KSLhNDVLTGJ95GL+UIf5C2YeazP5KyqwtuYxY06U+T7CWp37NOkwTKRxhm7mn0ILdnvRFsk9PLPtOf+4FeIt8M0zjO31IoBg5EP+4+kG3NZVMkH2vkjPhWTbhQ9bgBJ1eahBwowAFl0ZcvhjRKmy+xCB0okKF4Kuvy6c3+XG+unK8+mMyLBSk9uPQb9sr8MCmgyf+TXJIzXH12RkBEeYpvOipNQBzBX9w+R6e3yhgF4RTCjjPNyD5XgJENrRHUhpWQ9giLXJ74VNGcaXYSftyWlj8wh4bFb2ye4hif2lvRVaJT1+IanI4g4QsE5AQlTBuIm1vohxpcrf2x9L+90salqQS4yUg79mM4wLFrdhRmtuA7XwpgItwJJzgigaUSU0XtiTBRf5wqON76fRSAPtgzTiKTn1XlxyBb5oqZ8zpYJh32M7kZQ2eCu59lvAA79jc8f+9OlN5OIVsxWVPcXPzUtBofpjSsEC6NLxAiIC8v5dB8l4rjdtzH5bd5wNGKRgd7GoFc1HIMtqjBsu3K3idOO0weCX3msHOBE8wwM2VybrZ0walQoVC9HjluVBeVVD6YpgdyztPLvVv7mrox5KsT2wIBTurqYsVaZu6UjJ6PjbSZfSdf0jqmDtBerYaMqxHuh+mJlshVqSQ0iicjFB/Q3AdAhu3PXnb/GSTv7WK6l9pTTm4LfqRVKLkRqfl7+sN/rXNt6CrVe9qSrPXP+9DeHX7+WbnwxgY9L32FE6B/Fs+lppgVbgf+HI+lyKlFra+ayCONO2Xg/nr1JuS2vXsOM+9QDiSqvI5r54Lh8a5abPGsffrfNs4pnmsY4wSDBKAN+90n+arhqBkoquarLuu88aeZfwNJ2tF2k+iOncWkuLDD6RdK3Ep9+H5VkfxEi+x4Yzvy2qd04Dw+V0HMX3gpi/in/c7nC1YWuToxSxNK+/eBEHTKDSe6pYNALRID6oPZSZYbxiJssG5keLXU+myuNR6Kv6V2N818hFj1RqOx4VpvutYXvOz9bcp27+yyb6By295X5twP8yo3zFgvTejF44qQ2+i1I+XPC6014TLbD+mNc545ViT6WI6D7BKzkjQeYH7GPhtwiNT37RHgpn+7b86cgvnVLgw8+kgMv4oqJsITpbrXr5ktWUQ4of+qjB1d4Dtj1h45bJYAWhUmE1NUKX5/ODCHB6MMI5ntsW0ANfFaZK22wXf9gTZbxF+lu3eK4PvY3yxp7DEiMtZh7/sIxbuDVBXvc4SSMeGAA6CM7cTj5rFkaxQZYfQJEafKqze1BPmK4H/n8n3zk7Z9CdAA40m22QTQu2b+QFX6PRSRYNn5pLlKnBSN0f2+JEuvO7i+//vp8ugXZaqS9jMaYPiEo65wWRsR11UQwwfVKfGSoms9nmtMyagnnA669AoCViK/rViBpbwPRArz7m9gcHUYJ8eFQDXDb9xkJiJljRfJcWpxHXBehx+edYxgIlJHcz6roR1GynzMzZLwxDcgG6smGATqinXJGxbPhyRQflxeYZ3bfb6tqGejLHB2HeKUoh4hQUJs+/f/MDaHHfI+tVJ08fBsDx2eIkzgBjdyBsjk93bGYbu2LfDLCUhbKi91gGy3g5eVwsnIX90x8j4rVX3n6fmtFP0eMxYoZ/vgRlq2HNbbq3bmcb1+fi8qmzPGOuWyLqIH9/uxr0Sjj5Qk2BdcKrRihC41Rl470icKjR8NEMh3o63YALZ6lMc3IlFJ+a1ZmT1GRtjhYB4Un3lPt58GKdEEkPteoP0xHzr0zUxic0NOPeaOS+t+WX9E3/e2WrUtJRj33e0C9oQrcvbgpk0DzS5jogjgxIuZKyTF1QiB7/+KUoErf+SLHI0s9ZfO2A4LZqRTdDaPF3L6XN3hJN08Y0CCZmA50eRX3nGWJCzogSBw3lqt3TqQjosW18N0CglCLhJtUsDszFI4YHdfN8ph7cX1ea5G9jTA9981jgtI8Rcd0ugM1x/ns49xiL3/OIOYgkq96a9KHqfKgK0VIQatoa4cP61b2pvHOzVYrLqHSfqa1Ck2iCnLf2dlimGra2s0GWgZagllm/UeBKZ9LYAR/Ovp38tbSrpGtJTGKqb8zUfC/3sEli2BG+el1m5vfES4SaSP9HhVqsDMBVP9IwdI7mRB6eoJwf5bmeyIck9man+5Q9QdvCCZbcsgjW3fp0VqaZ8+7mcriRZ8O2VVFXiGO3J9yKNYxyUP+CzBczCnqj92pyrCw4MbTZlkV78LoI+gryqBD/XhoM8ZbttwwH2N81ASuaS/z2OS3ARMLwwpSEuTXP4yRhQSn5fmAGVNGzW8Hotm3GU9HppFCBhReHnwHFv7h96rO0yiUa+eb7fE3S/BkOgOZmrzi79UoznBCMKuxZ3ANbGfUfs0AFJbM/8xTW5BogHWtacADljBJEJW51TM3tT3gBQTiLvSkRwpXzCA4rSd62SW2XY5xBbURd5h8EnML+TXSFHwRgfDVSyEqqc9wd7O9JaTpvYeatMqAGVY4Z83N0c6enPLLPSBN+1NKSQXiqfT2VUWcXzmwUDSA7AwiFGJdWpQIhxFCBZeaipT1qEdZewJZDYkLeCY/VzCjaydqIX4gJLXMOccRZ4nKzbjVX9gFeLMkl99GFUWipmPD25RMJ6uodKiKYjclDGlpcjPMIKObdGwFbeag6GeU3RXfI8h0pH3vAPEDjKb0uZA0fEq6JQa4QGkriTNd0vAr+tloSbmBLb+J2YiUzCHyQiDb/zYVHStHykZ2MVORR1SVU/Cwe5Aig5Wnuk3oflBMgQZyThCnCs621u1S8fCF0ywORs/PahWYdpHpNbxYbuYUkeUtifKjiOpVUfLyZ44JtGafSTkneN7ZXIXxAc6LQiQuBBgfa7oli0IDXJ3wGxYppA0orgTQlEA3WlIicR9q0uRnOBnuGdEF77kcrNNgz3CTSft96I+yr8e3Rsu6rDVsJsme2DqGrsrlyt37pq2lZ0/uD890Kvifr2hAr/BG/fkqa9UfLYlN9uULrge4n9sdQauq/hnTZYZu7p0YsRBkydCBJF/34WB6U8K4D5H5qEQZbOx0QuRHemNYn8ogdyEQ3TBBgLrcByQQivFuZKI0rYE38y6twg/VudzPsG1yPc3C3X5s3e9NTnj8RxSqGeTrwVNhRlma/YmZc3k+18F4xT52M1quJh2OKNiJwHT907AM8dbFi/UOwTifee/G+3MCtOexqKTY0tFZ3OIAeVxZr6IKgUCyeGHsJfqs0+eALTu6gFpUFf1Pnsx7bVM9bu7XEAsZedpl+7oug1Ni+O76WisgTtBH3uqzJgO97ykW11kWipN+lMQQJZROGxaSbZRAy9NMDKh9q/0Cqoc22ZI6SXRZFHBUbWfZAzCOTr8USOZO5p8XfGQgECqVOqOE+4fvAr/+n4u/yb1V3NpZOfXgS+wsNRVvkNeKQr4iAn2Xk7IufNXqEMHYV11wRYGQFia5teR4nQfKCG4k96xda1DNzCHk1hSbSqrLJ9KIUnZN7icfc85+N7LKSq28HEGUINyFpLyTZmdCy1jChNEg7yC9yOjn29yOGKxpy6fBo1CedLDm7v81NYDgl/PwHVPysfhZvnuk9LwL5gdkGyI9L9u9VKt8Kg2afzwWXnWldDyetqloWp6T6MZjJhpSEoEybNR9lq4TTkDuKLRNktV6AWTUpI2Y6MwlUehYaz9L0awAzUmHvy8o3bDibXeXd+AfWc4538FU20FNc+lGVVeU/InoFu1u1C8OhtKXXovEXUaDexTqYC+lgH7SOxR9zBhvlnupoP6HwNYbDmzm5UiCh4BFlD95nw9sgT00ugsowJY5hJSgxl53fIiRv6NxF4ex1xMJhIWdRAeovdbPOM7++SRyno5bJh+ki5LXkFQbrGz72WtsaNnvCrKnQVFB9qEwCZyXQEtV/Gr3GH12scUF/y6J8UY4+0u/WJuaZ9hVtzhPFs1zZty4Bw/9UZK0V5FJhKAOXRlyqFlz850U0iJK5lSAifLPb67mN3zvSR6yZ9+3DxKuqQWQ6rAnQfRrIZGmCiBKsHTu0WQdfE+YJ+ofn2YBedgBJ+HrUX6uTN8xD92eQL6aZgfpws3pP2Hfs2I1z5rKci1N0HAlqU4r3q+lRHoPvsPtSw9/mszAbfNE+Xv+Eu6w03Gbn5oQKX4knZW2Lhfhu8wnkEPtGTpL+LcYwUavnak11zC4ul5/mC1pinBvZR0HyKqB2ou4/H6S7Yq72AVH0RghbI9tuKd2hvEOF26bu2GYqS1c+DY2BRkAqKnPkH/wyf79IpaqYXV2B2QnEVEpC9VcjN2Y/mf9XRc2KAuq+kF9vuOPu8V04llMrNKRf7KguQZeyTX0RHBSm5hNWrRd0u/3wNZ6J1uLSPVQWuz51qNfKkTTBobI77xG632O/clknoIh4qR4CQgcsJ20CYxZHfhKw96h3AY2Wjd2BlaN2hWi+TdaLMOKjAKd0y4xeJUrZ+7dUm6j03fl4ieAEEn0qCGCPV6wFj5pdavRU4xpf//6l02UstZxRPWHWVFSVsn3ViDVTfplhy6JM9tjvSNb71bK63bzPQeVmokPE8zrw+3uGl2EUAXapsr9D5MWwwIT0Y0PEB7/xlTcGHZXE1kP53WCZYD/hUoBgwrKvEev7yAoLee/yUBjAYBRdNt96xrhoebz4SV/kNQxs9aDeXi8kVeJCS4CW79VWp+jNnaC0cs5u15QjkYnd0Fh/JWiyeiXBhTGVxmzboXgw2vSB8hT00yfb2DSfk+WRok+xGPuzY6zOJQfhn6kYHFSZ/bRyL9QyHUk2/u5zPebISkAsBUOyeicx8yhkJQD+QivJ8gFceOCvQtH1JRhtsJhj2Xh2a/N5cTMasnwBSy1J9epH23ZKLRWjbCbULijNa77tEp7v5DJBVg5o2yuEqb0a9Vt8unp6mbnbJ7P2sdb66Dpv67tKKVvLlysAn5zd+ezt9qZnr8G3PF877rrAPEvLPIC/6TZzX9tzlmwbJJHXSL4qLampaG6GETfxrkddVEOcszvn00puU71cgTRO41zCbyi+FomdEMd0j9mb1+9+7AhLegNic9eZ/8bueVVaw4leQh/CqXdOisjoSxXgdmQ1YcG9R2HjaCu07HtsSzwCnssF3tZc5BGYPwN0IpnQO9nr14DeRUgK+yYgw9XVUNd6UxtK31N0XqXxLo8WUShxWJ5TmqH4UYA4N5ZaTivkniuIujxosr1eF5AywSrxSNdkPPoZdv7Tb9DP5DYeIKV9MtX/sHXI/Y6nv5QPTQk9OEDG+HZ3NRw8yt4YRNKuroF0eXBbnro6jv0TGe8X/fzFBb4Le/hRtWjydnraAzAQedl6bFsfO16c8Hd/ZgQ6wIrw84c6AuJICg0V/QnNi+6l0F1ERjHMELMT0K04owex8zCaycNjZ9LmyTy2sA5eC5j3XB80/3Ov6AIvUPp9KMw1cBxXmPcNdWQZnFBgRc4/Kgt17Knr9Wz6frDDljjcqGS6LqJMcZgiMaABYhRD2NeLLFNP4z33kUvwYwGQzmMifXRSz/EqfLVBpMC+1vs20kLous7exb0YnrjNAL4rQT2N/iYnE8AkEofcUAudUSPxz3EDKvfCXqxMJMtxCKw9Fu/iQF6c0ytztQ+665v+5i7jpyDPV5FnvciHHWYvs1a/0K444vUpuSPvEpyKOrzpAPZX1dZh8HemXk5kldT2vx0A6sv0COXxsDN51bmTqFJrLZpjTcNF7iR1LlgfIASUr4AYunT/NnbcGdZrtNG49Vv9/Os3bq/3BcZo3rGA4Lc/lxIMAVKzhGxZ6sxZfr+LqN8/Uk5sXUrG3PVvTaVjywHXw5YqndjCr9ne6ili4Giplvg7ONpct+vSGqixGmBUe5KHo0Ef1j+ZU2IKjnsRrNcnCVepeybdJhydcSzucLwDjcEgZVnJiXKaf86yp8pr5fW3xeVt9ZYRTPm7vhL8Vzs0BcV6DEOrvKAahkcP8HWcojCFwF3ikHZajG6UqL5BK02LXXmZkbjt8hoYhIZPBuY5LiATSgX18AKC4AxeZCVfnq4wdYnSmt6rr+Rs2cEgKNArIaoCypTwaoLaK4U7wY5NBcwj1rdiiXSxMgKm4AYmAI3/RsetRiejPPBbK05xYAI/E2Tdln7s1CDfc5xLPSudFwq7ayke4m/xjWUYXXS5w1l8ZHvzIVYVsELaIBxF5yCejzRhRdhYMQFqllqtqbegarkapk6hUAFTCVB8/eHnZBuLvlIhjcNzaXdoZ4rLdMX8VCjX0tUaBxjYoqCPPSS3mq6Asnf5yskj6GJhu+Ni6l17zLUPUt7u3sNokHTvriOPQ4zF0tvDdznTUy4r3pV7tbf+WMtBTCvQ3z11MS/KGQqGEiGUBNbUkdK+9UyRJXOzFsJZs3vXszJNIimVvi2vryYTydUaFW5BlHC03n4VF19m+4VW4nn9oJHf2VzkaiUzhmxP6K/uZXxS2jM/HmlDYVllvnf2z84l4ld2UmIQeL4wT2I3vZK2WEy5sS69KGp+2oP+Ugtg5fDmx6PPDyPqGWp13frJj8E7xuaUXn8ISAR2/CA4d1dMLlpX5g+i3qmZ5nm5O/GKHW+iPUGRn0IVSnTg50dRLuH0FnCwGQwntCF6nftqPDPo14/ZCYbVBpncoxCf03OvLLNM8XAUcGX7Of5odEW9a7caB+MZ77KMOmH/kw6M7gTwcIfkqPut+6B5uCm4Y2JCHURv12zbxR2OVEnZlBbrKiwMxjyuWcED8rt2zReN8hCCw7BwQN5oCGHNM9tRCUzPIe7St8OSnaJTL+d9dfIXQH2QNii5EE35pVmLfvM0KgliIGpdSD819q9DuRD+/uXrQpuf8YQQ1MpBxxagn0dfSLExurvnoEFFVS/qxj+RvSssBPsAiwcpBq9KBDI5j8NZTTV90bt5YPEUqMQau/zXVRIgaNNtzfq7ILZbyywwIk7PNwK8X6mq3rilVbT54zbXuQO7Ce1Pts7jmz4tzw/LxKXf7884dsJUcLUQS72L/H35o9XH6zhBnUtl3/OoW4W9cEKubvOjzjLdjz7CPgyIlI8Q5M3lpl6mKs2NTYZ71h3WIBC1Rxtj+t89dTjEybpEAugmNvumEjdgpV97398w38vPu2B4d/xbeOY3z76V+ca+HOZXgP6RBj+jn4ZrNTA14aKUd2BTCbdPFrhMoydwVh0aoT5aoNUxt6QAlSNhW1LxkaH5GIKPzF3EUtVNh/oUzW5Z+wByHeszpgKa0AUKNn2zxFyOT5RlQzqSMHhw63S8Bujn3OF4T1V9H7lSJmESDma2VPiKauL2vAn4NSmyvxay6sQ+D6X8TH+j/Y20AWQK7V9RzHU6EV5iyEoaR1CwdYADoG8832t38th9Ey2q0D++yG7UZeftDbogmOwbR0n7XqWeTabdjsvrrijlmS0kMqCH3rdk+chTD8xw2NwY44TNcc5y22IJKHjPP3MwCnciBSAJrLahHDfPLw/43rU+NV6K/pg6BWbNHWWZE1rV5O7ai5CQ/2DwLiUszZgqUl9jOFazpcfAWEvwb/KtCJ0xjSPDruCHu/TT73C9a0W0GsQ6O9YY3k7u5IPhvdkaX6LVeBE7jZATz0GyQHaH0z7BvhaUf467CvcGOlES3CwKKyjF87TyuDqG8d0A7iZc0FERGC1jHM9RqJFmqwEoDIv7Ujc0uujjeYxMyO+bKMGmeskHL3f+2TLG4kZMDn/ui6rPSpEZhUA74u1koJrkSxDrcNZ0hfAJWP73594nbW0hatZyD0UckbXi9mcY+mvAiZ4GTyXyqpH7NpM4KZZ5Y9wILASpAwEDZFR4nVE8P+S1GGgfz7bx3b4QhUuoyHygixli0cMGhCL3ahOn5RDNBfiytWK8zyoB6/EC6D/BlkmMXjfFK1kFzvxItJ//vLWZhEuOrg6wKzsB6+V2TsHqpC4JEOtxb66gvQh0Cm+cfXetZHXRXj+VOvNdV93sinAKwZ9Ck9l1a5S5Z4umFUlHkAC1xOAUWZvgI2FtUz5LtfDlDWiMx7u97aDpZCNxK6RjWmzN12LFm0Fi4PITQ+f2Lc7DGnTqfvYEEi/F0EUaMMi2fUjrwtpYkzrcLvYnhm2JWVJnZtaIKGyhnlHCM6kd/YTCZ6+ScicaybS/iYN8aHTDpAM9aVLincABgUcpaBT+Rc9MvZE5wIWkn0/CevaP9mVnl+CHt9IcFIgC1zVw+RYoWBoKWrHlXJvI6hqaPwmIfugHub75jlPRLGF7yjk26zWvZy8o1tVQYACg+dpO2eWodzoShxwfMkLyVsU+XWwWUGmSOkjum4YFOc1KU/L9cAfLxh4P4O+y4yV0oEPlqoSho5NwBUApQsIznkYKTXoGSzrFoz25ZVFuycNjcWL+CZvKBpxOSH+pkwqfgx6P/lbWlnfwHEC2dJCAGkEbiQPBOOMWq/P2oIt1KSznJcF5JNgC6dzRB4UtbgkjHmFOQ0bVvr8XLIPD9uvac2gh5vkudnvXT5SK2jOcURNqqdma/AgnKqQ3kOFkDjgSUGR0Y7DIq8ElRwMTq1DEOsAom0yaQb78EkDC2ALCYPPk8PrRvMIX58Bo2GiM0MpIbvsPXhqbh5/N8aJsxIp1JV82SYy/gPxkwu4II5fp+2pcZoRbqkO6UgP5nqvyDg0oGfxOebYHGqJFPemQc+uHknVdX9BvZAO/lboGrsmrads5XzPSYv5z7RJBI5lauQLd2kDtEL7K4fHmWaYz4adHlG0EWveoEc743KScJ47EPdXYJE9w0HrxrgrwZSTEwXxQSYG2MAaysU6ZIGRO0aEDwT7NqwMkl35TWNa9O42hKkNY58fqN9pP6aakZZ2cvoz1V18xvaFN8Wny/dCsJa5Fo/X6viZxzD7hdYUn+2nqvHQe5bQvzXf5b9j4kk7bUFwSTc4ZW64gcTM4gnXdv6nSrr/qiynIZzGKtOcf4hsvYYlIHE9YWzhRwCMf8TgdoQKdzIVfWh+9s7Zg+PmPxrSwmKp0vKbcfSSleo96codmWABQTcbM5cSXgvALtofEmmPU3sUo9nLHkmr5Rqu4N1hopuv8ifcCkgF1GWppQ11rvbdOnPTZjgLMPQW7ybD3vjg4UwsIxlTSJkBlw2lfR+jPXCkOyfzD1S4HjnStmR6qEkBTatgdY5ALSTgSCftJe+kw/yf0Ywobsr5oylYxCdPGlRW6S8Fbwytex4pW0o3hY/HS7sfVMnNbrlnYr8O3Ir1TqAJISf7vY3zv9a+MrzDLbXw1r2fdq2Q16KfI6zEyfDyUJ6uHMzB8dYCk73KtXV9paChsbXseyo9s3PNqg6pb2qC4d/Uw/UO8buKq2RzvyXtShGIuuB+kqgCO+U0vTJmMz7Q9XKPUdehesH2eHInk6aoGGYI/HhUgQ85P5HcK0gQiofrhFxZSqNzWHa8j5t/NOihqN5b+Fqhi683cdEX+LgZ25BHhCX6TjZjQkZWDGx3yUNQ7EcgMutyOm74HIf9NvOA140b5nM3G2szr0iCPainy0njSD91QpNq7k5kLeZLOYjsV5bE4KL9tnF48WSR4ydXUPP8mGG+F1ngqTPBd9mJv59giDf77S4ZhojOLAu5IcsYfGwKxwwIHniMk7h2Ba7G5QjtJSPq5Sxut/6Rs+dCWf+wCB5yo1fwxWJK6fvHgl+rrr/2biYifiEG4sRdWCQv1pASFsEy+HGNx1vw0v9xTmMV262lpFSno+M6v+S8zeJb5hTpgczlOx0nIxPkV/Lp+zqnZVYvDL2N/XGK+pW7x5H0Us2bVPFIyb7WxY89jd3eAUvZO4DXeCk9DrCRoWsNd1LffV1KzHL0skl+ro1Ffav//zPK2i4sTnno0p/Q6Y6qwfBCIz1K+H/erEoQvv/DMSExk2sHLaNlHYo5G3fMYvXjHJ4SAkW3qWHySfp0gxHuaT1Py8V6nYMfMtfSvjKyJzFkr3A2SKw64mY/pEsLaWxJ7XbM24QG/Ou/Hk+JH+BdT92Va1O2/f+1zB9ki5f5TZEROk4EG8Qz2L15y36gk6SFmYZ2cB4yVZ6xibsyXHbO49oXG8TTC6vJ5XUnzaAtZL2Qve5BAs/RTDTz9yshwmOvG96OATJ6BL9JPoac8oX3katosDtErUhVRMfJJumvb7tnsgtA1AXrcgE8kwbvtwIbjNC58o8eN87x6H0/cl2voOvYewXniT8qLLOXd66SvmbhK3jENp384lDUZY+NWTFW3PVBTMTTCFnfdwnet5bTHzK/oawPISpBkEP1Y7a1EBsmyWr9G11GiBOz+LLPWmkEwhO4gDQwT0QfJZ3C6RUH+NZf+FC26gKTTQXi2LHRUO1fkZEVZErxeVm7iHMvsRNleOZCStXUJq4Nb4yla3SGrFukVDyqCpIaB/iDzchxMsxtrYSfL9Cc8PygyZCEQqHQwE90F6uMdblwr7335g1M0qxlHMwYaP8lKL1ngdpZBxFYS31pswjmpmXZhftGCfrNdqRqAysUGhvLn+EDqDI02aCgeK2TPWBEArKuaJICIzGROx9MCpXEx7T+BE/TYbwQYMRbXGzH0S+iXDR3CK11ixlllvc0NR2OQxORRpD0QO4YGca+Mo3vpJWJNE1gTZL7K4J7p18PWu9zfyTo5X+CeVnSR9DY0+JIwP4sgVhli96wz0T3EhMlSvcPkTme2Y0xpG2iIZB2n8oHUHPnBUZ41ER+9sTQfs3ymCweXTzm5W8zRnWaNMbdvoUGviaDADSSBmixRRDyvmqJJmeH0M2I+vvVBctabuK8WdzbUkzifWHdGHCDoyLnUnfuRz1/VV+3uzXWZ9b4x2pCDA+QOWkG/3RjDvwVLCqSd5QhiSZ1IYcS3sVPJLsVKYoO5Py5/QBUGM/L3hVnXEa7fkH1f1E+wEJ1Tl1RzxcdhXg4BzqRtoLR0IviC+I7vhosZxc0jSqWrBYO2dtF0RDyHR5NmhADSpfQlFdESW2FYlvivO6wsNtzl1N6Z/52CeeptCg1OGPUooqJUHDyYlpQp3nUSEvvXOAe/UYnk/b9eKiTkqAzT1MtNg4OY1YL9+1in2BgK9lB58llcsmvihRCg7UaEpRZEMNSYn58HUGO9dfnWHr6q6W9nVmDhp77P1DjijL7+F6h/0Vk9vmab3bxmxCW9hgxM3IsUGOPXFN+IBH/1cisZ8fXIzdJnAMTRRkZ92NiKF0qZC7fKU5AQCcwbT81tM9TQhI+OvBz4N4MgZzR51TQxw7BBXgfauByCKScFwkY+lFZ1khacFF7vMr4lzt9ypIDrFSZgXMHdNhhdBX4xMsuQekCOtStl9FeU6sG3QNg1zMQJI0lGdbCWGLyXgYoyMwhqghsAuscfnxFA968xuRFdhR1K2qpuWqP540YxRYq9a736qsLEd1cUjee/YrbhoUzZZ+c6D/sDUZIlq6Z3l2XfYcpvyZQwq+t2IsJWeqtLZZaqcI1Osz1MKqy7Fu6XqxvZ2EExdCODEiZQF1xKsB8z3oHJHO9sw0xIKbHKdSNAHRrzKT0Fc4/er2egA6FvvZdqo7miugyApoiYZFKfuDkccrdQOKZLSPJ8dUfSqpaL6KrtHVkwFNq0W58WF1Imf983wsSNx01oFUggben1uyDca27zAl95tvh3Cn3NAp3WSvvLqlhnWzPxAzTcf1EbP+KoksZ8/LD8556vihnXeNLBDy+MdLTYzWpBHecP10tqvbRVb/6o412OwtbUGi4T4qcUXP2mZVGpWh40LFCxXtFhGf7Qk3o9KkV9LVUSpGMm61w5YYlqN2KXWbCHtmBnW90TUCg1U+7q3WjkFOmjuD6Mxy+fSMWvwH8X1hy3mZr4fv/yXMuzaLUre2foh5MrGyywBEUBcK0U3xC9ArGJVtORyoZrjs4ut9RkU9S3E6w1UH07pslTiGGNCsj6gMWUcR1f6Qs7pkg8gBMEZ5PyoNNyTO/1gZQ6ifStiBc+rG39wYwCHmbgzWXD3Hv+ar0FHC8FoHm9qxSsgeNIQxS9gOrdAlhvbLZdlWa76HTXN1Dm/PbGN92DRT8sHcMSGQbaNsTKM4CzzHNbkKF+TdkYNjQCapQHjvIymIsciw1kZc1gNKnrI+2DN3vVbGFp7xCKGijbvgmYeidr9Ue4apav4ECMcL5UkWDuC8Kqm9wYHVpnMz3roSBPjMJcfoUeHOgLkWqY3GU+LKgsL0SPrxk0mEn8uPxKrYxcH0y+ZdNRGXzOiInVIHrNaQvSqYOQ3Kat8yhDWZVZOArc4tRnCf7yfaFaCnryu0ML79oMX8OUGxu8x/+ixDN55MU/2ywe28pOtC6A2Loi+ELlj0N/jjnUKQ4YMPVGcX9OywA5jqAtb0Uo5KVqqvJBkfsNTjEVxxJb3ZRR94HTcLMnTfFFDl2N19PvyEX/BUEFcenDBZyt+ss+lv3tUBqiQH46PnlwQ4e5ARzGgwgNjZp/MF9QUEO7JzER4I0TYoup+QcaAU3JIZeLZ3fruX4j0DV5ieM+DFMy5NQuxQT8AoprxeyzxF7E8cEGPptytoVykVicu9oGZNUHM8vsaUjY1mbDiblvFPzNBJcelpXLaKm0Ec2sC3M0GKrIRh/GnqAzlHjI27HWPfwwiGqi15iOVf13c/1BlLjOqcmHC/iXh0nwS4rGwT3svWSiDuTCuvx/hsIwYMXK1TLoCc70mVL+V7AGu+Xv1FJRi8PCieGkyhyah7juDfBcRNTV4hSWQVfLg4+fnqS+pRG9cLtMltGnlSDUl2eAf1TAzVOiqlNrKX8SJY+0wXVKGkIpxl1SZtlWp5j3WPivPOjn2ndj474u2N+vQ/DrBcDaKmRjTEXMPoUuHTdS8PK8vPdYCKREEP/Y5drPc69ecYKBhKliu+LNaQdr9LsRzZAfvxWX6YAQBUrBLrduxk40lL9UiM56oe/MYFm+y+X4aIxKC5yARcnIigUr8Tf5wa5jhSrq1LWXlgmzD5RgyPAkpaota0RtCXdrfoNCAkCjT96DtF+T3hVz8i5TjC2IsXAm3dbWk1ep6fUa+FFcsL4AIfvmVCDaO433l+lETQxNj4CtxRM+ydFbYr60PqE07/bZPoErnb7spUjGg0BsdBUvnQnl5GfH51YtrVegMq1ISQYWfldyFtQUIqiTvIV42arvFt0GaAJWkTV+jRAKPJtM9ubIfZf602CNJbwshNvyO/RS+ymZu4kt4ntVU3sdRDnwUKVEixJmPRjv9fNWCTe/5QepScEOGQTO6cwfMr7GO6Rd3IdLI30DWYuWC/CXA6GmsmM/KGdF09NX8a9/aoNZnWPsicmL5D57bxUHh33nAAt7H6VJJa6KkJ+BratHEorpYSxW7dmBhtd+YMd48BVPR9A0MVZv0GFALAuYmsuq4BCqgd5p/9BP2TGAC1Ch4ro7kEJLfE73IF3iwPUVhB13wfja/sDeNmuJZcv214NmR4dn9Wfqn+cmKxHx/v0ZppqjOuwXUs8AgXqtuj+oY9SI0rvRAe2Q2abjX3MBJfkr9JZqETGDdoswnzSV11g0p0tvfwpFK8eGuORWrjAl+yjKXTbJViQnOJSBDtk0NoGCdmxGY9k+xvgqLNibxjZdPB82vlKy59dUm9Vq4Cuty+WLKn9UO0KzcxhwF0bbMdZtctCWMNUx6tf9BApbR4h8NT3HV98ZastQIoC6yp+YZqSDNvURVorgBj8kCkZNcvFwhsURc0GWFglEchmRLunATk6TRdPGlb8E++FPFGGgfRTLFydlXDmlQth+4pDPMm14/GCzfmX4q4Sv39N25TM2NOlYoun9GjfNErCQ9+Nvus9L2nuUxKgACEIVgcnqh4gFcfrvq0Seg5YiQ5ew30xXvhbb2W507Zj3+za5GZrEMtEe7ctKLWi1f3gcc/p5Mve1stfdm+DY8IJgP7mcWWYvidOG4UF2+6afnFk7dHG3wvC4ZRL0v+hgvhhkv0Bmvss2nkA8M6et3GjkI1BwHICYbtz51Xnz9ykCDA5jZQ6eSkyXfqVgew8I3v4xeSraoZUP4EiIMVZrE/fNppdCylW/mu82N3xl+o5VhqL+kNZZCbkbu/HGBBUL8DxktGhTbaLk+jJxyY/ORjkVRtFDFf2OhFysnyp/0C9ugJK42GG2kFt4bg9sbdnx7eVEfDmhO7u3kU6HQhc6ldDxG823hQxkNbdVZvG7ENLL2w5pMUnpO0LKkN8IaleUpVuIjrhGsSxLxP+zpDoWQ2U8+Ekqe2vDA2gMcGluEIRdjtcegp8srfr874YI7tTMtTBQV4edjuA/dxQkK97dhaP11hpO1XiAAWu9nQsi5z8szOjF+Bo8So4T8UGYuBnwo0qFC2qOYQmfXkRWU5QlLH7c0R2ZMaAD9pH/Ph3yDr8fNffhu1pDzalBJsuXHkC7ukVcaW4c3le+cROxo/0o5SABoehAAWC+ZeSBDou1gu8xo0TF7hA1LPrxPf0KIPcHaYvpO6I3sOZOLpbD02K5yqkGnaKKd2w2pGbxIISKL96IlOWtb9NtKjQGm3fitP910L3Aj+JJY4l3HAUKszgSSKyhy8hXA7j2tCEzYAsEAtMkn/FHeJdBTRO05il/2Mrzx9wH/XQH256cDYhLzuNwSmDX7bo3BUbP2tHo+jLI8wxPaFsEQmwVAOjn+84vqR9Smy/qHEkDV3bsRsmtpFbgFhipXYlPWJ7rwEMx988h/O/zW9aD+ujrRfbOv1+6zDXlmYr0HhTlbE/RNAak7qU3wbWDqZ3GM7nsAELfFs/tos0cN6hFo7W518ZoeDFW/vMSWwI1NUbdKeW+uoUTTHs7Bd66teU27iu9gIr9rsjn668jhy8mUIX5RPDPvNqRqpPnE0GSUdHDJiBLA4V5pfXGgKkL1oczlrRQ426Vs5bzdIwE87JUhJL2BWbrZK19+HccNdLdvbxfVlP4sVlS4P/avDRmJ1Lj2PC99bkyaYYi54excA1JizNJC6SALSxjk82m6xPhcpTx6FS7le23QBUBxDvTzQ15GGTMnMojQnXwiwt0rEQlx1wmqTYwJYmR/parQxryioApaY+8XQJhtAmDnBqEFHdyy8E8nvUuOGwNdf5zKmxX3RHcil77555OSr9xWdNIe0f04C8jN1RsdJVtSBP/0R6C7fO8q37zOrgQfghXZdQ3t8XT65nTTleL5zZcuEusxdZ6C90OFQHWr/XGU1Ic8hKg+F6ap1ybtDP7lzmFchLBCFeKZ7cQ7AdoplCW1fzWni7NWe3kF+TRhVdDHvrf7lApt7Q7xdN27t3TaD69JKFwI5HsA/1rbefPTNW6bDlDPGXINmbz9i7vuFyx4BuLa7wg5j9dVrlbr0pKC1KcgnnxBUDAz94coyq6Z/F2YtetOWrbCFI1/wj0AUXZVACbh632sgmSA6kg5f5WwRUpx0UqCh8vsYImXiEJZjMcVYb3PSwBa3qcRSVVr1ufaVuAdjxnKrMW+ls/U15wA+wDs9tlXtZeqg0KNZezeSU4Vt38+nqysn0A4L1WTHCWP47PJiBJnegIVpq71LH/Wmw3YNlhKRSrdWXnl/DPmlKuGchBKszj6trzGjt8ChlYNGGzkEtObxs0aDRCnTBlrXuCPQyBPJtwD4jzietszVAtLPXGKXPSxOXXV7zkr+PLyk3Z5JVOAd1Y84s/edMXGP2r8YQzQd9S6o99EDuFm++mjVT5z5xrmv8BFj8Hp/72MgtiQF3Ic4J/jyPGbTo/PLWjjb7Bz4gG8mV6OfAtPA6ajdZpcrvLAN2E/+1wHKsYmXwiqMwxRa/nj9MCFPxIxWdcB1UIkUg9upUza2JWeBALzkWNKM4IiNz0nomX+s0XVqIV66AT5elIR+82nv88d/u1XOYrsD7hWuKPIN4EBCW2zDP292JIe2KkUfT8LF4dAJc1jlA/a8MsvINgZV0sbmJgcVve2K+3SZN5zBbz8i5C3OrW66Hf0xNB1qwy0UupBBqJ5pOTOxDhIexMmSFJblOtRhAtu+yyqkDJ6AIlVp9ccu/9Ya6JUVlMsNCDhXfTbzAKYY5SWXnZXctQjIdXgR0dpOx9uOKgUUNC2Lh1tf/j85u6qrt6n6g2QdTGb5MpDMCurvGR+u03ZQvkdnFdIgBb0BrvPaULoHVaf/KlO/r161QupGT0ZB1Yc2xud8RAiY2usSt1+A+RwKqUX/ow7u+nQp7xVfAP5QmVXaIGrsNTYh0HqjXF/OBv7Upkf0NP0miPHHQzN9sNmkqGx+KdmsLw4D8jyEEX6Rd/XXMhFnfJn/0bEC/8SiTLb76m8obLVSjc8IdyS3KcVkxmlQ+mZgn2g0l2llUql2FmUEwgVm0IKuNHKPCmWzM9uP4sNg4lAxOaAgJqZtyMjmw1U6PFrdjFqvAxNhkombtqUcVF7fdtYytbV8S0C4rPEqmmLr6C+9kEeL3K0bm8Yj+pOTeKM5yPVkJ7RUHcz97ttUy00Qji4z87WsfQP4lTOtZI6nQ9xprG0ASkND3ztA/GQYbx9dHoFxLPgjNZjQYWLV0RmrH0XGeVH1h/Cn624GaJ9NRZlyE8ZVhgYPYRuslpCzQXyw+fnMK3vBipfRfO+53X67ZgbrTCsOFwbGpM5rcjs1rfyYt7+Qq8vpss5HKQBgEvSnLMeyHsrpEFeLgKJnPWU57LfcrJhC3HqG7y3SIa4nf4AM5NlfZhBeYN9deFavRlRLl2ncDcQkCrCdO78s5JE85nRT0cOz3Pn5IM0gQHEBibXzhl8t3Ss0/kt+B+wuIO0Rk6FzxkTfhihIXTUXP1UMNTrd1OI+IAkeRXEQGEgWdLvIgjFCyDfbW/+ro3nGMEeWNBLuZJ83lYuIvBOpUoPlxLQsIKC6q6cPepH8+KpbfFZnYM9u38fNu0S+5tfoPDb6HoCetPPvmTM6RiZeni2Gpo0iFPwk9vwxJK6pelSVhJiDrOjETJcjb1RvLOkQ21Sw073FT2uQILCq6XWXd2iJM4VVQejvdqzHcYInPIkDTrib/ALX+8x1RiCyPIY2o+XEDbIlP7KLhf0Agp3g6GCO4+lZFky1+4h/zB1Or/UY2eC3FbPGAQpQthDCgSdYFdt3PRfDYvtkw1X+CMV9bcxft2H5b7rVKGD4nbpOdH0siZ82hb9Pk+4oA759cFYF35LSNm8JAyjk+BmJ6z0LeIhEaFY7bOhSSTejhak0PcZxXyqyPGDRsMX3a5ALUNcCqyAP1DwvvphtUwL2Ry0BJVFEBDYFcVXGzDCS3Frr9RrBtbUT51KM4wkvADbZtdjf4U1hfHf1e3FOQomTI2LrE/8QAeRKmz+5yCnoAq9et5NPWj1Ky6ghoYMEUWbJZ77NQHtNU1MCzsS5E9VR+pgML4aVvdcjcI+A2EsuqlqnGbisCNCqiN9BuJGmHeS0WyXDP/x/z7o4fN2ZCn9XhpAjLuLTih2euy1pRq0WQib8AgTmKIP+/mltfIR0RgmiXOh7cs2fFlyauxLtaB5dg7XGLGIrhP7uZp1TwjWS0BiI/OlWNaSvH/C5Gcfq5fvz4XLEsVRha3Ak6811bY0fjgpV/8hkGroJnudIlhPJ8dQSEVtU93ahP0Veakh/EdWmh3XAPx63nUT1gjXL96cvsPwo7H5t1LdZ+X540TNjw9eYa00oeuOLyfz7PZSMkrBlESXj0Q5EwLMp3VXgDHSTauy91LaOnLIg3ZW6A0ZdFCLkcZRX/KRgvCj2dxQcjzf48BGKT/ujZuArCY2T/+iA3nxZXKORwlfj5IQeFJD7NwAv+EuwgUpigPBF2AbjRoGDu0ASJtD49qB8ApT8bNs5vFgmo3LO/KDHYp4RtMB8ggEcP5xkc2sWdFBiVmV+HHA8M+c4oYDWTYGfmjX0BJXlRTPqV3F197q5opD6JVDw0pzMug9foQO91DZSwxPx9AhfewH4X4dV+vzzDj8OD1CaeZ4rhzz9aPUs6MMFx1cDfGtRFyQ3+9+uNTRuhwU60uDfhU1vEapr9tEx/GrntPN0XNIYAb6A5gSfUmGwTSN2GidqmV9y9AYkXCpQD/tb/uWfDCqawWaP6lbmbQvHkJ1A4lGARWZ9Y8tLAfyNFB/PMNSou/P4QBWAKbuzplcbDVLLwreDJy4wxaOxGFyru7a442yNU/VXsRV9Pu7TvAw0+e3hKHk+g5QPHHP/XxuFp7JX3hKWT7TZJvH/YbYKYiroGlhIvxdsFQttro32RcvFk2DQ0kWAguewE7KPDSHCaSH6XydywpSg5tgyDd99nJAD5SyC4GnZC9uXrDGqZ+Z9xjHzoYwpGL0+uWHbqiVYpGbxrDQ0s5uzfS/im42wWr77LM8tATQSH/5hOSm3RissW5qmjfbJHxw3qDqiBpScG/3xKeE6lvuMF3G0gdfUJCYB5QnaOR5oFk0SMIO7PLHIYKmyLWCWmUJdjyQZWNy9KmUHa+/zCCT8caVvUkTIE9E6vwOfOrBTUgGSlViOfF9VZrvUV20C2+3Rmh30tshqumcKqxLLcOSFVLFp7V5Ttn3i1Q2sMsPpkymE3J5R7uXNkta/fMmVF9UYDJuPWOHX59yjUfIN49YaSnfanyFSa5VJqFdVU/kf5tpCfzMhZXrqbWTGhg6V+r0rRxuQqRXPttvj2zIJzlAlD+AQR/U/JJ7z3xof+o5gD0lqzR9bsMGvP2iLk/q63dbljL4rm6SwoUNbP2q7xGWAJf1gyrnKfrX8mXQEmR7B9xvslw7SIvy+/ssQxUEQMAZ7v2S6HD5xA/pBcERp94H0gkeVK8oDdKCKFlK1hc+NAE0HSO68GuY5gTbGSTQUh2CjRzg60k3yVvhcPtHXt64HKIIpZ0eHId+aMWJpdpJ1YIv85fAwkO1BvifDvaFuLYb7Le48Yetzl7SIWYa6XhnvBp7m/MslvGjub2svlYUHGynlf5J90etQv4syjFc7XSLMBB2EvK0EDKelB459oJzZ6ZtU23yCcZu2SAuErKnHp0d4NEipsMirrdu7ePcVDThTkaIYGE2pvagVFJzawGpiNK4Lr768NGPwFvMVBYcEZ9SWHzON6WdPx1lJ9QIJkZ3YWNkGxu2Ws0P2WF2Ij4YkjxBvQP3uSY7I+l0InOvhARJXTf/lAJaQf0XqQjvjl63bZabjl+ZccZSGX5Fn8zMTBNxINk/8Rvb2vPtwa+j6EbmP93QNz2hpMMJHdAygVkHyiLya2Wa/lSfzxyuWvndvKDSvu1nuawuJ0MGmvY0znddmMZtlIOxxBkw5MJyoAnEFD1qhUWngUOyk/o0RZ5WwFcOFPc3zCM3aSCGcUuTiFN0B1WckaFsPiMBImfTTQO3jxUZQLTU9ROi4jGKmaRJgQeLUPcrEDxukORy2nJNZtha0lT+HG4qWcs2YzkEg/p7hMPlzZ+6EEsKq4iLBhHMuGMupn+MGChvYcpANq5sYkApkH1HECgBA0wu1ZCBBQqOpvqAGSasLADZkuongxTOjiE28Juv5io4VSwn9GCbWd0IBHsePlVn+Q8s5vOtMt/6uJoYm2YSo1ZU6PyLNsE8De0bHHvoHc1wN7pB6iHsmeXlnGOWP9Xdp65JuzrTqRXVSkODVczfxXMu4L5c+jiXrzNhS4s5SY+gfDPDtZ5l496kiEGPpJzK/UjVA26Hwolq11CLysOu2aOXmy+k6WiguO5+v+NAm1DjBabKMyftw27qAsldZDEWrzQsRaUk/HTk1YIFT0qgPsogmOK3lgaTO6TZQkU99w1WmaC2zYFbBrQCIo4u4PE8raIKJdDv1F+KCPnEsVuPyTKEYILBlxIXQSNojrHlEB6bHvLxv06j1yNzT7nkitJwCzHMIGveh99sUdJqJ3NH+HBzE5tOxOLUnnCIj52LvrZDroeF0DnYBqa9dkmBcKJy18VK0JCZe/T9R1hoOkUTR3YRd5MH7/uNhhydDxbuPSjl/eQmPkdPWub+q4WrZ5vvvhFv5RmIah7nzgGJzPTlgIggjjMy6S5qQ7BkaLEnV4CTWhBtQKdYZwbYniZSNySeHc+nadVeCTtIVU5VTez55BOVKn+3KUnDjbw5R+X2nddH9z1xyrxDf1Wbpkj16IAmACXn+MLemXfd8qS1A2E6ImGuqeOSMpuTc37iE9YDrs7s6dARCoa7sWK+d67r+jrPnRr/PvzC+ruSCuQ6e/OME8pe5zEU9QLvJWQf7s/VL7P6+3lr9XX2/e5UP4w3u+B41ZXQYOSmg8G39B11Bt4JZee5B5NvR9zL1Uk86qLBy2+VWZhoomC9As+r0spHu6yfWbewWcsOdDL4VB6BKmoPE5EN3/uUEYn5OY3VOP2aGkWC+1uSe1HGAgCNhKxLePZo08gKTMTHmuehhMlDYBafLGgHpAPy7kqQTUIAtMw42dpr9DCzlWcb7qd70B7/QeV2pC7F9BeYDf5zdXzz6sUJw3op4mxigavWYvNKwQcjYChGZ41Nej5vVYaF6t/RAhCR5dCKqHZO/GKGBmScJcWI6nLnuRjJLlVrpR6AxzzcOLMhgK0edUwtOPphv5nXxpEZpw3uYMBddd5Wy2tJN7q19YTrj57O4ImDD/f7ydcI+soG77j6SFZUq5fn1lwadpVIOPUr61K9PHguAzrray1pYLgT16ZXOX6GBFBRri+vWd+AKHJuXPiPg8SYIauCjH3TN8r5t/NkZIzcOB1HqDBgevbhZ9z42fjMPfin4ugS5N4sR61/3z9k1yz4l1JWowWOy89B8I1kEg2TPax5uxchRgc2I4Gf5BV+PfozuJ5/sRseCNWvkzmB8/Ik+Fn+x41ZQPe+4+sQmMLhHbIqsrApY2XWkdPfvutnOr6P/rf4/YrW9gMp9t9y7DAz54acitOIfTNZYRYSrVHk9/YmosADpUe0qmlK88OJzDhibcQ8bO6or42z3dftva4gCqc8vrsh0aubJ8AJB90+y93JnNKHWamP30smzRgGjCmkbWdgBYkrNa2uOeHFI064aol5SAbq1wM6fJWHF4EVzSGuXJV6GM1PAmds7/Ot7meKSvV+cjIwygUfRm24UXf8rOGAy6n02z/ksQDMcSbd23WwFv+9EaxkVefriAD+ZC8KrSRFtfHbddwV7SUYQCOpXQmB03oZRAgiaUhAUaOd/dj6XdXaTz9yffrEreKG1kPDB31T2qBHqqgG3jgaAobV9zjGGOKsojMzrIdnNKHYQjrh2AE5GeZ3P5u1b9p70IqU7HJhHklVgA6GGv6uI6kVNvhsxd9AJSEnwTkLQZ6vCby1Iypk6ERlhD7T7gae29X0C0Cx4kSWf7FW4ZBr4q3ZdyF75u27LrUy4lH7coTLfGrNlcHGGnLxsxuiSt51SKqO6G0I17F4LydVyms+Fc6UdWg8NP5aeAVuFfkCo3BIFyjcShWxBRmDv0RMI5B0zjPpTbP5MbyKLWIK9oaRTjEJlmC1HiV4nWR2iBxEv2lwoVk8sj9aki8iImQY1lhlU4mcsDFpEBNyRZTdCa0baeprqIcv/ubcKllSgccfyZTM5PG+TvBkSc7+vvHxRu58c73dVWRt0V1gycywhwNd/hCW57FSS+KDNIi94znmiPJQFivscsve9Xnzc/ZNE9yi2LocresiB5WbWo6kSu53GUbOFTVDn2/NXRFSMaHk9SbzDthoFwXx1lQHgN/L6qVvzNF3K6TeD7Ch5Thp9WElCjofexBJ/RRHx872m1gT5l4pZ9D2OeEd0YfdGnTaNe4fWaUccq6g3AYBQ+U9SP5FLEXPM9myHS3UuxccPmEqj3Fman57QBnLLfvx20W9ueMlNDxm9XFYTEJcGA18tYdsnstCna5SPwOwcFtEC/o3x7523WWVLLOQ1OsAHtSDPh0pwKcic2SFyh7CAon0TgMcHeAa6NJIq186q374b9ScvbrTUKV/qpMno/CIonbOqaikqVqHAmLa1kBfyWjJsDaHvkT/3T9tv7R2KdlG+6EO+vKktUYydEqbbJl+g8CQHH0Zsf4yFqx9pvzB3soPwOZohLZPtkYexPHaWXadrBAmIvkH6JQlQNkYNRTCPL/Eb78jmo3A+MvhRLeBLwdfVWJUbkBLG1G3dSi2oBGkyb6Qr6R/Ajpmr289hkQvYvdtPlTXnd8rR5NTGehH4KLZYdaeY79T7062mHvnJBRM9cV9787c9tN0xmINtnaqtSw7cKYxn+MxnQJhm9ZtgI35shsJFSIb85u0/nhhJITvOTmaCm8iMcPuWYwyI8Vsinghe/cx2+FCvT0xNE8vW22OMLT3IJCLLQllbpTPTwuYwRkIgeJ4OGzzUBbRx4oLQyh2/sTux5zb9iLBokzPs0QH7twnh5X5MQc+uNNwMcLmWAopDXbaCiKaLcGCUcAdZwohXAzQxV3WIs2iQtM75ezmpscdkxKHSWJDSskCX8LBkeZc4h6CpbuCJqeGAWsPlqv6iXVjanU4dPrKlP4uWCeU1oAKaUDP/WjoRhGXqQW72qYVNSpfTWZ9gr6Z9oU8UpQMkWElv2SziXFMGyiJgRndFyiv0G3vIDlD2thXoWbjXMog6anb9Clhg/HRVkC/0Rj1nfEErrlGyw9kgl+J88maawA6x2Et8GbOkj/1ZHVZnPJmXhpYCujf8veWbuH74Hv4yWlTuqJkZMLKY9CF+DUqO+b+w1g2q+IQR8O7AxecTIaC3e/cNwN88uAJsZyfILAjAw8j2O3NlVu/RRf5Z1lkr7qOudypulFUPosNAhpVN4I2W7M5qf2Z9giJjUnY2RMZDywJzHFMEh2qgwz/0iLYTMykh65qgRGIE6uvL4YKrS31Y7xoulA9bzTrRYnSlciv0pXj4iSAAUfK/CEvhQyfcMga4VhhVV3UDoWCMD19DUMZtCVk4I3MovCd9ZvW3QXtrlmo7C3C0YFW+TFsQW/uIon7aKTi5UYXLfNcWZGWNN0rSimTL0D6eDDAnWE0iZxeFkRutsfXXWQxBBzwo49h/q2q3LyxcFkQtrMnLHFdmj+URkHW79CCb+1CvdI+jjuCkzToYY7bAlSmiO9qn3sE2mbLRejJonuFU6DmbUBlKORLJCUqRkW4bxmBOKXOrOdJkfWcmVy7i0PahMZsSqRvhtCYriecjmJb10O6aF92rN9moWg0iETlJXQai4flQtmhSFk6Ud0VG6XEUX1CX8F+xK0xHOxGI4kounWC8ZTMu8Ym7MnQ0Ip2n9jxd2/x9ym+xDHJgN8YKxnOevDTCfS6IrUeSzX+6PqgYLn5K6wnp6n1I5CRHX1gVK09OWKJXHl8E87XZPHMGNvXAzkghMqPMGmL9FamaDCMfsSQUUaDbfGwbBYkpnCNFrSTuz6zwKVkQ/qCuxoKdFs3gYsbEjKroV1/lD6NNMkp8kIImpUs5Jiw1615C1a10gFV2OeR8z9NUQp20Awa+UW0NRY2TixoFbfXwQPkB2y0uxGcMvzeaEwUqTvnYuOtyG09qSyrgHkeGkRfkaJFnu0hbuiB4oPBOq5oLDVBRscR/n46eOwpU/m79OXTMdyMZLT2TsehNtEHiH7xRi1onq4OjRdrAbCw9SFeD5Hz2dTtwTB16FOSVJ/7rOyIgs+kmYwR6YJfqepQnxh6VX9Q/OneINYZdY9nTz5eX+WsuMwK2WElM2aw4XpsZzpM4nsz4DwI4hMcDCcjhraA+tbTiwS8wW6YBzePTnZZAA2gnZK+VgeZq/kS6MAPNCTFMVa7ipfubHjVjKGBeH/5+17ogxBPpro8UJb7j1Lgpr2rjGIchjV+mSkF7FznrV+NjLx6ethNYy7M1opSd1gtzJ9IC8Y8Q+z6cuHXWBUfvqPWZ3bMvdUx2NpBaQqVRhHaB+T7ITOWjVElCLHnOVken3EoKnaRLsXSTCRRqWqOeDFK09ksopkhGvdObMPesUhr+sFvIJgCzvjikIBs5QHWlrnOKMATR7wCh078+JZCcG45nqn5dNBoM9wEz0jLgexdhuUpKIh0wNmddbCmuTlQm9Pv3DOzAz18AttTPnIjRbUj11T0gWAKAmT/KgRzbcPAeyhhnimnsauegdbly+qz+I0U9oh4WRD2JFfayZ3F/THaYXX53xjiTluY+Q9A28FVBE5yngCApDBqzAN0vnBw4ywFFNgImMORIe2o/mRumsLzyBTbJBNSrDVrHJgnHKNB7efqjceooroBskDErp8q4DOrDwGc/VOwk5qYUH0Km5RM5lRMxOed5kbe1hNsyFevY9DpjpQAn/IR1/RDa1Ahp6GrNscJRB0oFzFTZSP4Sd6AX4S4eiUE67cjISQR/gg46yae6TSfpMxr5zauhkxkDT192N1JHvghdIonnMvcdoaDzpZSX2iLTHkQ6cAID3b7sCt8rZggOvxJoowXRmODV51Q1hJ0bRZri3XAn2YeYlZeR44826mKIsK9MIeU7BYOh73oI9toPbTlC5MIwRn3R5NcsA9O3/4mfW82gkhslLWUFzd1EpQSAE+/7gHXPuufXVhcrTCMsxF1C2E+8FwR5j6hl9+5g/QN8Kf3+mg+pW0BkrHO49ggrLzChMppP7H7aCDdhP5kISRC7RdqOEJ0OF9MrmtouWI9JYqHbNSWsWFXTFn/3nID45dXmc0V82YMvDGfq1riTcdjewL9ndIdn0eLBDXfPrqfLVo+ThGb8u/KQugyu2lsYbr8zitzUt5jYUaxxLmxdOPOGwYY38yeRc9Xh1bAN6zfzCrxUh7MT/qA5GhcmEEKMZQ4BvxFbKyA1PvV7uKWejsWOFQpcvLXZY5lyWwp/MJiiz0yUfii8n4QG15ScqdaPV0+Bndh0qBBWgkTjY/YtKmY/NDVNA5lF/uX3WAu/xL9fMoFUXuMXxBeRSG+KSsSN9GNcE+ads2OnEUOQMnxA97thWmtmTh3nU0KXxMfwUoFCC5F8kfiecW1DHuVhB6j176aR2/xbUKVC8UTsC+8/EMACwuZTbvcd6C50wdXlQEUWIZ92UwFnSrkHU3jYb+tTlp2J0YIUk/wHTLpXb5PwPowKz+3pVqiK/r/+Odf/6T3Vqz//Af+UPgH+tc/ZdMVQ9IX//znnyPZu61vhvy/k6oYtv+a7nfz6mmm//5/90ExhCL+9c9aJwiGvzsUOE6lnzKFiTIv4A/69lWJwnCeY58PjFE5DsMUQqYIRWIkkVBQCaElVlIlhJNFkpTFP//zP//6Z1rG4x3BkL1D+D//WYok/8//Hv4//z/D+b/+9c+SNe+R4f+C3rGt3V69d5Zk+Xc9nsmS1//+/3b6e/het6L/72wctuLa/vnPsHfdv/7Zkmr9O9JLHE3eJMO7IQr9G4f+Tf095Tik4/tEzVC9d87m17w3v2E8uyKvin+nyVq8f/jfg7y3yb6Nf2Fn/HuSNauLfO/+nz37cWi2cfm78475KJb1b6P/Hfd/wf/8z/8Nlyc6wx7eAAA= -->
