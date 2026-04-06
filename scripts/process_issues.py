#!/usr/bin/env python3
"""
Issue Processor — Turns GitHub Issues into state mutations.

Follows the RAPPterBook pattern:
  Issue (JSON body) --> validate --> mutate state/*.json --> commit --> close issue

Supported actions:
  vote           - Upvote/downvote an agent
  review         - Submit a text review with rating
  submit_agent   - Submit a community agent.py for inclusion

Usage (called by GitHub Actions):
  python scripts/process_issues.py --event-path $GITHUB_EVENT_PATH
  python scripts/process_issues.py --test '{"action":"vote",...}'
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = REPO_ROOT / "state"
AGENTS_DIR = REPO_ROOT / "agents"
STAGING_DIR = REPO_ROOT / "staging"
VOTES_FILE = STATE_DIR / "votes.json"
REVIEWS_FILE = STATE_DIR / "reviews.json"
LEDGER_FILE = STATE_DIR / "binder_ledger.json"

REQUIRED_MANIFEST_FIELDS = [
    "schema", "name", "version", "display_name",
    "description", "author", "tags", "category",
]

VALID_TIERS = {"official", "verified", "community", "experimental", "unverified"}
SUBMITTABLE_TIERS = {"unverified", "community", "experimental"}


# ──────────────────────────────────────────────────────────────────────
# State I/O
# ──────────────────────────────────────────────────────────────────────

def load_json(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {}


def save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2) + "\n")
    tmp.replace(path)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ──────────────────────────────────────────────────────────────────────
# Parsing
# ──────────────────────────────────────────────────────────────────────

def _fetch_attachment(url: str) -> str | None:
    """Fetch a file attachment from a GitHub Issue URL."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "RAR-Pipeline/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode()
    except Exception:
        return None


def extract_json_from_body(body: str) -> dict:
    """Extract action from issue body.

    Supports:
      1. Dragged-and-dropped .py file attachment (auto-fetches, auto-wraps)
      2. ```json fenced block with action JSON
      3. Raw JSON object with action
      4. ```python fenced block with agent code (auto-wraps as submit_agent)
      5. Raw Python with __manifest__ (auto-wraps as submit_agent)
    """
    if not body or not body.strip():
        raise ValueError("Issue body is empty")

    # Try file attachment first — user dragged a .py file into the issue
    # GitHub renders as: [filename.py](https://github.com/user-attachments/assets/UUID)
    # or sometimes:      https://github.com/user-attachments/assets/UUID
    attach_match = re.search(
        r'\[([^\]]*\.py)\]\((https://github\.com/user-attachments/assets/[^\)]+)\)',
        body
    )
    if not attach_match:
        # Try bare URL pattern
        attach_match = re.search(
            r'(https://github\.com/user-attachments/assets/[a-f0-9\-]+)',
            body
        )
    if attach_match:
        url = attach_match.group(2) if attach_match.lastindex and attach_match.lastindex >= 2 else attach_match.group(1)
        code = _fetch_attachment(url)
        if code and "__manifest__" in code:
            return {"action": "submit_agent", "payload": {"code": code}}

    # Try fenced JSON block
    match = re.search(r"```json\s*\n(.*?)\n\s*```", body, re.DOTALL)
    if match:
        return json.loads(match.group(1))

    # Try raw JSON
    stripped = body.strip()
    if stripped.startswith("{"):
        try:
            return json.loads(stripped)
        except json.JSONDecodeError:
            pass

    # Try fenced Python block — auto-wrap as submit_agent
    py_match = re.search(r"```(?:python)?\s*\n(.*?)\n\s*```", body, re.DOTALL)
    if py_match:
        code = py_match.group(1)
        if "__manifest__" in code:
            return {"action": "submit_agent", "payload": {"code": code}}

    # Try raw Python (has __manifest__ and looks like Python)
    if "__manifest__" in stripped and ("class " in stripped or "def " in stripped):
        return {"action": "submit_agent", "payload": {"code": stripped}}

    raise ValueError("No valid JSON or Python agent code found in issue body")


def extract_manifest_from_code(code: str) -> dict | None:
    """Extract __manifest__ from agent source code using AST."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__manifest__":
                    try:
                        return ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        return None
    return None


# ──────────────────────────────────────────────────────────────────────
# Validators
# ──────────────────────────────────────────────────────────────────────

def validate_agent_name(name: str) -> str | None:
    """Return error string if agent name is invalid, else None."""
    if not name or not isinstance(name, str):
        return "Agent name is required"
    if not name.startswith("@") or "/" not in name:
        return f"Invalid agent name '{name}' — must be @publisher/slug"
    return None


def validate_manifest(manifest: dict) -> list[str]:
    """Return list of validation errors for a manifest."""
    errors = []
    for field in REQUIRED_MANIFEST_FIELDS:
        if field not in manifest:
            errors.append(f"Missing required field: {field}")

    name = manifest.get("name", "")
    err = validate_agent_name(name)
    if err:
        errors.append(err)

    version = manifest.get("version", "")
    parts = version.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        errors.append(f"Invalid version '{version}' — must be semver")

    if not isinstance(manifest.get("tags", []), list):
        errors.append("tags must be a list")

    tier = manifest.get("quality_tier", "unverified")
    if tier not in VALID_TIERS:
        errors.append(
            f"Invalid quality_tier '{tier}' — must be one of: "
            f"{', '.join(sorted(VALID_TIERS))}"
        )

    return errors


# ──────────────────────────────────────────────────────────────────────
# Action handlers
# ──────────────────────────────────────────────────────────────────────

def handle_vote(payload: dict, user: str) -> dict:
    """Process a vote action. Returns {"ok": True} or {"error": "..."}."""
    agent = payload.get("agent", "")
    direction = payload.get("direction", "up")

    err = validate_agent_name(agent)
    if err:
        return {"error": err}
    if direction not in ("up", "down"):
        return {"error": f"Invalid direction '{direction}' — must be 'up' or 'down'"}

    votes = load_json(VOTES_FILE)
    if "agents" not in votes:
        votes["agents"] = {}

    agent_votes = votes["agents"].setdefault(agent, {
        "up": 0, "down": 0, "score": 0, "voters": {}
    })

    prev = agent_votes["voters"].get(user)
    if prev == direction:
        # Undo vote (toggle off)
        agent_votes["voters"].pop(user)
        agent_votes[direction] -= 1
    else:
        # Remove previous vote if switching
        if prev:
            agent_votes[prev] -= 1
        agent_votes["voters"][user] = direction
        agent_votes[direction] += 1

    agent_votes["score"] = agent_votes["up"] - agent_votes["down"]
    votes["updated_at"] = now_iso()
    save_json(VOTES_FILE, votes)

    return {"ok": True, "agent": agent, "direction": direction, "score": agent_votes["score"]}


def handle_review(payload: dict, user: str) -> dict:
    """Process a review action."""
    agent = payload.get("agent", "")
    rating = payload.get("rating")
    text = payload.get("text", "")

    err = validate_agent_name(agent)
    if err:
        return {"error": err}
    if not isinstance(rating, (int, float)) or not (1 <= rating <= 5):
        return {"error": "Rating must be a number between 1 and 5"}
    if not text or not text.strip():
        return {"error": "Review text is required"}
    if len(text) > 2000:
        return {"error": "Review text must be under 2000 characters"}

    reviews = load_json(REVIEWS_FILE)
    if "agents" not in reviews:
        reviews["agents"] = {}

    agent_reviews = reviews["agents"].setdefault(agent, [])

    # Replace existing review from same user
    agent_reviews = [r for r in agent_reviews if r.get("user") != user]
    agent_reviews.append({
        "user": user,
        "rating": int(rating),
        "text": text.strip(),
        "timestamp": now_iso(),
    })

    reviews["agents"][agent] = agent_reviews
    reviews["updated_at"] = now_iso()
    save_json(REVIEWS_FILE, reviews)

    return {"ok": True, "agent": agent, "rating": rating}


def handle_submit_agent(payload: dict, user: str) -> dict:
    """Process an agent submission. Validates manifest and writes to staging/.

    Requires a registered binder. Agents land in staging/ for review — NOT in agents/.
    Admin approval (via label or workflow) promotes staging → agents and triggers card forge.
    """
    # Ledger check: binder must be registered
    if not is_binder_registered(user):
        return {
            "error": (
                f"No registered binder for '{user}'. "
                "Register first by opening an Issue with: "
                '{"action": "register_binder", "payload": {"namespace": "@' + user + '"}}  '
                "Your binder can be public or private."
            )
        }

    code = payload.get("code", "")
    if not code or not code.strip():
        return {"error": "Agent code is required"}

    manifest = extract_manifest_from_code(code)
    if manifest is None:
        return {"error": "No valid __manifest__ dict found in agent code"}

    errors = validate_manifest(manifest)
    if errors:
        return {"error": f"Manifest validation failed: {'; '.join(errors)}"}

    tier = manifest.get("quality_tier", "unverified")
    if tier not in SUBMITTABLE_TIERS:
        return {
            "error": f"quality_tier '{tier}' cannot be used for submissions. "
                     f"Allowed: {', '.join(sorted(SUBMITTABLE_TIERS))}"
        }

    name = manifest["name"]
    parts = name.split("/")
    publisher = parts[0]
    slug = parts[1]

    # Enforce snake_case filename
    if '-' in slug:
        return {
            "error": f"Agent slug '{slug}' contains dashes — must be snake_case "
                     f"(e.g., '{slug.replace('-', '_')}')"
        }

    # Namespace check: publisher must match GitHub username,
    # UNLESS the issue title explicitly declares the agent name (e.g. [AGENT] @borg/sherlock).
    # This allows maintainers to grant namespace access by accepting the issue.
    expected_publisher = f"@{user}"
    title_ns = payload.get("_title_namespace")  # injected by dispatcher
    if publisher != expected_publisher and publisher != title_ns:
        return {
            "error": f"Publisher must be '{expected_publisher}' for community submissions. "
                     f"Got '{publisher}'. To use a reserved namespace, include it in the "
                     f"issue title: [AGENT] {name}"
        }

    # Check if already in agents/ — version must be greater
    agent_file = AGENTS_DIR / publisher / f"{slug}.py"
    if agent_file.exists():
        existing_manifest = extract_manifest_from_code(agent_file.read_text())
        if existing_manifest:
            new_v = manifest.get("version", "0.0.0")
            old_v = existing_manifest.get("version", "0.0.0")
            if new_v <= old_v:
                return {
                    "error": f"Version {new_v} must be greater than existing {old_v}"
                }

    # Write to staging/ — NOT agents/. Approval promotes it later.
    staging_dir = STAGING_DIR / publisher
    staging_file = staging_dir / f"{slug}.py"
    staging_dir.mkdir(parents=True, exist_ok=True)
    staging_file.write_text(code)

    return {
        "ok": True,
        "agent": name,
        "file": str(staging_file.relative_to(REPO_ROOT)),
        "status": "pending_review",
    }


def handle_register_binder(payload: dict, user: str) -> dict:
    """Register a binder on the public ledger.

    Any GitHub user can register. Their binder can be public or private —
    we only store that they exist and their namespace. The GitHub username
    IS the identity (proven by the token that created the Issue).
    """
    repo_url = payload.get("repo", "")
    namespace = payload.get("namespace", f"@{user}")

    # Validate namespace format
    if not namespace.startswith("@"):
        namespace = f"@{namespace}"

    ledger = load_json(LEDGER_FILE)
    if "binders" not in ledger:
        ledger["binders"] = {}

    # Check if already registered
    if user in ledger["binders"]:
        existing = ledger["binders"][user]
        return {
            "ok": True,
            "status": "already_registered",
            "user": user,
            "namespace": existing.get("namespace", namespace),
            "registered_at": existing.get("registered_at", ""),
        }

    # Register
    ledger["binders"][user] = {
        "namespace": namespace,
        "repo": repo_url,
        "registered_at": now_iso(),
    }
    ledger["updated_at"] = now_iso()
    save_json(LEDGER_FILE, ledger)

    return {
        "ok": True,
        "status": "registered",
        "user": user,
        "namespace": namespace,
    }


def is_binder_registered(user: str) -> bool:
    """Check if a user has a registered binder on the ledger."""
    ledger = load_json(LEDGER_FILE)
    return user in ledger.get("binders", {})


# ──────────────────────────────────────────────────────────────────────
# Dispatcher
# ──────────────────────────────────────────────────────────────────────

HANDLERS = {
    "vote": handle_vote,
    "review": handle_review,
    "submit_agent": handle_submit_agent,
    "register_binder": handle_register_binder,
}


def process(data: dict, user: str) -> dict:
    """Route an action to its handler."""
    action = data.get("action", "")
    if action not in HANDLERS:
        return {"error": f"Unknown action '{action}'. Valid: {', '.join(HANDLERS.keys())}"}

    payload = data.get("payload", {})
    if not isinstance(payload, dict):
        return {"error": "payload must be a JSON object"}

    return HANDLERS[action](payload, user)


# ──────────────────────────────────────────────────────────────────────
# CLI entry point
# ──────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="Process GitHub Issue into state mutation")
    parser.add_argument("--event-path", help="Path to GitHub event JSON")
    parser.add_argument("--test", help="Raw JSON string for testing")
    args = parser.parse_args()

    if args.test:
        data = json.loads(args.test)
        user = data.pop("_user", "test-user")
        result = process(data, user)
        print(json.dumps(result, indent=2))
        return 0 if result.get("ok") else 1

    if args.event_path:
        event = json.loads(Path(args.event_path).read_text())
    else:
        event = json.loads(sys.stdin.read())

    issue = event.get("issue", {})
    user = issue.get("user", {}).get("login", "unknown")
    body = issue.get("body", "")
    title = issue.get("title", "")
    issue_number = issue.get("number", 0)

    # Skip issues with special labels
    labels = [l.get("name", "") for l in issue.get("labels", [])]
    if any(l in labels for l in ("operator-directive", "skip-processing")):
        print(f"Skipping issue #{issue_number} (special label)")
        return 0

    try:
        data = extract_json_from_body(body)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"::error::Failed to parse issue #{issue_number}: {e}")
        # Output for the workflow to comment on the issue
        print(f"RESULT_ERROR=Could not parse JSON from issue body: {e}")
        return 1

    # Extract namespace from title (e.g. "[AGENT] @borg/sherlock" → "@borg")
    # This grants namespace access when the title explicitly declares the agent
    title_ns_match = re.search(r"\[(?:AGENT|RAR)\]\s*(@[\w-]+)/", title)
    if title_ns_match and data.get("action") == "submit_agent":
        data.setdefault("payload", {})["_title_namespace"] = title_ns_match.group(1)

    result = process(data, user)
    result_json = json.dumps(result, indent=2)
    print(result_json)

    # Write result for the workflow to use
    github_output = os.environ.get("GITHUB_OUTPUT", "")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"result={json.dumps(result)}\n")
            f.write(f"success={'true' if result.get('ok') else 'false'}\n")

    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
