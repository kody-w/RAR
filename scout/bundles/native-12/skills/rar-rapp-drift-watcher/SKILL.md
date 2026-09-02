---
name: "rar-rapp-drift-watcher"
description: "Watch GitHub drift Issues and stage the fix as a pull request (Fixes #) \u2014 proposes only, never merges or closes. Closes the drift traceability loop: Issue \u2192 PR \u2192 operator merge \u2192 auto-close."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/drift_watcher", "rar_sha256": "6f2aedf636bbbde6a3b692c2d920c6af283291885886eba3f523179766529dee", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "drift_watcher_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/drift-watcher:f67a627076324230ffd1067559894e4e345fb88852d09fb20ebd36e2f6c1b2b3", "kind": "skill"}, "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["drift", "spec", "github", "issues", "pull-request", "traceability", "steward", "alignment", "operator-mediated"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/drift_watcher`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `drift_watcher_agent.py` is
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
