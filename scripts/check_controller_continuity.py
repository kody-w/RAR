#!/usr/bin/env python3
"""Fail if a namespace changes hands without it being noticed.

registry.json records `_controller.github_id` for 200 of its 202 entries. That
number is GitHub's immutable account id: it survives a rename, and a different
person can never obtain it. It is exactly the signal that would have caught
event-stream in 2018, where a package was handed to a new maintainer who then
shipped a backdoor — the name and the repo looked identical throughout.

Nothing in this repository has ever compared that field between two builds.
This does, on every push.

Two distinct events, deliberately reported differently:

  RENAME   same github_id, different login. Normal and allowed — people rename
           themselves. Reported so it is on the record, never fatal.

  HANDOVER different github_id under a namespace that already existed. This is
           the account-takeover / package-transfer shape, and it is fatal. If a
           handover is legitimate, record it in scripts/controller-handovers.json
           with a reason; that turns an alarm into a decision someone signed.
"""
import json
import argparse
import subprocess
import sys
from pathlib import Path


def entries(blob):
    d = json.loads(blob)
    e = d.get("agents") or d.get("entries") or (d if isinstance(d, list) else [])
    if isinstance(e, dict):
        e = list(e.values())
    out = {}
    for x in e:
        if not isinstance(x, dict):
            continue
        ns = (x.get("namespace") or str(x.get("name") or x.get("id") or "")
              .split("/")[0]).lstrip("@")
        c = x.get("_controller") or {}
        if ns and c.get("github_id"):
            out.setdefault(ns, (c["github_id"], c.get("github_login")))
    return out


def previous(repo_root: Path, path="registry.json", ref="HEAD~1"):
    r = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    return r.stdout if r.returncode == 0 else None


def main(repo_root: Path = Path("."), base: str = "HEAD~1"):
    repo_root = repo_root.resolve()
    cur_raw = (repo_root / "registry.json").read_text(encoding="utf-8")
    prev_raw = previous(repo_root, ref=base)
    if not prev_raw:
        print("  no previous registry.json to compare against — recording only")
        return 0
    cur, prev = entries(cur_raw), entries(prev_raw)

    allowed = {}
    p = repo_root / "scripts" / "controller-handovers.json"
    if p.is_file():
        allowed = json.loads(p.read_text(encoding="utf-8")).get(
            "handovers",
            {},
        )

    renames, handovers = [], []
    for ns, (gid, login) in sorted(cur.items()):
        if ns not in prev:
            continue                      # a brand-new namespace is not a handover
        old_gid, old_login = prev[ns]
        if gid != old_gid:
            handovers.append((ns, old_gid, old_login, gid, login))
        elif login != old_login:
            renames.append((ns, old_login, login))

    for ns, a, b in renames:
        print(f"  RENAME    @{ns}: {a} -> {b} (same account id — allowed)")

    fatal = []
    for ns, og, ol, ng, nl in handovers:
        ok = allowed.get(ns)
        if ok and int(ok.get("to_github_id", -1)) == int(ng):
            print(f"  HANDOVER  @{ns}: {ol}({og}) -> {nl}({ng}) — "
                  f"recorded: {ok.get('reason','no reason given')}")
        else:
            fatal.append((ns, og, ol, ng, nl))

    for ns, og, ol, ng, nl in fatal:
        print(f"::error::@{ns} changed controller: {ol} (id {og}) -> "
              f"{nl} (id {ng}). A different account now publishes under an "
              f"existing namespace. If this is intended, add it to "
              f"scripts/controller-handovers.json with a reason.")
    if fatal:
        return 1
    print(f"  controller continuity intact across {len(cur)} namespace(s)"
          + (f"; {len(renames)} rename(s)" if renames else ""))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--base", default="HEAD~1")
    args = parser.parse_args()
    sys.exit(main(args.repo_root, args.base))
