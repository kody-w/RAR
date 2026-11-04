"""Retirement steers discovery without unpublishing a pack or changing its pins."""
import json
import shutil
import subprocess
from pathlib import Path

import pytest

import build_registry

ROOT = Path(__file__).resolve().parent.parent
RETIRED = {
    "since": "2026-11-04",
    "reason": "Template generator; use the existing agent.",
    "replacement": "@kody-w/vibe_coding_loop",
}


def _pack(root, name, **fields):
    directory = root / name
    directory.mkdir()
    pack = {"name": name, "files": {}, **fields}
    path = directory / "pack.json"
    path.write_text(json.dumps(pack))
    return path


def test_retirement_passes_through_without_changing_pins_or_bytes(tmp_path):
    path = _pack(tmp_path, "old")
    [before] = build_registry.build_stack_packs(set(), tmp_path)
    pack = json.loads(path.read_text())
    pack.update(status="retired", retired=RETIRED)
    path.write_text(json.dumps(pack))
    raw = path.read_bytes()
    [after] = build_registry.build_stack_packs(set(), tmp_path)
    assert before["status"] == "current"
    assert after["status"] == "retired"
    assert after["retired"] == RETIRED
    assert {k: v for k, v in after.items() if k not in ("status", "retired")} == {
        k: v for k, v in before.items() if k != "status"
    }
    assert path.read_bytes() == raw


@pytest.mark.parametrize("retirement", [
    None,
    {**RETIRED, "since": "2026-02-30"},
    {**RETIRED, "since": "November 4"},
    {**RETIRED, "reason": " "},
    {**RETIRED, "replacement": 42},
    {k: v for k, v in RETIRED.items() if k != "replacement"},
])
def test_invalid_retirement_fails_the_builder(tmp_path, retirement):
    _pack(tmp_path, "old", status="retired", retired=retirement)
    with pytest.raises(ValueError, match="old:"):
        build_registry.build_stack_packs(set(), tmp_path)


def test_null_replacement_is_valid(tmp_path):
    _pack(tmp_path, "old", status="retired", retired={**RETIRED, "replacement": None})
    [pack] = build_registry.build_stack_packs(set(), tmp_path)
    assert pack["retired"]["replacement"] is None


@pytest.mark.parametrize("fields", [
    {"status": "deleted"},
    {"retired": RETIRED},
])
def test_inconsistent_status_is_rejected(tmp_path, fields):
    _pack(tmp_path, "old", **fields)
    with pytest.raises(ValueError, match="old:"):
        build_registry.build_stack_packs(set(), tmp_path)


@pytest.mark.parametrize("name,extra", [
    ("starter-test", {}),
    ("custom-starter", {"shelf": "starter"}),
])
@pytest.mark.parametrize("transitive", [False, True])
def test_starter_cannot_include_retired_pack(tmp_path, name, extra, transitive):
    _pack(tmp_path, "old", status="retired", retired=RETIRED)
    includes = ["old"]
    if transitive:
        _pack(tmp_path, "bridge", install={"includes": includes})
        includes = ["bridge"]
    _pack(tmp_path, name, install={"includes": includes}, **extra)
    with pytest.raises(ValueError, match=f"{name}: install.includes reaches retired pack:"):
        build_registry.build_stack_packs(set(), tmp_path)


def test_current_includes_and_cycles_still_build(tmp_path):
    _pack(tmp_path, "starter-test", install={"includes": ["current"]})
    _pack(tmp_path, "current", install={"includes": ["starter-test"]})
    assert len(build_registry.build_stack_packs(set(), tmp_path)) == 2


def test_retired_starter_cannot_include_itself(tmp_path):
    _pack(tmp_path, "starter-old", status="retired", retired=RETIRED,
          install={"includes": ["starter-old"]})
    with pytest.raises(ValueError, match="install.includes reaches retired pack"):
        build_registry.build_stack_packs(set(), tmp_path)


@pytest.mark.parametrize("name,replacement", [
    ("vibe-coding-loop", "@kody-w/vibe_coding_loop"),
    ("inheritance", None),
    ("wildhaven-hearth", "starter-personal"),
])
def test_published_catalog_retains_all_packs_and_retirement_metadata(name, replacement):
    registry = json.loads((ROOT / "registry.json").read_text())
    catalog = json.loads((ROOT / "api/v1/catalog.json").read_text())
    assert catalog["stack_packs"] == registry["stack_packs"]
    retired = next(p for p in catalog["stack_packs"] if p["name"] == name)
    assert retired["status"] == "retired"
    assert retired["retired"]["replacement"] == replacement
    assert retired["_verified"] is True


def test_personal_starter_no_longer_promises_or_includes_succession():
    pack = json.loads((ROOT / "stacks/starter-personal/pack.json").read_text())
    assert pack["version"] == "1.2.1"
    assert "inheritance" not in pack["install"]["includes"]
    assert "inherits" not in pack["purpose"]
    packs = {
        p.parent.name: json.loads(p.read_text())
        for p in (ROOT / "stacks").glob("*/pack.json")
    }
    build_registry.validate_stack_pack_status(packs)


def _node(script):
    if not shutil.which("node"):
        pytest.skip("node is not installed")
    result = subprocess.run(["node", "-e", script], capture_output=True, text=True, timeout=15)
    assert result.returncode == 0, result.stderr


def test_distros_hide_retired_by_default_and_toggle_counts_and_cards():
    page = (ROOT / "distros.html").read_text()
    js = page[page.index('  var shelf = "all"'):page.index('  fetch("registry.json"')]
    _node("""
const assert = require('node:assert/strict');
function element() {
  return {innerHTML: '', children: [], appendChild(x) { this.children.push(x); },
          querySelectorAll() { return []; }};
}
const elements = {shelves: element(), list: element(), pager: element()};
const document = {
  getElementById(id) { return elements[id]; },
  createElement() {
    const el = element(), input = {};
    el.querySelector = () => input;
    return el;
  }
};
const packs = [
  {name: 'current', shelf: 'pack'},
  {name: 'old', shelf: 'app', status: 'retired'}
];
let page = 1;
const PER_PAGE = 9, cardFor = p => p.name;
""" + js + """
render();
assert.deepEqual(elements.list.children, ['current']);
assert.match(elements.shelves.innerHTML, /Everything \\(1\\)/);
assert.match(elements.shelves.children[0].innerHTML, /Show retired \\(1\\)/);
elements.list.children = [];
elements.shelves.children[0].querySelector('input').onchange({target: {checked: true}});
assert.deepEqual(elements.list.children, ['current', 'old']);
assert.match(elements.shelves.innerHTML, /Everything \\(2\\)/);
elements.list.children = [];
elements.shelves.children.at(-1).querySelector('input').onchange({target: {checked: false}});
assert.deepEqual(elements.list.children, ['current']);
""")


def test_store_installable_packs_hide_retired_until_toggle():
    page = (ROOT / "store.html").read_text()
    js = page[page.index("let installablePacks = []"):page.index("function buildVerticalPacks(reg)")]
    _node("""
const assert = require('node:assert/strict');
const elements = Object.fromEntries(
  ['installable-packs', 'store-retired-toggle', 'store-retired-count', 'store-show-retired']
  .map(id => [id, {checked: false}]));
const document = {getElementById: id => elements[id]};
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
""" + js + f"""
installablePacks = [
  {{name: 'current', display_name: 'Current'}},
  {{name: 'old', display_name: 'Old pack', status: 'retired', retired: {json.dumps(RETIRED)}}}
];
renderInstallablePacks();
assert.doesNotMatch(elements['installable-packs'].innerHTML, /Old pack/);
assert.equal(elements['store-retired-count'].textContent, 1);
assert.equal(elements['store-retired-toggle'].hidden, false);
elements['store-show-retired'].checked = true;
renderInstallablePacks();
assert.match(elements['installable-packs'].innerHTML, /Old pack \\(retired\\)/);
assert.match(elements['installable-packs'].innerHTML, /@kody-w\\/vibe_coding_loop/);
""")
