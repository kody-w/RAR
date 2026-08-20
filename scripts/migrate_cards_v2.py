#!/usr/bin/env python3
"""Project every frozen v1 face into a pinned ``rar-card/2.0`` file."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rapp_sdk import _card_json_bytes, sha256_lf_v1, to_v2  # noqa: E402


RAW_ROOT = "https://raw.githubusercontent.com/kody-w/RAR"
V1_PATH = ROOT / "cards" / "holo_cards.json"
REGISTRY_PATH = ROOT / "registry.json"
OUTPUT_ROOT = ROOT / "cards" / "v2"
INDEX_PATH = OUTPUT_ROOT / "index.json"


def git_revision() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=15,
    )
    revision = result.stdout.strip()
    if result.returncode != 0 or not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise RuntimeError(
            "Could not resolve the repository HEAD: "
            + (result.stderr.strip() or revision or "unknown git error")
        )
    return revision


def load_object(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Could not read {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def registry_by_name(registry: dict) -> dict[str, dict]:
    agents = registry.get("agents")
    if not isinstance(agents, list):
        raise RuntimeError("registry.json must contain an agents array")
    result = {}
    for agent in agents:
        if not isinstance(agent, dict) or not isinstance(agent.get("name"), str):
            raise RuntimeError("registry.json contains an invalid agent entry")
        if agent["name"] in result:
            raise RuntimeError(f"registry.json contains duplicate id {agent['name']}")
        result[agent["name"]] = agent
    return result


def source_digest(agent_id: str, agent: dict) -> tuple[str, bool]:
    digest = agent.get("_sha256")
    used_stub_hash = False
    if not digest and agent.get("type") == "stub":
        digest = agent.get("_stub_sha256")
        used_stub_hash = True
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise RuntimeError(f"{agent_id}: registry has no usable source SHA-256")
    return digest, used_stub_hash


def plan_migration(revision: str) -> tuple[dict[Path, bytes], list[str]]:
    faces = load_object(V1_PATH)
    agents = registry_by_name(load_object(REGISTRY_PATH))
    planned: dict[Path, bytes] = {}
    index = {}
    stub_ids = []

    for agent_id in sorted(faces):
        face = faces[agent_id]
        if not isinstance(face, dict):
            raise RuntimeError(f"{agent_id}: v1 face must be an object")
        agent = agents.get(agent_id)
        if agent is None:
            raise RuntimeError(f"{agent_id}: no matching registry entry")
        relative_source = agent.get("_file")
        if not isinstance(relative_source, str) or not relative_source:
            raise RuntimeError(f"{agent_id}: registry entry has no _file")
        source_path = ROOT / relative_source
        try:
            source_bytes = source_path.read_bytes()
        except OSError as exc:
            raise RuntimeError(
                f"{agent_id}: could not read {relative_source}: {exc}"
            ) from exc
        expected_digest, used_stub_hash = source_digest(agent_id, agent)
        actual_digest = sha256_lf_v1(source_bytes)
        if actual_digest != expected_digest:
            raise RuntimeError(
                f"{agent_id}: registry digest {expected_digest} "
                f"does not match {relative_source} ({actual_digest})"
            )
        if used_stub_hash:
            stub_ids.append(agent_id)

        source_url = f"{RAW_ROOT}/{revision}/{relative_source}"
        scan_url = f"{RAW_ROOT}/main/cards/v2/{agent_id}.card"
        payload = [{
            "kind": "agent.py",
            "filename": source_path.name,
            "sha256_lf_v1": expected_digest,
            "url": source_url,
        }]
        card = to_v2(
            face,
            agent,
            payload=payload,
            state="dormant",
            origin={"kind": "rar"},
            dimension=None,
            scan_url=scan_url,
            rar_revision=revision,
            minted_by="scripts/migrate_cards_v2.py | rapp_sdk 2.0.0",
        )
        raw = _card_json_bytes(card)
        card_path = OUTPUT_ROOT / f"{agent_id}.card"
        planned[card_path] = raw
        index[agent_id] = {
            "seed": card["seed"],
            "name_seed": card["name_seed"],
            "incantation": card["incantation"],
            "sha": hashlib.sha256(raw).hexdigest(),
            "url": scan_url,
        }

    index_raw = (
        json.dumps(index, ensure_ascii=False, indent=2, separators=(",", ": "))
        + "\n"
    ).encode("utf-8")
    planned[INDEX_PATH] = index_raw
    return planned, stub_ids


def apply_migration(planned: dict[Path, bytes], *, check: bool) -> tuple[int, int]:
    expected_cards = {path.resolve() for path in planned if path.suffix == ".card"}
    stale = (
        sorted(
            path
            for path in OUTPUT_ROOT.rglob("*.card")
            if path.resolve() not in expected_cards
        )
        if OUTPUT_ROOT.exists()
        else []
    )
    changed = [
        path
        for path, content in planned.items()
        if not path.is_file() or path.read_bytes() != content
    ]
    if check:
        if changed or stale:
            details = [
                *(f"changed: {path.relative_to(ROOT)}" for path in changed),
                *(f"stale: {path.relative_to(ROOT)}" for path in stale),
            ]
            raise RuntimeError(
                "RAR card v2 migration drift:\n  " + "\n  ".join(details)
            )
        return 0, 0

    for path, content in planned.items():
        if path in changed:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
    for path in stale:
        path.unlink()
    for directory in sorted(
        (path for path in OUTPUT_ROOT.rglob("*") if path.is_dir()),
        reverse=True,
    ):
        try:
            directory.rmdir()
        except OSError:
            pass
    return len(changed), len(stale)


def existing_revision() -> str | None:
    if not OUTPUT_ROOT.exists():
        return None
    for path in sorted(OUTPUT_ROOT.glob("@*/*.card")):
        try:
            card = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            return None
        revision = (card.get("provenance") or {}).get("rar_revision")
        return revision if isinstance(revision, str) else None
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Migrate frozen RAR v1 card faces to rar-card/2.0",
    )
    parser.add_argument(
        "--revision",
        help="Git revision used for pinned payload URLs (default: HEAD)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report generated-card drift without writing",
    )
    args = parser.parse_args()
    if args.revision and not re.fullmatch(r"[0-9a-f]{40}", args.revision):
        parser.error("--revision must be a full 40-character lowercase Git SHA")

    try:
        revision = args.revision
        planned = None
        stub_ids = []
        if revision is None:
            prior_revision = existing_revision()
            if prior_revision and re.fullmatch(r"[0-9a-f]{40}", prior_revision):
                prior_plan, prior_stub_ids = plan_migration(prior_revision)
                try:
                    apply_migration(prior_plan, check=True)
                except RuntimeError:
                    pass
                else:
                    revision = prior_revision
                    planned = prior_plan
                    stub_ids = prior_stub_ids
        if revision is None:
            revision = git_revision()
        if planned is None:
            planned, stub_ids = plan_migration(revision)
        changed, removed = apply_migration(planned, check=args.check)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    card_count = sum(path.suffix == ".card" for path in planned)
    action = "checked" if args.check else "wrote"
    print(
        f"RAR cards v2: {action} {card_count} cards at {revision}; "
        f"{changed} changed, {removed} stale removed"
    )
    if stub_ids:
        print(
            "RAR cards v2: used _stub_sha256 for gated public stubs: "
            + ", ".join(stub_ids)
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
