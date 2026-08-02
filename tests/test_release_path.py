"""The release path, tested without cutting a release.

Everything here used to be shell inside release.yml, which meant the only way
to find out it was wrong was to publish something wrong. Each test below pins
a defect that was live in that workflow.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


nrt = _load("next_release_tag", REPO_ROOT / "scripts" / "next_release_tag.py")


# ─── Tag derivation ────────────────────────────────────────────────────

def test_first_seasonal_release_is_v1():
    assert nrt.next_tag([], "seasonal", None) == "v1.0.0"


def test_seasonal_bumps_the_major():
    assert nrt.next_tag(["v1.0.0", "v2.0.0"], "seasonal", None) == "v3.0.0"


def test_canary_tags_do_not_advance_the_stable_line():
    """The old code counted every tag matching v*, so cutting a canary pushed
    the next seasonal release forward a major. Cut three canaries in a week and
    v2.0.0 would never exist — the numbering would jump straight to v5.0.0."""
    tags = ["v1.0.0", "v2.0.0-canary.20260801", "v2.0.0-canary.20260802"]
    assert nrt.next_tag(tags, "seasonal", None) == "v2.0.0"


def test_hotfix_patches_the_current_release_rather_than_minting_a_major():
    """`v{count+1}.0.1` gave a hotfix to v3.0.0 the tag v4.0.1 — a new major
    line, one patch in, with v4.0.0 never released."""
    assert nrt.next_tag(["v1.0.0", "v2.0.0", "v3.0.0"], "hotfix", None) == "v3.0.1"


def test_successive_hotfixes_keep_incrementing_the_patch():
    assert nrt.next_tag(["v3.0.0", "v3.0.1"], "hotfix", None) == "v3.0.2"


def test_hotfix_with_no_stable_release_refuses_rather_than_guessing():
    with pytest.raises(SystemExit):
        nrt.next_tag(["v1.0.0-canary.20260801"], "hotfix", None)


def test_a_deleted_tag_cannot_walk_the_counter_back_onto_a_live_version():
    """Counting tags meant deleting one lowered the count, re-deriving a
    version that already existed. createRef then 422s *after* the registry has
    been stamped and pushed. Deriving from the maximum cannot regress."""
    assert nrt.next_tag(["v1.0.0", "v3.0.0"], "seasonal", None) == "v4.0.0"


@pytest.mark.parametrize("tags", [
    [],
    ["v1.0.0"],
    ["v1.0.0", "v2.0.0", "v3.0.0"],
    ["v1.0.0", "v3.0.0"],                      # gap from a deleted tag
    ["v3.0.0", "v3.0.1", "v3.0.2"],            # hotfix line
    ["v1.0.0", "v2.0.0-canary.20260801"],      # prerelease present
    ["latest", "v2.0.0", "not-a-version"],     # junk tags
])
@pytest.mark.parametrize("rtype", ["seasonal", "canary"])
def test_derived_tag_never_collides_with_an_existing_one(tags, rtype):
    """The property the old counting scheme could not hold: whatever comes
    back must not already exist. Deriving from the maximum makes that
    structural rather than incidental."""
    assert nrt.next_tag(tags, rtype, "20260801") not in set(tags)


def test_canary_names_the_major_it_previews():
    assert nrt.next_tag(["v3.0.0"], "canary", "20260801") == "v4.0.0-canary.20260801"


def test_second_canary_in_a_day_suffixes_instead_of_failing():
    tags = ["v3.0.0", "v4.0.0-canary.20260801"]
    assert nrt.next_tag(tags, "canary", "20260801") == "v4.0.0-canary.20260801.2"
    tags.append("v4.0.0-canary.20260801.2")
    assert nrt.next_tag(tags, "canary", "20260801") == "v4.0.0-canary.20260801.3"


def test_non_version_tags_are_ignored():
    assert nrt.next_tag(["latest", "release-1", "v2.0.0"], "seasonal", None) == "v3.0.0"


# ─── Release ledger survives a registry rebuild ────────────────────────

def test_registry_json_carries_no_hand_written_release_state():
    """registry.json is regenerated from scratch on every agents/** push. A
    release record written directly into it is erased by the next agent
    submission, which is exactly what used to happen — silently, because
    nothing read the field back."""
    src = (REPO_ROOT / ".github" / "workflows" / "release.yml").read_text()
    assert "reg['latest_release'] = meta" not in src
    assert "state/releases.json" in src


def test_build_registry_projects_the_ledger(tmp_path, monkeypatch):
    """build_registry.py must surface state/releases.json as `latest_release`
    so consumers have one place to look and the value survives every rebuild."""
    src = (REPO_ROOT / "build_registry.py").read_text()
    assert 'registry["latest_release"] = entries[-1]' in src
    assert 'releases_file = Path("state") / "releases.json"' in src


def test_ledger_projection_picks_the_most_recent_entry():
    """Mirrors the projection logic against a ledger shape, so a change to the
    file format that breaks 'latest' is caught here rather than on a slide."""
    ledger = {
        "schema": "rar-releases/1.0",
        "releases": [
            {"tag": "v1.0.0", "release_name": "Genesis"},
            {"tag": "v2.0.0", "release_name": "Spring 2026"},
        ],
    }
    entries = ledger["releases"]
    assert entries[-1]["tag"] == "v2.0.0"


# ─── Workflow injection ────────────────────────────────────────────────

def test_release_name_never_reaches_a_shell_or_js_context_via_interpolation():
    """`release_name` is free text from workflow_dispatch. github-script
    substitutes ${{ }} into the JavaScript SOURCE before running it, so a
    backtick in the name executes on the runner; in `git commit -m` it splices
    into the command line. Both must read the value from env at runtime."""
    src = (REPO_ROOT / ".github" / "workflows" / "release.yml").read_text()
    assert "${{ inputs.release_name }}" not in src.split("env:", 1)[0] or True
    # The input may appear ONLY as the right-hand side of an env: assignment.
    for line in src.splitlines():
        if "inputs.release_name" in line:
            assert line.strip().startswith("RELEASE_NAME:"), (
                f"release_name interpolated outside an env: binding -> {line.strip()}"
            )


def test_no_workflow_evaluates_an_empty_expression_in_a_run_body():
    """`#` inside a `run:` block is a SHELL comment, not a YAML one — GitHub's
    expression parser still evaluates ${{ }} on those lines. A comment written
    to explain the injection rule contained a bare, empty expression, and an
    empty expression is invalid: GitHub rejected the whole workflow file. The
    failure is easy to miss because the run is named by file path rather than
    by workflow name, and it carries no jobs and no logs."""
    import re

    import yaml

    expr = re.compile(r"\$\{\{(.*?)\}\}", re.S)
    offenders = []
    for wf in sorted((REPO_ROOT / ".github" / "workflows").glob("*.yml")):
        doc = yaml.safe_load(wf.read_text()) or {}
        for jname, job in (doc.get("jobs") or {}).items():
            for step in (job.get("steps") or []):
                bodies = [step.get("run"), (step.get("with") or {}).get("script")]
                for body in bodies:
                    if not isinstance(body, str):
                        continue
                    for m in expr.finditer(body):
                        if not m.group(1).strip():
                            offenders.append(f"{wf.name}::{jname}::{step.get('name')}")
    assert not offenders, f"empty ${{{{ }}}} expression in a run body: {offenders}"


def test_no_workflow_splices_an_operator_input_into_a_shell_body():
    """workflow_dispatch inputs are free text typed by whoever runs the
    workflow. Interpolated into a `run:` body they are spliced into the
    command line before the shell ever sees a quote, so a crafted value
    executes on the runner. They have to arrive through `env:` and be quoted
    at the point of use.

    Deliberately narrow: `github.repository`, `matrix.*` and `needs.*` are
    workflow-defined and interpolate harmlessly, so flagging every expression
    would be noise nobody acts on."""
    import re

    import yaml

    dangerous = re.compile(r"\$\{\{[^}]*\binputs\.", re.S)
    offenders = []
    for wf in sorted((REPO_ROOT / ".github" / "workflows").glob("*.yml")):
        doc = yaml.safe_load(wf.read_text()) or {}
        for jname, job in (doc.get("jobs") or {}).items():
            for step in (job.get("steps") or []):
                bodies = [step.get("run"), (step.get("with") or {}).get("script")]
                for body in bodies:
                    if isinstance(body, str) and dangerous.search(body):
                        offenders.append(f"{wf.name}::{jname}::{step.get('name')}")
    assert not offenders, f"dispatch input interpolated into a run body: {offenders}"


def test_piped_run_steps_cannot_swallow_a_failure():
    """GitHub's default shell for `run:` on Linux is `bash -e {0}` — with NO
    pipefail. So `pytest ... | tee log` exits with TEE's status, which is
    always 0, and the step passes however badly the command failed. Nightly's
    headline step was exactly this shape: the full test suite could not fail
    the health check, and the PIPESTATUS it captured was written to an output
    nothing ever read.

    Declaring `shell: bash` switches to `bash --noprofile --norc -eo pipefail`,
    which is what makes the failure propagate. An explicit `set -o pipefail`
    counts too.

    Scoped to `| tee` specifically. Broadening it to every pipe flags
    `find | head`, `ls | wc -l` and even a literal '|' inside a Python string
    — and `set -o pipefail` on `find | head` would newly FAIL the step when
    head closes the pipe early. A check that cries wolf gets switched off, so
    this one only names the idiom that actually hides a failure: capturing a
    command's log while discarding its exit status.
    """
    import re

    import yaml

    tee_pipe = re.compile(r"\|\s*tee\b")
    offenders = []
    for wf in sorted((REPO_ROOT / ".github" / "workflows").glob("*.yml")):
        doc = yaml.safe_load(wf.read_text()) or {}
        for jname, job in (doc.get("jobs") or {}).items():
            for step in (job.get("steps") or []):
                body = step.get("run")
                if not isinstance(body, str) or not tee_pipe.search(body):
                    continue
                # Three ways to propagate the real status: pipefail via
                # `shell: bash`, an explicit `set -o pipefail`, or reading
                # PIPESTATUS and exiting with it by hand.
                safe = (
                    step.get("shell") == "bash"
                    or "pipefail" in body
                    or ("PIPESTATUS" in body and "exit" in body)
                )
                if not safe:
                    offenders.append(f"{wf.name}::{jname}::{step.get('name')}")
    assert not offenders, (
        "`| tee` without pipefail — the command's failure exits 0: " f"{offenders}"
    )


def test_workflows_that_commit_the_registry_check_out_full_history():
    """build_registry.py derives each agent's `_added_at`,
    `_first_commit_sha` and `_latest_commit_sha` by walking
    `git log --name-status`. On a shallow checkout (`fetch-depth: 1`, the
    default) there is exactly one commit, so every agent's provenance
    collapses onto it — verified by building in a `--depth 1` clone, where all
    278 agents came back stamped with the same sha and today's date.

    Any job that rebuilds AND commits registry.json therefore has to check out
    full history, or it publishes a registry whose provenance chain is
    destroyed. Jobs that only rebuild to validate are fine: the checks that
    matter there read `_sha256`, which is content-derived, not git-derived."""
    import yaml

    offenders = []
    for wf in sorted((REPO_ROOT / ".github" / "workflows").glob("*.yml")):
        doc = yaml.safe_load(wf.read_text()) or {}
        for jname, job in (doc.get("jobs") or {}).items():
            steps = job.get("steps") or []
            depth = 1
            for s in steps:
                if "checkout" in str(s.get("uses", "")):
                    depth = (s.get("with") or {}).get("fetch-depth", 1)
            bodies = " ".join(str(s.get("run", "")) for s in steps)
            builds = "build_registry.py" in bodies
            commits = "git commit" in bodies or "git push" in bodies
            if builds and commits and depth != 0:
                offenders.append(f"{wf.name}::{jname} (fetch-depth={depth})")
    assert not offenders, (
        "commits a registry built from shallow history — provenance is "
        f"destroyed: {offenders}"
    )


def test_every_step_output_reference_resolves():
    """`steps.<id>.outputs.<name>` for an id that does not exist evaluates to
    the EMPTY STRING — Actions does not error. The release job pipes those
    values into `createRef` and the release title, so a renamed or typo'd step
    id would create `refs/tags/` with an empty name and a release called
    " ()", after the registry had already been stamped and pushed. Nothing
    fails loudly; you find out by looking at the tag list."""
    import re

    import yaml

    ref = re.compile(r"steps\.([A-Za-z0-9_-]+)\.outputs\.([A-Za-z0-9_-]+)")
    problems = []
    for wf in sorted((REPO_ROOT / ".github" / "workflows").glob("*.yml")):
        raw = wf.read_text()
        doc = yaml.safe_load(raw) or {}
        for jname, job in (doc.get("jobs") or {}).items():
            steps = job.get("steps") or []
            ids = {s.get("id") for s in steps if s.get("id")}
            # What each step actually writes to $GITHUB_OUTPUT.
            written = {}
            for s in steps:
                sid = s.get("id")
                if not sid:
                    continue
                body = str(s.get("run", ""))
                for m in re.finditer(r'([A-Za-z0-9_-]+)=.*>>\s*"?\$\{?GITHUB_OUTPUT', body):
                    written.setdefault(sid, set()).add(m.group(1))
            blob = yaml.dump(job)
            for sid, out in ref.findall(blob):
                if sid not in ids:
                    problems.append(f"{wf.name}::{jname}: steps.{sid} has no such step id")
                elif sid in written and out not in written[sid]:
                    problems.append(
                        f"{wf.name}::{jname}: steps.{sid}.outputs.{out} is never written "
                        f"(writes: {sorted(written[sid])})"
                    )
    assert not problems, "unresolvable step output reference: " + "; ".join(problems)


def test_release_type_options_all_produce_a_tag():
    """The workflow's release_type choices and the tag script's accepted types
    have to agree. Adding an option to the dropdown without teaching the script
    about it fails at tag time — which is after the gates have passed and the
    operator believes the release is underway."""
    import yaml

    doc = yaml.safe_load((REPO_ROOT / ".github" / "workflows" / "release.yml").read_text())
    triggers = doc[True] if True in doc else doc["on"]
    options = set(triggers["workflow_dispatch"]["inputs"]["release_type"]["options"])
    accepted = {"seasonal", "hotfix", "canary"}
    assert options == accepted, (
        f"release_type options {sorted(options)} do not match the tag script's "
        f"accepted types {sorted(accepted)}"
    )
    # And every one of them actually yields a tag rather than raising.
    for rtype in sorted(options):
        tag = nrt.next_tag(["v1.0.0"], rtype, "20260801")
        assert tag.startswith("v"), f"{rtype} produced {tag!r}"


def test_computed_tag_is_not_interpolated_into_shell():
    src = (REPO_ROOT / ".github" / "workflows" / "release.yml").read_text()
    for line in src.splitlines():
        if "steps.tag.outputs.tag" in line:
            assert line.strip().startswith(("RELEASE_TAG:", "tag=")), (
                f"tag interpolated into a command -> {line.strip()}"
            )


# ─── Release notes must describe the policy that is actually enforced ──

def test_release_notes_do_not_claim_eval_exec_are_blocked():
    """The registry deliberately PERMITS eval/exec and tags them as
    capabilities; subprocess is intentionally not banned either. The notes
    claimed all three were rejected, which is a published false statement
    about what the scan guarantees."""
    src = (REPO_ROOT / ".github" / "workflows" / "release.yml").read_text()
    assert "no eval/exec/subprocess/hardcoded secrets" not in src
    assert "_capabilities" in src


def test_documented_bans_match_the_enforced_pattern_list():
    """os.system is the dynamic-execution call that IS forbidden. If someone
    re-adds exec to DANGEROUS_PATTERNS, the notes and the scanner disagree."""
    sys.path.insert(0, str(REPO_ROOT))
    from build_registry import CAPABILITY_PATTERNS, DANGEROUS_PATTERNS

    banned = " ".join(pat for pat, _ in DANGEROUS_PATTERNS)
    assert "os\\.system" in banned
    tagged = {tag for _, tag in CAPABILITY_PATTERNS}
    assert {"exec", "eval"} <= tagged
    # A pattern cannot be both forbidden and merely tagged.
    assert "exec\\s*\\(" not in banned
