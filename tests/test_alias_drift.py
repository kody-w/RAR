"""Linux rule 4: retiring names may not spread. Files that mention an alias are frozen in aliases.json."""
import json, subprocess, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
A = json.loads((ROOT / "aliases.json").read_text())


def test_every_alias_has_status_and_review_date():
    for name, a in A["aliases"].items():
        assert a["status"].startswith("alias of"), name
        datetime.date.fromisoformat(a["since"]); datetime.date.fromisoformat(a["review_on"])


def test_no_new_files_mention_a_retiring_store():
    names = "|".join(A["aliases"])
    out = subprocess.run(["git", "grep", "-lE", names, "--", ".", ":!versions"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    new = sorted(set(out) - set(A["known_mentions"]) - {"aliases.json", "tests/test_alias_drift.py"})
    assert not new, f"new uses of a retiring store name (point to RAR instead): {new}"
