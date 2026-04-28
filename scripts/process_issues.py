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

# Default: a submitter can only publish under their own GitHub username
# (e.g. github user `BlazingBeard` can publish as `@BlazingBeard/...`).
# A brand namespace requires explicit authorization — only logins listed
# below can publish under it. Add new brand authorizations by editing
# this dict in a maintainer-merged PR; never via an issue submission.
# Keys are lowercased for case-insensitive matching.
BRAND_ALLOWLIST: dict[str, set[str]] = {
    "@rapp": {"kody-w"},
    "@kody": {"kody-w"},
    "@kody-w": {"kody-w"},
}


def _attestation_re():
    return re.compile(r"```attestation\s*\n(.*?)\n```", re.DOTALL)


def extract_attestation(body: str) -> dict | None:
    """Pull the ATTESTATION block emitted by `@rapp/rapp_publish_agent`
    (v0.2.0+). Returns a dict of keys → values, or None if no block."""
    if not body:
        return None
    m = _attestation_re().search(body)
    if not m:
        return None
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        k, v = line.split(":", 1)
        out[k.strip()] = v.strip()
    return out


def verify_attestation(att: dict, *, expected_submitter: str,
                        expected_name: str, content: bytes) -> str | None:
    """Verify an ATTESTATION block. Returns an error string on mismatch,
    or None on pass. Missing block (att=None) is the caller's call to
    handle — older publish agents pre-date this contract."""
    import hashlib as _h
    sub = (att.get("submitter") or "").lstrip("@").lower()
    if sub and sub != expected_submitter.lstrip("@").lower():
        return (f"Attestation submitter '@{sub}' does not match GitHub "
                f"issue author '@{expected_submitter}'. Refile from your "
                f"own account.")
    claimed = (att.get("claimed_name") or "").strip()
    if claimed and claimed != expected_name:
        return (f"Attestation claimed_name '{claimed}' differs from "
                f"resolved name '{expected_name}'.")
    declared_hash = (att.get("content_sha256") or "").strip()
    if declared_hash:
        actual = _h.sha256(content).hexdigest()
        if declared_hash != actual:
            return (f"Attestation content_sha256 '{declared_hash[:12]}…' "
                    f"does not match actual content hash "
                    f"'{actual[:12]}…'. Body may have been tampered with.")
    return None


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
      2. GitHub Gist link containing agent code (auto-fetches raw content)
      3. ```json fenced block with action JSON
      4. Raw JSON object with action
      5. ```python fenced block with agent code (auto-wraps as submit_agent)
      6. Raw Python with __manifest__ (auto-wraps as submit_agent)
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

    # Try GitHub Gist link — user linked a gist containing the agent code
    # Supports: https://gist.github.com/USER/HASH
    gist_match = re.search(
        r'https://gist\.github\.com/([\w-]+)/([a-f0-9]+)',
        body
    )
    if gist_match:
        gist_user, gist_id = gist_match.group(1), gist_match.group(2)
        raw_url = f"https://gist.githubusercontent.com/{gist_user}/{gist_id}/raw"
        code = _fetch_attachment(raw_url)
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
    # Auto-register binder if not already registered
    if not is_binder_registered(user):
        handle_register_binder({"namespace": f"@{user}"}, user)

    code = payload.get("code", "")
    if not code or not code.strip():
        return {"error": "Agent code is required"}

    # Reject unmodified template submissions
    if "@your_username/" in code or "YOUR LOGIC GOES HERE" in code or "RAPP AGENT TEMPLATE" in code:
        return {"error": "This is the unmodified template. Fill it in with your LLM first, then resubmit."}

    manifest = extract_manifest_from_code(code)
    if manifest is None:
        return {"error": "No valid __manifest__ dict found in agent code"}

    errors = validate_manifest(manifest)
    if errors:
        return {"error": f"Manifest validation failed: {'; '.join(errors)}"}

    tier = manifest.get("quality_tier", "unverified")
    if tier not in SUBMITTABLE_TIERS:
        # Auto-downgrade to community — submitters don't control tier
        tier = "community"
        code = re.sub(
            r'("quality_tier"\s*:\s*")[^"]+(")',
            r'\g<1>community\2',
            code
        )

    name = manifest["name"]
    parts = name.split("/")
    publisher = parts[0]
    slug = parts[1]

    # Auto-append _agent suffix if missing
    if not slug.endswith("_agent"):
        slug = slug + "_agent"
        name = f"{publisher}/{slug}"
        # Update manifest in the code so the file is correct
        code = re.sub(
            r'("name":\s*"@[^/]+/)[^"]+(")',
            rf'\g<1>{slug}\2',
            code
        )

    # Enforce snake_case filename
    if '-' in slug:
        return {
            "error": f"Agent slug '{slug}' contains dashes — must be snake_case "
                     f"(e.g., '{slug.replace('-', '_')}')"
        }

    # Namespace check: a submitter can only publish under their own
    # GitHub username — UNLESS the publisher namespace is explicitly
    # listed in BRAND_ALLOWLIST and the submitter is one of the logins
    # authorized for it. The previous title-fallback (publisher matched
    # if it appeared in the issue title) was a no-op security check —
    # the submitter controls the title — and let `BlazingBeard` publish
    # as `@howardh` in #70.
    expected_publisher = f"@{user}"
    pub_lc = publisher.lower()
    user_lc = user.lower()
    is_self = pub_lc == expected_publisher.lower()
    is_allowlisted_brand = (
        pub_lc in BRAND_ALLOWLIST
        and user_lc in {u.lower() for u in BRAND_ALLOWLIST[pub_lc]}
    )
    if not (is_self or is_allowlisted_brand):
        return {
            "error": f"Publisher must be '{expected_publisher}' (your "
                     f"GitHub username). Got '{publisher}'. Brand "
                     f"namespaces are gated on a maintainer-curated "
                     f"allowlist; if you need '{publisher}' authorized "
                     f"for your account, open a PR adding "
                     f"`{publisher}: [\"{user}\"]` to BRAND_ALLOWLIST in "
                     f"`scripts/process_issues.py`."
        }

    # Verify attestation block (rapp_publish_agent v0.2.0+).
    # Older publish agents that didn't emit one pass through — but they
    # also can't claim a brand namespace, so the BRAND_ALLOWLIST check
    # above is the primary gate.
    att = extract_attestation(payload.get("_issue_body") or "")
    if att is not None:
        att_err = verify_attestation(
            att,
            expected_submitter=user,
            expected_name=name,
            content=code.encode("utf-8"),
        )
        if att_err:
            return {"error": f"Attestation rejected: {att_err}"}

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

    # Pass the raw issue body through so handle_submit_agent can extract
    # and verify the ATTESTATION block emitted by rapp_publish_agent.
    if data.get("action") == "submit_agent":
        data.setdefault("payload", {})["_issue_body"] = body

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
