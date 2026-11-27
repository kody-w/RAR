"""An agent that declares its packages (PEP 723 `# /// script` block) must declare them in a form tools can read:
valid TOML with `dependencies` as a list of strings. Agent cards for phone hosts are built from this block."""
import re, tomllib
from pathlib import Path

import pytest

BLOCK = re.compile(r"(?ms)^# /// script\s*$(.*?)^# ///\s*$")
AGENTS = [p for p in Path("agents").rglob("*.py") if "# /// script" in p.read_text(encoding="utf-8", errors="ignore")]


@pytest.mark.parametrize("path", AGENTS, ids=str)
def test_declared_packages_parse(path):
    m = BLOCK.search(path.read_text(encoding="utf-8"))
    assert m, f"{path}: '# /// script' opened but never closed with '# ///'"
    body = "\n".join(l[2:] if l.startswith("# ") else l[1:] for l in m.group(1).splitlines())
    meta = tomllib.loads(body)
    deps = meta.get("dependencies", [])
    assert isinstance(deps, list) and all(isinstance(d, str) and d.strip() for d in deps), \
        f"{path}: dependencies must be a list of package strings"


def test_reader_matches_the_bundler():
    """The bundler and this check read the block the same way."""
    import sys
    sys.path.insert(0, "stacks/agentcard-bundles")
    import bundle_card
    src = '# /// script\n# dependencies = ["pypdf>=5", "tomli-w"]\n# ///\nimport pypdf\n'
    assert bundle_card.declared(src) == {"pypdf": "pypdf>=5", "tomli_w": "tomli-w"}
