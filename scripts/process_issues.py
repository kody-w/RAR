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
import hashlib
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = REPO_ROOT / "state"
AGENTS_DIR = REPO_ROOT / "agents"
STAGING_DIR = REPO_ROOT / "staging"
VOTES_FILE = STATE_DIR / "votes.json"
REVIEWS_FILE = STATE_DIR / "reviews.json"
LIFECYCLE_FILE = STATE_DIR / "agent_lifecycle.json"

CHANGE_REQUEST_SCHEMA = "rar-change-request/1.0"
RECEIPT_SCHEMA = "rar-receipt/1.0"

REQUIRED_MANIFEST_FIELDS = [
    "schema", "name", "version", "display_name",
    "description", "author", "tags", "category",
]

VALID_TIERS = {"official", "verified", "community", "experimental", "unverified"}
SUBMITTABLE_TIERS = {"unverified", "community", "experimental"}
REMOTE_SOURCE_LIMIT = 2 * 1024 * 1024
REMOTE_SOURCE_HOSTS = {
    "github.com",
    "gist.githubusercontent.com",
    "raw.githubusercontent.com",
}

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
    "@borg": {"howardh", "kody-w"},
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


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def semver_key(value: str) -> tuple[int, int, int] | None:
    parts = value.split(".")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        return None
    return tuple(int(part) for part in parts)


def canonical_json(data: dict) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


MUTATION_REVISION_FIELDS = (
    "schema",
    "request_id",
    "client_request_id",
    "idempotency_key",
    "client_command_sha256",
    "action",
    "agent",
    "actor_id",
    "source_body_sha256",
    "candidate_sha256",
    "candidate_version",
    "candidate_quality_tier",
    "source_url",
    "base_sha256",
    "base_version",
    "base_quality_tier",
    "base_lifecycle_sha256",
    "base_lifecycle_version",
    "base_lifecycle_receipt",
    "reason",
    "publisher",
    "slug",
    "canonical_path",
)


def mutation_revision_basis(data: dict) -> dict:
    return {
        field: data.get(field, "")
        for field in MUTATION_REVISION_FIELDS
    }


def mutation_revision_id(data: dict) -> str:
    return sha256_bytes(
        canonical_json(mutation_revision_basis(data)).encode("utf-8")
    )


def normalize_change_request(data: dict) -> dict:
    """Adapt the versioned CRUD envelope to the legacy action/payload shape."""
    if data.get("schema") != CHANGE_REQUEST_SCHEMA:
        return data

    operation = data.get("operation", "")
    if operation not in {"create", "read", "update", "delete", "restore"}:
        return {
            "action": "invalid",
            "payload": {
                "_normalization_error": (
                    f"Unsupported operation '{operation}' for {CHANGE_REQUEST_SCHEMA}"
                )
            },
        }

    resource = data.get("resource") or {}
    if resource.get("kind") != "agent":
        return {
            "action": "invalid",
            "payload": {
                "_normalization_error": "resource.kind must be 'agent'"
            },
        }
    preconditions = data.get("preconditions") or {}
    body_payload = data.get("payload") or {}
    source = body_payload.get("source") or {}
    payload = {
        "agent": resource.get("id", ""),
        "code": source.get("content", ""),
        "source_sha256": source.get("sha256", ""),
        "source_url": source.get("url", ""),
        "if_match": preconditions.get("if_match", ""),
        "if_none_match": preconditions.get("if_none_match", ""),
        "reason": body_payload.get("reason", ""),
        "request_id": data.get("request_id", ""),
        "idempotency_key": data.get("idempotency_key", ""),
        "_versioned": True,
    }
    return {"action": f"agent.{operation}", "payload": payload}


# ──────────────────────────────────────────────────────────────────────
# Parsing
# ──────────────────────────────────────────────────────────────────────

def _fetch_attachment(url: str) -> str | None:
    """Fetch a bounded GitHub-hosted source attachment."""
    try:
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme != "https" or parsed.hostname not in REMOTE_SOURCE_HOSTS:
            return None
        if parsed.hostname == "github.com" and not parsed.path.startswith(
            "/user-attachments/assets/"
        ):
            return None
        req = urllib.request.Request(url, headers={"User-Agent": "RAR-Pipeline/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            final = urllib.parse.urlparse(resp.geturl())
            github_asset_redirect = (
                parsed.hostname == "github.com"
                and parsed.path.startswith("/user-attachments/assets/")
                and re.fullmatch(
                    r"github-production-user-asset-[a-z0-9]+\.s3\.amazonaws\.com",
                    final.hostname or "",
                )
            )
            if final.scheme != "https" or not (
                final.hostname in REMOTE_SOURCE_HOSTS or github_asset_redirect
            ):
                return None
            declared_size = resp.headers.get("Content-Length")
            if declared_size and int(declared_size) > REMOTE_SOURCE_LIMIT:
                return None
            content = resp.read(REMOTE_SOURCE_LIMIT + 1)
            if len(content) > REMOTE_SOURCE_LIMIT:
                return None
            return content.decode("utf-8")
    except (
        OSError,
        UnicodeDecodeError,
        ValueError,
        urllib.error.HTTPError,
        urllib.error.URLError,
    ):
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

    # Versioned JSON commands take precedence over any URLs contained inside
    # their source locator fields.
    fence = re.search(r"```json\s*\n", body)
    if fence:
        candidate = body[fence.end():].lstrip()
        value, _end = json.JSONDecoder().raw_decode(candidate)
        if not isinstance(value, dict):
            raise ValueError("Issue command must be a JSON object")
        return value

    stripped = body.strip()
    if stripped.startswith("{"):
        try:
            value = json.loads(stripped)
            if not isinstance(value, dict):
                raise ValueError("Issue command must be a JSON object")
            return value
        except json.JSONDecodeError:
            pass

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


def replace_manifest_string_field(code: str, field: str, value: str) -> str | None:
    """Replace one string field in __manifest__ using AST byte positions."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None

    value_node = None
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == "__manifest__"
            for target in node.targets
        ):
            continue
        if not isinstance(node.value, ast.Dict):
            return None
        for key_node, candidate in zip(node.value.keys, node.value.values):
            if (
                isinstance(key_node, ast.Constant)
                and key_node.value == field
                and isinstance(candidate, ast.Constant)
                and isinstance(candidate.value, str)
            ):
                value_node = candidate
                break
        break

    if value_node is None or value_node.end_lineno is None:
        return None

    encoded = code.encode("utf-8")
    encoded_lines = code.encode("utf-8").splitlines(keepends=True)
    line_offsets = [0]
    for line in encoded_lines:
        line_offsets.append(line_offsets[-1] + len(line))
    start = line_offsets[value_node.lineno - 1] + value_node.col_offset
    end = line_offsets[value_node.end_lineno - 1] + value_node.end_col_offset
    replacement = json.dumps(value, ensure_ascii=True).encode("utf-8")
    return (encoded[:start] + replacement + encoded[end:]).decode("utf-8")


def validate_candidate_contract(code: str, manifest: dict) -> list[str]:
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        return [f"Python syntax error: {exc}"]
    candidates = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        has_perform = any(
            isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef))
            and member.name == "perform"
            for member in node.body
        )
        if not has_perform:
            continue
        inherits_basic = any(
            (isinstance(base, ast.Name) and base.id == "BasicAgent")
            or (isinstance(base, ast.Attribute) and base.attr == "BasicAgent")
            for base in node.bases
        )
        foundational_basic = (
            manifest.get("name") == "@rapp/basic_agent"
            and node.name == "BasicAgent"
        )
        if inherits_basic or foundational_basic:
            candidates.append(node.name)
    if not candidates:
        return ["Agent must define a BasicAgent subclass with perform()"]
    return []


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
    if semver_key(version) is None:
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


def _normalize_agent_identity(
    name: str,
    user: str,
) -> tuple[str, str, str] | tuple[None, None, str]:
    err = validate_agent_name(name)
    if err:
        return None, None, err

    parts = name.split("/")
    if len(parts) != 2:
        return None, None, f"Invalid agent name '{name}'"
    publisher, slug = parts
    if not slug.endswith("_agent"):
        slug += "_agent"
    if not re.fullmatch(r"[a-z0-9_]+", slug) or "-" in slug:
        return (
            None,
            None,
            f"Agent slug '{slug}' must be lowercase snake_case and end in _agent",
        )

    expected_publisher = f"@{user}"
    pub_lc = publisher.lower()
    user_lc = user.lower()
    is_self = pub_lc == expected_publisher.lower()
    is_allowlisted_brand = (
        pub_lc in BRAND_ALLOWLIST
        and user_lc in {allowed.lower() for allowed in BRAND_ALLOWLIST[pub_lc]}
    )
    if not (is_self or is_allowlisted_brand):
        return (
            None,
            None,
            f"Publisher must be '{expected_publisher}' (your GitHub username). "
            f"Got '{publisher}'.",
        )
    canonical_publisher = expected_publisher if is_self else pub_lc
    return canonical_publisher, slug, ""


def resolve_registered_agent(name: str) -> tuple[Path, dict] | None:
    candidates = []
    registry_file = REPO_ROOT / "registry.json"
    if registry_file.exists():
        try:
            registry = json.loads(registry_file.read_text(encoding="utf-8"))
            for entry in registry.get("agents", []):
                if str(entry.get("name", "")).casefold() != name.casefold():
                    continue
                path = REPO_ROOT / str(entry.get("_file", ""))
                try:
                    path.resolve().relative_to(AGENTS_DIR.resolve())
                except ValueError:
                    continue
                if path.exists():
                    manifest = extract_manifest_from_code(
                        path.read_text(encoding="utf-8")
                    )
                    if manifest and manifest.get("name") == entry.get("name"):
                        return path, manifest
        except (OSError, json.JSONDecodeError):
            pass

    patterns = ("*.py.card", "*.py.stub", "*.py")
    for priority, pattern in enumerate(patterns):
        for path in AGENTS_DIR.rglob(pattern):
            manifest = extract_manifest_from_code(path.read_text(encoding="utf-8"))
            if (
                manifest
                and str(manifest.get("name", "")).casefold() == name.casefold()
            ):
                candidates.append((priority, path, manifest))
    if not candidates:
        return None
    candidates.sort(key=lambda item: (item[0], str(item[1])))
    return candidates[0][1], candidates[0][2]


def _normalize_digest(value: str) -> str:
    value = (value or "").strip().lower()
    return value.removeprefix("sha256:")


def _issue_operation_key(payload: dict) -> str:
    context = payload.get("_context")
    if not isinstance(context, dict):
        return ""
    issue_identity = context.get("issue_node_id") or context.get("issue_number")
    body_sha256 = context.get("source_body_sha256") or sha256_bytes(
        str(payload.get("_issue_body") or "").encode("utf-8")
    )
    if not issue_identity:
        return ""
    return f"{issue_identity}:{body_sha256}"


def _request_context(payload: dict, user: str) -> dict:
    context = payload.get("_context")
    if not isinstance(context, dict):
        context = {}
    actor_id = context.get("actor_id")
    issue_number = context.get("issue_number")
    issue_node_id = context.get("issue_node_id")
    repository_id = context.get("repository_id")
    client_request_id = payload.get("request_id") or context.get("request_id")
    idempotency_key = str(payload.get("idempotency_key") or "")
    if idempotency_key and not re.fullmatch(
        r"[A-Za-z0-9_.:-]{8,128}",
        idempotency_key,
    ):
        raise ValueError("idempotency_key must be 8-128 URL-safe characters")
    if issue_node_id or issue_number:
        request_basis = {
            "repository_id": repository_id or "local",
            "issue_node_id": issue_node_id or issue_number or "local",
            "actor_id": actor_id or user.lower(),
        }
        request_id = f"req_{sha256_bytes(canonical_json(request_basis).encode())[:24]}"
    else:
        request_id = client_request_id
        if not request_id:
            request_basis = {
                "repository_id": "local",
                "issue_node_id": "local",
                "actor_id": actor_id or user.lower(),
            }
            request_id = (
                f"req_{sha256_bytes(canonical_json(request_basis).encode())[:24]}"
            )
    if not re.fullmatch(r"[A-Za-z0-9_.:-]{8,128}", request_id):
        raise ValueError("request_id must be 8-128 URL-safe characters")
    return {
        "request_id": request_id,
        "client_request_id": client_request_id or "",
        "idempotency_key": idempotency_key,
        "issue_number": issue_number or 0,
        "issue_node_id": issue_node_id or "",
        "repository_id": repository_id or "",
        "actor_id": actor_id or user,
        "actor_login": user,
        "issue_updated_at": context.get("issue_updated_at") or "",
        "source_body_sha256": sha256_bytes(
            str(payload.get("_issue_body") or "").encode("utf-8")
        ),
    }


def _client_command_sha256(
    *,
    action: str,
    agent: str,
    actor_id: int | str,
    candidate_sha256: str,
    candidate_version: str,
    candidate_quality_tier: str,
    payload: dict,
) -> str:
    client_command = {
        "action": action,
        "agent": agent,
        "actor_id": actor_id,
        "candidate_sha256": candidate_sha256,
        "candidate_version": candidate_version,
        "candidate_quality_tier": candidate_quality_tier,
        "source_url": str(payload.get("source_url") or ""),
        "if_match": _normalize_digest(payload.get("if_match", "")),
        "if_none_match": str(payload.get("if_none_match") or ""),
        "reason": str(payload.get("reason") or ""),
    }
    return sha256_bytes(canonical_json(client_command).encode("utf-8"))


def _idempotent_request_result(
    *,
    context: dict,
    client_command_sha256: str,
) -> dict | None:
    if not context["idempotency_key"]:
        return None
    roots = [STAGING_DIR / "requests", STATE_DIR / "requests"]
    for root in roots:
        if not root.exists():
            continue
        pattern = "*/*/request.json" if root == roots[0] else "*/*.json"
        for existing_file in root.glob(pattern):
            existing = json.loads(existing_file.read_text(encoding="utf-8"))
            if (
                existing.get("idempotency_key") == context["idempotency_key"]
                and str(existing.get("actor_id")) == str(context["actor_id"])
                and str(existing.get("repository_id"))
                == str(context["repository_id"])
            ):
                if existing.get("client_command_sha256") != client_command_sha256:
                    return {
                        "error": "Idempotency key conflicts with another command"
                    }
                same_issue = (
                    existing.get("issue_number") == context.get("issue_number")
                    and existing.get("issue_node_id") == context.get("issue_node_id")
                )
                if (
                    existing.get("status") == "pending_review"
                    and same_issue
                    and existing.get("source_body_sha256")
                    != context.get("source_body_sha256")
                ):
                    return None
                return {
                    "ok": True,
                    "action": existing["action"],
                    "agent": existing["agent"],
                    "request_id": existing["request_id"],
                    "revision_id": existing["revision_id"],
                    "candidate_sha256": existing.get("candidate_sha256", ""),
                    "file": str(existing_file.relative_to(REPO_ROOT)),
                    "status": (
                        "pending_review"
                        if existing.get("status") == "pending_review" and same_issue
                        else "duplicate"
                    ),
                }
    return None


def _stage_request(
    *,
    action: str,
    agent: str,
    publisher: str,
    slug: str,
    user: str,
    payload: dict,
    candidate_code: str | None,
    candidate_version: str | None,
    candidate_quality_tier: str | None,
    base_file: Path | None,
    base_lifecycle: dict | None = None,
    canonical_path: str | None = None,
) -> dict:
    try:
        context = _request_context(payload, user)
    except ValueError as exc:
        return {"error": str(exc)}

    base_sha256 = ""
    base_version = ""
    base_quality_tier = ""
    base_lifecycle_sha256 = ""
    base_lifecycle_version = ""
    base_lifecycle_receipt = ""
    if base_file is not None and base_file.exists():
        base_content = base_file.read_bytes()
        base_sha256 = sha256_bytes(base_content)
        base_manifest = extract_manifest_from_code(base_content.decode("utf-8"))
        if base_manifest:
            base_version = str(base_manifest.get("version", ""))
            base_quality_tier = str(
                base_manifest.get("quality_tier", "community")
            )
    if base_lifecycle:
        base_lifecycle_sha256 = str(base_lifecycle.get("sha256", ""))
        base_lifecycle_version = str(base_lifecycle.get("version", ""))
        base_lifecycle_receipt = str(base_lifecycle.get("latest_receipt", ""))

    expected = _normalize_digest(payload.get("if_match", ""))
    if expected and expected != base_sha256:
        return {
            "error": (
                f"Precondition failed for {agent}: expected sha256:{expected}, "
                f"current is sha256:{base_sha256 or 'absent'}"
            )
        }

    candidate_sha256 = ""
    if candidate_code is not None:
        candidate_sha256 = sha256_bytes(candidate_code.encode("utf-8"))
        declared = _normalize_digest(payload.get("source_sha256", ""))
        if declared and declared != candidate_sha256:
            return {
                "error": (
                    f"Source digest mismatch: declared sha256:{declared}, "
                    f"actual sha256:{candidate_sha256}"
                )
            }

    client_command_sha256 = _client_command_sha256(
        action=action,
        agent=agent,
        actor_id=context["actor_id"],
        candidate_sha256=candidate_sha256,
        candidate_version=candidate_version or "",
        candidate_quality_tier=candidate_quality_tier or "",
        payload=payload,
    )
    duplicate = _idempotent_request_result(
        context=context,
        client_command_sha256=client_command_sha256,
    )
    if duplicate is not None:
        return duplicate

    revision_basis = {
        "schema": CHANGE_REQUEST_SCHEMA,
        "request_id": context["request_id"],
        "client_request_id": context["client_request_id"],
        "idempotency_key": context["idempotency_key"],
        "client_command_sha256": client_command_sha256,
        "action": action,
        "agent": agent,
        "actor_id": context["actor_id"],
        "source_body_sha256": context["source_body_sha256"],
        "candidate_sha256": candidate_sha256,
        "candidate_version": candidate_version or "",
        "candidate_quality_tier": candidate_quality_tier or "",
        "source_url": str(payload.get("source_url") or ""),
        "base_sha256": base_sha256,
        "base_version": base_version,
        "base_quality_tier": base_quality_tier,
        "base_lifecycle_sha256": base_lifecycle_sha256,
        "base_lifecycle_version": base_lifecycle_version,
        "base_lifecycle_receipt": base_lifecycle_receipt,
        "reason": str(payload.get("reason") or ""),
        "publisher": publisher,
        "slug": slug,
        "canonical_path": canonical_path or f"agents/{publisher}/{slug}.py",
    }
    revision_id = mutation_revision_id(revision_basis)
    request_dir = STAGING_DIR / "requests" / context["request_id"] / revision_id
    request_file = request_dir / "request.json"
    candidate_file = request_dir / "candidate.py"

    request = {
        **revision_basis,
        "revision_id": revision_id,
        "status": "pending_review",
        "issue_number": context["issue_number"],
        "issue_node_id": context["issue_node_id"],
        "repository_id": context["repository_id"],
        "actor_login": context["actor_login"],
        "issue_updated_at": context["issue_updated_at"],
        "created_at": now_iso(),
    }

    if request_file.exists():
        existing = json.loads(request_file.read_text(encoding="utf-8"))
        candidate_matches = (
            candidate_code is None
            or (
                candidate_file.exists()
                and candidate_file.read_text(encoding="utf-8") == candidate_code
            )
        )
        comparable_existing = {
            key: value
            for key, value in existing.items()
            if key not in {"created_at", "issue_updated_at"}
        }
        comparable_request = {
            key: value
            for key, value in request.items()
            if key not in {"created_at", "issue_updated_at"}
        }
        if comparable_existing != comparable_request or not candidate_matches:
            return {"error": "Existing staged revision is not immutable"}
        return {
            "ok": True,
            "action": action,
            "agent": agent,
            "request_id": context["request_id"],
            "revision_id": revision_id,
            "candidate_sha256": candidate_sha256,
            "file": str(request_file.relative_to(REPO_ROOT)),
            "status": "pending_review",
        }

    request_dir.mkdir(parents=True, exist_ok=True)
    if candidate_code is not None:
        candidate_file.write_text(candidate_code, encoding="utf-8")
    request_file.write_text(
        json.dumps(request, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    archive_dir = STATE_DIR / "requests" / context["request_id"]
    for sibling in request_dir.parent.iterdir():
        if sibling == request_dir or not sibling.is_dir():
            continue
        old_request_file = sibling / "request.json"
        if not old_request_file.exists():
            continue
        old_request = json.loads(old_request_file.read_text(encoding="utf-8"))
        old_request["status"] = "superseded"
        old_request["superseded_by"] = revision_id
        old_request["superseded_at"] = now_iso()
        archive_dir.mkdir(parents=True, exist_ok=True)
        save_json(archive_dir / f"{old_request['revision_id']}.json", old_request)
        shutil.rmtree(sibling)

    return {
        "ok": True,
        "action": action,
        "agent": agent,
        "request_id": context["request_id"],
        "revision_id": revision_id,
        "candidate_sha256": candidate_sha256,
        "file": str(request_file.relative_to(REPO_ROOT)),
        "status": "pending_review",
    }


def cancel_issue_requests(issue_number: int, actor_id: int | str) -> dict:
    cancelled = []
    request_root = STAGING_DIR / "requests"
    if request_root.exists():
        for request_file in list(request_root.glob("*/*/request.json")):
            request = json.loads(request_file.read_text(encoding="utf-8"))
            if (
                request.get("issue_number") != issue_number
                or str(request.get("actor_id")) != str(actor_id)
            ):
                continue
            request["status"] = "cancelled"
            request["cancelled_at"] = now_iso()
            archive = (
                STATE_DIR
                / "requests"
                / request["request_id"]
                / f"{request['revision_id']}.json"
            )
            save_json(archive, request)
            shutil.rmtree(request_file.parent)
            cancelled.append(request["revision_id"])
    return {
        "ok": True,
        "action": "agent.cancel" if cancelled else "skipped",
        "status": "cancelled" if cancelled else "skipped",
        "revision_id": cancelled[-1] if cancelled else "",
        "cancelled_revisions": cancelled,
    }


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
    votes.setdefault("operations", {})
    operation_key = _issue_operation_key(payload)
    if operation_key and operation_key in votes["operations"]:
        return votes["operations"][operation_key]

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

    result = {
        "ok": True,
        "action": "vote",
        "agent": agent,
        "direction": direction,
        "score": agent_votes["score"],
    }
    if operation_key:
        votes["operations"][operation_key] = result
        save_json(VOTES_FILE, votes)
    return result


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
    reviews.setdefault("operations", {})
    operation_key = _issue_operation_key(payload)
    if operation_key and operation_key in reviews["operations"]:
        return reviews["operations"][operation_key]

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

    result = {
        "ok": True,
        "action": "review",
        "agent": agent,
        "rating": rating,
    }
    if operation_key:
        reviews["operations"][operation_key] = result
        save_json(REVIEWS_FILE, reviews)
    return result


def handle_submit_agent(payload: dict, user: str) -> dict:
    """Process an agent submission. Validates manifest and writes to staging/.

    Agents land in staging/ for review — NOT in agents/.
    Admin approval (via label or workflow) promotes staging → agents and triggers card forge.
    """
    code = payload.get("code", "")
    source_url = str(payload.get("source_url") or "")
    if not code and source_url:
        code = _fetch_attachment(source_url) or ""
        if not code:
            return {
                "error": (
                    "Could not fetch bounded UTF-8 source from the approved "
                    "GitHub URL"
                )
            }
    if not code or not code.strip():
        return {"error": "Agent code is required"}
    code = code.replace("\r\n", "\n")
    versioned = payload.get("_versioned") is True
    declared_digest = _normalize_digest(payload.get("source_sha256", ""))
    if versioned and not re.fullmatch(r"[0-9a-f]{64}", declared_digest):
        return {"error": "Versioned source requires a valid SHA256 digest"}

    # Reject unmodified template submissions
    if "@your_username/" in code or "YOUR LOGIC GOES HERE" in code or "RAPP AGENT TEMPLATE" in code:
        return {"error": "This is the unmodified template. Fill it in with your LLM first, then resubmit."}

    manifest = extract_manifest_from_code(code)
    if manifest is None:
        return {"error": "No valid __manifest__ dict found in agent code"}

    errors = validate_manifest(manifest)
    errors.extend(validate_candidate_contract(code, manifest))
    if errors:
        return {"error": f"Manifest validation failed: {'; '.join(errors)}"}

    original_name = manifest["name"]
    lifecycle_records = load_json(LIFECYCLE_FILE).get("agents", {})
    existing_owner_record = lifecycle_records.get(original_name, {})
    context_actor_id = (payload.get("_context") or {}).get("actor_id")
    owned_by_numeric_id = bool(
        existing_owner_record.get("owner_github_id") is not None
        and str(existing_owner_record.get("owner_github_id"))
        == str(context_actor_id)
    )
    if (
        existing_owner_record.get("owner_github_id") is not None
        and not owned_by_numeric_id
    ):
        return {"error": "GitHub numeric owner identity does not match agent owner"}
    if owned_by_numeric_id:
        identity_match = re.fullmatch(r"@([^/]+)/([a-z0-9_]+)", original_name)
        if not identity_match:
            return {"error": "Lifecycle-owned agent identity is invalid"}
        publisher = f"@{identity_match.group(1)}"
        raw_slug = identity_match.group(2)
        slug = (
            raw_slug
            if raw_slug.endswith("_agent")
            else f"{raw_slug}_agent"
        )
    else:
        publisher, slug, identity_error = _normalize_agent_identity(
            original_name,
            user,
        )
        if identity_error:
            return {"error": identity_error}
    registered_agent = resolve_registered_agent(original_name)
    candidate_agent_file = (
        registered_agent[0]
        if registered_agent
        else AGENTS_DIR / publisher / f"{slug}.py"
    )
    existing_candidate_manifest = (
        registered_agent[1]
        if registered_agent
        else None
    )
    requested_operation = str(payload.get("_operation") or "submit")
    existing_tombstone = (
        lifecycle_records.get(original_name)
        or lifecycle_records.get(f"{publisher}/{slug}")
        or {}
    )
    canonical_path = (
        str(candidate_agent_file.relative_to(REPO_ROOT))
        if candidate_agent_file.exists()
        else str(
            existing_tombstone.get("canonical_path")
            or f"agents/{publisher}/{slug}.py"
        )
    )
    preserves_existing_identity = bool(
        existing_candidate_manifest
        and existing_candidate_manifest.get("name") == original_name
        and requested_operation in {"submit", "update"}
    )
    preserves_tombstone_identity = bool(
        requested_operation == "restore"
        and existing_tombstone.get("status") in {"deleted", "retired"}
    )

    tier = manifest.get("quality_tier", "unverified")
    if tier not in SUBMITTABLE_TIERS:
        preserves_existing_tier = (
            preserves_existing_identity
            and existing_candidate_manifest.get("quality_tier", "community") == tier
        ) or (
            preserves_tombstone_identity
            and existing_tombstone.get("quality_tier") == tier
        )
        if preserves_existing_tier:
            pass
        elif versioned:
            return {
                "error": (
                    "Versioned submissions require quality_tier community, "
                    "experimental, or unverified"
                )
            }
        else:
            rewritten = replace_manifest_string_field(
                code,
                "quality_tier",
                "community",
            )
            if rewritten is None:
                return {"error": "Could not normalize quality_tier safely"}
            code = rewritten
            manifest = extract_manifest_from_code(code)
            if manifest is None or manifest.get("quality_tier") != "community":
                return {"error": "Could not normalize quality_tier safely"}

    name = (
        original_name
        if preserves_existing_identity or preserves_tombstone_identity
        else manifest["name"]
    )

    # Auto-append _agent suffix if missing
    if manifest["name"] != f"{publisher}/{slug}":
        if preserves_existing_identity or preserves_tombstone_identity:
            name = original_name
        elif versioned:
            return {
                "error": (
                    f"Versioned manifest name must be canonical: "
                    f"{publisher}/{slug}"
                )
            }
        else:
            name = f"{publisher}/{slug}"
            code = replace_manifest_string_field(code, "name", name) or ""
            manifest = extract_manifest_from_code(code)
            if manifest is None or manifest.get("name") != name:
                return {"error": "Could not normalize agent name safely"}
    declared_agent = str(payload.get("agent") or "")
    if declared_agent:
        if preserves_existing_identity or preserves_tombstone_identity:
            declared_matches = declared_agent.casefold() == name.casefold()
        else:
            declared_publisher, declared_slug, declared_error = (
                _normalize_agent_identity(declared_agent, user)
            )
            if declared_error:
                return {"error": declared_error}
            declared_matches = f"{declared_publisher}/{declared_slug}" == name
        if not declared_matches:
            return {
                "error": (
                    f"Request resource '{declared_agent}' does not match "
                    f"candidate manifest '{name}'"
                )
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

    candidate_sha256 = sha256_bytes(code.encode("utf-8"))
    if versioned and declared_digest != candidate_sha256:
        return {
            "error": (
                f"Source digest mismatch: declared sha256:{declared_digest}, "
                f"actual sha256:{candidate_sha256}"
            )
        }
    if versioned and payload.get("idempotency_key"):
        try:
            context = _request_context(payload, user)
        except ValueError as exc:
            return {"error": str(exc)}
        action = f"agent.{payload.get('_operation', '')}"
        duplicate = _idempotent_request_result(
            context=context,
            client_command_sha256=_client_command_sha256(
                action=action,
                agent=name,
                actor_id=context["actor_id"],
                candidate_sha256=candidate_sha256,
                candidate_version=str(manifest.get("version", "")),
                candidate_quality_tier=str(
                    manifest.get("quality_tier", "community")
                ),
                payload=payload,
            ),
        )
        if duplicate is not None:
            return duplicate

    lifecycle = lifecycle_records.get(name, {})
    agent_file = candidate_agent_file
    requested_action = str(payload.get("_operation") or "submit")
    if requested_action == "submit":
        if agent_file.exists():
            requested_action = "update"
        elif lifecycle.get("status") in {"deleted", "retired"}:
            requested_action = "restore"
        else:
            requested_action = "create"

    if requested_action == "create" and (
        agent_file.exists() or lifecycle.get("status") in {"deleted", "retired"}
    ):
        return {"error": f"{name} already exists or is tombstoned"}
    if requested_action == "update" and not agent_file.exists():
        return {"error": f"{name} does not exist; use create"}
    if requested_action == "restore" and lifecycle.get("status") not in {
        "deleted",
        "retired",
    }:
        return {"error": f"{name} is not deleted or retired"}
    if versioned and requested_action == "create" and payload.get(
        "if_none_match"
    ) != "*":
        return {"error": "Versioned create requires if_none_match='*'"}
    if versioned and requested_action == "update" and not re.fullmatch(
        r"[0-9a-f]{64}",
        _normalize_digest(payload.get("if_match", "")),
    ):
        return {"error": "Versioned update requires a valid if_match SHA256"}

    if agent_file.exists():
        existing_manifest = extract_manifest_from_code(agent_file.read_text())
        if existing_manifest:
            new_v = manifest.get("version", "0.0.0")
            old_v = existing_manifest.get("version", "0.0.0")
            new_key = semver_key(new_v)
            old_key = semver_key(old_v)
            if new_key is None or old_key is None or new_key <= old_key:
                return {
                    "error": f"Version {new_v} must be greater than existing {old_v}"
                }

    return _stage_request(
        action=f"agent.{requested_action}",
        agent=name,
        publisher=publisher,
        slug=slug,
        user=user,
        payload=payload,
        candidate_code=code,
        candidate_version=str(manifest.get("version", "")),
        candidate_quality_tier=str(manifest.get("quality_tier", "community")),
        base_file=agent_file if agent_file.exists() else None,
        base_lifecycle=lifecycle,
        canonical_path=canonical_path,
    )


def _handle_code_operation(payload: dict, user: str, operation: str) -> dict:
    adjusted = dict(payload)
    adjusted["_operation"] = operation
    return handle_submit_agent(adjusted, user)


def handle_read_agent(payload: dict, user: str) -> dict:
    name = str(payload.get("agent") or "")
    err = validate_agent_name(name)
    if err:
        return {"error": err}
    match = re.fullmatch(r"@([^/]+)/([a-z0-9_]+)", name)
    if not match:
        return {"error": "Agent name must use a safe @publisher/snake_case slug"}
    resolved = resolve_registered_agent(name)
    lifecycle_records = load_json(LIFECYCLE_FILE).get("agents", {})
    if resolved:
        agent_file, manifest = resolved
        name = str(manifest["name"])
    else:
        manifest = {}
        lifecycle_name = next(
            (
                key
                for key in lifecycle_records
                if key.casefold() == name.casefold()
            ),
            name,
        )
        lifecycle = lifecycle_records.get(lifecycle_name, {})
        status = lifecycle.get("status", "not_found")
        return {
            "ok": True,
            "action": "agent.read",
            "agent": lifecycle_name,
            "status": status,
            "lifecycle": lifecycle,
        }
    content = agent_file.read_bytes()
    lifecycle = lifecycle_records.get(name, {})
    return {
        "ok": True,
        "action": "agent.read",
        "agent": name,
        "status": "active",
        "version": manifest.get("version", ""),
        "sha256": sha256_bytes(content),
        "file": str(agent_file.relative_to(REPO_ROOT)),
        "lifecycle": lifecycle,
    }


def handle_delete_agent(payload: dict, user: str) -> dict:
    requested_name = str(payload.get("agent") or "")
    registered_agent = resolve_registered_agent(requested_name)
    name = (
        str(registered_agent[1]["name"])
        if registered_agent
        else requested_name
    )
    lifecycle_records = load_json(LIFECYCLE_FILE).get("agents", {})
    lifecycle_name = next(
        (
            key
            for key in lifecycle_records
            if key.casefold() == name.casefold()
        ),
        name,
    )
    owner_record = lifecycle_records.get(lifecycle_name, {})
    context_actor_id = (payload.get("_context") or {}).get("actor_id")
    owned_by_numeric_id = bool(
        owner_record.get("owner_github_id") is not None
        and str(owner_record.get("owner_github_id")) == str(context_actor_id)
    )
    if owner_record.get("owner_github_id") is not None and not owned_by_numeric_id:
        return {"error": "GitHub numeric owner identity does not match agent owner"}
    if owned_by_numeric_id:
        match = re.fullmatch(r"@([^/]+)/([a-z0-9_]+)", name)
        if not match:
            return {"error": "Lifecycle-owned agent identity is invalid"}
        publisher = f"@{match.group(1)}"
        raw_slug = match.group(2)
        slug = raw_slug if raw_slug.endswith("_agent") else f"{raw_slug}_agent"
    else:
        publisher, slug, identity_error = _normalize_agent_identity(name, user)
        if identity_error:
            return {"error": identity_error}
        if not registered_agent:
            name = f"{publisher}/{slug}"
    if not str(payload.get("reason") or "").strip():
        return {"error": "Delete reason is required"}
    if payload.get("_versioned") is True and not re.fullmatch(
        r"[0-9a-f]{64}",
        _normalize_digest(payload.get("if_match", "")),
    ):
        return {"error": "Versioned delete requires a valid if_match SHA256"}
    if payload.get("_versioned") is True and payload.get("idempotency_key"):
        try:
            context = _request_context(payload, user)
        except ValueError as exc:
            return {"error": str(exc)}
        duplicate = _idempotent_request_result(
            context=context,
            client_command_sha256=_client_command_sha256(
                action="agent.delete",
                agent=name,
                actor_id=context["actor_id"],
                candidate_sha256="",
                candidate_version="",
                candidate_quality_tier="",
                payload=payload,
            ),
        )
        if duplicate is not None:
            return duplicate
    agent_file = (
        registered_agent[0]
        if registered_agent
        else AGENTS_DIR / publisher / f"{slug}.py"
    )
    if not agent_file.exists():
        return {"error": f"{name} does not exist"}
    return _stage_request(
        action="agent.delete",
        agent=name,
        publisher=publisher,
        slug=slug,
        user=user,
        payload=payload,
        candidate_code=None,
        candidate_version=None,
        candidate_quality_tier=None,
        base_file=agent_file,
        base_lifecycle=owner_record,
        canonical_path=str(agent_file.relative_to(REPO_ROOT)),
    )


# ──────────────────────────────────────────────────────────────────────
# Dispatcher
# ──────────────────────────────────────────────────────────────────────

HANDLERS = {
    "vote": handle_vote,
    "review": handle_review,
    "submit_agent": handle_submit_agent,
    "agent.create": lambda payload, user: _handle_code_operation(
        payload, user, "create"
    ),
    "agent.read": handle_read_agent,
    "agent.update": lambda payload, user: _handle_code_operation(
        payload, user, "update"
    ),
    "agent.delete": handle_delete_agent,
    "agent.restore": lambda payload, user: _handle_code_operation(
        payload, user, "restore"
    ),
}


def process(data: dict, user: str) -> dict:
    """Route an action to its handler."""
    data = normalize_change_request(data)
    action = data.get("action", "")
    raw_payload = data.get("payload", {})
    if not isinstance(raw_payload, dict):
        return {"error": "payload must be a JSON object"}
    if action.startswith("agent.") and raw_payload.get("_versioned") is not True:
        return {
            "error": (
                "Internal agent actions require a validated "
                f"{CHANGE_REQUEST_SCHEMA} envelope"
            )
        }
    normalization_error = raw_payload.get("_normalization_error")
    if normalization_error:
        return {"error": normalization_error}
    if action not in HANDLERS:
        return {"error": f"Unknown action '{action}'. Valid: {', '.join(HANDLERS.keys())}"}

    return HANDLERS[action](raw_payload, user)


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
    actor_id = issue.get("user", {}).get("id", user)
    issue_node_id = issue.get("node_id", "")
    repository = event.get("repository", {})
    repository_id = repository.get("id", "")

    if issue.get("state") != "open":
        result = cancel_issue_requests(issue_number, actor_id)
        result["source_body_sha256"] = sha256_bytes(body.encode("utf-8"))
        print(json.dumps(result, indent=2))
        github_output = os.environ.get("GITHUB_OUTPUT", "")
        if github_output:
            with open(github_output, "a", encoding="utf-8") as output:
                output.write(f"result={json.dumps(result)}\n")
                output.write("success=true\n")
                for key in (
                    "action",
                    "revision_id",
                    "status",
                    "source_body_sha256",
                ):
                    output.write(f"{key}={result.get(key, '')}\n")
        return 0

    # Skip issues with special labels
    labels = [l.get("name", "") for l in issue.get("labels", [])]
    if any(l in labels for l in ("operator-directive", "skip-processing")):
        print(f"Skipping issue #{issue_number} (special label)")
        return 0
    terminal_labels = {"notarized", "deleted", "forged", "processed", "rejected"}
    if terminal_labels.intersection(labels):
        print(f"Skipping terminal issue #{issue_number}")
        github_output = os.environ.get("GITHUB_OUTPUT", "")
        if github_output:
            skipped = {"ok": True, "action": "skipped", "status": "skipped"}
            with open(github_output, "a", encoding="utf-8") as output:
                output.write(f"result={json.dumps(skipped)}\n")
                output.write("success=true\n")
                output.write("action=skipped\n")
                output.write("status=skipped\n")
        return 0

    try:
        data = extract_json_from_body(body)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"::error::Failed to parse issue #{issue_number}: {e}")
        # Output for the workflow to comment on the issue
        print(f"RESULT_ERROR=Could not parse JSON from issue body: {e}")
        return 1

    data = normalize_change_request(data)
    if data.get("action") in {
        "submit_agent",
        "agent.create",
        "agent.update",
        "agent.delete",
        "agent.restore",
        "vote",
        "review",
    }:
        payload = data.setdefault("payload", {})
        payload["_issue_body"] = body
        payload["_context"] = {
            "issue_number": issue_number,
            "issue_node_id": issue_node_id,
            "repository_id": repository_id,
            "actor_id": actor_id,
            "issue_updated_at": issue.get("updated_at", ""),
            "source_body_sha256": sha256_bytes(body.encode("utf-8")),
        }

    result = process(data, user)
    result.setdefault("source_body_sha256", sha256_bytes(body.encode("utf-8")))
    result_json = json.dumps(result, indent=2)
    print(result_json)

    # Write result for the workflow to use
    github_output = os.environ.get("GITHUB_OUTPUT", "")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"result={json.dumps(result)}\n")
            f.write(f"success={'true' if result.get('ok') else 'false'}\n")
            for key in (
                "action",
                "agent",
                "request_id",
                "revision_id",
                "status",
                "source_body_sha256",
            ):
                value = result.get(key, "")
                f.write(f"{key}={value}\n")

    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
