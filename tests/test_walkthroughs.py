"""Walkthroughs stack: every walkthrough passes the SDK check, and the check refuses bad ones."""
import importlib.util, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("walkthrough", ROOT / "stacks/walkthroughs/walkthrough.py")
wt = importlib.util.module_from_spec(spec); spec.loader.exec_module(wt)

def test_every_walkthrough_passes():
    files = sorted((ROOT / "stacks/walkthroughs/walkthroughs").glob("*.json"))
    assert files
    for f in files:
        errs, _ = wt.check(f)
        assert not errs, (f.name, errs)

def _bad(tmp_path, change):
    d = json.loads((ROOT / "stacks/walkthroughs/walkthroughs/brainstem-skill.json").read_text())
    change(d); p = tmp_path / "brainstem-skill.json"; p.write_text(json.dumps(d)); return wt.check(p)

def test_refuses_unknown_keys(tmp_path):
    errs, _ = _bad(tmp_path, lambda d: d["steps"][0].update(html="<script>"))
    assert any("unknown keys" in e for e in errs)

def test_refuses_not_simulated(tmp_path):
    errs, _ = _bad(tmp_path, lambda d: d.update(simulated=False))
    assert any("simulated" in e for e in errs)

def test_stale_pin_is_a_warning(tmp_path):
    errs, warns = _bad(tmp_path, lambda d: d["shows"].update(sha256="0" * 64))
    assert not errs and any("out of date" in w for w in warns)
