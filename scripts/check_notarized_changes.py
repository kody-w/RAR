#!/usr/bin/env python3
"""Require receipt evidence for every changed active agent artifact."""

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
    base = args.base
    if not base or set(base) == {"0"}:
        base = _git(repo_root, "rev-parse", "HEAD^").strip()

    lifecycle = {"agents": {}}
    if lifecycle_file.exists():
        lifecycle = json.loads(lifecycle_file.read_text(encoding="utf-8"))

    all_changes = _git(repo_root, "diff", "--name-status", base, "HEAD")
    if args.pull_request:
        protected = []
        for line in all_changes.splitlines():
            paths = line.split("\t")[1:]
            for path in paths:
                if (
                    path.startswith("agents/")
                    or path == "registry.json"
                    or path.startswith("staging/requests/")
                    or path == "state/agent_lifecycle.json"
                    or path.startswith("state/receipts/")
                    or path.startswith("state/requests/")
                ):
                    protected.append(path)
        if protected:
            for path in sorted(set(protected)):
                print(
                    f"ERROR {path}: canonical agent/lifecycle state must use "
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
    checked = 0
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
        checked += 1

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print(f"OK {checked} changed agent artifact(s) carry matching RAR receipts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
