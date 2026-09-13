#!/usr/bin/env python3
"""Apply one reviewed, hash-bound RAR skill catalog mutation."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

import build_skills_catalog as skill_catalog
import process_issues as pi


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
STAGING_DIR = REPO_ROOT / "staging" / "skill-requests"
STATE_DIR = REPO_ROOT / "state"
LIFECYCLE_FILE = STATE_DIR / "skill_lifecycle.json"
RECEIPTS_DIR = STATE_DIR / "skill-receipts"
REQUESTS_DIR = STATE_DIR / "skill-requests"
RECEIPT_SCHEMA = "rar-skill-receipt/1.0"


class SkillMutationError(RuntimeError):
    """Raised when an approved skill revision no longer matches review."""


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _save_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _hash_file(path: Path) -> str:
    return pi.sha256_bytes(path.read_bytes()) if path.exists() else ""


def _validate_request_identity(request_file: Path, request: dict) -> Path:
    if request.get("schema") != pi.SKILL_REQUEST_SCHEMA:
        raise SkillMutationError("Unsupported skill request schema")
    revision_id = str(request.get("revision_id") or "")
    request_id = str(request.get("request_id") or "")
    if not revision_id or pi.skill_mutation_revision_id(request) != revision_id:
        raise SkillMutationError("Skill request revision digest is invalid")
    if request_file.name == "request.json":
        path_request_id = request_file.parent.parent.name
        path_revision_id = request_file.parent.name
    else:
        path_request_id = request_file.parent.name
        path_revision_id = request_file.stem
    if path_request_id != request_id or path_revision_id != revision_id:
        raise SkillMutationError(
            "Skill request path is not bound to request and revision IDs"
        )

    skill = str(request.get("skill") or "")
    parsed = skill_catalog.parse_skill_name(skill)
    if not parsed:
        raise SkillMutationError("Invalid canonical skill identity")
    publisher, slug = parsed
    if (
        str(request.get("publisher") or "").casefold() != publisher.casefold()
        or request.get("slug") != slug
        or request.get("resource_kind") != "skill"
    ):
        raise SkillMutationError(
            "Skill request path metadata does not match its identity"
        )
    canonical = Path(str(request.get("canonical_path") or ""))
    expected = Path("skills") / publisher / slug / "manifest.json"
    if canonical.as_posix() != expected.as_posix() or canonical.is_absolute():
        raise SkillMutationError("Canonical skill path does not match identity")
    target = REPO_ROOT / canonical
    try:
        target.resolve().relative_to(SKILLS_DIR.resolve())
    except ValueError as exc:
        raise SkillMutationError("Canonical skill path escapes skills directory") from exc
    return target


def find_staged_request(event: dict) -> Path:
    issue = event.get("issue") or {}
    issue_number = issue.get("number")
    actor_id = (issue.get("user") or {}).get("id")
    body_sha256 = pi.sha256_bytes(str(issue.get("body") or "").encode("utf-8"))
    if not issue_number or actor_id is None:
        raise SkillMutationError(
            "Issue number and numeric author identity are required"
        )

    matches = []
    if STAGING_DIR.exists():
        for request_file in STAGING_DIR.glob("*/*/request.json"):
            request = _load_json(request_file)
            if (
                request.get("issue_number") == issue_number
                and str(request.get("actor_id")) == str(actor_id)
                and request.get("source_body_sha256") == body_sha256
                and request.get("status") == "pending_review"
            ):
                matches.append(request_file)
    if len(matches) == 1:
        return matches[0]

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
    raise SkillMutationError(
        f"Expected exactly one current staged or applied skill revision for "
        f"issue #{issue_number}; found {len(matches) + len(archived_matches)}"
    )


def _validate_staged_source(request_file: Path, manifest: dict) -> None:
    source_dir = request_file.parent / "source"
    for item in manifest["source"]["files"]:
        target = source_dir / item["path"]
        if not target.is_file():
            raise SkillMutationError(
                f"Staged skill source is missing {item['path']}"
            )
        if _hash_file(target) != skill_catalog.normalize_digest(item["sha256"]):
            raise SkillMutationError(
                f"Staged skill source digest changed for {item['path']}"
            )


def _validate_request(request_file: Path) -> tuple[dict, Path, Path, dict]:
    request = _load_json(request_file)
    target = _validate_request_identity(request_file, request)
    if request.get("status") != "pending_review":
        raise SkillMutationError("Skill request is not pending review")
    if request.get("action") not in {"skill.create", "skill.update"}:
        raise SkillMutationError(
            f"Unsupported skill mutation action '{request.get('action')}'"
        )

    candidate = request_file.parent / "candidate.json"
    if not candidate.is_file():
        raise SkillMutationError("Staged skill manifest is missing")
    if _hash_file(candidate) != request.get("manifest_sha256"):
        raise SkillMutationError(
            "Staged skill manifest digest does not match request"
        )
    try:
        manifest = _load_json(candidate)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SkillMutationError("Staged skill manifest is invalid JSON") from exc
    errors = skill_catalog.validate_manifest(
        manifest,
        expected_name=request["skill"],
    )
    if errors:
        raise SkillMutationError(
            f"Staged skill manifest is invalid: {'; '.join(errors)}"
        )
    if manifest["version"] != request.get("candidate_version"):
        raise SkillMutationError("Staged skill version does not match request")
    if manifest["source"]["repository"] != request.get("source_repository"):
        raise SkillMutationError("Staged skill repository does not match request")
    if manifest["source"]["revision"] != request.get("source_revision"):
        raise SkillMutationError("Staged skill revision does not match request")
    if (
        pi._skill_source_files_digest(manifest)
        != request.get("source_files_sha256")
    ):
        raise SkillMutationError("Staged skill file set does not match request")
    _validate_staged_source(request_file, manifest)
    return request, target, candidate, manifest


def _validate_applied_projection(
    request_file: Path,
    request: dict,
    receipt_file: Path,
    target: Path,
) -> dict:
    receipt = _load_json(receipt_file)
    revision_id = request["revision_id"]
    if (
        receipt.get("schema") != RECEIPT_SCHEMA
        or receipt.get("id") != f"rar_skill_{revision_id}"
        or receipt.get("revision_id") != revision_id
        or receipt.get("request_id") != request.get("request_id")
        or receipt.get("action") != request.get("action")
        or receipt.get("skill") != request.get("skill")
        or receipt.get("canonical_path") != request.get("canonical_path")
    ):
        raise SkillMutationError(
            "Existing skill receipt is not bound to archived request"
        )
    if receipt.get("artifact", {}).get("digest") != request.get(
        "manifest_sha256"
    ):
        raise SkillMutationError("Existing skill receipt digest is invalid")
    archived_path = (
        REQUESTS_DIR / request["request_id"] / f"{revision_id}.json"
    )
    if not archived_path.exists():
        raise SkillMutationError("Applied skill request archive is missing")
    archived = _load_json(archived_path)
    if (
        archived.get("status") != "applied"
        or pi.skill_mutation_revision_id(archived) != revision_id
        or archived.get("receipt") != receipt.get("id")
    ):
        raise SkillMutationError("Applied skill request archive is inconsistent")
    lifecycle = pi.load_json(LIFECYCLE_FILE)
    record = lifecycle.get("skills", {}).get(request["skill"], {})
    latest_receipt = str(record.get("latest_receipt") or "")
    if latest_receipt != receipt.get("id"):
        cursor = latest_receipt
        seen = set()
        while cursor.startswith("rar_skill_") and cursor not in seen:
            seen.add(cursor)
            if cursor == receipt.get("id"):
                return receipt
            cursor_path = (
                RECEIPTS_DIR
                / f"{cursor.removeprefix('rar_skill_')}.json"
            )
            if not cursor_path.exists():
                break
            cursor_receipt = _load_json(cursor_path)
            cursor = str((cursor_receipt.get("previous") or {}).get("receipt", ""))
        raise SkillMutationError(
            "Historical skill receipt is not in current receipt ancestry"
        )
    if (
        record.get("status") != "active"
        or record.get("sha256") != request.get("manifest_sha256")
        or record.get("canonical_path") != request.get("canonical_path")
        or not target.exists()
        or _hash_file(target) != request.get("manifest_sha256")
    ):
        raise SkillMutationError(
            "Published skill projection is inconsistent with receipt"
        )
    return receipt


def apply_request(
    request_file: Path,
    *,
    approver_id: int | str,
    approver_login: str,
    workflow_run: str = "",
) -> dict:
    raw_request = _load_json(request_file)
    target = _validate_request_identity(request_file, raw_request)
    revision_id = raw_request["revision_id"]
    receipt_file = RECEIPTS_DIR / f"{revision_id}.json"
    if receipt_file.exists():
        receipt = _validate_applied_projection(
            request_file,
            raw_request,
            receipt_file,
            target,
        )
        return {
            "ok": True,
            "already_applied": True,
            "revision_id": revision_id,
            "receipt": str(receipt_file.relative_to(REPO_ROOT)),
            "artifact": receipt["skill"],
            "skill": receipt["skill"],
            "status": receipt["status"],
        }

    request, target, candidate, manifest = _validate_request(request_file)
    current_sha256 = _hash_file(target)
    if current_sha256 != request.get("base_sha256", ""):
        raise SkillMutationError(
            f"Base digest changed for {request['skill']}: expected "
            f"{request.get('base_sha256') or 'absent'}, current "
            f"{current_sha256 or 'absent'}"
        )

    lifecycle = pi.load_json(LIFECYCLE_FILE)
    lifecycle.setdefault("schema", "rar-skill-lifecycle/1.0")
    lifecycle.setdefault("skills", {})
    previous = lifecycle["skills"].get(request["skill"], {})
    base_receipt = request.get("base_lifecycle_receipt", "")
    if base_receipt and (
        previous.get("latest_receipt") != base_receipt
        or previous.get("sha256") != request.get("base_lifecycle_sha256")
        or previous.get("version") != request.get("base_lifecycle_version")
    ):
        raise SkillMutationError("Skill lifecycle changed after staging")

    if request["action"] == "skill.create":
        if target.exists() or previous.get("status") == "active":
            raise SkillMutationError("Skill create requires an unused identity")
    else:
        if not target.exists():
            raise SkillMutationError("Skill update requires an active manifest")
        old_version = skill_catalog.semver_key(request.get("base_version", ""))
        new_version = skill_catalog.semver_key(request.get("candidate_version", ""))
        if old_version is None or new_version is None or new_version <= old_version:
            raise SkillMutationError("Skill update version must increase semantically")

    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(".json.tmp")
    shutil.copyfile(candidate, temporary)
    temporary.replace(target)

    owner_github_id = previous.get("owner_github_id", request["actor_id"])
    owner_github_login = previous.get(
        "owner_github_login",
        request["actor_login"],
    )
    receipt = {
        "schema": RECEIPT_SCHEMA,
        "id": f"rar_skill_{revision_id}",
        "issuer": "github:kody-w/RAR",
        "request_id": request["request_id"],
        "revision_id": revision_id,
        "action": request["action"],
        "artifact_type": "skill",
        "skill": request["skill"],
        "canonical_path": request["canonical_path"],
        "version": request["candidate_version"],
        "controller": {
            "github_id": owner_github_id,
            "github_login": owner_github_login,
        },
        "artifact": {
            "algorithm": skill_catalog.MANIFEST_HASH_ALGORITHM,
            "digest": request["manifest_sha256"],
        },
        "source": {
            "repository": manifest["source"]["repository"],
            "revision": manifest["source"]["revision"],
            "files": [
                {
                    "path": item["path"],
                    "sha256": skill_catalog.normalize_digest(item["sha256"]),
                }
                for item in manifest["source"]["files"]
            ],
        },
        "previous": {
            "version": request.get("base_version", ""),
            "digest": request.get("base_sha256", ""),
            "receipt": previous.get("latest_receipt", ""),
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
                "skill_metadata_schema",
                "namespace",
                "manifest_sha256",
                "immutable_source_revision",
                "source_file_sha256",
                "base_precondition",
                "deterministic_catalog_build",
                "focused_test_suite",
            ],
            "policy": "rar-skill-notary/1.0",
        },
        "protocol_conformance": manifest["protocol_conformance"],
        "status": "notarized",
        "created_at": pi.now_iso(),
    }
    _save_json(receipt_file, receipt)

    lifecycle["skills"][request["skill"]] = {
        "status": "active",
        "version": request["candidate_version"],
        "owner_github_id": owner_github_id,
        "owner_github_login": owner_github_login,
        "canonical_path": request["canonical_path"],
        "sha256": request["manifest_sha256"],
        "source_repository": request["source_repository"],
        "source_revision": request["source_revision"],
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
    archived_path = (
        REQUESTS_DIR / request["request_id"] / f"{revision_id}.json"
    )
    _save_json(archived_path, archived)
    shutil.rmtree(request_file.parent)

    return {
        "ok": True,
        "already_applied": False,
        "revision_id": revision_id,
        "receipt": str(receipt_file.relative_to(REPO_ROOT)),
        "artifact": request["skill"],
        "skill": request["skill"],
        "status": "notarized",
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
    except (
        SkillMutationError,
        OSError,
        ValueError,
        json.JSONDecodeError,
    ) as exc:
        print(f"::error::{exc}")
        return 1

    print(json.dumps(result, indent=2, sort_keys=True))
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as output:
            for key in ("revision_id", "receipt", "artifact", "skill", "status"):
                output.write(f"{key}={result[key]}\n")
            output.write(
                f"already_applied={'true' if result.get('already_applied') else 'false'}\n"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
