"""The freshness path, tested without waiting six hours for a cron.

`.github/workflows/aggregate.yml` is the only thing keeping `state/aggregated.json`
and `api/v1/front.json` current, and every way it can fail is quiet: a green run
that committed nothing, a green run that committed an empty catalog, a green run
that rebuilt the ranking and then threw it away. Two of those have already
happened in this repository on other workflows, so they are pinned here rather
than rediscovered.

The workflow scans are deliberately repo-wide. Both defects are shapes, not
one-off typos, and the next person to add a workflow gets the same guard.
"""
from __future__ import annotations

import importlib.util
import json
import sys
import urllib.error
from pathlib import Path

import pytest

yaml = pytest.importorskip("yaml")

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = REPO_ROOT / ".github" / "workflows"
AGGREGATE = WORKFLOWS / "aggregate.yml"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _doc(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _triggers(doc: dict) -> set[str]:
    """`on:` is the YAML 1.1 boolean True, not the string 'on'."""
    raw = doc[True] if True in doc else doc.get("on")
    if isinstance(raw, dict):
        return set(raw)
    if isinstance(raw, list):
        return set(raw)
    return {raw} if raw else set()


def _steps(path: Path, job: str) -> list[dict]:
    return _doc(path)["jobs"][job]["steps"]


def _bodies(steps: list[dict]) -> list[str]:
    return [str(s.get("run") or "") for s in steps]


# ─── (a) A dispatch run must not rebuild an artifact and then discard it ──

# Anything that regenerates a tracked file. Named explicitly rather than
# pattern-matched: "runs a python script" also describes every validation step,
# and a check that fires on those is noise nobody acts on.
BUILDERS = (
    "build_registry.py",
    "build_static_api.py",
    "build_pokedex_api.py",
    "build_front_page.py",
    "build_federation.py",
    "crawl_sources.py",
    "generate_aggregated_agents.py",
    "mint_maintainer_receipts.py",
    "dream_catcher.py",
    "discussion_ratings.py",
    "fetch_download_counts.py",
    "check_url_stability.py --update",
)


def _runs_on_dispatch(condition) -> bool:
    """Would this `if:` let the step run on a workflow_dispatch?

    Deliberately crude: a condition that never mentions `github.event_name`
    cannot discriminate on the event, and one that does runs on dispatch
    exactly when it names it. That covers both real spellings in this repo —
    `github.event_name == 'push'` and the corrected
    `(github.event_name == 'push' || github.event_name == 'workflow_dispatch')`
    — without pretending to be an expression evaluator.
    """
    if condition is None:
        return True
    text = str(condition)
    if "github.event_name" not in text:
        return True
    return "workflow_dispatch" in text


def test_a_dispatch_run_never_rebuilds_an_artifact_and_then_discards_it():
    """build-registry.yml rebuilt the headless static API on every run but
    committed it behind `if: github.event_name == 'push'`. So the one button a
    maintainer reaches for when the published catalog looks stale rebuilt the
    file and threw it away, and `api/v1/catalog.json` sat two versions behind
    main while every job reported green — see tests/test_api_freshness.py.

    The invariant: within a job that commits at all, any step that REGENERATES
    a tracked artifact on a dispatch run must be matched by a commit step that
    also runs on a dispatch run. A producer that is itself push-only is fine —
    the rule is one-directional. Jobs that rebuild only to validate, like
    nightly.yml, never commit and are not in scope.
    """
    offenders = []
    for wf in sorted(WORKFLOWS.glob("*.yml")):
        doc = _doc(wf)
        if "workflow_dispatch" not in _triggers(doc):
            continue
        for jname, job in (doc.get("jobs") or {}).items():
            steps = job.get("steps") or []
            committers = [s for s in steps
                          if "git commit" in str(s.get("run") or "")
                          or "git push" in str(s.get("run") or "")]
            if not committers:
                continue
            job_dispatches = _runs_on_dispatch(job.get("if"))
            commit_dispatches = job_dispatches and any(
                _runs_on_dispatch(s.get("if")) for s in committers)
            for step in steps:
                body = str(step.get("run") or "")
                if not any(b in body for b in BUILDERS):
                    continue
                if not (job_dispatches and _runs_on_dispatch(step.get("if"))):
                    continue
                if not commit_dispatches:
                    offenders.append(
                        f"{wf.name}::{jname}::{step.get('name')} rebuilds on "
                        "workflow_dispatch but no commit step does")
    assert not offenders, (
        "a manual run cannot repair staleness — it rebuilds and discards: "
        + "; ".join(offenders))


def test_the_aggregate_rebuild_and_commit_agree_on_every_event():
    """The same rule, stated directly against this workflow so a future edit
    that reintroduces an event gate fails by name rather than by scan."""
    steps = _steps(AGGREGATE, "aggregate")
    named = {s.get("name"): s for s in steps}
    rebuild = named["Rebuild the front page ranking"]
    commit = named["Commit the refreshed catalog and ranking"]
    assert rebuild.get("if") is None, (
        f"the rebuild is gated on {rebuild['if']!r} — a dispatch that skips it "
        "cannot repair a stale ranking")
    assert "github.event_name" not in str(commit.get("if") or ""), (
        f"the commit is gated on the event ({commit.get('if')!r}); a manual run "
        "would rebuild the ranking and then throw it away")


# ─── (b) No workflow input reaches a shell unquoted ───────────────────────

def _input_env(step: dict, job: dict) -> dict[str, str]:
    """Env vars in scope for this step whose value comes from a dispatch input."""
    bound = {}
    for scope in ((job.get("env") or {}), (step.get("env") or {})):
        for name, value in scope.items():
            if "inputs." in str(value):
                bound[name] = str(value)
    return bound


def _unquoted_uses(body: str, var: str) -> list[str]:
    """Lines where `$VAR` / `${VAR}` sits outside a double-quoted string.

    Quoting state is approximated by counting unescaped double quotes to the
    left on the same line: an odd count means the reference is inside one. That
    is exact for the single-line shell these workflows are made of, and the
    alternative — a real shell parser — is more machinery than the rule needs.
    """
    bad = []
    for line in body.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#"):
            continue
        for form in (f"${{{var}}}", f"${var}"):
            start = 0
            while (idx := line.find(form, start)) != -1:
                start = idx + 1
                # `$VARIABLE` must not match a reference to `$VAR`.
                tail = line[idx + len(form):idx + len(form) + 1]
                if form == f"${var}" and (tail.isalnum() or tail == "_"):
                    continue
                before = line[:idx].replace('\\"', "")
                if before.count('"') % 2 == 0:
                    bad.append(line.strip())
    return bad


def test_no_workflow_input_reaches_a_shell_unquoted():
    """d092016 fixed half of this: `ticks` was interpolated straight into the
    fleet's shell, so a crafted value was spliced into the command line before
    the shell saw a quote. tests/test_release_path.py pins that half — no
    `${{ inputs.* }}` inside a `run:` body.

    The other half is what happens after the value has been moved into `env:`.
    An env var is only safe at the point of USE: `--only $SOURCE` still splits
    on whitespace and still globs, so an input that merely travels through the
    environment is not yet contained. Both halves are checked here so the rule
    reads as one rule.
    """
    spliced, unquoted = [], []
    for wf in sorted(WORKFLOWS.glob("*.yml")):
        doc = _doc(wf)
        for jname, job in (doc.get("jobs") or {}).items():
            for step in (job.get("steps") or []):
                where = f"{wf.name}::{jname}::{step.get('name')}"
                bodies = [step.get("run"), (step.get("with") or {}).get("script")]
                for body in bodies:
                    if not isinstance(body, str):
                        continue
                    if "inputs." in body and "${{" in body:
                        spliced.append(where)
                    for var in _input_env(step, job):
                        for line in _unquoted_uses(body, var):
                            unquoted.append(f"{where}: {line}")
    assert not spliced, f"dispatch input interpolated into a run body: {spliced}"
    assert not unquoted, (
        "dispatch input used unquoted after arriving through env: " + "; ".join(unquoted))


def test_the_aggregate_input_never_touches_a_shell_at_all():
    """`dry_run` is only ever read by an `if:` expression, which Actions
    evaluates itself and never hands to bash. The strongest available form of
    the rule above: there is no shell for it to be unsafe in."""
    doc = _doc(AGGREGATE)
    declared = set((_doc(AGGREGATE)[True] if True in doc else doc["on"])
                   ["workflow_dispatch"]["inputs"])
    assert declared == {"dry_run"}
    for body in _bodies(_steps(AGGREGATE, "aggregate")):
        assert "inputs." not in body, (
            "an input reached a run body; bind it through env: and quote it")


# ─── The commit gate is content, not the clock ───────────────────────────

def test_comparable_ignores_the_build_stamp_and_nothing_else():
    """`generated` moves on every run, so a gate that diffs the file commits an
    identical ranking four times a day forever — the exact churn shape this
    repository already has in its history. `comparable()` is the one definition
    of "actually changed", and the workflow reuses it rather than restating it."""
    bfp = _load("build_front_page_gate", REPO_ROOT / "scripts" / "build_front_page.py")
    a = {"schema": "rar-front-page/1.0", "generated": "2026-08-02T03:40:00Z",
         "counts": {"ranked": 355}}
    b = {"schema": "rar-front-page/1.0", "generated": "2026-08-02T09:40:00Z",
         "counts": {"ranked": 355}}
    assert bfp.comparable(a) == bfp.comparable(b)
    b["counts"]["ranked"] = 356
    assert bfp.comparable(a) != bfp.comparable(b)


def test_the_ranking_is_restored_before_anything_is_staged():
    """Order matters: the discard has to happen while the file is still only a
    working-tree change. Staged first, the restore is a no-op and the churn
    commit goes out anyway."""
    steps = _steps(AGGREGATE, "aggregate")
    bodies = _bodies(steps)
    discard = next(i for i, b in enumerate(bodies)
                   if "comparable" in b and "checkout" in b)
    stage = next(i for i, b in enumerate(bodies) if "git add" in b)
    assert discard < stage


def test_nothing_is_staged_by_wildcard():
    """A scheduled job that stages by wildcard eventually commits something
    nobody chose — the runner's tree holds whatever every step above touched."""
    for body in _bodies(_steps(AGGREGATE, "aggregate")):
        for line in body.splitlines():
            if line.strip().startswith("git add"):
                assert " -A" not in line and not line.strip().endswith("."), (
                    f"stage explicit pathspecs -> {line.strip()}")


# ─── Fail loudly ─────────────────────────────────────────────────────────

def test_the_scheduled_crawl_runs_strict():
    bodies = _bodies(_steps(AGGREGATE, "aggregate"))
    assert any("crawl_sources.py --strict" in b for b in bodies), (
        "without --strict a 404 upstream is a warning, and the job goes green "
        "on a catalog that is quietly ageing")


def test_aggregation_regenerates_notarizes_and_indexes_source_containers():
    steps = _steps(AGGREGATE, "aggregate")
    named = {step.get("name"): step for step in steps}
    migrations = str(
        named["Apply pinned maintainer migrations"].get("run") or ""
    )
    generation = str(
        named["Regenerate aggregated RAPP containers"].get("run") or ""
    )
    receipts = str(named["Mint scoped maintainer receipts"].get("run") or "")
    registry = str(named["Rebuild registry and static API"].get("run") or "")

    assert "apply_maintainer_migrations.py" in migrations
    assert "generate_aggregated_agents.py" in generation
    assert "--namespace @cat-agent-skills" in receipts
    assert "--namespace @cowork-cookbook" in receipts
    assert "--agent @kody-w/connected_solution_agent" in receipts
    assert "--agent @rapter/rapp_dogg_agent" in receipts
    assert "build_registry.py" in registry
    assert "check_url_stability.py --update" in registry
    assert "build_pokedex_api.py" in registry
    assert "build_static_api.py" in registry
    publish = str(
        named["Publish commit-pinned Scout projection"].get("run") or ""
    )
    assert "git pull --ff-only origin main" in publish
    assert "build_scout_exports.py" in publish
    assert "tests/test_scout_rapp_skill.py" in publish
    assert "git add rapp_skill.md rapp_skills.md scout/" in publish


def _dead_source(tmp_path: Path):
    sources = tmp_path / "sources.json"
    sources.write_text(json.dumps({"schema": "rar-sources/1.0", "sources": [{
        "id": "ghost",
        "namespace": "@ghost",
        "format": "cat-skills/1",
        "index_url": "https://example.invalid/skills.json",
        "enabled": True,
    }]}), encoding="utf-8")
    return sources


@pytest.fixture()
def crawler(tmp_path, monkeypatch):
    cs = _load("crawl_sources_strict", REPO_ROOT / "scripts" / "crawl_sources.py")
    out = tmp_path / "aggregated.json"
    out.write_text(json.dumps({"items": [{"ref": "@ghost/kept"}]}), encoding="utf-8")

    def dead(url):
        raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)

    monkeypatch.setattr(cs, "SOURCES_FILE", _dead_source(tmp_path))
    monkeypatch.setattr(cs, "OUT_FILE", out)
    monkeypatch.setattr(cs, "fetch_json", dead)
    monkeypatch.setattr(cs, "FAILURES", [])
    return cs, out


def test_strict_fails_the_run_when_a_source_404s(crawler, monkeypatch):
    cs, out = crawler
    monkeypatch.setattr(sys, "argv", ["crawl_sources.py", "--strict"])
    assert cs.main() == 1, "a 404 upstream must fail the job, not warn"
    assert json.loads(out.read_text(encoding="utf-8"))["items"] == [{"ref": "@ghost/kept"}], (
        "strict must refuse BEFORE writing — a snapshot rebuilt from the "
        "sources that answered is a deletion of the ones that did not")


def test_the_default_posture_is_still_non_fatal(crawler, monkeypatch):
    """refresh-ratings.yml runs the crawler as one of six snapshot steps. A bad
    day upstream there must not fail the other five, so --strict is opt-in and
    the default behaviour is unchanged."""
    cs, out = crawler
    monkeypatch.setattr(sys, "argv", ["crawl_sources.py"])
    assert cs.main() == 0
    assert json.loads(out.read_text(encoding="utf-8"))["items"] == [{"ref": "@ghost/kept"}]


def test_the_catalog_is_verified_before_the_ranking_is_committed():
    """--strict catches a source that went dark on THIS run. It cannot catch a
    catalog that was already wrong on disk, which is the state a commit would
    make permanent."""
    bodies = _bodies(_steps(AGGREGATE, "aggregate"))
    verify = next(i for i, b in enumerate(bodies) if "not fit to publish" in b)
    stage = next(i for i, b in enumerate(bodies) if "git add" in b)
    assert verify < stage


# ─── Least privilege, and no two runs racing to push ─────────────────────

def test_permissions_are_explicit_and_minimal():
    doc = _doc(AGGREGATE)
    assert doc.get("permissions") == {"contents": "write"}, (
        "this job commits two files and does nothing else; anything beyond "
        "contents: write is privilege it cannot justify")


def test_two_runs_cannot_race_each_other_into_a_push_conflict():
    doc = _doc(AGGREGATE)
    concurrency = doc.get("concurrency") or {}
    assert concurrency.get("group"), "no concurrency group; two runs would both push"
    assert concurrency.get("cancel-in-progress") is False, (
        "cancelling the run already in flight can kill it mid-push")


def test_it_runs_on_a_schedule_and_on_demand():
    doc = _doc(AGGREGATE)
    raw = doc[True] if True in doc else doc["on"]
    assert raw["schedule"], "a frozen aggregate is the whole problem this solves"
    assert "workflow_dispatch" in raw, "a maintainer must be able to repair staleness"
    # Not on the hour: GitHub queues :00 crons behind everybody else's.
    for entry in raw["schedule"]:
        assert not entry["cron"].startswith("0 "), (
            f"top-of-hour cron is delivered late under load -> {entry['cron']}")
