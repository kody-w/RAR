"""Shared deterministic builder timestamps and append-only static frames."""

import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


@lru_cache(maxsize=1)
def commit_timestamp() -> str:
    if "SOURCE_DATE_EPOCH" in os.environ:
        epoch = int(os.environ["SOURCE_DATE_EPOCH"])
    else:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%ct"], cwd=ROOT,
            capture_output=True, text=True, check=True,
        )
        epoch = int(result.stdout.strip())
    return datetime.fromtimestamp(
        epoch, timezone.utc
    ).strftime("%Y-%m-%dT%H:%M:%SZ")


def json_bytes(payload: dict) -> bytes:
    return (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def stable_document(path: Path, payload: dict) -> dict:
    """Keep the original input-derived timestamp when content is unchanged."""
    if not path.exists():
        return payload
    previous = json.loads(path.read_text(encoding="utf-8"))
    timestamps = {"generated", "generated_at"}
    if (
        {k: v for k, v in previous.items() if k not in timestamps}
        == {k: v for k, v in payload.items() if k not in timestamps}
    ):
        payload = dict(payload)
        for key in timestamps & previous.keys() & payload.keys():
            timestamp = datetime.fromisoformat(previous[key].replace("Z", "+00:00"))
            payload[key] = timestamp.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return payload


def write_json(path: Path, payload: dict) -> int:
    rendered = json_bytes(stable_document(path, payload))
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_bytes() != rendered:
        path.write_bytes(rendered)
    return len(rendered)


def publish_frame(name: str, extension: str, content: bytes, root: Path = ROOT) -> dict:
    """Create a frame exclusively; even a truncated-hash collision cannot overwrite it."""
    relative = Path(name)
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        raise ValueError(f"invalid frame name: {name!r}")
    if "/" in extension or "\\" in extension or (extension and not extension.startswith(".")):
        raise ValueError(f"invalid frame extension: {extension!r}")
    digest = hashlib.sha256(content).hexdigest()
    path = root / "versions" / relative / f"{digest[:12]}{extension}"
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("xb") as stream:
            stream.write(content)
    except FileExistsError:
        if path.read_bytes() != content:
            raise ValueError(f"immutable frame collision or corruption: {path}")
    return {
        "sha256": digest,
        "sha8": digest[:12],
        "path": path.relative_to(root).as_posix(),
    }
