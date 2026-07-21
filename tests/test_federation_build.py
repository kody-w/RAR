"""Unit tests for scripts/build_federation.py (consolidated storefront
snapshot: peer-store catalogs projected into state/federation.json)."""

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="module")
def fed():
    spec = importlib.util.spec_from_file_location(
        "build_federation", REPO_ROOT / "scripts" / "build_federation.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["build_federation"] = module
    spec.loader.exec_module(module)
    return module


def test_frontmatter_simple(fed):
    fm = fed.parse_frontmatter("---\nname: my-skill\ndescription: Does a thing\n---\nBody")
    assert fm["name"] == "my-skill"
    assert fm["description"] == "Does a thing"


def test_frontmatter_folded_scalar(fed):
    md = "---\nname: x\ndescription: >\n  Line one\n  line two\n---\n"
    fm = fed.parse_frontmatter(md)
    assert fm["description"] == "Line one line two"


def test_frontmatter_missing(fed):
    assert fed.parse_frontmatter("# Just a heading\n") == {}


def test_clip_truncates(fed):
    long = "word " * 100
    clipped = fed.clip(long)
    assert len(clipped) <= fed.MAX_DESCRIPTION
    assert clipped.endswith("…")


def test_clip_collapses_whitespace(fed):
    assert fed.clip("  a\n  b\t c ") == "a b c"
