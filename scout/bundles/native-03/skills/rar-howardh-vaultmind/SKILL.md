---
name: "rar-howardh-vaultmind"
description: "Obsidian vault manager for multi-person 30-60-90 day plans, LLM knowledge bases, and scheduled automation. People: add_person, roster, check_in, retire, assign, priorities, metrics, plan. Reporting: report (HTML dashboard), dashboard (text summary), review (weekly). Wiki: compile, ingest, health, query. Productivity: paste (quick raw-text ingest), log (activity log), okr (objectives & key results), kanban (generate Kanban board). Automation: brief (morning digest), watch (URL monitor), job_status (show scheduled jobs), run_job (trigger a job), setup (configure jobs), pause (toggle job)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/vaultmind_agent", "rar_sha256": "6e2af2a79f6dcb1ba6fbf2ea9331d5f8a571b9842efa39727f4605333a3a846a", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Howard Hoy", "tags": ["obsidian", "30-60-90", "onboarding", "wiki", "knowledge-base", "vault", "automation", "scheduling", "monitoring"]}
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
