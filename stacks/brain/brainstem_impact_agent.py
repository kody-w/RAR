"""
Brainstem Impact agent - one file, drop it into any Brainstem's agents/ folder.

Finds when this Brainstem was first installed, then compares the lines of code
YOU wrote (git commits by your own git email) in an equal window before and
after that date. Read-only: it only runs `git log`. Nothing leaves the machine.
"""
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/brainstem_impact_agent",
    "version": "1.0.0",
    "display_name": "BrainstemImpact",
    "description": "Finds when the Brainstem was installed and compares the lines of code the user committed in equal windows before and after.",
    "author": "kody-w",
    "tags": ["brain", "impact", "productivity", "git", "metrics"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import os
import subprocess
from datetime import datetime, timedelta, timezone

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # running standalone
    from basic_agent import BasicAgent


def _git(args, cwd=None):
    try:
        r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True,
                           text=True, timeout=60)
        return r.stdout.strip() if r.returncode == 0 else ""
    except Exception:
        return ""


def _install_date():
    """Earliest trustworthy signal of when the Brainstem arrived."""
    home = os.path.expanduser("~/.brainstem")
    candidates = []
    src = os.path.join(home, "src")
    if os.path.isdir(os.path.join(src, ".git")):
        # first reflog entry = the day it was cloned onto this machine
        first = _git(["reflog", "--date=unix", "--format=%gd"], cwd=src).splitlines()
        if first:
            try:
                candidates.append((int(first[-1].split("@{")[1].rstrip("}")), "first clone of ~/.brainstem/src"))
            except (IndexError, ValueError):
                pass
    for path in (home, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))):
        if os.path.exists(path):
            st = os.stat(path)
            ts = getattr(st, "st_birthtime", None) or st.st_mtime
            candidates.append((int(ts), f"created {path}"))
    if not candidates:
        return None, "not found"
    ts, how = min(candidates)
    return datetime.fromtimestamp(ts, tz=timezone.utc), how


def _find_repos(roots, max_depth=4):
    repos = []
    skip = {"node_modules", ".venv", "venv", "Library", ".Trash", ".cache"}
    for root in roots:
        root = os.path.expanduser(root)
        base = root.rstrip(os.sep).count(os.sep)
        for dirpath, dirnames, _ in os.walk(root):
            if ".git" in dirnames:
                repos.append(dirpath)
                dirnames[:] = []
                continue
            if dirpath.count(os.sep) - base >= max_depth:
                dirnames[:] = []
            dirnames[:] = [d for d in dirnames if d not in skip and not d.startswith(".")]
    return repos


def _lines(repo, email, since, until):
    out = _git(["log", "--all", "--no-merges", f"--author={email}",
                f"--since={since.isoformat()}", f"--until={until.isoformat()}",
                "--numstat", "--format=@%H"], cwd=repo)
    added = removed = commits = 0
    for line in out.splitlines():
        if line.startswith("@"):
            commits += 1
            continue
        parts = line.split("\t")
        if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
            added += int(parts[0])
            removed += int(parts[1])
    return added, removed, commits


class BrainstemImpactAgent(BasicAgent):
    def __init__(self):
        self.name = "BrainstemImpact"
        self.metadata = {
            "name": self.name,
            "description": (
                "Measures the user's coding productivity before vs after they installed the "
                "Brainstem: finds the install date, then counts lines of code the user wrote "
                "(git commits by their email) in equal windows before and after. Use when the "
                "user asks about their impact, productivity, or before/after with the Brainstem."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "folders": {"type": "string", "description": "Comma-separated folders to scan for git repos. Default: ~/Documents/GitHub,~/code,~/src,~/projects"},
                    "email": {"type": "string", "description": "Author email to count. Default: the user's git config user.email"},
                    "window_days": {"type": "integer", "description": "Days on each side of the install date. Default: as many days as have passed since install (max 180)"},
                    "install_date": {"type": "string", "description": "Override install date, YYYY-MM-DD, if the user knows it"},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, folders="", email="", window_days=0, install_date="", **kwargs):
        if install_date:
            installed = datetime.strptime(install_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
            how = "given by the user"
        else:
            installed, how = _install_date()
        if not installed:
            return "I couldn't find when the Brainstem was installed. Tell me the date (YYYY-MM-DD) and I'll run it."

        email = email or _git(["config", "--global", "user.email"])
        if not email:
            return "I need the email you commit with (git config user.email isn't set)."

        now = datetime.now(timezone.utc)
        days_since = max((now - installed).days, 1)
        window = int(window_days) if window_days else min(days_since, 180)
        before_start, after_end = installed - timedelta(days=window), min(installed + timedelta(days=window), now)

        roots = [f.strip() for f in folders.split(",") if f.strip()] or \
            ["~/Documents/GitHub", "~/code", "~/src", "~/projects", "~/repos"]
        roots = [r for r in roots if os.path.isdir(os.path.expanduser(r))]
        repos = _find_repos(roots)
        if not repos:
            return f"No git repos found under {roots}. Tell me which folder holds your code."

        tot_b = [0, 0, 0]
        tot_a = [0, 0, 0]
        per_repo = []
        for repo in repos:
            b = _lines(repo, email, before_start, installed)
            a = _lines(repo, email, installed, after_end)
            for i in range(3):
                tot_b[i] += b[i]
                tot_a[i] += a[i]
            if b[0] or a[0]:
                per_repo.append((os.path.basename(repo), b[0], a[0]))
        per_repo.sort(key=lambda r: r[2] - r[1], reverse=True)

        days_after = max((after_end - installed).days, 1)
        rate_b = tot_b[0] / window
        rate_a = tot_a[0] / days_after
        if rate_b:
            mult = rate_a / rate_b
            headline = f"{mult:.1f}x the lines of code per day since installing the Brainstem."
        else:
            headline = "No commits before the Brainstem to compare against."

        lines = [
            f"**{headline}**",
            "",
            f"Installed: {installed:%Y-%m-%d} ({how}). Author: {email}. {len(repos)} repos scanned.",
            "",
            "| | Before | After |",
            "|---|---|---|",
            f"| Window | {window} days | {days_after} days |",
            f"| Lines added | {tot_b[0]:,} | {tot_a[0]:,} |",
            f"| Lines added per day | {rate_b:,.0f} | {rate_a:,.0f} |",
            f"| Commits | {tot_b[2]:,} | {tot_a[2]:,} |",
        ]
        if per_repo:
            lines += ["", "Biggest changes: " + ", ".join(
                f"{n} ({b:,} -> {a:,})" for n, b, a in per_repo[:5])]
        lines += ["", "_Lines added in your own git commits. Before/after is a correlation, "
                  "not proof the Brainstem caused it; generated files and lockfiles count too._"]
        return "\n".join(lines)


if __name__ == "__main__":
    print(BrainstemImpactAgent().perform())
