"""
Stack eggs stay RAPP/1 §9 eggs, and their pack.json receipts stay true.

stacks/microsoft-365-team and stacks/neighborhood-starter each ship a `.egg`
plus a pack.json that records its size and SHA-256. Both eggs were packed with
the ZIP UTF-8 name flag (general-purpose bit 11) clear in every header, which
RAPP/1 §9 rejects, and both receipts still described the bytes the eggs had
before their §9 re-pack. They were re-framed with rapp-1's own `rapp.pack_egg`
from their own manifest values and member bytes, so each egg's §9.1 address is
unchanged (see docs/RAPP1-CONFORMANCE.md for the public reproduction).

The framing test restates only the byte-reproducible ZIP rules these eggs have
broken before. Set RAPP1_CHECKOUT to a kody-w/rapp-1 checkout to run the full
reference `rapp.verify_egg` as well.
"""

import hashlib
import io
import json
import os
import sys
import zipfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
EGGS = sorted(REPO_ROOT.glob("stacks/*/*.egg"))


def test_the_stack_eggs_are_found():
    found = {egg.parent.name for egg in EGGS}
    assert {"microsoft-365-team", "neighborhood-starter"} <= found, found


@pytest.mark.parametrize("egg", EGGS, ids=lambda egg: egg.parent.name)
def test_the_pack_receipt_matches_the_egg_bytes(egg):
    receipt = json.loads((egg.parent / "pack.json").read_text(encoding="utf-8"))["files"][egg.name]
    data = egg.read_bytes()
    assert (receipt["size"], receipt["sha256"]) == (len(data), hashlib.sha256(data).hexdigest())


@pytest.mark.parametrize("egg", EGGS, ids=lambda egg: egg.parent.name)
def test_every_entry_has_rapp1_zip_framing(egg):
    blob = egg.read_bytes()
    with zipfile.ZipFile(io.BytesIO(blob)) as archive:
        infos = archive.infolist()
    assert infos[0].filename == "manifest.json"
    for info in infos:
        local_flags = int.from_bytes(blob[info.header_offset + 6:info.header_offset + 8], "little")
        assert (info.flag_bits, local_flags) == (0x0800, 0x0800), f"{info.filename}: UTF-8 name flag"
        assert info.compress_type == zipfile.ZIP_STORED, f"{info.filename}: stored"
        assert info.date_time == (1980, 1, 1, 0, 0, 0), f"{info.filename}: fixed timestamp"


@pytest.mark.skipif(not os.environ.get("RAPP1_CHECKOUT"), reason="set RAPP1_CHECKOUT to a kody-w/rapp-1 checkout")
@pytest.mark.parametrize("egg", EGGS, ids=lambda egg: egg.parent.name)
def test_the_rapp1_reference_verifies_the_egg(egg, monkeypatch):
    monkeypatch.setattr(sys, "dont_write_bytecode", True)
    monkeypatch.syspath_prepend(str(Path(os.environ["RAPP1_CHECKOUT"]).resolve()))
    import rapp

    assert rapp.verify_egg(egg.read_bytes()) == (True, None, "ok")
