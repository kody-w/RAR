#!/usr/bin/env python3
"""Require receipt evidence for changed canonical agent and skill artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


DEFAULT_REPO_ROOT = Path(__file__).resolve().parent.parent


def canonical_sha256(content: bytes) -> str:
    return hashlib.sha256(content.replace(b"\r\n", b"\n")).hexdigest()


def extract_manifest(source: str) -> dict | None:
    import ast

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == "__manifest__"
            for target in node.targets
        ):
            continue
        try:
            return ast.literal_eval(node.value)
        except (TypeError, ValueError):
            return None
    return None


def validate_agent_change(
    *,
    status: str,
    path: str,
    current_content: bytes | None,
    previous_content: bytes | None,
    lifecycle: dict,
    receipts_dir: Path,
) -> list[str]:
    errors = []
    content = previous_content if status == "D" else current_content
    if content is None:
        return [f"{path}: changed agent content is unavailable"]
    manifest = extract_manifest(content.decode("utf-8"))
    if manifest is None:
        return [f"{path}: changed agent manifest is invalid"]
    name = manifest.get("name", "")
    record = lifecycle.get("agents", {}).get(name)
    if not record:
        return [f"{path}: {name} changed without lifecycle evidence"]
    receipt_id = str(record.get("latest_receipt", ""))
    if not receipt_id.startswith("rar_"):
        return [f"{path}: {name} changed without a RAR receipt"]
    receipt_path = receipts_dir / f"{receipt_id.removeprefix('rar_')}.json"
    if not receipt_path.exists():
        return [f"{path}: receipt {receipt_id} is missing"]
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: receipt {receipt_id} is unreadable: {exc}"]
    digest = canonical_sha256(content)

    if status == "D":
        if record.get("status") != "deleted":
            errors.append(f"{path}: deletion lacks a deleted tombstone")
        if receipt.get("action") != "agent.delete":
            errors.append(f"{path}: deletion receipt action is not agent.delete")
    else:
        if record.get("status") != "active":
            errors.append(f"{path}: active artifact lacks active lifecycle")
        if receipt.get("action") not in {
            "agent.create",
            "agent.update",
            "agent.restore",
        }:
            errors.append(f"{path}: active receipt has invalid action")

    if record.get("sha256") != digest:
        errors.append(f"{path}: lifecycle digest does not match changed bytes")
    if receipt.get("artifact", {}).get("digest") != digest:
        errors.append(f"{path}: receipt digest does not match changed bytes")
    if receipt.get("agent") != name:
        errors.append(f"{path}: receipt identity does not match manifest")
    return errors


def validate_skill_change(
    *,
    status: str,
    path: str,
    current_content: bytes | None,
    lifecycle: dict,
    receipts_dir: Path,
) -> list[str]:
    if status == "D" or current_content is None:
        return [f"{path}: published skill manifests cannot be deleted"]
    try:
        manifest = json.loads(current_content.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        return [f"{path}: changed skill manifest is invalid: {exc}"]
    name = manifest.get("name", "")
    if manifest.get("artifact_type") != "skill":
        return [f"{path}: changed skill artifact_type must be skill"]
    record = lifecycle.get("skills", {}).get(name)
    if not record:
        return [f"{path}: {name} changed without skill lifecycle evidence"]
    receipt_id = str(record.get("latest_receipt", ""))
    if not receipt_id.startswith("rar_skill_"):
        return [f"{path}: {name} changed without a RAR skill receipt"]
    receipt_path = receipts_dir / f"{receipt_id.removeprefix('rar_skill_')}.json"
    if not receipt_path.exists():
        return [f"{path}: receipt {receipt_id} is missing"]
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: receipt {receipt_id} is unreadable: {exc}"]

    digest = hashlib.sha256(current_content).hexdigest()
    errors = []
    if record.get("status") != "active":
        errors.append(f"{path}: skill lacks active lifecycle")
    if record.get("canonical_path") != path:
        errors.append(f"{path}: lifecycle canonical path does not match")
    if record.get("sha256") != digest:
        errors.append(f"{path}: skill lifecycle digest does not match bytes")
    if receipt.get("schema") != "rar-skill-receipt/1.0":
        errors.append(f"{path}: skill receipt schema is invalid")
    if receipt.get("action") not in {"skill.create", "skill.update"}:
        errors.append(f"{path}: skill receipt action is invalid")
    if receipt.get("skill") != name:
        errors.append(f"{path}: skill receipt identity does not match manifest")
    if receipt.get("canonical_path") != path:
        errors.append(f"{path}: skill receipt canonical path does not match")
    if receipt.get("artifact", {}).get("digest") != digest:
        errors.append(f"{path}: skill receipt digest does not match bytes")
    return errors


def _git(repo_root: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", *args],
        cwd=repo_root,
        text=True,
        stderr=subprocess.DEVNULL,
    )


def _previous_content(repo_root: Path, base: str, path: str) -> bytes | None:
    result = subprocess.run(
        ["git", "show", f"{base}:{path}"],
        cwd=repo_root,
        capture_output=True,
    )
    return result.stdout if result.returncode == 0 else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--repo-root", default=str(DEFAULT_REPO_ROOT))
    parser.add_argument("--pull-request", action="store_true")
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    lifecycle_file = repo_root / "state" / "agent_lifecycle.json"
    receipts_dir = repo_root / "state" / "receipts"
    skill_lifecycle_file = repo_root / "state" / "skill_lifecycle.json"
    skill_receipts_dir = repo_root / "state" / "skill-receipts"
    base = args.base
    if not base or set(base) == {"0"}:
        base = _git(repo_root, "rev-parse", "HEAD^").strip()

    lifecycle = {"agents": {}}
    if lifecycle_file.exists():
        lifecycle = json.loads(lifecycle_file.read_text(encoding="utf-8"))
    skill_lifecycle = {"skills": {}}
    if skill_lifecycle_file.exists():
        skill_lifecycle = json.loads(
            skill_lifecycle_file.read_text(encoding="utf-8")
        )

    all_changes = _git(repo_root, "diff", "--name-status", base, "HEAD")
    if args.pull_request:
        protected = []
        for line in all_changes.splitlines():
            paths = line.split("\t")[1:]
            for path in paths:
                if (
                    path.startswith("agents/")
                    or (
                        path.startswith("skills/@")
                        and path.endswith("/manifest.json")
                    )
                    or path == "registry.json"
                    or path.startswith("staging/requests/")
                    or path.startswith("staging/skill-requests/")
                    or path == "state/agent_lifecycle.json"
                    or path.startswith("state/receipts/")
                    or path.startswith("state/skill-receipts/")
                    or path.startswith("state/requests/")
                    or path.startswith("state/skill-requests/")
                ):
                    protected.append(path)
        if protected:
            for path in sorted(set(protected)):
                print(
                    f"ERROR {path}: canonical notarized state must use "
                    "the GitHub Issue notarization workflow, not a pull request"
                )
            return 1
        print("OK pull request does not modify canonical notarized state")
        return 0

    output = _git(
        repo_root,
        "diff",
        "--name-status",
        base,
        "HEAD",
        "--",
        "agents/",
    )
    changes = []
    for line in output.splitlines():
        fields = line.split("\t")
        status = fields[0][0]
        if status == "R" and len(fields) == 3:
            changes.extend([("D", fields[1]), ("A", fields[2])])
        elif len(fields) >= 2:
            changes.append((status, fields[-1]))

    errors = []
    checked_agents = 0
    for status, path in changes:
        if not (
            path.endswith(".py")
            or path.endswith(".py.card")
        ) or path.endswith(".py.stub"):
            continue
        current_path = repo_root / path
        current = current_path.read_bytes() if current_path.exists() else None
        previous = _previous_content(repo_root, base, path)
        errors.extend(validate_agent_change(
            status=status,
            path=path,
            current_content=current,
            previous_content=previous,
            lifecycle=lifecycle,
            receipts_dir=receipts_dir,
        ))
        checked_agents += 1

    skill_output = _git(
        repo_root,
        "diff",
        "--name-status",
        base,
        "HEAD",
        "--",
        "skills/",
    )
    skill_changes = []
    for line in skill_output.splitlines():
        fields = line.split("\t")
        status = fields[0][0]
        if status == "R" and len(fields) == 3:
            skill_changes.extend([("D", fields[1]), ("A", fields[2])])
        elif len(fields) >= 2:
            skill_changes.append((status, fields[-1]))
    checked_skills = 0
    for status, path in skill_changes:
        if not (
            path.startswith("skills/@")
            and path.endswith("/manifest.json")
        ):
            continue
        current_path = repo_root / path
        current = current_path.read_bytes() if current_path.exists() else None
        errors.extend(
            validate_skill_change(
                status=status,
                path=path,
                current_content=current,
                lifecycle=skill_lifecycle,
                receipts_dir=skill_receipts_dir,
            )
        )
        checked_skills += 1

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print(
        f"OK {checked_agents} changed agent artifact(s) and "
        f"{checked_skills} changed skill manifest(s) carry matching receipts"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
