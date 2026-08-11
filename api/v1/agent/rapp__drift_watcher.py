"""DriftWatcherAgent — close the traceability loop on spec drift.

The drift/steward agents FIND drift and (operator-mediated) file GitHub Issues
that carry a machine-readable fix block. This agent is the other half of that
loop: it watches those Issues and STAGES the local-repo fix as a pull request.

It is operator-mediated end to end. It proposes — it never auto-merges and
never auto-closes. The loop stays fully traceable:

    drift detected  →  Issue (rapp-drift-issue/1.0 machine block)
                    →  PR (body says "Fixes #<n>")
                    →  operator reviews + merges
                    →  GitHub auto-closes the Issue via "Fixes #"

So every closed Issue points at exactly the PR that resolved it, and every PR
points back at the Issue that requested it. Nothing closes without a human.

  list                 open drift Issues + their parsed machine blocks
  propose issue=<n>    DRY-RUN the surgical PR (default); confirm=True to stage it
  help

Uses the `gh` CLI via a small subprocess helper. Offline / no-gh → a clean
degraded note. Generic + cover-safe: it never echoes tokens or secrets, and it
refuses path traversal / malformed repo slugs. MIT © Kody Wildfeuer.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone

try:
    from agents.basic_agent import BasicAgent  # type: ignore
except ImportError:
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:
            def __init__(self, name="Agent", metadata=None):
                self.name = name
                self.metadata = metadata or {}

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/drift_watcher",
    "version": "1.0.1",
    "display_name": "DriftWatcherAgent",
    "description": ("Watches drift-labeled GitHub Issues via the gh CLI and stages each proposed fix as a pull request; proposes only, never merges or closes."),
    "author": "Kody Wildfeuer",
    "tags": ["drift", "spec", "github", "issues", "pull-request", "traceability",
             "steward", "alignment", "operator-mediated"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# Where drift Issues live + the label the drift/steward agents stamp on them.
DRIFT_TRACKER = os.environ.get("DRIFT_TRACKER", "kody-w/RAPP")
DRIFT_LABEL = os.environ.get("DRIFT_LABEL", "rapp-drift")

# A repo slug must be exactly owner/name — no nesting, no spaces, no traversal.
_REPO_RE = re.compile(r"^[\w.-]+/[\w.-]+$")
# The fenced machine block the drift Issue carries (schema rapp-drift-issue/1.0).
_FENCE_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL)
# Commit identity (cover-safe: a neutral bot identity, never a real secret).
_GIT_NAME = os.environ.get("DRIFT_BOT_NAME", "drift-watcher")
_GIT_EMAIL = os.environ.get("DRIFT_BOT_EMAIL", "drift-watcher@users.noreply.github.com")


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _run(cmd, cwd=None, timeout=120):
    """Run a subprocess; return (rc, stdout, std err). Never raises on a missing
    binary or a timeout — degrades to a non-zero rc so callers stay offline-safe."""
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout or ""), (p.stderr or "")
    except FileNotFoundError:
        return 127, "", f"binary not found: {cmd[0] if cmd else '?'}"
    except subprocess.TimeoutExpired:
        return 124, "", "timed out"
    except Exception as e:  # pragma: no cover - defensive
        return 1, "", str(e)


def _scrub(text):
    """Cover: strip anything token-shaped before it ever leaves the agent."""
    if not text:
        return text
    text = re.sub(r"gh[pousr]_[A-Za-z0-9]{20,}", "[redacted-token]", text)
    text = re.sub(r"github_pat_[A-Za-z0-9_]{20,}", "[redacted-token]", text)
    text = re.sub(r"(?i)(authorization|token|bearer|secret|password)\s*[:=]\s*\S+",
                  r"\1: [redacted]", text)
    return text


def _parse_machine(body):
    """Pull the rapp-drift-issue/1.0 machine block out of an Issue body."""
    for m in _FENCE_RE.finditer(body or ""):
        try:
            obj = json.loads(m.group(1))
        except ValueError:
            continue
        if isinstance(obj, dict) and str(obj.get("schema", "")).startswith("rapp-drift-issue"):
            return obj
    return None


def _source_to_target(source):
    """Map a machine block 'source' like 'RAPP/specs/skill.md' to
    (repo='kody-w/RAPP', file='specs/skill.md'). The first path segment is the
    repo short-name under the species owner; the rest is the in-repo path."""
    if not source or "/" not in source:
        return None, None
    owner = os.environ.get("DRIFT_OWNER", "kody-w")
    repo_short, _, path = source.partition("/")
    return f"{owner}/{repo_short}", path


def _path_ok(path):
    """Refuse path traversal / absolute paths in the in-repo file path."""
    if not path or path.startswith(("/", "\\")):
        return False
    return ".." not in re.split(r"[\\/]+", path)


class DriftWatcherAgent(BasicAgent):
    def __init__(self):
        self.name = "DriftWatcherAgent"
        self.metadata = {
            "name": self.name,
            "description": ("Watch GitHub drift Issues and stage the fix as a "
                            "pull request (Fixes #) — proposes only, never "
                            "merges or closes. Closes the drift traceability "
                            "loop: Issue → PR → operator merge → auto-close."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["list", "propose", "help"]},
                    "tracker": {"type": "string",
                                "description": "list: owner/repo holding the drift Issues (default $DRIFT_TRACKER)"},
                    "label": {"type": "string",
                              "description": "list: Issue label to watch (default rapp-drift)"},
                    "issue": {"type": "integer",
                              "description": "propose: the drift Issue number to stage a PR for"},
                    "repo": {"type": "string",
                             "description": "propose: target owner/repo to fix (default from the machine block source)"},
                    "confirm": {"type": "boolean",
                                "description": "propose: False=DRY-RUN plan (default); True=actually stage the PR"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def system_context(self):
        return ("DriftWatcherAgent closes the drift loop: it watches GitHub "
                "Issues the drift/steward agents filed and stages the local "
                "fix as a pull request that says 'Fixes #<n>'. It is "
                "operator-mediated — it proposes PRs and never merges or "
                "closes. Use it to turn a drift Issue into a reviewable PR.")

    def _env(self, action, status, **f):
        return json.dumps({"schema": "rapp-drift-watcher/1.0", "action": action,
                           "status": status, **f}, indent=2, ensure_ascii=False)

    # ── list: open drift Issues + their parsed machine blocks ──
    def _list(self, kwargs):
        tracker = (kwargs.get("tracker") or DRIFT_TRACKER).strip()
        label = (kwargs.get("label") or DRIFT_LABEL).strip()
        if not _REPO_RE.match(tracker):
            return self._env("list", "error", error=f"invalid tracker slug: {tracker!r} (want owner/repo)")
        rc, out, err = _run(["gh", "issue", "list", "--repo", tracker,
                             "--label", label, "--state", "open",
                             "--json", "number,title,body"])
        if rc != 0:
            return self._env("list", "offline",
                             note="could not reach GitHub Issues via the gh CLI "
                                  "(offline or gh not installed/authed). Try again online.",
                             tracker=tracker, label=label, detail=_scrub(err)[:200])
        try:
            raw = json.loads(out or "[]")
        except ValueError:
            return self._env("list", "error", error="gh returned non-JSON output.")
        issues = []
        for it in raw:
            machine = _parse_machine(it.get("body", ""))
            issues.append({
                "number": it.get("number"),
                "title": it.get("title"),
                "fingerprint": (machine or {}).get("fingerprint"),
                "has_machine_block": machine is not None,
                "machine": machine,
            })
        actionable = [i for i in issues if i["has_machine_block"]]
        return self._env("list", "success",
                         scanned_at=_now(), tracker=tracker, label=label,
                         open_issues=len(issues),
                         actionable=len(actionable),
                         issues=issues,
                         note=("Each actionable Issue carries a rapp-drift-issue/1.0 "
                               "machine block. Run action=propose issue=<number> to "
                               "DRY-RUN the PR that would fix it."))

    # ── propose: dry-run plan (default) or stage the PR (confirm=True) ──
    def _propose(self, kwargs):
        number = kwargs.get("issue")
        if number is None:
            return self._env("propose", "error", error="pass issue=<number>")
        tracker = (kwargs.get("tracker") or DRIFT_TRACKER).strip()
        if not _REPO_RE.match(tracker):
            return self._env("propose", "error", error=f"invalid tracker slug: {tracker!r}")
        confirm = bool(kwargs.get("confirm"))

        # fetch the one Issue's body to read its machine block
        rc, out, err = _run(["gh", "issue", "view", str(number), "--repo", tracker,
                             "--json", "number,title,body"])
        if rc != 0:
            return self._env("propose", "offline",
                             note="could not read the drift Issue via the gh CLI "
                                  "(offline or gh not installed/authed). Try again online.",
                             tracker=tracker, issue=number, detail=_scrub(err)[:200])
        try:
            issue = json.loads(out or "{}")
        except ValueError:
            return self._env("propose", "error", error="gh returned non-JSON for the Issue.")
        machine = _parse_machine(issue.get("body", ""))
        if not machine:
            return self._env("propose", "error",
                             issue=number,
                             error="Issue has no rapp-drift-issue/1.0 machine block — nothing to stage.")

        fingerprint = machine.get("fingerprint") or f"issue-{number}"
        stale = machine.get("stale")
        replace_with = machine.get("replace_with")
        source = machine.get("source")

        # resolve the target repo + file
        repo = (kwargs.get("repo") or "").strip()
        if repo:
            target_repo, _, _ = repo, None, None
            _, file_path = _source_to_target(source)
        else:
            target_repo, file_path = _source_to_target(source)

        # ── guards ──
        if not target_repo or not _REPO_RE.match(target_repo):
            return self._env("propose", "error",
                             error=f"could not resolve a valid target repo (got {target_repo!r}). "
                                   "Pass repo=owner/repo.",
                             machine_source=source)
        if not file_path or not _path_ok(file_path):
            return self._env("propose", "error",
                             error=f"refusing unsafe / unresolved file path: {file_path!r}",
                             machine_source=source)
        if not stale or not replace_with:
            return self._env("propose", "error",
                             error="machine block missing 'stale' and/or 'replace_with' — "
                                   "no surgical change to make.",
                             machine=machine)

        branch = f"drift/{fingerprint}"
        plan = {
            "target_repo": target_repo,
            "target_file": file_path,
            "surgical_change": {
                "find": stale,
                "replace_with": replace_with,
                "kind": "literal string replacement",
            },
            "would_create": {
                "branch": branch,
                "pr_body_references": f"Fixes #{number}",
                "issue_comment": "the PR url (for traceability)",
            },
            "traceability": (f"Issue #{number} → PR (body 'Fixes #{number}') → operator "
                             "merges → GitHub auto-closes the Issue. Closed Issue ↔ "
                             "resolving PR is a permanent two-way link."),
        }

        # DRY-RUN (default): describe the plan, touch nothing.
        if not confirm:
            return self._env("propose", "dry_run",
                             issue=number, fingerprint=fingerprint,
                             plan=plan,
                             mode="plan",
                             note=("DRY-RUN — nothing was changed. This is the PR that "
                                   "WOULD be staged. Re-run with confirm=True to actually "
                                   "create the branch, apply the surgical replacement, push, "
                                   "and open the PR. The operator still merges (never me)."),
                             operator_mediated=True)

        # confirm=True: actually stage the PR.
        return self._stage(number, tracker, target_repo, file_path, stale,
                           replace_with, branch, fingerprint, plan)

    def _stage(self, number, tracker, target_repo, file_path, stale,
               replace_with, branch, fingerprint, plan):
        tmp = tempfile.mkdtemp(prefix="drift-watcher-")
        clone_dir = os.path.join(tmp, "repo")
        try:
            rc, out, err = _run(["gh", "repo", "clone", target_repo, clone_dir,
                                "--", "--depth", "1"])
            if rc != 0:
                return self._env("propose", "offline",
                                 issue=number,
                                 note="could not clone the target repo (offline or no access).",
                                 target_repo=target_repo, detail=_scrub(err)[:200])

            abs = os.path.normpath(os.path.join(clone_dir, file_path))
            # re-assert containment after normalization (defense in depth)
            if not abs.startswith(os.path.normpath(clone_dir) + os.sep):
                return self._env("propose", "error",
                                 error="resolved path escapes the repo — refusing.",
                                 file=file_path)
            if not os.path.isfile(abs):
                return self._env("propose", "stale_not_found",
                                 issue=number, target_repo=target_repo, file=file_path,
                                 note="the named file is not in the target repo — nothing changed.")
            with open(abs, "r", encoding="utf-8") as fh:
                content = fh.read()
            # word-boundary-safe replacement: a version token like "rapp-egg/1"
            # must NOT also hit "rapp-egg/10" or "rapp-egg/1.1". If the stale
            # token ends in a digit, forbid a following digit/dot.
            pattern = re.escape(stale) + (r"(?![0-9.])" if stale[-1:].isdigit() else "")
            new_content, n_repl = re.subn(pattern, lambda _m: replace_with, content)
            if n_repl == 0:
                return self._env("propose", "stale_not_found",
                                 issue=number, target_repo=target_repo, file=file_path,
                                 stale=stale,
                                 note="the stale token was not found in the file — "
                                      "nothing changed (the drift may already be fixed).")
            with open(abs, "w", encoding="utf-8") as fh:
                fh.write(new_content)

            git = ["git", "-C", clone_dir, "-c", f"user.name={_GIT_NAME}",
                   "-c", f"user.email={_GIT_EMAIL}"]
            steps = [
                git + ["checkout", "-b", branch],
                git + ["add", file_path],
                git + ["commit", "-m",
                       f"Fix drift {fingerprint}: align {file_path} to canon\n\nFixes #{number}"],
                git + ["push", "-u", "origin", branch],
            ]
            for step in steps:
                rc, out, err = _run(step)
                if rc != 0:
                    return self._env("propose", "error",
                                     issue=number,
                                     error=f"git step failed: {' '.join(step[3:])[:60]}",
                                     detail=_scrub(err)[:200])

            pr_body = (f"Fixes #{number}\n\n"
                       f"Surgical drift fix `{fingerprint}`: in `{file_path}`, replace the "
                       f"stale token with the canonical one.\n\n"
                       f"- find: `{stale}`\n- replace_with: `{replace_with}`\n\n"
                       "Operator-mediated: staged by DriftWatcherAgent, which never merges "
                       "or closes. Merging this PR auto-closes the Issue via `Fixes #` — "
                       "that is the permanent two-way traceability link.")
            rc, out, err = _run(["gh", "pr", "create", "--repo", target_repo,
                                "--head", branch, "--base", "main",
                                "--title", f"Fix drift {fingerprint}: align {file_path}",
                                "--body", pr_body])
            if rc != 0:
                return self._env("propose", "error",
                                 issue=number,
                                 error="branch pushed but `gh pr create` failed.",
                                 branch=branch, detail=_scrub(err)[:200])
            pr_url = (out or "").strip().splitlines()[-1] if out else ""

            # comment the PR url back on the Issue (traceability) — never close it
            _run(["gh", "issue", "comment", str(number), "--repo", tracker,
                 "--body", f"Drift fix staged as a PR (operator merges to close): {pr_url}"])

            return self._env("propose", "staged",
                             issue=number, fingerprint=fingerprint,
                             target_repo=target_repo, file=file_path,
                             branch=branch, pr_url=pr_url,
                             plan=plan,
                             traceability=(f"PR references 'Fixes #{number}'. The operator "
                                           "reviews + merges; GitHub auto-closes the Issue. "
                                           "I did NOT merge and did NOT close."),
                             operator_mediated=True,
                             note="PR opened. Awaiting operator review + merge.")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "list").lower()

        if action == "help" or action not in ("list", "propose"):
            return (
                "DriftWatcherAgent — close the drift traceability loop.\n"
                "  action=list                     open drift Issues + parsed machine blocks\n"
                "  action=propose issue=<n>        DRY-RUN the surgical PR that would fix it\n"
                "  action=propose issue=<n> confirm=true   actually stage the PR (branch + push + PR + comment)\n"
                "  tracker=owner/repo  label=rapp-drift     (optional) where to watch / which label\n"
                "  repo=owner/repo                 (optional) override the target repo to fix\n"
                "operator-mediated; proposes PRs, never merges. The PR says 'Fixes #<n>' so "
                "the operator's merge auto-closes the Issue — issue ↔ PR stays a permanent "
                "two-way link.")

        if action == "list":
            return self._list(kwargs)
        return self._propose(kwargs)


if __name__ == "__main__":
    print(DriftWatcherAgent().perform(action="help"))
