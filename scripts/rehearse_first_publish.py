#!/usr/bin/env python3
"""Rehearse a brand-new agent's first publish, end to end, in a throwaway copy of this catalog.

Nothing is published: no issue is opened and nothing is pushed. The rehearsal runs the same steps a real
first publish runs, read from the workflow files themselves so it cannot drift from them:

  1. the submit tool builds the submission (header added, fingerprint taken)
  2. intake stages it                     (scripts/process_issues.py)
  3. approval applies the staged bytes    (scripts/apply_agent_mutation.py)
  4. the admission checks run             (the "Run admission checks" step of approve-agent.yml)
  5. the approval job's own `git add` lines run, and nothing the checks built may be left behind

Step 5 is the point: a file the checks need but approval does not commit turns main red after the publish.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LOGIN = "rehearsal"
NAME = f"@{LOGIN}/first_publish_rehearsal_agent"
FILE = f"agents/@{LOGIN}/first_publish_rehearsal_agent.py"
AGENT = '''"""first_publish_rehearsal_agent: a throwaway agent used to rehearse a first publish. Never published."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "%s",
    "version": "1.0.0",
    "display_name": "First Publish Rehearsal",
    "description": "A throwaway agent used to rehearse a brand-new agent's first publish. It is never published.",
    "author": "RAR",
    "tags": ["rehearsal"],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

from agents.basic_agent import BasicAgent


class FirstPublishRehearsalAgent(BasicAgent):
    def __init__(self):
        self.name = "FirstPublishRehearsal"
        self.metadata = {
            "name": self.name,
            "description": "Answers 'rehearsed'. Used only to rehearse a first publish.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        return "rehearsed"
''' % NAME


def step(workflow: dict, name: str) -> str:
    for job in workflow["jobs"].values():
        for s in job.get("steps", []):
            if s.get("name") == name:
                return s["run"]
    raise SystemExit(f"approve-agent.yml has no step named {name!r}")


def run(copy: Path, command: str, what: str) -> str:
    done = subprocess.run(["bash", "-c", command], cwd=copy, capture_output=True, text=True)
    if done.returncode != 0:
        tail = (done.stdout + done.stderr)[-3000:]
        raise SystemExit(f"FAILED at: {what}\n$ {command}\n{tail}")
    return done.stdout


def main() -> int:
    work = Path(tempfile.mkdtemp(prefix="rar-rehearsal-"))
    copy = work / "catalog"
    try:
        subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", str(ROOT), str(copy)], check=True)
        run(copy, "git config user.name rehearsal && git config user.email rehearsal@example.invalid", "set up the copy")
        workflow = yaml.safe_load((copy / ".github/workflows/approve-agent.yml").read_text())

        # 1. the submit tool's own steps
        sys.path.insert(0, str(copy))
        import rapp_sdk
        code = rapp_sdk.with_ticket(AGENT, NAME, FILE)
        command = rapp_sdk.change_command("create", NAME, code, {"if_none_match": "*"}, "req_" + "0" * 32)
        issue = {
            "number": 999999, "node_id": "I_rehearsal", "state": "open", "title": f"[RAR] CREATE agent {NAME}",
            "body": rapp_sdk.issue_body(command), "updated_at": "2000-01-01T00:00:00Z",
            "labels": [], "user": {"id": 999999, "login": LOGIN},
        }
        repository = {"id": 1, "full_name": "rehearsal/catalog"}

        # 2. intake
        (work / "intake.json").write_text(json.dumps({"issue": issue, "repository": repository}))
        out = run(copy, f"python scripts/process_issues.py --event-path {work / 'intake.json'}", "intake stages the submission")
        if "pending_review" not in out:
            raise SystemExit(f"FAILED at: intake stages the submission\n{out[-2000:]}")

        # 3. approval applies the staged bytes
        approved = dict(issue, labels=[{"name": "agent-submission"}, {"name": "approved"}])
        (work / "approval.json").write_text(json.dumps({
            "issue": approved, "repository": repository, "sender": {"id": 999998, "login": "rehearsal-approver"},
        }))
        run(copy, f"python scripts/apply_agent_mutation.py --event-path {work / 'approval.json'}", "approval applies the staged bytes")
        if (copy / FILE).read_text() != code:
            raise SystemExit("FAILED at: the applied file is not the submitted bytes")

        # 4. the admission checks, exactly as the approval job runs them
        run(copy, step(workflow, "Run admission checks"), "admission checks")

        # 5. the approval job's own `git add` lines; nothing the checks built may be left behind
        adds = [line.strip() for name in ("Commit notarized mutation", "Refresh post-commit registry provenance")
                for line in step(workflow, name).splitlines() if line.strip().startswith("git add ")]
        for add in adds:
            run(copy, add, "the approval job's git add")
        left = [line for line in run(copy, "git status --porcelain", "git status").splitlines()
                if not line.startswith(("A ", "M ", "D ", "R "))]
        if left:
            raise SystemExit("FAILED at: approval leaves behind files the checks built or changed:\n" + "\n".join(left[:40]))
        staged = run(copy, "git diff --cached --name-only", "git diff").split()
        for needed in (FILE, f"a/{NAME}/agent.md", f"a/{NAME}/index.html", "registry.json"):
            if needed not in staged:
                raise SystemExit(f"FAILED at: approval does not commit {needed}")
        print(f"first publish rehearsed: {NAME} staged, applied, admitted; approval commits {len(staged)} files, leaves 0 behind")
        return 0
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
