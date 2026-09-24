#!/usr/bin/env python3
"""Build the static RAR Eggs catalog: whole brainstems, one file each (Article XXVI).

Canonical eggs live at ``eggs/@owner/<slug>.egg``. Each is a rapp/1 ``organism``
egg (RAPP SPEC §9): a brainstem's agents, soul and optional memory, plus the engine
version it expects. Eggs are read and verified with the RAPP reference
implementation (``scripts/rapp1.py``, vendored verbatim; see ``rapp1.vendor.json``),
never executed.

Registry policy on top of the spec:
  * variant ``organism`` only;
  * the path must match the egg's rappid: ``eggs/@<owner>/<slug>.egg``;
  * no engine code: no root-level ``.py`` file (an egg hatches onto the
    receiver's own engine), and no sign-in or secret files anywhere;
  * at most 5 MiB.

Writes ``api/v1/eggs.json``. ``--check`` verifies without writing and exits 1 on
any violation, so a pull request carrying a bad egg fails CI.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EGGS_DIR = REPO_ROOT / "eggs"
OUTPUT = REPO_ROOT / "api" / "v1" / "eggs.json"
VENDOR = Path(__file__).resolve().parent / "rapp1.vendor.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rapp1  # noqa: E402

CATALOG_SCHEMA = "rar-eggs-catalog/1.0"
MAX_BYTES = 5 * 1024 * 1024
FORBIDDEN_NAMES = {".env", ".copilot_token", ".copilot_session", ".copilot_pending", ".brainstem_secret"}
RAW_BASE = "https://raw.githubusercontent.com/kody-w/RAR/main/"


def _sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _soul_summary(soul: bytes) -> str:
    for line in soul.decode("utf-8", errors="replace").splitlines():
        line = line.strip().lstrip("#").strip()
        if line:
            return line[:200]
    return ""


def check_egg(path: Path) -> tuple[dict | None, list[str]]:
    """Return (catalog entry, problems). An entry is only returned when there are no problems."""
    rel = path.relative_to(REPO_ROOT).as_posix()
    blob = path.read_bytes()
    if len(blob) > MAX_BYTES:
        return None, [f"{rel}: {len(blob)} bytes is over the {MAX_BYTES}-byte limit"]
    ok, step, why = rapp1.verify_egg(blob)
    if not ok:
        return None, [f"{rel}: fails RAPP egg verification at {step}: {why}"]
    manifest, files = rapp1.read_egg(blob)
    problems = []
    if manifest["variant"] != "organism":
        problems.append(f"{rel}: variant is {manifest['variant']!r}; only 'organism' eggs are listed")
    parts = rapp1.rappid_parts(manifest["rappid"])
    expected = f"eggs/@{parts['owner']}/{parts['slug']}.egg"
    if rel != expected:
        problems.append(f"{rel}: path must match the egg's rappid ({expected})")
    for name in files:
        segments = name.split("/")
        if len(segments) == 1 and name.endswith(".py"):
            problems.append(f"{rel}: carries engine code ({name}); eggs hatch onto the receiver's engine")
        if segments[-1] in FORBIDDEN_NAMES:
            problems.append(f"{rel}: carries a sign-in or secret file ({name})")
    if problems:
        return None, problems

    payload = manifest.get("payload") or {}
    engine = payload.get("engine") if isinstance(payload.get("engine"), dict) else {}
    agents = sorted(
        name.split("/", 1)[1] for name in files
        if name.startswith("agents/") and name.count("/") == 1
        and name.endswith("_agent.py") and name != "agents/basic_agent.py"
    )
    settings = payload.get("settings_needed")
    return {
        "name": f"@{parts['owner']}/{parts['slug']}",
        "rappid": manifest["rappid"],
        "egg_address": rapp1.egg_address(manifest),
        "variant": manifest["variant"],
        "created_utc": manifest["created_utc"],
        "file": rel,
        "url": RAW_BASE + rel,
        "sha256": _sha256(blob),
        "size_bytes": len(blob),
        "soul_summary": _soul_summary(files["soul.md"]),
        "agents": agents,
        "files": len(files),
        "memory_included": any(n.startswith(".brainstem_data/") for n in files),
        "engine": {k: engine.get(k, "") for k in ("name", "version", "source", "commit")},
        "settings_needed": sorted(s for s in settings if isinstance(s, str)) if isinstance(settings, list) else [],
        "signed": manifest["sig"] is not None,
        "hatch": f"python3 -m brainfreeze up --egg {RAW_BASE + rel}",
    }, []


def build() -> tuple[dict, list[str]]:
    entries, problems = [], []
    paths = sorted(EGGS_DIR.glob("**/*.egg")) if EGGS_DIR.is_dir() else []
    for path in paths:
        entry, why = check_egg(path)
        problems += why
        if entry:
            entries.append(entry)
    vendor = json.loads(VENDOR.read_text())
    catalog = {
        "schema": CATALOG_SCHEMA,
        "artifact_type": "egg-catalog",
        "description": ("Static catalog of whole brainstems published as rapp/1 organism eggs: agents, soul "
                        "and optional memory, with the engine version they expect and never engine code. "
                        "One file, one brainstem. Hatch one onto your own engine with brainfreeze."),
        "hashing": {"files": "sha256", "egg": "rapp/1:egg-manifest"},
        "inputs": {
            "eggs": _sha256(json.dumps([[e["file"], e["sha256"]] for e in entries]).encode()),
            "rapp1": {"commit": vendor["commit"], "sha256": vendor["sha256"]},
        },
        "counts": {"total": len(entries)},
        "self_url": RAW_BASE + "api/v1/eggs.json",
        "hatch_tool": "https://github.com/kody-w/rapp-brainfreeze",
        "eggs": entries,
    }
    return catalog, problems


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="verify only; do not write api/v1/eggs.json")
    args = ap.parse_args(argv)

    vendor = json.loads(VENDOR.read_text())
    actual = _sha256((Path(__file__).resolve().parent / "rapp1.py").read_bytes())
    if actual != vendor["sha256"]:
        print(f"scripts/rapp1.py was edited (sha256 {actual}); it must stay a verbatim copy", file=sys.stderr)
        return 1

    catalog, problems = build()
    for p in problems:
        print(f"egg rejected: {p}", file=sys.stderr)
    if problems:
        return 1
    if not args.check:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(json.dumps(catalog, indent=2, sort_keys=False) + "\n")
    print(f"eggs: {catalog['counts']['total']} verified" + ("" if args.check else f" -> {OUTPUT.relative_to(REPO_ROOT)}"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
