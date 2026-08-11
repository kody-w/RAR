#!/usr/bin/env python3
"""Apply multiple approved, hash-bound RAR agent mutations atomically."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import apply_agent_mutation as mutation


class BatchMutationError(RuntimeError):
    pass


def _labels(issue: dict) -> set[str]:
    return {
        label.get("name", "") if isinstance(label, dict) else str(label)
        for label in issue.get("labels", [])
    }


def _preflight(events: list[dict]) -> list[tuple[int, Path, str]]:
    if not events:
        raise BatchMutationError("At least one approved issue is required")

    prepared: list[tuple[int, Path, str]] = []
    issue_numbers: set[int] = set()
    agents: set[str] = set()
    for event in events:
        issue = event.get("issue") or {}
        issue_number = issue.get("number")
        if not isinstance(issue_number, int) or issue_number <= 0:
            raise BatchMutationError("Every event requires a positive issue number")
        if issue_number in issue_numbers:
            raise BatchMutationError(f"Duplicate issue #{issue_number}")
        issue_numbers.add(issue_number)
        if issue.get("state") != "open":
            raise BatchMutationError(f"Issue #{issue_number} is not open")
        if not {"approved", "agent-submission"} <= _labels(issue):
            raise BatchMutationError(
                f"Issue #{issue_number} is not an approved agent submission"
            )

        request_file = mutation.find_staged_request(event)
        request = mutation._load_json(request_file)
        repository_id = (event.get("repository") or {}).get("id")
        if str(request.get("repository_id")) != str(repository_id):
            raise BatchMutationError(
                f"Issue #{issue_number} belongs to a different repository"
            )
        agent = str(request.get("agent", ""))
        if not agent:
            raise BatchMutationError(f"Issue #{issue_number} has no agent identity")
        if agent in agents:
            raise BatchMutationError(
                f"Batch contains multiple mutations for {agent}"
            )
        agents.add(agent)
        prepared.append((issue_number, request_file, agent))

    return sorted(prepared, key=lambda item: item[0])


def apply_batch(
    events: list[dict],
    *,
    approver_id: int | str,
    approver_login: str,
    workflow_run: str = "",
) -> dict:
    if not str(approver_id) or not approver_login:
        raise BatchMutationError("Approver identity is required")

    prepared = _preflight(events)
    results = []
    for issue_number, request_file, expected_agent in prepared:
        result = mutation.apply_request(
            request_file,
            approver_id=approver_id,
            approver_login=approver_login,
            workflow_run=workflow_run,
        )
        if result.get("agent") != expected_agent:
            raise BatchMutationError(
                f"Issue #{issue_number} applied an unexpected agent"
            )
        results.append({"issue_number": issue_number, **result})

    return {
        "ok": True,
        "schema": "rar-batch-receipt/1.0",
        "count": len(results),
        "issues": [result["issue_number"] for result in results],
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--events-path", type=Path, required=True)
    parser.add_argument("--result-path", type=Path, required=True)
    parser.add_argument("--approver-id", required=True)
    parser.add_argument("--approver-login", required=True)
    args = parser.parse_args()

    try:
        events = json.loads(args.events_path.read_text(encoding="utf-8"))
        if not isinstance(events, list):
            raise BatchMutationError("Events payload must be a JSON array")
        result = apply_batch(
            events,
            approver_id=args.approver_id,
            approver_login=args.approver_login,
            workflow_run=os.environ.get("GITHUB_RUN_ID", ""),
        )
        args.result_path.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except (
        BatchMutationError,
        mutation.MutationError,
        OSError,
        ValueError,
        json.JSONDecodeError,
    ) as exc:
        print(f"::error::{exc}")
        return 1

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
