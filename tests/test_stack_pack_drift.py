"""Every stack's pack.json must match the bytes beside it (a lockfile check, like `npm ci`).
Editing a stack file without re-signing its pack silently makes the distro unsummonable."""
import hashlib, json
from pathlib import Path

import pytest

STACKS = sorted(p.parent for p in Path("stacks").glob("*/pack.json"))


@pytest.mark.parametrize("stack", STACKS, ids=lambda p: p.name)
def test_pack_matches_files(stack):
    pk = json.loads((stack / "pack.json").read_text())
    for name, meta in (pk.get("files") or {}).items():
        f = stack / name
        assert f.is_file(), f"{stack.name}: {name} is listed in pack.json but missing"
        assert hashlib.sha256(f.read_bytes()).hexdigest() == meta["sha256"], \
            f"{stack.name}: {name} changed without re-signing pack.json"


def test_declared_copies_match_their_source():
    """A file whose pack entry names a `source` claims to be that catalog file, byte for byte."""
    for stack in STACKS:
        pk = json.loads((stack / "pack.json").read_text())
        for name, meta in (pk.get("files") or {}).items():
            src = Path(meta.get("source") or "")
            if meta.get("source") and src.is_file():
                assert (stack / name).read_bytes() == src.read_bytes(), \
                    f"{stack.name}: {name} drifted from its declared source {src}"
