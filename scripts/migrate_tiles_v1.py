#!/usr/bin/env python3
"""Build the rappid-tile/1.0 tree without modifying frozen card artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import urllib.parse
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rapp_sdk import (  # noqa: E402
    CARD_SCHEMA,
    TILE_SCHEMA,
    _tile_json_bytes,
    card_to_tile,
    sha256_lf_v1,
    to_tile,
)


RAW_ROOT = "https://raw.githubusercontent.com/kody-w/RAR"
CARD_ROOT = ROOT / "cards" / "v2"
CARD_INDEX_PATH = CARD_ROOT / "index.json"
FACE_PATH = ROOT / "cards" / "holo_cards.json"
REGISTRY_PATH = ROOT / "registry.json"
OUTPUT_ROOT = ROOT / "tiles" / "v1"
INDEX_PATH = OUTPUT_ROOT / "index.json"
INDEX_SCHEMA = "rappid-tile-index/1.0"


def load_object(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Could not read {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


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


def registry_by_name(registry: dict) -> dict[str, dict]:
    agents = registry.get("agents")
    if not isinstance(agents, list):
        raise RuntimeError("registry.json must contain an agents array")
    result = {}
    for agent in agents:
        if not isinstance(agent, dict) or not isinstance(agent.get("name"), str):
            raise RuntimeError("registry.json contains an invalid agent entry")
        if agent["name"] in result:
            raise RuntimeError(
                f"registry.json contains duplicate id {agent['name']}"
            )
        result[agent["name"]] = agent
    return result


def source_digest(agent_id: str, agent: dict) -> str:
    digest = agent.get("_sha256")
    if not digest and agent.get("type") == "stub":
        digest = agent.get("_stub_sha256")
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise RuntimeError(f"{agent_id}: registry has no usable source SHA-256")
    return digest


def card_path(agent_id: str, entry: dict) -> Path:
    url = entry.get("url")
    if not isinstance(url, str):
        raise RuntimeError(f"{agent_id}: frozen card index entry has no URL")
    parsed = urllib.parse.urlparse(url)
    marker = "/cards/v2/"
    if marker not in parsed.path:
        raise RuntimeError(f"{agent_id}: frozen card URL is outside cards/v2")
    relative = Path(urllib.parse.unquote(parsed.path.split(marker, 1)[1]))
    if relative.is_absolute() or ".." in relative.parts:
        raise RuntimeError(f"{agent_id}: frozen card URL contains an unsafe path")
    path = CARD_ROOT / relative
    if not path.is_file():
        raise RuntimeError(
            f"{agent_id}: frozen card is missing at {path.relative_to(ROOT)}"
        )
    return path


def collision_safe_filename(
    agent_id: str,
    agent: dict,
    counts: Counter,
) -> str:
    relative_source = agent.get("_file")
    if not isinstance(relative_source, str) or not relative_source:
        raise RuntimeError(f"{agent_id}: registry entry has no _file")
    source_name = Path(relative_source).name
    publisher = agent_id.split("/", 1)[0]
    if counts[(publisher, source_name)] <= 1:
        return source_name
    install_name = agent.get("_install_filename")
    if (
        not isinstance(install_name, str)
        or not install_name
        or Path(install_name).name != install_name
    ):
        raise RuntimeError(
            f"{agent_id}: colliding source filename {source_name!r} has no "
            "collision-safe install filename"
        )
    return install_name


def direct_tile(
    *,
    agent_id: str,
    face: dict,
    agent: dict,
    payload_filename: str,
    head_revision: str,
    scan_url: str,
) -> dict:
    relative_source = agent["_file"]
    source_path = ROOT / relative_source
    try:
        source_bytes = source_path.read_bytes()
    except OSError as exc:
        raise RuntimeError(
            f"{agent_id}: could not read {relative_source}: {exc}"
        ) from exc
    digest = source_digest(agent_id, agent)
    actual = sha256_lf_v1(source_bytes)
    if actual != digest:
        raise RuntimeError(
            f"{agent_id}: registry digest {digest} does not match "
            f"{relative_source} ({actual})"
        )
    revision = agent.get("_latest_commit_sha")
    if not isinstance(revision, str) or not re.fullmatch(
        r"[0-9a-f]{40}", revision
    ):
        revision = head_revision
    payload = [{
        "role": "primary",
        "kind": "agent.py",
        "filename": payload_filename,
        "sha256_lf_v1": digest,
        "url": f"{RAW_ROOT}/{revision}/{relative_source}",
    }]
    return to_tile(
        face,
        agent,
        payload=payload,
        state="dormant",
        origin={"kind": "rar"},
        dimension=None,
        scan_url=scan_url,
        registry_revision=revision,
        minted_by="scripts/migrate_tiles_v1.py | rapp_sdk 2.1.0",
    )


def plan_migration() -> dict[Path, bytes]:
    cards = load_object(CARD_INDEX_PATH)
    faces = load_object(FACE_PATH)
    agents = registry_by_name(load_object(REGISTRY_PATH))
    missing_agents = sorted(set(faces) - set(agents))
    if missing_agents:
        raise RuntimeError(
            "Frozen faces have no registry entries: " + ", ".join(missing_agents)
        )
    counts = Counter(
        (
            agent_id.split("/", 1)[0],
            Path(agent["_file"]).name,
        )
        for agent_id, agent in agents.items()
        if agent_id in faces and isinstance(agent.get("_file"), str)
    )
    head_revision = git_revision()
    planned: dict[Path, bytes] = {}
    tile_index = {}

    for agent_id in sorted(faces):
        face = faces[agent_id]
        if not isinstance(face, dict):
            raise RuntimeError(f"{agent_id}: frozen face must be an object")
        publisher = agent_id.split("/", 1)[0]
        if agent_id in cards:
            source = card_path(agent_id, cards[agent_id])
            filename = source.name.removesuffix(".card") + ".tile"
        else:
            filename = (
                collision_safe_filename(
                    agent_id,
                    agents[agent_id],
                    counts,
                )
                + ".tile"
            )
        scan_url = f"{RAW_ROOT}/main/tiles/v1/{publisher}/{filename}"
        if agent_id in cards:
            card = load_object(source)
            tile = card_to_tile(
                card,
                scan_url=scan_url,
                fetch_payloads=False,
            )
            if (
                tile["seed"] != card["seed"]
                or tile["face"] != card["face"]
                or tile["key"] != card["incantation"]
            ):
                raise RuntimeError(
                    f"{agent_id}: card migration changed seed, face, or key"
                )
        else:
            tile = direct_tile(
                agent_id=agent_id,
                face=face,
                agent=agents[agent_id],
                payload_filename=filename.removesuffix(".tile"),
                head_revision=head_revision,
                scan_url=scan_url,
            )

        raw = _tile_json_bytes(tile)
        output = OUTPUT_ROOT / publisher / filename
        if output in planned:
            raise RuntimeError(
                f"{agent_id}: duplicate tile path {output.relative_to(ROOT)}"
            )
        planned[output] = raw
        tile_index[agent_id] = {
            "seed": tile["seed"],
            "name_seed": tile["name_seed"],
            "key": tile["key"],
            "sha": hashlib.sha256(raw).hexdigest(),
            "url": scan_url,
        }

    index = {
        "schema": INDEX_SCHEMA,
        "cards": {
            "schema": CARD_SCHEMA,
            "index": f"{RAW_ROOT}/main/cards/v2/index.json",
            "frozen": True,
        },
        "tiles": tile_index,
    }
    planned[INDEX_PATH] = (
        json.dumps(index, ensure_ascii=False, indent=2, separators=(",", ": "))
        + "\n"
    ).encode("utf-8")
    return planned


def apply_migration(
    planned: dict[Path, bytes],
    *,
    check: bool,
) -> tuple[int, int]:
    expected_tiles = {
        path.resolve() for path in planned if path.suffix == ".tile"
    }
    stale = (
        sorted(
            path
            for path in OUTPUT_ROOT.rglob("*.tile")
            if path.resolve() not in expected_tiles
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
                "Rappid tile migration drift:\n  " + "\n  ".join(details)
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report generated tile drift without writing",
    )
    args = parser.parse_args()
    try:
        planned = plan_migration()
        changed, removed = apply_migration(planned, check=args.check)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    tile_count = sum(path.suffix == ".tile" for path in planned)
    action = "checked" if args.check else "wrote"
    print(
        f"Rappid tiles: {action} {tile_count} tiles; "
        f"{changed} changed, {removed} stale removed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
