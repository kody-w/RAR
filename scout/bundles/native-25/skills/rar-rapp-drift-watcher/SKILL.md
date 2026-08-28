---
name: "rar-rapp-drift-watcher"
description: "Watch GitHub drift Issues and stage the fix as a pull request (Fixes #) \u2014 proposes only, never merges or closes. Closes the drift traceability loop: Issue \u2192 PR \u2192 operator merge \u2192 auto-close."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/drift_watcher", "rar_sha256": "6f2aedf636bbbde6a3b692c2d920c6af283291885886eba3f523179766529dee", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["drift", "spec", "github", "issues", "pull-request", "traceability", "steward", "alignment", "operator-mediated"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/drift_watcher`. The original RAPP
agent is preserved byte-for-byte in `drift_watcher_agent.py` and in the RCI capsule.

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

DriftWatcherAgent — close the traceability loop on spec drift.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "list",
        "propose",
        "help"
      ],
      "type": "string"
    },
    "confirm": {
      "description": "propose: False=DRY-RUN plan (default); True=actually stage the PR",
      "type": "boolean"
    },
    "issue": {
      "description": "propose: the drift Issue number to stage a PR for",
      "type": "integer"
    },
    "label": {
      "description": "list: Issue label to watch (default rapp-drift)",
      "type": "string"
    },
    "repo": {
      "description": "propose: target owner/repo to fix (default from the machine block source)",
      "type": "string"
    },
    "tracker": {
      "description": "list: owner/repo holding the drift Issues (default $DRIFT_TRACKER)",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `drift_watcher_agent.py` and embedded as the fenced Python below (sha256 6f2aedf636bbbde6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `drift_watcher_agent.py` first:

```bash
python3 drift_watcher_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 drift_watcher_agent.py   # or on stdin
python3 drift_watcher_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
