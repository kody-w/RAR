#!/usr/bin/env python3
"""
Instance Setup — Auto-configures rar.config.json when a repo is created
from the RAR template.

Called by:  .github/workflows/template_setup.yml
Manual:    GITHUB_REPOSITORY=user/repo python scripts/setup_instance.py
"""

import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = REPO_ROOT / "rar.config.json"
UPSTREAM = "kody-w/RAR"


def main() -> int:
    github_repo = os.environ.get("GITHUB_REPOSITORY", "")
    if not github_repo or "/" not in github_repo:
        print("Error: GITHUB_REPOSITORY env var must be set (e.g. 'alice/my-agents')")
        return 1

    owner, repo = github_repo.split("/", 1)

    # Don't overwrite if this IS the main repo
    if github_repo == UPSTREAM:
        print(f"This is the main RAR repo ({UPSTREAM}). Skipping instance setup.")
        return 0

    config = {
        "schema": "rar-config/1.0",
        "role": "instance",
        "owner": owner,
        "repo": repo,
        "upstream": UPSTREAM,
        "federation": {
            "accept_submissions": True,
            "allow_upstream_sync": True,
        },
    }

    CONFIG_FILE.write_text(json.dumps(config, indent=2) + "\n")
    print(f"Configured as RAR instance: {owner}/{repo}")
    print(f"  Upstream: {UPSTREAM}")
    print(f"  Config:   {CONFIG_FILE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
