#!/usr/bin/env python3
"""Apply one hash-bound RAR agent mutation staged from a GitHub Issue."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

import process_issues as pi


REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = REPO_ROOT / "state"
STAGING_DIR = REPO_ROOT / "staging"
AGENTS_DIR = REPO_ROOT / "agents"
LIFECYCLE_FILE = STATE_DIR / "agent_lifecycle.json"
RECEIPTS_DIR = STATE_DIR / "receipts"
REQUESTS_DIR = STATE_DIR / "requests"


class MutationError(RuntimeError):
    pass


def _hash_file(path: Path) -> str:
    return pi.sha256_bytes(path.read_bytes()) if path.exists() else ""


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _validate_request_identity(request_file: Path, request: dict) -> Path:
    if request.get("schema") != pi.CHANGE_REQUEST_SCHEMA:
        raise MutationError("Unsupported request schema")
    revision_id = str(request.get("revision_id", ""))
    request_id = str(request.get("request_id", ""))
    if not revision_id or pi.mutation_revision_id(request) != revision_id:
        raise MutationError("Request revision digest is invalid")
    if request_file.name == "request.json":
        path_request_id = request_file.parent.parent.name
        path_revision_id = request_file.parent.name
    else:
        path_request_id = request_file.parent.name
        path_revision_id = request_file.stem
    if path_request_id != request_id or path_revision_id != revision_id:
        raise MutationError("Request path is not bound to request and revision IDs")

    match = re.fullmatch(r"@([^/]+)/([a-z0-9_]+)", str(request.get("agent", "")))
    if not match:
        raise MutationError("Invalid canonical agent identity")
    publisher = f"@{match.group(1)}"
    identity_slug = match.group(2)
    file_slug = (
        identity_slug
        if identity_slug.endswith("_agent")
        else f"{identity_slug}_agent"
    )
    if (
        str(request.get("publisher", "")).casefold() != publisher.casefold()
        or request.get("slug") != file_slug
    ):
        raise MutationError("Request path metadata does not match agent identity")
    publisher = str(request["publisher"])
    expected_path = f"agents/{publisher}/{file_slug}.py"
    canonical_path = Path(str(request.get("canonical_path", "")))
    if (
        request.get("action") == "agent.create"
        and canonical_path.as_posix() != expected_path
    ):
        raise MutationError("New agent path does not match canonical identity")
    if (
        canonical_path.is_absolute()
        or len(canonical_path.parts) < 3
        or canonical_path.parts[0] != "agents"
        or canonical_path.parts[1].casefold() != publisher.casefold()
        or canonical_path.suffix not in {".py", ".card", ".stub"}
    ):
        raise MutationError("Canonical path does not match publisher namespace")
    agent_file = REPO_ROOT / canonical_path
    try:
        agent_file.resolve().relative_to(AGENTS_DIR.resolve())
    except ValueError as exc:
        raise MutationError("Canonical agent path escapes agents directory") from exc
    return agent_file


def find_staged_request(event: dict) -> Path:
    issue = event.get("issue") or {}
    issue_number = issue.get("number")
    actor_id = (issue.get("user") or {}).get("id")
    body_sha256 = pi.sha256_bytes(str(issue.get("body") or "").encode("utf-8"))
    if not issue_number or actor_id is None:
        raise MutationError("Issue number and numeric author identity are required")

    matches = []
    request_root = STAGING_DIR / "requests"
    if request_root.exists():
        for request_file in request_root.glob("*/*/request.json"):
            request = _load_json(request_file)
            if (
                request.get("issue_number") == issue_number
                and str(request.get("actor_id")) == str(actor_id)
                and request.get("source_body_sha256") == body_sha256
                and request.get("status") == "pending_review"
            ):
                matches.append(request_file)

    if len(matches) != 1:
        archived_matches = []
        if not matches and REQUESTS_DIR.exists():
            for request_file in REQUESTS_DIR.glob("*/*.json"):
                request = _load_json(request_file)
                receipt_file = RECEIPTS_DIR / f"{request.get('revision_id', '')}.json"
                if (
                    request.get("issue_number") == issue_number
                    and str(request.get("actor_id")) == str(actor_id)
                    and request.get("source_body_sha256") == body_sha256
                    and request.get("status") == "applied"
                    and receipt_file.exists()
                ):
                    archived_matches.append(request_file)
        if len(archived_matches) == 1:
            return archived_matches[0]
        raise MutationError(
            f"Expected exactly one current staged or applied revision for issue "
            f"#{issue_number}; found {len(matches) + len(archived_matches)}"
        )
    return matches[0]


def _validate_request(request_file: Path) -> tuple[dict, Path, Path]:
    request = _load_json(request_file)
    agent_file = _validate_request_identity(request_file, request)
    if request.get("status") != "pending_review":
        raise MutationError("Request is not pending review")

    publisher = request.get("publisher", "")
    slug = request.get("slug", "")
    candidate_file = request_file.parent / "candidate.py"
    action = request.get("action")
    if action in {"agent.create", "agent.update", "agent.restore"}:
        if not candidate_file.is_file():
            raise MutationError("Staged candidate is missing")
        if _hash_file(candidate_file) != request.get("candidate_sha256"):
            raise MutationError("Staged candidate digest does not match request")
        manifest = pi.extract_manifest_from_code(
            candidate_file.read_text(encoding="utf-8")
        )
        if manifest is None:
            raise MutationError("Staged candidate manifest is invalid")
        if manifest.get("name") != request.get("agent"):
            raise MutationError("Staged candidate identity does not match request")
        if str(manifest.get("version", "")) != request.get("candidate_version"):
            raise MutationError("Staged candidate version does not match request")
        if str(
            manifest.get("quality_tier", "community")
        ) != request.get("candidate_quality_tier"):
            raise MutationError("Staged candidate quality tier does not match request")
    elif action == "agent.delete":
        if candidate_file.exists() or request.get("candidate_sha256"):
            raise MutationError("Delete request must not contain candidate bytes")
    else:
        raise MutationError(f"Unsupported mutation action '{action}'")

    if action in {"agent.update", "agent.delete"}:
        if not agent_file.exists():
            raise MutationError("Existing target artifact is missing")
        current_manifest = pi.extract_manifest_from_code(
            agent_file.read_text(encoding="utf-8")
        )
        if current_manifest is None or current_manifest.get("name") != request.get(
            "agent"
        ):
            raise MutationError("Existing target identity does not match request")

    return request, agent_file, candidate_file


def _validate_applied_projection(
    request_file: Path,
    request: dict,
    receipt_file: Path,
    agent_file: Path,
) -> dict:
    receipt = _load_json(receipt_file)
    revision_id = request["revision_id"]
    if (
        receipt.get("schema") != pi.RECEIPT_SCHEMA
        or receipt.get("id") != f"rar_{revision_id}"
        or receipt.get("revision_id") != revision_id
        or receipt.get("request_id") != request.get("request_id")
        or receipt.get("action") != request.get("action")
        or receipt.get("agent") != request.get("agent")
        or receipt.get("canonical_path") != request.get("canonical_path")
    ):
        raise MutationError("Existing receipt is not bound to archived request")

    expected_digest = (
        request.get("base_sha256", "")
        if request.get("action") == "agent.delete"
        else request.get("candidate_sha256", "")
    )
    if receipt.get("artifact", {}).get("digest") != expected_digest:
        raise MutationError("Existing receipt artifact digest is invalid")
    expected_quality_tier = (
        request.get("base_quality_tier", "community")
        if request.get("action") == "agent.delete"
        else request.get("candidate_quality_tier", "community")
    )
    if receipt.get("quality_tier") != expected_quality_tier:
        raise MutationError("Existing receipt quality tier is invalid")

    archived_request = (
        REQUESTS_DIR / request["request_id"] / f"{revision_id}.json"
    )
    if not archived_request.exists():
        raise MutationError("Applied request archive is missing")
    archived = _load_json(archived_request)
    if (
        archived.get("status") != "applied"
        or pi.mutation_revision_id(archived) != revision_id
        or archived.get("receipt") != receipt.get("id")
    ):
        raise MutationError("Applied request archive is inconsistent")

    lifecycle = pi.load_json(LIFECYCLE_FILE)
    record = lifecycle.get("agents", {}).get(request["agent"], {})
    latest_receipt = str(record.get("latest_receipt", ""))
    if latest_receipt != receipt.get("id"):
        cursor = latest_receipt
        seen = set()
        while cursor.startswith("rar_") and cursor not in seen:
            seen.add(cursor)
            if cursor == receipt.get("id"):
                return receipt
            cursor_path = RECEIPTS_DIR / f"{cursor.removeprefix('rar_')}.json"
            if not cursor_path.exists():
                break
            cursor_receipt = _load_json(cursor_path)
            cursor = str(cursor_receipt.get("previous", {}).get("receipt", ""))
        raise MutationError("Historical receipt is not in current receipt ancestry")

    expected_status = "deleted" if receipt.get("status") == "deleted" else "active"
    if (
        record.get("status") != expected_status
        or record.get("latest_receipt") != receipt.get("id")
        or record.get("sha256") != expected_digest
        or record.get("quality_tier") != expected_quality_tier
        or record.get("canonical_path") != request.get("canonical_path")
        or str(record.get("owner_github_id"))
        != str(receipt.get("controller", {}).get("github_id"))
    ):
        raise MutationError("Lifecycle projection is inconsistent with receipt")
    if expected_status == "active":
        if not agent_file.exists() or _hash_file(agent_file) != expected_digest:
            raise MutationError("Active artifact is inconsistent with receipt")
    elif agent_file.exists():
        raise MutationError("Deleted artifact still exists")
    return receipt


def apply_request(
    request_file: Path,
    *,
    approver_id: int | str,
    approver_login: str,
    workflow_run: str = "",
) -> dict:
    raw_request = _load_json(request_file)
    agent_file = _validate_request_identity(request_file, raw_request)
    revision_id = raw_request.get("revision_id", "")
    receipt_file = RECEIPTS_DIR / f"{revision_id}.json"
    if receipt_file.exists():
        receipt = _validate_applied_projection(
            request_file,
            raw_request,
            receipt_file,
            agent_file,
        )
        return {
            "ok": True,
            "already_applied": True,
            "revision_id": revision_id,
            "receipt": str(receipt_file.relative_to(REPO_ROOT)),
            "agent": receipt["agent"],
            "status": receipt["status"],
        }

    request, agent_file, candidate_file = _validate_request(request_file)
    revision_id = request["revision_id"]
    receipt_file = RECEIPTS_DIR / f"{revision_id}.json"
    archived_request = (
        REQUESTS_DIR
        / request["request_id"]
        / f"{revision_id}.json"
    )

    current_sha256 = _hash_file(agent_file)
    if current_sha256 != request.get("base_sha256", ""):
        raise MutationError(
            f"Base digest changed for {request['agent']}: expected "
            f"{request.get('base_sha256') or 'absent'}, current "
            f"{current_sha256 or 'absent'}"
        )

    lifecycle = pi.load_json(LIFECYCLE_FILE)
    lifecycle.setdefault("agents", {})
    previous_lifecycle = lifecycle["agents"].get(request["agent"], {})
    action = request["action"]
    base_receipt = request.get("base_lifecycle_receipt", "")
    if base_receipt and (
        previous_lifecycle.get("latest_receipt") != base_receipt
        or previous_lifecycle.get("sha256")
        != request.get("base_lifecycle_sha256")
        or previous_lifecycle.get("version")
        != request.get("base_lifecycle_version")
    ):
        raise MutationError("Lifecycle state changed after staging")

    if action == "agent.create":
        if agent_file.exists() or previous_lifecycle.get("status") in {
            "deleted",
            "retired",
        }:
            raise MutationError("Create requires an unused, untombstoned identity")
    elif action == "agent.update":
        if not agent_file.exists():
            raise MutationError("Update requires an active agent")
        previous_version = pi.semver_key(request.get("base_version", ""))
        candidate_version = pi.semver_key(request.get("candidate_version", ""))
        if (
            previous_version is None
            or candidate_version is None
            or candidate_version <= previous_version
        ):
            raise MutationError("Update version must increase semantically")
    elif action == "agent.restore":
        if agent_file.exists() or previous_lifecycle.get("status") not in {
            "deleted",
            "retired",
        }:
            raise MutationError("Restore requires a deleted or retired tombstone")
        if (
            previous_lifecycle.get("sha256")
            != request.get("base_lifecycle_sha256")
            or previous_lifecycle.get("version")
            != request.get("base_lifecycle_version")
            or previous_lifecycle.get("latest_receipt")
            != request.get("base_lifecycle_receipt")
        ):
            raise MutationError("Restore tombstone changed after staging")
        previous_version_key = pi.semver_key(
            str(previous_lifecycle.get("version", ""))
        )
        candidate_version_key = pi.semver_key(
            str(request.get("candidate_version", ""))
        )
        if (
            previous_version_key is not None
            and (
                candidate_version_key is None
                or candidate_version_key <= previous_version_key
            )
        ):
            raise MutationError("Restore version must exceed the tombstoned version")
    elif action == "agent.delete" and not agent_file.exists():
        raise MutationError("Delete requires an active agent")

    previous_sha256 = current_sha256
    previous_version = request.get("base_version", "")
    if action == "agent.restore":
        previous_sha256 = str(previous_lifecycle.get("sha256", ""))
        previous_version = str(previous_lifecycle.get("version", ""))
    if action == "agent.delete":
        agent_file.unlink()
        status = "deleted"
        artifact_sha256 = previous_sha256
        version = previous_version
        quality_tier = request.get("base_quality_tier", "community")
    else:
        agent_file.parent.mkdir(parents=True, exist_ok=True)
        temporary = agent_file.with_suffix(".py.tmp")
        shutil.copyfile(candidate_file, temporary)
        temporary.replace(agent_file)
        status = "notarized"
        artifact_sha256 = request["candidate_sha256"]
        version = request["candidate_version"]
        quality_tier = request["candidate_quality_tier"]
    owner_github_id = previous_lifecycle.get(
        "owner_github_id",
        request["actor_id"],
    )
    owner_github_login = request["actor_login"]

    receipt = {
        "schema": pi.RECEIPT_SCHEMA,
        "id": f"rar_{revision_id}",
        "issuer": "github:kody-w/RAR",
        "request_id": request["request_id"],
        "revision_id": revision_id,
        "action": action,
        "agent": request["agent"],
        "canonical_path": request["canonical_path"],
        "version": version,
        "quality_tier": quality_tier,
        "controller": {
            "github_id": owner_github_id,
            "github_login": owner_github_login,
        },
        "artifact": {
            "algorithm": "sha256-lf-v1",
            "digest": artifact_sha256,
        },
        "previous": {
            "version": previous_version,
            "digest": previous_sha256,
            "receipt": previous_lifecycle.get("latest_receipt", ""),
        },
        "submission": {
            "github_id": request["actor_id"],
            "github_login": request["actor_login"],
            "issue_number": request["issue_number"],
            "issue_node_id": request["issue_node_id"],
            "source_body_sha256": request["source_body_sha256"],
        },
        "acceptance": {
            "github_id": approver_id,
            "github_login": approver_login,
            "workflow_run": workflow_run,
            "checks": [
                "manifest",
                "namespace",
                "content_sha256",
                "base_precondition",
                "security_scan",
                "registry_build",
                "card_forge",
                "full_test_suite",
            ],
            "policy": "rar-notary/1.0",
        },
        "status": status,
        "created_at": pi.now_iso(),
    }
    _save_json(receipt_file, receipt)

    lifecycle["agents"][request["agent"]] = {
        "status": "active" if status == "notarized" else "deleted",
        "version": version,
        "quality_tier": quality_tier,
        "owner_github_id": owner_github_id,
        "owner_github_login": owner_github_login,
        "canonical_path": request["canonical_path"],
        "sha256": artifact_sha256,
        "latest_receipt": receipt["id"],
        "updated_at": receipt["created_at"],
    }
    lifecycle["updated_at"] = receipt["created_at"]
    pi.save_json(LIFECYCLE_FILE, lifecycle)

    archived = {
        **request,
        "status": "applied",
        "receipt": receipt["id"],
        "approved_by": {
            "github_id": approver_id,
            "github_login": approver_login,
        },
        "applied_at": receipt["created_at"],
    }
    _save_json(archived_request, archived)
    shutil.rmtree(request_file.parent)

    return {
        "ok": True,
        "already_applied": False,
        "revision_id": revision_id,
        "receipt": str(receipt_file.relative_to(REPO_ROOT)),
        "agent": request["agent"],
        "status": status,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event-path", required=True)
    args = parser.parse_args()
    event = _load_json(Path(args.event_path))
    sender = event.get("sender") or {}
    sender_id = sender.get("id")
    sender_login = sender.get("login", "")
    if sender_id is None or not sender_login:
        print("::error::Approval actor identity is required")
        return 1

    try:
        request_file = find_staged_request(event)
        result = apply_request(
            request_file,
            approver_id=sender_id,
            approver_login=sender_login,
            workflow_run=os.environ.get("GITHUB_RUN_ID", ""),
        )
    except (MutationError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"::error::{exc}")
        return 1

    print(json.dumps(result, indent=2, sort_keys=True))
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as output:
            for key in ("revision_id", "receipt", "agent", "status"):
                output.write(f"{key}={result[key]}\n")
            output.write(
                f"already_applied={'true' if result.get('already_applied') else 'false'}\n"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
