"""
Dream Catcher delta bundles: merged deltas fold into bundle files without loss.

Nothing produced in any frame is ever lost (rappterpedia/dream_catcher.py, rule
5). Folding is a storage change only, so these tests hold it to that: a fold
followed by an extract reproduces every original delta file byte for byte, a
merge reads bundled deltas exactly as it read loose ones, and every delta file
ever deleted from stream_deltas/ in this repository's history is still in a
bundle with its original bytes. The one exemption is a delta HELD_LOOSE has
named: held deltas are never folded, so deleting one is its owner redacting it.

The fold/merge tests run in a throwaway directory, never the real repository.
"""

import ast
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
DREAM_CATCHER = REPO_ROOT / "rappterpedia" / "dream_catcher.py"
DREAM_CATCHER_PATH = "rappterpedia/dream_catcher.py"
DELTAS = "rappterpedia/stream_deltas"
HEARTBEAT = REPO_ROOT / ".github" / "workflows" / "rappterpedia-heartbeat.yml"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, DREAM_CATCHER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


repo_dc = _load("_dream_catcher_repo")


@pytest.fixture
def dc(tmp_path, monkeypatch):
    mod = _load("_dream_catcher_sandbox")
    base = tmp_path / "rappterpedia"
    (base / "stream_deltas").mkdir(parents=True)
    monkeypatch.setattr(mod, "DELTAS_DIR", base / "stream_deltas")
    monkeypatch.setattr(mod, "BUNDLES_DIR", base / "stream_deltas" / "bundles")
    monkeypatch.setattr(mod, "STATE_FILE", base / "rappterpedia_state.json")
    monkeypatch.setattr(mod, "EXPORT_FILE", base / "rappterpedia_export.json")
    return mod


def _delta(frame, stream, articles=(), threads=(), reviews=()):
    return {"frame": frame, "stream_id": stream, "completed_at": "2026-09-25T00:00:00Z",
            "articles_created": list(articles), "threads_created": list(threads),
            "reviews_created": list(reviews)}


def _article(pk, title, **extra):
    return {"pk": pk, "title": title, "category": "agents", "tags": ["t"],
            "content": f"{title} body", "author": "AgentSmith", "source": "llm",
            "created": "2026-09-25T00:00:00Z", "updated": "2026-09-25T00:00:00Z", **extra}


def _state(dc, tick):
    dc.save_json(dc.STATE_FILE, {"tick_count": tick, "articles": [], "threads": [], "reviews": {},
                                 "next_article_id": 1, "next_thread_id": 1,
                                 "generated_topics": [], "generated_agent_ids": []})


def _loose(dc):
    return sorted(p.name for p in dc.DELTAS_DIR.glob("frame-*.json"))


def _bundle_bytes(dc):
    return {p.name: p.read_bytes() for p in dc.bundle_paths()}


def _write_originals(dc):
    """A realistic spread: empty and content-bearing deltas across three windows,
    the ' 2.json' copies a file sync once left behind, and non-ASCII text."""
    originals = {}
    for frame in (42, 99, 100, 150, 240, 250):
        for stream in ("alpha", "bravo", "refill"):
            name = f"frame-{frame}-{stream}.json"
            dc.save_json(dc.DELTAS_DIR / name, _delta(frame, stream))
    dc.save_json(dc.DELTAS_DIR / "frame-150-alpha.json", _delta(
        150, "alpha", articles=[_article("150:a", "Café — naïve ✓")],
        threads=[{"pk": "150:t", "title": "Discussion", "replies": [{"content": "yes"}]}]))
    dc.save_json(dc.DELTAS_DIR / "frame-240-alpha 2.json", _delta(240, "alpha"))
    dc.save_json(dc.DELTAS_DIR / "frame-99-live-demo.json", _delta(99, "live-demo"))
    for path in dc.DELTAS_DIR.glob("frame-*.json"):
        originals[path.name] = path.read_bytes()
    return originals


def test_fold_then_extract_reproduces_every_delta_byte_for_byte(dc, tmp_path):
    originals = _write_originals(dc)
    _state(dc, 250)

    report = dc.fold_merged_deltas()

    assert report["folded"] == len(originals) and report["kept"] == {}
    assert _loose(dc) == []
    assert sorted(_bundle_bytes(dc)) == ["frames-000000-000099.json", "frames-000100-000199.json",
                                         "frames-000200-000299.json"]
    for path in dc.bundle_paths():
        assert path.stat().st_size <= dc.BUNDLE_MAX_BYTES
    out = tmp_path / "extracted"
    assert dc.extract_bundled_deltas(out) == len(originals)
    assert {p.name: p.read_bytes() for p in out.iterdir()} == originals


def test_fold_is_idempotent(dc):
    _write_originals(dc)
    _state(dc, 250)
    dc.fold_merged_deltas()
    before = _bundle_bytes(dc)

    again = dc.fold_merged_deltas()

    assert again == {"folded": 0, "kept": {}, "written": []}
    assert _bundle_bytes(dc) == before


def test_fold_leaves_unmerged_unreproducible_and_held_deltas_loose(dc, monkeypatch):
    _state(dc, 10)
    monkeypatch.setattr(dc, "HELD_LOOSE", frozenset({"frame-5-held.json"}))
    dc.save_json(dc.DELTAS_DIR / "frame-10-alpha.json", _delta(10, "alpha"))
    dc.save_json(dc.DELTAS_DIR / "frame-11-alpha.json", _delta(11, "alpha"))
    odd = {
        "frame-5-broken.json": b'{"frame": 5,',
        "frame-5-list.json": b"[1, 2]",
        "frame-5-frame.json": json.dumps({"spec": "rapp/1", "kind": "x"}, indent=2).encode(),
        "frame-5-pretty.json": json.dumps(_delta(5, "pretty"), indent=4).encode(),
        "frame-5-nan.json": b'{"frame": NaN}',
        "frame-5-held.json": dc.delta_file_bytes(_delta(5, "held")),
    }
    for name, raw in odd.items():
        (dc.DELTAS_DIR / name).write_bytes(raw)

    report = dc.fold_merged_deltas()

    assert report["folded"] == 1
    assert sorted(report["kept"]) == sorted(odd)
    assert _loose(dc) == sorted([*odd, "frame-11-alpha.json"])
    for name, raw in odd.items():
        assert (dc.DELTAS_DIR / name).read_bytes() == raw


def test_merge_reads_bundled_deltas_exactly_like_loose_ones(dc):
    _state(dc, 6)
    state = json.loads(dc.STATE_FILE.read_text())
    state["articles"].append({"id": "dc-art-0001", "pk": "1:a", "title": "Stub", "content": "short"})
    state["next_article_id"] = 2
    dc.save_json(dc.STATE_FILE, state)
    dc.save_json(dc.DELTAS_DIR / "frame-7-alpha.json", _delta(
        7, "alpha", articles=[_article("7:a", "Deep Dive: One"), _article("7:b", "Deep Dive: Two")],
        threads=[{"pk": "7:t", "title": "Discussion: tiers", "replies": []}]))
    dc.save_json(dc.DELTAS_DIR / "frame-7-bravo.json", _delta(
        7, "bravo", articles=[_article("7:a", "Deep Dive: One")],
        reviews=[{"agent_name": "@kody-w/x", "text": "useful"}]))
    dc.save_json(dc.DELTAS_DIR / "frame-7-refill.json", _delta(
        7, "refill", articles=[_article("7:r", "Stub", _refill_id="dc-art-0001",
                                        content="long " * 70, source="llm-refill")]))
    dc.save_json(dc.DELTAS_DIR / "frame-8-alpha.json", _delta(8, "alpha"))
    initial = dc.STATE_FILE.read_bytes()
    loose_view = dc.load_frame_deltas(7)

    dc.merge_deltas(7)
    from_loose = dc.STATE_FILE.read_bytes()
    assert _loose(dc) == ["frame-8-alpha.json"]
    assert dc.load_frame_deltas(7) == loose_view

    dc.STATE_FILE.write_bytes(initial)
    dc.merge_deltas(7)
    assert dc.STATE_FILE.read_bytes() == from_loose
    merged = json.loads(from_loose)
    assert [a["id"] for a in merged["articles"]] == ["dc-art-0001", "dc-art-0002", "dc-art-0003"]
    assert merged["articles"][0]["source"] == "llm-refill" and merged["tick_count"] == 7


def test_a_full_window_opens_the_next_part(dc, monkeypatch, tmp_path):
    monkeypatch.setattr(dc, "BUNDLE_MAX_BYTES", 2048)
    _state(dc, 40)
    for frame in range(1, 41):
        dc.save_json(dc.DELTAS_DIR / f"frame-{frame}-alpha.json", _delta(frame, "alpha"))
    dc.save_json(dc.DELTAS_DIR / "frame-3-huge.json",
                 _delta(3, "huge", articles=[_article("3:h", "x" * 4096)]))
    originals = {p.name: p.read_bytes() for p in dc.DELTAS_DIR.glob("frame-*.json")}

    report = dc.fold_merged_deltas()

    names = set(_bundle_bytes(dc))
    assert len(names) > 2
    assert names == {"frames-000000-000099.json"} | {
        f"frames-000000-000099-part{n}.json" for n in range(2, len(names) + 1)}
    assert all(p.stat().st_size <= 2048 for p in dc.bundle_paths())
    assert list(report["kept"]) == ["frame-3-huge.json"] and _loose(dc) == ["frame-3-huge.json"]
    for frame in range(1, 41):
        assert [n for n, _ in dc.load_frame_deltas(frame)] == (
            ["frame-3-alpha.json", "frame-3-huge.json"] if frame == 3 else [f"frame-{frame}-alpha.json"])
    dc.extract_bundled_deltas(tmp_path / "out")
    for path in (tmp_path / "out").iterdir():
        assert path.read_bytes() == originals[path.name]


def test_a_loose_copy_of_a_bundled_name_folds_only_when_identical(dc):
    _state(dc, 5)
    dc.save_json(dc.DELTAS_DIR / "frame-5-alpha.json", _delta(5, "alpha"))
    dc.fold_merged_deltas()
    bundled = _bundle_bytes(dc)

    dc.save_json(dc.DELTAS_DIR / "frame-5-alpha.json", _delta(5, "alpha"))
    assert dc.fold_merged_deltas()["folded"] == 1
    assert _loose(dc) == [] and _bundle_bytes(dc) == bundled

    changed = _delta(5, "alpha", articles=[_article("5:z", "Newer")])
    dc.save_json(dc.DELTAS_DIR / "frame-5-alpha.json", changed)
    report = dc.fold_merged_deltas()
    assert list(report["kept"]) == ["frame-5-alpha.json"] and _bundle_bytes(dc) == bundled
    assert dc.load_frame_deltas(5) == [("frame-5-alpha.json", changed)]



def test_no_writer_overwrites_a_loose_or_bundled_delta(dc, tmp_path, monkeypatch):
    """produce, cycle and refill write a delta name once. A name that a loose or bundled
    delta already has, such as a delta committed before its frame ran, gets the next free
    "<stem> <k>.json" instead, and produce --out-dir never overwrites either."""
    _state(dc, 5)
    dc.save_json(dc.DELTAS_DIR / "frame-5-alpha.json", _delta(5, "alpha"))
    dc.fold_merged_deltas()
    early = dc.delta_file_bytes(_delta(6, "refill", articles=[_article("6:early", "Committed early")]))
    (dc.DELTAS_DIR / "frame-6-refill.json").write_bytes(early)
    bundled_alpha = dc.load_bundle(dc.bundle_paths()[0])["deltas"]["frame-5-alpha.json"]
    made = iter(range(1000))
    monkeypatch.setattr(dc, "produce_delta", lambda stream, frame, ticks=3: _delta(
        frame, stream, articles=[_article(f"{frame}:{stream}:{next(made)}", f"New {stream}")]))
    monkeypatch.setattr(dc, "produce_refill_delta", lambda stream, frame, batch=5: _delta(
        frame, stream, articles=[_article(f"{frame}:{stream}:{next(made)}", "Refilled")]))

    def run(*argv):
        monkeypatch.setattr(sys, "argv", ["dream_catcher.py", *argv])
        dc.main()

    run("produce", "--stream", "alpha", "--frame", "5")
    run("produce", "--stream", "alpha", "--frame", "5")
    assert _loose(dc) == ["frame-5-alpha 2.json", "frame-5-alpha 3.json", "frame-6-refill.json"]
    run("refill", "--frame", "6")
    run("cycle", "--streams", "2", "--frame", "7")
    run("produce", "--stream", "alpha", "--frame", "7")

    bundled = _bundled(dc)
    assert sorted(bundled) == ["frame-5-alpha 2.json", "frame-5-alpha 3.json", "frame-5-alpha.json",
                               "frame-6-refill 2.json", "frame-6-refill.json",
                               "frame-7-alpha.json", "frame-7-bravo.json"]
    assert _loose(dc) == ["frame-7-alpha 2.json"]
    assert bundled["frame-5-alpha.json"] == bundled_alpha
    assert dc.delta_file_bytes(bundled["frame-6-refill.json"]) == early
    assert {"Committed early", "Refilled"} <= {a["title"] for a in json.loads(dc.STATE_FILE.read_text())["articles"]}

    out = tmp_path / "worker"
    run("produce", "--stream", "bravo", "--frame", "8", "--out-dir", str(out))
    written = (out / "frame-8-bravo.json").read_bytes()
    assert [p.name for p in out.iterdir()] == ["frame-8-bravo.json"] and _loose(dc) == ["frame-7-alpha 2.json"]
    with pytest.raises(FileExistsError):
        run("produce", "--stream", "bravo", "--frame", "8", "--out-dir", str(out))
    assert (out / "frame-8-bravo.json").read_bytes() == written


def test_collect_copies_each_delta_in_once_and_never_overwrites_one(dc, tmp_path):
    _state(dc, 5)
    dc.save_json(dc.DELTAS_DIR / "frame-5-alpha.json", _delta(5, "alpha"))
    dc.fold_merged_deltas()
    dc.save_json(dc.DELTAS_DIR / "frame-6-bravo.json", _delta(6, "bravo"))
    bundled, loose_bravo = _bundle_bytes(dc), (dc.DELTAS_DIR / "frame-6-bravo.json").read_bytes()
    inbox = tmp_path / "delta-output"
    arrivals = {
        "delta-alpha/frame-5-alpha.json": _delta(5, "alpha"),
        "delta-bravo/frame-6-bravo.json": _delta(6, "bravo"),
        "delta-charlie/frame-6-charlie.json": _delta(6, "charlie"),
        "delta-delta/frame-6-bravo.json": _delta(6, "bravo", articles=[_article("6:b", "Other")]),
        "delta-echo/frame-5-alpha.json": _delta(5, "alpha", articles=[_article("5:a", "Other")]),
    }
    for relative, delta in arrivals.items():
        (inbox / relative).parent.mkdir(parents=True, exist_ok=True)
        (inbox / relative).write_bytes(dc.delta_file_bytes(delta))
    (inbox / "delta-echo" / "notes.txt").write_text("not a delta", encoding="utf-8")

    def relative(mapping):
        return {Path(source).relative_to(inbox).as_posix(): name for source, name in mapping.items()}

    report = dc.collect_deltas(inbox)

    assert relative(report["collected"]) == {
        "delta-charlie/frame-6-charlie.json": "frame-6-charlie.json",
        "delta-delta/frame-6-bravo.json": "frame-6-bravo 2.json",
        "delta-echo/frame-5-alpha.json": "frame-5-alpha 2.json",
    }
    assert relative(report["present"]) == {
        "delta-alpha/frame-5-alpha.json": "frame-5-alpha.json",
        "delta-bravo/frame-6-bravo.json": "frame-6-bravo.json",
    }
    for source, name in report["collected"].items():
        assert (dc.DELTAS_DIR / name).read_bytes() == Path(source).read_bytes()
    assert (dc.DELTAS_DIR / "frame-6-bravo.json").read_bytes() == loose_bravo
    assert _bundle_bytes(dc) == bundled
    again = dc.collect_deltas(inbox)
    assert again["collected"] == {} and len(again["present"]) == len(arrivals)


def test_extract_never_overwrites_and_never_writes_into_stream_deltas(dc, tmp_path):
    _state(dc, 5)
    dc.save_json(dc.DELTAS_DIR / "frame-5-alpha.json", _delta(5, "alpha"))
    dc.save_json(dc.DELTAS_DIR / "frame-5-bravo.json", _delta(5, "bravo"))
    dc.fold_merged_deltas()
    out = tmp_path / "out"

    assert dc.extract_bundled_deltas(out) == 2
    assert dc.extract_bundled_deltas(out) == 2
    (out / "frame-5-bravo.json").write_bytes(b'{"edited": true}')
    with pytest.raises(FileExistsError):
        dc.extract_bundled_deltas(out)
    assert (out / "frame-5-bravo.json").read_bytes() == b'{"edited": true}'
    for inside in (dc.DELTAS_DIR, dc.BUNDLES_DIR, dc.DELTAS_DIR / "copies"):
        with pytest.raises(ValueError):
            dc.extract_bundled_deltas(inside)
    assert _loose(dc) == [] and not (dc.DELTAS_DIR / "copies").exists()

def test_committed_bundles_are_well_formed_and_reproduce_their_digests():
    seen = {}
    loose = {p.name for p in repo_dc.DELTAS_DIR.glob("frame-*.json")}
    for path in repo_dc.bundle_paths():
        bundle = repo_dc.load_bundle(path)
        assert path.stat().st_size <= repo_dc.BUNDLE_MAX_BYTES < 1024 * 1024
        assert path.read_text(encoding="utf-8") == repo_dc._bundle_text(bundle), (
            f"{path.name} is not in the generator's own layout; regenerate it, never hand-edit")
        for name, delta in bundle["deltas"].items():
            assert hashlib.sha256(repo_dc.delta_file_bytes(delta)).hexdigest() == bundle["sha256"][name]
            assert name not in seen, f"{name} is in both {seen.get(name)} and {path.name}"
            seen[name] = path.name
            assert name not in loose, f"{name} is both loose and in {path.name}"
    assert not repo_dc.HELD_LOOSE & set(seen), "a held delta was folded"


def _git(*args, repo=REPO_ROOT, **kwargs):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, check=True, **kwargs)


def _blobs(repo, specs):
    """The bytes at each `rev:path` spec, or None where that is not a file."""
    if not specs:
        return []
    out = _git("cat-file", "--batch", input="".join(f"{spec}\n" for spec in specs).encode("utf-8"),
               repo=repo).stdout
    blobs, cursor = [], 0
    for _ in specs:
        header_end = out.index(b"\n", cursor)
        header = out[cursor:header_end].split()
        cursor = header_end + 1
        if header[-1] in (b"missing", b"ambiguous"):
            blobs.append(None)
            continue
        size = int(header[2])
        blobs.append(out[cursor:cursor + size] if header[1] == b"blob" else None)
        cursor += size + 1
    return blobs


def _held_loose_in(source):
    """HELD_LOOSE as one revision of dream_catcher.py assigns it (empty if it assigns none)."""
    try:
        module = ast.parse(source)
    except (SyntaxError, ValueError):
        return frozenset()
    held = frozenset()
    for node in module.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            targets = [node.target]
        else:
            continue
        if not any(isinstance(target, ast.Name) and target.id == "HELD_LOOSE" for target in targets):
            continue
        value = node.value
        if isinstance(value, ast.Call) and isinstance(value.func, ast.Name) and value.func.id == "frozenset":
            value = value.args[0] if value.args else ast.Tuple(elts=[], ctx=ast.Load())
        try:
            held = frozenset(ast.literal_eval(value))
        except (TypeError, ValueError):
            held = frozenset()
    return held


def _ever_held(repo):
    """Every name that any committed revision of dream_catcher.py put in HELD_LOOSE."""
    revisions = _git("log", "--format=%H", "--", DREAM_CATCHER_PATH, repo=repo).stdout.decode().split()
    sources = _blobs(repo, [f"{commit}:{DREAM_CATCHER_PATH}" for commit in revisions])
    return frozenset().union(*(_held_loose_in(source) for source in sources if source is not None))


def _bundled(mod):
    bundled = {}
    for path in mod.bundle_paths():
        bundled.update(mod.load_bundle(path)["deltas"])
    return bundled


def _removals_no_bundle_reproduces(repo, bundled):
    """Every delta file ever removed from stream_deltas/ whose exact bytes no bundle holds.

    A delta that HELD_LOOSE has ever named is exempt. Held deltas are never folded, so
    removing one is its owner redacting it, whether its name was dropped from HELD_LOOSE
    before, with or after the removal."""
    # -z: git prints each path raw and NUL-terminated. Without it, git quotes a path with
    # non-ASCII bytes, a quote or a backslash, and a prefix check would silently skip it.
    log = _git("log", "-z", "--diff-filter=D", "--name-only", "--format=%x00%H", "--", DELTAS + "/",
               repo=repo).stdout
    removed, commit = [], None
    for token in log.decode("utf-8").split("\x00"):
        token = token[1:] if token.startswith("\n") else token
        if len(token) in (40, 64) and all(c in "0123456789abcdef" for c in token):
            commit = token
        elif token.startswith(DELTAS + "/frame-") and token.count("/") == 2:
            assert commit, f"{token} precedes any commit in git log output"
            removed.append((commit, token))
    problems, held = [], None
    for (commit, path), original in zip(removed, _blobs(repo, [f"{c}^:{p}" for c, p in removed])):
        assert original is not None, f"{path} before {commit[:9]} is not a file"
        name = path.rsplit("/", 1)[1]
        if name in bundled and repo_dc.delta_file_bytes(bundled[name]) == original:
            continue
        if held is None:
            held = _ever_held(repo)
        if name in held:
            continue
        problems.append(f"{name}, removed in {commit[:9]}, is in no bundle" if name not in bundled
                        else f"the bundled {name} does not reproduce the bytes removed in {commit[:9]}")
    return problems


def test_every_delta_ever_removed_from_stream_deltas_is_still_in_a_bundle():
    try:
        if _git("rev-parse", "--is-shallow-repository").stdout.strip() != b"false":
            pytest.skip("needs full history (fetch-depth: 0)")
    except (OSError, subprocess.CalledProcessError):
        pytest.skip("not a git checkout")
    assert _removals_no_bundle_reproduces(REPO_ROOT, _bundled(repo_dc)) == []


def test_the_history_check_reads_held_loose_as_dream_catcher_assigns_it():
    assert _held_loose_in(DREAM_CATCHER.read_bytes()) == repo_dc.HELD_LOOSE, (
        "the history check reads HELD_LOOSE from past revisions without running them; "
        "keep it a literal frozenset of file names")
    assert _held_loose_in(b"HELD_LOOSE = frozenset()\n") == frozenset()
    assert _held_loose_in(b"HELD_LOOSE: frozenset = frozenset({'a.json'})\n") == {"a.json"}


def _sandbox_git(repo, *args):
    """Run git in a throwaway repository, isolated from any user or system git config."""
    env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
    return subprocess.run(["git", "-C", str(repo), "-c", "user.name=dream-catcher-test",
                           "-c", "user.email=", *args], capture_output=True, check=True, env=env)


def test_a_held_delta_may_be_redacted_and_every_other_removal_stays_bundled(dc, tmp_path, monkeypatch):
    """The owner redacts a held delta by deleting it or editing it in place, and drops its
    name from HELD_LOOSE in the same change or after it (dropping the name first is safe only
    if the redaction lands before the next merge, which would otherwise fold the unredacted
    delta). None of that is a loss; a delta nobody held that is gone from the tree and from
    every bundle is one."""
    source = tmp_path / "rappterpedia" / "dream_catcher.py"
    deleted, edited, late = ("frame-1-review-deleted.json", "frame-1-review-edited.json",
                             "frame-1-review-late.json")

    def hold(*names):
        listed = ", ".join(repr(name) for name in sorted(names))
        source.write_text(f"HELD_LOOSE = frozenset({{{listed}}})\n" if names else
                          "HELD_LOOSE = frozenset()\n", encoding="utf-8")
        monkeypatch.setattr(dc, "HELD_LOOSE", frozenset(names))

    def commit(message):
        _sandbox_git(tmp_path, "add", "-A")
        _sandbox_git(tmp_path, "commit", "-q", "-m", message)
        return _git("rev-parse", "HEAD", repo=tmp_path).stdout.decode().strip()

    _sandbox_git(tmp_path, "init", "-q")
    hold(deleted, edited, late)
    _state(dc, 2)
    for frame, stream in ((1, "alpha"), (1, "review-deleted"), (1, "review-edited"),
                          (1, "review-late"), (2, "alpha"), (3, "alpha")):
        dc.save_json(dc.DELTAS_DIR / f"frame-{frame}-{stream}.json",
                     _delta(frame, stream, articles=[_article(f"{frame}:{stream}", "Quoted tool output")]))
    commit("frames 1 to 3 produced")
    assert dc.fold_merged_deltas()["folded"] == 2
    commit("frame 2 merged: frame-1-alpha and frame-2-alpha fold, the held three stay loose")

    (dc.DELTAS_DIR / deleted).unlink()
    commit("redact a held delta by deleting it")
    hold(edited, late)
    commit("then drop its name")
    dc.save_json(dc.DELTAS_DIR / edited,
                 _delta(1, "review-edited", articles=[_article("1:review-edited", "[redacted]")]))
    hold(late)
    commit("redact a held delta in place and drop its name")
    hold()
    commit("drop a held name first")
    (dc.DELTAS_DIR / late).unlink()
    commit("then delete that delta before any merge")
    assert dc.fold_merged_deltas()["folded"] == 1
    commit("the next merge folds the redacted delta")
    (dc.DELTAS_DIR / "frame-3-alpha.json").unlink()
    lost = commit("a delta nobody held disappears")

    bundled = _bundled(dc)
    assert deleted not in bundled and late not in bundled
    assert bundled[edited]["articles_created"][0]["title"] == "[redacted]"
    assert _removals_no_bundle_reproduces(tmp_path, bundled) == [
        f"frame-3-alpha.json, removed in {lost[:9]}, is in no bundle"]


def test_the_history_check_sees_removed_deltas_whose_names_git_would_quote(tmp_path):
    """git log quotes a path with non-ASCII bytes, a double quote or a backslash unless -z is
    given. Such a name is still a delta name, so losing one must still be reported."""
    names = ("frame-1-plain.json", "frame-1-caf\u00e9.json", 'frame-1-say"hi".json',
             "frame-1-back\\slash.json")
    deltas = tmp_path / DELTAS
    deltas.mkdir(parents=True)
    for name in names:
        (deltas / name).write_text(json.dumps({"frame": 1}, indent=2), encoding="utf-8")
    _sandbox_git(tmp_path, "init", "-q")
    _sandbox_git(tmp_path, "add", "-A")
    _sandbox_git(tmp_path, "commit", "-q", "-m", "four deltas")
    for name in names:
        (deltas / name).unlink()
    _sandbox_git(tmp_path, "add", "-A")
    _sandbox_git(tmp_path, "commit", "-q", "-m", "all four lost")
    lost = _git("rev-parse", "HEAD", repo=tmp_path).stdout.decode().strip()
    assert sorted(_removals_no_bundle_reproduces(tmp_path, {})) == sorted(
        f"{name}, removed in {lost[:9]}, is in no bundle" for name in names)


def test_a_delta_committed_before_its_frame_ran_survives_the_heartbeat(dc, tmp_path):
    """RAR has committed deltas of frames that had not merged yet (66ca6dda2 did it for the
    refill deltas of frames 121-125), and the heartbeat then produced the same names. The old
    heartbeat overwrote the committed delta. With bundles that would leave a name both loose
    and bundled, or a removal that no bundle reproduces, and every later test run red. Now
    one heartbeat run keeps both deltas of each name and merges both."""

    def commit(message):
        _sandbox_git(tmp_path, "add", "-A", "rappterpedia")
        _sandbox_git(tmp_path, "commit", "-q", "-m", message)

    _sandbox_git(tmp_path, "init", "-q")
    _state(dc, 9)
    early = {"alpha": _delta(10, "alpha", articles=[_article("10:early-alpha", "Early alpha")]),
             "refill": _delta(10, "refill", articles=[_article("10:early-refill", "Early refill")])}
    for stream, delta in early.items():
        dc.save_json(dc.DELTAS_DIR / f"frame-10-{stream}.json", delta)
    commit("two deltas of frame 10, committed before frame 10 ran")

    # One heartbeat run for frame 10, step by step as the workflow runs it: a fleet worker
    # produces into its own directory, the merge job collects and merges, then refills.
    inbox = tmp_path / "delta-output"
    dc.save_new_delta(10, "alpha", _delta(10, "alpha", articles=[_article("10:alpha", "Fleet alpha")]),
                      out_dir=inbox / "delta-alpha")
    assert dc.collect_deltas(inbox)["collected"] == {
        str(inbox / "delta-alpha" / "frame-10-alpha.json"): "frame-10-alpha 2.json"}
    dc.merge_deltas(10)
    dc.save_new_delta(10, "refill", _delta(10, "refill", articles=[_article("10:refill", "Refill")]))
    dc.merge_deltas(10)
    commit("frame 10 merged")

    bundled = _bundled(dc)
    assert sorted(bundled) == ["frame-10-alpha 2.json", "frame-10-alpha.json",
                               "frame-10-refill 2.json", "frame-10-refill.json"]
    for stream, delta in early.items():
        assert dc.delta_file_bytes(bundled[f"frame-10-{stream}.json"]) == dc.delta_file_bytes(delta)
    assert _loose(dc) == []
    assert _removals_no_bundle_reproduces(tmp_path, bundled) == []
    assert {a["title"] for a in json.loads(dc.STATE_FILE.read_text())["articles"]} == {
        "Early alpha", "Early refill", "Fleet alpha", "Refill"}


def test_the_heartbeat_ships_each_stream_its_own_delta_and_nothing_else():
    """Before bundles, every fleet worker uploaded the whole stream_deltas/ tree and
    the merge job flattened every *.json it downloaded back into it. With bundles in
    a subdirectory that would copy bundles out of it, and a copy over a delta of the
    same name already on main would overwrite it. So each worker writes the delta it
    produces into its own empty directory and uploads only that file, and the merge
    job collects loose frame deltas with collect, which never overwrites one."""
    yaml = pytest.importorskip("yaml")
    jobs = yaml.safe_load(HEARTBEAT.read_text(encoding="utf-8"))["jobs"]
    produce = next(s for s in jobs["fleet"]["steps"] if "dream_catcher.py produce" in str(s.get("run")))
    assert "--out-dir delta-out" in produce["run"]
    upload = next(s for s in jobs["fleet"]["steps"] if "upload-artifact" in str(s.get("uses")))
    assert upload["with"]["path"] == (
        "delta-out/frame-${{ needs.get-frame.outputs.frame }}-${{ matrix.stream }}.json")
    assert upload["with"]["if-no-files-found"] == "error"
    collect = next(s for s in jobs["merge"]["steps"] if s.get("name") == "Collect deltas into stream_deltas/")
    assert "python rappterpedia/dream_catcher.py collect --from delta-output" in collect["run"]
    assert "cp " not in collect["run"] and "-exec" not in collect["run"]
    commit = next(s for s in jobs["merge"]["steps"] if "git commit" in str(s.get("run")))
    assert "git add rappterpedia/ state/" in commit["run"]
