#!/usr/bin/env python3
"""Build incubator/index.json: the RAPP egg incubator (rapp-static-api/1.0).

    python3 incubator/build_incubator.py           rebuild index.json
    python3 incubator/build_incubator.py --check   fail if index.json is stale, an egg fails rapp/1 verify,
                                                   or a published egg file was changed (eggs are append-only)

Input: one hand-written entries/<slug>.json per egg. Each points at an egg stored once under eggs/<slug>/<sha12>.egg,
named by the first 12 hex characters of its SHA-256. The build verifies every egg with rapp/1's own reference code
(tools/rapp.py, vendored at a pinned commit), reads its manifest, and writes the index. Stable-write: the
`generated` time only changes when something else did.
"""
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = "https://raw.githubusercontent.com/kody-w/RAR/main/incubator/"
PAGES = "https://kody-w.github.io/RAR/incubator/"
REQUIRED = ("slug", "title", "description", "author", "egg")


def load_rapp():
    spec = importlib.util.spec_from_file_location("rapp", HERE / "tools" / "rapp.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build():
    rapp = load_rapp()
    problems, eggs = [], []
    for path in sorted((HERE / "entries").glob("*.json")):
        try:
            entry = json.loads(path.read_text())
        except ValueError as exc:
            problems.append(f"{path.name}: not valid JSON ({exc})")
            continue
        missing = [k for k in REQUIRED if not entry.get(k)]
        if missing:
            problems.append(f"{path.name}: missing {', '.join(missing)}")
            continue
        if entry["slug"] != path.stem:
            problems.append(f"{path.name}: slug must equal the file name")
        egg_path = (HERE / entry["egg"]).resolve()
        if HERE.resolve() not in egg_path.parents or not egg_path.is_file():
            problems.append(f"{path.name}: egg {entry['egg']} not found inside incubator/")
            continue
        blob = egg_path.read_bytes()
        sha = hashlib.sha256(blob).hexdigest()
        if egg_path.stem != sha[:12]:
            problems.append(f"{entry['egg']}: file name must be the first 12 hex of its SHA-256 ({sha[:12]})")
        ok, step, why = rapp.verify_egg(blob)
        if not ok:
            problems.append(f"{entry['egg']}: fails rapp/1 egg verify ({step}): {why}")
            continue
        manifest, _ = rapp.read_egg(blob)
        payload = manifest.get("payload") or {}
        eggs.append({
            "slug": entry["slug"], "title": entry["title"], "description": entry["description"],
            "author": entry["author"], "tags": entry.get("tags", []),
            "style": payload.get("style", "playful"),
            "variant": manifest["variant"], "address": rapp.egg_address(manifest), "rappid": manifest["rappid"],
            "sha256": sha, "size": len(blob), "files": len(manifest["contents"]),
            "kernel": (payload.get("kernel") or {}).get("version"),
            "rules": (payload.get("rules") or {}).get("revision"),
            "path": entry["egg"], "raw": RAW + entry["egg"], "url": PAGES + entry["egg"],
        })
    return eggs, problems


def main():
    check = "--check" in sys.argv
    eggs, problems = build()
    out = HERE / "index.json"
    old = json.loads(out.read_text()) if out.exists() else {}
    index = {"schema": "rapp-incubator/1.0", "spec": "rapp-static-api/1.0",
             "generated": old.get("generated") or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
             "raw_base": RAW, "pages_base": PAGES,
             "summary": {"eggs": len(eggs), "problems": len(problems)}, "eggs": eggs}
    if {k: v for k, v in index.items() if k != "generated"} != {k: v for k, v in old.items() if k != "generated"}:
        index["generated"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    text = json.dumps(index, indent=2) + "\n"
    if check:
        # Append-only: every egg file the old index named must still exist, byte for byte.
        for e in old.get("eggs", []):
            p = HERE / e["path"]
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != e["sha256"]:
                problems.append(f"{e['path']}: a published egg was changed or removed; eggs are append-only")
        if out.read_text() != text if out.exists() else True:
            problems.append("index.json is stale: run python3 incubator/build_incubator.py and commit it")
        for p in problems:
            print("FAIL", p)
        print(f"{len(eggs)} egg(s), {len(problems)} problem(s)")
        sys.exit(1 if problems else 0)
    for p in problems:
        print("FAIL", p)
    out.write_text(text)
    print(f"index.json: {len(eggs)} egg(s), {len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
