#!/usr/bin/env python3
"""Keep every declared copy equal to its source.

A stack file whose pack entry names a `source` claims to be that catalog file, byte for
byte (tests/test_stack_pack_drift.py holds it to that). When the notary changes the
source, this refreshes the copy and re-signs its pack entry in the same commit, so the
claim stays true. One input (pack.json `source` entries) -> the copies. Idempotent.

    python scripts/sync_declared_copies.py          # refresh
    python scripts/sync_declared_copies.py --check  # exit 1 if any copy drifted
    python scripts/sync_declared_copies.py --list   # every declared copy's path, for `git add`
"""
import hashlib
import json
import sys
from pathlib import Path


def sync(root=Path("."), write=True):
    changed = []
    for pack in sorted((root / "stacks").glob("*/pack.json")):
        text = pack.read_text(encoding="utf-8")
        files = json.loads(text).get("files") or {}
        for name, meta in files.items():
            src = root / (meta.get("source") or "")
            copy = pack.parent / name
            if not meta.get("source") or not src.is_file() or not copy.is_file():
                continue
            body = src.read_bytes()
            if copy.read_bytes() == body:
                continue
            changed.append(f"{pack.parent.name}/{name}")
            if not write:
                continue
            old = copy.read_bytes()
            copy.write_bytes(body)
            # re-sign in place: swap only this entry's sha256 and size, keep the file's own formatting
            text = text.replace(meta["sha256"], hashlib.sha256(body).hexdigest())
            if "size" in meta:
                text = text.replace(f'"size": {len(old)}', f'"size": {len(body)}', 1) \
                    if meta["size"] == len(old) else text
            pack.write_text(text, encoding="utf-8")
    return changed


def declared(root=Path(".")):
    out = []
    for pack in sorted((root / "stacks").glob("*/pack.json")):
        for name, meta in (json.loads(pack.read_text(encoding="utf-8")).get("files") or {}).items():
            if meta.get("source") and (pack.parent / name).is_file():
                out.append(str((pack.parent / name).relative_to(root)))
    return out


if __name__ == "__main__":
    if "--list" in sys.argv[1:]:
        print(" ".join(declared()))
        sys.exit(0)
    check = "--check" in sys.argv[1:]
    drifted = sync(write=not check)
    for d in drifted:
        print(("drifted: " if check else "refreshed: ") + d)
    sys.exit(1 if check and drifted else 0)
