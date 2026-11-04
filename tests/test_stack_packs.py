"""Stack packs: stacks/<name>/pack.json projected into registry.json with a summon seed.

Contract:
  * additive and read-only: hash drift never fails the build, never edits a pack;
  * `_verified` is true only when every listed file exists and matches its sha256;
  * an optional `kernel` pin (a distro's pinned kernel) passes through untouched;
  * seeds come from the permanent forge and never collide with an agent seed;
  * s.html, the scan-to-summon landing page, is self-contained and never installs.
"""
import hashlib
import json
import re
from pathlib import Path

import build_registry

ROOT = Path(__file__).resolve().parent.parent


def _pack(tmp, name, files, kernel=None, corrupt=None):
    d = tmp / name
    d.mkdir(parents=True)
    listed = {}
    for fname, body in files.items():
        (d / fname).write_bytes(body)
        listed[fname] = {"sha256": hashlib.sha256(body).hexdigest()}
    if corrupt:
        (d / corrupt).write_bytes(b"changed after the pack was written\n")
    pack = {"schema": "rapp-rar-stack/1.0", "name": name, "display_name": name.title(),
            "version": "1.0.0", "purpose": "p" * 400, "files": listed}
    if kernel:
        pack["kernel"] = kernel
    (d / "pack.json").write_text(json.dumps(pack))


def test_verified_pack_and_fields(tmp_path):
    _pack(tmp_path, "good", {"a_agent.py": b"x = 1\n", "b.egg": b"egg"})
    [p] = build_registry.build_stack_packs(set(), tmp_path)
    assert p["_verified"] is True
    assert p["files"]["a_agent.py"]["verified"] is True
    assert len(p["purpose"]) == 300
    assert isinstance(p["_seed"], int)
    assert "kernel" not in p


def test_changed_file_is_unverified_not_an_error(tmp_path):
    _pack(tmp_path, "stale", {"a_agent.py": b"x = 1\n"}, corrupt="a_agent.py")
    [p] = build_registry.build_stack_packs(set(), tmp_path)
    assert p["_verified"] is False
    assert p["files"]["a_agent.py"]["verified"] is False


def test_missing_file_is_unverified(tmp_path):
    _pack(tmp_path, "gone", {"a_agent.py": b"x = 1\n"})
    (tmp_path / "gone" / "a_agent.py").unlink()
    [p] = build_registry.build_stack_packs(set(), tmp_path)
    assert p["_verified"] is False


def test_kernel_pin_passes_through(tmp_path):
    pin = {"repo": "example/kernel", "sha256": "0" * 64}
    _pack(tmp_path, "distro", {"a_agent.py": b"x\n"}, kernel=pin)
    [p] = build_registry.build_stack_packs(set(), tmp_path)
    assert p["kernel"] == pin


def test_seed_is_stable_and_collisions_are_withheld(tmp_path):
    _pack(tmp_path, "one", {"a_agent.py": b"x\n"})
    [first] = build_registry.build_stack_packs(set(), tmp_path)
    [again] = build_registry.build_stack_packs(set(), tmp_path)
    assert first["_seed"] == again["_seed"]
    [blocked] = build_registry.build_stack_packs({first["_seed"]}, tmp_path)
    assert "_seed" not in blocked


def test_pack_files_are_never_modified(tmp_path):
    _pack(tmp_path, "ro", {"a_agent.py": b"x\n"}, corrupt="a_agent.py")
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    build_registry.build_stack_packs(set(), tmp_path)
    after = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    assert before == after


def test_published_registry_stack_seeds_are_unique():
    reg = json.loads((ROOT / "registry.json").read_text())
    agent_seeds = {a["_seed"] for a in reg["agents"] if "_seed" in a}
    pack_seeds = [p["_seed"] for p in reg.get("stack_packs", []) if "_seed" in p]
    assert len(pack_seeds) == len(set(pack_seeds))
    assert not agent_seeds & set(pack_seeds)


def test_summon_page_is_self_contained_and_never_installs():
    page = (ROOT / "s.html").read_text()
    assert not re.search(r"<script[^>]+src=", page), "no external scripts"
    assert "<link" not in page, "no external stylesheets"
    assert "/agents/import" not in page, "the page never talks to a kernel directly"
    assert "_verified" in page and "notarized" in page, "unverified cards cannot be summoned"


def test_summon_page_never_parses_seeds_as_numbers():
    """A 64-bit seed loses precision as a JS number; the page must quote seeds before JSON.parse."""
    page = (ROOT / "s.html").read_text()
    assert "r.json()" not in page
    assert "parseExact" in page and '"_seed"' in page


def test_stack_chant_round_trips_to_its_seed(tmp_path):
    from rapp_sdk import words_to_seed
    _pack(tmp_path, "chanted", {"a_agent.py": b"x\n"})
    [p] = build_registry.build_stack_packs(set(), tmp_path)
    assert len(p["_incantation"].split()) == 7
    assert words_to_seed(p["_incantation"]) == p["_seed"]


def test_summon_page_decodes_chants_from_the_one_word_list():
    page = (ROOT / "s.html").read_text()
    assert 'fetch("rapp_sdk.py"' in page and "MNEMONIC_WORDS" in page, "no second copy of the word list"
    assert "BigInt" in page, "64-bit seeds must be decoded exactly"


def test_distros_page_draws_qr_locally_with_integrity_and_exact_seeds():
    page = (ROOT / "distros.html").read_text()
    assert 'integrity="sha384-' in page, "the QR library must be pinned with Subresource Integrity"
    assert "qrserver" not in page and "chart.googleapis" not in page, "never send links to a QR service"
    assert "parseExact" in page and "r.json()" not in page, "64-bit seeds read as text"
    assert "_verified === true" in page, "unverified stacks get no QR"


def test_chant_share_sheet_speaks_then_summons_verified_only():
    page = (ROOT / "chants.html").read_text()
    assert "speechSynthesis" in page and "SpeechSynthesisUtterance" in page, "says the chant out loud"
    assert 's.html#chant=' in page, "hands off to the summon page with the chant seeded"
    assert "_verified === true" in page, "only verified distros are listed"
    assert "setTimeout(finish" in page, "never hangs if the phone skips the speech end event"
    assert "parseExact" in page and "r.json()" not in page
