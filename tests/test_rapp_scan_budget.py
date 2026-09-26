"""
scripts/check_rapp_scan_budget.py restates the RAPP/1 checker's bounded scan.

kody-w/rapp-1's rapp_check.py (estate pin 591e014) stops discovering frames once
a checkout holds more than 10,000 candidate JSON files, and then reports the
whole repository as DRIFT ("verification unavailable"). RAR reached more than
16,000 of them before the Rappterpedia stream deltas were folded into bundles. The script
applies the same rules and fails at 90% of every bound.

These tests pin those rules on synthetic trees and never read RAR's own count.
The Test Suite's rapp-scan-budget job and the Nightly Health Check measure that
count. Agent approval and aggregation run this suite before they commit, and a
tree that nears a bound, while the checker can still finish, must never close
RAR's front door (docs/RAPP1-CONFORMANCE.md).

Set RAPP1_CHECKOUT to a kody-w/rapp-1 checkout to also compare the rules with
the checker's own walk and discovery budget on the same synthetic trees.
"""

import importlib.util
import json
import os
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "check_rapp_scan_budget.py"
WORKFLOWS = REPO_ROOT / ".github" / "workflows"
LIVE_CHECK = "python scripts/check_rapp_scan_budget.py"
EXHAUSTED = "bounded frame discovery JSON budget exhausted"


def _load():
    spec = importlib.util.spec_from_file_location("_rapp_scan_budget", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


budget = _load()


def _write(path: Path, text: str = "{}"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _index(frames, seq=0):
    return json.dumps({"schema": "rapp-frame-index/1", "stream_id": "s", "frames": frames,
                       "head": {"seq": seq, "frame_hash": "0" * 64}})


@pytest.fixture
def tree(tmp_path):
    root = tmp_path / "repo"
    _write(root / "counted.json")
    _write(root / "notes.txt", "not json")
    _write(root / "kit.egg", "not json either")
    _write(root / ".git" / "objects" / "hidden.json")
    _write(root / "a" / "rappid.json")
    _write(root / "a" / "frames" / "0.json")
    _write(root / "a" / "frames" / "1.json")
    _write(root / "a" / "frames" / "draft.json")
    _write(root / "a" / "notframes" / "0.json")
    _write(root / "big" / "large.json", " " * (budget.MAX_CANONICAL_BYTES + 1))
    _write(root / "idx" / "rapp-frame-index.json", _index(["listed.json", "missing.json"]))
    _write(root / "idx" / "listed.json")
    _write(root / "idx" / "unlisted.json")
    _write(root / "bad" / "rapp-frame-index.json", _index(["ignored.json"], seq=True))
    _write(root / "bad" / "ignored.json")
    _write(tmp_path / "outside" / "elsewhere.json")
    (root / "linked-dir").symlink_to(tmp_path / "outside", target_is_directory=True)
    (root / "linked.json").symlink_to(root / "counted.json")
    return root


def test_the_walk_counts_only_what_the_checker_would_read(tree):
    report = budget.measure(tree)
    counted = report["bounds"]["discovery_json_files"]["value"]
    # counted.json, a/frames/draft.json, a/notframes/0.json, idx/unlisted.json, bad/ignored.json
    assert counted == 5, report
    assert report["skipped_over_1_mib"] == 1
    assert report["bounds"]["discovery_json_bytes"]["value"] == 10
    assert report["walk_issues"] == []
    assert report["ok"]


def test_every_bound_fails_at_ninety_percent(tree, monkeypatch):
    monkeypatch.setattr(budget, "MAX_JSON_FILES", 5)
    report = budget.measure(tree)
    files = report["bounds"]["discovery_json_files"]
    assert (files["value"], files["fail_above"], files["ok"]) == (5, 4, False)
    assert not report["ok"]
    assert "FAIL" in budget.summary(report)
    assert budget.main(["--root", str(tree)]) == 1


def test_a_walk_that_cannot_finish_fails_even_below_the_json_bound(tree, monkeypatch):
    monkeypatch.setattr(budget, "MAX_WALK_DIRS", 2)
    report = budget.measure(tree)
    assert report["walk_issues"] == ["repository tree limit reached; tail not scanned"]
    assert not report["ok"]


def _workflow(name):
    yaml = pytest.importorskip("yaml")
    doc = yaml.safe_load((WORKFLOWS / name).read_text(encoding="utf-8"))
    return doc.get("on", doc.get(True)), doc["jobs"]


def _live_checks(job):
    return [step for step in job.get("steps") or [] if LIVE_CHECK in str(step.get("run", ""))]


def test_the_live_count_has_its_own_jobs_and_never_gates_the_front_door():
    triggers, jobs = _workflow("test.yml")
    assert {"push", "pull_request"} <= set(triggers)
    assert [name for name, job in jobs.items() if _live_checks(job)] == ["rapp-scan-budget"]
    assert all("rapp-scan-budget" not in (job.get("needs") or []) for job in jobs.values()), (
        "no job may wait on the budget, so a red budget never skips the rest of the suite")

    # Bot commits never start the Test Suite, so nightly measures it too: last, so
    # it hides no other failure; not gated on the steps above, so none of them
    # hides it; and into the log that the failure issue quotes only when it trips,
    # so an OK summary never pushes another step's failure out of that excerpt.
    triggers, jobs = _workflow("nightly.yml")
    steps, live = jobs["nightly"]["steps"], _live_checks(jobs["nightly"])
    assert "schedule" in triggers and len(live) == 1
    assert steps.index(live[0]) == len(steps) - 2 and steps[-1]["name"] == "Open issue on failure"
    assert live[0]["if"] == "${{ !cancelled() }}" and live[0]["shell"] == "bash"
    run = live[0]["run"]
    assert "tee -a /tmp/test_output.txt" in run
    assert run.index("else") < run.index("tee -a /tmp/test_output.txt") < run.index("exit 1"), (
        "only a tripped budget goes into the log the failure issue quotes")

    elsewhere = [wf.name for wf in sorted(WORKFLOWS.glob("*.yml"))
                 if wf.name not in ("test.yml", "nightly.yml")
                 and "check_rapp_scan_budget" in wf.read_text(encoding="utf-8")]
    assert elsewhere == [], "approval, aggregation, release and heartbeat runs never gate on the live count"


@pytest.mark.skipif(not os.environ.get("RAPP1_CHECKOUT"), reason="set RAPP1_CHECKOUT to a kody-w/rapp-1 checkout")
def test_the_rules_match_the_checkers_own_walk_and_budget(tree, monkeypatch):
    checkout = Path(os.environ["RAPP1_CHECKOUT"]).resolve()
    monkeypatch.setattr(sys, "dont_write_bytecode", True)
    monkeypatch.syspath_prepend(str(checkout))
    import rapp_check

    def exhausted():
        _, findings, _ = rapp_check.check_repo(str(tree))
        return any(f["detail"] == EXHAUSTED for f in findings)

    files, issues = rapp_check._walk_files(str(tree))
    ours, _, _, _, our_issues = budget.walk(tree)
    assert [p for p in files if p.endswith(".json")] == ours
    assert issues == our_issues == []

    # The checker reads exactly the files and bytes the script counts: a budget of
    # exactly that much is enough, and one less is exhausted.
    bounds = budget.measure(tree)["bounds"]
    for name, value in (("_MAX_JSON_FILES", bounds["discovery_json_files"]["value"]),
                        ("_MAX_JSON_BYTES", bounds["discovery_json_bytes"]["value"])):
        original = getattr(rapp_check, name)
        monkeypatch.setattr(rapp_check, name, value)
        assert not exhausted(), f"{name} = {value}"
        monkeypatch.setattr(rapp_check, name, value - 1)
        assert exhausted(), f"{name} = {value - 1}"
        monkeypatch.setattr(rapp_check, name, original)

    monkeypatch.setattr(rapp_check, "_MAX_WALK_DIRS", 2)
    monkeypatch.setattr(budget, "MAX_WALK_DIRS", 2)
    assert rapp_check._walk_files(str(tree))[1] == budget.walk(tree)[4] != []
