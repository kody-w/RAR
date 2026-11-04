"""Linux rule 4: retiring names may not spread. Files that mention an alias are frozen in aliases.json."""
import json, subprocess, datetime
from pathlib import Path

from tools.build_agent_pages import agent_page_contents, build_agent_pages

ROOT = Path(__file__).resolve().parent.parent
A = json.loads((ROOT / "aliases.json").read_text())


def test_every_alias_has_status_and_review_date():
    for name, a in A["aliases"].items():
        assert a["status"].startswith("alias of"), name
        datetime.date.fromisoformat(a["since"]); datetime.date.fromisoformat(a["review_on"])


def new_alias_mentions(root, aliases):
    names = "|".join(aliases["aliases"])
    result = subprocess.run(
        ["git", "grep", "-lzE", names, "--", ".", ":!versions"],
        cwd=root, capture_output=True, text=True,
    )
    if result.returncode not in {0, 1}:
        raise RuntimeError(f"alias scan failed: {result.stderr}")
    new = set(result.stdout.split("\0")) - {""} - set(aliases["known_mentions"]) - {
        "aliases.json", "tests/test_alias_drift.py",
    }
    if any(path.startswith("a/") for path in new):
        registry = json.loads((root / "registry.json").read_text(encoding="utf-8"))
        for agent in registry["agents"]:
            for filename, content in agent_page_contents(agent).items():
                relative = f"a/{agent['name']}/{filename}"
                if relative in new and (root / relative).read_bytes() == content.encode("utf-8"):
                    new.remove(relative)
    return sorted(new)


def test_no_new_files_mention_a_retiring_store():
    new = new_alias_mentions(ROOT, A)
    assert not new, f"new uses of a retiring store name (point to RAR instead): {new}"


def test_only_exact_generated_ticket_pages_are_exempt(tmp_path):
    agent = next(
        entry for entry in json.loads((ROOT / "registry.json").read_text())["agents"]
        if entry["name"] == "@rapp/store_navigator_agent"
    )
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    (tmp_path / "registry.json").write_text(json.dumps({"agents": [agent]}))
    build_agent_pages([agent], tmp_path)
    aliases = {**A, "known_mentions": ["registry.json"]}
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    assert new_alias_mentions(tmp_path, aliases) == []

    hand_added = f"a/{agent['name']}/notes.md"
    (tmp_path / hand_added).write_text(next(iter(A["aliases"])) + "\n")
    subprocess.run(["git", "add", hand_added], cwd=tmp_path, check=True)
    assert new_alias_mentions(tmp_path, aliases) == [hand_added]

    modified = f"a/{agent['name']}/agent.md"
    with (tmp_path / modified).open("a") as stream:
        stream.write("\nHand-written text\n")
    assert new_alias_mentions(tmp_path, aliases) == sorted([hand_added, modified])

    unknown = "a/@unknown/unknown_agent/index.html"
    (tmp_path / unknown).parent.mkdir(parents=True)
    (tmp_path / unknown).write_text((tmp_path / modified).read_text())
    subprocess.run(["git", "add", unknown], cwd=tmp_path, check=True)
    assert new_alias_mentions(tmp_path, aliases) == sorted([hand_added, modified, unknown])
