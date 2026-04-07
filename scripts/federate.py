#!/usr/bin/env python3
"""
Federation CLI — Manages the relationship between a RAPP binder and upstream.

Usage:
  python scripts/federate.py status              Show federation config
  python scripts/federate.py binder              Show binder: your agents, synced, pending
  python scripts/federate.py diff                Show local agents not in upstream
  python scripts/federate.py submit              Submit delta agents to upstream (goes to staging)
  python scripts/federate.py submit @me/agent    Submit a specific agent
  python scripts/federate.py sync                Check for upstream updates
  python scripts/federate.py sync --pull         Download new upstream agents locally
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = REPO_ROOT / "rar.config.json"
REGISTRY_FILE = REPO_ROOT / "registry.json"


# ──────────────────────────────────────────────────────────────────────
# Config & auth
# ──────────────────────────────────────────────────────────────────────

def load_config() -> dict | None:
    if not CONFIG_FILE.exists():
        return None
    return json.loads(CONFIG_FILE.read_text())


def get_token() -> str:
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        return token
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True, text=True, timeout=5,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return ""


def fetch_json(url: str, token: str = "") -> dict | None:
    headers = {"User-Agent": "RAR-Federation/1.0"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
        headers["Accept"] = "application/vnd.github.v3+json"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"  Failed to fetch {url}: {e}")
        return None


def fetch_text(url: str, token: str = "") -> str | None:
    headers = {"User-Agent": "RAR-Federation/1.0"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode()
    except Exception:
        return None


# ──────────────────────────────────────────────────────────────────────
# Commands
# ──────────────────────────────────────────────────────────────────────

def cmd_status(config: dict) -> int:
    role = config.get("role", "unknown")
    owner = config.get("owner", "?")
    repo = config.get("repo", "?")
    upstream = config.get("upstream")

    print(f"\nRAPP Federation Status")
    print(f"{'=' * 50}")
    print(f"  Role:     {role.upper()}")
    print(f"  Repo:     {owner}/{repo}")
    if upstream:
        print(f"  Upstream: {upstream}")
    else:
        print(f"  Upstream: (none — this is the main store)")
    print(f"  Config:   {CONFIG_FILE.relative_to(REPO_ROOT)}")

    fed = config.get("federation", {})
    print(f"\n  Accept submissions: {fed.get('accept_submissions', False)}")
    print(f"  Allow sync:        {fed.get('allow_upstream_sync', False)}")

    # Count local agents
    if REGISTRY_FILE.exists():
        reg = json.loads(REGISTRY_FILE.read_text())
        agents = reg.get("agents", [])
        stats = reg.get("stats", {})
        print(f"\n  Local agents:    {len(agents)}")
        print(f"  Publishers:      {stats.get('publishers', '?')}")
    print()
    return 0


def cmd_diff(config: dict) -> int:
    upstream = config.get("upstream")
    if not upstream:
        print("This is the main store — nothing to diff against.")
        return 0

    token = get_token()
    upstream_raw = f"https://raw.githubusercontent.com/{upstream}/main"

    print(f"\nComparing local registry against upstream ({upstream})...")

    # Load local
    if not REGISTRY_FILE.exists():
        print("Error: Local registry.json not found. Run build_registry.py first.")
        return 1
    local_reg = json.loads(REGISTRY_FILE.read_text())
    local_agents = {a["name"]: a for a in local_reg.get("agents", [])}

    # Load upstream
    upstream_reg = fetch_json(f"{upstream_raw}/registry.json", token)
    if not upstream_reg:
        print("Error: Could not fetch upstream registry.")
        return 1
    upstream_agents = {a["name"]: a for a in upstream_reg.get("agents", [])}

    # Compute delta
    new_agents = []
    updated_agents = []
    for name, agent in local_agents.items():
        if name not in upstream_agents:
            new_agents.append(agent)
        else:
            if agent.get("version", "") > upstream_agents[name].get("version", ""):
                updated_agents.append(agent)

    upstream_only = [
        a for name, a in upstream_agents.items() if name not in local_agents
    ]

    print(f"\n{'=' * 60}")
    print(f"  Federation Diff: {config['owner']}/{config['repo']} vs {upstream}")
    print(f"{'=' * 60}")
    print(f"\n  Local agents:    {len(local_agents)}")
    print(f"  Upstream agents: {len(upstream_agents)}")

    if new_agents:
        print(f"\n  NEW (local only — {len(new_agents)}):")
        for a in sorted(new_agents, key=lambda x: x["name"]):
            print(f"    + {a['name']} v{a['version']}  ({a.get('category', '?')})")

    if updated_agents:
        print(f"\n  UPDATED (newer version locally — {len(updated_agents)}):")
        for a in sorted(updated_agents, key=lambda x: x["name"]):
            old_v = upstream_agents[a["name"]].get("version", "?")
            print(f"    ~ {a['name']} v{old_v} -> v{a['version']}")

    if upstream_only:
        print(f"\n  UPSTREAM ONLY ({len(upstream_only)}):")
        for a in sorted(upstream_only, key=lambda x: x["name"])[:20]:
            print(f"    - {a['name']} v{a['version']}")
        if len(upstream_only) > 20:
            print(f"    ... and {len(upstream_only) - 20} more")

    if not new_agents and not updated_agents:
        print("\n  No local agents to submit upstream.")

    total_submittable = len(new_agents) + len(updated_agents)
    if total_submittable:
        print(f"\n  {total_submittable} agent(s) can be submitted to {upstream}.")
        print(f"  Run: python scripts/federate.py submit")

    print()
    return 0


def cmd_submit(config: dict, specific_agent: str | None = None) -> int:
    upstream = config.get("upstream")
    if not upstream:
        print("This is the main store — submit directly via the UI or Issues.")
        return 0

    token = get_token()
    if not token:
        print("Error: No GitHub token available.")
        print("  Set GITHUB_TOKEN env var or run `gh auth login`.")
        return 1

    upstream_raw = f"https://raw.githubusercontent.com/{upstream}/main"
    upstream_api = f"https://api.github.com/repos/{upstream}"

    # Load registries
    if not REGISTRY_FILE.exists():
        print("Error: Local registry.json not found.")
        return 1
    local_reg = json.loads(REGISTRY_FILE.read_text())
    local_agents = {a["name"]: a for a in local_reg.get("agents", [])}

    upstream_reg = fetch_json(f"{upstream_raw}/registry.json", token)
    upstream_agents = {}
    if upstream_reg:
        upstream_agents = {a["name"]: a for a in upstream_reg.get("agents", [])}

    # Determine what to submit
    if specific_agent:
        if specific_agent not in local_agents:
            print(f"Error: Agent '{specific_agent}' not found in local registry.")
            return 1
        to_submit = [local_agents[specific_agent]]
    else:
        to_submit = []
        for name, agent in local_agents.items():
            if name not in upstream_agents:
                to_submit.append(agent)
            elif agent.get("version", "") > upstream_agents[name].get("version", ""):
                to_submit.append(agent)

    if not to_submit:
        print("Nothing to submit — local registry matches upstream.")
        return 0

    print(f"\nSubmitting {len(to_submit)} agent(s) to {upstream}...\n")

    success = 0
    for agent in to_submit:
        name = agent["name"]
        filepath = REPO_ROOT / agent["_file"]

        if not filepath.exists():
            print(f"  SKIP {name} — file not found: {agent['_file']}")
            continue

        code = filepath.read_text()
        body_data = {
            "action": "submit_agent",
            "payload": {"code": code},
        }
        body_json = json.dumps(body_data, indent=2)
        issue_body = f"```json\n{body_json}\n```"

        payload = json.dumps({
            "title": f"[RAR] submit_agent",
            "body": issue_body,
            "labels": ["rar-action", "agent-submission", "federated"],
        }).encode()

        req = urllib.request.Request(
            f"{upstream_api}/issues",
            data=payload,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "Accept": "application/vnd.github.v3+json",
                "User-Agent": "RAR-Federation/1.0",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                result = json.loads(resp.read().decode())
                issue_url = result.get("html_url", "?")
                print(f"  OK  {name} v{agent['version']} -> {issue_url}")
                success += 1
        except urllib.error.HTTPError as e:
            err_body = e.read().decode()[:200] if e.fp else str(e)
            print(f"  FAIL {name} — {e.code}: {err_body}")
        except Exception as e:
            print(f"  FAIL {name} — {e}")

        # Rate limit: 1 second between submissions
        if len(to_submit) > 1:
            time.sleep(1)

    print(f"\nDone: {success}/{len(to_submit)} submitted successfully.")
    if success:
        print(f"\nSubmissions land in staging/ at {upstream} for review.")
        print(f"An admin will review and approve. Once approved:")
        print(f"  - Agent moves to agents/ in the main registry")
        print(f"  - Card is forged (details decided by the forge, not the submitter)")
        print(f"  - Agent is stamped into the next seasonal release")
        print(f"\nTrack your submissions: https://github.com/{upstream}/labels/pending-review")
    return 0 if success == len(to_submit) else 1


def cmd_binder(config: dict) -> int:
    """Show binder status — what's local, what's official, what's pending."""
    binder_file = REPO_ROOT / "binder" / "binder_state.json"
    owner = config.get("owner", "?")
    namespace = config.get("namespace", f"@{owner}")
    upstream = config.get("upstream")

    print(f"\nBinder: {namespace}")
    print(f"{'=' * 50}")

    # Count local agents
    local_agents = {}
    if REGISTRY_FILE.exists():
        reg = json.loads(REGISTRY_FILE.read_text())
        local_agents = {a["name"]: a for a in reg.get("agents", [])}

    my_agents = {n: a for n, a in local_agents.items() if n.startswith(namespace + "/")}
    synced = {n: a for n, a in local_agents.items() if not n.startswith(namespace + "/")}

    print(f"\n  Your agents ({namespace}/):  {len(my_agents)}")
    for name, a in sorted(my_agents.items()):
        tier = a.get("quality_tier", "community")
        card = "card" if a.get("_has_card") else "    "
        print(f"    [{tier:>11}] [{card}] {name} v{a['version']}")

    print(f"\n  Synced from upstream:      {len(synced)}")

    # Check staging
    staging = REPO_ROOT / "staging"
    staged = list(staging.rglob("*.py")) if staging.exists() else []
    staged = [f for f in staged if f.name != ".gitkeep"]
    if staged:
        print(f"\n  Pending upstream review:   {len(staged)}")
        for f in staged:
            print(f"    {f.relative_to(REPO_ROOT)}")

    # Binder state
    if binder_file.exists():
        state = json.loads(binder_file.read_text())
        owned = state.get("owned_cards", [])
        decks = state.get("decks", [])
        if owned:
            print(f"\n  Owned cards:               {len(owned)}")
        if decks:
            print(f"  Decks:                     {len(decks)}")

    pages_url = config.get("binder", {}).get("pages_url", "")
    if pages_url:
        print(f"\n  Binder URL: {pages_url}")

    print()
    return 0


def cmd_sync(config: dict, pull: bool = False) -> int:
    upstream = config.get("upstream")
    if not upstream:
        print("This is the main store — nothing to sync from.")
        return 0

    token = get_token()
    upstream_raw = f"https://raw.githubusercontent.com/{upstream}/main"

    print(f"\nSyncing from upstream ({upstream})...")

    # Load registries
    local_agents = {}
    if REGISTRY_FILE.exists():
        local_reg = json.loads(REGISTRY_FILE.read_text())
        local_agents = {a["name"]: a for a in local_reg.get("agents", [])}

    upstream_reg = fetch_json(f"{upstream_raw}/registry.json", token)
    if not upstream_reg:
        print("Error: Could not fetch upstream registry.")
        return 1
    upstream_agents = {a["name"]: a for a in upstream_reg.get("agents", [])}

    # Find what's upstream but not local
    missing = []
    updatable = []
    for name, agent in upstream_agents.items():
        if name not in local_agents:
            missing.append(agent)
        elif agent.get("version", "") > local_agents[name].get("version", ""):
            updatable.append(agent)

    print(f"\n  Upstream has {len(upstream_agents)} agents.")
    print(f"  Local has {len(local_agents)} agents.")

    if missing:
        print(f"\n  Available from upstream ({len(missing)}):")
        for a in sorted(missing, key=lambda x: x["name"])[:30]:
            tier = a.get("quality_tier", "community").upper()
            print(f"    [{tier}] {a['name']} v{a['version']}")
        if len(missing) > 30:
            print(f"    ... and {len(missing) - 30} more")

    if updatable:
        print(f"\n  Newer versions available ({len(updatable)}):")
        for a in sorted(updatable, key=lambda x: x["name"]):
            local_v = local_agents[a["name"]].get("version", "?")
            print(f"    {a['name']} v{local_v} -> v{a['version']}")

    if not missing and not updatable:
        print("\n  Local registry is up to date with upstream.")
        return 0

    if pull:
        to_pull = missing + updatable
        print(f"\n  Pulling {len(to_pull)} agent(s)...")
        pulled = 0
        for agent in to_pull:
            file_url = f"{upstream_raw}/{agent['_file']}"
            code = fetch_text(file_url, token)
            if not code:
                print(f"    FAIL {agent['name']} — could not download")
                continue

            dest = REPO_ROOT / agent["_file"]
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(code)
            print(f"    OK   {agent['name']} -> {agent['_file']}")
            pulled += 1

        print(f"\n  Pulled {pulled}/{len(to_pull)} agents.")
        if pulled:
            print("  Run `python build_registry.py` to update the local registry.")
    else:
        total = len(missing) + len(updatable)
        print(f"\n  {total} agent(s) available. Run with --pull to download:")
        print(f"  python scripts/federate.py sync --pull")

    print()
    return 0


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="RAPP Federation — manage instance/upstream relationship"
    )
    parser.add_argument(
        "command",
        choices=["status", "binder", "diff", "submit", "sync"],
        help="Federation command",
    )
    parser.add_argument(
        "agent",
        nargs="?",
        help="Specific agent name for submit (e.g. @alice/my_agent)",
    )
    parser.add_argument(
        "--pull",
        action="store_true",
        help="Download agents during sync",
    )
    args = parser.parse_args()

    config = load_config()
    if not config:
        print("Error: rar.config.json not found.")
        print("  If this is a template instance, run:")
        print("  GITHUB_REPOSITORY=user/repo python scripts/setup_instance.py")
        return 1

    commands = {
        "status": lambda: cmd_status(config),
        "binder": lambda: cmd_binder(config),
        "diff": lambda: cmd_diff(config),
        "submit": lambda: cmd_submit(config, args.agent),
        "sync": lambda: cmd_sync(config, args.pull),
    }

    return commands[args.command]()


if __name__ == "__main__":
    sys.exit(main())
