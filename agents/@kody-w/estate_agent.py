"""Estate — a single drop-in cartridge for tracking your local twin estate.

Twins live in ~/.rapp/twins/<rappid>/. Eggs live in ~/.rapp/eggs/. Soul
history lives in each twin's .brainstem_data/soul_history/. This
cartridge reads those paths and gives the user a coherent view of
what's on the device — running status, memory size, soul history,
parent lineage, egg backups.

Companion to twin_agent.py:
  • twin_agent.py — lifecycle ops (summon/hatch/boot/stop/update_soul)
  • estate_agent.py — read-only inspection across the whole estate

Drop into ~/.brainstem/agents/ on a standard rapp-installer'd brainstem.
The LLM gets a tool called `Estate`. In chat:

  User: "What twins do I have?"
  Model: Estate(view="overview")

  User: "Tell me about ketchikan-pulse"
  Model: Estate(view="inspect", rappid_uuid="ee026278-…")

  User: "Show me her soul history"
  Model: Estate(view="history", rappid_uuid="ee026278-…")

  User: "What eggs do I have backed up?"
  Model: Estate(view="eggs")

  User: "Show me my twin family tree"
  Model: Estate(view="lineage")

Read-only. Never modifies any local data. Use twin_agent for any edit.
"""

import json
import os
import pathlib
import socket
import time
import urllib.error
import urllib.request

from agents.basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/estate_agent",
    "version": "1.0.0",
    "display_name": "Estate",
    "description": "Inspect the user's local twin estate. Shows running status, soul history, eggs, lineage. Read-only — companion to twin_agent for lifecycle ops.",
    "author": "kody-w",
    "tags": ["twin", "estate", "inspect", "track", "local-first"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


VIEWS = ("overview", "inspect", "eggs", "history", "lineage")


# ── Path helpers ────────────────────────────────────────────────────────

def _rapp_home():
    return os.environ.get("RAPP_HOME") or os.path.join(os.path.expanduser("~"), ".rapp")


def _twins_dir():
    return os.path.join(_rapp_home(), "twins")


def _eggs_dir():
    return os.path.join(_rapp_home(), "eggs")


def _pids_dir():
    return os.path.join(_rapp_home(), "pids")


def _ports_dir():
    return os.path.join(_rapp_home(), "ports")


# ── Live status helpers ─────────────────────────────────────────────────

def _read_int_file(path):
    try:
        return int(pathlib.Path(path).read_text().strip())
    except (ValueError, OSError, FileNotFoundError):
        return None


def _pid_alive(pid):
    if not pid or pid <= 0:
        return False
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError, OSError):
        return False


def _probe_health(port, timeout=0.4):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=timeout) as r:
            return r.status == 200
    except (urllib.error.URLError, OSError, TimeoutError):
        return False


def _human_size(n):
    """Format a byte count as '1.2 KB', '3.4 MB', etc."""
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}" if unit != "B" else f"{n} B"
        n /= 1024.0
    return f"{n:.1f} TB"


def _dir_size(path):
    total = 0
    for root, _dirs, files in os.walk(path):
        for fn in files:
            try:
                total += os.path.getsize(os.path.join(root, fn))
            except OSError:
                pass
    return total


def _human_age(seconds):
    if seconds < 60:    return f"{int(seconds)}s ago"
    if seconds < 3600:  return f"{int(seconds / 60)}m ago"
    if seconds < 86400: return f"{int(seconds / 3600)}h ago"
    if seconds < 604800: return f"{int(seconds / 86400)}d ago"
    return f"{int(seconds / 604800)}w ago"


# ── Twin scanner ────────────────────────────────────────────────────────

def _scan_twin(rappid_dir):
    """Read everything we know about a single twin. Returns a dict."""
    rappid_dir = pathlib.Path(rappid_dir)
    rj_path = rappid_dir / "rappid.json"
    rj = {}
    if rj_path.exists():
        try:
            rj = json.loads(rj_path.read_text())
        except (json.JSONDecodeError, OSError):
            pass

    rappid = rj.get("rappid") or rappid_dir.name
    name = rj.get("name") or rappid_dir.name[:8]

    # Running status
    pid = _read_int_file(os.path.join(_pids_dir(), f"{rappid}.pid"))
    port = _read_int_file(os.path.join(_ports_dir(), f"{rappid}.port"))
    running = _pid_alive(pid) if pid else False
    healthy = _probe_health(port) if (running and port) else False

    # Memory size
    bs_data = rappid_dir / ".brainstem_data"
    memory_bytes = _dir_size(str(bs_data)) if bs_data.exists() else 0

    # Soul history depth
    history_dir = bs_data / "soul_history"
    history_count = 0
    last_edit_ts = None
    if history_dir.exists():
        history_files = sorted(history_dir.glob("*.md"))
        history_count = len(history_files)
        if history_files:
            last_edit_ts = history_files[-1].stat().st_mtime

    # Soul.md last-modified
    soul_mtime = None
    soul_path = rappid_dir / "soul.md"
    if soul_path.exists():
        soul_mtime = soul_path.stat().st_mtime

    # Egg backup count for this rappid
    egg_count = 0
    egg_total_bytes = 0
    eggs_for_rappid = pathlib.Path(_eggs_dir()) / rappid
    if eggs_for_rappid.exists():
        for e in eggs_for_rappid.glob("*.egg"):
            egg_count += 1
            try:
                egg_total_bytes += e.stat().st_size
            except OSError:
                pass

    return {
        "rappid": rappid,
        "name": rj.get("name") or name,
        "kind": rj.get("kind") or "?",
        "born_at": rj.get("born_at"),
        "parent_rappid": rj.get("parent_rappid"),
        "parent_repo": rj.get("parent_repo"),
        "description": rj.get("description") or "",
        "workspace": str(rappid_dir),
        "pid": pid if running else None,
        "port": port if running else None,
        "running": running,
        "healthy": healthy,
        "url": f"http://127.0.0.1:{port}/" if running and port else None,
        "memory_bytes": memory_bytes,
        "soul_mtime": soul_mtime,
        "history_count": history_count,
        "last_edit_mtime": last_edit_ts,
        "egg_count": egg_count,
        "egg_total_bytes": egg_total_bytes,
    }


def _scan_all():
    twins_dir = _twins_dir()
    out = []
    if not os.path.isdir(twins_dir):
        return out
    for entry in sorted(os.listdir(twins_dir)):
        full = os.path.join(twins_dir, entry)
        if os.path.isdir(full):
            out.append(_scan_twin(full))
    return out


# ── Renderers ───────────────────────────────────────────────────────────

def _render_overview(twins):
    if not twins:
        return ("Your estate is empty. Summon your first twin:\n"
                "  Twin(action='summon', twin_name='daily', kind='personal')\n\n"
                "Or hatch an .egg you have on disk:\n"
                "  Twin(action='hatch', egg_path='/path/to/twin.egg')")

    running_count = sum(1 for t in twins if t["running"])
    total_memory = sum(t["memory_bytes"] for t in twins)
    total_eggs = sum(t["egg_count"] for t in twins)
    now = time.time()

    lines = [
        f"Estate: {len(twins)} twin{'' if len(twins) == 1 else 's'} on this device "
        f"({running_count} running, {len(twins) - running_count} stopped)",
        f"  total memory: {_human_size(total_memory)} · total eggs: {total_eggs}",
        "",
    ]

    for t in twins:
        status = "● RUNNING" if t["running"] else "○ stopped"
        if t["running"] and not t["healthy"]:
            status = "● running (not responding)"
        url_part = f"  {t['url']}" if t["url"] else ""
        lines.append(f"  {status}  {t['name']} ({t['kind']}){url_part}")

        meta_parts = [f"rappid {t['rappid'][:8]}…"]
        if t["memory_bytes"] > 0:
            meta_parts.append(f"memory {_human_size(t['memory_bytes'])}")
        if t["history_count"] > 0:
            meta_parts.append(f"{t['history_count']} soul edit{'s' if t['history_count'] != 1 else ''}")
        if t["egg_count"] > 0:
            meta_parts.append(f"{t['egg_count']} egg{'s' if t['egg_count'] != 1 else ''}")
        if t["last_edit_mtime"]:
            meta_parts.append(f"last edit {_human_age(now - t['last_edit_mtime'])}")
        lines.append(f"           {' · '.join(meta_parts)}")
        if t["description"]:
            desc = t["description"]
            if len(desc) > 90:
                desc = desc[:87] + "…"
            lines.append(f"           \"{desc}\"")
        lines.append("")

    lines.append("Drill in: Estate(view='inspect', rappid_uuid='<rappid>')")
    return "\n".join(lines)


def _render_inspect(twins, rappid):
    t = next((x for x in twins if x["rappid"].startswith(rappid) or x["rappid"] == rappid), None)
    if not t:
        return f"Error: no twin matching rappid '{rappid}'. Use view='overview' to see all rappids."
    now = time.time()

    lines = [
        f"╭─ {t['name']} ({t['kind']}) ─" + "─" * max(1, 70 - len(t['name']) - len(t['kind']) - 5),
        f"│  rappid:        {t['rappid']}",
    ]
    if t["parent_rappid"]:
        lines.append(f"│  parent rappid: {t['parent_rappid']}")
    if t["parent_repo"]:
        lines.append(f"│  parent repo:   {t['parent_repo']}")
    if t["born_at"]:
        lines.append(f"│  born:          {t['born_at']}")
    if t["description"]:
        lines.append(f"│  description:   {t['description']}")
    lines.append("│")
    lines.append(f"│  workspace:     {t['workspace']}")
    lines.append(f"│  memory:        {_human_size(t['memory_bytes'])}")
    if t["soul_mtime"]:
        lines.append(f"│  soul.md:       last edited {_human_age(now - t['soul_mtime'])}")
    lines.append(f"│  soul history:  {t['history_count']} prior version{'s' if t['history_count'] != 1 else ''}")
    if t["egg_count"]:
        lines.append(f"│  egg backups:   {t['egg_count']} ({_human_size(t['egg_total_bytes'])})")
    lines.append("│")
    if t["running"]:
        lines.append(f"│  STATUS:        RUNNING")
        lines.append(f"│  pid:           {t['pid']}")
        lines.append(f"│  port:          {t['port']}")
        lines.append(f"│  health:        {'responding' if t['healthy'] else 'not responding'}")
        lines.append(f"│  url:           {t['url']}")
        lines.append(f"│")
        lines.append(f"│  Stop:  Twin(action='stop', rappid_uuid='{t['rappid']}')")
    else:
        lines.append(f"│  STATUS:        stopped")
        lines.append(f"│")
        lines.append(f"│  Boot:  Twin(action='boot', rappid_uuid='{t['rappid']}')")
    lines.append(f"│  Soul history:  Estate(view='history', rappid_uuid='{t['rappid']}')")
    lines.append("╰" + "─" * 78)
    return "\n".join(lines)


def _render_history(twins, rappid):
    t = next((x for x in twins if x["rappid"].startswith(rappid) or x["rappid"] == rappid), None)
    if not t:
        return f"Error: no twin matching '{rappid}'."

    history = pathlib.Path(t["workspace"]) / ".brainstem_data" / "soul_history"
    if not history.exists():
        return (f"'{t['name']}' has no soul history yet. "
                f"The first soul edit will create one — twins adapt with backups.")

    files = sorted(history.glob("*.md"), reverse=True)
    if not files:
        return f"'{t['name']}' has an empty history dir."

    now = time.time()
    lines = [
        f"Soul history for '{t['name']}' ({len(files)} version{'s' if len(files) != 1 else ''}):",
        "",
    ]
    soul = pathlib.Path(t["workspace"]) / "soul.md"
    if soul.exists():
        size = soul.stat().st_size
        mtime = soul.stat().st_mtime
        lines.append(f"  ▶ CURRENT  soul.md  ({_human_size(size)}, edited {_human_age(now - mtime)})")
    for f in files:
        ts_part = f.stem.split("Z")[0] + "Z" if "Z" in f.stem else f.stem
        reason = "—"
        # Filename pattern: 2026-05-04T16-41-04Z-add-brunch-section.md
        if "Z-" in f.stem:
            reason = f.stem.split("Z-", 1)[1].replace("-", " ")
        lines.append(f"    {f.name}  ({_human_size(f.stat().st_size)}, {reason})")
    lines.append("")
    lines.append("Revert to any prior version:  cp <history-file> soul.md")
    return "\n".join(lines)


def _render_eggs():
    eggs_root = _eggs_dir()
    if not os.path.isdir(eggs_root):
        return ("No egg backups yet. Pack a twin into an .egg via "
                "Twin(action='lay-egg', ...) — coming in twin_agent v1.1.")

    eggs = []
    for rappid in sorted(os.listdir(eggs_root)):
        rd = os.path.join(eggs_root, rappid)
        if not os.path.isdir(rd):
            continue
        for fn in sorted(os.listdir(rd), reverse=True):
            if not fn.endswith(".egg"):
                continue
            full = os.path.join(rd, fn)
            try:
                st = os.stat(full)
            except OSError:
                continue
            eggs.append({
                "rappid": rappid,
                "filename": fn,
                "path": full,
                "size": st.st_size,
                "mtime": st.st_mtime,
            })

    if not eggs:
        return "No egg backups yet."

    now = time.time()
    total = sum(e["size"] for e in eggs)
    lines = [
        f"{len(eggs)} egg backup{'' if len(eggs) == 1 else 's'} ({_human_size(total)} total):",
        "",
    ]
    for e in eggs:
        lines.append(
            f"  • {e['filename']}  ({_human_size(e['size'])}, {_human_age(now - e['mtime'])})"
        )
        lines.append(f"      rappid: {e['rappid'][:8]}…  path: {e['path']}")
    lines.append("")
    lines.append("Hatch any egg:  Twin(action='hatch', egg_path='<path>')")
    return "\n".join(lines)


def _render_lineage(twins):
    if not twins:
        return "No twins yet — no lineage to show."

    # Group by parent_rappid
    by_parent = {}
    for t in twins:
        parent = t["parent_rappid"] or "<no parent>"
        by_parent.setdefault(parent, []).append(t)

    lines = ["Twin family tree (grouped by parent):"]
    for parent, kids in sorted(by_parent.items()):
        if parent == "<no parent>":
            lines.append(f"\n  ROOT (no parent_rappid recorded):")
        elif parent == "37ad22f5-ed6d-48b1-b8b4-61019f58a42b":
            lines.append(f"\n  Parent: wildhaven-ai-homes-twin")
            lines.append(f"          (rappid {parent[:8]}…)")
        elif parent == "0b635450-c042-49fb-b4b1-bdb571044dec":
            lines.append(f"\n  Parent: rapp species root")
            lines.append(f"          (rappid {parent[:8]}…)")
        else:
            lines.append(f"\n  Parent: {parent[:8]}…")
        for t in kids:
            lines.append(f"    └─ {t['name']} ({t['kind']})  rappid {t['rappid'][:8]}…")

    lines.append("\nLineage chains walk back through parent_rappid → ... → rapp species root.")
    return "\n".join(lines)


# ── The cartridge ───────────────────────────────────────────────────────


class EstateAgent(BasicAgent):
    def __init__(self):
        self.name = "Estate"
        self.metadata = {
            "name": self.name,
            "description": (
                "Inspect the user's local twin estate. Read-only — for "
                "edits use the Twin tool. Pick a view: 'overview' for the "
                "full list with running status (default if user just asks "
                "'what twins do I have'); 'inspect' for one twin's full "
                "details (need rappid_uuid); 'history' for soul.md history "
                "of one twin (need rappid_uuid); 'eggs' for all .egg "
                "backups; 'lineage' for the family tree grouped by parent."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "view": {
                        "type": "string",
                        "enum": list(VIEWS),
                        "description": "Which view of the estate to render.",
                    },
                    "rappid_uuid": {
                        "type": "string",
                        "description": "Twin identifier — required for 'inspect' and 'history' views. Matches by prefix, so the first 8 chars are enough.",
                    },
                },
                "required": ["view"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        view = kwargs.get("view") or "overview"
        if view not in VIEWS:
            return f"Error: view must be one of {', '.join(VIEWS)}. Got: {view!r}"

        twins = _scan_all()

        if view == "overview":  return _render_overview(twins)
        if view == "lineage":   return _render_lineage(twins)
        if view == "eggs":      return _render_eggs()

        rappid = kwargs.get("rappid_uuid") or ""
        if not rappid:
            return f"Error: rappid_uuid required for view='{view}'. Use view='overview' first to find rappids."

        if view == "inspect":   return _render_inspect(twins, rappid)
        if view == "history":   return _render_history(twins, rappid)
        return f"Error: unhandled view {view!r}"
