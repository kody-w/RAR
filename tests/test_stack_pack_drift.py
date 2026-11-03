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


def _identity(path):
    import ast
    try:
        tree = ast.parse(path.read_text())
    except (SyntaxError, UnicodeDecodeError):
        return None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "__manifest__" for t in node.targets):
            try:
                m = ast.literal_eval(node.value)
                return (m.get("name"), m.get("version"))
            except ValueError:
                return None
    return None


def test_one_name_and_version_means_one_set_of_bytes():
    """Like npm/PyPI: a published version is immutable. A stack may carry a different
    version of a catalog agent, but never different bytes under the same version."""
    catalog = {}
    for f in Path("agents").rglob("*_agent.py"):
        ident = _identity(f)
        if ident and ident[0]:
            catalog[ident] = f
    for stack in STACKS:
        for f in stack.glob("*_agent.py"):
            ident = _identity(f)
            if ident in catalog:
                assert f.read_bytes() == catalog[ident].read_bytes(), \
                    f"{stack.name}: {f.name} reuses {ident[0]} {ident[1]} with different contents; bump its version"
