---
name: "rar-rapp-drift-watcher"
description: "Watch GitHub drift Issues and stage the fix as a pull request (Fixes #) \u2014 proposes only, never merges or closes. Closes the drift traceability loop: Issue \u2192 PR \u2192 operator merge \u2192 auto-close."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/drift_watcher", "rar_sha256": "0d87442bbc4330abef6f282af1e095f43c930580b20f1b3ac9ec010fad4187cd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["drift", "spec", "github", "issues", "pull-request", "traceability", "steward", "alignment", "operator-mediated"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `drift_watcher_agent.py` and embedded as the fenced Python below (sha256 0d87442bbc4330ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `drift_watcher_agent.py` first:

```bash
python3 drift_watcher_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 drift_watcher_agent.py   # or on stdin
python3 drift_watcher_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/drift_watcher_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/drift_watcher_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/drift_watcher/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
