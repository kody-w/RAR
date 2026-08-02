"""The release path, tested without cutting a release.

Everything here used to be shell inside release.yml, which meant the only way
to find out it was wrong was to publish something wrong. Each test below pins
a defect that was live in that workflow.
"""
from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
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
    # Quote-agnostic: the same bug written with double quotes was invisible to
    # the original single-quoted substring check.
    assert not re.search(r"""reg\[['"]latest_release['"]\]\s*=""", src), (
        "the release workflow writes latest_release straight into registry.json"
    )
    assert "state/releases.json" in src


def _minimal_repo(tmp_path, ledger=None):
    """A tree just large enough to run build_registry.py for real."""
    (tmp_path / "agents" / "@test").mkdir(parents=True)
    (tmp_path / "state").mkdir()
    shutil.copy(REPO_ROOT / "build_registry.py", tmp_path / "build_registry.py")
    # build_registry.py imports rapp_sdk once an agent validates cleanly.
    shutil.copy(REPO_ROOT / "rapp_sdk.py", tmp_path / "rapp_sdk.py")
    (tmp_path / "agents" / "@test" / "foo_agent.py").write_text(
        '"""T."""\nfrom agents.basic_agent import BasicAgent\n\n'
        '__manifest__ = {"schema": "rapp-agent/1.0", "name": "@test/foo",\n'
        '  "version": "1.0.0", "display_name": "Foo", "description": "d.",\n'
        '  "author": "T", "tags": ["t"], "category": "core"}\n\n'
        "class FooAgent(BasicAgent):\n"
        "    name = 'Foo'\n"
        "    def perform(self, **kwargs):\n        return 'ok'\n"
    )
    if ledger is not None:
        (tmp_path / "state" / "releases.json").write_text(json.dumps(ledger))
    return tmp_path


def test_build_registry_actually_projects_the_ledger(tmp_path):
    """RUNS build_registry.py and reads its output.

    The original version of this test grepped build_registry.py for two exact
    source substrings, and its sibling asserted `entries[-1]["tag"]` against a
    dict literal it had just written — testing Python list indexing. Both were
    green while the projection could have been deleted entirely.
    """
    repo = _minimal_repo(tmp_path, ledger={
        "schema": "rar-releases/1.0",
        "releases": [{"tag": "v1.0.0", "release_name": "Genesis"},
                     {"tag": "v2.0.0", "release_name": "Spring 2026"}],
    })
    subprocess.run([sys.executable, "build_registry.py"], cwd=repo,
                   capture_output=True, text=True, timeout=120)
    reg = json.loads((repo / "registry.json").read_text())
    assert reg.get("latest_release", {}).get("tag") == "v2.0.0", (
        "state/releases.json is not projected into registry.json — the release "
        "ledger is invisible to every consumer"
    )
    assert len(reg.get("releases", [])) == 2


def test_registry_build_survives_a_malformed_ledger(tmp_path):
    """A hand-edited ledger must not take the whole registry build down.

    The guard caught JSONDecodeError/OSError/AttributeError, which does not
    cover a `releases` value that is an object or a number.
    """
    for bad in ({"releases": {"not": "a list"}}, {"releases": 7}, {"releases": "x"}):
        repo = _minimal_repo(tmp_path / f"r{abs(hash(str(bad)))}", ledger=bad)
        r = subprocess.run([sys.executable, "build_registry.py"], cwd=repo,
                           capture_output=True, text=True, timeout=120)
        assert (repo / "registry.json").exists(), (
            f"build_registry.py produced no registry for ledger {bad!r}\n{r.stderr[-500:]}"
        )
        reg = json.loads((repo / "registry.json").read_text())
        lr = reg.get("latest_release")
        assert lr is None or isinstance(lr, dict), (
            f"garbage projected as latest_release for ledger {bad!r}: {lr!r}"
        )


# ─── Workflow injection ────────────────────────────────────────────────

def test_release_name_never_reaches_a_shell_or_js_context_via_interpolation():
    """`release_name` is free text from workflow_dispatch. github-script
    substitutes ${{ }} into the JavaScript SOURCE before running it, so a
    backtick in the name executes on the runner; in `git commit -m` it splices
    into the command line. Both must read the value from env at runtime."""
    src = (REPO_ROOT / ".github" / "workflows" / "release.yml").read_text()
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
    fails loudly; you find out by looking at the tag list.

    Checks that the step id EXISTS, not that the named output is written:
    a step can emit outputs from a program it calls (process_issues.py writes
    to $GITHUB_OUTPUT from Python), which no static scan of the run body can
    see. Asserting on that produced eighteen false positives on a workflow
    that was entirely correct."""
    import re

    import yaml

    ref = re.compile(r"steps\.([A-Za-z0-9_-]+)\.outputs\.[A-Za-z0-9_-]+")
    problems = []
    for wf in sorted((REPO_ROOT / ".github" / "workflows").glob("*.yml")):
        doc = yaml.safe_load(wf.read_text()) or {}
        for jname, job in (doc.get("jobs") or {}).items():
            steps = job.get("steps") or []
            ids = {s.get("id") for s in steps if s.get("id")}
            for sid in set(ref.findall(yaml.dump(job))):
                if sid not in ids:
                    problems.append(
                        f"{wf.name}::{jname}: steps.{sid}.outputs.* — no step has id '{sid}'"
                    )
    assert not problems, "unresolvable step output reference: " + "; ".join(problems)



def test_registry_is_rebuilt_before_the_seal_is_computed():
    """The integrity seal must describe the registry that actually ships.

    The metadata step seals every agent digest; a later step rebuilds
    registry.json and it is the REBUILT file that gets committed, tagged, and
    turned into release assets. Measuring before that rebuild published a seal
    over the old file — unrecomputable from the release, which is the only
    thing a seal is for — and left latest_release.agent_count contradicting
    stats.total_agents inside the same file.

    Reachable whenever the committed registry is behind agents/: a new
    `.py.stub` does not match build-registry.yml's `agents/**/*.py` trigger, so
    no rebuild is ever fired for it, and the URL-stability ledger only tracks
    `.py` — so it clears every validate gate and lands here."""
    import yaml

    doc = yaml.safe_load((REPO_ROOT / ".github" / "workflows" / "release.yml").read_text())
    steps = doc["jobs"]["release"]["steps"]

    build_at = seal_at = None
    for i, s in enumerate(steps):
        body = str(s.get("run", ""))
        if build_at is None and "build_registry.py" in body:
            build_at = i
        if seal_at is None and "integrity_seal" in body:
            seal_at = i

    assert build_at is not None, "the release job never rebuilds registry.json"
    assert seal_at is not None, "the release job never computes an integrity seal"
    assert build_at < seal_at, (
        f"registry.json is rebuilt at step {build_at} but the seal is computed at "
        f"step {seal_at} — the published seal describes a registry that is not "
        "the one committed, tagged, and shipped as assets"
    )


def test_computed_tag_is_not_interpolated_into_shell():
    src = (REPO_ROOT / ".github" / "workflows" / "release.yml").read_text()
    for line in src.splitlines():
        if "steps.tag.outputs.tag" in line:
            stripped = line.strip()
            # `tag=$(...)` writes the computed value to $GITHUB_OUTPUT and is
            # fine, but the previous allowlist accepted any line starting
            # `tag=` — including the shell-assignment form this test exists to
            # forbid. Require an env: binding, or the one $GITHUB_OUTPUT write.
            ok = stripped.startswith("RELEASE_TAG:") or (
                stripped.startswith("tag=") and "GITHUB_OUTPUT" in stripped
            )
            assert ok, f"tag interpolated into a command -> {stripped}"


# ─── Release notes must describe the policy that is actually enforced ──

def test_release_notes_do_not_claim_eval_exec_are_blocked():
    """The registry deliberately PERMITS eval/exec and tags them as
    capabilities; subprocess is intentionally not banned either. The notes
    claimed all three were rejected, which is a published false statement
    about what the scan guarantees."""
    src = (REPO_ROOT / ".github" / "workflows" / "release.yml").read_text()
    assert "no eval/exec/subprocess/hardcoded secrets" not in src
    assert "_capabilities" in src


def test_security_allowlist_waives_nothing_dangerous():
    """A waiver may not excuse a rule that is actually enforced.

    SECURITY_ALLOWLIST was written when eval/exec were banned, to excuse ten
    agents that legitimately needed them. eval/exec then moved to
    CAPABILITY_PATTERNS (allowed for everyone, merely tagged) and subprocess
    was dropped from the ban list — so the waiver stopped excusing what it was
    written for and started excusing the only three rules left, one of which is
    HARDCODED SECRETS. A secret committed in an allowlisted agent shipped
    unflagged.

    Rather than forbid the mechanism, forbid it being load-bearing: any file
    listed here must pass the scan on its own merits."""
    import re as _re
    import sys as _sys

    _sys.path.insert(0, str(REPO_ROOT))
    from build_registry import DANGEROUS_PATTERNS, SECURITY_ALLOWLIST

    offenders = []
    for rel in sorted(SECURITY_ALLOWLIST):
        p = REPO_ROOT / rel
        if not p.exists():
            offenders.append(f"{rel}: stale entry, file does not exist")
            continue
        src = p.read_text(encoding="utf-8")
        for pat, msg in DANGEROUS_PATTERNS:
            if _re.search(pat, src):
                offenders.append(f"{rel}: waived from an ENFORCED rule — {msg}")
    assert not offenders, "security allowlist is waiving real findings: " + "; ".join(offenders)


def test_release_type_options_are_exactly_what_the_tag_script_accepts():
    """Reads the script's argparse choices instead of restating them.

    The previous version hardcoded {"seasonal","hotfix","canary"} on both sides
    and called next_tag() directly, bypassing the argparse `choices` list the
    workflow actually goes through — so adding a fourth option to the script
    and the dropdown, but not to the hardcoded set, failed the test for the
    wrong reason, and adding it to only the dropdown was invisible."""
    import re as _re

    import yaml

    doc = yaml.safe_load((REPO_ROOT / ".github" / "workflows" / "release.yml").read_text())
    triggers = doc[True] if True in doc else doc["on"]
    options = set(triggers["workflow_dispatch"]["inputs"]["release_type"]["options"])

    src = (REPO_ROOT / "scripts" / "next_release_tag.py").read_text()
    m = _re.search(r'add_argument\(\s*"--type".*?choices=\[(.*?)\]', src, _re.S)
    assert m, "could not find the --type choices in next_release_tag.py"
    accepted = set(_re.findall(r'"([^"]+)"', m.group(1)))

    assert options == accepted, (
        f"release.yml offers {sorted(options)} but the tag script accepts "
        f"{sorted(accepted)} — a dropdown option the script rejects fails at "
        "tag time, after every gate has passed"
    )
    for rtype in sorted(options):
        assert nrt.next_tag(["v1.0.0"], rtype, "20260801").startswith("v")


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
