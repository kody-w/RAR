#!/usr/bin/env python3
"""
Instance Setup — Auto-configures rar.config.json and agents/ structure
when a repo is created from the RAPP template.

Creates:
  - rar.config.json (instance config, points upstream to main RAPP)
  - agents/@<owner>/ (your publisher namespace inside agents/)
  - staging/ directory (holds agents pending upstream submission)

Called by:  .github/workflows/template_setup.yml
Manual:    GITHUB_REPOSITORY=user/repo python scripts/setup_instance.py
"""

import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = REPO_ROOT / "rar.config.json"
STAGING_DIR = REPO_ROOT / "staging"
UPSTREAM = "kody-w/RAR"


def main() -> int:
    github_repo = os.environ.get("GITHUB_REPOSITORY", "")
    if not github_repo or "/" not in github_repo:
        print("Error: GITHUB_REPOSITORY env var must be set (e.g. 'alice/my-agents')")
        return 1

    owner, repo = github_repo.split("/", 1)

    # Don't overwrite if this IS the main repo
    if github_repo == UPSTREAM:
        print(f"This is the main RAPP repo ({UPSTREAM}). Skipping instance setup.")
        return 0

    # Write instance config
    config = {
        "schema": "rar-config/1.0",
        "role": "instance",
        "owner": owner,
        "repo": repo,
        "upstream": UPSTREAM,
        "namespace": f"@{owner}",
        "federation": {
            "accept_submissions": True,
            "allow_upstream_sync": True,
        },
        "pages_url": f"https://{owner}.github.io/{repo}/",
    }

    CONFIG_FILE.write_text(json.dumps(config, indent=2) + "\n")

    # Create staging directory
    STAGING_DIR.mkdir(exist_ok=True)
    gitkeep = STAGING_DIR / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.write_text("")

    # Create publisher namespace dir
    ns_dir = REPO_ROOT / "agents" / f"@{owner}"
    ns_dir.mkdir(parents=True, exist_ok=True)

    print(f"Configured as RAPP instance: {owner}/{repo}")
    print(f"  Upstream:   {UPSTREAM}")
    print(f"  Namespace:  @{owner}")
    print(f"  Agents:     agents/@{owner}/")
    print(f"  Staging:    {STAGING_DIR.relative_to(REPO_ROOT)}/")
    print(f"  Pages URL:  https://{owner}.github.io/{repo}/")
    print(f"  Config:     {CONFIG_FILE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
