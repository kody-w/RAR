---
name: "rar-rapp-drift-watcher"
description: "Watch GitHub drift Issues and stage the fix as a pull request (Fixes #) \u2014 proposes only, never merges or closes. Closes the drift traceability loop: Issue \u2192 PR \u2192 operator merge \u2192 auto-close."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/drift_watcher", "rar_sha256": "0d87442bbc4330abef6f282af1e095f43c930580b20f1b3ac9ec010fad4187cd", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["drift", "spec", "github", "issues", "pull-request", "traceability", "steward", "alignment", "operator-mediated"]}
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
